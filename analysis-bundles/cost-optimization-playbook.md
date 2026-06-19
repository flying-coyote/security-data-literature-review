---
type: reference
title: "Security Data Platform Cost Optimization Playbook"
created: 2025-10-15
tags: [cost-optimization, tiered-storage, tco, clickhouse, iceberg, security-data-platform]
---

# Cost Optimization Playbook

**Purpose**: Actionable strategies for reducing security data platform costs by 40-80%
**Evidence Source**: `cost-reality-reference.md` (12 sources, 92% Evidence Level A)
**Last Updated**: October 15, 2025
**Use Case**: Chapter 1 (Cost Comparisons), Chapter 4 (Implementation Journeys), practitioner cost reduction

---

## Executive Summary

This playbook provides evidence-based cost optimization strategies for security data platforms. All recommendations are validated across production deployments and quantified savings estimates.

**Key Optimization Areas**:
1. **Tiered Storage** - 55-80% storage cost reduction (AWS, Netflix)
2. **Streaming TCO Reality** - Avoid 2.5-3× hidden operational costs (IDC, DORA)
3. **Reliability Economics** - Right-size SLAs (each "nine" = 10× cost)
4. **Query Optimization** - 70% investigation time reduction (Altinity ClickHouse)
5. **Staffing Efficiency** - Managed services save 1-2 FTEs (30-40% ops reduction)

**Impact Potential**: $500K-2M/year savings for mid-sized security operations

---

## Optimization Strategy 1: Tiered Storage Implementation

### Problem Statement

**Cost Reality**:
- Hot storage (S3 Standard): $0.023/GB/month
- 1 PB retention: $23,000/month = $276K/year
- Multi-year compliance (7 years): $1.9M/year storage costs

**Opportunity**: 55-80% cost reduction with hot/warm/cold tiering

---

### Solution: Iceberg Lifecycle Policies + S3 Intelligent-Tiering

**Architecture**:
```
Data Ingestion → Apache Iceberg Tables (S3)

Automatic Lifecycle Transitions:
- Days 0-30: S3 Standard ($0.023/GB) - Frequent access (dashboards, active investigations)
- Days 30-365: S3 Intelligent-Tiering ($0.0125/GB) - Infrequent access (historical context)
- Days 365+: S3 Glacier Instant Retrieval ($0.004/GB) - Rare access (compliance, audit)

Query Layer: Trino (unified SQL across all tiers, seamless access)
```

**Evidence**: Netflix (70-80% storage cost reduction with Kafka tiered storage), AWS (55% average savings with tiered strategies).

---

### Implementation Steps

**Step 1: Analyze Access Patterns** (Week 1)

Determine hot/warm/cold data boundaries:
- [ ] Query analytics: Which date ranges are accessed most frequently?
- [ ] Investigation workflows: How often do analysts query data > 90 days old?
- [ ] Compliance requirements: What is minimum queryable retention?

**Tool**: S3 Access Analyzer, ClickHouse query logs, Trino query history

**Example Findings**:
- 80% of queries target last 30 days (hot tier)
- 15% of queries target 30-365 days (warm tier)
- 5% of queries target 365+ days (cold tier, compliance-driven)

---

**Step 2: Configure Iceberg Lifecycle Policies** (Week 2)

Create Iceberg table with lifecycle rules:
```sql
CREATE TABLE security_logs (
  timestamp TIMESTAMP,
  source_ip VARCHAR,
  event_type VARCHAR,
  ...
)
PARTITIONED BY (days(timestamp))
TBLPROPERTIES (
  'write.format.default' = 'parquet',
  'write.parquet.compression-codec' = 'zstd',
  'expire_snapshots.enabled' = 'true',
  'expire_snapshots.older_than_days' = '7'
);
```

Configure S3 Lifecycle Policy:
```json
{
  "Rules": [
    {
      "Id": "TransitionToIA",
      "Filter": {"Prefix": "data/"},
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "INTELLIGENT_TIERING"
        },
        {
          "Days": 365,
          "StorageClass": "GLACIER_IR"
        }
      ]
    }
  ]
}
```

**Validation**: Test queries across all tiers (verify performance degradation acceptable)

---

**Step 3: Monitor Cost Savings** (Ongoing)

**Metrics**:
- Storage costs by tier (S3 cost allocation tags)
- Query latency by tier (Trino query logs)
- Data retrieval costs (S3 retrieval fees)

**Tool**: AWS Cost Explorer, Grafana dashboards (S3 metrics), Trino query performance

**Expected Savings**:
- **Conservative (55% savings)**: $276K → $124K/year = **$152K savings**
- **Optimistic (80% savings)**: $276K → $55K/year = **$221K savings**

---

### ROI Analysis

**Investment**:
- Implementation time: 2-3 weeks (1 data engineer)
- Cost: ~$10K (staff time)
- Ongoing monitoring: 2-4 hours/month

**Return**:
- Annual savings: $152K-221K (depending on access patterns)
- ROI: 15× to 22× (first year)
- Payback period: < 1 month

**Evidence**: AWS tiered storage whitepapers, Netflix production deployment (70-80% reduction).

---

### Red Flags: When Tiering Doesn't Work

- [ ] **High cold data access**: If > 20% of queries target 365+ days, retrieval fees may offset savings
- [ ] **Compliance requires hot access**: Some regulations mandate sub-second access to all data (rare)
- [ ] **Small data volume**: < 100 GB total (tiering overhead > savings)

---

## Optimization Strategy 2: Avoid Premature Streaming

### Problem Statement

**Streaming Cost Reality**:
- Streaming architecture: $2.1M-2.3M/year (managed to self-managed)
- Batch architecture: $668K/year
- **Cost Multiplier**: 3.1-3.4× (streaming vs batch)

**Evidence**: IDC (2.5-3× higher operational staffing costs), DORA (2.7× operational staff), staffing calculator (consolidates 7 sources).

---

### Solution: Batch-First with Selective Streaming

**Decision Framework**:

**Choose Batch When**:
- Detection SLA > 15 minutes acceptable (80% of security use cases)
- Investigation workflows > response automation
- Team size < 7 FTEs (insufficient for streaming 2.7× multiplier)
- Budget < $1.5M/year
- No existing Kafka/Flink expertise (6-12 month ramp-up)

**Choose Streaming Only When**:
- Real-time detection required (< 1 minute SLA) for mission-critical workflows
- Incident costs > $3M/year (streaming ROI justifiable with 50-70% MTTR reduction)
- Team size > 7 FTEs with Level 4 streaming expertise
- Budget > $1.5M/year
- Business value > $1.5M/year (break-even 3-4 years)

**Evidence**: Staffing calculator (break-even analysis), DORA (Level 4 skills = top 5% orgs), Gartner (streaming expertise scarcity).

---

### Implementation Steps

**Step 1: Audit Detection Latency Requirements** (Week 1)

For each detection use case:
- [ ] What is the current detection latency? (SIEM alert delay)
- [ ] What is the business impact of 5-minute delay? 15-minute delay?
- [ ] Is automated response required (< 5 min) or analyst-driven (15-60 min)?

**Example Findings**:
- **Critical (5% of use cases)**: Automated account lockout, DDoS mitigation → Real-time required
- **High Priority (15% of use cases)**: Threat hunting dashboards → 5-15 min acceptable
- **Standard (80% of use cases)**: Compliance monitoring, historical analysis → 15-60 min acceptable

**Recommendation**: Implement batch for 80% of use cases, evaluate hybrid (managed Kafka + batch) for top 20%.

---

**Step 2: Quantify Batch vs Streaming TCO** (Week 2)

Use staffing calculator to compare 3-year TCO:

**Scenario A: Batch-Only**
- Team: 3.5 FTEs
- 3-Year TCO: $2.5M
- Coverage: 80% of use cases (15-60 min latency)

**Scenario B: Hybrid (Managed Kafka + Batch)**
- Team: 5-6 FTEs
- 3-Year TCO: $4.3M
- Coverage: 95% of use cases (5-60 min latency)
- **Premium**: $1.8M (vs batch-only)

**Scenario C: Full Streaming (Managed)**
- Team: 7-8 FTEs
- 3-Year TCO: $6.9M
- Coverage: 100% of use cases (< 1 min latency)
- **Premium**: $4.4M (vs batch-only)

**Question**: Does the 5% additional coverage (Scenario C vs B) justify $2.6M premium?

**Evidence**: Staffing calculator (TCO models from 7 sources, 90% Evidence Level A).

---

**Step 3: Pilot Batch, Defer Streaming Decision** (Months 1-6)

**Batch Pilot** (2-4 months):
- Implement batch architecture (ClickHouse/Trino + Iceberg)
- Measure detection coverage (% of use cases satisfied with 15-60 min latency)
- Measure analyst satisfaction (investigation workflow latency acceptable?)
- Measure incident impact (did batch latency cause missed detections?)

**Decision Point** (Month 6):
- If 90%+ use cases satisfied: Continue batch-only (save $4.4M over 3 years)
- If critical gaps identified: Evaluate hybrid (managed Kafka for top 10% use cases)
- If real-time essential for most workflows: Full streaming (justify $4.4M premium with business value)

**Evidence**: Phased approach reduces risk (Gartner implementation best practices), pilot validates assumptions before major investment.

---

### Cost Savings Example

**Mid-Sized Security Operations** (10 analysts, 500GB/day):
- **Premature Streaming**: $6.9M (3-year TCO, managed)
- **Batch-First**: $2.5M (3-year TCO)
- **SAVINGS**: **$4.4M** (64% cost reduction)

**Rationale**: Batch satisfies 90% of use cases (investigation workflows, compliance), streaming premium unjustified.

---

### Red Flags: When Streaming is Justified

- [ ] **Automated response critical**: SOAR-driven containment, sub-5 min response required
- [ ] **High incident costs**: > $3M/year, streaming 50-70% MTTR reduction = $1.5-2M/year savings
- [ ] **Regulatory requirements**: Real-time fraud detection (financial services), PCI-DSS sub-minute alerting
- [ ] **Existing Kafka expertise**: Team has Level 4 streaming skills (avoids 6-12 month ramp-up)

---

## Optimization Strategy 3: Right-Size Reliability SLAs

### Problem Statement

**Reliability Economics**:
- Each additional "nine" (e.g., 99% → 99.9% uptime) = 10× cost increase (DORA)
- Many organizations overspend on reliability beyond business needs

**Example**:
- 99% uptime (3.65 days downtime/year): $100K/year infrastructure
- 99.9% uptime (8.76 hours downtime/year): $1M/year infrastructure
- 99.99% uptime (52.6 minutes downtime/year): $10M/year infrastructure

**Evidence**: DORA State of DevOps 2024 (exponential reliability cost curve), AWS reliability whitepapers.

---

### Solution: Tiered Reliability by Workload Criticality

**Classification Framework**:

| Tier | Use Case | Target SLA | Acceptable Downtime | Infrastructure Cost |
|------|----------|-----------|-------------------|-------------------|
| **Critical** | Real-time detection, automated response | 99.9% | 8.76 hours/year | High (redundant, multi-AZ) |
| **High Priority** | Investigation dashboards, threat hunting | 99% | 3.65 days/year | Moderate (single-region, backups) |
| **Standard** | Compliance reporting, historical analysis | 95% | 18.25 days/year | Low (best-effort, batch processing) |

**Evidence**: Segment blog (reliability cost curve), DORA (10× per nine), AWS Well-Architected Framework.

---

### Implementation Steps

**Step 1: Classify Workloads by Business Impact** (Week 1)

For each security data workload:
- [ ] What is the business impact of 1-hour outage? 1-day outage?
- [ ] Is manual workaround available during outage?
- [ ] What is historical uptime requirement?

**Example Classification**:
- **Critical (10% of workloads)**: Automated threat response, real-time dashboards for SOC → 99.9% SLA
- **High Priority (30% of workloads)**: Analyst investigation tools, threat hunting → 99% SLA
- **Standard (60% of workloads)**: Compliance reporting, historical queries, weekly reviews → 95% SLA

---

**Step 2: Design Infrastructure by Tier** (Week 2-3)

**Critical Tier (99.9% SLA)**:
- Multi-AZ deployment (3 availability zones)
- Automated failover (< 5 minute RTO)
- Redundant components (load balancers, databases)
- 24/7 on-call (DORA: streaming requires always-on ops)
- **Cost**: $300K/year (example: Kafka + Flink with multi-AZ)

**High Priority Tier (99% SLA)**:
- Single-region, multi-node (2-3 nodes)
- Manual failover acceptable (< 1 hour RTO)
- Backups (hourly snapshots)
- Business hours on-call
- **Cost**: $80K/year (example: ClickHouse 3-node cluster)

**Standard Tier (95% SLA)**:
- Best-effort availability
- Batch processing (scheduled jobs, can tolerate delays)
- Daily backups
- No on-call (fix during business hours)
- **Cost**: $20K/year (example: Trino single-node or spot instances)

---

**Step 3: Monitor and Adjust** (Ongoing)

**Metrics**:
- Actual uptime by tier (vs target SLA)
- Incident frequency and impact (cost of downtime)
- Infrastructure cost by tier

**Adjustment Triggers**:
- If actual uptime consistently exceeds SLA (e.g., 99.95% vs 99% target): Consider downgrading infrastructure (cost savings)
- If incidents cause significant business impact: Consider upgrading SLA tier

---

### Cost Savings Example

**Before Optimization** (All workloads treated as critical):
- 10 workloads × $300K/year (99.9% SLA) = **$3M/year**

**After Optimization** (Tiered reliability):
- 1 critical workload × $300K = $300K
- 3 high-priority workloads × $80K = $240K
- 6 standard workloads × $20K = $120K
- **TOTAL**: **$660K/year**

**SAVINGS**: **$2.34M/year** (78% reduction)

---

### Red Flags: When Higher SLA is Justified

- [ ] **Regulatory requirements**: Financial services (real-time fraud), healthcare (patient safety)
- [ ] **Automated response**: Sub-minute detection + containment (ransomware, DDoS)
- [ ] **High incident costs**: > $100K/hour downtime impact (large enterprises)
- [ ] **Reputational risk**: Public-facing security (breach disclosure, customer trust)

---

## Optimization Strategy 4: Query Performance Optimization

### Problem Statement

**Investigation Time = Analyst Cost**:
- Security analyst: $130K/year salary ($236K total comp with 1.35× multiplier)
- Average investigation: 4-6 hours (traditional SIEM)
- Query latency: 30-60 seconds per query (Elasticsearch/Splunk)
- **Opportunity**: 70% investigation time reduction = 40% analyst productivity increase (Altinity)

**Evidence**: Altinity ClickHouse case study (70% reduction in MTTR, 40% analyst productivity increase).

---

### Solution: OLAP Query Engine + Native IP Types

**Architecture**:
```
Hot Data (0-30 days): ClickHouse (sub-second queries, native IP types)
Warm/Cold (30+ days): Iceberg + Trino (federated SQL)

Query Optimization:
- Native IPv4/IPv6 types (50-100× faster CIDR queries)
- Time-series partitioning (partition pruning)
- Columnar compression (10-12× storage reduction = faster scans)
- Materialized views (pre-aggregated metrics)
```

**Evidence**: ClickHouse (96% queries < 1s at Cloudflare, 50-100× faster CIDR queries with native IP types), Iceberg (97% query time reduction at SK Telecom).

---

### Implementation Steps

**Step 1: Benchmark Current Query Performance** (Week 1)

Measure baseline performance:
- [ ] Average query latency (P50, P90, P99)
- [ ] Slowest queries (top 10% by execution time)
- [ ] Query patterns (IP/CIDR filters, time ranges, JOINs)
- [ ] Analyst investigation time (average hours per incident)

**Tool**: SIEM query logs, analyst surveys, incident timestamps

**Example Baseline**:
- P50 latency: 15 seconds
- P90 latency: 45 seconds
- P99 latency: 120 seconds
- Average investigation time: 5 hours (includes 80-100 queries)

---

**Step 2: Optimize Schema Design** (Week 2)

**ClickHouse Schema Optimization**:
```sql
CREATE TABLE security_events (
  timestamp DateTime64(3),
  source_ip IPv4,               -- Native IP type (50-100× faster CIDR)
  destination_ip IPv4,
  event_type LowCardinality(String), -- Dictionary encoding for enums
  payload String,
  user_agent String
)
ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(timestamp)  -- Daily partitions (partition pruning)
ORDER BY (timestamp, source_ip, event_type); -- Optimized for time-series + IP queries
```

**Key Optimizations**:
- **Native IP types**: IPv4/IPv6 instead of String (50-100× faster CIDR matching)
- **Partition by time**: Daily partitions enable partition pruning (skip irrelevant data)
- **ORDER BY**: Defines sort order on disk (co-locate related events)
- **LowCardinality**: Dictionary encoding for low-cardinality strings (enums, fixed values)

**Evidence**: ClickHouse IP address types documentation (50-100× CIDR speedup), Percona time-series optimization.

---

**Step 3: Create Materialized Views for Common Queries** (Week 3)

Pre-aggregate frequent queries:
```sql
CREATE MATERIALIZED VIEW top_attackers_hourly
ENGINE = SummingMergeTree()
PARTITION BY toYYYYMMDD(timestamp)
ORDER BY (timestamp, source_ip)
AS
SELECT
  toStartOfHour(timestamp) AS timestamp,
  source_ip,
  count() AS event_count,
  uniq(destination_ip) AS unique_targets
FROM security_events
GROUP BY timestamp, source_ip;
```

**Use Case**: "Top attackers in last 24 hours" query (common threat hunting)
- **Before**: Full-corpus base-table scan on every refresh
- **After**: Serve the panel from a pre-aggregated materialized view

In the SDW lab I measured this directly on three SOC-dashboard panels against 20M OCSF events (single host, read latencies as medians with CV, answers verified identical between the two paths): the read speedup runs 45.3× (failed-auth-by-user), 53.6× (5-minute time series), and 76.8× (class rollup) [Tier B, `sdw-lab-benchmarks/ocsf-mv-acceleration`, H-MV-SECURITY-01]. That sits at the low end of the vendor-reported 78× to 9,000× range (Tier C/D: PostgreSQL/Snowflake/Databricks vendor benchmarks, best-case workloads, not independently reproduced), which is what I'd expect, since the published figures are favorable-workload best cases and a 709 MB base table on one machine is not where the 9,000× numbers come from. The transferable finding is the trade, not the magnitude: the MV is a bet that a fixed set of always-on questions is worth paying per-batch maintenance and storage to answer fast, so an ad-hoc pivot, a new filter, or a hunt still pays the base scan.

One caveat worth stating before anyone reaches for materialized views as a concurrency fix: the speedup above is per-query compute, and it buys no headroom under load. In the interference benchmark (single host, an open-loop scheduled workload running alongside ad-hoc queries) the StarRocks arm and the same arm backed by six EXPLAIN-verified materialized views both knee at the same scheduled rate — the MV layer did not shift the knee right at all [Tier B, `sdw-lab-benchmarks/workload-interference`, P5; one MV run, the base knee is reproduced 3× but the MV result wants reproduction for a firm claim]. The reading is that at the knee the binding constraint is open-loop scheduler and per-query coordinator saturation, not the per-query compute the MVs accelerate, so even a near-instant MV-rewritten query still pays the fixed per-query overhead the scheduler is drowning in. So an MV is the right tool for a slow but uncontended dashboard, and the wrong tool for a system that's tipping over because too many queries arrive at once, where the headroom comes from the engine's scheduler and coordinator rather than from pre-aggregating the answers.

---

**Step 4: Measure Performance Improvement** (Week 4+)

**Metrics**:
- Query latency reduction (P50, P90, P99)
- Investigation time reduction (hours per incident)
- Analyst productivity (incidents handled per analyst)

**Expected Results** (based on Altinity case study):
- Query latency: 15s → 0.5s (30× faster, P50)
- Investigation time: 5 hours → 1.5 hours (70% reduction)
- Analyst productivity: 40% increase (equivalent to hiring 2 additional analysts per 5-person team)

---

### Cost Savings Example

**Analyst Productivity Gains**:
- **Before**: 5 analysts × 5 hours/investigation × 200 investigations/year = 5,000 hours
- **After**: 5 analysts × 1.5 hours/investigation × 200 investigations/year = 1,500 hours
- **Time Savings**: 3,500 hours = 40% productivity increase

**Equivalent Cost Savings**:
- 40% productivity increase = capacity for 2 additional analysts
- 2 analysts × $236K total comp = **$472K/year equivalent capacity**

**Or**: Avoid hiring 2 additional analysts (headcount cost avoidance)

**Evidence**: Altinity ClickHouse security analytics case study (70% MTTR reduction, 40% productivity increase).

---

### ROI Analysis

**Investment**:
- ClickHouse migration: 2-4 weeks (1 data engineer)
- Schema optimization: 1 week
- Materialized views: 1 week
- **Total Cost**: ~$20K (staff time)

**Return**:
- Analyst productivity: $472K/year (equivalent capacity)
- Or: Headcount avoidance (2 analysts)
- **ROI**: 23× (first year)

---

## Optimization Strategy 5: Staffing Efficiency (Managed Services)

### Problem Statement

**Self-Managed Streaming Staffing**:
- 9-11 FTEs required (DORA 2.7× multiplier)
- 24/7 on-call rotation (3-4 FTEs minimum for sustainable rotation)
- Specialized skills premium (1.5-2× salary, MIT Technology Review)
- Annual cost: $1,972K/year (per staffing calculator)

**Opportunity**: Managed services reduce ops burden by 30-40%

**Evidence**: Staffing calculator (managed 2.0-2.2× vs self-managed 2.7×), industry patterns.

---

### Solution: Managed Kafka/Streaming Platforms

**Managed Platform Options**:
- **Confluent Cloud**: Fully managed Kafka, Schema Registry, connectors, ksqlDB
- **AWS MSK**: Managed Kafka (AWS-native), integration with AWS Glue (schema registry)
- **Azure Event Hubs**: Kafka-compatible, Azure-native streaming

**Staffing Reduction**:
- **Self-Managed**: 9-11 FTEs (2.7× multiplier)
- **Managed**: 7-8 FTEs (2.0-2.2× multiplier)
- **Savings**: 1.5-3 FTEs = $350K-700K/year

---

### Implementation Steps

**Step 1: Evaluate Managed Platform Viability** (Week 1)

Determine if managed platforms meet requirements:
- [ ] Data sovereignty: Can data reside in managed platform (compliance check)?
- [ ] Connector availability: Are required connectors supported (Confluent Hub, MSK Connect)?
- [ ] Kafka version: Does managed platform support required Kafka features (tiered storage, KRaft)?
- [ ] Control requirements: Is full platform control required (rare)?

**Decision**:
- If all checks pass: Managed platform viable (proceed to cost analysis)
- If any fail: Self-managed required (optimization limited to other strategies)

---

**Step 2: Cost Comparison (Self-Managed vs Managed)** (Week 2)

**Self-Managed Streaming** (3-year TCO):
- Staffing: $1,972K/year × 3 = $5,916K
- Infrastructure: $150K/year × 3 = $450K
- Training: $50K/year × 3 = $150K
- Incidents: $100K/year × 3 = $300K
- **TOTAL**: **$6,816K** (~$6.8M)

**Managed Streaming** (3-year TCO):
- Staffing: $1,850K/year × 3 = $5,550K (reduced ops)
- Managed Platform: $90K/year × 3 = $270K (Confluent Cloud / MSK)
- Infrastructure: $80K/year × 3 = $240K (reduced - no cluster management)
- Training: $35K/year × 3 = $105K (reduced - platform handles ops)
- Incidents: $50K/year × 3 = $150K (reduced - managed platform failures)
- **TOTAL**: **$6,315K** (~$6.3M)

**SAVINGS**: **$501K** (7% reduction over 3 years)

**Plus**: 1-3 months faster time to production (3-6 months vs 6-9 months)

**Evidence**: Staffing calculator (consolidates managed service patterns from industry data).

---

**Step 3: Pilot Managed Platform** (Months 1-3)

Test managed platform with non-critical workload:
- [ ] Deploy managed Kafka cluster (Confluent Cloud / MSK)
- [ ] Configure connectors (source + sink)
- [ ] Validate performance (throughput, latency)
- [ ] Test incident response (managed platform support)

**Success Criteria**:
- Performance meets requirements (1-2M events/sec, sub-second latency)
- Operational burden reduced (no cluster management, automated patching)
- Support responsiveness acceptable (managed platform SLA)

---

### Cost Savings Example

**Mid-Sized Security Operations** (streaming required):
- **Self-Managed**: $6.8M (3-year TCO)
- **Managed**: $6.3M (3-year TCO)
- **SAVINGS**: **$500K** (7% reduction)

**Plus**:
- Faster time to production: 3 months earlier revenue/value
- Reduced risk: 30-40% lower ops burden, fewer streaming expertise requirements
- Headcount efficiency: 1.5-3 FTEs reallocated to value-added work (detection development)

---

### Red Flags: When Self-Managed is Required

- [ ] **Data sovereignty**: Compliance prohibits data in managed platforms (rare, government/defense)
- [ ] **Full control required**: Custom Kafka broker configurations, plugin development
- [ ] **Cost at massive scale**: Managed platform pricing > self-managed at petabyte scale (uncommon for security ops)
- [ ] **Existing Kafka expertise**: Team has Level 4 Kafka skills, self-managed no incremental burden

---

## Optimization Strategy 6: Schema Design & Compression

### Problem Statement

**Storage Costs**:
- Poor schema design: 75-85% wasted storage (Elasticsearch baseline)
- JSON/text formats: Minimal compression (1-2×)
- **Opportunity**: 10-12× compression with optimized schema + columnar formats

**Evidence**: Altinity ClickHouse (75-85% storage reduction vs Elasticsearch), ClickHouse benchmarks (10-12× compression typical).

---

### Solution: Columnar Formats + Schema Optimization

**Schema Design Principles**:
1. **Use appropriate data types**: Native types (IPv4, DateTime64) vs generic strings
2. **Normalize enums**: LowCardinality encoding for fixed values (event_type, severity)
3. **Partition by time**: Daily/hourly partitions (partition pruning)
4. **Columnar storage**: Parquet, ORC, or ClickHouse native format
5. **Compression codec**: Zstd (high compression ratio, fast decompression)

---

### Implementation Steps

**Step 1: Audit Current Schema** (Week 1)

Identify optimization opportunities:
- [ ] Are IP addresses stored as strings? (Convert to IPv4/IPv6 native types)
- [ ] Are timestamps strings? (Convert to DateTime64)
- [ ] Are enums stored as strings? (Apply LowCardinality encoding)
- [ ] What is current compression ratio? (baseline measurement)

**Example Audit**:
```sql
-- BAD: Poor schema design (generic strings)
CREATE TABLE events_bad (
  timestamp String,           -- Should be DateTime64
  source_ip String,           -- Should be IPv4
  event_type String,          -- Should be LowCardinality(String)
  payload String
);
-- Storage: 1 PB uncompressed, 500 GB compressed (2× compression)
```

---

**Step 2: Redesign Schema with Optimization** (Week 2)

```sql
-- GOOD: Optimized schema
CREATE TABLE events_optimized (
  timestamp DateTime64(3),    -- Native timestamp (microsecond precision)
  source_ip IPv4,             -- Native IP type (50-100× faster CIDR, 4 bytes vs 15+ bytes)
  destination_ip IPv4,
  event_type LowCardinality(String), -- Dictionary encoding (1-2 bytes per value)
  payload String CODEC(ZSTD(3))      -- High compression (Zstd level 3)
)
ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(timestamp)
ORDER BY (timestamp, source_ip);
-- Storage: 1 PB uncompressed, 80-100 GB compressed (10-12× compression)
```

**Compression Improvement**: 500 GB → 90 GB = **82% storage reduction**

---

**Step 3: Migrate Data** (Week 3-4)

```sql
-- Migrate from old schema to new schema
INSERT INTO events_optimized
SELECT
  parseDateTimeBestEffort(timestamp) AS timestamp,
  toIPv4(source_ip) AS source_ip,
  toIPv4(destination_ip) AS destination_ip,
  event_type,
  payload
FROM events_bad;
```

**Validation**: Compare query performance and storage size before/after.

---

### Cost Savings Example

**Storage Reduction**:
- **Before**: 1 PB uncompressed → 500 GB compressed (2× compression)
- **After**: 1 PB uncompressed → 90 GB compressed (11× compression)
- **Reduction**: 500 GB → 90 GB = **82% storage savings**

**Cost Impact**:
- S3 Standard: 500 GB × $0.023/GB = $11.50/month
- Optimized: 90 GB × $0.023/GB = $2.07/month
- **Savings**: $9.43/month × 12 = **$113/year per PB**

**Scaling**: 10 PB retention (multi-year) = **$1,130/year savings**

**Plus**:
- Query performance: 82% less data to scan = 2-5× faster queries
- Network transfer: 82% less data movement (S3 → query engine)

---

## Cost Optimization Checklist

### Quick Wins (0-3 Months, High ROI)

- [ ] **Tiered Storage Implementation** (2-3 weeks)
  - Expected Savings: $150K-220K/year (55-80% storage costs)
  - ROI: 15-22×
  - Effort: Low (Iceberg lifecycle + S3 policies)

- [ ] **Schema Optimization** (3-4 weeks)
  - Expected Savings: $100K-500K/year (query performance + storage)
  - ROI: 10-25×
  - Effort: Medium (schema redesign + migration)

- [ ] **Right-Size Reliability SLAs** (2-3 weeks)
  - Expected Savings: $500K-2M/year (avoid over-engineered infrastructure)
  - ROI: Variable (depends on current over-provisioning)
  - Effort: Low (workload classification + infrastructure tiering)

---

### Medium-Term Optimization (3-6 Months)

- [ ] **Batch-First Implementation** (2-4 months)
  - Expected Savings: $1.4-4.4M (3-year TCO vs streaming)
  - ROI: 64-75% cost reduction (vs premature streaming)
  - Effort: Medium (requires implementation, but simpler than streaming)

- [ ] **Managed Services Evaluation** (1-2 months pilot)
  - Expected Savings: $500K (3-year TCO vs self-managed streaming)
  - ROI: 7% reduction + faster time to production
  - Effort: Low (pilot managed platform)

- [ ] **Query Performance Optimization** (4-6 weeks)
  - Expected Savings: $470K/year (analyst productivity, equivalent capacity)
  - ROI: 23×
  - Effort: Medium (ClickHouse migration, materialized views)

---

### Long-Term Optimization (6-12 Months)

- [ ] **Hybrid Architecture** (3-6 months)
  - Expected Savings: $2.6M (3-year TCO vs full streaming)
  - ROI: Selective streaming for critical use cases only
  - Effort: High (requires both streaming and batch expertise)

- [ ] **Continuous Cost Monitoring** (ongoing)
  - Expected Savings: 10-15% ongoing efficiency (detect waste, optimize continuously)
  - ROI: Ongoing
  - Effort: Low (automated dashboards, quarterly reviews)

---

## Cost Optimization Summary

| Strategy | Savings (Annual) | Effort | ROI | Timeline |
|----------|-----------------|--------|-----|----------|
| **Tiered Storage** | $150K-220K | Low | 15-22× | 2-3 weeks |
| **Avoid Premature Streaming** | $1.4M-4.4M (3-year) | Medium | 64-75% | 2-4 months |
| **Right-Size Reliability** | $500K-2M | Low | Variable | 2-3 weeks |
| **Query Optimization** | $470K (productivity) | Medium | 23× | 4-6 weeks |
| **Managed Services** | $500K (3-year) | Low | 7% | 1-2 months |
| **Schema Optimization** | $100K-500K | Medium | 10-25× | 3-4 weeks |

**Total Potential Savings**: **$2M-4M/year** (mid-sized security operations)

---

## Book Integration

**Chapter 1 (Cost Comparisons)**:
- Tiered storage economics (55-80% savings)
- SIEM vs modern stack TCO (batch $2.5M vs SIEM $5-10M)
- Streaming premium analysis ($4.4M difference vs batch)

**Chapter 4 (Implementation Journeys)**:
- Journey 1 (Batch-First): Tiered storage + query optimization
- Journey 2 (Streaming-First): Managed services + right-size reliability
- Journey 3 (Hybrid): Selective streaming + cost-conscious architecture

**Chapter 6 (Decision Framework)**:
- Cost optimization checklist for architectural decisions
- Break-even analysis for streaming investment
- Staffing efficiency (managed vs self-managed)

---

**Author**: Jeremy Wiley
**Date**: October 15, 2025
**Evidence Quality**: 92% Level A (11 of 12 sources from cost-reality-reference.md)
**Status**: Ready for book integration
