# Security Data Literature Review

## Commands
```bash
/monthly-update       # Monthly rolling update checklist
/add-source          # Add source with evidence classification
/quarterly-deep-dive # Quarterly deep dive workflow
```

## Current Status
**Phase**: 2 (Monthly Updates + Quarterly Deep Dives) | **Version**: 1.21.0
**Sources**: 118 | **Evidence Level A**: 80% | **Hypotheses Validated**: 7
See `PROJECT-BRIEF.md` for scope and `REPOSITORY-STATUS.md` for tracking.

## Evidence Tiers
| Tier | Type | Target |
|------|------|--------|
| A (1-2) | Production deployments, peer-reviewed | 78%+ |
| B (3) | Expert consensus, analyst reports | OK |
| C (4) | Vendor claims, blog posts | Cite bias |
| D (5) | Speculation, unverified | Avoid |

## Git Workflow
- 📋 Documentation updates
- ✅ Phase milestones
- 📊 Research additions
- 📚 Bibliography updates
- 🔧 Fixes

## Key Gotchas
- Update CHANGELOG.md for all content changes (citation stability)
- Never edit published versions - create new versioned snapshots
- Quarterly tags (YYYY-QX-v1.0) enable academic citation
- "Being wrong publicly" - document contradictions, invite corrections
- Link new sources to hypotheses in MASTER-BIBLIOGRAPHY.md

## Hybrid Update Model
- **Monthly** (6-8 hrs): New sources, community feedback, MCP refresh
- **Quarterly** (24 hrs): Expert interviews, comprehensive review, versioned snapshot

## Key Files
```
MASTER-BIBLIOGRAPHY.md              # 118+ sources with evidence tiers
LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md  # Hypotheses and validation
CHANGELOG.md                        # All revisions (citation stability)
PROJECT-PLAN-2026-Q1.md            # Current quarter plan
```

## Integration
- **Blog**: Evidence foundation for 3x/week content
- **Book**: Citations for 115,500-word manuscript
- **MCP Server**: 71 vendors, automated weekly refresh
