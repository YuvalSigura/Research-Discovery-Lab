# RDL — Source-only intake from four discovery passes

Intake: 32 primary publisher source URLs; baseline: 77; new catalogue total: 109. Date: 2026-10-16.

## Scientific restrictions

- These are catalogue CASE placeholders (one per publication), **not** 32 independently reconstructed or validated investigations.
- All new sources are unlicensed/unreviewed and not archived; all new CASE records are not_started and evidence unknown.
- No event, relation, question, mindset or predecision CTX was invented. No zero-day, novelty, causal link, negative conclusion or AI performance is independently approved.
- Negative result means no issue *in the test scope*; Bug Culture has an **initial negative then positive** research outcome; Project Zero fuzzing postmortem studies an undetected real bug.
- Wiz / Unit 42 / AI methodology articles are reported by their authors; not blinded multi-team evaluation.
- ngrinder and Blasting Past WebP are supplemental, not complete discovery decision logs.
- Dates are null when not checked from primary text; cross-paper independence, rights, publisher wording and temporal provenance need human review.
- Three earlier suggestions were already present on main and are **not duplicated**: CASE-000024 HTTP Terminator, CASE-000025 HTTP/1.1 Must Die, CASE-000040 Listen to the Whispers.

## Candidate register

| Case | Triage | Publisher | Source | Research opportunity |
|---|---|---|---|---|
| CASE-000078 | deep | GitHub Security Lab | [Fail2exploit: a security audit of Fail2ban](https://securitylab.github.com/research/Fail2exploit/) | First-person audit with no reportable findings |
| CASE-000079 | deep | Orca Security | [Azure ML: When Pipelines Go Off the Rails](https://orca.security/resources/blog/azure-machine-learning-privilege-escalation/) | Managed-identity and cloud-pipeline trust-boundary study |
| CASE-000080 | deep | PortSwigger | [Bypassing CSP with dangling iframes](https://portswigger.net/research/bypassing-csp-with-dangling-iframes) | Browser behavior invalidated earlier attack approach; documented pivot |
| CASE-000081 | deep | Orca Security | [Bad.Build: Google Cloud Build](https://orca.security/resources/blog/bad-build-google-cloud-build-potential-supply-chain-attack-vulnerability/) | Cloud service-account and artifact permission boundaries |
| CASE-000082 | supplemental | GitHub Security Lab | [GHSL-2024-069: Unsafe YAML deserialization in ngrinder](https://securitylab.github.com/advisories/GHSL-2024-069_ngrinder/) | Short impact-assessment advisory; not a full research trajectory |
| CASE-000083 | methodology | Wiz Research | [AI Agents vs Humans: Who Wins at Web Hacking in 2026?](https://www.wiz.io/blog/ai-agents-vs-humans-who-wins-at-web-hacking-in-2026) | Publisher-reported human vs agent exploration decisions; not blind independent trial |
| CASE-000084 | deep | Trail of Bits | [Codex (and GPT-4) can't beat humans on smart contract audits](https://blog.trailofbits.com/2023/03/22/codex-and-gpt4-cant-beat-humans-on-smart-contract-audits/) | Failure modes and modified research strategy; historical models only |
| CASE-000085 | deep | Google Project Zero | [Chrome bug of suffering: Project Zero Part 1](https://projectzero.google/2020/02/several-months-in-life-of-part1.html) | Extended reproduction attempts and retrospective hypothesis changes |
| CASE-000086 | deep | Wiz Research | [ExtraReplica: cross-account Azure PostgreSQL vulnerability](https://www.wiz.io/blog/wiz-research-discovers-extrareplica-cross-account-database-vulnerability-in-azure-postgresql) | Cross-system architecture analogy and isolation assumptions |
| CASE-000087 | methodology | Trail of Bits | [How we use /goal to find bugs in Patch the Planet](https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/) | Research goal selection and agent experiment design |
| CASE-000088 | deep | watchTowr Labs | [Ghost in the Wire, Sonic in the Wall](https://labs.watchtowr.com/ghost-in-the-wire-sonic-in-the-wall/) | Appliance reverse-engineering setbacks and debug vs release impact |
| CASE-000089 | deep | Trail of Bits | [Curvance: Invariants unleashed](https://blog.trailofbits.com/2024/04/30/curvance-invariants-unleashed/) | Invariant-based auditing and hypothesis checks |
| CASE-000090 | deep | watchTowr Labs | [GitLab Arbitrary File Read CVE-2023-2825 Analysis](https://labs.watchtowr.com/gitlab-arbitrary-file-read-gitlab-cve-2023-2825-analysis/) | Reported flaw reproduction and unusual hierarchy prerequisite |
| CASE-000091 | deep | Horizon3.ai | [The Long Tail of Log4Shell Exploitation](https://horizon3.ai/attack-research/attack-blogs/the-long-tail-of-log4shell-exploitation/) | Testing alternative surfaces after non-useful initial probes |
| CASE-000092 | supplemental | Google Project Zero | [Blasting Past WebP](https://projectzero.google/2025/03/blasting-past-webp.html) | Forensic reconstruction of already existing exploit; not first-discoverer notes |
| CASE-000093 | deep | GitHub Security Lab | [U-Boot NFS RCE Vulnerabilities](https://securitylab.github.com/research/uboot-rce-nfs-vulnerability/) | CodeQL and manual analysis of embedded network code |
| CASE-000094 | methodology | Trail of Bits | [Fuzzing an API with DeepState Part 2](https://blog.trailofbits.com/2019/01/23/fuzzing-an-api-with-deepstate-part-2/) | Iterative test harness decisions and correction of blind spots |
| CASE-000095 | deep | Google Project Zero | [This shouldn't have happened: A vulnerability postmortem](https://projectzero.google/2021/12/this-shouldnt-have-happened.html) | Why fuzzing did not uncover a serious bug; not a no-bug conclusion |
| CASE-000096 | deep | Check Point Research | [Denial of Fuzzing: Rust in the Windows kernel](https://research.checkpoint.com/2025/denial-of-fuzzing-rust-in-the-windows-kernel/) | Unexpected unreproducible crashes forced a research pivot |
| CASE-000097 | methodology | Google Project Zero | [Designing Sockfuzzer: XNU network syscall fuzzer](https://projectzero.google/2021/04/designing-sockfuzzer-network-syscall.html) | Harness fidelity and experimental design decisions |
| CASE-000098 | deep | Trail of Bits | [Exploiting zero days in abandoned hardware](https://blog.trailofbits.com/2025/07/25/exploiting-zero-days-in-abandoned-hardware/) | Hardware research with service pivot and firmware access problems |
| CASE-000099 | deep | watchTowr Labs | [FortiGate CVE-2024-23113: watchTowr analysis](https://labs.watchtowr.com/fortinet-fortigate-cve-2024-23113-a-super-complex-vulnerability-in-a-super-secure-appliance-in-2024/) | Reproduction of disclosed issue with environment prerequisites |
| CASE-000100 | deep | DEVCORE | [New Attack Surface on MS Exchange Part 1: ProxyLogon](https://devco.re/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-1-ProxyLogon/) | Architecture-led frontend/backend trust-boundary research |
| CASE-000101 | deep | Google Project Zero | [Windows Registry Adventure #7: Attack surface analysis](https://projectzero.google/2025/05/the-windows-registry-adventure-7-attack-surface.html) | Attack surface modeling; distinct from existing Part 8 |
| CASE-000102 | deep | watchTowr Labs | [Auth Bypass in (Un)Limited Scenarios: MOVEit](https://labs.watchtowr.com/auth-bypass-in-un-limited-scenarios-progress-moveit-transfer-cve-2024-5806/) | Reanalysis of auth bypass with reproduction constraints |
| CASE-000103 | deep | watchTowr Labs | [Cache Me If You Can: Sitecore cache poisoning to RCE](https://labs.watchtowr.com/cache-me-if-you-can-sitecore-experience-platform-cache-poisoning-to-rce/) | Cache behavior, filtered inputs and research pivot |
| CASE-000104 | deep | DEVCORE | [Journey of Bypassing Ubuntu Unprivileged Namespace Restriction](https://devco.re/blog/2025/06/26/the-journey-of-bypassing-ubuntus-unprivileged-namespace-restriction-en/) | First-person security boundary investigation |
| CASE-000105 | methodology | Wiz Research | [Introducing Atlas: Wiz AI vulnerability researcher](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher) | Publisher description of AI research orchestration and verification |
| CASE-000106 | methodology | Unit 42 | [The Frontier AI Vulnerability Burst](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/) | Publisher self-report of automated source vulnerability research |
| CASE-000107 | deep | Trail of Bits | [Taming 2,500 compiler warnings with CodeQL: OpenVPN2](https://blog.trailofbits.com/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/) | Thousands of warnings to 20 reviews; no exploitable issues in tested context |
| CASE-000108 | methodology | Google Project Zero | [Searching statically-linked vulnerable library functions in executable code](https://projectzero.google/2018/12/searching-statically-linked-vulnerable.html) | Binary-function similarity false positives and tool limitations |
| CASE-000109 | deep | Bug Culture | [Finding Hidden Features](https://bugculture.io/fuzz-or-miss/) | Initially negative web assessment pivoted to deeper directory discovery; final outcome positive |

## Evidence gate

Review first-party sections and provenance, record documented historical events only when anchored, separate inference from reported investigator decisions, run independent second-curator and research-lineage reviews, and never export unreviewed material as blind-qualified predecision knowledge.
