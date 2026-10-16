"""Scout triage must not silently ingest, mirror or approve discoveries."""
import unittest

from tools.triage_source_candidates import canonical_url, triage


class ScoutTriageTests(unittest.TestCase):
    def test_url_normalization_preserves_meaningful_query_and_drops_tracking(self):
        self.assertEqual(canonical_url("https://WWW.Example.com/path/?utm_source=x&v=2#section"),
                         "https://example.com/path?v=2")
        self.assertEqual(canonical_url("https://example.com/path?v=3"),
                         "https://example.com/path?v=3")
        self.assertIsNone(canonical_url("http://example.com/path"))
        self.assertIsNone(canonical_url("https://alice:pass@example.com/path"))
        self.assertIsNone(canonical_url(None))

    def test_duplicate_existing_and_batch_do_not_create_source_records(self):
        sources = [{"id": "SRC-000055", "url": "https://example.org/research/story"}]
        candidates = [
            {"candidate_id": "C1", "linked_original_writeup_url": "https://example.org/research/story?utm_source=x",
             "original_firsthand": "original_firsthand", "source_access": "article_read", "publication_date": "2026-08"},
            {"candidate_id": "C2", "linked_original_writeup_url": "https://new.example/research/first",
             "original_firsthand": "original_firsthand", "source_access": "article_read", "publication_date": "2026-10-02"},
            {"candidate_id": "C3", "linked_original_writeup_url": "https://new.example/research/first#section",
             "original_firsthand": "original_firsthand", "source_access": "article_read", "publication_date": "2026-10-02"}
        ]
        result = triage(candidates, existing_sources=sources)
        self.assertEqual([r["status"] for r in result["items"]],
                         ["duplicate_existing", "candidate_only", "duplicate_in_batch"])
        self.assertEqual((result["existing_duplicates"], result["batch_duplicates"]), (1, 1))
        self.assertTrue(all(r["rights_status"] == "unreviewed" for r in result["items"]))
        self.assertTrue(all(r["historical_events_created"] == 0 for r in result["items"]))
        self.assertEqual(len(sources), 1)

    def test_inaccessible_or_republished_is_reviewed_not_published_as_fact(self):
        result = triage([{"linked_original_writeup_url": "https://research.example/item",
                          "original_firsthand": "commentary", "source_access": "preview_only",
                          "license_review_pending": False}], existing_sources=[])
        row = result["items"][0]
        self.assertIn("firsthand_authorship_not_verified", row["review_reasons"])
        self.assertIn("primary_content_not_confirmed_read", row["review_reasons"])
        self.assertIn("publication_date_not_verified", row["review_reasons"])
        self.assertIn("license_claim_requires_independent_review", row["review_reasons"])
        self.assertEqual(row["promotion_status"], "candidate_only")
        self.assertFalse(row["captured_original_text"])

    def test_bad_candidates_fail_or_remain_blocked(self):
        with self.assertRaises(ValueError):
            triage({}, existing_sources=[])
        result = triage(["not an object", {"url": "ftp://example.com/research"}], existing_sources=[])
        self.assertEqual([r["status"] for r in result["items"]],
                         ["rejected_malformed", "blocked_invalid_primary_url"])


if __name__ == "__main__":
    unittest.main()
