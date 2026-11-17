---
type: audit
title: "Miessler-Lens Simplification Audit — security-data-literature-review (Cowork session)"
created: 2026-07-09
source: cowork cloud session (no owner memory loaded; read-only against existing files)
evidence-tier: mixed, per-claim (see legend)
method: adapted Miessler questions 1/11/14/15; counts re-derived from the tree, not from doc self-reports
---

# Miessler-lens repo audit — 2026-07-09 (cowork)

**What this is**: a simplification audit of this repository, answering four adapted Miessler questions from the repo's own record, ending in a ranked DELETE/STOP list. **Nothing here is applied.** Every row is a recommendation for the owner to veto or adopt. This session had no access to the owner's memory or the private project1 repo, and the sandbox could not run git against this working tree, so git state was read from `.git/` metadata directly and the branch/commit handoff at the end is for the local session.

**Evidence-tier legend (for claims in this file)**:
- **[A]** — derived directly from the tree, code, or `.git` metadata in this session (re-checkable with one command)
- **[B]** — from the repo's own recent post-audit record (`RESEARCH-JOURNAL.md`, `SELF-AUDIT-2026-06.md`, `CHANGELOG.md` [Unreleased], `REVIEW-AND-PLAN-2026-06.md`)
- **[C]** — from older self-reported docs (pre-2026-06-05 audit); treat as claims, not facts

---

## Ground truth re-derived from the tree (do not trust doc counts)

1. **176 `#### ` blocks in `MASTER-BIBLIOGRAPHY.md`** — grep-confirmed this session; matches the CLAUDE.md/README claim of 176 (175 tiered + 1 rejection stub). [A]
2. **Level-A count**: naive `**Evidence Level**: A` regex = 76 lines; the dashboard's first-marker-per-block method reports 74/175 = 42.3%. The 2-line delta is dual-tier entries (e.g., "A for the graduation fact; B for the feature docs"). The self-reported 42.3% is honest to within ±1%. [A]
3. **Git state**: `HEAD` = `main` @ `5a6f5bf` ("🔧 Monthly update 2026-07", 2026-07-09), **exactly equal to `origin/main`** — nothing unpushed on main. One stale branch `local-wip-2026-06-05` @ `9b4c758`. Reflog shows 15 commits 2026-06-30 → 2026-07-09 (appendix curation + monthly update), so the repo is currently active. [A]
4. **Zero git tags exist in this clone** — no `refs/tags/`, none in `packed-refs`. See Q4; this contradicts multiple docs. [A]
5. **~4,300 files (~a full Python venv) sit under `publication-graphics/venv/`**, and `venv/` is **not** in `.gitignore`. A binary grep of `.git/index` for `pyvenv.cfg` found nothing, so it is *probably* untracked local clutter — confirm locally before celebrating. [A]
6. **The figure scripts do not exist.** `publication-graphics/` contains only `README.md`, `requirements.txt`, `generate_all_figures.sh`, and the venv. The `figure2/3/4*.py` and `figure1_prisma_flowchart.tex` that `publication-graphics/README.md`, `generate_all_figures.sh:47-66`, root `README.md:61-65`, and `REPOSITORY-STATUS.md:128-132` all describe are absent, as are all PNG/PDF outputs. [A]
7. **Two archival conventions coexist**: `archive/` (12 files, Oct–Dec 2025) and `archived/` (4 files, one 2025-12-06 session). [A]
8. **Three directories contain only a README**: `infrastructure/`, `platforms/`, `security-specific/` — each promising "Quarterly Updates (January, April, July, October)" and named content files (`table-formats.md`, `catalogs.md`, …) that were never created (initialized 2025-10-15). [A]
9. **`vendor-landscape/quarterly-updates/` contains only the template.** No `2025-Q4-update.md`, no `2026-Q1/Q2-update.md` — zero quarterly updates ever produced against a cadence promised since October 2025 (`vendor-landscape/README.md:24-28`). [A]
10. **`build/` holds `litreview.md` + `litreview.pdf` on disk while `/build/` is gitignored**; the `.gitignore` comment says "reproducible via `tools/build/build.sh`" — **no `tools/` directory exists in this repo**. [A]

---

## Q1 — GOAL ALIGNMENT (Miessler #1 adapted)

**What this repo is FOR, in one sentence (from its own docs)**: it is the public, evidence-tiered, provenance-verified living bibliography that every external claim of the Security Data Works program (the MOAR handbook, securitydataworks.com `/writing` + `/research`, the hypothesis tracker) is supposed to trace back to (`README.md:3,12`; `SELF-AUDIT-2026-06.md` Q1; `book-appendices/README.md:3`). Since the 2026-06-05 fabrication audit, the sharper form is: **its value is the chain of custody on every claim, not the volume of claims** (`RESEARCH-JOURNAL.md:10-14`). [B]

**What in the tree works against that goal**:

1. **A second, frozen bibliography**: `REFERENCES.md` (78 IEEE-formatted sources, Oct 2025) duplicates the state of `MASTER-BIBLIOGRAPHY.md` at 78/176ths of its current size and none of its post-audit verdicts. Duplicated state that must drift — the exact disease the June plan diagnosed with project1's copy (`REVIEW-AND-PLAN-2026-06.md:39-42`). [A/B]
2. **Surfaces still asserting retired numbers**: 20 files still carry the pre-audit "79% Level A" claim [A: grep this session], including actively-presented root docs `PUBLICATION-MANUSCRIPT.md`, `APPENDICES.md`, `FIGURES-AND-TABLES.md`, `METHODOLOGY.md`, `PROJECT-BRIEF.md`, and `REPOSITORY-STATUS.md`. The manuscript abstract got a 2026-06 caveat ("a 2026-06 source audit withdrew the citations behind several of the originally stated multipliers") but its body still contains withdrawn figures. Each is a surface where a reader can cite a number the journal has already retracted — directly against the chain-of-custody goal.
3. **A status tracker that is a fossil wearing a live banner**: `REPOSITORY-STATUS.md` has a correct 2026-07-09 metrics line at the top, followed by ~650 lines of November–December 2025 plans presented in the present tense ("Actions in Progress: December 2025 monthly rolling update…", "Report Date: October 22, 2025" at the bottom). Third parallel status surface after README and CLAUDE.md; it consumed a reconciliation pass in June (`CHANGELOG.md` count-reconciliation entries) and drifted again by July. [A]
4. **Retired-purpose surfaces**: the IT Harvest partnership docs (`vendor-landscape/INTEGRATION-PLAN.md`, `IT-HARVEST-PARTNERSHIP-CHECKLIST.md`) serve a partnership that PROJECT-BRIEF marked "deferred/optional — MCP baseline sufficient" on 2025-10-30 (`PROJECT-BRIEF.md:377-383`); the empty scaffold dirs (`infrastructure/`, `platforms/`, `security-specific/`) serve a Phase-2B structure whose content model was superseded by the MCP vendor DB + `book-appendices/` (Appendix G *is* the vendor landscape now). [A/B]
5. **Docs no downstream consumer reads**: the June audit's one named constraint is that the site's `/research/methodology` page has **zero links into this repo**, and project1's bibliography is still a divergent copy (`SELF-AUDIT-2026-06.md` Q6; `REVIEW-AND-PLAN-2026-06.md` item 6). Meanwhile the repo maintains reader-facing inventory (README "Current Repository Contents") describing files by their October-2025 shape (CHANGELOG "Versions 1.0.0-1.12.0"; publication-graphics "Generated outputs … for all figures" — see ground truth #6). A source of truth nothing links to, describing contents it no longer has. [B/A]

---

## Q2 — DEPRECIATION vs DURABLE (Miessler #11 adapted)

Given frontier models now do harvesting, summarizing, and format-translation on demand, the work-classes in this repo split cleanly:

**Compounding (protect; the only things that can't be regenerated)**:

1. `RESEARCH-JOURNAL.md` — the append-only validation ledger with method/verdict vocabulary. This is the repo's crown jewel and the June audit already said "do not touch except to extend" (`SELF-AUDIT-2026-06.md`). [B]
2. `MASTER-BIBLIOGRAPHY.md` — but only *because* of the tier + validation-status fields tied to journal rows. The prose summaries inside entries are regenerable; the verdicts are not.
3. **Adjudication records**: `MONTHLY-2026-07-RESEARCH-PACKET.md`-style packets (claims verified at primary, held for human sign-off) are exactly the right durable artifact shape — the *decision* is the value.
4. `book-appendices/` A–M — canonical here per `book-appendices/README.md:3`, actively maintained (18 commits of curation, 2026-06-30 → 07-09 reflog). [A]
5. `vendor-landscape/vendor-database.json` — live-counted by the fixed dashboard (71 vendors). [B]
6. **Expert-interview primary material — which does not exist yet.** The guides (`EXPERT-INTERVIEW-GUIDE-*.md`) are prep, not primary material; the interviews have been "scheduled for Q1 2026" since October 2025 and remain unexecuted nine months later. The one work-class every doc agrees is irreplaceable is the one with zero artifacts. [A/B]

**Depreciating at model-release speed (STOP producing, not just deprioritize)**:

1. **STOP: static evidence-synthesis bundles.** 7 of the 8 `analysis-bundles/` files are October-2025 syntheses whose "94% Evidence Level A average" framing predates the audit (`REPOSITORY-STATUS.md:77`); a model regenerates any of them from the live bibliography in minutes, with current verdicts. Exception: `hypothesis-confidence-matrix.md`, which was re-anchored 2026-06-14 with first-party lab measurements — that one is adjudication and compounds. [A/C]
2. **STOP: static format-extractions of the bibliography** — `REFERENCES.md` (IEEE re-format), `APPENDICES.md`, `FIGURES-AND-TABLES.md` (figure *specs* with pre-audit numbers baked into the annotations: "79% Level A", "EXCEEDS TARGET +6pp"). Regenerate at submission time from live data. [A]
3. **STOP: committed figure packages.** `publication-graphics/` is the terminal case: the scripts are already gone, the venv remains, and the README hardcodes retired numbers into figure captions. Regenerating three matplotlib charts is now a single prompt. [A]
4. **STOP: session-log archives as first-class repo content.** `archive/SESSION-*.md` + `archived/2025-12-06-session/*` (≈3,000 lines) narrate work whose durable residue already lives in CHANGELOG/journal. The repo even carries a `.gitignore` rule for a local-only `.archive/` — a third convention. Session narration is exactly what model+git-log reconstructs on demand. [A]
5. **STOP: "verification report" documents that assert 100%.** `published/VERIFICATION-REPORT-2025-10-22.md` certified "All performance metrics (6M req/sec, 57TB/day…) ✓" — the 57 TB/day Shell figure was later found FABRICATED and removed (`RESEARCH-JOURNAL.md`, removed cf26e77, 2026-06-05). The durable form of verification is a journal row per claim, not a blanket certificate. [B]

---

## Q3 — VANISH TEST (Miessler #14 adapted)

If the owner disappeared for 30 days, what breaks or silently rots:

1. **The weekly loop fires into a void — and cries wolf by design.** The cloud routine (`trig_01XkVDZSc4nyMiUT5p7Ft2zr`, cron `33 12 * * 1`, `scripts/SCHEDULING.md:55-59`) is read-only/notify-only, which is correct — but `weekly_scheduled_check.py:decide()` escalates on `Level-A < 60% floor` (currently 42.3%, so **every run**) plus the monthly window. The June audit named this `loop-without-rethink` (`SELF-AUDIT-2026-06.md` Q3/Q4); the July fixes made the *health check* delta-aware but the escalation gate on disk is still level-only [A: code read this session]. Four identical Monday-REDs into the owner's absence, the signal is wallpaper — the same dynamic that hid the previous 96-day lapse (`REVIEW-AND-PLAN-2026-06.md:31-36`). **Worth durably encoding** (delta-aware gate + quarterly floor re-derive), not deleting.
2. **The adjudication queue rots silently.** `MONTHLY-2026-07-RESEARCH-PACKET.md` holds 11 catalog-ready sources + 8 judgment calls "pending sign-off." Nothing tracks packet age; a vanished owner means verified research decays toward stale, unmerged. **Encode**: a packet-age check in the weekly notification (one line of code).
3. **The provenance discipline lives in one person's habits.** The June audit's top-3 action #3 — block commits that add a `#### ` entry without a `**Validation Status**` line — is still not implemented. Worse, `PreCommit.sh` is (a) advisory-only ("Always allow commit", line 45-46) and (b) **wired to nothing**: `.claude/settings.json` registers only `SessionStart` and `Stop` hooks, and `.git/hooks/` contains only `.sample` files — so no commit path, Claude or plain git, even sees the reminder. [A] **Worth durably encoding** — this is the single highest-leverage bus-factor fix, already specified in SELF-AUDIT.
4. **The cleanup worklist is unreachable.** The journal's non-VERIFIED worklist lives in private `project1/FABRICATIONS-REGISTER-2026-06.md` (`RESEARCH-JOURNAL.md:33-35`). Anyone continuing the public repo without project1 access cannot see what's left to fix. **Encode**: a public, redacted count-only mirror (N MISMATCH remaining, N WEAK-SOURCE) or accept the coupling deliberately.
5. **Head-only conventions**: the "point-in-time Key Metrics blocks are history, don't update them" rule, the emoji commit-prefix taxonomy, and "which of the four status surfaces is authoritative" exist in CLAUDE.md + habit. Mostly harmless — but `REPOSITORY-STATUS.md`'s live-banner-over-fossil layout is only legible to someone who already knows the convention. **Delete the surface rather than encode the convention** (see DELETE list #2).
6. **Unpushed/stray state**: `main` is fully pushed [A]; the risk is the unexplained `local-wip-2026-06-05` branch and whatever uncommitted state sits in *other* working copies (the June audit saw `master` + a revival branch in its copy that this clone doesn't have — divergent clones are themselves a single-human dependency). Needs local confirmation.
7. **What does NOT break** (credit where due): the bibliography+journal pair is fully self-describing; the scripts self-locate after the July fix (`CHANGELOG.md` [Unreleased]); the Substack retirement is encoded in `monthly-update.md:37-38` so a future operator won't poll a dead channel. The 30-day vanish costs this repo freshness, not integrity — that is a direct payoff of the June provenance work. [B]

---

## Q4 — LOOP GAPS (Miessler #15 adapted): assumed vs enforced

| # | Maintenance the docs assume | What actually enforces it | Verdict |
|---|---|---|---|
| 1 | Monthly update executed (6-8h, `.claude/commands/monthly-update.md`) | Weekly routine *nags* (exit 10); a human must run it. Feb→Jun 2026 proved the failure mode (96 days dark) | Maintained-by-hope, now hope-with-a-doorbell. Acceptable **if** the notification sink is confirmed (see local-confirm #5) |
| 2 | Quarterly git tags `YYYY-QX-v1.0` for citation stability (CLAUDE.md; README:123-126; PROJECT-BRIEF Decision 4) | **Nothing — and it has never happened once.** Zero tags in this clone [A]. `PROJECT-PLAN-2026-Q1.md:27` claims "Create git tag 2025-Q4-v1.0 ✅ Jan 3" — no such tag is fetchable here, yet `published/README.md:134,143-152` instructs readers to cite "Version 2025-Q4-v1.0". A citation-stability promise with a false paper trail is worse than no promise | **The single worst doc-vs-reality gap in the repo.** Either create tags in the release flow or delete the promise everywhere |
| 3 | Quarterly deep dives incl. expert interviews (every status doc since Oct 2025) | Nothing. Zero interviews in 3 elapsed quarters; zero `quarterly-updates/*.md` files [A] | Retire the cadence claim or wire it to the scheduler like the weekly check was |
| 4 | Weekly link/freshness check | **Real**: cloud routine + `weekly_health_check.py`, honest after the 2026-06/07 fixes | The one enforced loop. Keep |
| 5 | Dashboard consulted pre-update (`monthly-update.md` step 2) | The dashboard **crashed on every run** (`TypeError` on the header regex) until fixed 2026-07-09 (`CHANGELOG.md` [Unreleased]) — and nobody noticed for weeks, proving the step wasn't being run | Checklist theater until July; now honest. Watch whether it's actually used |
| 6 | CHANGELOG updated for all content changes (CLAUDE.md "Key Gotchas") | Advisory echo in a Claude-only hook; plain git bypasses it [A] | Promote to a real `.git/hooks/pre-commit` or accept as convention |
| 7 | New bibliography entries carry validation provenance | Nothing mechanical (see Vanish #3) | Encode — already specified in SELF-AUDIT top-3 |
| 8 | Dedupe against hub/project1 + website linkage | Manual; both named pending in June (`REVIEW-AND-PLAN-2026-06.md` item 6, task #70: 159 site URLs untriaged) | Still open; the SoT's consumers still don't point at it |
| 9 | "Empty-scaffold dirs will be populated when needed" (README:89-111) | Nothing; 9 months, zero files | Delete scaffolds; recreate on first real content |

---

## Ranked DELETE/STOP list

Scoring: **deletion value = standing cost removed × recurrence + risk removed, discounted by effort.** All actions are recommendations; asterisked rows (*) have a needs-local-confirmation dependency.

| Rank | Action | Target | Why (cost × recurrence + risk) | Effort | Tier |
|---|---|---|---|---|---|
| 1* | **DELETE** | `publication-graphics/venv/` (~4,300 files) + `scripts/__pycache__/`; add `venv/`, `.venv/` to `.gitignore` | Largest object count in the repo for zero value; pollutes every future clone/search/audit; probably untracked so deletion is free | Trivial | A |
| 2 | **DELETE (archive first)** | `REPOSITORY-STATUS.md` as a maintained surface — fold the one live metrics line into README, move the fossil to `archive/` | 679 lines, ~90% stale-presented-as-current; third parallel status surface; consumed a June reconciliation pass and drifted again by July — recurring monthly tax + misleads any reader | Low | A |
| 3 | **STOP + archive** | The static publication quartet: `REFERENCES.md`, `APPENDICES.md`, `FIGURES-AND-TABLES.md`, and freeze `PUBLICATION-MANUSCRIPT.md` behind a "pre-audit draft" banner until journal submission is actually scheduled | Duplicate bibliography (78 vs 176) guaranteed to drift; retired 79%/withdrawn multipliers still citable from active root docs; regenerable from live data at submission time | Low | A/B |
| 4 | **DELETE (keep nothing)** | `publication-graphics/` remainder: README, `generate_all_figures.sh`, `requirements.txt` | Documents scripts that no longer exist (ground truth #6) and hardcodes retired numbers into future figures; regenerating 3 charts from live data is a single session's work | Trivial | A |
| 5 | **DELETE** | Empty scaffolds `infrastructure/`, `platforms/`, `security-specific/` (3 READMEs) | Each promises a quarterly cadence never once met and content files never created; README §"Future Expansion" already records the plan; empty dirs assert maintenance that doesn't exist | Trivial | A |
| 6 | **STOP + archive** | `vendor-landscape/INTEGRATION-PLAN.md`, `IT-HARVEST-PARTNERSHIP-CHECKLIST.md` | Serve a partnership marked optional/deferred since 2025-10-30; the MCP DB replaced it; keep `vendor-database.json` + schema + template | Trivial | A/B |
| 7 | **MERGE** | `archived/` → `archive/` (4 files); adopt one convention, note it in `archive/README.md` | Two parallel archival conventions + a third gitignored `.archive/`; every future archiving decision pays the ambiguity tax | Trivial | A |
| 8 | **DELETE (archive)** | Planning fossils: `PROJECT-PLAN-2026-Q1.md` (expired quarter; contains the false ✅-tag row — annotate when archiving), `monthly-update-workflow-verification.md` (Nov-2025, superseded by SCHEDULING.md per SELF-AUDIT), `LITERATURE-EXTRACTION-PLAN.md` (named dead weight in SELF-AUDIT) | Stale plans read as live commitments; the false tag claim actively misinforms citation-stability decisions | Trivial | A/B |
| 9 | **STOP** | Hand-maintained counts/percentages in README + CLAUDE.md prose — replace with "run `scripts/automation_dashboard.py`" pointer + one dated snapshot line | Count drift is this repo's most-repaired defect (reconciled Nov 2025, June 2026, July 2026 — three documented passes); each pass costs a session and the number is stale by the next add | Low | B |
| 10 | **STOP + archive** | 7 static `analysis-bundles/` files (all except `hypothesis-confidence-matrix.md`) | Oct-2025 syntheses with pre-audit quality claims; regenerable on demand from live bibliography; book chapters they accelerated are written | Low | A/C |
| 11 | **DECIDE-or-archive** | `EXPERT-INTERVIEW-GUIDE-LISA-CAO.md`, `EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md`, `isolation-first-security-tracking.md` | Nine months "scheduled"; tracking doc frozen at "Evidence Collection Phase" since Nov 2025 with unchecked December milestones. Either book the interviews (they'd create the repo's only irreplaceable primary material) or archive the prep; also fix the CHAO/CAO filename mismatch in README:68 and archive/README.md:92 [A] | Trivial (archive) | A |
| 12 | **DELETE (archive)** | `.claude/conversations/` (2 Oct-2025 session transcripts) | Session narration inside config space; belongs in archive if anywhere | Trivial | A |
| 13* | **DELETE** | Stray branch `local-wip-2026-06-05` after local inspection; delete `build/` on-disk artifacts if `tools/build/` truly lives elsewhere | Unlabeled WIP branches are unpushed-state risk (Vanish #6); the gitignore comment references nonexistent tooling | Trivial | A |
| 14 | **STOP (process rule)** | Producing blanket "✅ 100% verified" certificates (the `published/VERIFICATION-REPORT` pattern) | One already certified a figure later proven fabricated; the journal's per-claim rows are the honest replacement | Zero | B |

**Explicitly NOT on the list**: `RESEARCH-JOURNAL.md`, `MASTER-BIBLIOGRAPHY.md`, `CHANGELOG.md`, `book-appendices/`, `MONTHLY-2026-07-RESEARCH-PACKET.md`, `vendor-database.json` + schema, `scripts/` (post-fix), `.claude/` hooks/commands/skill, `hypothesis-confidence-matrix.md`, `published/` snapshots (immutable history — but see owner fork #2), `METHODOLOGY.md` (needs a count refresh, not deletion), `monthly-update-tracker.md` (live), `SELF-AUDIT-2026-06.md` / `REVIEW-AND-PLAN-2026-06.md` (recent adjudication records).

---

## Needs local confirmation (this session could not verify)

1. `git ls-files publication-graphics/venv | head` — venv tracked or untracked? (index grep says untracked; binary grep is not conclusive). Determines whether rank #1 is `rm -rf` or also needs `git rm -r --cached`.
2. `git tag -l && git ls-remote --tags origin` — does `2025-Q4-v1.0` exist anywhere? `PROJECT-PLAN-2026-Q1.md:27` says created Jan 3; this clone has zero tags. If it exists locally-only, push it; if it never existed, correct the record when archiving the plan.
3. `git branch -a` in the primary working copy — SELF-AUDIT saw `master` + `lit-review-revival-2026-06`; this clone has neither. Confirm one canonical copy and prune the rest.
4. `git log main..local-wip-2026-06-05` — anything unmerged worth keeping before deleting the branch?
5. Where do the Monday routine's notifications actually land, and does the owner see them? Also whether `~/weekly-review-reports/` is accumulating unread output.
6. Whether the delta-aware escalation (SELF-AUDIT top-3 #1) was intentionally deferred — `weekly_scheduled_check.py:decide()` on disk is still level-only + monthly-window.
7. Reachability plan for `project1/FABRICATIONS-REGISTER-2026-06.md` if project1 is unavailable (Vanish #4).
8. Whether `tools/build/build.sh` (referenced in `.gitignore:25`) lives in the book repo — if so, point the comment there; if not, the build path is fiction.

---

## Open owner forks (decisions only the owner can make)

1. **Journal submission — still live?** "Mid-2026" is now. If yes: regenerate REFERENCES/figures from live data as part of the submission sprint (ranks #3/#4 become "archive until sprint"). If no or deferred again: archive the entire publication surface and stop paying its drift tax.
2. **`published/` pre-audit snapshots**: leave byte-identical (strict citation-stability reading) vs. prepend a dated banner noting the 2026-06-05 audit superseded specific claims (chain-of-custody reading). The repo's own philosophy ("being wrong publicly") argues for the banner; the never-edit-published rule argues against. Genuine fork.
3. **Quarterly tags**: adopt-and-do (create the first real tag at the next stable point, wire tag-creation into the monthly/quarterly command) vs. drop the promise from CLAUDE.md/README/PROJECT-BRIEF. Anything but the current state, where readers are instructed to cite a tag that doesn't exist.
4. **Escalation gate**: accept permanent-RED until Level-A recovers to 60%+, or implement the delta-aware gate + quarterly floor re-derive per SELF-AUDIT. (Cheap, already specified, directly reduces vanish-risk.)
5. **Hypothesis-count adjudication**: 7 validated (CLAUDE.md) vs "3 strongly validated / 6 proposed" (Oct-2025 gap analysis) vs 31 (regex over-count). Research judgment; flagged since June; no mechanical fix possible.
6. **Empty scaffolds**: delete now / recreate on first content (recommended) vs. keep as roadmap markers.

---

## Git handoff (sandbox could not run git against this tree)

This session created exactly one new file: `MIESSLER-REPO-AUDIT-2026-07-09-cowork.md` (this file). No existing file was modified. To commit per the session rules (new branch only; never master/main; no force-push):

```bash
cd ~/security-data-literature-review
git checkout -b litreview-miessler-cowork-2026-07-09
git add MIESSLER-REPO-AUDIT-2026-07-09-cowork.md
git commit -m "📋 Miessler-lens simplification audit (cowork, 2026-07-09): 4 answers + ranked DELETE/STOP list"
git push -u origin litreview-miessler-cowork-2026-07-09
git checkout main
```
