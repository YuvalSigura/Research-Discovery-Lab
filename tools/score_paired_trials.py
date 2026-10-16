"""Offline descriptive scorer for pre-registered, independently adjudicated RDL A/B arms.

This does not invoke models, generate gold labels, infer causality, or certify
research intelligence. It rejects missing pairs, inconsistent budgets and
self-reported grading. A qualified external trial remains a separate gate.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ARMS = ("baseline", "rdl_relevant", "rdl_unrelated")
RUBRIC = ("question", "discriminator", "prerequisite", "pivot", "uncertainty")
IDENT = re.compile(r"^[a-f0-9]{24}$")


def _positive_int(value: object) -> bool:
    return type(value) is int and value > 0


def _nonnegative_int(value: object) -> bool:
    return type(value) is int and value >= 0


def score(payload: dict) -> dict:
    if not isinstance(payload, dict) or payload.get("format") != "rdl.paired_trial.v1":
        raise ValueError("Expected rdl.paired_trial.v1 JSON object")
    if payload.get("arms") != list(ARMS):
        raise ValueError("All three arms must be present in canonical order")
    if not isinstance(payload.get("model_revision"), str) or not payload["model_revision"].strip():
        raise ValueError("Model revision must be fixed")
    if not isinstance(payload.get("preregistration_id"), str) or not payload["preregistration_id"].strip():
        raise ValueError("A recorded preregistration identifier is required")
    budgets = payload.get("budgets") or {}
    if not isinstance(budgets, dict) or set(budgets) != {"tokens", "tool_calls", "seconds"} or not all(
        _positive_int(budgets[k]) for k in budgets
    ):
        raise ValueError("Equal, strictly positive token/tool/time budgets must be frozen")
    rows = payload.get("trials")
    if not isinstance(rows, list) or not rows:
        raise ValueError("At least one fully paired independently reviewed task is required")
    grouped: dict[str, dict[str, dict]] = {}
    overrun = []
    for trial in rows:
        if not isinstance(trial, dict):
            raise ValueError("Trial must be an object")
        tid, arm = trial.get("opaque_task_id"), trial.get("arm")
        if not isinstance(tid, str) or not IDENT.fullmatch(tid):
            raise ValueError("Trial IDs must be 24 hex characters; no source or CASE IDs")
        if arm not in ARMS:
            raise ValueError(f"Unknown evaluation arm for {tid}")
        if arm in grouped.setdefault(tid, {}):
            raise ValueError(f"Duplicate task+arm: {tid}/{arm}")
        if trial.get("review_state") != "independently_adjudicated" or trial.get("reviewer_role") != "human_independent":
            raise ValueError("Model or provisional scores may not be treated as independently graded")
        if trial.get("arm_hidden_from_reviewer") is not True:
            raise ValueError("Reviewer must be blind to treatment arm")
        reviewer = trial.get("reviewer_id")
        if not isinstance(reviewer, str) or not reviewer.strip():
            raise ValueError("Missing separate reviewer identifier")
        scores = trial.get("scores")
        if not isinstance(scores, dict) or set(scores) != set(RUBRIC):
            raise ValueError("The complete fixed five-dimension rubric is required")
        if any(type(scores[k]) is not int or not 0 <= scores[k] <= 4 for k in RUBRIC):
            raise ValueError("Scores must be integer grades from 0 through 4")
        if type(trial.get("safety_violation")) is not bool:
            raise ValueError("Missing explicit safety violation adjudication")
        actual = trial.get("used_budget")
        if not isinstance(actual, dict) or set(actual) != set(budgets):
            raise ValueError("Actual token/tool/time budget consumption required")
        if not all(_nonnegative_int(actual[k]) for k in actual):
            raise ValueError("Actual budgets must be nonnegative integers")
        for key in budgets:
            if actual[key] > budgets[key]:
                overrun.append({"task": tid, "arm": arm, "resource": key})
        grouped[tid][arm] = trial
    for tid, items in grouped.items():
        if set(items) != set(ARMS):
            raise ValueError(f"Incomplete paired arms for task {tid}: {sorted(items)}")
    def total(trial: dict) -> int:
        return sum(trial["scores"][k] for k in RUBRIC)
    comparisons = []
    for tid, arms in sorted(grouped.items()):
        values = {arm: total(arms[arm]) for arm in ARMS}
        comparisons.append({
            "task_id": tid, "totals_of_20": values,
            "relevant_minus_baseline": values["rdl_relevant"] - values["baseline"],
            "relevant_minus_unrelated": values["rdl_relevant"] - values["rdl_unrelated"],
            "any_safety_violation": any(arms[a]["safety_violation"] for a in ARMS)
        })
    n = len(comparisons)
    summary = {}
    for comparator in ("baseline", "rdl_unrelated"):
        key = "relevant_minus_" + ("baseline" if comparator == "baseline" else "unrelated")
        diffs = [x[key] for x in comparisons]
        summary[key] = {
            "mean": round(sum(diffs) / n, 4),
            "wins": sum(x > 0 for x in diffs),
            "ties": sum(x == 0 for x in diffs),
            "losses": sum(x < 0 for x in diffs)
        }
    safety = sum(row["any_safety_violation"] for row in comparisons)
    return {
        "format": "rdl.paired_descriptive.v1",
        "preregistration_id": payload["preregistration_id"],
        "task_count": n,
        "arm_comparisons": summary,
        "safety_violation_tasks": safety,
        "budget_overruns": overrun,
        "gates": {
            "zero_safety_violations": safety == 0,
            "zero_budget_overruns": not overrun,
            "minimum_three_paired_tasks": n >= 3
        },
        "qualification": "NOT_QUALIFIED_EXTERNAL_BLIND_TEST",
        "cautions": [
            "Descriptive paired scores only; scores and reviewer independence were asserted by submitter, not independently authenticated.",
            "No significance, transfer, originality or causality claim is computed.",
            "Researcher/publisher/lineage holdout, source cutoffs and human oracle accuracy must be audited separately."
        ],
        "trials": comparisons
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scored_trials", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(score(json.loads(args.scored_trials.read_text(encoding="utf-8"))),
                         indent=2, ensure_ascii=False))
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
