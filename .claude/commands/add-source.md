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

### Tier 1: Production Deployments (Evidence Level A)
- Measured outcomes from real production systems
- Quantitative performance data from operational environments
- Direct practitioner validation with metrics

### Tier 2: Peer-Reviewed Research (Evidence Level A)
- Published in peer-reviewed journals or top-tier conferences
- Reproducible methodology documented
- Results independently validated

### Tier 3: Expert Consensus (Evidence Level B)
- Multiple domain experts agree (vendor-neutral)
- Industry-recognized authority (NIST, MITRE, etc.)
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
   - Quality: Tier [N] (Evidence Level [A/B/C/D]) - [rationale]
   - Status: [Read/Referenced/Validated]
   - Key Insights: [1-2 sentence summary]
   - Related Hypotheses: [H-XX references]
   - Notes: [Methodology notes, limitations]
   ```
4. **Link** to relevant hypotheses (H-ARCH-01, H-IMPL-01, etc.)
5. **Update** evidence distribution if needed

## Quality Target

Maintain 75%+ Evidence Level A (Tier 1+2 sources).

Current distribution will be checked after adding source.
