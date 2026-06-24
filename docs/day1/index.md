---
layout: floor
title: "Day 1 — The Gatehouse"
nav_order: 1
has_children: true
permalink: /day1/
floor: 1
---

# Day 1 — The Gatehouse

*The outer wall looms before you, its stones etched with runes that pulse with cold blue light. Torches snap in the wind. This is the Gatehouse — where every great adventurer begins. The puzzles here seem simple, but do not be deceived: every command you master, every path you memorize, every commit you push is a brick in the fortress you are building. By the time you force open the Boss Gate, you will move through a remote cluster like you own it — logging in, navigating directories, transferring data, and versioning your work.*

**Duration:** ~3 hours &nbsp;·&nbsp; **Levels:** 1–3

---

## Who We Are

We are the **DARC team** — Data, Analytics, and Research Computing — at Stanford GSB. We run the Yens cluster and support pre-doctoral researchers with the computational side of their work.

This bootcamp exists because the technical skills that make or break a pre-doc RA are rarely taught anywhere. You are about to spend two years at Stanford GSB running analyses, managing datasets, and collaborating with your PI. We want you to spend that time doing research — not fighting your tools.

---

## Key Concepts

**What is research computing?**
Research computing is using computers to collect, organize, analyze, and share data as part of a research project. For a pre-doc RA this means: running scripts on datasets too large for Excel, processing thousands of files automatically, and reproducing results months later when a reviewer asks.

**What is a server?**
A server is a powerful computer you access over the network rather than sitting in front of. Servers run continuously, have far more CPU and memory than a laptop, and multiple people can use the same one at the same time. The Yens cluster at Stanford GSB is a set of research servers your team uses to do compute-intensive work.

**What is a terminal?**
A terminal is a text-based interface to your computer. Instead of clicking icons, you type commands. The terminal is how you talk to servers — there is no GUI when you SSH into a cluster — and it is how you automate work that would take days to do by hand.

---

## Why This Matters for Your Research Job

As a pre-doc RA, you will regularly face situations like these:

**Data arrives as a dump.**
Your PI or a vendor sends a folder with thousands of files — inconsistently named, unsorted, with no explanation. Organizing it by clicking takes days. The terminal takes seconds. Before you run a single analysis, your first job is to understand and organize what you have.

**Your laptop is the wrong tool.**
When a script runs for 12 hours and your laptop goes to sleep at hour 3, you lose everything. When your dataset is 80 GB and you only have 16 GB of RAM, nothing runs. The Yens exist precisely for this.

**Organization is a research skill.**
Where do your scripts live? Where does raw data live? Where do outputs go? These are not trivial questions. A research project that mixes scripts, raw data, and results in one folder is a project that cannot be reproduced — by you, your PI, or anyone who inherits it.

**Documentation is a career skill.**
Future-you will not remember why you organized files the way you did six months ago. A one-paragraph README written today saves hours of confusion later — and makes your work credible to collaborators and reviewers.

---

## How to Be Effective: A Framework

Every time you encounter a new dataset or task, use this four-step pattern:

| Step | What you do | Why |
|------|-------------|-----|
| **1. Explore** | Look at what you have before touching anything | Understand the problem before solving it |
| **2. Plan** | Decide on a strategy | Rushing to execute without a plan creates more work |
| **3. Execute** | Run the commands | Now the terminal earns its keep |
| **4. Document** | Write down what you did and why | Your future self and collaborators will thank you |

You will practice this pattern for the first time in the Grimoire Vault today.

---

## 🗡️ Rooms

Six hands-on rooms and a Boss Gate await. Work through each room in order — later rooms build on earlier ones, and the Boss Gate will demand everything you have learned today.

| Room | Format | What you master |
|------|--------|-----------------|
| [The Command Spire](command-spire/) | 💻 Hands-on | Bend any Unix file system to your will with core navigation commands |
| [The Grimoire Vault](grimoire-vault/) | 💻 Hands-on | Wield wildcards and bulk operations to reshape hundreds of files at once |
| [The SSH Gate](ssh-gate/) | 💻 Hands-on | Breach the walls of a remote server and know login nodes from compute nodes |
| [The Cartographer's Room](cartographers-room/) | 💻 Hands-on | Map the cluster's file system, track your quota, and summon software modules |
| [The Scroll Transfer](scroll-transfer/) | 💻 Hands-on | Conjure data across machines and master the shared file system |
| [The Repository](repository/) | 💻 Hands-on | Lock your progress in Git: fork → branch → commit → push, unbreakable |
| [Boss Gate 1](boss-gate-1/) | 🔑 Capstone | Prove you command everything from today on an open-ended challenge |
