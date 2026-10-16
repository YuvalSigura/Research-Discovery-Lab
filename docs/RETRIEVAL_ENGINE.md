# Research Retrieval & Investigation Reconstruction Engine

**Phase:** retrieval engine v1; usable on the current 50-source archive. No model training or autonomous web capture. The archive currently contains **metadata only**, not publication RAW or documented experimental trajectories.

## Operating contract

The engine does not invent research chronology, assumptions, failed trials or causal transitions. It can retrieve them once provenance-backed records are supplied. It distinguishes:

- **Source:** catalogued publication, not necessarily captured original text.
- **Case:** investigation; current 50 CASE records are legacy placeholders, not independently reconstructed investigations.
- **Event:** single documented or explicitly labelled reconstructed research action, question, challenged assumption, direction, experiment, outcome or decision.
- **Relation:** an explicitly recorded connection; temporal proximity **never** becomes causality.
- **Passage:** short licensed excerpt or original analysis, with source ID, locator and SHA-256.
- **Context:** reviewed snapshot of what was knowable at a particular time.
- **Evidence pack:** ordered dated events plus *unplaced* events, directions, failures, questions, unanswered paths, evidence and uncertainty.

## CLI

Install dependencies and validate:

\`\`\`shell
python -m pip install -r requirements-validation.txt
python tools/validate_archive.py
python tools/validate_registry.py
python -m unittest discover -s tests -v
\`\`\`

Search existing catalogue:

\`\`\`shell
python -m research_engine search "Chrome" --kind sources --limit 10
python -m research_engine search --publisher XBOW --kind sources
python -m research_engine search "assumption" --kind events
python -m research_engine search "permission" --case-id CASE-000001
\`\`\`

Build packs or trace documented pivots:

\`\`\`shell
python -m research_engine reconstruct CASE-000001 --view historical
python -m research_engine reconstruct CASE-000001 --view all
python -m research_engine coverage CASE-000001
python -m research_engine related CASE-000001
python -m research_engine trace CASE-000001 EVT-000001
python -m research_engine reconstruct CASE-000001 --view pre_discovery --cutoff 2025-03-01T12:00:00Z
\`\`\`

The last two trajectory operations appropriately fail or yield an empty grounded pack when no documented events or reviewed snapshots exist. Save a pack using normal shell redirection. CLI JSON can be consumed by future analysis workers.

## Data contracts

See \`schemas/v2/\` and \`registry/\`. New optional fields on EVT and REL encode:

| Field | Use |
| --- | --- |
| \`origin\` | \`historical\`, \`reconstructed\`, \`counterfactual\`, \`unknown\` |
| \`timestamps.occurred_at\` | When the underlying event actually occurred |
| \`timestamps.observed_at\` | When it was observed |
| \`timestamps.recorded_at\` | When it entered the research record |
| \`timestamps.published_at\` | When documentation was published |
| \`timestamps.known_at\` | Earliest time the evidence is established as known |
| \`hindsight_review\` | Whether a curator reviewed pre-discovery eligibility |
| \`direction_status\` | Considered, planned, attempted, not tested, abandoned, blocked, failed, succeeded, inconclusive, unknown |
| \`assumption_status\` | Assumed, challenged, supported, refuted, revised, unknown |
| \`expected_outcome\` / \`actual_outcome\` | Distinguish predictions and observations |
| \`information_gained\` | What a failed or successful trial actually taught |
| \`blocking_reason\` | Why an avenue did not continue |
| \`assumption_basis\` | Why an assumption was held; basis for challenging it |
| \`evidence_anchors\` | Exact source and passage/page/line/commit locator |
| \`causal_basis\` (REL) | \`explicit_documented\`, \`reconstructed\`, \`temporal_only\`, \`counterfactual\`, \`unknown\` |
| \`known_at\` and \`hindsight_review\` (REL) | Independent pre-discovery gate for links |

New \`kind\` values include \`direction\`, \`decision\`, \`pivot\`, \`knowledge_revision\`, \`blocking_factor\`, \`external_input\`. Additional predicates include \`raised_question\`, \`pivoted_to\`, \`challenged_assumption\`, \`abandoned_because\`, \`ruled_out_by\`, \`remained_unexplored\`, and more.

**Source excerpts:** \`PAS\` passages are SHA-256 verified. \`licensed_excerpt\` is permitted only if the publisher's source record has \`license_status: permitted\`. \`original_analysis\` contains an independently authored short passage, not republished copyrighted RAW. Do not commit private/restricted material or secrets to this public repository.

## Retrieval modes and fidelity

**Search:** Deterministic lexical plus explicit metadata filtering across sources, cases, events, passages, systems and mechanisms. It is not advertised as semantic search; cannot retrieve article text while articles remain uncaptured.

**Historical reconstruction:** Includes *only* historical events with documented/verified provenance. Dated events are ordered by **occurred_at**. Events without occurrence timestamps remain in \`chronology_unknown\`; ID order does not assert chronology.

**All reconstruction:** Adds explicitly labelled reconstructed and counterfactual hypotheses as separate branches. Never presents them as historical facts.

**Pre-discovery:** Fail-closed. Requires an explicit cutoff, documented historical event, contemporaneous dated source, \`known_at\`, curator's passed hindsight review and no final outcome/principle event. No source titles, full text, findings, mechanism labels or case labels are included. Relations independently require \`known_at\`, passed hindsight review and explicit documented causality. Late or partial-dated publications are not treated as contemporaneous.

**Question tracing:** Walks only explicit directed causal edges for the selected view and reports their provenance. \`followed_by\` and simple temporal adjacency are intentionally **not** treated as demonstrated cause.

**Cross-case:** Related cases require explicit relation, shared curated mechanisms or identical source identity. No source-title similarity becomes a scientific equivalence.

## Completeness and evidence integrity

Packs report source count, RAW availability, passage count, event count, anchored events, undated events and causal-link counts. \`metadata_only\` is a legitimate result. It is **not** a score indicating a genuine research trajectory has been recovered. Missing RAW, unexplained pivots, undocumented failed attempts and missing time should be reported as unknown, not filled by a language model.

The package is read-only. It does not execute research against targets, call LLMs, infer vulnerabilities or schedule investigations. It is separate from HOMELAB's execution and truth authorities.

## Synthetic tests

The unit tests contain a fabricated research story (challenged authorization assumption, failed avenue, question-driven pivot and untested branch). These fabricated events live **only in test fixtures** and must never become corpus evidence or training examples.

## Future acquisition boundary

When the collector is implemented, it can add copyright-cleared passage records and RAW manifests. The engine indexes new registry records automatically when loaded; it never fetches external URLs or guesses missing original publications. Training remains the last project phase.
