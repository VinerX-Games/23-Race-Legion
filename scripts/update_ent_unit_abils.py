# -*- coding: utf-8 -*-
"""Update Ents (Argvinol) race unit abilities and buffs (30 abilities, 4 buffs) with complete SD/HD validation."""
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
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    w3a_path = ROOT / "map.w3x/war3map.w3a"
    w3a_skin_path = ROOT / "map.w3x/war3mapSkin.w3a"
    w3h_path = ROOT / "map.w3x/war3map.w3h"
    w3h_skin_path = ROOT / "map.w3x/war3mapSkin.w3h"

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    original_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()
    original_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()
    original_w3h_hash = hashlib.sha256(w3h_path.read_bytes()).hexdigest()
    original_w3h_skin_hash = hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name not in ["war3map.wts", "war3map.w3a", "war3mapSkin.w3a", "war3map.w3h", "war3mapSkin.w3h"]
    }

    unit_abilities_data = [
        # --- Базовые пассивные способности древней ---
        {
            "id": "A0PW",
            "name": "|cffe4cfa3Крепкая кора|r",
            "values": {
                "name": "|cffe4cfa3Крепкая кора|r",
                "tip1": "|cffe4cfa3Крепкая кора|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Плотный слой древней коры увеличивает защиту на |cffffffff1|cffced4da ед. и отражает |cffffffff10%|cffced4da полученного в ближнем бою урона обратно в атакующего врага.|r"
            }
        },
        {
            "id": "A0PU",
            "name": "|cffe4cfa3Ядовитый сок|r",
            "values": {
                "name": "|cffe4cfa3Ядовитый сок|r",
                "tip1": "|cffe4cfa3Ядовитый сок|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки отравляют цель ядовитым соком, снижая скорость передвижения на |cffffffff15%|cffced4da, скорость атаки на |cffffffff10%|cffced4da и нанося |cffffffff4|cffced4da ед. урона в секунду в течение |cffffffff5|cffced4da сек. (по героям — |cffffffff1|cffced4da сек.).|r"
            }
        },

        # --- Энт дробитель (e02K) ---
        {
            "id": "A0Q2",
            "name": "|cffe4cfa3Сильный удар|r",
            "values": {
                "name": "|cffe4cfa3Сильный удар|r",
                "tip1": "|cffe4cfa3Сильный удар|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff20%|cffced4da наносит дополнительный урон при атаке и оглушает противника на |cffffffff2|cffced4da сек. (героев — на |cffffffff1|cffced4da сек.).|r"
            }
        },

        # --- Гончая Жизни (e02L) ---
        {
            "id": "A0O7",
            "name": "|cffe4cfa3Ядро Жизни|r",
            "values": {
                "name": "|cffe4cfa3Ядро Жизни|r",
                "tip1": "|cffe4cfa3Ядро Жизни|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает запас жизненной энергии, восстанавливая цели |cffffffff15|cffced4da ед. здоровья.|r"
            }
        },
        {
            "id": "A0PX",
            "name": "|cffe4cfa3Аура ядра жизни|r",
            "values": {
                "name": "|cffe4cfa3Аура ядра жизни|r",
                "tip1": "|cffe4cfa3Аура ядра жизни|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Излучает целительную энергию природы, ускоряя регенерацию здоровья находящихся рядом союзников на |cffffffff100%|cffced4da.|r"
            }
        },

        # --- Малое Древо Войны (e02O) ---
        {
            "id": "A0Q6",
            "name": "|cffe4cfa3Рассекающий удар|r",
            "values": {
                "name": "|cffe4cfa3Рассекающий удар|r",
                "tip1": "|cffe4cfa3Рассекающий удар|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощные размашистые удары наносят |cffffffff13%|cffced4da урона соседним вражеским бойцам.|r"
            }
        },

        # --- Гончая Маны (e03G) ---
        {
            "id": "A0PV",
            "name": "|cffe4cfa3Ядро Маны|r",
            "values": {
                "name": "|cffe4cfa3Ядро Маны|r",
                "tip1": "|cffe4cfa3Ядро Маны|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает тайную энергию, восстанавливая выбранному союзному заклинателю |cffffffff10|cffced4da ед. маны.|r"
            }
        },
        {
            "id": "A0PY",
            "name": "|cffe4cfa3Аура магического ядра|r",
            "values": {
                "name": "|cffe4cfa3Аура магического ядра|r",
                "tip1": "|cffe4cfa3Аура магического ядра|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Излучает потоки природной магии, ускоряя восстановление маны находящихся рядом союзных заклинателей.|r"
            }
        },

        # --- Лесной Дух (e02V) ---
        {
            "id": "A1P2",
            "name": "|cffe4cfa3Контроль Магии|r",
            "values": {
                "name": "|cffe4cfa3Контроль Магии|r",
                "tip1": "|cffe4cfa3Контроль Магии|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Похищает положительный эффект с вражеского бойца и передаёт его союзнику, либо снимает отрицательное заклинание с союзника и переносит его на ближайшего врага.|r"
            }
        },
        {
            "id": "A1P0",
            "name": "|cffe4cfa3Гнев деревьев|r",
            "values": {
                "name": "|cffe4cfa3Гнев деревьев|r",
                "tip1": "|cffe4cfa3Гнев деревьев|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из земли цепкие корни, которые опутывают противника, лишая его движения и возможности атаковать, и наносят |cffffffff15|cffced4da ед. урона в секунду.|r"
            }
        },
        {
            "id": "A1P1",
            "name": "|cffe4cfa3Эссенция Яда|r",
            "values": {
                "name": "|cffe4cfa3Эссенция Яда|r",
                "tip1": "|cffe4cfa3Эссенция Яда|r (|cffffffffE|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком едкого яда, нанося |cffffffff10|cffced4da ед. урона мгновенно и периодический урон в течение времени действия, а также замедляя её передвижение.|r"
            }
        },

        # --- Древо Познания (e03A) ---
        {
            "id": "A0QP",
            "name": "|cffe4cfa3Рассеивание заклинаний|r",
            "values": {
                "name": "|cffe4cfa3Рассеивание заклинаний|r",
                "tip1": "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Развеивает все положительные и отрицательные эффекты в указанной области, нанося |cffffffff200|cffced4da ед. урона призванным существам.|r"
            }
        },
        {
            "id": "A0PZ",
            "name": "|cffe4cfa3Покровительство Леса|r",
            "values": {
                "name": "|cffe4cfa3Покровительство Леса|r",
                "tip1": "|cffe4cfa3Покровительство Леса|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Благословляет выбранный союзный отряд, повышая его урон на |cffffffff10%|cffced4da и показатель брони на |cffffffff5|cffced4da ед.|r"
            }
        },
        {
            "id": "A0Q7",
            "name": "|cffe4cfa3Мудрость Лесов|r",
            "values": {
                "name": "|cffe4cfa3Мудрость Лесов|r",
                "tip1": "|cffe4cfa3Мудрость Лесов|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Древняя природная защита уменьшает входящий урон от вражеских заклинаний, магии и дистанционных пронзающих атак.|r"
            }
        },

        # --- Древо Ветров (e02M) ---
        {
            "id": "A1OY",
            "name": "|cffe4cfa3Смерч|r",
            "values": {
                "name": "|cffe4cfa3Смерч|r",
                "tip1": "|cffe4cfa3Смерч|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает вражеского воина в воздух сильным вихрем, выводя его из боя на время действия. Не действует на осадные орудия и здания.|r"
            }
        },
        {
            "id": "A1OZ",
            "name": "|cffe4cfa3Аура Ветров|r",
            "values": {
                "name": "|cffe4cfa3Аура Ветров|r",
                "tip1": "|cffe4cfa3Аура Ветров|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Потоки попутного ветра дают |cffffffff10%|cffced4da шанс уклониться от вражеских атак.|r"
            }
        },

        # --- Лесной Голем (e02N) ---
        {
            "id": "A0Q1",
            "name": "|cffe4cfa3Крепкий панцирь|r",
            "values": {
                "name": "|cffe4cfa3Крепкий панцирь|r",
                "tip1": "|cffe4cfa3Крепкий панцирь|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Монолитный каменный панцирь поглощает до |cffffffff12|cffced4da ед. урона при каждой вражеской атаке с вероятностью |cffffffff100%|cffced4da (минимальный получаемый урон — |cffffffff3|cffced4da ед.).|r"
            }
        },

        # --- Лесной Дракончик (e03O) ---
        {
            "id": "A1PL",
            "name": "|cffe4cfa3Слияние с Лесом|r",
            "values": {
                "name": "|cffe4cfa3Слияние с Лесом|r",
                "tip1": "|cffe4cfa3Слияние с Лесом|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При получении урона дракончик временно переходит в астральное состояние, становясь неуязвимым для атак на короткое время.|r"
            }
        },
        {
            "id": "A1PK",
            "name": "|cffe4cfa3Вспышка маны|r",
            "values": {
                "name": "|cffe4cfa3Вспышка маны|r",
                "tip1": "|cffe4cfa3Вспышка маны|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дракончик раскрывает крылья, повышая свою броню и выпуская сгустки магии, наносящие урон врагам при сотворении ими заклинаний поблизости.|r"
            }
        },
        {
            "id": "A1PM",
            "name": "|cffe4cfa3Невосприимчивость к магии|r",
            "values": {
                "name": "|cffe4cfa3Невосприимчивость к магии|r",
                "tip1": "|cffe4cfa3Невосприимчивость к магии|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обеспечивает абсолютную защиту от воздействия любых вражеских и дружественных заклинаний.|r"
            }
        },

        # --- Дриада (e02P) ---
        {
            "id": "A1P3",
            "name": "|cffe4cfa3Рассеяние чар|r",
            "values": {
                "name": "|cffe4cfa3Рассеяние чар|r",
                "tip1": "|cffe4cfa3Рассеяние чар|r (|cffffffffB|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает отрицательные заклинания с союзников и положительные с врагов, нанося |cffffffff250|cffced4da ед. урона призванным существам.|r"
            }
        },

        # --- Хранитель Рощи (e03M) ---
        {
            "id": "A0Q3",
            "name": "|cffe4cfa3Зов Древних|r",
            "values": {
                "name": "|cffe4cfa3Зов Древних|r",
                "tip1": "|cffe4cfa3Зов Древних|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь |cffffffff2|cffced4da малых древней на |cffffffff70|cffced4da сек.|r"
            }
        },
        {
            "id": "A0Q4",
            "name": "|cffe4cfa3Древесный покров|r",
            "values": {
                "name": "|cffe4cfa3Древесный покров|r",
                "tip1": "|cffe4cfa3Древесный покров|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Укрывает союзников защитной листвой, повышая показатель брони находящихся рядом бойцов на |cffffffff2|cffced4da ед.|r"
            }
        },
        {
            "id": "A0Q5",
            "name": "|cffe4cfa3Cпокойствие Леса|r",
            "values": {
                "name": "|cffe4cfa3Cпокойствие Леса|r",
                "tip1": "|cffe4cfa3Cпокойствие Леса|r (|cffffffffE|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает поток живительной энергии, восстанавливающий по |cffffffff5|cffced4da ед. здоровья в секунду союзникам в обширной области в течение |cffffffff10|cffced4da сек.|r"
            }
        },

        # --- Дух Леса (e03U / e03V) ---
        {
            "id": "A1PQ",
            "name": "|cffe4cfa3Страж Леса|r",
            "values": {
                "name": "|cffe4cfa3Страж Леса|r",
                "tip1": "|cffe4cfa3Страж Леса|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает из трупов павших воинов неуязвимых духов возмездия, атакующих врагов до гибели призвавшей их аватары.|r"
            }
        }
    ]

    buffs_data = [
        {
            "id": "B07R",
            "name": "|cffe4cfa3Аура ядра жизни|r",
            "values": {
                "bufftip": "|cffe4cfa3Аура ядра жизни|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Ускоренное восстановление здоровья под действием ауры ядра жизни.|r"
            }
        },
        {
            "id": "B08X",
            "name": "|cffe4cfa3Древесный покров|r",
            "values": {
                "bufftip": "|cffe4cfa3Древесный покров|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Повышенный показатель брони под действием древесного покрова.|r"
            }
        },
        {
            "id": "B090",
            "name": "|cffe4cfa3Страж Леса|r",
            "values": {
                "bufftip": "|cffe4cfa3Страж Леса|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Призванный дух возмездия, неуязвимый к вражеским атакам.|r"
            }
        },
        {
            "id": "B08V",
            "name": "|cffe4cfa3Покровительство Леса|r",
            "values": {
                "bufftip": "|cffe4cfa3Покровительство Леса|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Повышенный урон и показатель брони под благословением леса.|r"
            }
        }
    ]

    full_audit = json.loads((folder / "ent_unit_abils_full_audit.json").read_text(encoding="utf-8"))
    audit_abils = full_audit.get("abilities", {})
    audit_buffs = full_audit.get("buffs", {})

    updated_wts = original_wts
    wts_changed_ids = []
    ability_ops = []
    buff_ops = []

    # Update abilities
    for a in unit_abilities_data:
        aid = a["id"]
        audit_fields = audit_abils.get(aid, {}).get("fields", {})
        for f, val in a["values"].items():
            finfo = audit_fields.get(f)
            if finfo and finfo.get("is_wts"):
                string_id = finfo["wts_id"]
                updated_wts = update_wts_string(updated_wts, string_id, val)
                wts_changed_ids.append(string_id)
            else:
                ability_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": f,
                    "value": val
                })

    # Update buffs
    for b in buffs_data:
        bid = b["id"]
        audit_fields = audit_buffs.get(bid, {}).get("fields", {})
        for f, val in b["values"].items():
            finfo = audit_fields.get(f)
            if finfo and finfo.get("is_wts"):
                string_id = finfo["wts_id"]
                updated_wts = update_wts_string(updated_wts, string_id, val)
                wts_changed_ids.append(string_id)
            else:
                buff_ops.append({
                    "type": "buff",
                    "id": bid,
                    "field": f,
                    "value": val
                })

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Patch abilities
    if ability_ops:
        w3a_bytes = w3a_path.read_bytes()
        new_w3a, _ = patch_blob(w3a_bytes, ability_ops, "ability", add_missing=True)
        w3a_path.write_bytes(new_w3a)
        new_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()

        w3a_skin_bytes = w3a_skin_path.read_bytes()
        new_w3a_skin, _ = patch_blob(w3a_skin_bytes, ability_ops, "ability", add_missing=True)
        w3a_skin_path.write_bytes(new_w3a_skin)
        new_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()
    else:
        new_w3a_hash = original_w3a_hash
        new_w3a_skin_hash = original_w3a_skin_hash

    # Patch buffs
    if buff_ops:
        w3h_bytes = w3h_path.read_bytes()
        new_w3h, _ = patch_blob(w3h_bytes, buff_ops, "buff", add_missing=True)
        w3h_path.write_bytes(new_w3h)
        new_w3h_hash = hashlib.sha256(w3h_path.read_bytes()).hexdigest()

        w3h_skin_bytes = w3h_skin_path.read_bytes()
        new_w3h_skin, _ = patch_blob(w3h_skin_bytes, buff_ops, "buff", add_missing=True)
        w3h_skin_path.write_bytes(new_w3h_skin)
        new_w3h_skin_hash = hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest()
    else:
        new_w3h_hash = original_w3h_hash
        new_w3h_skin_hash = original_w3h_skin_hash

    # Reset cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()

    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Readback checks in SD and HD
    checks = []
    abil_ids = [a["id"] for a in unit_abilities_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(abil_ids), "--fields", "name,tip,ubertip,tip1,ubertip1"] + hd_flag))
        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

        for a in unit_abilities_data:
            fields = objects_by_id.get(a["id"], {})
            for f, expected in a["values"].items():
                actual = resolve(fields.get(f, ""))
                assert actual == expected, f"{f} mismatch for ability {a['id']} (hd={hd}):\nActual: '{actual}'\nExpected: '{expected}'"

            checks.append({
                "id": a["id"],
                "variant": "HD" if hd else "SD",
                "fields_verified": list(a["values"].keys())
            })

    buff_ids = [b["id"] for b in buffs_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk_buffs = require(cli(["get-objects-bulk", "--type", "buff", "--ids", ",".join(buff_ids), "--fields", "bufftip,buffubertip"] + hd_flag))
        buffs_by_id = {obj["id"]: obj["fields"] for obj in bulk_buffs.get("objects", [])}

        for b in buffs_data:
            fields = buffs_by_id.get(b["id"], {})
            for f, expected in b["values"].items():
                actual = resolve(fields.get(f, ""))
                assert actual == expected, f"{f} mismatch for buff {b['id']} (hd={hd}):\nActual: '{actual}'\nExpected: '{expected}'"

            checks.append({
                "id": b["id"],
                "variant": "HD" if hd else "SD",
                "fields_verified": list(b["values"].keys())
            })

    # Verify other binary files remain untouched
    for name, expected_hash in other_binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    registry = {
        "race": "Ents",
        "category": "unit_abilities_and_buffs",
        "total_abilities": len(unit_abilities_data),
        "total_buffs": len(buffs_data),
        "abilities": unit_abilities_data,
        "buffs": buffs_data
    }
    (folder / "ent_unit_abils.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Ents",
        "category": "unit_abilities_and_buffs",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "w3a_hash_before": original_w3a_hash,
        "w3a_hash_after": new_w3a_hash,
        "w3a_skin_hash_before": original_w3a_skin_hash,
        "w3a_skin_hash_after": new_w3a_skin_hash,
        "w3h_hash_before": original_w3h_hash,
        "w3h_hash_after": new_w3h_hash,
        "w3h_skin_hash_before": original_w3h_skin_hash,
        "w3h_skin_hash_after": new_w3h_skin_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "ent_unit_abils_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(unit_abilities_data)} Ent unit abilities and {len(buffs_data)} buffs.")
    print(f"Updated {len(set(wts_changed_ids))} WTS keys, {len(ability_ops)} ability patches, {len(buff_ops)} buff patches.")
    print(f"Verified {len(checks)} SD/HD checks.")

if __name__ == "__main__":
    main()
