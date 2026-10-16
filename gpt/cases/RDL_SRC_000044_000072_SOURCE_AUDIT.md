# Independent research source audit: SRC-000044–SRC-000072

Prepared 2026-10-16. **Crucial status semantics:** `article_inspected` means relevant sections of original public publisher article read (not full archival review). `article_opened_bounded` means publication confirmed but detailed scientific reconstruction not done. `landing_only` means actual research body was not returned. `inaccessible` means redirected URL was unavailable. This is not a set of 29 full investigations.
All findings are unpublished/retrospective author statements unless specifically stated otherwise; rights and historical known-at unavailable; 0 training eligible.

## SRC-000044 — PAN-OS Nginx/Apache path confusion

- Source: https://www.assetnote.io/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os
- Access/evidence: **inaccessible**. Canonical Assetnote redirects to slcyber URL currently inaccessible in live retrieval.
- Research question, if supported, or limitation: Question from title only: whether differing web-server path handling crosses authorization boundary; no historical X→Y verified.
- Research intelligence / epistemic caveat: Cannot reconstruct original tests or decisions.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000045 — Next.js middleware bypass due diligence

- Source: https://www.assetnote.io/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927
- Access/evidence: **inaccessible**. Publisher redirect target currently inaccessible.
- Research question, if supported, or limitation: Follow-up question from title only: what does independent due diligence add to a known middleware-bypass report? No specific actions verified.
- Research intelligence / epistemic caveat: Do not fabricate exploitation chronology.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000046 — Sitecore validation order

- Source: https://www.assetnote.io/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x
- Access/evidence: **article_inspected**. Section: Finding an Order of Operations bug in Sitecore and Practical Exploitation in the Wild
- Research question, if supported, or limitation: When does path normalization/security filtering run relative to later string transformations, and what prerequisites exist for practical file disclosure?
- Research intelligence / epistemic caveat: Article demonstrates code-level checks before later transformation, then path-leak-or-guess prerequisite for live exploit; technical mechanism and deployed prerequisite are separate decisions.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000047 — Ivanti SAML second auth bypass

- Source: https://www.slcyber.io/research/ivantis-pulse-connect-secure-auth-bypass-round-two
- Access/evidence: **article_inspected**. Where to Start? Finding the SAML Server; Finding the SSRF
- Research question, if supported, or limitation: Vendor advisory limited search to SAML; binary wrapper endpoint analysis stalled; researchers switched to configuring SAML VM for valid samples, then error-string search found saml-server and prior-art KeyInfo advisory led to SSRF.
- Research intelligence / epistemic caveat: Strong first-person explicit strategy change and self-critique (filesystem search could have been earlier); chain previous disclosure assumptions separate from new research.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000048 — Ivanti high-signal auth bypass

- Source: https://www.assetnote.io/resources/research/high-signal-detection-and-exploitation-of-ivantis-pulse-connect-secure-auth-bypass-rce/
- Access/evidence: **article_opened_bounded**. Original Assetnote redirects to slcyber article; open confirms source and title.
- Research question, if supported, or limitation: Research target: validate and detect existing Ivanti auth bypass and RCE with low false positives; no detailed historical transition independently extracted in this pass.
- Research intelligence / epistemic caveat: Do not treat previous two Ivanti posts as same event without lineage reconciliation.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000049 — Next.js SSRF advisory

- Source: https://www.assetnote.io/resources/research/advisory-next-js-ssrf-cve-2024-34351
- Access/evidence: **article_opened_bounded**. Original Assetnote redirects to slcyber advisory.
- Research question, if supported, or limitation: Source genre advisory: mechanism, impact, fix information may be extractable; original researcher's decision sequence unverified.
- Research intelligence / epistemic caveat: Advisory cannot stand as full decision diary.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000050 — Citrix DoS CVE analysis

- Source: https://www.assetnote.io/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534
- Access/evidence: **article_opened_bounded**. Original Assetnote redirects to slcyber technical analysis.
- Research question, if supported, or limitation: Potential comparative question: does error/crash validate controlled impact or merely local fault? No completed source-specific decision trace in pass.
- Research intelligence / epistemic caveat: Technical reproduction may study issue after someone else's discovery; verify lineage.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000051 — Pentera value problem of AI

- Source: https://pentera.io/resources/research/what-ai-cannot-decide-for-us/
- Access/evidence: **article_inspected**. Arrow and Gibbard-Satterthwaite social-choice limits are presented as limits of universal value aggregation.
- Research question, if supported, or limitation: Philosophical/mathematical argument: choosing values and objectives cannot be delegated to mere optimization without assumptions.
- Research intelligence / epistemic caveat: Not an experimental security research trajectory; carefully distinguish theorem premise from architecture recommendation.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000052 — Pentera behavioral frontier

- Source: https://pentera.io/resources/research/what-ai-cannot-predict-or-verify/
- Access/evidence: **article_inspected**. Halting problem / Rice / Busy Beaver framing: some universal behavioral decision problems are undecidable.
- Research question, if supported, or limitation: This does not prove particular finite dynamic test unreliable; avoid conflating universal formal impossibility with empirical test performance.
- Research intelligence / epistemic caveat: Theory article, no historical bug investigation.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000053 — Pentera information ceiling

- Source: https://pentera.io/resources/research/what-ai-cannot-learn-universally/
- Access/evidence: **article_inspected**. No Free Lunch and other results applied to hypothetical universal learner.
- Research question, if supported, or limitation: Generalization assumes task distribution and inductive bias; no distribution-free guarantee is not proof models cannot generalize usefully.
- Research intelligence / epistemic caveat: Theorem analysis, not empirical failure of a particular research agent.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000054 — Pentera self-reference

- Source: https://pentera.io/resources/research/mathematical-limits-of-ai/
- Access/evidence: **article_inspected**. Gödel, Löb, Tarski etc used to examine complete self-proof/self-truth claims.
- Research question, if supported, or limitation: Separate limits of fully general formal systems from practical external verifier with bounded evidence.
- Research intelligence / epistemic caveat: No human investigator X→Y case.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000055 — CyberPanel ShadowPanel

- Source: https://pentera.io/resources/research/pre-auth-rce-chain-cyberpanel/
- Access/evidence: **article_inspected**. The Trigger; Enter CyberPanel: widely reported cPanel incident inspired variant search in related control-plane product; central middleware suggested a single weak boundary with large consequence.
- Research question, if supported, or limitation: Explicit novelty trigger from external incident to a different product; 3-piece chain reportedly uses two bugs plus legitimate cronjob feature.
- Research intelligence / epistemic caveat: Distinguish analogous-product hypothesis, proven issues, legitimate-feature leverage, and author-reported impact.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000056 — Claude double-agent cross-service chain

- Source: https://pentera.io/resources/research/ai-double-agent-claude/
- Access/evidence: **article_inspected**. The backstory: another investigation led to a compromised email aggregator, and researchers asked what inbox access could imply for connected AI account preferences.
- Research question, if supported, or limitation: Multi-identity, multi-provider pivot: source data to downstream account setting control then local agent/extension action.
- Research intelligence / epistemic caveat: Explicitly track consent scope and all actors. This is author-reported chain, not proof of common default configurations.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000057 — AWS SSM shared-document trust

- Source: https://pentera.io/resources/research/ssm-cross-account-sharing/
- Access/evidence: **article_inspected**. TL;DR; Background: shared SSM documents appear under Shared with me, without explicit acceptance; executing one enables owner-controlled behavior.
- Research question, if supported, or limitation: Research question: does UI trust signal correspond to provenance/authorization of executable shared artifacts?
- Research intelligence / epistemic caveat: Security concern is trust/consent gap; no evidence a shared document executes automatically.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000058 — Podman WebView world-view

- Source: https://pentera.io/resources/research/podmans-webview/
- Access/evidence: **article_inspected**. TL;DR: service assumed local bound to all interfaces; Referer check and errors extend risk.
- Research question, if supported, or limitation: Question: is a desktop helper really confined to localhost or can an unauthenticated network peer reach it?
- Research intelligence / epistemic caveat: Separate network reachability, authorization check and observed resource-exhaustion effect; preserve environment-dependent exposure.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000059 — Gmail–Drive integration trust gap

- Source: https://pentera.io/resources/research/integration-flaws-gmail-google-drive/
- Access/evidence: **article_inspected**. Executive Summary: malware blocks and scanner trust seals behave differently across Gmail and Drive integration.
- Research question, if supported, or limitation: Question: are content-security verdicts consistent when moving through independent product pipelines and relying on external origin labels?
- Research intelligence / epistemic caveat: This describes two separate architectural logic flaws, not necessarily one continuous exploit; vendor observation still first-party.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000060 — LOLBins reverse engineering at machine speed

- Source: https://pentera.io/resources/research/ai-assisted-reverse-engineering-lolbins/
- Access/evidence: **article_inspected**. From a Simple Task to a Bigger Question; Old-School LOLBins Hunting; Moving to Automation: original product feature assignment introduced question whether new LOLBins can be found automatically.
- Research question, if supported, or limitation: Researcher manually reverse engineered known utilities first, traced syscall argument provenance, then assigned AI a narrow judgment about origin of execution arguments.
- Research intelligence / epistemic caveat: Exceptionally explicit workflow→unplanned research question; separate manual ground truth, automated collection and AI analysis; published model performance requires validation.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000061 — Exposed training apps as cloud pivots

- Source: https://pentera.io/resources/research/exposed-cloud-training-apps-pentera-labs/
- Access/evidence: **article_inspected**. TL;DR: intentionally vulnerable training apps externally reachable; authors report cloud impact and in-the-wild indicators, built SigInt to fingerprint/validate exposure.
- Research question, if supported, or limitation: Question: is a seemingly low-value demo/test app connected to high-privilege cloud identity or sensitive corporate systems?
- Research intelligence / epistemic caveat: Preserve legal authorized validation and independent indicators; a publicly reachable demo is not automatically a valid enterprise compromise.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000062 — Kubernetes ingress injection vectors

- Source: https://pentera.io/resources/research/ingress-nightmare/
- Access/evidence: **landing_only**. The retrieved page exposed only title and generic site footer; no research methods available in capture.
- Research question, if supported, or limitation: Potential research question from title unverified; cannot reconstruct attempts.
- Research intelligence / epistemic caveat: Requires alternate publisher content/capture.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000063 — AWS SSM hybrid landscapes

- Source: https://pentera.io/resources/research/risks-of-aws-ssm-in-hybrid-landscapes/
- Access/evidence: **landing_only**. Retrieved document did not expose research body reliably in this pass.
- Research question, if supported, or limitation: Title suggests hybrid SSM trust boundaries; do not treat such inference as actual historical question.
- Research intelligence / epistemic caveat: No source-supported X→Y.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000064 — FortiClient VPN zero days

- Source: https://pentera.io/resources/research/two-zero-days-forticlient-vpn-2024/
- Access/evidence: **landing_only**. Retrieved 181-line page exposed site navigation/footer rather than research body.
- Research question, if supported, or limitation: Known from title only: two issues announced; discovery pathway unknown.
- Research intelligence / epistemic caveat: No reconstruction permitted.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000065 — AD SID DoS

- Source: https://pentera.io/resources/research/dos-attack-active-directory-sid-exploitation/
- Access/evidence: **landing_only**. Site produced a headline and generic lead form only.
- Research question, if supported, or limitation: No original technique evidence retrieved; cannot know question/test sequence.
- Research intelligence / epistemic caveat: Do not infer attack methodology from title.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000066 — Remote memory reflective loading

- Source: https://pentera.io/resources/research/reflective-loading-with-remote-memory-interactions/
- Access/evidence: **landing_only**. Retrieved page was generic content/navigation.
- Research question, if supported, or limitation: No source-supported historical questions or decision transitions.
- Research intelligence / epistemic caveat: Require raw paper or canonical source.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000067 — DevalScript

- Source: https://pentera.io/resources/research/devalscript-the-language-of-processes/
- Access/evidence: **landing_only**. Retrieved page contained site chrome without substantive paper.
- Research question, if supported, or limitation: The title names a language/process idea, not evidence of a research chain.
- Research intelligence / epistemic caveat: Unknown.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000068 — WebLogic post-exploitation

- Source: https://pentera.io/resources/research/not-another-weblogic-exploitation-how-to-prevent-rce/
- Access/evidence: **landing_only**. Only heading and generic site footer visible.
- Research question, if supported, or limitation: No source-supported choice or experiment can be claimed.
- Research intelligence / epistemic caveat: Unknown.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000069 — LOLBAS Odyssey

- Source: https://pentera.io/resources/research/the-lolbas-odyssey-finding-new-lolbas-and-how-you-can-too/
- Access/evidence: **landing_only**. Retrieved article body unavailable in current scrape.
- Research question, if supported, or limitation: Do not merge with distinct 2026 LOLBin study as an identical research lineage without evidence.
- Research intelligence / epistemic caveat: Unknown.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000070 — Neglected network protocols

- Source: https://pentera.io/resources/research/death-by-default-neglected-network-protocols-you-should-know/
- Access/evidence: **landing_only**. Site body not available in current scrape.
- Research question, if supported, or limitation: Title offers possible discovery domain; no observed experiments.
- Research intelligence / epistemic caveat: Unknown.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000071 — TDS version detection

- Source: https://pentera.io/resources/research/detecting-an-mssql-databases-version-using-the-tds-protocol/
- Access/evidence: **landing_only**. Site body not available in current scrape.
- Research question, if supported, or limitation: May offer technique/background only; no safe invented X→Y.
- Research intelligence / epistemic caveat: Unknown.
- **Training:** blocked; no independently verified predecision snapshot.

## SRC-000072 — Evading detection research

- Source: https://pentera.io/resources/research/evading-detection-from-inception-to-reality/
- Access/evidence: **landing_only**. Landing page described a PDF but full PDF was not opened or inspected.
- Research question, if supported, or limitation: Original research process unknown until PDF acquisition.
- Research intelligence / epistemic caveat: Needs document source rights/reading.
- **Training:** blocked; no independently verified predecision snapshot.

## Cross-case observations (candidate, non-exhaustive)

- Source identity migration matters: original Assetnote link, canonical Searchlight Cyber page and research author's identity are separate provenance fields.
- A first-person switch from static reverse engineering to realistic test-fixture generation and error-search (47) exposes decisions not visible in a CVE announcement.
- A routine internal development task spawning an unplanned research question (60) is useful as a case where the original task and exploration boundary are explicitly documented.
- Corporate AI-limits articles (51–54) should not be treated as historical experiments or as categorical evidence that bounded practical verification is impossible.
- Landing-only sources (62–72) must remain unresolved rather than silently filled using generic security knowledge.

