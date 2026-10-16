"""Read-only, source-anchored independent curation work queue for RDL.

A work queue is not an adjudication and does not confer historical truth,
scientific confidence, source copyright permission, or benchmark eligibility.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOCUS = {"question", "assumption", "decision", "pivot", "experiment", "blocking_factor", "knowledge_revision", "outcome"}


def _records(root: Path, folder: str) -> list[dict]:
    return json.loads((root / "registry" / folder / "index.json").read_text(encoding="utf-8"))["records"]


def build(root: Path = ROOT, *, case_id: str | None = None) -> dict:
    cases = {c["id"]: c for c in _records(root, "cases")}
    if case_id is not None and case_id not in cases:
        raise ValueError(f"Unknown case: {case_id}")
    sources = {s["id"]: s for s in _records(root, "sources")}
    events = _records(root, "events")
    relations = _records(root, "relations")
    mindsets = _records(root, "mindsets")
    patterns = {p["id"]: p for p in _records(root, "question_patterns")}
    mappings = _records(root, "question_mappings")
    contexts = _records(root, "contexts")

    target_ids = [case_id] if case_id else sorted(cases)
    packets = []
    for cid in target_ids:
        es = [e for e in events if e["case_ref"] == cid]
        if not es and case_id is None:
            continue
        ids = {e["id"] for e in es}
        rs = [r for r in relations if r["subject"] in ids and r["object"] in ids]
        ms = [m for m in mindsets if m["case_ref"] == cid]
        qs = [m for m in mappings if m["case_ref"] == cid]
        ctxs = [c for c in contexts if c["case_ref"] == cid]
        srclist = [sources[s] for s in cases[cid]["source_refs"]]
        observations = []
        for e in es:
            flags = []
            if e["kind"] in FOCUS:
                flags.append("decision_or_scientific_claim_requires_independent_source_check")
            if e.get("origin") == "reconstructed":
                flags.append("analyst_reconstruction_not_historical_truth")
            if e.get("origin") == "historical" and e.get("kind") == "question":
                flags.append("confirm_question_is_explicit_author_account_not_analyst_words")
            if e.get("origin") == "historical" and (e.get("timestamps") or {}).get("known_at") is None:
                flags.append("no_contemporaneous_knowledge_cutoff")
            if e.get("hindsight_review") != "passed":
                flags.append("hindsight_not_independently_reviewed")
            if e.get("result_status") in {"negative", "failure", "inconclusive"}:
                flags.append("distinguish_failed_test_from_disproved_hypothesis")
            anchors = e.get("evidence_anchors") or []
            if not anchors or any("content_sha256" not in a for a in anchors):
                flags.append("source_anchor_not_immutable")
            observations.append({
                "event_id": e["id"], "kind": e["kind"], "claim": e["statement"],
                "origin": e.get("origin", "unknown"),
                "publisher_claim_status": (e.get("provenance") or {}).get("evidence_status", "unknown"),
                "source_anchors": [{"source_id": a["source_ref"], "locator": a["locator"]}
                                   for a in anchors],
                "review_flags": sorted(set(flags)),
                "curator_decision": "pending"
            })
        edges = []
        for r in rs:
            flags = ["causal_claim_requires_source_recheck"] if r.get("causal_basis") == "explicit_documented" else []
            if r.get("causal_basis") == "reconstructed":
                flags.append("inferred_connection_not_historical")
            if r.get("causal_basis") == "temporal_only":
                flags.append("sequence_not_causality")
            edges.append({
                "relation_id": r["id"], "subject": r["subject"], "predicate": r["predicate"],
                "object": r["object"], "causal_basis": r.get("causal_basis"),
                "curator_decision": "pending", "review_flags": flags
            })
        packets.append({
            "case_id": cid, "case_kind": cases[cid]["case_kind"],
            "status": "independent_review_pending",
            "source_inventory": [{"source_id": s["id"], "url": s["url"],
                                   "capture_status": s["capture_status"],
                                   "license_status": s.get("license_status", "unreviewed")}
                                  for s in srclist],
            "event_review": observations,
            "relation_review": edges,
            "mindset_review": [{"id": m["id"], "status": m.get("review_status", "not_reviewed")}
                               for m in ms],
            "question_mapping_review": [{
                "id": m["id"], "relation": m.get("abstraction_relation"),
                "review_status": m.get("review_status"),
                "family_status": patterns[m["pattern_ref"]]["status"]
            } for m in qs],
            "approved_predecision_snapshots": sum(
                1 for c in ctxs if c.get("hindsight_review") == "passed"
            ),
            "critical_review_questions": [
                "Is the wording in a contemporaneous source, an author's retrospective account, or the analyst's inference?",
                "What observation would contradict the proposed causal edge or underlying research question?",
                "Do stated negative or blocked results actually discriminate the claimed hypothesis?",
                "Is source revision, licensing, section locator and independent reviewer identity documented?",
                "Can an earlier knowledge cutoff be proved, rather than guessed from publication date?"
            ]
        })
    return {
        "schema": "rdl.independent_curation_queue.v1",
        "adjudication": "NONE - generated checklist only; cannot set reviewed status",
        "case_count": len(packets),
        "events_to_review": sum(len(x["event_review"]) for x in packets),
        "relations_to_review": sum(len(x["relation_review"]) for x in packets),
        "flag_totals": dict(sorted(Counter(
            flag for p in packets for item in p["event_review"]
            for flag in item["review_flags"]
        ).items())),
        "packets": packets
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--case-id")
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.root, case_id=args.case_id), indent=2, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
