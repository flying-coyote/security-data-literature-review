# U4 living docs: notes, verdicts and staged items (2026-11-17)

Scope: `PROJECT-BRIEF.md`, `monthly-update-tracker.md`, `isolation-first-security-tracking.md`, `LITERATURE-EXTRACTION-PLAN.md`, `PUBLICATION-VENUE-RECOMMENDATIONS.md`, `vendor-landscape/**`. No git, no CHANGELOG edits. Pre-edit copies of every rewritten file are in the session scratchpad (`qp/u4/*.before.*`) and in git HEAD.

## Gates at finish

- `python3 scripts/count_reconcile.py`: every U4 surface OK (PROJECT-BRIEF x7 incl. roster, monthly-tracker live status, venue header). At my last run two manuscript surfaces reported MISS ("manuscript 2.4 phase-4", "manuscript Table 1 Level-A"); those are in `PUBLICATION-MANUSCRIPT.md` (U2 scope, edited concurrently), not caused by U4.
- `python3 scripts/derive_vendor_rollups.py --check`: "all derived values match stored values; schema compliant" before and after the vendor edits. `--stats` 2026-11-17: 71 vendors, 92 logical sources (A 38, B 27, C 27, D 0), Tier-A share 41.3%, analyst coverage 30 (42.3%), production deployment 18 (25.4%), zero-source 11 (15.5%).
- `scripts/automation_dashboard.py` still parses the restructured tracker (latest month July 2026, 6.0 h/update).
- In-scope grep: zero `~/`, `/home/`, memory slugs, "FLAGGED for", hard-avoid words; no employer mention. Exceptions listed under Staged item 3.

## Vendor spot-verification (16 records, 2026-11-17)

| Record | Finding | Primary | Field change |
|---|---|---|---|
| rockset | Discontinued; OpenAI acquisition completed 2024-06-21, paid customers off-boarded by 2024-09-30; rockset.com 301 to OpenAI announcement | openai.com/index/openai-acquires-rockset/ ; docs.rockset.com FAQ (via search) | currency field only |
| dremio | SAP completed acquisition 2026-07-06 (announced 2026-05-04) | news.sap.com/2026/07/sap-completes-dremio-acquisition/ | currency field |
| fivetran | Fivetran + dbt Labs merger completed 2026-06-01 (announced 2025-10-13) | getdbt.com blog (completion post) | currency field |
| confluent-platform | IBM completion 2026-03-17 re-confirmed ($31/share, ~$11B EV) | confluent.io press release (pt-br copy), PR Newswire | currency field |
| exabeam | Merger with LogRhythm closed 2024-07-17; site now uses "New-Scale SIEM"/"New-Scale Fusion" and "LogRhythm SIEM" | exabeam.com | currency field (name kept) |
| rapid7-insightidr | InsightIDR relaunched as Incident Command (July 2025); /products/insightidr/ serves Incident Command | rapid7.com/products/insightidr/ | name -> "Rapid7 Incident Command (formerly InsightIDR)"; website trailing slash |
| minio | minio/minio archived read-only 2026-04-25, README "no longer maintained", points to AIStor Free/Enterprise | github.com/minio/minio | currency field |
| chronicle-security | chronicle.security 301 to Google Cloud "Google Security Operations" | cloud.google.com/security/products/security-operations | name -> "Google Security Operations (formerly Chronicle)"; website |
| azure-sentinel | Old URL redirects to Microsoft Sentinel page; duplicate of microsoft-sentinel; Azure-portal retirement 2027-03-31 (extended from 2026-07-01) | microsoft.com Sentinel page; learn.microsoft.com Sentinel what's-new (via search) | website; currency field |
| microsoft-sentinel | Live; same portal note | as above | currency field |
| databricks | Site names product "Databricks Data + AI Platform" | databricks.com | currency field (name kept) |
| crowdstrike-falcon-logscale | Live, name unchanged | crowdstrike.com LogScale page | currency field |
| talend | talend.com 301 to qlik.com/us/qlik-talend | qlik.com | website; currency field |
| starburst | Duplicate of starburst-enterprise; Starburst Data, Inc. still independent per site | starburst.io | currency field |
| starburst-enterprise | Live, built on Trino | starburst.io | currency field |
| ibm-qradar | Existing dr2 field already records PANW divestiture/EOLs; not re-fetched | (previously recorded) | currency field noting that |

Not verified: Snowflake (snowflake.com returned 403; "AI Data Cloud" naming unconfirmed), New Relic (DNS failure from this host; "New Relic One" and "Grok AI" naming in the record may be stale). Scores, tiers, evidence legs and rollups untouched.

## Tracker number ledger (monthly-update-tracker.md, isolation-first-security-tracking.md)

Verdicts use the U1 vocabulary. Each is also marked inline in the tracker.

| Location (history entry) | Figure | Verdict | Basis |
|---|---|---|---|
| Nov U1 Tenzir | 100+ Gbps | unverifiable-no-primary | bib entry URL is "LinkedIn post" |
| Nov U1 Cribl | 88-98% savings | unverifiable-no-primary | bib URL "CriblCon25 announcement" |
| Nov U1 Vortex | 5x/20x/100x | vendor claim, unvalidated | bib Level C, "NEEDS VALIDATION" |
| Nov U2 Netflix | isolation/Polaris/Level A | withdrawn | bib retitled 2026-07-09 (MASTER-BIBLIOGRAPHY.md:1395-1415) |
| Nov U2 Okta | expert validation | withdrawn | removed 2026-08-12 |
| Nov U2 Huntress | 93%, Iceberg, isolated AWS | 93% derivable (70K->5K = 92.9%; primary says ">90%"); Iceberg/isolation not-in-source | clickhouse.com Huntress blog, 2024-11-19, fetched 2026-11-17 |
| Dec U3 DORA | 2.7x staffing | withdrawn | bib MASTER-BIBLIOGRAPHY.md:580 |
| Dec U3 Prosci | 93% vs 15%; 183% | not-in-source | prosci.com/blog/change-management-best-practices fetched 2026-11-17: states "up to seven times more likely", 81% vs 15% (reinforcement); no 93% or 183% |
| Dec U3 MSRC | 200+ detections | unverifiable-no-primary | no bib entry |
| Dec U3 Cloudera TEI | 35%, 80%, $11.5M | unverified (bib: not re-verified, interactive TEI) | MASTER-BIBLIOGRAPHY.md:1441-1460 |
| Dec U3 Gartner | $183B/$212B/$292B, 11.7% | superseded; primary 403 | bib now $193B/$213B/$244B/$323B (2025-07-29 release) |
| Dec U3 Databricks | 11x / 377% | 11x verified (archive); 377% not landing-page-verifiable | bib MASTER-BIBLIOGRAPHY.md:617-634 |
| Dec U4 AI governance | <5%, 70-85%, 10x | unverifiable-no-primary | bib URL "LinkedIn professional discourse" |
| Dec U4 NANDA | 1,000+ agents | not-in-source (removed 2026-07-10) | bib note |
| Jan U6 ClickHouse | 400M rows/s, 5x | unverifiable-no-primary | not in bib |
| Jan U6 Kafka | 12x, 1M msg/s, 1.6B/30 min | unverifiable-no-primary | not in current Kafka entry |
| Jan U6 OCSF | 80%+ industry support | unverifiable-no-primary | no primary named |
| Jan U6 Databricks TCO | B->A upgrade; 9x | reversed (Level C 2026-08-19); 9x attributable to dateonic | bib MASTER-BIBLIOGRAPHY.md:1487-1512 |
| Feb U7 SACR | $200M ARR; 50-70%; 80%+; ~18 months | $200M, 80%, 18 months verified-at-primary (18 months unsourced in the article); 50-70% not-in-source (Axoflow 25-70%) | softwareanalyst.substack.com market guide, fetched 2026-11-17 |
| Feb U7 Rippling | $4.50/rule; <1 min latency | $4.50 verified (part 3); latency not in part 3 | rippling.com/blog/engineering-siem-part-3 |
| Feb U7 Monad | 50.7%, $1,929->$952 | verified with caveat (post states 50.14% and 50.7%; line items 50.65%) | monad.com post |
| Feb U7 OCSF | v1.7.0, 4 releases in 2025 | verified; current is 1.9.0 (2026-08-03) | github.com/ocsf/ocsf-schema/releases |
| Feb U7 DuckDB | v1.4.0 LTS "Jan 2026" | date wrong: released 2025-09-16 | duckdb.org/2025/09/16/announcing-duckdb-140 |
| Isolation tracker | 15-50% latency; 79% savings (500TB) | unverifiable-no-primary (planning targets stated as findings) | absent from bibliography and RESEARCH-JOURNAL.md |
| Isolation tracker | Huntress 1M EPS | not-in-source (already removed from bib) | MASTER-BIBLIOGRAPHY.md:976 |
| Isolation tracker | RLS +81%/+94%/-86% | verified-at-primary (first-party) | sdw-lab-benchmarks ocsf-rls-overhead/results/RESULTS.md:24-25 |
| All Level-A % in log (77-80%) | self-grade | withdrawn | METHODOLOGY.md §8.1a |

Process hours (4.7, 10.2, 6.1, 5.5, 6.5, 3.5, 4, 6 h) are first-party log values, left as logged.

## Venue facts (PUBLICATION-VENUE-RECOMMENDATIONS.md)

Verified at academic.oup.com on 2026-11-17: OA, first issue September 2015, scope statement (interdisciplinary / societal-implications requirement), 15,000-word paper limit, 350-word abstract, 5,000-word Perspectives, Oxford SciMed references, LMIC discount, Clarivate 2025 IF 4.4. Not verified: research-article APC (not displayed on the instructions page; DOAJ reports up to USD 1,994 but DOAJ returned 403 to a direct read), acceptance rate, all non-JoC venue facts. The October-2025 "Computer science approaches alone not sufficient" line is a paraphrase the About page supports: it states "computer science-based approaches, while necessary, are not sufficient to tackle cybersecurity challenges" (checked 2026-11-17).

## Cross-unit findings (outside U4 scope, for the owning unit or main session)

1. **U1 (bibliography)**: Prosci entry (MASTER-BIBLIOGRAPHY.md:532-556) states 93% vs 15% and 183% under a green mark; neither is on the cited page (see ledger). Huntress entry (951-981) lists "Iceberg data lake on isolated AWS infrastructure" and "Table-level RBAC" as Key Findings and "Chris Bisnett validation at RSA 2025" as the basis; the cited blog has neither, so these bullets look like the same mis-attribution class as Netflix. OCSF current release is 1.9.0 (2026-08-03), newer than the v1.8.0 the plan assumed.
2. **U2 (method)**: `METHODOLOGY.md:303` still states RQ7's "15-50% faster query performance" as part of the hypothesis; fine as a hypothesis, but it has no source and the first-party measurement shows the effect depends on query shape.
3. **U3 (gap analysis)**: `LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md:518` states "15-50% performance penalty when isolation could suffice" as an implication, and `:529` the same hypothesis; unsourced.
4. **U5 (structure)**: `.claude/commands/monthly-update.md` still uses the retired ">= 75% Level A" target (Quality Targets table, CHANGELOG template, checklist) and `git add -A`; `README.md:58` describes the isolation tracker as "15,800 words" (now about 1,400). The tracker now points refreshers at `/monthly-update`, so that command should match.

## Staged for the owner (not applied)

1. **Venue tactics content.** `PUBLICATION-VENUE-RECOMMENDATIONS.md` keeps its October-2025 strategy content (marketing rationale, APC cost judgement, co-author approach, CSUR/IEEE dual-track) on a public surface. Default: keep the verified JoC facts table and the comparison public, move the "Strategic Recommendation", "Recommendations by Goal" and "Next Steps" tactics to the hub. Not applied.
2. **Duplicate vendor records** (`azure-sentinel`/`microsoft-sentinel`, `starburst`/`starburst-enterprise`): merging changes vendor count and rollups. Default: merge at the next quarterly regeneration.
3. **Internal process text inside dated records**: `vendor-landscape/quarterly-updates/2026-Q3-regen-2026-07-18.md` ("Owner-ordered this session (\"do the vendor regen...\")", heading "Flagged to the owner") and `vendor-database.json` dated notes ("owner-ordered", "owner-gated", "-> owner re-score", "flagged for owner re-sourcing") carry owner-flag wording. Both are dated records under the never-retro-edit convention, so U4 left them. Default: leave the regen record body; reword the JSON `meta.notes` and per-leg notes to neutral "pending review" at the next regeneration.
4. **`validated_by: "Jeremy Wiley"`** in every vendor `evidence_summary` block (and `vendor-database-schema.md` example, owner lines) names the owner as validator of agent-run regenerations. Default: change to a role ("maintainer") in `derive_vendor_rollups.py --apply` at the next regeneration (script is U5 scope; changing stored blocks without the script would fail the gate).
5. **"Maintained by / Document Owner: Jeremy Wiley"** lines remain in the venue file and schema; removed from the two trackers and the brief as stale. Default: keep authorship in CITATION.cff only.
6. **New Relic and Snowflake records** were not verifiable this pass (DNS failure, 403); recheck at the next regeneration.
