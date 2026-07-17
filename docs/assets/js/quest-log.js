/* DARC Dungeon — Quest Log
 * Persists checkbox state across pages via localStorage.
 * Shows a floating widget with completion count.
 * No build step. No dependencies.
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'dungeon.v1.progress';

  // Total possible checkboxes across the entire dungeon (all 4 days)
  const TOTAL_CHECKS = 58;

  const LEVEL_TITLES = [
    'Initiate', 'Apprentice', 'Scholar', 'Journeyman', 'Adept',
    'Specialist', 'Expert', 'Veteran', 'Master', 'Archmage',
  ];

  // Full room structure — used to compute per-day totals in the quest log panel.
  // Keys match data-room attributes on checkboxes throughout the site.
  const DAYS = [
    {
      label: 'Day 1 — The Gatehouse',
      prefix: 'd1',
      rooms: [
        { id: 'd1-command-spire',       keys: ['main'] },
        { id: 'd1-grimoire-vault',       keys: ['main', 'side1'] },
        { id: 'd1-ssh-gate',             keys: ['main', 'side1'] },
        { id: 'd1-cartographers-room',   keys: ['main'] },
        { id: 'd1-scroll-transfer',      keys: ['main'] },
        { id: 'd1-repository',           keys: ['main'] },
        { id: 'd1-familiars-den',        keys: ['side1'] },
        { id: 'd1-boss-gate-1',           keys: ['main'] },
      ],
    },
    {
      label: 'Day 2 — The Alchemist\'s Lab',
      prefix: 'd2',
      rooms: [
        { id: 'd2-arcane-notebook',          keys: ['main'] },
        { id: 'd2-venv-forge',               keys: ['main'] },
        { id: 'd2-stanford-ai-playground',   keys: ['main'] },
        { id: 'd2-key-vault',                keys: ['main'] },
        { id: 'd2-oracles-chamber',          keys: ['main'] },
        { id: 'd2-human-vs-llm',             keys: ['main'] },
        { id: 'd2-boss-gate',                keys: ['commit'] },
      ],
    },
    {
      label: 'Day 3 — The Hearth',
      prefix: 'd3',
      rooms: [
        { id: 'd3-kitchen',         keys: ['main', 'side1', 'side2'] },
        { id: 'd3-head-chef',       keys: ['mystery', 'main', 'readme', 'side1', 'side2', 'side3', 'side4', 'side5', 'side6', 'side7'] },
        { id: 'd3-data-mine',       keys: ['main', 'side1', 'side2', 'side3', 'side4', 'side5'] },
        { id: 'd3-foremans-desk',   keys: ['main', 'submit', 'side1', 'side2', 'side3'] },
        { id: 'd3-watch-tower',     keys: ['main', 'side1', 'side2', 'side3', 'side4'] },
        { id: 'd3-chronicle',       keys: ['main', 'side1', 'side2'] },
        { id: 'd3-boss-gate',       keys: ['commit', 'side1'] },
      ],
    },
    {
      label: 'Day 4 — The GPU Fortress',
      prefix: 'd4',
      rooms: [
        { id: 'd4-array-cavern',         keys: ['main'] },
        { id: 'd4-armory',              keys: ['main'] },
        { id: 'd4-h200-chamber',        keys: ['main'] },
        { id: 'd4-summoning-circle',    keys: ['main'] },
        { id: 'd4-engine-room',         keys: ['main'] },
        { id: 'd4-trap-garden',         keys: ['main'] },
        { id: 'd4-boss-gate',           keys: ['commit'] },
      ],
    },
  ];

  // ── Storage ──────────────────────────────────────────────────────────────

  function loadProgress() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (_) {
      return {};
    }
  }

  function saveProgress(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (_) { /* quota full — fail silently */ }
  }

  function storageKey(room, key) {
    return room + '.' + key;
  }

  // ── Checkbox sync ─────────────────────────────────────────────────────────

  function initCheckboxes() {
    const progress = loadProgress();
    const checkboxes = document.querySelectorAll('[data-room][data-key]');

    checkboxes.forEach(function (cb) {
      const room = cb.getAttribute('data-room');
      const key  = cb.getAttribute('data-key');
      const sk   = storageKey(room, key);

      // Restore saved state
      if (progress[sk]) {
        cb.checked = true;
        var label = cb.closest('.quest-check');
        if (label) label.classList.add('done');
      }

      // Save on change
      cb.addEventListener('change', function () {
        const fresh = loadProgress();
        if (cb.checked) {
          fresh[sk] = true;
        } else {
          delete fresh[sk];
        }
        saveProgress(fresh);

        var label = cb.closest('.quest-check');
        if (label) label.classList.toggle('done', cb.checked);

        renderQuestLog();
      });
    });
  }

  // ── Quest Log widget ──────────────────────────────────────────────────────

  function countCompleted(progress) {
    var total = 0, done = 0;
    DAYS.forEach(function (day) {
      day.rooms.forEach(function (room) {
        room.keys.forEach(function (key) {
          total++;
          if (progress[storageKey(room.id, key)]) done++;
        });
      });
    });
    return { done: done, total: total };
  }

  function countDayCompleted(progress, day) {
    var done = 0, total = 0;
    day.rooms.forEach(function (room) {
      room.keys.forEach(function (key) {
        total++;
        if (progress[storageKey(room.id, key)]) done++;
      });
    });
    return { done: done, total: total };
  }

  function computeLevel(done) {
    return Math.min(10, Math.floor(done / TOTAL_CHECKS * 9) + 1);
  }

  function renderQuestLog() {
    var btn = document.getElementById('quest-log-btn');
    if (!btn) return;

    var progress = loadProgress();
    var counts = countCompleted(progress);
    var level = computeLevel(counts.done);
    var title = LEVEL_TITLES[level - 1];

    var toggle = document.getElementById('quest-log-toggle');
    if (toggle) {
      toggle.textContent = '⚔️ Lv.' + level + ' · ' + counts.done + '/' + TOTAL_CHECKS + ' Quest Log';
    }

    var levelEl = document.getElementById('quest-level-display');
    if (levelEl) {
      var pct = Math.round(counts.done / TOTAL_CHECKS * 100);
      levelEl.innerHTML = '<span class="level-title">Level ' + level + ' — ' + title + '</span>'
        + '<div class="level-bar"><div class="level-fill" style="width:' + pct + '%"></div></div>';
    }

    // Update the entrance page summary if present
    var summary = document.getElementById('quest-log-summary');
    if (summary) {
      summary.innerHTML = '<strong>Level ' + level + ' — ' + title + '</strong>'
        + ' &nbsp;·&nbsp; ' + counts.done + '/' + TOTAL_CHECKS + ' Quest Log';
    }

    // Update panel list items
    var list = document.getElementById('quest-log-list');
    if (!list) return;
    list.innerHTML = '';
    DAYS.forEach(function (day) {
      var dc = countDayCompleted(progress, day);
      var li = document.createElement('li');
      li.innerHTML = day.label.split(' — ')[0] + ': <span>' + dc.done + ' / ' + dc.total + '</span>';
      list.appendChild(li);
    });
  }

  function createWidget() {
    var sunetCss =
      '#quest-sunet{margin-top:.5rem;padding-top:.5rem;border-top:1px solid rgba(0,0,0,.12);font-size:.82rem;}' +
      '#quest-sunet label{display:block;font-size:.78rem;font-weight:700;margin-bottom:.2rem;}' +
      '#quest-sunet .quest-sunet-row{display:flex;gap:.3rem;}' +
      '#quest-sunet input{flex:1;min-width:0;font:inherit;padding:.15rem .4rem;border:1px solid #d9b477;border-radius:6px;}' +
      '#quest-sunet input:focus{outline:2px solid #e0a13a;outline-offset:1px;}' +
      '#quest-sunet button{font:inherit;cursor:pointer;border:1px solid #d9b477;background:#fff;border-radius:6px;padding:.15rem .55rem;}' +
      '#quest-sunet button:hover{background:#f3e6cf;}' +
      '#quest-sunet .quest-sunet-set{display:flex;align-items:center;gap:.35rem;color:#5b4a2f;}' +
      '#quest-sunet .quest-sunet-val{font-weight:700;}' +
      '#quest-sunet .quest-sunet-edit{border:none;background:none;padding:0;margin-left:auto;' +
        'color:#8a5a12;text-decoration:underline;font-size:.78rem;}' +
      '#quest-sunet .quest-sunet-edit:hover{background:none;color:#5b3a08;}';
    var sunetStyle = document.createElement('style');
    sunetStyle.textContent = sunetCss;
    document.head.appendChild(sunetStyle);

    var btn = document.createElement('div');
    btn.id = 'quest-log-btn';

    var toggle = document.createElement('button');
    toggle.id = 'quest-log-toggle';
    toggle.type = 'button';
    toggle.textContent = '⚔️ Lv.1 · 0/' + TOTAL_CHECKS + ' Quest Log';
    btn.appendChild(toggle);

    var panel = document.createElement('div');
    panel.id = 'quest-log-panel';

    var heading = document.createElement('h4');
    heading.textContent = 'Quest Progress';
    panel.appendChild(heading);

    var levelDisplay = document.createElement('div');
    levelDisplay.id = 'quest-level-display';
    panel.appendChild(levelDisplay);

    var list = document.createElement('ul');
    list.id = 'quest-log-list';
    panel.appendChild(list);

    // ── SUNet ID: fills the SUNetID placeholder in commands site-wide ────────
    var SUNET_KEY = 'bootcamp.sunetid';
    var sunet = document.createElement('div');
    sunet.id = 'quest-sunet';
    panel.appendChild(sunet);

    btn.appendChild(panel);
    document.body.appendChild(btn);

    toggle.addEventListener('click', function () {
      panel.classList.toggle('open');
    });

    document.addEventListener('click', function (e) {
      if (!btn.contains(e.target)) panel.classList.remove('open');
    });

    // SUNet field: compact once set (you rarely change it), expands to edit.
    function readSunet() {
      try { return (localStorage.getItem(SUNET_KEY) || '').trim(); } catch (_) { return ''; }
    }
    function writeSunet(v) {
      try {
        if (v) localStorage.setItem(SUNET_KEY, v);
        else localStorage.removeItem(SUNET_KEY);
      } catch (_) { /* storage blocked */ }
      document.dispatchEvent(new CustomEvent('sunet:changed', { detail: { id: v } }));
    }
    function renderSunet(editing) {
      var id = readSunet();
      if (id && !editing) {
        sunet.innerHTML = '<div class="quest-sunet-set">SUNet ID: ' +
          '<code class="quest-sunet-val"></code>' +
          '<button type="button" data-sunet-act="edit" class="quest-sunet-edit">change</button></div>';
        sunet.querySelector('.quest-sunet-val').textContent = id;
      } else {
        sunet.innerHTML =
          '<label for="quest-sunet-input">Your SUNet ID</label>' +
          '<div class="quest-sunet-row">' +
            '<input id="quest-sunet-input" type="text" placeholder="e.g. jdoe" autocomplete="off" spellcheck="false">' +
            '<button type="button" data-sunet-act="save">Set</button>' +
          '</div>';
        var inp = sunet.querySelector('#quest-sunet-input');
        inp.value = id;
        if (editing) { inp.focus(); inp.select(); }
      }
    }
    function commitSunet() {
      var inp = sunet.querySelector('#quest-sunet-input');
      if (!inp) return;
      writeSunet(inp.value.trim());
      renderSunet(false);
    }
    sunet.addEventListener('click', function (e) {
      var b = e.target.closest ? e.target.closest('[data-sunet-act]') : null;
      if (!b) return;
      // Re-rendering detaches this button mid-click; stop the event so the
      // panel's click-outside-to-close handler doesn't treat it as outside.
      e.stopPropagation();
      if (b.getAttribute('data-sunet-act') === 'save') commitSunet();
      else renderSunet(true);
    });
    sunet.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && e.target.id === 'quest-sunet-input') { e.preventDefault(); commitSunet(); }
    });
    renderSunet(false);

    // personalize.js asks us to open when an unset placeholder is clicked.
    document.addEventListener('sunet:open', function () {
      panel.classList.add('open');
      renderSunet(true);
      var inp = sunet.querySelector('#quest-sunet-input');
      if (inp) { inp.focus(); inp.select(); }
    });
  }

  // ── Entry point ───────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', function () {
    createWidget();
    initCheckboxes();
    renderQuestLog();
  });

})();
