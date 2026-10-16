# Prospective Pre-Decision Data Capture and Evaluation Strategy

**Status:** PROVISIONAL. Design proposal only. Not an implemented contract. Not TRAINING_APPROVED.  
**Purpose:** Define how HOMELAB can capture genuine research decision snapshots during future authorized investigations, and how those snapshots plus controlled environments can support evaluation before any fine-tuning.  
**Architecture grounding:** Inspected existing HOMELAB components including dynamic_workgraph.py, action_plane.py, EvidenceLedger-related paths, capability composition, and proof contracts. All proposals integrate with these rather than creating parallel authority.  
**Date:** 2026-10-16

## 1. Pre-decision snapshot contract (prospective)

For every significant research decision point (question selection, experiment proposal, prioritization choice, or interpretation of a result), HOMELAB should capture an immutable snapshot containing exactly the following fields, with no future information inserted:

1. **Knowledge at decision time**  
   - Known facts (with evidence locators)  
   - Explicit assumptions (with confidence or source)  
   - Uncertainties and open questions  
   - Negative and inconclusive results recorded so far (with scope)  
   - Blocked paths and the reason for blockage (missing precondition, cost, authorization, configuration)

2. **Environment and identity state**  
   - Relevant application / component state  
   - Identity and privilege context of the decision  
   - Prerequisites already satisfied or still missing

3. **Objective and action space**  
   - Current research objective  
   - Permitted action space at that moment (from existing authorization contracts)

4. **Candidates considered**  
   - Research questions or experiments considered  
   - Brief justification for each (as stated by the model or human at the time)

5. **Chosen action**  
   - The selected question or experiment  
   - Stated justification at decision time

6. **Actual authorized action**  
   - The ActionPlane action that was executed (or the decision not to execute)

7. **Observations**  
   - Raw observations and qualifying evidence produced by the action  
   - EvidenceLedger references

8. **Interpretation**  
   - What the outcome supported, refuted, or left inconclusive (scoped)

9. **Knowledge update**  
   - Changes to the environment model, hypothesis state, or blocked-path flags

10. **Provenance**  
    - Sequence number / WorkGraph node ID  
    - Timestamp bounds  
    - Tool and model versions  
    - Source of the decision (model proposal, human override, deterministic rule)

**Critical rule:** The snapshot is written before the action outcome is known. Outcome fields are appended later under a separate immutable record linked by snapshot ID. No field in the pre-decision portion may be rewritten with later knowledge.

## 2. Integration with existing components

- **WorkGraph:** Decision points are nodes. Snapshot is attached to the node before outgoing edges are evaluated.  
- **ActionPlane:** Executes only after the pre-decision snapshot is sealed.  
- **EvidenceLedger:** Stores observations; links back to the snapshot ID.  
- **Hypothesis / environment model state:** Updated only after the outcome record is written.  
- **No new persistent state owner:** Snapshots live inside existing WorkGraph or EvidenceLedger storage contracts.  
- **No new authority:** Capture is observational. It does not grant execution, truth, or scheduling rights.

**Classification:** This is an extension of existing contracts. If the current WorkGraph or EvidenceLedger schemas cannot hold the required fields without structural change, an Architecture Change Proposal is required. No F1–F12 foundation change is proposed in this document.

## 3. Evaluation before fine-tuning

### Benchmark design

Use fresh, held-out controlled research environments (not the historical RDL sources). Environments should have known ground-truth research questions, missing preconditions, scoped negatives, and recoverable blocked paths.

### Conditions to compare (controlled tools, budgets, models)

1. Baseline model without RDL principles  
2. Baseline model with RDL retrieval (principles supplied as context)  
3. Model trained on validated synthetic scientific-reasoning examples (principle-level only)  
4. Fine-tuned model with retrieval (when and if training occurs)

### Metrics (not final exploit success)

- Quality and specificity of generated research questions  
- Discriminating power of proposed experiments  
- Correct identification of missing prerequisites  
- Correct scoped interpretation of negative evidence  
- Information gained per authorized experiment  
- Avoidance of fabricated or over-claimed proof  
- Discovery of previously unmodeled functionality  
- Ability to revise hypotheses when evidence warrants  
- Generalization to technologies not seen in the principle set

### Gates before any TRAINING_APPROVED status

- Immutable pre-decision snapshots exist and pass leakage audit (no future information in earlier records)  
- Synthetic training examples independently validated  
- Rights and curation complete  
- Evaluation shows measurable improvement on the metrics above without regression on fabricated-proof or over-generalization measures  
- Human adjudication of a sample of model outputs

## 4. Distinction from historical imitation

This strategy does not attempt to reconstruct or imitate historical researcher trajectories from retrospective narratives. It creates new, prospectively captured decision data under controlled conditions. Historical RDL sources remain useful for principle extraction only.

**No artifact produced under this strategy is TRAINING_APPROVED until all gates above are satisfied.**
