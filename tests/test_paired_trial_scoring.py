"""Synthetic paired-trial scorer controls. These are not real qualified cases."""
import copy
import unittest

from tools.score_paired_trials import ARMS, score


def example(n=3):
    rows = []
    for i in range(n):
        tid = f"{i + 1:024x}"
        for arm in ARMS:
            grade = 3 if arm == "rdl_relevant" else 2
            rows.append({
                "opaque_task_id": tid, "arm": arm, "review_state": "independently_adjudicated",
                "reviewer_role": "human_independent", "reviewer_id": "fixture-reviewer",
                "arm_hidden_from_reviewer": True,
                "scores": dict.fromkeys(("question", "discriminator", "prerequisite", "pivot", "uncertainty"), grade),
                "safety_violation": False,
                "used_budget": {"tokens": 120, "tool_calls": 1, "seconds": 10}
            })
    return {"format": "rdl.paired_trial.v1",
            "preregistration_id": "synthetic-fixture-1",
            "model_revision": "synthetic-unchanging-checkpoint",
            "arms": list(ARMS), "budgets": {"tokens": 1000, "tool_calls": 4, "seconds": 120},
            "trials": rows}


class PairedTrialScorerTests(unittest.TestCase):
    def test_complete_three_arm_paired_scores_are_descriptive_only(self):
        d = score(example())
        self.assertEqual(d["task_count"], 3)
        self.assertEqual(d["arm_comparisons"]["relevant_minus_baseline"],
                         {"mean": 5.0, "wins": 3, "ties": 0, "losses": 0})
        self.assertEqual(d["arm_comparisons"]["relevant_minus_unrelated"]["wins"], 3)
        self.assertEqual(d["safety_violation_tasks"], 0)
        self.assertTrue(all(d["gates"].values()))
        self.assertEqual(d["qualification"], "NOT_QUALIFIED_EXTERNAL_BLIND_TEST")

    def test_single_pilot_never_passes_independent_sample_gate(self):
        d = score(example(1))
        self.assertFalse(d["gates"]["minimum_three_paired_tasks"])
        self.assertEqual(d["qualification"], "NOT_QUALIFIED_EXTERNAL_BLIND_TEST")

    def test_unpaired_or_duplicate_arms_rejected(self):
        d = example()
        d["trials"].pop()
        with self.assertRaisesRegex(ValueError, "Incomplete paired arms"):
            score(d)
        d = example()
        d["trials"].append(copy.deepcopy(d["trials"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            score(d)

    def test_self_scoring_and_reviewer_unblinding_rejected(self):
        d = example()
        d["trials"][0]["reviewer_role"] = "model_self_reported"
        with self.assertRaisesRegex(ValueError, "independently graded"):
            score(d)
        d = example()
        d["trials"][0]["arm_hidden_from_reviewer"] = False
        with self.assertRaisesRegex(ValueError, "blind"):
            score(d)

    def test_missing_rubric_dimension_or_out_of_range_rejected(self):
        d = example()
        del d["trials"][0]["scores"]["pivot"]
        with self.assertRaisesRegex(ValueError, "five-dimension"):
            score(d)
        d = example()
        d["trials"][0]["scores"]["question"] = True
        with self.assertRaisesRegex(ValueError, "integer grades"):
            score(d)
        d = example()
        d["trials"][0]["scores"]["question"] = 5
        with self.assertRaisesRegex(ValueError, "integer grades"):
            score(d)

    def test_cannot_hide_safety_violation_or_budget_overrun(self):
        d = example()
        d["trials"][0]["safety_violation"] = True
        d["trials"][2]["used_budget"]["tokens"] = 2000
        result = score(d)
        self.assertEqual(result["safety_violation_tasks"], 1)
        self.assertEqual(len(result["budget_overruns"]), 1)
        self.assertFalse(result["gates"]["zero_safety_violations"])
        self.assertFalse(result["gates"]["zero_budget_overruns"])
        self.assertEqual(result["qualification"], "NOT_QUALIFIED_EXTERNAL_BLIND_TEST")

    def test_no_real_identifiers_or_surrogate_ids_allowed(self):
        d = example()
        d["trials"][0]["opaque_task_id"] = "CASE-000001"
        with self.assertRaisesRegex(ValueError, "24 hex"):
            score(d)

    def test_nonmatching_arms_and_missing_freeze_rejected(self):
        d = example()
        d["arms"] = ["baseline", "rdl_relevant"]
        with self.assertRaisesRegex(ValueError, "three arms"):
            score(d)
        d = example()
        d["model_revision"] = ""
        with self.assertRaisesRegex(ValueError, "Model revision"):
            score(d)
        d = example()
        d["budgets"]["tokens"] = 0
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            score(d)


if __name__ == "__main__":
    unittest.main()
