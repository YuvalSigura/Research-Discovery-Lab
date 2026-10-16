"""Phase 2 evidence integrity and blind-evaluation negative controls."""
import json
import tempfile
import unittest
from pathlib import Path

from tools.curation_readiness import ROOT, report
from tools.build_predecision_candidates import build


def load(kind):
    return json.loads((ROOT / "registry" / kind / "index.json").read_text(encoding="utf-8"))["records"]


class Phase2IntakeTests(unittest.TestCase):
    def test_new_cases_are_documented_but_not_claimed_verified(self):
        sources = {x["id"]: x for x in load("sources")}
        cases = {x["id"]: x for x in load("cases")}
        for n, expected_kind in [(75, "exploit_chain"), (76, "negative_result")]:
            with self.subTest(case=n):
                sid, cid = f"SRC-{n:06}", f"CASE-{n:06}"
                self.assertIn(sid, sources)
                self.assertIn(cid, cases)
                self.assertEqual(sources[sid]["capture_status"], "not_archived")
                self.assertEqual(sources[sid]["license_status"], "unreviewed")
                self.assertIsNone(sources[sid]["sha256"])
                self.assertEqual(cases[cid]["case_kind"], expected_kind)
                self.assertEqual(cases[cid]["discovery_assessment"]["zero_day_status"], "unassessed")
                self.assertEqual(cases[cid]["discovery_assessment"]["review_status"], "not_reviewed")

    def test_retrospectives_cannot_gain_synthetic_history(self):
        events = [e for e in load("events") if e["case_ref"] in {"CASE-000075", "CASE-000076"}]
        self.assertEqual(len(events), 33)
        self.assertEqual(sum(e["case_ref"] == "CASE-000075" for e in events), 20)
        self.assertEqual(sum(e["case_ref"] == "CASE-000076" for e in events), 13)
        for e in events:
            self.assertIsNone(e["timestamps"]["occurred_at"])
            self.assertIsNone(e["timestamps"]["known_at"])
            self.assertEqual(e["hindsight_review"], "not_reviewed")
            self.assertTrue(e["evidence_anchors"])
            if e["origin"] == "reconstructed":
                self.assertEqual(e["provenance"]["evidence_status"], "proposed")
            else:
                self.assertEqual(e["provenance"]["evidence_status"], "documented")
        self.assertTrue(any(e["origin"] == "reconstructed" and e["kind"] == "question" for e in events))
        negative = [e for e in events if e["case_ref"] == "CASE-000076"]
        self.assertTrue(any(e["kind"] == "outcome" and e["result_status"] == "negative" for e in negative))
        self.assertFalse(any("independently verified" in e["statement"].lower() for e in negative))

    def test_question_abstraction_remains_unreviewed(self):
        self.assertGreaterEqual(len(load("mindsets")), 4)
        self.assertEqual(len(load("question_patterns")), 2)
        self.assertEqual(len(load("question_mappings")), 3)
        self.assertTrue(all(q["review_status"] == "proposed" for q in load("question_mappings")))
        self.assertTrue(all(q["status"] == "proposed" for q in load("question_patterns")))
        from research_engine import ResearchStore, QuestionAbstractionEngine
        actual = QuestionAbstractionEngine(ResearchStore()).convergence()
        self.assertEqual(actual["patterns"], [])

    def test_readiness_exposes_missing_approvals_and_never_invents_them(self):
        single = report(ROOT, case_id="CASE-000075")
        self.assertEqual(single["summary"]["cases"], 1)
        row = single["cases"][0]
        self.assertEqual(row["events"], 20)
        self.assertEqual(row["approved_predecision_snapshots"], 0)
        self.assertIn("no_approved_predecision_snapshot", row["flags"])
        self.assertIn("source_rights_unreviewed", row["flags"])
        self.assertIn("no_reviewed_question_equivalence", row["flags"])
        with self.assertRaises(ValueError):
            report(ROOT, case_id="CASE-999999")


class BlindCandidateTests(unittest.TestCase):
    def make_root(self, *, cutoff="2024-02-01T12:00:00Z", published="2024-01-01",
                  review="passed", observation_refs=None, evidence="documented"):
        directory = tempfile.TemporaryDirectory()
        root = Path(directory.name)
        data = {
            "sources": [{"id": "SRC-900001", "publication_date": published}],
            "cases": [{"id": "CASE-900001", "source_refs": ["SRC-900001"]}],
            "contexts": [{"id": "CTX-900001", "case_ref": "CASE-900001",
                          "snapshot_time": cutoff,
                          "hindsight_review": review,
                          "provenance": {"evidence_status": evidence, "source_refs": ["SRC-900001"]},
                          "known_observations": [{"text": "A documented observation of ordinary behavior",
                                                   "source_refs": observation_refs if observation_refs is not None else ["SRC-900001"]}],
                          "unknowns": ["Why did a normal transition happen?"],
                          "capabilities": ["An authorized read"],
                          "constraints": ["Do not mutate target state"]}]
        }
        for kind, records in data.items():
            path = root / "registry" / kind / "index.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"records": records}), encoding="utf-8")
        return directory, root

    def test_no_real_snapshot_is_not_an_imaginary_benchmark(self):
        pack = build(ROOT, secret="a private fixture key 32 bytes")
        self.assertEqual(pack["task_count"], 0)
        self.assertEqual(pack["status"], "human_review_required")

    def test_eligible_context_exports_source_free_review_candidate(self):
        temp, root = self.make_root()
        try:
            pack = build(root, secret="a private fixture key 32 bytes")
            self.assertEqual(pack["task_count"], 1)
            task = pack["tasks"][0]
            self.assertTrue(task["review_only"])
            serialized = json.dumps(task)
            self.assertNotIn("CASE-900001", serialized)
            self.assertNotIn("SRC-900001", serialized)
            self.assertNotIn("2024-02-01", serialized)
            self.assertNotIn("correct_answer", serialized)
            self.assertNotIn("outcome", serialized)
            self.assertEqual(len(task["opaque_task_id"]), 24)
            self.assertEqual(task["opaque_task_id"],
                             build(root, secret="a private fixture key 32 bytes")["tasks"][0]["opaque_task_id"])
            self.assertNotEqual(task["opaque_task_id"],
                                build(root, secret="a different private key 32 bytes")["tasks"][0]["opaque_task_id"])
        finally:
            temp.cleanup()

    def test_fail_closed_on_invalid_cutoffs_review_and_sources(self):
        for options, reason in [
            ({"cutoff": None}, "missing_or_invalid_exact_cutoff"),
            ({"cutoff": "2024-02-01"}, "missing_or_invalid_exact_cutoff"),
            ({"review": "not_reviewed"}, "hindsight_review_not_passed"),
            ({"evidence": "proposed"}, "snapshot_not_documented"),
            ({"published": "2024-02-01"}, "source_not_certainly_published_before_cutoff"),
            ({"published": "2025-01-01"}, "source_not_certainly_published_before_cutoff"),
            ({"published": "2024-01"}, "publication_day_unverified"),
            ({"observation_refs": []}, "observation_without_source"),
            ({"observation_refs": ["SRC-900002"]}, "source_not_in_case")
        ]:
            with self.subTest(options=options):
                temp, root = self.make_root(**options)
                try:
                    pack = build(root, secret="a private fixture key 32 bytes")
                    self.assertEqual(pack["task_count"], 0)
                    self.assertIn(reason, pack["excluded"][0]["reasons"])
                finally:
                    temp.cleanup()

    def test_private_key_required(self):
        with self.assertRaises(ValueError):
            build(ROOT, secret="short")


if __name__ == "__main__":
    unittest.main()
