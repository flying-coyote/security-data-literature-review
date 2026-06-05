# Scheduled update cadence

Decided 2026-06-05: **light weekly health-check-and-notify, escalating to a real refresh monthly
or when the check goes red.** This replaces the manual, unscheduled monthly checklist that lapsed
for 96 days.

## The mechanism

`scripts/weekly_scheduled_check.py` is the deterministic core. Each run:

1. runs the full health check (`weekly_health_check.py`),
2. computes Evidence-Level-A live (the health check leaves it unset),
3. decides escalation, and
4. prints a short notification + a `VERDICT: OK | ESCALATE` line. Exit `0` = OK, `10` = escalate.

Escalation fires when **red** — status critical, any broken links, Level-A below 75%, or more than
40% of sources older than 12 months — **or monthly**, on the weekly run that lands in the first 7
days of a calendar month. The script only DECIDES and NOTIFIES; it never edits the bibliography. A
real refresh is the supervised `/monthly-update` job, because this is a source-of-truth artifact and
unattended web-research edits to it should not happen.

Test it:

```bash
python3 scripts/weekly_scheduled_check.py   # prints the notification; exits 10 if a refresh is due
```

## Activating the weekly schedule

The schedule runs against `main` on GitHub, so this has to be true first:

1. The revival branch (`lit-review-revival-2026-06`) is merged to `main` and pushed, so
   `weekly_scheduled_check.py` exists on `main`.

Then create a weekly remote routine (via `/schedule`) that runs:

```
cd ~/security-data-literature-review && git pull --quiet && python3 scripts/weekly_scheduled_check.py
```

on a weekly cron (e.g. `33 8 * * 1` — Mondays ~08:33 local, off the :00 mark), and relays the printed
notification. On `VERDICT: ESCALATE`, the routine should surface "refresh due — run `/monthly-update`"
rather than attempt the refresh itself.

> Note on tooling: the in-session `CronCreate` is session-only and auto-expires after 7 days, so it is
> not suitable for this forever-weekly cadence — use a `/schedule` remote routine, which persists and
> can notify.
