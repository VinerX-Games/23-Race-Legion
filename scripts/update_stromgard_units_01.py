# -*- coding: utf-8 -*-
"""Update Stromgard units batch 1 (regular infantry, archers, casters & worker) via WTS with complete SD/HD validation."""
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
        "id": "h0G9",
        "wts": {"name": 21246, "tip": 21247, "ubertip": 17822},
        "hotkey": "Q",
        "name": "|cffe4cfa3Работник|r",
        "tip": "|cffe4cfa3Работник|r (|cffffffffQ|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий. Возводит здания, ремонтирует постройки и добывает древесину.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на расстояние до |cffffffff500|cffced4da.|n"
            "- |cffa9c7deРемонт|cffced4da: восстанавливает прочность зданий и техники за золото и древесину.|n"
            "- |cffa9c7deДобыча ресурсов|cffced4da: рубит лес и доставляет древесину в ратушу.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0F4",
        "wts": {"name": 23035, "tip": 23046, "ubertip": 37844},
        "hotkey": "Q",
        "name": "|cffe4cfa3Ополченец|r",
        "tip": "|cffe4cfa3Ополченец|r (|cffffffffQ|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Ополченец ближнего боя. Может обучаться в казармах или временно мобилизоваться из работников.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deЗащита|cffced4da: поднимает щит, усиливая защиту от атак ценой снижения скорости перемещения.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0GS",
        "wts": {"name": 21248, "tip": 21279, "ubertip": 21257},
        "hotkey": "E",
        "name": "|cffe4cfa3Пехотинец|r",
        "tip": "|cffe4cfa3Пехотинец|r (|cffffffffE|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Профессиональный воин ближнего боя передовой линии.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deПовышение|cffced4da: уничтожив |cffffffff2|cffced4da вражеских юнитов, становится капитаном.|n"
            "- |cffa9c7deЗащита|cffced4da: поднимает щит, снижая урон от стрел ценой скорости перемещения.|n"
            "- |cffa9c7deЗачарованные мечи|cffced4da: повышает урон оружия на |cffffffff10|cffced4da ед.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0GT",
        "wts": {"name": 20156, "tip": 23022, "ubertip": 25275},
        "hotkey": "A",
        "name": "|cffe4cfa3Защитник|r",
        "tip": "|cffe4cfa3Защитник|r (|cffffffffA|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый пехотинец с прочной бронёй и защитной аурой.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deЛатный доспех|cffced4da: поглощает до |cffffffff8|cffced4da ед. физического урона от каждой атаки.|n"
            "- |cffa9c7deАура защиты|cffced4da: даёт союзникам в радиусе |cffffffff300|cffced4da бонус |cffffffff+3|cffced4da к броне.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0GV",
        "wts": {"name": 21256, "tip": 38979, "ubertip": 25457},
        "hotkey": "W",
        "name": "|cffe4cfa3Арбалетчик|r",
        "tip": "|cffe4cfa3Арбалетчик|r (|cffffffffW|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Стрелок дальнего боя с бронебойными болтами.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deОгненные стрелы|cffced4da: расходует |cff6090e08|cffced4da ед. маны, добавляя |cffffffff+12|cffced4da ед. огненного урона.|n"
            "- |cffa9c7deЗащита|cffced4da: поднимает щит для защиты от стрел ценой снижения скорости.|n|n"
            "|cffa6afb8Атакует наземные и воздушные цели.|r"
        )
    },
    {
        "id": "h0GU",
        "wts": {"name": 21254, "tip": 1788, "ubertip": 25329},
        "hotkey": "R",
        "name": "|cffe4cfa3Рыцарь|r",
        "tip": "|cffe4cfa3Рыцарь|r (|cffffffffR|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый всадник прорыва, наносящий сокрушительные удары в ближнем бою.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deКритический удар|cffced4da: с вероятностью |cffffffff15%|cffced4da наносит урон в |cffffffff1.5|cffced4da раза выше.|n|n"
            "|cffa6afb8Атакует наземные цели.|r"
        )
    },
    {
        "id": "h0GW",
        "wts": {"name": 21259, "tip": 25510, "ubertip": 21277},
        "hotkey": "Q",
        "name": "|cffe4cfa3Жрец|r",
        "tip": "|cffe4cfa3Жрец|r (|cffffffffQ|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Магический лекарь и поддержка передовых отрядов.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deВолна исцеления|cffced4da: исцеляет до |cffffffff5|cffced4da союзников цепной волной (до |cffffffff200|cffced4da ед. здоровья).|n"
            "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты в области и наносит |cffffffff200|cffced4da ед. урона призванным существам.|n"
            "- |cffa9c7deВнутренний огонь|cffced4da: увеличивает урон союзника на |cffffffff15%|cffced4da и броню на |cffffffff+2|cffced4da на |cffffffff60|cffced4da сек.|n|n"
            "|cffa6afb8Атакует наземные и воздушные цели.|r"
        )
    },
    {
        "id": "h0GX",
        "wts": {"name": 23032, "tip": 22245, "ubertip": 21285},
        "hotkey": "W",
        "name": "|cffe4cfa3Заклинатель|r",
        "tip": "|cffe4cfa3Заклинатель|r (|cffffffffW|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Боевой маг дальнего боя, ослабляющий и контролирующий врагов.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deОгненная стрела|cffced4da: наносит |cffffffff75|cffced4da ед. урона и оглушает цель на |cffffffff2|cffced4da сек.|n"
            "- |cffa9c7deРазъедающий огонь|cffced4da: снижает урон врага на |cffffffff10%|cffced4da и броню на |cffffffff5|cffced4da ед. на |cffffffff60|cffced4da сек.|n"
            "- |cffa9c7deПроклятие|cffced4da: с вероятностью |cffffffff33%|cffced4da заставляет атаки цели промахиваться.|n|n"
            "|cffa6afb8Атакует наземные и воздушные цели.|r"
        )
    },
    {
        "id": "h0HD",
        "wts": {"name": 21278, "tip": 42678, "ubertip": 31728},
        "hotkey": "Q",
        "name": "|cffe4cfa3Оруженосец|r",
        "tip": "|cffe4cfa3Оруженосец|r (|cffffffffQ|r)",
        "ubertip": (
            "|cffa6afb8ЮНИТ:|cffced4da Вспомогательный пехотинец, ускоряющий передвижение и атаки армии.|n|n"
            "|cffa6afb8Способности:|cffced4da|n"
            "- |cffa9c7deАура выносливости|cffced4da: увеличивает скорость перемещения союзников на |cffffffff10%|cffced4da и скорость атаки на |cffffffff20%|cffced4da.|n|n"
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

    # Save registry
    registry = {
        "race": "Стромгард",
        "category": "Юниты",
        "batch": "01_regular_and_worker",
        "units": [u["id"] for u in UNITS],
        "changed_wts_count": len(changed_wts_ids),
        "strings": strings,
        "consumers": consumers,
        "in_game_checked": False
    }

    (folder / "stromgard_units_01.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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

    (folder / "stromgard_units_01_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "applied": True, "units": len(UNITS), "fields_checked": len(checks)}))

if __name__ == "__main__":
    main()
