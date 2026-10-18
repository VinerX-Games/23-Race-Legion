# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('scripts/cult_raw_dump.json', encoding='utf-8'))

wts_by_category = {
    'selection': {},
    'selection_markers': {},
    'buildings': {},
    'heroes': {},
    'units': {},
    'upgrades': {},
    'abilities': {}
}

# Selection
s = data['selection']
for k in ['name_sid', 'researchtip_sid', 'researchubertip_sid', 'untip_sid', 'unubertip_sid']:
    if s.get(k): wts_by_category['selection'][s[k]] = (s['id'], k, s.get(k.replace('_sid', '')))
for t_key, t_val in s.get('tips', {}).items():
    if t_val.get('sid'): wts_by_category['selection'][t_val['sid']] = (s['id'], t_key, t_val.get('val'))
for u_key, u_val in s.get('ubertips', {}).items():
    if u_val.get('sid'): wts_by_category['selection'][u_val['sid']] = (s['id'], u_key, u_val.get('val'))

# Selection markers
for m in data['selection_markers']:
    mid = m['id']
    for k, v in m.get('names', {}).items():
        if v.get('sid'): wts_by_category['selection_markers'][v['sid']] = (mid, k, v.get('val'))
    for k, v in m.get('tips', {}).items():
        if v.get('sid'): wts_by_category['selection_markers'][v['sid']] = (mid, k, v.get('val'))
    for k, v in m.get('ubertips', {}).items():
        if v.get('sid'): wts_by_category['selection_markers'][v['sid']] = (mid, k, v.get('val'))

# Buildings
for b in data['buildings']:
    bid = b['id']
    for k in ['name_sid', 'tip_sid', 'ubertip_sid']:
        if b.get(k): wts_by_category['buildings'][b[k]] = (bid, k, b.get(k.replace('_sid', '')))

# Heroes
for h in data['heroes']:
    hid = h['id']
    for k in ['name_sid', 'tip_sid', 'ubertip_sid']:
        if h.get(k): wts_by_category['heroes'][h[k]] = (hid, k, h.get(k.replace('_sid', '')))
    raw_aw = h.get('raw_awakentip', '')
    if raw_aw.startswith('TRIGSTR_'):
        wts_by_category['heroes'][int(raw_aw[8:])] = (hid, 'awakentip', h.get('awakentip'))
    raw_rev = h.get('raw_revivetip', '')
    if raw_rev.startswith('TRIGSTR_'):
        wts_by_category['heroes'][int(raw_rev[8:])] = (hid, 'revivetip', h.get('revivetip'))
    raw_prop = h.get('raw_propernames', '')
    if raw_prop.startswith('TRIGSTR_'):
        wts_by_category['heroes'][int(raw_prop[8:])] = (hid, 'propernames', h.get('propernames'))

# Units
for u in data['units']:
    uid = u['id']
    for k in ['name_sid', 'tip_sid', 'ubertip_sid']:
        if u.get(k): wts_by_category['units'][u[k]] = (uid, k, u.get(k.replace('_sid', '')))

# Upgrades
for up in data['upgrades']:
    upid = up['id']
    for k, v in up.get('names', {}).items():
        if v.get('sid'): wts_by_category['upgrades'][v['sid']] = (upid, k, v.get('val'))
    for k, v in up.get('tips', {}).items():
        if v.get('sid'): wts_by_category['upgrades'][v['sid']] = (upid, k, v.get('val'))
    for k, v in up.get('ubertips', {}).items():
        if v.get('sid'): wts_by_category['upgrades'][v['sid']] = (upid, k, v.get('val'))

# Abilities
for ab in data['abilities']:
    aid = ab['id']
    for k in ['name_sid', 'researchtip_sid', 'researchubertip_sid', 'untip_sid', 'unubertip_sid']:
        if ab.get(k): wts_by_category['abilities'][ab[k]] = (aid, k, ab.get(k.replace('_sid', '')))
    for k, v in ab.get('tips', {}).items():
        if v.get('sid'): wts_by_category['abilities'][v['sid']] = (aid, k, v.get('val'))
    for k, v in ab.get('ubertips', {}).items():
        if v.get('sid'): wts_by_category['abilities'][v['sid']] = (aid, k, v.get('val'))

total = sum(len(v) for v in wts_by_category.values())
print(f"Total WTS string references across categories: {total}")
for cat, sids in wts_by_category.items():
    print(f"  {cat}: {len(sids)} strings")

all_sids = {}
for cat, sids in wts_by_category.items():
    for sid, info in sids.items():
        if sid in all_sids:
            print(f"COLLISION: SID {sid} used in {all_sids[sid]} and {cat}:{info}")
        all_sids[sid] = f"{cat}:{info}"

print(f"Total unique SIDs: {len(all_sids)}")
