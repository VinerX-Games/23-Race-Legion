# -*- coding: utf-8 -*-
"""Update all 10 Goblin buildings with full SD verification and registry artifacts."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

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
        # h070: База
        14143: "|cffe4cfa3База|r",
        14144: "|cffe4cfa3База|r (|cffffffffQ|r)",
        6490:  "|cffa6afb8ЗДАНИЕ:|cffced4da Главное командное и экономическое здание картеля. Служит складом ресурсов, даёт начальные припасы и позволяет объявить город столицей.|r|n|n|cffa6afb8Обучает:|r|n- |cffa9c7deКрошшер|r|n|n|cffa6afb8Исследования:|r|n- |cffa9c7deРасширить банковский сектор|r|n|n|cffa6afb8Особенности:|r|n|cffced4da- Столица: объявляет базу столицей государства.|r|n|cffced4da- Торговля: позволяет обменивать золото на древесину и древесину на золото.|r|n|cffced4da- Коррупция: позволяет регулировать уровень коррупции картеля.|r|n|cffced4da- Припасы: |cffffffff+50|r единиц.|r",

        # h077: Банк
        14153: "|cffe4cfa3Банк|r",
        14154: "|cffe4cfa3Банк|r (|cffffffffA|r)",
        20481: "|cffa6afb8ЗДАНИЕ:|cffced4da Финансовый центр картеля. Обеспечивает кланы припасами и генерирует стабильный доход для расширения империи.|r|n|n|cffa6afb8Особенности:|r|n|cffced4da- Доход: приносит |cffffffff+40|r золота каждые |cffffffff25|r с.|r|n|cffced4da- Припасы: |cffffffff+40|r единиц.|r",

        # h073: Казармы
        14145: "|cffe4cfa3Казармы|r",
        14146: "|cffe4cfa3Казармы|r (|cffffffffW|r)",
        11989: "|cffa6afb8ЗДАНИЕ:|cffced4da Тренировочный лагерь пехоты. Обучает регулярные стрелковые и штурмовые отряды, а также нанимает наёмных огров.|r|n|n|cffa6afb8Обучает:|r|n- |cffa9c7deРекрут ТК|r|n- |cffa9c7deПулеметчик|r|n- |cffa9c7deОгнеметчик|r|n- |cffa9c7deРакетчик|r|n- |cffa9c7deСнайпер|r|n- |cffa9c7deСапер|r|n- |cffa9c7deМедик|r|n|n|cffa6afb8Нанимает:|r|n- |cffa9c7deОгр-костолом|r",

        # h074: Завод
        14147: "|cffe4cfa3Завод|r",
        14148: "|cffe4cfa3Завод|r (|cffffffffD|r)",
        11990: "|cffa6afb8ЗДАНИЕ:|cffced4da Промышленный комплекс тяжелого машиностроения. Производит бронетехнику, амфибии и самоходную артиллерию.|r|n|n|cffa6afb8Обучает:|r|n- |cffa9c7deОгнестрельный танк «Напалм-4000»|r|n- |cffa9c7deВездеход «Мурлок-3000»|r|n- |cffa9c7deМобильная артиллерия|r|n- |cffa9c7deБРДМ-2000|r|n- |cffa9c7deШтурмовой танк «Вепрь-5000»|r",

        # h075: Фабрика
        14149: "|cffe4cfa3Фабрика|r",
        14150: "|cffe4cfa3Фабрика|r (|cffffffffF|r)",
        19556: "|cffa6afb8ЗДАНИЕ:|cffced4da Высокотехнологичное предприятие картеля. Производит шагающие боевые мехи и оснащает элитную штурмовую пехоту экзоскелетами.|r|n|n|cffa6afb8Обучает:|r|n- |cffa9c7deМеха «Линчеватель-6000»|r|n- |cffa9c7deОператор силовой брони|r|n- |cffa9c7deОгнемеха «Пожар-7000»|r|n- |cffa9c7deСупербоец|r",

        # h076: Лаборатория
        14151: "|cffe4cfa3Лаборатория|r",
        14152: "|cffe4cfa3Лаборатория|r (|cffffffffR|r)",
        20476: "|cffa6afb8ЗДАНИЕ:|cffced4da Научно-исследовательский комплекс. Разрабатывает новые виды вооружения и брони, открывающие доступ к продвинутым боевым единицам картеля.|r|n|n|cffa6afb8Исследования:|r|n- |cffa9c7deБиологические эксперименты|r|n- |cffa9c7deПули|r|n- |cffa9c7deРакеты|r|n- |cffa9c7deОгнеметы|r|n- |cffa9c7deУдарные механизмы|r|n- |cffa9c7deМоторы|r|n- |cffa9c7deПодвижные механизмы|r|n- |cffa9c7deЛегкая обшивка|r|n- |cffa9c7deТяжелая обшивка|r|n- |cffa9c7deУвеличительная оптика|r|n|n|cffa6afb8Особенности:|r|n|cffced4da- Обнаружение: проводит платную разведку указанной области карты.|r|n|cffced4da- Развитие технологий: количество действующих лабораторий определяет технологический уровень картеля.|r",

        # h079: Бюро разработок
        14157: "|cffe4cfa3Бюро разработок|r",
        14158: "|cffe4cfa3Бюро разработок|r (|cffffffffE|r)",
        20488: "|cffa6afb8ЗДАНИЕ:|cffced4da Конструкторское бюро и склад древесины. Создает специальные инженерные модификации и нестандартные боеприпасы для техники и пехоты.|r|n|n|cffa6afb8Исследования:|r|n- |cffa9c7deУскорение|r|n- |cffa9c7deКоктейль Молотова|r|n- |cffa9c7deЭМИ-граната|r|n- |cffa9c7deАдреналиновые инъекции|r|n- |cffa9c7deСтандарты потребления|r|n- |cffa9c7deСпецбоеприпасы ракет|r|n- |cffa9c7deСпецбоеприпасы огнеметов|r|n- |cffa9c7deУлучшенные пилы|r|n- |cffa9c7deСпецкалибр пуль|r|n|n|cffa6afb8Особенности:|r|n|cffced4da- Склад древесины: рабочие могут сдавать сюда заготовленное дерево.|r",

        # h07S: Турель
        14159: "|cffe4cfa3Турель|r",
        14160: "|cffe4cfa3Турель|r (|cffffffffZ|r)",
        20627: "|cffa6afb8ЗДАНИЕ:|cffced4da Автоматическая пулеметная турель. Обеспечивает базовую оборону базы и укрепленных позиций картеля.|r|n|n|cffa6afb8Атака:|cffced4da Дальний бой (прокалывающая), урон |cffffffff23-27|r, интервал |cffffffff1,5|r с.|r|n|cffced4daАтакует наземные и воздушные цели.|r",

        # o016: Алтарь Торговли
        14186: "|cffe4cfa3Алтарь Торговли|r",
        14187: "|cffe4cfa3Алтарь Торговли|r (|cffffffffS|r)",
        18417: "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище коммерции и наёмного контракта. Позволяет призывать уникальных лидеров гоблинов и возвращать к жизни павших героев.|r|n|n|cffa6afb8Обучает:|r|n- |cffa9c7deСпецназовец|r|n- |cffa9c7deАлхимик|r|n- |cffa9c7deМеханик|r|n|n|cffa6afb8Нанимает:|r|n- |cffa9c7deМаг телепортации|r|n|n|cffa6afb8Особенности:|r|n|cffced4da- Воскрешает павших героев.|r|n|cffced4da- Припасы: |cffffffff+3|r единицы.|r",

        # h0D7: Верфь
        14184: "|cffe4cfa3Верфь|r",
        14185: "|cffe4cfa3Верфь|r (|cffffffffC|r)",
        20646: "|cffa6afb8ЗДАНИЕ:|cffced4da Портовое сооружение картеля. Строит суда флота, подводные лодки и амфибии, а также ремонтирует корабли в доках.|r|n|n|cffa6afb8Обучает:|r|n- |cffa9c7deВездеход «Мурлок-3000»|r|n- |cffa9c7deУниверсальный линкор|r|n- |cffa9c7deСубмарина|r|n- |cffa9c7deПодводная лодка|r|n- |cffa9c7deНефтяной танкер|r|n|n|cffa6afb8Исследования:|r|n- |cffa9c7deПочинка|r|n|n|cffa6afb8Особенности:|r|n|cffced4da- Зона ремонта: пассивная аура восстанавливает |cffffffff2,5|r ед. прочности в секунду повреждённым союзным кораблям поблизости.|r",
    }

    print(f"Applying {len(wts_updates)} WTS updates for Goblin buildings...")
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

    bld_keys = {
        "h070": (14143, 14144, 6490),
        "h077": (14153, 14154, 20481),
        "h073": (14145, 14146, 11989),
        "h074": (14147, 14148, 11990),
        "h075": (14149, 14150, 19556),
        "h076": (14151, 14152, 20476),
        "h079": (14157, 14158, 20488),
        "h07S": (14159, 14160, 20627),
        "o016": (14186, 14187, 18417),
        "h0D7": (14184, 14185, 20646),
    }

    checks = []
    for bid, (nid, tid, uid) in bld_keys.items():
        res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", bid])
        if not res.get("ok"):
            raise RuntimeError(f"Failed to fetch {bid}: {res}")
        f = res.get("object", {}) or res.get("fields", {})
        actual_name = resolve(f.get("name"))
        actual_tip = resolve(f.get("tip"))
        actual_ubertip = resolve(f.get("ubertip"))

        n_ok = (actual_name == wts_updates[nid])
        t_ok = (actual_tip == wts_updates[tid])
        u_ok = (actual_ubertip == wts_updates[uid])

        checks.append({"id": bid, "field": "name", "expected": wts_updates[nid], "actual": actual_name, "ok": n_ok})
        checks.append({"id": bid, "field": "tip", "expected": wts_updates[tid], "actual": actual_tip, "ok": t_ok})
        checks.append({"id": bid, "field": "ubertip", "expected": wts_updates[uid], "actual": actual_ubertip, "ok": u_ok})

    all_ok = all(c["ok"] for c in checks)
    print(f"SD Verification checks: {sum(c['ok'] for c in checks)}/{len(checks)} passed.")
    for c in checks:
        if not c["ok"]:
            print(f"  MISMATCH on {c['id']} {c['field']}")

    apply_payload = {
        "race": "Goblins",
        "category": "buildings",
        "total_buildings": len(bld_keys),
        "total_fields": len(checks),
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

    with open(folder / "goblins_buildings_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Гоблины (Goblins): категория 1 — Здания (10 зданий)",
        "buildings_count": len(bld_keys),
        "variants": ["SD"],
        "buildings": [
            {
                "id": bid,
                "hotkey": resolve(hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", bid]).get("object", {}).get("hotkey")),
                "strings": [
                    {"field": "name", "wts_id": nid, "after": wts_updates[nid]},
                    {"field": "tip", "wts_id": tid, "after": wts_updates[tid]},
                    {"field": "ubertip", "wts_id": uid, "after": wts_updates[uid]}
                ]
            }
            for bid, (nid, tid, uid) in bld_keys.items()
        ]
    }

    with open(folder / "goblins_buildings.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
