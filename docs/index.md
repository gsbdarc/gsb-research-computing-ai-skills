---
layout: default
title: "The DARC Dungeon"
nav_order: 0
permalink: /
---

# The DARC Dungeon

*You stand at the entrance of an ancient tower. Four floors rise above you, each sealed with an Archmage's crest. Somewhere inside, the secrets of computational research await — CLI runes carved into stone walls, SLURM forges humming in the depths, GPU engines blazing on the highest floor.*

*You are a pre-doctoral researcher. You have four days.*

{: .warning }
> **Day 1 — Do this first**
>
> 1. **Fork this repo** — click **Fork** in the top-right corner of the [GitHub page](https://github.com/gsbdarc/rf-bootcamp-2026) to create your own copy
> 2. **Enable GitHub Pages** on your fork: Settings → Pages → Source → **GitHub Actions** → Save
> 3. **Open your personal dungeon site:** `https://YOUR-USERNAME.github.io/rf-bootcamp-2026/`
>
> Your site is your quest log for the entire course. Keep it open — every room, exercise, and leaderboard submission happens here.

{: .important }
> **How the dungeon works**
>
> Each floor corresponds to one day of the bootcamp. Every floor has **rooms** — enter each room, complete the **Main Quest**, and move to the next.
>
> Finished early? Look for **Side Quests** — optional deeper challenges that unlock a named **Weapon** (a skill you carry for the rest of the course). Weapons compound: what you earn in Day 1 pays off in Day 3.
>
> Each floor ends with a **Boss Gate**: a capstone challenge you submit by committing your work to your fork on GitHub. Push your commit → the grader runs → the next floor unlocks on your personal site.
>
> Every completed main quest or side quest adds to your **Quest Log**. Your total drives your **Level** (shown in the widget, bottom-left). Complete every quest → 73/73 → Level 10 Archmage. The leaderboard ranks by level.

---

## The Four Floors

{% assign unlocked = site.data.progress.unlocked_floors %}

<div class="floor-grid">
  <div class="floor-card{% unless unlocked contains 1 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day1/' | relative_url }}">Floor 1 — The Gatehouse</a>{% unless unlocked contains 1 %} 🔒{% endunless %}</h3>
    <p>Levels 1–3 &nbsp;·&nbsp; 6 rooms + Boss Gate</p>
    <p>CLI &middot; SSH &middot; Yens file system &middot; Git</p>
  </div>
  <div class="floor-card{% unless unlocked contains 2 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day2/' | relative_url }}">Floor 2 — The Alchemist's Lab</a>{% unless unlocked contains 2 %} 🔒{% endunless %}</h3>
    <p>Levels 4–6 &nbsp;·&nbsp; 10 rooms + Boss Gate</p>
    <p>JupyterHub &middot; Virtual envs &middot; AI Playground &middot; Security &middot; Claude Code &middot; LLMs &middot; Screen</p>
  </div>
  <div class="floor-card{% unless unlocked contains 3 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day3/' | relative_url }}">Floor 3 — The SLURM Mines</a>{% unless unlocked contains 3 %} 🔒{% endunless %}</h3>
    <p>Levels 7–8 &nbsp;·&nbsp; 8 rooms + Boss Gate + Hall of Heroes</p>
    <p>SLURM &middot; Job arrays &middot; Scaling &middot; README</p>
  </div>
  <div class="floor-card{% unless unlocked contains 4 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day4/' | relative_url }}">Floor 4 — The GPU Fortress</a>{% unless unlocked contains 4 %} 🔒{% endunless %}</h3>
    <p>Levels 9–10 &nbsp;·&nbsp; 7 rooms + Boss Gate</p>
    <p>H200 GPU jobs &middot; Ollama &middot; Local vs cloud API &middot; Privacy &middot; Agent risks</p>
  </div>
</div>

---

*The gate is open. The torch is lit. Whatever waits inside — the shell that answers in milliseconds, the cluster that never sleeps, the model you'll summon from bare silicon — it is yours to claim.*

*Good luck, adventurer. The dungeon awaits.*
