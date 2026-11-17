#!/bin/bash
# PreCommit hook for security-data-literature-review
# Validates CHANGELOG.md is updated for significant changes

# Get staged files
STAGED_FILES=$(git diff --cached --name-only)

# Check if significant files are being committed
SIGNIFICANT_CHANGES=false
for file in $STAGED_FILES; do
    case "$file" in
        MASTER-BIBLIOGRAPHY.md|METHODOLOGY.md|PUBLICATION-MANUSCRIPT.md|REFERENCES.md)
            SIGNIFICANT_CHANGES=true
            ;;
        *.md)
            # Core documentation only: archive/ is history and working/ holds dated
            # working records (audits, intake, proposals), neither version-worthy
            if [[ ! "$file" =~ ^archive/ ]] && [[ ! "$file" =~ ^working/ ]]; then
                SIGNIFICANT_CHANGES=true
            fi
            ;;
    esac
done

# If significant changes, remind about CHANGELOG
if [ "$SIGNIFICANT_CHANGES" = true ]; then
    # Check if CHANGELOG.md is in staged files
    if ! echo "$STAGED_FILES" | grep -q "CHANGELOG.md"; then
        echo ""
        echo "⚠️  CHANGELOG Reminder"
        echo "━━━━━━━━━━━━━━━━━━━━━"
        echo "Significant files are being committed."
        echo "Consider updating CHANGELOG.md if this is a version-worthy change."
        echo ""
        echo "Staged files:"
        echo "$STAGED_FILES" | sed 's/^/  - /'
        echo ""
        echo "To update CHANGELOG, add an entry like:"
        echo "  ## [1.XX.0] - $(date +%Y-%m-%d)"
        echo ""
        # A reminder, not a blocker: the script always exits 0 below
    fi
fi

# Always allow commit (this is advisory only)
exit 0
