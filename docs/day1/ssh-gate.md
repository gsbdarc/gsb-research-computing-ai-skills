---
layout: default
title: "The SSH Gate"
parent: "Day 1 — The Gatehouse"
nav_order: 4
permalink: /day1/ssh-gate/
---

# The SSH Gate

<div data-room-id="d1-ssh-gate"></div>

*A crackling arc of electricity splits the gatehouse air, smelling of ozone and possibility. The rune carved above it reads: `ssh`. Touch the wrong stone and nothing stirs — touch the right one and a door tears open three thousand miles away, inside a machine humming in a Stanford data center. One command. A cryptographic handshake older than your laptop. And suddenly, you are there.*

---

## 🖊️ What Is a Remote Server?

Your laptop is powerful but limited: one machine, one location, and it has to be open and plugged in for work to run. A **remote server** is a computer you connect to over the network — it's always on, more powerful than your laptop, and your work keeps running after you close the lid.

Think of it this way:

```
  Your laptop          The Yens (today)         Cloud — AWS/GCP
  ─────────────        ──────────────────────   ────────────────
  Your kitchen         Shared restaurant         Rented kitchen
  ○ ○ ○ burners        ○○○○○○ ○○○○○○ burners    ○○○○○○ burners
  small fridge         walk-in fridges           rented fridge
  small store          warehouse (/scratch)      rented storage
  free, all yours      free, shared              unlimited, costs $$
```

**What are the Yens?**

The Yens are five shared **interactive compute servers** — not just gateways. Each one is genuinely powerful research hardware: when you SSH in, you land directly on a machine built for real work.

```
Your laptop
     │
     │  ssh SUNetID@yen.stanford.edu
     ▼
┌─────────────────────────────────────────────────────────────┐
│                   Stanford Yens Cluster                     │
│                                                             │
│  Interactive Yens  (where you land — shared compute)        │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐         │
│  │ yen1  │ │ yen2  │ │ yen3  │ │ yen4  │ │ yen5  │         │
│  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘         │
│  256 cores · ~1 TB RAM each · shared with all researchers   │
│                                                             │
│  GPU nodes  (Day 4)                                         │
│  ┌───────────────────────────────────────────────────┐      │
│  │  yen-gpu1: 4× A30 (24 GB)                         │      │
│  │  yen-gpu2/3: 4× A40 (48 GB) each                  │      │
│  │  yen-gpu4: 2× H200 (141 GB)                       │      │
│  └───────────────────────────────────────────────────┘      │
│                                                             │
│  Shared storage — all nodes see the same files:             │
│  /home/users/SUNetID/   ← backed up, limited quota         │
│  /scratch/SUNetID/      ← large, fast, not backed up       │
└─────────────────────────────────────────────────────────────┘
```

`ssh` opens an encrypted tunnel: you type locally, commands execute remotely, output streams back to your screen. The Yens are shared — you and every other researcher are on the same machines — so be a considerate neighbor: don't run jobs that peg all 256 cores for hours on end.

**What's inside a Yen server:**

![Server hardware diagram showing CPU, cores, and RAM — Yen1 has 256 cores]({{ "/assets/images/server-hardware-cpu-ram.png" | relative_url }})

The **CPU** is the processor chip. **Cores** are the individual workers inside it — each core runs instructions independently, which is what makes parallel work possible. **RAM** holds the data the CPU is actively using. Each Yen has 256 of those cores and around 1 TB of RAM.

---

## 🗡️ Main Quest

You are about to set foot on the Yens for the first time. Type carefully, breathe normally — the cluster is waiting for you.

{: .important }
> **Quest:** Connect to the Yens cluster over SSH, identify which interactive Yen you landed on, and read the login banner.

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
> The Yens (yen1–yen5) are shared interactive compute servers. You land on whichever one the load balancer picks. They're powerful, but shared — read the login banner when you connect, it describes current usage policies.

**Read the banner, then look around:**
```bash
ls ~          # your home directory on the Yens
pwd           # /home/users/SUNetID (or similar)
```

<label class="quest-check"><input type="checkbox" data-room="d1-ssh-gate" data-key="main"> Main Quest complete</label>

---

## 📦 Side Quests

Hidden inside this room is a shortcut that will save you a dozen keystrokes every single day — a carved sigil that shrinks a mouthful of a command down to two words.

{: .chest }
> **Side Quest 1 — SSH Sigil:** Set up `~/.ssh/config` on your laptop so that `ssh yen` connects you to `yen.stanford.edu` without typing your full username. You should be able to type nothing except `ssh yen` and be prompted for your password.

<label class="quest-check"><input type="checkbox" data-room="d1-ssh-gate" data-key="side1"> SSH Sigil unlocked</label>

---

## ⚔️ Weapons Earned

{: .weapon }
> **SSH Sigil** — configure `~/.ssh/config` with named hosts and your username; reduce `ssh SUNetID@yen.stanford.edu` to `ssh yen` — permanently.

---

## 🧠 Skills Learned

- You can now open a secure shell into the Yens cluster from anywhere with a single command
- You know the Yens are shared interactive compute servers — powerful, but shared with every researcher on the cluster
- You can tell at a glance whether you are on your laptop or deep inside a shared remote cluster
- You can read the login banner to catch system notices, maintenance windows, and usage policies before they catch you
