---
type: engagement
title: "Expert Interview Guide: Jake Thomas (Okta) — DuckDB Edge Processing and Security Data Volumes"
created: 2025-10-16
tags: [expert-interview, jake-thomas, okta, duckdb, isolation-first-security]
---

# Expert Interview Guide: Jake Thomas (Okta)

> **⚠️ Refresh before scheduling (2026-07-10 check)**: three figures in this guide's pre-interview context have since been withdrawn or flagged in MASTER-BIBLIOGRAPHY — do NOT quote them to Jake: Shell 57TB/day (entry withdrawn 2026-06-05), DuckDB "used at Facebook/Google/Airbnb" (removed 2026-07-10, no primary), and "6+ million monthly downloads" (uncatalogued; the verified v1.0.0-announcement phrasing is "download counts are in the millions each month"). Re-pull the context section from the current bibliography before the interview.

> **Re-pulled 2026-07-16**: the three figures flagged above are gone from the sections below. The Shell 57TB/day line is replaced in two places — the H1-VOLUME-07 status note now cites the surviving Cloudflare 6M req/sec production leg, and the Section 4 ask-script quote now cites Okta's own serverless-DuckDB figure (1M Lambda invocations/day, 250 GB/min peak, from Julien Hurault's write-up, Evidence Level A) — since a number about Jake's own employer gives him something concrete to confirm or correct rather than a withdrawn figure about a company he has no connection to. The "used at Facebook/Google/Airbnb" line is removed with no replacement, because no primary source for it was ever located. "6+ million monthly downloads" is corrected to the v1.0.0 announcement's verbatim phrasing, "download counts are in the millions each month." The corpus and hypothesis context throughout this guide is current as of this pull: 229 catalogued entries (227 tiered, 41.9% Level A, per `scripts/count_reconcile.py`) and the 2026-07-13 rubric rescore recorded in PUBLICATION-MANUSCRIPT.md §3.7. Neither H-EDGE-01 nor H1-VOLUME-07 carries a formal score under that rubric yet, which is honestly the point of this interview — it's the intended route to giving both one.

**Interviewee**: Jake Thomas
**Affiliation**: Okta
**Expertise**: Production defensive cyber operations, DuckDB at scale, security data volumes
**Interview Focus**: DuckDB edge processing, security data volume validation, production architecture
**Scheduled**: Week 3 (TBD)
**Interviewer**: Jeremy Wiley

---

## Interview Objectives

### Primary Goals
1. **Validate H-EDGE-01**: DuckDB for edge/embedded security analytics
2. **Validate H1-VOLUME-07**: Security data volume claims (mid-sized enterprises)
3. **Production Architecture**: DuckDB deployment patterns in defensive cyber ops
4. **Performance Validation**: DuckDB OLAP performance for security workloads

### Secondary Goals
5. Edge processing patterns: When to process locally vs centrally
6. Staffing/skills requirements for DuckDB deployments
7. Cost comparisons: DuckDB vs traditional SIEM vs cloud data warehouse
8. Emerging patterns: Edge analytics trend validation

---

## Pre-Interview Context

### What We Know from Literature Review

**DuckDB Positioning** (from MASTER-BIBLIOGRAPHY.md's DuckDB & Edge Processing section, re-pulled 2026-07-16):
- **Official Positioning**: Embedded analytics, SQLite alternative for OLAP workloads
- **Key Features**: In-process analytics, no server management, OLAP-grade performance, stable on-disk storage format since v1.0.0 (June 3, 2024)
- **Status**: Production-ready. The corpus now carries several DuckDB-relevant entries beyond the official docs page: the v1.0-1.4 release history (Evidence Level B), the DuckLake v1.0 lakehouse format with first-party BENCH-E catalog failure-mode findings run on DuckDB 1.5.3 (Evidence Level B, project/vendor-authoritative), a first-party OCSF row-level-security overhead measurement run directly on DuckDB 1.5.3 (Evidence Level B, single host), the Data Inlining in DuckLake vendor benchmark (Evidence Level C), and Julien Hurault's Okta multi-engine data-stack write-up (Evidence Level A, verified 2026-06-05) — the last of which already documents an Okta production number worth confirming with Jake directly: serverless DuckDB at 1M Lambda invocations/day, 250 GB/min peak.
- **Note**: MASTER-BIBLIOGRAPHY.md also carries a placeholder entry for this interview itself ("Okta Security Analytics - Isolation-First Architecture with DuckDB + Iceberg," Evidence Level B, attributed to Jake Thomas as personal communication), logged as scheduled for the Q1 2026 quarterly deep dive after slipping from October 2025. It's now July 2026, so this guide is being re-pulled well past that scheduled window.

**Current Evidence Gaps**:
- **H-EDGE-01**: Still proposed, still not formally validated - "DuckDB enables edge/endpoint security analytics." It sits outside the nine hypotheses scored under the 2026-07-13 rubric rescore (PUBLICATION-MANUSCRIPT.md §3.7) because it has no quantitative leg yet, so this interview is the intended route to giving it one.
- **Production deployments**: Jake Thomas (Okta) remains the primary intended validation source; Julien Hurault's write-up gives a secondary, already-verified Okta data point worth checking against what Jake is actually running today.
- **Security-specific benchmarks**: partially closed. The review's own first-party OCSF row-level-security bench now runs on DuckDB 1.5.3, so RLS overhead specifically has a measured number; general DuckDB security-workload performance (query latency, throughput under a security-telemetry shape) is still absent from the literature review.

**Related Hypotheses**:
- **H1-VOLUME-07** (Security Data Volumes): Partially validated at large scale. The Shell 57TB/day figure was withdrawn 2026-06-05 as fabricated-class and no longer supports this hypothesis; the surviving large-scale leg is Cloudflare's 6M req/sec production throughput (Evidence Level A, verified at primary). Mid-market validation is still the open gap this interview targets.
- **H3-PERFORMANCE-01** (OLAP Performance): Now High Confidence (4 stars, 19/25 under the 2026-07-13 rubric rescore) on the Cloudflare leg plus a first-party CIDR probe; a DuckDB comparison at security-relevant scale isn't part of that score yet, so it's a clean opening for this interview.

**Evidence Level Target**: A (production deployment, quantitative metrics from Jake)

**Corpus status** (2026-07-16): the live bibliography holds 229 catalogued `#### ` entries, 227 tiered, at 41.9% Evidence Level A (`scripts/count_reconcile.py`). Nine hypotheses carry a formal score under the 2026-07-13 rescore - one strongly validated, two high confidence, two moderate, four preliminary - and H-EDGE-01 and H1-VOLUME-07 are not among them, which is the honest way of saying this interview is trying to move both from unscored to scored.

---

### What We Need to Learn

**Critical Validation Points**:
1. **Production deployment details**: Scale (data volumes, query counts, user count)
2. **Architecture patterns**: Where DuckDB fits in security data pipeline
3. **Use cases**: What problems does DuckDB solve vs alternatives?
4. **Performance metrics**: Query latency, throughput, data volumes handled
5. **Cost comparison**: DuckDB TCO vs alternatives (SIEM, cloud warehouse)

**Evidence Gaps from Gap Analysis** (LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md):
- DuckDB production architecture (H-EDGE-01 validation)
- Security data volume validation (H1-VOLUME-07 - mid-sized enterprise data)
- Edge processing patterns (when to process locally vs centrally)
- Staffing/timeline: How long to deploy? What skills required?

---

## Interview Questions

### Section 1: DuckDB Production Deployment (20 minutes)

**Context-Setting**:
> "I'm researching DuckDB for security operations. I'd love to understand how you're using it at Okta."

**Q1.1 Deployment Overview**:
- How long have you been running DuckDB in production?
- What scale? (Data volumes per day, total dataset size, query count, user count)
- Deployment model: Edge/endpoint, centralized servers, hybrid?

**Q1.2 Use Case Details**:
- What specific security operations use DuckDB? (Threat hunting, incident response, log analysis, compliance reporting)
- What problem were you solving? (Why DuckDB vs alternatives?)
- What did you replace? (Legacy SIEM, ELK stack, cloud warehouse, nothing - net new capability)

**Q1.3 Architecture Pattern**:
- Where does DuckDB sit in your data pipeline? (Ingestion, storage, query, all of the above)
- Integration points: What systems does DuckDB connect to? (Kafka, S3, SIEM, ticketing)
- Data format: Parquet, Iceberg, Delta, raw logs?

**Q1.4 Team & Operations**:
- Team size: How many people support DuckDB deployment?
- Skills required: What expertise was needed? (SQL, Python, security domain knowledge)
- Operational burden: How much care and feeding does DuckDB need?

**Follow-up Probes**:
- What was the "aha moment" that made you choose DuckDB?
- Any surprises (good or bad) in production?
- If you started over today, would you make the same choice?

---

### Section 2: Performance & Scalability (15 minutes)

**Context-Setting**:
> "I'm building performance comparison tables for the book. I'd love to understand DuckDB's performance characteristics."

**Q2.1 Query Performance**:
- Typical query latency: What's the P50, P95, P99? (Seconds, milliseconds)
- Query complexity: Simple filters vs complex aggregations vs joins?
- Worst-case performance: What queries slow down? Any query patterns to avoid?

**Q2.2 Data Volume Handling**:
- Current data volumes: How much data are you querying? (GB, TB, PB)
- Growth trajectory: Started small, scaled up? Any scaling issues?
- Data retention: How long do you keep data in DuckDB? (Hot data only, full retention)

**Q2.3 Concurrency & Throughput**:
- Concurrent users: How many analysts/hunters query simultaneously?
- Query throughput: Queries per second/minute/hour?
- Resource utilization: CPU, memory, disk I/O - what's the bottleneck?

**Q2.4 Comparison to Alternatives**:
- Have you benchmarked DuckDB vs other systems? (ClickHouse, Trino, BigQuery, Athena)
- Performance comparison: Faster/slower than what you replaced?
- Cost-performance trade-offs: Where does DuckDB win on cost-per-query?

**Follow-up Probes**:
- Can you quantify the speedup vs your previous solution? (2×, 10×, 100×)
- Any performance optimizations you've discovered?
- What's DuckDB's performance ceiling? (Where does it start to struggle?)

---

### Section 3: Edge Processing Patterns (20 minutes)

**Context-Setting**:
> "Edge/embedded processing is an emerging pattern. I'm trying to understand when it makes sense."

**Q3.1 Edge vs Central Decision**:
- Why process at the edge vs centralize everything? (Latency, bandwidth, compliance, cost)
- What security workloads are good for edge processing?
- What workloads should stay centralized?

**Q3.2 DuckDB-Specific Edge Patterns**:
- Is DuckDB running on endpoints/sensors, or on edge servers?
- Data locality: Are you processing data where it lives, or still moving it?
- Network topology: How does edge DuckDB connect to central systems?

**Q3.3 Use Case Examples**:
- **Incident Response**: Is DuckDB on analyst laptops for local investigation?
- **Threat Hunting**: Pre-aggregation at edge before central analysis?
- **Compliance Reporting**: Distributed compliance checks on edge devices?

**Q3.4 Edge Challenges**:
- What's hard about edge processing? (Management, updates, data sync, consistency)
- How do you handle DuckDB updates/patches across distributed deployments?
- Data freshness: How do you keep edge data in sync with central?

**Q3.5 Central vs Edge Trade-offs**:
- Cost comparison: Edge compute vs central cloud compute?
- Performance: Latency reduction from edge processing - can you quantify?
- Complexity: Is edge worth the operational overhead?

**Follow-up Probes**:
- What's the "break-even" point for edge processing? (When does it make sense?)
- Any edge deployment horror stories? (What went wrong, lessons learned)
- Future: Will more security workloads move to edge, or is this niche?

---

### Section 4: Security Data Volumes & Economics (15 minutes)

**Context-Setting**:
> "I'm validating security data volume claims. One data point I have on Okta specifically is Julien Hurault's write-up describing serverless DuckDB at 1M Lambda invocations/day, 250 GB/min peak — I'd love to know if that still matches what you're running, and what a realistic mid-market range looks like more broadly."

**Q4.1 Data Volume Reality**:
- Okta's security data volume: TB/day, PB/year range?
- Data sources: Logs, network traffic, endpoint telemetry, threat intel?
- Growth rate: How fast is data volume growing? (Year-over-year %)

**Q4.2 Mid-Market Context**:
- Is Okta's volume representative of mid-sized enterprises, or unique?
- What do you see as "typical" for companies in the 1,000-10,000 employee range?
- Volume drivers: What generates the most data? (Logs, network, cloud telemetry)

**Q4.3 Cost Economics**:
- Storage costs: What's the annual cost for security data storage?
- Query costs: If using cloud (S3, BigQuery), what are query costs?
- DuckDB TCO: Total cost for DuckDB deployment (infrastructure, staff, licensing if applicable)?

**Q4.4 Cost Comparison**:
- DuckDB vs legacy SIEM: Can you quantify the cost difference?
- DuckDB vs cloud data warehouse: Cost savings from in-process analytics?
- What's the ROI? (Cost savings, analyst productivity, faster detection)

**Follow-up Probes**:
- What's the biggest cost surprise in security data management?
- Hidden costs: What do vendors not tell you about data platform costs?
- Cost optimization: What worked to reduce costs?

---

### Section 5: Implementation Reality (10 minutes)

**Context-Setting**:
> "I'm documenting realistic implementation timelines and staffing for the book."

**Q5.1 Implementation Timeline**:
- How long from decision to production? (Pilot, proof-of-concept, production rollout)
- What took the longest? (Procurement, setup, integration, training)
- If you did it again, how much faster could you go?

**Q5.2 Staffing & Skills**:
- Team size during implementation: How many FTEs?
- Skills required: Data engineering, security engineering, SQL expertise?
- Training investment: How much time to get analysts productive on DuckDB?

**Q5.3 Build vs Buy**:
- Did you consider managed alternatives? (Cloud data warehouse, managed SIEM)
- Why self-hosted DuckDB vs managed service?
- Would you make the same choice today? (Or would you use BigQuery, Snowflake, etc.)

**Q5.4 Vendor Ecosystem**:
- Any vendors supporting DuckDB for security? (Motherduck, others)
- Open-source vs commercial: All OSS, or any paid components?
- Support: Where do you go for help? (Community, paid support, internal expertise)

**Follow-up Probes**:
- What skills gap was hardest to fill?
- Vendor partnerships: Any that made DuckDB easier?
- What would you tell a team planning a DuckDB deployment?

---

### Section 6: Comparison to Alternatives (15 minutes)

**Context-Setting**:
> "I'm building a technology decision tree for the book. I need to understand when to choose DuckDB vs alternatives."

**Q6.1 Technology Evaluation**:
- What alternatives did you evaluate? (ClickHouse, Trino, Athena, Snowflake, BigQuery)
- Why did DuckDB win?
- What did DuckDB NOT do well? (Where did alternatives look better?)

**Q6.2 Use Case Fit**:
- When would you recommend DuckDB? (Use cases, scale, team profile)
- When would you NOT recommend DuckDB? (Wrong use case, wrong scale)
- DuckDB vs ClickHouse: How do you decide between them?

**Q6.3 Hybrid Patterns**:
- Are you using DuckDB alongside other systems? (Central ClickHouse + edge DuckDB?)
- Hybrid architecture: Where does each technology fit?
- Data movement: How do you orchestrate between edge DuckDB and central systems?

**Q6.4 Streaming vs Batch**:
- Is DuckDB batch-only for you, or do you have streaming patterns?
- Integration with Kafka: Any real-time patterns with DuckDB?
- Latency requirements: What's the freshness SLA for DuckDB data?

**Follow-up Probes**:
- What's the one thing DuckDB does better than anything else?
- What's the biggest limitation that would make you choose something else?
- 5-year forecast: Where does DuckDB fit in the security data landscape?

---

### Section 7: Hypothesis Validation & Book Recommendations (5 minutes)

**Context-Setting**:
> "I have specific hypotheses from my research. Can you help me validate or refute them?"

**Q7.1 Hypothesis Validation**:

**H-EDGE-01**: "DuckDB enables edge/endpoint security analytics with embedded analytical queries, eliminating network round-trips for local investigation while maintaining OLAP-grade performance, validated by production defensive cyber operations deployments."
- Does this match your experience? What would you change?
- Quantify "OLAP-grade performance" - what metrics validate this?

**H1-VOLUME-07**: "Security data volumes at mid-sized enterprises (1,000-10,000 employees) range from 500GB-5TB/day for comprehensive telemetry."
- Does this match your observations? What's the typical range?
- What factors drive higher/lower volume? (Cloud-native, on-prem, industry)

**Q7.2 Book Recommendations**:
- For a security architect evaluating DuckDB in 2026, what's your top advice?
- Top 3 mistakes to avoid in DuckDB deployment?
- Who else should I talk to? (DuckDB practitioners, security architects using edge processing)

**Q7.3 Future Trends**:
- Where is edge security analytics heading? (More adoption, niche use case)
- DuckDB roadmap: Any features that will change the game?
- Bold prediction: Will DuckDB be as common as ClickHouse in 5 years?

**Follow-up Probes**:
- What question am I not asking that I should be?
- Any misconceptions in my hypotheses?
- What would you emphasize in the book chapter on edge processing?

---

## Evidence Validation Checklist

### Hypothesis Validation Targets

**H-EDGE-01 (DuckDB Edge Processing)**:
- [ ] Production deployment confirmed (scale, timeline, stability)
- [ ] Use cases documented (specific security operations)
- [ ] Performance metrics captured (query latency, data volumes, throughput)
- [ ] Comparison to alternatives (when DuckDB wins, when it loses)
- [ ] Evidence Level: A (production validation, quantitative metrics)

**H1-VOLUME-07 (Security Data Volumes)**:
- [ ] Mid-market data volume range (GB/day or TB/day)
- [ ] Data source breakdown (logs, network, endpoint, cloud)
- [ ] Growth trajectory (year-over-year %)
- [ ] Representativeness (Okta as proxy for mid-market)
- [ ] Evidence Level: A (practitioner validation, production metrics)

**H-IMPL-02 (Staffing Requirements - Extended for DuckDB)**:
- [ ] Team size for DuckDB deployment (implementation + operations)
- [ ] Skills required (data eng, security eng, SQL)
- [ ] Timeline (pilot to production)
- [ ] Training investment
- [ ] Evidence Level: A (production deployment, quantitative staffing)

**Cost Economics**:
- [ ] DuckDB TCO (infrastructure, staff, tooling)
- [ ] Cost comparison to alternatives (SIEM, cloud warehouse)
- [ ] ROI quantification (cost savings, productivity gains)
- [ ] Evidence Level: A (financial data, quantitative comparison)

### Evidence Quality Target
- **Goal**: Evidence Level A (production metrics, quantitative data)
- **Backup**: Evidence Level B (practitioner insights, qualitative comparison)

---

## Post-Interview Actions

### Immediate (Within 24 hours)
1. **Transcribe Interview**: Key quotes, quantitative data, production architecture details
2. **Update MASTER-BIBLIOGRAPHY.md**: Add Jake Thomas as evidence source
3. **Hypothesis Updates**:
   - Validate H-EDGE-01 with production evidence (upgrade to validated status)
   - Update H1-VOLUME-07 with mid-market data
   - Extend H-IMPL-02 with DuckDB staffing data

### Short-Term (Within 1 week)
4. **Evidence Bundles**: Update relevant analysis bundles *(note 2026-07-10: the performance-benchmarks/implementation-reality/technology-decision-tree bundles are archived -> archive/analysis-bundles/; fold interview data into MASTER-BIBLIOGRAPHY.md and the live bundles instead)*
   - `performance-benchmarks-table.md`: Add DuckDB metrics (query latency, throughput, data volumes)
   - `implementation-reality-reference.md`: Add DuckDB deployment timeline/staffing
   - `cost-reality-reference.md`: Add DuckDB TCO vs alternatives
   - `technology-decision-tree.md`: Add DuckDB vs ClickHouse decision criteria
5. **Blog Post Potential**: "DuckDB at Scale: Production Deployments for Defensive Cyber Ops"
6. **Book Integration**: Add edge processing section to Chapter 9 (Emerging Patterns)

### Follow-up Validation
7. **Cross-Reference**: Compare Jake's insights with Lisa Cao (catalog/format implications for edge)
8. **Additional Practitioners**: Contact any DuckDB practitioners Jake recommends
9. **Vendor Validation**: Follow up with MotherDuck or DuckDB Labs for product roadmap insights

---

## Interview Recording & Consent

**Recording**:
- [ ] Request permission to record (for accuracy, not publication)
- [ ] Clarify attribution: "Jake Thomas, Okta" vs "security practitioner" vs anonymous
- [ ] Okta PR/legal: Any clearance needed for production deployment details?

**Consent for Use**:
- [ ] Academic publication (journal articles)
- [ ] Book citation (main manuscript)
- [ ] Blog post (public-facing content)
- [ ] Evidence level classification (Level A practitioner validation)

**Sensitive Information**:
- [ ] Production scale: Can I cite specific data volumes?
- [ ] Architecture details: Any sensitive security architecture I shouldn't publish?
- [ ] Cost data: Can I reference TCO, or is this confidential?

**Quote Approval**:
- [ ] Send transcript/key quotes for review before publication
- [ ] Clarify what's on-record vs off-record
- [ ] Verify production deployment details won't expose security posture

---

## Prepared Follow-ups

### If Jake Provides Quantitative Metrics
- "Can I cite these numbers in the book? What attribution would you prefer?"
- "Are these specific to Okta, or representative of the industry?"
- "What's the margin of error? (Best case, typical case, worst case)"

### If Jake Describes Production Architecture
- "Can you share an architecture diagram, or should I sketch one based on your description?"
- "Any security-sensitive details I should keep confidential?"
- "Can I use Okta as a named case study, or should I anonymize?"

### If Jake Identifies Trade-offs
- "Can you quantify the trade-off? (e.g., DuckDB is 50% cheaper but 2× slower)"
- "When does the trade-off flip? (Scale, use case, team profile)"
- "What would change your recommendation? (DuckDB → ClickHouse, edge → central)"

---

## Interview Tips

**Build Rapport**:
- Acknowledge Jake's expertise in defensive cyber ops
- Reference specific security data challenges (incident response speed, threat hunting at scale)
- Show genuine curiosity about edge processing patterns

**Stay Focused**:
- 75-80 minutes total, strict time management
- If one section runs long, skip lower-priority questions
- Prioritize: Production deployment details > Performance metrics > Cost economics

**Probe for Quantitative Data**:
- "Can you quantify that?" (data volumes TB/day, query latency ms, team size FTEs)
- "What's the range?" (Typical, best case, worst case)
- "Compared to what?" (DuckDB vs ClickHouse, edge vs central, before vs after)

**Document Production Validation**:
- Prioritize Level A evidence (production deployments, quantitative metrics, financial data)
- Get permission to cite before ending interview
- Note confidence levels ("this is widespread" vs "just at Okta" vs "anecdotal")

**Security Sensitivity**:
- Recognize Jake may not be able to share all details (Okta security posture)
- Offer anonymization if needed ("a major identity provider" vs "Okta")
- Clarify what's publishable vs background information

---

## Key Research Questions Summary

**Must Answer** (Critical for validation):
1. DuckDB production deployment scale (data volumes, query counts, user count)
2. Performance metrics (query latency, throughput) - quantitative
3. Cost comparison vs alternatives (SIEM, cloud warehouse) - quantitative
4. Use cases where DuckDB excels (edge processing, specific security operations)
5. Security data volume validation (mid-market range GB/day or TB/day)

**Should Answer** (Important for book quality):
6. Implementation timeline and staffing (FTEs, months, skills required)
7. Edge vs central trade-offs (when to process locally vs centrally)
8. DuckDB vs ClickHouse decision criteria (quantitative thresholds)
9. Architecture patterns (where DuckDB fits in security data pipeline)
10. Future trends (edge analytics adoption trajectory)

**Nice to Have** (Enriches narrative):
11. "Aha moment" story (why DuckDB won over alternatives)
12. Production deployment challenges (what went wrong, lessons learned)
13. Expert network connections (other DuckDB practitioners to interview)
14. Vendor ecosystem insights (MotherDuck, DuckDB Labs roadmap)
15. Bold predictions (DuckDB in 5 years)

---

---

## January 2026 Context Update: AI Governance & Isolation-First Research

### CSA/Google Cloud AI Security and Governance Study (December 2025)

**Key Findings to Discuss** (relevant for isolation-first security and AI readiness):
- **Only 26%** of organizations have comprehensive AI security governance
- **Governance maturity is the strongest predictor of AI readiness**
- Organizations with comprehensive policies: **46%** early agentic AI adoption
- Organizations with policies in development: only **12%** adoption (3.8× difference)
- **60%** plan to use agentic AI within 12 months

**Potential Discussion Points for Jake**:
- How does Okta's isolation-first architecture enable AI/ML security initiatives?
- Does simplified catalog governance (table-level RBAC vs RLS) correlate with AI success?
- What governance features matter most for AI-driven security at Okta scale?

### Isolation-First Security Evidence (RQ7-RQ10)

**Current Bibliography Findings** (re-pulled 2026-07-16, replacing the January 2026 draft's uncatalogued figures):
- DuckDB 1.0 released June 3, 2024 (stable on-disk storage format, production-ready; v1.0.0 announcement)
- "Download counts are in the millions each month, and download traffic just for extensions is upwards of four terabytes each day" (v1.0.0 announcement, verbatim - replaces the earlier "6+ million monthly downloads," which was never catalogued)
- Okta itself is a catalogued production adopter: serverless DuckDB at 1M Lambda invocations/day, 250 GB/min peak (Julien Hurault's write-up, Evidence Level A) - worth confirming directly with Jake rather than citing secondhand
- Gravitino: Pinterest is the confirmed adopter (Jerry Shao's "Scaling Iceberg Adoption at Pinterest with Gravitino" talk, per the cataloged Medium write-up); a broader adopter list (Uber, Apple, Intel, and others) circulates but is unverified against Gravitino's own project materials, so it shouldn't be quoted to Jake as confirmed

**Removed** (2026-07-10, no primary located): "Used at Facebook, Google, Airbnb" - do not quote this to Jake.

**Questions for Jake on Isolation-First Validation**:
- Does Okta use network isolation + IAM as primary security controls (vs fine-grained catalog)?
- What's the performance advantage of table-level RBAC vs row-level security for your workloads?
- Has the isolation-first approach simplified compliance (SOC 2/ISO 27001)?

**Sources**: DuckDB Labs, *DuckDB 1.0.0 Announcement* (2024-06-03); Julien Hurault, *Okta's Multi-Engine Data Stack* (2024-05-01); Medium/"Office," summarizing Jerry Shao, *Scaling Iceberg Adoption at Pinterest with Gravitino* (2025-08-26) - all per MASTER-BIBLIOGRAPHY.md. (The January 2026 draft cited "CSA/Google Cloud" here, which is the source for the AI-governance stats above, not for these DuckDB/Gravitino figures - corrected in this pass.)

---

**Prepared By**: Claude (AI Assistant) + Jeremy Wiley
**Date**: October 16, 2025 (updated January 3, 2026 with AI governance + isolation-first findings; context re-pulled 2026-07-16 - see banner note)
**Status**: Ready for scheduling
**Estimated Interview Duration**: 75-80 minutes
**Format**: Video call (Zoom/Google Meet) with recording
