# -*- coding: utf-8 -*-
"""Update Goblins race unit/building abilities (34 abilities) and buffs (9 buffs) with complete SD validation."""
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

# Definitions of all 34 Goblin unit and building abilities
UNIT_ABILITIES = [
    # 1. A0AW Коррупция: Дисциплина (6 levels, passive)
    {
        "id": "A0AW",
        "name": "|cffe4cfa3Коррупция: Дисциплина|r",
        "hotkey": None,
        "levels": 6,
        "values": {
            "name": "|cffe4cfa3Коррупция: Дисциплина|r",
            "tip1": "|cffe4cfa3Коррупция: Дисциплина|r [|cffffffffСтепень 0/5|r]",
            "tip2": "|cffe4cfa3Коррупция: Дисциплина|r [|cffffffffСтепень 1/5|r]",
            "tip3": "|cffe4cfa3Коррупция: Дисциплина|r [|cffffffffСтепень 2/5|r]",
            "tip4": "|cffe4cfa3Коррупция: Дисциплина|r [|cffffffffСтепень 3/5|r]",
            "tip5": "|cffe4cfa3Коррупция: Дисциплина|r [|cffffffffСтепень 4/5|r]",
            "tip6": "|cffe4cfa3Коррупция: Дисциплина|r [|cffffffffСтепень 5/5|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Боевая единица полностью боеготова и дисциплинирована. Штрафы отсутствуют.|r",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за коррупции и проблем с дисциплиной скорость боя и скорость передвижения снижены на |cffffffff10%|cffced4da.|r",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за коррупции и проблем с дисциплиной скорость боя и скорость передвижения снижены на |cffffffff20%|cffced4da.|r",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за коррупции и проблем с дисциплиной скорость боя и скорость передвижения снижены на |cffffffff30%|cffced4da.|r",
            "ubertip5": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за коррупции и проблем с дисциплиной скорость боя и скорость передвижения снижены на |cffffffff40%|cffced4da.|r",
            "ubertip6": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за критической коррупции и потери дисциплины скорость боя и скорость передвижения снижены на |cffffffff50%|cffced4da.|r"
        }
    },
    # 2. A0AV Коррупция: Дефект брони (6 levels, passive)
    {
        "id": "A0AV",
        "name": "|cffe4cfa3Коррупция: Дефект брони|r",
        "hotkey": None,
        "levels": 6,
        "values": {
            "name": "|cffe4cfa3Коррупция: Дефект брони|r",
            "tip1": "|cffe4cfa3Коррупция: Дефект брони|r [|cffffffffСтепень 0/5|r]",
            "tip2": "|cffe4cfa3Коррупция: Дефект брони|r [|cffffffffСтепень 1/5|r]",
            "tip3": "|cffe4cfa3Коррупция: Дефект брони|r [|cffffffffСтепень 2/5|r]",
            "tip4": "|cffe4cfa3Коррупция: Дефект брони|r [|cffffffffСтепень 3/5|r]",
            "tip5": "|cffe4cfa3Коррупция: Дефект брони|r [|cffffffffСтепень 4/5|r]",
            "tip6": "|cffe4cfa3Коррупция: Дефект брони|r [|cffffffffСтепень 5/5|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Броня изготовлена по стандарту и не имеет дефектов. Штрафы отсутствуют.|r",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за экономии на сплавах и коррупции показатель брони снижен на |cffffffff1|cffced4da ед.|r",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за экономии на сплавах и коррупции показатель брони снижен на |cffffffff2|cffced4da ед.|r",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за экономии на сплавах и коррупции показатель брони снижен на |cffffffff3|cffced4da ед.|r",
            "ubertip5": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за экономии на сплавах и коррупции показатель брони снижен на |cffffffff4|cffced4da ед.|r",
            "ubertip6": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Из-за критического дефекта брони показатель защиты снижен на |cffffffff5|cffced4da ед.|r"
        }
    },
    # 3. A0A6 Бракованные патроны (6 levels, passive)
    {
        "id": "A0A6",
        "name": "|cffe4cfa3Бракованные патроны|r",
        "hotkey": None,
        "levels": 6,
        "values": {
            "name": "|cffe4cfa3Бракованные патроны|r",
            "tip1": "|cffe4cfa3Бракованные патроны|r [|cffffffffСтепень 5/5|r]",
            "tip2": "|cffe4cfa3Бракованные патроны|r [|cffffffffСтепень 4/5|r]",
            "tip3": "|cffe4cfa3Бракованные патроны|r [|cffffffffСтепень 3/5|r]",
            "tip4": "|cffe4cfa3Бракованные патроны|r [|cffffffffСтепень 2/5|r]",
            "tip5": "|cffe4cfa3Бракованные патроны|r [|cffffffffСтепень 1/5|r]",
            "tip6": "|cffe4cfa3Бракованные патроны|r [|cffffffffСтепень 0/5|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff35%|cffced4da выстрел оказывается бракованным и не наносит урона цели.|r",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff28%|cffced4da выстрел оказывается бракованным и не наносит урона цели.|r",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff21%|cffced4da выстрел оказывается бракованным и не наносит урона цели.|r",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff14%|cffced4da выстрел оказывается бракованным и не наносит урона цели.|r",
            "ubertip5": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff7%|cffced4da выстрел оказывается бракованным и не наносит урона цели.|r",
            "ubertip6": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Все патроны высокого качества. Брак и осечки полностью отсутствуют.|r"
        }
    },
    # 4. A0D6 Коктейль Молотова (1 level, Q)
    {
        "id": "A0D6",
        "name": "|cffe4cfa3Коктейль Молотова|r",
        "hotkey": "Q",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Коктейль Молотова|r",
            "tip1": "|cffe4cfa3Коктейль Молотова|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает бутыль с зажигательной смесью в область радиусом |cffffffff85|cffced4da, поджигающую землю и наносящую по |cffffffff6|cffced4da ед. урона в секунду в течение |cffffffff15|cffced4da сек.|r"
        }
    },
    # 5. A0AX Лечение (1 level, E)
    {
        "id": "A0AX",
        "name": "|cffe4cfa3Лечение|r",
        "hotkey": "E",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Лечение|r",
            "tip1": "|cffe4cfa3Лечение|r (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff20|cffced4da ед. здоровья раненому союзнику. Не действует на технику и механизмы.|r"
        }
    },
    # 6. A0D2 Адреналиновые инъекции (1 level, Q)
    {
        "id": "A0D2",
        "name": "|cffe4cfa3Адреналиновые инъекции|r",
        "hotkey": "Q",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Адреналиновые инъекции|r",
            "tip1": "|cffe4cfa3Адреналиновые инъекции|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вводит боевой стимулятор на |cffffffff15|cffced4da сек., увеличивая скорость атаки на |cffffffff10%|cffced4da и скорость передвижения на |cffffffff35%|cffced4da, но отнимая часть текущего здоровья.|r"
        }
    },
    # 7. A0Z4 Огнеметная турель (1 level, E)
    {
        "id": "A0Z4",
        "name": "|cffe4cfa3Огнеметная турель|r",
        "hotkey": "E",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Огнеметная турель|r",
            "tip1": "|cffe4cfa3Огнеметная турель|r (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Устанавливает стационарную огнемётную турель на |cffffffff40|cffced4da сек., непрерывно сжигающую приближающихся противников.|r"
        }
    },
    # 8. A0D1 ЭМИ-граната (1 level, W)
    {
        "id": "A0D1",
        "name": "|cffe4cfa3ЭМИ-граната|r",
        "hotkey": "W",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3ЭМИ-граната|r",
            "tip1": "|cffe4cfa3ЭМИ-граната|r (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает электромагнитную гранату в область радиусом |cffffffff200|cffced4da, рассеивающую положительные чары с врагов и отрицательные с союзников, а также наносящую |cffffffff200|cffced4da ед. урона призванным существам.|r"
        }
    },
    # 9. A0AB Поджог (1 level, passive)
    {
        "id": "A0AB",
        "name": "|cffe4cfa3Поджог|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Поджог|r",
            "tip1": "|cffe4cfa3Поджог|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки поджигают поражённую цель, нанося по |cffffffff5|cffced4da ед. урона в секунду в течение |cffffffff12|cffced4da сек. (|cffffffff1|cffced4da сек. по героям).|r"
        }
    },
    # 10. A0AR Шанс самоподжога (6 levels, passive)
    {
        "id": "A0AR",
        "name": "|cffe4cfa3Шанс самоподжога|r",
        "hotkey": None,
        "levels": 6,
        "values": {
            "name": "|cffe4cfa3Шанс самоподжога|r",
            "tip1": "|cffe4cfa3Шанс самоподжога|r [|cffffffffСтепень 5/5|r]",
            "tip2": "|cffe4cfa3Шанс самоподжога|r [|cffffffffСтепень 4/5|r]",
            "tip3": "|cffe4cfa3Шанс самоподжога|r [|cffffffffСтепень 3/5|r]",
            "tip4": "|cffe4cfa3Шанс самоподжога|r [|cffffffffСтепень 2/5|r]",
            "tip5": "|cffe4cfa3Шанс самоподжога|r [|cffffffffСтепень 1/5|r]",
            "tip6": "|cffe4cfa3Шанс самоподжога|r [|cffffffffСтепень 0/5|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высокая вероятность самовоспламенения горючей смеси при стрельбе из-за критических дефектов топливной системы.|r",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заметная вероятность самовоспламенения горючей смеси при стрельбе из-за дефектов топливной системы.|r",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Умеренная вероятность самовоспламенения горючей смеси при стрельбе из-за дефектов топливной системы.|r",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Небольшая вероятность самовоспламенения горючей смеси при стрельбе.|r",
            "ubertip5": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Минимальная вероятность самовоспламенения горючей смеси при стрельбе.|r",
            "ubertip6": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Огнемётная система полностью герметична и безопасна. Дефекты и риск самоподжога отсутствуют.|r"
        }
    },
    # 11. A0A8 Взрыв напоследок (1 level, passive)
    {
        "id": "A0A8",
        "name": "|cffe4cfa3Взрыв напоследок|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Взрыв напоследок|r",
            "tip1": "|cffe4cfa3Взрыв напоследок|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При уничтожении техника взрывается, нанося урон всем окружающим наземным войскам в небольшом радиусе.|r"
        }
    },
    # 12. A0A7 Ба-бах! (1 level, B)
    {
        "id": "A0A7",
        "name": "|cffe4cfa3Ба-бах!|r",
        "hotkey": "B",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Ба-бах!|r",
            "tip1": "|cffe4cfa3Ба-бах!|r (|cffffffffB|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подрывает машину, жертвуя ею ради нанесения |cffffffff50|cffced4da ед. взрывного урона окружающим противникам.|r"
        }
    },
    # 13. A0A5 Расход топлива (6 levels, passive)
    {
        "id": "A0A5",
        "name": "|cffe4cfa3Расход топлива|r",
        "hotkey": None,
        "levels": 6,
        "values": {
            "name": "|cffe4cfa3Расход топлива|r",
            "tip1": "|cffe4cfa3Расход топлива|r [|cffffffffСтепень 5/5|r]",
            "tip2": "|cffe4cfa3Расход топлива|r [|cffffffffСтепень 4/5|r]",
            "tip3": "|cffe4cfa3Расход топлива|r [|cffffffffСтепень 3/5|r]",
            "tip4": "|cffe4cfa3Расход топлива|r [|cffffffffСтепень 2/5|r]",
            "tip5": "|cffe4cfa3Расход топлива|r [|cffffffffСтепень 1/5|r]",
            "tip6": "|cffe4cfa3Расход топлива|r [|cffffffffСтепень 0/5|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Неисправный двигатель расходует на |cffffffff50%|cffced4da больше топлива и смазочных материалов.|r",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Неисправный двигатель расходует на |cffffffff40%|cffced4da больше топлива и смазочных материалов.|r",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Неисправный двигатель расходует на |cffffffff30%|cffced4da больше топлива и смазочных материалов.|r",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Неисправный двигатель расходует на |cffffffff20%|cffced4da больше топлива и смазочных материалов.|r",
            "ubertip5": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Двигатель расходует на |cffffffff10%|cffced4da больше топлива от проектной нормы.|r",
            "ubertip6": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Двигатель отрегулирован по стандартам. Расход топлива оптимален, перерасход отсутствует.|r"
        }
    },
    # 14. A0BL Ускорение (1 level, Q)
    {
        "id": "A0BL",
        "name": "|cffe4cfa3Ускорение|r",
        "hotkey": "Q",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Ускорение|r",
            "tip1": "|cffe4cfa3Ускорение|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Разгоняет ходовую часть на |cffffffff13|cffced4da сек., увеличивая скорость передвижения на |cffffffff40%|cffced4da, но повышая получаемый машиной урон на |cffffffff25%|cffced4da.|r"
        }
    },
    # 15. A0A9 Шанс самоподрыва (6 levels, passive)
    {
        "id": "A0A9",
        "name": "|cffe4cfa3Шанс самоподрыва|r",
        "hotkey": None,
        "levels": 6,
        "values": {
            "name": "|cffe4cfa3Шанс самоподрыва|r",
            "tip1": "|cffe4cfa3Шанс самоподрыва|r [|cffffffffСтепень 5/5|r]",
            "tip2": "|cffe4cfa3Шанс самоподрыва|r [|cffffffffСтепень 4/5|r]",
            "tip3": "|cffe4cfa3Шанс самоподрыва|r [|cffffffffСтепень 3/5|r]",
            "tip4": "|cffe4cfa3Шанс самоподрыва|r [|cffffffffСтепень 2/5|r]",
            "tip5": "|cffe4cfa3Шанс самоподрыва|r [|cffffffffСтепень 1/5|r]",
            "tip6": "|cffe4cfa3Шанс самоподрыва|r [|cffffffffСтепень 0/5|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высокая вероятность детонации боеприпасов в стволе или пусковой установке при выстреле, наносящая урон самому орудию.|r",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заметная вероятность детонации боеприпасов в стволе или пусковой установке при выстреле, наносящая урон самому орудию.|r",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Умеренная вероятность детонации боеприпасов в пусковой установке при выстреле.|r",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Небольшая вероятность детонации боеприпасов в пусковой установке при выстреле.|r",
            "ubertip5": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Минимальная вероятность детонации боеприпасов при выстреле.|r",
            "ubertip6": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Орудийные системы полностью исправны. Риск детонации боеприпасов отсутствует.|r"
        }
    },
    # 16. A1MT Форсаж (1 level, E)
    {
        "id": "A1MT",
        "name": "|cffe4cfa3Форсаж|r",
        "hotkey": "E",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Форсаж|r",
            "tip1": "|cffe4cfa3Форсаж|r (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Перегружает корабельные котлы на |cffffffff25|cffced4da сек., увеличивая скорость передвижения на |cffffffff40%|cffced4da, но повышая получаемый судном урон на |cffffffff25%|cffced4da.|r"
        }
    },
    # 17. A0LG Опуститься в воду (1 level, D)
    {
        "id": "A0LG",
        "name": "|cffe4cfa3Опуститься в воду|r",
        "hotkey": "D",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Опуститься в воду|r",
            "tip1": "|cffe4cfa3Опуститься в воду|r (|cffffffffD|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Погружает судно под воду. Подлодка становится невидимой для обычного обзора, но теряет способность атаковать.|r"
        }
    },
    # 18. A0LF Почти в воде (1 level, passive)
    {
        "id": "A0LF",
        "name": "|cffe4cfa3Почти в воде|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Почти в воде|r",
            "tip1": "|cffe4cfa3Почти в воде|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Низкая посадка корпуса даёт |cffffffff25%|cffced4da шанс уклониться от вражеской физической атаки ценой сниженного радиуса обзора.|r"
        }
    },
    # 19. A0A4 Закрепиться (1 level, Q)
    {
        "id": "A0A4",
        "name": "|cffe4cfa3Закрепиться|r",
        "hotkey": "Q",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Закрепиться|r",
            "tip1": "|cffe4cfa3Закрепиться|r (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выдвигает опорные лапы и фиксирует орудие в осадном положении для ведения огня на дальнюю дистанцию.|r"
        }
    },
    # 20. A0D3 Закопать мину (1 level, W)
    {
        "id": "A0D3",
        "name": "|cffe4cfa3Закопать мину|r",
        "hotkey": "W",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Закопать мину|r",
            "tip1": "|cffe4cfa3Закопать мину|r (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Закапывает в указанной точке взрывную мину на |cffffffff1800|cffced4da сек., которая взрывается при приближении врагов.|r"
        }
    },
    # 21. A0D4 Купить мину (1 level, W)
    {
        "id": "A0D4",
        "name": "|cffe4cfa3Купить мину|r",
        "hotkey": "W",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Купить мину|r",
            "tip1": "|cffe4cfa3Купить мину|r (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приобретает фугасную мину для последующей установки на поле боя.|r"
        }
    },
    # 22. Asds Ба-бах! (1 level, B)
    {
        "id": "Asds",
        "name": "|cffe4cfa3Ба-бах!|r",
        "hotkey": "B",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Ба-бах!|r",
            "tip1": "|cffe4cfa3Ба-бах!|r (|cffffffffB|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подрывает запас взрывчатки, нанося |cffffffff150|cffced4da ед. урона окружающим противникам (|cffffffff300|cffced4da ед. по зданиям и деревьям). Сапёр погибает.|r"
        }
    },
    # 23. A0AH Сильный удар (1 level, passive)
    {
        "id": "A0AH",
        "name": "|cffe4cfa3Сильный удар|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Сильный удар|r",
            "tip1": "|cffe4cfa3Сильный удар|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff8%|cffced4da сокрушительный удар наносит на |cffffffff6|cffced4da ед. больше урона и оглушает цель на |cffffffff1|cffced4da сек.|r"
        }
    },
    # 24. A0BK Обнаружение (1 level, R)
    {
        "id": "A0BK",
        "name": "|cffe4cfa3Обнаружение|r",
        "hotkey": "R",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Обнаружение|r",
            "tip1": "|cffe4cfa3Обнаружение|r (|cffffffffR|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Открывает обзор в указанной области радиусом |cffffffff600|cffced4da на |cffffffff25|cffced4da сек., обнаруживая невидимые войска противника.|r"
        }
    },
    # 25. A0AS Увеличить уровень коррупции (1 level, E)
    {
        "id": "A0AS",
        "name": "|cffe4cfa3Увеличить уровень коррупции|r",
        "hotkey": "E",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Увеличить уровень коррупции|r",
            "tip1": "|cffe4cfa3Увеличить уровень коррупции|r (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает уровень коррупции в картеле на |cffffffff1|cffced4da ступень. Снижает затраты золота на армию, но ухудшает дисциплину и качество техники.|r"
        }
    },
    # 26. A0AT Уменьшить уровень коррупции (1 level, R)
    {
        "id": "A0AT",
        "name": "|cffe4cfa3Уменьшить уровень коррупции|r",
        "hotkey": "R",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Уменьшить уровень коррупции|r",
            "tip1": "|cffe4cfa3Уменьшить уровень коррупции|r (|cffffffffR|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает уровень коррупции в картеле на |cffffffff1|cffced4da ступень. Улучшает качество боевой техники и дисциплину, но повышает расходы на содержание.|r"
        }
    },
    # 27. A0AU Боеготовность (6 levels, passive)
    {
        "id": "A0AU",
        "name": "|cffe4cfa3Боеготовность|r",
        "hotkey": None,
        "levels": 6,
        "values": {
            "name": "|cffe4cfa3Боеготовность|r",
            "tip1": "|cffe4cfa3Боеготовность|r [|cffffffffСтепень 5/5|r]",
            "tip2": "|cffe4cfa3Боеготовность|r [|cffffffffСтепень 4/5|r]",
            "tip3": "|cffe4cfa3Боеготовность|r [|cffffffffСтепень 3/5|r]",
            "tip4": "|cffe4cfa3Боеготовность|r [|cffffffffСтепень 2/5|r]",
            "tip5": "|cffe4cfa3Боеготовность|r [|cffffffffСтепень 1/5|r]",
            "tip6": "|cffe4cfa3Боеготовность|r [|cffffffffСтепень 0/5|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Критический уровень дефектов. При выстреле существует высокая вероятность повреждения орудийных систем самой техники.|r",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высокий уровень дефектов. При выстреле существует ощутимый риск повреждения механизмов боевой единицы.|r",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Умеренный уровень дефектов узлов и агрегатов при ведении огня.|r",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Незначительный уровень дефектов узлов и агрегатов при ведении огня.|r",
            "ubertip5": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Минимальный уровень производственных дефектов.|r",
            "ubertip6": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Боевая единица полностью боеготова. Производственные дефекты отсутствуют.|r"
        }
    },
    # 28. A0KS Требования технологий: Пехота (1 level, passive)
    {
        "id": "A0KS",
        "name": "|cffe4cfa3Требования технологий: Пехота|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Требования технологий: Пехота|r",
            "tip1": "|cffe4cfa3Требования технологий: Пехота|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Необходимые исследования для найма пехоты:|n- |cffa9c7deПулемётчик|r: пули ур. |cffffffff2|cffced4da, лёгкая броня ур. |cffffffff2|cffced4da.|n- |cffa9c7deОгнемётчик|r: огнемёты ур. |cffffffff2|cffced4da, лёгкая броня ур. |cffffffff2|cffced4da.|n- |cffa9c7deРакетчик|r: ракеты ур. |cffffffff2|cffced4da, лёгкая броня ур. |cffffffff2|cffced4da.|n- |cffa9c7deСнайпер|r: пули ур. |cffffffff3|cffced4da, приборы наведения ур. |cffffffff2|cffced4da, лёгкая броня ур. |cffffffff2|cffced4da.|n- |cffa9c7deСапёр|r: ракеты ур. |cffffffff3|cffced4da, лёгкая броня ур. |cffffffff2|cffced4da.|n- |cffa9c7deМедик|r: биологические эксперименты ур. |cffffffff2|cffced4da, лёгкая броня ур. |cffffffff2|cffced4da.|r"
        }
    },
    # 29. A0LD Требования технологий: Техника (1 level, passive)
    {
        "id": "A0LD",
        "name": "|cffe4cfa3Требования технологий: Техника|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Требования технологий: Техника|r",
            "tip1": "|cffe4cfa3Требования технологий: Техника|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Необходимые исследования для сборки техники:|n- |cffa9c7deБРДМ-2000|r: ракеты ур. |cffffffff2|cffced4da, тяжёлая обшивка ур. |cffffffff1|cffced4da, моторы ур. |cffffffff1|cffced4da.|n- |cffa9c7deВездеход «Мурлок-3000»|r: пули ур. |cffffffff2|cffced4da, тяжёлая обшивка ур. |cffffffff1|cffced4da, моторы ур. |cffffffff1|cffced4da.|n- |cffa9c7deШтурмовой танк «Вепрь-5000»|r: ракеты ур. |cffffffff2|cffced4da, тяжёлая обшивка ур. |cffffffff2|cffced4da, моторы ур. |cffffffff2|cffced4da.|n- |cffa9c7deОгнестрельный танк «Напалм-4000»|r: огнемёты ур. |cffffffff2|cffced4da, тяжёлая обшивка ур. |cffffffff2|cffced4da, моторы ур. |cffffffff2|cffced4da.|n- |cffa9c7deМобильная артиллерия|r: ракеты ур. |cffffffff2|cffced4da, приборы наведения ур. |cffffffff2|cffced4da, тяжёлая обшивка ур. |cffffffff1|cffced4da, моторы ур. |cffffffff1|cffced4da.|r"
        }
    },
    # 30. A0LE Требования технологий: Меха (1 level, passive)
    {
        "id": "A0LE",
        "name": "|cffe4cfa3Требования технологий: Меха|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Требования технологий: Меха|r",
            "tip1": "|cffe4cfa3Требования технологий: Меха|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Необходимые исследования для создания мехов и супербойцов:|n- |cffa9c7deМеха «Линчеватель-6000»|r: ударные механизмы ур. |cffffffff2|cffced4da, подвижные механизмы ур. |cffffffff1|cffced4da, тяжёлая обшивка ур. |cffffffff1|cffced4da.|n- |cffa9c7deОгнемеха «Пожар-7000»|r: огнемёты ур. |cffffffff2|cffced4da, подвижные механизмы ур. |cffffffff1|cffced4da, тяжёлая обшивка ур. |cffffffff2|cffced4da.|n- |cffa9c7deОператор силовой брони|r: ударные механизмы ур. |cffffffff1|cffced4da, подвижные механизмы ур. |cffffffff1|cffced4da, тяжёлая обшивка ур. |cffffffff1|cffced4da.|n- |cffa9c7deСупербоец|r: биологические эксперименты ур. |cffffffff2|cffced4da, подвижные механизмы ур. |cffffffff1|cffced4da, тяжёлая обшивка ур. |cffffffff1|cffced4da, пули ур. |cffffffff2|cffced4da.|r"
        }
    },
    # 31. A0LH Требования технологий: Флот (1 level, passive)
    {
        "id": "A0LH",
        "name": "|cffe4cfa3Требования технологий: Флот|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Требования технологий: Флот|r",
            "tip1": "|cffe4cfa3Требования технологий: Флот|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Необходимые исследования для постройки флота:|n- |cffa9c7deВездеход-амфибия|r: пули ур. |cffffffff3|cffced4da, тяжёлая обшивка ур. |cffffffff2|cffced4da, моторы ур. |cffffffff2|cffced4da.|n- |cffa9c7deСубмарина|r: ракеты ур. |cffffffff1|cffced4da, тяжёлая обшивка ур. |cffffffff1|cffced4da, моторы ур. |cffffffff1|cffced4da.|n- |cffa9c7deПодводная лодка|r: ракеты ур. |cffffffff2|cffced4da, тяжёлая обшивка ур. |cffffffff2|cffced4da, моторы ур. |cffffffff2|cffced4da.|r"
        }
    },
    # 32. S001 Посадить в БРДМ (1 level, W)
    {
        "id": "S001",
        "name": "|cffe4cfa3Посадить в БРДМ|r",
        "hotkey": "W",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Посадить в БРДМ|r",
            "tip1": "|cffe4cfa3Посадить в БРДМ|r (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Размещает союзную пехоту в десантном отделении бронемашины.|r"
        }
    },
    # 33. A15N Зона ремонта (1 level, passive)
    {
        "id": "A15N",
        "name": "|cffe4cfa3Зона ремонта|r",
        "hotkey": None,
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Зона ремонта|r",
            "tip1": "|cffe4cfa3Зона ремонта|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Непрерывно ремонтирует повреждённые корабли и механизмы поблизости, восстанавливая по |cffffffff2.5|cffced4da ед. здоровья в секунду в радиусе |cffffffff550|cffced4da.|r"
        }
    },
    # 34. A0UU Взрыв напоследок (1 level, B)
    {
        "id": "A0UU",
        "name": "|cffe4cfa3Взрыв напоследок|r",
        "hotkey": "B",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Взрыв напоследок|r",
            "tip1": "|cffe4cfa3Взрыв напоследок|r (|cffffffffB|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff10|cffced4da ед. взрывного урона окружающим противникам при гибели боевой единицы.|r"
        }
    }
]

# Definitions of all 9 Goblin buffs
BUFFS = [
    # 1. B028 Бракованный патрон
    {
        "id": "B028",
        "name": "|cffe4cfa3Бракованный патрон|r",
        "values": {
            "bufftip": "|cffe4cfa3Бракованный патрон|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Очередной выстрел дал осечку и не нанёс урона цели.|r"
        }
    },
    # 2. B02H Коррупция: Дефект брони
    {
        "id": "B02H",
        "name": "|cffe4cfa3Коррупция: Дефект брони|r",
        "values": {
            "bufftip": "|cffe4cfa3Коррупция: Дефект брони|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Показатель брони этой боевой единицы снижен из-за производственного брака и коррупционных схем.|r"
        }
    },
    # 3. B02I Коррупция: Дисциплина
    {
        "id": "B02I",
        "name": "|cffe4cfa3Коррупция: Дисциплина|r",
        "values": {
            "bufftip": "|cffe4cfa3Коррупция: Дисциплина|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость боя и передвижения этой единицы снижены из-за нехватки снабжения и низкой дисциплины.|r"
        }
    },
    # 4. B087 Форсаж
    {
        "id": "B087",
        "name": "|cffe4cfa3Форсаж|r",
        "values": {
            "bufftip": "|cffe4cfa3Форсаж|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения увеличена за счёт перегрузки двигателя, но получаемый урон повышен.|r"
        }
    },
    # 5. B02A Лечение
    {
        "id": "B02A",
        "name": "|cffe4cfa3Лечение|r",
        "values": {
            "bufftip": "|cffe4cfa3Лечение|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Быстрое восстановление запаса здоровья под наблюдением медика.|r"
        }
    },
    # 6. B02J Поджог
    {
        "id": "B02J",
        "name": "|cffe4cfa3Поджог|r",
        "values": {
            "bufftip": "|cffe4cfa3Поджог|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Эта боевая единица охвачена пламенем и получает периодический урон огнём.|r"
        }
    },
    # 7. B02V Адреналин
    {
        "id": "B02V",
        "name": "|cffe4cfa3Адреналин|r",
        "values": {
            "bufftip": "|cffe4cfa3Адреналин|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Под действием боевой инъекции скорость атаки и скорость передвижения повышены.|r"
        }
    },
    # 8. B02W Коктейль Молотова (исправлена опечатка «Колотов»)
    {
        "id": "B02W",
        "name": "|cffe4cfa3Коктейль Молотова|r",
        "values": {
            "bufftip": "|cffe4cfa3Коктейль Молотова|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Область объята горючей смесью, наносящей периодический урон всем оказавшимся в огне бойцам.|r"
        }
    },
    # 9. B089 Контузия
    {
        "id": "B089",
        "name": "|cffe4cfa3Контузия|r",
        "values": {
            "bufftip": "|cffe4cfa3Контузия|r",
            "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения этой боевой единицы снижена в результате мощного оглушающего удара.|r"
        }
    }
]

def main():
    folder = ROOT / "docs" / "ui_text"
    source = ROOT / "map.w3x"
    wts_file = source / "war3map.wts"
    w3a_skin_file = source / "war3mapSkin.w3a"
    w3h_skin_file = source / "war3mapSkin.w3h"

    # Backup original hashes
    original_wts_hash = hashlib.sha256(wts_file.read_bytes()).hexdigest()
    original_w3a_skin_hash = hashlib.sha256(w3a_skin_file.read_bytes()).hexdigest()
    original_w3h_skin_hash = hashlib.sha256(w3h_skin_file.read_bytes()).hexdigest()

    # Track base binary files to ensure they remain untouched
    base_binaries = [
        "war3map.w3u", "war3map.w3t", "war3map.w3a", "war3map.w3b",
        "war3map.w3d", "war3map.w3q", "war3map.w3h"
    ]
    other_binary_hashes = {
        name: hashlib.sha256((source / name).read_bytes()).hexdigest()
        for name in base_binaries
        if (source / name).exists()
    }

    # Load fields mapping from generate_abils_fields_map.py
    fields_map_file = folder / "goblins_unit_abils_fields_map.json"
    if not fields_map_file.exists():
        print("Fields map not found, run scripts/generate_abils_fields_map.py first.")
        sys.exit(1)
    fields_map = json.loads(fields_map_file.read_text(encoding="utf-8"))

    wts_content = wts_file.read_text(encoding="utf-8")
    wts_changed = {}
    skin_w3a_ops = []
    skin_w3h_ops = []

    # Process all 34 abilities
    for a in UNIT_ABILITIES:
        aid = a["id"]
        finfo = fields_map.get(aid, {}).get("fields", {})
        for field, target_val in a["values"].items():
            info = finfo.get(field, {})
            wts_id = info.get("wts_id")
            is_shared = info.get("is_shared", True)

            # If unique WTS string, update directly in war3map.wts
            if wts_id is not None and not is_shared:
                wts_content = update_wts_string(wts_content, wts_id, target_val)
                wts_changed[wts_id] = target_val
            else:
                # Shared WTS or inline field -> patch into war3mapSkin.w3a
                skin_w3a_ops.append({
                    "id": aid,
                    "field": field,
                    "value": target_val
                })

    # Process all 9 buffs
    for b in BUFFS:
        bid = b["id"]
        finfo = fields_map.get(bid, {}).get("fields", {})
        for field, target_val in b["values"].items():
            info = finfo.get(field, {})
            wts_id = info.get("wts_id")
            is_shared = info.get("is_shared", True)

            if wts_id is not None and not is_shared:
                wts_content = update_wts_string(wts_content, wts_id, target_val)
                wts_changed[wts_id] = target_val
            else:
                # Shared or inline -> patch into war3mapSkin.w3h
                skin_w3h_ops.append({
                    "id": bid,
                    "field": field,
                    "value": target_val
                })

    print(f"Total WTS strings to update: {len(wts_changed)}")
    print(f"Total war3mapSkin.w3a ops: {len(skin_w3a_ops)}")
    print(f"Total war3mapSkin.w3h ops: {len(skin_w3h_ops)}")

    # Write updated WTS
    wts_file.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_file.read_bytes()).hexdigest()
    print(f"WTS updated: {original_wts_hash[:8]} -> {new_wts_hash[:8]}")

    # Patch war3mapSkin.w3a
    if skin_w3a_ops:
        patched_w3a, changed_w3a = patch_blob(
            w3a_skin_file.read_bytes(), skin_w3a_ops, "ability", add_missing=True
        )
        w3a_skin_file.write_bytes(patched_w3a)
        new_w3a_skin_hash = hashlib.sha256(patched_w3a).hexdigest()
        print(f"war3mapSkin.w3a updated with {len(changed_w3a)} mods: {original_w3a_skin_hash[:8]} -> {new_w3a_skin_hash[:8]}")
    else:
        new_w3a_skin_hash = original_w3a_skin_hash

    # Patch war3mapSkin.w3h
    if skin_w3h_ops:
        patched_w3h, changed_w3h = patch_blob(
            w3h_skin_file.read_bytes(), skin_w3h_ops, "buff", add_missing=True
        )
        w3h_skin_file.write_bytes(patched_w3h)
        new_w3h_skin_hash = hashlib.sha256(patched_w3h).hexdigest()
        print(f"war3mapSkin.w3h updated with {len(changed_w3h)} mods: {original_w3h_skin_hash[:8]} -> {new_w3h_skin_hash[:8]}")
    else:
        new_w3h_skin_hash = original_w3h_skin_hash

    # Readback checks in SD mode ONLY (User instruction: SD only, no HD)
    abil_ids = [a["id"] for a in UNIT_ABILITIES]
    buff_ids = [b["id"] for b in BUFFS]

    bulk_a = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(abil_ids)]))
    bulk_b = require(cli(["get-objects-bulk", "--type", "buff", "--ids", ",".join(buff_ids)]))

    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    objects_a = {obj["id"]: obj["fields"] for obj in bulk_a.get("objects", [])}
    objects_b = {obj["id"]: obj["fields"] for obj in bulk_b.get("objects", [])}

    checks = []
    mismatches = []

    for a in UNIT_ABILITIES:
        aid = a["id"]
        fields = objects_a.get(aid, {})
        for f, expected in a["values"].items():
            actual = resolve(fields.get(f, ""))
            matched = (actual == expected)
            checks.append({
                "id": aid,
                "type": "ability",
                "field": f,
                "matched": matched,
                "expected": expected,
                "actual": actual
            })
            if not matched:
                mismatches.append((aid, f, expected, actual))

    for b in BUFFS:
        bid = b["id"]
        fields = objects_b.get(bid, {})
        for f, expected in b["values"].items():
            actual = resolve(fields.get(f, ""))
            matched = (actual == expected)
            checks.append({
                "id": bid,
                "type": "buff",
                "field": f,
                "matched": matched,
                "expected": expected,
                "actual": actual
            })
            if not matched:
                mismatches.append((bid, f, expected, actual))

    print(f"\nSD readback validation: {len(checks) - len(mismatches)}/{len(checks)} fields matched.")
    if mismatches:
        print(f"FAILED: {len(mismatches)} mismatches:")
        for aid, f, exp, act in mismatches:
            print(f"  [{aid}] {f}:\n    Expected: {repr(exp)}\n    Actual:   {repr(act)}")
        sys.exit(1)

    # Save application report and registry
    apply_report = {
        "race": "goblins",
        "category": "unit_abilities_and_buffs",
        "total_abilities": len(UNIT_ABILITIES),
        "total_buffs": len(BUFFS),
        "total_checks": len(checks),
        "all_matched": len(mismatches) == 0,
        "wts_keys_updated": len(wts_changed),
        "skin_w3a_ops": len(skin_w3a_ops),
        "skin_w3h_ops": len(skin_w3h_ops),
        "hashes": {
            "wts": {"before": original_wts_hash, "after": new_wts_hash},
            "w3a_skin": {"before": original_w3a_skin_hash, "after": new_w3a_skin_hash},
            "w3h_skin": {"before": original_w3h_skin_hash, "after": new_w3h_skin_hash}
        },
        "base_binaries_untouched": all(
            hashlib.sha256((source / name).read_bytes()).hexdigest() == h
            for name, h in other_binary_hashes.items()
        )
    }

    registry = {
        "race": "goblins",
        "category": "unit_abilities_and_buffs",
        "total_abilities": len(UNIT_ABILITIES),
        "total_buffs": len(BUFFS),
        "abilities": UNIT_ABILITIES,
        "buffs": BUFFS
    }

    (folder / "goblins_unit_abils_apply.json").write_text(
        json.dumps(apply_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (folder / "goblins_unit_abils.json").write_text(
        json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Report saved to docs/ui_text/goblins_unit_abils_apply.json")
    print("Registry saved to docs/ui_text/goblins_unit_abils.json")
    print("All 34 unit abilities and 9 buffs successfully validated in SD mode!")

if __name__ == "__main__":
    main()
