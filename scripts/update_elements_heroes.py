# -*- coding: utf-8 -*-
"""Update Elements race heroes (all 6 heroes: 3 Altar heroes + 3 Elemental Lords) with SD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING {string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def get_heroes_data():
    return [
        # --- 1. Altar: Кристальный владыка ---
        {
            "id": "H0EZ",
            "name": "|cffe4cfa3Кристальный владыка|r",
            "propernames": "Камнелом",
            "tip": "|cffe4cfa3Кристальный владыка|r (|cffffffffW|r)",
            "revivetip": "|cffe4cfa3Кристальный владыка|r",
            "awakentip": "|cffe4cfa3Кристальный владыка|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Могучий кристаллический исполин стихии Земли. "
                "Основная характеристика — |cffffffffсила|cffced4da. "
                "Прочный танк передовой, способный защищать союзников морозным доспехом, "
                "укреплять собственную каменную кожу, оглушать врагов броском валуна "
                "и исцелять окружающую армию спокойствием природы.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deМорозный доспех|cffced4da: повышает броню союзника и замедляет атакующих его врагов.|n"
                "- |cffa9c7deБросок валуна|cffced4da: бросает камень во врага, нанося урон и оглушая цель.|n"
                "- |cffa9c7deКаменная кожа|cffced4da: пассивно снижает получаемый физический урон.|n"
                "- |cffa9c7deУмиротворение|cffced4da: восстанавливает здоровье союзникам в большой области вокруг владыки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные (ближний бой, урон героя) и воздушные цели (дальний бой, урон героя).|r"
            ),
            "wts": {
                "name": 5894,
                "propernames": 5899,
                "tip": 5909,
                "revivetip": 6628,
                "awakentip": 5904,
                "ubertip": 31768
            },
            "hotkey": "W"
        },

        # --- 2. Altar: Мастер ветра ---
        {
            "id": "H0F0",
            "name": "|cffe4cfa3Мастер ветра|r",
            "propernames": "Келен Разрушитель",
            "tip": "|cffe4cfa3Мастер ветра|r (|cffffffffQ|r)",
            "revivetip": "|cffe4cfa3Мастер ветра|r",
            "awakentip": "|cffe4cfa3Мастер ветра|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Стремительный повелитель воздушных вихрей. "
                "Основная характеристика — |cffffffffинтеллект|cffced4da. "
                "Мобильный маг и стрелок, мгновенно перемещающийся по полю боя скачком, "
                "поражающий множество целей ветровыми стрелами и призывающий огненного феникса.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deСкачок|cffced4da: мгновенно телепортирует героя на указанное расстояние.|n"
                "- |cffa9c7deЛовкий как ветер|cffced4da: увеличивает скорость перемещения и даёт шанс уклониться от атак.|n"
                "- |cffa9c7deМножественная атака|cffced4da: позволяет атаковать несколько вражеских целей одновременно.|n"
                "- |cffa9c7deФеникс|cffced4da: призывает могучую огненную птицу, атакующую врагов с воздуха.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, урон героя).|r"
            ),
            "wts": {
                "name": 15245,
                "propernames": 15246,
                "tip": 15248,
                "revivetip": 15249,
                "awakentip": 15247,
                "ubertip": 31770
            },
            "hotkey": "Q"
        },

        # --- 3. Altar: Повелитель огня ---
        {
            "id": "N037",
            "name": "|cffe4cfa3Повелитель огня|r",
            "propernames": "Искрогнев",
            "tip": "|cffe4cfa3Повелитель огня|r (|cffffffffE|r)",
            "revivetip": "|cffe4cfa3Повелитель огня|r",
            "awakentip": "|cffe4cfa3Повелитель огня|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Грозный полководец стихии Огня. "
                "Основная характеристика — |cffffffffсила|cffced4da. "
                "Разрушительный маг и боец пламени, испепеляющий врагов, "
                "вызывающий огненные столбы, призывающий порождений лавы и сжигающий всё вокруг кольцом огня.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deИспепеление|cffced4da: каждая атака наносит дополнительный урон и заставляет погибших врагов взрываться.|n"
                "- |cffa9c7deОгненный столб|cffced4da: обрушивает на указанную область столб бушующего пламени.|n"
                "- |cffa9c7deПорождение лавы|cffced4da: призывает лавового элементаля, разделяющегося при нанесении ударов.|n"
                "- |cffa9c7deКольцо огня|cffced4da: окружает героя бушующим огненным штормом, наносящим непрерывный урон врагам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, урон героя).|r"
            ),
            "wts": {
                "name": 6629,
                "propernames": 6630,
                "tip": 6657,
                "revivetip": 6658,
                "awakentip": 6656,
                "ubertip": 31769
            },
            "hotkey": "E"
        },

        # --- 4. Lord: Владыка морей (Нептулон) ---
        {
            "id": "E029",
            "name": "|cffe4cfa3Владыка морей|r",
            "propernames": "Нептулон",
            "tip": "|cffe4cfa3Владыка морей|r (|cffffffffQ|r)",
            "revivetip": "|cffe4cfa3Владыка морей|r",
            "awakentip": "|cffe4cfa3Владыка морей|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный Владыка морей Нептулон. "
                "Основная характеристика — |cffffffffинтеллект|cffced4da. "
                "Могущественный повелитель океанских глубин, смывающий врагов сокрушительными волнами, "
                "затопляющий поле боя и защищённый щитом маны.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deСокрушительная волна|cffced4da: обрушивает на врагов мощную водяную волну, наносящую урон.|n"
                "- |cffa9c7deПоле астрала|cffced4da: переводит цель в астральный мир, делая её уязвимой к магии.|n"
                "- |cffa9c7deЩит маны|cffced4da: поглощает получаемый урон за счёт расхода запаса маны.|n"
                "- |cffa9c7deНаводнение|cffced4da: призывает всесокрушающий потоп, наносящий огромный урон вражеской армии и зданиям.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, урон героя).|r"
            ),
            "wts": {
                "name": 14697,
                "propernames": 14727,
                "tip": 14734,
                "revivetip": 14735,
                "awakentip": 14733,
                "ubertip": 16120
            },
            "hotkey": "Q"
        },

        # --- 5. Lord: Владыка ветра (Алакир) ---
        {
            "id": "E027",
            "name": "|cffe4cfa3Владыка ветра|r",
            "propernames": "Алакир",
            "tip": "|cffe4cfa3Владыка ветра|r (|cffffffffD|r)",
            "revivetip": "|cffe4cfa3Владыка ветра|r",
            "awakentip": "|cffe4cfa3Владыка ветра|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный Владыка ветра Алакир. "
                "Основная характеристика — |cffffffffловкость|cffced4da. "
                "Непревзойдённый командир стихии Воздуха, управляющий смертоносными торнадо, "
                "поражающий врагов сокрушительными взмахами и призывающий грозовые облака.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deТорнадо|cffced4da: призывает разрушительный вихрь, подбрасывающий врагов в воздух и наносящий урон зданиям.|n"
                "- |cffa9c7deРазрушающий взмах|cffced4da: совершает мощный взмах, поражающий нескольких врагов перед собой.|n"
                "- |cffa9c7deСкорость ветра|cffced4da: многократно увеличивает скорость перемещения и атаки владыки.|n"
                "- |cffa9c7deГрозовые Облака|cffced4da: обрушивает на поле боя непрерывные удары молний.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные (ближний бой, урон героя) и воздушные цели (дальний бой, урон героя).|r"
            ),
            "wts": {
                "name": 14353,
                "propernames": 14356,
                "tip": 14367,
                "revivetip": 14364,
                "awakentip": 14360,
                "ubertip": 16118
            },
            "hotkey": "D"
        },

        # --- 6. Lord: Владыка Огня (Рагнарос) ---
        {
            "id": "E028",
            "name": "|cffe4cfa3Владыка Огня|r",
            "propernames": "Рагнарос",
            "tip": "|cffe4cfa3Владыка Огня|r (|cffffffffW|r)",
            "revivetip": "|cffe4cfa3Владыка Огня|r",
            "awakentip": "|cffe4cfa3Владыка Огня|r",
            "ubertip": (
                "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный Владыка Огня Рагнарос. "
                "Основная характеристика — |cffffffffсила|cffced4da. "
                "Воплощение первозданной ярости пламени, сокрушающее врагов колоссальными ударами Сульфураса, "
                "исцеляющееся в пламени и способное переродиться после гибели.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deКолоссальный удар|cffced4da: сокрушительный удар молотом, наносящий колоссальный урон и оглушающий цель.|n"
                "- |cffa9c7deБлагодать Пламени|cffced4da: окружает Рагнароса щитом из огня, поглощающим урон и обжигающим атакующих.|n"
                "- |cffa9c7deЯрость Пламени|cffced4da: увеличивает силу атаки и скорость боя при получении урона.|n"
                "- |cffa9c7deПламенное перерождение|cffced4da: возвращает Рагнароса к жизни на месте гибели с полным запасом сил.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные (ближний бой, урон героя) и воздушные цели (дальний бой, урон героя).|r"
            ),
            "wts": {
                "name": 14379,
                "propernames": 14380,
                "tip": 14676,
                "revivetip": 14394,
                "awakentip": 14370,
                "ubertip": 31766
            },
            "hotkey": "W"
        }
    ]

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

    heroes_data = get_heroes_data()

    # Update WTS
    updated_wts = original_wts
    wts_changed_ids = []
    for h in heroes_data:
        for f, string_id in h.get("wts", {}).items():
            updated_wts = update_wts_string(updated_wts, string_id, h[f])
            wts_changed_ids.append(string_id)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Invalidate wts cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()

    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Readback checks in SD only
    checks = []
    hero_ids = [h["id"] for h in heroes_data]
    res = cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(hero_ids),
               "--fields", "name,propernames,tip,ubertip,revivetip,awakentip"])
    require_ok = res.get("ok", False)
    assert require_ok, f"Bulk check failed: {res.get('error')}"

    objects = {item["id"]: item for item in res.get("objects", [])}
    for h in heroes_data:
        h_id = h["id"]
        obj = objects.get(h_id, {})
        fields = obj.get("fields", {})

        act_name = resolve(fields.get("name", ""))
        act_propernames = resolve(fields.get("propernames", ""))
        act_tip = resolve(fields.get("tip", ""))
        act_ubertip = resolve(fields.get("ubertip", ""))
        act_revivetip = resolve(fields.get("revivetip", ""))
        act_awakentip = resolve(fields.get("awakentip", ""))

        checks.append({
            "id": h_id,
            "mode": "SD",
            "name_ok": act_name == h["name"],
            "propernames_ok": act_propernames == h["propernames"],
            "tip_ok": act_tip == h["tip"],
            "ubertip_ok": act_ubertip == h["ubertip"],
            "revivetip_ok": act_revivetip == h["revivetip"],
            "awakentip_ok": act_awakentip == h["awakentip"],
            "actual_name": act_name,
            "actual_propernames": act_propernames,
            "actual_tip": act_tip,
            "actual_ubertip": act_ubertip,
            "actual_revivetip": act_revivetip,
            "actual_awakentip": act_awakentip
        })

    # Verify all checks pass
    all_ok = True
    for c in checks:
        fields_ok = (c["name_ok"] and c["propernames_ok"] and c["tip_ok"] and
                     c["ubertip_ok"] and c["revivetip_ok"] and c["awakentip_ok"])
        if not fields_ok:
            print(f"FAILED check for {c['id']}:")
            print(f"  name_ok: {c['name_ok']}, propernames_ok: {c['propernames_ok']}, tip_ok: {c['tip_ok']}, "
                  f"ubertip_ok: {c['ubertip_ok']}, revivetip_ok: {c['revivetip_ok']}, awakentip_ok: {c['awakentip_ok']}")
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
    plan_artifact = folder / "elements_heroes.json"
    apply_artifact = folder / "elements_heroes_apply.json"

    with open(plan_artifact, "w", encoding="utf-8") as f:
        json.dump({
            "race": "Elements",
            "category": "heroes",
            "total_heroes": len(heroes_data),
            "heroes": heroes_data
        }, f, ensure_ascii=False, indent=2)

    with open(apply_artifact, "w", encoding="utf-8") as f:
        json.dump({
            "race": "Elements",
            "category": "heroes",
            "wts_changed_count": len(wts_changed_ids),
            "wts_changed_ids": wts_changed_ids,
            "wts_hash_before": original_wts_hash,
            "wts_hash_after": new_wts_hash,
            "checks_summary": {
                "total_checks": len(checks),
                "passed": sum(1 for c in checks if (c["name_ok"] and c["propernames_ok"] and c["tip_ok"] and
                                                    c["ubertip_ok"] and c["revivetip_ok"] and c["awakentip_ok"])),
            },
            "checks": checks
        }, f, ensure_ascii=False, indent=2)

    print("Elements heroes update completed successfully!")
    print(f"Updated {len(wts_changed_ids)} WTS strings across {len(heroes_data)} heroes.")
    print(f"All {len(checks)} SD readback checks PASSED (100%).")
    print(f"All binary files: 100% intact (zero binary modifications).")

if __name__ == "__main__":
    main()
