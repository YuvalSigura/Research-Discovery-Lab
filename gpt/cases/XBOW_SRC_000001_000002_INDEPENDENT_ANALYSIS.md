# Independent reconstruction: Chrome full-chain, SRC-000001 and SRC-000002

**Date:** 2026-10-16. Sources read: official first-party XBOW announcement and detailed authored technical post. Independent from Grok files; the user had previously supplied Grok's draft observations in conversation, so this supplement should not be represented as completely blinded to all outside commentary. The earlier gpt/pass1 report existed before comparison. No complete raw campaign log, source content snapshot hash, curator adjudication, or predecision training approval.
**Lineage:** two publications of one Chrome project with an initial ineligible chain and later revised rewarded chain; neither are independent discoveries. The announcement is not a second scientific replication. Dates are published high-level campaign dates; the technical author says chronology will be covered separately.

## SRC-000001 — CEO high-level research announcement

First-party publication: https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit. Author/actor scope: Oege de Moor; XBOW team.

### T01 — How we did it
- X: Strategic expansion from web-app to compiled targets
- Candidate research question: Can a hybrid model-and-human team assemble a full Chrome attack chain by a challenging external deadline?
- Source-reported decision/test: Leadership chose Chrome and an August Black Hat target; researchers assigned strategic roles, agents conducted source/PoC work.
- Reported result: Author reports a first assembled chain, disqualified because Google already knew one bug.
- Y: Need new chain or replacement components; target achievement not identical to scientific novelty.
- Claim basis: explicit_author_reported; exact actual decision cutoff not known.

### T02 — How we did it
- X: First chain reported ineligible due collision
- Candidate research question: How can stage substitution be made cheap if an independently discovered stage duplicates prior vendor knowledge?
- Source-reported decision/test: Publisher describes a three-stage modular chain with alternatives; human team redirected search.
- Reported result: Later awarded six-day chain assembled with component replacement.
- Y: Modularity permitted substitution, but exact date of first architecture adoption is unknown.
- Claim basis: chronology_partially_known; exact actual decision cutoff not known.

## SRC-000002 — technical first-party retrospective; project notes

First-party publication: https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain. Author/actor scope: Brendan Dolan-Gavitt and XBOW team.

### T01 — Opening; six-day paragraph
- X: Full-chain objective under strict sandbox boundaries
- Candidate research question: Which narrower parallel research tasks can be run concurrently without sacrificing integration?
- Source-reported decision/test: Team separated broad search, V8 memory corruption, sandbox escapes and integration into agents/experts working in parallel.
- Reported result: Publisher describes modular stage interfaces and backups, no day-specific assignment.
- Y: Parallel campaigns and clean integration interfaces are documented, but cannot infer exact serial sequence.
- Claim basis: explicit_author_reported; exact actual decision cutoff not known.

### T02 — Stage 2: Two WebPs Diverged in a V8 Cage
- X: Needed V8 sandbox escape after in-cage access
- Candidate research question: What assumptions must downstream Blink code honor when attacker-controlled V8 objects are mutable?
- Source-reported decision/test: Authors explicitly decided not to attack V8 sandbox itself but to inspect other consumers' obligations under its threat model.
- Reported result: Author reports a WebCodecs/ImageDecoder transfer whose apparent immutable backing content could change under in-cage control, producing a WebP inconsistency.
- Y: Shift from internal sandbox bypass to external consumer invariants.
- Claim basis: explicit_author_reported; exact actual decision cutoff not known.

### T03 — Swapping Out the Middle
- X: Chain middle initially used Gin-related candidate
- Candidate research question: Could a duplicate stage be replaced without restarting the entire integrated chain?
- Source-reported decision/test: Check collision against known Google bug; replace V8 escape stage via predesigned interchangeable interface.
- Reported result: The Gin candidate collided with vendor issue; team replaced middle stage with animated WebP.
- Y: Final reported chain regained eligibility and worked in demonstration.
- Claim basis: explicit_author_reported; exact actual decision cutoff not known.

### T04 — Stage 3: The Renderer Refuses to Chill Out
- X: Renderer snapshot processing assumed source process frozen
- Candidate research question: Is the purported stable remote memory actually immutable in the face of special thread semantics?
- Source-reported decision/test: Test premise of complete target suspension and remote-copy retry; author describes freeze-exempt thread behavior.
- Reported result: Snapshot helper used first read error to derive retry length, which was unsafe when remote memory protections changed.
- Y: Demonstrated a time-dependent assumption violation in Crashpad logic; historical route to this question is not given.
- Claim basis: retrospective_technical_explanation; exact actual decision cutoff not known.

### T05 — Conclusions
- X: Three final bugs were all said to involve mutable state presumed immutable
- Candidate research question: Was this shared invariant the research team's a priori search strategy?
- Source-reported decision/test: Article's conclusion identifies the pattern after successful chain completion.
- Reported result: Author presents similarity as a retrospective observation, not documented original strategy for selecting all stages.
- Y: Label candidate generalized invariant-checking principle, not historical decision motivation.
- Claim basis: retrospective_analyst_pattern; exact actual decision cutoff not known.

## High-risk inference traps

1. Conclude only a six-day date window, NOT a day-by-day mapping for each vulnerability.
2. The Gin duplicate caused a replacement, but the modular architecture's exact original decision timestamp is not established.
3. Logical exploit stage prerequisites are not equivalent to actual chronological idea discovery.
4. The shared 'mutable thought immutable' motif appears in Conclusions, not necessarily in a contemporaneous overall search prompt.
5. Human intervention and agent research both contributed; do not assign individual unobserved private motives.
6. Reward, reproducibility and API spending are publisher claims; no independent economic or model-effectiveness benchmark is established.

