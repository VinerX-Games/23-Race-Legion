# -*- coding: utf-8 -*-
"""Update Dragon race units (all 18 units) with complete SD/HD validation."""
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

    units_data = [
        # 1. Base / Workers
        {
            "id": "o01D",
            "name": "|cffe4cfa3Строитель|r",
            "tip": "|cffe4cfa3Строитель|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Рабочий драконьих стай. Добывает ресурсы, возводит и чинит строения.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно переносит владельца на короткое расстояние|n"
                "- |cffa9c7deРемонтировать|cffced4da: восстанавливает прочность зданий и техники|n"
                "- |cffa9c7deСвязь с изумрудным сном|cffced4da: не тревожит местных духов при переходе.|n|n"
                "|cffa6afb8Атакует только наземные цели.|r"
            ),
            "wts": {"name": 14976, "tip": 15257, "ubertip": 18647},
            "hotkey": "Q"
        },
        {
            "id": "n03F",
            "name": "|cffe4cfa3Синий драконид – разведчик|r",
            "tip": "|cffe4cfa3Синий драконид – разведчик|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Быстрый разведывательный боец драконидов ближнего боя.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deРодство с магией|cffced4da: снижает получаемый магический урон на |cffffffff50%|cffced4da.|n|n"
                "|cffa6afb8Атакует только наземные цели.|r"
            ),
            "wts": {"name": 1582, "ubertip": 16916},
            "object_mods": {"tip": "|cffe4cfa3Синий драконид – разведчик|r (|cffffffffW|r)"},
            "hotkey": "W"
        },
        # 2. Bronze Flight (n03Z)
        {
            "id": "n03Q",
            "name": "|cffe4cfa3Бронзовый дракончик|r",
            "tip": "|cffe4cfa3Бронзовый дракончик|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Лёгкий летающий дракон бронзовой стаи первой ступени.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deЗамедление|cffced4da: снижает скорость боя и движения цели|n"
                "- |cffa9c7deУскользание|cffced4da: шанс избежать урона от вражеской атаки.|n|n"
                "|cffa6afb8Атакует только наземные цели.|r"
            ),
            "wts": {"name": 13752, "tip": 22512, "ubertip": 21497},
            "hotkey": "W"
        },
        {
            "id": "n03R",
            "name": "|cffe4cfa3Защитник сингулярности|r",
            "tip": "|cffe4cfa3Защитник сингулярности|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Боевой бронзовый дракон средней ступени, повелевающий искажениями пространства.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deЗеркальное изображение|cffced4da: создаёт иллюзорную копию и снимает эффекты|n"
                "- |cffa9c7deСингулярная перегрузка|cffced4da: временно увеличивает скорость боя и передвижения|n"
                "- |cffa9c7deГрозовая атака|cffced4da: поражает врагов ударами молний.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 39818, "tip": 22595, "ubertip": 21513},
            "hotkey": "E"
        },
        {
            "id": "n03S",
            "name": "|cffe4cfa3Хранитель времени|r",
            "tip": "|cffe4cfa3Хранитель времени|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Могучий древний дракон бронзовой стаи, управляющий временными потоками.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deЦепная молния|cffced4da: поражает основную цель и перескакивает на соседних врагов|n"
                "- |cffa9c7deВозврат времени|cffced4da: восстанавливает здоровье ближайшим союзникам|n"
                "- |cffa9c7deУскорение времени|cffced4da: ускоряет атаку и перемещение выбранного союзника|n"
                "- |cffa9c7deПерелет|cffced4da: медленно перелетает в выбранную область карты|n"
                "- |cffa9c7deУскользание|cffced4da: шанс избежать урона от атаки.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 39819, "tip": 22598, "ubertip": 21514},
            "hotkey": "R"
        },
        # 3. Green Flight (n041)
        {
            "id": "n03T",
            "name": "|cffe4cfa3Зеленый дракончик|r",
            "tip": "|cffe4cfa3Зеленый дракончик|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Лёгкий летающий дракон зелёной стаи первой ступени.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deФазовый сдвиг|cffced4da: переходит в иное измерение при получении удара, избегая урона|n"
                "- |cffa9c7deСвязь с изумрудным сном|cffced4da: не тревожит духов при переходе.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 13755, "tip": 22658, "ubertip": 21515},
            "hotkey": "W"
        },
        {
            "id": "n03U",
            "name": "|cffe4cfa3Изумрудный страж|r",
            "tip": "|cffe4cfa3Изумрудный страж|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Боевой зелёный дракон средней ступени, способный поражать несколько целей одновременно.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deМножественная атака|cffced4da: одновременно атакует до |cffffffff3|cffced4da целей|n"
                "- |cffa9c7deФазовый сдвиг|cffced4da: избегает входящего урона при ударе|n"
                "- |cffa9c7deСвязь с изумрудным сном|cffced4da: не тревожит духов при переходе.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 39754, "tip": 39755, "ubertip": 21516},
            "hotkey": "E"
        },
        {
            "id": "n03V",
            "name": "|cffe4cfa3Хранитель сна|r",
            "tip": "|cffe4cfa3Хранитель сна|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Древний дракон зелёной стаи, владеющий магией природы и Изумрудного Сна.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deСон|cffced4da: усыпляет вражескую цель|n"
                "- |cffa9c7deГнев деревьев|cffced4da: опутывает врага корнями, нанося периодический урон|n"
                "- |cffa9c7deИзгнание|cffced4da: перемещает цель в астрал, лишая возможности атаковать|n"
                "- |cffa9c7deПерелет|cffced4da: медленно перелетает в выбранную область карты|n"
                "- |cffa9c7deФазовый сдвиг|cffced4da: избегает входящего урона при ударе.|n|n"
                "|cffa6afb8Атакует только наземные цели.|r"
            ),
            "wts": {"name": 39756, "tip": 10915, "ubertip": 23071},
            "hotkey": "R"
        },
        # 4. Red Flight (n042)
        {
            "id": "n03K",
            "name": "|cffe4cfa3Красный дракончик|r",
            "tip": "|cffe4cfa3Красный дракончик|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Лёгкий летающий дракон красной стаи первой ступени.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deПоджог|cffced4da: воспламеняет атакованных противников, нанося периодический урон.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 11985, "tip": 16319, "ubertip": 21390},
            "hotkey": "W"
        },
        {
            "id": "n03L",
            "name": "|cffe4cfa3Вершитель жизни|r",
            "tip": "|cffe4cfa3Вершитель жизни|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Боевой дракон поддержки красной стаи средней ступени.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deИсцеляющий огонь|cffced4da: восстанавливает здоровье союзников в выбранной области|n"
                "- |cffa9c7deВосстановление|cffced4da: непрерывно лечит выбранного союзника в течение времени|n"
                "- |cffa9c7deБлагославление жизни|cffced4da: повышает урон и броню союзной цели|n"
                "- |cffa9c7deПоджог|cffced4da: воспламеняет врагов при атаке.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 10947, "tip": 13395, "ubertip": 21446},
            "hotkey": "E"
        },
        {
            "id": "n03M",
            "name": "|cffe4cfa3Защитник стаи|r",
            "tip": "|cffe4cfa3Защитник стаи|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Могучий древний красный дракон, отличающийся огромным запасом здоровья и плотной бронёй.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deПрочная чешуя|cffced4da: снижает получаемый от вражеских атак урон на |cffffffff12|cffced4da ед.|n"
                "- |cffa9c7deПламенное дыхание|cffced4da: выдыхает конус пламени, нанося урон группе врагов|n"
                "- |cffa9c7deПерелет|cffced4da: медленно перелетает в выбранную область карты|n"
                "- |cffa9c7deПоджог|cffced4da: воспламеняет цели при атаке.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 39705, "tip": 39706, "ubertip": 21496},
            "hotkey": "R"
        },
        # 5. Blue Flight (n043)
        {
            "id": "n03W",
            "name": "|cffe4cfa3Синий дракончик|r",
            "tip": "|cffe4cfa3Синий дракончик|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Лёгкий летающий дракон синей стаи первой ступени.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает положительные эффекты с врагов и наносит урон призванным|n"
                "- |cffa9c7deТелепортация|cffced4da: переносит группу союзников к дружественному наземному отряду или зданию|n"
                "- |cffa9c7deРодство с магией|cffced4da: снижает получаемый магический урон на |cffffffff50%|cffced4da|n"
                "- |cffa9c7deМорозное дыхание|cffced4da: атаки замедляют врагов.|n|n"
                "|cffa6afb8Атакует только наземные цели.|r"
            ),
            "wts": {"name": 14653, "tip": 22701, "ubertip": 27557},
            "hotkey": "W"
        },
        {
            "id": "n03X",
            "name": "|cffe4cfa3Хранитель энергии|r",
            "tip": "|cffe4cfa3Хранитель энергии|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Боевой маг синей стаи средней ступени, повелевающий разрушительной магией льда.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deБуран|cffced4da: обрушивает на выбранную область ледяные осколки|n"
                "- |cffa9c7deКольцо льда|cffced4da: наносит урон и замедляет врагов ледяным взрывом|n"
                "- |cffa9c7deЛедяная стрела|cffced4da: наносит урон и оглушает вражескую цель|n"
                "- |cffa9c7deТелепортация|cffced4da: перемещает группу союзников|n"
                "- |cffa9c7deРодство с магией|cffced4da: снижает входящий магический урон на |cffffffff50%|cffced4da.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 9790, "tip": 16380, "ubertip": 28390},
            "hotkey": "E"
        },
        {
            "id": "n03Y",
            "name": "|cffe4cfa3Хранитель магии|r",
            "tip": "|cffe4cfa3Хранитель магии|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Древний синий дракон, высший мастер чар тайной магии.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deПохищение заклинаний|cffced4da: перераспределяет магические эффекты между врагами и союзниками|n"
                "- |cffa9c7deПожирание магии|cffced4da: поглощает чары в области, восстанавливая здоровье и ману|n"
                "- |cffa9c7deВосполнение маны|cffced4da: восстанавливает ману ближайшим союзникам|n"
                "- |cffa9c7deВспышка маны|cffced4da: наносит урон врагам при сотворении ими заклинаний|n"
                "- |cffa9c7deПерелет|cffced4da: медленно перелетает в выбранную область карты|n"
                "- |cffa9c7deРодство с магией|cffced4da: снижает входящий магический урон на |cffffffff50%|cffced4da.|n|n"
                "|cffa6afb8Атакует только наземные цели.|r"
            ),
            "wts": {"name": 9791, "tip": 11986, "ubertip": 28391},
            "hotkey": "R"
        },
        # 6. Black Flight (n044)
        {
            "id": "n05Q",
            "name": "|cffe4cfa3Черный драконид – Надзиратель|r",
            "tip": "|cffe4cfa3Черный драконид – Надзиратель|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый штурмовой боец чёрной стаи ближнего боя с типом атаки хаос.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deСильный удар|cffced4da: шанс нанести повышенный урон и оглушить врага|n"
                "- |cffa9c7deПленяющая атака|cffced4da: снижает броню атакованного врага и раскрывает его позицию|n"
                "- |cffa9c7deУскользание|cffced4da: шанс избежать урона от вражеской атаки.|n|n"
                "|cffa6afb8Атакует только наземные цели.|r"
            ),
            "wts": {"name": 18657, "tip": 18671, "ubertip": 31949},
            "hotkey": "W"
        },
        {
            "id": "n03N",
            "name": "|cffe4cfa3Черный дракончик|r",
            "tip": "|cffe4cfa3Черный дракончик|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Лёгкий летающий дракон чёрной стаи первой ступени с разрушительным уроном хаоса.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deДраконья ярость|cffced4da: шанс нанести критический удар при атаке|n"
                "- |cffa9c7deУскользание|cffced4da: шанс избежать урона от атаки.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 13307, "ubertip": 31794},
            "object_mods": {"tip": "|cffe4cfa3Черный дракончик|r (|cffffffffE|r)"},
            "hotkey": "E"
        },
        {
            "id": "n03O",
            "name": "|cffe4cfa3Черный дракон|r",
            "tip": "|cffe4cfa3Черный дракон|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Могучий боевой чёрный дракон средней ступени с типом атаки хаос.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deДраконья ярость|cffced4da: шанс нанести критический удар при атаке|n"
                "- |cffa9c7deУскользание|cffced4da: шанс избежать урона от атаки.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 13404, "ubertip": 31795},
            "object_mods": {"tip": "|cffe4cfa3Черный дракон|r (|cffffffffE|r)"},
            "hotkey": "E"
        },
        {
            "id": "n03P",
            "name": "|cffe4cfa3Древний черный дракон|r",
            "tip": "|cffe4cfa3Древний черный дракон|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Колоссальный исполин чёрной стаи высшей ступени, сокрушающий врагов уроном хаоса.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deЯрость земли|cffced4da: аура, повышающая урон ближайших союзников на |cffffffff10%|cffced4da|n"
                "- |cffa9c7deДраконья ярость|cffced4da: шанс нанести критический удар при атаке|n"
                "- |cffa9c7deУскользание|cffced4da: шанс избежать урона от атаки.|n|n"
                "|cffa6afb8Атакует наземные и воздушные цели.|r"
            ),
            "wts": {"name": 13751, "ubertip": 31796},
            "object_mods": {"tip": "|cffe4cfa3Древний черный дракон|r (|cffffffffE|r)"},
            "hotkey": "E"
        }
    ]

    # Update WTS
    updated_wts = original_wts
    wts_changed_ids = []
    for u in units_data:
        for f, string_id in u.get("wts", {}).items():
            updated_wts = update_wts_string(updated_wts, string_id, u[f])
            wts_changed_ids.append(string_id)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Apply direct object mods for missing tips
    object_ops = [
        {"type": "unit", "id": "n03F", "field": "tip", "value": "|cffe4cfa3Синий драконид – разведчик|r (|cffffffffW|r)"},
        {"type": "unit", "id": "n03N", "field": "tip", "value": "|cffe4cfa3Черный дракончик|r (|cffffffffE|r)"},
        {"type": "unit", "id": "n03O", "field": "tip", "value": "|cffe4cfa3Черный дракон|r (|cffffffffE|r)"},
        {"type": "unit", "id": "n03P", "field": "tip", "value": "|cffe4cfa3Древний черный дракон|r (|cffffffffE|r)"}
    ]

    w3u_bytes = w3u_path.read_bytes()
    new_w3u, w3u_changed = patch_blob(w3u_bytes, object_ops, "unit", add_missing=True)
    w3u_path.write_bytes(new_w3u)
    new_w3u_hash = hashlib.sha256(w3u_path.read_bytes()).hexdigest()

    w3u_skin_bytes = w3u_skin_path.read_bytes()
    new_w3u_skin, w3u_skin_changed = patch_blob(w3u_skin_bytes, object_ops, "unit", add_missing=True)
    w3u_skin_path.write_bytes(new_w3u_skin)
    new_w3u_skin_hash = hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest()

    # Readback checks in SD and HD
    checks = []
    unit_ids = [u["id"] for u in units_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(unit_ids), "--fields", "name,tip,ubertip"] + hd_flag))
        wts_dict = hw.load_wts_strings()
        resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}
        for u in units_data:
            fields = objects_by_id.get(u["id"], {})
            actual_name = resolve(fields.get("name", ""))
            actual_tip = resolve(fields.get("tip", ""))
            actual_ubertip = resolve(fields.get("ubertip", ""))

            assert actual_name == u["name"], f"Name mismatch for {u['id']} (hd={hd}): {actual_name} != {u['name']}"
            assert actual_tip == u["tip"], f"Tip mismatch for {u['id']} (hd={hd}): {actual_tip} != {u['tip']}"
            assert actual_ubertip == u["ubertip"], f"Ubertip mismatch for {u['id']} (hd={hd}): {actual_ubertip} != {u['ubertip']}"

            checks.append({"id": u["id"], "variant": "HD" if hd else "SD", "fields_verified": ["name", "tip", "ubertip"]})

    # Save artifacts
    units_artifact = {
        "race": "Dragon",
        "category": "units",
        "total_units": len(units_data),
        "units": units_data
    }
    (folder / "dragon_units.json").write_text(json.dumps(units_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Dragon",
        "category": "units",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "w3u_hash_before": original_w3u_hash,
        "w3u_hash_after": new_w3u_hash,
        "w3u_skin_hash_before": original_w3u_skin_hash,
        "w3u_skin_hash_after": new_w3u_skin_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "dragon_units_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(units_data)} Dragon units ({len(wts_changed_ids)} WTS keys, 4 blob patches).")
    print(f"Verified {len(checks)} SD/HD object checks.")

if __name__ == "__main__":
    main()
