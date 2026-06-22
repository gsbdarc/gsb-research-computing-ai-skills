---
layout: default
title: "The DARC Dungeon"
nav_order: 0
permalink: /
---

# The DARC Dungeon

*You stand at the entrance of an ancient tower. Four floors rise above you, each sealed with an Archmage's crest. Somewhere inside, the secrets of computational research await — CLI runes carved into stone walls, SLURM forges humming in the depths, GPU engines blazing on the highest floor.*

*You are a pre-doctoral researcher. You have four days.*

{: .important }
> **How the dungeon works**
>
> Each floor corresponds to one day of the bootcamp. Every floor has **rooms** — enter each room, complete the **Main Quest**, and move to the next.
>
> Finished early? Look for **Chests** — optional deeper challenges that unlock a named **Weapon** (a skill you carry for the rest of the course). Weapons compound: what you earn in Day 1 pays off in Day 3.
>
> Each floor ends with a **Boss Gate**: a capstone challenge you submit by committing your work to your fork on GitHub. Push your commit → the grader runs → the next floor unlocks on your personal site.
>
> Every completed quest and opened chest earns **XP**. XP accumulates into your **Level** (shown in the widget, bottom-left). All main quests → 34 XP → Level 4 Journeyman. Open every chest → 78 XP → Level 10 Archmage. The leaderboard ranks by level.

---

## The Four Floors

{% assign unlocked = site.data.progress.unlocked_floors %}

<div class="floor-grid">
  <div class="floor-card{% unless unlocked contains 1 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day1/' | relative_url }}">Floor 1 — The Gatehouse</a>{% unless unlocked contains 1 %} 🔒{% endunless %}</h3>
    <p>Levels 1–3 &nbsp;·&nbsp; 9 rooms + Boss Gate</p>
    <p>CLI &middot; SSH &middot; Yens file system &middot; JupyterHub &middot; Git &middot; AI primer</p>
  </div>
  <div class="floor-card{% unless unlocked contains 2 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day2/' | relative_url }}">Floor 2 — The Alchemist's Lab</a>{% unless unlocked contains 2 %} 🔒{% endunless %}</h3>
    <p>Levels 4–6 &nbsp;·&nbsp; 10 rooms + Boss Gate</p>
    <p>Virtual envs &middot; AI Playground &middot; Security &middot; Claude Code &middot; LLMs &middot; Screen</p>
  </div>
  <div class="floor-card{% unless unlocked contains 3 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day3/' | relative_url }}">Floor 3 — The SLURM Mines</a>{% unless unlocked contains 3 %} 🔒{% endunless %}</h3>
    <p>Levels 7–8 &nbsp;·&nbsp; 8 rooms + Boss Gate + Hall of Heroes</p>
    <p>SLURM &middot; Job arrays &middot; Scaling &middot; README</p>
  </div>
  <div class="floor-card{% unless unlocked contains 4 %} floor-card-locked{% endunless %}">
    <h3><a href="{{ '/day4/' | relative_url }}">Floor 4 — The GPU Fortress</a>{% unless unlocked contains 4 %} 🔒{% endunless %}</h3>
    <p>Levels 9–10 &nbsp;·&nbsp; 7 rooms + Boss Gate</p>
    <p>H200 GPU jobs &middot; Ollama &middot; vLLM &middot; Privacy &middot; Agent risks</p>
  </div>
</div>

---

## Your Quest Log

<div id="quest-log-summary">Loading quest log…</div>

---

## The Grimoire

The dungeon's first trial involves a vault of spell files — hundreds of them, scattered and unsorted. Your instructor will give you a download link before Day 1.

Save `grimoire.zip` to your laptop before class. You'll unzip and sort it on your laptop in [The Grimoire Vault]({{ '/day1/grimoire-vault/' | relative_url }}), then transfer your sorted copy to the Yens in [The Scroll Transfer]({{ '/day1/scroll-transfer/' | relative_url }}).

**Spell file format:** `fireball_fire_3_offensive_meteor.spell`
`name_element_tier_type_mastery`
Elements: `fire` · `ice` · `lightning` · `earth` · `wind`

---

## Weapons Rack

A fully-equipped researcher who opens every chest across all four floors earns:

| Domain | Weapons |
|---|---|
| **Shell** | Grep Blade · Wildcard Wand · Shell Rune · Rsync Rune · Arcane Blade |
| **Remote access** | SSH Sigil · Module Lens · Screen Scroll |
| **Version control** | History Lens · Stash Spell |
| **Python env** | Freeze Flask · Editable Elixir · Pyenv Potion · Profile Rune |
| **Security** | Shield of `.gitignore` · Keyring Knife |
| **AI Playground + APIs** | Model Mirror · Stream Stone · Async Arrow |
| **AI-assisted coding** | Prompt Blade · Context Tome |
| **Data extraction** | Nested Tome · Retry Rune · Schema Shield |
| **SLURM + scaling** | Sacct Scythe · Mail Medallion · Template Tome · Watch Wand · Dependency Dagger · Checkpoint Charm · Siege Scale |
| **Documentation** | Structure Sigil · Changelog Charm |
| **GPU + local LLMs** | Smi Sight · Benchmark Blade · Model Menagerie · Modelfile Magic |

All main quests → 34 XP → Level 4 Journeyman. Every chest opened → 78 XP → Level 10 Archmage — fully equipped researcher.
