# -*- coding: utf-8 -*-
"""Inspect clear Russian text and details for all 24 Goblin units."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

raw_path = ROOT / "docs/ui_text/goblin_units_raw.json"
units = json.loads(raw_path.read_text(encoding="utf-8"))

clean_report = []

for uid, u in sorted(units.items()):
    if uid in ["h0G8", "h07A"]:
        continue
    name = resolve(u.get("name_raw"))
    tip = resolve(u.get("tip_raw"))
    ubertip = resolve(u.get("ubertip_raw"))
    hotkey = resolve(u.get("hotkey_raw"))
    
    # Abilities details
    abils_str = u.get("abillist") or ""
    abils_list = [a.strip() for a in abils_str.split(",") if a.strip()]
    abils_detail = []
    for ab in abils_list:
        res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "ability", "--id", ab])
        if res.get("ok"):
            af = res.get("object", {}) or res.get("fields", {})
            abils_detail.append(f"{ab}: {resolve(af.get('name'))}")
        else:
            abils_detail.append(f"{ab}: (unknown)")

    # Attack details
    atk1 = f"{u.get('mindmg1')}-{u.get('maxdmg1')} ({u.get('atktype1')}/{u.get('weaptp1')}, cool: {u.get('cool1')}, targs: {u.get('targs1')})" if u.get('mindmg1') != ' - ' and u.get('mindmg1') is not None else None
    atk2 = f"{u.get('mindmg2')}-{u.get('maxdmg2')} ({u.get('atktype2')}/{u.get('weaptp2')}, cool: {u.get('cool2')}, targs: {u.get('targs2')})" if u.get('mindmg2') != ' - ' and u.get('mindmg2') is not None else None

    item = {
        "id": uid,
        "name_clean": hw.clean_wc3_string(name),
        "hotkey": hotkey,
        "name_raw": u.get("name_raw"),
        "tip_raw": u.get("tip_raw"),
        "ubertip_raw": u.get("ubertip_raw"),
        "name_before": name,
        "tip_before": tip,
        "ubertip_before": ubertip,
        "abils": abils_detail,
        "atk1": atk1,
        "atk2": atk2
    }
    clean_report.append(item)

with open(ROOT / "docs/ui_text/goblin_units_clean.json", "w", encoding="utf-8") as out:
    json.dump(clean_report, out, ensure_ascii=False, indent=2)

print(f"Generated clean report for {len(clean_report)} units in docs/ui_text/goblin_units_clean.json")
