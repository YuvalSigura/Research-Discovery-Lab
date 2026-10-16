"""Fail on accidental removal of previously published research records.

Compares the immutable git baseline to the candidate revision. A correction of an
existing claim may be legitimate, but removing identifiers, dropping CASE sources,
or silently replacing source identity is not an ordinary curation update.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

KINDS = (
    "sources", "cases", "systems", "environments", "contexts", "findings",
    "mechanisms", "events", "relations", "passages", "mindsets",
    "question_patterns", "question_mappings",
)
ROOT = Path(__file__).resolve().parents[1]


def compare_snapshots(before: dict[str, list[dict]], after: dict[str, list[dict]]) -> list[str]:
    errors: list[str] = []
    for kind, older in before.items():
        newer = after.get(kind)
        if newer is None:
            errors.append(f"{kind}: registry missing from candidate revision")
            continue
        old_ids = [item["id"] for item in older]
        new_ids = [item["id"] for item in newer]
        if len(old_ids) != len(set(old_ids)):
            errors.append(f"{kind}: baseline has duplicate identifiers")
        if len(new_ids) != len(set(new_ids)):
            errors.append(f"{kind}: candidate has duplicate identifiers")
        old_map = {item["id"]: item for item in older}
        new_map = {item["id"]: item for item in newer}
        for rid in sorted(set(old_map) - set(new_map)):
            errors.append(f"{kind}: historical record removed: {rid}")
        for rid in sorted(set(old_map) & set(new_map)):
            old, new = old_map[rid], new_map[rid]
            if kind in {"sources", "legacy_catalog"} and old.get("url") != new.get("url"):
                errors.append(f"{kind}: canonical source identity changed for {rid}")
            if kind == "cases":
                missing_sources = set(old.get("source_refs", [])) - set(new.get("source_refs", []))
                if missing_sources:
                    errors.append(f"{kind}: {rid} lost source refs: {', '.join(sorted(missing_sources))}")
            if kind == "events" and old.get("case_ref") != new.get("case_ref"):
                errors.append(f"{kind}: {rid} moved to a different case")
            if kind == "relations":
                if old.get("subject") != new.get("subject") or old.get("object") != new.get("object"):
                    errors.append(f"{kind}: {rid} changed its evidence-graph endpoints")
    return errors


def _git_json(root: Path, ref: str, path: str) -> dict:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path}"], cwd=root,
        capture_output=True, text=True, encoding="utf-8", check=False
    )
    if proc.returncode:
        raise ValueError(f"Cannot read {path} at {ref[:12]}; full history required")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path} at {ref[:12]}") from exc


def snapshot(root: Path, ref: str) -> dict[str, list[dict]]:
    if not re.fullmatch(r"[0-9a-fA-F]{40}", ref):
        raise ValueError("Git revision must be a full, verified SHA-1 commit ID")
    out = {}
    for kind in KINDS:
        path = f"registry/{kind}/index.json"
        out[kind] = _git_json(root, ref, path)["records"]
    out["legacy_catalog"] = _git_json(root, ref, "research/index.json")["cases"]
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="40-digit commit SHA from the GitHub event")
    parser.add_argument("--head", default=None, help="candidate SHA; defaults to checked-out HEAD")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    if args.base == "0" * 40:
        print("SKIP: initial branch creation has no previous baseline")
        return
    head = args.head
    if head is None:
        proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=args.root,
                              capture_output=True, text=True, check=True)
        head = proc.stdout.strip()
    try:
        errors = compare_snapshots(snapshot(args.root, args.base), snapshot(args.root, head))
    except (ValueError, KeyError, OSError) as exc:
        parser.exit(2, f"Registry nonloss check could not run: {exc}\n")
    if errors:
        parser.exit(1, "Registry nonloss check FAILED:\n" + "\n".join(errors) + "\n")
    print("PASS: all existing registry and legacy-catalog identifiers preserved, with stable source identity")


if __name__ == "__main__":
    main()
