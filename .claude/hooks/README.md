# Session Hooks

**Project**: security-data-literature-review
**Last Updated**: 2026-01-02

This directory contains session hooks that execute at specific points during Claude Code sessions.

---

## Available Hooks

### `SessionStart.sh`
**Trigger**: Beginning of each Claude Code session
**Purpose**: Display project context and git status
**Output**:
- Git status (staged/unstaged changes)
- Recent commits (last 5)
- Current version from CHANGELOG.md
- Bibliography source count

**Benefit**: Provides immediate context awareness for each session

### `PreCommit.sh`
**Trigger**: Before git commits (advisory)
**Purpose**: Remind to update CHANGELOG.md for significant changes
**Behavior**:
- Checks if significant files are being committed (*.md excluding archive/)
- If CHANGELOG.md is not staged, displays reminder
- Non-blocking (allows commit to proceed)

**Benefit**: Maintains version history for academic citation stability

---

## Hook Execution

Hooks are shell scripts that Claude Code can execute at defined trigger points:

| Hook | Trigger | Blocking |
|------|---------|----------|
| SessionStart.sh | Session begins | No |
| PreCommit.sh | Before git commit | No (advisory) |

---

## Adding New Hooks

To add a new hook:

1. Create executable shell script in `.claude/hooks/`
2. Name according to trigger point (e.g., `PostEdit.sh`)
3. Make executable: `chmod +x .claude/hooks/<name>.sh`
4. Document in this README

---

**Created**: 2026-01-02 (Best Practices Audit)
