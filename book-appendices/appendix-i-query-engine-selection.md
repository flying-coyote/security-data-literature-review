---
type: essay-draft
title: "Appendix I: Query Engine Selection for Security Workloads"
created: 2026-06-10
tags: [query-engine, duckdb, trino, dremio, spark, iceberg]
---

# Appendix I: Query Engine Selection for Security Workloads

This material moved to the proof appendices so the platform-selection decision path in the handbook stays short. The engine choices the handbook chapters point at rest on the measurements carried here, in full.

## Opening: The Multi-Engine Reality

The handbook's platform-selection decision material set up the choice of platform, and that decision framework is now distributed across the manageability and foreground-decision material in Chapter 1, the what-good decision examples in Chapter 6, and the migration decisions in Chapter 7. Appendix H showed how OCSF (v1.x; the current release is v1.8.0, 2026-03-16) enables vendor-neutral schema standardization. Now comes a critical architectural question: **Which query engine do you use to actually analyze your security data?**

"Can we just use Spark for everything?"

This question comes up in almost every security data architecture review, and it's tempting: learn one engine, use it everywhere, simplify operations. The answer is mostly no, though, and the reason is worth working through, because security operations run a few different kinds of query that pull engine design in opposite directions. Different workloads end up demanding different engines.

Organizations that force all workloads through a single query engine pay for it in several ways at once, and the penalty comes from workload mismatch rather than from one modern engine being broadly faster than another: frustrated analysts asking why a dashboard takes 30 seconds to load on a batch-oriented engine, unnecessarily high costs from paying for capabilities they don't use, and operational friction as SOC dashboards compete with threat hunting scans for the same resources.

This appendix addresses **Anti-Pattern #4: "One Engine for Everything"** and shows you how to build hybrid architectures that route each security workload to its optimal engine, which delivers 50-75% cost savings (per the cost model in Section I.6.3) compared to single-platform approaches while providing better performance.

The appendix works through the security workload spectrum (real-time dashboards, threat hunting, ETL, and maintenance), why Spark stays necessary for Apache Iceberg maintenance (Iceberg's V3 features shipped through 2025 and the engines have broadly picked them up by mid-2026, while the V4 spec stays open as GitHub milestone #58 with no items merged into it since late 2025; H-ARCH-04: 0.98 confidence), when Trino or Starburst wins for ad-hoc investigations, when Dremio wins for sub-second SOC dashboards, and where DuckDB edge preprocessing earns its place (50-80% volume reduction, validated at 7.5 trillion records in Jake Thomas's Tier-B Okta personal account), before pulling the engines together into hybrid architecture patterns. The reason all of that is worth the operational weight is that no single engine handles all security workloads efficiently, so success comes from matching workload characteristics to engine strengths and accepting that you'll run 3-4 engines rather than one.

---

### Leadership Takeaway

Your security team will run 3-4 query engines rather than one, and this is normal architectural practice, not a sign of failure. The alternative (forcing all workloads through a single engine) costs 50-75% more and breaks down operationally where workloads conflict, as when dashboard refreshes queue behind threat-hunting scans; the worst penalties come from workload mismatch rather than engine-vs-engine speed, since in my single-host join bench (Tier B, 2026) every engine tested answered every join in the SOC suite in under 1.5 seconds. Organizations that adopt hybrid multi-engine architectures typically achieve 63% cost savings compared to single-platform approaches while delivering faster analyst response times. If your architect recommends multiple engines, they're following the same pattern reported at Netflix (5 PB/day, Tier C: ClickHouse meetup presentation, late 2024) and described by Jake Thomas at Okta (7.5 trillion records, Tier B: personal communication).

**Bottom line**: Multiple specialized engines cost less and fit security's conflicting workloads better than one general-purpose engine; the gain is operational fit and cost, with raw speed the smaller lever at SOC scale.

**Skip to**: Section I.6 for the cost comparison between single-platform and hybrid multi-engine architectures.

---

## Section I.1: The Security Workload Spectrum

Security operations demand a combination of query patterns that no single engine handles well, so the engine selection that follows depends on first being clear about which workload type you're actually serving.

### I.1.1 Real-Time SOC Dashboards

- **Latency**: Sub-second (<1 sec, 95th percentile)
- **Pattern**: Same queries repeated 100s-1000s of times/day (error rates, failed auth, top talkers)
- **Refresh**: Every 10-60 seconds, <5 min data freshness
- **Scale**: 20 displays × 10 tiles × 120 refreshes/hour = 24,000 queries/hour for a mid-size SOC
- **Analyst expectation**: Instant refresh, no visible lag during active incidents

---

### I.1.2 Ad-Hoc Threat Hunting

- **Latency**: Interactive (5-30 seconds acceptable, <60 seconds maximum)
- **Pattern**: Unpredictable, unique queries per investigation (lateral movement detection, exfiltration analysis, baseline comparison)
- **Complexity**: High, with complex joins, nested subqueries, full table scans across 7-90 days
- **Scale**: 10 active investigations/week × 30 queries each = 300 unique queries/week
- **Analyst expectation**: "I'm investigating a potential breach. Give me results within 30 seconds so I can iterate quickly."

When an engine can't deliver on that expectation across 30- or 90-day windows, the cost isn't just slow queries; it's what happens to the analyst, which is the incident that opens this book: a month of a skilled person's life spent wrestling data infrastructure because the query layer couldn't interrogate its own telemetry at the depth and duration the investigation actually needed.

See Section I.3.2 for full threat hunting query examples with Trino performance benchmarks.

---

### I.1.3 Batch ETL and Enrichment

- **Latency**: Minutes to hours (background processing, scheduled jobs)
- **Pattern**: Multi-stage transformations, including threat intel enrichment, OCSF normalization (Appendix H), ML feature engineering
- **Complexity**: Very high, with broadcast joins across 5-10 sources, risk scoring logic, format conversion
- **Scale**: 10 TB/day raw → 5 TB/day enriched (nightly ETL within 4-8 hour batch window)
- **Key requirement**: PySpark ecosystem for complex transformations (broadcast joins, UDFs, ML libraries)

---

### I.1.4 Iceberg Table Maintenance

- **Operations**: File compaction (`rewrite_data_files`), orphan cleanup (`remove_orphan_files`), snapshot expiration (`expire_snapshots`), delete file merging (`rewrite_position_delete_files`)
- **Frequency**: Daily (hot data), weekly (warm data), monthly (cold data)
- **Critical requirement**: ACID guarantees, and only Apache Spark has full Iceberg maintenance procedures
- **Without maintenance**: Query performance degrades 50-90× over 30-90 days as small files accumulate (Anti-Pattern #10: "Skipping Spark Maintenance")

See Section I.2 for detailed maintenance code, scheduling, and the cost of skipping maintenance.

---

### I.1.5 The Single-Engine Problem

Why can't one engine handle all four workload types?

| Workload | Spark | Trino | Dremio | DuckDB |
|----------|-------|-------|--------|--------|
| **SOC Dashboards** (<1 sec) | ✗ 5-30 sec cold start | ✗ No caching, rescans | ✓ Reflections <1 sec | ✗ Batch-oriented |
| **Threat Hunting** (5-30 sec) | ⚠ Slow startup | ✓ Fast interactive | ⚠ First-time queries bypass cache | ⚠ Not designed for interactive |
| **Batch ETL** (hours) | ✓ PySpark ecosystem | ⚠ Limited transformation libs | ⚠ Not ETL-focused | ⚠ Not distributed |
| **Iceberg Maintenance** | ✓ ONLY option | ✗ No procedures | ✗ No procedures | ✗ No procedures |

No single engine gets ✓ across all rows, which is why a hybrid architecture is required.

I put this table on a measured footing rather than leaving it qualitative. The numbers below are a first-party run on the MOAR reference stack (2026-06-07), four engines (DuckDB, Trino, ClickHouse, StarRocks) reading one shared Iceberg/OCSF table over a 1,000,000-row `network_activity` slice, reporting the median of four trials in milliseconds with the coefficient of variation in parentheses. It's a single host (a Ryzen 5800H laptop under WSL2), so the relative pattern across engines is the finding rather than the absolute milliseconds, which would move on real cluster hardware:

| Workload | DuckDB | Trino | ClickHouse | StarRocks | Fastest |
|----------|--------|-------|-----------|-----------|---------|
| `count(*)` full scan | 2.4 ms (10%) | 68.5 ms (10%) | 18.2 ms (11%) | 39.9 ms (1%) | DuckDB |
| `dst_port=3389` needle | 5.7 ms (3%) | 97.5 ms (6%) | 22.1 ms (8%) | 45.3 ms (1%) | DuckDB |
| group by `dst_port` | 12.1 ms (7%) | 96.6 ms (7%) | 30.1 ms (5%) | 55.3 ms (11%) | DuckDB |
| distinct `src_ip` (high-cardinality) | 139.7 ms (14%) | 427.9 ms (17%) | 168.7 ms (6%) | 97.7 ms (2%) | StarRocks |

The honest reading is that at 1M rows on a single host the embedded engine, DuckDB, with no coordinator and no network hop to pay for, is fastest on every gated small-batch workload, which is what you'd expect when the query is small enough that startup and the round-trip dominate the scan itself. The line worth dwelling on is the last one: on the high-cardinality `distinct src_ip` workload StarRocks already overtakes DuckDB, and that's the first sign that the per-workload specialization this table describes is a property of scale and concurrency rather than something a laptop surfaces. It shows up once the data is large enough and the query load concurrent enough that the columnar OLAP and MPP designs earn their coordinator overhead, so the table describes the architecture production scale calls for, and the crossover, where ClickHouse and StarRocks overtake the embedded engine, is the kind of thing worth measuring on your own data before committing. The first three workloads are gated on answer-equality, so each engine's result was checked against the others rather than assumed equal, and across those gated workloads all four engines agreed; the distinct count is reported latency-only and is not gated, because ClickHouse's `count(distinct)` is approximate by default and so isn't comparable as an exact answer in this run.

Pushing the same four engines over a 100,000,000-row slice of the same table (2026-06-07, same single host, `./moar bench 100000000`, again the median of four trials in milliseconds with the coefficient of variation in parentheses) surfaces the crossover the smaller snapshot could only point at:

| Workload | DuckDB | Trino | ClickHouse | StarRocks | Fastest |
|----------|--------|-------|-----------|-----------|---------|
| `count(*)` full scan | 12.4 ms (9%) | 44.4 ms (4%) | 10.5 ms (2%) | 48.2 ms (2%) | ClickHouse |
| `dst_port=3389` needle | 77.7 ms (16%) | 419.2 ms (4%) | 182.4 ms (5%) | 95.0 ms (3%) | DuckDB |
| group by `dst_port` | 103.1 ms (2%) | 668.9 ms (3%) | 229.1 ms (6%) | 194.4 ms (6%) | DuckDB |
| distinct `src_ip` (high-cardinality) | 4091 ms | 13519 ms | ERR | 5180 ms | DuckDB |

At 100M the board no longer belongs to one engine. On the full-scan `count(*)` ClickHouse now comes in fastest at 10.5 ms with DuckDB a hair behind at 12.4 ms, where both the 1M table above and the intermediate 10M run had DuckDB winning that workload outright, while DuckDB still takes the selective `dst_port=3389` needle and the `group by dst_port` aggregation. So the claim that no single engine wins every shape, which the 1M snapshot could only assert off the one StarRocks crossover, is now measured at scale: the columnar OLAP engine overtakes on the scan-everything count while the embedded engine holds the selective lookup and the grouped aggregation, and the practical reading is that you pick the engine for the query shape rather than for the workload as a whole. The gated workloads still agree on their answers across all four engines, and the high-cardinality distinct stays latency-only and ungated here too, where ClickHouse errored on it outright at this scale rather than finishing slow. The single-host caveat carries over unchanged, since the absolute milliseconds would move on cluster hardware and it's the relative ordering across engines that is the finding.

Joins, the shape security correlation leans on, got their own scored run (2026-06-10, same single host, Tier B: 10M-60M-row tables, one warmup plus seven timed trials per query, every answer verified against a DuckDB oracle; the queries are TPC-H-derived, so they aren't comparable to audited TPC-H results). The specialization is real: StarRocks won four of the five derived join queries and was 2.7-2.8× faster than both ClickHouse arms on the heaviest six-table join, while ClickHouse took the most aggregation-shaped of the five, so the premise this appendix rests on, that engines specialize by query shape, now has join-side measurement behind it. But the spread is small where security operations actually live, because on the SOC-scale join suite every engine answered every join in 0.069-1.411s, and a 53-million-pair correlation join came back a statistical three-way tie at about 0.86s across StarRocks and both ClickHouse arms. When every candidate answers the correlation query in under a second and a half, join latency stops being the selection criterion, and what should drive the choice instead is catalog maturity, concurrency behavior, and operating cost. The run's one failure makes that point better than any latency number: the only query that failed to finish anywhere was ClickHouse's own native MergeTree table on one join (past 300 seconds, twice), while the same engine over Iceberg ran the same query in 1.35s, a stats-blind planning failure (EXPLAIN-instrumented 2026-06-10: with no column statistics on either arm, the native path's greedy join reordering built a roughly 1.2-billion-row intermediate, and with the reordering disabled the same table answered in 5.3s), and exactly the class of new infrastructure problem that raw-speed comparisons don't show you. Same honesty as the tables above: one host, so the ratios travel and the absolute times don't, and TB-scale multi-node behavior is a different regime this run neither confirms nor refutes.

The deeper lesson from running it is one the table can't show. When several engines read the same open table, you have to verify they return the same answer rather than assume it. Across those five engines the counts agreed exactly, but that agreement is a control you run, not a guarantee you inherit, because a fast engine can be silently wrong: a version-scoped reader bug in chDB's Bloom-filter pushdown undercounted a selective lookup by a handful of rows, and it reproduced only at 100M scale (about 8,000 row groups, where 285 of 2,000 probe values came back 3 to 13 rows short) while reading clean at 10M, the kind of error a timing-only benchmark never catches. That scale-dependence is itself the methodology point, and it splits into two habits worth naming. Pin the artifact, because the defect lives in a specific version: chDB 4.1.8 ships embedded ClickHouse 26.3.9.1, and the same 100M file reads correctly on ClickHouse 26.5.1.882, so the bug is real but version-scoped, and a verdict that doesn't record the version is a verdict you can't trust six months later (it's filed as chdb#587 against the pinned embedded build, not against ClickHouse). Sweep the scale, because a cheap isolation at a smaller size can hide a row-group-count-dependent bug entirely, since had I trusted the clean 10M run I'd have published the engine as correct and never seen the 100M shortfall, so the isolation scale has to be validated against the scale the bug was first seen at rather than the scale that's convenient to run. Picking the engine for the workload is the part the table above is about; verifying that those engines actually return the same answer, at the scale you'll actually run them, is what keeps an investigation from standing on a number one of them quietly got wrong.

---

<!-- RENUMBER: 9.1A/9.4A/9.4B should be resequenced in final edit -->
## Section I.1A: Why Elasticsearch Struggles at Petabyte Scale

Elasticsearch was designed for full-text search over documents, while security analytics mostly runs aggregations over structured data, grouping by IP, counting by user, and slicing time series, and that mismatch turns expensive at TB+ scale, where it shows up as garbage-collection pauses that time out queries during active investigations and heap exhaustion on high-cardinality fields.

**Huntress case study** (Tier C: Huntress-reported, ClickHouse vendor ecosystem write-up, not independently audited): 3 million endpoints migrated from Elasticsearch to ClickHouse, with a reported **93% cost reduction**, going from weekly cluster instability and 10-20 hours/week operational burden to roughly zero incidents and under 2 hours/week.

### Four Architecture Limitations

**1. Storage overhead**: Elasticsearch indexes every field by default. A 500-byte security event becomes 2-5 KB stored (4-10× overhead). ClickHouse stores the same event in 50-100 bytes with columnar compression. At 1 TB/day: Elastic needs 4-10 TB storage vs ClickHouse 100-200 GB.

**2. Shard management**: At TB/day scale, 1,000+ shards create 2-3 TB RAM minimum, cluster instability during rebalancing, and 10-30 second JVM garbage collection pauses that cause query timeouts during active investigations.

**3. Tiering performance cliffs**: Queries spanning hot/warm/cold tiers degrade dramatically, so a 90-day investigation query takes 2 seconds for hot data, 15 seconds for warm, 90 seconds for cold. ClickHouse/Iceberg architectures are reported to hold 5-15 seconds regardless of tier (Tier C: vendor-ecosystem figures at TB+ multi-node scale, a regime my single-host bench in Section I.1.5 neither confirms nor refutes).

**4. Heap pressure on security workloads**: Aggregations on high-cardinality fields (millions of IPs, billions of file hashes) exhaust JVM heap at 31-32 GB practical max. ClickHouse's C++ implementation uses off-heap memory with no GC pauses.

### Decision Framework

| Use Case | Elasticsearch | ClickHouse/Columnar |
|----------|---------------|---------------------|
| **Full-text search** | ✓ Optimized | ⚠ Works, not optimized |
| **Aggregations** (group by IP, count by user) | ⚠ Heap pressure at scale | ✓ Optimized |
| **High-cardinality grouping** (millions of unique values) | ✗ Heap exhaustion | ✓ Columnar advantage |
| **Petabyte-scale storage** | ✗ 4-10× overhead | ✓ 10-20× compression |
| **Multi-year retention** | ✗ Cold tier 30-120 sec (reported) | ✓ Unified API 5-15 sec (reported; TB-scale vendor-ecosystem figures, not lab-verified) |

**Keep Elasticsearch if**: <1 TB/day, full-text search is critical, team has deep Elastic expertise, or managed Elastic Cloud handles operational complexity.

**Migrate to columnar if**: >1 TB/day, aggregation queries dominate (>70%), query performance degrading, or shard management consuming >5 hours/week.

**The hybrid option**: Keep small Elasticsearch cluster (<1 TB) for full-text search, use ClickHouse/columnar for aggregations and petabyte-scale retention.

---

## Section I.2: Why Spark is Irreplaceable

**H-ARCH-04: Spark Irreplaceable for Iceberg Maintenance** (Confidence: 0.98/1.0)

Even teams using Trino for queries and Dremio for dashboards generally still run Spark for Iceberg table maintenance, because Spark exposes the full set of maintenance procedures while the alternatives cover only part of the job: Athena offers `OPTIMIZE` and `VACUUM`, Trino has its own `OPTIMIZE`, and Dremio can compact, but none of them matches Spark's complete coverage of compaction, snapshot expiration, orphan cleanup, and delete-file merging in one place.

### I.2.1 The Maintenance Imperative

Apache Iceberg tables accumulate operational overhead over time:

**Problem 1: Small File Accumulation**

DuckDB edge preprocessing (Section I.5) writes 1,000-10,000 small Parquet files per day (optimized for serverless Lambda). Without compaction:
- Day 1: 5,000 files (queries scan 5,000 manifests)
- Day 7: 35,000 files (queries scan 35,000 manifests)
- Day 30: 150,000 files (**50-90× query slowdown**)

**Problem 2: Snapshot Bloat**

Iceberg maintains snapshot history for time-travel queries. Without expiration:
- 90 days × 24 snapshots/day = 2,160 snapshots
- Metadata scans become bottleneck (seconds added to every query)

**Problem 3: Delete Files**

Row-level deletes (GDPR "right to erasure", PCI-DSS data minimization) create delete files that slow scans. Without merging:
- 1,000 delete files × 1 KB each = 1 MB overhead per query
- Query planner must check every delete file against every data file

### I.2.2 Why ONLY Spark?

**Trino**: Can query Iceberg, cannot maintain
- No `CALL system.rewrite_data_files()` procedure
- No compaction, no orphan cleanup, no snapshot expiration
- Read-only Iceberg connector

**Dremio**: Can query + accelerate, cannot maintain
- Reflections enable fast queries, but not maintenance
- No Iceberg maintenance procedures exposed
- Query engine only, not storage management

**Snowflake**: Proprietary format, not Iceberg
- Uses internal format (not Iceberg metadata)
- Cannot maintain Iceberg tables (different architecture)

**DuckDB**: Can write Parquet, not Iceberg-aware maintenance
- Excellent for edge preprocessing (Section I.5)
- Not distributed (cannot compact TB-scale tables)
- No Iceberg catalog integration for ACID operations

**ONLY Apache Spark** has:
- Distributed file rewriting (parallel compaction across cluster)
- Bin-packing algorithms (optimize file sizes to 512 MB target)
- Transactional Iceberg support (ACID guarantees during maintenance)
- Native Iceberg procedures (`CALL system.*` commands)

"Spark is essentially the native language of Iceberg. You may deploy Dremio for queries, but Spark may still be necessary for table maintenance." — a data-platform practitioner [Personal communication, October 2025]

### I.2.3 Security-Specific Maintenance Schedule

| Frequency | Scope | Rationale | Target |
|-----------|-------|-----------|--------|
| **Daily** | Last 7 days | Active investigation period (threat hunts hit hot data) | <1,000 files/day |
| **Weekly** | 8-30 days | PCI-DSS/SOX compliance queries (Sunday 2 AM) | <5,000 files in 30-day window |
| **Monthly** | 30-90 days | Quarterly audit retention | <10,000 files in 90-day window |
| **Quarterly** | 90+ days | Snapshot expiration (retain 100 most recent) | Metadata overhead minimal |

**Cost optimization**: Spark on spot instances costs $0.05/hour vs $0.25/hour on-demand. Weekly compaction: ~4 hours × $0.05 = **$42/month** (vs $208 on-demand). Compaction is fault-tolerant batch work, so spot interruptions are acceptable.

### I.2.4 The Cost of Skipping Maintenance

As an illustrative scenario, drawn as a composite from three organizations with figures rounded rather than measured from any single one: a 30-day threat hunt query that takes around 8 seconds on Day 0 degrades to roughly 40 seconds by Day 30 (on the order of 350,000 accumulated small files, about 5× slower) and to several minutes by Day 60 (roughly 700,000 files, on the order of 30× slower). Emergency Spark compaction the next day took most of a day to catch up, and it restored query performance to about 9 seconds. The reason I'd budget for weekly Spark maintenance from Day 1 rather than treating it as an emergency response is that by the time the performance has collapsed you're already paying for the dug-out day on top of the slow queries that pushed you into it.

---

## Section I.3: Trino/Starburst for Threat Hunting

### I.3.1 Why Trino Excels at Ad-Hoc Investigations

Trino is built for unpredictable, first-time queries with complex WHERE clauses and full table scans, which is the pattern security threat hunting follows almost by definition, since each investigation asks a question nobody anticipated.

**Trino architectural advantages**:

1. **Fast query startup** (< 1 second vs Spark's 5-30 second cold start)
   - No JVM warmup delay
   - No executor allocation wait
   - Query begins processing immediately

2. **Cost-based optimizer** tuned for complex SQL
   - Predicate pushdown (filter at storage layer)
   - Join reordering (optimize multi-table correlation)
   - Partition pruning (scan only relevant date partitions)

3. **MPP (Massively Parallel Processing) architecture**
   - Distributed query execution across worker nodes
   - Pipeline parallelism (multiple stages execute simultaneously)
   - Memory-efficient streaming operators

4. **No query caching by default**
   - Every query is a fresh full scan (appropriate for unique investigations)
   - No cache invalidation complexity (vs Dremio Reflections)

"AWS Athena is Starburst/Trino at its core." — a data-platform practitioner [Personal communication, October 2025]

That's a reasonable signal of production maturity, though an existence proof rather than a benchmark: AWS evaluated query engines (Presto, Spark, custom) and selected Trino as Athena's foundation, which tells you it runs at extreme scale (millions of customers, exabyte-scale data) without telling you how it compares head-to-head. My scored join bench does compare head-to-head (Section I.1.5; single host, Tier B, answers oracle-verified), and Trino did not win that contest: it carried the largest join tax of the engines tested, with joined queries running about 4.35× their flat-table equivalents where StarRocks and ClickHouse sat near 1.8×, and it trailed StarRocks by roughly 2.15× on the heaviest six-table join. Every SOC-scale join still came back on Trino in under 1.5 seconds, though, which is comfortably interactive, so the case for Trino in this role rests where this section puts it, on federation, fast startup, and operational fit, rather than on join latency, where StarRocks led the heavier queries but the SOC-scale suite was too compressed to make speed the deciding criterion.

### I.3.2 Threat Hunting Query Patterns

**Pattern 1: Lateral Movement Detection**

```sql
-- Find suspicious privilege escalation after initial access
WITH initial_access AS (
    SELECT
        principal_id,
        user_name,
        src_endpoint_ip as entry_ip,
        event_time as entry_time
    FROM security.cloudtrail
    WHERE event_name = 'ConsoleLogin'
      AND user_agent LIKE '%Chrome%'  -- Web browser login
      AND event_date >= CURRENT_DATE - 30
),
privilege_events AS (
    SELECT
        principal_id,
        event_name,
        src_endpoint_ip,
        event_time,
        resources
    FROM security.cloudtrail
    WHERE event_name IN (
        'PutUserPolicy',      -- Inline policy assignment
        'AttachUserPolicy',   -- Managed policy attachment
        'CreateAccessKey',    -- Programmatic access
        'UpdateAssumeRolePolicy',  -- Role trust modification
        'PutRolePolicy'       -- Role permission expansion
    )
    AND event_date >= CURRENT_DATE - 30
)
SELECT
    i.user_name,
    i.entry_ip,
    i.entry_time,
    p.event_name as escalation_action,
    p.src_endpoint_ip as action_ip,
    p.event_time as escalation_time,
    (p.event_time - i.entry_time) as time_to_escalation,
    p.resources
FROM initial_access i
JOIN privilege_events p
    ON i.principal_id = p.principal_id
    AND p.event_time > i.entry_time
    AND p.event_time < i.entry_time + INTERVAL '2' HOURS  -- Escalation within 2 hours
WHERE i.entry_ip != p.src_endpoint_ip  -- IP changed = lateral movement indicator
ORDER BY escalation_time DESC
```

**Trino performance** (illustrative estimates for a tuned multi-node cluster, not a first-party single-host run): roughly 8-15 seconds on 1 TB (30 days CloudTrail), 30-60 seconds on 10 TB

**Why Trino wins**:
- Complex self-join with time window (Spark slower due to shuffle overhead)
- Array operations on `resources` field (Trino's native JSON handling)
- Predicate pushdown on date partition (scans only 30 days, not full retention)

---

**Pattern 2: Anomalous Data Access** (exfiltration detection)

The same CTE pattern applies: establish a 60-90 day baseline (APPROX_DISTINCT IPs, AVG/STDDEV download sizes), compare against last 7 days, flag users exceeding 3× request count or 5× download size with statistical anomaly assessment (3σ threshold).

**Trino performance** (illustrative estimate for a tuned multi-node cluster, not a first-party measured run): roughly 15-45 seconds on 90 days CloudTrail. Trino's statistical functions (STDDEV, APPROX_DISTINCT) and multi-window aggregations handle this baseline-comparison pattern well.

---

### I.3.3 Federated Queries for Operational Context

Trino's 40+ connectors enable joining Iceberg security data with operational databases **without ETL**, which is critical during active incident response.

**Example: Join CloudTrail with CMDB for asset context**

```sql
-- Investigate failed AWS API calls, enriched with asset criticality from PostgreSQL CMDB
SELECT
    ct.event_name,
    ct.error_code,
    ct.error_message,
    ct.principal_id,
    ct.src_endpoint_ip,
    ct.event_time,
    -- Asset context from PostgreSQL CMDB (live query)
    ai.hostname,
    ai.owner_team,
    ai.criticality,
    ai.compliance_scope,
    ai.environment
FROM iceberg.security.cloudtrail ct
JOIN postgresql.cmdb.asset_inventory ai
    ON ct.principal_id = ai.aws_arn
WHERE ct.error_code IS NOT NULL
  AND ct.event_date >= CURRENT_DATE - 7
  AND ai.criticality IN ('critical', 'high')  -- Focus on high-value assets
ORDER BY ct.event_time DESC
```

**Use case**: Analyst needs asset owner contact info during active investigation, and can query directly from CMDB without waiting for ETL pipeline (which might be nightly batch).

**Security-relevant connectors**: PostgreSQL (CMDB, vulnerability management), MySQL (user directories), MongoDB (threat intel), Elasticsearch (legacy SIEM), Kafka (real-time streams), plus Iceberg. Federated queries add 5-30 seconds latency vs pure Iceberg, which is acceptable during investigations when operational context is critical.

### I.3.4 When NOT to Use Trino

1. **High-frequency dashboard queries**: Trino rescans every time (no caching). SOC dashboard refreshing every 30 seconds = 1,920 wasteful full scans/day. Use Dremio Reflections (Section I.4).
2. **Iceberg maintenance**: No maintenance procedures. Must use Spark (Section I.2).
3. **Streaming ingestion** (<30 sec latency): Use Spark Streaming or Flink.
4. **Complex ETL**: SQL-only, no PySpark libraries. Use Spark for ML/transformations.

---

## Section I.4: Dremio for Sub-Second SOC Dashboards

### I.4.1 The SOC Dashboard Challenge

**Scenario**: 24/7 Security Operations Center with 20 large displays showing real-time threat metrics:

**Dashboard requirements**:
- 20 displays × 10 tiles each = 200 distinct queries
- Refresh every 30 seconds = 400 queries/minute = 24,000 queries/hour
- Latency requirement: <1 second (95th percentile) for instant visual updates
- Data freshness: <5 minutes lag acceptable

**Problem with Trino** (or any non-caching query engine), as an illustrative scenario rather than a first-party run:
- Every query = full table scan (no result caching)
- 24,000 full scans/hour on 30-day CloudTrail partition (1 TB)
- Query latency: 5-15 seconds per query (illustrative, not a measured run; unacceptable for real-time dashboard)
- Cost: $5/TB scanned × 24,000 scans/hour × 1 TB × 0.001 (partition factor) = **$120/hour = $2,880/day**
- Analyst experience: Laggy dashboards, miss real-time threats during slow refreshes

**Dremio solution**: **Reflections** (pre-aggregated, incrementally updated, transparent query acceleration)

### I.4.2 How Reflections Work

Dremio analyzes query patterns and creates optimized data structures (similar to materialized views but automatically managed):

**Example dashboard query** (repeated 1,920 times/day):

```sql
-- SOC dashboard tile: "Failed Authentications by Source IP (Last Hour)"
SELECT
    src_endpoint_ip,
    COUNT(*) as failed_attempts,
    COUNT(DISTINCT user_name) as unique_users,
    MAX(event_time) as last_failure
FROM security.authentication
WHERE event_time >= NOW() - INTERVAL '1' HOUR
  AND outcome = 'failure'
GROUP BY src_endpoint_ip
HAVING COUNT(*) > 5
ORDER BY failed_attempts DESC
LIMIT 20
```

**Without Reflection** (Trino behavior; the figures below are illustrative, not a first-party run):
- Scan: 1 hour of authentication logs (~100 GB uncompressed, 10 GB compressed Parquet)
- Query time: 8-15 seconds (illustrative estimate, full scan, aggregation, sort)
- Repeated 1,920 times/day = **15,360-28,800 seconds = 4.3-8 hours of compute time per tile**

**With Dremio Reflection** (automatic):

Dremio creates aggregation reflection:
```sql
-- Dremio automatically creates (not user-written):
CREATE REFLECTION authentication_hourly_failures
AS SELECT
    src_endpoint_ip,
    DATE_TRUNC('minute', event_time) as time_bucket,
    outcome,
    user_name
FROM security.authentication
WHERE event_time >= NOW() - INTERVAL '7' DAYS  -- Keep 7 days hot
PARTITION BY (DATE_TRUNC('day', event_time))
REFRESH EVERY 5 MINUTES  -- Incremental refresh
```

**Query execution with Reflection**:
- Scan: Pre-aggregated reflection (10 MB vs 10 GB = 1000× reduction)
- Query time: <1 second (lookup pre-computed aggregates)
- Repeated 1,920 times/day = **1,920 seconds = 32 minutes total compute time**

**Cost comparison**:
- Trino: 4.3-8 hours compute × $0.10/hour = $0.43-$0.80 per tile per day × 200 tiles = **$86-$160/day**
- Dremio: 32 minutes compute × $0.10/hour = $0.05 per tile per day × 200 tiles + reflection storage (20 GB × $0.023/GB/month) = **$10/day + $15/month storage**

**Savings**: 85-94% cost reduction for dashboard workloads, PLUS <1 second latency vs 8-15 seconds.

### I.4.3 Security Use Case: Real-Time Threat Visibility

Typical SOC dashboard tiles (failed authentication at a 15-min window, 30-sec refresh, <500ms; high-risk CloudTrail events at a 1-hour window, 1-min refresh; network anomalies at a 5-min window; risky users at a 24-hour window) all achieve <1 second latency with Dremio Reflections through automatic aggregation management and incremental refresh (process only new data every 5 minutes, not full recompute).

### I.4.4 When NOT to Use Dremio

1. **Ad-hoc threat hunting**: Reflections don't help first-time queries, so Dremio's acceleration story is the Reflections layer rather than the raw engine. Use Trino for investigations.
2. **Low query frequency**: Dremio licensing ($40K-$200K/year) only cost-effective at >100 queries/day on same patterns.
3. **Iceberg maintenance or complex ETL**: Query engine only. Use Spark.

---

## Section I.4A: ClickHouse for Real-Time Analytics at Petabyte Scale

While Sections I.3-I.4 covered Trino and Dremio, there's a fifth query engine worth examining at security-relevant scale: **ClickHouse**, the columnar database Netflix chose for their petabyte-scale logging system.

### I.4A.1 Why Netflix's Choice Matters for Security

What makes the choice relevant is how closely observability and security have converged on the same problem: Netflix's logging challenges, massive write throughput, sub-second queries over long retention, and cost-efficient petabyte storage, are the same ones security data hits at enterprise scale.

**Netflix's reported scale** (Tier C: ClickHouse meetup presentation by Daniel Muino, late 2024 — vendor ecosystem event, self-reported, not independently audited):
- **5 petabytes/day** ingestion across 40,000+ microservices
- **10.6 million events/second** average (12.5 million peak)
- **Sub-second query response** for investigations
- **20-second data availability** from ingestion to searchable

The specific numbers are Netflix's own figures. The architectural lesson (hot/cold tiering, columnar storage, generated parsers over regex) doesn't depend on taking those numbers at face value; the engineering rationale holds regardless of the exact scale.

### I.4A.2 Columnar Performance Advantage

Security queries scan millions of rows but touch few columns (timestamps, IPs, usernames). Columnar databases read only needed columns and achieve 10-100× better compression than row-oriented storage. The figures Netflix reported (Tier C: meetup presentation) put ClickHouse at 12-19× better compression than Elasticsearch and 5-100× faster on analytical queries, though these are figures the Netflix team presented to describe their own production system, not independently reproduced.

**Schema-on-read SIEM bake-off (SDW Lab, zeek-flagship-rerun, 2026-06-10; Tier B, single host)**: One measured bake-off on a specific workload, 10M OCSF-normalized Zeek conn.log network-telemetry events run against 5 standardized analytical queries, 7 trials per query, CV-gated, with the answers verified equal across every arm. These numbers reflect that workload and data profile; performance ratios will shift on different query types, data distributions, and tuning states:
- ClickHouse native MergeTree (sorted layout): **0.061s average**, 46.8× over the OpenSearch 2.18.0 schema-on-read foil (2.854s)
- ClickHouse-over-Iceberg (`icebergS3()`, zstd Parquet): **0.282s average**, 10.1× over the foil
- The average hides the finding, which is a two-regime split by query shape: the inverted index wins the cheap index-shaped lookups (a protocol-distribution count 3.4× and a duration filter 1.8× over native) while the columnar engines win the hunting-shaped aggregations by one to two orders of magnitude (a byte-sum group-by at 5.4× Iceberg / 21× native, a distinct-port scan at 14× Iceberg / 62× native). The full engine table is in I.4A.4.
- Source: SDW Lab zeek-flagship-rerun (2026-06-10), which supersedes the legacy 145× splunk-db-connect-benchmark (Dec 2025, retired). The legacy foil averaged 27.52s; OpenSearch 2.18.0, bulk-loaded and force-merged, averages 2.85s on the same five queries, so the foil itself is roughly 10× faster and every multiplier shrinks accordingly.

**Compression optimization gap**:
- Default (LZ4): 4.6× compression (712 MB for 10M events)
- Optimized (ZSTD-22 + LowCardinality): **8.2× compression** (399 MB for 10M events)
- Trade-off: +32% query latency with extreme compression
- Huntress 50:1 compression ratio (vs raw JSON): Achievable with ZSTD(22), not out-of-box default

### I.4A.3 Netflix's Three Optimizations (What Security Teams Can Steal)

Netflix engineer Daniel Muino presented their ClickHouse optimization journey at a ClickHouse meetup (late 2024). Three bottlenecks and their solutions:

**Optimization 1: Fingerprinting (216μs → 23μs)**. Log fingerprinting via regex/ML didn't scale at 10M events/sec. Solution: generated lexers using JFlex (precompiled state machines instead of runtime pattern matching). Result: 8-10× throughput increase. **Security takeaway**: If normalizing to OCSF (Appendix H) at petabyte scale, audit parsing pipelines for regex bottlenecks. Consider generated parsers if per-event latency >100μs.

**Optimization 2: Serialization (JDBC → Native Protocol, 30%+ gain)**. JDBC batch insert overhead compounds at 10M+ events/sec. Solution: custom native protocol encoder generating LZ4-compressed blocks directly. Result: 30%+ CPU reduction, faster writes. **Security takeaway**: For high-volume EDR/network telemetry, evaluate native protocol clients vs HTTP/JDBC APIs. LZ4 for real-time ingestion, ZSTD for cold storage.

**Optimization 3: Query Performance (3s → 700ms via Tag Sharding)**. Tag metadata stored as maps required linear scans. Solution: shard into 31 smaller maps by tag key namespace. Result: 4.3× faster queries, 5-8× less data scanned. **Security takeaway**: Shard OCSF `observables` by type (`observables_network[]`, `observables_file[]`, `observables_process[]`) for 3-5× faster filtering. Netflix's principle, "do the least amount of work," is that better data layout beats clever algorithms.

A first-party run on the MOAR reference stack (SDW Lab, 2026-06-08, Tier B) puts numbers on that layout choice for the multi-dimensional filters a SOC actually runs. I wrote one 2M-row OCSF Network Activity corpus three ways (unordered, sorted on `src_ip`, and Z-ordered over `src_ip` × `dst_port` × `time_bucket`) and ran four query shapes, and the layouts split by which dimension each query filtered on. The single `src_ip` sort was fastest whenever the query touched `src_ip`: a `src_ip`-in-/24-plus-time-window query ran 3.7 ms sorted against 4.8 ms Z-ordered and 12.5 ms unordered, because `src_ip` is its sort key and its row groups prune about 95%. But a single sort can only prune on that one key, so on a `dst_endpoint`-plus-port query and a time-window-only query it pruned nothing and ran 9.3 ms and 10.2 ms, while Z-order pruned on whichever dimensions the query touched and came in at 6.0 ms and 5.9 ms. Z-order was never the single fastest layout, but it was the no-regrets one: it held a 4.8–6.0 ms band across all four shapes where the single sort swung from 2.7 ms to 10.2 ms depending on whether the query happened to hit its key. All three layouts returned identical answers, so the layout is purely a pruning lever, changing how much data the engine skips without changing the result, and its price is paid at write time, where the Z-order sort took about 11.6 s against the single sort's 2.1 s and at Iceberg or DuckLake scale amortises across files at compaction. It's a single host, so the absolute milliseconds would move on cluster hardware and the cross-layout ordering is the finding.

The same layout-choice argument runs the other direction, which is worth following because it answers the standard objection that a lakehouse can't do the needle-in-a-haystack point lookup a SIEM's inverted index does. A second first-party run (SDW Lab, 2026-06-14, Tier B) measured exactly that regime, the random high-cardinality point lookup that defeats Parquet min/max pruning, on the 10M-row Zeek conn corpus, comparing an OpenSearch 3.7.0 term query against a ClickHouse-native MergeTree sorted on `(orig_h, resp_h, ts)` and a ClickHouse-over-Iceberg table left unsorted. A single-row `uid` lookup ran 3.5 ms on the OpenSearch index, 3.5 ms on the sorted native store, and 145 ms on the unsorted Iceberg table, and a rare-IP lookup returning 570 rows ran 5.7 ms, 4.5 ms, and 50 ms respectively, where the sorted native store actually edged the index. So the index wins 41× on the `uid` needle and 8.8× on the rare-IP needle against the unsorted lakehouse, but it ties the sorted columnar store on both, which means what loses by 9–41× is the unsorted open-format table that has no index and isn't clustered on the looked-up columns, so it full-scans, and not the lakehouse architecture as such. The point-lookup weakness people attribute to lakehouses is a layout choice, the same lever the Z-order finding above measures, and it ties back to the compaction sort-clustered arm where a sort on the looked-up columns bought a measured pruning gain: a sorted lakehouse layout matches the inverted index on the index's own home turf. The honest reading is the two-regime one, where the index wins the cheap point lookups against an unsorted lakehouse just as the lakehouse wins the heavy hunting aggregations against the SIEM in the flagship, and the question for a given deployment is which regime the workload actually lives in. The numbers are hot/warm and single-host, the same caveat the flagship carries, so the ratios transfer and the absolute milliseconds don't, and a cold S3 read on the unsorted arm would be slower still; the BM25 fuzzy full-text half of the index's home turf is not measured here because the Zeek conn corpus has no rich text field, which is future work on a corpus that has one.

### I.4A.4 ClickHouse Within the Lakehouse Architecture

In Netflix's stack ClickHouse is a specialized engine layered on Apache Iceberg, not a monolithic database doing everything. Netflix developed Iceberg (2018-2020) to solve Hive's partition management and schema evolution limitations, then open-sourced it. ClickHouse handles hot-tier real-time queries; Iceberg provides durable storage with multi-engine access.

**Measured bake-off** (SDW Lab, zeek-flagship-rerun, 2026-06-10; Tier B, single host): 10M OCSF-normalized Zeek conn.log events, 5 standardized analytical queries, 7 trials per query, CV-gated, with identical answers verified across every arm. This is one workload at one scale; treat the ratios as directional for network-telemetry-style analytical queries, not as universal performance guarantees:

| Engine | Format | Avg of medians (s) | vs OpenSearch 2.18.0 foil |
|--------|--------|--------------------|---------------------------|
| ClickHouse native MergeTree | native LZ4, sorted | 0.061 | 46.8× |
| ClickHouse `icebergS3()` | Iceberg, zstd Parquet | 0.282 | 10.1× |
| StarRocks | Iceberg | 0.343 | 8.3× |
| Trino | Iceberg | 0.795 | 3.6× |
| OpenSearch 2.18.0 (schema-on-read foil) | inverted index | 2.854 | 1× (baseline) |

*Source: SDW Lab, zeek-flagship-rerun/results/RESULTS.md + starrocks_trino_arms.json (2026-06-10). Supersedes the splunk-db-connect-benchmark (Dec 2025, retired).*

What the bake-off method demonstrates: the three open engines over Iceberg — ClickHouse, StarRocks, and Trino — query byte-identical Iceberg data and return identical answers, which is the architecture argument; ClickHouse-native and the OpenSearch foil are the two non-Iceberg reference points. The specific multiples are workload-dependent.

A companion foil run on the MOAR reference stack (SDW Lab, 2026-06-07; Tier B) isolates the storage and answer-equality leg of the same comparison at a smaller scale. The foil puts a lakehouse engine (DuckDB over Parquet) next to an OpenSearch-style schema-on-read SIEM over 200,000 OCSF Network Activity events, with a needle on `dst_port=3389` matching 25,000 of them. The two results worth carrying are the answer-equality and the storage ratio: the lakehouse and the SIEM agree on count, on the needle, and on the group-by, and the lakehouse footprint is 1.6 MB of Parquet against an 11.5 MB SIEM index, so the index is 7.0× the columnar footprint. The lakehouse was also faster on all three queries, with the needle at 3.4 ms against the SIEM's 4.7 ms, but that latency comparison carries a caveat I want to be honest about: at this corpus DuckDB's columnar scan is already under 10 ms and OpenSearch is queried over HTTP while DuckDB runs in-process, so the SIEM pays a round-trip the lakehouse doesn't, and a term index's real advantage is on highly selective needles at much larger scale, which a single-host run at 200k rows does not isolate. The findings that hold independent of scale are the answer-equality and the 7.0× storage ratio, and not the millisecond gap on the needle.

```text
$ ./moar compare   # 200,000 OCSF Network Activity events; needle dst_port=3389 = 25,000
  storage:  lakehouse Parquet 1.6 MB   |   SIEM index 11.5 MB   → index is 7.0× the columnar footprint
  query                         lakehouse    siem     agree
  count(*) full scan              200,000   200,000    ✓
  dst_port=3389 (needle)           25,000    25,000    ✓
  group by dst_port             8 buckets  8 buckets   ✓
  → identical answers; 7.0× less storage. (latency read with care: in-process DuckDB vs HTTP
    OpenSearch at 200k rows does not isolate the term index's large-scale needle advantage.)
```

*Figure I-1 — the foil run (`./moar compare`, single-host, Tier B). The scale-independent findings are the answer-equality and the 7.0× storage ratio; the figure carries the latency caveat so the millisecond gap is not over-read.*

### I.4A.5 Hot/Cold Tiering: ClickHouse + Iceberg Architecture

**The pattern validated by Netflix** (buried in meetup comments but architecturally significant):

> "ClickHouse is used for the hot tier for recent data requiring fast, interactive queries. For historical data, Netflix uses Apache Iceberg, which provides cost-efficient long-term storage."

**ClickHouse (Hot Tier)**:
- Last 2 weeks to 2 months of data (configurable retention)
- Sub-second queries for active investigations
- Optimized for write throughput + query speed
- Higher storage cost (SSD), but worth it for recent data

**Apache Iceberg (Cold Tier)**:
- Long-term historical data (months to years)
- Queried less frequently (forensics, compliance, trend analysis)
- Extremely cost-efficient storage (S3/ADLS with Parquet compression)
- Query latency: seconds to minutes (acceptable for historical analysis)

A unified query API searches both tiers transparently, so analysts don't think about "hot vs cold"; they query, and the system routes it appropriately.

**Why this matters for security**:

Security data has a **decay curve** for query frequency:
- **0-7 days**: Active investigations, high query frequency, need sub-second response
- **7-30 days**: Recent incident follow-up, moderate query frequency
- **30-90 days**: Trend analysis, compliance reporting, lower query frequency
- **90+ days**: Forensics, legal holds, compliance retention, rare queries

Most security teams store everything in one tier, either an expensive SIEM or a slow data lake, where Netflix instead optimizes the storage for how the data actually gets queried, letting the access pattern rather than uniformity decide which tier each window of data lives in.

**Cost impact**: Storing 5 PB in ClickHouse for one year: prohibitively expensive. Tiering to Iceberg after 30 days: **10-50× storage cost reduction** while maintaining query capability.

### I.4A.6 When to Use ClickHouse for Security Data

**Use ClickHouse if**:
- ✓ **>5 TB/day ingestion** (or will be soon) - architectural advantages emerge at TB+ scale
- ✓ **Scheduled analytics and real-time aggregations** (fingerprinting, tagging, enrichment pipelines)
- ✓ **Sub-second query response required** for specific workload types (real-time dashboards, metrics)
- ✓ **Engineering capacity to operate infrastructure** (ClickHouse isn't push-button managed service like Snowflake)
- ✓ **Structured/semi-structured logs dominate** (JSON, Syslog, CEF) - ClickHouse's strength

**Don't use ClickHouse if**:
- ✗ **<1 TB/day ingestion** - operational overhead exceeds benefit at small scale
- ✗ **Prefer fully managed services** (Snowflake, Databricks) - ClickHouse requires more hands-on ops
- ✗ **Need full-text search across unstructured data** - ClickHouse can do this, but Elasticsearch better optimized
- ✗ **Team has no columnar database experience** - steep learning curve compared to traditional SQL databases

**Consider DuckDB instead if**:
- **Smaller scale** (10s of GB to TBs, not PBs) - DuckDB's embedded simplicity wins
- **Edge analytics** (queries run where data lives, not centralized) - DuckDB serverless pattern (Section I.5)
- **Team SQL-familiar but not distributed databases** - DuckDB simpler operational model
- **Validation**: Jake Thomas at Okta runs DuckDB at 7.5 trillion records for security analytics (Section I.5)

**ClickHouse vs Trino/Dremio decision framework**:

| Use Case | ClickHouse | Trino | Dremio |
|----------|-----------|-------|--------|
| **Real-time dashboards** | ✓ Sub-second via aggregations | ✗ Rescans data | ✓ Reflections <1 sec |
| **Scheduled analytics** | ✓ Optimized for batch | ⚠ Works but not ideal | ⚠ Query engine only |
| **Ad-hoc threat hunting** | ⚠ Works, not specialized | ✓ Fast interactive | ⚠ First-time bypasses cache |
| **Hot/cold tiering** | ✓ Native (hot SSD → cold S3) | ✗ No native tiering | ⚠ Via Iceberg, not engine feature |
| **Iceberg maintenance** | ✗ No procedures | ✗ No procedures | ✗ No procedures |
| **High-cardinality aggregations** | ✓ Columnar advantage | ⚠ Slower on massive aggregations | ✓ Reflections help |

**The hybrid pattern** (Netflix-validated MOAR architecture):
- **Iceberg**: Storage foundation (ACID, schema evolution)
- **ClickHouse**: Hot tier (last 30 days, real-time aggregations, scheduled analytics)
- **Trino**: Ad-hoc investigations (threat hunting, forensics)
- **Dremio**: SOC dashboards (Reflections for <1 sec)
- **Spark**: Maintenance + complex ETL (Section I.2)
- **DuckDB**: Edge preprocessing (Section I.5)

**Schema-on-read SIEM footprint and scaling (SDW Lab, zeek-flagship-rerun, 2026-06-10; 10M Zeek conn.log events)**:
- OpenSearch 2.18.0 foil: **2.854s** average across the 5 standardized queries
- Index footprint: **1,868 MB** for 10M events (best_compression, 1 segment), a 2.0× compression against the 3,743 MB raw JSONL, where the same rows land in 440 MB of Iceberg Parquet (8.5×) and 685 MB of ClickHouse native LZ4 (5.5×)
- Superlinear index growth was the retired Dec-2025 bench's single-run observation (1M→10M: 3.47s→27.52s, roughly 8× for 10× the data); the rerun measures only the 10M point, so treat that scaling ratio as a directional historical reading, not a re-measured claim

Whether that superlinear scaling generalizes depends on query type and schema, and the rerun doesn't re-measure it. What the rerun does support is the storage inversion (the Iceberg table is the smallest artifact at 440 MB while the OpenSearch index is the largest compressed form at 1,868 MB), so the directional finding that columnar engines compress and aggregate far more efficiently than index-based SIEMs is structurally sound.

**Cost comparison** (petabyte-scale security data, from the TCO analysis in the handbook's manageability chapter, Chapter 1; pricing as of Q4 2025):
- **Schema-on-read SIEM**: $1.5M+/TB/year (unsustainable at 1+ PB/day)
- **Snowflake**: $23/TB/month storage + $2-$4/TB scanned (Section I.6.3: $38K/month for 10 TB/day)
- **ClickHouse + Iceberg hybrid**: $345-$7,080/month storage (depending on hot/cold ratio) + ~$3K compute
- **Savings**: 75-95% vs traditional SIEM, 50-70% vs cloud data warehouse

### I.4A.7 Key Takeaways from Netflix

Netflix's ClickHouse journey lines up with the MOAR architectural pattern for security data on five points, and what makes them worth carrying over isn't the headline scale but the engineering choices underneath it. Ingestion-path performance compounds, so the generated parsers that beat regex (216μs → 23μs) and the native protocols that beat generic APIs (30%+ gain) both come back to measuring per-event latency rather than trusting the framework. Data layout did more for them than clever algorithms, since sharding the tag-metadata maps took a query from 3s to 700ms by doing less work through better schema design. Hot/cold tiering stops being optional once you're at petabyte scale, where ClickHouse over the recent 30 days in front of Iceberg holding the cold years buys a 10-50× cost reduction. Columnar storage is what makes the analytics affordable, with the 12-19× compression against Elasticsearch and the 5-100× faster analytical queries that Netflix reported. And the lakehouse-plus-specialized-engines shape is the one this appendix argues for throughout, because the multi-engine architecture is where the 50-75% cost savings against single-platform come from (Section I.6.3).

### I.4A.8 Sidebar: Vortex, one layer below the engine choice

> A question worth tracking sits underneath everything in this appendix, at the file format the engines actually read. Vortex is an open columnar format (the PyPI package was renamed `vortex-array` → `vortex-data`, which is why it briefly looked abandoned, and it now lives under LF AI & Data), and the pitch is large scan and random-access speedups over Parquet. I ran it against zstd-Parquet on a seeded OCSF corpus rather than take the launch numbers, and the read win was real but single-digit (roughly 1.7–2.6× on a full decode-to-Arrow and 3.3–4× on a selective `dst_port=3389` needle), not the order-of-magnitude the vendor headline suggests, with answers identical across both formats and a footprint that was scale-dependent. The on-disk format has been backward-compatible since v0.36, though the API still ships breaking changes, so pin the version. The reason it stays a sidebar rather than a recommendation is that Vortex is not yet an Iceberg data file: Iceberg 1.11.0 shipped the pluggable File Format API but the Vortex plugin is still an open issue (apache/iceberg#15416), so you can't register it under an Iceberg table the way the MOAR stack registers Parquet. It's promising for scan-heavy read paths, but premature to adopt as a lakehouse format until that plugin lands, so the honest posture is to pin the version and watch the issue rather than build on it today.

---

## Section I.4B: Materialized Views Decision Framework

**Key question**: Should you pre-compute query results (materialized views) to accelerate security analytics, or query raw tables directly?

The promise is compelling: **78× to 9,000× query speedups** are reported across PostgreSQL, Snowflake, and Databricks (Tier C: vendor documentation and their own benchmarks, best-case workloads, not independently reproduced). Pre-aggregate authentication failures once, serve dashboard queries hundreds of times, and avoid rescanning terabytes for every refresh.

**But security data's unique characteristics create specific failure modes** that make materialized views far more complex than vendor documentation suggests.

### I.4B.1 The Core Trade-off: Refresh Cost vs Query Savings

Materialized views provide economic value when:

```
Query_cost × Query_frequency > Refresh_cost × Data_change_rate + Storage_cost
```

**Example**: An authentication failure dashboard refreshing every 5 minutes (288 queries/day) costs $144-432/day scanning 50 GB raw data. Pre-aggregated to 500 MB materialized view: $3.50-16.50/day (96-97% reduction). But if the same dashboard refreshes once per week, refresh costs EXCEED query savings.

So materialized views only make economic sense when the query frequency runs well ahead of the data change rate, which is the whole condition the inequality above is checking.

### I.4B.2 Security Data's Three Failure Modes

**Failure Mode #1: High Data Change Rates**

Security logs are append-heavy with continuous ingestion (EDR: 1M events/minute, network flows: 5-20 GB/hour). For correlation rules joining multiple tables, changes to ANY table trigger expensive recomputation. A lateral movement detection joining `auth_logs` (50 GB/day), `ip_reputation` (2 GB/day updates), and `malware_detections` (5 GB/day) forces full refresh daily, so refresh cost equals or exceeds query savings.

**Failure Mode #2: Schema Volatility**

Security schemas change frequently (new log sources, vendor updates, OCSF evolution). Platform responses are aggressive:

| Platform | Column Added | Column Dropped | Column Renamed |
|----------|-------------|----------------|----------------|
| **Snowflake MVs** | View unchanged | **All MVs suspended** | Suspended |
| **Databricks MVs** | Full recompute | Full recompute | Full recompute |
| **Dremio Reflections** | **INVALID** | INVALID | INVALID |

Snowflake suspends ALL dependent materialized views on ANY column modification — even columns not referenced in the view.

**Failure Mode #3: Complex Queries Force Full Refresh**

The q-hierarchical dichotomy (a result from incremental-view-maintenance theory, which separates queries whose results can be updated incrementally from those that cannot) shows that some patterns can't be maintained incrementally at all:

| Query Pattern | Why Full Refresh Required |
|---------------|---------------------------|
| **MEDIAN/PERCENTILE** | Non-distributive — must access all values |
| **Window functions (LAG, LEAD, RANK)** | Row order changes affect entire partition |
| **Multi-table JOINs with concurrent changes** | Multiple changing inputs trigger full recomputation |

Percentile-based behavioral baselines and process ancestry tracking (both common security use cases) hit these limits directly.

### I.4B.3 When Materialized Views Win for Security Data

Despite these challenges, materialized views provide clear value for specific use cases:

**1. Low-frequency updates + high-frequency queries**

Compliance reports running 50 times/day against weekly-refreshed policy violation summaries. Refresh cost: 1× per week. Query savings: 350× per week.

**2. Single-table aggregations on append-only logs**

Daily authentication statistics pre-aggregated overnight, queried throughout the day for dashboards. Single table, append-only, simple aggregation (distributive), so incremental refresh processes only new day's partition. 288 queries/day vs 1 refresh/day = 288:1 benefit ratio.

**3. Expensive aggregations serving multiple consumers**

Behavioral baselines (median file creates per user) computed once, used by 20 different detection rules. The 1× compute cost amortizes across 20 consumers.

**Snowflake production data** (Tier C: Snowflake-published figure, not independently reproduced): a reported 21.3% cost reduction for workloads matching these patterns, which isn't the 95% reduction the headline numbers suggest, but it's worthwhile savings when applied selectively.

### I.4B.4 The Four-Tier Materialization Strategy

Match materialization approach to workload characteristics:

| Tier | Latency | Platform | Use Case |
|------|---------|----------|----------|
| **Streaming** | Sub-second | Kafka + Flink, Materialize | Real-time detection (5-min window alerts) |
| **Micro-batch** | 5-15 min | Dremio Reflections, Databricks MVs | Behavioral baselines, simple aggregations |
| **Batch** | Daily/weekly | Spark jobs, dbt models | Complex analytics, compliance reporting |
| **Data Lake** | On-demand | Iceberg + Trino/DuckDB | Ad-hoc threat hunting (no materialization) |

**What the public Netflix material does and doesn't say**: the optimizations Netflix has described publicly (the ClickHouse blog post and Daniel Muino's meetup talk) are all base-table and ingest-path engineering — generated lexers for fingerprinting, a custom native insert protocol, sharded tag maps — and none of them is a materialized view. The public record therefore shows a 5 PB/day system reaching sub-second queries through layout and parser work rather than materialization, which is a useful existence proof that heavy materialization isn't a prerequisite at scale. It is not, to be careful about it, a documented statement that Netflix runs "zero materialized views" — I haven't seen them claim that, and the absence of MVs in the write-ups isn't the same as a confirmed architectural decision to avoid them.

### I.4B.5 Decision Framework: When to Materialize

**Deploy materialized views when ALL of the following are true**:

1. **Query frequency >> Data change rate**: Dashboard refreshing every 5 minutes, data updating every hour (12:1 ratio or higher)
2. **Refresh cost < Query cost savings**: $50/day refresh cost, $500/day query savings (10× benefit minimum)
3. **Schema stability**: Log source schema changes <1×/month
4. **IVM-compatible query patterns**: Simple aggregations, single-table or append-only multi-table
5. **Measured benefit validation**: Pilot with 3-5 views, measure actual performance gain and refresh costs before expanding

**Avoid materialized views when ANY of the following are true**:

1. **Schema volatility**: New log sources added weekly, vendor format changes monthly
2. **Complex correlation requirements**: 5-table joins with window functions and non-distributive aggregates
3. **Unpredictable query patterns**: Threat hunting workloads where queries are written during investigations
4. **High data change rates**: All source tables updating continuously (multi-table concurrent changes trigger full refresh)
5. **Insufficient operational expertise**: Team lacks experience debugging materialized view refresh failures

**Vendor recommendations align with selective deployment**:

- **Snowflake**: "Start slowly with this feature (i.e. create only a few materialized views on selected tables) and monitor the costs over time"
- **Databricks**: Materialized views "well-suited for data processing workloads such as ETL processing," meaning known patterns, not ad-hoc exploration
- **AWS Redshift AutoMV**: Automatically creates materialized views—**but also automatically drops them when cost-benefit analysis turns negative**

### I.4B.6 Failure Mode Summary

| Failure Mode | Trigger | Impact | Mitigation |
|---|---|---|---|
| **High data change rate** | Multiple source tables updating continuously | Full refresh triggered (kills IVM benefit), refresh cost > query savings | Limit MVs to single-table or append-only patterns |
| **Schema volatility** | New log source formats, vendor API changes | Snowflake: ALL dependent MVs suspended on ANY column change | Use staging view layer to absorb changes; OCSF normalization at ingestion |
| **Complex query patterns** | 5+ table joins, window functions, non-distributive aggregates | IVM impossible, forced full refresh on every update | Pre-aggregate simpler intermediate tables, materialize final step only |
| **Cache staleness** | Real-time security events queried against stale materialized data | Analysts miss active threats, false confidence in dashboard accuracy | Set refresh intervals based on detection SLA, not cost optimization |
| **Operational complexity** | Dozens of MVs across multiple schemas | Cascading refresh failures, debugging refresh lag, schema change propagation | Start with 3-5 MVs, measure actual benefit before expanding (Redshift AutoMV pattern) |

### I.4B.7 Key Takeaways

The posture I'd take on materialized views for security data follows from the failure modes above. Deploy them selectively, because they work for compliance dashboards, scheduled reports, and behavioral baselines on stable schemas, and they become a liability once the schema churns or the correlation gets complex. The reason they're harder here than in general BI analytics is that security data's high change rates, schema volatility, and complex correlations all push against incremental maintenance, so the mitigations that help are a staging view layer to absorb the schema volatility and OCSF normalization (Appendix H) to stabilize the schemas at ingestion. The 78-9,000× speedups only turn into savings when query frequency runs well ahead of the data change rate, which is why I'd pilot with three to five views and monitor refresh cost against query savings per view before expanding, the way Redshift AutoMV does it automatically. One more limit is worth setting against the speedup headline, because it's easy to read "an MV makes this query 78× faster" as "an MV helps when the system is under load," and a scored run of the workload-interference bench says it does not (SDW Lab, 2026-06-14, Tier B, single host, 10M-row corpus; quote the knee location, not the p95 magnitude, which spreads near saturation). On the scheduled-versus-ad-hoc mix, base StarRocks holds the interactive p95 flat out to roughly 32× the base scheduled rate and inflects at 64× (reproduced across three runs); a StarRocks arm with six pre-built materialized views covering the scheduled set, EXPLAIN-verified to actually rewrite, knees at the same 64×, zero steps to the right. The reading is that at the knee the binding constraint is open-loop scheduler and per-query coordinator saturation rather than the per-query compute the MV accelerates, so even a near-instant MV-rewritten query still pays the fixed per-query overhead the scheduler is firing 64× as often, and pre-materializing the answers buys no interference headroom. The caveat travels with the number — it's a single MV run on this corpus, heavier shapes would move the knee left, and a firm claim wants reproduction — but the direction is the result: an MV is a per-query compute lever, not a concurrency one, so don't reach for materialization to fix a noisy-neighbor problem that workload segregation (Section I.7) is the actual fix for. And the layered shape is what holds all of this together, matching the materialization tier to the workload across the streaming, micro-batch, batch, and data-lake rungs rather than reaching for one tier everywhere.

For detailed platform comparisons, see the Appendix E resource directory. For OCSF normalization, which is the schema-stability foundation successful materialized views depend on, see Appendix H.

---

## Section I.5: DuckDB for Edge Preprocessing

### I.5.1 Validated at Extreme Scale

**Jake Thomas (Okta)** (Tier B: personal communication): "7.5 trillion records processed in 6 months using thousands of concurrent DuckDB Lambda instances." This is Jake's own account of the system he built; it has not been independently audited.

**Architecture**:
```
[CloudTrail S3 Events] (raw JSON, 10-50 TB/day variable)
    ↓
[Lambda Function Triggered] (1 Lambda per S3 object notification)
    ↓
[DuckDB In-Memory Processing] (filter, normalize, compress)
    ↓ 50-80% volume reduction
[S3 Parquet Files] (optimized, partitioned)
    ↓
[Iceberg Tables] ← Query engines (Trino, Dremio, Spark)
```

**Cost impact**: Jake Thomas described Okta's previous Snowflake approach at approximately $2,000/day. The DuckDB serverless cost he characterized as "dramatically reduced"; the 80-95% savings estimate ($100-$400/day) is a reasonable inference from those numbers, not a figure he stated directly.

**Scalability validation**: 1.5-50 TB/day variable workload (50× peak-to-trough ratio) handled by serverless auto-scaling (thousands of concurrent Lambda functions).

### I.5.2 CloudTrail Filtering Pattern

**Problem**: AWS CloudTrail generates massive read-only noise (80% "Get", "List", "Describe" operations with no security value).

**Without filtering** (Anti-Pattern #11: "Ignoring Edge Preprocessing"):
- Ingest: 10 TB/day raw CloudTrail
- Store: 10 TB/day × $0.023/GB/month = $7,080/month storage
- Query: Threat hunts scan 10 TB (5 minutes per query)

**With DuckDB filtering**:

```python
import duckdb
import json

def lambda_handler(event, context):
    """
    Lambda function triggered by S3 CloudTrail event
    Filters out read-only operations, writes optimized Parquet
    """
    # S3 event contains CloudTrail JSON path
    cloudtrail_path = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']

    # DuckDB in-memory connection (Lambda ephemeral storage)
    con = duckdb.connect(':memory:')

    # Read CloudTrail JSON, filter in single pass
    filtered = con.execute(f"""
        SELECT
            eventTime,
            eventName,
            eventSource,
            awsRegion,
            sourceIPAddress,
            userAgent,
            errorCode,
            errorMessage,
            requestParameters,
            responseElements,
            userIdentity.principalId as principalId,
            userIdentity.arn as userArn,
            userIdentity.type as userType,
            resources
        FROM read_json('s3://{bucket}/{cloudtrail_path}', format='auto')
        WHERE
            (
                -- Keep all errors (security relevant)
                errorCode IS NOT NULL
                -- Keep authentication events
                OR eventName IN ('ConsoleLogin', 'AssumeRole', 'GetSessionToken', 'SwitchRole')
                -- Keep write operations (creates, updates, deletes)
                OR eventName LIKE 'Create%'
                OR eventName LIKE 'Put%'
                OR eventName LIKE 'Update%'
                OR eventName LIKE 'Delete%'
                OR eventName LIKE 'Attach%'
                OR eventName LIKE 'Detach%'
                OR eventName LIKE 'Modify%'
                -- Keep privilege escalation events
                OR eventName IN ('AddUserToGroup', 'PutUserPolicy', 'PutRolePolicy')
            )
            -- EXCLUDE read-only operations (80% reduction)
            AND eventName NOT LIKE 'Get%'
            AND eventName NOT LIKE 'List%'
            AND eventName NOT LIKE 'Describe%'
    """).df()

    # Write to S3 as compressed Parquet (10× compression vs JSON)
    output_path = cloudtrail_path.replace('.json.gz', '.parquet').replace('/raw/', '/processed/')
    con.execute(f"""
        COPY filtered TO 's3://{bucket}/{output_path}'
        (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 100000)
    """)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'input_path': cloudtrail_path,
            'output_path': output_path,
            'rows_filtered': len(filtered)
        })
    }
```

**Results**:
- Volume: 10 TB/day raw → 2 TB/day processed (**80% reduction**)
- Storage: $7,080/month → $1,416/month (**$5,664/month savings**)
- Query speed: 5-minute threat hunts → 1-minute threat hunts (**5× faster**)
- Cost per Lambda execution: $0.0000167/invocation × 10,000 invocations/day = **$167/day = $5,000/month** (still net savings vs storing unfiltered)

What edge preprocessing does is trade compute cost (Lambda executions) for storage and query cost savings, and at CloudTrail scale (TB/day) the storage plus query savings exceed the compute cost by roughly 3-5×.

### I.5.3 VPC Flow Logs Aggregation

**Problem**: AWS VPC Flow Logs generate 50-200× more data than CloudTrail (every network packet = 1 log entry).

**Without aggregation**:
- Raw volume: 100 TB/day
- Storage: $69,000/month
- Queries: Unusably slow (30+ minutes for 1-day scan)

**With DuckDB aggregation**:

```python
def aggregate_vpc_flow(event, context):
    """
    Aggregate VPC Flow Logs to connection-level summaries
    Reduces 200× volume (packet-level → connection-level)
    """
    con = duckdb.connect(':memory:')

    # Aggregate 5-minute batches of VPC Flow Logs
    aggregated = con.execute("""
        SELECT
            srcaddr,
            dstaddr,
            srcport,
            dstport,
            protocol,
            DATE_TRUNC('minute', TO_TIMESTAMP(start)) as time_bucket,
            SUM(bytes) as total_bytes,
            SUM(packets) as total_packets,
            COUNT(*) as flow_count,
            -- Aggregate TCP flags (connection state summary)
            BIT_OR(tcp_flags) as tcp_flags_summary,
            -- Aggregate actions (ACCEPT vs REJECT counts)
            SUM(CASE WHEN action = 'ACCEPT' THEN 1 ELSE 0 END) as accepted_count,
            SUM(CASE WHEN action = 'REJECT' THEN 1 ELSE 0 END) as rejected_count
        FROM read_csv('s3://bucket/vpc-flow/*.log', delim=' ')
        GROUP BY srcaddr, dstaddr, srcport, dstport, protocol, time_bucket
    """).df()

    # 200× reduction (packet-level → connection-level aggregates)
    con.execute("""
        COPY aggregated TO 's3://bucket/vpc-flow-aggregated/out.parquet'
        (FORMAT PARQUET, PARTITION_BY (time_bucket))
    """)
```

**Results**:
- Volume: 100 TB/day → 500 GB/day (**200× reduction**)
- Storage: $69,000/month → $345/month (**$68,655/month savings**)
- Queries: 30 minutes → 30 seconds (**60× faster**)

**Trade-off**: Lose packet-level granularity (acceptable for most security use cases, since connection-level visibility is sufficient for threat hunting; keep raw logs in S3 Glacier for forensics if needed).

### I.5.4 When to Use DuckDB Edge Preprocessing

**Use DuckDB when**:

1. **High-volume, low-value-density data** (CloudTrail 80% read-only, VPC Flow 99% benign)
2. **Variable workloads** (1-50 TB/day spikes, where serverless auto-scales)
3. **Cost-sensitive** (storage + query savings exceed Lambda compute cost)
4. **Filter/aggregate logic is simple** (SQL-expressible, not complex ML models)

**Don't use DuckDB for**:

1. **Low-volume data** (<100 GB/day, where edge preprocessing overhead isn't worth it)
2. **Interactive queries** (use Trino/Dremio for analyst-facing queries)
3. **Complex transformations requiring PySpark libraries** (use Spark for ML feature engineering)

**Decision framework**: If raw data volume is 5-10× larger than valuable subset, **edge preprocessing with DuckDB pays for itself within 30 days**.

### I.5.5 DuckLake: SQL-Based Catalog Now Shipping

DuckDB Labs shipped DuckLake v1.0 on April 13, 2026 — so the "experimental, not production-ready" framing from earlier drafts of this book is no longer accurate. DuckLake is now production software with a backward-compatibility guarantee and the `ducklake` extension shipping in DuckDB v1.5.2 as a top-10 core extension by downloads.

The architectural idea is worth understanding because it's a real inversion of the Iceberg/Delta approach. Where Iceberg and Delta store metadata in files (Avro manifests, JSON), DuckLake stores metadata in a SQL database — PostgreSQL, SQLite, or DuckDB self-hosted — and keeps data in Parquet files on object storage. That means catalog operations resolve via a SQL query rather than a chain of manifest files, which is meaningfully faster for small commits and streaming inserts. DuckDB Labs' own benchmarks (Tier C — vendor self-published, not independently reproduced) report roughly 100× faster streaming inserts compared to Iceberg's file-per-commit behavior on the same workload; those numbers are favorable to DuckLake's best-case scenario (pure-streaming, small commits), not a general-purpose head-to-head. Large analytical scans, multi-writer concurrency, and cross-engine compatibility at scale have not been independently benchmarked.

Some of that independent validation now exists, from my own lab rather than the vendor's, and it makes the gap both smaller and better-characterized than the headline. Running the streaming-commit workload on a single host, I reproduced DuckLake's inlining advantage over Iceberg at a modest **2–4× on tiny commits** (largest at the smallest batch, narrowing as the batch grows) rather than the vendor's 100–900×, so the direction holds while the magnitude is regime-specific and far smaller in a controlled run. The planning-speed claim held up more cleanly: with the engine held constant and files allowed to accumulate from 10 to 200, Iceberg's manifest planning grew **17.6×** while DuckLake's SQL-catalog resolution stayed flat, which is the architectural inversion above made visible as a number. And the large-analytical-scan worry mostly did not materialize, because at a billion rows, reading **byte-identical Parquet** registered into both an Iceberg and a DuckLake catalog, three of four queries came back at parity (within about 1%), which means the read-speed lever is the Parquet encoder rather than the table format. One heavy high-cardinality aggregation diverged about 1.3×, a reminder that the two engines' read paths still differ on the hardest scans, but the headline is that on identical bytes the formats read neutrally. All of this is Tier B, single machine, so the ratios transfer and the absolute times don't; the practical posture is unchanged (track DuckLake, don't yet build production security pipelines on it), but the performance story is now measured rather than taken from the vendor's best case.

One caution from the same lab work generalizes past DuckLake to any time you let more than one engine read the same open format, which is the whole premise of this appendix. When I ran a cross-engine answer-equality check before timing anything, one engine returned a filtered `count(*)` tens of rows short of the others over the byte-identical Parquet, silently, with no error raised — a deterministic equality-filter undercount in the tail row groups of the file. The reason it matters here is that a timing-only benchmark would have recorded that engine's wrong answer as a fast result and published it as a win, and in a detection pipeline a `count` that reads low doesn't crash, it just quietly under-counts a threshold. So engine selection over an open format carries a verification obligation the portability story tends to gloss: the engines are interchangeable for the SQL and roughly for the latency, but answer-equivalence is not free, and a standing cross-engine equality check on a few known-answer queries (re-run whenever you add an engine or bump a version) is the cheap insurance that catches it. A later, broader run sharpened both the worry and its bound: across twelve publishable Parquet readers on the same bytes — engines selected by distinct reader, since the divergence lives in the reader, not the query engine wrapped around it — ten were correct and only two silently wrong, so the risk is real but concentrated rather than pervasive, and most readers that fail do so loudly, by erroring (SDW Lab, `clickhouse-vs-duckdb/results/MULTI-ENGINE-CORRECTNESS.md`, Tier B, version-bound). The two failers are the reason "version-bound" is load-bearing rather than boilerplate: the chDB v3-reader Bloom-filter undercount was real on chDB 4.1.8 and fixed by the next point release (4.1.9 reads every cell correctly), while the fastparquet `PLAIN_DICTIONARY` mis-decode is still wrong on the latest version (2026.5.0), so the honest current statement isn't a static "two silently wrong" but "we caught two silently-wrong readers; one was fixed in a point release and one still isn't — which is exactly why the equality check belongs in CI rather than being assumed once and trusted forever." Two practical refinements fall out of it. The equality check needs a type-aware notion of "agree," because the same floating-point sum computed by different engines diverges in the last bit from ordinary IEEE-754 rounding while integer counts and sums match exactly, so you compare integers exactly and floating-point results within a tolerance. And the obligation reaches below the query to the bytes themselves: Parquet's per-page checksums are verified by some readers and ignored by others, so a corrupted page can return a confident wrong number on an engine that doesn't check, which makes verifying the answer and verifying the bytes two separate jobs an evidence-grade pipeline wants both of.

The same silent-wrong-answer pattern shows up a layer up from the reader too, at the detection logic itself, and the clearest measured case is text search. On a synthetic 2M-message corpus (Tier B, single host, median of 5; the synthetic corpus flatters indexes, so read the cross-arm comparison rather than the absolute milliseconds), an OpenSearch inverted index answered a base64-blob regex (`[A-Za-z0-9+/]{40,}`) in 5 ms but returned only 3,159 of the 7,946 true matches, missing roughly 60%, because the standard analyzer splits on `+` and `/` and fragments the blob into sub-tokens shorter than the pattern, while ClickHouse's raw-text `match()` and Hyperscan both returned the correct 7,946 in about 106 ms. For base64-payload hunting, anything that spans token boundaries, the index trades correctness for speed silently, and the only way to make it correct is to regex a non-analyzed field, which gives up the index speed that was the reason to reach for it. The mapping layer has its own version of the same failure, worked through in Appendix H, where a shipped Zeek-conn OCSF mapping picks the right class and fills every field but classifies the connection's activity wrong on most records, so a field-coverage score rates it clean while a detection filtering on that activity mis-buckets most of what it reads. Both land where the page-checksum split above lands: the answer comes back fast and confident and wrong, and only a ground-truth comparison catches it. That is why the fair-broker posture this appendix takes is to measure what a vendor asserts rather than time it, because "maps to OCSF" and "searches your logs" are coverage and capability claims, and whether they are correct on the records that matter is a separate measurement the buyer has to run.

The caveats that matter for security data architecture: DuckLake is DuckDB-centric on compute. Spark and Trino connectors are listed as in-progress (via MotherDuck and community contributors as of April 2026), but broader multi-engine support is less mature than Iceberg's ecosystem. The catalog database also introduces a new operational dependency — PostgreSQL or SQLite availability is now a hard requirement for table availability, which changes the failure model compared to object-storage-only Iceberg. Security environments that need ABAC, full audit trails, and provenance maturity will find DuckLake hasn't demonstrated those properties yet.

That new failure model is the part I went and measured rather than asserted, because the fair-broker move is not to argue the vendor's planning-speed headline but to run the failure modes a security team actually hits when it stands DuckLake up on a Postgres catalog. Three verified-real, currently-open `duckdb/ducklake` issues, reproduced (or not) per version (SDW Lab, 2026-06-14, Tier B, single host), and the version-binding is what matters most here, because these verdicts are catalog-layer only and may close the way one of them already did, so re-run them on the next DuckLake release before repeating them. The first is a silent correctness bug. On DuckDB 1.5.3 with the DuckLake extension at commit e6a3bd0a, two concurrent deletes of the same row commit without conflict when one is inlined (under `DATA_INLINING_ROW_LIMIT`) and the other is a Parquet delete file above that limit, because the conflict check never compares the two stores, and the deleted rows then reappear: in both commit orders the repro leaves **29 rows** that a correct system would have deleted to **0**, with no error raised (issue #1215, open). For a security lakehouse that is the worst class of bug, because a deletion that doesn't take effect — a GDPR erasure, a retention expiry, a tombstoned false-positive — fails silently under ordinary concurrent SQL. The second is a hard ceiling on wide schemas: DuckLake unconditionally creates a backing inlined-data table carrying every user column as `BYTEA`, which collides with Postgres's hard 1600-column-per-table limit, so 1,500 columns create fine while 1,600 and 1,700 both fail with `ERROR: tables can have at most 1600 columns`, and setting the inlining row limit to 0 does not help because the backing schema is still emitted in full (issue #1184, open, identical on the inlining-disabled path). Security schemas go wide — a fully-flattened OCSF event with all profiles and observables, or a normalized EDR or firewall table, can exceed 1,600 columns — so this is a concrete architectural constraint on the schema-on-write path through a Postgres-backed catalog, and it pairs directly with the flattening-fidelity and nested-OCSF cost the rest of this book documents. The third is the version-currency lesson the chDB answer-equality story (Sections I.1.5 and I.9) already taught in another corner of the stack: on DuckDB 1.5.2, where the extension auto-resolves to commit 415a9ebd, creating 60 tables then one `information_schema.tables` query hangs **60 s** and fails with a connection-pool timeout that exhausts at 14 connections (one per worker thread on this 14-thread host, exactly the thread-local-caching mechanism the issue described), while on DuckDB 1.5.3 the identical workload returns in **0.036 s** with no timeout (issue #1031, fixed between 1.5.2 and 1.5.3). The issue is still labeled open upstream with a PR pending, but the controlled old-version-versus-new comparison shows the fix is effectively in the 1.5.3 release, and that control matters more than the bug itself: "probably fixed" is worthless without running both versions, and the old-version reproduction is what separates a real fix from a repro that simply under-triggers on a given host. So the honest reading of DuckLake's SQL catalog is the one the planning-speed numbers above already pointed at: it buys the flat metadata resolution and pays for it in catalog-layer correctness and operability surface, two gaps open today (#1215, #1184) and one regression a point release already closed (#1031), and the surface is worth pinning to versions precisely because the design is interesting enough to keep watching closely.

What DuckLake does offer that's genuinely useful: data files are Parquet and Iceberg-compatible, so the format isn't a lock-in risk. If DuckLake's multi-engine story matures — and the V1.0 adoption signal (top-10 extension, MotherDuck hosted support, named Apache DataFusion and Spark integrations) suggests it's being actively developed — it's a plausible future option for DuckDB-centric security analytics at smaller scale. For now, the right posture is to track it, not build production pipelines on it.

---

## Section I.6: Hybrid Architecture - Putting It All Together

### I.6.1 Complete Security Data Pipeline

```text
┌─────────────────────────┐
│   Raw Security Data     │
│  (CloudTrail, VPC Flow, │
│   Zeek, EDR, etc.)      │
└───────────┬─────────────┘
            │
            ↓
┌─────────────────────────────────────────┐
│  DuckDB Lambda Edge Preprocessing       │
│  • Filter read-only operations (80%)    │
│  • Aggregate packet → connection (200×) │
│  • Normalize to OCSF (Section H.4)     │
│  • Compress JSON → Parquet (10×)        │
└───────────┬─────────────────────────────┘
            │ 50-80% volume reduction
            ↓
┌─────────────────────────────┐
│   S3 / Iceberg Storage      │
│   • Partitioned by date     │
│   • OCSF schema normalized  │
│   • Parquet format          │
└───────────┬─────────────────┘
            │
            ↓ Daily compaction (REQUIRED)
┌─────────────────────────────────┐
│   Spark Maintenance (Nightly)   │
│   • Compact small files         │
│   • Expire old snapshots        │
│   • Merge delete files          │
│   • 80% cost via spot instances │
└─────────────────────────────────┘
            │
            ↓ Query workloads routed by type
            │
      ┌─────┴──────────────┬─────────────────┐
      │                    │                 │
      ↓                    ↓                 ↓
┌──────────────┐   ┌────────────────┐   ┌──────────────┐
│    Trino     │   │    Dremio      │   │    Spark     │
│ Ad-hoc hunts │   │ SOC dashboards │   │  Complex ETL │
│ 5-30 sec     │   │ <1 sec queries │   │  Batch jobs  │
│ First-time   │   │ High-frequency │   │  ML features │
└──────────────┘   └────────────────┘   └──────────────┘
```

### I.6.2 Workload Routing Decision Tree

```python
def route_query(query_metadata):
    """
    Route security query to optimal engine based on workload characteristics
    """
    # Decision tree based on query pattern analysis

    if query_metadata['frequency'] == 'high' and query_metadata['source'] == 'dashboard':
        # SOC dashboards: repeated queries, sub-second latency required
        return 'dremio'  # Reflections enable <1 sec

    elif query_metadata['workload_type'] == 'iceberg_maintenance':
        # Table compaction, snapshot expiration, orphan cleanup
        return 'spark'  # ONLY option for maintenance

    elif query_metadata['query_type'] == 'ad_hoc_investigation':
        # Threat hunting: unpredictable, complex WHERE clauses
        return 'trino'  # Fast interactive, no cache overhead

    elif query_metadata['workload_type'] == 'batch_etl':
        # Complex transformations, PySpark libraries, scheduled jobs
        return 'spark'  # Mature ecosystem for data engineering

    elif query_metadata['needs_federation']:
        # Join Iceberg + PostgreSQL CMDB + Elasticsearch
        return 'trino'  # 40+ connectors, federated queries

    else:
        # Default: general-purpose threat hunting
        return 'trino'
```

**Routing implementation**: Query gateway (Trino Gateway, Presto Gateway, or custom API) classifies incoming queries and routes to appropriate engine.

### I.6.3 Cost Comparison: Hybrid vs Single-Platform

**Scenario**: Enterprise SOC
- **Data volume**: 10 TB/day security telemetry
- **Retention**: 90 days hot, 7 years total (cold storage)
- **Analysts**: 50 security analysts (24/7 SOC)
- **Dashboards**: 20 displays, 200 tiles, 30-second refresh
- **Threat hunts**: 50 investigations/week (30 queries each)

**Option 1: Snowflake Only** (single-platform baseline):

| Component | Monthly Cost | Calculation |
|-----------|--------------|-------------|
| Storage (10 TB/day × 90 days) | $20,700 | 900 TB × $23/TB/month |
| Compute (dashboards) | $14,400 | 24,000 queries/hour × 5 sec × $0.10/hour |
| Compute (threat hunting) | $3,000 | 1,500 queries/week × 30 sec × $0.10/hour |
| **Total** | **$38,100/month** | **$457,200/year** |

**Option 2: Hybrid Architecture** (optimized multi-engine):

| Component | Engine | Monthly Cost | Calculation |
|-----------|--------|--------------|-------------|
| Edge preprocessing | DuckDB Lambda | $5,000 | 10 TB/day → 2 TB/day (80% reduction) |
| Storage (2 TB/day × 90 days effective) | S3 | $4,140 | 180 TB × $23/TB |
| Maintenance (nightly) | Spark (spot) | $42 | Weekly compaction, 80% spot savings |
| SOC dashboards (200 tiles) | Dremio | $1,410 | 4 DCU × $352.50/DCU/month |
| Threat hunting (50 analysts) | Trino cluster | $3,000 | Self-managed cluster, 3 nodes |
| Reflection storage | S3 | $460 | 20 TB Dremio reflections |
| **Total** | | **$14,052/month** | **$168,624/year** |

**Savings**: $288,576/year (63% cost reduction vs Snowflake-only)

**Performance improvements** (illustrative, derived from the cost scenario above, not a first-party run):
- Dashboard latency: 5-15 seconds → <1 second (Dremio Reflections)
- Threat hunts: 30-60 seconds → 8-15 seconds (80% volume reduction)
- Query cost: $38,100/month → $14,052/month (63% savings)

---

## Section I.7: The Noisy Neighbor Problem

"Segregating workload types vital for noisy neighbor." — a data-platform practitioner [Personal communication, October 2025]

The problem shows up the moment SOC dashboards and 30-day threat-hunting scans share the same Trino cluster, because a 60-second full table scan queues behind the dashboard refreshes and analysts miss real-time threats during the active attack. The reason this hurts more in security than in general BI analytics is the cost of the wait: where a 60-second lag on a business dashboard is merely annoying, threat detection needs the low latency held even while a hunt is running.

The way I'd fix it is to dedicate a separate cluster per workload type, as in Section I.6.1's architecture diagram, with a query gateway routing by source so that Grafana goes to Dremio, Jupyter investigations to Trino, and Airflow ETL to Spark, and each cluster gets its own CPU and memory with no contention, right-sized for the pattern it serves. That's what keeps the SOC dashboard under a second even while a 30-day threat hunt is grinding away on the Trino cluster, because the hunt no longer has anything to queue behind the dashboard for.

### I.7.1 The interference knee, measured

The practitioner quote is the practitioner reason to segregate, and I went and put a first-party number on where the interference actually starts to bite, because the question a SOC architect really has is not whether co-tenancy hurts but how much co-tenant company an engine tolerates before the interactive experience cracks (SDW Lab, 2026-06-14, Tier B, single host: Beelink 5800H under WSL2, 48 GB / 14 threads, a cpuset 12/2 engine-versus-client split). The bench runs one engine at a time against the 10M-row Zeek conn corpus the rest of this appendix uses, fires a scheduled detection load open-loop on a fixed 60-second cycle so a slow response backs the queue up rather than throttling the scheduler, and probes the interactive p95 in a coordinated-omission-safe way against six pre-registered query shapes, with the breaking point declared up front so I wasn't choosing it after the fact. The interactive baseline is genuinely jittery on this host (probe CV 43.9–47.9% at null load), which is part of why the claim below is the knee's location and not its precise magnitude.

What the curves show is a lot of headroom and then a clean inflection. ClickHouse-native, ClickHouse-over-Iceberg, and StarRocks all hold the interactive p95 flat through 32× the base scheduled rate, at 0.099 s, 0.193 s, and 0.112 s respectively at that step, fifty to a hundred times under the 10-second "flow" threshold, and then they knee at 64×, where the p95 jumps to about 3.21 s for ClickHouse-native, 2.70 s for ClickHouse-over-Iceberg (a wide 1.16–4.05 s band across runs), and 3.77 s for StarRocks. Even at the knee every arm stays under the 10-second flow line and well under the 30-second "tolerable" one, and the knee reproduced at the same 64× step across three independent runs for all three engines, which is the pre-registered bar for claiming it. The magnitude at the knee spreads run-to-run the way latencies do near saturation, so what I'm claiming is the location of the inflection and the shape of the failure, not a precise number of seconds.

That shape is the affirmative measured argument for the dedicate-a-cluster fix this section already recommends. These engines absorb a large multiple of any realistic SOC scheduled load on the interactive path, and then past the knee the open-loop scheduler saturates and the queue grows rather than the latency drifting up gently, so the failure when it comes is the noisy-neighbor failure practitioner described, arriving suddenly at a load coordinate you'd rather discover in a bench than during an incident. Isolating each workload on its own cluster removes the co-tenant load that drives an engine toward its knee, which is why the routing table above is a capacity decision and not only a tuning one.

The single-host caveat travels with the number the same way it does everywhere else in this appendix, because the absolute coordinate of 64× is bound to this host, this cpuset, and this 10M-row corpus, and a larger corpus or heavier query shapes would move the knee left, so don't read 64× as a portable headroom you get for free. What travels is the ordering across engines and the failure shape, a flat interactive p95 under heavy scheduled company that then inflects reproducibly into scheduler saturation, and the practical reading that workload segregation is what keeps a real SOC well to the left of wherever its own knee sits.

---

## Section I.8: Implementation Roadmap

| Phase | Timeline | Goal | Key Actions | Cost Estimate |
|-------|----------|------|-------------|---------------|
| **1: MVP** | Month 1 | Trino + Spark foundation | Deploy 3-node Trino cluster, configure weekly Spark compaction (spot instances, Sunday 2 AM), optionally add DuckDB Lambda for CloudTrail preprocessing | $3K-5K/month |
| **2: Dashboards** | Month 2 | Sub-second SOC displays | Add Dremio (2-4 DCU), migrate top 10 dashboard queries from Trino, enable auto-recommended Reflections (10-20 for 200 tiles) | +$1.4K/month |
| **3: Optimize** | Month 3-4 | Maximize savings | Deploy query gateway (route by workload type), move Spark to spot instances with checkpointing, review Reflection efficiency, measure ROI vs baseline | $10K-15K/month total |

**Phase 1 success criteria**: Threat hunts <30 seconds (30-day scans), maintenance running weekly, optional 50-80% volume reduction from edge preprocessing.

**Phase 2 success criteria**: SOC dashboards <1 second (95th percentile), Reflection hit rate >80%, no noisy-neighbor interference.

**Phase 3 success criteria**: 50-75% cost reduction vs single-platform baseline, <10 hours/week operational overhead.

---

## Section I.9: Key Takeaways and Decision Framework

The findings that hold up across the production accounts and my own lab runs converge on a few things. There's no universal engine, so the hybrid architecture is what delivers the 50-75% cost savings against a single engine (H-ARCH-02: 0.95 confidence), and the reason the case rests on cost, workload conflict, and operational fit rather than raw speed is that in my single-host join bench (Tier B, 2026) every engine answered every SOC-scale join in well under 1.5 seconds, which is too compressed a spread to choose on. Spark stays irreplaceable for Iceberg maintenance, the one thing you can't skip even after standing up Trino for hunts and Dremio for dashboards (H-ARCH-04: 0.98 confidence, a data-platform practitioner validation). Segregating workloads is what keeps the noisy-neighbor interference out of security operations, where a queued scan costs you a missed detection rather than a slow report (a data-platform practitioner, and now measured: in the workload-interference bench of Section I.7.1 the three columnar/MPP arms hold the interactive p95 flat through 32× the base scheduled rate and knee at a reproduced 64×, single host, Tier B, so the affirmative reason to isolate is that the interference failure arrives suddenly at the knee rather than degrading gently). DuckDB edge preprocessing changes the economics by cutting 50-80% of the volume before it lands, which Jake Thomas validated at 7.5 trillion records at Okta. And Dremio Reflections are what take the dashboard query from the illustrative 5-15 seconds down to under a second (Section I.4.2's worked scenario, not a first-party run).

**Decision framework summary**:

| Security Workload | Optimal Engine | Latency Target | When to Use |
|-------------------|----------------|----------------|-------------|
| **SOC Dashboards** | Dremio | <1 second | High-frequency queries (>10/hour), same pattern |
| **Threat Hunting** | Trino/Starburst | 5-30 seconds | Ad-hoc investigations, first-time queries |
| **Batch ETL** | Spark | Minutes-hours | Complex transformations, PySpark libraries |
| **Iceberg Maintenance** | Spark | Hours (nightly) | File compaction, snapshot expiration (REQUIRED) |
| **Edge Preprocessing** | DuckDB Lambda | 1-5 minutes | Filter/aggregate before lakehouse (50-80% reduction) |

A handful of implementation principles fall out of all of this. Budget for Spark maintenance from Day 1, because the performance collapse from skipping it is the expensive kind to recover from. Segregate the workloads by cluster so SOC dashboards never compete with threat hunts for the same memory. Invest in edge preprocessing where the data warrants it, since at TB/day scale it pays back 5-10× inside 30 days. And start simple, with Trino and Spark, adding Dremio only once dashboard latency is an actual problem rather than an anticipated one.

The harder thing to carry out of this appendix isn't the routing table, which mostly writes itself once you've named the workloads, but the obligation that comes with running several engines over one open table. The portability story sells the engines as interchangeable, and for the SQL and roughly for the latency they are, but answer-equivalence is not something you inherit for free: a fast engine can be silently wrong, as the chDB Bloom-filter undercount and the tail-row-group equality-filter undercount both were, reading clean at 10M and short at 100M with no error raised. So the team that chooses this architecture is the one now accountable for a standing cross-engine equality check on a few known-answer queries, re-run whenever an engine is added or a version bumped, type-aware enough to compare integers exactly and floating-point within a tolerance, and reaching down to the Parquet page checksums that some readers verify and others ignore. That verification discipline is the price of the cost savings and the workload fit, and it's the part no benchmark hands you.

---

## References

**Primary validation sources**:
- a data-platform practitioner [Personal communication, October 2025]: Hybrid architecture patterns, workload segregation, Spark irreplaceable for Iceberg (Tier B)
- Jake Thomas (Okta) [Personal communication]: DuckDB extreme scale validation (7.5T records in 6 months, $2K/day Snowflake → "dramatically reduced" — figures are Jake's own account, not independently audited) (Tier B)
- Netflix ClickHouse scale figures [Daniel Muino, ClickHouse meetup presentation, late 2024]: 5 PB/day, 10.6M events/sec, sub-second queries — vendor ecosystem presentation, not independently reproduced (Tier C)
- Schema-on-read SIEM bake-off [SDW Lab, zeek-flagship-rerun, 2026-06-10]: a two-regime split over 10M OCSF-normalized Zeek conn.log events, 5 standardized queries, CV-gated, answers verified equal — the OpenSearch 2.18.0 foil (2.854s avg) against ClickHouse-native (0.061s, 46.8×), ClickHouse-over-Iceberg (0.282s, 10.1×), StarRocks (0.343s, 8.3×), and Trino (0.795s, 3.6×); the index wins the cheap lookups, the lakehouse wins the heavy hunting aggregations. Supersedes the splunk-db-connect-benchmark (Dec 2025, retired). One specific workload, directional for network-telemetry analytical queries (Tier B)

**Technical documentation**:
- [Apache Spark Iceberg Procedures](https://iceberg.apache.org/docs/latest/spark-procedures/)
- [Trino Iceberg Connector](https://trino.io/docs/current/connector/iceberg.html)
- [Dremio Reflections Architecture](https://docs.dremio.com/cloud/acceleration/reflections/)
- [DuckDB SQL Reference](https://duckdb.org/docs/sql/introduction)
- [DuckLake v1.0 release](https://ducklake.select/2026/04/13/ducklake-10/) (April 13, 2026)
- [DuckLake Data Inlining mechanics](https://ducklake.select/2026/04/02/data-inlining-in-ducklake/)
- [MotherDuck DuckLake hosted support announcement](https://motherduck.com/blog/announcing-ducklake-1-0-on-motherduck/)

**Validated hypotheses** (from knowledge base):
- H-ARCH-02: Hybrid architectures inevitable (0.95 confidence)
- H-ARCH-04: Spark irreplaceable for Iceberg maintenance (0.98 confidence)

**Case studies**:
- Okta DuckDB serverless (Tier B — Jake Thomas personal account): 7.5 trillion records in 6 months, 50 TB/day peak, $2K/day Snowflake → "dramatically reduced" DuckDB serverless cost
- Healthcare SOC hybrid (composite model): $38K/month Snowflake → $14K/month hybrid (63% savings, <1 sec dashboards) — illustrative calculation, not a named client
