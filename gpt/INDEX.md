# RDL — GPT independent research archive

This workspace contains ChatGPT-authored **source-grounded, provisional** research observations and reconstructions, separate from `grok/`.

## Latest scientific status — 2026-10-16

- **109/109 source IDs covered by at least a bounded review** and source provenance/status record; this is *not* 109 completed historical reconstructions.
- **95** original article/publication pages reviewed to varying, often shallow or section-based depth.
- **13** publisher-authorized alternative source pages or original PDFs recovered after initial access obstacles, also with bounded review.
- **1** publisher PDF identified with only an indexed summary (`SRC-000068`); original research body not audited.
- **27** provisionally structured X→Y transition records in two JSONL files (7 for Chrome SRC001-002; 20 selected deep transitions for 7 other investigations). Other reports contain additional **unstructured** candidate questions and transitions.
- **0** curator-approved complete reconstructions; **0** eligible fine-tuning examples with historical predecision ground truth; no verified rights.
- Several source pages are method papers, advisories or secondary forensic studies and intrinsically lack a complete investigator decision diary. `UNKNOWN` is often the scientific result.

The original frozen registry was **`066b37c840576427ecdb54cb4541d710b3100ba6`**. Branch `main` now includes these independent research additions, but the original official RDL registry and engines are not modified.

## Coverage and limitations

- [109-source review status JSON](SOURCE_COVERAGE_109_2026-10-16.json) — source-by-source review tier and unfilled validation gates.
- [Original independent pass 1](analysis/RDL_INDEPENDENT_109_SOURCE_ANALYSIS_PASS1.md) — historical 36 content observations / 73 metadata status **as of pass 1**, superseded only for coverage tracking by new reports; don't reinterpret it as deep work.
- [109-source triage CSV (original pass)](analysis/RDL_109_INDEPENDENT_RESEARCH_TRIAGE.csv) and [source treatment map](analysis/RDL_109_Source_Treatment_Map.md) — preliminary historic mapping, retained unaltered for auditability.
- [Recovered first-party original sources](cases/RDL_RECOVERED_PRIMARY_SOURCES_ADDENDUM.md) — 032, 044, 045, 062–072; source links and bounded research questions; preserves original source access errors.

## Independent source-specific analyses

- [001–002: XBOW Chrome dual publications](cases/XBOW_SRC_000001_000002_INDEPENDENT_ANALYSIS.md) — original narrative, parallel staged work, retrospective causal ambiguity.
- [003–010: XBOW investigations](cases/XBOW_SRC_000003_000010_INDEPENDENT_ANALYSIS.md).
- [011–023: XBOW investigations](cases/XBOW_SRC_000011_000023_INDEPENDENT_ANALYSIS.md).
- [024–043: PortSwigger, Project Zero, XBOW studies and source genres](cases/RDL_SRC_000024_000043_PRIMARY_SOURCE_PASS.md).
- [044–072: Assetnote/Searchlight and Pentera](cases/RDL_SRC_000044_000072_SOURCE_AUDIT.md) — explicitly mixed access depth.
- [073–109: diverse primary reports, reverse engineering, failure audits and methodology](cases/RDL_SRC_000073_000109_SOURCE_AUDIT.md).
- [Selected detailed decisions (7 cases)](cases/RDL_TARGETED_DEEP_X_TO_Y_AUDIT.md) — with [20 candidate X→Y JSONL records](cases/RDL_TARGETED_DEEP_X_TO_Y_CANDIDATES.jsonl).
- [Chrome 7 candidate X→Y JSONL records](cases/XBOW_SRC_000001_000002_TRANSITIONS_CANDIDATE.jsonl).
- [Independent Fail2ban reconstruction](cases/RDL_Fail2ban_Assistant_Independent_Sealed.md) — provisional, sealed authorship does not mean truth approval.
- [Three randomly selected cases for architecture stress test](analysis/RDL_Three_Random_Cases_Architecture_Stress_Test.md).

## Review and future comparison

- [Blind comparison methodology](methodology/RDL_COMPARISON_PROTOCOL.md).
- [Blank comparison worksheet](methodology/RDL_BLIND_COMPARISON_WORKSHEET.csv).

## Caution: evidence and model training

Published first-person retrospectives are **not automatically contemporaneous traces**. Storytelling order, exploit dependencies, study design and historical motivational causes must remain separate. False-positive analysis, blocked prerequisites, failed tests, negative results and deliberate stops cannot be conflated.

Nothing in this directory is presently training-ready. No train/validation split, immutable source capture, rights approval, independent human curation, blind next-step evaluation, source-claim semantic check or original experiment verification has been completed.

`grok/` is held separate and should not read `gpt/` while producing independent results. This directory was built without consulting Grok's GitHub files in this work round.
