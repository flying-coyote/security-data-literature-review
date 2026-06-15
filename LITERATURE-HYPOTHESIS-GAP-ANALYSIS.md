# Literature Review → Hypothesis Gap Analysis

**Purpose**: Identify missing hypotheses, concepts, and research areas based on literature extraction
**Sources**: 283 footnotes from best practices doc + MASTER-HYPOTHESIS-TRACKER.md (26 existing hypotheses)
**Date**: October 10, 2025
**Last Reviewed**: October 16, 2025 (v1.6.1 - Post-blog/book integration update)
**Status**: Analysis COMPLETE - 6 new hypotheses identified and proposed, 3 now STRONGLY VALIDATED

---

## Version 1.6.1 Update (October 16, 2025)

**Changes**:
- **H-IMPL-01 (Streaming TCO)**: Upgraded to STRONGLY VALIDATED (blog post + 8 Level A sources)
- **H-IMPL-02 (Staffing Scarcity)**: Upgraded to STRONGLY VALIDATED (staffing calculator + blog quantification)
- **H-COST-09 (Tiered Storage)**: Upgraded to VALIDATED (cost optimization playbook + ROI analysis)
- **Expert Interview Preparation**: Comprehensive guides created for Lisa Cao (H-ARCH-03, XTable) and Jake Thomas (H-EDGE-01, H1-VOLUME-07)

**Impact**: 3 of 6 proposed hypotheses now have strong multi-source validation suitable for academic publication.

---

## Executive Summary

**Finding**: Literature reveals 8 major hypothesis/concept gaps requiring formalization

**Critical Gaps** (Need immediate hypotheses):
1. **Operational TCO Reality** - Hidden costs 2.5-3× underestimated
2. **Streaming Staffing Requirements** - Specialized skills gap
3. **Security-Specific Implementation Timelines** - Different from general data engineering
4. **Tiered Storage Cost Optimization** - 70-80% savings patterns

**Emerging Concepts** (Need tracking):
5. **Table Format Interoperability** (Apache XTable)
6. **Vector Search for Security** (Trino 424+)
7. **DuckDB Edge Processing** (Jake Thomas validation)
8. **Kafka Streams for Security** (Production patterns)

---

## Analysis: Existing Hypotheses vs Literature

### Well-Validated Existing Hypotheses

**H-ARCH-01: Apache Iceberg Dominance**
- ✅ **Strong Validation**: Industry consensus as de facto standard
  - **Dremio 2024 survey**: 29% planning Iceberg vs 23% Delta Lake (next 3 years)
  - **Universal vendor support**: AWS, Google, Snowflake, Databricks, Microsoft
  - **Production validation**: SK Telecom (52.7TB in 3.39s, 97% query time reduction)
  - **Apache governance**: 300+ contributors across 100+ organizations
- **Literature Support**: Footnotes [^3], [^131], [^132], [^243-249]
- **Note**: Original "76% adoption" claim not found in validation searches (Oct 2025). Updated to "industry consensus" with Dremio survey + vendor support evidence. Confidence remains Strong (⭐⭐⭐⭐⭐).
- **Status**: STRONGLY VALIDATED

**H3-PERFORMANCE-01: ClickHouse OLAP Performance**
- ✅ **Strong Validation**: Cloudflare (96% <1s), Shell (57TB/day), multiple benchmarks
- **Literature Support**: Footnotes [^7], [^8], [^11], [^81], [^99-108]
- **Status**: VALIDATED

**H1-COST-08: SIEM vs Storage Cost Differential**
- ✅ **Partial Validation**: AWS tiered storage (55% savings), Netflix Kafka (70-80% reduction)
- **Literature Support**: Footnotes [^15], [^70]
- **Gap**: Need direct SIEM pricing validation (in progress per user)
- **Status**: PARTIALLY VALIDATED

**H1-VOLUME-07: Security Data Volume Claims**
- ✅ **Validation**: Shell ClickHouse (57TB/day security telemetry)
- **Literature Support**: Footnote [^11]
- **Gap**: Need mid-sized enterprise validation (SOC survey in progress)
- **Status**: PARTIALLY VALIDATED

**H-ARCH-06: Query Engines Hyper-Specialize by Workload**
- ✅ **First-party Validation (Tier B, single host)**: SDW Lab `engine-join-specialization` + the workload×engine crossover — StarRocks wins multi-table joins (≈2.7–2.8× over ClickHouse on the heaviest six-table join), ClickHouse wins flat scan-aggregation, DuckDB wins selective lookups; the per-workload winner differs at 100M rows, and the 2026-06 UEBA two-level-aggregation inverts the top (StarRocks 0.207 s > ClickHouse-Iceberg 0.378 s). "No single engine wins; pick the engine for the query shape."
- **Literature Support**: complements H-ARCH-01 (Iceberg-as-substrate) and H-ARCH-02 (multi-engine inevitability) — specialization is *why* multi-engine is forced
- **Note**: first-party (self-authored SDW Lab — label as such, not external citation); magnitudes host-specific, the per-shape ordering is the transferable claim
- **Status**: VALIDATED (first-party Tier B)

---

## Gap 1: Operational TCO Reality (NEW HYPOTHESIS NEEDED)

### Literature Evidence

**Source 1**: IDC - Hidden Costs of Real-Time Data [^59]
- **Finding**: 2.5-3× higher operational staffing costs for streaming
- **Cause**: Specialized expertise + 24/7 support requirements

**Source 2**: Enterprise Data Quarterly - Streaming TCO [^57]
- **Finding**: 1.5-2× higher infrastructure costs
- **Cause**: Redundancy requirements, continuous processing overhead

**Source 3**: DevOps Enterprise Summit - Incident Economics [^60]
- **Finding**: Streaming incidents cost 3-4× more annually
- **Cause**: Business impact, resolution complexity, off-hours response

### Proposed Hypothesis

**H-IMPL-01: Streaming Architecture Hidden Costs**

**Hypothesis**: Real-time streaming architectures incur 2.5-3× higher operational costs than equivalent batch architectures due to specialized staffing (2.7× more staff), higher infrastructure redundancy (1.5-2× costs), and incident management complexity (3-4× annual costs).

**Evidence Level**: A (IDC, DORA, Enterprise Data Quarterly)

**Status Update (v1.6.0 - Oct 15, 2025)**: ✅ **STRONGLY VALIDATED**
- Blog post "The Streaming Tax" synthesized 8 Level A sources with convergent validation
- 3-year TCO comparison quantified: Batch $2.5M vs Self-Managed Streaming $7.9M (3.2× multiplier)
- Break-even analysis: 6.3 years (conservative), 1.3 years (high-value ops)
- Evidence bundles: cost-reality-reference.md, staffing-budget-calculator.md

**Relevance**:
- Book Chapter 4 (Implementation journeys - TCO reality)
- Book Chapter 7 (Ingestion - streaming vs batch decision)

**Validation Needed**:
- [ ] Security-specific TCO comparison (streaming SIEM vs batch lake)
- [ ] Practitioner interviews on hidden operational costs
- [ ] Quantify 24/7 support premium

**Impact**: **CRITICAL** - Affects architectural decision framework, sets realistic expectations

---

## Gap 2: Streaming Staffing Specialization (NEW HYPOTHESIS NEEDED)

### Literature Evidence

**Source 1**: DORA 2024 State of DevOps [^31], [^33], [^43]
- **Finding 1**: 2.7× operational staff for streaming vs batch
- **Finding 2**: Fault-tolerance = "Level 4" specialized skill (top 5% orgs only)
- **Finding 3**: 3.2× higher incident rates for streaming

**Source 2**: DevOps.com / Ververica [^5], [^6]
- **Finding**: 3.2 average FTEs required for Flink pipelines
- **Timeline**: 4-9 months implementation

**Source 3**: MIT Technology Review [^61]
- **Finding**: 1.5-2× higher training investments
- **Cause**: Specialized skill requirements, continuous learning

### Proposed Hypothesis

**H-IMPL-02: Streaming Expertise Scarcity**

**Hypothesis**: Enterprise-grade stream processing requires specialized expertise available in <15% of organizations (Gartner [^41]), necessitating 2.7× larger operations teams (DORA [^31]) and 4-9 month implementation timelines (Ververica [^6]) even with experienced staff.

**Evidence Level**: A (DORA, Gartner, Ververica)

**Status Update (v1.6.0 - Oct 15, 2025)**: ✅ **STRONGLY VALIDATED**
- Staffing-budget-calculator.md: Batch 3.5 FTEs vs Streaming 9-11 FTEs (2.6-3.1× validated)
- Blog post quantified Tax #1 (Staffing): $1,304,000/year cost for 2.7× multiplier
- Implementation timeline: 3-7 months typical, 4-9 months with "Level 4" skills scarcity
- Evidence bundles: staffing-budget-calculator.md, implementation-reality-reference.md

**Relevance**:
- Book Chapter 4 (Journey 2: Streaming-first architect - staffing reality)
- Book Chapter 7 (Streaming implementation considerations)

**Validation Needed**:
- [ ] Security-specific staffing surveys
- [ ] Expert interviews (Lisa Cao, Jake Thomas on team composition)
- [ ] Quantify skills gap in security domain

**Impact**: **HIGH** - Affects staffing plans, implementation timelines, architectural choices

---

## Gap 3: Security-Specific Implementation Timelines (NEW HYPOTHESIS NEEDED)

### Literature Evidence

**Source 1**: SANS Institute - Security Analytics Implementation [^51]
- **Finding**: Security-specific timelines differ from general data engineering
- **Implication**: Security-specific constraints (compliance, change control, threat landscape)

**Source 2**: Gartner - Security Data Platforms [^12], [^138]
- **Finding**: 5.5 month average for security-focused lakehouse
- **Comparison**: General lakehouse 6-12 months

**Source 3**: Managed Kafka - Practitioner Experiences [^10]
- **Finding**: 3-6 months for production Kafka in security ops
- **Context**: Managed services, not self-hosted

### Proposed Hypothesis

**H-IMPL-03: Security Implementation Timeline Premium**

**Hypothesis**: Security-focused data platform implementations require 15-30% longer timelines than general data engineering due to compliance requirements, security change control processes, and threat-informed architecture decisions (SANS [^51], Gartner [^138]).

**Evidence Level**: B (SANS, Gartner - need more security-specific validation)

**Relevance**:
- Book Chapter 4 (All three journeys - realistic timeline expectations)
- PLAN.md priority engagements (CISA, expert network validation)

**Validation Needed**:
- [ ] SOC manager survey: Implementation timeline experiences
- [ ] CISA partnership: Government security implementation patterns
- [ ] Practitioner case studies (security-specific vs general)

**Impact**: **HIGH** - Sets realistic expectations, prevents timeline underestimation

---

## Gap 4: Tiered Storage Cost Optimization Patterns (NEW HYPOTHESIS NEEDED)

### Literature Evidence

**Source 1**: Netflix - Kafka Tiered Storage [^70]
- **Finding**: 70-80% storage cost reduction for multi-year retention
- **Technology**: Kafka tiered storage (S3 backend)

**Source 2**: AWS Storage Optimization [^15]
- **Finding**: 55% average savings with tiered strategies
- **Pattern**: Hot/warm/cold lifecycle management

**Source 3**: Confluent - Tiered Storage Documentation [^78], [^79]
- **Validation**: Substantial cost reduction confirmed
- **Technology maturity**: Kafka 3.0+ native support

### Proposed Hypothesis

**H-COST-09: Tiered Storage Economics**

**Hypothesis**: Implementing tiered storage architectures (hot/warm/cold) for security data reduces storage costs by 55-80% (AWS [^15], Netflix [^70]) while maintaining compliance retention requirements, with Kafka tiered storage and Iceberg lifecycle policies as primary implementation patterns.

**Evidence Level**: A (Netflix production, AWS whitepapers, Confluent documentation)

**Status Update (v1.6.0 - Oct 15, 2025)**: ✅ **VALIDATED**
- Cost-optimization-playbook.md: Strategy #1 (Tiered Storage) with 55-80% savings validated
- 15-23× ROI for quick wins (tiered storage, right-size reliability, avoid premature streaming)
- Total potential savings: $2M-4M/year for mid-sized operations
- Evidence bundles: cost-optimization-playbook.md, cost-reality-reference.md

**Relevance**:
- Book Chapter 1 (Cost comparisons - storage optimization)
- Book Chapter 7 (Ingestion - Kafka tiered storage)
- Book Chapter 8 (Storage formats - Iceberg lifecycle)

**Validation Needed**:
- [ ] Security-specific validation (compliance + tiering)
- [ ] Cost models: SIEM vs tiered lake
- [ ] Access pattern analysis (security workloads)

**Impact**: **HIGH** - Direct cost optimization opportunity, validates modern stack economics

---

## Gap 5: Kafka Streams for Security Operations (NEW HYPOTHESIS NEEDED)

### Literature Evidence

**Source 1**: LinkedIn Security - State Management [^68]
- **Finding**: Terabytes of state with millisecond access
- **Production**: Security implementation at scale

**Source 2**: Uber - Real-Time Security Views [^69]
- **Finding**: Thousands of real-time views, sub-second refresh
- **Technology**: Kafka Streams for security ops

**Source 3**: Nordstrom - Security Analytics [^86]
- **Finding**: Latency reduction for security operations
- **Pattern**: Stateful stream processing for entity tracking

**Source 4**: Confluent - Security Analytics Patterns [^83-85], [^87]
- **Capabilities**: Exactly-once semantics, stateful processing, sub-250ms latency
- **Security Use Cases**: Entity-based analytics, threat detection

### Proposed Hypothesis

**H-STREAM-01: Kafka Streams Security Patterns**

**Hypothesis**: Kafka Streams enables production-grade security analytics with stateful entity tracking (LinkedIn [^68]), sub-second detection latency (Uber [^69], Confluent [^85]), and exactly-once semantics critical for alert fidelity, representing a viable alternative to dedicated stream processors (Flink) for many security use cases.

**Evidence Level**: A (LinkedIn, Uber, Nordstrom production deployments)

**Relevance**:
- Book Chapter 7 (Ingestion - streaming options)
- Book Chapter 4 (Journey 2: Streaming-first - Kafka Streams path)

**Validation Needed**:
- [ ] Security-specific use case catalog (detection, enrichment, response)
- [ ] Kafka Streams vs Flink decision framework
- [ ] Practitioner adoption patterns

**Impact**: **MEDIUM** - Expands streaming implementation options, reduces complexity

---

## Gap 6: DuckDB Edge/Embedded Processing (FORMALIZE EXISTING WORK)

### Literature Evidence

**Source 1**: DuckDB Labs - Official Documentation [^144]
- **Positioning**: Embedded analytics, SQLite alternative
- **Capabilities**: Analytical SQL without external database

**Source 2**: Expert Network - Jake Thomas (Okta)
- **Context**: Production DuckDB deployment for security data
- **Use Case**: Defensive cyber operations at scale
- **Status**: Interview scheduled (Week 3 per PLAN.md)

### Current Status

**Existing Knowledge Base**: `01-knowledge-base/duckdb-edge-processing-patterns.md`
- Created October 10, 2025
- Source: Jake Thomas case study + emerging patterns

**Missing**: Formal hypothesis in MASTER-HYPOTHESIS-TRACKER.md

### Proposed Hypothesis

**H-EDGE-01: DuckDB for Edge Security Analytics**

**Hypothesis**: DuckDB enables edge/endpoint security analytics with embedded analytical queries, eliminating network round-trips for local investigation while maintaining OLAP-grade performance, validated by production defensive cyber operations deployments (Jake Thomas, Okta).

**Evidence Level**: B (Expert validation in progress, official documentation)

**Relevance**:
- Book Chapter (Emerging patterns)
- Expert network validation (Jake Thomas interview Week 3)
- Blog post: "DuckDB at Scale: Production Deployments for Defensive Cyber Ops"

**Validation Needed**:
- [ ] Jake Thomas interview (Week 3) - architecture details
- [ ] Production deployment patterns
- [ ] Performance benchmarks for security workloads

**Impact**: **MEDIUM** - Emerging pattern, differentiates from traditional architectures

---

## Gap 7: Table Format Interoperability (EMERGING - TRACK)

### Literature Evidence

**Source 1**: Apache XTable Documentation [^140], [^146]
- **Capability**: Table format interoperability layer (Iceberg ↔ Delta ↔ Hudi)
- **Status**: Apache incubator project

**Source 2**: Gartner Enterprise Survey [^147]
- **Finding**: 64% of architects concerned about table format lock-in
- **Mitigation**: 42% cite XTable as risk mitigation

### Assessment

**Current Hypothesis Coverage**: None directly addressing format portability

**Recommendation**: **TRACK, NOT FORMALIZE YET**

**Rationale**:
- Emerging standard (incubator)
- Adoption unclear (Gartner survey shows interest, not production usage)
- Lisa Cao interview (Week 3) may provide adoption insights

**Action**:
- [ ] Lisa Cao validation: Gravitino + XTable relationship
- [ ] Monitor Apache XTable graduation status
- [ ] Track production adoption (6-12 month timeline)

**Impact**: **LOW (currently)** - Emerging, not production-proven

---

## Gap 8: ClickHouse Security-Specific Optimizations (EXTEND EXISTING)

### Literature Evidence (Beyond General Performance)

**Source 1**: ClickHouse IP Address Types [^101]
- **Finding**: 50-100× faster CIDR-based threat hunting
- **Technology**: Native IPv4/IPv6 types

**Source 2**: Altinity - Security Analytics [^107-108]
- **Finding 1**: 75-85% storage reduction vs document databases
- **Finding 2**: 70% reduction in mean time to investigation
- **Finding 3**: 40% analyst productivity increase

**Source 3**: Percona - Time Series Optimization [^102]
- **Finding**: Time-series optimizations for security event data
- **Use Case**: Temporal query patterns

### Current Hypothesis

**H3-PERFORMANCE-01: ClickHouse OLAP Performance** - EXISTS, well-validated

**Gap**: Security-specific optimizations not explicitly called out

### Proposed Extension

**H3-PERFORMANCE-01 (Extended)**: Add security-specific subsection:

**Security-Specific Advantages**:
- Native IP types: 50-100× faster CIDR threat hunting ([^101])
- Storage efficiency: 75-85% reduction vs Elasticsearch ([^107])
- Analyst productivity: 40% increase, 70% faster investigations ([^108])
- Time-series optimization for security events ([^102])

**Evidence Level**: A (production deployments, quantitative benchmarks)

**Impact**: **MEDIUM** - Strengthens ClickHouse case for security use cases

---

## Recommended Actions

### Immediate (Week 1-2)

**1. Formalize Critical Hypotheses**:
- [ ] H-IMPL-01: Streaming Architecture Hidden Costs (TCO reality)
- [ ] H-IMPL-02: Streaming Expertise Scarcity (staffing 2.7×)
- [ ] H-IMPL-03: Security Implementation Timeline Premium
- [ ] H-COST-09: Tiered Storage Economics (55-80% savings)
- [ ] H-STREAM-01: Kafka Streams Security Patterns

**Add to**: `01-knowledge-base/MASTER-HYPOTHESIS-TRACKER.md`

**2. Extend Existing Hypothesis**:
- [ ] H3-PERFORMANCE-01: Add security-specific subsection (ClickHouse)

**3. Formalize Emerging Work**:
- [ ] H-EDGE-01: DuckDB Edge Processing (link to existing knowledge base doc)

### Expert Network Validation (Week 3)

**Lisa Cao Interview**:
- [ ] Gravitino adoption metrics (Gap 3 in master tracker)
- [ ] Table format interoperability (XTable) - production usage?
- [ ] Catalog proliferation management

**Jake Thomas Interview**:
- [ ] DuckDB production architecture (H-EDGE-01 validation)
- [ ] Security data volume validation (H1-VOLUME-07)
- [ ] Edge processing patterns

### Ongoing Monitoring

**Completed Actions**:
- ✅ All 283 footnotes extraction complete (October 10, 2025)
- ✅ Archive manuscript parts 1-5 assessed (no independent sources)
- ⏳ Expert network interviews scheduled (Lisa Cao, Jake Thomas - Week 3)

**Future Gap Monitoring**:
- Expert network interviews may reveal additional hypothesis gaps
- Quarterly literature updates may identify emerging patterns
- IT Harvest partnership data may surface vendor-specific hypotheses

---

## Impact Assessment

### Critical for Book Quality

**HIGH IMPACT** (Must formalize):
1. H-IMPL-01: TCO Reality - Prevents unrealistic cost expectations
2. H-IMPL-02: Staffing Reality - Prevents timeline/resource underestimation
3. H-COST-09: Tiered Storage - Validates cost optimization claims

**MEDIUM IMPACT** (Should formalize):
4. H-IMPL-03: Security Timelines - Sets realistic implementation expectations
5. H-STREAM-01: Kafka Streams - Expands architectural options
6. H-EDGE-01: DuckDB - Emerging pattern, differentiator

**LOW IMPACT (currently)**:
7. XTable Interoperability - Track, don't formalize yet (emerging)

### Hypothesis Tracker Stats (After Additions)

**Current**: 26 hypotheses
**Proposed Additions**: +6 critical hypotheses
**New Total**: 32 hypotheses
**Evidence Level A Target**: 24 of 32 (75%) - achievable with literature base

---

## Gap 9: Isolation-First Security Architecture Patterns (NEW - November 2025)

### Literature Evidence

**Source 1**: Netflix Security Observability Platform
- **Finding**: ClickHouse + Iceberg on isolated VPC with Polaris (table-level RBAC only)
- **Implication**: No row-level security, column masking, or metadata encryption needed
- **Evidence Level**: A (Production deployment at scale)

**Source 2**: Huntress EDR Data Lake
- **Finding**: Iceberg on isolated AWS infrastructure, table-level RBAC
- **Implication**: Simplified security posture, avoided Unity Catalog complexity
- **Evidence Level**: A (Production case study, 93% cost reduction)

**Source 3**: Okta Security Analytics
- **Finding**: DuckDB + Iceberg on isolated platform (Jake Thomas validation)
- **Implication**: Performance-first approach without fine-grained access overhead
- **Evidence Level**: B (Expert validation)

**Source 4**: Databricks Unity Catalog Overhead
- **Finding**: Row-level security, column masking, metadata encryption add query overhead
- **Implication**: 15-50% performance penalty when isolation could suffice
- **Evidence Level**: B (Vendor documentation, benchmarks needed)

**Source 5**: Alex Merced (Dremio) - Iceberg Metadata Encryption
- **Finding**: Metadata encryption adds 10-20% query latency overhead
- **Implication**: Avoidable for isolated security platforms
- **Evidence Level**: B (Vendor expert, quantitative estimates)

### Proposed Research Questions

**RQ7: Isolation Patterns and Performance**
- **Hypothesis**: Network isolation + IAM provides sufficient security boundary, achieving 15-50% faster query performance vs fine-grained catalog access
- **Evidence Level**: B (production validation needed)
- **Relevance**: Book Chapter 8 (Storage formats - Iceberg), Chapter 9 (Query engines - catalog selection)
- **Validation Needed**:
  - [ ] Query latency benchmarks: Unity Catalog RLS vs Polaris table-level RBAC
  - [ ] TCO comparison: Polaris/Nessie (open-source) vs Unity Catalog (licensed)
  - [ ] Operational hours: RLS policy management vs table-level permissions

**RQ8: Compliance Trade-offs of Isolation-First Architecture**
- **Hypothesis**: Network isolation as primary control meets SOC 2/ISO 27001/NIST CSF for most enterprise security teams
- **Evidence Level**: B (compliance framework mapping needed)
- **Relevance**: Book Chapter 11 (Governance), compliance guidance
- **Validation Needed**:
  - [ ] ISO 27001 control mapping: Network isolation vs catalog RLS
  - [ ] SOC 2 audit acceptance: CloudTrail (table-level) vs Unity Catalog (row-level)
  - [ ] Regulatory gap analysis: When is fine-grained access still required?

**RQ9: Multi-Tenant MSSP vs Isolation-First Architecture**
- **Hypothesis**: Multi-tenant MSSPs require row-level security, single-tenant SOCs benefit from isolation-first
- **Evidence Level**: B/C (MSSP case studies needed)
- **Relevance**: Book Chapter 4 (Architectural decision framework), MSSP market landscape
- **Validation Needed**:
  - [ ] MSSP case studies: Arctic Wolf, Expel, Red Canary architecture patterns
  - [ ] Cost per tenant: Unity Catalog DBU costs vs dedicated VPC per customer
  - [ ] Scale thresholds: When does multi-tenant become more cost-effective?

**RQ10: Isolation Patterns Influence on Catalog Governance**
- **Hypothesis**: Isolation-first elevates Polaris/Nessie to top-tier (vendor neutrality, Git workflows prioritized over fine-grained access)
- **Evidence Level**: B (catalog adoption patterns)
- **Relevance**: Book Chapter 8 (Storage formats - catalog selection), Chapter 9 (Query engines)
- **Validation Needed**:
  - [ ] Netflix Polaris adoption rationale (vendor-neutral, isolated platform)
  - [ ] Unity Catalog → Polaris migration patterns (when isolating infrastructure)
  - [ ] Decision criteria ranking: Fine-grained access vs vendor lock-in vs version control

**Impact**: **HIGH** - Foundational architectural pattern affecting catalog selection, TCO, performance, and compliance decisions across all security data architectures.

---

## Summary

**Finding**: Literature extraction reveals **10 critical hypothesis gaps** (6 original + 4 isolation-first security), primarily around operational reality (TCO, staffing, timelines), cost optimization (tiered storage), and architectural patterns (isolation-first security).

**Strategic Importance**: These gaps address the **"hidden costs"**, **"implementation reality"**, and **"architectural decision patterns"** that differentiate security-specific data architecture from general data engineering - critical for book credibility and practitioner utility.

**Next Action**:
1. ✅ Add 6 original hypotheses to MASTER-HYPOTHESIS-TRACKER.md (COMPLETE)
2. ✅ Add RQ7-RQ10 to METHODOLOGY.md (COMPLETE - November 2025)
3. Track isolation-first security evidence collection (November 2025 monthly update)

---

## Gap 10: AI/Agent Architectures for Security Analytics (NEW - December 2025)

### Literature Evidence

**Source 1**: AI Governance Maturity Gate (Rogojan, Wernfeldt - Dec 2025)
- **Finding**: AI initiatives fail at orgs with poor data governance (<5% success at Level 1)
- **Implication**: AI amplifies existing governance gaps by 10×
- **Evidence Level**: B (Practitioner consensus)

**Source 2**: RAPTOR Framework (Gadi Evron - Dec 2025)
- **Finding**: "Duct tape MVP" AI agent successfully patches vulnerabilities
- **Implication**: Practical AI security automation possible with simple infrastructure
- **Evidence Level**: B (Production demonstration)

**Source 3**: NANDA Infrastructure (MIT Media Lab - 2024-2025)
- **Finding**: "DNS for AI agents" enabling trillions of agent interactions
- **Implication**: Agent-to-agent coordination requires foundational infrastructure
- **Evidence Level**: A (MIT research, 10 years development)

**Source 4**: AI-Generated Parsers (Tenzir - Nov-Dec 2025)
- **Finding**: AI generates complete OCSF parsers from log samples
- **Implication**: Shifts integration control from vendors to customers
- **Evidence Level**: B (Production validation)
- **Measured follow-up (2026-06-14, #10)**: generating a mapping is not the same as a field-faithful one. Tenzir's *shipped* `zeek::ocsf::map` is class-right but derives `activity_id` on only 17% of records (83% mis-bucketed) and covers 1 of 4 common sources; this measurement is what re-tiers the RQ14 OCSF/parser legs from asserted-A to Tier-B (see OVERTURN under RQ14).

### Gap 10 Summary

The emergence of AI/agent architectures requires formal research questions to be addressed in Gap 11.

**Impact**: **EMERGING HIGH** - Foundational for next-generation security architectures

---

## Gap 11: Formal Research Questions RQ11-RQ14 (December 2025)

### RQ11: LIGER Stack vs Traditional SIEM Architecture

**Research Question**: Can the LIGER Stack architecture achieve a 60-80% median cost reduction (up to 90%+ in optimal conditions) vs traditional SIEMs while maintaining comparable security detection and investigation capabilities?

**Hypothesis**: The LIGER Stack (Lakehouse + Index + Graph + Engine + Route) reduces total cost of ownership by **60-80% (median), up to 90%+ in optimal conditions**, compared to traditional SIEMs through:
- Storage/compute separation ($0.023/GB/month S3 vs bundled SIEM pricing)
- Compression, but **workload-dependent**: the SDW lab measured the storage byte ratio spanning **~2.6× (high-entropy: base64 payloads, full SHA-256, per-event GUIDs) → 7.9× (EDR/Sysmon proc-creation) → 8.5× (flat Zeek conn)** on a pinned 10M-row corpus (`~/sdw-lab-benchmarks/cost-to-serve-retention/`, commit 3d0539a, Tier B). The headline "10-12×" holds only for moderate-entropy schemas; high-entropy ingest compresses ~3.3× worse, so per-event cost must be re-based on the workload's own raw bytes/event, not a single assumed ratio.
- Fixed compute costs (no per-query charges)
- Vendor-neutral architecture (avoiding lock-in premiums)

**Evidence Level**: A on direction and the production-cluster anchors; the **60-80% median band is Tier C** (Jeremy's own TCO model) anchored to **Tier-B first-party byte ratios** (2.6-8.5×) plus **primary-verified production-cluster economics** (Netflix Iceberg+ClickHouse 5 PB/day hot, 1+ EB Iceberg, $5/TB DataFusion compaction; Rippling $4.50/mo per CloudTrail detection — both Reproducible/Tier B in the 2026-06-14 Gemini reconciliation; Atlassian/Project Banyan 80% ingest-cost reduction, Asserted/public Databricks figure).

**Current Evidence**:
- LIGER: $3,560/month for 500GB/day with 365-day retention
- Azure Sentinel: $31,000-35,000/month (same volume/retention)
- Splunk Enterprise TCO: $54,167-100,000/month
- Compression validated: 10-12× (Huntress, Shell, Cloudflare cases)

**January 2026 Research Update** ✅:
- **Barracuda Networks**: 75% reduction in daily processing and storage costs (Databricks)
- **Palo Alto Networks**: 3× faster AI-powered threat detection (Databricks)
- **GitLab**: Queries over 100M rows reduced from 30-40s to <1s (ClickHouse)
- **Netflix**: 5 PB/day log ingestion pipeline (ClickHouse)
- **HSBC**: 3× more threat hunts with lower TCO (Databricks Lakehouse)
- **50% of world's 15 largest banks** using security data lakes (Hunters)
- **Forrester**: CISOs voting with budget for data-first architecture
- **OCSF**: 900+ contributors, 200+ orgs, Linux Foundation Project (Nov 2024)

**Cost-reduction range reconciliation (2026-06-14)**: across the lit-review the cost-reduction claim drifted (RQ11 "70-90%", RQ13 "50-70%", tiered-storage "55-80%", book "71-96%"). Standardized on **60-80% median, up to 90%+ in optimal conditions**, anchored to the lab byte ratios (re-measure per workload — the high-entropy ~2.6× floor keeps the range honestly workload-dependent rather than a universal constant) and the production-cluster anchors above. The per-deployment percentages cited here (Barracuda 75%, HSBC 3×, Atlassian/Banyan 80%) are individual operator outcomes, not the median — they sit inside the band but are point cases, mostly Tier-C/Asserted vendor cases except the Reproducible Netflix/Rippling anchors.

**Validation Metrics**:
- [x] TCO comparison across 10+ production deployments (Barracuda, HSBC, Netflix, GitLab, 50% top banks)
- [x] Query performance benchmarks (GitLab: 30-40s → <1s; ClickHouse 3-5× faster than Snowflake)
- [ ] Detection coverage comparison (rules ported successfully)
- [ ] Analyst satisfaction scores (usability study)
- [ ] Migration effort quantification (person-months)

**Relevance**: Book Chapters 1 (Reality Check), 9 (Security Architecture), 16 (Business Case)

---

### RQ12: AI/Agent Governance Maturity Gates

**Research Question**: What is the minimum data governance maturity level required for successful AI/agent deployment in security operations?

**Hypothesis**: Organizations require Data Governance Maturity Level 3+ (Defined) to achieve >40% success rate with AI security initiatives, with failure rates of:
- Level 1 (Chaos): <5% success
- Level 2 (Awareness): 15-25% success
- Level 3 (Defined): 40-60% success
- Level 4 (Managed): 70-85% success
- Level 5 (Optimized): >90% success

**Evidence Level**: A (CSA/Google Cloud survey + SANS Institute + practitioner consensus)

**Current Evidence**:
- AI amplifies governance gaps by 10× (poor data → hallucinations)
- Multiple practitioner validation (Rogojan, Wernfeldt)
- "6-month rule": Organizations not willing to fix governance first will fail

**January 2026 Research Update** ✅ **MAJOR VALIDATION**:
- **CSA/Google Cloud Survey** (Dec 2025): "Governance maturity stands out as the strongest indicator of AI readiness"
- **Only 26%** of organizations have comprehensive AI security governance
- **54%** use public frontier LLMs, **60%** plan agentic AI within 12 months
- Organizations with **comprehensive policies**: 46% early agentic AI adoption
- Organizations with **policies in development**: only 12% adoption (3.8× difference)
- Sensitive data exposure ranks as leading AI security concern
- **SANS Institute**: Implement AI incrementally in non-critical systems first
- **SANS**: Adopt enterprise AI policies with centralized governance boards

**Validation Metrics**:
- [x] Survey 50+ organizations on governance level vs AI success (CSA/Google: industry-wide survey)
- [x] Quantitative governance-success correlation (46% vs 12% adoption rate by maturity)
- [ ] Develop formal maturity assessment framework
- [ ] Quantify failure costs (wasted investment analysis)
- [ ] Document success patterns at each maturity level
- [ ] ROI model: Governance investment vs AI returns

**Relevance**: Book Chapter 17 (Future Predictions), Appendix D (Readiness Assessment)
**Interview Prep**: Use CSA findings in Lisa Cao and Jake Thomas interviews

---

### RQ13: Pipeline vs Query-Based Detection Economics

**Research Question**: Under what conditions does pipeline-based detection provide superior economics compared to query-based detection for security operations?

**Hypothesis**: Pipeline-based detection achieves 10-50× cost reduction when:
- Detection logic can be defined upfront (known patterns)
- Real-time alerting required (<1 minute latency)
- High-volume, low-value data sources (DNS, web logs, Windows events)
- Limited investigation requirements (detection-heavy vs investigation-heavy SOC)

**Evidence Level**: A (Quantitative production data from multiple sources)

**Current Evidence**:
- Pipeline detection: Store signals only (100× data reduction possible)
- Query-based: Store everything (10× compression only)
- Hybrid approach: High-value sources stored, high-volume sampled
- Cost difference: $700/month (pipeline) vs $7,000/month (query-based) for 1TB/day

**February 2026 Research Update** ✅:
- **Security data pipeline market**: Cribl $200M ARR (Feb 2025), fastest cybersecurity company to $100M ARR
- **Pipeline filtering**: 50-70% log volume reduction without losing visibility (SACR Market Guide 2025) — note this is a *volume*-reduction figure, distinct from the LIGER TCO band; volume reduction is one input to TCO, not the same quantity
- **SIEM ingestion reducible by 80%+** with pipeline pre-ingest processing
- **Cost-per-detection**: $4.50/month per detection rule on Snowflake serverless (Rippling production)
- **Okta case study**: 50.7% cost reduction ($1,929→$952/month) via pipeline filtering (Monad)
- **Storage differential**: SIEM ~$25/GB/day vs S3 $0.023/GB/month (1,087× cost gap)
- **Counterpoint**: Query-based with serverless (Snowflake) can be cost-effective at $4.50/month/rule
- **Security telemetry** doubling every ~18 months; traditional volume-based SIEM pricing "unsustainable"

**Validation Metrics**:
- [x] Cost modeling across 5 detection strategies (pipeline filtering, serverless query, tiered storage)
- [ ] False positive/negative rates for pipeline vs query
- [ ] Investigation impact analysis (sampled vs complete data)
- [ ] Regulatory compliance verification
- [x] Performance benchmarks (latency <1 min Snowpipe, 50-70MB/5min query scans)

**Cost-band reconciliation (2026-06-14)**: where this RQ touches *overall* TCO reduction (vs the pipeline *volume*-reduction and the per-detection $/rule figures above, which are their own measured quantities), it inherits the standardized **60-80% median, up to 90%+ optimal** band from RQ11 — anchored to the lab byte ratios (2.6-8.5×, re-measure per workload) and the production-cluster economics. The "10-50× cost reduction" multiplier in the hypothesis is conditions-specific (pipeline-able known patterns, high-volume/low-value sources) and is not the same quantity as the TCO band; keep the two distinct.

**Relevance**: Book Chapters 6 (Stream Processing), 9 (Security Architecture), 13 (Detection Engineering)

---

### RQ14: Agentic Security Automation ROI

**Research Question**: What is the return on investment for deploying AI agents in security operations, and what tasks can be successfully automated?

**Hypothesis**: AI agents can successfully automate 20-40% of Level 1 SOC tasks with positive ROI within 12 months, specifically:
- Parser generation (a vendor can ship an AI-generated OCSF mapping, but shipped ≠ field-faithful — see the OVERTURN note below)
- Vulnerability patching (RAPTOR framework validation)
- Initial triage and enrichment (30-40% reduction in analyst time)
- OCSF normalization (availability of a shipped mapping is the binding constraint, not an 80%-achievable automation rate — see the OVERTURN note)

**Evidence Level**: A on the ROI/triage legs (Google Cloud survey); **Tier B (measured) on the two OCSF/parser legs after the 2026-06-14 overturn** — see below.

> **OVERTURN — 2026-06-14 (first-party measurement supersedes the asserted "Parser generation 100% automation / OCSF normalization 80% achievable, Evidence Level A").** ⚠️ **Re-tiering of a published asserted-A confidence level — flagged for Jeremy's sign-off before any downstream surface cites it.**
>
> The asserted Level-A claim ("100% automation via Tenzir MCP" / "80% OCSF normalization achievable") was never a measurement — it was an inference from the *existence* of an AI-generated mapping. The SDW lab's pipeline-normalization-fidelity bench (#10) ran Tenzir's **shipped** library mapping `zeek::ocsf::map` unedited over a pinned corpus and measured what it actually delivers (`~/sdw-lab-benchmarks/pipeline-normalization-fidelity/FINDINGS-2026-06-14.md`, commit 20cf84c). Two things the asserted claim got wrong:
> - **Fidelity is not coverage.** On the one source Tenzir ships a JSON-consumable mapping for (Zeek conn), the mapping gets the OCSF *class* right (100%, Network Activity 4001) and most *values* (92%), but it does **not** derive `activity_id` from Zeek's `conn_state`, so the activity classification diverges from the faithful gold on **83% of records** (activity_id 17%), and `history` / `service` / `uid` land in `unmapped` rather than typed OCSF attributes (field fidelity 80%). A consumer filtering on `activity_id` (open vs close vs reset vs fail) mis-buckets most connections. "Maps to OCSF" is a coverage claim, not a fidelity guarantee.
> - **Availability is the binding constraint.** Tenzir ships **0% consumable coverage for 3 of the 4 common sources** tested — CloudTrail (no management-events → API Activity operator in the `amazon` package), Sysmon (the shipped `sysmon::ocsf::map` expects raw EVTX/XML, not the pre-parsed JSON most EDR shippers carry), and a generic auth source (no vendor ships a mapping). The second tool, **Vector 0.56.0, ships no OCSF mapping at all** (no OCSF component, function, or binary string), so this is a cross-tool finding, not a Tenzir quirk. Of the two open tools tested, one ships a usable mapping for one of four sources and the other ships none.
>
> **Re-tier:** from *asserted Level A* to a **measured Tier-B caveat** — *coverage is a claim, fidelity is not; shipped-mapping availability is the binding constraint on OCSF-normalization-at-source.* **Version-bound:** Tenzir **6.0.0**, library commit **671e049**, OCSF **1.8.0**, synthetic corpus, single host — re-run on a newer library before repeating. The Cribl arm (the one tool advertising a packaged OCSF Pack) is deferred and would test whether the availability gap is tool-specific or general. This is the same lineage as biblio entry #86, where a fabricated Tenzir "100% hands-off" was already corrected to "100% schema-conforming." Per-vendor percentages stay OUT of public surfaces (Matrix-paid IP); public statements carry the principle and shape only.

**Current Evidence**:
- RAPTOR: Successfully patches vulnerabilities ("duct tape MVP" works)
- Tenzir: AI generates complete OCSF parsers from samples — but the *shipped* library mapping is class-right/activity-wrong on 83% of Zeek-conn records and absent for 3 of 4 common sources (measured, #10, Tier B; see OVERTURN)
- NANDA: 1,000+ agents registered, infrastructure emerging
- Practitioner reports: AI assists but doesn't replace analysts

**January 2026 Research Update** ✅:
- **Google Cloud Survey** (Sep 2025): 52% of executives deploying AI agents in production
- **74% achieve ROI within first year** (Google Cloud)
- **39%** have deployed more than 10 agents across enterprise
- **Average ROI projection**: 171% (AI Multiple Research)
- **U.S. enterprises**: 192% ROI (3× traditional automation)
- **70% cost reduction** achievable with agentic AI systems
- **MTTD target**: <5 minutes for high severity (Obsidian Security)
- **MTTR automation target**: <10 minutes (Obsidian Security)
- **Target**: <2% false positive rate to avoid alert fatigue

**Validation Metrics**:
- [x] 12-month ROI validation (74% achieve ROI in first year - Google Cloud) — ROI/triage legs only
- [x] ROI quantification (171% average, 192% U.S. enterprises) — ROI/triage legs only
- [x] Time-to-value measurements (parser generation: manual vs AI) — REFRAMED by #10: the gating metric is shipped-mapping *availability + fidelity*, not generation speed (Tenzir: 1 of 4 sources covered, activity_id 17% on the covered one; Vector: none)
- [ ] Task automation taxonomy (what can/cannot be automated) — #10 narrows "OCSF normalization" from "80% achievable" to "coverage ≠ fidelity, availability-bound"
- [ ] Error rates and human oversight requirements
- [ ] Training data requirements and costs

**Relevance**: Book Chapter 17 (Future Predictions), Chapter 13 (Detection Engineering)

---

## Summary of RQ11-RQ14

These formal research questions address critical gaps in the literature:

1. **RQ11 (LIGER Stack)**: Validates the complete reference architecture; cost-reduction claim standardized 2026-06-14 to **60-80% median, up to 90%+ optimal** (anchored to lab byte ratios 2.6-8.5× + production-cluster economics), replacing the looser "70-90%"
2. **RQ12 (AI Governance)**: Establishes prerequisites for AI success in security operations
3. **RQ13 (Detection Economics)**: Quantifies pipeline vs query-based detection trade-offs
4. **RQ14 (Agent ROI)**: Documents practical automation opportunities and returns

**Total Research Questions**: RQ1-RQ10 (existing) + RQ11-RQ14 (new) = 14 formal research questions (later extended to 17 with RQ15-RQ17 — see Gap 12)

**January 2026 Evidence Status**:
| RQ | Status | Key Evidence Added |
|----|--------|-------------------|
| RQ11 | ✅ STRONG | Barracuda 75%, HSBC 3×, GitLab <1s, Netflix 5PB/day, 50% top banks |
| RQ12 | ✅ STRONG | CSA/Google survey: 46% vs 12% adoption by governance maturity |
| RQ13 | ✅ STRONG | Pipeline 50-70% cost reduction, $4.50/rule serverless, 1,087× storage gap |
| RQ14 | ✅ STRONG (ROI legs) · ⚠️ RE-TIERED (OCSF/parser legs) | Google 74% first-year ROI, 171% average, 192% U.S. enterprises. **OCSF/parser legs overturned 2026-06-14**: asserted-A "100% parser automation / 80% OCSF normalization" → measured Tier-B caveat (Tenzir #10: class-right/activity-wrong-on-83%, 1 of 4 sources covered; Vector ships none). Coverage ≠ fidelity; availability is the binding constraint. |

**Evidence Collection Priority** (Updated):
- **VALIDATED**: RQ11 (LIGER production evidence), RQ12 (CSA/Google governance survey), RQ13 (pipeline economics with quantitative cost data), RQ14 (agent **ROI/triage** legs — agent ROI metrics)
- **RE-TIERED 2026-06-14**: RQ14's **OCSF-normalization and parser-generation** legs moved from asserted Level A to a measured Tier-B caveat after the #10 first-party measurement (see the OVERTURN note under RQ14). The ROI/triage legs stand on the Google Cloud survey; the automation-rate legs do not.

---

## Gap 12: Formal Research Questions RQ15-RQ17 (June 2026)

Three research questions adopted from the 2026-06-13 Gemini Deep Research lit-review sweep (intake + triage in project1 `00-inbox/gemini/gemini-20260613-litreview-deepen-extend.md`). Each is framed as an open question and cross-referenced to existing work. The two named frameworks the sweep cited — an "SETC framework" for RQ16 and "ETDI" for RQ17 — are recorded as **to-confirm**, not asserted, since neither was opened at a primary; the questions are framed around the underlying concepts so they stand even if those names don't.

### RQ15: Wasm-Embedded Decoders as a Storage-Layer Threat Model

**Research Question**: Do file formats that embed WebAssembly decoders (e.g. CMU's F3) introduce a storage-layer code-execution threat — where a tampered or malicious embedded decoder runs arbitrary code in the reader's process if signature/sandbox validation is bypassed?

**Framing**: F3-style formats ship the decoder inside the file as Wasm so any engine can read evolving encodings; that portability moves decoder code across a trust boundary into every reader. If a host does not verify the decoder's provenance and sandbox its execution, a crafted file becomes an execution vector — a storage-layer analog of unsafe deserialization.

**Evidence Level**: D (proposed; logical threat, no demonstrated exploit)

**Current Evidence**: F3 is real and uses Wasm decoders (SIGMOD 2025, PACMMOD 3(4) Art. 245, DOI 10.1145/3749163 — in the bibliography); FastLanes (PVLDB 2025, DOI 10.14778/3749646.3749718) and Vortex are the adjacent data-parallel-format thread. The threat is projected from the architecture, not measured.

**Validation Metrics**:
- [ ] Characterize the sandbox + signature-validation model F3 actually ships
- [ ] Determine whether any reader executes an unverified embedded decoder
- [ ] Map to a known weakness class (deserialization / supply-chain CWE)

**Relevance**: Chapter 9 (format war) + the storage-layer security thread; pairs with the existing F3 WebAssembly-security concern.

### RQ16: Measurable Intelligence Loss from Collapsing High-Cardinality Telemetry into OCSF

**Research Question**: How much detection-relevant information is lost when high-cardinality endpoint telemetry is normalized/flattened into OCSF, and can that loss be measured per source?

**Note**: This overlaps the existing context-collapse / OCSF-flattening benchmark work — fold in, do not duplicate. The Gemini sweep referenced an "SETC framework"; that name is unverified, so the RQ is anchored to the SDW lab's own measurements rather than the unconfirmed framework.

**Evidence Level**: B (the context-collapse benchmark is measured, Tier B, in the SDW lab)

**Current Evidence**: The SDW context-collapse / OCSF-flattening benchmarks (sdw-lab-benchmarks) and the six-schema → OCSF 1.8.0 crosswalk corpus already measure mapping fidelity and flattening cost. This RQ formalizes the "intelligence loss" question specifically for high-cardinality endpoint sources. Two first-party measurements now ground it directly:
- **Detection-relevant loss is measured, de-gamed (Tier B).** The de-gamed BENCH-A re-run (`~/sdw-lab-benchmarks/ocsf-context-collapse-apt29/`, commit 52e4958) runs **unmodified upstream SigmaHQ** rules via pySigma→SQL against real **MITRE ATT&CK APT29** (OTRF/Mordor) telemetry under documented, blind coarsening. Adversary-relevant detections lose **~2× the recall** and go fully blind ~2× as often as routine detections; the headline blinding-recall-loss delta is **+0.188** at the documented 64-char truncation cap, bounded **+0.094 to +0.205** across a coarsening sweep (deterministic, no RNG, so the band is a truncation-cap curve, not a seed band). The blinded rules are the expected ones — Base64/encoded-PowerShell and long-script-block rules killed by command-line/script-block truncation, which is exactly APT29's encoded-PowerShell tradecraft. Earlier R1/R2 runs reported a larger gameable synthetic delta (+0.719); the **de-gamed +0.188 is the figure to cite** for this RQ, with the synthetic value labelled as such. Caveats travel: modest fired-rule sample, one dataset, one coarsening config, recall-loss measured against the fidelity store (not absolute per-event labels), and the independent-reviewer Tier-A gate on "does Store N resemble what shops build" stays open.
- **Per-source mapping/availability loss is measured (Tier B, #10).** The pipeline-normalization-fidelity bench shows the *normalization step itself* drops detection-relevant structure before any flattening: on Zeek conn the shipped Tenzir mapping leaves `activity_id` correct on only 17% of records and lands `history`/`service`/`uid` in `unmapped` (version-bound: Tenzir 6.0.0, library 671e049, OCSF 1.8.0). So "intelligence loss into OCSF" has two measurable legs — the *coarsening/flattening* leg (BENCH-A, +0.188) and the *mapping-fidelity* leg (#10, the activity-classification and unmapped-field loss).

**Validation Metrics**:
- [x] Quantify field/cardinality loss per source — BENCH-A (recall-loss delta +0.188, de-gamed) + #10 (activity_id 17%, field fidelity 80% on Zeek conn); per-source for high-cardinality EDR/Sysmon remains to run (#10 covered Zeek conn; Sysmon arm was XML-bound)
- [x] Tie measured loss to missed-detection scenarios — APT29 encoded-PowerShell rules go blind under command-line/script-block truncation (BENCH-A)
- [ ] Confirm whether a named "SETC framework" exists as a citable primary before referencing it — still to-confirm; the RQ stands on the lab's own measurements regardless

**Relevance**: Chapter 8 (OCSF/flattening); overlaps the OCSF-crosswalk corpus, the context-collapse benchmark (BENCH-A), and the pipeline-normalization-fidelity bench (#10). Single-host, synthetic-or-single-dataset Tier B — magnitudes ride the corpus; what travels is the shape (adversary-tail loss ~2× routine; activity-classification dropped at the mapping step).

### RQ17: Cryptographic MCP Tool-Validation vs Rug-Pull / Tool-Poisoning

**Research Question**: Can cryptographic tool-validation (signed tool manifests, scoped OAuth/JWT — e.g. an ETDI-style proposal) mitigate MCP rug-pull and tool-poisoning attacks, and what coverage gaps remain?

**Evidence Level**: D (proposed; the attack class is real, the mitigation is emerging)

**Current Evidence**: MCP supply-chain risk is documented — >30 MCP CVEs in early 2026; CVE-2025-6514 (mcp-remote, CVSS 9.6 RCE; verified in the vault); the Habler/Cisco Claude-Code memory-poisoning case (Cisco Blogs + OWASP GenAI ASI06, fixed in Claude Code v2.1.50). The Gemini sweep named "ETDI" as a cryptographic tool-validation proposal; that name is unconfirmed, so the RQ is framed around signed-manifest + scoped-token validation generally.

**Validation Metrics**:
- [ ] Inventory MCP tool-poisoning / rug-pull CVEs and patterns
- [ ] Assess signed-manifest + OAuth-scope validation approaches and their coverage
- [ ] Confirm "ETDI" as a citable primary or drop the name

**Relevance**: Chapter 12/13 (agentic security); pairs with the agentic-security thread (CVE-2025-6514, GTG-1002) and the AI-safety-vs-security framing.

## Summary of RQ15-RQ17

These three June-2026 questions extend the review into storage-layer and agentic-security threats:

1. **RQ15 (Wasm-decoder threat)**: a code-execution threat model for embedded-decoder formats (F3) — proposed, Tier D
2. **RQ16 (OCSF intelligence loss)**: measurable detection-relevant loss from flattening high-cardinality telemetry — anchored to the existing context-collapse benchmark, Tier B
3. **RQ17 (cryptographic MCP tool-validation)**: signed-manifest / scoped-token mitigation of MCP rug-pull / tool-poisoning — proposed, Tier D

**Total Research Questions**: RQ1-RQ10 + RQ11-RQ14 + RQ15-RQ17 = **17 formal research questions**. Two cited framework names (SETC for RQ16, ETDI for RQ17) are recorded as to-confirm, not asserted.

---

**Author**: Jeremy Wiley
**Date**: October 10, 2025 (original), updated November 14, 2025 (isolation-first security), December 6, 2025 (AI/agent architectures + LIGER Stack + formal RQ11-RQ14), January 3, 2026 (major evidence update from web research), **February 28, 2026** (RQ13 pipeline detection economics validated), **June 13, 2026** (RQ15-RQ17 adopted from the Gemini DR sweep), **June 14, 2026** (benchmark integration: RQ14 OCSF/parser legs OVERTURNED asserted-A → measured Tier-B caveat per #10 [⚠️ confidence-level change, flagged for sign-off]; RQ16 grounded on the measured BENCH-A de-gamed +0.188 and #10 mapping-fidelity legs; RQ11/RQ13 cost-reduction standardized to 60-80% median / up to 90%+ optimal, anchored to lab byte ratios 2.6-8.5× + production-cluster economics)
**Sources**: 150+ footnotes analyzed, MASTER-HYPOTHESIS-TRACKER.md reviewed, isolation-first security pattern from blog, AI/agent patterns from project1, LIGER Stack reference architecture, CSA/Google AI governance study, Forrester, ClickHouse case studies, Google Cloud agent ROI, **SACR Market Guide 2025, Rippling SIEM series, Monad detection cost analysis**
**Status**: All RQ11-RQ14 now have strong evidence validation
