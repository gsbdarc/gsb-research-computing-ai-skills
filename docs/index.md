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
> Your **Quest Log** — the widget in the bottom-left corner — tracks your progress right here on this site. No setup, no account, nothing to install. Just open the first room and begin.
>
> Partway through Day 1, in **The Repository** room, you'll learn git and build your *own* personal copy of this site — the one that carries your leaderboard rank and unlocks each floor as you clear its Boss Gate. Until then, work from right here.

**How the dungeon works**

Each floor corresponds to one day of the bootcamp. Every floor has **rooms** — enter each room, complete the **Main Quest**, and move to the next.

Finished early? Look for **Side Quests** — optional deeper challenges that unlock a named **Weapon** (a skill you carry for the rest of the course). Weapons compound: what you earn in Day 1 pays off in Day 3.

Each floor ends with a **Boss Gate**: a capstone challenge you submit by committing your work to your fork on GitHub. Push your commit → the grader runs → the next floor unlocks on your personal site.

Every completed quest adds to your **Quest Log** (shown in the widget, bottom-left). Completing all main quests on each floor is enough to pass the Boss Gate and advance. Side quests push your level higher — that is what separates the top of the leaderboard. The more side quests you finish, the higher your rank.

---

## The Four Floors

{% assign unlocked = site.data.progress.unlocked_floors %}

<div class="dungeon-layout">
  <div class="floor-card{% unless unlocked contains 1 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day1/' | relative_url }}">Floor 1 — The Gatehouse</a>{% unless unlocked contains 1 %} 🔒{% endunless %}</h3>
    <p>Levels 1–3 &nbsp;·&nbsp; 6 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">CLI &middot; SSH &middot; Yens file system &middot; Git</div>

  <div class="floor-card{% unless unlocked contains 2 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day2/' | relative_url }}">Floor 2 — The Alchemist's Lab</a>{% unless unlocked contains 2 %} 🔒{% endunless %}</h3>
    <p>Levels 4–6 &nbsp;·&nbsp; 10 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">JupyterHub &middot; Virtual envs &middot; AI Playground &middot; Security &middot; Claude Code &middot; LLMs &middot; Screen</div>

  <div class="floor-card{% unless unlocked contains 3 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day3/' | relative_url }}">Floor 3 — The SLURM Mines</a>{% unless unlocked contains 3 %} 🔒{% endunless %}</h3>
    <p>Levels 7–8 &nbsp;·&nbsp; 8 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">SLURM &middot; Job arrays &middot; Scaling &middot; README</div>

  <div class="floor-card{% unless unlocked contains 4 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day4/' | relative_url }}">Floor 4 — The GPU Fortress</a>{% unless unlocked contains 4 %} 🔒{% endunless %}</h3>
    <p>Levels 9–10 &nbsp;·&nbsp; 7 rooms + Boss Gate</p>
  </div>
  <div class="floor-skills">H200 GPU jobs &middot; Ollama &middot; Local vs cloud API &middot; Privacy &middot; Agent risks</div>
</div>
