#!/bin/sh
# backbrief-status.sh - status-contract hook (POSIX sh).
#
# Writes the deterministic status contract this layer exists for:
# .claude/memory/backbrief-status.json (the current record) and
# .claude/memory/backbrief-events.jsonl (the append-only event log).
# One script serves both registered events; it reads hook_event_name
# from the hook input on stdin and dispatches:
#
#   UserPromptSubmit  - if the prompt launches a tracked command, rewrite
#                       the status record and append an operation_launched
#                       event. Any other prompt writes nothing.
#   Stop              - if a status record exists, bump updated_at and
#                       append a turn_ended event. No record, no write.
#
# The contract records only what a hook can observe: which operation was
# last launched, when, and by which session. It never records success or
# failure, because a hook cannot observe completion - exit_status stays
# "unknown" by design, and /bb-status says so rather than implying more.
#
# Fail-silent by design, same as the memory layer: any missing folder,
# unparseable input, or internal error writes nothing, prints nothing,
# and exits 0. This script must never exit nonzero and must never print
# to stdout (UserPromptSubmit stdout would be injected into context).
#
# Project root resolution: $CLAUDE_PROJECT_DIR, falling back to the
# current directory if unset (the memory layer's sh half, same reason).

PROJECT_ROOT="${CLAUDE_PROJECT_DIR:-.}"
MEM_DIR="$PROJECT_ROOT/.claude/memory"
[ -d "$MEM_DIR" ] || exit 0

STATUS_FILE="$MEM_DIR/backbrief-status.json"
EVENTS_FILE="$MEM_DIR/backbrief-events.jsonl"

INPUT=$(cat 2>/dev/null) || exit 0
[ -n "$INPUT" ] || exit 0

EVENT=$(printf '%s' "$INPUT" | tr -d '\n' | sed -n 's/.*"hook_event_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
SID=$(printf '%s' "$INPUT" | tr -d '\n' | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
[ -n "$SID" ] || SID="unknown"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null) || exit 0

if [ "$EVENT" = "UserPromptSubmit" ]; then
    # First slash token of the prompt, letters and hyphens only. A prompt
    # that does not open with a tracked command writes nothing at all.
    OP_TOKEN=$(printf '%s' "$INPUT" | tr -d '\n' | sed -n 's/.*"prompt"[[:space:]]*:[[:space:]]*"[[:space:]]*\(\/[a-z][a-z-]*\).*/\1/p')
    [ -n "$OP_TOKEN" ] || exit 0

    PHASE="running"
    APPROVAL="false"
    case "$OP_TOKEN" in
        /intake)         OP="intake";         GATE="none" ;;
        /business-plan)  OP="business-plan";  GATE="ceo-gate (planning support)" ;;
        /grade)          OP="grade";          GATE="grading rule (3-pass cap)" ;;
        /grade-idea)     OP="grade-idea";     GATE="grading rule (single pass)" ;;
        /approve)        OP="approve";        GATE="owner decision - the recorded GO in .claude/memory/decisions.md"
                         PHASE="waiting_for_approval"; APPROVAL="true" ;;
        /next)           OP="next";           GATE="none" ;;
        /setup)          OP="setup";          GATE="none" ;;
        /demo)           OP="demo";           GATE="none" ;;
        /verify-install) OP="verify-install"; GATE="none" ;;
        /critique)       OP="critique";       GATE="none" ;;
        /council)        OP="council";        GATE="none" ;;
        /find-gap)       OP="find-gap";       GATE="none" ;;
        /handoff)        OP="handoff";        GATE="none" ;;
        /pickup)         OP="pickup";         GATE="none" ;;
        /bb-status)         OP="bb-status";         GATE="none" ;;
        /bb)             OP="bb";             GATE="none" ;;
        *) exit 0 ;;
    esac

    TMP="$STATUS_FILE.tmp"
    printf '{\n  "contract_version": 1,\n  "operation": "%s",\n  "phase": "%s",\n  "gate": "%s",\n  "approval_required": %s,\n  "started_at": "%s",\n  "updated_at": "%s",\n  "session_id": "%s",\n  "exit_status": "unknown"\n}\n' \
        "$OP" "$PHASE" "$GATE" "$APPROVAL" "$NOW" "$NOW" "$SID" > "$TMP" 2>/dev/null || { rm -f "$TMP" 2>/dev/null; exit 0; }
    mv "$TMP" "$STATUS_FILE" 2>/dev/null || { rm -f "$TMP" 2>/dev/null; exit 0; }
    printf '{"ts":"%s","session_id":"%s","event":"operation_launched","operation":"%s"}\n' \
        "$NOW" "$SID" "$OP" >> "$EVENTS_FILE" 2>/dev/null
    exit 0
fi

if [ "$EVENT" = "Stop" ]; then
    [ -f "$STATUS_FILE" ] || exit 0
    TMP="$STATUS_FILE.tmp"
    sed 's/"updated_at": "[^"]*"/"updated_at": "'"$NOW"'"/' "$STATUS_FILE" > "$TMP" 2>/dev/null || { rm -f "$TMP" 2>/dev/null; exit 0; }
    mv "$TMP" "$STATUS_FILE" 2>/dev/null || { rm -f "$TMP" 2>/dev/null; exit 0; }
    printf '{"ts":"%s","session_id":"%s","event":"turn_ended"}\n' \
        "$NOW" "$SID" >> "$EVENTS_FILE" 2>/dev/null
    exit 0
fi

exit 0
