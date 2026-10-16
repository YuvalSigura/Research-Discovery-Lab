# RDL — Blind Two-Analyst Comparison and Adjudication

## Status
**Not executed.** Grok's independent report has not yet been supplied; no comparisons, wins, disagreements, inter-rater agreement, independent curation or truth approvals have been computed.

The two analyst reports must be frozen with hashes before cross-viewing. Our current ChatGPT report is PASS 1 and is **not complete**: 109 registry items triaged, 36 provisional content notes, 73 awaiting detailed investigation. This baseline must not be substituted for 109 fully read research cases.

## Workflow
1. Grok independently uses only the canonical 109-source registry and original publisher links from `RDL_GROK_BLIND_ANALYSIS_PROMPT.md`; explicitly forbid access to ChatGPT's CSV, Markdown report, sidecar pack and prior comparison.
2. Freeze Grok JSONL, hash and runtime/model/version/date. Confirm exactly 109 unique IDs; record failed URLs and any cases missing detailed original-source reading.
3. Compare **data coverage first**: did both read the original publisher article? Which sources are only metadata? Don't award a model 'accuracy' points for ungrounded plausible guessing.
4. Normalize candidate units by `(source_id, investigator/run identity, hypothesis or question, experiment, result, decision)`; avoid matching claims solely by word similarity.
5. Evaluate every claimed causal relation and negative result against source passages/artifact records. Mark `SUPPORTED_BOUNDED`, `SUPPORTED_AUTHOR_RETROSPECTIVE`, `INFERENCE_ONLY`, `CONTRADICTED`, `UNKNOWN`, or `ACCESS_BLOCKED`.
6. A separate human curator, blinded to model identities where practical, examines disagreements and plausible matching claims alike. Agreement between models is **not** independent factual corroboration.
7. Report omissions separately from contradictions, and track evidence-timestamp hindsight leakage, competing motives, experiment scope, actor attribution, original finder vs independent reproducer, and branch/parallel-run conflation.
8. Export accepted, partially accepted and unresolved claims to a **candidate-only** dataset. Never update RDL canonical EVT/REL/CTX or HOMELAB model/training truth without later explicit, independently documented approval.

## Suggested comparison columns
- `source_id`, `research_lineage_id` (unknown allowed), `claim_id_a`, `claim_id_b`, `claim_type`, `original_source_locator`, `source_version`
- `a_claim`, `b_claim`, `a_attribution`, `b_attribution`, `a_evidence_refs`, `b_evidence_refs`, `known_at_evidence`
- `relationship_type`, `causal_basis_a`, `causal_basis_b`, `competing_explanations`, `test_scope`, `negative_semantics`
- `match_type`: EXACT_MEANING / COMPATIBLE / PARTIAL / CONTRADICTORY / A_ONLY / B_ONLY / UNCOMPARABLE
- `source_adjudication`: SUPPORTED_BOUNDED / AUTHOR_ACCOUNT_ONLY / INFERRED / CONTRADICTED / UNKNOWN / NOT_REVIEWED
- `reviewer_id`, `reviewer_independent`, `reviewer_source_check_notes`, `adjudicated_at`, `review_status`

## Comparison metrics, when source-grounded adjudication exists
- Verified/retrospective-only claim precision (stratified; don't treat author account as full historical proof).
- Recall against independently adjudicated **observable record only**; never score hidden private thoughts as missing if unrecorded.
- False causal promotion rate; false refutation rate; unsupported historical timeline assertion rate.
- Missing-actor/lineage attribution rate; duplicate-case/event rate.
- Disagreement rate; abstention/unknown correctness; editorial-order-as-chronology mistakes.
- Source coverage rate (full-text vs partial vs metadata-only) by publication type.

## Non-inferences
The existence of a paper, a matching heading, a source URL or a plausible technical story does not prove actual research chronology. A log timestamp is not automatically the researcher's first-known-at time. A publisher's retrospective claimed motive remains an author account until independent contemporaneous evidence warrants more. An absent later-stage message is not evidence that a later stage did not exist. An unavailable article is not a negative result.

## Important failure cases to adjudicate
- `CASE-000010`: search-result title mismatch vs real XBOW geolocation SQLi article on the same URL; page identity/revision check.
- `CASE-000044`, `CASE-000045`, `CASE-000047`: Assetnote links migrated, one old link redirected to generic acquisition page; canonical Searchlight Cyber research URL recovery required.
- `CASE-000032`: original Blogspot link initially inaccessible; alternative Project Zero publication found.
- `CASE-000001` / `CASE-000002`: overlapping reports of same Chrome research lineage.
- `CASE-000011`: parallel agent trajectories.
- `CASE-000022`: initial unproductive stack-overflow attempt vs successful separate HOCON file-read objective.
- `CASE-000073`: six-week topic failure, tools reused later; not a vulnerability research log.
- `CASE-000076`: evidence that a sanitizer alerted is not proof of an exploit.
- `CASE-000078`: failed first malformed input and retest; not universal refutation.
- `CASE-000092`: forensic analyst and original exploit author differ.
- `CASE-000095`: existing bug missed by fuzzers despite apparent coverage.
- `CASE-000104`: research objective changed; technical bypass was not disproven.
- `CASE-000107`: 7,000+ conversion candidates narrowing to 20; not 7,000 confirmed vulnerabilities.