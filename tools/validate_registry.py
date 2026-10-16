"""Validate typed research registries and crosswalk. Requires jsonschema."""
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"sources":"SRC","systems":"SYS","environments":"ENV","cases":"CASE","contexts":"CTX","findings":"FND","mechanisms":"MEC","events":"EVT","relations":"REL"}
SCHEMAS = {"sources":"source","systems":"system","environments":"environment","cases":"case","contexts":"context","findings":"finding","mechanisms":"mechanism","events":"research_event","relations":"relation"}
LINKS = {"source_refs":"SRC","system_refs":"SYS","environment_refs":"ENV","finding_refs":"FND","mechanism_refs":"MEC","case_refs":"CASE","case_ref":"CASE","context_ref":"CTX","previous_event_refs":"EVT","related_mechanisms":"MEC"}

def require(condition, message):
    if not condition: raise ValueError(message)

def validate(root=ROOT):
    records = {}
    for folder, prefix in KINDS.items():
        path = root / "registry" / folder / "index.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        require(data.get("schema_version") == "1.0" and data.get("entity_type") == prefix, f"{path}: invalid registry header")
        schema = json.loads((root / "schemas" / "v2" / (SCHEMAS[folder]+".schema.json")).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        for item in data["records"]:
            validator.validate(item)
            rid = item["id"]
            require(re.fullmatch(prefix + r"-[0-9]{6}", rid) is not None, f"Invalid identifier: {rid}")
            require(rid not in records, f"Duplicate identifier: {rid}")
            records[rid] = item
    for rid, item in records.items():
        for field, expected_prefix in LINKS.items():
            if field not in item: continue
            value = item[field]
            values = value if isinstance(value, list) else ([] if value is None else [value])
            for target in values:
                require(target in records, f"{rid}: dangling {field} -> {target}")
                require(target.startswith(expected_prefix+"-"), f"{rid}: invalid {field} type: {target}")
        if rid.startswith("REL-"):
            for field in ("subject", "object"):
                require(item[field] in records, f"{rid}: dangling {field}")
        if rid.startswith("SRC-"):
            parts=urlsplit(item["url"])
            require(parts.scheme=="https" and bool(parts.hostname), f"{rid}: invalid URL")
            for case in item.get("case_refs", []):
                require(rid in records[case]["source_refs"], f"{rid}: asymmetric case relationship")
        if rid.startswith("CASE-"):
            for source in item["source_refs"]:
                require(rid in records[source].get("case_refs", []), f"{rid}: asymmetric source relationship")
            if item["analysis_status"]=="reviewed":
                require(bool(item["source_refs"]), f"{rid}: reviewed case has no sources")
    old=json.loads((root/"research/index.json").read_text(encoding="utf-8"))
    cross=json.loads((root/"registry/legacy_crosswalk.json").read_text(encoding="utf-8"))
    require(len(cross["entries"])==old["case_count"], "Crosswalk count mismatch")
    by_id={c["id"]:c for c in old["cases"]}
    require(len(by_id)==old["case_count"], "Legacy duplicate IDs")
    require({e["legacy_id"] for e in cross["entries"]}==set(by_id), "Crosswalk IDs mismatch")
    for entry in cross["entries"]:
        rid=entry["new_case_ref"]; sid=entry["source_registry_ref"]
        require(rid in records and sid in records, "Crosswalk dangling record")
        require(sid in records[rid]["source_refs"], "Crosswalk source/case mismatch")
        require(records[sid]["url"]==entry["source_url"]==by_id[entry["legacy_id"]]["url"], "Crosswalk URL mismatch")
        require((root/entry["legacy_path"]).is_file(), "Missing legacy metadata")
    return {"records":len(records),"sources":sum(k.startswith("SRC-") for k in records),"cases":sum(k.startswith("CASE-") for k in records)}

if __name__=="__main__": print("PASS:",validate())
