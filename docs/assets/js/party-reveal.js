/* DARC Dungeon — Party Reveal
 * Face-down character cards that flip when clicked.
 *
 * The quest checkbox is deliberately NOT ticked for the student: this is their
 * first encounter with the Quest Log, so turning over the last card only
 * prompts them to tick it themselves, the same as every other quest on the
 * site. We just swap the prompt for a confirmation once they do.
 *
 * Which cards are face-up is remembered separately from quest progress, under
 * its own localStorage key, so a reload does not re-hide the party.
 * No-ops on pages without a .party-reveal block.
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'dungeon.v1.party';

  function loadRevealed() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      var arr = raw ? JSON.parse(raw) : [];
      return Array.isArray(arr) ? arr : [];
    } catch (_) {
      return [];
    }
  }

  function saveRevealed(indices) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(indices));
    } catch (_) { /* storage blocked or full — the cards still work this visit */ }
  }

  function setRevealed(card, on) {
    card.classList.toggle('revealed', on);
    var btn = card.querySelector('.party-flip');
    if (btn) btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  }

  function initBlock(root) {
    var cards = Array.prototype.slice.call(root.querySelectorAll('.party-card'));
    if (!cards.length) return;

    var room = root.getAttribute('data-quest-room');
    var key = root.getAttribute('data-quest-key');
    var checkbox = room && key
      ? document.querySelector('input[data-room="' + room + '"][data-key="' + key + '"]')
      : null;
    var banner = root.querySelector('.party-done');

    function allRevealed() {
      return cards.every(function (c) { return c.classList.contains('revealed'); });
    }

    function syncBanner() {
      if (banner) banner.hidden = !allRevealed();
    }

    cards.forEach(function (card, i) {
      var btn = card.querySelector('.party-flip');
      if (!btn) return;
      btn.addEventListener('click', function () {
        if (card.classList.contains('revealed')) return;  // one-way: no re-hiding
        setRevealed(card, true);
        syncBanner();
        var seen = loadRevealed();
        if (seen.indexOf(i) === -1) { seen.push(i); saveRevealed(seen); }
      });
    });

    // Swap the "now tick the box" prompt for a confirmation once they have.
    if (checkbox) {
      var syncLogged = function () {
        root.classList.toggle('quest-logged', checkbox.checked);
      };
      checkbox.addEventListener('change', syncLogged);
      syncLogged();
    }

    // Restore cards turned over on an earlier visit, without spinning them.
    var seen = loadRevealed();
    if (seen.length) {
      root.classList.add('party-instant');
      seen.forEach(function (i) { if (cards[i]) setRevealed(cards[i], true); });
      syncBanner();
      window.requestAnimationFrame(function () {
        root.classList.remove('party-instant');
      });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    var blocks = document.querySelectorAll('.party-reveal');
    Array.prototype.forEach.call(blocks, initBlock);
  });

})();
