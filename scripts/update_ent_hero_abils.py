# -*- coding: utf-8 -*-
"""Update Ents (Argvinol) race hero abilities (12 abilities, 42 levels) with complete SD/HD validation."""
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

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    original_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()
    original_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name not in ["war3map.wts", "war3map.w3a", "war3mapSkin.w3a"]
    }

    hero_abils_data = [
        # --- E02S Лесной Смотритель ---
        {
            "id": "A0PT",
            "hero_id": "E02S",
            "name": "|cffe4cfa3Тернистый куст|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Тернистый куст|r",
                "researchtip": "|cffe4cfa3Изучить Тернистый куст|r (|cffffffffQ|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает полосу острых шипов по линии удара, "
                    "подбрасывая противников в воздух, оглушая их и нанося урон.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: |cffffffff150|cffced4da урона, оглушение на |cffffffff3|cffced4da сек.|n"
                    "|cffa6afb8Уровень 2|cffced4da: |cffffffff200|cffced4da урона, оглушение на |cffffffff4|cffced4da сек.|n"
                    "|cffa6afb8Уровень 3|cffced4da: |cffffffff250|cffced4da урона, оглушение на |cffffffff5|cffced4da сек.|n"
                    "|cffa6afb8Уровень 4|cffced4da: |cffffffff300|cffced4da урона, оглушение на |cffffffff6|cffced4da сек.|r"
                ),
                "tip1": "|cffe4cfa3Тернистый куст — уровень 1|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff150|cffced4da урона и оглушает врагов по линии удара на |cffffffff3|cffced4da сек.|r",
                "tip2": "|cffe4cfa3Тернистый куст — уровень 2|r (|cffffffffQ|r)",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff200|cffced4da урона и оглушает врагов по линии удара на |cffffffff4|cffced4da сек.|r",
                "tip3": "|cffe4cfa3Тернистый куст — уровень 3|r (|cffffffffQ|r)",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff250|cffced4da урона и оглушает врагов по линии удара на |cffffffff5|cffced4da сек.|r",
                "tip4": "|cffe4cfa3Тернистый куст — уровень 4|r (|cffffffffQ|r)",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff300|cffced4da урона и оглушает врагов по линии удара на |cffffffff6|cffced4da сек.|r"
            }
        },
        {
            "id": "A0FW",
            "hero_id": "E02S",
            "name": "|cffe4cfa3Аура шипов|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Аура шипов|r",
                "researchtip": "|cffe4cfa3Изучить Ауру шипов|r (|cffffffffR|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя и союзников поблизости колючим щитом, "
                    "отражающим часть полученного в ближнем бою урона обратно в атакующего врага.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: отражает |cffffffff10%|cffced4da урона.|n"
                    "|cffa6afb8Уровень 2|cffced4da: отражает |cffffffff20%|cffced4da урона.|n"
                    "|cffa6afb8Уровень 3|cffced4da: отражает |cffffffff30%|cffced4da урона.|n"
                    "|cffa6afb8Уровень 4|cffced4da: отражает |cffffffff40%|cffced4da урона.|r"
                ),
                "tip1": "|cffe4cfa3Аура шипов — уровень 1|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отражает |cffffffff10%|cffced4da полученного в ближнем бою урона обратно в атакующего противника.|r",
                "tip2": "|cffe4cfa3Аура шипов — уровень 2|r",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отражает |cffffffff20%|cffced4da полученного в ближнем бою урона обратно в атакующего противника.|r",
                "tip3": "|cffe4cfa3Аура шипов — уровень 3|r",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отражает |cffffffff30%|cffced4da полученного в ближнем бою урона обратно в атакующего противника.|r",
                "tip4": "|cffe4cfa3Аура шипов — уровень 4|r",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отражает |cffffffff40%|cffced4da полученного в ближнем бою урона обратно в атакующего противника.|r"
            }
        },
        {
            "id": "A0PS",
            "hero_id": "E02S",
            "name": "|cffe4cfa3Рассекающий удар|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Рассекающий удар|r",
                "researchtip": "|cffe4cfa3Изучить Рассекающий удар|r (|cffffffffW|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Базовые атаки героя наносят урон нескольким врагам поблизости, "
                    "рассекая плоть стоящих рядом целей.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: наносит |cffffffff30%|cffced4da урона окружающим врагам.|n"
                    "|cffa6afb8Уровень 2|cffced4da: наносит |cffffffff35%|cffced4da урона окружающим врагам.|n"
                    "|cffa6afb8Уровень 3|cffced4da: наносит |cffffffff40%|cffced4da урона окружающим врагам.|n"
                    "|cffa6afb8Уровень 4|cffced4da: наносит |cffffffff45%|cffced4da урона окружающим врагам.|r"
                ),
                "tip1": "|cffe4cfa3Рассекающий удар — уровень 1|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff30%|cffced4da урона соседним вражеским бойцам.|r",
                "tip2": "|cffe4cfa3Рассекающий удар — уровень 2|r",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff35%|cffced4da урона соседним вражеским бойцам.|r",
                "tip3": "|cffe4cfa3Рассекающий удар — уровень 3|r",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff40%|cffced4da урона соседним вражеским бойцам.|r",
                "tip4": "|cffe4cfa3Рассекающий удар — уровень 4|r",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff45%|cffced4da урона соседним вражеским бойцам.|r"
            }
        },
        {
            "id": "A0C9",
            "hero_id": "E02S",
            "name": "|cffe4cfa3Дух Леса|r",
            "levels": 2,
            "values": {
                "name": "|cffe4cfa3Дух Леса|r",
                "researchtip": "|cffe4cfa3Изучить Дух Леса|r (|cffffffffR|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает аватару возмездия, которая поднимает неуязвимых духов "
                    "из павших тел на поле боя. Когда аватара погибает, духи исчезают.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: время жизни |cffffffff180|cffced4da сек.|n"
                    "|cffa6afb8Уровень 2|cffced4da: время жизни |cffffffff160|cffced4da сек., повышенный запас здоровья аватары.|r"
                ),
                "tip1": "|cffe4cfa3Дух Леса — уровень 1|r (|cffffffffR|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает аватару возмездия на |cffffffff180|cffced4da сек., поднимающую неуязвимых мстительных духов из павших тел.|r",
                "tip2": "|cffe4cfa3Дух Леса — уровень 2|r (|cffffffffR|r)",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает усиленную аватару возмездия на |cffffffff160|cffced4da сек., поднимающую неуязвимых мстительных духов из павших тел.|r"
            }
        },

        # --- E02Q Дух леса ---
        {
            "id": "A0PI",
            "hero_id": "E02Q",
            "name": "|cffe4cfa3Семя раздора|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Семя раздора|r",
                "researchtip": "|cffe4cfa3Изучить Семя раздора|r (|cffffffffQ|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проращивает в теле врага терновые корни, "
                    "наносящие периодический урон в течение 3 сек.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: |cffffffff30|cffced4da урона в сек.|n"
                    "|cffa6afb8Уровень 2|cffced4da: |cffffffff53|cffced4da урона в сек.|n"
                    "|cffa6afb8Уровень 3|cffced4da: |cffffffff73|cffced4da урона в сек.|n"
                    "|cffa6afb8Уровень 4|cffced4da: |cffffffff100|cffced4da урона в сек.|r"
                ),
                "tip1": "|cffe4cfa3Семя раздора — уровень 1|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проращивает колючие корни, наносящие цели |cffffffff30|cffced4da урона в секунду в течение |cffffffff3|cffced4da сек.|r",
                "tip2": "|cffe4cfa3Семя раздора — уровень 2|r (|cffffffffQ|r)",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проращивает колючие корни, наносящие цели |cffffffff53|cffced4da урона в секунду в течение |cffffffff3|cffced4da сек.|r",
                "tip3": "|cffe4cfa3Семя раздора — уровень 3|r (|cffffffffQ|r)",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проращивает колючие корни, наносящие цели |cffffffff73|cffced4da урона в секунду в течение |cffffffff3|cffced4da сек.|r",
                "tip4": "|cffe4cfa3Семя раздора — уровень 4|r (|cffffffffQ|r)",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проращивает колючие корни, наносящие цели |cffffffff100|cffced4da урона в секунду в течение |cffffffff3|cffced4da сек.|r"
            }
        },
        {
            "id": "A0PK",
            "hero_id": "E02Q",
            "name": "|cffe4cfa3Древесная кора|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Древесная кора|r",
                "researchtip": "|cffe4cfa3Изучить Древесную кору|r (|cffffffffW|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Укрывает союзников плотным слоем коры, "
                    "повышая их показатель защиты на 45 сек.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: +|cffffffff4|cffced4da к броне.|n"
                    "|cffa6afb8Уровень 2|cffced4da: +|cffffffff5|cffced4da к броне.|n"
                    "|cffa6afb8Уровень 3|cffced4da: +|cffffffff6|cffced4da к броне.|n"
                    "|cffa6afb8Уровень 4|cffced4da: +|cffffffff7|cffced4da к броне.|r"
                ),
                "tip1": "|cffe4cfa3Древесная кора — уровень 1|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает показатель брони союзников на |cffffffff4|cffced4da ед. на |cffffffff45|cffced4da сек.|r",
                "tip2": "|cffe4cfa3Древесная кора — уровень 2|r (|cffffffffW|r)",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает показатель брони союзников на |cffffffff5|cffced4da ед. на |cffffffff45|cffced4da сек.|r",
                "tip3": "|cffe4cfa3Древесная кора — уровень 3|r (|cffffffffW|r)",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает показатель брони союзников на |cffffffff6|cffced4da ед. на |cffffffff45|cffced4da сек.|r",
                "tip4": "|cffe4cfa3Древесная кора — уровень 4|r (|cffffffffW|r)",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает показатель брони союзников на |cffffffff7|cffced4da ед. на |cffffffff45|cffced4da сек.|r"
            }
        },
        {
            "id": "A0PJ",
            "hero_id": "E02Q",
            "name": "|cffe4cfa3Влияние леса|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Влияние леса|r",
                "researchtip": "|cffe4cfa3Изучить Влияние леса|r (|cffffffffE|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура живой природы ускоряет регенерацию здоровья "
                    "всех союзников поблизости.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: ускоряет восстановление на |cffffffff100%|cffced4da.|n"
                    "|cffa6afb8Уровень 2|cffced4da: ускоряет восстановление на |cffffffff150%|cffced4da.|n"
                    "|cffa6afb8Уровень 3|cffced4da: ускоряет восстановление на |cffffffff200%|cffced4da.|n"
                    "|cffa6afb8Уровень 4|cffced4da: ускоряет восстановление на |cffffffff250%|cffced4da.|r"
                ),
                "tip1": "|cffe4cfa3Влияние леса — уровень 1|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию здоровья находящихся рядом союзников на |cffffffff100%|cffced4da.|r",
                "tip2": "|cffe4cfa3Влияние леса — уровень 2|r",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию здоровья находящихся рядом союзников на |cffffffff150%|cffced4da.|r",
                "tip3": "|cffe4cfa3Влияние леса — уровень 3|r",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию здоровья находящихся рядом союзников на |cffffffff200%|cffced4da.|r",
                "tip4": "|cffe4cfa3Влияние леса — уровень 4|r",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию здоровья находящихся рядом союзников на |cffffffff250%|cffced4da.|r"
            }
        },
        {
            "id": "A0PL",
            "hero_id": "E02Q",
            "name": "|cffe4cfa3Кара леса|r",
            "levels": 2,
            "values": {
                "name": "|cffe4cfa3Кара леса|r",
                "researchtip": "|cffe4cfa3Изучить Кару леса|r (|cffffffffR|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает семена гнева, сотрясающие землю, наносящие урон "
                    "и замедляющие скорость атаки и перемещения врагов в области на 50%.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: |cffffffff250|cffced4da урона, замедление на |cffffffff5|cffced4da сек.|n"
                    "|cffa6afb8Уровень 2|cffced4da: |cffffffff300|cffced4da урона, замедление на |cffffffff5|cffced4da сек.|r"
                ),
                "tip1": "|cffe4cfa3Кара леса — уровень 1|r (|cffffffffR|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff250|cffced4da урона врагам в области и замедляет их передвижение и атаку на |cffffffff50%|cffced4da на |cffffffff5|cffced4da сек.|r",
                "tip2": "|cffe4cfa3Кара леса — уровень 2|r (|cffffffffR|r)",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff300|cffced4da урона врагам в области и замедляет их передвижение и атаку на |cffffffff50%|cffced4da на |cffffffff5|cffced4da сек.|r"
            }
        },

        # --- E02R Егерь диколесья ---
        {
            "id": "A0PM",
            "hero_id": "E02R",
            "name": "|cffe4cfa3Отравленное оружие|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Отравленное оружие|r",
                "researchtip": "|cffe4cfa3Изучить Отравленное оружие|r",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снаряжает стрелы егеря ядом, наносящим периодический урон "
                    "в течение 20 сек. (по героям — 10 сек.).|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: |cffffffff4|cffced4da урона в сек.|n"
                    "|cffa6afb8Уровень 2|cffced4da: |cffffffff8|cffced4da урона в сек.|n"
                    "|cffa6afb8Уровень 3|cffced4da: |cffffffff16|cffced4da урона в сек.|n"
                    "|cffa6afb8Уровень 4|cffced4da: |cffffffff32|cffced4da урона в сек.|r"
                ),
                "tip1": "|cffe4cfa3Отравленное оружие — уровень 1|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стрелы отравляют цель, нанося |cffffffff4|cffced4da ед. урона в секунду в течение |cffffffff20|cffced4da сек. (по героям — |cffffffff10|cffced4da сек.).|r",
                "tip2": "|cffe4cfa3Отравленное оружие — уровень 2|r",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стрелы отравляют цель, нанося |cffffffff8|cffced4da ед. урона в секунду в течение |cffffffff20|cffced4da сек. (по героям — |cffffffff10|cffced4da сек.).|r",
                "tip3": "|cffe4cfa3Отравленное оружие — уровень 3|r",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стрелы отравляют цель, нанося |cffffffff16|cffced4da ед. урона в секунду в течение |cffffffff20|cffced4da сек. (по героям — |cffffffff10|cffced4da сек.).|r",
                "tip4": "|cffe4cfa3Отравленное оружие — уровень 4|r",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стрелы отравляют цель, нанося |cffffffff32|cffced4da ед. урона в секунду в течение |cffffffff20|cffced4da сек. (по героям — |cffffffff10|cffced4da сек.).|r"
            }
        },
        {
            "id": "A0PN",
            "hero_id": "E02R",
            "name": "|cffe4cfa3Зов Древних|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Зов Древних|r",
                "researchtip": "|cffe4cfa3Изучить Зов Древних|r (|cffffffffW|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает древней из лесной чащи на 70 сек. "
                    "для сражения на передовой.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: призывает |cffffffff2|cffced4da древней.|n"
                    "|cffa6afb8Уровень 2|cffced4da: призывает |cffffffff4|cffced4da древней.|n"
                    "|cffa6afb8Уровень 3|cffced4da: призывает |cffffffff6|cffced4da древней.|n"
                    "|cffa6afb8Уровень 4|cffced4da: призывает |cffffffff8|cffced4da древней.|r"
                ),
                "tip1": "|cffe4cfa3Зов Древних — уровень 1|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da древней на |cffffffff70|cffced4da сек.|r",
                "tip2": "|cffe4cfa3Зов Древних — уровень 2|r (|cffffffffW|r)",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff4|cffced4da древней на |cffffffff70|cffced4da сек.|r",
                "tip3": "|cffe4cfa3Зов Древних — уровень 3|r (|cffffffffW|r)",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff6|cffced4da древней на |cffffffff70|cffced4da сек.|r",
                "tip4": "|cffe4cfa3Зов Древних — уровень 4|r (|cffffffffW|r)",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff8|cffced4da древней на |cffffffff70|cffced4da сек.|r"
            }
        },
        {
            "id": "A0V3",
            "hero_id": "E02R",
            "name": "|cffe4cfa3Аура меткости|r",
            "levels": 4,
            "values": {
                "name": "|cffe4cfa3Аура меткости|r",
                "researchtip": "|cffe4cfa3Изучить Ауру меткости|r (|cffffffffE|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает силу дистанционных атак находящихся рядом союзных стрелков.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: +|cffffffff10%|cffced4da к урону.|n"
                    "|cffa6afb8Уровень 2|cffced4da: +|cffffffff20%|cffced4da к урону.|n"
                    "|cffa6afb8Уровень 3|cffced4da: +|cffffffff30%|cffced4da к урону.|n"
                    "|cffa6afb8Уровень 4|cffced4da: +|cffffffff40%|cffced4da к урону.|r"
                ),
                "tip1": "|cffe4cfa3Аура меткости — уровень 1|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атак союзных стрелков поблизости на |cffffffff10%|cffced4da.|r",
                "tip2": "|cffe4cfa3Аура меткости — уровень 2|r",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атак союзных стрелков поблизости на |cffffffff20%|cffced4da.|r",
                "tip3": "|cffe4cfa3Аура меткости — уровень 3|r",
                "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атак союзных стрелков поблизости на |cffffffff30%|cffced4da.|r",
                "tip4": "|cffe4cfa3Аура меткости — уровень 4|r",
                "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атак союзных стрелков поблизости на |cffffffff40%|cffced4da.|r"
            }
        },
        {
            "id": "A0PP",
            "hero_id": "E02R",
            "name": "|cffe4cfa3Корни мира|r",
            "levels": 2,
            "values": {
                "name": "|cffe4cfa3Корни мира|r",
                "researchtip": "|cffe4cfa3Изучить Корни мира|r (|cffffffffR|r)",
                "researchubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взращивает из земли могучих лесных защитников, "
                    "готовых встать на защиту родной рощи.|n|n"
                    "|cffa6afb8Уровень 1|cffced4da: призывает отряд из |cffffffff5|cffced4da древней.|n"
                    "|cffa6afb8Уровень 2|cffced4da: призывает отряд из |cffffffff6|cffced4da древней.|r"
                ),
                "tip1": "|cffe4cfa3Корни мира — уровень 1|r (|cffffffffR|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взращивает отряд из |cffffffff5|cffced4da могучих древней для участия в сражении.|r",
                "tip2": "|cffe4cfa3Корни мира — уровень 2|r (|cffffffffR|r)",
                "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взращивает отряд из |cffffffff6|cffced4da могучих древней для участия в сражении.|r"
            }
        }
    ]

    audit = json.loads((folder / "ent_hero_abils_audit.json").read_text(encoding="utf-8"))

    # Update WTS strings and prepare object ops
    updated_wts = original_wts
    wts_changed_ids = []
    object_ops = []

    for a in hero_abils_data:
        aid = a["id"]
        audit_fields = audit.get(aid, {}).get("fields", {})
        for f, val in a["values"].items():
            finfo = audit_fields.get(f)
            if finfo and finfo.get("is_wts"):
                string_id = finfo["wts_id"]
                updated_wts = update_wts_string(updated_wts, string_id, val)
                wts_changed_ids.append(string_id)
            else:
                object_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": f,
                    "value": val
                })

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    if object_ops:
        w3a_bytes = w3a_path.read_bytes()
        new_w3a, _ = patch_blob(w3a_bytes, object_ops, "ability", add_missing=True)
        w3a_path.write_bytes(new_w3a)
        new_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()

        w3a_skin_bytes = w3a_skin_path.read_bytes()
        new_w3a_skin, _ = patch_blob(w3a_skin_bytes, object_ops, "ability", add_missing=True)
        w3a_skin_path.write_bytes(new_w3a_skin)
        new_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()
    else:
        new_w3a_hash = original_w3a_hash
        new_w3a_skin_hash = original_w3a_skin_hash

    # Reset cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()

    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Readback checks in SD and HD
    checks = []
    abil_ids = [a["id"] for a in hero_abils_data]
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(abil_ids), "--fields", "name,researchtip,researchubertip,tip1,tip2,tip3,tip4,ubertip1,ubertip2,ubertip3,ubertip4"] + hd_flag))
        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

        for a in hero_abils_data:
            fields = objects_by_id.get(a["id"], {})
            for f, expected in a["values"].items():
                actual = resolve(fields.get(f, ""))
                assert actual == expected, f"{f} mismatch for {a['id']} (hd={hd}):\nActual: '{actual}'\nExpected: '{expected}'"

            checks.append({
                "id": a["id"],
                "variant": "HD" if hd else "SD",
                "fields_verified": list(a["values"].keys())
            })

    # Verify other binary files remain untouched
    for name, expected_hash in other_binary_hashes.items():
        actual_hash = hashlib.sha256((source / name).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Binary file {name} unexpectedly changed!"

    registry = {
        "race": "Ents",
        "category": "hero_abilities",
        "total_abilities": len(hero_abils_data),
        "abilities": hero_abils_data
    }
    (folder / "ent_hero_abils.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Ents",
        "category": "hero_abilities",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "w3a_hash_before": original_w3a_hash,
        "w3a_hash_after": new_w3a_hash,
        "w3a_skin_hash_before": original_w3a_skin_hash,
        "w3a_skin_hash_after": new_w3a_skin_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "ent_hero_abils_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(hero_abils_data)} Ent hero abilities.")
    print(f"Updated {len(set(wts_changed_ids))} WTS keys, {len(object_ops)} object patches.")
    print(f"Verified {len(checks)} SD/HD object checks.")

if __name__ == "__main__":
    main()
