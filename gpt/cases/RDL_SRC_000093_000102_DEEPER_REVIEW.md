# GPT RDL — Deeper study of SRC-000093..102

Primary original publisher webpages opened and source-specific portions examined, 2026-10-16. **Provisional:** all result descriptions are from original author/publisher; the question is analyst reconstructed unless explicitly authored. No independent executable confirmation, original lab trace, full timestamps or training authorization.

## SRC-000093 — GHSL U-Boot 13 parser variants

Source: https://securitylab.github.com/research/uboot-rce-nfs-vulnerability/

### T1 — Variant Analysis using CodeQL
- X: Researchers initially observe two unchecked NFS packet-size uses
- Research question (analyst): Does this data flow recur elsewhere in same bootloader?
- Reported action: Build CodeQL query for ntoh bytes reaching memcpy length, manually review nine results
- Reported observation / Y: Reported found additional cases, some checked and not exploitable
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Disclosure timeline May 15–23, 2019
- X: Generic NFS handlers seem audited
- Research question (analyst): Can UDP length underflow reach handler variants outside narrow first flow?
- Reported action: Pavel generalizes query to IP/UDP; Kevin flags missed stack overflow in nfs_handler
- Reported observation / Y: More vulnerabilities and a corrected coverage model
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000094 — Trail Bits DeepState fuzzing red-black tree

Source: https://blog.trailofbits.com/2019/01/23/fuzzing-an-api-with-deepstate-part-2/

### T1 — Mutation Testing
- X: Single hand-seeded bug isn't enough to test fuzzer quality
- Research question (analyst): Can mutation testing measure how different fuzzers detect subtle behavioral changes?
- Reported action: Generate 2,602 mutants; retain 1,120 compiling; test different fuzzers
- Reported observation / Y: Detection differences emerge rather than prove a particular security exploit
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — There ain't no such thing as a free lunch
- X: Raw fuzzer kills 25 more mutants than DeepState
- Research question (analyst): Is faster execution the actual cause?
- Reported action: Inspect mutant types and compare forking allocation behavior
- Reported observation / Y: All 25 involved pointer relationships that forked tests couldn't expose
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T3 — There ain't no such thing as a free lunch
- X: Forking suppresses certain cases
- Research question (analyst): Could non-forking replay reveal test failures?
- Reported action: Introduce no_fork option and compare replay
- Reported observation / Y: Detects previously missed effects, but saved minimal reproducibility remains difficult
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000095 — Project Zero NSS BigSig postmortem

Source: https://projectzero.google/2021/12/this-shouldnt-have-happened.html

### T1 — How did I find the bug? Stack Coverage
- X: Existing block-edge fuzzer coverage can ignore differing caller contexts
- Research question (analyst): Could stack coverage keep inputs that same basic blocks nevertheless exercise differently?
- Reported action: Explore stack coverage and object isolation with SSL cert structures
- Reported observation / Y: Reported BigSig discovery despite existing extensive coverage indicators
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Issue #2; Issue #3 Misleading metrics
- X: Well-maintained NSS had many fuzzers and relevant coverage
- Research question (analyst): Why did obvious vulnerable path survive?
- Reported action: Inspect fuzz-harness size limits and whether coverage actually used fuzz-controlled certificates
- Reported observation / Y: 10,000-byte cap and hardcoded certs meant relevant inputs not effectively explored
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T3 — Issue #3 Misleading metrics
- X: Project aggregate code coverage appears high
- Research question (analyst): Does combined coverage mean input generation explores the relevant path?
- Reported action: Compare coverage contribution by target/harness design
- Reported observation / Y: Coverage can be recorded without any controllable input across that path
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000096 — Check Point Windows Rust kernel fuzzing

Source: https://research.checkpoint.com/2025/denial-of-fuzzing-rust-in-the-windows-kernel/

### T1 — Hunting for a BugCheck
- X: Kernel crash appears only after days and no stable sample
- Research question (analyst): Is a rare crash evidence of target bug or reproducer artifact?
- Reported action: Restart long fuzzing and record kernel dumps
- Reported observation / Y: Repeated similar crashes but culprit mutating sample still unknown
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Hunting for a BugCheck; Sharpening the axe
- X: RAM disk and shared memory obscure active sample at crash time
- Research question (analyst): Can forensic extraction recover fuzzer queue state retrospectively?
- Reported action: Reject signature search, compare Volatility limits, select MemProcFS dump queue extraction
- Reported observation / Y: New corpus reduces time-to-crash from days toward shorter window
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T3 — Approaching the prey
- X: Partial corpus narrows but no exact reproducible candidate
- Research question (analyst): How can every test sample be preserved without drastically altering fuzz timing?
- Reported action: Add network sample collection to harness while testing
- Reported observation / Y: Publisher reports smaller reproduction set and improved evidence preservation
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000097 — Project Zero Sockfuzzer design

Source: https://projectzero.google/2021/04/designing-sockfuzzer-network-syscall.html

### T1 — Network stack; packet entry
- X: Need stateful XNU network testing but syscalls complex
- Research question (analyst): Where can the packet-delivery interface be simplified to target network stack?
- Reported action: Trace packet through Ethernet and proto_input to ip_input/ip6_input
- Reported observation / Y: Choose interface with clean mbuf input and fewer external state constraints
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Building XNU as a library
- X: Kernel build slow for many fuzz iterations
- Research question (analyst): Can capture compile flags and reconstruct smaller kernel-library builds?
- Reported action: Use CMake and captured flags
- Reported observation / Y: Faster iterative local library fuzz cycle
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T3 — Writing a Fuzz Target
- X: Many specialized targets vs one monolithic target
- Research question (analyst): Should simplicity justify sacrificing rare protocol state coverage?
- Reported action: Author chooses one monolithic target and acknowledges limitations
- Reported observation / Y: Simple harness, possibly less precise TCP state reachability
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T4 — Permission model; Security checks
- X: Strict sandbox entitlement checks make code unreachable in fuzzer
- Research question (analyst): Should fuzzing allow all actions then scope severity afterward?
- Reported action: Relax test harness security permission model while preserving result interpretation
- Reported observation / Y: More internal paths reachable, but practical exploitability must be separately assessed
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000098 — Trail of Bits abandoned hardware

Source: https://blog.trailofbits.com/2025/07/25/exploiting-zero-days-in-abandoned-hardware/

### T1 — Project approach
- X: Unsupported hardware hard to obtain or update
- Research question (analyst): Can a research fixture be secured despite vendor abandonment?
- Reported action: Inspect available hardware and firmware using published team methods
- Reported observation / Y: Author reports hardware-specific findings under supported local laboratory context
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Implications
- X: Technical vulnerabilities identified
- Research question (analyst): Do real deployments reproduce same outcomes as controlled hardware?
- Reported action: Compare presented demonstrations with hardware constraints
- Reported observation / Y: Author highlights limitations and assumptions rather than universal exploitation
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000099 — watchTowr FortiGate CVE-2024-23113

Source: https://labs.watchtowr.com/fortinet-fortigate-cve-2024-23113-a-super-complex-vulnerability-in-a-super-secure-appliance-in-2024/

### T1 — The Vulnerability; protocol reverse-engineering
- X: Known CVE but need high-signal unaffected-vs-affected proof
- Research question (analyst): What is necessary to trigger suspected format string inside service protocol?
- Reported action: Analyze binary call paths and trace protocol exchange
- Reported observation / Y: Publisher reports a constrained trigger after reproducing expected handler states
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Exploitability discussion
- X: Crash signal may be sufficient for scanner goal
- Research question (analyst): Is fully stable RCE necessary to verify affected devices safely?
- Reported action: Inspect glibc format-write crash behavior in controlled lab
- Reported observation / Y: Publisher argues reliable vulnerability detection may be enough, avoids full RCE demonstration
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000100 — DEVCORE ProxyLogon original research

Source: https://devco.re/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-1-ProxyLogon/

### T1 — Why targeting on Exchange Server?
- X: Researcher targets high-value Exchange mail service
- Research question (analyst): Which prior Exchange findings highlight promising but underexamined boundaries?
- Reported action: Review historical preauth SSRF and composition research
- Reported observation / Y: Author considers very early request processing a fruitful attack surface
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — A New Attack Surface; ProxyLogon
- X: Exchange front proxy dispatches request to backend
- Research question (analyst): Where does untrusted routing information become authorization-sensitive?
- Reported action: Reverse engineer Exchange Front End/Back End request architecture
- Reported observation / Y: Author reports new proxy abuse; proof evolved into multi-CVE chain
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T3 — Historical collision discussion
- X: Previously reported own vulnerability overlaps in-the-wild use
- Research question (analyst): Is parallel discovery evidence of information leakage?
- Reported action: Review later public disclosure timelines and independent exploitation descriptions
- Reported observation / Y: Author reports same SSRF used in different chain by other actor, without inferring leak as fact
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000101 — Project Zero Windows Registry Adventure Part7

Source: https://projectzero.google/2025/05/the-windows-registry-adventure-7-attack-surface.html

### T1 — Registry hive access paths
- X: Registry contains complex hive state, regular API constrains malformed forms
- Research question (analyst): Which hive file-loading entry points are controllable by less-privileged attacker?
- Reported action: Review NTUSER.DAT and NTUSER.MAN mandatory profiles plus log parsing paths
- Reported observation / Y: Identify fixture/provenance prerequisites and loader paths worth analysis
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Attack surface analysis
- X: Need to connect Part7 analysis to Part8 exploitation
- Research question (analyst): How should an exhaustive complex surface be narrowed to testable invariants?
- Reported action: Map user profiles, file formats, boundary of hive loading and authentication
- Reported observation / Y: Published candidate threat-model paths rather than a single proven exploit
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## SRC-000102 — watchTowr MOVEit CVE follow-up

Source: https://labs.watchtowr.com/auth-bypass-in-un-limited-scenarios-progress-moveit-transfer-cve-2024-5806/

### T1 — Introduction; technical walkthrough
- X: Known vendor auth bypass CVE and patch
- Research question (analyst): Which prerequisite and architecture details explain why bypass appears only in some scenarios?
- Reported action: Set up version-specific lab and examine request/auth flow
- Reported observation / Y: Publication describes reproduction and analysis of disclosed flaw
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

### T2 — Opening dialogue
- X: Article embeds dramatized character dialogue
- Research question (analyst): Does quoted dialogue establish actual historical experimental choice?
- Reported action: Separate narrative entertainment from test evidence
- Reported observation / Y: No contemporaneous actor thoughts can be inferred from rhetorical format
- Causality: only if explicitly stated in source, otherwise reported chronology; experiment validity not independently checked.

## Distinct epistemic concerns

- SRC093 original investigation unusual: 2019 report includes **day-dated team collaboration chronology** May15–23, materially stronger temporal support than an ordinary retrospection.
- SRC094 experimental mutation testing matters to research harness fidelity; mutation-kill counts are not CVE count.
- SRC095 original BigSig is a *real bug that prior fuzzers missed*, never a failed/no-bug experiment.
- SRC096 memory-dump snapshots recover earlier fuzzer state but reconstructing exact crashing seed is a separate gate.
- SRC097 broadened internal harness access differs from real exploit reachability.
- SRC099/102 existing CVE reproduction must remain distinct from original discoverers.
- SRC100 factual historical parallel collision differs from proof of stolen PoC.

