# Literature Review MCP Server Specification

**Version**: 1.0.0
**Date**: January 20, 2026
**Status**: Design Phase (Production-ready quality standards)
**Based On**: H-MCP-CONTEXT-01 (Validated - >80% context reduction with workflow-based tools)

---

## Executive Summary

MCP server for managing the living literature review supporting the Modern Data Stack for Cybersecurity book (115,500 words) and Security Data Commons blog (3x/week). Designed for evidence-based research workflows with professional genealogy-grade source tracking.

**Key Metrics**:
- 115+ sources (79% Evidence Level A)
- 32 hypotheses tracked
- 71 vendors in landscape database
- Monthly rolling updates + quarterly deep dives

---

## Design Principles (Context-Efficient)

Following H-MCP-CONTEXT-01 validated patterns:

1. **4 high-level workflow tools** (not 20+ granular operations)
2. **Tool Output Schemas** for all responses
3. **On-demand sub-tool loading** via `find_tools` meta-tool
4. **Lazy bibliography loading** (by topic/tier, not full 115+ sources)

---

## Core Workflows (4 Workflow-Based Tools)

### 1. `bibliography_workflow`

**Purpose**: Search, add, update, and cite sources from MASTER-BIBLIOGRAPHY.md

**When to Use**:
- Finding sources for a specific topic/vendor/hypothesis
- Adding new sources with evidence tier classification
- Generating citations in Chicago/Evidence Explained format
- Validating evidence distribution (maintain 75%+ Level A)

**Input Schema**:
```json
{
  "type": "object",
  "properties": {
    "action": {
      "type": "string",
      "enum": ["search", "add", "update", "cite", "validate_distribution"],
      "description": "Bibliography operation to perform"
    },
    "query": {
      "type": "object",
      "properties": {
        "topic": {"type": "string", "description": "Topic filter (e.g., 'ClickHouse', 'OCSF', 'streaming')"},
        "evidence_tier": {"type": "string", "enum": ["A", "B", "C", "D", "any"]},
        "vendor": {"type": "string"},
        "date_range": {
          "type": "object",
          "properties": {
            "start": {"type": "string", "format": "date"},
            "end": {"type": "string", "format": "date"}
          }
        },
        "production_only": {"type": "boolean", "default": false}
      }
    },
    "source": {
      "type": "object",
      "description": "Required for 'add' action",
      "properties": {
        "title": {"type": "string"},
        "authors": {"type": "array", "items": {"type": "string"}},
        "date": {"type": "string", "format": "date"},
        "url": {"type": "string", "format": "uri"},
        "evidence_tier": {"type": "string", "enum": ["A", "B", "C", "D"]},
        "relevance": {"type": "string"},
        "key_findings": {"type": "array", "items": {"type": "string"}},
        "chapter_links": {"type": "array", "items": {"type": "string"}},
        "hypothesis_links": {"type": "array", "items": {"type": "string"}}
      }
    },
    "citation_format": {
      "type": "string",
      "enum": ["chicago", "evidence_explained", "substack_footnote"],
      "default": "chicago"
    }
  },
  "required": ["action"]
}
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "sources": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "title": {"type": "string"},
          "authors": {"type": "array", "items": {"type": "string"}},
          "date": {"type": "string"},
          "evidence_tier": {"type": "string"},
          "url": {"type": "string"},
          "hypothesis_links": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "total_count": {"type": "integer"},
    "evidence_distribution": {
      "type": "object",
      "properties": {
        "tier_a_percent": {"type": "number"},
        "tier_b_percent": {"type": "number"},
        "tier_c_percent": {"type": "number"},
        "tier_d_percent": {"type": "number"},
        "compliant": {"type": "boolean", "description": "True if >=75% Tier A"}
      }
    },
    "citation": {
      "type": "string",
      "description": "Formatted citation if action was 'cite'"
    },
    "warnings": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Quality warnings (broken links, outdated sources, etc.)"
    }
  }
}
```

---

### 2. `hypothesis_workflow`

**Purpose**: Track, validate, and synthesize evidence for 32+ research hypotheses

**When to Use**:
- Checking evidence coverage for a hypothesis
- Linking new sources to hypotheses
- Calculating confidence levels
- Identifying evidence gaps
- Generating synthesis reports

**Input Schema**:
```json
{
  "type": "object",
  "properties": {
    "action": {
      "type": "string",
      "enum": ["get_status", "link_source", "calculate_confidence", "find_gaps", "synthesize"],
      "description": "Hypothesis operation to perform"
    },
    "hypothesis_id": {
      "type": "string",
      "description": "Hypothesis ID (e.g., 'H-ARCH-01', 'H-EDGE-01', 'H-LIGER-01')"
    },
    "source_link": {
      "type": "object",
      "description": "Required for 'link_source' action",
      "properties": {
        "source_id": {"type": "string"},
        "evidence_type": {"type": "string", "enum": ["supporting", "contradicting", "neutral"]},
        "confidence_contribution": {"type": "number", "minimum": -1, "maximum": 1},
        "notes": {"type": "string"}
      }
    },
    "scope": {
      "type": "string",
      "enum": ["single", "research_question", "all"],
      "default": "single",
      "description": "Scope for gap analysis or synthesis"
    },
    "research_question": {
      "type": "string",
      "description": "Research question ID for scoped operations (e.g., 'RQ7', 'RQ13')"
    }
  },
  "required": ["action"]
}
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "hypothesis": {
      "type": "object",
      "properties": {
        "id": {"type": "string"},
        "statement": {"type": "string"},
        "research_question": {"type": "string"},
        "confidence_level": {"type": "number", "minimum": 1, "maximum": 5},
        "evidence_status": {"type": "string", "enum": ["validated", "partial", "gap", "contradicted"]}
      }
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source_id": {"type": "string"},
          "source_title": {"type": "string"},
          "evidence_type": {"type": "string"},
          "evidence_tier": {"type": "string"},
          "key_finding": {"type": "string"}
        }
      }
    },
    "gaps": {
      "type": "array",
      "description": "Missing evidence for full validation",
      "items": {
        "type": "object",
        "properties": {
          "gap_type": {"type": "string"},
          "description": {"type": "string"},
          "recommended_sources": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "contradictions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source_a": {"type": "string"},
          "source_b": {"type": "string"},
          "contradiction": {"type": "string"},
          "resolution_status": {"type": "string", "enum": ["unresolved", "resolved", "noted"]}
        }
      }
    },
    "synthesis": {
      "type": "string",
      "description": "Generated synthesis text for 'synthesize' action"
    }
  }
}
```

**Hypothesis Tracking Data Model**:
```json
{
  "hypotheses": {
    "H-ARCH-01": {
      "statement": "Isolation-first architecture provides 10x better query performance for threat hunting",
      "research_question": "RQ7",
      "confidence_level": 4,
      "sources": [
        {"id": "netflix-2024", "type": "supporting", "tier": "A"},
        {"id": "okta-2025", "type": "supporting", "tier": "A"}
      ],
      "validation_status": "partial",
      "gaps": ["Need 2 more production case studies"],
      "last_updated": "2026-01-15"
    }
  }
}
```

---

### 3. `expert_interview_workflow`

**Purpose**: Coordinate expert interviews for hypothesis validation

**When to Use**:
- Preparing interview guides
- Storing structured interview data
- Tracking expert vs. literature evidence
- Generating post-interview synthesis

**Input Schema**:
```json
{
  "type": "object",
  "properties": {
    "action": {
      "type": "string",
      "enum": ["prepare_guide", "store_interview", "get_expert_evidence", "synthesize_interview"],
      "description": "Interview operation to perform"
    },
    "expert": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "organization": {"type": "string"},
        "expertise_areas": {"type": "array", "items": {"type": "string"}},
        "hypotheses_relevant": {"type": "array", "items": {"type": "string"}}
      }
    },
    "interview_data": {
      "type": "object",
      "description": "Required for 'store_interview' action",
      "properties": {
        "date": {"type": "string", "format": "date"},
        "duration_minutes": {"type": "integer"},
        "questions_asked": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "question": {"type": "string"},
              "answer": {"type": "string"},
              "hypothesis_link": {"type": "string"},
              "confidence_from_answer": {"type": "number", "minimum": 1, "maximum": 5}
            }
          }
        },
        "key_insights": {"type": "array", "items": {"type": "string"}},
        "follow_up_needed": {"type": "array", "items": {"type": "string"}}
      }
    }
  },
  "required": ["action"]
}
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "interview_guide": {
      "type": "object",
      "description": "Generated for 'prepare_guide' action",
      "properties": {
        "expert_name": {"type": "string"},
        "primary_questions": {"type": "array", "items": {"type": "string"}},
        "hypothesis_validation_questions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "hypothesis_id": {"type": "string"},
              "question": {"type": "string"},
              "current_evidence": {"type": "string"}
            }
          }
        },
        "follow_up_templates": {"type": "array", "items": {"type": "string"}}
      }
    },
    "expert_evidence": {
      "type": "array",
      "description": "All evidence from expert interviews (distinct from literature)",
      "items": {
        "type": "object",
        "properties": {
          "expert": {"type": "string"},
          "date": {"type": "string"},
          "hypothesis_id": {"type": "string"},
          "evidence_type": {"type": "string"},
          "confidence_contribution": {"type": "number"},
          "quote": {"type": "string"}
        }
      }
    },
    "synthesis": {
      "type": "string",
      "description": "Post-interview synthesis for 'synthesize_interview' action"
    }
  }
}
```

---

### 4. `vendor_landscape_workflow`

**Purpose**: Manage the 71-vendor landscape database synchronized with Security Architect MCP Server

**When to Use**:
- Querying vendors by capability/evidence tier
- Validating vendor scores against evidence requirements
- Generating quarterly snapshots
- Syncing with Security Architect MCP Server

**Input Schema**:
```json
{
  "type": "object",
  "properties": {
    "action": {
      "type": "string",
      "enum": ["query", "validate_evidence", "generate_snapshot", "sync_mcp_server", "compare_vendors"],
      "description": "Vendor landscape operation"
    },
    "query": {
      "type": "object",
      "properties": {
        "category": {"type": "string"},
        "capability": {"type": "string"},
        "evidence_tier_min": {"type": "string", "enum": ["A", "B", "C", "D"]},
        "production_validated": {"type": "boolean"}
      }
    },
    "vendor_id": {"type": "string"},
    "snapshot_version": {"type": "string", "description": "e.g., '2026-Q1-v1.0'"}
  },
  "required": ["action"]
}
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "vendors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "name": {"type": "string"},
          "category": {"type": "string"},
          "evidence_quality": {"type": "string"},
          "production_deployments": {"type": "integer"},
          "analyst_coverage": {"type": "boolean"}
        }
      }
    },
    "evidence_validation": {
      "type": "object",
      "description": "Result of 'validate_evidence' action",
      "properties": {
        "vendor": {"type": "string"},
        "capability_scores": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "capability": {"type": "string"},
              "score": {"type": "integer", "minimum": 0, "maximum": 5},
              "required_evidence_tier": {"type": "string"},
              "actual_evidence_tier": {"type": "string"},
              "compliant": {"type": "boolean"}
            }
          }
        },
        "overall_compliant": {"type": "boolean"}
      }
    },
    "sync_status": {
      "type": "object",
      "properties": {
        "vendors_synced": {"type": "integer"},
        "conflicts_found": {"type": "integer"},
        "conflicts": {"type": "array", "items": {"type": "string"}}
      }
    }
  }
}
```

---

## Meta-Tool: `find_tools`

**Purpose**: Dynamic tool discovery for Claude Code tool search integration

```json
{
  "name": "find_tools",
  "description": "Search available literature review tools by keyword or task description",
  "input": {
    "query": {"type": "string", "description": "Natural language description of needed capability"}
  },
  "output": {
    "tools": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "description": {"type": "string"},
          "typical_use": {"type": "string"}
        }
      }
    }
  }
}
```

**Tool Metadata for Discovery**:
```python
TOOL_METADATA = [
    {
        "name": "bibliography_workflow",
        "description": "Search, add, cite sources from 115+ source bibliography. Evidence tier classification.",
        "keywords": ["source", "citation", "bibliography", "reference", "evidence", "tier"],
        "typical_use": "Finding sources, adding new research, generating citations"
    },
    {
        "name": "hypothesis_workflow",
        "description": "Track 32+ hypotheses, link evidence, calculate confidence, find gaps.",
        "keywords": ["hypothesis", "evidence", "confidence", "gap", "validate", "research question"],
        "typical_use": "Hypothesis validation, evidence synthesis, gap analysis"
    },
    {
        "name": "expert_interview_workflow",
        "description": "Prepare interview guides, store interview data, track expert evidence.",
        "keywords": ["expert", "interview", "guide", "validation", "quote"],
        "typical_use": "Expert interview preparation and synthesis"
    },
    {
        "name": "vendor_landscape_workflow",
        "description": "Query 71 vendors, validate evidence quality, sync with MCP server.",
        "keywords": ["vendor", "landscape", "capability", "sync", "compare"],
        "typical_use": "Vendor research, evidence validation, MCP sync"
    }
]
```

---

## Sub-Tools (Loaded On-Demand)

These tools are not exposed directly but loaded by workflow tools when needed:

| Sub-Tool | Parent Workflow | Purpose |
|----------|-----------------|---------|
| `parse_bibliography_md` | bibliography_workflow | Parse MASTER-BIBLIOGRAPHY.md |
| `classify_evidence_tier` | bibliography_workflow | Apply 5-tier classification rules |
| `validate_url` | bibliography_workflow | Check for broken links |
| `calculate_hypothesis_confidence` | hypothesis_workflow | Aggregate evidence into confidence score |
| `detect_contradictions` | hypothesis_workflow | Find conflicting sources |
| `generate_interview_guide` | expert_interview_workflow | Template-based guide generation |
| `sync_vendor_database` | vendor_landscape_workflow | Sync with Security Architect MCP |

---

## Data Storage

### File-Based Storage (Existing)

| File | Purpose | MCP Access |
|------|---------|------------|
| `MASTER-BIBLIOGRAPHY.md` | 115+ sources | Read/Write |
| `LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md` | 32 hypotheses | Read/Write |
| `vendor-landscape/vendor-database.json` | 71 vendors | Read/Write |
| `monthly-update-tracker.md` | Update history | Read |

### New Data Models

**Hypothesis Index** (`data/hypothesis-index.json`):
```json
{
  "version": "1.0.0",
  "last_updated": "2026-01-20",
  "hypotheses": {
    "H-ARCH-01": {
      "statement": "...",
      "research_question": "RQ7",
      "sources": ["source-id-1", "source-id-2"],
      "confidence": 4,
      "status": "partial"
    }
  }
}
```

**Expert Evidence Store** (`data/expert-evidence.json`):
```json
{
  "version": "1.0.0",
  "interviews": [
    {
      "expert": "Jake Thomas",
      "organization": "Okta",
      "date": "2026-01-20",
      "evidence": [
        {
          "hypothesis_id": "H-EDGE-01",
          "type": "supporting",
          "confidence_contribution": 0.8,
          "quote": "..."
        }
      ]
    }
  ]
}
```

---

## Implementation Stack

- **Python SDK**: `modelcontextprotocol/python-sdk`
- **Transport**: Streamable HTTP (stateless)
- **Storage**: Local JSON + Markdown files
- **Integration**:
  - Security Architect MCP Server (vendor sync)
  - Blog publishing workflow (evidence validation)

---

## Token Efficiency Targets

| Scenario | Without MCP | With MCP | Reduction |
|----------|-------------|----------|-----------|
| Bibliography search | ~15K (full file read) | ~2K (structured query) | 87% |
| Hypothesis validation | ~20K (multiple file reads) | ~3K (index lookup) | 85% |
| Vendor comparison | ~10K (database load) | ~1.5K (filtered query) | 85% |
| Expert interview prep | ~8K (manual research) | ~1K (generated guide) | 88% |

---

## Quality Standards

### Evidence Tier Requirements

| Tier | Evidence Level | Use Case | % Target |
|------|---------------|----------|----------|
| A | Production metrics, peer-reviewed | Primary claims | ≥45% |
| B | Analyst reports, expert consensus | Supporting claims | ≥30% |
| C | Vendor-neutral expert opinions | Context | ≤20% |
| D | Vendor claims (disclosed) | Comparison only | ≤5% |

### Validation Rules

1. **Bibliography Add**: Requires evidence tier classification with rationale
2. **Hypothesis Link**: Must specify evidence type (supporting/contradicting/neutral)
3. **Vendor Score**: Capability score ≤ available evidence tier
4. **Expert Evidence**: Stored separately from literature evidence for disclosure

---

## Integration Points

### Upstream (Sources)
- Book manuscript (115,500 words) - chapter references
- Blog posts (56 drafted) - citation needs
- Expert network - interview coordination

### Downstream (Consumers)
- Security Architect MCP Server - vendor database sync
- Blog publishing workflow - evidence validation
- Publication readiness checker - quality gates

### Cross-Project Sync

```python
# Weekly sync schedule
SYNC_SCHEDULE = {
    "vendor_database": {
        "source": "literature-review/vendor-landscape/vendor-database.json",
        "target": "security-architect-mcp-server/data/vendor_database.json",
        "frequency": "weekly",
        "conflict_resolution": "literature-review-authoritative"
    }
}
```

---

## Implementation Roadmap

### Phase 1: Core Workflows (Week 1-2)
- [ ] Implement `bibliography_workflow`
- [ ] Implement `hypothesis_workflow`
- [ ] Create hypothesis-index.json from existing markdown
- [ ] Add Tool Output Schemas

### Phase 2: Expert Integration (Week 3)
- [ ] Implement `expert_interview_workflow`
- [ ] Create expert-evidence.json data model
- [ ] Interview guide templates

### Phase 3: Vendor Sync (Week 4)
- [ ] Implement `vendor_landscape_workflow`
- [ ] Bidirectional sync with Security Architect MCP
- [ ] Quarterly snapshot automation

### Phase 4: Verification (Week 5)
- [ ] Token usage measurement
- [ ] Before/after comparison
- [ ] Document H-MCP-CONTEXT-01 compliance

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Context reduction | >80% | Token counts before/after |
| Bibliography query time | <2s | Benchmark |
| Evidence distribution | ≥75% Tier A | Automated validation |
| Hypothesis coverage | 100% indexed | Data completeness |
| Expert evidence tracked | 100% interviews | Data completeness |

---

## References

- [H-MCP-CONTEXT-01](/home/USER/project1/01-knowledge-base/hypotheses/extended-hypotheses.md)
- [MCP 2025 Best Practices](/home/USER/project1/01-knowledge-base/concepts/mcp-2025-best-practices-implementation-patterns.md)
- [Genealogy MCP Server Spec](/home/USER/genealogy/.claude/mcp-server-spec.md) - Reference implementation

---

## Tags

#mcp #literature-review #evidence-management #hypothesis-tracking #context-efficiency
