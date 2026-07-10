# Security Data Literature Review

## Commands
```bash
/monthly-update       # Monthly rolling update checklist
/add-source          # Add source with evidence classification
/quarterly-deep-dive # Quarterly deep dive workflow
```

## Current Status
**Phase**: 2 (Monthly Updates + Quarterly Deep Dives) | **Version**: 1.22.0
**Sources**: 176 (`#### ` blocks; 175 tiered + 1 rejection stub) | **Evidence Level A**: 42.3% (live 2026-07-09, 74/175) | **Hypotheses Validated**: 7 (needs review — see note)
See `PROJECT-BRIEF.md` for scope and `REPOSITORY-STATUS.md` for tracking.
> Counts are live-computed by `scripts/automation_dashboard.py`: sources = `#### ` blocks (176), Level-A% = A-tier over tiered entries (74/175 = 42.3%; the 1 untiered block is a documented rejection stub).
> The 80% Level-A figure was self-reported; the honest live number is 42.3% (74/175) after the 2026-06-05 audit
> folded corrections in and re-tiered ~25 entries off A (their headline stats weren't in the cited
> source). The freshness sweep + 2026 production sources are the path back toward the 75% target — the
> gap is now visible, not masked. The validated-hypothesis count is unreconciled across docs (7 here,
> "3 strongly validated/6 proposed" in the Oct-2025 gap analysis) and needs a real review.

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
