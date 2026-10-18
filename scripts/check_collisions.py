# -*- coding: utf-8 -*-
import json
from pathlib import Path

colls = {3002, 5542, 6926, 10901, 10902, 10916, 10918, 22662, 5595, 5596, 27305, 2888, 3692, 10064, 10976, 12857, 12886, 20630, 20631, 26476, 26477, 26484, 27193, 27969, 27970, 38201, 38229}

for race in ['felork', 'foresttrolls', 'cult', 'pandarens', 'hordew2']:
    p = Path(f'scripts/{race}_raw_dump.json')
    if not p.exists(): continue
    dump = json.loads(p.read_text(encoding='utf-8'))
    for cat in ['buildings', 'units', 'heroes', 'upgrades', 'abilities']:
        for item in dump.get(cat, []):
            iid = item.get('id')
            for k, v in item.items():
                if isinstance(v, dict):
                    for subk, subv in v.items():
                        if isinstance(subv, dict) and subv.get('sid') in colls:
                            print(f'[{race}] {cat} {iid}.{k}.{subk} uses SID {subv.get("sid")}')
                elif k.endswith('_sid') and v in colls:
                    print(f'[{race}] {cat} {iid}.{k} uses SID {v}')
