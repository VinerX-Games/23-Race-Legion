# -*- coding: utf-8 -*-
import json
data = json.load(open('scripts/silitids_upgrades_check.json', encoding='utf-8'))
for uid, d in data.items():
    name = list(d['names'].values())[0]['val']
    tip = list(d['tips'].values())[0]['val']
    ub = list(d['ubertips'].values())[0]['val']
    print(f"[{uid}] lvl={d['levels']} | {name} | {tip}")
    print(f"       ub: {ub[:100]}...")
