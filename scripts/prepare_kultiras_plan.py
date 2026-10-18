# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Kul Tiras race (Race 17)."""
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
    # 1. RACE SELECTION & MARKERS: A0HO, R07D, R0HX
    # =========================================================================
    # A0HO
    wts_updates[38869] = "|cffe4cfa3Кул-Тирас|r"
    wts_updates[38870] = "|cffe4cfa3Кул-Тирас|r (|cffffffffX|r)"
    wts_updates[28524] = (
        "|cffa6afb8РАСА:|cffced4da Могущественное островное королевство мореплавателей, опирающееся на несокрушимый флот, жрецов шторма и дисциплинированную морскую пехоту.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●|cffa6afb8●●●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Битва за Азерот»|r|n|n"
        "|cffced4daКул-Тирас был основан бесстрашными исследователями, бороздившими неизведанные воды в поисках славы и торговых путей. "
        "Когда-то эта нация была одним из ключевых оплотов Альянса Лордерона, а её легендарный флот безраздельно царил на морях Азерота. "
        "Пережив годы смуты, внутренних расколов и угрозы тёмных сил глубин, сыны и дочери Кул-Тираса вновь объединились под знаменем дома Праудмуров, "
        "сочетая тяжёлую пехоту, отважных морских волков, разрушительные мортиры и сокрушительную магию морских приливов.|r"
    )

    checks_def.append({"type": "ability", "id": "A0HO", "field": "name", "expected": wts_updates[38869]})
    checks_def.append({"type": "ability", "id": "A0HO", "field": "tip1", "expected": wts_updates[38870]})
    checks_def.append({"type": "ability", "id": "A0HO", "field": "ubertip1", "expected": wts_updates[28524]})

    # Selection markers: R07D, R0HX
    wts_updates[9500] = "|cffe4cfa3Кул-Тирас|r"
    wts_updates[9591] = "|cffe4cfa3Кул-Тирас|r"
    wts_updates[20111] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Кул-Тирасу.|r"

    wts_updates[30266] = "|cffe4cfa3Кул-Тирас или Альянс|r"
    wts_updates[29942] = "|cffe4cfa3Кул-Тирас или Альянс|r"

    checks_def.append({"type": "upgrade", "id": "R07D", "field": "name1", "expected": wts_updates[9500]})
    checks_def.append({"type": "upgrade", "id": "R07D", "field": "tip1", "expected": wts_updates[9591]})
    checks_def.append({"type": "upgrade", "id": "R07D", "field": "ubertip1", "expected": wts_updates[20111]})
    checks_def.append({"type": "upgrade", "id": "R0HX", "field": "name1", "expected": wts_updates[30266]})
    checks_def.append({"type": "upgrade", "id": "R0HX", "field": "tip1", "expected": wts_updates[29942]})

    # =========================================================================
    # 2. BUILDINGS (13 buildings)
    # =========================================================================
    # h01X: Ратуша (Q)
    wts_updates[17330] = "|cffe4cfa3Ратуша|r"
    wts_updates[4498] = "|cffe4cfa3Ратуша|r (|cffffffffQ|r)"
    wts_updates[4499] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Кул-Тираса первой ступени. Обучает работников и служит складом древесины.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deФорт|cffced4da: открывает доступ к передовым сооружениям и войскам Кул-Тираса.|r"
    )
    checks_def.append({"type": "unit", "id": "h01X", "field": "name", "expected": wts_updates[17330]})
    checks_def.append({"type": "unit", "id": "h01X", "field": "tip", "expected": wts_updates[4498]})
    checks_def.append({"type": "unit", "id": "h01X", "field": "ubertip", "expected": wts_updates[4499]})

    # h01Y: Форт (U)
    wts_updates[17332] = "|cffe4cfa3Форт|r"
    wts_updates[17333] = "|cffe4cfa3Форт|r (|cffffffffU|r)"
    wts_updates[10185] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Кул-Тираса второй ступени. Открывает доступ к Храму Жрецов Моря, Мастерской и передовым войскам.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deИнвестировать в Флот|cffced4da.|n- |cffa9c7deИнвестировать в Армию|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЗамок|cffced4da: открывает доступ к высшим военным технологиям и элитным силам флота.|r"
    )
    checks_def.append({"type": "unit", "id": "h01Y", "field": "name", "expected": wts_updates[17332]})
    checks_def.append({"type": "unit", "id": "h01Y", "field": "tip", "expected": wts_updates[17333]})
    checks_def.append({"type": "unit", "id": "h01Y", "field": "ubertip", "expected": wts_updates[10185]})

    # h01Z: Замок (U)
    wts_updates[17334] = "|cffe4cfa3Замок|r"
    wts_updates[17335] = "|cffe4cfa3Замок|r (|cffffffffU|r)"
    wts_updates[10186] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Кул-Тираса третьей ступени. Открывает доступ к высшим военным технологиям и элитным силам флота.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h01Z", "field": "name", "expected": wts_updates[17334]})
    checks_def.append({"type": "unit", "id": "h01Z", "field": "tip", "expected": wts_updates[17335]})
    checks_def.append({"type": "unit", "id": "h01Z", "field": "ubertip", "expected": wts_updates[10186]})

    # h020: Оружейная (S)
    wts_updates[17336] = "|cffe4cfa3Оружейная|r"
    wts_updates[17337] = "|cffe4cfa3Оружейная|r (|cffffffffS|r)"
    wts_updates[12960] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Кузница и арсенал Кул-Тираса. Разрабатывает базовые улучшения атаки и защиты пехоты, стрелков и заклинателей.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЖелезные мечи|cffced4da: увеличивает урон ближнего боя.|n"
        "- |cffa9c7deЖелезная броня|cffced4da: повышает защиту тяжелой пехоты.|n"
        "- |cffa9c7deДоспехи из клепаной кожи|cffced4da: повышает защиту стрелков и морских волков.|n"
        "- |cffa9c7deЧерный порох|cffced4da: увеличивает урон стрелков и мортир.|n"
        "- |cffa9c7deМагическая атака|cffced4da: увеличивает урон жрецов штормов.|r"
    )
    checks_def.append({"type": "unit", "id": "h020", "field": "name", "expected": wts_updates[17336]})
    checks_def.append({"type": "unit", "id": "h020", "field": "tip", "expected": wts_updates[17337]})
    checks_def.append({"type": "unit", "id": "h020", "field": "ubertip", "expected": wts_updates[12960]})

    # h021: Глубинный Алтарь (A)
    wts_updates[17338] = "|cffe4cfa3Глубинный Алтарь|r"
    wts_updates[17339] = "|cffe4cfa3Глубинный Алтарь|r (|cffffffffA|r)"
    wts_updates[12955] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священный алтарь глубин. Позволяет призывать легендарных героев Кул-Тираса и воскрешать их в случае гибели.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deКапитан|cffced4da: мастер фехтования и дуэлей.|n"
        "- |cffa9c7deВерховная Жрица Морей|cffced4da: повелительница стихии воды и морозных штормов.|n"
        "- |cffa9c7deАдмирал|cffced4da: закалённый флотоводец и мастер меткой стрельбы.|r"
    )
    checks_def.append({"type": "unit", "id": "h021", "field": "name", "expected": wts_updates[17338]})
    checks_def.append({"type": "unit", "id": "h021", "field": "tip", "expected": wts_updates[17339]})
    checks_def.append({"type": "unit", "id": "h021", "field": "ubertip", "expected": wts_updates[12955]})

    # h0G6: Глубинный Алтарь (A)
    wts_updates[18235] = "|cffe4cfa3Глубинный Алтарь|r"
    wts_updates[18236] = "|cffe4cfa3Глубинный Алтарь|r (|cffffffffA|r)"
    wts_updates[22586] = wts_updates[12955]
    checks_def.append({"type": "unit", "id": "h0G6", "field": "name", "expected": wts_updates[18235]})
    checks_def.append({"type": "unit", "id": "h0G6", "field": "tip", "expected": wts_updates[18236]})
    checks_def.append({"type": "unit", "id": "h0G6", "field": "ubertip", "expected": wts_updates[22586]})

    # h022: Казармы (B)
    wts_updates[17340] = "|cffe4cfa3Казармы|r"
    wts_updates[17341] = "|cffe4cfa3Казармы|r (|cffffffffB|r)"
    wts_updates[12956] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военный комплекс для подготовки регулярных сухопутных войск Кул-Тираса.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПехотинец|cffced4da.|n"
        "- |cffa9c7deСтрелок|cffced4da.|n"
        "- |cffa9c7deГвардеец|cffced4da.|n"
        "- |cffa9c7deРыцарь|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da.|n"
        "- |cffa9c7deПерековка меча|cffced4da.|n"
        "- |cffa9c7deМастерство|cffced4da.|n"
        "- |cffa9c7deТренировка ветерана|cffced4da.|n"
        "- |cffa9c7deУкрепленные тяжелые доспехи|cffced4da.|n"
        "- |cffa9c7deУдлиненные стволы|cffced4da.|n"
        "- |cffa9c7deТренировка с порохом|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h022", "field": "name", "expected": wts_updates[17340]})
    checks_def.append({"type": "unit", "id": "h022", "field": "tip", "expected": wts_updates[17341]})
    checks_def.append({"type": "unit", "id": "h022", "field": "ubertip", "expected": wts_updates[12956]})

    # h023: Лесопилка (L)
    wts_updates[17342] = "|cffe4cfa3Лесопилка|r"
    wts_updates[17343] = "|cffe4cfa3Лесопилка|r (|cffffffffL|r)"
    wts_updates[12961] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Лесопильный комбинат Кул-Тираса. Служит складом древесины и центром укрепления построек.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенная кладка|cffced4da: повышает прочность и броню построек.|n"
        "- |cffa9c7deУлучшенные топоры|cffced4da: увеличивает переносимый работниками объём древесины.|r"
    )
    checks_def.append({"type": "unit", "id": "h023", "field": "name", "expected": wts_updates[17342]})
    checks_def.append({"type": "unit", "id": "h023", "field": "tip", "expected": wts_updates[17343]})
    checks_def.append({"type": "unit", "id": "h023", "field": "ubertip", "expected": wts_updates[12961]})

    # h024: Ферма (F)
    wts_updates[17344] = "|cffe4cfa3Ферма|r"
    wts_updates[17345] = "|cffe4cfa3Ферма|r (|cffffffffF|r)"
    wts_updates[31626] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Кул-Тираса запасом пищи и вырабатывает регулярный доход.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+20|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h024", "field": "name", "expected": wts_updates[17344]})
    checks_def.append({"type": "unit", "id": "h024", "field": "tip", "expected": wts_updates[17345]})
    checks_def.append({"type": "unit", "id": "h024", "field": "ubertip", "expected": wts_updates[31626]})

    # h025: Сторожевая Башня (T)
    wts_updates[9696] = "|cffe4cfa3Сторожевая Башня|r"
    wts_updates[11394] = "|cffe4cfa3Сторожевая Башня|r (|cffffffffT|r)"
    wts_updates[31627] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное укрепление Кул-Тираса. Ведёт автоматический обстрел приближающихся противников.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h025", "field": "name", "expected": wts_updates[9696]})
    checks_def.append({"type": "unit", "id": "h025", "field": "tip", "expected": wts_updates[11394]})
    checks_def.append({"type": "unit", "id": "h025", "field": "ubertip", "expected": wts_updates[31627]})

    # h026: Храм Жрецов Моря (M)
    wts_updates[11908] = "|cffe4cfa3Храм Жрецов Моря|r"
    wts_updates[12080] = "|cffe4cfa3Храм Жрецов Моря|r (|cffffffffM|r)"
    wts_updates[12953] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище морских жрецов и полевых целителей Кул-Тираса.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЖрец Штормов|cffced4da.|n"
        "- |cffa9c7deПалубный Доктор|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deФолиант познаний магии морей|cffced4da.|n"
        "- |cffa9c7deОбучение доктора|cffced4da.|n"
        "- |cffa9c7deВысшее познание|cffced4da.|n"
        "- |cffa9c7deЖертвоприношение Владыкам Моря|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h026", "field": "name", "expected": wts_updates[11908]})
    checks_def.append({"type": "unit", "id": "h026", "field": "tip", "expected": wts_updates[12080]})
    checks_def.append({"type": "unit", "id": "h026", "field": "ubertip", "expected": wts_updates[12953]})

    # h027: Мастерская (W)
    wts_updates[12166] = "|cffe4cfa3Мастерская|r"
    wts_updates[12260] = "|cffe4cfa3Мастерская|r (|cffffffffW|r)"
    wts_updates[12954] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военная мануфактура Кул-Тираса. Подготавливает тяжелых алебардщиков, морских волков и мортирные расчеты, а также исследует артиллерийские технологии.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deАлебардщик|cffced4da.|n"
        "- |cffa9c7deМорской волк|cffced4da.|n"
        "- |cffa9c7deМортирный расчет|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deШрапнель|cffced4da.|n"
        "- |cffa9c7deЗаточка и освящение|cffced4da.|n"
        "- |cffa9c7deСвинцовые пули|cffced4da.|n"
        "- |cffa9c7deНовый сплав|cffced4da.|n"
        "- |cffa9c7deУвеличение количества пороха|cffced4da.|n"
        "- |cffa9c7deОглушающий выстрел|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h027", "field": "name", "expected": wts_updates[12166]})
    checks_def.append({"type": "unit", "id": "h027", "field": "tip", "expected": wts_updates[12260]})
    checks_def.append({"type": "unit", "id": "h027", "field": "ubertip", "expected": wts_updates[12954]})

    # kt02: Храм Моря (C)
    wts_updates[31999] = "|cffe4cfa3Храм Моря|r"
    wts_updates[20294] = "|cffe4cfa3Храм Моря|r (|cffffffffC|r)"
    wts_updates[25340] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Величественный морской собор Кул-Тираса. Служит центром подношений морским божествам и сбора авангардных отрядов королевства.|r"
    )
    checks_def.append({"type": "unit", "id": "kt02", "field": "name", "expected": wts_updates[31999]})
    checks_def.append({"type": "unit", "id": "kt02", "field": "tip", "expected": wts_updates[20294]})
    checks_def.append({"type": "unit", "id": "kt02", "field": "ubertip", "expected": wts_updates[25340]})

    # =========================================================================
    # 3. HEROES (3 heroes)
    # =========================================================================
    # H01L: Капитан (Z)
    wts_updates[5232] = "|cffe4cfa3Капитан|r"
    wts_updates[15170] = "|cffe4cfa3Капитан|r (|cffffffffZ|r)"
    wts_updates[5233] = "|cffe4cfa3Капитан|r"
    wts_updates[31618] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Опытный командир морской пехоты, виртуозно владеющий клинком в ближнем бою.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНаследная Ловкость|cffced4da: повышает шанс уклонения и критического удара.|n"
        "- |cffa9c7deУдарная волна|cffced4da: поражает врагов перед собой разрушительной волной силы.|n"
        "- |cffa9c7deМастер Дуэлянт|cffced4da: увеличивает физический урон по вражеским героям.|n"
        "- |cffa9c7deРодовые мечи|cffced4da: значительно повышает ловкость героя.|n|n"
        "Атакует наземные цели.|r"
    )
    wts_updates[5231] = "|cffe4cfa3Капитан|r"
    checks_def.append({"type": "unit", "id": "H01L", "field": "name", "expected": wts_updates[5232]})
    checks_def.append({"type": "unit", "id": "H01L", "field": "tip", "expected": wts_updates[15170]})
    checks_def.append({"type": "unit", "id": "H01L", "field": "propernames", "expected": wts_updates[5231]})
    checks_def.append({"type": "unit", "id": "H01L", "field": "ubertip", "expected": wts_updates[31618]})

    # H01N: Верховная Жрица Морей (X)
    wts_updates[5243] = "|cffe4cfa3Верховная Жрица Морей|r"
    wts_updates[15172] = "|cffe4cfa3Верховная Жрица Морей|r (|cffffffffX|r)"
    wts_updates[5244] = "|cffe4cfa3Верховная Жрица Морей|r"
    wts_updates[5246] = "|cffe4cfa3Верховная Жрица Морей|r"
    wts_updates[31619] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могущественная морская волшебница, повелевающая ледяными штормами и стихией океана.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСнежная буря|cffced4da: обрушивает на область ледяные осколки, наносящие урон волнами.|n"
        "- |cffa9c7deЛедяное удушение|cffced4da: заковывает противников во льды, оглушая и нанося урон.|n"
        "- |cffa9c7deПризыв элементаля воды|cffced4da: призывает водных духов океана.|n"
        "- |cffa9c7deАбсолютная Защита|cffced4da: колоссально увеличивает броню находящихся рядом союзников.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H01N", "field": "name", "expected": wts_updates[5243]})
    checks_def.append({"type": "unit", "id": "H01N", "field": "tip", "expected": wts_updates[15172]})
    checks_def.append({"type": "unit", "id": "H01N", "field": "propernames", "expected": wts_updates[5246]})
    checks_def.append({"type": "unit", "id": "H01N", "field": "ubertip", "expected": wts_updates[31619]})

    # H01K: Адмирал (C)
    wts_updates[5228] = "|cffe4cfa3Адмирал|r"
    wts_updates[15167] = "|cffe4cfa3Адмирал|r (|cffffffffC|r)"
    wts_updates[5229] = "|cffe4cfa3Адмирал|r"
    wts_updates[5227] = "|cffe4cfa3Адмирал|r"
    wts_updates[31617] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Закалённый в сражениях командующий флотом, поддерживающий союзников аурами и сокрушающий врагов мощными выстрелами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМассовое исцеление|cffced4da: восстанавливает здоровье союзникам вокруг.|n"
        "- |cffa9c7deОпытность|cffced4da: увеличивает скорость перемещения и регенерацию здоровья союзников.|n"
        "- |cffa9c7deКритический Выстрел|cffced4da: даёт шанс нанести многократный урон при атаке.|n"
        "- |cffa9c7deМеткий Выстрел|cffced4da: точный выстрел, наносящий высокий урон и оглушающий цель.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H01K", "field": "name", "expected": wts_updates[5228]})
    checks_def.append({"type": "unit", "id": "H01K", "field": "tip", "expected": wts_updates[15167]})
    checks_def.append({"type": "unit", "id": "H01K", "field": "propernames", "expected": wts_updates[5227]})
    checks_def.append({"type": "unit", "id": "H01K", "field": "ubertip", "expected": wts_updates[31617]})

    # =========================================================================
    # 4. UNITS (11 standard units + 20 vanguard units)
    # =========================================================================
    # h013: Работник (Q)
    wts_updates[3140] = "|cffe4cfa3Работник|r"
    wts_updates[3141] = "|cffe4cfa3Работник|r (|cffffffffQ|r)"
    wts_updates[20561] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основная рабочая сила Кул-Тираса. Возводит сооружения, добывает золото и древесину, а также ремонтирует повреждённые здания и боевую технику.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДобывать ресурсы|cffced4da: сбор древесины и золота.|n"
        "- |cffa9c7deРемонтировать|cffced4da: восстановление прочности техники и построек.|n"
        "- |cffa9c7deКороткий прыжок|cffced4da: быстрое перемещение на небольшое расстояние.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h013", "field": "name", "expected": wts_updates[3140]})
    checks_def.append({"type": "unit", "id": "h013", "field": "tip", "expected": wts_updates[3141]})
    checks_def.append({"type": "unit", "id": "h013", "field": "ubertip", "expected": wts_updates[20561]})

    # h019: Пехотинец (Q)
    wts_updates[2226] = "|cffe4cfa3Пехотинец|r"
    wts_updates[34624] = "|cffe4cfa3Пехотинец|r (|cffffffffQ|r)"
    wts_updates[38150] = (
        "|cffa6afb8ЮНИТ:|cffced4da Универсальный боец передовой линии Кул-Тираса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da: снижает урон от стрел и отражает пронзающие атаки.|n"
        "- |cffa9c7deМастерство|cffced4da: даёт шанс нанести критический удар.|n"
        "- |cffa9c7deУкрепленные тяжелые доспехи|cffced4da: снижает получаемый физический урон.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h019", "field": "name", "expected": wts_updates[2226]})
    checks_def.append({"type": "unit", "id": "h019", "field": "tip", "expected": wts_updates[34624]})
    checks_def.append({"type": "unit", "id": "h019", "field": "ubertip", "expected": wts_updates[38150]})

    # h01A: Морской волк (W)
    wts_updates[38851] = "|cffe4cfa3Морской волк|r"
    wts_updates[38852] = "|cffe4cfa3Морской волк|r (|cffffffffW|r)"
    wts_updates[38151] = (
        "|cffa6afb8ЮНИТ:|cffced4da Опытный морской стрелок-абордажник Кул-Тираса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСвинцовые пули|cffced4da: увеличивает урон по тяжелой броне.|n"
        "- |cffa9c7deОглушающий выстрел|cffced4da: даёт шанс оглушить врага и нанести дополнительный урон.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01A", "field": "name", "expected": wts_updates[38851]})
    checks_def.append({"type": "unit", "id": "h01A", "field": "tip", "expected": wts_updates[38852]})
    checks_def.append({"type": "unit", "id": "h01A", "field": "ubertip", "expected": wts_updates[38151]})

    # h01C: Рыцарь (R)
    wts_updates[38853] = "|cffe4cfa3Рыцарь|r"
    wts_updates[38854] = "|cffe4cfa3Рыцарь|r (|cffffffffR|r)"
    wts_updates[38152] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный конный всадник Кул-Тираса в тяжелых доспехах.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМастерство|cffced4da: даёт шанс нанести критический удар.|n"
        "- |cffa9c7deУкрепленные тяжелые доспехи|cffced4da: снижает получаемый физический урон.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01C", "field": "name", "expected": wts_updates[38853]})
    checks_def.append({"type": "unit", "id": "h01C", "field": "tip", "expected": wts_updates[38854]})
    checks_def.append({"type": "unit", "id": "h01C", "field": "ubertip", "expected": wts_updates[38152]})

    # h01D: Гвардеец (E)
    wts_updates[4476] = "|cffe4cfa3Гвардеец|r"
    wts_updates[34625] = "|cffe4cfa3Гвардеец|r (|cffffffffE|r)"
    wts_updates[24553] = (
        "|cffa6afb8ЮНИТ:|cffced4da Закалённый ветеран королевской гвардии Кул-Тираса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da: защищает от атак дальнего боя.|n"
        "- |cffa9c7deМастерство|cffced4da: даёт шанс нанести критический удар.|n"
        "- |cffa9c7deУкрепленные тяжелые доспехи|cffced4da: снижает входящий физический урон.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01D", "field": "name", "expected": wts_updates[4476]})
    checks_def.append({"type": "unit", "id": "h01D", "field": "tip", "expected": wts_updates[34625]})
    checks_def.append({"type": "unit", "id": "h01D", "field": "ubertip", "expected": wts_updates[24553]})

    # h01E: Стрелок (W)
    wts_updates[38855] = "|cffe4cfa3Стрелок|r"
    wts_updates[38856] = "|cffe4cfa3Стрелок|r (|cffffffffW|r)"
    wts_updates[38153] = (
        "|cffa6afb8ЮНИТ:|cffced4da Пехотинец дальнего боя, вооружённый дальнобойным мушкетом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСвинцовые пули|cffced4da: увеличивает урон по тяжелой броне.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01E", "field": "name", "expected": wts_updates[38855]})
    checks_def.append({"type": "unit", "id": "h01E", "field": "tip", "expected": wts_updates[38856]})
    checks_def.append({"type": "unit", "id": "h01E", "field": "ubertip", "expected": wts_updates[38153]})

    # h01F: Жрец Штормов (W)
    wts_updates[38857] = "|cffe4cfa3Жрец Штормов|r"
    wts_updates[38858] = "|cffe4cfa3Жрец Штормов|r (|cffffffffW|r)"
    wts_updates[38154] = (
        "|cffa6afb8ЮНИТ:|cffced4da Боевой маг приливов и штормов Кул-Тираса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМорская прохлада|cffced4da: замедляет противников и повышает урон атак.|n"
        "- |cffa9c7deПризыв Духа Моря|cffced4da: призывает морского духа на поле боя.|n"
        "- |cffa9c7deСокрушительная волна|cffced4da: наносит урон наземным врагам на прямой линии.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01F", "field": "name", "expected": wts_updates[38857]})
    checks_def.append({"type": "unit", "id": "h01F", "field": "tip", "expected": wts_updates[38858]})
    checks_def.append({"type": "unit", "id": "h01F", "field": "ubertip", "expected": wts_updates[38154]})

    # h01G: Палубный Доктор (Q)
    wts_updates[4695] = "|cffe4cfa3Палубный Доктор|r"
    wts_updates[34651] = "|cffe4cfa3Палубный Доктор|r (|cffffffffQ|r)"
    wts_updates[24732] = (
        "|cffa6afb8ЮНИТ:|cffced4da Корабельный лекарь и полевой санитар флота Кул-Тираса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМассовое исцеление|cffced4da: восстанавливает здоровье ближайшим союзникам.|n"
        "- |cffa9c7deМассовое восполнение маны|cffced4da: восстанавливает ману союзникам вокруг.|n"
        "- |cffa9c7deМассовый бонус к броне|cffced4da: повышает броню ближайших союзных бойцов.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты и наносит урон призванным существам.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01G", "field": "name", "expected": wts_updates[4695]})
    checks_def.append({"type": "unit", "id": "h01G", "field": "tip", "expected": wts_updates[34651]})
    checks_def.append({"type": "unit", "id": "h01G", "field": "ubertip", "expected": wts_updates[24732]})

    # h01H: Алебардщик (Q)
    wts_updates[4712] = "|cffe4cfa3Алебардщик|r"
    wts_updates[34693] = "|cffe4cfa3Алебардщик|r (|cffffffffQ|r)"
    wts_updates[38155] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый пехотинец ближнего боя с дальнобойной алебардой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗаточка и освящение|cffced4da: увеличивает урон по средней броне.|n"
        "- |cffa9c7deУкрепленные тяжелые доспехи|cffced4da: снижает получаемый физический урон.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01H", "field": "name", "expected": wts_updates[4712]})
    checks_def.append({"type": "unit", "id": "h01H", "field": "tip", "expected": wts_updates[34693]})
    checks_def.append({"type": "unit", "id": "h01H", "field": "ubertip", "expected": wts_updates[38155]})

    # h01I: Мортирный расчет (E)
    wts_updates[12338] = "|cffe4cfa3Мортирный расчет|r"
    wts_updates[12339] = "|cffe4cfa3Мортирный расчет|r (|cffffffffE|r)"
    wts_updates[38156] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойный артиллерийский расчёт осадного действия.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deШрапнель|cffced4da: повышает урон по небронированным и среднебронированным целям.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h01I", "field": "name", "expected": wts_updates[12338]})
    checks_def.append({"type": "unit", "id": "h01I", "field": "tip", "expected": wts_updates[12339]})
    checks_def.append({"type": "unit", "id": "h01I", "field": "ubertip", "expected": wts_updates[38156]})

    # kt00: Линкор Кул-Тираса (E)
    wts_updates[9623] = "|cffe4cfa3Линкор Кул-Тираса|r"
    checks_def.append({"type": "unit", "id": "kt00", "field": "name", "expected": wts_updates[9623]})

    # Vanguard units: h0NC..h0NV (20 units)
    vanguard_map = [
        ("h0NC", 1, 2744, 34695, 31868),
        ("h0ND", 2, 33287, 34696, 33218),
        ("h0NE", 3, 33291, 34697, 33289),
        ("h0NF", 4, 33295, 34701, 33293),
        ("h0NG", 5, 33299, 34702, 33297),
        ("h0NH", 6, 33303, 34707, 33301),
        ("h0NI", 7, 33307, 34708, 33305),
        ("h0NJ", 8, 33311, 34709, 33309),
        ("h0NS", 9, 33343, 34745, 33341),
        ("h0NL", 10, 33315, 34710, 33313),
        ("h0NM", 11, 33319, 34724, 33317),
        ("h0NN", 12, 33323, 34725, 33321),
        ("h0NO", 13, 33327, 34726, 33325),
        ("h0NP", 14, 33331, 34727, 33329),
        ("h0NQ", 15, 33335, 34728, 33333),
        ("h0NR", 16, 33339, 34744, 33337),
        ("h0NK", 17, 33347, 34746, 33345),
        ("h0NT", 18, 33369, 34747, 33349),
        ("h0NU", 19, 33372, 34748, 33371),
        ("h0NV", 20, 33376, 34749, 33374),
    ]

    for uid, idx, name_sid, tip_sid, uber_sid in vanguard_map:
        wts_updates[name_sid] = f"|cffe4cfa3Авангард {idx}|r"
        wts_updates[tip_sid] = f"|cffe4cfa3Авангард {idx}|r (|cffffffffQ|r)"
        wts_updates[uber_sid] = (
            f"|cffa6afb8ЮНИТ:|cffced4da Элитный пехотинец авангарда Кул-Тираса {idx}-го ранга.|n|n"
            "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da: с высокой вероятностью отражает пронзающие атаки.|n"
            "- |cffa9c7deМастерство|cffced4da: даёт шанс нанести критический удар.|n"
            "- |cffa9c7deУкрепленные тяжелые доспехи|cffced4da: снижает получаемый физический урон.|n|n"
            "Атакует наземные цели.|r"
        )
        checks_def.append({"type": "unit", "id": uid, "field": "name", "expected": wts_updates[name_sid]})
        checks_def.append({"type": "unit", "id": uid, "field": "tip", "expected": wts_updates[tip_sid]})
        checks_def.append({"type": "unit", "id": uid, "field": "ubertip", "expected": wts_updates[uber_sid]})

    # =========================================================================
    # 5. UPGRADES / RESEARCHES
    # =========================================================================
    # R027: Инвестировать в Флот (R)
    wts_updates[4524] = "|cffe4cfa3Инвестировать в Флот|r"
    wts_updates[4525] = "|cffe4cfa3Инвестировать в Флот|r (|cffffffffR|r)"
    wts_updates[12585] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает боевые характеристики кораблей флота: скорость боя |cffc8e087+20%|cffced4da, скорость движения |cffc8e087+40%|cffced4da, запас прочности |cffc8e087+140|cffced4da ед. Открывает новые морские технологии.|n|n"
        "|cffe6c07bВнимание: исключает возможность исследования «Инвестировать в Армию».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R027", "field": "name1", "expected": wts_updates[4524]})
    checks_def.append({"type": "upgrade", "id": "R027", "field": "tip1", "expected": wts_updates[4525]})
    checks_def.append({"type": "upgrade", "id": "R027", "field": "ubertip1", "expected": wts_updates[12585]})

    # R02S: Инвестировать в Армию (E)
    wts_updates[4531] = "|cffe4cfa3Инвестировать в Армию|r"
    wts_updates[4532] = "|cffe4cfa3Инвестировать в Армию|r (|cffffffffE|r)"
    wts_updates[32755] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает боевые характеристики сухопутных войск Кул-Тираса: скорость боя |cffc8e087+10%|cffced4da, запас здоровья |cffc8e087+100|cffced4da ед., запас маны |cffc8e087+100|cffced4da ед., регенерацию маны |cffc8e087+20%|cffced4da. Открывает новые военные технологии.|n|n"
        "|cffe6c07bВнимание: исключает возможность исследования «Инвестировать в Флот».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02S", "field": "name1", "expected": wts_updates[4531]})
    checks_def.append({"type": "upgrade", "id": "R02S", "field": "tip1", "expected": wts_updates[4532]})
    checks_def.append({"type": "upgrade", "id": "R02S", "field": "ubertip1", "expected": wts_updates[32755]})

    # R036: Железные мечи (6 levels)
    r036_names = [4790, 4788, 4787, 4786, 4785, 4784]
    r036_tips = [4795, 4794, 4793, 4792, 4791, 4789]
    r036_ubers = [4796, 4797, 4798, 4800, 4799, 4801]
    for i in range(6):
        lvl = i + 1
        wts_updates[r036_names[i]] = "|cffe4cfa3Железные мечи|r"
        wts_updates[r036_tips[i]] = f"|cffe4cfa3Железные мечи — уровень {lvl}|r (|cffffffffM|r)"
        wts_updates[r036_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак ближнего боя пехоты Кул-Тираса.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da.|n- |cffa9c7deРыцарь|cffced4da.|n- |cffa9c7deГвардеец|cffced4da.|n- |cffa9c7deАлебардщик|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R036", "field": f"name{lvl}", "expected": wts_updates[r036_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R036", "field": f"tip{lvl}", "expected": wts_updates[r036_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R036", "field": f"ubertip{lvl}", "expected": wts_updates[r036_ubers[i]]})

    # R037: Железная броня (6 levels)
    r037_names = [4805, 4807, 4806, 4810, 4809, 4808]
    r037_tips = [4811, 4812, 4813, 4816, 4815, 4814]
    r037_ubers = [4817, 4818, 4819, None, None, None]
    for i in range(6):
        lvl = i + 1
        wts_updates[r037_names[i]] = "|cffe4cfa3Железная броня|r"
        wts_updates[r037_tips[i]] = f"|cffe4cfa3Железная броня — уровень {lvl}|r (|cffffffffA|r)"
        checks_def.append({"type": "upgrade", "id": "R037", "field": f"name{lvl}", "expected": wts_updates[r037_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R037", "field": f"tip{lvl}", "expected": wts_updates[r037_tips[i]]})
        if r037_ubers[i]:
            wts_updates[r037_ubers[i]] = (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает защиту тяжелой пехоты и кавалерии Кул-Тираса.|n|n"
                "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da.|n- |cffa9c7deРыцарь|cffced4da.|n- |cffa9c7deГвардеец|cffced4da.|n- |cffa9c7deАлебардщик|cffced4da.|n|n"
                f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
            )
            checks_def.append({"type": "upgrade", "id": "R037", "field": f"ubertip{lvl}", "expected": wts_updates[r037_ubers[i]]})

    # R038: Доспехи из клепаной кожи (6 levels)
    r038_names = [4826, 4833, 4827, 4844, 4843, 4828]
    r038_tips = [4834, 4835, 4836, 4847, 4846, 4845]
    r038_ubers = [4837, 4838, 4839, 4848, 4849, 4850]
    for i in range(6):
        lvl = i + 1
        wts_updates[r038_names[i]] = "|cffe4cfa3Доспехи из клепаной кожи|r"
        wts_updates[r038_tips[i]] = f"|cffe4cfa3Доспехи из клепаной кожи — уровень {lvl}|r (|cffffffffL|r)"
        wts_updates[r038_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает броню стрелков, морских волков, заклинателей и расчетов мортир.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da.|n- |cffa9c7deМорской волк|cffced4da.|n- |cffa9c7deЖрец Штормов|cffced4da.|n- |cffa9c7deПалубный Доктор|cffced4da.|n- |cffa9c7deМортирный расчет|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R038", "field": f"name{lvl}", "expected": wts_updates[r038_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R038", "field": f"tip{lvl}", "expected": wts_updates[r038_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R038", "field": f"ubertip{lvl}", "expected": wts_updates[r038_ubers[i]]})

    # R039: Черный порох (6 levels)
    r039_names = [4851, 4852, 4853, 4869, 4868, 4867]
    r039_tips = [4854, 4855, 4856, 4872, 4871, 4870]
    r039_ubers = [4857, 4858, 4859, 4873, 4874, 4875]
    for i in range(6):
        lvl = i + 1
        wts_updates[r039_names[i]] = "|cffe4cfa3Черный порох|r"
        wts_updates[r039_tips[i]] = f"|cffe4cfa3Черный порох — уровень {lvl}|r (|cffffffffG|r)"
        wts_updates[r039_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон дистанционных атак стрелков, морских волков и артиллерии.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da.|n- |cffa9c7deМорской волк|cffced4da.|n- |cffa9c7deМортирный расчет|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R039", "field": f"name{lvl}", "expected": wts_updates[r039_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R039", "field": f"tip{lvl}", "expected": wts_updates[r039_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R039", "field": f"ubertip{lvl}", "expected": wts_updates[r039_ubers[i]]})

    # R035: Магическая атака (6 levels)
    r035_names = [4755, 4756, 4757, 4765, 4766, 4767]
    r035_tips = [4758, 4759, 4760, 4768, 4769, 4770]
    r035_ubers = [4761, 4762, 4763, 4771, 4772, 4773]
    for i in range(6):
        lvl = i + 1
        wts_updates[r035_names[i]] = "|cffe4cfa3Магическая атака|r"
        wts_updates[r035_tips[i]] = f"|cffe4cfa3Магическая атака — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[r035_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон магических атак заклинателей Кул-Тираса.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЖрец Штормов|cffced4da.|n- |cffa9c7deПалубный Доктор|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R035", "field": f"name{lvl}", "expected": wts_updates[r035_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R035", "field": f"tip{lvl}", "expected": wts_updates[r035_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R035", "field": f"ubertip{lvl}", "expected": wts_updates[r035_ubers[i]]})

    # R02T: Укрыться за щитом (A)
    wts_updates[4539] = "|cffe4cfa3Укрыться за щитом|r"
    wts_updates[4540] = "|cffe4cfa3Укрыться за щитом|r (|cffffffffA|r)"
    checks_def.append({"type": "upgrade", "id": "R02T", "field": "name1", "expected": wts_updates[4539]})
    checks_def.append({"type": "upgrade", "id": "R02T", "field": "tip1", "expected": wts_updates[4540]})

    # R01U: Перековка меча (3 levels) (D)
    r01u_names = [4510, 4511, 4512]
    r01u_tips = [4513, 4514, 4515]
    r01u_ubers = [15104, 15105, 15106]
    for i in range(3):
        lvl = i + 1
        wts_updates[r01u_names[i]] = "|cffe4cfa3Перековка меча|r"
        wts_updates[r01u_tips[i]] = f"|cffe4cfa3Перековка меча — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[r01u_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает мастерство фехтования и урон атак пехоты ближнего боя.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da.|n- |cffa9c7deГвардеец|cffced4da.|n- |cffa9c7deАлебардщик|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R01U", "field": f"name{lvl}", "expected": wts_updates[r01u_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R01U", "field": f"tip{lvl}", "expected": wts_updates[r01u_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R01U", "field": f"ubertip{lvl}", "expected": wts_updates[r01u_ubers[i]]})

    # R02U: Мастерство (Z)
    wts_updates[4542] = "|cffe4cfa3Мастерство|r"
    wts_updates[4543] = "|cffe4cfa3Мастерство|r (|cffffffffZ|r)"
    wts_updates[4545] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает бойцов искусству критических ударов, даруя способность «Мастерство».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da.|n- |cffa9c7deГвардеец|cffced4da.|n- |cffa9c7deРыцарь|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02U", "field": "name1", "expected": wts_updates[4542]})
    checks_def.append({"type": "upgrade", "id": "R02U", "field": "tip1", "expected": wts_updates[4543]})
    checks_def.append({"type": "upgrade", "id": "R02U", "field": "ubertip1", "expected": wts_updates[4545]})

    # R02V: Тренировка ветерана (X)
    wts_updates[4561] = "|cffe4cfa3Тренировка ветерана|r"
    wts_updates[4562] = "|cffe4cfa3Тренировка ветерана|r (|cffffffffX|r)"
    wts_updates[4564] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет гвардейцам воодушевлять союзников на поле боя, повышая их защиту.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГвардеец|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02V", "field": "name1", "expected": wts_updates[4561]})
    checks_def.append({"type": "upgrade", "id": "R02V", "field": "tip1", "expected": wts_updates[4562]})
    checks_def.append({"type": "upgrade", "id": "R02V", "field": "ubertip1", "expected": wts_updates[4564]})

    # R02W: Укрепленные тяжелые доспехи (C)
    wts_updates[4571] = "|cffe4cfa3Укрепленные тяжелые доспехи|r"
    wts_updates[4572] = "|cffe4cfa3Укрепленные тяжелые доспехи|r (|cffffffffC|r)"
    wts_updates[4574] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню дополнительными защитными пластинами, снижая входящий физический урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da.|n- |cffa9c7deГвардеец|cffced4da.|n- |cffa9c7deРыцарь|cffced4da.|n- |cffa9c7deАлебардщик|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02W", "field": "name1", "expected": wts_updates[4571]})
    checks_def.append({"type": "upgrade", "id": "R02W", "field": "tip1", "expected": wts_updates[4572]})
    checks_def.append({"type": "upgrade", "id": "R02W", "field": "ubertip1", "expected": wts_updates[4574]})

    # R02X: Удлиненные стволы (3 levels) (S)
    r02x_names = [4588, 4589, 4590]
    r02x_tips = [4591, 4592, 4593]
    r02x_ubers = [4594, 4595, 4596]
    for i in range(3):
        lvl = i + 1
        wts_updates[r02x_names[i]] = "|cffe4cfa3Удлиненные стволы|r"
        wts_updates[r02x_tips[i]] = f"|cffe4cfa3Удлиненные стволы — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r02x_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает дальность стрельбы стрелков и морских волков.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da.|n- |cffa9c7deМорской волк|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R02X", "field": f"name{lvl}", "expected": wts_updates[r02x_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R02X", "field": f"tip{lvl}", "expected": wts_updates[r02x_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R02X", "field": f"ubertip{lvl}", "expected": wts_updates[r02x_ubers[i]]})

    # R02Y: Тренировка с порохом (2 levels) (R)
    r02y_names = [4599, 4600]
    r02y_tips = [4602, 4603]
    r02y_ubers = [4605, 4606]
    for i in range(2):
        lvl = i + 1
        wts_updates[r02y_names[i]] = "|cffe4cfa3Тренировка с порохом|r"
        wts_updates[r02y_tips[i]] = f"|cffe4cfa3Тренировка с порохом — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[r02y_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Ускоряет перезарядку огнестрельного оружия стрелков и морских волков.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da.|n- |cffa9c7deМорской волк|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff2|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R02Y", "field": f"name{lvl}", "expected": wts_updates[r02y_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R02Y", "field": f"tip{lvl}", "expected": wts_updates[r02y_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R02Y", "field": f"ubertip{lvl}", "expected": wts_updates[r02y_ubers[i]]})

    # R0KL: Улучшенная кладка (6 levels) (X)
    r0kl_names = [39967, 39948, 39949, 39950, 39951, 39952]
    r0kl_tips = [39968, 39953, 39954, 39955, 39956, 39957]
    r0kl_ubers = [39958, 39959, 39960, 39961, 39962, 39963]
    for i in range(6):
        lvl = i + 1
        wts_updates[r0kl_names[i]] = "|cffe4cfa3Улучшенная кладка|r"
        wts_updates[r0kl_tips[i]] = f"|cffe4cfa3Улучшенная кладка — уровень {lvl}|r (|cffffffffX|r)"
        wts_updates[r0kl_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас прочности и броню всех сооружений Кул-Тираса.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0KL", "field": f"name{lvl}", "expected": wts_updates[r0kl_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R0KL", "field": f"tip{lvl}", "expected": wts_updates[r0kl_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R0KL", "field": f"ubertip{lvl}", "expected": wts_updates[r0kl_ubers[i]]})

    # R0H4: Улучшенные топоры (6 levels) (Z)
    r0h4_names = [39939, 39940, 39931, 39932, 39933, 39934]
    r0h4_tips = [39941, 39942, 39935, 39936, 39937, 39938]
    r0h4_ubers = [None, None, 28918, 28919, 28920, 28921]
    for i in range(6):
        lvl = i + 1
        wts_updates[r0h4_names[i]] = "|cffe4cfa3Улучшенные топоры|r"
        wts_updates[r0h4_tips[i]] = f"|cffe4cfa3Улучшенные топоры — уровень {lvl}|r (|cffffffffZ|r)"
        checks_def.append({"type": "upgrade", "id": "R0H4", "field": f"name{lvl}", "expected": wts_updates[r0h4_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R0H4", "field": f"tip{lvl}", "expected": wts_updates[r0h4_tips[i]]})
        if r0h4_ubers[i]:
            wts_updates[r0h4_ubers[i]] = (
                "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём древесины, переносимой работниками за одну ходку.|n|n"
                "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|n|n"
                f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
            )
            checks_def.append({"type": "upgrade", "id": "R0H4", "field": f"ubertip{lvl}", "expected": wts_updates[r0h4_ubers[i]]})

    # R03A: Фолиант познаний магии морей (3 levels) (S)
    r03a_names = [4876, 4881, 4882]
    r03a_tips = [4877, 4883, 4884]
    r03a_ubers = [4880, 4885, 4886]
    for i in range(3):
        lvl = i + 1
        wts_updates[r03a_names[i]] = "|cffe4cfa3Фолиант познаний магии морей|r"
        wts_updates[r03a_tips[i]] = f"|cffe4cfa3Фолиант познаний магии морей — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r03a_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает жрецов штормов тайным техникам магии глубин, увеличивая их запас маны на |cffffffff50|cffced4da ед., здоровье на |cffffffff30|cffced4da ед. и скорость регенерации маны на |cffffffff0.3|cffced4da/сек.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЖрец Штормов|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R03A", "field": f"name{lvl}", "expected": wts_updates[r03a_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R03A", "field": f"tip{lvl}", "expected": wts_updates[r03a_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R03A", "field": f"ubertip{lvl}", "expected": wts_updates[r03a_ubers[i]]})

    # R03B: Обучение доктора (3 levels) (A)
    r03b_names = [4892, 4897, 4898]
    r03b_tips = [4893, 4899, 4900]
    r03b_ubers = [4896, 4901, 4902]
    for i in range(3):
        lvl = i + 1
        wts_updates[r03b_names[i]] = "|cffe4cfa3Обучение доктора|r"
        wts_updates[r03b_tips[i]] = f"|cffe4cfa3Обучение доктора — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r03b_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает медицинские навыки палубных докторов, увеличивая их запас маны на |cffffffff75|cffced4da ед. и здоровье на |cffffffff10|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПалубный Доктор|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R03B", "field": f"name{lvl}", "expected": wts_updates[r03b_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R03B", "field": f"tip{lvl}", "expected": wts_updates[r03b_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R03B", "field": f"ubertip{lvl}", "expected": wts_updates[r03b_ubers[i]]})

    # R03G: Высшее познание (2 levels) (Z)
    r03g_names = [4935, 4936]
    r03g_tips = [4937, 4938]
    r03g_ubers = [4939, 4940]
    for i in range(2):
        lvl = i + 1
        wts_updates[r03g_names[i]] = "|cffe4cfa3Высшее познание|r"
        wts_updates[r03g_tips[i]] = f"|cffe4cfa3Высшее познание — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r03g_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья и маны, а также ускоряет регенерацию маны всех заклинателей Кул-Тираса.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЖрец Штормов|cffced4da.|n- |cffa9c7deПалубный Доктор|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff2|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R03G", "field": f"name{lvl}", "expected": wts_updates[r03g_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R03G", "field": f"tip{lvl}", "expected": wts_updates[r03g_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R03G", "field": f"ubertip{lvl}", "expected": wts_updates[r03g_ubers[i]]})

    # R03H: Жертвоприношение Владыкам Моря (Z)
    wts_updates[4944] = "|cffe4cfa3Жертвоприношение Владыкам Моря|r"
    wts_updates[4946] = "|cffe4cfa3Жертвоприношение Владыкам Моря|r (|cffffffffZ|r)"
    wts_updates[34844] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Древний ритуал подношения морским духам. Дарует солдатам Кул-Тираса бонус к скорости боя |cffc8e087+10%|cffced4da, скорости перемещения |cffc8e087+10%|cffced4da и запас маны |cffc8e087+40|cffced4da ед., но снижает урон атак на |cffe69a8d-4|cffced4da ед.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03H", "field": "name1", "expected": wts_updates[4944]})
    checks_def.append({"type": "upgrade", "id": "R03H", "field": "tip1", "expected": wts_updates[4946]})
    checks_def.append({"type": "upgrade", "id": "R03H", "field": "ubertip1", "expected": wts_updates[34844]})

    # R034: Шрапнель (D)
    wts_updates[4749] = "|cffe4cfa3Шрапнель|r"
    wts_updates[4750] = "|cffe4cfa3Шрапнель|r (|cffffffffD|r)"
    checks_def.append({"type": "upgrade", "id": "R034", "field": "name1", "expected": wts_updates[4749]})
    checks_def.append({"type": "upgrade", "id": "R034", "field": "tip1", "expected": wts_updates[4750]})

    # R033: Заточка и освящение (A)
    wts_updates[4733] = "|cffe4cfa3Заточка и освящение|r"
    wts_updates[4734] = "|cffe4cfa3Заточка и освящение|r (|cffffffffA|r)"
    wts_updates[20138] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Использует древние техники заточки и благословения стали, повышая урон алебардщиков по средней броне.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАлебардщик|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R033", "field": "name1", "expected": wts_updates[4733]})
    checks_def.append({"type": "upgrade", "id": "R033", "field": "tip1", "expected": wts_updates[4734]})
    checks_def.append({"type": "upgrade", "id": "R033", "field": "ubertip1", "expected": wts_updates[20138]})

    # R032: Свинцовые пули (A)
    wts_updates[4672] = "|cffe4cfa3Свинцовые пули|r"
    wts_updates[4673] = "|cffe4cfa3Свинцовые пули|r (|cffffffffA|r)"
    wts_updates[34843] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обеспечивает стрелков и морских волков особыми тяжелыми пулями, увеличивающими урон по тяжелобронированным целям.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da.|n- |cffa9c7deМорской волк|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R032", "field": "name1", "expected": wts_updates[4672]})
    checks_def.append({"type": "upgrade", "id": "R032", "field": "tip1", "expected": wts_updates[4673]})
    checks_def.append({"type": "upgrade", "id": "R032", "field": "ubertip1", "expected": wts_updates[34843]})

    # R031: Новый сплав (3 levels) (A)
    r031_names = [4724, 4727, 4728]
    r031_tips = [4725, 4729, 4730]
    r031_ubers = [21899, 21900, 21901]
    for i in range(3):
        lvl = i + 1
        wts_updates[r031_names[i]] = "|cffe4cfa3Новый сплав|r"
        wts_updates[r031_tips[i]] = f"|cffe4cfa3Новый сплав — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r031_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает прочность и урон алебард за счёт применения передовых металлических сплавов.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАлебардщик|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R031", "field": f"name{lvl}", "expected": wts_updates[r031_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R031", "field": f"tip{lvl}", "expected": wts_updates[r031_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R031", "field": f"ubertip{lvl}", "expected": wts_updates[r031_ubers[i]]})

    # R02Z: Увеличение количества пороха (3 levels) (S)
    r02z_names = [4641, 4649, 4650]
    r02z_tips = [4642, 4651, 4652]
    r02z_ubers = [4645, 4653, 4654]
    for i in range(3):
        lvl = i + 1
        wts_updates[r02z_names[i]] = "|cffe4cfa3Увеличение количества пороха|r"
        wts_updates[r02z_tips[i]] = f"|cffe4cfa3Увеличение количества пороха — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r02z_ubers[i]] = (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает пороховой заряд патронов, повышая урон выстрелов морских волков.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМорской волк|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R02Z", "field": f"name{lvl}", "expected": wts_updates[r02z_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R02Z", "field": f"tip{lvl}", "expected": wts_updates[r02z_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R02Z", "field": f"ubertip{lvl}", "expected": wts_updates[r02z_ubers[i]]})

    # R030: Оглушающий выстрел (A)
    wts_updates[4636] = "|cffe4cfa3Оглушающий выстрел|r"
    wts_updates[4637] = "|cffe4cfa3Оглушающий выстрел|r (|cffffffffA|r)"
    wts_updates[34764] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает морских волков вести огонь на подавление, даруя способность «Оглушающий выстрел».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМорской волк|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R030", "field": "name1", "expected": wts_updates[4636]})
    checks_def.append({"type": "upgrade", "id": "R030", "field": "tip1", "expected": wts_updates[4637]})
    checks_def.append({"type": "upgrade", "id": "R030", "field": "ubertip1", "expected": wts_updates[34764]})

    # kt01: Новые типы ядер (B)
    wts_updates[42025] = "|cffe4cfa3Новые типы ядер|r"
    wts_updates[31804] = "|cffe4cfa3Новые типы ядер|r (|cffffffffB|r)"
    wts_updates[31986] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Снабжает военные корабли Кул-Тираса разрывными снарядами, увеличивающими урон в морских сражениях.|r"
    )
    checks_def.append({"type": "upgrade", "id": "kt01", "field": "name1", "expected": wts_updates[42025]})
    checks_def.append({"type": "upgrade", "id": "kt01", "field": "tip1", "expected": wts_updates[31804]})
    checks_def.append({"type": "upgrade", "id": "kt01", "field": "ubertip1", "expected": wts_updates[31986]})

    # =========================================================================
    # 6. HERO ABILITIES
    # =========================================================================
    # A0TM: Наследная Ловкость (2 levels)
    wts_updates[134] = "|cffe4cfa3Наследная Ловкость|r"
    wts_updates[135] = "|cffe4cfa3Наследная Ловкость|r"
    wts_updates[12264] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует герою шанс уклониться от вражеской атаки и шанс нанести критический удар.|n|n"
        "|cffa6afb81-й уровень:|cffced4da шанс уклонения |cffffffff15%|cffced4da, критический урон |cffffffff1.5x|cffced4da.|n"
        "|cffa6afb82-й уровень:|cffced4da шанс уклонения |cffffffff25%|cffced4da, критический урон |cffffffff2.0x|cffced4da.|r"
    )
    wts_updates[12838] = "|cffe4cfa3Наследная Ловкость — уровень 1|r"
    wts_updates[12334] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс уклониться от вражеской атаки |cffffffff15%|cffced4da и шанс нанести |cffffffff1.5|cffced4da-кратный критический урон.|r"
    wts_updates[13583] = "|cffe4cfa3Наследная Ловкость — уровень 2|r"
    wts_updates[12572] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс уклониться от вражеской атаки |cffffffff25%|cffced4da и шанс нанести |cffffffff2.0|cffced4da-кратный критический урон.|r"
    checks_def.append({"type": "ability", "id": "A0TM", "field": "name", "expected": wts_updates[134]})
    checks_def.append({"type": "ability", "id": "A0TM", "field": "tip1", "expected": wts_updates[12838]})
    checks_def.append({"type": "ability", "id": "A0TM", "field": "ubertip1", "expected": wts_updates[12334]})
    checks_def.append({"type": "ability", "id": "A0TM", "field": "tip2", "expected": wts_updates[13583]})
    checks_def.append({"type": "ability", "id": "A0TM", "field": "ubertip2", "expected": wts_updates[12572]})

    # A1MF: Ударная волна (4 levels)
    wts_updates[21583] = "|cffe4cfa3Ударная волна|r"
    wts_updates[31104] = "|cffe4cfa3Ударная волна|r"
    wts_updates[31103] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает перед собой сокрушительную волну силы, поражающую наземных врагов.|n|n"
        "|cffa6afb81-й уровень:|cffced4da урон |cffffffff75|cffced4da ед.|n"
        "|cffa6afb82-й уровень:|cffced4da урон |cffffffff130|cffced4da ед.|n"
        "|cffa6afb83-й уровень:|cffced4da урон |cffffffff200|cffced4da ед.|n"
        "|cffa6afb84-й уровень:|cffced4da урон |cffffffff280|cffced4da ед.|r"
    )
    a1mf_tips = [31095, 31096, 31097, 31098]
    a1mf_ubers = [37754, 37777, 37778, 37867]
    a1mf_dmgs = [75, 130, 200, 280]
    for i in range(4):
        lvl = i + 1
        wts_updates[a1mf_tips[i]] = f"|cffe4cfa3Ударная волна — уровень {lvl}|r"
        wts_updates[a1mf_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает в секторе перед собой волну силы, наносящую |cffffffff{a1mf_dmgs[i]}|cffced4da ед. урона врагам на своём пути.|r"
        checks_def.append({"type": "ability", "id": "A1MF", "field": f"tip{lvl}", "expected": wts_updates[a1mf_tips[i]]})
        checks_def.append({"type": "ability", "id": "A1MF", "field": f"ubertip{lvl}", "expected": wts_updates[a1mf_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A1MF", "field": "name", "expected": wts_updates[21583]})

    # A07F: Мастер Дуэлянт (4 levels)
    wts_updates[5199] = "|cffe4cfa3Мастер Дуэлянт|r"
    wts_updates[5201] = "|cffe4cfa3Мастер Дуэлянт|r"
    wts_updates[20217] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает физический урон героя в поединках против вражеских героев.|n|n"
        "|cffa6afb81-й уровень:|cffced4da бонус к урону |cffc8e087+10%|cffced4da.|n"
        "|cffa6afb82-й уровень:|cffced4da бонус к урону |cffc8e087+15%|cffced4da.|n"
        "|cffa6afb83-й уровень:|cffced4da бонус к урону |cffc8e087+20%|cffced4da.|n"
        "|cffa6afb84-й уровень:|cffced4da бонус к урону |cffc8e087+30%|cffced4da.|r"
    )
    a07f_tips = [5200, 5202, 5203, 5204]
    a07f_ubers = [4415, 4412, 4413, 20579]
    a07f_bonuses = [10, 15, 20, 30]
    for i in range(4):
        lvl = i + 1
        wts_updates[a07f_tips[i]] = f"|cffe4cfa3Мастер Дуэлянт — уровень {lvl}|r"
        wts_updates[a07f_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает физический урон по вражеским героям на |cffc8e087+{a07f_bonuses[i]}%|cffced4da.|r"
        checks_def.append({"type": "ability", "id": "A07F", "field": f"tip{lvl}", "expected": wts_updates[a07f_tips[i]]})
        checks_def.append({"type": "ability", "id": "A07F", "field": f"ubertip{lvl}", "expected": wts_updates[a07f_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A07F", "field": "name", "expected": wts_updates[5199]})

    # A07C: Родовые мечи (4 levels)
    wts_updates[5188] = "|cffe4cfa3Родовые мечи|r"
    wts_updates[5189] = "|cffe4cfa3Родовые мечи|r"
    wts_updates[21896] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Фамильные клинки дома Праудмуров, увеличивающие ловкость владельца.|n|n"
        "|cffa6afb81-й уровень:|cffced4da ловкость |cffc8e087+4|cffced4da.|n"
        "|cffa6afb82-й уровень:|cffced4da ловкость |cffc8e087+5|cffced4da.|n"
        "|cffa6afb83-й уровень:|cffced4da ловкость |cffc8e087+7|cffced4da.|n"
        "|cffa6afb84-й уровень:|cffced4da ловкость |cffc8e087+10|cffced4da.|r"
    )
    a07c_tips = [5191, 5192, 5193, 5194]
    a07c_ubers = [13156, 13157, 13158, 13159]
    a07c_vals = [4, 5, 7, 10]
    for i in range(4):
        lvl = i + 1
        wts_updates[a07c_tips[i]] = f"|cffe4cfa3Родовые мечи — уровень {lvl}|r"
        wts_updates[a07c_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает ловкость героя на |cffc8e087+{a07c_vals[i]}|cffced4da ед.|r"
        checks_def.append({"type": "ability", "id": "A07C", "field": f"tip{lvl}", "expected": wts_updates[a07c_tips[i]]})
        checks_def.append({"type": "ability", "id": "A07C", "field": f"ubertip{lvl}", "expected": wts_updates[a07c_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A07C", "field": "name", "expected": wts_updates[5188]})

    # A075: Снежная буря (4 levels)
    wts_updates[5005] = "|cffe4cfa3Снежная буря|r"
    wts_updates[5006] = "|cffe4cfa3Снежная буря|r"
    a075_tips = [5007, 5008, 5009, 5010]
    for i in range(4):
        lvl = i + 1
        wts_updates[a075_tips[i]] = f"|cffe4cfa3Снежная буря — уровень {lvl}|r"
        checks_def.append({"type": "ability", "id": "A075", "field": f"tip{lvl}", "expected": wts_updates[a075_tips[i]]})
    wts_updates[40046] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область |cffffffff13|cffced4da волн ледяных осколков, наносящих урон врагам.|r"
    checks_def.append({"type": "ability", "id": "A075", "field": "name", "expected": wts_updates[5005]})
    checks_def.append({"type": "ability", "id": "A075", "field": "ubertip4", "expected": wts_updates[40046]})

    # A076: Ледяное удушение (4 levels)
    wts_updates[5012] = "|cffe4cfa3Ледяное удушение|r"
    wts_updates[5013] = "|cffe4cfa3Ледяное удушение|r"
    wts_updates[13090] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заковывает противников в ледяные оковы, оглушая их и нанося периодический урон.|n|n"
        "|cffa6afb81-й уровень:|cffced4da урон |cffffffff75|cffced4da, оглушение |cffffffff2|cffced4da сек.|n"
        "|cffa6afb82-й уровень:|cffced4da урон |cffffffff125|cffced4da, оглушение |cffffffff3|cffced4da сек.|n"
        "|cffa6afb83-й уровень:|cffced4da урон |cffffffff175|cffced4da, оглушение |cffffffff4|cffced4da сек.|n"
        "|cffa6afb84-й уровень:|cffced4da урон |cffffffff225|cffced4da, оглушение |cffffffff4|cffced4da сек.|r"
    )
    a076_tips = [5014, 5015, 5016, 5017]
    a076_ubers = [13125, 13126, 13127, 12206]
    a076_vals = [(75, 2), (125, 3), (175, 4), (225, 4)]
    for i in range(4):
        lvl = i + 1
        dmg, stun = a076_vals[i]
        wts_updates[a076_tips[i]] = f"|cffe4cfa3Ледяное удушение — уровень {lvl}|r"
        wts_updates[a076_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заковывает врагов в ледяные оковы, нанося |cffffffff{dmg}|cffced4da ед. урона и оглушая на |cffffffff{stun}|cffced4da сек.|r"
        checks_def.append({"type": "ability", "id": "A076", "field": f"tip{lvl}", "expected": wts_updates[a076_tips[i]]})
        checks_def.append({"type": "ability", "id": "A076", "field": f"ubertip{lvl}", "expected": wts_updates[a076_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A076", "field": "name", "expected": wts_updates[5012]})

    # A078: Призыв элементаля воды (4 levels)
    wts_updates[5036] = "|cffe4cfa3Призыв элементаля воды|r"
    wts_updates[5037] = "|cffe4cfa3Призыв элементаля воды|r"
    wts_updates[8303] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь верных стихийных духов океана.|n|n"
        "|cffa6afb81-й уровень:|cffced4da |cffffffff1|cffced4da элементаль.|n"
        "|cffa6afb82-й уровень:|cffced4da |cffffffff2|cffced4da элементаля.|n"
        "|cffa6afb83-й уровень:|cffced4da |cffffffff3|cffced4da элементаля.|n"
        "|cffa6afb84-й уровень:|cffced4da |cffffffff4|cffced4da элементаля.|r"
    )
    a078_tips = [5038, 5039, 5040, 5041]
    a078_ubers = [3381, 3382, 5018, 3380]
    a078_counts = [1, 2, 3, 4]
    for i in range(4):
        lvl = i + 1
        wts_updates[a078_tips[i]] = f"|cffe4cfa3Призыв элементаля воды — уровень {lvl}|r"
        cnt = a078_counts[i]
        suff = "элементаля" if cnt in (2, 3, 4) else "элементалей" if cnt > 4 else "элементаля"
        wts_updates[a078_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff{cnt}|cffced4da водного духа океана на помощь жрице.|r"
        checks_def.append({"type": "ability", "id": "A078", "field": f"tip{lvl}", "expected": wts_updates[a078_tips[i]]})
        checks_def.append({"type": "ability", "id": "A078", "field": f"ubertip{lvl}", "expected": wts_updates[a078_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A078", "field": "name", "expected": wts_updates[5036]})

    # A077: Абсолютная Защита (2 levels)
    wts_updates[5026] = "|cffe4cfa3Абсолютная Защита|r"
    wts_updates[5031] = "|cffe4cfa3Абсолютная Защита|r"
    wts_updates[3109] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da На время наделяет находящихся рядом союзников колоссальной броней, делая их практически неуязвимыми к физическим атакам.|r"
    wts_updates[5027] = "|cffe4cfa3Абсолютная Защита — уровень 1|r"
    wts_updates[20577] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников вокруг на |cffc8e087+99999%|cffced4da на короткое время.|r"
    wts_updates[5029] = "|cffe4cfa3Абсолютная Защита — уровень 2|r"
    wts_updates[20578] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников вокруг на |cffc8e087+99999%|cffced4da на увеличенное время.|r"
    checks_def.append({"type": "ability", "id": "A077", "field": "name", "expected": wts_updates[5026]})
    checks_def.append({"type": "ability", "id": "A077", "field": "tip1", "expected": wts_updates[5027]})
    checks_def.append({"type": "ability", "id": "A077", "field": "ubertip1", "expected": wts_updates[20577]})
    checks_def.append({"type": "ability", "id": "A077", "field": "tip2", "expected": wts_updates[5029]})
    checks_def.append({"type": "ability", "id": "A077", "field": "ubertip2", "expected": wts_updates[20578]})

    # A07B: Массовое исцеление (2 levels)
    wts_updates[5180] = "|cffe4cfa3Массовое исцеление|r"
    wts_updates[5178] = "|cffe4cfa3Массовое исцеление|r"
    wts_updates[4410] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье всем союзным войскам вокруг адмирала.|n|n"
        "|cffa6afb81-й уровень:|cffced4da исцеляет |cffc8e087250|cffced4da ед. здоровья.|n"
        "|cffa6afb82-й уровень:|cffced4da исцеляет |cffc8e087350|cffced4da ед. здоровья.|r"
    )
    wts_updates[5174] = "|cffe4cfa3Массовое исцеление — уровень 1|r"
    wts_updates[3111] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087250|cffced4da ед. здоровья всем союзникам поблизости.|r"
    wts_updates[5176] = "|cffe4cfa3Массовое исцеление — уровень 2|r"
    wts_updates[4409] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087350|cffced4da ед. здоровья всем союзникам поблизости.|r"
    checks_def.append({"type": "ability", "id": "A07B", "field": "name", "expected": wts_updates[5180]})
    checks_def.append({"type": "ability", "id": "A07B", "field": "tip1", "expected": wts_updates[5174]})
    checks_def.append({"type": "ability", "id": "A07B", "field": "ubertip1", "expected": wts_updates[3111]})
    checks_def.append({"type": "ability", "id": "A07B", "field": "tip2", "expected": wts_updates[5176]})
    checks_def.append({"type": "ability", "id": "A07B", "field": "ubertip2", "expected": wts_updates[4409]})

    # A07A: Опытность (4 levels)
    wts_updates[5167] = "|cffe4cfa3Опытность|r"
    wts_updates[5168] = "|cffe4cfa3Опытность|r"
    wts_updates[13154] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура командующего, увеличивающая скорость перемещения и регенерацию здоровья союзников.|n|n"
        "|cffa6afb81-й уровень:|cffced4da скорость |cffc8e087+10%|cffced4da, регенерация |cffc8e087+0.5|cffced4da/сек.|n"
        "|cffa6afb82-й уровень:|cffced4da скорость |cffc8e087+20%|cffced4da, регенерация |cffc8e087+1.0|cffced4da/сек.|n"
        "|cffa6afb83-й уровень:|cffced4da скорость |cffc8e087+30%|cffced4da, регенерация |cffc8e087+1.5|cffced4da/сек.|n"
        "|cffa6afb84-й уровень:|cffced4da скорость |cffc8e087+40%|cffced4da, регенерация |cffc8e087+2.0|cffced4da/сек.|r"
    )
    a07a_tips = [5169, 5170, 5171, 5172]
    a07a_ubers = [13151, 13152, 13153, 13150]
    a07a_vals = [(10, "0.5"), (20, "1.0"), (30, "1.5"), (40, "2.0")]
    for i in range(4):
        lvl = i + 1
        spd, reg = a07a_vals[i]
        wts_updates[a07a_tips[i]] = f"|cffe4cfa3Опытность — уровень {lvl}|r"
        wts_updates[a07a_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения союзников на |cffc8e087+{spd}%|cffced4da и регенерацию здоровья на |cffc8e087+{reg}|cffced4da ед./сек.|r"
        checks_def.append({"type": "ability", "id": "A07A", "field": f"tip{lvl}", "expected": wts_updates[a07a_tips[i]]})
        checks_def.append({"type": "ability", "id": "A07A", "field": f"ubertip{lvl}", "expected": wts_updates[a07a_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A07A", "field": "name", "expected": wts_updates[5167]})

    # A079: Критический Выстрел (4 levels)
    wts_updates[5160] = "|cffe4cfa3Критический Выстрел|r"
    wts_updates[5161] = "|cffe4cfa3Критический Выстрел|r"
    wts_updates[13149] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс нанести многократный урон при атаке.|n|n"
        "|cffa6afb81-й уровень:|cffced4da шанс |cffffffff15%|cffced4da, урон |cffffffff2x|cffced4da.|n"
        "|cffa6afb82-й уровень:|cffced4da шанс |cffffffff15%|cffced4da, урон |cffffffff3x|cffced4da.|n"
        "|cffa6afb83-й уровень:|cffced4da шанс |cffffffff15%|cffced4da, урон |cffffffff4x|cffced4da.|n"
        "|cffa6afb84-й уровень:|cffced4da шанс |cffffffff15%|cffced4da, урон |cffffffff5x|cffced4da.|r"
    )
    a079_tips = [5162, 5163, 5164, 5165]
    a079_ubers = [20857, 30447, 30448, 9223]
    a079_mults = [2, 3, 4, 5]
    for i in range(4):
        lvl = i + 1
        wts_updates[a079_tips[i]] = f"|cffe4cfa3Критический Выстрел — уровень {lvl}|r"
        wts_updates[a079_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff15%|cffced4da шанс нанести |cffffffff{a079_mults[i]}|cffced4da-кратный урон при атаке.|r"
        checks_def.append({"type": "ability", "id": "A079", "field": f"tip{lvl}", "expected": wts_updates[a079_tips[i]]})
        checks_def.append({"type": "ability", "id": "A079", "field": f"ubertip{lvl}", "expected": wts_updates[a079_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A079", "field": "name", "expected": wts_updates[5160]})

    # A05I: Меткий Выстрел (4 levels)
    wts_updates[5149] = "|cffe4cfa3Меткий Выстрел|r"
    wts_updates[5150] = "|cffe4cfa3Меткий Выстрел|r"
    wts_updates[13143] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прицельный мощный выстрел, наносящий высокий урон и оглушающий цель.|n|n"
        "|cffa6afb81-й уровень:|cffced4da урон |cffffffff150|cffced4da ед., оглушение героев |cffffffff0.5|cffced4da сек. (воинов |cffffffff5|cffced4da сек.).|n"
        "|cffa6afb82-й уровень:|cffced4da урон |cffffffff225|cffced4da ед., оглушение героев |cffffffff0.6|cffced4da сек. (воинов |cffffffff5|cffced4da сек.).|n"
        "|cffa6afb83-й уровень:|cffced4da урон |cffffffff350|cffced4da ед., оглушение героев |cffffffff0.7|cffced4da сек. (воинов |cffffffff5|cffced4da сек.).|n"
        "|cffa6afb84-й уровень:|cffced4da урон |cffffffff400|cffced4da ед., оглушение героев |cffffffff0.8|cffced4da сек. (воинов |cffffffff5|cffced4da сек.).|r"
    )
    a05i_tips = [5152, 5153, 5154, 5155]
    a05i_ubers = [13144, 13145, 13146, 13147]
    a05i_vals = [(150, "0.5"), (225, "0.6"), (350, "0.7"), (400, "0.8")]
    for i in range(4):
        lvl = i + 1
        dmg, stun = a05i_vals[i]
        wts_updates[a05i_tips[i]] = f"|cffe4cfa3Меткий Выстрел — уровень {lvl}|r"
        wts_updates[a05i_ubers[i]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели |cffffffff{dmg}|cffced4da ед. урона и оглушает героев на |cffffffff{stun}|cffced4da сек., обычных воинов на |cffffffff5|cffced4da сек.|r"
        checks_def.append({"type": "ability", "id": "A05I", "field": f"tip{lvl}", "expected": wts_updates[a05i_tips[i]]})
        checks_def.append({"type": "ability", "id": "A05I", "field": f"ubertip{lvl}", "expected": wts_updates[a05i_ubers[i]]})
    checks_def.append({"type": "ability", "id": "A05I", "field": "name", "expected": wts_updates[5149]})

    # =========================================================================
    # 7. UNIT ABILITIES
    # =========================================================================
    # A06K: Укрыться за щитом
    wts_updates[4501] = "|cffe4cfa3Укрыться за щитом|r"
    wts_updates[4502] = "|cffe4cfa3Укрыться за щитом|r"
    checks_def.append({"type": "ability", "id": "A06K", "field": "name", "expected": wts_updates[4501]})
    checks_def.append({"type": "ability", "id": "A06K", "field": "tip1", "expected": wts_updates[4502]})

    # A06L: Мастерство
    wts_updates[4504] = "|cffe4cfa3Мастерство|r"
    wts_updates[4505] = "|cffe4cfa3Мастерство|r"
    wts_updates[25342] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff15%|cffced4da шанс нанести |cffffffff1.8|cffced4da-кратный критический урон при атаке.|r"
    checks_def.append({"type": "ability", "id": "A06L", "field": "name", "expected": wts_updates[4504]})
    checks_def.append({"type": "ability", "id": "A06L", "field": "tip1", "expected": wts_updates[4505]})
    checks_def.append({"type": "ability", "id": "A06L", "field": "ubertip1", "expected": wts_updates[25342]})

    # A06N: Укрепленные тяжелые доспехи
    wts_updates[4558] = "|cffe4cfa3Укрепленные тяжелые доспехи|r"
    wts_updates[4559] = "|cffe4cfa3Укрепленные тяжелые доспехи|r"
    wts_updates[7957] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает входящий физический урон от вражеских атак.|r"
    checks_def.append({"type": "ability", "id": "A06N", "field": "name", "expected": wts_updates[4558]})
    checks_def.append({"type": "ability", "id": "A06N", "field": "tip1", "expected": wts_updates[4559]})
    checks_def.append({"type": "ability", "id": "A06N", "field": "ubertip1", "expected": wts_updates[7957]})

    # A06R: Свинцовые Пули
    wts_updates[4655] = "|cffe4cfa3Свинцовые пули|r"
    wts_updates[4656] = "|cffe4cfa3Свинцовые пули|r"
    wts_updates[4657] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон выстрелов по целям с тяжелой бронёй.|r"
    checks_def.append({"type": "ability", "id": "A06R", "field": "name", "expected": wts_updates[4655]})
    checks_def.append({"type": "ability", "id": "A06R", "field": "tip1", "expected": wts_updates[4656]})
    checks_def.append({"type": "ability", "id": "A06R", "field": "ubertip1", "expected": wts_updates[4657]})

    # A06Q: Оглушающий выстрел
    wts_updates[4634] = "|cffe4cfa3Оглушающий выстрел|r"
    wts_updates[4635] = "|cffe4cfa3Оглушающий выстрел|r"
    wts_updates[20135] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки с вероятностью наносят дополнительный урон и оглушают цель на |cffffffff1|cffced4da сек. (героев на |cffffffff0.2|cffced4da сек.).|r"
    checks_def.append({"type": "ability", "id": "A06Q", "field": "name", "expected": wts_updates[4634]})
    checks_def.append({"type": "ability", "id": "A06Q", "field": "tip1", "expected": wts_updates[4635]})
    checks_def.append({"type": "ability", "id": "A06Q", "field": "ubertip1", "expected": wts_updates[20135]})

    # A06V: Морская прохлада
    wts_updates[4697] = "|cffe4cfa3Морская прохлада|r"
    wts_updates[4698] = "|cffe4cfa3Морская прохлада|r"
    wts_updates[13101] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет поражённых врагов и добавляет |cffc8e087+5|cffced4da ед. к урону атак жреца штормов.|r"
    checks_def.append({"type": "ability", "id": "A06V", "field": "name", "expected": wts_updates[4697]})
    checks_def.append({"type": "ability", "id": "A06V", "field": "tip1", "expected": wts_updates[4698]})
    checks_def.append({"type": "ability", "id": "A06V", "field": "ubertip1", "expected": wts_updates[13101]})

    # A06T: Призыв Духа Моря
    wts_updates[4683] = "|cffe4cfa3Призыв Духа Моря|r"
    wts_updates[4684] = "|cffe4cfa3Призыв Духа Моря|r"
    wts_updates[13100] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь жрецу могучего духа океана.|r"
    checks_def.append({"type": "ability", "id": "A06T", "field": "name", "expected": wts_updates[4683]})
    checks_def.append({"type": "ability", "id": "A06T", "field": "tip1", "expected": wts_updates[4684]})
    checks_def.append({"type": "ability", "id": "A06T", "field": "ubertip1", "expected": wts_updates[13100]})

    # A06U: Сокрушительная волна
    wts_updates[4690] = "|cffe4cfa3Сокрушительная волна|r"
    wts_updates[4691] = "|cffe4cfa3Сокрушительная волна|r"
    wts_updates[5689] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну воды, наносящую по |cffffffff75|cffced4da ед. урона наземным врагам на прямой линии (максимум |cffffffff500|cffced4da ед. урона).|r"
    checks_def.append({"type": "ability", "id": "A06U", "field": "name", "expected": wts_updates[4690]})
    checks_def.append({"type": "ability", "id": "A06U", "field": "tip1", "expected": wts_updates[4691]})
    checks_def.append({"type": "ability", "id": "A06U", "field": "ubertip1", "expected": wts_updates[5689]})

    # A06X: Массовое восполнение маны
    wts_updates[4705] = "|cffe4cfa3Массовое восполнение маны|r"
    wts_updates[4706] = "|cffe4cfa3Массовое восполнение маны|r"
    wts_updates[15188] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e08750|cffced4da ед. маны союзным войскам в радиусе |cffffffff300|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "A06X", "field": "name", "expected": wts_updates[4705]})
    checks_def.append({"type": "ability", "id": "A06X", "field": "tip1", "expected": wts_updates[4706]})
    checks_def.append({"type": "ability", "id": "A06X", "field": "ubertip1", "expected": wts_updates[15188]})

    # A06W: Массовое исцеление
    wts_updates[4701] = "|cffe4cfa3Массовое исцеление|r"
    wts_updates[4703] = "|cffe4cfa3Массовое исцеление|r"
    wts_updates[13102] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e08775|cffced4da ед. здоровья союзникам в радиусе |cffffffff300|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "A06W", "field": "name", "expected": wts_updates[4701]})
    checks_def.append({"type": "ability", "id": "A06W", "field": "tip1", "expected": wts_updates[4703]})
    checks_def.append({"type": "ability", "id": "A06W", "field": "ubertip1", "expected": wts_updates[13102]})

    # A06Z: Рассеивание заклинаний
    wts_updates[4717] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[4718] = "|cffe4cfa3Рассеивание заклинаний|r"
    checks_def.append({"type": "ability", "id": "A06Z", "field": "name", "expected": wts_updates[4717]})
    checks_def.append({"type": "ability", "id": "A06Z", "field": "tip1", "expected": wts_updates[4718]})

    # A06Y: Массовый бонус к броне
    wts_updates[4714] = "|cffe4cfa3Массовый бонус к броне|r"
    wts_updates[4715] = "|cffe4cfa3Массовый бонус к броне|r"
    wts_updates[13104] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников в радиусе |cffffffff300|cffced4da ед. на |cffc8e087+2|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "A06Y", "field": "name", "expected": wts_updates[4714]})
    checks_def.append({"type": "ability", "id": "A06Y", "field": "tip1", "expected": wts_updates[4715]})
    checks_def.append({"type": "ability", "id": "A06Y", "field": "ubertip1", "expected": wts_updates[13104]})

    # A070: Заточка и освящение
    wts_updates[4720] = "|cffe4cfa3Заточка и освящение|r"
    wts_updates[4721] = "|cffe4cfa3Заточка и освящение|r"
    checks_def.append({"type": "ability", "id": "A070", "field": "name", "expected": wts_updates[4720]})
    checks_def.append({"type": "ability", "id": "A070", "field": "tip1", "expected": wts_updates[4721]})

    # A071: Шрапнель
    wts_updates[4747] = "|cffe4cfa3Шрапнель|r"
    wts_updates[4748] = "|cffe4cfa3Шрапнель|r"
    checks_def.append({"type": "ability", "id": "A071", "field": "name", "expected": wts_updates[4747]})
    checks_def.append({"type": "ability", "id": "A071", "field": "tip1", "expected": wts_updates[4748]})

    # Categories list for registries
    categories = {
        "buildings": [
            "h01X", "h01Y", "h01Z", "h020", "h021", "h0G6",
            "h022", "h023", "h024", "h025", "h026", "h027", "kt02"
        ],
        "heroes": ["H01L", "H01N", "H01K"],
        "units": [
            "h013", "h019", "h01A", "h01C", "h01D", "h01E", "h01F", "h01G", "h01H", "h01I", "kt00",
            "h0NC", "h0ND", "h0NE", "h0NF", "h0NG", "h0NH", "h0NI", "h0NJ", "h0NS",
            "h0NL", "h0NM", "h0NN", "h0NO", "h0NP", "h0NQ", "h0NR", "h0NK", "h0NT", "h0NU", "h0NV"
        ],
        "upgrades": [
            "R07D", "R0HX", "R027", "R02S", "R036", "R037", "R038", "R039", "R035",
            "R02T", "R01U", "R02U", "R02V", "R02W", "R02X", "R02Y", "R0KL", "R0H4",
            "R03A", "R03B", "R03G", "R03H", "R034", "R033", "R032", "R031", "R02Z", "R030", "kt01"
        ],
        "abilities": [
            "A0HO",
            "A0TM", "A1MF", "A07F", "A07C",
            "A075", "A076", "A078", "A077",
            "A07B", "A07A", "A079", "A05I",
            "A06K", "A06L", "A06N", "A06R", "A06Q", "A06V", "A06T", "A06U",
            "A06X", "A06W", "A06Z", "A06Y", "A070", "A071"
        ]
    }

    plan_data = {
        "race": "KulTiras",
        "race_id": 17,
        "categories": categories,
        "wts_updates": wts_updates,
        "checks_def": checks_def
    }

    out_file = folder / "kultiras_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {out_file} with {len(wts_updates)} WTS updates and {len(checks_def)} checks.")

if __name__ == "__main__":
    main()
