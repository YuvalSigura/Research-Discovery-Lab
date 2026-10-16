# RDL — Blind random-sample architectural stress test

**Date:** 2026-10-16. **Method:** `random.Random('3413c3be9faec2bc').sample(range(1,110),3)` drawn before viewing source text: `CASE-000011`, `CASE-000092`, `CASE-000104`. The sampling is random; the findings are a **qualitative design stress test**, not an empirical validation of unimplemented components or an estimate of accuracy over 109 cases. No GitHub modifications.

**Three reviewed primary sources:**

- [CASE-000011 / XBOW — TiTiler](https://xbow.com/blog/xbow-titiler-lfi), especially “From URL to Arbitrary File Read in 48 Steps,” “Creative Alternatives,” and “The Remarkable Achievement.”
- [CASE-000092 / Google Project Zero — Blasting Past WebP](https://projectzero.google/2025/03/blasting-past-webp.html), especially “Déjà vu?”, “Blastdoor”, “Key material”, conclusion.
- [CASE-000104 / DEVCORE — Ubuntu unprivileged namespace restriction](https://devco.re/blog/2025/06/26/the-journey-of-bypassing-ubuntus-unprivileged-namespace-restriction-en/), especially sections 1.2, 3, 5, and 7.

## Stress case 1 — CASE-000011: XBOW TiTiler

**Actual evidence types observed:** retrospective AI-agent investigation narrative; author summaries of experiments; HTTP return snippets; GDAL/VRT technical details; embedded screenshots and image outputs; explicitly described second parallel run and second technique.

**Meaningful source-grounded facts:** The author describes a 403 at reconnaissance and a subsequent OpenAPI-based search for URL-accepting endpoints; an outbound request confirms the relevant SSRF behavior; GDAL's geospatial format expectation constrains direct file ingestion; VRT-based experimentation unlocks pixel-based retrieval; a *parallel run* uses a histogram/statistics route toward byte-by-byte reading. The report mixes “48 Steps” in a section heading with later “32 iterations/steps” framing. **Do not resolve these counts without run IDs and access to underlying traces.** The original agent telemetry is not furnished as a fully independently inspectable event log in the publication. Claims about agent motivation derive from the publisher's report.

**Possible wrong reconstruction:** put all steps under one agent's single linear investigation and say the *failure of the first route caused the second run*. The article expressly says the second route happened in parallel, not as a sequential pivot from the first agent. Another error is converting marketing claims about speed and capability into independently checked benchmarks.

**Critical capabilities:** research-run identity and branching; screenshot/image and mixed-media extraction; experiment discriminator/negative semantics; environment prerequisites; publisher-claim versus direct log provenance; evidence-to-technique and parallel lineage relations; numerical reconciliation.

**Would original 10-capability concept succeed?** Partially **if fully implemented**: acquisition, atomic claims, code/mechanism, research-state and adversarial checks could recover portions. **No** credible guarantee of correct multi-run reconstruction without an explicit *run identity / parallel causality* contract and primary agent traces. Current sidecar is insufficient.

## Stress case 2 — CASE-000092: Project Zero BLASTPASS WebP

**Actual evidence types observed:** researcher's first-person *forensic* analysis of a prior exploit developed by a distinct actor; incident context from Apple/Citizen Lab and other writeups; crash logs and PKPass artifacts obtained in 2023; resumed analysis in March 2024; another batch of logs in late 2024; reverse engineering, native memory dumps and assembly; rejected analogies; unresolved missing later-stage key/message material.

**Meaningful source-grounded facts:** the researcher explicitly reports a FORCEDENTRY-based initial idea that turned out wrong after closer parser analysis. A later batch of 2024 crash logs modified what could be said about the possible non-BlastDoor route. The final key-material discussion says the next encrypted stage was unavailable because a corresponding message was not recovered. The author analyzes how an *existing attack* worked — the attack originator's development hypotheses are **not known** from this source.

**Possible wrong reconstruction:** treat Ian Beer's forensic choices as NSO's original design pathway; assign the late-2024 evidence to his March 2024 knowledge state; treat plausible inferred HomeKit-ASLR role as demonstrated fact; treat the absence of final-stage messages as evidence that no later exploit stage existed.

**Critical capabilities:** multi-actor/lineage attribution; knowledge-versus-publication-versus-incident time; native artifact parsers for logs/code/binary and reproducibility limits; conflict and explicit-inference labels; missing evidence semantics; independent testimony and report lineage.

**Would original 10-capability concept succeed?** **No for the stronger stated goal** of reconstructing the original attack developers' thought process: the primary evidence does not contain it. **Partially** for reconstructing the published *forensic analyst's* investigation, conditional on faithful extraction and actor/time contracts. A correct system should explicitly refuse the former task.

## Stress case 3 — CASE-000104: DEVCORE Ubuntu namespace bypass

**Actual evidence types observed:** first-person discovery story with precise external trigger; a dated competition change that affects work priorities, not exploit technical feasibility; shell outputs and AppArmor audit logs; kernel source and patch analysis; proof-of-concept; exact test version and mitigation preconditions; disclosure timeline involving ZDI, Ubuntu and other researchers.

**Meaningful source-grounded facts:** the author says an external disclosure on 2025-02-16 prompted attention; discovered a bypass on 2025-02-17; later the Pwn2Own target changed away from Ubuntu and the bypass lost its competition relevance, **not** its technical validity. The article provides a test on Ubuntu 24.10 kernel 6.11.0-14-generic and states a configuration prerequisite for the bypass. Other researchers posted related work in March, and the article records a later vendor disclosure sequence.

**Possible wrong reconstruction:** assign 'technical bypass disproven' as the reason for abandoning the competition path; assume other teams' later disclosures were known when the author began investigating; generalize the behavior to all Ubuntu releases or default configurations; collapse vulnerability discovery, contest-specific objective and responsible disclosure into one outcome.

**Critical capabilities:** decision utility/objective/context model; dated external events; original versus unrelated team attribution; version/configuration-state proof; differentiating scientific truth, competition relevance and reporting acceptance; source-code diff and audit-log verification.

**Would original 10-capability concept succeed?** **Partially** for evidence/event chronology and explicit causality, if implemented. **No** guarantee of sound decision reconstruction until it models changing external objectives/incentives as distinct from changes in the tested hypothesis' truth status.

## 10 planned capability stress matrix

Legend: **P** = design could support partial reconstruction if implemented correctly; **B** = blocked by substantive missing contract or evidence; **G** = potentially good at this task with verified input but implementation not yet demonstrated. Even 'G' is **not an empirical test pass**.

| Planned capability | XBOW / 011 | WebP / 092 | DEVCORE / 104 | Essential challenge |
|---|:---:|:---:|:---:|---|
| 1. Source Acquisition | P | B | P | mixed-media and missing private original artifacts |
| 2. Provenance & Integrity | P | P | P | article URL/section != immutable corroborated raw bytes |
| 3. Atomic Claim Extraction | G | P | G | code/log/narrative and quoted third parties must stay distinct |
| 4. Evidence Verification | P | P | P | checking semantics, experiment prerequisites and scope |
| 5. Research State Reconstruction | B | B | P | run identity; original attacker unknown; external objective changes |
| 6. Causal & Temporal Reasoning | B | P | P | parallel runs; historically knowable context; external decisions |
| 7. Competing Hypotheses | P | P | P | cannot choose winner where primary data absent |
| 8. Negative & Inconclusive Reasoning | P | P | G | unsatisfying test != impossibility; goal shift != technical failure |
| 9. Adversarial Reconstruction Audit | P | P | P | needs curated false-example/contrast datasets, not just self-reports |
| 10. Scientific Evaluation & Curation | B | B | B | independent expert reviewers and gold annotations not yet available |

**Interpretation:** The initial ten-system design is a useful *starting taxonomy*, but not demonstrated sufficient on these three randomly chosen cases. Current engines have only deterministic record retrieval and candidate-structure checking, not the promised specialized extraction or independent verification.

## Missing cross-cutting contracts exposed by sample

1. **Research Lineage / Actor / Run identity:** author, publisher, tool, agent, attack originator, analyst, replayer, vendor and parallel independent trials are separate entities. An article does not equal an investigation; an investigation may contain many runs; a report may narrate research by multiple actors. This is the strongest missing dimension.
2. **Decision context and utility state:** current question and evidence, research goal, constraints, incentives, external events and choices can change without changing the underlying security hypothesis (DEVCORE competition change).
3. **Claim scope and discrimination:** separate what the action actually tested, which observation would reject it, the preconditions and what remained unresolved.
4. **Artifact modality and reproducibility:** article prose plus screenshots are not equivalent to raw machine traces, and reverse engineering of binaries requires a separate parser/proof chain.
5. **Knowledge-time availability:** distinguish occurred_at, observed_at, author's learned_at, recorded_at, disclosed_at, published_at; a timestamp printed later is not automatic proof it was available to the author then.
6. **Source/lineage independence:** corroboration requires materially independent evidence, not merely several articles restating the same original publisher's claim.
7. **Completeness/selection:** report omissions, redaction, editorial ordering, selection of successful attempts and inability to obtain original artifacts must be first-class unknowns.

## Practical next decision: no exclusive router

Create a **Source Treatment Plan** (manual first) for every article: document genre, actors, claimed events, native artifacts, experimental and historical provenance, needed processors and *forbidden inferences*. A future orchestrator can use these manifests, but no classifier should be allowed to make scientific or historical truth decisions. Sample 12–15 sources across diverse structures and independently audit segmentation/missing evidence before automating treatment-plan inference.

**No Github branches or code changes performed.**