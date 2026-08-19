# Living Literature Review — Security Data Works evidence backbone

**Purpose**: Evidence backbone for the Security Data Works program — the book *Modular Open Architecture (MOAR) for Cybersecurity Data*, the securitydataworks.com essays/research, and the applied-bridge positioning
**Last Updated**: July 16, 2026 (Version 1.23.0)
**Last Reviewed**: June 29, 2026
**Search currency**: Database searches current as of 2026-07-13 (OpenAlex, dblp); curation is continuous
**Status**: Phase 2 ACTIVE | Tier-3 evidence companion to the MOAR handbook campaign

---

## Executive Summary

This repository contains a **living literature review** that is the shared evidence backbone for the Security Data Works program — the book *Modular Open Architecture (MOAR) for Cybersecurity Data*, the essays and research at securitydataworks.com, and the applied-bridge positioning all cite it. The review bridges cybersecurity and data engineering with evidence-tiered, source-verified research (each entry carries an A/B/C/D tier and a validation verdict in RESEARCH-JOURNAL.md). Published openly (first released October 22, 2025; the original Substack was retired 2026-05-24 and writing moved to securitydataworks.com) with ongoing monthly updates and quarterly deep dives.

**Current Status - June 2026** 🔄:
- **231 sources catalogued** (229 tiered + 2 documented stubs; 25.3% Evidence Level A, live 2026-07-23 — 58/229; the systematic-search incorporation added 26 peer-reviewed studies on 2026-07-13, after a critical appraisal refused 14 of the 40 the search returned — eight of them in predatory or compromised venues. The Level-A share barely moved, because most of what survived appraisal tiers at B or C; that is the honest result and not a disappointing one — see MASTER-BIBLIOGRAPHY.md § Systematic Search Arm; a 27th study was admitted 2026-07-16 when the second-screen adjudication reversed one exclusion through the same gate)
- **17 formal research questions** (RQ1-RQ14, plus RQ15-RQ17 adopted 2026-06-13 in Gap 12 — RQ16 substantively benchmarked, RQ15/RQ17 Tier-D unvalidated; roster ruled 17 on 2026-07-16)
- **Fabrication audit + freshness sweep complete** (2026-06-05 to 2026-06-21; Version 1.22.0, best-practices score 92/100 — see RESEARCH-JOURNAL.md)
- **Now the Tier-3 evidence backbone of the MOAR handbook campaign** (handbook on-page footnotes resolve to this repo's sources + their RESEARCH-JOURNAL verdicts)

## Current Priorities

**Handbook-campaign companion (current driver)**:
- Resolve each handbook on-page footnote to a source here, with a JIT verdict in RESEARCH-JOURNAL.md (VERIFIED before it ships)
- Phase 6: migrate the book appendices A–M into this repo as the public deep-evidence tier
- Hold the honest post-audit baseline: the 2026-06-05 audit re-tiered ~26 entries off Level A; don't silence the floor breach

**Ongoing Evidence Collection**:
- LIGER Stack production deployments
- AI governance maturity case studies
- Pipeline vs query detection benchmarks
- Agent automation ROI metrics

---

## Current Repository Contents

**Core Documentation Files**:
1. **MASTER-BIBLIOGRAPHY.md** - Complete bibliography with 231 catalogued sources (229 tiered), 25.3% Evidence Level A (live, 58/229)
2. **METHODOLOGY.md** - 10 research questions (RQ1-RQ10) including isolation-first security architecture (note 2026-07-16: the full roster is 17 — METHODOLOGY.md formalizes RQ1-RQ10, RQ11-RQ14 live in LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md Gap 11, and RQ15-RQ17 in Gap 12, the last two Tier-D unvalidated)
3. **PUBLICATION-MANUSCRIPT.md** - COMPLETE academic journal manuscript (~15.3k words main text, measured 2026-07-16; derived at build, see the manuscript's MANUSCRIPT METADATA block)
4. **REFERENCES.md** - IEEE/ACM formatted references (78 numbered sources, of which 12 are withdrawn in place; superseded 2026-07-16 by the manuscript's embedded reference section, and the file carries a superseded banner)
5. **APPENDICES.md** - 4 appendices (Evidence rubric, Confidence scoring, Expert protocol, Source taxonomy)
6. **FIGURES-AND-TABLES.md** - 5 figures + 5 tables with publication specifications
7. **LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md** - Gap analysis that seeded the original hypothesis roster (9 assessed as of 2026-07-10; the Oct-2025 numbers inside are the historical record)
8. **LITERATURE-EXTRACTION-PLAN.md** - Systematic extraction methodology (PRISMA-aligned)
9. **PUBLICATION-VENUE-RECOMMENDATIONS.md** - Academic publication strategy
10. **archive/REPOSITORY-STATUS.md** - Historical phase-status report (archived 2026-07-10; live metrics are the Quality Metrics block in this README)
11. **CHANGELOG.md** - Version tracking for academic citation stability (Versions 1.0.0-1.23.0 + [Unreleased])

**Analysis Bundles** (analysis-bundles/):
- Live (3): hypothesis-confidence-matrix.md (cited by manuscript Appendix B), cost-reality-reference.md (cited by FIGURES-AND-TABLES.md), staffing-budget-calculator.md (held pending the queued book ch06 footnote edit)
- Archived 2026-07-10 → archive/analysis-bundles/ (6 static Oct-2025 synthesis files, regenerable from the live bibliography; each carries its 2026-06-14 fold-correction notes)
- Source quality enhancements (contradiction analysis, validation chains, corroboration patterns)

**Monthly Update Tracking** (NEW - Phase 2G):
- **monthly-update-tracker.md** - Comprehensive tracking system for monthly rolling updates
- **isolation-first-security-tracking.md** - RQ7-RQ10 research tracking (15,800 words)
- **scripts/automation_dashboard.py** - Automation health monitoring dashboard
- **scripts/weekly_health_check.py** - MCP vendor database refresh and validation

**Publication Graphics** (publication-graphics/):
- Python scripts: Figure 2 (Evidence Distribution), Figure 3 (Source Taxonomy), Figure 4 (Hypothesis Confidence)
- LaTeX TikZ: Figure 1 (PRISMA flowchart)
- Generated outputs: PNG (300 DPI) + PDF (vector) for all figures
- Automated generation: generate_all_figures.sh, requirements.txt, README.md

**Expert Interview Guides**:
- **EXPERT-INTERVIEW-GUIDE-LISA-CAO.md** - Catalog adoption, XTable validation, H-ARCH-01
- **EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md** - DuckDB edge processing, H-EDGE-01, data volumes

---

## Hybrid Model Evolution (Phase 2G - Active)

**Monthly Rolling Updates** (6-8 hours/month, ACTIVE):
- New sources from blog feedback and LinkedIn monitoring
- Community engagement and reader corrections
- MCP vendor database refresh (automated weekly)
- Performance benchmarks and emerging technology tracking
- Source quality maintenance (broken link fixes, outdated source refresh)

**Quarterly Deep Dives** (~24 hours/quarter target — ruled 2026-07-16, resolving the ~32h formerly stated here against .claude/CLAUDE.md's ~24h; actuals are derived per update in monthly-update-tracker.md and reported month-labeled by scripts/automation_dashboard.py, so the hours figure is no longer hand-asserted anywhere):
- Expert interviews and validation (Lisa Cao, Jake Thomas, etc.)
- Comprehensive hypothesis review
- Versioned snapshots for citation stability (git tags: YYYY-QX-v1.0)
- Quarterly synthesis blog posts
- Evidence Level A restoration and quality improvements

## Future Repository Expansion (When Needed)

As the vendor landscape and platform coverage expands, the repository may grow to include:

> The `platforms/`, `infrastructure/`, and `security-specific/` topic directories were created as empty
> README-only stubs in Oct 2025 and never populated; they were removed 2026-07-09. Topic coverage lives in
> `MASTER-BIBLIOGRAPHY.md` (organized by topic) and `analysis-bundles/`. If per-topic tracking files are
> ever wanted, they can be recreated then rather than sitting empty.

### vendor-landscape/ (Planned - IT Harvest powered)
- `capability-matrix.md`: Platform capabilities by category
- `market-trends.md`: Quarterly trend analysis
- `quarterly-updates/`: YYYY-QX-update.md files

---

## Quarterly Deep Dive Process (Phase 2G - Active)

**Quarterly Cycle** (January, April, July, October):
1. **Month 1 (First month of quarter)**: Expert interviews + comprehensive hypothesis review
2. **Month 2**: Evidence synthesis + versioned snapshot (git tag)
3. **Month 3**: Quarterly synthesis blog post + academic citation updates

**Version Control** (Citation Stability):
- Each quarter creates git tag: `YYYY-QX-v1.0` (e.g., 2025-Q4-v1.0)
- CHANGELOG.md tracks all revisions
- Enables stable academic citations to specific versions
- Monthly updates tracked between quarterly snapshots

**Evidence Sources** (Hybrid Model):
1. **Vendor database** (quarterly regeneration, rollups gated by `scripts/derive_vendor_rollups.py`) - 71 vendors; 92 evidence legs, 41.3% Tier A at the 2026-07-18 regen
2. **Writing insights** (securitydataworks.com /writing) - source identification from essay + LinkedIn feedback
3. **Expert network validation** (Lisa Cao, Jake Thomas, Paul Agbabian, etc.)
4. **Community feedback** (practitioner corrections, reader feedback)
5. **IT Harvest partnership** (optional enhancement, not critical path)

---

## Integration Points

**Published Literature Review**:
- **First release** October 22, 2025 on the Security Data Commons Substack (retired 2026-05-24; essays now at securitydataworks.com/writing) — immutable snapshots in `published/`
- Monthly rolling updates (November 2025+)
- Quarterly deep dives for citation stability
- **Academic journal submission**: Journal of Cybersecurity (Oxford), owner ruling 2026-07-10; submission gate lifted 2026-07-15

**Book Manuscript**:
- All chapters have supporting citations in MASTER-BIBLIOGRAPHY.md
- Literature review provides evidence foundation for 115,500-word manuscript
- Quarterly deep dives feed book revisions

**Writing (securitydataworks.com)**:
- The /writing essays and /research pages cite this repo as their evidence backbone
- Reader feedback → new sources → literature updates → improved essay evidence
- "Being wrong publicly" philosophy: rapid iteration, intellectual honesty
- (The original Security Data Commons Substack was retired 2026-05-24; do not poll it)

**Vendor Database** (`vendor-landscape/`):
- 71 vendors; evidence rollups derived per vendor by `scripts/derive_vendor_rollups.py` (pre-commit/CI gated) — 92 logical sources, 41.3% Tier A at the 2026-Q3-c regeneration (2026-07-18)
- Quarterly regeneration cadence (the MCP-era weekly refresh retired with that repo's 2026-07-01 archive)
- Replaces IT Harvest dependency (partnership now optional)

**Expert Network**:
- Validation interviews (Lisa Cao, Jake Thomas, Paul Agbabian, etc.)
- Expert feedback incorporated into hypothesis validation
- Source: second-brain expert network (1,444 thought leaders mapped)

---

## Key Research Findings

**Research Questions** (10 detailed below, RQ1-RQ10 — note 2026-07-16: the full roster is 17, with RQ11-RQ14 in LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md Gap 11 and RQ15-RQ17 in Gap 12, RQ15/RQ17 still Tier-D unvalidated; the 10 detailed below are the METHODOLOGY.md set):
- **RQ1-RQ6**: Original data engineering questions (Iceberg adoption, TCO reality, staffing, performance, streaming)
- **RQ7-RQ10 (NEW)**: Isolation-first security architecture pattern
  - RQ7: Performance overhead of isolation mechanisms
  - RQ8: Table format convergence (Iceberg + XTable)
  - RQ9: Security-specific catalog features adoption
  - RQ10: Real-world deployment patterns

*Scores below are the canonical 2026-07-13 rubric rescore (`methods/RESCORE-2026-07-13.md`, applied to the manuscript in fea2e05; ruled canon 2026-07-16, replacing the 2026-07-09 adopted values that differed on seven of nine rows).*

**Hypothesis Validation Results** (9 assessed: 7 original + 2 added post-audit 2026-07-10; scores are the 2026-07-13 mechanical rescore under `methods/scoring-rubric.md`, matching PUBLICATION-MANUSCRIPT.md §3.7):
- H-ARCH-01 (Iceberg Dominance): STRONGLY VALIDATED, 23/25 - industry consensus as de facto standard; all four legs survived primary verification (the bare "76% adoption" figure is unsourced; refined per the H-ARCH-01 audit)
- H3-PERFORMANCE-01 (ClickHouse): HIGH CONFIDENCE, 19/25 - Cloudflare 6M req/sec production; the sub-second query-share figure was withdrawn in the 2026-06 audit (the earlier 20/25 was not reachable from the rubric's anchor values)
- H-STREAM-01 (Stateful Streaming): MODERATE, 15/25 - re-anchored on Samza (Noghabi et al., VLDB 2017) plus Azure production scale; two legs cap the source count, which demotes it from the earlier High Confidence
- H-LOGCOMP-01 (Machine-Data Compression; added 2026-07-10): HIGH CONFIDENCE, 17/25 - three peer-reviewed anchors (LogLite, PBC, Pebbles), verbatim-verified at their primaries
- H-SOC-BASELINE-01 (SOC Alert Base Rates; added 2026-07-10): MODERATE, 13/25 - Yang et al. (USENIX Security 2024) production measurement, single-source cap
- H-COST-09 (Tiered Storage): PRELIMINARY, 9/25 - mechanism documented and a first-party S3 tier-price derivation bounds the saving, but the original savings band was withdrawn in the 2026-06 audit; directional pending re-sourcing
- H-IMPL-02 (Staffing Scarcity): PRELIMINARY, 5/25 - quantitative legs withdrawn in the 2026-06/07 audits; no scoreable leg, instrument floor; directional pending re-sourcing
- H-IMPL-03 (Timeline Premium): PRELIMINARY, 5/25 - quantitative legs withdrawn in the 2026-06/07 audits; no scoreable leg, instrument floor; directional pending re-sourcing
- H-IMPL-01 (Streaming TCO): PRELIMINARY, 5/25 - quantitative legs withdrawn in the 2026-06/07 audits; no scoreable leg, instrument floor; directional pending re-sourcing

**Quality Metrics** (2026-07-12 — honest post-audit baseline, live-computed via `scripts/automation_dashboard.py` and gated by `scripts/count_reconcile.py`):
- **Evidence Level A: 25.3%** (58 of 229 tiered sources) — the 2026-06-05 fabrication audit re-tiered ~26 entries off A, and the denominator has since grown faster than the A-count as Tier-B practitioner/framing anchors were added; the 2026-07-13 systematic-search incorporation added 11 Level-A studies but 15 at B/C, so the share held flat. This is the honest baseline, not the pre-audit 78% claim
- Evidence Level B: 139 of 229 · Evidence Level C: 32 of 229 (across 231 `#### ` blocks incl. 2 documented stubs)
- The Tier-A floor (60%) is intentionally breached and surfaced, not silenced — a breach that reflects real corpus quality is the dashboard working (see `scripts/weekly_scheduled_check.py`)
- Every >12-month source now carries a 2026-06-05 validation or freshness marker; 9 fabricated entries removed, 3 dead links recorded (see RESEARCH-JOURNAL.md)
- Production-deployment anchors (Shell, Cloudflare, SK Telecom, Huntress, etc.) are vendor case studies — Tier C under the global tiers; verify each primary before load-bearing use

---

## Development: derived counts + pre-commit gate

Counted numbers on this repo's surfaces are derived, not hand-typed, because the same fact copied across seven-plus files drifted (a 9-vs-7 hypothesis count, and a stale 76/177 tier block sitting 160 lines below a corrected top block in this very README). `scripts/count_reconcile.py` is the single counting rule: it derives the assessed-hypothesis count from PUBLICATION-MANUSCRIPT.md §3.7 (distinct hypothesis IDs cross-checked against the section's own Confidence lines and band headers, so a malformed section fails rather than miscounts) and the bibliography tier counts from MASTER-BIBLIOGRAPHY.md via `automation_dashboard.parse_master_bibliography()`, then checks every allowlisted surface that states one of those numbers (this README, PROJECT-BRIEF.md, PUBLICATION-MANUSCRIPT.md, METHODOLOGY.md, FIGURES-AND-TABLES.md, monthly-update-tracker.md, and the Figure 4 script's roster dict) and exits non-zero on any mismatch, printing a per-surface table. The "Total Hypotheses: 32/34/36" population line is deliberately not gated — its book-side leg is enumerated nowhere in this repo, so the number was retired from live surfaces rather than presented next to gated ones.

Run it directly with `python3 scripts/count_reconcile.py` (full check, exit 1 on any stale surface). The commit gate is `scripts/pre-commit.sh`, which runs the existing secret scan first and then `count_reconcile.py --staged`, where only a staged file whose stated count disagrees with the live derivation blocks the commit. The local hook isn't version-controlled, so point it at the checked-in entry once per clone:

```bash
printf '#!/usr/bin/env bash\nexec bash "$(git rev-parse --show-toplevel)/scripts/pre-commit.sh"\n' \
  > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

Adding a new surface that states a gated count means adding one entry to the ALLOWLIST in `scripts/count_reconcile.py`, not writing another parser; rephrasing or retiring a surface means updating its entry, since a missing pattern fails the run on purpose.

---

**Current Phase**: Phase 2 ACTIVE — Tier-3 evidence companion to the MOAR handbook campaign.
**Recent Milestones**:
- ✅ Fabrication audit complete (2026-06-05): 9 fabricated entries removed, ~26 re-tiered off A, 3 dead links recorded
- ✅ Freshness sweep substantially complete (2026-06-05 / 06-09 / 06-21): every >12mo source carries a validation/freshness marker
- ✅ Health signals made honest (2026-06-29): `weekly_health_check.py` delta-aware, `automation_dashboard.py` live-counts the vendor DB (no bluffed GREEN)
- ✅ Wired as the handbook campaign's Tier-3 evidence backbone (CONTENT-loop owned)

**Next Actions**:
1. **Per-footnote JIT verification** — resolve each handbook on-page footnote to a source here, log the verdict in RESEARCH-JOURNAL.md
2. **Phase 6: appendix migration** — bring the book appendices A–M into this repo as the public deep-evidence tier
3. **Hold the post-audit baseline** — keep the Tier-A floor breach surfaced, not silenced
4. **Academic publication** — journal submission preparation

**Recently Completed** (2026-06-29):
- ✅ README synced to live state (was frozen at Jan-2, v1.19.0; now v1.22.0, honest 46%/146 baseline)
- ✅ Dashboard de-bluffed (vendor DB live-counted from vendor-landscape/vendor-database.json = 71)

**Online Publication**: securitydataworks.com/writing (the original October 22, 2025 release was on the Security Data Commons Substack, retired 2026-05-24 and archived read-only)
**Maintained By**: Jeremy Wiley
**Repository**: https://github.com/flying-coyote/security-data-literature-review

## License

The review prose, bibliography, methods records, and data files are licensed [CC-BY-4.0](LICENSE). The code — `scripts/`, `tools/` (excluding fonts), and the Python/shell files in `publication-graphics/` — is licensed [MIT](LICENSE-CODE), because Creative Commons licenses are not designed for software. The redistributed DM Sans and JetBrains Mono fonts in `tools/build/fonts/` remain under their own SIL Open Font License 1.1 (`tools/build/fonts/OFL-*.txt`).
