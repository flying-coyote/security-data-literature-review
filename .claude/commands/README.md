# Custom Slash Commands

**Project**: security-data-literature-review
**Last Updated**: 2026-01-02

This directory contains custom slash commands for the literature review workflow.

---

## Available Commands

### `/monthly-update`
**Purpose**: Execute monthly rolling update checklist
**When to Use**: During monthly literature review updates (6-8 hours/month)
**Workflow**:
1. Pre-update assessment (health check, dashboard, external inputs)
2. Add 2-5 new sources with evidence tier classification
3. Refresh 3-5 outdated sources
4. Fix broken links
5. Post-update verification and documentation

### `/add-source`
**Purpose**: Add new source to bibliography with evidence classification
**When to Use**: When adding any new research source
**Workflow**:
1. Capture source metadata (title, authors, venue, URL)
2. Apply Evidence Tier classification (Tier 1-5)
3. Add to MASTER-BIBLIOGRAPHY.md with standardized format
4. Link to relevant hypotheses (H-XX references)
5. Verify distribution maintains 75%+ Level A

### `/validate-evidence`
**Purpose**: Validate evidence quality across bibliography
**When to Use**: During monthly updates or when quality concerns arise
**Workflow**:
1. Run automation dashboard for quick assessment
2. Check evidence distribution by tier
3. Verify hypothesis coverage with Tier 1-2 sources
4. Assess source freshness
5. Generate validation report

### `/quarterly-deep-dive`
**Purpose**: Execute quarterly deep dive workflow
**When to Use**: January, April, July, October (quarterly cycles)
**Workflow**:
1. Expert interview preparation and execution
2. Comprehensive hypothesis validation review
3. Evidence synthesis across all research questions
4. Create versioned git tag for citation stability
5. Publish quarterly synthesis blog post

---

## Usage

Invoke commands by typing `/<command-name>` in a Claude Code session:

```
/monthly-update
/add-source
/validate-evidence
/quarterly-deep-dive
```

Each command provides a structured checklist to ensure consistent, high-quality research workflow execution.

---

## Quality Targets

| Metric | Target |
|--------|--------|
| Evidence Level A | >= 75% |
| Monthly time investment | <= 10 hours |
| Quarterly deep dive | ~24 hours |
| Source freshness | < 18 months |

---

**Created**: 2026-01-02 (Best Practices Audit)
