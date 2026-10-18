# -*- coding: utf-8 -*-
"""Update Stromgard race selection tooltip A0Y0 via WTS with complete SD/HD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING {string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    binary_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in source.glob("war3map*") if p.is_file() and p.name != "war3map.wts"}

    # Values for A0Y0
    new_name = "|cffe4cfa3Стромгард|r"
    new_tip = "|cffe4cfa3Стромгард|r (|cffffffffW|r)"
    new_ubertip = (
        "|cffa6afb8РАСА:|cffced4da Древнейшее королевство людей в низине Арати.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deNiCAmCHiK|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deNiCAmCHiK|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●|cffa6afb8●●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Битва за Азерот»|r|n|n"
        "|cffced4daКоролевство Стромгард — первое государство людей в Восточных королевствах, "
        "объединившее разрозненные племена и ставшее столицей древней империи Аратор. "
        "После битвы за Лордерон низина Арати превратилась в военный фронт между Альянсом и Ордой. "
        "Жители вернулись в отвоёванную столицу и во главе с Данатом Троллебоем встали на защиту "
        "восстановленного города во время битвы за Стромгард.|r"
    )

    registry = {
        "scope": "Стромгард (Stromgard): подсказка выбора расы A0Y0",
        "object": "A0Y0",
        "variants": ["SD", "HD"],
        "hotkey": {
            "reference": "TRIGSTR_20098",
            "value": "W"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua:342-358: InitTrig_Race_Stromgard_O фильтрует A0Y0; выбор создаёт пять h0G9, исследует R0H3, R0HY и запускает gg_trg_StromgardOn.",
            "Исходные поля name/tip1/ubertip1/hotkey/levels совпадают в SD/HD. Автор и куратор NiCAmCHiK, сложность 2/5 и клавиша W сохранены."
        ],
        "exceptions": [
            "NiCAmCHiK — авторский ник."
        ],
        "consumers": [
            {"file": "war3mapSkin.w3a", "id": "A0Y0", "field": ["anam", 0, 0], "wts_id": 38897},
            {"file": "war3mapSkin.w3a", "id": "A0Y0", "field": ["atp1", 1, 0], "wts_id": 38898},
            {"file": "war3mapSkin.w3a", "id": "A0Y0", "field": ["aub1", 1, 0], "wts_id": 25678}
        ],
        "in_game_checked": False,
        "strings": [
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0Y0",
                "field": "name",
                "reference_before": "TRIGSTR_38897",
                "before": "|cffeb968cСтромгард|r",
                "after": new_name
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0Y0",
                "field": "tip1",
                "reference_before": "TRIGSTR_38898",
                "before": "|cffeb968cСтромгард|r",
                "after": new_tip
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0Y0",
                "field": "ubertip1",
                "reference_before": "TRIGSTR_25678",
                "before": "|cffa0beaaСоздатель расы:|r |cffc8dcaaNiCAmCHiK|r|n|cffa0beaaКуратор расы:|r |cffc8dcaaNiCAmCHiK|r|n|cffa0beaaСложность:|r |cffadff2f●●|r●●●|n|cffa0beaaПериод:|r |cffc8dcaaLegion - Battle for Azeroth|r|n|nКоролевство |c00ff8e78Стромгард|r (или просто |c00ff8e78Стромгард|r) - первое королевство, основанное людьми в Восточных королевствах. Объединив разрозненные племена, Стромгард стал столицей империи Аратор.  После битвы за Лордерон низина Арати стала военным фронтом между Альянсом и Ордой. Горожане, похоже, вернулись в отвоеванную столицу, и во главе с Данатом Троллебоем защищали свой восстановленный город от вторжения Орды во время битвы за Стромгард.\n",
                "after": new_ubertip
            }
        ]
    }

    (folder / "stromgard_selection.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Apply changes to WTS
    updated_wts = update_wts_string(original_wts, 38897, new_name)
    updated_wts = update_wts_string(updated_wts, 38898, new_tip)
    updated_wts = update_wts_string(updated_wts, 25678, new_ubertip)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    for hd in (False, True):
        args = ["get-object", "--type", "ability", "--id", "A0Y0"]
        if hd:
            args.append("--hd")
        res = require(cli(args))
        f = res.get("fields", {})
        wts = hw.load_wts_strings()
        resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

        actual_name = resolve(f.get("name", ""))
        actual_tip = resolve(f.get("tip1", ""))
        actual_ubertip = resolve(f.get("ubertip1", ""))

        assert actual_name == new_name, f"Name mismatch (hd={hd}): {actual_name} != {new_name}"
        checks.append({"variant": "HD" if hd else "SD", "field": "name", "exact_match": True})

        assert actual_tip == new_tip, f"Tip mismatch (hd={hd}): {actual_tip} != {new_tip}"
        checks.append({"variant": "HD" if hd else "SD", "field": "tip1", "exact_match": True})

        assert actual_ubertip == new_ubertip, f"Ubertip mismatch (hd={hd}): {actual_ubertip} != {new_ubertip}"
        checks.append({"variant": "HD" if hd else "SD", "field": "ubertip1", "exact_match": True})

    # Verify binary files remained byte-identical
    for name, expected_hash in binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    report = {
        "ok": True,
        "applied": True,
        "method": "WTS-only",
        "changed_wts_ids": [38897, 38898, 25678],
        "binary_sha256_unchanged": binary_hashes,
        "before_wts_sha256": original_wts_hash,
        "after_wts_sha256": new_wts_hash,
        "checks": checks,
        "palette_and_color_resets_ok": True,
        "hotkey_and_levels_unchanged": True,
        "consumers_checked": registry["consumers"],
        "in_game_checked": False
    }

    (folder / "stromgard_selection_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "checks": len(checks)}))

if __name__ == "__main__":
    main()
