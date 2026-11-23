---
type: reference
title: "PRISMA-Aligned Systematic Literature Review Methodology"
created: 2025-10-21
tags: [prisma, methodology, systematic-review, evidence-tiers, literature-review]
---

# Methodology: Systematic Literature Review

**Purpose**: Academic methodology documentation for "Modern Data Stack for Cybersecurity" literature review
**Framework**: PRISMA-aligned systematic extraction and quality assessment
**Review Type**: Living literature review with quarterly updates
**Last Updated**: November 17, 2026

---

## 1. Overview

This systematic literature review employs a PRISMA-aligned methodology to consolidate research on modern data stack architectures for cybersecurity applications. The review bridges two distinct domains—cybersecurity and data engineering—to provide an evidence-based foundation for practitioners and researchers.

The document reads in the order the method runs: the question and its scope (§1, with the isolation-first research questions added in November 2025 kept at §5.4 because other files cite them there), the two search arms (§2.1-§2.3 curation, §2.4 the database search), critical appraisal of what the search returned (§2.5), tiering and credibility assessment (§3), extraction (§4), hypothesis scoring (§5), synthesis (§6), and limitations with the reproducibility record (§7). Sections 8-9 hold the quality measures and the book integration, and PUBLICATION-MANUSCRIPT.md §2 remains the methods statement of record wherever the two differ.

### 1.1 Research Objectives

1. **Primary**: Synthesize evidence on modern data stack technologies (table formats, query engines, streaming architectures) applied to security analytics
2. **Secondary**: Validate quantitative hypotheses regarding adoption rates, implementation costs, performance characteristics, and organizational requirements
3. **Tertiary**: Establish a living literature review infrastructure supporting quarterly updates for technology currency

### 1.2 Scope and Boundaries

**In Scope**:
- Modern data stack technologies (2018 onward): Apache Iceberg, query engines (Trino, Dremio, ClickHouse, DuckDB), streaming platforms (Kafka, Flink)
- Security-specific applications: SIEM alternatives, security data lakes, detection engineering platforms
- Implementation evidence: Total cost of ownership (TCO), staffing requirements, deployment timelines
- Production deployments: Enterprise case studies, performance benchmarks, operational patterns

**Out of Scope**:
- Traditional SIEM implementations (pre-2018 architectures)
- General-purpose data engineering without security focus
- Operational tooling implementations (focus on research/evidence)
- Vendor marketing materials (unless supported by production data)

**Time Period**: 2018 onward (the database arm's date floor), with no fixed end-date because the review is living, and pre-2018 sources for named foundational context only.

---

## 2. Literature Search Strategy

Identification runs on two arms, in the PRISMA 2020 sense. The **curation arm** (§2.1-§2.3) is "identification via other methods": it built the corpus between 2025 and 2026, beginning with the footnote extraction described below, and it still feeds the corpus through the ongoing channels in §2.2. The **database arm** (§2.4) is a systematic search of OpenAlex and dblp, designed and executed retrospectively on 2026-07-13 to test what the curated corpus had missed. The review therefore discloses itself as a retrospectively-verified curated review rather than a prospective systematic review; the manuscript's methods section (PUBLICATION-MANUSCRIPT.md §2.2) is the statement of record, and this section summarizes both arms rather than duplicating the protocol files. *(Restructured 2026-07-16: earlier versions of this section described only the footnote-extraction arm while §10 claimed a "PRISMA 2020 two-arm methodology"; the database-arm summary in §2.4 was added so the two statements agree.)*

### 2.1 Source Documents (Curation Arm: Origin)

The systematic extraction process identified two primary source categories:

**Primary Sources**:
1. **Best Practices Document** (2024-04-15): Comprehensive manuscript with 283 footnotes spanning foundational architecture, security implementations, cost analysis, and emerging technologies
2. **Archive Manuscripts** (74 files): Draft chapters across 5 parts (Crisis, Framework, Components, Implementation, Future) referencing centralized best practices footnotes

**Assessment**: Archive manuscripts were evaluated and found to reference footnotes centralized in the best practices document. No independent citations were discovered beyond the 283 footnotes, establishing the best practices document as the primary extraction target.

### 2.2 Supplementary Source Identification (Curation Arm: Ongoing Channels)

Beyond the primary extraction from archived manuscripts:

1. **Expert Network Validation**: one practitioner conversation has taken place (anonymized, as in the manuscript's acknowledgments). Further expert interviews are prepared but have not been held, so no claim in this review is sourced to them; the public work of the practitioners approached is citable and is cited as such.
2. **Blog Integration**: source identification through the security-data-commons blog, an October-2025 channel since retired
3. **Vendor Documentation**: Official technical documentation from Apache Software Foundation, AWS, Microsoft, Google, Confluent, Databricks
4. **Government Standards**: CISA, MITRE, DARPA, NSA, SANS Institute publications
5. **Industry Analysts**: Gartner, IDC, Forrester research reports with disclosed methodology

### 2.3 Extraction Execution (Curation Arm, October 2025)

**Phase 1 (October 14-25, 2025)**: Systematic extraction of 283 footnotes from best practices document using:
- Automated URL extraction from markdown footnotes
- Manual review of vendor documentation references
- Performance benchmark identification
- Expert quote attribution verification

**Extraction Coverage** (October-2025 record; the source documents sit outside this repository and these figures are not re-verified):
- 283 of 283 footnotes extracted
- 16 of 22 URLs validated (73%); the "100% of hypothesis-critical sources" grade that accompanied it was withdrawn when several of those sources failed later verification
- Archive manuscripts: 74 files assessed (no independent sources found)

The catalogue has since grown by curation and the database search to 279 catalogued entries, 277 of them tiered (derived 2026-11-23 by `scripts/count_reconcile.py`).

### 2.4 Database Arm: Retrospective Systematic Search (2026-07-13)

Everything in §2.1-§2.3 is curation, which PRISMA 2020 accommodates as the "identification via other methods" arm but which cannot, on its own, answer the question a reviewer will ask: what does the indexed literature hold, and did this review find it? To answer it, a genuine systematic search was run after the corpus already existed — on 2026-07-13, against the already-curated corpus — and its result is reported as measured. The protocol of record is `methods/PRISMA-SEARCH-PROTOCOL-2026-07-13.md` (databases, exact query strings, date window, eligibility criteria, deduplication rule), the run report is `methods/PRISMA-RETRO-RUN-2026-07-13.md`, and the machine outputs — search log, records, and per-record screening decisions — are on disk under `methods/prisma-results/`.

**Search and flow**: OpenAlex was queried with a strict boolean title-and-abstract filter (a security term AND a data-architecture term, 2018 date floor) and dblp with eight title-level queries. The run identified 400 records (354 OpenAlex, 46 dblp), removed 5 duplicates, screened 395 on title and abstract against pre-specified inclusion/exclusion criteria, and included 40. Screening was LLM-performed against the pre-specified criteria, with every per-record decision written to `methods/prisma-results/screen-batch-*.json` so a reviewer can audit any individual call; the single-screener limitation and the absence of any subscription database are stated in the protocol.

**Reconciliation**: none of the 40 included records was already in the curated corpus — measured recall of the corpus against a systematic search of its own subject was zero (0/40; `methods/prisma-results/reconciliation.json`). The corpus and the indexed literature had been reaching nearly disjoint bodies of work, which is reported as a finding rather than softened, though the search carries a disclosed blind spot of its own: its conjunctive query cannot reach the storage-side papers (PVLDB/CIDR/SIGMOD) that the review leans on hardest, so it tested one half of the review's subject and was structurally blind to the other. A 2026-07-16 addendum to the run report corrects the run-time corpus count (eight bibliography entries were invisible to the run's block counter through a heading-level defect, fixed the same day) without affecting the 0/40 finding.

### 2.5 Critical Appraisal of the Database Arm

**Critical appraisal and incorporation**: the 40 then went through critical appraisal, a stage the topical screening had skipped — venue identity resolved at the DOI, publisher and DOAJ/Scopus/Web-of-Science status established from primaries, predatory-list and delisting checks run, and each proposed citation put to an independent second reviewer instructed to refuse under uncertainty. Fourteen did not survive: eight were published in predatory, hijacked, or delisted venues, three were not peer-reviewed at all, one could not be read at any price, and two were refused on other appraisal grounds, with the per-record reason for every disposition in `methods/prisma-appraisal-2026-07-13.json`. The surviving 26 are incorporated into the corpus (`methods/incorporated-2026-07-13.json`), and a 2026-07-16 second screen of the 355 exclusions admitted one more through the same gate, for 27 (`methods/second-screen-adjudication-2026-07-16.json`).

---

## 3. Quality Assessment Framework

### 3.1 Evidence Level Classification

All sources are classified using a four-tier evidence system. Level A is reserved for peer-reviewed research and official standards; production evidence, however good, is Level B.

#### Evidence Level A (live share 23.1% at 2026-11-23, 17.0% immediately after the 2026-08-19 tier audit re-tiered 57 entries off A once the criteria below were corrected; NO target, see 8.1a; the earlier "79% achieved" self-grade was withdrawn in the 2026-06 audit)
**Criteria**: Peer-reviewed research, and official standards. Nothing else.
**Examples**:
- Peer-reviewed publications at a named venue with real review (USENIX Security, IEEE S&P, NDSS, CCS, VLDB, SIGMOD, ICSE, NeurIPS, ICML, ACL, KDD, TMLR, or a peer-reviewed journal). An arXiv preprint with no named venue is **not** peer-reviewed and does not qualify, however eminent its authors
- Standards-body documents: NIST (SP/IR/FIPS), ISO/IEC, IETF RFC, W3C, OASIS ratified standards
- The formal specification document of an open standard (the Iceberg *table spec*, the OCSF *schema spec*) — the specification itself, not the project's documentation, release notes, governance pages or issue trackers
- **Normative reference frameworks** from a neutral, non-commercial body, published as a versioned formal specification (MITRE D3FEND, MITRE ATLAS). Owner ruling, 2026-08-19: these hold the same evidentiary position as a NIST or ISO document. Their scope is the same too — primary for taxonomy and structure, and silent on efficacy. A framework is authoritative about what it says, never evidence that following it works
- **NOT Level A**, and this is where the corpus went wrong before 2026-08-19: production case studies and deployment writeups, vendor engineering blogs, industry-conference talks, trade books, analyst and vendor-commissioned reports, government *advisories* (as distinct from standards), consortium and foundation announcements, and official project documentation. All are Level B. (The earlier Shell entry was removed in the 2026 audit — dead URL, unverifiable)

**Current Achievement**: 64 of 277 tiered entries (23.1%), live-derived 2026-11-23, reported as a measurement rather than against a target (§8.1a). The earlier "57 of 72 sources (79%) — EXCEEDS" self-grade was withdrawn in the 2026-06 audit; `scripts/count_reconcile.py` now derives this figure from per-entry markers and gates every surface that states it. The 2026-07-13 systematic-search incorporation added 26 peer-reviewed studies without moving the share, because only 11 of them tier at Level A.

#### Evidence Level B (October-2025 design bound: <27% — currently BREACHED; live share 62.5%)
**Criteria**: Practitioners and production evidence — production deployments and case studies with real numbers, vendor engineering blogs, industry-conference talks, trade books, analyst reports, expert interviews, government advisories, and official project documentation. Real evidence, not independently reviewed.
**Examples**:
- Gartner, IDC, Forrester quantitative research
- Production case studies and deployment write-ups (Netflix, Uber, Cloudflare, SK Telecom)
- Vendor technical documentation (if production-validated)

**Live share**: 173 of 277 tiered entries (62.5%), derived 2026-11-23. *(Note, 2026-07-16, when the share was 47.6% (108 of 227): the <27% figure is the October-2025 design bound, and it is currently breached — a documented consequence of the 2026-06/07 audits moving inflated Level-A entries down to B (headline stats not present in the cited source, first-person practitioner authorship on vendor channels re-tiered B), not of quality decay in the incoming sources. The original "Achieved: 21% (15 of 72)" was the October-2025 self-grade at a 72-source corpus and is preserved here as history.)*

#### Evidence Level C (live share 14.4% — 40 of 277 tiered; original design intent was "Rejected: 0%")
**Criteria**: Vendor blog posts, product documentation, and conference talks not backed by production measurement
**Policy** *(corrected 2026-07-16 to match the manuscript §2.3 and the corpus)*: Level C sources ARE catalogued, with their bias flagged and their tier stated, where they are the only available account of a system's behaviour; they never carry a hypothesis on their own. The original October-2025 protocol declared Level C "Rejected: 0% — not included in bibliography unless upgraded to Level A/B with supporting evidence", and the corpus has never matched that claim (40 of 277 tiered entries are Level C, derived 2026-11-23). The policy is corrected here to describe what the review actually does, because a stated inclusion policy that the bibliography visibly contradicts is worse than a permissive one stated plainly; the original design intent is preserved in this note as history.

**Vendor product documentation** *(owner ruling 2026-11-03, written into this section 2026-11-23)*: a vendor's documentation is tiered by what it is cited for. It is Level B for what a feature does, because the vendor is the authority on its own product, and Level C, with the bias flagged, for any claim about how well the feature works, how fast it is or how it compares. The Level B example "Vendor technical documentation (if production-validated)" and the Level C criterion on product documentation not backed by production measurement are read under this ruling, and an entry citing vendor documentation says in its Evidence Level line which use it makes.

#### Evidence Level D (Rejected: 0%)
**Criteria**: Marketing materials, unverified claims, speculation
**Policy**: Excluded from literature review

### 3.2 Source Credibility Assessment

Each source undergoes multi-dimensional credibility evaluation:

**Quantitative Validation**:
- Specific metrics cited (e.g., "6 million requests/second" vs "significant improvement")
- Reproducible benchmarks with methodology disclosure
- Production scale indicators (data volumes, request rates, enterprise names)

**Author/Organization Authority**:
- Government agencies (CISA, MITRE, DARPA) = highest credibility
- Production deployments at scale (FAANG companies, Fortune 500) = high credibility
- Industry analysts with disclosed methodology (Gartner, IDC, Forrester) = moderate-high credibility
- Vendor claims validated by third parties = moderate credibility

**Temporal Relevance**:
- 2024-2025 sources prioritized for currency
- 2018-2023 sources accepted if still relevant (foundational technologies)
- Pre-2018 sources only for historical context (e.g., Brooks' "Mythical Man-Month")

**Metadata Completeness** (October-2025 self-assessment, not re-derived):
- 97% of entries include: Title, Author, Date, URL, Evidence Level, Hypothesis Links, Key Findings
- Missing metadata flagged for validation or downgrade

---

## 4. Data Extraction Process

### 4.1 Standardized Entry Format

Each source is documented with structured metadata:

```markdown
#### [Source Title]

**Authors**: [Names/Organization]
**Date**: [Publication/Access Date]
**URL**: [Link]
**Evidence Level**: [A/B/C/D]
**Relevance**:
- Hypothesis [ID] ([Brief description])
- Book Chapter [Number] ([Title])
- Best Practices Doc footnote [Reference]

**Key Findings**:
- [Bullet summary of quantitative claims]
- [Production deployment details]
- [Performance benchmarks]

**Citations**: [Where used in book/manuscript]
**Notes**: [Credibility assessment, validation status]
**Validation Status**: [✅ Active URL / ⚠️ Paywall / ❌ Dead link]
```

### 4.2 Extraction Categories

Sources organized into topical categories aligned with the October-2025 book structure (tallies from that catalogue, kept as record only; superseded by the per-entry source taxonomy in `methods/source-taxonomy.json`, and the sub-counts were never reconciled to the category totals):

1. **Foundational Architecture** (18 sources)
   - Table Formats (Iceberg, Delta, Hudi): 8 sources
   - Query Engines (Trino, Dremio, ClickHouse, DuckDB): 6 sources
   - Streaming Architectures (Kafka, Flink): 6 sources

2. **Security-Specific Data** (12 sources)
   - Data Volume & Characteristics: 4 sources
   - Cost Comparisons (SIEM vs Modern Stack): 5 sources
   - OCSF & Schema Standards: 3 sources

3. **Vendor Landscape** (15 sources)
   - Platform Capabilities: 8 sources
   - Performance Benchmarks: 7 sources

4. **Implementation & Organizational** (18 sources)
   - Change Management: 3 sources
   - Skills & Staffing: 6 sources
   - Deployment Patterns: 5 sources
   - TCO Analysis: 4 sources

5. **Emerging Technologies** (12 sources)
   - DuckDB Edge Processing: 2 sources
   - Table Format Interoperability (XTable): 2 sources
   - ML Infrastructure (Ray Serve, Feature Stores): 4 sources
   - Advanced Analytics: 4 sources

### 4.3 URL Validation Protocol

**Validation Process**:
1. **Automated Check**: HTTP status verification for all URLs
2. **Content Verification**: Manual review of 404s and redirects
3. **Wayback Machine**: Recovery of dead links where feasible
4. **Update Protocol**: Replace with current vendor documentation if original source unavailable

**Validation Results** (Phase 1, October 2025; the hypothesis-critical grade was later withdrawn, see §2.3):
- ✅ Active URLs: 16 of 22 (73%)
- ~~✅ Hypothesis-critical sources: 16 of 16 (100%)~~ (withdrawn)
- ⚠️ Paywalls (expected): 3 sources (Gartner, IDC, Forrester)
- ⚠️ Placeholders with corroborating evidence: 3 sources (non-critical)

**Current practice**: link checking runs through `scripts/link_check.py` (latest record `methods/link-check-2026-08-05.md`), and per-citation verification is logged in RESEARCH-JOURNAL.md.

---

## 5. Hypothesis-Driven Research Methodology

### 5.1 Hypothesis Formulation

The literature review validates quantitative hypotheses derived from:
1. **Book manuscript claims**: performance assertions, cost estimates, adoption rates
2. **Literature gap analysis**: patterns identified during extraction not previously formalized
3. **Isolation-first security pattern**: research questions RQ7-RQ10 (§5.4)
4. **Post-audit literature intake**: two hypotheses formulated 2026-07-10 from peer-reviewed primaries (H-LOGCOMP-01, H-SOC-BASELINE-01)

The wider hypothesis population these come from is tracked externally in the project's hypothesis tracker and is not counted here, because nothing in this repository enumerates it; the scored roster of this review is the set in PUBLICATION-MANUSCRIPT.md §3.7.

### 5.2 Hypothesis Validation Framework

> **Instrument note (2026-07-16)**: the five-level star scale below is the original October-2025 framework, retained for the historical record. The instrument of record is now the five-dimension, 25-point rubric in `methods/scoring-rubric.md` (anchor-only dimension values, a zero-scoreable-leg floor of 5/25, band thresholds at 21/16/11), applied to all nine hypotheses in `methods/RESCORE-2026-07-13.md`; current scores live in PUBLICATION-MANUSCRIPT.md §3.7. The worked examples below were also replaced 2026-07-16: the originals cited H-IMPL-01's 2.5-3× operational-cost legs and H-IMPL-03's 5.5-month average as live examples, but those legs were withdrawn in the 2026-06/07 audits (both hypotheses now sit at the instrument's 5/25 floor), so surviving hypotheses illustrate the bands instead.

Each hypothesis is classified using a 5-level confidence scale:

**STRONGLY VALIDATED (⭐⭐⭐⭐⭐)**:
- 5+ sources with quantitative evidence
- Multiple independent production deployments
- Government/standards body validation
- Example: **H-ARCH-01** (Iceberg Dominance) - 5 sources including Dremio survey, broad (not universal) vendor support, Apache governance; 23/25 Strongly Validated under the 2026-07-13 rescore

**STRONG (⭐⭐⭐⭐)**:
- 3-4 sources with quantitative evidence
- Industry analyst validation + production deployment
- Example: **H-LOGCOMP-01** (Machine-data-specialized compression) - three peer-reviewed compression anchors (LogLite PVLDB 18, PBC SIGMOD 2024, Pebbles IEEE TPDS 2021), all verbatim-verified at their primaries; 17/25 High Confidence under the 2026-07-13 rescore

**VALIDATED (⭐⭐⭐)**:
- 2-3 sources with quantitative evidence
- Production deployment or analyst consensus
- Example: **H-STREAM-01** (Kafka-based Stateful Streaming) - Samza at LinkedIn (Noghabi et al., VLDB 2017) plus Azure production scale, both primary-verified; 15/25 Moderate under the 2026-07-13 rescore, the demotion forced by the source-count anchor after the Uber withdrawal

**PRELIMINARY (⭐⭐)**:
- 1-2 sources, limited quantitative data
- Expert consensus without production validation
- Example: Requires additional evidence before publication

**UNVALIDATED (⭐)**:
- No supporting evidence found
- Flagged for revision or expert interview validation

### 5.3 Validated Hypotheses (Phase 1 Results)

> **Correction (2026-07-10, part-2 sweep; amended 2026-07-16 to add H3-PERFORMANCE-01)**: this table is the October-2025 Phase-1 record, preserved as-written — but several of its Key Evidence legs were later confirmed fabricated or unsupported and formally overturned: H-IMPL-01's IDC 2.5-3×, Confluent 45-55%, and Cloudera 39%/32% legs (hypothesis now scores 1/5), H-IMPL-02's DORA 2.7× and Ververica 3.2-FTE legs (now 2/5), H-IMPL-03's Gartner/phData 5.5-month leg, H-COST-09's Netflix 70-80% and AWS ~35% legs (replaced by the first-party S3 tier-price derivation; now 4/5), H-STREAM-01's LinkedIn "terabytes state" phrasing, and H3-PERFORMANCE-01's Shell 57TB/day leg (entry removed 2026-06-05, fabricated-class), its "96% <1s queries" figure (withdrawn 2026-07-11 — not in the cited Cloudflare article), and its "5-10× storage efficiency vs Elasticsearch" figure (corrected 2026-07-11, part-1 sweep: the benchmark's verified storage figure is 12-19×, the 5-12× multipliers on that page being query speed — see hypothesis-confidence-matrix.md's H3 section note). H3's surviving legs are Cloudflare's 6M req/sec and the first-party SDW lab CIDR probe, scoring 19/25 (High) under the 2026-07-13 rescore. (The x/5 values in this note are the 2026-07-10 interim scores; the 2026-07-13 rubric rescore supersedes them — H-IMPL-01/02/03 5/25, H-COST-09 9/25, H-STREAM-01 15/25, per PUBLICATION-MANUSCRIPT.md §3.7.) Do NOT cite this table's evidence column — current scores and verified legs live in LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md and MASTER-BIBLIOGRAPHY.md.

**7 Hypotheses Validated** with quantitative evidence *(Phase-1 claim — see correction above; the roster was extended to nine on 2026-07-10)*:

| Hypothesis | Status | Sources | Confidence | Key Evidence |
|------------|--------|---------|------------|--------------|
| **H-ARCH-01**: Apache Iceberg dominance as de facto standard | STRONGLY VALIDATED | 5 | ⭐⭐⭐⭐⭐ | Dremio survey (29% vs 23% Delta), broad vendor support (AWS, Google, Snowflake, Cloudera; Databricks in Public Preview since June 2025; Microsoft remains Delta-first with partial Fabric support — corrected 2026-07-10), 407 GitHub contributors *(2026-11-23: a floor under GitHub's 500-email limit; cite more than 400 contributors with linked accounts)* |
| **H-IMPL-01**: 2.5-3× operational costs for streaming vs batch | STRONG | 5 | ⭐⭐⭐⭐ | IDC (2.5-3× staffing), Confluent (45-55% TCO = ops), Cloudera (39% licensing, 32% hardware) |
| **H-IMPL-02**: 2.7× specialized staff for streaming architectures | STRONG | 4 | ⭐⭐⭐⭐⭐ | DORA (2.7× staff), Ververica (3.2 FTEs), McKinsey (tiger teams 35-40% acceleration) |
| **H-IMPL-03**: 5.5 month average for security data lakehouse | VALIDATED | 3 | ⭐⭐⭐ | Gartner/phData (5.5 months), Confluent (4-6 months), ~~security premium 15-30%~~ (SANS — withdrawn 2026-06-05, entry not present in cited sources) |
| **H-COST-09**: 55-80% cost savings with tiered storage | STRONG | 3 | ⭐⭐⭐⭐⭐ | Netflix (70-80%), AWS (35%), Kafka tiered storage |
| **H3-PERFORMANCE-01**: ClickHouse 6M req/sec, ~~96% <1s queries~~ (withdrawn 2026-07-11) | EXTENDED | 4 | ⭐⭐⭐⭐ | Cloudflare (6M/sec), ~~Shell (57TB/day)~~ (withdrawn 2026-06-05), ~~5-10×~~ 12-19× storage efficiency vs Elasticsearch (corrected 2026-07-11; vendor benchmark) — surviving legs: Cloudflare 6M req/sec + first-party SDW lab CIDR probe; 19/25 High under the 2026-07-13 rescore |
| **H-STREAM-01**: Kafka Streams for security analytics | VALIDATED | 3 | ⭐⭐⭐⭐ | LinkedIn (terabytes state), Uber (thousands of views), Confluent (sub-second latency) |

**Validation Quality Metrics**:
- Average sources per validated hypothesis: 4.1 *(October-2025 figure; the Sources column above averages 3.9)*
- ~~Quantitative evidence in all 9 hypotheses: 100% (7 original plus 2 added in the 2026-07-10 audit)~~ *(corrected 2026-07-16: false after the 2026-06/07 withdrawals. Under the 2026-07-13 rescore (PUBLICATION-MANUSCRIPT.md §3.7), five of the nine hold verified quantitative legs — H-ARCH-01 23/25, H3-PERFORMANCE-01 19/25, H-LOGCOMP-01 17/25, H-STREAM-01 15/25, H-SOC-BASELINE-01 13/25 — while H-COST-09 (9/25) holds only a first-party bound on the achievable saving and H-IMPL-01/02/03 (5/25 each) sit at the instrument's zero-scoreable-leg floor with no surviving quantitative support)*
- Production deployment validation: 6 of the 7 Phase-1 hypotheses (86%)
- Government/standards validation: 2 of the 7 Phase-1 hypotheses (29%)

### 5.4 Isolation-First Security Research Questions (November 2025)

Four new research questions (RQ7-RQ10) examine isolation-first security architecture patterns, where security data lives on dedicated infrastructure (isolated VPC/VNet) separate from corporate data platforms:

**RQ7: Isolation Patterns and Performance**
- **Question**: How do isolation patterns affect security data architecture performance?
- **Hypothesis**: Network isolation + IAM provides sufficient security boundary, eliminating need for fine-grained catalog access (RLS, column masking, metadata encryption) and achieving faster query performance (the 15-50% figure first stated here is an untested planning figure with no source; the one measurement is the first-party RLS entry in `isolation-first-security-tracking.md`, noted 2026-11-22)
- **Validation Metrics**: Query latency comparison, TCO comparison, operational hours
- **Data Sources**: Okta (Data Council 2024 public talk, scale only), Unity Catalog benchmarks, Iceberg metadata encryption overhead
- **Evidence Tier Target**: B

**RQ8: Compliance Trade-offs of Isolation-First Architecture**
- **Question**: Does isolation-first security meet SOC 2, ISO 27001, NIST CSF requirements without fine-grained catalog access?
- **Hypothesis**: Network isolation as primary security control meets compliance requirements for most enterprise security teams, with exceptions for multi-tenant MSSPs and federated global teams
- **Validation Metrics**: Compliance framework coverage, audit trail completeness, regulatory acceptance, gap analysis
- **Data Sources**: ~~Netflix compliance (SOC 2 with Polaris)~~ *(withdrawn 2026-11-23: the 2026-11-23 refresh found no Netflix deployment on the Polaris home, community or 1.9.0 access-control pages, and the Netflix logging post does not mention Polaris or compliance; see the Apache Polaris entry)*, Financial services SOC deployments, CISA zero-trust guidance, OCSF deployment case studies, ISO 27001/NIST CSF mappings
- **Evidence Tier Target**: B

**RQ9: Multi-Tenant MSSP vs Isolation-First Architecture Decision Thresholds**
- **Question**: What are the architectural decision thresholds for multi-tenant MSSP platforms vs single-tenant enterprise SOCs?
- **Hypothesis**: Multi-tenant MSSPs require row-level security (Unity Catalog), while single-tenant enterprise SOCs (500TB - 5PB scale) benefit from isolation-first architecture (Polaris/Nessie + table-level RBAC)
- **Validation Metrics**: Tenant isolation patterns, cost per tenant, operational complexity, scale thresholds
- **Data Sources**: MSSP case studies (Arctic Wolf, Expel, Red Canary), Enterprise SOCs (Netflix, Huntress, Okta), Unity Catalog multi-tenant patterns, AWS multi-tenant SaaS guidance, IT Harvest MSSP landscape
- **Evidence Tier Target**: B/C

**RQ10: Isolation Patterns Influence on Catalog Governance Decisions**
- **Question**: Does isolation-first security elevate Polaris and Nessie to top-tier catalog choices by changing selection criteria from "fine-grained access" to "vendor neutrality" and "version control"?
- **Hypothesis**: Isolated security platforms prioritize different catalog features: Unity Catalog wins for shared platforms (fine-grained access essential), Polaris (vendor neutrality) or Nessie (Git workflows) win for isolated platforms (table-level RBAC sufficient)
- **Validation Metrics**: Catalog adoption patterns, feature prioritization, migration patterns, decision criteria ranking
- **Data Sources**: ~~Netflix Polaris adoption rationale~~ *(withdrawn 2026-11-23, same reason as RQ8)*, Unity Catalog case studies, Nessie production deployments, Lisa Cao's published Gravitino work, Jake Thomas's Data Council 2024 talk, catalog feature comparison matrices (no interviews held with either)
- **Evidence Tier Target**: B

**Integration with Existing Research**:
- RQ7 extends H3-PERFORMANCE-01 (ClickHouse performance) with isolation pattern analysis
- RQ8 connects to compliance requirements from CISA, MITRE, NIST sources
- RQ9 addresses architectural decision framework from Chapter 4 (Implementation Journeys)
- RQ10 examines catalog selection criteria previously analyzed for shared platforms only

---

## 6. Synthesis and Analysis Methods

### 6.1 Evidence Synthesis

**Quantitative Synthesis**:
- **Performance Benchmarks**: Aggregated across multiple sources with methodology comparison
- **Cost Analysis**: TCO modeling using data from multiple sources (Cloudera, Confluent, AWS, Netflix; the IDC leg formerly listed here was withdrawn in the 2026-06 audit)
- **Adoption Rates**: Industry surveys (Dremio, Databricks, Confluent) with sample size and methodology disclosure

**Qualitative Synthesis**:
- **Implementation Patterns**: Cross-case analysis of production deployments (Netflix, Uber, LinkedIn, Cloudflare, SK Telecom; the Shell entry was removed in the 2026-06-05 audit — dead URL, unverifiable)
- **Expert Validation**: none held with Lisa Cao or Jake Thomas; their published work is used instead
- **Contradiction Analysis**: When sources conflict, document both perspectives with evidence quality assessment

### 6.2 Gap Analysis

**Literature Gaps Identified**:
1. **DuckDB Edge Processing** (H-EDGE-01): Limited production security deployments documented beyond Jake Thomas's public Data Council 2024 report
2. **Catalog Meta-Catalog Adoption** (H-ARCH-03): Emerging technology, adoption data sparse (pending Lisa Cao validation)
3. **OCSF Production Deployments**: Schema standard adoption unclear beyond vendor claims (expert interviews needed)

**New Hypotheses from Gap Analysis** (3 identified):
- Catalog unification patterns reducing operational complexity
- Edge processing viability for security analytics (DuckDB)
- Table format interoperability (XTable) adoption timelines

### 6.3 Temporal Analysis

The living-review cadence is the one the manuscript commits to in §2.7: monthly surveillance, quarterly incorporation, and an off-cycle update when a new Level-A source contradicts a scored hypothesis or moves it across a band boundary. The October-2025 plan for a month-by-month quarterly cycle built on an IT Harvest vendor-data partnership and per-quarter `YYYY-QX-update.md` files was not carried out in that form; versions are cut as tagged repository releases instead (§7.1).

---

## 7. Rigor and Reproducibility

### 7.1 Version Control for Citation Stability

**Problem**: Living literature reviews create citation instability (researchers cite moving targets)

**Solution**: Git-based version control with quarterly snapshots
- **CHANGELOG.md**: Documents all revisions with timestamps and rationale
- **Versioned Releases**: tagged repository releases, archived with a DOI once the first Zenodo release is minted, enable citation of a specific review version
- **Never Edit Published Versions**: Once published, create new version rather than edit existing

**Academic Citation Format**:
```
Wiley, J. (2026). Modern Data Architecture for Cybersecurity Operations: A Systematic
Literature Review (cite the commit hash, or a tag dated after 2026-11-17; the 2026-Q3-v1.0 tag of 2026-07-09 predates the database arm).
https://github.com/flying-coyote/security-data-literature-review (DOI to follow on the Zenodo release)
```

### 7.2 Transparency and Documentation

**Methodology Documentation**:
- LITERATURE-EXTRACTION-PLAN.md: Complete extraction process with timelines and decisions
- PROJECT-BRIEF.md: Separates canonical facts from assumptions requiring verification
- MASTER-BIBLIOGRAPHY.md: Standardized format with evidence levels and validation status

**Reproducibility**:
- All extraction from source documents (best practices doc, archive manuscripts)
- Link checking by `scripts/link_check.py`; every stated count derived by `scripts/count_reconcile.py`
- The expert-interview protocol is summarized in PUBLICATION-MANUSCRIPT.md Appendix C

### 7.3 Limitations and Biases

**Acknowledged Limitations**:

1. **Source Document Dependency**: the corpus began as an extraction of 283 footnotes from a single best-practices document, and that origin shaped it
   - *Mitigation*: Supplemented with expert validation, blog integration, vendor documentation, and — since 2026-07-13 — the systematic database search of §2.4, whose 26 surviving studies entered the corpus through a route the original curation did not control
   - *Residual*: measured recall of the curated corpus against that search was zero (0/40; see §2.4 and PUBLICATION-MANUSCRIPT.md §2.8)

2. **Vendor Documentation Prevalence**: vendor-authored material (69 vendor blogs and product docs, plus 14 big-tech engineering blogs) is 83 of 279 entries (29.7%; live per `methods/source-taxonomy.json`) — the largest single bloc *(the "33 of 75 (44%)" formerly stated here was the October-2025 figure at a 75-source corpus)*
   - *Mitigation*: Prioritize production-validated vendor sources (Netflix, Uber, Cloudflare), exclude marketing materials, flag bias per entry, never rest a hypothesis on a vendor source alone

3. **Recency Bias**: an October-2025 estimate put 70% of sources in 2023-2025 (not re-derived for the current corpus)
   - *Justification*: Modern data stack technologies evolved rapidly 2018-2025, recency ensures relevance

4. **English-Language Sources**: the synthesized corpus is in English, with one catalogued Portuguese short-course chapter from the database arm
   - *Impact*: May miss regional deployments (Asia-Pacific, Europe), though major vendors and standards bodies publish in English

5. **Publication Bias**: Production failures underreported in public case studies
   - *Mitigation*: the prepared interviews (manuscript Appendix C) are meant to capture implementation challenges absent from public documentation; until they are held, this mitigation is planned rather than applied

**Conflicts of Interest**: the review has no vendor funding. The author operates Security Data Works LLC, a consultancy whose commercial interests relate to the open, modular security-data architectures the review evaluates; the declaration of record is the Conflict of Interest statement in PUBLICATION-MANUSCRIPT.md, and the re-derivable rubric and tiers exist so a reader need not rely on the author's judgment.

---

## 8. Quality Metrics and Success Criteria

### 8.1 Phase 1 Quantitative Metrics (ACHIEVED ✅)

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Footnotes Extracted | 283/283 | 283/283 | ✅ 100% |
| Unique Sources Documented | 100+ | 279 catalogued (277 tiered; derived 2026-11-23) | ✅ Met |
| Evidence Level A | retired 2026-08-19 (see 8.1a) | 23.1% (64/277 tiered; live-derived 2026-11-23) | ✅ Measured, not targeted |
| URL Validation (Overall) | 80%+ | 73% (October 2025) | ⚠️ Near Target |
| URL Validation (Hypothesis-Critical) | 100% | ~~100%~~ withdrawn (see §2.3) | Superseded by per-citation verification |
| Hypotheses Assessed | 5+ | 9 (7 Phase-1, 2 added 2026-07-10) | ✅ |
| Metadata Completeness | 95%+ | 97% (October-2025 self-assessment) | ✅ |
| Book Chapters Cited | 7/7 (current seven-chapter book; the old 11/11 was the retired outline, remapped 2026-11-07 in `methods/chapter-remap-2026-11.md`) | 7/7 | ✅ 100% |

### 8.1a Why the Level-A share is no longer a target (owner ruling, 2026-08-19)

The >70% Level-A target is retired. It was set against the older Level-A criteria, which
counted production deployments and government publications as Level A; under the corrected
criteria in section 3.1 it was never reachable, because peer-reviewed research on security
data engineering barely exists. A corpus that is roughly two-thirds practitioner evidence is
not a deficient corpus, it is an accurate description of where the evidence in this field
actually lives.

The target also pointed the wrong way. The Level-A share falls as the corpus gets more
honest: the 2026-08-19 audit moved 57 entries down and the share went from 41.9% to 17.0%.
A metric that rewards the appearance of rigour over accurate labelling does not belong on a
public repository. The share is still derived and still reported; it is a description, not
a goal, and it should be read as "17.0% of this corpus is peer-reviewed or standards work",
which is a fact about the field rather than a grade.

These are the measures that replace it. Each rises as the corpus gets more accurate.

| Accuracy measure | Value (2026-08-19) | What it means |
|---|---|---|
| Tier accuracy | **229 of 229 (100%)** | every tiered entry checked against the section 3.1 definition — 96 audited downward from Level A, 190 audited upward from B/C |
| Claim–source integrity | **184 of 229 (80.3%)** | entries whose cited claim has been verified present in the cited source and marked ✅; 200 of 229 (87.3%) carry a validation record of some kind |
| Ineligible sources | **0** | personal communications as a cited source, the boundary breach found and removed 2026-08-12 |
| Outstanding fabrications | **0** | claims traced to a source that does not contain them, unresolved |

The tier-accuracy figure is worth one caveat so it is not over-read. It records that every
entry has been assessed against the definition, not that every assessment is correct. The
downward audit had one verdict overturned on adversarial review out of 61, and the upward
audit proposed two upgrades and upheld neither — so the error rate is low and measured
rather than assumed, which is the most that can honestly be claimed.

**Correction (2026-11-07).** The 229-of-229 row above is a dated 2026-08-19 measurement and
stays as recorded, but it was not fully right. Two Level-A entries that the downward audit
passed fail the section 3.1 definition: "Apache Arrow Flight SQL" (official project
documentation and a project blog post, which section 3.1 names as Level B) and "Mining
Temporal Attack Patterns from Cyberthreat Intelligence Reports" (an arXiv preprint tiered A
with no author list and no venue). Both were re-tiered A → B on 2026-11-07 with a dated note
in each entry. Read against the 229 entries the audit covered, that is 227 of 229 correct
(99.1%), which is a measured error rate for the audit itself; the live tier counts are derived
by `scripts/count_reconcile.py` and the denominator has since moved on as entries were added.

### 8.2 Phase 2 Metrics (planned October 2025; the IT Harvest partnership they assumed is still pending)

**Planned Metrics**:
- Quarterly updates published: 4 per year (Jan, Apr, Jul, Oct)
- Vendor landscape sources: 50+ additional sources
- Expert validation cycles: 2 per quarter
- Citation stability maintained: 100% versioned snapshots

### 8.3 Academic Publication Readiness

**Suitability Assessment**:
- ✅ PRISMA-aligned methodology documented
- Reported, not targeted: evidence quality stated as a measured Level-A share rather than against a target (23.1% derived 2026-11-23; §8.1a; the "79% exceeds standards" self-grade was withdrawn in the 2026-06 audit)
- ✅ Quantitative hypothesis validation with multiple sources
- ✅ Reproducible extraction process
- ✅ Version control for citation stability
- ✅ Limitations and biases acknowledged
- ⏳ Pending: First quarterly update (demonstrates living review process)

**Target Venues** *(superseded 2026-07-10 by owner ruling: the submission target is the Journal of Cybersecurity (Oxford University Press); the list below is preserved as the October-2025 assessment)*:
- **ACM Computing Surveys** (CSUR): Systematic literature reviews, high-impact
- **IEEE Security & Privacy**: Security practitioner audience
- **Conferences**: Industry security conferences (RSAC, Black Hat, BSides) for rapid dissemination

---

## 9. Integration with Book and Blog

### 9.1 Book Manuscript Integration

**Purpose**: Literature review provides evidence foundation for "Modern Data Stack for Cybersecurity". *(The integration points below are the October-2025 plan against the retired eleven-chapter outline; the current seven-chapter mapping is `methods/chapter-remap-2026-11.md` and the per-chapter claim-evidence matrix is `methods/claim-evidence-matrix-2026-11.md`.)*

**Integration Points**:
- **Chapter 1 (Cost Comparisons)**: 12 sources validating SIEM alternatives economics
- **Chapter 4 (Implementation Journeys)**: 15 sources quantifying timelines, staffing, TCO
- **Chapter 7 (Streaming/Ingestion)**: 10 sources on Kafka, Flink, operational patterns
- **Chapter 8 (Storage Formats)**: 8 sources on Iceberg, Delta, Hudi adoption
- **Chapter 9 (Query Engines)**: 6 sources on Trino, Dremio, ClickHouse, DuckDB
- **Advanced Analytics**: 10 sources on ML infrastructure, training data, deployment patterns

**Citation Format**: All book claims cite MASTER-BIBLIOGRAPHY.md with footnote numbers and evidence levels.

### 9.2 Blog Integration (Feedback Loop)

**Security Data Commons Blog** (October-2025 channel, since retired; the feedback loop below describes how it worked):
- **Blog → Literature Review**: Blog posts identify new sources requiring literature review integration
- **Literature Review → Blog**: Evidence-based writing with authoritative citations

**Example Workflow**:
1. Blog post on "ClickHouse vs Elasticsearch for Security Logs" cites literature review sources
2. Reader comments identify new production deployments (e.g., Cloudflare case study)
3. New source validated and added to MASTER-BIBLIOGRAPHY.md
4. Next quarterly update includes expanded ClickHouse evidence

---

## 10. Conclusion

This systematic literature review employs a PRISMA 2020 two-arm methodology to consolidate 277 tiered sources (derived 2026-11-23) on modern data stack technologies for cybersecurity. The approach prioritizes:

1. **Evidence Quality**: Level-A share live-derived per entry (23.1% at 2026-11-23, 17.0% immediately after the 2026-08-19 audit; the share is reported, not targeted — see 8.1a — the earlier 79% self-grade was withdrawn in the 2026-06 audit, and the 2026-08-19 audit re-tiered 57 entries that were not peer-reviewed research or official standards)
2. **Quantitative Validation**: 9 hypotheses assessed (7 original plus 2 added in the 2026-07-10 audit) — under the 2026-07-13 rubric rescore: 1 strongly validated, 2 high confidence, 2 moderate, and 4 preliminary whose quantitative legs were withdrawn in the 2026-06/07 audits (see PUBLICATION-MANUSCRIPT.md §3.7)
3. **Citation Stability**: Version control with quarterly snapshots enabling stable academic references
4. **Reproducibility**: Documented extraction process, standardized formats, transparent limitations

**Phase 1 Success**: Extraction complete with all book chapters cited, 9 hypotheses assessed (7 original plus 2 added in the 2026-07-10 audit); publication readiness is assessed in §8.3.

**Ongoing cadence**: monthly surveillance, quarterly incorporation, and tagged repository releases (first: 2026-Q3-v1.0), as set out in §6.3.

**Methodological Contribution**: Demonstrates living literature review infrastructure for rapidly-evolving technology domains requiring both academic rigor and practitioner currency.

---

**Maintained by**: Jeremy Wiley
**Project Repository**: https://github.com/flying-coyote/security-data-literature-review
**Last Updated**: November 17, 2026 (counts re-derived, tier definitions aligned with the 2026-08-19 audit, appraisal given its own section, stale October-2025 claims labelled)
**Version**: 1.3 (1.2 was the 2026-07-16 reconciliation pass; 1.1 added RQ7-RQ10, November 14, 2025)
**Next Review**: 2027-Q1 (quarterly cadence)
