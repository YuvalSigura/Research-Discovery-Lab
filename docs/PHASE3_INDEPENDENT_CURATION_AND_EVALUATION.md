# Phase 3 — Independent research curation and blind-evaluation preparation

**Prepared 2026-10-16 · Initial source analyst review only.** This increment is NOT a completed deep corpus, not a second independent curator review, not a real blind benchmark, and not evidence that RDL improves HOMELAB.

## Actual new research input: CASE-000077

Primary authored source: [Man Yue Mo and Peter Stöckli, GitHub Security Lab, “How to scan for vulnerabilities with GitHub Security Lab's open source AI-powered framework”](https://github.blog/security/how-to-scan-for-vulnerabilities-with-github-security-labs-open-source-ai-powered-framework/), published **2026-03-06** (updated 2026-03-10). The first-party page was inspected on 2026-10-16. Source rights remain unreviewed; **no article text, screenshots or proprietary media are mirrored**.

This is **one published methodology study** and must not be counted as individual full investigation trajectories. It reports a multi-stage process: threat model by application/component and entry point; brainstorm likely vulnerability ideas; audit each proposed issue with evidence and intended-usage boundaries; manually inspect the surviving candidates. The authors describe a possible conservatism tradeoff and retrospective observations of false positives caused by overlooked mitigations or layered authentication.

Source-backed quantitative report from its **“What we learned”** section: more than forty repositories were examined; 1,003 issue proposals were generated; the audit phase flagged 139; deduplication left 91; authors manually rejected **20 as unreproduced**, **52 as low severity** and retained **19** for reporting. These are self-reported aggregate numbers, not RDL replicas, not independently verified individual cases, not a controlled comparison against HOMELAB, and not a proof that the 20 failed to exist. A low-impact behavior is not automatically a false positive; an unreproduced claim is not automatically a disproven hypothesis.

New IDs: `SRC-000077 / CASE-000077`, twelve `EVT-000079..090` narrative events, eleven `REL-000069..079` relations, two `MND-000005..006` observations. Both MNDs are unreviewed. `EVT-000080` is an **analyst-formulated** question, not a quote from a historical transcript; `EVT-000084` represents a research concern explicitly expressed by the authors, but its contemporaneous timestamp remains unknown. `MND-000006` is specifically an analyst inference. The source cannot provide a pre-discovery knowledge snapshot.

### Different research questions, not forced common labels

The OpenVAS false-positive account (`CASE-000076`) examines whether an apparent tool warning actually arose from the allegedly unsafe code or from the measurement procedure. The GitHub report (`CASE-000077`) examines whether suggested source-level issues exceed intended privilege boundaries and survive confirmation. These can be **compared** as kinds of research validation, but they are not shown to instantiate an identical falsifiable question. This increment creates **no** new `QPT/QMP` mapping or curator-approved equivalence.

## Tool: independent curator queue

Run:

```bash
python tools/build_curator_queue.py --case-id CASE-000077
python tools/build_curator_queue.py --case-id CASE-000076
python tools/build_curator_queue.py  # all reconstructed cases
```

It emits claim/event/edge worksheets with publisher URLs and source locators, inferred-vs-documentary origin, unknown historical cutoffs, possible invalid-negative interpretations, question attribution checks and causal-edge challenges.

**What it cannot do:** verify exact source paragraphs, know original private motives, judge external impact, approve rights or impersonate a second human reviewer. Every emitted `curator_decision` is `pending`. A second independent curator must explicitly confirm source statements, challenge alternate explanations and register disagreements before any record is promoted. Section-only locators are not immutable evidence; where possible record stable source revision or a permissible source fingerprint.

### Deep-case completion gate (target: first 10–20 diverse cases)

For EACH deep case:

1. Confirm canonical original source and research lineage. One article or multiple reports of the same investigation is one lineage, not independent samples.
2. Distinguish **research question**, source-observed research move, researcher-stated motive, analyst reconstruction, and retrospective rationalization; mark unavailable early beliefs as unknown.
3. Record the actual experiment discriminator, authorized prerequisite, expected vs observed result, blocked versus falsified, and untried versus failed.
4. Audit each material causal edge and any inferred pivot with a second reviewer. Revisions are append-aware; prior conclusions remain traceable.
5. Explicitly include failed and inconclusive **independent** investigations from different publishers and domains. A failed stage in a successful exploit chain is not a distinct failed project.
6. Do not create `CTX` with `hindsight_review=passed` unless prior knowledge is supported by contemporaneous evidence available before the cutoff. Article publication date alone is not the investigation date.

Existing `CTX` count = **0**, and no historical benchmark samples are qualified.

## Offline paired A/B descriptive scorer

`tools/score_paired_trials.py` accepts a local JSON manifest (`rdl.paired_trial.v1`) of **previously independently adjudicated** responses. It runs **no LLMs** and executes no target requests.

Required arms per opaque task: `baseline`, `rdl_relevant`, and `rdl_unrelated`, all using the same pinned model revision and frozen token/tool/time budgets. Each arm requires blinded human-assigned integer grades 0–4 on:

- **question** — relevance to the uncertainty visible at this cutoff;
- **discriminator** — whether an experiment could distinguish plausible explanations;
- **prerequisite** — accurate handling of identity, access, setup and authorization;
- **pivot** — a defensible response to negative/inconclusive evidence;
- **uncertainty** — correct separation of observations, claims and what remains unknown.

Additional **hard gates**: zero scope/secret violations, zero budget overruns; incomplete matched arms or self-scored/unblinded responses fail closed. The scorer reports task-paired descriptive mean differences and win/tie/loss counts, never significance or causal generalization. The reviewer identity and actual blinding are declared by the submitter and require external audit; a field is not proof of independence.

### What constitutes an actual blind experiment?

Before any model sees a task, preregister tasks, split boundaries (publisher, researcher group, research lineage, mechanism and time), pinned model(s), seed, budget, controls, reviewers, scoring rules, stopping rule and acceptance thresholds. Use operator-owned, fresh instances and independently determined ground truth where historical cutoffs are unavailable. Humans must screen prompts for future-knowledge and target-identity leakage **after** the strict `build_predecision_candidates.py` gate. No answer keys or case IDs should enter the model prompt.

Run the baseline and RDL arms at matched resources. The unrelated-guidance control distinguishes useful research transfer from the generic benefit of being shown extra text. Synthetic fixtures exercise only the evaluator's input contracts. **No model A/B comparison was performed by this increment.**

## Status and next gate

| Component | Actual state |
| --- | --- |
| Typed corpus | 77 SRC / 77 CASE, 90 EVT / 79 REL |
| Research move observations | 6 MND, all unreviewed |
| Abstract question hypotheses | 2 proposed QPT / 3 proposed QMP; 0 curator-approved families/matches |
| Eligible pre-decision contexts | 0 CTX; 0 qualified real blind tasks |
| Case/source copyright RAW | no article RAW or licensed PAS added |
| New tools | read-only curator worksheets; offline matched-arm descriptive scorer |
| Real blind evaluation, transfer test, fine-tuning | **NOT DONE** |

Only after multiple independent human-reviewed trajectories and valid blinded decision benchmarks are available should we test Track A guidance integration with HOMELAB. Track B local fine-tuning comes later, conditional on measurable unseen-case gains. HOMELAB's execution, authority, secret and proof boundaries are unchanged.

**Review first:** verify the new source anchors, systematically audit earlier `origin=historical` questions for post-hoc wording, add genuinely independent negative investigations, and request a separate researcher to adjudicate at least the first four deep cases.
