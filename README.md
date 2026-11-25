# VeerDrishti — Major Project Report

This repository contains the editable LaTeX source and generated PDF for the
**VeerDrishti: Combat Vision System** final-year project report for the
**2026–2027** academic year. The repository is a report package; the Android
application source itself is not included here.

The final generated report is [`main.pdf`](main.pdf). Edit the source files,
rebuild the PDF, inspect the result, and never edit the PDF directly.

## Final verified status

The current report package is the final checked report version before physical
printing and approval:

- final PDF: `main.pdf`;
- total length: **65 pages**;
- page size: **A4** (`595.28 × 841.89 pt`);
- final file size: approximately **13.0 MB**, below the requested 15 MB limit;
- every raster image in the report is a PNG;
- PDF page labels follow the printed folios: the three cover pages are
  unnumbered, the front matter reads **i–xii**, and the body runs **1–50**, so a
  viewer's page box matches the page in hand;
- the PDF outline carries the same order: the cover, certificate and declaration,
  every Roman preliminary page titled with its number, then each chapter,
  `PUBLICATION DETAILS`, `REFERENCES`, `APPENDIX A` and `APPENDIX B`;
- Chapter 2 — Literature Survey: body pages **7–18**;
- Chapter 6 — Implementation: body pages **26–32**;
- Chapter 7 — Result: body pages **33–39**;
- Conclusion (Chapter 8): body page **40**;
- Publication Details occupy pages **41–43**, between the conclusion and the
  references: **A** ICSTIM 2026 conference paper (page 41, presented on
  **29 October 2026**, with the **Best Paper Award**), **B** DRDO synopsis
  (page 42), **C** college project expo (page 43, with the **Best Project Award**
  and both award certificates on the same page);
- References: body pages **44–45**;
- Appendix A occupies pages **46–49**;
- Appendix B occupies page **50** and carries the guide, award, and review
  photographs on a single untitled page;
- the final Table of Contents occupies three pages, labelled **vii–ix**;
- the final abstract is below the VTU 100-word limit and uses the available
  evidence-aligned 11.9–21.3 FPS wording;
- the contents entries carry no citation markers, while each of the eleven
  Literature Survey section headings ends with its source marker `[1]`–`[11]`;
- every contents and list entry shows only the page on which the item starts,
  never a page range;
- the report package is 65 pages and closes with the publication details and the
  photograph appendix;

The LaTeX build completed successfully with no fatal errors, undefined
references, or overfull boxes. `git diff --check` passed and generated auxiliary
files were removed after the final build. Underfull-box warnings may remain in
some long paragraphs or tables because line-end hyphenation is intentionally
disabled; these do not indicate clipped or overflowing text.

The report is ready for the remaining **physical** steps: guide approval,
corrections if requested, signatures, seals, viva fields, printing, binding, and
separate software-source handover.

## Build the report

The report uses XeLaTeX, `latexmk`, Biber, `biblatex-ieee`, and Times New Roman.
Run these commands from the repository root. Rebuild the institutional front
sheet first when any file under `sections/01_...` through `sections/09_...` or
`front_layout.tex` changes:

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -file-line-error front-sheet.tex
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
python3 tools/set_page_labels.py main.pdf   # viewer page labels i–xii, 1–50
pdfinfo main.pdf                 # page count and A4 check
pdffonts main.pdf                # embedded-font check
latexmk -c front-sheet.tex       # remove front-sheet auxiliary files
latexmk -c main.tex              # remove generated auxiliary files, keep PDF
```

The successful build creates `main.pdf` in the repository root. The final
checked report is 65 A4 pages. `tools/set_page_labels.py` must run after
`latexmk`: LaTeX cannot express the unnumbered cover range, so the script
rewrites the page-label dictionary of the built PDF (expanding only object
streams, then patching the catalogue at its original byte length) and leaves
every image and font stream untouched. A clean build requires XeLaTeX, `latexmk`, Biber,
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
front-sheet.tex                               Rebuildable institutional front sheet
report.sty                                    Shared typography and layout rules
front_layout.tex                              Named front-page coordinates
front-sheet.pdf                               Maintained nine-page institutional front matter
sections/                                     Front matter, lists, contents, submissions
chapters/                                     Main report chapters
appendices/                                   Source listing and project photographs
images/                                       Logos, diagrams, screenshots and photos
images/icstim-abstract-cropped.png             Cropped raster of the ICSTIM submission
images/with_guide.png                          Project group with the guide and awards
images/best_paper.png                          Best Paper Award presentation, ICSTIM 2026
images/best_project.png                        Best Project Award, college project expo
images/best_project_chauhan.png                Best Project Award certificate, Gaurav Chauhan
images/best_project_singh.png                  Best Project Award certificate, Gaurav Singh (rotated upright)
images/drdo-synopsis-cropped.png               Cropped raster of the DRDO synopsis
images/review01-upright.png                    Project review photograph 1
images/review02-upright.png                    Project review photograph 2
tools/set_page_labels.py                       Writes the PDF page labels after the build
literature_titles.tex                          Short titles used by the contents and bookmarks
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

`main.tex` controls the emitted order. The report currently imports the maintained
nine-page `front-sheet.pdf` so that the institutional cover, certificate,
declaration, acknowledgement, abstract page, mission/vision pages, programme
outcomes, artwork, and fixed margins remain stable. The editable files under
`sections/` document the same front matter and are used to regenerate the
maintained front sheet. The main build imports that generated nine-page PDF as a
stable front-matter unit.

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
| Body text | 12 pt, justified, 1.5 spacing | 12 pt Times New Roman, justified, 20.7 pt baseline |

The report also uses 12 pt bold running headers and footers with the project
title, academic year, department, page number, and the existing red double-rule
house style. These running rules are a presentation choice, not a separate VTU
font requirement.

### Line spacing and paragraph treatment

- The main report uses **1.5 line spacing**, matching the department reference
  report: `\setstretch{1.4276}` gives a **20.7 pt** baseline for 12 pt text.
  LaTeX's `\onehalfspacing` would give only 18 pt, because it scales the 14.5 pt
  default baseline rather than the 12 pt font size, which is visibly tighter
  than the Word setting on the reference report.
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
Arabic page numbers. The generated Table of Contents is kept within three pages
(labels vii–ix); the index on the first of them names the first contents page
only, as every list entry does. Chapter 2 begins at the foot of the first
contents page, and its paper titles are set as one flowing block, so a title
that wraps over three lines pushes the next entry down instead of overlapping
it. A wrapped paper title continues directly under the first word of that title
(the hanging indent is the measured width of the section number and its space),
level with every other wrapped entry in the contents.

### PDF navigation

The PDF carries a bookmark outline that mirrors the printed order and is bound
to the page labels: the unnumbered cover, certificate and declaration, then each
Roman preliminary page with its number in the bookmark title (`ACKNOWLEDGEMENT
(i)` … `LIST OF SNAPS (xii)`), then every chapter and section, `PUBLICATION
DETAILS`, `REFERENCES`, `APPENDIX A` and `APPENDIX B` with their Arabic pages.
Clicking a bookmark jumps to that page, and the bookmark destinations are the
pages the printed index gives for the same item.

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

- Figures and tables are numbered chapter-wise, for example `Fig 4.1` and
  `Table 7.1`. Captions and in-text references both use the abbreviated name
  without a colon, matching the department's reference report.
- Figure and table entries are maintained in the corresponding generated lists.
- Prototype screenshots are labelled as `Snap 7.1`–`Snap 7.4` and are also
  listed in the separate List of Snaps. The caption text on the page is the same
  short title as the list entry, and the snapshot label is set in the body
  weight rather than bold.
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

The nine-page institutional front sheet is now regenerated from the editable
LaTeX front-matter source with Times New Roman. The supplied BTI banner and VTU
logo remain artwork images, while the surrounding cover, certificate,
declaration, acknowledgement, abstract, mission, vision, PEO, PO, and PSO text
is typeset in Times New Roman. The final `pdffonts` audit reports only embedded
Times New Roman text fonts.

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

### Publication Details

The report includes the ICSTIM 2026 conference paper, the DRDO synopsis, and the
college project expo entry under a single **PUBLICATION DETAILS** heading placed
after the conclusion and before the References, matching the department's
reference report. The three entries are lettered **A**, **B** and **C** in the
Table of Contents instead of continuing the chapter numbers. These are additional
project-submission artifacts, not replacements for the VTU report chapters.

Every evidence image carries a snapshot number on the page itself — `A-i` for the
ICSTIM abstract, `B-i` for the DRDO synopsis, and `C-i` for the pair of expo
certificates on their single page — and the same number and description appear in
the List of Snaps. The Appendix B photographs carry no titles, captions, or list
entries; the appendix is a plain page of photographs.

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
- **Appendix B** contains the project photographs: the group with the guide
  holding the Best Project award certificates and rolling shield, the Best Paper
  Award presentation at ICSTIM 2026, the Best Project Award at the college
  project expo, and the two project review photographs.
- The VTU software-project requirement for a virus-free software disc, complete
  source/read-me material, build procedure, hardware/software requirements, and
  acknowledgement of third-party modules is an external submission deliverable.
  The Android application source is not included in this report repository.
- If the project is treated as sponsored or organization-based work, the
  department may also require an organization certificate, NOC, and accounts;
  those are not represented here because this package is prepared as an academic
  project report.

### Page count

VTU does not prescribe a 60-page count in the supplied guideline. The report was
expanded to **65 pages** following the guide's review, then trimmed to 62 pages
by combining the two expo certificates onto one page, the Appendix B photographs
onto one page, and condensing repeated discussion prose at the end of the Result
chapter. Adopting the department reference's 20.7 pt line spacing in place of
LaTeX's 18 pt loosened the text again, so Chapter 6 and the closing paragraphs of
Chapter 7 were condensed once more to hold the package at **65 pages**. The added
material is
limited to technically relevant implementation, validation, runtime
interpretation, evaluation protocol, and conclusion detail in Chapters 6, 7, and
8, plus the eleven-paper Literature Survey in Chapter 2; it does not invent new
experimental results.

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
- `chapters/literature_review.tex` — Chapter 2 survey text, section titles and
  their citation markers, and the end-of-section labels used for contents pages.
- `literature_titles.tex` — short section titles shared by the contents entries
  and the PDF bookmarks, so markers stay out of the Table of Contents.
- `sections/10_contents.tex` — fixed contents placement and generated labels.
- `sections/11_figures.tex`, `sections/12_tables.tex`, and `sections/13_snaps.tex`
  — list membership and labels.
- `sections/14_submissions.tex` — the PUBLICATION DETAILS heading, with the
  lettered entries below;
- `sections/14a_icstim.tex`, `sections/14b_drdo.tex`, and `sections/14c_expo.tex`
  — the lettered A, B and C publication details, in contents order.
- `references.bib` — bibliography records.

When changing the report abstract, rebuild the maintained `front-sheet.pdf` from
the front-matter source before rebuilding `main.pdf`, because `main.tex` imports
that PDF as the institutional front matter. The ICSTIM and DRDO source PDFs are
converted to cropped PNG evidence images in `images/` so that their content is
larger and clearer on the final publication pages.

## Final verification commands

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
python3 tools/set_page_labels.py main.pdf
qpdf --check main.pdf            # page-label patch keeps the file valid
pdfinfo main.pdf | awk '/^(Pages|Page size):/ {print}'
pdffonts main.pdf
grep -nE '(^!|Undefined|undefined|multiply defined|Overfull|Emergency stop|Fatal error|There were undefined)' main.log
git diff --check
latexmk -c main.tex
```

The expected final PDF check is 65 pages with an A4 page size. Build warnings
about underfull boxes in long prose or tables are not fatal; any overfull box,
undefined reference, missing font, or fatal error must be investigated before
printing.
