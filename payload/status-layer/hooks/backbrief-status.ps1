# backbrief-status.ps1 - status-contract hook (PowerShell).
#
# Functionally identical to backbrief-status.sh: writes the deterministic
# status contract, .claude\memory\backbrief-status.json (the current
# record) and .claude\memory\backbrief-events.jsonl (the append-only
# event log). One script serves both registered events; it reads
# hook_event_name from the hook input on stdin and dispatches:
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
# and exits 0.
#
# Project root resolution: this script's own location, two levels up from
# .claude\hooks\ (the memory layer's PowerShell half, same reason).

try {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $projectRoot = Split-Path -Parent (Split-Path -Parent $scriptDir)
    $memDir = Join-Path $projectRoot '.claude\memory'
    if (-not (Test-Path -LiteralPath $memDir -PathType Container)) { exit 0 }

    $statusFile = Join-Path $memDir 'backbrief-status.json'
    $eventsFile = Join-Path $memDir 'backbrief-events.jsonl'

    $raw = [Console]::In.ReadToEnd()
    if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
    $hookInput = $raw | ConvertFrom-Json
    $event = [string]$hookInput.hook_event_name
    $sid = [string]$hookInput.session_id
    if ([string]::IsNullOrEmpty($sid)) { $sid = 'unknown' }
    $now = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd'T'HH:mm:ss'Z'")

    if ($event -eq 'UserPromptSubmit') {
        $prompt = ([string]$hookInput.prompt).TrimStart()
        # First slash token of the prompt, letters and hyphens only. A prompt
        # that does not open with a tracked command writes nothing at all.
        $m = [regex]::Match($prompt, '^(/[a-z][a-z-]*)')
        if (-not $m.Success) { exit 0 }
        $token = $m.Groups[1].Value

        $phase = 'running'
        $approval = $false
        switch ($token) {
            '/intake'         { $op = 'intake';         $gate = 'none' }
            '/business-plan'  { $op = 'business-plan';  $gate = 'ceo-gate (planning support)' }
            '/grade'          { $op = 'grade';          $gate = 'grading rule (3-pass cap)' }
            '/grade-idea'     { $op = 'grade-idea';     $gate = 'grading rule (single pass)' }
            '/approve'        { $op = 'approve';        $gate = 'owner decision - the recorded GO in .claude/memory/decisions.md'
                                $phase = 'waiting_for_approval'; $approval = $true }
            '/next'           { $op = 'next';           $gate = 'none' }
            '/setup'          { $op = 'setup';          $gate = 'none' }
            '/demo'           { $op = 'demo';           $gate = 'none' }
            '/verify-install' { $op = 'verify-install'; $gate = 'none' }
            '/critique'       { $op = 'critique';       $gate = 'none' }
            '/council'        { $op = 'council';        $gate = 'none' }
            '/find-gap'       { $op = 'find-gap';       $gate = 'none' }
            '/handoff'        { $op = 'handoff';        $gate = 'none' }
            '/pickup'         { $op = 'pickup';         $gate = 'none' }
            '/bb-status'         { $op = 'bb-status';         $gate = 'none' }
            '/bb'             { $op = 'bb';             $gate = 'none' }
            default           { exit 0 }
        }

        $approvalJson = if ($approval) { 'true' } else { 'false' }
        $statusJson = @"
{
  "contract_version": 1,
  "operation": "$op",
  "phase": "$phase",
  "gate": "$gate",
  "approval_required": $approvalJson,
  "started_at": "$now",
  "updated_at": "$now",
  "session_id": "$sid",
  "exit_status": "unknown"
}
"@
        $tmp = "$statusFile.tmp"
        [System.IO.File]::WriteAllText($tmp, $statusJson + "`n")
        Move-Item -LiteralPath $tmp -Destination $statusFile -Force
        $eventLine = "{`"ts`":`"$now`",`"session_id`":`"$sid`",`"event`":`"operation_launched`",`"operation`":`"$op`"}"
        [System.IO.File]::AppendAllText($eventsFile, $eventLine + "`n")
        exit 0
    }

    if ($event -eq 'Stop') {
        if (-not (Test-Path -LiteralPath $statusFile -PathType Leaf)) { exit 0 }
        $body = [System.IO.File]::ReadAllText($statusFile)
        $body = [regex]::Replace($body, '"updated_at": "[^"]*"', ('"updated_at": "' + $now + '"'))
        $tmp = "$statusFile.tmp"
        [System.IO.File]::WriteAllText($tmp, $body)
        Move-Item -LiteralPath $tmp -Destination $statusFile -Force
        $eventLine = "{`"ts`":`"$now`",`"session_id`":`"$sid`",`"event`":`"turn_ended`"}"
        [System.IO.File]::AppendAllText($eventsFile, $eventLine + "`n")
        exit 0
    }

    exit 0
}
catch {
    exit 0
}
