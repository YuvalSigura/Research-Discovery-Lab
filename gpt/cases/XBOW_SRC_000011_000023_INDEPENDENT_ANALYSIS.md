# GPT Independent primary-source analysis — SRC-000011 to SRC-000023

**Date:** 2026-10-16. **Status:** first-party article reviewed; provisional and unreviewed; source captures, independent forensic validation, and training approval absent.
**Procedure:** articles opened directly in the 2026-10-16 session, relevant named sections inspected, major X→Y decision moves summarized. Claims remain author-reported unless noted. Unknown chronological/actor/private motives are not reconstructed.

**Attention:** Each item here documents at least one significant question/transition, not a claim of exhaustive reconstruction. Links may include related investigations, not automatic independent samples. This document must not be used as predecision fine-tuning ground truth.

## SRC-000011 — TiTiler — GDAL VRT file-read oracle

- Original: https://xbow.com/blog/xbow-titiler-lfi
- Locator: From URL to Arbitrary File Read in 48 Steps
- **X / known context:** URL-processing COG endpoints discoverable from OpenAPI; initial direct fetch accepted but expected raster/XML format
- **Question:** Can an accepted intermediary format cause the backend to process arbitrary referenced bytes and return observable derivative data?
- **Tests / decision:** Confirm outbound requests; inspect GDAL error; test VRT referencing remote source, switch from bulk PNG pixel output to single-byte histogram in another parallel run
- **Author-reported observation:** Article reports SSRF signal, format failure, VRT accepted, PNG image carrying bytes; independent parallel agent branch combined statistics and pixel offset for single-byte read
- **Y / learning:** Workflow discovery → GDAL format constraints → format-level re-interpretation; two separate parallel runs, do not flatten
- **Limits / counterexamples:** Reported 48-step vs 32-step descriptions refer to differing runs/sections; no full raw logs, author retrospective commentary
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000012 — TiTiler — expression parser RCE

- Original: https://xbow.com/blog/xbow-titiler-rce
- Locator: Reconnaissance and Initial Assessment; Probing the Expression Parser; Out-of-Band Verification
- **X / known context:** OpenAPI exposed URL and band-math expression parameters; early SSRF-to-file attempts blocked by formats
- **Question:** Is the expression parser a restricted evaluator, and which valid input state allows its behavior to be probed?
- **Tests / decision:** Generate valid TIFF after invalid data blocked parser; compare expression errors across endpoints; verify result through independent out-of-band observation
- **Author-reported observation:** Article reports expression evaluation on crop endpoint, OOB callback, and an error-output channel after a prior output-exfiltration attempt failed
- **Y / learning:** Separate prerequisite repair from exploit demonstration; validator is distinct from author inference
- **Limits / counterexamples:** Manual root-cause attribution to numexpr after automated run; no independent artifact replay; relation to same TiTiler product and another separately reported file-read
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000013 — Photo proxy — JavaScript clue

- Original: https://xbow.com/blog/xbow-photo-proxy-lfi
- Locator: How XBOW Turned a JavaScript Hint Into a Working File Inclusion; Vidi veni vici
- **X / known context:** No source code; web JavaScript revealed promising download and avatar/remote-image functionality
- **Question:** After one download endpoint fails repeated path variants, is there a different JavaScript-exposed feature processing URLs?
- **Tests / decision:** Try direct download path techniques; inspect additional JS; test newly identified proxy capability
- **Author-reported observation:** Download candidate repeatedly produced 500; different JS revealed proxy SSRF pathway with reported local-file access
- **Y / learning:** Do not turn repeated HTTP 500s into proof of an existing vulnerability; shift search surface based on new application information
- **Limits / counterexamples:** Few concrete original action traces and no complete alternative chronology; marketing narrative
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000014 — Z-Push — Basic Auth SQLi

- Original: https://xbow.com/blog/xbow-zpush-sqli
- Locator: Mapping the Territory; When Standard Attacks Fall Short; The Breakthrough; Fighting Against Time(outs)
- **X / known context:** Z-Push ActiveSync exposed protected routes and steady responses to typical query/body/header probes
- **Question:** Does an authentication identity field, rather than app endpoint parameters, reach a database expression?
- **Tests / decision:** Compare basic auth username timing after prior endpoint negatives; calibrate validator sleep magnitude against timeout thresholds
- **Author-reported observation:** Publisher reports delayed response on username probe and repeatable dependence on sleep time; validator initially constrained confirmation
- **Y / learning:** Shift from protected feature parameter search to authentication processing; distinguish exploitable hypothesis vs measurement-tool limitations
- **Limits / counterexamples:** No raw latency distributions or independent verification; do not mark other inputs universally safe
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000015 — Salesforce Aura — XSS

- Original: https://xbow.com/blog/xbow-salesforce-xss
- Locator: Initial Reconnaissance; Learning Phase; Aura/Lightning
- **X / known context:** Login redirect identified Experience Cloud, sparse forms and common reflected parameter attempts unproductive
- **Question:** Could framework-specific dynamic Aura components contain input processing beyond visible HTML forms?
- **Tests / decision:** Inspect site framework cues, try common inputs, then pivot to framework-specific endpoints and serialization behavior
- **Author-reported observation:** Publisher reports no obvious reflections in tested common parameters and subsequent Aura-based XSS finding
- **Y / learning:** Transferable transition: generic discovery → stack-aware search → dynamic framework surface; negative tests scoped
- **Limits / counterexamples:** Published edited excerpts; no proof that all site variants affected
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000016 — Akamai CloudTest — SOAP XXE

- Original: https://xbow.com/blog/xbow-akamai-cloudtest-xxe
- Locator: Discovery Phase; SOAP Endpoint Analysis; Refining the Attack
- **X / known context:** Redirect to CloudTest console; SOAP RepositoryService exposed XML parser input
- **Question:** Does SOAP parser resolve external entities, and if yes what observable output channel exists?
- **Tests / decision:** Submit structured XML probes, interpret parser error system-id, then investigate WSDL formatting and error-based output
- **Author-reported observation:** Error disclosed attempted file-path resolution; basic CDATA approach failed, leading to parameter-entity error channel
- **Y / learning:** An error can support a narrow parser-side hypothesis without proving arbitrary readable content; validity of request structure matters
- **Limits / counterexamples:** Some article language equates error with proof; no external reproduction and not all targets show same behavior
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000017 — GlobalProtect — XSS

- Original: https://xbow.com/blog/xbow-globalprotect-xss
- Locator: Initial Exploration; Initial failed attempts; Two paths emerge
- **X / known context:** Login and XML client-rendering flow visible; direct attempts to influence login page variables failed
- **Question:** Can client-consumed XML configuration endpoints carry attacker-influenced values from another input route?
- **Tests / decision:** Inspect client JS and hidden paths; test configuration endpoint and source-to-render behavior
- **Author-reported observation:** Publisher reports successful XSS after tracing alternative endpoints; initial login variables not controllable with direct query
- **Y / learning:** Model should track input reachability and differential client/server rendering, not just payload attempts
- **Limits / counterexamples:** Edited agent excerpts and claims of autonomy unverified outside publisher
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000018 — Zoo-Project — arbitrary file download

- Original: https://xbow.com/blog/xbow-zoo-project-arb
- Locator: Saving Christmas; A Christmas Carol
- **X / known context:** Source code available, cgi-bin and loader service discovered
- **Question:** Can source-review hypothesis about file operation be tested against an explicit benign canary fixture?
- **Tests / decision:** Static inspection of zoo_loader.cgi followed by directed request for planted flag.txt
- **Author-reported observation:** Publisher reports download of fixture and vulnerability; test is targeted to known planted file
- **Y / learning:** Cross-mode static→dynamic proof, deterministic canary oracle; not evidence of broad generalized coverage
- **Limits / counterexamples:** Short article with screenshots rather than full decision log
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000019 — 2FAuth — SVG import stored XSS

- Original: https://xbow.com/blog/xbow-2fauth-xss
- Locator: Breaking Down the Vulnerability; Authentication Workarounds; Refining the Attack
- **X / known context:** Authorized Docker setup with possible icon fetch and QR SVG paths; QR decode failed to demonstrate XSS
- **Question:** Which other import/export feature stores SVG content without sanitization after decoder path failed?
- **Tests / decision:** Inspect auth prerequisite and application controllers; probe QR SVG path; change to migrator/Aegis stored icon path; browser validator
- **Author-reported observation:** Publisher reports Aegis migration stored malicious icon and later XSS validation; early SSRF/icon controls and QR failures scoped
- **Y / learning:** Prerequisite auth work distinct from exploitation; source→storage→browser rendering chain; valid browser oracle
- **Limits / counterexamples:** Related 2FAuth SSRF article may describe distinct campaign; no timeline identity proof
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000020 — EDDI — ZIP and backup path traversal

- Original: https://xbow.com/blog/xbow-eddi-path
- Locator: The Objective; OpenAPI; Exploring Other Endpoints
- **X / known context:** Goal read planted target file; OpenAPI lists backup imports and template/store endpoints
- **Question:** After initial ZIP and template candidates fail, what other file-management path remains untested?
- **Tests / decision:** Test initialBot ZIP handling; explore template endpoint; return to wider backup/import and file path interfaces
- **Author-reported observation:** Publisher reports initial 500 on archive candidate, template restrictions, subsequent file-related search leading to path traversal
- **Y / learning:** Recognize wrong hypothesis vs blocked prerequisite; mixed known goal and open-ended surface choice
- **Limits / counterexamples:** Read-based source report; cannot infer private ranking among alternatives
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000021 — 2FAuth — preview SSRF

- Original: https://xbow.com/blog/xbow-2fauth-ssrf
- Locator: Identifying interesting endpoints; Mixing static and dynamic; Observe Orient Decide Act; Attacking SSRFs
- **X / known context:** Source review shows URI-handling preview; unauthenticated request blocked by login/CSRF prerequisite
- **Question:** Can valid authentication and valid image input produce server-side fetch beyond allowed network boundary?
- **Tests / decision:** Reconstruct legitimate registration/login/CSRF; compare image MIME and no-MIME results; observe callback
- **Author-reported observation:** Initial null/failed preview, then callback after correct input; publisher describes MIME restrictions and subsequent alternate formats
- **Y / learning:** Authenticated prerequisite handling and content-type processing distinct from vulnerability conclusion
- **Limits / counterexamples:** Different related 2FAuth XSS record not necessarily same run; full trace linked not checked
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000022 — Scoold — authentication bypass

- Original: https://xbow.com/blog/xbow-scoold-vuln
- Locator: Initial Code Analysis; Bypassing Authentication
- **X / known context:** JAR disassembly reveals configSet endpoint; 405 and later login requirements block unauthenticated testing
- **Question:** Is 405 a method error or auth control, and do path-normalization variants change the auth interpretation?
- **Tests / decision:** Disassemble code, fuzz endpoint mechanics, compare request normalization variants
- **Author-reported observation:** Publisher reports path semicolon variant changed auth response 401→200 and config access; the earlier stack-overflow interpretation came from description wording
- **Y / learning:** Separate mistaken metaphor-induced hypothesis, discovery of correct boundary, and validation; changed HTTP code alone requires state/action proof
- **Limits / counterexamples:** Edited trace highlights; source says prior false hypotheses, not contemporaneous complete history
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## SRC-000023 — Ninja Tables — WordPress download

- Original: https://xbow.com/blog/xbow-ninja-tables
- Locator: Targeted Reconnaissance; Discovery of a Download Functionality
- **X / known context:** WordPress fingerprint from sitemap, routine filesystem endpoint searches negative
- **Question:** What functionality mentioned in visible application JavaScript could provide a stronger file-read candidate?
- **Tests / decision:** Switch from generic common endpoints to blog / code / JS inspection; investigate ninja_table_force_download url action
- **Author-reported observation:** Publisher shows candidate endpoint and testing iterations leading to file-read report
- **Y / learning:** Distinguish systematic coverage from finding a target-specific capability; workflow→new question triggered by JS
- **Limits / counterexamples:** Excerpted research trace and redacted context; no original full run
- **Assessment:** provisional article-based reconstruction; no predecision ground truth; no training promotion.

## Cross-source provisional notes

These pages reveal systematic discovery intersecting with targeted deep exploration, repairs of prerequisites (MIME/format/auth), measurement-oracle corrections, source-to-dynamic investigation and multiple runs; these are candidate mechanisms, not proven universally useful heuristics.
Do not extract exploit payloads as next-question labels; prioritize state/questions/discriminators/observations and preserve unvisited branches as unknown.
