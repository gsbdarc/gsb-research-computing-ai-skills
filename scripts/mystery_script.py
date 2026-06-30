#!/usr/bin/env python3
"""
Mystery script — profile me.

How long does it run? How much memory does it use?
Measure first, then decide your #SBATCH directives.
"""
import os
import re
import glob
from collections import defaultdict

SPELL_DIR = os.path.expanduser("~/grimoire")


def load_spells(spell_dir):
    paths = sorted(glob.glob(os.path.join(spell_dir, "**", "*.spell"), recursive=True))
    corpus = []
    for p in paths:
        with open(p) as f:
            corpus.append((p, f.read()))
    return corpus


def build_index(corpus):
    index = defaultdict(list)
    for path, text in corpus:
        tokens = re.findall(r"\b[a-z]{3,}\b", text.lower())
        for pos, token in enumerate(tokens):
            index[token].append((path, pos))
    return index


def search(corpus, patterns):
    results = {}
    for pat in patterns:
        rx = re.compile(pat, re.IGNORECASE)
        hits = []
        for path, text in corpus:
            hits.extend(rx.findall(text))
        results[pat] = hits
    return results


def main():
    print(f"Loading from {SPELL_DIR} ...")
    corpus = load_spells(SPELL_DIR)
    print(f"  {len(corpus)} files loaded")

    print("Building index ...")
    index = build_index(corpus)
    print(f"  {len(index):,} unique tokens")

    print("Searching patterns ...")
    patterns = [r"\b\w{8,}\b", r"_[0-9]+_", r"[A-Z][a-z]+[A-Z]"]
    results = search(corpus, patterns)
    for pat, hits in results.items():
        print(f"  {pat!r}: {len(hits)} matches")

    total_entries = sum(len(v) for v in index.values())
    print(f"\nIndex entries in memory: {total_entries:,}")
    print("Done.")


if __name__ == "__main__":
    main()
