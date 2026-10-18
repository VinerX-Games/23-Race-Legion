# -*- coding: utf-8 -*-
"""Inspect and dump all details for Race 12: Scarlet Crusade (Алый Орден).
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def resolve_str(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        sid = int(s[8:])
        return {"sid": sid, "trigstr": s, "val": wts.get(sid, "")}
    elif isinstance(s, str):
        return {"sid": None, "trigstr": None, "val": s}
    return {"sid": None, "trigstr": None, "val": str(s) if s is not None else ""}

buildings = [
    'h05U', 'h05V', 'h05W', 'h05X', 'h05Y', 'h05Z', 'h060', 'h061',
    'h062', 'h063', 'h064', 'h068'
]

heroes = ['H03H', 'H06C', 'H06B']

units = [
    'h014', 'h039', 'h03A', 'h03B', 'h03C', 'h03D', 'h03F', 'h03G',
    'h03I', 'h065', 'h066', 'h067', 'n007', 'n008', 'o00I'
]

hero_abils = [
    'A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M',
    'A09G', 'A09F', 'A09I', 'A09J'
]

unit_abils = [
    'A09O', 'A081', 'A080', 'A07Z', 'A07X', 'A0OY', 'A08E', 'A08D',
    'A085', 'A08Y', 'A08X', 'A08P', 'A08O', 'A08F', 'A08G', 'A07I',
    'A08K', 'A083', 'A08J', 'A08L', 'A08M', 'A084', 'A08N', 'A082',
    'A08C', 'A088', 'A089', 'A07Y', 'A087', 'A08B', 'A08A', 'ANha', 'Ahrp'
]

upgrades = [
    'R040', 'R03Z', 'R03W', 'R03V', 'R03K', 'R03L', 'R03M', 'R048',
    'R049', 'R04A', 'R04B', 'R04C', 'R03X', 'R03Y', 'R0KG', 'R0KH',
    'R047', 'R046', 'R045', 'R03S', 'R03T', 'R044', 'R043', 'R042',
    'R041', 'R07B', 'R03U'
]

details = {
    "selection": {},
    "buildings": {},
    "heroes": {},
    "units": {},
    "abilities": {},
    "upgrades": {}
}

# Selection spell
res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', 'A0HM'])
f = res.get('object', {}) or res.get('fields', {})
details["selection"] = {
    "id": "A0HM",
    "fields": f,
    "name": resolve_str(f.get("name")),
    "tip1": resolve_str(f.get("tip1")),
    "ubertip1": resolve_str(f.get("ubertip1")),
    "hotkey": resolve_str(f.get("hotkey")),
}

# Buildings
for bid in buildings:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', bid])
    f = res.get('object', {}) or res.get('fields', {})
    details["buildings"][bid] = {
        "id": bid,
        "fields": f,
        "name": resolve_str(f.get("name")),
        "tip": resolve_str(f.get("tip")),
        "ubertip": resolve_str(f.get("ubertip")),
        "hotkey": resolve_str(f.get("hotkey")),
        "trains": f.get("trains"),
        "researches": f.get("researches"),
        "upgrade": f.get("upgrade"),
        "upgrades": f.get("upgrades"),
        "abillist": f.get("abillist"),
        "targs1": f.get("targs1"),
        "weaptype1": f.get("weaptype1")
    }

# Heroes
for hid in heroes:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', hid])
    f = res.get('object', {}) or res.get('fields', {})
    details["heroes"][hid] = {
        "id": hid,
        "fields": f,
        "name": resolve_str(f.get("name")),
        "propernames": resolve_str(f.get("propernames")),
        "tip": resolve_str(f.get("tip")),
        "ubertip": resolve_str(f.get("ubertip")),
        "hotkey": resolve_str(f.get("hotkey")),
        "heroabils": f.get("heroabils") or f.get("heroabillist"),
        "abillist": f.get("abillist"),
        "targs1": f.get("targs1"),
        "weaptype1": f.get("weaptype1")
    }

# Units
for uid in units:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    details["units"][uid] = {
        "id": uid,
        "fields": f,
        "name": resolve_str(f.get("name")),
        "tip": resolve_str(f.get("tip")),
        "ubertip": resolve_str(f.get("ubertip")),
        "hotkey": resolve_str(f.get("hotkey")),
        "abillist": f.get("abillist"),
        "targs1": f.get("targs1"),
        "weaptype1": f.get("weaptype1"),
        "builds": f.get("builds")
    }

# Abilities
all_abils = sorted(set(hero_abils) | set(unit_abils))
for aid in all_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    abil_entry = {
        "id": aid,
        "fields": f,
        "name": resolve_str(f.get("name")),
        "levels": f.get("levels", 1),
        "tips": {},
        "ubertips": {},
        "hotkeys": {},
        "untips": {},
        "unubertips": {},
        "unhotkeys": {}
    }
    levels = int(f.get("levels", 1) or 1)
    for lvl in range(1, max(levels, 4) + 1):
        for prefix in ["tip", "ubertip", "hotkey", "untip", "unubertip", "unhotkey"]:
            key = f"{prefix}{lvl}" if lvl > 1 or prefix in ["untip", "unubertip", "unhotkey"] else prefix
            val = f.get(f"{prefix}{lvl}") or (f.get(prefix) if lvl == 1 else None)
            if val is not None:
                target_dict = abil_entry[f"{prefix}s"] if f"{prefix}s" in abil_entry else None
                if target_dict is not None:
                    target_dict[lvl] = resolve_str(val)
    details["abilities"][aid] = abil_entry

# Upgrades
for upg in sorted(set(upgrades)):
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', upg])
    f = res.get('object', {}) or res.get('fields', {})
    upg_entry = {
        "id": upg,
        "fields": f,
        "name": resolve_str(f.get("name1") or f.get("name")),
        "levels": f.get("levels", 1),
        "names": {},
        "tips": {},
        "ubertips": {},
        "hotkeys": {}
    }
    levels = int(f.get("levels", 1) or 1)
    for lvl in range(1, max(levels, 6) + 1):
        for field in ["name", "tip", "ubertip", "hotkey"]:
            key = f"{field}{lvl}" if lvl > 1 else field
            val = f.get(f"{field}{lvl}") or (f.get(field) if lvl == 1 else None)
            if val is not None:
                upg_entry[f"{field}s"][lvl] = resolve_str(val)
    details["upgrades"][upg] = upg_entry

out_file = ROOT / "scripts/scarlet_complete_inventory.json"
out_file.write_text(json.dumps(details, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Complete inventory saved to {out_file}")
