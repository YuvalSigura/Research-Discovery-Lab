# TRACK B — Candidate Research-Question Principles

**Status:** PROVISIONAL. Not TRAINING_APPROVED. Not a training dataset.  
**Purpose:** Distill source-grounded scientific reasoning patterns into candidate question patterns for a future research-question model.  
**Independence note:** Principles below are derived from Grok's independent source readings under `grok/sources/`. GPT analyses under `gpt/` were consulted only after independent work for cross-check; agreement is not treated as independent corroboration.  
**Date:** 2026-10-16

## Epistemic framing

All principles below are candidate patterns observed across multiple retrospective sources. They do not constitute verified historical decision trajectories. Each principle includes:

- Stable ID
- Source anchors (SRC IDs + brief locator)
- Epistemic status
- What the model should learn to do
- Boundaries / failure conditions
- Counterexamples or disconfirming cases
- Required validation before any training use

---

## TB-Q001 — Negative result is scoped, not global

**Epistemic status:** author_reported across multiple sources; analyst reconstruction of the general pattern.  
**Sources:** SRC-000008 (Chef Automate: values/name fields negative, type field positive); SRC-000004 (Bing Images: XXE probes negative, renderer positive); SRC-000009 (Druid: historical endpoints negative due to configuration).  
**What the model should learn:** When an experiment returns a negative or null result, formulate the next question as "which exact scope and assumptions were tested?" rather than "is the class closed?". Propose a bounded negative interpretation and identify what remains untested.  
**Boundaries:** Does not apply when the source explicitly states a global closure with supporting evidence. Does not license inventing untested surfaces.  
**Failure condition:** Treating a scoped negative as license to continue indefinitely on the same surface without new discriminating evidence.  
**Counterexample:** A source that documents a systematic, exhaustive check of all relevant variants with consistent negatives and no remaining untested assumptions.  
**Validation required:** Human adjudication of the scoped vs global distinction on held-out sources; measurement of whether models over-generalize negatives.

---

## TB-Q002 — Blocked is not falsified

**Epistemic status:** author_reported in several sources; strong pattern.  
**Sources:** SRC-000003 (SMC-D: MITM abandoned due to complexity, later revived); SRC-000025 (HTTP/1.1: 0.CL deadlocks treated as prerequisite problem); SRC-000055 (CyberPanel: XSS blocked by missing scan_id).  
**What the model should learn:** When a direction is blocked by a missing precondition, cost judgment, or configuration state, generate the question "what would make this direction testable?" rather than closing it. Distinguish resource/complexity abandonment from experimental falsification.  
**Boundaries:** Does not require pursuing every blocked path. Must be weighed against available resources and expected information gain.  
**Failure condition:** Treating every timeout, 403, or missing token as a permanent closure.  
**Counterexample:** A source where the researcher explicitly documents that further investigation of the blocked path is not worthwhile given current constraints and alternative higher-value directions.  
**Validation required:** Evaluation on controlled environments where some blocked paths are recoverable and some are not.

---

## TB-Q003 — Missing prerequisite is a research question

**Epistemic status:** action_implied + author_reported.  
**Sources:** SRC-000055 (CyberPanel: two blocked primitives resolved by forgotten debug endpoint); SRC-000025 (early-response gadgets for 0.CL); SRC-000023 (Ninja Tables: nonce recoverable from client-side).  
**What the model should learn:** When two or more promising primitives are each blocked by a different missing precondition, formulate a question that searches for the missing link (debug surfaces, client-side artifacts, early-response behaviors, alternative routing).  
**Boundaries:** The missing link must be observable or reachable within the permitted action space. Do not invent prerequisites.  
**Failure condition:** Assuming every blocked pair has a recoverable link.  
**Counterexample:** Cases where the missing precondition is intentionally protected and no recoverable artifact exists in the authorized scope.  
**Validation required:** Synthetic controlled environments with recoverable vs non-recoverable missing preconditions.

---

## TB-Q004 — Separate trigger discovery from weaponization

**Epistemic status:** author_reported (methodology paper).  
**Sources:** SRC-000024 (HTTP Terminator: micro-inspiration produced novel triggers; autonomous weaponization required human intervention and workarounds).  
**What the model should learn:** Distinguish the research question "does this trigger produce a desync/parser discrepancy?" from "can this be weaponized reliably against live targets?". Propose different experiment designs and evidence standards for each.  
**Boundaries:** Applies primarily to protocol and parser research; less relevant to pure application logic bugs.  
**Failure condition:** Declaring a research direction closed because weaponization failed when the trigger itself was validated.  
**Counterexample:** Domains where trigger and weaponization are inseparable by design.  
**Validation required:** Evaluation tasks that require the model to propose trigger-only experiments before weaponization attempts.

---

## TB-Q005 — Micro-inspiration from primary specification can increase novelty

**Epistemic status:** author_reported experimental result.  
**Sources:** SRC-000024 (RFC micro-fragments outperformed broad prompts for rediscovery of unpublished techniques).  
**What the model should learn:** When generating hypotheses about protocol or specification-governed behavior, prefer constrained inspiration from primary specification fragments over open-ended prompting. Recognize when over-anchoring reduces novelty.  
**Boundaries:** Specific to domains with rich formal specifications. Not a general claim about all research.  
**Failure condition:** Over-fitting to the inspiration method itself.  
**Counterexample:** Research domains without accessible primary specifications.  
**Validation required:** Controlled comparison of inspiration methods on held-out protocol research tasks.

---

## TB-Q006 — When classic detection is mitigated, probe discrepancies and early-response gadgets

**Epistemic status:** author_reported multi-year research sequence.  
**Sources:** SRC-000025 (HTTP/1.1 must die: classic CL.TE methods fingerprinted; shift to parser discrepancy detection, 0.CL with early-response gadgets, Expect header).  
**What the model should learn:** After observing that a previously effective detection method is blocked or fingerprinted, generate questions about alternative discrepancy surfaces or early-response behaviors rather than abandoning the vulnerability class.  
**Boundaries:** Requires evidence that the class remains plausible. Does not license infinite exploration of a closed class.  
**Failure condition:** Continuing to probe a class after multiple independent sources of evidence indicate it is no longer viable.  
**Counterexample:** A class for which the source documents comprehensive mitigation and no remaining discrepancy surface.  
**Validation required:** Evaluation on environments where classic detection is blocked but alternative gadgets exist, and environments where the class is truly closed.

---

## TB-Q007 — Race window expansion via resource-lookup slowdown composition

**Epistemic status:** author_reported empirical + kernel analysis.  
**Sources:** SRC-000033 (Windows OMNS: long paths insufficient; composition of recursive directories, symbolic links, hash collisions, and shadow directories).  
**What the model should learn:** When a race condition is theoretically present but the window is too small, formulate questions about measurable slowdowns in the resource resolution path and possible compositional techniques, rather than abandoning the race.  
**Boundaries:** Domain-specific to systems with complex named-resource lookup. Requires empirical measurement capability.  
**Failure condition:** Assuming every race can be expanded this way.  
**Counterexample:** Races where the check and use are atomic or where lookup time cannot be influenced within the permitted action space.  
**Validation required:** Controlled race environments with and without expandable lookup paths.

---

## TB-Q008 — Key questions for state-machine race filtering

**Epistemic status:** author_reported methodology.  
**Sources:** SRC-000039 (Smashing the state machine: how is state stored? editing vs appending? operation keyed on what?).  
**What the model should learn:** Before expensive synchronization experiments, generate filtering questions about state storage, edit vs append semantics, and operation keys to prioritize candidate endpoints.  
**Boundaries:** Specific to multi-step state machine races. Not a general prioritization method.  
**Failure condition:** Applying the filter so strictly that valid but unusual state machines are excluded.  
**Counterexample:** Races that do not fit the storage/edit/key model.  
**Validation required:** Evaluation on race-prone applications where the filter correctly ranks high-value endpoints.

---

## Training distinction

- **Principle-level supervised training** (possible later, after validation): Use independently validated synthetic cases that instantiate these principles. The model learns to recognize the situation type and generate the appropriate question or interpretation.  
- **Historical trajectory imitation** (currently blocked): Requires defensible pre-decision snapshots that do not exist in the current retrospective corpus. Do not train on full published narratives.

**No principle in this document is TRAINING_APPROVED.** All require the validation gates listed above plus rights, curation, and leakage controls.
