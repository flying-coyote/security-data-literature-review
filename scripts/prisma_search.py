#!/usr/bin/env python3
"""PRISMA identification stage: run the systematic database search.

This is the retro-run. The review's corpus was assembled by curation, and this
script executes a real database search after the fact so the identification
stage is reproducible and so the curated corpus can be tested for coverage.
Nothing here is simulated: every count written to disk comes from a live HTTP
response.

Databases
---------
OpenAlex  strict boolean title/abstract filter (NOT the fuzzy `search` param,
          which returns relevance-matched noise). Cursor-paginated at 200/page.
          arXiv preprints are reached THROUGH OpenAlex, which indexes them; the
          arXiv Atom API is deliberately not called, so this script parses no
          XML at all.
dblp      title-level search only, so the same ground is covered by several
          short title strings rather than one long boolean. dblp rate-limits
          and intermittently 500s/503s, so calls are spaced and retried, and a
          query that never succeeds is RECORDED as failed rather than dropped.

Standard library only. Re-runnable.
"""

import argparse
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

MAILTO = "flyingcoyote@gmail.com"
USER_AGENT = (
    "security-data-literature-review/prisma_search.py "
    "(systematic review; mailto:%s)" % MAILTO
)

OPENALEX_ENDPOINT = "https://api.openalex.org/works"
DBLP_ENDPOINT = "https://dblp.org/search/publ/api"

FROM_PUBLICATION_DATE = "2018-01-01"

SEC = (
    '(cybersecurity OR "security analytics" OR SIEM OR "intrusion detection" '
    'OR "threat detection" OR "security operations" OR "security monitoring" '
    'OR "log analysis")'
)
STACK = (
    '(lakehouse OR "data lake" OR "Apache Iceberg" OR "Delta Lake" '
    'OR "query engine" OR Trino OR ClickHouse OR DuckDB OR "stream processing" '
    'OR "Apache Kafka" OR "Apache Flink" OR "columnar storage" OR Parquet '
    'OR "data warehouse")'
)

# dblp indexes titles only, so the boolean above cannot be sent as one string.
# These short strings cover the same conceptual ground term-pair by term-pair.
DBLP_QUERIES = [
    "security data lake",
    "SIEM data lake",
    "security analytics lakehouse",
    "security log stream processing",
    "intrusion detection stream processing",
    "security data warehouse",
    "threat detection Kafka",
    "security telemetry pipeline",
]

DBLP_SLEEP_SECONDS = 3.5
DBLP_PAGE_SIZE = 100
DBLP_RETRIES = 3

OUT_DIR = pathlib.Path(
    "/home/jerem/security-data-literature-review/methods/prisma-results"
)


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

def http_get_json(url, timeout=90):
    """Single GET returning parsed JSON. Raises on any failure."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def http_get_json_retrying(url, tries=DBLP_RETRIES, base_sleep=DBLP_SLEEP_SECONDS):
    """GET with exponential backoff.

    Returns (payload, error_str_or_None, retry_log). retry_log is the list of
    transient errors that were retried past, and it is written into
    search-log.json: dblp returns intermittent 500s and 503s, and a reviewer
    should be able to check from the artifacts that a retried query really did
    succeed rather than take the claim on trust.
    """
    last_error = None
    retry_log = []
    for attempt in range(tries):
        try:
            return http_get_json(url), None, retry_log
        except urllib.error.HTTPError as exc:
            last_error = "HTTP %s %s" % (exc.code, exc.reason)
        except Exception as exc:  # noqa: BLE001 - network errors are varied
            last_error = "%s: %s" % (type(exc).__name__, exc)
        if attempt < tries - 1:
            backoff = base_sleep * (2 ** attempt)
            retry_log.append(last_error)
            print("      retry %d/%d after %s (sleeping %.1fs)"
                  % (attempt + 1, tries - 1, last_error, backoff))
            time.sleep(backoff)
    return None, last_error, retry_log


# --------------------------------------------------------------------------
# OpenAlex
# --------------------------------------------------------------------------

def reconstruct_abstract(inverted_index):
    """OpenAlex ships abstracts as {word: [positions]}. Rebuild the text."""
    if not inverted_index:
        return None
    positions = []
    for word, indexes in inverted_index.items():
        for index in indexes:
            positions.append((index, word))
    positions.sort()
    return " ".join(word for _, word in positions)


def openalex_filter_string():
    return "title_and_abstract.search:%s AND %s,from_publication_date:%s" % (
        SEC, STACK, FROM_PUBLICATION_DATE
    )


def normalize_openalex_record(raw):
    host_venue = None
    primary_location = raw.get("primary_location") or {}
    source = primary_location.get("source") or {}
    if source:
        host_venue = source.get("display_name")

    authors = []
    for authorship in raw.get("authorships") or []:
        author = authorship.get("author") or {}
        if author.get("display_name"):
            authors.append(author["display_name"])

    open_access = raw.get("open_access") or {}
    oa_url = open_access.get("oa_url")
    if not oa_url:
        best_oa = raw.get("best_oa_location") or {}
        oa_url = best_oa.get("pdf_url") or best_oa.get("landing_page_url")

    return {
        "openalex_id": raw.get("id"),
        "doi": raw.get("doi"),
        "title": raw.get("title") or raw.get("display_name"),
        "abstract": reconstruct_abstract(raw.get("abstract_inverted_index")),
        "publication_year": raw.get("publication_year"),
        "type": raw.get("type"),
        "host_venue": host_venue,
        "authors": authors,
        "cited_by_count": raw.get("cited_by_count"),
        "open_access_url": oa_url,
        "sources": ["openalex"],
    }


def search_openalex(log):
    print("[openalex] strict title_and_abstract boolean filter, cursor paging")
    filter_string = openalex_filter_string()
    log["queries"]["openalex"] = {
        "endpoint": OPENALEX_ENDPOINT,
        "filter": filter_string,
        "per_page": 200,
        "paging": "cursor",
    }

    records = []
    cursor = "*"
    page = 0
    reported_count = None

    while cursor:
        params = urllib.parse.urlencode({
            "filter": filter_string,
            "per-page": "200",
            "cursor": cursor,
            "mailto": MAILTO,
        })
        url = OPENALEX_ENDPOINT + "?" + params
        payload, error, retries = http_get_json_retrying(url, tries=3, base_sleep=2.0)
        log["openalex_retries"].extend(retries)
        if payload is None:
            log["failed_queries"].append({
                "database": "openalex",
                "query": filter_string,
                "page": page,
                "error": error,
            })
            print("  !! openalex page %d FAILED: %s" % (page, error))
            break

        meta = payload.get("meta") or {}
        if reported_count is None:
            reported_count = meta.get("count")
            print("  meta.count reported by OpenAlex: %s" % reported_count)

        results = payload.get("results") or []
        for raw in results:
            records.append(normalize_openalex_record(raw))

        page += 1
        print("  page %d: %d records (running total %d)"
              % (page, len(results), len(records)))

        cursor = meta.get("next_cursor")
        if not results:
            break
        time.sleep(0.5)

    log["openalex_reported_count"] = reported_count
    log["raw_counts"]["openalex"] = len(records)
    print("[openalex] retrieved %d raw records" % len(records))
    return records


# --------------------------------------------------------------------------
# dblp
# --------------------------------------------------------------------------

def normalize_dblp_record(info):
    authors_block = (info.get("authors") or {}).get("author") or []
    if isinstance(authors_block, dict):
        authors_block = [authors_block]
    authors = []
    for author in authors_block:
        if isinstance(author, dict):
            if author.get("text"):
                authors.append(author["text"])
        elif isinstance(author, str):
            authors.append(author)

    doi = info.get("doi")
    if doi:
        doi = "https://doi.org/" + doi

    year = info.get("year")
    try:
        year = int(year) if year is not None else None
    except (TypeError, ValueError):
        year = None

    return {
        "openalex_id": None,
        "doi": doi,
        "title": (info.get("title") or "").rstrip("."),
        "abstract": None,  # dblp does not carry abstracts
        "publication_year": year,
        "type": info.get("type"),
        "host_venue": info.get("venue"),
        "authors": authors,
        "cited_by_count": None,
        "open_access_url": info.get("ee"),
        "dblp_key": info.get("key"),
        "sources": ["dblp"],
    }


def search_dblp(log):
    print("[dblp] title-level queries (%d), >=%.1fs between calls"
          % (len(DBLP_QUERIES), DBLP_SLEEP_SECONDS))
    log["queries"]["dblp"] = {
        "endpoint": DBLP_ENDPOINT,
        "format": "json",
        "h": DBLP_PAGE_SIZE,
        "paging": "f offset",
        "query_strings": list(DBLP_QUERIES),
    }

    records = []
    for query in DBLP_QUERIES:
        offset = 0
        query_records = 0
        total_reported = None
        query_retries = []

        while True:
            params = urllib.parse.urlencode({
                "q": query,
                "format": "json",
                "h": str(DBLP_PAGE_SIZE),
                "f": str(offset),
            })
            url = DBLP_ENDPOINT + "?" + params
            time.sleep(DBLP_SLEEP_SECONDS)
            payload, error, retries = http_get_json_retrying(url)
            query_retries.extend(retries)

            if payload is None:
                log["failed_queries"].append({
                    "database": "dblp",
                    "query": query,
                    "offset": offset,
                    "error": error,
                })
                print("  !! %-38s FAILED after %d tries: %s"
                      % (repr(query), DBLP_RETRIES, error))
                break

            hits = ((payload.get("result") or {}).get("hits") or {})
            if total_reported is None:
                try:
                    total_reported = int(hits.get("@total", 0))
                except (TypeError, ValueError):
                    total_reported = 0

            hit_list = hits.get("hit") or []
            if isinstance(hit_list, dict):
                hit_list = [hit_list]

            for hit in hit_list:
                info = hit.get("info") or {}
                if info.get("title"):
                    records.append(normalize_dblp_record(info))
                    query_records += 1

            offset += len(hit_list)
            if not hit_list or offset >= (total_reported or 0):
                break

        log["dblp_per_query_counts"][query] = {
            "reported_total": total_reported,
            "records_retrieved": query_records,
            "retries": len(query_retries),
            "retried_errors": query_retries,
        }
        print("  %-40s total=%-5s retrieved=%d"
              % (repr(query), total_reported, query_records))

    log["raw_counts"]["dblp"] = len(records)
    print("[dblp] retrieved %d raw records" % len(records))
    return records


# --------------------------------------------------------------------------
# Deduplication
# --------------------------------------------------------------------------

def normalize_doi(doi):
    if not doi:
        return None
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    doi = re.sub(r"^doi:", "", doi)
    return doi or None


def normalize_title_key(title):
    if not title:
        return None
    key = title.lower()
    key = re.sub(r"[^a-z0-9]+", "", key)
    return key or None


def deduplicate(records):
    """DOI first (it is the stronger identity), normalized title as fallback.

    A record with a DOI is keyed ONLY by that DOI, so a DOI match and a title
    match are never conflated in the counts.
    """
    unique = []
    by_doi = {}
    by_title = {}
    removed_by_doi = 0
    removed_by_title = 0

    for record in records:
        doi_key = normalize_doi(record.get("doi"))
        if doi_key:
            existing = by_doi.get(doi_key)
            if existing is not None:
                merge_sources(existing, record)
                removed_by_doi += 1
                continue
            by_doi[doi_key] = record
            unique.append(record)
            # index the title too, so a DOI-less duplicate of this record can
            # still be caught on the title fallback
            title_key = normalize_title_key(record.get("title"))
            if title_key and title_key not in by_title:
                by_title[title_key] = record
            continue

        title_key = normalize_title_key(record.get("title"))
        if title_key:
            existing = by_title.get(title_key)
            if existing is not None:
                merge_sources(existing, record)
                removed_by_title += 1
                continue
            by_title[title_key] = record
        unique.append(record)

    return unique, removed_by_doi, removed_by_title


def merge_sources(kept, duplicate):
    for source in duplicate.get("sources") or []:
        if source not in kept["sources"]:
            kept["sources"].append(source)
    # keep whichever field is populated; the retained record wins on conflict
    for field in ("abstract", "doi", "open_access_url", "dblp_key",
                  "openalex_id", "cited_by_count", "host_venue"):
        if not kept.get(field) and duplicate.get(field):
            kept[field] = duplicate[field]


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-openalex", action="store_true")
    parser.add_argument("--skip-dblp", action="store_true")
    parser.add_argument("--out-dir", default=str(OUT_DIR))
    args = parser.parse_args()

    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    log = {
        "run_timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/prisma_search.py",
        "note": (
            "Retro-run of the systematic search against a curated corpus. "
            "arXiv preprints are reached through OpenAlex, which indexes them; "
            "the arXiv Atom API is not queried."
        ),
        "date_filter": {"from_publication_date": FROM_PUBLICATION_DATE},
        "queries": {},
        "raw_counts": {},
        "dblp_per_query_counts": {},
        "openalex_retries": [],
        "failed_queries": [],
    }

    all_records = []
    if not args.skip_openalex:
        all_records.extend(search_openalex(log))
    if not args.skip_dblp:
        all_records.extend(search_dblp(log))

    total_raw = len(all_records)
    unique, removed_by_doi, removed_by_title = deduplicate(all_records)

    log["total_raw_records"] = total_raw
    log["duplicates_removed"] = {
        "by_doi": removed_by_doi,
        "by_normalized_title": removed_by_title,
        "total": removed_by_doi + removed_by_title,
    }
    log["unique_records"] = len(unique)
    log["records_by_source_combination"] = count_source_combinations(unique)

    records_path = out_dir / "records.json"
    log_path = out_dir / "search-log.json"
    records_path.write_text(json.dumps(unique, indent=2, ensure_ascii=False))
    log_path.write_text(json.dumps(log, indent=2, ensure_ascii=False))

    print()
    print("=" * 68)
    print("PRISMA IDENTIFICATION SUMMARY")
    print("=" * 68)
    print("run (UTC)                : %s" % log["run_timestamp_utc"])
    for database, count in log["raw_counts"].items():
        print("raw records: %-12s: %d" % (database, count))
    if log.get("openalex_reported_count") is not None:
        print("openalex meta.count      : %s" % log["openalex_reported_count"])
    print("total raw records        : %d" % total_raw)
    print("duplicates removed (DOI)  : %d" % removed_by_doi)
    print("duplicates removed (title): %d" % removed_by_title)
    print("duplicates removed (total): %d" % (removed_by_doi + removed_by_title))
    print("UNIQUE RECORDS           : %d" % len(unique))
    print("by source: %s" % json.dumps(log["records_by_source_combination"]))
    if log["failed_queries"]:
        print("FAILED QUERIES           : %d" % len(log["failed_queries"]))
        for failure in log["failed_queries"]:
            print("  - [%s] %r -> %s"
                  % (failure["database"], failure["query"], failure["error"]))
    else:
        print("failed queries           : 0")
    print()
    print("wrote %s" % records_path)
    print("wrote %s" % log_path)


def count_source_combinations(records):
    counts = {}
    for record in records:
        key = "+".join(sorted(record.get("sources") or []))
        counts[key] = counts.get(key, 0) + 1
    return counts


if __name__ == "__main__":
    main()
