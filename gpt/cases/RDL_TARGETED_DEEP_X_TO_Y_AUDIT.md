# Deep follow-up: experimental evidence-grounded X→Y records

**Date:** 2026-10-16. Author: GPT independent RDL research. All records candidate/unreviewed, first-party publisher reports. These 7 investigations are selected because the primary articles explicitly contain decisions or investigative pivots; the selection is intentional and *not* a representative sample of 109 articles. `SRC-000049` is a short advisory: its row uses linked first-party technical context and is marked as an unverified bridge, not a historic decision from the advisory.
**Scientific restrictions:** questions are analyst phrasing except where directly stated; never train a next-step policy on Y/revealed future facts; neither external reproduction nor adjudication nor raw historical transcripts were obtained.

## SRC-000044: PAN-OS — patch review becomes novel boundary hypothesis

- Publisher first-party URL: https://www.slcyber.io/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os-cve-2025-0108
- Research actor/lineage: Assetnote / Searchlight Cyber original researchers

### T01: Why is the Architecture Suspicious?
- X: Routine CVE patch checks
- Question (analyst): Why might PAN-OS management auth be suspicious after the known patch?
- Action: Inspect Nginx→Apache→PHP architecture and authorization header control
- Reported observation: Authentication was decided upstream on one representation of the URI but Apache reinterpreted paths downstream
- Y: A new inter-component path-normalization discrepancy became testable
- Basis: author_explicit_pivot. Confidence limited to first-party narrative; no independent replay.

### T02: Weird Apache Behavior
- X: Nginx and Apache can see differing URI normalization
- Question (analyst): Can an internal Apache rewrite cause an additional decode/redirect without recomputing the prior auth header?
- Action: Review RewriteRule internal redirect effects and compare differently encoded paths in a local analogue
- Reported observation: Publisher reports double decoding and survival of upstream authorization state
- Y: Hypothesis strengthened that path disagreement could misclassify protected management routes
- Basis: author_reported_inference. Confidence limited to first-party narrative; no independent replay.

### T03: The Bug; Conclusion
- X: Parser behavior suggests mismatch
- Question (analyst): Does protected PHP functionality become reachable via the two-layer processing sequence?
- Action: Test a constrained management path in affected lab version
- Reported observation: Publisher shows a response on protected PHP path despite being treated as unauthenticated by Nginx
- Y: Reported auth bypass within named PAN-OS configurations
- Basis: author_reported_test. Confidence limited to first-party narrative; no independent replay.

## SRC-000045: Next.js — false negatives and false positives in scanner oracle

- Publisher first-party URL: https://www.slcyber.io/research/doing-the-due-diligence-analysing-the-next-js-middleware-bypass-cve-2025-29927
- Research actor/lineage: Assetnote follow-up due-diligence team, not original CVE discoverers

### T01: What's Wrong With The Publicly Disclosed Checks?
- X: Public checks rely on middleware response headers typical of rewrites
- Question (analyst): Do detection signatures miss the more common middleware redirect behavior?
- Action: Compare redirect and rewrite responses in multiple framework versions
- Reported observation: Author reports common middleware header signals absent for redirects
- Y: Re-evaluate validity of public scanner coverage
- Basis: author_explicit_question. Confidence limited to first-party narrative; no independent replay.

### T02: Building a More Reliable Check
- X: Redirecting middleware lacks expected headers
- Question (analyst): Can an alternate client request context reveal a middleware-origin header?
- Action: Inspect framework source and test Next.js data request behavior
- Reported observation: Publisher reports a different internal response header appears for the relevant redirect handling
- Y: Design a broader detector of relevant middleware behavior
- Basis: author_reported_causal. Confidence limited to first-party narrative; no independent replay.

### T03: What's Wrong With The Publicly Disclosed Checks?; Building a More Reliable Check
- X: Candidate middleware redirect signals are noisy
- Question (analyst): Can ordinary locale redirects be distinguished from meaningful auth middleware?
- Action: Compare baseline locale routing and different headers; aggregate multiple framework variants
- Reported observation: Publisher reports locale-based false positives and redesigned narrower detection
- Y: Improve accuracy and reduce number of requests in vendor tests
- Basis: author_reported_measurement. Confidence limited to first-party narrative; no independent replay.

## SRC-000048: Ivanti — previously published exploit check fails in older build

- Publisher first-party URL: https://www.slcyber.io/research/high-signal-detection-and-exploitation-of-ivantis-pulse-connect-secure-auth-bypass-rce
- Research actor/lineage: Assetnote researchers reproducing an already known Ivanti advisory

### T01: Introduction
- X: Vendor disclosed active-exploitation class and public PoCs became available
- Question (analyst): Do existing proof requests work on all reportedly vulnerable product versions?
- Action: Configure several Ivanti versions and run published detection candidates
- Reported observation: Older test instance did not behave as public PoCs predicted
- Y: Scope the negative to test-version and request form; investigate the gate rather than declare patch
- Basis: author_reported_causal. Confidence limited to first-party narrative; no independent replay.

### T02: Analysis of the authentication bypass; Conclusion
- X: Public payload fails on version reported vulnerable
- Question (analyst): What is checked by the proxy before the Python endpoint executes?
- Action: Reverse engineer prefix handling against actual stored firmware and compare normalized routes
- Reported observation: Source reports an overly broad prefix match to an allowed path, even though downstream behavior differs
- Y: Obtain alternative high-signal detector in lab
- Basis: author_reported_technical. Confidence limited to first-party narrative; no independent replay.

### T03: Proof; analysis
- X: Proxy prefix interpretation is suspected
- Question (analyst): Can behavior be differentiated from a true authorization denial?
- Action: Compare denied baseline request and a semantically equivalent request admitted through a different route presentation
- Reported observation: Source shows a 403 vs 200 response and product behavior differences
- Y: Author reports authenticated-boundary bypass on tested build
- Basis: author_reported_test. Confidence limited to first-party narrative; no independent replay.

## SRC-000049: Next.js advisory — full process missing, linked technical investigation

- Publisher first-party URL: https://www.slcyber.io/research/advisory-next-js-ssrf-cve-2024-34351
- Research actor/lineage: Assetnote original research, SSRF

### T01: Summary; Blog Post; related Digging for SSRF in NextJS apps
- X: Framework commonly deployed as 'mostly static'
- Question (analyst): Could server features in Next.js expose more behavior than visible static pages suggest?
- Action: Related linked first-party detailed blog examines Server Actions and resulting host forwarding
- Reported observation: Publisher advisory records SSRF result under affected conditions; detailed study separate publication
- Y: Connect advisory to richer original research rather than invent an advisory-derived diary
- Basis: analyst_bridge_unverified. Confidence limited to first-party narrative; no independent replay.

## SRC-000050: Citrix NetScaler — blocked binary diff becomes dynamic evidence path

- Publisher first-party URL: https://www.slcyber.io/research/citrix-denial-of-service-analysis-of-cve-2024-8534
- Research actor/lineage: Assetnote follow-up patch analysis researchers

### T01: Finding the RDP Handler
- X: Known CVE patch, need high-signal non-disruptive check, unknown root cause
- Question (analyst): Can diffing patched/unpatched core binary identify responsible function?
- Action: Use Ghidra and BinDiff on two builds
- Reported observation: Hundreds of changed functions and stripped names made direct static diff unproductive
- Y: Switch to configuring valid RDP Proxy traffic and using log string anchor
- Basis: author_explicit_pivot. Confidence limited to first-party narrative; no independent replay.

### T02: Finding the RDP Handler
- X: Static code location unclear; RDP Proxy fixture available
- Question (analyst): Can runtime log strings identify protocol handler in stripped binary?
- Action: Connect with valid RDP file and match observed log text to binary constant
- Reported observation: Publisher found RDP handler, leveraged prior decompilation to recover names
- Y: Code path now identifiable for targeted investigation
- Basis: author_reported_test. Confidence limited to first-party narrative; no independent replay.

### T03: Triggering a Crash
- X: Protocol processing understood but bug trigger unknown
- Question (analyst): Which inputs trigger the reported memory corruption?
- Action: Probe ticket/cookie structures, then vary framing, lengths and repetition
- Reported observation: Initial field mutations did not crash; simpler oversized packet framing eventually did
- Y: Obtain minimal repeatable crash fixture for triage
- Basis: author_reported_causal. Confidence limited to first-party narrative; no independent replay.

### T04: Debugging the Crash; Out of Time; What Did We Learn?
- X: Crash reproducible, memory corruption cause remains uncertain
- Question (analyst): Can root cause and higher-than-DoS impact be proven under time/debug constraints?
- Action: Review stack and memory with slow reboot-driven debug loop
- Reported observation: Authors ran out of time before conclusive corruption cause or exploitability proof
- Y: Publish scoped DoS conclusion; construct safer fingerprinting check from connection behavior
- Basis: author_explicit_stop. Confidence limited to first-party narrative; no independent replay.

## SRC-000059: Gmail–Drive — planned SVG research uncovers mismatched security labels

- Publisher first-party URL: https://pentera.io/resources/research/integration-flaws-Gmail-Google-drive/
- Research actor/lineage: Pentera Ben Ilkashi

### T01: The Trigger: An Old-New Frontier in Phishing
- X: Routine product phishing capability research involving SVG attachments
- Question (analyst): Why does Gmail block a test SVG whereas other email providers may not?
- Action: Observe controls for identical controlled test artifact across delivery flows
- Reported observation: Gmail author reports blocked malicious SVG, triggering curiosity about alternate first-party integration
- Y: New investigation into Gmail and Drive scanning boundaries
- Basis: author_explicit_pivot. Confidence limited to first-party narrative; no independent replay.

### T02: Gmail's Files Scanner Bypass
- X: Gmail and Drive scanner classifications may differ
- Question (analyst): Does Google Drive file sharing preserve or incorrectly inherit Gmail's safe labeling?
- Action: Compare blocked direct attachment with Drive-linked content shown in Gmail
- Reported observation: Author reports conflicting scan verdicts and normal-looking in-app 'Scanned by Gmail' presentation
- Y: First distinct cross-service trust-label inconsistency reported
- Basis: author_reported_test. Confidence limited to first-party narrative; no independent replay.

### T03: Drive's Incomplete-Scan Warning Circumvention
- X: Initial trust-label discrepancy known
- Question (analyst): Does related Drive incomplete-scan warning survive the same Gmail integration?
- Action: Use controlled non-virus-detected sample and compare download UI in Drive versus Gmail preview
- Reported observation: Author reports missing warning in Gmail UI but present in direct Drive UI
- Y: Second separate UI trust/safety boundary finding
- Basis: author_explicit_pivot. Confidence limited to first-party narrative; no independent replay.

## SRC-000069: LOLBAS Odyssey — manual method creates its own automation opportunity

- Publisher first-party URL: https://pentera.io/wp-content/uploads/2023/08/pentera_labs_the_lolbas_odyssey_finding_new_lolbas_and_how_you_can_too.pdf
- Research actor/lineage: Pentera Nir Chako

### T01: The Manual 'One by One' Approach (PDF pp.5–6)
- X: Pentera's existing exposure validation used LOLBAS downloaders
- Question (analyst): Can additional trusted binaries be used as downloaders in SYSTEM context?
- Action: Try Excel as candidate after studying LOLBAS catalog
- Reported observation: Publisher reports Excel did not work for elevated-system context
- Y: Research shifts toward systematic enumerate-and-try method from Oddvar Moe's prior art
- Basis: author_explicit_pivot. Confidence limited to first-party narrative; no independent replay.

### T02: If You Want Something, Go and GET It (PDF pp.7–8)
- X: Known manual enumeration and simple HTTP response oracle work
- Question (analyst): How can 3,000+ Windows binaries be tested without manual exhaustion?
- Action: Scale manual routine into scripted enumeration plus callback logging
- Reported observation: Article reports automated identification of additional download-capable executables
- Y: Systematic work becomes reproducible harness functionality
- Basis: author_explicit_reason. Confidence limited to first-party narrative; no independent replay.

### T03: Automated Static Analysis; pp.9–11
- X: Automated binary downloading detection works
- Question (analyst): Does the same approach generalize to previously overlooked execution functionality?
- Action: Broaden binary invocation forms and replace callback oracle with process monitoring
- Reported observation: Publisher reports additional executor-oriented tests and extension to command-line flags
- Y: Original research objective expands into a second capability family
- Basis: author_reported_causal. Confidence limited to first-party narrative; no independent replay.

