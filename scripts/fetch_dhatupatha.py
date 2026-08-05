#!/usr/bin/env python3
"""Fetch the complete MIT-licensed Vidyut Dhātupāṭha."""
from pathlib import Path
from urllib.request import urlopen
import hashlib

URL = "https://raw.githubusercontent.com/ambuda-org/vidyut/main/vidyut-prakriya/data/dhatupatha.tsv"
OUT = Path(__file__).resolve().parents[1] / "data" / "dhatupatha.tsv"

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists() and OUT.stat().st_size > 10_000:
        print(f"Using existing {OUT}")
        return
    with urlopen(URL, timeout=60) as r:
        payload = r.read()
    if not payload.startswith(b"code\tdhatu\tartha"):
        raise RuntimeError("Unexpected Dhātupāṭha payload.")
    OUT.write_bytes(payload)
    print(f"Wrote {OUT} ({len(payload):,} bytes)")
    print("sha256", hashlib.sha256(payload).hexdigest())

if __name__ == "__main__":
    main()
