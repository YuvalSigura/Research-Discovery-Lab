"""Validate typed research registries and crosswalk. Requires jsonschema."""
import json
import re
import hashlib
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"sources":"SRC","systems":"SYS","environments":"ENV","cases":"CASE","contexts":"CTX","findings":"FND","mechanisms":"MEC","events":"EVT","relations":"REL","passages":"PAS","mindsets":"MND"}
SCHEMAS = {"sources":"source","systems":"system","environments":"environment","cases":"case","contexts":"context","findings":"finding","mechanisms":"mechanism","events":"research_event","relations":"relation","passages":"passage","mindsets":"mindset"}
LINKS = {"source_refs":"SRC","system_refs":"SYS","environment_refs":"ENV","finding_refs":"FND","mechanism_refs":"MEC","case_refs":"CASE","case_ref":"CASE","context_ref":"CTX","previous_event_refs":"EVT","related_mechanisms":"MEC","source_ref":"SRC","event_refs":"EVT","outcome_event_refs":"EVT","prior_art_source_refs":"SRC"}

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
        for holder in ("provenance", "knowledge"):
            evidence = item.get(holder) or {}
            for sid in evidence.get("source_refs", []):
                require(sid in records and sid.startswith("SRC-"),
                        f"{rid}: missing {holder} source {sid}")
        if rid.startswith("CTX-"):
            for obs in item.get("known_observations", []):
                for sid in obs.get("source_refs", []):
                    require(sid in records and sid.startswith("SRC-"),
                            f"{rid}: missing observation source {sid}")
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
        if rid.startswith("MND-"):
            case_id=item["case_ref"]
            cases=set(item["event_refs"]+item["outcome_event_refs"])
            for eid in cases:
                require(eid in records and eid.startswith("EVT-"),
                        f"{rid}: invalid mindset event {eid}")
                require(records[eid]["case_ref"]==case_id,
                        f"{rid}: mindset event crosses case boundary {eid}")
            case_source_ids=set(records[case_id]["source_refs"])
            references=set(item["provenance"]["source_refs"])
            anchors=item["evidence_anchors"]
            for anchor in anchors:
                sid=anchor["source_ref"]
                require(sid in records and sid.startswith("SRC-"),
                        f"{rid}: invalid mindset evidence source {sid}")
                require(sid in case_source_ids,
                        f"{rid}: mindset anchor source outside case {sid}")
                require(sid in references,
                        f"{rid}: mindset anchor absent from provenance {sid}")
            for sid in item.get("prior_art_source_refs", []):
                require(sid in records and sid.startswith("SRC-"),
                        f"{rid}: invalid prior-art source {sid}")
            if item["attribution"] in {"researcher_explicit","observed_research_action"}:
                require(item["provenance"]["evidence_status"] in {"documented","verified"},
                        f"{rid}: documented mindset requires documented evidence")
                require(bool(references and anchors),
                        f"{rid}: sourced mindset requires provenance and anchors")
            else:
                require(item["provenance"]["evidence_status"] in {"proposed","unknown"},
                        f"{rid}: analyst inference must not become documented history")
                require(item["outcome_linkage"]!="researcher_reported_contribution",
                        f"{rid}: inferred mindset cannot claim researcher-reported contribution")
            if item["novelty"]=="originality_candidate":
                require(item.get("comparison_scope")=="within_reviewed_prior_art",
                        f"{rid}: originality needs declared prior-art comparison")
                require(bool(item.get("prior_art_source_refs") and item.get("novelty_basis")),
                        f"{rid}: unsupported originality claim")
                require(item.get("review_status")=="curator_reviewed",
                        f"{rid}: originality requires curator review")
            if item["outcome_linkage"]=="researcher_reported_contribution":
                require(item["attribution"]=="researcher_explicit" and bool(anchors),
                        f"{rid}: outcome contribution needs explicit researcher testimony")
                require(bool(item["outcome_event_refs"]),
                        f"{rid}: outcome contribution without explicit outcome event")
            if item["outcome_linkage"]=="none":
                require(not item["outcome_event_refs"],
                        f"{rid}: outcome links contradict none")
            for eid in item["outcome_event_refs"]:
                require(records[eid]["kind"]=="outcome",
                        f"{rid}: outcome link must reference an outcome event")
        if rid.startswith("CASE-") and "discovery_assessment" in item:
            ass=item["discovery_assessment"]
            all_source_refs=set(ass["evidence_source_refs"]+
                                ass["independent_verification_refs"])
            require(all(sid in records and sid.startswith("SRC-")
                        for sid in all_source_refs),
                    f"{rid}: invalid zero-day evidence source")
            require(all(sid in item["source_refs"] for sid in all_source_refs),
                    f"{rid}: zero-day assessment source outside case")
            if ass["zero_day_status"]!="unassessed":
                require(bool(ass["evidence_source_refs"]),
                        f"{rid}: assessed outcome has no evidence")
            if ass["zero_day_status"]=="corroborated_zero_day":
                require(ass["review_status"]=="reviewed" and
                        bool(ass["independent_verification_refs"]),
                        f"{rid}: zero-day corroboration needs review and independent source")
                require(not set(ass["evidence_source_refs"]).issuperset(
                        ass["independent_verification_refs"]),
                        f"{rid}: zero-day corroboration must use separate source")
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
