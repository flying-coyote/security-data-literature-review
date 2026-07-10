# Literature Review Extraction Plan

> **Dated correction banner (2026-07-10, part-3 verification sweep).** Everything below is the **historical record of the October-2025 extraction as it graded itself at the time** — read the self-grades as that record, NOT as current achievement, because the 2026-06/07 fabrication audits overturned several of them:
> - **"73% Evidence Level A"** (asserted three times below): the live, dashboard-computed figure is **41.6% (77/185)** as of 2026-07-10 — the October self-grade is the masked number the audit exposed (see README/CLAUDE.md for the current derivation).
> - **"All 7 hypotheses validated with verified sources" / "All hypothesis-critical sources verified"**: contradicted by the post-overturn standing (roughly 1 strong / 2 high / the rest at 1-2/5 or pending re-score; several formerly "critical" sources — DORA multipliers, Ververica, IDC, MIT-TR, AWS/Netflix tiered-storage — were confirmed nonexistent or withdrawn). See `analysis-bundles/hypothesis-confidence-matrix.md` (banner) and `RESCORE-PROPOSAL-2026-07.md`.
> - **Count inconsistency, unreconciled**: "6 hypotheses formalized" (Total Work) vs "All 7 hypotheses validated" (Final Statistics) vs "6 new hypotheses (26→32)" (Deliverables) — the validated-hypothesis count was never reconciled (CLAUDE.md flags this too).
> - **MASTER-HYPOTHESIS-TRACKER.md is NOT in this repository** — it lives in the project1 hub repo (`~/project1/01-knowledge-base/MASTER-HYPOTHESIS-TRACKER.md`); the Deliverables pointer below is external.
> - The source-material claims (283 footnotes; 74 archive manuscripts) reference an archive external to this repo and have not been re-verified — treat as the October-2025 record, not checked facts.
> - "16 of 22 URLs validated (73%)" is historical and fine as record under this banner.

**Purpose**: Extract and consolidate literature sources from archived manuscripts into living literature review
**Source Materials**: Best practices document (2024-04-15) + 74 archived manuscript files
**Target**: Systematic bibliography organized by topic for book foundation
**Status**: ✅ **COMPLETE** (October 10, 2025)
**Last Reviewed**: October 15, 2025

**Note**: This plan was created for a 4-week extraction timeline (Oct 14 - Nov 8). Actual execution completed ahead of schedule on October 10, 2025.

---

## ✅ EXTRACTION COMPLETE - SUMMARY

**Completion Date**: October 10, 2025
**Total Work**: 283 footnotes extracted, 16 URLs validated, 6 hypotheses formalized

**Final Statistics**:
- ✅ 283 of 283 footnotes extracted (100%)
- ✅ 75+ sources documented with standardized format
- ✅ 73% Evidence Level A (production/academic sources)
- ✅ 16 of 22 URLs validated (73%, 100% hypothesis-critical)
- ✅ 74 archive manuscripts assessed (no independent sources)
- ✅ All 7 hypotheses validated with verified sources

**Deliverables**:
- ✅ MASTER-BIBLIOGRAPHY.md: Complete with 75+ sources
- ✅ LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md: 6 hypotheses identified
- ✅ MASTER-HYPOTHESIS-TRACKER.md: Updated with 6 new hypotheses (26→32)
- ✅ All hypothesis-critical sources verified
- ✅ Book integration ready for all chapters

**Key Achievement**: Living literature review foundation complete with strong evidence base supporting all book arguments.

---

## Phase 1: Source Document Inventory (Week 1)

### Archive Sources Identified

**Primary Source Documents**:
1. Best practices document (2024-04-15) - **283 footnotes** (comprehensive with citations)
2. Archived manuscript files - **74 files across 5 parts** (drafts referencing best practices footnotes)

**Archive Structure** (external to this repository):
- Part 1 (Crisis): 10 files - Problem definition, evidence-based approach
- Part 2 (Framework): 10 files - Modern data stack architecture
- Part 3 (Components): 12 files - Technology deep-dives
- Part 4 (Implementation): 25 files - Practical deployment
- Part 5 (Future): 26 files - Emerging technologies

**Note**: Archive manuscripts assessed and found to reference footnotes centralized in best practices document. No independent sources discovered beyond the 283 footnotes in best practices doc.

### Extraction Strategy

**Method**: Systematic file review extracting:
1. **Citations**: All footnoted sources, URLs, paper references
2. **Vendor Documentation**: Official docs referenced
3. **Performance Benchmarks**: Quantitative claims with sources
4. **Expert Quotes**: Attributed practitioner insights
5. **Research Papers**: Academic citations

**Tool**: Script to extract all URLs, footnotes, and citations into structured format

---

## Phase 2: Topic-Based Organization (Week 1-2)

### Literature Review Categories

Based on PLAN.md priorities and book structure:

#### Category 1: Foundational Architecture
**Target Files**:
- Best practices doc: Sections on Lambda/Kappa, Query Engines, Streaming
- Archive Part 2: Modern data stack framework chapters

**Extract**:
- Table format comparisons (Iceberg, Delta, Hudi)
- Query engine benchmarks (Trino, Dremio, ClickHouse)
- Streaming architecture patterns (Kafka, Flink)

#### Category 2: Security-Specific Data Characteristics
**Target Files**:
- Archive Part 1: Crisis/problem definition chapters
- Best practices doc: Security analytics sections

**Extract**:
- Volume estimates (2-12 TB/day validation)
- Cost comparisons (SIEM vs object storage)
- Workload characteristics (real-time + historical)

#### Category 3: Technology Deep-Dives
**Target Files**:
- Archive Part 3: Component chapters (ch07-ingestion, ch08-storage, ch09-query, ch10-analytics)
- Best practices doc: Platform options analysis

**Extract**:
- Vendor capability matrices
- Performance benchmarks
- Feature comparisons

#### Category 4: Implementation Patterns
**Target Files**:
- Archive Part 4: Implementation chapters
- Best practices doc: Implementation considerations

**Extract**:
- Deployment patterns
- Organizational readiness frameworks
- Change management strategies

#### Category 5: Emerging Technologies
**Target Files**:
- Archive Part 5: Future evolution chapters
- Best practices doc: Emerging technologies section

**Extract**:
- Technology trends
- Adoption timelines
- Expert predictions

---

## Phase 3: Citation Validation & Updates (Week 2-3)

### Validation Checklist

For each extracted source:
- [ ] URL still active (check for 404s)
- [ ] Content still relevant (2024-2025 validation)
- [ ] Author/vendor credibility verified
- [ ] Citation format standardized
- [ ] Evidence level assigned (A/B/C/D per methodology)

### Update Requirements

**2025 Refresh Needed**:
- Pricing data (Splunk, Datadog, cloud storage)
- Vendor capabilities (new releases, acquisitions)
- Market trends (Databricks/Tabular, Snowflake/Polaris)
- Performance benchmarks (version-specific)

---

## Phase 4: Living Review Structure Creation (Week 3-4)

### Target Directory Structure

```
living-literature-review/
├── foundations/
│   ├── table-formats-iceberg-delta-hudi.md
│   ├── query-engines-landscape.md
│   ├── streaming-architectures.md
│   └── storage-separation-compute.md
├── security-specific/
│   ├── data-volume-validation.md
│   ├── cost-comparisons-siem-vs-modern.md
│   ├── workload-characteristics.md
│   └── ocsf-adoption-tracking.md
├── vendor-landscape/
│   ├── query-platforms-trino-dremio-denodo.md
│   ├── olap-analytics-clickhouse-starrocks.md
│   ├── catalogs-polaris-unity-gravitino.md
│   └── capability-matrix.md
├── implementation/
│   ├── deployment-patterns.md
│   ├── organizational-readiness.md
│   └── change-management.md
├── emerging/
│   ├── ai-enhanced-administration.md
│   ├── duckdb-edge-processing.md
│   └── trend-analysis.md
└── MASTER-BIBLIOGRAPHY.md
```

### Bibliography Format

**Standardized Entry**:
```markdown
## [Source Title]

**Authors**: [Names]
**Date**: [Publication/Access Date]
**URL**: [Link]
**Evidence Level**: [A/B/C/D]
**Relevance**: [Book chapters, hypotheses]
**Key Findings**: [Bullet summary]
**Citations**: [Where used in book]
**Notes**: [Credibility assessment, validation status]
```

---

## Phase 5: Integration with Book & Blog (Week 4)

### Book Integration

**Chapter 1-2** (Foundation):
- Security data volume sources → foundations/data-volume-validation.md
- Cost comparison sources → security-specific/cost-comparisons.md
- Data engineering resources → foundations/*.md

**Chapter 3-5** (Decision Framework):
- Architecture pattern sources → foundations/
- Vendor comparison sources → vendor-landscape/

**Chapter 6-10** (Components):
- Technology deep-dives → vendor-landscape/
- Implementation patterns → implementation/

### Blog Integration

**Security Data Commons Blog**:
- Technical deep-dives cite living review sources
- Quarterly updates pull from vendor-landscape/
- Expert interviews validate emerging/ content

### IT Harvest Integration

**Collaboration Points**:
- Query engines pilot → query-platforms-trino-dremio-denodo.md
- Vendor data supplements capability-matrix.md
- Quarterly updates refresh vendor-landscape/

---

## Original Execution Timeline (Planned)

**Note**: This was the original 4-week plan. Actual execution completed ahead of schedule on October 10, 2025.

### Week 1 (Oct 14-18) - Planned
- ✅ Create extraction plan (completed early)
- ✅ Extract citations from best practices document (283 of 283)
- ✅ Scan archive Part 1-2 for foundational sources (assessed all 74 files)
- ⏳ Create foundations/ directory with initial files (deferred to Phase 2 with IT Harvest)

### Week 2 (Oct 21-25) - Completed Early
- ✅ Extract citations from archive Part 3 (all parts assessed)
- ✅ Validate URLs and update broken links (16 of 22, 73%)
- ❌ security-specific/ topic directory — not adopted; the empty stub was removed 2026-07-09, topic coverage consolidated into MASTER-BIBLIOGRAPHY.md (organized by topic). The proposed topic-directory tree above was superseded by that consolidation.
- ✅ Complete MASTER-BIBLIOGRAPHY.md (75+ sources documented)

### Week 3 (Oct 28-Nov 1) - Planned
- ⏳ Expert interview integration (Lisa Cao, Jake Thomas - scheduled)
- ✅ Validate evidence levels for all sources (73% Evidence Level A achieved)

### Week 4 (Nov 4-8) - Planned
- ⏳ Create directory structure (deferred pending IT Harvest partnership)
- ⏳ IT Harvest pilot integration (pending partnership establishment)
- ✅ Living review foundation v1.0 complete (extraction phase done Oct 10)

---

## Success Metrics - ACHIEVED

**Quantitative Results**:
- ✅ 75+ unique citations extracted (target: 100+, sufficient for book needs)
- ✅ 73% URLs validated and active (16 of 22, 100% hypothesis-critical)
- ✅ All 10 book chapters have linked bibliography in MASTER-BIBLIOGRAPHY.md
- ✅ Evidence Level A sources: ~55 sources (73%, target: >50)

**Qualitative Results**:
- ✅ Book writing informed by comprehensive literature base (283 sources extracted)
- ✅ Blog posts can cite authoritative sources (75+ documented)
- ⏳ IT Harvest collaboration planned (vendor data for Phase 2)
- ⏳ Expert network validates emerging technology claims (interviews scheduled Week 3)

---

## Tools & Automation

### Citation Extraction Script

**Purpose**: Automated extraction of footnotes, URLs, citations from markdown files

```python
# Pseudocode - to be implemented
def extract_citations(file_path):
    # Parse markdown for [^footnote] references
    # Extract URLs from links
    # Extract vendor documentation references
    # Extract research paper citations
    # Output structured JSON/CSV
```

**Input**: Archive markdown files
**Output**: CSV with [file, citation_type, source, context]

### URL Validation Script

**Purpose**: Check all extracted URLs for 404s, update dead links

### Bibliography Generator

**Purpose**: Convert extracted citations to standardized MASTER-BIBLIOGRAPHY.md format

---

## Risk Management

### Potential Issues

**Issue 1: Broken Links**
- **Mitigation**: Wayback Machine for dead URLs, update to current vendor docs

**Issue 2: Outdated Benchmarks**
- **Mitigation**: Flag 2024 data for 2025 revalidation, expert network update

**Issue 3: Duplicate Citations**
- **Mitigation**: Deduplication script, canonical URL normalization

**Issue 4: Vendor Bias**
- **Mitigation**: Multi-source validation, contradiction analysis per existing methodology

---

## Next Actions (Immediate)

1. Extract footnotes from best practices document (207 lines)
2. Scan archive/manuscript/part-1-crisis/ for citations
3. Create foundations/table-formats-iceberg-delta-hudi.md with initial sources
4. Begin MASTER-BIBLIOGRAPHY.md with standardized format

**Owner**: Jeremy Wiley
**Timeline**: Week 1-4 (Oct 14 - Nov 8)
**Dependencies**: Archive access, IT Harvest partnership, expert interviews (Week 3)
