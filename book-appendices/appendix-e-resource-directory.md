---
type: reference
title: "Appendix E: Consolidated Resource Directory"
created: 2025-10-15
tags: [moar-book, resource-directory, learning-paths, ocsf, iceberg]
---

# Appendix E: Consolidated Resource Directory

**Purpose**: Curated list of learning resources for building MOAR security data architectures. Compiled from the translation and navigation material (now Appendices D and J) with organization by topic.

**How to use**: Start with your learning goal (e.g., "Learn Apache Iceberg") → Find topic section → Follow recommended path (docs → blog posts → videos → community). External URLs spot-checked October 2025.

**Boundary with Appendix J**: This directory tells you where to learn each technology — books, documentation links, and week-by-week learning paths. The tool-by-tool implementation guides (when to use Flink versus Spark Structured Streaming, code patterns, the new-tool evaluation framework) are Appendix J Sections J.1–J.8, and the community landscape is J.9–J.17. Where the same tool appears in both, this appendix carries the learning path and J carries the implementation judgment.

---

## Quick Navigation

**Foundations**:
- [Books](#books) | [Data Engineering Fundamentals](#data-engineering-fundamentals) | [Security Data Architecture](#security-data-architecture)

**Technologies**:
- [Table Formats](#table-formats-iceberg-delta-hudi) | [Query Engines](#query-engines-trino-dremio-spark-athena) | [Catalogs](#data-catalogs-polaris-unity-nessie) | [Stream Processing](#stream-processing-kafka-flink) | [Orchestration](#orchestration-airflow-dagster-prefect)

**Standards & Frameworks**:
- [OCSF](#ocsf-open-cybersecurity-schema-framework) | [MITRE ATT&CK](#mitre-attck) | [D3FEND](#d3fend) | [NIST](#nist-cybersecurity-framework)

**Communities**:
- [Slack Channels](#slack-communities) | [Conferences](#conferences) | [Thought Leaders](#thought-leaders-to-follow) | [Blogs & Newsletters](#blogs--newsletters)

**Companion**:
- [Companion Essays](#companion-essays-security-data-works) — Chapter-to-post mapping for further reading

---

## Books

### Data Engineering Fundamentals

**"Fundamentals of Data Engineering" by Joe Reis & Matt Housley** (O'Reilly, 2022)
- **Why Essential**: The standard reference for data engineering principles
- **Security-Relevant Chapters**:
  - Chapter 6: Data Generation (storage patterns, object storage, separation of compute/storage)
  - Chapter 7: Storage (data lakes, lakehouses, table formats) <!-- lint-ignore-xref -->
  - Chapter 8: Ingestion (batch vs. streaming, change data capture) <!-- lint-ignore-xref -->
  - Chapter 9: Data Modeling (dimensional modeling, normalization) <!-- lint-ignore-xref -->
  - Chapter 10: Orchestration (Airflow, workflow management) <!-- lint-ignore-xref -->
- **Reading Path**: Read Chapters 6-10 for security data architecture foundations
- **Where to Buy**: oreilly.com, Amazon
- **Companion Resources**: Joe Reis blog (joereis.substack.com), Data Engineering Weekly newsletter

---

**"Designing Data-Intensive Applications" by Martin Kleppmann** (O'Reilly, 2017)
- **Why Essential**: Deep dive into distributed systems, databases, data processing
- **Security-Relevant Chapters**:
  - Chapter 4: Storage Engines (LSM-trees vs. B-trees—understand Elasticsearch, ClickHouse internals)
  - Chapter 6: Replication (high availability for SIEM replacement)
  - Chapter 11: Batch Processing (Spark, MapReduce for security data transformations) <!-- lint-ignore-xref -->
  - Chapter 12: Stream Processing (Kafka, Flink for real-time detection) <!-- lint-ignore-xref -->
- **Reading Path**: Focus on Chapters 4, 10, 11 for security context
- **Where to Buy**: oreilly.com, Amazon
- **Difficulty**: Advanced (assumes distributed systems knowledge)

---

**"Delta Lake: The Definitive Guide" by Denny Lee, Tathagata Das, et al.** (O'Reilly, 2024)
- **Why Relevant**: If considering Delta Lake table format (Databricks-centric architecture)
- **Security-Relevant Topics**:
  - Chapter 2: Delta Lake architecture (ACID transactions, time-travel)
  - Chapter 5: Schema evolution (OCSF v1.3 → v1.4 migrations)
  - Chapter 7: Streaming with Delta (real-time ingestion patterns) <!-- lint-ignore-xref -->
- **Alternative**: If choosing Iceberg (multi-engine), prioritize Iceberg docs over this book
- **Where to Buy**: oreilly.com, databricks.com/resources

---

**"The Data Warehouse Toolkit" by Ralph Kimball** (Wiley, 2013)
- **Why Relevant**: Dimensional modeling (star schema) for dashboard queries
- **Security Application**: Fact table = security events, dimension tables = hosts/users/IPs
- **Reading Path**: Chapter 1 (Dimensional Modeling 101), Chapter 4 (Retail Case Study—adapt to security)
- **Where to Buy**: Amazon, Wiley
- **Note**: Published 2013, principles still valid but examples pre-cloud era

---

**"Architecting an Apache Iceberg Lakehouse" by Alex Merced** (Manning Publications, 2026)
- **Why Essential**: A storage-layer decision framework for Iceberg lakehouses, drawn from production case studies
- **Security-Relevant Chapters**:
  - Chapter 1: Lakehouse definition, Iceberg architecture, cost optimization (cites Insider's reported ~90% S3 reduction)
  - Chapter 4: Audit methodology (5-step stakeholder interview process)
  - Chapter 5: Storage layer selection (15+ scenarios across performance, security, integrity, cost requirements)
- **Cases it draws on**: the Netflix origin story and Insider's reported ~90% cost reduction, with Iceberg adoption at Apple, AWS, Snowflake, and Databricks (Tier C, the book's own citations — verify against the primary sources before quoting a figure)
- **Application to Security Data**: Storage framework maps 1:1 to security workloads (healthcare HIPAA scenario identical to healthcare security log compliance). Integrated into the handbook's storage-layer decision material.
- **Where to Buy**: manning.com
- **Status**: Final edition published April 2026 (confirmed via manning.com)
- **Companion Resources**: Alex Merced YouTube (youtube.com/@alexmerceddata), Dremio blog (dremio.com/blog)

---

### Security Data Architecture

**"Applied Security Visualization" by Raffael Marty** (Addison-Wesley, 2008)
- **Why Relevant**: Security data visualization patterns (still applicable despite age)
- **Key Topics**: Time-series visualization, anomaly detection, dashboard design for SOC
- **Limitation**: Pre-cloud, pre-big data—principles valid, specific tools outdated
- **Where to Buy**: Amazon (used copies)

---

**Note**: As of October 2025, **no full-length book exists on modern security data architecture using open-source table formats and query engines**. This manuscript fills that gap. Monitor O'Reilly catalog for future publications in this space.

---

## Table Formats (Iceberg, Delta, Hudi)

### Apache Iceberg (Recommended for Multi-Engine)

**Official Documentation**: https://iceberg.apache.org/ (table-format spec V3 shipped through 2025 — deletion vectors, row lineage, table encryption — and by mid-2026 the engines have broadly adopted it, with Snowflake V3 support GA in early May 2026 and DuckDB reading and writing V3 deletion vectors as of its 1.5.3 release; the V4 spec is still open as GitHub milestone #58, which has stayed at two proposals with nothing merged into it since late 2025, so the spec line is real but the timeline is unsettled, and you should verify the current state before relying on it)
- **Start Here**: "Tables" guide (iceberg.apache.org/docs/latest/tables/)
- **Key Sections**:
  - Table Spec: Understand metadata, manifests, data files
  - Partitioning: Hidden partitioning for security (date-based partitioning without exposing to users)
  - Evolution: Schema evolution for OCSF v1.3 → v1.4
  - Maintenance: Compaction, snapshot expiration, orphan file cleanup

**Iceberg Blog** (Ryan Blue, creator): https://iceberg.apache.org/blog/
- "Why We Built Iceberg" (foundational post)
- "Iceberg Table Evolution" (schema changes without downtime)
- "Partition Evolution" (repartition without data rewrite)

**Subsurface Conference Videos** (YouTube: "Subsurface conference")
- Ryan Blue keynotes (Iceberg design principles, roadmap)
- Production case studies (Netflix, Apple, Tabular [now Databricks, acquired June 2024])

**Slack Community**: Apache Iceberg Slack (iceberg-community.slack.com)
- #help-iceberg: Troubleshooting queries, table management
- #implementation: Best practices, design patterns
- #security: Limited traffic, but growing (use #help-iceberg for now)

**Learning Path**:
1. **Week 1**: Read official docs (tables, partitioning, evolution) + watch Ryan Blue intro video
2. **Week 2**: Deploy local Iceberg table (MinIO or LocalStack S3), test with Spark/Trino
3. **Week 3**: Ingest sample security data (EDR logs, network flows), test queries
4. **Month 2**: Production pilot (3-5 data sources, 5-10 analysts)

---

### Delta Lake (Alternative if Databricks-Committed)

**Official Documentation**: https://delta.io/
- **Start Here**: "Learn" section (delta.io/learn)
- **Key Topics**:
  - ACID transactions (compare to Iceberg)
  - Time-travel queries (compliance use case)
  - Streaming integration (Spark Structured Streaming)

**Delta Lake Book**: "Delta Lake: The Definitive Guide" (O'Reilly, 2024)

**Learning Path**: If committed to Databricks, Delta Lake is default table format. Otherwise, Iceberg preferred for multi-engine flexibility.

---

### Apache Hudi (Less Common in Security)

**Official Documentation**: https://hudi.apache.org/
- **Use Case**: Heavy upsert workload (incremental CDC ingestion)
- **Security Applicability**: Rare—security data is append-only (minimal updates/deletes)
- **Recommendation**: Unless specific upsert requirement, use Iceberg or Delta

---

## Query Engines (Trino, Dremio, Spark, Athena)

### Trino (formerly Presto)

**Official Documentation**: https://trino.io/docs/current/
- **Start Here**: "Overview" + "Use Cases"
- **Security-Relevant Sections**:
  - Connectors: Iceberg, Hive, PostgreSQL, Kafka (federation across sources)
  - SQL Functions: String manipulation, JSON parsing, aggregation (threat hunting queries)
  - Performance: Predicate pushdown, partition pruning (query optimization)

**Trino Community Slack**: https://trinodb.io/slack
- #help: Query syntax, troubleshooting
- #connectors-iceberg: Iceberg-specific questions
- #general: Community discussions, best practices

**Starburst (Commercial Trino)**: https://www.starburst.io/
- **When to Use**: Need enterprise support, SLA, or managed Trino (Starburst Galaxy = Trino Cloud)
- **Free Resources**: Starburst documentation (many Trino best practices apply)

**Learning Path**:
1. **Week 1**: Deploy Trino locally (Docker), connect to sample Iceberg tables
2. **Week 2**: Write threat hunting queries (high-cardinality filtering, multi-table joins)
3. **Week 3**: Production pilot (self-hosted Trino or Starburst Galaxy trial)

"AWS Athena uses Starburst under the hood—Trino proven at security data scale." — a data-platform practitioner [Personal communication, October 2025]

> **Note**: Athena v3 runs open-source Trino, not Starburst specifically (Starburst is a commercial Trino distribution with additional enterprise features built on top). The underlying point holds — Athena's Trino foundation is proven at scale — but the "Starburst under the hood" framing overstates the Starburst relationship.

---

### Dremio

**Official Documentation**: https://docs.dremio.com/
- **Start Here**: "What is Dremio" + "Reflections" (key differentiator)
- **Security-Relevant Features**:
  - Reflections: Pre-computed aggregations (<1 sec dashboards, Appendix I pattern)
  - Iceberg optimization: Column-level and row-level security
  - BI integration: Tableau, Power BI, Looker connectors

**Dremio University**: https://www.dremio.com/university/
- Free courses: "Dremio Fundamentals," "Reflections Explained," "Iceberg with Dremio"

**Dremio Community Slack**: https://www.dremio.com/community/
- Active community, responsive Dremio engineers
- #reflections: Dashboard optimization questions
- #iceberg: Dremio + Iceberg best practices

**When to Use Dremio**:
- Dashboard-heavy workload (SOC dashboards refreshing every 30-60 seconds)
- BI tool integration priority (Tableau, Power BI)
- Managed service preference (Dremio Cloud vs. self-hosted Trino)

**Learning Path**:
1. **Week 1**: Dremio Cloud trial (14-day free), connect to Iceberg on S3
2. **Week 2**: Build SOC dashboards with Reflections (<1 sec refresh)
3. **Week 3**: Production decision (Dremio Cloud vs. Trino self-hosted)

---

### Apache Spark

**Official Documentation**: https://spark.apache.org/docs/latest/
- **Security-Relevant Use Cases**:
  - **Iceberg maintenance**: Compaction, snapshot expiration (Trino and Flink also support these procedures, but Spark has the most mature tooling and is the most commonly cited in production deployments)
  - **OCSF transformations**: Spark SQL for schema mapping (raw → OCSF)
  - **Batch ingestion**: Spark Streaming for real-time writes to Iceberg

**Learning Paths**:
- **Option 1: AWS EMR** (managed Spark): docs.aws.amazon.com/emr
- **Option 2: Databricks** (Spark + Delta Lake): databricks.com/learn
- **Option 3: Self-hosted Spark** (advanced): spark.apache.org/docs/latest/cluster-overview.html

"Spark is essentially the native language of Iceberg. You may deploy Dremio for queries, but Spark may still be necessary for table maintenance." — a data-platform practitioner [Personal communication, October 2025]

**Learning Path**:
1. **Week 1**: Spark SQL basics (DataFrames, SQL syntax)
2. **Week 2**: Iceberg write operations (CREATE TABLE, INSERT, MERGE)
3. **Week 3**: Maintenance procedures (compaction, snapshot expiration)

---

### AWS Athena

**Official Documentation**: https://docs.aws.amazon.com/athena/
- **When to Use**: AWS-committed, serverless preference, pay-per-query model acceptable
- **Security Application**: Ad-hoc threat hunting, compliance queries (infrequent, high-value queries)

**Athena + Iceberg**: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html
- Athena v3 reads and writes Iceberg format-version 2 tables (time-travel, partition evolution); confirm current format-version support against the AWS docs before relying on V3-spec features

**Cost Optimization**: $5 per TB scanned → Optimize via partitioning, Parquet columnar format, Iceberg metadata filtering

**Learning Path**: If AWS-first (Pattern 2, Appendix C), Athena is primary query engine—start here

---

## Materialized Views & Query Acceleration

### Materialized Views Fundamentals

**Appendix I.4B Decision Framework**: Start here for security-specific materialized views guidance
- Three failure modes: High data change rates, schema volatility, complex queries
- Deploy when ALL criteria met: Query frequency >> data change rate (12:1 ratio), refresh cost < query cost savings (10× benefit), schema stability (<1 change/month)
- Avoid when ANY true: Unpredictable queries (threat hunting), complex correlation (window functions), schema changes weekly

---

### Platform-Specific Documentation

**Dremio Reflections** (Preferred for security dashboards): https://docs.dremio.com/current/sonar/reflections/
- **Key Topics**:
  - Reflection policies (automatic vs. manual)
  - Raw vs. aggregation reflections
  - Refresh strategies (incremental vs. full)
  - Schema change handling (INVALID state triggers)
- **Learning Path**:
  1. **Week 1**: Enable reflections on 1-2 compliance dashboards
  2. **Week 2**: Monitor refresh costs vs query savings (DCU usage)
  3. **Week 3**: Expand to 3-5 high-frequency dashboards (measure ROI)

**Snowflake Materialized Views**: https://docs.snowflake.com/en/user-guide/views-materialized
- **Key Warning**: "Start slowly with this feature (i.e. create only a few materialized views on selected tables) and monitor the costs over time"
- **Schema Change Behavior**: Column modification suspends ALL materialized views on that table (even if column not referenced in view)
- **Security Fit**: Moderate—best for stable schemas, high-frequency queries

**Snowflake Dynamic Tables**: https://docs.snowflake.com/en/user-guide/dynamic-tables-about
- **Advantages over MVs**: Supports JOINs, window functions, target lag settings
- **Limitations**: Recreation required for schema changes, ~5% data change threshold for efficient incremental refresh
- **Security Fit**: Better than Snowflake MVs, but schema changes still problematic

**Databricks Materialized Views**: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-create-materialized-view.html
- **Key Feature**: Cost analysis automatically chooses incremental vs. full refresh
- **Schema Change Behavior**: Full recompute triggered on ANY schema change (a 500 GB table at 30-90 min is an illustrative estimate, not a measured deployment)
- **Security Fit**: Good if using Databricks Unity Catalog, schema changes costly

**AWS Redshift AutoMV**: https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-auto-mv.html
- **Unique Feature**: Automatically creates AND drops materialized views based on cost-benefit analysis
- **Algorithm**: Tracks query time saved, refresh time consumed, storage overhead, net benefit score
- **Key Insight**: Platform admits not all MVs remain economically viable over time
- **Security Application**: Instructive pattern—track MV economics, disable negative-ROI views

**PostgreSQL Materialized Views**: https://www.postgresql.org/docs/current/rules-materializedviews.html
- **Reported speedups**: 78× to 9,000× on favorable workloads (Tier C/D: vendor documentation and vendors' own benchmarks, best-case, not independently reproduced)
- **Refresh**: Manual `REFRESH MATERIALIZED VIEW` command (no automatic incremental refresh)
- **Security Fit**: Limited—suitable for small-scale use cases, manual refresh operational burden

---

### Streaming Materialized Views (Advanced)

**Materialize** (Differential Dataflow): https://materialize.com/docs/
- **Key Differentiator**: Among the strongest IVM support of the streaming platforms here, with fully incremental multi-table joins (the differential-dataflow design is the reason)
- **Architecture**: Maintains dataflow graphs (not result sets) for true incremental updates
- **Performance**: 1000× lower latency than traditional OLTP replicas (vendor claim)
- **Constraint**: Acceptable if touched partitions ≤1,000,000 rows/second (vendor docs, Tier C; can be exceeded during security incidents)
- **Security Fit**: Excellent for sophisticated detection engineering teams, steep learning curve
- **Learning Path**:
  1. **Week 1**: Materialize Cloud trial (14-day free), connect to Kafka + PostgreSQL sources
  2. **Week 2**: Build real-time correlation rules (5-minute windows, multi-table joins)
  3. **Week 3**: Performance testing (simulate alert storms, measure partition recompute overhead)

**ksqlDB** (Kafka Streams): https://docs.ksqldb.io/
- **Best For**: Simple Kafka-native streaming aggregations
- **Limitations**: Single-column join keys only, no SQL-style window functions, approximate COUNT_DISTINCT (HyperLogLog)
- **Security Fit**: Good for basic real-time metrics (event counts, simple aggregations), insufficient for complex correlation
- **Learning Path**: If already using Kafka, ksqlDB is natural choice for simple streaming MVs

**Apache Flink SQL Materialized Tables**: https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/materialized-table/overview/
- **Status**: Materialized Table feature (Flink 1.20+)
- **Complexity**: Operationally complex (Kafka + Flink + serving layer required)
- **Security Fit**: Best for large enterprises with dedicated stream processing teams
- **When to Use**: Real-time detection <30 seconds required, complex stateful processing needed

---

### Research Papers & Advanced Topics

**q-Hierarchical Dichotomy for IVM**: Berkholz, Keppeler, Schweikardt (2017) - https://arxiv.org/abs/1807.08380
- **Key Finding**: Some query patterns are **fundamentally impossible** to maintain incrementally in sub-linear time (O(N^1/2) update time required)
- **Security Relevance**: Explains why complex correlation rules (non-q-hierarchical queries) force full refresh regardless of platform
- **Reading Level**: Advanced (computer science theory)—skip unless interested in computational complexity foundations

**Netflix ClickHouse at petabyte scale** (5 PB/day, 10.6M events/sec average, peaking ~12.5M, logs searchable within ~20s): "How Netflix optimized its petabyte-scale logging system with ClickHouse" — ClickHouse blog, 2025 (https://clickhouse.com/blog/netflix-petabyte-scale-logging)
- **Key Insight**: The reported gains came from disciplined low-level engineering rather than exotic architecture — generated lexers for fingerprinting (regex → JFlex, ~8-10× ingest throughput), a custom native insert protocol with LZ4 compression in place of JDBC batch inserts, and sharding the tag map across 31 buckets to kill linear scans (filter queries 3s → 1.3s, filter-plus-projection ~3s → ~700ms)
- **Security Application**: A worked reference for running ClickHouse at security-relevant volume; note the original draft's "zero materialized views" framing is NOT supported by this article, which doesn't discuss materialized views at all

---

### Blog Posts & Tutorials

**"Materialized Views vs. Caching: When to Use Which"** (Dremio Blog): dremio.com/blog/
- Search for "Reflections vs caching" or "when to materialize"
- **Key Distinction**: MVs = pre-computed results (refresh required), caching = query result storage (TTL-based)
- **Security Application**: Dashboards = MVs (predictable queries), ad-hoc hunting = no materialization

**"Incremental View Maintenance Challenges"** (Materialize Blog): materialize.com/blog/
- Search for "IVM" or "differential dataflow"
- **Key Topics**: Why multi-table joins hard, window function recompute partitions, non-distributive aggregates

**"Snowflake Materialized Views Cost Optimization"** (DataCamp): datacamp.com/tutorial/materialized-views
- **Guidance**: "Materialize complex, resource-intensive queries such as joins, aggregations, and subqueries"—emphasis on **specific** queries, not all queries
- **Security Application**: Selective deployment for 3-5 high-value dashboards, measure before expanding

---

### Economic Analysis Tools

**Cost Tracking Metrics** (Implement these per-view):
- Query frequency (actual, not estimated—use query logs)
- Query cost savings = (baseline query cost - materialized query cost) × frequency
- Refresh cost (compute + storage)
- Schema change frequency (manual intervention triggers)
- Net benefit = Savings - Refresh cost - Operational overhead

**Alert Threshold**: Net benefit < 0 → Disable view (Redshift AutoMV pattern)

---

### Community Resources

**Dremio Community Slack** (#reflections channel): dremio.com/community/
- Active discussions on reflection optimization, refresh strategies, schema change handling
- Dremio engineers responsive to troubleshooting questions

**Materialize Community Slack**: materialize.com/community/
- Advanced topics: Differential dataflow, IVM edge cases, performance tuning

**r/dataengineering Materialized Views Discussions**: reddit.com/r/dataengineering
- Search for "materialized views" + "when to use" OR "pitfalls"
- Practitioner experiences: Success stories, cautionary tales, platform comparisons

---

### Key Takeaways for Security Architects

1. **Netflix at scale** (Appendix I.4A): the ClickHouse logging system runs at 5 PB/day on disciplined low-level engineering, which is the reminder that operational simplicity can outweigh performance optimization (the article doesn't discuss materialized views either way — don't read it as a "zero-MV" endorsement)
2. **Selective deployment**: Start with 3-5 high-value use cases (compliance dashboards, scheduled reports), measure before expanding
3. **Economic analysis critical**: the reported 78× to 9,000× best-case speedups (Tier C/D, not independently reproduced) only translate to cost savings when query frequency >> data change rate
4. **Layered architecture**: Streaming (real-time) → Micro-batch (baselines) → Batch (analytics) → Data lake (hunting). Use right tool for each tier.
5. **Security data failure modes**: High data change rates, schema volatility, complex correlation requirements make MVs operationally complex vs. general BI analytics

**For a full platform comparison**, see ["Materialized Views for Security Data: What Actually Works at Petabyte Scale"](https://securitydataworks.com/writing/engines/materialized-views) on securitydataworks.com.

---

## Data Catalogs (Polaris, Unity, Nessie)

### Polaris (Apache Iceberg Catalog)

**Official Repository**: https://github.com/apache/polaris
- **Status**: Apache incubator project (October 2024), production-ready
- **Why Important**: Iceberg-native catalog (vs. Hive Metastore legacy compatibility)

**Polaris Cloud** (Snowflake-managed): https://www.snowflake.com/en/data-cloud/workloads/apache-polaris/
- **When to Use**: Managed catalog service (eliminate self-hosted Hive Metastore burden)
- **Pricing**: Contact Snowflake (not published as of October 2025)

**Learning Path**:
1. **Week 1**: Deploy Polaris locally (Docker), connect Trino/Dremio to Polaris catalog
2. **Week 2**: Test multi-engine writes (Spark writes, Trino reads—catalog coordination)
3. **Week 3**: Polaris Cloud trial (if managed service preferred)

---

### Unity Catalog (Databricks)

**Official Documentation**: https://docs.databricks.com/data-governance/unity-catalog/
- **When to Use**: Databricks-committed, Delta Lake primary table format
- **Features**: Multi-cloud catalog (AWS + Azure + GCP), fine-grained access control
- **Limitation**: Databricks-centric (not multi-engine like Polaris)

---

### Nessie (Project Nessie)

**Official Documentation**: https://projectnessie.org/
- **Unique Feature**: Git-like versioning for data (branch, merge, rollback)
- **Security Application**: Isolated branches for testing detection rules (test branch → production merge)
- **Status**: Less mature than Polaris/Unity (consider for future evaluation)

---

## Stream Processing (Kafka, Flink)

### Apache Kafka

**Official Documentation**: https://kafka.apache.org/documentation/
- **Security Use Case**: Real-time ingestion (EDR → Kafka → Spark Streaming → Iceberg)
- **Learning Priority**: If real-time detection <30 sec required, Kafka is the standard choice

**Confluent (Commercial Kafka)**: https://www.confluent.io/
- **When to Use**: Managed Kafka Cloud, need enterprise support, schema registry integration
- **Free Resources**: Confluent blog (kafka architecture, best practices)

**Learning Path**:
1. **Week 1**: Kafka fundamentals (topics, partitions, consumer groups)
2. **Week 2**: Kafka Connect (source connectors for EDR, cloud, SaaS)
3. **Week 3**: Integration with Spark Streaming or Flink (Kafka → stream processor → Iceberg)

---

### Apache Flink

**Official Documentation**: https://flink.apache.org/
- **Security Use Case**: Real-time detection (stateful stream processing, windowed aggregations)
- **Complexity**: High—requires 2-3 data engineers minimum

**When to Use Flink**:
- Real-time detection <30 seconds (regulatory requirement)
- Stateful processing (maintain baselines, session tracking)
- Complex event processing (multi-stage correlation)

**Alternative**: If real-time not required, batch processing simpler (Spark, Athena scheduled queries)

---

## Orchestration (Airflow, Dagster, Prefect)

### Apache Airflow

**Official Documentation**: https://airflow.apache.org/docs/
- **Security Use Case**: Schedule batch jobs (Iceberg compaction, OCSF transformations, threat intel refresh)
- **Most Common**: Industry-standard workflow orchestration

**Astronomer (Managed Airflow)**: https://www.astronomer.io/
- **When to Use**: Need managed Airflow Cloud, avoid self-hosted operational burden

**Learning Path**:
1. **Week 1**: Airflow concepts (DAGs, operators, sensors)
2. **Week 2**: Write DAG for Iceberg maintenance (daily compaction, snapshot expiration)
3. **Week 3**: Production deployment (Astronomer Cloud or AWS MWAA)

---

### Dagster

**Official Documentation**: https://docs.dagster.io/
- **Differentiator**: Software-defined assets (data pipeline as code)
- **Security Application**: OCSF transformation pipelines (asset = OCSF table)
- **Status**: Growing adoption (less mature than Airflow, more modern design)

---

### Prefect

**Official Documentation**: https://docs.prefect.io/
- **Philosophy**: "Negative engineering" (handle failures gracefully)
- **When to Use**: Simpler than Airflow for basic workflows, hybrid execution model

---

## OCSF (Open Cybersecurity Schema Framework)

### Official Resources

**OCSF Schema Website**: https://schema.ocsf.io/ (current release v1.8.0, March 2026; the schema browser lets you pick the version)
- **Start Here**: Browse event classes (Authentication, Network Activity, Process Activity)
- **Key Sections**:
  - Class Browser: Explore field mappings
  - Downloads: JSON schema, Avro schema, CSV reference
  - Blog: OCSF adoption case studies

**OCSF GitHub**: https://github.com/ocsf
- Schema repository (contribute mappings, report issues)
- Reference implementations (parsers, transformers)

**OCSF Slack**: https://ocsfcommunity.slack.com/
- #general: Community discussions, adoption questions
- #schema-development: Propose new event classes, field additions
- #integrations: Vendor integration updates (AWS, Splunk, Microsoft)

---

### OCSF Learning Path

**Week 1: Schema Exploration**
- Browse https://schema.ocsf.io/ (Authentication, Network Activity, Process Activity classes)
- Compare OCSF fields to your existing log sources (CrowdStrike, Zeek, CloudTrail)
- Identify mapping gaps (fields with no OCSF equivalent)

**Week 2-3: Proof-of-Concept Mapping**
- Choose 1-2 high-value data sources (EDR, cloud logs)
- LLM-assisted mapping (Appendix H.4 pattern): GPT-4/Claude generates initial mapping
- Validate semantic accuracy (ambiguous fields flagged for human review)

**Month 2: Production Rollout**
- Expand to 5-10 data sources
- Automate transformations (dbt, Spark SQL)
- Validate detection rules work on OCSF-normalized data

---

### OCSF + D3FEND Integration (Appendix H.5)

**D3FEND**: https://d3fend.mitre.org/
- Ontological grounding for OCSF (DoD/IC compliance pathway)
- OCSF `d3fend` attribute (added v1.3.0) maps events to defensive techniques

**Use Case**: OCSF + D3FEND enables "Show me all detection rules mapped to D3FEND Network Traffic Analysis (D3-NTA)"

**Security Context Graph (`scg` MCP server)**: https://github.com/flying-coyote/sdw-lab-benchmarks (security-context-graph/)
- **What it is**: a read-only, concept-only graph (1,442 nodes / 7,618 deduped edges) joining the public spine — OCSF, D3FEND, ATT&CK, NIST 800-53, and CCI — exposed over a small stdio MCP server with seven tools (legend, stats, find_node, node, neighbors, paths, coverage). It ships the public layer only; the CC-BY-ND SCF crosswalk loads behind `SCG_WITH_SCF=1`.
- **Why it's here**: this is the OCSF↔D3FEND join above made walkable rather than asserted. The current spine carries 69 seeAlso pairs across 27 OCSF classes touching 14 of 607 DigitalArtifact leaves (97.7% leaf-orphan), and SKOS-typed control coverage of 606 edges over 402 controls (111 NIST 800-53, 291 CCI) and 79 D3FEND techniques, so you can see exactly where the crosswalk is dense and where it runs out.
- **The discipline it carries**: every edge is tagged with a `proxy_quality` and a documented trust rank — measured (1.0) and SKOS-typed (0.9) at the strong end down to intent-blind `artifact_cooccurrence` (0.25, the largest class at roughly 6,000 of 7,618 edges) and an explicit `unmapped` (0.0) gap. A multi-hop answer is only as good as its weakest edge, so `paths` returns a `path_trust` (the minimum edge on the chain) and a `crosses_inference` flag that fires when the chain leans on one of those intent-blind co-occurrence edges. It separates what is measured or curated from what was inferred, and names the weakest hop instead of hiding a cheap join, so navigation stays honest about its own provenance.
- **What it does not do**: it is not a grounding accuracy aid. In the SDW Lab field-mapping test (2026-06-08, Tier B), conceptual grounding prose was roughly inert against a plain schema-validity check, and graph structure changed a retrieval answer on only 1 of 9 incident-reconstruction queries (the identity-collapse case), so its value is real but narrow. It is evidence and a navigation tool, not a product — per-vendor scoring stays in the paid Capability Matrix.

---

## MITRE ATT&CK

**Official Website**: https://attack.mitre.org/
- **Security Application**: Map detection rules to ATT&CK techniques (coverage analysis)
- **Data Modeling**: Add `attack_technique_id` column to `detection_rules` table

**ATT&CK Navigator**: https://mitre-attack.github.io/attack-navigator/
- Visual tool: Coverage heatmap (which techniques have detection, which don't)

**Learning Path**: If unfamiliar with ATT&CK, start with "Getting Started" guide (attack.mitre.org/resources/getting-started/)

---

## D3FEND

**Official Website**: https://d3fend.mitre.org/
- **Purpose**: Defensive countermeasure knowledge graph (complement to ATT&CK's offensive focus)
- **OCSF Integration**: Appendix H.5 (ontological grounding for OCSF schema)

---

## NIST Cybersecurity Framework

**Official Website**: https://www.nist.gov/cyberframework
- **Relevance**: Framework for organizing security data architecture by CSF function
  - Identify (ID): Asset inventory integration
  - Detect (DE): Real-time detection, threat hunting
  - Respond (RS): Incident response workflows, SOAR integration

---

## Slack Communities

| Community | Slack URL | Primary Topics | Activity Level |
|------------------|----------------------------|------------------------------|----------------|
| **Apache Iceberg** | iceberg-community.slack.com | Iceberg table format, maintenance, multi-engine | High (1,000+ members) |
| **OCSF** | ocsfcommunity.slack.com | Schema mapping, vendor adoption | High (500+ members) |
| **Trino** | trinodb.io/slack | Trino queries, connectors, federation | High (3,000+ members) |
| **Dremio** | dremio.com/community | Dremio Reflections, BI integration | Medium-High (800+ members) |
| **dbt** | getdbt.com/community | OCSF transformations, data modeling | Very High (10,000+ members) |
| **Dagster** | dagster.io/slack | Data pipeline orchestration | Medium (2,000+ members) |
| **r/dataengineering** | reddit.com/r/dataengineering | General data engineering discussions | Very High (100K+ members) |

---

## Conferences

### Data + AI Summit (Databricks)
- **When**: Annually (June, San Francisco)
- **Focus**: Data engineering, AI/ML, lakehouse architecture
- **Security Relevance**: Iceberg talks, data governance, access control
- **Registration**: databricks.com/dataaisummit

### Subsurface (Iceberg)
- **When**: Annually (September, virtual + in-person)
- **Focus**: Apache Iceberg deep-dive, production case studies
- **Security Relevance**: Highest Iceberg content density
- **Registration**: subsurfaceconf.com
- **Note**: Originally organized by Tabular; Tabular was acquired by Databricks (June 2024). The conference continues under Iceberg community sponsorship.

### Trino Summit
- **When**: Annually (various locations)
- **Focus**: Trino query federation, connectors, performance
- **Security Relevance**: Threat hunting query patterns, multi-source federation
- **Registration**: trino.io/community.html

### RSA Conference
- **When**: Annually (April, San Francisco + various)
- **Focus**: Cybersecurity industry trends, vendor expo
- **Security Relevance**: OCSF adoption talks, security data panels
- **Registration**: rsaconference.com

### BSides Security
- **When**: Year-round (local chapters)
- **Focus**: Grassroots security community, technical talks
- **Security Relevance**: Detection engineering, threat hunting, security data architecture
- **Registration**: bsides.org (find local chapter)

---

## Thought Leaders to Follow

### Data Engineering

**Joe Reis** (Author, "Fundamentals of Data Engineering")
- Twitter/X: @joe_reis
- Newsletter: joereis.substack.com
- Focus: Data engineering principles, anti-patterns, career advice

**Ryan Blue** (Apache Iceberg creator, Tabular co-founder; now at Databricks, 2024)
- Twitter/X: @rdblue
- Conference talks: YouTube "Ryan Blue Subsurface" or "Ryan Blue Iceberg"
- Focus: Iceberg design, table formats, lakehouse architecture

**Alex Merced** (Developer Advocate, Dremio)
- YouTube: youtube.com/@alexmerceddata
- Blog: alexmerced.com/devblog
- Focus: Iceberg, Dremio, Apache Arrow, query engines

**Zhamak Dehghani** (Data Mesh creator)
- Twitter/X: @zhamakd
- Book: "Data Mesh" (O'Reilly)
- Focus: Decentralized data architecture (less directly relevant to security, but influential)

---

### Security Data Architecture

**a data-platform practitioner** (a data platform vendor, Practitioner validation in the variants chapter and Appendix I)
- LinkedIn: Search "a data-platform practitioner a data platform vendor"
- Focus: Starburst/Athena for security, Denodo virtualization, hybrid architectures
- **Book Validation**: Provided practitioner validation for multi-engine patterns, hybrid architectures

**Jake Thomas** (Practitioner, Security data engineering)
- Focus: Edge preprocessing with DuckDB, volume reduction patterns
- **Book Validation**: Provided DuckDB Lambda patterns in Appendix I

**Lisa Cao** (Gravitino contributor; formerly Datastrato, which rebranded)
- LinkedIn: Search "Lisa Cao Gravitino"
- Focus: Gravitino meta-catalogs, catalog federation
- **Topic**: Gravitino for security data source cataloging (Appendix D reference)

---

### Security Community (OCSF, ATT&CK)

**OCSF Working Groups**
- Monthly meetings (open to community): Check ocsfcommunity.slack.com for schedule
- Working groups: Schema Development, Integrations, Adoption

**MITRE ATT&CK Team**
- Twitter/X: @MITREattack
- Blog: medium.com/mitre-attack
- Focus: ATT&CK framework updates, detection engineering

---

## Blogs & Newsletters

### Data Engineering

**Joe Reis Newsletter** (joereis.substack.com)
- Weekly essays on data engineering, career, industry trends
- Free subscription

**Data Engineering Weekly** (dataengineeringweekly.com)
- Curated links: articles, tools, job postings
- Free email newsletter

**Dremio Blog** (dremio.com/blog)
- Reflections optimization, Iceberg best practices, BI integration
- Focus: Lakehouse architecture, query acceleration

**Trino Blog** (trino.io/blog/)
- Release notes, connector updates, performance tuning
- Focus: Query federation, new features

---

### Security

**Detection Engineering Weekly** (detectionengineering.net)
- Curated links: detection rules, threat hunting, security data
- Focus: Detection-as-code, analytic development

**SANS Internet Storm Center** (isc.sans.edu)
- Daily security news, threat intelligence, IOC feeds
- Free email digest

---

## Companion Essays: Security Data Works

**URL**: [securitydataworks.com/writing](https://securitydataworks.com/writing)
**Status**: ~70 essays across ten pillars, plus measured benchmarks at [/lab](https://securitydataworks.com/lab) and longer evidence pieces at [/research](https://securitydataworks.com/research) — continuously updated.
**Relationship**: these essays are the research laboratory for this book. Many of the frameworks, case studies, and production validations here were first tested as posts (originally on the Security Data Commons Substack, 2024–early 2026, now consolidated onto securitydataworks.com) with community feedback before they were folded into the manuscript, and the site keeps moving as the formats, standards, and benchmarks do.

The site covers what a fixed manuscript cannot — Iceberg V3/V4 as it shipped, the OCSF↔D3FEND grounding work, the Lab's measured numbers, and the fast-moving AI/agent material — so use this map as "further reading" for any chapter. Links go to the live essay; rows marked † are a best-fit mapping from the old post (titles didn't always survive the move one-to-one), worth a quick check.

### Foundation Layer (Architecture Decisions)

| Essay | Extends |
|-------|---------|
| [The MOAR Stack: Security Data Lakehouse Reference Architecture](https://securitydataworks.com/thesis/moar) | **Appendix C** — component model and reference architecture |
| [Apache Iceberg — Why It's Important to Security](https://securitydataworks.com/writing/lakehouse/iceberg-v3-thesis-shift) † | **Appendix D, Appendix I** — table-format capabilities, the V3/V4 shift |
| [Iceberg vs Delta Lake for Security Data](https://securitydataworks.com/writing/lakehouse/iceberg-vs-delta) | **the variants chapter** — decision framework with Netflix/Insider production evidence |
| [Unity Catalog vs Polaris vs Nessie](https://securitydataworks.com/writing/catalogs/catalog-decision) | **Appendix I** — catalog selection for fine-grained security governance |
| [dbt for Security Data Transformation](https://securitydataworks.com/writing/engines/dbt-for-security) | **Appendix D, Appendix H** — OCSF mapping patterns with dbt |
| [ETL vs ELT for Security Data](https://securitydataworks.com/writing/pipelines/etl-vs-elt) | **Appendix D** — cost implications at scale, data ownership models |
| [Iceberg Table Maintenance at Scale](https://securitydataworks.com/writing/lakehouse/iceberg-maintenance) | **Appendix I** — compaction, snapshot expiration, operational patterns |

### Engine Layer (Query Engines & Streaming)

| Essay | Extends |
|-------|---------|
| [ClickHouse at Petabyte Scale — Netflix Case Study](https://securitydataworks.com/writing/engines/clickhouse-petabyte) | **Appendix I** — 5 PB/day architecture, zero-MV validation |
| [Query-Engine Specialization: Push vs Pull](https://securitydataworks.com/writing/engines/push-pull-engines) † | **Appendix I** — dual-engine workload optimization |
| [Cribl vs Tenzir: Route-by-Value Economics](https://securitydataworks.com/writing/pipelines/cribl-vs-tenzir) | **the what-good pipeline-evaluation material, Appendix B** — pipeline evaluation |
| [DuckDB for Threat Hunting: 7.5 Trillion Records at Okta](https://securitydataworks.com/writing/engines/duckdb-threat-hunting) | **Appendix I** — Jake Thomas / Okta Tier-B personal account, edge preprocessing |
| [Kafka to Iceberg: Hidden Integration Costs](https://securitydataworks.com/writing/pipelines/kafka-iceberg-integration) | **Appendix I** — streaming-to-lakehouse architectural challenges |
| [Streaming Decision: RisingWave, Fluss, and the Alternatives](https://securitydataworks.com/writing/pipelines/streaming-decision) † | **Appendix I** — emerging alternatives to Kafka+Flink |

### Detection Layer (SIEM & Schema Standardization)

| Essay | Extends |
|-------|---------|
| [Browse the migration & detection pillars](https://securitydataworks.com/writing) ‡ | **the variants chapter** — adoption barriers (no single successor essay yet) |
| [Splunk Federated Search vs DB Connect](https://securitydataworks.com/writing/migration/splunk-federated-search) | **the variants chapter and the modernization chapter** — phased migration, parallel operation; now tracks Platform 10.4 + Cisco Data Fabric |
| [Detection Engineering Maturity Ladder (HMM Levels)](https://securitydataworks.com/writing/detection/detection-maturity) | **the modernization chapter** — why HMM2→HMM3 requires data infrastructure |
| [Schema Lock-In Costs — Why OCSF Matters](https://securitydataworks.com/writing/ocsf/schema-read-vs-write) † | **Appendix H** — migration cost, three-layer switching costs |
| [OCSF at Petabyte Scale — AWS Security Lake](https://securitydataworks.com/research/aws-security-lake-ocsf) † | **Appendix H** — production OCSF validation |
| [AI-Generated OCSF Parsers via MCP / LLM mapping](https://securitydataworks.com/writing/ocsf/llm-ocsf-mapping) | **Appendix H, Appendix F** — LLM-assisted mapping, and its measured fidelity ceiling |

### Automation Layer (Implementation & Organization)

| Essay | Extends |
|-------|---------|
| [NANDA: Agent-Native Security Infrastructure](https://securitydataworks.com/writing/ai/nanda-automation) | **the modernization chapter** — agent-native SOC architecture beyond the incremental-automation plateau |
| [Pitching MOAR to Federated Organizations](https://securitydataworks.com/writing/migration/federated-rollout-playbook) | **the modernization chapter** — stakeholder buy-in for multi-BU deployments |
| [Migration Reality Check: 800 Detection Rules](https://securitydataworks.com/writing/migration/migration-800-rules) | **the modernization chapter** — realistic migration timelines and costs |
| [Pipeline Lock-In: The Vendor Trap](https://securitydataworks.com/writing/pipelines/pipeline-lock-in) | **Appendix B** — acquisition economics |
| [Defining What You Can Own: an AI-Security Taxonomy](https://securitydataworks.com/writing/ai/defining-what-you-can-own) † | **the manageability chapter (Chapter 1 of the handbook)** — disambiguating "AI security" |

### Anti-Patterns & Deep Dives

| Essay | Extends |
|-------|---------|
| [Peak Lakehouse Threat Hunting Anti-Pattern](https://securitydataworks.com/writing/detection/peak-lakehouse-hunting) | **Appendix B** — architecture over-optimization mistakes |
| [Anti-Pattern: Field Mapping Hell](https://securitydataworks.com/writing/ocsf/field-mapping-anti-pattern) | **Appendix B, Appendix H** — data transformation failures |
| [Anti-Pattern: Underestimating Migration Costs](https://securitydataworks.com/writing/migration/migration-cost-reality) | **Appendix B, the modernization chapter** — realistic cost assessment (labor ran 40-100% over tech-only) |
| [Anti-Pattern: Flattening Away Detection Logic](https://securitydataworks.com/writing/ocsf/flattening-anti-pattern) | **Appendix B** — schema design mistakes; the absence→NULL recall result |

### Research Foundation

| Essay | Extends |
|-------|---------|
| [Why I Built a Living Literature Review / Methodology](https://securitydataworks.com/research/methodology) | **All chapters** — evidence methodology, confidence levels, contradiction-hunting; 100+ sources, PRISMA-aligned, quantitative guidance |
| [The Capability Matrix](https://securitydataworks.com/matrix) | **the handbook's vendor-evaluation/decision material** — the evidence-tiered vendor-evaluation method (method public; scores paid) |
| [AI-Native vs AI-Augmented: the Threat Timeline](https://securitydataworks.com/research/ai-native-vs-augmented) † | **the manageability chapter (Chapter 1 of the handbook)** — why defensive infrastructure must match AI-speed operations |

**Note**: these essays are continuously updated; the book is a March 2026 snapshot and the site captures developments past that date. † marks a best-fit mapping from a retired post number to its closest current essay — worth confirming the destination is the intended one. ‡ marks a post with no single successor essay yet; the link goes to the writing index.

---

## YouTube Channels

**Data Engineering**:
- "Databricks" (databricks.com/resources/demos): Data + AI Summit talks
- "Subsurface Conference" (subsurfaceconf.com): Iceberg deep-dives
- "Alex Merced - Data" (youtube.com/@alexmerceddata): Dremio, Iceberg, Apache Arrow

**Security**:
- "SANS Institute" (youtube.com/user/TheSANSInstitute): Security training, detection engineering
- "Black Hills Information Security" (youtube.com/user/BlackHillsInfoSec): Practical security, hands-on tutorials

---

## Online Courses (Free)

**Dremio University** (dremio.com/university/)
- "Dremio Fundamentals" (2 hours)
- "Reflections Explained" (1 hour)
- "Iceberg with Dremio" (3 hours)

**Databricks Academy** (academy.databricks.com)
- "Data Engineering with Databricks" (free tier)
- "Delta Lake Deep Dive" (free webinars)

**AWS Training** (aws.training)
- "Athena Fundamentals" (1 hour)
- "Building Data Lakes on AWS" (4 hours)
- Free with AWS account

---

This directory covers books, documentation, communities, conferences, and thought leaders organized by topic so you can navigate directly to your learning goal. External URLs were spot-checked October 2025; most recommendations are free (docs, Slack, YouTube).

---

## 30-60-180 Day Learning Plans

### 30-Day Foundation (Security Architect → Data Engineering Basics)

**Week 1: Foundational Reading**
- [ ] Read Joe Reis Chapters 1-5 (storage, compute, ingestion basics)
- [ ] Join dbt Slack, Trino Slack, r/dataengineering Reddit

**Week 2: Hands-On Experimentation**
- [ ] Install DuckDB locally
- [ ] Load sample security logs (download Zeek sample dataset)
- [ ] Practice SQL queries (filtering, aggregation, joins)

**Week 3: Table Formats**
- [ ] Read Apache Iceberg documentation (Table Format Spec)
- [ ] Watch Ryan Blue keynote (YouTube: "Ryan Blue Iceberg Subsurface")
- [ ] Set up Iceberg Docker quickstart

**Week 4: Community Engagement**
- [ ] Attend Trino office hours (virtual)
- [ ] Post question in dbt Slack about OCSF normalization
- [ ] Follow Joe Reis, Alex Merced, Ryan Blue on LinkedIn

---

### 60-Day Intermediate (Deeper Technical Understanding)

**Weeks 1-2: Advanced Concepts**
- [ ] Read Joe Reis Chapters 6-10 (ingestion, queries, pipelines, orchestration)
- [ ] Read Martin Kleppmann Chapters 4, 10, 11 (storage engines, batch, streaming)
- [ ] Set up AWS Athena free tier, query security data on S3

**Weeks 3-4: Tool-Specific Learning**
- [ ] Read "Trino: The Definitive Guide" (Fuller et al., 2022) or "Apache Iceberg: The Definitive Guide" (Shiran et al., 2024)
- [ ] Complete dbt Learn courses (learn.getdbt.com)
- [ ] Build proof-of-concept: Security log pipeline (Kafka → Spark → Iceberg → Trino)

---

### 180-Day Mastery (Production-Ready Architecture)

**Months 3-6: Deep Dive**
- [ ] Implement proof-of-concept with real security data (network flows, endpoint logs)
- [ ] Present findings to team (demonstrate MOAR value)
- [ ] Attend one data engineering conference (Data + AI Summit, Subsurface, Trino Summit)

**Months 3-6: Expert Network**
- [ ] LinkedIn connections: Lisa Cao, Alex Merced, Ryan Blue, Russell Spitzer (Apache Iceberg committer)
- [ ] Engage in Iceberg/Trino/dbt community calls (ask questions, contribute insights)
- [ ] Write blog post: "Security Architect's Journey to Modular Open Architecture"

---

## Recommended Reading Order

**New to Data Engineering** (Security architect background):
1. **Start**: Appendix D (Glossary) - Learn terminology
2. **Foundation**: Joe Reis "Fundamentals" Chapters 5-9
3. **Table Formats**: Iceberg docs + Ryan Blue videos
4. **Query Engines**: Trino or Dremio (choose based on workload—Appendix I decision framework)
5. **OCSF**: Schema exploration + LLM-assisted mapping (Appendix H.4)
6. **Community**: Join Iceberg + OCSF Slack, lurk for 2 weeks, then ask questions

**New to Security** (Data engineer background):
1. **Start**: the handbook's opening chapter, "Manageability > extreme performance" (Chapter 1)
2. **Terminology**: Appendix D (Security → Data Engineering translations)
3. **Standards**: MITRE ATT&CK (attack.mitre.org/resources/getting-started)
4. **OCSF**: Schema.ocsf.io (browse event classes, understand security data model)
5. **Community**: Join OCSF Slack, attend BSides local chapter
6. **Practical**: Appendix I (Query Engine Selection) - Security workload characteristics

**Experienced Practitioner** (Both disciplines):
1. **Architecture Patterns**: Appendix C (Reference Architectures)
2. **Anti-Patterns**: Appendix B (learn from $200K-$4M+ failures)
3. **Advanced Topics**: Appendix H (OCSF ontological grounding), Appendix I (Multi-engine patterns)
4. **Community Leadership**: Contribute to OCSF schema, write blog posts, speak at Subsurface/Trino Summit
