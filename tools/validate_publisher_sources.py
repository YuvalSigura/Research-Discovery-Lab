"""Validate curated source discovery configs. Never fetch or mirror websites."""
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    directory = root / "sources" / "publishers"
    index = json.loads((directory / "index.json").read_text(encoding="utf-8"))
    assert index["schema_version"] == "1.0"
    seen_keys, seen_publishers, seen_listing_urls = set(), set(), set()
    for item in index["publishers"]:
        key = item["key"]
        assert key not in seen_keys and key.replace("_", "").isalnum(), key
        seen_keys.add(key)
        path = root / item["config_path"]
        assert path.resolve().is_relative_to(directory.resolve()), "publisher config path escape"
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["schema_version"] == "1.0"
        assert data["publisher"] == item["publisher"]
        assert item["publisher"] not in seen_publishers
        seen_publishers.add(item["publisher"])
        assert data["raw_capture_enabled"] is False, "RAW collection needs separate permission gate"
        assert data["copyright_policy"] == "metadata_and_links_only_until_permission_review"
        assert data["research_listing_urls"], f"{key}: empty listing"
        root_host = urlsplit(data["root_url"]).hostname
        assert root_host, f"{key}: no publisher host"
        for url in data["research_listing_urls"]:
            parsed = urlsplit(url)
            assert parsed.scheme == "https" and parsed.hostname, url
            assert (parsed.hostname == root_host or
                    parsed.hostname.removeprefix("www.") == root_host.removeprefix("www.")), url
            assert url not in seen_listing_urls, f"duplicated listing URL: {url}"
            seen_listing_urls.add(url)
        assert data["exclude_by_default"], f"{key}: unscreened source"
    configured = {p.stem for p in directory.glob("*.json") if p.name != "index.json"}
    assert configured == seen_keys, f"Publisher index drift: {configured ^ seen_keys}"
    return {"publishers": len(seen_keys), "listing_urls": len(seen_listing_urls)}


if __name__ == "__main__":
    print("PASS:", validate())
