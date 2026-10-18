# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Race 35: Horde of the Second War (HordeW2)."""
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
    # 1. RACE SELECTION & MARKERS: A1JN, R0KB, R0KC, R0KD
    # =========================================================================
    # A1JN (Орда Второй Войны, Z)
    wts_updates[26684] = "|cffe4cfa3Орда Второй Войны|r"
    wts_updates[35847] = "|cffe4cfa3Орда Второй Войны|r (|cffffffffZ|r)"
    wts_updates[25701] = (
        "|cffa6afb8РАСА:|cffced4da Могущественная армия союза орков, огров, троллей и гоблинов времен Второй Войны, опирающаяся на ветеранский опыт войск, тяжелую осадную мощь и подчиненных красных драконов.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Warcraft II: Tides of Darkness»|r|n|n"
        "|cffced4daВ последние дни Первой Войны колдун Гул'дан впал в глубокую кому, пытаясь проникнуть в разум Медива. "
        "Воспользовавшись этим, Оргрим Молот Рока возглавил переворот, уничтожил Теневой Совет и сразил Чернорука Разрушителя, взяв верховное командование над Ордой. "
        "Объединив кланы орков, лесных троллей, двухголовых огров и предприимчивых гоблинов, Орда хлынула через Тёмный Портал в Лордерон. "
        "С помощью могущественного артефакта Души Демона клан Драконьей Пасти поработил Королеву Драконов Алекстразу, поставив гигантских красных драконов на службу новой непобедимой военной машине.|r"
    )
    checks_def.append({"type": "ability", "id": "A1JN", "field": "name", "expected": wts_updates[26684]})
    checks_def.append({"type": "ability", "id": "A1JN", "field": "tip1", "expected": wts_updates[35847]})
    checks_def.append({"type": "ability", "id": "A1JN", "field": "ubertip1", "expected": wts_updates[25701]})

    # Marker: R0KB
    wts_updates[32677] = "|cffe4cfa3Орда Второй Войны|r"
    wts_updates[32678] = "|cffe4cfa3Орда Второй Войны|r"
    checks_def.append({"type": "upgrade", "id": "R0KB", "field": "name1", "expected": wts_updates[32677]})
    checks_def.append({"type": "upgrade", "id": "R0KB", "field": "tip1", "expected": wts_updates[32678]})

    # Marker: R0KC
    wts_updates[5595] = "|cffe4cfa3Орда Скверны или Орда Второй Войны|r"
    wts_updates[5596] = "|cffe4cfa3Орда Скверны или Орда Второй Войны|r"
    wts_updates[27305] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер выбора между Ордой Скверны и Ордой Второй Войны.|r"
    checks_def.append({"type": "upgrade", "id": "R0KC", "field": "name1", "expected": wts_updates[5595]})
    checks_def.append({"type": "upgrade", "id": "R0KC", "field": "tip1", "expected": wts_updates[5596]})
    checks_def.append({"type": "upgrade", "id": "R0KC", "field": "ubertip1", "expected": wts_updates[27305]})

    # Marker: R0KD
    wts_updates[5598] = "|cffe4cfa3Культ Сумеречного Молота|r"
    wts_updates[5599] = "|cffe4cfa3Культ Сумеречного Молота|r"
    wts_updates[37033] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер выбора ветви развития Культа Сумеречного Молота.|r"
    checks_def.append({"type": "upgrade", "id": "R0KD", "field": "name1", "expected": wts_updates[5598]})
    checks_def.append({"type": "upgrade", "id": "R0KD", "field": "tip1", "expected": wts_updates[5599]})
    checks_def.append({"type": "upgrade", "id": "R0KD", "field": "ubertip1", "expected": wts_updates[37033]})

    # =========================================================================
    # 2. BUILDINGS (13 buildings)
    # =========================================================================
    # w20q: Дом вождей (Q)
    wts_updates[11791] = "|cffe4cfa3Дом вождей|r"
    wts_updates[11792] = "|cffe4cfa3Дом вождей|r (|cffffffffQ|r)"
    wts_updates[29700] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание первой ступени. Обеспечивает добычу ресурсов, начальный запас пищи и доступ к базовым сооружениям.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБатрак|cffced4da: базовый рабочий, строитель и добытчик ресурсов.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deВоенная экспертиза|cffced4da: повышает начальный опыт и боевые характеристики войск.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКрепость|cffced4da: открывает доступ к передовым сооружениям и технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "w20q", "field": "name", "expected": wts_updates[11791]})
    checks_def.append({"type": "unit", "id": "w20q", "field": "tip", "expected": wts_updates[11792]})
    checks_def.append({"type": "unit", "id": "w20q", "field": "ubertip", "expected": wts_updates[29700]})

    # w20w: Крепость (U)
    wts_updates[11793] = "|cffe4cfa3Крепость|r"
    wts_updates[11794] = "|cffe4cfa3Крепость|r (|cffffffffU|r)"
    checks_def.append({"type": "unit", "id": "w20w", "field": "name", "expected": wts_updates[11793]})
    checks_def.append({"type": "unit", "id": "w20w", "field": "tip", "expected": wts_updates[11794]})

    # w20e: Цитадель (U)
    wts_updates[11795] = "|cffe4cfa3Цитадель|r"
    wts_updates[11814] = "|cffe4cfa3Цитадель|r (|cffffffffU|r)"
    checks_def.append({"type": "unit", "id": "w20e", "field": "name", "expected": wts_updates[11795]})
    checks_def.append({"type": "unit", "id": "w20e", "field": "tip", "expected": wts_updates[11814]})

    # w20r: Казармы (W)
    wts_updates[11815] = "|cffe4cfa3Казармы|r"
    wts_updates[11816] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[29730] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Основное военное сооружение для подготовки пехоты и стрелков Орды.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРубака|cffced4da: стойкий орк-пехотинец ближнего боя.|n"
        "- |cffa9c7deМетатель топоров|cffced4da: лесной тролль дальнего боя.|n"
        "- |cffa9c7deОгр-воин|cffced4da: тяжелый двухголовый исполин ближнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deТренировки рубак|cffced4da: увеличивает запас здоровья и урон рубак.|n"
        "- |cffa9c7deТренировки огров|cffced4da: повышает запас здоровья огров.|n"
        "- |cffa9c7deТренировки метателей|cffced4da: увеличивает запас здоровья и дальность атаки метателей.|n"
        "- |cffa9c7deЗачарованные топоры|cffced4da: позволяет топорам отскакивать в дополнительные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w20r", "field": "name", "expected": wts_updates[11815]})
    checks_def.append({"type": "unit", "id": "w20r", "field": "tip", "expected": wts_updates[11816]})
    checks_def.append({"type": "unit", "id": "w20r", "field": "ubertip", "expected": wts_updates[29730]})

    # w20y: Свиноферма (A)
    wts_updates[11819] = "|cffe4cfa3Свиноферма|r"
    wts_updates[11820] = "|cffe4cfa3Свиноферма|r (|cffffffffA|r)"
    wts_updates[29732] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Орды провизией и увеличивает лимит войск.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "w20y", "field": "name", "expected": wts_updates[11819]})
    checks_def.append({"type": "unit", "id": "w20y", "field": "tip", "expected": wts_updates[11820]})
    checks_def.append({"type": "unit", "id": "w20y", "field": "ubertip", "expected": wts_updates[29732]})

    # w214: Лесопилка (E)
    wts_updates[11885] = "|cffe4cfa3Лесопилка|r"
    wts_updates[11886] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[29960] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр сбора древесины и улучшения экипировки армии Орды.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКрепкая броня|cffced4da: повышает защиту наземных войск Орды.|n"
        "- |cffa9c7deОружие ближнего боя|cffced4da: увеличивает урон воинов ближнего боя.|n"
        "- |cffa9c7deОружие дальнего боя|cffced4da: увеличивает урон стрелков.|n"
        "- |cffa9c7deУлучшенные пилы|cffced4da: повышает вместимость добываемой батраками древесины.|r"
    )
    checks_def.append({"type": "unit", "id": "w214", "field": "name", "expected": wts_updates[11885]})
    checks_def.append({"type": "unit", "id": "w214", "field": "tip", "expected": wts_updates[11886]})
    checks_def.append({"type": "unit", "id": "w214", "field": "ubertip", "expected": wts_updates[29960]})

    # w20a: Алтарь бури (S)
    wts_updates[11824] = "|cffe4cfa3Алтарь бури|r"
    wts_updates[11825] = "|cffe4cfa3Алтарь бури|r (|cffffffffS|r)"
    wts_updates[29734] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище предков и темных сил. Позволяет призывать легендарных вождей Орды и воскрешать павших героев.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deВождь Клана|cffced4da: могучий вождь ближнего боя.|n"
        "- |cffa9c7deСумеречный маг|cffced4da: двухголовый чернокнижник дальнего боя.|n"
        "- |cffa9c7deПредводитель троллей|cffced4da: смертоносный следопыт дальнего боя.|n"
        "- |cffa9c7deМэйм Блэкхенд|cffced4da: свирепый мастер клинка.|r"
    )
    checks_def.append({"type": "unit", "id": "w20a", "field": "name", "expected": wts_updates[11824]})
    checks_def.append({"type": "unit", "id": "w20a", "field": "tip", "expected": wts_updates[11825]})
    checks_def.append({"type": "unit", "id": "w20a", "field": "ubertip", "expected": wts_updates[29734]})

    # w20u: Сторожевая башня (Z)
    wts_updates[11822] = "|cffe4cfa3Сторожевая башня|r"
    wts_updates[11823] = "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)"
    wts_updates[29733] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое оборонительное сооружение Орды. Оснащено копьемётами для отражения вражеских атак с суши и воздуха.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w20u", "field": "name", "expected": wts_updates[11822]})
    checks_def.append({"type": "unit", "id": "w20u", "field": "tip", "expected": wts_updates[11823]})
    checks_def.append({"type": "unit", "id": "w20u", "field": "ubertip", "expected": wts_updates[29733]})

    # w20t: Тёмный храм (R)
    wts_updates[69] = "|cffe4cfa3Тёмный храм|r"
    wts_updates[70] = "|cffe4cfa3Тёмный храм|r (|cffffffffR|r)"
    wts_updates[29731] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Цитадель тёмных искусств и некромантии. Готовит могущественных колдунов и жрецов Орды.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРыцарь смерти|cffced4da: конный некромант, повелитель тёмной магии.|n"
        "- |cffa9c7deЖрец|cffced4da: священнослужитель троллей, лекарь и рассеиватель чар.|n"
        "- |cffa9c7deОгр-маг|cffced4da: двухголовый заклинатель, усиливающий союзников жаждой крови.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЧародейства огров|cffced4da: повышает здоровье, запас маны и открывает руны огров-магов.|n"
        "- |cffa9c7deРитуалы смерти|cffced4da: развивает некромантию и тёмные заклятия рыцарей смерти.|n"
        "- |cffa9c7deКолдовство вуду|cffced4da: увеличивает магический потенциал и силы жрецов.|r"
    )
    checks_def.append({"type": "unit", "id": "w20t", "field": "name", "expected": wts_updates[69]})
    checks_def.append({"type": "unit", "id": "w20t", "field": "tip", "expected": wts_updates[70]})
    checks_def.append({"type": "unit", "id": "w20t", "field": "ubertip", "expected": wts_updates[29731]})

    # w20i: Гоблинская лаборатория (D)
    wts_updates[11889] = "|cffe4cfa3Гоблинская лаборатория|r"
    wts_updates[11890] = "|cffe4cfa3Гоблинская лаборатория|r (|cffffffffD|r)"
    wts_updates[29961] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Мастерская гоблинских инженеров и алхимиков Орды.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deКатапульта|cffced4da: дальнобойное осадное орудие.|n"
        "- |cffa9c7deДирижабль|cffced4da: летающий транспорт и воздушный бомбардир.|n"
        "- |cffa9c7deПодрывной отряд|cffced4da: гоблины-саперы для подрыва зданий и укреплений.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКомплектование дирижаблей|cffced4da: увеличивает шанс спасения пехоты и оснащает дирижабли ракетами.|n"
        "- |cffa9c7deЗаряды взрыводия|cffced4da: повышает разрушительную мощь и радиус подрывных отрядов.|r"
    )
    checks_def.append({"type": "unit", "id": "w20i", "field": "name", "expected": wts_updates[11889]})
    checks_def.append({"type": "unit", "id": "w20i", "field": "tip", "expected": wts_updates[11890]})
    checks_def.append({"type": "unit", "id": "w20i", "field": "ubertip", "expected": wts_updates[29961]})

    # w210: Логово красных драконов (F)
    wts_updates[11829] = "|cffe4cfa3Логово красных драконов|r"
    wts_updates[11830] = "|cffe4cfa3Логово красных драконов|r (|cffffffffF|r)"
    wts_updates[29740] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Загон клана Драконьей Пасти, в котором содержатся порабощенные красные драконы.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deКрасный дракон|cffced4da: могучий огнедышащий исполин небес.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deРазведение драконов|cffced4da: повышает дальность атаки и запас здоровья драконов.|r"
    )
    checks_def.append({"type": "unit", "id": "w210", "field": "name", "expected": wts_updates[11829]})
    checks_def.append({"type": "unit", "id": "w210", "field": "tip", "expected": wts_updates[11830]})
    checks_def.append({"type": "unit", "id": "w210", "field": "ubertip", "expected": wts_updates[29740]})

    # w218: Верфь (C)
    wts_updates[22656] = "|cffe4cfa3Верфь|r"
    wts_updates[22661] = "|cffe4cfa3Верфь|r (|cffffffffC|r)"
    wts_updates[28309] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Прибрежная верфь для строительства военного флота и добычи нефти.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deНефтяной танкер|cffced4da: корабль для освоения нефтяных месторождений.|n"
        "- |cffa9c7deТранспорт|cffced4da: судно для перевозки сухопутных войск.|n"
        "- |cffa9c7deФрегат|cffced4da: легкий патрульный боевой корабль.|n"
        "- |cffa9c7deДредноут|cffced4da: тяжелый бронированный флагман флота.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОрудия флота|cffced4da: повышает урон кораблей.|n"
        "- |cffa9c7deУкреплённый корпус|cffced4da: увеличивает запас здоровья и броню флота.|r"
    )
    checks_def.append({"type": "unit", "id": "w218", "field": "name", "expected": wts_updates[22656]})
    checks_def.append({"type": "unit", "id": "w218", "field": "tip", "expected": wts_updates[22661]})
    checks_def.append({"type": "unit", "id": "w218", "field": "ubertip", "expected": wts_updates[28309]})

    # w219: Нефтяная платформа (Q)
    wts_updates[22670] = "|cffe4cfa3Нефтяная платформа|r"
    wts_updates[22676] = "|cffe4cfa3Нефтяная платформа|r (|cffffffffQ|r)"
    wts_updates[22678] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Морская добывающая платформа, возводимая нефтяными танкерами над месторождениями нефти.|n|n"
        "Даёт постоянный прирост золота в казну Орды.|r"
    )
    checks_def.append({"type": "unit", "id": "w219", "field": "name", "expected": wts_updates[22670]})
    checks_def.append({"type": "unit", "id": "w219", "field": "tip", "expected": wts_updates[22676]})
    checks_def.append({"type": "unit", "id": "w219", "field": "ubertip", "expected": wts_updates[22678]})

    # =========================================================================
    # 3. HEROES (4 heroes: W200, W201, W202, W203)
    # =========================================================================
    # W200: Вождь Клана (Оргрим Молот Рока, Z)
    wts_updates[11863] = "|cffe4cfa3Вождь Клана|r"
    wts_updates[11867] = "|cffe4cfa3Вождь Клана|r (|cffffffffZ|r)"
    wts_updates[11864] = "Мэйм, Некрош, Ренд"
    wts_updates[11865] = "|cffe4cfa3Вождь Клана|r"
    wts_updates[11866] = "|cffe4cfa3Вождь Клана|r (|cffffffffZ|r)"
    wts_updates[29891] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могущественный вождь Орды ближнего боя. Вдохновляет войско несокрушимой стойкостью и сокрушает вражеские ряды разрушительными ударами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВихрь клинков|cffced4da: мастерское вращение с оружием, наносящее урон окружающим врагам.|n"
        "- |cffa9c7deАура выносливости|cffced4da: пассивно увеличивает скорость атаки и передвижения союзников.|n"
        "- |cffa9c7deДержать строй|cffced4da: временно повышает броню и регенерацию здоровья союзных воинов.|n"
        "- |cffa9c7deРезня слабаков|cffced4da: особая способность, многократно умножающая урон по обычным юнитам.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "W200", "field": "name", "expected": wts_updates[11863]})
    checks_def.append({"type": "unit", "id": "W200", "field": "tip", "expected": wts_updates[11867]})
    checks_def.append({"type": "unit", "id": "W200", "field": "propernames", "expected": wts_updates[11864]})
    checks_def.append({"type": "unit", "id": "W200", "field": "awakentip", "expected": wts_updates[11865]})
    checks_def.append({"type": "unit", "id": "W200", "field": "revivetip", "expected": wts_updates[11866]})
    checks_def.append({"type": "unit", "id": "W200", "field": "ubertip", "expected": wts_updates[29891]})

    # W201: Сумеречный маг (Чо'Галл, C)
    wts_updates[11874] = "|cffe4cfa3Сумеречный маг|r"
    wts_updates[11879] = "|cffe4cfa3Сумеречный маг|r (|cffffffffC|r)"
    wts_updates[11876] = "Горлоп, Оммок, Дентарг"
    wts_updates[11877] = "|cffe4cfa3Сумеречный маг|r"
    wts_updates[11878] = "|cffe4cfa3Сумеречный маг|r (|cffffffffC|r)"
    wts_updates[29958] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Двухголовый огр-чернокнижник дальнего боя. Черпает мощь Бездны, подавляя волю врагов ужасом и разрушительными чарами развоплощения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСтрелы тьмы|cffced4da: залп теневых сгустков по конусу перед заклинателем.|n"
        "- |cffa9c7deАура гениальности|cffced4da: пассивно ускоряет восстановление маны окружающих союзников.|n"
        "- |cffa9c7deПоле развоплощения|cffced4da: поддерживаемая зона искажения пространства, наносящая урон и замедляющая врагов.|n"
        "- |cffa9c7deСтрах|cffced4da: особая способность, повергающая врагов в панику и лишающая возможности атаковать.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "W201", "field": "name", "expected": wts_updates[11874]})
    checks_def.append({"type": "unit", "id": "W201", "field": "tip", "expected": wts_updates[11879]})
    checks_def.append({"type": "unit", "id": "W201", "field": "propernames", "expected": wts_updates[11876]})
    checks_def.append({"type": "unit", "id": "W201", "field": "awakentip", "expected": wts_updates[11877]})
    checks_def.append({"type": "unit", "id": "W201", "field": "revivetip", "expected": wts_updates[11878]})
    checks_def.append({"type": "unit", "id": "W201", "field": "ubertip", "expected": wts_updates[29958]})

    # W202: Предводитель троллей (Зул'джин, X)
    wts_updates[11880] = "|cffe4cfa3Предводитель троллей|r"
    wts_updates[11884] = "|cffe4cfa3Предводитель троллей|r (|cffffffffX|r)"
    wts_updates[11881] = "Зул'джин, Каз'каг, Вульджин"
    wts_updates[11882] = "|cffe4cfa3Предводитель троллей|r"
    wts_updates[11883] = "|cffe4cfa3Предводитель троллей|r (|cffffffffX|r)"
    wts_updates[29959] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Ловкий предводитель лесных троллей дальнего боя. Ведёт огонь смертоносными топорами, вдохновляет стрелков и отравляет вражескую броню едкой кислотой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМетание топоров|cffced4da: поражает топорами каждого вражеского юнита в выбранной области.|n"
        "- |cffa9c7deЯрость берсерка|cffced4da: значительно ускоряет атаку героя на время действия.|n"
        "- |cffa9c7deАура меткости|cffced4da: пассивно повышает урон дальнобойных атак союзников.|n"
        "- |cffa9c7deРазъедающее зелье|cffced4da: особая способность, разрушающая броню и наносящая периодический урон кислотой.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "W202", "field": "name", "expected": wts_updates[11880]})
    checks_def.append({"type": "unit", "id": "W202", "field": "tip", "expected": wts_updates[11884]})
    checks_def.append({"type": "unit", "id": "W202", "field": "propernames", "expected": wts_updates[11881]})
    checks_def.append({"type": "unit", "id": "W202", "field": "awakentip", "expected": wts_updates[11882]})
    checks_def.append({"type": "unit", "id": "W202", "field": "revivetip", "expected": wts_updates[11883]})
    checks_def.append({"type": "unit", "id": "W202", "field": "ubertip", "expected": wts_updates[29959]})

    # =========================================================================
    # 4. UNITS (21 units)
    # =========================================================================
    # w200: Батрак (Q)
    wts_updates[11731] = "|cffe4cfa3Батрак|r"
    wts_updates[11745] = "|cffe4cfa3Батрак|r (|cffffffffQ|r)"
    wts_updates[29074] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Орды. Добывает золото и древесину, возводит и ремонтирует здания.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: получает опыт в бою и труде, повышая наносимый урон до |cffc8e087+30%|cffced4da.|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткое расстояние к ресурсам или зданиям.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w200", "field": "name", "expected": wts_updates[11731]})
    checks_def.append({"type": "unit", "id": "w200", "field": "tip", "expected": wts_updates[11745]})
    checks_def.append({"type": "unit", "id": "w200", "field": "ubertip", "expected": wts_updates[29074]})

    # w208: Рубака (Q)
    wts_updates[11787] = "|cffe4cfa3Рубака|r"
    wts_updates[11788] = "|cffe4cfa3Рубака|r (|cffffffffQ|r)"
    wts_updates[29535] = (
        "|cffa6afb8ЮНИТ:|cffced4da Выносливый орк-воин ближнего боя. Составляет основу ударной пехоты Орды.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: накапливает боевой опыт, увеличивая урон до |cffc8e087+30%|cffced4da.|n"
        "- |cffa9c7deЯрость|cffced4da: после исследования на |cffffffff9|cffced4da сек. увеличивает скорость атаки на |cffc8e087+20%|cffced4da и скорость бега на |cffc8e087+15%|cffced4da.|n"
        "- |cffa9c7deОтработанные навыки|cffced4da: после исследования дарует |cffffffff5%|cffced4da шанс уклонения и |cffffffff5%|cffced4da шанс критического удара.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w208", "field": "name", "expected": wts_updates[11787]})
    checks_def.append({"type": "unit", "id": "w208", "field": "tip", "expected": wts_updates[11788]})
    checks_def.append({"type": "unit", "id": "w208", "field": "ubertip", "expected": wts_updates[29535]})

    # w203: Метатель топоров (W)
    wts_updates[11750] = "|cffe4cfa3Метатель топоров|r"
    wts_updates[11751] = "|cffe4cfa3Метатель топоров|r (|cffffffffW|r)"
    wts_updates[29276] = (
        "|cffa6afb8ЮНИТ:|cffced4da Меткий лесной тролль дальнего боя, вооруженный метательными топорами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: боевой ветеранский опыт увеличивает урон до |cffc8e087+30%|cffced4da.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w203", "field": "name", "expected": wts_updates[11750]})
    checks_def.append({"type": "unit", "id": "w203", "field": "tip", "expected": wts_updates[11751]})
    checks_def.append({"type": "unit", "id": "w203", "field": "ubertip", "expected": wts_updates[29276]})

    # w204: Огр-воин (E)
    wts_updates[11752] = "|cffe4cfa3Огр-воин|r"
    wts_updates[11753] = "|cffe4cfa3Огр-воин|r (|cffffffffE|r)"
    wts_updates[29277] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелый пехотинец Орды с огромным запасом здоровья и разрушительным уроном.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: накапливает опыт в сражениях, повышая урон до |cffc8e087+30%|cffced4da.|n"
        "- |cffa9c7deСильный удар|cffced4da: с вероятностью |cffffffff15%|cffced4da наносит дополнительный урон и оглушает цель.|n"
        "- |cffa9c7deСопротивление магии|cffced4da: после исследования получает лишь |cffffffff35%|cffced4da урона от вражеских заклинаний.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w204", "field": "name", "expected": wts_updates[11752]})
    checks_def.append({"type": "unit", "id": "w204", "field": "tip", "expected": wts_updates[11753]})
    checks_def.append({"type": "unit", "id": "w204", "field": "ubertip", "expected": wts_updates[29277]})

    # w209: Рыцарь смерти (E)
    wts_updates[11789] = "|cffe4cfa3Рыцарь смерти|r"
    wts_updates[11790] = "|cffe4cfa3Рыцарь смерти|r (|cffffffffE|r)"
    wts_updates[29662] = (
        "|cffa6afb8ЮНИТ:|cffced4da Конный колдун Орды дальнего боя, черпающий силу в некромантии и магии смерти.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: повышает урон атак до |cffc8e087+30%|cffced4da с ростом ранга ветерана.|n"
        "- |cffa9c7deПохищение жизни|cffced4da: вытягивает |cffffffff45|cffced4da ед. здоровья в секунду из врага.|n"
        "- |cffa9c7deТёмный доспех|cffced4da: окружает союзника костяным щитом с поглощением урона.|n"
        "- |cffa9c7deСфера разрушения|cffced4da: пассивно усиливает атаку на |cffc8e087+20|cffced4da ед. и наносит урон по области.|n"
        "- |cffa9c7deВоскрешение мёртвых|cffced4da: поднимает скелетов из павших воинов.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w209", "field": "name", "expected": wts_updates[11789]})
    checks_def.append({"type": "unit", "id": "w209", "field": "tip", "expected": wts_updates[11790]})
    checks_def.append({"type": "unit", "id": "w209", "field": "ubertip", "expected": wts_updates[29662]})

    # w211: Жрец (Q)
    wts_updates[11857] = "|cffe4cfa3Жрец|r"
    wts_updates[11858] = "|cffe4cfa3Жрец|r (|cffffffffQ|r)"
    wts_updates[29836] = (
        "|cffa6afb8ЮНИТ:|cffced4da Шаман-целитель троллей дальнего боя. Поддерживает армию исцелением и нейтрализует магию врага.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: повышает боевые показатели до |cffc8e087+30%|cffced4da урона.|n"
        "- |cffa9c7deИсцеление|cffced4da: восстанавливает здоровье раненым союзникам.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает положительные эффекты с врагов и отрицательные с союзников.|n"
        "- |cffa9c7deЗамедление|cffced4da: снижает скорость перемещения врага на |cffe69a8d30%|cffced4da и скорость атаки на |cffe69a8d15%|cffced4da.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w211", "field": "name", "expected": wts_updates[11857]})
    checks_def.append({"type": "unit", "id": "w211", "field": "tip", "expected": wts_updates[11858]})
    checks_def.append({"type": "unit", "id": "w211", "field": "ubertip", "expected": wts_updates[29836]})

    # w205: Огр-маг (W)
    wts_updates[11754] = "|cffe4cfa3Огр-маг|r"
    wts_updates[11755] = "|cffe4cfa3Огр-маг|r (|cffffffffW|r)"
    wts_updates[29278] = (
        "|cffa6afb8ЮНИТ:|cffced4da Двухголовый огр-чернокнижник ближнего боя. Усиливает передовые отряды боевым неистовством.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: опыт ветерана повышает урон до |cffc8e087+30%|cffced4da.|n"
        "- |cffa9c7deЖажда крови|cffced4da: ускоряет атаку союзника на |cffc8e087+20%|cffced4da и передвижение на |cffc8e087+10%|cffced4da.|n"
        "- |cffa9c7deОко Кил'Рога|cffced4da: призывает парящее невидимое око для разведки.|n"
        "- |cffa9c7deВзрывная руна|cffced4da: размещает минные руны, наносящие взрывной урон подошедшим врагам.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w205", "field": "name", "expected": wts_updates[11754]})
    checks_def.append({"type": "unit", "id": "w205", "field": "tip", "expected": wts_updates[11755]})
    checks_def.append({"type": "unit", "id": "w205", "field": "ubertip", "expected": wts_updates[29278]})

    # w207: Катапульта (E)
    wts_updates[11785] = "|cffe4cfa3Катапульта|r"
    wts_updates[11786] = "|cffe4cfa3Катапульта|r (|cffffffffE|r)"
    wts_updates[29473] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелое осадное орудие дальнего боя. Разрушает вражеские укрепления и здания массивными валунами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: повышает урон до |cffc8e087+30%|cffced4da по мере накопления боевого опыта.|n|n"
        "|cffa6afb8Атакует наземные цели и деревья.|r"
    )
    checks_def.append({"type": "unit", "id": "w207", "field": "name", "expected": wts_updates[11785]})
    checks_def.append({"type": "unit", "id": "w207", "field": "tip", "expected": wts_updates[11786]})
    checks_def.append({"type": "unit", "id": "w207", "field": "ubertip", "expected": wts_updates[29473]})

    # w201: Дирижабль (W)
    wts_updates[11746] = "|cffe4cfa3Дирижабль|r"
    wts_updates[11747] = "|cffe4cfa3Дирижабль|r (|cffffffffW|r)"
    wts_updates[29220] = (
        "|cffa6afb8ЮНИТ:|cffced4da Летающий транспорт гоблинов. Перевозит войска по воздуху и обеспечивает огневую поддержку ракетами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: увеличивает урон до |cffc8e087+30%|cffced4da с рангом ветерана.|n"
        "- |cffa9c7deВзять на борт|cffced4da: вмещает сухопутные отряды для переброски по воздуху.|n"
        "- |cffa9c7deПерелёт|cffced4da: кратковременно ускоряет полет дирижабля.|n"
        "- |cffa9c7deРакетный обстрел|cffced4da: после исследования выпускает ракеты по наземным врагам.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w201", "field": "name", "expected": wts_updates[11746]})
    checks_def.append({"type": "unit", "id": "w201", "field": "tip", "expected": wts_updates[11747]})
    checks_def.append({"type": "unit", "id": "w201", "field": "ubertip", "expected": wts_updates[29220]})

    # w206: Подрывной отряд (Q)
    wts_updates[11756] = "|cffe4cfa3Подрывной отряд|r"
    wts_updates[11784] = "|cffe4cfa3Подрывной отряд|r (|cffffffffQ|r)"
    wts_updates[29454] = (
        "|cffa6afb8ЮНИТ:|cffced4da Команда гоблинов-камикадзе с пороховыми бочками. Взрывают себя, нанося колоссальный урон зданиям и деревьям.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБа-бах!|cffced4da: детонирует взрывчатку, сметая вражеские укрепления.|n|n"
        "|cffa6afb8Взрывает наземные цели и деревья.|r"
    )
    checks_def.append({"type": "unit", "id": "w206", "field": "name", "expected": wts_updates[11756]})
    checks_def.append({"type": "unit", "id": "w206", "field": "tip", "expected": wts_updates[11784]})
    checks_def.append({"type": "unit", "id": "w206", "field": "ubertip", "expected": wts_updates[29454]})

    # w202: Красный дракон (Q)
    wts_updates[11748] = "|cffe4cfa3Красный дракон|r"
    wts_updates[11749] = "|cffe4cfa3Красный дракон|r (|cffffffffQ|r)"
    wts_updates[29275] = (
        "|cffa6afb8ЮНИТ:|cffced4da Исполинский летающий дракон дальнего боя. Испепеляет вражеские отряды и постройки огненными шарами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКузня войны|cffced4da: ветеранский ранг усиливает урон дракона до |cffc8e087+30%|cffced4da.|n"
        "- |cffa9c7deПламенное дыхание|cffced4da: выдыхает конус пламени, нанося урон врагам.|n"
        "- |cffa9c7deОгненный столб|cffced4da: обрушивает столб огня в указанную область.|n"
        "- |cffa9c7deПрочная чешуя|cffced4da: снижает получаемый от атак урон на |cffc8e0876|cffced4da ед.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "w202", "field": "name", "expected": wts_updates[11748]})
    checks_def.append({"type": "unit", "id": "w202", "field": "tip", "expected": wts_updates[11749]})
    checks_def.append({"type": "unit", "id": "w202", "field": "ubertip", "expected": wts_updates[29275]})

    # w220: Нефтяной танкер (A)
    wts_updates[22696] = "|cffe4cfa3Нефтяной танкер|r"
    wts_updates[22698] = "|cffe4cfa3Нефтяной танкер|r (|cffffffffA|r)"
    wts_updates[36997] = (
        "|cffa6afb8ЮНИТ:|cffced4da Специализированное судно Орды. Предназначено для разведки морских ресурсов и возведения нефтяных платформ.|r"
    )
    checks_def.append({"type": "unit", "id": "w220", "field": "name", "expected": wts_updates[22696]})
    checks_def.append({"type": "unit", "id": "w220", "field": "tip", "expected": wts_updates[22698]})
    checks_def.append({"type": "unit", "id": "w220", "field": "ubertip", "expected": wts_updates[36997]})

    # h0D6: Фрегат (W)
    wts_updates[3002] = "|cffe4cfa3Фрегат|r"
    wts_updates[5542] = (
        "|cffa6afb8ЮНИТ:|cffced4da Скоростной боевой корабль флота Орды. Оснащен бортовыми орудиями для патрулирования и обстрела вражеских судов.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0D6", "field": "name", "expected": wts_updates[3002]})
    checks_def.append({"type": "unit", "id": "h0D6", "field": "ubertip", "expected": wts_updates[5542]})

    # h0D5: Дредноут (E)
    wts_updates[10916] = "|cffe4cfa3Дредноут|r"
    wts_updates[10918] = "|cffe4cfa3Дредноут|r (|cffffffffE|r)"
    wts_updates[6926] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелый бронированный флагман флота Орды дальнего боя. Сокрушает береговые батареи и морские цели мощными залпами осадных орудий.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0D5", "field": "name", "expected": wts_updates[10916]})
    checks_def.append({"type": "unit", "id": "h0D5", "field": "tip", "expected": wts_updates[10918]})
    checks_def.append({"type": "unit", "id": "h0D5", "field": "ubertip", "expected": wts_updates[6926]})

    # =========================================================================
    # 5. UPGRADES
    # =========================================================================
    # w2r0: Крепкая броня (1-6)
    w2r0_names = [37490, 37491, 37492, 37493, 37494, 37495]
    w2r0_tips = [37496, 37497, 37498, 37499, 37500, 37501]
    w2r0_ubs = [37502, 37503, 37504, 37505, 37506, 37507]
    for i in range(6):
        lvl = i + 1
        bon = lvl * 2
        wts_updates[w2r0_names[i]] = f"|cffe4cfa3Крепкая броня — уровень {lvl}|r"
        wts_updates[w2r0_tips[i]] = f"|cffe4cfa3Крепкая броня — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[w2r0_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню наземных войск Орды на |cffc8e087+{bon}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deМетатель топоров|cffced4da|n"
            "- |cffa9c7deОгр-воин|cffced4da|n- |cffa9c7deОгр-маг|cffced4da|n- |cffa9c7deРыцарь смерти|cffced4da|n- |cffa9c7deЖрец|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r0", "field": f"name{lvl}", "expected": wts_updates[w2r0_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r0", "field": f"tip{lvl}", "expected": wts_updates[w2r0_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r0", "field": f"ubertip{lvl}", "expected": wts_updates[w2r0_ubs[i]]})

    # w2r1: Оружие ближнего боя (1-6)
    w2r1_names = [37513, 37514, 37515, 37516, 37517, 37518]
    w2r1_tips = [37519, 37520, 37521, 37522, 37523, 37524]
    w2r1_ubs = [37525, 37526, 37527, 37528, 37529, 37530]
    for i in range(6):
        lvl = i + 1
        wts_updates[w2r1_names[i]] = f"|cffe4cfa3Оружие ближнего боя — уровень {lvl}|r"
        wts_updates[w2r1_tips[i]] = f"|cffe4cfa3Оружие ближнего боя — уровень {lvl}|r (|cffffffffM|r)"
        wts_updates[w2r1_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя Орды.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deОгр-воин|cffced4da|n- |cffa9c7deОгр-маг|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r1", "field": f"name{lvl}", "expected": wts_updates[w2r1_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r1", "field": f"tip{lvl}", "expected": wts_updates[w2r1_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r1", "field": f"ubertip{lvl}", "expected": wts_updates[w2r1_ubs[i]]})

    # w2r2: Оружие дальнего боя (1-6)
    w2r2_names = [37539, 37540, 37541, 37542, 37543, 37544]
    w2r2_tips = [37545, 37546, 37547, 37548, 37549, 37550]
    w2r2_ubs = [37551, 37552, 37553, 37554, 37555, 37556]
    for i in range(6):
        lvl = i + 1
        wts_updates[w2r2_names[i]] = f"|cffe4cfa3Оружие дальнего боя — уровень {lvl}|r"
        wts_updates[w2r2_tips[i]] = f"|cffe4cfa3Оружие дальнего боя — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[w2r2_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон дальнобойных атак войск Орды.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМетатель топоров|cffced4da|n- |cffa9c7deЖрец|cffced4da|n- |cffa9c7deРыцарь смерти|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r2", "field": f"name{lvl}", "expected": wts_updates[w2r2_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r2", "field": f"tip{lvl}", "expected": wts_updates[w2r2_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r2", "field": f"ubertip{lvl}", "expected": wts_updates[w2r2_ubs[i]]})

    # w2r3: Военная экспертиза (1-4)
    w2r3_names = [37561, 37562, 37563, 37564]
    w2r3_tips = [37565, 37566, 37567, 37568]
    w2r3_ubs = [37569, 37573, 37574, 37575]
    for i in range(4):
        lvl = i + 1
        wts_updates[w2r3_names[i]] = f"|cffe4cfa3Военная экспертиза — уровень {lvl}|r"
        wts_updates[w2r3_tips[i]] = f"|cffe4cfa3Военная экспертиза — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[w2r3_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает стартовый опыт при обучении всех войск Орды, наделяя их дополнительным рангом «Кузни войны».|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r3", "field": f"name{lvl}", "expected": wts_updates[w2r3_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r3", "field": f"tip{lvl}", "expected": wts_updates[w2r3_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r3", "field": f"ubertip{lvl}", "expected": wts_updates[w2r3_ubs[i]]})

    # w2r4: Чародейства огров (1-4)
    w2r4_names = [37579, 37580, 37581, 37582]
    w2r4_tips = [37583, 37586, 37584, 37585]
    w2r4_ubs = [37589, 37590, 37591, 37592]
    for i in range(4):
        lvl = i + 1
        wts_updates[w2r4_names[i]] = f"|cffe4cfa3Чародейства огров — уровень {lvl}|r"
        wts_updates[w2r4_tips[i]] = f"|cffe4cfa3Чародейства огров — уровень {lvl}|r (|cffffffffM|r)"
        wts_updates[w2r4_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и скорость её восстановления у огров-магов, а также открывает заклинания «Жажда крови» и «Взрывная руна».|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОгр-маг|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r4", "field": f"name{lvl}", "expected": wts_updates[w2r4_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r4", "field": f"tip{lvl}", "expected": wts_updates[w2r4_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r4", "field": f"ubertip{lvl}", "expected": wts_updates[w2r4_ubs[i]]})

    # w2r5: Ритуалы смерти (1-4)
    w2r5_names = [37596, 37597, 37598, 37599]
    w2r5_tips = [37600, 37603, 37601, 37602]
    w2r5_ubs = [37606, 37607, 37608, 37609]
    for i in range(4):
        lvl = i + 1
        wts_updates[w2r5_names[i]] = f"|cffe4cfa3Ритуалы смерти — уровень {lvl}|r"
        wts_updates[w2r5_tips[i]] = f"|cffe4cfa3Ритуалы смерти — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[w2r5_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, запас маны и скорость её восстановления у рыцарей смерти, а также открывает заклинания «Тёмный доспех», «Воскрешение мёртвых» и «Сфера разрушения».|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРыцарь смерти|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r5", "field": f"name{lvl}", "expected": wts_updates[w2r5_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r5", "field": f"tip{lvl}", "expected": wts_updates[w2r5_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r5", "field": f"ubertip{lvl}", "expected": wts_updates[w2r5_ubs[i]]})

    # w2r6: Колдовство вуду (1-4)
    w2r6_names = [37613, 37614, 37615, 37616]
    w2r6_tips = [37617, 37620, 37618, 37619]
    w2r6_ubs = [37623, 37624, 37625, 37626]
    for i in range(4):
        lvl = i + 1
        wts_updates[w2r6_names[i]] = f"|cffe4cfa3Колдовство вуду — уровень {lvl}|r"
        wts_updates[w2r6_tips[i]] = f"|cffe4cfa3Колдовство вуду — уровень {lvl}|r (|cffffffffV|r)"
        wts_updates[w2r6_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и скорость её восстановления у жрецов, а также открывает заклинания «Рассеивание заклинаний» и «Замедление».|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЖрец|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r6", "field": f"name{lvl}", "expected": wts_updates[w2r6_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r6", "field": f"tip{lvl}", "expected": wts_updates[w2r6_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r6", "field": f"ubertip{lvl}", "expected": wts_updates[w2r6_ubs[i]]})

    # w2r7: Тренировки рубак (1-3)
    w2r7_names = [22194, 37627, 37631]
    w2r7_tips = [25319, 37628, 37634]
    w2r7_ubs = [5532, 5535, 7897]
    for i in range(3):
        lvl = i + 1
        wts_updates[w2r7_names[i]] = f"|cffe4cfa3Тренировки рубак — уровень {lvl}|r"
        wts_updates[w2r7_tips[i]] = f"|cffe4cfa3Тренировки рубак — уровень {lvl}|r (|cffffffffG|r)"
        wts_updates[w2r7_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья рубак на |cffc8e087+100|cffced4da ед. и урон на |cffc8e087+5|cffced4da ед. за уровень, а также открывает способности «Ярость» и «Отработанные навыки».|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r7", "field": f"name{lvl}", "expected": wts_updates[w2r7_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r7", "field": f"tip{lvl}", "expected": wts_updates[w2r7_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r7", "field": f"ubertip{lvl}", "expected": wts_updates[w2r7_ubs[i]]})

    # w2r8: Тренировки огров (1-3)
    w2r8_names = [7899, 37636, 37640]
    w2r8_tips = [11817, 37637, 37643]
    w2r8_ubs = [40228, 40229, 40230]
    for i in range(3):
        lvl = i + 1
        wts_updates[w2r8_names[i]] = f"|cffe4cfa3Тренировки огров — уровень {lvl}|r"
        wts_updates[w2r8_tips[i]] = f"|cffe4cfa3Тренировки огров — уровень {lvl}|r (|cffffffffO|r)"
        wts_updates[w2r8_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает максимальный запас здоровья огров-воинов на |cffc8e087+125|cffced4da ед. за уровень и открывает способность «Сопротивление магии».|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОгр-воин|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r8", "field": f"name{lvl}", "expected": wts_updates[w2r8_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r8", "field": f"tip{lvl}", "expected": wts_updates[w2r8_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r8", "field": f"ubertip{lvl}", "expected": wts_updates[w2r8_ubs[i]]})

    # w2r9: Тренировки метателей (1-3)
    w2r9_names = [18418, 37647, 37651]
    w2r9_tips = [20461, 37648, 37654]
    w2r9_ubs = [5537, 5556, 21251]
    for i in range(3):
        lvl = i + 1
        wts_updates[w2r9_names[i]] = f"|cffe4cfa3Тренировки метателей — уровень {lvl}|r"
        wts_updates[w2r9_tips[i]] = f"|cffe4cfa3Тренировки метателей — уровень {lvl}|r (|cffffffffT|r)"
        wts_updates[w2r9_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья метателей топоров на |cffc8e087+85|cffced4da ед. и дальность их атаки на каждом уровне.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМетатель топоров|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2r9", "field": f"name{lvl}", "expected": wts_updates[w2r9_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r9", "field": f"tip{lvl}", "expected": wts_updates[w2r9_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2r9", "field": f"ubertip{lvl}", "expected": wts_updates[w2r9_ubs[i]]})

    # w2ra: Разведение драконов (1-2)
    w2ra_names = [37713, 37714]
    w2ra_tips = [37717, 37720]
    w2ra_ubs = [12715, 12958]
    for i in range(2):
        lvl = i + 1
        wts_updates[w2ra_names[i]] = f"|cffe4cfa3Разведение драконов — уровень {lvl}|r"
        wts_updates[w2ra_tips[i]] = f"|cffe4cfa3Разведение драконов — уровень {lvl}|r (|cffffffffB|r)"
        wts_updates[w2ra_ubs[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает дальность атаки красных драконов и повышает их здоровье на |cffc8e087+75|cffced4da ед. за уровень.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deКрасный дракон|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff2|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2ra", "field": f"name{lvl}", "expected": wts_updates[w2ra_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2ra", "field": f"tip{lvl}", "expected": wts_updates[w2ra_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2ra", "field": f"ubertip{lvl}", "expected": wts_updates[w2ra_ubs[i]]})

    # w2rb: Улучшенные пилы (1-6)
    w2rb_names = [37730, 37748, 37731, 37732, 37733, 37734]
    w2rb_tips = [37735, 37749, 37736, 37737, 37738, 37739]
    w2rb_ubs = [37745, 37740, 37741, 37742, 37743, 37744]
    for i in range(6):
        lvl = i + 1
        bon = lvl * 10
        wts_updates[w2rb_names[i]] = f"|cffe4cfa3Улучшенные пилы — уровень {lvl}|r"
        wts_updates[w2rb_tips[i]] = f"|cffe4cfa3Улучшенные пилы — уровень {lvl}|r (|cffffffffL|r)"
        wts_updates[w2rb_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой батраками древесины на |cffc8e087+{bon}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deБатрак|cffced4da|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}|cffced4da из |cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "w2rb", "field": f"name{lvl}", "expected": wts_updates[w2rb_names[i]]})
        checks_def.append({"type": "upgrade", "id": "w2rb", "field": f"tip{lvl}", "expected": wts_updates[w2rb_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "w2rb", "field": f"ubertip{lvl}", "expected": wts_updates[w2rb_ubs[i]]})

    # w2re: Заряды взрыводия (1-2)
    wts_updates[37676] = "|cffe4cfa3Заряды взрыводия — уровень 1|r"
    wts_updates[37677] = "|cffe4cfa3Заряды взрыводия — уровень 2|r"
    wts_updates[37680] = "|cffe4cfa3Заряды взрыводия — уровень 1|r (|cffffffffE|r)"
    wts_updates[37683] = "|cffe4cfa3Заряды взрыводия — уровень 2|r (|cffffffffE|r)"
    checks_def.append({"type": "upgrade", "id": "w2re", "field": "name1", "expected": wts_updates[37676]})
    checks_def.append({"type": "upgrade", "id": "w2re", "field": "name2", "expected": wts_updates[37677]})
    checks_def.append({"type": "upgrade", "id": "w2re", "field": "tip1", "expected": wts_updates[37680]})
    checks_def.append({"type": "upgrade", "id": "w2re", "field": "tip2", "expected": wts_updates[37683]})

    # w2rq: Комплектование дирижаблей (1-2)
    wts_updates[37659] = "|cffe4cfa3Комплектование дирижаблей — уровень 1|r"
    wts_updates[37660] = "|cffe4cfa3Комплектование дирижаблей — уровень 2|r"
    wts_updates[37663] = "|cffe4cfa3Комплектование дирижаблей — уровень 1|r (|cffffffffZ|r)"
    wts_updates[37666] = "|cffe4cfa3Комплектование дирижаблей — уровень 2|r (|cffffffffZ|r)"
    wts_updates[37669] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает дирижабли ракетными установками и увеличивает шанс спасения пехоты разыскной бригадой.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДирижабль|cffced4da|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1|cffced4da из |cffffffff2|cffced4da.|r"
    )
    wts_updates[37670] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает дирижабли ракетными установками и увеличивает шанс спасения пехоты разыскной бригадой.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДирижабль|cffced4da|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2|cffced4da из |cffffffff2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "w2rq", "field": "name1", "expected": wts_updates[37659]})
    checks_def.append({"type": "upgrade", "id": "w2rq", "field": "name2", "expected": wts_updates[37660]})
    checks_def.append({"type": "upgrade", "id": "w2rq", "field": "tip1", "expected": wts_updates[37663]})
    checks_def.append({"type": "upgrade", "id": "w2rq", "field": "tip2", "expected": wts_updates[37666]})
    checks_def.append({"type": "upgrade", "id": "w2rq", "field": "ubertip1", "expected": wts_updates[37669]})
    checks_def.append({"type": "upgrade", "id": "w2rq", "field": "ubertip2", "expected": wts_updates[37670]})

    # w286: Зачарованные топоры (1)
    wts_updates[37885] = "|cffe4cfa3Зачарованные топоры|r"
    wts_updates[37886] = "|cffe4cfa3Зачарованные топоры|r (|cffffffffA|r)"
    wts_updates[37888] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет топоры метателей троллей магической силой, позволяя им отскакивать в |cffffffff2|cffced4da дополнительные цели при атаке.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМетатель топоров|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "w286", "field": "name1", "expected": wts_updates[37885]})
    checks_def.append({"type": "upgrade", "id": "w286", "field": "tip1", "expected": wts_updates[37886]})
    checks_def.append({"type": "upgrade", "id": "w286", "field": "ubertip1", "expected": wts_updates[37888]})

    # w291: Драконы-поджигатели
    wts_updates[37800] = "|cffe4cfa3Драконы-поджигатели|r"
    wts_updates[37801] = "|cffe4cfa3Драконы-поджигатели|r"
    wts_updates[37802] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Наделяет красных драконов способностями «Огненный столб» и «Пламенное дыхание».|r"
    checks_def.append({"type": "upgrade", "id": "w291", "field": "name1", "expected": wts_updates[37800]})
    checks_def.append({"type": "upgrade", "id": "w291", "field": "tip1", "expected": wts_updates[37801]})
    checks_def.append({"type": "upgrade", "id": "w291", "field": "ubertip1", "expected": wts_updates[37802]})

    # w292: Драконы-защитники
    wts_updates[37791] = "|cffe4cfa3Драконы-защитники|r"
    wts_updates[37792] = "|cffe4cfa3Драконы-защитники|r"
    wts_updates[37793] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Увеличивает запас здоровья драконов на |cffc8e087+425|cffced4da ед. и наделяет их способностью «Прочная чешуя».|r"
    checks_def.append({"type": "upgrade", "id": "w292", "field": "name1", "expected": wts_updates[37791]})
    checks_def.append({"type": "upgrade", "id": "w292", "field": "tip1", "expected": wts_updates[37792]})
    checks_def.append({"type": "upgrade", "id": "w292", "field": "ubertip1", "expected": wts_updates[37793]})

    # w293: Драконы-огнепускатели
    wts_updates[37782] = "|cffe4cfa3Драконы-огнепускатели|r"
    wts_updates[37783] = "|cffe4cfa3Драконы-огнепускатели|r"
    wts_updates[37784] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Увеличивает урон атак красных драконов на |cffc8e087+25|cffced4da ед.|r"
    checks_def.append({"type": "upgrade", "id": "w293", "field": "name1", "expected": wts_updates[37782]})
    checks_def.append({"type": "upgrade", "id": "w293", "field": "tip1", "expected": wts_updates[37783]})
    checks_def.append({"type": "upgrade", "id": "w293", "field": "ubertip1", "expected": wts_updates[37784]})

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # w2a0: Кузня войны (15 levels)
    wts_updates[11961] = "|cffe4cfa3Кузня войны|r"
    w2a0_tips = [11960, 11969, 11970, 11971, 11972, 12088, 12101, 12102, 12103, 12104, 12105, 12106, 12107, 12108]
    w2a0_ubs = [11968, 12110, 12111, 12112, 12113, 12114, 12115, 12116, 12117, 12118, 12167, 12168, 12169, 12170]
    checks_def.append({"type": "ability", "id": "w2a0", "field": "name", "expected": wts_updates[11961]})
    for i in range(14):
        lvl = i + 1
        bon = lvl * 2
        wts_updates[w2a0_tips[i]] = f"|cffe4cfa3Кузня войны — ранг {lvl}|r"
        wts_updates[w2a0_ubs[i]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накапливая боевой и трудовой опыт, боец повышает свой ранг. "
            f"Каждый ранг увеличивает наносимый урон на |cffc8e087+{bon}%|cffced4da.|n|nТекущий ранг: |cffffffff{lvl}|cffced4da из |cffffffff15|cffced4da.|r"
        )
        checks_def.append({"type": "ability", "id": "w2a0", "field": f"tip{lvl}", "expected": wts_updates[w2a0_tips[i]]})
        checks_def.append({"type": "ability", "id": "w2a0", "field": f"ubertip{lvl}", "expected": wts_updates[w2a0_ubs[i]]})

    # w2a0 level 15: Герой войны
    wts_updates[12109] = "|cffe4cfa3Герой войны|r"
    wts_updates[12171] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Максимальный ранг закалки в бою. Увеличивает наносимый бойцом урон на |cffc8e087+30%|cffced4da.|n|n"
        "|cffc8e087Высший ветеранский ранг.|r"
    )
    checks_def.append({"type": "ability", "id": "w2a0", "field": "tip15", "expected": wts_updates[12109]})
    checks_def.append({"type": "ability", "id": "w2a0", "field": "ubertip15", "expected": wts_updates[12171]})

    # w2a1: Разыскная бригада (3 levels)
    wts_updates[12173] = "|cffe4cfa3Разыскная бригада|r"
    wts_updates[12172] = "|cffe4cfa3Разыскная бригада|r"
    wts_updates[12176] = "|cffe4cfa3Разыскная бригада|r"
    wts_updates[12177] = "|cffe4cfa3Разыскная бригада|r"
    wts_updates[12175] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При смертельном ранении союзных пехотинцев находящиеся рядом дирижабли имеют шанс спасти бойца и забрать его на борт.|r"
    wts_updates[12428] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При смертельном ранении союзных пехотинцев находящиеся рядом дирижабли имеют шанс спасти бойца и забрать его на борт.|r"
    wts_updates[12431] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При смертельном ранении союзных пехотинцев находящиеся рядом дирижабли имеют шанс спасти бойца и забрать его на борт.|r"
    checks_def.append({"type": "ability", "id": "w2a1", "field": "name", "expected": wts_updates[12173]})

    # w2a2: Ба-бах! (3 levels)
    wts_updates[12493] = "|cffe4cfa3Ба-бах!|r"
    wts_updates[12492] = "|cffe4cfa3Ба-бах!|r (|cffffffffB|r)"
    wts_updates[12766] = "|cffe4cfa3Ба-бах!|r (|cffffffffB|r)"
    wts_updates[12770] = "|cffe4cfa3Ба-бах!|r (|cffffffffB|r)"
    wts_updates[12778] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подрывники взрывают бочки с порохом, жертвуя собой и нанося разрушительный урон окружающим строениям, войскам и деревьям.|r"
    wts_updates[12791] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подрывники взрывают бочки с порохом, жертвуя собой и нанося разрушительный урон окружающим строениям, войскам и деревьям.|r"
    wts_updates[12800] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подрывники взрывают бочки с порохом, жертвуя собой и нанося разрушительный урон окружающим строениям, войскам и деревьям.|r"
    checks_def.append({"type": "ability", "id": "w2a2", "field": "name", "expected": wts_updates[12493]})

    # w2a3: Перелёт (1 level)
    wts_updates[12488] = "|cffe4cfa3Перелёт|r"
    wts_updates[12489] = "|cffe4cfa3Перелёт|r (|cffffffffF|r)"
    wts_updates[12490] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дирижабль ускоряет двигатели, значительно увеличивая скорость полета на |cffffffff30|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "w2a3", "field": "name", "expected": wts_updates[12488]})
    checks_def.append({"type": "ability", "id": "w2a3", "field": "tip1", "expected": wts_updates[12489]})
    checks_def.append({"type": "ability", "id": "w2a3", "field": "ubertip1", "expected": wts_updates[12490]})

    # w2a4: Жажда крови (1 level)
    wts_updates[16439] = "|cffe4cfa3Жажда крови|r"
    wts_updates[16440] = "|cffe4cfa3Жажда крови|r (|cffffffffB|r)"
    wts_updates[16441] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вводит союзного бойца в боевое неистовство, увеличивая скорость атаки на |cffc8e087+20%|cffced4da и скорость передвижения на |cffc8e087+10%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "w2a4", "field": "name", "expected": wts_updates[16439]})
    checks_def.append({"type": "ability", "id": "w2a4", "field": "tip1", "expected": wts_updates[16440]})
    checks_def.append({"type": "ability", "id": "w2a4", "field": "ubertip1", "expected": wts_updates[16441]})

    # w2a5: Воскрешение мёртвых (1 level)
    wts_updates[16444] = "|cffe4cfa3Воскрешение мёртвых|r"
    wts_updates[16445] = "|cffe4cfa3Воскрешение мёртвых|r (|cffffffffR|r)"
    checks_def.append({"type": "ability", "id": "w2a5", "field": "name", "expected": wts_updates[16444]})
    checks_def.append({"type": "ability", "id": "w2a5", "field": "tip1", "expected": wts_updates[16445]})

    # w2a6: Око Кил'Рога (1 level)
    wts_updates[16446] = "|cffe4cfa3Око Кил'Рога|r"
    wts_updates[16447] = "|cffe4cfa3Око Кил'Рога|r (|cffffffffE|r)"
    wts_updates[20211] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает невидимое парящее око для дальней разведки территории.|r"
    checks_def.append({"type": "ability", "id": "w2a6", "field": "name", "expected": wts_updates[16446]})
    checks_def.append({"type": "ability", "id": "w2a6", "field": "tip1", "expected": wts_updates[16447]})
    checks_def.append({"type": "ability", "id": "w2a6", "field": "ubertip1", "expected": wts_updates[20211]})

    # w2a8: Тёмный доспех (1 level)
    wts_updates[37256] = "|cffe4cfa3Тёмный доспех|r"
    wts_updates[37257] = "|cffe4cfa3Тёмный доспех|r (|cffffffffA|r)"
    wts_updates[37258] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзника костяным щитом, поглощающим до |cffffffff70|cffced4da ед. урона.|r"
    checks_def.append({"type": "ability", "id": "w2a8", "field": "name", "expected": wts_updates[37256]})
    checks_def.append({"type": "ability", "id": "w2a8", "field": "tip1", "expected": wts_updates[37257]})
    checks_def.append({"type": "ability", "id": "w2a8", "field": "ubertip1", "expected": wts_updates[37258]})

    # w2a9: Взрывная руна (1 level)
    wts_updates[20757] = "|cffe4cfa3Взрывная руна|r"
    wts_updates[20212] = "|cffe4cfa3Взрывная руна|r (|cffffffffR|r)"
    wts_updates[20215] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Устанавливает на земле |cffffffff3|cffced4da невидимые руны-ловушки. При приближении противника руны взрываются, нанося урон вражеским войскам.|r"
    checks_def.append({"type": "ability", "id": "w2a9", "field": "name", "expected": wts_updates[20757]})
    checks_def.append({"type": "ability", "id": "w2a9", "field": "tip1", "expected": wts_updates[20212]})
    checks_def.append({"type": "ability", "id": "w2a9", "field": "ubertip1", "expected": wts_updates[20215]})

    # w2aA: Ярость берсерка (Zul'jin, 4 levels)
    wts_updates[37364] = "|cffe4cfa3Ярость берсерка|r"
    wts_updates[37706] = "|cffe4cfa3Ярость берсерка|r"
    wts_updates[37705] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки героя на время действия.|r"
    w2aA_tips = [37350, 37351, 37352, 37353]
    w2aA_ubs = [37363, 37354, 37355, 37356]
    bon_list = [15, 30, 45, 60]
    checks_def.append({"type": "ability", "id": "w2aA", "field": "name", "expected": wts_updates[37364]})
    for i in range(4):
        lvl = i + 1
        bon = bon_list[i]
        cost = 50 + i * 25
        wts_updates[w2aA_tips[i]] = f"|cffe4cfa3Ярость берсерка — уровень {lvl}|r (|cffffffffB|r)"
        wts_updates[w2aA_ubs[i]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой впадает в боевую ярость, увеличивая скорость атаки на |cffc8e087+{bon}%|cffced4da на |cffffffff20|cffced4da сек.|n|n"
            f"Время восстановления: |cffffffff25|cffced4da сек. Расход маны: |cffffffff{cost}|cffced4da.|r"
        )
        checks_def.append({"type": "ability", "id": "w2aA", "field": f"tip{lvl}", "expected": wts_updates[w2aA_tips[i]]})
        checks_def.append({"type": "ability", "id": "w2aA", "field": f"ubertip{lvl}", "expected": wts_updates[w2aA_ubs[i]]})

    # w2aQ: Разъедающее зелье (Zul'jin, 2 levels)
    wts_updates[37366] = "|cffe4cfa3Разъедающее зелье|r"
    wts_updates[37369] = "|cffe4cfa3Разъедающее зелье|r"
    wts_updates[37367] = "|cffe4cfa3Разъедающее зелье — уровень 1|r (|cffffffffQ|r)"
    wts_updates[37368] = "|cffe4cfa3Разъедающее зелье — уровень 2|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "w2aQ", "field": "name", "expected": wts_updates[37366]})
    checks_def.append({"type": "ability", "id": "w2aQ", "field": "tip1", "expected": wts_updates[37367]})
    checks_def.append({"type": "ability", "id": "w2aQ", "field": "tip2", "expected": wts_updates[37368]})

    # w2aW: Стрелы тьмы (Cho'gall, 4 levels)
    wts_updates[37370] = "|cffe4cfa3Стрелы тьмы|r"
    wts_updates[37371] = "|cffe4cfa3Стрелы тьмы|r"
    wts_updates[37372] = "|cffe4cfa3Стрелы тьмы — уровень 1|r (|cffffffffW|r)"
    wts_updates[37373] = "|cffe4cfa3Стрелы тьмы — уровень 2|r (|cffffffffW|r)"
    wts_updates[37374] = "|cffe4cfa3Стрелы тьмы — уровень 3|r (|cffffffffW|r)"
    wts_updates[37375] = "|cffe4cfa3Стрелы тьмы — уровень 4|r (|cffffffffW|r)"
    wts_updates[27451] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает веером сгустки темной энергии, поражающие вражеские отряды на своём пути.|r"
    checks_def.append({"type": "ability", "id": "w2aW", "field": "name", "expected": wts_updates[37370]})

    # w2aZ: Аура гениальности (Cho'gall, 4 levels)
    wts_updates[37378] = "|cffe4cfa3Аура гениальности|r"
    wts_updates[37379] = "|cffe4cfa3Аура гениальности — уровень 1|r"
    wts_updates[37380] = "|cffe4cfa3Аура гениальности — уровень 2|r"
    wts_updates[37381] = "|cffe4cfa3Аура гениальности — уровень 3|r"
    wts_updates[37382] = "|cffe4cfa3Аура гениальности — уровень 4|r"
    wts_updates[37383] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно ускоряет восстановление маны находящихся рядом союзных героев и войск.|r"
    checks_def.append({"type": "ability", "id": "w2aZ", "field": "name", "expected": wts_updates[37378]})

    # w2ab: Похищение жизни (Death Knight, 1 level)
    wts_updates[37263] = "|cffe4cfa3Похищение жизни|r"
    wts_updates[37264] = "|cffe4cfa3Похищение жизни|r (|cffffffffD|r)"
    wts_updates[2926] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Непрерывно вытягивает жизненную силу врага, похищая |cffffffff45|cffced4da ед. здоровья в секунду и восстанавливая здоровье рыцарю смерти.|r"
    checks_def.append({"type": "ability", "id": "w2ab", "field": "name", "expected": wts_updates[37263]})
    checks_def.append({"type": "ability", "id": "w2ab", "field": "tip1", "expected": wts_updates[37264]})
    checks_def.append({"type": "ability", "id": "w2ab", "field": "ubertip1", "expected": wts_updates[2926]})

    # w2ac: Замедление (Priest, 1 level)
    wts_updates[36850] = "|cffe4cfa3Замедление|r"
    wts_updates[36849] = "|cffe4cfa3Замедление|r (|cffffffffW|r)"
    wts_updates[37074] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет выбранного противника, снижая скорость его передвижения на |cffe69a8d30%|cffced4da и скорость атаки на |cffe69a8d15%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "w2ac", "field": "name", "expected": wts_updates[36850]})
    checks_def.append({"type": "ability", "id": "w2ac", "field": "tip1", "expected": wts_updates[36849]})
    checks_def.append({"type": "ability", "id": "w2ac", "field": "ubertip1", "expected": wts_updates[37074]})

    # w2ad: Вихрь клинков (Orgrim Doomhammer, 4 levels)
    wts_updates[37326] = "|cffe4cfa3Вихрь клинков|r"
    wts_updates[37327] = "|cffe4cfa3Вихрь клинков|r"
    wts_updates[37328] = "|cffe4cfa3Вихрь клинков — уровень 1|r (|cffffffffB|r)"
    wts_updates[37329] = "|cffe4cfa3Вихрь клинков — уровень 2|r (|cffffffffB|r)"
    wts_updates[37330] = "|cffe4cfa3Вихрь клинков — уровень 3|r (|cffffffffB|r)"
    wts_updates[37331] = "|cffe4cfa3Вихрь клинков — уровень 4|r (|cffffffffB|r)"
    wts_updates[37332] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вождь закручивается в разрушительном смерче стали, нанося урон окружающим врагам в течение |cffffffff3|cffced4da сек.|r"
    wts_updates[37333] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вождь закручивается в разрушительном смерче стали, нанося урон окружающим врагам в течение |cffffffff3|cffced4da сек.|r"
    wts_updates[37334] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вождь закручивается в разрушительном смерче стали, нанося урон окружающим врагам в течение |cffffffff3|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "w2ad", "field": "name", "expected": wts_updates[37326]})

    # w2af: Метание топоров (Zul'jin, 4 levels)
    wts_updates[37336] = "|cffe4cfa3Метание топоров|r"
    wts_updates[37346] = "|cffe4cfa3Метание топоров|r"
    wts_updates[37347] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Метает топоры по каждому юниту в выбранной области.|r"
    wts_updates[37337] = "|cffe4cfa3Метание топоров — уровень 1|r (|cffffffffT|r)"
    wts_updates[37338] = "|cffe4cfa3Метание топоров — уровень 2|r (|cffffffffT|r)"
    wts_updates[37339] = "|cffe4cfa3Метание топоров — уровень 3|r (|cffffffffT|r)"
    wts_updates[37340] = "|cffe4cfa3Метание топоров — уровень 4|r (|cffffffffT|r)"
    wts_updates[37341] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает сокрушительные топоры по каждому вражескому воину в выбранной области радиусом |cffffffff315|cffced4da.|r"
    wts_updates[37342] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает сокрушительные топоры по каждому вражескому воину в выбранной области радиусом |cffffffff315|cffced4da.|r"
    wts_updates[37343] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает сокрушительные топоры по каждому вражескому воину в выбранной области радиусом |cffffffff315|cffced4da.|r"
    wts_updates[37344] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает сокрушительные топоры по каждому вражескому воину в выбранной области радиусом |cffffffff315|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "w2af", "field": "name", "expected": wts_updates[37336]})

    # w2ag: Сильный удар (Ogre, 1 level)
    wts_updates[37284] = "|cffe4cfa3Сильный удар|r"
    wts_updates[37285] = "|cffe4cfa3Сильный удар|r"
    wts_updates[37286] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff15%|cffced4da при атаке наносит дополнительный урон и оглушает цель на |cffffffff1|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "w2ag", "field": "name", "expected": wts_updates[37284]})
    checks_def.append({"type": "ability", "id": "w2ag", "field": "tip1", "expected": wts_updates[37285]})
    checks_def.append({"type": "ability", "id": "w2ag", "field": "ubertip1", "expected": wts_updates[37286]})

    # w2ah: Аура меткости (Zul'jin, 4 levels)
    wts_updates[37314] = "|cffe4cfa3Аура меткости|r"
    wts_updates[37315] = "|cffe4cfa3Аура меткости|r"
    wts_updates[37316] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон от дистанционных атак находящихся рядом союзников.|r"
    wts_updates[37317] = "|cffe4cfa3Аура меткости — уровень 1|r"
    wts_updates[37318] = "|cffe4cfa3Аура меткости — уровень 2|r"
    wts_updates[37319] = "|cffe4cfa3Аура меткости — уровень 3|r"
    wts_updates[37320] = "|cffe4cfa3Аура меткости — уровень 4|r"
    wts_updates[37324] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон от дистанционных атак находящихся рядом союзных войск на |cffc8e087+10%|cffced4da.|r"
    wts_updates[37321] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон от дистанционных атак находящихся рядом союзных войск на |cffc8e087+20%|cffced4da.|r"
    wts_updates[37322] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон от дистанционных атак находящихся рядом союзных войск на |cffc8e087+30%|cffced4da.|r"
    wts_updates[37323] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон от дистанционных атак находящихся рядом союзных войск на |cffc8e087+40%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "w2ah", "field": "name", "expected": wts_updates[37314]})

    # w2ak: Аура выносливости (Orgrim Doomhammer, 4 levels)
    wts_updates[37300] = "|cffe4cfa3Аура выносливости|r"
    wts_updates[37301] = "|cffe4cfa3Аура выносливости — уровень 1|r"
    wts_updates[37302] = "|cffe4cfa3Аура выносливости — уровень 2|r"
    wts_updates[37303] = "|cffe4cfa3Аура выносливости — уровень 3|r"
    wts_updates[37304] = "|cffe4cfa3Аура выносливости — уровень 4|r"
    checks_def.append({"type": "ability", "id": "w2ak", "field": "name", "expected": wts_updates[37300]})

    # w2al: Держать строй (Orgrim Doomhammer, 4 levels)
    wts_updates[37289] = "|cffe4cfa3Держать строй|r"
    wts_updates[37297] = "|cffe4cfa3Держать строй|r"
    wts_updates[37298] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню и регенерацию здоровья союзных воинов.|r"
    wts_updates[37288] = "|cffe4cfa3Держать строй — уровень 1|r (|cffffffffH|r)"
    wts_updates[37291] = "|cffe4cfa3Держать строй — уровень 2|r (|cffffffffH|r)"
    wts_updates[37290] = "|cffe4cfa3Держать строй — уровень 3|r (|cffffffffH|r)"
    wts_updates[37292] = "|cffe4cfa3Держать строй — уровень 4|r (|cffffffffH|r)"
    wts_updates[37293] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает войскам сомкнуть ряды, повышая броню на |cffc8e087+4|cffced4da ед. и регенерацию на |cffc8e087+15|cffced4da ед./сек. на |cffffffff20|cffced4da сек.|r"
    wts_updates[37294] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает войскам сомкнуть ряды, повышая броню на |cffc8e087+5|cffced4da ед. и регенерацию на |cffc8e087+25|cffced4da ед./сек. на |cffffffff20|cffced4da сек.|r"
    wts_updates[37295] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает войскам сомкнуть ряды, повышая броню на |cffc8e087+6|cffced4da ед. и регенерацию на |cffc8e087+35|cffced4da ед./сек. на |cffffffff20|cffced4da сек.|r"
    wts_updates[37296] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает войскам сомкнуть ряды, повышая броню на |cffc8e087+7|cffced4da ед. и регенерацию на |cffc8e087+45|cffced4da ед./сек. на |cffffffff20|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "w2al", "field": "name", "expected": wts_updates[37289]})

    # w2am: Отработанные навыки (Grunt)
    wts_updates[37269] = "|cffe4cfa3Отработанные навыки|r"
    wts_updates[37270] = "|cffe4cfa3Отработанные навыки|r"
    wts_updates[37271] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно дарует бойцу |cffffffff5%|cffced4da шанс уклониться от удара и |cffffffff5%|cffced4da шанс нанести критический урон.|r"
    checks_def.append({"type": "ability", "id": "w2am", "field": "name", "expected": wts_updates[37269]})
    checks_def.append({"type": "ability", "id": "w2am", "field": "tip1", "expected": wts_updates[37270]})
    checks_def.append({"type": "ability", "id": "w2am", "field": "ubertip1", "expected": wts_updates[37271]})

    # w2an: Ярость (Grunt, R)
    wts_updates[37266] = "|cffe4cfa3Ярость|r"
    wts_updates[37267] = "|cffe4cfa3Ярость|r (|cffffffffR|r)"
    wts_updates[27227] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Рубака впадает в ярость, ускоряя атаку на |cffc8e087+20%|cffced4da и скорость передвижения на |cffc8e087+15%|cffced4da на |cffffffff9|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "w2an", "field": "name", "expected": wts_updates[37266]})
    checks_def.append({"type": "ability", "id": "w2an", "field": "tip1", "expected": wts_updates[37267]})
    checks_def.append({"type": "ability", "id": "w2an", "field": "ubertip1", "expected": wts_updates[27227]})

    # w2ap: Резня слабаков (Orgrim Doomhammer, 2 levels)
    wts_updates[37306] = "|cffe4cfa3Резня слабаков|r"
    wts_updates[37311] = "|cffe4cfa3Резня слабаков|r"
    wts_updates[37312] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Многократно увеличивает урон атак по обычным воинам.|r"
    wts_updates[37307] = "|cffe4cfa3Резня слабаков — уровень 1|r (|cffffffffS|r)"
    wts_updates[37308] = "|cffe4cfa3Резня слабаков — уровень 2|r (|cffffffffS|r)"
    wts_updates[37310] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон атак по обычным воинам (не героям) в |cffffffff3|cffced4da раза.|r"
    wts_updates[32681] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон атак по обычным воинам (не героям) в |cffffffff4|cffced4da раза.|r"
    checks_def.append({"type": "ability", "id": "w2ap", "field": "name", "expected": wts_updates[37306]})

    # w2as: Ракетный обстрел (Zeppelin)
    wts_updates[37272] = "|cffe4cfa3Ракетный обстрел|r"
    wts_updates[37273] = "|cffe4cfa3Ракетный обстрел|r"
    checks_def.append({"type": "ability", "id": "w2as", "field": "name", "expected": wts_updates[37272]})
    checks_def.append({"type": "ability", "id": "w2as", "field": "tip1", "expected": wts_updates[37273]})

    # w2av: Сфера разрушения (Death Knight)
    wts_updates[37259] = "|cffe4cfa3Сфера разрушения|r"
    wts_updates[37260] = "|cffe4cfa3Сфера разрушения|r"
    wts_updates[37261] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон атаки на |cffc8e087+20|cffced4da ед. и наделяет атаки сплеш-уроном по области.|r"
    checks_def.append({"type": "ability", "id": "w2av", "field": "name", "expected": wts_updates[37259]})
    checks_def.append({"type": "ability", "id": "w2av", "field": "tip1", "expected": wts_updates[37260]})
    checks_def.append({"type": "ability", "id": "w2av", "field": "ubertip1", "expected": wts_updates[37261]})

    # w2ax: Рассеивание заклинаний (Priest, D)
    wts_updates[35606] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[35784] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffD|r)"
    wts_updates[36762] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает все магические эффекты с союзников и противников в выбранной области.|r"
    checks_def.append({"type": "ability", "id": "w2ax", "field": "name", "expected": wts_updates[35606]})
    checks_def.append({"type": "ability", "id": "w2ax", "field": "tip1", "expected": wts_updates[35784]})
    checks_def.append({"type": "ability", "id": "w2ax", "field": "ubertip1", "expected": wts_updates[36762]})

    # w2az: Исцеление (Priest, E)
    wts_updates[31629] = "|cffe4cfa3Исцеление|r"
    wts_updates[30004] = "|cffe4cfa3Исцеление|r (|cffffffffE|r)"
    checks_def.append({"type": "ability", "id": "w2az", "field": "name", "expected": wts_updates[31629]})
    checks_def.append({"type": "ability", "id": "w2az", "field": "tip1", "expected": wts_updates[30004]})

    # w284, w285: Сопротивление магии (Ogre)
    wts_updates[38304] = "|cffe4cfa3Сопротивление магии|r"
    wts_updates[38303] = "|cffe4cfa3Сопротивление магии|r"
    wts_updates[27982] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Толстая шкура огра поглощает магию, снижая получаемый урон от вражеских заклинаний до |cffffffff35%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "w284", "field": "name", "expected": wts_updates[38304]})
    checks_def.append({"type": "ability", "id": "w284", "field": "tip1", "expected": wts_updates[38303]})
    checks_def.append({"type": "ability", "id": "w284", "field": "ubertip1", "expected": wts_updates[27982]})

    # w288: Пламенное дыхание (Dragon, F)
    wts_updates[37769] = "|cffe4cfa3Пламенное дыхание|r"
    wts_updates[37770] = "|cffe4cfa3Пламенное дыхание|r (|cffffffffF|r)"
    wts_updates[37771] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выдыхает конус бушующего пламени, нанося |cffffffff55|cffced4da ед. урона врагам на линии огня.|r"
    checks_def.append({"type": "ability", "id": "w288", "field": "name", "expected": wts_updates[37769]})
    checks_def.append({"type": "ability", "id": "w288", "field": "tip1", "expected": wts_updates[37770]})
    checks_def.append({"type": "ability", "id": "w288", "field": "ubertip1", "expected": wts_updates[37771]})

    # w289: Огненный столб (Dragon, C)
    wts_updates[37767] = "|cffe4cfa3Огненный столб|r"
    wts_updates[37768] = "|cffe4cfa3Огненный столб|r (|cffffffffC|r)"
    checks_def.append({"type": "ability", "id": "w289", "field": "name", "expected": wts_updates[37767]})
    checks_def.append({"type": "ability", "id": "w289", "field": "tip1", "expected": wts_updates[37768]})

    # w290: Прочная чешуя (Dragon)
    wts_updates[37765] = "|cffe4cfa3Прочная чешуя|r"
    wts_updates[37766] = "|cffe4cfa3Прочная чешуя|r"
    wts_updates[4677] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бронированная чешуя дракона снижает получаемый от вражеских атак урон на |cffc8e0876|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "w290", "field": "name", "expected": wts_updates[37765]})
    checks_def.append({"type": "ability", "id": "w290", "field": "tip1", "expected": wts_updates[37766]})
    checks_def.append({"type": "ability", "id": "w290", "field": "ubertip1", "expected": wts_updates[4677]})

    # w294: Драконы-защитники
    wts_updates[37761] = "|cffe4cfa3Драконы-защитники|r"
    wts_updates[37762] = "|cffe4cfa3Драконы-защитники|r"
    wts_updates[37763] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает запас здоровья красных драконов и наделяет их способностью «Прочная чешуя».|r"
    checks_def.append({"type": "ability", "id": "w294", "field": "name", "expected": wts_updates[37761]})
    checks_def.append({"type": "ability", "id": "w294", "field": "tip1", "expected": wts_updates[37762]})
    checks_def.append({"type": "ability", "id": "w294", "field": "ubertip1", "expected": wts_updates[37763]})

    # w295: Драконы-поджигатели
    wts_updates[37758] = "|cffe4cfa3Драконы-поджигатели|r"
    wts_updates[37759] = "|cffe4cfa3Драконы-поджигатели|r"
    wts_updates[37760] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет красных драконов заклинаниями «Огненный столб» и «Пламенное дыхание».|r"
    checks_def.append({"type": "ability", "id": "w295", "field": "name", "expected": wts_updates[37758]})
    checks_def.append({"type": "ability", "id": "w295", "field": "tip1", "expected": wts_updates[37759]})
    checks_def.append({"type": "ability", "id": "w295", "field": "ubertip1", "expected": wts_updates[37760]})

    # w297: Драконы-огнепускатели
    wts_updates[11818] = "|cffe4cfa3Драконы-огнепускатели|r"
    wts_updates[11958] = "|cffe4cfa3Драконы-огнепускатели|r"
    wts_updates[37757] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон атак красных драконов на |cffc8e087+25|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "w297", "field": "name", "expected": wts_updates[11818]})
    checks_def.append({"type": "ability", "id": "w297", "field": "tip1", "expected": wts_updates[11958]})
    checks_def.append({"type": "ability", "id": "w297", "field": "ubertip1", "expected": wts_updates[37757]})

    # w296: Обстрел (Zeppelin)
    wts_updates[37399] = "|cffe4cfa3Обстрел|r"
    wts_updates[37400] = "|cffe4cfa3Обстрел|r"
    wts_updates[26773] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дирижабль раз в |cffffffff5|cffced4da сек. выпускает залп ракет по наземным противникам.|r"
    checks_def.append({"type": "ability", "id": "w296", "field": "name", "expected": wts_updates[37399]})
    checks_def.append({"type": "ability", "id": "w296", "field": "tip1", "expected": wts_updates[37400]})
    checks_def.append({"type": "ability", "id": "w296", "field": "ubertip1", "expected": wts_updates[26773]})

    # w298: Страх (Cho'gall, 2 levels)
    wts_updates[37398] = "|cffe4cfa3Страх|r"
    wts_updates[37395] = "|cffe4cfa3Страх|r"
    wts_updates[37396] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повергает врагов в панический страх, лишая возможности атаковать.|r"
    wts_updates[37391] = "|cffe4cfa3Страх — уровень 1|r (|cffffffffF|r)"
    wts_updates[37392] = "|cffe4cfa3Страх — уровень 2|r (|cffffffffF|r)"
    wts_updates[37393] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наводит ужас на врагов в радиусе |cffffffff350|cffced4da на |cffffffff10|cffced4da сек., запрещая им атаковать.|r"
    wts_updates[37394] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наводит ужас на врагов в радиусе |cffffffff350|cffced4da на |cffffffff10|cffced4da сек., запрещая им атаковать.|r"
    checks_def.append({"type": "ability", "id": "w298", "field": "name", "expected": wts_updates[37398]})

    # w299: Поле развоплощения (Cho'gall, 4 levels)
    wts_updates[37384] = "|cffe4cfa3Поле развоплощения|r"
    wts_updates[37385] = "|cffe4cfa3Поле развоплощения|r"
    wts_updates[37386] = "|cffe4cfa3Поле развоплощения — уровень 1|r (|cffffffffD|r)"
    wts_updates[37387] = "|cffe4cfa3Поле развоплощения — уровень 2|r (|cffffffffD|r)"
    wts_updates[37388] = "|cffe4cfa3Поле развоплощения — уровень 3|r (|cffffffffD|r)"
    wts_updates[37389] = "|cffe4cfa3Поле развоплощения — уровень 4|r (|cffffffffD|r)"
    wts_updates[9844] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создает искаженное магическое поле в радиусе |cffffffff165|cffced4da, наносящее урон и замедляющее противников.|r"
    checks_def.append({"type": "ability", "id": "w299", "field": "name", "expected": wts_updates[37384]})

    # A1JO: Взять на борт (Zeppelin, L)
    wts_updates[32683] = "|cffe4cfa3Взять на борт|r"
    wts_updates[32684] = "|cffe4cfa3Взять на борт|r (|cffffffffL|r)"
    wts_updates[32685] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Забирает на борт наземного союзника для воздушной перевозки.|r"
    checks_def.append({"type": "ability", "id": "A1JO", "field": "name", "expected": wts_updates[32683]})
    checks_def.append({"type": "ability", "id": "A1JO", "field": "tip1", "expected": wts_updates[32684]})
    checks_def.append({"type": "ability", "id": "A1JO", "field": "ubertip1", "expected": wts_updates[32685]})

    # =========================================================================
    # BUILD PLAN DATA
    # =========================================================================
    plan_data = {
        "race": "Horde of the Second War",
        "race_name_ru": "Орда Второй Войны",
        "race_id": 35,
        "wts_updates": wts_updates,
        "checks_def": checks_def,
        "categories": {
            "buildings": [
                "w20q", "w20w", "w20e", "w20r", "w20y", "w214", "w20a", "w20u", "w20t", "w20i", "w210", "w218", "w219"
            ],
            "units": [
                "w200", "w208", "w203", "w204", "xd04", "w209", "w211", "w205", "xd01", "xd06",
                "w207", "w201", "w206", "xd02", "xd05", "w202", "xd07", "h0D4", "h0D6", "h0D5", "w220"
            ],
            "heroes": [
                "W200", "W201", "W202", "W203"
            ],
            "upgrades": [
                "R0KB", "R0KC", "R0KD", "w2r0", "w2r1", "w2r2", "w2r3", "w2r4", "w2r5", "w2r6",
                "w2r7", "w2r8", "w2r9", "w2ra", "w2rb", "w2re", "w2rq", "w286", "w291", "w292", "w293"
            ],
            "abilities": [
                "A1JN", "w2a0", "w2a1", "w2a2", "w2a3", "w2a4", "w2a5", "w2a6", "w2a8", "w2a9",
                "w2aA", "w2aQ", "w2aW", "w2aZ", "w2ab", "w2ac", "w2ad", "w2af", "w2ag", "w2ah",
                "w2ak", "w2al", "w2am", "w2an", "w2ap", "w2as", "w2av", "w2ax", "w2az", "w284",
                "w285", "w288", "w289", "w290", "w294", "w295", "w296", "w297", "w298", "w299", "A1JO"
            ]
        }
    }

    plan_path = folder / "hordew2_plan.json"
    plan_path.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote plan to {plan_path} with {len(wts_updates)} strings and {len(checks_def)} checks.")

    # =========================================================================
    # GENERATE CATEGORY REGISTRIES IN docs/ui_text/
    # =========================================================================
    raw_dump = json.loads((ROOT / "scripts/hordew2_raw_dump.json").read_text(encoding="utf-8"))

    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    # 1. hordew2_selection.json
    sel_data = {
        "scope": "Орда Второй Войны (HordeW2): подсказка выбора расы A1JN и маркеры фракции R0KB, R0KC, R0KD",
        "object": "A1JN",
        "variants": ["SD"],
        "hotkey": {"value": "Z"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_HordeW2 регистрирует способность A1JN.",
            "При выборе создаются 5 рабочих w200, исследуется маркер R0KB, удаляется выбирающий юнит.",
            "Горячая клавиша Z, создатель VinerX, куратор VinerX, сложность 3/5 (●●●○○), период «Warcraft II: Tides of Darkness»."
        ],
        "strings": [
            {"field": "name", "wts_id": 26684, "after": wts_updates[26684]},
            {"field": "tip1", "wts_id": 35847, "after": wts_updates[35847]},
            {"field": "ubertip1", "wts_id": 25701, "after": wts_updates[25701]}
        ],
        "markers": [
            {
                "id": "R0KB",
                "name": "Орда Второй Войны (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 32677, "after": wts_updates[32677]},
                    {"field": "tip1", "wts_id": 32678, "after": wts_updates[32678]}
                ]
            },
            {
                "id": "R0KC",
                "name": "Орда Скверны или Орда Второй Войны (маркер выбора)",
                "strings": [
                    {"field": "name1", "wts_id": 5595, "after": wts_updates[5595]},
                    {"field": "tip1", "wts_id": 5596, "after": wts_updates[5596]},
                    {"field": "ubertip1", "wts_id": 27305, "after": wts_updates[27305]}
                ]
            },
            {
                "id": "R0KD",
                "name": "Культ Сумеречного Молота (маркер ветви)",
                "strings": [
                    {"field": "name1", "wts_id": 5598, "after": wts_updates[5598]},
                    {"field": "tip1", "wts_id": 5599, "after": wts_updates[5599]},
                    {"field": "ubertip1", "wts_id": 37033, "after": wts_updates[37033]}
                ]
            }
        ]
    }
    (folder / "hordew2_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote hordew2_selection.json")

    # 2. hordew2_buildings.json
    bld_entries = []
    for b in raw_dump["buildings"]:
        b_id = b["id"]
        if b_id not in plan_data["categories"]["buildings"]:
            continue
        hk_val = b.get("hotkey")
        entry = {"id": b_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(b.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        bld_entries.append(entry)

    bld_data = {
        "scope": f"Орда Второй Войны (HordeW2): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "hordew2_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote hordew2_buildings.json ({len(bld_entries)} buildings)")

    # 3. hordew2_units.json
    unit_entries = []
    for u in raw_dump["units"]:
        u_id = u["id"]
        if u_id not in plan_data["categories"]["units"]:
            continue
        hk_val = u.get("hotkey")
        entry = {"id": u_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(u.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        unit_entries.append(entry)

    unit_data = {
        "scope": f"Орда Второй Войны (HordeW2): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "hordew2_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote hordew2_units.json ({len(unit_entries)} units)")

    # 4. hordew2_heroes.json
    hero_entries = []
    for h in raw_dump["heroes"]:
        h_id = h["id"]
        if h_id not in plan_data["categories"]["heroes"]:
            continue
        hk_val = h.get("hotkey")
        entry = {"id": h_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(h.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        hero_entries.append(entry)

    hero_data = {
        "scope": f"Орда Второй Войны (HordeW2): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "hordew2_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote hordew2_heroes.json ({len(hero_entries)} heroes)")

    # 5. hordew2_abilities.json
    abil_entries = []
    for a in raw_dump["abilities"]:
        a_id = a["id"]
        if a_id not in plan_data["categories"]["abilities"]:
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
        "scope": f"Орда Второй Войны (HordeW2): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "hordew2_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote hordew2_abilities.json ({len(abil_entries)} abilities)")

    # 6. hordew2_research.json
    upg_entries = []
    for u in raw_dump["upgrades"]:
        u_id = u["id"]
        if u_id not in plan_data["categories"]["upgrades"]:
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
        if entry["strings"]:
            upg_entries.append(entry)

    upg_data = {
        "scope": f"Орда Второй Войны (HordeW2): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "hordew2_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote hordew2_research.json ({len(upg_entries)} upgrades)")

    # 7. hordew2_audit.json
    audit_data = {
        "race": "Орда Второй Войны (HordeW2)",
        "race_id": 35,
        "selection_ability": "A1JN",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "town_halls": {
                    "tier1": {"id": "w20q", "name": "Дом вождей", "food": 50},
                    "tier2": {"id": "w20w", "name": "Крепость", "food": 100},
                    "tier3": {"id": "w20e", "name": "Цитадель", "food": 150}
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
                    "W200": "Вождь Клана (Оргрим Молот Рока, Сила, ближний бой)",
                    "W201": "Сумеречный маг (Чо'Галл, Интеллект, дальний бой)",
                    "W202": "Предводитель троллей (Зул'джин, Ловкость, дальний бой)",
                    "W203": "Мэйм Блэкхенд (Мастер клинка, Ловкость, ближний бой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(wts_updates)
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0KB": "Маркер расы Орда Второй Войны",
                    "R0KC": "Маркер выбора между Ордой Скверны и Ордой Второй Войны",
                    "R0KD": "Маркер выбора ветви Культа Сумеречного Молота"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items found for HordeW2."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific triggers/chat messages found for HordeW2."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": ["Bblo", "Bfro", "Bhea", "Binv", "Bpig"],
            "status": "No custom buffs with unstandardized text found."
        },
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def)
    }
    (folder / "hordew2_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote hordew2_audit.json")

if __name__ == "__main__":
    main()
