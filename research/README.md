# Research Archive — Phase 1

This is a **source catalogue**, not a completed full-text RAW archive. **50** publisher publications have been registered with stable case IDs. Original article bytes have **not** been downloaded into this repository; every raw manifest explicitly records that status.

## Rules

1. Preserve original source URLs, attribution, stable IDs, and source versions.
2. Never mark source content as archived without actual bytes, SHA-256 digest, capture timestamp, and permission review.
3. Keep original bytes immutable; never overwrite RAW with analysis.
4. Never commit credentials, sensitive private-target evidence, or proprietary text without permission.
5. Keep future analysis versioned and separate, with provenance and a clear observed-vs-reconstructed distinction.
6. Prevent hindsight leakage: pre-discovery snapshots must not reveal later discoveries.
7. Split train/test by research lineage and family rather than random record.

## Structure

- `cases/CASE-XXXXXX/metadata.json` — source metadata.
- `cases/CASE-XXXXXX/raw/manifest.json` — precise RAW preservation status.
- `index.json` — searchable machine-readable index.
- `../schemas/` — metadata schemas.
- `../tools/validate_archive.py` — archive consistency validator.

## Next acquisition work

Expand verified source inventory, confirm permissions and capture source bytes into appropriate storage, record hashes and provenance, and check link health. Technical analysis and discovery reconstruction belong to **Phase 2**, not this archive phase.
