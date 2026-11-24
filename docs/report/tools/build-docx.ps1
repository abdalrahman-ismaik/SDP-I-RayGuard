# Build the Word copy of the report from the LaTeX source.
#
# Run from docs/report after the LaTeX build (build/main.aux and build/main.toc
# must be current):
#   powershell -ExecutionPolicy Bypass -File tools/build-docx.ps1
# Needs Pandoc 3.x, Microsoft Word and uv. Writes build/main-word-draft.docx
# and build/main-word-check.pdf (Word's own PDF export, for checking only).
$ErrorActionPreference = 'Stop'
$report = Split-Path -Parent $PSScriptRoot
Set-Location $report

$pandoc = (Get-Command pandoc -ErrorAction SilentlyContinue).Source
if (-not $pandoc) { $pandoc = Join-Path $env:LOCALAPPDATA 'Pandoc\pandoc.exe' }
if (-not (Test-Path $pandoc)) { throw 'Pandoc not found; install it with: winget install JohnMacFarlane.Pandoc' }
foreach ($f in 'build\main.aux', 'build\main.toc') {
  if (-not (Test-Path $f)) { throw "$f missing; run the LaTeX build first (see README.md)" }
}

# Fresh work folder: a lock file left by an interrupted Word run makes Word
# wait on a hidden "file in use" prompt.
$work = Join-Path $report 'build\docx'
if (Test-Path $work) { Remove-Item $work -Recurse -Force }
New-Item -ItemType Directory $work | Out-Null

uv run --locked python tools/docx_prep.py . "$work\flat.tex"
if ($LASTEXITCODE) { throw 'docx_prep.py failed' }

& $pandoc "$work\flat.tex" -f latex -t docx --resource-path=".;figures" `
  --lua-filter=tools/docx-refs.lua --citeproc --bibliography=references.bib `
  --csl=tools/ieee-min.csl -o "$work\pandoc.docx"
if ($LASTEXITCODE) { throw 'pandoc failed' }

& (Join-Path $PSScriptRoot 'docx-format.ps1') -In "$work\pandoc.docx" `
  -Out (Join-Path $report 'build\main-word-draft.docx') `
  -Pdf (Join-Path $report 'build\main-word-check.pdf')
