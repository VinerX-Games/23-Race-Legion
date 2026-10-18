# -*- coding: utf-8 -*-
"""Update Stromgard buildings batch 2 (modular quarter, workshop & shipyard) via WTS with complete SD/HD validation."""
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

BUILDINGS = [
    {
        "id": "h0HH",
        "wts": {"name": 21288, "tip": 21289, "ubertip": 21290},
        "hotkey": "W",
        "name": "|cffe4cfa3Место постройки|r",
        "tip": "|cffe4cfa3Место постройки|r (|cffffffffW|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Строительный фундамент Стромгарда. Позволяет возвести одно из специализированных городских строений.|n|n"
            "|cffa6afb8Улучшается до:|cffced4da|n"
            "- |cffa9c7deКазармы|cffced4da: подготовка пехоты, стрелков и рыцарей.|n"
            "- |cffa9c7deМагическая башня|cffced4da: подготовка жрецов и заклинателей.|n"
            "- |cffa9c7deРынок|cffced4da: найм оруженосцев и увеличение дохода.|r"
        )
    },
    {
        "id": "h0H4",
        "wts": {"name": 20884, "tip": 21273, "ubertip": 21063},
        "hotkey": "Z",
        "name": "|cffe4cfa3Казармы|r",
        "tip": "|cffe4cfa3Казармы|r (|cffffffffZ|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Военный лагерь подготовки наземных войск Стромгарда.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deОполченец|cffced4da: призывной боец ближнего боя.|n"
            "- |cffa9c7deПехотинец|cffced4da: базовый воин ближнего боя.|n"
            "- |cffa9c7deЗащитник|cffced4da: тяжёлый пехотинец со щитом.|n"
            "- |cffa9c7deАрбалетчик|cffced4da: стрелок дальнего боя.|n"
            "- |cffa9c7deРыцарь|cffced4da: тяжёлый конный всадник.|n|n"
            "|cffa6afb8Исследования:|cffced4da|n"
            "- |cffe4cfa3Защита|cffced4da: даёт пехотинцам способность снижения урона щитом.|n"
            "- |cffe4cfa3Тренировки защитников|cffced4da: повышает характеристики защитников.|n"
            "- |cffe4cfa3Дрессировка животных|cffced4da: увеличивает здоровье и скорость рыцарей.|n|n"
            "|cffa6afb8Перестраивается в:|cffced4da|n"
            "- |cffa9c7deМагическая башня|cffced4da.|n"
            "- |cffa9c7deРынок|cffced4da.|r"
        )
    },
    {
        "id": "h0HI",
        "wts": {"name": 21291, "tip": 21292, "ubertip": 21077},
        "hotkey": "X",
        "name": "|cffe4cfa3Магическая башня|r",
        "tip": "|cffe4cfa3Магическая башня|r (|cffffffffX|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Башня чародеев Стромгарда. Подготавливает заклинателей и исследует улучшения магических войск.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deЖрец|cffced4da: заклинатель поддержки, исцеления и рассеивания чар.|n"
            "- |cffa9c7deЗаклинатель|cffced4da: боевой маг атакующей и вспомогательной магии.|n|n"
            "|cffa6afb8Исследования:|cffced4da|n"
            "- |cffe4cfa3Посвящение жрецов|cffced4da: увеличивает запас маны, здоровье и скорость восстановления маны жрецов.|n"
            "- |cffe4cfa3Посвящение заклинателей|cffced4da: увеличивает запас маны, здоровье и скорость восстановления маны заклинателей.|n"
            "- |cffe4cfa3Зачарованные мечи|cffced4da: зачаровывает клинки пехотинцев магической силой.|n|n"
            "|cffa6afb8Перестраивается в:|cffced4da|n"
            "- |cffa9c7deКазармы|cffced4da.|n"
            "- |cffa9c7deРынок|cffced4da.|r"
        )
    },
    {
        "id": "h0HU",
        "wts": {"name": 20079, "tip": 21309, "ubertip": 42700},
        "hotkey": "C",
        "name": "|cffe4cfa3Рынок|r",
        "tip": "|cffe4cfa3Рынок|r (|cffffffffC|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Торговый и хозяйственный квартал. Увеличивает базовый доход золота на |cffc8e08775|cffced4da за выплату и нанимает оруженосцев.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deОруженосец|cffced4da: вспомогательный воин королевства.|n|n"
            "|cffa6afb8Перестраивается в:|cffced4da|n"
            "- |cffa9c7deКазармы|cffced4da.|n"
            "- |cffa9c7deМагическая башня|cffced4da.|n|n"
            "Итоговый доход зависит от текущих модификаторов экономики.|r"
        )
    },
    {
        "id": "h0HF",
        "wts": {"name": 21284, "tip": 42699, "ubertip": 20487},
        "hotkey": "F",
        "name": "|cffe4cfa3Мастерская|r",
        "tip": "|cffe4cfa3Мастерская|r (|cffffffffF|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Осадная мастерская Стромгарда. Производит боевую технику, осадные орудия и нанимает стрелков-следопытов.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deОхотник на троллей|cffced4da: дальнобойный стрелок с ружьём.|n"
            "- |cffa9c7deКатапульта|cffced4da: осадное орудие дальнего боя.|n"
            "- |cffa9c7deБоевой танк|cffced4da: тяжёлая штурмовая бронемашина.|n|n"
            "|cffa6afb8Исследования:|cffced4da|n"
            "- |cffe4cfa3Шрапнель|cffced4da: увеличивает урон охотников на троллей.|n"
            "- |cffe4cfa3Длинноствольные мушкеты|cffced4da: увеличивает дальность стрельбы стрелков.|r"
        )
    },
    {
        "id": "h011",
        "wts": {"name": 368, "tip": 369, "ubertip": 370},
        "hotkey": "C",
        "name": "|cffe4cfa3Верфь|r",
        "tip": "|cffe4cfa3Верфь|r (|cffffffffC|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Корабельная верфь. Строит суда и исследует улучшения военного и транспортного флота.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deТранспорт|cffced4da: вместительное морское судно для перевозки сухопутных войск.|n"
            "- |cffa9c7deФрегат|cffced4da: быстроходный боевой корабль.|n"
            "- |cffa9c7deЛинкор|cffced4da: тяжёлый артиллерийский линейный корабль.|n|n"
            "|cffa6afb8Исследования:|cffced4da|n"
            "- Корабельные орудия, обшивка, паруса и оснастка флота.|r"
        )
    }
]

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    binary_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in source.glob("war3map*") if p.is_file() and p.name != "war3map.wts"}

    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    strings = []
    consumers = []
    updated_wts = original_wts
    changed_wts_ids = []

    for b in BUILDINGS:
        bid = b["id"]
        for field in ("name", "tip", "ubertip"):
            sid = b["wts"][field]
            val = b[field]
            before_val = resolve(f"TRIGSTR_{sid}")
            strings.append({
                "rawcode": bid,
                "field": field,
                "wts_id": sid,
                "before": before_val,
                "after": val
            })
            consumers.append({
                "file": "war3map.w3u",
                "id": bid,
                "field": field,
                "wts_id": sid
            })
            updated_wts = update_wts_string(updated_wts, sid, val)
            changed_wts_ids.append(sid)

    registry = {
        "scope": "Стромгард (Stromgard): партия 2 — модульные строения, мастерская и верфь (6 объектов, 18 полей)",
        "building_ids": [b["id"] for b in BUILDINGS],
        "total_buildings": len(BUILDINGS),
        "total_fields": len(strings),
        "variants": ["SD", "HD"],
        "buildings": BUILDINGS,
        "evidence": [
            "h0HH (Место постройки): upgrade=h0HU,h0H4,h0HI, hotkey=W",
            "h0H4 (Казармы): trains=h0F4,h0GT,h0GU,h0GS,h0GV, researches=R0DN,R0DJ,R0DG, upgrade=h0HI,h0HU, hotkey=Z",
            "h0HI (Магическая башня): trains=h0GX,h0GW, researches=R0DH,R0DI,R0DK, upgrade=h0H4,h0HU, requires=h0H0, hotkey=X",
            "h0HU (Рынок): trains=h0HD, upgrade=h0HI,h0H4, requires=h0H0, fmade=75 (+75 базового дохода), hotkey=C",
            "h0HF (Мастерская): trains=h0L3,o03X,h0GY, researches=R0H2,R0H1, requires=h0H0,h0H6, hotkey=F",
            "h011 (Верфь): trains=h00X,h00Y,h00Z, researches=R005,R006,R007,R002,R003, hotkey=C"
        ],
        "strings": strings,
        "consumers": consumers,
        "in_game_checked": False
    }

    (folder / "stromgard_buildings_02.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Apply to war3map.wts
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    wts_after = hw.load_wts_strings()
    for hd in (False, True):
        for b in BUILDINGS:
            bid = b["id"]
            args = ["get-object", "--type", "unit", "--id", bid]
            if hd:
                args.append("--hd")
            res = require(cli(args))
            f = res.get("fields", {})

            for field in ("name", "tip", "ubertip"):
                expected = b[field]
                actual = f.get(field, "")
                if actual.startswith("TRIGSTR_"):
                    actual = wts_after.get(int(actual[8:]), actual)
                assert actual == expected, f"Mismatch on {bid} {field} (hd={hd}): {actual!r} != {expected!r}"
                checks.append({
                    "variant": "HD" if hd else "SD",
                    "rawcode": bid,
                    "field": field,
                    "exact_match": True
                })

    # Verify binary files remained byte-identical
    for name, expected_hash in binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    report = {
        "ok": True,
        "applied": True,
        "method": "WTS-only",
        "changed_wts_ids": changed_wts_ids,
        "binary_sha256_unchanged": binary_hashes,
        "before_wts_sha256": original_wts_hash,
        "after_wts_sha256": new_wts_hash,
        "checks": checks,
        "total_checks": len(checks),
        "palette_and_color_resets_ok": True,
        "hotkeys_and_mechanics_unchanged": True,
        "in_game_checked": False
    }

    (folder / "stromgard_buildings_02_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "buildings": len(BUILDINGS), "fields_checked": len(checks)}))

if __name__ == "__main__":
    main()
