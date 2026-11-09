#!/usr/bin/env python3
"""Give main.pdf the page-label metadata that matches the printed folios.

The report prints no folio on the three cover pages, roman folios i--xii on the
front matter (i--vi are baked into front-sheet.pdf), and arabic 1--50 on the
body. Neither hyperref nor xdvipdfmx can express the blank cover range, and
qpdf's --update-from-json ignores /PageLabels, so the label dictionary is
rewritten directly in the built PDF.

Only object streams are expanded (qpdf --object-streams=disable), which leaves
the image and font streams byte-for-byte untouched, and the replacement is
padded to the original byte length so every cross-reference offset stays valid.

Usage: python3 tools/set_page_labels.py main.pdf   (run after latexmk)
"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Zero-based physical page indices: first page labelled i, first page labelled 1.
ROMAN_START = 3
BODY_START = 15

# Compact spelling, padded with spaces to the length of hyperref's own array.
NEW_LABELS = (
    b"<</Nums[0<</P()>>"
    + str(ROMAN_START).encode()
    + b"<</S/r/St 1>>"
    + str(BODY_START).encode()
    + b"<</S/D/St 1>>]>>"
)


def dict_span(data, start):
    """Byte span of the <<...>> dictionary that begins at start."""
    depth = 0
    i = start
    while i < len(data):
        if data.startswith(b"<<", i):
            depth += 1
            i += 2
        elif data.startswith(b">>", i):
            depth -= 1
            i += 2
            if depth == 0:
                return start, i
        else:
            i += 1
    raise ValueError("unbalanced dictionary")


def patch_labels(data):
    """Return data with the page-label dictionary replaced, same total length."""
    at = data.find(b"/PageLabels")
    if at < 0:
        sys.exit("no /PageLabels in the build; check that hyperref still writes them")
    open_dict = data.index(b"<<", at + len(b"/PageLabels"))
    start, end = dict_span(data, open_dict)
    room = end - start
    if len(NEW_LABELS) > room:
        sys.exit(f"label dictionary needs {len(NEW_LABELS)} bytes, only {room} available")
    padded = NEW_LABELS[:-2] + b" " * (room - len(NEW_LABELS)) + b">>"
    assert len(padded) == room
    return data[:start] + padded + data[end:]


def labels_of(pdf_path):
    out = subprocess.run(
        ["qpdf", "--json", str(pdf_path)], capture_output=True, text=True, check=True
    )
    return json.loads(out.stdout).get("pagelabels") or []


def pdf_pages(pdf_path):
    out = subprocess.run(
        ["pdfinfo", str(pdf_path)], capture_output=True, text=True, check=True
    ).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))


def main():
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "main.pdf").resolve()
    for tool in ("qpdf", "pdfinfo"):
        if not shutil.which(tool):
            sys.exit(f"{tool} is required")

    pages = pdf_pages(target)
    if pages <= BODY_START:
        sys.exit(f"only {pages} pages; the label boundaries need review")

    with tempfile.TemporaryDirectory() as tmp:
        expanded = Path(tmp) / "main-expanded.pdf"
        subprocess.run(
            ["qpdf", "--object-streams=disable", str(target), str(expanded)],
            check=True,
        )
        data = expanded.read_bytes()
        patched = patch_labels(data)
        assert len(patched) == len(data), "length changed; offsets would break"
        target.write_bytes(patched)

    found = labels_of(target)
    expected = [
        {"index": 0, "label": {"/St": 1}},
        {"index": ROMAN_START, "label": {"/S": "/r", "/St": 1}},
        {"index": BODY_START, "label": {"/S": "/D", "/St": 1}},
    ]
    if len(found) != len(expected) or any(
        e["index"] != f["index"] or e["label"].get("/S") != f["label"].get("/S")
        for e, f in zip(expected, found)
    ):
        sys.exit(f"page labels did not apply: {found}")

    print(f"page labels set: covers unnumbered, {ROMAN_START}->i, {BODY_START}->1")


if __name__ == "__main__":
    main()
