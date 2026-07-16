# Security Data Literature Review - Claude Skills

**Project**: Living Literature Review for "Modern Data Stack for Cybersecurity"
**Status**: Phase 2 Active (live counts: `scripts/automation_dashboard.py` — the header's old 101/78% figures were the Jan-2026 snapshot)
**Skills**: 1 project-specific + 6 personal skills
**Last Updated**: 2026-07-16

---

## Project-Specific Skills

### 1. evidence-tier-classifier
**Purpose**: Evidence Level A (Tier 1-2) quality tracking against the 75% target (live share via `scripts/automation_dashboard.py`)
**Triggers**: "source", "paper", "add citation", "evidence quality"
**Features**:
- Tier 1-5 classification with detailed rationale
- Evidence Level A-D mapping
- Distribution tracking (live share derived by `scripts/automation_dashboard.py` — the old "79% ✅" self-grade was withdrawn in the 2026-06 audit; below the 75% target as of 2026-07-16)
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
Current: derive via scripts/automation_dashboard.py (41.9% on 2026-07-16 — below target; the old 79% self-grade was withdrawn 2026-06)
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

**Sources**: derive via `scripts/automation_dashboard.py` (229 blocks / 227 tiered on 2026-07-16)
**Quality**: 41.9% Evidence Level A on 2026-07-16 — below the 75% target (the old 78-79% self-grades were withdrawn in the 2026-06 audit)
**Distribution**:
- Tier 1 (Production): 21+ case studies documented
- Tier 2 (Peer-reviewed): 45+ sources
- Tier 3 (Expert consensus): 18+ sources

**Research Questions**: 14 total (RQ1-RQ14)
**Expert Interviews**: Q1 2026 Deep Dive (Lisa Cao, Jake Thomas)
**Target**: Maintain 75%+ Tier 1-2, quarterly deep dives

---

**Implementation**: 2025-10-17
**Version**: 1.1 (Updated 2026-01-02)
