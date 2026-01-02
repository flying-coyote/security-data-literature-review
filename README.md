# Living Literature Review for "Modern Data Stack for Cybersecurity"

**Purpose**: Comprehensive literature review and research foundation for book
**Last Updated**: January 2, 2026 (Version 1.19.0)
**Last Reviewed**: January 2, 2026
**Status**: Phase 2 ACTIVE | Monthly Updates + Quarterly Deep Dives

---

## Executive Summary

This repository contains a **living literature review** supporting the book "Modern Data Stack for Cybersecurity." The review bridges cybersecurity and data engineering domains with rigorous, evidence-based research. **Published openly on Substack** (October 22, 2025) with ongoing monthly updates and quarterly deep dives.

**Current Status - January 2026** 🔄:
- **101 sources documented** (78% Evidence Level A maintained)
- **14 research questions** (RQ1-RQ14) with comprehensive validation
- **Best practices audit complete** (Version 1.19.0 - Score: 92/100)
- **Q1 2026 Deep Dive active** (January - expert interviews, versioned snapshot)

## Current Priorities

**Q1 2026 Quarterly Deep Dive** (January):
- Expert interviews (Lisa Cao: catalog landscape, Jake Thomas: isolation-first validation)
- Versioned snapshot (tag 2025-Q4-v1.0 for citation stability)
- Quarterly synthesis blog post
- Comprehensive hypothesis validation review

**Ongoing Evidence Collection**:
- LIGER Stack production deployments
- AI governance maturity case studies
- Pipeline vs query detection benchmarks
- Agent automation ROI metrics

---

## Current Repository Contents

**Core Documentation Files**:
1. **MASTER-BIBLIOGRAPHY.md** - Complete bibliography with 83+ sources, 78% Evidence Level A
2. **METHODOLOGY.md** - 10 research questions (RQ1-RQ10) including isolation-first security architecture
3. **PUBLICATION-MANUSCRIPT.md** - COMPLETE academic journal manuscript (9,999 words, all sections drafted)
4. **REFERENCES.md** - IEEE/ACM formatted references (78 sources, alphabetically ordered)
5. **APPENDICES.md** - 4 appendices (Evidence rubric, Confidence scoring, Expert protocol, Source taxonomy)
6. **FIGURES-AND-TABLES.md** - 5 figures + 5 tables with publication specifications
7. **LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md** - Gap analysis with 7 validated hypotheses
8. **LITERATURE-EXTRACTION-PLAN.md** - Systematic extraction methodology (PRISMA-aligned)
9. **PUBLICATION-VENUE-RECOMMENDATIONS.md** - Academic publication strategy
10. **REPOSITORY-STATUS.md** - Comprehensive status report with completion metrics (updated November 14, 2025)
11. **CHANGELOG.md** - Version tracking for academic citation stability (Versions 1.0.0-1.12.0)

**Analysis Bundles** (analysis-bundles/):
- Evidence synthesis (5 bundles: cost reality, implementation, performance, security-specific, hypothesis confidence)
- Practitioner tools (3 tools: staffing calculator, technology decision tree, cost optimization playbook)
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
- **EXPERT-INTERVIEW-GUIDE-LISA-CHAO.md** - Catalog adoption, XTable validation, H-ARCH-01
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

### platforms/ (Planned)
- `query-engines.md`: Trino/Starburst, Dremio, Denodo, Athena
- `olap-analytics.md`: ClickHouse, StarRocks/Celerdata, Druid
- `hybrid-architectures.md`: Spark + Query Engine patterns

### infrastructure/ (Planned)
- `table-formats.md`: Iceberg, Delta, Hudi (trend analysis)
- `catalogs.md`: Gravitino, Polaris, Unity, Nessie
- `object-storage.md`: S3, MinIO, Azure Blob

### security-specific/ (Planned)
- `ocsf-adoption.md`: Quarterly tracking
- `detection-platforms.md`: Security analytics evolution
- `threat-intel-integration.md`: TI platform updates

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
2. **Blog post insights** (Security Data Commons, 3x/week) - 4-6× writing speedup
3. **Expert network validation** (Lisa Cao, Jake Thomas, Paul Agbabian, etc.)
4. **Community feedback** (Substack readers, practitioner corrections)
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

**Blog (PRIMARY DRIVER)**:
- **Security Data Commons** (3x/week practitioner content)
- 4-6× writing speedup demonstrated with evidence foundation
- Reader feedback → New sources → Literature updates → Improved blog evidence
- "Being wrong publicly" philosophy: rapid iteration, intellectual honesty

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
- H-ARCH-01 (Iceberg Dominance): STRONGLY VALIDATED - 76% adoption, 5 sources
- H-IMPL-01 (TCO Reality): STRONG - 2.5-3× operational costs, 5 sources
- H-IMPL-02 (Staffing Scarcity): STRONG - 2.7× staff required, 4 sources
- H-IMPL-03 (Timeline Premium): VALIDATED - 5.5 months average, 3 sources
- H-COST-09 (Tiered Storage): STRONG - 55-80% cost savings, 3 sources
- H3-PERFORMANCE-01 (ClickHouse): VALIDATED - 6M req/sec, 96% <1s queries
- H-STREAM-01 (Kafka Streams): VALIDATED - Production security patterns, 3 sources

**Quality Metrics** (Updated November 2025):
- **Evidence Level A: 78%** (65 of 83 sources) - **MAINTAINS quality target**
- Evidence Level B: 22% (18 of 83 sources)
- Evidence Level C/D: 0% (zero low-quality sources)
- Government/Standards Sources: 8+ (CISA, MITRE, DARPA, NSA, SANS)
- Industry Analysts: 10+ (Gartner, IDC, Forrester)
- Production Deployments: 21+ (Netflix, Uber, LinkedIn, Cloudflare, Shell, SK Telecom, Huntress, Okta, etc.)
- **New (November)**: 3 isolation-first security case studies (Netflix Polaris, Huntress, Okta)
- Metadata Completeness: 96%+

---

**Current Phase**: Phase 2G (Hybrid Model) - Monthly Updates + Quarterly Deep Dives ACTIVE
**Recent Milestones**:
- ✅ Two monthly updates complete (November 2025)
- ✅ Isolation-first security architecture integrated (RQ7-RQ10)
- ✅ Monthly update workflow operational (tracking, automation, dashboard)
- ✅ MCP vendor database operational (71 vendors, automated)

**Next Actions**:
1. **Expert Interviews** (January 2026) - Lisa Cao and Jake Thomas scheduled for Q1 quarterly deep dive
2. **January Monthly Update** (mid-January, 6-8 hours) - New sources, refresh outdated sources
3. **Quarterly Synthesis** - Comprehensive blog post on Q4 2025 findings
4. **Academic Publication** (mid-2026: journal submission preparation)

**Recently Completed** (January 2, 2026):
- ✅ Git tag 2025-Q4-v1.0 created for citation stability
- ✅ Best practices audit completed (Score: 92/100)
- ✅ Completed phases archived

**Online Publication**: [Security Data Commons on Substack](https://securitydatacommons.substack.com) (Published October 22, 2025)
**Maintained By**: Jeremy Wiley
**Repository**: https://github.com/flying-coyote/security-data-literature-review
