# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

research_ids = [
    'R0D4', 'R007',
    'R04P', 'R04E', 'R04F', 'R04G', 'R04H', 'R04I', 'R04J', 'R04K', 'R04L', 'R04M',
    'R056', 'R07A', 'R05X', 'R05Y', 'R04N', 'R04Q', 'R04R', 'R053', 'R05W'
]

bulk = require(cli(['get-objects-bulk', '--type', 'upgrade', '--ids', ','.join(research_ids)]))
objects = {o['id']: o for o in bulk.get('objects', [])}

print(f"Loaded {len(objects)} research objects.\n")

report = {}
for rid in research_ids:
    obj = objects.get(rid)
    if not obj:
        print(f"[{rid}] MISSING!")
        continue
    f = obj.get('fields', {})
    code = f.get('code')
    name = resolve(f.get('name'))
    raw_name = f.get('name')
    lvls = int(f.get('levels', '1'))
    hotkey = f.get('hotkey')
    print(f"=== [{rid}] (code={code}, lvls={lvls}, hotkey={hotkey}) {name} (raw={raw_name}) ===")
    report[rid] = {
        "id": rid,
        "code": code,
        "levels": lvls,
        "hotkey": hotkey,
        "name_raw": raw_name,
        "name": name,
        "levels_info": []
    }
    for lvl in range(1, lvls + 1):
        tip_k = f"tip{lvl}"
        ub_k = f"ubertip{lvl}"
        tip_raw = f.get(tip_k)
        ub_raw = f.get(ub_k)
        tip_res = resolve(tip_raw)
        ub_res = resolve(ub_raw)
        print(f"  Level {lvl}:")
        print(f"    {tip_k}: {repr(tip_raw)} -> {repr(tip_res)}")
        print(f"    {ub_k}: {repr(ub_raw)} -> {repr(ub_res)}")
        report[rid]["levels_info"].append({
            "level": lvl,
            "tip_raw": tip_raw,
            "tip": tip_res,
            "ubertip_raw": ub_raw,
            "ubertip": ub_res
        })

Path(ROOT / "docs/ui_text/goblins_research_raw.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("\nSaved raw research data to docs/ui_text/goblins_research_raw.json")
