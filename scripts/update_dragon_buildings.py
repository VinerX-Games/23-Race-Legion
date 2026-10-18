# -*- coding: utf-8 -*-
"""Update Dragon race buildings (all 10 buildings) with complete SD/HD validation."""
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
    other_binary_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in source.glob("war3map*") if p.is_file() and p.name not in ["war3map.wts", "war3map.w3u", "war3mapSkin.w3u"]}

    buildings_data = [
        {
            "id": "dra0",
            "name": "|cffe4cfa3Древний Храм|r",
            "tip": "|cffe4cfa3Древний Храм|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Главное святилище драконьих стай. "
                "Служит центром поселения, пунктом сбора ресурсов, позволяет назначать столицу, "
                "обменивать ресурсы, обучать рабочих и разведчиков, а также исследовать новые поколения драконов.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deСтроитель|cffced4da|n"
                "- |cffa9c7deСиний драконид – разведчик|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deНовое поколение|cffced4da.|r"
            ),
            "wts": {"name": 39646, "tip": 39648, "ubertip": 39647},
            "hotkey": "Q"
        },
        {
            "id": "h0F9",
            "name": "|cffe4cfa3Гнездо драконов|r",
            "tip": "|cffe4cfa3Гнездо драконов|r (|cffffffffA|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Гнездо для выведения драконьего потомства. "
                "Обеспечивает пищу для содержания армии и приносит |cffffffff+20|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
            ),
            "wts": {"name": 16959, "tip": 17018, "ubertip": 31815},
            "hotkey": "A"
        },
        {
            "id": "n03I",
            "name": "|cffe4cfa3Сосредоточение могущества|r",
            "tip": "|cffe4cfa3Сосредоточение могущества|r (|cffffffffS|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Центр сосредоточения магической и физической силы драконов. "
                "Позволяет исследовать улучшенную добычу ресурсов, практику полётов и мудрость различных драконьих стай.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deУлучшенная добыча|cffced4da|n"
                "- |cffa9c7deПрактика полетов|cffced4da|n"
                "- |cffa9c7deМудрость зеленых драконов|cffced4da|n"
                "- |cffa9c7deМудрость синих драконов|cffced4da|n"
                "- |cffa9c7deМудрость красных драконов|cffced4da|n"
                "- |cffa9c7deМудрость бронзовых драконов|cffced4da|n"
                "- |cffa9c7deМудрость черных драконов|cffced4da.|r"
            ),
            "wts": {"name": 14972, "tip": 10913, "ubertip": 8157},
            "hotkey": "S"
        },
        {
            "id": "n03Z",
            "name": "|cffe4cfa3Гнездо бронзовых драконов|r",
            "tip": "|cffe4cfa3Гнездо бронзовых драконов|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель бронзовой стаи, повелителей времени. "
                "Позволяет призывать Ноздорму, обучать строителей и боевых бронзовых драконов, "
                "а также исследовать магию времени и эволюцию стаи.|n|n"
                "|cffa6afb8Герои:|cffced4da|n"
                "- |cffa9c7deНоздорму|cffced4da.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deСтроитель|cffced4da|n"
                "- |cffa9c7deБронзовый дракончик|cffced4da|n"
                "- |cffa9c7deЗащитник сингулярности|cffced4da|n"
                "- |cffa9c7deХранитель времени|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deМагия времени|cffced4da|n"
                "- |cffa9c7deЭволюция бронзовых драконов|cffced4da.|r"
            ),
            "wts": {"name": 14668, "tip": 8148, "ubertip": 8149},
            "hotkey": "R"
        },
        {
            "id": "n041",
            "name": "|cffe4cfa3Гнездо зеленых драконов|r",
            "tip": "|cffe4cfa3Гнездо зеленых драконов|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель зелёной стаи, владык природы и изумрудного сна. "
                "Позволяет призывать Изеру, обучать строителей и боевых зелёных драконов, "
                "а также исследовать изумрудную связь и эволюцию стаи.|n|n"
                "|cffa6afb8Герои:|cffced4da|n"
                "- |cffa9c7deИзера|cffced4da.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deСтроитель|cffced4da|n"
                "- |cffa9c7deЗеленый дракончик|cffced4da|n"
                "- |cffa9c7deИзумрудный страж|cffced4da|n"
                "- |cffa9c7deХранитель сна|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deИзумрудная связь|cffced4da|n"
                "- |cffa9c7deЭволюция зеленых драконов|cffced4da.|r"
            ),
            "wts": {"name": 14670, "tip": 8150, "ubertip": 8151},
            "hotkey": "W"
        },
        {
            "id": "n042",
            "name": "|cffe4cfa3Гнездо красных драконов|r",
            "tip": "|cffe4cfa3Гнездо красных драконов|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель красной стаи, защитников жизни и пламени. "
                "Позволяет призывать Алекстразу, обучать строителей и боевых красных драконов, "
                "а также исследовать мудрость жизни и эволюцию стаи.|n|n"
                "|cffa6afb8Герои:|cffced4da|n"
                "- |cffa9c7deАлекстраза|cffced4da.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deСтроитель|cffced4da|n"
                "- |cffa9c7deКрасный дракончик|cffced4da|n"
                "- |cffa9c7deВершитель жизни|cffced4da|n"
                "- |cffa9c7deЗащитник стаи|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deМудрость жизни|cffced4da|n"
                "- |cffa9c7deЭволюция красных драконов|cffced4da.|r"
            ),
            "wts": {"name": 14762, "tip": 8153, "ubertip": 25583},
            "hotkey": "E"
        },
        {
            "id": "n043",
            "name": "|cffe4cfa3Гнездо синих драконов|r",
            "tip": "|cffe4cfa3Гнездо синих драконов|r (|cffffffffD|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель синей стаи, хранителей тайной магии и знаний. "
                "Позволяет призывать Малигоса, обучать строителей и боевых синих драконов, "
                "а также исследовать тайные чары и эволюцию стаи.|n|n"
                "|cffa6afb8Герои:|cffced4da|n"
                "- |cffa9c7deМалигос|cffced4da.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deСтроитель|cffced4da|n"
                "- |cffa9c7deСиний дракончик|cffced4da|n"
                "- |cffa9c7deХранитель энергии|cffced4da|n"
                "- |cffa9c7deХранитель магии|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deПрактика арканы|cffced4da|n"
                "- |cffa9c7deЭволюция синих драконов|cffced4da.|r"
            ),
            "wts": {"name": 14788, "tip": 8154, "ubertip": 8155},
            "hotkey": "D"
        },
        {
            "id": "n044",
            "name": "|cffe4cfa3Гнездо черных драконов|r",
            "tip": "|cffe4cfa3Гнездо черных драконов|r (|cffffffffF|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель чёрной стаи, владык земли и глубин. "
                "Позволяет обучать строителей, чёрных драконов и надзирателей, "
                "а также исследовать ярость земли, ускользание и эволюцию стаи.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deСтроитель|cffced4da|n"
                "- |cffa9c7deЧерный дракончик|cffced4da|n"
                "- |cffa9c7deЧерный дракон|cffced4da|n"
                "- |cffa9c7deДревний черный дракон|cffced4da|n"
                "- |cffa9c7deЧерный драконид – Надзиратель|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deЯрость земли|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da|n"
                "- |cffa9c7deДраконья ярость|cffced4da|n"
                "- |cffa9c7deЭволюция черных драконов|cffced4da.|r"
            ),
            "wts": {"name": 14882, "ubertip": 8156},
            "hotkey": "F",
            "object_mods": {"tip": "|cffe4cfa3Гнездо черных драконов|r (|cffffffffF|r)"}
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
        },
        {
            "id": "dra1",
            "name": "|cffe4cfa3Выбор Стаи|r",
            "tip": "|cffe4cfa3Выбор Стаи|r",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Временный пункт выбора направленности драконьей стаи. "
                "Позволяет утвердить вступление в Драконий Союз и получить базовых строителей для основания поселения.|r"
            ),
            "wts": {"name": 39757, "tip": 39758},
            "hotkey": "T",
            "object_mods": {"ubertip": "|cffa6afb8ЗДАНИЕ:|cffced4da Временный пункт выбора направленности драконьей стаи. Позволяет утвердить вступление в Драконий Союз и получить базовых строителей для основания поселения.|r"}
        }
    ]

    # Update WTS
    updated_wts = original_wts
    wts_changed_ids = []
    for b in buildings_data:
        for f, string_id in b.get("wts", {}).items():
            updated_wts = update_wts_string(updated_wts, string_id, b[f])
            wts_changed_ids.append(string_id)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Apply direct object mods for missing fields
    object_ops = [
        {"type": "unit", "id": "n044", "field": "tip", "value": "|cffe4cfa3Гнездо черных драконов|r (|cffffffffF|r)"},
        {"type": "unit", "id": "dra1", "field": "ubertip", "value": "|cffa6afb8ЗДАНИЕ:|cffced4da Временный пункт выбора направленности драконьей стаи. Позволяет утвердить вступление в Драконий Союз и получить базовых строителей для основания поселения.|r"}
    ]

    w3u_bytes = w3u_path.read_bytes()
    new_w3u, w3u_changed = patch_blob(w3u_bytes, object_ops, "unit", add_missing=True)
    w3u_path.write_bytes(new_w3u)
    new_w3u_hash = hashlib.sha256(w3u_path.read_bytes()).hexdigest()

    w3u_skin_bytes = w3u_skin_path.read_bytes()
    new_w3u_skin, w3u_skin_changed = patch_blob(w3u_skin_bytes, object_ops, "unit", add_missing=True)
    w3u_skin_path.write_bytes(new_w3u_skin)
    new_w3u_skin_hash = hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    building_ids = [b["id"] for b in buildings_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(building_ids), "--fields", "name,tip,ubertip"] + hd_flag))
        wts_dict = hw.load_wts_strings()
        resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}
        for b in buildings_data:
            fields = objects_by_id.get(b["id"], {})
            actual_name = resolve(fields.get("name", ""))
            actual_tip = resolve(fields.get("tip", ""))
            actual_ubertip = resolve(fields.get("ubertip", ""))

            assert actual_name == b["name"], f"Name mismatch for {b['id']} (hd={hd}): {actual_name} != {b['name']}"
            assert actual_tip == b["tip"], f"Tip mismatch for {b['id']} (hd={hd}): {actual_tip} != {b['tip']}"
            assert actual_ubertip == b["ubertip"], f"Ubertip mismatch for {b['id']} (hd={hd}): {actual_ubertip} != {b['ubertip']}"

            checks.append({"id": b["id"], "variant": "HD" if hd else "SD", "fields_verified": ["name", "tip", "ubertip"]})

    # Verify other binary files remain untouched
    for name, expected_hash in other_binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    registry = {
        "scope": "Драконы (Dragon): категория зданий (10 зданий, 30 полей)",
        "in_game_checked": False,
        "variants": ["SD", "HD"],
        "buildings": [b["id"] for b in buildings_data],
        "evidence": {
            "town_hall": "dra0 Древний Храм обучает o01D и n03F, исследует R0D9, имеет функции столицы и обмена ресурсов",
            "farms": "h0F9 Гнездо драконов обеспечивает пищу и приносит +20 золота за выплату",
            "upgrade_center": "n03I Сосредоточение могущества исследует R0DT, R0B0, R0AV, R0AW, R0AX, R0AY, R0AZ",
            "dragon_flights": "4 гнезда стай (n03Z бронзовые, n041 зеленые, n042 красные, n043 синие) вызывают Аспектов-героев, драконов и их эволюцию; n044 черные драконы обучают боевых драконов и надзирателей",
            "shipyard": "h0D8 Верфь строит суда h0D9, h0DB, h0DA, исследует 5 морских улучшений и обладает аурой Ремонта A15N",
            "selector": "dra1 Выбор Стаи служит стартовым пунктом выбора и перехода в Драконий Союз"
        },
        "changed_wts_ids": wts_changed_ids,
        "object_mods": object_ops
    }

    report = {
        "ok": True,
        "applied": True,
        "buildings_count": len(buildings_data),
        "fields_verified_count": len(checks) * 3,
        "wts_changed_count": len(wts_changed_ids),
        "w3u_changed": w3u_changed,
        "w3u_skin_changed": w3u_skin_changed,
        "checks": checks,
        "sha256": {
            "wts_before": original_wts_hash,
            "wts_after": new_wts_hash,
            "w3u_before": original_w3u_hash,
            "w3u_after": new_w3u_hash,
            "w3u_skin_before": original_w3u_skin_hash,
            "w3u_skin_after": new_w3u_skin_hash
        }
    }

    (folder / "dragon_buildings.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "dragon_buildings_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "buildings": len(buildings_data), "checks": len(checks)}))

if __name__ == "__main__":
    main()
