# Session hooks

**Project**: security-data-literature-review
**Last updated**: 2026-11-17

Two shell scripts live here. Only `SessionStart.sh` is wired into Claude Code, through `.claude/settings.json`; `PreCommit.sh` is an advisory helper you run by hand, because Claude Code has no pre-commit trigger and the repo's real commit gate is `scripts/pre-commit.sh`, installed as the git hook (see README.md, "Reproducing the counts").

## `SessionStart.sh`

Runs at the start of every Claude Code session in this repo (`.claude/settings.json`, `hooks.SessionStart`). It prints the git status, the last five commits, the current version heading from CHANGELOG.md and the number of `#### ` entry blocks in MASTER-BIBLIOGRAPHY.md. The block count is a raw heading count and includes the documented stubs; the tiered counts come from `python3 scripts/count_reconcile.py`.

## `PreCommit.sh` (manual, advisory)

Run `bash .claude/hooks/PreCommit.sh` with changes staged and it reminds you to add a CHANGELOG.md entry when a core document is staged without one. It ignores `archive/` and `working/`, because those hold history and dated working records rather than the citable review, and it always exits 0.

## The gates that actually block

| Gate | Where it runs | What it blocks |
|------|---------------|----------------|
| `scripts/pre-commit.sh` | local git hook, once installed per clone | secrets, a staged file with a stale gated count, a staged vendor DB whose rollups drift, a staged file with a stale moved path or broken relative link, and a new personal-communication attribution in the bibliography or a book appendix |
| `.github/workflows/gates.yml` | every push and pull request | a stale gated count, a taxonomy mismatch, vendor-rollup drift, invalid metadata, and a stale moved path or broken relative link, all checked repo-wide; the secret scan reads only staged changes, so in a CI checkout it finds nothing to scan and the scan does its work only in the local hook |

`.claude/settings.json` also carries a `Stop` hook that warns about uncommitted changes and unpushed commits at the end of a session.
