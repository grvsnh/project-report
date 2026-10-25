# VeerDrishti — Major Project Report

This repository contains the editable LaTeX source for the **VeerDrishti:
Combat Vision System** final-year project report for **2026–2027**. It documents
the Android prototype and its available implementation evidence; the application source
itself is not included in this repository.

The generated report is [`main.pdf`](main.pdf). Edit the source files, rebuild
the document, and inspect the new PDF. Do not edit the PDF directly.

## Quick build

The project uses **XeLaTeX**, **latexmk**, **Biber**, and the **Times New Roman**
font. From the directory containing `main.tex`:

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The successful build leaves `main.pdf` in the repository root. The cleanup
command is `latexmk -c main.tex` and keeps the PDF. To build in VS Code,
install the LaTeX Workshop extension, open the repository folder, and run the
configured **latexmk (XeLaTeX)** recipe.

## Files

```text
main.tex                         Report entry point and page order
report.sty                       Shared typography, headings and page commands
front_layout.tex                 Named front-page placements
front-sheet.pdf                  Supplied nine-page front matter
B3 - Abstract.pdf                ICSTIM 2026 abstract submission image source
Synopsis.pdf                     DRDO Students Development Program synopsis
sections/                        Editable front matter reference, lists and contents
chapters/                        Report chapters
images/                          Logos, banner and diagrams
references.bib                   Bibliography entries
Guidelines-for-Project-work- ... VTU 2022-scheme guidelines
main.pdf                         Generated report
```

The document order is controlled by the `\input{...}` lines in `main.tex`.

The body chapters are Introduction, Literature Survey, Requirements and Analysis,
System Design, Scheduling, **Implementation (6)**, **Result (7)**, and
**Conclusion (8)**. Edit `chapters/implementation.tex` and `chapters/result.tex`
to extend the new chapters. Add matching rows to `sections/10_contents.tex` when
adding sections; their numbers, titles, and page ranges resolve through labels.
Figure and table list membership is also maintained in `sections/11_figures.tex`
and `sections/12_tables.tex`.

`\ReportPhase` and `\AcademicYear` in `report.sty` supply shared front-page
metadata and the academic year. The PDF title is set there as well.

## Prototype evidence

The report documents the current prototype description: CameraX capture,
YOLO26 Nano task variants, Flutter YOLOView, and Logcat diagnostics. Its
architecture, workflow, visual outputs, runtime readings, and schedule are
recorded directly in the report and retained within the **2026–2027** academic
year.

The Result chapter reports the displayed **11.9–21.3 FPS** readings as screenshot
observations, not a sustained benchmark. Combat-specific accuracy, a test dataset,
device specifications, and completed fine-tuning results are not established by
the current prototype material. Replace or extend those parts with actual
measurements when available. GAN augmentation, thermal fusion, and
open-vocabulary detection remain proposed extensions rather than demonstrated
prototype features.

`images/vtu-logo.png` is the supplied VTU artwork. The BTI banner is in `images/`,
with aspect ratio preserved by the shared layout. Replace the source artwork if
the institution changes its branding.

### Front pages

The first nine pages are imported from the supplied `front-sheet.pdf` so the
cover, certificate Viva area, declaration, acknowledgement, sentence case,
bold spans, artwork, margins, and vision/mission/outcome layouts match the
provided reference. The corresponding editable files in `sections/` remain in
the repository for reference but are not emitted by the final build.

After the references, the report includes the submitted ICSTIM 2026 abstract
and the DRDO Students Development Program synopsis as two additional pages
before Appendix A. Their page entries appear in the two-page contents and as
`A-i` and `B-i` in the List of Snaps.

The generated index, contents, figure list, table list, and snap list continue
to use the named placements in `front_layout.tex`. For future source-based
front-page work, use named placements:

```latex
\FrontLine{cover-university}{\textbf{VISVESVARAYA TECHNOLOGICAL UNIVERSITY}}
\FrontParagraph{certificate-body}{Your certificate text.}
```

The placement names and their measurements are kept in `front_layout.tex`.
Change wording in `sections/`; change a fixed position only when necessary in
`front_layout.tex`.

For body content, edit the matching file in `chapters/`. Add figures to
`images/`, cite sources with their keys from `references.bib`, and rebuild
after every significant change.

## Minimal Linux setup

The current preparation machine uses a user-level TinyTeX installation and
the same command-line tools listed above. First check whether the tools and
font already exist:

```sh
command -v xelatex latexmk biber tlmgr
fc-match -f '%{family}\n' 'Times New Roman'
```

If these commands succeed and the font lookup reports **Times New Roman**, no
new installation is needed.

### Ubuntu or Debian

Install only the operating-system prerequisites:

```sh
sudo apt update
sudo apt install --no-install-recommends curl ca-certificates perl xz-utils fontconfig
```

### Arch Linux

```sh
sudo pacman -S --needed curl ca-certificates perl xz fontconfig
```

### Install the user-level TinyTeX toolchain

Run this only when a suitable TeX installation is not already present. The
installer uses `~/.TinyTeX`; do not run it over an installation you want to
keep.

```sh
mkdir -p "$HOME/.local/bin"
curl -fsSL https://tinytex.yihui.org/install-bin-unix.sh \
  -o /tmp/install-tinytex.sh
TINYTEX_INSTALLER=TinyTeX-0 sh /tmp/install-tinytex.sh
export PATH="$HOME/.local/bin:$PATH"

tlmgr install latex-bin xetex latexmk biber biblatex biblatex-ieee \
  fontspec lm geometry booktabs caption enumitem etoolbox fancyhdr \
  graphics tools pgfgantt refcount setspace pgf titlesec xcolor hyperref
tlmgr path add
```

Keep `~/.local/bin` in your shell `PATH` after restarting the terminal. Do not
mix `sudo tlmgr` with a distribution-managed TeX installation. Use the package
manager that owns the TeX installation.

### Times New Roman

The source explicitly selects Times New Roman and the repository does not
bundle Microsoft fonts. For the same line breaks and page layout as the
current PDF, install the regular, bold, italic, and bold-italic font files
from a lawful source in a user font directory:

```sh
mkdir -p "$HOME/.local/share/fonts/times-new-roman"
# Copy the four licensed Times New Roman .ttf files into that directory.
fc-cache -f "$HOME/.local/share/fonts/times-new-roman"
fc-match -f '%{family}\n' 'Times New Roman'
```

If an installed substitute is selected in `report.sty`, the report will still
build, but line breaks and page counts can change.

### Verify the repository

From the repository root:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdfinfo main.pdf                 # optional: confirms pages and A4 size
pdffonts main.pdf                # optional: checks embedded fonts
latexmk -c main.tex
```

If Biber on Arch reports `libcrypt.so.1` missing, install the compatibility
package and rebuild:

```sh
sudo pacman -S --needed libxcrypt-compat
```

## VTU guideline report

The supplied **Guidelines for Final Year Project Work — 2022 scheme** were
checked against the source. The current report implements the relevant
report-preparation requirements as follows:

| Guideline | Current report |
|---|---|
| Paper and margins | A4; left 1.25 in, right 1 in, top and bottom 0.75 in |
| Spacing and body text | 1.5 line spacing; 12 pt justified body text |
| Heading sizes | Chapter label 16 pt, chapter title 18 pt, section 16 pt, subsection 14 pt |
| Front matter | Cover, certificate, declaration, acknowledgements, abstract, index, figure list and table list |
| Numbering | Roman preliminary pages and Arabic-numbered chapters |
| Figures and tables | Numbered by chapter and included in their lists |
| Abstract | Uses the official supplied abstract wording |
| References | Numbered in citation order through `biblatex` IEEE style |
| Report body | Introduction, literature survey, requirements, design, schedule, implementation, result, discussion and conclusion |

The implementation and result chapters document the available prototype
evidence.
Additional measurements, appendices, and hardware/software deliverables should
be added as they become available. Before printing or final submission,
confirm the exact certificate wording, title-page arrangement, officials,
academic year, signatures, copies, binding, appendices, and external-viva
requirements with the project guide and department. Successful compilation
does not replace that approval.

## Final check before submission

- Build `main.pdf` successfully and inspect every page visually.
- Check names, USNs, title, academic year, guide, officials and signatures.
- Preserve the official supplied abstract wording.
- Confirm that claims from papers are cited and are not presented as project measurements.
- Add implementation and evaluation evidence before calling the work complete.
- Obtain guide and department approval before printing.
