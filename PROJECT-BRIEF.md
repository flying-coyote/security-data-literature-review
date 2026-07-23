---
type: plan
title: "Security Data Literature Review Project Brief"
created: 2025-10-19
tags: [project-brief, literature-review, decisions-log, assumptions, project-scope]
---

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
- Level-A share: 41.9% live-computed 2026-07-23 (96/229 tiered) — the earlier "79% — EXCEEDS 73% target" self-grade was withdrawn in the 2026-06 audit; target recovery is open work
- 9 analysis bundles created (170,100 words evidence synthesis)
- All book chapters have supporting source citations
- **Source**: README.md lines 15-23, archive/REPOSITORY-STATUS.md (archived 2026-07-10), CLAUDE.md lines 33-44

### Fact 2: 9 Hypotheses Assessed with Quantitative Confidence Scoring ✅
**CONFIRMED**: 9 hypotheses assessed (7 original + 2 added post-audit 2026-07-10); scores below are the canonical 2026-07-13 mechanical rescore, and the withdrawn pre-audit multipliers are deliberately not restated here
*Scores are the 2026-07-13 rubric rescore (`methods/RESCORE-2026-07-13.md`, ruled canon 2026-07-16; it replaced the 2026-07-09 adopted values on seven of nine rows), matching PUBLICATION-MANUSCRIPT.md §3.7.*
- **H-ARCH-01** (Iceberg Dominance): STRONGLY VALIDATED, 23/25 - industry consensus as de facto standard (the "76% adoption" figure is unsourced — refined per the H-ARCH-01 audit)
- **H3-PERFORMANCE-01** (ClickHouse): HIGH CONFIDENCE, 19/25 - Cloudflare 6M req/sec production (the earlier 20/25 was off the rubric's anchor values)
- **H-STREAM-01** (Stateful Streaming): MODERATE, 15/25 - Samza (VLDB 2017) plus Azure production scale; two legs cap the source count, demoting the earlier High Confidence
- **H-LOGCOMP-01** (Machine-Data Compression; added 2026-07-10): HIGH CONFIDENCE, 17/25 - three peer-reviewed anchors
- **H-SOC-BASELINE-01** (SOC Alert Base Rates; added 2026-07-10): MODERATE, 13/25 - Yang et al. (USENIX Security 2024)
- **H-COST-09** (Tiered Storage): PRELIMINARY, 9/25 - savings band withdrawn; first-party S3 tier-delta bound; directional pending re-sourcing
- **H-IMPL-02** (Staffing Scarcity): PRELIMINARY, 5/25 - quantitative legs withdrawn; instrument floor; directional pending re-sourcing
- **H-IMPL-03** (Timeline Premium): PRELIMINARY, 5/25 - quantitative legs withdrawn; instrument floor; directional pending re-sourcing
- **H-IMPL-01** (Streaming TCO): PRELIMINARY, 5/25 - quantitative legs withdrawn; instrument floor; directional pending re-sourcing
- **Source**: PUBLICATION-MANUSCRIPT.md §3.7, RESCORE-PROPOSAL-2026-07.md, LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md

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
- **Status (2026-07-16)**: the blog channel this fact describes was the Security Data Commons Substack, retired 2026-05-24 and archived read-only; the essays now live at securitydataworks.com/writing

### Fact 5: Academic Publication Quality Maintained ✅
**CONFIRMED**: Evidence standards suitable for peer review
- 79% Evidence Level A (57 of 72 sources) - production deployments + peer-reviewed research — withdrawn 2026-06-05: this and the bullets below are the October 2025 pre-audit self-grade, kept as record; the honest Level-A figure is 41.9% (96/229 tiered, derived 2026-07-23 via scripts/automation_dashboard.py), and target recovery is open work
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

### Fact 7: Hybrid Update Model - Monthly Rolling + Quarterly Deep Synthesis ✅
**CONFIRMED**: Blog-aligned hybrid update strategy for living literature review
- **Monthly rolling updates**: New sources, corrections, community feedback (~6-8 hours/month)
- **Quarterly deep synthesis**: Comprehensive reviews, hypothesis validation, expert interviews (~24 hours/quarter)
- **Average effort**: ~18 hours/month (sustainable for solo practitioner with MCP automation)
- **Publication venue**: Online (Substack) as openly accessible resource, academic journal deferred to 2026
- **Versioning**: Rolling updates via git commits, quarterly snapshots (YYYY-QX-v1.0 tags) for citation stability
- **Philosophy**: "Being wrong publicly" - rapid iteration, intellectual honesty, collaborative corrections
- **Source**: Substack justification post (Oct 22, 2025), CLAUDE.md, MCP vendor database automation
- **Status (2026-07-16)**: three of these legs have since changed — the Substack venue was retired 2026-05-24 (writing moved to securitydataworks.com/writing); no automated weekly MCP refresh exists (the MCP server repo was archived 2026-07-01, and the vendor DB is refreshed quarterly in vendor-landscape/); and the publication venue was ruled by the owner 2026-07-10: Journal of Cybersecurity (Oxford)

### Fact 8: Directory Structure Planned for Phase 2 ✅
**CONFIRMED**: Future structure designed for vendor landscape integration
- `vendor-landscape/`: Capability matrix, market trends (IT Harvest powered) — the Phase-2 structure actually kept and maintained
- ~~`platforms/`, `infrastructure/`, `security-specific/`~~: empty README-only stubs, never populated; removed 2026-07-09 (topic coverage lives in MASTER-BIBLIOGRAPHY.md + analysis-bundles/)
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
- Maintains 79% Evidence Level A quality standard — withdrawn 2026-06-05: the 79% self-grade was withdrawn in the audit; the honest live figure is 41.9% (95/227 tiered, derived 2026-07-16)
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
**ASSUMPTION**: Q1 2026 expert interviews (Lisa Cao, Jake Thomas) will confirm quantitative claims
- **Lisa Cao**: Catalog adoption rates, XTable validation, H-ARCH-03 (Gravitino meta-catalog)
- **Jake Thomas**: DuckDB deployment data (7.5T records, 1.5-50 TB/day), H-EDGE-01 (edge processing viability), isolation-first validation (RQ7)
- **Verification needed**: Conduct 2 interviews as part of Q1 2026 quarterly deep dive (January 2026)
- **Impact if false**: Downgrade hypothesis confidence from "STRONGLY VALIDATED" to "VALIDATED" or "PRELIMINARY", add caveats
- **Source**: README.md, EXPERT-INTERVIEW-GUIDE-LISA-CHAO.md, EXPERT-INTERVIEW-GUIDE-JAKE-THOMAS.md

### Assumption 4: Academic Publication Deferred to 2026 (Online-First Strategy) ✅ REVISED
**REVISED STRATEGY**: Online publication (Substack) is primary venue, academic journal deferred
- **Current approach**: Published openly on Substack (Oct 22, 2025), 38,000 words, 75+ sources
- **Academic publication**: Deferred to mid-2026 after community validation and refinement
- **Rationale**: "Being wrong publicly" philosophy prioritizes rapid iteration and practitioner engagement over academic credibility signal
- **Future path**: Community-validated Substack version → Refined manuscript → Journal submission (ACM CSUR, USENIX, IEEE S&P) in 2026
- **Trade-off**: Broader practitioner reach (Substack) vs academic credibility (journal), online-first chosen
- **Source**: Substack blog posts (Oct 22, 2025), blog philosophy ("Security Architects Need to Be Wrong")
- **Status (2026-07-16)**: superseded twice — the Substack was retired 2026-05-24 (essays at securitydataworks.com/writing), and the venue question was ruled by the owner 2026-07-10: Journal of Cybersecurity (Oxford), not the ACM CSUR / USENIX / IEEE S&P shortlist above

### Assumption 5: 75%+ Evidence Level A Achievable with Monthly Rolling Updates ⚠️
**ASSUMPTION**: Monthly rolling updates can maintain ≥75% Evidence Level A (slight degradation from 79% acceptable)
- **Verification needed**: 3-month trial (Nov 2025 - Jan 2026), track quality metrics monthly
- **Impact if true**: Monthly updates sustainable, supports blog cadence, validates hybrid model
- **Impact if false**: Reduce to bi-monthly or quarterly, accept slower blog evidence refresh
- **Mitigation**: MCP vendor database automation (84% Tier A), evidence-tier-classifier skill, quarterly deep dives maintain rigor
- **Decision point**: February 2026 - Continue monthly (if quality ≥75%), adjust to bi-monthly/quarterly (if <75%)
- **Source**: MCP vendor database integration (84% Tier A automated), UltraThink analysis (Oct 30, 2025)

### Assumption 6: Blog Will Continue Driving Source Identification ⚠️
**ASSUMPTION**: 3x/week blog cadence will consistently identify new sources for literature review
- **Verification needed**: Track blog posts over 3 months, measure new source identification rate
- **Impact if false**: Proactive source hunting required (conference monitoring, academic searches)
- **Evidence**: 1 post demonstrated 4-6× speedup, but sustained rate unproven
- **Source**: README.md line 20, CLAUDE.md lines 241-244

---

## PART 3: SCOPE & BOUNDARIES

**In Scope**:
- Living literature review published openly on Substack (primary venue) — status 2026-07-16: the Substack was retired 2026-05-24; the open venue is securitydataworks.com/writing, and the journal target is Journal of Cybersecurity per the 2026-07-10 owner ruling
- Evidence foundation for book (115,500 words) and blog (3x/week practitioner content)
- Hypothesis validation (9 assessed as of 2026-07-10, drawn from book-manuscript claims, literature-gap analysis, and post-audit peer-reviewed additions; the book-side population count lives in the book project's hypothesis tracker and is deliberately not restated here, since nothing in this repo can verify it)
- **Hybrid update model**: Monthly rolling updates + quarterly deep synthesis
- **Blog philosophy**: "Being wrong publicly" - rapid iteration, intellectual honesty, collaborative corrections
- Academic quality maintained (79%→75%+ Evidence Level A) for eventual journal submission (2026)
- Blog integration (4-6× writing speedup, source identification feedback loop)
- Expert network validation (Lisa Cao, Jake Thomas, a data-platform practitioner, Paul Agbabian)
- Community engagement (reader feedback, corrections, contributions)

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

### Decision 3: Hybrid Update Model (Monthly Rolling + Quarterly Deep Synthesis)
**Decision**: Monthly rolling updates + quarterly deep dives (not purely quarterly or purely monthly)
**Rationale**:
- **Monthly rolling updates** (~6-8 hours): New sources, corrections, community feedback - supports blog cadence (3x/week)
- **Quarterly deep synthesis** (~24 hours): Comprehensive reviews, hypothesis validation, expert interviews - maintains academic rigor
- **Total effort sustainable**: ~18 hours/month average with MCP automation (71 vendors, 84% Tier A automated)
- **Aligns with blog commitment**: Published Substack justification states "monthly refresh cycles"
- **Philosophy fit**: "Being wrong publicly" requires rapid iteration (monthly) balanced with quality (quarterly deep dives)
- **Online-first**: Substack publication venue supports rolling updates, quarterly snapshots for citation stability
**Made by**: Jeremy (Project Lead), informed by UltraThink analysis (Oct 30, 2025)
**Reversible?**: Yes (3-month trial Nov-Jan 2026, decision point Feb 2026 to continue/adjust/revert based on quality metrics)

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
- 7 hypotheses + 14 research questions have quantitative claims (2.5-3× costs, 2.7× staffing, 5.5-month timelines; the H-ARCH-01 "76% adoption" example was unsourced and refined to "industry consensus") — note 2026-07-16: those multipliers were withdrawn in the 2026-06/07 audits and now read directionally pending re-sourcing (PUBLICATION-MANUSCRIPT.md §3.7)
- Expert validation strengthens evidence (personal communication = additional source)
- Interview guides ensure systematic, reproducible questioning
- Scheduled for Q1 2026 quarterly deep dive (January 2026)
**Made by**: Jeremy (Project Lead)
**Reversible?**: Yes (interviews can be rescheduled if needed)

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

### Pending Decision 2: Academic Publication Timing ✅ RESOLVED (Deferred to Mid-2026)
**Decision**: Academic journal submission deferred to mid-2026 (online-first strategy)
**Rationale**:
- **Primary venue**: Substack (openly accessible, published Oct 22, 2025)
- **Philosophy alignment**: "Being wrong publicly" prioritizes practitioner engagement and rapid iteration over academic credibility signal
- **Community validation**: 6-12 months of monthly updates + reader feedback → Refined, validated manuscript
- **Sequencing**: Substack (Oct 2025) → Community feedback (Nov 2025 - Jun 2026) → Refined manuscript → Journal submission (mid-2026)
- **Journals**: ACM Computing Surveys, USENIX Security, IEEE S&P (submission target: Q2-Q3 2026)
- **Positioning**: Cite Substack as "preprint" demonstrating community validation and practitioner impact
**Trade-offs accepted**:
- Online-first: Broader practitioner reach, faster iteration, collaborative corrections
- Academic later: Credibility signal deferred, but manuscript quality improved through community engagement
**Decision made**: October 30, 2025 (UltraThink analysis)
**Reversible?**: Yes (if community engagement low, could submit earlier; if engagement high, defer further)

### Pending Decision 3: Evidence Level A Target with Monthly Updates ✅ RESOLVED (75%+ Acceptable)
**Decision**: Accept 75%+ Evidence Level A with monthly rolling updates (from 79% baseline)
**Rationale**:
- **Currency vs quality trade-off**: Monthly updates prioritize practitioner currency, slight quality degradation (79% → 75%) acceptable
- **MCP automation baseline**: 71 vendors, 84% Tier A quality automated → Anchors vendor landscape at high quality
- **Quarterly deep dives**: Comprehensive reviews every 3 months maintain rigor, prevent "slippery slope" degradation
- **Validation approach**: 3-month trial (Nov 2025 - Jan 2026) tracks quality monthly
- **Decision trigger**: IF quality drops <75% for 2 consecutive months → Reduce to bi-monthly or quarterly
**Trade-offs accepted**:
- Slight quality degradation (79% → 75-77% expected) for monthly currency
- Quarterly deep dives act as quality checkpoints (prevent further degradation)
**Decision made**: October 30, 2025 (UltraThink analysis)
**Blocking**: Not blocking (3-month trial validates assumption, can adjust if quality degrades)

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

**Blocker 1: IT Harvest Partnership (NOW OPTIONAL - MCP Baseline Sufficient) ✅ RESOLVED**
- **Status**: NO LONGER BLOCKING - MCP vendor database (71 vendors, 84% Tier A) provides sufficient baseline
- **Revised approach**: MCP automation covers vendor landscape needs, IT Harvest partnership becomes optional enhancement
- **Impact**: Phase 2 vendor landscape work can proceed with MCP baseline, IT Harvest partnership deferred or deprioritized
- **Future consideration**: Partnership may add value for deeper vendor insights, but not critical path for literature review updates
- **Resolution date**: October 30, 2025 (MCP integration complete, 71 vendors documented)

**Blocker 2: Automated Vendor Data Ingestion ✅ RESOLVED (MCP Integration)**
- **Status**: RESOLVED - MCP vendor database automation operational (weekly refresh, GitHub metrics)
- **Capability**: 71 vendors, 110 evidence sources, automated weekly refresh + monthly GitHub metrics
- **Burden reduction**: 75-90% reduction in manual vendor curation effort
- **Impact**: Monthly rolling updates now sustainable, automation enables hybrid model scalability
- **Resolution date**: October 23, 2025 (MCP vendor database integration, Phase 2F complete)

---

## PART 7: INTEGRATION POINTS & DEPENDENCIES

### Integration with Book Manuscript
- **Dependency**: Literature review provides evidence foundation for all 11 chapters + 5 appendices
- **Status**: ✅ Complete for Phase 1 (76+ sources cover all chapters)
- **Future**: Chapter 9 "Technology State Assessment" requires quarterly vendor landscape updates (Phase 2)
- **Repository**: https://github.com/flying-coyote/modern-data-stack-for-cybersecurity-book

### Integration with Blog (PRIMARY DRIVER)
- **Dependency**: Literature review provides evidence foundation for blog (4-6× speedup demonstrated)
- **Status**: ✅ Published online (Substack, Oct 22, 2025), 3x/week blog cadence active
- **Feedback loop**: Blog posts → Reader feedback → New sources → Literature updates → Improved blog evidence
- **Update alignment**: Monthly rolling updates support blog's need for current evidence (3x/week output)
- **Philosophy**: "Being wrong publicly" - blog and literature review share rapid iteration, collaborative corrections approach
- **Repository**: https://github.com/flying-coyote/security-data-commons-blog

### Integration with Expert Network
- **Dependency**: Expert interviews validate quantitative claims (Lisa Cao, Jake Thomas, Paul Agbabian)
- **Status**: ⏳ Interviews planned for Q1 2026 quarterly deep dive (January 2026)
- **Future**: Quarterly updates include expert validation cycle (Month 2 of each quarter)
- **Source**: second-brain expert network (1,444 thought leaders mapped, 45 actively tracked)

### Integration with IT Harvest Partnership (OPTIONAL ENHANCEMENT)
- **Dependency**: REVISED - MCP vendor database (71 vendors) provides sufficient baseline, IT Harvest optional
- **Status**: ⏳ Partnership deferred/optional (MCP automation reduces urgency)
- **MCP baseline**: 71 vendors, 84% Tier A quality, automated weekly refresh + monthly GitHub metrics
- **Future consideration**: Partnership may provide deeper vendor insights, but not critical path
- **Impact**: Minimal - MCP covers vendor landscape needs, IT Harvest would be enhancement (not requirement)

---

## PART 8: SUCCESS METRICS & VALIDATION

### Phase 1 Success Metrics (ACHIEVED ✅)
- ✅ 283 footnotes extracted from best practices document
- ✅ 76+ sources documented with standardized format
- ✅ 41.9% Evidence Level A (live-derived 2026-07-23: 96 of 229 tiered; the Phase-1 "79% — EXCEEDS 73% target" self-grade was withdrawn in the 2026-06 audit)
- ✅ 9 hypotheses assessed (7 original + 2 added post-audit 2026-07-10) with quantitative confidence scoring
- ✅ All book chapters have supporting citations
- ✅ Blog integration demonstrated (1 post, 4-6× speedup)

### Phase 2 Success Metrics (REVISED - Hybrid Model)
- ✅ MCP vendor database operational (71 vendors, 84% Tier A, automated) - COMPLETE
- ⏳ First monthly rolling update (November 2025 target)
- ⏳ 3-month trial validated (Nov 2025 - Jan 2026, quality ≥75% maintained)
- ⏳ First quarterly deep dive (Q1 2026 - January, expert interviews, hypothesis validation)
- ⏳ Versioned snapshot published (2025-Q4-v1.0 tag for citation stability)
- ⏳ Academic publication submitted (mid-2026, ACM CSUR or USENIX or IEEE S&P)

### Ongoing Quality Metrics (REVISED - Hybrid Model)
- **Baseline**: 79% Evidence Level A achieved (Phase 1 complete)
- **Monthly target**: ≥75% Evidence Level A (slight degradation acceptable for currency)
- **Quarterly target**: 77-79% Evidence Level A (deep dives restore rigor)
- **Metadata completeness**: Maintain 97%
- **Blog integration**: 4-6× writing speedup sustained (3x/week blog output)
- **Community engagement**: Track reader feedback, corrections submitted, new sources contributed
- **Time sustainability**: ≤10 hours/month for monthly updates (if >12 hours, reduce frequency)

---

## PART 9: TIMELINE & MILESTONES

### Completed Milestones ✅
- **October 15, 2025**: Phase 1-2C complete (283 footnotes, 76+ sources, 79% Level A)
- **October 15, 2025**: 9 analysis bundles created (170,100 words evidence synthesis)
- **October 16, 2025**: Blog integration demonstrated (1 post published)
- **October 16, 2025**: Expert interview guides prepared (Lisa Cao, Jake Thomas)

### Upcoming Milestones (Next 3 Months - Hybrid Model Trial)
- **November 2025**: First monthly rolling update (new sources, community feedback, MCP vendor database refresh)
- **December 2025**: Second monthly update (track time investment, quality metrics)
- **January 2026**: Third monthly update + **First quarterly deep dive** (comprehensive review, expert interviews, versioned snapshot)
- **February 2026**: Decision point - Continue monthly (if quality ≥75%), adjust to bi-monthly, or revert to quarterly

### Phase 2-3 Milestones (Next 6-12 Months)
- **Q1 2026 (January)**: First quarterly deep dive (Lisa Cao/Jake Thomas interviews, hypothesis validation, 2025-Q4-v1.0 tag)
- **Q2 2026 (April)**: Second quarterly deep dive (comprehensive review, quarterly synthesis blog post)
- **Q2-Q3 2026 (Mid-2026)**: Academic journal submission (ACM CSUR, USENIX Security, or IEEE S&P)

### Long-Term Milestones (6-18 Months - Hybrid Model Maturity)
- **Month 6 (Apr 2026)**: 6 monthly updates + 2 quarterly deep dives completed, quality metrics validated
- **Mid-2026 (Q2-Q3)**: Academic journal submission (ACM CSUR, USENIX Security, or IEEE S&P)
- **Month 12 (Oct 2026)**: 12 monthly updates + 4 quarterly deep dives completed, hybrid model proven sustainable
- **Month 18 (Apr 2027)**: Academic publication accepted (optimistic), book published with living literature review

---

## PART 10: AI CONTEXT & DOMAIN BACKGROUND

### Domain: Cybersecurity + Data Engineering Intersection

**Core Problem**: Security teams lack modern data engineering capabilities, relying on legacy SIEM platforms ($2M+/year costs, 250 GB/day scale limits, vendor lock-in)

**Modern Data Stack Solution**: Apache Iceberg (table format) + query engines (Trino, Dremio, DuckDB) + OCSF (schema standardization) enable petabyte-scale security data lakes at 10× lower cost

**Literature Gap**: Cybersecurity literature focuses on detection logic, data engineering literature ignores security requirements → This literature review bridges the gap

### Key Technologies Covered

- **Table Formats**: Apache Iceberg (industry consensus / de facto standard), Delta Lake, Apache Hudi
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
- Hypotheses drawn from book-manuscript claims, literature-review gap analysis, and post-audit peer-reviewed additions (the book-side population count lives in the book project's hypothesis tracker and is deliberately not restated here, since nothing in this repo can verify it)
- 9 hypotheses assessed so far (7 original + 2 added post-audit 2026-07-10; scored per PUBLICATION-MANUSCRIPT.md §3.7)
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

**Status**: Phase 1 complete, Phase 2 active (hybrid model - monthly rolling + quarterly deep dives)
**Next Action**: First monthly rolling update (November 2025) - 3-month trial to validate sustainability
**Priority**: HIGH - Primary driver for blog (3x/week), foundation for book, academic publication deferred to 2026
**Owner**: Jeremy Wiley (Project Lead)
**Updated**: 2026-07-16 (label-don't-decide correction sweep; prior stamp October 30, 2025 — strategic realignment: quarterly → monthly/hybrid, journal → online-first)
