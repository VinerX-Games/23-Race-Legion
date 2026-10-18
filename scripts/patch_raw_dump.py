# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
p = ROOT / "scripts/hordew2_raw_dump.json"
d = json.loads(p.read_text(encoding="utf-8"))

bld_ub_map = {
    "w20q": "TRIGSTR_29700",
    "w20r": "TRIGSTR_29730",
    "w20y": "TRIGSTR_29732",
    "w214": "TRIGSTR_29960",
    "w20a": "TRIGSTR_29734",
    "w20u": "TRIGSTR_29733",
    "w20t": "TRIGSTR_29731",
    "w20i": "TRIGSTR_29961",
    "w210": "TRIGSTR_29740",
    "w218": "TRIGSTR_28309",
    "w219": "TRIGSTR_22678"
}

unit_ub_map = {
    "w200": "TRIGSTR_29074",
    "w208": "TRIGSTR_29535",
    "w203": "TRIGSTR_29276",
    "w204": "TRIGSTR_29277",
    "w209": "TRIGSTR_29662",
    "w211": "TRIGSTR_29836",
    "w205": "TRIGSTR_29278",
    "w207": "TRIGSTR_29473",
    "w201": "TRIGSTR_29220",
    "w206": "TRIGSTR_29454",
    "w202": "TRIGSTR_29275",
    "h0D6": "TRIGSTR_5542",
    "h0D5": "TRIGSTR_6926",
    "w220": "TRIGSTR_36997"
}

hero_ub_map = {
    "W200": "TRIGSTR_29891",
    "W201": "TRIGSTR_29958",
    "W202": "TRIGSTR_29959"
}

for b in d.get("buildings", []):
    if b["id"] in bld_ub_map:
        b["raw_ubertip"] = bld_ub_map[b["id"]]

for u in d.get("units", []):
    if u["id"] in unit_ub_map:
        u["raw_ubertip"] = unit_ub_map[u["id"]]

for h in d.get("heroes", []):
    if h["id"] in hero_ub_map:
        h["raw_ubertip"] = hero_ub_map[h["id"]]

p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated hordew2_raw_dump.json with raw_ubertip mappings.")
