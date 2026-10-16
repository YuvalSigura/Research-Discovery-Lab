"""Evidence-linked research questions, researcher strategies, and open-world umbrella patterns.

No personality profiling. No causal inference from success; no forced clustering.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from .engine import HISTORICAL_EVIDENCE, origin, provenance, status

HISTORICAL_ATTRIBUTIONS = {"researcher_explicit", "observed_research_action"}
ASSESSMENT_KEYS = ("unassessed", "claimed_zero_day", "corroborated_zero_day",
                   "not_zero_day", "disputed")


def _historical_event(event: dict) -> bool:
    return origin(event) == "historical" and status(event) in HISTORICAL_EVIDENCE


def _historical_mindset(item: dict, store) -> bool:
    """Historical view includes actions/questions explicitly connected in source evidence."""
    if not (item["attribution"] in HISTORICAL_ATTRIBUTIONS
            and status(item) in HISTORICAL_EVIDENCE
            and item["question_link_basis"] == "explicit_documented"):
        return False
    if not all(_historical_event(store.get(eid, "events"))
               for eid in item["event_refs"] + item["question_event_refs"]):
        return False
    for relation_id in item["question_relation_refs"]:
        relation = store.get(relation_id, "relations")
        if (status(relation) not in HISTORICAL_EVIDENCE
                or relation.get("causal_basis") != "explicit_documented"):
            return False
    return True


def _reviewed_mapping(item: dict, store) -> bool:
    pattern = store.get(item["pattern_ref"], "question_patterns")
    question = store.get(item["question_event_ref"], "events")
    return (item["review_status"] == "curator_reviewed"
            and pattern["status"] == "curator_reviewed"
            and status(item) in HISTORICAL_EVIDENCE
            and _historical_event(question))


class QuestionAbstractionEngine:
    """Curated many-to-many question -> umbrella pattern -> mindset -> outcome analysis."""

    def __init__(self, store):
        self.store = store

    def case_report(self, case_id: str, *, view: str = "historical") -> dict:
        """Novel moves must be read through the question that motivated them.

        Historical view excludes retrospective inferred links and proposed groupings.
        """
        self.store.get(case_id, "cases")
        if view not in {"historical", "all"}:
            raise ValueError("case_report supports historical or all; not pre_discovery")
        all_questions = sorted((e for e in self.store.events_by_case.get(case_id, [])
                                if e["kind"] == "question"
                                and (view == "all" or _historical_event(e))),
                               key=lambda e: e["id"])
        question_ids = {e["id"] for e in all_questions}
        observations = sorted(
            (o for o in self.store.mindsets_by_case.get(case_id, [])
             if view == "all" or _historical_mindset(o, self.store)),
            key=lambda x: x["id"])
        mappings = sorted(
            (m for m in self.store.question_mappings_by_case.get(case_id, [])
             if m["question_event_ref"] in question_ids
             and (view == "all" or _reviewed_mapping(m, self.store))),
            key=lambda x: x["id"])
        question_to_map = defaultdict(list)
        question_to_mindset = defaultdict(list)
        for m in mappings:
            question_to_map[m["question_event_ref"]].append(m)
        for mind in observations:
            for qid in mind["question_event_refs"]:
                if qid in question_ids:
                    question_to_mindset[qid].append(mind)

        cases = []
        for question in all_questions:
            qid = question["id"]
            assigned = question_to_map[qid]
            moves = question_to_mindset[qid]
            cases.append({
                "question_event_id": qid,
                "question": question["statement"],
                "origin": origin(question),
                "evidence_status": status(question),
                "prior_event_refs": question.get("previous_event_refs", []),
                "umbrella_assignments": [
                    {
                        "mapping_id": item["id"], "pattern_id": item["pattern_ref"],
                        "umbrella_question": self.store.get(
                            item["pattern_ref"], "question_patterns")["question_text"],
                        "revision": item["pattern_definition_revision"],
                        "mapping_basis": item["mapping_basis"],
                        "review_status": item["review_status"],
                        "abstraction_rationale": item["abstraction_rationale"],
                        "mismatches": item.get("mismatches", []),
                        "evidence_anchors": item["evidence_anchors"]
                    } for item in assigned
                ],
                "research_moves": [
                    {
                        "mindset_id": m["id"],
                        "mindset_key": m["mindset_key"],
                        "action_event_refs": m["event_refs"],
                        "statement": m["statement"],
                        "novelty": m["novelty"],
                        "novelty_basis": m.get("novelty_basis"),
                        "prior_art_source_refs": m.get("prior_art_source_refs", []),
                        "question_link_basis": m["question_link_basis"],
                        "question_relation_refs": m["question_relation_refs"],
                        "attribution": m["attribution"],
                        "outcome_linkage": m["outcome_linkage"],
                        "outcome_event_refs": m["outcome_event_refs"],
                        "evidence_status": status(m),
                        "evidence_anchors": m["evidence_anchors"]
                    } for m in moves
                ]
            })
        used_m = {m["mindset_id"] for q in cases for m in q["research_moves"]}
        total_m = {m["id"] for m in observations}
        case = self.store.get(case_id, "cases")
        assessment = case.get("discovery_assessment") or {"zero_day_status": "unassessed"}
        return {
            "case_id": case_id, "view": view, "questions": cases,
            "discovery_assessment": assessment,
            "coverage": {
                "documented_or_proposed_questions": len(all_questions),
                "observed_strategy_labels": len(observations),
                "question_linked_strategy_labels": len(used_m),
                "unlinked_strategy_ids": sorted(total_m - used_m),
                "curated_or_proposed_umbrella_mappings": len(mappings),
                "unmapped_questions": sorted(
                    q["question_event_id"] for q in cases if not q["umbrella_assignments"]),
                "question_strategy_unknowns": sorted(
                    q["question_event_id"] for q in cases if not q["research_moves"])
            },
            "note": ("A linked question explains what is being investigated, not proof that"
                     " a researcher consciously adopted a stated mindset. Historical and"
                     " retrospective reconstruction are separate.")
        }

    def convergence(self, *, view: str = "historical",
                    minimum_cases: int = 1, limit: int = 100) -> dict:
        """Explore whether different procedures converge on common research questions.

        Only curated mappings count in historical view. No statistics or causality are inferred.
        """
        if view not in {"historical", "all"}:
            raise ValueError("convergence supports historical or all")
        if minimum_cases < 1 or not 1 <= limit <= 500:
            raise ValueError("minimum_cases must be positive and limit 1..500")
        groups = []
        for pattern in self.store.registries["question_patterns"]:
            if view == "historical" and pattern["status"] != "curator_reviewed":
                continue
            raw_mappings = self.store.mappings_by_pattern[pattern["id"]]
            mappings = [
                m for m in raw_mappings if view == "all" or _reviewed_mapping(m, self.store)
            ]
            # Deduplicate cases and questions independently, never count multiple
            # techniques or source articles as independent successes.
            included_cases = {m["case_ref"] for m in mappings}
            if len(included_cases) < minimum_cases:
                continue
            outcomes = Counter()
            for cid in included_cases:
                case = self.store.get(cid, "cases")
                assess = case.get("discovery_assessment") or {}
                outcome = assess.get("zero_day_status", "unassessed")
                outcomes[outcome] += 1
            methods = defaultdict(set)
            originality = []
            for m in mappings:
                cid, qid = m["case_ref"], m["question_event_ref"]
                for mindset in self.store.mindsets_by_case[cid]:
                    if qid not in mindset["question_event_refs"]:
                        continue
                    if view == "historical" and not _historical_mindset(mindset, self.store):
                        continue
                    methods[mindset["mindset_key"]].add(cid)
                    if mindset["novelty"] in {"originality_candidate", "method_recombination"}:
                        originality.append({
                            "case_id": cid, "question_id": qid, "mindset_id": mindset["id"],
                            "novelty": mindset["novelty"],
                            "question_link_basis": mindset["question_link_basis"]
                        })
            cases = sorted(included_cases)
            groups.append({
                "pattern_id": pattern["id"],
                "question_text": pattern["question_text"],
                "definition_revision": pattern["definition_revision"],
                "status": pattern["status"],
                "scope": pattern["scope"],
                "inclusion_criteria": pattern["inclusion_criteria"],
                "exclusion_criteria": pattern["exclusion_criteria"],
                "case_count": len(cases),
                "case_ids": cases,
                "mapped_question_count": len({(m["case_ref"],m["question_event_ref"])
                                              for m in mappings}),
                "mapping_ids": sorted(m["id"] for m in mappings),
                "strategies_by_case_count": {
                    method: len(case_ids) for method,case_ids in sorted(methods.items())
                },
                "apparently_original_moves_under_this_question": sorted(
                    originality, key=lambda x: x["mindset_id"]),
                "outcome_counts_by_case": {
                    key: outcomes[key] for key in ASSESSMENT_KEYS if outcomes[key]
                },
                "interpretation": (
                    "Question equivalence is curator-approved only in historical view;"
                    " outcome counts are descriptive and do not establish that a"
                    " question, strategy or degree of originality caused a zero-day.")
            })
        groups.sort(key=lambda g: (-g["case_count"], g["pattern_id"]))
        counted = {cid for g in groups for cid in g["case_ids"]}
        all_cases = self.store.registries["cases"]
        analyzed_cases = {c["id"] for c in all_cases
                          if self.store.events_by_case.get(c["id"])}
        all_questions = [
            q for q in self.store.registries["events"]
            if q["kind"] == "question" and (view == "all" or _historical_event(q))
        ]
        recognized = {(m["case_ref"],m["question_event_ref"]) for g in groups
                      for mid in g["mapping_ids"]
                      for m in [self.store.get(mid,"question_mappings")]}
        return {
            "view": view, "minimum_cases": minimum_cases,
            "patterns": groups[:limit], "total_patterns_with_sufficient_cases": len(groups),
            "question_coverage": {
                "eligible_question_count": len(all_questions),
                "mapped_to_reported_patterns": len(recognized),
                "unmapped_or_out_of_scope_questions": sorted([
                    q["id"] for q in all_questions if
                    (q["case_ref"],q["id"]) not in recognized
                ]),
                "cases_with_any_research_events": len(analyzed_cases),
                "cases_in_reported_patterns": len(counted),
                "catalogue_case_count": len(all_cases)
            },
            "epistemic_limits": [
                "Candidate families are open-world: novel questions may require new patterns.",
                "Routine and original moves may share a question without sharing implementation.",
                "Outcomes and research moves are separately curated; no zero-day causality claim.",
                "Published cases are selected, dependent and subject to survivorship bias.",
                "Counts are descriptive, not a statistical estimate of zero-day likelihood.",
                "Questions without reviewed mappings remain unclassified rather than forced."
            ]
        }

    def compare_case_questions(self, case_ids: list[str], *, view: str = "historical") -> dict:
        """Retrieve the shared umbrella question mappings for arbitrary case comparisons."""
        if not 2 <= len(set(case_ids)) <= 50 or len(set(case_ids)) != len(case_ids):
            raise ValueError("Supply 2..50 distinct investigation IDs")
        reports = [self.case_report(cid, view=view) for cid in case_ids]
        by_pattern = defaultdict(lambda: defaultdict(list))
        for report in reports:
            for q in report["questions"]:
                for mapping in q["umbrella_assignments"]:
                    by_pattern[mapping["pattern_id"]][report["case_id"]].append(q["question_event_id"])
        overlap = []
        for pid, case_map in by_pattern.items():
            if len(case_map) < 2:
                continue
            pattern = self.store.get(pid, "question_patterns")
            overlap.append({
                "pattern_id": pid, "question_text": pattern["question_text"],
                "case_question_refs": {cid: sorted(set(qids))
                                       for cid,qids in sorted(case_map.items())},
                "evidence": "explicit_curated_mappings" if view=="historical"
                            else "may_include_proposed_analyst_mappings"
            })
        overlap.sort(key=lambda r: r["pattern_id"])
        return {
            "case_ids": case_ids, "view": view, "shared_umbrella_questions": overlap,
            "cases_without_question_coverage": [
                x["case_id"] for x in reports if not x["questions"]],
            "interpretation": "Question convergence does not assert novelty, shared mechanism or causation."
        }
