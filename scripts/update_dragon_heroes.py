# -*- coding: utf-8 -*-
"""Update Dragon race heroes (all 4 heroes, both base and dragon forms: 8 objects) with complete SD/HD validation."""
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
    binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name != "war3map.wts"
    }

    heroes_data = [
        # 1. Nozdormu (Bronze Aspect) - Base Form
        {
            "id": "N040",
            "name": "|cffe4cfa3Ноздорму|r",
            "propernames": "Ноздорму",
            "tip": "|cffe4cfa3Ноздорму|r (|cffffffffZ|r)",
            "revivetip": "|cffe4cfa3Ноздорму|r",
            "awakentip": "|cffe4cfa3Ноздорму|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Владыка времени и бессмертный аспект бронзовой стаи. "
                "Повелевает песчаными бурями, ускоряет свои атаки, обращает раны вспять и возрождается после гибели.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму бронзового дракона|n"
                "- |cffa9c7deМанипуляция времени|cffced4da: наносит периодический урон врагам в песчаной буре|n"
                "- |cffa9c7deУскорение времени|cffced4da: колоссально повышает скорость боя ценой входящего урона|n"
                "- |cffa9c7deЗдоровье прошлого|cffced4da: мгновенно обращает время вспять и восстанавливает здоровье|n"
                "- |cffa9c7deРеинкарнация|cffced4da: автоматически воскрешает героя после гибели.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 3647,
                "propernames": 13860,
                "tip": 15678,
                "ubertip": 31806,
                "revivetip": 19864,
                "awakentip": 13863
            },
            "hotkey": "Z"
        },
        # 1b. Nozdormu - Dragon Form
        {
            "id": "N049",
            "name": "|cffe4cfa3Ноздорму|r",
            "propernames": "Ноздорму",
            "tip": "|cffe4cfa3Ноздорму|r",
            "revivetip": "|cffe4cfa3Ноздорму|r",
            "awakentip": "|cffe4cfa3Ноздорму|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Владыка времени и бессмертный аспект бронзовой стаи. "
                "Повелевает песчаными бурями, ускоряет свои атаки, обращает раны вспять и возрождается после гибели.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму бронзового дракона|n"
                "- |cffa9c7deМанипуляция времени|cffced4da: наносит периодический урон врагам в песчаной буре|n"
                "- |cffa9c7deУскорение времени|cffced4da: колоссально повышает скорость боя ценой входящего урона|n"
                "- |cffa9c7deЗдоровье прошлого|cffced4da: мгновенно обращает время вспять и восстанавливает здоровье|n"
                "- |cffa9c7deРеинкарнация|cffced4da: автоматически воскрешает героя после гибели.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 20382,
                "propernames": 32148,
                "tip": 32154,
                "ubertip": 31812,
                "revivetip": 15595,
                "awakentip": 32149
            },
            "hotkey": "E"
        },
        # 2. Ysera (Green Aspect) - Base Form
        {
            "id": "N047",
            "name": "|cffe4cfa3Изера|r",
            "propernames": "Изера",
            "tip": "|cffe4cfa3Изера|r (|cffffffffZ|r)",
            "revivetip": "|cffe4cfa3Изера|r",
            "awakentip": "|cffe4cfa3Изера|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Владычица Изумрудного Сна и аспект зелёной стаи. "
                "Поражает врагов разрушительными волнами энергии, ускоряет и лечит союзников, "
                "лишает противников магии и погружает врагов в кокон сна.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму зелёного дракона|n"
                "- |cffa9c7deЯрость Изеры|cffced4da: выпускает сокрушительную волну природной энергии|n"
                "- |cffa9c7deАура жизни|cffced4da: ускоряет передвижение и регенерацию здоровья союзников|n"
                "- |cffa9c7deНемота|cffced4da: запрещает врагам в области применять способности|n"
                "- |cffa9c7deЧастица изумрудного сна|cffced4da: заключает врагов в сонный кокон, оглушая и нанося урон.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 16632,
                "propernames": 16900,
                "tip": 16634,
                "ubertip": 31809,
                "revivetip": 20804,
                "awakentip": 16633
            },
            "hotkey": "Z"
        },
        # 2b. Ysera - Dragon Form
        {
            "id": "N04B",
            "name": "|cffe4cfa3Изера|r",
            "propernames": "Изера",
            "tip": "|cffe4cfa3Изера|r",
            "revivetip": "|cffe4cfa3Изера|r",
            "awakentip": "|cffe4cfa3Изера|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Владычица Изумрудного Сна и аспект зелёной стаи. "
                "Поражает врагов разрушительными волнами энергии, ускоряет и лечит союзников, "
                "лишает противников магии и погружает врагов в кокон сна.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму зелёного дракона|n"
                "- |cffa9c7deЯрость Изеры|cffced4da: выпускает сокрушительную волну природной энергии|n"
                "- |cffa9c7deАура жизни|cffced4da: ускоряет передвижение и регенерацию здоровья союзников|n"
                "- |cffa9c7deНемота|cffced4da: запрещает врагам в области применять способности|n"
                "- |cffa9c7deЧастица изумрудного сна|cffced4da: заключает врагов в сонный кокон, оглушая и нанося урон.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 20720,
                "propernames": 20721,
                "tip": 16903,
                "ubertip": 31814,
                "revivetip": 20807,
                "awakentip": 16902
            },
            "hotkey": "E"
        },
        # 3. Alexstrasza (Red Aspect) - Base Form
        {
            "id": "N046",
            "name": "|cffe4cfa3Алекстраза|r",
            "propernames": "Алекстраза",
            "tip": "|cffe4cfa3Алекстраза|r (|cffffffffZ|r)",
            "revivetip": "|cffe4cfa3Алекстраза|r",
            "awakentip": "|cffe4cfa3Алекстраза|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Королева драконов и аспект красной стаи, хранительница всего живого в Азероте. "
                "Обрушивает на недругов шквалы очищающего огня, оглушает огненными стрелами и поражает множество целей одновременно.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму красного дракона|n"
                "- |cffa9c7deОгненный ливень|cffced4da: обрушивает волны пламени по площади|n"
                "- |cffa9c7deВозмездие пламени|cffced4da: поражает потоками огня ближайших врагов|n"
                "- |cffa9c7deОгненная стрела|cffced4da: наносит урон и оглушает вражескую цель|n"
                "- |cffa9c7deПожар|cffced4da: позволяет временно атаковать до |cffffffff11|cffced4da целей одновременно.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 6800,
                "propernames": 15591,
                "tip": 16631,
                "ubertip": 31808,
                "revivetip": 15543,
                "awakentip": 16630
            },
            "hotkey": "Z"
        },
        # 3b. Alexstrasza - Dragon Form
        {
            "id": "N048",
            "name": "|cffe4cfa3Алекстраза|r",
            "propernames": "Алекстраза",
            "tip": "|cffe4cfa3Алекстраза|r",
            "revivetip": "|cffe4cfa3Алекстраза|r",
            "awakentip": "|cffe4cfa3Алекстраза|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Королева драконов и аспект красной стаи, хранительница всего живого в Азероте. "
                "Обрушивает на недругов шквалы очищающего огня, оглушает огненными стрелами и поражает множество целей одновременно.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму красного дракона|n"
                "- |cffa9c7deОгненный ливень|cffced4da: обрушивает волны пламени по площади|n"
                "- |cffa9c7deВозмездие пламени|cffced4da: поражает потоками огня ближайших врагов|n"
                "- |cffa9c7deОгненная стрела|cffced4da: наносит урон и оглушает вражескую цель|n"
                "- |cffa9c7deПожар|cffced4da: позволяет временно атаковать до |cffffffff11|cffced4da целей одновременно.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 16385,
                "propernames": 20516,
                "tip": 16876,
                "ubertip": 31811,
                "revivetip": 15569,
                "awakentip": 16875
            },
            "hotkey": "E"
        },
        # 4. Malygos (Blue Aspect) - Base Form
        {
            "id": "N045",
            "name": "|cffe4cfa3Малигос|r",
            "propernames": "Малигос",
            "tip": "|cffe4cfa3Малигос|r (|cffffffffZ|r)",
            "revivetip": "|cffe4cfa3Малигос|r",
            "awakentip": "|cffe4cfa3Малигос|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Хранитель Магии и верховный аспект синей стаи. "
                "Повелевает астральными силами, обрушивает искры чистой тайной магии, питает союзников маной и поглощает чужие заклинания.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму синего дракона|n"
                "- |cffa9c7deПоле астрала|cffced4da: переводит всех юнитов в выбранной области в астрал|n"
                "- |cffa9c7deИскры мощи|cffced4da: обстреливает область сгустками маны, оглушая врагов|n"
                "- |cffa9c7deВладыка магии|cffced4da: аура, ускоряющая восстановление маны союзников|n"
                "- |cffa9c7deПожирание магии|cffced4da: поглощает чары в области, восстанавливая здоровье и ману.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 25201,
                "propernames": 25202,
                "tip": 25204,
                "ubertip": 31807,
                "revivetip": 25205,
                "awakentip": 25203
            },
            "hotkey": "Z"
        },
        # 4b. Malygos - Dragon Form
        {
            "id": "N04A",
            "name": "|cffe4cfa3Малигос|r",
            "propernames": "Малигос",
            "tip": "|cffe4cfa3Малигос|r",
            "revivetip": "|cffe4cfa3Малигос|r",
            "awakentip": "|cffe4cfa3Малигос|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Хранитель Магии и верховный аспект синей стаи. "
                "Повелевает астральными силами, обрушивает искры чистой тайной магии, питает союзников маной и поглощает чужие заклинания.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОблик дракона|cffced4da: принимает истинную форму синего дракона|n"
                "- |cffa9c7deПоле астрала|cffced4da: переводит всех юнитов в выбранной области в астрал|n"
                "- |cffa9c7deИскры мощи|cffced4da: обстреливает область сгустками маны, оглушая врагов|n"
                "- |cffa9c7deВладыка магии|cffced4da: аура, ускоряющая восстановление маны союзников|n"
                "- |cffa9c7deПожирание магии|cffced4da: поглощает чары в области, восстанавливая здоровье и ману.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {
                "name": 25588,
                "propernames": 25590,
                "tip": 25594,
                "ubertip": 31813,
                "revivetip": 25596,
                "awakentip": 25592
            },
            "hotkey": "E"
        }
    ]

    # Update WTS
    updated_wts = original_wts
    wts_changed_ids = []
    fields_list = ["name", "propernames", "tip", "ubertip", "revivetip", "awakentip"]
    for h in heroes_data:
        for f in fields_list:
            string_id = h["wts"][f]
            updated_wts = update_wts_string(updated_wts, string_id, h[f])
            wts_changed_ids.append(string_id)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    hero_ids = [h["id"] for h in heroes_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(hero_ids), "--fields", ",".join(fields_list)] + hd_flag))
        wts_dict = hw.load_wts_strings()
        resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}
        for h in heroes_data:
            fields = objects_by_id.get(h["id"], {})
            for f in fields_list:
                actual_val = resolve(fields.get(f, ""))
                expected_val = h[f]
                assert actual_val == expected_val, f"Mismatch for {h['id']}.{f} (hd={hd}): '{actual_val}' != '{expected_val}'"

            checks.append({"id": h["id"], "variant": "HD" if hd else "SD", "fields_verified": fields_list})

    # Save artifacts
    heroes_artifact = {
        "race": "Dragon",
        "category": "heroes",
        "total_hero_objects": len(heroes_data),
        "heroes": heroes_data
    }
    (folder / "dragon_heroes.json").write_text(json.dumps(heroes_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Dragon",
        "category": "heroes",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "binary_hashes_before": binary_hashes,
        "checks": checks
    }
    (folder / "dragon_heroes_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(heroes_data)} Dragon hero objects ({len(wts_changed_ids)} WTS keys).")
    print(f"Verified {len(checks)} SD/HD object checks.")

if __name__ == "__main__":
    main()
