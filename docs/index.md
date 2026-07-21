---
layout: default
title: "The DARC Dungeon"
nav_order: 0
permalink: /
---

# The DARC Dungeon

## Prerequisites

You can read the site and track your Quest Log with nothing installed. To do the hands-on work, you'll need a few things set up — your instructor can help with any of these in class:

- **A Claude account.** Stanford provides Claude for Education, free for most people. Request access at [uit.stanford.edu/service/claude](https://uit.stanford.edu/service/claude).
- **Terminal access.** On **macOS**, use the built-in **Terminal** app. On **Windows**, install [Git Bash](https://git-scm.com/downloads) and open it from the Start menu.
- **A GitHub account.** Free — [sign up](https://github.com/signup) if you don't already have one.
- **Access to the Yen servers.** Stanford GSB's research cluster. Faculty, PhD students, post-docs, and research fellows have access by default; others need a SUNet ID and faculty sponsorship. See [Access the Yens](https://rcpedia.stanford.edu/_getting_started/how_access_yens/) on RCpedia.

---

{: .important }
> **New here? Start with Day 1 → The Gatehouse.**
>
> 1. **Fork this repo** — click **Fork** in the top-right corner of the [GitHub page](https://github.com/gsbdarc/gsb-research-computing-ai-skills) to create your own copy
> 2. **Enable Actions** on your fork — click the **Actions** tab → **"I understand my workflows, go ahead and enable them"**
> 3. **Enable GitHub Pages** on your fork: Settings → Pages → Build and deployment → Source → select **GitHub Actions** (saves automatically)
> 4. **Trigger the first build** — Actions → "Deploy Jekyll site to Pages" → Run workflow → Run workflow
> 5. **Open your personal dungeon site** (~2 min after step 4): `https://YOUR-USERNAME.github.io/gsb-research-computing-ai-skills/`
>
> Once your site is live, put a **🟢 green sticky** on your laptop lid. If you're stuck on any step, put a **🔴 red sticky** up so an instructor can come help.
>
> Partway through Day 1, in **The Repository** room, you'll learn git and build your *own* personal copy of this site — the one that carries your leaderboard rank and unlocks each floor as you clear its Boss Gate. Until then, work from right here.

**How the dungeon works**

Each floor corresponds to one day of the bootcamp. Every floor has **rooms** — enter each room, complete the **Main Quest**, and move to the next.

Finished early? Look for **Side Quests** — optional deeper challenges that unlock a named **Weapon** (a skill you carry for the rest of the course). Weapons compound: what you earn in Day 1 pays off in Day 3.

Each floor ends with a **Boss Gate**: an optional capstone challenge you submit by committing your work to your fork on GitHub. Every floor is open from the start — clear the Boss Gates for the satisfaction (and the leaderboard), not to unlock anything.

Every completed quest adds to your **Quest Log** (shown in the widget, bottom-left) and to your standing on the leaderboard. Side quests push your level higher — that is what separates the top of the leaderboard. The more side quests you finish, the higher your rank.

---

## The Four Floors

<div class="dungeon-layout">
  <div class="floor-card">
    <h3><a href="{{ '/day1/' | relative_url }}">Floor 1 — The Gatehouse</a></h3>
    <p>Levels 1–3 &nbsp;·&nbsp; 6 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">CLI &middot; SSH &middot; Yens file system &middot; Git</div>

  <div class="floor-card">
    <h3><a href="{{ '/day2/' | relative_url }}">Floor 2 — The Alchemist's Lab</a></h3>
    <p>Levels 4–6 &nbsp;·&nbsp; 8 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">JupyterHub &middot; Python envs &middot; AI Playground &middot; Secure key management &middot; Pydantic &middot; AI agents &amp; data privacy</div>

  <div class="floor-card">
    <h3><a href="{{ '/day3/' | relative_url }}">Floor 3 — The SLURM Mines</a></h3>
    <p>Levels 7–8 &nbsp;·&nbsp; 6 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">SLURM &middot; Resource estimation &middot; Job lifecycle &middot; Job monitoring</div>

  <div class="floor-card">
    <h3><a href="{{ '/day4/' | relative_url }}">Floor 4 — The GPU Fortress</a></h3>
    <p>Levels 9–10 &nbsp;·&nbsp; 7 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">Job arrays &middot; GPU tiers &middot; Local LLMs &middot; OpenAI-compatible API &middot; Human vs LLM</div>
</div>
