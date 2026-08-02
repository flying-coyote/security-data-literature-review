---
type: essay-draft
title: "Appendix F: OCSF Implementation Guide & Field Mapping Reference"
created: 2025-12-15
tags: [moar-book, ocsf, field-mapping, implementation, semantic-validation]
---

# Appendix F: OCSF Implementation Guide & Field Mapping Reference

**Purpose**: Practical implementation patterns, tools, and field mapping methodology for adopting Open Cybersecurity Schema Framework (OCSF) normalization in your security data architecture.

**How to use**: This appendix provides step-by-step implementation guidance for the OCSF strategic framework introduced in Appendix H. Reference this appendix when actually building OCSF transformations for your log sources.

**Cross-Reference**: Appendix H provides strategic context (why OCSF, lock-in prevention, coalition dynamics). This appendix provides tactical implementation ("how to map Zeek logs to OCSF").

> **Version pin**: The class UIDs and field names in this appendix follow the OCSF v1.x schema the referenced CISA Zeek-OCSF project used, so read them as a worked example from that point in the schema's life rather than as the current contract. The current release as of this writing is OCSF v1.8.0 (March 2026), and the schema moves quickly enough that class UIDs, enum values, and field names drift between versions, so verify everything I use here against schema.ocsf.io before you build on it. Where a mapping rides on a specific value, I name the class (for example Network Activity, class_uid 4001) so you can re-check it against whatever version you are targeting.

---

## Section F.1: Three OCSF Implementation Approaches

**Decision framework**: Choose approach based on scale, resources, vendor support

### Approach 1: Manual Mapping

**When to use**:
- Small-scale: <5 log sources
- Deep customization required (unusual data formats, legacy systems)
- Learning OCSF schema (POC phase)
- Compliance requirement for human-reviewable transformations

**Process**:
1. Download log source schema (CSV export, API documentation, sample logs)
2. Read OCSF schema documentation (event classes, field definitions)
3. Create field mapping table: `source_field` → `ocsf_field` + semantic validation
4. Implement transformation (Python script, SQL view, Power Query M)
5. Test with sample data (validate OCSF schema compliance)
6. Peer review (domain expert validates semantic preservation)

**Effort**: 2-4 hours per log source (an illustrative planning figure that assumes an experienced engineer and a straightforward schema), which I use here as a rough estimate for sizing, not a measured rate

**Example**: Zeek conn.log → OCSF Network Activity (4001)

**Source schema** (Zeek conn.log):
```
ts, uid, id.orig_h, id.orig_p, id.resp_h, id.resp_p, proto, service, duration, orig_bytes, resp_bytes, conn_state, missed_bytes, history, orig_pkts, orig_ip_bytes, resp_pkts, resp_ip_bytes
```

**OCSF Network Activity schema** (subset):
```json
{
  "class_uid": 4001,
  "time": "timestamp",
  "src_endpoint": {
    "ip": "string",
    "port": "integer"
  },
  "dst_endpoint": {
    "ip": "string",
    "port": "integer"
  },
  "connection_info": {
    "protocol_num": "integer",
    "direction_id": "integer"
  },
  "traffic": {
    "bytes": "long",
    "packets": "long"
  }
}
```

**Field mapping table** (manual creation):

| Zeek Field | OCSF Field | Mapping Logic | Semantic Notes |
|------------|------------|---------------|----------------|
| `ts` | `time` | Unix timestamp → ISO 8601 | Direct conversion |
| `id.orig_h` | `src_endpoint.ip` | String (IP address) | Originator = source |
| `id.orig_p` | `src_endpoint.port` | Integer | Direct |
| `id.resp_h` | `dst_endpoint.ip` | String (IP address) | Responder = destination |
| `id.resp_p` | `dst_endpoint.port` | Integer | Direct |
| `proto` | `connection_info.protocol_num` | Map: tcp=6, udp=17, icmp=1 | IANA protocol numbers |
| `orig_bytes` | `traffic.bytes_in` | Long integer | **Semantic note**: `orig_bytes` = bytes FROM originator TO responder = ingress from perspective of destination |
| `resp_bytes` | `traffic.bytes_out` | Long integer | **Semantic note**: `resp_bytes` = bytes FROM responder TO originator = egress from perspective of destination |

**Python implementation** (simplified):
```python
import pandas as pd
from datetime import datetime

def zeek_conn_to_ocsf(zeek_df):
    """Transform Zeek conn.log to OCSF Network Activity 4001"""

    ocsf_df = pd.DataFrame({
        'class_uid': 4001,  # Network Activity
        'category_uid': 4,  # Network Activity category
        'time': zeek_df['ts'].apply(lambda x: datetime.fromtimestamp(x).isoformat()),
        'src_endpoint.ip': zeek_df['id.orig_h'],
        'src_endpoint.port': zeek_df['id.orig_p'],
        'dst_endpoint.ip': zeek_df['id.resp_h'],
        'dst_endpoint.port': zeek_df['id.resp_p'],
        'connection_info.protocol_num': zeek_df['proto'].map({'tcp': 6, 'udp': 17, 'icmp': 1}),
        'traffic.bytes_in': zeek_df['orig_bytes'],
        'traffic.bytes_out': zeek_df['resp_bytes'],
        'traffic.packets_in': zeek_df['orig_pkts'],
        'traffic.packets_out': zeek_df['resp_pkts']
    })

    return ocsf_df
```

**Pros**:
- Full control over transformation logic
- Deep semantic understanding built during manual mapping
- Human-reviewable (compliance requirement)
- No additional tools required (Python/SQL standard skills)

**Cons**:
- **Does not scale**: at the midpoint of the 2-4 hours/source above, call it 3 hours, 50 log sources works out to roughly 150 hours, on the order of 3-4 weeks full-time (arithmetic from the planning figure, not a measured project total)
- Error-prone (field name typos, semantic misalignment)
- Maintenance burden (OCSF schema updates require manual review + code changes)

**Best for**: Proof-of-concept, <10 sources, compliance-critical environments requiring human validation

---

### Approach 2: LLM-Assisted Mapping (The Default for Custom and Non-Standard Sources)

**When to use**:
- Medium-scale: 10-100 log sources
- Need speed + accuracy balance
- Team has SQL/Power Query skills (peer review capability)
- Transparent transformations required (FISMA, audit compliance)

**Process** (as applied in the CISA Zeek-OCSF project):

**Step 1: Prepare Source Schema CSV**
```csv
source_field,data_type,description
ts,timestamp,"Timestamp of connection start (Unix epoch)"
id.orig_h,string,"Originating host IP address (connection initiator)"
id.orig_p,integer,"Originating host port number"
id.resp_h,string,"Responding host IP address (connection receiver)"
id.resp_p,integer,"Responding host port number"
proto,string,"Transport layer protocol (tcp/udp/icmp)"
orig_bytes,integer,"Bytes sent from originator to responder"
resp_bytes,integer,"Bytes sent from responder to originator"
...
```

**Step 2: LLM Prompt for OCSF Mapping**

```
You are a cybersecurity data engineer creating OCSF (Open Cybersecurity Schema Framework) transformations.

Task: Map the following source schema to OCSF Network Activity (class_uid 4001).

Source schema (Zeek conn.log):
[CSV from Step 1]

OCSF Network Activity schema reference:
- class_uid: 4001 (Network Activity)
- time: ISO 8601 timestamp
- src_endpoint.ip: Source IP address
- src_endpoint.port: Source port
- dst_endpoint.ip: Destination IP address
- dst_endpoint.port: Destination port
- connection_info.protocol_num: IANA protocol number (tcp=6, udp=17, icmp=1)
- traffic.bytes_in: Bytes received by destination
- traffic.bytes_out: Bytes sent by destination

Requirements:
1. Generate Power Query M code for transformation
2. Include semantic validation comments for ambiguous mappings
3. Flag fields with confidence scores (High/Medium/Low)

Output format: Power Query M code with step-by-step transformations
```

**Step 3: LLM Output** (a capable frontier LLM; GPT-class or Claude-class, with specific models evolving over time):

```m
let
    // Load Zeek conn.log (tab-separated)
    Source = Csv.Document(File.Contents("conn.log"), [Delimiter="#x09", Columns=19]),

    // Rename columns to Zeek field names
    RenamedSource = Table.RenameColumns(Source,{
        {"Column1", "ts"},
        {"Column2", "uid"},
        {"Column3", "id.orig_h"},
        {"Column4", "id.orig_p"},
        {"Column5", "id.resp_h"},
        {"Column6", "id.resp_p"},
        {"Column7", "proto"},
        {"Column8", "service"},
        {"Column9", "duration"},
        {"Column10", "orig_bytes"},
        {"Column11", "resp_bytes"}
    }),

    // OCSF class identification
    AddedClassUID = Table.AddColumn(RenamedSource, "class_uid", each 4001),
    AddedCategoryUID = Table.AddColumn(AddedClassUID, "category_uid", each 4),

    // Time conversion (Unix timestamp → ISO 8601)
    AddedTime = Table.AddColumn(AddedCategoryUID, "time", each
        DateTime.ToText(#datetime(1970, 1, 1, 0, 0, 0) + #duration(0, 0, 0, [ts]), "yyyy-MM-ddTHH:mm:ss.fffZ"),
        type text
    ),

    // Source endpoint mapping (Confidence: High - direct semantic match)
    AddedSrcIP = Table.AddColumn(AddedTime, "src_endpoint.ip", each [#"id.orig_h"], type text),
    AddedSrcPort = Table.AddColumn(AddedSrcIP, "src_endpoint.port", each [#"id.orig_p"], Int64.Type),

    // Destination endpoint mapping (Confidence: High)
    AddedDstIP = Table.AddColumn(AddedSrcPort, "dst_endpoint.ip", each [#"id.resp_h"], type text),
    AddedDstPort = Table.AddColumn(AddedDstIP, "dst_endpoint.port", each [#"id.resp_p"], Int64.Type),

    // Protocol mapping (Confidence: High - IANA standard)
    AddedProtocol = Table.AddColumn(AddedDstPort, "connection_info.protocol_num", each
        if [proto] = "tcp" then 6
        else if [proto] = "udp" then 17
        else if [proto] = "icmp" then 1
        else null, // Unmapped protocols
        Int64.Type
    ),

    // Traffic mapping (Confidence: Medium - semantic validation required)
    // SEMANTIC VALIDATION NOTE:
    // Zeek "orig_bytes" = bytes FROM originator (source) TO responder (destination)
    // OCSF "traffic.bytes_in" = bytes received BY the asset (from perspective of dst)
    // Therefore: orig_bytes → bytes_in (bytes coming INTO destination)
    //
    // Zeek "resp_bytes" = bytes FROM responder (destination) TO originator (source)
    // OCSF "traffic.bytes_out" = bytes sent BY the asset (from perspective of dst)
    // Therefore: resp_bytes → bytes_out (bytes going OUT OF destination)
    //
    // PEER REVIEW REQUIRED: Verify semantic alignment matches your analysis requirements
    AddedBytesIn = Table.AddColumn(AddedProtocol, "traffic.bytes_in", each [orig_bytes], Int64.Type),
    AddedBytesOut = Table.AddColumn(AddedBytesIn, "traffic.bytes_out", each [resp_bytes], Int64.Type),

    // Select final OCSF columns
    SelectedColumns = Table.SelectColumns(AddedBytesOut,{
        "class_uid", "category_uid", "time",
        "src_endpoint.ip", "src_endpoint.port",
        "dst_endpoint.ip", "dst_endpoint.port",
        "connection_info.protocol_num",
        "traffic.bytes_in", "traffic.bytes_out"
    })
in
    SelectedColumns
```

**Step 4: Peer Review** (Domain Expert Validation)

Security analyst reviews LLM-generated transformation in Excel Power Query editor:
- Can see each transformation step (transparent)
- Validates semantic alignment (especially flagged Medium/Low confidence fields)
- Catches errors: "Wait, `orig_bytes` should map to `bytes_in`, but from whose perspective? Source or destination?"

Semantic validation catches the majority of the mapping errors that do slip through (an illustrative figure of roughly 80-85% based on the CISA Zeek-OCSF project experience, not a formally published rate). It helps to keep the two numbers in this appendix straight, because they measure different denominators: the 95% is overall mapping accuracy across the whole transformation, while the 80-85% is the share of the remaining errors that semantic validation catches, so the two are complementary rather than competing.
- Example error: LLM mapped Zeek `orig_bytes` → OCSF `traffic.bytes_out`, which is wrong because it should be `bytes_in`
- Human reviewer: "Originator bytes = bytes FROM source = bytes TO destination = bytes IN from destination perspective"
- Correction: `orig_bytes` → `traffic.bytes_in` ✓

**Step 5: Production Deployment**

Power Query M code → AWS Lambda (Python equivalent) or dbt (SQL equivalent) for production transformation pipeline.

**Effort**: 15-20 minutes per log source (an illustrative breakdown of LLM generation at 5 min plus peer review at 10-15 min), the working figure from the CISA Zeek-OCSF project's own accounting rather than an independently measured rate (Tier B, self-assessed)

**Comparison to manual** (illustrative, both figures from the planning estimates above):
- Manual: 2-4 hours per source
- LLM-assisted: 15-20 minutes per source
- **Speedup**: roughly 6-9× faster, the efficiency gain the CISA Zeek-OCSF project reported on its own work rather than the ratio of the two per-source estimates above, which run 6× to 16× on the endpoints (Tier B, self-assessed; not a measured benchmark)

Chapter 2 prices the same work at the better part of an engineer-year for a big deployment mapping hundreds of sources, which looks incompatible with the rate above until you notice the two figures cover different things. The chapter doesn't say which of the two approaches it prices, but its figure reads to me as the manual shape of the job, since 300 sources at 2 to 4 hours each is already 600 to 1,200 hours before you add the schema-learning time, the peer review, and the re-mapping that every OCSF release forces, none of which the per-source rate here includes. So read the 15 to 20 minutes as the marginal cost of one more source once a team is fluent, and read the engineer-year as what the program costs end to end.

**Accuracy**: roughly 95% field-mapping correctness, as reported by the CISA Zeek-OCSF project across 20 Zeek protocols (the CISA-facing power-query phase set this appendix describes; the repository's full unified set later grew to 101 protocols, so both counts are real in the source) and roughly 2,900 lines of M code; treat that as the project's own working figure (Tier B, self-assessed and illustrative, not an independently published rate) rather than a benchmark you can cite as measured. Appendix H deliberately speaks only directionally about this same project's accuracy, and I keep the worked numbers here because a tactical sizing guide needs planning figures, though they carry the same self-assessed status either way.

**Pros**:
- Scales: at the illustrative 20 minutes/source, 50 sources is roughly 16 hours, on the order of 2 days against the 3-4 weeks the manual estimate implies (arithmetic from the planning figures, not a measured project total)
- Accuracy: roughly 95% with semantic validation in the CISA project's own accounting (peer review catches most of the remainder); an illustrative working figure (Tier B, self-assessed), not a formally published rate
- Transparent: Power Query M is reviewable by non-programmers (an Excel user can validate)
- Maintainable: OCSF schema updates → re-run LLM prompt → updated transformations

**Cons**:
- Requires LLM access (a frontier API, GPT-class or Claude-class; on the order of $50-$200 total for 50 sources, which is a sizing estimate rather than a quoted price, since per-token pricing shifts over time)
- Peer review still required, because you cannot fully automate the semantic validation; that part stays a human judgment call
- Medium confidence fields need extra validation (illustratively on the order of a fifth to a third of fields, from the CISA project's experience rather than a published measurement)

**Best for**: 10-100 sources, enterprise deployments, government FISMA compliance (transparent transformations)

---

### Approach 3: Vendor Automation

**When to use**:
- Vendor provides pre-built OCSF mappings (AWS Security Lake, Splunk OCSF app)
- Standard log sources (CloudTrail, VPC Flow, Office 365, etc.)
- Time-to-value prioritized over customization

**Process**:
1. Enable vendor OCSF feature (AWS Security Lake native ingestion, Splunk app install)
2. Configure log source ingestion (point to S3 bucket, Azure Blob, etc.)
3. Vendor auto-maps to OCSF (black-box transformation)
4. Query OCSF-formatted data (Athena, Dremio, Splunk queries)

**Effort**: Minutes to hours (configuration only, no coding)

**Examples**:

**AWS Security Lake** (the OCSF class names and UIDs below are spec facts, so verify each against the OCSF schema at schema.ocsf.io for the version you target, since UIDs drift between releases):
- Natively ingests AWS sources in OCSF format:
  - CloudTrail → OCSF API Activity (class_uid 6003)
  - VPC Flow Logs → OCSF Network Activity (4001)
  - GuardDuty → OCSF Security Finding (2001)
  - Route 53 DNS → OCSF DNS Activity (4003)
- Third-party sources via OCSF custom source API

**Splunk OCSF App**:
- Bidirectional CIM ↔ OCSF mapping:
  - Ingest OCSF → Auto-normalize to CIM (existing detection rules work)
  - Export CIM → Transform to OCSF (cloud-native integrations)

**Pros**:
- Quickest path to a working pipeline (no transformation development)
- The vendor maintains the mappings, so schema updates are handled for you
- Tested at scale, with the vendor validating mappings against a large customer base (vendor claim, Tier C, not independently verified)

**Cons**:
- Limited customization (the vendor decides field mappings, and you cannot override them)
- Black box: no transparency into the transformation logic, which fails FISMA audit requirements
- Vendor lock-in risk, somewhat ironically: using AWS Security Lake OCSF creates an AWS dependency (mitigated if you export to an open table format like Apache Iceberg, where V3 features such as deletion vectors and row lineage have shipped and the V4 spec is still in flight)
- Coverage gaps: the vendor maps common sources only, so custom and legacy apps still require manual mapping

**Best for**: Standard log sources, fast POC, organizations without data engineering resources

---

**Decision matrix**:

| Approach | Sources | Effort | Transparency | Customization | Best Fit |
|----------|---------|--------|--------------|---------------|----------|
| **Manual** | <10 | 2-4 hr/src | ✓ Full | ✓ Complete | POC, compliance-critical, learning |
| **LLM-Assisted** | 10-100 | 15-20 min/src | ✓ Full | ✓ Complete | **Custom sources at enterprise scale (recommended)** |
| **Vendor** | Standard only | Min to hours | ✗ Black box | ✗ Limited | Fast POC, standard sources, no resources |

**Hybrid approach** (the split I most often see in practice, an author's assessment with illustrative proportions rather than a surveyed distribution):
- Vendor automation for the bulk of standard sources: CloudTrail, VPC Flow, Office 365, Azure AD
- LLM-assisted for custom sources: Application logs, custom tools, legacy systems
- Manual for the handful of critical or complex sources: Unusual schemas, compliance-sensitive, learning cases

**CISA Zeek-OCSF project**: 100% LLM-assisted (transparency requirement), 20 protocols in the power-query phase this appendix describes, roughly 2,900 lines M code, with the project reporting roughly 95% mapping accuracy on its own work (Tier B, self-assessed; an illustrative figure, not an independently published rate).

---

## Section F.2: Semantic Validation Framework

**Why semantic validation matters**:

Field names deceive you if you trust them, because `bytes` in one schema does not mean the same thing as `bytes` in another without the semantic definition behind it, and the names look identical right up until a detection rule fires on the wrong direction of traffic.

**Example failure**: Zeek conn.log → OCSF Network Activity

**Naive name-based mapping** (wrong):
- Zeek `orig_bytes` → OCSF `traffic.bytes_out` (both have "bytes", assume same)

**Semantic reality** (correct after validation):
- Zeek `orig_bytes` = "bytes sent FROM originator (source) TO responder (destination)"
- OCSF `traffic.bytes_out` = "bytes sent FROM the asset"
- **Question**: What is "the asset" in OCSF Network Activity? Source or destination?
- **OCSF definition**: Asset = destination (recipient of traffic)
- **Therefore**: `orig_bytes` (bytes TO destination) = `traffic.bytes_in` (bytes received BY destination), NOT `bytes_out`

**Without semantic validation**: Detection rule "alert on >1 GB outbound traffic" triggers on wrong field → false negatives (misses exfiltration) or false positives (alerts on download traffic).

Comparing field DESCRIPTIONS rather than names is what catches most mapping errors before they reach production. Of the errors that survive the LLM pass, the CISA Zeek-OCSF project experience suggests semantic validation catches roughly 80-85% (Tier B, self-assessed), which is best read as an illustrative order-of-magnitude rather than a formally published rate.

### 5-Step Semantic Validation Process

**Step 1: Document Source Semantics**

Don't rely on field names alone. Capture descriptions from vendor documentation.

**Zeek conn.log documentation** (excerpt):
```
orig_bytes (count): Bytes sent FROM originating endpoint TO responding endpoint.
               Does not include IP/TCP headers. Does include application payload.

resp_bytes (count): Bytes sent FROM responding endpoint TO originating endpoint.
               Does not include IP/TCP headers. Does include application payload.
```

**Step 2: Document OCSF Target Semantics**

Read OCSF schema definitions (GitHub schema repository, JSON Schema docs).

**OCSF Network Activity traffic object**:
```json
{
  "traffic": {
    "bytes_in": {
      "description": "The total number of bytes received by the endpoint",
      "type": "long"
    },
    "bytes_out": {
      "description": "The total number of bytes sent by the endpoint",
      "type": "long"
    }
  }
}
```

**Key semantic question**: What is "the endpoint" in OCSF Network Activity?

**Paraphrase of OCSF schema intent** (not a verbatim quotation; confirm against the live schema):
> Network Activity describes communication between two endpoints. The `src_endpoint` field identifies the initiator (connection originator), and `dst_endpoint` identifies the responder (connection receiver). Traffic metrics are measured from the perspective of the destination endpoint.

**Step 3: Compare Semantics (Not Names)**

Create semantic alignment table:

| Source Field | Source Semantic | OCSF Field | OCSF Semantic | Alignment |
|--------------|----------------|------------|---------------|-----------|
| `orig_bytes` | Bytes FROM originator TO responder | `traffic.bytes_in` | Bytes received BY endpoint (destination) | ✓ **MATCH**: Originator sends → Destination receives |
| `orig_bytes` | Bytes FROM originator TO responder | `traffic.bytes_out` | Bytes sent BY endpoint (destination) | ✗ **MISMATCH**: Originator sends ≠ Destination sends |
| `resp_bytes` | Bytes FROM responder TO originator | `traffic.bytes_out` | Bytes sent BY endpoint (destination) | ✓ **MATCH**: Responder (destination) sends |
| `resp_bytes` | Bytes FROM responder TO originator | `traffic.bytes_in` | Bytes received BY endpoint (destination) | ✗ **MISMATCH**: Responder sends ≠ Destination receives |

**Correct mapping**:
- `orig_bytes` → `traffic.bytes_in` ✓
- `resp_bytes` → `traffic.bytes_out` ✓

**Step 4: Flag Confidence Scores**

Not all mappings are unambiguous. Flag questionable alignments for peer review.

**Confidence categories** (the percentage bands below are an illustrative rubric for triaging mappings, not a measured semantic-similarity score):

**High Confidence** (90-100% semantic match):
- Example: Zeek `id.orig_h` → OCSF `src_endpoint.ip` (both mean "source IP address", no ambiguity)
- LLM mapping + schema definition alignment = high confidence
- **Action**: Accept mapping, light peer review

**Medium Confidence** (70-90% semantic match):
- Example: Zeek `proto` → OCSF `connection_info.protocol_num` (mapping logic required: "tcp" string → 6 integer, per IANA standard)
- Transformation logic beyond 1:1 field copy
- **Action**: Peer review validates transformation correctness

**Low Confidence** (<70% semantic match):
- Example: Zeek `weird.log` (protocol anomalies) → OCSF ??? (no direct equivalent in the CISA-era v1.x schema; check whether a later release added one)
- Multiple possible OCSF targets, unclear semantic fit
- **Action**: Domain expert review, consider OCSF schema extension proposal, or use `unmapped{}` object

**Step 5: Peer Review by Domain Expert**

**Who**: Security analyst or network engineer familiar with source data (not necessarily OCSF expert)

**What to review**:
- Medium/Low confidence mappings
- Fields with "semantic validation note" comments (from LLM-assisted approach)
- Transformation logic (not just field renames)

**Review questions**:
1. "Does this mapping preserve the meaning of the source field?"
2. "If I query OCSF field X, will I get the security insight I expect?"
3. "Are there any perspectives reversed?" (e.g., source vs destination viewpoint)

**Example peer review catch** (real error from CISA project):

**LLM-generated mapping**:
```m
// Zeek DNS: Map response code
AddedRcode = Table.AddColumn(Previous, "rcode", each
    if [rcode_name] = "NOERROR" then 0
    else if [rcode_name] = "NXDOMAIN" then 3
    else null
)
```

**Peer reviewer**:
> "Wait—OCSF DNS Activity has `rcode` field, but LLM mapped Zeek `rcode` (integer) and `rcode_name` (string) both to OCSF `rcode`. Which takes precedence? Also, Zeek provides both—should we include both in OCSF, or only one?"

**Resolution**:
- OCSF `rcode_id` = integer (DNS response code per RFC 1035)
- OCSF `rcode` = string (human-readable: "NOERROR", "NXDOMAIN")
- **Corrected mapping**: `rcode` → `rcode_id`, `rcode_name` → `rcode` ✓

Across the 20 Zeek protocols in the CISA project, semantic validation (comparing descriptions, not names) caught most of the mapping errors before production deployment. The roughly 80-85% figure is the share of the errors surviving the LLM pass that this step caught, and it is an illustrative, self-assessed estimate (Tier B) rather than a formally published CISA measurement.

---

## Section F.3: Common OCSF Mapping Challenges

Real-world schemas create four common mapping challenges. This section provides solutions.

### Challenge 1: One-to-Many Mappings

**Problem**: Single source field decomposes into multiple OCSF fields

**Example**: Zeek `id` (connection 4-tuple: source IP, source port, destination IP, destination port)

**Source schema** (Zeek):
```
id = { orig_h: "192.168.1.100", orig_p: 54321, resp_h: "10.0.0.5", resp_p: 443 }
```

**OCSF target** (Network Activity):
```json
{
  "src_endpoint": {
    "ip": "192.168.1.100",
    "port": 54321
  },
  "dst_endpoint": {
    "ip": "10.0.0.5",
    "port": 443
  }
}
```

**Solution**: Decomposition transformation with clear documentation

```m
// One-to-many: Zeek connection ID → OCSF endpoints
AddedSrcIP = Table.AddColumn(Source, "src_endpoint.ip", each [id][orig_h]),
AddedSrcPort = Table.AddColumn(AddedSrcIP, "src_endpoint.port", each [id][orig_p]),
AddedDstIP = Table.AddColumn(AddedSrcPort, "dst_endpoint.ip", each [id][resp_h]),
AddedDstPort = Table.AddColumn(AddedDstIP, "dst_endpoint.port", each [id][resp_p])
```

---

### Challenge 2: Many-to-One Mappings

**Problem**: Multiple source fields consolidate into single OCSF field

**Example**: Zeek DNS flags (AA, TC, RD, RA, Z) → OCSF `flag_ids[]` array

The integer flag IDs I use below are the kind of value that drifts between schema versions, so check them against the DNS Activity `flag_ids` enum in whatever release you are targeting before you rely on the specific numbers.

**Source schema** (Zeek dns.log):
```
AA=T, TC=F, RD=T, RA=T, Z=0
```

**OCSF target** (DNS Activity):
```json
{
  "flag_ids": [1, 3, 4],  // Array of set flags
  // OCSF DNS flag IDs: 1=AA (authoritative), 3=RD (recursion desired), 4=RA (recursion available)
}
```

**Solution**: Array consolidation with semantic preservation

```m
// Many-to-one: Zeek DNS flags → OCSF flag_ids array
AddedFlags = Table.AddColumn(Source, "flag_ids", each
    List.Select(
        {
            if [AA] = "T" then 1 else null,   // Authoritative Answer
            if [TC] = "T" then 2 else null,   // Truncated
            if [RD] = "T" then 3 else null,   // Recursion Desired
            if [RA] = "T" then 4 else null    // Recursion Available
        },
        each _ <> null  // Remove nulls (unset flags)
    ),
    type {Int64.Type}
)
```

---

### Challenge 3: No Direct OCSF Equivalent

**Problem**: Source field has no matching OCSF field in current schema version

**Example**: Zeek `weird.log` (protocol anomalies like "bad_TCP_checksum", "SYN_flood_detected")

**OCSF (CISA-era v1.x)**: No "Network Anomaly" event class existed when the CISA project ran, so anomalies like these had nowhere clean to land; check the current release (v1.8.0 as of this writing) to see whether a later version added one before you settle on a workaround.

**Options**:

**Option A: Use `unmapped{}` Object** (OCSF extension mechanism)
```json
{
  "class_uid": 4001,  // Network Activity
  "time": "2025-01-10T14:32:00Z",
  "src_endpoint": {...},
  "unmapped": {
    "zeek_weird_name": "bad_TCP_checksum",
    "zeek_weird_notice": true,
    "zeek_weird_peer": "192.168.1.100"
  }
}
```

**Pros**: Preserves all source data (no loss)
**Cons**: Not OCSF-standard (other tools may ignore `unmapped` fields)

**Option B: Map to Closest OCSF Field + Confidence Score**
```json
{
  "class_uid": 2001,  // Security Finding (closest approximation)
  "finding_info": {
    "title": "Zeek Protocol Anomaly: bad_TCP_checksum",
    "src": "zeek_weird",
    "confidence": 70  // Medium confidence mapping
  }
}
```

**Pros**: Uses OCSF standard field
**Cons**: Semantic mismatch (weird != security finding), requires interpretation

**Option C: Propose OCSF Schema Extension** (Community contribution)
1. Open GitHub issue in OCSF repository: "Proposal: Network Anomaly Event Class"
2. Describe use case (Zeek weird.log, Suricata anomaly.log, etc.)
3. Propose schema structure
4. TSC evaluates (30-day RFC period)
5. If approved, included in a future OCSF release

**Pros**: Improves OCSF for entire community
**Cons**: 3-6 month timeline (not immediate solution)

**Option D: Accept Data Loss** (Document what's lost)

For non-critical fields, accept they won't map to OCSF:
```text
# Transformation documentation:
# Source field "zeek_weird.notice_type" NOT mapped to OCSF (CISA-era v1.x; re-check against the current release)
# Rationale: No equivalent OCSF field, low security value (informational only)
# Risk: Protocol anomaly visibility reduced in OCSF queries
# Mitigation: Retain raw Zeek logs for 90 days (detailed forensics if needed)
```

**Pros**: Simplifies transformation
**Cons**: Data loss, potential blind spots

**Decision framework**:
- **High security value field** → Option A (unmapped) or Option C (propose extension)
- **Medium value field** → Option B (closest match) with confidence flag
- **Low value field** → Option D (accept loss) with documentation

---

### Challenge 4: OCSF Class Selection

**Problem**: Multiple OCSF event classes could represent same source event

**Example**: HTTP log (web traffic)

**Options**:
1. **Network Activity (4001)**: Generic network traffic
2. **HTTP Activity (4002)**: Protocol-specific HTTP class
3. **Web Resources Activity (6001)**: Web-focused activity

**Decision framework**:

**Prefer specific class** if exists:
- HTTP log → HTTP Activity (4002) ✓ (provides HTTP-specific fields: `http_request.method`, `http_response.code`, `http_request.url`)

**Use generic class** if no specific match:
- Unknown protocol → Network Activity (4001) (captures IP/port/bytes)

**Hybrid approach**: Base class + observables
```json
{
  "class_uid": 4001,  // Network Activity (base)
  "src_endpoint": {...},
  "observables": [
    {
      "name": "HTTP Request",
      "type_id": 23,  // URL observable
      "value": "https://example.com/api/endpoint"
    },
    {
      "name": "HTTP Method",
      "type_id": 99,  // Other observable
      "value": "POST"
    }
  ]
}
```

**Use when**: Specific class lacks needed fields, but want to preserve details via observables

**A query-portability cost rides along with this choice.** Putting detail into an `observables[]` list of structs is good for schema fidelity, but it quietly changes how portable the resulting hunt is across engines, and that is worth knowing before you commit a feed to it. I tested the natural OCSF observables question, "does any observable carry `type_id = 21`", against one byte-identical Parquet file with explicit ground-truth counts, giving each engine its fair best expression (Tier B, single machine; duckdb 1.5.3, datafusion 53.0.0, chdb 4.1.8, polars 1.41.2). Scalar struct access (`src_endpoint.port`, `dst_endpoint.ip`) and list cardinality (`len(observables)`) stayed portable, every engine read the same nested bytes and returned the same count, so the open read contract holds through one level of nesting. The list-of-struct field predicate is where it breaks. DuckDB (`list_filter` with a lambda), chDB (`arrayExists`), and Polars (`list.eval`) all expressed it and agreed on the count (250 for `type_id = 21`, 1000 for a value present in every row), but DataFusion 53.0.0 could not apply a per-element struct-field predicate inside a `WHERE` clause and errored with `Cannot access field at argument`, so the same hunt that runs on three engines does not run on the fourth without rewriting it as an `UNNEST` subquery. This is a concrete, measured reason teams flatten observables into their own columns or a side table before querying, trading some schema fidelity for query portability. The DataFusion result is a capability gap on this version rather than a law, so re-check it on upgrade.

---

**Mapping complexity summary** (the frequency and effort columns are illustrative planning figures from the CISA project's experience, not a published measurement, so use them to size work, not to benchmark):

| Challenge | Frequency (illustrative) | Recommended Approach | Effort Impact (illustrative) |
|-----------|-----------|---------------------|---------------|
| One-to-many | common | Decomposition (straightforward) | +2 min/field |
| Many-to-one | occasional | Array consolidation | +5 min/field |
| No OCSF equivalent | uncommon | `unmapped{}` or propose extension | +10 min/field |
| Class selection | Per log source (once) | Prefer specific, fallback generic | +5 min/source |

**Total effort impact** (illustrative, building on the LLM-assisted estimate above): roughly 15-20 minutes per source baseline plus another 5-10 minutes where complex mappings appear, so on the order of 20-30 minutes per log source as a planning estimate rather than a measured rate.

---

## Cross-References & Resources

**Appendix H** (Strategic Context):
- Section H.1: Schema lock-in problem ($6.9M migration cost example)
- Section H.2: OCSF coalition dynamics (multi-vendor Linux Foundation coalition; exact membership count not fixed, see H.2.1)
- Section H.3: Production validation (1+ PB/day deployments)
- Section H.5: Ontological foundation (D3FEND → CCO → BFO)
- Section H.6: When OCSF may not fit your use case

**Related Appendices**:
- Appendix C: MOAR reference architectures (with OCSF integration)
- Appendix D: Glossary (security ↔ data engineering terminology, including OCSF terms)
- Appendix E: Resource directory (OCSF learning resources)

**External Resources**:
- OCSF GitHub Repository: https://github.com/ocsf/ocsf-schema
- OCSF Documentation: https://schema.ocsf.io/
- OCSF Slack Community: https://ocsf.io
- AWS Security Lake OCSF Integration: https://docs.aws.amazon.com/security-lake/

**Implementation Tools**:
- Power Query M (Excel, Power BI): LLM-assisted transformation development
- dbt (Data Build Tool): SQL-based transformation for production pipelines
- Apache Spark: Scale transformations for petabyte-scale data
- Python pandas: Prototyping and custom transformation logic
- AWS Lambda: Serverless transformation execution

---

Whichever of the three approaches you pick, the part that decides whether the mapping is right is the same: comparing field descriptions instead of field names, and getting a human who knows the source data to sign off on the perspective-sensitive fields before anything reaches a detection rule. That is the step that survives schema version changes, vendor mapping updates, and the next log source you add, so it is worth building into the pipeline rather than treating as a one-time review.

**Next**: Use Appendix H for the strategic decision (should we adopt OCSF at all?), then come back here for the tactical work (how do we actually map our logs?).
