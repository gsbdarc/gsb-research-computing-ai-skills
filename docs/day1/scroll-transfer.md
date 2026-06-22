---
layout: default
title: "The Scroll Transfer"
parent: "Day 1 — The Gatehouse"
nav_order: 6
permalink: /day1/scroll-transfer/
---

# The Scroll Transfer

<div data-room-id="d1-scroll-transfer"></div>

*Deep in the courier's chamber, a pneumatic tube pierces the dungeon wall — the only passage between your world and the cluster's vast vaults. Every scroll you send hurtles through an encrypted tunnel and lands exactly where you aim it. On the Yens, that tube has a name: `scp`, secure copy. It rides the same SSH connection you already wield, and it obeys a simple, ruthless law — one copy exists, wherever you choose to put it.*

---

## 🗡️ Main Quest

Your grimoire is sorted, your spells are ready — now send them into the cluster's depths where real compute awaits.

{: .important }
> **Quest:** Transfer your sorted grimoire directory from your laptop to your Yens scratch space using `scp`.

Run this from your **laptop** (not on the Yens — open a new local terminal tab):

```bash
scp -r ~/grimoire/ SUNetID@yen.stanford.edu:/scratch/SUNetID/grimoire/
```

- `-r` means recursive — copies the whole directory tree
- The destination path is `remote_host:remote_path`

**Verify the transfer on the Yens:**
```bash
# SSH back onto the Yens (or use the tab that's already open)
ls /scratch/SUNetID/grimoire/fire/    # should show your fire spells
```

{: .note }
> 💡 The Yens use a **shared file system** — every login node (yen1–yen5) sees the same `/home` and `/scratch`. You copy once and the file is everywhere on the cluster simultaneously. No need to copy again if you switch nodes.

<label class="quest-check"><input type="checkbox" data-room="d1-scroll-transfer" data-key="main"> Main Quest complete</label>

---

## 📦 Chests

A secret compartment behind the courier's desk — crack it open and you'll find a rune that makes `scp` look like a stone chisel.

{: .chest }
> **Chest 1 — Rsync Rune:** Transfer the grimoire again, but this time use `rsync -avz --progress` instead of `scp`. Then add a new spell file and run rsync a second time — notice that it only transfers the new file. Why is this useful for large datasets?

<label class="quest-check"><input type="checkbox" data-room="d1-scroll-transfer" data-key="chest1"> Rsync Rune unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **Rsync Rune** — use `rsync` for incremental transfers; sync only what changed, resume interrupted transfers, and preserve permissions — the right tool when `scp` would re-copy 50 GB every run.

---

## 🧠 Skills Learned

- You can now beam entire directory trees from your laptop into the cluster with a single `scp` command
- You know the Yens' shared file system means one copy lands everywhere — no node-by-node shuffling required
- You can tell the difference between `scp` (full copy, fast and simple) and `rsync` (incremental sync, built for serious data)
- You can choose the right transfer tool for the job — and never waste bandwidth re-sending 50 GB you already moved
