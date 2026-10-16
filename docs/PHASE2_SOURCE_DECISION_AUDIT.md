# Phase 2 — Source-grounded decision corpus and scientific review queue

**Prepared:** 2026-10-16 · **Status:** initial analyst reconstruction, **not** independently curator-reviewed or blind-qualified. No target requests, exploit execution, fine-tuning, or copyrighted source mirroring.

## Implemented in this increment

- Two new primary-source CASE/SRC pairs: `CASE-000075` (ServiceNow) and `CASE-000076` (negative OpenVAS-claim investigation). Both are retrospective author accounts, not reconstructed contemporaneous laboratory notebooks.
- 33 new research EVT events / 30 REL links. Historic events retain unknown `occurred_at` / `known_at` and `hindsight_review=not_reviewed`. Analyst question reformulations are explicitly `origin=reconstructed` with `evidence_status=proposed`; their links are `causal_basis=reconstructed`, not `explicit_documented`.
- Four **unreviewed** source-linked MND observations, two **proposed** QPT research-question candidates, and three **proposed** QMP comparisons. These **do not** establish convergent underlying questions or the originality of any investigator's thinking.
- `tools/triage_source_candidates.py` consumes a scout/Grok JSON candidate array and builds a **read-only** deduplicated intake queue. It flags non-first-party or preview-only sources and never grants redistribution rights or stable SRC identifiers.
- `tools/curation_readiness.py` inventories missing evidence and curation gates on real cases.
- `tools/build_predecision_candidates.py` exports **review-only**, source-free decision prompts only when a human-reviewed context has documented evidence sourced to material published **before** its cutoff. No approved CTX records exist yet, so the actual archive should export **zero** candidate tasks. The exporter does not include a solution label and uses operator-keyed opaque IDs; it does not guarantee that observation prose is semantically anonymous.
- `tests/test_phase2_curation.py` checks provenance, nonpromotion, expected negative result, and blind-export rejection cases.

## Publisher source review

| Source | Grounded trajectory | Critical uncertainties |
| --- | --- | --- |
| **ServiceNow** — [Adam Kues, *Chaining Three Bugs to Access All Your ServiceNow Data*](https://www.slcyber.io/research/chaining-three-bugs-to-access-all-your-servicenow-data), original Assetnote research, currently hosted by Searchlight Cyber, **2024-07-11** (`SRC-000075`) | The author explicitly begins with **how routing works** (*The Architecture*). They explain DB-backed route types and two-stage rendering (*Signs of Trouble*), try an unauthenticated title path, find a sanitization barrier (*Bug 1*), describe two unsuccessful namespace experiments before changing their syntactic assumption (*Bug 2*), then inspect inconsistent path normalization before a claimed database-credential read (*Bug 3*). Disclosure was reportedly **2024-05-14** (*Conclusion*). | No contemporaneous notes or exact timing for internal decisions. Question paraphrases `EVT-000050` and `EVT-000060` are **analyst reconstructions**. The article reports reproduction in its environment and vendor patches; RDL has not tested ServiceNow or independently verified full deployment impact. |
| **OpenVAS false-positive** — [Arafat Afzalzada/Stingrai, *The Perils of Premature Vulnerability Reporting*](https://www.stingrai.io/blog/the-perils-of-premature-vulnerability-reporting-a-case-study-in-off-by-one), **2026-01-07** (`SRC-000076`) | The account traces a suspected allocation shortfall, warning from an initial ASan test, vendor disagreement, recalculation of separator+NUL bytes, revised tests, and the publisher's negative conclusion. It is one **negative investigation**, not evidence that every OpenVAS version is secure. | We lack independently preserved vendor communications, commit/version pin, original instrument files and independent reproduction. Importantly, the article's pictured canaries surround fields in a struct that holds a **separately allocated pointer** to the tested buffer; on the information shown, those canaries alone are not a demonstrated adjacent heap-buffer guard. Arithmetic and the later explanation are material distinct evidence; do **not** promote 'canaries intact' into an independently established universal negative. |
| **ShadowPanel** — [Pentera primary account](https://pentera.io/resources/research/) (`CASE-000055`) | Existing partial variant-analysis, blocked scan-identifier and rediscovery trajectory retained. An MND observation is linked to its explicit question-to-direction edge. | No contemporaneous cutoff or second reviewer; existing broad section locators need individual passage-level audit. |
| **watchTowr .MOBI** — [watchTowr original investigation](https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/) (`CASE-000074`) | Existing partial reconstruction retained. Loose 'TLS/SSL validation' section locators were corrected to the actual **Tales of TLS** heading. | No rogue certificate issued; account is retrospective. Initial provider negative and later parser adjustment are not independent replicas. |
| **PortSwigger topic selection** — [James Kettle](https://portswigger.net/research/how-i-choose-a-security-research-topic) (`CASE-000073`) | Existing author-reported fast-failure, abandonment and reused-tool reasoning retained; added a non-reviewed MND observation linked to an explicit question/experiment relation. | This is methodological reflection, not complete timestamped vulnerability discovery. |
| **XBOW Chrome** — [original report](https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain) (`CASE-000002`) | Five existing process events retained; a duplicate discovered component is a prior-art collision, not failed exploitation. | No agent-internal decision trail or independent research-dataset validation. |

## Comparison hypotheses: explicitly NOT scientific results

- `QPT-000001`: a **candidate** question about whether another dependency/interface makes a blocked direction reachable. `QMP-000001` (.MOBI) is `partial_overlap`; `QMP-000002` (reconstructed ShadowPanel question) is `analogy_only`. WHOIS reply-server ownership and possession of a scan identifier are not equivalent preconditions. No convergence count should increase.
- `QPT-000002`: proposed **instrument-validity** question based on a publisher-reported false positive. `QMP-000003` is a proposed specialization tied to a reconstructed diagnostic question. No independent case pair has been reviewed for equivalence.
- All four `MND` entries have `novelty=unassessed`, no implied expert causal effect, no outcome contribution claim and no curator approval.

## Evidence gates and first review tasks

1. **Source anchors**: locate exact paragraphs/section revisions for each critical EVT/REL; separate a named heading from an immutable captured passage. No `PAS` or RAW snapshots are asserted while rights remain `unreviewed`. Preserve the original Assetnote publishing identity versus the current Searchlight Cyber host.
2. **Second curator**: seek independent challenge on the first-person motive, negative result, event ordering, inferred relations and whether the proposed questions are actually comparable. Never impersonate a second human review.
3. **Negative controls**: acquire at least several independent negative/inconclusive investigations from different teams and mechanisms. Do not count a merely unsuccessful step in an eventual exploit chain as a separate independent negative investigation.
4. **Contemporaneous pre-decision contexts**: only curate `CTX` when the source set establishes a defensible historical knowledge cutoff. Later retrospective disclosures are **not** adequate to certify an earlier state. Presently **zero eligible contexts**.
5. **Prior-art and question families**: document inclusion/exclusion and competing framings; only independent human approval can promote QPT/QMP to `curator_reviewed`.
6. **Blind evaluation**: compare SAME loaded model, tool/token/time budgets and policy across no-context, relevant RDL, unrelated RDL and oracle/upper-bound conditions; hold out researcher, publisher, research lineage, mechanism and time. Decision grading must be independent of the model and measured on unseen contexts, not reconstructed after viewing the end.
7. **HOMELAB Track A**: only expose advisory research guidance after those gates. WorkGraph, ActionPlane, Evidence/Verifier and Proof remain authoritative. No new secret or execution owners.
8. **Track B**: dataset generation and fine-tuning remain last, conditional on held-out gains.

## Commands

```bash
python tools/validate_archive.py
python tools/validate_registry.py
python tools/validate_publisher_sources.py
python -m unittest discover -s tests -p "test_*.py" -v
python tools/triage_source_candidates.py path/to/scout_candidates.json
python tools/curation_readiness.py --case-id CASE-000075
python tools/curation_readiness.py --case-id CASE-000076
# RDL_BLIND_KEY must be an operator-held string >=16 characters, not committed:
python tools/build_predecision_candidates.py
# Expected: zero candidate tasks, since no eligible CTX has been independently reviewed.
```

**Definition of this increment:** new source-grounded cases, negative example, unreviewed hypothesis and question data, auditable candidate-source triage, readiness tool and tested **fail-closed** evaluation export. **Not:** completion of the research factory, independent empirical validation, usable training samples, proven question-family convergence or live researcher intelligence.
