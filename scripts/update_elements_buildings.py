# -*- coding: utf-8 -*-
"""Update Elements race buildings (all 12 buildings) with complete SD/HD validation."""
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
            "id": "h0EQ",
            "name": "|cffe4cfa3Скопление стихий|r",
            "tip": "|cffe4cfa3Скопление стихий|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Главное святилище и центр концентрации первичных стихий. "
                "Позволяет призывать духов стихий, добывать и складировать ресурсы. "
                "Приносит |cffffffff1500|cffced4da ед. золота каждые |cffffffff25|cffced4da сек. "
                "и даёт |cffffffff50|cffced4da ед. пищи.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deДух стихий|cffced4da.|n|n"
                "|cffa6afb8Улучшается до:|cffced4da |cffa9c7deНаполнитель стихий|cffced4da.|r"
            ),
            "wts": {"name": 13651, "tip": 7296, "ubertip": 8099},
            "hotkey": "Q"
        },
        {
            "id": "h0ER",
            "name": "|cffe4cfa3Наполнитель стихий|r",
            "tip": "|cffe4cfa3Наполнитель стихий|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Развитое святилище стихий второго уровня. "
                "Позволяет призывать духов стихий, открывает доступ к новым типам стихийных войск и улучшениям. "
                "Приносит |cffffffff1500|cffced4da ед. золота каждые |cffffffff25|cffced4da сек. "
                "и увеличивает лимит пищи до |cffffffff100|cffced4da ед.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deДух стихий|cffced4da.|n|n"
                "|cffa6afb8Улучшается до:|cffced4da |cffa9c7deСтихийный Бастион|cffced4da.|r"
            ),
            "wts": {"name": 13656, "tip": 7299, "ubertip": 15037},
            "hotkey": "Z"
        },
        {
            "id": "h0ES",
            "name": "|cffe4cfa3Стихийный Бастион|r",
            "tip": "|cffe4cfa3Стихийный Бастион|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Высшая цитадель могущества стихий третьего уровня. "
                "Открывает доступ к элитным воинам стихий и высшим элементальным воплощениям. "
                "Приносит |cffffffff1500|cffced4da ед. золота каждые |cffffffff25|cffced4da сек. "
                "и увеличивает лимит пищи до |cffffffff150|cffced4da ед.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deДух стихий|cffced4da|n"
                "- |cffa9c7deОсобый Огня|cffced4da|n"
                "- |cffa9c7deОсобый Воды|cffced4da|n"
                "- |cffa9c7deОсобый Земли|cffced4da|n"
                "- |cffa9c7deОсобый Ветра|cffced4da.|r"
            ),
            "wts": {"name": 13659, "tip": 7301, "ubertip": 15040},
            "hotkey": "Z"
        },
        {
            "id": "h0EO",
            "name": "|cffe4cfa3Огненные недра|r",
            "tip": "|cffe4cfa3Огненные недра|r (|cffffffffF|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель первичной стихии Огня. "
                "Обучает пламенных элементалей, гончих и огненных птиц, "
                "а также исследует усиления боевой ярости и температуры пламени.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deЭлементаль Огня|cffced4da|n"
                "- |cffa9c7deГончая пламени|cffced4da|n"
                "- |cffa9c7deВозжигатель|cffced4da|n"
                "- |cffa9c7deЗагробник Огня|cffced4da|n"
                "- |cffa9c7deОгненная птица|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deЯрость|cffced4da|n"
                "- |cffa9c7deПовышение температуры|cffced4da|n"
                "- |cffa9c7deРассекающий удар|cffced4da.|r"
            ),
            "wts": {"name": 9240, "tip": 24394, "ubertip": 14076},
            "hotkey": "F"
        },
        {
            "id": "h0EP",
            "name": "|cffe4cfa3Магическая башня|r",
            "tip": "|cffe4cfa3Магическая башня|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое оборонительное сооружение стихий. "
                "Благодаря силе огня атакует несколько целей одновременно зарядами стихийной энергии. "
                "Может быть улучшена до башни с телепортацией.|n|n"
                "|cffa6afb8Улучшается до:|cffced4da |cffa9c7deМагическая башня|cffced4da (получает способность «Тёмный призыв»).|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон, мульти-атака).|r"
            ),
            "wts": {"name": 7322, "tip": 14949, "ubertip": 32142},
            "hotkey": "Z"
        },
        {
            "id": "h0L5",
            "name": "|cffe4cfa3Магическая башня|r",
            "tip": "|cffe4cfa3Магическая башня|r (|cffffffffZ|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Улучшенное оборонительное сооружение стихий. "
                "Атакует несколько целей одновременно и наделено способностью «Тёмный призыв», "
                "позволяющей телепортировать союзные войска к башне.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deТёмный призыв|cffced4da: мгновенно телепортирует выбранные союзные войска к башне.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон, мульти-атака).|r"
            ),
            "wts": {"name": 15030, "tip": 18365},
            "hotkey": "Z",
            "object_mods": {
                "ubertip": (
                    "|cffa6afb8ЗДАНИЕ:|cffced4da Улучшенное оборонительное сооружение стихий. "
                    "Атакует несколько целей одновременно и наделено способностью «Тёмный призыв», "
                    "позволяющей телепортировать союзные войска к башне.|n|n"
                    "|cffa6afb8Способности:|cffced4da|n"
                    "- |cffa9c7deТёмный призыв|cffced4da: мгновенно телепортирует выбранные союзные войска к башне.|n|n"
                    "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон, мульти-атака).|r"
                )
            }
        },
        {
            "id": "h0ET",
            "name": "|cffe4cfa3Морской бассейн|r",
            "tip": "|cffe4cfa3Морской бассейн|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель первичной стихии Воды. "
                "Обучает элементалей воды, морей, океанов и грязи, "
                "а также исследует ледяные стрелы, рассеяние чар и водную магию.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deЭлементаль Воды|cffced4da|n"
                "- |cffa9c7deЭлементаль Океана|cffced4da|n"
                "- |cffa9c7deЭлементаль Морей|cffced4da|n"
                "- |cffa9c7deЗагробник Глубин|cffced4da|n"
                "- |cffa9c7deРифовый Элементаль|cffced4da|n"
                "- |cffa9c7deГрязевой Элементаль|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deМагия воды|cffced4da|n"
                "- |cffa9c7deЛедяные стрелы|cffced4da|n"
                "- |cffa9c7deМагия морей|cffced4da|n"
                "- |cffa9c7deРассеяние чар|cffced4da.|r"
            ),
            "wts": {"name": 15077, "tip": 15078, "ubertip": 15029},
            "hotkey": "R"
        },
        {
            "id": "h0EU",
            "name": "|cffe4cfa3Ветролом|r",
            "tip": "|cffe4cfa3Ветролом|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель первичной стихии Воздуха. "
                "Обучает элементалей ветра, грозы и шторма, воздушных волков, "
                "а также исследует скорость воздуха, критические удары и ярость грома.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deЭлементаль Ветра|cffced4da|n"
                "- |cffa9c7deГрозовой Элементаль|cffced4da|n"
                "- |cffa9c7deВоздушный волк|cffced4da|n"
                "- |cffa9c7deЗагробник Бури|cffced4da|n"
                "- |cffa9c7deШтормовой Элементаль|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deЯрость грома|cffced4da|n"
                "- |cffa9c7deКритический удар|cffced4da|n"
                "- |cffa9c7deЛегкость воздуха|cffced4da.|r"
            ),
            "wts": {"name": 15079, "tip": 15080, "ubertip": 15043},
            "hotkey": "W"
        },
        {
            "id": "h0EV",
            "name": "|cffe4cfa3Элементальная мастерская|r",
            "tip": "|cffe4cfa3Элементальная мастерская|r (|cffffffffD|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Центр стихийных исследований и концентрации магии. "
                "Позволяет исследовать базовые усиления четырёх стихий (Огня, Воды, Земли и Ветра), "
                "повышая силу атаки и защиту войск, а также улучшать эффективность добычи ресурсов духами стихий.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deУлучшенная добыча|cffced4da|n"
                "- |cffa9c7deОгонь|cffced4da|n"
                "- |cffa9c7deВода|cffced4da|n"
                "- |cffa9c7deЗемля|cffced4da|n"
                "- |cffa9c7deВетер|cffced4da.|r"
            ),
            "wts": {"name": 15057, "tip": 15058, "ubertip": 12970},
            "hotkey": "D"
        },
        {
            "id": "h0EW",
            "name": "|cffe4cfa3Каменоломня|r",
            "tip": "|cffe4cfa3Каменоломня|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель первичной стихии Земли. "
                "Обучает элементалей земли и песка, разнообразные типы големов и воителей бури, "
                "а также исследует каменное здоровье и сокрушающие удары.|n|n"
                "|cffa6afb8Обучает:|cffced4da|n"
                "- |cffa9c7deЭлементаль Земли|cffced4da|n"
                "- |cffa9c7deПесчаный Элементаль|cffced4da|n"
                "- |cffa9c7deКаменный голем|cffced4da|n"
                "- |cffa9c7deОгненный голем|cffced4da|n"
                "- |cffa9c7deОгненный Страж|cffced4da|n"
                "- |cffa9c7deЛедяной Голем|cffced4da|n"
                "- |cffa9c7deКристальный голем|cffced4da|n"
                "- |cffa9c7deВоитель бури|cffced4da|n"
                "- |cffa9c7deЯнтарный Загробник|cffced4da|n"
                "- |cffa9c7deЯростный голем|cffced4da|n"
                "- |cffa9c7deГранитный голем|cffced4da.|n|n"
                "|cffa6afb8Исследования:|cffced4da|n"
                "- |cffa9c7deКаменное здоровье|cffced4da|n"
                "- |cffa9c7deСокрушение|cffced4da.|r"
            ),
            "wts": {"name": 15283, "tip": 15284, "ubertip": 15046},
            "hotkey": "E"
        },
        {
            "id": "h0EX",
            "name": "|cffe4cfa3Стихийный кристалл|r",
            "tip": "|cffe4cfa3Стихийный кристалл|r (|cffffffffA|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Энергетический кристалл стихийного снабжения. "
                "Предоставляет пищу для поддержания стихийной армии и генерирует регулярный доход золота.|n|n"
                "|cffa6afb8Свойства:|cffced4da|n"
                "- Предоставляет |cffffffff40|cffced4da ед. пищи.|n"
                "- Приносит |cffffffff30|cffced4da ед. золота каждые |cffffffff25|cffced4da сек.|r"
            ),
            "wts": {"name": 19661, "tip": 15069, "ubertip": 30661},
            "hotkey": "A"
        },
        {
            "id": "h0EY",
            "name": "|cffe4cfa3Алтарь Пространства|r",
            "tip": "|cffe4cfa3Алтарь Пространства|r (|cffffffffS|r)",
            "ubertip": (
                "|cffa6afb8ЗДАНИЕ:|cffced4da Священный алтарь героев стихий. "
                "Позволяет призывать великих лордов стихий и воскрешать павших героев. "
                "Предоставляет |cffffffff3|cffced4da ед. пищи.|n|n"
                "|cffa6afb8Призывает героев:|cffced4da|n"
                "- |cffa9c7deКристальный владыка|cffced4da|n"
                "- |cffa9c7deМастер ветра|cffced4da|n"
                "- |cffa9c7deПовелитель огня|cffced4da.|r"
            ),
            "wts": {"name": 15044, "tip": 15045, "ubertip": 12980},
            "hotkey": "S"
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

    # Apply direct object mods for missing fields (h0L5 ubertip)
    object_ops = [
        {"type": "unit", "id": "h0L5", "field": "ubertip", "value": b["object_mods"]["ubertip"]}
        for b in buildings_data if "object_mods" in b
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
        extra = ["--graphics", "hd"] if hd else []
        res = cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(building_ids)] + extra)
        mode = "HD" if hd else "SD"
        require(res)

        objects = {item["id"]: item for item in res.get("objects", [])}
        for b in buildings_data:
            b_id = b["id"]
            obj = objects.get(b_id, {})
            fields = obj.get("fields", {})

            act_name = resolve(fields.get("name", ""))
            act_tip = resolve(fields.get("tip", ""))
            act_ubertip = resolve(fields.get("ubertip", ""))

            checks.append({
                "id": b_id,
                "mode": mode,
                "name_ok": act_name == b["name"],
                "tip_ok": act_tip == b["tip"],
                "ubertip_ok": act_ubertip == b["ubertip"],
                "actual_name": act_name,
                "actual_tip": act_tip,
                "actual_ubertip": act_ubertip
            })

    # Verify all checks pass
    all_ok = True
    for c in checks:
        if not (c["name_ok"] and c["tip_ok"] and c["ubertip_ok"]):
            print(f"FAILED check for {c['id']} ({c['mode']}):")
            print(f"  name_ok: {c['name_ok']}, tip_ok: {c['tip_ok']}, ubertip_ok: {c['ubertip_ok']}")
            all_ok = False

    assert all_ok, "Some readback checks failed!"

    # Verify other binary hashes
    binary_intact = True
    for fname, orig_hash in other_binary_hashes.items():
        curr_hash = hashlib.sha256((source / fname).read_bytes()).hexdigest()
        if curr_hash != orig_hash:
            print(f"ERROR: Binary file {fname} was modified!")
            binary_intact = False
    assert binary_intact, "Other binary files were modified!"

    # Save artifacts
    plan_artifact = folder / "elements_buildings.json"
    apply_artifact = folder / "elements_buildings_apply.json"

    with open(plan_artifact, "w", encoding="utf-8") as f:
        json.dump({
            "race": "Elements",
            "category": "buildings",
            "total_buildings": len(buildings_data),
            "buildings": buildings_data
        }, f, ensure_ascii=False, indent=2)

    with open(apply_artifact, "w", encoding="utf-8") as f:
        json.dump({
            "race": "Elements",
            "category": "buildings",
            "wts_changed_count": len(wts_changed_ids),
            "wts_changed_ids": wts_changed_ids,
            "object_ops": object_ops,
            "wts_hash_before": original_wts_hash,
            "wts_hash_after": new_wts_hash,
            "w3u_hash_before": original_w3u_hash,
            "w3u_hash_after": new_w3u_hash,
            "w3u_skin_hash_before": original_w3u_skin_hash,
            "w3u_skin_hash_after": new_w3u_skin_hash,
            "checks_summary": {
                "total_checks": len(checks),
                "passed": sum(1 for c in checks if c["name_ok"] and c["tip_ok"] and c["ubertip_ok"]),
            },
            "checks": checks
        }, f, ensure_ascii=False, indent=2)

    print("Elements buildings update completed successfully!")
    print(f"Updated {len(wts_changed_ids)} WTS strings across {len(buildings_data)} buildings.")
    print(f"Object ops applied: {len(object_ops)} (h0L5 ubertip).")
    print(f"All {len(checks)} SD/HD readback checks PASSED (100%).")
    print(f"Other binary files: 100% intact.")

if __name__ == "__main__":
    main()
