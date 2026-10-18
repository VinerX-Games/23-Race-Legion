# -*- coding: utf-8 -*-
"""Update Demon race buildings with complete SD validation."""
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

    # 11 buildings, 33 WTS strings
    wts_updates = {
        # h0DS: Накопитель Скверны
        13204: "|cffe4cfa3Накопитель Скверны|r",
        13205: "|cffe4cfa3Накопитель Скверны|r (|cffffffffA|r)",
        31733: "|cffa6afb8ЗДАНИЕ:|cffced4da Хозяйственное строение Скверны. Обеспечивает армию Легиона припасами, увеличивая чистый базовый доход золота на |cffc8e08734|cffced4da за выплату (+40 от припасов за вычетом 6 за содержание строения).|n|nИтоговый доход зависит от текущих модификаторов экономики.|r",

        # h0DT: Генератор Скверны
        13208: "|cffe4cfa3Генератор Скверны|r",
        13209: "|cffe4cfa3Генератор Скверны|r (|cffffffffE|r)",
        19467: "|cffa6afb8ЗДАНИЕ:|cffced4da Магический источник Скверны. Поддерживает стабильность демонических сооружений насквозь пропитанной порчей энергией.|n|n|cffa6afb8Особенности:|cffced4da|n- Аура Скверны: восстанавливает зданиям Легиона по |cffffffff6|cffced4da ед. здоровья в секунду в радиусе |cffffffff900|cffced4da.|r",

        # h0DU: Аванпост
        13242: "|cffe4cfa3Аванпост|r",
        13243: "|cffe4cfa3Аванпост|r (|cffffffffQ|r)",
        31740: "|cffa6afb8ЗДАНИЕ:|cffced4da Главный оплот передовой базы Легиона. Служит центром сбора добытых ресурсов и подготавливает рабочих.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deАрхитектор Скверны|cffced4da: базовый рабочий, строитель и ремонтник.|n|n|cffa6afb8Улучшается до:|cffced4da|n- |cffa9c7deШтаб Демонов|cffced4da: открывает передовые сооружения и доступ ко второму этапу развития.|n|nПозволяет обменивать ресурсы на рынке и назначать столицу.|r",

        # h0DV: Штаб Демонов
        13246: "|cffe4cfa3Штаб Демонов|r",
        13247: "|cffe4cfa3Штаб Демонов|r (|cffffffffZ|r)",
        31741: "|cffa6afb8ЗДАНИЕ:|cffced4da Укреплённый штаб Легиона (вторая ступень). Открывает возведение Портала, Тёмной Библиотеки и новые уровни улучшений в Кузне.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deАрхитектор Скверны|cffced4da: базовый рабочий, строитель и ремонтник.|n|n|cffa6afb8Улучшается до:|cffced4da|n- |cffa9c7deПалаты Командования|cffced4da: высшая ступень ставки Легиона.|n|nПозволяет обменивать ресурсы на рынке и назначать столицу.|r",

        # h0DW: Палаты Командования
        13250: "|cffe4cfa3Палаты Командования|r",
        13251: "|cffe4cfa3Палаты Командования|r (|cffffffffZ|r)",
        31742: "|cffa6afb8ЗДАНИЕ:|cffced4da Цитадель верховного командования Пылающего Легиона (третья ступень). Открывает максимальный предел Накопителей Скверны и высшие технологии расы.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deАрхитектор Скверны|cffced4da: базовый рабочий, строитель и ремонтник.|n|n|cffa6afb8Особенности:|cffced4da|n- Защита столицы: повышает броню союзников поблизости.|n- Позволяет обменивать ресурсы на рынке и назначать столицу.|r",

        # h0DX: Алтарь Командиров Скверны
        13254: "|cffe4cfa3Алтарь Командиров Скверны|r",
        13255: "|cffe4cfa3Алтарь Командиров Скверны|r (|cffffffffS|r)",
        31743: "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище призыва высших командиров Легиона. Позволяет призывать новых и воскрешать павших героев.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deНатрезим|cffced4da: коварный владыка теней и ментальной магии.|n- |cffa9c7deЧернокнижник|cffced4da: владыка губительного колдовства и огня Скверны.|n- |cffa9c7deШиварра|cffced4da: шестирукая воительница и жрица пламени Скверны.|r",

        # h0DY: Малый Портал
        13258: "|cffe4cfa3Малый Портал|r",
        13259: "|cffe4cfa3Малый Портал|r (|cffffffffW|r)",
        31744: "|cffa6afb8ЗДАНИЕ:|cffced4da Врата призыва штурмовых отрядов Легиона.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deВластитель|cffced4da: ударный пехотинец ближнего боя.|n- |cffa9c7deЗверь Скверны|cffced4da: быстроногий боевой зверь.|n- |cffa9c7deМо'агр|cffced4da: тяжёлый громила с сокрушительным ударом.|n- |cffa9c7deАдская колесница|cffced4da: осадная машина дальнего боя.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗащита|cffced4da: повышает живучесть боевых единиц.|n- |cffa9c7deКровавый палач|cffced4da: улучшает Властителей до Кровавых палачей.|n- |cffa9c7deКровавое отродье|cffced4da: улучшает Кровавых палачей до Кровавых отродий.|n- |cffa9c7deКровопускатель|cffced4da: улучшает Кровавых отродий до Кровопускателей.|r",

        # h0DZ: Кузня Скверны
        13262: "|cffe4cfa3Кузня Скверны|r",
        13263: "|cffe4cfa3Кузня Скверны|r (|cffffffffR|r)",
        31745: "|cffa6afb8ЗДАНИЕ:|cffced4da Арсенал и мастерская тёмных инженеров Легиона.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОружие Скверны|cffced4da: увеличивает урон ближнего боя.|n- |cffa9c7deОсквернённая броня|cffced4da: повышает защиту ближнего боя.|n- |cffa9c7deМагия Скверны|cffced4da: увеличивает силу заклинаний и дальних атак.|n- |cffa9c7deУкрепление Скверной|cffced4da: повышает защиту дальнего боя и магов.|n- |cffa9c7deПознание Скверны|cffced4da: усиливает боевые параметры особых отрядов.|n- |cffa9c7deУлучшенная добыча|cffced4da: увеличивает переносимый объём древесины.|r",

        # h0E0: Тёмная Библиотека
        13266: "|cffe4cfa3Тёмная Библиотека|r",
        13267: "|cffe4cfa3Тёмная Библиотека|r (|cffffffffD|r)",
        31746: "|cffa6afb8ЗДАНИЕ:|cffced4da Хранилище запретных гримуаров и центр подготовки чернокнижников.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЭредар-колдун|cffced4da: могущественный заклинатель Скверны.|n- |cffa9c7deДемон-тюремщик|cffced4da: надзиратель, подавляющий волю врагов.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deДревние знания эредаров|cffced4da: открывает способности Эредаров-колдунов.|n- |cffa9c7deМастерство владения Скверной|cffced4da: открывает способности Демонов-тюремщиков.|r",

        # h0E1: Портал
        13284: "|cffe4cfa3Портал|r",
        13285: "|cffe4cfa3Портал|r (|cffffffffF|r)",
        31748: "|cffa6afb8ЗДАНИЕ:|cffced4da Пространственные врата в глубины Круговерти Пустоты. Призывает элитных демонов и чудовищ Легиона.|n|n|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЛовчий Скверны|cffced4da: быстрый охотник на магов и поглотитель маны.|n- |cffa9c7deИнфернал|cffced4da: пылающий исполин, защищённый от магии.|n- |cffa9c7deСтраж ужаса|cffced4da: крылатый палач с разрушительным арсеналом заклинаний.|n|n|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deДрессировка зверей|cffced4da: усиливает параметры Ловчих Скверны.|n- |cffa9c7deМастерство устрашения|cffced4da: раскрывает боевой потенциал Стражей ужаса.|r",

        # n02C: Башня смерти
        13269: "|cffe4cfa3Башня смерти|r",
        13270: "|cffe4cfa3Башня смерти|r (|cffffffffZ|r)",
        31747: "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение Легиона. Поражает врагов сгустками разрушительной тёмной энергии.|n|nАтакует наземные и воздушные цели.|r",
    }

    print(f"Applying {len(wts_updates)} WTS updates for Demon buildings...")
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

    bld_map = [
        ("h0DS", 13204, 13205, 31733),
        ("h0DT", 13208, 13209, 19467),
        ("h0DU", 13242, 13243, 31740),
        ("h0DV", 13246, 13247, 31741),
        ("h0DW", 13250, 13251, 31742),
        ("h0DX", 13254, 13255, 31743),
        ("h0DY", 13258, 13259, 31744),
        ("h0DZ", 13262, 13263, 31745),
        ("h0E0", 13266, 13267, 31746),
        ("h0E1", 13284, 13285, 31748),
        ("n02C", 13269, 13270, 31747),
    ]

    checks = []
    registry_buildings = []

    for bid, nid, tid, uid in bld_map:
        args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", bid]
        res = hw.run_cli_json(args)
        if not res.get("ok"):
            raise RuntimeError(f"Failed to read {bid} via HiveWE: {res}")
        fields = res.get("object", {}) or res.get("fields", {})

        actual_name = resolve(fields.get("name"))
        actual_tip = resolve(fields.get("tip"))
        actual_ubertip = resolve(fields.get("ubertip"))

        name_ok = (actual_name == wts_updates[nid])
        tip_ok = (actual_tip == wts_updates[tid])
        ubertip_ok = (actual_ubertip == wts_updates[uid])

        checks.append({"building": bid, "field": "name", "expected": wts_updates[nid], "actual": actual_name, "ok": name_ok})
        checks.append({"building": bid, "field": "tip", "expected": wts_updates[tid], "actual": actual_tip, "ok": tip_ok})
        checks.append({"building": bid, "field": "ubertip", "expected": wts_updates[uid], "actual": actual_ubertip, "ok": ubertip_ok})

        registry_buildings.append({
            "id": bid,
            "hotkey": resolve(fields.get("hotkey")),
            "name": {"wts_id": nid, "text": wts_updates[nid]},
            "tip": {"wts_id": tid, "text": wts_updates[tid]},
            "ubertip": {"wts_id": uid, "text": wts_updates[uid]},
        })

    all_ok = all(c["ok"] for c in checks)
    print(f"Verification checks passed: {sum(1 for c in checks if c['ok'])} / {len(checks)}")

    apply_payload = {
        "race": "Demons",
        "category": "Buildings",
        "buildings_count": len(bld_map),
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

    with open(folder / "demon_buildings_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Пылающий Легион (Demon): Категория 1 — Здания (11 зданий, 33 поля)",
        "buildings": registry_buildings
    }

    with open(folder / "demon_buildings.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
