---
layout: default
title: "Boss Gate 1"
parent: "Day 1 — The Gatehouse"
nav_order: 10
permalink: /day1/boss-gate-1/
---

# Boss Gate 1

*Iron doors. A glowing crest — the Archmage's seal — pulses cold blue across the stone. The inscription burns into view: "Prove you can find what is hidden, and leave a record of your discovery." Somewhere in the depths of `/scratch`, buried among hundreds of decoy files, a single spell bears the Archmage's true signature. The passage to Floor 2 will not open until you surface it.*

---

## 🔑 The Challenge

{: .boss }
> **Boss Battle — The Archmage's Signature**
>
> A single spell file bearing the Archmage's signature is hidden somewhere in the vault:
>
> ```
> /scratch/shared/rf_bootcamp_2026/vault/
> ```
>
> Find the file. Its name alone is not enough — read its contents to find the signature string inside.
>
> **Submit your answer:**
>
> 1. Create a file called `signature_spell.txt` in your repo containing:
>    - The full path to the spell file
>    - The signature string from its contents
> 2. Commit and push to your fork:
>
> ```bash
> git add signature_spell.txt
> git commit -m "Boss Gate 1: Archmage signature found"
> git push
> ```
>
> That commit is your key. No push, no exit.

{: .tip }
> 💡 **Hint:** You have `find`, `grep`, and pipes. You do not need Python. Think about what makes this file different from the other 300.

---

<label class="quest-check"><input type="checkbox" data-room="d1-boss-gate" data-key="commit"> Committed and pushed `signature_spell.txt`</label>

---

## 🧠 Skills This Gate Tests

- You can `ssh` into the Yens cluster and operate as a remote explorer
- You can wield `find` and `grep` to hunt through a forest of directories for one specific target
- You can crack open files from the command line and read what's inside
- You own the complete git spellchain: add → commit → push to your fork
