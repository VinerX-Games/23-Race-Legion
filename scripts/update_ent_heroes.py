# -*- coding: utf-8 -*-
"""Update Ents (Argvinol) race heroes (3 heroes, 18 fields) with complete SD/HD validation."""
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
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name != "war3map.wts"
    }

    heroes_data = [
        {
            "id": "E02S",
            "name": "|cffe4cfa3Лесной Смотритель|r",
            "propernames": "|cffe4cfa3Ядрин Леший|r",
            "tip": "|cffe4cfa3Лесной Смотритель|r (|cffffffffC|r)",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Могучий лесной хранитель ближнего боя, отражающий вражеские атаки "
                "шипастой аурой и сокрушающий врагов живой силой леса.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deТернистый куст|cffced4da: оглушает врагов и наносит урон по линии удара.|n"
                "- |cffa9c7deАура шипов|cffced4da: отражает часть входящего урона ближнего боя обратно в атакующего.|n"
                "- |cffa9c7deРассекающий удар|cffced4da: базовые атаки наносят урон окружающим вражеским бойцам.|n"
                "- |cffa9c7deДух Леса|cffced4da: призывает могучую аватару возмездия, поднимающую неуязвимых духов из трупов.|n|n"
                "|cffa6afb8Атакует:|cffced4da только наземные цели.|r"
            ),
            "revivetip": "Воскресить |cffe4cfa3Лесной Смотритель|r (|cffffffffC|r)",
            "awakentip": "Оживить |cffe4cfa3Лесной Смотритель|r (|cffffffffC|r)",
            "wts": {
                "name": 41643,
                "propernames": 15684,
                "tip": 41646,
                "ubertip": 21271,
                "revivetip": 41647,
                "awakentip": 41645
            },
            "hotkey": "C",
            "primary": "STR"
        },
        {
            "id": "E02Q",
            "name": "|cffe4cfa3Дух леса|r",
            "propernames": "|cffe4cfa3Ника|r,|cffe4cfa3Эсса Лесной Дух|r",
            "tip": "|cffe4cfa3Дух леса|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Магический дух поддержки дальнего боя, укрепляющий союзную армию "
                "аурами брони и регенерации и карающий врагов силами природы.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deСемя раздора|cffced4da: проращивает корни, наносящие цели периодический урон.|n"
                "- |cffa9c7deДревесная кора|cffced4da: повышает показатель защиты всех союзников поблизости.|n"
                "- |cffa9c7deВлияние леса|cffced4da: существенно ускоряет восстановление здоровья союзных войск.|n"
                "- |cffa9c7deКара леса|cffced4da: сотрясает землю мощным природным взрывом, наносящим урон по площади.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели.|r"
            ),
            "revivetip": "Воскресить |cffe4cfa3Дух леса|r (|cffffffffZ|r)",
            "awakentip": "Оживить |cffe4cfa3Дух леса|r (|cffffffffZ|r)",
            "wts": {
                "name": 41633,
                "propernames": 13304,
                "tip": 41636,
                "ubertip": 21268,
                "revivetip": 41637,
                "awakentip": 41635
            },
            "hotkey": "Z",
            "primary": "INT"
        },
        {
            "id": "E02R",
            "name": "|cffe4cfa3Егерь диколесья|r",
            "propernames": "|cffe4cfa3Катрин Лесная Песня|r",
            "tip": "|cffe4cfa3Егерь диколесья|r (|cffffffffX|r)",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Быстрый стрелок дальнего боя, усиливающий стрелков союзной армии, "
                "отравляющий врагов и призывающий древней из чащи.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОтравленное оружие|cffced4da: стрелы наносят цели периодический урон ядом.|n"
                "- |cffa9c7deЗов Древних|cffced4da: призывает древней для сражения на передовой линии.|n"
                "- |cffa9c7deАура меткости|cffced4da: повышает силу дистанционных атак находящихся рядом союзников.|n"
                "- |cffa9c7deКорни мира|cffced4da: сковывает врагов корнями и взращивает отряд лесных защитников.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели.|r"
            ),
            "revivetip": "Воскресить |cffe4cfa3Егерь диколесья|r (|cffffffffX|r)",
            "awakentip": "Оживить |cffe4cfa3Егерь диколесья|r (|cffffffffX|r)",
            "wts": {
                "name": 41638,
                "propernames": 13416,
                "tip": 41641,
                "ubertip": 21269,
                "revivetip": 41642,
                "awakentip": 41640
            },
            "hotkey": "X",
            "primary": "AGI"
        }
    ]

    # Update WTS strings
    new_wts = original_wts
    wts_changed_ids = []

    fields_to_update = ["name", "propernames", "tip", "ubertip", "revivetip", "awakentip"]

    for h in heroes_data:
        w = h["wts"]
        for f in fields_to_update:
            new_wts = update_wts_string(new_wts, w[f], h[f])
            wts_changed_ids.append(w[f])

    wts_path.write_text(new_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Reset cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()

    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Readback checks in SD and HD
    checks = []
    hero_ids = [h["id"] for h in heroes_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(hero_ids), "--fields", "name,propernames,tip,ubertip,revivetip,awakentip"] + hd_flag))
        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

        for h in heroes_data:
            fields = objects_by_id.get(h["id"], {})
            for f in fields_to_update:
                actual = resolve(fields.get(f, ""))
                expected = h[f]
                assert actual == expected, f"{f} mismatch for {h['id']} (hd={hd}):\nActual: '{actual}'\nExpected: '{expected}'"

            checks.append({
                "id": h["id"],
                "variant": "HD" if hd else "SD",
                "fields_verified": fields_to_update
            })

    # Verify other binary files remain untouched
    for name, expected_hash in other_binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    registry = {
        "race": "Ents",
        "category": "heroes",
        "total_heroes": len(heroes_data),
        "heroes": heroes_data
    }
    (folder / "ent_heroes.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Ents",
        "category": "heroes",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "ent_heroes_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(heroes_data)} Ent heroes.")
    print(f"Updated {len(set(wts_changed_ids))} WTS keys.")
    print(f"Verified {len(checks)} SD/HD object checks ({len(checks)*6} field values).")

if __name__ == "__main__":
    main()
