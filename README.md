# Living Literature Review — Security Data Works evidence backbone

**Purpose**: Evidence backbone for the Security Data Works program — the book *Modular Open Architecture (MOAR) for Cybersecurity Data*, the securitydataworks.com essays/research, and the applied-bridge positioning
**Last Updated**: June 29, 2026 (Version 1.22.0)
**Last Reviewed**: June 29, 2026
**Status**: Phase 2 ACTIVE | Tier-3 evidence companion to the MOAR handbook campaign

---

## Executive Summary

This repository contains a **living literature review** that is the shared evidence backbone for the Security Data Works program — the book *Modular Open Architecture (MOAR) for Cybersecurity Data*, the essays and research at securitydataworks.com, and the applied-bridge positioning all cite it. The review bridges cybersecurity and data engineering with evidence-tiered, source-verified research (each entry carries an A/B/C/D tier and a validation verdict in RESEARCH-JOURNAL.md). Published openly (first released October 22, 2025; the original Substack was retired 2026-05-24 and writing moved to securitydataworks.com) with ongoing monthly updates and quarterly deep dives.

**Current Status - June 2026** 🔄:
- **182 sources catalogued** (180 tiered + 2 documented stubs; 42.8% Evidence Level A, live 2026-07-10 — 77/180; honest post-audit baseline + 2026 Tier-A primary sources + Tier-B bridge-framing + detection-engineering anchors + WT-2 production anchors; freshness sweep substantially complete — see RESEARCH-JOURNAL.md)
- **14 research questions** (RQ1-RQ14) with comprehensive validation
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
1. **MASTER-BIBLIOGRAPHY.md** - Complete bibliography with 182 catalogued sources (180 tiered), 42.8% Evidence Level A (live, 77/180)
2. **METHODOLOGY.md** - 10 research questions (RQ1-RQ10) including isolation-first security architecture
3. **PUBLICATION-MANUSCRIPT.md** - COMPLETE academic journal manuscript (9,999 words, all sections drafted)
4. **REFERENCES.md** - IEEE/ACM formatted references (78 sources, alphabetically ordered)
5. **APPENDICES.md** - 4 appendices (Evidence rubric, Confidence scoring, Expert protocol, Source taxonomy)
6. **FIGURES-AND-TABLES.md** - 5 figures + 5 tables with publication specifications
7. **LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md** - Gap analysis with 7 validated hypotheses
8. **LITERATURE-EXTRACTION-PLAN.md** - Systematic extraction methodology (PRISMA-aligned)
9. **PUBLICATION-VENUE-RECOMMENDATIONS.md** - Academic publication strategy
10. **archive/REPOSITORY-STATUS.md** - Historical phase-status report (archived 2026-07-10; live metrics are the Quality Metrics block in this README)
11. **CHANGELOG.md** - Version tracking for academic citation stability (Versions 1.0.0-1.12.0)

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

**Quarterly Deep Dives** (~32 hours/quarter, Q1 2026 next):
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
1. **MCP vendor database** (automated weekly refresh) - 71 vendors, 84% Tier A
2. **Writing insights** (securitydataworks.com /writing) - source identification from essay + LinkedIn feedback
3. **Expert network validation** (Lisa Cao, Jake Thomas, Paul Agbabian, etc.)
4. **Community feedback** (practitioner corrections, reader feedback)
5. **IT Harvest partnership** (optional enhancement, not critical path)

---

## Integration Points

**Published Literature Review**:
- **Substack** (October 22, 2025) - 38,000 words, openly accessible
- Monthly rolling updates (November 2025+)
- Quarterly deep dives for citation stability
- Academic journal submission planned (mid-2026)

**Book Manuscript**:
- All chapters have supporting citations in MASTER-BIBLIOGRAPHY.md
- Literature review provides evidence foundation for 115,500-word manuscript
- Quarterly deep dives feed book revisions

**Writing (securitydataworks.com)**:
- The /writing essays and /research pages cite this repo as their evidence backbone
- Reader feedback → new sources → literature updates → improved essay evidence
- "Being wrong publicly" philosophy: rapid iteration, intellectual honesty
- (The original Security Data Commons Substack was retired 2026-05-24; do not poll it)

**MCP Vendor Database** (Automation Foundation):
- 71 vendors, 84% Tier A quality, 110 evidence sources
- Automated weekly refresh + monthly GitHub metrics
- Replaces IT Harvest dependency (partnership now optional)
- 75-90% burden reduction enables sustainable monthly updates

**Expert Network**:
- Validation interviews (Lisa Cao, Jake Thomas, Paul Agbabian, etc.)
- Expert feedback incorporated into hypothesis validation
- Source: second-brain expert network (1,444 thought leaders mapped)

---

## Key Research Findings

**Research Questions** (10 total, RQ1-RQ10):
- **RQ1-RQ6**: Original data engineering questions (Iceberg adoption, TCO reality, staffing, performance, streaming)
- **RQ7-RQ10 (NEW)**: Isolation-first security architecture pattern
  - RQ7: Performance overhead of isolation mechanisms
  - RQ8: Table format convergence (Iceberg + XTable)
  - RQ9: Security-specific catalog features adoption
  - RQ10: Real-world deployment patterns

**Hypothesis Validation Results** (7 validated):
- H-ARCH-01 (Iceberg Dominance): STRONGLY VALIDATED - industry consensus as de facto standard, 5 sources (the bare "76% adoption" figure is unsourced; refined per the H-ARCH-01 audit)
- H-IMPL-01 (TCO Reality): STRONG - 2.5-3× operational costs, 5 sources
- H-IMPL-02 (Staffing Scarcity): STRONG - 2.7× staff required, 4 sources
- H-IMPL-03 (Timeline Premium): VALIDATED - 5.5 months average, 3 sources
- H-COST-09 (Tiered Storage): STRONG - 55-80% cost savings, 3 sources
- H3-PERFORMANCE-01 (ClickHouse): VALIDATED - 6M req/sec, 96% <1s queries
- H-STREAM-01 (Kafka Streams): VALIDATED - Production security patterns, 3 sources

**Quality Metrics** (2026-07-09 — honest post-audit baseline, live-computed via `scripts/automation_dashboard.py`):
- **Evidence Level A: 42.9%** (76 of 177 tiered sources) — the 2026-06-05 fabrication audit re-tiered ~26 entries off A, and the denominator has since grown faster than the A-count as Tier-B practitioner/framing anchors were added; this is the honest baseline, not the pre-audit 78% claim
- Evidence Level B: 87 of 180 · Evidence Level C: 16 of 180 (across 182 `#### ` blocks incl. 2 documented stubs)
- The Tier-A floor (60%) is intentionally breached and surfaced, not silenced — a breach that reflects real corpus quality is the dashboard working (see `scripts/weekly_scheduled_check.py`)
- Every >12-month source now carries a 2026-06-05 validation or freshness marker; 9 fabricated entries removed, 3 dead links recorded (see RESEARCH-JOURNAL.md)
- Production-deployment anchors (Shell, Cloudflare, SK Telecom, Huntress, etc.) are vendor case studies — Tier C under the global tiers; verify each primary before load-bearing use

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

**Online Publication**: [Security Data Commons on Substack](https://securitydatacommons.substack.com) (Published October 22, 2025)
**Maintained By**: Jeremy Wiley
**Repository**: https://github.com/flying-coyote/security-data-literature-review
