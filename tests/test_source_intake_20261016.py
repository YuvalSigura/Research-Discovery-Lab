"""Cataloguing is not scientific validation."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def get(kind):return json.loads((ROOT/"registry"/kind/"index.json").read_text(encoding="utf-8"))["records"]
class IntakeTests(unittest.TestCase):
 def test_source_identity_and_rights(self):
  sources=get("sources");fresh=[s for s in sources if int(s["id"].split("-")[1])>=78]
  self.assertEqual(len(sources),109);self.assertEqual(len(fresh),32)
  self.assertEqual(len({s["url"].lower().rstrip("/") for s in sources}),len(sources))
  self.assertTrue(all(s["license_status"]=="unreviewed" and s["capture_status"]=="not_archived" and s["sha256"] is None for s in fresh))
 def test_fail_closed_new_case_science(self):
  fresh=[c for c in get("cases") if int(c["id"].split("-")[1])>=78]
  self.assertEqual(len(fresh),32)
  self.assertTrue(all(c["analysis_status"]=="not_started" and c["provenance"]["evidence_status"]=="unknown" and c["discovery_assessment"]["zero_day_status"]=="unassessed" for c in fresh))
  self.assertFalse(any(int(e["case_ref"].split("-")[1])>=78 for e in get("events")))
 def test_crosswalk_preserved(self):
  r=json.loads((ROOT/"research/index.json").read_text(encoding="utf-8"));x=json.loads((ROOT/"registry/legacy_crosswalk.json").read_text(encoding="utf-8"))
  self.assertEqual(r["case_count"],109)
  self.assertEqual([c["id"] for c in r["cases"]],[e["legacy_id"] for e in x["entries"]])
  self.assertEqual(len(list((ROOT/"research/cases").glob("CASE-*/metadata.json"))),109)
if __name__=="__main__":unittest.main()
