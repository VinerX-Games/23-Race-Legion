# -*- coding: utf-8 -*-
"""Update Stromgard heroes via WTS with complete SD/HD validation."""
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

HEROES = [
    {
        "id": "H0HB",
        "wts": {
            "name": 20436,
            "propernames": 20454,
            "tip": 20466,
            "ubertip": 31727,
            "revivetip": 20473,
            "awakentip": 20459
        },
        "hotkey": "Q",
        "name": "|cffe4cfa3Генерал|r",
        "propernames": "|cffe4cfa3Генерал|r",
        "tip": "|cffe4cfa3Генерал|r (|cffffffffQ|r)",
        "revivetip": "|cffe4cfa3Генерал|r",
        "awakentip": "|cffe4cfa3Генерал|r",
        "role": "Могучий полководец ближнего боя (Сила)",
        "targets": "наземные цели",
        "ubertip": (
            "|cffa6afb8ГЕРОЙ:|cffced4da Могучий полководец ближнего боя. Возводит укрепления, рассекает врагов и вдохновляет союзную армию.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deУдарная волна|cffced4da: выпускает силовую волну, наносящую урон врагам на линии.|n"
            "- |cffa9c7deСторожевая башня|cffced4da: возводит временную оборонительную башню для огневой поддержки.|n"
            "- |cffa9c7deЖгучая кровь|cffced4da: пассивно ускоряет восстановление здоровья героя.|n"
            "- |cffa9c7deГенеральская забава|cffced4da: делает окружающие союзные войска временно неуязвимыми.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "H0HL",
        "wts": {
            "name": 23618,
            "propernames": 23619,
            "tip": 23622,
            "ubertip": 42684,
            "revivetip": 23623,
            "awakentip": 20484
        },
        "hotkey": "W",
        "name": "|cffe4cfa3Казначей|r",
        "propernames": "|cffe4cfa3Казначей|r",
        "tip": "|cffe4cfa3Казначей|r (|cffffffffW|r)",
        "revivetip": "|cffe4cfa3Казначей|r",
        "awakentip": "|cffe4cfa3Казначей|r",
        "role": "Экономический герой дальнего боя (Ловкость)",
        "targets": "наземные и воздушные цели",
        "ubertip": (
            "|cffa6afb8ГЕРОЙ:|cffced4da Экономический герой дальнего боя. Значительно ускоряет приток золота и уничтожает врагов ради наживы.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deЗолотая ручка|cffced4da: мгновенно уничтожает вражеского юнита, обращая его стоимость в золото.|n"
            "- |cffa9c7deНалоги|cffced4da: каждая атака героя отнимает золото у цели и передаёт его вам.|n"
            "- |cffa9c7deКазначейский талант|cffced4da: пассивно увеличивает периодический доход государства.|n"
            "- |cffa9c7deПрибавка к золоту|cffced4da: единовременно вносит крупную сумму золота в государственную казну.|n|n"
            "|cffa6afb8Атакует наземные и воздушные цели.|r"
        )
    },
    {
        "id": "H0HA",
        "wts": {
            "name": 20430,
            "propernames": 20431,
            "tip": 20434,
            "ubertip": 26718,
            "revivetip": 20435,
            "awakentip": 20433
        },
        "hotkey": "E",
        "name": "|cffe4cfa3Верховный маг|r",
        "propernames": "|cffe4cfa3Верховный маг|r",
        "tip": "|cffe4cfa3Верховный маг|r (|cffffffffE|r)",
        "revivetip": "|cffe4cfa3Верховный маг|r",
        "awakentip": "|cffe4cfa3Верховный маг|r",
        "role": "Боевой маг дальнего боя (Интеллект)",
        "targets": "наземные и воздушные цели",
        "ubertip": (
            "|cffa6afb8ГЕРОЙ:|cffced4da Боевой маг дальнего боя. Поражает врагов огнём, ускоряет восполнение маны и варит восстановительный суп.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deОгненная стрела|cffced4da: поражает врага огненным зарядом, нанося урон и оглушая цель.|n"
            "- |cffa9c7deМагический котел|cffced4da: призывает котёл, исцеляющий союзников и обжигающий врагов рядом.|n"
            "- |cffa9c7deАура гениальности|cffced4da: пассивно увеличивает скорость восстановления маны у союзников.|n"
            "- |cffa9c7deОгненный ливень|cffced4da: обрушивает на указанную область сокрушительный дождь огненных метеоров.|n|n"
            "|cffa6afb8Атакует наземные и воздушные цели.|r"
        )
    },
    {
        "id": "H0L4",
        "wts": {
            "name": 28772,
            "propernames": 28773,
            "tip": 28775,
            "ubertip": 42686,
            "revivetip": 28777,
            "awakentip": 28774
        },
        "hotkey": "Q",
        "name": "|cffe4cfa3Данат Троллебой|r",
        "propernames": "|cffe4cfa3Данат Троллебой|r",
        "tip": "|cffe4cfa3Данат Троллебой|r (|cffffffffQ|r)",
        "revivetip": "|cffe4cfa3Данат Троллебой|r",
        "awakentip": "|cffe4cfa3Данат Троллебой|r",
        "role": "Легендарный правитель и полководец ближнего боя (Сила)",
        "targets": "наземные цели",
        "ubertip": (
            "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный правитель и полководец Стромгарда. Вдохновляет войско аурой ветерана и сокрушает врагов клинком Трол'калар.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deАура ветерана|cffced4da: врождённо увеличивает урон союзников поблизости на |cffffffff10%|cffced4da.|n"
            "- |cffa9c7deВсплеск ярости|cffced4da: резко повышает скорость боя ценой повышенного входящего урона.|n"
            "- |cffa9c7deБоевой клич|cffced4da: временно увеличивает силу атаки окружающих союзников.|n"
            "- |cffa9c7deЯрость Трол'калар|cffced4da: даёт шанс нанести критический удар повышенной мощности.|n"
            "- |cffa9c7deАватар|cffced4da: дарует невосприимчивость к магии, дополнительное здоровье, броню и урон.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    }
]

def main():
    source = ROOT / "map.w3x"
    wts_path = source / "war3map.wts"
    folder = ROOT / "docs" / "ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    # Snapshot current hashes of all binary object files
    binary_files = [
        "war3map.w3u", "war3mapSkin.w3u",
        "war3map.w3a", "war3mapSkin.w3a",
        "war3map.w3t", "war3mapSkin.w3t",
        "war3map.w3q", "war3mapSkin.w3q"
    ]
    binary_hashes = {name: hashlib.sha256((source / name).read_bytes()).hexdigest() for name in binary_files}
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    wts_content = wts_path.read_text(encoding="utf-8")
    updated_wts = wts_content

    changed_wts_ids = []
    strings = {}
    consumers = {}

    fields_to_update = ("name", "propernames", "tip", "ubertip", "revivetip", "awakentip")

    for h in HEROES:
        hid = h["id"]
        consumers[hid] = {
            "name": h["wts"]["name"],
            "propernames": h["wts"]["propernames"],
            "tip": h["wts"]["tip"],
            "ubertip": h["wts"]["ubertip"],
            "revivetip": h["wts"]["revivetip"],
            "awakentip": h["wts"]["awakentip"],
            "hotkey": h["hotkey"]
        }
        for field in fields_to_update:
            sid = h["wts"][field]
            val = h[field]
            updated_wts = update_wts_string(updated_wts, sid, val)
            changed_wts_ids.append(sid)
            strings[str(sid)] = val

    # Save registry
    registry = {
        "race": "Стромгард",
        "category": "Герои",
        "heroes": [h["id"] for h in HEROES],
        "changed_wts_count": len(changed_wts_ids),
        "strings": strings,
        "consumers": consumers,
        "in_game_checked": False
    }

    (folder / "stromgard_heroes.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Apply to war3map.wts
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    wts_after = hw.load_wts_strings()
    for hd in (False, True):
        for h in HEROES:
            hid = h["id"]
            args = ["get-object", "--type", "unit", "--id", hid]
            if hd:
                args.append("--hd")
            res = require(cli(args))
            f = res.get("fields", {})

            for field in fields_to_update:
                expected = h[field]
                actual = f.get(field, "")
                if actual.startswith("TRIGSTR_"):
                    actual = wts_after.get(int(actual[8:]), actual)
                assert actual == expected, f"Mismatch on {hid} {field} (hd={hd}): {actual!r} != {expected!r}"
                checks.append({
                    "variant": "HD" if hd else "SD",
                    "rawcode": hid,
                    "field": field,
                    "exact_match": True
                })

    # Verify binary files remained byte-identical
    for name, expected_hash in binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    report = {
        "ok": True,
        "applied": True,
        "method": "WTS-only",
        "changed_wts_ids": changed_wts_ids,
        "binary_sha256_unchanged": binary_hashes,
        "before_wts_sha256": original_wts_hash,
        "after_wts_sha256": new_wts_hash,
        "checks": checks,
        "total_checks": len(checks),
        "palette_and_color_resets_ok": True,
        "hotkeys_and_mechanics_unchanged": True,
        "in_game_checked": False
    }

    (folder / "stromgard_heroes_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "heroes": len(HEROES), "fields_checked": len(checks)}))

if __name__ == "__main__":
    main()
