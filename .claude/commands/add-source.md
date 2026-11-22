---
type: operating-doc
title: "Add Source to Bibliography — Evidence Tier Procedure"
created: 2026-01-02
updated: 2026-11-17
tags: [literature-review, bibliography, evidence-tiers, source-classification, citation-format]
---

# Add Source to Bibliography

Add a new research source to the literature review with proper evidence classification.

## Source Information Required

Please provide:
1. **Title**: Full title of the source
2. **Author(s)**: Complete author list
3. **Publication Date**: When published
4. **Venue**: Journal, conference, blog, vendor, etc.
5. **URL/DOI**: Permanent link to source
6. **Type**: Journal / Conference / Blog / Industry Report / Vendor / Production Case Study

## Evidence Tier Classification

I will classify the source using the Evidence Tier system:

METHODOLOGY §3.1 is the canonical definition (corrected 2026-08-19); in short:

- **A**: peer-reviewed research at a confirmed venue (checked at the publisher or DOI record, not inferred), standards-body documents (NIST, ISO/IEC, IETF RFC, W3C, OASIS), formal open-standard specifications (the Iceberg table spec, the OCSF schema spec), and the MITRE D3FEND and ATLAS frameworks, which are authoritative on structure and silent on efficacy
- **B**: production deployments and case studies with real numbers, first-party lab benchmarks, vendor engineering blogs from the operating team, conference talks, trade books, analyst reports, expert interviews, government advisories (as distinct from standards), official project documentation, and preprints, theses and workshop papers whose venue is not confirmed
- **C**: vendor material with no production measurement behind it, and vendor-authored pieces quoting a practitioner; bias flagged, and never carrying a hypothesis on its own
- **D**: marketing, unverified claims and speculation; not catalogued

## Process

1. **Classify** the source using criteria above
2. **Check** MASTER-BIBLIOGRAPHY.md for duplicates
3. **Add** a `#### ` entry block in the format of the most recent blocks in MASTER-BIBLIOGRAPHY.md (the count gate counts only `#### ` blocks, so an entry in any other shape is invisible to it):
   ```markdown
   #### [Title] ([Author], [Venue], [Year])

   **Authors**: [list]
   **Date**: [publication date; date read]
   **URL**: [link, or DOI]
   **Evidence Level**: [A/B/C] ([rationale against METHODOLOGY §3.1])
   **Relevance**:
   - [what the source supports, per hypothesis or topic]

   **Key Findings**: [each number with its locator at the primary]
   **Citations**: [formatted citation]
   **Notes**: [limitations, bias, edition or version bounds]
   **Validation Status**: ✅ Verified [date] ([what was read at the primary])
   ```
4. **Link** to relevant hypotheses (H-ARCH-01, H-IMPL-01, etc.)
5. **Update** evidence distribution if needed

## Quality Target

There is no Level-A share target. The >70% target was retired by owner ruling 2026-08-19 (METHODOLOGY §8.1a): the share describes where evidence in this field lives and can fall as honest practitioner evidence is added. Tier each source accurately against §3.1, verify the cited claim at the primary, then run `python3 scripts/count_reconcile.py` and `python3 scripts/derive_source_taxonomy.py --check` (a new entry needs a dated taxonomy record under `methods/`, wired into `scripts/derive_source_taxonomy.py` as a new ADDED_* input, or `--check` fails on a count mismatch).
