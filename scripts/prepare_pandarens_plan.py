# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Pandarens race (Race 34)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. RACE SELECTION & MARKER: A1I6, R0L3
    # =========================================================================
    # A1I6: Пандарены (Z)
    wts_updates[38913] = "|cffe4cfa3Пандарены|r"
    wts_updates[38914] = "|cffe4cfa3Пандарены|r (|cffffffffZ|r)"
    wts_updates[42408] = (
        "|cffa6afb8РАСА:|r |cffced4daМиролюбивые и мудрые жители Пандарии, в совершенстве владеющие боевыми искусствами, магией стихий и тайнами хмелеварения.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deCapral|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●|r|cffa6afb8○○○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Mists of Pandaria»|r|n|n"
        "|cffced4daПандарены — древний гармоничный народ Туманного континента, приверженцы равновесия стихий и внутреннего покоя. "
        "Однако их миролюбие обманчиво: в час опасности монахи и мастера стихий встают на защиту родной земли, обрушивая на врагов мощь огня, земли, бури и сокрушительную силу рукопашного боя. "
        "Чем богаче запасы на фермах пандаренов, тем крепче здоровье и стойкость их воинов.|r"
    )
    checks_def.append({"type": "ability", "id": "A1I6", "field": "name", "expected": wts_updates[38913]})
    checks_def.append({"type": "ability", "id": "A1I6", "field": "tip1", "expected": wts_updates[38914]})
    checks_def.append({"type": "ability", "id": "A1I6", "field": "ubertip1", "expected": wts_updates[42408]})

    # R0L3: Пандарены (маркер расы)
    wts_updates[28728] = "|cffe4cfa3Пандарены|r"
    checks_def.append({"type": "upgrade", "id": "R0L3", "field": "name1", "expected": wts_updates[28728]})

    # =========================================================================
    # 2. BUILDINGS (15 buildings)
    # =========================================================================
    # pa23: Ратуша Синего Зяблика (Q)
    wts_updates[36638] = "|cffe4cfa3Ратуша Синего Зяблика|r"
    wts_updates[35288] = "|cffe4cfa3Ратуша Синего Зяблика|r (|cffffffffQ|r)"
    wts_updates[2214] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daГлавное здание первой ступени. Обеспечивает добычу ресурсов и начальный лимит пищи.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n- |cffa9c7deРабочий Пандаренов|cffced4da: базовый рабочий и строитель.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n- |cffa9c7deУсиление Мастеров Земли|cffced4da|n"
        "- |cffa9c7deУсиление Мастеров Огня|cffced4da|n"
        "- |cffa9c7deИзучение Хмелеварения|cffced4da|n"
        "- |cffa9c7deИзучить Геомантию|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|r|cffced4da|n- |cffa9c7deКрепость Четырёх Мастеров|cffced4da: требует не менее 20 ферм или рыбацких домов.|r"
    )
    checks_def.append({"type": "unit", "id": "pa23", "field": "name", "expected": wts_updates[36638]})
    checks_def.append({"type": "unit", "id": "pa23", "field": "tip", "expected": wts_updates[35288]})
    checks_def.append({"type": "unit", "id": "pa23", "field": "ubertip", "expected": wts_updates[2214]})

    # pa24: Крепость Четырёх Мастеров (U)
    wts_updates[3144] = "|cffe4cfa3Крепость Четырёх Мастеров|r"
    wts_updates[35292] = "|cffe4cfa3Крепость Четырёх Мастеров|r (|cffffffffU|r)"
    checks_def.append({"type": "unit", "id": "pa24", "field": "name", "expected": wts_updates[3144]})
    checks_def.append({"type": "unit", "id": "pa24", "field": "tip", "expected": wts_updates[35292]})

    # pa25: Цитадель Равновесия (U)
    wts_updates[3145] = "|cffe4cfa3Цитадель Равновесия|r"
    wts_updates[35294] = "|cffe4cfa3Цитадель Равновесия|r (|cffffffffU|r)"
    checks_def.append({"type": "unit", "id": "pa25", "field": "name", "expected": wts_updates[3145]})
    checks_def.append({"type": "unit", "id": "pa25", "field": "tip", "expected": wts_updates[35294]})

    # pa26: Ферма (A)
    wts_updates[36639] = "|cffe4cfa3Ферма|r"
    wts_updates[2241] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daОбеспечивает армию пандаренов провизией. Увеличение числа ферм усиливает здоровье воинов по расовой способности.|n|n"
        "Даёт |cffffffff20|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "pa26", "field": "name", "expected": wts_updates[36639]})
    checks_def.append({"type": "unit", "id": "pa26", "field": "ubertip", "expected": wts_updates[2241]})

    # pa27: Алтарь Древних Мастеров (S)
    wts_updates[36640] = "|cffe4cfa3Алтарь Древних Мастеров|r"
    wts_updates[35296] = "|cffe4cfa3Алтарь Древних Мастеров|r (|cffffffffS|r)"
    wts_updates[2283] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daСлужит для призыва и воскрешения павших героев расы Пандаренов.|n|n"
        "|cffa6afb8Герои:|r|cffced4da|n- |cffa9c7deЛидер Шадо-Пан|cffced4da: герой поддержки и призыва подкреплений.|n"
        "- |cffa9c7deМастер Железной Лапы|cffced4da: несокрушимый защитник ближнего боя с каменной стойкостью.|n"
        "- |cffa9c7deВысший Монах|cffced4da: повелитель бури и целитель союзников.|n"
        "- |cffa9c7deТанцующий с Ветром|cffced4da: стремительный мастер клинка со скрытными атаками.|r"
    )
    checks_def.append({"type": "unit", "id": "pa27", "field": "name", "expected": wts_updates[36640]})
    checks_def.append({"type": "unit", "id": "pa27", "field": "tip", "expected": wts_updates[35296]})
    checks_def.append({"type": "unit", "id": "pa27", "field": "ubertip", "expected": wts_updates[2283]})

    # pa28: Палаты мастеров (W)
    wts_updates[36641] = "|cffe4cfa3Палаты мастеров|r"
    wts_updates[35298] = "|cffe4cfa3Палаты мастеров|r (|cffffffffW|r)"
    wts_updates[2285] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daБазовое военное сооружение. Обучает пехоту, стрелков, всадников и элитных мастеров.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n- |cffa9c7deВоин Пандаренов|cffced4da: базовый боец ближнего боя.|n"
        "- |cffa9c7deЛучник Пандаренов|cffced4da: стрелок дальнего боя с грозовыми стрелами.|n"
        "- |cffa9c7deВсадник Пандарен|cffced4da: мобильный боец кавалерии.|n"
        "- |cffa9c7deМастер Геомант|cffced4da: маг земли и целитель (требует «Изучить Геомантию»).|n"
        "- |cffa9c7deХмелевар|cffced4da: элитный боец-гибрид (требует «Изучение Хмелеварения»).|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n- |cffa9c7deСделать Геомантов Адептами|cffced4da|n"
        "- |cffa9c7deСделать Хмелеваров адептами|cffced4da|n"
        "- |cffa9c7deУтяжелённая Рукоять|cffced4da|n"
        "- |cffa9c7deНефритовые Доспехи|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "pa28", "field": "name", "expected": wts_updates[36641]})
    checks_def.append({"type": "unit", "id": "pa28", "field": "tip", "expected": wts_updates[35298]})
    checks_def.append({"type": "unit", "id": "pa28", "field": "ubertip", "expected": wts_updates[2285]})

    # pa30: Башня размышления (E)
    wts_updates[36642] = "|cffe4cfa3Башня размышления|r"
    wts_updates[35679] = "|cffe4cfa3Башня размышления|r (|cffffffffE|r)"
    wts_updates[2320] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daАкадемия и кузница пандаренов. Служит для исследования улучшений атаки, брони и заготовки древесины.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n- |cffa9c7deЖелезные Мечи|cffced4da: повышает урон бойцов ближнего боя (уровни 1–6).|n"
        "- |cffa9c7deЖелезная Броня|cffced4da: повышает защиту бойцов ближнего боя (уровни 1–6).|n"
        "- |cffa9c7deСтальные Наконечники|cffced4da: повышает урон стрелков и артиллерии (уровни 1–6).|n"
        "- |cffa9c7deДоспехи из кожи|cffced4da: повышает защиту стрелков и артиллерии (уровни 1–6).|n"
        "- |cffa9c7deУлучшенные топоры|cffced4da: увеличивает добычу древесины (уровни 1–6).|r"
    )
    checks_def.append({"type": "unit", "id": "pa30", "field": "name", "expected": wts_updates[36642]})
    checks_def.append({"type": "unit", "id": "pa30", "field": "tip", "expected": wts_updates[35679]})
    checks_def.append({"type": "unit", "id": "pa30", "field": "ubertip", "expected": wts_updates[2320]})

    # pa31: Оружейная (D)
    wts_updates[36643] = "|cffe4cfa3Оружейная|r"
    wts_updates[35302] = "|cffe4cfa3Оружейная|r (|cffffffffD|r)"
    wts_updates[2322] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daПодготавливает тяжелую пехоту, стражей врат и осадную артиллерию пандаренов.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n- |cffa9c7deВоин Нефритовой Стражи|cffced4da: бронированный тяжелый пехотинец.|n"
        "- |cffa9c7deСтражник Нефритовых Врат|cffced4da: защитник с невосприимчивостью к заклинаниям.|n"
        "- |cffa9c7deОрудийный Расчёт|cffced4da: дальнобойная осадная мортира.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n- |cffa9c7deДрессировка Животных|cffced4da|n"
        "- |cffa9c7deДлинные Луки|cffced4da|n"
        "- |cffa9c7deЗащита Ци|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "pa31", "field": "name", "expected": wts_updates[36643]})
    checks_def.append({"type": "unit", "id": "pa31", "field": "tip", "expected": wts_updates[35302]})
    checks_def.append({"type": "unit", "id": "pa31", "field": "ubertip", "expected": wts_updates[2322]})

    # pa32: Вместилище Стихий (F)
    wts_updates[36644] = "|cffe4cfa3Вместилище Стихий|r"
    wts_updates[35304] = "|cffe4cfa3Вместилище Стихий|r (|cffffffffF|r)"
    wts_updates[2369] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daСвятилище духов стихий. Обучает мастеров огня, земли и бури, а также развивает их способности.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n- |cffa9c7deМастер Огня|cffced4da: штурмовик ближнего боя с огненной аурой.|n"
        "- |cffa9c7deМастер Земли|cffced4da: стойкий боец ближнего боя с рассекающими ударами.|n"
        "- |cffa9c7deМастер Бури|cffced4da: маг дальнего боя с вихрями и раздвоенной молнией.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n- |cffa9c7deПосвящение Мастеров Огня|cffced4da|n"
        "- |cffa9c7deПосвящение Мастеров Земли|cffced4da|n"
        "- |cffa9c7deПосвящение Мастеров Бури|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "pa32", "field": "name", "expected": wts_updates[36644]})
    checks_def.append({"type": "unit", "id": "pa32", "field": "tip", "expected": wts_updates[35304]})
    checks_def.append({"type": "unit", "id": "pa32", "field": "ubertip", "expected": wts_updates[2369]})

    # pa33: Обитель Монахов (R)
    wts_updates[36645] = "|cffe4cfa3Обитель Монахов|r"
    wts_updates[35306] = "|cffe4cfa3Обитель Монахов|r (|cffffffffR|r)"
    wts_updates[2371] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daМонастырь боевых искусств. Обучает монахов Инь и Ян, стражей храма и мастеров стиля Пьяной Лапы.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n- |cffa9c7deМонах Инь|cffced4da: маг поддержки с рассеиванием заклинаний и исцелением.|n"
        "- |cffa9c7deМонах Ян|cffced4da: монах ярости и боевого баланса.|n"
        "- |cffa9c7deМастер Пьяной Лапы|cffced4da: боец ближнего боя с оглушающими ударами.|n"
        "- |cffa9c7deСтраж Храма|cffced4da: элитный защитник с аурой регенерации маны.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n- |cffa9c7deСделать Монахов Адептами|cffced4da|n"
        "- |cffa9c7deПосвящение Монахов Ян в адепты|cffced4da|n"
        "- |cffa9c7deСекреты Древних Мастеров|cffced4da|n"
        "- |cffa9c7deУкрепление Духа|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "pa33", "field": "name", "expected": wts_updates[36645]})
    checks_def.append({"type": "unit", "id": "pa33", "field": "tip", "expected": wts_updates[35306]})
    checks_def.append({"type": "unit", "id": "pa33", "field": "ubertip", "expected": wts_updates[2371]})

    # h0NZ: Рыбацкий дом (X)
    wts_updates[36654] = "|cffe4cfa3Рыбацкий дом|r"
    wts_updates[35959] = "|cffe4cfa3Рыбацкий дом|r (|cffffffffX|r)"
    wts_updates[3593] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daОбеспечивает припасами и свежей рыбой армию пандаренов. Засчитывается для перехода на следующие ступени цитадели.|n|n"
        "Даёт |cffffffff20|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "h0NZ", "field": "name", "expected": wts_updates[36654]})
    checks_def.append({"type": "unit", "id": "h0NZ", "field": "tip", "expected": wts_updates[35959]})
    checks_def.append({"type": "unit", "id": "h0NZ", "field": "ubertip", "expected": wts_updates[3593]})

    # h0P5: Башня Пандаренов (Z)
    wts_updates[36646] = "|cffe4cfa3Башня Пандаренов|r"
    wts_updates[35309] = "|cffe4cfa3Башня Пандаренов|r (|cffffffffZ|r)"
    wts_updates[25066] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daБазовое оборонительное сооружение и защитная стена пандаренов.|n|n"
        "|cffa6afb8Улучшение:|r|cffced4da|n- |cffa9c7deЗащитная Башня Пандаренов|cffced4da: скорострельная башня.|n"
        "- |cffa9c7deМагическая Башня Пандаренов|cffced4da: башня с магическим уроном.|n"
        "- |cffa9c7deОсадная Башня Пандаренов|cffced4da: тяжелая башня с уроном по площади.|r"
    )
    checks_def.append({"type": "unit", "id": "h0P5", "field": "name", "expected": wts_updates[36646]})
    checks_def.append({"type": "unit", "id": "h0P5", "field": "tip", "expected": wts_updates[35309]})
    checks_def.append({"type": "unit", "id": "h0P5", "field": "ubertip", "expected": wts_updates[25066]})

    # pa34: Защитная Башня Пандаренов (Z)
    wts_updates[2874] = "|cffe4cfa3Защитная Башня Пандаренов|r"
    wts_updates[20695] = "|cffe4cfa3Защитная Башня Пандаренов|r (|cffffffffZ|r)"
    wts_updates[2406] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daСкорострельная оборонительная башня, обстреливающая приближающихся противников.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa34", "field": "name", "expected": wts_updates[2874]})
    checks_def.append({"type": "unit", "id": "pa34", "field": "tip", "expected": wts_updates[20695]})
    checks_def.append({"type": "unit", "id": "pa34", "field": "ubertip", "expected": wts_updates[2406]})

    # h0P3: Магическая Башня Пандаренов (Z)
    wts_updates[9508] = "|cffe4cfa3Магическая Башня Пандаренов|r"
    wts_updates[22645] = "|cffe4cfa3Магическая Башня Пандаренов|r (|cffffffffZ|r)"
    wts_updates[20700] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daОборонительная башня, поражающая врагов концентрированными зарядами энергии Ци.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0P3", "field": "name", "expected": wts_updates[9508]})
    checks_def.append({"type": "unit", "id": "h0P3", "field": "tip", "expected": wts_updates[22645]})
    checks_def.append({"type": "unit", "id": "h0P3", "field": "ubertip", "expected": wts_updates[20700]})

    # h0P4: Осадная Башня Пандаренов (Z)
    wts_updates[22644] = "|cffe4cfa3Осадная Башня Пандаренов|r"
    wts_updates[25064] = "|cffe4cfa3Осадная Башня Пандаренов|r (|cffffffffZ|r)"
    wts_updates[22988] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daТяжелая орудийная башня, поражающая врагов разрывными пороховыми зарядами по площади.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0P4", "field": "name", "expected": wts_updates[22644]})
    checks_def.append({"type": "unit", "id": "h0P4", "field": "tip", "expected": wts_updates[25064]})
    checks_def.append({"type": "unit", "id": "h0P4", "field": "ubertip", "expected": wts_updates[22988]})

    # =========================================================================
    # 3. HEROES (5 heroes)
    # =========================================================================
    # PA36: Лидер Шадо-Пан (W)
    wts_updates[21966] = "|cffe4cfa3Лидер Шадо-Пан|r"
    wts_updates[35317] = "|cffa9c7deХуниг Тростниковая Вода|r"
    wts_updates[30098] = "|cffe4cfa3Лидер Шадо-Пан|r (|cffffffffW|r)"
    wts_updates[26526] = "|cffe4cfa3Лидер Шадо-Пан|r"
    wts_updates[33471] = "|cffe4cfa3Лидер Шадо-Пан|r"
    wts_updates[40296] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daГлава тайного ордена Шадо-Пан, мастер тактики и призыва подкреплений, усиливающий натиск соратников.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deПризыв Помощи|cffced4da: открывает портал, вызывающий союзных бойцов на поле боя.|n"
        "- |cffa9c7deВоодушевляющее Присутствие|cffced4da: аура, повышающая силу атаки союзных войск.|n"
        "- |cffa9c7deПьяный Мастер|cffced4da: шанс уклониться от атаки и нанести критический урон.|n"
        "- |cffa9c7deЗащита Древних Мастеров|cffced4da: особая способность, дарующая временную неуязвимость окружающим союзникам.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffЛовкость|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "PA36", "field": "name", "expected": wts_updates[21966]})
    checks_def.append({"type": "unit", "id": "PA36", "field": "propernames", "expected": wts_updates[35317]})
    checks_def.append({"type": "unit", "id": "PA36", "field": "tip", "expected": wts_updates[30098]})
    checks_def.append({"type": "unit", "id": "PA36", "field": "ubertip", "expected": wts_updates[40296]})

    # PA37: Мастер Железной Лапы (R)
    wts_updates[36651] = "|cffe4cfa3Мастер Железной Лапы|r"
    wts_updates[35322] = "|cffa9c7deСиндзё Медовар|r"
    wts_updates[6726] = "|cffe4cfa3Мастер Железной Лапы|r (|cffffffffR|r)"
    wts_updates[5226] = "|cffe4cfa3Мастер Железной Лапы|r"
    wts_updates[6728] = "|cffe4cfa3Мастер Железной Лапы|r"
    wts_updates[40297] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daНесокрушимый защитник Пандарии, принимающий на себя удары противников и сокрушающий врагов мощью монастыря Земли.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deУдар Восходящего Солнца|cffced4da: оглушает врага броском молота и наносит урон.|n"
        "- |cffa9c7deВыдержка Монастыря Земли|cffced4da: каменная стойкость, существенно снижающая получаемый урон от атак.|n"
        "- |cffa9c7deПровокация|cffced4da: вынуждает врагов атаковать героя, возвращая часть полученного урона.|n"
        "- |cffa9c7deПьяный Мастер|cffced4da: шанс уклониться от удара и нанести критический урон.|n"
        "- |cffa9c7deЕдинение с Инь|cffced4da: особая способность, колоссально повышающая здоровье, броню, урон и дарующая невосприимчивость к магии.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "PA37", "field": "name", "expected": wts_updates[36651]})
    checks_def.append({"type": "unit", "id": "PA37", "field": "propernames", "expected": wts_updates[35322]})
    checks_def.append({"type": "unit", "id": "PA37", "field": "tip", "expected": wts_updates[6726]})
    checks_def.append({"type": "unit", "id": "PA37", "field": "ubertip", "expected": wts_updates[40297]})

    # PA38: Высший Монах (Q)
    wts_updates[35265] = "|cffe4cfa3Высший Монах|r"
    wts_updates[35330] = "|cffa9c7deМоджо Ярость Стихий|r"
    wts_updates[35300] = "|cffe4cfa3Высший Монах|r (|cffffffffQ|r)"
    wts_updates[35328] = "|cffe4cfa3Высший Монах|r"
    wts_updates[35329] = "|cffe4cfa3Высший Монах|r"
    wts_updates[40298] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daМастер духовных энергий, подчинивший силу бури и целительные потоки Ци для защиты союзников и уничтожения орд врагов.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deВолна исцеления|cffced4da: волна энергии Ци, последовательно исцеляющая группу союзников.|n"
        "- |cffa9c7deЦепная молния|cffced4da: электрический разряд, поражающий цепочку вражеских целей.|n"
        "- |cffa9c7deПьяный Мастер|cffced4da: шанс уклониться от атаки и нанести критический урон.|n"
        "- |cffa9c7deКатаклизм|cffced4da: особая способность, призывающая опустошительную бурю молний в выбранную область.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "PA38", "field": "name", "expected": wts_updates[35265]})
    checks_def.append({"type": "unit", "id": "PA38", "field": "propernames", "expected": wts_updates[35330]})
    checks_def.append({"type": "unit", "id": "PA38", "field": "tip", "expected": wts_updates[35300]})
    checks_def.append({"type": "unit", "id": "PA38", "field": "ubertip", "expected": wts_updates[40298]})

    # PA40: Танцующий с Ветром (E)
    wts_updates[36648] = "|cffe4cfa3Танцующий с Ветром|r"
    wts_updates[35311] = "|cffa9c7deМоджо Тёмный Эль|r"
    wts_updates[6733] = "|cffe4cfa3Танцующий с Ветром|r"
    wts_updates[40300] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daСтремительный и неуловимый мастер клинка, наносящий смертоносные удары из невидимости и рассекающий армии вихрем стали.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deВеер Клинков|cffced4da: шквал кинжалов, наносящий урон всем окружающим врагам.|n"
        "- |cffa9c7deТанец Ветра|cffced4da: невидимость и ускорение с мощным бонусным уроном при выходе из скрытности.|n"
        "- |cffa9c7deТехника Тысячи Порезов|cffced4da: мастерство критических ударов огромной разрушительной силы.|n"
        "- |cffa9c7deПьяный Мастер|cffced4da: шанс уклониться от вражеской атаки и нанести критический урон.|n"
        "- |cffa9c7deБуря Клинков|cffced4da: особая способность, окружающая героя вихрем клинков с иммунитетом к магии.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffЛовкость|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "PA40", "field": "name", "expected": wts_updates[36648]})
    checks_def.append({"type": "unit", "id": "PA40", "field": "propernames", "expected": wts_updates[35311]})
    checks_def.append({"type": "unit", "id": "PA40", "field": "ubertip", "expected": wts_updates[40300]})

    # pa22: Хмелевар (R) (элитный гибридный юнит / мастер-хмелевар)
    wts_updates[36637] = "|cffe4cfa3Хмелевар|r"
    wts_updates[35287] = "|cffe4cfa3Хмелевар|r (|cffffffffR|r)"
    wts_updates[33306] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daЭлитный мастер пандаренского хмелеварения. Обливает врагов хмелем, сжигает дыханием огня и воодушевляет армию кружкой пива.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deПламенное дыхание|cffced4da: выдыхает конус пламени, поджигая облитых отваром врагов.|n"
        "- |cffa9c7deХмельные пары|cffced4da: обливает врагов отваром, вызывая промахи и замедление.|n"
        "- |cffa9c7deБагманское пиво|cffced4da: аура, ускоряющая передвижение и регенерацию здоровья союзников.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклониться от удара и нанести увеличенный урон.|n|n"
        "|cffa6afb8Требуется исследование:|r |cffa9c7deИзучение Хмелеварения|r.|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa22", "field": "name", "expected": wts_updates[36637]})
    checks_def.append({"type": "unit", "id": "pa22", "field": "tip", "expected": wts_updates[35287]})
    checks_def.append({"type": "unit", "id": "pa22", "field": "ubertip", "expected": wts_updates[33306]})

    # =========================================================================
    # 4. UNITS (14 units)
    # =========================================================================
    # pa01: Рабочий Пандаренов (Q)
    wts_updates[14453] = "|cffe4cfa3Рабочий Пандаренов|r"
    wts_updates[3538] = "|cffe4cfa3Рабочий Пандаренов|r (|cffffffffQ|r)"
    wts_updates[42400] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daБазовый рабочий пандаренов. Добывает золото и древесину, возводит и ремонтирует здания.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deРемонтировать|cffced4da: восстанавливает прочность зданий и механизмов.|n"
        "- |cffa9c7deДобывать Ресурсы|cffced4da: добыча золота в рудниках и заготовка древесины.|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткое расстояние.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклониться от атаки.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa01", "field": "name", "expected": wts_updates[14453]})
    checks_def.append({"type": "unit", "id": "pa01", "field": "tip", "expected": wts_updates[3538]})
    checks_def.append({"type": "unit", "id": "pa01", "field": "ubertip", "expected": wts_updates[42400]})

    # pa05: Воин Пандаренов (Q)
    wts_updates[16554] = "|cffe4cfa3Воин Пандаренов|r"
    wts_updates[39812] = "|cffe4cfa3Воин Пандаренов|r (|cffffffffQ|r)"
    wts_updates[31735] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daБазовый боец ближнего боя армии пандаренов. Стойкий рукопашник первой линии.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deЧувство баланса|cffced4da: 7% шанс уклониться от атаки и 10% шанс нанести на 20% больше урона.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa05", "field": "name", "expected": wts_updates[16554]})
    checks_def.append({"type": "unit", "id": "pa05", "field": "tip", "expected": wts_updates[39812]})
    checks_def.append({"type": "unit", "id": "pa05", "field": "ubertip", "expected": wts_updates[31735]})

    # pa12: Лучник Пандаренов (W)
    wts_updates[36627] = "|cffe4cfa3Лучник Пандаренов|r"
    wts_updates[42401] = "|cffe4cfa3Лучник Пандаренов|r (|cffffffffW|r)"
    wts_updates[31818] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМеткий стрелок дальнего боя. Эффективен против наземных и летающих противников.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deГрозовые Стрелы|cffced4da: заряжает стрелы электричеством, нанося дополнительный урон.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa12", "field": "name", "expected": wts_updates[36627]})
    checks_def.append({"type": "unit", "id": "pa12", "field": "tip", "expected": wts_updates[42401]})
    checks_def.append({"type": "unit", "id": "pa12", "field": "ubertip", "expected": wts_updates[31818]})

    # pa11: Всадник Пандарен (E)
    wts_updates[36626] = "|cffe4cfa3Всадник Пандарен|r"
    wts_updates[39813] = "|cffe4cfa3Всадник Пандарен|r (|cffffffffE|r)"
    wts_updates[31817] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daБыстрый всадник пандаренов верхом на боевом звере. Мобильная ударная кавалерия.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deЧувство баланса|cffced4da: шанс уклониться от удара и нанести увеличенный урон.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa11", "field": "name", "expected": wts_updates[36626]})
    checks_def.append({"type": "unit", "id": "pa11", "field": "tip", "expected": wts_updates[39813]})
    checks_def.append({"type": "unit", "id": "pa11", "field": "ubertip", "expected": wts_updates[31817]})

    # pa06: Мастер Геомант (R)
    wts_updates[23143] = "|cffe4cfa3Мастер Геомант|r"
    wts_updates[35246] = "|cffe4cfa3Мастер Геомант|r (|cffffffffR|r)"
    wts_updates[31749] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМонах-геомант, черпающий силу из недр земли. Сжигает ману врагов и исцеляет соратников.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deУдары Ци|cffced4da: каждая атака сжигает ману цели и наносит дополнительный урон.|n"
        "- |cffa9c7deЭнергия Ци|cffced4da: волна исцеления, восстанавливающая здоровье союзников.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Требуется исследование:|r |cffa9c7deИзучить Геомантию|r.|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa06", "field": "name", "expected": wts_updates[23143]})
    checks_def.append({"type": "unit", "id": "pa06", "field": "tip", "expected": wts_updates[35246]})
    checks_def.append({"type": "unit", "id": "pa06", "field": "ubertip", "expected": wts_updates[31749]})

    # pa04: Воин Нефритовой Стражи (E)
    wts_updates[15727] = "|cffe4cfa3Воин Нефритовой Стражи|r"
    wts_updates[35240] = "|cffe4cfa3Воин Нефритовой Стражи|r (|cffffffffE|r)"
    wts_updates[31732] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daТяжелый пехотинец храмовой стражи в зачарованных нефритовых латах.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deНефритовые Доспехи|cffced4da: поглощает значительную часть входящего урона от атак.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa04", "field": "name", "expected": wts_updates[15727]})
    checks_def.append({"type": "unit", "id": "pa04", "field": "tip", "expected": wts_updates[35240]})
    checks_def.append({"type": "unit", "id": "pa04", "field": "ubertip", "expected": wts_updates[31732]})

    # pa10: Стражник Нефритовых Врат (A)
    wts_updates[35299] = "|cffe4cfa3Стражник Нефритовых Врат|r"
    wts_updates[35258] = "|cffe4cfa3Стражник Нефритовых Врат|r (|cffffffffA|r)"
    wts_updates[31792] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daЭлитный страж священных рубежей, защищенный от вражеской магии и негативных эффектов.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deЗащита Ци|cffced4da: стойкость к негативным эффектам и магическая защита.|n"
        "- |cffa9c7deНефритовые Доспехи|cffced4da: поглощение входящего физического урона.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa10", "field": "name", "expected": wts_updates[35299]})
    checks_def.append({"type": "unit", "id": "pa10", "field": "tip", "expected": wts_updates[35258]})
    checks_def.append({"type": "unit", "id": "pa10", "field": "ubertip", "expected": wts_updates[31792]})

    # pa14: Орудийный Расчёт (Q)
    wts_updates[36629] = "|cffe4cfa3Орудийный Расчёт|r"
    wts_updates[35270] = "|cffe4cfa3Орудийный Расчёт|r (|cffffffffQ|r)"
    wts_updates[31869] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daДальнобойная пороховая артиллерия пандаренов. Сокрушает вражеские укрепления и скопления пехоты.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa14", "field": "name", "expected": wts_updates[36629]})
    checks_def.append({"type": "unit", "id": "pa14", "field": "tip", "expected": wts_updates[35270]})
    checks_def.append({"type": "unit", "id": "pa14", "field": "ubertip", "expected": wts_updates[31869]})

    # pa08: Мастер Огня (Q)
    wts_updates[23447] = "|cffe4cfa3Мастер Огня|r"
    wts_updates[35252] = "|cffe4cfa3Мастер Огня|r (|cffffffffQ|r)"
    wts_updates[31754] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМонах стихии огня, сжигающий вражеские ряды и взрывающий поверженных противников.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deОбжигающее Пламя Дракона|cffced4da: огненная аура, наносящая урон наземным врагам вокруг.|n"
        "- |cffa9c7deИспепеление|cffced4da: нарастающий урон от атак и мощный взрыв цели при гибели.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa08", "field": "name", "expected": wts_updates[23447]})
    checks_def.append({"type": "unit", "id": "pa08", "field": "tip", "expected": wts_updates[35252]})
    checks_def.append({"type": "unit", "id": "pa08", "field": "ubertip", "expected": wts_updates[31754]})

    # pa07: Мастер Земли (E)
    wts_updates[23409] = "|cffe4cfa3Мастер Земли|r"
    wts_updates[35249] = "|cffe4cfa3Мастер Земли|r (|cffffffffE|r)"
    wts_updates[31750] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daСтойкий монах стихии земли, обладающий сокрушительными рассекающими ударами.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deУдар Гнева Земли|cffced4da: рассекающие удары, наносящие урон окружающим врагам.|n"
        "- |cffa9c7deНефритовые Доспехи|cffced4da: поглощение входящего физического урона.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa07", "field": "name", "expected": wts_updates[23409]})
    checks_def.append({"type": "unit", "id": "pa07", "field": "tip", "expected": wts_updates[35249]})
    checks_def.append({"type": "unit", "id": "pa07", "field": "ubertip", "expected": wts_updates[31750]})

    # pa13: Мастер Бури (W)
    wts_updates[36628] = "|cffe4cfa3Мастер Бури|r"
    wts_updates[35267] = "|cffe4cfa3Мастер Бури|r (|cffffffffW|r)"
    wts_updates[31819] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daПовелитель шторма и молний. Поражает врагов электрическими разрядами и поднимает цели в вихрь.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deРаздвоенная молния|cffced4da: поражает до 4 противников электрическим конусом.|n"
        "- |cffa9c7deТорнадо|cffced4da: подбрасывает врага в воздух, выводя из боя.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa13", "field": "name", "expected": wts_updates[36628]})
    checks_def.append({"type": "unit", "id": "pa13", "field": "tip", "expected": wts_updates[35267]})
    checks_def.append({"type": "unit", "id": "pa13", "field": "ubertip", "expected": wts_updates[31819]})

    # pa29: Монах Инь (W)
    wts_updates[30611] = "|cffe4cfa3Монах Инь|r"
    wts_updates[30612] = "|cffe4cfa3Монах Инь|r (|cffffffffW|r)"
    wts_updates[33310] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМонах поддержки, следующий темному пути равновесия. Рассеивает заклинания и исцеляет соратников.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deИсцеление|cffced4da: восстанавливает здоровье находящимся рядом союзникам.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает чары в области и наносит урон призванным существам.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa29", "field": "name", "expected": wts_updates[30611]})
    checks_def.append({"type": "unit", "id": "pa29", "field": "tip", "expected": wts_updates[30612]})
    checks_def.append({"type": "unit", "id": "pa29", "field": "ubertip", "expected": wts_updates[33310]})

    # pa38: Монах Ян (Q)
    wts_updates[36631] = "|cffe4cfa3Монах Ян|r"
    wts_updates[35275] = "|cffe4cfa3Монах Ян|r (|cffffffffQ|r)"
    wts_updates[33322] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМонах поддержки, следующий светлому пути равновесия. Пробуждает ярость в союзниках и усиливает армию.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deЯрость|cffced4da: существенно ускоряет атаку и перемещение выбранного союзника.|n"
        "- |cffa9c7deПризыв к Балансу|cffced4da: повышает урон и броню находящихся рядом соратников.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa38", "field": "name", "expected": wts_updates[36631]})
    checks_def.append({"type": "unit", "id": "pa38", "field": "tip", "expected": wts_updates[35275]})
    checks_def.append({"type": "unit", "id": "pa38", "field": "ubertip", "expected": wts_updates[33322]})

    # pa09: Мастер Пьяной Лапы (R)
    wts_updates[23448] = "|cffe4cfa3Мастер Пьяной Лапы|r"
    wts_updates[35255] = "|cffe4cfa3Мастер Пьяной Лапы|r (|cffffffffR|r)"
    wts_updates[31791] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМастер непредсказуемого стиля пьяного кунг-фу. Оглушает врагов тяжелыми бочками и легко уклоняется от ударов.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deУдар Хмельной Бочки|cffced4da: шанс нанести дополнительный урон и оглушить цель.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa09", "field": "name", "expected": wts_updates[23448]})
    checks_def.append({"type": "unit", "id": "pa09", "field": "tip", "expected": wts_updates[35255]})
    checks_def.append({"type": "unit", "id": "pa09", "field": "ubertip", "expected": wts_updates[31791]})

    # pa35: Страж Храма (E)
    wts_updates[35244] = "|cffe4cfa3Страж Храма|r"
    wts_updates[35250] = "|cffe4cfa3Страж Храма|r (|cffffffffE|r)"
    wts_updates[33318] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daСвященный защитник храмов Пандарии. Оглушает врагов пламенными стрелами и ускоряет регенерацию маны армии.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n- |cffa9c7deОгненная стрела|cffced4da: наносит урон пламенем и оглушает цель.|n"
        "- |cffa9c7deАура Умиротворённости|cffced4da: ускоряет восстановление маны окружающих союзников.|n"
        "- |cffa9c7deЧувство баланса|cffced4da: шанс уклонения и критического урона.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "pa35", "field": "name", "expected": wts_updates[35244]})
    checks_def.append({"type": "unit", "id": "pa35", "field": "tip", "expected": wts_updates[35250]})
    checks_def.append({"type": "unit", "id": "pa35", "field": "ubertip", "expected": wts_updates[33318]})

    # =========================================================================
    # 5. UPGRADES (24 upgrades)
    # =========================================================================
    # PA10: Длинные Луки (X)
    wts_updates[42410] = "|cffe4cfa3Длинные Луки|r"
    wts_updates[42450] = "|cffe4cfa3Длинные Луки — уровень 1|r (|cffffffffX|r)"
    wts_updates[22964] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает дальность атаки Лучников Пандаренов на |cffc8e08725|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deЛучник Пандаренов|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r"
    )
    wts_updates[42452] = "|cffe4cfa3Длинные Луки|r"
    wts_updates[42451] = "|cffe4cfa3Длинные Луки — уровень 2|r (|cffffffffX|r)"
    wts_updates[23454] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает дальность атаки Лучников Пандаренов на |cffc8e08750|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deЛучник Пандаренов|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r"
    )

    # PA12: Укрепление Духа (B)
    wts_updates[42014] = "|cffe4cfa3Укрепление Духа|r"
    wts_updates[3805] = "|cffe4cfa3Укрепление Духа|r (|cffffffffB|r)"
    wts_updates[42015] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДарует пандаренам бонус |cffc8e087+125 к здоровью|cffced4da и |cffc8e087+10 к урону|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- Войскам ближнего боя пандаренов.|r"
    )

    # PA14: Защита Ци (Z)
    wts_updates[42016] = "|cffe4cfa3Защита Ци|r"
    wts_updates[23126] = "|cffe4cfa3Защита Ци|r (|cffffffffZ|r)"
    wts_updates[3127] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daПовышает регенерацию здоровья Стражников Нефритовых Врат и наделяет их невосприимчивостью к заклинаниям.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deСтражник Нефритовых Врат|cffced4da.|r"
    )

    # PA80: Доспехи из кожи (S) (уровни 1–6)
    leather_names = [
        "Доспехи из кожи", "Доспехи из клёпаной кожи", "Доспехи из армированной кожи",
        "Доспехи из драконьей кожи", "Доспехи из бамбука", "Нефритовые доспехи стрелков"
    ]
    pa80_name_sids = [22667, 25036, 31788, 31797, 35579, 35591]
    pa80_tip_sids = [35592, 35930, 36607, 36608, 36609, 36610]
    pa80_ub_sids = [36611, 36618, 36649, 25033, 22704, 25034]
    for lvl in range(1, 7):
        wts_updates[pa80_name_sids[lvl-1]] = f"|cffe4cfa3{leather_names[lvl-1]}|r"
        wts_updates[pa80_tip_sids[lvl-1]] = f"|cffe4cfa3{leather_names[lvl-1]} — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[pa80_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daПовышает броню воинов дальнего боя армии пандаренов на |cffc8e087+{lvl}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deЛучник Пандаренов|cffced4da|n"
            "- |cffa9c7deМастер Бури|cffced4da|n"
            "- |cffa9c7deОрудийный Расчёт|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r"
        )

    # PA81: Железные Мечи (Q) (уровни 1–6)
    sword_names = [
        "Железные Мечи", "Стальные мечи", "Мифриловые мечи",
        "Серебряные Мечи", "Вольфрамовые Мечи", "Нефритовые Мечи"
    ]
    pa81_name_sids = [41954, 41958, 41959, 41955, 41956, 41957]
    for lvl in range(1, 7):
        wts_updates[pa81_name_sids[lvl-1]] = f"|cffe4cfa3{sword_names[lvl-1]}|r"
    # L4..L6 have tip and ubertip sids in WTS
    wts_updates[35454] = "|cffe4cfa3Серебряные Мечи — уровень 4|r (|cffffffffQ|r)"
    wts_updates[35450] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daПовышает урон воинов ближнего боя армии пандаренов на |cffc8e087+4|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deВоин Пандаренов|cffced4da|n"
        "- |cffa9c7deВоин Нефритовой Стражи|cffced4da|n"
        "- |cffa9c7deВсадник Пандарен|cffced4da|n"
        "- |cffa9c7deМастер Геомант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff4/6|r"
    )
    wts_updates[35458] = "|cffe4cfa3Вольфрамовые Мечи — уровень 5|r (|cffffffffQ|r)"
    wts_updates[35451] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daПовышает урон воинов ближнего боя армии пандаренов на |cffc8e087+5|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deВоин Пандаренов|cffced4da|n"
        "- |cffa9c7deВоин Нефритовой Стражи|cffced4da|n"
        "- |cffa9c7deВсадник Пандарен|cffced4da|n"
        "- |cffa9c7deМастер Геомант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff5/6|r"
    )
    wts_updates[35457] = "|cffe4cfa3Нефритовые Мечи — уровень 6|r (|cffffffffQ|r)"
    wts_updates[35452] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daПовышает урон воинов ближнего боя армии пандаренов на |cffc8e087+6|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deВоин Пандаренов|cffced4da|n"
        "- |cffa9c7deВоин Нефритовой Стражи|cffced4da|n"
        "- |cffa9c7deВсадник Пандарен|cffced4da|n"
        "- |cffa9c7deМастер Геомант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff6/6|r"
    )

    # PA82: Изучение Хмелеварения (Z)
    wts_updates[41960] = "|cffe4cfa3Изучение Хмелеварения|r"
    wts_updates[35464] = "|cffe4cfa3Изучение Хмелеварения|r (|cffffffffZ|r)"
    wts_updates[3119] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daОткрывает найм элитных Хмелеваров в Палатах мастеров.|n|n"
        "|cffe6c07bВнимание:|r |cffe69a8dЗапрещает найм Мастеров Геомантов.|r|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deПалаты мастеров|cffced4da.|r"
    )

    # PA83: Изучить Геомантию (X)
    wts_updates[41961] = "|cffe4cfa3Изучить Геомантию|r"
    wts_updates[35465] = "|cffe4cfa3Изучить Геомантию|r (|cffffffffX|r)"
    wts_updates[3120] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daОткрывает найм Мастеров Геомантов в Палатах мастеров.|n|n"
        "|cffe6c07bВнимание:|r |cffe69a8dЗапрещает найм Хмелеваров.|r|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deПалаты мастеров|cffced4da.|r"
    )

    # PA84: Железная Броня (A) (уровни 1–6)
    pa84_name_sids = [42411, 42415, 42416, 42417, 42418, 42419]
    pa84_tip_sids = [38233, 38451, 40270, 36661, 40427, 42371]
    pa84_ub_sids = [42425, 42426, 42427, 42412, 42413, 42414]
    for lvl in range(1, 7):
        wts_updates[pa84_name_sids[lvl-1]] = "|cffe4cfa3Железная Броня|r"
        wts_updates[pa84_tip_sids[lvl-1]] = f"|cffe4cfa3Железная Броня — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[pa84_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daПовышает броню воинов ближнего боя армии пандаренов на |cffc8e087+{lvl}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deВоин Пандаренов|cffced4da|n"
            "- |cffa9c7deВоин Нефритовой Стражи|cffced4da|n"
            "- |cffa9c7deВсадник Пандарен|cffced4da|n"
            "- |cffa9c7deМастер Земли|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r"
        )

    # PA85: Нефритовые Доспехи (Z)
    wts_updates[41968] = "|cffe4cfa3Нефритовые Доспехи|r"
    wts_updates[41969] = "|cffe4cfa3Нефритовые Доспехи|r (|cffffffffZ|r)"
    wts_updates[35491] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daСнабжает Воинов Нефритовой Стражи тяжелыми доспехами, снижающими получаемый от атак урон на |cffc8e08718|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deВоин Нефритовой Стражи|cffced4da.|r"
    )

    # PA86: Посвящение Мастеров Бури (W) (уровни 1, 2)
    wts_updates[41970] = "|cffe4cfa3Посвящение Мастеров Бури|r"
    wts_updates[41972] = "|cffe4cfa3Посвящение Мастеров Бури — адепты|r (|cffffffffW|r)"
    wts_updates[19840] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает запас здоровья Мастеров Бури на |cffc8e08740|cffced4da, маны на |cffc8e087100|cffced4da и ускоряет регенерацию маны.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Бури|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r"
    )
    wts_updates[41971] = "|cffe4cfa3Посвящение Мастеров Бури|r"
    wts_updates[41973] = "|cffe4cfa3Посвящение Мастеров Бури — мастера|r (|cffffffffW|r)"
    wts_updates[20775] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает здоровье Мастеров Бури на |cffc8e08775|cffced4da, ману на |cffc8e087150|cffced4da и регенерацию маны.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Бури|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r"
    )

    # PA87: Посвящение Мастеров Земли (E) (уровни 1, 2)
    wts_updates[41974] = "|cffe4cfa3Посвящение Мастеров Земли|r"
    wts_updates[41976] = "|cffe4cfa3Посвящение Мастеров Земли — адепты|r (|cffffffffE|r)"
    wts_updates[22726] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает запас здоровья Мастеров Земли на |cffc8e087100|cffced4da ед. и наделяет их невосприимчивостью к заклинаниям.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Земли|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r"
    )
    wts_updates[41975] = "|cffe4cfa3Посвящение Мастеров Земли|r"
    wts_updates[41977] = "|cffe4cfa3Посвящение Мастеров Земли — мастера|r (|cffffffffE|r)"
    wts_updates[22749] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает запас здоровья Мастеров Земли на |cffc8e087125|cffced4da ед. и закрепляет невосприимчивость к магии.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Земли|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r"
    )

    # PA88: Посвящение Мастеров Огня (Q) (уровни 1, 2)
    wts_updates[41978] = "|cffe4cfa3Посвящение Мастеров Огня|r"
    wts_updates[41979] = "|cffe4cfa3Посвящение Мастеров Огня — адепты|r (|cffffffffQ|r)"
    wts_updates[22893] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает урон от атак Мастеров Огня на |cffc8e08710|cffced4da и запас их здоровья на |cffc8e08730|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Огня|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r"
    )
    wts_updates[41980] = "|cffe4cfa3Посвящение Мастеров Огня|r"
    wts_updates[41981] = "|cffe4cfa3Посвящение Мастеров Огня — мастера|r (|cffffffffQ|r)"
    wts_updates[22907] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает урон Мастеров Огня на |cffc8e08715|cffced4da и запас здоровья на |cffc8e08755|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Огня|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r"
    )

    # PA89: Посвящение Монахов Ян в адепты (S) (уровни 1, 2)
    wts_updates[41982] = "|cffe4cfa3Посвящение Монахов Ян|r"
    wts_updates[41984] = "|cffe4cfa3Посвящение Монахов Ян — адепты|r (|cffffffffS|r)"
    wts_updates[2875] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает запас здоровья, маны и регенерацию маны Монахов Ян, а также обучает способности |cffa9c7de«Ярость»|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМонах Ян|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r"
    )
    wts_updates[41983] = "|cffe4cfa3Посвящение Монахов Ян|r"
    wts_updates[41985] = "|cffe4cfa3Посвящение Монахов Ян — мастера|r (|cffffffffS|r)"
    wts_updates[2883] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает запас здоровья, маны и регенерацию маны Монахов Ян.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМонах Ян|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r"
    )

    # PA90: Сделать Геомантов Адептами (C) (уровни 1–3)
    wts_updates[41986] = "|cffe4cfa3Посвящение Геомантов|r"
    wts_updates[35521] = "|cffe4cfa3Посвящение Геомантов — ученики|r (|cffffffffC|r)"
    wts_updates[3121] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает урон, скорость атаки и здоровье Мастеров Геомантов.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Геомант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/3|r"
    )
    wts_updates[41987] = "|cffe4cfa3Посвящение Геомантов|r"
    wts_updates[35522] = "|cffe4cfa3Посвящение Геомантов — адепты|r (|cffffffffC|r)"
    wts_updates[3122] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает урон, скорость атаки и здоровье Мастеров Геомантов.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Геомант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/3|r"
    )
    wts_updates[41988] = "|cffe4cfa3Посвящение Геомантов|r"
    wts_updates[35523] = "|cffe4cfa3Посвящение Геомантов — мастера|r (|cffffffffC|r)"
    wts_updates[3123] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно повышает боевые параметры и обучает Мастеров Геомантов заклинанию |cffa9c7de«Энергия Ци»|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Геомант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3/3|r"
    )

    # PA91: Сделать Монахов Адептами (A) (уровни 1, 2)
    wts_updates[41989] = "|cffe4cfa3Посвящение Монахов Инь|r"
    wts_updates[41991] = "|cffe4cfa3Посвящение Монахов Инь — адепты|r (|cffffffffA|r)"
    wts_updates[35529] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает здоровье, ману, регенерацию маны Монахов Инь и обучает заклинанию |cffa9c7de«Рассеивание заклинаний»|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМонах Инь|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r"
    )
    wts_updates[41990] = "|cffe4cfa3Посвящение Монахов Инь|r"
    wts_updates[41992] = "|cffe4cfa3Посвящение Монахов Инь — мастера|r (|cffffffffA|r)"
    wts_updates[35530] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает здоровье, ману и регенерацию маны Монахов Инь, усиливая заклинание |cffa9c7de«Исцеление»|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМонах Инь|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r"
    )

    # PA92: Сделать Хмелеваров учениками (X) (уровни 1–3)
    wts_updates[41993] = "|cffe4cfa3Посвящение Хмелеваров|r"
    wts_updates[41995] = "|cffe4cfa3Посвящение Хмелеваров — ученики|r (|cffffffffX|r)"
    wts_updates[3124] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает запас здоровья на |cffc8e087100|cffced4da, маны на |cffc8e087150|cffced4da Хмелеваров и наделяет их невосприимчивостью к магии.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deХмелевар|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/3|r"
    )
    wts_updates[41994] = "|cffe4cfa3Посвящение Хмелеваров|r"
    wts_updates[41996] = "|cffe4cfa3Посвящение Хмелеваров — адепты|r (|cffffffffX|r)"
    wts_updates[3125] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает здоровье на |cffc8e087125|cffced4da, ману на |cffc8e087150|cffced4da Хмелеваров и усиливает их способности.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deХмелевар|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/3|r"
    )
    wts_updates[41997] = "|cffe4cfa3Посвящение Хмелеваров|r"
    wts_updates[41998] = "|cffe4cfa3Посвящение Хмелеваров — мастера|r (|cffffffffX|r)"
    wts_updates[3126] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно повышает боевые параметры Хмелеваров и доводит их хмельное мастерство до совершенства.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deХмелевар|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3/3|r"
    )

    # PA93: Стальные Наконечники (W) (уровни 1–6)
    arrow_names = [
        "Стальные Наконечники", "Железные Наконечники", "Мифриловые Наконечники",
        "Вольфрамовые Наконечники", "Серебряные Наконечники", "Нефритовые Наконечники"
    ]
    pa93_name_sids = [41999, 42000, 42001, 42002, 42003, 42004]
    pa93_tip_sids = [35543, 35710, 35549, 35717, 35718, 35719]
    pa93_ub_sids = [35766, 35767, 35768, 35711, 35712, 35713]
    for lvl in range(1, 7):
        wts_updates[pa93_name_sids[lvl-1]] = f"|cffe4cfa3{arrow_names[lvl-1]}|r"
        wts_updates[pa93_tip_sids[lvl-1]] = f"|cffe4cfa3{arrow_names[lvl-1]} — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[pa93_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daПовышает урон воинов дальнего боя армии пандаренов на |cffc8e087+{lvl}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deЛучник Пандаренов|cffced4da|n"
            "- |cffa9c7deМастер Бури|cffced4da|n"
            "- |cffa9c7deОрудийный Расчёт|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r"
        )

    # PA94: Улучшенные топоры (Z) (уровни 1–6)
    pa94_name_sids = [42436, 42437, 42428, 42429, 42430, 42431]
    pa94_tip_sids = [42438, 42439, 42432, 42433, 42434, 42435]
    for lvl in range(1, 7):
        wts_updates[pa94_name_sids[lvl-1]] = "|cffe4cfa3Улучшенные топоры|r"
        wts_updates[pa94_tip_sids[lvl-1]] = f"|cffe4cfa3Улучшенные топоры — уровень {lvl}|r (|cffffffffZ|r)"
    # Levels 3..6 have ubertip sids in WTS
    pa94_ub_sids_part = [(3, 35554), (4, 35555), (5, 35556), (6, 35557)]
    for lvl, sid in pa94_ub_sids_part:
        wts_updates[sid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает объём древесины, переносимой Рабочими Пандаренов, на |cffc8e087+8|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deРабочий Пандаренов|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r"
        )

    # PA95: Утяжелённая Рукоять (X)
    wts_updates[42011] = "|cffe4cfa3Утяжелённая Рукоять|r"
    wts_updates[35568] = "|cffe4cfa3Утяжелённая Рукоять|r (|cffffffffX|r)"
    wts_updates[35569] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУтяжеляет оружие Воинов Нефритовой Стражи, увеличивая их урон на |cffc8e087+8|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deВоин Нефритовой Стражи|cffced4da.|r"
    )

    # pa16: Усиление Мастеров Огня (Q)
    wts_updates[42022] = "|cffe4cfa3Усиление Мастеров Огня|r"
    wts_updates[2927] = "|cffe4cfa3Усиление Мастеров Огня|r (|cffffffffQ|r)"
    wts_updates[38751] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daВозвращает Мастерам Огня истинную мощь пламени, повышая их здоровье на |cffc8e087+200|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Огня|cffced4da.|r"
    )

    # pa21: Дрессировка Животных (C)
    wts_updates[42453] = "|cffe4cfa3Дрессировка Животных|r"
    wts_updates[42455] = "|cffe4cfa3Дрессировка Животных|r (|cffffffffC|r)"
    wts_updates[42454] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДарует Всадникам Пандаренам |cffc8e087+150 к здоровью|cffced4da и |cffc8e087+10% к скорости передвижения|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deВсадник Пандарен|cffced4da.|r"
    )

    # pa39: Секреты Древних Мастеров (D) (уровни 1, 2)
    wts_updates[42018] = "|cffe4cfa3Секреты Древних Мастеров|r"
    wts_updates[42020] = "|cffe4cfa3Секреты Древних Мастеров — адепты|r (|cffffffffD|r)"
    wts_updates[36866] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daУвеличивает запас здоровья, урон и регенерацию маны Стражей Храма, а также наделяет их |cffa9c7de«Аурой Умиротворённости»|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deСтраж Храма|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r"
    )
    wts_updates[42019] = "|cffe4cfa3Секреты Древних Мастеров|r"
    wts_updates[42021] = "|cffe4cfa3Секреты Древних Мастеров — мастера|r (|cffffffffD|r)"
    wts_updates[36867] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daДополнительно увеличивает здоровье, урон и усиливает восстанавливающую ману ауру Стражей Храма.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deСтраж Храма|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r"
    )

    # pa47: Усиление Мастеров Земли (R)
    wts_updates[42023] = "|cffe4cfa3Усиление Мастеров Земли|r"
    wts_updates[3116] = "|cffe4cfa3Усиление Мастеров Земли|r (|cffffffffR|r)"
    wts_updates[3117] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|r |cffced4daНаделяет Мастеров Земли несокрушимой монолитной стойкостью, повышая здоровье на |cffc8e087+400|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|r|cffced4da|n- |cffa9c7deМастер Земли|cffced4da.|r"
    )

    # =========================================================================
    # 6. ABILITIES (37 abilities)
    # =========================================================================
    # A1I7: Сытые и довольные
    wts_updates[35480] = "|cffe4cfa3Сытые и довольные|r"
    wts_updates[35578] = "|cffe4cfa3Сытые и довольные|r"
    wts_updates[25601] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная расовая способность пандаренов. Чем больше построено ферм и рыбацких домов, тем выше шанс, что новые воины выйдут из казарм с увеличенным запасом здоровья.|r"
    )

    # A1RB: Исцеление (Q)
    wts_updates[42010] = "|cffe4cfa3Исцеление|r"
    wts_updates[42009] = "|cffe4cfa3Исцеление|r (|cffffffffQ|r)"
    wts_updates[42236] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВосполняет |cffffffff5|cffced4da ед. здоровья находящимся рядом раненым союзникам (до |cffffffff8|cffced4da целей).|n|n"
        "Расход маны: |cffffffff2|cffced4da ед. Перезарядка: |cffffffff1|cffced4da сек.|r"
    )

    # PA02: Единение с Инь (R)
    wts_updates[35484] = "|cffe4cfa3Единение с Инь|r"
    wts_updates[35925] = "|cffe4cfa3Единение с Инь|r (|cffffffffR|r)"
    wts_updates[35926] = "|cffe4cfa3Единение с Инь|r (|cffffffffR|r)"

    # PA03: Веер Клинков (Q)
    wts_updates[35485] = "|cffe4cfa3Веер Клинков|r"
    wts_updates[35575] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВыпускает веер кинжалов во всех направлениях, нанося по |cffffffff95|cffced4da ед. урона окружающим врагам.|n|n"
        "Расход маны: |cffffffff100|cffced4da ед. Перезарядка: |cffffffff12|cffced4da сек.|r"
    )
    wts_updates[35705] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВыпускает веер кинжалов во всех направлениях, нанося по |cffffffff145|cffced4da ед. урона окружающим врагам.|n|n"
        "Расход маны: |cffffffff90|cffced4da ед. Перезарядка: |cffffffff10|cffced4da сек.|r"
    )
    wts_updates[35706] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВыпускает веер кинжалов во всех направлениях, нанося по |cffffffff210|cffced4da ед. урона окружающим врагам.|n|n"
        "Расход маны: |cffffffff85|cffced4da ед. Перезарядка: |cffffffff8|cffced4da сек.|r"
    )
    wts_updates[35383] = "|cffe4cfa3Веер Клинков — уровень 4|r (|cffffffffQ|r)"
    wts_updates[35385] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВыпускает веер кинжалов во всех направлениях, нанося по |cffffffff240|cffced4da ед. урона окружающим врагам.|n|n"
        "Расход маны: |cffffffff65|cffced4da ед. Перезарядка: |cffffffff6|cffced4da сек.|r"
    )

    # PA05: Удары Ци
    wts_updates[35486] = "|cffe4cfa3Удары Ци|r"
    wts_updates[35929] = "|cffe4cfa3Удары Ци|r"
    wts_updates[35931] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная способность. Каждая атака Мастера Геоманта сжигает |cffffffff30|cffced4da ед. маны цели и наносит дополнительный урон.|r"
    )

    # PA13: Защита Ци
    wts_updates[35487] = "|cffe4cfa3Защита Ци|r"
    wts_updates[3765] = "|cffe4cfa3Защита Ци|r"

    # PA15: Воодушевляющее Присутствие
    wts_updates[36665] = "|cffe4cfa3Воодушевляющее Присутствие|r"
    wts_updates[38450] = "|cffe4cfa3Воодушевляющее Присутствие|r"
    wts_updates[23367] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура Лидера Шадо-Пан, вдохновляющая окружающие войска и повышающая их силу атаки на |cffc8e0877%–28%|cffced4da.|r"
    )
    wts_updates[23131] = "|cffe4cfa3Воодушевляющее Присутствие — уровень 1|r"
    wts_updates[40273] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура. Вдохновляет находящихся рядом союзных воинов, увеличивая их атаку на |cffc8e0877%|cffced4da.|r"
    )
    wts_updates[23132] = "|cffe4cfa3Воодушевляющее Присутствие — уровень 2|r"
    wts_updates[40278] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура. Вдохновляет находящихся рядом союзных воинов, увеличивая их атаку на |cffc8e08714%|cffced4da.|r"
    )
    wts_updates[23145] = "|cffe4cfa3Воодушевляющее Присутствие — уровень 3|r"
    wts_updates[40277] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура. Вдохновляет находящихся рядом союзных воинов, увеличивая их атаку на |cffc8e08721%|cffced4da.|r"
    )
    wts_updates[23146] = "|cffe4cfa3Воодушевляющее Присутствие — уровень 4|r"
    wts_updates[40279] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура. Вдохновляет находящихся рядом союзных воинов, увеличивая их атаку на |cffc8e08728%|cffced4da.|r"
    )

    # PA16: Энергия Ци (Q)
    wts_updates[40295] = "|cffe4cfa3Энергия Ци|r"
    wts_updates[32280] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daСоздает целительную волну энергии, восстанавливающую здоровье союзников последовательными скачками.|r"
    )
    wts_updates[28016] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daСоздает волну энергии, восстанавливающую |cffffffff45|cffced4da ед. здоровья первой цели и исцеляющую до |cffffffff6|cffced4da союзников.|n|n"
        "Расход маны: |cffffffff90|cffced4da ед. Перезарядка: |cffffffff9|cffced4da сек.|r"
    )

    # PA20: Аура Умиротворённости (E)
    wts_updates[42409] = "|cffe4cfa3Аура Умиротворённости|r"
    wts_updates[36667] = "|cffe4cfa3Аура Умиротворённости — уровень 1|r (|cffffffffE|r)"
    wts_updates[35034] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура. Ускоряет регенерацию маны находящихся рядом союзников на |cffc8e087+1.75|cffced4da ед. в секунду.|r"
    )
    wts_updates[36666] = "|cffe4cfa3Аура Умиротворённости — уровень 2|r (|cffffffffE|r)"
    wts_updates[35904] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура. Ускоряет регенерацию маны находящихся рядом союзников на |cffc8e087+3.5|cffced4da ед. в секунду.|r"
    )

    # PA45: Нефритовые Доспехи (K)
    wts_updates[9143] = "|cffe4cfa3Нефритовые Доспехи|r"
    wts_updates[9507] = "|cffe4cfa3Нефритовые Доспехи|r"
    wts_updates[9506] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная способность. Защитные зачарованные пластины снижают получаемый урон от вражеских атак на |cffffffff18|cffced4da ед. (минимальный урон |cffffffff2|cffced4da).|r"
    )

    # PA46: Рассеивание заклинаний (D)
    wts_updates[12384] = "|cffe4cfa3Рассеивание заклинаний|r"

    # PA50: Удар Восходящего Солнца (Q)
    wts_updates[21395] = "|cffe4cfa3Удар Восходящего Солнца|r"
    wts_updates[35347] = "|cffe4cfa3Удар Восходящего Солнца|r"
    wts_updates[35348] = "|cffe4cfa3Удар Восходящего Солнца — уровень 1|r (|cffffffffQ|r)"
    wts_updates[35349] = "|cffe4cfa3Удар Восходящего Солнца — уровень 2|r (|cffffffffQ|r)"
    wts_updates[35350] = "|cffe4cfa3Удар Восходящего Солнца — уровень 3|r (|cffffffffQ|r)"
    wts_updates[35351] = "|cffe4cfa3Удар Восходящего Солнца — уровень 4|r (|cffffffffQ|r)"
    wts_updates[34328] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daБросает сокрушительный молот в цель, нанося |cffffffff450|cffced4da ед. урона и оглушая противника на |cffffffff6|cffced4da сек. (|cffffffff3|cffced4da сек. героев).|n|n"
        "Расход маны: |cffffffff75|cffced4da ед. Перезарядка: |cffffffff12|cffced4da сек.|r"
    )

    # PA51: Выдержка Монастыря Земли (E)
    wts_updates[21427] = "|cffe4cfa3Выдержка Монастыря Земли|r"
    wts_updates[34335] = "|cffe4cfa3Выдержка Монастыря Земли|r"
    wts_updates[30676] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная стойкость монастыря Земли, поглощающая от |cffffffff12|cffced4da до |cffffffff30|cffced4da ед. входящего урона от атак.|r"
    )
    wts_updates[12317] = "|cffe4cfa3Выдержка Монастыря Земли — уровень 1|r"
    wts_updates[15593] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daСнижает получаемый от вражеских атак урон на |cffffffff12|cffced4da ед. (минимальный урон |cffffffff1|cffced4da).|r"
    )
    wts_updates[14452] = "|cffe4cfa3Выдержка Монастыря Земли — уровень 2|r"
    wts_updates[15594] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daСнижает получаемый от вражеских атак урон на |cffffffff15|cffced4da ед. (минимальный урон |cffffffff1|cffced4da).|r"
    )
    wts_updates[15980] = "|cffe4cfa3Выдержка Монастыря Земли — уровень 3|r"
    wts_updates[16889] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daСнижает получаемый от вражеских атак урон на |cffffffff18|cffced4da ед. (минимальный урон |cffffffff1|cffced4da).|r"
    )
    wts_updates[21680] = "|cffe4cfa3Выдержка Монастыря Земли — уровень 4|r"
    wts_updates[20694] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daСнижает получаемый от вражеских атак урон на |cffffffff30|cffced4da ед. (минимальный урон |cffffffff1|cffced4da).|r"
    )

    # PA53: Ярость (W)
    wts_updates[21766] = "|cffe4cfa3Ярость|r"
    wts_updates[29754] = "|cffe4cfa3Ярость|r (|cffffffffW|r)"
    wts_updates[38745] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВводит выбранного союзника в состояние боевого ража, увеличивая скорость атаки на |cffc8e087+50%|cffced4da и скорость бега на |cffc8e087+35%|cffced4da на |cffffffff60|cffced4da сек.|n|n"
        "Расход маны: |cffffffff50|cffced4da ед. Перезарядка: |cffffffff1|cffced4da сек.|r"
    )

    # PA55: Буря Клинков (R)
    wts_updates[21924] = "|cffe4cfa3Буря Клинков|r"
    wts_updates[35369] = "|cffe4cfa3Буря Клинков|r (|cffffffffR|r)"
    wts_updates[35371] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daОсобая способность. Окружает героя вихрем клинков с иммунитетом к магии, наносящим |cffffffff180|cffced4da урона/сек. наземным врагам.|r"
    )
    wts_updates[35368] = "|cffe4cfa3Буря Клинков|r (|cffffffffR|r)"
    wts_updates[35372] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВращается в смертоносном вихре в течение |cffffffff7|cffced4da сек., получая невосприимчивость к магии и нанося по |cffffffff180|cffced4da урона в секунду наземным врагам.|n|n"
        "Расход маны: |cffffffff200|cffced4da ед. Перезарядка: |cffffffff120|cffced4da сек.|r"
    )

    # PA57: Танец Ветра (W)
    wts_updates[29964] = "|cffe4cfa3Танец Ветра|r"
    wts_updates[36742] = "|cffe4cfa3Танец Ветра — уровень 4|r (|cffffffffW|r)"
    wts_updates[36743] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daДарует невидимость и |cffc8e087+90% к скорости передвижения|cffced4da на |cffffffff60|cffced4da сек. Атака из невидимости наносит |cffffffff150|cffced4da бонусного урона.|n|n"
        "Расход маны: |cffffffff5|cffced4da ед. Перезарядка: |cffffffff7|cffced4da сек.|r"
    )

    # PA59: Техника Тысячи Порезов (E)
    wts_updates[35264] = "|cffe4cfa3Техника Тысячи Порезов|r"
    wts_updates[35388] = "|cffe4cfa3Техника Тысячи Порезов|r"
    wts_updates[35391] = "|cffe4cfa3Техника Тысячи Порезов — уровень 1|r"
    wts_updates[39183] = "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная способность. Дает |cffffffff15%|cffced4da шанс нанести |cffffffff2-кратный|cffced4da критический урон при атаке.|r"
    wts_updates[35392] = "|cffe4cfa3Техника Тысячи Порезов — уровень 2|r"
    wts_updates[39184] = "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная способность. Дает |cffffffff15%|cffced4da шанс нанести |cffffffff3-кратный|cffced4da критический урон при атаке.|r"
    wts_updates[35393] = "|cffe4cfa3Техника Тысячи Порезов — уровень 3|r"
    wts_updates[39185] = "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная способность. Дает |cffffffff15%|cffced4da шанс нанести |cffffffff4-кратный|cffced4da критический урон при атаке.|r"
    wts_updates[35394] = "|cffe4cfa3Техника Тысячи Порезов — уровень 4|r"
    wts_updates[39182] = "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная способность. Дает |cffffffff15%|cffced4da шанс нанести |cffffffff5-кратный|cffced4da критический урон при атаке.|r"

    # PA60: Цепная молния (W)
    wts_updates[35400] = "|cffe4cfa3Цепная молния|r"
    wts_updates[35396] = "|cffe4cfa3Цепная молния — уровень 4|r (|cffffffffW|r)"
    wts_updates[36745] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПоражает цель молнией на |cffffffff400|cffced4da ед. урона, перескакивающей до |cffffffff15|cffced4da врагов с потерей |cffffffff5%|cffced4da мощности за скачок.|n|n"
        "Расход маны: |cffffffff85|cffced4da ед. Перезарядка: |cffffffff9|cffced4da сек.|r"
    )

    # PA61: Багманское пиво
    wts_updates[35401] = "|cffe4cfa3Багманское пиво|r"
    wts_updates[42402] = "|cffe4cfa3Багманское пиво|r"
    wts_updates[42404] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАура. Хмельной дух ускоряет перемещение союзников на |cffc8e087+15%|cffced4da и повышает скорость регенерации их здоровья на |cffc8e087+50%|cffced4da.|r"
    )

    # PA62: Грозовые Стрелы (Q)
    wts_updates[42405] = "|cffe4cfa3Грозовые Стрелы|r"
    wts_updates[35404] = "|cffe4cfa3Грозовые Стрелы|r"
    wts_updates[35405] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daЗаряжает стрелы лучников силой грозы, добавляя к выстрелам урон от молний.|r"
    )
    wts_updates[42406] = "|cffe4cfa3Грозовые Стрелы|r (|cffffffffQ|r)"
    wts_updates[42407] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daАвтокаст. Добавляет |cffffffff5|cffced4da ед. урона от бури к каждой атаке.|n|n"
        "Расход маны: |cffffffff4|cffced4da ед. за выстрел.|r"
    )

    # PA63: Обжигающее Пламя Дракона (W)
    wts_updates[35402] = "|cffe4cfa3Обжигающее Пламя Дракона|r"
    wts_updates[35408] = "|cffe4cfa3Обжигающее Пламя Дракона|r (|cffffffffW|r)"
    wts_updates[38747] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВключаемая аура. Окружает Мастера Огня языками пламени, наносящими |cffffffff15|cffced4da ед. урона каждые |cffffffff0.5|cffced4da сек. наземным врагам поблизости.|n|n"
        "Расход маны: |cffffffff10|cffced4da ед./сек.|r"
    )

    # PA65: Призыв к Балансу (Q)
    wts_updates[35406] = "|cffe4cfa3Призыв к Балансу|r"
    wts_updates[23129] = "|cffe4cfa3Призыв к Балансу|r (|cffffffffQ|r)"
    wts_updates[38748] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВоодушевляет соратников, повышая урон на |cffc8e087+15%|cffced4da и броню на |cffc8e087+4|cffced4da ед. на |cffffffff45|cffced4da сек.|n|n"
        "Расход маны: |cffffffff100|cffced4da ед.|r"
    )

    # PA66: Испепеление (C)
    wts_updates[22591] = "|cffe4cfa3Испепеление|r"
    wts_updates[22597] = "|cffe4cfa3Испепеление|r"

    # PA67: Пламенное дыхание 1 (Q)
    wts_updates[35413] = "|cffe4cfa3Пламенное дыхание|r"

    # PA68: Чувство баланса
    wts_updates[22657] = "|cffe4cfa3Чувство баланса|r"
    wts_updates[22659] = "|cffe4cfa3Чувство баланса|r"
    wts_updates[22665] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная расовая ловкость. Дает |cffffffff7%|cffced4da шанс уклониться от вражеской атаки и |cffffffff10%|cffced4da шанс нанести на |cffc8e08720%|cffced4da больше урона.|r"
    )

    # PA69: Удар Гнева Земли
    wts_updates[35415] = "|cffe4cfa3Удар Гнева Земли|r"
    wts_updates[5769] = "|cffe4cfa3Удар Гнева Земли|r"
    wts_updates[5768] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивные рассекающие удары. Атаки наносят |cffffffff5%|cffced4da урона по площади всем врагам рядом с основной целью.|r"
    )

    # PA70: Хмельные Пары (W)
    wts_updates[35416] = "|cffe4cfa3Хмельные Пары|r"

    # PA73: Раздвоенная молния (Q)
    wts_updates[35418] = "|cffe4cfa3Раздвоенная молния|r"
    wts_updates[3808] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВыпускает конус молний перед собой, поражая до |cffffffff4|cffced4da врагов и нанося по |cffffffff125|cffced4da ед. урона.|n|n"
        "Расход маны: |cffffffff50|cffced4da ед. Перезарядка: |cffffffff11|cffced4da сек.|r"
    )

    # PA74: Удар Хмельной Бочки
    wts_updates[35472] = "|cffe4cfa3Удар Хмельной Бочки|r"
    wts_updates[39157] = "|cffe4cfa3Удар Хмельной Бочки|r"
    wts_updates[35471] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПассивная способность. Атаки с |cffffffff15%|cffced4da вероятностью наносят |cffffffff+15|cffced4da ед. бонусного урона и оглушают цель на |cffffffff2|cffced4da сек.|r"
    )

    # PA75: Катаклизм (R)
    wts_updates[35473] = "|cffe4cfa3Катаклизм|r"
    wts_updates[35421] = "|cffe4cfa3Катаклизм|r (|cffffffffR|r)"
    wts_updates[35422] = "|cffe4cfa3Катаклизм — уровень 1|r (|cffffffffR|r)"
    wts_updates[34611] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПризывает бурю молний в указанную область на |cffffffff15|cffced4da сек., наносящую по |cffffffff25|cffced4da ед. урона врагам каждую секунду.|n|n"
        "Расход маны: |cffffffff200|cffced4da ед. Перезарядка: |cffffffff100|cffced4da сек.|r"
    )
    wts_updates[39160] = "|cffe4cfa3Катаклизм — уровень 2|r (|cffffffffR|r)"
    wts_updates[40315] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПризывает сокрушительную бурю молний на |cffffffff15|cffced4da сек., наносящую по |cffffffff35|cffced4da ед. урона врагам каждую секунду.|n|n"
        "Расход маны: |cffffffff300|cffced4da ед. Перезарядка: |cffffffff100|cffced4da сек.|r"
    )

    # PA76: Призыв Помощи (Q)
    wts_updates[35479] = "|cffe4cfa3Призыв Помощи|r"
    wts_updates[3967] = "|cffe4cfa3Призыв Помощи|r (|cffffffffQ|r)"
    wts_updates[4085] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daОткрывает пространственный портал, призывающий союзных воинов пандаренов на помощь герою.|r"
    )
    wts_updates[3955] = "|cffe4cfa3Призыв Помощи — уровень 1|r (|cffffffffQ|r)"
    wts_updates[38430] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daОткрывает портал и призывает воина пандаренов на помощь в бою.|n|n"
        "Перезарядка: |cffffffff60|cffced4da сек.|r"
    )
    wts_updates[36603] = "|cffe4cfa3Призыв Помощи — уровень 2|r (|cffffffffQ|r)"
    wts_updates[38439] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daОткрывает портал и призывает двух воинов Нефритовой Стражи на помощь в бою.|n|n"
        "Перезарядка: |cffffffff50|cffced4da сек.|r"
    )
    wts_updates[36604] = "|cffe4cfa3Призыв Помощи — уровень 3|r (|cffffffffQ|r)"
    wts_updates[38448] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daОткрывает портал и призывает трех стражников Нефритовых Врат на помощь в бою.|n|n"
        "Перезарядка: |cffffffff40|cffced4da сек.|r"
    )
    wts_updates[36605] = "|cffe4cfa3Призыв Помощи — уровень 4|r (|cffffffffQ|r)"
    wts_updates[38449] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daОткрывает портал и призывает отряд элитных стражей храма на помощь в бою.|n|n"
        "Перезарядка: |cffffffff30|cffced4da сек.|r"
    )

    # PA77: Пьяный Мастер
    wts_updates[35414] = "|cffe4cfa3Пьяный Мастер|r"

    # PA78: Провокация (W)
    wts_updates[6735] = "|cffe4cfa3Провокация|r"
    wts_updates[6789] = "|cffe4cfa3Провокация|r (|cffffffffW|r)"
    wts_updates[6790] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daЗаставляет врагов атаковать героя, снижая получаемый урон на |cffffffff10%|cffced4da и возвращая часть урона врагам в ближнем бою.|r"
    )
    wts_updates[6788] = "|cffe4cfa3Провокация — уровень 1|r (|cffffffffW|r)"
    wts_updates[6791] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВынуждает ближайших врагов атаковать героя. Снижает получаемый урон на |cffffffff10%|cffced4da на |cffffffff7|cffced4da сек. и возвращает |cffffffff5%|cffced4da ближнего урона атакующим.|n|n"
        "Перезарядка: |cffffffff20|cffced4da сек.|r"
    )
    wts_updates[6736] = "|cffe4cfa3Провокация — уровень 2|r (|cffffffffW|r)"
    wts_updates[6747] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВынуждает ближайших врагов атаковать героя. Снижает получаемый урон на |cffffffff10%|cffced4da на |cffffffff7|cffced4da сек. и возвращает |cffffffff10%|cffced4da ближнего урона атакующим.|n|n"
        "Перезарядка: |cffffffff18|cffced4da сек.|r"
    )
    wts_updates[6737] = "|cffe4cfa3Провокация — уровень 3|r (|cffffffffW|r)"
    wts_updates[6756] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВынуждает ближайших врагов атаковать героя. Снижает получаемый урон на |cffffffff10%|cffced4da на |cffffffff7|cffced4da сек. и возвращает |cffffffff20%|cffced4da ближнего урона атакующим.|n|n"
        "Перезарядка: |cffffffff16|cffced4da сек.|r"
    )
    wts_updates[6742] = "|cffe4cfa3Провокация — уровень 4|r (|cffffffffW|r)"
    wts_updates[6748] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВынуждает ближайших врагов атаковать героя. Снижает получаемый урон на |cffffffff10%|cffced4da на |cffffffff7|cffced4da сек. и возвращает |cffffffff30%|cffced4da ближнего урона атакующим.|n|n"
        "Перезарядка: |cffffffff14|cffced4da сек.|r"
    )
    wts_updates[6745] = "|cffe4cfa3Провокация — уровень 5|r (|cffffffffW|r)"
    wts_updates[6768] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daВынуждает ближайших врагов атаковать героя. Снижает получаемый урон на |cffffffff10%|cffced4da на |cffffffff7|cffced4da сек. и возвращает |cffffffff40%|cffced4da ближнего урона атакующим.|n|n"
        "Перезарядка: |cffffffff12|cffced4da сек.|r"
    )

    # PA79: Добывать Ресурсы (G)
    wts_updates[35426] = "|cffe4cfa3Добывать Ресурсы|r"

    # pa15: Торнадо (W)
    wts_updates[41935] = "|cffe4cfa3Торнадо|r"

    # pa36: Огненная стрела (Q)
    wts_updates[41632] = "|cffe4cfa3Огненная стрела|r"

    # pa37: Волна исцеления (Q)
    wts_updates[41819] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[30016] = "|cffe4cfa3Волна исцеления — уровень 4|r (|cffffffffQ|r)"
    wts_updates[38211] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daПризывает мощную волну энергии Ци, восстанавливающую |cffffffff300|cffced4da ед. здоровья первой цели и исцеляющую до |cffffffff5|cffced4da союзников с потерей |cffffffff25%|cffced4da мощности за скачок.|n|n"
        "Расход маны: |cffffffff90|cffced4da ед. Перезарядка: |cffffffff9|cffced4da сек.|r"
    )

    # pa44: Защита Древних Мастеров (R)
    wts_updates[41820] = "|cffe4cfa3Защита Древних Мастеров|r"
    wts_updates[6499] = "|cffe4cfa3Защита Древних Мастеров|r (|cffffffffR|r)"
    wts_updates[6500] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daОсобая способность. Дарует полную неуязвимость окружающим союзникам в области вокруг Шадо-Пана.|n|n"
        "Сам герой остается уязвимым.|r"
    )
    wts_updates[36848] = "|cffe4cfa3Защита Древних Мастеров — уровень 1|r (|cffffffffR|r)"
    wts_updates[38220] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daДарует неуязвимость всем союзникам вокруг героя на |cffffffff20|cffced4da сек. Сам герой остается уязвимым.|n|n"
        "Расход маны: |cffffffff150|cffced4da ед. Перезарядка: |cffffffff180|cffced4da сек.|r"
    )
    wts_updates[36851] = "|cffe4cfa3Защита Древних Мастеров — уровень 2|r (|cffffffffR|r)"
    wts_updates[38219] = (
        "|cffa6afb8СПОСОБНОСТЬ:|r |cffced4daДарует неуязвимость всем союзникам вокруг героя на |cffffffff30|cffced4da сек. Сам герой остается уязвимым.|n|n"
        "Расход маны: |cffffffff150|cffced4da ед. Перезарядка: |cffffffff120|cffced4da сек.|r"
    )

    # =========================================================================
    # BUILD PLAN DATA STRUCTURE
    # =========================================================================
    categories = {
        "selection": ["A1I6"],
        "selection_markers": ["R0L3"],
        "buildings": [
            "pa23", "pa24", "pa25", "pa26", "pa27", "pa28", "pa30", "pa31", "pa32", "pa33",
            "h0NZ", "h0P5", "pa34", "h0P3", "h0P4"
        ],
        "units": [
            "pa01", "pa05", "pa12", "pa11", "pa06", "pa04", "pa10", "pa14", "pa08", "pa07",
            "pa13", "pa29", "pa38", "pa09", "pa35"
        ],
        "heroes": ["PA36", "PA37", "PA38", "PA40", "pa22"],
        "upgrades": [
            "PA10", "PA12", "PA14", "PA80", "PA81", "PA82", "PA83", "PA84", "PA85", "PA86",
            "PA87", "PA88", "PA89", "PA90", "PA91", "PA92", "PA93", "PA94", "PA95", "R0L3",
            "pa16", "pa21", "pa39", "pa47"
        ],
        "abilities": [
            "A1I6", "A1I7", "A1RB", "PA02", "PA03", "PA05", "PA13", "PA15", "PA16", "PA20",
            "PA45", "PA46", "PA50", "PA51", "PA53", "PA55", "PA57", "PA59", "PA60", "PA61",
            "PA62", "PA63", "PA65", "PA66", "PA67", "PA68", "PA69", "PA70", "PA73", "PA74",
            "PA75", "PA76", "PA77", "PA78", "PA79", "pa15", "pa36", "pa37", "pa44"
        ],
        "buffs": []
    }

    plan_data = {
        "race": "Pandarens",
        "race_name_ru": "Пандарены",
        "race_id": 34,
        "selection_ability": "A1I6",
        "total_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": categories
    }

    plan_path = folder / "pandarens_plan.json"
    plan_path.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote plan to {plan_path} with {len(wts_updates)} strings and {len(checks_def)} checks.")

    # =========================================================================
    # GENERATE CATEGORY REGISTRIES IN docs/ui_text/
    # =========================================================================
    raw_dump = json.loads((ROOT / "scripts/pandarens_raw_dump.json").read_text(encoding="utf-8"))

    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    def get_field_sid(item, field_name):
        v = item.get(f"raw_{field_name}")
        if not v:
            ov = item.get("overrides", {})
            f = item.get("fields", {})
            v = ov.get(field_name) or f.get(field_name)
        return parse_str_id(v)

    # 1. pandarens_selection.json
    sel_data = {
        "scope": "Пандарены (Pandarens): подсказка выбора расы A1I6 и маркер фракции R0L3",
        "object": "A1I6",
        "variants": ["SD"],
        "hotkey": {"value": "Z"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Pandarens регистрирует способность A1I6.",
            "При выборе создаются 5 рабочих pa01, исследуется маркер R0L3, удаляется выбирающий юнит.",
            "Горячая клавиша Z, создатель Capral, куратор VinerX, сложность 1/5 (●○○○○), период «Mists of Pandaria»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38913, "after": wts_updates[38913]},
            {"field": "tip1", "wts_id": 38914, "after": wts_updates[38914]},
            {"field": "ubertip1", "wts_id": 42408, "after": wts_updates[42408]}
        ],
        "markers": [
            {
                "id": "R0L3",
                "name": "Пандарены (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 28728, "after": wts_updates[28728]}
                ]
            }
        ]
    }
    (folder / "pandarens_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote pandarens_selection.json")

    # 2. pandarens_buildings.json
    bld_entries = []
    for b in raw_dump["buildings"]:
        b_id = b["id"]
        if b_id not in categories["buildings"]:
            continue
        hk_val = b.get("hotkey")
        entry = {"id": b_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            sid = get_field_sid(b, f)
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        bld_entries.append(entry)

    bld_data = {
        "scope": f"Пандарены (Pandarens): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "pandarens_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote pandarens_buildings.json ({len(bld_entries)} buildings)")

    # 3. pandarens_units.json
    unit_entries = []
    for u in raw_dump["units"]:
        u_id = u["id"]
        if u_id not in categories["units"]:
            continue
        hk_val = u.get("hotkey")
        entry = {"id": u_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            sid = get_field_sid(u, f)
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        unit_entries.append(entry)

    unit_data = {
        "scope": f"Пандарены (Pandarens): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "pandarens_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote pandarens_units.json ({len(unit_entries)} units)")

    # 4. pandarens_heroes.json
    hero_entries = []
    for h in raw_dump["heroes"]:
        h_id = h["id"]
        if h_id not in categories["heroes"]:
            continue
        hk_val = h.get("hotkey")
        entry = {"id": h_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            sid = get_field_sid(h, f)
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        hero_entries.append(entry)

    hero_data = {
        "scope": f"Пандарены (Pandarens): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "pandarens_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote pandarens_heroes.json ({len(hero_entries)} heroes)")

    # 5. pandarens_abilities.json
    abil_entries = []
    for a in raw_dump["abilities"]:
        a_id = a["id"]
        if a_id not in categories["abilities"]:
            continue
        entry = {"id": a_id, "levels": a.get("levels", 1), "strings": []}
        sid_name = parse_str_id(a.get("raw_name"))
        if sid_name and sid_name in wts_updates:
            entry["strings"].append({"field": "name", "wts_id": sid_name, "after": wts_updates[sid_name]})
        sid_rtip = parse_str_id(a.get("raw_researchtip"))
        if sid_rtip and sid_rtip in wts_updates:
            entry["strings"].append({"field": "researchtip", "wts_id": sid_rtip, "after": wts_updates[sid_rtip]})
        sid_rub = parse_str_id(a.get("raw_researchubertip"))
        if sid_rub and sid_rub in wts_updates:
            entry["strings"].append({"field": "researchubertip", "wts_id": sid_rub, "after": wts_updates[sid_rub]})
        for lvl_str, tips in a.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"tip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        for lvl_str, ubertips in a.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"ubertip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        if entry["strings"]:
            abil_entries.append(entry)

    abil_data = {
        "scope": f"Пандарены (Pandarens): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "pandarens_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote pandarens_abilities.json ({len(abil_entries)} abilities)")

    # 6. pandarens_research.json
    upg_entries = []
    for u in raw_dump["upgrades"]:
        u_id = u["id"]
        if u_id not in categories["upgrades"]:
            continue
        entry = {"id": u_id, "levels": u.get("levels", 1), "strings": []}
        for lvl_str, names in u.get("names", {}).items():
            sid = parse_str_id(names.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"name_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        for lvl_str, tips in u.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"tip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        for lvl_str, ubertips in u.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"ubertip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        upg_entries.append(entry)

    upg_data = {
        "scope": f"Пандарены (Pandarens): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "pandarens_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote pandarens_research.json ({len(upg_entries)} upgrades)")

    # 7. pandarens_audit.json
    audit_data = {
        "race": "Пандарены (Pandarens)",
        "race_id": 34,
        "selection_ability": "A1I6",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "town_halls": {
                    "tier1": {"id": "pa23", "name": "Ратуша Синего Зяблика", "food": 50},
                    "tier2": {"id": "pa24", "name": "Крепость Четырёх Мастеров", "food": 100},
                    "tier3": {"id": "pa25", "name": "Цитадель Равновесия", "food": 150}
                }
            },
            "units": {
                "count": len(unit_entries),
                "ids": [u["id"] for u in unit_entries]
            },
            "heroes": {
                "count": len(hero_entries),
                "ids": [h["id"] for h in hero_entries],
                "names": {
                    "PA36": "Лидер Шадо-Пан (Ловкость, ближний бой)",
                    "PA37": "Мастер Железной Лапы (Сила, ближний бой)",
                    "PA38": "Высший Монах (Интеллект, дальний бой)",
                    "PA40": "Танцующий с Ветром (Ловкость, ближний бой)",
                    "pa22": "Хмелевар (Элитный гибридный юнит / мастер стиля)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(wts_updates)
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0L3": "Маркер расы Пандарены"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items found for Pandarens."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific chat messages found for Pandarens."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": ["BUfa", "BUts", "Bblo", "Bcyc", "Bwwv", "Binv", "Bpig"],
            "status": "No race-specific custom buffs in war3map.w3h for Pandarens."
        },
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def)
    }
    (folder / "pandarens_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote pandarens_audit.json")

if __name__ == "__main__":
    main()
