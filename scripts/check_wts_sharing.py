# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

data = json.load(open('scripts/illidari_wts_mapping.json', encoding='utf-8'))
illidari_sids = set()

for cat, objs in data.items():
    for oid, finfo in objs.items():
        for fld, val in finfo.items():
            if isinstance(val, list) and len(val) == 2 and isinstance(val[0], int):
                illidari_sids.add(val[0])

print(f"Illidari total unique WTS strings: {len(illidari_sids)}")

# Check against all binary files
binary_files = [
    "war3map.w3u", "war3mapSkin.w3u",
    "war3map.w3a", "war3mapSkin.w3a",
    "war3map.w3q", "war3mapSkin.w3q",
    "war3map.w3h", "war3mapSkin.w3h",
    "war3map.w3t", "war3mapSkin.w3t",
    "war3map.w3b", "war3mapSkin.w3b",
    "war3map.w3d", "war3mapSkin.w3d"
]

all_binary_text = ""
for bf in binary_files:
    p = Path(f"map.w3x/{bf}")
    if p.exists():
        raw = p.read_bytes()
        # find all TRIGSTR_XXXX
        matches = re.findall(rb"TRIGSTR_(\d+)", raw)
        for m in matches:
            all_binary_text += f"{bf}:{int(m.decode('ascii'))}\n"

# Check Lua triggers
lua_text = ""
for lf in Path("map.w3x/_lua").glob("**/*.lua"):
    raw = lf.read_text(encoding="utf-8", errors="replace")
    matches = re.findall(r"TRIGSTR_(\d+)", raw)
    for m in matches:
        lua_text += f"{lf.name}:{int(m)}\n"

print("Done scanning.")
