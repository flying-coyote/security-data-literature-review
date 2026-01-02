# Monthly Rolling Update Checklist

Execute this checklist for the monthly literature review update.

## Pre-Update Assessment (15-30 min)

### 1. Run Health Check
```bash
python3 scripts/weekly_health_check.py
```
Review output for:
- Broken links requiring fixes
- Outdated sources (>12 months) flagged for refresh
- Evidence level distribution

### 2. Check Automation Dashboard
```bash
python3 scripts/automation_dashboard.py
```
Verify:
- Evidence Level A percentage (target: >= 75%)
- All readiness checks pass

### 3. Review External Inputs
- [ ] Check Substack comments for reader feedback
- [ ] Review LinkedIn monitoring for new sources
- [ ] Check blog posts for citation opportunities

## Update Tasks (4-6 hours)

### 1. Add New Sources (2-3 sources typical)
For each new source, apply Evidence Tier Classifier:
- Tier 1: Production deployments (Evidence Level A)
- Tier 2: Peer-reviewed (Evidence Level A)
- Tier 3: Expert consensus (Evidence Level B)
- Tier 4/5: Avoid unless necessary

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

### 4. Update Evidence Percentages
If source distribution changed:
- Recalculate Evidence Level A percentage
- Update CLAUDE.md if threshold changed
- Update README.md metrics

## Post-Update Verification (30-45 min)

### 1. Run Health Check Again
```bash
python3 scripts/weekly_health_check.py
```
Confirm:
- No new broken links introduced
- Evidence Level A maintained or improved

### 2. Update Tracking Documents
Update monthly-update-tracker.md with:
- Date and version
- Time invested (hours)
- Sources added/refreshed
- Evidence Level A percentage
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

### Quality Metrics
- Evidence Level A: XX% (target: >= 75%)
- Total sources: XXX
```

### 4. Commit and Push
```bash
git add -A
git commit -m "Monthly update: Version 1.XX.0 - [brief summary]"
git push
```

## Quality Targets

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| Evidence Level A | >= 75% | Add Tier 1-2 sources |
| Time Investment | <= 10 hours | Streamline workflow |
| Sources Added | 2-5 per month | Increase if gaps found |

## Session Complete Checklist

- [ ] Health check passes
- [ ] Evidence Level A >= 75%
- [ ] monthly-update-tracker.md updated
- [ ] CHANGELOG.md updated
- [ ] Changes committed and pushed
- [ ] Time tracked for this session
