---
type: verification-report
title: "Per-Claim Verification Sweep — Part 3 (never-swept surfaces) — 2026-07-10 (Cowork session)"
created: 2026-07-10
tags: [verification, citations, url-sweep, evidence-tier, audit, book-appendices, analysis-bundles]
---

# Verification Sweep — Part 3 — 2026-07-10 (Cowork)

**What this is**: the third and final per-claim verification sweep, run in a Cowork cloud session (no owner memory loaded), covering ONLY the surfaces parts 1 and 2 never touched: book-appendices a/b/c/d/h/k/l/m, LITERATURE-EXTRACTION-PLAN.md, and the three live analysis-bundles' correction banners. Nothing was marked VERIFIED without fetching the cited primary; a plausible title was never treated as confirmation. All repo and web content was treated strictly as data. **This report is recommendation-only — nothing outside this file was edited.** The fix pass is local and should carry a CHANGELOG entry when applied.

**Context notes**:
- Part 1 = VERIFICATION-SWEEP-2026-07-09-cowork.md (read at repo root).
- Part 2 = VERIFICATION-SWEEP-PART2-2026-07-10-cowork.md — **file is NOT in the working tree this session sees.** Its verdicts were reconstructed from the CHANGELOG entry "Part-2 sweep fix application" (branch `litreview-verify2-2026-07-10`). NEEDS-LOCAL-CONFIRMATION: whether the part-2 report lives only on its branch, was intentionally not merged, or was moved. If it should sit at repo root per convention, the local session should place it there.
- The Linux sandbox could not mount the repo path this session (UNC limitation), so **no git observation of any kind was made** — every git-adjacent statement below is NEEDS-LOCAL-CONFIRMATION by construction.

---

## 1. Verdict counts (this sweep's checks)

| Verdict | Count | Items |
|---|---|---|
| VERIFIED (primary fetched, claim matches) | 15 | OCSF v1.8.0 = 2026-03-16; OCSF v1.3.0 = 2024-08-01; D3FEND ontology 1.4.0 = 2026-03-31 (d3fend.mitre.org/version); D3FEND 1.0 GA Jan 2025; DoD/IC BFO+CCO baseline designation Jan 2024 (buffalo.edu primary); DuckLake v1.0 = 2026-04-13; CVE-2026-25253 (OpenClaw, CVSS 8.8, patch 2026.1.29, gatewayUrl chain, ~40K exposed); arXiv:2601.10338 (31,132 skills / 26.1% / 13.3% exfil / 11.8% priv-esc — all verbatim); G-Cloud 14 pricing PDF live + all six quoted rates verbatim ($2,049.30 / $793.50 / $764.75 / $598.00 / $448.50 / $431.25); Met Police Splunk-CDW deal (£780K + £1.774M over 5 years, DPS, CDW — GLA decision PCD 1331); securitydataworks.com/writing/engines/materialized-views (live, content consistent); PaloAltoNetworks/Splunk-Apps repo archived (2024-12-14, read-only); book-appendices/figures/moar-architecture.png exists; Cisco acquired **Splunk** (not Cribl) March 2024; SDW-lab 45–77× MV first-party figure consistent between appendix C and the live essay |
| CONTRADICTED | 1 | Appendix B AP#9: "2024: Cisco acquires Cribl" — **no such acquisition exists**; Cisco acquired Splunk (2024-03-18); Cribl remains independent (Splunk in fact won an IP case *against* Cribl in April 2024) |
| CLAIM-MISMATCH / drift | 4 | "78× to 9,000×" MV range in appendices C+D (units + attribution error — see §3.6); appendix C "51-270× … Splunk DMA docs" attribution (essay credits 270× to unsafehex.com practitioner post; "51×" unlocated); appendix C Netflix/Muino meetup "late 2024" vs bibliography-corrected July 2025 talk / Oct 2025 blog; appendix D line ~422 "Glacier ($0.001/GB/month)" conflates Deep Archive (~$0.00099) with "Glacier" while A.6 prices Glacier Flexible at $0.0036 |
| PARTIAL | 2 | arXiv:2604.03070 exists and title matches ("How Your Credentials Are Leaked by LLM Agent Skills"); the 17,022 / ~3.1% figures NOT re-verified (PDF unreadable to the fetcher). Met Police detail: headline figures verified; the "10% discount for the five-year commitment" clause and the "2024 deal" year not confirmed in the fetched snippet (PCD funding year reads 2022/23) — confirm against the full PCD 1331 text |
| NO-PRIMARY-IN-REPO (flagged, not fetched or unfetchable) | 8 | Appendix K.3 "Gartner (6-8 FTEs for multi-region data platform management)"; K.3 "Denodo public enterprise pricing (validated $1.2M/year…)" — no Denodo entry exists in MASTER-BIBLIOGRAPHY; staffing-calculator "IBM Cost of a Data Breach 2024: $200K avg difference <30min vs >1hr detection" — no IBM CODB entry in bibliography and the stat does not resemble the report's published lifecycle framing; staffing-calculator Altinity 70%/40% (already self-flagged unconfirmed at line ~499 but used unflagged in Calculator 5); appendix C "Splunk ES ~1,700 correlation rules" (likely conflates ES's bundled correlation searches with the ESCU detection count — no primary cited); appendix C Apple "Baris Aydın, Subsurface Live 2023" (no bibliography entry; talk not fetched); appendix H §H.3.1 2 PB/day case study (correctly labeled Tier C but carries **no URL/citation anywhere** — unciteable as it stands); staffing-calculator "Gartner security lakehouse average: 3 months" / "6-12 month ramp-up (Gartner)" / "3-4 FTE core teams (Gartner)" (same unverifiable-Gartner family as the withdrawn 5.5-month leg) |
| STALE-VS-CURRENT-BIBLIOGRAPHY (banner/coverage gaps in the three bundles + extraction plan) | ~20 line-items | detail in §4 and §5 — these are the sweep's most important findings |
| NOT-FETCHED this pass (honest residue) | 12 | see §6 |

**Headline**: the eight never-swept appendices are **clean of the withdrawn-legs watch list** — no live DORA 2.7×/3.2×/Level-4, IDC, Ververica, MIT-TR, DOES, Gartner-5.5-month, AWS-55%, Netflix-70-80%, Shell-57TB, EDQ, or universal-vendor-support assertions anywhere in appendices a/b/c/d/h/k/l/m. The appendices written or reworked post-audit (h, k, l, m, and most of a/c/d) carry conspicuously good tier-labeling hygiene. The watch-list legs survive **only** in the two book-cited analysis-bundles (where the 2026-07-10 folded corrections missed spots) and, in softened form, in LITERATURE-EXTRACTION-PLAN.md's un-bannered self-grades. One new fabrication-class finding (Cisco-Cribl) was found in appendix B.

---

## 2. Coverage per file (honest accounting — nothing silently truncated)

1. **appendix-a-decision-worksheets.md** — read in full (1,157 lines). External anchors fetched: G-Cloud 14 PDF (live; all six quoted rates verbatim), Met Police GLA PCD 1331 (headline figures verified). NOT re-fetched: aws.amazon.com/s3/pricing, aws.amazon.com/athena/pricing, azure.microsoft.com Sentinel pricing — rationale: the file self-stamps these "verified 2026-07-06 (Azure Retail Prices API)" and part 1's H-COST-09 restoration re-fetched live S3 US-East-1 list prices on 2026-07-09; the internal arithmetic (e.g., Deep-Archive ~23× vs Standard = 0.023/0.00099) is consistent with those stamps. Zero watch-list legs. Illustrative/directional figures are tier-labeled at the claim site throughout.
2. **appendix-b-anti-patterns.md** — read in full (858 lines). One CONTRADICTED finding (Cisco-Cribl, §3.1). OCSF v1.8.0 references verified. Jake Thomas/Okta figures trace to the bibliography's Tier-B personal-communication entry (labeled as such in the appendix). Prosci appears only as a properly hedged rule-of-thumb attribution — no withdrawn 30/60/80 assertion. AP#12 is internally consistent with appendix D's PR #294 account and appendix M's coverage instrument.
3. **appendix-c-reference-architectures.md** — read in full (1,058 lines). securitydataworks.com essay fetched (live); MV first-party 45–77× consistent; two mismatch findings on the vendor-range figures (§3.6). moar-architecture.png exists. SAP-Dremio July 2026 consistent with part 1's verification (not re-fetched). Netflix 5 PB/day consistent with the bibliography's two verified entries; the "late 2024" meetup date is drift against the 2026-07-09 correction (talk July 2025). Splunk ES "~1,700 correlation rules" and Apple/Aydın flagged NO-PRIMARY. Cost tables are consistently labeled A.6-model outputs.
4. **appendix-d-glossary-translation-guide.md** — read in full (775 lines). DuckLake v1.0 date verified; PAN Splunk-Apps archived verified (PR #294 itself not individually fetched — GitHub API returned empty to this fetcher; the PR URL is cited in-text and the surrounding facts check out; one local click closes it). OCSF v1.8.0/March-2026 verified. HIPAA 45 CFR 164.316(b)(2)(i) 6-year, PCI-DSS 1-year, SOX 7-year cites reviewed as consistent with the well-known statutory text (not re-fetched). One minor internal pricing inconsistency (§3.7). tabular-io/iceberg-rest-image not fetched (residue).
5. **appendix-h-ocsf-strategy.md** — read in full (1,023 lines). OCSF v1.8.0 (2026-03-16) and v1.3.0/d3fend (August 2024) verified at the GitHub releases page; D3FEND 1.0 GA (Jan 2025) and the Jan-2024 DoD/IC BFO+CCO designation verified (buffalo.edu). The appendix's own hedges on FY2027/ATO claims, NIST/NATO/MITRE-AI Tier-D items, and Splunkbase download counts are accurate as written — no action needed there. The G-Cloud "$1,240/GB/day/yr platform+ES" anchor is verbatim-consistent with the fetched PDF ($793.50+$448.50). §H.3.1's 2 PB/day case study: honestly tier-labeled but **uncited** — flag. Flexera 89% and W3Techs ~96% not fetched (residue; both hedged in-text).
6. **appendix-k-three-journeys-walkthroughs.md** — read in full (968 lines). Composite/A.6-model labeling is thorough and repeated at each journey head. Two Evidence-line flags in K.3 (§3.8): the "Gartner 6-8 FTEs" attribution and the "validated" claim on Denodo pricing, neither of which has a primary in the repo — K.2's parallel Evidence line was already softened ("not a sourced Gartner rate"), so K.3 just needs the same treatment. IT Harvest 83-vendor count properly hedged.
7. **appendix-l-implementation-operations-detail.md** — read in full (233 lines). CVE-2026-25253 verified in detail; arXiv:2601.10338 verified verbatim; arXiv:2604.03070 partial (title only). AIVSS v0.8 / AIUC-1 / Microsoft Agent 365 / Temporal-Dapr not fetched — all carry in-text Tier C/B labels with explicit verify-before-citing hedges, so the text is safe as written; closing them is optional local work. L.3/L.4/L.5 are explicitly composite/illustrative. Zero watch-list legs.
8. **appendix-m-detection-coverage.md** — read in full (93 lines). D3FEND 1.4.0 / 2026-03-31 verified exactly (including the careful OCSF-attribute-version vs ontology-version disambiguation, which is correct). Axelsson 2000 and Sommer-Paxson 2010 are real Tier-A classics already grounded in the bibliography. Tidal Cyber (Mar 2026) and Atkinson/SpecterOps not re-fetched (residue; both tier-labeled with the vendor-incentive flag already in place). First-party C5/SCG figures are internally consistent and clearly scoped; the deliberate "no 27 zero-defense figure" self-correction is the right kind of note. The T1071→4003 (DNS C2 rule) vs T1071→4001 (beacon hunt) difference across M.2/M.3/M.4 is legitimate (different detections over different classes), not an error.
9. **LITERATURE-EXTRACTION-PLAN.md** — read in full (329 lines); counts/process claims checked against current repo reality (§5).
10. **analysis-bundles/cost-reality-reference.md, staffing-budget-calculator.md, hypothesis-confidence-matrix.md** — read in full; every banner claim cross-checked against the current MASTER-BIBLIOGRAPHY entries (TEI at :1431-1469, Gartner CAGR note at :2971, DORA at :549-573, Samza at :704-721, Iceberg contributors at :1750, SANS/timeline note at :2967, Huntress at :976-1028). WITHDRAWN markers themselves were NOT re-flagged (they are records); findings below are strictly (a) live un-struck assertions the corrections missed and (b) banner statements now contradicted by the post-banner bibliography. Detail in §4.

---

## 3. Findings in the eight appendices, ranked

### 3.1 ⚠️ Appendix B AP#9 asserts a Cisco acquisition of Cribl that never happened (CONTRADICTED — worst new finding)

`appendix-b-anti-patterns.md` states twice, as fact inside a "Fortune 500 Retail" case: "Our Cribl license went from $800K to $2.4M **after Cisco acquisition**" (symptom quote) and "**2024: Cisco acquires Cribl**, 3× price increase" (Real-World Consequences). Cisco acquired **Splunk** (completed 2024-03-18, ~$28B); Cribl has never been acquired by Cisco and remains independent — Splunk actually won an IP suit against Cribl in April 2024. This is fabricated-attribution class (an invented real-world event anchoring a dollar consequence), the same failure family the 2026-06 audit existed to purge, in a file the audits never reached. Note the case reads as an anonymized composite, but naming two real companies in a false M&A event is not anonymization. Recommend: reframe as an explicit hypothetical ("if your pipeline vendor were acquired and list price tripled…") or anonymize the vendor names entirely; do not keep "Cisco acquires Cribl" in any form.

### 3.2 Appendix A's pricing anchors check out end-to-end (strong positive)

The G-Cloud 14 EMEA distributor PDF is live at the cited URL and every rate the appendix quotes is verbatim in it: Splunk Cloud $2,049.30 (5-9 GB/day), $793.50 (2,000-4,999), $764.75 (5,000-9,999); Enterprise term $598.00 (2,000-4,999); ES $448.50 (2,000-4,999) and $431.25 (5,000-9,999). The derived figures ($1,196 and ~$1,240 platform+ES, the $14.35M list at 12 TB/day) reproduce from those rates. The Met Police anchor is real and matches the GLA decision record (PCD 1331: £780,000 project revenue 2022/23 + £1,774,000 ongoing over five years, awarded to CDW Ltd for DPS CONNECT audit). Two small residues: (a) the appendix calls it a "2024 Splunk SaaS deal" while the PCD funding year reads 2022/23 — check the PCD's decision date and align; (b) the "locked a 10% discount" detail wasn't in the fetched snippet — confirm against the full PCD text and add the PCD 1331 URL as the citation (the appendix currently names the deal without a source link).

### 3.3 Appendix H's external spine verifies cleanly (positive)

OCSF v1.8.0 released 2026-03-16 (exact); d3fend attribute landed in v1.3.0, released 2024-08-01 ("August 2024" ✓); D3FEND 1.0 GA January 2025 ✓; the January-2024 DoD/ODNI/CDAO designation of BFO+CCO as baseline standards is confirmed at the University at Buffalo release the appendix cites as its Tier-B source ✓. The appendix's refusal to assert the FY2027/ATO enforcement claims without a primary is validated — searches surface no such primary. One fix: §H.3.1's 2 PB/day deployment is tier-labeled but has no citation at all; either add the vendor case-study URL to the bibliography and cite it, or mark it explicitly "unciteable — no primary on file."

### 3.4 Appendix M's standards claims verify exactly (positive)

D3FEND ontology 1.4.0, release date 2026-03-31 — verbatim from d3fend.mitre.org/version, matching the part-2 flag-closure. The M.2 disambiguation (OCSF *attribute* introduced in OCSF v1.3.0 vs D3FEND-the-ontology at 1.4.0) is correct on both halves — both halves now primary-verified.

### 3.5 Appendix L's incident spine verifies (positive, with one partial)

CVE-2026-25253 is real and matches every detail the appendix carries (OpenClaw ex-Clawdbot, CVSS 8.8, patched 2026.1.29, unvalidated `gatewayUrl` → token exfil → RCE, ~40K exposed instances, early-Feb-2026 disclosure; SonicWall/ProArch/THN advisories exist as cited). arXiv:2601.10338 matches verbatim on all four quoted figures. arXiv:2604.03070 exists with the exact quoted title; its 17,022/3.1% figures could not be re-read (PDF served no machine-readable text) — one local PDF open closes it.

### 3.6 Appendices C and D carry a units-and-attribution error on the materialized-view range (CLAIM-MISMATCH)

Both appendices state MVs deliver "**78× to 9,000×** speedups in the vendor literature (Tier C)". The author's own cited essay (fetched, live) says: Snowflake's published figure is "roughly **78% query improvement**" (a percentage, not a multiplier) and the 9,000× top end comes from a **single-developer PostgreSQL case study** (Sid Ngeth, 350×–9,000×), not vendor literature. So "78×" is a units error and "vendor literature" mislabels the 9,000× source. Recommend: replace the range with the essay's actual decomposition (Snowflake ~78% improvement; single-developer PostgreSQL case study 350×–9,000×; practitioner Splunk DMA 270×), or simply "roughly 270×–9,000× across published anecdotes (Tier C/D, not vendor-official)". Related: appendix C's Pattern-4 note attributes "51-270× speedups documented" to docs.splunk.com — the essay credits the 270× to a practitioner write-up (unsafehex.com), and no source for "51×" was located; fix the attribution or drop the range.

### 3.7 Minor drift items (appendices C, D)

(a) Appendix C: Netflix/Muino attribution says "ClickHouse meetup presentation, **late 2024**" — the bibliography corrected this 2026-07-09 to the July 2025 meetup talk (blog Oct 23, 2025); align the date. (b) Appendix D hot/cold example prices "Glacier ($0.001/GB/month)" — that's the Deep Archive rate (~$0.00099); A.6 prices "Glacier Flexible" at $0.0036. Name the tier ("Glacier Deep Archive ~$0.001") to keep D and A.6 consistent. (c) Appendix D's example repo pointer github.com/tabular-io/iceberg-rest-image was not fetched; Tabular is now Databricks, so verify the repo still resolves (or point at the apache/iceberg-rest-fixture successor) in the fix pass.

### 3.8 Appendix K.3's Evidence line needs the K.2 treatment (NO-PRIMARY)

K.2's Evidence line was already fixed to say "directional scenario assumptions, not a sourced Gartner rate." K.3's parallel line still asserts: "**Gartner (6-8 FTEs for multi-region data platform management)**" — no such Gartner source exists in the repo (and the Gartner staffing/timeline family has a 100% failure rate in these audits) — and "**Denodo public enterprise pricing (validated $1.2M/year** for multi-region deployment with 8 connectors)" — no Denodo entry exists in MASTER-BIBLIOGRAPHY, and "validated" is exactly the word the repo's conventions reserve for fetched primaries. Recommend: soften both to author-modeled/directional, or add real primaries (a Denodo AWS-Marketplace listing would be a citable public price anchor if one at this shape exists).

---

## 4. The three live analysis-bundles: banner-consistency findings (the sweep's core)

Per instruction, WITHDRAWN markers were not re-flagged. The findings below are only (a) live, un-struck assertions the folded corrections missed, and (b) banner claims now contradicted by the current bibliography. Watch-list legs are marked ⚑.

### 4.1 cost-reality-reference.md — the 2026-06-14 banner is stale against three post-banner verdicts

The banner predates the 2026-07-09/10 fix passes and three of its "survives the audit" claims are now contradicted by the current bibliography:

1. ⚑ **DORA "Level 4" qualitative leg asserted live.** §1.1 (line ~56): "Fault-tolerance expertise as a specialized 'Level 4' skill (top organizations only) — this qualitative finding **IS in the surviving DORA research and is retained**", repeated at §5.3, §9 ("retained, A") and §10 Ch.4 msg 2. Part 1's fetch found **zero** occurrences of any Level-taxonomy, "top 5%", or "fault-tolerance" in DORA 2024, and the current bibliography entry (line ~571) now says "DORA does not study streaming-vs-batch operational ratios; do not use this source for staffing or incident-rate comparisons." The Level-4 leg is not qualitative-surviving — it is nonexistent-in-source. Strike it wherever the bundle asserts it lives.
2. **Forrester TEI 39/32/29 asserted as surviving.** Executive summary: "the 39% licensing / 32% hardware split is from that same source and **stands**"; §1.3 carries the full 39/32/29 with "Evidence Level A / Confidence High"; §9 and §10 repeat "29% operational — retained, A." The current bibliography (line ~1444): the breakdown "appears in **NEITHER** TEI document (grep-negative in both) and was withdrawn — H-IMPL-01 must not cite a TCO distribution from Forrester TEI." Update all four sites.
3. **Gartner 28% CAGR asserted as retained-A.** §5.2 (full section, with multi-year cost table built on it), §6.2 assumption 1, §9 ("survives the audit"), §10 Ch.6 msg 2. The current bibliography (line ~2971): "the Gartner '28% CAGR' was withdrawn 2026-07-09 — its cited Gartner item is a spending forecast with no volume CAGR." Update all four sites (the qualitative "volumes grow; plan for growth" point can stand unsourced-labeled).
4. Minor: the recalibrated anchor still reads "Huntress **93%** … Level A" — the applied convention elsewhere (fix 20; gap-analysis note) is source-verbatim "more than 90% (~$70K→~$5K/month)" for the blog, with 93% only as derived arithmetic; the bibliography still carries 93% in the entry, so this is a wording-alignment note, not a contradiction. Also: all `📍 MASTER-BIBLIOGRAPHY.md:NNN` line anchors predate the July edits and many have drifted; the bundle's own "Source Truth: all citations reference line numbers" makes this worth one mechanical re-anchor pass.
5. §4.2 "MITRE validated" (behavioral baselining 18-24 months) and §4.3 "validated by Uber, Netflix, Disney+" — unsourced validation attributions in retained text; either point at bibliography entries or soften to "reported."

### 4.2 staffing-budget-calculator.md — the 2026-07-10 folded correction missed at least ten live spots

The banner and the Evidence-Summary strikes are good, but the correction was applied unevenly — the following are **live, un-struck** assertions in the body:

1. ⚑ **MIT Technology Review** (confirmed nonexistent) asserted live 4×: line ~26 ("Specialized Skills Premium: 1.5-2× salary for Level 4 expertise **(MIT Technology Review)**" — in the Key Multipliers box, un-struck, sitting two lines below a struck Ververica/Gartner item); line ~89 ("Evidence: MIT Technology Review (1.5-2× higher training investments), Gartner skills scarcity (Level 4 expertise premium)"); line ~179 ("Training: $40K-60K … - MIT Technology Review 1.5-2× training premium"); line ~473 ("retention critical (MIT Technology Review)").
2. ⚑ **Gartner timeline/staffing family** (same family as the struck "Gartner 5.5 months" at line ~497) asserted live 3×: line ~41 ("Evidence: Gartner security lakehouse implementations average 3-4 FTE core teams"); line ~161 ("Timeline: 2-4 months (**Gartner security lakehouse average: 3 months**)"); line ~470 ("Requires 6-12 month ramp-up (Gartner)").
3. ⚑ **SANS 15-30%** asserted live at line ~476 ("Security-specific compliance - 15-30% longer timelines (SANS Institute)") — the current bibliography (line ~2967) says the 15-30% security-premium figure was **removed in the 2026-06-05 audit (not present in the cited sources)**.
4. ⚑ **"Level 4" taxonomy language** used live and unattributed at lines ~321 and ~344 ("Level 4 skills scarce", "Level 4 streaming expertise") — the taxonomy is the fabricated DORA leg; replace with plain "specialized streaming expertise."
5. **IBM Cost of a Data Breach 2024: "$200K avg difference between <30min and >1hr detection"** (line ~267) — no IBM CODB entry exists in the bibliography, and the framing does not match the report's published detection-lifecycle statistics; NO-PRIMARY, and Calculator 5's break-even math consumes it. Flag prominently or re-derive the break-even from the Altinity-free, IBM-free inputs.
6. **Altinity 70% MTTR / 40% productivity** — correctly marked "not re-verified … treat as unconfirmed" in the Evidence Summary (line ~499) but used without that caveat in Calculator 5's value model (lines ~262-272). Carry the caveat to the point of use, since the break-even conclusions ("7.7 years", "1.3 years") rest on it.

### 4.3 hypothesis-confidence-matrix.md — the 2026-07-10 banner is good but its coverage has five holes

The CHANGELOG for the folded correction says "matrix summary rows re-scored to the current post-overturn 1/5 / 2/5 / 4/5" — that is true of the Executive Summary table only. Found:

1. ⚑⚑ **The "Consolidated Confidence Assessment" table (§ after the first-party rows, lines ~807-846) was never re-scored** and still instructs, live and un-struck: H-IMPL-01 "⭐⭐⭐⭐ **2.5-3× operational costs** — cite convergence"; H-IMPL-02 "⭐⭐⭐⭐⭐ **2.7× staffing, Level 4 skills** — strongest validation, **lead with this**"; H-IMPL-03 "**5.5 months**, 15-30% premium"; H-COST-09 "⭐⭐⭐⭐⭐ **55-80% tiered storage savings** — cite **AWS + Netflix**"; H3-PERFORMANCE-01 "cite Cloudflare + **Shell**"; H-STREAM-01 "**Terabytes of state** … cite LinkedIn + Uber". This is a full row of watch-list legs presented as current book guidance, directly contradicting the banner three screens up. The following "Confidence Distribution Analysis" ("86% of hypotheses have High or Strong confidence") is the same pre-overturn material un-noted. Recommend the same treatment the per-hypothesis sections got: strike-through + dated record note, with a pointer to the banner's adjudicated scores.
2. **H-STREAM-01 has no section record note** although both its legs are gone from the current bibliography: the LinkedIn "terabytes of state with millisecond access" claim was orphaned (part 1) and re-anchored to Samza/VLDB-2017 on 2026-07-09 with an explicit "do not cite a millisecond latency number to this paper" note (bibliography ~704-721), and the Uber sub-second-refresh figures are recorded as withdrawn in cost-reality-reference §4.1's cross-reference. The section still cites "MASTER-BIBLIOGRAPHY.md:502-520 / 681-699" and recommends book language asserting both legs. Needs the dated record-note treatment + re-anchor to Samza's verified figures.
3. ⚑ **H-ARCH-01's body has no record note** while carrying three legs the bibliography has since corrected: "universal vendor support (AWS, Google, Snowflake, Databricks, **Microsoft**)" asserted 4× incl. the Recommended Book Language (the banner itself records Microsoft as the named Delta-first holdout — corrected 2026-07-10, but only the ⛔ journal block covers it); "**300+ contributors across 100+ organizations**" asserted 4× (bibliography ~1750: replaced 2026-07-09 with the GitHub-derived **407 contributors**, organization count dropped as underivable); "SK Telecom (52.7 TB in 3.39s)" in Confidence Drivers (part 1: figures not in the cited recap; re-attributed to the Trino Summit slides with table-size framing 2026-07-10). One section note covering these three would close it.
4. **H3-PERFORMANCE-01's record note is itself slightly wrong**: it says "Cloudflare and the first-party lab legs stand" — the 6M req/sec and 96%<1s legs do stand, but the section also asserts "Cloudflare: **10-12× compression**" and "**5-10× storage efficiency vs Elasticsearch**", both part-1 CLAIM-MISMATCH verdicts (real: ~10× as 600→60 B/row; 12-19× storage in the CH-vs-ES benchmark, with 5-12× being query-speed multipliers). Amend the note.
5. **H-IMPL-03's note ("the SANS security-premium leg stands") contradicts the bibliography** (line ~2967: the 15-30% figure was removed 2026-06-05, not present in the cited sources). The Exec-Summary row repeats "SANS premium leg stands." Both should read: withdrawn pending a real primary; the whole hypothesis then has zero quantitative legs, which the RESCORE adjudication should reflect.

---

## 5. LITERATURE-EXTRACTION-PLAN.md vs current repo reality

The file was partially touched on 2026-07-09 (the security-specific/ stub-removal note at line ~242 is accurate), but its headline self-grades were left un-bannered, and it is a live, six-citer document:

1. **"73% Evidence Level A" asserted 3×** (Final Statistics; Week-3 "73% achieved"; Success Metrics "~55 sources (73%)") — the live, dashboard-computed figure is **41.6% (77/185)** and the repo's own README/CLAUDE.md treat the historical self-grades as the masked number the audit exposed. As a *historical record of the October-2025 completion state* the figures can stay, but per the repo's convention (METHODOLOGY §5.3, the gap analysis, the bundles) they need a dated correction banner so the file stops asserting them as current achievement. 
2. **"All 7 hypotheses validated with verified sources" / "✅ All hypothesis-critical sources verified"** — contradicted by the post-overturn standing (1 strong / 2 high / 4 preliminary; several formerly "critical" sources confirmed nonexistent). Same banner treatment.
3. **Internal count inconsistency**: "6 hypotheses formalized" (Total Work) vs "All 7 hypotheses validated" (Final Statistics) vs "6 new hypotheses (26→32)" (Deliverables) — worth one reconciling sentence in the banner, since CLAUDE.md already flags the validated-hypothesis count as unreconciled.
4. **MASTER-HYPOTHESIS-TRACKER.md does not exist in this repository** (glob-negative repo-wide). If it lives in project1, say so at the reference; NEEDS-LOCAL-CONFIRMATION otherwise.
5. The source-material claims (283 footnotes in the 2024-04-15 best-practices doc; 74 archive manuscripts) reference an archive **external to this repo** — unverifiable in this session; NEEDS-LOCAL-CONFIRMATION only if anyone ever cites them as checked.
6. "16 of 22 URLs validated (73%)" — historical, fine as record under the same banner.

---

## 6. NOT-FETCHED residue (honest list — none of these were marked verified)

| Item | Where | Why left | Suggested closure |
|---|---|---|---|
| aws S3 / Athena / Sentinel pricing pages | appendix A Sources | owner-stamped 2026-07-06; S3 re-derived first-party 2026-07-09 (part 1) | re-stamp at next monthly |
| Flexera 2024 89% multi-cloud | appendix H §H.1.2 | Tier-C-labeled vendor survey, hedged in-text | one fetch of the report landing page |
| W3Techs ~96% | appendix H §H.1.3 | hedged ("by W3Techs count") | one fetch of w3techs.com OS stats |
| Splunk ES "~1,700 correlation rules" | appendix C Pattern 4 | no primary cited; suspect ESCU-vs-ES conflation | cite research.splunk.com detection count or ES docs, and say which product the number belongs to |
| Apple / Baris Aydın, Subsurface 2023 | appendix C Production Validation | no bibliography entry | locate the Subsurface talk page; add entry or drop the named attribution |
| Iceberg V4 = open milestone #58; 1.11.0 File Format API | appendices H+L | part-2 verified 1.11.0 contents; milestone not re-checked | one GitHub milestone check |
| Vortex (LF project, `vortex-data`, plugin-still-open) | appendix C | hedged in-text | one fetch |
| Tidal Cyber (Mar 2026) + Atkinson/SpecterOps | appendix M | tier-labeled w/ vendor-incentive flag already | optional |
| OWASP AIVSS v0.8 / AIUC-1 / MS Agent 365 / PydanticAI | appendix L | all carry in-text confirm-before-citing hedges | optional |
| arXiv:2604.03070 figures (17,022 / 3.1%) | appendix L | PDF unreadable to fetcher | open the PDF locally |
| PR #294 page itself | appendices D+H | repo archived ✓ verified; PR page not individually fetched | one local click |
| github.com/tabular-io/iceberg-rest-image | appendix D | not fetched | one fetch (Tabular→Databricks migration risk) |

---

## 7. Proposed fix list (recommendation-only; one line each; local session applies + CHANGELOG entry)

1. appendix-b-anti-patterns.md AP#9 (~lines 599, 621-624) → remove "Cisco acquires Cribl" both places; reframe the case as explicit hypothetical or fully anonymized ("a major pipeline vendor's acquisition tripled list price"); do not attach real company names to a fictitious acquisition.
2. appendix-c-reference-architectures.md (~line 873) + appendix-d (~line 373) → "78× to 9,000× (vendor literature)" → correct units + attribution per the SDW essay (Snowflake ~78% improvement; single-developer PostgreSQL study 350×-9,000×; practitioner Splunk DMA 270×).
3. appendix-c (~line 954) → "51-270× … docs.splunk.com" → re-attribute 270× to the unsafehex.com practitioner write-up; locate or drop "51×".
4. appendix-c (~line 59) → Netflix/Muino "late 2024" → July 2025 meetup talk (blog 2025-10-23), per bibliography correction.
5. appendix-c (~line 689) → "~1,700 correlation rules" → cite a primary and name the product (ES bundled correlation searches vs ESCU detections), or soften to "Splunk ships an extensive pre-built detection library (Tier C)".
6. appendix-c Production Validation → add a bibliography entry for the Apple/Aydın Subsurface 2023 talk or drop the named attribution.
7. appendix-d (~line 422) → "Glacier ($0.001/GB/month)" → "S3 Glacier Deep Archive (~$0.001/GB/month)" for consistency with A.6's Glacier-Flexible rate.
8. appendix-h §H.3.1 → attach the actual vendor case-study citation for the 2 PB/day deployment (or mark explicitly "no primary on file — unciteable").
9. appendix-a Step-2 anchor block → add the GLA PCD 1331 URL as the Met Police citation; reconcile "2024 deal" vs the PCD funding year; confirm the 10%-discount clause against the PCD text.
10. appendix-k K.3 Evidence line → drop/soften "Gartner (6-8 FTEs…)" and change "Denodo public enterprise pricing (validated $1.2M/year…)" to "author-modeled; Denodo list pricing not publicly verified" — or add real primaries (mirror the K.2 fix).
11. staffing-budget-calculator.md → strike the four live MIT-TR attributions (~26, 89, 179, 473), the three live Gartner attributions (~41, 161, 470), and the SANS 15-30% (~476, removed from bibliography 2026-06-05); replace "Level 4" language (~26, 89, 321, 344) with "specialized streaming expertise."
12. staffing-budget-calculator.md (~267, 262-272) → flag the IBM CODB "$200K" figure NO-PRIMARY and carry the Altinity "unconfirmed" caveat into Calculator 5 at point of use (the break-even headlines depend on both).
13. hypothesis-confidence-matrix.md Consolidated Confidence Assessment + Confidence Distribution (~807-846) → strike-through + dated record note mirroring the per-hypothesis treatment; point at the banner's adjudicated scores.
14. hypothesis-confidence-matrix.md H-STREAM-01 → add section record note (LinkedIn leg re-anchored to Samza, no ms-latency claim; Uber refresh figures withdrawn); replace the Recommended Book Language.
15. hypothesis-confidence-matrix.md H-ARCH-01 → add section record note covering universal-support-incl-Microsoft (Delta-first holdout), 300+/100+ → 407 contributors (org count underivable), SK Telecom figures → Trino Summit re-attribution.
16. hypothesis-confidence-matrix.md H3-PERFORMANCE-01 record note → amend "Cloudflare legs stand" to except the 10-12× compression and 5-10×-vs-ES legs (part-1 mismatches; real figures ~10× and 12-19×).
17. hypothesis-confidence-matrix.md H-IMPL-03 note + Exec-Summary row → "SANS premium leg stands" → withdrawn per bibliography :2967; reflect zero surviving quantitative legs in the RESCORE adjudication.
18. cost-reality-reference.md → strike the live DORA-Level-4-retained claims (~56, §5.3, §9, §10); update TEI 39/32/29 "stands" → withdrawn-in-neither-document (4 sites); update Gartner 28% CAGR "retained" → withdrawn 2026-07-09 (4 sites); align Huntress wording to source-verbatim "more than 90%"; optional mechanical re-anchor of the 📍 line references.
19. LITERATURE-EXTRACTION-PLAN.md → add a dated correction banner (historical-record framing for the 73%-Level-A and all-7-validated claims; note the 6-vs-7 count inconsistency; annotate the MASTER-HYPOTHESIS-TRACKER.md pointer as external-to-repo).
20. CHANGELOG.md → entry when this fix pass lands (citation-stability rule); locate/decide placement of VERIFICATION-SWEEP-PART2-2026-07-10-cowork.md in the working tree (NEEDS-LOCAL-CONFIRMATION).

---

## 8. Git handoff

- **Branch**: create `litreview-verify3-2026-07-10` from the current mainline — **never commit to main**.
- **Contents**: this report only (`VERIFICATION-SWEEP-PART3-2026-07-10-cowork.md`). Nothing else was created or modified by this session.
- **Local pre-commit verification** (this session made zero git observations; all of the following is the local session's to confirm): `git status` shows only this file as new; confirm no other tracked file changed; confirm the part-2 report's whereabouts (branch `litreview-verify2-2026-07-10`?) and whether it should be merged to root alongside this one.
- **Fix pass**: apply §7 items on a separate branch after owner review, re-verifying each edit against the primary named in this report at time of application (several targets — bundle line numbers especially — may drift); carry a CHANGELOG entry per the citation-stability rule.
- **Suggested commit message**: `📊 Verification sweep part 3 (cowork): appendices a-d/h/k-m + extraction plan + bundle banners — 1 contradicted, 4 mismatches, ~20 banner-gap items; recommendation-only`.

---

*Method note: repo files were read in full (no sampling); every VERIFIED verdict above rests on a fetch performed 2026-07-10 in this session (GitHub releases pages, d3fend.mitre.org/version, arXiv abstract pages, the G-Cloud 14 PDF, the GLA PCD search record, the SDW essay, UB news release, vendor advisories via search). Web content was treated as data throughout; nothing in any fetched page was executed or followed as instruction.*
