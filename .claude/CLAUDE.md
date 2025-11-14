# Security Data Literature Review - Project Context

## Project Purpose
Living literature review published openly on Substack, supporting blog (3x/week practitioner content) and book (115,500 words). Bridges cybersecurity and data engineering domains with rigorous, evidence-based research and "being wrong publicly" philosophy. **Hybrid update model**: Monthly rolling updates (new sources, community feedback) + quarterly deep synthesis (comprehensive reviews, expert validation). Online-first strategy prioritizes practitioner engagement, academic journal submission deferred to mid-2026.

## Key Documentation Files

### PROJECT-BRIEF.md
**Purpose**: Complete project context using Memory Prompts Prompt 3 format - confirmed facts vs. assumptions, scope, constraints, risks
**Update Trigger**: Phase transitions, major milestones (IT Harvest partnership, quarterly updates), expert interview results
**Lifecycle**: PROJECT-SCOPED (12+ months active, quarterly updates planned)
**Note**: Separates canonical facts from assumptions requiring verification - critical for AI context

### MASTER-BIBLIOGRAPHY.md
**Purpose**: Complete bibliography with 75+ sources, evidence levels (A/B/C/D), hypothesis validation
**Update Trigger**: New sources added, hypothesis validation updates, evidence level adjustments

### LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md
**Purpose**: Gap analysis identifying new hypotheses from literature review
**Update Trigger**: New hypotheses identified, gap analysis updates

### LITERATURE-EXTRACTION-PLAN.md
**Purpose**: Systematic extraction methodology (PRISMA-aligned)
**Update Trigger**: Methodology refinements, extraction process updates

### PUBLICATION-VENUE-RECOMMENDATIONS.md
**Purpose**: Academic publication strategy for literature review
**Update Trigger**: New venue opportunities, submission planning

### CHANGELOG.md
**Purpose**: Track all revisions for academic citation stability
**Update Trigger**: Every update to content - maintains version history for citations

### REPOSITORY-STATUS.md
**Purpose**: Current status, phase tracking, completion metrics
**Update Trigger**: Phase transitions, major milestones

## Current Phase
**Status**: Phase 1 (Literature Extraction) COMPLETE ✅ | Phase 2 (Monthly Updates) ACTIVE 🔄
**Last Updated**: November 14, 2025
**Focus**: Monthly rolling updates + quarterly deep synthesis (committed to ongoing monthly cadence)
**Published**: Substack (Oct 22, 2025), 38,000 words, 75+ sources, 79% Evidence Level A

**Phase 1 Accomplishments** ✅:
- 283 footnotes extracted from best practices document
- 75+ sources documented with standardized format
- 79% Evidence Level A (production/academic sources)
- 7 hypotheses validated with quantitative evidence
- 16 of 22 URLs validated (73% overall, 100% hypothesis-critical)
- All book chapters have supporting source citations

**Phase 2 Active** 🔄:
- **Hybrid update model**: Monthly rolling updates (~6-8 hours) + quarterly deep synthesis (~24 hours/quarter)
- **MCP vendor database**: 71 vendors, 84% Tier A, automated weekly refresh (replaces IT Harvest dependency)
- **Committed to monthly updates**: Tracking quality and time for continuous improvement
- **Quarterly deep dives**: Comprehensive reviews, expert interviews (Lisa Chao, Jake Thomas), versioned snapshots
- **Community engagement**: Reader feedback, corrections, collaborative source identification

## Quality Standards

### Blog Philosophy: "Being Wrong Publicly"
This project embodies the blog's core philosophy from [Security Data Commons](https://securitydatacommons.substack.com):

**Intellectual Honesty**:
- Transparent documentation of contradictions, limitations, unresolved questions
- Acknowledge uncertainty explicitly ("may" not "definitely", confidence levels 1/5 to 5/5)
- Invite corrections and community contributions
- "We need to try things, share results, fail publicly, learn collectively"

**Rapid Iteration**:
- Monthly rolling updates prioritize currency over perfection
- Quarterly deep dives maintain rigor without blocking progress
- Evidence evolves as new sources emerge, updates visible via git history

**Collaborative Learning**:
- Reader feedback drives source identification
- Community corrections improve evidence quality
- Practitioner engagement valued over academic gatekeeping

**Pragmatic Specificity**:
- Name vendors, costs, deployment details (not abstract generalities)
- Production deployments > marketing claims
- Quantitative evidence with confidence intervals

### From Second Brain Project
This project inherits evidence quality standards from [second-brain](https://github.com/flying-coyote/second-brain):

**Evidence-Based Reasoning**:
- All sources categorized by evidence level (A/B/C/D)
- Level A: Production deployments, peer-reviewed research
- Level B: Industry analyst reports, vendor documentation
- Level C: Blog posts, conference talks
- Level D: Marketing materials, unverified claims
- Quantify uncertainty explicitly in hypothesis validation
- Document contradictions when found

**Professional Objectivity**:
- Academic quality suitable for peer review
- Balanced perspective with trade-offs
- No vendor bias in analysis
- Cite sources for all claims
- Acknowledge limitations and gaps

**Systematic Documentation**:
- PRISMA-aligned extraction methodology
- Standardized source format
- Version control for citation stability
- CHANGELOG tracks all revisions
- Clear success criteria for each phase

**UltraThink Methodology**:
- Use FRAME-ANALYZE-SYNTHESIZE for complex analysis
- Hypothesis-driven research approach
- Expert validation for critical claims
- Gap analysis to identify new research directions

### Literature Review-Specific Standards

**Source Quality**:
- 79%+ Evidence Level A maintained
- Government/standards sources prioritized (CISA, MITRE, DARPA, NSA, SANS)
- Industry analysts included (Gartner, IDC, Forrester)
- Production deployments documented (Netflix, Uber, LinkedIn, etc.)
- Academic research cited when available

**Citation Stability**:
- Quarterly updates create versioned snapshots (YYYY-QX-update.md)
- CHANGELOG.md documents all changes
- Never edit published versions (create new versions instead)
- Academic citation format maintained

**Hypothesis Validation**:
- Quantitative evidence required for validation
- Multiple sources preferred (3+ sources = strong validation)
- Confidence levels explicitly stated
- Contradictions documented and analyzed

## Claude Skills

### Project-Specific Skills (1 skill)
This project has 1 specialized Claude Skill that activates automatically during literature review work:

**evidence-tier-classifier**:
- **Activates**: When adding sources, citing papers, updating bibliography, or validating evidence quality
- **Classifies**: Tier 1-5 evidence classification with detailed rationale (Tier 1=Production, Tier 2=Peer-reviewed, Tier 3=Expert consensus, Tier 4=Vendor claims, Tier 5=Speculation)
- **Validates**: Maintains 79% Evidence Level A (Tier 1-2) quality standard, tracks distribution, links evidence to hypotheses
- **Purpose**: Systematic quality management for 75+ sources, ensures academic rigor
- **Location**: `.claude/skills/evidence-tier-classifier/SKILL.md`

### Personal Skills (6 universal skills)
All personal skills from `~/.claude/skills/` are available:
- **academic-citation-manager**: General citation management and bibliography formatting
- **voice-consistency-enforcer**: Maintains intellectual honesty and balanced academic perspective
- **ultrathink-analyst**: FRAME-ANALYZE-SYNTHESIZE for deep research methodology analysis
- **git-workflow-helper**: Version control for literature updates and CHANGELOG tracking
- **systematic-debugger**: Debug bibliography generation scripts
- **tdd-enforcer**: Test extraction automation scripts

### Workflow Integration

**Research Source Addition Workflow**:
1. User finds research source
2. **evidence-tier-classifier** classifies Tier 1-5 with rationale
3. **academic-citation-manager** (personal) adds to bibliography with proper formatting
4. **research-synthesis-extractor** (project1) extracts concepts
5. **hypothesis-validator** (project1) links to hypotheses
6. **git-workflow-helper** commits updates to CHANGELOG.md

**Hypothesis Validation Workflow**:
1. Identify hypothesis to validate
2. **evidence-tier-classifier** assesses evidence quality across sources
3. **academic-citation-manager** ensures proper citation format
4. **voice-consistency-enforcer** validates balanced assessment (acknowledges limitations)
5. Update MASTER-BIBLIOGRAPHY.md with validation status

**Quarterly Update Workflow** (Phase 2):
1. IT Harvest data refresh + platform updates
2. **evidence-tier-classifier** classifies new sources
3. **ultrathink-analyst** synthesizes trends and insights
4. **voice-consistency-enforcer** ensures academic objectivity
5. Create YYYY-QX-update.md versioned snapshot
6. **git-workflow-helper** updates CHANGELOG.md

**Documentation**: See `.claude/skills/README.md` for complete skill descriptions and workflow patterns.

## Git Workflow

### Commit Message Conventions
```
📋 Documentation updates and source additions
✅ Phase milestones and validation completions
📊 Research additions and hypothesis updates
🔧 Fixes and corrections
📚 Bibliography updates
🔍 Source validation and evidence level adjustments
```

### Commit Message Format
```
[emoji] Brief description (50 chars max)

- Detailed bullet points if needed
- List sources added/updated
- Note evidence levels
- Reference hypotheses validated

Co-Authored-By: Claude <noreply@anthropic.com>  # If AI-assisted
```

## Research Findings Summary

### Validated Hypotheses (7 total)
1. **H-ARCH-01 (Iceberg Dominance)**: STRONGLY VALIDATED - 76% adoption, 5 sources
2. **H-IMPL-01 (TCO Reality)**: STRONG - 2.5-3× operational costs, 5 sources
3. **H-IMPL-02 (Staffing Scarcity)**: STRONG - 2.7× staff required, 4 sources
4. **H-IMPL-03 (Timeline Premium)**: VALIDATED - 5.5 months average, 3 sources
5. **H-COST-09 (Tiered Storage)**: STRONG - 55-80% cost savings, 3 sources
6. **H3-PERFORMANCE-01 (ClickHouse)**: VALIDATED - 6M req/sec, 96% <1s queries
7. **H-STREAM-01 (Kafka Streams)**: VALIDATED - Production security patterns, 3 sources

### Quality Metrics
- **Evidence Level A**: 73% (production deployments, peer-reviewed research)
- **Government/Standards Sources**: 8 (CISA, MITRE, DARPA, NSA, SANS)
- **Industry Analysts**: 10 (Gartner, IDC, Forrester)
- **Production Deployments**: 18 (Netflix, Uber, LinkedIn, Cloudflare, Shell, SK Telecom, etc.)

## Future Structure (Phase 2 - Planned)

### platforms/ (Quarterly updates)
- `query-engines.md`: Trino/Starburst, Dremio, Denodo, Athena
- `olap-analytics.md`: ClickHouse, StarRocks/Celerdata, Druid
- `hybrid-architectures.md`: Spark + Query Engine patterns

### infrastructure/ (Quarterly updates)
- `table-formats.md`: Iceberg, Delta, Hudi trend analysis
- `catalogs.md`: Gravitino, Polaris, Unity, Nessie
- `object-storage.md`: S3, MinIO, Azure Blob

### security-specific/ (Quarterly updates)
- `ocsf-adoption.md`: Quarterly tracking
- `detection-platforms.md`: Security analytics evolution
- `threat-intel-integration.md`: TI platform updates

### vendor-landscape/ (IT Harvest powered)
- `capability-matrix.md`: Platform capabilities by category
- `market-trends.md`: Quarterly trend analysis
- `quarterly-updates/`: YYYY-QX-update.md versioned files

## Quarterly Update Process (Phase 2 - Planned)

**Quarterly Cycle** (Jan, Apr, Jul, Oct):
1. **Month 1**: IT Harvest data refresh + platform updates
2. **Month 2**: Expert validation + blog synthesis
3. **Month 3**: Publication + citation updates

**Version Control**:
- Each update creates new `YYYY-QX-update.md`
- CHANGELOG.md tracks all revisions
- Enables academic citation of specific versions

**Sources**:
1. IT Harvest vendor data (primary - partnership pending)
2. Blog post insights (ongoing from security-data-commons-blog)
3. Expert network validation (Lisa Chao, Jake Thomas, Paul Agbabian, etc.)
4. a data-platform practitioner + practitioner feedback

## Integration Points

### Blog (PRIMARY DRIVER)
- **Literature review published online**: Substack (Oct 22, 2025), 38,000 words, openly accessible
- **Evidence foundation for blog**: 4-6× writing speedup demonstrated for 3x/week practitioner content
- **Feedback loop**: Blog posts → Reader feedback → New sources → Literature updates → Improved blog evidence
- **Philosophy alignment**: "Being wrong publicly" - rapid iteration, intellectual honesty, collaborative corrections
- **Update alignment**: Monthly rolling updates support blog's need for current evidence
- **Repository**: https://github.com/flying-coyote/security-data-commons-blog

### Book Manuscript
- All chapters have supporting citations in MASTER-BIBLIOGRAPHY.md
- Literature review provides evidence foundation for 115,500-word manuscript
- Quarterly deep dives feed book revisions and new chapter content
- Repository: https://github.com/flying-coyote/modern-data-stack-for-cybersecurity-book

### MCP Vendor Database (AUTOMATION FOUNDATION)
- **71 vendors**: 84% Tier A quality, 110 evidence sources
- **Automated maintenance**: Weekly refresh + monthly GitHub metrics (75-90% burden reduction)
- **Replaces IT Harvest dependency**: Sufficient baseline for vendor landscape, partnership now optional
- **Enables hybrid model**: Automation makes monthly updates sustainable for solo practitioner

### IT Harvest Partnership (OPTIONAL ENHANCEMENT)
- **Status**: Deferred/optional - MCP vendor database provides sufficient baseline
- **Future consideration**: Partnership may add deeper vendor insights, but not critical path
- **Charles Wells collaboration**: Can revisit if MCP baseline proves insufficient

### Expert Network
- Validation interviews referenced throughout
- Expert feedback incorporated into hypothesis validation
- Source: second-brain expert network (1,444 thought leaders mapped)

## Related Projects

### Core Projects
- **[second-brain](https://github.com/flying-coyote/second-brain)**: Source of quality standards and methodology
- **[modern-data-stack-for-cybersecurity-book](https://github.com/flying-coyote/modern-data-stack-for-cybersecurity-book)**: 115,500-word manuscript this literature review supports
- **[security-data-commons-blog](https://github.com/flying-coyote/security-data-commons)**: Blog providing ongoing source identification and validation

### Integration Strategy
- **Book**: Literature review provides evidence foundation and citations
- **Blog**: Identifies new sources, validates claims through practitioner engagement
- **Living Review**: Quarterly updates keep research current for book revisions and blog content

## Success Metrics

### Phase 1 (COMPLETE) ✅
- [x] 283 footnotes extracted
- [x] 75+ sources documented
- [x] 79% Evidence Level A (exceeded 73% target)
- [x] 7 hypotheses validated with quantitative evidence
- [x] 16/22 URLs validated (100% hypothesis-critical)
- [x] All book chapters cited
- [x] Published online (Substack, Oct 22, 2025) - 38,000 words, openly accessible

### Phase 2 (ACTIVE - Monthly Updates Ongoing) 🔄
- [x] MCP vendor database operational (71 vendors, 84% Tier A, automated) - COMPLETE
- [ ] Monthly rolling updates ongoing (November 2025+)
- [ ] First quarterly deep dive (Q1 2026 - January, expert interviews, versioned snapshot)
- [ ] Blog support sustained (3x/week practitioner content with current evidence)

### Hybrid Model Metrics (Phase 2-3 - Ongoing)
- **Monthly rolling updates**: 12x per year (new sources, corrections, community feedback)
- **Quarterly deep dives**: 4x per year (comprehensive reviews, expert validation, versioned snapshots)
- **Quality baseline**: ~75-78% Evidence Level A (track for continuous improvement)
- **Time tracking**: Monitor for awareness, typical range 6-10 hours/month
- **Blog integration**: 4-6× writing speedup sustained, 3x/week blog output
- **Community engagement**: Track reader feedback, corrections, source contributions
- **Citation stability**: Quarterly git tags (YYYY-QX-v1.0) for academic citations

## Current Priorities

### Immediate (Phase 2 - Monthly Updates Ongoing: Nov 2025+)
1. **Monthly rolling updates**: New sources, community feedback, MCP vendor database refresh
2. **Track quality metrics**: Evidence Level A percentage, time investment for continuous improvement
3. **Sustain blog output**: 3x/week practitioner content supported by current evidence base
4. **Community engagement**: Respond to reader feedback, incorporate corrections, document source contributions

### Short-term (Phase 2 - First Quarterly Deep Dive: January 2026)
1. **Execute expert interviews** (Lisa Chao, Jake Thomas - deferred to Q1 2026 quarterly deep dive)
2. **Comprehensive review** of Oct-Dec 2025 monthly updates (hypothesis validation, evidence synthesis)
3. **Versioned snapshot**: Tag repository with 2025-Q4-v1.0 for citation stability
4. **Quarterly synthesis blog post**: Publish comprehensive findings from Q4 2025 review

### Long-term (Phase 3 - Hybrid Model Maturity: 2026+)
1. **Sustain hybrid model**: 12 monthly updates + 4 quarterly deep dives per year
2. **Academic journal submission** (mid-2026): ACM CSUR, USENIX Security, or IEEE S&P after community validation
3. **Blog-literature feedback loop**: Reader contributions, corrections, collaborative source identification
4. **Version control and citation stability**: Quarterly git tags (2026-Q1-v1.0, 2026-Q2-v1.0, etc.)
5. **IT Harvest partnership (optional)**: Evaluate if MCP baseline sufficient or partnership adds value

## Next Session Priorities

When resuming work on this project, focus on:

1. **Monthly Rolling Updates** - New sources, community feedback, MCP vendor refresh
2. **Track Metrics** - Evidence Level A percentage, time investment for awareness
3. **Community Engagement** - Respond to Substack reader feedback, incorporate corrections
4. **Blog Support** - Sustain 3x/week output with current evidence (4-6× speedup demonstrated)
5. **Prepare for Q1 Deep Dive** (January 2026) - Expert interviews, hypothesis validation, versioned snapshot

---

**Usage**: This file is loaded in every Claude Code conversation to provide consistent project context. Update when phase transitions occur or major research findings are added.

**Last Updated**: October 30, 2025 (Strategic realignment: Hybrid update model adopted, online-first publication strategy, IT Harvest partnership optional, Version 1.9.0)
