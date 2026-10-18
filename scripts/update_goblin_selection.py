# -*- coding: utf-8 -*-
"""Update Goblin race selection ability A0AC with complete SD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)
    wts_path = ROOT / "map.w3x/war3map.wts"

    original_hashes = {
        "wts": hashlib.sha256(wts_path.read_bytes()).hexdigest(),
        "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest(),
        "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
        "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
        "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
    }

    wts_updates = {
        38861: "|cffe4cfa3Гоблины|r",
        38862: "|cffe4cfa3Гоблины|r (|cffffffffW|r)",
        35189: "|cffa6afb8РАСА:|cffced4da Предприимчивые изобретатели, алхимики и торговцы картелей.|r|n|n|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n|cffa6afb8Сложность:|r |cffffffff●●●●|cffa6afb8●|r|n|cffa6afb8Период:|r |cffa9c7de«Катаклизм»|r|n|n|cffced4daГоблины — одна из самых гротескных и предприимчивых рас Азерота. Искусные инженеры, алхимики и аферисты, гоблины всегда ищут максимальную выгоду, делая ставку на передовые технологии, разрушительную пиротехнику и тотальную коммерциализацию войны.|r"
    }

    print(f"Applying {len(wts_updates)} WTS updates for Goblin selection...")
    wts_content = wts_path.read_text(encoding="utf-8")
    for sid, new_val in sorted(wts_updates.items()):
        wts_content = update_wts_string(wts_content, sid, new_val)

    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print("WTS updated successfully.")

    # Reset HiveWE cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Verify A0AC in SD
    checks = []
    args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", "ability", "--id", "A0AC"]
    res = hw.run_cli_json(args)
    if not res.get("ok"):
        raise RuntimeError(f"Failed to read A0AC via HiveWE: {res}")
    fields = res.get("object", {}) or res.get("fields", {})
    actual_name = resolve(fields.get("name"))
    actual_tip = resolve(fields.get("tip1"))
    actual_ubertip = resolve(fields.get("ubertip1"))

    name_ok = (actual_name == wts_updates[38861])
    tip_ok = (actual_tip == wts_updates[38862])
    ubertip_ok = (actual_ubertip == wts_updates[35189])

    checks.append({"field": "name", "expected": wts_updates[38861], "actual": actual_name, "ok": name_ok})
    checks.append({"field": "tip1", "expected": wts_updates[38862], "actual": actual_tip, "ok": tip_ok})
    checks.append({"field": "ubertip1", "expected": wts_updates[35189], "actual": actual_ubertip, "ok": ubertip_ok})

    all_ok = all(c["ok"] for c in checks)
    print("Verification checks:")
    for c in checks:
        print(f"  {c['field']}: {'OK' if c['ok'] else 'MISMATCH'}")

    apply_payload = {
        "race": "Goblins",
        "ability": "A0AC",
        "wts_updated": list(wts_updates.keys()),
        "hashes_before": original_hashes,
        "hashes_after": {
            "wts": new_wts_hash,
            "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
            "w3u_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest(),
            "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
            "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
            "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
            "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
            "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
            "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
        },
        "binary_files_unchanged": (
            original_hashes["w3u"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest() and
            original_hashes["w3u_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest() and
            original_hashes["w3a"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest() and
            original_hashes["w3a_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest() and
            original_hashes["w3h"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest() and
            original_hashes["w3h_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest() and
            original_hashes["w3q"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest() and
            original_hashes["w3q_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest()
        ),
        "checks": checks,
        "all_checks_passed": all_ok
    }

    with open(folder / "goblins_selection_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Гоблины (Goblins): подсказка выбора расы A0AC",
        "object": "A0AC",
        "variants": ["SD"],
        "hotkey": {
            "reference": "TRIGSTR_13572",
            "value": "W"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua:457: InitTrig_Race_Goblins_O фильтрует A0AC; выбор создаёт 5 n00V, исследует R07E, R0J3 и запускает Trig_GoblinsOn_Actions().",
            "A0AC находится на стартовой панели выбора рас, клавиша W (TRIGSTR_13572).",
            "Создатель VinerX, сложность 4/5 (Высокая), период «Катаклизм» и клавиша W сохранены."
        ],
        "strings": [
            {"field": "name", "wts_id": 38861, "after": wts_updates[38861]},
            {"field": "tip1", "wts_id": 38862, "after": wts_updates[38862]},
            {"field": "ubertip1", "wts_id": 35189, "after": wts_updates[35189]}
        ]
    }

    with open(folder / "goblins_selection.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
