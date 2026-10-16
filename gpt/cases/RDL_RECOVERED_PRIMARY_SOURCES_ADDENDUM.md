# RDL — Source recovery addendum: original-content gaps found after first pass

**2026-10-16. Original inventory frozen at `066b37c840576427ecdb54cb4541d710b3100ba6`.** This addendum restores publisher-controlled mirrors or official PDFs for 14 previously inaccessible/landing-only records. It **does not overwrite** first-attempt errors in `RDL_SRC_000044_000072_SOURCE_AUDIT.md`: retrieval history is part of provenance.
All X→Y narratives are *bounded, first-party author reported, unreviewed*; only SRC-000068 still lacks content. No rights clearance, original lab logs or independent verification; all are **training-blocked**.

## SRC-000032 — From Naptime to Big Sleep

- Registry URL: https://googleprojectzero.blogspot.com/2024/11/from-naptime-to-big-sleep.html
- Recovered primary or first-party location: https://googleprojectzero.blogspot.com/2024/11/?m=1
- Provenance: publisher monthly archive, original author preserved
- Source evidence: November 1, 2024 Big Sleep team text reports that earlier AIxCC SQLite null dereference inspired targeting SQLite; an AI agent reported another exploitable SQLite underflow before release.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Prior model-assisted vulnerability research and AIxCC event → open question whether targeting the same widely used, heavily tested program with richer agents would yield a meaningful new issue → first-party article reports a finding.
- **Unknowns / limitations:** This is a published organizational retrospective, not full chronological agent trace; author expressly cautions that a tailored fuzzer may still be as effective. Historical private decisions and blind efficacy not verified.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000044 — PAN-OS path confusion

- Registry URL: https://www.assetnote.io/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os
- Recovered primary or first-party location: https://www.slcyber.io/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os-cve-2025-0108
- Provenance: original publisher article migrated to acquiring organization
- Source evidence: Assetnote explicitly states its routine practice of checking existing CVEs and how patches work. While reviewing earlier PAN-OS fixes they noticed proxy architecture: Nginx sets an auth-check header, Apache re-processes paths, then PHP enforces it.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Routine patch validation → question 'can Nginx and Apache interpret path differently after rewrite?' → analyze independent normalization and double-decoding behavior → article reports bypass of auth boundary.
- **Unknowns / limitations:** Exact tested chronology and all discarded hypotheses unavailable. The article is first-party narrative with reproducible-looking examples, not independently verified by RDL.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000045 — Next.js middleware due diligence

- Registry URL: https://www.assetnote.io/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927
- Recovered primary or first-party location: https://www.slcyber.io/research/doing-the-due-diligence-analysing-the-next-js-middleware-bypass-cve-2025-29927
- Provenance: original Assetnote research mirrored/migrated to Searchlight Cyber; note URL spelling 'analysing'
- Source evidence: After publicly disclosed CVE, researchers found standard detection signatures miss redirect-based middleware and locale redirects produce false positives. Reviewed Next.js code to identify a response header surfaced by alternative request context and derived more reliable checks.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Public PoC and template signature → challenge whether the oracle covers redirect-vs-rewrite behavior → compare middleware responses, audit framework internals and redesign baseline/probe → publisher claims higher coverage and less noise.
- **Unknowns / limitations:** Independent measured detection ROC and all raw sampled installations absent; this is due diligence by *later researchers*, not private thoughts of original discoverers zhero/inzo_.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000062 — Ingress-NGINX new injection vectors

- Registry URL: https://pentera.io/resources/research/ingress-nightmare/
- Recovered primary or first-party location: https://pentera.io/blog/ingress-nginx-injection-vulnerabilities/ ; https://pentera.io/wp-content/uploads/2026/03/penteralabs_ingress.pdf
- Provenance: publisher summary + original Pentera research PDF
- Source evidence: Pentera says it began by reproducing Wiz's published IngressNightmare findings in its own lab and, during replication, found three additional input/annotation points; report specifies new points and records later disclosure.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Known-CVE reproduction workflow → unexpected question 'do sibling annotations hit the same unsafe config boundary?' → inspect neighboring configuration inputs → three publisher-reported new issues.
- **Unknowns / limitations:** The original Wiz discoveries and Pentera follow-up belong to separate investigator lineages. The PDF is located but no full independent manual verification of every page or exploit is claimed.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000063 — AWS SSM hybrid landscapes

- Registry URL: https://pentera.io/resources/research/risks-of-aws-ssm-in-hybrid-landscapes/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2025/01/pentera_labs_risks_of_aws_ssm_in_hybrid_landscapes.pdf ; https://pentera.io/blog/deciphering-risk-of-aws-sssm-in-hybrid-environments/
- Provenance: official Pentera PDF and publisher overview
- Source evidence: Original document explains why centralized AWS SSM management crosses hybrid trust boundaries and demonstrates scenario classes, including trusted administration channels and on-prem assets.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Legitimate management convenience and broad privileges → architecture question about unexpected identity/host reach across the cloud–on-prem boundary → report proposes and tests multiple representative scenarios.
- **Unknowns / limitations:** A set of scenario demonstrations does not establish particular private historical decision order or generalized prevalence.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000064 — FortiClient VPN zero days

- Registry URL: https://pentera.io/resources/research/two-zero-days-forticlient-vpn-2024/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2024/11/pentera_labs_fortinet_cves-1.pdf ; https://pentera.io/blog/fortinet-vulnerabilities-cve-2024-47574-disclosure/
- Provenance: original PDF and first-party blog
- Source evidence: Author says discovery was sparked by PipeViewer, a named-pipes permission viewer. This led to checking whether lower-privilege clients could access privileged FortiClient service APIs and examining separate opaque IPC protections.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Encounter interesting research tool → question 'which named pipes have unexpectedly permissive ACLs and high-privilege peers?' → inspect service IPC and source-reported vulnerabilities.
- **Unknowns / limitations:** Press-release summary is not the full research transcript; a publisher-authored PDF was located but its full text not audited in this pass.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000065 — Active Directory SID DoS

- Registry URL: https://pentera.io/resources/research/dos-attack-active-directory-sid-exploitation/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2024/11/pentera_labs_youll_never_sidem_coming-1.pdf ; https://pentera.io/blog/dos-attack-active-directory-sid-exploitation/
- Provenance: original PDF plus first-party blog
- Source evidence: Authors demonstrate that token SID membership limit may stop login when memberships exceed a threshold; Microsoft viewed it as administration/policy issue, authors disagree on security categorization.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Known AD group/token limit → ask whether low-privilege group administration can induce a domain-wide unintended effect → author-reported demonstration and contested vendor impact interpretation.
- **Unknowns / limitations:** Exploitability depends on delegated group membership privileges, actual domain configuration and specified assumptions. Disagreement about severity does not invalidate the observed test outcome.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000066 — Reflective loading remote memory interactions

- Registry URL: https://pentera.io/resources/research/reflective-loading-with-remote-memory-interactions/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2024/06/pentera_labs_reflective_loading_remote_memory_interactions.pdf
- Provenance: original publisher PDF
- Source evidence: Paper decomposes reflective module interaction into memory operations, data representation and remote function calls. Rather than only repeating actions one-by-one, authors build separate MemoryAPI, BufferAPI and ModuleAPIs.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Remote program/library interaction objective → decomposition into memory/objects/functions → design interfaces for separate constraints and examples.
- **Unknowns / limitations:** Engineering methods documented more clearly than original subjective decision sequence; future exploit relevance and security claims need separate evaluation.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000067 — DevalScript

- Registry URL: https://pentera.io/resources/research/devalscript-the-language-of-processes/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2024/06/pentera_labs_reflective_loading_deval_script.pdf
- Provenance: original publisher PDF
- Source evidence: PDF expressly reports network latency from issuing many separate remote memory commands motivated trying a bulk-command interface; this suggested double evaluation and composable primitives, becoming a scripting language.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Functionally valid but latency-heavy prior framework → how to reduce round trips? → bulk command idea → double evaluation emerges → generalized interpreter / DevalScript.
- **Unknowns / limitations:** A retrospective engineering narrative with explicit stated motive, not raw design-session log. Do not infer it improved outcomes universally.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000068 — WebLogic post exploitation

- Registry URL: https://pentera.io/resources/research/not-another-weblogic-exploitation-how-to-prevent-rce/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2023/12/pentera_labs_not_another_weblogic_exploitation_the_road_to_post_exploitation.pdf
- Provenance: official PDF identified via indexed publisher search; full extraction failed during opening
- Source evidence: The document's title and official PDF provenance were confirmed, but no reliable body-level description extracted in this pass.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** UNKNOWN — source evidence insufficient for detailed historical decision sequence.
- **Unknowns / limitations:** Do not substitute article title or generic WebLogic technique lore for evidence. Flag PDF retrieval/manual inspection pending.
- Status: original_pdf_found_content_not_verified; independent review pending; training blocked.

## SRC-000069 — LOLBAS Odyssey

- Registry URL: https://pentera.io/resources/research/the-lolbas-odyssey-finding-new-lolbas-and-how-you-can-too/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2023/08/pentera_labs_the_lolbas_odyssey_finding_new_lolbas_and_how_you_can_too.pdf
- Provenance: original publisher PDF, first-person
- Source evidence: Author sought additional LOLBAS downloaders for Pentera validation. Initial Excel idea had a specific SYSTEM-context limitation. He adapted Oddvar Moe's manual list-and-test process, observed measurable HTTP callback, then realized 3,000+ binaries made manual coverage infeasible.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Existing routine validation objective → prior-art method and targeted Excel failure → small viable controlled tests → scalability obstacle → automate bounded 'try and measure' loop → expand feature classes.
- **Unknowns / limitations:** Article explicitly reports several decisions; exact time order and future performance transfer remain independently unchecked. Its metrics of 12 new files/four weeks are first-party claims.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000070 — Neglected network protocols

- Registry URL: https://pentera.io/resources/research/death-by-default-neglected-network-protocols-you-should-know/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2023/07/pentera_labs_neglected_network_protocols-1.pdf
- Provenance: original Pentera research PDF
- Source evidence: The official paper examines three legacy network protocols and the types of discovery/exposure they enable.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Hypothesis candidate: seemingly low-priority default protocols may expose capabilities or information; detailed original lab experimentation chronology not independently inspected.
- **Unknowns / limitations:** Source-reported scenarios are not one chronological exploit chain; current review is limited to first-party abstract/sections.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000071 — MSSQL TDS pre-login

- Registry URL: https://pentera.io/resources/research/detecting-an-mssql-databases-version-using-the-tds-protocol/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2023/05/pentera_labs_the_gateway_to_control_initiating_attacks_on_mssql_databases.pdf ; https://pentera.io/blog/how-to-find-the-mssql-databases-version-with-the-tds-protocol/
- Provenance: publisher PDF and original blog
- Source evidence: Authors examine TDS pre-login packet which includes a version token before successful user authentication; this yields protocol-derived environment information.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Environment model lacks DB version → ask what metadata can be obtained from protocol handshake before auth → inspect pre-login parser and extract version field.
- **Unknowns / limitations:** Feature exists as part of protocol design; obtaining a version is not itself a vulnerability, and test requires reachable DB port.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## SRC-000072 — Evading Detection dependencies

- Registry URL: https://pentera.io/resources/research/evading-detection-from-inception-to-reality/
- Recovered primary or first-party location: https://pentera.io/wp-content/uploads/2023/02/pentera_labs_evading_detection_pdf.pdf
- Provenance: original 11-page Pentera PDF; research body read via PDF text indexing
- Source evidence: Reflective loader briefly worked; new Windows Defender detection happened around dependency resolution. Comparing original GetProcAddress and custom implementation exposed DLL forwarding; later the team investigated ApiSet indirection.
- **Bounded research question / X→Y (analyst paraphrase unless explicit):** Initially working loader → detection after Defender update → which dependency API calls trigger detector? → compare own resolution function with system API → DLL forwarding and ApiSet emerged as correctness constraints.
- **Unknowns / limitations:** Retrospective timeline; exact contemporary logs and alternative attempts absent. Separate tool incompatibility from actual security detection and from developer's broader objective.
- Status: official_first_party_content_recovered_bounded; independent review pending; training blocked.

## Revised evidence access status

- Previously 14 records lacked original content: SRC-000032, -044, -045, -062 through -072.
- 13 of 14 now have *some* substantive publisher-controlled source text identified and checked, with varying depth; SRC-000068 still publisher PDF locator only.
- New addresses are **additional provenance locators**, not a change to historical source ID or a second independent investigation.
- `READ_FULL` cannot be inferred from any of these recoveries, including official PDFs; first-party page availability, actual paragraph verification, researcher diary reconstruction and adjudicated truth are separate gates.

