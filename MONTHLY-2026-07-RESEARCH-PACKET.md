---
type: review
title: "Monthly Update 2026-07 — Research Packet (freshness + new-source candidates, for adjudication)"
created: 2026-07-09
tags: [monthly-update, freshness, new-sources, adjudication, evidence-tier]
---

# Monthly Update 2026-07 — Research Packet

**What this is**: the output of the July monthly sweep's research phase, run as a multi-agent workflow
(11 freshness checks + a six-angle new-source discovery, then an adversarial verification pass that
re-fetched every candidate's primary and confirmed the specific claim before anything was called
catalog-ready). Nothing here was catalogued without a primary-confirmed claim, and nothing tier-changing,
retitling, or source-adding was applied to `MASTER-BIBLIOGRAPHY.md` on my own — that's your adjudication,
consistent with how this corpus is maintained. The only bibliography edits already applied are the
objective metadata corrections in §1 (they don't move any tier count).

**Method note / honesty**: verifiers were told to default to skeptical and to REJECT a real-but-unconfirmable
source rather than admit an unverified figure. 0 candidates were rejected outright; 12 came back
catalog-ready (11 unique — one was found twice across angles), 4 as partial leads. Vendor-published
case studies are flagged as such even where the numbers are specific, because "specific and dated" is not
the same as "independent."

---

## §1 — Applied already (objective metadata corrections, no tier change)

These were provably-wrong dates or a stale freshness note on existing entries; each was verified at the
live primary before I changed it. Tier counts are untouched (still 74 A / 85 B / 16 C across 175 tiered
sources / 176 blocks = 42.3% Level-A).

| Entry | Was | Now (verified at primary) |
|-------|-----|---------------------------|
| ClickHouse Log Analytics — Cloudflare | Date "2024" | **2022-09-02** (byline read twice) |
| ClickHouse — GitLab Sub-Second Analytics | Date "2024" | **2025** (byline Oct 21, 2025) |
| ClickHouse vs Snowflake Benchmarks | Date "2024" | **2023** (published Sept 6, 2023) |
| Cloudera Impala + Iceberg Performance | Date "2024" | **2022-02-22** (page dated Feb 22, 2022) |
| Kafka to Iceberg: 9 Solutions (Streambased) | Date "October 2024" | **2025-10-20** |
| ClickHouse vs Elasticsearch — Storage Efficiency | note "publication date pre-2025" | **page updated 2026-03-03** |

The recurring pattern: the 2025-10-15 bulk-generation stamped "2024" on a lot of entries whose primaries are
actually 2022–2023 or 2025. Worth a wider date-audit pass in a future month — the freshness inventory can be
re-run per-source rather than by the health check's year-token proxy.

---

## §2 — Freshness changes HELD for your call (tier / title / claim judgment)

Each is verified at primary; I didn't apply them because each involves a re-tier, a retitle, a citation
split, or removing a headline number from published prose.

- **Netflix "Security Observability — Isolation-First Architecture with Polaris"** — the title is a
  misattribution: "Apache Polaris" appears in the ClickHouse blog only as one Iceberg catalog *option*, and
  the blog never says "isolation-first." Verified figures to fold in: 5 PB/day, 10.6M events/sec avg (12.5M
  peak), ~5 KB/event, 500–1,000 QPS, 20s searchability vs a 5-min SLA, 40K+ microservices, ClickHouse hot
  tier + Iceberg cold tier. Proposed retitle: "How Netflix optimized its petabyte-scale logging system with
  ClickHouse" (Daniel Muino, ClickHouse meetup, July 2025; blog dated Oct 23, 2025). Keep B (vendor case
  study; no first-party Netflix primary found).
- **ClickHouse Log Analytics — Cloudflare** (claim, not date) — drop the "12×": there is no 12× figure on
  the page. The real figure is "~10× storage reduction migrating Elasticsearch → ClickHouse (600 → 60
  bytes/row, LZ4)" — an ES→CH migration figure (columnar + schema change), not a pure columnar-compression
  ratio. Soften "security-relevant workload" → "error/troubleshooting request-log analytics
  (security-adjacent)." Optional corroborator (no compression figures): ClickHouse-hosted Cloudflare "Trouble
  will find you" (2026-02-18) — 96T events/hour, 1.61 quadrillion/day query scale.
- **ClickHouse vs Elasticsearch — Storage Efficiency** (claim) — page's own 2026 headline is now "12–19×
  less storage" on a synthetic billion-row `count(*)` benchmark; keep the ~5× realistic-OTel figure and note
  the range. On-domain corroborator: ClickHouse "Do you still need Elasticsearch for log analytics?"
  (2026-04-23) — 4.95× less storage / 16.29× column compression on OpenTelemetry logs to 50B rows.
- **ClickHouse vs Snowflake** (tier) — all three posts are ClickHouse-run benchmarks of a competitor and
  **Snowflake has publicly contested** the 2026 CostBench/write-side numbers. B is defensible only with the
  vendor-bias + contested-by-Snowflake caveat stated; there's a real case to re-tier **B→C**. Newer anchors
  if you keep it: CostBench end-to-end (2026-06-23), write-side (2026-05-06).
- **Cloudera Impala + Iceberg** (tier) — the "10×" is a vendor-relayed single unnamed-customer anecdote, not
  a Cloudera-run reproducible benchmark, so "A (Production benchmarks)" overstates it → **re-tier A→B**.
  Also: `RESEARCH-JOURNAL.md` line ~126 ("redirect; '10x over Hive' gone (also DEAD)") is stale and
  contradicts the correct 2026-06-05 re-source note — annotate as superseded.
- **Cloudera TEI (Forrester 2024)** (citation split) — the catalogued URL is the *Private Cloud / On-Prem*
  study (supports the 35% + 254% ROI / $17.8M figures), and does **not** contain the 194% ROI / $35M figures
  — those are the *Public Cloud* study
  (`cloudera.com/campaign/forrester-tei-report-...-public-cloud.html`). Split so each figure sits under the
  URL that supports it. Keep May-2024 date, Tier A. No 2025/2026 Cloudera TEI update exists.
- **Kai Waehner "Top Trends 2025"** (refresh to next-year edition) — the 2026 edition is live (same author,
  same annual series, 2025-12-10): market consolidation, diskless Kafka + Iceberg storage, real-time
  analytics in the streaming layer, RPO=0 SLAs, sovereign-cloud, agentic AI with real-time context. Repoint
  URL/date/title to the 2026 edition (or keep the 2025 post as a superseded prior-year anchor). Stays B
  (single-author, Confluent-affiliated — keep the viewpoint framing).
- **"Streaming vs Batch Cost Differential" (phantom)** — **retire**. The URL is an unresolved placeholder,
  no CloudZero primary supports it, and every specific multiplier once attached to this claim has already
  been withdrawn; `APPENDICES.md` D.3 already dropped the CloudZero line. It's a dangling ghost. If you keep
  the qualitative "streaming carries a cost premium" point, anchor it only to the retained Cloudera/Forrester
  TEI entry and add that 2025–2026 sources argue the premium is *conditional* on utilization/scale, not a
  fixed differential. (Retiring it moves the count to 174 tiered / 176 blocks / 2 rejection stubs → 74/174 =
  42.5% — trivial, but re-sync the surfaces if you do it.)

---

## §3 — New sources, catalog-ready (primary-verified). Recommend catalguing 2–3; the rest are optional.

Grouped by honest tier. Every claim below was read on the fetched primary by the verification pass.

### Tier A (strongest — recommend both)
- **Ursa: A Lakehouse-Native Data Streaming Engine for Kafka** — StreamNative, **PVLDB Vol. 18(12):5184-5196,
  2025**, VLDB 2025 **Best Industry Paper** (doi:10.14778/3750601.3750636).
  <https://www.vldb.org/pvldb/vol18/p5184-guo.pdf> — Kafka-compatible engine that writes topics directly to
  Iceberg/Delta on object storage (leaderless, no broker disks), ~5% of the cost point vs broker-disk
  architectures. **H-ARCH**: streaming and lakehouse storage converging into one substrate — removes the
  connector hop between the detection pipeline and the security data lake. *Peer-reviewed → clean A.*
- **How Exabeam uses ClickHouse for scalable, searchable security analytics** — ClickHouse case study of
  Exabeam (SIEM/UEBA vendor), Sep 11, 2025.
  <https://clickhouse.com/blog/exabeam-clickhouse-security-analytics> — 10 global regions, **1.2M events/sec
  per region** at peak, ~**17.5× compression** (3.5 PB → 200 TiB), sub-second queries. **H3-PERFORMANCE-01 /
  RQ11**: an incumbent SIEM vendor running its own backend on ClickHouse — evidence for the columnar-store-
  as-SIEM-backend thesis from the incumbent side. *Note: ClickHouse-published → if you hold the line that
  vendor-published case studies are B, tier this B; the verifier put it at A on production-quantitative
  grounds. Your call — flag the vendor bias either way.*

### Tier B (measured or credible-practitioner)
- **OpenSec: Measuring IR Agent Calibration Under Adversarial Evidence** — Jarrod Barnes (independent),
  arXiv:2601.21083 (2026). <https://arxiv.org/abs/2601.21083> — four frontier models over-contain: GPT-5.2
  executes containment in 100% of episodes at 82.5% FP rate, acting before gathering evidence. **RQ14**:
  exactly the *skeptical, measured* counter-evidence to autonomous-SOC hype the RQ needs. *Recommend this as
  the third add if you want a measured RQ14 anchor — it cuts against the vendor ROI grain.*
- **Randomized Controlled Trials for a Phishing Triage Agent** — James Bono (Microsoft), arXiv:2511.13860
  (2025). <https://arxiv.org/abs/2511.13860> — first RCT (with control group) on MS Security Copilot Phishing
  Triage Agent: measured analyst throughput/accuracy gains. **RQ12**. *Rigorous design but vendor-authored on
  their own product → B + bias flag; not A (preprint, not independently replicated).*
- **CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage** — GMU + Fluency Security,
  arXiv:2510.00311 (2025). <https://arxiv.org/abs/2510.00311> — Table 4 FP-reduction deltas on real traces,
  released dataset. **RQ12**. *Partial independence (vendor co-author) → B.*
- **Go jump in a lake: Measuring the data-lake effect on your SIEM** — Red Canary, 2026.
  <https://redcanary.com/blog/security-operations/data-lake-siem/> — decomposes the SIEM bill: 105 TB
  OpenSearch cluster ≈ $24,688/mo, **65% of it compute**. **H-COST-09 / RQ13**: rare practitioner source that
  splits compute vs storage rather than quoting a headline %. *Illustrative figures → B.*
- **Delivering Significant Cost Savings with Cribl (RiverSafe case study)** — RiverSafe (SI), 2025.
  <https://riversafe.co.uk/resources/case-studies/delivering-significant-cost-savings-and-increased-visibility-with-cribl/>
  — Cribl Stream in front of Splunk: 750 → 450 GB/day (**~40% ingest cut**), avoids £120–150K/yr licence
  growth, no detection-coverage loss. **H-COST-09 / RQ13**. *Measured before/after → B.*
- **Icebergs in the Data Lake** — Jack Naglieri (Panther founder), Detection at Scale, Jan 6, 2025.
  <https://www.detectionatscale.com/p/icebergs-in-the-data-lake> — practitioner articulation of *why* Iceberg
  (schema evolution for verbose security logs, hidden partitioning, engine interop) is becoming the neutral
  substrate. **H-ARCH-01 / RQ11**: the mechanism behind the dominance claim. *Named practitioner essay → B.*
- **How Artemis Security runs 69× faster detection queries with ClickHouse Cloud** — ClickHouse case study,
  Jul 1, 2026. <https://clickhouse.com/blog/artemis-security-real-time-threat-detection> — query coalescing
  collapses the one-query-per-rule SIEM pattern: 2.5s vs 173s coalesced, 46× less CPU, 100× less memory I/O.
  **H3-PERFORMANCE-01 / RQ11**. *Vendor-published → B + bias flag.*

### Tier C (vendor marketing — catalogue only with an explicit bias flag)
- **Databricks Announces Lakewatch: New, Agentic SIEM** — Databricks, Mar 24, 2026.
  <https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem> — a major lakehouse
  vendor entering the SIEM market (private preview; Adobe, Dropbox named). **RQ11** competitive-landscape data
  point. *"up to 80%" cost / "100%" retention are hedged marketing, private preview → C.*
- **How Vensure Cut SIEM Costs by 83% Using Realm.Security** — Realm.Security "SIEM Pricing 2026" page, Apr
  23, 2026. <https://realm.security/siem-pricing-2026-leading-siem-providers-compared/> — single self-reported
  customer metric (83% firewall-log reduction upstream of Sumo Logic), also covered by Dark Reading.
  **H-COST-09 / RQ13**. *Self-published, no methodology → C.*

---

## §4 — Leads (real + on-topic, but NOT catalog-ready — need your eye)

- **Sometimes Simpler is Better: SOTA Provenance-Based IDS** — Bilot et al., **USENIX Security 2025**
  (peer-reviewed, camera-ready confirmed). <https://www.usenix.org/conference/usenixsecurity25/presentation/bilot>
  — top-tier; flagged a lead only on claim-phrasing, not credibility. *Probably a clean A add once the anchor
  claim is written to what the paper actually shows — worth a look.*
- **Matryoshka: Semantic-Aware Parsing for Security Logs** — arXiv:2506.17512. Likely **overlaps the existing
  "Matryoshka: Semantic-Aware Log Parsing" entry** — check for dup before adding.
- **CSTS: A Canonical Security Telemetry Substrate for AI-Native Cyber Detection** — arXiv:2603.23459.
  On-topic (RQ16-adjacent) but post-cutoff framing; partial claim confirmation.
- **OWASP State of Agentic AI Security and Governance 2.0** —
  <https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/> — the specific figure as
  phrased is **contradicted at the primary** on a falsifiable numeric detail; re-phrase to the real number
  before any use.

---

## Recommendation

If you want the "2–3 typical" monthly add: **Ursa (A)** and **Exabeam (A/B — your tier call)**, plus
**OpenSec (B)** as a measured RQ14 counterweight. The RiverSafe + Red Canary pair is the best *measured*
pipeline-economics evidence for RQ13 if you want a fourth. Hold the Tier-C vendor pieces unless you want the
competitive-landscape note on Databricks entering the SIEM market.
