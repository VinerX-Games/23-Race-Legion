# -*- coding: utf-8 -*-
"""Draft and verify all Night Elf UI texts."""
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8')
dump = json.loads((ROOT / 'scripts/nightelf_raw_dump.json').read_text(encoding='utf-8'))

# Collect all WTS string IDs that actually exist in the raw dump
wts_candidates = {}

def add_wts(sid, category, oid, field, original):
    if sid is not None and sid > 0:
        wts_candidates[sid] = {
            'cat': category,
            'id': oid,
            'field': field,
            'orig': original
        }

def parse_sid(raw):
    if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
        try:
            return int(raw[8:])
        except ValueError:
            return None
    return None

# Selection
add_wts(parse_sid(dump['selection']['raw_name']), 'selection', 'A0HL', 'name', dump['selection']['name'])
add_wts(parse_sid(dump['selection']['tips']['tip1']['raw']), 'selection', 'A0HL', 'tip1', dump['selection']['tips']['tip1']['val'])
add_wts(parse_sid(dump['selection']['ubertips']['ubertip1']['raw']), 'selection', 'A0HL', 'ubertip1', dump['selection']['ubertips']['ubertip1']['val'])

# Marker
m = dump['selection_markers'][0]
add_wts(parse_sid(m['names']['name1']['raw']), 'marker', 'R07L', 'name1', m['names']['name1']['val'])
add_wts(parse_sid(m['tips']['tip1']['raw']), 'marker', 'R07L', 'tip1', m['tips']['tip1']['val'])
add_wts(parse_sid(m['ubertips']['ubertip1']['raw']), 'marker', 'R07L', 'ubertip1', m['ubertips']['ubertip1']['val'])

# Buildings
for b in dump['buildings']:
    bid = b['id']
    add_wts(parse_sid(b.get('raw_name')), 'building', bid, 'name', b.get('name'))
    add_wts(parse_sid(b.get('raw_tip')), 'building', bid, 'tip', b.get('tip'))
    add_wts(parse_sid(b.get('raw_ubertip')), 'building', bid, 'ubertip', b.get('ubertip'))

# Worker & Units
for u in dump['workers'] + dump['units']:
    uid = u['id']
    add_wts(parse_sid(u.get('raw_name')), 'unit', uid, 'name', u.get('name'))
    add_wts(parse_sid(u.get('raw_tip')), 'unit', uid, 'tip', u.get('tip'))
    add_wts(parse_sid(u.get('raw_ubertip')), 'unit', uid, 'ubertip', u.get('ubertip'))

# Heroes
for h in dump['heroes']:
    hid = h['id']
    add_wts(parse_sid(h.get('raw_name')), 'hero', hid, 'name', h.get('name'))
    add_wts(parse_sid(h.get('raw_tip')), 'hero', hid, 'tip', h.get('tip'))
    add_wts(parse_sid(h.get('raw_ubertip')), 'hero', hid, 'ubertip', h.get('ubertip'))
    add_wts(parse_sid(h.get('raw_propernames')), 'hero', hid, 'propernames', h.get('propernames'))
    add_wts(parse_sid(h.get('raw_awakentip')), 'hero', hid, 'awakentip', h.get('awakentip'))
    add_wts(parse_sid(h.get('raw_revivetip')), 'hero', hid, 'revivetip', h.get('revivetip'))

# Upgrades
for upg in dump['upgrades']:
    uid = upg['id']
    for i in range(1, upg['levels'] + 1):
        n = upg['names'].get(f'name{i}', {})
        t = upg['tips'].get(f'tip{i}', {})
        ub = upg['ubertips'].get(f'ubertip{i}', {})
        add_wts(parse_sid(n.get('raw')), 'upgrade', uid, f'name{i}', n.get('val'))
        add_wts(parse_sid(t.get('raw')), 'upgrade', uid, f'tip{i}', t.get('val'))
        add_wts(parse_sid(ub.get('raw')), 'upgrade', uid, f'ubertip{i}', ub.get('val'))

# Abilities
for ab in dump['abilities']:
    aid = ab['id']
    add_wts(parse_sid(ab.get('raw_name')), 'ability', aid, 'name', ab.get('name'))
    add_wts(parse_sid(ab.get('raw_researchtip')), 'ability', aid, 'researchtip', ab.get('researchtip'))
    add_wts(parse_sid(ab.get('raw_researchubertip')), 'ability', aid, 'researchubertip', ab.get('researchubertip'))
    add_wts(parse_sid(ab.get('raw_untip')), 'ability', aid, 'untip', ab.get('untip'))
    add_wts(parse_sid(ab.get('raw_unubertip')), 'ability', aid, 'unubertip', ab.get('unubertip'))
    for i in range(1, ab['levels'] + 1):
        t = ab['tips'].get(f'tip{i}', {})
        ub = ab['ubertips'].get(f'ubertip{i}', {})
        add_wts(parse_sid(t.get('raw')), 'ability', aid, f'tip{i}', t.get('val'))
        add_wts(parse_sid(ub.get('raw')), 'ability', aid, f'ubertip{i}', ub.get('val'))

print(f"Total candidate WTS IDs for Night Elf: {len(wts_candidates)}")
by_cat = {}
for sid, info in wts_candidates.items():
    by_cat[info['cat']] = by_cat.get(info['cat'], 0) + 1
for cat, cnt in sorted(by_cat.items()):
    print(f"  {cat}: {cnt}")
