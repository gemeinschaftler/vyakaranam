#!/usr/bin/env python3
"""Validate compiled proof PDFs when the repository contains any.

Markdown-only proof projects are valid and are checked by their own link-aware
build workflows. This validator therefore succeeds cleanly when no PDFs exist.
"""
from __future__ import annotations

import hashlib
import subprocess
import tempfile
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PROOFS = ROOT / "vyakaranamlikhitam"


def validate_pdf(path: Path) -> None:
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        raise RuntimeError(f"{path}: missing PDF header")
    if not data.rstrip().endswith(b"%%EOF"):
        raise RuntimeError(f"{path}: missing PDF EOF marker")

    reader = PdfReader(path, strict=True)
    if not reader.pages:
        raise RuntimeError(f"{path}: contains no pages")

    subprocess.run(["pdfinfo", str(path)], check=True, stdout=subprocess.DEVNULL)
    with tempfile.TemporaryDirectory() as tmp:
        prefix = Path(tmp) / "page"
        subprocess.run(
            ["pdftoppm", "-f", "1", "-singlefile", "-png", str(path), str(prefix)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if not prefix.with_suffix(".png").exists():
            raise RuntimeError(f"{path}: first page did not render")

    digest = hashlib.sha256(data).hexdigest()
    print(f"OK {path.relative_to(ROOT)} pages={len(reader.pages)} sha256={digest}")


def main() -> None:
    pdfs = sorted(PROOFS.rglob("*.pdf"))
    if not pdfs:
        print("No proof PDFs found; Markdown-only proof folders are valid.")
        return
    for pdf in pdfs:
        validate_pdf(pdf)


if __name__ == "__main__":
    main()
