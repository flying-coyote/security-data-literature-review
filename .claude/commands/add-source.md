---
type: operating-doc
title: "Add Source to Bibliography — Evidence Tier Procedure"
created: 2026-01-02
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

Evidence Level A is defined by METHODOLOGY §3.1 (corrected 2026-08-19): **peer-reviewed research and official standards, nothing else.** Production deployments, practitioner measurements, vendor benchmarks and official project documentation are Level B however good they are, and an arXiv preprint with no published venue is Level B too.

### Tier 1: Peer-Reviewed Research and Official Standards (Evidence Level A)
- Published in a peer-reviewed journal or conference proceedings (venue confirmed at the publisher or DOI record, not inferred)
- Or an official standard or framework from a standards body (NIST, ISO, IETF RFC, and similar)
- Preprints, workshop papers whose proceedings are not yet published, and theses: Level B until the venue is confirmed

### Tier 2: Production Deployments and Practitioner Evidence (Evidence Level B)
- Measured outcomes from real production systems, with the measurement disclosed
- First-party lab benchmarks, named-practitioner talks, engineering blogs from the operating team
- Official project documentation (Apache, CNCF) for what a feature does

### Tier 3: Expert Consensus (Evidence Level B)
- Multiple domain experts agree (vendor-neutral)
- Industry-recognized authority that is not itself a published standard (MITRE guidance, CISA advisories, analyst syntheses); a published NIST or ISO standard is Tier 1
- Documented reasoning provided

### Tier 4: Vendor Claims (Evidence Level C)
- Vendor marketing or white papers
- Case studies without independent validation
- **Use sparingly, mark bias**

### Tier 5: Speculation (Evidence Level D)
- Theoretical only, no empirical support
- **Do NOT use for literature review claims**

## Process

1. **Classify** the source using criteria above
2. **Check** MASTER-BIBLIOGRAPHY.md for duplicates
3. **Add** entry with standardized format:
   ```markdown
   **"[Title]"**
   - Authors: [Complete author list]
   - Published: [Date] in [Venue]
   - URL/DOI: [Permanent link]
   - Quality: Evidence Level [A/B/C] - [rationale against METHODOLOGY §3.1]
   - Status: [Read/Referenced/Validated]
   - Key Insights: [1-2 sentence summary]
   - Related Hypotheses: [H-XX references]
   - Notes: [Methodology notes, limitations]
   ```
4. **Link** to relevant hypotheses (H-ARCH-01, H-IMPL-01, etc.)
5. **Update** evidence distribution if needed

## Quality Target

There is no Level-A share target. The >70% target was retired by owner ruling 2026-08-19 (METHODOLOGY §8.1a): the share describes where evidence in this field lives and can fall as honest practitioner evidence is added. Tier each source accurately against §3.1, verify the cited claim at the primary, then run `python3 scripts/count_reconcile.py` and `python3 scripts/derive_source_taxonomy.py --check` (a new entry needs a dated taxonomy record under `methods/`).
