#!/usr/bin/env python3
"""Check a proposed kta form against the canonical audited precedent list."""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PRECEDENTS = ROOT / "data" / "examples.json"


def norm(text: str) -> str:
    return unicodedata.normalize("NFC", text.strip()).replace("√", "")


def load_precedents() -> list[dict[str, Any]]:
    rows = json.loads(PRECEDENTS.read_text(encoding="utf-8"))
    required = {"gana", "code", "root", "slp1", "kta", "rules", "note"}
    for index, row in enumerate(rows):
        missing = required - row.keys()
        if missing:
            raise ValueError(f"precedent {index} lacks: {', '.join(sorted(missing))}")
    return rows


def find(rows: list[dict[str, Any]], dhatu: str, gana: int | None) -> list[dict[str, Any]]:
    key = norm(dhatu)
    matches = [
        row for row in rows
        if key in {norm(row["root"]), norm(row["slp1"]), norm(row["code"])}
    ]
    if gana is not None:
        matches = [row for row in matches if row["gana"] == gana]
    return matches


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Look up or check kta forms in data/examples.json."
    )
    parser.add_argument("dhatu", help="Dhātu in Devanāgarī, SLP1, or source code")
    parser.add_argument("--gana", type=int, choices=range(1, 12))
    parser.add_argument("--kta", help="Proposed kta form to check")
    parser.add_argument("--json", action="store_true", help="Emit stable JSON")
    args = parser.parse_args()

    matches = find(load_precedents(), args.dhatu, args.gana)
    proposed = norm(args.kta) if args.kta else None
    accepted = None if proposed is None else any(
        proposed in {norm(part) for part in row["kta"].split("/")} for row in matches
    )
    result = {
        "query": {"dhatu": args.dhatu, "gana": args.gana, "kta": args.kta},
        "status": "found" if matches else "not-in-precedent-list",
        "accepted": accepted,
        "matches": matches,
        "source": str(PRECEDENTS.relative_to(ROOT)),
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif not matches:
        print("No audited precedent is recorded for that dhātu and gaṇa.")
        print(f"Canonical list: {result['source']}")
    else:
        for row in matches:
            print(f"{row['code']} | gaṇa {row['gana']} | √{row['root']} → {row['kta']}")
            print(f"rules: {', '.join(row['rules'])}")
            print(f"note: {row['note']}")
        if accepted is not None:
            print("check: " + ("matches precedent" if accepted else "does not match precedent"))

    return 0 if matches and accepted is not False else 1


if __name__ == "__main__":
    sys.exit(main())
