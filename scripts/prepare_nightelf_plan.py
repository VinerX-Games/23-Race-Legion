# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Night Elf race (Race 26)."""
import json
from pathlib import Path
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
    # 1. RACE SELECTION: A0HL, R07L
    # =========================================================================
    # A0HL (Hotkey S)
    wts_updates[38863] = "|cffe4cfa3Ночные эльфы|r"
    wts_updates[38864] = "|cffe4cfa3Ночные эльфы|r (|cffffffffS|r)"
    wts_updates[35173] = (
        "|cffa6afb8РАСА:|cffced4da Древняя цивилизация калдорай, хранителей природы и служителей богини Элуны.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«WoW Vanilla — Legion»|r|n|n"
        "|cffced4daНочные эльфы, или калдорай — одна из древнейших рас Азерота, тысячелетиями оберегающая священные леса Калимдора. "
        "Опираясь на благословение Луны, мудрость друидов и первобытную силу древних древ, эльфы сочетают скрытность, "
        "меткую стрельбу и разрушительную магию природы.|r"
    )
    checks_def.append({"type": "ability", "id": "A0HL", "field": "name", "expected": wts_updates[38863]})
    checks_def.append({"type": "ability", "id": "A0HL", "field": "tip1", "expected": wts_updates[38864]})
    checks_def.append({"type": "ability", "id": "A0HL", "field": "ubertip1", "expected": wts_updates[35173]})

    # Marker: R07L
    wts_updates[10673] = "|cffe4cfa3Ночные эльфы|r"
    wts_updates[10674] = "|cffe4cfa3Ночные эльфы|r"
    wts_updates[20119] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к расе Ночных эльфов.|r"
    checks_def.append({"type": "upgrade", "id": "R07L", "field": "name1", "expected": wts_updates[10673]})
    checks_def.append({"type": "upgrade", "id": "R07L", "field": "tip1", "expected": wts_updates[10674]})
    checks_def.append({"type": "upgrade", "id": "R07L", "field": "ubertip1", "expected": wts_updates[20119]})

    # =========================================================================
    # 2. BUILDINGS (14 buildings)
    # =========================================================================
    # etol: Древо жизни (Q)
    wts_updates[26923] = "|cffe4cfa3Древо жизни|r"
    wts_updates[26924] = "|cffe4cfa3Древо жизни|r (|cffffffffQ|r)"
    wts_updates[5481] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Ночных эльфов первой ступени. Обеспечивает запас пищи и добычу ресурсов.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгонёк|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКруг Кенария|cffced4da|n- |cffa9c7deПуть Элуны|cffced4da|n- |cffa9c7deБлагословение природы|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deДрево столетий|cffced4da: открывает доступ к передовым сооружениям и технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "etol", "field": "name", "expected": wts_updates[26923]})
    checks_def.append({"type": "unit", "id": "etol", "field": "tip", "expected": wts_updates[26924]})
    checks_def.append({"type": "unit", "id": "etol", "field": "ubertip", "expected": wts_updates[5481]})

    # etoa: Древо столетий (Z)
    wts_updates[26925] = "|cffe4cfa3Древо столетий|r"
    wts_updates[26935] = "|cffe4cfa3Древо столетий|r (|cffffffffZ|r)"
    wts_updates[10114] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Ночных эльфов второй ступени. Существенно увеличивает запас пищи.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгонёк|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deБлагословение природы|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deДрево вечности|cffced4da: открывает доступ к высшим технологиям Ночных эльфов.|r"
    )
    checks_def.append({"type": "unit", "id": "etoa", "field": "name", "expected": wts_updates[26925]})
    checks_def.append({"type": "unit", "id": "etoa", "field": "tip", "expected": wts_updates[26935]})
    checks_def.append({"type": "unit", "id": "etoa", "field": "ubertip", "expected": wts_updates[10114]})

    # etoe: Древо вечности (Z)
    wts_updates[26936] = "|cffe4cfa3Древо вечности|r"
    wts_updates[26937] = "|cffe4cfa3Древо вечности|r (|cffffffffZ|r)"
    wts_updates[10115] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Ночных эльфов третьей ступени. Обеспечивает максимальный запас пищи.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгонёк|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deБлагословение природы|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "etoe", "field": "name", "expected": wts_updates[26936]})
    checks_def.append({"type": "unit", "id": "etoe", "field": "tip", "expected": wts_updates[26937]})
    checks_def.append({"type": "unit", "id": "etoe", "field": "ubertip", "expected": wts_updates[10115]})

    # emow: Лунный колодец (A)
    wts_updates[26938] = "|cffe4cfa3Лунный колодец|r"
    wts_updates[26939] = "|cffe4cfa3Лунный колодец|r (|cffffffffA|r)"
    wts_updates[31600] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Экономическое и вспомогательное сооружение. Накапливает живительную воду, восполняющую здоровье и ману союзников, а также приносит доход.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит |cffc8e087+20|cffced4da ед. дохода каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "emow", "field": "name", "expected": wts_updates[26938]})
    checks_def.append({"type": "unit", "id": "emow", "field": "tip", "expected": wts_updates[26939]})
    checks_def.append({"type": "unit", "id": "emow", "field": "ubertip", "expected": wts_updates[31600]})

    # eaom: Древо войны (W)
    wts_updates[26940] = "|cffe4cfa3Древо войны|r"
    wts_updates[26941] = "|cffe4cfa3Древо войны|r (|cffffffffW|r)"
    wts_updates[12949] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое военное сооружение армии Ночных эльфов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deЛучница|cffced4da: меткий стрелок дальнего боя.|n"
        "- |cffa9c7deОхотница|cffced4da: быстрый штурмовой боец с рикошетящей глефой.|n"
        "- |cffa9c7deГлефомет|cffced4da: дальнобойное осадное орудие.|n"
        "- |cffa9c7deЛунный воин|cffced4da: ловкий боец ближнего боя.|n"
        "- |cffa9c7deДух леса|cffced4da: древний лесной страж природы.|n"
        "- |cffa9c7deФурболг-следопыт|cffced4da: союзный воин ближнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deУлучшенные луки|cffced4da|n"
        "- |cffa9c7deТренировка меткости|cffced4da|n"
        "- |cffa9c7deУлучшенные лунные глефы|cffced4da|n"
        "- |cffa9c7deПронзающие лезвия|cffced4da|n"
        "- |cffa9c7deТанец полумесяца|cffced4da|n"
        "- |cffa9c7deОбучение друидизму|cffced4da|n"
        "- |cffa9c7deОпутывание|cffced4da|n"
        "- |cffa9c7deУдлинённые клинки|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "eaom", "field": "name", "expected": wts_updates[26940]})
    checks_def.append({"type": "unit", "id": "eaom", "field": "tip", "expected": wts_updates[26941]})
    checks_def.append({"type": "unit", "id": "eaom", "field": "ubertip", "expected": wts_updates[12949]})

    # eate: Алтарь старейшин (S)
    wts_updates[27021] = "|cffe4cfa3Алтарь старейшин|r"
    wts_updates[27022] = "|cffe4cfa3Алтарь старейшин|r (|cffffffffS|r)"
    wts_updates[12948] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священный алтарь для призыва и воскрешения героев Ночных эльфов.|n|n"
        "|cffa6afb8Герои:|cffced4da|n"
        "- |cffa9c7deХранитель рощи|cffced4da: герой-мистик, повелитель природы.|n"
        "- |cffa9c7deДруид-мастер|cffced4da: могущественный маг стихий и друидизма.|n"
        "- |cffa9c7deЛунная охотница|cffced4da: смертоносный ловкий стрелок Элуны.|r"
    )
    checks_def.append({"type": "unit", "id": "eate", "field": "name", "expected": wts_updates[27021]})
    checks_def.append({"type": "unit", "id": "eate", "field": "tip", "expected": wts_updates[27022]})
    checks_def.append({"type": "unit", "id": "eate", "field": "ubertip", "expected": wts_updates[12948]})

    # eaow: Древо ветров (R)
    wts_updates[27025] = "|cffe4cfa3Древо ветров|r"
    wts_updates[27026] = "|cffe4cfa3Древо ветров|r (|cffffffffR|r)"
    wts_updates[31602] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает летающих существ и магов стихии воздуха.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deДруид-ворон|cffced4da: маг поддержки, владеющий ветром и обликом буревестника.|n"
        "- |cffa9c7deЧудесный дракончик|cffced4da: летучий истребитель вражеских магов.|n"
        "- |cffa9c7deДревний Гвардеец|cffced4da: стойкий элитный страж ветров.|n"
        "- |cffa9c7deФурболг-воитель|cffced4da: могучий вождь фурболгов с аурой.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deПосвящение друида-ворона|cffced4da|n"
        "- |cffa9c7deЗнак ворона|cffced4da|n"
        "- |cffa9c7deАннулирование|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "eaow", "field": "name", "expected": wts_updates[27025]})
    checks_def.append({"type": "unit", "id": "eaow", "field": "tip", "expected": wts_updates[27026]})
    checks_def.append({"type": "unit", "id": "eaow", "field": "ubertip", "expected": wts_updates[31602]})

    # eaoe: Древо мудрости (D)
    wts_updates[27023] = "|cffe4cfa3Древо мудрости|r"
    wts_updates[27024] = "|cffe4cfa3Древо мудрости|r (|cffffffffD|r)"
    wts_updates[31601] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает магов земли, целителей и тяжелых лесных исполинов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deДриада|cffced4da: быстрый стрелок-антимаг с замедляющим ядом.|n"
        "- |cffa9c7deДруид-хищник|cffced4da: маг-целитель, способный принимать облик свирепого медведя.|n"
        "- |cffa9c7deГорный великан|cffced4da: тяжелый исполин, поглощающий осадный и магический урон.|n"
        "- |cffa9c7deДруид-сова|cffced4da: астральный друид Солнца и Луны.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deПосвящение друида-хищника|cffced4da|n"
        "- |cffa9c7deЗнак хищника|cffced4da|n"
        "- |cffa9c7deРассеяние чар|cffced4da|n"
        "- |cffa9c7deУстойчивая кожа|cffced4da|n"
        "- |cffa9c7deКаменная кожа|cffced4da|n"
        "- |cffa9c7deМагия совы|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "eaoe", "field": "name", "expected": wts_updates[27023]})
    checks_def.append({"type": "unit", "id": "eaoe", "field": "tip", "expected": wts_updates[27024]})
    checks_def.append({"type": "unit", "id": "eaoe", "field": "ubertip", "expected": wts_updates[31601]})

    # edob: Дом охотников (E)
    wts_updates[27027] = "|cffe4cfa3Дом охотников|r"
    wts_updates[27028] = "|cffe4cfa3Дом охотников|r (|cffffffffE|r)"
    wts_updates[3803] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главная кузница и арсенал Ночных эльфов. Улучшает вооружение и защиту армии.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deСила Луны|cffced4da: повышает урон стрелков.|n"
        "- |cffa9c7deЛунные доспехи|cffced4da: повышает броню стрелков и друидов.|n"
        "- |cffa9c7deСила леса|cffced4da: повышает урон воинов ближнего боя и зверей.|n"
        "- |cffa9c7deПрочные шкуры|cffced4da: повышает броню воинов ближнего боя и зверей.|n"
        "- |cffa9c7deНочное зрение|cffced4da|n"
        "- |cffa9c7deЛунный фонтан|cffced4da|n"
        "- |cffa9c7deЧасовой|cffced4da|n"
        "- |cffa9c7deСлияние с деревьями|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "edob", "field": "name", "expected": wts_updates[27027]})
    checks_def.append({"type": "unit", "id": "edob", "field": "tip", "expected": wts_updates[27028]})
    checks_def.append({"type": "unit", "id": "edob", "field": "ubertip", "expected": wts_updates[3803]})

    # etrp: Сторожевое древо (Z)
    wts_updates[27029] = "|cffe4cfa3Сторожевое древо|r"
    wts_updates[27030] = "|cffe4cfa3Сторожевое древо|r (|cffffffffZ|r)"
    wts_updates[31604] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение Ночных эльфов. Мечет тяжелые валуны в приближающихся врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deУкоренение|cffced4da: укрепляется в земле для дальнобойной стрельбы.|n"
        "- |cffa9c7deСъесть дерево|cffced4da: восстанавливает здоровье, поглощая дерево.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "etrp", "field": "name", "expected": wts_updates[27029]})
    checks_def.append({"type": "unit", "id": "etrp", "field": "tip", "expected": wts_updates[27030]})
    checks_def.append({"type": "unit", "id": "etrp", "field": "ubertip", "expected": wts_updates[31604]})

    # edos: Гнездо химер (Z)
    wts_updates[27031] = "|cffe4cfa3Гнездо химер|r"
    wts_updates[27032] = "|cffe4cfa3Гнездо химер|r (|cffffffffZ|r)"
    checks_def.append({"type": "unit", "id": "edos", "field": "name", "expected": wts_updates[27031]})
    checks_def.append({"type": "unit", "id": "edos", "field": "tip", "expected": wts_updates[27032]})

    # e03X: Храм Друидов (E)
    wts_updates[8676] = "|cffe4cfa3Храм Друидов|r"
    wts_updates[8742] = "|cffe4cfa3Храм Друидов|r (|cffffffffE|r)"
    wts_updates[9105] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище древних друидов, взывающее к силам дикой природы и первобытных зверей.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deПризыв помощи|cffced4da: призыв сил Диких Богов.|n"
        "- |cffa9c7deМилость Природы|cffced4da: целительный природный дождь.|n"
        "- |cffa9c7deЯрость Природы|cffced4da: призыв могучих древней.|r"
    )
    checks_def.append({"type": "unit", "id": "e03X", "field": "name", "expected": wts_updates[8676]})
    checks_def.append({"type": "unit", "id": "e03X", "field": "tip", "expected": wts_updates[8742]})
    checks_def.append({"type": "unit", "id": "e03X", "field": "ubertip", "expected": wts_updates[9105]})

    # e03W: Храм Элуны (E)
    wts_updates[2064] = "|cffe4cfa3Храм Элуны|r"
    wts_updates[2930] = "|cffe4cfa3Храм Элуны|r (|cffffffffE|r)"
    wts_updates[31603] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище богини Луны, дарующее благословение и небесную мощь воительницам калдорай.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deЗов Элуны|cffced4da: аура боевого неистовства.|n"
        "- |cffa9c7deЯрость Элуны|cffced4da: посвящение в ночные воительницы.|n"
        "- |cffa9c7deСлёзы Элуны|cffced4da: перерождение павших воинов в огоньки.|r"
    )
    checks_def.append({"type": "unit", "id": "e03W", "field": "name", "expected": wts_updates[2064]})
    checks_def.append({"type": "unit", "id": "e03W", "field": "tip", "expected": wts_updates[2930]})
    checks_def.append({"type": "unit", "id": "e03W", "field": "ubertip", "expected": wts_updates[31603]})

    # h0D8: Верфь (C)
    wts_updates[10907] = "|cffe4cfa3Верфь|r"
    wts_updates[10908] = "|cffe4cfa3Верфь|r (|cffffffffC|r)"
    wts_updates[10903] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Морское сооружение для строительства и оснащения боевых кораблей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deТранспортный корабль|cffced4da|n"
        "- |cffa9c7deФрегат|cffced4da|n"
        "- |cffa9c7deЛинкор|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deОрудия флота|cffced4da|n"
        "- |cffa9c7deУкреплённый корпус|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0D8", "field": "name", "expected": wts_updates[10907]})
    checks_def.append({"type": "unit", "id": "h0D8", "field": "tip", "expected": wts_updates[10908]})
    checks_def.append({"type": "unit", "id": "h0D8", "field": "ubertip", "expected": wts_updates[10903]})

    # =========================================================================
    # 3. WORKER & UNITS (20 units)
    # =========================================================================
    # ewsp: Огонёк (Q)
    wts_updates[27042] = "|cffe4cfa3Огонёк|r"
    wts_updates[27043] = "|cffe4cfa3Огонёк|r (|cffffffffQ|r)"
    wts_updates[31605] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Ночных эльфов. Бестелесный дух, собирающий древесину без вырубки леса, "
        "выращивающий здания и способный развеять магию ценой своей жизни.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deСамопожертвование|cffced4da: взрывается, сжигая ману врагов и нанося урон призванным существам.|n"
        "- |cffa9c7deОбновление|cffced4da: восстанавливает здоровье повреждённым древам.|n"
        "- |cffa9c7deСбор древесины|cffced4da: добывает дерево, не уничтожая деревья.|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенный телепорт на короткое расстояние.|n|n"
        "Не атакует.|r"
    )
    checks_def.append({"type": "unit", "id": "ewsp", "field": "name", "expected": wts_updates[27042]})
    checks_def.append({"type": "unit", "id": "ewsp", "field": "tip", "expected": wts_updates[27043]})
    checks_def.append({"type": "unit", "id": "ewsp", "field": "ubertip", "expected": wts_updates[31605]})

    # earc: Лучница (Q)
    wts_updates[1252] = "|cffe4cfa3Лучница|r"
    wts_updates[1253] = "|cffe4cfa3Лучница|r (|cffffffffQ|r)"
    wts_updates[1255] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый меткий стрелок дальнего боя калдорай.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deСлиться с тенью|cffced4da: становится невидимой ночью в неподвижном состоянии.|n"
        "- |cffa9c7deЗащита Элуны|cffced4da: снижает урон от атак дальнего боя и заклинаний.|n"
        "- |cffa9c7deСесть на гиппогрифа|cffced4da: объединяется с гиппогрифом в наездницу.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "earc", "field": "name", "expected": wts_updates[1252]})
    checks_def.append({"type": "unit", "id": "earc", "field": "tip", "expected": wts_updates[1253]})
    checks_def.append({"type": "unit", "id": "earc", "field": "ubertip", "expected": wts_updates[1255]})

    # esen: Охотница (W)
    wts_updates[217] = "|cffe4cfa3Охотница|r"
    wts_updates[219] = "|cffe4cfa3Охотница|r (|cffffffffW|r)"
    wts_updates[1250] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый мобильный воин авангарда Ночных эльфов, верхом на свирепой пантере.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЛунные глефы|cffced4da: глефа рикошетит по дополнительным целям.|n"
        "- |cffa9c7deЧасовой|cffced4da: сажает сову-разведчика на дерево для постоянного обзора.|n"
        "- |cffa9c7deСлиться с тенью|cffced4da: скрывается ночью в неподвижности.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "esen", "field": "name", "expected": wts_updates[217]})
    checks_def.append({"type": "unit", "id": "esen", "field": "tip", "expected": wts_updates[219]})
    checks_def.append({"type": "unit", "id": "esen", "field": "ubertip", "expected": wts_updates[1250]})

    # ebal: Глефомет (R)
    wts_updates[1424] = "|cffe4cfa3Глефомет|r"
    wts_updates[6114] = "|cffe4cfa3Глефомет|r (|cffffffffR|r)"
    wts_updates[33517] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойное осадное орудие Ночных эльфов, сокрушающее укрепления и скопления врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deПронзающие лезвия|cffced4da: пробивает строй противников и позволяет срубать деревья выстрелом.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "ebal", "field": "name", "expected": wts_updates[1424]})
    checks_def.append({"type": "unit", "id": "ebal", "field": "tip", "expected": wts_updates[6114]})
    checks_def.append({"type": "unit", "id": "ebal", "field": "ubertip", "expected": wts_updates[33517]})

    # e00I: Лунный воин (E)
    wts_updates[27293] = "|cffe4cfa3Лунный воин|r"
    wts_updates[27294] = "|cffe4cfa3Лунный воин|r (|cffffffffE|r)"
    wts_updates[31703] = (
        "|cffa6afb8ЮНИТ:|cffced4da Ловкий эльфийский боец ближнего боя с парными глефами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deТанец полумесяца|cffced4da: шанс |cffffffff15%|cffced4da при атаке совершить стремительный перекат за спину цели, нанося |cffffffff50%|cffced4da базового урона всем врагам на пути.|n"
        "- |cffa9c7deУдлинённые клинки|cffced4da: увеличенный радиус поражения глефами.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e00I", "field": "name", "expected": wts_updates[27293]})
    checks_def.append({"type": "unit", "id": "e00I", "field": "tip", "expected": wts_updates[27294]})
    checks_def.append({"type": "unit", "id": "e00I", "field": "ubertip", "expected": wts_updates[31703]})

    # e00J: Дух леса (Q)
    wts_updates[27295] = "|cffe4cfa3Дух леса|r"
    wts_updates[27296] = "|cffe4cfa3Дух леса|r (|cffffffffQ|r)"
    wts_updates[31704] = (
        "|cffa6afb8ЮНИТ:|cffced4da Первобытный дух чащобы, призванный охранять священные рощи.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deОпутывание|cffced4da: атаки опутывают цель живыми лозами, замедляя передвижение и скорость атаки.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e00J", "field": "name", "expected": wts_updates[27295]})
    checks_def.append({"type": "unit", "id": "e00J", "field": "tip", "expected": wts_updates[27296]})
    checks_def.append({"type": "unit", "id": "e00J", "field": "ubertip", "expected": wts_updates[31704]})

    # n05H: Фурболг-следопыт (W)
    wts_updates[27565] = "|cffe4cfa3Фурболг-следопыт|r"
    wts_updates[27566] = "|cffe4cfa3Фурболг-следопыт|r (|cffffffffW|r)"
    wts_updates[31905] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мощный союзный воин ближнего боя из племени фурболгов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВолшебный огонь|cffced4da: снижает броню цели и даёт обзор на ней.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n05H", "field": "name", "expected": wts_updates[27565]})
    checks_def.append({"type": "unit", "id": "n05H", "field": "tip", "expected": wts_updates[27566]})
    checks_def.append({"type": "unit", "id": "n05H", "field": "ubertip", "expected": wts_updates[31905]})

    # edot: Друид-ворон (W)
    wts_updates[27055] = "|cffe4cfa3Друид-ворон|r"
    wts_updates[27056] = "|cffe4cfa3Друид-ворон|r (|cffffffffW|r)"
    wts_updates[31599] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мобильный друид стихии ветра и воздуха.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВолшебный огонь|cffced4da: ослабляет броню противника и раскрывает его местоположение.|n"
        "- |cffa9c7deСмерч|cffced4da: поднимает вражеского воина в воздух, выводя из боя.|n"
        "- |cffa9c7deОблик буревестника|cffced4da: превращается в летучего ворона для разведки и воздушного боя.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "edot", "field": "name", "expected": wts_updates[27055]})
    checks_def.append({"type": "unit", "id": "edot", "field": "tip", "expected": wts_updates[27056]})
    checks_def.append({"type": "unit", "id": "edot", "field": "ubertip", "expected": wts_updates[31599]})

    # efdr: Чудесный дракончик (Q)
    wts_updates[27057] = "|cffe4cfa3Чудесный дракончик|r"
    wts_updates[27058] = "|cffe4cfa3Чудесный дракончик|r (|cffffffffQ|r)"
    checks_def.append({"type": "unit", "id": "efdr", "field": "name", "expected": wts_updates[27057]})
    checks_def.append({"type": "unit", "id": "efdr", "field": "tip", "expected": wts_updates[27058]})

    # e00H: Древний Гвардеец (W)
    wts_updates[27291] = "|cffe4cfa3Древний Гвардеец|r"
    wts_updates[27292] = "|cffe4cfa3Древний Гвардеец|r (|cffffffffW|r)"
    wts_updates[31702] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелый элитный воин-маг ближнего боя, закаленный веками тренировок.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deАннулирование|cffced4da: блокирует входящие вражеские заклинания.|n"
        "- |cffa9c7deЗачарованная глефа|cffced4da: заряжает оружие магической энергией.|n"
        "- |cffa9c7deЗащита|cffced4da: отражает стрелковые атаки.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e00H", "field": "name", "expected": wts_updates[27291]})
    checks_def.append({"type": "unit", "id": "e00H", "field": "tip", "expected": wts_updates[27292]})
    checks_def.append({"type": "unit", "id": "e00H", "field": "ubertip", "expected": wts_updates[31702]})

    # n064: Фурболг-воитель (E)
    wts_updates[5750] = "|cffe4cfa3Фурболг-воитель|r"
    wts_updates[5765] = "|cffe4cfa3Фурболг-воитель|r (|cffffffffE|r)"
    wts_updates[33189] = (
        "|cffa6afb8ЮНИТ:|cffced4da Свирепый вождь фурболгов с типом атаки Хаос.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deКомандирская аура|cffced4da: повышает урон союзников поблизости.|n"
        "- |cffa9c7deГромовая поступь|cffced4da: сотрясает землю, нанося урон и замедляя врагов.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n064", "field": "name", "expected": wts_updates[5750]})
    checks_def.append({"type": "unit", "id": "n064", "field": "tip", "expected": wts_updates[5765]})
    checks_def.append({"type": "unit", "id": "n064", "field": "ubertip", "expected": wts_updates[33189]})

    # edry: Дриада (Q)
    wts_updates[27050] = "|cffe4cfa3Дриада|r"
    wts_updates[27049] = "|cffe4cfa3Дриада|r (|cffffffffQ|r)"
    wts_updates[31596] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый стрелок дальнего боя и главный антимаг калдорай.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЗамедляющий яд|cffced4da: каждая атака наносит периодический урон и замедляет скорость цели.|n"
        "- |cffa9c7deРассеяние чар|cffced4da: снимает отрицательные эффекты с союзников и положительные с врагов.|n"
        "- |cffa9c7deНевосприимчивость к магии|cffced4da: полный иммунитет к вражеским заклинаниям.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "edry", "field": "name", "expected": wts_updates[27050]})
    checks_def.append({"type": "unit", "id": "edry", "field": "tip", "expected": wts_updates[27049]})
    checks_def.append({"type": "unit", "id": "edry", "field": "ubertip", "expected": wts_updates[31596]})

    # edoc: Друид-хищник (W)
    wts_updates[27051] = "|cffe4cfa3Друид-хищник|r"
    wts_updates[27052] = "|cffe4cfa3Друид-хищник|r (|cffffffffW|r)"
    wts_updates[31597] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий друид-целитель, способный трансформироваться в свирепого боевого медведя.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deРёв|cffced4da: вдохновляет союзников, увеличивая их урон на |cffc8e08725%|cffced4da.|n"
        "- |cffa9c7deОмоложение|cffced4da: восстанавливает здоровье цели в течение времени.|n"
        "- |cffa9c7deОблик медведя|cffced4da: превращается в грозного бойца ближнего боя с высоким запасом здоровья.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "edoc", "field": "name", "expected": wts_updates[27051]})
    checks_def.append({"type": "unit", "id": "edoc", "field": "tip", "expected": wts_updates[27052]})
    checks_def.append({"type": "unit", "id": "edoc", "field": "ubertip", "expected": wts_updates[31597]})

    # emtg: Горный великан (E)
    wts_updates[27053] = "|cffe4cfa3Горный великан|r"
    wts_updates[27054] = "|cffe4cfa3Горный великан|r (|cffffffffE|r)"
    wts_updates[31598] = (
        "|cffa6afb8ЮНИТ:|cffced4da Огромный каменный исполин, способный выдерживать колоссальный урон.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deПровокация|cffced4da: заставляет врагов атаковать великана.|n"
        "- |cffa9c7deБоевая дубинка|cffced4da: вырывает дерево и атакует осадным уроном с эффектом рассечения.|n"
        "- |cffa9c7deУстойчивая кожа|cffced4da: снижает урон от магии и сокращает длительность заклинаний.|n"
        "- |cffa9c7deКаменная кожа|cffced4da: снижает входящий урон от атак.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "emtg", "field": "name", "expected": wts_updates[27053]})
    checks_def.append({"type": "unit", "id": "emtg", "field": "tip", "expected": wts_updates[27054]})
    checks_def.append({"type": "unit", "id": "emtg", "field": "ubertip", "expected": wts_updates[31598]})

    # n05D: Друид-сова (R)
    wts_updates[27194] = "|cffe4cfa3Друид-сова|r"
    wts_updates[27627] = "|cffe4cfa3Друид-сова|r (|cffffffffR|r)"
    wts_updates[31904] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мудрый астральный друид, владеющий силами Солнца и Луны.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deАстральная фаза|cffced4da: переключает стойку между Солнцем (атаки поджигают цели, заклинание «Солнечный ожог») и Луной (атаки восстанавливают ману раненому союзнику, заклинание «Звёздный луч»).|n"
        "- |cffa9c7deОблик совуха|cffced4da: трансформация в яростного совуха-берсерка.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n05D", "field": "name", "expected": wts_updates[27194]})
    checks_def.append({"type": "unit", "id": "n05D", "field": "tip", "expected": wts_updates[27627]})
    checks_def.append({"type": "unit", "id": "n05D", "field": "ubertip", "expected": wts_updates[31904]})

    # n05G: Совух-берсерк
    wts_updates[27418] = "|cffe4cfa3Совух-берсерк|r"
    wts_updates[32922] = (
        "|cffa6afb8ЮНИТ:|cffced4da Свирепая боевая форма друида-совы с типом атаки Хаос.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deБешенство совуха|cffced4da: увеличивает скорость атаки и передвижения.|n"
        "- |cffa9c7deАстральная фаза|cffced4da: использование астральных заклинаний Солнца и Луны.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n05G", "field": "name", "expected": wts_updates[27418]})
    checks_def.append({"type": "unit", "id": "n05G", "field": "ubertip", "expected": wts_updates[32922]})

    # Naval: h0D9, h0DB, h0DA
    wts_updates[10911] = "|cffe4cfa3Транспорт|r"
    checks_def.append({"type": "unit", "id": "h0D9", "field": "name", "expected": wts_updates[10911]})

    wts_updates[5520] = "|cffe4cfa3Фрегат|r"
    wts_updates[10898] = "|cffa6afb8ЮНИТ:|cffced4da Боевой парусно-гребной корабль прибрежного флота.|n|n|cffa6afb8Атакует наземные и воздушные цели.|r"
    checks_def.append({"type": "unit", "id": "h0DB", "field": "name", "expected": wts_updates[5520]})
    checks_def.append({"type": "unit", "id": "h0DB", "field": "ubertip", "expected": wts_updates[10898]})

    wts_updates[10931] = "|cffe4cfa3Линкор|r"
    wts_updates[6929] = "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый флагманский линейный корабль дальнего боя.|n|n|cffa6afb8Атакует наземные цели.|r"
    checks_def.append({"type": "unit", "id": "h0DA", "field": "name", "expected": wts_updates[10931]})
    checks_def.append({"type": "unit", "id": "h0DA", "field": "ubertip", "expected": wts_updates[6929]})

    # =========================================================================
    # 4. HEROES (3 heroes)
    # =========================================================================
    # E00V: Хранитель рощи (K)
    wts_updates[27634] = "|cffe4cfa3Хранитель рощи|r"
    wts_updates[20328] = "|cffe4cfa3Хранитель рощи|r (|cffffffffK|r)"
    wts_updates[20330] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Полубог-мистик священных рощ Калимдора, повелевающий первозданными силами природы и леса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deСила природы|cffced4da: превращает деревья в преданных духов-древней.|n"
        "- |cffa9c7deЗамедляющие корни|cffced4da: атаки опутывают врагов, снижая скорость бега и атаки.|n"
        "- |cffa9c7deАура шипов|cffced4da: окружает союзников щитом, отражающим урон ближнего боя.|n"
        "- |cffa9c7deЯрость природы|cffced4da: массовое опутывание и поражение врагов грозовыми ударами.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    wts_updates[20346] = "|cffe4cfa3Хранитель рощи|r"
    wts_updates[20348] = "|cffe4cfa3Хранитель рощи|r"
    checks_def.append({"type": "unit", "id": "E00V", "field": "name", "expected": wts_updates[27634]})
    checks_def.append({"type": "unit", "id": "E00V", "field": "tip", "expected": wts_updates[20328]})
    checks_def.append({"type": "unit", "id": "E00V", "field": "ubertip", "expected": wts_updates[20330]})

    # E011: Лунная охотница (C)
    wts_updates[16268] = "|cffe4cfa3Лунная охотница|r"
    wts_updates[3714] = "|cffa9c7deКатрис Звёздная Песня|r"
    wts_updates[3857] = "|cffe4cfa3Лунная охотница|r (|cffffffffC|r)"
    wts_updates[31708] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Искусный верховный следопыт Часовых, разящая врагов стрелами Элуны с дистанции.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВзрыв маны|cffced4da: обстреливает область сгустками маны, оглушая врагов.|n"
        "- |cffa9c7deЛедяные стрелы|cffced4da: атаки наносят дополнительный урон и замедляют цель.|n"
        "- |cffa9c7deАура меткости|cffced4da: увеличивает урон дальнобойных атак союзников.|n"
        "- |cffa9c7deСмертельный выстрел|cffced4da: выпускает мощную стрелу, пронзающую врагов на линии.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffЛовкость|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    wts_updates[3856] = "|cffe4cfa3Лунная охотница|r"
    wts_updates[3898] = "|cffe4cfa3Лунная охотница|r"
    checks_def.append({"type": "unit", "id": "E011", "field": "name", "expected": wts_updates[16268]})
    checks_def.append({"type": "unit", "id": "E011", "field": "propernames", "expected": wts_updates[3714]})
    checks_def.append({"type": "unit", "id": "E011", "field": "tip", "expected": wts_updates[3857]})
    checks_def.append({"type": "unit", "id": "E011", "field": "ubertip", "expected": wts_updates[31708]})

    # E00W: Друид-мастер (Z)
    wts_updates[27385] = "|cffe4cfa3Друид-мастер|r"
    wts_updates[3606] = "|cffa9c7deВерховный друид|r"
    wts_updates[8455] = "|cffe4cfa3Друид-мастер|r (|cffffffffZ|r)"
    wts_updates[31707] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Верховный архидруид, в совершенстве овладевший стихией бури, скрытностью и древними звериными формами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deРаздвоенная молния|cffced4da: поражает веером молний группу противников перед собой.|n"
        "- |cffa9c7deСкачок|cffced4da: мгновенно телепортируется на короткую дистанцию.|n"
        "- |cffa9c7deУскользание|cffced4da: шанс уклониться от входящих атак.|n"
        "- |cffa9c7deОблик совухи|cffced4da: превращается в грозного совуха с усиленными характеристиками.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    wts_updates[27386] = "|cffe4cfa3Друид-мастер|r"
    wts_updates[27387] = "|cffe4cfa3Друид-мастер|r"
    checks_def.append({"type": "unit", "id": "E00W", "field": "name", "expected": wts_updates[27385]})
    checks_def.append({"type": "unit", "id": "E00W", "field": "propernames", "expected": wts_updates[3606]})
    checks_def.append({"type": "unit", "id": "E00W", "field": "tip", "expected": wts_updates[8455]})
    checks_def.append({"type": "unit", "id": "E00W", "field": "ubertip", "expected": wts_updates[31707]})

    # =========================================================================
    # 5. RESEARCH / UPGRADES
    # =========================================================================
    # R0G1: Круг Кенария (R)
    wts_updates[27190] = "|cffe4cfa3Круг Кенария|r"
    wts_updates[40869] = "|cffe4cfa3Круг Кенария|r (|cffffffffR|r)"
    wts_updates[41852] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Выбор пути друидов Круга Кенария и духов дикой природы. "
        "Открывает доступ к друидам и фурболгам, блокируя ветку Часовых Элуны.|n|n"
        "|cffa6afb8Открывает доступ к:|cffced4da|n"
        "- |cffa9c7deДух леса|cffced4da|n"
        "- |cffa9c7deДруид-ворон|cffced4da|n"
        "- |cffa9c7deДруид-хищник|cffced4da|n"
        "- |cffa9c7deДруид-сова|cffced4da|n"
        "- |cffa9c7deФурболг-следопыт|cffced4da|n"
        "- |cffa9c7deФурболг-воитель|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0G1", "field": "name1", "expected": wts_updates[27190]})
    checks_def.append({"type": "upgrade", "id": "R0G1", "field": "tip1", "expected": wts_updates[40869]})
    checks_def.append({"type": "upgrade", "id": "R0G1", "field": "ubertip1", "expected": wts_updates[41852]})

    # R0G2: Путь Элуны (E)
    wts_updates[41838] = "|cffe4cfa3Путь Элуны|r"
    wts_updates[40871] = "|cffe4cfa3Путь Элуны|r (|cffffffffE|r)"
    wts_updates[20295] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Выбор пути воинства Часовых и служителей богини Элуны. "
        "Открывает доступ к эльфийским воинам и стрелкам, блокируя ветку Круга Кенария.|n|n"
        "|cffa6afb8Открывает доступ к:|cffced4da|n"
        "- |cffa9c7deЛучница|cffced4da|n"
        "- |cffa9c7deОхотница|cffced4da|n"
        "- |cffa9c7deЛунный воин|cffced4da|n"
        "- |cffa9c7deДревний Гвардеец|cffced4da|n"
        "- |cffa9c7deТанец полумесяца|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0G2", "field": "name1", "expected": wts_updates[41838]})
    checks_def.append({"type": "upgrade", "id": "R0G2", "field": "tip1", "expected": wts_updates[40871]})
    checks_def.append({"type": "upgrade", "id": "R0G2", "field": "ubertip1", "expected": wts_updates[20295]})

    # R0GB: Выбор направления
    wts_updates[27604] = "|cffe4cfa3Выбор направления|r"
    wts_updates[27605] = "|cffe4cfa3Выбор направления|r"
    wts_updates[41817] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер выбора пути развития расы Ночных эльфов (Круг Кенария или Путь Элуны).|r"
    checks_def.append({"type": "upgrade", "id": "R0GB", "field": "name1", "expected": wts_updates[27604]})
    checks_def.append({"type": "upgrade", "id": "R0GB", "field": "tip1", "expected": wts_updates[27605]})
    checks_def.append({"type": "upgrade", "id": "R0GB", "field": "ubertip1", "expected": wts_updates[41817]})

    # Renb: Благословение природы (W)
    wts_updates[27161] = "|cffe4cfa3Благословение природы|r"
    wts_updates[40023] = "|cffe4cfa3Благословение природы|r (|cffffffffW|r)"
    checks_def.append({"type": "upgrade", "id": "Renb", "field": "name1", "expected": wts_updates[27161]})
    checks_def.append({"type": "upgrade", "id": "Renb", "field": "tip1", "expected": wts_updates[40023]})

    # Resm: Сила Луны (Q) — 6 уровней
    for lvl in range(1, 7):
        name_sids = [27059, 27061, 27060, 27064, 27063, 27062]
        tip_sids = [27065, 27066, 27067, 27070, 27069, 27068]
        ub_sids = [27071, 27072, 27073, 27074, 27075, 27076]
        wts_updates[name_sids[lvl-1]] = f"|cffe4cfa3Сила Луны — уровень {lvl}|r"
        wts_updates[tip_sids[lvl-1]] = f"|cffe4cfa3Сила Луны — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон стрелков дальнего боя на |cffc8e087+10%|cffced4da за каждый уровень.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛучница|cffced4da|n- |cffa9c7deОхотница|cffced4da|n- |cffa9c7deГлефомет|cffced4da|n- |cffa9c7deДриада|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "Resm", "field": f"name{lvl}", "expected": wts_updates[name_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Resm", "field": f"tip{lvl}", "expected": wts_updates[tip_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Resm", "field": f"ubertip{lvl}", "expected": wts_updates[ub_sids[lvl-1]]})

    # Rema: Лунные доспехи (A) — 6 уровней
    for lvl in range(1, 7):
        name_sids = [27139, 27140, 27141, 27144, 27143, 27142]
        tip_sids = [27145, 27146, 27147, 27150, 27149, 27148]
        ub_sids = [27151, 27152, 27153, 27154, 27155, 27156]
        wts_updates[name_sids[lvl-1]] = f"|cffe4cfa3Лунные доспехи — уровень {lvl}|r"
        wts_updates[tip_sids[lvl-1]] = f"|cffe4cfa3Лунные доспехи — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает защиту стрелков и друидов на |cffc8e087+2|cffced4da ед. брони за уровень.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛучница|cffced4da|n- |cffa9c7deОхотница|cffced4da|n- |cffa9c7deГлефомет|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deДруиды|cffced4da (в облике ночного эльфа).|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "Rema", "field": f"name{lvl}", "expected": wts_updates[name_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Rema", "field": f"tip{lvl}", "expected": wts_updates[tip_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Rema", "field": f"ubertip{lvl}", "expected": wts_updates[ub_sids[lvl-1]]})

    # Resw: Сила леса (W) — 6 уровней
    for lvl in range(1, 7):
        name_sids = [27077, 27078, 27079, 27082, 27081, 27080]
        tip_sids = [27083, 27084, 27085, 27088, 27087, 27086]
        ub_sids = [27089, 27090, 27091, 27092, 27093, 27094]
        wts_updates[name_sids[lvl-1]] = f"|cffe4cfa3Сила леса — уровень {lvl}|r"
        wts_updates[tip_sids[lvl-1]] = f"|cffe4cfa3Сила леса — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя и зверей на |cffc8e087+10%|cffced4da за каждый уровень.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛунный воин|cffced4da|n- |cffa9c7deДух леса|cffced4da|n- |cffa9c7deФурболги|cffced4da|n- |cffa9c7deГорный великан|cffced4da|n- |cffa9c7deДруиды|cffced4da (в облике зверей)|n- |cffa9c7deХимера|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "Resw", "field": f"name{lvl}", "expected": wts_updates[name_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Resw", "field": f"tip{lvl}", "expected": wts_updates[tip_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Resw", "field": f"ubertip{lvl}", "expected": wts_updates[ub_sids[lvl-1]]})

    # Rerh: Прочные шкуры (R) — 6 уровней
    for lvl in range(1, 7):
        name_sids = [27117, 27118, 27119, 27122, 27121, 27120]
        tip_sids = [27123, 27124, 27125, 27128, 27127, 27126]
        ub_sids = [27129, 27130, 27131, 27132, 27133, 27134]
        wts_updates[name_sids[lvl-1]] = f"|cffe4cfa3Прочные шкуры — уровень {lvl}|r"
        wts_updates[tip_sids[lvl-1]] = f"|cffe4cfa3Прочные шкуры — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает защиту воинов ближнего боя и зверей на |cffc8e087+2|cffced4da ед. брони за уровень.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛунный воин|cffced4da|n- |cffa9c7deДух леса|cffced4da|n- |cffa9c7deФурболги|cffced4da|n- |cffa9c7deГорный великан|cffced4da|n- |cffa9c7deДруиды|cffced4da (в облике зверей)|n- |cffa9c7deХимера|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "Rerh", "field": f"name{lvl}", "expected": wts_updates[name_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Rerh", "field": f"tip{lvl}", "expected": wts_updates[tip_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "Rerh", "field": f"ubertip{lvl}", "expected": wts_updates[ub_sids[lvl-1]]})

    # R0GC: Слияние с деревьями (Z) — 6 уровней
    for lvl in range(1, 7):
        name_sids = [27655, 27656, 27657, 27658, 27659, 27660]
        tip_sids = [27661, 27662, 27663, 27664, 27665, 27666]
        ub_sids = [26003, 25998, 25999, 26000, 26001, 26002]
        wts_updates[name_sids[lvl-1]] = f"|cffe4cfa3Слияние с деревьями — уровень {lvl}|r"
        wts_updates[tip_sids[lvl-1]] = f"|cffe4cfa3Слияние с деревьями — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём добываемой огоньками древесины на |cffc8e087+5|cffced4da ед. за уровень.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОгонёк|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GC", "field": f"name{lvl}", "expected": wts_updates[name_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GC", "field": f"tip{lvl}", "expected": wts_updates[tip_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GC", "field": f"ubertip{lvl}", "expected": wts_updates[ub_sids[lvl-1]]})

    # Reuv: Ночное зрение (U)
    wts_updates[27135] = "|cffe4cfa3Ночное зрение|r"
    wts_updates[27136] = "|cffe4cfa3Ночное зрение|r (|cffffffffU|r)"
    checks_def.append({"type": "upgrade", "id": "Reuv", "field": "name1", "expected": wts_updates[27135]})
    checks_def.append({"type": "upgrade", "id": "Reuv", "field": "tip1", "expected": wts_updates[27136]})

    # Rews: Лунный фонтан (E)
    wts_updates[27137] = "|cffe4cfa3Лунный фонтан|r"
    wts_updates[27138] = "|cffe4cfa3Лунный фонтан|r (|cffffffffE|r)"
    checks_def.append({"type": "upgrade", "id": "Rews", "field": "name1", "expected": wts_updates[27137]})
    checks_def.append({"type": "upgrade", "id": "Rews", "field": "tip1", "expected": wts_updates[27138]})

    # Resc: Часовой (S)
    wts_updates[27105] = "|cffe4cfa3Часовой|r"
    wts_updates[27106] = "|cffe4cfa3Часовой|r (|cffffffffS|r)"
    checks_def.append({"type": "upgrade", "id": "Resc", "field": "name1", "expected": wts_updates[27105]})
    checks_def.append({"type": "upgrade", "id": "Resc", "field": "tip1", "expected": wts_updates[27106]})

    # Reib: Улучшенные луки (A)
    wts_updates[27099] = "|cffe4cfa3Улучшенные луки|r"
    wts_updates[27100] = "|cffe4cfa3Улучшенные луки|r (|cffffffffA|r)"
    checks_def.append({"type": "upgrade", "id": "Reib", "field": "name1", "expected": wts_updates[27099]})
    checks_def.append({"type": "upgrade", "id": "Reib", "field": "tip1", "expected": wts_updates[27100]})

    # Remk: Тренировка меткости (A)
    wts_updates[27098] = "|cffe4cfa3Тренировка меткости|r"
    wts_updates[27097] = "|cffe4cfa3Тренировка меткости|r (|cffffffffA|r)"
    checks_def.append({"type": "upgrade", "id": "Remk", "field": "name1", "expected": wts_updates[27098]})
    checks_def.append({"type": "upgrade", "id": "Remk", "field": "tip1", "expected": wts_updates[27097]})

    # Remg: Улучшенные лунные глефы (G)
    wts_updates[27101] = "|cffe4cfa3Улучшенные лунные глефы|r"
    wts_updates[27102] = "|cffe4cfa3Улучшенные лунные глефы|r (|cffffffffG|r)"
    checks_def.append({"type": "upgrade", "id": "Remg", "field": "name1", "expected": wts_updates[27101]})
    checks_def.append({"type": "upgrade", "id": "Remg", "field": "tip1", "expected": wts_updates[27102]})

    # Repb: Пронзающие лезвия (P)
    wts_updates[27095] = "|cffe4cfa3Пронзающие лезвия|r"
    wts_updates[27096] = "|cffe4cfa3Пронзающие лезвия|r (|cffffffffP|r)"
    checks_def.append({"type": "upgrade", "id": "Repb", "field": "name1", "expected": wts_updates[27095]})
    checks_def.append({"type": "upgrade", "id": "Repb", "field": "tip1", "expected": wts_updates[27096]})

    # R0GA: Обучение друидизму (S)
    wts_updates[27594] = "|cffe4cfa3Обучение друидизму|r"
    wts_updates[27595] = "|cffe4cfa3Обучение друидизму|r (|cffffffffS|r)"
    wts_updates[27596] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает фурболгов тайным искусствам друидов. "
        "Повышает скорость атаки на |cffc8e087+15%|cffced4da и максимальный запас здоровья на |cffc8e087+50|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deФурболг-следопыт|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0GA", "field": "name1", "expected": wts_updates[27594]})
    checks_def.append({"type": "upgrade", "id": "R0GA", "field": "tip1", "expected": wts_updates[27595]})
    checks_def.append({"type": "upgrade", "id": "R0GA", "field": "ubertip1", "expected": wts_updates[27596]})

    # R0G9: Опутывание (A)
    wts_updates[27579] = "|cffe4cfa3Опутывание|r"
    wts_updates[27580] = "|cffe4cfa3Опутывание|r (|cffffffffA|r)"
    wts_updates[27581] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет атаки Духов леса способностью оплетать врагов живыми лозами, "
        "замедляя их скорость атаки и передвижения.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДух леса|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0G9", "field": "name1", "expected": wts_updates[27579]})
    checks_def.append({"type": "upgrade", "id": "R0G9", "field": "tip1", "expected": wts_updates[27580]})
    checks_def.append({"type": "upgrade", "id": "R0G9", "field": "ubertip1", "expected": wts_updates[27581]})

    # R0G7: Удлинённые клинки (D)
    wts_updates[27561] = "|cffe4cfa3Удлинённые клинки|r"
    wts_updates[27562] = "|cffe4cfa3Удлинённые клинки|r (|cffffffffD|r)"
    wts_updates[27554] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает радиус поражения глефами и наделяет воинов способностью блокировать входящие заклинания.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛунный воин|cffced4da|n- |cffa9c7deДревний Гвардеец|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0G7", "field": "name1", "expected": wts_updates[27561]})
    checks_def.append({"type": "upgrade", "id": "R0G7", "field": "tip1", "expected": wts_updates[27562]})
    checks_def.append({"type": "upgrade", "id": "R0G7", "field": "ubertip1", "expected": wts_updates[27554]})

    # Redt: Посвящение друида-ворона (A) — 2 уровня
    wts_updates[27111] = "|cffe4cfa3Друид-ворон: посвящение в адепты|r"
    wts_updates[27113] = "|cffe4cfa3Друид-ворон: посвящение в адепты|r (|cffffffffA|r)"
    wts_updates[27112] = "|cffe4cfa3Друид-ворон: посвящение в мастера|r"
    wts_updates[27114] = "|cffe4cfa3Друид-ворон: посвящение в мастера|r (|cffffffffA|r)"
    checks_def.append({"type": "upgrade", "id": "Redt", "field": "name1", "expected": wts_updates[27111]})
    checks_def.append({"type": "upgrade", "id": "Redt", "field": "tip1", "expected": wts_updates[27113]})
    checks_def.append({"type": "upgrade", "id": "Redt", "field": "name2", "expected": wts_updates[27112]})
    checks_def.append({"type": "upgrade", "id": "Redt", "field": "tip2", "expected": wts_updates[27114]})

    # Reec: Знак ворона (M)
    wts_updates[27159] = "|cffe4cfa3Знак ворона|r"
    wts_updates[27160] = "|cffe4cfa3Знак ворона|r (|cffffffffM|r)"
    checks_def.append({"type": "upgrade", "id": "Reec", "field": "name1", "expected": wts_updates[27159]})
    checks_def.append({"type": "upgrade", "id": "Reec", "field": "tip1", "expected": wts_updates[27160]})

    # R0G6: Аннулирование (S) — 3 уровня
    for lvl in range(1, 4):
        name_sids = [27546, 27547, 27552]
        tip_sids = [8471, 8472, 27553]
        ub_sids = [8468, 8474, 8475]
        wts_updates[name_sids[lvl-1]] = f"|cffe4cfa3Аннулирование — уровень {lvl}|r"
        wts_updates[tip_sids[lvl-1]] = f"|cffe4cfa3Аннулирование — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает магическую защиту Древних Гвардейцев. "
            f"Увеличивает скорость атаки на |cffc8e087+{lvl * 10}%|cffced4da и регенерацию здоровья на |cffc8e087+{lvl * 0.5}|cffced4da ед./сек.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревний Гвардеец|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0G6", "field": f"name{lvl}", "expected": wts_updates[name_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0G6", "field": f"tip{lvl}", "expected": wts_updates[tip_sids[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0G6", "field": f"ubertip{lvl}", "expected": wts_updates[ub_sids[lvl-1]]})

    # Redc: Посвящение друида-хищника (L) — 2 уровня
    wts_updates[27107] = "|cffe4cfa3Друид-хищник: посвящение в адепты|r"
    wts_updates[27109] = "|cffe4cfa3Друид-хищник: посвящение в адепты|r (|cffffffffL|r)"
    wts_updates[27108] = "|cffe4cfa3Друид-хищник: посвящение в мастера|r"
    wts_updates[27110] = "|cffe4cfa3Друид-хищник: посвящение в мастера|r (|cffffffffL|r)"
    checks_def.append({"type": "upgrade", "id": "Redc", "field": "name1", "expected": wts_updates[27107]})
    checks_def.append({"type": "upgrade", "id": "Redc", "field": "tip1", "expected": wts_updates[27109]})
    checks_def.append({"type": "upgrade", "id": "Redc", "field": "name2", "expected": wts_updates[27108]})
    checks_def.append({"type": "upgrade", "id": "Redc", "field": "tip2", "expected": wts_updates[27110]})

    # Reeb: Знак хищника (M)
    wts_updates[27044] = "|cffe4cfa3Знак хищника|r"
    wts_updates[27045] = "|cffe4cfa3Знак хищника|r (|cffffffffM|r)"
    checks_def.append({"type": "upgrade", "id": "Reeb", "field": "name1", "expected": wts_updates[27044]})
    checks_def.append({"type": "upgrade", "id": "Reeb", "field": "tip1", "expected": wts_updates[27045]})

    # Resi: Рассеяние чар (A)
    wts_updates[27115] = "|cffe4cfa3Рассеяние чар|r"
    wts_updates[27116] = "|cffe4cfa3Рассеяние чар|r (|cffffffffA|r)"
    checks_def.append({"type": "upgrade", "id": "Resi", "field": "name1", "expected": wts_updates[27115]})
    checks_def.append({"type": "upgrade", "id": "Resi", "field": "tip1", "expected": wts_updates[27116]})

    # Rers: Устойчивая кожа (D)
    wts_updates[27103] = "|cffe4cfa3Устойчивая кожа|r"
    wts_updates[27104] = "|cffe4cfa3Устойчивая кожа|r (|cffffffffD|r)"
    checks_def.append({"type": "upgrade", "id": "Rers", "field": "name1", "expected": wts_updates[27103]})
    checks_def.append({"type": "upgrade", "id": "Rers", "field": "tip1", "expected": wts_updates[27104]})

    # Rehs: Каменная кожа (F)
    wts_updates[27157] = "|cffe4cfa3Каменная кожа|r"
    wts_updates[27158] = "|cffe4cfa3Каменная кожа|r (|cffffffffF|r)"
    checks_def.append({"type": "upgrade", "id": "Rehs", "field": "name1", "expected": wts_updates[27157]})
    checks_def.append({"type": "upgrade", "id": "Rehs", "field": "tip1", "expected": wts_updates[27158]})

    # R0G8: Магия совы (M) — 2 уровня
    wts_updates[27570] = "|cffe4cfa3Магия совы — уровень 1|r"
    wts_updates[27571] = "|cffe4cfa3Магия совы — уровень 1|r (|cffffffffM|r)"
    wts_updates[27572] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает друидов-сов, повышая здоровье на |cffc8e087+40|cffced4da ед., "
        "запас маны на |cffc8e087+25|cffced4da ед. и скорость регенерации маны на |cffc8e087+20%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДруид-сова|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[27573] = "|cffe4cfa3Магия совы — уровень 2|r"
    wts_updates[27574] = "|cffe4cfa3Магия совы — уровень 2|r"
    wts_updates[27575] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает друидам-совам «Облик совуха», "
        "дополнительно увеличивая здоровье на |cffc8e087+40|cffced4da ед., запас маны на |cffc8e087+25|cffced4da ед. "
        "и регенерацию маны на |cffc8e087+20%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДруид-сова|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0G8", "field": "name1", "expected": wts_updates[27570]})
    checks_def.append({"type": "upgrade", "id": "R0G8", "field": "tip1", "expected": wts_updates[27571]})
    checks_def.append({"type": "upgrade", "id": "R0G8", "field": "ubertip1", "expected": wts_updates[27572]})
    checks_def.append({"type": "upgrade", "id": "R0G8", "field": "name2", "expected": wts_updates[27573]})
    checks_def.append({"type": "upgrade", "id": "R0G8", "field": "tip2", "expected": wts_updates[27574]})
    checks_def.append({"type": "upgrade", "id": "R0G8", "field": "ubertip2", "expected": wts_updates[27575]})

    # R0KS: Зов Элуны (Q)
    wts_updates[12378] = "|cffe4cfa3Зов Элуны|r"
    wts_updates[41894] = "|cffe4cfa3Зов Элуны|r (|cffffffffQ|r)"
    wts_updates[11036] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет союзников благословением богини Луны, "
        "временно повышая скорость атаки и передвижения войск в области действия.|n|n"
        "|cffa6afb8Действует на:|cffced4da войска Ночных эльфов.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0KS", "field": "name1", "expected": wts_updates[12378]})
    checks_def.append({"type": "upgrade", "id": "R0KS", "field": "tip1", "expected": wts_updates[41894]})
    checks_def.append({"type": "upgrade", "id": "R0KS", "field": "ubertip1", "expected": wts_updates[11036]})

    # R0KT: Ярость Элуны (W)
    wts_updates[41846] = "|cffe4cfa3Ярость Элуны|r"
    wts_updates[41897] = "|cffe4cfa3Ярость Элуны|r (|cffffffffW|r)"
    wts_updates[41896] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Посвящает эльфийских воительниц в священный орден Ночных воительниц, "
        "наделяя их оружие дополнительным уроном тёмной лунной энергии.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛучница|cffced4da|n- |cffa9c7deОхотница|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0KT", "field": "name1", "expected": wts_updates[41846]})
    checks_def.append({"type": "upgrade", "id": "R0KT", "field": "tip1", "expected": wts_updates[41897]})
    checks_def.append({"type": "upgrade", "id": "R0KT", "field": "ubertip1", "expected": wts_updates[41896]})

    # R0KU: Слёзы Элуны (E)
    wts_updates[41849] = "|cffe4cfa3Слёзы Элуны|r"
    wts_updates[41850] = "|cffe4cfa3Слёзы Элуны|r (|cffffffffE|r)"
    wts_updates[41848] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует павшим воинам шанс переродиться в виде священных светлячков-огоньков, "
        "возвращая ресурсы и поддерживая жизнь рощи.|n|n"
        "|cffa6afb8Действует на:|cffced4da павших воинов Ночных эльфов.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0KU", "field": "name1", "expected": wts_updates[41849]})
    checks_def.append({"type": "upgrade", "id": "R0KU", "field": "tip1", "expected": wts_updates[41850]})
    checks_def.append({"type": "upgrade", "id": "R0KU", "field": "ubertip1", "expected": wts_updates[41848]})

    # R0CY: Призыв помощи (Q)
    wts_updates[41899] = "|cffe4cfa3Призыв помощи|r"
    wts_updates[31803] = "|cffe4cfa3Призыв помощи|r (|cffffffffQ|r)"
    wts_updates[41901] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Друиды обращаются за поддержкой к Диким Богам Азерота, "
        "призывая защитников чащи на помощь легионам эльфов.|n|n"
        "|cffa6afb8Действует на:|cffced4da силы природы Ночных эльфов.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0CY", "field": "name1", "expected": wts_updates[41899]})
    checks_def.append({"type": "upgrade", "id": "R0CY", "field": "tip1", "expected": wts_updates[31803]})
    checks_def.append({"type": "upgrade", "id": "R0CY", "field": "ubertip1", "expected": wts_updates[41901]})

    # R0KV: Милость Природы (W)
    wts_updates[33342] = "|cffe4cfa3Милость Природы|r"
    wts_updates[33380] = "|cffe4cfa3Милость Природы|r (|cffffffffW|r)"
    wts_updates[35428] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Орошает землю целительным дождём природы, "
        "исцеляющим раненых союзных воинов в выбранной области.|n|n"
        "|cffa6afb8Действует на:|cffced4da союзные войска Ночных эльфов.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0KV", "field": "name1", "expected": wts_updates[33342]})
    checks_def.append({"type": "upgrade", "id": "R0KV", "field": "tip1", "expected": wts_updates[33380]})
    checks_def.append({"type": "upgrade", "id": "R0KV", "field": "ubertip1", "expected": wts_updates[35428]})

    # R0KW: Ярость Природы (E)
    wts_updates[35453] = "|cffe4cfa3Ярость Природы|r"
    wts_updates[35455] = "|cffe4cfa3Ярость Природы|r (|cffffffffE|r)"
    wts_updates[35456] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Призывает в выбранную рощу отряд могучих древней-защитников, "
        "сокрушающих нападающих врагов.|n|n"
        "|cffa6afb8Призывает:|cffced4da лесных древней.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0KW", "field": "name1", "expected": wts_updates[35453]})
    checks_def.append({"type": "upgrade", "id": "R0KW", "field": "tip1", "expected": wts_updates[35455]})
    checks_def.append({"type": "upgrade", "id": "R0KW", "field": "ubertip1", "expected": wts_updates[35456]})

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # A0I3: Небольшой скачок (W)
    wts_updates[26484] = "|cffe4cfa3Небольшой скачок|r"
    wts_updates[10617] = "|cffe4cfa3Небольшой скачок|r (|cffffffffW|r)"
    wts_updates[10618] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает огонька на короткую дистанцию, спасая от преследования.|r"

    # A0FD: Удлинённые мечи
    wts_updates[2917] = "|cffe4cfa3Удлинённые клинки|r"
    wts_updates[2919] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает дальность и ширину поражения клинками в ближнем бою.|r"

    # A0EF: Танец полумесяца
    wts_updates[2731] = "|cffe4cfa3Танец полумесяца|r"
    wts_updates[2733] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff15%|cffced4da при атаке воин совершает стремительный перекат "
        "полумесяцем за спину цели, нанося |cffffffff50%|cffced4da от своего базового урона всем врагам на пути.|r"
    )

    # A0FC: Опутывание
    wts_updates[39686] = "|cffe4cfa3Опутывание|r"
    wts_updates[39687] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки опутывают цель живыми побегами, замедляя скорость передвижения и боя.|r"

    # Acyc: Смерч
    wts_updates[25834] = "|cffe4cfa3Смерч|r"
    wts_updates[27586] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает вражеского воина в воздух вихрем смерча, временно выводя его из сражения.|r"

    # A12K: Рассеивание заклинаний
    wts_updates[24656] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[24657] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[24658] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает положительные эффекты с врагов и отрицательные эффекты с союзников.|r"

    # A16L: Невосприимчивость к магии
    wts_updates[27631] = "|cffe4cfa3Невосприимчивость к магии|r"
    wts_updates[27632] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Полный иммунитет ко всем видам направленных и площадных заклинаний.|r"

    # Amfl: Вспышка маны
    wts_updates[14084] = "|cffe4cfa3Вспышка маны|r"
    wts_updates[14085] = "|cffe4cfa3Вспышка маны|r"
    wts_updates[14086] = "|cffe4cfa3Отменить вспышку маны|r"
    wts_updates[14087] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переходит в энергетический режим, нанося магический урон врагам поблизости при произнесении ими заклинаний.|r"

    # Apsh: Фазовый сдвиг
    wts_updates[15946] = "|cffe4cfa3Фазовый сдвиг|r"
    wts_updates[15948] = "|cffe4cfa3Фазовый сдвиг|r"
    wts_updates[15949] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При получении урона дракончик временно перемещается в другое измерение, избегая атак.|r"

    # A16I: Аннулирование
    wts_updates[8469] = "|cffe4cfa3Аннулирование|r"
    wts_updates[8470] = "|cffe4cfa3Аннулирование|r"
    wts_updates[8473] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Блокирует входящие вражеские заклинания и повышает скорость боя стража.|r"

    # A0FB: Зачарованная глефа
    wts_updates[2909] = "|cffe4cfa3Зачарованная глефа|r"
    wts_updates[2910] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заряжает атаки глефомета или воина дополнительным магическим уроном.|r"

    # A164: Облик совы
    wts_updates[27420] = "|cffe4cfa3Облик совы|r"
    wts_updates[27421] = "|cffe4cfa3Облик совы|r"
    wts_updates[27422] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Трансформирует друида в яростного совуха, усиливая физические параметры.|r"

    # Hero E00V Spells:
    # A0FJ: Сила природы (Q) — 4 уровня
    wts_updates[3524] = "|cffe4cfa3Сила природы|r"
    wts_updates[3431] = "|cffe4cfa3Сила природы — уровень 1|r (|cffffffffQ|r)"
    wts_updates[3432] = "|cffe4cfa3Сила природы — уровень 2|r (|cffffffffQ|r)"
    wts_updates[3440] = "|cffe4cfa3Сила природы — уровень 3|r (|cffffffffQ|r)"
    wts_updates[3441] = "|cffe4cfa3Сила природы — уровень 4|r (|cffffffffQ|r)"
    wts_updates[3442] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает указанную рощу деревьев в отряд из |cffffffff2|cffced4da верных древней-защитников на |cffffffff60|cffced4da сек.|r"
    wts_updates[3443] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает указанную рощу деревьев в отряд из |cffffffff3|cffced4da верных древней-защитников на |cffffffff60|cffced4da сек.|r"
    wts_updates[3522] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает указанную рощу деревьев в отряд из |cffffffff4|cffced4da верных древней-защитников на |cffffffff60|cffced4da сек.|r"
    wts_updates[3523] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает указанную рощу деревьев в отряд из |cffffffff5|cffced4da верных древней-защитников на |cffffffff60|cffced4da сек.|r"

    # A0FH: Замедляющие корни (R) — 4 уровня
    wts_updates[14273] = "|cffe4cfa3Замедляющие корни|r"
    wts_updates[14275] = "|cffe4cfa3Замедляющие корни — уровень 1|r"
    wts_updates[14322] = "|cffe4cfa3Замедляющие корни — уровень 2|r"
    wts_updates[14391] = "|cffe4cfa3Замедляющие корни — уровень 3|r"
    wts_updates[14393] = "|cffe4cfa3Замедляющие корни — уровень 4|r"
    wts_updates[2916] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака опутывает врага корнями, замедляя бег на |cffe69a8d15%|cffced4da и скорость боя на |cffe69a8d10%|cffced4da на |cffffffff3|cffced4da сек.|r"
    wts_updates[3229] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака опутывает врага корнями, замедляя бег на |cffe69a8d25%|cffced4da и скорость боя на |cffe69a8d15%|cffced4da на |cffffffff3|cffced4da сек.|r"
    wts_updates[3297] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака опутывает врага корнями, замедляя бег на |cffe69a8d35%|cffced4da и скорость боя на |cffe69a8d20%|cffced4da на |cffffffff3|cffced4da сек.|r"
    wts_updates[3298] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака опутывает врага корнями, замедляя бег на |cffe69a8d45%|cffced4da и скорость боя на |cffe69a8d25%|cffced4da на |cffffffff3|cffced4da сек.|r"

    # A0FI: Аура шипов (E) — 4 уровня
    wts_updates[3300] = "|cffe4cfa3Аура шипов|r"
    wts_updates[3341] = "|cffe4cfa3Аура шипов — уровень 1|r"
    wts_updates[3342] = "|cffe4cfa3Аура шипов — уровень 2|r"
    wts_updates[3427] = "|cffe4cfa3Аура шипов — уровень 3|r"
    wts_updates[3429] = "|cffe4cfa3Аура шипов — уровень 4|r"
    wts_updates[3430] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзников барьером из острых шипов, отражающим входящий урон ближнего боя обратно в атакующих.|r"

    # ken0: Ярость природы (R) — 2 уровня
    wts_updates[26390] = "|cffe4cfa3Ярость природы|r"
    wts_updates[30523] = "|cffe4cfa3Ярость природы — уровень 1|r (|cffffffffR|r)"
    wts_updates[40189] = "|cffe4cfa3Ярость природы — уровень 2|r (|cffffffffR|r)"
    wts_updates[40192] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взывает к гневу леса, опутывая корнями и оглушая наземных врагов в большой области с нанесением урона.|r"
    wts_updates[40193] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взывает к гневу леса, опутывая корнями и оглушая наземных врагов в большой области с нанесением сокрушительного урона.|r"

    # A1MW: Оплетение
    wts_updates[11596] = "|cffe4cfa3Оплетение|r"
    wts_updates[11597] = "|cffe4cfa3Оплетение|r"
    wts_updates[11598] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывает цель корнями, обездвиживая и нанося периодический урон.|r"

    # A160, A161: Покровительство друидов
    wts_updates[14835] = "|cffe4cfa3Покровительство друидов|r"
    wts_updates[27376] = "|cffe4cfa3Покровительство друидов — уровень 1|r"
    wts_updates[27377] = "|cffe4cfa3Покровительство друидов — уровень 2|r"
    wts_updates[27378] = "|cffe4cfa3Покровительство друидов — уровень 3|r"
    wts_updates[27380] = "|cffe4cfa3Покровительство друидов — уровень 4|r"
    wts_updates[27381] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает регенерацию маны и силу заклинаний друидов.|r"
    wts_updates[27382] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает регенерацию маны и силу заклинаний друидов.|r"
    wts_updates[27383] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает регенерацию маны и силу заклинаний друидов.|r"
    wts_updates[27384] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает регенерацию маны и силу заклинаний друидов.|r"
    wts_updates[27379] = "|cffe4cfa3Покровительство друидов|r"

    # Hero E011 Spells:
    # A0FL: Взрыв маны (Q) — 4 уровня
    wts_updates[3899] = "|cffe4cfa3Взрыв маны|r"
    wts_updates[4357] = "|cffe4cfa3Взрыв маны — уровень 1|r (|cffffffffQ|r)"
    wts_updates[4358] = "|cffe4cfa3Взрыв маны — уровень 2|r (|cffffffffQ|r)"
    wts_updates[4406] = "|cffe4cfa3Взрыв маны — уровень 3|r (|cffffffffQ|r)"
    wts_updates[4614] = "|cffe4cfa3Взрыв маны — уровень 4|r (|cffffffffQ|r)"
    wts_updates[4617] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область сгустками маны, нанося урон наземным врагам и оглушая их на |cffffffff1|cffced4da сек.|r"
    wts_updates[4627] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область сгустками маны, нанося урон наземным врагам и оглушая их на |cffffffff1.5|cffced4da сек.|r"
    wts_updates[4628] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область сгустками маны, нанося урон наземным врагам и оглушая их на |cffffffff2|cffced4da сек.|r"
    wts_updates[4631] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область сгустками маны, нанося урон наземным врагам и оглушая их на |cffffffff2.5|cffced4da сек.|r"

    # A0FQ: Ледяные стрелы (W) — 4 уровня
    wts_updates[4662] = "|cffe4cfa3Ледяные стрелы|r"
    wts_updates[4664] = "|cffe4cfa3Ледяные стрелы — уровень 1|r (|cffffffffW|r)"
    wts_updates[4923] = "|cffe4cfa3Ледяные стрелы — уровень 2|r (|cffffffffW|r)"
    wts_updates[4924] = "|cffe4cfa3Ледяные стрелы — уровень 3|r (|cffffffffW|r)"
    wts_updates[4925] = "|cffe4cfa3Ледяные стрелы — уровень 4|r (|cffffffffW|r)"
    wts_updates[4926] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заряжает стрелы холодом, нанося дополнительный урон и замедляя скорость атаки и бега цели.|r"

    # A0FS: Аура меткости (E) — 4 уровня
    wts_updates[4968] = "|cffe4cfa3Аура меткости|r"
    wts_updates[5625] = "|cffe4cfa3Аура меткости — уровень 4|r"
    wts_updates[5626] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон всех союзных стрелков дальнего боя поблизости.|r"

    # A0FT: Смертельный выстрел (R) — 2 уровня
    wts_updates[5023] = "|cffe4cfa3Смертельный выстрел|r"
    wts_updates[5048] = "|cffe4cfa3Смертельный выстрел — уровень 1|r (|cffffffffR|r)"
    wts_updates[5049] = "|cffe4cfa3Смертельный выстрел — уровень 2|r (|cffffffffR|r)"
    wts_updates[5050] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелу невероятной силы, пронзающую всех наземных врагов на прямой линии с высоким уроном.|r"
    wts_updates[5051] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелу невероятной силы, пронзающую всех наземных врагов на прямой линии с колоссальным уроном.|r"

    # Hero E00W Spells:
    # AEbl: Скачок (W)
    wts_updates[25764] = "|cffe4cfa3Скачок|r"
    wts_updates[9615] = "|cffe4cfa3Скачок — уровень 4|r (|cffffffffW|r)"
    wts_updates[9616] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит друида на короткое расстояние, позволяя вступить в бой или уйти от опасности.|r"

    # ANfl: Раздвоенная молния (Q)
    wts_updates[21406] = "|cffe4cfa3Раздвоенная молния — уровень 4|r (|cffffffffQ|r)"
    wts_updates[27563] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цепью молний до |cffffffff10|cffced4da врагов в конусе перед собой, нанося |cffffffff300|cffced4da урона.|r"

    # AEev: Ускользание (E) — 4 уровня
    wts_updates[5770] = "|cffe4cfa3Ускользание|r"
    wts_updates[10941] = "|cffe4cfa3Ускользание — уровень 1|r"
    wts_updates[8771] = "|cffe4cfa3Ускользание — уровень 2|r"
    wts_updates[8772] = "|cffe4cfa3Ускользание — уровень 3|r"
    wts_updates[8775] = "|cffe4cfa3Ускользание — уровень 4|r"
    wts_updates[11335] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffc8e08710%|cffced4da уклониться от вражеской физической атаки.|r"
    wts_updates[8780] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffc8e08720%|cffced4da уклониться от вражеской физической атаки.|r"
    wts_updates[9392] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffc8e08730%|cffced4da уклониться от вражеской физической атаки.|r"
    wts_updates[12243] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffc8e08740%|cffced4da уклониться от вражеской физической атаки.|r"

    # A0FM: Облик совухи (R) — 2 уровня
    wts_updates[4379] = "|cffe4cfa3Облик совухи|r"
    wts_updates[4666] = "|cffe4cfa3Облик совухи — уровень 1|r (|cffffffffR|r)"
    wts_updates[4667] = "|cffe4cfa3Облик совухи — уровень 2|r (|cffffffffR|r)"
    wts_updates[4615] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает друида в могучего совуха, увеличивая броню и урон в ближнем бою.|r"
    wts_updates[4669] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает друида в могучего совуха, значительно увеличивая броню и урон в ближнем бою.|r"

    # A01C: Свечение героя
    wts_updates[2038] = "|cffe4cfa3Свечение героя|r"
    wts_updates[2039] = "|cffe4cfa3Свечение героя|r"

    # System capital abilities
    wts_updates[12857] = "|cffe4cfa3Обмен древесины на золото|r"
    wts_updates[12858] = "|cffe4cfa3Обмен древесины на золото|r"
    wts_updates[12859] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обменивает запас древесины на золото в государственной казне.|r"

    wts_updates[2888] = "|cffe4cfa3Обмен золота на древесину|r"
    wts_updates[2889] = "|cffe4cfa3Обмен золота на древесину|r"
    wts_updates[2890] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обменивает золото на древесину в государственной казне.|r"

    wts_updates[27193] = "|cffe4cfa3Обозначить столицу|r"
    wts_updates[27191] = "|cffe4cfa3Обозначить столицу|r"
    wts_updates[27192] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Провозглашает главное древо официальной столицей государства Ночных эльфов.|r"

    # A15N: Зона ремонта
    wts_updates[25578] = "|cffe4cfa3Зона ремонта|r"
    wts_updates[25579] = "|cffe4cfa3Зона ремонта|r"
    wts_updates[25580] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Автоматически восстанавливает прочность находящихся рядом кораблей.|r"

    # =========================================================================
    # CATEGORIES
    # =========================================================================
    plan = {
        "race": "Ночные эльфы (Night Elf)",
        "race_id": 26,
        "selection": {
            "ability_id": "A0HL",
            "marker_id": "R07L"
        },
        "categories": {
            "buildings": [
                "etol", "etoa", "etoe", "emow", "eaom", "eate", "eaow", "eaoe",
                "edob", "etrp", "edos", "e03X", "e03W", "h0D8"
            ],
            "units": [
                "ewsp", "earc", "esen", "ebal", "e00I", "e00J", "n05H", "edot",
                "efdr", "e00H", "n064", "edry", "edoc", "emtg", "n05D", "n05G",
                "h0D9", "h0DB", "h0DA"
            ],
            "heroes": [
                "E00V", "E011", "E00W"
            ],
            "research": [
                "R07L", "Renb", "R0G1", "R0G2", "R0GB", "Resm", "Rema", "Resw",
                "Rerh", "Reuv", "Rews", "Resc", "R0GC", "Reib", "Remk", "Remg",
                "Repb", "R0GA", "R0G9", "R0G7", "Redt", "Reec", "R0G6", "Redc",
                "Reeb", "Resi", "Rers", "Rehs", "R0G8", "R0KS", "R0KT", "R0KU",
                "R0CY", "R0KV", "R0KW"
            ],
            "abilities": [
                "A0HL", "A0I3", "A0FD", "A0EF", "A0FC", "Acyc", "A12K", "A16L",
                "Amfl", "Apsh", "A16I", "A0FB", "A164", "A0FJ", "A0FH", "A0FI",
                "ken0", "A1MW", "A160", "A161", "A0FL", "A0FQ", "A0FS", "A0FT",
                "AEbl", "ANfl", "AEev", "A0FM", "A01C", "A0LJ", "A0LI", "A0IQ", "A15N"
            ]
        },
        "wts_updates": wts_updates,
        "checks_def": checks_def
    }

    out_file = folder / "nightelf_plan.json"
    out_file.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {out_file} with {len(wts_updates)} updates and {len(checks_def)} checks.")

if __name__ == '__main__':
    main()
