---
layout: floor
title: "Day 1 — Foundations"
nav_order: 1
has_children: true
permalink: /day1/
floor: 1
---

# Day 1 — Foundations

Day 1 covers the essentials: moving around a Unix system from the command line, connecting to the Yens research cluster over SSH, transferring and organizing files, and version-controlling your work with Git. By the end you'll be able to log in to a remote cluster, navigate its file system, move data around, and track your work the way researchers do everywhere.

**Duration:** ~3 hours

---

We are the **DARC team** at Stanford GSB — we run the Yens research cluster and support pre-docs like you with the computational side of your work. Joining us today is **Ben**, a PhD student here at GSB who uses these same tools daily for his own research — he knows exactly what it's like to be where you are now.

By the end of today you will navigate a remote research server the same way researchers at every university in the world do. Everything you learn here travels with you — to your next job, to a PhD program, and beyond.

---

## Meet Your Party

<div data-room-id="d1-intro"></div>

Four of us are travelling with you this week. Turn over each card to see who they are.

<div class="party-reveal" data-quest-room="d1-intro" data-quest-key="party" markdown="0">
  <div class="party-grid">

    <div class="party-card">
      <button type="button" class="party-flip" aria-pressed="false" aria-label="Turn over the first card">
        <span class="party-inner">
          <span class="party-face party-face-down"><span class="party-sigil" aria-hidden="true">✦</span><span class="party-tap">Click to reveal</span></span>
          <span class="party-face party-face-up"></span>
        </span>
      </button>
      <p class="party-caption">
        <span class="party-unknown">? ? ?</span>
        <span class="party-known">
          <span class="party-name">Alex Storer</span>
          <span class="party-class">Wizard</span>
          <span class="party-item">Staff of Arcane Insight</span>
          <span class="party-role">DARC team</span>
        </span>
      </p>
    </div>

    <div class="party-card">
      <button type="button" class="party-flip" aria-pressed="false" aria-label="Turn over the second card">
        <span class="party-inner">
          <span class="party-face party-face-down"><span class="party-sigil" aria-hidden="true">✦</span><span class="party-tap">Click to reveal</span></span>
          <span class="party-face party-face-up"></span>
        </span>
      </button>
      <p class="party-caption">
        <span class="party-unknown">? ? ?</span>
        <span class="party-known">
          <span class="party-name">Jeff Ott</span>
          <span class="party-class">Cleric</span>
          <span class="party-item">Mace of Radiance · Shield of Resolve</span>
          <span class="party-role">DARC team</span>
        </span>
      </p>
    </div>

    <div class="party-card">
      <button type="button" class="party-flip" aria-pressed="false" aria-label="Turn over the third card">
        <span class="party-inner">
          <span class="party-face party-face-down"><span class="party-sigil" aria-hidden="true">✦</span><span class="party-tap">Click to reveal</span></span>
          <span class="party-face party-face-up"></span>
        </span>
      </button>
      <p class="party-caption">
        <span class="party-unknown">? ? ?</span>
        <span class="party-known">
          <span class="party-name">Natalya Rapstine</span>
          <span class="party-class">Ranger</span>
          <span class="party-item">Bow of the Wilds</span>
          <span class="party-role">DARC team</span>
        </span>
      </p>
    </div>

    <div class="party-card">
      <button type="button" class="party-flip" aria-pressed="false" aria-label="Turn over the fourth card">
        <span class="party-inner">
          <span class="party-face party-face-down"><span class="party-sigil" aria-hidden="true">✦</span><span class="party-tap">Click to reveal</span></span>
          <span class="party-face party-face-up"></span>
        </span>
      </button>
      <p class="party-caption">
        <span class="party-unknown">? ? ?</span>
        <span class="party-known">
          <span class="party-name">Ben Barrett</span>
          <span class="party-class">Rogue</span>
          <span class="party-item">Twin Daggers</span>
          <span class="party-role">GSB PhD student</span>
        </span>
      </p>
    </div>

  </div>

  <p class="party-done" hidden>
    <span class="party-nudge">✨ <strong>Your party is assembled.</strong> Now tick <em>Met the party</em> below. That is a quest — every one you tick is counted in the Quest Log, the ⚔️ button at the bottom-left of every page.</span>
    <span class="party-logged">✅ <strong>First quest logged.</strong> Open the ⚔️ Quest Log at the bottom-left any time to see how far you have come.</span>
  </p>
</div>

<label class="quest-check"><input type="checkbox" data-room="d1-intro" data-key="party"> Met the party</label>

---

## Sections

Work through the sections in order — later ones build on earlier ones, and the Day 1 Challenge draws on everything you've learned.

| Section | Format | What you'll learn |
|------|--------|-----------------|
| [Command Line Basics](command-spire/) | 💻 Hands-on | Navigate a Unix file system with core commands: `pwd`, `ls`, `cd`, `mkdir`, `cp`, `rm` |
| [Bulk File Operations](grimoire-vault/) | 💻 Hands-on | Use wildcards, pipes, `grep`, and `sort` to work on many files at once |
| [Connecting to a Cluster](ssh-gate/) | 💻 Hands-on | Connect to a remote server and tell interactive nodes from compute nodes |
| [The Cluster File System](cartographers-room/) | 💻 Hands-on | Find your way around cluster storage, check your quota, and load software modules |
| [Transferring Files (scp)](scroll-transfer/) | 💻 Hands-on | Copy files between your machine and the cluster over the shared file system |
| [Version Control with Git](repository/) | 💻 Hands-on | Track your work in Git: fork → branch → commit → push |
| [Working with Claude Code](familiars-den/) | 💻 Hands-on | Set up Claude Code and understand what data it can and can't be given |
| [Day 1 Challenge](boss-gate-1/) | 🔑 Capstone | Put everything from today together in an open-ended challenge |
