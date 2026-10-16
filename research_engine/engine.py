"""Evidence-aware research search, trajectory reconstruction and question tracing.

Read-only. The engine does not infer historical steps or causal connections.
"""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any

from .store import ResearchStore

TOKEN = re.compile(r"[^\W_]{2,}", re.UNICODE)
HISTORICAL_EVIDENCE = {"documented", "verified"}
OUTCOME_KINDS = {"outcome", "principle"}
CAUSAL_PREDICATES = {
    "raised_question", "pivoted_to", "triggered_by", "motivated_by", "tested_by",
    "informed_by", "produced_evidence", "challenged_assumption", "revised_belief",
    "abandoned_because", "failed_because", "blocked_by", "ruled_out_by",
    "refuted_assumption", "supported_assumption"
}


def tokens(text: str) -> list[str]:
    return TOKEN.findall(text.casefold())


def iso_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid timestamp: {value}") from exc
    if result.tzinfo is None:
        raise ValueError(f"Timezone missing: {value}")
    return result.astimezone(timezone.utc)


def provenance(record: dict) -> dict:
    return record.get("provenance") or {"evidence_status": "unknown", "source_refs": []}


def status(record: dict) -> str:
    return provenance(record).get("evidence_status", "unknown")


def origin(record: dict) -> str:
    return record.get("origin", "unknown")


def public_passage(passage: dict, source: dict) -> bool:
    """Never expose an excerpt lacking explicit permission to reproduce it."""
    if passage.get("usage_status") == "original_analysis":
        return True
    return (passage.get("usage_status") == "licensed_excerpt"
            and source.get("license_status") == "permitted")


class ResearchRetrievalEngine:
    def __init__(self, store: ResearchStore):
        self.store = store

    def search(self, query: str, *, kinds: list[str] | None = None,
               filters: dict | None = None, limit: int = 20) -> dict:
        """Deterministic lexical/structured search. No semantic match is claimed."""
        if not 1 <= limit <= 100:
            raise ValueError("limit must be 1..100")
        filters = filters or {}
        allowed_filters = {"case_id", "publisher", "domain", "case_kind", "source_id"}
        if set(filters) - allowed_filters:
            raise ValueError(f"Unknown search filters: {sorted(set(filters)-allowed_filters)}")
        selected = kinds or ["sources", "cases", "events", "passages", "systems",
                             "environments", "findings", "mechanisms"]
        if set(selected) - set(self.store.registries):
            raise ValueError("Unknown entity type")
        query_tokens = tokens(query)
        if not query_tokens and not filters:
            raise ValueError("Supply search terms or a structured filter")
        documents = []
        for kind in selected:
            for record in self.store.registries[kind]:
                if not self._matches_filters(kind, record, filters):
                    continue
                if kind == "passages":
                    source = self.store.get(record["source_ref"], "sources")
                    if not public_passage(record, source):
                        continue
                fields = self._searchable_fields(kind, record)
                field_text = " ".join(fields)
                corpus_tokens = tokens(field_text)
                if query_tokens and not any(t in corpus_tokens for t in query_tokens):
                    continue
                documents.append((kind, record, fields, corpus_tokens))
        # Local corpus IDF and weighted textual match; do not present as semantic retrieval.
        counts = Counter(t for _, _, _, ts in documents for t in set(ts))
        output = []
        for kind, record, fields, corpus_tokens in documents:
            words = Counter(corpus_tokens)
            if query_tokens:
                score = sum((1 + math.log(1 + len(documents)/(1+counts.get(t, 0))))
                            * (2 if t in tokens(fields[0]) else 1)
                            * min(words.get(t, 0), 3)
                            for t in set(query_tokens))
                score += 2 * (query.casefold() in fields[0].casefold())
            else:
                score = 0
            snippet = next((value for value in fields if any(t in tokens(value) for t in query_tokens)),
                           fields[0] if fields else "")
            result = {"id": record["id"], "entity_type": kind, "score": round(score, 5),
                      "snippet": snippet[:350]}
            if kind == "passages":
                result.update({"source_ref": record["source_ref"],
                               "locator": record["locator"], "usage_status": record["usage_status"]})
            if kind == "sources":
                result["url"] = record["url"]
            if kind == "events":
                result.update({"case_ref": record["case_ref"],
                               "evidence_status": status(record), "origin": origin(record)})
            output.append(result)
        output.sort(key=lambda r: (-r["score"], r["entity_type"], r["id"]))
        return {"query": query, "search_type": "deterministic_lexical",
                "filters": filters, "total_matches": len(output), "results": output[:limit],
                "limitations": ["No semantic similarity is inferred; uncovered sources may match after RAW acquisition."]}

    def _case_ids(self, kind: str, record: dict) -> set[str]:
        if kind == "cases":
            return {record["id"]}
        if kind in ("events", "contexts"):
            return {record["case_ref"]}
        if kind == "passages":
            return set(self.store.get(record["source_ref"], "sources").get("case_refs", []))
        if kind == "sources":
            return set(record.get("case_refs", []))
        if kind == "findings":
            return set(record.get("case_refs", []))
        return {case["id"] for case in self.store.registries["cases"] if (
            record["id"] in case.get("system_refs", []) or
            record["id"] in case.get("environment_refs", []) or
            record["id"] in case.get("mechanism_refs", []))}

    def _matches_filters(self, kind: str, record: dict, filters: dict) -> bool:
        case_ids = self._case_ids(kind, record)
        if "case_id" in filters and filters["case_id"] not in case_ids:
            return False
        if "source_id" in filters:
            source_id = filters["source_id"]
            if kind == "sources":
                if record["id"] != source_id:
                    return False
            elif kind == "passages":
                if record["source_ref"] != source_id:
                    return False
            elif not any(source_id in self.store.get(cid, "cases").get("source_refs", [])
                         for cid in case_ids):
                return False
        if "publisher" in filters and not any(
            s.get("publisher", "").casefold() == str(filters["publisher"]).casefold()
            for cid in case_ids for s in self.store.case_sources(cid)
        ):
            return False
        if "domain" in filters and not any(filters["domain"] in
             self.store.get(cid, "cases").get("domain_labels", []) for cid in case_ids):
            return False
        if "case_kind" in filters and not any(
            self.store.get(cid, "cases").get("case_kind") == filters["case_kind"]
            for cid in case_ids
        ):
            return False
        return True

    def _searchable_fields(self, kind: str, record: dict) -> list[str]:
        if kind == "sources":
            return [record["title"], record.get("publisher", ""), record.get("url", "")]
        if kind == "cases":
            names = [s["title"] for s in self.store.case_sources(record["id"])]
            return names + [record.get("case_kind", ""), " ".join(record.get("domain_labels", []))]
        if kind == "passages":
            return [record["text"]]
        if kind == "events":
            return [record["statement"], record.get("kind", ""),
                    record.get("decision_rationale") or "",
                    record.get("assumption_basis") or "",
                    record.get("information_gained") or "",
                    record.get("blocking_reason") or ""]
        return [str(record.get(field, "")) for field in
                ("name", "description", "deployment", "configuration", "outcome")]

    def reconstruct(self, case_id: str, *, view: str = "historical",
                    cutoff: str | None = None) -> dict:
        """Build a grounded evidence pack. Unknown chronology stays unplaced.

        historical: documented historical events only.
        all: includes reconstructed/counterfactual branches with explicit labels.
        pre_discovery: fail-closed, reviewed, time-scoped observations only.
        """
        if view not in {"historical", "all", "pre_discovery"}:
            raise ValueError("view must be historical, all or pre_discovery")
        if view == "pre_discovery" and not cutoff:
            raise ValueError("pre_discovery requires an explicit timestamp cutoff")
        horizon = iso_time(cutoff) if cutoff else None
        case = self.store.get(case_id, "cases")
        sources = self.store.case_sources(case_id)
        all_events = self.store.events_by_case.get(case_id, [])
        all_contexts = self.store.contexts_by_case.get(case_id, [])
        warnings = []
        if view == "pre_discovery":
            events = [self._pre_discovery_event(e, horizon) for e in all_events]
            events = [e for e in events if e is not None]
            contexts = [self._pre_discovery_context(c, horizon) for c in all_contexts]
            contexts = [c for c in contexts if c is not None]
        elif view == "historical":
            events = [e for e in all_events if origin(e) == "historical"
                      and status(e) in HISTORICAL_EVIDENCE]
            contexts = [c for c in all_contexts if status(c) in HISTORICAL_EVIDENCE]
        else:
            events = list(all_events)
            contexts = list(all_contexts)
        selected_ids = {e["id"] for e in events}
        connections = self.store.case_relations(case_id, selected_ids)
        if view == "historical":
            connections = [r for r in connections if status(r) in HISTORICAL_EVIDENCE
                           and r.get("causal_basis") != "counterfactual"]
        if view == "pre_discovery":
            connections = [r for r in connections if
                           r["subject"] in selected_ids and r["object"] in selected_ids
                           and status(r) in HISTORICAL_EVIDENCE
                           and r.get("causal_basis") == "explicit_documented"
                           and r.get("hindsight_review") == "passed"
                           and iso_time(r.get("known_at")) is not None
                           and iso_time(r.get("known_at")) <= horizon
                           and self._sources_preexisting(provenance(r).get("source_refs", []), horizon)]
        dated, undated = [], []
        for event in events:
            occurred = (event.get("timestamps") or {}).get("occurred_at")
            if occurred is None:
                undated.append(event)
            else:
                dated.append(event)
        dated.sort(key=lambda e: (iso_time(e["timestamps"]["occurred_at"]), e["id"]))
        undated.sort(key=lambda e: e["id"])
        if view == "pre_discovery":
            # Return an opaque ID only; publication titles, URLs, findings, outcomes and
            # unreviewed source text are withheld even when the case is known.
            return {
                "case_id": case_id, "view": view, "cutoff": cutoff,
                "events": events, "contexts": contexts, "relations": connections,
                "timeline": [{"event_id": e["id"], "occurred_at": e["timestamps"]["occurred_at"]}
                             for e in dated],
                "chronology_unknown": [e["id"] for e in undated],
                "source_ids": sorted({sid for e in events
                                     for sid in provenance(e).get("source_refs", [])}),
                "warnings": (["Fail-closed: missing hindsight review, contemporary provenance, "
                               "or known-at timestamps cause events to be withheld."]
                             + (["No eligible pre-discovery evidence."] if not events else []))
            }
        source_summaries = [self._source_summary(s) for s in sources]
        passages = [p for p in self.store.case_passages(case_id)
                    if public_passage(p, self.store.get(p["source_ref"], "sources"))]
        findings = self.store.findings_by_case.get(case_id, [])
        if view == "historical":
            findings = [f for f in findings if status(f) in HISTORICAL_EVIDENCE]
        mechanisms = [self.store.get(mid, "mechanisms") for mid in case.get("mechanism_refs", [])]
        if view == "historical":
            mechanisms = [m for m in mechanisms if m.get("status") == "supported"]
        report = self._coverage(case, events, sources, passages, connections, dated, undated)
        if not events:
            warnings.append("No eligible trajectory events: chronology and reasoning cannot be reconstructed.")
        if not passages:
            warnings.append("No authorized searchable full-text passages for this investigation.")
        if undated:
            warnings.append("Some event occurrence times are unknown; event IDs are NOT chronological ordering.")
        warnings.append("A timeline position does not establish causation; only explicit edges express transitions.")
        return {
            "case_id": case_id, "view": view,
            "case_kind": case.get("case_kind", "unclassified"),
            "domain_labels": case.get("domain_labels", []),
            "source_records": source_summaries,
            "systems": [self.store.get(sid, "systems") for sid in case.get("system_refs", [])],
            "environments": [self.store.get(eid, "environments") for eid in case.get("environment_refs", [])],
            "contexts": contexts, "events": sorted(events, key=lambda e: e["id"]),
            "timeline": [{"event_id": e["id"], "occurred_at": e["timestamps"]["occurred_at"]}
                         for e in dated],
            "chronology_unknown": [e["id"] for e in undated],
            "relations": connections, "passages": passages, "findings": findings,
            "mechanisms": mechanisms,
            "assumptions": [e["id"] for e in events if e["kind"] == "assumption"],
            "challenged_assumptions": [e["id"] for e in events
                                      if e.get("assumption_status") == "challenged"],
            "directions": [e["id"] for e in events if e["kind"] == "direction"],
            "failed_or_negative": [e["id"] for e in events if
                                    e.get("direction_status") == "failed"
                                    or e.get("result_status") in {"failure", "negative"}],
            "untried": [e["id"] for e in events if
                        e.get("direction_status") in {"not_tested", "considered", "planned"}],
            "questions": [e["id"] for e in events if e["kind"] == "question"],
            "experiments": [e["id"] for e in events if e["kind"] == "experiment"],
            "pivots": [r["id"] for r in connections if r["predicate"] == "pivoted_to"],
            "coverage": report, "warnings": warnings
        }

    def _source_summary(self, source: dict) -> dict:
        return {k: source.get(k) for k in
                ("id", "title", "publisher", "url", "publication_date",
                 "capture_status", "license_status", "sha256")}

    def _sources_preexisting(self, source_ids: list[str], horizon: datetime) -> bool:
        if not source_ids:
            return False
        for sid in source_ids:
            source = self.store.get(sid, "sources")
            publication = source.get("publication_date")
            # Incomplete YYYY-MM dates and missing dates fail closed.
            if not publication or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", publication):
                return False
            if datetime.fromisoformat(publication).replace(tzinfo=timezone.utc) > horizon:
                return False
        return True

    def _pre_discovery_event(self, event: dict, horizon: datetime) -> dict | None:
        if (origin(event) != "historical" or status(event) not in HISTORICAL_EVIDENCE
                or event.get("hindsight_review") != "passed"
                or event["kind"] in OUTCOME_KINDS):
            return None
        event_time = iso_time((event.get("timestamps") or {}).get("known_at"))
        if event_time is None or event_time > horizon:
            return None
        occurred = iso_time((event.get("timestamps") or {}).get("occurred_at"))
        if occurred is not None and occurred > horizon:
            return None
        source_ids = provenance(event).get("source_refs", [])
        if not self._sources_preexisting(source_ids, horizon):
            return None
        # Allowlisted fields only. Do not leak later conclusions in auxiliary text.
        return {
            "id": event["id"], "kind": event["kind"], "statement": event["statement"],
            "timestamps": {"known_at": event_time.isoformat(),
                           "occurred_at": (event.get("timestamps") or {}).get("occurred_at")},
            "origin": "historical", "evidence_status": status(event),
            "source_refs": list(source_ids)
        }

    def _pre_discovery_context(self, context: dict, horizon: datetime) -> dict | None:
        if (status(context) not in HISTORICAL_EVIDENCE
                or context.get("hindsight_review") != "passed"):
            return None
        time = iso_time(context.get("snapshot_time"))
        if time is None or time > horizon:
            return None
        if not self._sources_preexisting(provenance(context).get("source_refs", []), horizon):
            return None
        return {"id": context["id"], "snapshot_time": context["snapshot_time"],
                "known_observations": context.get("known_observations", []),
                "unknowns": context.get("unknowns", [])}

    def _coverage(self, case: dict, events: list[dict], sources: list[dict],
                  passages: list[dict], relations: list[dict],
                  dated: list[dict], undated: list[dict]) -> dict:
        return {
            "source_count": len(sources), "raw_archived_sources": sum(
                s.get("capture_status") == "archived" for s in sources),
            "authorized_passage_count": len(passages), "trajectory_event_count": len(events),
            "documented_events": sum(status(e) in HISTORICAL_EVIDENCE for e in events),
            "anchored_events": sum(bool(e.get("evidence_anchors")) for e in events),
            "timestamped_events": len(dated), "unplaced_events": len(undated),
            "explicit_causal_links": sum(r.get("causal_basis") == "explicit_documented"
                                         and r["predicate"] in CAUSAL_PREDICATES
                                         for r in relations),
            "reconstructed_links": sum(r.get("causal_basis") == "reconstructed" for r in relations),
            "status": ("metadata_only" if not events and not passages
                       else "partial_reconstruction" if not events or undated
                       else "evidence_available_not_completeness_certified")
        }

    def trace_question(self, case_id: str, question_id: str, *,
                       view: str = "historical", max_depth: int = 6) -> dict:
        """Trace documented/inferred predecessors without confusing mere sequence with cause."""
        if not 1 <= max_depth <= 20:
            raise ValueError("max_depth must be 1..20")
        pack = self.reconstruct(case_id, view=view)
        nodes = {e["id"]: e for e in pack["events"]}
        if question_id not in nodes or nodes[question_id]["kind"] != "question":
            raise ValueError("Question is not eligible or not present in this case")
        incoming = defaultdict(list)
        for rel in pack["relations"]:
            if rel["subject"] not in nodes or rel["object"] not in nodes:
                continue
            if rel["predicate"] not in CAUSAL_PREDICATES:
                continue
            basis = rel.get("causal_basis", "unknown")
            if basis not in ({"explicit_documented"} if view == "historical" else
                             {"explicit_documented", "reconstructed"}):
                continue
            # Most predicates run cause -> effect, except motivated_by, tested_by etc.
            if rel["predicate"] in {"motivated_by", "tested_by", "blocked_by",
                                    "abandoned_because", "failed_because"}:
                cause, effect = rel["object"], rel["subject"]
            else:
                cause, effect = rel["subject"], rel["object"]
            incoming[effect].append((cause, rel))
        visited = {question_id}
        queue = deque([(question_id, 0)])
        steps = []
        while queue:
            item, depth = queue.popleft()
            if depth >= max_depth:
                continue
            for parent, relation in sorted(incoming.get(item, []), key=lambda p: p[1]["id"]):
                steps.append({"from": parent, "to": item, "relation_id": relation["id"],
                              "predicate": relation["predicate"],
                              "causal_basis": relation.get("causal_basis", "unknown"),
                              "evidence_status": status(relation)})
                if parent not in visited:
                    visited.add(parent)
                    queue.append((parent, depth + 1))
        return {"case_id": case_id, "question_id": question_id, "view": view,
                "predecessor_events": [nodes[key] for key in sorted(visited) if key != question_id],
                "causal_steps": steps,
                "limitations": (["No qualifying causal history documented."]
                                if not steps else []),
                "note": "This is a provenance-filtered graph traversal, not an inferred history."}

    def related_cases(self, case_id: str, *, limit: int = 20) -> dict:
        """Return evidence-backed mechanism/source overlap and explicit case links only."""
        if not 1 <= limit <= 100:
            raise ValueError("limit must be 1..100")
        primary = self.store.get(case_id, "cases")
        matches = []
        a_mechanisms = set(primary.get("mechanism_refs", []))
        a_sources = set(primary.get("source_refs", []))
        for other in self.store.registries["cases"]:
            if other["id"] == case_id:
                continue
            shared_m = sorted(a_mechanisms.intersection(other.get("mechanism_refs", [])))
            shared_s = sorted(a_sources.intersection(other.get("source_refs", [])))
            edges = [r for r in self.store.registries["relations"]
                     if {r["subject"], r["object"]} == {case_id, other["id"]}]
            if not (shared_m or shared_s or edges):
                continue
            matches.append({"case_id": other["id"], "shared_mechanism_refs": shared_m,
                            "shared_source_refs": shared_s,
                            "explicit_relations": edges,
                            "evidence": "curated_links_only"})
        matches.sort(key=lambda x: (-len(x["shared_mechanism_refs"]),
                                    -len(x["shared_source_refs"]), x["case_id"]))
        return {"case_id": case_id, "related": matches[:limit],
                "note": "No relation is inferred from title similarity or chronology."}
