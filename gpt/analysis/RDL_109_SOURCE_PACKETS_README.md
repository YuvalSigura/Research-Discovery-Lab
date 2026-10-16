# GPT Research Corpus — 109 source-by-source analyst packets

This directory is a **lossless source-note consolidation** from existing independent GPT primary-article review files, *not* 109 new completed research reconstructions, or verified full article copies. Each JSONL row preserves the source-specific notes, analyst-formulated questions, uncertainties and method observations verbatim from the already-written RDL analysis files, with a link to its precise original analysis file.

- Inventory frozen at `066b37c840576427ecdb54cb4541d710b3100ba6`.
- 109 source IDs represented exactly once; 37 include a second more granular analysis section from previous deep-review passes.
- All 109 have **training_ready=false**; no original investigator private logs or known-at snapshots approved.
- Publishers' retroactive accounts remain author reports; the notebook text is analysts' paraphrase, NOT direct source article reproduction.
- `source_analysis_note` and `deeper_analysis_note` include Markdown of prior independent analysis. Missing deeper notes means only bounded review, not that research content doesn't exist.
- Some first-attempt inaccessible URLs have later recovered first-party material recorded separately in `RDL_RECOVERED_PRIMARY_SOURCES_ADDENDUM.md`; the fields here retain the first and deep-pass historical notes rather than silently deleting the retrieval history.
- This index is **not a fine-tuning input**. Use it to locate gaps and source-specific research claims before manual source verification and lineage-based reviewer arbitration.

## Prioritized correctness checks

1. Distinguish the author's stated historical question from analyst-generated question candidates.
2. Distinguish first-party reported experiment outcome from independently verified target behavior.
3. Ensure lineage independence before cross-source pattern counting.
4. Separate expected/observed results, prerequisite blocks, measurement limitations and actual hypothesis refutation.
5. Do not train next-decision policy from retrospective X→Y without contemporary known-at cutoff artifacts.

See `gpt/cases/RDL_SRC_000026_000094_000095_000107_DEEP_PRIMARY_AUDIT.md` for new four-source discriminating follow-up.
