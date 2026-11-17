---
type: evidence
title: "Bibliography verification sweep (2026-11-17)"
created: 2026-11-17
tags: [bibliography-validation, number-fidelity, citation-existence, literature-review]
---

# Bibliography verification sweep (2026-11-17)

This folder records a check of every one of the 273 `#### ` entries in [`MASTER-BIBLIOGRAPHY.md`](../../MASTER-BIBLIOGRAPHY.md), asking two questions of each: does the cited work exist at the identifier the entry gives, and does each number the entry quotes appear in that source. The per-entry record is [`ledger.json`](ledger.json), one object per entry with the identifiers checked, the HTTP result for each URL, an existence verdict, and a verdict for every quoted number together with the URL and the sentence it was found in. Line numbers in the ledger are the bibliography's line numbers after this sweep's own edits.

## Verdicts

| Number verdict | Count | What it means |
|---|--:|---|
| `verified-at-primary`, re-checked 2026-11-17 | 307 | Found at the cited primary on the day; the ledger gives the URL and the surrounding sentence |
| `verified-at-primary`, carried | 77 | Not re-read on the day; carried from an earlier check at the primary that the entry records (see `basis`) |
| `unverifiable-paywall` | 56 | The source exists but its text could not be read: a paywall, a registration form, a landing page that carries no report text, or HTTP 403/406/429 to an automated reader |
| `not-in-source` | 12 | The cited page's text was read and the number was not in it |
| `unverifiable-no-primary` | 4 | The entry names no fetchable primary for the number |
| `dead-link` | 0 | No quoted number rests on a dead URL (dead identifiers are counted separately below) |
| `n/a-correction-note` | 32 | The number appears only inside a dated note recording a withdrawn figure, so it is not a live claim |
| **Total numbers recorded** | **488** | across 132 entries that state at least one number |

Of the 384 verified numbers, 286 were matched automatically against the fetched text of the cited page on 2026-11-17, 21 were checked by hand the same day (derived ratios, numbers the extractor misread, the composite entries, and one first-party lab figure), and 77 are carried from an earlier check that the entry itself records, such as a verbatim quote taken at admission, a "numbers confirmed in source" provenance line, or a page-render check of percentages printed inside a figure image, where the publisher page now blocks an automated reader or the number is not in the text layer. The ledger's `basis` field says which of the three applies to each number, so a reader who wants only the numbers re-read on 2026-11-17 can filter on it.

Every number with a verdict other than `verified-at-primary` or `n/a-correction-note` is visibly marked in the bibliography, either removed with a dated note (`removed_in_file` in the ledger) or covered by an *Unverified 2026-11-17* label or entry-level note giving the reason (`labelled_unverified_in_file`), and the entry's Validation Status line ends with a count of its unconfirmed figures. The one exception is the documented "Declined — EITT Academy" stub, whose two figures are recorded only as the reason the source was declined. A further 24 items, some grouping several figures, were removed or labelled in ten entries whose sources could not support them (the retired December 2025 benchmark timings, a replica-count line on the Cloudflare entry that neither cited page carries, and the composite and LinkedIn-only entries that named no primary), and these are listed per entry under `removed_or_labelled_2026_11_17`.

| Entry existence | Count |
|---|--:|
| Exists (DOI resolves at Crossref, or the URL returned the page) | 253 |
| Unconfirmed (the URL blocks an automated reader, or returned 404 while still being search-indexed) | 11 |
| No fetchable primary (LinkedIn discussion, a personal communication, or a composite with no named source) | 5 |
| Documented stub, no primary by design | 2 |
| Paywalled analyst document with no public URL | 1 |
| Not fetched by policy (a linkedin.com URL) | 1 |

All 60 DOIs in the file resolved at Crossref with a title matching the entry.

| Dead or unconfirmed identifier | Count |
|---|--:|
| Dead: a cited URL that returns 404 with no archived copy (the dataversity.net Alt URL on the Data-Centric Revolution entry, marked dead in the file; the entry's primary URL is live) | 1 |
| Unconfirmed: 404 to an automated reader while still search-indexed (Navan case study, marked in the file) | 1 |

Two further 404s in the ledger's `identifier_checks` are extraction artefacts, URLs captured with a trailing semicolon (`ducklake.select/;` and the Apache Ossie incubator page), and both pages return 200 without it.

## How the check ran

A script parsed each entry, collected every DOI, arXiv ID and URL in it, and fetched them with a generic browser user agent: Crossref for each DOI's record and abstract, OpenAlex for abstracts the publisher page would not serve, and the cited pages themselves, with PDFs converted to text. Numbers were extracted from each entry's Key Findings and Notes, skipping sentences that record a withdrawal or correction, and each was searched for in the fetched text under its common spellings (`10x`, `10×`, `10 times`, `10-fold`; `5 PB`, `5 petabytes`). The script never fetched linkedin.com and did not try to get around a site that refused an automated reader, so pages behind a 403 are recorded as unverifiable rather than read another way. Version currency was checked against each project's own release record (GitHub releases, the project's downloads page or the spec page) on the same day, and the dated currency notes in the bibliography cite those pages.

## Limits a reader should know

- An automated match shows the number is present on the page near the entry's wording; it does not prove the entry describes the number's meaning correctly. A spot-check of 20 random automated matches found one where the number belonged to a different comparison on the same page (Prosci's 15%), and that one is corrected to `not-in-source`.
- Numbers outside Key Findings and Notes, such as a figure stated in an entry's Relevance list, were not extracted.
- `not-in-source` here means the figure was not in the text that could be fetched, and is used only where that text was the source's own content. Where the fetch returned a landing page, a product page or a page shell, the verdict is `unverifiable-paywall` instead, and the bibliography label says the figure is not on the landing page. For pages that render part of their content client-side, a figure may exist and still be recorded as not found, which is why the bibliography labels it *unverified* rather than deleting it.
- The sweep ran as one scripted pass with manual review of the priority entries, so the composite and no-identifier entries got a hand check and the remaining entries got the automated check plus the 20-match spot-check.

## Changes it made to the bibliography

The bibliography's own entries carry each change as a dated note, and [RESEARCH-JOURNAL.md](../../RESEARCH-JOURNAL.md) has one row per changed verdict under the 2026-11-17 heading. Tier changes, withdrawals and splits the sweep recommends were not applied, because each would change the gated corpus counts; they are listed for an owner decision with the quality-pass notes.
