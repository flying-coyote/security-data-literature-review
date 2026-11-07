#!/usr/bin/env python3
"""Weekly scheduled check + escalation gate for the literature review.

This is what the weekly scheduled agent runs. The cadence (decided 2026-06-05):

  - WEEKLY: run the health check and emit a short notification. If everything is green,
    that's the whole job — no edits, no refresh.
  - ESCALATE TO A REAL REFRESH when the check goes RED *or* once a month:
      RED      = status critical, OR any broken links,
                 OR sources are drifting stale past the freshness threshold.
    The Level-A share is reported but never escalates: the share target was retired by
    owner ruling 2026-08-19 (METHODOLOGY §8.1a), so a floor on it would go red every run
    and the signal would be noise. The integrity measures (verified-claim count, entries
    with no validation record) are reported in its place.
      MONTHLY  = the weekly run that lands in the first 7 days of a calendar month.

The script only DECIDES and NOTIFIES. It never edits the bibliography itself — a real
refresh is a supervised job (run `/monthly-update`), because this is a source-of-truth
artifact and autonomous web-research edits to it should not happen unattended.

Exit code: 0 = OK (no action), 10 = ESCALATE (refresh due). The scheduled agent relays
the printed notification and, on ESCALATE, flags that a refresh is due.
"""

import os
import re
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from weekly_health_check import LiteratureReviewHealthCheck  # noqa: E402

# Escalation thresholds
# TIER_A_FLOOR was removed 2026-11-07. It sat at 60% against a live share of ~17% and so
# escalated every run. The share target itself was retired by owner ruling 2026-08-19
# (METHODOLOGY §8.1a): the share falls as the corpus gets more honest, so it is reported
# as a description and never gates. The integrity measures below replace it in the
# notification; they are derived, not thresholded, until the owner rules a floor.
OUTDATED_FRACTION_RED = 0.40  # >40% of sources >12mo is a red-line freshness failure
MONTHLY_WINDOW_DAYS = 7       # the weekly run within the first N days of a month triggers monthly refresh


def live_tier_a_percentage():
    """Compute Evidence Level A % live from the bibliography (the health check leaves this unset).
    Imported, not reimplemented (count_reconcile.py's rule): a divergent local counting rule
    reported 43.0% while the canonical parser said 41.9%, so the escalation floor and the
    published number could disagree. Returns 0.0 if the bibliography is unreadable."""
    sys.path.insert(0, HERE)
    try:
        from automation_dashboard import parse_master_bibliography
        bib = parse_master_bibliography()
        return float(bib["evidence_quality"]) if bib else 0.0
    except Exception:
        return 0.0


def integrity_measures():
    """Derive the claim-integrity measures from the bibliography, per #### block (the
    same block split the canonical parser uses). Returns (verified, no_record, tiered):
    verified = blocks whose Validation Status line carries a ✅; no_record = tiered blocks
    with no validation line of any kind. Returns None if the bibliography is unreadable."""
    path = os.path.join(HERE, "..", "MASTER-BIBLIOGRAPHY.md")
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return None
    blocks = re.split(r"(?m)^####\s+", content)[1:]
    tiered = [b for b in blocks if re.search(r"\*\*Evidence Level\*\*:\s*[A-D]\b", b)]
    verified = sum(1 for b in tiered if re.search(r"\*\*Validation Status\*\*:\s*✅", b))
    no_record = sum(1 for b in tiered if not re.search(r"\*\*Validation", b))
    return verified, no_record, len(tiered)


def decide(result, today):
    """Return (escalate: bool, reasons: list[str], monthly: bool)."""
    reasons = []

    if result.status == "critical":
        reasons.append("health check status is CRITICAL")
    if result.broken_links:
        reasons.append(f"{len(result.broken_links)} broken link(s)")
    if result.total_sources:
        frac = len(result.outdated_evidence) / result.total_sources
        if frac > OUTDATED_FRACTION_RED:
            reasons.append(f"{len(result.outdated_evidence)}/{result.total_sources} "
                           f"({frac*100:.0f}%) sources >12 months old")

    red = bool(reasons)
    monthly = today.day <= MONTHLY_WINDOW_DAYS
    if monthly:
        reasons.append(f"monthly refresh window (day {today.day} of the month)")

    return (red or monthly), reasons, monthly


def notify(result, escalate, reasons, monthly):
    light = "🟢" if result.status == "healthy" else "🟡" if result.status == "warning" else "🔴"
    lines = [
        f"# Literature review — weekly check ({result.timestamp[:10]})",
        "",
        f"{light} **Status: {result.status.upper()}** · "
        f"{result.total_sources} sources · {result.tier_a_percentage:.0f}% Level A · "
        f"{len(result.broken_links)} broken · {len(result.outdated_evidence)} outdated >12mo · "
        f"last commit {result.days_since_commit}d ago",
    ]
    im = integrity_measures()
    if im:
        verified, no_record, tiered = im
        lines.append(f"Integrity: {verified}/{tiered} entries claim-verified ✅ · "
                     f"{no_record} with no validation record · Level-A share is descriptive, "
                     "not a target (METHODOLOGY §8.1a)")
    if not escalate:
        lines += ["", "✅ Healthy — no action this week."]
    else:
        kind = "MONTHLY + RED" if (monthly and result.status != "healthy") else ("MONTHLY" if monthly else "RED")
        lines += [
            "",
            f"🔧 **ESCALATE ({kind}) — a real refresh is due.** Run `/monthly-update` in a supervised session.",
            "Reasons:",
        ] + [f"- {r}" for r in reasons]
        if result.broken_links:
            lines += ["", "Broken links to fix:"] + [f"- {u}" for u in result.broken_links[:10]]
    return "\n".join(lines)


def main():
    today = datetime.now()
    # Locate the repo relative to this script so the check works wherever the repo is
    # checked out (local working tree or a fresh clone in a scheduled remote routine),
    # not only at the health check's hardcoded ~/security-data-literature-review default.
    hc = LiteratureReviewHealthCheck(repo_path=os.path.join(HERE, ".."))
    result = hc.run_all_checks()
    # The health check leaves tier_a_percentage unset (0.0); compute it live so the
    # notification and the Level-A floor check use the real number, not a misleading 0%.
    if not result.tier_a_percentage:
        result.tier_a_percentage = live_tier_a_percentage()
    escalate, reasons, monthly = decide(result, today)
    print()
    print(notify(result, escalate, reasons, monthly))
    print()
    print(f"VERDICT: {'ESCALATE' if escalate else 'OK'}")
    return 10 if escalate else 0


if __name__ == "__main__":
    sys.exit(main())
