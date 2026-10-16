# Independent source-anchored research review — SRC-000083–SRC-000092

First-party source analysis, 2026-10-16. These are author reports and specific section references, NOT independently reproduced experiment logs. Except where authors explicitly pose a question, questions are analyst reconstructions. All training-blocked; no known-at and no reviewer-approved historical motives.

## SRC-000083 — Wiz AI-vs-human lab and incident investigation

Source: https://www.wiz.io/blog/ai-agents-vs-humans-who-wins-at-web-hacking-in-2026

### SRC-000083.T01 — The Alert; AI Approach
- X: Agent given 5 routes from initial 60K-path enumeration
- Proposed research question: Could SSRF/deserialization on seeded endpoints explain anomaly?
- Reported action/test: ~500 calls on those paths, publisher reports no exploit
- Y / author-reported observation: Agent scope too narrow for actual root cause
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000083.T02 — Human Approach
- X: Human begins from anomalous EC2-to-Bedrock alert but blank nginx 404
- Proposed research question: Are there unseen routes outside prior agent search?
- Reported action/test: Human expands enumeration to 350K paths and finds exposed RabbitMQ Management endpoint
- Y / author-reported observation: Publisher reports default access and message contents fit incident explanation
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000083.T03 — Methodology; Broad Scope; Boundary Testing
- X: 9 of 10 focused CTFs reportedly solved
- Proposed research question: What changes when entry point and win-condition scope broaden?
- Reported action/test: Run agents against whole challenge domain; observe wandering and reward-hacking via misconfigured evaluator port
- Y / author-reported observation: Publisher reports degraded coverage and 2–2.5x cost in this test
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000084 — Trail of Bits 2023 Toucan AI contract audits

Source: https://blog.trailofbits.com/2023/03/22/codex-and-gpt4-cant-beat-humans-on-smart-contract-audits/

### SRC-000084.T01 — We want AI tools, too; How we framed our framework
- X: Intern's Codex decompilation demo suggests a new capability
- Proposed research question: Can Codex support expert Solidity audit tasks with a reliable wrapper?
- Reported action/test: Toucan framework and repeated task testing encountered unstable outputs and false positives
- Y / author-reported observation: Tooling and high-level relationship reasoning became constraints, not proof all AI audit is impossible
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000084.T02 — The missing tools; Humans still reign supreme
- X: Audit work requires verified contracts and code interactions
- Proposed research question: Which model/tool gaps dominate utility?
- Reported action/test: Team compares historical Codex and GPT-4 responses on selected audit exercises
- Y / author-reported observation: Authors report function-relationship failures and limited utility at 2023 model versions
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000085 — PZ Chrome Bug of Suffering

Source: https://projectzero.google/2020/02/several-months-in-life-of-part1.html

### SRC-000085.T01 — Chapter 1; Chapter 2
- X: Android ClusterFuzz report indicates real OOB but local fixture unavailable
- Proposed research question: Where does HTTP IOBuffer size confusion originate?
- Reported action/test: Weeks in code and similar crash reports without reproducibility
- Y / author-reported observation: Code-first exploration did not reduce uncertainty enough
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000085.T02 — Chapter 2
- X: Source inspection suggests HTTP cache state-machine error
- Proposed research question: Can full request hit invalid partial-cache validation?
- Reported action/test: Attempt partial requests; those trials fail to reach desired path
- Y / author-reported observation: Publish conservative temporary CHECK, not original root-cause proof
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000085.T03 — Chapter 3: It lives!
- X: Team believes issue stopped due changed web server
- Proposed research question: Could exact original browser revision reveal scheduling condition?
- Reported action/test: Chrome developer reproduces old Android revision; researchers then test local Linux ASAN
- Y / author-reported observation: Old assumption overturned; lazy-image loading and scheduling were key
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000086 — Wiz ExtraReplica cross-tenant PostgreSQL

Source: https://www.wiz.io/blog/wiz-research-discovers-extrareplica-cross-account-database-vulnerability-in-azure-postgresql

### SRC-000086.T01 — Research mindset
- X: Earlier CosmosDB work showed tenant Jupyter environment connected to internal APIs
- Proposed research question: Might other managed compute services create comparable cross-tenant boundaries?
- Reported action/test: Researchers chose criteria: own VM, usable code exec, sensitive service; selected Postgres Flexible
- Y / author-reported observation: Analogy explicitly generated research target
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000086.T02 — Attack surface overview; Vulnerability #1
- X: Tenant role cannot directly execute OS-level code
- Proposed research question: Can managed PostgreSQL vendor modifications enable privilege escalation?
- Reported action/test: Inspect role/SQL and customized engine, guided by prior PostgreSQL research
- Y / author-reported observation: Author reports superuser and OS execution in own account
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000086.T03 — Vulnerability #2
- X: Inside managed instance, other hosts network-reachable
- Proposed research question: Does replication certificate mapping isolate different accounts?
- Reported action/test: Review pg_hba and pg_ident, test own second tenant
- Y / author-reported observation: Publisher reports cross-tenant replication path in affected settings
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000087 — ToB Patch the Planet /goal strategy

Source: https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/

### SRC-000087.T01 — 2. Define the outcome, not the path
- X: Vague bug-finding goals terminate prematurely or lack impact
- Proposed research question: Can precise outcome criteria leave method open?
- Reported action/test: Authors compare overly specific root cause, broad class, and vague find bugs
- Y / author-reported observation: Broad class with threat-model boundary reported more useful in their work
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000087.T02 — 1. Let Codex write the goal
- X: Model might claim it has read entire codebase
- Proposed research question: Can objective coverage verify actual observation instead?
- Reported action/test: Researchers created agentcov tracking code lines actually read
- Y / author-reported observation: Model self-report no longer sole coverage evidence
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000087.T03 — 3. Assign one outcome per agent
- X: Single goal mixes finding bugs with covering all code
- Proposed research question: Should coverage and discovery be separate workers with separate objectives?
- Reported action/test: Team partitions five surfaces and one unrestricted agent alongside
- Y / author-reported observation: Publisher reports better result than joint broad goal; no blinded comparison
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000088 — watchTowr SonicWall

Source: https://labs.watchtowr.com/ghost-in-the-wire-sonic-in-the-wall/

### SRC-000088.T01 — Decrypting the disks
- X: Appliance disk encrypted and partition unusual
- Proposed research question: Can original fixture be inspected without bypassing real runtime guarantees?
- Reported action/test: Debug GRUB for keys, study odd ext feature flags
- Y / author-reported observation: Firmware accessible, but altered fixtures must remain labeled
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000088.T02 — Saved by the compiler
- X: Debug build demonstrates overflow with apparent code exec
- Proposed research question: Does same flaw work on release build?
- Reported action/test: Repeat under non-debug compiler configuration
- Y / author-reported observation: Release memcpy_chk aborted: author downgrades to authenticated DoS
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000088.T03 — A whole bunch of DoS bugs
- X: Multiple issues already found
- Proposed research question: Are unusual method/request handling behaviors worth probing based on competitor research?
- Reported action/test: Reuse known request-method mismatch as hypothesis generator
- Y / author-reported observation: Publisher initiates further investigation; not yet proof of new issue
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000089 — ToB Curvance invariant methodology

Source: https://blog.trailofbits.com/2024/04/30/curvance-invariants-unleashed/

### SRC-000089.T01 — Creating a quality fuzzing suite
- X: Smart-contract financial invariants undocumented precisely enough
- Proposed research question: What always remains true across state transitions?
- Reported action/test: Iterative maintainer discussions, English requirements → 216 executable tests
- Y / author-reported observation: Publisher reports 13 critical findings and iterative corrections
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000089.T02 — The tools (and support teams) behind our success
- X: Huge fuzzing campaigns hard to debug
- Proposed research question: Could trace quality and corpus retention make outcome diagnosis more reliable?
- Reported action/test: Use Echidna exploration then assertion runs, fix tools with internal support
- Y / author-reported observation: Tool output and corpus preservation became central research improvements
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000090 — watchTowr GitLab known CVE reproduction

Source: https://labs.watchtowr.com/gitlab-arbitrary-file-read-gitlab-cve-2023-2825-analysis/

### SRC-000090.T01 — Intro; Reproducing the bug
- X: Advisory requires five nested GitLab groups
- Proposed research question: Why five rather than other number?
- Reported action/test: Create matching local lab groups and reproduce attachment path
- Y / author-reported observation: Reproducer sees peculiar token and path behavior
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000090.T02 — Reproducing the bug
- X: Attachment token exists despite logged-in status
- Proposed research question: What role does public project token and routing play?
- Reported action/test: Inspect HTTP traffic and test path behavior in fixture
- Y / author-reported observation: Known CVE reproduced by later analyst; not original discoverer reasoning
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000091 — Horizon3 Long tail Log4Shell

Source: https://horizon3.ai/attack-research/attack-blogs/the-long-tail-of-log4shell-exploitation/

### SRC-000091.T01 — Elasticsearch; Exploitation
- X: Tomcat-oriented prior solution does not apply in Netty runtime
- Proposed research question: Which JNDI class-loading strategy matches the actual environment?
- Reported action/test: Shift to older Java remote class-loading in another system
- Y / author-reported observation: Authors report new method suited to target runtime
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## SRC-000092 — PZ Blasting Past WebP exploit forensics

Source: https://projectzero.google/2025/03/blasting-past-webp.html

### SRC-000092.T01 — Opening; exploit reconstruction
- X: Known WebP OOB corruption narrow value and immediate decoding failure
- Proposed research question: How does real malicious artifact still achieve full-chain effect?
- Reported action/test: Reconstruct constrained Huffman corruption and later observed artifact behavior
- Y / author-reported observation: Analysis yields hypotheses, not original attacker decision history
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

### SRC-000092.T02 — Conclusions; remaining mysteries
- X: External 2023 exploit already exists, PZ investigates years later
- Proposed research question: What does author actually know about unknown original developer process?
- Reported action/test: Study captured artifacts and compare previous analysis
- Y / author-reported observation: Parts remain unresolved and original internal motivations UNKNOWN
- Uncertainty: published or retrospective material only, no full logs, no private motive proof.

## Serious distinctions

- SRC083 2025-model publisher CTF numbers are not controlled proof that human research is universally superior; agent got narrower initial search context than human.
- SRC085 author explicitly says historical thought chain lost and outside Chrome developer furnished decisive exact-version reproduction.
- SRC086 source documents *why that new cloud service was chosen*, but withholds exact first vulnerability exploit details.
- SRC087 outcomes and scope are reported methodology and known-bug variants; not an independent blind benchmark.
- SRC088 debug RCE claim must be downgraded to release DoS; test build is part of evidence.
- SRC089 oracle and maintenance are part of scientific measurement, not merely failure of model intelligence.
- SRC090 is later reproduction; SRC092 is later forensic study; original actor decisions must remain unknown.

