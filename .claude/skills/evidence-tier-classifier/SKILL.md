---
name: Evidence Tier Classifier
description: Apply Evidence Level classification (Tier 1-5) when user adds sources, references papers, or discusses research quality for literature review. Trigger when user mentions "source", "paper", "add citation", "evidence quality", "bibliography", or evaluates research credibility. Maintain 70%+ Tier 1-2 target for publication-quality literature review. Integrates with personal academic-citation-manager skill.
allowed-tools: Read, Grep, Edit
---

# Evidence Tier Classifier

## Purpose
Maintain rigorous evidence quality standards for literature review by classifying all sources into Evidence Tiers 1-5, ensuring 70%+ Tier 1-2 for publication readiness.

## Trigger Conditions

**ACTIVATE when user:**
- Adds new sources to literature review
- Discusses research paper quality or credibility
- Mentions "evidence level", "tier", "source quality"
- Reviews bibliography entries
- Evaluates study methodology
- Says "add to bibliography", "cite this source"

**DO NOT ACTIVATE when:**
- Casual reading (not adding to bibliography)
- Internal notes or drafts
- User explicitly reviewing only

## Evidence Tier Classification System

### Tier 1: Production Deployments (Strongest - Evidence Level A)

**Criteria:**
- Measured outcomes from real production systems
- Quantitative performance data from operational environments
- Direct practitioner validation with metrics
- Documented costs, latency, throughput from live deployments

**Examples:**
- "Okta processes 100K QPS with DuckDB in production" (Jake Thomas, 2024)
- "Splunk deployment costs $2.3M annually for 10TB/day" (enterprise case study)
- "SOC reduced query latency 85% after Iceberg migration" (measured outcome)

**Classification Weight**: Evidence Level A (highest confidence)

### Tier 2: Peer-Reviewed Research (Strong - Evidence Level A)

**Criteria:**
- Published in peer-reviewed journals or top-tier conferences
- Reproducible methodology clearly documented
- Results independently validated or replicated
- Rigorous statistical analysis where applicable

**Examples:**
- ACM CSUR journal articles
- IEEE Security & Privacy conference papers
- USENIX OSDI systems papers
- VLDB database research papers

**Classification Weight**: Evidence Level A (high confidence)

### Tier 3: Expert Consensus (Moderate - Evidence Level B)

**Criteria:**
- Multiple domain experts agree on methodology
- Industry-recognized thought leaders
- Vendor-neutral assessment or framework
- Documented reasoning provided (not just assertion)

**Examples:**
- NIST cybersecurity guidelines
- MITRE ATT&CK framework
- Industry analyst reports (Gartner, Forrester with methodology)
- Practitioner blogs with production insights (Anton Chuvakin, Bruce Schneier)

**Classification Weight**: Evidence Level B (moderate confidence)

### Tier 4: Vendor Claims (Weak - Evidence Level C)

**Criteria:**
- Vendor marketing materials or white papers
- Case studies without independent validation
- Benchmarks conducted by vendor
- Product documentation claims

**Warning**: Must be marked as unvalidated, potential bias

**Examples:**
- Vendor white papers
- Sales case studies
- Product benchmark reports (vendor-run)
- Marketing collateral

**Classification Weight**: Evidence Level C (use with caution)

### Tier 5: Speculation (Insufficient - Evidence Level D)

**Criteria:**
- Theoretical proposals without empirical testing
- Blog posts without supporting data
- Social media claims or discussions
- Personal opinions without evidence

**Warning**: Do NOT use for evidence-based literature review claims

**Classification Weight**: Evidence Level D (insufficient for research)

## Classification Workflow

### Step 1: Source Metadata Capture

**When user adds source:**
```
Source Metadata:
- Title: [Full title]
- Author(s): [Complete list]
- Published: [Date] in [Venue]
- URL/DOI: [Permanent link]
- Type: [Journal / Conference / Blog / Industry Report / Vendor]
```

### Step 2: Tier Classification Assessment

**Apply classification criteria:**
```
Evidence Tier Assessment:

Tier 1 (Production - Evidence Level A): ☐
Questions:
- Measured production outcomes with specific metrics?
- Real deployment data (not simulation)?
- Quantitative performance documented?
- Practitioner validation with attribution?

Tier 2 (Peer-reviewed - Evidence Level A): ☐
Questions:
- Published in peer-reviewed venue?
- Reproducible methodology documented?
- Statistical validation provided?
- Independent replication possible?

Tier 3 (Expert Consensus - Evidence Level B): ☐
Questions:
- Multiple experts agree (vendor-neutral)?
- Documented reasoning provided?
- Industry-recognized authority?
- Framework or guideline (NIST, MITRE)?

Tier 4 (Vendor - Evidence Level C): ☐
Questions:
- Vendor marketing or sales material?
- Unvalidated case study?
- Benchmark conducted by vendor?
Warning: Mark bias, use sparingly

Tier 5 (Speculation - Evidence Level D): ☐
Questions:
- No empirical support?
- Theoretical only?
- Social media or unsupported blog?
Warning: Do NOT use for literature review

Classification: Tier [N] (Evidence Level [A/B/C/D])
Rationale: [Why this tier? Specific criteria met]
```

### Step 3: Add to Master Bibliography

**Check existing entry:**
```bash
# Search for existing source
Grep: MASTER-BIBLIOGRAPHY.md for [author or title]
```

**Add new entry:**
```markdown
Edit: MASTER-BIBLIOGRAPHY.md

**"[Title]"**
- Authors: [Complete author list]
- Published: [Date] in [Venue]
- URL/DOI: [Permanent link]
- Quality: Tier [N] (Evidence Level [A/B/C/D]) - [rationale]
- Status: [Read/Referenced/Validated]
- Key Insights: [1-2 sentence summary]
- Related Hypotheses: [H-XX references]
- Notes: [Methodology notes, limitations, etc.]
```

### Step 4: Update Evidence Distribution

**Calculate distribution:**
```bash
# Count entries by tier
Grep: MASTER-BIBLIOGRAPHY.md count by tier

Evidence Distribution Report:
---
Total Sources: [N]

Tier 1 (Production): [X] ([%])
Tier 2 (Peer-reviewed): [Y] ([%])
Tier 3 (Expert): [Z] ([%])
Tier 4 (Vendor): [A] ([%])
Tier 5 (Speculation): [B] ([%])

Evidence Level A (Tier 1+2): [%]
Evidence Level B (Tier 3): [%]
Evidence Level C (Tier 4): [%]
Evidence Level D (Tier 5): [%]

Target: 70%+ Evidence Level A (Tier 1+2)
Current: [%] ✅/⚠️
```

**Current Status** (as of Oct 16):
- Total: 76+ sources
- Evidence Level A: 79% (✅ EXCEEDS 70% target)
- Distribution: Strong production + peer-reviewed mix

### Step 5: Quality Assessment

**Assess overall quality:**
```
Literature Review Quality Assessment:

✅ PUBLICATION-READY if:
- 70%+ Evidence Level A (Tier 1+2)
- Tier 4-5 sources clearly marked as limited evidence
- Diverse source mix (not relying on single type)
- Key hypotheses supported by Tier 1-2 evidence

⚠️ NEEDS IMPROVEMENT if:
- <70% Evidence Level A
- Over-reliance on Tier 4 vendor sources
- Tier 5 speculation used for claims
- Key hypotheses lack Tier 1-2 support
```

## Integration with Hypothesis Validation

**Link evidence to hypotheses:**

**For each source:**
```
Related Hypotheses: H-ARCH-03, H-DATA-01, H-EDGE-01

Evidence Support:
- H-ARCH-03: Tier 1 evidence (production validation)
- H-DATA-01: Tier 2 evidence (peer-reviewed study)
- H-EDGE-01: Tier 3 evidence (expert consensus)
```

**Hypothesis confidence influenced by tier:**
- High Confidence: Multiple Tier 1-2 sources
- Medium Confidence: Tier 2-3 sources, limited Tier 1
- Low Confidence: Mainly Tier 3-4, no Tier 1-2

## Project-Specific Guidelines

**Target for "Modern Data Stack for Cybersecurity" Literature Review:**
- Minimum: 70% Evidence Level A (Tier 1+2)
- Ideal: 75-80% Evidence Level A
- Current: 79% (✅ exceeds target)
- Sources: 76+ documented (target: 100+ for comprehensive review)

**Practitioner Focus:**
- Heavily weight Tier 1 (production deployments)
- Practitioners trust production validation over theory
- Balance with Tier 2 (academic rigor for credibility)
- Use Tier 3 for frameworks (NIST, MITRE)
- Minimize Tier 4, avoid Tier 5

## Special Cases

### Vendor Claims (Tier 4 Handling)

**When vendor source is necessary:**
```
✓ Mark clearly as vendor claim
✓ Note potential bias
✓ Seek corroborating independent evidence
✓ Use for feature lists, not performance claims
✓ Prefer independent benchmarks over vendor tests
```

**Example:**
```markdown
**"Splunk Performance Whitepaper"**
- Tier: 4 (Vendor claim - Splunk marketing)
- Use: Feature capabilities only
- Caution: Performance claims unvalidated
- Corroborate: Seek practitioner testimonials (Tier 1)
```

### Thought Leader Blogs (Tier 2-3 Determination)

**Tier 2 (if):**
- Production examples with specific metrics
- Reproducible methodology
- Peer-reviewed venue or comparable rigor

**Tier 3 (if):**
- Expert perspective with reasoning
- Industry experience documented
- Vendor-neutral assessment
- But no empirical data or production metrics

**Example:**
- Anton Chuvakin blog: Usually Tier 3 (expert perspective)
- IF includes production metrics: Upgrade to Tier 1
- IF speculative opinion: Tier 5 (don't use)

## Anti-Patterns to Avoid

**DON'T:**
- ❌ Inflate tier to justify weak claim
- ❌ Use Tier 5 sources for evidence-based statements
- ❌ Over-rely on Tier 4 vendor materials
- ❌ Mix tiers without clarification
- ❌ Cite sources you haven't read (tier requires evaluation)

**DO:**
- ✅ Be honest about tier classification
- ✅ Seek higher-tier sources for key claims
- ✅ Mark vendor bias explicitly
- ✅ Balance production (Tier 1) with academic (Tier 2)
- ✅ Document classification rationale

## Integration with Other Skills

**Works WITH:**
- **academic-citation-manager** (personal): General citation management
- **research-synthesis-extractor** (project1): Extract concepts from sources
- **hypothesis-validator** (project1): Link evidence to hypotheses
- **publication-quality-checker** (project1): Verify evidence before publishing

**Sequence:**
1. User finds source
2. **Evidence Tier Classifier**: Classify tier (1-5)
3. **Academic Citation Manager**: Add to bibliography
4. **Research Synthesis Extractor**: Extract concepts
5. **Hypothesis Validator**: Link to relevant hypotheses

## Example Classification Session

**User**: "I found a paper about DuckDB performance from VLDB 2024 conference"

**Evidence Tier Classifier**:

```
Evidence Tier Classification

Source Metadata:
- Title: "DuckDB: Efficient Analytical Query Processing in SQL"
- Authors: Raasveldt, Mühleisen
- Published: 2024, VLDB (Very Large Databases) Conference
- Type: Peer-reviewed conference paper

Tier Assessment:

Tier 1 (Production): ☐ No - Research paper, not production deployment
Tier 2 (Peer-reviewed): ✓ YES
- VLDB is top-tier database conference (peer-reviewed)
- Reproducible methodology with benchmarks
- Independent validation possible
- Academic rigor demonstrated

Tier 3 (Expert): ☐ No - Exceeds expert consensus (has peer review)
Tier 4 (Vendor): ☐ No - Academic research, vendor-neutral
Tier 5 (Speculation): ☐ No - Empirical data provided

Classification: Tier 2 (Evidence Level A)
Rationale: Peer-reviewed top-tier conference, reproducible methodology,
independent benchmarks provided

Add to bibliography:

**"DuckDB: Efficient Analytical Query Processing in SQL"**
- Authors: Mark Raasveldt, Hannes Mühleisen
- Published: 2024, VLDB Conference
- DOI: [doi link]
- Quality: Tier 2 (Evidence Level A) - Peer-reviewed, reproducible methodology
- Status: Read
- Key Insights: Columnar vectorized execution, 100x faster than SQLite
- Related Hypotheses: H-EDGE-01 (edge processing), H-DATA-05 (query performance)
- Notes: Benchmarks include TPC-H, reproducible with provided test harness

Evidence Distribution Update:
---
Total Sources: 77 (was 76)
Evidence Level A (Tier 1+2): 79.2% (✅ maintains >70% target)
Tier 2 count: 42 sources
```

## Quick Reference

### Evidence Tier Summary
```
Tier 1: Production (measured outcomes) → Evidence Level A
Tier 2: Peer-reviewed (reproducible) → Evidence Level A
Tier 3: Expert consensus (documented) → Evidence Level B
Tier 4: Vendor claims (mark bias) → Evidence Level C
Tier 5: Speculation (don't use) → Evidence Level D

Target: 70%+ Evidence Level A (Tier 1+2)
Current: 79% ✅
```

### Classification Decision Tree
```
Has measured production data with metrics? → Tier 1
Peer-reviewed + reproducible? → Tier 2
Expert consensus + reasoning? → Tier 3
Vendor material? → Tier 4 (mark bias)
Speculation without data? → Tier 5 (don't use)
```

## References

**Current Status**: 76+ sources, 79% Evidence Level A
**Target**: 100+ sources, maintain 70%+ Evidence Level A
**Methodology**: PRISMA-aligned systematic review
**File**: `MASTER-BIBLIOGRAPHY.md` in literature review project

---

**Version**: 1.0
**Created**: 2025-10-17
**Applies to**: security-data-literature-review project
