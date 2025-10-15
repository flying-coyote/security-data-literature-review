# Security-Specific Data Platforms

## Purpose
Track security-specific technologies including detection platforms, threat intelligence integration, and security telemetry standards (OCSF).

## Update Cadence
**Quarterly Updates** (January, April, July, October)

## Contents

### ocsf-adoption.md
- **OCSF (Open Cybersecurity Schema Framework)**: Adoption tracking
- **Schema Evolution**: Version updates, new event classes
- **Vendor Support**: Platform integrations, transformation tools
- **Focus**: Standardization progress, interoperability improvements

### detection-platforms.md
- **Security Analytics Evolution**: SIEM → Security Data Lake → Detection Engineering platforms
- **Modern Detection Stacks**: ClickHouse, Trino, Iceberg-based architectures
- **Query Performance**: Sub-second detection queries, real-time correlation
- **Focus**: Platform capabilities, cost efficiency, detection engineering workflows

### threat-intel-integration.md
- **TI Platform Updates**: MISP, OpenCTI, ThreatConnect evolution
- **Lakehouse Integration**: Streaming threat feeds into data lakehouses
- **Enrichment Patterns**: Real-time vs. batch enrichment architectures
- **Focus**: Integration patterns, data quality, false positive reduction

## Quality Standards
- **Evidence Level A Priority**: Government sources (CISA, MITRE, NSA), production security deployments
- **Security Domain Expertise**: Validated by security practitioners
- **Quantitative Metrics**: Detection performance, cost comparisons, adoption rates
- **Vendor-Neutral**: Balanced analysis of commercial and open-source options

## Sources
1. **Government/Standards**: CISA, MITRE ATT&CK, NSA, NIST, SANS
2. **Security Practitioners**: Shell SIEM team, SK Telecom, production deployments
3. **Security Vendors**: Vendor documentation (Level B evidence)
4. **Blog Integration**: security-data-commons-blog security deep-dives
5. **Expert Network**: Lisa Chao, Jake Thomas, Paul Agbabian validation

## Integration with Book
Supports:
- Chapter 7 "Detection Engineering with Data Lakehouses"
- Chapter 8 "Streaming Security Telemetry" (Kafka Streams patterns)
- Chapter 10 "OCSF Implementation Guide"

---
**Last Updated**: October 15, 2025 (directory initialization)
