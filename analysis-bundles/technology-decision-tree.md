# Technology Decision Tree

**Purpose**: Structured decision framework for security data platform architecture selection
**Evidence Source**: `cost-reality-reference.md`, `implementation-reality-reference.md`, `performance-benchmarks-table.md`
**Last Updated**: October 15, 2025
**Use Case**: Chapter 6 (Decision Framework), practitioner architecture selection

---

## Executive Summary

This decision tree guides security teams through architecture selection using evidence-based criteria. Each decision point is supported by quantitative data from production deployments and validated across multiple sources.

**Key Decision Points**:
1. **Latency Requirements** - Real-time vs batch tolerance
2. **Team Capability** - Existing expertise and staffing capacity
3. **Budget Reality** - 3-year TCO constraints
4. **Business Value** - Incident costs and analyst productivity
5. **Build vs Buy** - Self-managed vs managed services

**Decision Tree Output**: Specific architecture recommendation with estimated TCO, staffing, and timeline

---

## Decision Tree Overview

```
START: Security Data Platform Architecture Selection
│
├─ Question 1: What are your detection latency requirements?
│  ├─ A: Real-time detection required (< 1 minute SLA) → GO TO Question 2 (Streaming Path)
│  ├─ B: Near real-time acceptable (1-15 minutes) → GO TO Question 3 (Hybrid Path)
│  └─ C: Batch processing acceptable (15-60 minutes) → GO TO Question 4 (Batch Path)
│
├─ Question 2 (STREAMING PATH): What is your team's streaming expertise?
│  ├─ A: Existing Kafka/Flink expertise (Level 4) → GO TO Question 5 (Self-Managed)
│  ├─ B: General data engineering, no streaming → GO TO Question 6 (Managed Services)
│  └─ C: Limited data engineering expertise → RECOMMENDATION: Start with Batch, build capability
│
├─ Question 3 (HYBRID PATH): What is your primary use case priority?
│  ├─ A: Automated response workflows (< 5 min) → GO TO Question 7 (Streaming + Batch Hybrid)
│  ├─ B: Investigation workflows (5-30 min) → GO TO Question 8 (Batch-First Hybrid)
│  └─ C: Compliance + historical analysis → GO TO Question 4 (Batch Path)
│
├─ Question 4 (BATCH PATH): What is your data volume and query pattern?
│  ├─ A: High-volume OLAP (TB+/day, ad-hoc queries) → RECOMMENDATION: Batch - ClickHouse + Iceberg
│  ├─ B: Moderate volume (100GB-1TB/day) → RECOMMENDATION: Batch - Trino + Iceberg
│  └─ C: Low volume (< 100GB/day) → RECOMMENDATION: Batch - DuckDB or Trino
│
├─ Question 5 (SELF-MANAGED STREAMING): What is your budget capacity?
│  ├─ A: > $2.5M/year operational budget → RECOMMENDATION: Self-Managed Kafka + Flink
│  ├─ B: $1.5-2.5M/year → RECOMMENDATION: Managed Streaming (Confluent/MSK)
│  └─ C: < $1.5M/year → RECOMMENDATION: Reconsider - Streaming may not be viable
│
├─ Question 6 (MANAGED STREAMING): Can you absorb 2.0-2.2× staffing increase?
│  ├─ A: Yes, team can grow to 7-8 FTEs → RECOMMENDATION: Managed Kafka + Kafka Streams
│  ├─ B: Limited growth (5-6 FTEs max) → RECOMMENDATION: Managed Kafka + Batch Processing
│  └─ C: No capacity to grow team → RECOMMENDATION: Start with Batch, revisit in 12-18 months
│
├─ Question 7 (STREAMING + BATCH HYBRID): What is your incident cost reality?
│  ├─ A: > $3M/year in incident costs → RECOMMENDATION: Hybrid - Streaming (hot) + Batch (warm/cold)
│  ├─ B: $1-3M/year → RECOMMENDATION: Hybrid - Managed Streaming + Batch
│  └─ C: < $1M/year → RECOMMENDATION: Batch-First (streaming ROI unclear)
│
└─ Question 8 (BATCH-FIRST HYBRID): Do you need multi-year queryable retention?
   ├─ A: Yes, compliance requires 2-7 years → RECOMMENDATION: Batch - Iceberg + Tiered Storage
   ├─ B: 6-12 months sufficient → RECOMMENDATION: Batch - Any table format
   └─ C: 30-90 days sufficient → RECOMMENDATION: Batch - DuckDB or ClickHouse
```

---

## Decision Point 1: Latency Requirements

### Question: What are your detection latency requirements?

**Context**: Detection latency drives architectural complexity and cost. Real-time streaming costs 2.8-3.2× more than batch over 3 years (per TCO calculators).

---

#### Option A: Real-time detection required (< 1 minute SLA)

**Use Cases**:
- Automated threat response (SOAR integration)
- Fraud detection (financial services)
- DDoS mitigation (real-time traffic analysis)
- Insider threat detection (behavioral analytics)

**Requirements**:
- Sub-second to sub-minute data availability
- Stateful stream processing (entity tracking, windowing)
- 24/7 operational support (DORA: streaming requires always-on ops)

**Evidence**: Uber security analytics (sub-second refresh for thousands of real-time views), LinkedIn security (terabyte-scale state management for entity tracking).

**Next Step**: → GO TO Question 2 (Streaming Path)

---

#### Option B: Near real-time acceptable (1-15 minutes)

**Use Cases**:
- Threat hunting dashboards
- Investigation workflows (analyst-driven)
- Compliance monitoring (non-critical)
- Security operations center (SOC) situational awareness

**Requirements**:
- Micro-batch processing (5-15 minute intervals)
- Can leverage both streaming and batch components
- Operational burden lower than always-on streaming

**Evidence**: Gartner security lakehouse implementations (5.5 months average) often target 5-15 minute refresh for investigation workflows.

**Next Step**: → GO TO Question 3 (Hybrid Path)

---

#### Option C: Batch processing acceptable (15-60 minutes)

**Use Cases**:
- Threat intelligence enrichment (hourly updates)
- Compliance reporting (daily/weekly)
- Historical threat hunting (investigative)
- Cost optimization (deferred non-critical alerts)

**Requirements**:
- Hourly or daily batch processing
- Simpler operational model (no 24/7 streaming ops)
- 3-year TCO ~$2.5M (baseline from staffing calculator)

**Evidence**: Shell ClickHouse deployment (57TB/day security telemetry) uses batch ingestion for most workloads, reserving streaming for critical detection.

**Next Step**: → GO TO Question 4 (Batch Path)

---

## Decision Point 2: Streaming Expertise (Real-Time Path)

### Question: What is your team's streaming expertise level?

**Context**: Streaming requires Level 4 specialized skills (DORA: top 5% of organizations). Lack of expertise extends timelines by 6-12 months and requires $50K-100K consulting (industry norm).

---

#### Option A: Existing Kafka/Flink expertise (Level 4)

**Characteristics**:
- Team has deployed production Kafka clusters (3+ years experience)
- Familiar with exactly-once semantics, state management, fault tolerance
- Experience with 24/7 on-call for streaming systems
- Understands Kafka internals (partition rebalancing, consumer lag, offset management)

**Validation**:
- [ ] At least 2 team members with Kafka production experience
- [ ] Existing on-call rotation for streaming systems
- [ ] Incident response runbooks for streaming failures

**Evidence**: Ververica case study shows even with experienced staff, Flink production deployment requires 4-9 months and 3.2 FTEs.

**Next Step**: → GO TO Question 5 (Self-Managed Streaming Budget Assessment)

---

#### Option B: General data engineering, no streaming

**Characteristics**:
- Team has batch ETL/ELT experience (Airflow, dbt, SQL pipelines)
- Familiar with data modeling, schema design, query optimization
- Limited or no experience with Kafka, Flink, stream processing concepts
- No 24/7 operational experience

**Implications**:
- 6-12 months training/ramp-up required (Gartner)
- Managed services reduce operational burden by 30-40%
- Consulting likely required ($50K-100K)
- Streaming multiplier: 2.0-2.2× (vs 2.7× for self-managed)

**Evidence**: MIT Technology Review (1.5-2× higher training investments), DORA (Level 4 skills = top 5% of organizations).

**Next Step**: → GO TO Question 6 (Managed Services Viability)

---

#### Option C: Limited data engineering expertise

**Characteristics**:
- Security engineering team without dedicated data engineers
- SQL familiarity but limited pipeline development experience
- No experience with infrastructure as code (Terraform, CloudFormation)
- Team size < 5 FTEs

**Recommendation**: **Start with Batch Architecture**

**Rationale**:
- Streaming requires 9-11 FTEs (per staffing calculator)
- 2.7× staffing multiplier not viable for small teams
- 4-9 month streaming timeline too long for limited resources
- Batch provides 80% of value with 30% of complexity

**Path Forward**:
1. Implement batch architecture (2-4 months, 3.5 FTEs)
2. Build data engineering capability (6-12 months)
3. Reassess streaming viability in 12-18 months

**Evidence**: Gartner skills scarcity (streaming expertise gap), DORA (2.7× operational staff requirement).

**Next Step**: → GO TO Question 4 (Batch Path)

---

## Decision Point 3: Hybrid Use Case Priority

### Question: What is your primary use case priority?

**Context**: Hybrid architectures balance real-time and batch processing. The dominant use case determines whether streaming or batch should be the primary component.

---

#### Option A: Automated response workflows (< 5 minutes)

**Use Cases**:
- SOAR-driven automated containment
- User account lockouts (compromise detected)
- Firewall rule updates (threat-based)
- Alert escalation (critical severity)

**Requirements**:
- Real-time decision-making (sub-5 minute response)
- Stateful processing (user/entity context)
- High reliability (exactly-once semantics critical for automated actions)

**Architecture Implication**: Streaming-primary with batch for historical context

**Evidence**: Uber security (thousands of real-time views for automated workflows), Confluent (exactly-once semantics for alert fidelity).

**Next Step**: → GO TO Question 7 (Streaming + Batch Hybrid Assessment)

---

#### Option B: Investigation workflows (5-30 minutes)

**Use Cases**:
- Analyst-driven threat hunting
- Incident investigation dashboards
- Contextual enrichment (TI lookups)
- Weekly compliance reporting

**Requirements**:
- Interactive query performance (< 1 second for 90% of queries)
- Multi-year queryable retention (Iceberg + tiered storage)
- Ad-hoc analysis flexibility (SQL-based exploration)

**Architecture Implication**: Batch-primary with optional streaming for high-priority alerts

**Evidence**: ClickHouse Cloudflare deployment (96% of queries < 1 second), SK Telecom Iceberg (97% query time reduction).

**Next Step**: → GO TO Question 8 (Batch-First Hybrid Assessment)

---

#### Option C: Compliance + historical analysis

**Use Cases**:
- Regulatory compliance (SOX, PCI-DSS, GDPR)
- Historical threat hunting (monthly/quarterly reviews)
- Audit log retention (immutable storage)
- Cost-optimized long-term retention

**Requirements**:
- Multi-year retention (2-7 years typical)
- Immutable audit trail (Iceberg snapshot isolation)
- Tiered storage (55-80% cost savings from hot/warm/cold)

**Architecture Implication**: Batch-only with tiered storage lifecycle

**Evidence**: AWS tiered storage (55% average savings), Netflix Kafka (70-80% reduction with tiered storage).

**Next Step**: → GO TO Question 4 (Batch Path)

---

## Decision Point 4: Batch Architecture Selection

### Question: What is your data volume and query pattern?

**Context**: Batch architecture offers 3 primary query engine options, each optimized for different workloads. Choice depends on data volume, query complexity, and latency requirements.

---

#### Option A: High-volume OLAP (TB+/day, ad-hoc queries)

**Characteristics**:
- Data volume > 1 TB/day
- Ad-hoc analytical queries (aggregations, JOINs, filters)
- Sub-second query latency required (analyst interactive workflows)
- High compression ratio important (storage cost optimization)

**Recommendation**: **ClickHouse + Apache Iceberg**

**Evidence**:
- **ClickHouse Performance**: 6M events/sec ingest, 96% queries < 1s (Cloudflare), 57TB/day production scale (Shell)
- **Compression**: 10-12× compression ratio typical, 75-85% storage reduction vs Elasticsearch (Altinity)
- **Security Optimizations**: Native IP types (50-100× faster CIDR queries), time-series optimizations

**Architecture**:
```
Ingestion → Kafka (optional buffer) → ClickHouse (hot queries, 7-30 days)
                                   → Iceberg (warm/cold, multi-year retention)

Query: ClickHouse (real-time) + Trino (historical Iceberg queries)
```

**3-Year TCO**: ~$2.5M (baseline batch budget per staffing calculator)

**Next Step**: RECOMMENDATION OUTPUT (See "Batch - ClickHouse + Iceberg" section)

---

#### Option B: Moderate volume (100GB-1TB/day)

**Characteristics**:
- Data volume 100GB-1TB/day
- Mixed workload (interactive queries + scheduled reports)
- Query latency 1-5 seconds acceptable
- Federation required (multiple data sources: S3, JDBC, APIs)

**Recommendation**: **Trino + Apache Iceberg**

**Evidence**:
- **Trino Performance**: Petabyte-scale queries (Meta), 10-100× faster than Hive (industry benchmarks)
- **Federation**: 40+ connectors (S3, PostgreSQL, MySQL, Elasticsearch, etc.)
- **Iceberg Integration**: Native Iceberg support, time travel, schema evolution

**Architecture**:
```
Ingestion → Batch ETL (Airflow/dbt) → Iceberg Tables (S3/Azure Blob)

Query: Trino (federated SQL across Iceberg + other sources)
```

**3-Year TCO**: ~$2.3M (slightly lower than ClickHouse due to simpler ops)

**Next Step**: RECOMMENDATION OUTPUT (See "Batch - Trino + Iceberg" section)

---

#### Option C: Low volume (< 100GB/day)

**Characteristics**:
- Data volume < 100GB/day
- Small team (< 5 FTEs)
- Minimal operational overhead required
- Embedded analytics or edge processing possible

**Recommendation**: **DuckDB or Trino (depending on use case)**

**DuckDB Use Cases**:
- Edge/endpoint security analytics (embedded queries)
- Single-server deployments (no distributed infrastructure)
- Investigative workflows (analyst laptops)

**Evidence**: Jake Thomas (Okta) - production DuckDB for defensive cyber operations

**Trino Use Cases**:
- Federation across multiple sources (APIs, databases, S3)
- Multi-user query concurrency (10+ analysts)
- Cloud-native deployment (separation of storage/compute)

**Architecture (DuckDB)**:
```
Ingestion → Parquet files (S3/local) → DuckDB (embedded analytics)
```

**Architecture (Trino)**:
```
Ingestion → Batch ETL → Iceberg/Parquet → Trino (federated queries)
```

**3-Year TCO**: ~$1.8M (DuckDB lower ops burden) to $2.3M (Trino)

**Next Step**: RECOMMENDATION OUTPUT (See "Batch - Low Volume" section)

---

## Decision Point 5: Self-Managed Streaming Budget

### Question: What is your operational budget capacity?

**Context**: Self-managed streaming requires 9-11 FTEs ($2.0M/year) + infrastructure ($150K/year) + incident costs ($100K/year). 3-year TCO = $7.9M (per staffing calculator).

---

#### Option A: > $2.5M/year operational budget

**Budget Breakdown**:
- Staffing: $1,972K/year (9.5 FTEs)
- Infrastructure: $150K/year (self-managed Kafka clusters)
- Training: $50K/year (ongoing skills development)
- Incidents: $100K/year (DORA 3.2× incident rate)
- **TOTAL**: $2,272K/year (~$2.3M)

**Viability**: ✅ Budget supports self-managed streaming

**Recommendation**: **Self-Managed Kafka + Flink**

**Advantages**:
- Full control over streaming platform (compliance/sovereignty)
- Custom stream processing logic (complex stateful workflows)
- No vendor lock-in (open-source ecosystem)

**Evidence**: LinkedIn security (terabyte-scale state management), Uber (thousands of real-time views).

**Next Step**: RECOMMENDATION OUTPUT (See "Self-Managed Streaming" section)

---

#### Option B: $1.5-2.5M/year operational budget

**Budget Breakdown**:
- Staffing: $1,850K/year (8 FTEs) - managed services reduce ops burden
- Managed Platform: $90K/year (Confluent Cloud / AWS MSK)
- Infrastructure: $80K/year (reduced - managed clusters)
- Training: $35K/year
- Incidents: $50K/year (reduced - managed platform handles ops)
- **TOTAL**: $2,105K/year (~$2.1M)

**Viability**: ✅ Budget supports managed streaming

**Recommendation**: **Managed Kafka (Confluent/MSK) + Kafka Streams**

**Advantages**:
- Reduced operational burden (30-40% lower ops headcount)
- Faster time to production (3-6 months vs 4-9 months)
- Lower incident costs (managed platform handles infrastructure)

**Evidence**: Ververica (managed services reduce ops burden), Netflix (production Kafka at scale).

**Next Step**: RECOMMENDATION OUTPUT (See "Managed Streaming" section)

---

#### Option C: < $1.5M/year operational budget

**Budget Reality**:
- Minimum streaming budget: ~$2.1M/year (managed) to $2.3M/year (self-managed)
- Current budget: < $1.5M/year
- **GAP**: $600K-800K/year shortfall

**Viability**: ❌ Budget insufficient for streaming operations

**Recommendation**: **Reconsider streaming - Start with Batch**

**Rationale**:
- Streaming ROI unclear with limited budget (7.7-year break-even per calculator)
- Batch architecture provides 80% of detection value at $668K/year (vs $2.1M)
- Staffing multiplier (2.7×) not viable with budget constraints

**Path Forward**:
1. Implement batch architecture ($668K/year operational)
2. Demonstrate business value (incident cost reduction, analyst productivity)
3. Build business case for streaming investment (12-18 months)

**Next Step**: → GO TO Question 4 (Batch Path)

---

## Decision Point 6: Managed Streaming Team Growth

### Question: Can you absorb 2.0-2.2× staffing increase?

**Context**: Managed streaming reduces ops burden (vs self-managed 2.7×) but still requires 2.0-2.2× more staff than batch. 8 FTEs minimum for production operations (per staffing calculator).

---

#### Option A: Yes, team can grow to 7-8 FTEs

**Current Team**: Likely 3-4 FTEs
**Required Team**: 7-8 FTEs (managed streaming)
**Growth**: +4 FTEs (2× current size)

**Hiring Requirements**:
- 2-3 Stream Processing Engineers ($175K median, specialized skills)
- 1-2 additional Data Engineers ($140K median)
- 1 Platform/SRE Engineer ($150K median)

**Timeline**: 6-12 months hiring + onboarding (Gartner skills scarcity)

**Recommendation**: **Managed Kafka + Kafka Streams**

**Evidence**: Confluent Kafka Streams (exactly-once semantics, sub-250ms latency), Nordstrom (production security analytics).

**Next Step**: RECOMMENDATION OUTPUT (See "Managed Streaming" section)

---

#### Option B: Limited growth (5-6 FTEs max)

**Current Team**: 3-4 FTEs
**Maximum Team**: 5-6 FTEs
**Gap**: 2-3 FTEs short of streaming minimum (8 FTEs)

**Hybrid Recommendation**: **Managed Kafka (buffer) + Batch Processing (primary)**

**Architecture**:
```
Ingestion → Managed Kafka (real-time buffer, 7-30 days) → Batch ETL → Iceberg (multi-year)

Critical Alerts: Kafka Streams (lightweight real-time detection)
Investigation: Batch queries (ClickHouse/Trino + Iceberg)
```

**Staffing**:
- 1 Stream Processing Engineer (Kafka Streams for critical alerts only)
- 2 Data Engineers (batch pipelines + occasional Kafka Streams)
- 1 Platform Engineer (managed Kafka + batch infrastructure)
- 1 Security Engineer (detection logic)
- **TOTAL**: 5 FTEs

**Evidence**: Managed Kafka commonly used as ingestion buffer without full streaming analytics (industry pattern).

**Next Step**: RECOMMENDATION OUTPUT (See "Hybrid - Managed Kafka + Batch" section)

---

#### Option C: No capacity to grow team

**Current Team**: 3-4 FTEs
**Growth Capacity**: None (budget/hiring constraints)
**Streaming Viability**: ❌ Insufficient capacity

**Recommendation**: **Start with Batch, revisit in 12-18 months**

**Rationale**:
- Streaming requires minimum 7-8 FTEs (managed) or 9-11 FTEs (self-managed)
- Current capacity only supports batch (3.5 FTEs per staffing calculator)
- Attempting streaming with insufficient staff = high risk of operational failure

**Path Forward**:
1. Implement batch architecture (3.5 FTEs, 2-4 months)
2. Demonstrate value (incident cost reduction, analyst productivity)
3. Build business case for team expansion (6-12 months)
4. Reassess streaming viability when team can grow to 7+ FTEs

**Next Step**: → GO TO Question 4 (Batch Path)

---

## Decision Point 7: Streaming + Batch Hybrid (High-Value Ops)

### Question: What is your incident cost reality?

**Context**: Streaming economics improve with high incident costs. Break-even analysis shows streaming pays off when incident costs > $3M/year and streaming reduces MTTR by 50-70%.

---

#### Option A: > $3M/year in incident costs

**Incident Cost Analysis**:
- Current incident costs: > $3M/year
- Streaming benefit: 50-70% MTTR reduction (Altinity: 70% investigation time reduction)
- **Annual Savings**: $1.5-2.1M/year

**Business Case**:
- 3-year streaming cost: $6.9M (managed) or $7.9M (self-managed)
- 3-year batch cost: $2.5M
- **Cost Difference**: $4.4M (managed) or $5.4M (self-managed)
- **Break-Even**: 2.1-3.6 years (high-value ops)

**Recommendation**: **Hybrid - Streaming (hot) + Batch (warm/cold)**

**Architecture**:
```
Ingestion → Kafka → Flink/Kafka Streams (real-time detection, 24-48 hours)
                 → Batch ETL → Iceberg (warm/cold, multi-year retention)

Hot Queries: Flink state / ClickHouse (last 24-48 hours)
Investigation: Trino + Iceberg (historical context, multi-year)
```

**Staffing**: 9-11 FTEs (full streaming + batch operations)

**Evidence**: Netflix (streaming + batch hybrid for multi-year retention), Uber (real-time views + historical batch).

**Next Step**: RECOMMENDATION OUTPUT (See "Hybrid - Streaming Primary" section)

---

#### Option B: $1-3M/year in incident costs

**Incident Cost Analysis**:
- Current incident costs: $1-3M/year
- Streaming benefit: $500K-1.5M/year (50-70% MTTR reduction)
- **Annual Savings**: Moderate ($500K-1.5M)

**Business Case**:
- Break-even: 3.0-8.9 years (depending on incident costs and streaming approach)
- Managed streaming: 4.5-6.3 years break-even
- Self-managed streaming: 7.7+ years break-even

**Recommendation**: **Hybrid - Managed Streaming + Batch**

**Architecture**:
```
Ingestion → Managed Kafka (Confluent/MSK) → Kafka Streams (critical alerts)
                                          → Batch ETL → Iceberg (multi-year)

Critical Alerts: Kafka Streams (sub-minute detection)
Investigation: ClickHouse/Trino + Iceberg (batch queries)
```

**Staffing**: 7-8 FTEs (managed streaming reduces ops burden)

**Evidence**: Managed Kafka widely adopted for hybrid architectures (lower ops burden).

**Next Step**: RECOMMENDATION OUTPUT (See "Hybrid - Managed Streaming + Batch" section)

---

#### Option C: < $1M/year in incident costs

**Incident Cost Analysis**:
- Current incident costs: < $1M/year
- Streaming benefit: < $500K/year (conservative)
- **Annual Savings**: Low (< $500K)

**Business Case**:
- Break-even: 8.9+ years (streaming ROI unclear)
- Streaming premium not justified by incident cost reduction alone

**Recommendation**: **Batch-First (streaming ROI unclear)**

**Rationale**:
- Streaming costs $2.1-2.3M/year vs batch $668K/year
- Incident savings ($500K/year) do not cover streaming premium ($1.4-1.6M/year)
- Batch provides 80% of detection value at 30% of cost

**Path Forward**:
1. Implement batch architecture (lower risk, proven ROI)
2. Monitor incident costs and analyst productivity
3. Reassess streaming if incident costs increase or business value case strengthens

**Next Step**: → GO TO Question 4 (Batch Path)

---

## Decision Point 8: Batch-First Hybrid Retention

### Question: Do you need multi-year queryable retention?

**Context**: Multi-year retention drives storage architecture decisions. Tiered storage (hot/warm/cold) provides 55-80% cost savings (AWS, Netflix) while maintaining queryable access.

---

#### Option A: Yes, compliance requires 2-7 years queryable retention

**Compliance Drivers**:
- Regulatory requirements (SOX, PCI-DSS, HIPAA, GDPR)
- Audit log retention (immutable, tamper-evident)
- Historical threat hunting (investigations require multi-year context)

**Recommendation**: **Batch - Iceberg + Tiered Storage**

**Architecture**:
```
Ingestion → Batch ETL → Iceberg Tables (S3/Azure Blob with tiered storage)

Storage Tiers:
- Hot (0-30 days): S3 Standard (frequent access, $0.023/GB)
- Warm (30-365 days): S3 Intelligent-Tiering (infrequent, $0.0125/GB)
- Cold (365+ days): S3 Glacier Instant Retrieval ($0.004/GB)

Query: Trino (unified SQL across all tiers)
```

**Cost Savings**: 55-80% storage cost reduction (AWS 55% average, Netflix 70-80%)

**Evidence**:
- **Netflix**: 70-80% storage cost reduction with Kafka tiered storage
- **AWS**: 55% average savings with hot/warm/cold lifecycle
- **Iceberg**: Native lifecycle policy support, seamless tier transitions

**Next Step**: RECOMMENDATION OUTPUT (See "Batch - Iceberg + Tiered Storage" section)

---

#### Option B: 6-12 months retention sufficient

**Use Cases**:
- Short-term threat detection (no long-term compliance)
- Real-time investigation workflows (recent data only)
- Cost optimization (minimize storage footprint)

**Recommendation**: **Batch - Any table format (Iceberg, Delta, or Parquet)**

**Architecture**:
```
Ingestion → Batch ETL → Iceberg/Delta/Parquet (S3 Standard)

Retention: 6-12 months rolling window
TTL Cleanup: Automated deletion after retention period

Query: ClickHouse (hot queries) or Trino (historical)
```

**Cost Optimization**: Single-tier storage (S3 Standard), no tiered lifecycle overhead

**Evidence**: Many security operations focus on 30-90 day "hot" data for investigations (industry norm).

**Next Step**: RECOMMENDATION OUTPUT (See "Batch - Short-Term Retention" section)

---

#### Option C: 30-90 days retention sufficient

**Use Cases**:
- Real-time detection only (minimal historical context)
- High data volume with aggressive retention policies
- Cost-constrained environments

**Recommendation**: **Batch - DuckDB or ClickHouse**

**Architecture (ClickHouse)**:
```
Ingestion → ClickHouse (native TTL, automated cleanup)

Retention: 30-90 days (ClickHouse TTL policy)
Storage: Single-tier (no Iceberg/Delta overhead)

Query: ClickHouse (sub-second OLAP)
```

**Architecture (DuckDB - Low Volume)**:
```
Ingestion → Parquet files (local or S3)

Retention: Manual file cleanup (30-90 day rolling window)

Query: DuckDB (embedded analytics)
```

**Cost Optimization**: Minimal storage footprint, no table format overhead

**Evidence**: ClickHouse TTL widely used for short-term retention (Altinity best practices).

**Next Step**: RECOMMENDATION OUTPUT (See "Batch - Short-Term Retention" section)

---

## Recommendation Outputs

### RECOMMENDATION 1: Self-Managed Streaming (Kafka + Flink)

**When to Choose**:
- Real-time detection required (< 1 minute SLA)
- Existing Level 4 streaming expertise (Kafka/Flink production experience)
- Budget capacity > $2.5M/year
- Incident costs > $3M/year (streaming ROI justifiable)
- Compliance/sovereignty requires full platform control

---

**Architecture**:
```
Ingestion:
- Kafka (self-managed clusters, 3+ brokers per AZ)
- Schema Registry (Confluent Schema Registry or AWS Glue)
- Kafka Connect (source connectors: Syslog, API pulls, log shippers)

Stream Processing:
- Apache Flink (stateful processing, exactly-once semantics)
- State Backend: RocksDB (local) + S3 (checkpoints)
- Watermarks & windowing for time-based aggregations

Storage:
- Hot: Flink state (sub-second queries, last 24-48 hours)
- Warm: ClickHouse (fast OLAP, 7-30 days)
- Cold: Iceberg (multi-year, tiered S3)

Query:
- Real-time: Flink SQL or custom applications
- Historical: Trino (federated SQL across ClickHouse + Iceberg)
```

---

**Team Composition** (9-11 FTEs):
- **Stream Processing Engineers**: 3-4 FTEs
  - Flink job development (stateful processing, windowing)
  - Exactly-once semantics tuning
  - State backend optimization (RocksDB, checkpointing)
  - Performance tuning (backpressure, parallelism)
- **Data Engineers**: 2 FTEs
  - Kafka Connect connector development
  - Schema evolution (Avro/Protobuf)
  - Data quality validation
- **Platform/SRE Engineers**: 2-3 FTEs
  - Kafka cluster operations (broker management, rebalancing)
  - 24/7 on-call rotation (DORA: streaming requires always-on ops)
  - Observability (Prometheus, Grafana, Kafka lag monitoring)
  - Incident response runbooks
- **Security Engineers**: 1.5-2 FTEs
  - Real-time detection logic
  - Enrichment workflows (TI lookups)
  - Automated response integration (SOAR)

**Staffing Evidence**: DORA (2.7× operational staff), Ververica (3.2 FTEs for Flink pipelines), IDC (2.5-3× higher staffing costs).

---

**Budget (Annual)**:
- **Staffing**: $1,972K (9.5 FTEs, per staffing calculator)
- **Infrastructure**: $150K (Kafka clusters, Flink compute, monitoring)
- **Training**: $50K (ongoing skills development, conferences)
- **Incident Costs**: $100K (DORA 3.2× incident rate)
- **TOTAL ANNUAL**: **$2,272K** (~$2.3M/year)

**3-Year TCO**: **$7.9M** (per staffing calculator)

**Budget Evidence**: Staffing calculator consolidates IDC, DORA, Ververica, MIT Technology Review data.

---

**Implementation Timeline**: 6-9 months

**Phase 1 (Months 1-2)**: Foundation
- Kafka cluster setup (3 brokers × 3 AZs)
- Flink cluster deployment (JobManager + TaskManagers)
- Observability stack (Prometheus, Grafana, Kafka lag exporter)
- Team: 4-5 FTEs (architecture, infrastructure)

**Phase 2 (Months 3-6)**: Development
- Flink job development (3-5 critical detection use cases)
- Stateful processing (entity tracking, behavioral analytics)
- Exactly-once semantics validation
- Team: 7-8 FTEs (full development)

**Phase 3 (Months 7-9)**: Production Ramp-Up
- Production deployment (phased rollout)
- 24/7 on-call rotation established
- Runbook development (incident response)
- Team: 9-11 FTEs (full operational team)

**Timeline Evidence**: Ververica (4-9 months with experienced staff), DORA (streaming complexity extends timelines).

---

**Performance Expectations**:
- **Ingestion**: 1-2M events/sec (Kafka production scale)
- **Processing Latency**: Sub-second to sub-minute (Flink stream processing)
- **State Size**: Terabytes (LinkedIn: terabyte-scale state management)
- **Query Latency**: < 1s for hot queries (ClickHouse: 96% <1s)

**Performance Evidence**: Kafka (4.5M events/sec at Azure), Flink (LinkedIn terabyte-scale state), ClickHouse (Cloudflare 96% <1s).

---

**Break-Even Analysis**:
- **3-Year Cost Difference vs Batch**: $7.9M - $2.5M = **$5.4M**
- **Required Annual Business Value**: $1.8M/year (to break even in 3 years)

**Business Value Sources**:
- Incident cost reduction: 50-70% MTTR reduction (Altinity)
- Analyst productivity: 40% increase (Altinity)
- Automated response: Sub-minute detection → containment

**Break-Even Scenarios**:
- **High-Value Ops** (incident costs > $3M/year): **2.2 years**
- **Moderate Ops** (incident costs $1-3M/year): **7.7 years**
- **Low-Value Ops** (incident costs < $1M/year): **Not viable**

**Break-Even Evidence**: Staffing calculator (TCO models), Altinity (70% MTTR reduction, 40% productivity increase).

---

**Technology Stack**:
- **Streaming**: Apache Kafka 3.6+ (tiered storage, KRaft mode)
- **Processing**: Apache Flink 1.18+ (exactly-once, state backends)
- **Hot Storage**: ClickHouse 23.8+ (native IP types, time-series optimization)
- **Cold Storage**: Apache Iceberg 1.4+ (lifecycle policies, snapshot isolation)
- **Query**: Trino 435+ (Iceberg native, Arrow Flight SQL)
- **Observability**: Prometheus, Grafana, Kafka lag exporter, Flink metrics

**Technology Evidence**: All versions represent production-validated releases with security-specific features.

---

**Risks & Mitigations**:

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Skills gap extends timeline 6-12 months | High (Gartner: Level 4 scarcity) | High ($500K+ cost overrun) | Consulting ($50K-100K), managed services fallback |
| Incident rate 3.2× higher during ramp-up | High (DORA validated) | Medium ($100K/year) | Extensive runbooks, phased rollout, SRE investment |
| State management complexity | Medium | High (data loss risk) | RocksDB tuning, S3 checkpointing, exactly-once validation |
| Budget overrun 30-50% | Medium | High | Red flags monitoring (per staffing calculator), quarterly reviews |

**Risk Evidence**: DORA (3.2× incident rate), Gartner (Level 4 skills scarcity), DevOps Enterprise Summit (3-4× incident costs).

---

**Key Decision Factors**:
- ✅ **Strong Fit**: Existing Kafka/Flink expertise, budget > $2.5M/year, incident costs > $3M/year, compliance requires full control
- ⚠️ **Moderate Fit**: Some streaming experience, budget $2.0-2.5M/year, managed services not viable (compliance)
- ❌ **Poor Fit**: No streaming expertise, budget < $2.0M/year, incident costs < $1M/year, small team (< 7 FTEs)

---

### RECOMMENDATION 2: Managed Streaming (Confluent/MSK + Kafka Streams)

**When to Choose**:
- Real-time detection required (< 1 minute SLA)
- General data engineering expertise (no Level 4 streaming skills)
- Budget capacity $1.5-2.5M/year
- Team can grow to 7-8 FTEs
- Faster time to production preferred (3-6 months vs 6-9 months)

---

**Architecture**:
```
Ingestion:
- Managed Kafka (Confluent Cloud, AWS MSK, Azure Event Hubs)
- Schema Registry (Confluent managed or AWS Glue)
- Managed Connectors (Confluent Hub, AWS MSK Connect)

Stream Processing:
- Kafka Streams (lightweight, embedded in applications)
- Exactly-once semantics (built-in)
- Stateful processing (RocksDB local state stores)

Storage:
- Hot: Kafka topic (7-30 days managed retention)
- Warm: ClickHouse (batch loaded from Kafka, 30-90 days)
- Cold: Iceberg (multi-year, tiered S3)

Query:
- Real-time: Kafka Streams applications (state stores) or ksqlDB
- Historical: Trino (federated SQL across ClickHouse + Iceberg)
```

---

**Team Composition** (7-8 FTEs):
- **Stream Processing Engineers**: 2-3 FTEs
  - Kafka Streams application development
  - Stateful processing (entity tracking)
  - Exactly-once semantics
- **Data Engineers**: 2 FTEs
  - Managed connector configuration
  - Schema design (Avro/JSON)
  - Batch ETL (Kafka → Iceberg)
- **Platform Engineers**: 2 FTEs
  - Managed platform configuration (reduced ops burden)
  - Observability (Confluent Cloud metrics, CloudWatch)
  - Incident response (platform-managed infrastructure failures)
- **Security Engineers**: 1 FTE
  - Detection logic (Kafka Streams applications)
  - Enrichment workflows

**Staffing Evidence**: Staffing calculator (2.0-2.2× multiplier for managed services vs 2.7× self-managed).

---

**Budget (Annual)**:
- **Staffing**: $1,850K (8 FTEs, per staffing calculator)
- **Managed Platform**: $90K (Confluent Cloud / AWS MSK)
- **Infrastructure**: $80K (ClickHouse, Trino compute)
- **Training**: $35K (Kafka Streams, managed platform training)
- **Incident Costs**: $50K (reduced - managed platform handles ops)
- **TOTAL ANNUAL**: **$2,105K** (~$2.1M/year)

**3-Year TCO**: **$6.9M** (per staffing calculator)

**Budget Evidence**: Staffing calculator, managed service pricing (Confluent Cloud, AWS MSK typical costs).

---

**Implementation Timeline**: 3-6 months

**Phase 1 (Months 1-2)**: Foundation
- Managed Kafka cluster provisioning (Confluent Cloud / MSK)
- Schema Registry setup
- Managed connector configuration (sources)
- Team: 3-4 FTEs

**Phase 2 (Months 3-4)**: Development
- Kafka Streams applications (3-5 critical use cases)
- Stateful processing (entity tracking, windowing)
- ClickHouse batch ingestion (Kafka → ClickHouse)
- Team: 6-7 FTEs

**Phase 3 (Months 5-6)**: Production Ramp-Up
- Production deployment
- Observability dashboards (Confluent Cloud metrics, CloudWatch)
- Runbooks (application-level incidents only, platform-managed infra)
- Team: 7-8 FTEs

**Timeline Evidence**: Managed services reduce timeline by 1-3 months (industry norm), staffing calculator accounts for reduced complexity.

---

**Performance Expectations**:
- **Ingestion**: 1-2M events/sec (managed Kafka autoscaling)
- **Processing Latency**: Sub-250ms (Kafka Streams, Confluent benchmarks)
- **Query Latency**: < 1s for historical queries (ClickHouse + Trino)

**Performance Evidence**: Confluent (Kafka Streams sub-250ms latency), ClickHouse (96% <1s queries).

---

**Break-Even Analysis**:
- **3-Year Cost Difference vs Batch**: $6.9M - $2.5M = **$4.4M**
- **Required Annual Business Value**: $1.47M/year (to break even in 3 years)

**Break-Even Scenarios**:
- **High-Value Ops** (incident costs > $3M/year): **1.8 years**
- **Moderate Ops** (incident costs $1-3M/year): **6.3 years**
- **Low-Value Ops** (incident costs < $1M/year): **Not viable**

**Break-Even Evidence**: Staffing calculator (TCO models).

---

**Technology Stack**:
- **Streaming**: Confluent Cloud (managed Kafka) or AWS MSK
- **Processing**: Kafka Streams 3.6+ or ksqlDB (Confluent managed)
- **Hot Storage**: ClickHouse 23.8+ (self-managed or ClickHouse Cloud)
- **Cold Storage**: Apache Iceberg 1.4+
- **Query**: Trino 435+ (Iceberg native)

---

**Risks & Mitigations**:

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Kafka Streams learning curve (6-12 months) | High | Medium ($200K-400K) | Training ($35K/year), Confluent professional services |
| Managed platform limitations (control) | Medium | Low | Evaluate requirements (most security use cases fit managed constraints) |
| Vendor lock-in (Confluent Cloud) | Low | Medium | Use open-source Kafka Streams (portable), AWS MSK alternative |

---

**Key Decision Factors**:
- ✅ **Strong Fit**: No streaming expertise, budget $1.5-2.5M/year, team 7-8 FTEs, faster time to production
- ⚠️ **Moderate Fit**: Some Kafka experience, budget $1.2-1.5M/year, managed platform acceptable
- ❌ **Poor Fit**: Compliance requires full control, budget < $1.2M/year, team < 6 FTEs

---

### RECOMMENDATION 3: Hybrid - Managed Kafka + Batch

**When to Choose**:
- Near real-time detection acceptable (1-15 minutes)
- Team size limited (5-6 FTEs, cannot grow to 7-8)
- Budget capacity $1.2-1.8M/year
- Managed Kafka for ingestion buffer, batch for primary analytics

---

**Architecture**:
```
Ingestion:
- Managed Kafka (buffer, 7-30 days retention)
- Kafka Connect (managed connectors for sources)

Stream Processing (Lightweight):
- Kafka Streams (critical alerts only, 2-3 use cases)
- Stateless or minimal state (simple filtering, enrichment)

Batch Processing (Primary):
- Batch ETL (Airflow, dbt) → Iceberg tables
- Kafka → Iceberg (hourly or daily loads)

Storage:
- Hot: Kafka (7-30 days, real-time buffer)
- Warm: ClickHouse (batch loaded, 30-90 days)
- Cold: Iceberg (multi-year, tiered S3)

Query:
- Critical Alerts: Kafka Streams (real-time, limited use cases)
- Investigation: Trino + Iceberg (batch queries, primary workflow)
```

---

**Team Composition** (5-6 FTEs):
- **Stream Processing Engineer**: 1 FTE (Kafka Streams for critical alerts only)
- **Data Engineers**: 2 FTEs (batch ETL, Kafka → Iceberg, Kafka Streams occasional support)
- **Platform Engineer**: 1 FTE (managed Kafka + batch infrastructure)
- **Security Engineer**: 1 FTE (detection logic, batch + limited real-time)

**Staffing Evidence**: Hybrid approach reduces streaming burden to 1-2 FTEs (vs 3-4 for full streaming), batch remains primary (3-4 FTEs baseline).

---

**Budget (Annual)**:
- **Staffing**: $1,100K (5.5 FTEs average)
- **Managed Kafka**: $60K (moderate scale, buffer only)
- **Infrastructure**: $100K (ClickHouse, Trino, Iceberg storage)
- **Training**: $25K
- **TOTAL ANNUAL**: **$1,285K** (~$1.3M/year)

**3-Year TCO**: **$4.3M**

---

**Implementation Timeline**: 3-5 months

**Phase 1 (Months 1-2)**: Foundation
- Managed Kafka setup (buffer)
- Batch ETL framework (Airflow, dbt)
- Team: 3-4 FTEs

**Phase 2 (Months 3-4)**: Development
- Batch pipelines (Kafka → Iceberg)
- Kafka Streams (2-3 critical alert use cases)
- ClickHouse setup (batch loaded)
- Team: 5 FTEs

**Phase 3 (Month 5)**: Production
- Production deployment
- Observability (Kafka + batch)
- Team: 5-6 FTEs (steady state)

---

**Break-Even Analysis**:
- **3-Year Cost Difference vs Batch**: $4.3M - $2.5M = **$1.8M**
- **Required Annual Business Value**: $600K/year

**Break-Even**: 3-4 years (moderate-value ops)

---

**Key Decision Factors**:
- ✅ **Strong Fit**: Team 5-6 FTEs (cannot grow to 8), budget $1.2-1.8M/year, most use cases tolerate 1-15 min latency
- ⚠️ **Moderate Fit**: Limited critical alerts (2-3 use cases require real-time), batch primary workflow
- ❌ **Poor Fit**: Real-time required for most use cases (full streaming needed), team < 5 FTEs

---

### RECOMMENDATION 4: Batch - ClickHouse + Iceberg (High-Volume OLAP)

**When to Choose**:
- Batch processing acceptable (15-60 minutes)
- Data volume > 1 TB/day
- Interactive query performance critical (< 1 second)
- Security-specific optimizations required (IP/CIDR queries, time-series)

---

**Architecture**:
```
Ingestion:
- Kafka (optional buffer, 7-30 days) → Batch ETL (hourly/daily)
- Direct ingestion (log shippers, API pulls) → Staging → ClickHouse

Storage:
- Hot: ClickHouse (7-30 days, sub-second queries)
- Cold: Iceberg (multi-year, tiered S3)

Query:
- Interactive: ClickHouse (analyst dashboards, ad-hoc queries)
- Historical: Trino + Iceberg (multi-year threat hunting)
```

---

**Team Composition** (3.5 FTEs, baseline):
- **Data Engineers**: 2 FTEs (batch ETL, ClickHouse optimization)
- **Platform Engineer**: 1 FTE (infrastructure, observability)
- **Security Engineer**: 0.5 FTE (detection logic, use case development)

---

**Budget (Annual)**:
- **Staffing**: $668K (3.5 FTEs, per staffing calculator)
- **Infrastructure**: $60K (ClickHouse compute, S3 storage)
- **Training**: $20K
- **TOTAL ANNUAL**: **$748K**

**3-Year TCO**: **$2.5M** (baseline from staffing calculator)

---

**Implementation Timeline**: 2-4 months

**Phase 1 (Month 1)**: Foundation
- ClickHouse deployment (cluster or cloud)
- Iceberg table setup
- Team: 2-3 FTEs

**Phase 2 (Months 2-3)**: Development
- Batch ingestion pipelines
- ClickHouse schema optimization (ORDER BY, PARTITION BY)
- Security use case development
- Team: 3.5 FTEs

**Phase 3 (Month 4)**: Production
- Production rollout
- Observability dashboards
- Team: 3.5 FTEs (steady state)

---

**Performance Expectations**:
- **Ingestion**: 1.8-2.2M events/sec per node (ClickHouse benchmarks)
- **Query Latency**: 96% queries < 1 second (Cloudflare production)
- **Production Scale**: 57TB/day validated (Shell security telemetry)
- **CIDR Queries**: 50-100× faster vs traditional databases (native IP types)

**Performance Evidence**: ClickHouse (Cloudflare 96% <1s, Shell 57TB/day), native IP types (50-100× speedup).

---

**Security-Specific Advantages**:
- **Native IP Types**: IPv4/IPv6 native types, CIDR queries 50-100× faster
- **Time-Series Optimization**: Optimized for temporal security event data
- **Compression**: 10-12× compression ratio, 75-85% storage reduction vs Elasticsearch
- **Analyst Productivity**: 40% increase, 70% faster investigations (Altinity)

**Security Evidence**: security-performance-advantages.md (8 sources, 100% Level A).

---

**Technology Stack**:
- **OLAP**: ClickHouse 23.8+ (native IP types, TTL policies)
- **Storage**: Apache Iceberg 1.4+ (lifecycle policies, snapshot isolation)
- **Query**: ClickHouse (hot queries), Trino 435+ (historical Iceberg)
- **Orchestration**: Airflow 2.7+ or dbt 1.6+

---

**Key Decision Factors**:
- ✅ **Strong Fit**: High-volume (TB+/day), sub-second query latency required, IP/CIDR-heavy workloads, batch acceptable
- ⚠️ **Moderate Fit**: Moderate volume (100GB-1TB/day), some real-time required (consider hybrid)
- ❌ **Poor Fit**: Real-time detection required, low volume (< 100GB/day, overkill)

---

### RECOMMENDATION 5: Batch - Trino + Iceberg (Moderate Volume, Federation)

**When to Choose**:
- Batch processing acceptable (15-60 minutes)
- Data volume 100GB-1TB/day
- Federation required (multiple data sources: S3, JDBC, APIs)
- Query latency 1-5 seconds acceptable

---

**Architecture**:
```
Ingestion:
- Batch ETL (Airflow, dbt) → Iceberg tables (S3/Azure Blob)
- Kafka (optional buffer) → Batch loads (hourly)

Storage:
- Iceberg (unified format, multi-year retention)
- Tiered storage (hot/warm/cold lifecycle)

Query:
- Trino (federated SQL across Iceberg + PostgreSQL + MySQL + Elasticsearch)
- 40+ connectors for heterogeneous sources
```

---

**Team Composition** (3.5 FTEs, baseline):
- **Data Engineers**: 2 FTEs (batch ETL, Iceberg optimization)
- **Platform Engineer**: 1 FTE (Trino cluster, observability)
- **Security Engineer**: 0.5 FTE (detection logic)

---

**Budget (Annual)**:
- **Staffing**: $668K (3.5 FTEs)
- **Infrastructure**: $50K (Trino compute, S3 storage)
- **Training**: $20K
- **TOTAL ANNUAL**: **$738K**

**3-Year TCO**: **$2.3M**

---

**Implementation Timeline**: 2-4 months

---

**Performance Expectations**:
- **Query Latency**: 1-5 seconds (typical Trino queries)
- **Scale**: Petabyte-scale validated (Meta production)
- **Federation**: Unified SQL across 40+ data sources

**Performance Evidence**: Trino (Meta petabyte-scale, 10-100× faster than Hive).

---

**Technology Stack**:
- **Query Engine**: Trino 435+ (Iceberg native, Arrow Flight SQL 20× faster)
- **Storage**: Apache Iceberg 1.4+ (time travel, schema evolution)
- **Orchestration**: Airflow 2.7+ or dbt 1.6+

---

**Key Decision Factors**:
- ✅ **Strong Fit**: Moderate volume (100GB-1TB/day), federation required, batch acceptable
- ⚠️ **Moderate Fit**: High-volume (TB+/day, ClickHouse may be better), sub-second latency required
- ❌ **Poor Fit**: Real-time detection required, low volume (< 100GB/day, simpler options exist)

---

### RECOMMENDATION 6: Batch - Iceberg + Tiered Storage (Multi-Year Compliance)

**When to Choose**:
- Multi-year queryable retention required (2-7 years)
- Compliance-driven (SOX, PCI-DSS, HIPAA, GDPR)
- Cost optimization critical (55-80% storage savings)
- Audit log immutability required

---

**Architecture**:
```
Ingestion:
- Batch ETL → Iceberg tables (S3/Azure Blob with tiered storage)

Storage Lifecycle:
- Hot (0-30 days): S3 Standard ($0.023/GB, frequent access)
- Warm (30-365 days): S3 Intelligent-Tiering ($0.0125/GB, infrequent)
- Cold (365+ days): S3 Glacier Instant Retrieval ($0.004/GB, rare access)

Query:
- Trino (unified SQL across all tiers, seamless tier transitions)
- Iceberg time travel (historical snapshots, audit trails)
```

---

**Cost Savings**: 55-80% storage cost reduction

**Example**:
- 1 PB retention (7 years)
- Without tiering: $23,000/month ($0.023/GB × 1M GB)
- With tiering: $9,200/month (55% savings) to $4,600/month (80% savings)
- **Annual Savings**: $165K (55%) to $220K (80%)

**Cost Evidence**: AWS (55% average savings), Netflix (70-80% with Kafka tiered storage).

---

**Team Composition** (3.5 FTEs, baseline):
- **Data Engineers**: 2 FTEs (Iceberg lifecycle policies)
- **Platform Engineer**: 1 FTE (storage management, cost monitoring)
- **Security Engineer**: 0.5 FTE (detection logic)

---

**Budget (Annual)**:
- **Staffing**: $668K (3.5 FTEs)
- **Infrastructure**: $40K (Trino compute, tiered storage optimized)
- **Training**: $20K
- **TOTAL ANNUAL**: **$728K**

**3-Year TCO**: **$2.3M** (similar to baseline batch, storage cost savings offset other expenses)

---

**Implementation Timeline**: 2-4 months

---

**Technology Stack**:
- **Storage**: Apache Iceberg 1.4+ (lifecycle policies, snapshot isolation)
- **Object Storage**: S3 Intelligent-Tiering, Glacier Instant Retrieval
- **Query**: Trino 435+ (Iceberg native, cross-tier queries)

---

**Key Decision Factors**:
- ✅ **Strong Fit**: Multi-year retention (2-7 years), compliance-driven, cost optimization critical
- ⚠️ **Moderate Fit**: 6-12 months retention (tiering less impactful)
- ❌ **Poor Fit**: 30-90 days retention (single-tier sufficient), real-time required

---

## Summary: Quick Selection Matrix

| Scenario | Architecture | Team Size | Budget (Annual) | 3-Year TCO | Timeline | Key Advantage |
|----------|-------------|-----------|----------------|-----------|----------|---------------|
| **Real-time, Expert Team, High Budget** | Self-Managed Streaming (Kafka + Flink) | 9-11 FTEs | $2.3M | $7.9M | 6-9 months | Full control, custom processing |
| **Real-time, No Expertise, Moderate Budget** | Managed Streaming (Confluent/MSK) | 7-8 FTEs | $2.1M | $6.9M | 3-6 months | Reduced ops burden, faster time |
| **Near Real-time, Limited Team** | Hybrid (Managed Kafka + Batch) | 5-6 FTEs | $1.3M | $4.3M | 3-5 months | Balance real-time + batch, small team viable |
| **Batch, High-Volume OLAP** | ClickHouse + Iceberg | 3.5 FTEs | $748K | $2.5M | 2-4 months | Sub-second queries, IP/CIDR optimizations |
| **Batch, Federation Required** | Trino + Iceberg | 3.5 FTEs | $738K | $2.3M | 2-4 months | 40+ connectors, unified SQL |
| **Batch, Multi-Year Compliance** | Iceberg + Tiered Storage | 3.5 FTEs | $728K | $2.3M | 2-4 months | 55-80% storage savings, immutable audit |
| **Batch, Low Volume** | DuckDB or Trino | 3 FTEs | $668K | $2.0M | 2-3 months | Minimal ops overhead, embedded or cloud |

---

**Author**: Jeremy Wiley
**Date**: October 15, 2025
**Evidence Quality**: 94% Level A (consolidated from cost-reality, implementation-reality, performance-benchmarks)
**Status**: Ready for book integration (Chapter 6 Decision Framework)
