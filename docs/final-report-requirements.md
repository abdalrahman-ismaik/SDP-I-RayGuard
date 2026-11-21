# SDP I final report requirements

Recorded 21 November 2026 at the project owner's request. This is the authoritative
shared report specification; [tasks](tasks.md), T38, is the only backlog. Requirements
recorded here are not completed deliverables. Consult this specification for all
subsequent report writing, research, figures, implementation evidence and rehearsal.

## Authority and source record

- **Primary course reference:** local `docs/SDPI & SDPII Handbook/` containing
  `COSC 497 498 SDPI & SDPII Handbook_August 2026.docx`, titled Senior Design Project
  Handbook, College of Computing and Mathematical Sciences, Fall 2026. The original
  remains local. Its body text and both SDP I assessment tables were inspected on
  21 November; rendered pagination and embedded form artwork were not verified.
- Source locators: §§3–4 (planning and engineering practice), §§5.1–5.4 (report,
  presentation and writing), §6 (assessment), §7 (milestones), General Forms,
  **Typical Structure of the Final SDPI Project Report**, **SDPI Supervisor
  Assessment Form**, and **SDPI Examiner Assessment Form**. The contents lists the
  typical structures at p.21 and assessment forms at p.27; these are source-listed
  starting pages, not newly verified render page numbers. The SDP I structure's
  note points to Risk Assessment pp.13–14 and Health and Safety p.15; check the
  actual form before reproduction because text extraction does not establish layout.
- **Owner decisions, 21 November:** LaTeX is the canonical report source; use
  research papers and their verified primary references, project documentation and
  meeting records; produce meaningful figures, images, tables and a Gantt chart;
  include the applicable handbook forms and all required report parts. Prepare a
  checked Word copy alongside the LaTeX PDF unless PDF acceptance is confirmed.
- **Deadline:** owner confirms **24 November 2026**; plan for **17:00 UTC+4** from
  the supplied Blackboard field. The older 27 November report notice remains a
  recorded conflict, not permission to delay. [Course checklist](course-endgame-2026-11.md)
  retains submission instructions and presentation details.
- Specific course notices can amend submission logistics. Meetings establish agreed
  project direction; the proposal retains broader requirements. Papers establish
  published findings, inspected releases establish implementation details, and real
  execution records establish project results. Flag unresolved conflicts explicitly.

## Report coverage and traceability

The handbook calls this a typical structure and permits adaptation. Use its six SDP I
chapters as the baseline below; include tests and evaluation within Chapter 5 rather
than silently substituting the different SDP II outline. The following IDs identify
requirements for traceability, not a second task backlog. While drafting, map each ID
to actual section/figure/table labels and evidence; unmapped items stay visible gaps.

| ID | Required coverage or guidance | Planned report destination and acceptance evidence |
|---|---|---|
| R01 | Unified title page; abstract approximately 200 words; contents | Front matter. Obtain current institutional title-page format and verified project number, roster and supervisors; abstract states motivation, work actually done and supported conclusions. Add lists of figures/tables and abbreviations as project presentation choices. |
| R02 | Goals, objectives, motivation, method and report overview | Chapter 1. Measurable objectives and clear SDP I scope; distinguish original proposal, meeting amendments and unfinished scope. |
| R03 | Technical background; literature and patent search | Chapter 1. Synthesis and critical comparison of supplied papers and inspected primary sources; record actual search coverage, not invented patents or searches. |
| R04 | GitHub links, AI code-generation prompts and individual contributions | Chapter 1 and appendix. Link both research/app repositories, explain their boundary, give verified per-student contributions and sanitized relevant AI prompt/disclosure records. Each student demonstrates their work to the supervisor, ideally before presentation. |
| R05 | Requirements and system specification | Chapter 2. Functional/nonfunctional requirements, interfaces, operating conditions, failure responses, constraints and safety; trace objectives to design, implementation and evidence. Record supervisor approval only when obtained. |
| R06 | Engineering model and theoretical foundations | Chapter 3. Explain relevant mathematical/physical models, detector coordinates and task/category conventions, assumptions and limitations. Separate proposed P2 reasoning from implemented behavior. |
| R07 | Concept generation and design evaluation | Chapter 4. Alternatives, modeling/simulation actually performed, assessment criteria and justified selections; discuss technical feasibility, cost/resources and tradeoffs. |
| R08 | Implementation and fabrication | Chapter 5. Actual architecture, preprocessing, model/config/class pairing, app integration, reproducible setup, revisions and relevant development decisions. Explain software-only applicability where appropriate; do not imply lab collection was software-only. |
| R09 | Testing, results and evaluation | Chapter 5. Verification/validation, representative and failure cases, appropriate established procedures and stress/error handling. Present quantitative results only with eligible data and reproducible evidence; distinguish software tests, real inference, benchmark evaluation and scanner qualification. |
| R10 | Summary, conclusions, critical appraisal and further work | Chapter 6. Evaluate objectives against evidence, constraints and limitations; address relevant standards, ethics, safety, environmental impact and sustainability using §§4.4/4.9. Do not claim certification or standards compliance without evidence. |
| R11 | References | Minimum 10 credible references, concentrating on papers/books; web references carry access dates. Exclude Wikipedia and unreliable sources. Verify metadata and every source supporting a claim. |
| R12 | Appendices and project management | Gantt chart, dependencies, responsibilities, contingency planning, original system specification, relevant software excerpts/proofs and other supporting material as applicable. Include an existing interim progress report if available; the later notice says no new separate progress report is required. |
| R13 | Risk Assessment and Health and Safety forms | Include the official applicable forms and risk discussion; verify current templates, required signatures, recipients and placement. See forms below. |
| R14 | Declaration and other institutional paperwork | Review and include the handbook declaration/current course version as required, preserving official wording and actual human signatures. Check remaining forms for applicability; do not automatically require SDP II clearance for SDP I. |
| R15 | Submission, contribution review and presentation | Reviewed final PDF and equivalent Word copy; verified filename/project number, group submission and permitted distribution, private receipts, individual explain-backs and rehearsed demo/presentation. See T38 and the course checklist. |

### Formatting and writing

Handbook §5.1.2 gives **typical** length of 40–80 pages excluding front matter and
appendices; it is guidance, not a reason to pad the report or a verified hard minimum.
Its formatting guidance specifies A4, single-sided, 1.5 or double line spacing and
approximately 25 mm left/right margins. Default to A4, 1.5 spacing, approximately
25 mm margins and readable 11–12 pt body text unless the institutional template
requires otherwise. Font size is a project default, not a quoted handbook rule.

Use original explanation, synthesis and critical appraisal. Define acronyms, connect
chapters logically, cite quotations and revise for clarity. Every figure/table needs
a self-contained caption; cite reproduced figures. A professional visual must help
explain a requirement, method, comparison or result.

## Evidence, sources and visuals

- Build the bibliography from supplied research papers, their independently inspected
  primary references, official release documentation and approved project records.
  A paper's bibliography is a discovery source, not evidence that we read its sources.
  Verify author/title/year/venue/DOI or URL and support claims with the correct source.
- Use meeting companions and follow-ups, the proposal, research/architecture/decision
  records, audits and actual run manifests. Preserve recorded requirement, published
  finding, recommendation, unresolved question and executed result as distinct claims.
- Never substitute published scores, checkpoint metadata, image counts or synthetic
  checks for locally measured performance. Preserve the published test split; document
  label/overlap/group uncertainty and distinguish complete-device from component tasks.
  Empty detections never establish benignness. Do not invent authorship, hours or results.
- Plan architecture and data-flow diagrams; requirement/design comparison tables;
  theory/model illustrations; a dated Gantt chart; approved GUI screenshots; and
  eligible results/failure figures. Use only assets that explain the text. Reference
  each numbered visual in the body and check labels, legends, units and print readability.
- Record source, citation, permission/license or reuse review and evidence identity
  for each visual. Mark original/adapted/reproduced and illustrative/actual/recorded
  where relevant. Prefer original explanatory diagrams and vector plots/diagrams;
  inspect third-party reuse rights before including figures or dataset images.
- Gantt chart: show historical plan and evidence-backed actual progress distinctly,
  dependencies and report milestones; retain missed dates as history. Future bars
  are estimates. Do not infer working hours or backdate task acceptance.

## Forms and distribution gates

The SDP I structure expressly lists **Risk Assessment** and **Health and Safety**
forms for submission with SDP I/II reports. The Health and Safety form also says it
accompanies the SDP I final report, identifies electrical/radiation/laser/robotic/
mechanical/other hazards, requests student representative and supervisor signatures,
and directs the original to the University Safety Officer with copies bound into
proposal/report. Review real X-ray lab work with the supervisor; do not tick
software-only or declare no hazards by assumption. Risk-form artwork/fields require
visual inspection of the original before filling or reproducing them.

Preserve declaration wording and disclose assistance accurately. Never manufacture
signatures, approvals or risk ratings; filled personal/signed forms remain private
unless explicitly authorized for an appropriate distribution copy. Project Clearance
forms I/II are explicitly marked for the **SDP II final report**; require them for
SDP I only on a specific course/supervisor instruction. Historical selection/idea
forms are not automatically new final-report deliverables.

Handbook §5.1.2 mentions five final copies plus a personal copy and calls report/IP
confidential, requiring written permission to publish/distribute. The later course
notice requests Blackboard upload, email and GitHub. Obtain clarification for physical
copies and public GitHub distribution; a course delivery instruction does not settle
confidentiality. Prepare privately meanwhile. Original PDFs, scans, weights, credentials,
private paths and session records remain excluded from Git. Do not commit the handbook
or silently expose a signed report. Record actual permission and permitted audience.

## LaTeX production and submission workflow

Planned shared source layout: `docs/report/main.tex`, modular `chapters/`,
`references.bib`, approved `figures/` with provenance register, and build README.
These are future deliverables, not files created by this requirements update.
Use LuaLaTeX via `latexmk` by default, with a compatible bibliography processor;
verify available tools and record the exact reproducible build command during setup.
Do not install tools or change global configuration as part of this documentation task.
Ignore auxiliary/build files; retain only approved source and permitted deliverables.

LaTeX is canonical. Produce a PDF and a Word `.docx` copy from the same content.
Validate conversion feasibility early; equations, bibliography, numbering, captions,
cross-references, tables, figures and forms need explicit comparison and correction.
Inspect every page of both rendered outputs. The course notice accepts `.doc`/`.docx`;
use the checked Word copy unless PDF acceptance is explicitly confirmed. Format
acceptance, verified filename and project number are submission gates. Retain identical
content across the submitted and permitted email/GitHub copies, recording any approved
privacy redactions as a distinct distribution version rather than silently changing it.

## Assessment coverage

These are **within-form weights**, each totaling 100. Handbook §6 assigns supervisor
and examiner 50% each; do not apply either form alone as the course-wide weighting.

| Area | SDP I supervisor | SDP I examiner | Evidence to prepare |
|---|---|---|---|
| GitHub | 15: organization 4, history 5, individual contributions 4, version control 2 | No separate category | Accessible setup/docs, meaningful human history, traceable work and integration practices |
| Report | 20: problem/objectives 5, methodology 6, implementation/results 6, quality 3 | 20: problem/objectives 5, design/method 6, results/evaluation 6, writing 3 | R01–R15 mapped to actual report/evidence |
| Presentation | 20: content 7, technical explanation 6, delivery/visuals 4, participation 3 | 20: organization 7, technical depth 7, delivery/visuals 6 | Accurate timed narrative and each student's explanation |
| Live demo | 25: functionality 10, reliability 7, technical demonstration 5, preparation 3 | 25: functional coverage 10, robustness 8, execution 7 | Reproducible real workflow, error handling and clearly labeled fallback |
| Q&A | 20: understanding 8, justification 5, ownership 4, clarity 3 | 35: knowledge 12, reasoning 10, problem solving 8, contribution/clarity 5 | Defend methods, alternatives, failures, limitations and actual personal work |

## Completion gates

T38 owns execution state, owners and dates. Report acceptance requires R01–R15 mapped
to concrete content/evidence or an explicitly reviewed applicability decision; correct
SDP I structure and rubric coverage; verified citations/visual provenance; reviewed
forms and permissions; successful LaTeX build without missing assets/references;
visual inspection of PDF and Word; factual contribution review; and checked submission
instructions. Submission, email, publication and rehearsal complete only with actual
human action and evidence. Recording this specification completes none of those actions.
