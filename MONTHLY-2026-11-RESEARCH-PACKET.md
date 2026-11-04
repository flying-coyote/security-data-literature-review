---
type: review
title: "Monthly Update 2026-11 — Research Packet (thin: egress-limited run; one verified refresh, leads only)"
created: 2026-11-04
tags: [monthly-update, freshness, new-sources, adjudication, evidence-tier]
---

# Monthly Update 2026-11 — Research Packet

> **Read this first.** This packet was prepared by an unattended scheduled run in a cloud container whose
> network allowlist blocked most primary hosts (`iceberg.apache.org`, `www.usenix.org`, `api.crossref.org`,
> `csrc.nist.gov` all failed DNS; only `github.com` fetched). Under the repo rule "never invent metadata,"
> **only one item below is primary-verified**. Everything else is a search-result lead that needs a
> networked re-check in the supervised session. Nothing in `MASTER-BIBLIOGRAPHY.md` or any other existing
> file was edited.

## §1 — Health summary (`scripts/weekly_health_check.py`, run 2026-11-04; needed `/usr/bin/python3`, `python3` lacked `requests`)

| Check | Result |
|-------|--------|
| Status | **WARNING** (6 pass / 3 warn / 0 fail) |
| Git | clean; last commit 1 day ago |
| Bibliography | 231 `####` blocks; 206 URLs sampled |
| Broken links | **0 confirmed.** 9 of 10 sampled-and-unreachable links were `ProxyError` → **inconclusive, not counted as broken** (see list below) |
| Freshness | 93 / 226 sources > 12 months old (>20% → "update evidence sources") |
| Hypotheses | 9 assessed (1 strong / 2 high / 2 moderate / 4 preliminary) |
| Publication | Missing sections: Abstract, Discussion; main text 14,879 words (target 10,000–15,000) |
| Quarterly | Not an update month; no 2026-Q4 update exists yet |
| Vendor DB | present, 71 vendors |
| **Evidence Level A** | **17.0%** (39 A / 156 B / 34 C of 229 tiered) — far below the floor |

Inconclusive links to re-check from a networked host: doi.org/10.1108/ijwis-03-2021-0023;
stratos.seas.harvard.edu (Kester et al.); clickhouse.com/docs (compression-codecs and query-optimization
pages); doi.org/10.1109/icin69025.2026.11481838; doi.org/10.52436/1.jutif.2023.4.4.649; fortinet.com
newsroom press release; doi.org/10.1109/compsac61105.2024.00355; technicspub.com/software_wasteland.

Tooling note: the health check's "Outdated Evidence" list prints only `Year 20XX` with no entry names, so
it cannot drive source selection by itself. I picked candidates by reading old-dated, hypothesis-linked
entries in the bibliography. Worth fixing the script to print titles.

## §2 — Proposed refreshes

### 2.1 VERIFIED — OCSF Schema v1.8.0 → v1.9.0 (bibliography entry ~line 4427)
- **Old:** "OCSF Schema v1.8.0" entry, which states v1.8.0 "is the latest release" (Tier A, official standard).
- **Proposed:** add/repoint to **v1.9.0**, read on the primary
  <https://github.com/ocsf/ocsf-schema/releases>. Headlines listed there: new `user_management`,
  `role_management`, `clipboard_activity`, `device_power_state_activity` event classes; a `record_integrity`
  profile (cryptographic attestation); a `delegation` object for the `ai_operation` profile; an `ai_agent`
  object. Cadence on the page: 1.5.0 28 Apr 2025, 1.6.0 1 Aug 2025, 1.7.0 14 Nov 2025, 1.8.0 18 Mar 2026
  (changelog header says Mar 16, tag says Mar 18 — the existing entry already uses 18 Mar).
- **Caveat:** the release page shows v1.9.0 as "03 Aug" with the year taken from the changelog (2026); the
  fetch tool paraphrased the page, so confirm the exact tag date and year in the browser before writing it.
  The 1.8.0 entry's "six-schemas crosswalk corpus targets 1.8.0" claim will also need a look.
- **Tier:** A (official schema standard), unchanged — consistent with the existing entry.
- **Why it matters:** the `ai_operation`/`ai_agent`/`delegation` additions are directly relevant to the
  AI-agent hypotheses (RQ12/RQ14) and to Appendix F.

### 2.2 NOT VERIFIED — other candidates I could not check (no change proposed)
- **Apache Iceberg v3 spec entry (~line 4354):** web search (Dremio, Starburst, AWS S3 docs dated
  2026-01-08) says v3 shipped mid-2025 with deletion vectors, row lineage, default values, new types, and
  that AWS EMR Spark 7.12+/Glue support it. The Apache primary (`iceberg.apache.org`) was blocked, so I
  cannot confirm the release version/date. The existing entry may already be fine; just re-check the
  "Iceberg V3/1.11.0" wording against the Apache release notes.
- **LHBench (CIDR 2023, ~line 856):** searched for a newer peer-reviewed cross-format benchmark and found
  **none** — only vendor/practitioner blogs (iceberglakehouse.com, RisingWave, Synvert). LHBench remains
  the best Level-A anchor; no replacement proposed. Do not substitute the blog benchmarks (Tier C).
- **Samza VLDB 2017, Kester SIGMOD 2017, Cloudera TEI 2021 (C):** no newer primary searched this run
  (time spent on the blocked-host failures). Not proposed.

## §3 — Proposed new sources (all UNVERIFIED leads; none ready to catalogue)

None of these could be opened on a primary page, so no title/author/date metadata is asserted beyond what
appeared in search results.

1. **Bilot et al., "Sometimes Simpler is Better: SOTA Provenance-Based IDS", USENIX Security 2025** — already
   a *lead* in the July packet §4 (peer-reviewed, camera-ready confirmed then). Still the best clean Level-A
   candidate; I could not reach usenix.org to re-read the abstract. **Proposed tier A** once the anchor claim
   is written against the paper's own text. Not found in the bibliography (grep for "Bilot"/"provenance-based" empty).
2. **A VLDB 2025 paper, DOI 10.14778/3742728.3742733** — surfaced via a Crossref URL in search results while I
   looked for ClickHouse/log-storage work; its title and content were **not retrievable** (crossref blocked).
   Do not catalogue until opened. If it is the ClickHouse industrial paper cited by the THESAI SIEM paper,
   it would be a peer-reviewed A for the columnar-store-as-SIEM-backend thesis (H3-PERFORMANCE-01) — this is
   a guess, flagged as such.
3. **LogCloud (object-storage log management, 2025 database venue)** — appeared in search as a peer-reviewed
   system targeting compressed-storage-vs-search tradeoff on TB-scale logs. Venue, authors and date not
   verified. Potentially A for RQ11/RQ13 if confirmed.

Also noted, not proposed: NIST SP 800-92 Rev. 1 ("Cybersecurity Log Management Planning Guide") — search
indicates it is still an **initial public draft (Oct 2023)** with no final found; grep shows no 800-92 entry
in the bibliography. If the owner wants a government-standard Level-A log-management anchor, the draft is
citable only as a draft (tier call: A as an official NIST publication, or B while unfinalized).
Needs a check on csrc.nist.gov for current status.

## §4 — Open questions for Jeremy
1. **Network allowlist:** should the scheduled environment allow `iceberg.apache.org`, `www.usenix.org`,
   `api.crossref.org`, `csrc.nist.gov` (and arxiv.org / vldb.org / dl.acm.org)? Without them this packet
   cannot verify Level-A primaries, which is exactly the class the 17.0% floor needs.
2. Fix `weekly_health_check.py` so the outdated list prints entry titles (and ideally ranks by hypothesis link)?
3. Do you want a separate OCSF 1.9.0 entry or an in-place update of the 1.8.0 entry (version-in-title convention vs. citation stability)?
4. NIST SP 800-92r1 draft: acceptable as Tier A, or hold until final?
5. July leads still open (Bilot, CSTS arXiv:2603.23459, OWASP agentic 2.0) — carry them into this session's primary-verification pass.

## §5 — Counts
Verified refreshes: **1** (of ≤5). Unverified refresh candidates: 2 checked, not confirmable. Proposed new
sources: **3 leads, 0 primary-verified.** Level-A candidates among them: 3 (all pending verification).
