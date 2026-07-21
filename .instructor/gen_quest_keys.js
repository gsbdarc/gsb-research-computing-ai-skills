// Regenerate scripts/quest_keys.json from the DAYS registry in
// docs/assets/js/quest-log.js. The JSON is the canonical, ordered list of quest
// keys that both the Quest Log token encoder (quest-log.js) and the decoder
// (scripts/quest_sync.py) rely on. Run this after changing DAYS:
//
//     node .instructor/gen_quest_keys.js
//
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const src = fs.readFileSync(path.join(ROOT, "docs/assets/js/quest-log.js"), "utf8");

const m = src.match(/const DAYS = (\[[\s\S]*?\n  \]);/);
if (!m) {
  console.error("Could not find the DAYS array in docs/assets/js/quest-log.js");
  process.exit(1);
}
const DAYS = eval(m[1]);

const keys = [];
DAYS.forEach((d) => d.rooms.forEach((r) => r.keys.forEach((k) => keys.push(r.id + "." + k))));

const out = path.join(ROOT, "scripts", "quest_keys.json");
fs.writeFileSync(out, JSON.stringify(keys) + "\n");
console.log(`Wrote ${keys.length} keys to ${path.relative(ROOT, out)}`);
