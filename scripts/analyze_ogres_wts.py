# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
dump = json.loads((ROOT / 'scripts/ogres_raw_dump.json').read_text(encoding='utf-8'))

def parse_wts_id(val):
    if isinstance(val, str) and val.startswith('TRIGSTR_'):
        try:
            return int(val[8:])
        except ValueError:
            return None
    return None

wts_needed = {}

# 1. Selection
s = dump['selection']
for f in ['name', 'tip1', 'ubertip1']:
    sid = s.get('tips', {}).get(f, {}).get('sid') or s.get('ubertips', {}).get(f, {}).get('sid')
    if f == 'name': sid = s.get('name_sid') or parse_wts_id(s.get('raw_name'))
    raw = s.get(f'raw_{f}') or s.get('tips', {}).get(f, {}).get('raw') or s.get('ubertips', {}).get(f, {}).get('raw')
    wts_needed[('selection', s['id'], f)] = (parse_wts_id(raw), s.get(f) or s.get('tips', {}).get(f, {}).get('val') or s.get('ubertips', {}).get(f, {}).get('val'))

for m in dump['selection_markers']:
    for f in ['name1', 'tip1', 'ubertip1']:
        raw = m.get('names', {}).get(f, {}).get('raw') or m.get('tips', {}).get(f, {}).get('raw') or m.get('ubertips', {}).get(f, {}).get('raw')
        val = m.get('names', {}).get(f, {}).get('val') or m.get('tips', {}).get(f, {}).get('val') or m.get('ubertips', {}).get(f, {}).get('val')
        wts_needed[('marker', m['id'], f)] = (parse_wts_id(raw), val)

# 2. Buildings
for b in dump['buildings']:
    for f in ['name', 'tip', 'ubertip']:
        raw = b.get(f'raw_{f}')
        val = b.get(f)
        wts_needed[('building', b['id'], f)] = (parse_wts_id(raw), val)

# 3. Units
for u in dump['units']:
    for f in ['name', 'tip', 'ubertip']:
        raw = u.get(f'raw_{f}')
        val = u.get(f)
        wts_needed[('unit', u['id'], f)] = (parse_wts_id(raw), val)

# 4. Heroes
for h in dump['heroes']:
    for f in ['name', 'propernames', 'tip', 'ubertip', 'awakentip', 'revivetip']:
        raw = h.get(f'raw_{f}')
        val = h.get(f)
        wts_needed[('hero', h['id'], f)] = (parse_wts_id(raw), val)

# 5. Upgrades
for u in dump['upgrades']:
    for lvl in range(1, u.get('levels', 1) + 1):
        for f in ['name', 'tip', 'ubertip']:
            field_key = f'{f}{lvl}'
            dic = u.get(f'{f}s', {})
            item = dic.get(field_key, {})
            raw = item.get('raw')
            val = item.get('val')
            wts_needed[('upgrade', u['id'], field_key)] = (parse_wts_id(raw), val)

# 6. Abilities
for a in dump['abilities']:
    raw_name = a.get('raw_name')
    if raw_name:
        wts_needed[('ability', a['id'], 'name')] = (parse_wts_id(raw_name), a.get('name'))
    if a.get('raw_researchtip'):
        wts_needed[('ability', a['id'], 'researchtip')] = (parse_wts_id(a.get('raw_researchtip')), a.get('researchtip'))
    if a.get('raw_researchubertip'):
        wts_needed[('ability', a['id'], 'researchubertip')] = (parse_wts_id(a.get('raw_researchubertip')), a.get('researchubertip'))
    for lvl in range(1, a.get('levels', 1) + 1):
        raw_t = a.get('tips', {}).get(f'tip{lvl}', {}).get('raw')
        val_t = a.get('tips', {}).get(f'tip{lvl}', {}).get('val')
        if raw_t:
            wts_needed[('ability', a['id'], f'tip{lvl}')] = (parse_wts_id(raw_t), val_t)
        raw_ub = a.get('ubertips', {}).get(f'ubertip{lvl}', {}).get('raw')
        val_ub = a.get('ubertips', {}).get(f'ubertip{lvl}', {}).get('val')
        if raw_ub:
            wts_needed[('ability', a['id'], f'ubertip{lvl}')] = (parse_wts_id(raw_ub), val_ub)

# 7. Buffs
for b in dump['buffs']:
    raw_t = b.get('raw_bufftip')
    val_t = b.get('bufftip')
    if raw_t:
        wts_needed[('buff', b['id'], 'bufftip')] = (parse_wts_id(raw_t), val_t)
    raw_ub = b.get('raw_buffubertip')
    val_ub = b.get('buffubertip')
    if raw_ub:
        wts_needed[('buff', b['id'], 'buffubertip')] = (parse_wts_id(raw_ub), val_ub)

print(f"Total fields collected: {len(wts_needed)}")
with_wts = {k: v for k, v in wts_needed.items() if v[0] is not None}
without_wts = {k: v for k, v in wts_needed.items() if v[0] is None}
print(f"With TRIGSTR ID: {len(with_wts)}")
print(f"Without TRIGSTR ID: {len(without_wts)}")

print("\nSample without TRIGSTR:")
for k, v in list(without_wts.items())[:15]:
    print(" ", k, "->", v[1][:50] if v[1] else v[1])
