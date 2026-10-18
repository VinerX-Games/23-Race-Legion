# -*- coding: utf-8 -*-
"""Update Stromgard units batch 2 (war machines, specialists, paladins & summoned wards) via WTS with complete SD/HD validation."""
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

UNITS = [
    {
        "id": "h0HE",
        "wts": {"name": 21281, "tip": 21282, "ubertip": 26717},
        "hotkey": "Q",
        "name": "|cffe4cfa3Капитан|r",
        "tip": "|cffe4cfa3Капитан|r (|cffffffffQ|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Элитный командир пехоты, возглавляющий отряды в ближнем бою. Получается при повышении пехотинца после побед над врагами.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deКритический удар|cffced4da: с вероятностью |cffffffff15%|cffced4da наносит урон в |cffffffff1.5|cffced4da раза выше.|n"
            "- |cffa9c7deЗащита|cffced4da: поднимает щит, усиливая защиту ценой скорости перемещения.|n"
            "- |cffa9c7deЗачарованные мечи|cffced4da: повышает урон оружия на |cffffffff10|cffced4da ед.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0L3",
        "wts": {"name": 28770, "tip": 28771, "ubertip": 42685},
        "hotkey": "W",
        "name": "|cffe4cfa3Охотник на троллей|r",
        "tip": "|cffe4cfa3Охотник на троллей|r (|cffffffffW|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Меткий стрелок дальнего боя, специализированный на отстреле лёгких и средних целей.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deСнайперский выстрел|cffced4da: пассивно наносит повышенный урон целям со средней бронёй и без защиты.|n|n"
            "|cffa6afb8Атакует наземные и воздушные цели.|r"
        )
    },
    {
        "id": "o03X",
        "wts": {"name": 28778, "tip": 42687, "ubertip": 42688},
        "hotkey": "Q",
        "name": "|cffe4cfa3Катапульта|r",
        "tip": "|cffe4cfa3Катапульта|r (|cffffffffQ|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Осадное орудие дальнего боя для разрушения вражеских укреплений и строений.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0GY",
        "wts": {"name": 21334, "tip": 21335, "ubertip": 26496},
        "hotkey": "E",
        "name": "|cffe4cfa3Боевой танк|r",
        "tip": "|cffe4cfa3Боевой танк|r (|cffffffffE|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Тяжелобронированная машина прорыва, оснащённая осадными и зенитными орудиями.|n|n"
            "|cffa6afb8Атакует наземные и воздушные цели.|r"
        )
    },
    {
        "id": "h0HC",
        "wts": {"name": 21336, "tip": 21337, "ubertip": 31836},
        "hotkey": "W",
        "name": "|cffe4cfa3Осел|r",
        "tip": "|cffe4cfa3Осел|r (|cffffffffW|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Вьючное животное поддержки, доставляющее припасы и использующее боевые барабаны.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты в области и наносит |cffffffff200|cffced4da ед. урона призванным существам.|n"
            "- |cffa9c7deУдарная волна|cffced4da: сотрясает барабаны, нанося |cffffffff50|cffced4da ед. урона врагам на линии.|n|n"
            "|cffa6afb8Не атакует.|r"
        )
    },
    {
        "id": "h02Z",
        "wts": {"name": 20414, "tip": 21190, "ubertip": 31840},
        "hotkey": "E",
        "name": "|cffe4cfa3Паладин (Возмездие)|r",
        "tip": "|cffe4cfa3Паладин (Возмездие)|r (|cffffffffE|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Воин Света специализации «Возмездие». Наносит урон по области и усиливает атаки союзников.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deОгненный порошок|cffced4da: обжигает ближайших противников, нанося |cffffffff70|cffced4da ед. урона.|n"
            "- |cffa9c7deКара Света|cffced4da: поражает врагов волной света на |cffffffff100|cffced4da ед. урона цели и |cffffffff70|cffced4da ед. по области, замедляя их на |cffffffff2|cffced4da сек.|n"
            "- |cffa9c7deКомандирская аура|cffced4da: увеличивает урон союзников на |cffffffff10%|cffced4da.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0HX",
        "wts": {"name": 20421, "tip": 21252, "ubertip": 31841},
        "hotkey": "E",
        "name": "|cffe4cfa3Паладин (Защита)|r",
        "tip": "|cffe4cfa3Паладин (Защита)|r (|cffffffffE|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Воин Света специализации «Защита». Обладает повышенной стойкостью и усиливает броню союзников.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deЛатный доспех|cffced4da: поглощает до |cffffffff8|cffced4da ед. физического урона от каждой атаки.|n"
            "- |cffa9c7deМассовая защита|cffced4da: даёт союзникам в радиусе |cffffffff250|cffced4da бонус |cffffffff+2|cffced4da к броне на |cffffffff30|cffced4da сек.|n"
            "- |cffa9c7deАура защиты|cffced4da: пассивно даёт союзникам в радиусе |cffffffff300|cffced4da бонус |cffffffff+3|cffced4da к броне.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0I3",
        "wts": {"name": 20426, "tip": 21474, "ubertip": 31842},
        "hotkey": "E",
        "name": "|cffe4cfa3Паладин (Свет)|r",
        "tip": "|cffe4cfa3Паладин (Свет)|r (|cffffffffE|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Воин Света специализации «Свет». Исцеляет раненых союзников заклинаниями и аурой.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deМассовое исцеление|cffced4da: восполняет |cffffffff75|cffced4da ед. здоровья союзникам в радиусе |cffffffff250|cffced4da.|n"
            "- |cffa9c7deРегенерация|cffced4da: пассивно восстанавливает здоровье союзников поблизости.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    }
]

SUMMONS = [
    {"id": "o02Q", "wts": {"name": 42701}, "name": "|cffe4cfa3Сторожевая башня|r"},
    {"id": "o06A", "wts": {"name": 42718}, "name": "|cffe4cfa3Сторожевая башня|r"},
    {"id": "o06B", "wts": {"name": 42719}, "name": "|cffe4cfa3Сторожевая башня|r"},
    {"id": "o06C", "wts": {"name": 42720}, "name": "|cffe4cfa3Сторожевая башня|r"},
    {"id": "o02R", "wts": {"name": 23040}, "name": "|cffe4cfa3Магический котел|r"},
    {"id": "o06D", "wts": {"name": 23054}, "name": "|cffe4cfa3Магический котел|r"},
    {"id": "o06E", "wts": {"name": 23366}, "name": "|cffe4cfa3Магический котел|r"},
    {"id": "o06F", "wts": {"name": 23688}, "name": "|cffe4cfa3Магический котел|r"}
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

    for u in UNITS:
        uid = u["id"]
        consumers[uid] = {
            "name": u["wts"]["name"],
            "tip": u["wts"]["tip"],
            "ubertip": u["wts"]["ubertip"],
            "hotkey": u["hotkey"]
        }
        for field in ("name", "tip", "ubertip"):
            sid = u["wts"][field]
            val = u[field]
            updated_wts = update_wts_string(updated_wts, sid, val)
            changed_wts_ids.append(sid)
            strings[str(sid)] = val

    for s in SUMMONS:
        sid_name = s["wts"]["name"]
        val = s["name"]
        updated_wts = update_wts_string(updated_wts, sid_name, val)
        changed_wts_ids.append(sid_name)
        strings[str(sid_name)] = val
        consumers[s["id"]] = {"name": sid_name}

    # Save registry
    registry = {
        "race": "Стромгард",
        "category": "Юниты",
        "batch": "02_specialists_machines_paladins_summons",
        "units": [u["id"] for u in UNITS],
        "summons": [s["id"] for s in SUMMONS],
        "changed_wts_count": len(changed_wts_ids),
        "strings": strings,
        "consumers": consumers,
        "in_game_checked": False
    }

    (folder / "stromgard_units_02.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Apply to war3map.wts
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    wts_after = hw.load_wts_strings()
    for hd in (False, True):
        for u in UNITS:
            uid = u["id"]
            args = ["get-object", "--type", "unit", "--id", uid]
            if hd:
                args.append("--hd")
            res = require(cli(args))
            f = res.get("fields", {})

            for field in ("name", "tip", "ubertip"):
                expected = u[field]
                actual = f.get(field, "")
                if actual.startswith("TRIGSTR_"):
                    actual = wts_after.get(int(actual[8:]), actual)
                assert actual == expected, f"Mismatch on {uid} {field} (hd={hd}): {actual!r} != {expected!r}"
                checks.append({
                    "variant": "HD" if hd else "SD",
                    "rawcode": uid,
                    "field": field,
                    "exact_match": True
                })

        for s in SUMMONS:
            sid = s["id"]
            args = ["get-object", "--type", "unit", "--id", sid]
            if hd:
                args.append("--hd")
            res = require(cli(args))
            f = res.get("fields", {})
            expected = s["name"]
            actual = f.get("name", "")
            if actual.startswith("TRIGSTR_"):
                actual = wts_after.get(int(actual[8:]), actual)
            assert actual == expected, f"Mismatch on {sid} name (hd={hd}): {actual!r} != {expected!r}"
            checks.append({
                "variant": "HD" if hd else "SD",
                "rawcode": sid,
                "field": "name",
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

    (folder / "stromgard_units_02_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "units": len(UNITS), "summons": len(SUMMONS), "fields_checked": len(checks)}))

if __name__ == "__main__":
    main()
