"""Adversarial sidecar tests. No fixture enters the canonical registry."""
import copy
import json
import unittest
from pathlib import Path
from research_reconstruction_lab import inspect, PackError
ROOT=Path(__file__).resolve().parents[1]
SEED=json.loads((ROOT/"examples/fail2ban_candidate_pack.json").read_text(encoding="utf-8"))

class ParallelLabTests(unittest.TestCase):
    def p(self):return copy.deepcopy(SEED)
    def test_sample_keeps_all_truth_unapproved(self):
        result=inspect(self.p())
        self.assertEqual(result["status"],"candidate_unreviewed")
        self.assertFalse(result["truth_promotion_allowed"])
        self.assertFalse(result["predecision_snapshot_approved"])
        self.assertEqual(result["counts"]["claims"],5)
        self.assertEqual(result["connections"][0]["assessment"],"author_reported_unverified_causality")
        self.assertEqual(result["connections"][1]["assessment"],"sequence_only")
        self.assertEqual(result["connections"][2]["assessment"],"unresolved_competing_explanations")
    def test_no_evidence_is_not_hypothesis_refutation(self):
        p=self.p();c=p["claims"][0];c["outcome"]="no_evidence_observed"
        c["hypothesis_effect"]="refuted_in_scope";c["scope"]="one trial";c["discriminator"]="difference"
        with self.assertRaisesRegex(PackError,"does not refute"):inspect(p)
    def test_inconclusive_is_not_hypothesis_refutation(self):
        p=self.p();c=p["claims"][0];c["outcome"]="inconclusive"
        c["hypothesis_effect"]="refuted_in_scope";c["scope"]="one trial";c["discriminator"]="difference"
        with self.assertRaises(PackError):inspect(p)
    def test_refuted_requires_scope_and_discriminator(self):
        p=self.p();c=p["claims"][0];c["hypothesis_effect"]="refuted_in_scope"
        with self.assertRaisesRegex(PackError,"scope"):inspect(p)
        c["scope"]="single malformed input"
        with self.assertRaisesRegex(PackError,"discriminator"):inspect(p)
    def test_sequence_cannot_masquerade_as_motivation(self):
        p=self.p();l=p["links"][1];l["kind"]="motivated";l["alternatives"]=[]
        result=inspect(p)
        self.assertEqual(result["connections"][1]["assessment"],"unresolved_competing_explanations")
        self.assertIn({"id":"L2","code":"order_not_causation"},result["warnings"])
        self.assertIn({"id":"L2","code":"missing_competing_explanations"},result["warnings"])
    def test_explicit_motive_requires_author_account(self):
        p=self.p();p["links"][0]["evidence_refs"]=["E2"]
        with self.assertRaisesRegex(PackError,"author report"):inspect(p)
    def test_analyst_notes_cannot_back_author_claim(self):
        p=self.p();p["evidence"][0]["kind"]="analyst_note"
        with self.assertRaises(PackError):inspect(p)
    def test_unknown_decision_reason_is_flagged(self):
        p=self.p();p["claims"][1]["reason_documented"]=False
        self.assertIn({"id":"C2","code":"decision_reason_unknown"},inspect(p)["warnings"])
    def test_no_events_are_inferred_automatically(self):
        p=self.p();p["claims"]=[];p["links"]=[]
        r=inspect(p)
        self.assertEqual(r["counts"]["claims"],0)
        self.assertFalse(r["legacy_registry_modified"])
    def test_unanchored_author_claim_fails(self):
        p=self.p();p["claims"][0]["evidence_refs"]=[]
        with self.assertRaises(PackError):inspect(p)
    def test_known_at_naive_time_is_rejected(self):
        p=self.p();p["evidence"][0]["known_at"]="2021-06-16T12:00:00"
        with self.assertRaisesRegex(PackError,"timezone unknown"):inspect(p)
        p["evidence"][0]["known_at"]="2021-06-16T12:00:00+03:00"
        r=inspect(p)
        self.assertFalse(r["predecision_snapshot_approved"])
        self.assertIn({"id":"E1","code":"known_at_requires_independent_artifact_validation"},r["warnings"])
    def test_reject_dangling_and_duplicate_ids(self):
        p=self.p();p["links"][0]["from"]="MISSING"
        with self.assertRaises(PackError):inspect(p)
        p=self.p();p["sources"].append(p["sources"][0])
        with self.assertRaises(PackError):inspect(p)
    def test_negative_result_does_not_imply_negative_case_outcome(self):
        r=inspect(self.p());self.assertEqual(r["claims"][0]["hypothesis_effect"],"open")
        self.assertNotIn("case_outcome",r)
if __name__=="__main__":unittest.main()
