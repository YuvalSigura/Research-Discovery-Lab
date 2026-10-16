"""Test that a seemingly valid archive cannot silently lose historical records."""
import unittest
from tools.check_registry_nonloss import compare_snapshots


class RegistryNonlossTests(unittest.TestCase):
    def setUp(self):
        self.base = {
            "sources": [{"id": "SRC-000001", "url": "https://example.org/one"}],
            "cases": [{"id": "CASE-000001", "source_refs": ["SRC-000001"]}],
            "events": [{"id": "EVT-000001", "case_ref": "CASE-000001", "statement": "Initial finding"}],
            "relations": [{"id": "REL-000001", "subject": "EVT-000001", "object": "EVT-000002"}],
            "legacy_catalog": [{"id": "CASE-000001", "url": "https://example.org/one"}],
        }

    def candidate(self):
        return {kind: [dict(x) for x in values] for kind, values in self.base.items()}

    def test_append_only_is_accepted(self):
        new = self.candidate()
        new["events"].append({"id": "EVT-000002", "case_ref": "CASE-000001"})
        self.assertEqual(compare_snapshots(self.base, new), [])

    def test_missing_event_is_rejected(self):
        new = self.candidate()
        new["events"] = []
        self.assertIn("historical record removed", " ".join(compare_snapshots(self.base, new)))

    def test_missing_whole_registry_is_rejected(self):
        new = self.candidate()
        del new["relations"]
        self.assertIn("registry missing", " ".join(compare_snapshots(self.base, new)))

    def test_source_identity_rewrite_is_rejected(self):
        new = self.candidate()
        new["sources"][0]["url"] = "https://attacker.example/another"
        self.assertIn("source identity changed", " ".join(compare_snapshots(self.base, new)))

    def test_case_source_removed_is_rejected(self):
        new = self.candidate()
        new["cases"][0]["source_refs"] = []
        self.assertIn("lost source refs", " ".join(compare_snapshots(self.base, new)))

    def test_relation_target_rewrite_is_rejected(self):
        new = self.candidate()
        new["relations"][0]["object"] = "EVT-999999"
        self.assertIn("evidence-graph endpoints", " ".join(compare_snapshots(self.base, new)))

    def test_legacy_catalog_deletion_is_rejected(self):
        new = self.candidate()
        new["legacy_catalog"] = []
        self.assertIn("historical record removed", " ".join(compare_snapshots(self.base, new)))

    def test_event_reassignment_is_rejected(self):
        new = self.candidate()
        new["events"][0]["case_ref"] = "CASE-999999"
        self.assertIn("different case", " ".join(compare_snapshots(self.base, new)))

    def test_record_correction_without_deletion_is_permitted(self):
        new = self.candidate()
        new["events"][0]["statement"] = "Corrected source-backed description"
        self.assertEqual(compare_snapshots(self.base, new), [])


if __name__ == "__main__":
    unittest.main()
