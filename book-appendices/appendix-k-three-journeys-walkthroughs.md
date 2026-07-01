---
type: essay-draft
title: "Appendix K: Three Architect Journeys — Full Decision Walkthroughs"
created: 2026-06-10
tags: [vendor-selection, architecture-decision, hipaa, dremio, iceberg, security-data]
---

# Appendix K: The Three Journeys — Full Walkthroughs

The handbook's variants chapter — Chapter 6, "What good looks like" — carries the decision-relevant summaries of the three architect journeys, the situation and constraints, the decision each architect made, and the outcome with its trade-offs, and this appendix carries the complete walkthroughs behind them: the full requirement tiers, the vendor elimination lists and scoring matrices, the POC designs and per-vendor results, the limitation registers with their mitigations, and the staffing and budget reality checks. Each section below picks up where the corresponding variant summary leaves off, so read the journey's summary in the variants chapter first for the organizational context and the decision rationale, then come here when you want to see the machinery turn.

## K.1 Jennifer's Healthcare SOC: On-Prem/Hybrid Priority

Jennifer's organizational context and constraints, the final architecture decision (Dremio Cloud + on-prem Dremio for PHI), and the Architecture Optimization Statement she put in front of the executive sponsors are in her variant summary in the handbook's variants chapter. This walkthrough picks up at the requirements mapping.

Jennifer is a composite teaching scenario rather than a single named deployment, so the POC timings, the per-vendor cost projections, the staffing counts, and the multi-year TCO bands below are illustrative figures generated from the author's TCO model (Appendix A, Worksheet A.6) applied to a 2.5 TB/day healthcare profile — not measured numbers from one production system. The model's cost inputs, including the discounted Splunk platform rate, trace back to the published G-Cloud 14 pricing anchor documented in Worksheet A.6. Where a figure instead comes from a first-party SDW lab run or a named source, that is called out at the figure.

### Requirements Mapping: The Decision Framework Applied

Jennifer used the three-tier requirement hierarchy from the handbook's decision-worksheet methodology (Appendix A, Worksheet A.1) to filter the vendor landscape systematically.

**Tier 1: Mandatory Requirements (Disqualification Criteria)**

These requirements created hard filters, so any vendor missing even one gets eliminated immediately:

- A SQL query interface, because the analysts know SQL basics from Splunk SPL and Python-first platforms (raw Spark, Databricks notebooks requiring PySpark) would force extensive retraining. SQL is non-negotiable.

- On-premises or hybrid deployment, because HIPAA PHI must stay in controlled data centers and cloud-only platforms (Snowflake, BigQuery, Databricks Cloud without a hybrid option) cannot handle the 20% of data containing PHI even where they are cost-effective for the other 80%.

- A **3-year queryable retention minimum**, since compliance audits work over multi-year windows and platforms with 90-day limits or "archive to offline storage" models fail here. The data has to stay queryable, not just stored.

- Multi-source integration, because security telemetry comes from 40+ sources: EDR (CrowdStrike), network (Zeek), cloud (CloudTrail), SaaS (Okta, O365), and legacy systems, and the platform must ingest diverse formats without a custom parser for each one.

- An open data format, because after the Splunk lock-in experience Jennifer requires vendor-neutral storage, so proprietary formats (Splunk's tsidx, Elastic's Lucene) that make migration operationally infeasible are out. Apache Iceberg, Delta Lake, or Parquet, something portable.

- Operational simplicity, because with 0-1 data engineers available the platforms that need constant tuning (Spark cluster optimization, Kafka broker management, complex Trino configurations) exceed the team's capacity. Managed services or simple architectures only.

**Tier 2: Strongly Preferred (3× Scoring Weight)**

These requirements aren't disqualifying, but heavily weighted in vendor scoring:

- The **Apache Iceberg table format** (3 points), because the industry momentum toward Iceberg provides future flexibility. "Every enterprise is using Iceberg or has it on their roadmap" — a data-platform practitioner [Personal communication, October 2025]. Delta Lake is acceptable (2 points), proprietary formats score 0.

- Time-series partitioning (3 points), because almost every security query I've watched analysts run is time-bounded, since a hunt or an investigation works over a window rather than the whole corpus. Platforms with date-based partition pruning (scan days, not years) cut the data scanned by roughly the ratio of the window to the retention period, so a 30-day query against three years of history reads on the order of a few percent of the table (Apache Iceberg documentation, partition pruning). Native support scores 3, manual partition management scores 1.

- OCSF normalization support (3 points), since the long-term schema-standardization roadmap needs it. Native support scores 3, ETL-based transformation scores 2, no support scores 0. Not mandatory today, heavily preferred for the future.

- A managed query service option (3 points), because on-premises is possible for PHI compliance but a managed cloud service for the non-PHI data (80% of volume) reduces operational burden. Hybrid capability, on-prem + cloud unified query, scores highest (3 points), on-prem only scores 1.

**Tier 3: Nice to Have (Tiebreaker Only)**

These features provide marginal value, breaking ties between close finalists:

- Real-time streaming ingestion: Current 5-15 minute batch latency acceptable for threat hunting. Real-time detection handled by limited Splunk deployment. Nice to have, not critical.

- Built-in ML anomaly detection: SOC prefers rule-based detection with explainability. ML features can be added later via SageMaker or separate tools. Tiebreaker at best.

- Multi-cloud query federation: Currently AWS + on-prem only. Future Azure integration possible but not driving current decision.

**Organizational Constraints (Override Technical Evaluation)**

These constraints act as final validators even for technically superior solutions:

- **Team capacity: 0-1 data engineers** → Self-managed Trino cluster disqualified despite technical elegance. Operational burden exceeds team capacity regardless of capability.

- **Budget: $300K-$500K** → Solutions exceeding $500K annual cost eliminated even if feature-rich. Executive budget authority cannot be exceeded.

- **Compliance: HIPAA on-prem** → Cloud-only solutions fail even with perfect feature set. Regulatory constraint trumps technical preference.

- **Vendor tolerance: Low risk appetite** → Startup platforms (<3 years market presence, limited reference customers) fail despite innovation. Enterprise support availability required for audit defensibility.

### Vendor Filtering Process

Jennifer started with IT Harvest's security data platform landscape: 83 vendors identified across SIEM, data lake, log management, and analytics categories.

**Tier 1 Filtering Results**

Applying the six mandatory requirements:

✗ **Eliminated: 56 vendors** (examples with disqualification reasons):

- **Cloud-only platforms** (18 vendors): Snowflake, BigQuery, Databricks Cloud, Confluent Cloud, plus Chronicle (a Google-Cloud-dependent SaaS that cannot run on-prem at all), which cannot support the on-prem PHI requirement
- **Proprietary data formats** (22 vendors): Splunk, Sumo Logic, Datadog, LogRhythm, whose proprietary storage formats make migration operationally infeasible and violate the open-format requirement
- **Complex operational requirements** (12 vendors): Self-managed Kafka + Spark + Trino, Apache Druid clusters, ClickHouse distributed, which exceed 0-1 engineer capacity
- **Non-SQL primary interface** (4 vendors): Platforms requiring Python/Scala for queries (raw Spark without SQL layer), which violate analyst skill match

✓ **Advanced to Tier 2: 27 vendors** (met all mandatory requirements):

- Dremio (cloud + on-prem hybrid, Iceberg-native, SQL-first, managed option)
- Starburst (Trino commercial, hybrid deployment, Iceberg support, enterprise SLA)
- AWS Athena + Glue (hybrid via Outposts, Iceberg support, SQL-native, fully managed)
- Denodo (data virtualization, on-prem capable, SQL interface)
- Apache Iceberg + managed Trino services (open source foundation, commercial support available)
- Azure Synapse (hybrid deployment, Parquet/Delta, SQL, managed)
- Google BigQuery Omni (multi-cloud including on-prem, managed)
- [Plus 20 others meeting baseline requirements]

**Tier 2 Scoring Matrix**

Applying the four strongly preferred requirements with 3× scoring weight:

| Vendor Solution | Iceberg Native (3 pts) | Managed Option (3 pts) | OCSF Support (3 pts) | Operational Simplicity (3 pts) | **Weighted Score** |
|-----------------|----------------------|----------------------|---------------------|--------------------------------|-------------------|
| **Dremio Cloud + Self-Hosted** | ✓ Full (3) | ✓ Cloud available (3) | ⚠ ETL possible (1) | ✓ Very high (3) | **30 points** |
| **Starburst Enterprise** | ✓ Full (3) | ✓ Galaxy option (3) | ⚠ ETL possible (1) | ⚠ Medium (2) | **27 points** |
| **AWS Athena + Glue** | ✓ Full (3) | ✓ Fully managed (3) | ⚠ Custom ETL (1) | ✓ Very high (3) | **30 points** |
| **Denodo Platform** | ✗ Virtualization (0) | ✓ Enterprise (3) | ⚠ Custom (1) | ✓ High (3) | **21 points** |
| **Self-managed Trino + Iceberg** | ✓ Full (3) | ✗ None (0) | ⚠ Custom (1) | ✗ Low (0) | **12 points** |
| **Azure Synapse** | ⚠ Delta primary (2) | ✓ Managed (3) | ⚠ Custom (1) | ✓ High (3) | **27 points** |

**Finalists Identified** (Top 3 by weighted score):

1. **Dremio** (30 points): Iceberg-native, hybrid deployment, managed cloud option, operational simplicity via Reflections
2. **AWS Athena** (30 points): Fully managed, Iceberg support, but requires Outposts hardware for on-prem ($250K capital expense)
3. **Starburst** (27 points): Trino-based, enterprise support, but higher operational complexity than Dremio/Athena

### POC Evaluation

**POC Design (30-Day Evaluation)**

Jennifer designed proof-of-concept testing realistic threat hunting workflows with actual security data:

**Test Dataset**:
- 90 days historical logs (8 TB total)
- Mix: 20% on-prem clinical systems (simulating PHI), 80% cloud/SaaS
- Representative sources: CrowdStrike EDR, Zeek network, AWS CloudTrail, Okta

**Success Criteria**:
1. **Query performance**: <60 seconds for 90-day threat hunts (analyst patience threshold)
2. **Operational burden**: <4 hours/week maintenance (1/2 day of IT data team time)
3. **Cost projection**: Within $400K/year budget (buffer below $500K cap)
4. **Analyst usability**: SOC analysts can write queries independently after 1 week training

**POC Results**

**Dremio Cloud + On-Prem Deployment**:

✓ **Query performance**: 15-45 seconds for 90-day threat hunts
- Reflections (Dremio's acceleration layer) pre-aggregate common patterns
- Partition pruning on timestamp reduces data scanned by roughly the window-to-retention ratio (a 30-day query against multi-year history reads on the order of a few percent of the table; see the Iceberg partition-pruning note in §K.1 Tier 2), modeled here at about 95%
- Example (illustrative composite-journey POC figure, not a first-party measured run): Hunt for "credential dumping behavior" across 3 billion events (30 days × 100M events/day) completes in 22 seconds

✓ **Operational burden**: 2-3 hours/week
- Mostly reflection tuning (identifying frequently queried patterns)
- Iceberg table maintenance handled by Dremio Cloud (compaction, snapshots)
- Minimal cluster management (Kubernetes required but stable)

✓ **Cost projection**: $380K/year
- Storage (3-year retention, 2.5 TB/day): $180K (S3 tiered lifecycle: Standard → Glacier)
- Dremio Cloud license (compute): $120K (based on query volume, not data ingestion)
- On-prem infrastructure (Kubernetes for PHI data): $80K (existing hardware, software only)

✓ **Analyst feedback**: the SOC analysts read it as querying a database and picked it up quickly
- SQL familiarity from Splunk SPL transfers directly
- BI-like interface (point-and-click for simple queries, SQL for complex)
- One week training sufficient for 80% of hunting workflows

⚠ **On-prem complexity**: Requires Kubernetes cluster
- Jennifer's IT team has limited Kubernetes experience
- Dremio on-prem deployment needs K8s for high availability
- Mitigation: Engage Dremio professional services for initial setup ($40K)

**AWS Athena + Glue**:

✓ **Query performance**: 30-90 seconds for 90-day hunts
- Partition pruning effective (Iceberg metadata helps)
- No acceleration layer like Dremio Reflections (each query scans raw data)
- Adequate but slower than Dremio for repeated queries

✓ **Operational burden**: <1 hour/week
- Fully managed, no infrastructure to maintain
- Glue catalog handles metadata automatically
- Minimal operational overhead (highest simplicity)

⚠ **Cost projection**: $520K/year (exceeds budget)
- Storage (3-year retention): $180K (same S3 costs as Dremio)
- Athena query costs: $240K/year (based on 600 TB scanned monthly, since analysts re-run queries frequently)
- Glue catalog + Kinesis ingestion: $100K/year

✗ **On-prem deployment**: Requires AWS Outposts
- On-prem Athena needs Outposts hardware: $250K capital expense (unbudgeted)
- Alternatively: Keep PHI data in separate on-prem Trino (adds operational complexity)

✓ **Analyst feedback**: standard SQL, familiar to anyone coming from BI tools

**Starburst Enterprise (Trino)**:

✓ **Query performance**: 20-50 seconds for 90-day hunts
- Cost-based optimizer provides good performance
- Comparable to Dremio, slightly slower than Athena for simple queries
- Better than both on the POC's complex joins at this multi-node cluster scale (a regime-specific result rather than a Trino constant; in my single-host SOC-scale join bench, Tier B 2026, Trino carried the largest join overhead of the engines tested)

⚠ **Operational burden**: 6-8 hours/week (exceeds 4-hour target)
- Cluster management (Trino coordinator + workers, scaling)
- Performance tuning (memory configuration, connector optimization)
- More complex than Dremio's managed approach

✓ **Cost projection**: $420K/year (within budget)
- Storage: $180K (same S3 costs)
- Starburst Enterprise license: $160K/year (12 TB/day ingestion tier)
- Infrastructure (compute clusters): $80K/year (AWS EC2 costs)

⚠ **Analyst feedback**: powerful, but with a steep learning curve
- Trino-specific features require training (connector catalog, memory tuning)
- More complex than Dremio's BI-like interface

✓ **On-prem deployment**: Self-hosted, full control
- Deploy Trino on-prem for PHI data (no Outposts hardware required)
- Unified query across on-prem Trino + cloud Trino (federation)

On these results Jennifer selected Dremio Cloud + on-prem Dremio for PHI; the five-point decision rationale is in her variant summary in the handbook's variants chapter.

### Critical Limitations and Honest Trade-Offs

Jennifer documented the limitations explicitly for the executive sponsors and SOC leadership, because the open lakehouse approach carries its own set of trade-offs against Splunk and is not free of them; the honest case for it depends on naming what it does not do.

**What This Architecture Does NOT Solve**:

**1. Real-time detection gap** (5-15 minute latency unacceptable for alerting)

Dremio batch queries update every 5-15 minutes, adequate for threat hunting ("show me lateral movement attempts in the last 30 days") but insufficient for real-time alerting ("alert within 30 seconds of brute force authentication").

**Mitigation**:
- Maintain a limited schema-on-read SIEM deployment for real-time detection only
- Reduce the SIEM to 100 GB/day of highest-priority sources (EDR alerts, admin authentication, privileged access)
- Cost: $200K/year (vs $800K current)
- Use Dremio for threat hunting, forensics, compliance, 90% of analyst queries
- Use the SIEM for real-time correlation rules, 10% of use cases but critical

**Long-term solution**:
- Evaluate Apache Flink or Spark Streaming for real-time detection layer on Iceberg
- Requires dedicated streaming engineer (18-24 months to hire and build capability)
- Phase 2 roadmap, not Phase 1 deployment

**2. Spark maintenance requirement** (practitioner validation)

Apache Iceberg requires periodic maintenance operations: data file compaction (combining small files into optimized sizes), orphan file cleanup (removing unreferenced files from failed jobs), and snapshot expiration (managing time-travel history). These often require Apache Spark for a self-managed deployment, though Athena (OPTIMIZE/VACUUM), Trino (OPTIMIZE), and Dremio (managed maintenance) can also perform compaction and maintenance, so Spark is the common path rather than the only one.

"Spark is essentially the native language of Iceberg. You may deploy Dremio for queries, but Spark may still be necessary for table maintenance." — a data-platform practitioner [Personal communication, October 2025]

**Jennifer's situation**: Healthcare IT team lacks Spark expertise. Learning Spark cluster management, PySpark development, and maintenance job scheduling would require months of training.

**Mitigation**:
- Dremio Cloud includes managed Iceberg maintenance (compaction, cleanup, snapshot expiration handled automatically)
- Jennifer pays for this convenience in Dremio Cloud license ($120K/year)
- If migrating off Dremio in future, Spark expertise becomes mandatory, a risk accepted

**Alternative if choosing Starburst or self-managed Trino**:
- Must deploy Spark separately for Iceberg maintenance
- Weekly compaction jobs (combine small files from hourly ingestion into daily partitions)
- Monthly orphan cleanup (remove unreferenced files from failed ingestion jobs)
- Snapshot expiration (manage time-travel history, expire snapshots older than retention policy)
- Requires 1 dedicated data engineer with Spark expertise, which Jennifer doesn't have

**3. On-premises Kubernetes complexity**

Dremio on-prem deployment requires Kubernetes for high availability, load balancing, and resource management. Jennifer's IT team has limited Kubernetes experience, mostly developers using Docker locally, not production K8s cluster operations.

**Challenge**: Deploying production Kubernetes for security-critical SOC platform introduces operational risk. K8s misconfiguration could expose PHI, cause availability issues during security investigations, or create compliance audit findings.

**Mitigation**:
- Engage Dremio Professional Services for initial deployment and knowledge transfer ($40K one-time)
- Train 2 IT engineers on Kubernetes fundamentals (40-hour online course, $2K/engineer)
- Hybrid trust boundary architecture: Keep only PHI-containing logs on-prem (estimated 20% of total data volume), move remaining 80% to Dremio Cloud (SaaS logs, network traffic, cloud infrastructure)
- Reduces on-prem complexity to smaller Kubernetes deployment (3-node cluster vs 10+ node cluster for full 2.5 TB/day)

**Alternative considered**: Run on-prem Dremio on VMs without Kubernetes
- Single-server deployment possible but loses high availability
- Acceptable for non-critical workloads, unacceptable for 24/7 SOC dependency
- Rejected, with Kubernetes complexity accepted for HA requirement

**4. OCSF normalization not native**

Open Cybersecurity Schema Framework (OCSF) standardizes security event schemas across vendors, so the same field names apply whether a log comes from CrowdStrike EDR, Okta, or AWS CloudTrail. Dremio has no native OCSF transformation capability. Purpose-built SIEMs (Splunk, Sentinel) include vendor-specific normalization; lakehouse platforms do not.

**Challenge**: Analysts write queries using vendor-specific field names (CrowdStrike: "event_simpleName", Okta: "eventType", CloudTrail: "eventName"). Cross-source queries require knowing each vendor's schema. OCSF would unify to standard "event.type" field across all sources.

**Mitigation options**:
1. **Vector log shipper OCSF transformation**: Deploy Vector (open-source log processor) for OCSF mapping at ingestion, so before data reaches Dremio, it is transformed to OCSF schema
2. **SQL views in Dremio**: Create OCSF-mapped views translating vendor schemas to OCSF in query layer (fields aliased at read time)
3. **LLM-assisted mapping** (Appendix H pattern): Use GPT-4 to generate OCSF mapping configurations from vendor documentation (which, in the mapping work I've done, cut the drafting time substantially against hand-writing each field map, though a human still has to validate every result)

**Jennifer's approach**: Start with SQL views (quickest implementation, 2-3 days effort), migrate to Vector transformation incrementally (6-month roadmap as OCSF adoption increases).

The Architecture Optimization Statement Jennifer put in front of the executive sponsors, summarizing what the architecture optimizes for and what it does not provide, is carried in her variant summary in the handbook's variants chapter.

### Staffing & Budget Reality Check: HIPAA Hybrid Architecture

Jennifer's Dremio hybrid architecture, with cloud logs on S3 and PHI logs on an on-premises object store, represents a common mid-sized security operations pattern for regulated industries, and the staffing and budget for a 2.5 TB/day healthcare deployment with 3-year retention and HIPAA compliance shake out roughly as follows:

**Team Composition** (3.5-4.5 FTEs):
- 2 Data Engineers (Dremio query optimization, Iceberg table management, OCSF normalization)
- 1 Platform Engineer (on-prem object-store infrastructure, Dremio cluster operations, Kubernetes management)
- 0.5-1.5 Security Engineers (detection logic, HIPAA compliance use cases, analyst support)

**Annual Operational Budget**: $750K-900K
- Staffing: $668K-800K (3.5-4.5 FTEs × $191K average fully-loaded cost, including salary + benefits + overhead)
- Infrastructure: $50K-70K (on-premises hardware amortization, object-store support contracts, network costs)
- Dremio Cloud licensing: $120K/year (managed Iceberg maintenance, hybrid deployment)
- Training: $20K-30K (Dremio certifications, Kubernetes courses, Iceberg best practices)

**Implementation Timeline**: 3-5 months
- Month 1-2: On-prem object store + Dremio setup + Kubernetes cluster (2-3 FTEs, Dremio Professional Services $40K)
- Month 3-4: Iceberg table design + HIPAA compliance validation + data migration (3-4 FTEs)
- Month 5: Production migration + parallel operations with legacy Splunk (4-5 FTEs)

**3-Year Total Cost of Ownership (TCO)**: $2.4M-2.9M
- Implementation: $250K-350K (one-time: Professional Services, training, initial infrastructure)
- Operations: $2.2M-2.7M (3 years × $750K-900K annual operational budget)

**Comparison to Alternatives**:
- **Expanding the schema-on-read SIEM to full 2.5 TB/day, 30-day retention**: $1.6M+/year = $4.8M+ over 3 years (65-100% MORE expensive, with 30-day retention vs 3-year)
- **Baseline batch lakehouse (from practitioner tools)**: $2.5M over 3 years for generic 2 TB/day deployment

**Why Jennifer's TCO is 16% higher than baseline**: HIPAA compliance premium adds 15-20% to timeline (change control, audit requirements, security validation) and ongoing costs (dedicated security engineer FTE for compliance, professional services for secure Kubernetes deployment, dual environment complexity with hybrid on-prem/cloud split).

The economics here are driven by the batch-first choice: it keeps the team size manageable (3.5-4.5 FTEs against 9-11 for a streaming build) and the budget predictable, and HIPAA adds complexity at the margins without changing the underlying numbers, because the hybrid on-prem/cloud split is operationally workable for a regulated industry where data sovereignty is mandatory rather than optional.

**Evidence**: Staffing Calculator from the literature review (batch 3.5 FTEs baseline, +1 FTE for compliance/governance). The deployment-timeline and HIPAA-compliance premiums are directional scenario assumptions — a regulated-industry build carries change-control, audit, and security-validation overhead a generic one doesn't — not figures from a specific sourced rate.

## K.2 Marcus's Financial Services SOC: Enterprise Cloud Commitment

Marcus's journey is the worked example in the handbook's variants chapter, so the organizational context, the Tier 1 mandatory requirements, the Tier 2 scoring matrix with finalists, the Path A decision with its rationale, and the full Path B re-run are all in his variant summary there. This section carries the step-by-step detail beyond that treatment: the Tier 2 and Tier 3 requirements, the organizational constraints, the Tier 1 elimination detail, the full POC design and per-vendor results, and the staffing and budget comparison of the two paths.

Marcus is a composite teaching scenario, so the POC latencies, the per-vendor cost projections (the $2.9M Athena baseline, the Starburst, Databricks, and Splunk figures), the FTE counts, and the 3-year TCO numbers below are illustrative figures from the author's TCO model (Appendix A, Worksheet A.6) applied to a 12 TB/day financial-services profile, not a measured deployment. The AWS unit prices (S3 tiers, Athena $/TB scanned, Kinesis $/GB) are list rates as of Q4 2025; the Splunk $11.4M/year licensing is list-modeled from the G-Cloud 14 anchor in Worksheet A.6, not a quoted contract. Vendor-specific capability claims (Databricks Photon, Delta UniForm, Starburst connectors) are vendor representations at Tier C unless separately sourced.

### Tier 2 and Tier 3 Requirements and Organizational Constraints

**Tier 2: Strongly Preferred (3× Scoring Weight)**

- AWS-native integration (3 points): deep integration with IAM (identity and access), VPC (network isolation), S3 lifecycle (automated tiering to Glacier), and CloudWatch (monitoring and metrics). Platforms built on AWS-native services score highest, multi-cloud platforms with "good" AWS integration score medium, platforms requiring manual configuration score low.

- An **open table format, Iceberg or Delta** (3 points), to prevent vendor lock-in. "Every enterprise is using Iceberg or it's on their roadmap" — a data-platform practitioner [Personal communication, October 2025]. Iceberg scores 3 (multi-engine support: Athena, Dremio, Trino, Spark), Delta scores 2 (Databricks-centric but convertible), proprietary formats score 0.

- A managed service (3 points), to minimize operational overhead. Fully managed (no infrastructure to operate) scores 3, partially managed (managed compute, self-managed storage) scores 2, self-managed scores 0. The team can handle moderate complexity but prefers managed.

- Multi-engine query support (3 points), the flexibility to use different query engines for different workloads: Athena for analyst ad-hoc queries (pay-per-query), Redshift for dashboard queries (persistent cluster for sub-second latency), EMR Spark for complex transformations. Platforms supporting multiple engines score 3, single-engine platforms score 0-1.

- Streaming analytics capability (3 points) for real-time fraud detection and insider-threat monitoring. Native streaming (Kinesis → query in <1 minute) scores 3, micro-batch (5-minute latency) scores 2, batch-only scores 0.

**Tier 3: Nice to Have (Tiebreaker)**

- Built-in ML/AI features: Can use SageMaker for custom ML models. Nice to have, not critical.
- Native OCSF support: Can implement via Glue ETL. Tiebreaker at best.
- Multi-region replication: GDPR requires EU data stay in EU, but replication not needed (deploy separate EU stack if necessary).

**Organizational Constraints (Override Technical Evaluation)**

- **Team capacity: 3 data engineers + AWS expertise** → Can manage moderate complexity (Spark streaming jobs, Glue pipelines). Self-managed Kubernetes cluster acceptable but not preferred.

- **Budget: $2M-$4M** → Mid-range enterprise budget. Cost matters but not primary constraint (risk reduction and capability prioritized over cost optimization).

- **Compliance: FINRA, GDPR, PCI** → Multi-region support required (US, EU data residency), 7-year queryable retention mandatory, real-time fraud detection regulatory requirement.

- **Vendor relationship: $15M/year AWS commitment** → Use AWS services where feasible. Choosing GCP or Azure-primary solutions forfeits negotiated discounts.

- **Executive directive: Cloud-first** → Eliminate on-premises options. CTO-level mandate cannot be violated without exceptional justification (none exists for security data).

### Tier 1 Filtering Detail

Starting with 83-vendor landscape:

✗ **Eliminated: 65 vendors**

- **On-premises focused** (12 vendors): Self-hosted Trino requiring on-prem deployment, on-prem Dremio without cloud option, which violate cloud-first executive directive
- **Single-cloud without multi-cloud** (8 vendors): BigQuery (GCP-only), Azure Synapse (Azure-only without AWS connectors), which violate multi-cloud requirement
- **No 7-year queryable retention** (18 vendors): Splunk with archive-to-unqueryable-S3, Elastic cold tier with 1-year query limit, platforms with 90-day retention maximums, which violate compliance requirement
- **Limited enterprise SLA** (14 vendors): Open-source without commercial support (Apache Druid, Pinot community editions), startups without 24/7 support (less than 3 years established, <100 enterprise customers), which violate SLA requirement
- **Batch-only or real-time-only** (13 vendors): Batch analytics platforms without streaming capability, real-time platforms without cost-effective 7-year retention, which violate dual capability requirement

✓ **Advanced to Tier 2: 18 vendors**

- AWS Athena + Iceberg + Glue + Kinesis (AWS-native, 7-year S3 queryability, managed, multi-cloud via federation)
- Starburst Galaxy (AWS-based Trino, Iceberg support, managed service, enterprise SLA)
- Dremio Cloud (AWS deployment, Iceberg-native, managed service, multi-engine via federation)
- Snowflake (multi-cloud, Iceberg support, enterprise scale, 7-year retention)
- Databricks (AWS-native, Delta Lake, unified streaming/batch, enterprise)
- Azure Synapse (multi-cloud connectors, Parquet/Delta, managed, Microsoft SLA)
- [Plus 12 others meeting mandatory requirements]

The Tier 2 scoring matrix and the three finalists it produced are in Marcus's variant summary in the handbook's variants chapter.

### POC Design and Results

**POC Design (60-Day Enterprise Evaluation)**

Marcus's POC tested at production scale to validate enterprise performance:

**Test dataset**: 1 year historical logs (4.3 PB), real-time ingestion (12 TB/day)
**Workload mix**: 70% threat hunting (ad-hoc queries, 90-day to 1-year scans), 20% dashboards (real-time monitoring), 10% compliance queries (multi-year audit investigations)

**Success criteria**:
1. Query performance: <30 seconds for 90-day hunts, <5 minutes for 1-year compliance queries
2. Real-time latency: <2 minutes ingestion-to-query (fraud detection requirement)
3. Cost within $3.5M/year total platform budget
4. Multi-cloud federation: AWS + Azure unified query (single SQL interface for acquired companies)

**POC Results: AWS Athena + Iceberg + Glue + Kinesis Firehose**

✓ **Query performance exceeded expectations**:
- 90-day threat hunts: 8-25 seconds (partition pruning reduces 12 PB corpus to 1 TB scanned)
- 1-year compliance queries: 90-180 seconds (Iceberg metadata-based filtering)
- 7-year audit queries: 4-8 minutes (acceptable for quarterly compliance use case)

Example threat hunt:
```sql
-- Hunt for credential stuffing across 90 days (990 TB scanned without optimization)
SELECT user_id, source_ip, COUNT(*) as failed_attempts
FROM security_events_iceberg
WHERE event_type = 'authentication_failure'
  AND date >= CURRENT_DATE - INTERVAL '90' DAY
  AND rate_limit_triggered = true
GROUP BY user_id, source_ip
HAVING COUNT(*) > 100
ORDER BY failed_attempts DESC;

-- Athena execution: 14 seconds (partition pruning: 990 TB → 8 TB scanned)
```

✓ **Real-time latency acceptable**: 60-90 seconds ingestion-to-query
- Kinesis Firehose buffers logs (60-second batches)
- S3 write + Glue catalog refresh (15-30 seconds)
- Iceberg table metadata update (5-10 seconds)
- Total: 80-130 seconds (slightly above 60-second target, acceptable for fraud detection when combined with separate real-time alerting layer)

✓ **Cost projection: $2.9M/year** (within $3.5M budget, all pricing as of Q4 2025)

Detailed cost breakdown:
- **S3 storage (7-year tiered retention)**: $1.2M/year
  - Year 1: S3 Standard ($0.023/GB/month) — $1.0M/year for 3.6 PB
  - Year 2-3: S3 Infrequent Access ($0.0125/GB/month) — $0.15M/year incremental
  - Year 4-7: S3 Glacier Flexible Retrieval ($0.0036/GB/month) — $0.05M/year incremental
- **Athena query costs**: $800K/year
  - 500 TB scanned/day average (analysts, dashboards, compliance)
  - $5/TB scanned = $2,500/day × 365 days = $913K/year
  - AWS discount (volume pricing from $15M commitment): 12% discount = $800K/year
- **Glue catalog + Kinesis Firehose**: $400K/year
  - Glue Data Catalog: $100K/year (request costs, storage)
  - Kinesis Firehose: $300K/year (12 TB/day ingestion × $0.029/GB)
- **Data transfer (multi-cloud federation)**: $500K/year
  - AWS → Azure Synapse federated queries (15% of queries cross-cloud)
  - Egress: 180 TB/month × $0.09/GB = $486K/year

**Total AWS-native stack**: $2.9M/year (17% buffer below $3.5M budget)

This $2.9M is the Athena-native baseline carried as Marcus's headline figure throughout the book. The architecture Marcus actually selected adds a Starburst Enterprise license (~$400K/year) for the ~10% of advanced federation and high-concurrency workloads, with Athena's query spend dropping as the heaviest queries move off it, so the all-in hybrid lands at roughly $3.0M/year (see Marcus's variant summary in the handbook's variants chapter) — still inside the $3.5M budget.

✓ **Multi-cloud federation validated**:
- Athena federated queries to Azure Synapse via connectors
- Query latency overhead: 5-10 seconds (acceptable)
- Example: Join AWS CloudTrail (Athena Iceberg) + Azure AD logs (Synapse) in single SQL query
- Performance degradation acceptable for 15% of queries requiring cross-cloud data

✓ **AWS integration advantages**:
- Native IAM: Row-level security via Iceberg metadata + Lake Formation permissions
- VPC endpoints: Private S3 access, no internet egress costs for queries
- S3 lifecycle: Automated tiering (Standard → IA → Glacier) based on access patterns
- CloudWatch metrics: Query performance monitoring, cost tracking, anomaly detection

**POC Results: Starburst Galaxy (AWS Deployment)**

✓ **Query performance strong**: 5-20 seconds (90-day), 60-120 seconds (1-year)
- Trino cost-based optimizer outperforms Athena for complex queries (multi-table joins, subqueries)
- Simple scans slower than Athena (no Athena-specific optimizations)

✓ **Real-time latency better**: 30-60 seconds
- Starburst streaming connector: Kafka → Iceberg (lower latency than Kinesis Firehose batching)
- Advantage for real-time fraud detection use case

⚠ **Cost projection: $3.8M/year** (exceeds $3.5M budget by 8.5%)

Cost breakdown:
- **S3 storage**: $1.2M/year (same as Athena, shared storage layer)
- **Starburst Galaxy license**: $1.6M/year
  - 12 TB/day ingestion-based pricing tier
  - Enterprise SLA with 24/7 support included
  - Galaxy is the fully-managed SaaS edition (compute bundled); the self-managed Starburst Enterprise license in Jennifer's K.1 ($160K/year) prices only the software, which is why the two Starburst figures differ by an order of magnitude
- **Compute infrastructure**: $800K/year
  - AWS EC2 for Starburst clusters (c5.4xlarge instances, auto-scaling)
  - Higher compute costs than Athena (persistent clusters vs serverless)
- **Data transfer**: $200K/year
  - Lower than Athena (Starburst cluster-to-cluster replication for Azure, not query-time federation)

⚠ **AWS integration good, not native**:
- Requires additional IAM configuration (Starburst service accounts, cross-account roles)
- VPC setup more complex (Starburst cluster networking vs Athena serverless)
- S3 lifecycle managed separately (no Starburst-native tiering)

**POC Results: Databricks (AWS Deployment)**

✓ **Query performance excellent**: 3-15 seconds (90-day), 45-90 seconds (1-year)
- Delta Lake caching (frequently accessed data cached in cluster memory)
- Photon engine acceleration (C++ vectorized execution)
- Fastest option tested, especially for repeated queries

✓ **Real-time latency best**: <30 seconds
- Spark Streaming → Delta Lake (native integration)
- Meets fraud detection <30 second requirement without separate alerting layer

⚠ **Cost projection: $4.2M/year** (exceeds budget by 20%)

Cost breakdown:
- **S3 storage**: $1.2M/year (Delta format on S3)
- **Databricks DBU consumption**: $2.4M/year
  - DBUs (Databricks Units) for compute: queries, streaming jobs, notebook analytics
  - All-you-can-eat model: $0.55/DBU, estimated 4.4M DBUs/year for workload
- **Infrastructure**: $600K/year (EC2 costs billed separately from DBUs)

⚠ **Multi-cloud challenge**: Requires separate Databricks workspaces
- AWS workspace cannot directly query Azure workspace
- Data replication required for cross-cloud queries (adds cost, latency, compliance complexity)
- Rejected for multi-cloud requirement

⚠ **Vendor lock-in concern**: Delta Lake format
- Convertible to Iceberg via UniForm feature (Databricks converts Delta → Iceberg simultaneously)
- Adds 10-15% storage overhead (both formats maintained)
- Less portable than Iceberg-native approach

On these results Marcus selected the AWS Athena + Starburst Enterprise hybrid; the architecture pattern, cost optimization, and decision rationale are in his variant summary in the handbook's variants chapter, along with the Path B re-run that later sent the organization back to Splunk.

### Staffing & Budget Reality Check: Greenfield vs SIEM Parallel Path

Marcus's journey from AWS Athena greenfield (Path A) to Splunk parallel path with future lakehouse optionality (Path B) illustrates the staffing and budget implications of changing requirements mid-stream, and the way team capacity and regulatory constraints reshaped the economics is worth tracing through both paths side by side:

| Dimension | Path A: Athena greenfield (2022-23 plan) | Path B: Splunk + lakehouse optionality (2024 actual) |
|---|---|---|
| Team | 3 FTE (2 data engineers, 1 platform engineer, AWS) | 2 FTE (0 dedicated data engineers; 2 security engineers with Splunk from the existing SOC) |
| Budget/yr | $600K operational (staffing + AWS infra) | $12M (SIEM licensing $11.4M for 15 TB/day high-volume tier, list-modeled, + 2 FTE $600K) |
| Timeline | 3-4 months (Athena serverless, Iceberg tables, Glue ETL) | 1 month (Splunk ES + fraud-detection content, no custom dev) |
| 3-year TCO | $2.1M ($300K implementation + $1.8M operations) | $36M+ (SIEM licensing dominates) |
| Performance | 60-90 s latency, historical compliance | <5 s real-time detection (beats SEC <30 s mandate) |

**Why Path B Won Despite 17× Higher Cost**:

1. **Regulatory Mandate Changed**: New SEC requirement for <30 second fraud detection made 60-90 second Athena latency non-compliant (compliance risk >> cost savings)

2. **Team Reality Shifted**: Lost 2 of 3 data engineers to attrition, couldn't hire replacements within 90-day SEC deadline (0 available data engineering capacity for Athena/Iceberg maintenance)

3. **Timeline Pressure**: 90-day SEC compliance deadline impossible with greenfield Athena deployment (3-4 months minimum), but achievable with Splunk turnkey fraud detection rules (day-1 availability)

4. **Operational Complexity During Crisis**: Troubleshooting the Athena + Starburst + Iceberg stack requires coordinating across AWS support (Athena), Starburst support (connectors), and the internal team (Iceberg maintenance), which is unacceptable during 3 AM fraud incidents vs single Splunk support call

5. **Risk-Adjusted Value**: Real-time fraud prevention worth $9M/year premium given regulatory exposure ($50M+ SEC fines for non-compliance), reputational risk (financial services brand damage), and operational simplicity with 0 data engineers

The reading I'd take from this is that the "expensive" SIEM option turned out cheaper once total cost of ownership took in the compliance risk, the team-capacity constraint, and the timeline pressure, and Marcus's decision was driven by realistic team sizing (no data engineers available within the deadline) and by a non-negotiable regulatory threshold (sub-30-second detection) rather than by any technology preference.

**Path B Includes Optionality**: Marcus designed Splunk deployment to preserve future lakehouse migration:
- Export Splunk data to S3 in Parquet format (creates lakehouse-ready archive for compliance queries)
- Use Splunk for real-time detection ONLY (10-15% of total queries)
- Build Athena/Iceberg for historical compliance workloads when team capacity recovers (18-24 month roadmap)
- Total 3-year cost: schema-on-read SIEM $36M + future Athena $600K = $36.6M (vs the pure-SIEM $39M, vs Athena-only non-compliant)

**Evidence**: Staffing Calculator from the literature review (batch 3 FTEs minimum for lakehouse, streaming 9-11 FTEs), schema-on-read SIEM list pricing (modeled $11.4M/year for the 15 TB/day high-volume tier). Deployment-timeline figures are directional scenario assumptions, not a sourced Gartner rate.

## K.3 Priya's Multi-National SOC: Multi-Cloud Virtualization

Priya's organizational context and constraints, the final decision (Denodo Platform for global virtualization) with its rationale and cost breakdown, and the Architecture Decision Summary she put in front of the executive sponsors are in her variant summary in the handbook's variants chapter. This walkthrough picks up at the requirements mapping.

Priya is a composite teaching scenario, so the POC query timings, the Denodo and Starburst cost figures, the staffing counts, and the multi-year TCO and cost-comparison bands below are illustrative figures from the author's TCO model (Appendix A, Worksheet A.6) applied to an 18 TB/day multi-region profile, not a measured deployment. The Denodo licensing band is anchored to Denodo's public enterprise pricing as noted at the Evidence line; the per-vendor capability claims (Denodo query pushdown behavior, QRadar/Splunk/Sentinel API limits) are vendor representations at Tier C unless separately sourced.

### Requirements Mapping: The Decision Framework Applied

**Tier 1: Mandatory Requirements (Disqualification Criteria)**

- **Multi-cloud query federation** across AWS + Azure + GCP + on-prem for unified visibility:
- A single SQL query has to return results from all cloud providers and on-premises systems
- Analysts cannot manually query 8 different platforms (the current painful reality)
- Platforms requiring separate instances per cloud (BigQuery GCP-only, Redshift AWS-only) fail here

- **Data-sovereignty compliance**, EU data staying in the EU, China in China, and so on:
- Zero cross-border data movement for raw security events
- Query results (aggregated, anonymized) can cross borders for global threat analysis
- Platforms requiring data consolidation into a central repository (Splunk, Snowflake ingestion) fail here

- A zero-data-movement architecture, query in place with no replication:
- Regional Splunk, QRadar, Sentinel stay operational (cannot force migration)
- The platform layers on top, querying existing systems via APIs or federation
- Platforms requiring ETL into new storage fail here (the operational disruption is unacceptable)

- Heterogeneous source integration, Splunk + QRadar + Sentinel + raw logs + cloud-native:
- This means multiple SIEM platforms with proprietary schemas, not just multiple clouds
- Platforms supporting only homogeneous sources (Iceberg-only, Delta-only, relational-only) fail
- Must query Splunk's proprietary format, QRadar's DB2 database, Sentinel Log Analytics, and S3 Parquet simultaneously

- A SQL query interface, given varying analyst skill levels (junior to senior, different tools):
- Standard ANSI SQL required (the most universal skill)
- Proprietary query languages (Splunk SPL-only, KQL-only) fail, because analysts cannot learn 8 different languages

- Minimal regional IT disruption, since the central team cannot mandate technology changes:
- Regional IT teams must see value, not a central mandate imposing work
- Platforms requiring regional infrastructure deployment (self-managed clusters, agents, data collectors) fail unless adoption is voluntary
- API-based integration preferred (no regional changes required)

**Tier 2: Strongly Preferred (3× Scoring Weight)**

- A **virtualization layer** (3 points), purpose-built data virtualization rather than query federation:
- True virtualization (Denodo-style): an abstraction layer with query pushdown, result merging, caching
- Query federation (Trino-style): distributed SQL across connectors
- Both acceptable; virtualization scores 3 (mature), federation scores 2 (emerging)

- Centralized governance (3 points): unified RBAC, audit trail, compliance reporting
- Central control over who accesses what data across all regions
- Audit trail: "Show all queries accessing China employee data for compliance review"
- Platforms with basic access control score 1, comprehensive governance score 3

- Low operational overhead (3 points), since there are 0 central data engineers available:
- Managed service mandatory (no infrastructure for Priya's team to operate)
- Regional infrastructure optional if voluntary (cannot mandate)
- Self-managed platforms score 0, partially managed score 2, fully managed score 3

- Incremental adoption (3 points), starting small and expanding region-by-region:
- Cannot deploy globally day-1 (organizational change management)
- Must prove value in 1-2 regions, then expand based on success
- Platforms requiring all-or-nothing deployment score 0, incremental score 3

**Tier 3: Nice to Have (Tiebreaker)**

- Real-time streaming: Batch acceptable for global threat hunting (regional SIEMs handle real-time detection)
- Advanced analytics: ML/AI regional responsibility, not central platform feature
- Cost optimization: Visibility prioritized over cost (compliance-driven, not cost-driven decision)

**Organizational Constraints (Override Technical Evaluation)**

- **Team capacity: 0 central data engineers** → Managed service non-negotiable, no infrastructure to maintain
- **Regulatory: Multi-region data sovereignty** → Data virtualization approach required, consolidation illegal
- **Political: Regional autonomy** → Cannot mandate tech stack changes, must demonstrate value for voluntary adoption
- **Budget: $4.5M total** → Split central platform ($1.5M Priya controls) + regional operations ($3M regional IT allocates if they see value)

### Vendor Filtering Process

**Tier 1 Filtering Results**

From 83-vendor landscape:

✗ **Eliminated: 71 vendors**

- **Data consolidation architectures** (32 vendors): Splunk (ingest to Splunk Cloud), Snowflake (load data to Snowflake), Databricks (Delta Lake ingestion), Dremio (Iceberg ingestion), all of which require data movement and violate zero-movement + data sovereignty requirements
- **Single-cloud focused** (16 vendors): AWS Athena (AWS-only without complex federation), Azure Synapse (Azure-only), BigQuery (GCP-only), which violate multi-cloud requirement
- **Homogeneous source requirement** (14 vendors): Iceberg-only platforms (cannot query Splunk), Delta-only platforms (cannot query QRadar DB2), relational-only (cannot query Sentinel Log Analytics), which violate heterogeneous integration
- **High operational overhead** (9 vendors): Self-managed Trino federation (requires regional cluster deployment), Apache Drill (complex distributed setup), custom Presto (operational burden), which violate zero central data engineers constraint

✓ **Advanced to Tier 2: 12 vendors**

- Denodo Platform (purpose-built data virtualization, 25-year history, multi-cloud, heterogeneous sources, enterprise managed)
- Starburst Galaxy (Trino federation, multi-cloud connectors, managed service, heterogeneous via connectors)
- Dremio Cloud (federation capability, limited virtualization, managed, API connectors possible)
- IBM Cloud Pak for Data (data virtualization module, multi-cloud, enterprise support)
- Apache Drill (open-source federation, SQL on anything, self-managed)
- [Plus 7 others with federation/virtualization capability]

**Tier 2 Scoring Matrix**

| Vendor Solution | Virtualization Layer (3 pts) | Centralized Governance (3 pts) | Low Overhead (3 pts) | Incremental Adoption (3 pts) | **Weighted Score** |
|-----------------|----------------------------|------------------------------|-------------------|----------------------------|-------------------|
| **Denodo Platform** | ✓✓ Native virtualization (6 pts) | ✓ RBAC + audit + compliance (3) | ✓ Fully managed (3) | ✓ API-based, region-by-region (3) | **45 points** |
| **Starburst Galaxy** | ✓ Trino federation (3) | ✓ RBAC, limited audit (3) | ✓ Fully managed (3) | ⚠ Requires connector setup per region (2) | **33 points** |
| **Dremio Cloud** | ⚠ Limited virtualization, federation via reflections (2) | ✓ RBAC (3) | ✓ Fully managed (3) | ✓ API federation possible (3) | **33 points** |
| **IBM Cloud Pak** | ✓ Virtualization module (3) | ✓ Enterprise governance (3) | ⚠ Managed but complex setup (2) | ⚠ Requires regional deployment (1) | **27 points** |
| **Apache Drill (OSS)** | ✓ Schema-free federation (3) | ⚠ Basic ACLs (1) | ✗ Self-managed (0) | ⚠ Complex multi-region setup (1) | **15 points** |

**Finalists** (Top 2 by weighted score):

1. **Denodo Platform** (45 points): Purpose-built virtualization, mature governance, managed service, incremental adoption via APIs
2. **Starburst Galaxy** (33 points): Modern Trino federation, managed service, good multi-cloud support but requires more regional coordination

### POC Evaluation

**POC Design (90-Day Multi-Region Evaluation)**

Priya's POC tested data virtualization across heterogeneous platforms in realistic compliance scenario:

**Test scope**: 3 regions (US/Splunk on AWS, EU/Sentinel on Azure, APAC/QRadar on GCP)
**Data sources**: Splunk API (Americas 5 TB/day), Azure Sentinel API (EMEA 2 TB/day), QRadar API (APAC 3 TB/day)

**Success criteria**:
1. **Unified query**: Single SQL query returning results from all 3 regional SIEMs (different vendors, different clouds)
2. **Data sovereignty**: EU data never leaves EU datacenter, only query results (aggregated) cross borders
3. **Performance**: <2 minutes for cross-region threat hunt (acceptable for global incident response)
4. **Zero disruption**: No changes required to regional Splunk/Sentinel/QRadar deployments

**POC Results: Denodo Platform**

✓ **Unified query demonstrated**:

```sql
-- Global threat hunt: Single SQL query across Splunk + Sentinel + QRadar
SELECT
  region,
  COUNT(DISTINCT user_id) as affected_users,
  COUNT(*) as suspicious_events,
  ARRAY_AGG(DISTINCT source_ip) as attacker_ips
FROM denodo.global_security_events_vw  -- Virtual view federating all regional SIEMs
WHERE event_type IN ('brute_force_attempt', 'credential_stuffing', 'account_takeover')
  AND timestamp >= CURRENT_TIMESTAMP - INTERVAL '24' HOUR
  AND confidence_score > 0.8
GROUP BY region
ORDER BY suspicious_events DESC;

-- Denodo execution plan (query pushdown + result merge):
-- 1. Parse query, identify data sources (Splunk API, Sentinel API, QRadar API)
-- 2. Push WHERE clause to each regional Denodo instance
--    - Americas Denodo: Query Splunk API with event_type filter
--    - EMEA Denodo: Query Sentinel API with event_type filter
--    - APAC Denodo: Query QRadar API with event_type filter
-- 3. Each regional Denodo returns aggregated results (not raw events)
-- 4. Global Denodo merges results, executes final GROUP BY
-- 5. Return unified results to analyst
```

**Result**: Single query, no manual coordination across 3 regional teams, 8 different platforms

✓ **Data sovereignty compliance validated**:

**How Denodo ensures compliance**:
1. **Query pushdown**: Denodo sends query logic to regional instance (WHERE clause, GROUP BY), not "send all data to central location"
2. **Regional execution**: EU Denodo queries Sentinel in Azure EU region, so data never leaves EU
3. **Aggregated results only**: Regional Denodo returns summarized data (COUNT, ARRAY_AGG), not raw events with EU employee PII
4. **Cross-border transfer**: Only aggregated results cross borders (e.g., "152 events from EU region" not "152 events with usernames/IPs/details")

**GDPR compliance validated**: EU data processing occurs in EU region (Azure EMEA), only statistical aggregates cross to US for global view (no personal data transfer)

✓ **Performance: 45-90 seconds for cross-region hunt**

Performance breakdown:
- API latency (Splunk/Sentinel/QRadar response): 20-40 seconds (depends on source SIEM load)
- Denodo query pushdown + execution: 10-20 seconds
- Result merging and aggregation: 5-10 seconds
- Network latency (cross-region): 10-20 seconds
- **Total**: 45-90 seconds

**Performance trade-off reality**:
- Native regional SIEM query (Splunk-only, US-only): 10-20 seconds
- Denodo single-region query (US Splunk via Denodo): 15-30 seconds (1.5× overhead, acceptable)
- Denodo cross-region query (US + EU + APAC): 45-90 seconds (2-4.5× overhead, acceptable for global visibility)

**POC benchmark queries with timing**:

| POC Query | Scope | Denodo Result | Native SIEM Equivalent |
|-----------|-------|---------------|----------------------|
| Brute force global summary (24h) | 3 regions, ~500K auth events | 52 seconds | N/A (no cross-region capability) |
| Compromised credential correlation (user in EU, login from APAC) | 2 regions, 48h window | 38 seconds | Manual: 2+ hours coordination between SOC teams |
| Privileged access audit (all global admins, 30 days) | 3 regions, ~12K admin events | 1 min 24 sec | Manual: 4-6 hours per region, 3 separate reports |
| Single-region deep forensic (US Splunk, 90-day threat hunt) | 1 region, ~45 TB | 28 seconds | Splunk native: 18 seconds (1.6× overhead) |

The honest comparison Priya's team drew from this is that the cross-region queries are not fast by Splunk standards, but they replace a process that was previously impossible, coordinating three SOC teams across time zones, manually exporting CSV files, and hoping the field names line up, so the real baseline for the 52-second query is not a faster query, it is "we have never been able to do this at all."

The POC surfaced three lessons worth carrying into the decision. The first is that cache configuration matters more than it looks: Denodo's result caching, on a 30-60 second TTL, made repeated analyst queries 3-5× faster on a cache hit, and during the POC 40% of follow-up queries hit cache, pulling the average response time for an iterative investigation down from 52 seconds to 22. The second is that connector tuning is real work that a vendor demo hides; QRadar's API returned events in a different timestamp format than Splunk and Sentinel, and Priya's team spent three days in Denodo's VQL (Virtual Query Language) normalizing timestamps across sources, a one-time cost that would never show up in a sales POC. The third is that regional IT buy-in was easier than expected, precisely because Denodo connected through the existing APIs with no change to regional infrastructure, so the regional teams approved the POC in a single meeting once they understood there were no agents, no forwarders, and no firewall changes to absorb.

✓ **Zero regional disruption**:
- Denodo connects to existing Splunk/Sentinel/QRadar via REST APIs
- No agents to deploy, no log forwarders to configure, no data collectors to manage
- Regional IT teams experience no change (Splunk continues operating exactly as before)
- Regional SOC analysts continue using local Splunk/Sentinel/QRadar for daily operations
- Only global security architects use Denodo for cross-region investigations

**POC Results: Starburst Galaxy (Trino Federation)**

✓ **Unified query possible**: Trino connectors for Splunk, Sentinel, Azure Data Lake, S3

⚠ **Data sovereignty complexity**:
- Trino federation executes in Starburst cluster (single region deployment)
- To ensure GDPR compliance: Deploy separate Starburst clusters per region (EU cluster for EU data, US cluster for US data)
- Cross-region query requires Starburst cluster-to-cluster communication (added operational complexity)
- More complex than Denodo's regional query pushdown model

⚠ **Performance: 60-120 seconds** (slower than Denodo)
- Trino connector overhead + data format translation
- Splunk API → Trino row format → query execution → result format
- Additional translation layer vs Denodo's optimized API integration

⚠ **Regional disruption**: Requires SIEM database access or S3 export
- Splunk connector needs Splunk database access (expose internal DB to Trino, a security concern)
- Alternative: Export Splunk logs to S3 (requires regional IT effort to maintain export pipeline)
- Regional IT teams resist: "We're already running Splunk, why add S3 export complexity?"

✓ **Cost: $1.2M/year** (lower than Denodo)
- Starburst Galaxy license: $800K/year (multi-cloud federation tier)
- Infrastructure (regional clusters): $300K/year (AWS + Azure + GCP)
- Data transfer: $100K/year (cluster-to-cluster communication)

**Cost vs capability trade-off**: 34% cheaper than Denodo ($1.2M vs $1.8M) but higher operational complexity and regional disruption

On these results Priya selected the Denodo Platform for global virtualization; the five-point decision rationale and the $1.8M/year cost breakdown are in her variant summary in the handbook's variants chapter.

### Architecture Pattern and Performance Trade-Offs

**Denodo Deployment Architecture**:

```
                    ┌─────────────────────────────────────┐
                    │  Global Denodo Platform (US AWS)   │
                    │  - Unified SQL interface            │
                    │  - Centralized RBAC & governance    │
                    │  - Cross-region query coordination  │
                    │  - Audit trail & compliance reports │
                    └─────────────────────────────────────┘
                              │           │           │
                              ▼           ▼           ▼
               ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
               │ Americas Regional│  │  EMEA Regional   │  │  APAC Regional   │
               │     Denodo       │  │     Denodo       │  │     Denodo       │
               │   (AWS US East)  │  │  (Azure EU West) │  │ (GCP Singapore)  │
               └──────────────────┘  └──────────────────┘  └──────────────────┘
                        │                      │                      │
                        ▼                      ▼                      ▼
              ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
              │  Splunk (5TB/day)│  │ Sentinel (2TB/day)│  │ QRadar (3TB/day) │
              │   + AWS S3 logs  │  │  + Azure Blob    │  │   + GCS logs     │
              └──────────────────┘  └──────────────────┘  └──────────────────┘
```

**Cross-Region Query Flow**:

1. **Analyst submits query** to Global Denodo (US): "Show brute force attempts globally in last 24 hours"

2. **Global Denodo parses query**, identifies required data sources: Americas Splunk, EMEA Sentinel, APAC QRadar

3. **Query pushdown to regional Denodo instances**:
   - Send query logic (WHERE event_type = 'brute_force', timestamp > -24 hours) to each regional Denodo
   - Do NOT send "give me all your data" (that would violate data sovereignty)

4. **Regional execution** (in parallel):
   - Americas Denodo → Queries Splunk API (within AWS US region, no data movement)
   - EMEA Denodo → Queries Sentinel API (within Azure EU region, EU data stays in EU)
   - APAC Denodo → Queries QRadar API (within GCP APAC region, APAC data stays in APAC)

5. **Aggregated results return** to Global Denodo:
   - Americas: 324 events, 45 affected users, [list of source IPs]
   - EMEA: 152 events, 28 affected users, [list of source IPs]
   - APAC: 89 events, 12 affected users, [list of source IPs]
   - **Raw events never cross borders** (only statistical aggregates)

6. **Global Denodo merges results**, executes final aggregation:
   - Total: 565 events, 85 affected users
   - Geographic distribution shown
   - Compliance: No GDPR/China law violation (aggregates only crossed borders)

**Performance Trade-Off Documentation**:

| Query Type | Native SIEM | Denodo Single-Region | Denodo Cross-Region | Performance Overhead |
|------------|-------------|---------------------|-------------------|---------------------|
| **Regional query** (Splunk US only) | 10-20 sec | 15-30 sec | N/A | 1.5× (acceptable) |
| **Cross-region query** (US + EU + APAC) | Not possible (manual coordination) | N/A | 45-90 sec | First time capability (no baseline to compare) |
| **Dashboard refresh** (regional metrics) | 5-10 sec | 12-25 sec | N/A | 2-2.5× (acceptable for 5-min refresh) |
| **Compliance audit** (7-year historical, multi-region) | Hours (manual per region) | N/A | 4-8 min | 10-20× faster than manual |

**When is 2-4.5× overhead acceptable?**

✓ **Acceptable use cases** (Denodo's strengths):
- Global threat hunting: Cross-region APT investigation (no alternative exists, manual coordination takes hours)
- Compliance audits: Multi-region access reviews (Denodo 8 minutes vs manual 4-6 hours per region)
- Executive dashboards: Global security posture (refresh every 15 minutes, 90-second query acceptable)

✗ **Unacceptable use cases** (use regional SIEMs instead):
- Real-time alerting: <30 second detection requirement (regional Splunk/Sentinel handle this, 10-20 sec native)
- High-frequency queries: Analyst running 100+ queries/day (use regional SIEM for regional investigations, Denodo for cross-region only)
- Forensic deep-dive: Retrieving 50+ fields for single event (regional SIEM provides better performance and full field access)

Priya's usage guidance to the SOC analysts, which followed directly from that split, is in her variant summary in the handbook's variants chapter.

**Cost Comparison vs Alternatives**:

| Approach | Description | Annual Cost | Performance | Data Sovereignty | Regional Disruption |
|----------|-------------|-------------|-------------|------------------|-------------------|
| **Denodo Virtualization** (selected) | API-based federation, query pushdown | $1.8M/year | 45-90 sec cross-region | ✓ Compliant (query pushdown) | ✓ Zero (API-only) |
| **SIEM Consolidation** (schema-on-read SIEM global) | Migrate all regions to a single schema-on-read SIEM cloud | $8.5M/year | 10-20 sec (native) | ✗ Violates GDPR, China law | ✗ High (force migration) |
| **Lakehouse Federation** (Iceberg + Trino multi-cloud) | Export all SIEMs to Iceberg, Trino federation | $2.1M/year | 60-120 sec cross-region | ⚠ Complex (requires regional S3 export) | ⚠ Medium (S3 export pipelines) |
| **Manual Coordination** (status quo) | Analysts query each SIEM separately, manual correlation | $0 new cost | 5-10 min per region (4-6 hours for all regions) | ✓ Compliant (no automation) | ✓ Zero (no changes) |

**Denodo value proposition**: $1.8M/year to gain first-time capability (unified cross-region visibility) without data sovereignty violations or regional disruption. Alternative approaches either violate compliance (consolidation), create operational burden (lakehouse export), or provide no improvement (manual status quo).

**What Denodo Does NOT Solve**:

**1. Performance optimization**: Virtualization inherently slower than native storage

Denodo adds 50-200% latency overhead (1.5-3× slower than querying data directly). This is architectural reality of virtualization, since the query must traverse abstraction layer, API calls, data format translation.

**Mitigation**:
- Denodo caching: Frequently-run queries cached for 30-60 seconds (materialized results, no API call on cache hit)
- Materialized views: Pre-computed aggregations for dashboards (refreshed every 5-15 minutes, dashboard queries instant)
- Selective use: Cross-region queries use Denodo (no alternative), regional queries use native SIEM (better performance)

**When overhead unacceptable**: Real-time detection, high-frequency analyst queries → Use regional SIEMs, not Denodo

**2. Real-time streaming**: Denodo batch queries only (no real-time correlation across regions)

Denodo queries APIs on-demand (when analyst submits SQL). Cannot correlate real-time events across regions: Americas authentication failure + EMEA privilege escalation + APAC data exfiltration within 30-second window.

**Reality**: Real-time detection remains regional responsibility
- Regional Splunk/Sentinel/QRadar handle real-time correlation (within their region, <30 second latency)
- Denodo for historical threat hunting only (cross-region investigation after alert from regional SIEM)
- No vendor currently solves real-time cross-region correlation with data sovereignty compliance (would require streaming data cross-border, illegal under GDPR/China law)

**3. Source heterogeneity limits**: Denodo only as good as source API quality

Denodo queries regional SIEMs via APIs:
- **QRadar API limitation**: Only 90 days queryable via API (older data in DB, no API access), so Denodo cannot query QRadar data >90 days
- **Splunk API rate limits**: 50 requests/second max, so Denodo queries throttled under high analyst load
- **Sentinel API latency**: Variable 1-5 second response time (Azure Load), so Denodo performance depends on Sentinel backend

**Mitigation**: Hybrid architecture
- **High-value sources**: Deploy S3/Blob export pipelines (regional IT voluntary), giving better performance than API and no rate limits
- **Low-value sources**: API-only (acceptable performance for infrequent queries)
- **Example**: Americas deploys Splunk → S3 export (improves Denodo query performance from 40 sec to 15 sec for US data), APAC keeps QRadar API-only (queries infrequent, export pipeline not justified)

**4. Cost structure**: Per-connector + per-user licensing (not consumption-based)

Denodo pricing: $1.2M/year for 3 regions, 50 users, 8 data source connectors

- Small queries pay same as large queries (not Athena-style $5/TB scanned)
- Adding 4th region: +$250K/year (regardless of query volume)
- Flat cost structure benefits high-query-volume use cases, penalizes low-volume

**Cost reality check**:
- **Denodo**: $1.8M/year for 18 TB/day federated access = $100/TB/year
- **SIEM consolidation**: $8.5M/year = $472/TB/year (4.7× more expensive, but violates compliance)
- **Lakehouse (if consolidation were legal)**: $2.1M/year = $117/TB/year (slightly more expensive, requires regional disruption)

So Denodo comes out cost-effective against the alternatives that are actually compliant, and it only looks expensive when you compare it to consolidation, which is cheaper per terabyte but isn't legal under the data-sovereignty rules Priya has to satisfy.

The Architecture Decision Summary Priya put in front of the executive sponsors, naming what the organization gains and what it trades, is carried in her variant summary in the handbook's variants chapter.

### Staffing & Budget Reality Check: Data Sovereignty Virtualization

Priya's Denodo virtualization approach for EU/US/China data sovereignty represents the most complex staffing and budget scenario in the book, and the cost of multi-region security operations when regulatory compliance and political constraints drive the architecture works out roughly like this:

**Team Composition** (6-8 FTEs):
- 3 Data Engineers (Denodo virtualization layer configuration, per-region connector optimization, API integration, query pushdown tuning)
- 2 Platform Engineers (multi-region infrastructure coordination, performance monitoring, connector maintenance across 8 heterogeneous sources)
- 1.5-2.5 Security Engineers (regional detection logic coordination, cross-region threat hunting, compliance validation)
- 0.5 Data Governance Engineer (GDPR/CCPA/China Cybersecurity Law compliance, data residency validation, legal coordination)

**Annual Operational Budget**: $1.8M-2.2M
- Staffing: $1.3M-1.6M (6-8 FTEs × $191K average fully-loaded cost, including salary + benefits + overhead)
- Denodo Licensing: $1.2M/year (enterprise multi-region, 3 regions, 50 concurrent users, 8 data source connectors)
- Regional Infrastructure Coordination: $50K-80K/year (API access fees, regional S3/Blob export pipelines where deployed voluntarily)
- Professional Services: $150K-200K/year (Denodo optimization, connector tuning, performance troubleshooting)
- Training: $30K-50K/year (Denodo certifications, data sovereignty compliance, multi-cloud API integration)

**Implementation Timeline**: 6-9 months
- Month 1-3: Denodo platform deployment + API connector configuration for 3 regional SIEMs (Splunk, QRadar, Sentinel)
- Month 4-6: Cross-region query federation testing + GDPR/China law compliance validation with legal team + query pushdown optimization
- Month 7-9: Security use case migration (threat hunting playbooks adapted for federated queries) + analyst training + compliance audit documentation

**3-Year Total Cost of Ownership (TCO)**: $7.0M-8.8M
- Implementation: $1.2M-1.6M (one-time: 6-9 months × 6-8 FTEs, Denodo Professional Services, compliance validation)
- Operations: $5.4M-6.6M (3 years × $1.8M-2.2M annual operational budget)
- Denodo Licensing: $3.6M (3 years × $1.2M)
- **Note**: Denodo licensing included in operational budget above, not double-counted

**Comparison to Alternatives**:
- **SIEM Consolidation (schema-on-read SIEM cloud, global)**: $8.5M/year = $25.5M over 3 years (3× MORE expensive, but **violates GDPR and China Cybersecurity Law**, so not viable)
- **Lakehouse Federation (Iceberg + Trino multi-cloud)**: $2.1M/year = $6.3M over 3 years (20% CHEAPER, but requires regional S3 export pipelines = high political friction with autonomous regional IT teams, 6-12 month delays)
- **Manual Coordination (status quo)**: $0 new cost, but 4-6 hours per cross-region investigation (unacceptable operational burden, investigators abandon cross-region hunts)
- **Baseline batch lakehouse (single-region)**: $2.5M over 3 years for 2 TB/day (from practitioner tools)

**Why Priya's TCO is 3× higher than single-region baseline**: Multi-region complexity is exponential coordination overhead rather than just "multiply by 3 regions":
- Data governance: Full-time FTE for GDPR/CCPA/China law compliance (vs 0.2 FTE for single-region)
- Platform engineering: 2× FTEs coordinating across 15 autonomous IT teams (vs 1 FTE managing single environment)
- Denodo premium: Virtualization licensing ($1.2M/year) vs open-source Trino federation ($0 licensing, but requires regional data export buy-in)
- Political cost: API-only integration avoids regional disruption (avoiding 6-12 month negotiation delays worth $600K-1.2M in delayed value)

Data sovereignty changes the architecture economics from the ground up, and the thing driving the change is regulatory and political complexity rather than a technology problem, which is why it takes additional team capacity (6-8 FTEs against a 3.5 baseline) and premium tooling (Denodo at $1.2M/year against open-source alternatives) to satisfy legal and political constraints that a lakehouse consolidation cannot satisfy at any price.

Denodo earns the spend in an organization that has all three of these at once: multi-region data-sovereignty mandates, decentralized IT with genuine regional autonomy, and a real need for unified cross-region visibility. An organization missing those constraints should consolidate on a lakehouse (Iceberg + Athena/Dremio) instead and take the roughly 3× lower cost and the better performance that come with it.

**Evidence**: Staffing Calculator from literature review (batch 3.5 FTEs baseline, +2-3 FTEs for multi-region governance), Gartner (6-8 FTEs for multi-region data platform management), Denodo public enterprise pricing (validated $1.2M/year for multi-region deployment with 8 connectors).
