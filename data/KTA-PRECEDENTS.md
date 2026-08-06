# kta precedent registry

`examples.json` is the single canonical, machine-readable list of currently audited `dhātu → kta` precedents.

Required fields:

- `gana`: integer `1..11`
- `code`: stable Dhātupāṭha/source identifier
- `root`: Devanāgarī dhātu
- `slp1`: tool input form
- `kta`: one or more attested outputs, separated by `/` when alternatives are recorded
- `category`: composition/audit categories
- `rules`: invoked rule identifiers
- `note`: audit qualification

Both interfaces consume this file:

```bash
python scripts/check_kta.py गम् --gana 1
python scripts/check_kta.py gam --gana 1 --kta गत --json
python3 -m http.server
# then open /vyakaranamlikhitam/kta/index.html
```

A missing entry means only “not yet in the audited precedent list.” It is not evidence that a proposed form is impossible.

The optional Heritage wrappers are pinned in `requirements-inria.txt`. They provide independent morphology/lexicon checks against Gérard Huet’s INRIA Sanskrit Heritage Platform; their output does not silently overwrite this registry.
