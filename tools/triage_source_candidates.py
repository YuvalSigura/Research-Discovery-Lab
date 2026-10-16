"""Rights-aware, read-only triage of scout candidate JSON into an intake review queue.

Never fetches webpages, mirrors publisher content, writes registry records,
manufactures stable SRC IDs, or treats a candidate as an approved investigation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

ROOT = Path(__file__).resolve().parents[1]
_TRACKING = {"fbclid", "gclid", "mc_cid", "mc_eid"}


def canonical_url(raw: object) -> str | None:
    if not isinstance(raw, str):
        return None
    raw = raw.strip()
    try:
        u = urlsplit(raw)
        if u.scheme.lower() != "https" or not u.hostname or u.username or u.password:
            return None
        if u.port not in (None, 443):
            port = f":{u.port}"
        else:
            port = ""
        host = (u.hostname or "").lower()
        if host.startswith("www."):
            host = host[4:]
        kept = [(key, value) for key, value in parse_qsl(u.query, keep_blank_values=True)
                if not key.lower().startswith("utm_") and key.lower() not in _TRACKING]
        path = (u.path or "/").rstrip("/") or "/"
        return urlunsplit(("https", host + port, path, urlencode(sorted(kept)), ""))
    except ValueError:
        return None


def triage(candidates: list[dict], *, existing_sources: list[dict]) -> dict:
    if not isinstance(candidates, list):
        raise ValueError("Scout input must be a JSON array")
    indexed = {}
    for item in existing_sources:
        url = canonical_url(item.get("url"))
        if url:
            indexed.setdefault(url, item["id"])
    seen = {}
    rows = []
    for i, item in enumerate(candidates):
        if not isinstance(item, dict):
            rows.append({"position": i, "status": "rejected_malformed", "reasons": ["candidate_not_object"]})
            continue
        url = canonical_url(item.get("linked_original_writeup_url") or item.get("canonical_url") or item.get("url"))
        original_post = canonical_url(item.get("original_x_permalink"))
        reasons = []
        if not url:
            reasons.append("no_verified_https_primary_url")
        attribution = str(item.get("original_firsthand") or item.get("source_attribution") or "").lower()
        if attribution not in {"original_firsthand", "firsthand", "first_party"}:
            reasons.append("firsthand_authorship_not_verified")
        access = str(item.get("source_access") or "").lower().replace(" ", "_")
        if access not in {"article_read", "post_read", "full_text_read"}:
            reasons.append("primary_content_not_confirmed_read")
        if not item.get("publication_date"):
            reasons.append("publication_date_not_verified")
        if item.get("license_review_pending") is False:
            # A scout cannot grant re-publication permission; separate rights
            # review remains mandatory even if a candidate marks it false.
            reasons.append("license_claim_requires_independent_review")
        if url and url in indexed:
            status = "duplicate_existing"
            reasons.append("already_catalogued")
        elif url and url in seen:
            status = "duplicate_in_batch"
            reasons.append("same_primary_url_as_earlier_candidate")
        elif not url:
            status = "blocked_invalid_primary_url"
        else:
            status = "candidate_only"
        if url and url not in seen:
            seen[url] = i
        rows.append({
            "position": i,
            "candidate_id": item.get("candidate_id"),
            "primary_url": url,
            "original_x_permalink": original_post,
            "existing_source_ref": indexed.get(url) if url else None,
            "status": status,
            "review_reasons": sorted(set(reasons)),
            "rights_status": "unreviewed",
            "promotion_status": "candidate_only",
            "historical_events_created": 0,
            "captured_original_text": False
        })
    return {"format": "rdl.scout.triage.v1", "total_candidates": len(rows),
            "candidate_only_count": sum(r["status"] == "candidate_only" for r in rows),
            "existing_duplicates": sum(r["status"] == "duplicate_existing" for r in rows),
            "batch_duplicates": sum(r["status"] == "duplicate_in_batch" for r in rows),
            "rejected_invalid": sum(r["status"].startswith(("rejected_", "blocked_")) for r in rows),
            "items": rows}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidates", type=Path, help="JSON array from the discovery scout; never auto-ingested")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        data = json.loads(args.candidates.read_text(encoding="utf-8"))
        sources = json.loads((args.root / "registry" / "sources" / "index.json").read_text(encoding="utf-8"))["records"]
        print(json.dumps(triage(data, existing_sources=sources), indent=2, ensure_ascii=False))
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
