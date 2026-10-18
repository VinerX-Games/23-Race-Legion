# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Dalaran race (Race 16)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. RACE SELECTION: A0HN
    # =========================================================================
    wts_updates[38867] = "|cffe4cfa3Даларан|r"
    wts_updates[38868] = "|cffe4cfa3Даларан|r (|cffffffffS|r)"
    wts_updates[21869] = (
        "|cffa6afb8РАСА:|cffced4da Могущественное магократическое государство Кирин-Тора, объединяющее величайших чародеев Азерота и повелевающее всеми школами магии.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●●|cffa6afb8●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Wrath of the Lich King — Legion»|r|n|n"
        "|cffced4daДаларан — древнее королевство магов, основанное на берегах озера Лордамер и управляемое верховным советом Кирин-Тора. "
        "В эпоху великих войн парящий город стал неприступной твердыней смертных рас, перемещаясь в самое сердце битвы — от ледяных просторов Нордскола до Расколотых островов. "
        "Армия Даларана всецело опирается на магическое искусство: пироманты, криоманты, арканисты и повелители Бездны сокрушают противников разрушительными заклинаниями, "
        "зачарованные стражи защищают ряды магов, а магические накопители обеспечивают войска колоссальным притоком маны и поддержкой могущественных артефактов.|r"
    )

    checks_def.append({"type": "ability", "id": "A0HN", "field": "name", "expected": wts_updates[38867]})
    checks_def.append({"type": "ability", "id": "A0HN", "field": "tip1", "expected": wts_updates[38868]})
    checks_def.append({"type": "ability", "id": "A0HN", "field": "ubertip1", "expected": wts_updates[21869]})

    # Selection markers: R0BW, R0KK
    wts_updates[9238] = "|cffe4cfa3Даларан|r"
    wts_updates[9239] = "|cffe4cfa3Даларан|r"
    wts_updates[20124] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к королевству Даларан.|r"

    wts_updates[16408] = "|cffe4cfa3Альянс или Даларан|r"
    wts_updates[16409] = "|cffe4cfa3Альянс или Даларан|r"
    wts_updates[16416] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Альянсу или Даларану.|r"

    checks_def.append({"type": "upgrade", "id": "R0BW", "field": "name1", "expected": wts_updates[9238]})
    checks_def.append({"type": "upgrade", "id": "R0BW", "field": "tip1", "expected": wts_updates[9239]})
    checks_def.append({"type": "upgrade", "id": "R0BW", "field": "ubertip1", "expected": wts_updates[20124]})

    checks_def.append({"type": "upgrade", "id": "R0KK", "field": "name1", "expected": wts_updates[16408]})
    checks_def.append({"type": "upgrade", "id": "R0KK", "field": "tip1", "expected": wts_updates[16409]})
    checks_def.append({"type": "upgrade", "id": "R0KK", "field": "ubertip1", "expected": wts_updates[16416]})

    # =========================================================================
    # 2. BUILDINGS (14 buildings)
    # =========================================================================
    # h030: Волшебное Пристанище (Q)
    wts_updates[17369] = "|cffe4cfa3Волшебное Пристанище|r"
    wts_updates[17370] = "|cffe4cfa3Волшебное Пристанище|r (|cffffffffQ|r)"
    wts_updates[31635] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Даларана. Обучает конструкторов и служит складом древесины.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deКонструктор|cffced4da: базовый строитель и рабочий.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУвеличение маны|cffced4da: увеличивает запас маны магов ценой здоровья.|n"
        "- |cffa9c7deПродолжительность жизни|cffced4da: увеличивает запас здоровья магов ценой маны.|n"
        "- |cffa9c7deУскоренное произношение заклинаний|cffced4da: повышает скорость атаки магов.|r"
    )
    checks_def.append({"type": "unit", "id": "h030", "field": "name", "expected": wts_updates[17369]})
    checks_def.append({"type": "unit", "id": "h030", "field": "tip", "expected": wts_updates[17370]})
    checks_def.append({"type": "unit", "id": "h030", "field": "ubertip", "expected": wts_updates[31635]})

    # h031: Конденсатор Маны (A)
    wts_updates[17371] = "|cffe4cfa3Конденсатор Маны|r"
    wts_updates[17372] = "|cffe4cfa3Конденсатор Маны|r (|cffffffffA|r)"
    wts_updates[31636] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает войска Даларана запасом пищи и вырабатывает регулярный доход.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+20|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h031", "field": "name", "expected": wts_updates[17371]})
    checks_def.append({"type": "unit", "id": "h031", "field": "tip", "expected": wts_updates[17372]})
    checks_def.append({"type": "unit", "id": "h031", "field": "ubertip", "expected": wts_updates[31636]})

    # h02V: Алтарь Волшебства (S)
    wts_updates[17367] = "|cffe4cfa3Алтарь Волшебства|r"
    wts_updates[17368] = "|cffe4cfa3Алтарь Волшебства|r (|cffffffffS|r)"
    wts_updates[2012] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Позволяет призывать и воскрешать героев Даларана.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deВерховный маг|cffced4da: герой-маг стихии льда.|n"
        "- |cffa9c7deОгненный мастер|cffced4da: герой-маг разрушительного пламени.|n"
        "- |cffa9c7deМастер Тайной магии|cffced4da: герой-чародей тайной магии и телепортации.|r"
    )
    checks_def.append({"type": "unit", "id": "h02V", "field": "name", "expected": wts_updates[17367]})
    checks_def.append({"type": "unit", "id": "h02V", "field": "tip", "expected": wts_updates[17368]})
    checks_def.append({"type": "unit", "id": "h02V", "field": "ubertip", "expected": wts_updates[2012]})

    # h02W: Волшебная Библиотека (D)
    wts_updates[17229] = "|cffe4cfa3Волшебная Библиотека|r"
    wts_updates[17230] = "|cffe4cfa3Волшебная Библиотека|r (|cffffffffD|r)"
    wts_updates[31633] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр высшего магического образования Даларана. Обучает заклинателей четырёх магических школ и исследует улучшения их мастерства.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПиромант|cffced4da: маг огня с заклинанием «Пламя феникса».|n"
        "- |cffa9c7deЧародей Льда|cffced4da: маг льда со способностью «Ледяная тюрьма».|n"
        "- |cffa9c7deАрканист|cffced4da: маг тайной энергии с заклинанием «Сверхновая».|n"
        "- |cffa9c7deМаг Бездны|cffced4da: темный чародей со способностью призыва порождений Бездны.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМагия Огня|cffced4da: открывает новые заклинания пиромантов.|n"
        "- |cffa9c7deМагия Льда|cffced4da: открывает новые заклинания чародеев льда.|n"
        "- |cffa9c7deТайная магия|cffced4da: открывает новые заклинания арканистов.|n"
        "- |cffa9c7deВзгляд в Бездну|cffced4da: открывает новые заклинания магов Бездны.|n"
        "- |cffa9c7deМагический страж|cffced4da: позволяет башням обнаруживать невидимых врагов.|r"
    )
    checks_def.append({"type": "unit", "id": "h02W", "field": "name", "expected": wts_updates[17229]})
    checks_def.append({"type": "unit", "id": "h02W", "field": "tip", "expected": wts_updates[17230]})
    checks_def.append({"type": "unit", "id": "h02W", "field": "ubertip", "expected": wts_updates[31633]})

    # h02X: Волшебная Оружейная (W)
    wts_updates[17231] = "|cffe4cfa3Волшебная Оружейная|r"
    wts_updates[17232] = "|cffe4cfa3Волшебная Оружейная|r (|cffffffffW|r)"
    wts_updates[12957] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает боевых магов, защитников и магические конструкты Даларана.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПехотинец|cffced4da: стойкий мечник ближнего боя.|n"
        "- |cffa9c7deЗачарователь|cffced4da: универсальный маг, способный менять меч на посох.|n"
        "- |cffa9c7deЗаклинатель Света|cffced4da: священнослужитель с целительным тотемом и изгнанием.|n"
        "- |cffa9c7deМагический Эксперимент|cffced4da: свирепый конструкт с критическими ударами.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗащита|cffced4da: снижает урон пехотинцев от стрелковых атак.|n"
        "- |cffa9c7deМагический Щит|cffced4da: позволяет пехотинцам поглощать урон за счёт маны.|n"
        "- |cffa9c7deЗачарованное оружие|cffced4da: повышает скорость боя зачарователей.|n"
        "- |cffa9c7deПознания Света|cffced4da: увеличивает здоровье, ману и регенерацию заклинателей Света.|r"
    )
    checks_def.append({"type": "unit", "id": "h02X", "field": "name", "expected": wts_updates[17231]})
    checks_def.append({"type": "unit", "id": "h02X", "field": "tip", "expected": wts_updates[17232]})
    checks_def.append({"type": "unit", "id": "h02X", "field": "ubertip", "expected": wts_updates[12957]})

    # h02Y: Магическая кузня (E)
    wts_updates[17233] = "|cffe4cfa3Магическая кузня|r"
    wts_updates[17234] = "|cffe4cfa3Магическая кузня|r (|cffffffffE|r)"
    wts_updates[31634] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Улучшает оружие, посохи, мантии и магическую защиту существ Даларана. Служит складом древесины.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deВолшебные Мечи|cffced4da: увеличивает урон пехотинцев и башен.|n"
        "- |cffa9c7deУсиление посоха|cffced4da: увеличивает урон атак магов дальнего боя.|n"
        "- |cffa9c7deНакидки|cffced4da: повышает броню магов и зачарователей.|n"
        "- |cffa9c7deЗащита огня|cffced4da: усиливает броню огненных созданий.|n"
        "- |cffa9c7deЗащита льда|cffced4da: усиливает броню ледяных созданий.|r"
    )
    checks_def.append({"type": "unit", "id": "h02Y", "field": "name", "expected": wts_updates[17233]})
    checks_def.append({"type": "unit", "id": "h02Y", "field": "tip", "expected": wts_updates[17234]})
    checks_def.append({"type": "unit", "id": "h02Y", "field": "ubertip", "expected": wts_updates[31634]})

    # h034: Хранилище Маны (R)
    wts_updates[17240] = "|cffe4cfa3Хранилище Маны|r"
    wts_updates[17241] = "|cffe4cfa3Хранилище Маны|r (|cffffffffR|r)"
    wts_updates[30627] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Магическое сооружение первой ступени. Концентрирует запасы чародейской энергии и обеспечивает армию припасами.|n|n"
        "Даёт |cffffffff10|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deХранилище Маны — уровень 2|cffced4da: расширяет резервуары маны и открывает глобальную ауру восполнения маны.|r"
    )
    checks_def.append({"type": "unit", "id": "h034", "field": "name", "expected": wts_updates[17240]})
    checks_def.append({"type": "unit", "id": "h034", "field": "tip", "expected": wts_updates[17241]})
    checks_def.append({"type": "unit", "id": "h034", "field": "ubertip", "expected": wts_updates[30627]})

    # h035: Хранилище Маны (уровень 2) (T)
    wts_updates[17242] = "|cffe4cfa3Хранилище Маны|r"
    wts_updates[17243] = "|cffe4cfa3Хранилище Маны — уровень 2|r (|cffffffffT|r)"
    wts_updates[30628] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Магическое сооружение второй ступени с расширенными резервуарами энергии.|n|n"
        "Даёт |cffffffff10|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВосстановление маны|cffced4da: ускоряет регенерацию маны всех союзников по всей карте.|n"
        "- |cffa9c7deВосполнить ману|cffced4da: мгновенно восстанавливает запас маны выбранного союзника.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМагический Талисман|cffced4da: повышает скорость регенерации маны всех магов Даларана.|r"
    )
    checks_def.append({"type": "unit", "id": "h035", "field": "name", "expected": wts_updates[17242]})
    checks_def.append({"type": "unit", "id": "h035", "field": "tip", "expected": wts_updates[17243]})
    checks_def.append({"type": "unit", "id": "h035", "field": "ubertip", "expected": wts_updates[30628]})

    # h036: Накопитель Маны (F)
    wts_updates[17244] = "|cffe4cfa3Накопитель Маны|r"
    wts_updates[17245] = "|cffe4cfa3Накопитель Маны|r (|cffffffffF|r)"
    wts_updates[30954] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Монументальный накопитель тайной магии. Аккумулирует колоссальные потоки чародейской силы и открывает высшие магические познания.|n|n"
        "Даёт |cffffffff10|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deГлубокие познания|cffced4da: увеличивает максимальный запас маны всех магов Даларана.|r"
    )
    checks_def.append({"type": "unit", "id": "h036", "field": "name", "expected": wts_updates[17244]})
    checks_def.append({"type": "unit", "id": "h036", "field": "tip", "expected": wts_updates[17245]})
    checks_def.append({"type": "unit", "id": "h036", "field": "ubertip", "expected": wts_updates[30954]})

    # h032: Магическая Башня (Z)
    wts_updates[17238] = "|cffe4cfa3Магическая Башня|r"
    wts_updates[17239] = "|cffe4cfa3Магическая Башня|r (|cffffffffZ|r)"
    wts_updates[12959] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное магическое сооружение. Атаки башни сжигают ману цели и наносят повышенный урон призванным существам.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПротиводействие|cffced4da: сжигает ману цели при каждом попадании и наносит дополнительный урон.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h032", "field": "name", "expected": wts_updates[17238]})
    checks_def.append({"type": "unit", "id": "h032", "field": "tip", "expected": wts_updates[17239]})
    checks_def.append({"type": "unit", "id": "h032", "field": "ubertip", "expected": wts_updates[12959]})

    # h037: Волшебная Темница (T)
    wts_updates[17246] = "|cffe4cfa3Волшебная Темница|r"
    wts_updates[17247] = "|cffe4cfa3Волшебная Темница|r (|cffffffffT|r)"
    wts_updates[31638] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Специализированное хранилище опасных магических сущностей, аномалий и экспериментальных конструктов Даларана.|r"
    )
    checks_def.append({"type": "unit", "id": "h037", "field": "name", "expected": wts_updates[17246]})
    checks_def.append({"type": "unit", "id": "h037", "field": "tip", "expected": wts_updates[17247]})
    checks_def.append({"type": "unit", "id": "h037", "field": "ubertip", "expected": wts_updates[31638]})

    # h038: Хранилище Артефактов (D)
    wts_updates[17248] = "|cffe4cfa3Хранилище Артефактов|r"
    wts_updates[17249] = "|cffe4cfa3Хранилище Артефактов|r (|cffffffffD|r)"
    wts_updates[31639] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Торговая лавка магических предметов. Предлагает могущественные артефакты и чародейские реликвии, созданные магами Даларана.|r"
    )
    checks_def.append({"type": "unit", "id": "h038", "field": "name", "expected": wts_updates[17248]})
    checks_def.append({"type": "unit", "id": "h038", "field": "tip", "expected": wts_updates[17249]})
    checks_def.append({"type": "unit", "id": "h038", "field": "ubertip", "expected": wts_updates[31639]})

    # n063: Телепорт
    wts_updates[31593] = "|cffe4cfa3Телепорт|r"
    checks_def.append({"type": "unit", "id": "n063", "field": "name", "expected": wts_updates[31593]})

    # h011: Верфь (C)
    wts_updates[368] = "|cffe4cfa3Верфь|r"
    wts_updates[369] = "|cffe4cfa3Верфь|r (|cffffffffC|r)"
    wts_updates[370] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Строит боевые корабли и исследует улучшения флота.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТранспорт|cffced4da|n- |cffa9c7deФрегат|cffced4da|n- |cffa9c7deЛинкор|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбстрел|cffced4da|n- |cffa9c7deДополнительные паруса|cffced4da|n"
        "- |cffa9c7deПочинка|cffced4da|n- |cffa9c7deОрудия флота|cffced4da|n- |cffa9c7deУкреплённый корпус|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h011", "field": "name", "expected": wts_updates[368]})
    checks_def.append({"type": "unit", "id": "h011", "field": "tip", "expected": wts_updates[369]})
    checks_def.append({"type": "unit", "id": "h011", "field": "ubertip", "expected": wts_updates[370]})

    # =========================================================================
    # 3. UNITS (14 units)
    # =========================================================================
    # u001: Конструктор (Q)
    wts_updates[17373] = "|cffe4cfa3Конструктор|r"
    wts_updates[17374] = "|cffe4cfa3Конструктор|r (|cffffffffQ|r)"
    wts_updates[1418] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Даларана. Создаёт и ремонтирует здания, а также добывает золото и древесину.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСкачок|cffced4da: мгновенно перемещается на небольшое расстояние.|n"
        "- |cffa9c7deРемонт|cffced4da: восстанавливает прочность зданий и техники.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u001", "field": "name", "expected": wts_updates[17373]})
    checks_def.append({"type": "unit", "id": "u001", "field": "tip", "expected": wts_updates[17374]})
    checks_def.append({"type": "unit", "id": "u001", "field": "ubertip", "expected": wts_updates[1418]})

    # h02I: Пехотинец (Q)
    wts_updates[17347] = "|cffe4cfa3Пехотинец|r"
    wts_updates[17348] = "|cffe4cfa3Пехотинец|r (|cffffffffQ|r)"
    wts_updates[24921] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стойкий воин ближнего боя, прикрывающий передовые позиции магов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗащита|cffced4da: укрывается за щитом, снижая урон от стрелковых атак ценой скорости передвижения.|n"
        "- |cffa9c7deМагический Щит|cffced4da: поглощает входящий урон за счёт запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02I", "field": "name", "expected": wts_updates[17347]})
    checks_def.append({"type": "unit", "id": "h02I", "field": "tip", "expected": wts_updates[17348]})
    checks_def.append({"type": "unit", "id": "h02I", "field": "ubertip", "expected": wts_updates[24921]})

    # h02J: Пиромант (Q)
    wts_updates[17349] = "|cffe4cfa3Пиромант|r"
    wts_updates[17350] = "|cffe4cfa3Пиромант|r (|cffffffffQ|r)"
    wts_updates[31628] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг-заклинатель стихии огня, наносящий высокий урон по площади.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПламя феникса|cffced4da: выпускает огненную волну в указанном направлении.|n"
        "- |cffa9c7deОгненная стрела|cffced4da: поражает и оглушает цель сгустком огня.|n"
        "- |cffa9c7deПоджигание|cffced4da: окружает врага пламенем, нанося урон окружающим войскам.|n"
        "- |cffa9c7deПризыв создания огня|cffced4da: призывает могучего огненного стража.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02J", "field": "name", "expected": wts_updates[17349]})
    checks_def.append({"type": "unit", "id": "h02J", "field": "tip", "expected": wts_updates[17350]})
    checks_def.append({"type": "unit", "id": "h02J", "field": "ubertip", "expected": wts_updates[31628]})

    # h02K: Чародей Льда (W)
    wts_updates[17351] = "|cffe4cfa3Чародей Льда|r"
    wts_updates[17352] = "|cffe4cfa3Чародей Льда|r (|cffffffffW|r)"
    wts_updates[35272] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг-заклинатель стихии льда, специализирующийся на контроле и защите союзников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЛедяная тюрьма|cffced4da: сковывает цель глыбой льда и наносит урон.|n"
        "- |cffa9c7deМорозный доспех|cffced4da: повышает броню союзника и замедляет атакующих его врагов.|n"
        "- |cffa9c7deЛедяные стрелы|cffced4da: наделяет атаки эффектом замедления.|n"
        "- |cffa9c7deПризыв создания льда|cffced4da: призывает ледяного стража с аурой мороза.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02K", "field": "name", "expected": wts_updates[17351]})
    checks_def.append({"type": "unit", "id": "h02K", "field": "tip", "expected": wts_updates[17352]})
    checks_def.append({"type": "unit", "id": "h02K", "field": "ubertip", "expected": wts_updates[35272]})

    # h02L: Заклинатель Света (E)
    wts_updates[17353] = "|cffe4cfa3Заклинатель Света|r"
    wts_updates[17354] = "|cffe4cfa3Заклинатель Света|r (|cffffffffE|r)"
    wts_updates[31630] = (
        "|cffa6afb8ЮНИТ:|cffced4da Жрец священного Света, обеспечивающий исцеление и рассеивание вражеской магии.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМагический тотем|cffced4da: призывает тотем, исцеляющий находящихся рядом союзников.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает чары с указанной области и наносит урон призванным целям.|n"
        "- |cffa9c7deГлубокая вера|cffced4da: пассивно ускоряет восстановление здоровья союзных войск.|n"
        "- |cffa9c7deИзгнание|cffced4da: переносит цель в астрал, лишая возможности атаковать.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02L", "field": "name", "expected": wts_updates[17353]})
    checks_def.append({"type": "unit", "id": "h02L", "field": "tip", "expected": wts_updates[17354]})
    checks_def.append({"type": "unit", "id": "h02L", "field": "ubertip", "expected": wts_updates[31630]})

    # h02M: Арканист (E)
    wts_updates[17359] = "|cffe4cfa3Арканист|r"
    wts_updates[17360] = "|cffe4cfa3Арканист|r (|cffffffffE|r)"
    wts_updates[31631] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг чистой тайной магии, повелевающий пространством и временем.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСверхновая|cffced4da: концентрирует вспышку тайной энергии, поражающую и замедляющую цель.|n"
        "- |cffa9c7deИскажение времени|cffced4da: временно увеличивает скорость союзников вокруг.|n"
        "- |cffa9c7deЗеркальное изображение|cffced4da: создаёт иллюзорную копию арканиста.|n"
        "- |cffa9c7deМассовая телепортация|cffced4da: переносит группу бойцов к союзному зданию.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02M", "field": "name", "expected": wts_updates[17359]})
    checks_def.append({"type": "unit", "id": "h02M", "field": "tip", "expected": wts_updates[17360]})
    checks_def.append({"type": "unit", "id": "h02M", "field": "ubertip", "expected": wts_updates[31631]})

    # h02N: Зачарователь (дальний бой) (S)
    wts_updates[17355] = "|cffe4cfa3Зачарователь|r"
    wts_updates[17356] = "|cffe4cfa3Зачарователь|r (|cffffffffS|r)"
    wts_updates[7175] = (
        "|cffa6afb8ЮНИТ:|cffced4da Универсальный боевой маг в стойке дальнего боя. Атакует посохом, сжигая ману цели, и может перейти в ближний бой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСменить оружие|cffced4da: переключается на меч для ближнего боя.|n"
        "- |cffa9c7deСжигание маны|cffced4da: каждая атака сжигает ману противника.|n"
        "- |cffa9c7deМагический Щит|cffced4da: поглощает урон за счёт маны.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02N", "field": "name", "expected": wts_updates[17355]})
    checks_def.append({"type": "unit", "id": "h02N", "field": "tip", "expected": wts_updates[17356]})
    checks_def.append({"type": "unit", "id": "h02N", "field": "ubertip", "expected": wts_updates[7175]})

    # h02O: Зачарователь (ближний бой) (W)
    wts_updates[17357] = "|cffe4cfa3Зачарователь|r"
    wts_updates[17358] = "|cffe4cfa3Зачарователь|r (|cffffffffW|r)"
    wts_updates[7179] = (
        "|cffa6afb8ЮНИТ:|cffced4da Универсальный боевой маг в стойке ближнего боя. Сражается мечом, сжигая ману цели, и может перейти в дальний бой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСменить оружие|cffced4da: переключается на посох для дальнего боя.|n"
        "- |cffa9c7deСжигание маны|cffced4da: каждая атака сжигает ману противника.|n"
        "- |cffa9c7deМагический Щит|cffced4da: поглощает урон за счёт маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02O", "field": "name", "expected": wts_updates[17357]})
    checks_def.append({"type": "unit", "id": "h02O", "field": "tip", "expected": wts_updates[17358]})
    checks_def.append({"type": "unit", "id": "h02O", "field": "ubertip", "expected": wts_updates[7179]})

    # h02P: Маг Бездны (R)
    wts_updates[17361] = "|cffe4cfa3Маг Бездны|r"
    wts_updates[17362] = "|cffe4cfa3Маг Бездны|r (|cffffffffR|r)"
    wts_updates[31632] = (
        "|cffa6afb8ЮНИТ:|cffced4da Темный чародей, черпающий разрушительную энергию из глубин Бездны.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПризыв создания Бездны|cffced4da: призывает свирепое порождение Бездны.|n"
        "- |cffa9c7deБезумие Бездны|cffced4da: увеличивает урон находящихся рядом союзников.|n"
        "- |cffa9c7deЗабывчивость|cffced4da: лишает врагов в указанной области возможности творить заклинания.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h02P", "field": "name", "expected": wts_updates[17361]})
    checks_def.append({"type": "unit", "id": "h02P", "field": "tip", "expected": wts_updates[17362]})
    checks_def.append({"type": "unit", "id": "h02P", "field": "ubertip", "expected": wts_updates[31632]})

    # n009: Магическое Создание Огня
    wts_updates[17363] = "|cffe4cfa3Магическое Создание Огня|r"
    wts_updates[17364] = "|cffe4cfa3Магическое Создание Огня|r"
    checks_def.append({"type": "unit", "id": "n009", "field": "name", "expected": wts_updates[17363]})
    checks_def.append({"type": "unit", "id": "n009", "field": "tip", "expected": wts_updates[17364]})

    # n00A: Магическое Создание Льда
    wts_updates[17365] = "|cffe4cfa3Магическое Создание Льда|r"
    wts_updates[17366] = "|cffe4cfa3Магическое Создание Льда|r"
    checks_def.append({"type": "unit", "id": "n00A", "field": "name", "expected": wts_updates[17365]})
    checks_def.append({"type": "unit", "id": "n00A", "field": "tip", "expected": wts_updates[17366]})

    # n00B: Магический Эксперимент (R)
    wts_updates[937] = "|cffe4cfa3Магический Эксперимент|r"
    wts_updates[15186] = "|cffe4cfa3Магический Эксперимент|r (|cffffffffR|r)"
    wts_updates[899] = (
        "|cffa6afb8ЮНИТ:|cffced4da Свирепый летучий конструкт магов Даларана, созданный для нанесения сокрушительного урона.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКритический удар|cffced4da: даёт шанс нанести многократный урон при атаке.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n00B", "field": "name", "expected": wts_updates[937]})
    checks_def.append({"type": "unit", "id": "n00B", "field": "tip", "expected": wts_updates[15186]})
    checks_def.append({"type": "unit", "id": "n00B", "field": "ubertip", "expected": wts_updates[899]})

    # n00M: Усиленное Магическое Создание Огня
    wts_updates[17398] = "|cffe4cfa3Усиленное Магическое Создание Огня|r"
    wts_updates[17399] = "|cffe4cfa3Усиленное Магическое Создание Огня|r"
    checks_def.append({"type": "unit", "id": "n00M", "field": "name", "expected": wts_updates[17398]})
    checks_def.append({"type": "unit", "id": "n00M", "field": "tip", "expected": wts_updates[17399]})

    # n00N: Усиленное Магическое Создание Льда
    wts_updates[17400] = "|cffe4cfa3Усиленное Магическое Создание Льда|r"
    wts_updates[17401] = "|cffe4cfa3Усиленное Магическое Создание Льда|r"
    checks_def.append({"type": "unit", "id": "n00N", "field": "name", "expected": wts_updates[17400]})
    checks_def.append({"type": "unit", "id": "n00N", "field": "tip", "expected": wts_updates[17401]})

    # =========================================================================
    # 4. HEROES (5 heroes)
    # =========================================================================
    # H04S: Верховный маг (E)
    wts_updates[2527] = "|cffe4cfa3Верховный маг|r"
    wts_updates[19603] = "|cffe4cfa3Верховный маг|r (|cffffffffE|r)"
    wts_updates[2620] = "Нилас Чаротворец"
    wts_updates[31650] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Мудрый архимаг Кирин-Тора, подчинивший стихию абсолютного холода.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКольцо льда|cffced4da: поражает врагов ледяной волной, нанося урон и замедляя их.|n"
        "- |cffa9c7deПризыв элементаля воды|cffced4da: призывает подконтрольного элементаля воды.|n"
        "- |cffa9c7deАура мороза|cffced4da: замедляет скорость перемещения и атаки находящихся рядом врагов.|n"
        "- |cffa9c7deЛедяные оковы|cffced4da: сковывает льдом и оглушает наземных врагов в области действия.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H04S", "field": "name", "expected": wts_updates[2527]})
    checks_def.append({"type": "unit", "id": "H04S", "field": "tip", "expected": wts_updates[19603]})
    checks_def.append({"type": "unit", "id": "H04S", "field": "propernames", "expected": wts_updates[2620]})
    checks_def.append({"type": "unit", "id": "H04S", "field": "ubertip", "expected": wts_updates[31650]})

    # H04W: Огненный мастер (W)
    wts_updates[2528] = "|cffe4cfa3Огненный мастер|r"
    wts_updates[2530] = "|cffe4cfa3Огненный мастер|r (|cffffffffW|r)"
    wts_updates[15137] = "Тенн Огнетворец"
    wts_updates[31651] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могучий пиромант, испепеляющий врагов разрушительными заклинаниями пламени.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненный ливень|cffced4da: обрушивает на указанную область волны всепоглощающего огня.|n"
        "- |cffa9c7deОгненная стрела|cffced4da: поражает цель сгустком огня, нанося урон и оглушая её.|n"
        "- |cffa9c7deАура пламени|cffced4da: окружает союзников щитом, отражающим урон ближнего боя во врагов.|n"
        "- |cffa9c7deАпокалипсис|cffced4da: обрушивает метеоритный дождь и призывает огненных чудовищ.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H04W", "field": "name", "expected": wts_updates[2528]})
    checks_def.append({"type": "unit", "id": "H04W", "field": "tip", "expected": wts_updates[2530]})
    checks_def.append({"type": "unit", "id": "H04W", "field": "propernames", "expected": wts_updates[15137]})
    checks_def.append({"type": "unit", "id": "H04W", "field": "ubertip", "expected": wts_updates[31651]})

    # H04X: Мастер Тайной магии (Q)
    wts_updates[2616] = "|cffe4cfa3Мастер Тайной магии|r"
    wts_updates[2618] = "|cffe4cfa3Мастер Тайной магии|r (|cffffffffQ|r)"
    wts_updates[15139] = "Нилас Чаротворец"
    wts_updates[3334] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Искусная волшебница, виртуозно манипулирующая тайной энергией и пространством.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПохищение маны|cffced4da: вытягивает ману из врага или передает её союзнику.|n"
        "- |cffa9c7deСила магии|cffced4da: наделяет обычные атаки героини дополнительным уроном от тайной магии.|n"
        "- |cffa9c7deАура гениальности|cffced4da: значительно ускоряет восполнение маны окружающих союзников.|n"
        "- |cffa9c7deМассовая телепортация|cffced4da: мгновенно переносит героиню и её армию к союзному бойцу или зданию.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H04X", "field": "name", "expected": wts_updates[2616]})
    checks_def.append({"type": "unit", "id": "H04X", "field": "tip", "expected": wts_updates[2618]})
    checks_def.append({"type": "unit", "id": "H04X", "field": "propernames", "expected": wts_updates[15139]})
    checks_def.append({"type": "unit", "id": "H04X", "field": "ubertip", "expected": wts_updates[3334]})

    # H052: Глава Кирин-Тора (X)
    wts_updates[3231] = "|cffe4cfa3Глава Кирин-Тора|r"
    wts_updates[3233] = "|cffe4cfa3Глава Кирин-Тора|r (|cffffffffX|r)"
    wts_updates[3235] = "|cffe4cfa3Ронин|r"
    wts_updates[31655] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный верховный лидер Кирин-Тора. Обладает непревзойдённой мощью и повелевает древними артефактами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВзрыв маны|cffced4da: обстреливает область сгустками маны, оглушая наземных врагов.|n"
        "- |cffa9c7deЛедяное Наказание|cffced4da: окружает героя аурой льда, наносящей урон окружающим наземным врагам.|n"
        "- |cffa9c7deЗащита магии|cffced4da: поглощает значительную часть входящего урона от атак.|n"
        "- |cffa9c7deПризыв Магических Артефактов|cffced4da: призывает реликвии, атакующие врагов и исцеляющие союзников.|n"
        "- |cffa9c7deТемный призыв|cffced4da: переносит группу союзников к герою.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H052", "field": "name", "expected": wts_updates[3231]})
    checks_def.append({"type": "unit", "id": "H052", "field": "tip", "expected": wts_updates[3233]})
    checks_def.append({"type": "unit", "id": "H052", "field": "propernames", "expected": wts_updates[3235]})
    checks_def.append({"type": "unit", "id": "H052", "field": "ubertip", "expected": wts_updates[31655]})

    # H053: Хранитель (X)
    wts_updates[3318] = "|cffe4cfa3Хранитель|r"
    wts_updates[3320] = "|cffe4cfa3Хранитель|r (|cffffffffX|r)"
    wts_updates[3322] = "|cffe4cfa3Кадгар|r"
    wts_updates[20031] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный Хранитель Азерота. Мастерски сочетает целительную силу льда и испепеляющий огонь.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗаморозка ран|cffced4da: выпускает ледяную волну, исцеляющую союзников по области.|n"
        "- |cffa9c7deВолна смерти|cffced4da: выпускает сокрушительный водяной вал, сметающий врагов на пути.|n"
        "- |cffa9c7deСожжение|cffced4da: окружает героя огненной бурей, непрерывно сжигающей наземных врагов.|n"
        "- |cffa9c7deЛедяные оковы|cffced4da: сковывает льдом и оглушает наземных врагов в области действия.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H053", "field": "name", "expected": wts_updates[3318]})
    checks_def.append({"type": "unit", "id": "H053", "field": "tip", "expected": wts_updates[3320]})
    checks_def.append({"type": "unit", "id": "H053", "field": "propernames", "expected": wts_updates[3322]})
    checks_def.append({"type": "unit", "id": "H053", "field": "ubertip", "expected": wts_updates[20031]})

    # =========================================================================
    # 5. RESEARCHES (UPGRADES)
    # =========================================================================

    # R013: Защита огня (6 levels)
    r013_names = [1651, 1652, 1653, 1648, 1649, 1650]
    r013_tips = [1747, 1748, 1749, 1750, 1751, 1752]
    r013_ubts = [1660, 1661, 1662, 1663, 1665, 1664]
    for i in range(6):
        lvl = i + 1
        wts_updates[r013_names[i]] = "|cffe4cfa3Защита огня|r"
        wts_updates[r013_tips[i]] = f"|cffe4cfa3Защита огня — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r013_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню огненных созданий Даларана на |cffffffff{lvl}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагическое Создание Огня|cffced4da|n"
            "- |cffa9c7deУсиленное Магическое Создание Огня|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R013", "field": f"name{lvl}", "expected": wts_updates[r013_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R013", "field": f"tip{lvl}", "expected": wts_updates[r013_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R013", "field": f"ubertip{lvl}", "expected": wts_updates[r013_ubts[i]]})

    # R014: Защита льда (6 levels)
    r014_names = [1753, 1674, 1675, 1670, 1671, 1672]
    r014_tips = [1754, 1755, 1756, 1757, 1758, 1759]
    r014_ubts = [1682, 1683, 1684, 1685, 1687, 1686]
    for i in range(6):
        lvl = i + 1
        wts_updates[r014_names[i]] = "|cffe4cfa3Защита льда|r"
        wts_updates[r014_tips[i]] = f"|cffe4cfa3Защита льда — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r014_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню ледяных созданий Даларана на |cffffffff{lvl}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагическое Создание Льда|cffced4da|n"
            "- |cffa9c7deУсиленное Магическое Создание Льда|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R014", "field": f"name{lvl}", "expected": wts_updates[r014_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R014", "field": f"tip{lvl}", "expected": wts_updates[r014_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R014", "field": f"ubertip{lvl}", "expected": wts_updates[r014_ubts[i]]})

    # R012: Усиление посоха (6 levels)
    r012_names = [1621, 1622, 1623, 1624, 1625, 1626]
    r012_tips = [1742, 1741, 1743, 1744, 1745, 1746]
    r012_ubts = [1633, 1634, 1635, 1636, 1637, 1638]
    for i in range(6):
        lvl = i + 1
        wts_updates[r012_names[i]] = "|cffe4cfa3Усиление посоха|r"
        wts_updates[r012_tips[i]] = f"|cffe4cfa3Усиление посоха — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[r012_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак посохом всех магов дальнего боя Даларана.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПиромант|cffced4da|n"
            "- |cffa9c7deЧародей Льда|cffced4da|n- |cffa9c7deАрканист|cffced4da|n"
            "- |cffa9c7deЗаклинатель Света|cffced4da|n- |cffa9c7deЗачарователь|cffced4da|n"
            "- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R012", "field": f"name{lvl}", "expected": wts_updates[r012_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R012", "field": f"tip{lvl}", "expected": wts_updates[r012_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R012", "field": f"ubertip{lvl}", "expected": wts_updates[r012_ubts[i]]})

    # R00Q: Волшебные Мечи (6 levels)
    r00q_names = [24566, 24567, 24864, 25423, 25895, 26367]
    r00q_tips = [24865, 24869, 24918, 26485, 26486, 26487]
    r00q_ubts = [25080, 25172, 25188, 26488, 27723, 27724]
    for i in range(6):
        lvl = i + 1
        wts_updates[r00q_names[i]] = "|cffe4cfa3Волшебные Мечи|r"
        wts_updates[r00q_tips[i]] = f"|cffe4cfa3Волшебные Мечи — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r00q_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон в ближнем бою пехотинцев и зачарователей, а также усиливает атаку Магических Башен.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n"
            "- |cffa9c7deЗачарователь|cffced4da|n- |cffa9c7deМагическая Башня|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R00Q", "field": f"name{lvl}", "expected": wts_updates[r00q_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R00Q", "field": f"tip{lvl}", "expected": wts_updates[r00q_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R00Q", "field": f"ubertip{lvl}", "expected": wts_updates[r00q_ubts[i]]})

    # R00T: Накидка (6 levels)
    r00t_names = [1208, 1209, 1210, 1205, 1206, 1207]
    r00t_tips = [1735, 1736, 1737, 1738, 1739, 1740]
    r00t_ubts = [1217, 1218, 1219, 1220, 1222, 1221]
    for i in range(6):
        lvl = i + 1
        wts_updates[r00t_names[i]] = "|cffe4cfa3Магическая накидка|r"
        wts_updates[r00t_tips[i]] = f"|cffe4cfa3Магическая накидка — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r00t_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает броню пехотинцев и всех заклинателей Даларана на |cffffffff{lvl}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n"
            "- |cffa9c7deПиромант|cffced4da|n- |cffa9c7deЧародей Льда|cffced4da|n"
            "- |cffa9c7deАрканист|cffced4da|n- |cffa9c7deЗаклинатель Света|cffced4da|n"
            "- |cffa9c7deЗачарователь|cffced4da|n- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R00T", "field": f"name{lvl}", "expected": wts_updates[r00t_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R00T", "field": f"tip{lvl}", "expected": wts_updates[r00t_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R00T", "field": f"ubertip{lvl}", "expected": wts_updates[r00t_ubts[i]]})

    # R018: Увеличение маны (10 levels)
    r018_names = [1860, 1869, 1870, 1871, 1872, 1911, 1913, 1912, 1914, 1915]
    r018_tips = [1861, 1873, 1874, 1875, 1876, 1916, 1917, 1918, 1919, 1920]
    r018_ubts = [1862, 1877, 1878, 1879, 1880, 1921, 1922, 1923, 1924, 1925]
    for i in range(10):
        lvl = i + 1
        wts_updates[r018_names[i]] = "|cffe4cfa3Увеличение маны|r"
        wts_updates[r018_tips[i]] = f"|cffe4cfa3Увеличение маны — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[r018_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас маны магов Даларана на |cffffffff{lvl * 50}|cffced4da ед., но снижает их здоровье на |cffe69a8d{lvl * 25}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n"
            "- |cffa9c7deПиромант|cffced4da|n- |cffa9c7deЧародей Льда|cffced4da|n"
            "- |cffa9c7deАрканист|cffced4da|n- |cffa9c7deЗаклинатель Света|cffced4da|n"
            "- |cffa9c7deЗачарователь|cffced4da|n- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff10|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R018", "field": f"name{lvl}", "expected": wts_updates[r018_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R018", "field": f"tip{lvl}", "expected": wts_updates[r018_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R018", "field": f"ubertip{lvl}", "expected": wts_updates[r018_ubts[i]]})

    # R017: Продолжительность жизни (10 levels)
    r017_names = [1850, 1856, 1857, 1858, 1859, 1891, 1892, 1893, 1894, 1895]
    r017_tips = [1819, 1831, 1832, 1833, 1834, 1896, 1897, 1898, 1899, 1905]
    r017_ubts = [1820, 1835, 1836, 1837, 1838, 1900, 1901, 1902, 1903, 1904]
    for i in range(10):
        lvl = i + 1
        wts_updates[r017_names[i]] = "|cffe4cfa3Продолжительность жизни|r"
        wts_updates[r017_tips[i]] = f"|cffe4cfa3Продолжительность жизни — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[r017_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья магов Даларана на |cffffffff{lvl * 50}|cffced4da ед., но снижает их запас маны на |cffe69a8d{lvl * 25}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n"
            "- |cffa9c7deПиромант|cffced4da|n- |cffa9c7deЧародей Льда|cffced4da|n"
            "- |cffa9c7deАрканист|cffced4da|n- |cffa9c7deЗаклинатель Света|cffced4da|n"
            "- |cffa9c7deЗачарователь|cffced4da|n- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff10|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R017", "field": f"name{lvl}", "expected": wts_updates[r017_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R017", "field": f"tip{lvl}", "expected": wts_updates[r017_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R017", "field": f"ubertip{lvl}", "expected": wts_updates[r017_ubts[i]]})

    # R015: Ускоренное произношение заклинаний (3 levels)
    r015_names = [1761, 1762, 1763]
    r015_tips = [1764, 1765, 1766]
    r015_ubts = [1928, 1929, 1930]
    for i in range(3):
        lvl = i + 1
        wts_updates[r015_names[i]] = "|cffe4cfa3Ускоренное произношение заклинаний|r"
        wts_updates[r015_tips[i]] = f"|cffe4cfa3Ускоренное произношение заклинаний — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[r015_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки магов Даларана магическим оружием на |cffffffff{lvl * 17}%|cffced4da.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПиромант|cffced4da|n"
            "- |cffa9c7deЧародей Льда|cffced4da|n- |cffa9c7deАрканист|cffced4da|n"
            "- |cffa9c7deЗаклинатель Света|cffced4da|n- |cffa9c7deЗачарователь|cffced4da|n"
            "- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R015", "field": f"name{lvl}", "expected": wts_updates[r015_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R015", "field": f"tip{lvl}", "expected": wts_updates[r015_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R015", "field": f"ubertip{lvl}", "expected": wts_updates[r015_ubts[i]]})

    # R016: Взгляд в Бездну (5 levels)
    r016_names = [1797, 1806, 1807, 1808, 1809]
    r016_tips = [1798, 1810, 1811, 1812, 1813]
    r016_ubts = [1799, 1814, 1815, 1816, 1817]
    for i in range(5):
        lvl = i + 1
        wts_updates[r016_names[i]] = "|cffe4cfa3Взгляд в Бездну|r"
        wts_updates[r016_tips[i]] = f"|cffe4cfa3Взгляд в Бездну — уровень {lvl}|r (|cffffffffQ|r)"
        spec_text = "открывает способность «Безумие Бездны»" if lvl == 1 else ("открывает способность «Забывчивость»" if lvl == 2 else "усиливает магический потенциал")
        wts_updates[r016_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас маны магов Бездны на |cffffffff{lvl * 35}|cffced4da ед. и {spec_text}.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff5|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R016", "field": f"name{lvl}", "expected": wts_updates[r016_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R016", "field": f"tip{lvl}", "expected": wts_updates[r016_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R016", "field": f"ubertip{lvl}", "expected": wts_updates[r016_ubts[i]]})

    # R00Z: Магия Огня (2 levels: Ученик / Адепт)
    wts_updates[1446] = "|cffe4cfa3Ученик стихии Огня|r"
    wts_updates[1449] = "|cffe4cfa3Ученик стихии Огня|r (|cffffffffA|r)"
    wts_updates[1573] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье пиромантов на |cffffffff50|cffced4da ед., ману на |cffffffff50|cffced4da ед., ускоряет регенерацию маны и открывает заклинание «Поджигание».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПиромант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    )
    wts_updates[1447] = "|cffe4cfa3Адепт стихии Огня|r"
    wts_updates[1450] = "|cffe4cfa3Адепт стихии Огня|r (|cffffffffA|r)"
    wts_updates[1574] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье пиромантов на |cffffffff50|cffced4da ед., ману на |cffffffff50|cffced4da ед. и открывает заклинание «Призыв создания огня».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПиромант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R00Z", "field": "name1", "expected": wts_updates[1446]})
    checks_def.append({"type": "upgrade", "id": "R00Z", "field": "tip1", "expected": wts_updates[1449]})
    checks_def.append({"type": "upgrade", "id": "R00Z", "field": "ubertip1", "expected": wts_updates[1573]})
    checks_def.append({"type": "upgrade", "id": "R00Z", "field": "name2", "expected": wts_updates[1447]})
    checks_def.append({"type": "upgrade", "id": "R00Z", "field": "tip2", "expected": wts_updates[1450]})
    checks_def.append({"type": "upgrade", "id": "R00Z", "field": "ubertip2", "expected": wts_updates[1574]})

    # R010: Магия Льда (2 levels: Ученик / Адепт)
    wts_updates[1513] = "|cffe4cfa3Ученик стихии Льда|r"
    wts_updates[1461] = "|cffe4cfa3Ученик стихии Льда|r (|cffffffffS|r)"
    wts_updates[1576] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье чародеев льда на |cffffffff40|cffced4da ед., ману на |cffffffff75|cffced4da ед., ускоряет регенерацию маны и открывает способность «Морозный доспех».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЧародей Льда|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    )
    wts_updates[1514] = "|cffe4cfa3Адепт стихии Льда|r"
    wts_updates[1462] = "|cffe4cfa3Адепт стихии Льда|r (|cffffffffS|r)"
    wts_updates[1577] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье чародеев льда на |cffffffff40|cffced4da ед., ману на |cffffffff75|cffced4da ед. и открывает способность «Призыв создания льда».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЧародей Льда|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R010", "field": "name1", "expected": wts_updates[1513]})
    checks_def.append({"type": "upgrade", "id": "R010", "field": "tip1", "expected": wts_updates[1461]})
    checks_def.append({"type": "upgrade", "id": "R010", "field": "ubertip1", "expected": wts_updates[1576]})
    checks_def.append({"type": "upgrade", "id": "R010", "field": "name2", "expected": wts_updates[1514]})
    checks_def.append({"type": "upgrade", "id": "R010", "field": "tip2", "expected": wts_updates[1462]})
    checks_def.append({"type": "upgrade", "id": "R010", "field": "ubertip2", "expected": wts_updates[1577]})

    # Rhse: Магический страж (1 level)
    wts_updates[40196] = "|cffe4cfa3Магический страж|r"
    wts_updates[40197] = "|cffe4cfa3Магический страж|r (|cffffffffS|r)"
    wts_updates[13312] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Магические Башни способностью обнаруживать находящиеся рядом невидимые войска противника.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагическая Башня|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "Rhse", "field": "name1", "expected": wts_updates[40196]})
    checks_def.append({"type": "upgrade", "id": "Rhse", "field": "tip1", "expected": wts_updates[40197]})
    checks_def.append({"type": "upgrade", "id": "Rhse", "field": "ubertip1", "expected": wts_updates[13312]})

    # R011: Тайная магия (2 levels: Ученик / Адепт)
    wts_updates[1519] = "|cffe4cfa3Ученик Тайной магии|r"
    wts_updates[1473] = "|cffe4cfa3Ученик Тайной магии|r (|cffffffffD|r)"
    wts_updates[1476] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье арканистов на |cffffffff40|cffced4da ед., ману на |cffffffff50|cffced4da ед., ускоряет регенерацию маны и открывает способность «Искажение времени».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАрканист|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    )
    wts_updates[1474] = "|cffe4cfa3Адепт Тайной магии|r"
    wts_updates[1521] = "|cffe4cfa3Адепт Тайной магии|r (|cffffffffD|r)"
    wts_updates[1477] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье арканистов на |cffffffff40|cffced4da ед., ману на |cffffffff50|cffced4da ед. и открывает способность «Зеркальное изображение».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАрканист|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R011", "field": "name1", "expected": wts_updates[1519]})
    checks_def.append({"type": "upgrade", "id": "R011", "field": "tip1", "expected": wts_updates[1473]})
    checks_def.append({"type": "upgrade", "id": "R011", "field": "ubertip1", "expected": wts_updates[1476]})
    checks_def.append({"type": "upgrade", "id": "R011", "field": "name2", "expected": wts_updates[1474]})
    checks_def.append({"type": "upgrade", "id": "R011", "field": "tip2", "expected": wts_updates[1521]})
    checks_def.append({"type": "upgrade", "id": "R011", "field": "ubertip2", "expected": wts_updates[1477]})

    # R01C: Познания Света (3 levels: Малые, Обширные, Глубокие)
    wts_updates[2694] = "|cffe4cfa3Малые познания Света|r"
    wts_updates[2697] = "|cffe4cfa3Малые познания Света|r (|cffffffffD|r)"
    wts_updates[20538] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье заклинателей Света на |cffffffff40|cffced4da ед., ману на |cffffffff50|cffced4da ед. и ускоряет регенерацию маны.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЗаклинатель Света|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1|cffced4da/|cffffffff3|cffced4da.|r"
    )
    wts_updates[2695] = "|cffe4cfa3Обширные познания Света|r"
    wts_updates[2698] = "|cffe4cfa3Обширные познания Света|r (|cffffffffD|r)"
    wts_updates[20539] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает характеристики заклинателей Света и открывает заклинание «Рассеивание заклинаний».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЗаклинатель Света|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2|cffced4da/|cffffffff3|cffced4da.|r"
    )
    wts_updates[2696] = "|cffe4cfa3Глубокие познания Света|r"
    wts_updates[2699] = "|cffe4cfa3Глубокие познания Света|r (|cffffffffD|r)"
    wts_updates[20540] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает характеристики заклинателей Света и открывает способность «Изгнание».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЗаклинатель Света|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3|cffced4da/|cffffffff3|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "name1", "expected": wts_updates[2694]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "tip1", "expected": wts_updates[2697]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "ubertip1", "expected": wts_updates[20538]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "name2", "expected": wts_updates[2695]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "tip2", "expected": wts_updates[2698]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "ubertip2", "expected": wts_updates[20539]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "name3", "expected": wts_updates[2696]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "tip3", "expected": wts_updates[2699]})
    checks_def.append({"type": "upgrade", "id": "R01C", "field": "ubertip3", "expected": wts_updates[20540]})

    # R01B: Зачарованное оружие (1 level)
    wts_updates[2489] = "|cffe4cfa3Зачарованное оружие|r"
    wts_updates[2492] = "|cffe4cfa3Зачарованное оружие|r (|cffffffffS|r)"
    wts_updates[27796] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Добавляет зачарованное оружие в экипировку зачарователей, увеличивая их скорость атаки на |cffffffff10%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЗачарователь|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01B", "field": "name1", "expected": wts_updates[2489]})
    checks_def.append({"type": "upgrade", "id": "R01B", "field": "tip1", "expected": wts_updates[2492]})
    checks_def.append({"type": "upgrade", "id": "R01B", "field": "ubertip1", "expected": wts_updates[27796]})

    # R01A: Магический Щит (1 level)
    wts_updates[2473] = "|cffe4cfa3Магический Щит|r"
    wts_updates[2476] = "|cffe4cfa3Магический Щит|r (|cffffffffS|r)"
    wts_updates[2479] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет пехотинцев способностью «Магический Щит» и увеличивает их запас маны на |cffffffff25|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01A", "field": "name1", "expected": wts_updates[2473]})
    checks_def.append({"type": "upgrade", "id": "R01A", "field": "tip1", "expected": wts_updates[2476]})
    checks_def.append({"type": "upgrade", "id": "R01A", "field": "ubertip1", "expected": wts_updates[2479]})

    # R00S: Магический Талисман (5 levels)
    r00s_names = [1178, 1187, 1188, 1189, 1190]
    r00s_tips = [1179, 1191, 1192, 1193, 1194]
    r00s_ubts = [13594, 13595, 13596, 13597, 15790]
    for i in range(5):
        lvl = i + 1
        wts_updates[r00s_names[i]] = "|cffe4cfa3Магический Талисман|r"
        wts_updates[r00s_tips[i]] = f"|cffe4cfa3Магический Талисман — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r00s_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость регенерации маны всех магов Даларана на |cffffffff{lvl * 10}%|cffced4da.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПиромант|cffced4da|n"
            "- |cffa9c7deЧародей Льда|cffced4da|n- |cffa9c7deАрканист|cffced4da|n"
            "- |cffa9c7deЗаклинатель Света|cffced4da|n- |cffa9c7deЗачарователь|cffced4da|n"
            "- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff5|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R00S", "field": f"name{lvl}", "expected": wts_updates[r00s_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R00S", "field": f"tip{lvl}", "expected": wts_updates[r00s_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R00S", "field": f"ubertip{lvl}", "expected": wts_updates[r00s_ubts[i]]})

    # R00R: Глубокие познания (5 levels)
    r00r_names = [1840, 1842, 1843, 1844, 1845]
    r00r_tips = [1841, 1846, 1847, 1848, 1849]
    r00r_ubts = [1159, 1174, 1175, 1176, 1177]
    for i in range(5):
        lvl = i + 1
        wts_updates[r00r_names[i]] = "|cffe4cfa3Глубокие познания|r"
        wts_updates[r00r_tips[i]] = f"|cffe4cfa3Глубокие познания — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r00r_ubts[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас маны всех магов Даларана на |cffffffff{lvl * 25}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПиромант|cffced4da|n"
            "- |cffa9c7deЧародей Льда|cffced4da|n- |cffa9c7deАрканист|cffced4da|n"
            "- |cffa9c7deЗаклинатель Света|cffced4da|n- |cffa9c7deЗачарователь|cffced4da|n"
            "- |cffa9c7deМаг Бездны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da/|cffffffff5|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R00R", "field": f"name{lvl}", "expected": wts_updates[r00r_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R00R", "field": f"tip{lvl}", "expected": wts_updates[r00r_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R00R", "field": f"ubertip{lvl}", "expected": wts_updates[r00r_ubts[i]]})

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================

    # A0I3: Скачок (Конструктор)
    wts_updates[26484] = "|cffe4cfa3Скачок|r"
    wts_updates[26476] = "|cffe4cfa3Скачок|r (|cffffffffC|r)"
    wts_updates[26477] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит конструктора на небольшое расстояние.|r"
    wts_updates[10064] = "|cffe4cfa3Скачок|r"
    wts_updates[10976] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит конструктора на небольшое расстояние.|r"
    checks_def.append({"type": "ability", "id": "A0I3", "field": "name", "expected": wts_updates[26484]})
    checks_def.append({"type": "ability", "id": "A0I3", "field": "tip1", "expected": wts_updates[26476]})
    checks_def.append({"type": "ability", "id": "A0I3", "field": "ubertip1", "expected": wts_updates[26477]})

    # Hero: H04S (Верховный маг)
    # A03K: Призыв элементаля воды
    wts_updates[2517] = "|cffe4cfa3Призыв элементаля воды|r"
    wts_updates[2524] = "|cffe4cfa3Призыв элементаля воды|r"
    wts_updates[3278] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь подконтрольного элементаля воды.|n|n"
        "|cffffcc001-й уровень:|r 1 элементаль.|n"
        "|cffffcc002-й уровень:|r 2 элементаля.|n"
        "|cffffcc003-й уровень:|r 3 элементаля.|n"
        "|cffffcc004-й уровень:|r 4 элементаля.|n"
        "|cffffcc005-й уровень:|r 5 элементалей.|r"
    )
    a03k_tips = [2520, 2521, 3445, 3448, 3449]
    a03k_ubts = [3247, 3248, 3249, 3250, 3261]
    for i in range(5):
        lvl = i + 1
        wts_updates[a03k_tips[i]] = f"|cffe4cfa3Призыв элементаля воды — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a03k_ubts[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь |cffffffff{lvl}|cffced4da элементалей воды.|r"
    checks_def.append({"type": "ability", "id": "A03K", "field": "name", "expected": wts_updates[2517]})

    # A03J: Кольцо льда
    wts_updates[2515] = "|cffe4cfa3Кольцо льда|r"
    wts_updates[2516] = "|cffe4cfa3Кольцо льда|r"
    wts_updates[2248] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает врагов вокруг цели ледяной волной, нанося урон и замедляя их передвижение и атаку.|r"
    wts_updates[29629] = "|cffe4cfa3Кольцо льда — уровень 4|r (|cffffffffQ|r)"
    wts_updates[1942] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff250|cffced4da ед. урона основной цели и |cffffffff200|cffced4da ед. урона по области, замедляя передвижение и атаку поражённых врагов.|r"
    wts_updates[2514] = "|cffe4cfa3Кольцо льда — уровень 5|r (|cffffffffQ|r)"
    wts_updates[1945] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff300|cffced4da ед. урона основной цели и |cffffffff250|cffced4da ед. урона по области, замедляя передвижение и атаку поражённых врагов.|r"
    checks_def.append({"type": "ability", "id": "A03J", "field": "name", "expected": wts_updates[2515]})

    # A03I: Ледяные оковы
    wts_updates[2502] = "|cffe4cfa3Ледяные оковы|r"
    wts_updates[2503] = "|cffe4cfa3Ледяные оковы|r"
    wts_updates[3246] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает ледяные оковы, оглушая находящихся рядом наземных врагов и нанося им урон.|r"
    wts_updates[2504] = "|cffe4cfa3Ледяные оковы — уровень 1|r (|cffffffffR|r)"
    wts_updates[18355] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оглушает находящихся рядом наземных воинов на |cffffffff5|cffced4da сек. (героев на |cffffffff1.5|cffced4da сек.) и наносит им урон.|r"
    wts_updates[2505] = "|cffe4cfa3Ледяные оковы — уровень 2|r (|cffffffffR|r)"
    wts_updates[18356] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оглушает находящихся рядом наземных воинов на |cffffffff7|cffced4da сек. (героев на |cffffffff2|cffced4da сек.) и наносит им урон.|r"
    checks_def.append({"type": "ability", "id": "A03I", "field": "name", "expected": wts_updates[2502]})

    # A03D: Аура мороза
    wts_updates[1700] = "|cffe4cfa3Аура мороза|r"
    wts_updates[2443] = "|cffe4cfa3Аура мороза|r"
    wts_updates[2509] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная аура. Замедляет скорость перемещения и атаки находящихся рядом вражеских войск.|r"
    wts_updates[2441] = "|cffe4cfa3Аура мороза — уровень 1|r"
    wts_updates[1791] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость перемещения врагов на |cffffffff15%|cffced4da и скорость атаки на |cffffffff10%|cffced4da в радиусе |cffffffff1000|cffced4da.|r"
    wts_updates[2445] = "|cffe4cfa3Аура мороза — уровень 2|r"
    wts_updates[2522] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость перемещения врагов на |cffffffff25%|cffced4da и скорость атаки на |cffffffff15%|cffced4da в радиусе |cffffffff1000|cffced4da.|r"
    wts_updates[2447] = "|cffe4cfa3Аура мороза — уровень 3|r"
    wts_updates[2523] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость перемещения врагов на |cffffffff35%|cffced4da и скорость атаки на |cffffffff20%|cffced4da в радиусе |cffffffff1000|cffced4da.|r"
    wts_updates[2450] = "|cffe4cfa3Аура мороза — уровень 4|r"
    wts_updates[4732] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость перемещения врагов на |cffffffff45%|cffced4da и скорость атаки на |cffffffff30%|cffced4da в радиусе |cffffffff1000|cffced4da.|r"
    wts_updates[2451] = "|cffe4cfa3Аура мороза — уровень 5|r"
    wts_updates[16071] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость перемещения врагов на |cffffffff50%|cffced4da и скорость атаки на |cffffffff35%|cffced4da в радиусе |cffffffff1000|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A03D", "field": "name", "expected": wts_updates[1700]})

    # Hero: H04W (Огненный мастер)
    # A03Q: Апокалипсис
    wts_updates[2582] = "|cffe4cfa3Апокалипсис|r"
    wts_updates[2591] = "|cffe4cfa3Апокалипсис|r"
    wts_updates[2592] = "|cffe4cfa3Апокалипсис — уровень 1|r (|cffffffffR|r)"
    wts_updates[2595] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает метеориты на указанную область и призывает магических созданий огня.|r"
    wts_updates[2593] = "|cffe4cfa3Апокалипсис — уровень 2|r (|cffffffffR|r)"
    wts_updates[2594] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает сокрушительный дождь метеоритов и призывает усиленных созданий огня.|r"
    checks_def.append({"type": "ability", "id": "A03Q", "field": "name", "expected": wts_updates[2582]})

    # A03O: Огненная стрела
    wts_updates[2574] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[2573] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[340] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня в противника, нанося урон и оглушая его.|r"
    wts_updates[2568] = "|cffe4cfa3Огненная стрела — уровень 1|r (|cffffffffW|r)"
    wts_updates[344] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff75|cffced4da ед. урона и оглушает цель на |cffffffff2|cffced4da сек.|r"
    wts_updates[2569] = "|cffe4cfa3Огненная стрела — уровень 2|r (|cffffffffW|r)"
    wts_updates[335] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff150|cffced4da ед. урона и оглушает воина на |cffffffff3|cffced4da сек. (героя на |cffffffff2|cffced4da сек.).|r"
    wts_updates[2570] = "|cffe4cfa3Огненная стрела — уровень 3|r (|cffffffffW|r)"
    wts_updates[336] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff270|cffced4da ед. урона и оглушает воина на |cffffffff4|cffced4da сек. (героя на |cffffffff2|cffced4da сек.).|r"
    wts_updates[2571] = "|cffe4cfa3Огненная стрела — уровень 4|r (|cffffffffW|r)"
    wts_updates[337] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff350|cffced4da ед. урона и оглушает воина на |cffffffff5|cffced4da сек. (героя на |cffffffff2|cffced4da сек.).|r"
    wts_updates[2572] = "|cffe4cfa3Огненная стрела — уровень 5|r (|cffffffffW|r)"
    wts_updates[339] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff430|cffced4da ед. урона и оглушает воина на |cffffffff6|cffced4da сек. (героя на |cffffffff2|cffced4da сек.).|r"
    checks_def.append({"type": "ability", "id": "A03O", "field": "name", "expected": wts_updates[2574]})

    # A03M: Огненный ливень
    wts_updates[2544] = "|cffe4cfa3Огненный ливень|r"
    wts_updates[3450] = "|cffe4cfa3Огненный ливень|r"
    wts_updates[15032] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область волны огня, наносящие мгновенный и периодический урон.|r"
    wts_updates[2545] = "|cffe4cfa3Огненный ливень — уровень 1|r (|cffffffffQ|r)"
    wts_updates[2547] = "|cffe4cfa3Огненный ливень — уровень 2|r (|cffffffffQ|r)"
    wts_updates[2551] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на область волны огня, наносящие урон и поджигающие цели.|r"
    wts_updates[2548] = "|cffe4cfa3Огненный ливень — уровень 3|r (|cffffffffQ|r)"
    wts_updates[2552] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на область волны огня, наносящие урон и поджигающие цели.|r"
    wts_updates[2549] = "|cffe4cfa3Огненный ливень — уровень 4|r (|cffffffffQ|r)"
    wts_updates[2553] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на область волны огня, наносящие урон и поджигающие цели.|r"
    wts_updates[2550] = "|cffe4cfa3Огненный ливень — уровень 5|r (|cffffffffQ|r)"
    wts_updates[2554] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на область волны огня, наносящие урон и поджигающие цели.|r"
    checks_def.append({"type": "ability", "id": "A03M", "field": "name", "expected": wts_updates[2544]})

    # A03L: Аура пламени
    wts_updates[2536] = "|cffe4cfa3Аура пламени|r"
    wts_updates[2537] = "|cffe4cfa3Аура пламени|r"
    wts_updates[2638] = "|cffe4cfa3Аура пламени — уровень 1|r"
    wts_updates[2639] = "|cffe4cfa3Аура пламени — уровень 2|r"
    wts_updates[2640] = "|cffe4cfa3Аура пламени — уровень 3|r"
    wts_updates[2641] = "|cffe4cfa3Аура пламени — уровень 4|r"
    wts_updates[7958] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает находящихся рядом союзников щитом, отражающим |cffffffff40%|cffced4da урона ближнего боя во врагов.|r"
    wts_updates[2642] = "|cffe4cfa3Аура пламени — уровень 5|r"
    wts_updates[2644] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает находящихся рядом союзников щитом, отражающим |cffffffff50%|cffced4da урона ближнего боя во врагов.|r"
    checks_def.append({"type": "ability", "id": "A03L", "field": "name", "expected": wts_updates[2536]})

    # Hero: H04X (Мастер Тайной магии)
    # A044: Сила магии
    wts_updates[2737] = "|cffe4cfa3Сила магии|r"
    wts_updates[2738] = "|cffe4cfa3Сила магии|r"
    wts_updates[33197] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет к автоатакам героини дополнительный урон от тайной магии.|r"
    wts_updates[2739] = "|cffe4cfa3Сила магии — уровень 1|r (|cffffffffW|r)"
    wts_updates[32337] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffffffff+15|cffced4da ед. дополнительного урона к автоатакам.|r"
    wts_updates[2740] = "|cffe4cfa3Сила магии — уровень 2|r (|cffffffffW|r)"
    wts_updates[32466] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffffffff+30|cffced4da ед. дополнительного урона к автоатакам.|r"
    wts_updates[2741] = "|cffe4cfa3Сила магии — уровень 3|r (|cffffffffW|r)"
    wts_updates[32953] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffffffff+40|cffced4da ед. дополнительного урона к автоатакам.|r"
    wts_updates[33198] = "|cffe4cfa3Сила магии — уровень 4|r (|cffffffffW|r)"
    wts_updates[33200] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffffffff+50|cffced4da ед. дополнительного урона к автоатакам.|r"
    wts_updates[33199] = "|cffe4cfa3Сила магии — уровень 5|r (|cffffffffW|r)"
    wts_updates[33201] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffffffff+60|cffced4da ед. дополнительного урона к автоатакам.|r"
    checks_def.append({"type": "ability", "id": "A044", "field": "name", "expected": wts_updates[2737]})

    # A03V: Массовая телепортация
    wts_updates[2657] = "|cffe4cfa3Массовая телепортация|r"
    wts_updates[38891] = "|cffe4cfa3Массовая телепортация|r"
    wts_updates[38892] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переносит находящихся рядом воинов к союзному бойцу или зданию.|r"
    wts_updates[2659] = "|cffe4cfa3Массовая телепортация — уровень 1|r (|cffffffffR|r)"
    wts_updates[2660] = "|cffe4cfa3Массовая телепортация — уровень 2|r (|cffffffffR|r)"
    wts_updates[2661] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переносит до |cffffffff24|cffced4da находящихся рядом союзных воинов к союзному бойцу или зданию.|r"
    checks_def.append({"type": "ability", "id": "A03V", "field": "name", "expected": wts_updates[2657]})

    # A03U: Аура гениальности
    wts_updates[2649] = "|cffe4cfa3Аура гениальности|r"
    wts_updates[2650] = "|cffe4cfa3Аура гениальности|r"
    wts_updates[20072] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная аура. Ускоряет регенерацию маны всех находящихся рядом союзников.|r"
    wts_updates[2651] = "|cffe4cfa3Аура гениальности — уровень 1|r"
    wts_updates[2652] = "|cffe4cfa3Аура гениальности — уровень 2|r"
    wts_updates[2653] = "|cffe4cfa3Аура гениальности — уровень 3|r"
    wts_updates[2654] = "|cffe4cfa3Аура гениальности — уровень 4|r"
    wts_updates[2648] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Значительно ускоряет регенерацию маны находящихся рядом союзников.|r"
    wts_updates[2655] = "|cffe4cfa3Аура гениальности — уровень 5|r"
    wts_updates[2656] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Колоссально ускоряет регенерацию маны находящихся рядом союзников.|r"
    checks_def.append({"type": "ability", "id": "A03U", "field": "name", "expected": wts_updates[2649]})

    # A1FQ: Похищение маны
    wts_updates[33210] = "|cffe4cfa3Похищение маны — уровень 4|r (|cffffffffQ|r)"
    wts_updates[33211] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает |cffffffff120|cffced4da ед. маны/сек. из врага или передает её союзнику.|r"
    wts_updates[33213] = "|cffe4cfa3Похищение маны — уровень 5|r (|cffffffffQ|r)"
    wts_updates[33214] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает |cffffffff150|cffced4da ед. маны/сек. из врага или передает её союзнику.|r"
    wts_updates[33212] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает ману из врага или передает её союзнику.|r"
    checks_def.append({"type": "ability", "id": "A1FQ", "field": "tip4", "expected": wts_updates[33210]})

    # Hero: H052 (Глава Кирин-Тора - Ронин)
    # A04E: Взрыв маны
    wts_updates[3302] = "|cffe4cfa3Взрыв маны|r"
    wts_updates[3303] = "|cffe4cfa3Взрыв маны|r"
    wts_updates[4685] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область сгустками маны, оглушая наземных врагов и нанося им урон.|r"
    wts_updates[3305] = "|cffe4cfa3Взрыв маны — уровень 1|r (|cffffffffQ|r)"
    wts_updates[4688] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область сгустками маны, нанося урон и оглушая наземных врагов на |cffffffff2|cffced4da сек.|r"
    wts_updates[3306] = "|cffe4cfa3Взрыв маны — уровень 2|r (|cffffffffQ|r)"
    wts_updates[4689] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает область сгустками маны, нанося повышенный урон и оглушая врагов.|r"
    wts_updates[3307] = "|cffe4cfa3Взрыв маны — уровень 3|r (|cffffffffQ|r)"
    wts_updates[4699] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает область сгустками маны, нанося высокий урон и оглушая врагов.|r"
    wts_updates[3308] = "|cffe4cfa3Взрыв маны — уровень 4|r (|cffffffffQ|r)"
    wts_updates[4707] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает область сгустками маны, нанося сокрушительный урон и оглушая врагов.|r"
    wts_updates[823] = "|cffe4cfa3Взрыв маны — уровень 5|r (|cffffffffQ|r)"
    wts_updates[4716] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает область мощнейшими сгустками маны, нанося колоссальный урон и оглушая врагов.|r"
    checks_def.append({"type": "ability", "id": "A04E", "field": "name", "expected": wts_updates[3302]})

    # A04D: Защита магии
    wts_updates[3301] = "|cffe4cfa3Защита магии|r"
    wts_updates[3328] = "|cffe4cfa3Защита магии|r"
    wts_updates[3329] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно поглощает часть получаемого урона от атак.|r"
    wts_updates[3291] = "|cffe4cfa3Защита магии — уровень 1|r"
    wts_updates[3323] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff12|cffced4da ед. получаемого урона от атак.|r"
    wts_updates[3292] = "|cffe4cfa3Защита магии — уровень 2|r"
    wts_updates[3324] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff15|cffced4da ед. получаемого урона от атак.|r"
    wts_updates[3293] = "|cffe4cfa3Защита магии — уровень 3|r"
    wts_updates[3325] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff25|cffced4da ед. получаемого урона от атак.|r"
    wts_updates[3294] = "|cffe4cfa3Защита магии — уровень 4|r"
    wts_updates[3326] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff30|cffced4da ед. получаемого урона от атак.|r"
    wts_updates[3295] = "|cffe4cfa3Защита магии — уровень 5|r"
    wts_updates[3327] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff40|cffced4da ед. получаемого урона от атак.|r"
    checks_def.append({"type": "ability", "id": "A04D", "field": "name", "expected": wts_updates[3301]})

    # A04B: Призыв Магических Артефактов
    wts_updates[3272] = "|cffe4cfa3Призыв Магических Артефактов|r"
    wts_updates[3271] = "|cffe4cfa3Призыв Магических Артефактов|r"
    wts_updates[27535] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает магические артефакты, атакующие врагов и исцеляющие союзников.|r"
    wts_updates[3266] = "|cffe4cfa3Призыв Магических Артефактов — уровень 1|r (|cffffffffR|r)"
    wts_updates[3275] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает магические реликвии, атакующие врагов и восстанавливающие здоровье союзникам.|r"
    wts_updates[3269] = "|cffe4cfa3Призыв Магических Артефактов — уровень 2|r (|cffffffffR|r)"
    wts_updates[3276] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает усиленные магические реликвии, непрерывно атакующие врагов и исцеляющие союзников.|r"
    checks_def.append({"type": "ability", "id": "A04B", "field": "name", "expected": wts_updates[3272]})

    # A04A: Ледяное Наказание
    wts_updates[3236] = "|cffe4cfa3Ледяное Наказание|r"
    wts_updates[3237] = "|cffe4cfa3Ледяное Наказание|r"
    wts_updates[11967] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя ледяной бурей, наносящей урон окружающим наземным врагам.|r"
    wts_updates[3238] = "|cffe4cfa3Ледяное Наказание — уровень 1|r (|cffffffffW|r)"
    wts_updates[6610] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит урон от холода в секунду находящимся рядом наземным врагам. Расходует ману до отмены.|r"
    wts_updates[3239] = "|cffe4cfa3Ледяное Наказание — уровень 2|r (|cffffffffW|r)"
    wts_updates[6821] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит повышенный урон от холода в секунду окружающим наземным врагам.|r"
    wts_updates[3240] = "|cffe4cfa3Ледяное Наказание — уровень 3|r (|cffffffffW|r)"
    wts_updates[7786] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит высокий урон от холода в секунду окружающим наземным врагам.|r"
    wts_updates[3244] = "|cffe4cfa3Ледяное Наказание — уровень 4|r (|cffffffffW|r)"
    wts_updates[7787] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит сокрушительный урон от холода в секунду окружающим наземным врагам.|r"
    wts_updates[3245] = "|cffe4cfa3Ледяное Наказание — уровень 5|r (|cffffffffW|r)"
    wts_updates[7788] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит мощнейший урон от холода в секунду окружающим наземным врагам.|r"
    checks_def.append({"type": "ability", "id": "A04A", "field": "name", "expected": wts_updates[3236]})

    # Hero: H053 (Хранитель - Кадгар)
    # A04I: Заморозка ран
    wts_updates[3385] = "|cffe4cfa3Заморозка ран|r"
    wts_updates[3386] = "|cffe4cfa3Заморозка ран|r"
    wts_updates[3387] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает ледяную волну, исцеляющую союзников вокруг цели.|r"
    wts_updates[3388] = "|cffe4cfa3Заморозка ран — уровень 1|r (|cffffffffQ|r)"
    wts_updates[3393] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает ледяную волну, восстанавливающую здоровье основной цели и союзникам по области.|r"
    wts_updates[3389] = "|cffe4cfa3Заморозка ран — уровень 2|r (|cffffffffQ|r)"
    wts_updates[3394] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье цели и окружающим союзникам по области.|r"
    wts_updates[3390] = "|cffe4cfa3Заморозка ран — уровень 3|r (|cffffffffQ|r)"
    wts_updates[3395] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье цели и окружающим союзникам по области.|r"
    wts_updates[3391] = "|cffe4cfa3Заморозка ран — уровень 4|r (|cffffffffQ|r)"
    wts_updates[3396] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье цели и окружающим союзникам по области.|r"
    wts_updates[3392] = "|cffe4cfa3Заморозка ран — уровень 5|r (|cffffffffQ|r)"
    wts_updates[3397] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье цели и окружающим союзникам по области.|r"
    checks_def.append({"type": "ability", "id": "A04I", "field": "name", "expected": wts_updates[3385]})

    # A04H: Волна смерти
    wts_updates[3374] = "|cffe4cfa3Волна смерти|r"
    wts_updates[3375] = "|cffe4cfa3Волна смерти|r"
    wts_updates[5922] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает мощную волну воды, наносящую урон врагам на своём пути.|r"
    wts_updates[3377] = "|cffe4cfa3Волна смерти — уровень 1|r (|cffffffffW|r)"
    wts_updates[5928] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну воды в секторе перед собой, нанося |cffffffff100|cffced4da ед. урона врагам на пути.|r"
    wts_updates[3378] = "|cffe4cfa3Волна смерти — уровень 2|r (|cffffffffW|r)"
    wts_updates[5933] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff150|cffced4da ед. урона врагам на пути.|r"
    wts_updates[3379] = "|cffe4cfa3Волна смерти — уровень 3|r (|cffffffffW|r)"
    wts_updates[6043] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff200|cffced4da ед. урона врагам на пути.|r"
    wts_updates[6057] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff250|cffced4da ед. урона врагам на пути.|r"
    wts_updates[6060] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff300|cffced4da ед. урона врагам на пути.|r"
    checks_def.append({"type": "ability", "id": "A04H", "field": "name", "expected": wts_updates[3374]})

    # A04G: Сожжение
    wts_updates[3348] = "|cffe4cfa3Сожжение|r"
    wts_updates[3349] = "|cffe4cfa3Сожжение|r"
    wts_updates[3350] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует огненную ауру, непрерывно сжигающую окружающих наземных врагов.|r"
    wts_updates[3351] = "|cffe4cfa3Сожжение — уровень 1|r (|cffffffffE|r)"
    wts_updates[3352] = "|cffe4cfa3Сожжение — уровень 2|r (|cffffffffE|r)"
    wts_updates[3353] = "|cffe4cfa3Сожжение — уровень 3|r (|cffffffffE|r)"
    wts_updates[3354] = "|cffe4cfa3Сожжение — уровень 4|r (|cffffffffE|r)"
    wts_updates[3356] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит урон от огня в секунду окружающим наземным врагам. Расходует ману до отмены.|r"
    wts_updates[3355] = "|cffe4cfa3Сожжение — уровень 5|r (|cffffffffE|r)"
    wts_updates[3357] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит высокий урон от огня в секунду окружающим наземным врагам. Расходует ману до отмены.|r"
    checks_def.append({"type": "ability", "id": "A04G", "field": "name", "expected": wts_updates[3348]})

    # Unit Abilities:
    # A03H: Магический Щит
    wts_updates[2468] = "|cffe4cfa3Магический Щит|r"
    wts_updates[2469] = "|cffe4cfa3Магический Щит|r (|cffffffffT|r)"
    checks_def.append({"type": "ability", "id": "A03H", "field": "name", "expected": wts_updates[2468]})

    # A02J / A00W: Огненная стрела (Пиромант)
    wts_updates[20501] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[20502] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[2259] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня, оглушающий цель и наносящий урон от пламени.|r"
    wts_updates[19732] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[20498] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[2273] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток пламени, оглушающий цель и наносящий урон от огня.|r"
    checks_def.append({"type": "ability", "id": "A02J", "field": "name", "expected": wts_updates[20501]})
    checks_def.append({"type": "ability", "id": "A00W", "field": "name", "expected": wts_updates[19732]})

    # A01W: Призыв создания огня
    wts_updates[1722] = "|cffe4cfa3Призыв создания огня|r"
    wts_updates[1723] = "|cffe4cfa3Призыв создания огня|r (|cffffffffR|r)"
    wts_updates[5383] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает подконтрольное магическое создание огня.|r"
    checks_def.append({"type": "ability", "id": "A01W", "field": "name", "expected": wts_updates[1722]})

    # A01O: Поджигание
    wts_updates[1600] = "|cffe4cfa3Поджигание|r"
    wts_updates[1601] = "|cffe4cfa3Поджигание|r (|cffffffffW|r)"
    wts_updates[1602] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает цель пламенем, наносящим периодический урон ей и окружающим войскам.|r"
    checks_def.append({"type": "ability", "id": "A01O", "field": "name", "expected": wts_updates[1600]})

    # A01N: Пламя феникса
    wts_updates[1596] = "|cffe4cfa3Пламя феникса|r"
    wts_updates[1595] = "|cffe4cfa3Пламя феникса|r (|cffffffffE|r)"
    wts_updates[1384] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает огненного феникса в секторе перед собой, наносящего урон всем врагам на пути.|r"
    checks_def.append({"type": "ability", "id": "A01N", "field": "name", "expected": wts_updates[1596]})

    # A01V: Ледяные стрелы
    wts_updates[1717] = "|cffe4cfa3Ледяные стрелы|r"
    wts_updates[1718] = "|cffe4cfa3Ледяные стрелы|r (|cffffffffE|r)"
    wts_updates[1719] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает ледяную стрелу, наносящую дополнительный урон и замедляющую атаку врага.|r"
    checks_def.append({"type": "ability", "id": "A01V", "field": "name", "expected": wts_updates[1717]})

    # A01U: Морозный доспех
    wts_updates[1708] = "|cffe4cfa3Морозный доспех|r"
    wts_updates[1709] = "|cffe4cfa3Морозный доспех|r (|cffffffffW|r)"
    wts_updates[3869] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Укрывает союзника ледяным щитом, повышающим броню и замедляющим атакующих его врагов ближнего боя.|r"
    checks_def.append({"type": "ability", "id": "A01U", "field": "name", "expected": wts_updates[1708]})

    # A01T: Ледяная тюрьма
    wts_updates[1703] = "|cffe4cfa3Ледяная тюрьма|r"
    wts_updates[1704] = "|cffe4cfa3Ледяная тюрьма|r (|cffffffffQ|r)"
    wts_updates[15143] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает ледяной сгусток, наносящий урон и оглушающий цель.|r"
    checks_def.append({"type": "ability", "id": "A01T", "field": "name", "expected": wts_updates[1703]})

    # A01Q: Призыв создания льда
    wts_updates[1617] = "|cffe4cfa3Призыв создания льда|r"
    wts_updates[1616] = "|cffe4cfa3Призыв создания льда|r (|cffffffffR|r)"
    wts_updates[2156] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает подконтрольное магическое создание льда.|r"
    checks_def.append({"type": "ability", "id": "A01Q", "field": "name", "expected": wts_updates[1617]})

    # A040 / A031: Изгнание
    wts_updates[2688] = "|cffe4cfa3Изгнание|r"
    wts_updates[2689] = "|cffe4cfa3Изгнание|r (|cffffffffR|r)"
    wts_updates[2775] = "|cffe4cfa3Изгнание|r"
    wts_updates[2774] = "|cffe4cfa3Изгнание|r (|cffffffffR|r)"
    wts_updates[3741] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переносит цель в астрал. Изгнанная цель не может атаковать и замедляется, но получает увеличенный урон от заклинаний.|r"
    checks_def.append({"type": "ability", "id": "A040", "field": "name", "expected": wts_updates[2688]})

    # A03Z: Глубокая вера
    wts_updates[2685] = "|cffe4cfa3Глубокая вера|r"
    wts_updates[2686] = "|cffe4cfa3Глубокая вера|r"
    wts_updates[6965] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная аура. Ускоряет регенерацию здоровья находящихся рядом союзных войск.|r"
    checks_def.append({"type": "ability", "id": "A03Z", "field": "name", "expected": wts_updates[2685]})

    # A03Y: Рассеивание заклинаний
    wts_updates[2683] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[2684] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffW|r)"
    checks_def.append({"type": "ability", "id": "A03Y", "field": "name", "expected": wts_updates[2683]})

    # A03X: Магический тотем
    wts_updates[2679] = "|cffe4cfa3Магический тотем|r"
    wts_updates[2680] = "|cffe4cfa3Магический тотем|r (|cffffffffQ|r)"
    wts_updates[555] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижный тотем, восстанавливающий союзникам вокруг себя |cffffffff1.5%|cffced4da здоровья в секунду.|r"
    checks_def.append({"type": "ability", "id": "A03X", "field": "name", "expected": wts_updates[2679]})

    # A03S: Массовая телепортация (Арканист)
    wts_updates[2608] = "|cffe4cfa3Массовая телепортация|r"
    wts_updates[2609] = "|cffe4cfa3Массовая телепортация|r (|cffffffffR|r)"
    wts_updates[18369] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переносит до |cffffffff6|cffced4da находящихся рядом союзных воинов к союзному зданию.|r"
    checks_def.append({"type": "ability", "id": "A03S", "field": "name", "expected": wts_updates[2608]})

    # A01M: Зеркальное изображение (Арканист)
    wts_updates[29059] = "|cffe4cfa3Зеркальное изображение|r"
    wts_updates[29060] = "|cffe4cfa3Зеркальное изображение|r (|cffffffffE|r)"
    wts_updates[3083] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт иллюзорную копию арканиста и снимает с него отрицательные эффекты.|r"
    checks_def.append({"type": "ability", "id": "A01M", "field": "name", "expected": wts_updates[29059]})

    # A01L: Сверхновая (Арканист)
    wts_updates[1583] = "|cffe4cfa3Сверхновая|r"
    wts_updates[1581] = "|cffe4cfa3Сверхновая|r (|cffffffffQ|r)"
    wts_updates[13113] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вызывает вспышку чародейской энергии вокруг цели, нанося урон от тайной магии и замедляя врагов.|r"
    checks_def.append({"type": "ability", "id": "A01L", "field": "name", "expected": wts_updates[1583]})

    # A01K: Искажение времени (Арканист)
    wts_updates[1566] = "|cffe4cfa3Искажение времени|r"
    wts_updates[1579] = "|cffe4cfa3Искажение времени — уровень 1|r (|cffffffffW|r)"
    wts_updates[203] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Искажает течение времени, временно повышая скорость перемещения и атаки союзников.|r"
    wts_updates[1580] = "|cffe4cfa3Искажение времени — уровень 2|r (|cffffffffW|r)"
    wts_updates[1586] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Значительно повышает скорость перемещения и атаки союзников на |cffffffff15|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A01K", "field": "name", "expected": wts_updates[1566]})

    # A03G: Сжигание маны (Зачарователь)
    wts_updates[5926] = "|cffe4cfa3Сжигание маны|r"
    wts_updates[5927] = "|cffe4cfa3Сжигание маны|r"
    wts_updates[1585] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно сжигает |cffffffff5|cffced4da ед. маны атакованного врага при каждом ударе.|r"
    checks_def.append({"type": "ability", "id": "A03G", "field": "name", "expected": wts_updates[5926]})

    # A01G: Сменить оружие (Меч)
    wts_updates[1503] = "|cffe4cfa3Сменить оружие (Меч)|r"
    wts_updates[1504] = "|cffe4cfa3Сменить оружие (Меч)|r (|cffffffffW|r)"
    wts_updates[1505] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Зачарователь меняет посох на меч, переходя в стойку ближнего боя.|r"
    checks_def.append({"type": "ability", "id": "A01G", "field": "name", "expected": wts_updates[1503]})

    # A01F: Сменить оружие (Посох)
    wts_updates[1486] = "|cffe4cfa3Сменить оружие (Посох)|r"
    wts_updates[1487] = "|cffe4cfa3Сменить оружие (Посох)|r (|cffffffffW|r)"
    wts_updates[1488] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Зачарователь меняет меч на посох, переходя в стойку дальнего боя.|r"
    checks_def.append({"type": "ability", "id": "A01F", "field": "name", "expected": wts_updates[1486]})

    # A03F / A03E: Зачарованное оружие
    wts_updates[2462] = "|cffe4cfa3Зачарованное оружие|r"
    wts_updates[2460] = "|cffe4cfa3Зачарованное оружие|r"
    wts_updates[2459] = "|cffe4cfa3Зачарованное оружие|r"
    wts_updates[2457] = "|cffe4cfa3Зачарованное оружие|r"
    checks_def.append({"type": "ability", "id": "A03F", "field": "name", "expected": wts_updates[2462]})
    checks_def.append({"type": "ability", "id": "A03E", "field": "name", "expected": wts_updates[2459]})

    # A021: Безумие Бездны (Маг Бездны)
    wts_updates[1952] = "|cffe4cfa3Безумие Бездны|r"
    wts_updates[1951] = "|cffe4cfa3Безумие Бездны|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "A021", "field": "name", "expected": wts_updates[1952]})

    # A022: Забывчивость (Маг Бездны)
    wts_updates[1953] = "|cffe4cfa3Забывчивость|r"
    wts_updates[1954] = "|cffe4cfa3Забывчивость|r (|cffffffffW|r)"
    checks_def.append({"type": "ability", "id": "A022", "field": "name", "expected": wts_updates[1953]})

    # A01X: Призыв создания Бездны
    wts_updates[1789] = "|cffe4cfa3Призыв создания Бездны|r"
    wts_updates[1790] = "|cffe4cfa3Призыв создания Бездны|r (|cffffffffE|r)"
    wts_updates[3112] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь порождение Бездны.|r"
    checks_def.append({"type": "ability", "id": "A01X", "field": "name", "expected": wts_updates[1789]})

    # A01S: Кольцо огня (Создание огня)
    wts_updates[1699] = "|cffe4cfa3Кольцо огня|r"
    wts_updates[1698] = "|cffe4cfa3Кольцо огня|r"
    wts_updates[29525] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Непрерывно наносит урон от огня в секунду находящимся рядом врагам.|r"
    checks_def.append({"type": "ability", "id": "A01S", "field": "name", "expected": wts_updates[1699]})

    # A01R: Аура мороза (Создание льда)
    wts_updates[1695] = "|cffe4cfa3Аура мороза|r"
    wts_updates[1696] = "|cffe4cfa3Аура мороза|r"
    wts_updates[2756] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость перемещения и атаки находящихся рядом противников.|r"
    checks_def.append({"type": "ability", "id": "A01R", "field": "name", "expected": wts_updates[1695]})

    # A045: Критический удар (Магический Эксперимент)
    wts_updates[2947] = "|cffe4cfa3Критический удар|r"
    wts_updates[2948] = "|cffe4cfa3Критический удар|r"
    checks_def.append({"type": "ability", "id": "A045", "field": "name", "expected": wts_updates[2947]})

    # Building abilities:
    # A1O5: Структурный щит
    wts_updates[24417] = "|cffe4cfa3Структурный щит|r"
    wts_updates[24418] = "|cffe4cfa3Структурный щит|r (|cffffffffD|r)"
    checks_def.append({"type": "ability", "id": "A1O5", "field": "name", "expected": wts_updates[24417]})

    # A03W: Восстановление маны
    wts_updates[2666] = "|cffe4cfa3Восстановление маны|r"
    wts_updates[2678] = "|cffe4cfa3Восстановление маны|r"
    wts_updates[5691] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Глобальная аура. Ускоряет регенерацию маны всех союзников по всей карте.|r"
    wts_updates[2667] = "|cffe4cfa3Восстановление маны|r"
    checks_def.append({"type": "ability", "id": "A03W", "field": "name", "expected": wts_updates[2666]})

    # A018: Восполнить ману
    wts_updates[1120] = "|cffe4cfa3Восполнить ману|r"
    wts_updates[1118] = "|cffe4cfa3Восполнить ману|r (|cffffffffQ|r)"
    wts_updates[1119] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно восполняет запас маны выбранного союзного юнита.|r"
    checks_def.append({"type": "ability", "id": "A018", "field": "name", "expected": wts_updates[1120]})

    # A0HY: Массовая телепортация (Телепорт n063)
    wts_updates[10846] = "|cffe4cfa3Массовая телепортация|r"
    wts_updates[10847] = "|cffe4cfa3Массовая телепортация|r (|cffffffffZ|r)"
    wts_updates[10853] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит всех союзных воинов рядом с порталом на другую сторону.|r"
    checks_def.append({"type": "ability", "id": "A0HY", "field": "name", "expected": wts_updates[10846]})

    # Output plan
    plan_data = {
        "race": "Даларан (Dalaran)",
        "race_id": 16,
        "selection_ability": "A0HN",
        "selection_markers": ["R0BW", "R0KK"],
        "categories": {
            "buildings": [
                "h030", "h031", "h02V", "h02W", "h02X", "h02Y",
                "h034", "h035", "h036", "h032", "h037", "h038",
                "n063", "h011"
            ],
            "units": [
                "u001", "h02I", "h02J", "h02K", "h02L", "h02M",
                "h02N", "h02O", "h02P", "n009", "n00A", "n00B",
                "n00M", "n00N"
            ],
            "heroes": [
                "H04S", "H04W", "H04X", "H052", "H053"
            ],
            "upgrades": [
                "R013", "R014", "R012", "R00Q", "R00T", "R018", "R017", "R015",
                "R016", "R00Z", "R010", "Rhse", "R011", "R01C", "R01B", "R01A",
                "R00S", "R00R", "R0BW", "R0KK"
            ],
            "abilities": [
                "A0HN", "A0I3",
                "A03K", "A03J", "A03I", "A03D",
                "A03Q", "A03O", "A03M", "A03L",
                "A044", "A03V", "A03U", "A1FQ",
                "A04E", "A04D", "A04B", "A04A",
                "A04I", "A04H", "A04G",
                "A03H", "A02J", "A00W", "A01W", "A01O", "A01N",
                "A01V", "A01U", "A01T", "A01Q",
                "A040", "A031", "A03Z", "A03Y", "A03X",
                "A03S", "A01M", "A01L", "A01K",
                "A03G", "A01G", "A01F", "A03F", "A03E",
                "A021", "A022", "A01X",
                "A01S", "A01R", "A045",
                "A1O5", "A03W", "A018", "A0HY"
            ]
        },
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def
    }

    out_file = folder / "dalaran_plan.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(plan_data, f, ensure_ascii=False, indent=2)

    print(f"Plan generated successfully:")
    print(f"  Total WTS updates: {len(wts_updates)}")
    print(f"  Total checks planned: {len(checks_def)}")
    print(f"  Saved to {out_file}")

if __name__ == "__main__":
    main()
