# TRACK B — Candidate Research-Question Principles

**Status:** PROVISIONAL. Not TRAINING_APPROVED. Not a training dataset.  
**Purpose:** Distill source-grounded scientific reasoning patterns into candidate question patterns for a future research-question model. Technique-specific examples are retained as illustrations under broader questions.  
**Independence note:** Principles below are derived from Grok's independent source readings under `grok/sources/`. GPT analyses under `gpt/` were consulted only after independent work for cross-check; agreement is not treated as independent corroboration.  
**Revision note:** Revised 2026-10-16 to elevate technique-specific observations into broader scientific questions while retaining original anchors.  
**Date:** 2026-10-16

## Epistemic framing

All principles below are candidate patterns observed across multiple retrospective sources. They do not constitute verified historical decision trajectories. Each principle includes:

- Stable ID
- Broader scientific question
- Source anchors (SRC IDs + brief locator)
- Epistemic status
- What the model should learn to do
- Boundaries / failure conditions
- Counterexamples or disconfirming cases
- Required validation before any training use

---

## TB-Q001 — Negative result is scoped, not global

**Broader question:** Which exact scope, identity, inputs, and assumptions were tested by this negative result, and what remains untested?  
**Epistemic status:** author_reported across multiple sources; analyst reconstruction of the general pattern.  
**Sources:** SRC-000008 (Chef Automate: values/name fields negative, type field positive); SRC-000004 (Bing Images: XXE probes negative, renderer positive); SRC-000009 (Druid: historical endpoints negative due to configuration).  
**What the model should learn:** When an experiment returns a negative or null result, formulate the next question around the tested scope rather than closing the class. Identify what remains untested.  
**Boundaries:** Does not apply when the source explicitly states a global closure with supporting evidence. Does not license inventing untested surfaces.  
**Failure condition:** Treating a scoped negative as license to continue indefinitely on the same surface without new discriminating evidence.  
**Counterexample:** A source that documents a systematic, exhaustive check of all relevant variants with consistent negatives and no remaining untested assumptions.  
**Validation required:** Human adjudication of the scoped vs global distinction on held-out sources; measurement of whether models over-generalize negatives.

---

## TB-Q002 — Blocked is not falsified

**Broader question:** Is this direction blocked by a missing precondition, a cost judgment, an authorization limit, or an experimental negative — and what would make it testable?  
**Epistemic status:** author_reported in several sources; strong pattern.  
**Sources:** SRC-000003 (SMC-D: MITM abandoned due to complexity, later revived); SRC-000025 (HTTP/1.1: 0.CL deadlocks treated as prerequisite problem); SRC-000055 (CyberPanel: XSS blocked by missing scan_id).  
**What the model should learn:** Distinguish the reason for blockage. Generate the question “what would make this direction testable?” when the blockage is a missing precondition or cost judgment. Do not treat authorization limits as scientific findings.  
**Boundaries:** Does not require pursuing every blocked path. Must be weighed against available resources and expected information gain.  
**Failure condition:** Treating every timeout, 403, or missing token as a permanent closure.  
**Counterexample:** A source where the researcher explicitly documents that further investigation of the blocked path is not worthwhile given current constraints and alternative higher-value directions.  
**Validation required:** Evaluation on controlled environments where some blocked paths are recoverable and some are not.

---

## TB-Q003 — Missing prerequisite is a research question

**Broader question:** Which missing precondition is blocking progress, and what observable or constructible artifact within the authorized scope might supply it?  
**Epistemic status:** action_implied + author_reported.  
**Sources:** SRC-000055 (CyberPanel: two blocked primitives resolved by forgotten debug endpoint); SRC-000025 (early-response gadgets for 0.CL); SRC-000023 (Ninja Tables: nonce recoverable from client-side).  
**What the model should learn:** When promising directions are blocked by missing preconditions, formulate a question that searches for the missing link inside the permitted action space.  
**Boundaries:** The missing link must be observable or reachable within the permitted action space. Do not invent prerequisites.  
**Failure condition:** Assuming every blocked pair has a recoverable link.  
**Counterexample:** Cases where the missing precondition is intentionally protected and no recoverable artifact exists in the authorized scope.  
**Validation required:** Synthetic controlled environments with recoverable vs non-recoverable missing preconditions.

---

## TB-Q004 — Separate trigger discovery from weaponization

**Broader question:** What does a successful trigger demonstrate, and what additional evidence is required to claim a reliable capability?  
**Epistemic status:** author_reported (methodology paper).  
**Sources:** SRC-000024 (HTTP Terminator: micro-inspiration produced novel triggers; autonomous weaponization required human intervention and workarounds).  
**What the model should learn:** Distinguish the research question “does this trigger produce the hypothesized discrepancy?” from “can this be turned into a reliable, demonstrated capability?” Propose different experiment designs and evidence standards for each.  
**Boundaries:** Applies across protocol, parser, and logic research; the specific form of weaponization varies by domain.  
**Failure condition:** Declaring a research direction closed because weaponization failed when the trigger itself was validated.  
**Counterexample:** Domains where trigger and weaponization are inseparable by design.  
**Validation required:** Evaluation tasks that require the model to propose trigger-only experiments before capability claims.

---

## TB-Q005 — Specification or implementation assumptions can generate hypotheses

**Broader question:** Which assumption in a specification, interface contract, or implementation could be violated or interpreted differently to produce a new hypothesis?  
**Epistemic status:** author_reported experimental result (technique) elevated to general question.  
**Sources:** SRC-000024 (RFC micro-fragments outperformed broad prompts for rediscovery of unpublished techniques). Technique example: constrained inspiration from primary specification fragments.  
**What the model should learn:** When working in a domain with accessible specifications or contracts, generate hypotheses by challenging specific assumptions or obligations stated in those documents, rather than relying only on open-ended exploration. Recognize when over-anchoring reduces novelty.  
**Boundaries:** Most useful in domains with formal or semi-formal specifications. Not a claim that this method is universally superior.  
**Failure condition:** Over-fitting to one inspiration method.  
**Counterexample:** Research domains without accessible primary specifications.  
**Validation required:** Controlled comparison of hypothesis-generation methods on held-out tasks.

---

## TB-Q006 — Different components may interpret the same input or state differently

**Broader question:** Do different components, parsers, or layers interpret the same input, state, or message differently, and does that discrepancy create a security-relevant gap?  
**Epistemic status:** author_reported multi-year research sequence.  
**Sources:** SRC-000025 (HTTP/1.1 must die: classic CL.TE methods fingerprinted; shift to parser discrepancy detection, 0.CL with early-response gadgets, Expect header).  
**What the model should learn:** After observing that a previously effective detection method is blocked or fingerprinted, generate questions about alternative interpretation discrepancies or early-response behaviors rather than abandoning the class, provided evidence remains that the class is still plausible.  
**Boundaries:** Requires evidence that the class remains plausible. Does not license infinite exploration of a closed class.  
**Failure condition:** Continuing to probe a class after multiple independent sources of evidence indicate it is no longer viable.  
**Counterexample:** A class for which the source documents comprehensive mitigation and no remaining discrepancy surface.  
**Validation required:** Evaluation on environments where classic detection is blocked but alternative discrepancies exist, and environments where the class is truly closed.

---

## TB-Q007 — Time, state, and ordering assumptions can be challenged

**Broader question:** Which assumption about time, state stability, or execution order is required for a security guarantee, and how can that assumption be stressed or violated within the permitted action space?  
**Epistemic status:** author_reported empirical + kernel analysis (technique) elevated to general question.  
**Sources:** SRC-000033 (Windows OMNS: long paths insufficient; composition of recursive directories, symbolic links, hash collisions, and shadow directories to expand a race window). Technique example: measuring and composing slowdowns in a resource lookup path.  
**What the model should learn:** When a race or time-of-check/time-of-use condition is theoretically present but the window is small, formulate questions about which timing or ordering assumptions can be influenced, and what measurements would distinguish competing explanations, rather than abandoning the class.  
**Boundaries:** Requires that the relevant timing or ordering assumptions are influenceable within the authorized action space.  
**Failure condition:** Assuming every race or ordering issue can be expanded.  
**Counterexample:** Cases where the check and use are atomic or where the relevant timing cannot be influenced.  
**Validation required:** Controlled environments with and without influenceable timing or ordering assumptions.

---

## TB-Q008 — Filter candidate surfaces with structural questions before expensive experiments

**Broader question:** Which structural properties of state, identity, or operation make a candidate surface more or less likely to exhibit the hypothesized behavior?  
**Epistemic status:** author_reported methodology.  
**Sources:** SRC-000039 (Smashing the state machine: how is state stored? editing vs appending? operation keyed on what?).  
**What the model should learn:** Before expensive synchronization or high-cost experiments, generate filtering questions about relevant structural properties (state storage, edit vs append, operation key, identity context, etc.) to prioritize candidates.  
**Boundaries:** The specific filtering questions depend on the hypothesis class. Over-strict filters can exclude valid but unusual cases.  
**Failure condition:** Applying a filter so strictly that valid surfaces are excluded, or skipping the filter and wasting resources on low-probability candidates.  
**Counterexample:** Hypothesis classes that do not admit useful structural pre-filters.  
**Validation required:** Evaluation on applications where structural filters correctly rank high-value candidates.

---

## Training distinction

- **Principle-level supervised training** (possible later, after validation): Use independently validated synthetic cases that instantiate these broader questions. The model learns to recognize the situation type and generate the appropriate question or interpretation. Technique-specific examples may appear as illustrations but are not the training target.  
- **Historical trajectory imitation** (currently blocked): Requires defensible pre-decision snapshots that do not exist in the current retrospective corpus. Do not train on full published narratives.

## Candidate finalization: learning unit, counterfactuals, and gates

The stable TB-Q identifiers denote **candidate research-question families**, not historically verified causal rules or automatically accepted training labels. A technique (for example, RFC-fragment prompting or Windows lookup slowdown) is an instance or test context under a broader question. This registry is open-world: a new question need not fit TB-Q001–Q008.

For each eventual example, preserve: (a) an evidence-bounded **observation**, (b) the exact uncertainty and competing explanations, (c) an admissible discriminating question or experiment, (d) a **plausible but scientifically unsound contrast**, and (e) a rubric that judges the reasoning rather than whether the response matches a historical researcher's next step. The reason for the contrast must be grounded in a controlled fixture or independently reviewed evidence. "What happened later" is never a pre-decision input or a unique answer key.

**No fine-tuning directly from these retrospective analyses.** Principle-level synthetic examples become eligible only after independent fixture/label review, leakage and memorization controls, held-out evaluation, rights review, and explicit dataset approval. Research principles can be used earlier as separately labeled **provisional retrieval guidance** or for benchmark *design*, but no scientific or security truth is promoted by retrieval.

**Avoid false universalization:** TB-Q001 does not imply every negative warrants another probe; TB-Q003 does not imply every prerequisite can be recovered; TB-Q006 does not imply discrepancies are necessarily vulnerabilities; TB-Q007 does not imply controllable races in every system. Include closed, irrecoverable, benign, and instrument-artifact counterexamples, and measure unnecessary follow-up rate.

**Cross-track binding:** TA-H001–TA-H008 are *candidate* operational interpretations, not authoritative implementations. Record mappings as versioned candidate mappings, not proven causal transfer. P0 experiment-outcome and campaign-stagnation fixes being developed separately in HOMELAB are not redefined here.

**No principle in this document is TRAINING_APPROVED.** All require the validation gates above plus rights, curation, and leakage controls.
