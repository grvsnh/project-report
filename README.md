# VeerDrishti — Major Project Report

This repository contains the editable LaTeX source and generated PDF for the
**VeerDrishti: Combat Vision System** final-year project report for the
**2026–2027** academic year. The repository is a report package; the Android
application source itself is not included here.

The final generated report is [`main.pdf`](main.pdf). Edit the source files,
rebuild the PDF, inspect the result, and never edit the PDF directly.

## Build the report

The report uses XeLaTeX, `latexmk`, Biber, `biblatex-ieee`, and Times New Roman.
Run these commands from the repository root:

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdfinfo main.pdf                 # page count and A4 check
pdffonts main.pdf                # embedded-font check
latexmk -c main.tex              # remove generated auxiliary files, keep PDF
```

The successful build creates `main.pdf` in the repository root. The final
checked report is 55 A4 pages. A clean build requires XeLaTeX, `latexmk`, Biber,
the LaTeX packages used by `report.sty`, and licensed Times New Roman font files
available to XeLaTeX. Microsoft font files are not redistributed in this
repository.

For a local Linux setup, first check the toolchain:

```sh
command -v xelatex latexmk biber
fc-match -f '%{family}\n' 'Times New Roman'
```

Install TeX packages using the package manager that owns the local TeX
installation. Do not mix `sudo tlmgr` with a distribution-managed TeX
installation. Install the four licensed Times New Roman faces—regular, bold,
italic, and bold italic—in a user font directory, refresh the font cache, and
verify the font lookup before comparing line breaks or page counts.

## Report source map

```text
main.tex                                      Report entry point and page order
report.sty                                    Shared typography and layout rules
front_layout.tex                              Named front-page coordinates
front-sheet.pdf                               Maintained nine-page institutional front matter
sections/                                     Front matter, lists, contents, submissions
chapters/                                     Main report chapters
appendices/                                   Source listing and project photographs
images/                                       Logos, diagrams, screenshots and photos
references.bib                                Bibliography database
B3 - Abstract.pdf                             Submitted ICSTIM abstract artifact
Synopsis.pdf                                  Submitted DRDO synopsis artifact
Guidelines-for-Project-work- 2022 Scheme.pdf VTU 2022-scheme reference used for review
main.pdf                                      Generated final report
```

The body chapters are:

1. Introduction
2. Literature Review
3. Requirements and Analysis
4. System Design
5. Scheduling
6. Implementation
7. Result
8. Conclusion

`main.tex` controls the emitted order. The report currently imports the supplied
nine-page `front-sheet.pdf` so that the institutional cover, certificate,
declaration, acknowledgement, abstract page, mission/vision pages, programme
outcomes, artwork, and fixed margins remain stable. The editable files under
`sections/` document the same front matter and remain useful as source/reference
material. The main build does not emit those editable front-page files directly.

## VTU 2022-scheme requirements followed

The supplied **Guidelines for Final Year Project Work (2022 scheme)** were read
and checked against the current source and PDF. The following are the actual
rules implemented in the report.

### Page size, margins and printing orientation

- The report is produced on **A4 paper: 210 × 297 mm**.
- The body layout uses the VTU margins:
  - left: **1.25 inches**;
  - right: **1 inch**;
  - top: **0.75 inch**;
  - bottom: **0.75 inch**.
- The PDF pages are portrait A4 pages and are intended for one-sided printing.
- The final physical copies must be printed on A4 bond paper, hard-bound with a
  plastic covering, after guide approval.
- The PDF itself cannot prove one-sided printing, paper stock, binding, number of
  copies, or dry-toner copying; those are physical-submission requirements.

### Font, heading sizes and alignment

The main body is set in Times New Roman through `fontspec`:

| Report element | VTU value | Current implementation |
|---|---:|---|
| Chapter label, for example `Chapter 6` | 16 pt, left | 16 pt bold, left |
| Chapter title, for example `IMPLEMENTATION` | 18 pt, centred | 18 pt bold, centred |
| Section heading | 16 pt, left | 16 pt bold, left |
| Subsection heading | 14 pt, left | 14 pt bold, left |
| Body text | 12 pt, justified | 12 pt Times New Roman, justified |

The report also uses 12 pt bold running headers and footers with the project
title, academic year, department, page number, and the existing red double-rule
house style. These running rules are a presentation choice, not a separate VTU
font requirement.

### Line spacing and paragraph treatment

- The main report uses **1.5 line spacing** through `\onehalfspacing`.
- Body and table prose is justified.
- Paragraph indentation is disabled and paragraphs are separated without an
  additional paragraph gap, matching the adopted VTU layout.
- Automatic and line-end hyphenation is disabled to preserve readable word
  boundaries. This is a deliberate readability choice; it can create some
  underfull lines, but the build has no overfull-box diagnostics.

### Required report order and preliminary pages

The report includes the VTU-style flow:

1. cover page;
2. certificate page;
3. declaration page;
4. acknowledgement;
5. abstract;
6. institutional mission/vision and outcome pages;
7. table of contents;
8. list of figures;
9. list of tables;
10. list of snaps used for screenshot evidence;
11. Arabic-numbered report chapters;
12. references;
13. appendices.

The preliminary material uses Roman page labels and the report chapters use
Arabic page numbers. The generated Table of Contents is kept within two pages.

### Chapter content

- **Introduction** states the problem, motivation, objectives, methodology,
  societal relevance, feasibility, and work distribution.
- **Literature Review** surveys relevant computer-vision and edge-AI work,
  identifies the project context, and includes a comparison table.
- **Requirements and Analysis** separates functional, non-functional, hardware,
  software, and acceptance requirements.
- **System Design** documents the architecture and operational workflow.
- **Scheduling** contains the project plan and Gantt chart.
- **Implementation** documents camera capture, rotation handling, task selection,
  thresholds, overlays, runtime readings, integration boundaries, and risks.
- **Result** separates directly observed screenshot evidence from claims that
  require controlled testing.
- **Conclusion** summarizes the implemented prototype, its practical utility,
  limitations, and future work.

The last chapter therefore contains the summary, current contribution, utility,
limitations, and scope for further work expected by the guideline.

### Figures, tables, snaps and equations

- Figures and tables are numbered chapter-wise, for example `Figure 4.1` and
  `Table 7.1`.
- Figure and table entries are maintained in the corresponding generated lists.
- Prototype screenshots are labelled as `Snap 7.1`–`Snap 7.4` and are also
  listed in the separate List of Snaps.
- No mathematical equations are currently used in the report. Therefore the VTU
  SI-unit and right-justified decimal equation-number rule is not triggered. If
  equations are added later, they must use SI units and chapter-wise numbers such
  as `(3.2)` aligned on the right.

### References and academic integrity

- References are stored in `references.bib` and rendered using `biblatex` with
  the IEEE style.
- Citations appear in square-bracket numeric form and the bibliography is
  numbered in citation order.
- Literature results are presented as results of the cited papers, not as
  measurements produced by VeerDrishti.
- The report avoids presenting the current screenshots as a completed field
  validation or a combat-accuracy benchmark.

## Deliberate exceptions and how to explain them

These are intentional choices, not unnoticed formatting failures.

### Institutional mission, vision and outcome pages

The college-supplied front matter includes the institute vision and mission, the
Computer Science and Engineering vision and mission, PEOs, POs, and PSOs. These
pages are retained because they are institutional front matter expected by the
college template, even though the short VTU report-flow list does not explicitly
name every one of them.

These pages use their supplied measured layout rather than inheriting the body
chapter spacing. Their placement, wording, artwork, and margins are therefore an
institutional-template exception to the normal body style.

### Front-sheet fonts and fixed layout

The supplied institutional PDF contains its own embedded fonts and artwork. The
main report body is Times New Roman, but the imported institutional pages may
contain Calibri or Arial because the supplied template was preserved. This is
intentional: changing those pages would alter the approved college design.

The abstract page in the report front matter was corrected to stay below the VTU
100-word limit and to agree with the available evidence. The separate
`B3 - Abstract.pdf` remains the original ICSTIM submission artifact and is kept
unchanged as a record of what was submitted to that conference.

### Subsection numbering

VTU permits numbered decimal sections and subsections. The current report keeps
visible section numbers but intentionally hides subsection prefixes for a cleaner
presentation. This is a deliberate style exception. If the department requires
every subsection to display a number, set `secnumdepth` appropriately in
`report.sty` and update the contents layout before printing.

### Submission pages after References

The report includes the ICSTIM abstract submission and DRDO synopsis after
References and before Appendix A. These are additional project-submission
artifacts, not replacements for the VTU report chapters. They are explicitly
labelled in the Table of Contents and List of Snaps so an evaluator can tell
where the formal report ends and the supporting submissions begin.

### Certificates, signatures and dates

The report contains the guide, coordinator, HOD, and principal certificate
blocks, declaration fields, student signature fields, and viva examiner lines.
The blank signature, date, seal, and examiner fields are intentional because they
must be completed physically after guide and department approval. A successful
LaTeX build must not be described as proof that the report has already been
approved or signed.

### Appendices and software deliverables

- **Appendix A** contains a representative source-code listing relevant to the
  Android/YOLO integration and camera rotation path. It is not a substitute for
  handing over the complete application source.
- **Appendix B** contains project photographs.
- The VTU software-project requirement for a virus-free software disc, complete
  source/read-me material, build procedure, hardware/software requirements, and
  acknowledgement of third-party modules is an external submission deliverable.
  The Android application source is not included in this report repository.
- If the project is treated as sponsored or organization-based work, the
  department may also require an organization certificate, NOC, and accounts;
  those are not represented here because this package is prepared as an academic
  project report.

### Page count

VTU does not prescribe a 55-page count in the supplied guideline. The report was
kept at **55 pages** because that was the agreed project requirement. Page count
was achieved by adding technically relevant detail only to Chapters 6 and 7,
without inventing new experimental results.

## Evidence and claims in the final report

The available prototype evidence demonstrates:

- camera capture and display;
- portrait and landscape rotation handling;
- object-detection boxes and labels;
- segmentation overlays;
- pose keypoints and skeleton visualisation;
- configurable confidence and IoU thresholds;
- displayed runtime fields.

The Result chapter reports displayed readings between **11.9 and 21.3 FPS** and
processing-time readings between **30.8 and 62.9 ms** for the supplied
demonstration screenshots. These are configuration-specific observations, not a
sustained benchmark. The report does not claim measured combat accuracy,
annotated-dataset precision/recall/mAP, long-run thermal stability, power
consumption, or field deployment validation.

The safest explanation to an evaluator is: the current report proves the
capture-to-display prototype path and documents the visible outputs; controlled
accuracy, robustness, and deployment studies are clearly marked as future work.

## Viva-ready formatting explanation

If a teacher asks how the report follows VTU formatting, the short answer is:

> “The report is A4 with VTU margins—1.25 inches on the left, 1 inch on the
> right, and 0.75 inch at the top and bottom. The body is 12-point Times New
> Roman, justified, with 1.5 line spacing. Chapter labels are 16 point,
> chapter titles are 18 point and centred, section headings are 16 point, and
> subsection headings are 14 point. Preliminary pages use Roman numbering and
> the chapters use Arabic numbering. Figures and tables are numbered chapter-wise
> and the references use IEEE numeric citation order.”

If asked about the exceptions, explain that the institutional mission/vision and
outcome pages retain the college template, the submitted ICSTIM and DRDO pages
are clearly marked supporting artifacts, subsection numbers are intentionally
hidden for presentation, and all signatures/seals remain for physical approval.

## Final physical-submission checklist

Before printing and signing, confirm each item with the guide and department:

- guide has reviewed the final PDF and approved the corrections;
- names, USNs, project title, branch, guide, coordinator, HOD, principal, and
  academic year are correct;
- guide, coordinator, HOD, and principal signatures and seal are completed;
- declaration date and student signatures are completed;
- viva examiner names/signatures and dates are completed when applicable;
- the required number of copies is confirmed with the department;
- copies are printed one-sided on A4 bond paper and hard-bound with plastic
  covering;
- the outer-cover colour is confirmed with the department because the supplied
  guideline table does not show a filled colour value in this copy;
- the separate abstract copies requested by the department are prepared;
- the complete Android source, read-me, build/run instructions, third-party
  acknowledgements, and virus-free software handover are prepared separately;
- any organization certificate, NOC, or sponsorship paperwork is added only if
  the department classifies the project that way.

## Important files to edit

- `chapters/implementation.tex` — Chapter 6 implementation details.
- `chapters/result.tex` — Chapter 7 results, evidence boundary, and limitations.
- `sections/05_abstract.tex` — editable report abstract text.
- `report.sty` — body font, margins, spacing, heading sizes, numbering depth, and
  running header/footer rules.
- `front_layout.tex` — measured coordinates for editable institutional pages.
- `sections/10_contents.tex` — fixed contents placement and generated labels.
- `sections/11_figures.tex`, `sections/12_tables.tex`, and `sections/13_snaps.tex`
  — list membership and labels.
- `sections/14_submissions.tex` — ICSTIM and DRDO supporting pages.
- `references.bib` — bibliography records.

When changing the report abstract, update the emitted `front-sheet.pdf` page as
well, because `main.tex` imports that PDF as the institutional front matter.

## Final verification commands

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdfinfo main.pdf | awk '/^(Pages|Page size):/ {print}'
pdffonts main.pdf
grep -nE '(^!|Undefined|undefined|multiply defined|Overfull|Emergency stop|Fatal error|There were undefined)' main.log
git diff --check
latexmk -c main.tex
```

The expected final PDF check is 55 pages with an A4 page size. Build warnings
about underfull boxes in long prose or tables are not fatal; any overfull box,
undefined reference, missing font, or fatal error must be investigated before
printing.
