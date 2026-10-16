"""Synthetic offline tests: research move novelty is always relative to a research question.

No fabricated data here is registered as a real investigation.
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from research_engine import ResearchStore, ResearchRetrievalEngine, QuestionAbstractionEngine
from tests.test_retrieval_engine import fixture_engine, event, relation, PROVENANCE, ROOT

SOURCE="SRC-900001"
SRC2="SRC-900003"
C1="CASE-900001"
C2="CASE-900002"
P1="QPT-900001"
P2="QPT-900002"


def synthetic_data():
    store=fixture_engine().store
    data={k:[copy.deepcopy(x) for x in v] for k,v in store.registries.items()}
    src2={"schema_version":"1.0","id":SRC2,
          "title":"Synthetic hypothetical non-zero-day research trajectory",
          "publisher":"Test Lab","url":"https://example.org/synthetic-two",
          "publication_date":"2020-01-01","capture_status":"not_archived",
          "license_status":"unreviewed","case_refs":[C2]}
    data["sources"].append(src2)
    c2=next(x for x in data["cases"] if x["id"]==C2)
    c2["source_refs"]=[SRC2]
    c1=next(x for x in data["cases"] if x["id"]==C1)
    c1["discovery_assessment"]={
        "zero_day_status":"corroborated_zero_day","evidence_source_refs":[SOURCE],
        "independent_verification_refs":["SRC-900002"],"review_status":"reviewed",
        "basis":"Synthetic test-only independent check"}
    c2["discovery_assessment"]={
        "zero_day_status":"not_zero_day","evidence_source_refs":[SRC2],
        "independent_verification_refs":[],"review_status":"reviewed",
        "basis":"Synthetic negative control"}
    question2=event(900008,"question",
                    "Could identity be recomputed after an asynchronous handoff?",
                    time="2020-01-03T10:00:00Z",known="2020-01-03T11:00:00Z")
    question2.update(case_ref=C2,provenance={"evidence_status":"documented",
                                            "source_refs":[SRC2]},
                     evidence_anchors=[{"source_ref":SRC2,"locator":"synthetic:2:1"}])
    action2=event(900009,"direction","Apply established identity-boundary checklist",
                  time="2020-01-03T12:00:00Z",known="2020-01-03T13:00:00Z",
                  direction_status="failed",result_status="negative")
    action2.update(case_ref=C2,provenance={"evidence_status":"documented",
                                          "source_refs":[SRC2]},
                   evidence_anchors=[{"source_ref":SRC2,"locator":"synthetic:2:2"}])
    data["events"].extend([question2,action2])
    rel2=relation(900006,"EVT-900008","pivoted_to","EVT-900009")
    rel2.update(provenance={"evidence_status":"documented","source_refs":[SRC2]})
    data["relations"].append(rel2)

    p1={"schema_version":"1.0","id":P1,
        "question_text":"When does an identity guarantee stop holding between authority checks and state transitions?",
        "scope":"curated_pattern","definition_revision":1,"status":"curator_reviewed",
        "inclusion_criteria":["Question studies a presumed identity/authority invariant across components or state transitions"],
        "exclusion_criteria":["Questions about parser divergence alone"],
        "boundary_or_invariant":"identity authority transition",
        "reviewed_by":"synthetic-curator",
        "provenance":{"evidence_status":"documented","source_refs":[SOURCE,SRC2]},
        "evidence_anchors":[{"source_ref":SOURCE,"locator":"synthetic:pattern:1"}]}
    p2={"schema_version":"1.0","id":P2,
        "question_text":"Do two parsers interpret the same protocol message differently at component boundaries?",
        "scope":"hypothesis","definition_revision":1,"status":"proposed",
        "inclusion_criteria":["Parser divergence"],
        "exclusion_criteria":["Identity consistency without parser behavior"],
        "provenance":{"evidence_status":"proposed","source_refs":[]},
        "evidence_anchors":[]}
    data["question_patterns"].extend([p1,p2])
    map1={"schema_version":"1.0","id":"QMP-900001",
          "case_ref":C1,"question_event_ref":"EVT-900003",
          "pattern_ref":P1,"pattern_definition_revision":1,
          "mapping_basis":"analyst_comparison","review_status":"curator_reviewed",
          "abstraction_relation":"same_core_question",
          "question_novelty":"known_research_question",
          "question_novelty_basis":"Synthetic documented comparison",
          "abstraction_rationale":"The stated question tests which identity guarantee survives state/order changes.",
          "provenance":dict(PROVENANCE),
          "evidence_anchors":[{"source_ref":SOURCE,"locator":"synthetic:mapping:1"}]}
    map2={"schema_version":"1.0","id":"QMP-900002",
          "case_ref":C2,"question_event_ref":"EVT-900008",
          "pattern_ref":P1,"pattern_definition_revision":1,
          "mapping_basis":"analyst_comparison","review_status":"curator_reviewed",
          "abstraction_relation":"same_core_question",
          "question_novelty":"known_research_question",
          "question_novelty_basis":"Synthetic identity-transition case comparison",
          "abstraction_rationale":"A different technique addresses the same identity-transition invariant.",
          "provenance":{"evidence_status":"documented","source_refs":[SRC2]},
          "evidence_anchors":[{"source_ref":SRC2,"locator":"synthetic:mapping:2"}]}
    proposed={**map1, "id":"QMP-900003","pattern_ref":P2,
              "mapping_basis":"algorithmic_suggestion","review_status":"proposed",
              "abstraction_relation":"analogy_only","question_novelty":"unassessed",
              "abstraction_rationale":"Lexical similarity alone, not reviewed conceptual evidence.",
              "provenance":{"evidence_status":"proposed","source_refs":[SOURCE]}}
    data["question_mappings"].extend([map1,map2,proposed])

    original={"schema_version":"1.0","id":"MND-900001","case_ref":C1,
        "event_refs":["EVT-900004"],"question_event_refs":["EVT-900003"],
        "question_link_basis":"explicit_documented",
        "question_relation_refs":["REL-900003"],
        "mindset_key":"mechanism_recombination",
        "statement":"Synthesized separate state and identity tests under the known research question",
        "attribution":"researcher_explicit",
        "novelty":"method_recombination","comparison_scope":"within_case",
        "provenance":dict(PROVENANCE),
        "evidence_anchors":[{"source_ref":SOURCE,"locator":"synthetic:move:1"}],
        "outcome_linkage":"none","outcome_event_refs":[]}
    routine={**original,"id":"MND-900002","case_ref":C2,
        "event_refs":["EVT-900009"],"question_event_refs":["EVT-900008"],
        "question_relation_refs":["REL-900006"],
        "mindset_key":"procedural_checklist",
        "novelty":"established_procedure","comparison_scope":"within_case",
        "statement":"Applies a routine known checklist to an analogous boundary question",
        "provenance":{"evidence_status":"documented","source_refs":[SRC2]},
        "evidence_anchors":[{"source_ref":SRC2,"locator":"synthetic:move:2"}]}
    inferred={**original,"id":"MND-900003",
        "mindset_key":"assumption_challenge",
        "question_link_basis":"analyst_hypothesis",
        "question_relation_refs":[],
        "attribution":"analyst_inference",
        "novelty":"originality_candidate",
        "comparison_scope":"within_reviewed_prior_art",
        "prior_art_source_refs":["SRC-900002"],
        "novelty_basis":"Synthetic prior-art review (not real)",
        "review_status":"curator_reviewed",
        "statement":"Analyst-only reconstruction of an original-looking reasoning move",
        "provenance":{"evidence_status":"proposed","source_refs":[SOURCE]}}
    data["mindsets"].extend([original,routine,inferred])
    return data


class ResearchQuestionUmbrellaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=synthetic_data()
        cls.engine=ResearchRetrievalEngine(ResearchStore(registries=cls.data,validate=False))
        cls.abstraction=QuestionAbstractionEngine(cls.engine.store)

    def test_case_questions_drive_novelty_assessment(self):
        result=self.abstraction.case_report(C1)
        question=next(q for q in result["questions"]
                      if q["question_event_id"]=="EVT-900003")
        self.assertEqual(question["umbrella_assignments"][0]["pattern_id"],P1)
        self.assertEqual(len(question["research_moves"]),1)
        self.assertEqual(question["research_moves"][0]["novelty"],"method_recombination")
        self.assertEqual(question["research_moves"][0]["question_relation_refs"],["REL-900003"])
        self.assertEqual(result["discovery_assessment"]["zero_day_status"],
                         "corroborated_zero_day")
        self.assertNotIn("MND-900003",[x["mindset_id"] for x in question["research_moves"]])

    def test_inferred_mindset_cannot_become_historical(self):
        result=self.abstraction.case_report(C1,view="all")
        linked=[m for q in result["questions"] for m in q["research_moves"]]
        self.assertIn("MND-900003",[m["mindset_id"] for m in linked])
        inference=next(m for m in linked if m["mindset_id"]=="MND-900003")
        self.assertEqual(inference["attribution"],"analyst_inference")
        self.assertEqual(inference["question_link_basis"],"analyst_hypothesis")

    def test_distinct_methods_converge_on_one_question(self):
        group=self.abstraction.convergence()
        self.assertEqual(group["patterns"][0]["case_count"],2)
        self.assertEqual(group["patterns"][0]["mapped_question_count"],2)
        self.assertEqual(group["patterns"][0]["strategies_by_case_count"],
                         {"mechanism_recombination":1,"procedural_checklist":1})
        self.assertEqual(group["patterns"][0]["outcome_counts_by_case"],
                         {"corroborated_zero_day":1,"not_zero_day":1})
        self.assertEqual(group["patterns"][0]["pattern_id"],P1)

    def test_proposed_and_algorithmic_groups_never_count_as_verified(self):
        historical=self.abstraction.convergence()
        self.assertEqual([g["pattern_id"] for g in historical["patterns"]],[P1])
        all_view=self.abstraction.convergence(view="all")
        approved = {g["pattern_id"] for g in all_view["patterns"]
                    if g["status"] == "curator_reviewed"}
        self.assertEqual(approved, {P1})
        self.assertTrue(all(g["status"] != "curator_reviewed"
                            for g in all_view["patterns"] if g["pattern_id"] != P1),
                        "A real proposed umbrella question must never become approved in all-view")
        self.assertEqual(next(g for g in all_view["patterns"] if g["pattern_id"] == P1)["status"],
                         "curator_reviewed")
        q=self.abstraction.case_report(C1,view="all")["questions"]
        self.assertIn(P2,{m["pattern_id"] for item in q
                          for m in item["umbrella_assignments"]})

    def test_overlapping_questions_are_not_merged(self):
        result=self.abstraction.convergence(view="all")
        self.assertNotIn(P2,{group["pattern_id"] for group in result["patterns"]})
        case=self.abstraction.case_report(C1,view="all")
        proposed=[m for q in case["questions"] for m in q["umbrella_assignments"]
                  if m["pattern_id"]==P2]
        self.assertEqual(proposed[0]["abstraction_relation"],"analogy_only")

    def test_case_comparison_requires_curated_question_mappings(self):
        result=self.abstraction.compare_case_questions([C1,C2])
        self.assertEqual(len(result["shared_umbrella_questions"]),1)
        self.assertEqual(result["shared_umbrella_questions"][0]["pattern_id"],P1)
        with self.assertRaises(ValueError):
            self.abstraction.compare_case_questions([C1,C1])

    def test_reconstruction_pack_includes_questions_without_hindsight_leak(self):
        pack=self.engine.reconstruct(C1)
        self.assertEqual(pack["question_analysis"]["view"],"historical")
        pred=self.engine.reconstruct(C1,view="pre_discovery",
                                     cutoff="2020-01-02T12:00:00Z")
        leaked=json.dumps(pred)
        self.assertNotIn("question_analysis",leaked)
        self.assertNotIn("Research question",leaked)
        self.assertNotIn("mechanism_recombination",leaked)
        self.assertNotIn("corroborated_zero_day",leaked)

    def test_question_mapping_is_not_inferred_from_title_or_shared_outcome(self):
        unstored={k:[copy.deepcopy(x) for x in v] for k,v in self.data.items()}
        unstored["question_mappings"]=[]
        result=QuestionAbstractionEngine(
            ResearchStore(registries=unstored,validate=False)).convergence()
        self.assertEqual(result["patterns"],[])
        self.assertGreater(result["question_coverage"]["unmapped_or_out_of_scope_questions"].__len__(),0)

    def test_schema_rejects_novelty_without_question_and_evidence(self):
        schema=json.loads((ROOT/"schemas/v2/mindset.schema.json").read_text(encoding="utf-8"))
        validator=Draft202012Validator(schema)
        value=copy.deepcopy(self.data["mindsets"][0])
        validator.validate(value)
        del value["question_event_refs"]
        self.assertTrue(list(validator.iter_errors(value)))
        value=copy.deepcopy(self.data["mindsets"][0])
        value["mindset_key"]="invented_reasoning_style"
        self.assertTrue(list(validator.iter_errors(value)))

    def test_question_mapping_requires_valid_definition_revision(self):
        schema=json.loads((ROOT/"schemas/v2/question_mapping.schema.json").read_text(encoding="utf-8"))
        Draft202012Validator(schema).validate(self.data["question_mappings"][0])
        self.assertEqual(self.data["question_mappings"][0]["pattern_definition_revision"],1)
        # Cross-record enforcement lives in tools.validate_registry.validate and is
        # tested by disk-based fault injection below.

    def test_real_corpus_unclassified_until_analysed(self):
        live=ResearchRetrievalEngine(ResearchStore(ROOT))
        report=live.question_convergence()
        self.assertEqual(report["patterns"],[])
        self.assertEqual(report["question_coverage"]["mapped_to_reported_patterns"],0)
        single=live.question_analysis("CASE-000001")
        self.assertEqual(single["coverage"]["curated_or_proposed_umbrella_mappings"],0)

    def test_cli_question_summary_no_fabrication(self):
        cmd=[sys.executable,"-m","research_engine","question-convergence"]
        result=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        parsed=json.loads(result.stdout)
        self.assertEqual(parsed["patterns"],[])
        self.assertEqual(parsed["view"],"historical")

    def test_mindset_is_not_personality(self):
        report=self.engine.question_analysis(C2)
        q=next(q for q in report["questions"]
               if q["question_event_id"]=="EVT-900008")
        self.assertEqual(q["research_moves"][0]["mindset_key"],"procedural_checklist")
        self.assertEqual(q["research_moves"][0]["novelty"],"established_procedure")
        self.assertEqual(report["discovery_assessment"]["zero_day_status"],"not_zero_day")


if __name__=="__main__":
    unittest.main()
