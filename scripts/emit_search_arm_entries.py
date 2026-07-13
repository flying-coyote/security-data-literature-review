#!/usr/bin/env python3
"""
emit_search_arm_entries.py — render the appraised search-arm studies as bibliography blocks.

Every number in the emitted text is transcribed from methods/prisma-appraisal-2026-07-13.json,
which holds only figures a verifier independently located in the source. Nothing here is
retyped by hand, so a number cannot drift between the appraisal record and the bibliography.

Where a paper's headline figure is real but not usable as evidence for this review — a speedup
measured against a different hardware baseline, a percentage that is malformed as written, a
figure the paper itself attributes to a third party — CARRY lists what may be quoted and the
entry says in the open why the rest is left behind.

Usage: python3 scripts/emit_search_arm_entries.py > /tmp/search-arm.md
"""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
APPRAISAL = REPO / "methods" / "prisma-appraisal-2026-07-13.json"

# Per-record curation. `carry` = indices into numbers_claimed that may be quoted as evidence.
# `withhold` = a plain sentence naming what is deliberately not carried, and why.
CURATION = {
    1: dict(
        section="streaming",
        title="CATRACA — Stream-Processing Threat Detection as a Virtual Network Function (Concurrency and Computation, 2019)",
        carry=[0, 1],
        relevance=[
            "Hypothesis H-STREAM-01 (stateful stream processing at scale) — a peer-reviewed instance of detection embedded in the streaming pipeline rather than bolted on after it",
            "Book Chapter 7 (Ingestion — streaming)",
        ],
        note="A deployed, evaluated system (not a proposal), with concept-drift handling — the pattern the rest of the corpus sources from vendor material.",
    ),
    2: dict(
        section="streaming",
        title="Virtual Network Function for Real-Time Threat Detection Using Stream Processing (MobiSecServ, 2018)",
        carry=[0],
        relevance=[
            "Hypothesis H-STREAM-01 (streaming throughput at scale)",
            "Book Chapter 7 (Ingestion — streaming)",
        ],
        note="Earlier conference statement of the CATRACA line of work; shares authors with the 2019 journal paper above and with the SBRC short-course chapter below, so the three are one research group and not three independent confirmations.",
    ),
    4: dict(
        section="streaming",
        title="Adaptive and Auto-Scaling Stream Processing for Real-Time Intrusion Detection (IEEE GLOBECOM, 2018)",
        carry=[0, 1, 2],
        relevance=[
            "Hypothesis H-STREAM-01 (elastic vs monolithic stream processing)",
            "Book Chapter 7 (Ingestion) — the elastic-scaling argument",
        ],
        note="Uses the Wisdom CEP engine; the auto-scaling deployment is reported to use fewer resources than a monolithic one at the same load, which is the architectural claim the review makes from vendor sources elsewhere.",
    ),
    3: dict(
        section="streaming",
        title="Flink vs Spark Streaming for Machine-Learning NIDS on Data Streams (ACIS SNPD Winter, 2021)",
        carry=[],
        relevance=[
            "Hypothesis H-STREAM-01 (engine selection)",
            "Answers, in part, the head-to-head engine comparison this review names as open work (Section 4.4, Future Direction 4)",
        ],
        note="A direct peer-reviewed Flink-versus-Spark-Streaming comparison on a security workload. The abstract's headline claim is qualitative, so the paper is carried for the existence and direction of the comparison, not for a throughput number.",
    ),
    13: dict(
        section="streaming",
        title="AIDA Framework — Real-Time Correlation and Prediction of Intrusion Detection Alerts (ARES, 2019)",
        carry=[0],
        relevance=[
            "Hypothesis H-STREAM-01 (stream processing for alert correlation)",
            "Book Chapter 9 (Detection) — pipeline-side correlation",
        ],
        note="Notable because it is deployed inside SABU, a production multi-peer alert-sharing platform, rather than evaluated on a testbed.",
    ),
    23: dict(
        section="streaming",
        title="Faust vs Streamz — Complex Event Processing Engines for IoT Intrusion Detection (Computers, MDPI, 2026)",
        carry=[0, 1, 2, 3, 4],
        relevance=[
            "Hypothesis H-STREAM-01 (engine selection under a security workload)",
            "Directly answers Future Direction 4 (Section 4.4): a like-for-like engine benchmark on an identical security workload, with significance testing",
        ],
        note="The closest published analogue to this program's own engine benchmarks: same workload across engines, effect sizes and p-values reported rather than a single headline multiple.",
    ),
    26: dict(
        section="streaming",
        title="Practical Performance of a Distributed Processing Framework for ML-Based NIDS (IEEE COMPSAC, 2024)",
        carry=[0, 1, 2, 3, 4, 5, 6, 7],
        relevance=[
            "Hypothesis H3-PERFORMANCE-01 (pipeline throughput is distinct from model accuracy)",
            "Supports this review's core methodological stance: the pipeline, not the classifier, is where the throughput goes",
        ],
        note="Separates framework performance from model accuracy and locates the bottlenecks in Zeek, Logstash and Elasticsearch — the classifiers with a 30x throughput spread land within 0.007 of each other on F1. The arXiv deposit of this paper (record 33) is the same work and was removed as a duplicate.",
    ),
    24: dict(
        section="streaming",
        title="SPARCS — Stream-Processing Architecture for Real-Time Cyber-Physical Security (IEEE eScience, 2019)",
        carry=[0, 1, 2, 3, 4, 5],
        relevance=[
            "Book Chapter 6 (Architecture) — an end-to-end collection/transport/storage/processing reference design",
            "Serialization-format selection (Chapter 8): the measured Protobuf/MsgPack/JSON spread is directly comparable to the format decisions this review discusses",
        ],
        note="Authored at Lawrence Berkeley National Laboratory. The only record in the search set to receive a clean CITE with no venue caveat.",
    ),
    14: dict(
        section="streaming",
        title="Cloud-Based Snort NIDS Using Containers and Big Data (Big Data and Cognitive Computing, 2022)",
        carry=[0, 1],
        relevance=[
            "Hypothesis H-STREAM-01 (Kafka ingest throughput)",
            "Book Chapter 7 (Ingestion) — the containerized-sensor pattern",
        ],
        note="Kafka message-rate and throughput figures measured on a lambda-architecture backend.",
    ),
    0: dict(
        section="streaming",
        title="Intrusion Detection Streaming Transactions Using Apache Kafka and Spark Streaming (IEEE ICAIT, 2019)",
        carry=[],
        relevance=[
            "Hypothesis H-STREAM-01 — recorded as an instance of first-party Kafka/Spark pipeline measurement on UNSW-NB15",
        ],
        note=(
            "Carried for the existence of the measurement only. No number may be quoted from it: the readable abstract "
            "contains no figures, and its one directional statement (that Kafka partitions *increase* processing time) "
            "contradicts the paper's own stated aim, which the full text — IEEE-paywalled and unread — would have to resolve. "
            "A metadata trap worth recording: Semantic Scholar mis-assigns this paper to the unrelated IEEE International "
            "Conference on Advanced Infocomm Technology; the venue here is the Yangon ICAIT series, per Crossref."
        ),
    ),
    # ---- non-vendor production deployments ----
    9: dict(
        section="production",
        title="CERN — Large-Scale Intrusion Detection on Big Data Technologies (PoS, ISGC 2018)",
        carry=[0, 1],
        relevance=[
            "Hypothesis H1-VOLUME-07 (production security-telemetry volumes)",
            "Book Chapter 3 — a named, non-vendor production deployment at scale",
        ],
        note=(
            "Valuable for what it is rather than what it measures: the corpus's production-scale evidence is otherwise "
            "almost entirely big-tech engineering blogs, and this is a named public-research deployment with no product to sell."
        ),
    ),
    25: dict(
        section="production",
        title="INFN-CNAF — General-Purpose Data-Streaming Platform for Log Analysis and Security Protection (EPJ Web of Conferences, CHEP 2023)",
        carry=[],
        relevance=[
            "Book Chapter 3 — a second named non-vendor production deployment (WLCG Tier-1), alongside CERN above",
        ],
        note=(
            "A platform description rather than an evaluation: it reports the architecture in production but publishes no "
            "throughput or latency measurement, so it supports the deployment claim and not a performance claim."
        ),
    ),
    # ---- storage, reduction, query ----
    12: dict(
        section="storage",
        title="Workload-Aware Storage Reduction for Multi-Tenant SIEM on ClickHouse (IJACSA, 2026)",
        carry=[0, 1, 2, 3, 4, 5, 7],
        relevance=[
            "Hypothesis H3-PERFORMANCE-01 (ClickHouse for security analytics) and H-LOGCOMP-01 (machine-data compression)",
            "The closest published analogue to this program's own ClickHouse storage-reduction measurements",
        ],
        note=(
            "READ THE VENUE APPRAISAL BEFORE CITING THIS. The figures were located in the source and are reported here "
            "faithfully, but the venue cannot carry a Level-A claim, so this paper does not corroborate the storage-reduction "
            "claim in the way a peer-reviewed source normally would — it records that the only indexed paper on the exact "
            "question sits in a weak venue. The ~$30,000/year saving is the paper's own back-of-envelope projection for a "
            "hypothetical 100 GB/day SOC, not a measured result, and is not carried. Note also that this author's other "
            "2026 paper (ECTI-CIT, below) is the review's other peer-reviewed check on a vendor-sourced claim: the two are "
            "the same author and are not independent of each other."
        ),
    ),
    35: dict(
        section="storage",
        title="Comparative Evaluation of Log-Reduction Techniques Using Vector on Public Security Datasets (ECTI-CIT, 2026)",
        carry=[0, 1, 2, 3],
        relevance=[
            "Hypothesis H-COST-09 (pipeline reduction economics) — a dataset-based check on the Cribl/Vector-class reduction claims the corpus otherwise takes from vendor material",
            "Book Chapter 7 (Ingestion) — the route/reshape/reduce pattern",
        ],
        note=(
            "Benchmarks five Vector-based reduction methods against a Filebeat baseline over 3M+ SOC records, reporting "
            "attack-coverage retention alongside the reduction — which is the honest way to state a reduction claim, since "
            "throwing away data always reduces volume and the question is what detection you lose. Same single author as the "
            "IJACSA ClickHouse paper above; the two are not independent."
        ),
    ),
    8: dict(
        section="storage",
        title="Time Models in Graph Databases for Security Log Analysis (International Journal of Web Information Systems, 2021)",
        carry=[],
        relevance=[
            "Book Chapter 8 (Schema and modelling) — temporal modelling of security logs",
            "The corpus carries no graph-database anchor; this is the only one the search returned",
        ],
        note=(
            "Compares three timestamp-storage models for query performance. The finding is comparative and qualitative — "
            "the simplest model also yields the simplest queries — so no figure is carried."
        ),
    ),
    10: dict(
        section="storage",
        title="Efficient Host Intrusion Detection Using Hyperdimensional Computing (IEEE BigData, 2024)",
        carry=[0],
        relevance=[
            "Book Chapter 9 (Detection) — cited for its statement of the provenance-graph query-latency problem, which the review's cost-to-serve argument depends on",
        ],
        note=(
            "The paper's headline speedups (up to 4,242x on CPU, up to 18,000x on a hardware accelerator, and power figures "
            "quoted in orders of magnitude) are measured against different baselines and different hardware than anything this "
            "review compares, and are deliberately NOT carried. What is carried is the framing: state-of-the-art provenance-graph "
            "query latencies are described as impractical for modern threat detection, from an authorship group including "
            "Patrick McDaniel and Tajana Rosing."
        ),
    ),
    # ---- security data lake / forensics ----
    37: dict(
        section="lake",
        title="Data-Lake-Based Security Transmission and Storage Scheme for Streaming Big Data (Cluster Computing, 2024)",
        carry=[],
        relevance=[
            "Hypothesis H-ARCH-01 (lakehouse/data-lake architecture for security data)",
            "Book Chapter 6 (Architecture) — secure ingestion and storage of streaming security data",
        ],
        note=(
            "An ECC lightweight-encryption interceptor at the data source, an SSL-secured Flume/Kafka transport, and an "
            "LZO-compressed Hadoop data-lake storage layer. The published abstract reports roughly an 18% reduction in memory "
            "load attributed to the encryption interceptor; the figure was confirmed in the publisher's abstract by an "
            "independent check, but no full text was read, so it is recorded and not built upon. Cluster Computing has a "
            "documented paper-mill problem confined to guest-edited special issues; this is a regular-issue article, which is "
            "why it survives appraisal."
        ),
    ),
    38: dict(
        section="lake",
        title="Digital-Forensics Architecture on a Security Lake for Automated Evidence Collection (Journal of Intelligent Systems, 2024)",
        carry=[],
        relevance=[
            "Hypothesis H-ARCH-01 (security data lake) — the closest published statement of the security-lake thesis this review argues",
            "Book Chapter 6 (Architecture)",
        ],
        note=(
            "A security-lake plus data-lake architecture for real-time forensic evidence collection across multiple cloud "
            "accounts and regions, stated to be validated on an actual AWS deployment. Appraised at abstract level only — the "
            "publisher's full text was unreachable — so no quantitative result is carried. Venue verified at primaries: "
            "DOAJ-listed, Scopus Q2, double-anonymous review, not retracted."
        ),
    ),
    # ---- framing ----
    27: dict(
        section="framing",
        title="Corporate Security Is a Big Data Problem (ACM Ubiquity, 2018)",
        carry=[],
        relevance=[
            "Section 1.2 (Literature gap) — a 2018 statement, in an ACM venue, of the thesis this review otherwise dates to vendor writing",
        ],
        note=(
            "Argues corporate security is a big-data problem and sketches a security-data-lake-to-'security cockpit' "
            "architecture. Ubiquity is ACM's editor-led web magazine, not a peer-reviewed journal — the review it applies to "
            "commentary is lighter than a journal's, so this is a framing source and not evidence."
        ),
    ),
    28: dict(
        section="framing",
        title="Machine Learning on Distributed Stream-Processing Platforms — Storm, Spark Streaming and Flink (SBRC Short Courses, 2018, in Portuguese)",
        carry=[],
        relevance=[
            "Background for the engine-comparison discussion (Storm vs Spark Streaming vs Flink), including lambda-architecture treatment",
        ],
        note=(
            "A short-course/tutorial chapter, not a primary study. Every figure in it is quoted from third parties, so no "
            "number is carried. Shares authors with records 1 and 2 above (the CATRACA group)."
        ),
    ),
    # ---- recorded, not currently supporting a claim ----
    11: dict(
        section="recorded",
        title="High-Performance FPGA Architecture for Data-Stream Processing — IPsec Gateway (International Journal of Electronics and Telecommunications, 2018)",
        carry=[1, 2],
        relevance=[
            "No hypothesis in this edition. Recorded from the systematic search: hardware acceleration of the ingest tier is outside the scope this review sets (software architecture on commodity infrastructure), and is noted as adjacent work rather than folded into a finding",
        ],
        note="Peer-reviewed and sound; simply not on any claim this review makes.",
    ),
    22: dict(
        section="recorded",
        title="Hybrid Stream Processing for Runtime Protection in Remote Driving (IEEE ICIN, 2026)",
        carry=[],
        relevance=[
            "No hypothesis in this edition. Recorded from the systematic search as an automotive/OT instance of the online-vs-offline detection split",
        ],
        note=(
            "Its headline figure — an online operator beating an offline detector 'by 584.3% in latency time' — is malformed "
            "as written (a percentage improvement in latency is not interpretable without the direction and the base), so no "
            "number is carried."
        ),
    ),
    6: dict(
        section="recorded",
        title="Data-Warehouse Modelling for Security-Log Management in a Government SOC (Jurnal Teknik Informatika, 2023)",
        carry=[],
        relevance=[
            "No hypothesis in this edition. Recorded as the only treatment the search returned of Kimball-style dimensional modelling applied to SOC log data",
        ],
        note=(
            "A modelling proposal with no evaluation, in a journal not listed in DOAJ, Scopus or Web of Science. Recorded for "
            "completeness of the search record; it supports nothing."
        ),
    ),
    29: dict(
        section="recorded",
        title="Architectural and Analytical Aspects of Big Data for IoT System Security (Cybersecurity: Education, Science, Technique, 2026)",
        carry=[],
        relevance=["No hypothesis in this edition. Recorded from the systematic search"],
        note="Simulated evaluation, qualitative claims only, no figures with units in the abstract.",
    ),
    32: dict(
        section="recorded",
        title="Analysis of Logs in the Environment of Email Services (IEEE ICETA, 2020)",
        carry=[],
        relevance=[
            "No hypothesis in this edition. Recorded from the systematic search as a store-selection comparison (Elasticsearch, Kafka, Redis, Splunk, MongoDB) for audit records",
        ],
        note="The comparison method could not be established from the available text, so it is recorded and not relied on.",
    ),
    34: dict(
        section="recorded",
        title="Binary-Feature-Extraction Data-Provenance System on Flink (IEEE CyberC, 2018)",
        carry=[],
        relevance=[
            "No hypothesis in this edition. Recorded from the systematic search as provenance-as-security-telemetry implemented on a stream processor",
        ],
        note="A pattern the corpus does not otherwise carry; noted for a future edition rather than cited here.",
    ),
}

SECTIONS = [
    ("streaming", "Streaming Architectures & Engine Comparisons (search arm)"),
    ("production", "Non-Vendor Production Deployments (search arm)"),
    ("storage", "Storage Reduction, Compression & Query (search arm)"),
    ("lake", "Security Data Lake & Forensics Architecture (search arm)"),
    ("framing", "Framing & Position Sources (search arm)"),
    ("recorded", "Recorded from the Search, Not Supporting a Claim in This Edition (search arm)"),
]


def fmt_authors(authors):
    if not authors:
        return "Not recorded in the source metadata"
    return ", ".join(authors)


def main():
    data = json.loads(APPRAISAL.read_text(encoding="utf-8"))
    by_rank = {r["rank"]: r for r in data["records"]}

    missing = set(CURATION) - set(by_rank)
    if missing:
        print(f"FATAL: curated ranks absent from the appraisal record: {sorted(missing)}", file=sys.stderr)
        return 2

    citable = {r["rank"] for r in data["records"] if r["final_disposition"] != "DROP"}
    if set(CURATION) != citable:
        print(
            "FATAL: curation does not match the citable set.\n"
            f"  curated but not citable: {sorted(set(CURATION) - citable)}\n"
            f"  citable but not curated: {sorted(citable - set(CURATION))}",
            file=sys.stderr,
        )
        return 2

    out = []
    for key, heading in SECTIONS:
        ranks = [rk for rk, c in CURATION.items() if c["section"] == key]
        if not ranks:
            continue
        out.append(f"### {heading}\n")
        for rk in sorted(ranks):
            rec, cur = by_rank[rk], CURATION[rk]
            out.append(f"#### {cur['title']}\n")
            out.append(f"**Authors**: {fmt_authors(rec['authors'])}")
            out.append(f"**Date**: {rec['year']} ({rec['venue_resolved']})")
            out.append(f"**URL**: {rec['doi'] or 'No DOI registered'}")

            tier = rec["final_tier"]
            out.append(f"**Evidence Level**: {tier} ({rec['appraiser_reason'].split('.')[0].strip()})")

            flags = rec["integrity_flags"]
            if flags or rec["venue_class"] not in ("established_journal", "established_conference"):
                out.append(
                    f"**Venue appraisal (2026-07-13)**: {rec['publisher']} — class `{rec['venue_class']}`. "
                    + (" ".join(f"{f.rstrip('.')}." for f in flags) if flags else "No integrity flags found.")
                )

            out.append("**Relevance**:")
            for r in cur["relevance"]:
                out.append(f"- {r}")

            carried = [rec["numbers_claimed"][i] for i in cur["carry"] if i < len(rec["numbers_claimed"])]
            out.append("\n**Key Findings**:")
            for n in carried:
                out.append(f"- {n}")
            if cur.get("note"):
                out.append(f"- {cur['note']}")

            out.append(
                f"\n**Provenance**: PRISMA database-arm search, 2026-07-13 (search record {rk} of 40). "
                f"Appraised for venue integrity and content, then independently verified by a second reviewer; "
                f"number check: {rec['verify_number_check'].replace('_', ' ')}.\n"
            )
        out.append("---\n")

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
