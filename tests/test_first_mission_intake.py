"""Evidence-first first-mission intake regression checks (stdlib only)."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def registry(kind):
    return json.loads((ROOT / "registry" / kind / "index.json").read_text(encoding="utf-8"))["records"]

class FirstMissionIntakeTests(unittest.TestCase):
    def setUp(self):
        self.sources = {x["id"]: x for x in registry("sources")}
        self.cases = {x["id"]: x for x in registry("cases")}
        self.events = registry("events")
        self.relations = registry("relations")

    def test_sources_are_rights_aware_and_cases_remain_unreviewed(self):
        required = {
            "SRC-000073": "https://portswigger.net/research/how-i-choose-a-security-research-topic",
            "SRC-000074": "https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/",
        }
        for sid, url in required.items():
            with self.subTest(sid=sid):
                source = self.sources[sid]
                self.assertEqual(source["url"], url)
                self.assertEqual(source["capture_status"], "not_archived")
                self.assertIsNone(source["sha256"])
                self.assertEqual(source["license_status"], "unreviewed")
                case = self.cases["CASE-" + sid.removeprefix("SRC-")]
                self.assertNotEqual(case["analysis_status"], "reviewed")
                self.assertEqual(case["discovery_assessment"]["zero_day_status"], "unassessed")
                self.assertEqual(case["discovery_assessment"]["review_status"], "not_reviewed")

    def test_source_anchors_and_no_fabricated_history_clock(self):
        expected_cases = {"CASE-000073": 8, "CASE-000074": 14, "CASE-000002": 5}
        for cid, minimum in expected_cases.items():
            case_events = [x for x in self.events if x["case_ref"] == cid]
            if cid == "CASE-000002":
                case_events = [x for x in case_events if int(x["id"].split("-")[1]) > 18]
            self.assertGreaterEqual(len(case_events), minimum)
            for event in case_events:
                with self.subTest(event=event["id"]):
                    self.assertEqual(event["provenance"]["evidence_status"], "documented")
                    self.assertIn(event["evidence_anchors"][0]["source_ref"], self.cases[cid]["source_refs"])
                    self.assertTrue(event["evidence_anchors"][0]["locator"].startswith("section"))
                    self.assertIsNone(event["timestamps"]["occurred_at"])
                    self.assertIsNone(event["timestamps"]["known_at"])
                    self.assertEqual(event["hindsight_review"], "not_reviewed")

    def test_genuine_negative_vs_blocked_vs_stopped(self):
        mobi = [x for x in self.events if x["case_ref"] == "CASE-000074"]
        self.assertTrue(any(x.get("result_status") == "negative" for x in mobi))
        self.assertTrue(any(x.get("direction_status") == "blocked" and
                            x.get("result_status") == "not_applicable" for x in mobi))
        self.assertTrue(any(x.get("direction_status") == "abandoned" and
                            "certificate" in x["statement"].lower() for x in mobi))
        self.assertFalse(any("successfully issued a rogue certificate" in x["statement"].lower() for x in mobi))

    def test_no_self_approved_mindset_or_umbrella_convergence(self):
        for kind in ("mindsets", "question_patterns", "question_mappings"):
            for item in registry(kind):
                self.assertNotIn(item.get("case_ref"), {"CASE-000073", "CASE-000074"})
        for link in self.relations:
            if int(link["id"].split("-")[1]) <= 19:
                continue
            self.assertIn(link["subject"], {x["id"] for x in self.events})
            self.assertIn(link["object"], {x["id"] for x in self.events})
            self.assertEqual(link["hindsight_review"], "not_reviewed")
            self.assertIsNone(link["known_at"])

if __name__ == "__main__":
    unittest.main()
