---
type: operating-doc
title: "Expert Interview Guide: Lisa Cao (Catalog Landscape — Gravitino, Polaris, XTable)"
created: 2025-11-26
tags: [expert-interview, catalog-landscape, gravitino, xtable, iceberg, hypothesis-validation]
---

# Expert Interview Guide: Lisa Cao (Datastrato)

**Interviewee**: Lisa Cao
**Affiliation**: Datastrato (Gravitino project)
**Expertise**: Catalog management, table format interoperability, data lakehouse infrastructure
**Interview Focus**: Gravitino adoption, catalog landscape, XTable/format portability
**Scheduled**: Week 3 (TBD)
**Interviewer**: Jeremy Wiley

---

## Interview Objectives

### Primary Goals
1. **Validate H-ARCH-03**: Catalog adoption patterns and Gravitino positioning
2. **Assess XTable Adoption**: Table format interoperability in production
3. **Catalog Landscape**: Multi-catalog management challenges and solutions
4. **Security Use Cases**: Catalog requirements specific to security operations

### Secondary Goals
5. Evidence for catalog selection criteria in book Chapter 9 (Query Engines)
6. Practitioner insights for technology decision tree
7. Emerging patterns: Catalog proliferation management

---

## Pre-Interview Context

### What We Know from Literature Review

**Catalog Landscape** (from MASTER-BIBLIOGRAPHY.md):
- **Gravitino**: Apache project, multi-catalog federation layer
- **Polaris**: Snowflake open-source catalog (Iceberg-focused)
- **Unity Catalog**: Databricks offering (multi-format support)
- **Nessie**: Dremio's Git-like catalog with versioning

**Table Format Interoperability** (from Gap Analysis):
- **Apache XTable**: Format interoperability layer (Iceberg ↔ Delta ↔ Hudi)
- **Gartner Survey**: 64% architects concerned about format lock-in, 42% cite XTable as mitigation
- **Status**: Apache incubator, adoption patterns unclear

**Current Hypothesis Status**:
- **H-ARCH-01** (Iceberg Dominance): STRONGLY VALIDATED (industry consensus as de facto standard; the "76% adoption" figure is unsourced)
- **H-ARCH-03** (Catalog Adoption): Needs validation - no formal hypothesis yet
- **XTable**: Emerging technology, production usage unknown

### Evidence Gaps to Address
1. **Gravitino adoption metrics**: How many organizations/projects using it?
2. **Catalog selection criteria**: What drives catalog choice? (Performance, features, vendor lock-in concerns)
3. **Multi-catalog use cases**: When do organizations need catalog federation vs single catalog?
4. **XTable production usage**: Anyone using XTable in production? What use cases?
5. **Security-specific considerations**: Do security operations have unique catalog requirements?

---

## Interview Questions

### Section 1: Gravitino Adoption & Positioning (15 minutes)

**Context-Setting**:
> "I'm researching catalog management for security data lakehouses. I'd love to understand Gravitino's role in this landscape."

**Q1.1 Adoption Metrics**:
- How many organizations are currently using Gravitino in production?
- What types of organizations? (Enterprise, startups, specific industries?)
- What's the typical scale? (Data volumes, user counts, catalogs managed)

**Q1.2 Use Case Patterns**:
- What are the top 3 use cases driving Gravitino adoption?
- Multi-catalog federation vs single catalog management - which is more common?
- Are there specific industries or domains where Gravitino is particularly well-suited?

**Q1.3 Security Operations Context**:
- Have you seen Gravitino deployed for security operations specifically? (SIEM replacement, security data lake, threat hunting platforms)
- Any unique requirements for security vs general analytics catalogs?
- Compliance/governance considerations: Do security teams have different catalog needs?

**Follow-up Probes**:
- What's the most impressive production deployment you've seen?
- What surprised you most about how organizations are using Gravitino?
- Any anti-patterns you've observed? (Things people try that don't work well)

---

### Section 2: Catalog Landscape & Selection Criteria (20 minutes)

**Context-Setting**:
> "For the book, I'm building a decision framework for catalog selection. I'd love your perspective on the landscape."

**Q2.1 Competitive Positioning**:
- How do you position Gravitino vs Polaris, Unity Catalog, and Nessie?
- When would you recommend Gravitino vs alternatives?
- What are Gravitino's unique strengths? Where does it fall short?

**Q2.2 Selection Criteria**:
- What should architects evaluate when choosing a catalog? (Top 5 criteria)
- How important is vendor lock-in concern in catalog decisions?
- Performance considerations: Do catalog performance characteristics matter for security workloads?

**Q2.3 Multi-Catalog Management**:
- Why do organizations end up with multiple catalogs? (Acquisitions, different teams, different vendors)
- Catalog proliferation: Is this a growing problem?
- Federation strategies: When to federate vs consolidate?

**Q2.4 Integration Patterns**:
- Gravitino with query engines: Any preferred combinations? (Trino, Dremio, ClickHouse)
- Storage format support: Iceberg-first vs multi-format - what's the reality?
- Object storage integration: S3, Azure Blob, MinIO - any gotchas?

**Follow-up Probes**:
- What do people get wrong about catalog selection?
- Hidden costs or complexity in catalog management?
- How much engineering effort for catalog setup/maintenance? (FTE estimates)

---

### Section 3: Table Format Interoperability & XTable (15 minutes)

**Context-Setting**:
> "Apache XTable keeps coming up in vendor conversations. I'm trying to understand if it's production-ready or still emerging."

**Q3.1 XTable Production Status**:
- Have you seen XTable deployed in production? (Any organizations you can reference?)
- What use cases is XTable solving? (Format migration, multi-engine access, vendor lock-in mitigation)
- Is XTable mature enough for security operations? (24/7 uptime, compliance requirements)

**Q3.2 Format Portability Reality**:
- How big a concern is table format lock-in for enterprises?
- Does XTable actually solve this, or are there limitations?
- Performance implications: Does format translation add latency/cost?

**Q3.3 Gravitino + XTable Relationship**:
- How does Gravitino relate to XTable? (Complementary, overlapping, independent?)
- Can Gravitino manage XTable-backed tables?
- Would you recommend using both together?

**Q3.4 Format Convergence Trends**:
- Is the industry converging on Iceberg, or will multi-format be permanent?
- What's your 3-5 year forecast for table formats? (Iceberg 80%+? Permanent fragmentation?)
- Should security architects plan for multi-format or bet on Iceberg?

**Follow-up Probes**:
- Gartner survey shows 64% lock-in concern, 42% cite XTable - do those numbers match your experience?
- What's the biggest misconception about format interoperability?
- When would you NOT recommend XTable?

---

### Section 4: Architecture Patterns & Best Practices (15 minutes)

**Context-Setting**:
> "I'm documenting reference architectures for security data platforms. What patterns are you seeing?"

**Q4.1 Common Architecture Patterns**:
- Typical Gravitino deployment pattern: Cloud, on-prem, hybrid?
- Integration with streaming (Kafka) vs batch (Spark) - any differences?
- Catalog HA/DR: How are organizations handling catalog availability? (Catalog downtime = platform downtime)

**Q4.2 Security-Specific Patterns**:
- Log aggregation at scale: Catalog considerations for high-volume security logs?
- Threat intelligence integration: Catalog role in TI data management?
- Multi-tenancy: SOC teams sharing catalog vs separate catalogs - what's working?

**Q4.3 Implementation Reality**:
- How long to deploy Gravitino? (Pilot to production timeline)
- Team size/skills: What expertise is needed? (Data engineering, platform engineering, security engineering)
- Common pitfalls: What causes Gravitino deployments to struggle?

**Q4.4 Cost Considerations**:
- Gravitino TCO: What are the hidden costs? (Maintenance, upgrades, scale-out)
- Managed vs self-hosted: Any managed Gravitino offerings?
- Cost vs alternatives: How does Gravitino cost compare to Unity/Polaris?

**Follow-up Probes**:
- What's a "hero deployment" story you can share?
- What question am I not asking that I should be?
- Any upcoming Gravitino features that will change the game?

---

### Section 5: Future Trends & Recommendations (10 minutes)

**Context-Setting**:
> "This book will be published in 2026. I want to make sure recommendations stay relevant."

**Q5.1 Emerging Patterns**:
- What catalog-related trends are you tracking? (Next 1-2 years)
- AI/ML workloads: Do they have different catalog needs than OLAP analytics?
- Edge/distributed catalogs: Relevant for security (EDR, sensor data)?

**Q5.2 Book Recommendations**:
- For a security architect planning a lakehouse in 2026, what catalog advice would you give?
- Top 3 mistakes to avoid in catalog selection?
- Required reading: Any resources you'd recommend on catalog architecture?

**Q5.3 Expert Network**:
- Who else should I talk to about catalogs/formats? (Industry experts, practitioners)
- Any case studies or reference architectures you'd recommend reviewing?
- Upcoming conferences/talks where catalog topics will be featured?

**Follow-up Probes**:
- If you were writing Chapter 9 (Query Engines + Catalogs), what would you emphasize?
- What's the one thing everyone gets wrong about catalogs?
- Bold prediction: Where will the catalog landscape be in 5 years?

---

## Evidence Validation Checklist

### Hypothesis Validation Targets

**H-ARCH-03 (New)**: Catalog Adoption Patterns
- [ ] Gravitino adoption metrics (production deployments count)
- [ ] Catalog selection criteria (quantitative if possible)
- [ ] Multi-catalog vs single catalog use case breakdown

**XTable Production Status**:
- [ ] Production deployment count (even if small)
- [ ] Use cases where XTable is solving real problems
- [ ] Maturity assessment (ready for security ops or not)

**Format Convergence**:
- [ ] Iceberg vs Delta vs Hudi - current adoption split
- [ ] 3-5 year forecast on format standardization
- [ ] Lock-in concerns - real or overblown?

### Evidence Quality Target
- **Goal**: Evidence Level A (practitioner validation, production metrics)
- **Backup**: Evidence Level B (expert opinion, industry observations)

---

## Post-Interview Actions

### Immediate (Within 24 hours)
1. **Transcribe Interview**: Key quotes, quantitative data, production examples
2. **Update MASTER-BIBLIOGRAPHY.md**: Add Lisa Cao as evidence source
3. **Hypothesis Updates**:
   - Formalize H-ARCH-03 if sufficient evidence gathered
   - Update XTable status in Gap Analysis (production-ready vs emerging)

### Short-Term (Within 1 week)
4. **Evidence Bundles**: Update relevant analysis bundles with new data
   - `technology-decision-tree.md`: Add catalog selection criteria
   - `implementation-reality-reference.md`: Add Gravitino deployment timelines/FTEs
5. **Blog Post Potential**: "Catalog Management for Security Operations: Gravitino, Polaris, Unity Compared"
6. **Book Integration**: Update Chapter 9 with catalog guidance

### Follow-up Interviews
7. **References**: Contact any practitioners Lisa recommends
8. **Validation**: Cross-reference Lisa's insights with other experts (Jake Thomas, a data-platform practitioner)
9. **IT Harvest**: Coordinate catalog vendor data with Lisa's insights

---

## Interview Recording & Consent

**Recording**:
- [ ] Request permission to record (for accuracy, not publication)
- [ ] Clarify attribution: "Lisa Cao, Datastrato" vs "industry expert" vs anonymous

**Consent for Use**:
- [ ] Academic publication (journal articles)
- [ ] Book citation (main manuscript)
- [ ] Blog post (public-facing content)
- [ ] Evidence level classification (Level A practitioner validation)

**Quote Approval**:
- [ ] Send transcript/key quotes for review before publication
- [ ] Clarify what's on-record vs off-record
- [ ] Verify production deployment details won't expose sensitive info

---

## Prepared Follow-ups

### If Lisa Provides Metrics
- "Can I cite these numbers in the book? What attribution would you prefer?"
- "Are these public metrics or confidential? Can I reference in academic publication?"
- "What's the source of these metrics? (Internal Datastrato data, user surveys, Apache project stats)"

### If Lisa Describes Production Deployments
- "Can you share organization name, or should I keep this anonymous?"
- "What scale? (Data volumes, user count, queries/day)"
- "How long has this been in production? Any incident/downtime history?"

### If Lisa Identifies Gaps in My Understanding
- "What resources would help me understand this better?"
- "Is there documentation/architecture diagrams I should review?"
- "Would another expert be better positioned to answer this?"

---

## Interview Tips

**Build Rapport**:
- Acknowledge Gravitino's Apache project success
- Reference specific Gravitino features/documentation you've reviewed
- Show genuine curiosity about catalog challenges

**Stay Focused**:
- 75 minutes total, strict time management
- If one section runs long, skip lower-priority questions
- Prioritize: Adoption metrics > XTable status > Architecture patterns

**Probe for Quantitative Data**:
- "Can you quantify that?" (adoption %, timeline months, FTE count)
- "What's the range?" (Best case, worst case, typical case)
- "Compared to what?" (Gravitino vs alternatives, current state vs future state)

**Document Production Validation**:
- Prioritize Level A evidence (production deployments, quantitative metrics)
- Get permission to cite before ending interview
- Note confidence levels ("confident this is widespread" vs "anecdotal, small sample")

---

---

## January 2026 Context Update: AI Governance Research

### CSA/Google Cloud AI Security and Governance Study (December 2025)

**Key Findings to Discuss** (relevant for catalog governance in AI-enabled security):
- **Only 26%** of organizations have comprehensive AI security governance
- **Governance maturity is the strongest predictor of AI readiness**
- Organizations with comprehensive policies: **46%** early agentic AI adoption
- Organizations with policies in development: only **12%** adoption (3.8× difference)
- **60%** plan to use agentic AI within 12 months

**Potential Discussion Points**:
- How does catalog governance (Gravitino) enable or constrain AI/ML security initiatives?
- Are organizations with better data catalog governance more successful with AI security tools?
- What catalog features matter most for AI-driven security analytics?

**Source**: CSA/Google Cloud "The State of AI Security and Governance" (Dec 2025)

---

**Prepared By**: Claude (AI Assistant) + Jeremy Wiley
**Date**: October 16, 2025 (updated January 3, 2026 with AI governance findings)
**Status**: Ready for scheduling
**Estimated Interview Duration**: 75 minutes
**Format**: Video call (Zoom/Google Meet) with recording
