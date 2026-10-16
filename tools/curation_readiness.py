"""Read-only, evidence-first curation readiness report.

This reports missing prerequisites, not a numerical measure of research quality.
It never promotes a case, snapshot, mindset or question mapping to reviewed.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(root: Path, kind: str) -> list[dict]:
    path = root / "registry" / kind / "index.json"
    return json.loads(path.read_text(encoding="utf-8"))["records"]


def report(root: Path = ROOT, *, case_id: str | None = None) -> dict:
    cases = load(root, "cases")
    sources = {x["id"]: x for x in load(root, "sources")}
    events = load(root, "events")
    relations = load(root, "relations")
    contexts = load(root, "contexts")
    mindsets = load(root, "mindsets")
    mappings = load(root, "question_mappings")
    patterns = {x["id"]: x for x in load(root, "question_patterns")}
    if case_id and not any(c["id"] == case_id for c in cases):
        raise ValueError(f"Unknown case: {case_id}")
    rows = []
    for c in cases:
        cid = c["id"]
        if case_id and cid != case_id:
            continue
        es = [e for e in events if e["case_ref"] == cid]
        eids = {e["id"] for e in es}
        rs = [r for r in relations if r["subject"] in eids and r["object"] in eids]
        cs = [x for x in contexts if x["case_ref"] == cid]
        ms = [x for x in mindsets if x["case_ref"] == cid]
        qs = [x for x in mappings if x["case_ref"] == cid]
        src = [sources[s] for s in c["source_refs"]]
        flags = []
        if not es:
            flags.append("no_reconstructed_events")
        if not any(e["kind"] == "question" for e in es):
            flags.append("no_documented_question")
        if es and not rs:
            flags.append("no_interevent_relations")
        if not cs:
            flags.append("no_context_snapshots")
        if not any(x.get("hindsight_review") == "passed" for x in cs):
            flags.append("no_approved_predecision_snapshot")
        if not ms:
            flags.append("no_mindset_observations")
        if not any(m.get("review_status") == "curator_reviewed" for m in ms):
            flags.append("no_curator_reviewed_mindsets")
        if not any(
            q.get("review_status") == "curator_reviewed"
            and patterns.get(q["pattern_ref"], {}).get("status") == "curator_reviewed"
            for q in qs
        ):
            flags.append("no_reviewed_question_equivalence")
        if any(s.get("capture_status") != "archived" for s in src):
            flags.append("original_source_not_archived")
        if any(s.get("license_status") == "unreviewed" for s in src):
            flags.append("source_rights_unreviewed")
        if any(
            e.get("timestamps", {}).get("known_at") is None
            for e in es
            if e.get("origin") == "historical"
        ):
            flags.append("historical_knowledge_times_unknown")
        if c.get("analysis_status") != "reviewed":
            flags.append("case_not_curator_reviewed")
        rows.append({
            "case_id": cid,
            "case_kind": c.get("case_kind"),
            "analysis_status": c.get("analysis_status"),
            "events": len(es),
            "questions": sum(e["kind"] == "question" for e in es),
            "historical_events": sum(e.get("origin") == "historical" for e in es),
            "analyst_reconstructions": sum(e.get("origin") == "reconstructed" for e in es),
            "relations": len(rs),
            "context_snapshots": len(cs),
            "approved_predecision_snapshots": sum(x.get("hindsight_review") == "passed" for x in cs),
            "mindset_observations": len(ms),
            "reviewed_mindsets": sum(x.get("review_status") == "curator_reviewed" for x in ms),
            "question_mappings": len(qs),
            "reviewed_question_mappings": sum(q.get("review_status") == "curator_reviewed" for q in qs),
            "flags": flags
        })
    return {
        "report_version": "rdl.curation.readiness.v1",
        "interpretation": "Coverage indicators and curation blockers only; none imply independent verification.",
        "summary": {
            "cases": len(rows),
            "with_events": sum(r["events"] > 0 for r in rows),
            "with_approved_predecision_snapshot": sum(r["approved_predecision_snapshots"] > 0 for r in rows),
            "with_reviewed_question_mapping": sum(r["reviewed_question_mappings"] > 0 for r in rows),
            "cases_by_kind": dict(sorted(Counter(r["case_kind"] for r in rows).items()))
        },
        "cases": rows
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--case-id")
    args = parser.parse_args()
    try:
        print(json.dumps(report(args.root, case_id=args.case_id), indent=2, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
