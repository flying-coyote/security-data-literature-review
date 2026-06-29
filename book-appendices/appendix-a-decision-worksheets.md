---
type: essay-draft
title: "Appendix A: Decision Worksheets — Security Data Platform Selection"
created: 2025-10-15
tags: [moar-book, decision-framework, vendor-evaluation, tco, worksheets]
---

# Appendix A: Decision Worksheets

**Purpose**: Actionable templates for applying the handbook's requirements framework and decision methodology to YOUR organization.

**How to use**: Print or copy these worksheets. Work through them with your stakeholder group (security leadership, SOC analysts, data engineering, compliance, finance). Your completed worksheets become your platform selection criteria.

---

## Worksheet A.1: Three-Tier Requirements Classification

**Instructions**: For each requirement listed, determine its tier (Mandatory/Strongly Preferred/Nice to Have). Add your organization-specific requirements to the bottom. Remember: Tier 1 = disqualification filter, Tier 2 = scoring multiplier, Tier 3 = tiebreaker only.

### Tier 1: MANDATORY Requirements (Disqualification Criteria)

Check all that apply. Any vendor missing even ONE Tier 1 requirement is immediately disqualified.

**Query Interface:**
- [ ] SQL (ANSI SQL standard, not proprietary SPL/KQL)
- [ ] Python/PySpark acceptable
- [ ] Proprietary query language acceptable (existing team trained)
- [ ] Other: ________________________________

**Deployment Model:**
- [ ] Cloud-only acceptable (no on-premises requirement)
- [ ] On-premises required (data sovereignty, air-gapped environment)
- [ ] Hybrid required (both cloud + on-prem unified architecture)
- [ ] Multi-cloud required (AWS + Azure + GCP)
- [ ] Specific cloud mandate: [ ] AWS [ ] Azure [ ] GCP

**Retention Requirements:**
- [ ] Minimum retention: _______ days hot (interactive query <10 sec)
- [ ] Minimum retention: _______ days warm (query <60 sec)
- [ ] Minimum retention: _______ years cold (queryable, not just archived)
- [ ] Query transparency (analysts don't specify tier, automatic routing)

**Compliance Mandates:**
- [ ] HIPAA (PHI data residency requirements)
- [ ] GDPR (EU data must remain in EU)
- [ ] PCI-DSS (cardholder data isolation)
- [ ] FINRA (7-year queryable audit trail)
- [ ] FedRAMP (US federal cloud authorization)
- [ ] SOC 2 Type II (annual audit compliance)
- [ ] ISO 27001 (information security standard)
- [ ] Data sovereignty: ________________________________
- [ ] Other: ________________________________

**Real-Time Detection:**
- [ ] Real-time required: <_______ seconds alert latency (e.g., <30 sec for SEC fraud detection)
- [ ] Batch acceptable: _______ minute latency tolerance (e.g., 5-15 min for threat hunting)
- [ ] Dual capability: Streaming (real-time) + batch (historical) in same platform

**Data Format:**
- [ ] Open table format required (Apache Iceberg, V3 spec, or Delta Lake; vendor-neutral migration path)
- [ ] Proprietary format acceptable (vendor lock-in tolerance)
- [ ] SQL-queryable format (not raw JSON/CSV without schema)

**Integration Requirements:**
- [ ] Must ingest: ________________________________ (list critical sources: EDR, SIEM, cloud logs)
- [ ] Must integrate with: ________________________________ (SOAR, ticketing, threat intel)
- [ ] API access required (REST API for custom integrations)

**Team Capacity:**
- [ ] Zero data engineers (SOC-analyst manageable platform only)
- [ ] 1-2 data engineers available (managed services preferred)
- [ ] 3-5 data engineers available (hybrid architecture acceptable)
- [ ] 5+ data engineers available (fully composable stack viable)

**Budget Constraint:**
- [ ] Annual budget: $____________ to $____________ (hard ceiling)
- [ ] Cost model preference: [ ] CapEx (on-prem purchase) [ ] OpEx (cloud subscription)
- [ ] Per-GB pricing unacceptable (exceeds budget at our volume)

**Enterprise Requirements:**
- [ ] 99.9% uptime SLA minimum
- [ ] 24/7 vendor support (phone + email)
- [ ] Multi-year commercial support commitment (not community-only OSS)
- [ ] Security certifications: [ ] SOC 2 [ ] ISO 27001 [ ] FedRAMP [ ] Other: ________

**Your Organization-Specific Tier 1 Requirements:**
- [ ] ________________________________
- [ ] ________________________________
- [ ] ________________________________

---

### Tier 2: STRONGLY PREFERRED Requirements (3× Scoring Weight)

These requirements heavily influence scoring but don't automatically disqualify. Platforms missing Tier 2 must have compensating strengths.

**Storage and Query:**
- [ ] Apache Iceberg table format (multi-engine, Apache governance)
- [ ] Delta Lake acceptable (Databricks ecosystem)
- [ ] Multi-engine query capability (swap Trino ↔ Dremio ↔ Athena without data migration)
- [ ] Federated query (query across SIEM, databases, data lake simultaneously)

**Schema Standardization:**
- [ ] OCSF normalization support (Open Cybersecurity Schema Framework, v1.x)
- [ ] Native OCSF integration (minimal transformation required)
- [ ] ETL/ELT-based OCSF transformation acceptable (dbt, Spark, custom)
- [ ] Schema evolution support (add fields without breaking queries)

**Performance Optimization:**
- [ ] Time-series partitioning (date-based partition pruning for 10-100× speedup)
- [ ] Columnar storage (Parquet/Arrow for high-cardinality filtering)
- [ ] Predicate pushdown (filter at storage layer, not query layer)
- [ ] Query caching (materialized views, reflections, accelerations)

**Operational Features:**
- [ ] Managed service option (reduce operational burden)
- [ ] Automated table maintenance (compaction, snapshot expiration, orphan cleanup)
- [ ] Monitoring and observability (query performance metrics, cost tracking)
- [ ] Multi-tenancy support (separate dev/test/prod environments)

**Cost Optimization:**
- [ ] Tiered storage lifecycle (hot/warm/cold automated transitions)
- [ ] Compression efficiency (ZSTD, Snappy, or vendor-optimized)
- [ ] Compute-storage separation (scale independently, shut down compute when idle)
- [ ] Pay-per-query pricing acceptable (vs. always-on cluster cost)

**Security and Governance:**
- [ ] Row-level security (filter data by user role)
- [ ] Column-level security (mask PII/PHI fields)
- [ ] Query audit logging (who ran what query when)
- [ ] Data lineage tracking (upstream/downstream dependencies)

**Your Organization-Specific Tier 2 Requirements:**
- [ ] ________________________________
- [ ] ________________________________
- [ ] ________________________________

---

### Tier 3: NICE TO HAVE Requirements (1× Scoring Weight, Tiebreaker Only)

Convenient but not decision-driving. Don't let Tier 3 features override Tier 1-2 evaluation.

**Advanced Features:**
- [ ] Built-in ML anomaly detection
- [ ] Native threat intelligence feeds (STIX/TAXII integration)
- [ ] Automated compliance reporting (SOC 2, PCI-DSS templates)
- [ ] Executive dashboard templates (security posture, KPIs)
- [ ] Mobile application (on-call incident response)

**Ecosystem Integrations:**
- [ ] SOAR platform integration (Splunk Phantom, Palo Alto XSOAR)
- [ ] Ticketing integration (Jira, ServiceNow)
- [ ] ChatOps integration (Slack, Teams notifications)
- [ ] SSO/SAML integration (Okta, Azure AD)

**Developer Experience:**
- [ ] Jupyter notebook integration (data science workflows)
- [ ] Git integration (version control for queries, dashboards)
- [ ] API-first design (programmatic access for automation)
- [ ] SDK availability (Python, Java, Go client libraries)

**Your Organization-Specific Tier 3 Requirements:**
- [ ] ________________________________
- [ ] ________________________________

---

## Worksheet A.2: Organizational Constraints Assessment

**Instructions**: Answer honestly. Team capacity and budget shape what's actually buildable, so they tend to decide the outcome more than abstract platform features do.

### Constraint 1: Team Skills and Capacity

**1. How many data engineers / platform engineers on your security team?**
- [ ] 0 engineers (security-focused team only: SOC analysts, security engineers)
- [ ] 1-2 engineers (small platform team, limited bandwidth)
- [ ] 3-5 engineers (moderate team, can manage hybrid complexity)
- [ ] 5+ engineers (large team, can support fully composable stack)

**2. What's their primary expertise?**
- [ ] Security/SOC background (strong domain knowledge, limited data platform experience)
- [ ] Data engineering background (strong platform skills, learning security context)
- [ ] Cloud infrastructure background (AWS/Azure/GCP expertise)
- [ ] Mixed team (diverse skills covering multiple areas)

**3. Can you hire specialized data engineering talent?**
- [ ] Yes, with budget allocated ($150K-$180K annual per engineer)
- [ ] Yes, but timeline is critical (6-12 month recruitment acceptable?)
- [ ] No—hiring freeze, budget constraints, or >12 month timeline unacceptable

**4. Operational burden tolerance:**
- [ ] Minimal (prefer managed SaaS, no cluster management)
- [ ] Moderate (can manage ONE complex system, not multiple)
- [ ] High (team can operate self-hosted Kafka, Spark, Trino, multiple systems)

**Constraint 1 Implication** (auto-filled based on answers):
- **0-1 engineers + minimal burden** → Managed SIEM or cloud-native fully managed (Athena, Sentinel, Dremio Cloud)
- **2-3 engineers + moderate burden** → Hybrid (managed ingestion + self-hosted query, or simplified stack)
- **3-5 engineers + high tolerance** → Self-hosted Iceberg + Trino + Spark, custom pipelines with commercial support
- **5+ engineers** → Any architecture viable (open source, commercial, bleeding-edge)

---

### Constraint 2: Budget and Cost Model

**1. Annual security data platform budget:**
- [ ] <$500K (cost-sensitive, traditional SIEM economically infeasible at volume)
- [ ] $500K-$2M (moderate budget, balance cost vs. capability)
- [ ] $2M-$10M (enterprise budget, cost important but not sole factor)
- [ ] $10M+ (large enterprise, cost less constrained—focus on capability/team fit)

**2. Cost model organizationally acceptable:**
- [ ] CapEx / On-premises (hardware purchase, depreciation, data center costs)
- [ ] OpEx / Cloud (monthly subscription, pay-as-you-go)
- [ ] Hybrid (mix of owned infrastructure + cloud services)

**3. CFO sensitivity:**
- [ ] Cost-sensitive ("How much does it cost?" leads every vendor conversation)
- [ ] Capability-focused ("Will it solve our problem?" leads, cost discussed after validation)
- [ ] Balanced (cost and capability weighted equally)

**4. Current spend (for migration scenarios):**
- [ ] Current SIEM: $____________/year
- [ ] Considering migration: [ ] Yes (justify with TCO) [ ] No (staying with incumbent)
- [ ] Acceptable ROI timeline: [ ] 1 year [ ] 2 years [ ] 3+ years

**Constraint 2 Implication**:
- **<$500K budget** → MOAr (Iceberg + OSS Trino) or cloud-native serverless (Athena)—traditional SIEM infeasible
- **$500K-$2M budget** → All options viable—decision shifts to team capacity, not cost
- **$2M+ budget** → Cost less constraining—focus on operational fit, vendor relationship strategy

---

### Constraint 3: Data Sovereignty and Compliance

**1. Data residency requirements:**
- [ ] GDPR (EU): Customer data must remain in EU data centers
- [ ] China: Data generated in China stays in China (localization laws)
- [ ] US Federal: FedRAMP, ITAR, or other federal data sovereignty
- [ ] Multi-region: Different data must stay in different regions (complex)
- [ ] None: No geographic restrictions on security data storage

**2. Can security data leave on-premises environment?**
- [ ] Yes / Cloud-first (security data can move to AWS/Azure/GCP)
- [ ] Hybrid (some data cloud-acceptable, some must stay on-premises—e.g., PHI, PCI)
- [ ] No / On-premises only (all security data must remain in owned data centers)

**3. Regulatory audit frequency:**
- [ ] Annual SOC 2 Type II (standard compliance, once yearly, predictable)
- [ ] Quarterly audits (financial services, healthcare—frequent, rigorous)
- [ ] Continuous / Real-time (federal, defense—ongoing audit trail, immutable logs)

**4. Immutability requirements:**
- [ ] Append-only logs required (cannot delete/modify historical events for compliance)
- [ ] Time-travel required ("show me data as of audit date October 1, 2024")
- [ ] Query-level audit trail (who queried what data when—for compliance evidence)

**Constraint 3 Implication**:
- **Multi-region sovereignty** → Denodo virtualization or regional Iceberg deployments (cannot consolidate to single cloud region)
- **On-premises required** → Self-hosted stack (Iceberg on MinIO, Trino on-prem) or traditional SIEM on-prem—cloud-native eliminated
- **High-frequency audits** → Iceberg snapshot isolation (immutable, versioned) or Splunk with comprehensive audit logging

---

### Constraint 4: Vendor Relationship Tolerance

**1. Existing vendor relationships influencing decision:**
- [ ] Splunk incumbent (5+ years deployment, institutional knowledge, existing contract)
- [ ] AWS commitment (AWS Enterprise Support, heavy AWS investment, prefer AWS-native)
- [ ] Microsoft E5 licensing (Office 365 E5 includes Sentinel—"free" SIEM economically attractive)
- [ ] Other cloud commitment: [ ] Azure [ ] GCP

**2. Vendor consolidation preference:**
- [ ] Prefer fewer vendors (limit vendor relationships for procurement simplicity)
- [ ] Prefer best-of-breed (multiple vendors acceptable if each excels at specific capability)
- [ ] No preference (agnostic, driven by technical merit)

**3. Open-source tolerance:**
- [ ] High / OSS-first (comfortable with Apache projects, community support, self-managed)
- [ ] Medium / OSS with commercial support (OSS acceptable if vendor provides support—Starburst for Trino, Dremio)
- [ ] Low / Commercial only (require vendor SLA, 24/7 support, legal accountability)

**4. Migration tolerance:**
- [ ] High (willing to migrate from incumbent SIEM if savings/capability justify—$500K-$2M migration cost acceptable)
- [ ] Medium (consider migration if payback <2 years)
- [ ] Low (prefer operational continuity over cost savings—migration risk > cost optimization)

**Constraint 4 Implication**:
- **Splunk incumbent + low migration tolerance** → Stay with Splunk (a large migration cost and a multi-quarter timeline plus operational risk; model your own migration figure with the A.6 Step 6 worksheet rather than assuming a fixed band here)
- **AWS-committed** → AWS-native solutions (Athena, EMR, Glue) with Iceberg for portability
- **High OSS tolerance** → Apache Trino + Iceberg self-hosted, full control
- **Low OSS tolerance** → Commercial platforms only (Dremio Cloud, Starburst Enterprise, managed SIEM)

---

## Worksheet A.3: Workload-to-Capability Mapping

**Instructions**: For each security workload your team performs, identify required platform capabilities. Mark workloads as Tier 1 (critical), Tier 2 (important), or Tier 3 (occasional).

### Workload 1: Real-Time Detection

**Workload Description**: Detect threats within seconds/minutes of occurrence (brute force, malware execution, data exfiltration)

**Workload Tier** (check one):
- [ ] Tier 1 (critical—regulatory mandate or operational requirement)
- [ ] Tier 2 (important—preferred but can tolerate 5-15 min delay)
- [ ] Tier 3 (occasional—batch detection acceptable)

**If Tier 1, required capabilities** (all must be supported):
- [ ] Streaming ingestion (Kafka, Flink, Spark Streaming—continuous event processing)
- [ ] Windowed aggregation (5-min, 15-min time-based grouping for counts/thresholds)
- [ ] Stateful processing (maintain baseline state: per-host/user behavior, known-good hashes)
- [ ] Low-latency alerting (<30 seconds from ingestion to notification)

**Candidate Platforms** (auto-filtered based on capabilities; the latencies in parentheses are illustrative architecture characterizations, not measured benchmark results — validate them in your own POC, Worksheet A.5):
- ✓ Splunk SIEM (real-time forwarding, SPL streaming, <1 min alert latency)
- ✓ Iceberg + Apache Flink (Kafka → Flink → Iceberg, <30 sec latency)
- ✓ ClickHouse (materialized views, streaming aggregation, <5 sec latency)
- ✗ AWS Athena batch (hourly/daily scheduled queries—disqualified for Tier 1 real-time)
- ⚠ Dremio + Iceberg (batch ingestion via Spark Streaming, 2-5 min Reflection refresh—marginal for Tier 1)

---

### Workload 2: Threat Hunting (Historical Deep Analysis)

**Workload Description**: Hunt for IOCs across 90 days, correlate multi-source events, filter high-cardinality fields

**Workload Tier**:
- [ ] Tier 1 (critical—primary SOC function)
- [ ] Tier 2 (important—weekly threat hunts)
- [ ] Tier 3 (occasional—ad-hoc investigations)

**If Tier 1, required capabilities**:
- [ ] Columnar storage (Parquet/Arrow—scan billions of rows for specific fields 10-100× faster than row storage)
- [ ] Partition pruning (date-based partitioning with metadata elimination—read only relevant days, not full 7-year table)
- [ ] Predicate pushdown (filter at storage layer: `WHERE command_line LIKE '%mimikatz%'` reads only matching files)
- [ ] Distributed MPP (massively parallel processing across 10-50 workers—<60 sec query on 3B rows)

**Candidate Platforms** (the timings noted are illustrative architecture characterizations, not measured benchmark results — validate in your own POC, Worksheet A.5):
- ✓ Trino + Iceberg (Parquet native, Iceberg metadata pruning, connector pushdown, MPP)
- ✓ Dremio + Iceberg (Arrow in-memory, Gandiva LLVM pushdown, Reflections, MPP)
- ⚠ Splunk (tsidx indexed but not columnar, time buckets, distributed search heads—acceptable but not optimized)
- ✗ PostgreSQL (row-oriented heap storage, no MPP—20-45 min queries on billions of rows—disqualified for Tier 1)
- ✓ AWS Athena + Iceberg (Parquet on S3, Iceberg metadata, Presto/Trino engine, serverless auto-scaling)

---

### Workload 3: Forensic Deep-Dive (Incident Reconstruction)

**Workload Description**: Retrieve every event for specific host/user/timeframe with 50+ fields, sub-second retrieval for recent data

**Workload Tier**:
- [ ] Tier 1 (critical—active incident response)
- [ ] Tier 2 (important—post-incident investigation)
- [ ] Tier 3 (occasional—historical forensics)

**If Tier 1, required capabilities**:
- [ ] Indexed point queries (fast retrieval by host_id, user_id, timestamp—not full-table scan)
- [ ] Row-level retrieval (return complete events with all 50+ fields, not just aggregated counts)
- [ ] Time-travel capability (query "as of" specific timestamp for compliance: "show me October 1 snapshot")
- [ ] Hot tier optimization (SSD/NVMe for 7-30 days—<1 sec query, vs. minutes for cold Glacier)

**Candidate Platforms**:
- ✓ Iceberg + Dremio (partition filters + Reflections for point queries, full row SELECT *, snapshot isolation, S3 Standard hot / Glacier cold)
- ✓ ClickHouse (primary key index, fast row retrieval, ReplacingMergeTree for manual snapshots, NVMe/SSD tiering)
- ✓ AWS Athena + Iceberg (partition pruning, full row SELECT *, Iceberg TIMESTAMP AS OF, S3 Standard query speed)
- ✓ Elasticsearch (inverted index for _id and term queries, document _source retrieval, hot/warm nodes—no native time-travel but custom snapshots)

---

### Workload 4: Compliance Retention (Long-Term Archival)

**Workload Description**: 7-year queryable retention, query transparency across tiers, immutable audit trail, cost-optimized cold storage

**Workload Tier**:
- [ ] Tier 1 (critical—regulatory mandate: SOC 2, HIPAA, FINRA)
- [ ] Tier 2 (important—business requirement)
- [ ] Tier 3 (occasional—rarely query old data)

**If Tier 1, required capabilities**:
- [ ] Multi-tier lifecycle policies (automated S3 Standard → Glacier transition, NVMe → HDD, policy-driven not manual)
- [ ] Cold storage queryability (query engine reads Glacier/cold tier—not "archived offline to tape")
- [ ] Immutable table format (versioned, append-only: Iceberg snapshots, Delta versions—compliance audit trail)
- [ ] Compression efficiency (ZSTD, Snappy codecs materially reduce cold-storage cost; the exact ratio is workload-dependent — measure it on your own data, and see the SDW Lab compression results in Appendix C/I for measured figures rather than relying on an illustrative one here)

**Candidate Platforms**:
- ✓ Iceberg + S3 (S3 lifecycle automated, Athena/Trino query Glacier slowly but functional, snapshot isolation immutable, Parquet codecs)
- ⚠ Splunk (archive to S3 separate from indexed, archived data NOT queryable via SPL—disqualified for "queryable 7-year retention")
- ✓ Delta Lake + Cloud (Azure/AWS/GCS lifecycle, Spark on cold tiers, versioned Delta transaction log, Parquet codecs)
- ⚠ ClickHouse (manual TTL policies, cold tier query slow without tier transparency, DELETE supported so not immutable by default—audit risk for compliance-first)

---

### Your Organization-Specific Workloads

**Workload 5**: ________________________________

**Workload Tier**: [ ] Tier 1 [ ] Tier 2 [ ] Tier 3

**Required Capabilities**:
- [ ] ________________________________
- [ ] ________________________________
- [ ] ________________________________

**Workload 6**: ________________________________

**Workload Tier**: [ ] Tier 1 [ ] Tier 2 [ ] Tier 3

**Required Capabilities**:
- [ ] ________________________________
- [ ] ________________________________

---

## Worksheet A.4: Vendor Filtering Matrix

**Instructions**: List all vendors under consideration. Apply Tier 1 filters first (disqualify any vendor missing even ONE Tier 1 requirement). Score remaining vendors on Tier 2 (3× weight) and Tier 3 (1× weight).

### Phase 1: Tier 1 Filtering (Disqualification Pass)

| Vendor/Platform | Tier 1 Req #1 | Tier 1 Req #2 | Tier 1 Req #3 | Tier 1 Req #4 | Tier 1 Req #5 | **Result** |
|-----------------|---------------|---------------|---------------|---------------|---------------|------------|
| Example: Splunk Enterprise | ✓ SQL (SPL) | ✓ Hybrid | ✓ 7-year | ✓ HIPAA | ✓ Real-time | ✓ **PASS** |
| Example: AWS Athena (batch) | ✓ SQL | ✓ Cloud | ✓ 7-year | ✓ HIPAA | ✗ Batch only | ✗ **FAIL** |
| _________________ | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| _________________ | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| _________________ | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| _________________ | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| _________________ | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| _________________ | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

**Tier 1 Result**: _______ vendors eliminated, _______ viable candidates proceed to scoring.

---

### Phase 2: Tier 2 Scoring (3× Weight)

For each Tier 2 requirement, score: 3 = fully supported, 2 = partially supported, 1 = workaround required, 0 = not supported. Multiply score by 3 (weight).

| Vendor/Platform | Tier 2 Req #1 (×3) | Tier 2 Req #2 (×3) | Tier 2 Req #3 (×3) | Tier 2 Req #4 (×3) | **Tier 2 Total** |
|-----------------|-------------------|-------------------|-------------------|-------------------|------------------|
| Example: Dremio Cloud | 3×3=9 (Iceberg) | 3×3=9 (Multi-engine) | 2×3=6 (OCSF via ETL) | 3×3=9 (Managed) | **33** |
| Example: Self-hosted Trino | 3×3=9 (Iceberg) | 3×3=9 (Multi-engine) | 1×3=3 (Custom OCSF) | 0×3=0 (Self-hosted) | **21** |
| _________________ | ___×3=___ | ___×3=___ | ___×3=___ | ___×3=___ | ______ |
| _________________ | ___×3=___ | ___×3=___ | ___×3=___ | ___×3=___ | ______ |
| _________________ | ___×3=___ | ___×3=___ | ___×3=___ | ___×3=___ | ______ |

---

### Phase 3: Tier 3 Scoring (1× Weight)

For each Tier 3 requirement, score: 1 = supported, 0 = not supported. Add directly (no weight multiplier).

| Vendor/Platform | Tier 3 Req #1 | Tier 3 Req #2 | Tier 3 Req #3 | Tier 3 Req #4 | **Tier 3 Total** |
|-----------------|---------------|---------------|---------------|---------------|------------------|
| Example: Dremio Cloud | 1 (ML via SageMaker) | 1 (Threat intel API) | 1 (Compliance templates) | 1 (Exec dashboards) | **4** |
| Example: Self-hosted Trino | 0 (No built-in ML) | 1 (API integration) | 0 (No templates) | 0 (Build custom) | **1** |
| _________________ | ___ | ___ | ___ | ___ | ______ |
| _________________ | ___ | ___ | ___ | ___ | ______ |
| _________________ | ___ | ___ | ___ | ___ | ______ |

---

### Phase 4: Final Scoring and Ranking

| Vendor/Platform | Tier 2 Score (3× weight) | Tier 3 Score (1× weight) | **Total Score** | **Rank** |
|-----------------|--------------------------|--------------------------|-----------------|----------|
| Example: Dremio Cloud | 33 | 4 | **37** | **#1** |
| Example: Self-hosted Trino | 21 | 1 | **22** | **#2** |
| _________________ | ______ | ______ | ______ | ______ |
| _________________ | ______ | ______ | ______ | ______ |
| _________________ | ______ | ______ | ______ | ______ |

**Top 3-5 Finalists** (proceed to POC evaluation):
1. ________________________________ (Score: ______)
2. ________________________________ (Score: ______)
3. ________________________________ (Score: ______)
4. ________________________________ (Score: ______)
5. ________________________________ (Score: ______)

---

## Worksheet A.5: POC Evaluation Criteria

**Instructions**: For each finalist, conduct 2-4 week proof-of-concept. Use YOUR actual security data (1-2 TB sample, 30-90 days). Evaluate against these criteria.

### POC Setup (Week 1)

**Data Preparation**:
- [ ] Identify 3-5 representative data sources (EDR, network logs, cloud logs, SaaS apps)
- [ ] Extract 30-90 day sample (1-2 TB total—enough to test performance, not full production)
- [ ] Anonymize PII/PHI if required for vendor POC environment
- [ ] Document data characteristics (volume, schema, cardinality, query patterns)

**Environment Setup**:
- [ ] Vendor provides POC environment (cloud sandbox or on-prem trial)
- [ ] Ingest sample data (test ingestion pipeline, transformation, table creation)
- [ ] Verify data accessibility (can analysts query data with familiar tools?)
- [ ] Baseline cost (track compute hours, storage GB, query costs for POC spend)

---

### POC Evaluation (Weeks 2-4)

**Criterion 1: Query Performance**

Test representative queries from each workload category:

| Query Type | Description | Target Latency | Vendor A Result | Vendor B Result | Vendor C Result |
|------------|-------------|----------------|-----------------|-----------------|-----------------|
| **Threat hunt** | Scan 90 days for IOC pattern (e.g., `command_line LIKE '%mimikatz%'`) | <60 seconds | ______ sec | ______ sec | ______ sec |
| **Forensic retrieval** | Point query: all events from host X, time Y-Z | <10 seconds | ______ sec | ______ sec | ______ sec |
| **Aggregate dashboard** | Failed logins by source IP, hourly, 30 days | <5 seconds | ______ sec | ______ sec | ______ sec |
| **Complex join** | Correlate process + network + file events (3-way join, 7 days) | <2 minutes | ______ sec | ______ sec | ______ sec |

**Performance Winner**: ________________________________ (fastest average across all query types)

---

**Criterion 2: Analyst Usability**

Have 2-3 SOC analysts use the platform for daily operations during POC. Survey results:

| Usability Factor | Rating Scale (1-5) | Vendor A | Vendor B | Vendor C |
|------------------|--------------------|----------|----------|----------|
| **Ease of learning** | 5 = intuitive (learned in 1 day), 1 = difficult (requires week+ training) | ___/5 | ___/5 | ___/5 |
| **Query interface** | 5 = SQL familiar, 1 = proprietary language barrier | ___/5 | ___/5 | ___/5 |
| **Investigation workflow** | 5 = natural (pivot, drill-down easy), 1 = clunky | ___/5 | ___/5 | ___/5 |
| **Dashboard creation** | 5 = self-service (analysts build own), 1 = requires data engineer | ___/5 | ___/5 | ___/5 |
| **Error messages** | 5 = helpful (actionable), 1 = cryptic ("query failed") | ___/5 | ___/5 | ___/5 |

**Analyst Feedback** (free-form):
- Vendor A: ________________________________________________________________
- Vendor B: ________________________________________________________________
- Vendor C: ________________________________________________________________

**Usability Winner**: ________________________________

---

**Criterion 3: Cost Projection**

Extrapolate POC costs to full production volume (actual daily ingest rate, target retention):

| Cost Component | Vendor A (monthly) | Vendor B (monthly) | Vendor C (monthly) |
|----------------|-------------------|-------------------|-------------------|
| **Ingestion** (GB/day × 30 days × $__/GB) | $__________ | $__________ | $__________ |
| **Storage** (Retention days × daily GB × $__/GB/month) | $__________ | $__________ | $__________ |
| **Compute** (Query engine cluster or per-query costs) | $__________ | $__________ | $__________ |
| **Support** (Enterprise SLA, training, professional services) | $__________ | $__________ | $__________ |
| **TOTAL MONTHLY** | $__________ | $__________ | $__________ |
| **ANNUAL** | $__________ | $__________ | $__________ |

**Cost Comparison to Current SIEM** (if migrating):
- Current annual cost: $__________
- Vendor A savings: $__________ (__________%)
- Vendor B savings: $__________ (__________%)
- Vendor C savings: $__________ (__________%)

**Cost Winner**: ________________________________ (lowest TCO for equivalent capability)

---

**Criterion 4: Integration and Operational Fit**

| Integration Factor | Vendor A | Vendor B | Vendor C |
|--------------------|----------|----------|----------|
| **Data source connectors** (EDR, cloud, SaaS—out-of-box vs. custom) | ___/10 supported OOTB | ___/10 | ___/10 |
| **SOAR integration** (Splunk Phantom, Palo Alto XSOAR, custom) | [ ] Native [ ] API [ ] None | [ ] Native [ ] API [ ] None | [ ] Native [ ] API [ ] None |
| **SSO/SAML** (Okta, Azure AD integration) | [ ] Yes [ ] No | [ ] Yes [ ] No | [ ] Yes [ ] No |
| **Monitoring/observability** (query performance metrics, cost tracking) | [ ] Built-in [ ] Third-party [ ] None | [ ] Built-in [ ] Third-party [ ] None | [ ] Built-in [ ] Third-party [ ] None |
| **Operational burden** (team estimate: hours/week for maintenance) | _____ hrs/week | _____ hrs/week | _____ hrs/week |

**Operational Fit Winner**: ________________________________

---

**Criterion 5: Vendor Support Experience**

Rate vendor support responsiveness during POC:

| Support Factor | Vendor A | Vendor B | Vendor C |
|----------------|----------|----------|----------|
| **Response time** (avg hours to first response) | _____ hours | _____ hours | _____ hours |
| **Resolution quality** (issues resolved vs. "won't fix") | ___/5 | ___/5 | ___/5 |
| **Documentation** (accuracy, completeness, examples) | ___/5 | ___/5 | ___/5 |
| **Community** (Slack, forums, GitHub responsiveness) | ___/5 | ___/5 | ___/5 |
| **Roadmap transparency** (feature requests, release schedule) | ___/5 | ___/5 | ___/5 |

**Support Winner**: ________________________________

---

### POC Final Recommendation

**Weighted Scoring** (adjust weights to match YOUR organizational priorities):

| Criterion | Weight | Vendor A Score | Vendor A Weighted | Vendor B Score | Vendor B Weighted | Vendor C Score | Vendor C Weighted |
|-----------|--------|----------------|-------------------|----------------|-------------------|----------------|-------------------|
| **Performance** | 25% | ___/100 | _____ | ___/100 | _____ | ___/100 | _____ |
| **Usability** | 20% | ___/100 | _____ | ___/100 | _____ | ___/100 | _____ |
| **Cost** | 30% | ___/100 | _____ | ___/100 | _____ | ___/100 | _____ |
| **Integration** | 15% | ___/100 | _____ | ___/100 | _____ | ___/100 | _____ |
| **Support** | 10% | ___/100 | _____ | ___/100 | _____ | ___/100 | _____ |
| **TOTAL** | 100% | | **_____** | | **_____** | | **_____** |

**POC Winner**: ________________________________ (highest weighted score)

---

**Final Recommendation to Executive Sponsor**:

Based on Tier 1 filtering (_______ vendors eliminated), Tier 2-3 scoring (top 3-5 finalists), and POC evaluation (performance, usability, cost, integration, support), we recommend:

**Selected Platform**: ________________________________

**Justification**:
- Meets all Tier 1 mandatory requirements (disqualification filters passed)
- Scored highest on Tier 2 strongly preferred capabilities (3× weighted)
- POC demonstrated ________________________________ (performance, usability, cost advantages)
- Aligns with organizational constraints: ________________________________ (team capacity, budget, compliance)

**Implementation Timeline**: _______ months (Pilot → Production → Optimization)

**Total Cost of Ownership**: $__________/year (vs. current $__________/year—$__________ savings, __________% reduction)

**Risk Mitigation**: ________________________________ (vendor lock-in prevention: open table format, SQL standard, multi-engine capability)

---

## How to Use These Worksheets

**Stakeholder Workshop** (recommended approach):
1. **Assemble team** (2-3 hour workshop): CISO, SOC leadership, analysts, data engineering, compliance, IT operations, CFO rep
2. **Complete Worksheets A.1-A.3** as group (requirements classification, constraints, workload mapping)
3. **Research vendors** individually (1-2 weeks): Each stakeholder researches 2-3 vendors against requirements
4. **Complete Worksheet A.4** as group (vendor filtering matrix—apply Tier 1 filters, score Tier 2-3)
5. **POC execution** (2-4 weeks): Top 3-5 finalists conduct proof-of-concept with YOUR actual data
6. **Complete Worksheet A.5** as group (POC evaluation—performance, usability, cost, integration, support)
7. **Final recommendation** to executive sponsor (CISO, CIO, CFO) with completed worksheets as evidence

**Solo Architect Approach** (if no stakeholder workshop possible):
1. Complete worksheets individually based on knowledge of organizational constraints
2. Validate assumptions with key stakeholders asynchronously (email, Slack, quick meetings)
3. Use worksheets as communication tool: "Here's my requirements analysis—do these Tier 1 mandatory requirements match your understanding?"
4. Iterate based on feedback, then proceed to vendor filtering and POC

---

## Worksheet A.6: TCO Calculator & Cost Analysis

**Purpose**: A Total Cost of Ownership (TCO) calculation methodology for comparing traditional SIEM vs. MOAr vs. hybrid architectures at YOUR specific data volume and retention requirements.

**Instructions**: Input your organization's actual data volume, retention requirements, and team capacity. Calculator provides annual TCO comparison across platform options.

---

### Step 1: Define Your Data Volume & Retention

**Daily Ingestion Volume**:
- Total security data ingestion: __________ GB/day (or __________ TB/day)
  - _Baseline calculation_: 10,000 employees × 20-200 GB/day/1000 users = 200 GB - 2 TB/day
  - _Cloud-heavy multiplier_: Traditional baseline × 1.5-3× if multi-cloud, Kubernetes, extensive SaaS
  - _Actual measurement_: Check current SIEM ingestion dashboard or pipeline throughput metrics

**Retention Tiers**:
- **Hot tier** (interactive query, <10 sec latency): __________ days (typical: 30-90 days)
- **Warm tier** (investigation query, <60 sec latency): __________ days (typical: 90-180 days, or 0 if not needed)
- **Cold tier** (compliance archive, queryable but slow): __________ years (typical: 1-7 years)

**Total Retention Volume Calculation**:
```
Hot Volume = Daily GB × Hot Days
Warm Volume = Daily GB × Warm Days
Cold Volume = Daily GB × 365 × Cold Years

Total Retention = Hot + Warm + Cold
```

**Example** (2 TB/day enterprise, 30 hot / 90 warm / 7-year cold):
- Hot: 2,000 GB/day × 30 days = 60,000 GB (60 TB)
- Warm: 2,000 GB/day × 90 days = 180,000 GB (180 TB)
- Cold: 2,000 GB/day × 365 × 7 = 5,110,000 GB (5.1 PB)
- **Total**: 5.35 PB retention

---

### Step 2: Traditional SIEM Cost Model

**SIEM Pricing Reality** (as of Q4 2025; verify current rates before procurement). The schema-on-read and Sentinel rates are the two that feed the model below and are anchored — the schema-on-read band against the G-Cloud 14 published list (see the anchor note after Step 2), Sentinel against Microsoft's public list (Sources, below). The Elastic and QRadar rows are directional vendor-shape figures (Tier C), included for orientation and not used in any calculation:

| SIEM Platform | Pricing Model | Cost Range (per GB/day) | 7-Year Retention Support |
|---------------|---------------|------------------------|-------------------------|
| **Schema-on-read SIEM** | Ingest volume licensing | $300-$400/GB/day/year (platform; +ES ~2×) — G-Cloud-14-anchored, see note after Step 2 | ⚠ Hot only (archive to S3 not queryable) |
| **Microsoft Sentinel** | Consumption (GB ingested + GB retained) | $2.96-$5.22/GB ingested, plus retention per GB-month (Microsoft public list, see Sources) | ✓ Cold tier queryable (slow) |
| **Elastic SIEM** | Self-hosted or cloud, node-based | $15K-$50K/month base + storage (directional, Tier C) | ⚠ Warm/hot only (cold archive manual) |
| **IBM QRadar** | EPS (events per second) licensing | 10,000 EPS = $80K-$150K/year (directional, Tier C) | ⚠ Hot only |

**Schema-on-Read SIEM Cost Calculation** (2 TB/day example):
- Base licensing: 2,000 GB/day × $300/GB/day/year = **$600,000/year**
- Hot retention only: 30-90 days (compliance gap for 7-year requirement)
- Archive to S3: Additional $7K/month S3 storage for 5.1 PB cold = $84K/year
- **Problem**: Archived data NOT queryable via Splunk SPL—requires separate tooling
- **Total**: $684K/year (but fails 7-year queryable retention requirement)

**Microsoft Sentinel Cost Calculation** (2 TB/day example; ingestion and retention priced separately):
- Ingestion (analytics tier, ~90 days included): 2,000 GB/day × 30 days × $2.96-$5.22/GB = **$178K-$313K/month** (~$2.1M-$3.8M/year) — the dominant, recurring charge
- Retention beyond the included window: the warm/cold archive accumulating toward 5.1 PB over 7 years is priced per GB-month at long-term/archive rates well below the ingestion rate (~$0.026-$0.05/GB/month), adding **~$130K-$255K/month** as it fills (~$1.6M-$3.1M/year at steady state)
- **Total**: roughly **$3.7M-$6.9M/year** as retention accumulates — expensive at scale, but driven by ingestion, not by re-charging accumulated storage at the ingestion rate

Traditional SIEM pricing breaks at petabyte scale. For 7-year compliance retention (these bands are model-derived from the discounted per-GB/day rates below — the G-Cloud anchor that follows grounds the Splunk platform floor, not the full blended band):
- **500 GB/day**: $365K-$1.1M/year (SIEM acceptable)
- **2 TB/day**: $1.5M-$4.4M/year (SIEM cost-prohibitive)
- **10 TB/day**: $7.3M-$22M/year (SIEM infeasible)

**Published-list anchor (UK G-Cloud 14).** These bands are grounded in Splunk's public-sector framework pricing. The G-Cloud 14 EMEA distributor schedule (April 2024) lists Splunk Cloud platform ingest on a declining per-GB/day curve, from $2,049/GB/day/year at 5-9 GB/day down to $793.50 at the 2,000-4,999 GB/day band (2 TB/day) and $764.75 above 5,000 GB/day, with the self-hosted Enterprise term license on a parallel curve ($598/GB/day/year at 2 TB/day). Splunk Enterprise Security, the correlation and detection-content layer an actual SOC runs, is a separate per-GB/day subscription on top, adding $448.50/GB/day/year at the 2 TB/day band, so two rates matter and they differ by roughly 2×. The platform-only schema-on-read baseline is $598-794/GB/day/year of published list at 2 TB/day, which after the 30-50% enterprise discounting that large multi-year Splunk contracts carry is the $300-400/GB/day/year this model uses, so the $600K above is the discounted-platform floor. The full SOC stack, platform plus Enterprise Security, lists near $1,240/GB/day/year, or roughly $620-870 once discounted, and that is the rate the worked MOAR-variant examples price.

Marcus's $12M renewal at 10-12 TB/day reconciles to the published list almost exactly, because Cloud platform ($764.75) plus Enterprise Security ($431.25) at the 5,000-9,999 GB/day band is $1,196/GB/day/year, and that times 10,000 GB/day is $11.96M. The Metropolitan Police's 2024 Splunk SaaS deal is a named instance of the discounting at work: the Directorate of Professional Standards bought Splunk through reseller CDW for £780K up front plus £1.774M over five years, locking a 10% discount for the five-year commitment against dollar-denominated list prices. The rate this cost model uses is therefore the conservative floor, platform-only and deeply discounted, sitting beneath a published curve whose full-stack list runs three to four times higher.

---

### Step 3: MOAr Cost Model

**Architecture**: S3/Blob storage + Iceberg table format + Query engine (Trino/Dremio/Athena) + Alerting (OSS or lightweight SIEM for hot tier only)

**Pricing currency**: cloud and vendor rates in this MOAr cost model are as of Q4 2025; verify current rates before procurement.

**Component Costs**:

**1. Storage (S3 tiered)**:
- Hot tier (S3 Standard): $0.023/GB/month
- Warm tier (S3 Standard-IA): $0.0125/GB/month
- Cold tier (S3 Glacier Flexible): $0.0036/GB/month

**2. Query Engine Options** (the Athena $/TB-scanned rate is AWS public list, see Sources; the cluster/managed monthly bands are directional model inputs, Tier C — they depend on your query frequency and node sizing, which the worksheet asks you to fill in):
| Engine | Deployment | Cost Model | Typical Monthly Cost (2 TB/day use case) |
|--------|-----------|------------|----------------------------------------|
| **AWS Athena** | Serverless | $5/TB scanned (AWS public list) | $5K-$15K/month (depends on query frequency) |
| **Trino (self-hosted)** | EC2/EKS cluster | Compute hours | $8K-$20K/month (r6i.4xlarge × 3-5 nodes; directional, Tier C) |
| **Dremio Cloud** | Managed SaaS | Compute hours + storage | $10K-$25K/month (standard tier; directional, Tier C) |
| **Starburst Enterprise** | Managed or self-hosted | Compute hours + support | $15K-$35K/month (enterprise support; directional, Tier C) |

**3. Ingestion Pipeline** (Cribl/Tenzir/OSS):
- See the handbook's pipeline cost comparison (Cribl/Tenzir/OSS)
- Typical: $1.1M-$2M/year (Cribl) or $330K-$720K/year (Tenzir) or $186K-$408K/year (OSS Logstash) for 10 TB/day
- For 2 TB/day: ~$220K-$400K/year (Cribl) or ~$66K-$144K/year (Tenzir)

**4. Lightweight SIEM for Real-Time** (optional, hot tier only; these hot-tier monthly bands are directional infrastructure estimates, Tier C):
- ClickHouse self-hosted: $3K-$8K/month (hot 30 days only, 60 TB)
- Elastic hot tier: $5K-$12K/month
- **OR** skip SIEM entirely, use Flink + Iceberg for streaming alerts

**MOAr Total (2 TB/day example)**:
```
Storage:
- Hot (60 TB): 60,000 GB × $0.023/GB/month = $1,380/month
- Warm (180 TB): 180,000 GB × $0.0125/GB/month = $2,250/month
- Cold (5.1 PB): 5,100,000 GB × $0.0036/GB/month = $18,360/month
Storage subtotal: $21,990/month = $264K/year

Query Engine (Athena serverless):
- 500 TB scanned/month (avg query workload) × $5/TB = $2,500/month = $30K/year

Pipeline (Tenzir):
- $66K-$144K/year (2 TB/day tier)

Real-Time Alerting (ClickHouse hot tier):
- $3K-$8K/month = $36K-$96K/year

TOTAL: $264K + $30K + $105K (midpoint) + $66K (midpoint) = $465K/year
```

**Savings vs. schema-on-read SIEM**: $684K - $465K = **$219K/year (32% savings)** (model-derived: both sides are computed from the rate assumptions above, not a measured invoice comparison)
**Savings vs. Sentinel**: ~$3.7M-$6.9M - $465K ≈ **$3.2M-$6.4M/year (88-93% savings)**

Savings increase with data volume and retention period because storage is a marginal cost in MOAr but a fixed license cost in SIEM.

---

### Step 4: Hybrid Architecture Cost Model

**Pattern**: Keep SIEM for real-time hot tier (30-90 days), use data lake for warm/cold (90 days - 7 years)

**Why Hybrid**:
- Organizational inertia (existing Splunk investment, trained analysts, operational continuity)
- Regulatory requirements (SEC <30 sec real-time detection, SIEM-proven compliance)
- Team capacity constraints (0-1 data engineers, cannot support full MOAr)

**Cost Model** (2 TB/day with 10:1 route-by-value):
```
Cribl Pipeline (route-by-value):
- High-value to SIEM (200 GB/day, 10% of volume): 200 GB/day × $300/GB/day/year = $60K/year
- Low-value to Lake (1,800 GB/day, 90% of volume): S3 storage only

SIEM (hot tier, 30 days, 200 GB/day only):
- Schema-on-read SIEM: $60K/year (10× cost reduction via route-by-value)

Data Lake (warm/cold, 1,800 GB/day full volume):
- Storage (30 days hot + 7 years cold): ~$180K/year
- Query engine: ~$30K/year
- Subtotal lake: $210K/year

Pipeline (Cribl Stream):
- $220K-$400K/year (2 TB/day tier) = ~$310K/year midpoint

TOTAL HYBRID: $60K (SIEM) + $210K (Lake) + $310K (Pipeline) = $580K/year
```

**Savings vs. Full SIEM**: $684K - $580K = **$104K/year (15% savings)**, and it solves the 7-year retention gap
**Savings vs. Sentinel**: ~$3.7M-$6.9M - $580K ≈ **$3.1M-$6.3M/year (84-91% savings)**

**When Hybrid Makes Sense**:
- Existing SIEM investment (sunk cost, but trained team)
- Real-time regulatory requirement (<30 sec, SIEM-proven)
- Team capacity 0-1 engineers (cannot support full MOAr complexity)
- See the variants chapter of the handbook (Chapter 6, "What good looks like") for the full hybrid approach

---

### Step 5: Cost Comparison Summary Table

The dollar bands in this table are outputs of the cost models in Steps 2-4, not measured invoices — every figure is computed from the rate assumptions above (the discounted G-Cloud-anchored Splunk floor, Microsoft's Sentinel list, AWS storage and Athena list, and the directional engine/pipeline inputs). Read them as a modeled comparison, and re-run the worksheet with your own rates before relying on any single number.

| Platform Architecture | 500 GB/day | 2 TB/day | 10 TB/day | 7-Year Retention Support | Team Capacity Required |
|-----------------------|------------|----------|-----------|-------------------------|------------------------|
| **Traditional SIEM (schema-on-read)** | $365K-$1.1M/year | $1.5M-$4.4M/year | $7.3M-$22M/year | ✗ Hot only (30-90 days) | 0 data engineers (SOC-managed) |
| **Traditional SIEM (Sentinel)** | $0.95M-$1.7M/year | $3.7M-$6.9M/year | $19M-$34M/year | ✓ Queryable (slow cold tier) | 0 data engineers (cloud-managed) |
| **MOAr (OSS)** | $180K-$280K/year | $265K-$470K/year | $548K-$848K/year | ✓ Full query transparency | 3-5 data engineers (self-hosted) |
| **MOAr (Cloud-Managed)** | $220K-$350K/year | $380K-$650K/year | $950K-$1.5M/year | ✓ Full query transparency | 1-2 data engineers (managed services) |
| **Hybrid (SIEM + Lake)** | $280K-$450K/year | $500K-$850K/year | $2M-$3.5M/year | ✓ Lake queryable, SIEM hot | 1-2 data engineers + SOC analysts |

**Reading the table**: the savings widen as volume grows, because in this model storage is a marginal cost for MOAr but a fixed license cost for the SIEM — the modeled gap is roughly 92-96% at 10 TB/day and 45-60% at 500 GB/day. The 7-year retention requirement is where the traditional SIEM tends to break, since it cannot economically hold petabyte-scale compliance data the way a tiered lake can. Team capacity shifts which row you land on: OSS is the cheapest but assumes 3-5 data engineers, while the cloud-managed option costs roughly 2× more and gets by with 1-2 engineers. The hybrid pattern sits in between at a modeled 15-30% savings versus a full SIEM, and it solves the retention gap while staying workable for a team with zero or one data engineer.

---

### Step 6: ROI Calculation & Payback Period

**Migration Cost** (if moving from incumbent SIEM to MOAr):
- Professional services / consulting: $150K-$500K (depends on complexity, 6-12 months timeline)
- Staff time (internal): 2-3 FTE × 6 months = $75K-$150K loaded cost
- Training (SOC analysts, SQL workshops): $20K-$50K
- **Total migration cost**: $245K-$700K (one-time)

**Annual Savings** (2 TB/day example, schema-on-read SIEM → MOAr):
- Current schema-on-read SIEM cost: $684K/year (hot only, archive gap)
- MOAr cost: $465K/year (full 7-year retention)
- **Annual savings**: $219K/year

**Payback Period** (using ~$450K, the midpoint of the $245K-$700K migration range):
- Migration cost ÷ Annual savings = $450K ÷ $219K ≈ **2 years payback** (roughly 1.1 years at the $245K low end, 3.2 years at the $700K high end)
- After payback, savings compound: Year 3 = $219K net savings, Year 4 = $219K, Year 5 = $219K
- **5-year TCO savings**: $219K × 5 - $450K ≈ **$645K cumulative** (at the midpoint migration cost)

**When ROI Justifies Migration**:
- Payback < 3 years (acceptable for most CFOs)
- Compliance gap solved (7-year retention economically feasible)
- Team capacity available (1-2 engineers minimum, or managed services)

**When NOT to Migrate** (stay with incumbent SIEM):
- Payback > 3 years (savings too small to justify disruption)
- Team capacity 0 engineers (no one to operate MOAr)
- Operational continuity critical (SEC real-time requirement, cannot tolerate migration risk)
- See the variants chapter of the handbook (Chapter 6, "What good looks like") for the "When Splunk Wins" case where staying with the incumbent is the valid approach

---

### Step 7: Hidden Costs & Considerations

**Pricing currency**: the hidden-cost rates below are as of Q4 2025; verify current rates before procurement.

**MOAr Hidden Costs**:
1. **Staff learning curve**: 2-day SQL workshop for SOC analysts ($5K-$15K training budget)
2. **Data engineering hiring**: $150K-$180K/year per engineer (if team capacity insufficient)
3. **Table maintenance**: Spark cluster for compaction, snapshot expiration ($3K-$8K/month ongoing)
4. **Monitoring/observability**: Query performance metrics, cost tracking tools ($2K-$5K/month)

**SIEM Hidden Costs** (rarely appear in initial vendor quotes):
1. **Professional services**: Annual health checks, tuning, optimization ($50K-$150K/year)
2. **Premium apps**: Enterprise Security, SOAR integrations, ML toolkit ($20K-$100K/year add-ons)
3. **Storage expansion**: Incremental licensing as data grows (10-30% annual growth common)
4. **Retention gap workarounds**: Separate archive solution if 7-year queryable required ($50K-$200K/year)

**Total Cost of Ownership Includes**:
- Platform licensing / infrastructure
- Storage (all tiers: hot, warm, cold)
- Compute (query engines, ingestion pipelines)
- Staff (data engineers, SOC analysts, training)
- Professional services (consulting, support, annual renewals)
- Integration costs (SOAR, threat intel, ticketing, SSO)
- **Migration cost amortized** (if switching platforms)

---

### Your TCO Calculation Worksheet

**Input Your Data**:
- Daily ingestion: __________ GB/day
- Hot retention: __________ days
- Warm retention: __________ days
- Cold retention: __________ years
- Current SIEM annual cost: $__________/year
- Team capacity: __________ data engineers available

**Pricing currency**: the unit rates in this worksheet are as of Q4 2025; verify current rates before procurement.

**Calculate MOAr Annual Cost**:
```
Storage Hot: (Daily GB × Hot Days) × $0.023/GB/month × 12 = $__________
Storage Warm: (Daily GB × Warm Days) × $0.0125/GB/month × 12 = $__________
Storage Cold: (Daily GB × 365 × Cold Years) × $0.0036/GB/month × 12 = $__________
Query Engine: (Choose Athena $30K-$50K or Trino $96K-$240K or Dremio $120K-$300K) = $__________
Pipeline: (See the handbook's pipeline cost comparison for Cribl/Tenzir/OSS costs at your volume) = $__________
Real-Time Alerting: (Optional ClickHouse $36K-$96K or skip) = $__________

TOTAL MOAr = $__________/year
```

**Calculate Savings**:
```
Annual Savings = Current SIEM Cost - MOAr Cost = $__________/year
Savings Percentage = (Savings ÷ Current Cost) × 100 = __________%

Migration Cost (one-time) = $__________
Payback Period = Migration Cost ÷ Annual Savings = __________ years

5-Year TCO Comparison:
- SIEM 5-year cost: Current Annual × 5 = $__________
- MOAr 5-year cost: (MOAr Annual × 5) + Migration = $__________
- 5-Year Savings: SIEM 5-year - Modern 5-year = $__________
```

**Decision Threshold**:
- ✓ **Proceed if**: Payback < 3 years AND 5-year savings > $500K AND team capacity ≥ 1 engineer
- ⚠ **Evaluate hybrid if**: Team capacity = 0 engineers OR payback 3-4 years OR migration risk high
- ✗ **Stay with SIEM if**: Payback > 4 years OR team capacity = 0 AND budget < $500K for managed services

---

**Cross-References**:
- **The manageability argument** (Chapter 1 of the handbook, "Manageability > extreme performance"): cost reality and the retention gap problem
- **The handbook's pipeline cost comparison**: Cribl/Tenzir/OSS
- **The variants chapter** (Chapter 6 of the handbook, "What good looks like"): the worked MOAR-variant TCO examples (Jennifer $380K/year platform + $200K Splunk, Marcus $2.9M/year modern stack vs $12M Splunk expansion, Priya $1.8M/year Denodo)
- **The variants chapter** (Chapter 6 of the handbook, "What good looks like"): when traditional SIEM wins despite higher cost
- **The modularity chapter** (Chapter 7 of the handbook, "Modularity: incremental modernization"): building the business case for the CFO stakeholder pitch

**Sources & Validation**:
- Microsoft Sentinel public pricing (2025): docs.microsoft.com/azure/sentinel/pricing
- Splunk pricing (validated against public list price + 30-50% enterprise discounting)
- AWS S3 pricing: aws.amazon.com/s3/pricing
- AWS Athena pricing: aws.amazon.com/athena/pricing
- TCO calculation based on AWS S3 pricing (2025) and schema-on-read SIEM list pricing (30-50% enterprise discount applied); the resulting reduction vs SIEM at 10 TB/day scale is a model-derived output of the Steps 2-5 comparison (large, in the high-double-digit percent range — see the Step 5 table and reading note for the band), not a measured invoice-to-invoice result

---

## Worksheet A.7: Stakeholder Workshop Participants

**Instructions**: Before you complete Worksheets A.1–A.3, confirm who is in the room. Use this table to check that every group whose concerns shape the requirements is represented. A requirements set assembled without one of these voices is the most common reason a platform decision gets overturned later.

| Stakeholder Group | Key Concerns | Must Participate? |
|-------------------|--------------|-------------------|
| **CISO / Security Leadership** | Risk reduction, compliance, budget | ✓ Required |
| **SOC Analysts** | Query usability, investigation workflow, training burden | ✓ Required |
| **Detection Engineers** | Rule development, integration capability, real-time performance | ✓ Required |
| **Compliance / Legal** | Retention requirements, data sovereignty, audit capability | ✓ Required |
| **Data Engineering Team** | Operational burden, technical feasibility, maintenance | ✓ Required (if exists) |
| **IT Operations** | Infrastructure, vendor relationships, procurement | ✓ Required |
| **CFO / Finance** | Total cost of ownership, budget constraints, ROI | ✓ Required |
| **CIO / CTO** | Cloud strategy alignment, enterprise architecture, vendor consolidation | ⚠ Recommended |

---

## Worksheet A.8: Initial Vendor Research Card

**Instructions**: Fill one card per vendor before you build the Worksheet A.4 filtering matrix. The card captures the at-a-glance facts — deployment model, pricing shape, company stage — that decide whether a vendor is even worth scoring.

```
Vendor: _______________________
Product: _______________________

Deployment Models: [ ] Cloud SaaS  [ ] Self-hosted  [ ] Hybrid
Pricing Model: [ ] Consumption  [ ] Flat license  [ ] Infrastructure-based
Estimated Annual Cost (for your scale): $__________
Company Stage: [ ] Public  [ ] Late-stage private  [ ] Startup (<3 years)
Enterprise Customers: [ ] 100+  [ ] 50-100  [ ] <50

Key Differentiators:
-
-

Potential Concerns:
-
-
```

---

## Worksheet A.9: Architecture Decision Record (ADR) Template

**Instructions**: Once you've selected a platform, capture the decision in a durable record. The ADR is what you hand to an architecture board, and the document that holds up when someone revisits the choice two years later. Fill in the bracketed sections.

```markdown
# Architecture Decision Record: Security Data Platform Selection

**Date**: YYYY-MM-DD
**Status**: Proposed / Accepted / Superseded
**Decision Makers**: [List stakeholders who approved]

## Context

[2-3 paragraphs explaining:
- Current security data challenge (volume, retention, cost, tools)
- Why change needed (Splunk expansion cost, compliance requirement, etc.)
- Organizational constraints (team capacity, budget, vendor relationships)]

## Decision

**Selected Platform**: [Vendor + Product]

**Annual Cost**: $__________
- Storage: $__________
- Compute/Query: $__________
- License: $__________
- Professional Services (Year 1): $__________

**Deployment Model**: [Cloud SaaS / On-premises / Hybrid]

**Implementation Timeline**: _____ months

## Requirements Analysis

**Tier 1 Mandatory Requirements Met**:
- ✓ [Requirement 1]
- ✓ [Requirement 2]
- ✓ [Requirement 3]
- ...

**Tier 2 Strongly Preferred (Weighted Score: ___ points)**:
- ✓ [Requirement achieved with 3 points]
- ⚠ [Requirement partially achieved with 1-2 points]
- ...

**Organizational Constraints Satisfied**:
- ✓ Budget: Within $__________ limit
- ✓ Team capacity: Operational burden fits ____ engineer capacity
- ✓ [Other constraints...]

## POC Results Summary

[Table comparing finalists with key metrics]

## Rationale

[3-5 paragraphs explaining WHY this platform won:
1. Primary advantage (cost, performance, operational simplicity, etc.)
2. How it beats alternatives on critical requirements
3. Organizational fit (team capacity, vendor relationships, strategic alignment)
4. Risk mitigation (vendor stability, open format, migration path)]

## Critical Limitations and Trade-Offs

**What This Architecture Does NOT Solve**:

1. [Limitation 1]: [Description]
   - **Mitigation**: [How you'll address this gap]

2. [Limitation 2]: [Description]
   - **Mitigation**: [How you'll address this gap]

**Trade-Offs Accepted**:
- [Trade-off 1]: Accepted [downside] to gain [benefit]
- [Trade-off 2]: Accepted [downside] to gain [benefit]

**Honest Expectation Setting**:
> "This architecture optimizes for [PRIMARY GOAL]. It does NOT provide [LIMITATIONS]. Organizations prioritizing [ALTERNATIVE GOAL] should evaluate [ALTERNATIVE PLATFORMS]."

## Alternatives Considered and Rejected

**[Alternative Platform 1]**: [Why rejected]
- [Specific reason it failed requirements or POC]

**[Alternative Platform 2]**: [Why rejected]
- [Specific reason it failed requirements or POC]

## Implementation Plan

**Phase 1** (Months 1-2): [Pilot deployment, training]
**Phase 2** (Months 3-4): [Production rollout, data migration]
**Phase 3** (Months 5-6): [Optimization, legacy SIEM sunset]

**Success Metrics**:
- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]

## Risks and Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | Low/Med/High | Low/Med/High | [Mitigation strategy] |
| [Risk 2] | Low/Med/High | Low/Med/High | [Mitigation strategy] |

## References

- POC evaluation results: [Link to detailed report]
- Vendor proposals: [Link to documents]
- Stakeholder workshop notes: [Link to requirements gathering]
- Industry research: [Citations to validation sources]
```

---

## Worksheet A.10: Decision Process Master Checklist

**Instructions**: Track the end-to-end selection process against this checklist. It mirrors the workshop flow in "How to Use These Worksheets" and gives you a single page to confirm nothing was skipped before you present to your executive sponsor.

**Requirements Gathering** ✓:
- [ ] Stakeholder workshop completed (CISO, SOC, compliance, finance, IT, data engineering)
- [ ] Tier 1 mandatory requirements documented (5-8 hard filters)
- [ ] Tier 2 strongly preferred requirements documented (4-6 weighted requirements)
- [ ] Tier 3 nice-to-have requirements documented (2-4 tiebreakers)
- [ ] Organizational constraints documented (budget, team, vendor, political)

**Vendor Filtering** ✓:
- [ ] Started with IT Harvest security data platform categories (order of 80-100 vendors as of mid-2025 — directional, Tier C; check the current IT Harvest count for your category before relying on it)
- [ ] Applied Tier 1 filters (typically reduces to roughly 10-25 vendors — illustrative, your filters and category set will move this)
- [ ] Optional: IT Harvest research on finalists (funding, maturity, positioning)

**Finalist Scoring** ✓:
- [ ] Applied Tier 2 weighted scoring (3× multiplier)
- [ ] Applied Tier 3 tiebreaker scoring (1× multiplier)
- [ ] Validated organizational constraints (budget, team, vendor, political)
- [ ] Selected 2-4 finalists representing different architectural approaches

**POC Evaluation** ✓:
- [ ] Success criteria defined (performance, cost, operational, usability)
- [ ] Realistic test dataset prepared (90 days minimum, 5-10 sources)
- [ ] Structured POC executed (4 weeks: setup, performance, operations, cost validation)
- [ ] POC results scored against criteria
- [ ] Vendor support quality assessed

**Decision Documentation** ✓:
- [ ] Architecture Decision Record written (context, decision, rationale, trade-offs)
- [ ] Limitations honestly documented (what this does NOT solve)
- [ ] Alternatives considered and why rejected
- [ ] Implementation plan defined (pilot → rollout → optimization)
- [ ] Stakeholder approval gained (CISO, CFO, CIO, architecture board)

---

These worksheets turn the handbook's requirements framework and decision methodology into templates you can actually fill in. Once you've worked through them, they become the documented justification for your platform selection, the artifact you hand to a CFO or an architecture board when they ask why this platform and not the incumbent, and the record that holds up when someone revisits the decision two years later.

**Next**: Appendix B (Anti-Patterns Catalog) identifies common failures and prevention strategies.

