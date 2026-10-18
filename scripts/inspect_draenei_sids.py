# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
with open(ROOT / 'scripts/draenei_raw_dump.json', encoding='utf-8') as f:
    d = json.load(f)

print('=== UPGRADES IN DUMP ===')
for u in d['upgrades']:
    uid = u['id']
    lvls = u.get('levels', 1)
    sids = []
    for k, v in u.get('names', {}).items():
        if isinstance(v.get('raw'), str) and v['raw'].startswith('TRIGSTR_'):
            sids.append((k, int(v['raw'][8:])))
    for k, v in u.get('tips', {}).items():
        if isinstance(v.get('raw'), str) and v['raw'].startswith('TRIGSTR_'):
            sids.append((k, int(v['raw'][8:])))
    for k, v in u.get('ubertips', {}).items():
        if isinstance(v.get('raw'), str) and v['raw'].startswith('TRIGSTR_'):
            sids.append((k, int(v['raw'][8:])))
    print(f"{uid} (lvls={lvls}): total_sids={len(sids)} -> {sids}")

print('\n=== ABILITIES IN DUMP ===')
for a in d['abilities']:
    aid = a['id']
    lvls = a.get('levels', 1)
    sids = []
    if isinstance(a.get('raw_name'), str) and a['raw_name'].startswith('TRIGSTR_'):
        sids.append(('name', int(a['raw_name'][8:])))
    if isinstance(a.get('raw_researchtip'), str) and a['raw_researchtip'].startswith('TRIGSTR_'):
        sids.append(('researchtip', int(a['raw_researchtip'][8:])))
    if isinstance(a.get('raw_researchubertip'), str) and a['raw_researchubertip'].startswith('TRIGSTR_'):
        sids.append(('researchubertip', int(a['raw_researchubertip'][8:])))
    for k, v in a.get('tips', {}).items():
        if isinstance(v.get('raw'), str) and v['raw'].startswith('TRIGSTR_'):
            sids.append((k, int(v['raw'][8:])))
    for k, v in a.get('ubertips', {}).items():
        if isinstance(v.get('raw'), str) and v['raw'].startswith('TRIGSTR_'):
            sids.append((k, int(v['raw'][8:])))
    print(f"{aid} (lvls={lvls}) {a.get('name')}: total_sids={len(sids)} -> {sids}")
