# Living Literature Review: Quarterly Technology State Assessment

**Purpose**: IT Harvest-powered vendor landscape with quarterly updates
**Cadence**: Quarterly (Jan, Apr, Jul, Oct)
**Integration**: Book Chapter 9, blog references, practitioner navigation

---

## Structure

### platforms/
- `query-engines.md`: Trino/Starburst, Dremio, Denodo, Athena
- `olap-analytics.md`: ClickHouse, StarRocks/Celerdata, Druid
- `hybrid-architectures.md`: Spark + Query Engine patterns

### infrastructure/
- `table-formats.md`: Iceberg, Delta, Hudi (trend analysis)
- `catalogs.md`: Gravitino, Polaris, Unity, Nessie
- `object-storage.md`: S3, MinIO, Azure Blob

### security-specific/
- `ocsf-adoption.md`: Quarterly tracking
- `detection-platforms.md`: Security analytics evolution
- `threat-intel-integration.md`: TI platform updates

### vendor-landscape/ (IT Harvest powered)
- `capability-matrix.md`: Platform capabilities by category
- `market-trends.md`: Quarterly trend analysis
- `quarterly-updates/`: YYYY-QX-update.md files

---

## Update Process

**Quarterly Cycle**:
1. **Month 1**: IT Harvest data refresh + platform updates
2. **Month 2**: Expert validation + blog synthesis
3. **Month 3**: Publication + citation updates

**Version Control**:
- Each update creates new `YYYY-QX-update.md`
- CHANGELOG.md tracks all revisions
- Enables academic citation of specific versions

**Sources**:
1. IT Harvest vendor data (primary)
2. Blog post insights (ongoing)
3. Expert network validation (Lisa Chao, Jake Thomas, etc.)
4. Matthew Mullins + practitioner feedback

---

## Integration Points

**Book Chapter 9**: "Technology State Assessment"
**Blog**: Deep-dives feed quarterly synthesis
**IT Harvest**: Vendor data powers landscape updates
**Expert Network**: Validation and trend insights

---

**Status**: Structure created, awaiting IT Harvest partnership
**Next Action**: Pilot with query engines category (Week 4)
**Source**: Archive + IT Harvest + expert validation
