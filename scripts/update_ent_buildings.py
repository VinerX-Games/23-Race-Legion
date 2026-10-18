# -*- coding: utf-8 -*-
"""Update Ents (Argvinol) race buildings (10 buildings) with complete SD/HD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require
from apply_faceless_object_text import patch_blob

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING {string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    w3u_path = ROOT / "map.w3x/war3map.w3u"
    w3u_skin_path = ROOT / "map.w3x/war3mapSkin.w3u"

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    original_w3u_hash = hashlib.sha256(w3u_path.read_bytes()).hexdigest()
    original_w3u_skin_hash = hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name not in ["war3map.wts", "war3map.w3u", "war3mapSkin.w3u"]
    }

    buildings_data = [
        {
            "id": "e02B",
            "name": "|cffe4cfa3Древо Знаний|r",
            "tip": "|cffe4cfa3Древо Знаний|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Главное святилище и центр поселения древней. "
                "Позволяет назначать столицу, обменивать ресурсы, призывать рабочих виспов и исследовать базовые улучшения лесной армии.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deДревний Висп|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deСила природы|cffced4da|n"
                "- |cffa9c7deПрочная кора|cffced4da|n"
                "- |cffa9c7deБлагословение природы|cffced4da.|n|n"
                "|cffa6afb8Улучшается до:|cffced4da |cffa9c7deДрево просветления|cffced4da.|r"
            ),
            "wts": {"name": 35187, "tip": 37723},
            "hotkey": "Q"
        },
        {
            "id": "e02C",
            "name": "|cffe4cfa3Древо просветления|r",
            "tip": "|cffe4cfa3Древо просветления|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Вторая ступень главного святилища древней. "
                "Открывает доступ к продвинутым войскам, постройкам и улучшениям, "
                "позволяет назначать столицу, обменивать ресурсы и призывать рабочих.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deДревний Висп|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deСила природы|cffced4da|n"
                "- |cffa9c7deПрочная кора|cffced4da|n"
                "- |cffa9c7deБлагословение природы|cffced4da.|n|n"
                "|cffa6afb8Улучшается до:|cffced4da |cffa9c7deДрево познания|cffced4da.|r"
            ),
            "wts": {"name": 37975, "tip": 40075},
            "hotkey": "Z"
        },
        {
            "id": "e02D",
            "name": "|cffe4cfa3Древо познания|r",
            "tip": "|cffe4cfa3Древо познания|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Высшая ступень святилища древней. "
                "Открывает максимальный технологический уровень, защитные чары столицы, "
                "позволяет обменивать ресурсы и призывать рабочих виспов.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deДревний Висп|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deСила природы|cffced4da|n"
                "- |cffa9c7deПрочная кора|cffced4da|n"
                "- |cffa9c7deБлагословение природы|cffced4da.|r"
            ),
            "wts": {"name": 41521, "tip": 41536},
            "hotkey": "Z"
        },
        {
            "id": "e02E",
            "name": "|cffe4cfa3Колодец воспоминаний|r",
            "tip": "|cffe4cfa3Колодец воспоминаний|r (|cffffffffA|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Священный источник живительной влаги. "
                "Обеспечивает поселение пищей, восстанавливает здоровье и ману союзным войскам, "
                "а также приносит доход в |cffffffff+7|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
            ),
            "wts": {"name": 41537, "tip": 41538},
            "hotkey": "A"
        },
        {
            "id": "e02F",
            "name": "|cffe4cfa3Древо войны|r",
            "tip": "|cffe4cfa3Древо войны|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Военная роща древней. Позволяет пробуждать боевых древесных воинов, лесных гончих и исследовать боевые улучшения.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deДревень|cffced4da|n"
                "- |cffa9c7deЭнт дробитель|cffced4da|n"
                "- |cffa9c7deГончая Жизни|cffced4da|n"
                "- |cffa9c7deМалое Древо Войны|cffced4da|n"
                "- |cffa9c7deГончая Маны|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deЯдовитый Сок|cffced4da|n"
                "- |cffa9c7deУсиление Ядра Маны|cffced4da|n"
                "- |cffa9c7deУсиление Ядра Жизни|cffced4da|n"
                "- |cffa9c7deМастерство Войны|cffced4da.|r"
            ),
            "wts": {"name": 41542, "tip": 41543},
            "hotkey": "W"
        },
        {
            "id": "e02G",
            "name": "|cffe4cfa3Алтарь мудрейших|r",
            "tip": "|cffe4cfa3Алтарь мудрейших|r (|cffffffffS|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Священный алтарь древнейших хранителей рощи. "
                "Позволяет призывать и воскрешать героев лесного народа.|n|n"
                "|cffa6afb8Герои:|cffced4da|n"
                "- |cffa9c7deЛесной Смотритель|cffced4da|n"
                "- |cffa9c7deДух леса|cffced4da|n"
                "- |cffa9c7deЕгерь диколесья|cffced4da.|r"
            ),
            "wts": {"name": 41540, "tip": 41541},
            "hotkey": "S"
        },
        {
            "id": "e02H",
            "name": "|cffe4cfa3Древо мудрости|r",
            "tip": "|cffe4cfa3Древо мудрости|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище древней магии природы. "
                "Позволяет призывать духов, могучих древесных гигантов и исследовать тайные знания леса.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deЛесной Дух|cffced4da|n"
                "- |cffa9c7deДрево Познания|cffced4da|n"
                "- |cffa9c7deДрево Ветров|cffced4da|n"
                "- |cffa9c7deЛесной Голем|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deКрепкий панцирь|cffced4da|n"
                "- |cffa9c7deБлагословение Ветра|cffced4da|n"
                "- |cffa9c7deУчения Леса|cffced4da|n"
                "- |cffa9c7deМагия Духа|cffced4da.|r"
            ),
            "wts": {"name": 41545, "tip": 41546},
            "hotkey": "E"
        },
        {
            "id": "e03N",
            "name": "|cffe4cfa3Обитель Хранителей|r",
            "tip": "|cffe4cfa3Обитель Хранителей|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Роща защитников леса. "
                "Позволяет призывать лесных дракончиков, дриад, хранителей рощи и изучать их особые способности.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deЛесной Дракончик|cffced4da|n"
                "- |cffa9c7deДриада|cffced4da|n"
                "- |cffa9c7deХранитель Рощи|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deМудрость Дракончиков|cffced4da|n"
                "- |cffa9c7deАзы Дриад|cffced4da|n"
                "- |cffa9c7deЗнание Хранителей|cffced4da.|r"
            ),
            "wts": {"name": 19415, "tip": 33246},
            "hotkey": "R"
        },
        {
            "id": "e02I",
            "name": "|cffe4cfa3Сторожевое древо|r",
            "tip": "|cffe4cfa3Сторожевое древо|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Древний древесный страж, защищающий границы владений. "
                "Атакует бросками тяжёлых валунов наземные и воздушные цели.|n|n"
                "Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 41548, "tip": 41549},
            "hotkey": "Z"
        },
        {
            "id": "h0D8",
            "name": "|cffe4cfa3Верфь|r",
            "tip": "|cffe4cfa3Верфь|r (|cffffffffC|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Строит корабли и исследует общие улучшения флота.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deТранспорт|cffced4da|n"
                "- |cffa9c7deФрегат|cffced4da|n"
                "- |cffa9c7deЛинкор|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deОбстрел|cffced4da|n"
                "- |cffa9c7deДополнительные паруса|cffced4da|n"
                "- |cffa9c7deПочинка|cffced4da|n"
                "- |cffa9c7deОрудия флота|cffced4da|n"
                "- |cffa9c7deУкреплённый корпус|cffced4da.|n|n"
                "|cffa9c7deЗона ремонта|cffced4da восстанавливает |cffc8e0872,5|cffced4da здоровья/сек. союзным наземным механическим войскам в радиусе |cffffffff550|cffced4da.|r"
            ),
            "wts": {"name": 10907, "tip": 10908, "ubertip": 10903},
            "hotkey": "C"
        }
    ]

    # Update WTS
    updated_wts = original_wts
    wts_changed_ids = []
    for b in buildings_data:
        for f, string_id in b.get("wts", {}).items():
            if b["id"] == "h0D8":
                continue  # already standardized
            updated_wts = update_wts_string(updated_wts, string_id, b[f])
            wts_changed_ids.append(string_id)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Apply ubertips via patch_blob to war3map.w3u and war3mapSkin.w3u
    object_ops = [
        {"type": "unit", "id": b["id"], "field": "ubertip", "value": b["ubertip"]}
        for b in buildings_data if b["id"] != "h0D8"
    ]

    w3u_bytes = w3u_path.read_bytes()
    new_w3u, w3u_changed = patch_blob(w3u_bytes, object_ops, "unit", add_missing=True)
    w3u_path.write_bytes(new_w3u)
    new_w3u_hash = hashlib.sha256(w3u_path.read_bytes()).hexdigest()

    w3u_skin_bytes = w3u_skin_path.read_bytes()
    new_w3u_skin, w3u_skin_changed = patch_blob(w3u_skin_bytes, object_ops, "unit", add_missing=True)
    w3u_skin_path.write_bytes(new_w3u_skin)
    new_w3u_skin_hash = hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest()

    # Invalidate wts cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()

    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Readback checks in SD and HD
    checks = []
    building_ids = [b["id"] for b in buildings_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(building_ids), "--fields", "name,tip,ubertip"] + hd_flag))
        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

        for b in buildings_data:
            fields = objects_by_id.get(b["id"], {})
            actual_name = resolve(fields.get("name", ""))
            actual_tip = resolve(fields.get("tip", ""))
            actual_ubertip = resolve(fields.get("ubertip", ""))

            assert actual_name == b["name"], f"Name mismatch for {b['id']} (hd={hd}): '{actual_name}' != '{b['name']}'"
            assert actual_tip == b["tip"], f"Tip mismatch for {b['id']} (hd={hd}): '{actual_tip}' != '{b['tip']}'"
            assert actual_ubertip == b["ubertip"], f"Ubertip mismatch for {b['id']} (hd={hd}):\nActual: '{actual_ubertip}'\nExpected: '{b['ubertip']}'"

            checks.append({
                "id": b["id"],
                "variant": "HD" if hd else "SD",
                "fields_verified": ["name", "tip", "ubertip"]
            })

    # Verify other binary files remain untouched
    for name, expected_hash in other_binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    registry = {
        "race": "Ents",
        "category": "buildings",
        "total_buildings": len(buildings_data),
        "buildings": buildings_data
    }
    (folder / "ent_buildings.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Ents",
        "category": "buildings",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "w3u_hash_before": original_w3u_hash,
        "w3u_hash_after": new_w3u_hash,
        "w3u_skin_hash_before": original_w3u_skin_hash,
        "w3u_skin_hash_after": new_w3u_skin_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "ent_buildings_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(buildings_data)} Ent buildings.")
    print(f"Updated {len(set(wts_changed_ids))} WTS keys, {len(object_ops)} object patches.")
    print(f"Verified {len(checks)} SD/HD object checks (60 field values).")

if __name__ == "__main__":
    main()
