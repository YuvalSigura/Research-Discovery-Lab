"""Validate Research Archive catalog and RAW manifests. Python stdlib only."""
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

def validate():
    index = json.loads((ROOT / "research/index.json").read_text(encoding="utf-8"))
    cases = index["cases"]
    assert index["case_count"] == len(cases)
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids)), "Duplicate case IDs"
    urls = [c["url"] for c in cases]
    assert len(urls) == len(set(urls)), "Duplicate URLs"
    for c in cases:
        folder = ROOT / "research/cases" / c["id"]
        meta = json.loads((folder / "metadata.json").read_text(encoding="utf-8"))
        raw = json.loads((folder / "raw/manifest.json").read_text(encoding="utf-8"))
        assert meta["id"] == raw["case_id"] == c["id"]
        assert meta["title"] == c["title"]
        assert meta["sources"][0]["url"] == c["url"]
        assert urlparse(c["url"]).scheme == "https"
        if meta["sources"][0]["original_content_status"] == "not_archived":
            assert not raw["raw_files"], "RAW declared absent but files listed"
    return len(cases)

if __name__ == "__main__":
    print(f"PASS: {validate()} catalogued research cases")
