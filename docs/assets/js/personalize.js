/* DARC Bootcamp — Personalize commands
 * Replaces the `SUNetID` placeholder inside code blocks with the value the
 * learner sets in the Quest Log (see quest-log.js), stored in localStorage.
 *
 * Coordination with quest-log.js:
 *   - it reads/writes the same localStorage key and fires `sunet:changed`
 *     when the value changes;  this script re-renders the tokens.
 *   - when an *unset* placeholder is clicked, this script fires `sunet:open`
 *     to pop open the Quest Log with the SUNet field focused.
 */
(function () {
  'use strict';

  var KEY = 'bootcamp.sunetid';
  var PLACEHOLDER = 'SUNetID';

  function getId() {
    try { return (localStorage.getItem(KEY) || '').trim(); } catch (_) { return ''; }
  }

  function injectStyles() {
    var css =
      '.sunet-token{border-bottom:1px dashed currentColor;border-radius:2px;padding:0 1px;}' +
      '.sunet-token.sunet-unset{cursor:pointer;background:rgba(230,126,34,.18);color:#b3611a;font-style:italic;}' +
      '.sunet-token.sunet-unset:hover{background:rgba(230,126,34,.30);}';
    var s = document.createElement('style');
    s.textContent = css;
    document.head.appendChild(s);
  }

  // Wrap every `SUNetID` occurrence inside code in a span (once).
  function wrapTokens() {
    var codes = document.querySelectorAll('pre code, code');
    codes.forEach(function (code) {
      var walker = document.createTreeWalker(code, NodeFilter.SHOW_TEXT, null);
      var nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);
      nodes.forEach(function (node) {
        if (node.parentNode && node.parentNode.classList &&
            node.parentNode.classList.contains('sunet-token')) return;
        if (node.nodeValue.indexOf(PLACEHOLDER) === -1) return;
        var parts = node.nodeValue.split(PLACEHOLDER);
        var frag = document.createDocumentFragment();
        parts.forEach(function (part, i) {
          if (part) frag.appendChild(document.createTextNode(part));
          if (i < parts.length - 1) {
            var span = document.createElement('span');
            span.className = 'sunet-token';
            frag.appendChild(span);
          }
        });
        node.parentNode.replaceChild(frag, node);
      });
    });
  }

  function renderTokens() {
    var id = getId();
    document.querySelectorAll('.sunet-token').forEach(function (s) {
      s.textContent = id || PLACEHOLDER;
      if (id) {
        // Set: just an underlined value with a reminder — not clickable.
        s.classList.remove('sunet-unset');
        s.removeAttribute('role');
        s.removeAttribute('tabindex');
        s.title = 'This is your SUNet ID — change it in your Quest Log';
      } else {
        // Unset: highlighted and clickable to open the Quest Log.
        s.classList.add('sunet-unset');
        s.setAttribute('role', 'button');
        s.setAttribute('tabindex', '0');
        s.title = 'Click to set your SUNet ID in your Quest Log';
      }
    });
  }

  // SVG <text> can't hold clickable spans, so we just fill it in (and re-fill
  // on change), keeping the original template so it can revert.
  var svgNodes = [];
  function collectSvg() {
    document.querySelectorAll('svg').forEach(function (svg) {
      var walker = document.createTreeWalker(svg, NodeFilter.SHOW_TEXT, null);
      while (walker.nextNode()) {
        var n = walker.currentNode;
        if (n.nodeValue.indexOf(PLACEHOLDER) !== -1) {
          svgNodes.push({ node: n, template: n.nodeValue });
        }
      }
    });
  }
  function renderSvg() {
    var id = getId();
    svgNodes.forEach(function (rec) {
      rec.node.nodeValue = rec.template.split(PLACEHOLDER).join(id || PLACEHOLDER);
    });
  }

  function openQuestLog() {
    // Deferred so this click doesn't also trigger the Quest Log's
    // click-outside-to-close handler on the same event.
    setTimeout(function () {
      document.dispatchEvent(new CustomEvent('sunet:open'));
    }, 0);
  }

  document.addEventListener('click', function (e) {
    var token = e.target.closest ? e.target.closest('.sunet-token.sunet-unset') : null;
    if (token) openQuestLog();
  });
  document.addEventListener('keydown', function (e) {
    if ((e.key === 'Enter' || e.key === ' ') && e.target.classList &&
        e.target.classList.contains('sunet-unset')) {
      e.preventDefault();
      openQuestLog();
    }
  });

  // The Quest Log tells us when the value changed.
  document.addEventListener('sunet:changed', function () {
    renderTokens();
    renderSvg();
  });

  document.addEventListener('DOMContentLoaded', function () {
    injectStyles();
    wrapTokens();
    renderTokens();
    collectSvg();
    renderSvg();
  });
})();
