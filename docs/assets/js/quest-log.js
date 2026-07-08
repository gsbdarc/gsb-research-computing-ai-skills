/* DARC Dungeon — Quest Log
 * Persists checkbox state across pages via localStorage.
 * Shows a floating widget with completion count.
 * No build step. No dependencies.
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'dungeon.v1.progress';

  // Total possible checkboxes across the entire dungeon (all 4 days)
  const TOTAL_CHECKS = 31;

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
        { id: 'd1-ssh-gate',             keys: ['main'] },
        { id: 'd1-cartographers-room',   keys: ['main'] },
        { id: 'd1-scroll-transfer',      keys: ['main'] },
        { id: 'd1-repository',           keys: ['main'] },
        { id: 'd1-claude-code',          keys: ['main'] },
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
      label: 'Day 3 — The SLURM Mines',
      prefix: 'd3',
      rooms: [
        { id: 'd3-kitchen',              keys: ['main'] },
        { id: 'd3-head-chef',            keys: ['main'] },
        { id: 'd3-data-mine',            keys: ['main'] },
        { id: 'd3-scales',               keys: ['main'] },
        { id: 'd3-foremans-desk',        keys: ['main'] },
        { id: 'd3-watch-tower',          keys: ['main'] },
        { id: 'd3-chronicle',            keys: ['main'] },
        { id: 'd3-boss-gate',            keys: ['commit'] },
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

  function exportQuestLog() {
    var data = loadProgress();
    var json = JSON.stringify(data, null, 2);
    var blob = new Blob([json], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'quest_log.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    var hint = document.getElementById('quest-sync-hint');
    if (hint) hint.style.display = 'block';
  }

  function createWidget() {
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

    var syncDiv = document.createElement('div');
    syncDiv.className = 'quest-sync';

    var syncBtn = document.createElement('button');
    syncBtn.type = 'button';
    syncBtn.id = 'quest-sync-btn';
    syncBtn.textContent = '📤 Sync to leaderboard';
    syncBtn.addEventListener('click', exportQuestLog);
    syncDiv.appendChild(syncBtn);

    var hint = document.createElement('p');
    hint.id = 'quest-sync-hint';
    hint.innerHTML = 'Save <code>quest_log.json</code> to your repo root, then:<br>'
      + '<code>git add quest_log.json && git commit -m "sync" && git push</code>';
    hint.style.display = 'none';
    syncDiv.appendChild(hint);

    panel.appendChild(syncDiv);
    btn.appendChild(panel);

    document.body.appendChild(btn);

    toggle.addEventListener('click', function () {
      panel.classList.toggle('open');
    });

    document.addEventListener('click', function (e) {
      if (!btn.contains(e.target)) panel.classList.remove('open');
    });
  }

  // ── Entry point ───────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', function () {
    createWidget();
    initCheckboxes();
    renderQuestLog();
  });

})();
