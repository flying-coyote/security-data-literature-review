#!/usr/bin/env python3
"""Link-check every URL cited in MASTER-BIBLIOGRAPHY.md.

Why this exists: the bibliography is the citation source-of-truth for the
book, the essays, and the applied-bridge positioning, and it has accumulated
hundreds of URLs over a year of curation — vendor blogs get restructured,
whitepapers get taken down, conference pages rot. Nobody has swept the whole
set in one pass before; the health-check and weekly-scheduled-check scripts
each sample 10 URLs at random per run, which is fine for drift detection but
was never meant to answer "how many of the ~280 citations are actually still
live." This script answers that, once, exhaustively.

REPORT-ONLY: this script never writes to MASTER-BIBLIOGRAPHY.md or any other
source file. It writes a dated report under methods/. Any link fixes it turns
up are owner-adjudicated by hand — that's the same rule the rest of the repo
applies to bibliography edits, and a bulk automated rewrite of citation URLs
is exactly the kind of change that shouldn't happen without a human reading
each one (a redirect can land on a paywall, a different article, or a domain
squatter, and a script can't tell those apart from "still the right source").

A HEAD request is tried first (cheap, no body transfer); many publishers
(Elsevier, IEEE, some vendor blogs) 403 or 405 a bare HEAD from a non-browser
client, so those specific codes fall back to a GET before being called
blocked. A python-requests / urllib default User-Agent gets 403'd by several
sites in this bibliography (Gartner-class paywalls in particular), so this
script sends a real browser UA throughout.

Standard library only (urllib, concurrent.futures) — no venv/pip dependency
to keep working, so this keeps running on whatever Python happens to be on
the machine that runs it.
"""

import concurrent.futures
import re
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = REPO_ROOT / "MASTER-BIBLIOGRAPHY.md"
REPORT_PATH = REPO_ROOT / "methods" / f"link-check-{datetime.now():%Y-%m-%d}.md"

# Many publishers 403 the default python-urllib/requests UA outright, so a
# real desktop-Chrome UA is used for every request in this run.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
HEADERS = {"User-Agent": USER_AGENT, "Accept": "*/*"}

TIMEOUT_SECONDS = 15
MAX_WORKERS = 12
NETWORK_ERROR_RETRIES = 1  # one retry (2 tries total) on timeout/DNS/connection errors
SAME_HOST_DELAY_SECONDS = 1.0  # minimum gap between requests to the same host

# A bare HEAD gets refused by some servers for reasons that have nothing to
# do with whether the page exists (method not allowed, WAF rule against
# bodyless requests), so those specific codes earn a GET retry before the
# URL is called blocked.
RETRY_WITH_GET_ON = {403, 405, 501}

# Expected, not a failure: these are the codes a paywalled/anti-bot source
# (Gartner, IDC, Forrester, LinkedIn, etc.) returns to an automated client
# even when the citation is perfectly valid for a human reader.
PAYWALL_OR_BLOCKED_CODES = {401, 403, 429}

DEAD_CODES = {404, 410}

URL_RE = re.compile(r"https?://[^\s<>]+")
# Trailing characters that are almost always Markdown punctuation, not part
# of the URL — but a trailing ')' or ']' might close a bracket that's really
# part of the URL (e.g. a Wikipedia "_(disambiguation)" path), so those two
# are only stripped when the URL doesn't have a matching open bracket.
TRAILING_PUNCTUATION = ".,;:!?)]}\"'"


def extract_urls(text):
    """Pull every http(s) URL out of the bibliography text, deduped.

    No distinction is made between **URL**/**Alt URL**/**Source** fields and
    inline prose mentions — a plain full-document scan catches all of them
    in one pass, which is also more robust than trusting every citation to
    use the same field label consistently (some don't).
    """
    found = []
    seen = set()
    for match in URL_RE.finditer(text):
        url = _strip_trailing_punctuation(match.group(0))
        if url and url not in seen:
            seen.add(url)
            found.append(url)
    return found


def _strip_trailing_punctuation(url):
    while url and url[-1] in TRAILING_PUNCTUATION:
        if url[-1] == ")" and url.count("(") >= url.count(")"):
            break
        if url[-1] == "]" and url.count("[") >= url.count("]"):
            break
        url = url[:-1]
    return url


def _request_once(url, method):
    """One HTTP attempt. An HTTPError is a real response (some non-2xx
    status) so it's converted to a (code, final_url) pair here rather than
    left to propagate — only a genuine network failure (timeout, DNS,
    connection reset, TLS error) should reach the retry/error path below.
    """
    request = urllib.request.Request(url, method=method, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return response.getcode(), response.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl() or url


def _classify(url, code, final_url):
    redirect_note = ""
    if final_url and final_url != url:
        redirect_note = f"redirected -> {final_url}"

    if 200 <= code < 400:
        return {"class": "OK", "status": code, "note": redirect_note}
    if code in PAYWALL_OR_BLOCKED_CODES:
        note = "expected for paywalled/anti-bot sources"
        if redirect_note:
            note = f"{note}; {redirect_note}"
        return {"class": "PAYWALL_OR_BLOCKED", "status": code, "note": note}
    if code in DEAD_CODES:
        return {"class": "DEAD", "status": code, "note": redirect_note}
    # Any other status (5xx, 400, 406, 999-style bot blocks, etc.) doesn't
    # fit the three named classes cleanly, so it's recorded as an error with
    # the status called out rather than silently folded into one of them.
    note = f"unclassified HTTP status {code}"
    if redirect_note:
        note = f"{note}; {redirect_note}"
    return {"class": "ERROR", "status": code, "note": note}


class HostThrottle:
    """Serializes + paces requests per host so 12 worker threads never look
    like a scraping burst to any one site — several dozen URLs in this
    bibliography share a host (duckdb.org, clickhouse.com, confluent.io),
    and hitting one of those with 12 simultaneous requests is the kind of
    thing that gets a research script's IP rate-limited or blocked.
    """

    def __init__(self, hosts, delay_seconds):
        self._delay = delay_seconds
        self._locks = {host: threading.Lock() for host in hosts}
        self._last_request_at = {host: 0.0 for host in hosts}

    def wait_turn(self, host):
        lock = self._locks.setdefault(host, threading.Lock())
        with lock:
            now = time.monotonic()
            remaining = self._last_request_at.get(host, 0.0) + self._delay - now
            if remaining > 0:
                time.sleep(remaining)
            self._last_request_at[host] = time.monotonic()


def check_url(url, throttle):
    """Check one URL end to end: throttle, HEAD-then-maybe-GET, classify,
    with one retry on a genuine network-level error."""
    host = urlparse(url).netloc
    last_exc = None
    for attempt in range(NETWORK_ERROR_RETRIES + 1):
        try:
            throttle.wait_turn(host)
            code, final_url = _request_once(url, "HEAD")
            if code in RETRY_WITH_GET_ON:
                throttle.wait_turn(host)
                code, final_url = _request_once(url, "GET")
            result = _classify(url, code, final_url)
            result["url"] = url
            return result
        except Exception as exc:  # noqa: BLE001 - network errors are varied (timeout, DNS, SSL, reset)
            last_exc = exc
            if attempt < NETWORK_ERROR_RETRIES:
                time.sleep(1.0)
                continue
    return {
        "url": url,
        "class": "ERROR",
        "status": "",
        "note": f"{type(last_exc).__name__}: {last_exc}",
    }


def run_link_check(urls):
    hosts = {urlparse(url).netloc for url in urls}
    throttle = HostThrottle(hosts, SAME_HOST_DELAY_SECONDS)
    results = []
    total = len(urls)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(check_url, url, throttle): url for url in urls}
        for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            result = future.result()
            results.append(result)
            if done % 20 == 0 or done == total:
                print(f"  checked {done}/{total}")
    return results


def write_report(results):
    counts = Counter(r["class"] for r in results)
    by_class = defaultdict(list)
    for r in results:
        by_class[r["class"]].append(r)

    lines = [
        "# Bibliography Link Check",
        "",
        f"**Date**: {datetime.now():%Y-%m-%d}",
        f"**Source**: `MASTER-BIBLIOGRAPHY.md` ({len(results)} unique URLs extracted)",
        f"**Script**: `scripts/link_check.py`",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Class | Count | Meaning |",
        "|---|---|---|",
        f"| OK | {counts.get('OK', 0)} | 2xx/3xx — reachable |",
        f"| PAYWALL_OR_BLOCKED | {counts.get('PAYWALL_OR_BLOCKED', 0)} | 401/403/429 — expected for Gartner/IDC/Forrester-class sources, not a failure |",
        f"| DEAD | {counts.get('DEAD', 0)} | 404/410 — confirmed gone |",
        f"| ERROR | {counts.get('ERROR', 0)} | timeout/DNS/other, or a status code outside the three classes above |",
        f"| **Total** | **{len(results)}** | |",
        "",
        "---",
        "",
        "## Non-OK URLs",
        "",
    ]

    non_ok = [r for r in results if r["class"] != "OK"]
    if non_ok:
        lines.append("| URL | Class | Status | Note |")
        lines.append("|---|---|---|---|")
        # Worst-first ordering so DEAD links (the ones that actually need
        # owner attention) sort above the expected PAYWALL_OR_BLOCKED noise.
        class_order = {"DEAD": 0, "ERROR": 1, "PAYWALL_OR_BLOCKED": 2}
        for r in sorted(non_ok, key=lambda r: (class_order.get(r["class"], 9), r["url"])):
            note = r["note"].replace("|", "\\|") if r["note"] else ""
            lines.append(f"| {r['url']} | {r['class']} | {r['status']} | {note} |")
    else:
        lines.append("_None — every extracted URL returned 2xx/3xx._")

    lines.extend([
        "",
        "---",
        "",
        "_This pass is report-only: no bibliography file was edited by this script. "
        "Any fixes (re-pointing a dead URL, dropping a stale citation) are owner-adjudicated by hand._",
        "",
    ])

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines))
    return counts


def main():
    text = BIB_PATH.read_text()
    urls = extract_urls(text)
    print(f"Extracted {len(urls)} unique URLs from {BIB_PATH.name}")
    print(f"Checking with {MAX_WORKERS} workers, {SAME_HOST_DELAY_SECONDS}s same-host delay...")

    results = run_link_check(urls)
    counts = write_report(results)

    print()
    print("Summary:")
    for cls in ("OK", "PAYWALL_OR_BLOCKED", "DEAD", "ERROR"):
        print(f"  {cls}: {counts.get(cls, 0)}")
    print(f"  Total: {len(results)}")
    print(f"Report written to {REPORT_PATH}")


if __name__ == "__main__":
    main()
