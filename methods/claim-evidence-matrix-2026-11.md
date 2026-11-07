# Claim-to-evidence matrix, seven-chapter book (2026-11-07)

Built for the phase 1 lit-review upgrade (plan lane D). The index is the footnotes in the seven chapter drafts in `~/modern-data-stack-for-cybersecurity-book` (`part-1-so-what/` ch01-ch02, `part-2-what-now/` ch03-ch07), 75 footnotes as of 2026-11-07 (the upgrade plan's figure of 73 was two short), plus a short, bounded list of unfootnoted strong claims per chapter. Each row joins the chapter's own tier label to the bibliography entry, where there is one, in the chapter numbering of `methods/chapter-remap-2026-11.md`.

## How to read it

- **Chapter tier label(s)** are the "Tier X" strings in the footnote text, extracted by script; a footnote can carry more than one (a lab derivation over a Tier A ontology reads "BA").
- **Load** is a judgment: H means the chapter's argument leans on the claim (a headline figure, a section's thesis, a recommendation), M supporting, L colour or attribution.
- **Thin** means a load-carrying or supporting claim whose only legs are first-hand, first-party lab, modeled, vendor or social-media sources, so it has no peer-reviewed or standards leg. That is a statement about the kind of evidence, not about whether the claim is true: much of the book's strongest evidence is first-party lab work, which is Tier B by rule and often the only measurement that exists. "THIN → closed" means a Tier A source admitted on 2026-11-07 now supports the claim's mechanism; the scope limit in each admitted entry says how far.
- **First-hand and composite rows** (anonymized practitioner accounts, composite personas) are deliberately Tier B or modeled; the owner decides which of those he wants evidenced and which stay first-person.

## Summary

| Chapter | Footnotes | Tier A labels | Load-carrying | Load-carrying with no A leg (after this pass) | Thin flagged | Thin closed today | Unfootnoted strong claims |
|---|---|---|---|---|---|---|---|
| ch01 | 9 | 1 | 3 | 2 | 3 | 1 | 0 |
| ch02 | 7 | 0 | 3 | 3 | 5 | 0 | 1 |
| ch03 | 10 | 1 | 6 | 3 | 7 | 2 | 1 |
| ch04 | 15 | 4 | 4 | 3 | 3 | 0 | 0 |
| ch05 | 14 | 1 | 5 | 3 | 5 | 2 | 1 |
| ch06 | 14 | 1 | 3 | 3 | 6 | 0 | 1 |
| ch07 | 6 | 1 | 2 | 2 | 3 | 0 | 0 |
| **Total** | 75 | 9 | 26 | 19 | 32 | 5 | 4 |

## The thinnest claims (for the scouting decision)

Ranked by load and by how far the current evidence sits from a peer-reviewed or standards leg. These are the rows the main session can point the ≤20 Flash calls at, and none has been scouted yet.

1. **ch03, ~30% of production security data unusable** (unfootnoted; figure caption Tier B first-hand). No external leg of any tier; the chapter's tl;dr repeats it. The literature that exists measures adjacent things (parser template accuracy, IDS dataset defects, alert base rates in Yang et al.), so the honest outcome may be a scoped corroboration rather than a matching figure.
2. **ch02, the SIEM-versus-object-storage cost multiple** (desk calc C, lab B, vendor corroborations C). Durner et al. supports reading from object storage, not the price ratio; a peer-reviewed cost-of-storage-tier study for log or security data is the gap.
3. **ch07, "well over half, often two-thirds" of migration work is organizational** (author model). Kokulu et al. now supports the kind of issue, not the share.
4. **ch07, rule triage 800 → ~400 with a dead tail of noise** (first-hand). NoDoze admitted; Julisch (TISSEC 2003) held pending a primary read is the closer fit.
5. **ch03 §3.1, data-quality dimensions** (DAMA, B). Wang & Strong (JMIS 1996) held pending a primary read.
6. **ch03, vendor field mappings wrong by construction / PR #294** (first-hand). No peer-reviewed measurement of vendor parser or add-on field completeness was found in the walk.
7. **ch04, timezone/offset loss collapses correlation recall** and **context collapse under OCSF truncation** (lab B). No peer-reviewed leg on timestamp normalization in security log correlation was found.
8. **ch01, ~80% of data-science time is data preparation** (CrowdFlower survey, C). Kandel et al. (TVCG 2012) is a candidate for the mechanism; a peer-reviewed time-share figure is the gap.
9. **ch06, keep-the-SIEM binding conditions and the composite cost figures** (modeled). These are modeled by design; evidence would be a peer-reviewed SOC staffing or SIEM-TCO study.
10. **ch05 §5.3a, point lookups on lakes** (LinkedIn C, Spotify blog B). A peer-reviewed secondary-index-on-Parquet or lake point-lookup evaluation is the gap.

Two tier-label mismatches found in passing, for the book repo rather than this one: `conway-ch7` labels *Datamation* (1968) Tier A, which §3.1 would call B; `sigma` labels the SigmaHQ specification Tier A, which is generous for a community specification.

## ch01: You're doing data engineering without the tools for it

9 footnotes; 1 carry a Tier A label; 3 are load-carrying (H); 2 load-carrying footnotes still have no peer-reviewed or standards leg after this pass; 3 flagged thin, of which 1 gained an admitted Tier A leg on 2026-11-07.

| Footnote | Section | Claim | Current source(s) | Chapter tier label(s) | Bibliography | Load | Thin? | New or candidate leg / notes |
|---|---|---|---|---|---|---|---|---|
| `csf` | 1.1 You're already doing data engineerin | Security is ~twenty kinds of work (CSF 2.0: 6 functions, 22 categories) | NIST CSF 2.0 | A | in bib, A | M | - | - |
| `wrangle` | 1.1 You're already doing data engineerin | ~80% of data-science work is data preparation | CrowdFlower 2016 survey | C | not in bib | H | THIN | Kandel et al. TVCG 2012 (candidate, mechanism not figure) |
| `bonifield-ch1` | 1.1 You're already doing data engineerin | Pulling data out of the SIEM to wrangle it is ad hoc data engineering | Bonifield, No Starch 2025 | B | in bib, B | L | - | - |
| `reed-ch1` | 1.4 Complexity is the natural enemy of s | Possible subgroups roughly double with each added system | Reed 1999 essay | B | not in bib | M | - | - |
| `schneier-ch1` | 1.4 Complexity is the natural enemy of s | "Complexity is the worst enemy of security" | Schneier 1999 essay | B | not in bib | H | THIN | Shin et al. IEEE TSE 2011 (candidate) |
| `venables-ch1` | 1.4 Complexity is the natural enemy of s | Complexity is not the enemy; bad design is | Venables 2021 blog | B | not in bib | M | - | - |
| `geer-ch1` | 1.4 Complexity is the natural enemy of s | Complexity hides interdependence, the source of surprises | Geer 2018 Hoover paper | B | not in bib | M | - | - |
| `laws-ch1` | 1.4 Complexity is the natural enemy of s | Network value grows ~n log n, not Reed's 2^n | Briscoe, Odlyzko, Tilly, IEEE Spectrum 2006 | B | not in bib | L | - | - |
| `chuvakin-ch1` | 1.5 The debt is mostly already paid | SIEM problems are people/process/organization problems, not technology | Chuvakin via LinkedIn quotation | B | related Chuvakin entry B; this quote not catalogued | H | THIN → closed | Kokulu et al. CCS 2019 (ADMITTED A) |

## ch02: MOAR explained

7 footnotes; 0 carry a Tier A label; 3 are load-carrying (H); 3 load-carrying footnotes still have no peer-reviewed or standards leg after this pass; 5 flagged thin, of which 0 gained an admitted Tier A leg on 2026-11-07.

| Footnote | Section | Claim | Current source(s) | Chapter tier label(s) | Bibliography | Load | Thin? | New or candidate leg / notes |
|---|---|---|---|---|---|---|---|---|
| `bonifield-ch2` | 2.2 The components | The coupled Logstash-into-Elasticsearch build is still the default | Bonifield 2025 | B | in bib, B | L | - | - |
| `revrun` | 2.4 Why swappable is what makes it safe | Every swapped tier returns the identical answer | SDW MOAR reversibility run (first-party) | B | first-party lab | H | THIN (first-party only) | - |
| `zeekdemo` | 2.4 Why swappable is what makes it safe | Status docs drifted from what actually ran | First-hand, private build | B | first-party | L | - | - |
| `cost-desk-ch2` | 2.3 The economics | SIEM vs object-storage cost conversation; multiplier depends on retention | Splunk G-Cloud 14 pricelist + AWS list prices (desk calc) | C | G-Cloud anchor inside a C entry | H | THIN | Durner et al. PVLDB 2023 (ADMITTED A, mechanism only; no price ratio) |
| `cost-floor-ch2` | 2.3 The economics | Hot index ~14.8x warm Iceberg/S3 and ~96.7x cold Glacier on storage | SDW Lab cost-to-serve (first-party) | B | first-party lab | H | THIN (first-party only) | Durner et al. PVLDB 2023 (context) |
| `cost-corroboration-ch2` | 2.3 The economics | Production migrations report 60-80% SIEM cost cuts | Rivian, Navan and others (vendor-published) | CC | in bib, C | M | THIN | - |
| `catalogwrites` | 2.4 Why swappable is what makes it safe | Two catalogs writing one table silently orphan data; one catalog owns writes | Yaseen LinkedIn post | B | not in bib | M | THIN | - |

Unfootnoted strong claims:

| Location | Claim | Current support | Load | Gap |
|---|---|---|---|---|
| §2.3 | The SIEM-versus-object-storage cost multiple as the reason the cost conversation exists | Desk calc (C) + first-party lab (B) + vendor corroborations (C) | H | THIN: no peer-reviewed or standards leg on the multiple itself; Durner et al. (A) supports only the object-storage-read mechanism |

## ch03: Trustworthy security data

10 footnotes; 1 carry a Tier A label; 6 are load-carrying (H); 3 load-carrying footnotes still have no peer-reviewed or standards leg after this pass; 7 flagged thin, of which 2 gained an admitted Tier A leg on 2026-11-07.

| Footnote | Section | Claim | Current source(s) | Chapter tier label(s) | Bibliography | Load | Thin? | New or candidate leg / notes |
|---|---|---|---|---|---|---|---|---|
| `dq-dims` | 3.1 Security data is still data | Security data failures are ordinary data-quality dimensions | DAMA-DMBOK2 | B | not in bib | H | THIN | Wang & Strong JMIS 1996 (held candidate) |
| `golden` | 3.1 Security data is still data | Watch the pipeline with the four golden signals | Google SRE book | B | related SRE entry B | L | - | - |
| `pr294-ch3` | Story time | Vendor spec, emitted data and third-party add-on drift apart | First-hand PR #294 | B | not in bib (first-hand) | H | THIN | - |
| `petrescu-ch3` | Story time | Bad parsing logic: parsers look accurate under the usual metric and are not | Petrescu et al. ISSRE 2023 | A | in bib, A | H | - | Zhu et al. ICSE-SEIP 2019 (ADMITTED A, the benchmark being corrected) |
| `antipattern` | 3.3 Vendors are routinely confidently wr | Field mapping can be wrong by construction; verify by measurement | First-hand, anonymized | B | not in bib (first-hand) | H | THIN | - |
| `mojibake-ch3` | 3.2 What trust means: source, flow, and  | Misread code page looked like foreign-language content | First-hand | B | first-hand | L | - | - |
| `equiv-ch3` | 3.4 The silent wrong answer | 11 of 12 engines matched on identical Parquet; chDB 4.1.8 undercounted | SDW Lab answer-equality scorecard | B | first-party lab | H | THIN → closed | Rigger & Su OOPSLA 2020 (ADMITTED A) |
| `sqlsem` | 3.4 The silent wrong answer | Same SQL, same bytes, different counts across engines (NULL/timezone) | SDW Lab null/coercion/timezone run | B | first-party lab | H | THIN → closed | Rigger & Su OOPSLA 2020 (ADMITTED A, three-valued-logic mechanism) |
| `nl2sql` | 3.4 The silent wrong answer | Small local NL2SQL models produce silent errors | SDW Lab NL2SQL silent-error bench | B | first-party lab | M | THIN | - |
| `flatten-ch3` | 3.6 The tests, in one place | Floating timestamps break cross-source correlation | SDW Lab flattening-fidelity | BB | first-party lab | M | THIN | - |

Unfootnoted strong claims:

| Location | Claim | Current support | Load | Gap |
|---|---|---|---|---|
| §Story time, l.29-37; tl;dr l.167; figure ch03-quality-donut | Roughly 30% (about a third) of production security data reviewed is unusable quality, none of it erroring | First-hand practitioner observation, Tier B in the figure caption | H | THINNEST: no external leg of any tier; Petrescu (A) supports the parser mechanism, never the share |

## ch04: Well-connected security data

15 footnotes; 4 carry a Tier A label; 4 are load-carrying (H); 3 load-carrying footnotes still have no peer-reviewed or standards leg after this pass; 3 flagged thin, of which 0 gained an admitted Tier A leg on 2026-11-07.

| Footnote | Section | Claim | Current source(s) | Chapter tier label(s) | Bibliography | Load | Thin? | New or candidate leg / notes |
|---|---|---|---|---|---|---|---|---|
| `pr294-ch4` | Story time | The parser, not the feed, is where the join key goes wrong | First-hand PR #294 | B | first-hand | M | - | - |
| `lambert-ch4` | 4.1 D3FEND: security's ontology | Defenders think in lists, attackers in graphs | Lambert 2015 blog | B | not in bib | M | - | Sheyner et al. IEEE S&P 2002 (candidate) |
| `bonifield-ch4` | 4.2 Open Cybersecurity Schema Framework  | ECS normalization keeps the join inside one index | Bonifield 2025 | B | in bib, B | L | - | - |
| `mccomb` | 4.2 Open Cybersecurity Schema Framework  | Start with a small extensible model and extend as sources arrive | McComb 2019 book | B | in bib, B | M | - | - |
| `tz` | 4.2 Open Cybersecurity Schema Framework  | Dropping the offset drops correlation recall from 1.00 to ~0.46-0.50 | SDW Lab flattening-fidelity | B | first-party lab | H | THIN | - |
| `d3fend` | 4.1 D3FEND: security's ontology | OCSF carries the D3FEND link in-schema | MITRE D3FEND 1.0/1.4.0; OCSF v1.3.0 | A | in bib, A | H | - | - |
| `wall-ch4` | 4.1 D3FEND: security's ontology | ATT&CK-to-D3FEND artifact join yields one connected map | Derived from D3FEND 1.4.0 export | BA | B derivation over A | M | - | - |
| `atlas-ch4` | 4.1 D3FEND: security's ontology | ATLAS: 0 of 140 techniques integrated vs 40.8% for ATT&CK Enterprise | MITRE coverage dashboard run | B | first-party run of MITRE tooling | M | - | - |
| `madani-ch4` | 4.1 D3FEND: security's ontology | An artifact edge says a defense is relevant, not that it would stop the attack | Madani et al. C&ESAR 2026 | B | in bib, B (pending proceedings) | M | - | - |
| `sigma` | 4.3 Sigma: portable detections so logic  | One Sigma rule compiles to ~30 backends | SigmaHQ spec, pySigma | AB | spec A in footnote; Sigma not a standalone bib entry | M | - | Tier label check: SigmaHQ is a community specification, not a standards-body standard; A on the spec is generous under §3.1. - |
| `method-ch4` | 4.4 Verify the connection | Verify mappings deductively, not by trusting the integration | First-hand method run | B | first-hand | M | - | - |
| `datahealth-ch4` | 4.5 Cover the sources, not just the fiel | Some asset attributes are held by no source at all; merges cannot recover them | SDW Lab assurance-gap bench | B | first-party lab | H | THIN | - |
| `context-ch4` | 4.2 Open Cybersecurity Schema Framework  | OCSF truncation costs detection recall on real APT29 data | SDW Lab context-collapse bench | B | first-party lab | H | THIN | - |
| `tenable-ch4` | Story time | Vulnerability data present but unusable at the parsing handoff | First-hand, anonymized | B | first-hand | M | - | - |
| `bfo-ch4` | 4.1 D3FEND: security's ontology | OCSF/D3FEND inherit BFO's continuant/occurrent split | ISO/IEC 21838-2:2021 (+ Tier D reading) | AD | in bib, A | M | - | - |

## ch05: Performant security data

14 footnotes; 1 carry a Tier A label; 5 are load-carrying (H); 3 load-carrying footnotes still have no peer-reviewed or standards leg after this pass; 5 flagged thin, of which 2 gained an admitted Tier A leg on 2026-11-07.

| Footnote | Section | Claim | Current source(s) | Chapter tier label(s) | Bibliography | Load | Thin? | New or candidate leg / notes |
|---|---|---|---|---|---|---|---|---|
| `largescan` | Story time: does Iceberg really read slo | Iceberg looked 1.1-1.55x slower on first pass (confounded) | SDW Lab ocsf-read-scan | B | first-party lab | M | - | - |
| `samecodec` | Story time: does Iceberg really read slo | ~1.7x size gap is writer encoding, not codec | SDW Lab ocsf-read-scan | B | first-party lab | H | THIN → closed | Zeng et al. PVLDB 2023; BtrBlocks SIGMOD 2023 (ADMITTED A) |
| `parity` | Story time: does Iceberg really read slo | Byte-identical files read at parity through Iceberg and DuckLake | SDW Lab same-files arm | B | first-party lab | H | THIN (first-party only) | LHBench CIDR 2023 already in bib (A) as context |
| `storage` | 5.1 The table format is read-neutral, an | Matched codec: DuckLake files smaller than Iceberg's | SDW Lab parity arm | B | first-party lab | M | - | - |
| `writerlever` | 5.1 The table format is read-neutral, an | The writer is the read lever | SDW Lab writer-read-lever | B | first-party lab | H | THIN → closed | Zeng et al. PVLDB 2023 (ADMITTED A) |
| `bakeoff` | 5.3 Match the engine to the workload, th | ClickHouse over Iceberg 10.1x faster than OpenSearch schema-on-read | SDW Lab zeek-flagship-rerun (+ production corroboration entry) | BBB | first-party lab; corroboration B | H | THIN (no peer-reviewed leg) | Durner et al. PVLDB 2023 (context) |
| `shapes` | 5.3 Match the engine to the workload, th | Query shape changes which engine wins | SDW Lab soc-query-shapes | B | first-party lab | M | - | - |
| `equiv-ch5` | 5.4 Performant does not mean correct | Fast and correct are different properties | SDW Lab scorecard (pointer to ch03) | B | first-party lab | M | - | Rigger & Su OOPSLA 2020 (ADMITTED A) |
| `tworegime` | 5.3 Match the engine to the workload, th | Index wins lookups and text; columnar wins heavy aggregation | SDW Lab two-regime legs | B | first-party lab | H | - | Access Path Selection SIGMOD 2017 already in bib (A) |
| `kumar` | 5.3a Which engine for which question | Scan-oriented lakes are weak at point lookups | Kumar LinkedIn post | C | not in bib | M | THIN | - |
| `rap` | 5.3a Which engine for which question | Dependent reads bottleneck lake point queries; index proposals | Spotify engineering blog; Iceberg dev list | BB | related entry B | M | - | - |
| `streamcx` | 5.3a Which engine for which question | Streaming bought ~3 s median freshness over batch | SDW Lab stream-complexity | BB | first-party lab | M | - | - |
| `streamfresh` | 5.3a Which engine for which question | Streaming keeps a structural freshness edge at file-size boundaries | SDW Lab freshness run | B | first-party lab | M | - | - |
| `ivm` | 5.3a Which engine for which question | Incremental view maintenance as the third answer between batch and streaming | DBSP PVLDB 2023 | ACDB | in bib, A | M | - | - |

Unfootnoted strong claims:

| Location | Claim | Current support | Load | Gap |
|---|---|---|---|---|
| tl;dr l.138 | Open Parquet read by a fast columnar engine matches or beats the proprietary indexed store on heavy aggregations | Summary of the ch05 lab legs (B) | H | THIN on peer review: lab-only; Durner, Zeng and BtrBlocks (A) support adjacent mechanisms |

## ch06: MOAR variants

14 footnotes; 1 carry a Tier A label; 3 are load-carrying (H); 3 load-carrying footnotes still have no peer-reviewed or standards leg after this pass; 6 flagged thin, of which 0 gained an admitted Tier A leg on 2026-11-07.

| Footnote | Section | Claim | Current source(s) | Chapter tier label(s) | Bibliography | Load | Thin? | New or candidate leg / notes |
|---|---|---|---|---|---|---|---|---|
| `vt-ch6` | 6.5 The honest case: when to keep the SI | Keep-the-SIEM case: months-deep retro-hunt on existing Splunk | First-hand | B | first-hand | M | - | - |
| `marcus` | Story time | Composite: ~71% projected cost cut vs expanding the SIEM | Composite persona (Appendix K.2) | none | modeled | H | THIN (modeled) | - |
| `splunk` | Story time | Splunk ships >2,000 pre-built detections | splunk/security_content repo count | B | not in bib | M | - | - |
| `jennifer` | 6.1 The sovereignty variant: when data c | Composite: Dremio hybrid ~$380K/yr vs ~$1.6M/yr SIEM | Composite persona | C | modeled, C | M | THIN (modeled) | - |
| `priya` | 6.1 The sovereignty variant: when data c | Composite: Denodo virtualization keeps regulated data in region | Composite persona | none | modeled | M | THIN (modeled) | - |
| `cloud` | 6.2 The cloud-commitment variant: when t | Composite: AWS-native $3.47M/yr all-in vs ~$12M SIEM expansion | Appendix K.2 model | none | modeled | H | THIN (modeled) | - |
| `storeclass` | 6.2 The cloud-commitment variant: when t | ClickHouse tighter bytes still ~3.3x costlier per month on gp3 | SDW Lab cost-to-serve | B | first-party lab | M | - | - |
| `dnb` | 6.3 The multi-engine variant: the defaul | A named bank runs a multi-engine Iceberg stack | DNB talk/case | B | in bib, B | M | - | - |
| `interference` | 6.3 The multi-engine variant: the defaul | Interactive p95 holds to 32x load then breaks at 64x | SDW Lab workload-interference | B | first-party lab | M | - | - |
| `multiengine` | 6.3 The multi-engine variant: the defaul | Composite five-engine environment, illustrative ranges | Composite model | none | modeled | L | - | - |
| `equiv-ch6` | 6.3 The multi-engine variant: the defaul | Swappability is a property you check | SDW Lab scorecard (pointer) | B | first-party lab | M | - | Rigger & Su OOPSLA 2020 (ADMITTED A) |
| `siemwins` | 6.5 The honest case: when to keep the SI | Four binding conditions make the SIEM the right answer | Author model + lit-review staffing calculator | none | modeled | H | THIN | - |
| `streamlab` | 6.5 The honest case: when to keep the SI | Streaming cost sits in running/recovering infra, not writing it | SDW Lab stream-complexity | B | first-party lab | M | - | - |
| `governance` | 6.3 The multi-engine variant: the defaul | No cross-engine governance standard is enforced yet | Snowflake engineering blog (vendor) + Iceberg REST spec | CA | not in bib; C | M | THIN | Footnote carries A for the Iceberg REST spec and C for the vendor blog. - |

Unfootnoted strong claims:

| Location | Claim | Current support | Load | Gap |
|---|---|---|---|---|
| §6.4 l.101 | The hybrid pattern saves roughly 10% against a full-volume SIEM at 2 TB/day | Appendix A.6 model | M | THIN (modeled only) |

## ch07: Modularity

6 footnotes; 1 carry a Tier A label; 2 are load-carrying (H); 2 load-carrying footnotes still have no peer-reviewed or standards leg after this pass; 3 flagged thin, of which 0 gained an admitted Tier A leg on 2026-11-07.

| Footnote | Section | Claim | Current source(s) | Chapter tier label(s) | Bibliography | Load | Thin? | New or candidate leg / notes |
|---|---|---|---|---|---|---|---|---|
| `mccomb-ch7` | 7.4 Routing around the barriers, includi | Assign 3-5 people for 3-5 years to data centrality | McComb 2019 | B | in bib, B | L | - | - |
| `s3-ch7` | 7.3 Sequence it one source and one workl | Open Parquet on S3 at ~$0.023/GB-month makes run-alongside affordable | AWS list price | none | not in bib (price anchor) | M | - | - |
| `migration-model-ch7` | Story time | Over half (often two-thirds) of migration work is organizational | Author model, practitioner interviews | none | modeled | H | THIN | Kokulu et al. CCS 2019 (ADMITTED A, kind not share) |
| `800rules-ch7` | 7.3 Sequence it one source and one workl | Triage 800 rules to ~400; dead tail removed ~75 alerts/day | First-hand, anonymized | B | first-hand | H | THIN | NoDoze NDSS 2019 (ADMITTED A, alert fatigue); Julisch TISSEC 2003 (held) |
| `leighton` | 7.2 Outpatient is incremental, reversibl | Federated SIEM is as slow as the slowest source | Leighton (Panther) LinkedIn | B | not in bib | M | THIN | - |
| `conway-ch7` | Story time | System structure copies the organization that builds it | Conway, Datamation 1968 | AB | not in bib (magazine; footnote labels A) | M | - | Tier label mismatch: chapter labels A, but Datamation is a trade magazine, so B under §3.1. - |
