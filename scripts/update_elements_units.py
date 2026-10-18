# -*- coding: utf-8 -*-
"""Data definitions and updater for Elements race units (32 units)."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli
from apply_faceless_object_text import patch_blob

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING {string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def get_units_data():
    return [
        # --- 1. Worker ---
        {
            "id": "e00F",
            "name": "|cffe4cfa3Дух стихий|r",
            "tip": "|cffe4cfa3Дух стихий|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий стихий. "
                "Добывает золото и древесину, возводит и ремонтирует здания стихий. "
                "Способен совершать мгновенный скачок и рассеивать чары ценой своей жизни при детонации.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткую дистанцию.|n"
                "- |cffa9c7deДетонация|cffced4da: взрывается, сжигая ману врагов и нанося урон призванным существам.|n"
                "- |cffa9c7deРемонт|cffced4da: чинит повреждённые здания стихий.|n|n"
                "|cffa6afb8Не атакует.|r"
            ),
            "wts": {"name": 25425, "tip": 27585, "ubertip": 35307},
            "hotkey": "Q"
        },

        # --- 2. Tier 3 Specials (h0ES Стихийный Бастион) ---
        {
            "id": "n07Y",
            "name": "|cffe4cfa3Особый Огня|r",
            "tip": "|cffe4cfa3Особый Огня|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Высший элементаль стихии Огня. "
                "Элитный стрелок пламени, обладающий пассивным уклонением от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 42298, "tip": 42295, "ubertip": 42297},
            "hotkey": "Q"
        },
        {
            "id": "n07X",
            "name": "|cffe4cfa3Особый Воды|r",
            "tip": "|cffe4cfa3Особый Воды|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Высший элементаль стихии Воды. "
                "Элитный стрелок водных глубин, обладающий пассивным уклонением от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 42294, "tip": 42290, "ubertip": 42292},
            "hotkey": "Q"
        },
        {
            "id": "n07W",
            "name": "|cffe4cfa3Особый Земли|r",
            "tip": "|cffe4cfa3Особый Земли|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Высший элементаль стихии Земли. "
                "Элитный стрелок каменных недр, обладающий пассивным уклонением от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 42289, "tip": 38187, "ubertip": 38190},
            "hotkey": "Q"
        },
        {
            "id": "n07Z",
            "name": "|cffe4cfa3Особый Ветра|r",
            "tip": "|cffe4cfa3Особый Ветра|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Высший элементаль стихии Ветра. "
                "Элитный стрелок бури, обладающий пассивным уклонением от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 42306, "tip": 42299, "ubertip": 42301},
            "hotkey": "Q"
        },

        # --- 3. Fire Temple (h0EO Огненные недра) ---
        {
            "id": "n02R",
            "name": "|cffe4cfa3Элементаль Огня|r",
            "tip": "|cffe4cfa3Элементаль Огня|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец стихии Огня. "
                "Воин ближнего боя, создающий вокруг себя обжигающее кольцо пламени.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deКольцо огня|cffced4da: создаёт огненный ореол, наносящий периодический урон ближайшим врагам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, обычный урон).|r"
            ),
            "wts": {"name": 14747, "ubertip": 8792},
            "object_mods": {"tip": "|cffe4cfa3Элементаль Огня|r (|cffffffffQ|r)"},  # TRIGSTR_2235 is shared
            "hotkey": "Q"
        },
        {
            "id": "n036",
            "name": "|cffe4cfa3Гончая пламени|r",
            "tip": "|cffe4cfa3Гончая пламени|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Быстрый зверь стихии Огня. "
                "Атакует врагов в ближнем бою, рассекая ударами сразу несколько целей.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deРассекающий удар|cffced4da: передаёт часть урона от атаки окружающим врагам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, обычный урон).|r"
            ),
            "wts": {"name": 15285, "tip": 6219, "ubertip": 39435},
            "hotkey": "W"
        },
        {
            "id": "n02S",
            "name": "|cffe4cfa3Возжигатель|r",
            "tip": "|cffe4cfa3Возжигатель|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Огненный маг поддержки. "
                "Ослабляет вражеские доспехи, сжигает защиту, поджигает цели и окружён огненным вихрем.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deСожжение доспехов|cffced4da: снижает броню атакуемой цели.|n"
                "- |cffa9c7deПоджог|cffced4da: наносит периодический урон огнём выбранному врагу.|n"
                "- |cffa9c7deКольцо огня|cffced4da: наносит периодический урон окружающим противникам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (дальний бой, магический урон).|r"
            ),
            "wts": {"name": 14890, "ubertip": 8793},
            "object_mods": {"tip": "|cffe4cfa3Возжигатель|r (|cffffffffW|r)"},  # TRIGSTR_3568 is shared
            "hotkey": "W"
        },
        {
            "id": "n07O",
            "name": "|cffe4cfa3Загробник Огня|r",
            "tip": "|cffe4cfa3Загробник Огня|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Стрелок стихии Огня. "
                "Поражает врагов с дистанции огненными снарядами и уклоняется от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 31826, "tip": 31827, "ubertip": 31837},
            "hotkey": "Q"
        },
        {
            "id": "h0F1",
            "name": "|cffe4cfa3Огненная птица|r",
            "tip": "|cffe4cfa3Огненная птица|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Могучее летающее создание стихии Огня. "
                "Атакует с воздуха магическим пламенем, наносит периодический урон огнём и поддерживает жизнь союзников.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deПламя феникса|cffced4da: обжигает ближайших врагов периодическим огненным уроном.|n"
                "- |cffa9c7deПламя жизни|cffced4da: восстанавливает жизненную силу союзных созданий.|n"
                "- |cffa9c7deКольцо огня|cffced4da: наносит урон окружающим противникам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, магический урон).|r"
            ),
            "wts": {"name": 15288, "tip": 16073, "ubertip": 39437},
            "hotkey": "R"
        },

        # --- 4. Water Temple (h0ET Морской бассейн) ---
        {
            "id": "n02U",
            "name": "|cffe4cfa3Элементаль Воды|r",
            "tip": "|cffe4cfa3Элементаль Воды|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Базовый стрелок стихии Воды. "
                "Атакует врагов водяными брызгами и способен рассеивать вражеские и союзные заклинания.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deРассеяние чар|cffced4da: снимает положительные эффекты с врагов и отрицательные с союзников, нанося урон призванным существам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 14877, "tip": 8794, "ubertip": 16059},
            "hotkey": "Q"
        },
        {
            "id": "n07C",
            "name": "|cffe4cfa3Элементаль Океана|r",
            "tip": "|cffe4cfa3Элементаль Океана|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Закалённый воин океанских глубин. "
                "Атакует с дистанции мощными потоками воды и очищает поле боя от магии.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deРассеяние чар|cffced4da: рассеивает магические эффекты и наносит урон призванным существам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 38191, "tip": 40299, "ubertip": 40529},
            "hotkey": "Q"
        },
        {
            "id": "n02T",
            "name": "|cffe4cfa3Элементаль Морей|r",
            "tip": "|cffe4cfa3Элементаль Морей|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Магический стрелок стихии Морей. "
                "Замедляет цели ледяными стрелами, защищает союзников морозным доспехом и рассеивает чары.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deЛедяные стрелы|cffced4da: замедляет скорость перемещения и атаки поражённых врагов.|n"
                "- |cffa9c7deМорозный доспех|cffced4da: увеличивает броню союзника и замедляет атакующих его в ближнем бою.|n"
                "- |cffa9c7deРассеяние чар|cffced4da: снимает магические эффекты.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, магический урон).|r"
            ),
            "wts": {"name": 14871, "tip": 14876, "ubertip": 18692},
            "hotkey": "E"
        },
        {
            "id": "n07T",
            "name": "|cffe4cfa3Загробник Глубин|r",
            "tip": "|cffe4cfa3Загробник Глубин|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Стрелок стихии Воды из морских глубин. "
                "Поражает врагов водяными снарядами и избегает вражеских атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 38174, "tip": 38175, "ubertip": 38184},
            "hotkey": "Q"
        },
        {
            "id": "n032",
            "name": "|cffe4cfa3Рифовый Элементаль|r",
            "tip": "|cffe4cfa3Рифовый Элементаль|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Могучий высший элементаль коралловых рифов. "
                "Атакует врагов магией воды и сокрушает их ледяным кольцом холода.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deКольцо льда|cffced4da: взрывается ледяной волной, наносящей урон и замедляющей врагов в области действия.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, магический урон).|r"
            ),
            "wts": {"name": 14898, "tip": 14899, "ubertip": 39158},
            "hotkey": "R"
        },
        {
            "id": "n02Z",
            "name": "|cffe4cfa3Грязевой Элементаль|r",
            "tip": "|cffe4cfa3Грязевой Элементаль|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Осадный элементаль земли и воды. "
                "Наносит огромный урон зданиям, способен опутывать врагов корнями и погружаться под воду.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deОпутывание|cffced4da: обездвиживает вражеского юнита и наносит ему периодический урон.|n"
                "- |cffa9c7deПогружение|cffced4da: позволяет скрываться под водой.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, осадный урон).|r"
            ),
            "wts": {"name": 14754, "tip": 14780, "ubertip": 36363},
            "hotkey": "E"
        },

        # --- 5. Air Temple (h0EU Ветролом) ---
        {
            "id": "n02Q",
            "name": "|cffe4cfa3Элементаль Ветра|r",
            "tip": "|cffe4cfa3Элементаль Ветра|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Базовый стрелок стихии Ветра. "
                "Атакует врагов воздушными порывами и уклоняется от ударов благодаря высокой скорости.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 28667, "ubertip": 8791},
            "object_mods": {"tip": "|cffe4cfa3Элементаль Ветра|r (|cffffffffQ|r)"},  # TRIGSTR_2954 is shared
            "hotkey": "Q"
        },
        {
            "id": "n02V",
            "name": "|cffe4cfa3Грозовой Элементаль|r",
            "tip": "|cffe4cfa3Грозовой Элементаль|r (|cffffffffW|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Стрелок стихии Молний. "
                "Соткан из чистой электрической энергии, наносит критические удары и уклоняется от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deКритический удар|cffced4da: даёт шанс нанести увеличенный урон при атаке.|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 14879, "tip": 14880, "ubertip": 22593},
            "hotkey": "W"
        },
        {
            "id": "n07P",
            "name": "|cffe4cfa3Воздушный волк|r",
            "tip": "|cffe4cfa3Воздушный волк|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Быстрый зверь стихии Ветра. "
                "Атакует врагов ветровыми разрядами с дистанции и уклоняется от ударов.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 31838, "tip": 31863, "ubertip": 31866},
            "hotkey": "Q"
        },
        {
            "id": "n07R",
            "name": "|cffe4cfa3Загробник Бури|r",
            "tip": "|cffe4cfa3Загробник Бури|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Стрелок стихии Бури. "
                "Поражает цели зарядами штормового ветра и обладает природным уклонением.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 31941, "tip": 31942, "ubertip": 32794},
            "hotkey": "Q"
        },
        {
            "id": "n02P",
            "name": "|cffe4cfa3Штормовой Элементаль|r",
            "tip": "|cffe4cfa3Штормовой Элементаль|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Высший элементаль Шторма. "
                "Соткан из грозовых туч и молний. Поражает врагов мощными разрядами и уклоняется от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"ubertip": 8787},
            "object_mods": {
                "name": "|cffe4cfa3Штормовой Элементаль|r",  # TRIGSTR_2951 is shared
                "tip": "|cffe4cfa3Штормовой Элементаль|r (|cffffffffR|r)"  # TRIGSTR_2952 is shared
            },
            "hotkey": "R"
        },

        # --- 6. Earth Temple (h0EW Каменоломня) ---
        {
            "id": "n02W",
            "name": "|cffe4cfa3Элементаль Земли|r",
            "tip": "|cffe4cfa3Элементаль Земли|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Базовый тяжелый боец стихии Земли. "
                "Обладает высокой прочностью и наносит разрушительный осадный урон вражеским постройкам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, осадный урон).|r"
            ),
            "wts": {"tip": 6194, "ubertip": 25274},
            "object_mods": {"name": "|cffe4cfa3Элементаль Земли|r"},  # TRIGSTR_3569 is shared
            "hotkey": "Q"
        },
        {
            "id": "n07V",
            "name": "|cffe4cfa3Песчаный Элементаль|r",
            "tip": "|cffe4cfa3Песчаный Элементаль|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый боец стихии Песка и Земли. "
                "Крепкий защитник ближнего боя, эффективно разрушающий вражеские укрепления.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, осадный урон).|r"
            ),
            "wts": {"name": 41310, "tip": 41520, "ubertip": 41918},
            "hotkey": "Q"
        },
        {
            "id": "n02X",
            "name": "|cffe4cfa3Каменный голем|r",
            "tip": "|cffe4cfa3Каменный голем|r (|cffffffffE|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый голем из цельного камня. "
                "Атакует врагов в ближнем бою и оглушает дальние цели броском массивного валуна.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deБросок валуна|cffced4da: бросает камень во врага, нанося урон и оглушая цель на несколько секунд.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, обычный урон).|r"
            ),
            "wts": {"name": 14883, "tip": 6195, "ubertip": 28311},
            "hotkey": "E"
        },
        {
            "id": "n034",
            "name": "|cffe4cfa3Огненный голем|r",
            "tip": "|cffe4cfa3Огненный голем|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Могучий гибридный голем Огня и Земли. "
                "Наносит урон от хаоса в ближнем бою, обжигает врагов кольцом огня и сбивает воздушные цели валунами.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deКольцо огня|cffced4da: наносит периодический урон огнём окружающим противникам.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные (ближний бой, урон от хаоса) и воздушные цели (дальний бой, осадный урон).|r"
            ),
            "wts": {"name": 15059, "tip": 15061, "ubertip": 16069},
            "hotkey": "R"
        },
        {
            "id": "n07N",
            "name": "|cffe4cfa3Огненный Страж|r",
            "tip": "|cffe4cfa3Огненный Страж|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Защитник рубежей стихий. "
                "Поражает наземных и воздушных врагов огненными зарядами и уклоняется от ударов.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 31670, "tip": 31671, "ubertip": 31825},
            "hotkey": "Q"
        },
        {
            "id": "n035",
            "name": "|cffe4cfa3Ледяной Голем|r",
            "tip": "|cffe4cfa3Ледяной Голем|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Могучий гибридный голем Льда и Земли. "
                "Наносит урон от хаоса в ближнем бою, сбивает летающие цели и замедляет окружающих врагов аурой мороза.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deАура мороза|cffced4da: замедляет скорость перемещения и атаки противников вблизи голема.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные (ближний бой, урон от хаоса) и воздушные цели (дальний бой, осадный урон).|r"
            ),
            "wts": {"name": 15062, "tip": 15064, "ubertip": 16070},
            "hotkey": "R"
        },
        {
            "id": "n031",
            "name": "|cffe4cfa3Кристальный голем|r",
            "tip": "|cffe4cfa3Кристальный голем|r (|cffffffffA|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Элитный кристаллический голем земли. "
                "Обладает мощной защитой от магии, снижает урон от заклинаний и сотрясает землю мощным громовым ударом.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deКристаллы антимагии|cffced4da: защищают тело голема от магического воздействия.|n"
                "- |cffa9c7deСнижение урона от способностей|cffced4da: снижает получаемый магический урон на |cffffffff33%|cffced4da.|n"
                "- |cffa9c7deГромовой удар|cffced4da: ударяет оземь, нанося урон и замедляя врагов поблизости.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, урон от хаоса).|r"
            ),
            "wts": {"name": 14896, "tip": 14897, "ubertip": 32077},
            "hotkey": "A"
        },
        {
            "id": "n07Q",
            "name": "|cffe4cfa3Воитель бури|r",
            "tip": "|cffe4cfa3Воитель бури|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Закалённый боец стихии Бури. "
                "Атакует врагов штормовыми зарядами и уклоняется от атак.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 31867, "tip": 31933, "ubertip": 31940},
            "hotkey": "Q"
        },
        {
            "id": "n07S",
            "name": "|cffe4cfa3Янтарный Загробник|r",
            "tip": "|cffe4cfa3Янтарный Загробник|r (|cffffffffQ|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Стрелок стихии Янтаря и Земли. "
                "Поражает врагов с дистанции и избегает ударов благодаря уклонению.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deУскользание|cffced4da: даёт |cffffffff15%|cffced4da вероятность уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные и воздушные цели (дальний бой, колющий урон).|r"
            ),
            "wts": {"name": 33346, "tip": 33350, "ubertip": 33378},
            "hotkey": "Q"
        },
        {
            "id": "n033",
            "name": "|cffe4cfa3Яростный голем|r",
            "tip": "|cffe4cfa3Яростный голем|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Неудержимый исполин стихии Земли. "
                "Полностью невосприимчив к магии, оглушает дальние цели броском валуна и сокрушает ряды врагов мощным ударом.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deНевосприимчивость к магии|cffced4da: даёт полный иммунитет ко всем видам заклинаний.|n"
                "- |cffa9c7deБросок валуна|cffced4da: бросает камень во врага, нанося урон и оглушая цель.|n"
                "- |cffa9c7deСокрушение|cffced4da: наносит урон по области при сокрушительном ударе.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, обычный урон).|r"
            ),
            "wts": {"name": 15054, "tip": 15055, "ubertip": 32143},
            "hotkey": "R"
        },
        {
            "id": "n02Y",
            "name": "|cffe4cfa3Гранитный голем|r",
            "tip": "|cffe4cfa3Гранитный голем|r (|cffffffffR|r)",
            "ubertip": (
                "|cffa6afb8ЮНИТ:|cffced4da Высший голем из прочнейшего гранита. "
                "Обладает огромным запасом здоровья и сотрясает землю сокрушительным громовым ударом.|n|n"
                "|cffa6afb8Способности:|cffced4da|n"
                "- |cffa9c7deГромовой удар|cffced4da: ударяет оземь, нанося урон и замедляя всех врагов вокруг.|n|n"
                "|cffa6afb8Атакует:|cffced4da наземные цели (ближний бой, обычный урон).|r"
            ),
            "wts": {"name": 14885, "tip": 14886, "ubertip": 35534},
            "hotkey": "R"
        }
    ]

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

    units_data = get_units_data()

    # Update WTS
    updated_wts = original_wts
    wts_changed_ids = []
    for u in units_data:
        for f, string_id in u.get("wts", {}).items():
            updated_wts = update_wts_string(updated_wts, string_id, u[f])
            wts_changed_ids.append(string_id)

    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Collect object mods for fields using shared WTS keys
    object_ops = []
    for u in units_data:
        for field, val in u.get("object_mods", {}).items():
            object_ops.append({
                "type": "unit",
                "id": u["id"],
                "field": field,
                "value": val
            })

    if object_ops:
        w3u_bytes = w3u_path.read_bytes()
        new_w3u, w3u_changed = patch_blob(w3u_bytes, object_ops, "unit", add_missing=True)
        w3u_path.write_bytes(new_w3u)
        new_w3u_hash = hashlib.sha256(w3u_path.read_bytes()).hexdigest()

        w3u_skin_bytes = w3u_skin_path.read_bytes()
        new_w3u_skin, w3u_skin_changed = patch_blob(w3u_skin_bytes, object_ops, "unit", add_missing=True)
        w3u_skin_path.write_bytes(new_w3u_skin)
        new_w3u_skin_hash = hashlib.sha256(w3u_skin_path.read_bytes()).hexdigest()
    else:
        new_w3u_hash = original_w3u_hash
        new_w3u_skin_hash = original_w3u_skin_hash

    # Invalidate wts cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()

    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Readback checks in SD only (per user instruction: no HD needed)
    checks = []
    unit_ids = [u["id"] for u in units_data]
    res = cli(["get-objects-bulk", "--type", "unit", "--ids", ",".join(unit_ids)])
    require_ok = res.get("ok", False)
    assert require_ok, f"Bulk check failed: {res.get('error')}"

    objects = {item["id"]: item for item in res.get("objects", [])}
    for u in units_data:
        u_id = u["id"]
        obj = objects.get(u_id, {})
        fields = obj.get("fields", {})

        act_name = resolve(fields.get("name", ""))
        act_tip = resolve(fields.get("tip", ""))
        act_ubertip = resolve(fields.get("ubertip", ""))

        checks.append({
            "id": u_id,
            "mode": "SD",
            "name_ok": act_name == u["name"],
            "tip_ok": act_tip == u["tip"],
            "ubertip_ok": act_ubertip == u["ubertip"],
            "actual_name": act_name,
            "actual_tip": act_tip,
            "actual_ubertip": act_ubertip
        })

    # Verify all checks pass
    all_ok = True
    for c in checks:
        if not (c["name_ok"] and c["tip_ok"] and c["ubertip_ok"]):
            print(f"FAILED check for {c['id']}:")
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
    plan_artifact = folder / "elements_units.json"
    apply_artifact = folder / "elements_units_apply.json"

    with open(plan_artifact, "w", encoding="utf-8") as f:
        json.dump({
            "race": "Elements",
            "category": "units",
            "total_units": len(units_data),
            "units": units_data
        }, f, ensure_ascii=False, indent=2)

    with open(apply_artifact, "w", encoding="utf-8") as f:
        json.dump({
            "race": "Elements",
            "category": "units",
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

    print("Elements units update completed successfully!")
    print(f"Updated {len(wts_changed_ids)} WTS strings across {len(units_data)} units.")
    print(f"Object ops applied: {len(object_ops)} (fields with shared WTS keys).")
    print(f"All {len(checks)} SD readback checks PASSED (100%).")
    print(f"Other binary files: 100% intact.")

if __name__ == "__main__":
    main()
