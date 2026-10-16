# Independent primary-source analysis: SRC-000024 to SRC-000043

**Date:** 2026-10-16. **Status:** primary URLs checked; 19 successfully opened, 1 failed (`SRC-000032`); analytical observations remain **provisional/unreviewed**. Longer whitepapers were sampled at introduction and relevant methods, not read exhaustively line-by-line. No archived text, source fingerprint, predecision snapshot, or training approval.
**Scope:** Distinguish a case's stated research problem, the exposed method, source-reported observation, transfer hypothesis, and inaccessible history. Do not force policy ledgers, curated top-10 articles, vendor claims, or huge case anthologies into false X→Y diarized single investigations.

## SRC-000024 — HTTP Terminator: novel autonomous desync research

- Primary source: https://portswigger.net/research/can-ai-do-novel-security-research
- Locator: Introduction; Ideation; Evaluation; Weaponization; Cascade
- **Research question / knowledge gap:** How can human research methods be decomposed into a self-feeding but evidence-bounded autonomy loop?
- **Source-supported process or finding:** Expert first tests whether LLM can rediscover unpublished protocol-ruler trick: generic prompt poor, analogy anchor even hurt, micro-inspiration from RFCs generated much broader candidates; author then validated on live authorized programs, distinguished anomalies from verified impact and fed novel signals back into cascade.
- **Limit / possible error:** Research methodology with explicitly reported experiments and technical case studies. Micro-inspiration, context anchoring, evaluation oracle specificity and anomaly-driven cascade all require distinct traces; publisher's own metrics are not independent controlled proof.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000025 — HTTP/1.1 must die

- Primary source: https://portswigger.net/research/http1-must-die
- Locator: Abstract; problem framing
- **Research question / knowledge gap:** Can many apparently separate request-smuggling cases share a dangerous protocol-level invariant?
- **Source-supported process or finding:** The author argues repeated implementation-level patches have not resolved weak HTTP/1.1 request isolation and presents new classes and a toolkit for finding parser disagreement.
- **Limit / possible error:** Published broad technical paper; protocol generalization is an argued conclusion, not proof that every deployment is vulnerable; individual study chronology requires section-specific reconstruction.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000026 — HTTP pipeline vs smuggling false positives

- Primary source: https://portswigger.net/research/how-to-distinguish-http-pipelining-from-request-smuggling
- Locator: Connection reuse false-positives; Connection-locked request smuggling; Connection state attacks
- **Research question / knowledge gap:** Is an apparent desync a client-to-server framing artifact or cross-user/request isolation failure?
- **Source-supported process or finding:** Compare behavior with and without connection reuse; constrain hypotheses to connection-locked smuggling, connection-state behavior or client-side desync as needed; demand impact evidence.
- **Limit / possible error:** Methodology for differential oracle validation; not one investigator timeline; apparent false positive can be genuine under extra prerequisites.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000027 — Browser-powered desync research

- Primary source: https://portswigger.net/research/browser-powered-desync-attacks
- Locator: Abstract; research journey and methodology
- **Research question / knowledge gap:** Can a victim browser be the client that creates the connection-level condition previously thought attacker-only?
- **Source-supported process or finding:** Reframe attacker infrastructure assumption by treating browser connections as transport; combine cross-domain/browser constraints with adapted desync probes; author reports novel testing methodology.
- **Limit / possible error:** Broad set of cases; first-person synthesis, not a chronological lab notebook for every subfinding; avoid reusing impact anecdotes as independent investigation lineages.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000028 — HTTP/2 technical desync research

- Primary source: https://portswigger.net/research/http2
- Locator: Abstract
- **Research question / knowledge gap:** Which implementation and protocol-translation assumptions introduce new attack surface when HTTP/2 is treated as a mere transport upgrade?
- **Source-supported process or finding:** Research examines HTTP/2-specific desync, tunneling and parser discrepancy where false-positive interpretation is a key obstacle.
- **Limit / possible error:** Technical case anthology; separate discovery lineage and weaponization examples; initial ideation and exact chronology mostly undocumented in page abstract.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000029 — HTTP desync 2019

- Primary source: https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn
- Locator: Abstract; methodology
- **Research question / knowledge gap:** Does a front-end/back-end interpret HTTP message boundaries differently and thereby violate request isolation?
- **Source-supported process or finding:** Author builds a black-box detection and proof methodology around cross-parser differential, then explores varied target impacts.
- **Limit / possible error:** Historical technique revival and substantial set of targets; not one continuous experiment; case claims need separate evidence.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000030 — XBOW GPT-5.5 evaluation announcement

- Primary source: https://xbow.com/blog/gpt-5-5-and-xbow-a-step-change-in-autonomous-application-security
- Locator: How GPT 5.5 Performed; Model Capability Alone is Never the Whole Story
- **Research question / knowledge gap:** Does changing model improve entire supervised-orchestrated workflow rather than only isolated bug recognition?
- **Source-supported process or finding:** XBOW reports internal test differences, auth-workflow speed and reduced misses; differentiates model intelligence from orchestration, evidence and governance.
- **Limit / possible error:** Marketing/publisher-reported aggregate comparison; missing blinded raw tasks and independence. No source-supported individual X→Y discovery trajectories.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000031 — XBOW Mythos and GPT-5.5 research claims

- Primary source: https://xbow.com/blog/mythos-gpt-5-5-ai-vulnerability-detection-security
- Locator: Coverage discussion; model-harness framing
- **Research question / knowledge gap:** Does finding one bug imply adequate systematic coverage and trustworthy validation?
- **Source-supported process or finding:** Publisher argues model persistence and revisit behavior can be weak, so independent coverage/orchestration is necessary.
- **Limit / possible error:** Position article with vendor claims; distinguish methodological recommendation from measured causal result; no case-by-case raw traces.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000032 — Google Project Zero Naptime to Big Sleep

- Primary source: https://googleprojectzero.blogspot.com/2024/11/from-naptime-to-big-sleep.html
- Locator: Access: failed opening 2026-10-16
- **Research question / knowledge gap:** UNAVAILABLE — no direct source-supported question reconstruction.
- **Source-supported process or finding:** The canonical address returned an internal error in the retrieval step; do not convert title or other article summaries into evidence.
- **Limit / possible error:** source_not_read; requires retry via publisher mirror or preserved capture, do not train.
- **Status:** source_inaccessible; unreviewed; training-blocked.

## SRC-000033 — Windows race conditions by path lookups

- Primary source: https://projectzero.google/2025/12/windows-exploitation-techniques.html
- Locator: Introduction; Investigating Object Manager Lookup Performance
- **Research question / knowledge gap:** How can a tiny state-change race window be made observable/controllable by manipulating named-resource lookup latency?
- **Source-supported process or finding:** James Forshaw explains transfer from previous race-timing methods toward object-manager namespace lookup; 2016 piece republished with modern Windows update.
- **Limit / possible error:** Originally conceived in 2016, republished 2025: preserve separate event and publication times. Documented own reasoning, not universal path recipe.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000034 — Knowledge-driven CoreAudio fuzzing

- Primary source: https://projectzero.google/2025/05/breaking-sound-barrier-part-i-fuzzing.html
- Locator: The Approach: Knowledge-Driven Fuzzing
- **Research question / knowledge gap:** How should coverage plateaus turn into manual reverse engineering and better harness design rather than aimless extra fuzzing?
- **Source-supported process or finding:** Author explicitly cycles vector → target → harness → fuzz → crash/coverage → manual analysis → harness iteration.
- **Limit / possible error:** First-person methodology with code artifact links; author says hybrid method was learned from another researcher. Persist origin of principle and empirical outcomes separately.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000035 — Windows Registry exploitation options

- Primary source: https://projectzero.google/2025/05/the-windows-registry-adventure-8-exploitation.html
- Locator: Where to start: high-level overview of potential options
- **Research question / knowledge gap:** Given controllable hive allocator and known memory corruption, which target cell and mitigation bypass strategy is tractable?
- **Source-supported process or finding:** Author narrows multiple candidate primitive/target alternatives using exploitability constraints; setup assumes earlier attack-surface research in Part 7.
- **Limit / possible error:** Continuation of same project, not standalone discovery; candidate selection is reported retrospective design; missing earlier investigation unless linked to part 7.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000036 — Project Zero policy 2025

- Primary source: https://projectzero.google/2025/07/reporting-transparency.html
- Locator: The Trial: Reporting Transparency; Why the Change
- **Research question / knowledge gap:** Can earlier transparency close downstream upstream patch-adoption gap?
- **Source-supported process or finding:** Publisher proposes public metadata shortly after reporting while retaining disclosure windows.
- **Limit / possible error:** Policy design rationale, not vulnerability research X→Y; evaluate institutional risk decision not attacker experiment.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000037 — PZ Reporting Transparency 2025 ledger

- Primary source: https://projectzero.google/reporting-transparency-2025.html
- Locator: 2025 disclosure tables
- **Research question / knowledge gap:** What can be known from published report/fix/protection dates?
- **Source-supported process or finding:** Dates and known/unknown patch-protection labels are logged per issue; not researcher hypotheses or discovery choices.
- **Limit / possible error:** Structured timeline metadata; historical status revisions matter, no actor mind inference, possible overlapping issue lineages.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000038 — PZ Reporting Transparency 2026 ledger

- Primary source: https://projectzero.google/reporting-transparency.html
- Locator: Current 2026 disclosure tables
- **Research question / knowledge gap:** What report dates and vendor states are documented, with what censorship/unknown future states?
- **Source-supported process or finding:** Publisher maintains current list including recent report entries; many details intentionally withheld until disclosure.
- **Limit / possible error:** Dynamic page; immutable snapshot mandatory for time-based use; no X→Y discovery evidence.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000039 — Smashing the state machine

- Primary source: https://portswigger.net/research/smashing-the-state-machine
- Locator: Outline; Beyond limit-overrun; methodology
- **Research question / knowledge gap:** Were race conditions underestimated because timing jitter and weak tools limited observable behaviors?
- **Source-supported process or finding:** Author introduces workflow/state transition race models and single-packet alignment to separate concurrency vulnerability from measurement noise.
- **Limit / possible error:** Multiple case studies; do not treat all as one historical diary or report framework claims as universal.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000040 — Listen to the whispers

- Primary source: https://portswigger.net/research/listen-to-the-whispers-web-timing-attacks-that-actually-work
- Locator: Abstract; methodology
- **Research question / knowledge gap:** Can sub-millisecond response timing differences expose hidden features and server behaviors that standard response inspection misses?
- **Source-supported process or finding:** Author builds high-precision differential measurement tools then uses them to investigate invisible surface and hidden routes.
- **Limit / possible error:** Technical-methodology anthology; must preserve control/latency measurement assumptions and false positives, not only final effect.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000041 — HTTP Anomaly Rank

- Primary source: https://portswigger.net/research/introducing-http-anomaly-rank
- Locator: HTTP Anomaly Rank; Backslash Powered Scanner antecedent
- **Research question / knowledge gap:** How can thousands of noisy HTTP responses be ranked without pre-committing to a specific expected exploit signature?
- **Source-supported process or finding:** Author transfers stable-response attribute diffing developed in 2016 to a response anomaly ranking algorithm integrated into testing tools.
- **Limit / possible error:** Harness/measurement innovation, not a full vulnerability trajectory. Distinguish ranking novelty from validated security impact.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000042 — Top techniques of 2024

- Primary source: https://portswigger.net/research/top-10-web-hacking-techniques-of-2024
- Locator: Community nomination and voting method
- **Research question / knowledge gap:** How does an expert community identify innovative methods across many independent authors?
- **Source-supported process or finding:** Article describes nominations, shortlist, expert panel, then commentary on winners.
- **Limit / possible error:** Secondary curated overview, not a source for winner researchers' private processes; use outgoing first-party links as leads and don't double-count.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## SRC-000043 — Top techniques of 2025

- Primary source: https://portswigger.net/research/top-10-web-hacking-techniques-of-2025
- Locator: Community nomination and voting method
- **Research question / knowledge gap:** What evaluation criteria and community filters selected the top methods?
- **Source-supported process or finding:** Article reports crowd nomination and panel selection with named finalists; leads to many primary articles.
- **Limit / possible error:** Secondary curated overview and selection-bias sample; not 10 independent research traces contained in one article.
- **Status:** primary_article_inspected_bounded; unreviewed; training-blocked.

## Emerging but unvalidated research dimensions

- **Observation-oracle design** is part of research intelligence: instrument design changes what research can discover (24,26,39,40,41).
- The distinction between **coverage confidence** and a single validated finding belongs to system-level evaluation (30,31) but the vendor claims lack open replication.
- Reporting-policy ledgers and community rankings are **different evidence genres** from investigation decisions; they are useful for lineage, context and source acquisition, not for fabricating inner process (36-38,42-43).
- Research authors describe multiple independent campaigns in long whitepapers; careful segmentation is required to avoid circular/correlated training examples.
