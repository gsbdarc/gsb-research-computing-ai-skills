---
layout: default
title: "Boss Gate 1"
parent: "Day 1 — The Gatehouse"
nav_order: 10
permalink: /day1/boss-gate-1/
---

# Boss Gate 1

*The Archmage's crest seals the passage to Floor 2. The seal reads: "Prove you can find what is hidden, and leave a record of your discovery." The vault is somewhere in `/scratch`. The signature spell is in there. Find it.*

---

{: .boss }
> **Boss Battle — The Archmage's Signature**
>
> A single spell file bearing the Archmage's signature is hidden somewhere in the vault:
>
> ```
> /scratch/rf_bootcamp_2026/vault/
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
> **Hint:** You have `find`, `grep`, and pipes. You do not need Python. Think about what makes this file different from the other 300.

---

<label class="quest-check"><input type="checkbox" data-room="d1-boss-gate" data-key="commit"> Committed and pushed `signature_spell.txt`</label>

---

## Skills This Gate Tests

- `ssh` to reach the Yens
- `find` and `grep` to search across a directory tree
- Reading file contents from the command line
- The complete git workflow: add → commit → push to your fork
