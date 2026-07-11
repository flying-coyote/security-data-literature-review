---
type: reference
title: "Vendor Database Schema — Security Data Platforms"
created: 2025-10-23
tags: [vendor-database, schema, evidence-tiers, security-data, quarterly-update]
---

# Vendor Database Schema - Literature Review

**Purpose**: Master vendor database schema for security data platforms
**Status**: Active - Source of Truth for MCP Server
**Last Updated**: 2025-10-22
**Integration**: Syncs to `security-architect-mcp-server/data/vendor_database.json`

---

## Overview

This file defines the authoritative vendor database schema. The MCP server `vendor_database.json` is a **generated artifact** - all edits must be made here.

**Quarterly Update Cycle**: January, April, July, October (planned cadence — not yet started; no quarterly update produced as of 2026-07)

**Current Version**: no quarterly snapshot produced yet (the "2025-Q4 (in development)" target did not ship)

---

## Schema Documentation

See `~/security-architect-mcp-server/docs/INTEGRATION-SCHEMA.md` for complete schema definition.

**Key Principles**:
1. **Evidence-Based**: All capability scores 4-5 require Evidence Tier A/B sources
2. **Citation Stability**: All sources link to MASTER-BIBLIOGRAPHY.md
3. **Version Control**: Quarterly updates create new snapshot files
4. **Vendor Neutrality**: No marketing hype, balanced trade-offs

---

## Evidence Tier Requirements

| Capability Score | Required Evidence Tier | Minimum Sources | Confidence Level |
|-----------------|------------------------|-----------------|------------------|
| **5** (Best-in-class) | Tier A | 3+ | 4-5 |
| **4** (Strong) | Tier A or B | 2+ | 3-4 |
| **3** (Adequate) | Tier B or C | 1-2 | 2-3 |
| **2** (Limited) | Tier C or D | 1 | 1-2 |
| **1** (Weak) | Any tier | 1 | 1 |
| **0** (Not supported) | N/A | N/A | N/A |

---

## Vendor Entry Template

Use this template when adding new vendors:

```json
{
  "id": "vendor-name-lowercase",
  "name": "Vendor Name",
  "category": "SIEM Platform | Query Engine | Lakehouse | ETL/ELT Platform | OLAP/Analytics Engine | Data Catalog & Governance | Observability Platform | Streaming Platform | Security Analytics",
  "description": "1-2 sentence description focusing on security data use cases and key differentiators. No marketing hype.",
  "website": "https://vendor.com",

  "capabilities": {
    "query_performance": {
      "score": 0-5,
      "evidence": {
        "tier": "A|B|C|D",
        "confidence": 1-5,
        "sources": [
          {
            "id": "source-id-kebab-case",
            "description": "Brief description of what this source validates",
            "url": "https://source-url.com",
            "evidence_tier": "A|B|C|D",
            "type": "production_deployment | benchmark | vendor_documentation | expert_interview | blog_post",
            "lit_review_ref": "MASTER-BIBLIOGRAPHY.md#source-id"
          }
        ],
        "validation_notes": "How evidence supports the score. Note any caveats or contradictions.",
        "last_validated": "2025-MM-DD"
      }
    },

    "compression_efficiency": {
      "score": 0-5,
      "evidence": { /* same structure */ }
    },

    "operational_complexity": "low | medium | high",
    "team_size_required": "lean | standard | large",
    "sql_interface": true | false,
    "deployment_models": ["cloud", "on-prem", "hybrid"],
    "cost_model": "consumption | subscription | per-gb | hybrid | oss",
    "maturity": "production | beta | alpha"
  },

  "cost_modeling": {
    "typical_annual_cost_range": "$X-Y annually",
    "cost_notes": "Detailed cost breakdown with evidence sources",
    "tco_analysis_ref": "analysis-bundles/cost-reality-reference.md#vendor-tco",
    "evidence": {
      "tier": "A|B|C|D",
      "confidence": 1-5,
      "sources": [ /* array of evidence sources */ ]
    }
  },

  "architecture_patterns": ["liger_stack", "traditional_siem", "hybrid_approach", "cloud_native", "batch_olap"],
  "liger_role": "L | I | G | E | R | multiple | none",

  "decision_tree_fit": {
    "streaming_path": true | false,
    "batch_path": true | false,
    "hybrid_path": true | false,
    "volume_threshold": "< 100GB/day | 100GB-1TB/day | 1TB+/day",
    "use_cases": ["real_time_detection", "threat_hunting", "compliance", "incident_response"],
    "decision_tree_ref": "archive/analysis-bundles/technology-decision-tree.md#recommendation-X"
  },

  "journey_persona_fit": {
    "jennifer": "low | medium | high",
    "marcus": "low | medium | high",
    "priya": "low | medium | high",
    "rationale": "Why this vendor fits each persona (or doesn't)",
    "decision_tree_mapping": "Which decision tree path led here"
  },

  "evidence_summary": {
    "total_sources": 0,
    "tier_a_sources": 0,
    "tier_b_sources": 0,
    "tier_c_sources": 0,
    "tier_d_sources": 0,
    "overall_evidence_quality": "A | B | C | D",
    "last_validated": "2025-MM-DD",
    "validated_by": "Jeremy Wiley"
  },

  "tags": ["oss", "managed-service", "security-optimized", "production-validated"],

  "last_updated": "2025-MM-DDTHH:MM:SS",
  "source_repository": "security-data-literature-review",
  "sync_version": "2025-QX"
}
```

---

## Validation Checklist

Before committing new/updated vendor entries:

### Evidence Quality
- [ ] All capability scores 4-5 have Evidence Tier A or B sources
- [ ] All capability scores 4-5 have 2+ sources minimum
- [ ] Confidence levels align with evidence tier distribution
- [ ] No Tier D sources used for scores 4-5

### Citations
- [ ] All `evidence.sources` have valid `lit_review_ref`
- [ ] All `lit_review_ref` resolve to MASTER-BIBLIOGRAPHY.md entries
- [ ] Cost modeling has evidence sources
- [ ] Technology decision tree references are valid

### Completeness
- [ ] All 9 capability categories scored (or marked N/A with rationale)
- [ ] Architecture patterns specified
- [ ] Journey persona fit assessed
- [ ] Evidence summary calculated
- [ ] Tags include key differentiators

### Vendor Neutrality
- [ ] Description avoids marketing hype ("revolutionary", "game-changing", etc.)
- [ ] Trade-offs documented honestly
- [ ] Contradictory evidence noted in validation_notes
- [ ] Cost range realistic (not aspirational pricing)

---

## Quarterly Update Process

### Month 1: Data Collection
1. IT Harvest data refresh (when partnership established)
2. New vendor additions
3. Capability updates from vendor releases
4. Evidence source validation (check for broken links, outdated info)

### Month 2: Expert Validation
1. Expert network review (Lisa Cao, Jake Thomas, etc.)
2. Contradiction resolution
3. Confidence level adjustments
4. Blog synthesis integration

### Month 3: Publication & Sync
1. Create `quarterly-updates/2025-QX-update.md`
2. Update CHANGELOG.md
3. Run `sync_to_mcp_server.py`
4. Publish blog post on updates

---

## IT Harvest Integration (Phase 3)

When IT Harvest partnership is established:

**Automated Data Collection**:
- Vendor version updates
- Pricing changes
- Capability matrix updates
- Market trends (M&A, funding, product launches)

**Manual Validation**:
- Evidence tier classification
- Confidence level assignment
- Source citation
- Contradiction resolution

**Workflow**:
1. IT Harvest API pull → `vendor-landscape/it-harvest-raw.json`
2. Manual review → Update `vendor-database.json`
3. Evidence annotation → Link to MASTER-BIBLIOGRAPHY.md
4. Validation → Run quality checks
5. Sync → Push to MCP server

---

## Version Control & Citation Stability

**Problem**: Researchers need stable citations. If we edit vendor entries, citations break.

**Solution**: Quarterly snapshot files

```
vendor-landscape/
├── vendor-database.json ← Always current (HEAD)
├── quarterly-updates/
│   ├── 2025-Q4-update.md ← First snapshot
│   ├── 2026-Q1-update.md
│   ├── 2026-Q2-update.md
│   └── vendor-database-2025-Q4.json ← Frozen snapshot
```

**Citation Format**:
> "According to the 2025-Q4 vendor landscape snapshot, ClickHouse sustained 6M requests/second in production deployments (Cloudflare)."

---

## Contact & Maintenance

**Owner**: Jeremy Wiley
**Repository**: security-data-literature-review
**Sync Target**: security-architect-mcp-server
**Update Frequency**: Quarterly (Jan, Apr, Jul, Oct)
**Issue Tracking**: GitHub Issues (both repositories)

---

**Status**: Schema Defined - Ready for Vendor Migration
**Next**: Migrate existing 64 MCP vendors to integrated schema
