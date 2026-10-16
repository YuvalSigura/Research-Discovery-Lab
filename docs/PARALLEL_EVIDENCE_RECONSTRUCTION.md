# Parallel Evidence-First Reconstruction Lab — experimental v1

**Isolation:** `research_engine` (the existing registry-based retrieval and reconstruction engine) remains unchanged. This new `research_reconstruction_lab` is a separate, **non-authoritative** checker of *candidate* research narratives. It does not import the original engine, write `registry/`, or promote research outcomes into HOMELAB.

## Why a second engine?

Fail2ban CASE-000078 illustrates an epistemic trap: the author's published report describes a sequence of SQL and command-injection research, but section order does not prove one result motivated the next. By contrast, an author-reported observation about an integer parsing error leading to a retest is better evidence of a reported cause, **not proof of contemporaneous mental state**. A failed payload does not refute the entire hypothesis. Missing evidence can cause a pivot without proving that any vulnerability was absent.

## Workflow

1. Collect original source references, exact passage/commit/log locators and legal reuse rights, without assuming retrospective prose is a time-accurate action log.
2. Produce multiple candidate claims and links *outside the canonical registry*. Use the same source packet across competing human or model interpretations and preserve rejected alternatives.
3. Run the deterministic checker to flag absent support, missing discriminators, negative-to-refutation leaps, unsupported causality and uncertain decision motives.
4. Re-check each candidate statement and locator against the actual source. Independent adjudicators challenge source paraphrases and alternative motives. **The checker alone cannot verify semantics, independent causality or source fidelity.**
5. Only after review, a separately approved future import process can map findings into RDL `EVT`, `REL`, `CTX`. **No such importer is included.**

## Run in PowerShell

```powershell
python -m research_reconstruction_lab examples/fail2ban_candidate_pack.json
python -m unittest discover -s tests -p "test_parallel_reconstruction_lab.py" -v
python -m research_engine reconstruct CASE-000078 --view historical
```

The last command must still return `metadata_only`; it demonstrates that the new experimental engine cannot contaminate historical truth. The example is a **provisional interpretation based on a published article**, not independently reviewed science and not copyrighted full text.

## Input contract

A JSON pack has `schema: rdl.reconstruction_candidate.v1`, `case_id`, `sources`, `evidence`, `claims`, and `links`. Every evidence entry has an ID, first-party source ref, locator, paraphrase and type: `retrospective_author`, `contemporaneous_artifact`, `source_code`, `independent_source`, or `analyst_note`. Evidence may have timezone-aware `occurred_at` and `known_at` **only if actually established**; the checker always withholds approval of historical knowledge.

Claims distinguish author reports, artifacts, analyst inference and unknown attribution. `result` entries distinguish `negative_test`, `no_evidence_observed`, `inconclusive` and `not_run`. A test with no evidence or an inconclusive outcome cannot itself refute a hypothesis. A narrowly scoped refutation needs an explicit discriminator and still requires human verification of test validity.

Links preserve `followed_by`, `motivated`, `revised_after`, `tested_by` and `stopped_because` separately. `author_explicit` requires an author-account source anchor; it remains labeled `author_reported_unverified_causality`. `chronology_only` never proves motivation. Competing explanations remain visible instead of being silently merged.

## Not implemented in v1

- Automated webpage ingestion, full-text extraction, source-artifact hashing and semantic entailment checking.
- Independent alternative generation with LLMs, automatic historical-motive discovery, or model-based source adjudication.
- Permission to copy source texts, promote `EVT/REL/CTX`, declare truth or train on retrospective reconstructions.

Next gate: adversarial testing on multiple independently sourced investigations and deliberately misleading narratives before adding acquisition and candidate-generation components. An empty or unresolved analysis is a valid scientific result.
