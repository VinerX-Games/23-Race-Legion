# -*- coding: utf-8 -*-
"""Update Demon race heroes with complete SD validation."""
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

    # 7 heroes, 42 WTS strings
    wts_updates = {
        # N02F: Натрезим
        13418: "|cffe4cfa3Натрезим|r",
        13934: "|cffe4cfa3Повелитель ужаса|r",
        13935: "|cffe4cfa3Натрезим|r (|cffffffffM|r)",
        13421: "|cffe4cfa3Натрезим|r",
        13420: "|cffe4cfa3Натрезим|r",
        31751: "|cffa6afb8ГЕРОЙ:|cffced4da Могучий командир Скверны, повелитель ментальных манипуляций и поглощения урона. Основная характеристика — |cffffffffсила|cffced4da. Защищён шипастой бронёй, оскверняет вражеские ряды, испепеляет цели сгустками Скверны и способен восстать из мёртвых после гибели.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deШипастая броня|cffced4da: повышает броню и возвращает урон атакующим в ближнем бою врагам.|n- |cffa9c7deОсквернение|cffced4da: оскверняет землю, замедляя врагов и усиливая демонов.|n- |cffa9c7deСгусток Скверны|cffced4da: обрушивает струю пламени Скверны по конусу перед собой.|n- |cffa9c7deРеинкарнация|cffced4da: мгновенно возрождает натрезима при получении смертельного урона.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # N02A: Чернокнижник
        13234: "|cffe4cfa3Чернокнижник|r",
        13235: "|cffe4cfa3Чернокнижник|r",
        13929: "|cffe4cfa3Чернокнижник|r (|cffffffffW|r)",
        13930: "|cffe4cfa3Чернокнижник|r",
        13236: "|cffe4cfa3Чернокнижник|r",
        31738: "|cffa6afb8ГЕРОЙ:|cffced4da Верховный чародей Легиона, повелевающий тёмной поддержкой и подавлением магии. Основная характеристика — |cffffffffинтеллект|cffced4da. Разъедает броню врагов коррозией, усиливает союзников дарами Скверны, погружает противников в безмолвие и сжигает цели испепелением.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКоррозия Скверны|cffced4da: снижает показатель брони вражеских войск в радиусе ауры.|n- |cffa9c7deДары Скверны|cffced4da: наделяет союзника приливом силы, увеличивая его урон и защиту.|n- |cffa9c7deНемота|cffced4da: запрещает вражеским отрядам применять заклинания в указанной области.|n- |cffa9c7deИспепеление|cffced4da: каждая атака наносит дополнительный урон и взрывает погибшую цель.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (дальний бой, урон героя).|r",

        # U028: Шиварра
        13231: "|cffe4cfa3Шиварра|r",
        13232: "|cffe4cfa3Джизельда|r",
        13925: "|cffe4cfa3Шиварра|r (|cffffffffE|r)",
        13926: "|cffe4cfa3Шиварра|r",
        13233: "|cffe4cfa3Шиварра|r",
        31737: "|cffa6afb8ГЕРОЙ:|cffced4da Шестирукая демоническая воительница и жрица пламени Легиона. Основная характеристика — |cffffffffловкость|cffced4da. Порождает зверей Скверны из павших тел, впадает в ярость в гуще битвы, наносит сокрушительные критические удары клинками и защищается осквернённым щитом.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСоздание Скверны|cffced4da: заражает врага паразитом, порождающим Зверя Скверны после смерти жертвы.|n- |cffa9c7deЯрость Скверны|cffced4da: резко повышает темп боя ценой повышенного входящего урона.|n- |cffa9c7deКритический удар|cffced4da: даёт шанс нанести многократный урон при атаке.|n- |cffa9c7deЩит Скверны|cffced4da: окружает шиварру барьером, отражающим удары врагов.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # N02G: Генерал Легиона
        13319: "|cffe4cfa3Генерал Легиона|r",
        13320: "|cffe4cfa3Архимонд|r",
        13937: "|cffe4cfa3Генерал Легиона|r (|cffffffffW|r)",
        13939: "|cffe4cfa3Генерал Легиона|r",
        13321: "|cffe4cfa3Генерал Легиона|r",
        31752: "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный верховный главнокомандующий Пылающего Легиона. Основная характеристика — |cffffffffсила|cffced4da. Сокрушает ряды врагов ударами чудовищной мощи, изгоняет души в астрал, обрушивает метеоритный Апокалипсис и подчиняет стихию Скверны своей несокрушимой воле.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКритический удар|cffced4da: даёт шанс нанести колоссальный урон при ударе.|n- |cffa9c7deДары Скверны|cffced4da: погружает цель в астральный план, делая уязвимой к магии.|n- |cffa9c7deАпокалипсис|cffced4da: призывает опустошительный метеоритный дождь на огромную территорию.|n- |cffa9c7deПовелевание Скверной|cffced4da: тёмная аура, подавляющая сопротивление окружающих врагов.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # N02B: Верховный Чернокнижник
        13237: "|cffe4cfa3Верховный Чернокнижник|r",
        13238: "|cffe4cfa3Кил'джеден|r",
        13931: "|cffe4cfa3Верховный Чернокнижник|r (|cffffffffZ|r)",
        13933: "|cffe4cfa3Верховный Чернокнижник|r",
        13239: "|cffe4cfa3Верховный Чернокнижник|r",
        31739: "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный владыка эредаров и величайший чернокнижник во Вселенной. Основная характеристика — |cffffffffинтеллект|cffced4da. Мечет испепеляющие сгустки Скверны, искажает астральное пространство, поражает врагов смертоносным Перстом боли и повелевает первородной мощью хаоса.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСгусток Скверны|cffced4da: запускает сгусток тёмной энергии во вражеский отряд.|n- |cffa9c7deПоле астрала|cffced4da: создаёт пространственную брешь, перемещающую войска.|n- |cffa9c7deПерст боли|cffced4da: поражает выбранную цель разрядом колоссального магического урона.|n- |cffa9c7deПовелевание Скверной|cffced4da: раскрывает высший потенциал всех способностей чернокнижника.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (дальний бой, урон героя).|r",

        # N02H: Владыка Судеб
        6773: "|cffe4cfa3Владыка Судеб|r",
        6891: "|cffe4cfa3Каззак|r",
        6895: "|cffe4cfa3Владыка Судеб|r (|cffffffffZ|r)",
        6894: "|cffe4cfa3Владыка Судеб|r",
        6893: "|cffe4cfa3Владыка Судеб|r",
        31753: "|cffa6afb8ГЕРОЙ:|cffced4da Мифический полководец Легиона, мастерски владеющий разрушительной магией пламени. Основная характеристика — |cffffffffсила|cffced4da. Поглощает жизненные силы врагов, ускоренно заживляет раны в пылу схватки, высвобождает огненную ярость и воскресает после гибели.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПоглощение Скверны|cffced4da: высасывает здоровье и силы противников поблизости.|n- |cffa9c7deЗаживление ран|cffced4da: ускоряет естественную регенерацию здоровья в бою.|n- |cffa9c7deОгненная ярость|cffced4da: обрушивает огненные всплески на окружающие цели.|n- |cffa9c7deРеинкарнация|cffced4da: возвращает владыку к жизни после падения на поле брани.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # U027: Владыка Легиона
        13228: "|cffe4cfa3Владыка Легиона|r",
        7174: "|cffe4cfa3Аватара Саргераса|r",
        13922: "|cffe4cfa3Владыка Легиона|r (|cffffffffZ|r)",
        13924: "|cffe4cfa3Владыка Легиона|r",
        13230: "|cffe4cfa3Владыка Легиона|r",
        31736: "|cffa6afb8ГЕРОЙ:|cffced4da Легендарное физическое воплощение Падшего Титана. Основная характеристика — |cffffffffсила|cffced4da. Обладает нечеловеческой стойкостью и колоссальным запасом прочности, рассекает вражеские ряды титаническими ударами, защищён непробиваемой кожей Скверны и обрушивает пылающие метеоры.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: наносит урон окружающим наземным целям каждым взмахом меча.|n- |cffa9c7deКожа, покрытая Скверной|cffced4da: снижает любой получаемый урон и даёт защиту от магии.|n- |cffa9c7deВладычество|cffced4da: подавляющая аура, ослабляющая атаку вражеских войск.|n- |cffa9c7deОгненный метеорит|cffced4da: призывает с неба пылающий метеорит, оглушающий и сжигающий всё вокруг.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",
    }

    print(f"Applying {len(wts_updates)} WTS updates for Demon heroes...")
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

    hero_map = [
        ("N02F", 13418, 13934, 13935, 31751, 13421, 13420),
        ("N02A", 13234, 13235, 13929, 31738, 13930, 13236),
        ("U028", 13231, 13232, 13925, 31737, 13926, 13233),
        ("N02G", 13319, 13320, 13937, 31752, 13939, 13321),
        ("N02B", 13237, 13238, 13931, 31739, 13933, 13239),
        ("N02H", 6773, 6891, 6895, 31753, 6894, 6893),
        ("U027", 13228, 7174, 13922, 31736, 13924, 13230),
    ]

    checks = []
    registry_heroes = []

    for hid, nid, pid, tid, ubid, rvid, awid in hero_map:
        args = ["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", hid]
        res = hw.run_cli_json(args)
        if not res.get("ok"):
            raise RuntimeError(f"Failed to read {hid} via HiveWE: {res}")
        fields = res.get("object", {}) or res.get("fields", {})

        actual_name = resolve(fields.get("name"))
        actual_proper = resolve(fields.get("propernames"))
        actual_tip = resolve(fields.get("tip"))
        actual_ubertip = resolve(fields.get("ubertip"))
        actual_revivetip = resolve(fields.get("revivetip"))
        actual_awakentip = resolve(fields.get("awakentip"))

        name_ok = (actual_name == wts_updates[nid])
        proper_ok = (actual_proper == wts_updates[pid])
        tip_ok = (actual_tip == wts_updates[tid])
        ubertip_ok = (actual_ubertip == wts_updates[ubid])
        revivetip_ok = (actual_revivetip == wts_updates[rvid])
        awakentip_ok = (actual_awakentip == wts_updates[awid])

        checks.append({"hero": hid, "field": "name", "expected": wts_updates[nid], "actual": actual_name, "ok": name_ok})
        checks.append({"hero": hid, "field": "propernames", "expected": wts_updates[pid], "actual": actual_proper, "ok": proper_ok})
        checks.append({"hero": hid, "field": "tip", "expected": wts_updates[tid], "actual": actual_tip, "ok": tip_ok})
        checks.append({"hero": hid, "field": "ubertip", "expected": wts_updates[ubid], "actual": actual_ubertip, "ok": ubertip_ok})
        checks.append({"hero": hid, "field": "revivetip", "expected": wts_updates[rvid], "actual": actual_revivetip, "ok": revivetip_ok})
        checks.append({"hero": hid, "field": "awakentip", "expected": wts_updates[awid], "actual": actual_awakentip, "ok": awakentip_ok})

        registry_heroes.append({
            "id": hid,
            "hotkey": resolve(fields.get("hotkey")),
            "name": {"wts_id": nid, "text": wts_updates[nid]},
            "propernames": {"wts_id": pid, "text": wts_updates[pid]},
            "tip": {"wts_id": tid, "text": wts_updates[tid]},
            "ubertip": {"wts_id": ubid, "text": wts_updates[ubid]},
            "revivetip": {"wts_id": rvid, "text": wts_updates[rvid]},
            "awakentip": {"wts_id": awid, "text": wts_updates[awid]},
        })

    all_ok = all(c["ok"] for c in checks)
    print(f"Verification checks passed: {sum(1 for c in checks if c['ok'])} / {len(checks)}")

    apply_payload = {
        "race": "Demons",
        "category": "Heroes",
        "heroes_count": len(hero_map),
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

    with open(folder / "demon_heroes_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Пылающий Легион (Demon): Категория 3 — Герои (7 героев, 42 поля)",
        "heroes": registry_heroes
    }

    with open(folder / "demon_heroes.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
