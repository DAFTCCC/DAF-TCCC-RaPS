import fs from 'node:fs';
import vm from 'node:vm';

const context = { window: {} };
vm.createContext(context);
vm.runInContext(fs.readFileSync('www/tiers.js', 'utf8'), context, { filename: 'tiers.js' });
const tiers = context.window.TCCC_TIERS;
if (!tiers) throw new Error('TCCC_TIERS did not load.');

const expected = {
  '1': {criteria:33, critical:17, timers:3},
  '2': {criteria:71, critical:16, timers:3},
  '3': {criteria:124, critical:28, timers:7},
  '4': {criteria:124, critical:30, timers:9},
};
for (const id of ['1','2','3','4']) {
  const t = tiers[id];
  if (!t) throw new Error(`Missing Tier ${id}.`);
  if (!Array.isArray(t.sections) || !t.sections.length) throw new Error(`Tier ${id} has no sections.`);
  const items = t.sections.flatMap(s => s.items || []);
  const ids = new Set();
  for (const item of items) {
    if (!item.id || !item.text) throw new Error(`Tier ${id} contains a criterion without id/text.`);
    if (ids.has(item.id)) throw new Error(`Tier ${id} duplicate criterion id: ${item.id}`);
    ids.add(item.id);
    if (!['source','daf'].includes(item.provenance || 'source')) throw new Error(`Tier ${id} invalid provenance on ${item.id}`);
  }
  for (const timer of (t.timers || [])) {
    if (!timer.id || !timer.label) throw new Error(`Tier ${id} has malformed timer.`);
    if (timer.linkedItemId && !ids.has(timer.linkedItemId)) throw new Error(`Tier ${id} timer ${timer.id} links to missing ${timer.linkedItemId}`);
  }
  if (!Array.isArray(t.ratings) || t.ratings.map(r=>r.key).join(',') !== 'pass,fail,nt') {
    throw new Error(`Tier ${id} ratings must be PASS / FAIL / NT only.`);
  }
  if (items.length !== expected[id].criteria || items.filter(i=>i.critical).length !== expected[id].critical || (t.timers||[]).length !== expected[id].timers) {
    throw new Error(`Tier ${id} content/timer count changed unexpectedly.`);
  }
  if (/N\/O/.test(t.instructions || '')) throw new Error(`Tier ${id} instructions still expose N/O.`);
  console.log(`Tier ${id}: ${items.length} criteria, ${items.filter(i=>i.critical).length} critical, ${(t.timers||[]).length} timers — OK`);
}
console.log('TCCC v3 content validation passed.');
