# TRACK A — Candidate Heuristics for HOMELAB Intelligence

**Status:** PROVISIONAL. Not an architecture change. Not a new authority.  
**Purpose:** Translate source-grounded research principles into candidate capabilities that can be expressed using existing HOMELAB components (WorkGraph, ActionPlane, EvidenceLedger, hypothesis state, capability composition) without introducing new scheduler, truth authority, execution authority, or persistent state ownership.  
**Architecture note:** Inspected Harness repository structure (action_plane.py, dynamic_workgraph.py, capability_chain_engine.py, discovery_hypotheses.py, etc.). All proposals below are classified as guidance for existing components or as potential Architecture Change Proposals (ACP) if they require new contracts. No F1–F12 foundation modifications are proposed here.  
**Revision note:** Revised 2026-10-16 to correct TA-H002, TA-H004, and TA-H006.  
**Date:** 2026-10-16

## Classification key

- **Deterministic infrastructure:** Rule or check that can be implemented without model judgment.  
- **Model reasoning / retrieval guidance:** Pattern that should be supplied to the research model as context or retrieved principle.  
- **Existing component extension:** Fits within current WorkGraph, ActionPlane, or EvidenceLedger contracts.  
- **ACP required:** Would need an Architecture Change Proposal if implemented as new contract.

---

## TA-H001 — Scoped negative interpretation

**Maps to:** TB-Q001  
**Classification:** Model reasoning guidance + EvidenceLedger annotation.  
**Existing components:** EvidenceLedger (record experiment outcome with scope), discovery_hypotheses.py or equivalent hypothesis state.  
**Proposed use:** When an experiment returns a negative result, the research model should be prompted or retrieved with the principle that the negative is scoped to the tested inputs, identity, and assumptions. The EvidenceLedger entry should record the tested scope explicitly.  
**Does not:** Automatically close a hypothesis. Does not grant new execution rights.  
**Validation:** Check that negative annotations remain scoped in subsequent planning.

---

## TA-H002 — Distinguish blockage reasons in hypothesis state

**Maps to:** TB-Q002  
**Classification:** Model reasoning guidance + existing hypothesis-state annotation.  
**Existing components:** Hypothesis / discovery state (not WorkGraph task status).  
**Proposed use:** When a direction is blocked, record the reason in the hypothesis state, distinguishing at least:
- Missing precondition (recoverable if the precondition can be observed or constructed within authorized scope)
- Cost / complexity judgment (abandoned for resource reasons; may be revisited)
- Authorization limit (blocked by policy; not a research conclusion)
- Experimental negative (scoped result under tested conditions)

Do not collapse these into a single WorkGraph node flag. WorkGraph remains a task/execution structure; research conclusions about recoverability belong in hypothesis state.  
**Does not:** Automatically re-execute. Does not override budget or authorization. Does not treat authorization limits as scientific findings.  
**Validation:** Verify that authorization-blocked and cost-abandoned paths are not treated as falsified hypotheses.

---

## TA-H003 — Missing-prerequisite search guidance

**Maps to:** TB-Q003  
**Classification:** Model reasoning / retrieval guidance.  
**Existing components:** Capability composition surfaces, discovery runtime.  
**Proposed use:** When the model identifies two or more blocked primitives with different missing preconditions, retrieve the principle and prompt the model to generate questions about observable surfaces that might supply the missing link (client-side artifacts, debug endpoints, early-response behaviors) within the currently authorized action space.  
**Does not:** Authorize new endpoints or expand the permitted action space.  
**Validation:** Confirm that suggested searches remain inside authorized scope.

---

## TA-H004 — Controlled comparison for connection-reuse effects

**Maps to:** SRC-000026  
**Classification:** Model reasoning guidance + deterministic measurement support.  
**Existing components:** ActionPlane HTTP request handling.  
**Proposed use:** When an HTTP behavior is observed that may be related to desync, pipelining, or connection state, perform a controlled comparison: measure the behavior both with connection reuse enabled and with connection reuse disabled. Use the comparison to distinguish:
- Artifact of the testing tool or connection handling
- Behavior that depends on connection state
- Behavior independent of connection reuse

Do not treat “disable connection reuse first” as a hard filter that decides whether further investigation continues. Connection reuse can be a required condition for some real vulnerability classes.  
**Does not:** Change authorization.  
**Validation:** Test against known cases where the signal appears only with reuse, only without reuse, and in both conditions.

---

## TA-H005 — Schema recovery from structured errors

**Maps to:** SRC-000008  
**Classification:** Model reasoning guidance + deterministic capture.  
**Existing components:** EvidenceLedger (store error responses), ActionPlane.  
**Proposed use:** When an API returns structured error messages that reveal expected fields or types, capture the error in EvidenceLedger and make it available to the research model as environment model update before further injection testing.  
**Does not:** Automatically mutate requests.  
**Validation:** Ensure error capture does not leak sensitive data beyond the authorized engagement.

---

## TA-H006 — Known-token candidates as hypotheses, not facts

**Maps to:** SRC-000008 and similar XBOW cases  
**Classification:** Model / retrieval guidance.  
**Existing components:** Application intelligence / environment model; existing secret-handling paths.  
**Proposed use:** When prior knowledge or retrieval surfaces a well-known default credential or token that may be relevant to the target, record it as a hypothesis about the current environment, not as a verified fact. Any attempt to verify or use the token must go through existing authorized secret-handling and engagement-rule mechanisms.  
**Does not:** Automatically treat the token as present. Does not bypass secret-handling contracts. Does not expand authorization.  
**Validation:** Confirm that token hypotheses remain hypotheses until verified under authorized conditions, and that secret handling is unchanged.

---

## TA-H007 — Human-override candidate for abandoned heuristics

**Maps to:** SRC-000003  
**Classification:** Model guidance + optional human review hook (existing approvals if present).  
**Existing components:** Agent supervisor or approvals path, if already present.  
**Proposed use:** When the model abandons a direction solely due to perceived cost or complexity, surface a short summary of the abandoned idea for optional human review rather than discarding it silently.  
**Does not:** Require human intervention. Does not create a new approval authority.  
**Validation:** Measure whether the hook produces useful recoveries without excessive noise.

---

## TA-H008 — Deterministic validators for model proposals

**Maps to:** SRC-000031  
**Classification:** Existing EvidenceLedger / proof contracts.  
**Existing components:** EvidenceLedger, candidate-to-proof runtime.  
**Proposed use:** Continue to require deterministic or independently verifiable checks before any model-proposed finding is treated as evidence. Model proposals remain proposals.  
**Does not:** Change existing truth authority boundaries.  
**Validation:** Audit that no model output is promoted without evidence contract satisfaction.

---

## Summary of authority boundaries

None of the heuristics above introduce:
- A new scheduler
- New truth authority
- New execution authority
- New persistent state ownership outside existing WorkGraph / EvidenceLedger / hypothesis-state contracts

Any implementation that would require new contracts must be submitted as an Architecture Change Proposal and evaluated against the frozen F1–F12 foundations.

**All heuristics remain provisional.**
