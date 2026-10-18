# -*- coding: utf-8 -*-
import json
from pathlib import Path

dump = json.loads(Path('scripts/nagi_raw_dump.json').read_text('utf-8'))
wts_sids = {}

def parse_sid(s):
    if isinstance(s, int):
        return s
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        try:
            return int(s[8:])
        except ValueError:
            return None
    return None

def add_sid(sid, source):
    sid = parse_sid(sid)
    if sid is not None:
        if sid not in wts_sids:
            wts_sids[sid] = []
        wts_sids[sid].append(source)

# Selection
add_sid(dump['selection']['name_sid'], 'selection.name')
for k, v in dump['selection']['tips'].items(): add_sid(v.get('sid'), f'selection.{k}')
for k, v in dump['selection']['ubertips'].items(): add_sid(v.get('sid'), f'selection.{k}')

# Markers
for m in dump['selection_markers']:
    for k, v in m.get('names', {}).items(): add_sid(v.get('sid'), f"{m['id']}.{k}")
    for k, v in m.get('tips', {}).items(): add_sid(v.get('sid'), f"{m['id']}.{k}")
    for k, v in m.get('ubertips', {}).items(): add_sid(v.get('sid'), f"{m['id']}.{k}")

# Buildings
for b in dump['buildings']:
    add_sid(b.get('raw_name'), f"{b['id']}.name")
    add_sid(b.get('raw_tip'), f"{b['id']}.tip")
    add_sid(b.get('raw_ubertip'), f"{b['id']}.ubertip")

# Worker
for w in dump['worker']:
    add_sid(w.get('raw_name'), f"{w['id']}.name")
    add_sid(w.get('raw_tip'), f"{w['id']}.tip")
    add_sid(w.get('raw_ubertip'), f"{w['id']}.ubertip")

# Heroes
for h in dump['heroes']:
    add_sid(h.get('raw_name'), f"{h['id']}.name")
    add_sid(h.get('raw_tip'), f"{h['id']}.tip")
    add_sid(h.get('raw_ubertip'), f"{h['id']}.ubertip")

# Units
for u in dump['units']:
    add_sid(u.get('raw_name'), f"{u['id']}.name")
    add_sid(u.get('raw_tip'), f"{u['id']}.tip")
    add_sid(u.get('raw_ubertip'), f"{u['id']}.ubertip")

# Upgrades
for up in dump['upgrades']:
    for k, v in up.get('names', {}).items(): add_sid(v.get('sid'), f"{up['id']}.{k}")
    for k, v in up.get('tips', {}).items(): add_sid(v.get('sid'), f"{up['id']}.{k}")
    for k, v in up.get('ubertips', {}).items(): add_sid(v.get('sid'), f"{up['id']}.{k}")

# Abilities
for ab in dump['abilities']:
    add_sid(ab.get('name_sid'), f"{ab['id']}.name")
    for k, v in ab.get('tips', {}).items(): add_sid(v.get('sid'), f"{ab['id']}.{k}")
    for k, v in ab.get('ubertips', {}).items(): add_sid(v.get('sid'), f"{ab['id']}.{k}")

# Buffs
for bf in dump['buffs']:
    add_sid(bf.get('bufftip_sid'), f"{bf['id']}.bufftip")
    add_sid(bf.get('buffubertip_sid'), f"{bf['id']}.buffubertip")

print(f"Total distinct WTS string IDs found in Nagi objects: {len(wts_sids)}")
for sid, sources in sorted(wts_sids.items()):
    if len(sources) > 1:
        print(f"Shared STRING {sid}: {sources}")
