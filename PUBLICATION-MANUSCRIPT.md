---
type: essay-draft
title: "Modern Data Architecture for Cybersecurity Operations: Systematic Literature Review Manuscript Draft"
created: 2025-10-21
tags: [manuscript, academic-publication, systematic-review, security-data-lakehouse, draft]
---

# Modern Data Architecture for Cybersecurity Operations: A Systematic Literature Review

**Authors**: Jeremy Wiley [Additional co-authors TBD based on expert validation contributions]

**Keywords**: Data lakehouse, security analytics, OLAP, streaming architectures, cybersecurity data engineering, systematic review

**Manuscript Status**: DRAFT v0.3 (In Progress)
**Created**: October 21, 2025
**Last Updated**: July 10, 2026

---

## ABSTRACT

Security teams collect enormous volumes of log and event data, and the systems that store and search it are among the most expensive infrastructure they run. Data platforms that grew out of web-scale analytics (Apache Iceberg, ClickHouse, Kafka Streams) promise to cut those costs, but the evidence on whether they hold up under security workloads is split across two literatures that rarely meet, because cybersecurity research treats data infrastructure as a given while data engineering studies general analytics rather than security operations. We conducted a PRISMA 2020 two-arm review bridging the two, synthesizing 219 tiered sources spanning production deployments, peer-reviewed research, and government standards, and we maintain it as a living review with quarterly updates because these sources shift too fast for a one-time survey. A retrospective systematic search of OpenAlex and dblp, run against the already-curated corpus, found that none of the 40 studies it included was already cited — a measured recall of zero, which we report rather than repair silently; the 26 that survived a critical appraisal of venue integrity are incorporated here, and the 14 that did not are recorded with their reasons, eight of them having been published in predatory or compromised venues. The architectures work but demand more time and scarcer expertise than vendor accounts suggest: start with batch on SQL-friendly platforms, add streaming after validating business impact, tier storage for multi-year retention, and plan multi-month implementations plus a 6-12 month proficiency ramp (a practitioner estimate).

Nine hypotheses were assessed, seven from the original extraction and two added in July 2026 from post-audit peer-reviewed primaries, each graded on the review's A-D evidence tiers. Apache Iceberg emerged as industry consensus for open table formats with universal vendor support, and ClickHouse validated for security analytics at scale (Cloudflare: 6M requests/sec; a first-party CIDR probe measured roughly 13-17× native-IP speedup at 20M rows on a single host, with about 2.9× IPv4-versus-String storage savings). Streaming architectures carry a material operational cost and staffing premium over batch alternatives, since the required fault-tolerance expertise remains scarce. The two hypotheses added post-audit carry clean peer-reviewed legs, one measuring production-SOC alert base rates of 24K-134K per day with a true-attack share on the order of 0.01% in the studied SOCs, the other measuring machine-data-specialized compression at multiples over general-purpose equivalents. Production validation across 18+ organizations confirms requirements general analytics does not exercise, among them IP/CIDR-based threat hunting, incident-driven burst capacity, stateful entity tracking, and multi-year queryable retention. The 2026 source audits withdrew the citations behind several originally stated multipliers, so those findings now read directionally pending re-sourcing.

---

## 1. INTRODUCTION

### 1.1 The Security Data Challenge

Modern cybersecurity operations generate unprecedented volumes of telemetry data. Large platform operators process millions of security-relevant events per second, and incident response drives sharp, unpredictable traffic surges. Traditional Security Information and Event Management (SIEM) architectures, designed for earlier threat landscapes, increasingly struggle with these data volumes, facing both scalability limits and prohibitive costs.

The modern data stack—comprising data lakehouses, distributed query engines, and streaming architectures—emerged from web-scale companies solving big data challenges in general analytics contexts (e.g., Netflix, Uber, LinkedIn). These architectural patterns promise solutions to security operations' data challenges: cost-efficient storage through table formats like Apache Iceberg, high-performance analytics via engines like ClickHouse, and real-time processing capabilities through Kafka Streams. Organizations are increasingly adopting these patterns for security operations, with production deployments at Cloudflare (6 million requests/second) and Microsoft (trillions of events daily).

However, security practitioners face a critical knowledge gap: **How do these general-purpose data architectures perform in security-specific contexts, and what are the quantified operational costs of implementation?** Vendor marketing claims abound, but systematic evidence-based guidance on architecture selection, total cost of ownership (TCO), staffing requirements, and performance benchmarks for security workloads remains scarce. A CISO evaluating ClickHouse versus traditional SIEM for a Security Operations Center (SOC) lacks peer-reviewed benchmarks, validated cost models, or industry consensus on best practices.

This evidence gap has tangible consequences. Organizations underestimate implementation timelines (industry implementations run materially longer than the commonly assumed 2-3 months), underestimate staffing requirements (streaming architectures require materially more operational staff than batch alternatives), and lack quantitative frameworks for evaluating cost-performance trade-offs (tiered storage reduces retention costs, but under what conditions?). The absence of systematic synthesis across cybersecurity and data engineering literatures leaves practitioners navigating vendor claims without rigorous validation.

### 1.2 Literature Gap: Two Disconnected Domains

Our analysis reveals two robust but disconnected literature streams:

**Cybersecurity literature** addresses threat detection algorithms, incident response procedures, compliance frameworks, and adversarial tactics. Publications from organizations like MITRE, CISA, SANS, and NSA provide authoritative guidance on security operations. However, this literature treats data infrastructure as a black box, rarely engaging with data engineering fundamentals: storage format optimizations, query engine selection criteria, streaming versus batch trade-offs, or data lakehouse architectural patterns. Cost and staffing guidance, when present, focuses on security analyst headcount rather than data engineering operations.

**Data engineering literature** provides rigorous treatment of distributed systems, query optimization, storage formats (Iceberg, Delta Lake, Hudi), streaming architectures (Kafka, Flink), and OLAP engines (ClickHouse, Druid, Pinot). Leading industry sources (Netflix, Uber, LinkedIn) publish production deployment details with quantitative benchmarks. However, these publications address general analytics workloads—business intelligence, machine learning, customer analytics—not security-specific requirements. Security operations' unique characteristics (high-velocity ingestion, extended retention periods, compliance audit trails, incident-driven query patterns, threat hunting workflows) receive minimal attention.

This disconnect creates a critical gap: **No systematic review synthesizes evidence across both domains to provide security practitioners with validated architectural guidance.** Existing surveys in computer science (e.g., ACM Computing Surveys publications) cover distributed systems or security independently but not their intersection. Security conferences (Black Hat, RSA) feature vendor presentations on modern data stacks but lack peer-reviewed validation. Data engineering conferences (Strata, DataEngineering.io) rarely address security operations as a distinct workload type.

The gap has three dimensions:

1. **Architectural patterns**: Which table formats, query engines, and streaming architectures are validated for security workloads versus general analytics?

2. **Operational costs**: What are quantified TCO, staffing multipliers, and implementation timelines for security data platforms versus vendor claims?

3. **Performance benchmarks**: How do OLAP engines, streaming processors, and data lakehouses perform on security-specific workloads (threat hunting, SIEM replacement, compliance reporting) at TB-PB scale?

### 1.3 Research Questions

This systematic review addresses the following research questions:

**RQ1: What architectural patterns are validated in production security data platforms?**
- Which table formats (Iceberg, Delta Lake, Hudi) demonstrate adoption in security contexts?
- Which query engines (ClickHouse, Trino, Dremio, Spark) are deployed for security analytics?
- What streaming versus batch architecture patterns exist for security telemetry ingestion?
- What is the evidence level for each pattern (vendor claims vs. production deployments vs. peer-reviewed research)?

**RQ2: What are the quantified operational costs of security data architectures?**
- What is the total cost of ownership (TCO) for streaming versus batch architectures in security contexts?
- What staffing multipliers apply for different architectural choices (e.g., Kafka Streams vs. batch processing)?
- What are validated implementation timelines for security lakehouse projects?
- How do tiered storage strategies impact costs, and under what conditions?

**RQ3: What performance benchmarks exist for security-specific workloads?**
- What query performance (latency, throughput) is validated for security analytics at TB-PB scale?
- What ingestion rates are achievable for streaming security telemetry (events per second)?
- What storage efficiency gains (compression ratios, cost per TB) are validated?
- How do security workloads differ from general analytics in performance characteristics?

**RQ4: What implementation patterns are validated for security operations?**
- What change management strategies are documented for transitioning from SIEM to modern data stack?
- What skills gaps exist, and what staffing models address them?
- What deployment patterns (cloud, on-premises, hybrid) are validated for security compliance requirements?
- What operational reliability patterns (SLAs, incident response) are documented?

### 1.4 Contribution

This systematic review makes the following contributions to knowledge and practice:

**1. Cross-domain synthesis**: This review bridges the cybersecurity and data-engineering literatures under a PRISMA 2020 two-arm methodology. We synthesize 219 tiered sources from government agencies (CISA, MITRE, DARPA, NSA, SANS), industry analysts (Gartner, Forrester), production deployments (Netflix, Uber, LinkedIn, Cloudflare, SK Telecom, and — via the search arm — CERN, INFN-CNAF and Lawrence Berkeley National Laboratory), peer-reviewed research, and vendor technical documentation. Our evidence classification prioritizes production deployments and peer-reviewed research, and every count on every surface of this review is derived from the bibliography by a committed script rather than hand-maintained, so that a stated number cannot drift from the corpus it describes.

**2. Quantitative hypothesis validation**: We provide evidence-based validation of 9 operational hypotheses (7 original plus 2 added in the 2026-07 audit) critical for security practitioners:
- Apache Iceberg dominance (industry consensus, universal vendor support)
- Streaming architecture operational cost premium vs. batch
- Staffing multipliers for streaming vs. batch
- Implementation timelines longer than vendor claims
- Tiered storage savings for multi-year retention
- ClickHouse OLAP performance (6M requests/second at Cloudflare)
- Kafka Streams security patterns (production validation)

Each hypothesis receives transparent confidence scoring using a multi-dimensional rubric (source count, evidence quality, source diversity, quantitative precision, geographic/organizational diversity).

**3. Production evidence base**: We document 18+ production deployments with quantitative metrics, moving beyond vendor marketing claims to validated performance data. Examples include Cloudflare's 6 million requests/second with ClickHouse, SK Telecom's production Iceberg deployment with Trino.

**4. Practitioner-oriented guidance**: We translate research findings into actionable operational guidance:
- Architecture selection frameworks with quantified trade-offs
- Staffing models by architecture type
- Budget planning templates accounting for streaming cost premiums and tiered storage savings
- Timeline expectations calibrated to industry experience versus optimistic assumptions (2-3 months)
- Skills assessment frameworks identifying scarce fault-tolerance expertise requirements

**5. Gap identification for future research**: We systematically identify 6 evidence gaps requiring further investigation, including mid-market data volume validation, direct SIEM cost comparisons, emerging technology patterns (DuckDB edge processing, XTable interoperability), catalog adoption metrics, and security-specific benchmark suites.

**Target audience**: This review serves three communities:
- **Security practitioners** (security architects, SOC managers, CISOs) seeking evidence-based architecture selection guidance
- **Data engineers** in security contexts needing security-specific requirements and performance benchmarks
- **Researchers** in cybersecurity and data systems exploring the intersection of both domains

By providing the first systematic synthesis of this fragmented literature, we enable security organizations to make evidence-based infrastructure decisions, moving from vendor marketing claims to production-validated patterns with quantified operational costs.

---

## 2. METHODOLOGY

### 2.1 Systematic Review Approach

This review follows PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines [16] adapted for systematic literature reviews in computer science. Unlike traditional static literature reviews, this employs a living review methodology with version control to support quarterly updates while maintaining citation stability for academic references.

**Review Protocol**:
- **Planning period**: September 2024 - October 2025
- **Execution period**: October 2025 (4 weeks, completed ahead of schedule)
- **Source materials**: Book manuscript footnotes (283 citations), expert network validation, ongoing research (2024-2025)
- **Living review structure**: Quarterly updates (Jan, Apr, Jul, Oct) with versioned snapshots (YYYY-QX-update.md)

**Research Objectives**:
1. **Primary**: Synthesize evidence on modern data stack technologies (table formats, query engines, streaming architectures) applied to security analytics
2. **Secondary**: Validate quantitative hypotheses regarding adoption rates, implementation costs, performance characteristics, and organizational requirements
3. **Tertiary**: Establish living literature review infrastructure supporting quarterly updates for technology currency

**Scope Boundaries**:
- **In Scope**: Modern data stack technologies (2018-2025), security-specific applications (SIEM alternatives, security data lakes), implementation evidence (TCO, staffing, timelines), production deployments
- **Out of Scope**: Traditional SIEM implementations (pre-2018), general data engineering without security focus, operational tooling implementations, vendor marketing materials

### 2.2 Literature Search Strategy

**Primary Source Documents**:

The systematic extraction identified two primary source categories:

1. **Best Practices Document** (2024-04-15): Comprehensive manuscript with 283 footnotes spanning foundational architecture, security implementations, cost analysis, and emerging technologies
2. **Archive Manuscripts** (74 files): Draft chapters across 5 parts (Crisis, Framework, Components, Implementation, Future) referencing centralized best practices footnotes

Archive manuscripts were evaluated and found to reference footnotes centralized in the best practices document with no independent citations beyond the 283 footnotes, establishing the best practices document as the primary extraction target.

**Supplementary Source Identification**:

Beyond primary extraction, sources were supplemented through:

1. **Expert Network Validation**: Practitioner interviews (Lisa Cao - Datastrato/Apache Gravitino, Jake Thomas - Okta, a data-platform practitioner, Paul Agbabian) providing production deployment validation
2. **Blog Integration**: Ongoing source identification through security-data-commons blog (3×/week cadence)
3. **Vendor Documentation**: Official technical documentation from Apache Software Foundation, AWS, Microsoft, Google, Confluent, Databricks
4. **Government Standards**: CISA, MITRE, DARPA, NSA, SANS Institute publications
5. **Industry Analysts**: Gartner, IDC, Forrester research reports with peer-reviewed quality assessment

**Search Execution**:

Phase 1 (October 14-25, 2025) employed systematic extraction of 283 footnotes using automated URL extraction from markdown footnotes, manual review of vendor documentation references, performance benchmark identification, and expert quote attribution verification.

**Extraction Coverage**:
- 283 of 283 footnotes extracted (100% completion)
- 221 sources catalogued with a standardized format, of which 219 carry an evidence tier
- 16 of 22 URLs validated (73% overall, 100% hypothesis-critical sources)
- Archive manuscripts: 74 files assessed (no independent sources found)

**Database Search (added 2026-07-13, run retrospectively)**:

Everything described above is curation, which PRISMA 2020 accommodates as the "identification via other methods" arm but which cannot, on its own, answer the question a reviewer will ask: what does the indexed literature hold, and did this review find it? To answer it we ran a genuine systematic search after the fact and reported the result whatever it turned out to be.

The search queried OpenAlex with a strict boolean title-and-abstract filter (a security term AND a data-architecture term, 2018 date floor) and dblp with eight title-level queries, on 2026-07-13. It identified 400 records, removed 5 duplicates, screened 395 on title and abstract against pre-specified criteria, and included 40. The full protocol, the per-record screening decisions, and the search logs are committed under `methods/`.

The reconciliation against the existing corpus produced the finding that matters most in this section: **none of the 40 was already cited.** Measured recall of the curated corpus against a systematic search of its own subject was zero. The corpus and the indexed literature had been reaching disjoint bodies of work — which is, in a sense, the review's own thesis turned back on itself, and is reported here rather than quietly corrected.

The 40 were then critically appraised, a stage the topical screening had skipped: venue identity resolved at the DOI, publisher and DOAJ/Scopus/Web-of-Science status established from primaries, predatory-list and delisting checks run, and each proposed citation put to an independent second reviewer instructed to refuse it under uncertainty. **Fourteen did not survive.** Eight were published in predatory or compromised venues — one in a journal documented as hijacked, one in a title Clarivate delisted in its March-2023 cull of Hindawi journals after the publisher admitted paper-mill compromise. Three were not peer-reviewed at all, including a preprint typeset with a counterfeit publisher masthead and a placeholder DOI. One could not be read at any price and was dropped rather than cited unread. The remaining 26 are incorporated into this edition, and the appraisal record for all 40 — every drop and its reason — is `methods/prisma-appraisal-2026-07-13.json`.

### 2.3 Source Selection and Quality Assessment

**Inclusion Criteria**:
1. **Relevance**: Addresses data architecture for security operations, analytics at scale, or production deployments
2. **Evidence quality**: Production deployments, peer-reviewed research, industry analyst reports, or government/standards publications
3. **Recency**: Published 2020-2025 (exceptions for foundational work like Brooks' "Mythical Man-Month")
4. **Accessibility**: Publicly available or obtainable through standard academic channels

**Exclusion Criteria**:
1. Marketing materials without technical depth or quantitative validation
2. Unverified claims or speculation without production evidence
3. Sources superseded by more recent publications
4. Duplicate coverage of same deployment/study

**Evidence Level Classification**:

Sources classified using a four-tier evidence system prioritizing production deployments and peer-reviewed research (adapted from evidence-based medicine):

**Evidence Level A** (target >70%; live 42.9%, 94 of 219 tiered):
- Production case studies (Netflix, Uber, LinkedIn, Cloudflare, SK Telecom) with quantitative benchmarks
- Peer-reviewed academic publications in venues whose peer review has been verified to exist
- Government/standards body publications (CISA, MITRE, DARPA, NSA, SANS, Apache Software Foundation)

**Evidence Level B** (live 46.6%, 102 of 219 tiered):
- Gartner, IDC, Forrester quantitative research with disclosed methodology
- Expert practitioner validation (personal communication with production deployment details)
- Vendor technical documentation (if production-validated); peer-reviewed conference work whose review depth could not be independently established

**Evidence Level C** (live 10.5%, 23 of 219 tiered):
- Vendor blog posts, product documentation, and conference talks not backed by production measurement
- Policy, stated as practised rather than as originally intended: Level C sources **are** catalogued, with their bias flagged and their tier stated, where they are the only available account of a system's behaviour. They never carry a hypothesis on their own. The original protocol declared Level C "rejected, 0%", and the corpus has never matched that claim — 23 of 219 tiered entries are Level C. The protocol is corrected here to describe what the review actually does, because a stated inclusion policy that the bibliography visibly contradicts is worse than a permissive one stated plainly.

**Evidence Level D** (0%):
- Marketing materials, unverified claims, speculation
- Policy: excluded. No Level D source is catalogued, and this one the corpus does honour.

**A note on what "peer-reviewed" is taken to mean.** The 2026-07-13 systematic search made this concrete rather than nominal. Of the 40 studies it topically included, eight were published in venues that are predatory, hijacked, or delisted for paper-mill compromise — venues where the peer review that Level A rests on did not meaningfully happen. A paper in such a venue cannot be Level A however relevant its claims, and this review drops it rather than laundering a weak claim through a citation that merely looks authoritative. Venue integrity is therefore part of the tier assignment, not a separate courtesy.

**Multi-Dimensional Credibility Assessment**:

Each source underwent evaluation across multiple dimensions:

*Quantitative Validation*: Specific metrics cited (e.g., "6 million requests/second" vs "significant improvement"), reproducible benchmarks with methodology disclosure, production scale indicators (data volumes, request rates, enterprise names)

*Author/Organization Authority*: Government agencies (CISA, MITRE, DARPA) = highest credibility; production deployments at scale (FAANG companies, Fortune 500) = high credibility; industry analysts with disclosed methodology (Gartner, IDC, Forrester) = moderate-high credibility; vendor claims validated by third parties = moderate credibility

*Temporal Relevance*: 2024-2025 sources prioritized for currency; 2018-2023 sources accepted if still relevant (foundational technologies); pre-2018 sources only for historical context

*Metadata Completeness*: 97% of entries include Title, Author, Date, URL, Evidence Level, Hypothesis Links, Key Findings; missing metadata flagged for validation or downgrade

### 2.4 Data Extraction Process

**Standardized Entry Format**:

Each source documented with structured metadata:
- Title, Authors/Organization, Publication Date, URL
- Evidence Level classification (A/B/C/D)
- Relevance tags (hypothesis IDs, book chapters, footnote references)
- Key Findings (quantitative claims, production deployment details, performance benchmarks)
- Citations (where used in book/manuscript)
- Validation Status (✅ Active URL / ⚠️ Paywall / ❌ Dead link with corroboration)

**Extraction Categories**:

Sources organized into topical categories aligned with book structure:

1. **Foundational Architecture** (18 sources): Table Formats (Iceberg, Delta, Hudi) - 8 sources; Query Engines (Trino, Dremio, ClickHouse, DuckDB) - 6 sources; Streaming Architectures (Kafka, Flink) - 6 sources

2. **Security-Specific Data** (12 sources): Data Volume & Characteristics - 4 sources; Cost Comparisons (SIEM vs Modern Stack) - 5 sources; OCSF & Schema Standards - 3 sources

3. **Vendor Landscape** (15 sources): Platform Capabilities - 8 sources; Performance Benchmarks - 7 sources

4. **Implementation & Organizational** (18 sources): Change Management - 3 sources; Skills & Staffing - 6 sources; Deployment Patterns - 5 sources; TCO Analysis - 4 sources

5. **Emerging Technologies** (12 sources): DuckDB Edge Processing - 2 sources; Table Format Interoperability (XTable) - 2 sources; ML Infrastructure - 4 sources; Advanced Analytics - 4 sources

**URL Validation Protocol**:

Validation Process: (1) Automated HTTP status verification for all URLs, (2) Content verification with manual review of 404s and redirects, (3) Wayback Machine recovery of dead links where feasible, (4) Update protocol replacing with current vendor documentation if original unavailable

Validation Results (Phase 1):
- ✅ Active URLs: 16 of 22 (73%)
- ✅ Hypothesis-critical sources: 16 of 16 (100%)
- ⚠️ Paywalls (expected): 3 sources (Gartner, IDC, Forrester)
- ⚠️ Placeholders with corroborating evidence: 3 sources (non-critical)

Validation Priority: All hypothesis-validating sources verified before publication. Non-critical placeholders acceptable if supported by related evidence.

**Extraction Phases**:

*Phase 1: Source Document Inventory* (Week 1) - Identified 283 footnotes in best practices document; assessed 74 archived manuscript files

*Phase 2: Systematic Extraction* (Week 1-2) - Extracted all 283 footnotes with standardized format; consolidated duplicates; Result: the initial catalogue of unique sources, which has since grown by curation and by the 2026-07-13 database search to 221 entries

*Phase 3: Validation & Quality Assurance* (Week 2-3) - URL validation, evidence level verification, cross-reference validation, expert network review

*Phase 4: Hypothesis Validation* (Week 3-4) - Identified 9 hypotheses requiring quantitative validation (7 in this phase; 2 further hypotheses were added in the 2026-07-10 audit, for 9 in total); mapped sources to hypotheses; calculated confidence scores

### 2.5 Hypothesis-Driven Research Framework

**Hypothesis Formulation**:

The literature review validates quantitative hypotheses derived from:
1. **Book manuscript claims** (29 hypotheses): Performance assertions, cost estimates, adoption rates
2. **Literature gap analysis** (3 hypotheses): Patterns identified during extraction not previously formalized
3. **Post-audit literature intake** (2 hypotheses): formulated 2026-07-10 from peer-reviewed primaries catalogued by the post-audit evidence hunt (Gemini DR-3 intake; wording adjudicated in NEW-HYPOTHESES-PROPOSAL-2026-07.md)

The scored roster reported in this manuscript is the 9 hypotheses assessed here; the wider hypothesis population from which they are drawn is tracked externally in the project's hypothesis tracker, not counted in this review.

**Hypothesis Validation Framework**:

Each hypothesis is scored on a five-dimension rubric — source count, evidence quality, source diversity, quantitative precision, and geographic/organizational diversity — each dimension worth up to 5 points, for a total between 5 and 25. The instrument of record is `methods/scoring-rubric.md`, which documents the anchor values for every dimension, the rules that decide edge cases (what counts as a scoreable leg, how first-party measurements are treated, how a shared author collaboration counts once), and a worked example, so a reviewer holding that file and MASTER-BIBLIOGRAPHY.md can re-derive every score below. Totals map to bands:

| Total | Band label | Stars |
|---|---|---|
| 21–25 | Strongly Validated | ⭐⭐⭐⭐⭐ |
| 16–20 | High Confidence | ⭐⭐⭐⭐ |
| 11–15 | Moderate | ⭐⭐⭐ |
| 5–10 | Preliminary | ⭐⭐ |

A hypothesis whose quantitative legs were all withdrawn sits at the instrument's 5/25 floor inside the Preliminary band, carried with a withdrawn-legs note.

**Phase 1 Validation Results**:

*[2026-06 source audit note: citations supporting the original staffing, TCO, timeline, and tiered-storage multipliers were withdrawn (fabricated entries or stats not present in the cited sources). A 2026-07 per-citation verification pass additionally withdrew the DORA-attributed "Level 4 / top 5%" skill taxonomy and the Forrester TEI TCO breakdown and re-attributed the LinkedIn stateful-processing figures to Samza (VLDB 2017). The affected multipliers are removed throughout this manuscript, and those hypotheses revert to directional claims pending re-sourcing. The confidence scores below are post-audit values, recomputed 2026-07-13 under the explicit rubric (`methods/RESCORE-2026-07-13.md`), not pre-audit figures.]*

9 Hypotheses assessed (7 original; 2 added post-audit 2026-07-10, provenance noted per row); scores recomputed 2026-07-13 under `methods/scoring-rubric.md`, superseding the 2026-07-09 adopted values where they differ:

- **H-ARCH-01** (Iceberg Dominance): STRONGLY VALIDATED, 23/25 ⭐⭐⭐⭐⭐ - Dremio survey (29% vs 23% Delta), broad vendor support, 407 GitHub contributors (2026-07-09)
- **H3-PERFORMANCE-01** (ClickHouse): HIGH CONFIDENCE, 19/25 ⭐⭐⭐⭐ - Cloudflare production, verbatim-verified
- **H-LOGCOMP-01** (Machine-data-specialized compression; added post-audit 2026-07-10): HIGH CONFIDENCE, 17/25 ⭐⭐⭐⭐ - LogLite PVLDB 18 + PBC SIGMOD '24 + Pebbles IEEE TPDS '21, all verbatim-verified at primary
- **H-STREAM-01** (Stateful Streaming): MODERATE, 15/25 ⭐⭐⭐ - Samza VLDB 2017 (peer-reviewed) + Azure production; two legs cap the source count
- **H-SOC-BASELINE-01** (Production SOC alert base rates; added post-audit 2026-07-10): MODERATE, 13/25 ⭐⭐⭐ - Yang et al. USENIX Security 2024, verbatim-verified; single-source caps the score
- **H-COST-09** (Tiered Storage savings): PRELIMINARY, 9/25 ⭐⭐ - savings band withdrawn 2026-06; first-party S3 tier-delta derivation bounds the saving; directional
- **H-IMPL-01** (Streaming TCO premium): PRELIMINARY, 5/25 ⭐⭐ - DORA + TEI legs withdrawn; no scoreable leg, instrument floor; directional
- **H-IMPL-02** (Staffing premium): PRELIMINARY, 5/25 ⭐⭐ - DORA attribution withdrawn as fabricated; no scoreable leg, instrument floor; directional
- **H-IMPL-03** (Timeline premium): PRELIMINARY, 5/25 ⭐⭐ - timeline figures withdrawn 2026-06/07; no scoreable leg, instrument floor; directional

### 2.6 Synthesis and Analysis Methods

**Quantitative Synthesis**:
- **Performance Benchmarks**: Aggregated across multiple sources with methodology comparison
- **Cost Analysis**: TCO modeling using data from multiple sources (Cloudera, Confluent, AWS, Netflix)
- **Adoption Rates**: Industry surveys (Dremio, Databricks, Confluent) with sample size and methodology disclosure

**Qualitative Synthesis**:
- **Implementation Patterns**: Cross-case analysis of production deployments (Netflix, Uber, LinkedIn, Cloudflare, SK Telecom)
- **Expert Validation**: Practitioner interviews for hypothesis validation
- **Contradiction Analysis**: When sources conflict, document both perspectives with evidence quality assessment (post-audit state, per §3.8: one named tension — H-LOGCOMP-01's specialized-compression result against H-ARCH-01's open-format consensus — is resolved as a standardization-cost trade rather than a contradiction; the earlier convergence examples rested on citations withdrawn in the 2026-06/07 audits and were removed)

**Gap Analysis**:

Literature Gaps Identified:
1. **DuckDB Edge Processing** (H-EDGE-01): Limited production security deployments documented
2. **Catalog Meta-Catalog Adoption** (H-ARCH-03): Emerging technology, adoption data sparse
3. **OCSF Production Deployments**: Schema standard adoption unclear beyond vendor claims
4. **Mid-Market Data Volumes**: Claims validated at large scale, need mid-market validation
5. **Direct SIEM Pricing**: Cost comparisons rely on storage optimization vs direct SIEM quotes
6. **Security-Specific Benchmarks**: Most performance data from general analytics workloads

New Hypotheses from Gap Analysis (3 identified): Catalog unification patterns reducing operational complexity, edge processing viability for security analytics (DuckDB), table format interoperability (XTable) adoption timelines

**Thematic Organization**:

Sources organized by theme rather than chronologically:
1. Foundational Architecture (table formats, query engines, streaming)
2. Security-Specific Data (volumes, cost comparisons, schema standards)
3. Vendor Landscape (platform capabilities, performance benchmarks)
4. Implementation & Organizational (change management, skills, deployment)
5. Emerging Technologies

### 2.7 Rigor and Reproducibility

**Version Control for Citation Stability**:

Living literature reviews create citation instability (researchers cite moving targets). Solution: Git-based version control with quarterly snapshots.

- **CHANGELOG.md**: Documents all revisions with timestamps and rationale
- **Versioned Files**: YYYY-QX-update.md snapshots enable citation of specific review versions
- **Policy**: Never edit published versions; create new version rather than edit existing

Academic Citation Format:
```
Wiley, J. (2025). Modern Data Stack for Cybersecurity: Living Literature Review
(Version 2025-Q4). https://github.com/flying-coyote/security-data-literature-review
```

**Transparency and Documentation**:

*Methodology Documentation*: LITERATURE-EXTRACTION-PLAN.md (complete extraction process), PROJECT-BRIEF.md (separates canonical facts from assumptions), MASTER-BIBLIOGRAPHY.md (standardized format with evidence levels)

*Reproducibility*: All extraction from source documents traceable, automated URL validation scripts (planned), expert interview guides publicly documented

**Quarterly Update Methodology** (Planned - Phase 2):
1. **Month 1**: IT Harvest vendor data refresh + platform capability updates
2. **Month 2**: Expert validation cycle + blog synthesis
3. **Month 3**: Publication of versioned snapshot (YYYY-QX-update.md)

### 2.8 Limitations and Threats to Validity

**Acknowledged Limitations**:

1. **Source Document Dependency**: the corpus began as an extraction of 283 footnotes from a single best-practices document, and that origin shaped it
   - *Mitigation*: supplemented with expert validation, vendor documentation, standards material, and — since 2026-07-13 — a systematic database search whose 26 surviving studies entered the corpus through a route the original curation did not control
   - *Residual*: the search measured the size of the problem before it fixed it. Recall of the curated corpus against a systematic search of its own subject was **zero of 40**. A curated corpus that had never been tested against the indexed literature turned out not to overlap it at all

2. **Vendor Documentation Prevalence**: vendor-authored material (63 vendor blogs and product docs, plus 14 big-tech engineering blogs) is 77 of 221 entries (34.8%) — the largest single bloc, and larger than the peer-reviewed literature
   - *Mitigation*: prioritize production-validated vendor sources (Netflix, Uber, Cloudflare); exclude marketing materials; flag bias per entry; never rest a hypothesis on a vendor source alone
   - *Residual*: a review that urges practitioners to distrust vendor accounts is itself, by source count, substantially built from them

3. **Venue Quality in the Indexed Literature**: of the 40 studies the systematic search topically included, 14 were not fit to cite — eight of them published in predatory, hijacked, or paper-mill-compromised venues
   - *Impact*: this is a limitation of the field, not only of the review. A fifth of what a systematic database search returns at the security/data-architecture intersection cannot be used, which means any review of this literature that trusts indexing alone will cite junk. Venue integrity was made part of tier assignment as a result
   - *Mitigation*: every included study's venue was resolved at the DOI and checked against DOAJ, Scopus, Web of Science, delisting records and predatory-publisher lists, then put to an independent verifier instructed to refuse under uncertainty (`methods/prisma-appraisal-2026-07-13.json`)

4. **Non-Independence Within the Search Arm**: the 26 incorporated studies resolve to only 23 independent author groups
   - *Impact*: sharpest where it hurts most. The two studies that were supposed to put peer-reviewed footing under the corpus's weakest, vendor-sourced claims — ClickHouse storage reduction, and pipeline log-reduction economics — share a single author, and one of the two appears in a journal removed from DOAJ in 2017. They corroborate each other, not the claim. Three further studies (the CATRACA line of work) come from one group
   - *Mitigation*: both are catalogued with the dependency stated in the entry itself, and neither is treated as independent confirmation

5. **The Search Cannot Reach the Storage Literature**: the database query is conjunctive — a security term AND a data-architecture term — and the storage-side papers this review depends on do not carry a security term in their title or abstract
   - *Impact*: 24 peer-reviewed entries already in the corpus (Delta Lake, LHBench, FastLanes, LogLite, DBSP, Ursa, and their PVLDB/CIDR/SIGMOD kin) were **unreachable by construction** by the very search meant to test the corpus's coverage. The systematic search therefore validated one half of this review's subject and was structurally blind to the other
   - *Mitigation*: none applied in this edition; the limitation is reported rather than repaired. A future run needs a second query arm on the storage side, with the security constraint dropped and relevance restored by hand

6. **Publication Bias**: Successful deployments more likely published than failures
   - *Mitigation*: Expert interviews capture implementation challenges not in public documentation

7. **Geographic Bias**: Predominantly US/European sources (some Asia-Pacific representation like SK Telecom)
   - *Impact*: May miss regional deployments, though major vendors and standards bodies publish in English

8. **Organizational Bias**: Large enterprises more likely to publish than mid-sized organizations
   - *Impact*: Mid-market validation needs additional evidence collection

9. **Temporal Currency**: Rapidly evolving field, findings may age quickly
   - *Mitigation*: Living review with quarterly updates maintains currency

10. **Access Constraints**: Some industry analyst reports behind paywalls (cited but not fully analyzed)
   - *Impact*: 3 sources (Gartner, IDC, Forrester) verified but not deeply analyzed

11. **English-Language Sources**: The synthesised corpus is in English
   - *Impact*: May miss regional deployments, though major standards bodies publish in English. The systematic search returned Portuguese- and Russian-language records; the Portuguese short-course chapter is catalogued, and the rest were excluded on other grounds

**Threats to Validity**:

*Internal Validity*: Single extractor (Jeremy Wiley) introduces potential bias
   - *Mitigation*: Expert network review (Lisa Cao, Jake Thomas, a data-platform practitioner) provides validation

*External Validity*: Large enterprise focus may not generalize to mid-market
   - *Acknowledged*: Findings most applicable to organizations with similar scale/resources

*Construct Validity*: Evidence level classification subjective
   - *Mitigation*: Explicit rubric, transparent scoring, multiple reviewers for critical sources

*Author Independence*: the author's commercial position and its handling are declared in the Conflict of Interest statement below.

---

## 3. FINDINGS

### 3.1 Overview of Evidence Base

**Source statistics** (derived per entry on 2026-07-13, not self-reported):
- **Total sources**: 221 catalogued entries, of which 219 carry an evidence tier and 2 are documented no-primary stubs
- **Evidence levels**: Level A 42.9% (94/219), Level B 46.6% (102/219), Level C 10.5% (23/219), Level D 0%

**Source type distribution** (Figure 3; derived by `scripts/derive_source_taxonomy.py` and reconciled against the bibliography):
- **Vendor engineering blogs and product documentation**: 63 (28.5%)
- **Peer-reviewed academic**: 50 (22.6%)
- **Open-source project documentation, specs, and repositories**: 33 (14.9%)
- **Practitioner talks and personal blogs**: 18 (8.1%)
- **Standards, frameworks, and government publications**: 17 (7.7%)
- **Big-tech engineering blogs**: 14 (6.3%)
- **Analyst and industry reports**: 12 (5.4%)
- **Books**: 8 (3.6%)
- **Expert interviews, first-party lab measurements, documented no-primary stubs**: 2 each

Two observations follow from that distribution, and both cut against the review rather than for it.

The first is that vendor-authored material — vendor blogs and product documentation, plus the big-tech engineering blogs — is 77 of 221 entries (34.8%), which makes it the largest bloc in the corpus and larger than the peer-reviewed literature. A review arguing that security teams should evaluate data platforms on measured evidence rather than vendor accounts is itself, by source count, substantially built on vendor accounts. The mitigation is real but partial: vendor sources are tiered, their bias is flagged per entry, and no hypothesis rests on one alone. The imbalance remains.

The second is that the peer-reviewed share (50 of 221, 22.6%) roughly doubled on 2026-07-13, when the systematic search's surviving 26 studies were incorporated — and that the corpus had, before that date, a *measured* recall of zero against a systematic search of its own subject. The peer-reviewed base of this review is younger than the review.

**Geographic/organizational diversity**:
- **Regions**: United States, Europe, Asia-Pacific (SK Telecom); the search arm added Brazilian, Japanese, Thai, Ukrainian, Czech and Slovak work
- **Organization types**: Tech giants, enterprises, startups, government, standards bodies, and — new with the search arm — public research infrastructure (CERN, INFN-CNAF, Lawrence Berkeley National Laboratory), which is the one category of production-scale deployment with no product to sell
- **Industries**: Technology, telecommunications, retail, energy, finance, scientific computing

### 3.2 Theme 1: Foundational Architecture Patterns

Our analysis identifies three architectural patterns validated across multiple production security deployments: Apache Iceberg for table formats, ClickHouse for OLAP analytics, and Kafka Streams for real-time processing.

#### 3.2.1 Table Formats: Apache Iceberg as Industry Consensus

Apache Iceberg emerged as the industry consensus choice for open table formats, validated by universal vendor support and production deployments at scale. Multiple independent sources confirm this pattern:

**Universal Vendor Adoption**: AWS, Google Cloud, Microsoft Azure, Snowflake, and Databricks all announced Iceberg compatibility, providing interoperability broader than Delta Lake's single-vendor governance model, where competing vendors face architectural friction under Databricks-led governance.

**Community Strength**: Apache Software Foundation governance attracted 400+ contributors (407 per GitHub's deduplicated contributor count for apache/iceberg, as of 2026-07-09), demonstrating vendor-neutral development uncommon in enterprise data infrastructure [2].

**Production Validation**: SK Telecom operates Iceberg with Trino in production for large-scale analytics [18].

**Adoption Trends**: Dremio's 2024 survey found 29% of organizations planning open table format adoption chose Iceberg vs 23% for Delta Lake [9], indicating growing momentum despite Delta's earlier market entry.

Our original "76% adoption" hypothesis required refinement to "industry consensus as de facto standard" due to source limitations, but the underlying claim—Iceberg dominance—received strong validation across these sources.

#### 3.2.2 Query Engines: ClickHouse Performance for Security Workloads

ClickHouse demonstrated measured performance for security analytics, validated by production deployments processing telemetry at scale:

**Cloudflare Production** (6M requests/second): Cloudflare's HTTP analytics processes 6 million requests per second [3]. Its Elasticsearch-to-ClickHouse log-pipeline migration cut per-record storage from 600 bytes to 60 bytes (~10×) [17], efficiency critical for security workloads generating TB/day volumes.

**Storage Efficiency**: ClickHouse's billion-row benchmark vs Elasticsearch measured 12-19× less storage at functionally equivalent configuration [5] (9-12× with Elasticsearch `_source` disabled) — a vendor benchmark, but directionally consistent with Cloudflare's independent production migration.

**Security-Specific Optimization**: ClickHouse native IPv4/IPv6 data types speed up CIDR-based threat hunting vs string-based IP storage common in general analytics platforms. A first-party CIDR probe on the MOAR reference stack (ClickHouse, one host, 20M rows, `lab/cidr_probe.py`, 2026-06-07) measured ~13-17× warm, 0.010 s native IPv4 vs 0.166 s per-row String parsing on the identical answer, with the IPv4 column ~2.9× smaller in storage (65.4 MiB vs 188.1 MiB) [20], [21]. This security-specific feature justifies platform selection independent of general OLAP capabilities.

Multiple sources validate ClickHouse performance claims, with Cloudflare representing production telemetry at scale.

#### 3.2.3 Streaming Architectures: Kafka Streams Production Patterns

Kafka-based stateful stream processing is validated at production scale across major deployments:

**LinkedIn Stateful Processing (Samza)**: LinkedIn's Samza — its Kafka-based stream processor, sharing Kafka Streams' local-state design — scales to state sizes of hundreds of TB per application, with partitioned local state serving millions of requests/sec (Noghabi et al., VLDB 2017) [14]. Stateful processing enables per-user, per-device behavioral analytics impossible with batch SQL aggregations. *The earlier "terabytes of state with millisecond access" attribution to Kafka Streams at LinkedIn was corrected in the 2026-07 verification pass: LinkedIn's engine is Samza, and the verified figures are those above.*

**Microsoft Azure Scale**: Azure Event Hubs (Kafka-compatible) processes trillions of events daily [12], validating Kafka scalability for cloud-scale security telemetry. Security incidents drive sharp traffic surges, requiring elastic streaming capacity.

LinkedIn and Microsoft provide production validation for Kafka-based security telemetry patterns.

**Peer-reviewed corroboration (added 2026-07-13)**: until the systematic search was run, every source in this subsection was a vendor or big-tech engineering account. The search supplied academic measurements of the same patterns. Andreoni Lopez et al. (*Concurrency and Computation*, 2019) report a deployed stream-processing threat-detection function sustaining over 95% accuracy against DoS and probe traffic across three datasets and over 85% under concept drift — detection embedded in the pipeline rather than bolted on after it [29]. Loganathan et al. (IEEE GLOBECOM, 2018) measure an auto-scaling CEP processor at over 2.5 million events/sec [35] with lower resource use than a monolithic deployment, which is the elastic-scaling argument this review makes from vendor material elsewhere. Saputra et al. (*Big Data and Cognitive Computing*, 2022) measure Kafka at a maximum 650,000 messages/sec and 172 MB/s into a Spark/Hadoop backend [37]. Husák and Kašpar (ARES, 2019) deploy stream-based alert correlation inside SABU, a production multi-peer alert-sharing platform [33]. None of these was in the corpus before 2026-07-13.

### 3.3 Theme 2: Cost Economics & TCO Reality

Modern data stack architectures promise cost savings vs traditional SIEM, but operational reality reveals nuanced trade-offs requiring quantitative analysis.

#### 3.3.1 Streaming Architecture Cost Premium

Streaming architectures incur materially higher operational costs than batch processing:

**Specialized-Skills Scarcity**: Fault-tolerance expertise (exactly-once semantics, checkpointing, backpressure management) is scarce relative to commodity SQL skills, creating talent competition that drives salary premiums. *The "Level 4 skill / top 5% of organizations" classification previously attributed to DORA 2024 was withdrawn in the 2026-07 verification pass — no such taxonomy appears in that report; the scarcity claim is stated directionally pending re-sourcing.*

**Cloudera TCO Analysis (withdrawn)**: A licensing/hardware/operational TCO breakdown formerly cited here to Forrester's Cloudera TEI studies appears in neither TEI document [10], [11] and was withdrawn in the 2026-07 verification pass. The underlying observation — batch platforms already carry a significant operational-cost share, and streaming increases it — stands as a directional claim only.

The citations behind the original quantitative TCO multiplier did not survive the 2026-06 source audit, so the premium is stated directionally pending re-sourcing.

#### 3.3.2 Tiered Storage Economics

Tiered storage strategies materially reduce the cost of multi-year security data retention:

**Kafka Tiered Storage**: Hot data (recent 7-30 days) resides on Kafka brokers; cold data (historical compliance retention) migrates to object storage (S3), cutting the cost of holding multi-year retention online [7].

**Storage Tier Economics**: Hot tier (S3 Standard, Kafka brokers) provides <100ms access at full price; warm tier (S3 Infrequent Access) trades lower cost for <1s latency; cold tier (S3 Glacier) is priced for archive, with 12-48 hour retrieval for audit/compliance queries. First-party price derivation (AWS public list prices, US-East-1, fetched 2026-07-09): against S3 Standard at $0.023/GB-month, Standard-IA ($0.0125) is 45.7% cheaper, Glacier Instant Retrieval ($0.004) 82.6%, Glacier Flexible Retrieval ($0.0036) 84.3%, and Glacier Deep Archive ($0.00099) 95.7% — list-price-per-GB deltas only, before retrieval fees and minimum-storage-duration charges, so they bound the achievable saving rather than state an effective TCO [20].

**Security Application**: Compliance requirements (HIPAA, PCI-DSS, SOC 2) mandate multi-year queryable retention (1-7 years). Tiered storage makes extended retention economically viable because security querying concentrates heavily on the most recent ~30 days, with only a small share touching older data (hot tier justified, cold tier appropriate) — a practitioner observation stated illustratively; the formerly stated 70%/<5% split had no locatable source and was withdrawn in the 2026-07 verification pass.

The citations behind the original quantitative savings band did not survive the 2026-06 source audit, so the savings claim is stated directionally pending re-sourcing.

#### 3.3.3 Reliability Cost Economics

Reliability investments scale steeply in cost with each additional "nine" of availability, and many organizations buy more availability than the business case supports:

**Reliability Economics**: Each additional "nine" of availability costs disproportionately more, because infrastructure redundancy, operational complexity, and testing overhead all rise with the availability target, while equivalent security effectiveness is often achievable at lower availability. A tiered reliability model reserves the highest availability for mission-critical components only: detection engines and SOC consoles may warrant four nines, while data storage and batch processing tolerate two-three nines (99-99.9%). Cost-benefit analysis rarely justifies five nines for security platforms. (The specific cost multipliers and overspend percentages previously cited here rested on placeholder citations and were removed in the 2026-06 source audit.)

**Security Context**: SIEM availability of three nines (99.9% = 8.76 hours downtime/year) suffices for most security operations. Detection engines require four nines for critical alerting, but data lake storage accepts two-three nines (batch processing tolerates delays).

Right-sizing availability targets lets practitioners reclaim infrastructure costs from over-provisioning.

### 3.4 Theme 3: Implementation Reality

Vendor marketing timelines contrast sharply with implementation reality documented in industry research and production case studies.

#### 3.4.1 Staffing Requirements and Specialized Skills

Streaming architectures require materially more operational staff than batch alternatives, and the fault-tolerance expertise they demand is scarce:

**Skills-Scarcity Spectrum**: Fault-tolerance expertise (Kafka exactly-once semantics, Flink checkpointing, backpressure management) sits at the scarce end of a spectrum that runs from commodity SQL skills through advanced distributed-systems experience. *The "Level 1/3/4" taxonomy and its organization-share percentages, previously attributed to DORA 2024 [8], were withdrawn in the 2026-07 verification pass (not present in that report); the spectrum framing is retained as directional only.*

**Security-Specific Hybrid Skills Scarcity**: Security architect + distributed systems expertise rarely combined in single practitioner. Organizations choose between upskilling security team (6-12 months to proficiency, stated as practitioner estimate), hiring data engineers with 20-30% salary premium, or outsourcing via tiger teams/managed services.

**Incident Rate Impact**: Streaming architectures carry higher operational incident exposure than batch, requiring 24/7 on-call rotation with deep troubleshooting expertise (backpressure root cause analysis, stateful processing debugging). On-call compensation adds 15-20% staffing cost beyond base salary premium.

The citations behind the original staffing multiplier did not survive the 2026-06 source audit (fabricated entries or stats not present in the cited sources), so the staffing premium is stated directionally pending re-sourcing. The 2026-07 verification pass additionally withdrew the DORA-attributed skill-taxonomy classification (not present in that report).

#### 3.4.2 Implementation Timelines

Security-focused data lakehouse implementations run materially longer than vendor marketing suggests:

**Security-Specific Constraints**: Compliance validation gates (HIPAA, PCI-DSS, SOC 2 reviews), security tool integrations (EDR, SIEM, threat intel platforms), and detection logic migration (translating and validating existing rules) each extend timelines beyond general data engineering baselines.

**Proficiency Timeline**: Teams typically need 6-12 months to reach proficiency after initial deployment — a practitioner estimate; the Gartner attribution formerly here had no locatable source and was withdrawn in the 2026-07 verification pass, and the month-by-month curve that follows is illustrative. Month 1: 20% productivity (heavy vendor support); Month 3: 50% productivity (independent operations, escalations for complex issues); Month 6: 75% productivity (optimization, cost management); Month 12: 90% productivity (architectural evolution). Year 1 TCO must include vendor support contracts or consulting budget for learning curve support.

The citations behind the original average-timeline figure did not survive the 2026-06 source audit, so the finding is stated directionally: security-focused implementations run months, not weeks, and the supporting evidence is US-centric (European GDPR/APAC data localization may extend timelines further).

#### 3.4.3 Skills Scarcity and Training Investment

Platform selection correlates with skill availability, creating trade-offs between operational simplicity and specialized capabilities:

**SQL-Friendly Platforms** (Trino, ClickHouse, Iceberg): 2-4 month learning curve leveraging existing analyst SQL skills. Low-Medium scarcity enables internal skill development.

**Kafka Fundamentals**: 3-4 months for pub/sub basics, 6-9 months for Kafka Streams stateful processing. Medium-High scarcity requires training investment ($15K-$20K per engineer for fundamentals, $25K-$35K for advanced) plus 200-300 hour time commitment.

**Flink Stateful Processing**: 9-12 months proficiency timeline, 300-400 hours training investment ($35K-$50K including opportunity cost). High scarcity makes hiring external expertise (20-30% salary premium) competitive with internal development.

**Training ROI Analysis**: Kafka Streams training investment ($25K per engineer for 200 hours) breaks even in 6 months if enabling transition from Confluent Cloud ($150K annual premium vs self-hosted) to internal operations. Risk: Training wasted if engineers leave before ROI realized or proficiency not achieved in 6-12 month window.

**Recommendation**: Managed services for Year 1 (de-risk timeline), build expertise in parallel, transition to self-hosted Year 2 after proficiency achieved. Batch-only implementations start with SQL-friendly platforms (ClickHouse, Trino, Iceberg); avoid Flink/Kafka unless real-time requirements justify the streaming cost premium AND can hire scarce fault-tolerance expertise OR accept 12-18 month proficiency timeline.

### 3.5 Theme 4: Performance Benchmarks

Production deployments provide quantitative performance validation across query engines, streaming platforms, and table formats, establishing realistic expectations vs vendor marketing claims.

**Query Performance Validation**: ClickHouse processes 6M req/sec at Cloudflare, and SK Telecom operates Iceberg with Trino in production at large scale (see Section 3.2 for details).

**Streaming Throughput**: Kafka-compatible streaming is validated at trillion events/day scale in Microsoft Azure production. LinkedIn's Samza runs stateful jobs at up to hundreds of TB of state per application, serving millions of requests/sec from local state (VLDB 2017).

**Storage Efficiency**: ClickHouse cut Cloudflare's per-record log storage ~10× (600→60 bytes/row), and its billion-row vendor benchmark measured 12-19× less storage than Elasticsearch (9-12× with `_source` disabled). Kafka tiered storage cuts the cost of multi-year retention. Apache Arrow Flight SQL is designed for faster result retrieval than JDBC/ODBC [1], which matters for multi-engine architectures.

**Security-Specific Benchmarks**: ClickHouse native IP types speed up CIDR-based threat hunting vs string-based implementations (a first-party probe measured ~13-17× at 20M rows on a single host, with ~2.9× IPv4-vs-String storage savings). Incident response drives traffic surges requiring elastic burst capacity. These security-specific requirements differentiate performance needs from general analytics.

**Benchmark Caveats**: Vendor benchmarks require skepticism; Cloudflare's production deployment (6M req/sec) is the strongest independent validation in this set. Your mileage may vary based on query patterns, data characteristics, infrastructure (SSD vs HDD), configuration tuning, and workload specifics. Recommendation: Pilot with your data before production commitment.

**Engine comparisons from the search arm (added 2026-07-13)**. This review has argued that vendor benchmarks are optimized for the vendor and that the field needs like-for-like comparisons on identical security workloads. The systematic search found some, and they belong here rather than in a future-work list.

Kajiura and Nakamura (IEEE COMPSAC, 2024) run five machine-learning NIDS classifiers through one distributed pipeline and report the throughputs separately from the accuracies: Decision Tree at 22,972 sessions/sec, Naive Bayes at 22,736, Random Forest at 19,869, SVM at 8,413, and kNN at 723 — a thirty-fold spread — while the three fastest, once tuned, land within about 0.008 of each other on F1 (0.964–0.972) [34]. The bottlenecks they locate are in Zeek, Logstash and Elasticsearch, not in the models. That is this review's central methodological claim, measured by someone else: the pipeline, not the classifier, is where the throughput goes.

Abbasi et al. (*Computers*, 2026) compare Faust and Streamz on an identical IoT intrusion-detection workload with significance testing, reporting Streamz at 4,450 events/sec with a 12 ms median latency and 40 MB resident memory, and Faust holding 93–98% detection accuracy; Streamz sustains above 95% efficiency to 3,500 events/sec while Faust degrades past 2,500 [27]. Notably, they find Faust and Kafka Streams statistically indistinguishable on detection quality (96.2% vs 96.8%, p = 0.318) while the performance differences across engines are significant (p < 0.001, Cohen's d > 0.8) — engine choice moves throughput, not detection quality, which is precisely the separation practitioners are usually sold the opposite of.

Gentz et al. (IEEE eScience, 2019), at Lawrence Berkeley National Laboratory, publish serialization measurements for a full security data pipeline that make the format decision concrete: in Python, MsgPack serializes in 0.68 ms against JSON's 6.47 ms and Protobuf's 47.02 ms, while in C++ the ordering inverts and all three fall under 1 ms [32]. A format choice that looks like a detail costs two orders of magnitude in the wrong runtime.

*Caution on the two closest analogues to this program's own measurements.* The search returned one paper reporting workload-aware storage reduction for multi-tenant SIEM on ClickHouse (79% uncompressed, 70% compressed, with Sigma rule coverage preserved [30]) and one benchmarking Vector-based log-reduction against a Filebeat baseline over 3M+ SOC records (45% throughput improvement, 80% outbound traffic reduction, 98% attack coverage retained [31]). These are the two claims this review most needed peer-reviewed footing under, since it otherwise sources them from vendor blogs. They are the same author, publishing twice in 2026, and one of the two venues (IJACSA) was removed from DOAJ in 2017 and is indexed only in Web of Science's Emerging Sources index. They are reported here because a systematic review reports what its search returns; they are not treated as independent confirmation of anything, and the claims they touch remain vendor-sourced in substance.### 3.6 Theme 5: Security-Specific Considerations

Security workloads exhibit performance requirements fundamentally different from general analytics, requiring specialized platform capabilities:

**IP/CIDR-Based Threat Hunting**: ClickHouse native IPv4/IPv6 data types speed up CIDR-based threat hunting vs string-based IP storage common in general analytics platforms (Snowflake, BigQuery, Redshift) [6]; a first-party CIDR probe (MOAR reference stack, 20M rows, single host, 2026-06-07) measured ~13-17× warm, with the native IPv4 column ~2.9× smaller in storage than String. Security analysts constantly filter by IP/CIDR ("show all traffic to AWS IP ranges"), whereas business analytics rarely uses CIDR patterns. This security-specific optimization justifies platform selection independent of general OLAP capabilities.

**Burst Capacity for Incidents**: Active security incidents drive sharp traffic surges that last hours to days at investigation intensity. Business analytics exhibit predictable load (scheduled dashboard refreshes, end-of-quarter reports); security workloads demand unpredictable burst handling. Cloud elastic platforms (Athena, ClickHouse Cloud, Confluent Cloud) provide burst capacity without continuous over-provisioning; on-premises requires 4× capacity provisioning (expensive) or accepts degraded performance during critical investigations (unacceptable).

**Stateful Entity Behavior Tracking**: LinkedIn's Samza maintains partitioned local state at up to hundreds-of-TB scale per application, served at millions of requests/sec (VLDB 2017), the pattern per-entity security tracking needs ("what's normal for THIS user over 30 days?"). Business analytics aggregate by dimensions (SQL GROUP BY); security requires per-entity stateful history. Batch SQL re-processes entire historical windows per query (slow, expensive); stateful streaming maintains per-entity state continuously (fast, efficient).

**Multi-Year Queryable Retention**: CISA's AA23-193A advisory quotes OMB M-21-31's log-retention requirement for US federal civilian agencies [4] — at least 12 months in active storage plus 18 months in cold storage [15] — a compliance mandate rather than an APT-detection recommendation, but a concrete retention floor security teams can plan against. Compliance investigations require fast queries across multi-year data ("show all access to this patient record 2022-2024"), not cold archive restoration (48-hour delay unacceptable for HIPAA audit). Tiered lakehouse architecture (Iceberg + Trino) provides multi-year queryable retention at materially lower cost while maintaining acceptable performance.

**Analyst Productivity**: Sub-second queries enable iterative threat hunting with 10-20 pivots per investigation. Slow queries (30-60s) reduce exploration to 3-5 pivots before analysts abandon investigation due to delays (practitioner estimate).

Multiple production and government sources validate these security-specific requirements, distinguishing security analytics from general business intelligence workloads.

**Non-vendor production deployments (added 2026-07-13)**. The production-scale evidence in this review has one structural weakness that no amount of tiering fixes: it comes almost entirely from companies with a product to sell or a platform to promote. The systematic search surfaced the exception — public research infrastructure, which operates security telemetry at scale and publishes about it without a commercial interest. Panero et al. (PoS, ISGC 2018) describe CERN's intrusion-detection system processing approximately 1 TB/day in real time, with a stated goal of at least 5 TB/day [36]. Amori et al. (*EPJ Web of Conferences*, CHEP 2023) describe the equivalent platform at INFN-CNAF, a WLCG Tier-1 site, though they publish the architecture without a performance evaluation [28]. Gentz et al. (IEEE eScience, 2019) do the same for Lawrence Berkeley National Laboratory [32]. These are the only production-scale deployments in the corpus with no vendor incentive attached, and they were absent from it until a database search went looking.

### 3.7 Hypothesis Validation Summary

Nine hypotheses received quantitative validation (seven assessed in the original extraction; two formulated post-audit on 2026-07-10 from newly catalogued peer-reviewed primaries, provenance noted per row) with varying confidence levels based on source count, evidence quality, source diversity, quantitative precision, and geographic/organizational diversity. *[2026-06 source audit note: citations behind the staffing, TCO, timeline, and tiered-storage multipliers were withdrawn (fabricated entries or stats not present in the cited sources); the affected figures are removed below and those hypotheses revert to directional claims pending re-sourcing. A 2026-07 per-citation verification pass withdrew two further items — the DORA-attributed "Level 4 / top 5%" skill taxonomy and the Forrester TEI TCO breakdown — and re-attributed the LinkedIn stateful-processing figures to Samza (VLDB 2017). Scores were then recomputed on 2026-07-13 under the explicit rubric (`methods/scoring-rubric.md`, applied in `methods/RESCORE-2026-07-13.md`), which supersedes the 2026-07-09 adopted values where they differ; each score below states its five-dimension split so a reviewer can re-derive it in place, and pre-audit values are noted per hypothesis.]*

**Strongly Validated (⭐⭐⭐⭐⭐) - 1 hypothesis** *(tiers grouped by the 2026-07-13 rubric rescore; see `methods/RESCORE-2026-07-13.md`)*:

*H-ARCH-01 (Iceberg Dominance)*: Industry consensus as de facto standard for open table formats, validated by broad vendor support (AWS, Google, Snowflake, Databricks; Microsoft the named Delta-first holdout), Apache Software Foundation governance (407 GitHub contributors as of 2026-07-09), production deployments (SK Telecom operating Iceberg with Trino at scale), and growing adoption momentum (Dremio: 29% planning Iceberg vs 23% Delta). Confidence: 23/25 points (5/5/5/3/5 across source count, evidence quality, source diversity, quantitative precision, and organizational diversity), unchanged by the 2026-07-13 rescore — all four legs survived primary verification and two strengthened (GitHub-derived contributor count; SK Telecom figures verified in the Trino Summit slides [18]). Precision scores 3 rather than 5 because the surviving figures quantify adoption momentum and community size rather than the dominance share the claim asserts; the original "76%" was withdrawn and the claim refined to "industry consensus".

**High Confidence (⭐⭐⭐⭐) - 2 hypotheses**:

*H3-PERFORMANCE-01 (ClickHouse)*: 6M req/sec throughput validated by Cloudflare production (~10× per-record storage reduction in its ES→ClickHouse migration), 12-19× storage efficiency vs Elasticsearch per ClickHouse's billion-row benchmark (9-12× with `_source` disabled; treated as a vendor benchmark), and a first-party CIDR probe (`lab/cidr_probe.py`, 2026-06-07, ClickHouse single host, 20M rows) measuring ~13-17× native-IPv4 speedup over per-row String parsing on the identical answer [21]; the Shell deployment citation and the sub-second query-share figure were withdrawn in the 2026-06 source audit. Confidence: 19/25 points (5/3/3/5/3) — four legs, of which three are Level A, so evidence quality scores 3 rather than 5 (2026-07-13 rescore; the 2026-07-09 adopted 20/25 was not reachable from the rubric's anchor values; pre-audit 21/25).

*H-LOGCOMP-01 (Machine-Data-Specialized Compression; formulated post-audit 2026-07-10)*: Storage and processing designs specialized to machine-generated data deliver measured multiples over general-purpose equivalents on their evaluated workloads: LogLite streaming log compression averages up to 67.8% compression-ratio improvement and up to 2.7× compression speed against state-of-the-art baselines (PVLDB 18(11)) [24]; PBC reaches roughly twice the compression ratio of prior techniques on machine-generated data (SIGMOD/PACMMOD 2024) [26]; and Pebbles telemetry sketching reports up to ~8× transfer-volume reduction with ~27× throughput improvement (IEEE TPDS 32(8), 2021) [22]. All figures verbatim-verified at their primaries 2026-07-10. Blitzcrank (PVLDB 17(10)) is deliberately not counted as an anchor: it is semantic compression for in-memory OLTP (85% memory reduction at a 19% throughput cost on TPC-C [23]), cited only as the adjacent row-store result. Confidence: 17/25 points (3/5/1/5/3) — three independent peer-reviewed anchors, all Level A, but they are a single source type (academic), and organizational diversity scores 3 rather than 5 because LogLite and PBC share the Ant Group / Guangzhou University / UNSW author collaboration, so the three papers contribute two independent groups (with Colorado State), not three; no production-deployment leg yet. Relationship to H-ARCH-01, stated as a trade rather than a contradiction: this result quantifies what the open-format standardization trade costs — adopting Iceberg/Parquet buys interoperability and ecosystem at a measured compression/performance premium relative to specialized designs, and the two hypotheses together price the interoperability decision instead of sloganeering either side.

**Moderate (⭐⭐⭐) - 2 hypotheses**:

*H-STREAM-01 (Kafka-based Stateful Streaming)*: Stateful security processing at scale validated by LinkedIn's Samza (hundreds of TB of state per application, millions of requests/sec from local state — Noghabi et al., VLDB 2017 [14]; re-attributed from an orphaned Kafka Streams claim in the 2026-07 verification pass) and Microsoft Azure production scale (trillions of events/day); the Uber citation was withdrawn in the 2026-06 source audit. Confidence: 15/25 points (1/5/3/3/3), demoted from High in the 2026-07-13 rescore: the section now cites exactly two legs, and the rubric's source-count anchor prices 1-2 sources at 1 point, so the demotion is forced by the withdrawal rather than by any new doubt about the surviving legs, both of which are primary-verified. Precision scores 3 because the surviving figures are ranges rather than measured quantifications of the claim variable, and the evidence stays US-centric. Restoration path: one additional verified, catalogued production or peer-reviewed leg returns the hypothesis to 17/25 and the High band.

*H-SOC-BASELINE-01 (Production SOC Alert Base Rates; formulated post-audit 2026-07-10)*: In the production SOCs studied by Yang et al. (USENIX Security 2024), alert volume ran 24K-134K alerts per day while true attacks were on the order of 0.01% of alerts, with measured composition splits (27%/49%) documenting where the volume comes from [25]. All figures verbatim-verified at the primary 2026-07-10. Confidence: 13/25 points (1/5/1/5/1) — evidence quality and quantitative precision are at their maxima (peer-reviewed production measurement), but a single paper floors source count, source diversity, and organizational diversity at 1 each, exactly as the instrument's single-source caps require; a second independent production study is the promotion path. The architectural inference this base rate invites — that the cost side of a security data architecture goes almost entirely to events that never become incidents — is discussed in §4.1 as an inference and is deliberately not part of the hypothesis statement.

**Preliminary (⭐⭐) - 4 hypotheses** *(quantitative legs withdrawn in the 2026-06/07 audits; each claim is directional pending re-sourcing)*:

*H-COST-09 (Tiered Storage)*: Tiered storage materially reduces the cost of multi-year retention. The mechanism is well documented (Kafka tiered storage, S3 storage classes), but the citations behind the original savings band were withdrawn in the 2026-06 source audit and the query-recency split is now labeled illustrative. The restoration path opened: a first-party derivation of the S3 Standard/IA/Glacier tier-price deltas, tiered B because the underlying list prices are vendor-published, now bounds the achievable saving. Confidence: 9/25 points (1/1/1/3/3) — two legs, neither at Level A, one source type, and a bound rather than a realized measurement, so precision scores 3 (2026-07-13 rescore; pre-audit 19/25).

*H-IMPL-01 (Streaming TCO)*: Streaming carries a material operational cost premium vs batch. The citations behind the original multiplier were withdrawn in the 2026-06 source audit, and the Cloudera TCO breakdown formerly described here as surviving evidence was itself withdrawn in the 2026-07 verification pass (the 39/32/29 split appears in neither Forrester TEI document), leaving the hypothesis fully directional with no quantitative support. Confidence: 5/25 points (1/1/1/1/1) — zero scoreable legs, so every dimension takes its floor and the total is the instrument's minimum (2026-07-13 rescore; pre-audit 22/25).

*H-IMPL-02 (Staffing Scarcity)*: Streaming requires materially more operational staff than batch, and the fault-tolerance expertise it demands is scarce. The citations behind the original staffing multiplier were withdrawn in the 2026-06 source audit, and the DORA-attributed "Level 4 / top 5%" skill classification was withdrawn in the 2026-07 verification pass (not present in that report), leaving no quantified leg in this corpus. Confidence: 5/25 points (1/1/1/1/1) — zero scoreable legs, instrument floor (2026-07-13 rescore; pre-audit 23/25).

*H-IMPL-03 (Timeline Premium)*: Security-focused lakehouse implementations run materially longer than vendor marketing suggests, with security-specific constraints (compliance gates, tool integrations, detection logic migration) adding time. The citations behind the original average and premium figures were withdrawn in the 2026-06 source audit, and the proficiency-timeline attribution was withdrawn in the 2026-07 verification pass. Confidence: 5/25 points (1/1/1/1/1) — zero scoreable legs, instrument floor (2026-07-13 rescore; pre-audit 13/25; all-US-centric evidence — European GDPR/APAC localization may extend timelines). The three H-IMPL hypotheses previously carried a 6/7/7 gradation, which was judgment the instrument cannot express and is retired; they now tie at the floor.

**Validation Quality** (rubric rescore, 2026-07-13): the review's architecture and performance findings are validated at strong-to-high confidence on primary-verified production evidence (1 strongly validated, 2 high confidence), two hypotheses sit at moderate confidence (H-STREAM-01, whose demotion from High is forced by the source-count anchor after the Uber withdrawal, and H-SOC-BASELINE-01, which enters capped by its single source), and the organizational-cost findings remain preliminary (4 hypotheses) — their quantitative legs were withdrawn as fabricated attribution or figures absent from cited sources, and each is stated directionally pending re-sourcing. Every surviving score reflects only evidence that passed primary-source verification, and every score re-derives from `methods/scoring-rubric.md`.

### 3.8 Evidence Gaps & Contradictions

**Literature Gaps Requiring Future Research**:

1. **Mid-Market Data Volumes**: Claims validated at large enterprise scale (e.g., Cloudflare 6M req/sec); need 50-200TB mid-market validation for staffing, cost, timeline extrapolation.

2. **Direct SIEM Cost Comparisons**: Cost analyses rely on storage optimization data and TCO modeling; lack head-to-head Splunk vs ClickHouse or Sentinel vs lakehouse pricing with identical workloads.

3. **DuckDB Edge Processing** (H-EDGE-01): Emerging pattern for security analytics at edge with limited production security deployments documented. Requires expert validation (Jake Thomas interview pending).

4. **XTable Interoperability**: Cross-format table interoperability (Iceberg ↔ Delta ↔ Hudi) claims from vendors lack production use case validation. Requires expert validation (Lisa Cao interview pending).

5. **Catalog Adoption Metrics**: Gravitino meta-catalog and multi-catalog management patterns lack quantitative adoption data beyond anecdotal reports.

6. **Security-Specific Benchmark Suites**: TPC-like benchmarks exist for general analytics (TPC-H, TPC-DS); security workloads lack standardized benchmark suite for vendor-neutral performance comparison.

   *Partial first-party answer (2026-06-07)*: the SDW MOAR reference stack now provides a first-party, identical-workload starting point against this gap — one shared Apache Iceberg table holding OCSF events, queried by four engines (DuckDB, Trino, ClickHouse, StarRocks) with an answer-equality gate applied before any latency or storage figure is read, so the comparison rests on a verified correctness floor rather than vendor-optimized configurations. The headline first-party readings: no single engine wins every workload (DuckDB leads gated small-batch, StarRocks leads high-cardinality distinct), and a baseline probe measured a schema-on-read SIEM index at ~7.0× the columnar footprint on OCSF data [20], [21]. This does not close the gap — it is a single-host apparatus (Ryzen 5800H, WSL2), so organizational/TCO claims and streaming-throughput claims remain out of its reach, and the absolute latencies are bounded to that host (the relative pattern is the finding). A standardized, multi-node, concurrency-aware security benchmark suite is still future work; the contribution here is a reproducible identical-workload method with a correctness gate, not a datacenter benchmark.

**One Named Tension, Resolved as a Trade**: the post-audit H-LOGCOMP-01 (machine-data-specialized designs measurably beat general-purpose equivalents) sits in deliberate tension with H-ARCH-01's open-format consensus; §3.7 frames it as quantifying the cost of the standardization trade rather than as a contradiction. Beyond that, cross-source validation revealed convergent evidence without contradictions; apparent discrepancies resolved through use-case analysis rather than representing true contradictions. (The convergence examples previously cited here rested on citations withdrawn in the 2026-06 source audit and were removed.)

**Mitigation for Gaps**: Expert interview protocol addresses DuckDB (Jake Thomas) and catalog adoption (Lisa Cao) gaps. IT Harvest partnership (pending) will provide vendor landscape data for catalog/platform adoption metrics. Mid-market validation requires targeted case study identification in future quarterly updates.

---

## 4. DISCUSSION

### 4.1 Implications for Security Practitioners

This systematic review provides security practitioners with evidence-based guidance for infrastructure decisions, translating research findings into actionable operational recommendations:

**Architecture Selection Framework**: Apache Iceberg emerged as the safest choice for open table formats, validated by universal vendor support and production deployments (SK Telecom operating Iceberg with Trino at scale). ClickHouse validated for security analytics at scale (Cloudflare: 6M req/sec), with security-specific optimizations (native IP types: a first-party probe measured ~13-17× CIDR speedup at 20M rows on a single host, with ~2.9× IPv4-vs-String storage savings) justifying platform selection independent of general OLAP capabilities. Kafka-based stateful streaming is supported for entity tracking at moderate confidence (LinkedIn's Samza at hundreds-of-TB state scale, plus Azure's production scale), though the evidence is two US legs reporting ranges rather than measured quantifications, so the pattern is credible without being strongly validated; practitioners must also accept a material operational cost premium and a scarce-skills requirement before committing to streaming architectures.

**Budget Planning Reality**: Organizations evaluating modern data stacks must account for operational costs as a major TCO component. Streaming architectures incur a material operational cost premium vs batch; practitioners selecting streaming must justify with real-time detection requirements or MTTD reduction quantifying business impact. Tiered storage reduces the cost of multi-year compliance retention, transforming economics of extended retention from prohibitive to viable. Measured production base rates frame the whole budget conversation: in the SOCs studied by Yang et al. (USENIX Security 2024), 24K-134K alerts/day carried a true-attack share on the order of 0.01% [25], so nearly all storage, movement, and triage spend goes to events that never become incidents — an inference drawn here from their measured composition (H-SOC-BASELINE-01), not a cost claim the paper itself makes. Right-sizing reliability targets (three nines for SIEM storage vs four nines for detection engines) reclaims infrastructure costs from over-provisioning.

**Staffing Models and Skills Investment**: Security teams implementing streaming require materially more operational staff than batch, because the fault-tolerance expertise involved is scarce and commands salary premiums. Organizations face build vs buy decision: upskill internal team (6-12 months to proficiency — practitioner estimate — plus $25K-$50K training investment per engineer), hire external expertise (20-30% salary premium, competitive market), or outsource via managed services (30-50% cost premium, operational simplicity). Recommendation: Managed services Year 1 de-risk timeline while building internal expertise in parallel; transition to self-hosted Year 2 after proficiency achieved.

**Timeline Expectations Calibration**: Vendor marketing claims ("deploy in weeks") contrast sharply with the industry reality of multi-month security-focused implementations. Security-specific constraints add further time: compliance validation gates (HIPAA, PCI-DSS reviews), security tool integrations (EDR, SIEM, threat intel), detection logic migration (rule translation/validation). Team proficiency requires additional 6-12 months beyond initial deployment before achieving operational independence (practitioner estimate; a Gartner attribution here was withdrawn in the 2026-07 verification pass). Year 1 budgets must include vendor support contracts or consulting for learning curve.

**Hybrid Architecture Strategy**: Production deployments at Uber and Netflix validate the hybrid pattern [19]: streaming hot path for real-time detection (5-10% of workload), batch cold path for historical analysis (90-95% of workload). Hybrid captures most of streaming's detection value while avoiding the pure-streaming cost multiplier. Security teams should start batch (SQL-friendly platforms: ClickHouse, Trino, Iceberg), add selective streaming for highest-value use cases, measure MTTD improvement vs cost to justify expansion.

### 4.2 Comparison to General Data Engineering

Security analytics exhibit performance requirements fundamentally different from general business intelligence, requiring specialized platform capabilities:

**Volume Characteristics**: Security generates higher velocity data (continuous high-volume ingestion vs business analytics' batch ETL patterns) with longer retention requirements (OMB M-21-31 [15], quoted by CISA AA23-193A: ≥12 months active + 18 months cold for federal civilian agencies, vs general analytics' 3-6 month active data). Security data volume growth outpaces business analytics, requiring elastic scaling capacity.

**Performance Requirements**: Security rewards platform-native IP/CIDR handling absent in general analytics (a first-party probe measured ~13-17× CIDR speedup at 20M rows on a single host, with ~2.9× IPv4-vs-String storage savings). Incident-driven burst capacity requires elastic architecture or 4× over-provisioning; business analytics exhibit predictable load (scheduled dashboards, quarterly reports). Analyst productivity critically depends on sub-second query latency enabling 10-20 investigation pivots vs 3-5 pivots with slow queries (30-60s latency; practitioner estimate).

**Stateful Processing Patterns**: Security requires per-entity behavioral tracking ("what's normal for THIS user over 30 days?") vs business analytics' dimensional aggregation (SQL GROUP BY by region, product, quarter). Kafka-backed stateful processors maintain partitioned local state at up to hundreds-of-TB scale per application (LinkedIn's Samza, VLDB 2017) enabling real-time entity views impossible with batch SQL re-processing entire historical windows per query.

**Compliance Constraints**: Security operations demand multi-year queryable retention vs business analytics' acceptable cold archive (48-hour restoration delay unacceptable for HIPAA audit investigations). Compliance requires audit trails, data lineage, retention policies as first-class requirements, not optional features.

**Operational Patterns**: Incident response creates unpredictable query spikes requiring immediate analyst investigation vs business analytics' tolerance for batch processing delays. Detection engines require four nines availability (99.99%) while general analytics tolerates three nines (99.9%), creating differential reliability requirements within same infrastructure.

**Technology Fit Implications**: Platforms excelling at general analytics (Snowflake, BigQuery, Redshift) may underperform for security-specific patterns. ClickHouse native IP types, Kafka Streams stateful processing, and Iceberg multi-year queryable retention provide measured advantages for security patterns (e.g., the first-party ~13-17× CIDR probe). Generic data warehouses require workarounds (string-based IP storage, batch re-processing for entity history) imposing performance penalties unacceptable for security workflows.

### 4.3 Theoretical Contributions

This systematic review makes four theoretical contributions to knowledge:

**1. Cross-Domain Synthesis Methodology**: First systematic literature review bridging cybersecurity and data engineering domains using PRISMA-aligned methodology adapted for computer science. Evidence classification system prioritizes production deployments, peer-reviewed research, and government standards while maintaining practitioner relevance. Living review methodology with version control (quarterly snapshots, CHANGELOG.md) solves citation stability problem for rapidly-evolving technology domains, enabling academic references to specific review versions while supporting practitioner currency needs.

**2. Hypothesis-Driven Validation Framework**: Multi-dimensional confidence scoring rubric (source count, evidence quality, source diversity, quantitative precision, geographic/organizational diversity) provides transparent assessment of claim strength. Nine hypotheses were scored under this framework (a post-audit re-score was adopted 2026-07-09 and two hypotheses were added post-audit on 2026-07-10 from newly catalogued peer-reviewed primaries; the scores reported here are the 2026-07-13 recomputation under the explicit instrument, `methods/scoring-rubric.md`, which documents the anchor values and edge-case rules so every score is re-derivable by a reviewer rather than adopted on the authors' judgment). Framework enables appropriate claim strength in academic writing: strongly validated claims (⭐⭐⭐⭐⭐) support primary arguments, moderate confidence claims (⭐⭐⭐) require caveats. This addresses academic literature's tendency toward overconfident assertions or hedge-word ambiguity by providing quantitative confidence levels.

**3. Operational Reality Quantification**: Staffing multipliers, cost premiums, implementation timelines, and skills scarcity address a practitioner knowledge gap not addressed in academic security literature (focuses on algorithms, not infrastructure) or data engineering literature (focuses on general analytics, not security). Validation replaces vendor marketing claims with convergent evidence from independent sources and production case studies. This operational reality enables security organizations to make evidence-based infrastructure decisions with realistic budgets, timelines, and staffing plans.

**4. Security-Specific Performance Framework**: Identification of performance requirements unique to security (IP/CIDR hunting: a first-party probe measured ~13-17× speedup at 20M rows on a single host, with ~2.9× IPv4-vs-String storage savings; burst capacity: incident-driven surges; stateful entity tracking: hundreds-of-TB local state at LinkedIn's Samza; multi-year queryable retention) differentiates security analytics from general business intelligence. Framework enables technology selection based on security-specific patterns rather than extrapolating from general analytics benchmarks. Validation that generic platforms (Snowflake, BigQuery) underperform for security patterns justifies security-optimized platform selection (ClickHouse, Kafka Streams) independent of general OLAP capabilities.

### 4.4 Limitations & Future Work

**Study Limitations** (see Section 2.8 for detailed discussion):

*Source Document Dependency*: the corpus began as an extraction of 283 footnotes from a single best-practices document, supplemented with expert validation and vendor material, which introduces selection bias toward the author's priorities. The 2026-07-13 systematic search measured that bias rather than asserting it: recall of the curated corpus against a database search of its own subject was zero of 40, and the 26 studies that survived venue appraisal have been incorporated. The search's own blind spot — a conjunctive query cannot reach the storage-side literature — is stated in Section 2.8.

*Geographic Bias*: Predominantly US/European sources (SK Telecom provides Asia-Pacific validation, but limited). Cost differentials, regulatory constraints (GDPR, data localization), and implementation timelines may vary by region.

*Organizational Scale Bias*: Large enterprise focus (e.g., Cloudflare 6M req/sec) may not generalize to mid-market organizations (50-200TB workloads). Staffing, cost, timeline extrapolations require mid-market validation.

*Publication Bias*: Successful deployments more likely published than failures. Expert interviews capture implementation challenges not in public documentation, but failure analysis remains limited.

*Temporal Currency*: Rapidly evolving field (modern data stack 2018-2025 era) creates risk findings age quickly. Living review with quarterly updates (planned Phase 2) mitigates but does not eliminate temporal limitations.

**Future Research Directions**:

**1. Longitudinal Studies**: Track architecture evolution over quarterly updates to identify adoption trends, technology maturation patterns, and cost/performance trajectories. Planned IT Harvest partnership (pending) will enable systematic vendor landscape tracking with versioned snapshots (YYYY-QX-update.md) supporting temporal analysis.

**2. Mid-Market Validation**: Target 50-200TB security operations for quantitative validation of staffing, cost, timeline claims. Current evidence validates TB-PB enterprise scale; extrapolation to mid-market requires empirical validation, not assumption of linear scaling.

**3. Emerging Technology Validation**: DuckDB edge processing (H-EDGE-01), XTable table format interoperability, and Gravitino meta-catalog adoption require production security deployment case studies. Expert interviews (Lisa Cao - catalogs, Jake Thomas - DuckDB) address immediate gaps; quarterly updates track maturation.

**4. Comparative Performance Studies**: Head-to-head benchmarks (ClickHouse vs Druid vs Elasticsearch; Kafka Streams vs Flink vs Spark Streaming) with identical security workloads (not vendor-optimized benchmarks). Security-specific benchmark suite (TPC-like for security analytics) would enable vendor-neutral comparison. A first-party step in this direction now exists: the SDW MOAR reference stack runs four engines (DuckDB, Trino, ClickHouse, StarRocks) over one shared Iceberg/OCSF table with an answer-equality gate, producing an identical-workload comparison on first-party data (2026-06-07). It is deliberately scoped as a single-host apparatus, so it informs the relative engine pattern and a measured ~7.0× SIEM-index storage ratio [21] but not multi-node throughput, concurrency, or organizational TCO — those remain the open work this future direction names.

The 2026-07-13 systematic search partly answered this direction, which is worth recording because it is the clearest case of the search changing a finding rather than padding a bibliography. Abbasi et al. (Computers, 2026) benchmark Faust against Streamz on an identical IoT intrusion-detection workload with significance testing rather than a single headline multiple [27]; Yahyaoui et al. (ACIS SNPD, 2021) put Flink head-to-head against Spark Streaming on a security workload [38]; and Kajiura and Nakamura (IEEE COMPSAC, 2024) do the thing this review argues for most insistently — they separate the pipeline's throughput from the classifier's accuracy, and find five NIDS models spanning a thirty-fold throughput range while their three fastest, once tuned, land within about 0.008 of each other on F1, with the bottlenecks sitting in Zeek, Logstash and Elasticsearch rather than in the models [34]. The comparative literature this direction called for is thinner than it should be, but it is not empty, and it was not cited here until a systematic search went looking for it.

**5. Failure Analysis**: Systematic study of failed implementations overcoming publication bias. What streaming deployments were abandoned? What drove rollback from lakehouse to traditional SIEM? What organizational factors predict success/failure? Requires confidential case study access or retrospective practitioner surveys.

**6. Economic Impact Studies**: Quantify MTTD reduction from streaming vs batch architectures; measure analyst productivity gains from sub-second queries; calculate breach cost avoidance from enhanced detection. These ROI metrics justify streaming cost premiums with quantified business impact rather than architectural preference.

---

## 5. CONCLUSION

Modern data stack architectures promise to transform security operations, but practitioners evaluating these technologies face a critical knowledge gap: cybersecurity literature focuses on detection algorithms while data engineering literature addresses general analytics, leaving security-specific infrastructure guidance fragmented across disconnected domains. This systematic literature review bridges that gap, synthesizing 219 tiered sources spanning production deployments, peer-reviewed research, and government standards across the cybersecurity and data-engineering literatures under a PRISMA 2020 two-arm methodology.

Our hypothesis validation establishes operational reality contradicting vendor marketing claims. Apache Iceberg emerged as industry consensus for open table formats (universal vendor support, Apache Software Foundation governance); ClickHouse validated for security analytics at scale (Cloudflare 6M req/sec; a first-party CIDR probe measured ~13-17× native-IP speedup at 20M rows on a single host, with ~2.9× IPv4-vs-String storage savings); streaming architectures carry a material operational cost and staffing premium vs batch alternatives, with the required fault-tolerance expertise remaining scarce; implementation timelines for security-focused deployments run months, not weeks; and tiered storage reduces the cost of multi-year compliance retention. Two post-audit hypotheses extend the set with verbatim-verified peer-reviewed legs: measured production-SOC alert base rates (Yang et al., USENIX Security 2024) and machine-data-specialized compression beating general-purpose equivalents (H-SOC-BASELINE-01, H-LOGCOMP-01; added 2026-07-10). The 2026-06 and 2026-07 source audits withdrew the citations behind several of the originally stated multipliers and classifications, so those findings are stated directionally here pending re-sourcing, while the surviving production figures remain quantitative.

Production validation across organizations including Netflix, Uber, LinkedIn, Cloudflare, SK Telecom, and Microsoft demonstrates modern data stack viability for security operations while identifying security-specific requirements differentiating from general analytics: IP/CIDR-based threat hunting (a first-party probe measured ~13-17× speedup at 20M rows on a single host, with ~2.9× IPv4-vs-String storage savings), incident-driven burst capacity (requiring elastic architecture), stateful entity behavior tracking (hundreds of TB of local state per application at LinkedIn's Samza, millions of requests/sec), and multi-year queryable retention. These requirements justify security-optimized platform selection (ClickHouse, Kafka Streams, Iceberg) independent of general OLAP capabilities, as generic data warehouses (Snowflake, BigQuery, Redshift) may underperform for security-specific patterns.

Practitioner guidance synthesizes findings into actionable recommendations: Start with batch architectures using SQL-friendly platforms (ClickHouse, Trino, Iceberg) leveraging existing analyst skills; add selective streaming for highest-value real-time use cases after validating business impact justifies the streaming cost premium; implement tiered storage for multi-year compliance retention; right-size reliability targets (three nines for storage, four nines for detection engines) reclaiming infrastructure costs from over-provisioning; plan realistic timelines (multi-month implementation + a 6-12 month proficiency ramp) rather than vendor claims ("deploy in weeks"); and invest in scarce fault-tolerance expertise (upskill internal team, hire external talent, or outsource via managed services) before committing to streaming architectures.

This living literature review establishes foundation for ongoing evidence synthesis supporting quarterly technology updates. Planned IT Harvest partnership enables systematic vendor landscape tracking with versioned snapshots (YYYY-QX-update.md) solving citation stability problem while maintaining practitioner currency. Expert interviews (Lisa Cao - catalog landscape, Jake Thomas - DuckDB edge processing) address immediate evidence gaps. Future research priorities include mid-market validation (50-200TB workloads), comparative performance benchmarks (security-specific test suites), failure analysis overcoming publication bias, and economic impact studies quantifying MTTD reduction and analyst productivity gains justifying streaming cost premiums with business impact rather than architectural preference.

Security practitioners can now make evidence-based architecture decisions with documented cost/staffing/performance trade-offs, moving from vendor marketing claims to production-validated patterns. Organizations implementing modern data stacks for security operations have systematic evidence base replacing fragmented anecdotes, enabling realistic budgets (accounting for heavy operational costs), achievable timelines (multi-month implementation + proficiency period), and staffing plans (a streaming staffing premium and scarce specialized skills). The gap between cybersecurity and data engineering literatures is bridged, providing security practitioners with rigorous operational guidance previously unavailable in either domain independently.

---

## ACKNOWLEDGMENTS

*[Drafted 2026-07-09; FINALIZE after expert review completes — acknowledge only contributions actually received.]*

The author thanks the practitioners whose production experience informed this review's validation work, including a data-platform practitioner (anonymized by request) whose input shaped the Starburst/Athena viability assessment. Planned expert interviews — Lisa Cao (catalog landscape) and Jake Thomas (DuckDB edge processing) — will be acknowledged here on completion, as will the IT Harvest partnership (Charles Wells, vendor landscape data) if established. The 2026-06 and 2026-07 source audits that reshaped this manuscript's evidence base were internal work; the errors they corrected, and any that remain, are the author's own.

---

## FUNDING

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

---

## CONFLICT OF INTEREST

The author operates Security Data Works LLC, an independent consultancy whose commercial interests relate to the open, modular security-data architectures this review evaluates. The scoring rubric and evidence tiers used throughout are designed to be independently re-derivable precisely so that a reader need not rely on the author's judgment; all scoring inputs and scripts are in the public repository.

---

## DATA AVAILABILITY

The data underlying this review — the evidence-tiered bibliography (MASTER-BIBLIOGRAPHY.md), the hypothesis scoring data behind Section 3.7 and Table 2, and the figure source data — are available in the public repository at https://github.com/flying-coyote/security-data-literature-review, archived at DOI: 10.5281/zenodo.PLACEHOLDER (placeholder; minted on the tagged release).

---

## CODE AVAILABILITY

The scoring, count-reconciliation, and validation scripts used to derive every count and figure reported here (including `scripts/count_reconcile.py`, `scripts/automation_dashboard.py`, and the figure-generation scripts in `publication-graphics/`) are in the same public repository at https://github.com/flying-coyote/security-data-literature-review and the same archived deposit, DOI: 10.5281/zenodo.PLACEHOLDER (placeholder; minted on the tagged release).

---

## REFERENCES

*Generated 2026-07-09 from MASTER-BIBLIOGRAPHY.md, restricted to works cited inline in this manuscript; every entry below was verified against its primary during the 2026-06/2026-07 source audits or on generation day. The full living-review corpus (221 entries, 219 of them carrying evidence-tier classifications, derived 2026-07-13) is maintained in MASTER-BIBLIOGRAPHY.md in this repository and is the citable corpus this review synthesises; see Appendix D. Expert-interview inputs (L. Cao, J. Thomas, P. Agbabian) are personal communications and are not listed. First-party artifacts are labeled.*

[1] Apache Arrow Community, "Introducing Apache Arrow Flight SQL: Accelerating Database Access," Apache Arrow Blog, Feb. 16, 2022. [Online]. Available: https://arrow.apache.org/blog/2022/02/16/introducing-arrow-flight-sql/

[2] Apache Iceberg Community, "Apache Iceberg" (project documentation and community), Apache Software Foundation. [Online]. Available: https://iceberg.apache.org/ ; contributor count derived from https://github.com/apache/iceberg (407 contributors, GitHub deduplicated count, as of Jul. 9, 2026)

[3] A. Bocharov, "HTTP Analytics for 6M Requests per Second Using ClickHouse," Cloudflare Blog, Mar. 6, 2018. [Online]. Available: https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/

[4] CISA and FBI, "Enhanced Monitoring to Detect APT Activity Targeting Outlook Online," Cybersecurity Advisory AA23-193A, Jul. 12, 2023. [Online]. Available: https://www.cisa.gov/news-events/alerts/2023/07/12/cisa-and-fbi-release-cybersecurity-advisory-enhanced-monitoring-detect-apt-activity-targeting

[5] ClickHouse, "ClickHouse vs. Elasticsearch: The Billion-Row Matchup," ClickHouse Blog, May 7, 2024 (vendor benchmark). [Online]. Available: https://clickhouse.com/blog/clickhouse_vs_elasticsearch_the_billion_row_matchup

[6] ClickHouse, "IPv4 and IPv6 Data Types," ClickHouse Documentation. [Online]. Available: https://clickhouse.com/docs/sql-reference/data-types/ipv6

[7] Confluent, "Tiered Storage," Confluent Platform Documentation (Kafka tiered-storage mechanism). [Online]. Available: https://docs.confluent.io/platform/current/kafka/tiered-storage.html

[8] DevOps Research and Assessment (DORA) / Google Cloud, "2024 Accelerate State of DevOps Report," 2024. [Online]. Available: https://dora.dev/research/2024/dora-report/ (cited in this manuscript's audit notes; see §3.4.1)

[9] Dremio, "State of the Data Lakehouse 2024," press release, Nov. 2023 (survey: Propeller Insights, n=500). [Online]. Available: https://www.dremio.com/press-releases/state-of-the-data-lakehouse-2024-businesses-are-leaving-cloud-data-warehouses-for-data-lakehouses/

[10] Forrester Consulting (commissioned by Cloudera), "The Total Economic Impact of Cloudera Data Platform — Public Cloud," Oct. 2021.

[11] Forrester Consulting (commissioned by Cloudera), "The Total Economic Impact of Cloudera — Private Cloud," May 2024. [Online]. Available: https://tei.forrester.com/go/cloudera/onPremises/

[12] Microsoft Azure, "Processing Trillions of Events per Day with Apache Kafka on Azure," Azure Blog, Feb. 5, 2019. [Online]. Available: https://azure.microsoft.com/en-us/blog/processing-trillions-of-events-per-day-with-apache-kafka-on-azure/

[13] Netflix (D. Muino), "Petabyte-Scale Logging at Netflix with ClickHouse," ClickHouse Blog, 2025. [Online]. Available: https://clickhouse.com/blog/netflix-petabyte-scale-logging

[14] S. A. Noghabi, K. Paramasivam, Y. Pan, N. Ramesh, J. Bringhurst, I. Gupta, and R. H. Campbell, "Samza: Stateful Scalable Stream Processing at LinkedIn," *Proceedings of the VLDB Endowment*, vol. 10, no. 12, pp. 1634-1645, 2017. [Online]. Available: https://www.vldb.org/pvldb/vol10/p1634-noghabi.pdf

[15] Office of Management and Budget, "M-21-31: Improving the Federal Government's Investigative and Remediation Capabilities Related to Cybersecurity Incidents," Aug. 2021. [Online]. Available: https://www.whitehouse.gov/wp-content/uploads/2021/08/M-21-31-Improving-the-Federal-Governments-Investigative-and-Remediation-Capabilities-Related-to-Cybersecurity-Incidents.pdf

[16] M. J. Page et al., "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews," *BMJ*, vol. 372, n71, 2021, doi: 10.1136/bmj.n71.

[17] M. Singh, "Log Analytics Using ClickHouse," Cloudflare Blog, Sep. 2, 2022. [Online]. Available: https://blog.cloudflare.com/log-analytics-using-clickhouse/

[18] SK Telecom (J. Song and J. Oh), "Journey to Iceberg with Trino," Trino Summit 2022, Dec. 2022. Recap: https://trino.io/blog/2022/12/19/trino-summit-2022-sk-telecom-recap.html ; slides (precise figures): https://trino.io/assets/blog/trino-summit-2022/Trino@SK-Telecom.pdf

[19] Uber Engineering, "Inside Uber's Large-Scale Real-Time Analytics Platform," Confluent Current 2025 (conference session). [Online]. Available: https://current.confluent.io/post-conference-videos-2025/inside-ubers-large-scale-real-time-analytics-platform-bng25

[20] J. Wiley, "MOAR Stack — Security Data Lakehouse Reference Architecture" [dataset], Security Data Works (FIRST-PARTY reference architecture and cost model). [Online]. Available: https://securitydataworks.com/thesis/moar ; the figures cited from it are reproduced in this review's archived deposit, DOI: 10.5281/zenodo.PLACEHOLDER (placeholder; minted on the tagged release)

[21] J. Wiley, "SDW Lab Benchmarks" [dataset], GitHub repository (FIRST-PARTY: CIDR probe `lab/cidr_probe.py`, MOAR reference-stack engine comparison, schema-on-read baseline storage probe). [Online]. Available: https://github.com/flying-coyote/sdw-lab-benchmarks ; the result files cited here are reproduced in this review's archived deposit, DOI: 10.5281/zenodo.PLACEHOLDER (placeholder; minted on the tagged release)

[22] T. Buddhika, S. L. Pallickara, and S. Pallickara, "Pebbles: Leveraging Sketches for Processing Voluminous, High Velocity Data Streams," *IEEE Transactions on Parallel and Distributed Systems*, vol. 32, no. 8, pp. 2005-2020, Aug. 2021, doi: 10.1109/TPDS.2021.3055265. [Online]. Available: https://par.nsf.gov/servlets/purl/10284573

[23] Y. Qiao, Y. Gao, and H. Zhang, "Blitzcrank: Fast Semantic Compression for In-Memory Online Transaction Processing," *Proceedings of the VLDB Endowment*, vol. 17, no. 10, pp. 2528-2540, 2024. [Online]. Available: https://www.vldb.org/pvldb/volumes/17/paper/Blitzcrank%3A%20Fast%20Semantic%20Compression%20for%20In-Memory%20Online%20Transaction%20Processing

[24] B. Tang, S. Yang, Z. Shen, W. Zhang, X. Lin, and Z. Tian, "LogLite: Lightweight Plug-and-Play Streaming Log Compression," *Proceedings of the VLDB Endowment*, vol. 18, no. 11, pp. 3757-3770, 2025. [Online]. Available: https://www.vldb.org/pvldb/vol18/p3757-yang.pdf

[25] L. Yang, Z. Chen, C. Wang, Z. Zhang, S. Booma, P. Cao, C. Adam, A. Withers, Z. Kalbarczyk, R. K. Iyer, and G. Wang, "True Attacks, Attack Attempts, or Benign Triggers? An Empirical Measurement of Network Alerts in a Security Operations Center," in *Proceedings of the 33rd USENIX Security Symposium (USENIX Security '24)*, 2024. [Online]. Available: https://www.usenix.org/conference/usenixsecurity24/presentation/yang-limin

[26] J. Zhang, Z. Shen, S. Yang, L. Meng, C. Xiao, W. Jia, Y. Li, Q. Sun, W. Zhang, and X. Lin, "PBC: High-Ratio Compression for Machine-Generated Data," *Proc. ACM Manag. Data (PACMMOD)*, SIGMOD 2024, 2024. [Online]. Available: https://arxiv.org/pdf/2311.13947

**Format**: IEEE-style, alphabetical by author/organization. **Corpus note**: the 219 tiered sources synthesized by this review resolve through MASTER-BIBLIOGRAPHY.md (versioned, evidence-tiered, count derived rather than stated); the list above is the subset carrying claims in this manuscript.

---


**Systematic-search arm (incorporated 2026-07-13).** The following entries entered this review through the database search described in Section 2.2, not through the original curation. They are grouped here as [27]–[38] because they are a distinct provenance, and each carries the evidence tier its venue appraisal supports. The 14 studies the appraisal refused are not listed here; they are recorded, with reasons, in `methods/prisma-appraisal-2026-07-13.json`.

[27] M. Abbasi, F. Cardoso, P. Váz, J. Silva, F. Sá, and P. Martins, "Performance Comparison of Python-Based Complex Event Processing Engines for IoT Intrusion Detection: Faust Versus Streamz," *Computers*, vol. 15, no. 3, art. 200, 2026. doi: 10.3390/computers15030200. [Systematic-search arm, 2026-07-13; Level A.]

[28] F. Amori, S. Antonelli, V. Ciaschini, A. Falabella, E. Fattibene, F. Fornari, D. Lattanzio, D. Michelotto, and L. Morganti, "General Purpose Data Streaming Platform for Log Analysis, Anomaly Detection and Security Protection," *EPJ Web of Conferences* (CHEP 2023), vol. 295, art. 01032, 2024. doi: 10.1051/epjconf/202429501032. [Systematic-search arm; Level B — architecture in production, no performance evaluation published.]

[29] M. Andreoni Lopez, D. M. F. Mattos, O. C. M. B. Duarte, and G. Pujolle, "Toward a Monitoring and Threat Detection System Based on Stream Processing as a Virtual Network Function for Big Data," *Concurrency and Computation: Practice and Experience*, vol. 31, no. 20, e5344, 2019. doi: 10.1002/cpe.5344. [Systematic-search arm; Level A. Shares authors with the CATRACA conference and short-course reports; the three are one group.]

[30] N. Chalaemwongwan, "Workload-Aware Storage Reduction for Multi-Tenant SIEM on ClickHouse," *International Journal of Advanced Computer Science and Applications*, vol. 17, no. 4, 2026. doi: 10.14569/ijacsa.2026.0170474. [Systematic-search arm; **Level C — venue caveat**: IJACSA was removed from DOAJ in 2017 and is indexed only in Web of Science ESCI. Reported, not relied upon. Same author as [31]; the two are not independent.]

[31] N. Chalaemwongwan, "Comparative Evaluation of Log Reduction Techniques Using Vector on Public Security Datasets," *ECTI Transactions on Computer and Information Technology*, vol. 20, no. 2, 2026. doi: 10.37936/ecti-cit.2026202.264216. [Systematic-search arm; Level A. Same author as [30]; the two are not independent.]

[32] R. Gentz, S. Peisert, J. Boverhof, and D. Gunter, "SPARCS: Stream-Processing Architecture Applied in Real-Time Cyber-Physical Security," in *Proc. IEEE 15th Int. Conf. on eScience*, 2019, pp. 91-100. doi: 10.1109/escience.2019.00028. [Systematic-search arm; Level A. Lawrence Berkeley National Laboratory.]

[33] M. Husák and J. Kašpar, "AIDA Framework: Real-Time Correlation and Prediction of Intrusion Detection Alerts," in *Proc. 14th Int. Conf. on Availability, Reliability and Security (ARES)*, 2019, art. 81. doi: 10.1145/3339252.3340513. [Systematic-search arm; Level A. Deployed in the SABU production alert-sharing platform.]

[34] M. Kajiura and J. Nakamura, "Practical Performance of a Distributed Processing Framework for Machine-Learning-Based NIDS," in *Proc. IEEE 48th Annual Computers, Software, and Applications Conf. (COMPSAC)*, 2024. doi: 10.1109/compsac61105.2024.00355. [Systematic-search arm; Level A.]

[35] G. V. Loganathan, J. Samarabandu, and X. Wang, "Real-Time Intrusion Detection in Network Traffic Using Adaptive and Auto-Scaling Stream Processor," in *Proc. IEEE Global Communications Conf. (GLOBECOM)*, 2018. doi: 10.1109/glocom.2018.8647489. [Systematic-search arm; Level A.]

[36] P. Panero, L. Vâlsan, V. Brillault, and I. C. Schuszter, "Building a Large Scale Intrusion Detection System Using Big Data Technologies," in *Proc. Int. Symp. on Grids and Clouds (ISGC)*, PoS(ISGC2018)014, 2018. doi: 10.22323/1.327.0014. [Systematic-search arm; Level B. CERN.]

[37] F. A. Saputra, M. Salman, J. A. N. Hasim, I. U. Nadhori, and K. Ramli, "The Next-Generation NIDS Platform: Cloud-Based Snort NIDS Using Containers and Big Data," *Big Data and Cognitive Computing*, vol. 6, no. 1, art. 19, 2022. doi: 10.3390/bdcc6010019. [Systematic-search arm; Level B.]

[38] A. Yahyaoui, H. Lakhdhar, T. Abdellatif, and R. Attia, "Machine Learning Based Network Intrusion Detection for Data Streaming IoT Applications," in *Proc. 21st ACIS Int. Winter Conf. on Software Engineering, AI, Networking and Parallel/Distributed Computing (SNPD-Winter)*, 2021. doi: 10.1109/snpdwinter52325.2021.00019. [Systematic-search arm; Level B.]

## FIGURES

*Note (2026-07-13): Figure 4 regenerated from the rubric rescore (`methods/RESCORE-2026-07-13.md`); its band thresholds are now drawn at the rubric's boundaries (21/16/11). Figure 2 carries the live evidence tally (2026-07-09). Figure 1's flowchart carries no percentages; its caption below was corrected to drop the withdrawn 79% self-grade. The planned Figure 5 (technology adoption trends) was cut: its three panels restated H-ARCH-01, H3-PERFORMANCE-01, and H-STREAM-01 per technology, which Figure 4 and Table 2 now carry in full, and its remaining un-withdrawn figures were among those the audits corrected or re-attributed. This build has four figures.*

### Figure 1: PRISMA 2020 Flow Diagram

![Figure 1: PRISMA 2020 two-arm flow diagram. Databases and registers: 400 records identified (OpenAlex 354, dblp 46), 5 duplicates removed, 395 screened on title and abstract, 355 excluded against pre-specified criteria, 40 meeting the topical inclusion criteria, and 26 surviving a critical appraisal of venue integrity that excluded 14 — eight of them in predatory or compromised venues. Other methods: 195 curated entries, of which 171 are grey literature no database search returns. The two arms converge on the 219 tiered studies this edition synthesises. The search was run retrospectively on 2026-07-13 against a corpus built by curation, and overlap between the two arms is zero.](publication-graphics/figure1_prisma_flowchart.pdf){ width=85% }

Alt text: A PRISMA 2020 flow diagram with two identification arms converging on the review's evidence base. The left arm, identification via databases and registers, begins with 400 records — 354 from OpenAlex under a strict boolean title-and-abstract filter with a 2018 date floor, and 46 from dblp across eight title-level queries — from which 5 duplicates were removed (1 by DOI, 4 by normalized title), leaving 395 records screened on title and abstract. 355 were excluded against the pre-specified criteria, the largest groups being 137 data-engineering papers with no security application, 103 machine-learning intrusion-detection model papers that merely run on a streaming platform without evaluating the data architecture, and 36 dblp records falling outside the 2018 date floor, which dblp's API cannot enforce at query time. 40 met the topical inclusion criteria and then entered a critical-appraisal stage that the topical screening had not applied, in which venue identity was resolved at the DOI and indexing status established from primaries. That stage excluded 14: eight in predatory or compromised venues, including one paper in a hijacked journal and one in a title Clarivate delisted after an admitted paper-mill compromise; three not peer-reviewed at all, including a preprint typeset with a counterfeit publisher masthead; one whose full text could not be obtained at any price; and two whose citation the independent verifier refused. 26 studies were included. The right arm, identification via other methods, holds the 195 curated bibliography entries, of which 171 are grey literature that no database search returns — 63 vendor engineering blogs, 33 open-source project docs, 18 practitioner talks, 17 standards and government documents, 14 big-tech engineering blogs, 12 analyst reports, 8 books, and 6 further entries — alongside 24 academic entries that are indexable in principle. The arms converge on 219 tiered studies. A note records that the overlap between them is zero: none of the 40 database-included studies was already in the curated corpus, so the corpus's measured recall against a systematic search of its own subject was zero before this incorporation.

**Shows**:
- The two identification arms PRISMA 2020 provides, both used honestly: a systematic database search (395 screened, 40 topically included, 26 surviving appraisal) and the curated grey-literature corpus (195 entries, 171 of them grey) that a database search structurally cannot reach
- The exclusion profile, which is the substantive finding: the security-plus-data-architecture query is dominated by machine-learning detection-model papers (E1, n=103) and by pure data-engineering work (E2, n=137)
- A second exclusion profile the appraisal produced, and a harder one to report: 14 of the 40 topically-included studies were not fit to cite, and eight of those sat in predatory or compromised venues. A fifth of what a systematic database search returns at this intersection cannot be used
- The zero overlap between the two arms, and with it the corpus's measured recall against the systematic search — zero of 40 before this edition incorporated them
- That the search was run *after* the corpus was curated, disclosed as a retro-run rather than presented as a prospective protocol (methods/PRISMA-RETRO-RUN-2026-07-13.md)

### Figure 2: Evidence Level Distribution

![Figure 2: Evidence level distribution, per-source tally derived 2026-07-13 — 42.9% Level A (94/219 tiered), 46.6% Level B (102/219), 10.5% Level C (23/219); below the >70% Level A target, stated honestly in place of the withdrawn 79% self-grade.](publication-graphics/figure2_evidence_distribution.png){ width=85% }

Alt text: Bar chart of the evidence-level distribution across the 219 tiered sources as derived on 2026-07-13: Level A 42.9% (94 sources), Level B 46.6% (102 sources), Level C 10.5% (23 sources). A reference line marks the greater-than-70-percent Level-A target, and the chart annotates the shortfall against it — the honest derived figure stated in place of the 79% self-grade withdrawn in the 2026-06 audit.

**Shows**:
- Bar chart of the tier mix (A: 42.9%, B: 46.6%, C: 10.5% of 219 tiered entries; derived from MASTER-BIBLIOGRAPHY.md by `scripts/count_reconcile.py` on 2026-07-13, not self-graded)
- The >70% Level-A target line with the honest gap annotated
- The mix is essentially unchanged by the systematic-search incorporation of 2026-07-13, which added 11 Level-A studies against 15 at Level B or C. Adding peer-reviewed work to this corpus did not raise its Level-A share, because Level A in this scheme also admits production case studies and standards, and because half of what survived venue appraisal is conference-grade rather than journal-grade.

### Figure 3: Source Type Taxonomy

![Figure 3: Source-type taxonomy of the 221-entry corpus, derived per entry rather than estimated — peer-reviewed academic 50 (22.6%), vendor blogs and product documentation 63 (28.5%), open-source project documentation 33 (14.9%), practitioner talks and personal blogs 18 (8.1%), standards and government 17 (7.7%), big-tech engineering blogs 14 (6.3%), analyst and industry reports 12 (5.4%), books 8 (3.6%), and expert interviews, first-party lab measurements and documented no-primary stubs at 2 each.](publication-graphics/figure3_source_taxonomy.png){ width=85% }

Alt text: Horizontal bar chart of the source-type taxonomy across the 221 catalogued entries, ordered largest to smallest: vendor blogs and product documentation 63 sources (28.5%), peer-reviewed academic 50 (22.6%), open-source project documentation 33 (14.9%), practitioner talks and personal blogs 18 (8.1%), standards and government publications 17 (7.7%), big-tech engineering blogs 14 (6.3%), analyst and industry reports 12 (5.4%), books 8 (3.6%), and expert interviews, first-party lab measurements, and documented no-primary stubs at 2 sources each. Peer-reviewed work is drawn in a distinct colour and vendor-authored categories in another, because the contrast between them is the point of the chart.

**Shows**:
- Vendor-authored material (vendor blogs and product docs, plus big-tech engineering blogs) is 77 of 221 entries (34.8%) — the single largest bloc, and larger than the peer-reviewed literature
- Peer-reviewed academic work is 50 of 221 (22.6%), up from 24 of 195 (12.3%) before the 2026-07-13 systematic-search incorporation, which roughly doubled it
- Every count is derived per entry by `scripts/derive_source_taxonomy.py` and reconciled against the bibliography's block count, so a source added without a classification fails the build rather than silently vanishing from the chart. The previous version of this figure was hand-maintained, summed to 74, and described a corpus that had not existed since October 2025.

### Figure 4: Hypothesis Validation Confidence Levels

![Figure 4: Hypothesis validation confidence levels for all 9 hypotheses under the 2026-07-13 rubric rescore — 1 strongly validated (H-ARCH-01, 23/25), 2 high confidence (H3-PERFORMANCE-01 19/25, H-LOGCOMP-01 17/25 †), 2 moderate (H-STREAM-01 15/25, H-SOC-BASELINE-01 13/25 †), 4 preliminary (H-COST-09 9/25, H-IMPL-01 5/25, H-IMPL-02 5/25, H-IMPL-03 5/25). † = post-audit additions, 2026-07-10.](publication-graphics/figure4_hypothesis_confidence.png){ width=85% }

Alt text: Horizontal bar chart of confidence scores on the 25-point rubric for all 9 assessed hypotheses under the 2026-07-13 rescore, ordered strongest to weakest: H-ARCH-01 (Iceberg dominance) 23/25, strongly validated; H3-PERFORMANCE-01 (ClickHouse OLAP) 19/25 and H-LOGCOMP-01 (machine-data-specialized compression) 17/25, both high confidence; H-STREAM-01 (stateful streaming) 15/25 and H-SOC-BASELINE-01 (production SOC alert base rates) 13/25, both moderate; and H-COST-09 (tiered-storage savings) 9/25 with H-IMPL-01 (streaming TCO premium), H-IMPL-02 (staffing premium), and H-IMPL-03 (timeline premium) tied at the 5/25 instrument floor, all preliminary. Threshold lines mark the rubric's band boundaries at 21, 16, and 11 points. H-LOGCOMP-01 and H-SOC-BASELINE-01 are marked as the two hypotheses added post-audit on 2026-07-10.

**Shows**:
- Bar chart of 9 hypotheses with rescored confidence scores (23/25 down to the 5/25 floor)
- Grouped by validation strength (1 Strongly Validated, 2 High, 2 Moderate, 4 Preliminary), with band thresholds drawn at the rubric's 21/16/11 boundaries
- Rubric example (H-ARCH-01, strongest) and the honest audit summary

---

## TABLES

### Table 1: Source Quality Metrics

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Total Sources | 100+ | 221 catalogued (219 tiered; live-derived 2026-07-13) | ✅ Met |
| Peer-reviewed share | (none set) | 22.6% (50/221; was 12.3% before the 2026-07-13 search incorporation) | Reported, not targeted |
| Evidence Level A | >70% | 42.9% (94/219 tiered; live-derived 2026-07-13) | ❌ Below target (honest live figure; was a withdrawn 79% self-grade) |
| URL Validation (hypothesis-critical citations) | 90%+ | 100% (16/16 critical); 73% overall | ✅ Met (critical scope) |
| Geographic Diversity | 2+ regions | 3 regions (US, EU, APAC) | ✅ Met |
| Organizational Types | 3+ types | 5 types | ✅ Exceeded |

### Table 2: Hypothesis Validation Summary

| Hypothesis ID | Description | Confidence (post-audit) | Dimension split | Pre-audit | Key Validation |
|--------------|-------------|------------------------|-----------------|-----------|----------------|
| H-ARCH-01 | Iceberg Dominance | ⭐⭐⭐⭐⭐ 23/25 | 5/5/5/3/5 | 23/25 | Industry consensus; all legs primary-verified |
| H3-PERFORMANCE-01 | ClickHouse OLAP | ⭐⭐⭐⭐ 19/25 | 5/3/3/5/3 | 21/25 | Cloudflare verbatim-verified; 4 legs, 3 at Level A |
| H-LOGCOMP-01 † | Machine-data-specialized compression | ⭐⭐⭐⭐ 17/25 | 3/5/1/5/3 | — | LogLite + PBC + Pebbles, verbatim-verified at primary; two independent author groups |
| H-STREAM-01 | Stateful streaming | ⭐⭐⭐ 15/25 | 1/5/3/3/3 | 17/25 | Samza VLDB 2017 + Azure verbatim-verified; two legs cap the source count |
| H-SOC-BASELINE-01 † | Production SOC alert base rates | ⭐⭐⭐ 13/25 | 1/5/1/5/1 | — | Yang USENIX Sec '24, verbatim-verified; single-source cap |
| H-COST-09 | Tiered Storage savings | ⭐⭐ 9/25 | 1/1/1/3/3 | 19/25 | Savings band withdrawn 2026-06; first-party S3 tier-delta bound; directional |
| H-IMPL-01 | Streaming TCO premium | ⭐⭐ 5/25 | 1/1/1/1/1 | 22/25 | DORA + TEI legs withdrawn; no scoreable leg, instrument floor |
| H-IMPL-02 | Staffing premium | ⭐⭐ 5/25 | 1/1/1/1/1 | 23/25 | DORA attribution fabricated (withdrawn 2026-07); no scoreable leg, instrument floor |
| H-IMPL-03 | Timeline premium | ⭐⭐ 5/25 | 1/1/1/1/1 | 13/25 | Timeline figures withdrawn 2026-06/07; no scoreable leg, instrument floor |

*Dimension split reads source count / evidence quality / source diversity / quantitative precision / geographic-organizational diversity, each 1-5, per `methods/scoring-rubric.md` (the instrument of record; bands 21-25 Strongly Validated, 16-20 High, 11-15 Moderate, 5-10 Preliminary). Confidence scores were recomputed 2026-07-13 under that rubric (`methods/RESCORE-2026-07-13.md`), superseding the 2026-07-09 adopted values where they differ; ties order alphabetically by hypothesis ID. † Formulated post-audit 2026-07-10 from peer-reviewed primaries catalogued by the DR-3 intake (NEW-HYPOTHESES-PROPOSAL-2026-07.md); no pre-audit score exists. Preliminary rows lost the citations behind their quantitative multipliers (fabricated attribution or figures absent from cited sources) and are directional pending re-sourcing; the three H-IMPL rows tie at the instrument's 5/25 floor because no scoreable leg survives, and their former 6/7/7 gradation is retired as judgment the instrument cannot express.*

### Table 3: Cost Comparison Findings

| Architecture | Operational Cost Premium | Staffing Multiplier | Timeline | Sources |
|-------------|-------------------------|-------------------|----------|---------|
| Batch (Baseline) | 1.0× | 1.0× | — | Baseline (definitional) |
| Streaming | Elevated (under re-validation) | Elevated (under re-validation) | — | Citations withdrawn 2026-06 |
| Tiered Storage Optimization | Reduced (under re-validation) | N/A | N/A | Citations withdrawn 2026-06 |

*2026-06 source audit: the quantitative multipliers previously shown here rested on withdrawn citations and are removed pending re-sourcing.*

### Table 4: Performance Benchmarks (Security Workloads)

| Platform | Query Performance | Ingestion Rate | Storage Efficiency | Production Validation |
|---------|------------------|----------------|-------------------|---------------------|
| ClickHouse | — (figure withdrawn 2026-06) | N/A | 12-19× vs Elasticsearch (vendor benchmark; 9-12× with `_source` disabled) | Cloudflare (6M req/sec) |
| Kafka | N/A | — (figure withdrawn 2026-06) | N/A | Microsoft (trillions/day) |
| Iceberg | — (figure withdrawn 2026-06) | N/A | N/A | SK Telecom (production Iceberg + Trino) |

### Table 5: Evidence Gaps Identified

| Gap Area | Current Evidence | Gap Description | Future Research Needed |
|---------|-----------------|-----------------|----------------------|
| Mid-market volumes | Large-scale only | Validated at TB-PB scale, not mid-market | Mid-sized org quantification |
| Direct SIEM pricing | Storage optimization proxy | Cost comparisons indirect | Head-to-head SIEM vs lakehouse |
| DuckDB edge processing | Emerging, no production | H-EDGE-01 lacks validation | Production deployment data |
| XTable interoperability | Vendor claims only | Cross-format maturity unclear | Production use cases |
| Catalog adoption | Anecdotal | Gravitino adoption unknown | Quantitative adoption metrics |
| Security benchmarks | General analytics proxy; **first-party MOAR reference stack now provides one identical-workload, answer-equality-gated comparison** (4 engines, one Iceberg/OCSF table, 2026-06-07) | TPC-like security benchmarks missing; first-party answer is single-host only (no multi-node / concurrency / TCO) | Standardized multi-node, concurrency-aware security benchmark suite |

---

## APPENDICES

### Appendix A: Evidence Classification Rubric (Detailed)

*Drafted 2026-07-09.* This appendix expands Section 2.3's evidence-quality assessment, documenting the four-tier classification rubric applied to every source in the corpus, the inclusion and exclusion criteria that drove each tier assignment, and the post-audit state of the tier mix as it stands after the 2026-06 fabrication withdrawal and the 2026-07 verification sweep.

**The four tiers.** The rubric adapts evidence-based medicine classification to computer science and cybersecurity source material, ranking sources by how directly their claims can be checked against a named, reproducible origin.

Level A (high-quality evidence) covers production-validated deployments with quantitative metrics and a named organization (for example, Huntress's more-than-90-percent infrastructure cost reduction after a ClickHouse migration, or Cloudflare's 6 million requests/second figure), peer-reviewed academic research with a formal review process, and government or standards-body publications (CISA, MITRE, DARPA, NSA, SANS, Apache Software Foundation) offering authoritative technical guidance. Quality indicators at this tier include quantitative metrics on throughput, cost, timeline, or staffing; production-scale validation in the terabyte-to-petabyte range; named rather than anonymous organizations; and a methodology that in principle permits independent verification.

Level B (moderate-quality evidence) covers industry analyst reports (Gartner, IDC, Forrester) with quantitative survey data, expert-validation interviews from recognized practitioners, vendor technical documentation that carries production validation rather than marketing framing, and comprehensive industry surveys with sample sizes above roughly 50 organizations. The rubric explicitly allows vendor-sponsored material into this tier when it is methodologically rigorous and technically substantive rather than promotional; the dividing line is whether the vendor's documentation demonstrates production validation and technical depth, or reads as marketing copy without it, in which case it is excluded rather than downgraded.

Levels C (limited evidence) and D (unreliable evidence) were designed as exclusion tiers — defined at zero percent of the corpus, with sources assigned to them dropped rather than cited with caveats. Design and practice have drifted here, and the drift is reported rather than hidden: the live corpus holds 16 provisionally-retained Level C entries (9.0 percent of the tiered corpus), each carrying a bias flag, and the next curation pass must either re-tier or purge them to restore the design intent.

**Vendor bias handling.** Because a meaningful share of the corpus is vendor-authored or vendor-commissioned technical documentation, classification does not treat vendor authorship as automatically disqualifying, nor as automatically Level A. A vendor source earns Level B only where it shows production validation and technical depth beyond promotional claims. The tier boundary is the mechanism by which vendor incentive is handled, and that boundary is where the 2026 audits found the most drift.

**Classification process.** Sources move through four steps: initial assessment (source type, URL, publication metadata), quality evaluation (quantitative evidence present, production validation, reproducibility, methodological transparency), evidence-level assignment against the criteria above, and cross-validation, where corroboration from an independent source type is preferred for any claim feeding hypothesis validation.

**Post-audit state of the tier mix.** The original classification pass assigned a large majority of sources to Level A, targeting a greater-than-70-percent Level-A share. The 2026-06 fabrication audit and the 2026-07 verification sweep re-checked surviving inline figures against their cited sources and found that a substantial share of the originally Level-A entries carried statistics not actually present in the source, or had entries removed outright. The live, derived tally as of 2026-07-13 is 94 of 219 tiered entries at Level A (42.9 percent), 102 at Level B (46.6 percent), and 23 at Level C (10.5 percent) — below the target, and reported here honestly in place of the withdrawn 79 percent self-graded figure (see Table 1). Per-source evidence levels remain provisional pending further re-verification.

The systematic-search incorporation of 2026-07-13 is worth reading against that target rather than as progress toward it. It added 26 peer-reviewed studies, which nearly doubled the corpus's peer-reviewed share, and it moved the Level-A percentage by one tenth of a point in the wrong direction (43.0 to 42.9). Only 11 of the 26 tier at Level A: the rest are conference work whose review depth could not be independently established, or papers in venues too weak to carry a Level-A claim. The lesson is not that the search failed — it is that Level A in this scheme is a demanding grade that most of the indexed literature at this intersection does not meet, and that a corpus cannot be raised to a 70-percent Level-A share by adding peer-reviewed papers unless the papers are good ones.

**What tier constrains.** A source's tier gates what kind of claim it can carry. A quantitative claim feeding hypothesis validation should be backed by at least one Level A source, with Level B treated as corroborating rather than sufficient on its own; the post-audit re-score reflects this constraint directly, grading one hypothesis strongly validated, two at high confidence, two moderate, and four preliminary, in each case because the surviving Level A support narrowed after the audits. A Level B source alone may support a qualified or contextual claim but not a headline quantitative one. Level C and D sources support no claim in the published text.

### Appendix B: Hypothesis Confidence Scoring Methodology

*Drafted 2026-07-09; instrument made explicit 2026-07-12 and re-run 2026-07-13.* This appendix documents the scoring instrument used throughout the manuscript to grade hypothesis validation strength. The instrument of record is now `methods/scoring-rubric.md`, which consolidates the source rubric (`analysis-bundles/hypothesis-confidence-matrix.md`) and makes explicit the arbitration rules that previously lived nowhere — anchor-only dimension values, what counts as a scoreable leg, and how first-party measurements and shared author collaborations are treated; §2.5 carries the band table. The instrument scores each hypothesis on five dimensions, five points each, for a total of 5-25 points, and it exists so that a confidence label like "strong" or "preliminary" traces back to a reproducible calculation rather than an author's impression.

**The five dimensions.** Each dimension is scored independently: *source count* (1-2 sources score 1 point, 3 sources score 3, 4 or more score 5 — no extra credit past 6, since redundant sources add no independent confirmation); *evidence-level quality* (scored by the share of cited sources at Evidence Level A, from 1 point at 0-25% up to 5 points at 100%); *source diversity* (1 point for a single source type, 3 for two types, 5 for three or more, across government, industry-analyst, production-deployment, academic, and vendor types); *quantitative precision* (1 point for a directional claim, 3 for a range estimate, 5 for a precise figure); and *geographic/organizational diversity* (1 point for a single org or region, 3 for two to three, 5 for four or more with international spread).

**Star-tier thresholds.** The five dimensions sum to a 5-25 total mapped to the star scale: 5-10 Preliminary, 11-15 Moderate, 16-20 High Confidence, 21-25 Strongly Validated. One band table now governs every surface (§2.5, §3.7, Table 2, and Figure 4's threshold lines, drawn at 21/16/11). The earlier five-level prose scale in §2.5 (Strongly Validated, Strong, Validated, Preliminary, Unvalidated) conflicted with these point bands and is retired: the instrument's floor is 5, which lands inside Preliminary, so the legacy Unvalidated tier is unreachable by score and survives only as a categorical label for a claim with no supporting evidence of any kind, which no current hypothesis matches.

**The 2026-07 re-score rule.** The 2026-06 audit withdrew citations found fabricated or mismatched to their sources, and the 2026-07 verification sweep re-verified every surviving inline figure. RESCORE-PROPOSAL-2026-07.md formalizes how the rubric absorbs that history: a hypothesis scores only on evidence that has survived primary-source verification or has not yet been challenged; a withdrawn leg scores zero, and a leg flagged fabricated-or-dead by a prior audit also scores zero until independently re-verified. This is why several hypotheses dropped sharply even though their underlying claims did not change — H-IMPL-01 fell from 22/25 to the instrument's 5/25 floor because its DORA and TEI legs did not survive verification, and H-COST-09 fell from 19/25 to 9/25 once its savings band was withdrawn and its access-pattern split relabeled illustrative (the 9 rather than the floor reflects the first-party S3 tier-delta derivation, which bounds the achievable saving without measuring a realized one). Both retain their practitioner reasoning in the text as unquantified direction.

**Worked example: H-ARCH-01 post-audit (23/25).** The instrument decomposes H-ARCH-01 as 5/5/5/3/5: 5 for source count (four distinct measurements — the SK Telecom production deployment, the vendor-support roundup, the Apache Software Foundation contributor base, and the Dremio survey — which reaches the 4-or-more anchor), 5 for evidence quality (all four legs Level A), 5 for source diversity (production deployment, vendor, standards body, and industry-survey types), 3 for quantitative precision, and 5 for geographic/organizational diversity (SK Telecom in South Korea alongside the ASF's international contributor base and US and global vendors). Precision stays at 3 under the explicit rubric rather than rising: the claim variable is dominance share, whose only precise quantification was the withdrawn 76%, and the surviving precise figures (29%-vs-23% planning intent, 407 contributors) quantify adoption momentum and community size instead, which the rubric scores as precise figures for an adjacent indicator. The decomposition reproduced unchanged when the instrument was re-run on 2026-07-13, so the score is stable under the explicit rules. H-ARCH-01 is the manuscript's only hypothesis holding the Strongly Validated tier post-audit.

**Re-computation as evidence changes.** The rubric is not scored once and left static. A hypothesis's score is recomputed whenever an audit changes its available evidence — a citation withdrawn, a figure re-verified, or a new primary replacing an orphaned one. H-STREAM-01 is the clearest case: the 2026-07 sweep re-anchored its stateful-processing claim on the peer-reviewed Samza VLDB 2017 paper, which improved the composition without changing the total, and then the 2026-07-13 rescore moved it from 17/25 to 15/25 and out of the High band, because with the Uber leg withdrawn the section cites two sources and the source-count anchor prices 1-2 sources at 1 point. The demotion is forced by the instrument rather than by any new doubt about the surviving legs, and one further verified, catalogued leg restores the hypothesis to 17/25. That is the standing precedent: future audits that change a hypothesis's evidentiary basis trigger the same dimension-by-dimension recomputation, not an ad hoc star adjustment.

### Appendix C: Expert Validation Protocol

*Drafted 2026-07-09 from the prepared interview guides; the protocol below documents intended method and evidence-tiering rules, not a completed interview round.*

**Purpose and status.** The literature review supplements desk research with a small expert-interview program designed to validate specific hypotheses that quantitative literature alone could not settle. As of this writing, that program consists of two prepared interview guides — for Jake Thomas (Okta) and Lisa Cao (Datastrato, the Gravitino project) — plus one anonymized practitioner whose validation is already recorded in the bibliography. The bibliography marks the Jake Thomas interview as validation-in-progress rather than complete.

**The expert network.** Jake Thomas is targeted for production defensive-cyber-operations experience with DuckDB at scale: his guide sets out to validate H-EDGE-01 (DuckDB for edge and embedded security analytics) and H1-VOLUME-07 (security data volumes at mid-sized enterprises), and to gather production architecture detail the review could not source independently. Lisa Cao is targeted for catalog-landscape expertise — Gravitino adoption patterns, positioning against Polaris, Unity Catalog, and Nessie, and Apache XTable production maturity — with her guide proposing to formalize a new hypothesis (H-ARCH-03) on catalog adoption. The project brief names a data-platform practitioner and Paul Agbabian as follow-on contacts, and records one completed interview with an anonymized practitioner validating query-engine viability for security operations (Starburst and Athena patterns).

**Interview structure.** Both guides follow the same shape: primary and secondary objectives tied to named hypotheses, a pre-interview summary of what the review already knows and where the gaps sit, a sequence of timed question sections (roughly 75-80 minutes per guide), and a closing section that puts the specific hypothesis language in front of the expert and asks directly whether it matches their experience and what they would change. The Thomas guide runs seven sections (production deployment, performance and scalability, edge-processing patterns, data-volume economics, implementation reality, comparison to alternatives, hypothesis validation); the Cao guide runs five (Gravitino adoption, catalog selection criteria, XTable interoperability, architecture patterns, future trends). Each closes with a recording-and-consent checklist (permission to record, attribution preference, publishable versus background) and a quote-approval step before any material moves into the manuscript.

**Recording and evidence tiering.** Both guides direct that interview material be transcribed within 24 hours, added to the master bibliography with the expert named as a source, and used to update the relevant hypothesis status. Expert testimony is logged as personal communication, not treated as a citable published source. The bibliography's grading practice distinguishes an expert speaking to their own production deployment (graded A as direct production evidence) from an expert validating or commenting on claims built from other sources (graded B).

**Limits of the protocol.** The guides are explicit that expert interviews validate direction and plausibility, not quantitative figures: interviewers are instructed to ask "can you quantify that?" and to record whether an answer reflects widespread confidence or a single deployment's anecdote. Neither guide substitutes for a benchmark or a published dataset; even a production-validated expert account should be read as corroborating a hypothesis's plausibility, not as replacing the quantitative evidence the hypothesis still needs.

### Appendix D: Source List by Theme

*Generated 2026-07-09, extended 2026-07-13 for the systematic-search incorporation. The 38 inline-cited references (see REFERENCES) grouped by review theme; the full evidence-tiered corpus behind each theme lives in MASTER-BIBLIOGRAPHY.md in this repository (221 entries, 219 of them tiered, as of 2026-07-13), organized under the same theme headings with per-entry evidence levels, key findings, and validation status.*

**Theme 1 — Foundational Architecture** (table formats, query engines, streaming): Apache Iceberg project + GitHub [2]; Dremio lakehouse survey [9]; SK Telecom Iceberg/Trino [18]; ClickHouse-vs-Elasticsearch benchmark [5]; ClickHouse IP types [6]; Samza VLDB 2017 [14]; Azure Kafka [12]; Uber real-time platform [19]; Arrow Flight SQL [1]

**Theme 2 — Cost Economics & TCO**: Forrester TEI Public Cloud [10]; Forrester TEI Private Cloud [11]; Confluent tiered storage [7]

**Theme 3 — Implementation Reality**: DORA 2024 [8] (audit-note citation only — see §3.4.1)

**Theme 4 — Performance Benchmarks**: Cloudflare HTTP analytics [3]; Cloudflare log analytics [17]; Netflix petabyte-scale logging [13]; SDW Lab first-party benchmarks [21]; MOAR reference architecture [20]; machine-data compression — Pebbles [22], Blitzcrank [23], LogLite [24], PBC [26]

**Theme 5 — Security-Specific Requirements**: CISA AA23-193A [4]; OMB M-21-31 [15]; SOC alert base rates, USENIX Security '24 [25]

**Methodology**: PRISMA 2020 statement [16]

**Systematic-search arm** (peer-reviewed, incorporated 2026-07-13; see §2.2 and the systematic-search arm in MASTER-BIBLIOGRAPHY.md): streaming detection pipelines — CATRACA [29], AIDA/SABU [33], Loganathan auto-scaling CEP [35], cloud Snort NIDS [37]; non-vendor production deployments — CERN [36], INFN-CNAF [28], Lawrence Berkeley/SPARCS [32]; engine and pipeline benchmarks — Kajiura & Nakamura pipeline-vs-model NIDS [34], Abbasi Faust-vs-Streamz [27], Yahyaoui Flink-vs-Spark Streaming [38]; storage and log-reduction — ClickHouse SIEM storage reduction [30] (Level C, venue caveat), Vector log-reduction [31]

---

## MANUSCRIPT METADATA

**Version**: 0.3 (content drafted; sources audited 2026-06 + 2026-07; references generated)
**Word count**: ~10,100 words of main text (abstract through Conclusion; excludes references, figures, tables, and appendices), within the 10,000-15,000 target for a Journal of Cybersecurity article; the full document runs ~14,060 words including references and appendices (measured 2026-07-11)
**Target venue**: Journal of Cybersecurity (Oxford, open access) — owner ruling 2026-07-10, replacing the Oct-2025 CSUR/IEEE plan; submission work gated post-2026-07-15
**Submission target**: post-2026-07-15 window at Journal of Cybersecurity (owner ruling 2026-07-10)
**Status**: All sections drafted. 2026-06 audit withdrew fabricated multipliers; 2026-07 per-citation verification sweep applied (33-item fix pass) — every surviving inline figure is primary-verified. References + Appendix D generated 2026-07-09.

**Remaining before submission**:
1. ~~Confidence re-score~~ DONE 2026-07-09 (RESCORE-PROPOSAL-2026-07.md adopted; §2.5/§3.7/Tables 1-2/Figures 2+4 updated)
2. ~~Re-sourcing hunts for the directional claims (staffing/TCO/timeline multipliers)~~ DONE 2026-07-10 — the DR-1 Deep Research hunt returned zero Tier-A/B (two predatory-adjacent venues, one anonymous Medium; two C-tier leads catalogued in GEMINI-DR1-INTAKE-2026-07-10.md); the four PRELIMINARY scores stand. Only literature restoration route left: Gartner Market Guide seat-access check (H-IMPL-02)
3. Appendices A-C drafting; Acknowledgments
4. Expert review (Lisa Cao, Jake Thomas)
5. ~~Venue decision~~ RULED 2026-07-10 (Journal of Cybersecurity, open access; work post-7/15) + formatting pass
6. Promote new Tier-A-anchored hypotheses from the DR-3 intake (owner ruling 2026-07-10: keep the 7 with the honest split AND add; wording staged in NEW-HYPOTHESES-PROPOSAL-2026-07.md, gate pass before integration)

---

**Document maintained by**: Jeremy Wiley
**Created**: October 21, 2025
**Repository**: security-data-literature-review/PUBLICATION-MANUSCRIPT.md
