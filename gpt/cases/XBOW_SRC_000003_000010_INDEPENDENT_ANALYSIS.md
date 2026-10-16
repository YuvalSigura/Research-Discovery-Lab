# RDL independent primary-source analysis: SRC-000003–SRC-000010

Date: 2026-10-16. Status: **provisional and unreviewed**. Eight first-party articles read and source sections identified; no publisher source capture SHA, no independent corroboration, no historical pre-decision knowledge certification, no rights approval, no fine-tuning-ready samples. This is not an original private research transcript.

**Analysis target:** trace the *question at X → selected experiment → reported observation → explicit or possible cause of pivot → state Y*. Author-reported motivation is separated from independently recorded motivation. No unsupported historical day-by-day timeline is filled in. All notes below are paraphrases.

## SRC-000003 — No Time to Pwn: Linux kernel CVE-2026-72018

Source: https://xbow.com/blog/no-time-to-pwn-cve-2026-72018 ; publisher XBOW; see sections **From “unexploitable” to root access**, **Exploit Strategy**, **Reliability**, **Autonomy and the research frontier**.

**Question 1:** Could an obscure SMC-D bug become a realistic local privilege-escalation scenario? **X:** Agent initially evaluated a hardware-oriented threat model; local use appeared blocked by a field fixed to zero. **Trial/obstacle:** Agent considered packet modification but discarded it as expensive; source says a human reviewer recognized the abandoned idea in the agent's trace and explicitly asked to test it. **Y:** A local model became testable. **Causality:** Intervention is *author reported*; complete original trace and exact decision times were not independently verified. **Learning:** Stopping when a prerequisite looks fixed can miss a cheaper way to change the experimental setup; avoiding costly experiments is often rational, not proof of impossibility.

**Question 2:** What are the actual constraints of the available write primitive? **X:** Agent repeatedly reasoned as though it had a general write primitive from another configuration. **Experiment:** Human demanded direct validation. **Observation:** Publisher reports the local primitive was only a constrained zero-write. **Y:** Agent relinquished the stronger assumption. **Causality:** Explicitly narrated by author. **Learning:** Revalidate experimental affordances rather than propagating outdated context assumptions.

**Question 3:** Must an agent amplify a primitive before pursuing its objective? **X:** Agent explored stronger primitives. **Instruction:** Human reframed the question to whether existing limited behavior was sufficient. **Y:** The team reports finding a viable target and a working constrained demonstration. **Reliability:** 22 of 100 boots in a mitigations-disabled setup, according to publication; not evidence of general deployment reliability. **Training risk:** Do not confuse publication's exploit implementation detail with universally appropriate test choice or omission of alternatives.

## SRC-000004 — A Shell Is Worth a Thousand Images: Bing Images

Source: https://xbow.com/blog/bing-images-rce-vulnerabilities ; see **Following the trace**, **From SVG to command execution**, **Proof**.

**Question 1:** What actually processes user-controlled bytes after an apparently normal image fetch? **X:** Blind server-side fetch looked like expected product behavior. **Signal:** Backend-dependent HTTP 500 and out-of-band fetch observations. **Y:** Research continued deeper into parsing instead of dismissing the signal. **Basis:** Publisher-retrospective cause.

**Question 2:** Is the observed behavior XML entity expansion or image rendering? **X:** Parser errors were compatible with several hypotheses. **Discriminator:** Compare tests of external XML features against ordinary SVG references. **Observation:** Publisher reports negative XXE-specific results but positive renderer image-reference fetches. **Y:** Search shifted to renderer/coder/delegate surface. **Epistemic limit:** Tested negative probes do not universally refute XXE.

**Question 3:** What downstream helper handles data? **Approach:** Differential image-processing behavior and representative *cleaned* trace. **Y:** Publisher reports two Bing image-ingestion paths reaching unsafe delegates and code execution. **Do not conflate:** This page also names a separate Microsoft Devices Pricing Program vulnerability; all three are not one continuous exploit.

## SRC-000005 — Dead.Letter: Exim CVE-2026-45185

Source: https://xbow.com/blog/dead-letter-cve-2026-45185-xbow-found-rce-exim ; see **Setting the challenge**, **Running the race**, **Special Delivery**, **Timeline**.

**Question 1:** Report a high-impact issue before completing an exploit, or delay disclosure to build proof? **X:** The team assessed a potentially impactful finding. **Decision:** Send report first; author explicitly describes this choice, not a machine-determined experimental result. **Y:** Maintainer response and an impending public fix set a time-limited opportunity. **Why:** Risk-management and disclosure constraints, not a falsified vulnerability.

**Question 2:** How do human-assisted and autonomous-agent exploit investigations diverge under the same deadline? **X:** After disclosure, roughly seven-day window. **Experiment:** Two *parallel* branches: named human researcher working with assistant vs XBOW Native team using incremental stages with changing hardening conditions. **Observation:** Article reports early progress by the agent branch; author's description of internal AI work partly relies on the AI's later explanation. **Y:** Parallel experiment outcomes—not a single linear researcher trajectory. **Caution:** Compare budgets, hints and actual run logs before making human-versus-agent effectiveness claims.

## SRC-000006 — Three Microsoft RCE announcement

Source: https://xbow.com/blog/three-rce-vulnerabilities-in-microsoft-identified-xbow ; see **announcement** and **disclosure-withholding paragraph**.

**Coverage:** Names three Microsoft CVEs and author-reported autonomous discovery but explicitly withholds technical mechanics. **Research question / X→Y:** Not recoverable from this announcement. **Action:** Link as supporting publisher-disclosure artifact to detailed SRC-000004, but do not double-count investigations or manufacture decisions. **Fine-tuning suitability:** Not a stand-alone decision trajectory.

## SRC-000007 — Spree IDOR trace excerpts

Source: https://xbow.com/blog/tales-from-the-trace-how-xbow-reasons-its-way-into-finding-idors ; see **Finding 1** chapters and **Finding 2** chapters.

**Finding 1, Q1:** Where are the resources containing address data? **X:** `/user/edit` exposed password-related elements, direct routes had 502/timeouts. **Choice:** Use authenticated visual navigation and network inspection to discover actual address paths. **Y:** Identifiers for testing ownership. **Basis:** Selected first-person agent excerpts reproduced by publisher; full trace unavailable.

**Finding 1, Q2:** Does a 403 under one authentication context mean access control is secure under all contexts? **X:** Cross-object access with session yielded 403. **Experiment:** Test same kind of resource without credentials. **Observation:** Author reports a successful unauthenticated response containing address fields from a test account. **Y:** Candidate unauthorized access finding. **Critical lesson:** An observed denial is scoped to that principal and state; it does not decide another identity state.

**Finding 2, Q3:** What baseline is necessary to distinguish cross-object read from malformed request? **X:** Checkout API calls without an order token returned 404/routing failures. **Choice:** Create separate cart A and cart B with independent tokens, then compare ownership constraints. **Y:** Author reports cross-cart address reference worked. **Warning:** Findings 1 and 2 are separate paths; do not merge them into one experiment chain. Excerpted PII is excluded from these notes.

## SRC-000008 — Chef Automate SQL Injection

Source: https://xbow.com/blog/cooking-an-sql-injection-vulnerability-in-chef-automate ; see **Discovery Process**, **Vulnerability Analysis**, **Exploitation Verification**.

**Q1:** How can inaccessible compliance APIs be examined? **X:** Recon identified API paths returning authentication errors. **Author-reported observation:** Agent knew a default collector credential from prior knowledge, obtained access. **Y:** A newly reachable search endpoint for analysis. **Warning:** Don't include credentials in training examples, and don't assume prior knowledge was learned during this investigation.

**Q2:** Which structured field can influence SQL? **X:** API schema was unclear; endpoint error messages revealed required JSON structure. **Experiment:** Compare fields; some payload locations uninteresting, changing `type` produced database errors. **Y:** Targeted hypothesis about database query building. **Caution:** Uninteresting tested fields are not globally proven safe.

**Q3:** How to distinguish SQL interpretation from generic HTTP error? **Experiment:** Published time-delay comparison. **Observation:** Publisher reports differentiated delays supporting SQL injection. **Y:** Validated within published tests and disclosed. **Unknown:** Raw measurements, controls and original request traces.

## SRC-000009 — Apache Druid management proxy SSRF

Source: https://xbow.com/blog/apache-druid-proxy ; see **research narrative**.

**Q1:** Do historical SSRF paths remain viable in this installation? **X:** Prior CVEs suggested endpoints worth checking. **Experiments:** Test earlier endpoint candidates. **Result:** Publisher says no relevant behavior; some components were not configured. **Y:** Reframe search. **Important:** A disabled/unconfigured component is a blocked prerequisite, not refutation of the vulnerability class.

**Q2:** Are there other built-in extensibility/proxy capabilities? **Action:** Explore extensions and management proxy. **Observation:** An error indicated proxy presence; author reports further iterations yielded an SSRF. **Y:** New proxy-focused line of research. **Unknown:** Full trace and intermediate comparisons are not included in article text.

## SRC-000010 — Geolocation failure to SQL injection

Source: https://xbow.com/blog/xbow-geolocation-sqli ; see **Bypassing geolocation restriction**, **Digital Nomad**.

**Q1:** Can a geofenced web feature be made accessible? **X:** App gate prevented ordinary navigation. **Experiments:** Alternate request context, user-agent and discovery routes. **Observation:** Multiple negative tests. **Y:** Search refocused on still-reachable application behavior. **Caution:** Results do not prove all geofence bypasses impossible.

**Q2:** Does anomalous behavior in a remaining endpoint indicate a deeper issue? **Action:** Explore request parameters and cookies. **Observation:** HTTP 500 under certain cookie values, followed by comparative timing tests. **Y:** Publisher reports blind SQL injection confirmation. **Caution:** A 500 alone is not proof; raw timing samples are absent.

## Cross-case training themes (hypotheses; NOT certified training examples)

1. `X→Y` moves can depend on a **human override of a rational agent heuristic** (003), not solely a discovered exploit primitive.
2. Failed or negative tests matter only within the exact **tested scope and assumptions** (004, 008, 009, 010).
3. Build **valid prerequisite state** before treating an error as an authorization boundary (007).
4. Multi-researcher parallel execution and later retrospective reconstruction are different things (005).
5. A disclosure-only article cannot supply nonexistent research trajectories (006).
6. Avoid lineage duplication for Microsoft CVEs described in both 004 and 006.

**Next validation gates:** immutable source captures and hash, independent source checks, access to complete traces where possible, lineage adjudication, source rights, blinded next-step evaluation without information from Y leaking into X.