---
type: adjudication-sheet
title: "Miessler repo-audit adjudication — locally verified verdicts (2026-07-09/10)"
created: 2026-07-09
status: executed 2026-07-10 — owner signed off; archives applied with two verdict modifications (see Execution record)
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

## Execution record (2026-07-10, owner sign-off "yes get it done")

A 9-agent read-only verification pass re-checked every staged row before execution; 7 of 9 executed as staged, 2 modified:

- **Items 1, 2, 3, 6, 7, 8 executed as staged** (banner → repoint → index, one commit). Item 3's merge went into the existing `archive/2025-12-december/` rather than a new subdir (same-date session material consolidated); item 7's venv was deleted only after pinning exact versions to `publication-graphics/requirements-lock.txt` (matplotlib 3.10.7 / numpy 2.3.4 — loose `>=` pins meant a fresh install couldn't guarantee pixel-identical figures); item 8's branch was deleted after a file-by-file diff vs main confirmed nothing unique (the 21 added vendors live newer in appendix-g, the credential-scan hook was superseded by `scripts/secret-scan.sh` on 2026-06-30, and a verbatim cherry-pick would have deleted content main retains — mcp-server-spec.md plus the azure-sentinel/starburst vendor entries).
- **Item 4 SPLIT**: PROJECT-PLAN-2026-Q1.md (its fourth, previously-uncorrected phantom-tag mention at the Jan 2-3 completed list annotated first) and monthly-update-workflow-verification.md archived; **LITERATURE-EXTRACTION-PLAN.md KEPT LIVE** — six live root docs cite it as the canonical PRISMA-aligned methodology, including two immutable published/ snapshots whose citations can't be repointed without violating never-edit-published.
- **Item 5 MODIFIED**: 6 of 8 archived to `archive/analysis-bundles/`; **cost-reality-reference.md kept live** (FIGURES-AND-TABLES.md's correction note cites its §2.3 as the live grounding for the recalibrated 60-80% band); **staffing-budget-calculator.md HELD** — project1's queued reconciliation edit-set (`staged-decisions-2026-07/staged-reconciliation-results.json`, ready-to-apply) writes its path + line numbers into the book's ch06 `[^siemwins]` footnote; archive only after that edit lands and the citation path is settled. **RESOLVED 2026-07-10 (later): KEEP LIVE** — the footnote landed (book d6eb0ca) citing the calculator at its live path, which settles it permanently live under the same book-cites-it precedent as hypothesis-confidence-matrix. The hold's caution proved DOUBLY right: on final check both live book-cited bundles (the calculator AND hypothesis-confidence-matrix) were found still asserting every withdrawn leg (DORA/IDC/Ververica/MIT-TR/DOES/Gartner/AWS-55%/Netflix/Shell) — they had escaped every sweep because the sweeps' scope ended at the bibliography + appendices e/f/g/i/j. Both got folded-correction banners 2026-07-10 (calculator re-labeled author-modeled throughout; matrix rows re-scored to the post-overturn 1/5 / 2/5 / 4/5 with a DO-NOT-USE stop on its journal-ready statements); the book's Ververica-median parenthetical in [^siemwins] was dropped in the same pass (book e582063). Part-3 sweep over the remaining never-swept appendices (a-d, h, k-m) staged as cowork Prompt G.
- **Item 9 adopted**: both process rules written into `.claude/CLAUDE.md` Key Gotchas (derive-don't-state counts; no blanket verification certificates).
- **New finding fixed in the same pass** (commit 08422b7): LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md was a live public surface still asserting the withdrawn IDC/DORA/Ververica/MIT-TR/DOES/AWS/Netflix figures — it escaped both the 2026-06-14 fold-correction sweep and the 2026-07-09 fix passes; Gaps 1/2/4 + H1-COST-08 now carry dated OVERTURN notes. Also fixed: vendor-landscape/README.md advertised never-created `capability-matrix.md`/`market-trends.md` (now labeled), and archive/README.md's inventory was backfilled with the previously-unregistered `2025-12-december/` subdir.
- **Deliberately untouched**: dated point-in-time audit snapshots (AUDIT-REPORT-BEST-PRACTICES.md, SELF-AUDIT-2026-06.md, MIESSLER-REPO-AUDIT) keep their as-written inventory rows — same never-retro-edit principle as published/.

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
