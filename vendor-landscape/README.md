# Vendor Landscape Tracking

## Purpose
Intended to maintain quarterly snapshots of the data lakehouse vendor landscape, powered by IT Harvest partnership data (market trends, capability matrices, vendor evolution tracking).

> **Status (2026-07-09): mechanism ready, not yet in use.** Zero quarterly updates have been produced. The
> schema, the update template (`quarterly-updates/TEMPLATE-YYYY-QX-update.md`), and this process doc all
> exist, but the cadence has not started — it is contingent on the IT Harvest partnership, which is still at
> the outreach stage (the unfilled coordination checklist was archived 2026-07-10 → `../archive/IT-HARVEST-PARTNERSHIP-CHECKLIST.md`,
> and the partnership itself is optional per PROJECT-BRIEF.md Blocker 1). Read everything below as the
> *planned* mechanism, not an active one.

## Update Cadence (planned — not yet started)
Intended **Quarterly Updates** (January, April, July, October). None produced as of 2026-07.

## Contents

> Note (2026-07-10): `capability-matrix.md` and `market-trends.md` below were planned deliverables that were
> **never created** — descriptions kept as design intent only. What actually exists here: `vendor-database.json`,
> `vendor-database-schema.md`, `MCP-VENDOR-INTEGRATION-SUMMARY.md`, and `quarterly-updates/` (template only).

### capability-matrix.md
- **Platform Capabilities**: Feature comparison across vendors
- **Category Analysis**: Query engines, OLAP platforms, catalogs, security platforms
- **Maturity Assessment**: Production readiness, enterprise support
- **Focus**: Objective capability mapping, no promotional content

### market-trends.md
- **Adoption Trends**: Technology adoption rates over time
- **Market Dynamics**: M&A activity, funding, product launches
- **Technology Evolution**: Feature convergence, differentiation strategies
- **Focus**: Quantitative trend analysis, market position shifts

### quarterly-updates/
Intended home for versioned quarterly snapshots (citation stability). **Currently contains only
`TEMPLATE-YYYY-QX-update.md`** — no dated update has been produced. The files below were targets that did
not happen:
- `2025-Q4-update.md` (was "target: first update" — not produced)
- `2026-Q1-update.md` (not produced)
- `2026-Q2-update.md` (not produced)

## IT Harvest Partnership
**Status**: Pre-Partnership Planning with MCP Vendor Baseline Complete (October 23, 2025)

**Baseline Data Available**: 71-vendor database from MCP Server enrichment provides ready-made foundation:
- 110 evidence sources (84% Tier A quality = 92 Tier A sources)
- 46.5% analyst coverage (Gartner MQ, Forrester Wave for 33 vendors)
- 35.2% production validation (Fortune 500 deployments for 25 OSS vendors)
- Automated maintenance (weekly refresh + monthly GitHub metrics tracking)

**Partnership Acceleration**: MCP vendor baseline enables:
1. **Pilot Project Validation**: 10 query engine vendors already documented with evidence
2. **First Quarterly Update**: ~60% effort reduction (baseline data + evidence exists)
3. **Quality Baseline**: 84% Tier A evidence quality sets partnership expectations

**Partnership Roadmap**:
1. **Phase 1: Partnership Establishment**
   - Initial outreach to Charles Wells
   - Define pilot project scope (query engines)
   - Clarify data access terms and attribution
   - Establish communication channels

2. **Phase 2: Pilot Project - Query Engines**
   - Vendor list: Trino/Starburst, Dremio, Denodo, Athena, ClickHouse, StarRocks, Druid
   - Data points: Version updates, capabilities, pricing trends, adoption indicators
   - Success criteria: Validate data quality and integration workflow
   - Deliverable: First quarterly update with query engine vendor landscape

3. **Phase 3: Full Partnership - All Categories**
   - Expand to infrastructure layer (table formats, catalogs, object storage)
   - Add security-specific platforms (OCSF, detection platforms, threat intel)
   - Establish quarterly update cycle (Jan, Apr, Jul, Oct)

4. **Phase 4: Ongoing Operations**
   - Quarterly data refresh → Expert validation → Publication
   - Continuous improvement feedback loop
   - Blog integration and book manuscript updates

**Coordination Resources**:
- **../archive/IT-HARVEST-PARTNERSHIP-CHECKLIST.md** (archived 2026-07-10 — unfilled template, partnership optional): partnership coordination guide
  - Phase-by-phase checklist (4 phases)
  - Data collection specifications
  - Quality assurance standards
  - Risk mitigation strategies

**Timeline**:
- Partnership establishment: TBD (pending initial outreach)
- First quarterly update: originally targeted Q4 2025 / Q1 2026 (post-pilot) — **not produced as of 2026-07**; deferred pending the partnership

## Quality Standards
- **Vendor-Neutral Analysis**: No promotional content, balanced trade-offs
- **Quantitative Metrics**: Adoption rates, market share, capability scores
- **Citation Stability**: Versioned snapshots for academic citation
- **Expert Validation**: Practitioner review before publication

## Quarterly Update Process

**Month 1: Data Collection**
- IT Harvest data refresh
- Platform capability updates
- Market trend analysis

**Month 2: Validation**
- Expert network validation
- Blog synthesis integration
- Hypothesis validation updates

**Month 3: Publication**
- Create YYYY-QX-update.md
- Update CHANGELOG.md
- Academic citation updates

## Sources
1. **IT Harvest**: Primary vendor landscape data (partnership pending)
2. **Expert Network**: Validation interviews
3. **Blog Integration**: security-data-commons-blog insights
4. **Industry Analysts**: Gartner, Forrester, IDC reports
5. **Production Deployments**: Case study validation

## Integration with Book
Supports Chapter 9 "Technology State Assessment" with quarterly vendor landscape snapshots that remain citable as research evolves.

## Version Control
- Each quarterly update creates a new `YYYY-QX-update.md` file
- Previous versions never edited (citation stability)
- CHANGELOG.md tracks all revisions
- Enables academic citation: "According to the Q4 2025 vendor landscape snapshot..."

---

## MCP Vendor Database Integration

**Status**: ✅ COMPLETE (October 23, 2025 - Session 2)

**Integration Summary**: See `MCP-VENDOR-INTEGRATION-SUMMARY.md` for comprehensive details

**Quick Facts**:
- 71 vendors across 9 categories (SIEM, Query Engine, Streaming, Lakehouse, ETL/ELT, Observability, Object Storage, Data Catalog, Data Virtualization)
- 110 evidence sources (84% Tier A quality)
- Zero Tier D (marketing) sources
- Automated maintenance: Weekly refresh validates analyst URLs, monthly GitHub metrics tracking
- Quality grade: A (Excellent) - 92.7/100

**Integration Value**:
- IT Harvest partnership accelerated (10 query engines baseline ready)
- First quarterly update effort reduced ~60% (baseline data exists)
- Academic publication validated (110 evidence sources)
- Vendor landscape population ready (vendor-database.json seeds directory)

**Files**:
- Source: `vendor-database.json` (71 vendors, 79 vendor-level evidence sources)
- Integration Summary: `MCP-VENDOR-INTEGRATION-SUMMARY.md` (~25 KB comprehensive documentation)
- MCP Server: `security-architect-mcp-server/data/vendor_database.json` (sync retired — that repo was archived 2026-07-01; this JSON is now the frozen 71-vendor baseline, with current vendor coverage living in the book's appendix-g)

---
**Last Updated**: October 23, 2025 (MCP vendor baseline complete - IT Harvest partnership ready for acceleration)
