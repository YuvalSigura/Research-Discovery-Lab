"""Publisher discovery source contract tests: offline, no web fetching."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.validate_publisher_sources import validate, ROOT


class PublisherSourceTests(unittest.TestCase):
    def test_publisher_source_registry(self):
        result = validate()
        self.assertEqual(result["publishers"], 9)
        self.assertGreaterEqual(result["listing_urls"], 10)

    def test_no_auto_archiving(self):
        index = json.loads((ROOT / "sources/publishers/index.json").read_text(encoding="utf-8"))
        for publisher in index["publishers"]:
            config = json.loads((ROOT / publisher["config_path"]).read_text(encoding="utf-8"))
            self.assertFalse(config["raw_capture_enabled"])


if __name__ == "__main__":
    unittest.main()
