# Vendor Landscape

This folder holds the review's vendor database: one structured record per platform (two platforms currently have duplicate records, see below) that the handbook and the literature review discuss, covering SIEMs, query engines, streaming platforms, lakehouse table formats, ETL and pipeline tools, object storage, catalogs, observability platforms and data-virtualization layers. Each record carries capability scores, the evidence behind each score with its tier, a cost model where one is published, and a derived summary of how well the record is evidenced. It is a working dataset rather than part of the paper, so it sits outside the Zenodo deposit, and readers who want the vendor narrative will find it in the handbook's Appendix G (`../book-appendices/appendix-g-vendor-landscape.md`), which draws on these records.

## What is here

| File | What it is |
|---|---|
| `vendor-database.json` | The database. `meta.version` names the current regeneration and `meta.vendor_count` the record count; every vendor's `evidence_summary` block is derived, not typed. |
| `vendor-database-schema.md` | The schema, including the Evidence Tier Requirements table that bounds each capability score by the tier and number of its sources. |
| `quarterly-updates/` | One dated record per regeneration (never edited after the fact) plus `TEMPLATE-YYYY-QX-update.md`. The first is `2026-Q3-regen-2026-07-18.md`. |
| `MCP-VENDOR-INTEGRATION-SUMMARY.md` | Historical record of the October 2025 integration with the `security-architect-mcp-server` repository, which was archived on 2026-07-01. Nothing in it describes a running process. |

## How the database is maintained now

The database is on a quarterly regeneration cadence, in January, April, July and October, run by hand in this repository, though the last regeneration was 2026-07-18 (version 2026-Q3-c) and the October 2026 one is overdue. It is manual because the automated sync and weekly refresh described in the October 2025 integration record ended when the MCP server repository was archived. A regeneration re-checks evidence legs at their live primaries, folds in verified vendor changes (acquisitions, renames, end-of-life dates, pricing terms) as dated fields on the affected record, re-derives capability scores against the schema's tier table, and then recomputes every `evidence_summary` block with `scripts/derive_vendor_rollups.py --apply`. Each regeneration leaves a dated record in `quarterly-updates/` naming what changed and why, so a citation to a particular snapshot can be traced to its state at the time.

The rollup figures are the part most prone to drift, since the October 2025 hand-stated rollups overstated the Tier-A share by about forty points, so they are not stated as a live figure outside dated snapshots. `scripts/derive_vendor_rollups.py --check` recomputes every vendor's rollup from its source objects, compares it with the stored block and enforces the schema's score-to-evidence rules, and it runs both in `scripts/pre-commit.sh` and in the CI workflow `.github/workflows/gates.yml`, so a hand edit to the JSON that breaks either is caught by the local hook where it is installed and by CI on push. To read the current aggregates, run:

```bash
python3 scripts/derive_vendor_rollups.py --stats   # totals, tier counts, analyst and production coverage
python3 scripts/derive_vendor_rollups.py --check   # the gate
```

For orientation only, a `--stats` run on 2026-11-17 reported 71 vendors and 92 logical evidence sources (38 Tier A, 27 Tier B, 27 Tier C, none at Tier D), with 11 vendors carrying no source at all; those 11 say so in their own records (`overall_evidence_quality: unevidenced`). Vendor tiers here still use the pre-2026-08-19 definition, in which a verified production deployment counts as Tier A; under METHODOLOGY.md §3.1 most of these legs would be Level B, so this Tier-A count is not comparable with the bibliography's Level-A share (noted 2026-11-22). The vendor count can also be read straight from the JSON with `python3 -c "import json; print(len(json.load(open('vendor-landscape/vendor-database.json'))['vendors']))"`, and by category the 71 split into 19 SIEM (one record still labelled "SIEM Platform"), 10 streaming, 9 query engine, 7 lakehouse, 6 ETL/ELT, 5 object storage, 5 catalog and governance, 5 observability, 4 data virtualization and 1 OLAP engine.

Between full regenerations, a lighter currency check can add a dated `currency_check_YYYY_MM_DD` field to individual records without touching scores or rollups. The 2026-11-17 check covered 15 records at a primary, plus a pointer on `ibm-qradar` to its existing 2026-07-18 field, and recorded, among other things, that Rockset is discontinued (OpenAI acquisition, 2024), that SAP completed its acquisition of Dremio on 2026-07-06, that Fivetran and dbt Labs completed their merger on 2026-06-01, that Rapid7 launched Incident Command in July 2025, which now occupies the InsightIDR product page, and that the open-source MinIO repository was archived in late April 2026. Two pairs of records are duplicates kept for continuity (`azure-sentinel` with `microsoft-sentinel`, and `starburst` with `starburst-enterprise`); merging them changes the vendor count and the rollups, so it waits for the next full regeneration.

## Evidence rules that apply here

Vendor-authored material (product documentation, pricing pages, a vendor's own announcement of an analyst placement) describes what a product does and is cited for that, but it is tiered C under the vendor-channel rule when it is the only support for a claim about how well the product works, and analyst placements are read at a public primary because the reports themselves are licensed. A capability score of 5 needs three or more Tier-A sources (Tier A in the pre-2026-08-19 sense noted above), which most platforms do not have, so many scores fell to 3 or 4 in the 2026-Q3-c regeneration; that reflects the schema being enforced rather than new doubt about the platforms, and a score goes back up only when new evidence is added.

## Open items

Five things are known and not yet done. The October 2026 regeneration is overdue, so `meta.version` is still 2026-Q3-c and `quarterly-updates/` holds one dated record, from 2026-07-18. Several vendor-documentation legs of the same class as the Sentinel pricing leg still sit at Tier B (the 2026-Q3-c record names eight by id) and need the same vendor-channel review, which belongs to the pending re-tier ratification rather than to a regeneration. The two duplicate pairs above need merging. And the planned derived views, a capability matrix and a market-trends page, were never built; if they are, they should be generated from the JSON so they cannot drift from it. And the vendor legs still use the pre-2026-08-19 tier definition; re-tiering them to METHODOLOGY.md §3.1 moves scores, so it belongs to an owner-gated regeneration rather than a hand edit.

## History

The folder was set up in October 2025 to hold quarterly vendor snapshots fed by an analyst-data partnership and synchronized with the MCP server repository. The partnership did not go ahead before the integration it was meant to feed was archived, the synchronized repository was archived on 2026-07-01, and no quarterly snapshot shipped until the 2026-Q3-c regeneration on 2026-07-18, which replaced the October 2025 rollups with derived ones. The full change history is in `../CHANGELOG.md`.

---
**Last updated**: 2026-11-22 (tier-definition note and currency-check wording); 2026-11-17 (currency check of 15 records plus one pointer; page rewritten to describe the mechanism as it runs)
