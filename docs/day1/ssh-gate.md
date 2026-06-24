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

## 🖊️ Why Use a Server at All?

Your laptop is fine for writing code and running small tests. But research computing regularly runs into walls that a laptop cannot break through:

| Situation | What happens on a laptop | What happens on the Yens |
|-----------|--------------------------|--------------------------|
| Dataset is 80 GB | Out of memory, script crashes | Loads fine — 250 GB–3 TB RAM per node |
| Analysis takes 12 hours | Laptop sleeps, WiFi drops, run dies | Job keeps running — always on, always connected |
| Need to run 100 jobs in parallel | One at a time, ties up your machine | Submit all 100 at once via the scheduler |
| Data is restricted (IRB, NDA) | Must stay on Stanford systems | Yens are Stanford-managed infrastructure |
| Collaborating with your PI | "Can you send me the data?" | PI already has access to `/yen/projects/` |

The Yens are available to all researchers at GSB — faculty, PhD students, and pre-docs alike. Today we learn how to use them effectively.

{: .note }
> *"My regression on the full sample took 14 hours. My laptop died at hour 6. I lost everything. Two days later I reran it on the Yens and went to sleep. It finished while I was gone."* — Ben

---

## 🖊️ What Is a Remote Server?

Your laptop is powerful but limited: one machine, one location, and it has to be open and plugged in for work to run. A **remote server** is a computer you connect to over the network — it's always on, more powerful than your laptop, and your work keeps running after you close the lid.

**What are the Yens?**

The Yens are a 17-node shared research computing cluster: 5 interactive nodes you SSH into directly, and 12 nodes accessible only through the SLURM scheduler (Day 3). All 17 nodes share the same file system — a file you write on yen1 is instantly visible on every other node.

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
│  many cores · hundreds of GB RAM · per-user limits enforced │
│                         │                                   │
│                    scheduler (Day 3)                        │
│                         │                                   │
│  SLURM compute nodes  (scheduler-only, dedicated)           │
│  ┌─────────────────────────────────────────────────┐        │
│  │  8 CPU nodes + 4 GPU nodes  (12 total)          │        │
│  │  only accessible via sbatch / srun              │        │
│  └─────────────────────────────────────────────────┘        │
│                                                             │
│  Shared storage — all nodes see the same files:             │
│  /home/users/SUNetID/   ← backed up, limited, personal     │
│  /yen/projects/         ← backed up, large, for project    │
│                            files, scripts, and results      │
│  /scratch/shared/SUNetID/ ← large, fast, NOT backed up     │
└─────────────────────────────────────────────────────────────┘
```

`ssh` opens an encrypted tunnel: you type locally, commands execute remotely, output streams back to your screen. The interactive Yens are shared — per-user CPU and RAM limits are enforced automatically. See the [current limits](https://rcpedia.stanford.edu/_policies/user_limits/) for details. For heavier jobs, the SLURM scheduler (Day 3) gives you dedicated compute nodes.

**What's inside a Yen server:**

![Server hardware diagram showing CPU, cores, and RAM — Yen1 has 256 cores]({{ "/assets/images/server-hardware-cpu-ram.png" | relative_url }})

The **CPU** is the processor chip. **Cores** are the individual workers inside it — each core runs instructions independently, which is what makes parallel work possible. **RAM** holds the data the CPU is actively using. The Yen servers vary in size — see the [current specs on RCPedia](https://rcpedia.stanford.edu/_getting_started/yen-servers/#overview-of-the-yen-computing-infrastructure) for details.

---

## 🗡️ Main Quest

You are about to set foot on the Yens for the first time. Type carefully, breathe normally — the cluster is waiting for you.

{: .important }
> **Quest:** Connect to the Yens cluster over SSH, identify which interactive Yen you landed on, and read the login banner.

**Connect:**
```bash
ssh SUNetID@yen.stanford.edu
```

Replace `SUNetID` with your Stanford username. When prompted for your password, type your Stanford password (nothing will appear — that's normal). You will be prompted for Duo two-factor authentication.

**Identify your node:**
```bash
hostname      # e.g. yen1, yen2, yen3, yen4, or yen5
whoami        # confirm you're logged in as yourself
```

{: .note }
> The Yens (yen1–yen5) are shared interactive compute servers. You land on whichever one the load balancer picks. They're powerful, but shared — read the login banner when you connect, it describes current usage policies.

**Read the banner, then look around:**
```bash
ls ~                              # your home directory on the Yens
pwd                               # /home/users/SUNetID
ls /scratch/shared/$USER          # your scratch space
ls /yen/projects/                 # shared project storage
```

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

<label class="quest-check"><input type="checkbox" data-room="d1-ssh-gate" data-key="main"> Main Quest complete</label>
