"""Validate typed research registries and crosswalk. Requires jsonschema."""
import json
import re
import hashlib
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"sources":"SRC","systems":"SYS","environments":"ENV","cases":"CASE","contexts":"CTX","findings":"FND","mechanisms":"MEC","events":"EVT","relations":"REL","passages":"PAS"}
SCHEMAS = {"sources":"source","systems":"system","environments":"environment","cases":"case","contexts":"context","findings":"finding","mechanisms":"mechanism","events":"research_event","relations":"relation","passages":"passage"}
LINKS = {"source_refs":"SRC","system_refs":"SYS","environment_refs":"ENV","finding_refs":"FND","mechanism_refs":"MEC","case_refs":"CASE","case_ref":"CASE","context_ref":"CTX","previous_event_refs":"EVT","related_mechanisms":"MEC","source_ref":"SRC"}

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
        validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
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
        if rid.startswith("EVT-"):
            evidence = item.get("provenance", {})
            if item.get("origin") == "historical":
                require(evidence.get("evidence_status") in {"documented","verified"},
                        f"{rid}: historical claim must be sourced")
                require(bool(evidence.get("source_refs")), f"{rid}: historical source refs missing")
            for anchor in item.get("evidence_anchors", []):
                require(anchor["source_ref"] in records, f"{rid}: dangling evidence anchor")
                require(anchor["source_ref"].startswith("SRC-"), f"{rid}: invalid evidence anchor type")
                require(anchor["source_ref"] in records[item["case_ref"]]["source_refs"],
                        f"{rid}: evidence source not in case")
            timestamps = item.get("timestamps", {})
            if timestamps.get("occurred_at") and timestamps.get("known_at"):
                actual = datetime.fromisoformat(timestamps["occurred_at"].replace("Z","+00:00"))
                known = datetime.fromisoformat(timestamps["known_at"].replace("Z","+00:00"))
                require(actual <= known, f"{rid}: event known before it occurred")
        if rid.startswith("REL-"):
            for anchor in item.get("evidence_anchors", []):
                require(anchor["source_ref"] in records and anchor["source_ref"].startswith("SRC-"),
                        f"{rid}: invalid source anchor")
            if item.get("causal_basis") == "explicit_documented":
                require(item["provenance"]["evidence_status"] in {"documented","verified"},
                        f"{rid}: undocumented explicit causal relation")
                require(bool(item["provenance"]["source_refs"]), f"{rid}: explicit causal link missing source")
        if rid.startswith("PAS-"):
            require(item["source_ref"] in records and item["source_ref"].startswith("SRC-"),
                    f"{rid}: passage lacks valid source")
            expected=hashlib.sha256(item["text"].encode("utf-8")).hexdigest()
            require(item["content_sha256"]==expected, f"{rid}: text/hash mismatch")
            if item["usage_status"]=="licensed_excerpt":
                require(records[item["source_ref"]]["license_status"]=="permitted",
                        f"{rid}: licensed excerpt without recorded permission")
            for cid in item.get("case_refs", []):
                require(cid in records and cid.startswith("CASE-"), f"{rid}: invalid passage case")
                require(item["source_ref"] in records[cid]["source_refs"],
                        f"{rid}: passage case source mismatch")
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
