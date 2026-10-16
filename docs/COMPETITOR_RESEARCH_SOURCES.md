# External competitor research discovery — curated source registry

Verified public research or security-oriented landing pages as of 2026-10-16. This is a **source-discovery list only**. Nothing below is automatically proof of original research, recovered chronology, RAW permission, or a complete investigation record.

| Publisher | Priority | Main entry points | What to seek |
|---|---|---|---|
| Horizon3.ai | High | [Attack Blogs](https://horizon3.ai/category/attack-research/attack-blogs/), [Disclosures](https://horizon3.ai/category/attack-research/disclosures/) | Researcher-written chains, disclosures, alternate paths, validation |
| Cymulate Research Labs | High | [Research](https://cymulate.com/research/) | Original cross-component security investigations, AI tools, trust boundaries |
| SafeBreach Labs | High | [Labs](https://www.safebreach.com/safebreach-labs/) | New weaknesses, assumption challenges, false expectations about defenses |
| NetSPI | High | [Technical Blog](https://www.netspi.com/blog/technical-blog/) | Experiment details, cloud identity and penetration research |
| Praetorian | High | [Security Blog](https://www.praetorian.com/blog/) | Vulnerability Research, Labs, methodology and agent-driven discovery |
| XM Cyber | Medium | [Blog](https://xmcyber.com/blog/) | Researcher-attributed weaknesses and contextual attack paths |
| Picus Labs | Medium | [Labs](https://www.picussecurity.com/picus-labs) | Aggregate simulation research, attack paths, empirical counterexamples |
| AttackIQ | Medium | [Threat Research](https://www.attackiq.com/category/research/) | Reconstructed adversary methods, assessment and emulation methodology |

Existing: [Pentera Labs](https://pentera.io/resources/), configured in `sources/publishers/pentera.json`.

## Inclusion policy

Prioritize articles where first-hand investigators show **assumption → observation → question → direction → attempt → evidence → failure/negative outcome → pivot → revised question**. Do not reduce quality to CVE count. Untried branches and abandoned experiments belong in trajectory records **only if documented**. Distinguish publicly documented trajectory from plausible analyst reconstruction and counterfactual suggestions.

Classify content by what it **actually** documents: original experimental case, incident/threat analysis, replication, methodology, aggregate empirical report, synthesis, or marketing. A research-labelled article can still be commentary.

## Intake gate

1. Register publisher and source URL with clear provenance and dedupe.
2. Verify article identity, author/date, original investigation status, and boundaries of accessible evidence.
3. Do not mirror RAW or attach full text without rights review. `raw_capture_enabled=false` for all these entries.
4. On review, create distinct SRC and CASE records (one paper may contain multiple investigations); cite exact source anchors for historical events/relations.
5. Missing failures or rationales must remain **unknown** and should not be invented.

The source registry is checked by `tools/validate_publisher_sources.py` and CI. It does not yet crawl or ingest the listed sites, and no claims are made about access to private/paywalled sources.
