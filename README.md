# Living Literature Review for "Modern Data Stack for Cybersecurity"

**Purpose**: Comprehensive literature review and research foundation for book
**Last Updated**: October 10, 2025
**Last Reviewed**: October 15, 2025
**Status**: Phase 1 (Literature Extraction) COMPLETE | Phase 2 (Vendor Landscape) PENDING

---

## Executive Summary

This repository contains a **completed systematic literature review** supporting the book "Modern Data Stack for Cybersecurity." The review bridges cybersecurity and data engineering domains with rigorous, evidence-based research.

**Current Status - Phase 1 Complete**:
- ✅ 283 footnotes extracted from best practices document
- ✅ 75+ sources documented with standardized format
- ✅ 73% Evidence Level A (production/academic sources)
- ✅ 7 hypotheses validated with quantitative evidence
- ✅ 16 of 22 URLs validated (73% overall, 100% hypothesis-critical)
- ✅ All book chapters have supporting source citations

**Future Work - Phase 2 Planned**:
- ⏳ IT Harvest partnership for vendor landscape data
- ⏳ Quarterly technology state assessment updates
- ⏳ Implementation of structured directory organization (see below)

---

## Current Repository Contents

**Core Documentation Files**:
1. **MASTER-BIBLIOGRAPHY.md** - Complete bibliography with 75+ sources, evidence levels, and hypothesis validation
2. **LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md** - Gap analysis identifying 6 new hypotheses from literature
3. **LITERATURE-EXTRACTION-PLAN.md** - Systematic extraction methodology (PRISMA-aligned)
4. **PUBLICATION-VENUE-RECOMMENDATIONS.md** - Academic publication strategy for literature review

---

## Proposed Future Structure (Phase 2 - Not Yet Implemented)

When IT Harvest partnership is established and quarterly updates begin, the repository will expand to:

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

## Planned Quarterly Update Process (Phase 2)

**Quarterly Cycle** (Jan, Apr, Jul, Oct):
1. **Month 1**: IT Harvest data refresh + platform updates
2. **Month 2**: Expert validation + blog synthesis
3. **Month 3**: Publication + citation updates

**Version Control**:
- Each update creates new `YYYY-QX-update.md`
- CHANGELOG.md tracks all revisions
- Enables academic citation of specific versions

**Sources**:
1. IT Harvest vendor data (primary - partnership pending)
2. Blog post insights (ongoing)
3. Expert network validation (Lisa Chao, Jake Thomas, etc.)
4. Matthew Mullins + practitioner feedback

---

## Integration Points

**Book Chapters**: All chapters have supporting citations in MASTER-BIBLIOGRAPHY.md
**Blog**: Deep-dives cite literature review sources
**IT Harvest**: Vendor data integration planned for Chapter 9 "Technology State Assessment"
**Expert Network**: Validation interviews referenced throughout

---

## Key Research Findings

**Hypothesis Validation Results**:
- H-ARCH-01 (Iceberg Dominance): STRONGLY VALIDATED - 76% adoption, 5 sources
- H-IMPL-01 (TCO Reality): STRONG - 2.5-3× operational costs, 5 sources
- H-IMPL-02 (Staffing Scarcity): STRONG - 2.7× staff required, 4 sources
- H-IMPL-03 (Timeline Premium): VALIDATED - 5.5 months average, 3 sources
- H-COST-09 (Tiered Storage): STRONG - 55-80% cost savings, 3 sources
- H3-PERFORMANCE-01 (ClickHouse): VALIDATED - 6M req/sec, 96% <1s queries
- H-STREAM-01 (Kafka Streams): VALIDATED - Production security patterns, 3 sources

**Quality Metrics**:
- Evidence Level A: 73% (production deployments, peer-reviewed research)
- Government/Standards Sources: 8 (CISA, MITRE, DARPA, NSA, SANS)
- Industry Analysts: 10 (Gartner, IDC, Forrester)
- Production Deployments: 18 (Netflix, Uber, LinkedIn, Cloudflare, Shell, SK Telecom, etc.)

---

**Current Phase**: Literature Review Foundation Complete
**Next Phase**: IT Harvest partnership establishment → Vendor landscape integration
**Next Action**: Pilot with query engines category (pending IT Harvest partnership)
**Maintained By**: Jeremy Wiley
