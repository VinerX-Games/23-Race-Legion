# -*- coding: utf-8 -*-
"""Update Demon race selection ability A0MY with complete SD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw

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
        38885: "|cffe4cfa3Пылающий Легион|r",
        38886: "|cffe4cfa3Пылающий Легион|r (|cffffffffZ|r)",
        35179: "|cffa6afb8РАСА:|cffced4da Бесчисленная армия демонов и владык Скверны.|r|n|n|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8●●|r|n|cffa6afb8Период:|r |cffa9c7de«Легион»|r|n|n|cffced4daПылающий Легион — колоссальная армия демонов, инферналов и развращённых народов, стремящаяся искоренить саму жизнь и уничтожить порядок во Вселенной. Легион неоднократно вторгался в Азерот, неся разрушение и оставляя неизгладимые шрамы: скверна демонов породила Орду, привела к созданию Плети и спровоцировала череду опустошительных войн. Лишь ценой невероятных жертв защитникам мира удавалось сдерживать натиск воинства Саргераса.|r"
    }

    print(f"Applying {len(wts_updates)} WTS updates for Demon selection...")
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

    # Verify A0MY in SD
    checks = []
    args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", "ability", "--id", "A0MY"]
    res = hw.run_cli_json(args)
    if not res.get("ok"):
        raise RuntimeError(f"Failed to read A0MY via HiveWE: {res}")
    fields = res.get("object", {}) or res.get("fields", {})
    actual_name = resolve(fields.get("name"))
    actual_tip = resolve(fields.get("tip1"))
    actual_ubertip = resolve(fields.get("ubertip1"))

    name_ok = (actual_name == wts_updates[38885])
    tip_ok = (actual_tip == wts_updates[38886])
    ubertip_ok = (actual_ubertip == wts_updates[35179])

    checks.append({"field": "name", "expected": wts_updates[38885], "actual": actual_name, "ok": name_ok})
    checks.append({"field": "tip1", "expected": wts_updates[38886], "actual": actual_tip, "ok": tip_ok})
    checks.append({"field": "ubertip1", "expected": wts_updates[35179], "actual": actual_ubertip, "ok": ubertip_ok})

    all_ok = all(c["ok"] for c in checks)
    print("Verification checks:")
    for c in checks:
        print(f"  {c['field']}: {'OK' if c['ok'] else 'MISMATCH'}")

    apply_payload = {
        "race": "Demons",
        "ability": "A0MY",
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

    with open(folder / "demon_selection_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Пылающий Легион (Demon): подсказка выбора расы A0MY",
        "object": "A0MY",
        "variants": ["SD"],
        "hotkey": {
            "reference": "TRIGSTR_16598",
            "value": "Z"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua:476: InitTrig_Race_Demon_O фильтрует A0MY; выбор создаёт 8 e02Y и исследует R0AO.",
            "A0MY находится на стартовой панели выбора рас, клавиша Z (TRIGSTR_16598).",
            "Создатель Escanor (Яхве), сложность 3/5 (Средняя), период «Легион» и клавиша Z сохранены."
        ],
        "strings": [
            {"field": "name", "wts_id": 38885, "after": wts_updates[38885]},
            {"field": "tip1", "wts_id": 38886, "after": wts_updates[38886]},
            {"field": "ubertip1", "wts_id": 35179, "after": wts_updates[35179]}
        ]
    }

    with open(folder / "demon_selection.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
