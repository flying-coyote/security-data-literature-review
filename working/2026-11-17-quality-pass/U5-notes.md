# U5-structure notes (2026-11-17)

The full change log with sources is kept in the private hub.

## Integration steps for the main session

1. After U1 to U4 and U6 land, run `python3 scripts/repoint_moved_paths.py` (dry run) and compare with `working/2026-11-17-quality-pass/U5-repoint-dryrun.md`, which lists the 21 rewrites pending in other units' files at the time U5 finished (9 files; none in U5's scope, 0 broken relative links repo-wide). Then `--apply`, then `--check`. The pending rewrites include path mentions inside dated records (`methods/RESCORE-2026-07-13.md:11` and `:68`, `methods/RETIER-PROPOSAL-2026-07-18.md:13`, the 2026-07-10 record notes in `analysis-bundles/hypothesis-confidence-matrix.md`, and `monthly-update-tracker.md:286` and `:442` on 2026-11-17). Default: accept those path-only repoints, following the archive procedure's banner, repoint, index precedent (`working/audits/D-AUDIT-ADJUDICATION-2026-07-09.md:38`), and say so in the folded CHANGELOG entry; the alternative is adding those files to `NO_REWRITE` in the script. Either way, run `--apply` in the same commit or push as the moves so CI is never red on master. Links inside fenced and inline code are ignored, but path mentions are rewritten everywhere, including inside inline code.
2. The repo-wide `--check` goes green only after that `--apply`. Until then the CI step fails, and `scripts/pre-commit.sh` blocks any commit that stages one of the files with a pending rewrite, so apply before committing those files.
3. Insert the U6 snippets from `docs/figures/EMBED.md` at the two README markers: `<!-- U6-FIGURE: review-method ... -->` (section "How the review was built") and `<!-- U6-FIGURE: evidence-tiers ... -->` (section "How evidence is tiered"). The README already carries a repository-map table, so U6's table form is not needed there. Hold U6's repository-map image from every surface until its REFERENCES.md and APPENDICES.md nodes (and the matching alt text in `docs/figures/EMBED.md` §3) point at the manuscript's embedded REFERENCES and APPENDICES sections, because the README now labels both files superseded.
4. Fold `U5-changelog.md` into CHANGELOG.md [Unreleased], and at the same time add a dated backfill entry for the 2026-08-19 tier audit that moved 57 entries off Level A (METHODOLOGY.md:452; the commit is c1f5d66 per the pre-pass `.claude/CLAUDE.md`), which CHANGELOG.md does not record today. Once folded, move the README version line from "unreleased changes through 2026-11-08" to 2026-11-17.
5. Retire one of the three README surfaces that repeat the gated 22.5% figure (README lines 23, 24 and the repository-map row), by removing its ALLOWLIST entry in `scripts/count_reconcile.py` ("README top status block" or "README contents bibliography line") and the matching README text in the same commit; U5 does not edit the gate.
6. `CITATION.cff` (lines 2-3 and 7-8) still says a DOI is minted on the first tagged release, which the deposit-scope ruling in `docs/ZENODO-RELEASE-CHECKLIST.md` Step 0 replaced with a manual upload of the curated export. Align its comment and message with the README's "How to cite" wording.
7. The CI secret-scan step in `.github/workflows/gates.yml` is a no-op, because `scripts/secret-scan.sh` reads only `git diff --cached` and exits 0 when nothing is staged. A follow-up can make the CI step scan the push range (for example `git diff origin/main...HEAD`); the README and `.claude/hooks/README.md` now say the scan runs only in the local hook.
8. Stage the moves as renames (`git add -A working/` plus the deleted root paths, or `git mv` equivalents) so history follows the files.

## Corrections to the plan

- The root held 32 Markdown files before the move, not 34 (`ls *.md | wc -l`), so it now holds 15, not 17.
- `.claude/mcp-server-spec.md` had no live reader (grep: only CHANGELOG.md:143 and the 2026-07-16 review mention it) and moved to `working/proposals/`. That brings the map to 18 entries.
- `scripts/link_check.py` and `scripts/weekly_*.py` name only `MASTER-BIBLIOGRAPHY.md`, `PUBLICATION-MANUSCRIPT.md`, `vendor-landscape/` and `methods/`, none of which moved, so they needed no change.

## For other units

- **U2 (METHODOLOGY.md §3.1)**: the Level A block still carries two leftover bullets that contradict its own criteria, "Government/standards body publications (CISA, MITRE, DARPA, NSA, SANS, Apache Software Foundation)" and a duplicate "Peer-reviewed academic publications", and the line "61 of 271 tiered entries (22.5%) ... BELOW target" refers to a target §8.1a retired. The B block says "live share 68.3%" in its heading but "108 of 227 (47.6%)" in its body, and the C heading says "24 of 227". U5 copied none of these; `.claude/CLAUDE.md` and the skill follow the criteria lines only.
- **U2 (manuscript)**: once `--apply` runs, PUBLICATION-MANUSCRIPT.md names `working/proposals/...` and `working/intake/...` paths in prose (lines 290, 987, 1052, 1163-1168 at the time of the dry run). Those files are excluded from the Zenodo deposit, as they were before the move, so a reader of the deposit cannot follow them; a sentence saying they live in the public repository may help.
- `CITATION.cff` (not edited) says the exact tally is in the README's "Quality Metrics block"; the README section is now "Corpus at a glance (quality metrics)", so the pointer still resolves.

## Staged for the owner (not applied)

1. **Expert-interview guides in a public repo.** Both guides name third parties, carry an outreach plan and name the interviewer; U5 only moved them to `working/expert-interviews/`. Default: move them to the private hub and leave a one-line stub (PLAN.md §4 item 2).
2. **Home-directory paths in moved records.** `working/proposals/mcp-server-spec.md:717-719` links three paths on the owner's machine outside this repository, and `working/audits/REVIEW-AND-PLAN-2026-06.md:40` names another. U5 left the bodies unedited under the move-only rule. Default for each: a dated one-line edit that replaces the path with a plain pointer.
3. **Gemini intake notes** carry Google Doc IDs at line 10 of `working/intake/GEMINI-DR1-INTAKE-2026-07-10.md` and `GEMINI-DR3-INTAKE-2026-07-10.md`, and all three name a home-directory path to a private hub file at the same line; DR2's Doc ID was redacted 2026-07-16 under the redact-to-pointer ruling, the other two were not. Default: apply the same redaction to DR1 and DR3, and reduce the hub path to a plain pointer in all three.
4. **`docs/ZENODO-RELEASE-CHECKLIST.md` Step 2** still describes the GitHub-release webhook route, while Step 0 rules a manual upload of the curated export for v1. U5 brought the tag example to the ruled `YYYY-QX-v1.0` placeholder and named Step 0's re-tag of `2026-Q3-v1.0` (fallback `2026-Q3-v1.1`). Two choices stay with the owner: whether Step 2 is rewritten for the manual route, and whether the first deposit carries the Q3 re-tag or a new-quarter tag. Default: Step 0 as written, re-tag `2026-Q3-v1.0`.
5. **First-party lab measurements are tiered two ways.** The skill and `/add-source` tier them at Level B, while `methods/scoring-rubric.md:39` counts a first-party lab measurement on the MOAR reference stack as Level A for Dimension 2, and METHODOLOGY §3.1 says nothing about first-party lab work. Default: keep B for tiering and add a one-line cross-reference in the rubric explaining the scoring exception.
6. **Positioning phrase dropped from the README.** The old README's purpose line said the review backed "the applied-bridge positioning"; the rewrite leaves it out, because it describes a business position rather than the review. Default: leave it out. The Journal of Cybersecurity target, also dropped in the rewrite, is restored as one line under "Where to start".
7. **Roster wording.** The README roster keeps each hypothesis's score, band and withdrawn-leg caveat from the pre-pass README in shorter form; any further rewording of those lines is left for the owner (PLAN §4 item 1 holds H3-PERFORMANCE-01's framing).

## Checks run

- `python3 scripts/count_reconcile.py`: all 79 surfaces agree (273 / 271 / A 61 / B 170 / C 40; 9 hypotheses).
- `python3 scripts/validate_metadata.py`: valid and consistent (cffconvert not installed, schema check skipped).
- `python3 scripts/repoint_moved_paths.py --check --paths README.md .claude .github docs scripts tools/build working/README.md .gitignore`: 0 pending, 0 broken. `--check --paths working`: 0 pending, 0 broken.
- `bash -n` on `tools/build/export_paper.sh`, `tools/build/build.sh`, `scripts/pre-commit.sh`, `.claude/hooks/PreCommit.sh`: all pass. None was executed, because each calls git.
- `export_paper.sh` whitelist: every named path exists.
- `scripts/automation_dashboard.py` smoke run: exit 0.
