# MCP Server Integration Plan

**Purpose**: Roadmap for integrating literature review with MCP server
**Status**: Implementation Phase
**Started**: 2025-10-22
**Target Completion**: Week of 2025-10-28

---

## Integration Goals

1. **Single Source of Truth**: Literature review becomes authoritative vendor data source
2. **Evidence-Based Rigor**: All vendor capability scores backed by Evidence Tier A/B sources
3. **Citation Stability**: Quarterly versioning enables stable academic citations
4. **Automated Sync**: Sync script propagates updates from lit review → MCP server
5. **Quality Assurance**: Validation rules ensure evidence tier standards

---

## Implementation Phases

### Phase 1: Schema & Infrastructure (Oct 22-23) ✅ IN PROGRESS

**Deliverables**:
- [x] Define integrated vendor database schema
- [x] Create `vendor-landscape/vendor-database-schema.md`
- [x] Document integration architecture
- [ ] Create initial `vendor-database.json` (starter with 3 exemplar vendors)
- [ ] Build `scripts/sync_from_literature_review.py`

**Owner**: Jeremy + Claude
**Duration**: 2 days
**Status**: 60% complete

---

### Phase 2: Vendor Migration (Oct 24-26)

**Deliverables**:
- [ ] Migrate 64 existing MCP vendors to integrated schema
- [ ] Annotate capability scores with evidence tiers
- [ ] Link all sources to MASTER-BIBLIOGRAPHY.md
- [ ] Map vendors to technology decision tree
- [ ] Assign journey persona fit

**Approach**:
- Start with top 10 high-value vendors (ClickHouse, Trino, Dremio, Splunk, Sentinel, etc.)
- Use semi-automated migration script with manual evidence annotation
- Validate against existing literature review evidence
- Target: 20 vendors/day = 3-4 days total

**Owner**: Jeremy (manual evidence review) + Claude (automation)
**Duration**: 3-4 days
**Status**: Not started

---

### Phase 3: Sync Automation (Oct 27-28)

**Deliverables**:
- [ ] Complete `sync_from_literature_review.py` script
- [ ] Build `validate_evidence_tiers.py` quality checker
- [ ] Create `generate_integration_report.py`
- [ ] Test end-to-end sync workflow
- [ ] Document sync process in README.md

**Workflow**:
```bash
# From MCP server directory
cd ~/security-architect-mcp-server
python scripts/sync_from_literature_review.py

# Output:
# ✓ Loaded 64 vendors from literature review
# ✓ Validated evidence tiers (79% Tier A)
# ✓ Checked bibliography references (327 sources)
# ✓ Generated vendor_database.json
# ✓ Created INTEGRATION_STATUS.md report
```

**Owner**: Jeremy + Claude
**Duration**: 2 days
**Status**: Not started

---

### Phase 4: MCP Tool Integration (Oct 29-30)

**Deliverables**:
- [ ] Update `generate_report.py` to cite bibliography sources
- [ ] Enhance `match_journey.py` with decision tree mapping
- [ ] Add evidence tier filtering to `filter_vendors.py`
- [ ] Update test suite for integrated schema
- [ ] Document new MCP capabilities

**New MCP Features**:
1. **Evidence-Based Filtering**: Filter by evidence tier (e.g., "Show me only vendors with Tier A evidence")
2. **Citation Generation**: Architecture reports include bibliography citations
3. **Decision Tree Navigation**: Journey matching references specific decision tree nodes
4. **Evidence Transparency**: Show confidence levels and source counts in vendor listings

**Owner**: Jeremy + Claude
**Duration**: 2 days
**Status**: Not started

---

### Phase 5: Documentation & Beta Testing (Oct 31-Nov 1)

**Deliverables**:
- [ ] Update MCP server README.md with integration details
- [ ] Create INTEGRATION_STATUS.md template
- [ ] Document quarterly update workflow
- [ ] Beta test with 2-3 test conversations
- [ ] Generate sample architecture report with citations

**Owner**: Jeremy
**Duration**: 2 days
**Status**: Not started

---

## Success Criteria

### Evidence Quality
- ✅ 70%+ Evidence Tier A sources (Target: Match lit review's 79%)
- ✅ All capability scores 4-5 have Tier A/B evidence
- ✅ All sources link to MASTER-BIBLIOGRAPHY.md
- ✅ Confidence levels align with evidence tier distribution

### Integration Completeness
- ✅ 64 vendors migrated to integrated schema
- ✅ Technology decision tree mapped to all vendors
- ✅ Journey persona fit assessed for all vendors
- ✅ Sync script runs without errors

### MCP Functionality
- ✅ Architecture reports include bibliography citations
- ✅ Evidence tier filtering works
- ✅ Decision tree navigation functional
- ✅ All 178 tests passing (fix existing 1 failure)

---

## Risk Mitigation

### Risk 1: Evidence Annotation is Time-Consuming

**Likelihood**: High
**Impact**: Medium (delays timeline 3-5 days)

**Mitigation**:
- Use existing literature review evidence (already 79% Tier A)
- Focus on top 20 vendors first (80/20 rule)
- Semi-automate with script that suggests evidence from MASTER-BIBLIOGRAPHY.md
- Accept "pending evidence annotation" for lower-priority vendors initially

---

### Risk 2: Schema Migration Breaks MCP Tests

**Likelihood**: Medium
**Impact**: High (MCP server non-functional)

**Mitigation**:
- Create `vendor_database.json.backup` before migration
- Run test suite after each migration batch
- Maintain backward compatibility in MCP tools (gracefully handle missing evidence fields)
- Feature flag for integrated schema (fallback to legacy if needed)

---

### Risk 3: Evidence Sources Missing from Bibliography

**Likelihood**: Medium
**Impact**: Low (broken citation links)

**Mitigation**:
- Validation script checks all `lit_review_ref` links
- Add missing sources to MASTER-BIBLIOGRAPHY.md during migration
- Flag unknown sources for manual review
- Allow "pending bibliography entry" with issue tracking

---

## Quarterly Update Workflow (Post-Integration)

Once integration is complete, quarterly updates follow this process:

### January, April, July, October

**Week 1-2: Data Collection**
1. IT Harvest API refresh (when available)
2. Manual vendor research (new platforms, pricing updates)
3. Evidence source validation (check for broken links)
4. Add new vendors (target: 5-10 per quarter → 80+ by end 2026)

**Week 3: Expert Validation**
1. Expert network review (Lisa Chao, Jake Thomas)
2. Hypothesis validation updates
3. Contradiction resolution
4. Confidence level adjustments

**Week 4: Publication & Sync**
1. Create `quarterly-updates/2025-QX-update.md` snapshot
2. Update CHANGELOG.md
3. Run `sync_from_literature_review.py`
4. Validate MCP test suite passes
5. Publish blog post on quarterly update

**Effort**: ~20 hours per quarter = 5 hours/month sustained

---

## Integration Architecture Diagram

```
┌───────────────────────────────────────────────────────────────┐
│ LITERATURE REVIEW (Master Data)                               │
│ ~/security-data-literature-review/                            │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│  vendor-landscape/                                            │
│  ├── vendor-database.json ← EDIT HERE                         │
│  ├── vendor-database-schema.md                                │
│  ├── INTEGRATION-PLAN.md (this file)                          │
│  └── quarterly-updates/                                       │
│      ├── 2025-Q4-update.md                                    │
│      └── vendor-database-2025-Q4.json (frozen snapshot)       │
│                                                                │
│  analysis-bundles/                                            │
│  ├── technology-decision-tree.md ← Decision logic             │
│  ├── cost-reality-reference.md                                │
│  └── performance-benchmarks-table.md                          │
│                                                                │
│  MASTER-BIBLIOGRAPHY.md ← All citations                       │
│  CHANGELOG.md ← Version tracking                              │
└───────────────────────────────────────────────────────────────┘
                              ↓
                    sync_from_literature_review.py
                              ↓
┌───────────────────────────────────────────────────────────────┐
│ MCP SERVER (Generated Artifact)                               │
│ ~/security-architect-mcp-server/                              │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│  data/                                                         │
│  ├── vendor_database.json ← AUTO-GENERATED (DO NOT EDIT!)     │
│  ├── .last_sync ← Sync metadata                               │
│  └── INTEGRATION_STATUS.md ← Sync report                      │
│                                                                │
│  scripts/                                                      │
│  ├── sync_from_literature_review.py                           │
│  ├── validate_evidence_tiers.py                               │
│  └── generate_integration_report.py                           │
│                                                                │
│  src/tools/                                                    │
│  ├── generate_report.py ← Cites bibliography                  │
│  ├── match_journey.py ← Maps to decision tree                 │
│  └── filter_vendors.py ← Evidence tier filtering              │
└───────────────────────────────────────────────────────────────┘
                              ↓
                    Architect uses MCP Server
                              ↓
┌───────────────────────────────────────────────────────────────┐
│ ARCHITECTURE REPORT (Output)                                  │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│  ## Vendor Recommendation: ClickHouse                          │
│                                                                │
│  **Evidence Quality**: Tier A (5 sources, confidence 5/5)     │
│                                                                │
│  **Query Performance**: ClickHouse achieves sub-second query   │
│  performance for 96% of queries in production (Cloudflare      │
│  deployment, 6M req/sec) [1] and handles 57TB/day security     │
│  telemetry (Shell case study) [2].                             │
│                                                                │
│  **Decision Tree Fit**: Batch - ClickHouse + Iceberg           │
│  (Question 4, Option A: High-volume OLAP)                      │
│                                                                │
│  **Journey Persona**: Marcus (High Fit) - Data engineering     │
│  background aligns with ClickHouse operational complexity.     │
│                                                                │
│  **References**:                                               │
│  [1] Cloudflare. "HTTP Analytics for 6M Requests/Second Using  │
│      ClickHouse." 2024.                                        │
│  [2] Altinity. "Shell ClickHouse Security Telemetry: 57TB/day  │
│      Production Scale." 2024.                                  │
│                                                                │
│  Evidence based on literature review version 2025-Q4.          │
└───────────────────────────────────────────────────────────────┘
```

---

## Next Immediate Actions (Today)

1. ✅ Create schema documentation (DONE)
2. ⏳ Create starter `vendor-database.json` with 3 exemplar vendors (ClickHouse, Trino, Splunk)
3. ⏳ Build basic `sync_from_literature_review.py` script
4. ⏳ Test sync workflow end-to-end

**Time Estimate**: 4-6 hours remaining today

---

## Questions for Jeremy

1. **Prioritization**: Should we migrate all 64 vendors this week, or start with top 20 and expand iteratively?
2. **Evidence Annotation Depth**: How detailed should evidence sources be initially? (Full annotation vs placeholder for Phase 2?)
3. **IT Harvest Timing**: Should we wait for IT Harvest partnership or proceed with manual updates?
4. **Beta Testing**: Do you have 2-3 architects ready for beta testing once integration is complete?

---

**Status**: Phase 1 in progress (60% complete)
**Next Session**: Create exemplar vendors + sync script
**Owner**: Jeremy Wiley + Claude
**Last Updated**: 2025-10-22
