---
type: crosswalk
title: "Appendix D: Security ↔ Data Engineering Terminology Translation Guide"
created: 2025-10-15
tags: [security-data, data-engineering, terminology, siem, etl, translation]
---

# Appendix D: The Security ↔ Data Engineering Translation Glossary

I have watched a lot of security architects walk into the data engineering world for the first time, and the scene that follows is a composite of those conversations rather than any single person. Picture a security architect with fifteen years of SOC experience standing in the hallway at Data + AI Summit with their RSA Conference badge still in the laptop bag. They have been to dozens of cybersecurity conferences, but this is a different room: everyone is talking about medallion architectures, reverse ETL, and semantic layers, terms that never showed up in any threat model they have built.

The keynote describes a "data mesh implementation with domain-oriented decentralized ownership and federated computational governance," and the architect is translating in their head the whole time, because that sounds a lot like a distributed security data architecture where each team owns its own security data sources. At the Iceberg booth they ask about retention policies and the engineer answers with "snapshot expiration, configurable TTL, orphan file cleanup to manage table lifecycle," which is automated deletion of old data while keeping the important parts, the thing security teams have been asking their SIEM vendor for years.

The recognition usually comes in a hallway conversation. A data engineer describes building a lakehouse with real-time streaming ingestion, columnar storage, and federated query engines, the security architect asks whether that is just a SIEM, and the honest answer is that it mostly is, only nobody calls it that. Security architects and data engineers keep solving the same problems in different vocabularies, and the rest of this appendix is the translation guide between the two.

---

**Purpose**: Bridge the terminology gap between cybersecurity and data engineering disciplines. Each entry includes: security term, data engineering equivalent, context notes, and when/why the translation matters.

**How to use**: When reading data engineering documentation (Iceberg docs, Trino blogs, Spark tutorials), reference this glossary to translate concepts into security context. When communicating with data engineering teams, use their terminology for clarity.

---

## D.1: The Translation Challenge

### Why Security and Data Engineering Struggle to Communicate

The core problem is the same concepts expressed in different vocabulary.

Consider a representative exchange between a security architect and a data engineer:

- **Security architect**: "We need to correlate EDR telemetry with network flow logs for lateral movement detection, retaining 90 days hot and 7 years cold for compliance."
- **Data engineer**: "So you want to build an ELT pipeline ingesting endpoint event streams, join with network traffic fact tables, store in Iceberg with tiered lifecycle policies?"
- **Security architect**: "I... think so? Yes?"

The security architect knows what they need, which is threat detection across data sources with long-term retention, and the data engineer knows how to build it with streaming pipelines, table formats, and query engines. Translation friction is what slows collaboration, and the root cause is that the two disciplines evolved in different problem domains.

**Security Operations** is oriented toward threat detection and incident response. Its data is unstructured or semi-structured logs arriving from hundreds of heterogeneous sources. Retention is driven by compliance mandates with fixed timeframes, and the figures teams work to are six years under HIPAA's documentation rule, twelve months of audit log history under PCI DSS, and seven years under the SOX accounting-records regime (D.2 carries the citations and the caveats on each). The query workload is high-cardinality filtering (finding rare events in billions of rows) and the latency requirements combine real-time alerting (seconds to a few minutes, depending on detection type) with interactive investigation (under 60 seconds).

**Business Intelligence** is oriented toward metrics, reporting, and decision-making. Its data is structured, drawn from transactional systems. Retention follows business value, so data is deleted once it's no longer useful. The query workload is aggregation and rollups, summarizing millions of rows to thousands of reporting rows. Batch ETL running hourly or daily is acceptable, and dashboard refresh under 10 seconds satisfies most use cases.

Despite these different profiles, both domains need the same underlying infrastructure: object storage (S3, Azure Blob, GCS), SQL-based query engines, pipeline orchestration (Airflow, Dagster, Prefect), and table formats (Iceberg, Delta). Security architects can use mature data engineering patterns directly, but first the vocabulary has to align.

---

## D.2: What Security Operations Actually Does (Orientation for Data Engineers)

*If you're a security professional, skip ahead to D.3. This primer is for data engineers entering the security domain who need context on how security teams operate day-to-day.*

**The SOC Floor**. Security Operations Centers run 24/7 with tiered analyst teams. Tier 1 analysts triage thousands of alerts daily, escalating suspicious events to Tier 2 investigators who correlate across data sources. Tier 3 analysts handle confirmed incidents, forensic analysis with legal implications where data preservation is mandatory, not optional. Think of it as a 24/7 on-call rotation, but every page may involve an active adversary.

**Detection Engineering**. Detection engineers write rules that fire when suspicious patterns appear in telemetry data. A rule might say: "Alert when a process accesses lsass.exe memory AND the parent process is not an authorized security tool." These are analogous to data quality checks that page on-call engineers, except that the "data quality issue" is an attacker inside your network. Organizations maintain hundreds to thousands of these rules, each tuned to minimize false positives while catching real threats.

**Threat Hunting**. Hypothesis-driven ad-hoc queries across weeks or months of historical data. A threat hunter might ask: "Show me all DNS queries to domains registered in the last 30 days, grouped by source host, over the past 90 days." This is exploratory data analysis, but the goal is finding adversaries who evaded automated detection. Queries are interactive (analysts iterate in real-time), high-cardinality (filtering rare events from billions of rows), and unpredictable (you can't pre-aggregate what you don't know you'll need).

**Incident Response**. When a confirmed breach occurs, responders reconstruct attacker activity across weeks or months of historical data. Legal hold requirements mean data must be preserved as evidence, because deletion or modification can create compliance liability. A typical investigation question: "Show me every action taken by this compromised account between August 1 and October 15, across all systems." This requires queryable long-term retention, not just archived storage.

**Compliance Retention**. Retention timeframes are regulatory mandates, not business choices. HIPAA's Security Rule sets a six-year retention period for the documentation it requires, including written records of required actions, activities, and assessments (45 CFR 164.316(b)(2)(i)), so the six-year figure health-care teams run their logs on comes from a documentation rule that internal policy extends to log retention rather than from an explicit log mandate, and some states require longer, so verify against your state health privacy law. PCI DSS v4.0 Requirement 10.5.1 requires twelve months of audit log history, with at least the most recent three months immediately available for analysis. The seven-year figure people attribute to SOX traces to the accounting-records rule at 18 U.S.C. 1520 rather than to any log-retention statute. Auditors will ask for specific records spanning years, and "we archived that to cold storage and can't query it" is not an acceptable answer.

Real-time alerting (sub-second to a few minutes, depending on detection type), interactive investigation (seconds), and long-term forensics (minutes across years of data) are three fundamentally different query patterns hitting the same underlying data, which is why Appendix I recommends multiple query engines, since no single engine handles all three patterns efficiently.

---

## D.3: Essential Data Engineering Concepts for Security Architects

### Concept 1: Separation of Storage and Compute

*Principle*: Decouple data storage from query processing.

Traditional schema-on-read SIEM approach couples storage and compute:

- Splunk indexers: Storage (tsidx indexes) + compute (search heads) bundled
- Elasticsearch cluster: Storage (shards) + compute (query nodes) in same infrastructure
- Problem: Scaling storage requires scaling compute (expensive, inflexible)

MOAR approach separates them:

```
Storage Layer               Compute Layer
-------------               -------------
S3/Blob/GCS                 → Query Engine (Trino, Dremio, Spark)
+ Iceberg/Delta metadata    → Multiple engines can read same data
```

**Advantages for Security**:
1. **Cost optimization**: Scale storage independently (cheap object storage), scale compute only when querying
2. **Vendor flexibility**: Swap query engines without data migration (try Trino, switch to Dremio, same Iceberg tables underneath)
3. **Multi-workload support**: Use Trino for ad-hoc queries, Spark for batch processing, Dremio for BI dashboards, all reading the same data

---

### Concept 2: Table Formats (Schema Evolution + ACID Transactions)

*Principle*: Manage data as versioned, schema-aware tables, not raw files.

Naive approach with raw Parquet files:

```
s3://security-logs/
  network-flows/date=2025-10-01/file1.parquet
  network-flows/date=2025-10-02/file2.parquet
```

The problems: no schema evolution (adding a new field requires rewriting all historical files), no ACID transactions (concurrent writes cause corruption), no time-travel (no way to query "data as of yesterday").

Table format approach (Iceberg/Delta) addresses all three via a metadata layer that tracks schema versions, file locations, and partitioning strategy; ACID transactions that allow multiple writers (a Spark batch job and a Trino analyst query) to coordinate safely; time-travel (`SELECT * FROM network_flows TIMESTAMP AS OF '2025-10-01 00:00:00'`); and schema evolution that adds fields without rewriting (backward compatible).

**Security Value**:
- **Safe schema changes**: OCSF schema evolves across minor releases (the current line is v1.8.0, released March 2026) without breaking existing queries
- **Multi-writer coordination**: Real-time ingestion (Kafka → Flink) + batch enrichment (Spark) write to same table safely
- **Compliance audit trail**: Time-travel enables "show me data as it existed on audit date"

> **Note on DuckLake (April 2026)**: DuckDB Labs shipped DuckLake v1.0 on April 13, 2026, an alternative catalog-and-format design that stores table metadata in a SQL database (DuckDB or any Postgres-compatible store) rather than in a file manifest, while the data files themselves remain Parquet and are compatible with Iceberg readers. The benchmark headline at v1.0 was roughly 100–900× faster streaming ingest than Iceberg's file-manifest approach on the DuckLake team's own tests, which is a significant gap if it holds at scale and across workloads. DuckLake is now shipping and worth tracking, though the SQL-metadata trade-off (metadata durability and multi-engine access depend on the backing database) is a real architectural difference from Iceberg's self-describing file manifests. For a security data lake, it is an emerging option rather than a settled choice; Iceberg and Delta Lake have years of production scale behind them. Watch DuckLake v1.x releases for independent validation of the performance claims before committing to it in a production architecture, since an initial independent reproduction now exists (a modest 2–4× streaming advantage on a single host rather than the headline 100–900×, with reads neutral on byte-identical Parquet), covered in Appendix I.

---

### Concept 3: Query Engines vs. Data Warehouses

*Principle*: Query engines process data wherever it lives, rather than requiring it to be loaded into a warehouse first.

Traditional warehouse approach:

```
Data Sources → ETL Pipeline → Data Warehouse (Snowflake/Redshift) → Query
```

Advantage: warehouse is optimized for BI workloads (fast aggregation). Limitation: data must be loaded first (ETL lag, vendor lock-in).

Query engine approach:

```
Data Sources (S3, databases, APIs) → Query Engine (Trino/Dremio) → Results
```

Advantage: query data in-place without loading (federated queries across heterogeneous sources). Limitation: performance depends on source optimization.

**Security Use Case** (federated threat hunting):
```sql
-- Query across Splunk, EDR database, and S3 data lake simultaneously
SELECT
    s.timestamp AS splunk_alert_time,
    e.process_name AS edr_process,
    n.dest_ip AS network_destination
FROM splunk.alerts s
JOIN edr_postgres.processes e
    ON s.host_id = e.host_id
JOIN s3_iceberg.network_flows n
    ON e.host_id = n.host_id
WHERE s.alert_name = 'Suspicious PowerShell'
  AND s.timestamp > NOW() - INTERVAL '24 hours'
```

Three sources (Splunk, PostgreSQL, S3) queried in a single SQL statement, with no data movement required.

---

### Concept 4: Batch vs. Streaming (Lambda vs. Kappa Architecture)

*Principle*: Process data as continuous streams (real-time) or scheduled batches.

Batch processing:
- **Pattern**: Accumulate data, process on schedule (hourly/daily)
- **Tools**: Apache Spark (batch jobs), dbt (SQL transformations), Airflow (orchestration)
- **Security use case**: Nightly OCSF normalization, threat intelligence enrichment

Stream processing:
- **Pattern**: Process events continuously as they arrive
- **Tools**: Apache Kafka (message broker), Apache Flink (stream processor), Spark Streaming
- **Security use case**: Real-time alerting (detect brute force within 5-minute window)

**Lambda Architecture** (dual pipelines):
```
              ┌──> Batch Layer (historical, accurate) ──┐
Data Sources  │                                         ├──> Merge Results
              └──> Speed Layer (real-time, approximate) ─┘
```

The problem with Lambda is maintaining two codebases (batch + streaming) for the same logic. This is nonetheless the security reality in many SOCs: a SIEM handles real-time detection while a data lake carries the historical query workload.

**Kappa Architecture** (stream-only):

A single stream processing pipeline reprocesses historical data by replaying the stream, which simplifies maintenance to one codebase, though the operational discipline to reprocess large histories on demand is a real cost.

---

### Concept 5: Dimensional Modeling (Star Schema) vs. Denormalization

*Principle*: Organize data for analytical queries.

Dimensional modeling (BI standard):
```
Fact Table: Sales               Dimension Tables:
- date_id (FK)                  - Customers (customer_id, name, region)
- customer_id (FK)              - Products (product_id, name, category)
- product_id (FK)               - Time (date_id, year, quarter, month)
- revenue
```
Efficient joins (foreign keys indexed) make aggregate queries fast.

Denormalization (log standard):
```json
{
  "timestamp": "2025-10-07T12:00:00Z",
  "src_endpoint": {
    "ip": "192.168.1.100",
    "hostname": "DESKTOP-001",
    "user": {"name": "jsmith", "department": "Engineering"}
  },
  "event_type": "authentication_failure"
}
```
No joins required, fast filtering on all fields.

Security logs arrive denormalized, but the normalization opportunity exists: extract entities (hosts, users, IPs) into dimension tables, and reduce storage by referencing entity_id instead of repeating full context. The trade-off is join complexity versus storage efficiency, and where your team lands on that depends on query patterns and operational maturity.

---

### Concept 6: ELT vs. ETL (Transform in Database vs. Pre-Transform)

ETL (Extract, Transform, Load):
- Transform data BEFORE loading into warehouse
- **Tools**: Airbyte, Fivetran, custom scripts
- **Benefit**: Load optimized data (smaller, pre-aggregated)
- **Limitation**: Can't re-transform without reprocessing source

ELT (Extract, Load, Transform):
- Load raw data, transform IN warehouse using SQL
- **Tools**: dbt (data build tool), Spark SQL
- **Benefit**: Flexibility (re-transform without reloading)
- **Limitation**: Storage cost for raw data

**Security Preference: ELT (load raw, transform later)**

The reason is unknown future use cases. Today you detect ransomware via process + file + network correlation. Tomorrow a new threat technique emerges that requires a field you've never analyzed before. If ETL discarded that field, you cannot retroactively hunt for the new threat. If ELT kept the raw data, you query the raw logs and build the new detection.

**OCSF Normalization Pattern** (ELT approach):
```
Raw Logs (S3)  →  Load to Iceberg (raw table)  →  dbt transforms to OCSF (normalized view)
                  ↓
              Keep raw + normalized (both queryable)
```

**A note on the parsing layer nobody owns**. Before you can normalize a field, someone has to extract it correctly, and that step is less reliable than you'd expect. In 2023, as a customer of Palo Alto (not an employee or vendor), I submitted [PR #294](https://github.com/PaloAltoNetworks/Splunk-Apps/pull/294) to Palo Alto's own Splunk app, fixing roughly 142 broken field extractions. The PAN-OS TRAFFIC and CONFIG logs are positional comma-separated records: one wrong field assignment cascades, and every field after it slides one position into the wrong column. Because it was a public PR, the fix would have shipped to every other customer of that app, not just my organization. It was never merged; the repository is now archived. Parsing is a layer nobody in the chain is paid to own, which means correctness here gets decided (or not) before any normalization framework touches the data. Chapter 3 gives the fuller first-hand account with a figure, and Appendix B catalogs the same failure mode as Anti-Pattern #12, "Mapping Wrong by Construction."

---

## D.4: Resource Quick Reference

The full resource directory lives in **Appendix E**, and the by-topic tool guides and community landscape are carried in full in **Appendix J**, with detailed learning paths, documentation links, community channels, and recommended reading orders by background. This section provides the essential starting points, so follow those pointers for everything deeper.

### Foundational Books

| Book | Author | Why It Matters for Security |
|------|--------|---------------------------|
| *Fundamentals of Data Engineering* | Joe Reis & Matt Housley (2022) | **Start here.** Chapters 6-10 cover storage, ingestion, queries, and orchestration, the foundation this book builds on |
| *Designing Data-Intensive Applications* | Martin Kleppmann (2017) | Deep dive into storage engines, batch/stream processing. Read after Reis. |
| *Apache Iceberg: The Definitive Guide* | Tomer Shiran, Jason Hughes & Alex Merced (O'Reilly, 2024) | Table format most security architectures will use. Multi-engine support, schema evolution. |

### Key Technologies at a Glance

| Category | Recommended Start | Security Use Case | Deep Dive |
|----------|-------------------|-------------------|-----------|
| **Table Format** | Apache Iceberg | Multi-engine queries, schema evolution, vendor-neutral | Appendix C, Appendix J |
| **Query Engines** | Trino (federated), StarRocks (real-time) | Threat hunting, SOC dashboards | Appendix I, Appendix J |
| **Catalog** | Polaris (Iceberg-native) | Metadata governance across engines | Appendix C, Appendix J |
| **Transformation** | dbt | OCSF normalization, SQL-based | Appendix H, Appendix J |
| **Orchestration** | Airflow or Dagster | Batch jobs: compaction, enrichment, threat intel refresh | Appendix J |
| **Streaming** | Kafka + Flink (if <30s required) | Real-time detection pipelines | Appendix I, Appendix J |

### Communities to Join First

- **dbt Slack** (tens of thousands of members) frames security problems in data engineering vocabulary
- **Apache Iceberg Slack** covers table format questions and production patterns
- **OCSF Slack** covers schema mapping and vendor adoption discussions
- **r/dataengineering** (Reddit) carries daily questions and practitioner experiences

For detailed documentation links, thought leaders, conferences, learning paths, and reading orders by experience level, see **Appendix J: Resources and Community**.

---

## D.5: Architecture Decision Overview

After building vocabulary, you face concrete decisions: which table format, which catalog, which transformation tools? These decisions determine whether your security data architecture locks you into vendors, whether you can enforce governance at scale, and whether your transformation logic survives schema changes. The data engineering community validated these patterns across petabyte-scale deployments; security teams now adapt them.

**Three Critical Architecture Decisions**:

1. **Table Format (Iceberg vs. Delta Lake)**: Determines query engine flexibility, metadata scalability, vendor lock-in risk, CDC maturity. Most security teams: **Apache Iceberg** (vendor-neutral, multi-engine support) unless Databricks-committed (then Delta Lake).

2. **Catalog Selection (Unity, Polaris, Nessie, Gravitino)**: Your governance enforcement point, determining row-level security capability, rollback options, and catalog federation. Greenfield security teams: **Polaris** (vendor-neutral, table-level security) unless you need fine-grained access (Unity) or Git workflows (Nessie) or managing multiple catalog types (Gravitino).

3. **Transformation Tools (dbt for Security)**: SQL transformations for OCSF normalization, enrichment, detection rules. Security teams standardize on **dbt** (SQL-based, testing framework, version control, documentation auto-generation).

**Detailed Decision Frameworks**: **Appendix E** indexes the table-format and catalog documentation behind the Iceberg-versus-Delta and Polaris-versus-Unity-versus-Nessie choices, **Appendix I** works through query-engine selection and complements the catalog choices rather than covering them, and **Appendix H** covers OCSF normalization with dbt, while **Appendix C** shows the five reference architectures those choices compose into.

**Cross-References**:
- **The what-good-looks-like material** (the variants chapter, Chapter 6 of the handbook): worked examples applying these decision frameworks across the MOAR variants, with the incremental-modernization decisions carried in the modularity chapter (Chapter 7)
- **Appendix H**: OCSF normalization with dbt (detailed implementation)
- **Appendix I**: Query engine selection (complements table format + catalog choices)
- **Appendix C**: Reference architectures (Iceberg + Polaris in MOAR architecture)

---

## D.6: Engaging the Data Engineering Community

Security architects who speak both languages can use mature tooling, proven design patterns, and operational experience at petabyte scale. Data engineers, in return, get high-cardinality workload challenges, real-time plus historical dual requirements, and schema-on-read use cases they don't encounter in typical BI contexts, so the trade runs both directions rather than one discipline lending to the other.

**Practical engagement**:

1. **Attend Data Conferences**: Subsurface (Dremio, fall), Trino Summit (September), Data + AI Summit (June), and ask data engineers "How do you handle high-cardinality filtering?" and "What's your approach to 7-year retention with tiered storage?"

2. **Join Online Communities**: the four listed in D.4, plus Trino Slack, framing security problems in data engineering vocabulary (the translation tables in D.7 give you the words)

3. **Follow Thought Leaders**: Joe Reis (LinkedIn + newsletter), Alex Merced (YouTube tutorials), Ryan Blue (Iceberg roadmap), and comment thoughtfully to build relationships

4. **Experiment Hands-On**: DuckDB (duckdb.org), AWS Athena Free Tier, Iceberg Docker (github.com/databricks/iceberg-rest-image, where the old tabular-io path redirects since Databricks acquired Tabular; verified live 2026-07-10), since breaking things teaches more than documentation

---

## D.7: The Full Bidirectional Glossary

### Alphabetical Index (Security → Data Engineering)

---

### Core Concepts

#### Alert / Detection Rule
**Security Term**: Alert, detection rule, correlation search, analytic
**Data Engineering Equivalent**: Scheduled query, materialized view, stream processing job
**Context**:
- **Batch alerting** = Scheduled query (Airflow DAG runs query every 5 minutes, alerts if threshold exceeded)
- **Real-time alerting** = Stream processing (Flink/Spark Streaming processes events continuously, emits alert on match)
**Why It Matters**: Data engineers don't say "alert"; they say "query output exceeds threshold" or "stream processor emits event"

---

#### Archive / Cold Storage
**Security Term**: Archive, offline storage, long-term retention
**Data Engineering Equivalent**: Cold tier, Glacier storage, archived partitions
**Context**:
- **Security expectation**: "Archived data is queryable" (compliance requirement: 7-year retention)
- **Data engineering reality**: "Archived = Glacier/cold tier, queryable but slow (minutes vs. seconds)"
- **SIEM anti-pattern**: "Archived to tape = NOT queryable" (Splunk archives to offline S3, cannot query via SPL)
**Why It Matters**: When data engineer says "archived," clarify "queryable cold tier" vs. "offline backup"

---

#### Correlation / Join
**Security Term**: Correlation, event correlation, multi-source analysis
**Data Engineering Equivalent**: SQL JOIN, stream-stream join, windowed join
**Context**:
- **Security use case**: "Correlate process creation (EDR) with network connection (Zeek) by host_id and timestamp window"
- **Data engineering translation**: `SELECT * FROM edr_processes p JOIN network_flows n ON p.host_id = n.host_id WHERE p.timestamp BETWEEN n.timestamp - INTERVAL '5 minutes' AND n.timestamp`
**Why It Matters**: Data engineers use standard SQL JOINs, with no special "correlation" language (except in proprietary SIEM query languages such as SPL, KQL, and AQL)

---

#### Dashboard / Visualization
**Security Term**: Dashboard, security posture view, SOC metrics
**Data Engineering Equivalent**: BI dashboard, report, aggregated view, materialized view
**Context**:
- **Real-time dashboard** = Materialized view (Dremio Reflections pre-compute aggregations for <1 sec refresh)
- **Ad-hoc dashboard** = Query-time aggregation (Tableau queries Trino on-demand, 5-30 sec latency)
**Why It Matters**: Data engineers optimize dashboards via caching (Reflections, materialized views), not by making queries "go faster"

---

#### Materialized Views / Pre-Computed Results
**Security Term**: Data Model Acceleration (Splunk), accelerated summary (SIEM-specific)
**Data Engineering Equivalent**: Materialized view, query results cache, aggregation table, Dremio Reflections
**Context**:
- **Security expectation**: "Pre-compute dashboard queries for instant refresh"
- **Data engineering reality**: "Materialized views can provide dramatic speedups: Snowflake reports roughly a 78% query improvement (a percentage, not a multiplier), a single-developer PostgreSQL case study reports 350×–9,000× (Sid Ngeth, 2025, synthetic Rails dataset), and a practitioner Splunk write-up reports ~270×, but these are best-case figures; security data frequently hits the failure modes below." Evidence tier C/D, not independently reproduced (units and attribution corrected 2026-07-10); see Appendix I.4B for the conditions under which these figures hold.
- **Three failure modes**:
  1. **High data change rates** (continuous log ingestion) → refresh costs exceed query savings
  2. **Schema volatility** (new log sources, vendor updates) → views invalidated frequently
  3. **Complex queries** (5-table joins, MEDIAN/PERCENTILE) → force full refresh, no incremental benefit
**Decision Framework (from Appendix I.4B)**:
- **Deploy when**: Query frequency >> data change rate (12:1 ratio), refresh cost < query cost savings (10× benefit), schema stable (<1 change/month), simple aggregations only
- **Avoid when**: Unpredictable query patterns (threat hunting), complex correlation rules (window functions), schema changes weekly, insufficient operational expertise
**Why It Matters**: Data engineers say "let's materialize this" when they see repeated queries, so security architects must evaluate whether the benefits outweigh the operational complexity for security workloads

---

#### Detection Engineering / Rule Development
**Security Term**: Detection engineering, writing detection rules, building analytics
**Data Engineering Equivalent**: Query development, ETL pipeline design, data modeling
**Context**:
- **Security focus**: "Does this rule detect lateral movement?"
- **Data engineering focus**: "Does this query scan minimal data?" (performance + cost optimization)
- **Overlap**: Both care about false positives (security) = wasted compute (data engineering)
**Why It Matters**: Data engineers prioritize query efficiency; security prioritizes detection accuracy, so the two sides need to collaborate on both

---

#### Enrichment / Contextualization
**Security Term**: Enrichment (add threat intel, GeoIP, asset inventory context)
**Data Engineering Equivalent**: Data enrichment, dimension table joins, lookup tables
**Context**:
- **Security pattern**: "Enrich IP address with GeoIP country code + threat intel reputation score"
- **Data engineering pattern**: `SELECT e.*, g.country, t.reputation FROM events e LEFT JOIN geoip g ON e.src_ip = g.ip LEFT JOIN threat_intel t ON e.src_ip = t.ip`
**Why It Matters**: Data engineers use standard JOINs for enrichment, not "enrichment frameworks," which is simpler than it sounds

---

#### Event / Log Entry
**Security Term**: Event, log entry, telemetry record
**Data Engineering Equivalent**: Row, record, event (same term)
**Context**:
- **Security**: "Process execution event from EDR"
- **Data engineering**: "Row in `edr_processes` table"
- **No translation needed**: Both disciplines use "event" interchangeably
**Why It Matters**: one of the few terms with a 1:1 mapping, so there's no confusion

---

#### Hot Data / Recent Data
**Security Term**: Hot data, recent logs, actively queried data
**Data Engineering Equivalent**: Hot tier, S3 Standard, frequently accessed partition
**Context**:
- **Security pattern**: "Last 7 days queried 100× per day (hot), older data queried 2× per week (cold)"
- **Data engineering solution**: S3 Standard (hot, $0.023/GB/month) for 7 days, transition to S3 Glacier Deep Archive (~$0.001/GB/month; tier named 2026-07-10 for consistency with A.6, which prices Glacier Flexible Retrieval separately at $0.0036) for older data
**Why It Matters**: Data engineers design tiered storage based on access patterns, so tell them your query frequency to optimize cost

---

#### Indicator of Compromise (IOC) / Threat Intelligence
**Security Term**: IOC, indicator, threat intel feed, reputation data
**Data Engineering Equivalent**: Reference data, lookup table, dimension table
**Context**:
- **Security**: "Check if IP matches IOC list (10M malicious IPs)"
- **Data engineering**: "JOIN events ON threat_intel_lookup WHERE ip IN (SELECT ip FROM ioc_table)"
- **Optimization**: Broadcast join for small IOC lists (threshold varies by engine: Spark default ~10MB, configurable higher; Trino and DuckDB handle larger in-memory sets but depend on cluster RAM), partition pruning (date-based IOC refresh)
**Why It Matters**: IOC lookups = standard database JOINs, which data engineers optimize via indexing, partitioning, and caching

---

#### Incremental View Maintenance (IVM)
**Security Term**: N/A (new concept from data engineering)
**Data Engineering Equivalent**: IVM, incremental refresh, delta processing
**Context**:
- **Full refresh**: Recompute entire materialized view from scratch (expensive for large tables)
- **Incremental refresh**: Process only changed data since last refresh (efficient for append-only logs)
- **Security challenge**: Complex correlation rules (5-table joins, window functions, PERCENTILE) often force full refresh despite incremental capabilities
**Why It Matters**: When data engineer says "this view supports incremental refresh," ask "What if all joined tables change simultaneously?" (Answer often: "Falls back to full refresh")

---

#### Ingestion / Collection
**Security Term**: Log collection, telemetry ingestion, data forwarding
**Data Engineering Equivalent**: Data ingestion, ETL, data pipeline
**Context**:
- **Security tools**: Splunk Universal Forwarder, Filebeat, Logstash
- **Data engineering tools**: Fivetran, Airbyte, Kafka, AWS Kinesis
- **Overlap**: Both move data from source to destination, though data engineering tools are often cheaper and more scalable
**Why It Matters**: Data engineers say "ETL" or "ingestion pipeline," not "log forwarding"

---

#### Modular Open Architecture (MOAR)
**Security Term**: Next-gen SIEM architecture, security data lake, lakehouse for security
**Data Engineering Equivalent**: Composable data platform, lakehouse architecture, modular data stack
**Context**:
- **Definition**: Architectural philosophy for cybersecurity data: composable, vendor-neutral components selected based on organizational constraints rather than vendor bundling
- **Five design principles**: a vendor-neutral data layer, separation of storage and compute, compression-first design, schema evolution without breaking changes, and query engine specialization
- **Component model (L-I-G-E-R)**: Lakehouse (Iceberg/Delta) + Index (Polaris/Unity) + Graph (Grafana) + Engine (StarRocks/ClickHouse/Trino/DuckDB) + Route (Cribl/Tenzir/Kafka). Note: this book uses MOAR (Modular Open Architecture) for the architecture itself, and LIGER (L-I-G-E-R) for the specific five-layer reference composition the lab builds and tests, one instance of MOAR rather than a synonym for it.
- **Graph (the G) is usually a passthrough** rather than a build decision: the shop almost always already has somewhere its analysts work (Grafana, Superset, a custom hunt UI, or the incumbent SOC consoles such as Splunk, Elastic, or Sentinel, kept for federated read during a transition) and whatever sits on top inherits the trust, connection, and performance properties from the layers underneath rather than creating them, so the book stays exhaustive about the infrastructure below the analytic and deliberately not about the analytic itself. That's also why the lab ships no swap verb for Graph: it's a passthrough, not a component the lab swaps and answer-equality-checks.
- **Index (the catalog layer) is a scale-and-governance bet**: at single-node SOC scale it earns its place less from query performance (the engines answer sub-second whether or not a separate catalog is brokering metadata) and more from governance, lineage, and letting several engines read the same tables without stepping on each other, so its weight in the decision rises with scale and with the number of engines sharing the lake rather than being needed on day one in every deployment.
- **Contrast with SIEM**: SIEM bundles all capabilities in one platform; MOAR separates concerns into interchangeable layers
**Why It Matters**: MOAR is the organizing framework of this book, and understanding it bridges security architects ("I need detection and response") with data engineers ("I need composable, open-format storage and compute")
**See**: About This Book (definition), Appendix C (reference architectures), and the manageability-over-extreme-performance material that opens the handbook (Chapter 1) for the opportunity framing

---

#### Normalization / Schema Standardization
**Security Term**: Log normalization, schema standardization, CIM/OCSF mapping
**Data Engineering Equivalent**: Data modeling, schema transformation, ETL transformation
**Context**:
- **Security pattern**: "Normalize CrowdStrike EDR (vendor schema) to OCSF Process Activity (standard schema)"
- **Data engineering pattern**: "Transform source schema to target schema via dbt models or Spark SQL"
- **Tool**: dbt (data build tool) = preferred data engineering approach for transformations
**Why It Matters**: Data engineers use dbt for schema transformations, so OCSF mapping fits naturally into the dbt workflow

---

#### Ontology / Reasoner / Entailment
**Security Term**: Ontology (D3FEND), knowledge graph, semantic model
**Data Engineering Equivalent**: A schema with typed relationships plus machine-checkable constraints (the closest everyday analogue: a data model whose keys and types a checker can actually verify)
**Context**:
- **Ontology** = a schema that also states what things *are* and how classes relate (a subclass tree a machine can walk), so a defense watching a general class provably covers the specific kinds beneath it
- **Reasoner** (e.g., ELK) = the program that computes what the ontology's claims imply and reports contradictions; the "does this even compile" check for a knowledge model
- **Entailment** = a connection the reasoner infers rather than one a human wrote (Chapter 4's D3FEND join runs on these)
**Why It Matters**: The payoff is fail-loud semantics: a wrong change to the model gets refused by the reasoner before it ships (Appendix H.5.7 walks a real case) instead of surfacing months later as silently wrong query results

---

#### Parsing / Field Extraction
**Security Term**: Parsing, field extraction, log parsing
**Data Engineering Equivalent**: Schema-on-read, JSON parsing, CSV parsing, regex extraction
**Context**:
- **Security**: "Parse Windows event log XML to extract event_id, user, timestamp"
- **Data engineering**: `SELECT json_extract(raw_log, '$.event_id') AS event_id FROM logs` (schema-on-read)
- **Optimization**: Parse once at ingestion (schema-on-write) vs. parse every query (schema-on-read)
**Why It Matters**: Data engineers prefer schema-on-write (parse once, store typed columns) for query performance

---

#### Partition / Time Window
**Security Term**: Time window, date range, recent data
**Data Engineering Equivalent**: Partition, partition key, partition pruning
**Context**:
- **Security query**: "Show me failed logins in last 7 days"
- **Data engineering optimization**: Partition table by `event_date` (Iceberg hidden partition) → Query scans 7 partitions, not 7-year table
- **Performance gain**: roughly 10-100× faster queries via partition pruning (order-of-magnitude rule of thumb, depends on partition selectivity and data layout)
**Why It Matters**: Tell data engineers your query patterns ("95% of queries filter by date") → they partition by date → queries often 10-100× faster

---

#### Query / Search
**Security Term**: Search, hunt, investigate, query
**Data Engineering Equivalent**: Query, SELECT statement, analytics query
**Context**:
- **Security**: "Search for IOC across 90 days of data"
- **Data engineering**: "Run ad-hoc query on 90-day partition"
- **Performance concern**: Full-table scan (security: "search everything") vs. partition pruning (data engineering: "search only relevant partitions")
**Why It Matters**: Data engineers optimize queries via partitioning, indexing, columnar storage, so help them by specifying filters ("always filter by date")

---

#### Retention / Data Lifecycle
**Security Term**: Retention, data retention policy, log storage duration
**Data Engineering Equivalent**: Lifecycle policy, data retention, TTL (time-to-live)
**Context**:
- **Security requirement**: "7-year retention for compliance"
- **Data engineering solution**: S3 lifecycle policy (90-day Standard → Glacier transition), Iceberg snapshot retention
**Why It Matters**: Data engineers automate retention via lifecycle policies, so specify queryable versus archival retention

---

#### SIEM / Data Lake
**Security Term**: SIEM (Security Information and Event Management)
**Data Engineering Equivalent**: Data lake, lakehouse, data platform
**Context**:
- **SIEM = Proprietary data lake**: Splunk (tsidx storage + SPL query) = specialized data lake for security
- **Modern approach**: Open data lake (Iceberg on S3) + query engine (Trino/Dremio) = SIEM-equivalent at a modeled 32-91% lower cost, depending on volume and on which SIEM baseline you price against. Worksheet A.6 models the saving at 36-42% at 500 GB/day and 90-91% at 10 TB/day against the full-stack schema-on-read SIEM row, while 32% is the conservative floor from its Step 6 worked example, which prices MOAR against a platform-license-only SIEM at 2 TB/day (see Appendix A.6 for the full cost model, whose figures are computed from published rates rather than taken from measured invoices)
**Why It Matters**: SIEMs are data lakes with security-specific features, so data engineers can build the equivalent using open-source tools

---

#### Source / Data Source
**Security Term**: Log source, telemetry source, security data source
**Data Engineering Equivalent**: Data source, upstream system, producer
**Context**:
- **Security**: "40 log sources (EDR, cloud, network, SaaS)"
- **Data engineering**: "40 upstream producers writing to data lake"
**Why It Matters**: no translation is needed, since both disciplines use "data source" identically

---

#### Threat Hunting / Exploratory Analysis
**Security Term**: Threat hunting, proactive investigation, hypothesis-driven analysis
**Data Engineering Equivalent**: Exploratory data analysis (EDA), ad-hoc queries, data discovery
**Context**:
- **Security threat hunting**: "Hunt for lateral movement patterns (SMB connections between internal hosts)"
- **Data engineering EDA**: "Explore network_flows table for connection patterns WHERE src_ip LIKE '10.%' AND dest_ip LIKE '10.%'"
- **Tooling**: Jupyter notebooks (data science), SQL workbenches (data engineering), Splunk (security)
**Why It Matters**: Data engineers optimize for ad-hoc query performance (Trino/Dremio excel at this), so threat hunting fits naturally

---

### Architecture Patterns Translation

#### Lambda Architecture (Batch + Stream)
**Security Context**: Dual-platform strategy
- **Speed layer** = Real-time SIEM (Splunk, Sentinel) for sub-30-second alerting
- **Batch layer** = Historical data lake (Iceberg, Athena) for 90-day threat hunting
**Data Engineering Context**: Dual processing pipelines (real-time + batch) for same logic
**Why It Matters**: Many SOCs use Lambda architecture without knowing the term, though data engineers recognize the pattern

---

#### Medallion Architecture (Bronze → Silver → Gold)
**Security Context**: Data maturity pipeline
- **Bronze** = Raw logs (untransformed, source schema)
- **Silver** = Cleaned logs (parsed fields, typed columns, deduplicated)
- **Gold** = OCSF-normalized (standardized schema, enriched with threat intel)
**Data Engineering Context**: Databricks pattern for data quality layers
**Why It Matters**: When data engineers say "let's build medallion architecture," they mean "raw → cleaned → normalized"

---

#### Star Schema / Dimensional Model
**Security Context**: Fact table + dimension tables
- **Fact table** = Events (process executions, network connections; high cardinality, billions of rows)
- **Dimension tables** = Entities (hosts, users, IPs; low cardinality, thousands of rows)
**Data Engineering Context**: Ralph Kimball dimensional modeling (data warehousing standard)
**Why It Matters**: Data engineers suggest star schema for dashboard queries (fast aggregations via dimension joins)

---

### Technology Translation Table

| Security Technology | Data Engineering Equivalent | Why Translation Matters |
|---------------------|----------------------------|-------------------------|
| **Splunk** | Proprietary data lake + query engine | Splunk = tsidx storage + SPL = specialized lakehouse |
| **Elasticsearch** | Document store + inverted index | Elasticsearch = JSON storage + search engine, not optimized for columnar analytics |
| **Logstash** | ETL pipeline / data ingestion tool | Logstash = Ruby-based ETL; data engineers commonly reach for Kafka, Airbyte, dbt, or Spark depending on the pattern, with Fivetran as one option, not the default |
| **Kibana** | BI dashboard tool | Kibana = Elasticsearch-specific, data engineers use Tableau/Grafana/QuickSight |
| **Sysmon** | Data source / telemetry producer | Sysmon = Windows endpoint monitoring (data source, not processing tool) |
| **Zeek** | Data source / telemetry producer | Zeek = Network monitoring (produces logs, not SIEM) |
| **SOAR** | Orchestration / workflow automation | SOAR = Security-specific Airflow (data engineers: "workflow orchestration") |
| **Threat Intel Platform** | Reference data / lookup service | Threat intel = Dimension table (JOIN for enrichment) |

---

### Data Engineering → Security Translation

For data engineers reading this book, here are security terms translated into data engineering concepts:

#### EDR (Endpoint Detection and Response)
**Data Engineering Translation**: Host-level telemetry source producing process, file, network, registry events
**Context**: EDR = Rich data source (roughly 5-20 GB/day per 1,000 endpoints in the deployments I've seen; varies widely by EDR vendor and telemetry verbosity), high cardinality (billions of rows)
**Query pattern**: "Show me process creation events WHERE process_name = 'powershell.exe'" = High-cardinality filter, benefits from columnar storage

---

#### MITRE ATT&CK
**Data Engineering Translation**: Taxonomy/classification system (like product categories in e-commerce)
**Context**: ATT&CK = Framework mapping adversary behaviors to detection rules
**Usage**: Detection rules tagged with ATT&CK IDs (T1055 = Process Injection) for coverage analysis
**Data modeling**: Add `attack_technique_id` column to detection_rules table (dimension for aggregation)

---

#### OCSF (Open Cybersecurity Schema Framework)
**Data Engineering Translation**: Industry-standard schema (like Parquet format for security data)
**Context**: OCSF = Target schema for security log normalization, vendor-agnostic; current release v1.8.0 (March 2026)
**Benefit**: Analogous to Apache Iceberg table format, enabling multi-tool compatibility without vendor lock-in

---

#### SOC (Security Operations Center)
**Data Engineering Translation**: Data analysis team (like data science team or BI team)
**Context**: SOC analysts = Data consumers who run queries, build dashboards, investigate anomalies
**Query patterns**: Ad-hoc (threat hunting), scheduled (detection rules), dashboard (metrics)

---

### Phrase Translation

#### Security Phrase → Data Engineering Translation

| Security Says | Data Engineering Hears | Bridge Communication |
|---------------|----------------------|---------------------|
| "Correlate events across sources" | "JOIN tables on common keys" | "We need to JOIN EDR, network, and cloud logs on host_id and timestamp window" |
| "Search for IOC across 90 days" | "Ad-hoc query with date partition filter" | "We need interactive query performance on 90-day partitions" |
| "Real-time alerting <30 seconds" | "Stream processing with sub-minute latency" | "We need Kafka + Flink/Spark Streaming for real-time" |
| "7-year compliance retention" | "Tiered storage with lifecycle policies" | "We need hot tier (90 days) + cold tier (7 years), both queryable" |
| "Enrich with threat intel" | "LEFT JOIN with reference table" | "We need to JOIN events with threat_intel dimension table on IP address" |
| "Normalize to OCSF" | "Transform source schema to target schema" | "We need dbt models to map vendor schemas to OCSF" |
| "Threat hunting" | "Exploratory data analysis (EDA)" | "We need ad-hoc query engine (Trino/Dremio) for interactive investigation" |
| "Detection rule" | "Scheduled query + alerting threshold" | "We need Airflow DAG running SQL query every 5 minutes, alert if count > threshold" |

---

#### Data Engineering Phrase → Security Translation

| Data Engineering Says | Security Hears | Bridge Communication |
|---------------------|----------------|---------------------|
| "Partition pruning" | "Faster queries" | "Partitioning by date makes your threat hunts roughly 10-100× faster, depending on selectivity" |
| "Columnar storage" | "Optimized for filtering" | "Parquet format makes 'WHERE process_name = X' queries fast on billions of rows" |
| "Schema-on-read" | "Parse at query time" | "We can store raw JSON, parse fields when you query (flexible but slower)" |
| "Materialized view" | "Pre-computed dashboard" | "We pre-compute your dashboard aggregations for <1 sec refresh" |
| "Broadcast join" | "Fast lookups" | "We load your 10M IOC list into memory for instant threat intel enrichment" |
| "Data skew" | "Slow queries" | "Some hosts generate 1000× more events → queries slow on those partitions" |
| "Compaction" | "Maintenance" | "We merge small files into large files so your queries run faster" |
| "Time-travel" | "Historical snapshots" | "You can query data 'as of October 1' for compliance audits" |

---

### Common Misunderstandings

#### Collaboration Gap #1: Security architects and data engineers often talk past each other on requirements

**What security architects often assume**: Data engineers need to be taught what security requires before they can help.

**How data engineers think about it**: They understand query patterns, access patterns, and performance requirements immediately, so the translation problem is one of vocabulary, not concept. Frame security needs in data engineering terms and the conversation changes:
- Unclear: "We need correlation capability"
- Actionable: "We need multi-table JOINs with <60 second latency on billions of rows"

---

#### Collaboration Gap #2: SIEMs occupy a category of their own, separate from data infrastructure

**What security architects often assume**: SIEM capabilities are too specialized to replicate with general-purpose data engineering tools.

**How data engineers think about it**: SIEMs are specialized data lakes, and the features are real, though they're not magic. For most SOC workflows, a MOAR stack covers most of the structured-analytics ground, with named gaps (streaming subsearch, the transaction model) that decide specific shops [*qualifier: this book's assessment based on production architecture patterns; no independent third-party study has benchmarked this coverage claim specifically*]:
- **SPL core detection queries** largely translate to standard SQL (GROUP BY, window functions, time-bucketing), but SPL's streaming subsearch and transaction model have no direct SQL equivalent and require workarounds in stream processors such as Flink
- **Real-time alerting** = Stream processing (Kafka + Flink = proven at scale)
- **Investigation workflow** = SQL workbench + Jupyter notebooks (familiar to data engineers)

---

#### Collaboration Gap #3: Data engineering teams treat security as someone else's concern

**What security architects often assume**: Data engineers will deprioritize access control and audit requirements unless pushed.

**How data engineers think about it**: They care deeply about access control, audit logging, and compliance, just under different terminology:
- Security: "Row-level security" → Data engineering: "Predicate pushdown filtering by user role"
- Security: "Audit trail" → Data engineering: "Query logs, access logs, change tracking"
- Security: "Data sovereignty" → Data engineering: "Regional data residency, partition by geography"

---

### Glossary Usage Examples

#### Example 1: Requesting Dashboard Optimization

**Security Ask (unclear)**:
> "Our SOC dashboard is slow. Can you make it faster?"

**Data Engineering Response**:
> "What's slow mean? 5 seconds? 30 seconds? What queries power the dashboard?"

**Improved Ask (using glossary)**:
> "Our SOC dashboard queries 30-day aggregations (COUNT, GROUP BY source_ip) and takes 30 seconds to refresh. We need <5 second refresh for real-time monitoring. Can we use materialized views or query caching?"

**Result**: Data engineer understands problem (30s → <5s) and solution space (Dremio Reflections, ClickHouse materialized views)

---

#### Example 2: Explaining Threat Hunting Workload

**Security Ask (unclear)**:
> "We need threat hunting capability."

**Data Engineering Response**:
> "What's threat hunting? How often? How much data?"

**Improved Ask (using glossary)**:
> "Threat hunting = ad-hoc exploratory queries on 90-day partitions, 5-10 queries per day per analyst (10 analysts = 50-100 queries/day). Query patterns: Filter by host_id, process_name, timestamp (high-cardinality fields). Need <60 second latency for interactive investigation."

**Result**: Data engineer selects Trino (optimized for ad-hoc, high-cardinality filtering) vs. Dremio (optimized for dashboards)

---

#### Example 3: Communicating Retention Requirements

**Security Ask (unclear)**:
> "We need 7-year retention for compliance."

**Data Engineering Response**:
> "7 years in what tier? Hot? Warm? Cold? Queryable or archive-only?"

**Improved Ask (using glossary)**:
> "We need 7-year queryable retention. Access pattern: 90% of queries target last 90 days (hot tier, <10 sec latency required). 10% of queries target 90 days to 7 years (cold tier, <5 minute latency acceptable). Compliance requires all 7 years queryable, not offline archive."

**Result**: Data engineer designs S3 Standard (90-day hot) + S3 Glacier (7-year cold) with Iceberg time-travel for compliance

---

This appendix provides:
- **Opening narrative**: The translation challenge in context (a composite security architect at Data + AI Summit)
- **Bidirectional translation**: Security ↔ Data Engineering terminology
- **Context notes**: When/why the translation matters
- **Phrase translation table**: Common communication patterns
- **Misunderstanding clarification**: Bridge discipline gaps
- **Usage examples**: How to apply glossary in real conversations

**Next**: Appendix E (Consolidated Resource Directory) and Appendix J (Resources and Community) carry the learning resources in full.

---

## D.8: Endnotes and Sources

**Evidence Quality**: A/B-Level for terminology and architecture claims, though individual vendor-benchmark figures are tagged C/D inline where they are cited (data engineering resources + practitioner validation)

**Data Engineering Resources Cited**:
- Joe Reis & Matt Housley: "Fundamentals of Data Engineering" (O'Reilly, 2022)
- Martin Kleppmann: "Designing Data-Intensive Applications" (O'Reilly, 2017)
- Official documentation: Apache Iceberg, Trino, Delta Lake, dbt

**Practitioner Validation**:
- A data-platform practitioner [Personal communication, October 2025]: Hybrid architecture necessity, Starburst/Athena connection, Denodo multi-cloud virtualization
- Lisa Cao (Datastrato): Gravitino meta-catalog expertise, catalog proliferation management [Personal communication, 2025; Gravitino architecture: gravitino.apache.org/docs]
