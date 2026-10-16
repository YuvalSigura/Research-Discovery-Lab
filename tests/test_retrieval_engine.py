"""Offline black-box tests for search, chronology, decisions, provenance and leakage."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

from research_engine import ResearchRetrievalEngine, ResearchStore
from research_engine.engine import iso_time

ROOT = Path(__file__).resolve().parents[1]
EARLY = "2020-01-01"
PROVENANCE = {"evidence_status": "documented", "source_refs": ["SRC-900001"],
              "notes": "SYNTHETIC TEST ONLY"}


def event(number, kind, statement, *, time=None, known=None, **other):
    value = {"schema_version": "1.0", "id": f"EVT-{number:06d}",
             "case_ref": "CASE-900001", "kind": kind, "statement": statement,
             "origin": "historical",
             "hindsight_review": "passed",
             "provenance": dict(PROVENANCE),
             "timestamps": {"occurred_at": time, "known_at": known},
             "evidence_anchors": [{"source_ref": "SRC-900001",
                                    "locator": f"synthetic-test:{number}"}]}
    value.update(other)
    return value


def relation(number, subject, predicate, obj, *, basis="explicit_documented",
             known="2020-01-06T00:00:00Z"):
    return {"schema_version": "1.0", "id": f"REL-{number:06d}",
            "subject": subject, "predicate": predicate, "object": obj,
            "causal_basis": basis, "hindsight_review": "passed", "known_at": known,
            "provenance": dict(PROVENANCE)}


def fixture_engine():
    """Synthetic data are never committed into the archive registry."""
    base = ResearchStore(ROOT)
    data = {name: list(records) for name, records in base.registries.items()}
    src = {"schema_version": "1.0", "id": "SRC-900001",
           "title": "SECRET FINAL ANSWER: test exploit chain",
           "publisher": "Synthetic", "url": "https://example.org/fictional",
           "publication_date": EARLY, "capture_status": "not_archived",
           "license_status": "unreviewed", "sha256": None,
           "case_refs": ["CASE-900001"]}
    late = dict(src, id="SRC-900002", title="Later published retrospective",
                url="https://example.org/later", publication_date="2022-01-01",
                case_refs=["CASE-900001"])
    data["sources"].extend([src, late])
    cas = {"schema_version": "1.0", "id": "CASE-900001",
           "source_refs": ["SRC-900001", "SRC-900002"],
           "system_refs": [], "environment_refs": [],
           "mechanism_refs": ["MEC-900001"], "domain_labels": ["cloud_identity"],
           "analysis_status": "in_progress", "case_kind": "vulnerability",
           "provenance": dict(PROVENANCE)}
    other = dict(cas, id="CASE-900002", source_refs=[], domain_labels=["web_api"])
    data["cases"].extend([cas, other])
    data["mechanisms"].append({"schema_version": "1.0", "id": "MEC-900001",
                                "name": "Time-of-check/time-of-use assumption",
                                "description": "SYNTHETIC challenge of a stale authorization assumption",
                                "status": "candidate", "evidence_refs": []})
    data["events"].extend([
        event(900001, "assumption", "Assume authorization never changes during processing",
              time="2020-01-02T01:00:00Z", known="2020-01-02T02:00:00Z",
              assumption_status="challenged", assumption_basis="design claim"),
        event(900002, "direction", "Try an identity-change experiment",
              time="2020-01-03T01:00:00Z", known="2020-01-03T02:00:00Z",
              direction_status="failed", result_status="negative",
              expected_outcome="mismatched identity", actual_outcome="no mismatch observed",
              information_gained="identity remains stable in this configuration"),
        event(900003, "question", "Would ordering, rather than identity, change the outcome?",
              time="2020-01-04T01:00:00Z", known="2020-01-04T02:00:00Z"),
        event(900004, "direction", "Explore a later state transition",
              time="2020-01-05T01:00:00Z", known="2020-01-05T02:00:00Z",
              direction_status="attempted"),
        event(900005, "direction", "Consider alternate component boundary",
              time=None, known=None, direction_status="not_tested",
              blocking_reason="No authorized environment for this option"),
        event(900006, "direction", "Hypothetical avenue that never historically occurred",
              time=None, known=None, origin="counterfactual",
              provenance={"evidence_status": "proposed", "source_refs": []},
              direction_status="not_tested"),
        event(900007, "question", "Retrospective question not knowable at cutoff",
              time="2020-01-02T01:30:00Z", known="2020-01-02T03:00:00Z",
              provenance={"evidence_status": "documented", "source_refs": ["SRC-900002"]}),
    ])
    data["relations"].extend([
        relation(900001, "EVT-900001", "challenged_assumption", "EVT-900002"),
        relation(900002, "EVT-900002", "raised_question", "EVT-900003"),
        relation(900003, "EVT-900003", "pivoted_to", "EVT-900004"),
        relation(900004, "EVT-900001", "followed_by", "EVT-900003",
                 basis="temporal_only"),
        relation(900005, "EVT-900003", "motivated_by", "EVT-900001",
                 basis="reconstructed"),
    ])
    data["contexts"].append({
        "schema_version": "1.0", "id": "CTX-900001", "case_ref": "CASE-900001",
        "snapshot_time": "2020-01-02T02:00:00Z",
        "known_observations": [{"text": "Early state transition documented",
                                "source_refs": ["SRC-900001"]}],
        "unknowns": ["Later test outcome not yet observable"], "hindsight_review": "passed",
        "provenance": dict(PROVENANCE)
    })
    original = "Independent authored analysis: early authorization observation"
    excerpt = "UNLICENSED FULL TEXT MUST NOT BE RETURNED"
    data["passages"].extend([
        {"schema_version": "1.0", "id": "PAS-900001", "source_ref": "SRC-900001",
         "text": original, "locator": "synthetic note 1", "usage_status": "original_analysis",
         "content_sha256": hashlib.sha256(original.encode()).hexdigest()},
        {"schema_version": "1.0", "id": "PAS-900002", "source_ref": "SRC-900002",
         "text": excerpt, "locator": "synthetic note 2", "usage_status": "licensed_excerpt",
         "content_sha256": hashlib.sha256(excerpt.encode()).hexdigest()}
    ])
    return ResearchRetrievalEngine(ResearchStore(registries=data, validate=False))


class RetrievalEngineTests(unittest.TestCase):
    def setUp(self):
        self.engine = fixture_engine()

    def test_real_catalog_is_searchable(self):
        live = ResearchRetrievalEngine(ResearchStore(ROOT))
        matches = live.search("Chrome", kinds=["sources"])
        self.assertTrue(matches["results"])
        self.assertIn("source_count", live.reconstruct("CASE-000001")["coverage"])

    def test_real_catalog_does_not_invent_trajectory(self):
        live = ResearchRetrievalEngine(ResearchStore(ROOT))
        pack = live.reconstruct("CASE-000001")
        self.assertEqual(pack["coverage"]["status"], "metadata_only")
        self.assertEqual(pack["timeline"], [])
        self.assertEqual(pack["relations"], [])
        self.assertTrue(pack["warnings"])

    def test_ordered_and_unplaced_are_distinct(self):
        pack = self.engine.reconstruct("CASE-900001", view="historical")
        self.assertEqual([x["event_id"] for x in pack["timeline"]],
                         ["EVT-900001", "EVT-900007", "EVT-900002",
                          "EVT-900003", "EVT-900004"])
        self.assertEqual(pack["chronology_unknown"], ["EVT-900005"])
        self.assertIn("EVT-900002", pack["failed_or_negative"])
        self.assertIn("EVT-900005", pack["untried"])
        self.assertIn("EVT-900001", pack["challenged_assumptions"])
        self.assertEqual(pack["pivots"], ["REL-900003"])
        self.assertNotIn("EVT-900006", [x["id"] for x in pack["events"]])

    def test_counterfactual_kept_separate(self):
        all_view = self.engine.reconstruct("CASE-900001", view="all")
        event = next(x for x in all_view["events"] if x["id"] == "EVT-900006")
        self.assertEqual(event["origin"], "counterfactual")
        self.assertEqual(event["provenance"]["evidence_status"], "proposed")

    def test_pre_discovery_blocks_hindsight_and_titles(self):
        pack = self.engine.reconstruct("CASE-900001", view="pre_discovery",
                                       cutoff="2020-01-02T12:00:00Z")
        self.assertEqual([x["id"] for x in pack["events"]], ["EVT-900001"])
        self.assertEqual(pack["relations"], [])
        self.assertEqual(len(pack["contexts"]), 1)
        txt = json.dumps(pack)
        self.assertNotIn("SECRET FINAL ANSWER", txt)
        self.assertNotIn("Retrospective question", txt)
        self.assertNotIn("no mismatch observed", txt)
        self.assertNotIn("2022-01-01", txt)
        self.assertNotIn("Time-of-check/time-of-use", txt)

    def test_pre_discovery_is_fail_closed(self):
        with self.assertRaises(ValueError):
            self.engine.reconstruct("CASE-900001", view="pre_discovery")
        with self.assertRaises(ValueError):
            self.engine.reconstruct("CASE-900001", view="pre_discovery",
                                    cutoff="2020-01-02")  # timezone mandatory

    def test_explicit_question_provenance(self):
        trace = self.engine.trace_question("CASE-900001", "EVT-900003")
        self.assertEqual({x["from"] for x in trace["causal_steps"]},
                         {"EVT-900001", "EVT-900002"})
        self.assertNotIn("REL-900004",
                         {x["relation_id"] for x in trace["causal_steps"]})
        self.assertNotIn("REL-900005",
                         {x["relation_id"] for x in trace["causal_steps"]})

    def test_inferred_relation_only_in_all_mode(self):
        trace = self.engine.trace_question("CASE-900001", "EVT-900003", view="all")
        self.assertIn("REL-900005", {x["relation_id"] for x in trace["causal_steps"]})

    def test_license_is_fail_closed(self):
        pack = self.engine.reconstruct("CASE-900001")
        self.assertEqual([p["id"] for p in pack["passages"]], ["PAS-900001"])
        search = self.engine.search("UNLICENSED", kinds=["passages"])
        self.assertEqual(search["total_matches"], 0)
        self.assertEqual(self.engine.search("Independent", kinds=["passages"])["total_matches"], 1)

    def test_structured_search_and_scope(self):
        found = self.engine.search("authorization", kinds=["events"],
                                   filters={"case_id": "CASE-900001"})
        self.assertGreater(found["total_matches"], 0)
        filtered = self.engine.search("", kinds=["sources"], filters={"publisher": "Synthetic"})
        self.assertEqual(filtered["total_matches"], 2)
        with self.assertRaises(ValueError):
            self.engine.search("")
        with self.assertRaises(ValueError):
            self.engine.search("abc", filters={"unexpected": "x"})

    def test_related_cases_need_explicit_match(self):
        r = self.engine.related_cases("CASE-900001")
        self.assertIn("CASE-900002", [x["case_id"] for x in r["related"]])
        self.assertEqual(r["related"][0]["shared_mechanism_refs"], ["MEC-900001"])

    def test_parses_timezone_only(self):
        self.assertEqual(iso_time("2020-01-02T12:00:00+00:00"),
                         iso_time("2020-01-02T12:00:00Z"))
        with self.assertRaises(ValueError):
            iso_time("2020-01-02T12:00:00")

    def test_cli_end_to_end(self):
        command = [sys.executable, "-m", "research_engine", "coverage", "CASE-000001"]
        p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)["coverage"]["status"], "metadata_only")


if __name__ == "__main__":
    unittest.main()
