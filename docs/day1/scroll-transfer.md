---
layout: default
title: "The Scroll Transfer"
parent: "Day 1 — The Gatehouse"
nav_order: 6
permalink: /day1/scroll-transfer/
---

# The Scroll Transfer

<div data-room-id="d1-scroll-transfer"></div>

*The courier's chamber. Scrolls move between the dungeon and the outside world through a narrow pneumatic tube. On the Yens, that tube is called `scp` — secure copy — and it moves files between your laptop and the cluster using the same SSH connection you already know. One copy exists, wherever you put it.*

---

## Main Quest

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
> The Yens use a **shared file system** — every login node (yen1–yen5) sees the same `/home` and `/scratch`. You copy once and the file is everywhere on the cluster simultaneously. No need to copy again if you switch nodes.

<label class="quest-check"><input type="checkbox" data-room="d1-scroll-transfer" data-key="main"> Main Quest complete</label>

---

## Chest

{: .chest }
> **Chest 1 — Rsync Rune:** Transfer the grimoire again, but this time use `rsync -avz --progress` instead of `scp`. Then add a new spell file and run rsync a second time — notice that it only transfers the new file. Why is this useful for large datasets?

<label class="quest-check"><input type="checkbox" data-room="d1-scroll-transfer" data-key="chest1"> Rsync Rune unlocked</label>

---

## Weapon Earned

{: .weapon }
> **Rsync Rune** — use `rsync` for incremental transfers; sync only what changed, resume interrupted transfers, and preserve permissions — the right tool when `scp` would re-copy 50 GB every run.

---

## Skills Learned

- Transfer files between your laptop and a remote server using `scp`
- Understand that the Yens shared file system means one copy is visible on all nodes
- Know the difference between `scp` (full copy) and `rsync` (incremental sync)
- Recognize when each tool is the right choice for a research workflow
