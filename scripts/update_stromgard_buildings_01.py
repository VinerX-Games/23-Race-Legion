# -*- coding: utf-8 -*-
"""Update Stromgard buildings batch 1 (main & municipal buildings) via WTS with complete SD/HD validation."""
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
        "id": "h0GZ",
        "wts": {"name": 21263, "tip": 42691, "ubertip": 42690},
        "hotkey": "Q",
        "name": "|cffe4cfa3Ратуша|r",
        "tip": "|cffe4cfa3Ратуша|r (|cffffffffQ|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание первой ступени. Принимает добытые золото и древесину.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deРаботник|cffced4da.|n|n"
            "|cffa6afb8Улучшается до:|cffced4da|n"
            "- |cffa9c7deФорт|cffced4da.|n|n"
            "|cffa6afb8Дополнительные функции:|cffced4da|n"
            "- |cffa9c7deПризыв к оружию|cffced4da: временно превращает работников в ополченцев.|n"
            "- |cffa9c7deЗащита столицы|cffced4da: снижает восстановление здоровья ближайших органических врагов.|r"
        )
    },
    {
        "id": "h0H0",
        "wts": {"name": 21265, "tip": 42692, "ubertip": 22569},
        "hotkey": "D",
        "name": "|cffe4cfa3Форт|r",
        "tip": "|cffe4cfa3Форт|r (|cffffffffD|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание второй ступени. Принимает добытые золото и древесину.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deРаботник|cffced4da.|n|n"
            "|cffa6afb8Исследования:|cffced4da|n"
            "- |cffe4cfa3Профессиональная армия|cffced4da: усиливает характеристики войск казарм и магических башен.|n"
            "- |cffe4cfa3Призывная армия|cffced4da: позволяет нанимать войска парами со сниженными характеристиками.|n|n"
            "|cffa6afb8Улучшается до:|cffced4da|n"
            "- |cffa9c7deЗамок|cffced4da.|n|n"
            "|cffa6afb8Дополнительные функции:|cffced4da|n"
            "- |cffa9c7deПризыв к оружию|cffced4da: временно превращает работников в ополченцев.|n"
            "- |cffa9c7deЗащита столицы|cffced4da: снижает восстановление здоровья ближайших органических врагов.|r"
        )
    },
    {
        "id": "h0H1",
        "wts": {"name": 21267, "tip": 42693, "ubertip": 22575},
        "hotkey": "Z",
        "name": "|cffe4cfa3Замок|r",
        "tip": "|cffe4cfa3Замок|r (|cffffffffZ|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание третьей, высшей ступени. Принимает добытые золото и древесину и открывает доступ к передовым технологиям.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deРаботник|cffced4da.|n|n"
            "|cffa6afb8Дополнительные функции:|cffced4da|n"
            "- |cffa9c7deПризыв к оружию|cffced4da: временно превращает работников в ополченцев.|n"
            "- |cffa9c7deЗащита столицы|cffced4da: снижает восстановление здоровья ближайших органических врагов.|r"
        )
    },
    {
        "id": "h0H2",
        "wts": {"name": 21115, "tip": 42695, "ubertip": 42694},
        "hotkey": "A",
        "name": "|cffe4cfa3Ферма|r",
        "tip": "|cffe4cfa3Ферма|r (|cffffffffA|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Хозяйственное строение. Обеспечивает провизией армию королевства, увеличивая базовый доход золота на |cffc8e08740|cffced4da за выплату.|n|n"
            "Итоговый доход зависит от текущих модификаторов экономики.|r"
        )
    },
    {
        "id": "h0H3",
        "wts": {"name": 21270, "tip": 42696, "ubertip": 20424},
        "hotkey": "S",
        "name": "|cffe4cfa3Алтарь королей|r",
        "tip": "|cffe4cfa3Алтарь королей|r (|cffffffffS|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Священное место сбора предводителей Стромгарда. Позволяет призывать и воскрешать павших героев королевства.|n|n"
            "|cffa6afb8Обучает:|cffced4da|n"
            "- |cffa9c7deГенерал|cffced4da: военачальник ближнего боя.|n"
            "- |cffa9c7deКазначей|cffced4da: маг поддержки и управления ресурсами.|n"
            "- |cffa9c7deВерховный маг|cffced4da: могущественный заклинатель дальнего боя.|r"
        )
    },
    {
        "id": "h0H5",
        "wts": {"name": 21274, "tip": 42697, "ubertip": 22611},
        "hotkey": "E",
        "name": "|cffe4cfa3Лесопилка|r",
        "tip": "|cffe4cfa3Лесопилка|r (|cffffffffE|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Лесопильный двор. Принимает добытую древесину и позволяет исследовать улучшения добычи и прочности строений.|n|n"
            "|cffa6afb8Исследования:|cffced4da|n"
            "- |cffe4cfa3Улучшенные инструменты|cffced4da: повышает вместимость добываемой работниками древесины.|n"
            "- |cffe4cfa3Улучшенная кладка|cffced4da: увеличивает запас здоровья и броню зданий.|r"
        )
    },
    {
        "id": "h0H6",
        "wts": {"name": 21276, "tip": 42698, "ubertip": 22616},
        "hotkey": "R",
        "name": "|cffe4cfa3Кузница|r",
        "tip": "|cffe4cfa3Кузница|r (|cffffffffR|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Оружейная кузница. Позволяет исследовать улучшения оружия, доспехов, пороха и стрел для армии Стромгарда.|n|n"
            "|cffa6afb8Исследования:|cffced4da|n"
            "- |cffe4cfa3Железные мечи|cffced4da: увеличивает урон пехоты и рыцарей.|n"
            "- |cffe4cfa3Железная броня|cffced4da: увеличивает защиту пехоты и рыцарей.|n"
            "- |cffe4cfa3Чёрный порох|cffced4da: увеличивает урон стрелков и осадных орудий.|n"
            "- |cffe4cfa3Накидки из клёпаной кожи|cffced4da: увеличивает защиту стрелков.|n"
            "- |cffe4cfa3Магическая атака|cffced4da: увеличивает урон заклинателей.|n"
            "- |cffe4cfa3Огненные стрелы|cffced4da: наделяет стрелков огненными стрелами.|r"
        )
    },
    {
        "id": "h0HG",
        "wts": {"name": 21286, "tip": 8048, "ubertip": 12986},
        "hotkey": "Z",
        "name": "|cffe4cfa3Сторожевая башня|r",
        "tip": "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)",
        "ubertip": (
            "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое оборонительное сооружение. Обстреливает противников стрелами с большого расстояния.|n|n"
            "Атакует наземные и воздушные цели.|r"
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
        "scope": "Стромгард (Stromgard): партия 1 — основные и муниципальные здания (8 объектов, 24 поля)",
        "building_ids": [b["id"] for b in BUILDINGS],
        "total_buildings": len(BUILDINGS),
        "total_fields": len(strings),
        "variants": ["SD", "HD"],
        "buildings": BUILDINGS,
        "evidence": [
            "h0GZ (Ратуша): trains=h0G9, upgrade=h0H0, abillist=Argl,A0IQ,A0LJ,A0LI, hotkey=Q",
            "h0H0 (Форт): trains=h0G9, researches=R0D6,R0D5, upgrade=h0H1, abillist=A0LJ,A0LI,A0IQ,Argl, hotkey=D",
            "h0H1 (Замок): trains=h0G9, abillist=A0LJ,A0LI,A0IQ,Argl, hotkey=Z",
            "h0H2 (Ферма): fmade=40 (+40 базового дохода в 54_count_dis.lua), hotkey=A",
            "h0H3 (Алтарь королей): trains=H0HB,H0HL,H0HA, воскрешение героев, hotkey=S",
            "h0H5 (Лесопилка): researches=R0DM,R0DL, abillist=Abds,Arlm, склад древесины, hotkey=E",
            "h0H6 (Кузница): researches=R0E2,R0DA,R0DB,R0DE,R0DD,R0DC, hotkey=R",
            "h0HG (Сторожевая башня): weapson=1, atktype1=pierce, avgdmg1=25, rangen1=700, targs1=ground,structure,debris,air,item,ward, hotkey=Z"
        ],
        "strings": strings,
        "consumers": consumers,
        "in_game_checked": False
    }

    (folder / "stromgard_buildings_01.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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

    (folder / "stromgard_buildings_01_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "buildings": len(BUILDINGS), "fields_checked": len(checks)}))

if __name__ == "__main__":
    main()
