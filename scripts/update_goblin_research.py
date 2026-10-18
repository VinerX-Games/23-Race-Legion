# -*- coding: utf-8 -*-
"""Update Goblins race researches (20 researches, 96 levels, 288 fields) with complete SD validation."""
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
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

# Helper function to generate 6-level standard research values
def make_6_level_research(rid, name, hotkey, effect_desc_func, affects_list, total_levels=6):
    res = {
        "id": rid,
        "name": f"|cffe4cfa3{name}|r",
        "hotkey": hotkey,
        "maxlevel": total_levels,
        "values": {}
    }
    affects_str = "|n".join([f"- |cffa9c7de{u}|cffced4da" for u in affects_list])
    for lvl in range(1, total_levels + 1):
        eff = effect_desc_func(lvl)
        res["values"][f"name{lvl}"] = f"|cffe4cfa3{name}|r — уровень |cffffffff{lvl}|r"
        res["values"][f"tip{lvl}"] = f"|cffe4cfa3{name}|r — уровень |cffffffff{lvl}|r (|cffffffff{hotkey}|r)"
        res["values"][f"ubertip{lvl}"] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da {eff}|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n{affects_str}.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/{total_levels}|cffced4da.|r"
        )
    return res

# Definitions of all 20 Goblin researches
RESEARCHES = [
    # ========================================================
    # 1. Base (h070): R0D4 Расширить банковский сектор (2 levels)
    # ========================================================
    {
        "id": "R0D4",
        "name": "|cffe4cfa3Банковский сектор|r",
        "hotkey": "Z",
        "maxlevel": 2,
        "values": {
            "name1": "|cffe4cfa3Банковский сектор|r — ступень |cffffffff1|r",
            "tip1": "|cffe4cfa3Банковский сектор|r — ступень |cffffffff1|r (|cffffffffZ|r)",
            "ubertip1": (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Расширяет финансовую инфраструктуру картеля, "
                "увеличивая лимит доступных банков до уровня |cffffffffТ2|cffced4da.|n|n"
                "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deБанк|cffced4da.|n|n"
                "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
            ),
            "name2": "|cffe4cfa3Банковский сектор|r — ступень |cffffffff2|r",
            "tip2": "|cffe4cfa3Банковский сектор|r — ступень |cffffffff2|r (|cffffffffZ|r)",
            "ubertip2": (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Завершает формирование финансовой сети картеля, "
                "увеличивая лимит доступных банков до максимального уровня |cffffffffТ3|cffced4da.|n|n"
                "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deБанк|cffced4da.|n|n"
                "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
            )
        }
    },

    # ========================================================
    # 2-11. Laboratory (h076): 10 core military researches (6 levels each)
    # ========================================================
    # 2. R04P Биологические эксперименты
    make_6_level_research(
        "R04P", "Биологические эксперименты", "F",
        lambda lvl: f"Увеличивает максимальный запас здоровья пехотинцев на |cffffffff+{lvl * 4}%|cffced4da. Не действует на технику и механизмы.",
        [
            "Рекрут ТК", "Пулеметчик", "Снайпер", "Ракетчик", "Медик",
            "Огнеметчик", "Сапер", "Огр-Костолом", "Супербоец"
        ]
    ),

    # 3. R04E Пули
    make_6_level_research(
        "R04E", "Пули", "Q",
        lambda lvl: f"Увеличивает урон боевых единиц, вооружённых огнестрельным пулевым оружием, на |cffffffff+{lvl * 2}|cffced4da ед.",
        [
            "Рекрут ТК", "Пулеметчик", "Снайпер", "Вездеход «Мурлок-3000»",
            "Супербоец", "Вездеход-амфибия"
        ]
    ),

    # 4. R04F Ракеты
    make_6_level_research(
        "R04F", "Ракеты", "E",
        lambda lvl: f"Увеличивает урон боевых единиц, оснащённых ракетным вооружением, на |cffffffff+{lvl * 4}|cffced4da ед.",
        [
            "Ракетчик", "Сапер", "БРДМ-2000", "Штурмовой танк «Вепрь-5000»",
            "Мобильная артиллерия", "Субмарина", "Универсальный линкор"
        ]
    ),

    # 5. R04G Огнеметы
    make_6_level_research(
        "R04G", "Огнеметы", "W",
        lambda lvl: f"Увеличивает урон боевых единиц, использующих огнемёты и зажигательные смеси, на |cffffffff+{lvl * 3}|cffced4da ед.",
        [
            "Огнеметчик", "Огнестрельный танк «Напалм-4000»", "Огнемеха «Пожар-7000»"
        ]
    ),

    # 6. R04H Ударные механизмы
    make_6_level_research(
        "R04H", "Ударные механизмы", "A",
        lambda lvl: f"Увеличивает урон боевых единиц, сражающихся в ближнем бою при помощи гидравлических кулаков, на |cffffffff+{lvl * 5}|cffced4da ед.",
        [
            "Меха «Линчеватель-6000»", "Оператор силовой брони"
        ]
    ),

    # 7. R04I Моторы
    make_6_level_research(
        "R04I", "Моторы", "D",
        lambda lvl: f"Увеличивает скорость передвижения всей боевой техники и флота картеля на |cffffffff+{lvl * 3}%|cffced4da.",
        [
            "БРДМ-2000", "Вездеход «Мурлок-3000»", "Огнестрельный танк «Напалм-4000»",
            "Штурмовой танк «Вепрь-5000»", "Мобильная артиллерия", "Универсальный линкор",
            "Субмарина", "Подводная лодка", "Нефтяной танкер"
        ]
    ),

    # 8. R04J Подвижные механизмы
    make_6_level_research(
        "R04J", "Подвижные механизмы", "S",
        lambda lvl: f"Увеличивает скорость атаки шагающих механизмов и бойцов в силовой броне на |cffffffff+{lvl * 3}%|cffced4da.",
        [
            "Меха «Линчеватель-6000»", "Огнемеха «Пожар-7000»",
            "Оператор силовой брони", "Супербоец"
        ]
    ),

    # 9. R04K Легкая обшивка
    make_6_level_research(
        "R04K", "Легкая обшивка", "Z",
        lambda lvl: f"Увеличивает показатель защиты пехотинцев на |cffffffff+{lvl}|cffced4da ед. брони.",
        [
            "Рекрут ТК", "Пулеметчик", "Снайпер", "Ракетчик",
            "Медик", "Огнеметчик", "Сапер", "Огр-Костолом"
        ]
    ),

    # 10. R04L Тяжелая обшивка
    make_6_level_research(
        "R04L", "Тяжелая обшивка", "X",
        lambda lvl: f"Увеличивает показатель защиты техники, мехов, кораблей и бойцов в силовой броне на |cffffffff+{lvl}|cffced4da ед. брони.",
        [
            "БРДМ-2000", "Вездеход «Мурлок-3000»", "Огнестрельный танк «Напалм-4000»",
            "Штурмовой танк «Вепрь-5000»", "Мобильная артиллерия", "Меха «Линчеватель-6000»",
            "Огнемеха «Пожар-7000»", "Оператор силовой брони", "Супербоец",
            "Универсальный линкор", "Субмарина", "Подводная лодка"
        ]
    ),

    # 11. R04M Увеличительная оптика
    make_6_level_research(
        "R04M", "Увеличительная оптика", "C",
        lambda lvl: f"Увеличивает дальность атаки дальнобойных стрелков и артиллерии картеля на |cffffffff+{lvl * 50}|cffced4da ед.",
        [
            "Снайпер", "Мобильная артиллерия"
        ]
    ),

    # ========================================================
    # 12-20. Bureau of Developments (h079): 9 upgrades
    # ========================================================
    # 12. R056 Ускорение (1 level)
    {
        "id": "R056",
        "name": "|cffe4cfa3Ускорение|r",
        "hotkey": "E",
        "maxlevel": 1,
        "values": {
            "name1": "|cffe4cfa3Ускорение|r",
            "tip1": "|cffe4cfa3Ускорение|r (|cffffffffE|r)",
            "ubertip1": (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Ускорение» у бронетехники, "
                "позволяющую кратковременно повысить скорость передвижения ценой увеличенного получаемого урона.|n|n"
                "|cffa6afb8Затрагивает:|cffced4da|n"
                "- |cffa9c7deБРДМ-2000|cffced4da|n"
                "- |cffa9c7deОгнестрельный танк «Напалм-4000»|cffced4da|n"
                "- |cffa9c7deШтурмовой танк «Вепрь-5000»|cffced4da.|r"
            )
        }
    },

    # 13. R07A Коктейль Молотова (1 level)
    {
        "id": "R07A",
        "name": "|cffe4cfa3Коктейль Молотова|r",
        "hotkey": "W",
        "maxlevel": 1,
        "values": {
            "name1": "|cffe4cfa3Коктейль Молотова|r",
            "tip1": "|cffe4cfa3Коктейль Молотова|r (|cffffffffW|r)",
            "ubertip1": (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет рекрутам бросать зажигательные смеси, "
                "создающие область огня и наносящие периодический урон наземным войскам.|n|n"
                "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deРекрут ТК|cffced4da.|r"
            )
        }
    },

    # 14. R05X ЭМИ-граната (1 level)
    {
        "id": "R05X",
        "name": "|cffe4cfa3ЭМИ-граната|r",
        "hotkey": "Z",
        "maxlevel": 1,
        "values": {
            "name1": "|cffe4cfa3ЭМИ-граната|r",
            "tip1": "|cffe4cfa3ЭМИ-граната|r (|cffffffffZ|r)",
            "ubertip1": (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «ЭМИ-граната» у супербойцов, "
                "рассеивающую заклинания и наносящую урон призванным существам.|n|n"
                "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deСупербоец|cffced4da.|r"
            )
        }
    },

    # 15. R05Y Адреналиновые инъекции (1 level)
    {
        "id": "R05Y",
        "name": "|cffe4cfa3Адреналиновые инъекции|r",
        "hotkey": "X",
        "maxlevel": 1,
        "values": {
            "name1": "|cffe4cfa3Адреналиновые инъекции|r",
            "tip1": "|cffe4cfa3Адреналиновые инъекции|r (|cffffffffX|r)",
            "ubertip1": (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Адреналиновые инъекции» у супербойцов, "
                "позволяющую повысить боевые характеристики за счёт здоровья.|n|n"
                "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deСупербоец|cffced4da.|r"
            )
        }
    },

    # 16. R04N Стандарты потребления (6 levels)
    make_6_level_research(
        "R04N", "Стандарты потребления", "F",
        lambda lvl: f"Снижает штрафное потребление топлива и ресурсов у боевой техники картеля на |cffffffff{lvl}|cffced4da ступень.",
        [
            "БРДМ-2000", "Вездеход «Мурлок-3000»", "Огнестрельный танк «Напалм-4000»",
            "Штурмовой танк «Вепрь-5000»", "Мобильная артиллерия", "Меха «Линчеватель-6000»",
            "Огнемеха «Пожар-7000»"
        ]
    ),

    # 17. R04Q Безопасность ракет (6 levels)
    make_6_level_research(
        "R04Q", "Безопасность ракет", "D",
        lambda lvl: f"Снижает риск детонации боеприпасов в ракетных пусковых установках на |cffffffff{lvl}|cffced4da ступень.",
        [
            "Ракетчик", "БРДМ-2000", "Штурмовой танк «Вепрь-5000»",
            "Мобильная артиллерия", "Субмарина", "Подводная лодка"
        ]
    ),

    # 18. R04R Безопасность огнеметов (6 levels)
    make_6_level_research(
        "R04R", "Безопасность огнеметов", "S",
        lambda lvl: f"Снижает риск самовозгорания горючей смеси при стрельбе огнемётов на |cffffffff{lvl}|cffced4da ступень.",
        [
            "Огнеметчик", "Огнестрельный танк «Напалм-4000»", "Огнемеха «Пожар-7000»"
        ]
    ),

    # 19. R05W Качество боеприпасов (6 levels)
    make_6_level_research(
        "R05W", "Качество боеприпасов", "A",
        lambda lvl: f"Снижает вероятность брака патронов и осечек при стрельбе на |cffffffff{lvl}|cffced4da ступень.",
        [
            "Рекрут ТК", "Пулеметчик", "Вездеход «Мурлок-3000»", "Супербоец"
        ]
    ),

    # 20. R053 Улучшенные пилы (6 levels)
    make_6_level_research(
        "R053", "Улучшенные пилы", "Q",
        lambda lvl: f"Увеличивает объём древесины, переносимой рабочими механизмами, на |cffffffff+{lvl * 6}|cffced4da ед.",
        [
            "Крошшер"
        ]
    )
]

def main():
    folder = ROOT / "docs" / "ui_text"
    source = ROOT / "map.w3x"
    wts_file = source / "war3map.wts"
    w3q_skin_file = source / "war3mapSkin.w3q"

    # Backup original hashes
    original_wts_hash = hashlib.sha256(wts_file.read_bytes()).hexdigest()
    original_w3q_skin_hash = hashlib.sha256(w3q_skin_file.read_bytes()).hexdigest()

    # Base binaries must remain untouched
    base_binaries = [
        "war3map.w3u", "war3map.w3t", "war3map.w3a", "war3map.w3b",
        "war3map.w3d", "war3map.w3q", "war3map.w3h"
    ]
    other_binary_hashes = {
        name: hashlib.sha256((source / name).read_bytes()).hexdigest()
        for name in base_binaries
        if (source / name).exists()
    }

    # Load fields mapping from generate_research_fields_map.py
    fields_map_file = folder / "goblins_research_fields_map.json"
    if not fields_map_file.exists():
        print("Fields map not found, run scripts/generate_research_fields_map.py first.")
        sys.exit(1)
    fields_map = json.loads(fields_map_file.read_text(encoding="utf-8"))

    wts_content = wts_file.read_text(encoding="utf-8")
    wts_changed = {}
    skin_w3q_ops = []

    for r in RESEARCHES:
        rid = r["id"]
        finfo = fields_map.get(rid, {})
        for field, target_val in r["values"].items():
            info = finfo.get(field, {})
            wts_id = info.get("wts_id")
            is_shared = info.get("is_shared", True)

            # If unique WTS string, update directly in war3map.wts
            if wts_id is not None and not is_shared:
                wts_content = update_wts_string(wts_content, wts_id, target_val)
                wts_changed[wts_id] = target_val
            else:
                # Shared WTS or inline field -> patch into war3mapSkin.w3q
                skin_w3q_ops.append({
                    "id": rid,
                    "field": field,
                    "value": target_val
                })

    print(f"Total WTS strings to update: {len(wts_changed)}")
    print(f"Total war3mapSkin.w3q ops: {len(skin_w3q_ops)}")

    # Write updated WTS
    wts_file.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_file.read_bytes()).hexdigest()
    print(f"WTS updated: {original_wts_hash[:8]} -> {new_wts_hash[:8]}")

    # Patch war3mapSkin.w3q
    if skin_w3q_ops:
        patched_w3q, changed_w3q = patch_blob(
            w3q_skin_file.read_bytes(), skin_w3q_ops, "upgrade", add_missing=True
        )
        w3q_skin_file.write_bytes(patched_w3q)
        new_w3q_skin_hash = hashlib.sha256(patched_w3q).hexdigest()
        print(f"war3mapSkin.w3q updated with {len(changed_w3q)} mods: {original_w3q_skin_hash[:8]} -> {new_w3q_skin_hash[:8]}")
    else:
        new_w3q_skin_hash = original_w3q_skin_hash

    # Readback checks in SD mode ONLY (User instruction: SD only, no HD)
    res_ids = [r["id"] for r in RESEARCHES]
    bulk = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(res_ids)]))

    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    objects = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

    checks = []
    mismatches = []

    for r in RESEARCHES:
        rid = r["id"]
        fields = objects.get(rid, {})
        for f, expected in r["values"].items():
            actual = resolve(fields.get(f, ""))
            matched = (actual == expected)
            checks.append({
                "id": rid,
                "field": f,
                "matched": matched,
                "expected": expected,
                "actual": actual
            })
            if not matched:
                mismatches.append((rid, f, expected, actual))

    print(f"\nSD readback validation: {len(checks) - len(mismatches)}/{len(checks)} fields matched.")
    if mismatches:
        print(f"FAILED: {len(mismatches)} mismatches:")
        for rid, f, exp, act in mismatches:
            print(f"  [{rid}] {f}:\n    Expected: {repr(exp)}\n    Actual:   {repr(act)}")
        sys.exit(1)

    # Save application report and registry
    apply_report = {
        "race": "goblins",
        "category": "researches",
        "total_researches": len(RESEARCHES),
        "total_checks": len(checks),
        "all_matched": len(mismatches) == 0,
        "wts_keys_updated": len(wts_changed),
        "skin_w3q_ops": len(skin_w3q_ops),
        "hashes": {
            "wts": {"before": original_wts_hash, "after": new_wts_hash},
            "w3q_skin": {"before": original_w3q_skin_hash, "after": new_w3q_skin_hash}
        },
        "base_binaries_untouched": all(
            hashlib.sha256((source / name).read_bytes()).hexdigest() == h
            for name, h in other_binary_hashes.items()
        )
    }

    (folder / "goblins_research_apply.json").write_text(
        json.dumps(apply_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (folder / "goblins_research.json").write_text(
        json.dumps(RESEARCHES, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Report saved to docs/ui_text/goblins_research_apply.json")
    print("Registry saved to docs/ui_text/goblins_research.json")
    print("All 20 Goblin researches successfully validated in SD mode!")

if __name__ == "__main__":
    main()
