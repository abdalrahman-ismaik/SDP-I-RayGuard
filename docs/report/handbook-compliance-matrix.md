# Handbook compliance matrix — SDP I final report (draft, 22 Nov 2026)

Working document for the report. Sources: `docs/final-report-requirements.md`, the Fall 2026 SDP I handbook (§4, §5.1.1, §5.1.2, §5.4, §6, §7, typical structure p. 21, rubrics), and the attached proposal. Status key: **done** = present in the draft and checked; **partial** = present with a stated gap; **open** = needs an action; **human** = needs a person (signature, confirmation, cover or form).

## A. Structure

| Requirement (handbook) | Where in draft | Status | Action |
|---|---|---|---|
| Title page | `main.tex` title page | partial | Official cover, project number, roster: **human** |
| Abstract about 200 words | `main.tex` abstract | done | 198 words (22 Nov count) |
| Table of contents | `main.tex` | done | — |
| Ch.1 Introduction: goals, motivation, method | `chapters/01-introduction.tex` | done | — |
| Ch.1 technical background and literature and patent search | Chapter 1, Table 1.2 | partial | Literature and patent search record added; IBM US10977755B2 claims partly read from text page; Infosys applications unread (404); USPTO full-text search not exhaustive |
| Ch.1 GitHub details and AI-prompt disclosure | Appendix C; Chapter 1 | partial | Sanitized prompts and per-student contributions: **human** |
| Ch.2 Requirements and system specification | `chapters/02-system-overview.tex` | done | — |
| Ch.3 Engineering model, limitations and assumptions | `chapters/03-theory.tex` | done | — |
| Ch.4 Concept generation and design evaluation | `chapters/04-design.tex` | done | — |
| Ch.5 Implementation and Fabrication | `chapters/05-implementation.tex` | done | Title changed; software-only note added |
| Ch.6 Conclusions: summary, critical appraisal, further work | `chapters/06-conclusions.tex` | done | — |
| Appendix: project management | Appendix A | done | Gantt rebuild (step 3) |
| Appendix: risk and required forms | Appendix B | partial | Official forms and signatures: **human** |
| Appendix: contributions | Appendix C | partial | Per-student confirmation: **human** |

## B. References and sources

| Requirement | Status | Action |
|---|---|---|
| Minimum 10 references | done (10 entries) | Add verified papers and books (step 2) |
| Prefer papers and books | partial (9 of 10 are arXiv/misc) | Replace or add journal and conference sources |
| Access dates for internet sources | partial | Add access dates to every web or arXiv entry |
| No Wikipedia or non-credible sources | done | Keep |
| Citation style | done | IEEEtran in `main.tex`; build has 0 undefined citations (22 Nov) |
| Cite reproduced figures | done (figures are original) | Keep provenance register |

## C. Writing and figures

| Requirement | Status | Action |
|---|---|---|
| Self-contained captions | partial | Review each caption (step 3) |
| Acronyms defined at first use | partial | Check abbreviations list against text |
| No copied paragraphs; quotations marked | not checked | Run a text-overlap check against sources (step 2) |
| Professional figures and tables | partial | Restyle tables and diagrams (step 3) |
| Gantt chart (§4): horizontal bars, dependencies, effort in hours, duration in days, subtasks ≤ 2 days, inputs, outputs, contingency, responsibilities | open | Rebuild to handbook form; effort marked "actual effort unreported" where not recorded (step 3) |

## D. Format (§5.1.2)

| Requirement | Status | Action |
|---|---|---|
| 40–80 pages excluding front matter and appendices | partial (body is about 18 pages, PDF pp. 8–25, from the 36-page build) | Add the semester record and the matrix content; do not pad (step 3) |
| A4, single-sided | done | — |
| 1.5 or double line spacing | done (`onehalfspacing`) | — |
| About 25 mm margins | done (`margin=25mm`) | — |
| Five final copies plus personal copy; confidentiality | human | Confirm distribution route with coordinator |

## E. Rubrics (handbook; supervisor 50%, examiner 50%)

| Criterion | Where the evidence lives | Status |
|---|---|---|
| GitHub: organisation, commit history, individual contributions, version control | Appendix C, repository | partial (human confirmation) |
| Report: problem and objectives | Ch.1 | done |
| Report: technical methodology | Ch.3, Ch.4 | done |
| Report: implementation and results | Ch.5 | partial (no final metrics) |
| Report: quality | whole | open (layout check) |
| Presentation and demo | Appendix / runbook, out of report scope | human |

## F. Dates and open conflicts (reported, not resolved)

| Item | Conflict | Status |
|---|---|---|
| Report deadline | 24 Nov 17:00 UTC+4 (owner) vs 27 Nov (pasted notice) | open conflict |
| Collection | Batch 1 by 15 Oct (historical) vs 30 Nov overall | open conflict |
| Collection count | 500 target vs 577 paths and 478 distinct payloads | open conflict |
| Round 1 allocation | F03 one item per student vs C01 all four families per student | open conflict |
| PR #21 status | merged (tasks T40) vs open (status/tasks line 61) | open conflict |
| Logo | A04 adoption (progress heading) vs A03 approved 28 Sep (status) | open conflict |
| CVCI 2027 deadline | 30 Nov official site vs 5 Dec invitation | open conflict |
| ISDIA organiser | UOWD (email) vs UOWD host with IRC partner (site) | open conflict |
| Poster timeline | 30 Sep, 14 Oct, 17 Oct revision vs 20 Oct confirmation | open conflict |
| Evidence status | T22 "verified" on owner confirmation alone | note |

## G. Human-only items (agents must not complete)

- Official cover, project number, final roster, supervisor details.
- Signatures on the Risk Assessment and Health and Safety forms; declaration wording.
- Student contribution confirmations and sanitized AI-prompt excerpts.
- Approved screenshots, final metrics, distribution clearance.
