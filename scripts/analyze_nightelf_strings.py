# -*- coding: utf-8 -*-
"""Analyze all strings in nightelf_raw_dump.json."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/nightelf_raw_dump.json"
dump = json.loads(dump_file.read_text(encoding="utf-8"))

def parse_sid(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        try:
            return int(val[8:])
        except ValueError:
            return None
    return None

wts_map = {}

def check_obj(category, obj, fields):
    oid = obj.get('id')
    for f in fields:
        raw = obj.get(f"raw_{f}")
        val = obj.get(f)
        sid = parse_sid(raw)
        if sid is not None:
            wts_map[sid] = {
                'cat': category,
                'id': oid,
                'field': f,
                'raw': raw,
                'val': val
            }

# Selection
check_obj('selection', dump['selection'], ['name', 'tip1', 'ubertip1'])
# Marker
for m in dump['selection_markers']:
    for i in range(1, m['levels'] + 1):
        for f in ['name', 'tip', 'ubertip']:
            raw = m[f'{f}s'].get(f'{f}{i}', {}).get('raw')
            val = m[f'{f}s'].get(f'{f}{i}', {}).get('val')
            sid = parse_sid(raw)
            if sid is not None:
                wts_map[sid] = {'cat': 'selection_marker', 'id': m['id'], 'field': f'{f}{i}', 'raw': raw, 'val': val}

# Workers
for w in dump['workers']:
    check_obj('worker', w, ['name', 'tip', 'ubertip', 'hotkey'])

# Buildings
for b in dump['buildings']:
    check_obj('building', b, ['name', 'tip', 'ubertip', 'hotkey'])

# Units
for u in dump['units']:
    check_obj('unit', u, ['name', 'tip', 'ubertip', 'hotkey'])

# Heroes
for h in dump['heroes']:
    check_obj('hero', h, ['name', 'tip', 'ubertip', 'propernames', 'awakentip', 'revivetip', 'hotkey'])

# Upgrades
for upg in dump['upgrades']:
    uid = upg['id']
    for i in range(1, upg['levels'] + 1):
        for f in ['name', 'tip', 'ubertip', 'hotkey']:
            fk = f'{f}s'
            item = upg[fk].get(f'{f}{i}')
            if item:
                raw = item.get('raw')
                val = item.get('val')
                sid = parse_sid(raw)
                if sid is not None:
                    wts_map[sid] = {'cat': 'upgrade', 'id': uid, 'field': f'{f}{i}', 'raw': raw, 'val': val}

# Abilities
for ab in dump['abilities']:
    aid = ab['id']
    check_obj('ability', ab, ['name', 'hotkey', 'researchhotkey', 'researchtip', 'researchubertip', 'untip', 'unubertip', 'unhotkey'])
    for i in range(1, ab['levels'] + 1):
        t_item = ab['tips'].get(f'tip{i}')
        if t_item:
            raw = t_item.get('raw')
            val = t_item.get('val')
            sid = parse_sid(raw)
            if sid is not None:
                wts_map[sid] = {'cat': 'ability', 'id': aid, 'field': f'tip{i}', 'raw': raw, 'val': val}
        ub_item = ab['ubertips'].get(f'ubertip{i}')
        if ub_item:
            raw = ub_item.get('raw')
            val = ub_item.get('val')
            sid = parse_sid(raw)
            if sid is not None:
                wts_map[sid] = {'cat': 'ability', 'id': aid, 'field': f'ubertip{i}', 'raw': raw, 'val': val}

# Buffs
for bf in dump['buffs']:
    check_obj('buff', bf, ['bufftip', 'buffubertip', 'editorname'])

print(f"Total unique TRIGSTR strings mapped: {len(wts_map)}")
cats = {}
for sid, info in wts_map.items():
    cats[info['cat']] = cats.get(info['cat'], 0) + 1
for cat, cnt in sorted(cats.items()):
    print(f"  {cat}: {cnt}")

out_analysis = ROOT / "scripts/nightelf_analysis.txt"
with open(out_analysis, 'w', encoding='utf-8') as f:
    for sid in sorted(wts_map.keys()):
        info = wts_map[sid]
        f.write(f"STRING {sid} [{info['cat']}] [{info['id']}.{info['field']}]:\n{info['val']}\n\n")

print(f"Saved analysis to {out_analysis}")
