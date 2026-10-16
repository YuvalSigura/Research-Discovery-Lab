# GPT independent research source audit — SRC-000073 through SRC-000109

**Date:** 2026-10-16. **Status:** provisional bounded review of 37 original source pages. URLs were opened in this pass; sections were sampled in long articles rather than exhaustive line-by-line study. Some have richer earlier case-specific analysis in `gpt/analysis/` and `gpt/cases/`. No contemporaneous predecision snapshots, immutable source-article captures, independent verification or fine-tuning approval. Reconstructed questions are *analyst formulations*, not historical quotes unless expressly documented.

Each entry separates genre, analyst-formulated question, what the first-party article reports, uncertainty, and candidate research intelligence. This is a first pass, not a complete investigator mental-state reconstruction.

## SRC-000073 — How I choose a security research topic

- **Source:** https://portswigger.net/research/how-i-choose-a-security-research-topic
- **Genre:** first-person strategy & topic selection
- **Question to investigate (analyst formulation unless author explicitly states it):** How should a researcher pick a topic worth pursuing before a specific vulnerability is known?
- **Source-reported process / bounded X→Y:** Early viability test rejected one idea; another consumed six weeks before the author gave up; author then leveraged existing race-testing infrastructure for a lower-cost next direction.
- **What cannot be concluded:** Topic utility, feasibility and audience tradeoffs; the source reports reasons, but historical knowledge cutoffs and discarded candidates are not complete.
- **Candidate transferable research insight, unvalidated:** Topic-choice narratives reveal strategic decisions even when detailed exploit chronology is absent.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000074 — .MOBI WHOIS research

- **Source:** https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/
- **Genre:** first-person infrastructure and trust boundary investigation
- **Question to investigate (analyst formulation unless author explicitly states it):** Can a hard-to-satisfy WHOIS response-control prerequisite be obtained in deployed infrastructure?
- **Source-reported process / bounded X→Y:** Researchers explored abandoned `.mobi` infrastructure and observed real clients querying an acquired domain. A CA-related validation choice was reached, but they stopped before unauthorized certificate issuance.
- **What cannot be concluded:** Provider-specific early negative was not universal proof; practical control evidence does not prove downstream certificate issuance.
- **Candidate transferable research insight, unvalidated:** Separate prerequisite acquisition, measured external exposure, and intentionally unperformed final impacts.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000075 — ServiceNow chaining three bugs

- **Source:** https://www.slcyber.io/research/chaining-three-bugs-to-access-all-your-servicenow-data
- **Genre:** first-party multi-step technical investigation
- **Question to investigate (analyst formulation unless author explicitly states it):** Which architectural routing and security assumptions separate tenant/application data exposure?
- **Source-reported process / bounded X→Y:** Researchers state why a cloud workflow handling sensitive data was a promising target, probe multiple controls and combine three source-reported weaknesses.
- **What cannot be concluded:** Do not merge publication order with exact discovery chronology. Later host migration from Assetnote to Searchlight Cyber is provenance, not another investigation.
- **Candidate transferable research insight, unvalidated:** Maintain distinct component boundaries, individual finding proofs and chain prerequisites.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000076 — OpenVAS off-by-one false positive

- **Source:** https://www.stingrai.io/blog/the-perils-of-premature-vulnerability-reporting-a-case-study-in-off-by-one
- **Genre:** negative and measurement-forensics analysis
- **Question to investigate (analyst formulation unless author explicitly states it):** Was the apparent overflow caused by unsafe application code or by the measurement method?
- **Source-reported process / bounded X→Y:** The author traces the scanner warning to test instrumentation/canary conditions and challenges the originally reported interpretation.
- **What cannot be concluded:** A controlled negative/false-positive case does not establish broader safety of the codebase.
- **Candidate transferable research insight, unvalidated:** Separating measurement artifact from real target behavior matters before proof promotion.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000077 — GHSL open-source AI-powered framework

- **Source:** https://github.blog/security/how-to-scan-for-vulnerabilities-with-github-security-labs-open-source-ai-powered-framework/
- **Genre:** published methodology with aggregate results
- **Question to investigate (analyst formulation unless author explicitly states it):** How should a multi-stage AI research process filter plausible security ideas without confusing candidate generation with verified vulnerabilities?
- **Source-reported process / bounded X→Y:** Authors report threat modeling, issue proposals, audit, dedup and human validation (1003 proposals → 139 audits → 91 deduplicated, 20 unreproduced, 52 low severity, 19 reports).
- **What cannot be concluded:** These aggregates do not supply individual predecision contexts; low impact is not false positive; unreproduced is not globally disproven.
- **Candidate transferable research insight, unvalidated:** Assess staged question generation, skepticism, cost tradeoffs and independence of final checking.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000078 — Fail2exploit Fail2ban

- **Source:** https://securitylab.github.com/research/Fail2exploit/
- **Genre:** first-person audit with bounded negative result
- **Question to investigate (analyst formulation unless author explicitly states it):** Do candidate Fail2ban injection paths actually cross meaningful privilege or deployment boundaries?
- **Source-reported process / bounded X→Y:** Author tests SQL/injection and logging interfaces; author reports no reportable vulnerability despite localized concerning behavior.
- **What cannot be concluded:** Article section order not proof of pivot; local forged-log disruption differs from remote attack; custom root regex isn't default path.
- **Candidate transferable research insight, unvalidated:** Useful negative-case reasoning: distinguish attack prerequisites, deployment realism and non-exploitable effect.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000079 — Azure ML Pipelines Go Off the Rails

- **Source:** https://orca.security/resources/blog/azure-machine-learning-privilege-escalation/
- **Genre:** cloud privilege escalation write-up
- **Question to investigate (analyst formulation unless author explicitly states it):** Do cloud ML pipelines and managed identities preserve isolation when user-provided jobs execute with service privileges?
- **Source-reported process / bounded X→Y:** Orca reconstructs control-plane, task permissions and credential propagation that enable the reported boundary crossing.
- **What cannot be concluded:** First-party retrospective account; original order of researchers' internal hypotheses largely not documented.
- **Candidate transferable research insight, unvalidated:** Extract identity graph, cloud roles, execution authority and prerequisite-specific scope.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000080 — Bypassing CSP with dangling iframes

- **Source:** https://portswigger.net/research/bypassing-csp-with-dangling-iframes
- **Genre:** first-person browser research generated by maintenance
- **Question to investigate (analyst formulation unless author explicitly states it):** What changed in a formerly working browser behavior, and can a different HTML parsing condition preserve the same research capability?
- **Source-reported process / bounded X→Y:** Author reports routine lab maintenance around Chrome 97 exposed a broken technique, prompting experiments with alternate dangling markup and iframe parsing.
- **What cannot be concluded:** Author's narrated reasoning, not independent contemporaneous trace; broad CSP bypass is environment specific.
- **Candidate transferable research insight, unvalidated:** High-value case: routine planned task unexpectedly generated a new question and experiments.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000081 — Bad.Build Cloud Build

- **Source:** https://orca.security/resources/blog/bad-build-google-cloud-build-potential-supply-chain-attack-vulnerability/
- **Genre:** cloud trust and service-account analysis
- **Question to investigate (analyst formulation unless author explicitly states it):** How do inherited/default build service-account permissions turn an apparently bounded build job into higher-privilege access?
- **Source-reported process / bounded X→Y:** Published cloud architecture and account permissions explain reported opportunity for supply-chain impact.
- **What cannot be concluded:** Do not presume all Cloud Build projects have same privilege setup; impact is environment-scoped author report.
- **Candidate transferable research insight, unvalidated:** Research transfer may involve effective-permission graph rather than vulnerability name.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000082 — GHSL ngrinder unsafe YAML advisory

- **Source:** https://securitylab.github.com/advisories/GHSL-2024-069_ngrinder/
- **Genre:** short advisory and follow-up retest
- **Question to investigate (analyst formulation unless author explicitly states it):** What remains exploitable after a previous advisory and patch?
- **Source-reported process / bounded X→Y:** Advisory documents a remaining unsafe YAML processing path and report metadata.
- **What cannot be concluded:** Insufficient for an entire discovery decision diary; distinguish patch-diff checking from finding original flaw.
- **Candidate transferable research insight, unvalidated:** Useful to test limitations of short-form security advisories.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000083 — Wiz AI agents vs humans

- **Source:** https://www.wiz.io/blog/ai-agents-vs-humans-who-wins-at-web-hacking-in-2026
- **Genre:** self-reported human/AI comparative study
- **Question to investigate (analyst formulation unless author explicitly states it):** How do exploration breadth, tool choice and hypotheses shape progression in a web research challenge?
- **Source-reported process / bounded X→Y:** Authors contrast an agent spending hundreds of calls on one unlikely deserialization direction with a human using broad route enumeration and finding an exposed service.
- **What cannot be concluded:** Publisher test has differing tools/time/task conditions, cannot infer a controlled causal superiority of humans from the anecdote.
- **Candidate transferable research insight, unvalidated:** Candidate signal: coverage and direction diversity matter, but quantitative comparisons need matched arms.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000084 — Codex and GPT-4 smart-contract audits

- **Source:** https://blog.trailofbits.com/2023/03/22/codex-and-gpt4-cant-beat-humans-on-smart-contract-audits/
- **Genre:** historical feasibility assessment of older LLMs
- **Question to investigate (analyst formulation unless author explicitly states it):** What audit judgments can language models reliably support compared with established tools and humans?
- **Source-reported process / bounded X→Y:** Authors manually tested candidate tasks and concluded those historical models were weak in selected real audit scenarios.
- **What cannot be concluded:** Authors explicitly do not claim rigorous benchmark; results do not generalize to current models.
- **Candidate transferable research insight, unvalidated:** Preserve version, task, prompt and evaluation limits; do not convert author opinion to broad impossibility.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000085 — Chrome Bug of Suffering

- **Source:** https://projectzero.google/2020/02/several-months-in-life-of-part1.html
- **Genre:** extended first-person retrospective debugging
- **Question to investigate (analyst formulation unless author explicitly states it):** What can be learned when a crash appears real but resists reliable reproduction over months?
- **Source-reported process / bounded X→Y:** Author describes ongoing testing, environmental setup and changing hypotheses; notes parts of original process are missing.
- **What cannot be concluded:** Publication history is not an exact lab notebook; do not infer undocumented inner states.
- **Candidate transferable research insight, unvalidated:** Valuable for state over time, blocked vs refuted, and opportunity cost of pursuing rare signals.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000086 — Wiz ExtraReplica Azure PostgreSQL

- **Source:** https://www.wiz.io/blog/wiz-research-discovers-extrareplica-cross-account-database-vulnerability-in-azure-postgresql
- **Genre:** cloud architecture analogue and isolation test
- **Question to investigate (analyst formulation unless author explicitly states it):** Could replication-style service trust accidentally let one Azure account access another account's database?
- **Source-reported process / bounded X→Y:** Authors reason from cross-account service architecture and report a replication control weakness allowing cross-tenant PostgreSQL access.
- **What cannot be concluded:** Source is one retrospective Wiz investigation, not an independently replayed cloud trace.
- **Candidate transferable research insight, unvalidated:** Track tenant identities and platform-managed credentials as first-class evidence.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000087 — How we use /goal — Patch the Planet

- **Source:** https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/
- **Genre:** agent experiment goal selection methodology
- **Question to investigate (analyst formulation unless author explicitly states it):** How does an explicit testable goal constrain agent behavior while allowing creative methods?
- **Source-reported process / bounded X→Y:** Authors describe red/green targets using known vulnerable and patched revisions and compare outputs under constraints.
- **What cannot be concluded:** Methodology report; tasks from CVE variants can leak desired targets to evaluation unless blinded.
- **Candidate transferable research insight, unvalidated:** Question formulation should specify observable evidence and falsifiable comparisons, not just a generic goal.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000088 — SonicWall ghost in the wire

- **Source:** https://labs.watchtowr.com/ghost-in-the-wire-sonic-in-the-wall/
- **Genre:** hardware-assisted reverse engineering
- **Question to investigate (analyst formulation unless author explicitly states it):** What must be learned before research can proceed on an appliance with protected storage and limited debug access?
- **Source-reported process / bounded X→Y:** Research begins with acquiring a device, imaging drives and coping with encryption and firmware accessibility.
- **What cannot be concluded:** Debug build behavior and release exploitability must remain distinct; chronology is author retrospective.
- **Candidate transferable research insight, unvalidated:** Hardware acquisition, firmware provenance and research fixture construction are core process evidence.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000089 — Curvance invariants unleashed

- **Source:** https://blog.trailofbits.com/2024/04/30/curvance-invariants-unleashed/
- **Genre:** invariant-based smart-contract audit case
- **Question to investigate (analyst formulation unless author explicitly states it):** Can explicitly stated financial invariants reveal bugs that individual transaction checks miss?
- **Source-reported process / bounded X→Y:** Authors discuss iteratively encoding invariants, running tests and addressing tool/runtime and invariant-design errors.
- **What cannot be concluded:** Tool failures and false assertions are not automatically proof of real contract vulnerability.
- **Candidate transferable research insight, unvalidated:** Important as specification/oracle engineering and iterative hypothesis refinement.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000090 — GitLab arbitrary file read analysis

- **Source:** https://labs.watchtowr.com/gitlab-arbitrary-file-read-gitlab-cve-2023-2825-analysis/
- **Genre:** reproduction and analysis of existing CVE
- **Question to investigate (analyst formulation unless author explicitly states it):** Why does a file-read issue require an unusual hierarchy of five nested groups?
- **Source-reported process / bounded X→Y:** WatchTowr researchers recreate prerequisites and examine GitLab routing/file handling to explain the unusual condition.
- **What cannot be concluded:** Reproducers' steps must never be falsely assigned to original discoverers.
- **Candidate transferable research insight, unvalidated:** Explanatory curiosity about seemingly arbitrary prerequisite motivates fruitful reverse engineering.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000091 — Long tail of Log4Shell

- **Source:** https://horizon3.ai/attack-research/attack-blogs/the-long-tail-of-log4shell-exploitation/
- **Genre:** known-CVE surface hunting and reproduction
- **Question to investigate (analyst formulation unless author explicitly states it):** Do less obvious application paths retain a known class even after common test methods fail?
- **Source-reported process / bounded X→Y:** Authors explore alternate surfaces and candidate behaviors under application-specific constraints.
- **What cannot be concluded:** Existing exploit class; not an original zero-day discovery diary.
- **Candidate transferable research insight, unvalidated:** Prior-art-directed experimentation and boundary-specific adaptation are relevant.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000092 — Blasting Past WebP

- **Source:** https://projectzero.google/2025/03/blasting-past-webp.html
- **Genre:** forensic reconstruction of real-world exploit
- **Question to investigate (analyst formulation unless author explicitly states it):** How did a captured attack chain traverse a WebP parser and survive modern runtime protections?
- **Source-reported process / bounded X→Y:** Project Zero uses external artifacts and technical reconstruction of an older exploit; some stages remained unresolved.
- **What cannot be concluded:** The researcher's 2025 reconstruction ≠ private reasoning of 2023 exploit authors. Later-obtained evidence cannot populate early cutoff snapshots.
- **Candidate transferable research insight, unvalidated:** Clear example of multiple research lineages observing the same exploit.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000093 — U-Boot NFS RCE vulnerabilities

- **Source:** https://securitylab.github.com/research/uboot-rce-nfs-vulnerability/
- **Genre:** source-code audit with multiple related findings
- **Question to investigate (analyst formulation unless author explicitly states it):** Which network parsing invariants in U-Boot NFS can fail across repeated request data?
- **Source-reported process / bounded X→Y:** GHSL authors report finding multiple NFS parser flaws through CodeQL-guided and manual code reasoning.
- **What cannot be concluded:** Many findings within one audit are not many independent investigation samples.
- **Candidate transferable research insight, unvalidated:** Separate source-to-sink technical proof, configured boot path and actual execution exposure.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000094 — Fuzzing an API with DeepState Part 2

- **Source:** https://blog.trailofbits.com/2019/01/23/fuzzing-an-api-with-deepstate-part-2/
- **Genre:** experimental harness and oracle design
- **Question to investigate (analyst formulation unless author explicitly states it):** When does a fuzzer fail to reveal a bug because its harness/coverage is incomplete?
- **Source-reported process / bounded X→Y:** Authors adjust generators, assertions and symbolic/mutation engines, interpreting code coverage and crash feedback.
- **What cannot be concluded:** Tool noise and missing coverage do not disprove the target's possible flaws.
- **Candidate transferable research insight, unvalidated:** Research intelligence often resides in improving experimental instrumentation.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000095 — This shouldn't have happened — BigSig

- **Source:** https://projectzero.google/2021/12/this-shouldnt-have-happened.html
- **Genre:** postmortem of missed real vulnerability
- **Question to investigate (analyst formulation unless author explicitly states it):** How could a serious vulnerability persist despite extensive fuzzing?
- **Source-reported process / bounded X→Y:** Author analyzes why candidate fuzzing setups and coverage had not found an existing bug.
- **What cannot be concluded:** It is not a negative 'no vulnerabilities found' research outcome; the bug is real.
- **Candidate transferable research insight, unvalidated:** Avoid conflating coverage, state reachability, correctness of oracle and no-crash outcome.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000096 — Denial of Fuzzing — Rust Windows Kernel

- **Source:** https://research.checkpoint.com/2025/denial-of-fuzzing-rust-in-the-windows-kernel/
- **Genre:** fuzzing failure analysis and forensic workaround
- **Question to investigate (analyst formulation unless author explicitly states it):** When unreproducible crashes block triage, can crash-time state be captured more faithfully?
- **Source-reported process / bounded X→Y:** Authors report using a RAM-disk/dump-oriented research setup to reconstruct crash conditions and save seed inputs.
- **What cannot be concluded:** A workaround may apply only to specific kernel/harness conditions; preserve author-reported chronology.
- **Candidate transferable research insight, unvalidated:** Measurement provenance and preserving failure fixtures can unlock research directions.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000097 — Designing Sockfuzzer

- **Source:** https://projectzero.google/2021/04/designing-sockfuzzer-network-syscall.html
- **Genre:** explicit first-person fuzzer design
- **Question to investigate (analyst formulation unless author explicitly states it):** Which XNU network-syscall assumptions remain untested, despite belief that the surface was heavily fuzzed?
- **Source-reported process / bounded X→Y:** Author describes adapting knowledge from Chrome fuzzing and building Sockfuzzer with targeted syscall/state coverage.
- **What cannot be concluded:** Community belief is not test evidence; method portability requires platform-specific adaptation.
- **Candidate transferable research insight, unvalidated:** Prior expertise transferred to newly scoped experiment design.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000098 — Exploiting zero days in abandoned hardware

- **Source:** https://blog.trailofbits.com/2025/07/25/exploiting-zero-days-in-abandoned-hardware/
- **Genre:** hardware research with constraints
- **Question to investigate (analyst formulation unless author explicitly states it):** How can an abandoned device be studied when firmware availability, access and maintenance support are limited?
- **Source-reported process / bounded X→Y:** Research team obtains gear, inspects firmware/service behaviors and reports exploit demonstrations.
- **What cannot be concluded:** Multiple findings and prototypes share hardware lineage; do not assume general user deployment impact.
- **Candidate transferable research insight, unvalidated:** Acquisition and fixture reality affects which questions can be asked.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000099 — FortiGate CVE-2024-23113 analysis

- **Source:** https://labs.watchtowr.com/fortinet-fortigate-cve-2024-23113-a-super-complex-vulnerability-in-a-super-secure-appliance-in-2024/
- **Genre:** deep reproduction of prior report
- **Question to investigate (analyst formulation unless author explicitly states it):** Can researchers verify real exploitability of a difficult pre-existing CVE under realistic appliance conditions?
- **Source-reported process / bounded X→Y:** Article documents reproduction rabbit holes and detailed primitive-specific constraints.
- **What cannot be concluded:** Again original discoverer vs later reproducer separation; stylized article prose isn't a raw thought transcript.
- **Candidate transferable research insight, unvalidated:** Proof requires practical constraints beyond static vulnerability label.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000100 — ProxyLogon new Exchange attack surface

- **Source:** https://devco.re/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-1-ProxyLogon/
- **Genre:** first-person architectural discovery narrative
- **Question to investigate (analyst formulation unless author explicitly states it):** Which overlooked Exchange routing/control-plane feature might violate assumptions about unauthenticated access?
- **Source-reported process / bounded X→Y:** DEVCORE authors explain studying an overlooked area and forming hypotheses about backend request and authorization boundaries.
- **What cannot be concluded:** Publication order not exact research-time causal order.
- **Candidate transferable research insight, unvalidated:** Original-research case with architecture-led exploration.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000101 — Windows Registry Adventure Part 7

- **Source:** https://projectzero.google/2025/05/the-windows-registry-adventure-7-attack-surface.html
- **Genre:** attack surface exploration and corpus-based design
- **Question to investigate (analyst formulation unless author explicitly states it):** How to transform registry subsystem complexity into concrete parser and memory hypotheses?
- **Source-reported process / bounded X→Y:** Author analyzes entry points, attackers' primitives, registry hive layout and test/harness affordances.
- **What cannot be concluded:** Part 8 is same research line; treat as connected chapters not independent cases.
- **Candidate transferable research insight, unvalidated:** Systematic discovery and technical model-building precede exploitability.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000102 — MOVEit CVE-2024-5806 analysis

- **Source:** https://labs.watchtowr.com/auth-bypass-in-un-limited-scenarios-progress-moveit-transfer-cve-2024-5806/
- **Genre:** post-disclosure technical reconstruction with theatrical dialogue
- **Question to investigate (analyst formulation unless author explicitly states it):** How does an apparent auth-bypass report really work in the specified MOVEit architecture?
- **Source-reported process / bounded X→Y:** WatchTowr analyzes known CVE mechanics and checks prerequisites.
- **What cannot be concluded:** Fictionalized dialogue opening is not a contemporaneous experiment or historical decision trace.
- **Candidate transferable research insight, unvalidated:** Preserve source rhetoric separately from evidence-bearing sections.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000103 — Sitecore cache poisoning to RCE

- **Source:** https://labs.watchtowr.com/cache-me-if-you-can-sitecore-experience-platform-cache-poisoning-to-rce/
- **Genre:** large multi-stage technical case study
- **Question to investigate (analyst formulation unless author explicitly states it):** Do cache-key, request parameter and backend expression boundaries allow unsafe reuse of attacker-controlled cache contents?
- **Source-reported process / bounded X→Y:** Authors describe architecture, experiments and a resulting chain from cache poisoning to code execution.
- **What cannot be concluded:** Very long article; relevant opening and section(s) inspected, not exhaustive intermediate chronology. No exact known-at research states.
- **Candidate transferable research insight, unvalidated:** Maintain cache state, version and prerequisites; avoid flattening technical exposition into research diary.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000104 — Ubuntu namespace bypass journey

- **Source:** https://devco.re/blog/2025/06/26/the-journey-of-bypassing-ubuntus-unprivileged-namespace-restriction-en/
- **Genre:** first-person constraint-driven research
- **Question to investigate (analyst formulation unless author explicitly states it):** Which Ubuntu permission restrictions might be bypassed, and does continued work still serve competition objectives?
- **Source-reported process / bounded X→Y:** Researcher reports a viable Ubuntu-specific direction and later a competition switch to RHEL that changed priorities.
- **What cannot be concluded:** Stopping because objective changed is not refuting a technical result.
- **Candidate transferable research insight, unvalidated:** Research-goal state must remain separate from hypothesis truth.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000105 — Atlas AI vulnerability researcher

- **Source:** https://www.wiz.io/blog/atlas-ai-vulnerability-researcher
- **Genre:** vendor methodology and product capability claims
- **Question to investigate (analyst formulation unless author explicitly states it):** What roles should orchestrator, static/dynamic analyzers and models play in automated research?
- **Source-reported process / bounded X→Y:** Wiz reports multi-agent architecture and selective use of expensive models with proofs.
- **What cannot be concluded:** Publisher metrics and examples are not independent benchmark; not a full raw investigator decision trace.
- **Candidate transferable research insight, unvalidated:** Hypotheses for harness/model separation, not validated universal architecture.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000106 — Frontier AI Vulnerability Burst

- **Source:** https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/
- **Genre:** vendor aggregate AI-security research claim
- **Question to investigate (analyst formulation unless author explicitly states it):** How should AI's detection rate be evaluated across selected disclosed cases?
- **Source-reported process / bounded X→Y:** Authors report 92% of cases discovered in selected corpus of recent vulnerabilities.
- **What cannot be concluded:** Potential selection bias, lineages and leaked CVE familiarity; not proof of general prospective discovery.
- **Candidate transferable research insight, unvalidated:** Distinguish replication speed from unknown-vulnerability discovery.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000107 — OpenVPN2 warnings with CodeQL

- **Source:** https://blog.trailofbits.com/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/
- **Genre:** quantitative alert triage and negative outcome
- **Question to investigate (analyst formulation unless author explicitly states it):** Can query design reduce 2,500 compiler warning noise to a feasible, evidence-grounded manual review list?
- **Source-reported process / bounded X→Y:** Authors report iterative query stages reducing large candidate sets to around 20 manual reviews, with no exploitable issue in this tested slice.
- **What cannot be concluded:** Not thousands of refuted vulnerabilities; don't confuse filtering from proving safety.
- **Candidate transferable research insight, unvalidated:** Learn changing instrumentation sensitivity and bounded negative conclusions.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000108 — Searching statically-linked vulnerable functions

- **Source:** https://projectzero.google/2018/12/searching-statically-linked-vulnerable.html
- **Genre:** tool development and source-matching method
- **Question to investigate (analyst formulation unless author explicitly states it):** Can one identify vulnerable library copies when code is embedded inside binaries without dynamic linkage metadata?
- **Source-reported process / bounded X→Y:** Author describes function matching and feature selection to detect vulnerable code copies in downstream executables.
- **What cannot be concluded:** Detection of matching code isn't proof target exploitable; article not exploit decision diary.
- **Candidate transferable research insight, unvalidated:** Research question turns unknown software lineage into analyzable surface.
- **Status:** bounded original article review; provisional; training blocked.

## SRC-000109 — Finding hidden features — Bug Culture

- **Source:** https://bugculture.io/fuzz-or-miss/
- **Genre:** first-person hidden-functionality research
- **Question to investigate (analyst formulation unless author explicitly states it):** After seemingly negative conventional testing, can less visible functionality reveal additional research opportunities?
- **Source-reported process / bounded X→Y:** Author reports initial discouraging results, then pivot to hidden features and fuzzing that produced positive findings.
- **What cannot be concluded:** Initial negative result must not be mislabeled final no-bug conclusion; authors' narrative isn't full original test log.
- **Candidate transferable research insight, unvalidated:** Key case of systematically broadening environment model before concluding exhausted.
- **Status:** bounded original article review; provisional; training blocked.

## Comparative observations, *not* final principles

- A previously planned task can trigger an unexpected research question (073, 080, 090), but source-reported motive must not be silently turned into a model gold label.
- Reality constraints, identity/context and goal changes affect scientific interpretation: cloud identity (079,081,086), access/prerequisites (074,088,098), competition objectives (104).
- Failed outcomes are multidimensional: blocked prerequisite, tool/oracle failure, explicit hypothesis refutation, cost-of-work abandonment and negative scoped audit (076,078,085,095,096,107,109).
- Reproduction and forensic reconstruction (090,092,099,102) are not the originator's historical process.
- Some sources are methodology, aggregate performance claims or advisories (077,082,083,084,087,105,106); don't fabricate private X→Y from them.
- The most useful next work is unabridged source-grounded step extraction and challenge with independent reviewer and true predecision timing; no training approval is justified yet.

