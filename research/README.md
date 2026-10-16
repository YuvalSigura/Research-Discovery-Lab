# Research Archive — Phase 1

This is a **source catalogue**, not a completed full-text RAW archive. 31 publisher articles have been registered with stable case IDs. Original article bytes have **not** been downloaded into this repository; every raw manifest explicitly records that status.

## Rules

1. Preserve the original source URL, publication metadata, and stable ID.
2. Never mark source content as archived without the actual bytes, a SHA-256 digest, capture timestamp, and legal basis for retention/distribution.
3. Keep original bytes immutable; never overwrite RAW with analysis.
4. Do not commit sensitive data, live credentials, exploit payloads from private targets, or proprietary texts without permission.
5. Store subsequent analyses under `analysis/` with versioned authorship, evidence citations, and distinctions between observed facts and reconstructed reasoning.
6. Do not use future-discovery information in pre-discovery training snapshots.
7. Keep holdout research lineages isolated from training to prevent answer leakage.

## Structure

- `cases/CASE-XXXXXX/metadata.json` — stable bibliographic and provenance metadata.
- `cases/CASE-XXXXXX/raw/manifest.json` — exact status of RAW preservation.
- `index.json` — machine-readable collection index.
- `../schemas/` — JSON schemas for validation.
- `../tools/validate_archive.py` — deterministic consistency checks.

## Next phase

In Phase 2, add `analysis/` files for technical mechanism, discovery timeline, pre-discovery snapshots, hypothesis provenance, and cross-case principles. None are claimed complete now.
