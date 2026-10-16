"""Synthetic E0 study-design controls: no model trials or external claims."""
import copy
import unittest

from tools.validate_e0_study_design import validate_design


def fixture_design(n=8):
    sha = "a" * 64
    fixtures = []
    for i in range(n):
        tid = f"{i + 1:024x}"
        fixtures.append({
            "opaque_task_id": tid,
            "fixture_author_id": "independent-fixture-author",
            "fixture_digest_sha256": sha,
            "source_lineage_separation_reviewed": True,
            "gold_answer_key_sealed": True,
            "taxonomy_holdout": i < 2,
            "hidden_category_id": ("unseen-topic-" + str(i)) if i < 2 else "",
            "guidance": {
                "rdl_relevant": {"sha256": sha, "token_count": 100},
                "rdl_unrelated": {"sha256": "b" * 64, "token_count": 102},
            },
        })
    return {
        "format": "rdl.e0.preregistered_design.v1",
        "arms": ["baseline", "rdl_relevant", "rdl_unrelated"],
        "preregistration_id": "synthetic-design-only",
        "model_revision": "fixed-model-revision",
        "tokenizer_revision": "fixed-tokenizer",
        "retrieval_corpus_revision": "frozen-corpus",
        "fixture_set_revision": "hidden-fixtures-v1",
        "base_prompt_sha256": sha,
        "retrieval_corpus_sha256": sha,
        "fixture_manifest_sha256": sha,
        "decoding_parameters": {"temperature": 0},
        "context_window_tokens": 4096,
        "authors": {
            "ontology": ["ontology-writer"],
            "retrieval_guidance": ["guidance-writer"],
            "fixture": ["independent-fixture-author"],
            "reviewer": ["independent-rater-a", "independent-rater-b"],
        },
        "independence_attestations": {
            "fixture_authors_blind_to_ontology": True,
            "reviewers_blind_to_arms": True,
            "hidden_keys_separated": True,
            "source_near_duplicate_screened": True,
        },
        "independent_fixture_protocol_ref": "hypothetical-independent-protocol",
        "power_plan": {
            "two_sided_alpha": 0.05,
            "target_power": 0.80,
            "minimum_detectable_difference": 2.0,
            "assumed_paired_difference_sd": 1.0,
            "anticipated_attrition_fraction": 0.10,
            "multiplicity": "bonferroni_two_primary_contrasts",
            "assumptions_basis": "synthetic-only plausible test values",
            "cluster_dependence_review": "synthetic independent tasks; no publisher link",
        },
        "fixtures": fixtures,
        "rating_plan": {
            "agreement_metric": "quadratic_weighted_cohen_kappa",
            "minimum_acceptable_agreement": 0.60,
            "confidence_interval_method": "preregistered bootstrap by task",
            "low_agreement_disposition": "no_go",
            "planned_double_rated_task_ids": [f"{i + 1:024x}" for i in range(2)],
        },
    }


class E0StudyDesignTests(unittest.TestCase):
    def test_valid_design_is_metadata_only(self):
        result = validate_design(fixture_design())
        self.assertEqual(result["planned_paired_tasks"], 8)
        self.assertEqual(result["unseen_category_families_declared"], 2)
        self.assertIn("METADATA", result["qualification"])
        self.assertNotIn("TRAINING_APPROVED", result["qualification"])

    def test_ontology_author_must_not_author_hidden_fixtures(self):
        d = fixture_design()
        d["authors"]["fixture"] = ["ontology-writer"]
        with self.assertRaisesRegex(ValueError, "Fixture authors"):
            validate_design(d)

    def test_holdout_requires_independent_unknown_categories(self):
        d = fixture_design()
        d["fixtures"][1]["taxonomy_holdout"] = False
        with self.assertRaisesRegex(ValueError, "holdout"):
            validate_design(d)
        d = fixture_design()
        d["fixtures"][1]["hidden_category_id"] = "CQ-001"
        with self.assertRaisesRegex(ValueError, "Unseen categories"):
            validate_design(d)

    def test_placebo_must_be_token_length_matched(self):
        d = fixture_design()
        d["fixtures"][0]["guidance"]["rdl_unrelated"]["token_count"] = 150
        with self.assertRaisesRegex(ValueError, "length mismatch"):
            validate_design(d)

    def test_three_pairs_do_not_count_as_statistical_power(self):
        d = fixture_design(3)
        d["rating_plan"]["planned_double_rated_task_ids"] = ["000000000000000000000001"]
        with self.assertRaisesRegex(ValueError, "power|holdout|Insufficient planned"):
            validate_design(d)
        d = fixture_design()
        d["power_plan"]["assumed_paired_difference_sd"] = 5.0
        with self.assertRaisesRegex(ValueError, "Insufficient planned"):
            validate_design(d)

    def test_double_rating_plan_and_blinding_are_required(self):
        d = fixture_design()
        d["rating_plan"]["planned_double_rated_task_ids"].pop()
        with self.assertRaisesRegex(ValueError, "Double rating"):
            validate_design(d)
        d = fixture_design()
        d["independence_attestations"]["reviewers_blind_to_arms"] = False
        with self.assertRaisesRegex(ValueError, "attestation"):
            validate_design(d)

    def test_prompt_revision_and_frozen_decoding_required(self):
        d = fixture_design()
        d["base_prompt_sha256"] = ""
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            validate_design(d)
        d = fixture_design()
        d["decoding_parameters"] = {}
        with self.assertRaisesRegex(ValueError, "Decoding parameters"):
            validate_design(d)


if __name__ == "__main__":
    unittest.main()
