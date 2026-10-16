# Source-specific deeper reading: SRC-000073–SRC-000082

2026-10-16 · **Only original first-party webpages used**. This review adds decision/event granularities that were absent from the initial 109-item bounded audit, without redefining all articles as histories of one serial process. All transitions are prospective *analytical candidates*, with the research question our wording unless explicitly quoted. Historic `known_at` unavailable; no training approval.

Broad source lesson types include strategic topic choice, gaining realistic environmental prerequisites, false positive measurement correction, methodology, cloud identity, user interface behavior, and short advisories.

## SRC-000073: first-person strategic research planning

- Source: https://portswigger.net/research/how-i-choose-a-security-research-topic
- Actors: James Kettle

### Candidate T01 — Fast failure
- X: Initial proposed concept required heavy investment
- Research question, analyst phrased: Can a cheap realistic fixture reject an idea before spending weeks?
- Reported action/test: Create a realistic purpose-built proof website to test concept viability
- Reported observation: Author found original concept extremely unrealistic
- Y or stated strategy criterion: Abandon first concept rapidly
- Basis: author_explicit_motive; independent verification absent.

### Candidate T02 — Fast failure
- X: Second concept showed enough promise to continue
- Research question, analyst phrased: Is marginal progress worth six weeks of work?
- Reported action/test: Continue tests and observe resulting research yield
- Reported observation: Author reports second concept eventually flopped after six weeks
- Y or stated strategy criterion: Abandon second concept despite sunk cost
- Basis: author_explicit_stop; independent verification absent.

### Candidate T03 — Fast failure
- X: Third topic had to be selected under risk of failure
- Research question, analyst phrased: Can existing tooling make a previously distant research area cheap to explore?
- Reported action/test: Assess race-condition tooling reusable from earlier project
- Reported observation: Author estimated one day porting plus 1–2 weeks testing and found a high-impact issue in under a week
- Y or stated strategy criterion: Commit to race condition research
- Basis: author_explicit_motive; independent verification absent.

### Candidate T04 — Direct impact vs audience impact
- X: Researcher contemplates topic impact
- Research question, analyst phrased: Does high direct impact translate into useful results for the audience?
- Reported action/test: Compare hypothetical one-vendor CDN exploit with method audience can reuse
- Reported observation: Author favors reusable methodology and tools over single-vendor war story
- Y or stated strategy criterion: Selection criterion: audience transferability affects research choice
- Basis: author_stated_criterion; independent verification absent.

### Candidate T05 — Existing skill-sets vs personal development
- X: Long period specializing in HTTP smuggling
- Research question, analyst phrased: Could specialization reduce future options even when current topic remains fruitful?
- Reported action/test: Evaluate long-term skills and diverse foundations
- Reported observation: Author deliberately chose race conditions partly for skill diversification
- Y or stated strategy criterion: Strategic objective includes future learning, not only short-term vulnerability yield
- Basis: author_stated_criterion; independent verification absent.

## SRC-000074: first-person infrastructure research and restraint

- Source: https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/
- Actors: watchTowr Benjamin Harris and Aliz Hammond

### Candidate T01 — Setting The Scene
- X: WHOIS test server caused a client crash under lab-controlled responses
- Research question, analyst phrased: What real-world precondition gives attacker legitimate-looking control over a WHOIS response?
- Reported action/test: Challenge existing lab redirect with MITM, server ownership and referral prerequisites
- Reported observation: Team recognizes the realistic preconditions are difficult
- Y or stated strategy criterion: Search for an alternative authority pathway instead of prematurely claiming remote impact
- Basis: author_explicit_question; independent verification absent.

### Candidate T02 — Collateral Damage In Pursuit Of RCE; So What? It's Old
- X: WHOIS clients may hardcode outdated upstream server addresses
- Research question, analyst phrased: Are previously authoritative server domains still queried after migration?
- Reported action/test: Identify an expired old `.mobi` authoritative hostname, acquire it and log WHOIS requests
- Reported observation: Authors report real inbound queries from many outdated clients
- Y or stated strategy criterion: Remote server response control is now plausible for a bounded subset of stale clients
- Basis: author_reported_test; independent verification absent.

### Candidate T03 — Prior Art; Reality check
- X: Controlled WHOIS server receives production queries
- Research question, analyst phrased: Could known client-side vulnerabilities be triggered by this response origin?
- Reported action/test: Study prior CVEs in WHOIS clients, reproduce selected historical issue in a lab
- Reported observation: Authors report a known PHP WHOIS bug can be reproduced but practical targets uncertain
- Y or stated strategy criterion: Narrow claims to vulnerable old clients and attack prerequisites
- Basis: author_reported_test; independent verification absent.

### Candidate T04 — Certificate authority validation testing
- X: Trust in WHOIS metadata is potentially reused by CAs
- Research question, analyst phrased: Could a CA validation UI use the deprecated server for domain contact proof?
- Reported action/test: Try a fictitious test domain at a certificate provider
- Reported observation: Initial provider does not display attacker-controlled contact, a negative signal
- Y or stated strategy criterion: Consider that response-format mismatch or provider-specific implementation could hide effect
- Basis: author_explicit_pivot; independent verification absent.

### Candidate T05 — GlobalSign; We stopped before issuing
- X: One provider produces missing record rather than controlled email
- Research question, analyst phrased: Is a WHOIS syntax/parser mismatch masking continued queries to old server?
- Reported action/test: Try existing domain with representative legitimate WHOIS formatting, change controlled server response
- Reported observation: Author reports a provider then presented controlled email as domain-contact verification choice
- Y or stated strategy criterion: Observed chosen validation method, not actual certificate issue; deliberately stop
- Basis: author_explicit_stop; independent verification absent.

## SRC-000075: technical multi-flaw first-party study

- Source: https://www.slcyber.io/research/chaining-three-bugs-to-access-all-your-servicenow-data
- Actors: Original Assetnote/now Searchlight Cyber researchers

### Candidate T01 — Introduction; three vulnerability sections
- X: ServiceNow holds sensitive multitenant workflows and contains complex authorization routing
- Research question, analyst phrased: What boundaries tie a client-controlled request to a particular tenant and data record?
- Reported action/test: Examine application routes and authorization behavior in source-reported technical analysis
- Reported observation: Publisher documents three interlocking issues leading to broad data access
- Y or stated strategy criterion: Present a chain of tested capabilities; exact historical order of discovery not established
- Basis: author_reported_mechanism; independent verification absent.

## SRC-000076: false positive correction and vendor dialogue

- Source: https://www.stingrai.io/blog/the-perils-of-premature-vulnerability-reporting-a-case-study-in-off-by-one
- Actors: Stingrai/Arafat Afzalzada

### Candidate T01 — The Initial Discovery
- X: OpenVAS GSS buffer allocation uses +3 and +4 constants
- Research question, analyst phrased: Do constants omit null terminator and create a one-byte overwrite?
- Reported action/test: Count separator characters and hypothesize mistaken length calculations
- Reported observation: Early analysis incorrectly classifies candidate overflow
- Y or stated strategy criterion: Construct empirical checks instead of treating arithmetic concern as proof
- Basis: author_reported_hypothesis; independent verification absent.

### Candidate T02 — The False Positive: Understanding What Went Wrong
- X: An apparent AddressSanitizer signal reinforces candidate issue
- Research question, analyst phrased: Did ASan catch the production sprintf out of bounds or only the testing code reading OOB?
- Reported action/test: Add buffer canaries and track exactly which program statement generated ASan violation
- Reported observation: Publisher reports sprintf wrote terminator within allocation; test code itself read past end
- Y or stated strategy criterion: Withdraw overflow claim; ASan behavior reinterpreted as test-harness artifact
- Basis: author_reported_test; independent verification absent.

### Candidate T03 — Lessons Learned; Conclusion
- X: Developer intent behind magic constants not documented in source
- Research question, analyst phrased: How should a vendor explanation affect scientific confidence?
- Reported action/test: Combine vendor allocation explanation with independent string arithmetic and canary testing
- Reported observation: Explanations reconciled with test results across lengths
- Y or stated strategy criterion: Report false positive within code scope and preserve the correction
- Basis: author_reported_correction; independent verification absent.

## SRC-000077: aggregate methodology and author-reported results

- Source: https://github.blog/security/how-to-scan-for-vulnerabilities-with-github-security-labs-open-source-ai-powered-framework/
- Actors: GitHub Security Lab authors and AI framework

### Candidate T01 — Methodology; What we learned
- X: Need a broad audit method over diverse repositories
- Research question, analyst phrased: Can explicit threat models create better scoped and interpretable vulnerability hypotheses?
- Reported action/test: Generate proposals by application components, entry points and intended usage
- Reported observation: Publisher reports 1003 proposals over >40 repositories
- Y or stated strategy criterion: Structured candidate-generation phase for later adversarial audit
- Basis: published_methodology; independent verification absent.

### Candidate T02 — What we learned
- X: Candidate generation yields many unverified issues
- Research question, analyst phrased: Which candidate issues cross real security boundaries after independent audit and human reproduction?
- Reported action/test: AI audit flags 139, dedup leaves 91; analysts reject 20 unreproduced and 52 low severity
- Reported observation: 19 issues retained for reporting, publisher aggregate
- Y or stated strategy criterion: Need separate scope, impact and reproducibility judgments; none are 1003 independently validated bugs
- Basis: published_aggregate_result; independent verification absent.

## SRC-000078: first-person negative research audit

- Source: https://securitylab.github.com/research/Fail2exploit/
- Actors: Kevin Backhouse GitHub Security Lab

### Candidate T01 — SQL injection and command injection sections; Conclusion
- X: Fail2ban has configured log and SQL-related processing
- Research question, analyst phrased: Do suspected parser and injection behavior yield a reportable exploit under realistic privileges?
- Reported action/test: Review implementation, experiment on specific attack surfaces and account for deployment prerequisites
- Reported observation: Author reports several interesting effects but no reportable findings in tested configurations
- Y or stated strategy criterion: Narrow conclusions to actual prerequisites and tested deployment, not global product safety
- Basis: author_reported_negative; independent verification absent.

## SRC-000079: cloud architecture and pipeline privilege study

- Source: https://orca.security/resources/blog/azure-machine-learning-privilege-escalation/
- Actors: Orca original security research

### Candidate T01 — Cloud pipeline architecture and finding sections
- X: Azure ML automated pipelines run workloads with managed identities and project permissions
- Research question, analyst phrased: Can user-influenced pipeline state affect operations with a higher service identity?
- Reported action/test: Inspect documented ML resource and identity architecture; author reports boundary tests
- Reported observation: Publisher describes a privilege-escalation path through pipeline service permissions
- Y or stated strategy criterion: Record role assumptions, target identity and authorization prerequisites separately
- Basis: author_reported_mechanism; independent verification absent.

## SRC-000080: first-person unexpected maintenance finding

- Source: https://portswigger.net/research/bypassing-csp-with-dangling-iframes
- Actors: Gareth Heyes

### Candidate T01 — Introduction
- X: Security Academy CSP lab used a background attribute trick
- Research question, analyst phrased: Why did routine Chrome 97 lab update break a previous method?
- Reported action/test: Try alternative attributes and CSS timing manipulations
- Reported observation: Author says multiple variants failed
- Y or stated strategy criterion: Stop repeated same-class tweaking and reconsider underlying CSP and browser behavior
- Basis: author_explicit_pivot; independent verification absent.

### Candidate T02 — Cross domain iframe issues
- X: No simple replacement for old dangling markup technique
- Research question, analyst phrased: What cross-origin iframe properties are observable even across domains?
- Reported action/test: Run own Hackability inspector and vary nested iframe names
- Reported observation: Author sees existence check for iframe name but cannot enumerate arbitrary token
- Y or stated strategy criterion: Explore iframe state changes rather than brute-force names
- Basis: author_reported_test; independent verification absent.

### Candidate T03 — Cross domain iframe issues; Conclusion
- X: Cross-domain iframe read seems forbidden by same-origin policy
- Research question, analyst phrased: Can changing iframe location to about:blank change the effective object origin/visibility?
- Reported action/test: Change nested iframe navigation and inspect frame objects and names
- Reported observation: Author reports readable name and ability to access changed origin frame
- Y or stated strategy criterion: New way to complete original CSP lab under Chrome97 restrictions
- Basis: author_reported_causal; independent verification absent.

## SRC-000081: service-account permissions and artifact trust

- Source: https://orca.security/resources/blog/bad-build-google-cloud-build-potential-supply-chain-attack-vulnerability/
- Actors: Orca original cloud researchers

### Candidate T01 — Default service-account permissions; impact
- X: Build pipelines receive default service identities and materialize code into artifacts
- Research question, analyst phrased: Does a build action cross least-privilege boundary to another project's artifact or code namespace?
- Reported action/test: Analyze default IAM scope and artifact ingestion under related build operations
- Reported observation: Publisher reports potential supply-chain consequences under described setup
- Y or stated strategy criterion: Future lab research must distinguish policy defaults from selected per-project access settings
- Basis: author_reported_mechanism; independent verification absent.

## SRC-000082: short advisory patch-followup

- Source: https://securitylab.github.com/advisories/GHSL-2024-069_ngrinder/
- Actors: GitHub Security Lab advisory

### Candidate T01 — Affected component; advisory description
- X: Earlier bug report and patch exist on YAML processing
- Research question, analyst phrased: Did the remediation cover all relevant deserialization entry paths?
- Reported action/test: Review affected code and report remaining unsafe input path
- Reported observation: Advisory records a second vulnerable condition and report dates
- Y or stated strategy criterion: A short advisory can support technical residual risk but not reconstruct original ideation chronology
- Basis: advisory_scope_only; independent verification absent.

## Scientific limits

- `SRC-000073` includes **topic selection criteria**; these are not automatically experiments in its target application.
- `SRC-000074` stopped *before* certificate issuance; a provider's observed email option must not be upgraded to completed certificate compromise.
- `SRC-000075`, `079`, `081`, `082` lack full thought traces; technical mechanism alone does not prove why the investigator looked there.
- `SRC-000076` uses researcher-owned test code that produced an ASan signal; preserve code-under-test identity in evidence.
- `SRC-000077` totals across many repos are not single-investigation step logs.
- `SRC-000080` routine maintenance actually supplied an unplanned bug-research trigger; no need to invent it.

