---
layout: default
title: "Leaderboard"
nav_order: 5
permalink: /leaderboard/
---

# 🏆 DARC Dungeon Leaderboard

*Rankings update when students sync their quest logs. Each completed main quest or side quest adds to your **Quest Log**; your total drives your **Level** (max Level 10 — Archmage, 31/31 Quest Log complete). **Boss Gates** = floors cleared (max 4).*

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
  var MAIN   = 'gsbdarc/rf-bootcamp-2026';
  var REPO   = 'rf-bootcamp-2026';
  var BRANCH = 'main';
  var TOTAL  = 30;

  var LEVEL_TITLES = [
    'Initiate', 'Apprentice', 'Scholar', 'Journeyman', 'Adept',
    'Specialist', 'Expert', 'Veteran', 'Master', 'Archmage',
  ];

  function computeLevel(checks) {
    return Math.min(10, Math.floor(checks / TOTAL * 9) + 1);
  }

  function levelBadge(checks) {
    var lv = computeLevel(checks);
    return '<span class="lb-level-num">Lv.' + lv + '</span>'
      + '<span class="lb-level-title">' + LEVEL_TITLES[lv - 1] + '</span>';
  }

  function parseStudents(text) {
    var students = [], re = /^- username:\s*(\S+)/gm, m;
    while ((m = re.exec(text)) !== null) {
      var username = m[1].replace(/['"]/g, '');
      var after = text.slice(m.index + m[0].length);
      var nm = after.match(/^[\s\S]*?name:\s*["']?(.+?)["']?\s*$/m);
      students.push({ username: username, name: nm ? nm[1].trim() : username });
    }
    return students;
  }

  function parseProgress(text) {
    var floors = [], re = /^- (\d+)/gm, m;
    while ((m = re.exec(text)) !== null) floors.push(parseInt(m[1]));
    var cm = text.match(/^completed_checks:\s*(\d+)/m);
    return {
      floors: floors.length ? floors : [1],
      completedChecks: cm ? parseInt(cm[1]) : 0
    };
  }

  function fetchText(url) {
    return fetch(url, { cache: 'no-store' }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.text();
    });
  }

  function gateIcons(maxFloor) {
    var cleared = Math.max(0, maxFloor - 1);
    var html = '';
    for (var i = 0; i < 4; i++) {
      html += i < cleared
        ? '<span class="gate-cleared" title="Boss Gate ' + (i+1) + ' cleared">⚔</span>'
        : '<span class="gate-locked" title="Boss Gate ' + (i+1) + ' locked">·</span>';
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
      + '<th>Rank</th><th>Name</th><th>Level</th><th>Boss Gates</th><th>Progress</th>'
      + '</tr></thead><tbody>';

    entries.forEach(function (e, i) {
      var maxFloor = Math.max.apply(null, e.floors);
      var allClear = maxFloor >= 5;
      var rowClass = allClear ? 'lb-all-clear' : (i === 0 ? 'lb-leader' : '');
      html += '<tr class="' + rowClass + '">'
        + '<td class="lb-rank">' + rankCell(i) + '</td>'
        + '<td class="lb-name">' + e.name + (allClear ? '<span class="lb-crown">👑</span>' : '') + '</td>'
        + '<td class="lb-level">' + levelBadge(e.completedChecks) + '</td>'
        + '<td class="lb-gates">' + gateIcons(maxFloor) + '</td>'
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
          var url = RAW + '/' + s.username + '/' + REPO + '/' + BRANCH + '/docs/_data/progress.yml';
          return fetchText(url)
            .then(function (t) { return Object.assign({}, s, parseProgress(t)); })
            .catch(function () { return Object.assign({}, s, { floors: [1], completedChecks: 0 }); });
        })).then(function (entries) {
          entries.sort(function (a, b) {
            var cd = b.completedChecks - a.completedChecks;
            return cd !== 0 ? cd : Math.max.apply(null, b.floors) - Math.max.apply(null, a.floors);
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
