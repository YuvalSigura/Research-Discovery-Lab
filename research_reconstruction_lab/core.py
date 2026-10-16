"""Review proposed reasoning traces, without inferring private history or writing RDL registries.

The caller supplies evidence summaries and candidate events; this engine checks
internal epistemic constraints, NOT whether a paraphrase is true to a publisher.
"""
from __future__ import annotations
import re
from datetime import datetime
from urllib.parse import urlsplit

SCHEMA = "rdl.reconstruction_candidate.v1"
EVIDENCE_KINDS = {"retrospective_author", "contemporaneous_artifact", "source_code", "independent_source", "analyst_note"}
CLAIM_KINDS = {"observation", "question", "hypothesis", "experiment", "result", "decision", "blocker", "outcome"}
CLAIM_BASIS = {"author_report", "artifact_observed", "analyst_inference", "unknown"}
OUTCOMES = {"not_applicable", "observed", "negative_test", "no_evidence_observed", "inconclusive", "not_run"}
EFFECTS = {"unassessed", "supported_in_scope", "refuted_in_scope", "open"}
LINK_KINDS = {"followed_by", "motivated", "revised_after", "tested_by", "stopped_because"}
LINK_BASIS = {"author_explicit", "chronology_only", "analyst_inference", "unknown"}

class PackError(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise PackError(message)

def nonempty(x, label):
    require(isinstance(x, str) and bool(x.strip()), label + ": nonempty string required")
    return x.strip()

def objects(x, label):
    require(isinstance(x, list) and all(isinstance(v, dict) for v in x), label + ": object array required")
    return x

def ids(x, label):
    require(isinstance(x, list) and all(isinstance(v, str) and v for v in x), label + ": ID array required")
    require(len(x) == len(set(x)), label + ": repeated ID")
    return x

def timestamp(value, label):
    if value is None:
        return
    require(isinstance(value, str), label + ": timestamp must be a string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PackError(label + ": bad timestamp") from exc
    require(parsed.tzinfo is not None and parsed.utcoffset() is not None,
            label + ": timezone unknown (do not invent an offset)")

def inspect(pack):
    """Return conservative review findings for a submitted provisional evidence pack.

    Successful structural inspection does NOT substantiate source claims, causal
    motives, claimed timestamps, independent curation, or historical predecision CTX.
    """
    require(isinstance(pack, dict) and pack.get("schema") == SCHEMA,
            "unexpected or absent candidate pack schema")
    case_id = nonempty(pack.get("case_id"), "case_id")
    require(re.fullmatch("CASE-[0-9]{6}", case_id) is not None, "invalid CASE ID")
    sources = objects(pack.get("sources"), "sources")
    require(bool(sources), "at least one source required")
    source_map = {}
    for s in sources:
        sid = nonempty(s.get("id"), "source ID")
        require(re.fullmatch("SRC-[0-9]{6}", sid) is not None and sid not in source_map,
                "source identity invalid or duplicated: " + sid)
        u = urlsplit(nonempty(s.get("url"), sid + ".url"))
        require(u.scheme == "https" and bool(u.hostname), sid + ": HTTPS source required")
        source_map[sid] = s
    evidence_map = {}
    warnings = []
    for e in objects(pack.get("evidence"), "evidence"):
        eid = nonempty(e.get("id"), "evidence ID")
        require(eid not in evidence_map, eid + ": duplicate evidence ID")
        require(e.get("source_ref") in source_map, eid + ": source not in pack")
        require(e.get("kind") in EVIDENCE_KINDS, eid + ": invalid evidence kind")
        nonempty(e.get("locator"), eid + ".locator")
        nonempty(e.get("statement"), eid + ".statement")
        timestamp(e.get("known_at"), eid + ".known_at")
        timestamp(e.get("occurred_at"), eid + ".occurred_at")
        if e.get("kind") == "retrospective_author":
            warnings.append({"id": eid, "code": "retrospective_does_not_prove_contemporaneous_motive"})
        if e.get("known_at") is not None:
            warnings.append({"id": eid, "code": "known_at_requires_independent_artifact_validation"})
        evidence_map[eid] = e
    claim_map = {}
    for c in objects(pack.get("claims"), "claims"):
        cid = nonempty(c.get("id"), "claim ID")
        require(cid not in claim_map, cid + ": duplicate claim")
        require(c.get("kind") in CLAIM_KINDS, cid + ": invalid claim kind")
        nonempty(c.get("statement"), cid + ".statement")
        basis = c.get("basis", "unknown")
        require(basis in CLAIM_BASIS, cid + ": invalid claim basis")
        refs = ids(c.get("evidence_refs", []), cid + ".evidence_refs")
        require(all(x in evidence_map for x in refs), cid + ": dangling evidence")
        outcome = c.get("outcome", "not_applicable")
        effect = c.get("hypothesis_effect", "unassessed")
        require(outcome in OUTCOMES and effect in EFFECTS, cid + ": invalid outcome/effect")
        if outcome != "not_applicable" or effect != "unassessed":
            require(c["kind"] == "result", cid + ": outcome/impact requires result claim")
        if effect in {"supported_in_scope", "refuted_in_scope"}:
            nonempty(c.get("scope"), cid + ".scope")
        if effect == "refuted_in_scope":
            require(outcome not in {"no_evidence_observed", "inconclusive", "not_run", "not_applicable"},
                    cid + ": absence of evidence does not refute a hypothesis")
            nonempty(c.get("discriminator"), cid + ".discriminator")
            warnings.append({"id": cid, "code": "semantic_refutation_needs_independent_test_review"})
        if basis in {"author_report", "artifact_observed"}:
            require(refs and any(evidence_map[r]["kind"] != "analyst_note" for r in refs),
                    cid + ": evidence-backed claim missing independent source anchor")
        if basis == "analyst_inference":
            warnings.append({"id": cid, "code": "analyst_inference_not_historical_truth"})
        if not refs:
            warnings.append({"id": cid, "code": "claim_without_evidence"})
        if c["kind"] == "decision" and not c.get("reason_documented", False):
            warnings.append({"id": cid, "code": "decision_reason_unknown"})
        claim_map[cid] = c
    connections = []
    seen_links = set()
    for l in objects(pack.get("links"), "links"):
        lid = nonempty(l.get("id"), "link ID")
        require(lid not in seen_links, lid + ": duplicate link")
        seen_links.add(lid)
        require(l.get("from") in claim_map and l.get("to") in claim_map and
                l["from"] != l["to"], lid + ": invalid link endpoints")
        kind = l.get("kind")
        basis = l.get("basis", "unknown")
        require(kind in LINK_KINDS and basis in LINK_BASIS, lid + ": invalid kind/basis")
        refs = ids(l.get("evidence_refs", []), lid + ".evidence_refs")
        require(all(x in evidence_map for x in refs), lid + ": dangling evidence")
        alt = l.get("alternatives", [])
        require(isinstance(alt, list) and all(isinstance(x, str) and x.strip() for x in alt),
                lid + ": invalid alternative interpretations")
        if basis == "author_explicit":
            require(refs and any(evidence_map[x]["kind"] == "retrospective_author" for x in refs),
                    lid + ": author-explicit motive requires an author report")
        assessment = ("sequence_only" if kind == "followed_by" else
                      "author_reported_unverified_causality" if basis == "author_explicit" else
                      "unresolved_competing_explanations")
        if kind != "followed_by" and basis != "author_explicit":
            warnings.append({"id": lid, "code": "causal_motive_not_established"})
            if not alt:
                warnings.append({"id": lid, "code": "missing_competing_explanations"})
        if kind != "followed_by" and basis == "chronology_only":
            warnings.append({"id": lid, "code": "order_not_causation"})
        if assessment == "author_reported_unverified_causality":
            warnings.append({"id": lid, "code": "reported_motive_not_contemporaneous_proof"})
        connections.append({"id": lid, "from": l["from"], "to": l["to"],
                            "kind": kind, "submitted_basis": basis,
                            "assessment": assessment, "alternatives": alt,
                            "evidence_refs": refs})
    return {
        "schema": "rdl.reconstruction_inspection.v1", "case_id": case_id,
        "status": "candidate_unreviewed", "source_verification": "not_performed",
        "independent_curator_review": "pending", "truth_promotion_allowed": False,
        "legacy_registry_modified": False, "predecision_snapshot_approved": False,
        "counts": {"sources": len(source_map), "evidence": len(evidence_map),
                   "claims": len(claim_map), "connections": len(connections),
                   "warnings": len(warnings)},
        "claims": [{"id": c["id"], "kind": c["kind"], "statement": c["statement"],
                    "basis": c.get("basis", "unknown"),
                    "hypothesis_effect": c.get("hypothesis_effect", "unassessed"),
                    "outcome": c.get("outcome", "not_applicable"),
                    "review": "pending"} for c in claim_map.values()],
        "connections": connections, "warnings": warnings,
        "limitations": [
            "Source URLs, locators and submitted paraphrases were not independently fact-checked.",
            "Retrospective narration does not prove the researcher's actual knowledge or decision chronology.",
            "An accepted discriminator field is not proof a test really discriminates.",
            "No automatic registry import, history approval or HOMELAB target-execution authority."
        ]
    }
