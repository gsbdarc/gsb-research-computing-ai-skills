---
layout: default
title: "Transferring Files (scp)"
parent: "Day 1 — Foundations"
nav_order: 6
permalink: /day1/scroll-transfer/
---

# Transferring Files (scp)

<div data-room-id="d1-scroll-transfer"></div>

`scp` (secure copy) transfers files between your laptop and the cluster. It runs over the same SSH connection you already use, copying files to wherever you specify.

---

## Exercise

Transfer a directory from your laptop to your Yens scratch space using `scp`.

{: .important }
> **Task:** Copy your sorted directory from your laptop to your Yens scratch space using `scp`.

First, **on the Yens**, create your scratch directory:

```bash
mkdir /scratch/shared/$USER
```

Then, from your **laptop** (open a new local terminal tab):

```bash
scp -r ~/Desktop/grimoire/ SUNetID@yen.stanford.edu:/scratch/shared/SUNetID/grimoire/
```

- `-r` means recursive — copies the whole directory tree
- The destination path is `remote_host:remote_path`

**Verify the transfer on the Yens:**
```bash
# SSH back onto the Yens (or use the tab that's already open)
ls /scratch/shared/SUNetID/grimoire/fire/    # should show your files
```

{: .note }
> The Yens use a **shared file system** — every Yen server (yen1–yen5) sees the same `/home` and `/scratch`. You copy once and the file is available everywhere on the cluster. No need to copy again if you switch nodes.

<label class="quest-check"><input type="checkbox" data-room="d1-scroll-transfer" data-key="main"> Exercise complete</label>

---

## Optional practice

**Download: copy from the Yens back to your laptop**

`scp` always takes the form `scp SOURCE DESTINATION`. In the exercise the source was local and the destination was remote (an upload). Swap the order and you have a **download** — pull a file from the Yens back to your laptop.

Run this from your **laptop** (not the Yens):

```bash
scp -r SUNetID@yen.stanford.edu:/scratch/shared/SUNetID/grimoire/ ~/Desktop/grimoire_from_yens/
```

Now the remote path is the source and the local path is the destination. Same command, order reversed.

**Which machine you run it from matters**

You can run `scp` from any machine — your laptop *or* a server you're logged into. The rule is about reachability: every host you name with `host:path` has to be reachable *from wherever you run the command*. Reaching a machine over SSH means it has a public address and an SSH server listening.

The Yens have both (`yen.stanford.edu`). Your laptop has neither — it sits behind your home or campus network with no public hostname, so nothing on the internet can open a connection *to* it. Your laptop can reach out to the Yens, but the Yens cannot reach back.

That asymmetry is why, for a laptop ⇄ Yens transfer, you run `scp` **from your laptop** — it names the Yens (reachable) and refers to itself locally. The reverse doesn't work: logged into the Yens, `scp file my-laptop:...` fails because your laptop has no address to send to. When *both* endpoints are reachable servers, though, you can run `scp` from either one (next).

**Copy from one server to another**

Neither side of an `scp` command has to be your laptop — you can copy directly between two remote machines: `scp host1:path host2:path`. On the Yens the shared file system usually makes this unnecessary (a file in `/home` or `/scratch` is already on every node). The exception is **`/tmp`**, which is local to each node and *not* shared — so to get a file from `/tmp` on one node to `/tmp` on another, you do have to copy it.

The reason this works is that the Yen nodes can reach *each other* on the network, not just your laptop reaching them. You can see this directly: from your laptop, SSH into one node, then SSH again from that node to another.

```bash
ssh SUNetID@yen.stanford.edu    # from your laptop → land on a Yen (say yen1)
hostname                        # confirms which node, e.g. yen1
ssh yen2                        # hop from yen1 to yen2 — no full address needed on-cluster
hostname                        # now shows yen2
```

Each `ssh` opens a connection *to* a reachable machine — your laptop can reach the Yens, and any Yen can reach any other. That second hop (`yen1 → yen2`) is the same reachability that lets `scp` copy between the two nodes.

Because `/tmp` is shared by *everyone* logged into that node, don't drop files at the top level like `/tmp/note.txt` — your name could collide with someone else's. Tuck your file behind your username instead. The `$USER` variable holds your username, so a filename like `/tmp/note_$USER.txt` is unique to you.

One important detail: **run this transfer from a Yens node, not your laptop.** Both nodes are reachable servers, so either one can run the copy — and running it on the Yens means `$USER` expands to your SUNetID (on your laptop it would expand to your laptop username, giving the wrong path).

**SSH into one node** (say `yen1`), create a file, then copy it to a *different* node (`yen2`):

```bash
# on yen1
echo "hello from $(hostname)" > /tmp/note_$USER.txt   # $USER = your SUNetID here
scp /tmp/note_$USER.txt $USER@yen2.stanford.edu:/tmp/  # copy it straight to yen2
```

The file goes from yen1's local disk to yen2's local disk directly — it never touches your laptop. (Use `hostname` any time to check which node you're on.)

---

## What You Learned

- You can copy entire directory trees between your laptop and the cluster with a single `scp` command — reverse the source and destination to switch between upload and download
- You can run `scp` from any machine, as long as every host you name is reachable from there — and since your laptop isn't publicly reachable but the Yens are, laptop ⇄ Yens transfers must be run from your laptop
- `scp` can also copy directly between two servers — useful for node-local storage like `/tmp` that the shared file system doesn't cover
- You know the Yens' shared file system means one copy is available everywhere — no node-by-node copying required
