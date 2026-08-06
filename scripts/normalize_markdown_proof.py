#!/usr/bin/env python3
"""Normalize source anomalies in the generated kta Markdown proof.

Vidyut's Dhātupāṭha contains terminal placeholder rows in gaṇa 10 and no 11.*
rows. This layer removes the placeholders and creates an explicitly labelled
supplementary gaṇa-11 registry from the project's denominative examples.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "vyakaranamlikhitam" / "kta" / "kta-process-map.md"
EXAMPLES = ROOT / "data" / "examples.json"


def deva_to_iast(text: str) -> str:
    return transliterate(text, sanscript.DEVANAGARI, sanscript.IAST)


def sa_iast(text: str) -> str:
    return f'<i lang="sa-Latn">{text}</i>'


def main() -> None:
    text = PROOF.read_text(encoding="utf-8")

    # Remove source placeholders such as 10.0497–10.0509, whose dhātu is '-'.
    text = re.sub(
        r'^\| <a id="dhatu-[^"]+"></a>`[^`]+` \| <i lang="sa-Latn">√-</i> \|.*\n',
        "",
        text,
        flags=re.MULTILINE,
    )

    examples = [
        ex for ex in json.loads(EXAMPLES.read_text(encoding="utf-8"))
        if ex.get("gana") == 11
    ]
    if not examples:
        raise RuntimeError("Gaṇa 11 requires at least one denominative example")

    rows: list[str] = []
    for index, ex in enumerate(examples, start=1):
        code = f"11.S{index:03d}"
        root_anchor = "dhatu-" + code.lower().replace(".", "-")
        root_iast = deva_to_iast(ex["root"])
        rows.append(
            f'| <a id="{root_anchor}"></a>`{code}` | '
            f'{sa_iast("√" + root_iast)} | supplementary denominative entry; '
            'traditional source audit pending |'
        )

        old = (
            f'[{sa_iast("√" + root_iast)}](#gana-11); '
            'gaṇa registry; exact source row awaits audit.'
        )
        new = (
            f'[{sa_iast("√" + root_iast)}](#{root_anchor}); '
            f'supplementary entry `{code}`.'
        )
        text = text.replace(old, new)

    marker = (
        '<a id="gana-11"></a>\n'
        '## Gaṇa 11 — <i lang="sa-Latn">kaṇḍvādi-gaṇaḥ</i> · '
        '<span lang="sa-Deva">कण्ड्वादिगणः</span>\n\n'
        '[Derivation chapter 11](#chapter-11) · [↑ Contents](#toc)\n\n'
        '| Source ID | Dhātu | Meaning/domain |\n'
        '|---|---|---|\n'
    )
    replacement = (
        '<a id="gana-11"></a>\n'
        '## Gaṇa 11 — <i lang="sa-Latn">kaṇḍvādi-gaṇaḥ</i> · '
        '<span lang="sa-Deva">कण्ड्वादिगणः</span>\n\n'
        '[Derivation chapter 11](#chapter-11) · [↑ Contents](#toc)\n\n'
        '> Vidyut has no `11.*` rows; this is an explicitly separate '
        'supplementary denominative registry.\n\n'
        '| Source ID | Dhātu | Meaning/domain |\n'
        '|---|---|---|\n'
        + "\n".join(rows)
        + "\n"
    )
    if marker not in text:
        raise RuntimeError("Could not locate the gaṇa-11 preamble section")
    text = text.replace(marker, replacement, 1)

    text = re.sub(
        r'(\| 11 \| \[<i lang="sa-Latn">kaṇḍvādi-gaṇaḥ</i>.*?\| \[chapter 11\]\(#chapter-11\) \| )0( \|)',
        rf'\g<1>{len(rows)}\g<2>',
        text,
        count=1,
    )

    if '√-</i>' in text:
        raise RuntimeError("Unfiltered placeholder root remains")
    if '<a id="dhatu-11-s001"></a>' not in text:
        raise RuntimeError("Supplementary gaṇa-11 anchor was not created")

    PROOF.write_text(text, encoding="utf-8")
    print(f"Normalized {PROOF}; added {len(rows)} gaṇa-11 supplementary entry/entries")


if __name__ == "__main__":
    main()
