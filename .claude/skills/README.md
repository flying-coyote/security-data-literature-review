# Security Data Literature Review - Claude Skills

**Project**: Living Literature Review for "Modern Data Stack for Cybersecurity"
**Status**: Phase 1-2C Complete (76+ sources, 79% Tier 1-2)
**Skills**: 1 project-specific + 6 personal skills
**Last Updated**: 2025-10-17

---

## Project-Specific Skills

### 1. evidence-tier-classifier
**Purpose**: Maintain 79% Evidence Level A (Tier 1-2) academic quality
**Triggers**: "source", "paper", "add citation", "evidence quality"
**Features**:
- Tier 1-5 classification with detailed rationale
- Evidence Level A-D mapping
- Distribution tracking (current: 79% Tier 1-2 ✅ exceeds 70% target)
- Hypothesis-evidence linking
- Publication readiness assessment

**Value**: Systematic quality management for 76+ sources
**Status**: ✅ Active

---

## Personal Skills Used

From `~/.claude/skills/` (shared across all projects):

1. **academic-citation-manager**: General citation management and bibliography
2. **git-workflow-helper**: Version control for literature updates
3. **ultrathink-analyst**: Deep analysis of research methodologies
4. **systematic-debugger**: Debug bibliography generation scripts
5. **tdd-enforcer**: Test extraction automation
6. **voice-consistency-enforcer**: Maintains intellectual honesty, pragmatic specificity, conversational authority

**⚠️ Note**: Personal skills live in `~/.claude/skills/` (user home directory) and are **NOT included in this repository**. These are user-specific preferences that work across all projects. If you clone this repository, you can use your own personal skills or create these skills based on the [Anthropic Skills documentation](https://docs.claude.com/en/docs/claude-code/skills).

---

## Evidence Tier System

```
Tier 1: Production deployments (measured outcomes) → Evidence Level A
Tier 2: Peer-reviewed research (reproducible) → Evidence Level A
Tier 3: Expert consensus (documented reasoning) → Evidence Level B
Tier 4: Vendor claims (note bias) → Evidence Level C
Tier 5: Speculation (don't use) → Evidence Level D

Target: 70%+ Evidence Level A (Tier 1+2)
Current: 79% ✅
```

---

## Research Workflow

```
1. User finds research source
2. evidence-tier-classifier → Classify Tier 1-5
3. academic-citation-manager (personal) → Add to bibliography
4. research-synthesis-extractor (project1) → Extract concepts
5. hypothesis-validator (project1) → Link to hypotheses
6. git-workflow-helper → Commit updates
```

---

## Integration with Project1 & Book

**Shares evidence standards**:
- Project1: Same Tier 1-5 classification system
- Book: Uses Tier 1-2 sources for publication quality
- Blog: Cites Tier 1-3 sources appropriately

**Literature Review-specific**:
- PRISMA-aligned systematic methodology
- 100+ source target (comprehensive review)
- Quarterly update cycles
- Academic publication preparation (ACM CSUR target)

---

## Current Status

**Sources**: 76+ documented
**Quality**: 79% Evidence Level A (Tier 1+2) ✅
**Distribution**:
- Tier 1 (Production): [documented in MASTER-BIBLIOGRAPHY.md]
- Tier 2 (Peer-reviewed): 42 sources
- Tier 3 (Expert consensus): [documented]

**Analysis Bundles**: 9 completed (170,100 words)
**Expert Interviews**: Week 3 scheduled (Lisa Chao, Jake Thomas)
**Target**: 100+ sources, maintain 70%+ Tier 1-2

---

**Implementation**: 2025-10-17
**Version**: 1.0
