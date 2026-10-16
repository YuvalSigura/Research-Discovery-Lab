# RDL PR #5 — Independent-review disposition and remaining scientific gates

**Status:** PROVISIONAL / DO_NOT_PROMOTE / NOT_TRAINING_APPROVED  
**Date:** 2026-10-16  
**Original reviewed head:** `0b70b541b4ba6f04a059f0739dce219ff60d4860`. Subsequent candidate revisions must receive **fresh independent review**.  
**Review basis:** Independent Claude PR #5 review and Grok supervisor verification supplied by the project operator. Neither reviewer certified a historical predecision dataset; the supervisor explicitly noted errors and subjective severity judgments in the initial review.

## Disposition by finding

| Claude ID | Review issue | Treatment in this PR | Status / caveat |
|---|---|---|---|
| P0-2 | CQ-003 silently used `partial_overlap` from unrelated QMP-000001 | Source-bound link to SRC-000055 → QMP-000002 `analogy_only`; schema+registry validator enforce | Structural fix applied; semantic family equivalence still unreviewed |
| P0-3 | CQ-009 `unreviewed_overlap` invalid; QMP has `specialization` | Source-bound SRC-000076 → QMP-000003 `specialization`; canonical schema vocabulary | Structural fix applied |
| P0-4 | CQ-014 TA-H008 source mismatch | Removed unsupported source equivalence; maintained separate conceptual proof guidance. Added TA-H008 vendor-position caveat | Structural fix applied; no claim of independent technical proof from SRC-000031 |
| P0-5 | E01–E14 mirror CQ taxonomy | Demoted to *public calibration checklist only*; independent unseen fixture authors, cross-category cases, ≥25% of independent tasks outside ontology in ≥2 held-out families | Protocol corrected; no actual hidden fixtures built |
| P0-6 | `n >= 3` and no power/IRR | Predeclared paired effect/SD/power with multiplicity/attrition; ≥25% double-rated task-triplets; ordinal agreement plan; design-only preflight validator | Statistical DESIGN preflight exists; empirical N adequacy, IRR and confidence intervals remain unexecuted |
| P0-7 | External FUP-B1/B3 and F1–F12 references unresolved | Cross-project dependency document labels them `UNVERIFIABLE_FROM_THIS_REPO` and distinguishes offline benchmark from live HOMELAB integration | Documentation resolved, external code remains unverified |
| P0-8 | Generic Track A owner could duplicate HOMELAB components | Added named owner collision matrix incl. `ResearchStateStore`, `CoverageLedger`, `SurfaceGraph`, `ApplicationIntelligenceEngine` and `ProofLifecycle` | Checklists added; actual production ownership requires Harness code access |
| P1-1 | CQ-013 XBOW 001/002/011 counted as publisher diversity | Explicit lineage note + per-source publisher lineage field | Structural fix |
| P1-2/P1-3 | SRC-000095 and SRC-000109 assigned to wrong families | Removed SRC-000095 from CQ-005; removed SRC-000109 from CQ-008; retained in their better-grounded families | Analyst assignment corrected; first-party adjudication still needed |
| P1-4 | One uniform `source_basis` hides genre differences | Each source has distinct `source_evidence`, provisional basis, lineage, attribution and caveats | Reviewable estimates; NOT curator-certified |
| P1-5 | CQ-010 unique sourcing absent | CQ-010 is a `cross_cutting_evaluation_lens`, not an independent recurring question family | 15 local IDs = 14 families + 1 lens |
| P1-6 | Relationship vocabulary, MD/JSON phrasing diverged | Normalized to canonical QMP relationship enum and byte-identical question texts; CI validator compares with existing QMP | Structural fix |
| P1-7 | No schema or CI guard | Dedicated restrictive Draft 2020-12 JSON Schema; `validate_registry.py` invokes source/QMP/MD parity check; synthetic negative tests | Automated guard committed, not a curator review |
| P1-8/P1-9 | Placebo content and prereg manifest unconstrained | Independent E0 design validator enforces declared guidance length/digest, frozen core prompt/model/decode metadata and design counts | Assertions about independence remain self-reported; live stimulus-log enforcement not implemented |
| P1-10 | Predecision conditions omit unrelated placebo | E0 baseline/relevant/unrelated defined; E1 SFT/SFT+retrieval explicitly separate | Documentation fixed |
| P1-11/P1-12 | CQ-003 case relation and TA-H002 state owner | Case-specific analogy label; TA-H002 does not assume new hypothesis owner | Design fix; Harness reality pending |
| P2 mirror/deep audit | Assetnote mirrors and later SRC-000048 deep audit not disclosed | Added recovered-publisher provenance and targeted deep audit references | Documented, awaiting curator passage review |
| New principle | Vendor aggregate/publisher claims need their own epistemic lens | Added CQ-015 with SRC-000030/031 vendor position vs SRC-000105/106 self-reported metrics | PROVISIONAL; no independently verified denominators |

## Corrections to the reviewer

- The claim that GPT/Grok's examples were **entirely disjoint** for CQ-001–003 was incorrect: CQ-001 and TB-Q001 share SRC-000008; CQ-003 and TB-Q003 share SRC-000055; CQ-002 remains without shared cited source. A shared cited publication is **not** an independent replication.
- TA-H008's previous conceptual link was not a fabricated historical quote. The mismatched source attribution was still removed so no cross-document evidence connection is implied.
- P0-7/P0-8 were *valid documentary limitations*. They did **not** prove a current HOMELAB runtime architecture defect; the actual code owner mapping was not inspected.
- The separate *withdrawn/downgraded* fabrication concerns around the SRC-000055, SRC-000044/045 and SRC-000048 headings remain withdrawn/downgraded, not treated as active P0 defects.

## Existing and new automation

- `tools/validate_registry.py` validates the provisional JSON using `schemas/v2/rdl_candidate_questions.schema.json`, checks source/QMP link fidelity, rejects any silently changed `TRAINING_BLOCKED` status and compares MD/JSON questions.
- `tests/test_provisional_question_crosswalk.py` tests false QMP upgrades, invented enum values, source mismatches, source/seed errors, Markdown drift, bogus promoted status and stale QMP revision.
- `tools/validate_e0_study_design.py` is an optional future E0 preregistration *metadata preflight*; `tests/test_e0_study_design.py` tests invalid holdout, author collision, underpowered design, unmatched placebo, missing double-rate plan and unpinned prompts.
- Existing `tools/score_paired_trials.py` remains a **descriptive-only**, `rdl.paired_trial.v1` tool; its `n >= 3` format gate cannot independently establish study power or rater validity.
- No ingestion, curation, QPT/QMP promotion, training, historical predecision reconstruction or model-weight updates occur.

## Blocking scientific work after technical repairs

1. **Fresh independent PR re-review** of the new head, including the source-specific QMP and lineages. GPT did not independently certify its own revised ontology.
2. Independent original-source passage adjudication: case/actor/run provenance, crosswalk same-core versus analogy, publisher independence and rights/usage; labels remain provisional until reviewer review is traceable.
3. Independently authored hidden E0 tasks, at least two genuine out-of-ontology categories and preregistered leakage/lineage holdout; no self-generated benchmark answer keys from the CQ rows.
4. Preregister statistical sample-size assumptions, actual paired score data, separate blinded human double ratings, ordinal IRR with CIs, real safety adjudications and multiple-comparison-aware effect reporting. The design preflight cannot prove any of these happened.
5. Before any live integration, audit actual HOMELAB production caller/writer/authorization/proof/secret ownership on an *accessible exact commit* after its P0 release gate. No implementation is approved by RDL docs.

**Decision today:** Suitable for renewed **documentation-only** independent review. **NOT approved** for scientific curation/QPT-QMP promotion, model training or HOMELAB feature deployment.
