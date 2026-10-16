"""Fail-closed candidate builder for blind pre-decision evaluation.

Not a benchmark, an answer key, a success score, or permission to use retrospective
articles as prior knowledge. Outputs anonymous *review candidates* only. Human
reviewers must independently inspect semantic and identity leakage before release.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def records(root: Path, kind: str) -> list[dict]:
    return json.loads((root / "registry" / kind / "index.json").read_text(encoding="utf-8"))["records"]


def _timestamp(text: object) -> datetime | None:
    if not isinstance(text, str) or not text:
        return None
    try:
        value = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if value.tzinfo is None:
        return None
    return value.astimezone(timezone.utc)


def build(root: Path = ROOT, *, secret: str) -> dict:
    if len(secret) < 16:
        raise ValueError("A private, operator-supplied HMAC key of at least 16 characters is required")
    sources = {x["id"]: x for x in records(root, "sources")}
    cases = {x["id"]: x for x in records(root, "cases")}
    contexts = records(root, "contexts")
    tasks = []
    exclusions = []
    seen = set()
    for context in contexts:
        cid = context["case_ref"]
        reasons = []
        snapshot = _timestamp(context.get("snapshot_time"))
        if snapshot is None:
            reasons.append("missing_or_invalid_exact_cutoff")
        if context.get("hindsight_review") != "passed":
            reasons.append("hindsight_review_not_passed")
        if context.get("provenance", {}).get("evidence_status") not in {"documented", "verified"}:
            reasons.append("snapshot_not_documented")
        observations = context.get("known_observations") or []
        if not observations:
            reasons.append("no_known_observations")
        for item in observations:
            refs = item.get("source_refs") or []
            if not refs:
                reasons.append("observation_without_source")
            for source_id in refs:
                source = sources.get(source_id)
                if source is None or cid not in cases or source_id not in cases[cid]["source_refs"]:
                    reasons.append("source_not_in_case")
                    continue
                # Date-only publication metadata cannot prove an article was available at
                # 09:00 on that same day. Require strictly earlier publication DAY.
                published = source.get("publication_date")
                if not isinstance(published, str) or re.fullmatch(r"\\d{4}-\\d{2}-\\d{2}", published) is None:
                    reasons.append("publication_day_unverified")
                elif snapshot is not None and published >= snapshot.date().isoformat():
                    reasons.append("source_not_certainly_published_before_cutoff")
        if reasons:
            exclusions.append({"context_id": context["id"], "reasons": sorted(set(reasons))})
            continue
        opaque = hmac.new(secret.encode("utf-8"), (cid + "|" + context["id"] + "|" + str(context["snapshot_time"])).encode("utf-8"), hashlib.sha256).hexdigest()[:24]
        if opaque in seen:
            raise ValueError("Opaque evaluation id collision")
        seen.add(opaque)
        tasks.append({
            "opaque_task_id": opaque,
            "review_only": True,
            "known_observations": [x["text"] for x in observations],
            "unknowns": context.get("unknowns", []),
            "available_capabilities": context.get("capabilities", []),
            "constraints": context.get("constraints", []),
            "prompt": "Given only the information above, propose the next research question and a feasible discriminating experiment; state uncertainty and what would change the decision."
        })
    return {
        "format": "rdl.predecision.candidates.v1",
        "status": "human_review_required",
        "warning": "Candidate tasks are not a blind-qualified benchmark. Human audit must remove semantic answer, target-identity and future-information leakage; no gold labels or actual outcomes are exported.",
        "task_count": len(tasks),
        "excluded_count": len(exclusions),
        "tasks": tasks,
        "excluded": exclusions
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--key-env", default="RDL_BLIND_KEY", help="Environment variable holding the private ID key; never print it")
    args = parser.parse_args()
    key = os.environ.get(args.key_env, "")
    try:
        result = build(args.root, secret=key)
    except (ValueError, OSError, KeyError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
