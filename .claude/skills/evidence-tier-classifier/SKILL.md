---
type: spec
name: Evidence Tier Classifier
description: Apply Evidence Level classification (Tier 1-5) when user adds sources, references papers, or discusses research quality for literature review. Trigger when user mentions "source", "paper", "add citation", "evidence quality", "bibliography", or evaluates research credibility. Maintain 75%+ Tier 1-2 target for publication-quality literature review.
allowed-tools: Read, Grep, Edit
---

# Evidence Tier Classifier

## Purpose
Classify sources into Evidence Tiers 1-5, maintaining 75%+ Tier 1-2 for publication readiness.

## Trigger Conditions

**ACTIVATE when user:**
- Adds sources, discusses paper quality, mentions "evidence level/tier/source quality"
- Says "add to bibliography", "cite this source", reviews bibliography entries

**DO NOT ACTIVATE for:** Casual reading, internal notes, review-only discussions

## Evidence Tier System

| Tier | Name | Evidence Level | Criteria | Use |
|------|------|---------------|----------|-----|
| **1** | Production | A (highest) | Measured outcomes from live systems with metrics | Primary evidence |
| **2** | Peer-Reviewed | A (high) | Published in journals/conferences, reproducible methodology | Primary evidence |
| **3** | Expert Consensus | B (moderate) | Multiple experts agree, vendor-neutral, documented reasoning | Supporting evidence |
| **4** | Vendor Claims | C (weak) | Marketing, unvalidated case studies, vendor benchmarks | Mark bias, use sparingly |
| **5** | Speculation | D (insufficient) | No empirical support, social media, opinions | Do NOT use |

**Target**: 75%+ Evidence Level A (Tier 1+2) | **Current**: 78% ✅

## Classification Workflow

### Step 1: Capture Metadata
```
Title: [Full title]
Author(s): [Complete list]
Published: [Date] in [Venue]
URL/DOI: [Permanent link]
Type: [Journal/Conference/Blog/Industry Report/Vendor]
```

### Step 2: Apply Decision Tree
```
Has measured production metrics? → Tier 1
Peer-reviewed + reproducible? → Tier 2
Expert consensus + reasoning? → Tier 3
Vendor material? → Tier 4 (mark bias)
No empirical support? → Tier 5 (don't use)
```

### Step 3: Add to Bibliography
```markdown
**"[Title]"**
- Authors: [list]
- Published: [Date] in [Venue]
- URL/DOI: [link]
- Quality: Tier [N] (Evidence Level [A/B/C/D]) - [rationale]
- Status: [Read/Referenced/Validated]
- Key Insights: [1-2 sentences]
- Related Hypotheses: [H-XX references]
```

### Step 4: Verify Distribution
After adding, check Evidence Level A percentage remains ≥75%.

## Special Cases

**Vendor Sources (Tier 4)**: Mark bias, use for features not performance, seek corroboration.

**Thought Leader Blogs**:
- Has production metrics → Tier 1
- Expert reasoning only → Tier 3
- Speculation → Tier 5 (don't use)

## Anti-Patterns

❌ Inflate tier to justify claims | ❌ Use Tier 5 for evidence | ❌ Over-rely on Tier 4
✅ Be honest about classification | ✅ Seek Tier 1-2 for key claims | ✅ Document rationale

## Hypothesis Confidence

- **High**: Multiple Tier 1-2 sources
- **Medium**: Tier 2-3 sources, limited Tier 1
- **Low**: Mainly Tier 3-4, no Tier 1-2

## Current Status

- **Sources**: 101 documented
- **Evidence Level A**: 78% (✅ exceeds 75% target)
- **File**: `MASTER-BIBLIOGRAPHY.md`

---
**Version**: 1.1 | **Updated**: 2026-01-02
