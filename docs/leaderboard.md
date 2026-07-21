---
layout: default
title: "Leaderboard"
nav_order: 5
permalink: /leaderboard/
---

# 🏆 Class Leaderboard

*Rankings update when students sync their progress. Each completed exercise adds to your total, which drives your **Level** (max Level 10). **Challenges** = optional day-end capstones completed (max 4).*

<div id="lb-controls">
  <button id="lb-refresh">↻ Refresh</button>
  <span id="lb-timestamp"></span>
</div>

<div id="lb-container"><p class="lb-loading">Loading…</p></div>

<style>
#lb-controls { margin: 1rem 0; display: flex; align-items: center; gap: 1rem; }
#lb-refresh {
  padding: 0.4rem 0.9rem; cursor: pointer; border-radius: 4px;
  border: 1px solid #ccc; background: #f0f0f0; font-size: 0.9em;
}
#lb-refresh:hover { background: #e0e0e0; }
#lb-timestamp { color: #999; font-size: 0.85em; }

.lb-table { width: 100%; border-collapse: collapse; font-size: 1em; margin-top: 0.5rem; }
.lb-table th {
  text-align: left; padding: 0.5rem 0.8rem;
  border-bottom: 2px solid #ddd; color: #666;
  font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.04em;
}
.lb-table td { padding: 0.65rem 0.8rem; border-bottom: 1px solid #eee; vertical-align: middle; }
.lb-table tr:last-child td { border-bottom: none; }

.lb-rank { width: 3rem; text-align: center; font-size: 1.3em; font-weight: 700; }
.lb-name { font-weight: 600; font-size: 1em; }
.lb-gates { font-size: 1.15em; letter-spacing: 0.1em; white-space: nowrap; }
.gate-cleared { color: #e67e22; }
.gate-locked  { color: #ddd; }
.gate-label { font-size: 0.78em; color: #999; margin-left: 0.4rem; font-family: sans-serif; letter-spacing: 0; }
.lb-level { white-space: nowrap; }
.lb-bar-wrap { min-width: 120px; }
.lb-bar { background: #eee; border-radius: 999px; height: 10px; }
.lb-fill { background: linear-gradient(90deg, #e67e22, #f1c40f); border-radius: 999px; height: 10px; transition: width 0.5s ease; }

tr.lb-all-clear td { background: #fffbf0; }
tr.lb-leader td { background: #f4f8ff; }
.lb-crown { margin-left: 0.25rem; }
.lb-loading { color: #aaa; }
</style>

<script>
(function () {
  var RAW    = 'https://raw.githubusercontent.com';
  var MAIN   = 'gsbdarc/gsb-research-computing-ai-skills';
  var REPO   = 'gsb-research-computing-ai-skills';
  var BRANCH = 'main';
  var TOTAL  = 73; // keep in sync with TOTAL_CHECKS in assets/js/quest-log.js

  // quest_log.json keys that mark each day's optional capstone as complete
  var BOSS_GATE_KEYS = [
    'd1-boss-gate-1.main',
    'd2-boss-gate.commit',
    'd3-boss-gate.commit',
    'd4-boss-gate.commit',
  ];

  function computeLevel(checks) {
    return Math.min(10, Math.floor(checks / TOTAL * 9) + 1);
  }

  function levelBadge(checks) {
    var lv = computeLevel(checks);
    return '<span class="lb-level-num">Lv.' + lv + '</span>';
  }

  function parseStudents(text) {
    var students = [];
    var re = /^- username:\s*(\S+)/gm, m, matches = [];
    while ((m = re.exec(text)) !== null) {
      matches.push({
        username: m[1].replace(/['"]/g, ''),
        contentStart: m.index + m[0].length,
        lineStart: m.index
      });
    }
    // Bound each entry by the next "- username:" so a missing repo:/name:
    // can't bleed into the following entry's value.
    for (var i = 0; i < matches.length; i++) {
      var end = (i + 1 < matches.length) ? matches[i + 1].lineStart : text.length;
      var block = text.slice(matches[i].contentStart, end);
      var repoM = block.match(/^\s*repo:\s*["']?(.+?)["']?\s*$/m);
      var nameM = block.match(/^\s*name:\s*["']?(.+?)["']?\s*$/m);
      students.push({
        username: matches[i].username,
        repo: repoM ? repoM[1].trim() : REPO,
        name: nameM ? nameM[1].trim() : matches[i].username
      });
    }
    return students;
  }

  function parseQuestLog(text) {
    var data;
    try { data = JSON.parse(text); } catch (e) { data = {}; }
    var completedChecks = 0;
    for (var k in data) { if (data[k] === true) completedChecks++; }
    var bossGates = 0;
    BOSS_GATE_KEYS.forEach(function (k) { if (data[k] === true) bossGates++; });
    return { completedChecks: completedChecks, bossGates: bossGates };
  }

  function fetchText(url) {
    return fetch(url, { cache: 'no-store' }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.text();
    });
  }

  function gateIcons(cleared) {
    var html = '';
    for (var i = 0; i < 4; i++) {
      html += i < cleared
        ? '<span class="gate-cleared" title="Challenge ' + (i+1) + ' cleared">✔</span>'
        : '<span class="gate-locked" title="Challenge ' + (i+1) + ' not yet done">·</span>';
    }
    html += '<span class="gate-label">' + Math.min(cleared, 4) + '/4</span>';
    return html;
  }

  function progressBar(n) {
    var pct = Math.min(100, Math.round(n / TOTAL * 100));
    return '<div class="lb-bar"><div class="lb-fill" style="width:' + pct + '%"></div></div>';
  }

  function rankCell(i) {
    if (i === 0) return '🥇';
    if (i === 1) return '🥈';
    if (i === 2) return '🥉';
    return i + 1;
  }

  function renderTable(entries) {
    if (!entries.length) {
      return '<p>No students registered yet — the instructor will add them before class.</p>';
    }
    var html = '<table class="lb-table"><thead><tr>'
      + '<th>Rank</th><th>Name</th><th>Level</th><th>Challenges</th><th>Progress</th>'
      + '</tr></thead><tbody>';

    entries.forEach(function (e, i) {
      var allClear = e.bossGates >= 4;
      var rowClass = allClear ? 'lb-all-clear' : (i === 0 ? 'lb-leader' : '');
      html += '<tr class="' + rowClass + '">'
        + '<td class="lb-rank">' + rankCell(i) + '</td>'
        + '<td class="lb-name">' + e.name + (allClear ? '<span class="lb-crown">👑</span>' : '') + '</td>'
        + '<td class="lb-level">' + levelBadge(e.completedChecks) + '</td>'
        + '<td class="lb-gates">' + gateIcons(e.bossGates) + '</td>'
        + '<td class="lb-bar-wrap">' + progressBar(e.completedChecks) + '</td>'
        + '</tr>';
    });

    html += '</tbody></table>';
    return html;
  }

  function load() {
    var container = document.getElementById('lb-container');
    var ts = document.getElementById('lb-timestamp');
    container.innerHTML = '<p class="lb-loading">Loading…</p>';

    fetchText(RAW + '/' + MAIN + '/' + BRANCH + '/docs/_data/students.yml')
      .then(function (text) {
        var students = parseStudents(text);
        if (!students.length) {
          container.innerHTML = '<p>No students enrolled yet.</p>';
          return;
        }
        return Promise.all(students.map(function (s) {
          var url = RAW + '/' + s.username + '/' + (s.repo || REPO) + '/' + BRANCH + '/quest_log.json';
          return fetchText(url)
            .then(function (t) { return Object.assign({}, s, parseQuestLog(t)); })
            .catch(function () { return Object.assign({}, s, { completedChecks: 0, bossGates: 0 }); });
        })).then(function (entries) {
          entries.sort(function (a, b) {
            var cd = b.completedChecks - a.completedChecks;
            return cd !== 0 ? cd : b.bossGates - a.bossGates;
          });
          container.innerHTML = renderTable(entries);
          ts.textContent = 'Updated ' + new Date().toLocaleTimeString();
        });
      })
      .catch(function () {
        container.innerHTML = '<p>Could not load student list. Check back soon.</p>';
      });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('lb-refresh').addEventListener('click', load);
    load();
    setInterval(load, 120000); // auto-refresh every 2 minutes
  });
})();
</script>
