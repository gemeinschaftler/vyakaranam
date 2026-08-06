# vyakaranam

tools and drafts of rules and examples for learning sanskrit grammar's longstanding body of work

## व्याकरणलिखितम् — written proofs of work

- [`vyakaranamlikhitam/`](vyakaranamlikhitam/)
  - [`kta/`](vyakaranamlikhitam/kta/)
    - [Human input: dhātu + gaṇa → audited kta precedent](vyakaranamlikhitam/kta/index.html)
    - [Preambled Dhātupāṭha by examples](vyakaranamlikhitam/kta/kta-process-map.md)

Every exploratory project ends by depositing a linked, human-inspectable Markdown artifact under `vyakaranamlikhitam/<project>/`. Editable registries, source data, generators, and checker tools remain elsewhere in the repository.

## Two inputs, one function

Human and machine functions are identical: resolve a dhātu and gaṇa against the currently audited `kta` precedent list. Their *niveśa* differs:

- human: [`vyakaranamlikhitam/kta/index.html`](vyakaranamlikhitam/kta/index.html)
- machine: `python scripts/check_kta.py <dhātu> --gana <1..11> [--kta <form>] [--json]`
- canonical list: [`data/examples.json`](data/examples.json), documented in [`data/KTA-PRECEDENTS.md`](data/KTA-PRECEDENTS.md)

For local browser use:

```bash
python3 -m http.server
# open http://localhost:8000/vyakaranamlikhitam/kta/
```

The optional current Heritage wrappers are pinned in [`requirements-inria.txt`](requirements-inria.txt). They support independent checks against Gérard Huet’s INRIA Sanskrit Heritage Platform; they do not silently alter the canonical precedent list.

---

# क्तप्रक्रियामानचित्रम् — kta Process Map

A long-term, generator-backed Markdown knowledge system for deciding and deriving the `क्त` form of a Sanskrit dhātu.

## Published structure

- **Bar-down process preamble** — the reusable decision path.
- **Preamble 1 — धातुगणाः** — the complete Vidyut Dhātupāṭha, grouped into eleven gaṇa sections and equipped with stable root anchors.
- **Preamble 2 — सूत्राणि** — the rule registry in ascending Aṣṭādhyāyī order.
- **Chapters 1–11 — गणपदानि** — local “sūtras used” anchors and linked derivation bars.
- **Cross-cutting registries** — sandhi uses, composition categories with root lists, and irregular constructions by gaṇa.

Every derivation links first to the chapter-local occurrence of a rule; that local occurrence links to its single global entry in Preamble 2. Root identities link to their Dhātupāṭha entries in Preamble 1.

## Regeneration

```bash
python -m pip install indic-transliteration
python scripts/generate_markdown_proof.py
```

The generator retrieves the complete MIT-licensed Vidyut `dhatupatha.tsv`, combines it with the local rule/example registries, validates every internal link, and writes:

`vyakaranamlikhitam/kta/kta-process-map.md`

The generated process map is permission-gated: request the user’s permission before regenerating or replacing it.

## Philological status

The architecture is complete, while individual derivations remain explicitly auditable. No generated form should be promoted to “verified” without checking rule order, anuvṛtti, optionality, lexical exceptions, and commentary.

## Stable identifiers

- root: `dhatu-01-0001`
- global rule: `rule-as-8-2-42`
- local rule use: `use-g01-as-8-2-42-u01`
- derivation: `deriv-g01-gam-kta`
