#!/usr/bin/env python3
"""Generate the complete linked Markdown proof for the kta project."""
from __future__ import annotations

import csv
import io
import json
import re
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "vyakaranamlikhitam" / "kta" / "kta-process-map.md"
DHATUPATHA_URL = (
    "https://raw.githubusercontent.com/ambuda-org/vidyut/"
    "main/vidyut-prakriya/data/dhatupatha.tsv"
)

GANA_NAMES: dict[int, tuple[str, str]] = {
    1: ("भ्वादिगणः", "bhvādi-gaṇaḥ"),
    2: ("अदादिगणः", "adādi-gaṇaḥ"),
    3: ("जुहोत्यादिगणः", "juhotyādi-gaṇaḥ"),
    4: ("दिवादिगणः", "divādi-gaṇaḥ"),
    5: ("स्वादिगणः", "svādi-gaṇaḥ"),
    6: ("तुदादिगणः", "tudādi-gaṇaḥ"),
    7: ("रुधादिगणः", "rudhādi-gaṇaḥ"),
    8: ("तनादिगणः", "tanādi-gaṇaḥ"),
    9: ("क्र्यादिगणः", "kryādi-gaṇaḥ"),
    10: ("चुरादिगणः", "curādi-gaṇaḥ"),
    11: ("कण्ड्वादिगणः", "kaṇḍvādi-gaṇaḥ"),
}

BASE_RULES = ["AS-1-1-26", "AS-3-2-102"]


def anchor(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def sa_iast(text: str) -> str:
    return f'<i lang="sa-Latn">{esc(text)}</i>'


def sa_deva(text: str) -> str:
    return f'<span lang="sa-Deva">{esc(text)}</span>'


def slp1_to_iast(text: str) -> str:
    return transliterate(text, sanscript.SLP1, sanscript.IAST)


def deva_to_iast(text: str) -> str:
    return transliterate(text, sanscript.DEVANAGARI, sanscript.IAST)


def load_json(name: str) -> Any:
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


def load_dhatupatha() -> list[dict[str, str]]:
    with urllib.request.urlopen(DHATUPATHA_URL, timeout=90) as response:
        payload = response.read().decode("utf-8")
    rows = list(csv.DictReader(io.StringIO(payload), delimiter="\t"))
    if len(rows) < 1500:
        raise RuntimeError(f"Dhātupāṭha unexpectedly short: {len(rows)} rows")
    return rows


def rule_key(rule: dict[str, str]) -> tuple[int, ...]:
    return tuple(int(part) for part in rule["number"].split("."))


def clean_root_key(text: str) -> str:
    return re.sub(r"[~\\^/ ]", "", text)


def resolve_root(example: dict[str, Any], roots: list[dict[str, str]]) -> dict[str, str] | None:
    exact = next((row for row in roots if row["code"] == example.get("code")), None)
    if exact:
        return exact
    target = clean_root_key(example.get("slp1", ""))
    candidates: list[tuple[int, dict[str, str]]] = []
    for row in roots:
        source = clean_root_key(row["dhatu"])
        score = 0
        if source == target:
            score = 100
        elif source.rstrip("aAiIuUfFxXeEoO") == target:
            score = 95
        elif source.startswith(target):
            score = 85
        elif target.startswith(source):
            score = 75
        if score:
            candidates.append((score, row))
    return max(candidates, key=lambda pair: pair[0])[1] if candidates else None


def local_use_id(gana: int, rule_id: str) -> str:
    return f"use-g{gana:02d}-{rule_id.lower()}-u01"


def derivation_id(gana: int, example: dict[str, Any]) -> str:
    return f"deriv-g{gana:02d}-{anchor(example['slp1'])}-kta"


def root_id(code: str) -> str:
    return "dhatu-" + code.replace(".", "-")


def global_rule_id(rule_id: str) -> str:
    return "rule-" + rule_id.lower()


def category_id(category: str) -> str:
    return "category-" + category.lower().replace("_", "-")


def rule_source_url(number: str) -> str:
    a, b, c = number.split(".")
    return f"https://ashtadhyayi.com/sutraani/{a}/{b}/{c}"


def validate_links(markdown: str) -> None:
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', markdown))
    targets = set(re.findall(r"\]\(#([^)]+)\)", markdown))
    missing = sorted(targets - anchors)
    if missing:
        raise RuntimeError("Missing internal anchors: " + ", ".join(missing[:30]))
    if len(re.findall(r'<a id="chapter-\d{2}"></a>', markdown)) != 11:
        raise RuntimeError("Expected all eleven gaṇa chapters")
    if '<a id="preamble-1"></a>' not in markdown or '<a id="preamble-2"></a>' not in markdown:
        raise RuntimeError("Both preambles are required")


def main() -> None:
    rules: list[dict[str, str]] = sorted(load_json("rules.json"), key=rule_key)
    examples: list[dict[str, Any]] = load_json("examples.json")
    categories: dict[str, dict[str, str]] = load_json("categories.json")
    dhatus = load_dhatupatha()

    roots_by_gana: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in dhatus:
        try:
            gana = int(row["code"].split(".")[0])
        except (ValueError, IndexError):
            continue
        if gana in GANA_NAMES:
            roots_by_gana[gana].append(row)

    rule_by_id = {rule["id"]: rule for rule in rules}
    resolved: dict[int, list[tuple[dict[str, Any], dict[str, str] | None]]] = defaultdict(list)
    for example in examples:
        resolved[example["gana"]].append(
            (example, resolve_root(example, roots_by_gana[example["gana"]]))
        )

    lines: list[str] = []
    add = lines.append
    add('<a id="toc"></a>')
    add("# " + sa_deva("क्तप्रक्रियामानचित्रम्") + " — the linked *⟨kta⟩* process map")
    add("")
    add("A long-term, generator-backed map for deciding and deriving the Sanskrit *⟨kta⟩* form. Sanskrit is marked as italic IAST; Devanāgarī is supplied where it preserves the source text most clearly. Verbal roots carry `√`, and affixes are enclosed in `⟨ ⟩`.")
    add("")
    add("## Table of contents")
    add("")
    add("- [Bar-down process preamble](#process-map)")
    add("- [Preamble 1 — *dhātu-gaṇāḥ*: complete Dhātupāṭha](#preamble-1)")
    for gana in range(1, 12):
        add(f"  - [Gaṇa {gana}: {GANA_NAMES[gana][1]}](#gana-{gana:02d})")
    add("- [Preamble 2 — *sūtrāṇi*: ordered rule registry](#preamble-2)")
    for gana in range(1, 12):
        add(f"- [Chapter {gana}: {GANA_NAMES[gana][1]}-padam](#chapter-{gana:02d})")
    add("- [Sandhi rules employed](#sandhi-registry)")
    add("- [Categories of composition](#composition-categories)")
    add("- [Irregular constructions by gaṇa](#irregular-by-gana)")
    add("- [Sources and generation contract](#sources)")
    add("")

    add('<a id="process-map"></a>')
    add("## Bar-down process preamble")
    add("")
    add("| Bar | Decision | Registry destination |")
    add("|---|---|---|")
    process_rows = [
        ("B0 — identity", "Resolve the exact Dhātupāṭha entry, gaṇa, indicatory markers, meaning, preverb, and intended syntax.", "[Preamble 1](#preamble-1)"),
        ("B1 — affix", "Introduce *⟨kta⟩* and register it as *niṣṭhā*.", f"[{BASE_RULES[0]}](#{global_rule_id(BASE_RULES[0])}); [{BASE_RULES[1]}](#{global_rule_id(BASE_RULES[1])})"),
        ("B2 — interpretation", "Test the ordinary resultative/passive reading and any licensed *kartari* interpretation.", f"[AS-3-4-72](#{global_rule_id('AS-3-4-72')})"),
        ("B3 — iṭ", "Apply the ārdhadhātuka *iṭ* system; do not infer *seṭ / aniṭ / veṭ* from gaṇa alone.", f"[AS-7-2-35](#{global_rule_id('AS-7-2-35')})"),
        ("B4 — root operations", "Apply substitutions, augments, and ordered phonology, recording every invoked rule once locally.", "[Preamble 2](#preamble-2)"),
        ("B5 — niṣṭhā", "Search 8.2.42ff. for substitution, lexical prescription, option, prohibition, or meaning-conditioned output.", f"[AS-8-2-42](#{global_rule_id('AS-8-2-42')})"),
        ("B6 — sandhi", "Apply only rules actually triggered by the derivation.", "[Sandhi registry](#sandhi-registry)"),
        ("B7 — audit", "Return the surface form, competing licensed forms, interpretation, sources, and unresolved commentarial questions.", "[Categories](#composition-categories)"),
    ]
    for bar, decision, destination in process_rows:
        add(f"| **{bar}** | {decision} | {destination} |")
    add("")
    add("### Gaṇa chapter map")
    add("")
    add("| Gaṇa | Dhātupāṭha registry | Derivation chapter | Entries |")
    add("|---:|---|---|---:|")
    for gana in range(1, 12):
        deva, roman = GANA_NAMES[gana]
        add(f"| {gana} | [{sa_iast(roman)} · {sa_deva(deva)}](#gana-{gana:02d}) | [chapter {gana}](#chapter-{gana:02d}) | {len(roots_by_gana[gana])} |")
    add("")
    add("[↑ Contents](#toc)")
    add("")

    add('<a id="preamble-1"></a>')
    add("# Preamble 1 — " + sa_iast("dhātu-gaṇāḥ") + ": complete Dhātupāṭha")
    add("")
    add("The source rows are reproduced in gaṇa order without silently removing indicatory markers. Each entry has a stable anchor for chapter derivations.")
    add("")
    for gana in range(1, 12):
        deva, roman = GANA_NAMES[gana]
        add(f'<a id="gana-{gana:02d}"></a>')
        add(f"## Gaṇa {gana} — {sa_iast(roman)} · {sa_deva(deva)}")
        add("")
        add(f"[Derivation chapter {gana}](#chapter-{gana:02d}) · [↑ Contents](#toc)")
        add("")
        add("| Source ID | Dhātu | Meaning/domain |")
        add("|---|---|---|")
        for row in roots_by_gana[gana]:
            code = row["code"]
            root_iast = slp1_to_iast(row["dhatu"])
            meaning_iast = slp1_to_iast(row["artha"])
            add(f'| <a id="{root_id(code)}"></a>`{code}` | {sa_iast("√" + root_iast)} | {sa_iast(meaning_iast)} |')
        add("")

    add('<a id="preamble-2"></a>')
    add("# Preamble 2 — " + sa_iast("sūtrāṇi") + ": ordered rule registry")
    add("")
    add("Rules are stored once, in Aṣṭādhyāyī order. A chapter derivation links first to its local **Sūtras used in this section** occurrence; that occurrence links here.")
    add("")
    for rule in rules:
        rid = global_rule_id(rule["id"])
        iast = deva_to_iast(rule["sutra"])
        add(f'<a id="{rid}"></a>')
        add(f"## {rule['number']} — {sa_iast(iast)}")
        add("")
        add(f"- **Devanāgarī:** {sa_deva(rule['sutra'])}")
        add(f"- **Operational record:** {esc(rule['operation'])}")
        add(f"- **Scope:** `{rule['scope']}`")
        add(f"- **Audit status:** `{rule['status']}`")
        add(f"- **Source page:** [Aṣṭādhyāyī {rule['number']}]({rule_source_url(rule['number'])})")
        add("")
        add("[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)")
        add("")

    for gana in range(1, 12):
        deva, roman = GANA_NAMES[gana]
        chapter_examples = resolved[gana]
        used_rules = list(BASE_RULES)
        for example, _ in chapter_examples:
            for rid in example["rules"]:
                if rid not in used_rules:
                    used_rules.append(rid)
        used_rules = [rid for rid in used_rules if rid in rule_by_id]

        add(f'<a id="chapter-{gana:02d}"></a>')
        add(f"# Chapter {gana} — {sa_iast(roman + '-padam')} · {sa_deva(deva)}")
        add("")
        add(f"[Gaṇa {gana} in Preamble 1](#gana-{gana:02d}) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)")
        add("")
        add(f'<a id="chapter-{gana:02d}-rules"></a>')
        add("## Sūtras used in this section")
        add("")
        for rid in used_rules:
            rule = rule_by_id[rid]
            uid = local_use_id(gana, rid)
            add(f'<a id="{uid}"></a>')
            add(f"- **{rid} local use:** [{sa_iast(deva_to_iast(rule['sutra']))}](#{global_rule_id(rid)}) — {esc(rule['operation'])}")
        add("")
        add("## Derivation bars")
        add("")
        if chapter_examples:
            for example, source_row in chapter_examples:
                did = derivation_id(gana, example)
                root_iast = deva_to_iast(example["root"])
                kta_iast = deva_to_iast(example["kta"])
                add(f'<a id="{did}"></a>')
                add(f"### {sa_iast('√' + root_iast)} → {sa_iast(kta_iast)}")
                add("")
                if source_row:
                    root_link = f"[{sa_iast('√' + root_iast)}](#{root_id(source_row['code'])})"
                    source_note = f"Dhātupāṭha `{source_row['code']}`"
                else:
                    root_link = f"[{sa_iast('√' + root_iast)}](#gana-{gana:02d})"
                    source_note = "gaṇa registry; exact source row awaits audit"
                add("| Bar | Recorded operation | Linked authority |")
                add("|---|---|---|")
                add(f"| Root identity | {root_link}; {source_note}. | [Preamble 1](#preamble-1) |")
                if "AS-3-2-102" in used_rules:
                    add(f"| Affix selection | Introduce {sa_iast('⟨kta⟩')}. | [local AS-3-2-102](#{local_use_id(gana, 'AS-3-2-102')}) |")
                if "AS-1-1-26" in used_rules:
                    add(f"| Technical designation | Register {sa_iast('⟨kta⟩')} as {sa_iast('niṣṭhā')}. | [local AS-1-1-26](#{local_use_id(gana, 'AS-1-1-26')}) |")
                for rid in example["rules"]:
                    if rid not in BASE_RULES and rid in rule_by_id:
                        add(f"| Rule-conditioned operation | Apply only in the environment recorded for `{rid}`. | [local {rid}](#{local_use_id(gana, rid)}) |")
                category_links = ", ".join(
                    f"[{cat}](#{category_id(cat)})" for cat in example["category"]
                )
                add(f"| Audit result | {sa_iast(kta_iast)}. {esc(example['note'])} | {category_links} |")
                add("")
        else:
            add("| Bar | Recorded operation | Linked authority |")
            add("|---|---|---|")
            add(f"| Root identity | Select an exact entry from [{sa_iast(roman)}](#gana-{gana:02d}). | [Preamble 1](#preamble-1) |")
            add(f"| Affix selection | Introduce {sa_iast('⟨kta⟩')}. | [local AS-3-2-102](#{local_use_id(gana, 'AS-3-2-102')}) |")
            add(f"| Technical designation | Register it as {sa_iast('niṣṭhā')}. | [local AS-1-1-26](#{local_use_id(gana, 'AS-1-1-26')}) |")
            add("| Expansion point | Add a root-specific bar only together with every newly invoked local rule use. | [Preamble 2](#preamble-2) |")
            add("")
        add("## Sandhi rules employed in this chapter")
        add("")
        sandhi_used = [rid for rid in used_rules if rule_by_id[rid]["scope"] == "sandhi"]
        if sandhi_used:
            for rid in sandhi_used:
                add(f"- [{rid}](#{local_use_id(gana, rid)})")
        else:
            add("— No sandhi rule is invoked by the currently audited derivation bars.")
        add("")
        add("## Irregular constructions in this gaṇa")
        add("")
        irregular = [
            ex for ex, _ in chapter_examples
            if "CAT-LEXICAL" in ex["category"] or "CAT-OPTIONAL" in ex["category"]
        ]
        if irregular:
            for ex in irregular:
                add(f"- [{sa_iast('√' + deva_to_iast(ex['root']))} → {sa_iast(deva_to_iast(ex['kta']))}](#{derivation_id(gana, ex)})")
        else:
            add("—")
        add("")
        add("[↑ Chapter beginning](#chapter-%02d) · [↑ Contents](#toc)" % gana)
        add("")

    add('<a id="sandhi-registry"></a>')
    add("# Sandhi rules employed")
    add("")
    sandhi_rules = [rule for rule in rules if rule["scope"] == "sandhi"]
    if sandhi_rules:
        add("| Rule | Sanskrit | Actual chapter uses |")
        add("|---|---|---|")
        for rule in sandhi_rules:
            chapter_uses = []
            for gana in range(1, 12):
                if any(rule["id"] in ex["rules"] for ex, _ in resolved[gana]):
                    chapter_uses.append(f"[chapter {gana}](#{local_use_id(gana, rule['id'])})")
            uses = ", ".join(chapter_uses) if chapter_uses else "registered; not yet invoked"
            add(f"| [{rule['id']}](#{global_rule_id(rule['id'])}) | {sa_iast(deva_to_iast(rule['sutra']))} | {uses} |")
    else:
        add("—")
    add("")
    add("[↑ Contents](#toc)")
    add("")

    add('<a id="composition-categories"></a>')
    add("# Categories of composition")
    add("")
    for cat, record in categories.items():
        add(f'<a id="{category_id(cat)}"></a>')
        cat_iast = deva_to_iast(record["name"])
        add(f"## {sa_iast(cat_iast)} · {sa_deva(record['name'])}")
        add("")
        add(esc(record["description"]))
        add("")
        members = [ex for ex in examples if cat in ex["category"]]
        if members:
            for ex in members:
                add(f"- [{sa_iast('√' + deva_to_iast(ex['root']))} → {sa_iast(deva_to_iast(ex['kta']))}](#{derivation_id(ex['gana'], ex)})")
        else:
            add("—")
        add("")
    add("[↑ Contents](#toc)")
    add("")

    add('<a id="irregular-by-gana"></a>')
    add("# Irregular constructions by gaṇa")
    add("")
    for gana in range(1, 12):
        deva, roman = GANA_NAMES[gana]
        add(f"## Gaṇa {gana} — {sa_iast(roman)}")
        irregular = [
            ex for ex, _ in resolved[gana]
            if "CAT-LEXICAL" in ex["category"] or "CAT-OPTIONAL" in ex["category"]
        ]
        if irregular:
            for ex in irregular:
                add(f"- [{sa_iast('√' + deva_to_iast(ex['root']))} → {sa_iast(deva_to_iast(ex['kta']))}](#{derivation_id(gana, ex)}) — {esc(ex['note'])}")
        else:
            add("—")
        add("")
    add("[↑ Contents](#toc)")
    add("")

    add('<a id="sources"></a>')
    add("# Sources and generation contract")
    add("")
    add(f"- Complete Dhātupāṭha registry: [Vidyut `dhatupatha.tsv`]({DHATUPATHA_URL}).")
    add("- Rule texts and operational records: [`data/rules.json`](../../data/rules.json).")
    add("- Examples: [`data/examples.json`](../../data/examples.json).")
    add("- Composition categories: [`data/categories.json`](../../data/categories.json).")
    add("- Generator: [`scripts/generate_markdown_proof.py`](../../scripts/generate_markdown_proof.py).")
    add("")
    add("The generated Markdown is the proof-of-work endpoint. Source registries and tooling remain editable elsewhere in the repository; this folder contains only the human-readable project artifact.")
    add("")
    add("[↑ Contents](#toc)")
    add("")

    markdown = "\n".join(lines)
    validate_links(markdown)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(markdown, encoding="utf-8")
    print(f"Wrote {OUT} ({len(markdown):,} characters; {len(dhatus):,} Dhātupāṭha rows)")


if __name__ == "__main__":
    main()
