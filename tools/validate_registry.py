"""Validate v2 typed registry integrity; Python standard library only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"sources":"SRC","systems":"SYS","environments":"ENV","cases":"CASE","contexts":"CTX","findings":"FND","mechanisms":"MEC","events":"EVT","relations":"REL"}
REQUIRED = {
 "SRC": {"title","publisher","url","capture_status"},
 "SYS": {"name","knowledge"}, "ENV": {"system_refs","knowledge"},
 "CASE": {"source_refs","system_refs","environment_refs","case_kind","analysis_status"},
 "CTX": {"case_ref","snapshot_time","known_observations","unknowns","provenance"},
 "FND": {"case_refs","outcome","provenance"},
 "MEC": {"name","description","status","evidence_refs"},
 "EVT": {"case_ref","kind","statement","provenance"},
 "REL": {"subject","predicate","object","provenance"},
}
LINKS = {"source_refs":"SRC","system_refs":"SYS","environment_refs":"ENV","finding_refs":"FND","mechanism_refs":"MEC","case_refs":"CASE","context_ref":"CTX","previous_event_refs":"EVT","related_mechanisms":"MEC"}

def validate():
    records = {}
    for folder,prefix in KINDS.items():
        path = ROOT / "registry" / folder / "index.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["entity_type"] == prefix
        for item in data["records"]:
            assert item["schema_version"] == "1.0"
            assert re.fullmatch(prefix+r"-[0-9]{6}",item["id"]),item
            assert item["id"] not in records, f"duplicate {item['id']}"
            assert REQUIRED[prefix].issubset(item),item["id"]
            records[item["id"]] = item
    for key,item in records.items():
        for field,prefix in LINKS.items():
            if field not in item: continue
            val = item[field]
            values = val if isinstance(val,list) else ([] if val is None else [val])
            for ref in values:
                assert ref in records, f"{key}: dangling {field} -> {ref}"
                assert ref.startswith(prefix+"-"), f"{key}: wrong type {field} -> {ref}"
        if key.startswith("REL-"):
            for field in ("subject","object"):
                assert item[field] in records, f"{key}: dangling {field}"
        if key.startswith("CASE-"):
            assert item["analysis_status"] in ("not_started","in_progress","reviewed")
    old=json.loads((ROOT/"research/index.json").read_text(encoding="utf-8"))
    crosswalk=json.loads((ROOT/"registry/legacy_crosswalk.json").read_text(encoding="utf-8"))
    assert len(crosswalk["entries"])==old["case_count"]
    assert {x["legacy_id"] for x in crosswalk["entries"]}=={x["id"] for x in old["cases"]}
    for entry in crosswalk["entries"]:
        assert entry["new_case_ref"] in records
        assert (ROOT/entry["legacy_path"]).is_file()
    return len(records)

if __name__=="__main__":
    print(f"PASS: {validate()} registry records and legacy crosswalk validated")
