# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / 'scripts/hordew2_raw_dump.json', encoding='utf-8'))

print("=== UPGRADES IN DUMP ===")
for up in data['upgrades']:
    sids = []
    for f in ['names', 'tips', 'ubertips']:
        for lvl, val in up.get(f, {}).items():
            if val.get('sid'):
                sids.append((f, lvl, val['sid'], val.get('val', '')[:40].replace('\n', ' ')))
    print(f"[{up['id']}] levels={up.get('levels')} (total sids: {len(sids)})")
    for s in sids:
        print(f"    {s[0]}_{s[1]}: sid={s[2]} -> {s[3]}")

print("\n=== ABILITIES IN DUMP ===")
for ab in data['abilities']:
    sids = []
    if ab.get('raw_name') and ab.get('raw_name').startswith('TRIGSTR_'):
        sids.append(('name', int(ab['raw_name'][8:]), ab.get('name', '')))
    for f in ['tips', 'ubertips']:
        for lvl, val in ab.get(f, {}).items():
            if val.get('sid'):
                sids.append((f"{f}_{lvl}", val['sid'], val.get('val', '')[:40].replace('\n', ' ')))
    for f in ['researchtip', 'researchubertip']:
        raw_f = f"raw_{f}"
        if ab.get(raw_f) and ab.get(raw_f).startswith('TRIGSTR_'):
            sids.append((f, int(ab[raw_f][8:]), ab.get(f, '')[:40].replace('\n', ' ')))
    print(f"[{ab['id']}] {ab.get('name')} (levels: {ab.get('levels')}) total_sids: {len(sids)}")
    for s in sids:
        print(f"    {s[0]}: sid={s[1]} -> {s[2]}")
