# Security Data Literature Review

## Commands
```bash
/monthly-update       # Monthly rolling update checklist
/add-source          # Add source with evidence classification
/quarterly-deep-dive # Quarterly deep dive workflow
```

## Current Status
**Phase**: 2 (Monthly Updates + Quarterly Deep Dives) | **Version**: 1.22.0
**Sources**: 195 (`#### ` blocks; 193 tiered + 2 stubs) | **Evidence Level A**: 43.0% (live 2026-07-10, 83/193) | **Hypotheses Validated**: 7 (needs review — see note)
See `PROJECT-BRIEF.md` for scope; live metrics are README.md's Quality Metrics block (live-computed via `scripts/automation_dashboard.py`). REPOSITORY-STATUS.md was archived 2026-07-10 → `archive/` (it was a fourth hand-synced copy of the same numbers).
> Counts are live-computed by `scripts/automation_dashboard.py`: sources = `#### ` blocks (195), Level-A% = A-tier over tiered entries (83/193 = 43.0%; the 2 untiered blocks are documented rejection/retirement stubs).
> The 80% Level-A figure was self-reported; the honest live number is 43.0% (83/193) after the 2026-06-05 audit and the 2026-07-10 DR-3 Tier-A adds
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
- Don't hand-maintain counts in prose — `scripts/automation_dashboard.py` is authoritative (derive, don't state)
- Vendor-channel tier rule (owner-adjudicated 2026-07-10): first-person practitioner AUTHORSHIP on a vendor channel = Tier B with a curation caveat; vendor-AUTHORED piece QUOTING a practitioner = Tier C. Authorship is the line, not who appears.
- No blanket "100% verified" certificates — the 2025-10-22 certificate certified later-confirmed fabrications; verification claims stay per-item with the primary named

## Hybrid Update Model
- **Monthly** (6-8 hrs): New sources, community feedback, MCP refresh
- **Quarterly** (24 hrs): Expert interviews, comprehensive review, versioned snapshot

## Key Files
```
MASTER-BIBLIOGRAPHY.md              # 118+ sources with evidence tiers
LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md  # Hypotheses and validation
CHANGELOG.md                        # All revisions (citation stability)
monthly-update-tracker.md           # Rolling monthly cadence (Q1 plan archived 2026-07-10)
```

## Integration
- **Blog**: RETIRED 2026-05-24 (Substack archived read-only; essays live at securitydataworks.com/writing)
- **Book**: Citations for the MOAR manuscript (word count lives in the book repo's own build — derive, don't state)
- **MCP Server**: repo ARCHIVED 2026-07-01; the vendor DB lives in vendor-landscape/ here, quarterly cadence (no automated weekly refresh exists)
