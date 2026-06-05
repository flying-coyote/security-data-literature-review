#!/usr/bin/env python3
"""Weekly scheduled check + escalation gate for the literature review.

This is what the weekly scheduled agent runs. The cadence (decided 2026-06-05):

  - WEEKLY: run the health check and emit a short notification. If everything is green,
    that's the whole job — no edits, no refresh.
  - ESCALATE TO A REAL REFRESH when the check goes RED *or* once a month:
      RED      = status critical, OR any broken links, OR Evidence-Level-A < 75%,
                 OR sources are drifting stale past the freshness threshold.
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
TIER_A_FLOOR = 75.0          # % Evidence Level A target
OUTDATED_FRACTION_RED = 0.40  # >40% of sources >12mo is a red-line freshness failure
MONTHLY_WINDOW_DAYS = 7       # the weekly run within the first N days of a month triggers monthly refresh


def live_tier_a_percentage():
    """Compute Evidence Level A % live from the bibliography (the health check leaves this unset).
    Counts '**Evidence Level**: A' entries over total '#### ' entries. Returns 0.0 if unreadable."""
    path = os.path.join(HERE, "..", "MASTER-BIBLIOGRAPHY.md")
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return 0.0
    entries = len(re.findall(r"^#### ", content, re.MULTILINE))
    level_a = len(re.findall(r"\*\*Evidence Level\*\*:\s*A\b", content))
    return round(100.0 * level_a / entries, 1) if entries else 0.0


def decide(result, today):
    """Return (escalate: bool, reasons: list[str], monthly: bool)."""
    reasons = []

    if result.status == "critical":
        reasons.append("health check status is CRITICAL")
    if result.broken_links:
        reasons.append(f"{len(result.broken_links)} broken link(s)")
    if result.tier_a_percentage and result.tier_a_percentage < TIER_A_FLOOR:
        reasons.append(f"Evidence Level A {result.tier_a_percentage:.0f}% < {TIER_A_FLOOR:.0f}% floor")
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
