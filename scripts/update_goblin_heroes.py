# -*- coding: utf-8 -*-
"""Update all 6 Goblin heroes with SD validation and artifacts."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw
from apply_faceless_object_text import patch_blob

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
    skin_u_path = ROOT / "map.w3x/war3mapSkin.w3u"

    original_hashes = {
        "wts": hashlib.sha256(wts_path.read_bytes()).hexdigest(),
        "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256(skin_u_path.read_bytes()).hexdigest(),
        "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
        "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
        "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
    }

    wts_updates = {
        # H0BD: Спецназовец (Z)
        14162: "|cffe4cfa3Спецназовец|r",
        14164: "|cffe4cfa3Спецназовец|r (|cffffffffZ|r)",
        14165: "|cffe4cfa3Спецназовец|r",
        14163: "|cffe4cfa3Спецназовец|r",

        # Galh: Алхимик (C)
        14114: "|cffe4cfa3Алхимик|r",
        14116: "|cffe4cfa3Алхимик|r (|cffffffffC|r)",
        14117: "|cffe4cfa3Алхимик|r",
        14115: "|cffe4cfa3Алхимик|r",
        19928: "|cffa6afb8ГЕРОЙ:|cffced4da Мастер опасных реактивов, восседающий на спине послушного огра. Основная характеристика — |cffffffffсила|cffced4da. Тяжёлый боец передовой, распыляющий лечебные газы, разрушающий броню врагов кислотными бомбами и превращающий противников в чистое золото.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deИсцеляющий газ|cffced4da: распыляет целебные испарения, восстанавливающие здоровье союзников.|n- |cffa9c7deКислотная бомба|cffced4da: обливает врагов едким составом, снижая их броню и нанося периодический урон.|n- |cffa9c7deЭликсир ярости|cffced4da: резко повышает скорость передвижения и боя огра.|n- |cffa9c7deТрансмутация|cffced4da: мгновенно уничтожает вражеского воина, превращая его в кучу золота.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # Gmex: Механик (X)
        14113: "|cffe4cfa3Механик|r",
        14111: "|cffe4cfa3Механик|r (|cffffffffX|r)",
        14112: "|cffe4cfa3Механик|r",
        14110: "|cffe4cfa3Механик|r",
        12847: "|cffa6afb8ГЕРОЙ:|cffced4da Гениальный инженер и конструктор боевых механизмов. Основная характеристика — |cffffffffинтеллект|cffced4da. Поддерживает армию фабриками заводных гоблинов, накрывает врагов кассетными ракетами и лично трансформируется в несокрушимого робогоблина.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПортативная фабрика|cffced4da: разворачивает автомат, непрерывно выпускающий взрывающихся заводных гоблинов.|n- |cffa9c7deКассетные ракеты|cffced4da: обстреливает область ракетами, оглушая и повреждая врагов.|n- |cffa9c7deУлучшенная инженерия|cffced4da: пассивно усиливает боевые характеристики и эффективность всех механизмов.|n- |cffa9c7deРобогоблин|cffced4da: трансформирует механика в бронированную боевую машину с осадным типом брони.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # N018: Шеф Кабестана (Z)
        14166: "|cffe4cfa3Шеф Кабестана|r",
        14168: "|cffe4cfa3Шеф Кабестана|r (|cffffffffZ|r)",
        14169: "|cffe4cfa3Шеф Кабестана|r",
        14167: "|cffe4cfa3Шеф Кабестана|r",
        28303: "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный градоначальник Кабестана и главный инженер Орды. Основная характеристика — |cffffffffинтеллект|cffced4da. Обороняет позиции автономными турелями, закладывает смертоносные взрывные бочки, ремонтирует союзную технику и поражает цепи врагов электричеством.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСамодельная турель|cffced4da: устанавливает огневую турель, непрерывно обстреливающую врагов.|n- |cffa9c7deБочка-взрывучка|cffced4da: закладывает пороховую бочку, взрывающуюся с колоссальным уроном через |cffffffff3|cffced4da с.|n- |cffa9c7deПоле саморемонта|cffced4da: аура, восстанавливающая здоровье союзным механизмам поблизости.|n- |cffa9c7deРазряд!|cffced4da: выпускает электрический импульс по линии, пробивающий ряды противников.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # N019: Мастер осады (X)
        9825:  "|cffe4cfa3Мастер осады|r",
        14177: "|cffe4cfa3Мастер осады|r (|cffffffffX|r)",
        14178: "|cffe4cfa3Мастер осады|r",
        14176: "|cffe4cfa3Мастер осады|r",
        39574: "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный главный конструктор военной машины Истинной Орды. Основная характеристика — |cffffffffинтеллект|cffced4da. Создаёт портативные заводы «Железных звёзд», ведёт автоматический ракетный огонь, обрушивает ракетопады и мгновенно перезаряжает все бортовые системы.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВзрыв|cffced4da: запускает тяжёлую ракету, поражающую цель и наносящую урон по области.|n- |cffa9c7deПортативный завод|cffced4da: производит самоходные «Железные звёзды», катящиеся на врага.|n- |cffa9c7deАвтоматический ракетомет|cffced4da: пассивно выпускает ракеты по ближайшим противникам.|n- |cffa9c7deРакетопад|cffced4da: обрушивает массированный шквал ракетных залпов на указанную область.|n- |cffa9c7deПерезагрузка|cffced4da: мгновенно обнуляет время восстановления всех способностей мастера осады.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон героя).|r",

        # N01A: Торговый Принц (Z)
        9909:  "|cffe4cfa3Торговый Принц|r",
        14181: "|cffe4cfa3Торговый Принц|r (|cffffffffZ|r)",
        14182: "|cffe4cfa3Торговый Принц|r",
        14180: "|cffe4cfa3Торговый Принц|r",
        28305: "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный правитель Картеля Трюмных Вод. Основная характеристика — |cffffffffинтеллект|cffced4da. Оснащён роскошным шагоходом с пулемётом, вдохновляет наёмников аурой пропаганды, призывает боевых мехов и запускает разрушительную Большую Красную Кнопку.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРазрывные пули|cffced4da: даёт шанс нанести критический урон при выстреле.|n- |cffa9c7deАура пропаганды|cffced4da: пассивно увеличивает урон от атак всех союзников поблизости.|n- |cffa9c7deПризвать мехи|cffced4da: вызывает на поле боя боевых штурмовых роботов.|n- |cffa9c7deБольшая Красная Кнопка|cffced4da: активирует секретную систему самоуничтожения позиции врага колоссальным взрывом.|n|n|cffa6afb8Атакует:|cffced4da наземные цели (дальний бой, урон героя).|r",
    }

    # H0BD ubertip patch in war3mapSkin.w3u (avoid touching shared TRIGSTR_2701)
    h0bd_ubertip = "|cffa6afb8ГЕРОЙ:|cffced4da Элитный стрелок и тактик диверсионных операций картеля. Основная характеристика — |cffffffffловкость|cffced4da. Ведёт беглый огонь из скорострельного пулемёта, подавляет магию и атаки врагов шоковыми гранатами, увеличивает урон стрелков аурой меткости и обрушивает разрушительные ракетные удары.|n|n|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОсколочная граната|cffced4da: бросает гранату, наносящую урон по области осколочным взрывом.|n- |cffa9c7deШоковая граната|cffced4da: лишает противников в области возможности атаковать и применять заклинания.|n- |cffa9c7deАура меткости|cffced4da: увеличивает урон дальнобойных атак союзных войск поблизости.|n- |cffa9c7deАртобстрел|cffced4da: обрушивает на указанную территорию сокрушительный залп ракет.|n|n|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, урон героя).|r"
    skin_ops = [
        {"id": "H0BD", "field": "ubertip", "value": h0bd_ubertip}
    ]

    print(f"Applying {len(wts_updates)} WTS updates for Goblin heroes...")
    wts_content = wts_path.read_text(encoding="utf-8")
    for sid, new_val in sorted(wts_updates.items()):
        wts_content = update_wts_string(wts_content, sid, new_val)

    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print("WTS updated successfully.")

    print("Patching H0BD ubertip in war3mapSkin.w3u...")
    patched_blob, changed = patch_blob(skin_u_path.read_bytes(), skin_ops, "unit", add_missing=True)
    skin_u_path.write_bytes(patched_blob)
    new_skin_hash = hashlib.sha256(skin_u_path.read_bytes()).hexdigest()
    print(f"war3mapSkin.w3u patched ({len(changed)} mods changed).")

    # Reset HiveWE cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    hero_keys = {
        "H0BD": (14162, 14164, None, 14165, 14163),
        "Galh": (14114, 14116, 19928, 14117, 14115),
        "Gmex": (14113, 14111, 12847, 14112, 14110),
        "N018": (14166, 14168, 28303, 14169, 14167),
        "N019": (9825,  14177, 39574, 14178, 14176),
        "N01A": (9909,  14181, 28305, 14182, 14180),
    }

    checks = []
    for hid, (nid, tid, ubid, rtid, atid) in hero_keys.items():
        res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", hid])
        if not res.get("ok"):
            raise RuntimeError(f"Failed to fetch {hid}: {res}")
        f = res.get("object", {}) or res.get("fields", {})
        actual_name = resolve(f.get("name"))
        actual_tip = resolve(f.get("tip"))
        actual_ubertip = resolve(f.get("ubertip"))
        actual_revivetip = resolve(f.get("revivetip"))
        actual_awakentip = resolve(f.get("awakentip"))

        expected_name = wts_updates[nid]
        expected_tip = wts_updates[tid]
        expected_ubertip = h0bd_ubertip if hid == "H0BD" else wts_updates[ubid]
        expected_revivetip = wts_updates[rtid]
        expected_awakentip = wts_updates[atid]

        n_ok = (actual_name == expected_name)
        t_ok = (actual_tip == expected_tip)
        u_ok = (actual_ubertip == expected_ubertip)
        rt_ok = (actual_revivetip == expected_revivetip)
        at_ok = (actual_awakentip == expected_awakentip)

        checks.append({"id": hid, "field": "name", "expected": expected_name, "actual": actual_name, "ok": n_ok})
        checks.append({"id": hid, "field": "tip", "expected": expected_tip, "actual": actual_tip, "ok": t_ok})
        checks.append({"id": hid, "field": "ubertip", "expected": expected_ubertip, "actual": actual_ubertip, "ok": u_ok})
        checks.append({"id": hid, "field": "revivetip", "expected": expected_revivetip, "actual": actual_revivetip, "ok": rt_ok})
        checks.append({"id": hid, "field": "awakentip", "expected": expected_awakentip, "actual": actual_awakentip, "ok": at_ok})

    all_ok = all(c["ok"] for c in checks)
    print(f"SD Verification checks: {sum(c['ok'] for c in checks)}/{len(checks)} passed.")
    for c in checks:
        if not c["ok"]:
            print(f"  MISMATCH on {c['id']} {c['field']}")

    apply_payload = {
        "race": "Goblins",
        "category": "heroes",
        "total_heroes": len(hero_keys),
        "total_fields": len(checks),
        "wts_updated": list(wts_updates.keys()),
        "skin_patch_count": len(skin_ops),
        "hashes_before": original_hashes,
        "hashes_after": {
            "wts": new_wts_hash,
            "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
            "w3u_skin": new_skin_hash,
            "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
            "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
            "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
            "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
            "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
            "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
        },
        "binary_files_unchanged": (
            original_hashes["w3u"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest() and
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

    with open(folder / "goblins_heroes_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Гоблины (Goblins): категория 3 — Герои (6 героев)",
        "heroes_count": len(hero_keys),
        "variants": ["SD"],
        "heroes": [
            {
                "id": hid,
                "hotkey": resolve(hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", hid]).get("object", {}).get("hotkey")),
                "strings": [
                    {"field": "name", "wts_id": nid, "after": wts_updates[nid]},
                    {"field": "tip", "wts_id": tid, "after": wts_updates[tid]},
                    {"field": "ubertip", "wts_id": ubid, "after": h0bd_ubertip if hid == "H0BD" else wts_updates[ubid]},
                    {"field": "revivetip", "wts_id": rtid, "after": wts_updates[rtid]},
                    {"field": "awakentip", "wts_id": atid, "after": wts_updates[atid]}
                ]
            }
            for hid, (nid, tid, ubid, rtid, atid) in hero_keys.items()
        ]
    }

    with open(folder / "goblins_heroes.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
