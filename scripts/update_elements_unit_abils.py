# -*- coding: utf-8 -*-
"""Update Elements race unit/building abilities and buffs (25 abilities + 5 buffs) with SD validation."""
import hashlib
import json
from pathlib import Path
import re
import struct
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require
from apply_faceless_object_text import patch_blob

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

# Definitions of all 25 unit/building abilities and 5 buffs
UNIT_ABILITIES = [
    {
        "id": "A01N",
        "name": "|cffe4cfa3Пламя феникса|r",
        "hotkey": "E",
        "values": {
            "name": "|cffe4cfa3Пламя феникса|r",
            "tip1": "|cffe4cfa3Пламя феникса|r (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает перед собой огненного феникса, наносящего по |cffffffff100|cffced4da ед. урона всем противникам на своём пути. Максимальный суммарный урон: |cffffffff300|cffced4da ед.|r"
        }
    },
    {
        "id": "A01R",
        "name": "|cffe4cfa3Аура мороза|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Аура мороза|r",
            "tip1": "|cffe4cfa3Аура мороза|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость передвижения противников поблизости на |cffffffff20%|cffced4da и скорость их атаки на |cffffffff5%|cffced4da в радиусе |cffffffff150|cffced4da.|r"
        }
    },
    {
        "id": "A01S",
        "name": "|cffe4cfa3Кольцо огня|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Кольцо огня|r",
            "tip1": "|cffe4cfa3Кольцо огня|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Непрерывно обжигает противников вокруг себя, нанося |cffffffff6|cffced4da ед. урона в секунду в радиусе |cffffffff220|cffced4da.|r"
        }
    },
    {
        "id": "A0CE",
        "name": "|cffe4cfa3Ледяной доспех|r",
        "hotkey": "E",
        "values": {
            "name": "|cffe4cfa3Ледяной доспех|r",
            "tip1": "|cffe4cfa3Ледяной доспех|r (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Укрывает союзника ледяным щитом на |cffffffff45|cffced4da сек., повышающим броню на |cffffffff2|cffced4da ед. и замедляющим атакующих его в ближнем бою противников на |cffffffff3|cffced4da сек.|r"
        }
    },
    {
        "id": "A0I3",
        "name": "|cffe4cfa3Скачок|r",
        "hotkey": "C",
        "values": {
            "name": "|cffe4cfa3Скачок|r",
            "tip1": "|cffe4cfa3Скачок|r (|cffffffffC|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит работника на расстояние до |cffffffff500|cffced4da ед. Время восстановления: |cffffffff40|cffced4da сек.|r"
        }
    },
    {
        "id": "A0OZ",
        "name": "|cffe4cfa3Поджог|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Поджог|r",
            "tip1": "|cffe4cfa3Поджог|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет башне атаковать до |cffffffff9|cffced4da противников одновременно в радиусе |cffffffff500|cffced4da, нанося по |cffffffff25|cffced4da ед. урона каждой цели каждые |cffffffff2|cffced4da сек.|r"
        }
    },
    {
        "id": "A0PG",
        "name": "|cffe4cfa3Громовой удар|r",
        "hotkey": "Q",
        "values": {
            "name": "|cffe4cfa3Громовой удар|r",
            "tip1": "|cffe4cfa3Громовой удар|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сотрясает землю мощным ударом, нанося |cffffffff70|cffced4da ед. урона всем противникам в радиусе |cffffffff400|cffced4da.|r"
        }
    },
    {
        "id": "A0PH",
        "name": "|cffe4cfa3Поджог|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Поджог|r",
            "tip1": "|cffe4cfa3Поджог|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака поджигает цель, нанося |cffffffff2|cffced4da ед. урона в секунду в течение |cffffffff5|cffced4da сек.|r"
        }
    },
    {
        "id": "A0Q8",
        "name": "|cffe4cfa3Сожжение доспехов|r",
        "hotkey": "Q",
        "values": {
            "name": "|cffe4cfa3Сожжение доспехов|r",
            "tip1": "|cffe4cfa3Сожжение доспехов|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает доспехи цели на |cffffffff60|cffced4da сек., снижая её урон на |cffffffff10%|cffced4da и броню на |cffffffff5|cffced4da ед.|r"
        }
    },
    {
        "id": "A0Q9",
        "name": "|cffe4cfa3Рассекающий удар|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Рассекающий удар|r",
            "tip1": "|cffe4cfa3Рассекающий удар|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака наносит |cffffffff13%|cffced4da урона другим наземным противникам в радиусе |cffffffff150|cffced4da от цели.|r"
        }
    },
    {
        "id": "A0QA",
        "name": "|cffe4cfa3Критический удар|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Критический удар|r",
            "tip1": "|cffe4cfa3Критический удар|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10%|cffced4da шанс нанести двойной урон при атаке.|r"
        }
    },
    {
        "id": "A0QC",
        "name": "|cffe4cfa3Ледяные стрелы|r",
        "hotkey": "Q",
        "values": {
            "name": "|cffe4cfa3Ледяные стрелы|r",
            "tip1": "|cffe4cfa3Ледяные стрелы|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет к атаке ледяной урон, нанося дополнительно |cffffffff3|cffced4da ед. урона и замедляя скорость атаки цели на |cffffffff30%|cffced4da, а скорость передвижения — на |cffffffff30%|cffced4da на |cffffffff6|cffced4da сек. (|cffffffff1|cffced4da сек. для героев).|r"
        }
    },
    {
        "id": "A0QD",
        "name": "|cffe4cfa3Кольцо льда|r",
        "hotkey": "W",
        "values": {
            "name": "|cffe4cfa3Кольцо льда|r",
            "tip1": "|cffe4cfa3Кольцо льда|r (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает кольцо леденящей волны, наносящее цели |cffffffff75|cffced4da ед. урона и ещё |cffffffff40|cffced4da ед. урона противникам в радиусе |cffffffff150|cffced4da. Замедляет передвижение и атаку целей на |cffffffff4|cffced4da сек. (|cffffffff2|cffced4da сек. для героев).|r"
        }
    },
    {
        "id": "A0QE",
        "name": "|cffe4cfa3Пламя жизни|r",
        "hotkey": "W",
        "values": {
            "name": "|cffe4cfa3Пламя жизни|r",
            "tip1": "|cffe4cfa3Пламя жизни|r (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff150|cffced4da ед. здоровья союзникам в радиусе |cffffffff300|cffced4da.|r"
        }
    },
    {
        "id": "A0QF",
        "name": "|cffe4cfa3Сокрушение|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Сокрушение|r",
            "tip1": "|cffe4cfa3Сокрушение|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff25%|cffced4da каждая атака наносит |cffffffff15|cffced4da ед. урона противникам поблизости от цели.|r"
        }
    },
    {
        "id": "A0QH",
        "name": "|cffe4cfa3Кристаллы антимагии|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Кристаллы антимагии|r",
            "tip1": "|cffe4cfa3Кристаллы антимагии|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Кристаллическая решётка рассеивает магию, поглощая |cffffffff33%|cffced4da направленного в голема заклинательного урона.|r"
        }
    },
    {
        "id": "A0QI",
        "name": "|cffe4cfa3Бросок валуна|r",
        "hotkey": "Q",
        "values": {
            "name": "|cffe4cfa3Бросок валуна|r",
            "tip1": "|cffe4cfa3Бросок валуна|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Швыряет в противника тяжёлый валун, наносящий |cffffffff70|cffced4da ед. урона и оглушающий цель на |cffffffff1|cffced4da сек. (|cffffffff0,5|cffced4da сек. для героев).|r"
        }
    },
    {
        "id": "A0QM",
        "name": "|cffe4cfa3Невосприимчивость к магии|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Невосприимчивость к магии|r",
            "tip1": "|cffe4cfa3Невосприимчивость к магии|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует полную невосприимчивость к магии и большинству заклинаний.|r"
        }
    },
    {
        "id": "A0W7",
        "name": "|cffe4cfa3Вода|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Вода|r",
            "tip1": "|cffe4cfa3Вода|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает верховную стихию Воды. Открывает создание Особого Воды, Рифового элементаля, Загробника Глубин, Ледяного голема и Кристального голема. Блокирует базовых элементалей Воды и Каменных големов, а также выбор других верховных стихий.|r"
        }
    },
    {
        "id": "A0W8",
        "name": "|cffe4cfa3Земля|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Земля|r",
            "tip1": "|cffe4cfa3Земля|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает верховную стихию Земли. Открывает создание Особого Земли, Грязевого элементаля, Яростного голема, Гранитного голема и Янтарного Загробника. Блокирует базовых элементалей Земли и Каменных големов, а также выбор других верховных стихий.|r"
        }
    },
    {
        "id": "A0W9",
        "name": "|cffe4cfa3Огонь|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Огонь|r",
            "tip1": "|cffe4cfa3Огонь|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает верховную стихию Огня. Открывает создание Особого Огня, Огненной птицы, Загробника Огня, Огненного голема и Огненного Стража. Блокирует базовых элементалей Огня и Каменных големов, а также выбор других верховных стихий.|r"
        }
    },
    {
        "id": "A0WA",
        "name": "|cffe4cfa3Воздух|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Воздух|r",
            "tip1": "|cffe4cfa3Воздух|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает верховную стихию Ветра. Открывает создание Особого Ветра, Загробника Бури, Штормового элементаля и Воителя бури. Блокирует базовых элементалей Ветра и Каменных големов, а также выбор других верховных стихий.|r"
        }
    },
    {
        "id": "A18B",
        "name": "|cffe4cfa3Тёмный призыв|r",
        "hotkey": "W",
        "values": {
            "name": "|cffe4cfa3Тёмный призыв|r",
            "tip1": "|cffe4cfa3Тёмный призыв|r (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da После применения в течение |cffffffff3|cffced4da сек. переносит до |cffffffff36|cffced4da союзных воинов из указанной области к этой башне.|r"
        }
    },
    {
        "id": "A1MQ",
        "name": "|cffe4cfa3Ускользание|r",
        "hotkey": None,
        "values": {
            "name": "|cffe4cfa3Ускользание|r",
            "tip1": "|cffe4cfa3Ускользание|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10%|cffced4da шанс уклониться от вражеской физической атаки.|r"
        }
    },
    {
        "id": "Adis",
        "name": "|cffe4cfa3Рассеивание чар|r",
        "hotkey": "Q",
        "values": {
            "name": "|cffe4cfa3Рассеивание чар|r",
            "tip1": "|cffe4cfa3Рассеивание чар|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает положительные эффекты с противников и отрицательные с союзников в радиусе |cffffffff200|cffced4da, а также наносит |cffffffff200|cffced4da ед. урона призванным существам.|r"
        }
    }
]

BUFFS = [
    {
        "id": "B071",
        "name": "|cffe4cfa3Сожжение доспехов|r",
        "values": {
            "bufftip": "|cffe4cfa3Сожжение доспехов|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Броня этого воина снижена огненным жаром Рагнароса.|r"
        }
    },
    {
        "id": "B054",
        "name": "|cffe4cfa3Торнадо|r",
        "values": {
            "bufftip": "|cffe4cfa3Торнадо|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Этот воин находится в вихре торнадо и получает периодический урон.|r"
        }
    },
    {
        "id": "B008",
        "name": "|cffe4cfa3Аура мороза|r",
        "values": {
            "bufftip": "|cffe4cfa3Аура мороза|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки и передвижения этого воина снижена леденящим холодом.|r"
        }
    },
    {
        "id": "B055",
        "name": "|cffe4cfa3Поджог|r",
        "values": {
            "bufftip": "|cffe4cfa3Поджог|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Этот воин объят пламенем и получает периодический урон огнём.|r"
        }
    },
    {
        "id": "B056",
        "name": "|cffe4cfa3Поджог|r",
        "values": {
            "bufftip": "|cffe4cfa3Поджог|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Этот воин объят пламенем и получает периодический урон огнём.|r"
        }
    }
]

def main():
    folder = ROOT / "docs/ui_text"
    raw_map = json.load(open(folder / "elements_unit_abils_wts_map.json", encoding="utf-8"))

    source = ROOT / "map.w3x"
    wts_path = source / "war3map.wts"
    w3a_skin_path = source / "war3mapSkin.w3a"
    w3h_skin_path = source / "war3mapSkin.w3h"

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    wts_changed = []
    ability_ops = []
    buff_ops = []

    updated_wts = original_wts

    # 1. Process abilities
    for item in UNIT_ABILITIES:
        aid = item["id"]
        meta = raw_map.get(aid, {})
        for field, val in item["values"].items():
            f_meta = meta.get(field, {})
            wid = f_meta.get("wts_id")
            if wid:
                updated_wts = update_wts_string(updated_wts, wid, val)
                wts_changed.append((aid, field, wid, val))
            else:
                ability_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": field,
                    "value": val
                })

    # 2. Process buffs
    for item in BUFFS:
        bid = item["id"]
        meta = raw_map.get(bid, {})
        for field, val in item["values"].items():
            f_meta = meta.get(field, {})
            wid = f_meta.get("wts_id")
            if wid:
                updated_wts = update_wts_string(updated_wts, wid, val)
                wts_changed.append((bid, field, wid, val))
            else:
                buff_ops.append({
                    "type": "buff",
                    "id": bid,
                    "field": field,
                    "value": val
                })

    print(f"Total WTS keys to update: {len(wts_changed)}")
    print(f"Total ability ops to patch: {len(ability_ops)}")
    print(f"Total buff ops to patch: {len(buff_ops)}")

    # Write WTS
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Patch binary skins if needed
    if ability_ops:
        skin_bytes = w3a_skin_path.read_bytes()
        new_skin_bytes, _ = patch_blob(skin_bytes, ability_ops, "ability", add_missing=True)
        w3a_skin_path.write_bytes(new_skin_bytes)

    if buff_ops:
        buff_skin_bytes = w3h_skin_path.read_bytes()
        new_buff_skin, _ = patch_blob(buff_skin_bytes, buff_ops, "buff", add_missing=True)
        w3h_skin_path.write_bytes(new_buff_skin)

    # Readback checks in SD mode
    all_abils = [a["id"] for a in UNIT_ABILITIES]
    bulk_a = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(all_abils)]))
    all_buffs = [b["id"] for b in BUFFS]
    bulk_b = require(cli(["get-objects-bulk", "--type", "buff", "--ids", ",".join(all_buffs)]))

    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    lookup_a = {obj["id"]: obj["fields"] for obj in bulk_a.get("objects", [])}
    lookup_b = {obj["id"]: obj["fields"] for obj in bulk_b.get("objects", [])}

    checks = []
    mismatches = []

    for item in UNIT_ABILITIES:
        aid = item["id"]
        fields = lookup_a.get(aid, {})
        for f, expected in item["values"].items():
            actual = resolve(fields.get(f, ""))
            matched = (actual == expected)
            checks.append({"id": aid, "field": f, "expected": expected, "actual": actual, "matched": matched})
            if not matched:
                mismatches.append((aid, f, expected, actual))

    for item in BUFFS:
        bid = item["id"]
        fields = lookup_b.get(bid, {})
        for f, expected in item["values"].items():
            actual = resolve(fields.get(f, ""))
            matched = (actual == expected)
            checks.append({"id": bid, "field": f, "expected": expected, "actual": actual, "matched": matched})
            if not matched:
                mismatches.append((bid, f, expected, actual))

    print(f"\nSD readback validation: {len(checks) - len(mismatches)}/{len(checks)} fields matched.")
    if mismatches:
        print(f"FAILED: {len(mismatches)} mismatches:")
        for obj_id, f, exp, act in mismatches:
            print(f"  [{obj_id}] {f}:\n    Expected: {repr(exp)}\n    Actual:   {repr(act)}")
        sys.exit(1)

    report = {
        "race": "elements",
        "category": "unit_abilities_and_buffs",
        "total_abilities": len(UNIT_ABILITIES),
        "total_buffs": len(BUFFS),
        "total_checks": len(checks),
        "all_matched": len(mismatches) == 0,
        "wts_keys_updated": len(wts_changed),
        "ability_ops": len(ability_ops),
        "buff_ops": len(buff_ops),
        "hashes": {
            "wts": {"before": original_wts_hash, "after": new_wts_hash}
        }
    }
    (folder / "elements_unit_abils_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    registry = {
        "abilities": UNIT_ABILITIES,
        "buffs": BUFFS
    }
    (folder / "elements_unit_abils.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Report saved to docs/ui_text/elements_unit_abils_apply.json")
    print("Registry saved to docs/ui_text/elements_unit_abils.json")
    print("All unit abilities and buffs successfully validated in SD mode!")

if __name__ == "__main__":
    main()
