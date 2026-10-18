# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "scripts/silitids_raw_dump.json", encoding="utf-8"))

def parse_sid(raw):
    if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
        try:
            return int(raw[8:])
        except ValueError:
            return None
    return None

wts_map = {}

# 1. Selection
s = data['selection']
for f in ['raw_name']:
    sid = parse_sid(s.get(f))
    if sid: wts_map[sid] = ('selection', s['id'], 'name')
sid = parse_sid(s['tips']['tip1']['raw'])
if sid: wts_map[sid] = ('selection', s['id'], 'tip1')
sid = parse_sid(s['ubertips']['ubertip1']['raw'])
if sid: wts_map[sid] = ('selection', s['id'], 'ubertip1')

# 2. Markers
for m in data['selection_markers']:
    for lvl in range(1, m['levels'] + 1):
        for fld in ['name', 'tip', 'ubertip']:
            sid = parse_sid(m[f'{fld}s'][f'{fld}{lvl}']['raw'])
            if sid: wts_map[sid] = ('marker', m['id'], f'{fld}{lvl}')

# 3. Buildings
for b in data['buildings']:
    for f in ['name', 'tip', 'ubertip']:
        sid = parse_sid(b.get(f'raw_{f}'))
        if sid: wts_map[sid] = ('building', b['id'], f)

# 4. Units
for u in data['units']:
    for f in ['name', 'tip', 'ubertip']:
        sid = parse_sid(u.get(f'raw_{f}'))
        if sid: wts_map[sid] = ('unit', u['id'], f)

# 5. Heroes
for h in data['heroes']:
    for f in ['name', 'propernames', 'tip', 'ubertip', 'awakentip', 'revivetip']:
        sid = parse_sid(h.get(f'raw_{f}'))
        if sid: wts_map[sid] = ('hero', h['id'], f)

# 6. Upgrades
for up in data['upgrades']:
    for lvl in range(1, up['levels'] + 1):
        for fld in ['name', 'tip', 'ubertip']:
            raw_v = up[f'{fld}s'].get(f'{fld}{lvl}', {}).get('raw')
            sid = parse_sid(raw_v)
            if sid: wts_map[sid] = ('upgrade', up['id'], f'{fld}{lvl}')

# 7. Abilities
for a in data['abilities']:
    sid = parse_sid(a.get('raw_name'))
    if sid: wts_map[sid] = ('ability', a['id'], 'name')
    sid = parse_sid(a.get('raw_researchtip'))
    if sid: wts_map[sid] = ('ability', a['id'], 'researchtip')
    sid = parse_sid(a.get('raw_researchubertip'))
    if sid: wts_map[sid] = ('ability', a['id'], 'researchubertip')
    for lvl in range(1, a['levels'] + 1):
        raw_t = a['tips'].get(f'tip{lvl}', {}).get('raw')
        sid = parse_sid(raw_t)
        if sid: wts_map[sid] = ('ability', a['id'], f'tip{lvl}')
        raw_ub = a['ubertips'].get(f'ubertip{lvl}', {}).get('raw')
        sid = parse_sid(raw_ub)
        if sid: wts_map[sid] = ('ability', a['id'], f'ubertip{lvl}')

# 8. Buffs
for b in data['buffs']:
    sid = b.get('bufftip_sid')
    if sid: wts_map[sid] = ('buff', b['id'], 'bufftip')
    sid = b.get('buffubertip_sid')
    if sid: wts_map[sid] = ('buff', b['id'], 'buffubertip')
    sid = b.get('editorname_sid')
    if sid: wts_map[sid] = ('buff', b['id'], 'editorname')

# 9. Trigger messages
wts_map[38642] = ('message', 'triggers', 'TRIGSTR_38642')

print(f"Total unique WTS string mappings: {len(wts_map)}")
print("Categories count:")
from collections import Counter
counts = Counter([v[0] for v in wts_map.values()])
for cat, cnt in counts.most_common():
    print(f"  {cat}: {cnt}")
