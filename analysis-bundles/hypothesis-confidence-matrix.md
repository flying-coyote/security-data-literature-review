---
type: evidence
title: "Hypothesis Validation Confidence Assessment Matrix"
created: 2025-10-15
tags: [hypothesis-validation, evidence-scoring, first-party-benchmarks, ocsf, clickhouse, iceberg]
---

# Hypothesis Validation Confidence Assessment

**Purpose**: Transparent confidence scoring for 7 borrowed-source hypotheses plus 6 first-party (lab-measured) hypotheses, with methodological rigor
**Target Use**: Book confidence statements, academic publication, honest claim evaluation
**Created**: October 15, 2025
**Updated**: June 14, 2026 (re-anchored H-OCSF-CONTEXT-COLLAPSE-01 on the de-gamed APT29 +0.188 and labelled the synthetic-testbed +0.719 as its gameable predecessor; folded in the flattening-fidelity mechanism-decomposition curves; added the H-CROSS-TOOL-ASSURANCE-01 data-health band annotation. June 7: added first-party MOAR reference-stack measurements; re-grounded two borrowed cells)
**Sources**: Borrowed-source citations reference MASTER-BIBLIOGRAPHY.md entries; first-party citations reference the SDW MOAR reference stack and the public lab benchmark repository
**Methodology**: Evidence-based confidence rubric (source count, evidence level, validation type)

> **Evidence-tier note**: The original 7 hypotheses are validated by *borrowed* third-party production numbers (Cloudflare, Shell, SK Telecom, Netflix and the like), which top out at Evidence Level A as reported-by-the-operator. The 6 hypotheses added in the June 2026 revision are backed by *first-party lab measurements* taken on the SDW MOAR reference stack (the "Modular Open Architecture" stack), which is a distinct and, for the specific claim measured, higher tier: the workload, the data, the engines and the comparison are ours, the run is reproducible, and an answer-equality gate is applied before any latency or storage number is read. Where a first-party measurement and a borrowed production number speak to the same claim, both legs are kept and labeled, because each answers a different question — the borrowed number says it holds at production scale on someone else's workload, the first-party number says we ran an identical-workload comparison ourselves and can show the apparatus. The first-party legs carry an explicit single-host scope limit (Ryzen 5800H, WSL2); H-ARCH-02 now includes a single-host concurrency sweep (C1→C16), but the legs still do not claim datacenter scale, multi-node cluster concurrency, or TCO.

---

## Executive Summary

**All 7 hypotheses are validated**, but with **varying confidence levels**:

| Hypothesis | Confidence | Source Count | Evidence Level A % | Key Validation |
|------------|-----------|--------------|-------------------|----------------|
| **H-ARCH-01** (Iceberg) | ⭐⭐⭐⭐⭐ Strong | 5 (+1 first-party) | 100% | Industry consensus, universal vendor support; FIRST-PARTY answer-equality on one Iceberg/OCSF table |
| **H-IMPL-01** (TCO) | ⭐⭐⭐⭐ High | 5 | 80% | IDC, DORA, Confluent convergence |
| **H-IMPL-02** (Staffing) | ⭐⭐⭐⭐⭐ Strong | 4 | 100% | DORA 2.7×, IDC 2.5-3×, Ververica 3.2 FTEs |
| **H-IMPL-03** (Timeline) | ⭐⭐⭐ Moderate | 3 | 67% | Gartner 5.5 months, SANS premium validated |
| **H-COST-09** (Tiered Storage) | ⭐⭐⭐⭐⭐ Strong | 3 | 100% | AWS 55%, Netflix 70-80%, production validated |
| **H3-PERFORMANCE-01** (ClickHouse) | ⭐⭐⭐⭐ High | 4 (+1 first-party) | 100% | Cloudflare 6M req/sec, Shell 57TB/day; FIRST-PARTY ~7.0× storage on OCSF data (FOIL) |
| **H-STREAM-01** (Kafka Streams) | ⭐⭐⭐⭐ High | 3 | 100% | LinkedIn, Uber production security |

**FIRST-PARTY hypotheses (lab-measured, MOAR reference stack, 2026-06-07, single host):**

| Hypothesis | Confidence | Source Count | Evidence Tier | Key Measurement |
|------------|-----------|--------------|---------------|-----------------|
| **H-ENGINE-ANSWER-EQUIVALENCE-01** (four engines, one table) | ⭐⭐⭐⭐ High | 1 (first-party, multi-engine) | First-party lab | DuckDB, Trino, ClickHouse, StarRocks agree on count / needle / group-by over one Iceberg/OCSF table |
| **H-ARCH-02** (no single engine wins) | ⭐⭐⭐⭐ High | 1 (first-party, 4 engines, 1M→100M + C1→C16 sweep) | First-party lab | Both axes measured: at 100M the workload-shape crossover appears (ClickHouse wins full-scan count, DuckDB wins needle + group-by; DuckDB had swept at 1M/10M), and the concurrency sweep splits them again — DuckDB fastest at C1 but flat ~46 q/s, ClickHouse scales 20→58 q/s and overtakes by C16 |
| **H-OCSF-CONTEXT-COLLAPSE-01** (flattening fidelity) | ⭐⭐⭐⭐ High | 2 (published lab artifacts: de-gamed APT29 + mechanism decomposition) | First-party lab (public) | De-gamed APT29 adversary-vs-routine recall-loss delta **+0.188** (sweep range +0.094 to +0.205) on unmodified SigmaHQ rules; the synthetic-testbed BENCH-A +0.719 is the gameable lab-authored predecessor it supersedes |
| **H-SEC-CATALOG-01** (catalog portability) | ⭐⭐⭐ Moderate | 1 (first-party, 5 open catalogs) | First-party lab | swap-catalog across REST/Polaris/Nessie/Lakekeeper/Gravitino; Unity Catalog leg NOT reproducible |
| **H-DUCKLAKE-02** (swap-format read-neutral + commit-tax) | ⭐⭐⭐⭐ High | 1 (first-party, two legs: identical bytes + streaming commits) | First-party lab | Iceberg↔DuckLake read-neutral on byte-identical data; under a 100-commit stream Iceberg ingest ~37×, metadata footprint ~515×, planning ~21×, while DuckLake planning stays flat (~7 ms) — the write-contract complement to read-neutrality |
| **H-NDR-FEDERATION-01** (cross-source correlation) | ⭐⭐⭐⭐ High | 1 (first-party, 2-source join) | First-party lab | Join surfaces attacker 198.51.100.66 (lateral movement) no single source reveals |

**Key Insight**: **Hypothesis validation strength correlates with source diversity** (government + industry + production), not just source count. H-IMPL-02 (staffing) has **strongest validation** despite only 4 sources because: DORA (industry research) + IDC (analyst) + Ververica (production) + McKinsey (consulting) represent **4 independent validation types**. The first-party hypotheses score differently: a single source, but a source we control end-to-end, so the discriminating dimensions are reproducibility and the answer-equality gate rather than independent-source count. A first-party run cannot manufacture source diversity, and we do not pretend it does; its claim is narrower and better-controlled, which is why several of these sit at High rather than Strong despite being measured rather than borrowed.

---

## Confidence Rubric

### Scoring Dimensions

**1. Source Count** (1-5 points):
- 1-2 sources: 1 point (weak)
- 3 sources: 3 points (moderate)
- 4-5 sources: 5 points (strong)
- 6+ sources: 5 points (strong, no extra credit for redundancy)

**2. Evidence Level Quality** (1-5 points):
- 0-25% Level A: 1 point (weak)
- 26-50% Level A: 2 points (moderate-low)
- 51-75% Level A: 3 points (moderate)
- 76-99% Level A: 4 points (high)
- 100% Level A: 5 points (exceptional)

**3. Source Diversity** (1-5 points):
- 1 source type (e.g., all vendor): 1 point (weak)
- 2 source types: 3 points (moderate)
- 3+ source types: 5 points (strong)
- Source types: Government, Industry Analyst, Production Deployment, Academic, Vendor

**4. Quantitative Precision** (1-5 points):
- Directional claim only ("costs more"): 1 point
- Range estimate ("2-4× more"): 3 points
- Precise quantification ("2.7× more"): 5 points

**5. Geographic/Organizational Diversity** (1-5 points):
- Single org/region: 1 point
- 2-3 orgs/regions: 3 points
- 4+ orgs/regions, international: 5 points

**Total Confidence Score**: 5-25 points
- 5-10: Weak (1⭐)
- 11-15: Moderate (3⭐)
- 16-20: High (4⭐)
- 21-25: Strong (5⭐)

---

## Hypothesis-by-Hypothesis Assessment

### H-ARCH-01: Apache Iceberg Dominance

**Hypothesis**: "Apache Iceberg has emerged as the de facto standard for open table formats in enterprise data lakehouses, with 76% adoption among organizations standardizing on open formats."

**Validation Status**: ✅ **STRONGLY VALIDATED** (with refinement)

---

#### Confidence Scoring

**Source Count**: 5 points (5 borrowed sources) + 1 first-party leg
- SK Telecom production deployment
- Apache Iceberg Foundation (300+ contributors, 100+ orgs)
- Universal vendor support (AWS, Google, Snowflake, Databricks, Microsoft)
- Cloudera production validation
- Dremio 2024 survey (29% planning Iceberg vs 23% Delta)
- **FIRST-PARTY (lab-measured, 2026-06-07, MOAR reference stack, single host)**: an Iceberg/OCSF table is read by four independent engines (DuckDB, Trino, ClickHouse, StarRocks) that all agree on count / needle / group-by, and the same logical data round-trips Iceberg↔DuckLake read-neutral on byte-identical files — direct evidence that Iceberg functions as a vendor-neutral, engine-portable table format, not merely that vendors announced support. This is the answer-equality + swap-format leg the borrowed sources cannot supply; it is a distinct evidence tier (we ran it) and is reported alongside, not in place of, the borrowed production validation.

**Evidence Level Quality**: 5 points (100% Level A)
- All 5 sources = Level A (production deployments, official ASF metrics, vendor announcements)

**Source Diversity**: 5 points (4 source types)
- Production Deployment: SK Telecom, Cloudera
- Standards Body: Apache Software Foundation
- Vendor: Universal vendor commitments
- Industry Survey: Dremio 2024

**Quantitative Precision**: 3 points (range estimate, not precise)
- Original claim: "76% adoption" (specific, but **source not found**)
- Refined claim: "Industry consensus as de facto standard" + "29% planning Iceberg vs 23% Delta" (Dremio)
- Loss of precision from 76% → "industry consensus"

**Geographic/Organizational Diversity**: 5 points (international)
- SK Telecom (South Korea)
- Cloudera (US)
- AWS, Google, Snowflake, Databricks, Microsoft (global)
- Apache Software Foundation (300+ contributors, 100+ orgs worldwide)

**Total Confidence**: **23/25 points** = ⭐⭐⭐⭐⭐ **STRONG**

---

#### Confidence Drivers

✅ **Universal vendor support**: AWS, Google, Snowflake, Databricks, Microsoft all announced Iceberg compatibility
✅ **Apache Software Foundation governance**: Open, vendor-neutral governance (vs Delta = Databricks-led)
✅ **Production validation at scale**: SK Telecom (52.7 TB in 3.39s), Cloudera (10× vs Hive)
✅ **Community strength**: 300+ contributors across 100+ organizations
✅ **FIRST-PARTY engine portability (lab-measured, 2026-06-07)**: four engines return identical answers over one Iceberg/OCSF table, and the data swaps Iceberg↔DuckLake read-neutral on identical bytes — we verified the format's vendor-neutrality ourselves rather than inferring it from vendor announcements (single-host apparatus; see H-ENGINE-ANSWER-EQUIVALENCE-01 and H-DUCKLAKE-02)

---

#### Confidence Limiters

⚠️ **"76%" statistic not located**: Web searches found Dremio survey (29% vs 23%), but not specific "76%" claim
⚠️ **Refinement required**: Recommend changing claim from "76% adoption" to "industry consensus as de facto standard, with universal vendor support and growing momentum (Dremio: 29% planning Iceberg vs 23% Delta)"

---

#### Recommended Book Language

**Strong Confidence Statement**:
> "Apache Iceberg has emerged as the industry consensus choice for open table formats, with universal support from all major cloud providers (AWS, Google, Microsoft) and data platforms (Snowflake, Databricks). The Apache Software Foundation governance model—with 300+ contributors across 100+ organizations—provides vendor-neutral leadership that Delta Lake's Databricks-led model cannot match. Dremio's 2024 survey confirms growing momentum: 29% of organizations planning to adopt an open table format chose Iceberg vs 23% for Delta Lake."

**Citations**:
- Universal vendor support: MASTER-BIBLIOGRAPHY.md:1312-1332
- Apache Software Foundation governance: MASTER-BIBLIOGRAPHY.md:1337-1355
- Dremio 2024 survey: Web search results (October 15, 2025)
- SK Telecom production: MASTER-BIBLIOGRAPHY.md:49-69

---

### H-IMPL-01: Streaming Hidden Costs (TCO Reality)

**Hypothesis**: "Streaming architectures incur 2.5-3× higher operational costs vs batch processing due to specialized expertise, 24/7 monitoring, and incident management complexity."

**Validation Status**: ✅ **HIGH CONFIDENCE**

---

#### Confidence Scoring

**Source Count**: 5 points (5 sources)
- IDC Research (2.5-3× operational staffing)
- DORA 2024 Report (2.7× staff, 3.2× incidents)
- Enterprise Data Quarterly (1.5-2× infrastructure)
- Confluent (45-55% ops complexity)
- Cloudera TCO (39% licensing, 32% hardware, 29% operational)

**Evidence Level Quality**: 4 points (80% Level A)
- Level A: IDC, DORA, Cloudera (3 of 5)
- Level B: Enterprise Data Quarterly, Confluent (2 of 5)

**Source Diversity**: 5 points (4 source types)
- Industry Analyst: IDC
- Industry Research: DORA
- Production Data: Confluent (thousands of deployments)
- Commissioned Research: Cloudera/Forrester TEI

**Quantitative Precision**: 5 points (precise convergence)
- IDC: 2.5-3× operational staffing
- DORA: 2.7× operational staff
- Enterprise Data Quarterly: 1.5-2× infrastructure
- Confluent: 45-55% ops complexity
- **Convergence**: Multiple independent sources all cite **2-3× range**

**Geographic/Organizational Diversity**: 3 points (US-centric)
- IDC (US-based research)
- DORA (global survey, but US-heavy)
- Confluent (US vendor, global customers)
- Cloudera (US vendor)

**Total Confidence**: **22/25 points** = ⭐⭐⭐⭐ **HIGH**

---

#### Confidence Drivers

✅ **Independent source convergence**: IDC (2.5-3×), DORA (2.7×), Confluent (45-55%) all validate 2-3× range
✅ **Mixed source types**: Industry analyst + industry research + vendor production data
✅ **Quantitative precision**: Not directional ("costs more"), but precise multipliers
✅ **Operational vs infrastructure split**: Multiple sources differentiate staffing (2.5-3×) from infrastructure (1.5-2×)

---

#### Confidence Limiters

⚠️ **US-centric sources**: European/APAC validation limited (cost differentials may vary by region)
⚠️ **Enterprise-focused**: Mid-market (50-200 TB) validation less comprehensive

---

#### Recommended Book Language

**High Confidence Statement**:
> "Streaming architectures incur 2.5-3× higher operational costs vs batch processing, validated by independent sources: IDC research (2.5-3× operational staffing), DORA 2024 (2.7× staff, 3.2× incident rates), and Confluent production data (45-55% of TCO from operational complexity). The premium stems from specialized expertise requirements (fault-tolerance = 'Level 4' skill per DORA, available in top 5% of organizations only), 24/7 monitoring demands, and incident management complexity."

**Citations**:
- IDC: MASTER-BIBLIOGRAPHY.md:569-586
- DORA: MASTER-BIBLIOGRAPHY.md:357-376
- Confluent: MASTER-BIBLIOGRAPHY.md:1056-1076

---

### H-IMPL-02: Staffing Scarcity (Specialized Skills)

**Hypothesis**: "Organizations implementing streaming architectures require 2.7× operational staff vs batch alternatives, with fault-tolerance expertise representing 'Level 4' specialized skills available in only the top 5% of organizations."

**Validation Status**: ✅ **STRONGLY VALIDATED**

---

#### Confidence Scoring

**Source Count**: 5 points (4 sources)
- DORA 2024 (2.7× staff, Level 4 skills)
- IDC Research (2.5-3× operational staffing)
- Ververica (3.2 FTEs for Flink)
- McKinsey (tiger teams, 35-40% acceleration)

**Evidence Level Quality**: 5 points (100% Level A)
- All 4 sources = Level A

**Source Diversity**: 5 points (4 source types)
- Industry Research: DORA
- Industry Analyst: IDC
- Production Case Study: Ververica (Klaviyo)
- Consulting: McKinsey

**Quantitative Precision**: 5 points (precise convergence)
- DORA: 2.7× staff
- IDC: 2.5-3× operational staffing
- Ververica: 3.2 average FTEs for Flink
- All sources cite **2-3× range** or **3+ FTE minimum**

**Geographic/Organizational Diversity**: 3 points (US-centric, some international)
- DORA: Global survey
- Ververica: Klaviyo (US case study)
- McKinsey: International consulting firm

**Total Confidence**: **23/25 points** = ⭐⭐⭐⭐⭐ **STRONG**

---

#### Confidence Drivers

✅ **Independent validation**: DORA, IDC, Ververica all converge on 2-3× staffing multiplier
✅ **Skills classification**: DORA "Level 4" provides formal taxonomy (not anecdotal "skills are scarce")
✅ **100% Evidence Level A**: Exceptional source quality
✅ **Production validation**: Ververica 3.2 FTEs from real Flink deployment (not survey)

---

#### Confidence Limiters

⚠️ **Mid-market data limited**: Most sources focus on enterprise (500TB+)
⚠️ **Platform-specific**: Ververica 3.2 FTEs is **Flink-specific**, may not generalize to all streaming

---

#### Recommended Book Language

**Strong Confidence Statement**:
> "Streaming architectures require 2.7× operational staff vs batch processing (DORA 2024), with fault-tolerance expertise classified as a 'Level 4' specialized skill available in only the top 5% of organizations. Production validation confirms these staffing requirements: Ververica case study shows 3.2 average FTEs required for production Flink pipelines, while IDC research cites 2.5-3× higher operational staffing costs. McKinsey research on tiger teams (cross-functional expert groups) provides a mitigation strategy: short-term specialized staffing can accelerate implementation 35-40%, enabling knowledge transfer to internal teams."

**Citations**:
- DORA: MASTER-BIBLIOGRAPHY.md:357-376
- IDC: MASTER-BIBLIOGRAPHY.md:569-586
- Ververica: MASTER-BIBLIOGRAPHY.md:871-892
- McKinsey: MASTER-BIBLIOGRAPHY.md:1010-1030

---

### H-IMPL-03: Timeline Premium (Security Implementation)

**Hypothesis**: "Security-focused data lakehouse implementations require 15-30% longer timelines vs general data engineering due to compliance validation, security tool integrations, and detection logic migration."

**Validation Status**: ✅ **VALIDATED** (moderate confidence)

---

#### Confidence Scoring

**Source Count**: 3 points (3 sources)
- Gartner/phData (5.5 months security-focused)
- Confluent (4-6 months Kafka deployment)
- SANS Institute (security timeline premium vs general data engineering)

**Evidence Level Quality**: 3 points (67% Level A)
- Level A: SANS (2 of 3)
- Level B: phData (1 of 3)
- Note: Gartner = Level A, but phData implementation details = Level B

**Source Diversity**: 3 points (3 source types)
- Industry Analyst: Gartner
- Practitioner: phData
- Security Authority: SANS Institute
- Vendor: Confluent

**Quantitative Precision**: 3 points (range estimate)
- Gartner/phData: 5.5 months average (specific)
- SANS: 15-30% premium (range)
- Confluent: 4-6 months Kafka (general, not security-specific)

**Geographic/Organizational Diversity**: 1 point (limited)
- All sources US-centric
- No international security lakehouse timeline data

**Total Confidence**: **13/25 points** = ⭐⭐⭐ **MODERATE**

---

#### Confidence Drivers

✅ **SANS security-specific validation**: Authoritative source on security timeline differences
✅ **Quantitative precision**: 5.5 months (Gartner/phData) provides specific benchmark
✅ **15-30% premium validated**: SANS confirms security constraints add time vs general data engineering

---

#### Confidence Limiters

⚠️ **Source count limited**: Only 3 sources (vs 4-5 for stronger hypotheses)
⚠️ **Geographic diversity weak**: All US-centric (European/APAC data protection timelines may differ)
⚠️ **phData = Level B**: Implementation partner perspective (practitioner, not research)
⚠️ **General vs security timeline split unclear**: Confluent 4-6 months is general Kafka, not security-specific

---

#### Recommended Book Language

**Moderate Confidence Statement**:
> "Security-focused data lakehouse implementations average 5.5 months (Gartner/phData research), representing a 15-30% timeline premium vs general data engineering (SANS Institute validation). The premium stems from security-specific constraints: compliance validation gates (HIPAA, PCI-DSS, SOC 2 reviews add 2-4 weeks), security tool integrations (EDR, SIEM, threat intel platforms add 1-2 weeks), and detection logic migration (translating existing rules, validating accuracy adds 2-3 weeks). Confluent's 4-6 month Kafka deployment timeline provides a general baseline, with security use cases trending toward the longer end of the range."

**Confidence Caveat**: "Timeline data is predominantly from US implementations; European GDPR or APAC data localization requirements may extend timelines further."

**Citations**:
- Gartner/phData: MASTER-BIBLIOGRAPHY.md:940-960
- SANS: MASTER-BIBLIOGRAPHY.md:482-499
- Confluent: MASTER-BIBLIOGRAPHY.md:917-937

---

### H-COST-09: Tiered Storage Economics

**Hypothesis**: "Tiered storage strategies (hot/warm/cold) deliver 55-80% cost savings for multi-year security data retention, with AWS documenting 55% average savings and Netflix achieving 70-80% for Kafka tiered storage."

**Validation Status**: ✅ **STRONGLY VALIDATED**

---

#### Confidence Scoring

**Source Count**: 3 points (3 sources)
- AWS Storage Optimization Whitepaper (55%)
- Netflix Kafka Tiered Storage (70-80%)
- AWS Well-Architected (35% conservative estimate, 30-40% range)

**Evidence Level Quality**: 5 points (100% Level A)
- All 3 sources = Level A (AWS official docs, Netflix production)

**Source Diversity**: 3 points (2 source types)
- Cloud Provider: AWS (official documentation)
- Production Deployment: Netflix (authoritative streaming source)

**Quantitative Precision**: 5 points (precise range)
- AWS: 55% average, 30-40% range (conservative)
- Netflix: 70-80% for multi-year Kafka retention
- Range: **55-80% validated**

**Geographic/Organizational Diversity**: 3 points (US-centric, but Netflix = global scale)
- AWS: Global cloud provider
- Netflix: Global streaming platform

**Total Confidence**: **19/25 points** = ⭐⭐⭐⭐⭐ **STRONG**

---

#### Confidence Drivers

✅ **Production validation**: Netflix 70-80% savings is **real production deployment**, not theoretical
✅ **AWS authoritative**: Cloud provider official documentation (not marketing)
✅ **Convergent range**: AWS (55%) + Netflix (70-80%) establish **55-80% range**
✅ **100% Evidence Level A**: Exceptional source quality

---

#### Confidence Limiters

⚠️ **Source count moderate**: 3 sources (adequate, but not extensive)
⚠️ **Use case specific**: Netflix 70-80% is **Kafka tiered storage for multi-year retention** (not general lakehouse)
⚠️ **AWS conservative vs aggressive**: AWS cites both 35% (conservative) and 55% (average), creating ambiguity

---

#### Recommended Book Language

**Strong Confidence Statement**:
> "Tiered storage strategies deliver 55-80% cost savings for multi-year security data retention, validated by AWS official documentation (55% average savings) and Netflix production deployment (70-80% for Kafka tiered storage). The architecture separates hot data (recent 7-90 days, frequent access, S3 Standard or Kafka brokers) from cold data (historical 1-7 years, compliance retention, S3 Glacier). AWS provides a conservative 35% estimate (30-40% range) for general workloads, while security-specific use cases with multi-year compliance retention achieve Netflix-level savings (70-80%)."

**Citations**:
- AWS Storage Optimization: MASTER-BIBLIOGRAPHY.md:287-306, 1173-1194
- Netflix: MASTER-BIBLIOGRAPHY.md:523-542

---

### H3-PERFORMANCE-01: ClickHouse OLAP Performance

**Hypothesis**: "ClickHouse delivers exceptional OLAP performance for security workloads: 6 million requests/second throughput, 96% of queries completing under 1 second, and 5-10× storage efficiency vs Elasticsearch."

**Validation Status**: ✅ **HIGH CONFIDENCE**

---

#### Confidence Scoring

**Source Count**: 5 points (4 borrowed sources) + 1 first-party leg
- Cloudflare: 6M req/sec, 96% <1s queries
- Cloudflare: 10-12× compression
- Shell: 57TB/day security telemetry
- ClickHouse vs Elasticsearch: 5-10× storage efficiency
- **FIRST-PARTY (lab-measured, 2026-06-07, MOAR reference stack, single host)**: the FOIL probe (lakehouse vs an OpenSearch SIEM) over 200,000 OCSF events measured a SIEM index footprint of 11.5 MB against a columnar Parquet footprint of 1.6 MB — the SIEM index is ~7.0× the columnar footprint, which lands inside the borrowed "5-10×" band rather than at its edge, and answers agreed across the engines before the ratio was read. HEDGE: single host, OpenSearch over HTTP vs DuckDB in-process; the term-index advantage at larger scale is not isolated, so the robust first-party findings here are the answer-equality and the ~7.0× storage ratio, not a latency claim.

**Evidence Level Quality**: 5 points (100% Level A)
- All 4 sources = Level A (production deployments, benchmark study)

**Source Diversity**: 3 points (2 source types)
- Production Deployment: Cloudflare (2 sources), Shell
- Benchmark: ClickHouse vs Elasticsearch comparison

**Quantitative Precision**: 5 points (precise metrics)
- 6M req/sec (specific)
- 96% queries <1s (precise percentile)
- 5-10× storage efficiency (range)

**Geographic/Organizational Diversity**: 3 points (international)
- Cloudflare: Global CDN
- Shell: Global energy company
- ClickHouse: Vendor (but production validated)

**Total Confidence**: **21/25 points** = ⭐⭐⭐⭐ **HIGH**

---

#### Confidence Drivers

✅ **Production validation at scale**: Cloudflare (6M req/sec), Shell (57TB/day) prove ClickHouse works at massive security scale
✅ **Quantitative precision**: Not "fast," but "6M req/sec" and "96% <1s"
✅ **Security-specific**: Shell 57TB/day is **enterprise security deployment** (not general analytics)
✅ **100% Evidence Level A**: Exceptional
✅ **FIRST-PARTY storage measurement (lab-measured, 2026-06-07)**: our FOIL probe measured a SIEM index at ~7.0× the columnar Parquet footprint on first-party OCSF data (11.5 MB vs 1.6 MB over 200,000 events), inside the borrowed 5-10× band, with answers agreeing across engines — a measured leg under the borrowed benchmark, scoped to a single host (term-index advantage at larger scale not isolated)

---

#### Confidence Limiters

⚠️ **Source diversity moderate**: 2 production deployments + 1 benchmark (adequate, not extensive)
⚠️ **Vendor benchmark skepticism**: ClickHouse vs Elasticsearch comparison is ClickHouse-published (but Cloudflare/Shell validate claims)

---

#### Recommended Book Language

**High Confidence Statement**:
> "ClickHouse delivers exceptional OLAP performance for security workloads, validated by production deployments at massive scale: Cloudflare processes 6 million requests/second with 96% of queries completing under 1 second, while Shell analyzes 57 TB/day of security telemetry with sub-second query performance. Storage efficiency is equally compelling: ClickHouse achieves 10-12× compression ratios for log data (Cloudflare) and 5-10× storage efficiency vs Elasticsearch (ClickHouse benchmark), validated by real-world security deployments."

**Citations**:
- Cloudflare (6M req/sec): MASTER-BIBLIOGRAPHY.md:74-94
- Cloudflare (compression): MASTER-BIBLIOGRAPHY.md:97-116
- Shell: MASTER-BIBLIOGRAPHY.md:119-141
- ClickHouse vs Elasticsearch: MASTER-BIBLIOGRAPHY.md:1382-1401

---

### H-STREAM-01: Kafka Streams Security Patterns

**Hypothesis**: "Kafka Streams enables production-scale stateful security processing: LinkedIn maintains terabytes of state with millisecond access times, Uber operates thousands of real-time security views with sub-second refresh rates."

**Validation Status**: ✅ **HIGH CONFIDENCE**

---

#### Confidence Scoring

**Source Count**: 3 points (3 sources)
- LinkedIn: Kafka Streams state management (terabytes of state, ms access)
- Uber: Real-time security views (thousands of views, sub-second refresh)
- Confluent: Kafka Streams best practices

**Evidence Level Quality**: 5 points (100% Level A)
- All 3 sources = Level A (production deployments)

**Source Diversity**: 3 points (2 source types)
- Production Deployment: LinkedIn, Uber
- Vendor Best Practices: Confluent

**Quantitative Precision**: 5 points (precise metrics)
- Terabytes of state (LinkedIn)
- Millisecond access times (LinkedIn)
- Thousands of views (Uber)
- Sub-second refresh (Uber)

**Geographic/Organizational Diversity**: 1 point (US-centric)
- LinkedIn, Uber, Confluent all US-based

**Total Confidence**: **17/25 points** = ⭐⭐⭐⭐ **HIGH**

---

#### Confidence Drivers

✅ **Production security validation**: Both LinkedIn and Uber are **security-specific use cases**, not general streaming
✅ **Quantitative precision**: Not "scales well," but "terabytes of state" and "sub-second refresh"
✅ **100% Evidence Level A**: Exceptional

---

#### Confidence Limiters

⚠️ **Source count moderate**: 3 sources (adequate, but not extensive)
⚠️ **US-centric**: All sources US-based (no European/APAC validation)
⚠️ **Large enterprise only**: LinkedIn, Uber = massive scale (mid-market validation limited)

---

#### Recommended Book Language

**High Confidence Statement**:
> "Kafka Streams enables production-scale stateful security processing, validated by deployments at LinkedIn (maintaining terabytes of state with millisecond access times for security entity tracking) and Uber (operating thousands of real-time security views with sub-second refresh rates). These production deployments prove that stateful stream processing—previously considered too complex for security operations—is not only feasible but operationally superior to batch re-processing for entity behavior analytics."

**Citations**:
- LinkedIn: MASTER-BIBLIOGRAPHY.md:502-520
- Uber: MASTER-BIBLIOGRAPHY.md:681-699

---

## First-Party Hypotheses (Lab-Measured)

These six hypotheses are validated by first-party measurements on the SDW MOAR reference stack ("Modular Open Architecture"), run 2026-06-07 on a single host (Ryzen 5800H, WSL2). They are a distinct evidence tier from the borrowed-source hypotheses above: the data, the workload, the engines and the comparison are ours, the run is reproducible, and an answer-equality gate is applied before any latency or storage number is read. The scoring rubric above rewards independent-source diversity, which a single-apparatus run cannot supply, so these are scored on what they actually demonstrate — reproducibility, the answer-equality gate, and an identical-workload comparison — and they carry an explicit single-host scope limit. None of them claims datacenter scale, concurrency behavior, or organizational TCO; the relative pattern across engines is the finding, not the absolute milliseconds.

The five engines configured were DuckDB, Trino, ClickHouse, StarRocks, and Dremio; Dremio was not brought up for this run, so every engine claim below is a **four-engine** measured result.

---

### H-ENGINE-ANSWER-EQUIVALENCE-01: Four Engines Return Identical Answers

**Hypothesis**: "Four independent query engines, reading one shared Apache Iceberg table holding OCSF-shaped events, return the same answers for the same questions."

**Validation Status**: ✅ **VALIDATED (first-party, single host)**

**Evidence Tier**: First-party lab measurement (2026-06-07, MOAR reference stack). Distinct from — and for this specific claim, stronger than — the borrowed production numbers, because answer-equality across engines is something the literature's single-operator deployments never test (each runs one engine).

**Measurement**: DuckDB, Trino, ClickHouse and StarRocks each query the same Iceberg/OCSF table and agree on all three probes — `count(*)`, the needle (`dst_port = 3389`), and the `group-by dst_port`. Answer-equality is the gate: latency numbers (recorded under H-ARCH-02) are only read once the engines are shown to be computing the same thing.

**Confidence Drivers**:
✅ Cross-engine agreement on count, needle and group-by over identical bytes — the correctness floor under every later performance comparison
✅ Reproducible (fixed seed, fixed data) on the documented apparatus
✅ Establishes that an open table format (Iceberg) + open schema (OCSF) lets engines be swapped without changing the answer

**Confidence Limiters**:
⚠️ Single host; four engines (Dremio configured but not brought up this run)
⚠️ One table, OCSF `network_activity`; broader schema coverage not yet exercised
⚠️ Equivalence demonstrated on three query shapes, not an exhaustive query surface

**Recommended Language**:
> "On the MOAR reference stack, four engines — DuckDB, Trino, ClickHouse, StarRocks — reading one shared Iceberg/OCSF table returned identical answers for count, a needle lookup (dst_port=3389), and a group-by. The answer-equality gate is applied before any latency is reported, so the performance comparison rests on a verified correctness floor (first-party, single host, 2026-06-07)."

---

### H-ARCH-02: No Single Engine Wins

**Hypothesis**: "On one shared Iceberg/OCSF table, no single engine wins every workload — engine choice is a workload-and-scale property, not a global ranking."

**Validation Status**: ✅ **VALIDATED (first-party, single host)**

**Evidence Tier**: First-party lab measurement (2026-06-07, MOAR reference stack). The literature has no vendor-neutral identical-workload engine comparison (it is one of the review's named gaps); this is a first-party answer to it, bounded to a single host. The hypothesis has two axes — specialization by workload shape and specialization by concurrency — and the entry now measures both. The scale legs (1M baseline, 100M crossover) cover the workload-shape axis: the 100M-row run is where per-workload specialization actually appears across engines, and the 1M run is kept as the smaller-scale baseline that shows the crossover had not yet emerged. The concurrency-sweep leg covers the other axis, and it closes the concurrency half of the hypothesis that the scale legs only hinted at — the scale runs are single-client, so on their own they could note that specialization "is expected to shift with concurrency" but could not show it; the sweep measures it directly, and the single-query winner and the concurrent-throughput winner turn out to differ.

**Measurement (stronger leg — 100M-row crossover)**: 100,000,000-row OCSF `network_activity` table, single host, milliseconds:

| Workload | DuckDB | Trino | ClickHouse | StarRocks |
|----------|--------|-------|------------|-----------|
| full-scan `count(*)` | 12.4 | 44.4 | **10.5** | 48.2 |
| needle `dst_port=3389` | **77.7** | — | — | — |
| group-by `dst_port` | **103.1** | — | — | — |

At 100M the fastest engine differs by workload: ClickHouse wins the full-scan `count(*)` (10.5 ms vs DuckDB 12.4, Trino 44.4, StarRocks 48.2), while DuckDB wins both the selective needle (77.7 ms) and the group-by (103.1 ms). Answer-equality held across the gated workloads. Trino errored on the high-cardinality `distinct` at 100M, so that workload is not reported as a four-engine result at this scale.

**Measurement (1M baseline — no crossover yet)**: 1,000,000-row OCSF `network_activity` table, median of 4 trials, milliseconds (CV% in parentheses):

| Workload | DuckDB | Trino | ClickHouse | StarRocks |
|----------|--------|-------|------------|-----------|
| `count(*)` | **2.4** (10) | 68.5 (10) | 18.2 (11) | 39.9 (1) |
| needle `dst_port=3389` | **5.7** (3) | 97.5 (6) | 22.1 (8) | 45.3 (1) |
| group-by `dst_port` | **12.1** (7) | 96.6 (7) | 30.1 (5) | 55.3 (11) |
| distinct `src_ip` (latency-only; ClickHouse approx) | 139.7 (14) | 427.9 (17) | 168.7 (6) | **97.7** (2) |

**Measurement (concurrency-sweep leg — the other axis)**: `lab/concurrency_sweep.py`, MOAR reference stack, single host. C concurrent clients each run a scan-aggregate over the shared 10M-row OCSF table; C swept from 1 to 16, recording throughput (queries/sec) and p95 latency (ms):

| Engine | Throughput, C1 → C16 (q/s) | p95 latency, C1 → C16 (ms) | Shape |
|--------|----------------------------|----------------------------|-------|
| DuckDB | ~46 → ~46 (flat) | 57 → 689 (~12×) | fastest at one client, caps under concurrency |
| ClickHouse | 20 → 58 | 59 → 355 (gentlest) | scales with C, overtakes DuckDB by C16 |
| StarRocks | 16 → 42 | — | scales, plateaus ~C8 |
| Trino | 9 → 13 (flat-low) | → 1736 | single-host coordinator penalty, no cluster |

DuckDB's throughput is flat at ~46 q/s across every C while its p95 climbs from 57 to 689 ms (~12×): one embedded process on a fixed core budget is the fastest at a single client but does not gain under added concurrency. ClickHouse scales the opposite way — throughput climbs 20 → 58 q/s, overtaking DuckDB by C16, on the gentlest p95 (59 → 355 ms). StarRocks scales to 42 q/s but plateaus around C8, and Trino stays flat-low (9 → 13 q/s) with p95 blowing out to 1736 ms, which is the single-host coordinator penalty rather than a cluster result. So the single-query winner (DuckDB) and the concurrent-throughput winner (ClickHouse) are different engines, which is "no single engine wins" along the concurrency axis as well as the workload-shape axis.

**Reading**: at 1M (and at 10M) the embedded DuckDB won every gated workload — count, needle and group-by — so the smaller runs do not on their own demonstrate specialization, since one engine sweeping the board is also what you would see if that engine were simply better. The 100M run is the scale point where the crossover appears: ClickHouse takes the full-scan `count(*)` while DuckDB keeps the selective needle and the group-by, so "no single engine wins" is measured rather than asserted, and the 1M→100M progression is itself the evidence — the per-workload split is a property of scale, not visible until the table is large enough to exercise it. Engine specialization is a scale-and-concurrency property, and the concurrency-sweep leg measures the second half of that directly: the single-client query winner (DuckDB) and the concurrent-throughput winner (ClickHouse) are different engines, so engine choice is specialized by concurrency as well as by workload shape — the scale legs only hinted at this when they noted the pattern "is expected to shift with concurrency," and the sweep now shows the crossover happening as clients pile on rather than as the table grows. The relative pattern is the finding, not the absolute milliseconds. The 1M `distinct` row is latency-only (ClickHouse uses an approximate distinct), so it is read as a latency comparison, not an exact-count claim; at 100M Trino errored on that workload, so `distinct` is not a four-engine result at scale.

**Confidence Drivers**:
✅ The 100M run shows an actual cross-engine crossover (ClickHouse wins full-scan count, DuckDB wins needle and group-by) — direct evidence of per-workload specialization, which the 1M sweep alone could not establish
✅ Four engines × multiple workloads, all on one shared table — the comparison is identical-workload by construction
✅ Answer-equality held across the gated workloads at 100M, gated by H-ENGINE-ANSWER-EQUIVALENCE-01 before latency is read
✅ The 1M→100M progression is documented, so the emergence of the crossover with scale is visible rather than a single-scale snapshot
✅ The concurrency sweep (C1→C16, 10M-row shared table) measures the second axis directly: the single-query winner (DuckDB, flat ~46 q/s) and the concurrent-throughput winner (ClickHouse, 20→58 q/s, overtaking by C16) are different engines, so "no single engine wins" holds by concurrency, not only by workload shape
✅ 1M run is median of 4 trials with CV% reported, so trial-to-trial spread is visible at the baseline scale

**Confidence Limiters**:
⚠️ Single host; in-process DuckDB has a structural advantage over the networked engines, and the relative pattern is expected to keep shifting with further data volume. Single-host concurrency is now measured (the sweep), so the remaining gap is multi-node cluster concurrency — the sweep exercises each engine's scheduling model under contention on one box, not a real distributed cluster, where Trino's coordinator/worker model in particular would be expected to behave differently than the single-host coordinator penalty seen here
⚠️ The crossover is a relative-pattern finding on one apparatus, a direction rather than a scaling law; absolute milliseconds and q/s are bounded to this host
⚠️ Trino errored on the high-cardinality `distinct` at 100M, so that workload is not a four-engine result at scale; the 1M ClickHouse `distinct` is approximate and that row is latency-only

**Recommended Language**:
> "Engine specialization runs along two axes, and the lab measured both. By workload shape: at 1M (and 10M) rows the embedded DuckDB won every gated workload, but at 100M rows the crossover emerged — ClickHouse won the full-scan count (10.5 ms vs DuckDB 12.4, Trino 44.4, StarRocks 48.2) while DuckDB kept the selective needle (77.7 ms) and the group-by (103.1 ms), with answer-equality holding across the gated workloads. By concurrency: sweeping 1 to 16 concurrent clients over a shared 10M-row table, DuckDB stayed fastest at one client but flat at ~46 q/s while its p95 climbed ~12×, whereas ClickHouse scaled from 20 to 58 q/s and overtook DuckDB by 16 clients on the gentlest p95 — so the single-query winner and the concurrent-throughput winner are different engines. So 'no single engine wins' is the measured result on both axes, not an assertion carried over from the smaller single-client runs; the finding is the relative pattern, bounded to a single host. The remaining open gap is multi-node cluster concurrency, which still needs a real cluster (first-party, 2026-06-07; Trino errored on the high-cardinality distinct at 100M)."

---

### H-OCSF-CONTEXT-COLLAPSE-01: Flattening-Fidelity Loss

**Hypothesis**: "Flattening OCSF events into a tabular layout collapses context, and the loss is measurable."

**Validation Status**: ✅ **VALIDATED (first-party, published lab artifact)**

**Evidence Tier**: First-party lab measurement, and the most publicly developed of the six — three published Tier-B artifacts in the public lab repository (`github.com/flying-coyote/sdw-lab-benchmarks`) speak to it: the original synthetic-testbed `bench-a-context-collapse/`, its de-gamed re-run `ocsf-context-collapse-apt29/`, and the mechanism-decomposition leg `flattening-fidelity/` (the standalone `ocsf-flattening-benchmark` repo is archived and forwards there). Cite the de-gamed APT29 result as the headline and the mechanism-decomposition curves as the "why", rather than re-deriving either here.

**Measurement (headline — de-gamed APT29, supersedes the synthetic delta)**: the de-gamed re-run scores **unmodified upstream SigmaHQ rules** (cloned verbatim, compiled via pySigma→SQL) against real MITRE ATT&CK APT29 evaluation telemetry (OTRF/Mordor day 1), with each rule's adversary/routine split taken from its own `attack.tXXXX` tags rather than lab judgment. Under the documented 64-char field-truncation cap it reports an adversary-vs-routine mean blinding recall-loss delta of **+0.188**, and a coarsening-sensitivity sweep over the truncation cap (256 → 16 chars) bounds it to **+0.094 to +0.205** — the published +0.188 sitting mid-to-upper in that range, positive at every cap, never inverting. Adversary-relevant detections lose **~2× the recall** and go fully blind **~2× as often** as routine detections, with the blinded rules the expected encoded-PowerShell / long-script-block family (APT29's tradecraft). The fidelity store costs **1.799×** the bytes (1,888,601 vs 1,049,655) and 1.265× query wall-clock against this battery, so storage is the more expensive axis of keeping fidelity.

**Measurement (synthetic-testbed predecessor — labelled, retained as the audit trail)**: the original BENCH-A on the lab's own synthetic testbed reported a headline delta of **+0.719** (robust across background re-draws, +0.710 to +0.719). That result is **gameable** — the lab authored the detection rules, planted the attack chain, and chose the coarsening grains — which is why it is superseded by the de-gamed APT29 re-run above and quoted here as the synthetic-testbed magnitude, not the headline. The routine→adversary disproportionality replicated with nothing lab-authored, which is what the de-gamed run establishes.

**Measurement (mechanism decomposition — `flattening-fidelity/`, the three failure modes as curves)**: the flattening-fidelity leg isolates each mechanism on its own synthetic corpus and reports two of the three magnitudes as closed-form curves rather than point estimates. Mode 1 (absence→NULL coercion) is **100% silent miss by construction** — absence and NULL are the same byte once the column is flattened — privilege-escalation recall 0.00 lossy vs 1.00 preserved. Mode 2 (grain rollup) collapses beacon-hunt to **F1 = 2/(2 + decoy-to-beacon ratio)**, the published 0.50 being the ratio-2 point (seed leaves it unmoved, CV ≈ 0). Mode 3 (floating timestamps) collapses cross-zone correlation to **recall = 1 − cross-zone fraction**, the published ~0.46–0.50 being the fraction-0.5 point. The fidelity-preserving store holds 1.0 at every parameter, so the parameter-independent finding is the *shape* (lossy store collapses on the corpus parameter, preserved store does not), and the magnitude reads off the parameter.

**Confidence Drivers**:
✅ The de-gamed APT29 leg removes all three Karen-flagged levers (lab-authored rules → unmodified SigmaHQ, synthetic chain → real APT29 telemetry, lab-chosen grains → documented volume-driven defaults applied blind), so the disproportionality holds with nothing lab-authored
✅ The coarsening-sensitivity sweep bounds the headline (+0.094 to +0.205) and shows it is positive at every truncation cap, robust to the "you picked the cap" rebuttal
✅ Mechanism decomposition reports two magnitudes as closed-form curves (F1 = 2/(2+r), recall = 1−cross-zone fraction) measured equal to the closed form, with the preserved store at 1.0 throughout
✅ Published, externally inspectable, reproducible (pinned pySigma/sigma-cli versions; fixed seeds; documented methods)
✅ Security-specific by construction (OCSF events, real APT29 detection rules, the flattening problem security log pipelines actually hit)
✅ A measured fidelity delta with a priced storage/query cost (1.799× storage, 1.265× query), not a directional "flattening loses information" assertion

**Confidence Limiters**:
⚠️ The de-gamed APT29 leg is one dataset, one coarsening config, a modest fired-rule sample (APT29 exercises a subset of techniques); recall-loss is measured against the fidelity store, not absolute per-event labels
⚠️ The synthetic-testbed +0.719 is gameable (lab-authored rules/chain/grains) and is retained only as the labelled predecessor, not a citable headline
⚠️ The mechanism-decomposition magnitudes (Mode 2 F1, Mode 3 recall) are corpus parameters, not universal constants; only Mode 1 (absence→NULL) is structural and parameter-free
⚠️ Single-host lab apparatus throughout; the independent-reviewer sign-off that the coarse store resembles what shops actually build remains the open Tier-A gate

**Recommended Language**:
> "The context-collapse loss is measured, not asserted: on real MITRE ATT&CK APT29 telemetry scored with unmodified upstream SigmaHQ rules, OCSF coarsening blinds adversary-relevant detections ~2× more than routine ones — a +0.188 mean recall-loss delta (sweep range +0.094 to +0.205) under a documented field-truncation default, and the fidelity store that avoids it costs 1.799× the storage. The earlier synthetic-testbed figure (+0.719) was a lab-authored, gameable predecessor; the de-gamed re-run reproduces the disproportionality with nothing lab-authored. (First-party, reproducible; github.com/flying-coyote/sdw-lab-benchmarks, ocsf-context-collapse-apt29/ and flattening-fidelity/.)"

---

### H-SEC-CATALOG-01: Catalog Portability

**Hypothesis**: "A lakehouse table is portable across catalog implementations — the same data can be served from different catalogs by swapping the catalog, not rewriting the table."

**Validation Status**: ✅ **VALIDATED for open catalogs (first-party); ⚠️ Unity Catalog leg NOT reproducible**

**Evidence Tier**: First-party lab measurement (2026-06-07, MOAR reference stack).

**Measurement**: the swap-catalog probe ran the same table across five open catalog implementations — a REST catalog, Polaris, Nessie, Lakekeeper and Gravitino — and served the data from each. The **open-catalog legs are the reproducible result.** The Unity Catalog leg is **NOT reproducible** in this apparatus and is reported as a negative/limitation, not a success — the portability claim holds for the open-catalog set, and stops at the boundary of a vendor-governed catalog we could not bring up.

**Confidence Drivers**:
✅ Five independent open catalog implementations served the same table (REST, Polaris, Nessie, Lakekeeper, Gravitino)
✅ Honest negative: the Unity Catalog leg is recorded as not-reproducible rather than quietly dropped

**Confidence Limiters**:
⚠️ Unity Catalog NOT reproducible in this apparatus — portability is demonstrated for open catalogs only
⚠️ Single host; functional portability shown, not catalog performance or concurrency under load

**Recommended Language**:
> "The same lakehouse table was served from five open catalogs — REST, Polaris, Nessie, Lakekeeper, Gravitino — by swapping the catalog, demonstrating catalog portability across the open set. The Unity Catalog leg was not reproducible in this apparatus, so the claim is scoped to open catalogs and stops at the vendor-governed boundary (first-party, single host, 2026-06-07)."

---

### H-DUCKLAKE-02: Swap-Format Read-Neutral + Streaming Commit-Tax

**Hypothesis**: "Reading the same logical data is format-neutral between Iceberg and DuckLake when the underlying bytes are identical; the format choice for security telemetry turns instead on the write/commit contract under a tiny-frequent-commit cadence."

**Validation Status**: ✅ **VALIDATED (first-party, single host)**

**Evidence Tier**: First-party lab measurement (2026-06-07, MOAR reference stack). Two complementary legs: a read-path leg that controls the writer confound by reading byte-identical data into both formats, and a write-path leg that measures the commit-tax directly under streaming cadence.

**Measurement (leg 1 — read-neutrality)**: the swap-format probe registered the same byte-identical files into both an Iceberg table and a DuckLake table and read both; the read was **format-neutral** — Iceberg↔DuckLake showed no read advantage on identical bytes. The control is that the bytes are the same, so any difference would be the format layer, not the writer/encoder.

**Measurement (leg 2 — streaming commit-tax, the write-contract complement)**: because reads are at parity on byte-identical data, the format choice for security telemetry — whose cadence is many tiny frequent commits — turns on the write/commit contract, which `lab/commit_tax.py` measures directly (MinIO object store, single host; the script lives in `security-data-that-works/docker/lab/commit_tax.py`, run 2026-06-07 — the committed 2026-06-15 re-run in that repo's `docker/MOAR-EVIDENCE-RUN-2026-06-15.md` reproduces the shape, with DuckLake planning 5.6–7.2 ms and Iceberg 9.9→142.5 ms; run-to-run magnitudes differ, the shape is the finding). Writing 100,000 rows as one batch commit versus 100 streaming commits, Iceberg pays a steep per-commit tax as cadence rises: ingest 0.44 s → 16.3 s (~37×), data files 1 → 100 (the file-per-commit floor), metadata files 4 → 301, metadata footprint 8.9 KB → 4,579 KB (~515×), and query-planning latency 8.7 ms → 181 ms (~21×, from walking the lengthening manifest list). DuckLake on the same 100-commit stream keeps its metadata in the catalog DB, so planning stays flat (~7 ms regardless of cadence), and with inlining enabled it writes 0 per-commit Parquet files. So the leg that actually distinguishes the two formats for security's commit pattern is the write contract, not the read path — leg 1 establishes read parity, leg 2 shows where the parity ends.

**Confidence Drivers**:
✅ Byte-identical underlying data isolates the format layer from the writer confound (leg 1)
✅ Read-neutrality is the measured result, not an assumed equivalence (leg 1)
✅ The commit-tax is measured under the tiny-frequent-commit cadence that matches security telemetry, not assumed (leg 2)
✅ The write-path leg and the read-path leg are complementary: reads at parity on identical bytes, writes diverging sharply under streaming cadence, so the format decision is located on the write contract directly

**Confidence Limiters**:
⚠️ Single host (MinIO object store); the *shape* of the tax is the finding, not a production-scale magnitude
⚠️ Leg 1 measures read-neutrality, leg 2 the streaming write/commit path; neither covers maintenance-operation behavior (compaction, expiry) at scale
⚠️ Iceberg's per-commit floor is sensitive to commit batching and table-maintenance settings; the 100-commit stream is a deliberate worst-case for the file-per-commit floor

**Recommended Language**:
> "Reading byte-identical data registered into both an Iceberg and a DuckLake table was format-neutral on a single host — no read advantage either way — which isolates the format layer from the writer confound. The write contract is where they diverge: under a 100-commit stream of 100,000 rows, Iceberg's ingest went 0.44 s → 16.3 s (~37×), its metadata footprint 8.9 KB → 4,579 KB (~515×), and query-planning 8.7 ms → 181 ms (~21×) as it walked a lengthening manifest list, while DuckLake kept planning flat (~7 ms) by holding metadata in the catalog DB and wrote 0 per-commit Parquet files with inlining on. So for security telemetry's tiny-frequent-commit cadence, reads are at parity and the format choice turns on the commit contract (first-party, MinIO, single host, 2026-06-07)."

---

### H-NDR-FEDERATION-01: Cross-Source Correlation

**Hypothesis**: "Joining two security telemetry sources surfaces an attacker that neither source reveals on its own."

**Validation Status**: ✅ **VALIDATED (first-party, single host)**

**Evidence Tier**: First-party lab measurement (2026-06-07, MOAR reference stack). Demonstrates federation value on a controlled cross-source join rather than asserting it.

**Measurement**: the correlate probe joined two OCSF sources on `src_ip` and surfaced attacker `198.51.100.66` exhibiting 8 failed authentications plus 5 RDP connections — a lateral-movement pattern visible only in the join. Neither source alone shows the pattern; the cross-source correlation is what makes it legible.

**Confidence Drivers**:
✅ The lateral-movement pattern (8 failed auths + 5 RDP connections) is present only after the join, demonstrating federation value concretely
✅ Controlled, reproducible join on a known schema key (`src_ip`)

**Confidence Limiters**:
⚠️ Single host; constructed two-source scenario, not a production NDR estate
⚠️ Demonstrates the join surfaces the pattern; does not measure detection rate, false-positive cost, or scale behavior

**Recommended Language**:
> "Joining two OCSF sources on src_ip surfaced attacker 198.51.100.66 (8 failed auths + 5 RDP connections, a lateral-movement pattern) that neither source revealed alone — federation value shown on a controlled join, not asserted (first-party, single host, 2026-06-07)."

---

### H-CROSS-TOOL-ASSURANCE-01: Cross-Tool Data-Health Gap (band annotation)

**Hypothesis**: "Assurance lives in the cross-tool view — the merged, freshness/authority-ranked picture of an estate recovers materially more true state than any single tool, and a residual gap remains that no tool covers correctly."

**Validation Status**: ✅ **VALIDATED (first-party, single host, synthetic corpus)**

**Evidence Tier**: First-party lab measurement (`ocsf-data-health/`, public Tier-B; DuckDB 1.5.3, seed 20260601). This is the first-party benchmark behind the fourth layer (the cross-tool gap) of the data-health framework the Capability Matrix scores. Added here as a confidence annotation — not a fully rubric-scored row — because its discriminating dimensions are the same single-apparatus reproducibility / determinism-gate profile as the other first-party legs rather than independent-source diversity.

**Measurement (point → band)**: a synthetic estate of 20,000 assets × 7 attributes = 140,000 ground-truth cells, observed by four source tools through deterministic flaw models, scored by exact set-based measures. The canonical run (truth=701, obs=702) reports best-single-tool recovery **47.7%** and cross-tool best-context recovery **75.6%** (+27.9% over best single, 24.4% residual gap no tool covers correctly). A 12-seed re-draw of the whole corpus (EXT-3) bands those two headline magnitudes: best-single **47.4% ± 0.15%** (range 47.1–47.7%, CV 0.3%) and cross-tool **75.4% ± 0.21%** (range 75.0–75.6%, CV 0.3%), so the canonical 47.7/75.6 point sits at the top edge of each band — a real reproducible draw of a tight distribution, not a fragile single seed. EXT-1 separately holds the three orderings (cross-tool > best-single, residual > 0, scored merge > naive) at every point of a 3×3 staleness×coverage grid; the parameter-independent finding is the *order*, the magnitudes are corpus parameters.

**Confidence Drivers**:
✅ The headline is banded across 12 independent corpus re-draws (CV 0.3% on both magnitudes), inoculating against a single-draw rebuttal
✅ The ordering holds at every cell of a parameter sweep, so the transferable claim (cross-tool > best-single, residual > 0) is parameter-independent
✅ Build-twice byte-identical determinism gate + planted-ground-truth integrity check before any number is read

**Confidence Limiters**:
⚠️ Single-host, synthetic corpus — Tier B, no production claim; the flaw-model magnitudes are corpus parameters, not universal constants (read METHODOLOGY.md before trusting any number)
⚠️ The bandable result is the magnitude of two measures on the easiest entity (assets, one clean key); a contested join key (EXT-2 identities) costs a measured −10.1% entity-resolution tax that the asset headline does not carry

**Recommended Language**:
> "Across a 20k-asset synthetic estate, the cross-tool merge recovers 75.4% of true state (±0.21% over 12 corpus re-draws, CV 0.3%) against the best single tool's 47.4% (±0.15%, CV 0.3%), leaving a residual ~24% no tool covers correctly — assurance lives in the cross-tool view, the magnitude is a tight reproducible band rather than one lucky seed, and the parameter-independent finding is the ordering (first-party, single host, synthetic; github.com/flying-coyote/sdw-lab-benchmarks, ocsf-data-health/)."

---

## Consolidated Confidence Assessment

### Overall Validation Strength

| Hypothesis | Confidence | Recommendation for Book |
|------------|-----------|------------------------|
| **H-ARCH-01** | ⭐⭐⭐⭐⭐ | **Refine from "76%" to "industry consensus"** - strong claim justified |
| **H-IMPL-01** | ⭐⭐⭐⭐ | **2.5-3× operational costs** - high confidence, cite convergence |
| **H-IMPL-02** | ⭐⭐⭐⭐⭐ | **2.7× staffing, Level 4 skills** - strongest validation, lead with this |
| **H-IMPL-03** | ⭐⭐⭐ | **5.5 months, 15-30% premium** - moderate confidence, add caveat |
| **H-COST-09** | ⭐⭐⭐⭐⭐ | **55-80% tiered storage savings** - strong, cite AWS + Netflix |
| **H3-PERFORMANCE-01** | ⭐⭐⭐⭐ | **6M req/sec, 96% <1s** - high confidence, cite Cloudflare + Shell; FIRST-PARTY ~7.0× storage (FOIL) added |
| **H-STREAM-01** | ⭐⭐⭐⭐ | **Terabytes of state, sub-second views** - high confidence, cite LinkedIn + Uber |

**First-party (lab-measured, MOAR reference stack, 2026-06-07, single host):**

| Hypothesis | Confidence | Recommendation for Book |
|------------|-----------|------------------------|
| **H-ENGINE-ANSWER-EQUIVALENCE-01** | ⭐⭐⭐⭐ | **Four engines agree on one Iceberg/OCSF table** - lead the apparatus with the answer-equality gate |
| **H-ARCH-02** | ⭐⭐⭐⭐ | **No single engine wins** - lead with the measured 100M crossover (ClickHouse full-scan count, DuckDB needle + group-by; DuckDB swept at 1M/10M); then the concurrency sweep, where the single-query winner (DuckDB, flat ~46 q/s) and the throughput winner (ClickHouse, 20→58 q/s by C16) differ — specialized by concurrency as well as workload shape; relative pattern, single host, remaining gap is multi-node cluster concurrency |
| **H-OCSF-CONTEXT-COLLAPSE-01** | ⭐⭐⭐⭐ | **De-gamed +0.188 adversary-vs-routine recall-loss delta** (sweep +0.094 to +0.205, ~2× recall / blind, 1.799× storage to keep fidelity) on unmodified SigmaHQ + real APT29 — cite the de-gamed APT29 + mechanism-decomposition artifacts; the synthetic-testbed +0.719 is the gameable, labelled predecessor it supersedes, don't lead with it |
| **H-SEC-CATALOG-01** | ⭐⭐⭐ | **Portable across 5 open catalogs** - state the Unity Catalog leg as not-reproducible |
| **H-DUCKLAKE-02** | ⭐⭐⭐⭐ | **Iceberg↔DuckLake read-neutral on identical bytes; commit-tax diverges under streaming** - reads at parity (writer-confound control), but a 100-commit stream costs Iceberg ~37× ingest / ~515× metadata footprint / ~21× planning while DuckLake stays flat; lead with the write-contract complement for security's tiny-frequent-commit cadence |
| **H-NDR-FEDERATION-01** | ⭐⭐⭐⭐ | **Join surfaces 198.51.100.66 lateral movement** - federation value on a controlled join |
| **H-CROSS-TOOL-ASSURANCE-01** | ⭐⭐⭐⭐ | **Cross-tool 75.4% vs best-single 47.4% recovery** (CV 0.3% over 12 corpus re-draws), ~24% residual gap no tool covers — assurance lives in the cross-tool view; lead with the banded magnitudes, transferable claim is the ordering (band annotation, not rubric-scored) |

---

### Confidence Distribution Analysis

**Strong Confidence (⭐⭐⭐⭐⭐)**: 3 hypotheses
- H-ARCH-01 (Iceberg dominance)
- H-IMPL-02 (Staffing scarcity)
- H-COST-09 (Tiered storage)

**High Confidence (⭐⭐⭐⭐)**: 3 hypotheses
- H-IMPL-01 (TCO reality)
- H3-PERFORMANCE-01 (ClickHouse)
- H-STREAM-01 (Kafka Streams)

**Moderate Confidence (⭐⭐⭐)**: 1 hypothesis
- H-IMPL-03 (Timeline premium)

**Assessment**: **86% of hypotheses have High or Strong confidence** (6 of 7). Only H-IMPL-03 has moderate confidence due to limited source count (3 sources, 67% Level A).

---

## Academic Publication Readiness

### Confidence Statements for Journal Submission

**Strong Confidence Hypotheses** (suitable for primary claims):
> "Our systematic review strongly validates that Apache Iceberg has emerged as the industry consensus choice for open table formats, with universal vendor support across AWS, Google, Microsoft, Snowflake, and Databricks (5 sources, 100% Evidence Level A)."

> "Streaming architectures require 2.7× operational staff vs batch processing, with fault-tolerance expertise classified as 'Level 4' specialized skills (DORA, IDC, Ververica, McKinsey validation; 4 sources, 100% Evidence Level A)."

> "Tiered storage strategies deliver 55-80% cost savings for multi-year security data retention, validated by AWS official documentation and Netflix production deployment (3 sources, 100% Evidence Level A)."

---

**High Confidence Hypotheses** (suitable for supporting claims):
> "Streaming architectures incur 2.5-3× higher operational costs vs batch processing, with convergent validation from industry analyst (IDC), industry research (DORA), and production data (Confluent) (5 sources, 80% Evidence Level A)."

> "ClickHouse delivers exceptional OLAP performance for security workloads: 6M req/sec throughput and 96% of queries <1s, validated by Cloudflare and Shell production deployments processing 57 TB/day of security telemetry (4 sources, 100% Evidence Level A)."

---

**Moderate Confidence Hypotheses** (require caveat):
> "Security-focused data lakehouse implementations average 5.5 months (Gartner/phData), representing a 15-30% timeline premium vs general data engineering (SANS validation). However, this finding is based on predominantly US implementations; European GDPR or APAC data localization requirements may extend timelines further (3 sources, 67% Evidence Level A)."

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-15 | Initial confidence assessment (7 hypotheses) |
| 1.1 | 2026-06-07 | Added 6 first-party (MOAR reference-stack) hypotheses; re-grounded two borrowed cells |
| 1.2 | 2026-06-07 | Upgraded H-ARCH-02 with the measured 100M-row crossover (stronger leg): ClickHouse wins full-scan count, DuckDB wins needle + group-by; 1M table kept as baseline (DuckDB swept at 1M/10M), 1M→100M progression documented as the evidence that specialization is a scale property |
| 1.3 | 2026-06-07 | Added the H-ARCH-02 concurrency-sweep leg (`lab/concurrency_sweep.py`, C1→C16 over a shared 10M-row OCSF table): DuckDB flat ~46 q/s (p95 57→689 ms), ClickHouse 20→58 q/s overtaking by C16 (gentlest p95 59→355 ms), StarRocks 16→42 q/s plateauing ~C8, Trino flat-low 9→13 q/s (p95→1736 ms, single-host coordinator penalty). Closes the concurrency half of "no single engine wins" that the single-client scale legs only hinted at — the single-query winner (DuckDB) and the concurrent-throughput winner (ClickHouse) differ, so specialization is by concurrency as well as workload shape. Single-host limiter updated: single-host concurrency now measured, remaining gap is multi-node cluster concurrency |
| 1.4 | 2026-06-14 | Re-anchored H-OCSF-CONTEXT-COLLAPSE-01 on the **de-gamed APT29** result (+0.188 adversary-vs-routine recall-loss delta, sweep +0.094 to +0.205, ~2× recall/blind, 1.799× storage to keep fidelity) from `ocsf-context-collapse-apt29/`; labelled the synthetic-testbed **+0.719** (`bench-a-context-collapse/`, robust +0.710–0.719) as the gameable lab-authored predecessor it supersedes, retained as the audit trail. Folded in the `flattening-fidelity/` mechanism-decomposition curves (Mode 1 = 100% structural; Mode 2 F1 = 2/(2+decoy ratio); Mode 3 recall = 1−cross-zone fraction; preserved store 1.0 throughout). Added an **H-CROSS-TOOL-ASSURANCE-01** band annotation from `ocsf-data-health/`: best-single 47.4% / cross-tool 75.4% recovery (CV 0.3% over 12 corpus re-draws, canonical 47.7/75.6 at the top edge), residual ~24% gap, ordering parameter-independent. All numbers re-derived from the first-party FINDINGS docs; this is a presentation/banding refinement, no magnitude change. **Jeremy sign-off pending** on (a) treating the de-gamed +0.188 as the matrix headline over the published +0.719 and (b) the new data-health annotation row |

---

**Maintained By**: Jeremy Wiley
**Repository**: security-data-literature-review
**Purpose**: Transparent confidence scoring for honest hypothesis evaluation
**Methodology**: Evidence-based rubric (source count, evidence level, diversity, precision, geographic spread)
