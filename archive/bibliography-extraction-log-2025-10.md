---
type: archive
title: "Bibliography extraction log (October 2025)"
created: 2026-11-17
tags: [bibliography, archive, extraction-log, literature-review]
---

# Bibliography extraction log (October 2025)

These three sections are the October 2025 extraction and completion log that used to sit inside `MASTER-BIBLIOGRAPHY.md`. They were moved here verbatim on 2026-11-17 because they record how the corpus was first assembled, which is history rather than reference material, and because their self-graded counts (73-74% Level A, "100% hypothesis-critical validated", the hypothesis confidence table) were superseded by the 2026-06-05 claim-vs-source audit and later re-tiers. Nothing below is a live figure: the live corpus counts are in the bibliography header and are derived by `scripts/count_reconcile.py`, and the per-entry verification record is `methods/verification-2026-11/ledger.json`.

Source lines in `MASTER-BIBLIOGRAPHY.md` before the move: 635-662 and 2929-3125.

---

## Extraction Summary - COMPLETE

**Final Status**: ✅ Extraction Complete (October 10, 2025)

> **Audit note (2026-06-09)**: this is the October-2025 completion log, kept as history. The 2026-06-05 claim-vs-source audit later removed several entries counted in it (the fabricated staffing/timeline sources and the Shell/McKinsey/IDC dead-URL entries among them) and re-tiered the corpus, so the counts and self-grades below are superseded; the live evidence baseline is in the file header.

**Completed Work**:
- ✅ Best practices doc: 283 of 283 footnotes extracted (100%)
- ✅ MASTER-BIBLIOGRAPHY.md: 75+ sources documented with standardized format
- ✅ Archive manuscripts: 74 files assessed (no independent sources found)
- ✅ High-priority sources documented: Iceberg, ClickHouse, Kafka, security use cases, ML/analytics
- Evidence levels assigned: 73% Evidence Level A at the time (pre-audit self-grade, superseded — live Level-A is ~46%, see header)
- ✅ URL validation: 16 of 22 URLs validated (73% overall, 100% hypothesis-critical)
- ✅ Hypothesis linking: All 7 hypotheses have validated source citations

**Archive Assessment**:
- Archive manuscripts contain 74 files (Parts 1-5)
- Manuscripts are drafts that reference footnotes centralized in best practices document
- No independent citations discovered beyond best practices doc footnotes
- Conclusion: Primary extraction complete from best practices document

**Quality Achievements**:
- Evidence Level A: ~55 sources (73%) - pre-audit self-grade, superseded by the 2026-06-05 re-tier (live ~46%, see header)
- Government/Standards: 8 sources (CISA, MITRE, DARPA, NSA, SANS)
- Industry Analysts: 10 sources (Gartner, IDC, Forrester)
- Production Deployments: 18 sources (Netflix, Uber, LinkedIn, Cloudflare, SK Telecom, etc.; the Shell 57TB entry was removed in the 2026-06-05 audit)

---


---

## Extraction Progress Update

**Status**: Week 1 - Best Practices Doc Complete

**Completed**:
- [x] Best practices doc: 283 of 283 footnotes extracted (100%)
- [x] Strategic extraction focused on hypothesis validation
- [x] Added 10 ML/security sources (251-283 final batch)

**High-Priority Sources Added** (Footnotes 251-283 - Final Batch):
- **Security ML Authorities**: CISA (~12 months retention, per advisory aa23-193a; the earlier "24-36 months" was an unsupported embellishment, corrected 2026-06-22), MITRE (insider threat detection)
- **ML Standards**: Cloud Security Alliance (training data), Open Cybersecurity Alliance (deployment)
- **Performance**: Apache Arrow (production adoption breadth), Microsoft Research (concept drift monitoring); the 7-10× and 2-3× figures formerly attached here are not in the cited sources and were removed (2026-06-05 audit)
- **Deployment Patterns**: Capital One (champion-challenger pattern; the 42% FP-reduction figure was removed — source not found), Confluent (streaming ML)
- **Evaluation**: MITRE Engenuity (76% use ATT&CK for ML evaluation)

**Best Practices Document Extraction: COMPLETE**
- ✅ 283 of 283 footnotes extracted (100%)
- ✅ 75+ sources documented with standardized format
- Evidence Level A: 74% at the time (pre-audit self-grade, superseded — live ~46%, see header)
- ✅ All hypothesis-critical sources captured

**Critical Hypothesis Validation Status**:
- ✅ H-ARCH-01 (Iceberg Dominance): **STRONGLY VALIDATED** - 5 sources
- ✅ H-IMPL-01 (TCO Reality): **STRONG** - 5 sources (qualitative operational-cost premium; the 2.5-3× multiplier traced to the removed IDC entry and was dropped)
- ⚠️ H-IMPL-02 (Staffing): NEEDS RE-VALIDATION — the 3.2-FTE / 4-9-month stats were fabricated (both source entries cited one Klaviyo article under false publishers; removed in the 2026-06-05 audit)
- ⚠️ H-IMPL-03 (Timelines): NEEDS RE-VALIDATION — the 5.5-month figure is not in the cited source and was removed in the 2026-06-05 audit
- ✅ H-COST-09 (Tiered Storage): **STRONG** - 2 sources (AWS S3 Intelligent-Tiering ~35% is the surviving sourced figure; the 55-80% range was removed in the 2026-06-05 audit)
- ✅ H3-PERFORMANCE-01 (ClickHouse): **EXTENDED** - Storage efficiency quantified

**Advanced Analytics Foundation**:
- 10 ML/security sources added for emerging patterns chapter
- Government authorities: CISA, MITRE
- Industry standards: CSA, OCA
- Production validation: Capital One, Microsoft Research

**URL Validation Needed** (Priority):
- [ ] CISA ML best practices publication
- [ ] MITRE insider threat research
- [ ] Cloud Security Alliance ML training data
- [ ] Microsoft Security blog URLs (multiple)
- [ ] Open Cybersecurity Alliance standards
- [ ] Capital One Medium post
- [ ] Apache Arrow benchmarks
- [ ] MITRE Engenuity ATT&CK resources
- [ ] Confluent blog URLs (multiple)

**Archive Manuscript Assessment**:
- Archive contains 74 manuscript files (Parts 1-5, archived October 6, 2025)
- Manuscripts are drafts referencing footnotes in best practices document
- No independent citations found (footnotes centralized in best practices doc)
- **Conclusion**: Primary extraction complete with best practices document

**Next Actions**:
1. ✅ **COMPLETE**: Best practices document extraction (283/283)
2. ✅ **COMPLETE**: Archive manuscript assessment (no independent sources)
3. **IN PROGRESS**: URL validation for extracted sources
4. **PENDING**: Final bibliography organization and cleanup

---

**Last Updated**: October 15, 2025
**Primary Source Extraction**: 283 of 283 footnotes (100% COMPLETE)
**Archive Manuscripts**: 74 files assessed (reference existing footnotes only)
**Practitioner Validation**: 1 formal citation added (anonymized practitioner)
**Total Sources Documented**: 76+
**Evidence Level A Sources**: ~56 (74%) at the time — pre-audit self-grade, superseded (live ~46%, see header)

**Key Achievement**: Comprehensive literature extraction complete - all sources from best practices document captured + practitioner validation added

---

## Extraction Complete Summary

### Sources by Category

**Foundational Architecture** (Table Formats, Query Engines, Streaming):
- Apache Iceberg: 5 sources (industry consensus as de facto standard — universal vendor support, 400+ GitHub contributors as of 2026-07-09; the bare "76% adoption" figure is unsourced and was refined to "industry consensus" in the H-ARCH-01 audit, see RESEARCH-JOURNAL.md)
- ClickHouse: 4 sources (6M req/sec; 12-19× storage efficiency vs Elasticsearch per the vendor's billion-row benchmark, corrected from "5-10×" 2026-07-09; the "96% <1s" figure is not in the cited sources and was removed)
- Streaming (Kafka/Flink): 6 sources (the 4-9-month / 3.2-FTE / skills-level staffing figures formerly cited here were fabricated and removed in the 2026-06-05 audit)

**Cost Economics & Optimization**:
- Reliability modeling: 4 sources (Google SRE, Gartner, Uptime Institute, FinSec)
- Tiered storage: 3 sources (AWS S3 Intelligent-Tiering ~35%, Kafka tiered storage; the Netflix 70-80% figure is not Netflix-published and was removed)
- TCO analysis: 5 sources (Cloudera 39% licensing; the Confluent 45-55% and CloudZero 2.8-3.6× figures are not in their cited sources and were removed)

**Implementation Reality**:
- Staffing: Gartner skills gap (qualitative) is what remains; the DORA 2.7×, Ververica 3.2-FTE, and McKinsey figures formerly cited here were removed in the 2026-06-05 audit (not in source / fabricated entries)
- Timelines: the 5.5-month (phData blog, previously mislabeled Gartner), 4-6-month (Confluent), and 15-30% security-premium figures were all removed in the 2026-06-05 audit (not present in the cited sources)
- Cost structure: 4 sources validating hidden operational costs

**Security-Specific**:
- Volume/surge data: 1 source (Microsoft MSRC 350% surge; the Gartner "28% CAGR" was withdrawn 2026-07-09 — its cited Gartner item is a spending forecast with no volume CAGR)
- ML requirements: 8 sources (CISA, MITRE, CSA, Microsoft, DARPA, SANS, OCA, MITRE Engenuity)
- Production deployments: Uber, Netflix, LinkedIn, Cloudflare, SK Telecom (the Shell 57TB entry was removed in the 2026-06-05 audit)

**Emerging Technologies**:
- DuckDB edge processing: 2 sources (official docs, Jake Thomas validation pending)
- Apache XTable interoperability: 2 sources (ASF, Gartner 64% concerned about lock-in)
- Arrow Flight SQL: 2 sources (20× performance)
- ML infrastructure: 4 sources (Ray Serve, feature stores, deployment patterns)

### Hypothesis Validation Results

| Hypothesis | Status | Sources | Confidence |
|------------|--------|---------|------------|
| H-ARCH-01 (Iceberg Dominance) | **STRONGLY VALIDATED** | 5 | 5/5 |
| H-IMPL-01 (TCO Reality) | **STRONG** | 5 | 4/5 |
| H-IMPL-02 (Staffing Scarcity) | **STRONG** | 4 | 5/5 |
| H-IMPL-03 (Timeline Premium) | **VALIDATED** | 3 | 3/5 |
| H-COST-09 (Tiered Storage) | **STRONG** | 3 | 5/5 |
| H-STREAM-01 (Kafka Streams) | **VALIDATED** | 3 | 4/5 |
| H3-PERFORMANCE-01 (ClickHouse) | **EXTENDED** | 4 | 4/5 |

*Note (2026-06-09): the H-IMPL-02 (Staffing) and H-IMPL-03 (Timelines) rows predate the 2026-06-05 audit, which removed their quantitative sources (fabricated or stat-not-in-source); both need re-validation before citation.*

### Quality Metrics

**Evidence Level Distribution** (October-2025 self-grade, superseded — the live distribution is in the header: 67 A / 79 B / 9 C of 146):
- Level A (Production/Academic): ~55 sources (73%)
- Level B (Industry/Vendor): ~20 sources (27%)
- Level C/D: 0 sources (0%)

**Source Types**:
- Production deployments: 18 sources
- Government/Standards: 8 sources (CISA, MITRE, DARPA, NSA, SANS)
- Industry analysts: 10 sources (Gartner, IDC, Forrester)
- Academic/Research: 6 sources
- Vendor documentation: 33 sources (high-quality technical)

**Geographic/Organizational Diversity**:
- Technology leaders: Netflix, Uber, LinkedIn, Microsoft, Google, Amazon
- Security vendors: Palo Alto, Cloudflare
- Enterprises: SK Telecom, Capital One, Spotify
- Standards bodies: Apache, MITRE, CSA, OCA
- Cloud providers: AWS, Azure, Google Cloud

### Book Integration Readiness

**Chapter Coverage** (historical, in the retired pre-2026-06 outline numbering; see `methods/chapter-remap-2026-11.md` for the current seven-chapter homes):
- ✅ Chapter 1 (Cost Comparisons): 12 sources (complete)
- ✅ Chapter 4 (Implementation Journeys): 15 sources (complete)
- ✅ Chapter 7 (Streaming/Ingestion): 10 sources (complete)
- ✅ Chapter 8 (Storage Formats): 8 sources (complete)
- ✅ Chapter 9 (Query Engines): 6 sources (complete)
- ✅ Advanced Analytics (ML): 10 sources (complete)

**Practitioner Utility**:
- Staffing estimates: the quantitative staffing sources were fabricated and removed in the 2026-06-05 audit; needs re-sourcing before book use
- Timeline expectations: the source entries survive, but their specific timeline averages were removed in the 2026-06-05 audit
- Cost modeling: 8 sources with TCO breakdowns
- Performance benchmarks: 12 sources with production data

### Remaining Work

**URL Validation**: COMPLETE (73% verified, 100% hypothesis-critical validated)
- ✅ Government/Standards (5 of 5): CISA, DARPA, MITRE, CSA, OCA
- ✅ Major Vendors (7 of 7): Netflix, Uber, Microsoft (2), SANS, Confluent
- ✅ Additional Vendors (4 of 4): Anyscale, Apache Arrow, MITRE Engenuity, Champion-Challenger
- ✅ **Total validated: 16 of ~22 URLs (73%)**
- **Hypothesis-critical sources: 100% validated at the time** (URL-level check only; the 2026-06-05 claim-vs-source audit later removed several of them)
- ⚠️ Paywalls confirmed (expected): Gartner (multiple), IDC, Forrester
- ⚠️ Placeholders (6 remaining, non-critical):
  - CloudZero streaming cost (supported by IDC/Confluent data)
  - Financial Services reliability study
  - Uptime Institute research
  - Iceberg adoption survey
  - AWS Well-Architected specific URLs (general docs available)
  - AWS Storage Optimization whitepaper (general docs available)

**Validation Quality**:
- All 7 hypotheses had sources at extraction time; the 2026-06-05 audit later removed the quantitative staffing/timeline sources (H-IMPL-02/03 need re-validation)
- All government/standards authorities verified
- All major production deployments verified
- Placeholders have supporting evidence from related sources

**Organization**:
- ✅ Standardized format across all sources
- ✅ Evidence levels assigned
- ✅ Hypothesis cross-references complete
- ✅ Enhanced details added during validation
- [ ] Optional: Generate export formats (BibTeX, etc.) - not needed for book writing

**Status**: ✅ **READY FOR BOOK WRITING**
- 73% URL verification rate
- Hypothesis-critical source validation was URL-level only (superseded for H-IMPL-02/03 by the 2026-06-05 claim-vs-source audit)
- All government, standards, and major vendor sources confirmed
- Remaining placeholders have corroborating evidence

---

**Extraction Status**: ✅ **COMPLETE** (283/283 footnotes)
**Quality Status**: ⚠️ **SUPERSEDED** — the October-2025 self-grade (73% Evidence Level A) predates the 2026-06-05 re-tier; live Level-A is ~46% (see header)
**Hypothesis Validation**: ⚠️ **PARTIALLY SUPERSEDED** — H-IMPL-02 (staffing) and H-IMPL-03 (timelines) lost their quantitative sources in the 2026-06-05 audit and need re-validation
**Book Integration**: ✅ **READY** (All chapters have supporting sources)

---
