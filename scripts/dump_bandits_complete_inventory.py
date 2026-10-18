# -*- coding: utf-8 -*-
"""Comprehensive dump of all Bandits race objects, fields, and WTS string references."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

inventory = {
    "selection": "A0HR",
    "buildings": [
        'h007', 'h008', 'h009', 'h00A', 'h00B', 'h00O', 'h01V', 'h01W',
        'h03O', 'h03P', 'h03Q', 'h03R', 'h051', 'h07G', 'h0DF', 'h0DG', 'h0DH'
    ],
    "heroes": ['H03S', 'H047', 'H048'],
    "units": [
        'h002', 'h003', 'h005', 'h006', 'h00P', 'h00Q', 'h00S', 'h00U',
        'h029', 'h02A', 'h02B', 'h02Q', 'h02R', 'h02S', 'h02T', 'h02U',
        'h03K', 'h03L', 'h03N', 'n000', 'n002', 'n004', 'o00C'
    ],
    "hero_abils": [
        'A01J', 'A01D', 'A01H', 'A01I', 'A023', 'ANrf', 'AHab', 'ANlm',
        'A0WV', 'A026', 'A028', 'A029', 'Aamk'
    ],
    "unit_abils": [
        'A00M', 'A000', 'A00L', 'A01A', 'A00P', 'A01B', 'A013', 'A00J',
        'A00N', 'A016', 'A017', 'A169', 'A00X', 'A00V', 'A00K', 'A165',
        'A00R', 'A19T', 'A00U', 'Aspo', 'A00S', 'A00T', 'A012', 'A00Z',
        'A00Y', 'ACbh', 'Ashm', 'A17Q', 'A011', 'A010', 'Abof', 'Afbt'
    ],
    "upgrades": [
        'R00J', 'R00L', 'R00M', 'R00V', 'R00U', 'R00X', 'R00K', 'R00N',
        'R00W', 'R0HP', 'R00Y', 'R00G', 'R00D', 'R00A', 'R00B', 'R00E',
        'R00F', 'R00C', 'R00I', 'R0BS'
    ],
    "fleet_upgrades": ['R005', 'R006', 'R007', 'R002', 'R003']
}

out_data = {}

# 1. Selection
res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', 'A0HR'])
f = res.get('object', {}) or res.get('fields', {})
out_data["selection"] = {
    "id": "A0HR",
    "name": f.get("name"),
    "name_val": resolve(f.get("name")),
    "tip1": f.get("tip1"),
    "tip1_val": resolve(f.get("tip1")),
    "ubertip1": f.get("ubertip1"),
    "ubertip1_val": resolve(f.get("ubertip1")),
    "hotkey": f.get("hotkey"),
    "hotkey_val": resolve(f.get("hotkey")),
}

# 2. Buildings
out_data["buildings"] = {}
for bid in inventory["buildings"]:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', bid])
    f = res.get('object', {}) or res.get('fields', {})
    out_data["buildings"][bid] = {
        "id": bid,
        "name": f.get("name"),
        "name_val": resolve(f.get("name")),
        "tip": f.get("tip"),
        "tip_val": resolve(f.get("tip")),
        "ubertip": f.get("ubertip"),
        "ubertip_val": resolve(f.get("ubertip")),
        "hotkey": f.get("hotkey"),
        "hotkey_val": resolve(f.get("hotkey")),
        "trains": f.get("trains"),
        "researches": f.get("researches"),
        "upgrade": f.get("upgrade"),
        "upgrades": f.get("upgrades"),
        "abillist": f.get("abillist"),
        "targs1": f.get("targs1"),
        "weaptype1": f.get("weaptype1")
    }

# 3. Heroes
out_data["heroes"] = {}
for hid in inventory["heroes"]:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', hid])
    f = res.get('object', {}) or res.get('fields', {})
    out_data["heroes"][hid] = {
        "id": hid,
        "name": f.get("name"),
        "name_val": resolve(f.get("name")),
        "propernames": f.get("propernames"),
        "propernames_val": resolve(f.get("propernames")),
        "tip": f.get("tip"),
        "tip_val": resolve(f.get("tip")),
        "ubertip": f.get("ubertip"),
        "ubertip_val": resolve(f.get("ubertip")),
        "hotkey": f.get("hotkey"),
        "hotkey_val": resolve(f.get("hotkey")),
        "heroabils": f.get("heroabils") or f.get("heroabillist"),
        "targs1": f.get("targs1"),
        "weaptype1": f.get("weaptype1")
    }

# 4. Units
out_data["units"] = {}
for uid in inventory["units"]:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    out_data["units"][uid] = {
        "id": uid,
        "name": f.get("name"),
        "name_val": resolve(f.get("name")),
        "tip": f.get("tip"),
        "tip_val": resolve(f.get("tip")),
        "ubertip": f.get("ubertip"),
        "ubertip_val": resolve(f.get("ubertip")),
        "hotkey": f.get("hotkey"),
        "hotkey_val": resolve(f.get("hotkey")),
        "abillist": f.get("abillist"),
        "upgrades": f.get("upgrades"),
        "targs1": f.get("targs1"),
        "weaptype1": f.get("weaptype1")
    }

# 5. Hero Abils & Unit Abils
out_data["abils"] = {}
all_abils = sorted(set(inventory["hero_abils"] + inventory["unit_abils"]))
for aid in all_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    levels = int(f.get('levels') or 1)
    ab_dict = {
        "id": aid,
        "name": f.get("name"),
        "name_val": resolve(f.get("name")),
        "levels": levels,
        "hotkey": f.get("hotkey"),
        "hotkey_val": resolve(f.get("hotkey")),
        "researchhotkey": f.get("researchhotkey"),
        "researchhotkey_val": resolve(f.get("researchhotkey")),
        "researchtip": f.get("researchtip"),
        "researchtip_val": resolve(f.get("researchtip")),
        "researchubertip": f.get("researchubertip"),
        "researchubertip_val": resolve(f.get("researchubertip")),
        "tips": {},
        "ubertips": {}
    }
    for i in range(1, levels + 1):
        tk = f"tip{i}"
        uk = f"ubertip{i}"
        if f.get(tk):
            ab_dict["tips"][i] = {"raw": f.get(tk), "val": resolve(f.get(tk))}
        if f.get(uk):
            ab_dict["ubertips"][i] = {"raw": f.get(uk), "val": resolve(f.get(uk))}
    out_data["abils"][aid] = ab_dict

# 6. Upgrades
out_data["upgrades"] = {}
for uid in inventory["upgrades"]:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    # determine max levels from keys
    tips = [k for k in f if k.startswith('tip')]
    max_lvl = len(tips) if tips else int(f.get('levels') or 1)
    upg_dict = {
        "id": uid,
        "levels": max_lvl,
        "class": f.get("class"),
        "names": {},
        "tips": {},
        "ubertips": {},
        "hotkeys": {}
    }
    for i in range(1, max_lvl + 1):
        nk = f"name{i}" if f.get(f"name{i}") else "name"
        tk = f"tip{i}"
        uk = f"ubertip{i}"
        hk = f"hotkey{i}" if f.get(f"hotkey{i}") else "hotkey"
        if f.get(nk):
            upg_dict["names"][i] = {"raw": f.get(nk), "val": resolve(f.get(nk))}
        if f.get(tk):
            upg_dict["tips"][i] = {"raw": f.get(tk), "val": resolve(f.get(tk))}
        if f.get(uk):
            upg_dict["ubertips"][i] = {"raw": f.get(uk), "val": resolve(f.get(uk))}
        if f.get(hk):
            upg_dict["hotkeys"][i] = {"raw": f.get(hk), "val": resolve(f.get(hk))}
    out_data["upgrades"][uid] = upg_dict

out_file = ROOT / "scripts/bandits_complete_inventory.json"
out_file.write_text(json.dumps(out_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Dump complete! Written {len(out_data)} sections to {out_file}")
