# IT Harvest Partnership Coordination Checklist

**Purpose**: Coordinate vendor landscape data integration for quarterly technology state assessments
**Partnership Contact**: Charles Wells (IT Harvest)
**Target**: Query Engines Pilot → Full Vendor Landscape Integration
**Created**: October 15, 2025
**Status**: Pre-Partnership Planning

---

## Phase 1: Partnership Establishment

### Initial Contact & Scope Definition

- [ ] **Initial Outreach to Charles Wells**
  - Introduce literature review project and book context
  - Explain quarterly update goals (Jan, Apr, Jul, Oct)
  - Request exploratory meeting to discuss partnership

- [ ] **Define Pilot Project Scope** (Query Engines Category)
  - Specific vendors to track: Trino/Starburst, Dremio, Denodo, Athena, ClickHouse, StarRocks, Druid
  - Data points needed: Version updates, capabilities, pricing trends, adoption indicators
  - Update frequency: Quarterly snapshots
  - Success criteria: Validate data quality and integration workflow

- [ ] **Clarify Data Access Terms**
  - Data usage rights (literature review, book citations, blog posts)
  - Attribution requirements (how to cite IT Harvest data)
  - Confidentiality constraints (what can/cannot be published)
  - Update frequency and delivery method

- [ ] **Establish Communication Channels**
  - Primary contact method (email, Slack, scheduled calls)
  - Escalation path for urgent requests
  - Quarterly sync cadence (pre-update planning calls)

### Legal & Administrative

- [ ] **Review Data Sharing Agreement**
  - Usage rights for academic/book purposes
  - Attribution requirements
  - Derivative work permissions (blog posts, presentations)
  - Duration and renewal terms

- [ ] **Define Citation Format**
  - How to cite IT Harvest data in MASTER-BIBLIOGRAPHY.md
  - Evidence level assignment (likely Level B - industry data)
  - Example citation format agreed upon

- [ ] **Establish Data Refresh Cadence**
  - Quarterly snapshots (Jan, Apr, Jul, Oct)
  - Data delivery timeline (e.g., 1st week of quarter)
  - Version control for historical data

---

## Phase 2: Pilot Project - Query Engines

### Data Collection Setup

- [ ] **Define Query Engines Vendor List**
  - Confirmed vendor list with IT Harvest
  - Coverage: SQL query engines + OLAP analytics platforms
  - Prioritization: Security-relevant platforms first

- [ ] **Specify Data Points Required**
  - **Platform Capabilities**:
    - [ ] Version/release history (last 12 months)
    - [ ] Feature matrix (Iceberg support, security features, performance claims)
    - [ ] Pricing model (per-node, per-query, serverless)
    - [ ] Deployment options (cloud, on-premises, hybrid)
  - **Market Position**:
    - [ ] Customer counts (if available)
    - [ ] Funding/M&A activity
    - [ ] Analyst mentions (Gartner, Forrester, IDC)
  - **Technical Evolution**:
    - [ ] Major feature launches
    - [ ] Performance benchmarks (if published)
    - [ ] Security certifications

- [ ] **Establish Data Delivery Format**
  - Preferred format: CSV, JSON, structured markdown, API
  - Field definitions agreed upon
  - Sample data reviewed and validated

### Pilot Execution

- [ ] **Receive First Data Drop** (Query Engines)
  - Date received: _____________
  - Data coverage: _____________ vendors
  - Data quality assessment: _____________

- [ ] **Create First Platform Update**
  - Document vendors in `platforms/query-engines.md`
  - Document vendors in `platforms/olap-analytics.md`
  - Use data to populate quarterly update template
  - Cross-reference with MASTER-BIBLIOGRAPHY.md sources

- [ ] **Validate Data Quality**
  - Cross-check claims against vendor announcements
  - Verify version numbers and release dates
  - Identify gaps or inconsistencies
  - Provide feedback to IT Harvest

- [ ] **Generate Pilot Quarterly Update**
  - Use `vendor-landscape/quarterly-updates/TEMPLATE-YYYY-QX-update.md`
  - Complete Section 1: Query Engines & OLAP Platforms
  - Assign evidence levels to IT Harvest data (likely Level B)
  - Integrate with existing MASTER-BIBLIOGRAPHY.md sources

### Pilot Evaluation

- [ ] **Assess Pilot Success**
  - Data quality meets standards (accuracy, completeness, timeliness)
  - Integration workflow is efficient
  - Citation format works for academic/book purposes
  - Quarterly cadence is sustainable

- [ ] **Identify Improvements Needed**
  - Data gaps to address
  - Process refinements
  - Additional data points desired
  - Delivery format adjustments

- [ ] **Decision: Proceed to Full Partnership**
  - Go/No-Go decision date: _____________
  - Rationale: _____________

---

## Phase 3: Full Partnership - All Categories

### Expand Coverage

- [ ] **Infrastructure Layer**
  - Table formats: Iceberg, Delta, Hudi adoption tracking
  - Catalogs: Gravitino, Polaris, Unity, Nessie evolution
  - Object storage: S3, MinIO, Azure Blob feature updates

- [ ] **Security-Specific Platforms**
  - OCSF adoption: Vendor support, schema version tracking
  - Detection platforms: ClickHouse, security analytics platforms
  - Threat intel: MISP, OpenCTI, ThreatConnect updates

- [ ] **Platform Layer**
  - Query engines: Expanded to full vendor landscape
  - OLAP analytics: Market position tracking
  - Hybrid architectures: Emerging pattern identification

### Quarterly Update Process

- [ ] **Month 1: Data Collection & Integration**
  - Week 1: IT Harvest data refresh received
  - Week 2: Populate platforms/, infrastructure/, security-specific/ directories
  - Week 3: Update capability matrices and market trends
  - Week 4: Draft quarterly update (YYYY-QX-update.md)

- [ ] **Month 2: Expert Validation**
  - Week 1: Expert network review of IT Harvest findings
  - Week 2: Blog post synthesis (security-data-commons-blog integration)
  - Week 3: Hypothesis validation updates based on new data
  - Week 4: Finalize quarterly update draft

- [ ] **Month 3: Publication & Integration**
  - Week 1: Publish quarterly update to vendor-landscape/quarterly-updates/
  - Week 2: Update MASTER-BIBLIOGRAPHY.md with new sources
  - Week 3: Update CHANGELOG.md with version history
  - Week 4: Blog post publication announcing quarterly findings

### Quality Assurance

- [ ] **Maintain Evidence Level Standards**
  - IT Harvest data: Evidence Level B (industry data)
  - Cross-validation with Level A sources when possible
  - Target: 73%+ Evidence Level A overall (IT Harvest augments, doesn't replace)

- [ ] **Citation Stability**
  - Versioned quarterly snapshots (YYYY-QX-update.md)
  - Never edit published updates (create v2 if corrections needed)
  - CHANGELOG.md tracks all revisions

- [ ] **Vendor-Neutral Analysis**
  - No promotional content
  - Balanced trade-offs
  - Quantitative metrics prioritized
  - Acknowledge limitations and gaps

---

## Phase 4: Ongoing Operations

### Quarterly Cycle Execution

**Q1 Update (January):**
- [ ] Month 1: IT Harvest data refresh (Jan 1-31)
- [ ] Month 2: Expert validation (Feb 1-28)
- [ ] Month 3: Publication (Mar 1-31)
- [ ] Deliverable: 2026-Q1-update.md

**Q2 Update (April):**
- [ ] Month 1: IT Harvest data refresh (Apr 1-30)
- [ ] Month 2: Expert validation (May 1-31)
- [ ] Month 3: Publication (Jun 1-30)
- [ ] Deliverable: 2026-Q2-update.md

**Q3 Update (July):**
- [ ] Month 1: IT Harvest data refresh (Jul 1-31)
- [ ] Month 2: Expert validation (Aug 1-31)
- [ ] Month 3: Publication (Sep 1-30)
- [ ] Deliverable: 2026-Q3-update.md

**Q4 Update (October):**
- [ ] Month 1: IT Harvest data refresh (Oct 1-31)
- [ ] Month 2: Expert validation (Nov 1-30)
- [ ] Month 3: Publication (Dec 1-31)
- [ ] Deliverable: 2026-Q4-update.md

### Continuous Improvement

- [ ] **Feedback Loop with IT Harvest**
  - Quarterly feedback on data quality
  - Request adjustments to data points tracked
  - Identify new vendors to add to coverage

- [ ] **Integration with Book Manuscript**
  - Update book citations with quarterly data
  - Incorporate market trends into narrative
  - Reference versioned quarterly updates for citation stability

- [ ] **Blog Integration**
  - Quarterly blog post announcing vendor landscape findings
  - Deep-dives on specific platform evolutions
  - Practitioner feedback incorporation

---

## Success Metrics

### Pilot Project (Query Engines)
- [ ] Data quality: 90%+ accuracy vs vendor announcements
- [ ] Coverage: 10+ vendors documented
- [ ] Integration: First quarterly update published
- [ ] Timeline: 4-6 weeks from data receipt to publication

### Full Partnership (All Categories)
- [ ] Quarterly cadence maintained (4 updates/year)
- [ ] Evidence Level A: 73%+ maintained (IT Harvest = Level B augmentation)
- [ ] Expert validation: 2+ experts per quarterly update
- [ ] Blog integration: 1 blog post per quarterly update
- [ ] Book citations: Versioned updates referenced in manuscript

---

## Risk Mitigation

### Partnership Delays
- **Risk**: IT Harvest partnership takes longer than expected
- **Mitigation**: Continue Phase 1 (literature review) maintenance, proceed with book writing
- **Impact**: Phase 2 remains "nice to have," not blocking primary objectives

### Data Quality Issues
- **Risk**: IT Harvest data accuracy concerns
- **Mitigation**: Cross-validate with Level A sources, adjust evidence levels accordingly
- **Impact**: Downgrade to supplementary role if quality insufficient

### Quarterly Cadence Unsustainable
- **Risk**: 4 updates/year too aggressive
- **Mitigation**: Reduce to semi-annual (2 updates/year) or annual (1 update/year)
- **Impact**: Adjust expectations, maintain citation stability with longer intervals

---

## Contact Information

**IT Harvest Partnership**:
- Primary Contact: Charles Wells
- Email: _____________
- Phone: _____________
- Meeting Cadence: _____________

**Literature Review Team**:
- Lead: Jeremy Wiley
- Repository: security-data-literature-review
- Book: Modern Data Stack for Cybersecurity
- Blog: security-data-commons

**Expert Network** (for quarterly validation):
- Lisa Cao (Catalog landscape)
- Jake Thomas (DuckDB, edge processing)
- Additional experts as needed

---

## Appendix: Data Point Examples

### Query Engine Example (ClickHouse)
```markdown
**ClickHouse**:
- Version: 24.10 released (Oct 2024)
- Key features: Native IPv4/IPv6 types, vectorized query execution
- Performance: 6M req/sec (Cloudflare validation)
- Pricing: Open-source (Apache 2.0), ClickHouse Cloud (pay-per-query)
- Security features: Row-level security, encryption at rest
- Adoption indicators: Shell (57TB/day), Cloudflare, Uber
- Evidence level: A (production deployments) + B (IT Harvest market data)
```

### Capability Matrix Example
| Vendor | Iceberg Support | Security Features | Pricing Model | Evidence Level |
|--------|----------------|-------------------|---------------|----------------|
| Trino | ✅ Native | RBAC, row-level | Open-source | A (production) |
| Dremio | ✅ Native | RBAC, query audit | Per-user | B (IT Harvest) |
| ClickHouse | ⚠️ Via Iceberg REST | Row-level, encryption | Open-source + cloud | A (production) |

### Market Trend Example
```markdown
**Apache Iceberg Adoption Trend**:
- Q4 2024: Industry consensus = de facto standard
- Vendor support: AWS, Google, Snowflake, Databricks (universal)
- Community: 300+ contributors, 100+ organizations
- Dremio survey (2024): 29% planning Iceberg vs 23% Delta (next 3 years)
- Evidence level: B (industry survey) + A (vendor announcements)
- Hypothesis H-ARCH-01: STRONGLY VALIDATED (updated from 76% to industry consensus)
```

---

**Last Updated**: October 15, 2025
**Status**: Pre-Partnership Planning
**Next Action**: Initial outreach to Charles Wells
