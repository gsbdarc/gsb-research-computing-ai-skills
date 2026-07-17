---
layout: default
title: "The Cluster File System"
parent: "Day 1 — Foundations"
nav_order: 5
permalink: /day1/cartographers-room/
---

# The Cluster File System

<div data-room-id="d1-cartographers-room"></div>

This room covers how storage is organized on the Yens: where your files live, how much space you have, and what software is available. Knowing this early helps you avoid running out of quota mid-job or being unable to find the software you need.

---

## Exercise

Before you work with data files, learn the layout: what storage is yours, how much space you have, and what software the cluster already provides.

{: .important }
> **Task:** Explore the Yens file system — find out where your data lives, how much space you have, and what software is available.

**The file system layout:**

<svg viewBox="0 0 660 200" role="img" aria-labelledby="fs-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:660px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="fs-title">The Yens have three main places to keep files. Your home directory is small and backed up. Project storage is shared with your team and backed up. Scratch is huge and fast but NOT backed up, so files there can be deleted — copy out anything you want to keep.</title>
  <text x="14" y="26" font-size="12.5" font-weight="700" letter-spacing="0.4" fill="#8a94a6">📁  WHERE YOUR FILES LIVE ON THE YENS</text>

  <!-- Home: backed up -->
  <rect x="14" y="40" width="200" height="150" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="30" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">🏠  Your home</text>
  <text x="30" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/home/users/SUNetID/</text>
  <rect x="28" y="112" width="172" height="28" rx="8" fill="#e3f2e6" stroke="#b7ddba" stroke-width="1.5"/>
  <text x="114" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#2e7d46">✓  backed up</text>
  <text x="30" y="162" font-size="11" fill="#6a7280">personal workspace</text>
  <text x="30" y="180" font-size="11" fill="#6a7280">small quota</text>

  <!-- Projects: backed up -->
  <rect x="230" y="40" width="200" height="150" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="246" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">👥  Project storage</text>
  <text x="246" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/yen/projects/</text>
  <rect x="244" y="112" width="172" height="28" rx="8" fill="#e3f2e6" stroke="#b7ddba" stroke-width="1.5"/>
  <text x="330" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#2e7d46">✓  backed up</text>
  <text x="246" y="162" font-size="11" fill="#6a7280">shared with your team</text>
  <text x="246" y="180" font-size="11" fill="#6a7280">space is limited</text>

  <!-- Scratch: NOT backed up -->
  <rect x="446" y="40" width="200" height="150" rx="14" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="462" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">⚡  Scratch space</text>
  <text x="462" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/scratch/shared/SUNetID/</text>
  <rect x="460" y="112" width="172" height="28" rx="8" fill="#fdeceb" stroke="#f0c3bd" stroke-width="1.5"/>
  <text x="546" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#c0392b">✕  NOT backed up</text>
  <text x="462" y="162" font-size="11" fill="#6a7280">huge &amp; fast</text>
  <text x="462" y="180" font-size="11" fill="#6a7280">copy out what you keep</text>
</svg>

Rule of thumb: the project itself — scripts, data, and outputs — lives in **projects**; your personal files live in **home** (both are backed up); **scratch** is for big temporary files you don't need to keep.

{: .note }
> **How to organize your work on the Yens:**
> - **A project — its scripts, data, and outputs → `/yen/projects/your_project/`.** This is the shared, backed-up home for the project itself; keep raw data and outputs in **separate subfolders** (e.g. `data/` and `output/`) so they never get mixed up. Access is controlled by the project's **workgroup**: everyone in it can read and write, which is how you, your PI, and collaborators share the same files. You may belong to **several** project workgroups at once, each with its own folder under `/yen/projects/`. See [Workgroups](https://rcpedia.stanford.edu/_policies/workgroups/) on RCpedia for who gets access and how it's managed.
> - **Personal files → your home, `/home/users/SUNetID/`.** Things that are yours, not any one project's: authentication tokens, R or shell preferences, quick one-off experiments. Backed up, and only you can see it.
> - **Large, temporary things → `/scratch/shared/SUNetID/`.** Fast and roomy, but **not backed up** and periodically cleared. Use it for things you don't need to keep or that won't fit in your quota — a big public dataset you're exploring, or an LLM you're testing out. Copy anything worth keeping back to `/yen/projects/`.

**Local disk: `/tmp`**

Those three locations — home, projects, and scratch — are all on the **shared file system**: every node sees the same files. Each node *also* has its own **local disk** that is **not** shared with other nodes, and `/tmp` lives there — it's where programs often write temporary files while they run.

Two things to know about `/tmp`: it's **private to that node** (a file at `/tmp` on `yen1` isn't visible on `yen2`), and it's **temporary and not backed up** (cleared automatically). Keep anything you care about — data, results — on the shared file system.

**Check your quota:**
```bash
gsbquota                             # shows home and scratch usage for your account
gsbquota /yen/projects/your_project  # append a path to check a project folder's usage
```

**Browse storage in a visual file manager:**
```bash
gsbbrowser                # opens an interactive file size browser in the terminal
# navigate with arrow keys, q to quit
```

**See what software modules are available:**
```bash
module avail              # lists all available software modules
module avail python       # filter by name
module load python/3.11   # load a specific version (adjust to what's available)
python --version          # confirm it loaded
module list               # see what's currently loaded
module unload python/3.11 # unload it
```

<label class="quest-check"><input type="checkbox" data-room="d1-cartographers-room" data-key="main"> Exercise complete</label>
