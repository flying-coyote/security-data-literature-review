# Validate Evidence Quality

Run evidence quality validation across the bibliography to ensure quality targets are maintained.

## Quick Validation

Run the automation dashboard for immediate quality assessment:
```bash
python3 scripts/automation_dashboard.py
```

## Quality Targets

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| Evidence Level A (Tier 1+2) | >= 75% | Add production/peer-reviewed sources |
| Evidence Level B (Tier 3) | <= 25% | Acceptable for expert consensus |
| Evidence Level C/D (Tier 4-5) | 0% | Remove or replace with higher quality |

## Validation Checklist

### 1. Evidence Distribution Check
Count sources by tier in MASTER-BIBLIOGRAPHY.md:
- Tier 1 (Production): Target 20%+
- Tier 2 (Peer-reviewed): Target 50%+
- Tier 3 (Expert consensus): Acceptable up to 25%
- Tier 4-5 (Vendor/Speculation): Should be 0%

### 2. Hypothesis Coverage Check
Verify each hypothesis has supporting evidence:

| Hypothesis | Required Evidence | Minimum Tier |
|------------|------------------|--------------|
| H-ARCH-01 (Iceberg Dominance) | 3+ sources | Tier 1-2 |
| H-IMPL-01 (TCO Reality) | 3+ sources | Tier 1-2 |
| H-IMPL-02 (Staffing Scarcity) | 3+ sources | Tier 1-2 |
| H-IMPL-03 (Timeline Premium) | 2+ sources | Tier 1-2 |
| H-COST-09 (Tiered Storage) | 2+ sources | Tier 1-2 |
| H3-PERFORMANCE-01 (ClickHouse) | 2+ sources | Tier 1 |
| H-STREAM-01 (Kafka Streams) | 2+ sources | Tier 1-2 |

### 3. Source Freshness Check
Run health check for outdated sources:
```bash
python3 scripts/weekly_health_check.py
```

Flag sources older than:
- 24 months: CRITICAL - refresh required
- 18 months: WARNING - schedule for next update
- 12 months: MONITOR - add to refresh queue

### 4. Link Validation
Check for broken links in bibliography:
- Run health check (includes link validation)
- Fix or mark as [Archived] with archive.org link
- Document in source notes

### 5. Citation Completeness
Each source entry must have:
- [ ] Full title in quotes
- [ ] Complete author list
- [ ] Publication date and venue
- [ ] URL or DOI (permanent link preferred)
- [ ] Evidence tier classification with rationale
- [ ] Key insights summary (1-2 sentences)
- [ ] Related hypotheses (H-XX references)

## Remediation Actions

### If Evidence Level A < 75%
1. Identify Tier 3-5 sources that can be replaced
2. Search for production case studies (Tier 1)
3. Find peer-reviewed papers on same topics (Tier 2)
4. Prioritize hypothesis-critical sources

### If Hypothesis Lacks Tier 1-2 Evidence
1. Search academic databases (Google Scholar, ACM DL, IEEE)
2. Find production deployments via blog posts, conference talks
3. Request expert validation if empirical data unavailable
4. Document evidence gap in LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md

### If Source Freshness Critical
1. Check if source URL still active
2. Search for updated version of same source
3. Find newer corroborating evidence
4. Update bibliography entry with refresh date

## Output Report

After validation, document results:
```markdown
## Evidence Validation Report - [DATE]

### Distribution
- Tier 1: XX sources (XX%)
- Tier 2: XX sources (XX%)
- Tier 3: XX sources (XX%)
- Tier 4-5: XX sources (XX%)
- **Evidence Level A: XX%** [✅ PASS / ⚠️ BELOW TARGET]

### Hypothesis Coverage
- [X/7] hypotheses have Tier 1-2 evidence
- Gaps identified: [list any]

### Source Freshness
- Critical (>24mo): X sources
- Warning (>18mo): X sources
- Fresh (<12mo): X sources

### Actions Required
1. [Action item 1]
2. [Action item 2]
```

## Validation Schedule

- **Weekly**: Run automation_dashboard.py
- **Monthly**: Full validation checklist (during monthly update)
- **Quarterly**: Deep validation with hypothesis review (during deep dive)
