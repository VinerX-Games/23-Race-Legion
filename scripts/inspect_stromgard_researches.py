# -*- coding: utf-8 -*-
"""Inspect Stromgard researches in war3map.w3q and war3mapSkin.w3q."""
import sys, json, struct
from pathlib import Path
sys.path.insert(0, "scripts")
from implement_draenei_rework import object_records
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        sid = int(val[8:])
        return wts.get(sid, val)
    return val

# All known or potential Stromgard research IDs
# Let's inspect all upgrades in war3map.w3q and war3mapSkin.w3q starting with R0D, R0H, etc.
raw = Path("map.w3x/war3map.w3q").read_bytes()
v, tables = object_records(raw, True) # upgrades are extended

raw_skin = Path("map.w3x/war3mapSkin.w3q").read_bytes()
v_skin, tables_skin = object_records(raw_skin, True)

researches = {}

def process_table(table, is_skin=False):
    for r in table:
        rid = r["id"]
        entry = researches.setdefault(rid, {"base": r["header"][4:8].decode("ascii", "replace").strip("\x00"), "mods": {}})
        for mod in r["mods"]:
            tag, lvl, data_ptr = mod[0]
            raw_b = mod[1]
            mtype = struct.unpack("<I", raw_b[4:8])[0]
            val = None
            if mtype == 0:
                val = struct.unpack("<i", raw_b[8:12])[0]
            elif mtype in (1, 2):
                val = round(struct.unpack("<f", raw_b[8:12])[0], 4)
            elif mtype == 3:
                val = res(raw_b[8:-4].decode("utf-8", "replace").strip("\x00"))
            entry["mods"][f"{tag}_{lvl}"] = val

for t in tables:
    process_table(t, False)
for t in tables_skin:
    process_table(t, True)

# Filter for Stromgard researches
# Let's see which ones have Stromgard in name, or base objects, or match R0D*
stromgard_res = {}
for rid, data in sorted(researches.items()):
    name = data["mods"].get("gnam_0") or data["mods"].get("gnam_1") or ""
    # Check if rid starts with R0D or contains relevant text
    if rid.startswith("R0D") or any(word in str(v).lower() for v in data["mods"].values() for word in ["стромгард", "пехотинец", "арбалетчик", "рыцарь", "жрец", "заклинатель", "порох"]):
        stromgard_res[rid] = data

with open("docs/ui_text/stromgard_researches_raw.json", "w", encoding="utf-8") as f:
    json.dump(stromgard_res, f, ensure_ascii=False, indent=2)

print(f"Found {len(stromgard_res)} potential Stromgard researches.")
for rid, d in stromgard_res.items():
    print(f"{rid} ({d['base']}): name={d['mods'].get('gnam_0') or d['mods'].get('gnam_1')}")
