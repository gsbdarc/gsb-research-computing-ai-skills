#!/usr/bin/env python3
"""
generate_grimoire.py — Create ~300 spell files for the Day 1 Grimoire Vault exercise.

Usage:
    python generate_grimoire.py [--output-dir PATH] [--seed INT] [--count INT]

Output: files named  name_element_tier_type_mastery.spell
        e.g.         thunderstrike_lightning_3_offensive_storm.spell

After generation, pre-stage the grimoire on the Yens before Day 1:
    scp -r grimoire/ SUNetID@yen.stanford.edu:/scratch/rf_bootcamp_2026/grimoire/

Students copy the vault to their home directory during the Scroll Transfer room:
    scp -r SUNetID@yen.stanford.edu:/scratch/rf_bootcamp_2026/grimoire/ ~/
"""

import argparse
import os
import random

ELEMENTS = ['fire', 'ice', 'lightning', 'earth', 'wind']
TIERS = [1, 2, 3, 4, 5]
TYPES = ['offensive', 'defensive', 'utility', 'healing']

# Each element's mastery suffix (the 5th field)
MASTERIES = {
    'fire': 'meteor',
    'ice': 'blizzard',
    'lightning': 'storm',
    'earth': 'quake',
    'wind': 'gale',
}

# Spell name pools per element (~10 each)
NAMES = {
    'fire': [
        'fireball', 'emberblast', 'cinderwave', 'ignite', 'flamewall',
        'pyroclasm', 'ashstrike', 'solarflare', 'heatray', 'scorch',
    ],
    'ice': [
        'icebolt', 'frostbite', 'glacierwall', 'chilledge', 'snowburst',
        'hailstorm', 'deepfreeze', 'crystalshield', 'permafrost', 'sleetwave',
    ],
    'lightning': [
        'thunderstrike', 'voltarc', 'staticburst', 'shockwave', 'chainbolt',
        'sparkwall', 'overcharge', 'ionicblast', 'galvanicpulse', 'stormcall',
    ],
    'earth': [
        'earthquake', 'rockwall', 'mudslide', 'stonebind', 'terrashift',
        'bouldertoss', 'tremblesherd', 'dustdevil', 'sandstorm', 'crystalspike',
    ],
    'wind': [
        'galeforce', 'cyclonewall', 'airblade', 'gustshield', 'sirocco',
        'tornadopunch', 'jetstream', 'vortexseal', 'tempestblast', 'whirlwind',
    ],
}


def generate(output_dir: str, seed: int, target: int) -> None:
    random.seed(seed)
    os.makedirs(output_dir, exist_ok=True)

    files = []

    # Phase 1: one file per (element, tier, type) combo — ensures coverage
    for element in ELEMENTS:
        for tier in TIERS:
            for spell_type in TYPES:
                name = random.choice(NAMES[element])
                mastery = MASTERIES[element]
                files.append((name, element, tier, spell_type, mastery))

    # Phase 2: random fill to reach ~target (introduces variety + some duplicates)
    while len(files) < target:
        element = random.choice(ELEMENTS)
        tier = random.choice(TIERS)
        spell_type = random.choice(TYPES)
        name = random.choice(NAMES[element])
        mastery = MASTERIES[element]
        files.append((name, element, tier, spell_type, mastery))

    # Phase 3: shuffle so files aren't element-clustered (that's the exercise)
    random.shuffle(files)

    written = 0
    for name, element, tier, spell_type, mastery in files:
        filename = f"{name}_{element}_{tier}_{spell_type}_{mastery}.spell"
        path = os.path.join(output_dir, filename)
        with open(path, 'w') as f:
            f.write(f"element={element}\ntier={tier}\ntype={spell_type}\n")
        written += 1

    print(f"Generated {written} spell files in {output_dir}/")
    print(f"Seed: {seed}  (rerun with --seed {seed} to reproduce exactly)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate grimoire spell files for Day 1 exercise.")
    parser.add_argument('--output-dir', default='grimoire', help='Directory to write spell files into')
    parser.add_argument('--seed', type=int, default=2026, help='Random seed for reproducibility')
    parser.add_argument('--count', type=int, default=300, help='Approximate number of spell files to generate')
    args = parser.parse_args()

    generate(args.output_dir, args.seed, args.count)


if __name__ == '__main__':
    main()
