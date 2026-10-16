# Prospective Pre-Decision Data Capture and Evaluation Strategy

**Status:** PROVISIONAL. Design proposal only. Not an implemented contract. Not TRAINING_APPROVED.  
**Purpose:** Define how HOMELAB can capture genuine research decision data during future authorized investigations, and how that data plus controlled environments can support evaluation before any fine-tuning.  
**Architecture grounding:** Inspected existing HOMELAB components (dynamic_workgraph.py, action_plane.py, EvidenceLedger-related paths, capability composition, proof contracts). Proposals integrate with these; no new authority is created.  
**Revision note:** Revised 2026-10-16 to separate Knowledge Snapshot / Decision Record / Outcome Record and to require capture of model inputs.  
**Date:** 2026-10-16

## 1. Three linked immutable records

Every significant research decision point produces three separately sealed records linked by a common decision_id. No record is rewritten after sealing.

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

- **WorkGraph:** Decision points are nodes. Knowledge Snapshot is attached and sealed before outgoing edges are evaluated. Decision Record is attached before ActionPlane is invoked.
- **ActionPlane:** Executes only after Knowledge Snapshot and Decision Record are sealed.
- **EvidenceLedger:** Stores observations referenced by the Outcome Record.
- **Hypothesis / environment model state:** Updated only after the Outcome Record is written.
- **No new persistent state owner:** Records live inside existing WorkGraph or EvidenceLedger storage contracts.
- **No new authority:** Capture is observational. It does not grant execution, truth, or scheduling rights.

**Classification:** Extension of existing contracts. If current schemas cannot hold the required fields and immutability guarantees without structural change, an Architecture Change Proposal is required. No F1–F12 foundation change is proposed here.

## 3. Evaluation before fine-tuning

### Benchmark design

Use fresh, held-out controlled research environments (not the historical RDL sources). Environments should contain known ground-truth research questions, recoverable and non-recoverable missing preconditions, scoped negatives, and competing hypotheses.

### Conditions to compare (controlled tools, budgets, models)

1. Baseline model without RDL principles
2. Baseline model with RDL retrieval (principles supplied as context)
3. Model trained on validated synthetic scientific-reasoning examples (principle-level only)
4. Fine-tuned model with retrieval (only after training gates are passed)

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

- Three-record structure implemented and passing leakage audit (no future information in earlier records; model inputs captured)
- Synthetic training examples independently validated
- Rights and curation complete
- Evaluation shows measurable improvement on the metrics above without regression on fabricated-proof or over-generalization measures
- Human adjudication of a sample of model outputs

## 4. Distinction from historical imitation

This strategy does not attempt to reconstruct or imitate historical researcher trajectories from retrospective narratives. It creates new, prospectively captured decision data under controlled conditions. Historical RDL sources remain useful for principle extraction only.

**No artifact produced under this strategy is TRAINING_APPROVED until all gates above are satisfied.**
