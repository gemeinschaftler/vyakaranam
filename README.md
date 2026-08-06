# vyakaranam

tools and drafts of rules and examples for learning sanskrit grammar's longstanding body of work

open to editing.

## व्याकरणलिखितम् — compiled proofs of work

- [`vyakaranamlikhitam/`](vyakaranamlikhitam/)
  - [`kta/`](vyakaranamlikhitam/kta/)
    - [`kta-process-map-proof.pdf`](vyakaranamlikhitam/kta/kta-process-map-proof.pdf)

Every exploratory project ends by depositing one or more compiled, human-inspectable PDFs under `vyakaranamlikhitam/<project>/`. These proof folders contain only final PDFs; editable sources and generators remain elsewhere in the repository.

---

# क्तप्रक्रियामानचित्रम् — kta Process Map

A long-term, generator-backed LaTeX knowledge system for deciding and deriving the `क्त` form of a Sanskrit dhātu.

## Design

- **Preamble 1 — धातुगणाः** is generated from the complete MIT-licensed Vidyut `dhatupatha.tsv`.
- **Preamble 2 — सूत्राणि** is generated in ascending Aṣṭādhyāyī order.
- **Chapters 1–11 — गणपदानि** contain linked derivation bars.
- Every chapter begins with **सूत्राणि प्रयुक्तानि**. Local derivation steps link first to a local usage-anchor, which links to the global sūtra entry.
- Sandhi rules, composition categories, root-lists, and irregular constructions are registries rather than repeated prose.
- Stable semantic identifiers survive reordering and regeneration.

## Build

Requirements:

- Python 3.11+
- LuaLaTeX
- internet access for the first `make data` run

```bash
make
```

The downloaded Dhātupāṭha remains in `data/dhatupatha.tsv`; generated files are placed in `build/generated/`.

## Philological status

The architecture is complete, while the rule registry is deliberately conservative. Entries marked `core` form the initial audited backbone; entries marked `expand` are explicit expansion points. No generated form should be promoted to “verified” without checking rule order, anuvṛtti, optionality, lexical exceptions, and commentary.

## Stable identifiers

- root: `DHATU-01-0001`
- global rule: `AS-8-2-42`
- local rule use: `G01-AS-8-2-42-U01`
- derivation: `G01-DHATU-01-0001-KTA`
- sandhi use: `G01-SANDHI-AS-8-4-55-U01`
