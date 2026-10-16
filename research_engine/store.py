"""Read-only, source-grounded registries for the Research Retrieval Engine.

A source is not an investigation. Missing records are never synthesized.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

KINDS = ("sources", "cases", "systems", "environments", "contexts",
         "findings", "mechanisms", "events", "relations", "passages")


class ResearchStore:
    """Load indexed research entities. Optional in-memory registries aid isolated tests."""

    def __init__(self, root: Path | str | None = None, *, registries: dict | None = None,
                 validate: bool = True):
        self.root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
        if registries is None:
            if validate:
                from tools.validate_registry import validate as validate_repository
                validate_repository(self.root)
            registries = {
                name: json.loads((self.root / "registry" / name / "index.json").read_text(encoding="utf-8"))["records"]
                for name in KINDS
            }
        self.registries = {name: list(registries.get(name, [])) for name in KINDS}
        self.by_id = {}
        self.kind_by_id = {}
        for kind, records in self.registries.items():
            for record in records:
                rid = record["id"]
                if rid in self.by_id:
                    raise ValueError(f"duplicate entity ID: {rid}")
                self.by_id[rid] = record
                self.kind_by_id[rid] = kind
        self.events_by_case = defaultdict(list)
        self.contexts_by_case = defaultdict(list)
        self.findings_by_case = defaultdict(list)
        self.passages_by_source = defaultdict(list)
        self.relations_by_node = defaultdict(list)
        for event in self.registries["events"]:
            self.events_by_case[event["case_ref"]].append(event)
        for context in self.registries["contexts"]:
            self.contexts_by_case[context["case_ref"]].append(context)
        for finding in self.registries["findings"]:
            for cid in finding.get("case_refs", []):
                self.findings_by_case[cid].append(finding)
        for passage in self.registries["passages"]:
            self.passages_by_source[passage["source_ref"]].append(passage)
        for relation in self.registries["relations"]:
            self.relations_by_node[relation["subject"]].append(relation)
            self.relations_by_node[relation["object"]].append(relation)

    def get(self, entity_id: str, expected_kind: str | None = None) -> dict:
        record = self.by_id.get(entity_id)
        if record is None:
            raise KeyError(f"Unknown research entity: {entity_id}")
        if expected_kind and self.kind_by_id[entity_id] != expected_kind:
            raise ValueError(f"{entity_id} is not a {expected_kind}")
        return record

    def case_sources(self, case_id: str) -> list[dict]:
        case = self.get(case_id, "cases")
        return [self.get(ref, "sources") for ref in case.get("source_refs", [])]

    def case_passages(self, case_id: str) -> list[dict]:
        result = []
        for source in self.case_sources(case_id):
            result.extend(self.passages_by_source.get(source["id"], []))
        return sorted(result, key=lambda p: p["id"])

    def case_relations(self, case_id: str, event_ids: set[str] | None = None) -> list[dict]:
        """Only relations whose endpoints belong to the selected investigation."""
        case = self.get(case_id, "cases")
        accepted = {case_id}
        accepted.update(s["id"] for s in self.case_sources(case_id))
        accepted.update(e["id"] for e in self.events_by_case.get(case_id, []))
        accepted.update(c["id"] for c in self.contexts_by_case.get(case_id, []))
        accepted.update(f["id"] for f in self.findings_by_case.get(case_id, []))
        accepted.update(case.get("system_refs", []))
        accepted.update(case.get("environment_refs", []))
        accepted.update(case.get("mechanism_refs", []))
        if event_ids is not None:
            accepted = accepted.difference(e["id"] for e in self.events_by_case.get(case_id, [])
                                            if e["id"] not in event_ids)
        return sorted((r for r in self.registries["relations"]
                       if r["subject"] in accepted and r["object"] in accepted),
                      key=lambda r: r["id"])
