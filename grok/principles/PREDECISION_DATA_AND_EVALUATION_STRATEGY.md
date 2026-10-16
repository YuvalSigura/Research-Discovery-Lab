# Prospective Pre-Decision Data Capture and Evaluation Strategy

**Status:** PROVISIONAL. Design proposal only. Not an implemented contract. Not TRAINING_APPROVED.  
**Purpose:** Define how HOMELAB can capture genuine research decision data during future authorized investigations, and how that data plus controlled environments can support evaluation before any fine-tuning.  
**Architecture grounding:** Inspected existing HOMELAB components (dynamic_workgraph.py, action_plane.py, EvidenceLedger-related paths, capability composition, proof contracts). Proposals integrate with these; no new authority is created.  
**Revision note:** Revised 2026-10-16 to separate Knowledge Snapshot / Decision Record / Outcome Record and to require capture of model inputs.  
**Date:** 2026-10-16

## 1. Three linked immutable records

Each **selected, auditable research decision** is associated with up to three logical separately sealed records linked by a stable decision_id. The records need not be three new storage tables or three WorkGraph nodes: use existing state/evidence owners. A no-execution decision still requires a terminal decision/outcome disposition. Records are never rewritten after sealing; later corrections are additional linked revisions.

### 1.1 Knowledge Snapshot (sealed before decision)

Captures the knowledge state available for the decision:

- Known facts with evidence locators
- Explicit assumptions (with source or confidence)
- Uncertainties and open questions
- Negative and inconclusive results recorded so far, with explicit scope
- Blocked paths and the reason for blockage (missing precondition, cost/complexity judgment, authorization limit, configuration)
- Relevant environment / component state
- Identity and privilege context
- Prerequisites satisfied or still missing
- Current research objective
- Permitted action space at that moment
- **Model inputs actually received:** retrieval results, memory summaries, tool responses, and any other context supplied to the model for this decision. These must be recorded so that later analysis can distinguish what the model saw from what the system knew.

### 1.2 Decision Record (sealed after choice, before execution)

- Candidates considered (questions or experiments)
- Brief justification for each candidate as stated at decision time
- Selected choice
- Stated justification for the selection
- Success / failure / inconclusive criteria defined for the chosen experiment (what observation would support, refute, or leave the hypothesis inconclusive)
- Source of the decision (model proposal, human override, deterministic rule)

### 1.3 Outcome Record (sealed after execution)

- Actual authorized action executed (ActionPlane reference) or explicit decision not to execute
- Raw observations and qualifying evidence (EvidenceLedger references)
- Scoped interpretation: what the outcome supported, refuted, or left inconclusive
- Knowledge update performed (changes to environment model, hypothesis state, blocked-path status)
- Sequence number / WorkGraph node ID
- Timestamp bounds
- Tool and model versions

**Critical rules:**
- Knowledge Snapshot is sealed before any decision is finalized and before any action is executed.
- Decision Record is sealed before ActionPlane execution.
- Outcome Record is written only after the action completes and is linked by decision_id; it never rewrites earlier records.
- Future information must never appear in earlier records.
- Model-input capture is mandatory for any decision that will later be considered for training or evaluation.

## 2. Integration with existing components

- **WorkGraph:** Correlate each decision to an **existing task/node when one exists**; not every internal reasoning choice requires a new node. If existing WorkGraph contracts cannot represent the correlation, keep it as a reference in an authorized existing research/evidence record and propose any structural contract change separately. Snapshot is sealed before the decision sees outcome information; Decision Record is sealed before the selected execution is dispatched.
- **ActionPlane:** Executes only after Knowledge Snapshot and Decision Record are sealed.
- **EvidenceLedger:** Stores observations referenced by the Outcome Record.
- **Hypothesis / environment model state:** Existing owners consume verified or appropriately scoped observations according to their current state-transition contracts. Outcome persistence and domain-state update must use a documented crash-recoverable ordering; do not assert that one component owns every closure decision.
- **No new persistent state owner:** Records live inside existing WorkGraph or EvidenceLedger storage contracts.
- **No new authority:** Capture is observational. It does not grant execution, truth, or scheduling rights.

**Classification:** Extension of existing contracts. If current schemas cannot hold the required fields and immutability guarantees without structural change, an Architecture Change Proposal is required. No F1–F12 foundation change is proposed here.

## 2A. Sealing, concurrency, replay, and crash-recovery contract — required for any implementation

**Authority and identity.** A decision records `decision_id`, `investigation_id`, `subject_id`, `policy/scope revision`, optional `campaign_id`, `existing_workgraph_task_id`, `actor/model incarnation`, and `existing owner`. Use a stable decision ID across retries; a retry *attempt* gets its own attempt ID. Correlation IDs must be distinct from semantic content hashes. Do not invent a global namespace or separate persistent owner.

**Version and integrity.** Serialize a typed, versioned record deterministically; retain `schema_version`, `record_type`, `decision_id`, `record_version`, `previous_record_digest` (for linked amendments), `content_digest`, `sealed_at`, `owner_writer_id`, and the currently valid authority/policy revision. Use the repository's existing digest/event conventions if present. A SHA-256 checksum makes accidental mutation detectable; it is **not a signature of provenance or tamper-proof security** without independently controlled signing keys or trusted append-only storage. Do not introduce a new secret/key-resolution route. If the current storage cannot enforce immutability, classify the gap and require architecture approval before claiming a hard seal.

**Actual model-visible context.** Freeze a content-addressed or version-pinned manifest of the complete **effective** inputs visible to the decision model, including system/developer instructions where permitted, model/tool parameters, retrieved passage IDs and versions, summarized memory revision, tool-result IDs/bodies, and truncation/compaction boundaries. This is an access-controlled research artifact: do **not** put raw secrets, tokens, private user content, or unrestricted raw tool dumps into a public dataset. Preserve protected references or authorized redacted reproductions and explicitly record when full reconstruction is unavailable. Store `context_complete=false` if any unavailable private or internal input prevents exact reproduction; such records cannot support claims of fully known predecision context.

**Ordering.** Required logical order:
1. Existing state owner obtains a consistent point-in-time view and freezes Knowledge Snapshot K.
2. A decision consumes K and other **already-frozen** eligible inputs; seal Decision Record D with references to K and the exact model-visible input manifest.
3. Recheck scope/authorization freshness at ActionPlane. Sealing D is not execution permission and is not a substitute for ActionPlane approval.
4. Execute via existing WorkGraph/ActionPlane; append evidence to the normal evidence authority.
5. Seal Outcome Record O referencing the exact K/D and execution attempt, with explicit `execution_status`, `experimental_outcome`, and separate `proof_status`; only the existing verifier/proof owner may promote truth.
6. Existing domain owners consume O via their current event/state transition paths. Late evidence and corrected interpretations append linked updates; K and D stay unchanged.

**Concurrency and exactly-once limitations.** Enforce conditional append/compare-and-swap against existing owner version or event position; unique constraints for `(decision_id, record_type, record_version)`; reject conflicting second writes, not merely last-writer-wins. Record monotonic per-owner sequence and causality links rather than presuming clock order across workers. Deduplicate receipt **processing** with stable source event IDs; do not assert exactly-once target execution after an ambiguous transport timeout. Use existing idempotency keys, attempt records, outcome reconciliation, and policy-safe retry rules. Parallel decisions must reference their own K versions; do not silently merge distinct identity, policy or environment states.

**Crash/restart matrix:**
- Crash before K seal: no committed decision; reconstruct only from a new consistent snapshot.
- Crash after K but before D: K may remain orphaned; do not execute; either resume bounded planning with same K if still valid or create a new K.
- Crash after D but before dispatch: reconcile the existing task/action journal first; recheck policy; dispatch only if no attempt was recorded and the action contract permits it.
- Crash after dispatch but before receipt: mark execution uncertain; reconcile evidence and attempt status; never blindly resubmit a non-idempotent action.
- Crash after evidence but before O: reconstruct O **only from existing qualifying durable evidence** with causal attribution; do not hallucinate result.
- Crash after O but before downstream state projection: replay the existing state transition idempotently, preserving domain owners and proof boundaries.

**Failure/partial states.** A denial, cancellation, no-execute decision, expired policy, redacted/missing context, inconsistent snapshot, late evidence, conflict, or timeout must have an explicit reason and bounded reconciliation path. A delayed proof review may add a verified-proof linkage later without rewriting O's original observations. Define retention, access control, data minimization, corpus opt-in, and rights checks before exporting any snapshot for training.

**Verification gate.** Test sealed immutability, digest mismatch, stale K, wrong-policy D, duplicate concurrent writer, replayed receipt, crash at each boundary, late evidence correction, policy revocation, conflicting attempts, non-idempotent timeout, cross-identity/tenant linking, secret redaction, and context-compaction incompleteness. A passing unit mock alone is not proof of production replay behavior.

**Ownership review:** The current repository might place task, hypothesis, campaign and proof transitions with different owners. This specification **does not consolidate them into a reducer**. Confirm actual owner paths and whether F1–F12 already supply the proposed record semantics. Only genuine missing foundational authority/persistence contracts merit an Architecture Change Proposal; ordinary fields on an existing authorized record are not automatically ACP-worthy.

---

## 3. Evaluation before fine-tuning

### Benchmark design

Use fresh, held-out controlled research environments (not the historical RDL sources). Environments should contain known ground-truth research questions, recoverable and non-recoverable missing preconditions, scoped negatives, and competing hypotheses.

### Conditions to compare (controlled tools, budgets, models)

**E0: no training, test retrieval value first (three required matched arms).**
1. Baseline model without RDL principles (`baseline`)
2. Identical model with *relevant, provisional* RDL retrieval (`rdl_relevant`)
3. Identical model with **content-/length-matched unrelated guidance** as a placebo (`rdl_unrelated`)

**E1: future training comparison — not authorized.**
4. Model fine-tuned only on independently validated and rights-cleared synthetic principle examples (`sft_principles`)
5. Such a fine-tuned model with matched retrieval (`sft_plus_retrieval`)

This distinction is controlled by [the RDL scientific evaluation protocol](../../docs/RDL_PRINCIPLE_EVALUATION_PROTOCOL.md), not by the order of examples in this document. The current `rdl.paired_trial.v1` scorer supports only the three E0 arms and is descriptive. The evaluation requires **independently authored hidden fixtures that are not a re-labeling of this ontology**, at least two held-out out-of-ontology categories, a preregistered power/sample-size plan, independent double-rating and an ordinal IRR result, and leakage/rights/lineage audits **before making any performance claims**. The scorer's `n >= 3` check is not a power calculation. E1 needs its own schema/scorer and new authorization.

### Metrics (not final exploit success)

- Quality and specificity of generated research questions
- Discriminating power of proposed experiments
- Correct identification and handling of missing prerequisites
- Correct scoped interpretation of negative evidence
- Information gained per authorized experiment
- Avoidance of fabricated or over-claimed proof
- Discovery of previously unmodeled functionality
- Ability to revise hypotheses when evidence warrants
- Generalization to technologies and applications not present in the principle set

### Gates before any TRAINING_APPROVED status

- Three-record logical structure wired to existing owners, passing sealing/replay/concurrency/fault-injection and leakage audits (including exact model-visible context or explicit incompleteness)
- Synthetic training examples independently validated
- Rights and curation complete
- Evaluation shows measurable improvement on the metrics above without regression on fabricated-proof or over-generalization measures
- Human adjudication of a sample of model outputs

## 4. Distinction from historical imitation

This strategy does not attempt to reconstruct or imitate historical researcher trajectories from retrospective narratives. It creates new, prospectively captured decision data under controlled conditions. Historical RDL sources remain useful for principle extraction only.

### Scientific evaluation controls

Preregister held-out tasks, environments, mechanisms, investigators/publishers and source lineage separation; freeze evaluation rubric and model/tool/token/time budgets before any comparison. Include negative and irrecoverable-prerequisite examples as well as positives; grade epistemic calibration and **unnecessary follow-up** alongside question quality. Match baseline/retrieval/fine-tuning conditions and disclose where frozen model revisions are unavailable. No article's eventual success is a unique gold next action; judge admissibility and discriminating power against fixture ground truth. Record contamination and rights review separately.

**External-repository qualification:** References to FUP-B1/B3, F1–F12, WorkGraph, ResearchStateStore and other HOMELAB owners are `UNVERIFIABLE_FROM_THIS_REPO` until the external branch, SHA, production callers and tests have been audited. Offline controlled E0 evaluation has independent scientific gates; live HOMELAB instrumentation additionally requires its architectural conformance gates. See [external dependency record](../../docs/RDL_EXTERNAL_HOMELAB_DEPENDENCIES.md).

**Review amendment provenance:** This E0/E1 clarification was added by GPT after Claude's independent PR #5 review on 2026-10-16. It does not retroactively claim that Grok had independently established these requirements.

**Document-finalization status:** This file is now a **detailed provisional design contract for engineering review**, not an implemented or approved architectural contract. Validate the exact HOMELAB branch and ongoing FUP-B1/FUP-B3 changes before implementation. No statement here grants a new scheduler, proof owner, target execution authority, or state writer.

**No artifact produced under this strategy is TRAINING_APPROVED until all gates above are satisfied.**
