# -*- coding: utf-8 -*-
"""Update Demon race units with complete SD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw

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

    # 15 units, 45 WTS strings
    wts_updates = {
        # e02Y: Архитектор Скверны
        19471: "|cffe4cfa3Архитектор Скверны|r",
        19472: "|cffe4cfa3Архитектор Скверны|r (|cffffffffQ|r)",
        31821: "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Легиона. Добывает золото и древесину, возводит и ремонтирует демонические строения, а также способен собрать осадного Скверно-бота.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРемонт|cffced4da: восстанавливает прочность повреждённых зданий и механизмов.|n|nНе атакует.|r",

        # u026: Архитектор Скверны
        13222: "|cffe4cfa3Архитектор Скверны|r",
        13223: "|cffe4cfa3Архитектор Скверны|r (|cffffffffQ|r)",
        31734: "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Легиона. Добывает ресурсы, возводит и ремонтирует строения Скверны.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРемонт|cffced4da: восстанавливает прочность повреждённых зданий и механизмов.|n|nАтакует наземные цели.|r",

        # n025: Властитель
        13193: "|cffe4cfa3Властитель|r",
        13194: "|cffe4cfa3Властитель|r (|cffffffffW|r)",
        42225: "|cffa6afb8ЮНИТ:|cffced4da Базовый штурмовой воин Легиона ближнего боя. Наносит урон типа Хаос и способен эволюционировать в более свирепые формы демонов.|n|nАтакует наземные цели.|r",

        # n026: Кровавый Палач
        13280: "|cffe4cfa3Кровавый Палач|r",
        13281: "|cffe4cfa3Кровавый Палач|r (|cffffffffW|r)",
        42226: "|cffa6afb8ЮНИТ:|cffced4da Закалённый в битвах воин Легиона (вторая форма эволюции). Обладает повышенным здоровьем, сокрушительной атакой Хаоса и способен трансформироваться далее.|n|nАтакует наземные цели.|r",

        # n02D: Кровавое отродье
        13195: "|cffe4cfa3Кровавое отродье|r",
        13197: "|cffe4cfa3Кровавое отродье|r (|cffffffffW|r)",
        42314: "|cffa6afb8ЮНИТ:|cffced4da Элитный штурмовик Легиона (третья форма эволюции). Рассекает вражеские ряды ударами глефы и готов к финальной мутации.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: наносит сплэш-урон ближайшим противникам при каждой атаке.|n|nАтакует наземные цели.|r",

        # n02E: Кровопускатель
        13289: "|cffe4cfa3Кровопускатель|r",
        13291: "|cffe4cfa3Кровопускатель|r (|cffffffffW|r)",
        42315: "|cffa6afb8ЮНИТ:|cffced4da Высший воин авангарда Легиона (финальная форма эволюции). Вооружён массивным осквернённым щитом и секирой, сокрушающей скопления противников.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: поражает нескольких врагов одновременно мощным ударом.|n- |cffa9c7deУкрыться за щитом|cffced4da: снижает получаемый урон от дальних атак за счёт скорости бега.|n|nАтакует наземные цели.|r",

        # n023: Зверь Скверны
        13187: "|cffe4cfa3Зверь Скверны|r",
        13188: "|cffe4cfa3Зверь Скверны|r (|cffffffffQ|r)",
        40473: "|cffa6afb8ЮНИТ:|cffced4da Свирепый боевой хищник Легиона. Отличается стремительной скоростью передвижения и частыми атаками Хаоса, преследуя отступающих врагов.|n|nАтакует наземные цели.|r",

        # n027: Мо'агр
        13313: "|cffe4cfa3Мо'агр|r",
        13314: "|cffe4cfa3Мо'агр|r (|cffffffffE|r)",
        42311: "|cffa6afb8ЮНИТ:|cffced4da Массивный демонический боец ближнего боя. Обладает огромным запасом здоровья и оглушает цели сокрушительными ударами палицы.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСильный удар|cffced4da: шанс оглушить цель и нанести дополнительный урон.|n|nАтакует наземные цели.|r",

        # n02I: Адская колесница
        13328: "|cffe4cfa3Адская колесница|r",
        13329: "|cffe4cfa3Адская колесница|r (|cffffffffR|r)",
        42316: "|cffa6afb8ЮНИТ:|cffced4da Тяжёлая осадная машина Пылающего Легиона. Обстреливает укрепления и вражеские скопления снарядами с колоссальным осадным уроном на большой дистанции.|n|nАтакует наземные и воздушные цели.|r",

        # n020: Эредар-колдун
        13086: "|cffe4cfa3Эредар-колдун|r",
        13087: "|cffe4cfa3Эредар-колдун|r (|cffffffffQ|r)",
        38406: "|cffa6afb8ЮНИТ:|cffced4da Искусный чернокнижник эредаров. Поражает противников магией Скверны, вытягивает жизненные силы и проклинает вражеские отряды.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПерст боли|cffced4da: поражает врага вспышкой тёмной молнии.|n- |cffa9c7deПохищение жизни|cffced4da: вытягивает здоровье вражеского воина.|n- |cffa9c7deПроклятие|cffced4da: вызывает промахи у атакуемой цели.|n|nАтакует наземные и воздушные цели.|r",

        # n028: Демон-тюремщик
        13326: "|cffe4cfa3Демон-тюремщик|r",
        13327: "|cffe4cfa3Демон-тюремщик|r (|cffffffffW|r)",
        42312: "|cffa6afb8ЮНИТ:|cffced4da Жестокий палач и тюремщик Легиона. Специализируется на подавлении контроля, пленении одиночных воинов и расстройстве вражеских рядов.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПленение|cffced4da: захватывает вражеского воина внутрь переносной клетки.|n- |cffa9c7deСон|cffced4da: усыпляет противника, выводя его из боя.|n- |cffa9c7deЛовушка тюремщика|cffced4da: сковывает передвижение врагов тёмными путами.|n- |cffa9c7deРазрушение заклинаний|cffced4da: рассеивает магические эффекты.|n|nАтакует наземные и воздушные цели.|r",

        # n024: Ловчий Скверны
        13190: "|cffe4cfa3Ловчий Скверны|r",
        13191: "|cffe4cfa3Ловчий Скверны|r (|cffffffffQ|r)",
        40530: "|cffa6afb8ЮНИТ:|cffced4da Демонический гончий хищник, питающийся магической энергией. Идеален для нейтрализации вражеских заклинателей и героев.|n|nАтакует наземные цели.|r",

        # n022: Инфернал
        13184: "|cffe4cfa3Инфернал|r",
        13185: "|cffe4cfa3Инфернал|r (|cffffffffW|r)",
        39392: "|cffa6afb8ЮНИТ:|cffced4da Могучий осадный исполин из ожившего камня и пламени Скверны. Полностью невосприимчив к магии и непрерывно обжигает находящихся рядом наземных противников.|n|nАтакует наземные цели.|r",

        # n021: Страж ужаса
        13089: "|cffe4cfa3Страж ужаса|r",
        13182: "|cffe4cfa3Страж ужаса|r (|cffffffffE|r)",
        38407: "|cffa6afb8ЮНИТ:|cffced4da Элитный крылатый командир Легиона. Обрушивает на врагов огненный шквал, подавляет боевой дух неприятеля и воодушевляет союзные отряды.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненный ливень|cffced4da: накрывает область волнами пылающего огня.|n- |cffa9c7deАура страха|cffced4da: снижает урон атакующих врагов вокруг.|n- |cffa9c7deАура Скверны|cffced4da: повышает скорость бега и регенерацию союзников.|n|nАтакует наземные цели.|r",

        # n029: Скверно-бот
        13225: "|cffe4cfa3Скверно-бот|r",
        13227: "|cffe4cfa3Скверно-бот|r (|cffffffffX|r)",
        42313: "|cffa6afb8ЮНИТ:|cffced4da Исполинский осадный конструкт архитекторов Скверны. Обладает гигантским запасом прочности, наносит сокрушительный круговой урон Хаоса и может служить подвижным укреплением для пехоты.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: поражает скопления наземных врагов каждым ударом.|n- |cffa9c7deОбитаемый отсек|cffced4da: союзные стрелки могут вести огонь изнутри бота.|n|nАтакует наземные цели.|r",
    }

    print(f"Applying {len(wts_updates)} WTS updates for Demon units...")
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

    unit_map = [
        ("e02Y", 19471, 19472, 31821),
        ("u026", 13222, 13223, 31734),
        ("n025", 13193, 13194, 42225),
        ("n026", 13280, 13281, 42226),
        ("n02D", 13195, 13197, 42314),
        ("n02E", 13289, 13291, 42315),
        ("n023", 13187, 13188, 40473),
        ("n027", 13313, 13314, 42311),
        ("n02I", 13328, 13329, 42316),
        ("n020", 13086, 13087, 38406),
        ("n028", 13326, 13327, 42312),
        ("n024", 13190, 13191, 40530),
        ("n022", 13184, 13185, 39392),
        ("n021", 13089, 13182, 38407),
        ("n029", 13225, 13227, 42313),
    ]

    checks = []
    registry_units = []

    for uid, nid, tid, ubid in unit_map:
        args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", uid]
        res = hw.run_cli_json(args)
        if not res.get("ok"):
            raise RuntimeError(f"Failed to read {uid} via HiveWE: {res}")
        fields = res.get("object", {}) or res.get("fields", {})

        actual_name = resolve(fields.get("name"))
        actual_tip = resolve(fields.get("tip"))
        actual_ubertip = resolve(fields.get("ubertip"))

        name_ok = (actual_name == wts_updates[nid])
        tip_ok = (actual_tip == wts_updates[tid])
        ubertip_ok = (actual_ubertip == wts_updates[ubid])

        checks.append({"unit": uid, "field": "name", "expected": wts_updates[nid], "actual": actual_name, "ok": name_ok})
        checks.append({"unit": uid, "field": "tip", "expected": wts_updates[tid], "actual": actual_tip, "ok": tip_ok})
        checks.append({"unit": uid, "field": "ubertip", "expected": wts_updates[ubid], "actual": actual_ubertip, "ok": ubertip_ok})

        registry_units.append({
            "id": uid,
            "hotkey": resolve(fields.get("hotkey")),
            "name": {"wts_id": nid, "text": wts_updates[nid]},
            "tip": {"wts_id": tid, "text": wts_updates[tid]},
            "ubertip": {"wts_id": ubid, "text": wts_updates[ubid]},
        })

    all_ok = all(c["ok"] for c in checks)
    print(f"Verification checks passed: {sum(1 for c in checks if c['ok'])} / {len(checks)}")

    apply_payload = {
        "race": "Demons",
        "category": "Units",
        "units_count": len(unit_map),
        "fields_checked": len(checks),
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

    with open(folder / "demon_units_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Пылающий Легион (Demon): Категория 2 — Юниты (15 юнитов, 45 полей)",
        "units": registry_units
    }

    with open(folder / "demon_units.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
