# Phase 1 — retrieval engine status

## Delivered

- 50 preserved original research source entries, 50 source registry entities and legacy case crosswalk.
- Ten typed registries/schemas: sources, cases, systems, environments, contexts, findings, mechanisms, events, relations, passages.
- Read-only Python research engine and JSON CLI: search, reconstruct, trace, related, coverage.
- Deterministic lexical and structured-filter retrieval, provenance, passage SHA-256 and explicit license checks.
- Chronological reconstruction with unknown chronology separate; assumptions, abandoned/failed/untried directions, pivots and source-backed questions.
- Historical versus explicitly reconstructed/counterfactual views; fail-closed pre-discovery snapshots and dedicated trajectory gap audit.
- CI schema validation, fault-injection tests and offline synthetic branching-investigation tests.

## Not accomplished / intentionally deferred

- The 50 real publications have **no original RAW full-text captures**. Search currently indexes catalogue metadata, not missing article content.
- The existing CASE IDs are source-catalogue placeholders, **not fully reconstructed investigations**; evidence-backed event extraction and curatorial review still need actual sources.
- No live acquisition or web crawling as part of this read-only engine.
- No automatic historical assertion that was not documented; no LLM decision authority.
- No training; fine-tuning is the last project phase.

See \`docs/RETRIEVAL_ENGINE.md\`.
