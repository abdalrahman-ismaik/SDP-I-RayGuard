# RayGuard SDP I report draft

Canonical source is `main.tex` with six modular chapters, appendices and a BibTeX
bibliography. This is an initial evidence-based draft, not a submission-ready report.
Follow [the requirements specification](../final-report-requirements.md); T38 is the
sole backlog. Personal names/IDs, contribution confirmations, official cover/forms,
signatures, approved screenshots and distribution clearance
remain outstanding. The owner explicitly authorized publishing this draft source to the
project GitHub repository on 22 November 2026. This does not make the report submission-
ready or clear distribution of an assembled PDF/Word copy, signed forms or private
receipts; resolve the handbook/course distribution conflict before those are shared.

## Build

From this directory, with MiKTeX/TeX Live and Python-independent native tools:

```powershell
New-Item -ItemType Directory -Force build | Out-Null
foreach ($name in @('coordinates','architecture','experiments','gantt')) {
    lualatex -interaction=nonstopmode -halt-on-error -output-directory=build "figures/$name.tex"
    pdftoppm -png -singlefile -r 180 "build/$name.pdf" "figures/$name"
}
lualatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
bibtex build/main
lualatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
lualatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

If BibTeX cannot resolve its working directory, run `bibtex main` inside build with
`BIBINPUTS` set to the parent source directory for that process only. Do not change
global TeX settings. All generated build files stay ignored. Figures are original
illustrations; see the provenance register. No raw scans or research PDF reproductions
are included. Compile and inspect every page; missing references/assets, overflow and
unreadable figures block final delivery. Typical handbook length is guidance; do not pad.

## Sources and Word path

The ten research entries were checked against supplied papers and primary arXiv
metadata/abstracts on 21 November 2026; the supplementary sources have not all received
full-paper deep reading. The report uses only supported high-level summaries for them.
IEDXray and FALCON detailed findings derive from inspected supplied papers and dated
project reviews. Access to the Nature web page failed; the local supplied paper was used.
The bibliography is a starting research record, not a claim that all cited experiments
were reproduced. The mistaken exploratory lookup of arXiv:1312.6114 is excluded because
it is unrelated to the report's optimizer discussion.

LaTeX remains canonical. A Word copy is required under the current course notice unless
PDF acceptance is confirmed. Establish conversion with Pandoc and compare equations,
captions, figure/table references, citations and pagination; conversion alone is not
acceptance. No Word copy is marked ready until rendering and content/layout comparison
pass. Keep any native tool downloads and conversion helpers in ignored local output.

## Acceptance review

Use appendix R01–R15 coverage, then both handbook rubrics. Check exact app/research
revisions and actual run records, final contributions, reference metadata, official
forms and filename. Chapter 5 now includes the completed reduced generic training
study and frozen test job 820, linked to `docs/t41-results.md`. This does not close
whole-report acceptance, specific-task evaluation or repeated-seed studies. Retain report review on 23 Nov,
submission 24 Nov 17:00 UTC+4 and separate collection obligation on 30 Nov.
