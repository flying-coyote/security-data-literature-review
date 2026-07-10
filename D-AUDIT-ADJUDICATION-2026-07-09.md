---
type: adjudication-sheet
title: "Miessler repo-audit adjudication — locally verified verdicts (2026-07-09/10)"
created: 2026-07-09
status: staged — corrections APPLIED; deletions/archives await owner sign-off
tags: [audit, adjudication, repo-hygiene]
---

# D-audit adjudication — every remaining row locally verified

**Why this sheet exists**: the cowork audit (MIESSLER-REPO-AUDIT-2026-07-09-cowork.md) had a demonstrated ~60% false rate on its first 5 checked claims because its sandbox could not run git, so nothing else in it was actionable unverified. A read-only local verifier has now checked EVERY remaining row with actual commands. Corrections (text fixes) were applied immediately; deletions and archives are staged below for owner sign-off, per the archive procedure (banner → repoint → index, one commit).

## Corrections APPLIED this pass (no sign-off needed — they fix false statements)

| What | Where | Fix |
|---|---|---|
| Stale "79% Level A — EXCEEDS" self-grade still asserted live | METHODOLOGY.md (5 spots), PROJECT-BRIEF.md | Replaced with the live 42.9% figure + withdrawal note; Shell dropped from the examples list |
| False "✅ tag 2025-Q4-v1.0 created Jan 3" completion claims — **the tag never existed** (verified: `git tag -l` + `ls-remote` show only 2026-Q3-v1.0) | PROJECT-PLAN-2026-Q1.md (3 spots) | Marked NEVER CREATED with the verification date; falsely-reported-complete status corrected |
| Citation instructions pointing at the nonexistent tag | published/README.md | Re-pointed to the real 2026-Q3-v1.0; citation year corrected |
| CAO/CHAO filename mismatch (file is …LISA-CAO.md; refs said CHAO) | README.md:68, archive/README.md:92 | Fixed |

## Verified TRUE — archives/deletions awaiting owner sign-off (all confirmed still-present by local commands)

1. **REPOSITORY-STATUS.md** (679 lines; June-2026 banner over October-2025 body) — fold live metrics into README, archive the body.
2. **vendor-landscape/INTEGRATION-PLAN.md + IT-HARVEST-PARTNERSHIP-CHECKLIST.md** — partnership is "NOW OPTIONAL" per PROJECT-BRIEF; archive both, keep vendor-database.json + schema.
3. **archived/ vs archive/** — two coexisting conventions; merge archived/2025-12-06-session/ into archive/.
4. **Planning fossils** — PROJECT-PLAN-2026-Q1.md (expired quarter; its false tag row is now annotated), monthly-update-plan + one more per audit rank 8; archive all three.
5. **analysis-bundles/** — 8 static synthesis files (all but hypothesis-confidence-matrix.md, which stays live; it is now cited by manuscript Appendix B); archive the rest.
6. **.claude/conversations/** — 2 Oct-2025 session transcripts; archive.
7. **publication-graphics/venv** — 4,320 files on disk, confirmed untracked + gitignored; safe to `rm -rf` (no git-side effect). NOTE: the figure regeneration pass (2026-07-09) USES this venv — if removed, recreate from requirements.txt before regenerating figures.
8. **Branch `local-wip-2026-06-05`** — DO NOT blind-delete: it holds exactly one unmerged commit (9b4c758, "WIP snapshot… vendor-db +959 lines, .claude infra — preserved for cloud-reconcile review"). Review/cherry-pick first.
9. **Process rules to adopt** (no artifact): stop hand-maintaining counts in README/CLAUDE prose (dashboard is authoritative); stop blanket "100% verified" certificates (the 2025-10-22 certificate certified later-confirmed fabrications).

## Verified FALSE / already resolved

- venv-not-gitignored, figure-scripts-missing, broken-tools-reference: FALSE (the original 3).
- Static "publication quartet" (REFERENCES/APPENDICES/FIGURES-AND-TABLES/PUBLICATION-MANUSCRIPT) no longer needs archiving — all four were corrected in place by the 2026-07-09 fix passes.
- SELF-AUDIT's branch-set description does not match this clone (no `master`, no `lit-review-revival-2026-06` here) — multiple divergent working copies confirmed; reconcile which clone is canonical.

## Owner forks (not resolvable from repo state)

- **Journal submission**: partly answered — the manuscript's own metadata said "Submission target: Q4 2025" and it passed unsubmitted (corrected 2026-07-09). Remaining decision: pick a new venue + date, or shelve.
- **published/ pre-audit snapshots**: leave byte-identical (citation-stability reading) vs prepend corrective banners (chain-of-custody reading).
- **Escalation gate**: weekly_scheduled_check.py:decide() confirmed level-only with a hardcoded 60% Tier-A floor that is deliberately breached (code comment says do not silence) — accept permanent-RED until Level-A recovers, or build a delta-aware gate.
- **Monday-routine notification destination** and **project1 fabrications-register coupling**: owner-knowledge questions the repo can't answer.
- **Hypothesis-count adjudication** (7 vs alternates): research judgment.
