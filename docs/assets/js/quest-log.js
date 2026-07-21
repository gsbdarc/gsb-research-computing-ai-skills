/* DARC Dungeon — Quest Log
 * Persists checkbox state across pages via localStorage.
 * Shows a floating widget with completion count.
 * No build step. No dependencies.
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'dungeon.v1.progress';

  // Total possible checkboxes across the entire dungeon is computed from DAYS
  // (defined below) in TOTAL_CHECKS, so it can never drift out of sync with the
  // room structure when quests are added or removed.

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
        { id: 'd1-familiars-den',        keys: ['main', 'skill', 'side1'] },
        { id: 'd1-boss-gate-1',           keys: ['main'] },
      ],
    },
    {
      label: 'Day 2 — The Alchemist\'s Lab',
      prefix: 'd2',
      rooms: [
        { id: 'd2-arcane-notebook',          keys: ['main', 'side1', 'side2'] },
        { id: 'd2-venv-forge',               keys: ['main', 'side1', 'side2', 'side3'] },
        { id: 'd2-stanford-ai-playground',   keys: ['main', 'side1', 'side2', 'side3'] },
        { id: 'd2-key-vault',                keys: ['main', 'side1', 'side2'] },
        { id: 'd2-oracles-chamber',          keys: ['main', 'side1', 'side2', 'side3', 'side4'] },
        { id: 'd2-human-vs-llm',             keys: ['main'] },
        { id: 'd2-boss-gate',                keys: ['commit'] },
      ],
    },
    {
      label: 'Day 3 — Cluster Computing',
      prefix: 'd3',
      rooms: [
        { id: 'd3-kitchen',         keys: ['main', 'side1', 'side2'] },
        { id: 'd3-head-chef',       keys: ['mystery', 'main', 'readme', 'side2', 'side3', 'side4', 'side5', 'side6', 'side7'] },
        { id: 'd3-data-mine',       keys: ['main', 'side1', 'side3', 'side5'] },
        { id: 'd3-foremans-desk',   keys: ['main', 'submit', 'side1', 'side2', 'side3', 'side4'] },
        { id: 'd3-watch-tower',     keys: ['main', 'side1', 'side2', 'side3', 'side4', 'side5'] },
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

  // Single source of truth for the grand total: sum every room's keys across all
  // days. Add or remove a key above and this stays correct automatically.
  const TOTAL_CHECKS = DAYS.reduce(function (sum, day) {
    return sum + day.rooms.reduce(function (roomSum, room) {
      return roomSum + room.keys.length;
    }, 0);
  }, 0);

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

  // Canonical, ordered list of every quest key, derived from DAYS. MUST match
  // scripts/quest_keys.json (read by scripts/quest_sync.py); regenerate that
  // file with `node .instructor/gen_quest_keys.js` after changing DAYS.
  function orderedKeys() {
    var keys = [];
    DAYS.forEach(function (d) {
      d.rooms.forEach(function (r) {
        r.keys.forEach(function (k) { keys.push(r.id + '.' + k); });
      });
    });
    return keys;
  }

  // FNV-1a (32-bit) over the joined key list, as hex. Lets quest_sync.py detect
  // a token built from a different site version than the clone has.
  function keyListHash(keys) {
    var s = keys.join(',');
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) {
      h ^= s.charCodeAt(i);
      h = Math.imul(h, 0x01000193) >>> 0;
    }
    return h.toString(16);
  }

  // Encode completed quests as a compact, fixed-size, paste-safe token:
  // version "1", a hash of the key list, and a base64url bitfield (one bit per
  // canonical key). scripts/quest_sync.py decodes it on the Yens.
  function encodeProgress() {
    var progress = loadProgress();
    var keys = orderedKeys();
    var bytes = new Uint8Array(Math.ceil(keys.length / 8));
    var count = 0;
    for (var i = 0; i < keys.length; i++) {
      if (progress[keys[i]] === true) {
        bytes[i >> 3] |= (1 << (i & 7));
        count++;
      }
    }
    var bin = '';
    for (var j = 0; j < bytes.length; j++) bin += String.fromCharCode(bytes[j]);
    var b64 = btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    return { token: '1.' + keyListHash(keys) + '.' + b64, count: count };
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

    var toggle = document.getElementById('quest-log-toggle');
    if (toggle) {
      toggle.textContent = '⚔️ Lv.' + level + ' · ' + counts.done + '/' + TOTAL_CHECKS + ' Quest Log';
    }

    var levelEl = document.getElementById('quest-level-display');
    if (levelEl) {
      var pct = Math.round(counts.done / TOTAL_CHECKS * 100);
      levelEl.innerHTML = '<span class="level-title">Level ' + level + '</span>'
        + '<div class="level-bar"><div class="level-fill" style="width:' + pct + '%"></div></div>';
    }

    // Update the entrance page summary if present
    var summary = document.getElementById('quest-log-summary');
    if (summary) {
      summary.innerHTML = '<strong>Level ' + level + '</strong>'
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
      '#quest-sunet .quest-sunet-edit:hover{background:none;color:#5b3a08;}' +
      '#quest-sync{margin-top:.5rem;padding-top:.5rem;border-top:1px solid rgba(0,0,0,.12);font-size:.82rem;}' +
      '#quest-sync .quest-sync-go{font:inherit;cursor:pointer;border:1px solid #d9b477;background:#fff;border-radius:6px;padding:.25rem .6rem;font-weight:700;}' +
      '#quest-sync .quest-sync-go:hover{background:#f3e6cf;}' +
      '#quest-sync .quest-sync-hint{color:#6a7280;font-size:.72rem;display:block;margin:.3rem 0 .15rem;}' +
      '#quest-sync textarea{width:100%;box-sizing:border-box;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.7rem;border:1px solid #d9b477;border-radius:6px;padding:.3rem;resize:none;}' +
      '#quest-sync .quest-sync-row{display:flex;gap:.4rem;align-items:center;margin-top:.3rem;}' +
      '#quest-sync .quest-sync-copy{font:inherit;cursor:pointer;border:1px solid #d9b477;background:#fff;border-radius:6px;padding:.15rem .55rem;}' +
      '#quest-sync .quest-sync-copy:hover{background:#f3e6cf;}';
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

    // ── Sync: encode progress into a token to paste into scripts/quest_sync.py ─
    var sync = document.createElement('div');
    sync.id = 'quest-sync';
    sync.innerHTML = '<button type="button" class="quest-sync-go">🔄 Sync</button>';
    panel.appendChild(sync);

    function renderSync() {
      var enc = encodeProgress();
      var go = '<button type="button" class="quest-sync-go">🔄 Sync</button>';
      if (!enc.count) {
        sync.innerHTML = go + '<span class="quest-sync-hint">Complete a quest first, then sync.</span>';
        return;
      }
      sync.innerHTML = go
        + '<span class="quest-sync-hint">Copy your progress token, then paste it into the sync command shown on the page:</span>'
        + '<textarea readonly rows="2"></textarea>'
        + '<div class="quest-sync-row"><button type="button" class="quest-sync-copy">Copy token</button>'
        + '<span class="quest-sync-hint" style="margin:0">' + enc.count + ' quest' + (enc.count === 1 ? '' : 's') + '</span></div>';
      sync.querySelector('textarea').value = enc.token;
    }
    sync.addEventListener('click', function (e) {
      var goBtn = e.target.closest ? e.target.closest('.quest-sync-go') : null;
      var cpBtn = e.target.closest ? e.target.closest('.quest-sync-copy') : null;
      if (!goBtn && !cpBtn) return;
      e.stopPropagation();  // keep the panel's click-outside handler from closing us
      if (goBtn) { renderSync(); return; }
      var ta = sync.querySelector('textarea');
      if (ta) {
        ta.select();
        try { navigator.clipboard.writeText(ta.value); } catch (_) { try { document.execCommand('copy'); } catch (__) {} }
        cpBtn.textContent = 'Copied ✓';
        setTimeout(function () { cpBtn.textContent = 'Copy'; }, 1500);
      }
    });

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
