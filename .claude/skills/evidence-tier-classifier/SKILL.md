---
type: spec
name: Evidence Tier Classifier
description: Classify a source at Evidence Level A, B, C or D under METHODOLOGY §3.1 when the user adds a source to the literature review, cites a paper, or asks about a source's evidence quality. Trigger when the user mentions "source", "paper", "add citation", "evidence level", "tier", "bibliography" or evaluates research credibility. Level A is peer-reviewed research and official standards only; there is no Level-A share target.
allowed-tools: Read, Grep, Edit
---

# Evidence Tier Classifier

## Purpose
Give each source the Evidence Level that METHODOLOGY §3.1 defines, with the rationale written into its bibliography entry, so a reader can see why a claim rests where it does. The classifier tiers accurately; it does not aim for a share. The Level-A target was retired by owner ruling 2026-08-19 (METHODOLOGY §8.1a), because the share falls as honest practitioner evidence is added and a floor on it rewards over-tiering.

## Trigger conditions

**Activate when the user:**
- Adds sources, discusses paper quality, mentions "evidence level", "tier" or "source quality"
- Says "add to bibliography" or "cite this source", or reviews bibliography entries

**Do not activate for:** casual reading, internal notes, review-only discussions

## Evidence levels (METHODOLOGY §3.1 is canonical)

| Level | What qualifies | Use |
|-------|----------------|-----|
| **A** | Peer-reviewed research at a named venue (confirmed at the publisher or DOI record); standards-body documents (NIST SP/IR/FIPS, ISO/IEC, IETF RFC, W3C, OASIS); the formal specification of an open standard (the Iceberg table spec, the OCSF schema spec); normative frameworks from a neutral body (MITRE D3FEND, MITRE ATLAS), authoritative on structure and silent on efficacy | Primary evidence |
| **B** | Production deployments and case studies with real numbers; first-party lab benchmarks; vendor engineering blogs from the operating team; conference talks; trade books; analyst reports; expert interviews; government advisories (as distinct from standards); official project documentation; preprints, theses and workshop papers whose venue is not confirmed | Real evidence, not independently reviewed |
| **C** | Vendor blog posts, product documentation, white papers and talks with no production measurement behind them; vendor-authored pieces quoting a practitioner | Catalogued with bias flagged; never carries a hypothesis on its own |
| **D** | Marketing, unverified claims, speculation | Excluded from the review |

Vendor-channel rule (owner-adjudicated 2026-07-10): first-person practitioner authorship on a vendor channel is Level B with a curation caveat; a vendor-authored piece quoting a practitioner is Level C.

## Classification workflow

### Step 1: capture metadata
```text
Title: [Full title]
Author(s): [Complete list]
Published: [Date] in [Venue]
URL/DOI: [Permanent link]
Type: [Journal/Conference/Standard/Specification/Talk/Blog/Industry Report/Vendor]
```

### Step 2: apply the decision tree
```text
Peer-reviewed at a confirmed venue, a standards-body document,
  a formal open-standard specification, or a normative MITRE framework? -> A
Practitioner or production evidence with the measurement disclosed,
  a talk, an analyst report, project docs, or an unconfirmed-venue preprint? -> B
Vendor material with no production measurement behind it? -> C (flag bias)
No empirical support? -> D (do not catalogue)
```

### Step 3: add to the bibliography
Use the entry format of the most recent `#### ` blocks in MASTER-BIBLIOGRAPHY.md:
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

### Step 4: check the gates
Add a dated taxonomy record under `methods/`, then run `python3 scripts/count_reconcile.py` and `python3 scripts/derive_source_taxonomy.py --check`. The new counts propagate through the gated surfaces; nothing is hand-edited to a target.

## Anti-patterns

- Inflating a level to make a claim look stronger
- Treating a production case study, however good, as Level A
- Marking a number verified without reading it at the primary
- Letting a Level C source carry a hypothesis alone

## Hypothesis confidence
Confidence is not inferred from tier mix here. It is scored under the five-dimension instrument in `methods/scoring-rubric.md`, and the canonical scores are PUBLICATION-MANUSCRIPT.md §3.7.

---
**Version**: 2.0 | **Updated**: 2026-11-17 (tier definitions brought to METHODOLOGY §3.1; retired 75% target and Jan-2026 counts removed)
