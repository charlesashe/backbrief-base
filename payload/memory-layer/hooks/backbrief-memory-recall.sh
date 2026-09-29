#!/bin/sh
# backbrief-memory-recall.sh, SessionStart hook (POSIX sh).
#
# Prints a compact digest of this project's own memory, the newest handoff
# brief plus the tail of the decision log, to stdout, so Claude Code injects
# it into the model's context at session start (design D1, D3).
#
# Fail-silent by design (D4): any missing file, missing folder, or internal
# error along the way prints nothing and exits 0. This script must never
# exit nonzero and must never print a partial digest.
#
# Project root resolution: $CLAUDE_PROJECT_DIR, falling back to the current
# directory if unset (design D5's sh half).

PROJECT_ROOT="${CLAUDE_PROJECT_DIR:-.}"
HANDOFFS_DIR="$PROJECT_ROOT/.claude/memory/handoffs"
DECISIONS_FILE="$PROJECT_ROOT/.claude/memory/decisions.md"

# No handoffs folder at all: nothing to recall yet. Exit clean.
[ -d "$HANDOFFS_DIR" ] || exit 0

# Newest brief = lexicographically last *.md filename. Correct because the
# shipped /handoff stamps YYYY-MM-DD-HHMM- names (design D3).
NEWEST=$(ls -1 "$HANDOFFS_DIR" 2>/dev/null | grep -E '\.md$' 2>/dev/null | sort 2>/dev/null | tail -n 1 2>/dev/null)
[ -n "$NEWEST" ] || exit 0

BRIEF_PATH="$HANDOFFS_DIR/$NEWEST"
[ -f "$BRIEF_PATH" ] || exit 0

BYTES=$(wc -c < "$BRIEF_PATH" 2>/dev/null | tr -d ' \t\n')
case "$BYTES" in
    ''|*[!0-9]*) exit 0 ;;
esac

if [ "$BYTES" -le 4000 ]; then
    BODY=$(cat "$BRIEF_PATH" 2>/dev/null) || exit 0
else
    TITLE=$(head -n 1 "$BRIEF_PATH" 2>/dev/null) || exit 0
    # From the first heading line containing "next action" (case-insensitive)
    # up to (not including) the next "## " heading, or EOF.
    NEXT_ACTION=$(awk '
        /^##[^#]/ {
            if (grab) exit
            if (tolower($0) ~ /next action/) { grab=1; print; next }
            next
        }
        grab { print }
    ' "$BRIEF_PATH" 2>/dev/null)

    if [ -n "$NEXT_ACTION" ]; then
        BODY="$TITLE

$NEXT_ACTION

(truncated; full brief at $BRIEF_PATH)"
    else
        # No "Next action" heading: degrade gracefully to title + note.
        BODY="$TITLE

(truncated; full brief at $BRIEF_PATH)"
    fi
fi

DECISIONS_BLOCK=""
if [ -f "$DECISIONS_FILE" ]; then
    # Matches BOTH shipped decision-log formats: the '## ' heading style and the
    # '- YYYY-MM-DD:' bullet style the scaffold's starter file uses. Requiring a date
    # on the bullet form keeps ordinary list items out. Sub-bullets are indented, so
    # an entry's rationale lines cannot match either branch.
    DTAIL=$(grep -E '^(## |- [0-9]{4}-[0-9]{2}-[0-9]{2})' "$DECISIONS_FILE" 2>/dev/null | tail -n 5)
    if [ -n "$DTAIL" ]; then
        DECISIONS_BLOCK="

Last 5 decision-log entries:
$DTAIL"
    fi
fi

printf '[Backbrief memory] %s - Run /pickup for the complete read.\n\n%s%s\n' "$NEWEST" "$BODY" "$DECISIONS_BLOCK"

exit 0
