# Working records

This folder holds the dated working files behind the review: the audits that checked it, the research-intake notes that fed it, the proposals that changed its scores, and two expert-interview guides. None of them is part of the citable review, which is the manuscript, the bibliography and the method at the repository root, and none of them enters the Zenodo deposit (`tools/build/export_paper.sh` excludes `working/` and fails the build if anything from it appears in the export manifest).

The files moved here from the repository root, and one from `.claude/`, on 2026-11-17, with their names and bodies unchanged. Each one is a point-in-time record, so a figure inside it describes the corpus on the day it was written, not today; the live counts come from `python3 scripts/count_reconcile.py`, and the outcome of each record is in the status column below and in CHANGELOG.md. `MOVE-MAP.json` lists every old and new path, and `scripts/repoint_moved_paths.py` rewrites mentions of the old paths from it.

## Audits

| File | Date | What it is | Status | Old path |
|---|---|---|---|---|
| [AUDIT-REPORT-BEST-PRACTICES.md](audits/AUDIT-REPORT-BEST-PRACTICES.md) | 2026-01-02 | Repository audit against the claude-code-project-best-practices framework | Executed by its own account (lines 13-17); kept as a dated snapshot, not retro-edited (D-AUDIT sheet line 43) | `AUDIT-REPORT-BEST-PRACTICES.md` |
| [SELF-AUDIT-2026-06.md](audits/SELF-AUDIT-2026-06.md) | 2026-06-21 | Intent self-audit: whether each mechanism still matches the reason it was added | Superseded by the July audits; no execution record of its own; kept as a dated snapshot (D-AUDIT sheet line 43) | `SELF-AUDIT-2026-06.md` |
| [REVIEW-AND-PLAN-2026-06.md](audits/REVIEW-AND-PLAN-2026-06.md) | 2026-06-05 | State-of-the-repository review and revival plan after a 96-day lapse | Executed except the website-citation merge, left open at line 110; the cadence it proposed is now `scripts/SCHEDULING.md` | `REVIEW-AND-PLAN-2026-06.md` |
| [MIESSLER-REPO-AUDIT-2026-07-09-cowork.md](audits/MIESSLER-REPO-AUDIT-2026-07-09-cowork.md) | 2026-07-09 | Simplification audit from a cloud session without git access, ending in a ranked delete/stop list | Recommendation-only; every row re-verified and adjudicated in the D-AUDIT sheet below | `MIESSLER-REPO-AUDIT-2026-07-09-cowork.md` |
| [D-AUDIT-ADJUDICATION-2026-07-09.md](audits/D-AUDIT-ADJUDICATION-2026-07-09.md) | 2026-07-09/10 | Local verification of every row of the cowork audit, with corrections applied and archives staged | Executed 2026-07-10 (frontmatter `status`) | `D-AUDIT-ADJUDICATION-2026-07-09.md` |
| [VERIFICATION-SWEEP-2026-07-09-cowork.md](audits/VERIFICATION-SWEEP-2026-07-09-cowork.md) | 2026-07-09 | Per-citation verification sweep, part 1 (49 URL and claim checks) | Recommendation-only; fix pass applied (CHANGELOG 2026-07-09 "verification-sweep fix pass, part 1") | `VERIFICATION-SWEEP-2026-07-09-cowork.md` |
| [VERIFICATION-SWEEP-PART2-2026-07-10-cowork.md](audits/VERIFICATION-SWEEP-PART2-2026-07-10-cowork.md) | 2026-07-10 | Part 2: the bibliography entries part 1 did not reach, plus the appendix-g and appendix-j links | Recommendation-only; 59 fixes applied (CHANGELOG 2026-07-10 (later) "Part-2 sweep fix application") | `VERIFICATION-SWEEP-PART2-2026-07-10-cowork.md` |
| [VERIFICATION-SWEEP-PART3-2026-07-10-cowork.md](audits/VERIFICATION-SWEEP-PART3-2026-07-10-cowork.md) | 2026-07-10 | Part 3: the surfaces parts 1 and 2 never touched (book appendices, extraction plan, analysis-bundle banners) | Recommendation-only; fix pass applied (CHANGELOG 2026-07-10 (evening) "Part-3 sweep landed") | `VERIFICATION-SWEEP-PART3-2026-07-10-cowork.md` |
| [REVIEW-AND-RECOMMENDATIONS-2026-07-16.md](audits/REVIEW-AND-RECOMMENDATIONS-2026-07-16.md) | 2026-07-16 | Review of the changes since 2026-07-08 and readiness for journal submission and the Zenodo deposit | Recommendation-only; executed in waves (CHANGELOG 2026-07-16 Gate C, Gate D and review fix pass entries) | `REVIEW-AND-RECOMMENDATIONS-2026-07-16.md` |

## Research intake

| File | Date | What it is | Status | Old path |
|---|---|---|---|---|
| [GEMINI-DR1-INTAKE-2026-07-10.md](intake/GEMINI-DR1-INTAKE-2026-07-10.md) | 2026-07-10 | Deep-research intake on streaming-versus-batch economics, every candidate verified at its primary | Disposed: no Tier-A or Tier-B material found, nothing catalogued (line 12) | `GEMINI-DR1-INTAKE-2026-07-10.md` |
| [GEMINI-DR2-INTAKE-2026-07-10.md](intake/GEMINI-DR2-INTAKE-2026-07-10.md) | 2026-07-10 | Vendor-landscape delta scan, 28 grouped checks at vendor primaries | Applied the same day: 16 changes landed in appendix-g (line 12) | `GEMINI-DR2-INTAKE-2026-07-10.md` |
| [GEMINI-DR3-INTAKE-2026-07-10.md](intake/GEMINI-DR3-INTAKE-2026-07-10.md) | 2026-07-10 | Hunt for peer-reviewed primaries, with three misattributions caught | Applied: six Level-A entries catalogued (line 12) | `GEMINI-DR3-INTAKE-2026-07-10.md` |
| [MONTHLY-2026-07-RESEARCH-PACKET.md](intake/MONTHLY-2026-07-RESEARCH-PACKET.md) | 2026-07-09 | July monthly sweep: freshness checks and new-source candidates for adjudication | Partly applied; nine candidates, four leads and the softer re-tiers left open (line 10); the re-tiers continue in `methods/RETIER-PROPOSAL-2026-07-18.md` | `MONTHLY-2026-07-RESEARCH-PACKET.md` |

## Proposals and design records

| File | Date | What it is | Status | Old path |
|---|---|---|---|---|
| [RESCORE-PROPOSAL-2026-07.md](proposals/RESCORE-PROPOSAL-2026-07.md) | 2026-07-09 | Post-audit confidence re-score of the original seven hypotheses | Adopted 2026-07-09, then superseded 2026-07-13 by the mechanical rescore in `methods/RESCORE-2026-07-13.md` (frontmatter `status`) | `RESCORE-PROPOSAL-2026-07.md` |
| [NEW-HYPOTHESES-PROPOSAL-2026-07.md](proposals/NEW-HYPOTHESES-PROPOSAL-2026-07.md) | 2026-07-10 | Wording for two new hypotheses anchored on the DR-3 primaries | Adjudicated and integrated into the manuscript 2026-07-10 (frontmatter `status`) | `NEW-HYPOTHESES-PROPOSAL-2026-07.md` |
| [mcp-server-spec.md](proposals/mcp-server-spec.md) | 2026-01-20 | Design specification for a literature-review MCP server | Historical: the server's repository was archived 2026-07-01, and the corpus statistics inside predate the 2026-06-05 audit (banner, line 10) | `.claude/mcp-server-spec.md` |

## Expert-interview guides

| File | Date | What it is | Status | Old path |
|---|---|---|---|---|
| [EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md](expert-interviews/EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md) | 2025-10-16 | Interview guide on DuckDB edge processing and security data volumes | Not scheduled (line 18); context re-pulled 2026-07-16 (line 12) | `EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md` |
| [EXPERT-INTERVIEW-GUIDE-LISA-CAO.md](expert-interviews/EXPERT-INTERVIEW-GUIDE-LISA-CAO.md) | 2025-11-26 | Interview guide on the catalog landscape (Gravitino, Polaris, XTable) | Not scheduled (line 16); refresh-before-scheduling banner of 2026-07-10 | `EXPERT-INTERVIEW-GUIDE-LISA-CAO.md` |

## Current pass

`2026-11-17-quality-pass/` holds the notes and changelog fragments from the November 2026 quality pass while it is integrated; they are working notes, and the CHANGELOG.md entry for the pass is the record.

For older material (session logs, superseded status reports, the October 2025 extraction log), see [`archive/README.md`](../archive/README.md).
