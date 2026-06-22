---
layout: default
title: "The SSH Gate"
parent: "Day 1 — The Gatehouse"
nav_order: 4
permalink: /day1/ssh-gate/
---

# The SSH Gate

<div data-room-id="d1-ssh-gate"></div>

*A crackling arc of electricity spans the gatehouse entrance. The rune above it reads: `ssh`. Touch the wrong stone and nothing happens — touch the right one and a door appears three thousand miles away. This is how researchers reach the Yens: a single command, a handshake of cryptographic keys, and you are in.*

---

## Main Quest

{: .important }
> **Quest:** Connect to the Yens cluster over SSH, identify which login node you landed on, and read the login banner.

**Connect:**
```bash
ssh SUNetID@yen.stanford.edu
```

Replace `SUNetID` with your Stanford username. When prompted for your password, type your Stanford password (nothing will appear — that's normal). You may be prompted for Duo two-factor authentication.

**Identify your node:**
```bash
hostname      # e.g. yen1, yen2, yen3, yen4, or yen5
whoami        # confirm you're logged in as yourself
```

{: .note }
> The Yens have **login nodes** (yen1–yen5) and **compute nodes**. You always land on a login node. Never run heavy computation on a login node — that's what SLURM is for (Day 3). The login banner you see when you connect describes this.

**Read the banner, then look around:**
```bash
ls ~          # your home directory on the Yens
pwd           # /home/users/SUNetID (or similar)
```

<label class="quest-check"><input type="checkbox" data-room="d1-ssh-gate" data-key="main"> Main Quest complete</label>

---

## Chest

{: .chest }
> **Chest 1 — SSH Sigil:** Set up `~/.ssh/config` on your laptop so that `ssh yen` connects you to `yen.stanford.edu` without typing your full username. You should be able to type nothing except `ssh yen` and be prompted for your password.

<label class="quest-check"><input type="checkbox" data-room="d1-ssh-gate" data-key="chest1"> SSH Sigil unlocked</label>

---

## Weapon Earned

{: .weapon }
> **SSH Sigil** — configure `~/.ssh/config` with named hosts and your username; reduce `ssh SUNetID@yen.stanford.edu` to `ssh yen` — permanently.

---

## Skills Learned

- Connect to a remote server over SSH from your laptop
- Understand what a login node is and why you don't run computation on it
- Recognize the difference between your local laptop and a shared remote cluster
- Read a login banner for system notices and usage policies
