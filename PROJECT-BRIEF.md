# PROJECT BRIEF: Security Data Literature Review

**Created**: October 19, 2025
**Methodology**: Memory Prompts Prompt 3 (Project Brief Compiler) - 26 Questions
**Purpose**: Comprehensive project context separating confirmed facts from assumptions
**Lifecycle**: PROJECT-SCOPED (12+ months active, quarterly updates planned)

---

## PART 1: CANONICAL FACTS (Confirmed with Sources)

### Fact 1: Phase 1-2C Complete, 76+ Sources Documented ✅
**CONFIRMED**: Phase 1 (Literature Extraction) complete with 76+ sources documented
- 283 footnotes extracted from best practices document
- 79% Evidence Level A (production/academic sources) - **EXCEEDS 73% target**
- 9 analysis bundles created (170,100 words evidence synthesis)
- All book chapters have supporting source citations
- **Source**: README.md lines 15-23, REPOSITORY-STATUS.md, CLAUDE.md lines 33-44

### Fact 2: 7 Hypotheses Validated with Quantitative Evidence ✅
**CONFIRMED**: Strong quantitative validation for 7 hypotheses
- **H-ARCH-01** (Iceberg Dominance): 76% adoption, 5 sources
- **H-IMPL-01** (TCO Reality): 2.5-3× operational costs, 5 sources
- **H-IMPL-02** (Staffing Scarcity): 2.7× staff required, 4 sources
- **H-IMPL-03** (Timeline Premium): 5.5 months average, 3 sources
- **H-COST-09** (Tiered Storage): 55-80% cost savings, 3 sources
- **H3-PERFORMANCE-01** (ClickHouse): 6M req/sec, 96% <1s queries
- **H-STREAM-01** (Kafka Streams): Production security patterns, 3 sources
- **Source**: README.md lines 108-117, LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md

### Fact 3: Expert Interview Guides Prepared for Week 3 ✅
**CONFIRMED**: Interview guides complete for expert validation
- **Lisa Cao** (Dremio): Catalog adoption, XTable validation, H-ARCH-03 (12 questions)
- **Jake Thomas** (Okta): DuckDB edge processing, H-EDGE-01, data volumes (14 questions)
- Guides include primary questions + follow-ups + hypothesis validation sections
- **Source**: README.md line 22, EXPERT-INTERVIEW-GUIDE-LISA-CHAO.md, EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md, CLAUDE.md line 134

### Fact 4: Blog Integration Established (1 Post Published, 4-6× Speedup) ✅
**CONFIRMED**: Literature review successfully integrated with blog workflow
- 1 blog post published using literature review sources
- 4-6× speedup demonstrated for evidence-based blog writing
- Literature review serves as foundation for blog deep-dives
- **Source**: README.md line 20, SESSION-2025-10-15-FINAL-INTEGRATION-BLOG-BOOK.md

### Fact 5: Academic Publication Quality Maintained ✅
**CONFIRMED**: Evidence standards suitable for peer review
- 79% Evidence Level A (57 of 72 sources) - production deployments + peer-reviewed research
- 21% Evidence Level B (15 of 72 sources) - industry analysts
- 0% Evidence Level C/D - zero low-quality sources
- Government/Standards: 8 sources (CISA, MITRE, DARPA, NSA, SANS)
- Industry Analysts: 10 sources (Gartner, IDC, Forrester)
- Production Deployments: 18+ companies (Netflix, Uber, LinkedIn, Cloudflare, Shell, SK Telecom)
- Metadata Completeness: 97% (70 of 72 entries complete)
- **Source**: README.md lines 119-125, CLAUDE.md lines 87-93, 189-193

### Fact 6: PRISMA-Aligned Extraction Methodology ✅
**CONFIRMED**: Systematic extraction methodology documented
- LITERATURE-EXTRACTION-PLAN.md provides complete methodology
- Standardized source format (Title, Author, Year, Type, Evidence Level, Hypothesis Links)
- Version control via CHANGELOG.md for academic citation stability
- **Source**: README.md lines 36-37, CLAUDE.md lines 73-77

### Fact 7: Quarterly Update Process Planned (Not Yet Active) ✅
**CONFIRMED**: Phase 2 quarterly update process designed
- Quarterly cycle: Jan, Apr, Jul, Oct
- Month 1: IT Harvest data refresh + platform updates
- Month 2: Expert validation + blog synthesis
- Month 3: Publication + citation updates
- Versioned snapshots (YYYY-QX-update.md) for citation stability
- **Source**: README.md lines 80-95, CLAUDE.md lines 217-233

### Fact 8: Directory Structure Planned for Phase 2 ✅
**CONFIRMED**: Future structure designed for vendor landscape integration
- `platforms/`: Query engines, OLAP analytics, hybrid architectures
- `infrastructure/`: Table formats, catalogs, object storage
- `security-specific/`: OCSF adoption, detection platforms, threat intel
- `vendor-landscape/`: Capability matrix, market trends (IT Harvest powered)
- **Source**: README.md lines 54-75, CLAUDE.md lines 195-215

### Fact 9: Book Integration Complete for All Chapters ✅
**CONFIRMED**: All book chapters have supporting citations
- MASTER-BIBLIOGRAPHY.md provides evidence foundation
- 115,500-word manuscript supported by 76+ sources
- Literature review cited throughout 11 chapters + 5 appendices
- **Source**: README.md lines 100-103, CLAUDE.md lines 236-240

### Fact 10: Claude Skill for Evidence Classification Operational ✅
**CONFIRMED**: evidence-tier-classifier skill active for quality management
- Activates during source additions, citation updates, bibliography work
- Classifies Tier 1-5 evidence with rationale (Tier 1=Production, Tier 2=Peer-reviewed, etc.)
- Maintains 79% Evidence Level A quality standard
- **Source**: CLAUDE.md lines 111-116

---

## PART 2: ASSUMPTIONS REQUIRING VERIFICATION

### Assumption 1: IT Harvest Partnership Will Be Established ⚠️
**ASSUMPTION**: IT Harvest partnership (Charles Wells collaboration) will provide vendor landscape data for Phase 2
- **Verification needed**: Partnership agreement, data access confirmed, pilot scope defined
- **Impact if false**: Phase 2 delayed, need alternative vendor data sources (manual curation, direct vendor outreach)
- **Evidence gap**: No confirmed partnership agreement yet (October 19, 2025)
- **Source**: README.md lines 27-28, 93-94, CLAUDE.md lines 247-250

### Assumption 2: Quarterly Updates Will Begin Q4 2025 or Q1 2026 ⚠️
**ASSUMPTION**: First quarterly update will launch Q4 2025 or Q1 2026
- **Verification needed**: IT Harvest partnership timeline, resource allocation confirmed
- **Impact if false**: Literature review becomes stale, blog/book lack current vendor data
- **Evidence gap**: Dependent on Assumption 1 (partnership establishment)
- **Source**: README.md line 130, CLAUDE.md line 302

### Assumption 3: Expert Interviews Will Validate All Quantitative Claims ⚠️
**ASSUMPTION**: Week 3 expert interviews (Lisa Cao, Jake Thomas) will confirm quantitative claims
- **Lisa Cao**: Catalog adoption rates, XTable validation, H-ARCH-03 (Gravitino meta-catalog)
- **Jake Thomas**: DuckDB deployment data (7.5T records, 1.5-50 TB/day), H-EDGE-01 (edge processing viability)
- **Verification needed**: Conduct 2 interviews Week 3 (October 21-25, 2025)
- **Impact if false**: Downgrade hypothesis confidence from "STRONGLY VALIDATED" to "VALIDATED" or "PRELIMINARY", add caveats
- **Source**: README.md line 22, EXPERT-INTERVIEW-GUIDE-LISA-CHAO.md, EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md

### Assumption 4: Academic Publication (ACM CSUR) Will Accept Literature Review ⚠️
**ASSUMPTION**: Literature review quality sufficient for ACM Computing Surveys publication
- **Verification needed**: Peer review submission, acceptance (12-18 month timeline)
- **Impact if false**: Adjust publication venue (IEEE Security & Privacy, conferences instead), still suitable for blog/book
- **Evidence gap**: No submission yet, PUBLICATION-VENUE-RECOMMENDATIONS.md provides strategy
- **Source**: README.md line 26, PUBLICATION-VENUE-RECOMMENDATIONS.md

### Assumption 5: 79% Evidence Level A Can Be Maintained with Quarterly Updates ⚠️
**ASSUMPTION**: Quarterly vendor landscape updates will maintain 79% Evidence Level A quality
- **Verification needed**: First quarterly update completed, evidence levels re-assessed
- **Impact if false**: Accept lower evidence quality (70-75% Level A), focus on Level B vendor documentation
- **Risk**: IT Harvest data may be Level B (vendor-provided), not Level A (production deployments)
- **Source**: README.md lines 119-122, CLAUDE.md lines 87-93

### Assumption 6: Blog Will Continue Driving Source Identification ⚠️
**ASSUMPTION**: 3x/week blog cadence will consistently identify new sources for literature review
- **Verification needed**: Track blog posts over 3 months, measure new source identification rate
- **Impact if false**: Proactive source hunting required (conference monitoring, academic searches)
- **Evidence**: 1 post demonstrated 4-6× speedup, but sustained rate unproven
- **Source**: README.md line 20, CLAUDE.md lines 241-244

---

## PART 3: SCOPE & BOUNDARIES

**In Scope**:
- Literature review supporting "Modern Data Stack for Cybersecurity" book
- Evidence foundation for 11 book chapters + 5 appendices
- Hypothesis validation (32 hypotheses total, 7 validated so far)
- Quarterly updates for vendor landscape (Phase 2, pending IT Harvest)
- Academic quality suitable for peer review (ACM CSUR, IEEE S&P targets)
- Blog integration (source identification, evidence-based writing)
- Expert network validation (Lisa Cao, Jake Thomas, a data-platform practitioner, Paul Agbabian)

**Out of Scope**:
- Not a comprehensive systematic review of ALL cybersecurity literature (focused on modern data stack)
- Not covering traditional SIEM implementations (focus on modern data architecture)
- Not operational tooling (pure research, not code/implementation)
- Not covering every vendor (focus on query engines, table formats, catalogs per Chapter 9)
- Not a book chapter itself (supporting research infrastructure)

**Boundaries**:
- **Domain**: Cybersecurity + data engineering intersection
- **Time Period**: 2018-2025 (modern data stack era), pre-2018 for foundational context
- **Geographic**: Global (US/EU/APAC production deployments documented)
- **Evidence Quality**: Minimum Level B (no Level C/D sources), target 73%+ Level A

---

## PART 4: PRIOR DECISIONS & RATIONALE

### Decision 1: PRISMA-Aligned Methodology (October 15, 2025)
**Decision**: Adopt PRISMA-aligned systematic extraction methodology
**Rationale**:
- Academic publication requires systematic, reproducible methodology
- PRISMA provides standardized reporting for literature reviews
- Enables peer review acceptance (ACM CSUR, IEEE S&P targets)
- Supports citation stability via version control (CHANGELOG.md)
**Made by**: Jeremy (Project Lead)
**Reversible?**: No (fundamental to project credibility)

### Decision 2: Evidence Level A Target 73%+ (Phase 1)
**Decision**: Maintain 73%+ Evidence Level A (production deployments, peer-reviewed research)
**Rationale**:
- Academic quality requires strong evidence (not blog posts, marketing)
- 73% provides credibility while allowing 27% Level B (industry analysts)
- Government/standards sources prioritized (CISA, MITRE, DARPA, NSA, SANS)
- Production deployments > vendor claims (Netflix, Uber > marketing materials)
**Made by**: Jeremy (Project Lead)
**Reversible?**: Partially (could adjust to 70-75% if quarterly updates dilute quality)

### Decision 3: Quarterly Update Cycle (Jan/Apr/Jul/Oct)
**Decision**: Quarterly updates (not monthly or annual) for Phase 2 vendor landscape
**Rationale**:
- Quarterly balances currency vs maintenance burden
- Aligns with book revision cycles (quarterly feedback incorporation)
- Supports blog cadence (3x/week can draw from quarterly research)
- IT Harvest partnership model (assuming Charles Wells collaboration)
**Made by**: Jeremy (Project Lead)
**Reversible?**: Yes (could adjust to bi-annual if quarterly proves too frequent)

### Decision 4: Versioned Snapshots (YYYY-QX-update.md)
**Decision**: Create versioned snapshots for each quarterly update (not edit existing files)
**Rationale**:
- Academic citation stability (papers cite specific versions, not moving target)
- CHANGELOG.md tracks all revisions for auditing
- Never edit published versions (prevents citation rot)
- Enables temporal analysis (how did vendor landscape evolve Q1→Q2?)
**Made by**: Jeremy (Project Lead)
**Reversible?**: No (fundamental to academic citation credibility)

### Decision 5: Blog Integration (Not Separate Publication)
**Decision**: Integrate literature review with blog (not separate standalone publication initially)
**Rationale**:
- 4-6× speedup demonstrated for evidence-based blog writing
- Blog posts drive new source identification (feedback loop)
- Literature review serves blog, book, and eventual academic publication
- Avoids duplicating content across repositories
**Made by**: Jeremy (Project Lead)
**Reversible?**: Yes (could extract standalone publication later if needed)

### Decision 6: Focus on Chapter 9 Vendor Landscape (Phase 2 Priority)
**Decision**: Prioritize Chapter 9 "Technology State Assessment" for IT Harvest integration
**Rationale**:
- Chapter 9 requires current vendor landscape (query engines, catalogs, table formats)
- IT Harvest partnership provides systematic vendor data (vs ad-hoc curation)
- Query engines pilot project (first integration, learn process)
- Other chapters already well-cited with production deployment sources
**Made by**: Jeremy (Project Lead)
**Reversible?**: Partially (could expand to other chapters if pilot succeeds)

### Decision 7: Expert Interviews for Quantitative Validation
**Decision**: Conduct expert interviews (Lisa Cao, Jake Thomas) to validate quantitative claims
**Rationale**:
- 7 hypotheses have quantitative claims (76% adoption, 2.5-3× costs, 2.7× staffing)
- Expert validation strengthens evidence (personal communication = additional source)
- Interview guides ensure systematic, reproducible questioning
- Aligns with Week 3 expert interview schedule (October 21-25, 2025)
**Made by**: Jeremy (Project Lead)
**Reversible?**: No (interviews already scheduled)

---

## PART 5: PENDING DECISIONS & TRADE-OFFS

### Pending Decision 1: IT Harvest Partnership Model
**Decision needed**: Partnership structure (revenue share, licensing, collaboration model)
**Options**:
1. **Revenue share**: IT Harvest provides data, share blog/book revenue
2. **Licensing**: Pay for data access (annual fee)
3. **Collaboration**: Co-author quarterly updates, mutual promotion
4. **Free pilot**: Query engines pilot, evaluate value before commitment
**Trade-offs**:
- Revenue share: Aligns incentives, but book revenue uncertain
- Licensing: Predictable cost, but upfront investment
- Collaboration: Lower cost, but requires IT Harvest time commitment
- Free pilot: Low risk, but may not scale to full vendor landscape
**Decision timeline**: Week 4-5 (after expert interviews complete)
**Blocking**: Phase 2 cannot start without partnership model

### Pending Decision 2: Academic Publication Timing
**Decision needed**: When to submit literature review for academic publication (ACM CSUR, IEEE S&P)
**Options**:
1. **Immediate** (Q4 2025): Submit Phase 1 literature review now
2. **After Q1 2026 update**: Include first quarterly update for stronger contribution
3. **After book publication** (mid-2026): Avoid competing with book, submit after book published
4. **No academic publication**: Focus on blog/book only (faster iteration)
**Trade-offs**:
- Immediate: Establishes academic credibility early, but Phase 1 only (no vendor landscape)
- After Q1 update: Stronger contribution (quarterly update process documented), but delayed
- After book: Avoids competition, but academic publication delayed 12+ months
- No publication: Faster iteration, but loses academic credibility signal
**Decision timeline**: Month 2 (after first quarterly update if IT Harvest partnership succeeds)
**Blocking**: Not blocking other work (can proceed with blog/book regardless)

### Pending Decision 3: Evidence Level A Target for Phase 2
**Decision needed**: Maintain 79% Level A with quarterly updates, or accept 70-75%?
**Options**:
1. **Maintain 79%**: Strict quality standard (production deployments only)
2. **Accept 70-75%**: Allow more Level B vendor documentation (IT Harvest data)
3. **Separate standards**: 79% for core hypotheses, 70% for vendor landscape
4. **Adaptive**: Adjust target based on Phase 2 data availability
**Trade-offs**:
- Maintain 79%: Academic credibility, but may limit vendor landscape coverage
- Accept 70-75%: Broader coverage, but lower evidence quality
- Separate standards: Pragmatic, but adds complexity
- Adaptive: Flexible, but risks "slippery slope" quality degradation
**Decision timeline**: After first quarterly update (evaluate IT Harvest data quality)
**Blocking**: Not blocking Phase 2 start (can adjust target retroactively)

### Pending Decision 4: Paul Agbabian Expert Interview
**Decision needed**: Should Paul Agbabian be interviewed for OCSF production deployment validation?
**Options**:
1. **Yes, Week 3**: Add to Lisa Cao + Jake Thomas interview schedule
2. **Yes, Week 4-5**: Conduct separately after Lisa/Jake interviews
3. **No, email instead**: Send written questions, less time-intensive
4. **Defer to Phase 2**: Wait for IT Harvest partnership, may provide OCSF adoption data
**Trade-offs**:
- Yes Week 3: Comprehensive validation, but 3 interviews in 1 week (time-intensive)
- Yes Week 4-5: Spread workload, but delays OCSF validation
- Email instead: Faster, but less depth, may not capture nuance
- Defer: Reduced workload, but OCSF adoption claims remain unvalidated
**Decision timeline**: Week 3 (before Lisa/Jake interviews if adding Paul)
**Blocking**: Not blocking other work (OCSF hypotheses already "VALIDATED", expert interview would strengthen to "STRONGLY VALIDATED")

---

## PART 6: RISKS, ASSUMPTIONS & CONSTRAINTS

### High-Probability Risks

**Risk 1: IT Harvest Partnership Delays Phase 2**
- Probability: 40% (HIGH)
- Impact: 3-6 month delay for quarterly updates
- Mitigation: Develop fallback plan (manual vendor curation, alternative data sources)
- Contingency: Use blog posts + direct vendor outreach for Chapter 9

**Risk 2: Expert Interviews Don't Validate Quantitative Claims**
- Probability: 25% (MEDIUM)
- Impact: Downgrade hypothesis confidence, add caveats to book
- Mitigation: Prepare downgrade language now ("preliminary findings pending validation")
- Contingency: Seek additional expert interviews (a data-platform practitioner, Paul Agbabian backups)

**Risk 3: Quarterly Update Maintenance Burden Too High**
- Probability: 30% (MEDIUM)
- Impact: Quarterly updates become bi-annual (loss of currency)
- Mitigation: Automate data ingestion (IT Harvest API if available), template workflows
- Contingency: Reduce scope (query engines + table formats only, drop catalogs/storage)

### Medium-Probability Risks

**Risk 4: Blog Cadence Slows, Source Identification Decreases**
- Probability: 20% (LOW-MEDIUM)
- Impact: Literature review stagnates (no new sources), relies only on quarterly updates
- Mitigation: Proactive source hunting (conference monitoring, academic searches, alerts)
- Contingency: Phase 2 quarterly updates become primary source identification mechanism

**Risk 5: Academic Publication Rejection**
- Probability: 40% (MEDIUM - first submission often rejected)
- Impact: Revise and resubmit (6-12 month delay), or pivot to conference publication
- Mitigation: PUBLICATION-VENUE-RECOMMENDATIONS.md provides multiple venue options
- Contingency: Submit to conferences instead (shorter review cycles, broader reach)

### Unknowns

**Unknown 1: IT Harvest Data Quality** (Level A vs B vs C?)
- **Question**: Will IT Harvest data meet Evidence Level A standards (production deployments)?
- **Impact**: May dilute overall evidence quality from 79% to 70-75%
- **Resolution**: Pilot with query engines category, assess data quality before full commitment

**Unknown 2: Expert Interview Data Precision** (Exact numbers vs ranges?)
- **Question**: Will Lisa Cao/Jake Thomas provide exact deployment data, or ranges/estimates?
- **Impact**: Affects hypothesis confidence (exact = STRONGLY VALIDATED, ranges = VALIDATED)
- **Resolution**: Interview guides prepared with specific quantitative questions, follow-ups for precision

**Unknown 3: Quarterly Update Velocity** (Can maintain 4x/year?)
- **Question**: Is quarterly cadence sustainable with solo practitioner + blog + book commitments?
- **Impact**: May need to reduce to bi-annual updates (currency loss)
- **Resolution**: Track time for first quarterly update, extrapolate sustainability

### Blockers

**Blocker 1: IT Harvest Partnership Required for Phase 2**
- **Blocking**: All Phase 2 vendor landscape work
- **Resolution timeline**: Week 4-5 (Charles Wells outreach, partnership model agreement)
- **Impact**: ~50% of Phase 2 work blocked (vendor landscape), 50% can proceed (expert interviews, blog integration)

**Blocker 2: No Automated Vendor Data Ingestion**
- **Blocking**: Quarterly update scalability (manual curation doesn't scale)
- **Resolution timeline**: Month 2-3 (build automation scripts, API integration if available)
- **Impact**: Quarterly updates labor-intensive without automation (may force bi-annual cadence)

---

## PART 7: INTEGRATION POINTS & DEPENDENCIES

### Integration with Book Manuscript
- **Dependency**: Literature review provides evidence foundation for all 11 chapters + 5 appendices
- **Status**: ✅ Complete for Phase 1 (76+ sources cover all chapters)
- **Future**: Chapter 9 "Technology State Assessment" requires quarterly vendor landscape updates (Phase 2)
- **Repository**: https://github.com/flying-coyote/modern-data-stack-for-cybersecurity-book

### Integration with Blog
- **Dependency**: Blog posts cite literature review sources (4-6× speedup for evidence-based writing)
- **Status**: ✅ 1 post published demonstrating integration, ongoing 3x/week cadence
- **Future**: Blog posts drive new source identification (feedback loop for literature review)
- **Repository**: https://github.com/flying-coyote/security-data-commons

### Integration with Expert Network
- **Dependency**: Expert interviews validate quantitative claims (Lisa Cao, Jake Thomas, Paul Agbabian)
- **Status**: 🔄 Week 3 interviews scheduled (October 21-25, 2025)
- **Future**: Quarterly updates include expert validation cycle (Month 2 of each quarter)
- **Source**: second-brain expert network (1,444 thought leaders mapped, 45 actively tracked)

### Integration with IT Harvest Partnership
- **Dependency**: Vendor landscape data for Chapter 9, quarterly updates
- **Status**: ⏳ Partnership pending (Charles Wells collaboration)
- **Future**: Query engines pilot → Full vendor landscape integration
- **Impact**: ~50% of Phase 2 work (vendor-landscape/ directory, quarterly updates)

---

## PART 8: SUCCESS METRICS & VALIDATION

### Phase 1 Success Metrics (ACHIEVED ✅)
- ✅ 283 footnotes extracted from best practices document
- ✅ 76+ sources documented with standardized format
- ✅ 79% Evidence Level A (EXCEEDS 73% target)
- ✅ 7 hypotheses validated with quantitative evidence
- ✅ All book chapters have supporting citations
- ✅ Blog integration demonstrated (1 post, 4-6× speedup)

### Phase 2 Success Metrics (PENDING)
- ⏳ IT Harvest partnership established
- ⏳ Query engines pilot completed (first quarterly update)
- ⏳ Directory structure implemented (platforms/, infrastructure/, security-specific/, vendor-landscape/)
- ⏳ First quarterly update published (Q4 2025 or Q1 2026)
- ⏳ Expert interviews completed (Lisa Cao, Jake Thomas validation)
- ⏳ Academic publication submitted (ACM CSUR or IEEE S&P)

### Ongoing Quality Metrics
- **Maintain**: 79% Evidence Level A (production deployments, peer-reviewed research)
- **Maintain**: 97% metadata completeness (70 of 72 entries)
- **Increase**: Government/standards sources (currently 8, target 12+ with quarterly updates)
- **Increase**: Production deployments (currently 18, target 25+ with vendor landscape)

---

## PART 9: TIMELINE & MILESTONES

### Completed Milestones ✅
- **October 15, 2025**: Phase 1-2C complete (283 footnotes, 76+ sources, 79% Level A)
- **October 15, 2025**: 9 analysis bundles created (170,100 words evidence synthesis)
- **October 16, 2025**: Blog integration demonstrated (1 post published)
- **October 16, 2025**: Expert interview guides prepared (Lisa Cao, Jake Thomas)

### Upcoming Milestones (Next 4 Weeks)
- **Week 3 (Oct 21-25)**: Expert interviews (Lisa Cao, Jake Thomas)
- **Week 4 (Oct 28-Nov 1)**: IT Harvest partnership outreach (Charles Wells)
- **Week 4-5**: Blog launch (Oct 28), literature review sources cited in posts

### Phase 2 Milestones (Next 3-6 Months)
- **Month 2 (Nov 2025)**: IT Harvest partnership established, query engines pilot started
- **Month 3 (Dec 2025)**: First quarterly update published (Q4 2025 if partnership ready, else Q1 2026)
- **Month 4-6 (Jan-Mar 2026)**: Directory structure implemented, quarterly update process refined

### Long-Term Milestones (6-18 Months)
- **Month 6 (Apr 2026)**: Academic publication submitted (ACM CSUR or IEEE S&P)
- **Month 12 (Oct 2026)**: 4 quarterly updates completed, blog-literature feedback loop established
- **Month 18 (Apr 2027)**: Academic publication accepted (optimistic), book published with quarterly-updated literature review

---

## PART 10: AI CONTEXT & DOMAIN BACKGROUND

### Domain: Cybersecurity + Data Engineering Intersection

**Core Problem**: Security teams lack modern data engineering capabilities, relying on legacy SIEM platforms ($2M+/year costs, 250 GB/day scale limits, vendor lock-in)

**Modern Data Stack Solution**: Apache Iceberg (table format) + query engines (Trino, Dremio, DuckDB) + OCSF (schema standardization) enable petabyte-scale security data lakes at 10× lower cost

**Literature Gap**: Cybersecurity literature focuses on detection logic, data engineering literature ignores security requirements → This literature review bridges the gap

### Key Technologies Covered

- **Table Formats**: Apache Iceberg (76% adoption), Delta Lake, Apache Hudi
- **Query Engines**: Trino/Starburst, Dremio, Denodo, DuckDB, ClickHouse, Athena
- **Catalogs**: Gravitino (meta-catalog), Polaris, Unity Catalog, Nessie
- **Schemas**: OCSF (Open Cybersecurity Schema Framework), ECS (Elastic Common Schema)
- **Security Platforms**: Splunk, Elastic, Microsoft Sentinel, QRadar, Chronicle

### Evidence Quality Philosophy

**Evidence Tier System** (inherited from second-brain project):
- **Level A** (79% target): Production deployments (Netflix, Uber, LinkedIn), peer-reviewed research, government standards (CISA, MITRE)
- **Level B** (21% acceptable): Industry analysts (Gartner, IDC, Forrester), expert consensus, vendor documentation (if verified)
- **Level C** (0% rejected): Blog posts, conference talks (unless backed by production data)
- **Level D** (0% rejected): Marketing materials, unverified claims, speculation

**Rationale**: Academic publication requires strong evidence → Production deployments > vendor marketing

### Research Methodology Context

**PRISMA-Aligned Extraction**:
- Systematic, reproducible methodology for literature reviews
- Standardized reporting (LITERATURE-EXTRACTION-PLAN.md)
- Version control for citation stability (CHANGELOG.md)
- Enables peer review acceptance (ACM CSUR, IEEE S&P targets)

**Hypothesis-Driven Research**:
- 32 hypotheses total (29 from book, 3 from literature review gap analysis)
- 7 hypotheses validated so far (quantitative evidence, multiple sources)
- Expert interviews validate quantitative claims (Lisa Cao, Jake Thomas)

**Quarterly Update Model** (Phase 2):
- IT Harvest partnership provides systematic vendor data
- Quarterly cycle (Jan/Apr/Jul/Oct) balances currency vs maintenance
- Versioned snapshots (YYYY-QX-update.md) ensure citation stability

### Integration Strategy Context

**Three-Tier Content Strategy** (from second-brain project):
1. **Book** (115,500 words): Comprehensive, publication-ready, expert-validated
2. **Blog** (3x/week): Thought leadership, evidence-based, literature review sources
3. **Literature Review** (76+ sources): Foundation for book + blog, quarterly updates for currency

**Why Living Literature Review?**:
- Modern data stack evolves rapidly (quarterly vendor updates required)
- Blog posts drive new source identification (feedback loop)
- Academic publication establishes credibility (ACM CSUR, IEEE S&P targets)
- Expert network validation ensures quality (1,444 thought leaders mapped)

---

**Status**: Phase 1 complete, Phase 2 pending IT Harvest partnership
**Next Action**: Week 3 expert interviews (Lisa Cao, Jake Thomas validation)
**Priority**: HIGH - Foundation for book + blog, academic credibility signal
**Owner**: Jeremy Wiley (Project Lead)
