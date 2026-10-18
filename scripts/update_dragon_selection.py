# -*- coding: utf-8 -*-
"""Update Dragons race selection tooltip A0RQ via WTS with complete SD/HD validation."""
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

    # Values for A0RQ
    new_name = "|cffe4cfa3Аспекты Драконов|r"
    new_tip = "|cffe4cfa3Аспекты Драконов|r (|cffffffffA|r)"
    new_ubertip = (
        "|cffa6afb8РАСА:|cffced4da Великие стаи драконов, хранителей Азерота.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Катаклизм»|r|n|n"
        "|cffced4daАспекты Драконов — предводители пяти великих стай, наделённые титанами силой "
        "для защиты Азерота. Каждый титан передал часть своего могущества одному из владык, "
        "вверив им заботу о жизни, магии, времени, изумрудном сне и земных недрах. "
        "Объединив могущество стай, драконы стоят на страже спокойствия мира.|r"
    )

    registry = {
        "scope": "Драконы (Dragon): подсказка выбора расы A0RQ",
        "object": "A0RQ",
        "variants": ["SD", "HD"],
        "hotkey": {
            "reference": "TRIGSTR_4263",
            "value": "A"
        },
        "levels": 1,
        "evidence": [
            "04_race_selection.lua:363-381: InitTrig_Race_Dragon_O фильтрует A0RQ; выбор создаёт одну dra1, исследует R0BY и запускает DragonsOn().",
            "04_race_selection.lua:1066-1071: случайный выбор расы также создаёт dra1, исследует R0BY и активирует триггеры DragonsOn().",
            "Исходные поля name/tip1/ubertip1/hotkey/levels совпадают в SD/HD. Автор Escanor (Яхве), сложность 3/5 (Средняя), период «Катаклизм» и клавиша A сохранены."
        ],
        "exceptions": [
            "Escanor (Яхве) — авторский ник."
        ],
        "consumers": [
            {"file": "war3mapSkin.w3a", "id": "A0RQ", "field": ["anam", 0, 0], "wts_id": 38893},
            {"file": "war3mapSkin.w3a", "id": "A0RQ", "field": ["atp1", 1, 0], "wts_id": 38894},
            {"file": "war3mapSkin.w3a", "id": "A0RQ", "field": ["aub1", 1, 0], "wts_id": 35183},
            {"file": "war3map.w3a", "id": "A0RQ", "field": ["anam", 0, 0], "wts_id": 38893},
            {"file": "war3map.w3a", "id": "A0RQ", "field": ["atp1", 1, 0], "wts_id": 38894},
            {"file": "war3map.w3a", "id": "A0RQ", "field": ["aub1", 1, 0], "wts_id": 35183}
        ],
        "in_game_checked": False,
        "strings": [
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0RQ",
                "field": "name",
                "reference_before": "TRIGSTR_38893",
                "before": "|cffc8dc8cАспекты Драконов|r",
                "after": new_name
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0RQ",
                "field": "tip1",
                "reference_before": "TRIGSTR_38894",
                "before": "|cffc8dc8cАспекты Драконов|r",
                "after": new_tip
            },
            {
                "source": "map.w3x/war3map.wts",
                "rawcode": "A0RQ",
                "field": "ubertip1",
                "reference_before": "TRIGSTR_35183",
                "before": "|cff7dc87dСоздатель расы:|r |cffe17d00Escanor (Яхве)|r|n|cff7dc87dСложность:|r |cffffbe37Средняя|r|n|cff7dc87dПериод:|r |cffff5e19Cataclysm|r|n|cff7dc87dОписание: |r|cff8080ffАспекты Драконов|r - лидеры пяти кланов драконов. Аспектами стали пять драконов, наделенные огромной силой для защиты Азерота, чтобы ничто не угрожало спокойствию этого мира. Каждый титан дал часть своей силы одному из драконов, которые в последствии и стали Аспектами. Дав Могущественную Силу Аспектам, Титаны ушли из сотворенного ими мира.",
                "after": new_ubertip
            }
        ]
    }

    (folder / "dragon_selection.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Apply changes to WTS
    updated_wts = update_wts_string(original_wts, 38893, new_name)
    updated_wts = update_wts_string(updated_wts, 38894, new_tip)
    updated_wts = update_wts_string(updated_wts, 35183, new_ubertip)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    for hd in (False, True):
        args = ["get-object", "--type", "ability", "--id", "A0RQ"]
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
        "changed_wts_ids": [38893, 38894, 35183],
        "binary_sha256_unchanged": binary_hashes,
        "before_wts_sha256": original_wts_hash,
        "after_wts_sha256": new_wts_hash,
        "checks": checks,
        "palette_and_color_resets_ok": True,
        "hotkey_and_levels_unchanged": True,
        "consumers_checked": registry["consumers"],
        "in_game_checked": False
    }

    (folder / "dragon_selection_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "checks": len(checks)}))

if __name__ == "__main__":
    main()
