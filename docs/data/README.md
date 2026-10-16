# Review-only data — NOT an ingestion or training directory

This folder contains **provisional analyst-authored research-question comparisons**.

- `RDL_CONSOLIDATED_CANDIDATE_QUESTIONS.v0.json` is **not** the canonical `QPT` or `QMP` registry and may not be globbed into registry ingestion, retrieval-as-truth, approved curation or model training by default.
- The document is structurally validated by `tools/validate_registry.py` solely to detect errors (e.g., mismatch with source-specific QMP relationships, unauthorized status promotion).
- Validation does **not** change `PROVISIONAL`, `UNREVIEWED` or `TRAINING_BLOCKED`. Any explicit future promotion requires independent adjudication via the appropriate canonical registry, rights verification and independent evaluation.
- Any future tool that starts reading `docs/data/*.json` for nonvalidation purposes must obtain explicit governance review and must not silently treat `CQ-*` as canonical `QPT-*` or validated historical predecision records.

The current record contains **14 provisional scientific-question families plus one cross-cutting evaluation lens**. It has no approved training samples.
