# Branch consolidation and data-loss prevention — 2026-10-16

Repository: `YuvalSigura/Research-Discovery-Lab`. This is a file and commit-history preservation record, **not** evidence that a research claim was independently validated.

## Verified before consolidation

- `main` at `7756db14f4c88a7699f49fe50b62aee123e26913`: [CI run #77 PASS](https://github.com/YuvalSigura/Research-Discovery-Lab/actions/runs/38859530920).
- PR [#1](https://github.com/YuvalSigura/Research-Discovery-Lab/pull/1), source `research/first-mission-evidence-reconstruction-20261016`, tip `54dfae0ec98c9aa737ea94fb1c85372ed24c6d74`. Its snapshot contained **221 blobs**. The resulting first PR squash commit `535bf5b2ac5319a0525264071d2e6d3399744080` contained **the exact same set of paths and Git blob hashes** (221/221). All 221 source-branch blobs also exist in the present main tree; the 13 changed blobs between old branch and present main correspond to later updated records, tests and documentation, not missing files.
- PR [#2](https://github.com/YuvalSigura/Research-Discovery-Lab/pull/2), source `research/phase2-decision-corpus-20261016`, tip `ce03bd7878c29491babf38975911951298b89ee2`. Its snapshot contained **231 blobs**, and the merged `main` snapshot has **identical paths and hashes** (231/231). [PR CI #76 PASS](https://github.com/YuvalSigura/Research-Discovery-Lab/actions/runs/38859394322).
- All three recursive Git trees reported `truncated=false`. Both source PRs were merged into main before this consolidation.
- GitHub Actions historical **failed runs are permanent historical results**, not failing checks on the current main revision. Latest tested main revision passed. Never delete or rewrite CI history to pretend failures never occurred.

## Preserve detailed Git history

Squash merges preserve the final content but not the individual commits as ancestors. The **merge-ancestry conservation commit that introduces this document** must have:

1. The previously validated main SHA (`7756db14f4c88a7699f49fe50b62aee123e26913`) as **first parent**.
2. The original PR #1 branch tip (`54dfae0ec98c9aa737ea94fb1c85372ed24c6d74`) as **second parent**.
3. The original PR #2 branch tip (`ce03bd7878c29491babf38975911951298b89ee2`) as **third parent**.

The commit tree must preserve all existing main files, adding only this document, the nonloss test/helper and the CI workflow update. After fast-forwarding main, confirm both former branch tips are ancestors and all corresponding objects remain accessible before any branch deletion.

## New safeguards

- On **every push to main**, and on **every PR targeting main**, run archive, registry, publisher and Python tests.
- Fetch Git history to compare the baseline commit with the proposed candidate, and **reject removal of existing SRC/CASE/EVT/REL/PAS/MND/QPT/QMP/CTX etc. IDs**, removal of legacy catalogue IDs, source URL identity replacement, dropping prior CASE sources, moving EVTs to another case, or changing REL endpoints.
- A necessary intentional historical restructuring should be separately reviewed, with a documented data migration and changed guard policy; do not silently bypass, skip or delete the failing guard.
- On direct commits to main, CI detects mistakes **after** the push. To truly prevent a future bad merge, configure GitHub's repository **Rulesets/Branch protection** to require the `validate` check before merge, disallow force pushes and require review of protected data/authority changes. Users who choose a single-branch direct-push workflow should run the same checks locally *before* pushing.

## Remote branch cleanup procedure (after verification)

Delete only these **two** historical branch refs (not main):

- `research/first-mission-evidence-reconstruction-20261016`
- `research/phase2-decision-corpus-20261016`

The branch refs may be deleted without losing content or commits **only after both branch tips are confirmed ancestors of main**. The two branch names and original SHAs are recorded here. Deleting a branch removes the ref, not the Git commit objects reachable from main. Do **not** delete main, reset history, force-push, or delete tags/commit objects. The connected GitHub integration may not expose a branch-delete operation, in which case remove the two refs through GitHub's Branches page after verification.
