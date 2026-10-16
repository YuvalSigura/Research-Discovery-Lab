"""Fault-injection checks: each corruption must fail validation."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from tools.validate_registry import ROOT, validate

class RegistryIntegrityTests(unittest.TestCase):
    def test_repository(self):
        result=validate()
        self.assertGreaterEqual(result["sources"],50)
        self.assertEqual(result["sources"],result["cases"])

    def test_schema_files_exist(self):
        from tools.validate_registry import KINDS, SCHEMAS
        for kind in KINDS:
            with self.subTest(kind=kind):
                self.assertTrue((ROOT / "schemas" / "v2" / (SCHEMAS[kind]+".schema.json")).is_file())

    def corrupt_and_reject(self, filename, change):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            shutil.copytree(ROOT/"registry",root/"registry")
            shutil.copytree(ROOT/"schemas",root/"schemas")
            shutil.copytree(ROOT/"research",root/"research")
            path=root/filename
            data=json.loads(path.read_text(encoding="utf-8"))
            change(data)
            path.write_text(json.dumps(data),encoding="utf-8")
            with self.assertRaises(Exception): validate(root)

    def test_dangling_source(self):
        self.corrupt_and_reject("registry/cases/index.json",lambda d:d["records"][0].update(source_refs=["SRC-999999"]))

    def test_invalid_case_kind(self):
        self.corrupt_and_reject("registry/cases/index.json",lambda d:d["records"][0].update(case_kind="invented"))

    def test_duplicate_ids(self):
        self.corrupt_and_reject("registry/sources/index.json",lambda d:d["records"].append(dict(d["records"][0])))

    def test_asymmetric_link(self):
        self.corrupt_and_reject("registry/sources/index.json",lambda d:d["records"][0].update(case_refs=[]))

    def test_crosswalk_mismatch(self):
        self.corrupt_and_reject("registry/legacy_crosswalk.json",lambda d:d["entries"][0].update(source_url="https://example.org/wrong"))

if __name__=="__main__": unittest.main()
