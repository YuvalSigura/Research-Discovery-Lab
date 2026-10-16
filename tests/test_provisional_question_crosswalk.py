"""Synthetic negative tests: provisional CQ crosswalk must not silently promote or drift.

No test fixture in this module is a real historical or pre-decision research case.
"""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from jsonschema.exceptions import ValidationError

from tools.validate_registry import ROOT, validate_provisional_question_crosswalk


FILE = "docs/data/RDL_CONSOLIDATED_CANDIDATE_QUESTIONS.v0.json"
MD = "docs/RDL_GPT_GROK_QUESTION_ONTOLOGY_CANDIDATES.md"
SCHEMA = "schemas/v2/rdl_candidate_questions.schema.json"
SEEDS = "ontology/common/research_question_hypotheses.json"
QMP = "registry/question_mappings/index.json"
SOURCES = "registry/sources/index.json"


class ProvisionalQuestionCrosswalkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for rel in (FILE, MD, SCHEMA, SEEDS, QMP):
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, dest)
        self.records = {}
        for rel in (SOURCES, QMP):
            source = json.loads((ROOT / rel).read_text(encoding="utf-8"))
            self.records.update({item["id"]: item for item in source["records"]})
        self.original = json.loads((self.root / FILE).read_text(encoding="utf-8"))

    def write_candidate(self, obj):
        (self.root / FILE).write_text(
            json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    def case(self, cid):
        d = copy.deepcopy(self.original)
        return d, next(item for item in d["candidate_families"] if item["id"] == cid)

    def test_current_crosswalk_passes_but_remains_training_blocked(self):
        result = validate_provisional_question_crosswalk(self.root, self.records)
        self.assertEqual(result["candidate_records"], 15)
        self.assertEqual(result["status"], "PROVISIONAL_TRAINING_BLOCKED")

    def test_cq003_cannot_borrow_cq074_relation(self):
        data, obj = self.case("CQ-003")
        obj["qpt_mapping_proposal"][0]["relationship"] = "partial_overlap"
        self.write_candidate(data)
        with self.assertRaisesRegex(ValueError, "silent relation upgrade"):
            validate_provisional_question_crosswalk(self.root, self.records)

    def test_cq009_cannot_use_invented_relation(self):
        data, obj = self.case("CQ-009")
        obj["qpt_mapping_proposal"][0]["relationship"] = "unreviewed_overlap"
        self.write_candidate(data)
        with self.assertRaises(ValidationError):
            validate_provisional_question_crosswalk(self.root, self.records)

    def test_wrong_existing_qmp_source_fails(self):
        data, obj = self.case("CQ-003")
        obj["qpt_mapping_proposal"][0]["source_ref"] = "SRC-000011"
        self.write_candidate(data)
        with self.assertRaisesRegex(ValueError, "source mismatch"):
            validate_provisional_question_crosswalk(self.root, self.records)

    def test_unknown_source_and_bad_seed_fail(self):
        data, obj = self.case("CQ-015")
        obj["source_ids"][0] = "SRC-999999"
        self.write_candidate(data)
        with self.assertRaisesRegex(ValueError, "Unknown CQ source"):
            validate_provisional_question_crosswalk(self.root, self.records)
        data, obj = self.case("CQ-015")
        obj["seed_refs"][0] = "fabricated_seed"
        self.write_candidate(data)
        with self.assertRaisesRegex(ValueError, "Unknown seed"):
            validate_provisional_question_crosswalk(self.root, self.records)

    def test_unreviewed_training_gate_is_schema_locked(self):
        data, obj = self.case("CQ-001")
        obj["training_status"] = "TRAINING_APPROVED"
        self.write_candidate(data)
        with self.assertRaises(ValidationError):
            validate_provisional_question_crosswalk(self.root, self.records)

    def test_duplicate_id_and_markdown_question_drift_fail(self):
        data = copy.deepcopy(self.original)
        data["candidate_families"].append(copy.deepcopy(data["candidate_families"][0]))
        self.write_candidate(data)
        with self.assertRaisesRegex(ValueError, "Duplicate candidate ID"):
            validate_provisional_question_crosswalk(self.root, self.records)
        data, obj = self.case("CQ-004")
        obj["question"] = "Unreviewed rewrite not matched in Markdown"
        self.write_candidate(data)
        with self.assertRaisesRegex(ValueError, "wording drift"):
            validate_provisional_question_crosswalk(self.root, self.records)

    def test_registry_sha_must_be_exact(self):
        data = copy.deepcopy(self.original)
        data["existing_qmp_registry_sha"] = "a" * 40
        self.write_candidate(data)
        with self.assertRaisesRegex(ValueError, "revision is stale"):
            validate_provisional_question_crosswalk(self.root, self.records)

    def test_source_basis_must_not_look_reviewed(self):
        data, obj = self.case("CQ-015")
        obj["source_evidence"][0]["attribution_status"] = "CURATOR_REVIEWED"
        self.write_candidate(data)
        with self.assertRaises(ValidationError):
            validate_provisional_question_crosswalk(self.root, self.records)


if __name__ == "__main__":
    unittest.main()
