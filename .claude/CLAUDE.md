# Security Data Literature Review

## Commands
```bash
/monthly-update       # Monthly rolling update checklist
/add-source           # Add source with evidence classification
/validate-evidence    # Tier distribution and hypothesis-coverage check
/quarterly-deep-dive  # Quarterly deep dive workflow
```

## Current status
**Phase**: 2 (monthly updates + quarterly deep dives) | **Version**: 1.23.0 + [Unreleased] (see CHANGELOG.md)
**Counts**: this file states none, because hand-copied counts here drifted twice. Run `python3 scripts/count_reconcile.py` (bibliography blocks, tiered entries, A/B/C split and the assessed-hypothesis count, gated on every surface that states them) or `python3 scripts/automation_dashboard.py` (dashboard view).
**Hypotheses**: scored under the 2026-07-13 rubric rescore (`methods/RESCORE-2026-07-13.md`, instrument `methods/scoring-rubric.md`); the canonical list and scores are PUBLICATION-MANUSCRIPT.md §3.7. The "N validated" vocabulary is retired pending the owner's canonical-status ruling.
**Level-A share**: a description, not a target. The 70-80% targets were retired by owner ruling 2026-08-19 (METHODOLOGY §8.1a), because the share falls as honest practitioner evidence is added and a floor on it rewards over-tiering.

## Evidence tiers (METHODOLOGY §3.1 is canonical)
| Level | What qualifies | How it is used |
|-------|----------------|----------------|
| A | Peer-reviewed research at a named venue; standards-body documents (NIST, ISO/IEC, IETF RFC, W3C, OASIS); the formal specification of an open standard (the Iceberg table spec, the OCSF schema spec); normative frameworks from a neutral body (MITRE D3FEND, MITRE ATLAS), authoritative on structure and silent on efficacy | Primary evidence |
| B | Practitioner and production evidence: deployments and case studies with real numbers, vendor engineering blogs, conference talks, trade books, analyst reports, expert interviews, government advisories, official project documentation, and arXiv preprints with no venue | Real evidence, not independently reviewed |
| C | Vendor blog posts, product documentation and talks with no production measurement behind them | Catalogued with bias flagged; never carries a hypothesis on its own |
| D | Marketing, unverified claims, speculation | Excluded |

Vendor-channel rule (owner-adjudicated 2026-07-10): first-person practitioner authorship on a vendor channel is Level B with a curation caveat; a vendor-authored piece quoting a practitioner is Level C. Authorship is the line, not who appears.

## Git workflow
- 📋 Documentation updates
- ✅ Phase milestones
- 📊 Research additions
- 📚 Bibliography updates
- 🔧 Fixes

## Key gotchas
- Update CHANGELOG.md for all content changes (citation stability)
- Never edit `published/`; create a new versioned snapshot instead
- Quarterly tags (`YYYY-QX-v1.0`) enable academic citation
- "Being wrong publicly": document contradictions, invite corrections
- Link new sources to hypotheses in MASTER-BIBLIOGRAPHY.md, and add a dated taxonomy record under `methods/` (`scripts/derive_source_taxonomy.py --check`)
- Don't hand-maintain counts in prose; `scripts/count_reconcile.py` derives them and gates every surface in its ALLOWLIST (derive, don't state)
- No blanket "100% verified" certificates: the 2025-10-22 certificate certified later-confirmed fabrications, so verification claims stay per-item with the primary named
- Moving a file means adding it to `working/MOVE-MAP.json` and running `python3 scripts/repoint_moved_paths.py --apply`, then `--check`

## Update cadence
- **Weekly** (automated check, `scripts/weekly_scheduled_check.py`, see `scripts/SCHEDULING.md`): health check and notify; escalates to a refresh when red or in the first week of a month
- **Monthly** (supervised `/monthly-update`): new sources, reader corrections, link repair
- **Quarterly** (about 24 hours, `/quarterly-deep-dive`): comprehensive hypothesis review, vendor-landscape regeneration, versioned snapshot

## Key files
```
README.md                    # reader entry point; gated count lines (count_reconcile.py ALLOWLIST)
PUBLICATION-MANUSCRIPT.md    # the paper; §3.7 is the canonical hypothesis list and scores
MASTER-BIBLIOGRAPHY.md       # every catalogued source with its Evidence Level and validation status
METHODOLOGY.md               # search, appraisal, tiering (§3.1) and scoring method
RESEARCH-JOURNAL.md          # per-claim verification verdicts
CHANGELOG.md                 # all revisions (citation stability)
methods/                     # search protocol, PRISMA runs, appraisal, rescore, taxonomy inputs
scripts/                     # count_reconcile.py, derive_*.py, dashboard, weekly checks, repoint_moved_paths.py
book-appendices/             # handbook appendices A-M, the public deep-evidence tier
working/                     # dated audits, intake notes, proposals, interview guides (index: working/README.md)
archive/                     # superseded working snapshots and session logs (index: archive/README.md)
published/                   # immutable 2025-10-22 release snapshots; never edited
```

## Integration
- **Writing**: essays live at securitydataworks.com/writing (the Security Data Commons Substack was retired 2026-05-24 and archived read-only)
- **Book**: citations for the MOAR handbook; its word count lives in the book repo's own build (derive, don't state)
- **Vendor database**: `vendor-landscape/` here, regenerated quarterly and gated by `scripts/derive_vendor_rollups.py`; the MCP server repo was archived 2026-07-01 and its spec is a record at `working/proposals/mcp-server-spec.md`

## Review rules (folded from the retired `.claude/review-protocol.md`, 2026-11-08)

- **apply_now** (edit without staging for Jeremy) requires ALL of: mechanically derivable from a named source; reversible in one commit; no narrative, voice or framing change; no price, tier or taxonomy choice; not touching a settled decision in the hub's DO-NOT-REFLAG list. Anything else is staged for the owner in the hub.
- **Numbers**: every quantitative claim in agent-drafted, publication-bound prose is re-derived by a different agent from the named source before commit; unverifiable means stage it, never ship it.

## Cloud sessions and Claude Code Projects (2026-11-15)

A Claude Code Projects thread loads this file and `.claude/rules/` only, not this repo's skills, commands, hooks or permission rules from `.claude/settings.json`, or `.mcp.json`. An ordinary single-repo cloud session or cloud routine does read the committed `.claude/settings.json` ([cloud sessions doc](https://code.claude.com/docs/en/claude-code-on-the-web), corrected 2026-11-15), but no cloud session gets git hooks, because a fresh clone has none, so these local gates do not run there: the pre-commit hook (`pre-commit.sh`) and the repo skills ([Projects docs](https://code.claude.com/docs/en/claude-projects), "What threads pick up from your repositories"). From a cloud thread, work on a branch and open a draft pull request, never push to `main` and never merge, and say in the pull request which of these local gates still need a local run before merge.
