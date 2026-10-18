# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw
from implement_draenei_rework import object_records

wts = hw.load_wts_strings()

def r(s):
    if isinstance(s, str) and s.startswith("TRIGSTR_"):
        return int(s[8:]), wts.get(int(s[8:]), s)
    return None, s

report = {
    "selection": {},
    "buildings": {},
    "units": {},
    "heroes": {},
    "upgrades": {},
    "abilities": {}
}

d1 = json.load(open("scripts/illidari_raw_dump.json", encoding="utf-8"))
d2 = json.load(open("scripts/illidari_abils_upgrades_dump.json", encoding="utf-8"))

# 1. Selection
sel = d1["selection"]
flds = sel.get("fields", {})
report["selection"]["A0OK"] = {
    "name": r(flds.get("name")),
    "tip1": r(flds.get("tip1")),
    "ubertip1": r(flds.get("ubertip1")),
    "hotkey": flds.get("hotkey")
}

# 2. Buildings & 3. Units & 4. Heroes from war3map.w3u
content_u = Path('map.w3x/war3map.w3u').read_bytes()
ver_u, tables_u = object_records(content_u, False)

all_unit_objs = {}
for table in tables_u:
    for rec in table:
        uid = rec['id']
        mods = {}
        for (tag, sub1, sub2), raw_val in rec['mods']:
            val_bytes = raw_val[8:-4] if len(raw_val) >= 12 else b""
            null_pos = val_bytes.find(b'\x00')
            if null_pos != -1:
                mods[tag] = val_bytes[:null_pos].decode('utf-8', errors='replace')
            else:
                mods[tag] = str(val_bytes)
        all_unit_objs[uid] = mods

b_ids = ["h0E9", "h0EA", "h0EB", "h0EC", "h0ED", "h0EE", "h0EF", "h0EG", "h0EH", "h0EM", "h0EN", "o01C", "h011"]
u_ids = ["h0EI", "h0EJ", "o01A", "o01B", "o019", "h0EK", "h0EL", "n02O", "n02M", "n02N", "h04Y", "h04Z", "h050"]
h_ids = ["H043", "E01W", "E024", "E025"]

for bid in b_ids:
    mods = all_unit_objs.get(bid, {})
    report["buildings"][bid] = {
        "name": r(mods.get("unam")),
        "tip": r(mods.get("utip")),
        "ubertip": r(mods.get("utub")),
        "hotkey": r(mods.get("uhot")),
        "raw_mods": mods
    }

for uid in u_ids:
    mods = all_unit_objs.get(uid, {})
    report["units"][uid] = {
        "name": r(mods.get("unam")),
        "tip": r(mods.get("utip")),
        "ubertip": r(mods.get("utub")),
        "hotkey": r(mods.get("uhot")),
        "uabi": mods.get("uabi"),
        "upgr": mods.get("upgr"),
        "raw_mods": mods
    }

for hid in h_ids:
    mods = all_unit_objs.get(hid, {})
    report["heroes"][hid] = {
        "name": r(mods.get("unam")),
        "propernames": r(mods.get("upro")),
        "tip": r(mods.get("utip")),
        "ubertip": r(mods.get("utub")),
        "awakentip": r(mods.get("uawt")),
        "revivetip": r(mods.get("utpr")),
        "hotkey": r(mods.get("uhot")),
        "uhab": mods.get("uhab"),
        "uabi": mods.get("uabi"),
        "raw_mods": mods
    }

# 5. Upgrades
for uid, upg in d2["upgrades"].items():
    report["upgrades"][uid] = {}
    flds = upg.get("fields", {})
    for k, v in flds.items():
        if isinstance(v, str) and v.startswith("TRIGSTR_"):
            sid, val = r(v)
            report["upgrades"][uid][k] = (sid, val)

# 6. Abilities
for aid, ab in d2["abils"].items():
    report["abilities"][aid] = {}
    flds = ab.get("fields", {})
    for k, v in flds.items():
        if isinstance(v, str) and v.startswith("TRIGSTR_"):
            sid, val = r(v)
            report["abilities"][aid][k] = (sid, val)

Path("scripts/illidari_wts_mapping.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved scripts/illidari_wts_mapping.json successfully.")
