# Security Data Literature Review

## Commands
```bash
/monthly-update       # Monthly rolling update checklist
/add-source          # Add source with evidence classification
/quarterly-deep-dive # Quarterly deep dive workflow
```

## Current Status
**Phase**: 2 (Monthly Updates + Quarterly Deep Dives) | **Version**: 1.23.0 (+ [Unreleased])
**Counts**: run `python3 scripts/automation_dashboard.py` — this file no longer states them (they drifted twice while hand-maintained here; the derive-don't-state gotcha below applies to this file too). Snapshot 2026-11-07 (late): 252 blocks / 250 tiered / 19.2% Level A (48/250), after the nine handbook-footnote companions (Reis, six [un]prompted talks, Humio, Marwick & boyd); earlier the same day 243 / 241 / 19.5% after two A→B re-tiers and nine verified snowball admissions (earlier snapshot 2026-11-05: 231 / 229 / 17.0%). The 41.9% of 2026-07-16 fell to 17.0% when the 2026-08-19 audit moved 57 entries down; the upward re-audit found nothing under-tiered, so 17.0% is the measurement and the Level-A target is retired (c1f5d66).
**Hypotheses**: 9 assessed under the 2026-07-13 rubric rescore (1 strong / 2 high / 2 moderate / 4 preliminary, per `count_reconcile.py` Counter 1). The "N validated" vocabulary is retired pending the owner's canonical-status ruling.
See `PROJECT-BRIEF.md` for scope; live metrics are README.md's Quality Metrics block (live-computed via `scripts/automation_dashboard.py`). REPOSITORY-STATUS.md was archived 2026-07-10 → `archive/` (it was a fourth hand-synced copy of the same numbers).
> The 80% Level-A figure was self-reported; the honest live number was ~42% after the 2026-06-05 audit and is 17.0% after the 2026-08-19 audit
> folded corrections in and re-tiered ~25 entries off A (their headline stats weren't in the cited
> source). The freshness sweep + 2026 production sources are the path back toward the 75% target — the
> gap is now visible, not masked.

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

Portfolio-review program (2026-07): see `.claude/review-protocol.md` before any review-program session.
