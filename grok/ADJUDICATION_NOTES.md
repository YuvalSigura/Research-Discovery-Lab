# ADJUDICATION NOTES — Batch 1 v2 correction

## SRC-000001 / SRC-000002 (xbow-chrome-fullchain-2026)

### v1 issues identified on independent re-read (2026-10-16)
1. Previous analysis (and summarizer output) assigned concrete Maglev/WebP/Crashpad activities to Day 1–2 / 3–4 / 5 / 6.  
   **Correction**: Neither source assigns specific bugs to calendar days. Technical post states only: chain built Sunday Aug 2 through Friday Aug 7; work split into parallel campaigns (broad search, V8 corruption, V8 sandbox escape, renderer sandbox escape, integration). Day-by-day detail removed.

2. Modularity causality.  
   Announcement: team “wisely built the full-chain exploit as three independent parts, each with an alternative” after or in context of first disqualification.  
   Technical post: modular stages and backups designed “to guard against” collisions; strategy “paid off” when Gin stage collided with issue 542670566 and was replaced by WebP.  
   **Correction**: Causality of modularity adoption relative to collisions is uncertain. Do not claim modularity was invented only after discovery of the duplicate. Engineering dependency (stages replaceable) is distinct from chronological discovery order.

3. Claim basis separation.  
   **Correction**: All mechanism claims marked author_reported (retrospective technical narrative). No independent contemporaneous artifacts verified in this pass. Linked Chromium issues noted as next evidence actions, not yet treated as observed by us.

4. Lineage.  
   **Confirmed**: Both posts describe one investigation. Multiple chain revisions and parallel human/agent runs remain distinct sub-elements, not separate lineages.

5. Named participants and model versions.  
   **Confirmed**: Author statements in the posts, not independently verified identity or tool-trace records.

### Changes in v2
- Removed fabricated day assignments.
- Marked modularity timing as uncertain.
- Tightened forbidden_inferences.
- Added explicit transition record for Gin→WebP replacement with rival explanations.
- All training_status remain TRAINING_BLOCKED; predecision_eligibility NOT_PREDECISION_ELIGIBLE.

No external model outputs were consulted. Original v1 statements preserved only in this note for audit.
