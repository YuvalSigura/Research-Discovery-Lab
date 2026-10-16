<div align="center">

# 🔬 Research Discovery Lab

### Understand the questions behind discoveries — before training a model to ask them.

**An evidence-grounded research archive, investigation reconstruction engine and question-first research intelligence project.**

[![Status: Active research infrastructure](https://img.shields.io/badge/status-active%20research%20infrastructure-4C78A8)](#verified-project-status)
[![CI](https://github.com/YuvalSigura/Research-Discovery-Lab/actions/workflows/archive-validation.yml/badge.svg)](https://github.com/YuvalSigura/Research-Discovery-Lab/actions/workflows/archive-validation.yml)

[Current state](#verified-project-status) · [Thesis](#research-thesis) · [Research engine](#implemented-retrieval-and-investigation-engine) · [Question-first analysis](#question-first-analysis-what-was-the-investigator-trying-to-find-out) · [Roadmap](#remaining-roadmap--training-is-last) · [Data integrity](#scientific-integrity-and-source-rights)

</div>

---

> **The central question is not only how a zero-day was found. It is what question made the investigator look in that direction — and whether seemingly original research moves are different ways of investigating the same deeper question.**
>
> **Zero-day ≠ original thinking. Routine work ≠ low-value research. Negative results ≠ failed science.**

## Research thesis

A discovery may follow a checklist, variant analysis, anomaly investigation, an unexpected failure, or the deliberate challenge of an architectural assumption. Its significance and its reasoning originality are **separate properties**.

Research Discovery Lab (RDL) aims to reconstruct **the process that produced a question**, not merely the final exploitation steps. Across many independent investigations, it asks whether researchers repeatedly converge on a smaller — but not predetermined — collection of fundamental, discriminating research questions.

These may concern identity, authority, timing, state changes, parser disagreement, isolation, trust boundaries or interactions among intended product features. They are **candidate patterns**, not a fixed list that every investigation must fit.

This is a separate project from the HOMELAB authorized security-research execution system. RDL models evidence, decisions, questions and research knowledge; it does **not** introduce a new authority for target execution or verified findings.

## Verified project status

The following figures reflect the current repository baseline as inspected after the last successful CI run; they are not claims about deep coverage of every publication.

| Item | Status |
| --- | --- |
| Catalogued publications | **109 source records** (77 baseline + 32 catalogue-only candidates; see [intake ledger](docs/SOURCE_INTAKE_2026-10-16.md)) |
| CASE records | **109**, mostly source-compatible catalogue placeholders |
| Deep case example | **ShadowPanel**, **James Kettle topic selection**, **watchTowr .MOBI**, **ServiceNow** and **an OpenVAS false-positive account**, and **GitHub Security Lab taskflow methodology**, partially reconstructed; **XBOW Chrome** has five initial process events |
| ShadowPanel trajectory | **18 source-anchored events; 19 provenance-tagged relations** (ShadowPanel alone); **90 events and 79 relations** across current archive |
| Publisher-discovery seeds | **9 configured research publishers**, in `sources/publishers/` |
| Typed archive, schemas, integrity checks | Implemented |
| Read-only retrieval, chronology, causal question tracing | Implemented |
| Mindset taxonomy, question-to-move model and open-world umbrella-question analysis | Implemented **as infrastructure** |
| Mindset / question-pattern / cross-case mappings | **6 unreviewed MND**, **2 proposed QPT**, **3 proposed QMP**; **0 reviewed** |
| Original article RAW text and licensed passages | **Not archived** for the catalogue |
| Automated acquisition, document processing and historical extraction | **Not implemented end to end** |
| Dataset creation, blind evaluation, fine-tuning | **Fail-closed predecision candidate exporter and offline descriptive A/B scorer exist**, but **0 approved CTX**, **0 qualified benchmark tasks**, and **no actual model comparison**; training is last |

**New source catalogue intake:** 32 unreviewed first-party leads, without new event trajectories or validated blind test tasks. [Intake guardrails](docs/SOURCE_INTAKE_2026-10-16.md).

**Previously verified main baseline:** [consolidated main CI PASS](https://github.com/YuvalSigura/Research-Discovery-Lab/actions/runs/38860482526), commit `2e66bca`; the current increment requires its own GitHub Actions run. See [Phase-3 research review and evaluation](docs/PHASE3_INDEPENDENT_CURATION_AND_EVALUATION.md).

The research trajectory records are **partial reconstructions from authors' retrospective public accounts**, not independently repeated exploit experiments. Where event times are unavailable, the engine preserves uncertainty instead of manufacturing dates or causal ordering. See [first-mission source review](docs/FIRST_MISSION_SOURCE_REVIEW.md), [Pentera import notes](docs/PENTERA_IMPORT.md), and [phase status](docs/PHASE1_STATUS.md).

## Implemented retrieval and investigation engine

The Python `research_engine` package reads the typed registries and produces evidence-aware JSON. It provides:

- **Source and record retrieval:** deterministic lexical search with metadata filters and source references; no unsupported claims of semantic indexing or uncaptured full-text search.
- **Scout intake triage:** `tools/triage_source_candidates.py` deduplicates canonical first-party leads, flags unverifiable sources and keeps rights unreviewed; it deliberately creates no authoritative archive records.
- **Independent review preparation:** `tools/build_curator_queue.py` produces source-linked human-review worksheets with inferred motives and uncertain causal edges flagged; no automatic promotion.
- **Offline descriptive paired-arm checks:** `tools/score_paired_trials.py` validates three matched A/B/control arms and blinded human scoring; it does not run models or claim transfer.
- **Investigation reconstruction:** documented events in known time order; unknown-time events kept in a separate bucket.
- **Trajectory accounting:** assumptions, hypotheses, considered/abandoned/untried directions, experiments, negative and inconclusive results, pivots, and questions.
- **Provenance-aware tracing:** explicit transitions between questions, evidence and research decisions; chronology alone is not treated as causality.
- **Coverage/gap reports:** missing triggering evidence, unexplained pivots, unattested motivations and unresolved question directions.
- **Fail-closed pre-discovery views:** do not reveal final findings, post-cutoff evidence, or inferred historical knowledge as if it existed at the time.
- **Rights checks:** source-backed passage hashes and explicit permission requirements for republished excerpts.
- **Offline tests and GitHub Actions:** schema, relation, archival and leakage checks, plus **synthetic-only** negative/control research cases.

### Run locally

Requires Python 3.12 or a compatible installation:

```bash
python -m pip install -r requirements-validation.txt
python tools/validate_archive.py
python tools/validate_registry.py
python tools/validate_publisher_sources.py
python -m unittest discover -s tests -p "test_*.py" -v

# Browse existing catalogue
python -m research_engine search "CyberPanel"
python -m research_engine search "Chrome" --kind sources

# Existing partial ShadowPanel reconstruction
# First-mission case studies: method choice, infrastructure assumptions, and agent pivots
python -m research_engine reconstruct CASE-000073 --view historical
python -m research_engine reconstruct CASE-000074 --view historical
python -m research_engine reconstruct CASE-000002 --view historical

python -m research_engine reconstruct CASE-000055 --view historical
python -m research_engine coverage CASE-000055

# Grounded questions, mindset links and question abstraction
python -m research_engine questions CASE-000055
python -m research_engine question-convergence --min-cases 2
python tools/triage_source_candidates.py path/to/scout_candidates.json
python tools/curation_readiness.py --case-id CASE-000075
python tools/build_curator_queue.py --case-id CASE-000077
# After external, preregistered scored trial data is available:
# python tools/score_paired_trials.py /path/to/blind_human_scores.json
# Export requires an operator-held RDL_BLIND_KEY; with 0 approved CTX exports 0 tasks:
python tools/build_predecision_candidates.py
python -m research_engine compare-questions CASE-000055 CASE-000001

# Strict time-sliced view; unknown or late evidence is withheld
python -m research_engine reconstruct CASE-000055 --view pre_discovery --cutoff 2026-01-01T00:00:00Z
```

**Expected behavior:** query results can be sparse or empty. In particular, question-family convergence must report no reviewed matches: existing real QMP records are **proposed**, not curator-reviewed. The blind candidate builder must export zero tasks while no CTX records are approved. An empty answer is preferable to a fabricated research story.

API and record semantics: [retrieval documentation](docs/RETRIEVAL_ENGINE.md).

## Question-first analysis: what was the investigator trying to find out?

The unit of comparison is the **research question**, not the exploit name or the researcher’s personality. Our evidence graph captures:

```text
Known context + assumptions + observations
                 ↓
         Motivating research question
                 ↓
      Research decision / direction
                 ↓
      Actual test / evidence / result
                 ↓
       New question, pivot, or stop
                 │
                 └── Mindset observation tied to *this move*
                                      │
                                      └── Novelty relative to prior work

Specific question in case A ──┐
Specific question in case B ──┼── Reviewed umbrella-question hypothesis
Specific question in case C ──┘         (QPT; open-world, not forced)
```

The system distinguishes five independent assessments:

1. **What question was asked, why, and what evidence was available when it arose?**
2. **What research move was actually performed?** Checklist, variant analysis, anomaly follow-up, hypothesis test, assumption challenge, recombination, failure-driven pivot, etc.
3. **How original was the move relative to the question and prior art?** Conventional procedure, contextual adaptation, novel recombination, or *candidate* originality.
4. **Does it instantiate an underlying question shared with other cases?** Require a reviewed, versioned mapping and inclusion/exclusion criteria; analogy alone is not identity.
5. **What was the outcome?** A claimed zero-day, independently corroborated zero-day, no zero-day, a disputed outcome, or unknown — independently assessed, never used as a shortcut for originality.

A single investigator may use multiple strategies in one investigation. **Mindset here is a label for evidenced actions and decisions, not a psychological profile of a person.**

### Open-world research-question families

The ontology includes **candidate seed questions**, but the engine must support genuinely new families and preserve unmatched questions. Similar tools, CVEs, attack chains and titles are not sufficient grounds to merge investigations. Convergence is counted only when the underlying uncertainty is substantially the same and the mapping is reviewed; partial overlap and analogies remain distinct.

The model also preserves differences between the researcher’s *explicit stated reasoning* and an analyst’s *retrospective inference*. The latter must not become historical truth.

Full methodology and data contracts: [question-first research intelligence](docs/QUESTION_FIRST_RESEARCH.md).

## Research sources and acquisition policy

RDL prioritizes first-party security research that documents **how an investigator arrived at a discovery**, especially failed attempts, surprising observations, competing hypotheses, changed assumptions, abandoned directions and evidence-driven pivots. Relevant sources include vulnerability research laboratories, offensive-security validation vendors, academic work, bug-bounty disclosures and original public investigator threads on X.

Starting publishers include Pentera Labs and the curated watchlist in [competitor research sources](docs/COMPETITOR_RESEARCH_SOURCES.md). The publisher seeds are **discovery inputs only**, not automatically archived source texts or endorsed original investigations.

For X/Twitter discovery, use [the Grok research-hunting prompt](docs/GROK_X_RESEARCH_DISCOVERY.md) to collect original thread permalinks, author/date, linked primary publications and a first-pass *evidence-backed* trajectory assessment. Each source must pass ingestion and licensing gates before entering the scientific corpus.

Public access is **not** permission to mirror articles, X posts, media or PDFs. Capture only permitted original bytes, maintain source hashes/capture dates, and preserve provenance. Keep independent original analysis separate from publisher text.

## Data architecture

```text
sources/             Curated publisher discovery seeds
research/            Legacy catalogue and RAW manifests
registry/            Typed SRC, CASE, SYS, ENV, CTX, EVT, REL, PAS,
                     FND, MEC, MND, QPT and QMP registries
schemas/v2/          Schema validation for each registry
ontology/            Event, relation, mindset and question vocabularies
research_engine/     Retrieval and question-analysis read-only implementation
tools/               Archive, registry and publisher-config validators
tests/               Offline regression, corruption and synthetic-case tests
docs/                Policy, intake, reconstruction and research methodologies
```

The core trajectory is a branching, evidence-backed graph rather than a linear hindsight story. Four distinct temporal concepts may matter: when an event occurred, when it was observed, when it was recorded, and when it became available or was published.

All original/historical vs analyst-reconstructed vs counterfactual vs unknown claims remain explicitly distinct. **Not tried ≠ failed. Failed test ≠ disproven hypothesis. Disclosed vulnerability ≠ proven zero-day.**

## Remaining roadmap — training is last

The existing retrieval/question-analysis foundation is **not** the finished research factory. Phase 2 added publisher-sourced cases, a negative investigation with methodological caveats, and unreviewed MND/QPT/QMP hypotheses. The subsequent increment adds a GitHub Security Lab methodology study, an explicit independent curation queue and a strictly descriptive paired-trial scorer. **No question-family convergence, human-curated blind context or model-performance gain has been demonstrated.**

| Order | Stage | Exit criterion |
| --- | --- | --- |
| **1** | **Research acquisition:** canonical URL discovery, deduplication, source monitoring and rights-aware capture | Public origin, version, permission and provenance are recorded |
| **2** | **Document processing:** structure-aware extraction from permitted HTML, PDF, code, figures and source references | Reconstructable exact citations, anchors and hashes |
| **3** | **Investigation reconstruction:** extract events, hypotheses, questions, failed/untried paths, decision reasons and alternative explanations | Deep reviewed packs, first across 10–20 diverse independent investigations |
| **4** | **Evidence verification and adjudication:** verify source anchors, contradictions, chronology and causal support | Claim-level citation and negative/uncertainty coverage gates |
| **5** | **Cross-case question intelligence:** review MND/QPT/QMP mappings and test convergence across different researcher groups | Reliable grouping of equivalent questions, with difficult negative cases and unclassified questions retained |
| **6** | **Evaluation factory:** blind holdouts split by researcher, publisher, research lineage, mechanism and time; matched-budget untuned baselines | Measurable value without hindsight leakage or survivorship claims |
| **7 — LAST** | **Training / fine-tuning experiments:** only after the corpus, reconstruction, review and blind evaluation machinery are ready | Demonstrated improvement in question selection on unseen research |

Scaling toward thousands of articles is a **long-term target**, not a current corpus size. Deep analysis quality and measurable retrieval coverage take priority over raw count.

The eventual research-question CEO and bounded workers are **future model/arena experiments**, not deployed capabilities of the current read-only archive. In any future HOMELAB integration, WorkGraph owns execution state, ActionPlane owns authorization and target execution, and deterministic Evidence/Verifier/Proof controls scientific truth. Models propose; they do not self-authorize actions or self-certify vulnerability claims.

## Scientific integrity and source rights

- **Evidence before belief:** each substantive claim needs a source/locator, uncertainty status and an auditable review path.
- **No invented trajectories:** inferred motives, failed attempts and untried directions remain explicitly hypothetical unless documented.
- **Question before method:** distinguish the underlying research question from a checklist or technique used to explore it.
- **Originality before outcome bias:** routine work can discover zero-days; original reasoning can end with a useful negative result.
- **No forced umbrella classes:** new questions may not fit old categories; contested mappings remain contested.
- **Pre-discovery integrity:** withhold information that could not have been known at the investigated decision point.
- **No spurious causal claim:** the coexistence of a mindset and a zero-day does not prove the mindset caused the discovery.
- **Responsible sourcing:** preserve canonical URLs, capture timestamps, authors and appropriate legal permissions.
- **Authorized environments only:** no autonomous target exploitation, external execution authority or unsanctioned investigation is introduced by this repository.

## Contributing

Contributions are especially useful in original research source discovery, provenance-preserving parsers, careful reconstruction of **why a question emerged**, independent reviews of competing abstractions, negative-result examples and robust evaluation design.

For proposed source/case updates, provide original URLs, precise source anchors, an originality assessment, and which material is fact, inference, or currently unknown.

---

<div align="center">

**Better questions. Better investigations. Research intelligence grounded in evidence.**

*Research Discovery Lab · Separate companion to HOMELAB*

</div>
