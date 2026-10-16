# RDL — GPT × Grok Consolidated Research-Question Ontology (CANDIDATE v0)

**Status:** PROVISIONAL / REVIEW_REQUIRED / TRAINING_BLOCKED  
**Date:** 2026-10-16  
**Scope:** Research-principle consolidation, not training, not an authoritative QPT/QMP promotion, not a HOMELAB implementation authorization.

## 0. What this consolidation is — and is not

This is an **analyst-authored candidate crosswalk**. It combines:
- Grok's eight provisional `TB-Q001…TB-Q008` questions and corresponding `TA-H001…TA-H008` candidate guidance;
- GPT's bounded primary-source case notes and deeper candidate X→Y analyses;
- the existing open-world seed ontology in `ontology/common/research_question_hypotheses.json`;
- the two **already proposed, not curator-approved** patterns `QPT-000001/2` and mappings `QMP-000001…3`.

The first-party articles, not either model's paraphrase, remain the evidence to be reviewed. **Agreement between GPT and Grok over the same article does not provide two independent witnesses.** Two accounts of the same Chrome research (`SRC-000001/002`) are one lineage, not two replications. Sequential and parallel research runs must not be merged into a fictional single decision chronology.

This is **not a complete adjudication** of all 109 sources; the associations below are *candidate semantic matches*. Where a proposed family has two source IDs, this is not automatically evidence of independent convergence. Several included studies are methodology or retrospective forensics, not original investigator diaries. Sources SRC-000001, SRC-000002 **and SRC-000011** share XBOW publisher lineage; SRC-000044/045 share the Assetnote/Searchlight Cyber lineage; SRC-000007/other repeated publishers cannot be double-counted as independent replications. Nothing in this document creates real historical `known_at` data, an accepted gold next step, or training approval.

**Read-only source basis:** 
- [Grok questions](../grok/principles/TRACK_B_CANDIDATE_QUESTIONS.md) and [Grok Harness heuristics](../grok/principles/TRACK_A_CANDIDATE_HEURISTICS.md)
- [GPT 001–002](../gpt/cases/XBOW_SRC_000001_000002_INDEPENDENT_ANALYSIS.md), [GPT 003–010](../gpt/cases/XBOW_SRC_000003_000010_INDEPENDENT_ANALYSIS.md), [GPT 011–023](../gpt/cases/XBOW_SRC_000011_000023_INDEPENDENT_ANALYSIS.md)
- [GPT 024–043](../gpt/cases/RDL_SRC_000024_000043_PRIMARY_SOURCE_PASS.md), [GPT 044–072](../gpt/cases/RDL_SRC_000044_000072_SOURCE_AUDIT.md), [targeted deep audit](../gpt/cases/RDL_TARGETED_DEEP_X_TO_Y_AUDIT.md)
- [GPT 073–082](../gpt/cases/RDL_SRC_000073_000082_DEEPER_REVIEW.md), [083–092](../gpt/cases/RDL_SRC_000083_000092_DEEPER_REVIEW.md), [093–102](../gpt/cases/RDL_SRC_000093_000102_DEEPER_REVIEW.md), [103–109](../gpt/cases/RDL_SRC_000103_000109_DEEPER_REVIEW.md), [deep audit 026/094/095/107](../gpt/cases/RDL_SRC_000026_000094_000095_000107_DEEP_PRIMARY_AUDIT.md)
- [Question-first methodology](QUESTION_FIRST_RESEARCH.md), [current QPT registry](../registry/question_patterns/index.json), [current QMP registry](../registry/question_mappings/index.json).

All candidate examples below identify an **article section or technical subject**, not an immutable first-party passage capture. The curator must acquire/verifiably locate source passages before upgrading any assertion.

**Machine-readable candidate view:** [RDL_CONSOLIDATED_CANDIDATE_QUESTIONS.v0.json](data/RDL_CONSOLIDATED_CANDIDATE_QUESTIONS.v0.json) contains 15 local IDs (14 provisional question families and one cross-cutting evaluation lens) with aligned question text, source IDs, seed crosswalk, epistemic labels, boundary warnings and explicit training prohibition. All 46 source-ID references (31 unique) were checked against the 109-source registry, and all seed references against the existing ontology. This is **structural validation only**, not source-fidelity adjudication.

## 1. Rule for semantic merging

Two questions may be proposed as the **same core question** only if their relevant uncertainty, preconditions, discriminating experiment, and counterexample remain equivalent after removing product/technique-specific terms. Similar exploit classes, endpoint labels, tool names, or successful outcomes are insufficient.

Allowed relationships are the canonical QMP schema values `same_core_question`, `specialization`, `partial_overlap`, `analogy_only`, and `unresolved`. The first is **not** asserted by any unreviewed Grok crosswalk in this revision. All mappings below are **unreviewed analyst proposals**, not accepted `QMP` records.

Techniques (single-packet timing, micro-fragment prompting, lookup slowdown, debug-route exploration) are examples/strategies, **not automatically distinct universal questions**. Equally, a question about instrument error is not automatically a question about absent prerequisite.

## 2. Consolidated candidate families

The `CQ-xxx` IDs are *local candidate IDs only*. `CQ-010` is explicitly a **cross-cutting evaluation lens**, not an independent question family; `CQ-015` is an additional, provisional question about publisher/vendor self-report validity. Therefore, 15 local records represent 14 candidate question families and one lens. They are **not** new canonical `QPT` IDs and must not be imported into the registry without independent review.

| Candidate | Central falsifiable question | Grok relation (proposed) | GPT first-party research illustrations | HOMELAB role / confidence |
|---|---|---|---|---|
| **CQ-001 Scoped negative** | Which exact scope does a negative observation refute, and what remains untested? | TB-Q001: partial_overlap | SRC-000008 "Vulnerability Analysis"; SRC-000078 negative Fail2ban audit; SRC-000107 "Step 5" | Model question + scoped evidence metadata; multi-source provisional |
| **CQ-002 Blockage semantics** | Is a path blocked by authorization, missing state, cost, or actual experimental refutation? | TB-Q002: analogy_only | SRC-000022 "Initial Code Analysis"; SRC-000073 "Fast failure"; SRC-000104 competition objective shift | Typed research-state distinction; multi-source provisional |
| **CQ-003 Missing prerequisite** | Which missing prerequisite makes a blocked direction testable, if obtaining it is authorized? | TB-Q003: partial_overlap; QPT-000001: **SRC-000055 → QMP-000002 analogy_only** (SRC-000074 → QMP-000001 partial_overlap is distinct, not cited) | SRC-000055 "The Almost-Bug / Stepping Back"; SRC-000011 "From URL to Arbitrary File Read"; SRC-000086 "Vulnerability #2" | Prerequisite hypothesis / planner proposal; multi-source provisional |
| **CQ-004 Trigger versus capability** | What does a validated trigger support, versus a demonstrated reusable capability? | TB-Q004: partial_overlap | SRC-000024 "Evaluation / Weaponization"; SRC-000022 "Bypassing Authentication" | Claim-scoped experiment levels; provisional |
| **CQ-005 Contract/invariant challenge** | Which specification or implementation invariant can be tested for counterexamples? | TB-Q005: partial_overlap | SRC-000089 "Creating a quality fuzzing suite"; SRC-000002 "Two WebPs Diverged" | Model hypothesis generation; provisional |
| **CQ-006 Cross-component interpretation** | Do separate components or authorities disagree in interpreting input, paths, or security state? | TB-Q006: partial_overlap | SRC-000044 "Weird Apache Behavior"; SRC-000045 "Building a More Reliable Check"; SRC-000059 "Gmail's Files Scanner Bypass" | Boundary-model candidate questions; provisional |
| **CQ-007 Time/state/order invariants** | Does the claimed guarantee hold across time, state transitions and ordering? | TB-Q007: partial_overlap | SRC-000033 "Object Manager Lookup Performance"; SRC-000039 state-machine filtering; SRC-000085 "Chapter 3" | Stateful experiment planning; provisional |
| **CQ-008 Effective coverage** | Do the test inputs exercise security-relevant behavior rather than only generating superficial coverage? | TB-Q008: partial_overlap | SRC-000095 "Misleading metrics"; SRC-000094 "Mutation Testing"; SRC-000097 "Writing a Fuzz Target" | Coverage / feedback gap diagnostics; provisional |
| **CQ-009 Instrument validity** | Could the observed signal originate in the measurement or test procedure rather than the target? | No direct TB equivalent; QPT-000002: **SRC-000076 → QMP-000003 specialization** | SRC-000076 "AddressSanitizer: A Tool for Detection, Not Proof"; SRC-000026 "Connection reuse false-positives"; SRC-000094 "There ain't no such thing..." | Deterministic controls + model interpretation; provisional |
| **CQ-010 Evaluation lens (cross-cutting)** | Across candidate questions, which permitted experiment gives the most discriminating evidence per unit of cost? | TB-Q008: partial_overlap | SRC-000073 "Fast failure"; SRC-000107 "Step 2–5"; SRC-000024 "Ideation / Evaluation" | Model prioritization; provisional |
| **CQ-011 Variant and context transfer** | Does an assumption from another deployment, version or tenant actually transfer here? | TB-Q005: analogy_only; TB-Q006: analogy_only | SRC-000086 "Research mindset"; SRC-000048 "Analysis of the authentication bypass"; SRC-000104 "Emergence of Bypass" | Context/version-bound hypothesis; provisional |
| **CQ-012 Action/state discovery gap** | Which meaningful actions, workflows, identities or states remain missing from our application model? | TB-Q003: partial_overlap; TB-Q008: partial_overlap | SRC-000109 "Fuzzing to Find Hidden Features"; SRC-000008 "Discovery Process"; SRC-000055 "Stepping Back" | Semantic discovery gap / rediscovery candidate; provisional |
| **CQ-013 Actor/run/time provenance** | Whose run and knowledge state do these observations belong to, and when were they available? | No direct TB equivalent | SRC-000011 parallel TiTiler runs; SRC-000092 forensic researcher versus attacker; SRC-000104 objective change; SRC-000001/002 overlapping Chrome lineage | Scientific data-quality gate; provisional |
| **CQ-015 Publisher-claim validity** | Which vendor or publisher self-reported claims depend on unobserved denominators, selection criteria, or unverifiable aggregate measurements? | No direct TB equivalent; independent review needed | SRC-000030/031 vendor-position claims; SRC-000105 "200+"; SRC-000106 "92%" (all unverified publisher-level metrics) | Publisher assertions must remain bounded and attributed; provisional |
| **CQ-014 Observation-to-proof boundary** | Which exact claim does evidence support and when may existing proof authority promote it? | TB-Q004: partial_overlap | SRC-000076 false-positive correction; SRC-000026 reuse oracle; SRC-000095 BigSig coverage and proof limitations | Existing Evidence/Verifier/ProofLifecycle only; provisional |

**Evidence-lineage disclosure:** 46 source references represent 31 distinct source IDs, not 46 research trajectories or independent publisher lineages. `CQ-007` is weighted toward Project Zero, `CQ-006` has only two publisher lineages (SRC-000044/045 are related), and `CQ-013` cites three XBOW publications (SRC-000001/002/011). Vendor aggregate claims in CQ-015 have no externally validated denominator in the sources examined. The source evidence basis in JSON is an *unreviewed analyst classification*, not a historical observation timestamp.

**Recovered-source provenance:** SRC-000044 and SRC-000045's specific headings are supported by the later [targeted deep audit](../gpt/cases/RDL_TARGETED_DEEP_X_TO_Y_AUDIT.md) and the [recovered first-party mirror notes](../gpt/cases/RDL_RECOVERED_PRIMARY_SOURCES_ADDENDUM.md), not simply the stale earlier bounded audit. SRC-000048's section is likewise located in the later deep audit pass. Preserve original publisher attribution and recorded mirror provenance; do not count a publisher migration as independent corroboration.

**Crosswalk caveat:** No row asserts that a historical researcher literally asked the abstract question in this wording. Unless a source explicitly quotes it, the question is an analyst formulation.

## 3. Scientific boundaries and adversarial contrasts

These distinctions must survive any attempted merge:

| Tempting merger | Why it is potentially invalid | Required counterexample |
|---|---|---|
| CQ-001 negative vs CQ-002 blocked | A complete, properly executed negative can refute a *bounded* hypothesis. Policy denial provides no such evidence. | Same hypothesis with one valid negative and one authorization block |
| CQ-002 blockage vs CQ-003 prerequisite | Some paths are abandoned due to cost, lack of rights, or changing goals; no recoverable technical prerequisite follows. | Irrecoverable authorized limit, or a cheap alternative making continuation irrational |
| CQ-003 reachability vs CQ-004 capability | Gaining access to a required feature does not prove the intended security effect. | Accessible feature with enforced authorization and no vulnerability |
| CQ-004 trigger vs CQ-014 proof | A discriminator signal can support a narrow effect but still fail independent provenance/correlation requirements. | Positive model narrative with wrong-experiment evidence |
| CQ-005 invariant vs CQ-006 parser disagreement | Not every violated invariant involves two components; not every interpretation difference is security relevant. | Atomic single-component logic fault vs harmless formatting difference |
| CQ-007 race vs CQ-008 coverage | Failing to reach the vulnerable timing window may be a coverage problem, not a disproven race; some operations are truly atomic. | Atomic control and unreachable-harness control |
| CQ-008 effective coverage vs CQ-012 action discovery | Hitting an endpoint/line does not mean the workflow is reachable under all identities or states. | All known endpoints hit, authenticated feature still unknown |
| CQ-009 measurement artifact vs genuine negative | An ASan warning from test code and a negative result with valid oracle have different meaning. | Faulty instrumentation vs correctly executed refutation |
| CQ-010 **cross-cutting evaluation lens** vs correctness | The cheapest test may have no discriminatory power; the most promising research path may still be unauthorized. | Low-cost but uninformative probe, higher-cost but admissible discriminator |
| CQ-011 variant analysis vs proof by analogy | Similar products/versions cannot transfer a verified vulnerability without fresh evidence. | Patched/version-divergent control |
| CQ-015 vendor-level aggregate claim vs target-instrument artifact | Publisher-reported performance is not the same error class as an individual test-oracle defect. | A vendor claim with disclosed sampling and independently replicated denominator, contrasted with one non-replicable aggregate claim |
| CQ-013 forensic vs original research | A later forensic analyst's decisions are not the original exploit author's decisions. | SRC-000092-style actor separation |
| CQ-003 QPT-000001 | The source-specific existing QMP maps SRC-000055 / QMP-000002 as `analogy_only`; SRC-000074 / QMP-000001 independently maps `partial_overlap`. They must not be combined into one label. | WHOIS origin control versus missing scan identifier |
| CQ-009 QPT-000002 | Existing QMP-000003 maps SRC-000076 as `specialization`; instrument validity is already a **proposed** pattern in the canonical registry; this candidate is a consolidation view, not a duplicate authority. | Cheap fast-fail test without any defective oracle |

## 4. Outcome-independent scientific questions for the model

The research-question model should be trained/evaluated to ask **conditional questions**, not memorize a fixed checklist:
1. What is the narrow observation, its scope, and source?
2. Which mutually plausible explanations remain?
3. What baseline, control, or discriminator would distinguish them?
4. Was execution technically complete, the hypothesis supported/refuted, and the claim independently verified? These are distinct.
5. Which missing capability, identity, prerequisite, or state affects reachability?
6. Could this be a measurement or tool artifact?
7. What does the current map fail to cover: an action, role, workflow, data flow, or protocol state?
8. What additional experiment offers information gain within permitted budgets and authority?
9. When is an explicit negative, blocked, or exhaustion conclusion more scientifically justified than further probing?
10. What information is unavailable, retrospective, or private — requiring abstention rather than invention?

A model does not have to ask all ten questions each time. Relevance, cost and evidential fit should determine which questions matter.

## 5. What belongs where (advisory mapping only)

**Model reasoning / RDL retrieval:** competing explanations, research-question generation, conceptual invariants, hypothesis prioritization, and research strategy. These remain suggestions and should be evaluated before fine-tuning.

**Deterministic or existing-state contracts in HOMELAB:** identity/scope checking, action provenance, evidence correlation, verifier/proof promotion, task execution, typed blockers, replay/idempotency, and cost limits. Model narrative must not authorize execution or mint VERIFIED.

**Possible existing-Harness extensions after code audit:** semantic action/state coverage, controlled experiment comparison, graph of missing prerequisites, and prospective predecision context capture. Before proposing *any* new storage/hook, check the existing named components `ResearchStateStore`, `CoverageLedger`, `SurfaceGraph`, `EvidenceBackedExhaustion`, `ApplicationIntelligenceEngine`, `discovery_fabric`, `state_epoch_recon`, `ProofLifecycle`, and the actual convergence reducer — all are **external named candidates, not verified from this RDL repository**. Reconcile with the separately reported local FUP-B1/FUP-B3 work and frozen F1–F12 contracts before attempting integration. See [external dependency provenance](RDL_EXTERNAL_HOMELAB_DEPENDENCIES.md); all such gates are `UNVERIFIABLE_FROM_THIS_REPO` until the exact Harness branch and SHA are independently inspected.

**No code changes are authorized by this document.** The candidate classification is not an Architecture Change Proposal and not an implementation sign-off.

## 6. Curation queue: what an independent reviewer must challenge

| Priority | Case / question | Review task |
|---|---|---|
| P0 | CQ-001/002, SRC-000008 vs 022 | Distinguish valid field-level negative from method/auth blocker; review exact author passages |
| P0 | CQ-003/QPT-000001, SRC-000055 vs 074 | Confirm the existing `analogy_only` and `partial_overlap` judgments; do not silently upgrade to same-core |
| P0 | CQ-009/QPT-000002, SRC-000076 and 026 | Is the same core uncertainty really instrument-caused false signal, or only superficially similar? |
| P0 | CQ-013, SRC-000011 | Split the parallel TiTiler runs; do not invent causal pivot across runs |
| P0 | CQ-013, SRC-000092 | Separate forensic investigator's search from original attack originator's unknown process |
| P0 | CQ-015, SRC-000105/106/030/031 | Validate denominators, vendor claim qualifiers, selection effects and whether an aggregate-report family is warranted |
| P0 | CQ-014, SRC-000076 | Check author arithmetic, actual ASan statement and tester-generated read; do not infer global safety |
| P1 | CQ-008, SRC-000094/095 | Challenge harness-coverage causal explanations and reported measurement denominators |
| P1 | CQ-011, SRC-000086/104 | Bind variant analogy to exact versions, tenant context, and changed research objective |
| P1 | CQ-012, SRC-000109 | Distinguish unknown feature discovery from claim of complete attack-surface enumeration |
| P1 | CQ-006, SRC-000044/059 | Determine whether route normalization and UI trust labels genuinely instantiate one core scientific question or only analogy |

Reviewer output for each candidate: original source URL + stable locator or permissible captured digest; author/actor/run and publication context; exact claim; historical-vs-analyst basis; competing explanation; negative control; relationship (`candidate_same_core`/specialization/partial/analogy/unresolved); reviewer verdict; proposed revision; rights status; publisher lineage; original article versus recovered mirror; controlled relationship vocabulary.

**Do not allow GPT, the author of this consolidation, to self-certify its own classifications.** Independent reviewer approval is required before importing approved mappings into canonical QPT/QMP. Grok/GPT agreement does not substitute for first-party verification.

## 7. Next gate

1. Freeze source analysis revisions used for comparison and record their SHAs. Keep original independent `gpt/` and `grok/` analyses unchanged.
2. Perform curator adjudication on the P0 queue; log omissions and contradictions separately from unsupported claims.
3. Commission independently authored, category-blinded fresh tasks and negative controls **not 1:1 derived from the questions**, including held-out families outside this ontology; the ontology author cannot write the hidden evaluation fixtures. See [evaluation protocol](RDL_PRINCIPLE_EVALUATION_PROTOCOL.md).
4. Run baseline versus relevant/unrelated RDL retrieval under matched budgets **before** any fine-tuning.
5. After synthetic examples and prospective decision records independently pass rights, leakage, curation and evaluation gates, consider training. Currently: **0 TRAINING_APPROVED; no verified historical predecision snapshots**.

**Final classification: CANDIDATE ONTOLOGY v0 REVIEW 2 — PROVISIONAL / DO NOT PROMOTE.** Source mappings remain subject to independent scientific adjudication, and none of the claimed HOMELAB production hooks are verified within RDL.
