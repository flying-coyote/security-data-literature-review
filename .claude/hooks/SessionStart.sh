#!/bin/bash
# SessionStart hook for security-data-literature-review
# Displays git status and recent activity at session start

echo "=== Literature Review Session ==="
echo ""

# Git status
echo "Git Status:"
git status --short 2>/dev/null || echo "  (not in git repository)"
echo ""

# Recent commits
echo "Recent Commits:"
git log --oneline -5 2>/dev/null || echo "  (no commits found)"
echo ""

# Current version from CHANGELOG
if [ -f "CHANGELOG.md" ]; then
    CURRENT_VERSION=$(grep -m1 "^## \[" CHANGELOG.md | sed 's/## \[\([^]]*\)\].*/\1/')
    echo "Current Version: $CURRENT_VERSION"
fi

# Quick metrics
if [ -f "MASTER-BIBLIOGRAPHY.md" ]; then
    SOURCE_COUNT=$(grep -c "^\*\*\"" MASTER-BIBLIOGRAPHY.md 2>/dev/null || echo "0")
    echo "Bibliography Sources: ~$SOURCE_COUNT"
fi

echo ""
echo "=== Ready to work ==="
