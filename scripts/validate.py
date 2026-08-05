#!/usr/bin/env python3
from pathlib import Path
import json, csv
ROOT=Path(__file__).resolve().parents[1]
rules={x["id"] for x in json.loads((ROOT/"data/rules.json").read_text(encoding="utf-8"))}
examples=json.loads((ROOT/"data/examples.json").read_text(encoding="utf-8"))
errors=[]
for e in examples:
    for r in e["rules"]:
        if r not in rules: errors.append(f"Unknown rule {r} in {e['root']}")
codes=set()
with (ROOT/"data/dhatupatha.tsv").open(encoding="utf-8") as f:
    for row in csv.DictReader(f,delimiter="\t"): codes.add(row["code"])
for e in examples:
    if not e["code"].endswith(".x") and e["code"] not in codes:
        errors.append(f"Example code absent from Dhātupāṭha: {e['code']}")
if errors: raise SystemExit("\n".join(errors))
print(f"Validation passed: {len(rules)} rules, {len(codes)} roots, {len(examples)} examples.")
