---
type: operating-doc
title: "Monthly Literature Review Rolling Update Checklist"
created: 2026-01-02
tags: [literature-review, monthly-cadence, bibliography, source-freshness, quality-assurance]
---

# Monthly Rolling Update Checklist

Execute this checklist for the monthly literature review update.

## Pre-Update Assessment (15-30 min)

### 1. Run Health Check
```bash
python3 scripts/weekly_health_check.py
```
Review output for:
- Broken links requiring fixes
- Outdated sources (>12 months) flagged for refresh; refresh the flagged ones that still carry a cited claim
- Evidence level distribution

### 2. Check Automation Dashboard
```bash
python3 scripts/automation_dashboard.py
```
Note the Level-A share as a description (there is no target since the 2026-08-19 ruling, METHODOLOGY §8.1a) and confirm the readiness checks pass. `python3 scripts/count_reconcile.py` gives the exact counts.

### 3. Review External Inputs
- [ ] Review securitydataworks.com/writing feedback and comments for reader-surfaced sources
- [ ] Review the owner's LinkedIn saved-items export for new sources
- [ ] Check the Lab benchmarks (securitydataworks.com/lab) for new first-party measured evidence to cite
- [ ] Check published essays for citation opportunities

> Note: the old Security Data Commons Substack was retired 2026-05-24; the live channel is
> securitydataworks.com (`/writing`, `/research`, `/lab`). Do not look for Substack feedback.

## Update Tasks (4-6 hours)

### 1. Add New Sources (2-3 sources typical)
For each new source, apply the Evidence Level under METHODOLOGY §3.1 (`/add-source` walks it):
- A: peer-reviewed research at a confirmed venue, standards-body documents, formal open-standard specifications, MITRE D3FEND / ATLAS
- B: production and practitioner evidence, talks, analyst reports, project documentation, venue-less preprints
- C: vendor material with no production measurement, bias flagged, never carrying a hypothesis alone
- D: excluded

Update MASTER-BIBLIOGRAPHY.md with:
- Full citation metadata
- Evidence tier classification
- Related hypotheses (H-XX references)
- Key insights summary

### 2. Refresh Outdated Sources (3-5 sources)
Select from health check's outdated sources list:
- Prioritize hypothesis-critical sources
- Update URLs if changed
- Verify data still accurate
- Add newer corroborating evidence if available

### 3. Fix Broken Links
Address any links flagged in health check:
- Find replacement URLs
- Mark as [Archived] if no replacement available
- Document in source notes

### 4. Re-derive the counts
Run `python3 scripts/count_reconcile.py`. If a gated surface disagrees, update the line it names (README.md, PROJECT-BRIEF.md, the manuscript and the others in its ALLOWLIST); never type a count into a file the gate does not cover. Add the dated taxonomy record under `methods/` and run `python3 scripts/derive_source_taxonomy.py --check`.

## Post-Update Verification (30-45 min)

### 1. Run Health Check Again
```bash
python3 scripts/weekly_health_check.py
```
Confirm:
- No new broken links introduced
- `count_reconcile.py` and `repoint_moved_paths.py --check` pass

### 2. Update Tracking Documents
Update monthly-update-tracker.md with:
- Date and version
- Time invested (hours)
- Sources added/refreshed
- Counts from `count_reconcile.py`
- Key changes summary

### 3. Update CHANGELOG.md
Add new version entry:
```markdown
## [1.XX.0] - YYYY-MM-DD

### Added
- [Source count] new sources
- [Topic] evidence for [RQ]

### Changed
- Refreshed [count] outdated sources
- Fixed [count] broken links

### Counts
- [paste the first two lines of `python3 scripts/count_reconcile.py`]
```

### 4. Commit
Stage the files you changed by name (not `git add -A`), commit, and let the pre-commit gate run. From a cloud thread, open a draft pull request instead of pushing (see `.claude/CLAUDE.md`).

## Quality Targets

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| Time Investment | <= 10 hours | Streamline workflow |
| Sources Added | 2-5 per month | Increase if gaps found |

## Session Complete Checklist

- [ ] Health check passes
- [ ] `count_reconcile.py` passes
- [ ] monthly-update-tracker.md updated
- [ ] CHANGELOG.md updated
- [ ] Changes committed
- [ ] Time tracked for this session
