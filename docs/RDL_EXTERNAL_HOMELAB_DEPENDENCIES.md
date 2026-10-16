# RDL ↔ HOMELAB external architecture references and ownership collision gate

**Status:** PROVISIONAL / UNVERIFIABLE_FROM_THIS_REPO  
**Date:** 2026-10-16  
**Purpose:** Make cross-repository references resolvable *as references*, without misrepresenting RDL as an owner or verifier of HOMELAB runtime code.

## Repository boundary

- RDL repository: `YuvalSigura/Research-Discovery-Lab`.
- External implementation project (reported by coordinator): `YuvalSigura/harness`, working copy `harness-ceo-test`, local branch `v2/gate-r-20261014`, reported local HEAD `387f7fe` as of 2026-10-16. **Not inspected here; those commits were reported unpushed and may have changed since.**
- F1–F12 are **externally maintained, frozen V1.2 foundational architecture contracts**, not definitions in the RDL repository. RDL does not certify them, import them, redefine them or mark conformance `PASS`.
- `FUP-B1` (experiment satisfaction) and `FUP-B3` (stagnation / rediscovery) are separate HOMELAB work items. Their implementation/release status is **UNVERIFIABLE_FROM_THIS_REPO**. Supervisor has reported pending local P0 follow-up defects D1/D2; RDL does not declare them fixed.
- Authoritative proof, action/authorization, secret, state and scheduling ownership remains in the actual HOMELAB architecture, not in this RDL research documentation.

**Do not infer a branch's code SHA from a PR summary.** Before an RDL principle becomes an implementation ticket, attach exact repository + inspected commit SHA + production caller + current writer/owner + scope/authorization/proof invariant + tests. An inaccessible local working tree makes the hook `UNVERIFIED`, not `MISSING`.

## Explicit named-component collision checklist

These names are **reported candidate existing HOMELAB components**, not code-verified implementation locations. Record the exact source file/function and ownership contract before relying on them.

| RDL heuristic / proposed feature | First existing owner/components to audit | Critical non-duplication test |
|---|---|---|
| TA-H001 scoped negatives | `XART/EvidenceLedger`, `ResearchStateStore`, existing experiment-outcome/reducer consumers | Do not add a second evidence truth writer or independent hypothesis closure |
| TA-H002 reason-typed blockers | `ResearchStateStore`, hypothesis owner, convergence reducer, `WorkGraph` | WorkGraph task state vs hypothesis conclusion; no new "hypothesis store" without real ownership review |
| TA-H003 missing prerequisites | `SurfaceGraph`, `EvidenceBackedExhaustion`, `discovery_fabric`, existing capability/plan representation | No second prerequisite graph/scheduler and no automatic capability grants |
| TA-H004 HTTP reuse controls | `ActionPlane`, permitted HTTP transport/capture, evidence correlation | No unapproved requests; differentiated real state-dependent effects vs tool artifacts |
| TA-H005 schema from errors | `ApplicationIntelligenceEngine`, discovery fabric, existing evidence capture/redaction | Avoid parallel environment model ownership or unredacted error stores |
| TA-H006 default-credential hypothesis | Existing secret authority, `ApplicationIntelligenceEngine`, `ActionPlane` authorization | Secrets remain secret; no implicit authorization or promotion from retrieval |
| TA-H007 optional human review | Existing supervisor/approval authority and WorkGraph planning | No hidden scheduler, approval authority or unbounded queue |
| TA-H008 deterministic proof | `XART/EvidenceLedger`, verifier, `ProofLifecycle`, existing claim lifecycle | Model output never becomes VERIFIED on its own |
| RDL prospective context | Existing WorkGraph/owner event model, `ResearchStateStore`, evidence store | No new persistence authority; immutability/replay and model-input capture verified |
| Semantic action-state discovery | `CoverageLedger`, `SurfaceGraph`, `ApplicationIntelligenceEngine`, `discovery_fabric`, `state_epoch_recon` | Reuse actual coverage/state epochs; no duplication of discovery state graph |

The terms `CoverageLedger`, `SurfaceGraph`, `EvidenceBackedExhaustion`, `ApplicationIntelligenceEngine`, `ResearchStateStore`, `discovery_fabric`, `state_epoch_recon`, `WorkGraph`, `ActionPlane`, `ProofLifecycle` and `convergence reducer` are **inspection targets**. The review that listed them did **not** inspect the external repository's current code. A name match is not proof the behavior is implemented and wired.

## Architectural approval contract

1. Locate exact existing authority owner and production path in the target checked-out branch.
2. Classify planned feature `already_wired`, `existing_but_not_wired`, `partial`, `missing`, or `unverified` with code-and-test evidence.
3. Route advice through the existing reasoning/planning interfaces. Actual target execution stays with ActionPlane; state writes with existing owner; proof promotion with verifier/proof lifecycle; secrets with existing secret authority.
4. Implement no new truth/target execution/scheduler/secret resolver/persistent state/global-namespace authority without approved Architecture Change Proposal when truly required.
5. Require policy, replay, restart, identity, event causality and no-silent-success tests. An offline RDL benchmark may be run independently in a controlled simulated fixture without asserting HOMELAB runtime conformance.

**Cross-project gate:** Offline research-question evaluation requires its own scientific checks (independent fixture authors, lineages, power/IRR and leakage), **not** a claim that HOMELAB P0/Phase 0.5 is finished. Live HOMELAB prospective data capture or runtime deployment additionally requires independently verified branch-specific conformance and authorization.
