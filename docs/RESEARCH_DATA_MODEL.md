# Research Data Model v2 — Phase 1

## Core design

**Publication/source != investigation/case != finding != mechanism.**

A single source can document multiple investigations; one investigation can have several sources, systems, environments, findings, and mechanisms. Cases should not be physically grouped by technology because investigations span domains.

## Typed entities

| Registry | Entity | Purpose |
|---|---|---|
| sources | SRC | Immutable source identity, provenance and lawful capture |
| systems | SYS | Product, component, technology and architecture |
| environments | ENV | Version, deployment, configuration and dependencies |
| cases | CASE | Research investigation and its relationships |
| contexts | CTX | Pre-discovery knowledge and limitations |
| findings | FND | Outcome, applicability and negative conditions |
| mechanisms | MEC | Cross-domain mechanism and generalizable principle |
| events | EVT | Observations, assumptions, questions, experiments and evidence |
| relations | REL | Provenance-bearing typed cross-entity edges |

## Scientific integrity

1. Record source-backed facts separately from reconstructed hypotheses and unknowns.
2. Do not expose post-discovery outcomes in pre-discovery training snapshots.
3. Keep documented negative and inconclusive results.
4. Store system/version and deployment as **context**, not as substitutes for a mechanism.
5. Support cross-domain comparison through mechanisms and typed event graphs.
6. Version schema and ontology; do not silently change interpretation of old cases.
7. Keep private or copyrighted RAW out of public GitHub without permission.

## Legacy compatibility

All existing 50 source catalogue records remain untouched. The v2 case registry contains placeholder records with matching CASE IDs and a crosswalk. Their investigation boundaries and system details require later evidence-backed review.

## Phase boundary

This commit implements **Phase 1 structural contracts**, not Phase 2 research analysis, automated extraction, or model training.
