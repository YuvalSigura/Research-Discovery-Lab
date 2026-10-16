# First-mission primary-source verification and partial trajectory reconstruction

**Intake date:** 2026-10-16  
**Review state:** analyst source inspection; **NOT curator-reviewed**.  
**Purpose:** Ground Grok's first-mission source-discovery report in public primary-source evidence and populate a *bounded* first set of research decision points. Not an exhaustive corpus, a full historical log, proof of zero-days, a training dataset, or permission to republish source material.

## What entered the typed registries

| Case | Source | Status | Evidence-bearing narrative |
| --- | --- | --- | --- |
| `CASE-000073` / `SRC-000073` | [James Kettle, *How I choose a security research topic*](https://portswigger.net/research/how-i-choose-a-security-research-topic), published 2023-06-14, updated 2025-04-10 | partial reconstruction | Short viability test ruled out first concept; second concept lasted six weeks before failure; reused tooling made race conditions cheap to test; author also discusses audience value and personal development |
| `CASE-000074` / `SRC-000074` | [watchTowr Labs, *.MOBI WHOIS*](https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/), 2024-09-11 | partial reconstruction | Laboratory precondition challenged; abandoned infrastructure made WHOIS response control plausible; old-client traffic contradicted assumptions; a provider's negative result led to parser-compatibility reconsideration; authors explicitly stopped before rogue certificate issuance |
| `CASE-000002` / `SRC-000002` | [XBOW, *Zero to Calc in Six Days*](https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain), October 2026 | five additional **partial** events | Parallel agent/human work, duplicate Gin stage, modular replacement with animated WebP, author-reported confirmation |

All added `EVT` events cite **named sections of public primary articles**. Where exact event/knowledge timestamps were not established, the fields remain null. These are **retrospective public narratives**, not contemporaneous lab notebooks. Their historical origin means the **public author documents the described occurrence**; it does not prove that the stated motivation was recorded at that historical time. No `CTX` pre-discovery snapshot has been approved.

Registry source entries remain `capture_status=not_archived`, `sha256=null`, `license_status=unreviewed`. No article HTML/PDF, screenshots, verbatim text passages, or third-party assets were committed. The *source URL and section title* are the locator, not an immutable captured quotation or content hash.

## Important corrections to loose Grok interpretations

1. **.MOBI did not demonstrate unauthorized certificate issuance.** The authors describe reaching a certificate provider's **email validation choice**, then explicitly stopping. Actual certificate issuance, victim compromise and completed unauthorized RCE remain **unproven by this report**. In addition, the article documents a provider test that initially *did not* show the controlled email. It would be invalid to label that observation as proof the provider was safe, or to claim all CA providers were affected.
2. **PortSwigger's topic-selection article is methodology rather than a complete vulnerability discovery timeline.** It supports explicit *decision criteria and abandoned directions*, but not a complete chronology or the full experiments behind the ultimately reported race-condition finding.
3. **XBOW's Gin duplicate is a research collision, not evidence of a failed exploit.** The technical article itself notes it focuses on vulnerabilities and mechanics; fuller process chronology and agent traces are not present. The human/AI task allocation is described by the publisher, not independently audited.
4. **ShadowPanel is already present** as `CASE-000055` with a partial trajectory. The Grok summary does not warrant a duplicate CASE or an invented second experiment.
5. **ServiceNow**: [the original researcher write-up, now hosted by Searchlight Cyber](https://www.slcyber.io/research/chaining-three-bugs-to-access-all-your-servicenow-data) starts with architectural routing questions and provides a substantive technical investigation. It is a **next reconstruction candidate**, not treated as a finished case in this commit. The former Assetnote URL redirects; preserve both canonical destination and origin when adding it.

## Provenance and evidence limits

- This work verifies **that the cited first-party pages contain these narrative descriptions**; RDL did not repeat attacks or obtain original investigator notes. `documented` is not synonymous with independently verified.
- Do not infer exact historical internal beliefs or private intentions from retrospective prose. Any proposed questions not explicitly articulated by the article belong in `origin=reconstructed` / `evidence_status=proposed`, not historical mode.
- Events reflect source-supported ordering only where a narrative says so; a `followed_by` relation is not causal proof. No exact times are manufactured from article publication dates.
- An avenue rendered **unreachable by a prerequisite** is not necessarily an experiment that failed. This matters especially for the .MOBI/Fail2Ban candidate.
- Each source currently supports **one published account**, not full independent reproduction or external corroboration. The `discovery_assessment` of newly created CASEs is `unassessed`.
- Related cases **have not** been assigned reviewed umbrella-question families (`QPT/QMP`) or reviewed mindset labels (`MND`). Similarities such as 'unmet precondition', 'fast failure' and 'modular substitution' are **comparative hypotheses only**.

## Candidate question comparisons — do not promote automatically

| Candidate question | Source-specific instantiations | Crucial difference / counterexample |
| --- | --- | --- |
| What prerequisite prevents a plausible idea from working in a real deployment? | .MOBI's unreachable WHOIS-server control; ShadowPanel's missing scan identifier | One concerns infrastructure ownership, the other an application identifier. Similar words do not establish same-core uncertainty. |
| What is the least costly experiment that separates viability from wishful thinking? | Kettle's realistic test site; .MOBI's query logging | Log collection estimates deployed exposure; a controlled prototype tests concept feasibility. Different evidence targets. |
| Can a useful line of work survive failure of one stage? | Chrome chain's Gin-to-WebP replacement; Kettle's reuse of tools after failed concept | Swapping a known duplicate chain component is not the same as changing the research topic. |

**These are analyst hypotheses** for later adversarial comparison, with inclusion/exclusion rules and independent review; no QMP convergence count is incremented.

## Handoff and next curation gates

1. Verify exact paragraph/section anchors against source revisions, and preserve snapshots **only if licensed**; otherwise keep URL, inspection date, and original-analysis notes. Capture version changes separately.
2. Reconstruct ServiceNow with its primary-source author perspective and independently identify what was known before the routing/templating analysis, including any genuinely described failures.
3. Add independent negative/inconclusive investigations, not merely failed steps on eventual successful chains.
4. Obtain a second reviewer to challenge inferred causation, missing alternative hypotheses and document provenance. Do not mark `hindsight_review=passed` without contemporaneous evidence and a defensible cutoff.
5. Keep Track A research-guidance extraction separate from Track B train/eval; no fine-tuning or pre-discovery training samples were produced here.

## Local verification

```bash
python tools/validate_archive.py
python tools/validate_registry.py
python tools/validate_publisher_sources.py
python -m unittest discover -s tests -p "test_*.py" -v
python -m research_engine reconstruct CASE-000073 --view historical
python -m research_engine reconstruct CASE-000074 --view historical
python -m research_engine reconstruct CASE-000002 --view historical
python -m research_engine question-convergence --min-cases 2
```

Expected: substantive historical retrospective narrative events in the three packs; **no invented pre-discovery truth and no approved cross-case equivalence**. GitHub Actions results for the associated commit are the integration-check evidence, not the existence of this document.
