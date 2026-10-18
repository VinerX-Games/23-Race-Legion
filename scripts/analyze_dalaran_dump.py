# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent

out_lines = []
def log(s=""):
    print(s)
    out_lines.append(s)

with open(ROOT / 'scripts/dalaran_raw_dump.json', encoding='utf-8') as f:
    d = json.load(f)

log('=== 1. SELECTION ABILITY ===')
s = d['selection']
log(f"ID: {s['id']}, name: {s['name']} ({s['raw_name']}), hotkey: {s['hotkey']} ({s['raw_hotkey']})")
log(f"tip1: {s['tips'].get('tip1')}")
log(f"ubertip1: {s['ubertips'].get('ubertip1')}")

log('\n=== 2. SELECTION MARKERS ===')
for m in d['selection_markers']:
    log(f"ID: {m['id']}, class: {m['raw_class']}")
    for k in m['names']:
        log(f"  {k}: {m['names'][k]}")
    for k in m['tips']:
        log(f"  {k}: {m['tips'][k]}")
    for k in m['ubertips']:
        log(f"  {k}: {m['ubertips'][k]}")

log('\n=== 3. BUILDINGS ===')
for b in d['buildings']:
    log(f"{b['id']}: name={b['name']} ({b['raw_name']}) | tip={b['tip']} ({b['raw_tip']}) | hotkey={b['hotkey']} ({b['raw_hotkey']})")
    log(f"   ubertip={b['raw_ubertip']}: {repr(b['ubertip'])[:120]}...")
    log(f"   trains: {b['trains']} | researches: {b['researches']} | upg: {b['upgrades_to']}")

log('\n=== 4. UNITS ===')
for u in d['units']:
    log(f"{u['id']}: name={u['name']} ({u['raw_name']}) | tip={u['tip']} ({u['raw_tip']}) | hotkey={u['hotkey']} ({u['raw_hotkey']})")
    log(f"   ubertip={u['raw_ubertip']}: {repr(u['ubertip'])[:120]}...")
    log(f"   abils: {u['abils']} | upgs: {u['upgrades']} | atk1_targs={u['targs1']}, atk2_targs={u['targs2']}")

log('\n=== 5. HEROES ===')
for h in d['heroes']:
    log(f"{h['id']}: name={h['name']} ({h['raw_name']}) | tip={h['tip']} ({h['raw_tip']}) | hotkey={h['hotkey']} ({h['raw_hotkey']})")
    log(f"   propernames={h['propernames']} ({h['raw_propernames']})")
    log(f"   ubertip={h['raw_ubertip']}: {repr(h['ubertip'])[:120]}...")
    log(f"   heroabils: {h['heroabils']} | abils: {h['abils']} | atk1_targs={h['targs1']}")

log('\n=== 6. UPGRADES ===')
for u in d['upgrades']:
    log(f"{u['id']}: levels={u['levels']}, class={u['raw_class']}")
    for i in range(1, u['levels'] + 1):
        name = u['names'].get(f'name{i}', {})
        tip = u['tips'].get(f'tip{i}', {})
        ubt = u['ubertips'].get(f'ubertip{i}', {})
        hk = u['hotkeys'].get(f'hotkey{i}', {})
        log(f"   lvl {i}: name={name.get('val')} ({name.get('raw')}) | tip={tip.get('val')} ({tip.get('raw')}) | hk={hk.get('val')} ({hk.get('raw')})")
        log(f"          ubt={repr(ubt.get('val'))[:120]} ({ubt.get('raw')})")

log('\n=== 7. ABILITIES ===')
for a in d['abilities']:
    log(f"{a['id']}: levels={a['levels']}, name={a['name']} ({a['raw_name']}) | hotkey={a['hotkey']} ({a['raw_hotkey']})")
    for i in range(1, a['levels'] + 1):
        tip = a['tips'].get(f'tip{i}', {})
        ubt = a['ubertips'].get(f'ubertip{i}', {})
        log(f"   lvl {i}: tip={tip.get('val')} ({tip.get('raw')}) | ubt={repr(ubt.get('val'))[:120]} ({ubt.get('raw')})")
    if a.get('researchtip'):
        log(f"   learn: tip={a.get('researchtip')} ({a.get('raw_researchtip')}) | hk={a.get('researchhotkey')} | ubt={repr(a.get('researchubertip'))[:120]} ({a.get('raw_researchubertip')})")

with open(ROOT / 'scripts/dalaran_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
log("\nWrote analysis to scripts/dalaran_analysis.txt")
