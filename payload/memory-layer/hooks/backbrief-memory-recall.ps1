# backbrief-memory-recall.ps1 - SessionStart hook (PowerShell).
#
# Functionally identical to backbrief-memory-recall.sh: prints a compact
# digest of this project's own memory (the newest handoff brief plus the
# tail of the decision log) to stdout, for Claude Code to inject into the
# model's context at session start (design D1, D3).
#
# Fail-silent by design (D4): any missing file, missing folder, or internal
# error prints nothing and exits 0. This script must never exit nonzero and
# must never print a partial digest.
#
# Project root resolution: this script's own location, two levels up from
# .claude\hooks\ (design D5's PowerShell half) - never an environment
# variable, so it works whether PowerShell or Git Bash is the hook shell.

try {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $projectRoot = Split-Path -Parent (Split-Path -Parent $scriptDir)
    $handoffsDir = Join-Path $projectRoot '.claude\memory\handoffs'
    $decisionsFile = Join-Path $projectRoot '.claude\memory\decisions.md'

    if (-not (Test-Path -LiteralPath $handoffsDir -PathType Container)) { exit 0 }

    # Newest brief = lexicographically last *.md filename. Correct because
    # the shipped /handoff stamps YYYY-MM-DD-HHMM- names (design D3).
    $newest = Get-ChildItem -LiteralPath $handoffsDir -Filter '*.md' -File -ErrorAction Stop |
        Sort-Object -Property Name |
        Select-Object -Last 1

    if (-not $newest) { exit 0 }

    $briefPath = $newest.FullName
    $bytes = (Get-Item -LiteralPath $briefPath -ErrorAction Stop).Length

    if ($bytes -le 4000) {
        $body = (Get-Content -LiteralPath $briefPath -Raw -ErrorAction Stop).TrimEnd("`r", "`n")
    }
    else {
        $lines = @(Get-Content -LiteralPath $briefPath -ErrorAction Stop)
        if ($lines.Count -eq 0) { exit 0 }
        $title = $lines[0]

        # From the first heading line containing "next action"
        # (case-insensitive) up to (not including) the next "## " heading,
        # or EOF.
        $nextActionLines = @()
        $grab = $false
        foreach ($line in $lines) {
            if ($line -match '^##[^#]') {
                if ($grab) { break }
                if ($line -match '(?i)next action') {
                    $grab = $true
                    $nextActionLines += $line
                }
                continue
            }
            if ($grab) { $nextActionLines += $line }
        }

        # sh's $(...) command substitution strips trailing blank lines
        # automatically; PowerShell's array join does not, so match that
        # behavior explicitly for byte-for-byte parity between the two
        # scripts.
        while ($nextActionLines.Count -gt 0 -and $nextActionLines[-1] -eq '') {
            $nextActionLines = $nextActionLines[0..($nextActionLines.Count - 2)]
        }

        if ($nextActionLines.Count -gt 0) {
            $body = "$title`n`n$($nextActionLines -join "`n")`n`n(truncated; full brief at $briefPath)"
        }
        else {
            # No "Next action" heading: degrade gracefully to title + note.
            $body = "$title`n`n(truncated; full brief at $briefPath)"
        }
    }

    $decisionsBlock = ''
    if (Test-Path -LiteralPath $decisionsFile -PathType Leaf) {
        # Matches BOTH shipped decision-log formats: the '## ' heading style and the
        # '- YYYY-MM-DD:' bullet style the scaffold's starter file uses. Requiring a
        # date on the bullet form keeps ordinary list items out. Sub-bullets are
        # indented, so an entry's rationale lines cannot match either branch.
        $headings = Get-Content -LiteralPath $decisionsFile -ErrorAction Stop | Where-Object { $_ -match '^(## |- \d{4}-\d{2}-\d{2})' }
        if ($headings.Count -gt 0) {
            $tail = $headings | Select-Object -Last 5
            $decisionsBlock = "`n`nLast 5 decision-log entries:`n$($tail -join "`n")"
        }
    }

    $marker = "[Backbrief memory] $($newest.Name) - Run /pickup for the complete read."
    Write-Output "$marker`n`n$body$decisionsBlock"
    exit 0
}
catch {
    exit 0
}
