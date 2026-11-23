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
foreach ($name in @('coordinates','architecture','experiments','gantt','method','workflow','t41-flow','t41-search','t41-test','t41-size','t41-oppoint','t41-gap','t41-curves','t41-pr','p2-pipeline','p2-kofn')) {
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
PDF acceptance is confirmed. Conversion alone is not acceptance: compare equations,
captions, figure/table references, citations and pagination with the PDF. No Word copy is
marked ready until rendering and content/layout comparison pass.

After the LaTeX build above, build the Word copy from this directory (needs Pandoc 3.x,
`winget install JohnMacFarlane.Pandoc`, plus Microsoft Word and uv):

```powershell
powershell -ExecutionPolicy Bypass -File tools/build-docx.ps1
```

It writes `build/main-word-draft.docx` and `build/main-word-check.pdf` (Word's export,
for comparison only). The steps are in `tools/`:

| File | Role |
|---|---|
| `docx_prep.py` | Flattens the chapters and rewrites custom table macros as plain tabulars; copies heading, table, figure and equation numbers from `build/main.aux` and `build/main.toc` |
| `docx-refs.lua` | Places the bibliography before the appendices |
| `ieee-min.csl` | Minimal numeric citation style for `--citeproc`; numbering follows citation order as in IEEEtran |
| `docx-format.ps1` | Word automation: A4, margins, fonts, 1.5 spacing, table rules, title page, contents and lists |

Known differences from the PDF: equation numbers are typed text, the bibliography is a
simplified IEEE style, front matter has arabic page numbers and there is no running
header. The title-page text is duplicated in `docx_prep.py`; the script stops if it no
longer matches `main.tex`.

## T41 figures from saved predictions

`figures/t41-pr.csv` and the annotated example images in `figures/private/` come from the
saved predictions of frozen-test job 820 (Ahmed's evidence archive, SHA-256
`d8d5e039…`) and the local IEDXray test set. From the repository root:

```powershell
uv run --locked --with-requirements environments/evaluation.in --with pillow python docs/report/tools/t41_figures.py --run <extracted>/runs/generic-frozen-test-20261123 --annotations data/IEDXray/annotations/binary_explosive_det_test.json --images data/IEDXray/Test
```

The script checks the prediction and annotation hashes and stops unless AP@[.50:.95]
reproduces 41.5886 and 48.0502 exactly. `figures/private/` holds dataset scans and is
ignored by Git; without it the report builds with a placeholder note in place of the
example figure.

## Acceptance review

Use appendix R01–R15 coverage, then both handbook rubrics. Check exact app/research
revisions and actual run records, final contributions, reference metadata, official
forms and filename. Chapter 5 now includes the completed reduced generic training
study and frozen test job 820, linked to `docs/t41-results.md`. This does not close
whole-report acceptance, specific-task evaluation or repeated-seed studies. Retain report review on 23 Nov,
submission 24 Nov 17:00 UTC+4 and separate collection obligation on 30 Nov.
