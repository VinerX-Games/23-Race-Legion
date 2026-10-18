# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

hero_abils = {
    "H0BD (Спецназовец)": ["A0D8", "A0D7", "AEar", "A0D5"],
    "Galh (Алхимик)": ["ANhs", "ANab", "ANcr", "ANtm"],
    "Gmex (Механик)": ["ANsy", "ANcs", "ANeg", "ANrg"],
    "N018 (Шеф Кабестана)": ["A0DR", "A1KK", "A0DL", "A0DK"],
    "N019 (Мастер осады)": ["A0DU", "A1N0", "A1N3", "A1N1", "A1N4"],
    "N01A (Торговый Принц)": ["A0E2", "A0E1", "A0E0", "A13G"],
}

for h, ab_list in hero_abils.items():
    print(f"=== {h} ===")
    for ab in ab_list:
        res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "ability", "--id", ab])
        if res.get("ok"):
            f = res.get("object", {}) or res.get("fields", {})
            name = hw.clean_wc3_string(resolve(f.get("name")))
            tip = hw.clean_wc3_string(resolve(f.get("tip1") or f.get("researchtip") or ""))
            ub = hw.clean_wc3_string(resolve(f.get("ubertip1") or f.get("researchubertip") or ""))
            print(f"  [{ab}] {name} -> {ub[:80]}...")
        else:
            print(f"  [{ab}] NOT FOUND")
