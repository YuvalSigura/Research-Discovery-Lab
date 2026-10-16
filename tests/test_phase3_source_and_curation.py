"""Phase-3 primary-source intake and independent curation queue checks."""
import json
import unittest

from research_engine import QuestionAbstractionEngine, ResearchStore
from tools.build_curator_queue import ROOT, build


def get_records(kind):
    return json.loads((ROOT / "registry" / kind / "index.json").read_text(encoding="utf-8"))["records"]


class Phase3SourceChecks(unittest.TestCase):
    def test_github_security_lab_is_one_methodology_case_not_twenty_negative_cases(self):
        source = next(s for s in get_records("sources") if s["id"] == "SRC-000077")
        case = next(c for c in get_records("cases") if c["id"] == "CASE-000077")
        self.assertEqual(source["capture_status"], "not_archived")
        self.assertEqual(source["license_status"], "unreviewed")
        self.assertIsNone(source["sha256"])
        self.assertEqual(case["case_kind"], "methodology")
        self.assertEqual(case["analysis_status"], "in_progress")
        self.assertEqual(case["discovery_assessment"]["zero_day_status"], "unassessed")
        es = [e for e in get_records("events") if e["case_ref"] == "CASE-000077"]
        self.assertEqual(len(es), 12)
        self.assertEqual(sum(e["kind"] == "outcome" for e in es), 1)
        for e in es:
            self.assertEqual(e["hindsight_review"], "not_reviewed")
            self.assertIsNone(e["timestamps"]["known_at"])
            self.assertIsNone(e["timestamps"]["occurred_at"])
            self.assertTrue(e["evidence_anchors"])
            self.assertEqual(e["evidence_anchors"][0]["source_ref"], "SRC-000077")
            self.assertEqual(e["provenance"]["evidence_status"],
                             "proposed" if e["origin"] == "reconstructed" else "documented")

    def test_aggregate_unreproduced_candidates_not_labelled_as_proven_safe(self):
        es = {e["id"]: e for e in get_records("events")}
        self.assertEqual(es["EVT-000086"]["result_status"], "inconclusive")
        self.assertIn("not 20 individually reconstructed", es["EVT-000086"]["actual_outcome"])
        self.assertNotIn("verified", es["EVT-000090"]["actual_outcome"].lower())
        self.assertEqual(len([e for e in get_records("events") if e["case_ref"] == "CASE-000077"
                              and e.get("result_status") == "negative"]), 0)

    def test_only_unreviewed_mindset_observations_and_no_automatic_question_convergence(self):
        ms = [m for m in get_records("mindsets") if m["case_ref"] == "CASE-000077"]
        self.assertEqual(len(ms), 2)
        self.assertEqual({m["attribution"] for m in ms},
                         {"researcher_explicit", "analyst_inference"})
        self.assertEqual({m["provenance"]["evidence_status"] for m in ms},
                         {"documented", "proposed"})
        self.assertTrue(all(m.get("novelty") == "unassessed" for m in ms))
        self.assertTrue(all(m.get("review_status") != "curator_reviewed" for m in ms))
        self.assertEqual(QuestionAbstractionEngine(ResearchStore()).convergence()["patterns"], [])

    def test_source_case_links_are_bidirectional_and_no_licensed_passage_is_assumed(self):
        source = next(s for s in get_records("sources") if s["id"] == "SRC-000077")
        case = next(c for c in get_records("cases") if c["id"] == "CASE-000077")
        self.assertEqual(source["case_refs"], ["CASE-000077"])
        self.assertEqual(case["source_refs"], ["SRC-000077"])
        self.assertFalse(any(p["source_ref"] == "SRC-000077" for p in get_records("passages")))


class CuratorQueueChecks(unittest.TestCase):
    def test_case_queue_exposes_reconstructed_question_and_limited_anchors(self):
        report = build(ROOT, case_id="CASE-000077")
        self.assertEqual(report["case_count"], 1)
        self.assertEqual(report["events_to_review"], 12)
        self.assertEqual(report["relations_to_review"], 11)
        packet = report["packets"][0]
        self.assertEqual(packet["status"], "independent_review_pending")
        self.assertEqual(packet["approved_predecision_snapshots"], 0)
        self.assertTrue(all(e["curator_decision"] == "pending" for e in packet["event_review"]))
        inferred = next(e for e in packet["event_review"] if e["event_id"] == "EVT-000080")
        self.assertIn("analyst_reconstruction_not_historical_truth", inferred["review_flags"])
        self.assertIn("source_anchor_not_immutable", inferred["review_flags"])
        causal = next(r for r in packet["relation_review"] if r["relation_id"] == "REL-000074")
        self.assertIn("causal_claim_requires_source_recheck", causal["review_flags"])

    def test_existing_case_queue_does_not_make_unreviewed_data_historical_truth(self):
        report = build(ROOT, case_id="CASE-000076")
        self.assertEqual(report["case_count"], 1)
        self.assertEqual(report["packets"][0]["status"], "independent_review_pending")
        self.assertEqual(report["packets"][0]["approved_predecision_snapshots"], 0)
        self.assertIn("distinguish_failed_test_from_disproved_hypothesis",
                      report["flag_totals"])
        with self.assertRaises(ValueError):
            build(ROOT, case_id="CASE-999999")

    def test_catalogue_only_cases_omitted_from_default_review_queue(self):
        report = build(ROOT)
        self.assertGreaterEqual(report["case_count"], 6)
        self.assertLess(report["case_count"], 77)
        self.assertEqual(report["adjudication"].split(" - ")[0], "NONE")
        self.assertFalse(any(p["status"] == "curator_reviewed" for p in report["packets"]))


if __name__ == "__main__":
    unittest.main()
