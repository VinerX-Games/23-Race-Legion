# -*- coding: utf-8 -*-
"""Generate exact wts_updates and checks_def for Gilneas / Worgens using real object WTS IDs."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def build_plan():
    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. SELECTION: A121, R0FX
    # =========================================================================
    wts_updates[38899] = "|cffe4cfa3Гилнеас|r"
    wts_updates[38900] = "|cffe4cfa3Гилнеас|r (|cffffffffA|r)"
    wts_updates[26678] = (
        "|cffa6afb8РАСА:|cffced4da Королевство людей, поражённое проклятием воргенов, сочетающее дисциплину армии и свирепую мощь диких зверей.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deNiCAmCHiK|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●|cffa6afb8○○○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Cataclysm — Battle for Azeroth»|r|n|n"
        "|cffced4daГилнеас был одним из самых могущественных человеческих королевств. Его правитель, Генн Седогрив, долгое время держал народ в изоляции за великой стеной. "
        "Однако древнее проклятие воргенов проникло в королевство, подвергнув жителей необратимой трансформации. Научившись контролировать звериную сущность, "
        "воины Гилнеаса обрушивают на врагов сокрушительные когти, ярость волчьей крови и смертоносную меткость стрелков.|r"
    )
    checks_def.append({"type": "ability", "id": "A121", "field": "name", "expected": wts_updates[38899]})
    checks_def.append({"type": "ability", "id": "A121", "field": "tip1", "expected": wts_updates[38900]})
    checks_def.append({"type": "ability", "id": "A121", "field": "ubertip1", "expected": wts_updates[26678]})

    # Marker: R0FX
    wts_updates[8429] = "|cffe4cfa3Гилнеас|r"
    wts_updates[25159] = "|cffe4cfa3Гилнеас|r"
    wts_updates[5600] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к королевству Гилнеас.|r"
    checks_def.append({"type": "upgrade", "id": "R0FX", "field": "name1", "expected": wts_updates[8429]})
    checks_def.append({"type": "upgrade", "id": "R0FX", "field": "tip1", "expected": wts_updates[25159]})
    checks_def.append({"type": "upgrade", "id": "R0FX", "field": "ubertip1", "expected": wts_updates[5600]})

    # =========================================================================
    # 2. BUILDINGS (11 buildings)
    # =========================================================================
    # h0IJ: Ратуша (Q)
    wts_updates[22563] = "|cffe4cfa3Ратуша|r"
    wts_updates[22564] = "|cffe4cfa3Ратуша|r (|cffffffffQ|r)"
    wts_updates[10184] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Гилнеаса первой ступени. Обеспечивает запас пищи и добычу ресурсов.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПостройщик|cffced4da: рабочий строитель и добытчик ресурсов.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deФорт|cffced4da: открывает доступ к передовым сооружениям и технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IJ", "field": "name", "expected": wts_updates[22563]})
    checks_def.append({"type": "unit", "id": "h0IJ", "field": "tip", "expected": wts_updates[22564]})
    checks_def.append({"type": "unit", "id": "h0IJ", "field": "ubertip", "expected": wts_updates[10184]})

    # h0IK: Форт (Z)
    wts_updates[22567] = "|cffe4cfa3Форт|r"
    wts_updates[22568] = "|cffe4cfa3Форт|r (|cffffffffZ|r)"
    wts_updates[27622] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Гилнеаса второй ступени. Существенно увеличивает запас пищи.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПостройщик|cffced4da: рабочий строитель и добытчик ресурсов.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЗамок|cffced4da: открывает доступ к высшим технологиям королевства.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IK", "field": "name", "expected": wts_updates[22567]})
    checks_def.append({"type": "unit", "id": "h0IK", "field": "tip", "expected": wts_updates[22568]})
    checks_def.append({"type": "unit", "id": "h0IK", "field": "ubertip", "expected": wts_updates[27622]})

    # h0IL: Замок (Z)
    wts_updates[22573] = "|cffe4cfa3Замок|r"
    wts_updates[22574] = "|cffe4cfa3Замок|r (|cffffffffZ|r)"
    wts_updates[27623] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Гилнеаса третьей ступени. Обеспечивает максимальный запас пищи.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПостройщик|cffced4da: рабочий строитель и добытчик ресурсов.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IL", "field": "name", "expected": wts_updates[22573]})
    checks_def.append({"type": "unit", "id": "h0IL", "field": "tip", "expected": wts_updates[22574]})
    checks_def.append({"type": "unit", "id": "h0IL", "field": "ubertip", "expected": wts_updates[27623]})

    # h0IM: Ферма (A)
    wts_updates[22580] = "|cffe4cfa3Ферма|r"
    wts_updates[22581] = "|cffe4cfa3Ферма|r (|cffffffffA|r)"
    wts_updates[31862] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию королевства продовольствием.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IM", "field": "name", "expected": wts_updates[22580]})
    checks_def.append({"type": "unit", "id": "h0IM", "field": "tip", "expected": wts_updates[22581]})
    checks_def.append({"type": "unit", "id": "h0IM", "field": "ubertip", "expected": wts_updates[31862]})

    # h0IN: Алтарь предков (S)
    wts_updates[22583] = "|cffe4cfa3Алтарь предков|r"
    wts_updates[22585] = "|cffe4cfa3Алтарь предков|r (|cffffffffS|r)"
    wts_updates[27624] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Позволяет призывать и воскрешать павших героев Гилнеаса.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deВерховный охотник|cffced4da: мастер охоты ближнего боя.|n"
        "- |cffa9c7deЛорд друид|cffced4da: повелитель природных стихий и ауры маны.|n"
        "- |cffa9c7deГенерал Гилнеаса|cffced4da: вдохновляющий полководец с аурой урона.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IN", "field": "name", "expected": wts_updates[22583]})
    checks_def.append({"type": "unit", "id": "h0IN", "field": "tip", "expected": wts_updates[22585]})
    checks_def.append({"type": "unit", "id": "h0IN", "field": "ubertip", "expected": wts_updates[27624]})

    # h0IO: Казармы (W)
    wts_updates[22587] = "|cffe4cfa3Казармы|r"
    wts_updates[22588] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[22454] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает базовые боевые силы и осадную технику.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПехотинец|cffced4da: универсальный боец ближнего боя со щитом.|n"
        "- |cffa9c7deСтрелок|cffced4da: меткий стрелок дальнего боя с мушкетом.|n"
        "- |cffa9c7deКатапульта|cffced4da: дальнобойное осадное орудие.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deДлинноствольные мушкеты|cffced4da|n"
        "- |cffa9c7deЗащита|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IO", "field": "name", "expected": wts_updates[22587]})
    checks_def.append({"type": "unit", "id": "h0IO", "field": "tip", "expected": wts_updates[22588]})
    checks_def.append({"type": "unit", "id": "h0IO", "field": "ubertip", "expected": wts_updates[22454]})

    # h0IP: Лесопилка (E)
    wts_updates[22609] = "|cffe4cfa3Лесопилка|r"
    wts_updates[22610] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[28244] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит складом древесины и центром улучшения инструментов лесозаготовок.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенные инструменты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IP", "field": "name", "expected": wts_updates[22609]})
    checks_def.append({"type": "unit", "id": "h0IP", "field": "tip", "expected": wts_updates[22610]})
    checks_def.append({"type": "unit", "id": "h0IP", "field": "ubertip", "expected": wts_updates[28244]})

    # h0IQ: Кузница (R)
    wts_updates[22613] = "|cffe4cfa3Кузница|r"
    wts_updates[22615] = "|cffe4cfa3Кузница|r (|cffffffffR|r)"
    wts_updates[28243] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр усовершенствования вооружения, доспехов и звериных способностей воргенов.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОружие ближнего боя|cffced4da|n"
        "- |cffa9c7deКованая броня|cffced4da|n"
        "- |cffa9c7deОружие дальнего боя|cffced4da|n"
        "- |cffa9c7deКожаная броня|cffced4da|n"
        "- |cffa9c7deНутро зверя|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IQ", "field": "name", "expected": wts_updates[22613]})
    checks_def.append({"type": "unit", "id": "h0IQ", "field": "tip", "expected": wts_updates[22615]})
    checks_def.append({"type": "unit", "id": "h0IQ", "field": "ubertip", "expected": wts_updates[28243]})

    # h0IR: Военная академия (D)
    wts_updates[22619] = "|cffe4cfa3Военная академия|r"
    wts_updates[22639] = "|cffe4cfa3Военная академия|r (|cffffffffD|r)"
    wts_updates[22433] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает специализированных бойцов и боевых магов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТопорометатель|cffced4da: стрелок поддержки с оглушающим броском.|n"
        "- |cffa9c7deРыцарь|cffced4da: тяжёлый всадник ближнего боя.|n"
        "- |cffa9c7deВорген маг|cffced4da: боевой заклинатель с рассеиванием и тёмной стаей.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deДрессировка Топорометателей|cffced4da|n"
        "- |cffa9c7deВолчья кровь|cffced4da|n"
        "- |cffa9c7deДрессировка|cffced4da|n"
        "- |cffa9c7deПознания магии|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IR", "field": "name", "expected": wts_updates[22619]})
    checks_def.append({"type": "unit", "id": "h0IR", "field": "tip", "expected": wts_updates[22639]})
    checks_def.append({"type": "unit", "id": "h0IR", "field": "ubertip", "expected": wts_updates[22433]})

    # h0IS: Храм друидов (F)
    wts_updates[22668] = "|cffe4cfa3Храм друидов|r"
    wts_updates[22669] = "|cffe4cfa3Храм друидов|r (|cffffffffF|r)"
    wts_updates[22435] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Место единения с природой и культивации первобытной силы воргенов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da: свирепый штурмовик ближнего боя.|n"
        "- |cffa9c7deВорген друид|cffced4da: целитель и заклинатель поддержки с боевым воем.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗвериные рефлексы|cffced4da|n"
        "- |cffa9c7deВолчьи конечности|cffced4da|n"
        "- |cffa9c7deСлияние с природой|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IS", "field": "name", "expected": wts_updates[22668]})
    checks_def.append({"type": "unit", "id": "h0IS", "field": "tip", "expected": wts_updates[22669]})
    checks_def.append({"type": "unit", "id": "h0IS", "field": "ubertip", "expected": wts_updates[22435]})

    # h0JT: Сторожевая Башня (Z)
    wts_updates[25420] = "|cffe4cfa3Сторожевая башня|r"
    wts_updates[25674] = "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)"
    wts_updates[20491] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение. Обнаруживает невидимых врагов.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JT", "field": "name", "expected": wts_updates[25420]})
    checks_def.append({"type": "unit", "id": "h0JT", "field": "tip", "expected": wts_updates[25674]})
    checks_def.append({"type": "unit", "id": "h0JT", "field": "ubertip", "expected": wts_updates[20491]})

    # =========================================================================
    # 3. WORKER: h0IT (Q)
    # =========================================================================
    wts_updates[22673] = "|cffe4cfa3Постройщик|r"
    wts_updates[22680] = "|cffe4cfa3Постройщик|r (|cffffffffQ|r)"
    wts_updates[22674] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Гилнеаса. Добывает золото и древесину, возводит и ремонтирует здания.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткую дистанцию.|n"
        "- |cffa9c7deСбор ресурсов|cffced4da: добывает золото в рудниках и рубит деревья.|n"
        "- |cffa9c7deРемонт|cffced4da: восстанавливает прочность зданий.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IT", "field": "name", "expected": wts_updates[22673]})
    checks_def.append({"type": "unit", "id": "h0IT", "field": "tip", "expected": wts_updates[22680]})
    checks_def.append({"type": "unit", "id": "h0IT", "field": "ubertip", "expected": wts_updates[22674]})

    # =========================================================================
    # 4. UNITS (10 units)
    # =========================================================================
    # h0IU: Пехотинец (волк) (Q)
    wts_updates[22832] = "|cffe4cfa3Пехотинец|r"
    wts_updates[22436] = "|cffe4cfa3Пехотинец|r (|cffffffffQ|r)"
    wts_updates[27684] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец ближнего боя в форме волка.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗащита|cffced4da: уменьшает получаемый урон от стрелков и отражает пронзающие атаки.|n"
        "- |cffa9c7deНутро зверя|cffced4da: пробивает среднюю и тяжёлую броню цели.|n"
        "- |cffa9c7deКровотечение|cffced4da: периодический урон после атаки.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IU", "field": "name", "expected": wts_updates[22832]})
    checks_def.append({"type": "unit", "id": "h0IU", "field": "tip", "expected": wts_updates[22436]})
    checks_def.append({"type": "unit", "id": "h0IU", "field": "ubertip", "expected": wts_updates[27684]})

    # h0IV: Стрелок (W)
    wts_updates[22836] = "|cffe4cfa3Стрелок|r"
    wts_updates[9361] = "|cffe4cfa3Стрелок|r (|cffffffffW|r)"
    wts_updates[27690] = (
        "|cffa6afb8ЮНИТ:|cffced4da Меткий стрелок дальнего боя, вооружённый длинноствольным мушкетом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДлинноствольные мушкеты|cffced4da: увеличивает дальность стрельбы.|n"
        "- |cffa9c7deНутро зверя|cffced4da: пробивает броню цели.|n"
        "- |cffa9c7deКровотечение|cffced4da: периодический урон после атаки.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IV", "field": "name", "expected": wts_updates[22836]})
    checks_def.append({"type": "unit", "id": "h0IV", "field": "tip", "expected": wts_updates[9361]})
    checks_def.append({"type": "unit", "id": "h0IV", "field": "ubertip", "expected": wts_updates[27690]})

    # h0IW: Рыцарь (W)
    wts_updates[22478] = "|cffe4cfa3Рыцарь|r"
    wts_updates[22600] = "|cffe4cfa3Рыцарь|r (|cffffffffW|r)"
    wts_updates[31278] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый бронированный кавалерист Гилнеаса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНутро зверя|cffced4da: пробивает среднюю и тяжёлую броню цели.|n"
        "- |cffa9c7deКровотечение|cffced4da: периодический урон после атаки.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IW", "field": "name", "expected": wts_updates[22478]})
    checks_def.append({"type": "unit", "id": "h0IW", "field": "tip", "expected": wts_updates[22600]})
    checks_def.append({"type": "unit", "id": "h0IW", "field": "ubertip", "expected": wts_updates[31278]})

    # h0IX: Ворген друид (Q)
    wts_updates[22857] = "|cffe4cfa3Ворген друид|r"
    wts_updates[22858] = "|cffe4cfa3Ворген друид|r (|cffffffffQ|r)"
    wts_updates[31470] = (
        "|cffa6afb8ЮНИТ:|cffced4da Целитель и маг поддержки, черпающий силы из дикой природы.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЭссенция здоровья|cffced4da: восстанавливает здоровье союзникам рядом.|n"
        "- |cffa9c7deВой|cffced4da: повышает урон союзных войск на |cffffffff25%|cffced4da.|n"
        "- |cffa9c7deНутро зверя|cffced4da: пробивает броню цели.|n"
        "- |cffa9c7deКровотечение|cffced4da: периодический урон после атаки.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IX", "field": "name", "expected": wts_updates[22857]})
    checks_def.append({"type": "unit", "id": "h0IX", "field": "tip", "expected": wts_updates[22858]})
    checks_def.append({"type": "unit", "id": "h0IX", "field": "ubertip", "expected": wts_updates[31470]})

    # h0IY: Пехотинец (человек) (Q)
    wts_updates[22865] = "|cffe4cfa3Пехотинец (человек)|r"
    wts_updates[22833] = "|cffe4cfa3Пехотинец (человек)|r (|cffffffffQ|r)"
    wts_updates[31608] = (
        "|cffa6afb8ЮНИТ:|cffced4da Человеческий пехотинец Гилнеаса со щитом и мечом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗащита|cffced4da: уменьшает получаемый урон от стрелков и отражает пронзающие атаки.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IY", "field": "name", "expected": wts_updates[22865]})
    checks_def.append({"type": "unit", "id": "h0IY", "field": "tip", "expected": wts_updates[22833]})
    checks_def.append({"type": "unit", "id": "h0IY", "field": "ubertip", "expected": wts_updates[31608]})

    # h0IZ: Рыцарь (человек) (W)
    wts_updates[22853] = "|cffe4cfa3Рыцарь (человек)|r"
    wts_updates[22854] = "|cffe4cfa3Рыцарь (человек)|r (|cffffffffW|r)"
    wts_updates[31610] = (
        "|cffa6afb8ЮНИТ:|cffced4da Человеческий кавалерист в тяжёлых доспехах.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМастерство|cffced4da: шанс нанести критический урон.|n"
        "- |cffa9c7deУкрепленные тяжелые доспехи|cffced4da: снижает получаемый физический урон.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0IZ", "field": "name", "expected": wts_updates[22853]})
    checks_def.append({"type": "unit", "id": "h0IZ", "field": "tip", "expected": wts_updates[22854]})
    checks_def.append({"type": "unit", "id": "h0IZ", "field": "ubertip", "expected": wts_updates[31610]})

    # h0J0: Ворген маг (Q)
    wts_updates[22495] = "|cffe4cfa3Ворген маг|r"
    wts_updates[22497] = "|cffe4cfa3Ворген маг|r (|cffffffffQ|r)"
    wts_updates[31674] = (
        "|cffa6afb8ЮНИТ:|cffced4da Боевой заклинатель, использующий тёмную магию и первобытные усиления.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассеивание чар|cffced4da: снимает положительные заклинания с врагов и наносит урон призванным существам.|n"
        "- |cffa9c7deДух зверя|cffced4da: увеличивает скорость атаки и передвижения союзника.|n"
        "- |cffa9c7deТемная стая|cffced4da: выпускает стаю нетопырей, поражающую врагов на линии.|n"
        "- |cffa9c7deНутро зверя|cffced4da: пробивает броню цели.|n"
        "- |cffa9c7deКровотечение|cffced4da: периодический урон после атаки.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0J0", "field": "name", "expected": wts_updates[22495]})
    checks_def.append({"type": "unit", "id": "h0J0", "field": "tip", "expected": wts_updates[22497]})
    checks_def.append({"type": "unit", "id": "h0J0", "field": "ubertip", "expected": wts_updates[31674]})

    # h0J1: Полудикий ворген (W)
    wts_updates[22548] = "|cffe4cfa3Полудикий ворген|r"
    wts_updates[22551] = "|cffe4cfa3Полудикий ворген|r (|cffffffffW|r)"
    wts_updates[31726] = (
        "|cffa6afb8ЮНИТ:|cffced4da Свирепый боец передовой линии с острыми когтями.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗвериные рефлексы|cffced4da: шанс уклониться от вражеской атаки и нанести критический удар.|n"
        "- |cffa9c7deНутро зверя|cffced4da: пробивает среднюю и тяжёлую броню цели.|n"
        "- |cffa9c7deКровотечение|cffced4da: периодический урон после атаки.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0J1", "field": "name", "expected": wts_updates[22548]})
    checks_def.append({"type": "unit", "id": "h0J1", "field": "tip", "expected": wts_updates[22551]})
    checks_def.append({"type": "unit", "id": "h0J1", "field": "ubertip", "expected": wts_updates[31726]})

    # h0NA: Топорометатель (E)
    wts_updates[32792] = "|cffe4cfa3Топорометатель|r"
    wts_updates[32793] = "|cffe4cfa3Топорометатель|r (|cffffffffE|r)"
    wts_updates[31729] = (
        "|cffa6afb8ЮНИТ:|cffced4da Опытный метатель топоров, поражающий врагов на средней дистанции.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМетнуть топор|cffced4da: бросает топор, нанося урон и оглушая цель.|n"
        "- |cffa9c7deЯростный бросок|cffced4da: шанс нанести критический урон при атаке.|n"
        "- |cffa9c7deНутро зверя|cffced4da: пробивает броню цели.|n"
        "- |cffa9c7deКровотечение|cffced4da: периодический урон после атаки.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0NA", "field": "name", "expected": wts_updates[32792]})
    checks_def.append({"type": "unit", "id": "h0NA", "field": "tip", "expected": wts_updates[32793]})
    checks_def.append({"type": "unit", "id": "h0NA", "field": "ubertip", "expected": wts_updates[31729]})

    # o02T: Катапульта (E)
    wts_updates[22860] = "|cffe4cfa3Катапульта|r"
    wts_updates[22861] = "|cffe4cfa3Катапульта|r (|cffffffffE|r)"
    wts_updates[31609] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлое осадное орудие дальнего боя. Наносит осадный урон по площади.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o02T", "field": "name", "expected": wts_updates[22860]})
    checks_def.append({"type": "unit", "id": "o02T", "field": "tip", "expected": wts_updates[22861]})
    checks_def.append({"type": "unit", "id": "o02T", "field": "ubertip", "expected": wts_updates[31609]})

    # =========================================================================
    # 5. HEROES (4 heroes)
    # =========================================================================
    # H0J2: Верховный охотник (E)
    wts_updates[32680] = "|cffe4cfa3Верховный охотник|r"
    wts_updates[24537] = "|cffe4cfa3Бузан Охотник|r"
    wts_updates[31874] = "|cffe4cfa3Верховный охотник|r (|cffffffffE|r)"
    wts_updates[31873] = "|cffe4cfa3Верховный охотник|r"
    wts_updates[31875] = "|cffe4cfa3Верховный охотник|r"
    wts_updates[25156] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могучий вожак стаи и непревзойдённый следопыт. Специализируется на подавлении одиночных целей и сокрушительных ударах.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКопье охотника|cffced4da: оглушает врага и наносит урон.|n"
        "- |cffa9c7deСокрушающий удар|cffced4da: наносит урон по земле и замедляет противников.|n"
        "- |cffa9c7deСлабое место|cffced4da: пассивно наносит многократный критический урон.|n"
        "- |cffa9c7deДух древнего волка|cffced4da: призывает на помощь духов древних волков.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H0J2", "field": "name", "expected": wts_updates[32680]})
    checks_def.append({"type": "unit", "id": "H0J2", "field": "propernames", "expected": wts_updates[24537]})
    checks_def.append({"type": "unit", "id": "H0J2", "field": "tip", "expected": wts_updates[31874]})
    checks_def.append({"type": "unit", "id": "H0J2", "field": "awakentip", "expected": wts_updates[31873]})
    checks_def.append({"type": "unit", "id": "H0J2", "field": "revivetip", "expected": wts_updates[31875]})
    checks_def.append({"type": "unit", "id": "H0J2", "field": "ubertip", "expected": wts_updates[25156]})

    # H0J6: Лорд друид (W)
    wts_updates[24944] = "|cffe4cfa3Лорд друид|r"
    wts_updates[24943] = "|cffe4cfa3Друид|r"
    wts_updates[24946] = "|cffe4cfa3Лорд друид|r (|cffffffffW|r)"
    wts_updates[24945] = "|cffe4cfa3Лорд друид|r"
    wts_updates[24947] = "|cffe4cfa3Лорд друид|r"
    wts_updates[25157] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Мудрый повелитель сил природы, подчинивший звериную сущность. Обеспечивает союзников маной и сокрушает врагов молниями.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЦепная молния|cffced4da: поражает молнией несколько вражеских целей.|n"
        "- |cffa9c7deБлагословение духов|cffced4da: аура, ускоряющая восстановление маны союзников.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает входящий урон за счёт маны.|n"
        "- |cffa9c7deЗов Духов|cffced4da: пассивно ускоряет регенерацию здоровья и маны героя.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H0J6", "field": "name", "expected": wts_updates[24944]})
    checks_def.append({"type": "unit", "id": "H0J6", "field": "propernames", "expected": wts_updates[24943]})
    checks_def.append({"type": "unit", "id": "H0J6", "field": "tip", "expected": wts_updates[24946]})
    checks_def.append({"type": "unit", "id": "H0J6", "field": "awakentip", "expected": wts_updates[24945]})
    checks_def.append({"type": "unit", "id": "H0J6", "field": "revivetip", "expected": wts_updates[24947]})
    checks_def.append({"type": "unit", "id": "H0J6", "field": "ubertip", "expected": wts_updates[25157]})

    # H0J7: Генерал Гилнеаса (Q)
    wts_updates[25018] = "|cffe4cfa3Генерал Гилнеаса|r"
    wts_updates[25017] = "|cffe4cfa3Генерал|r"
    wts_updates[25021] = "|cffe4cfa3Генерал Гилнеаса|r (|cffffffffQ|r)"
    wts_updates[25019] = "|cffe4cfa3Генерал Гилнеаса|r"
    wts_updates[25020] = "|cffe4cfa3Генерал Гилнеаса|r"
    wts_updates[31876] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Храбрый военачальник королевства. Вдохновляет армию аурой урона, сокрушает ряды врагов и принимает несокрушимый облик.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолчьи рефлексы|cffced4da: шанс уклонения и нанесения критического урона.|n"
        "- |cffa9c7deВолна силы|cffced4da: выпускает сокрушительную волну энергии.|n"
        "- |cffa9c7deАура командира|cffced4da: увеличивает атаку союзных войск вокруг.|n"
        "- |cffa9c7deАватара зверя|cffced4da: дарует бонус к броне, здоровью, урону и иммунитет к магии.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H0J7", "field": "name", "expected": wts_updates[25018]})
    checks_def.append({"type": "unit", "id": "H0J7", "field": "propernames", "expected": wts_updates[25017]})
    checks_def.append({"type": "unit", "id": "H0J7", "field": "tip", "expected": wts_updates[25021]})
    checks_def.append({"type": "unit", "id": "H0J7", "field": "awakentip", "expected": wts_updates[25019]})
    checks_def.append({"type": "unit", "id": "H0J7", "field": "revivetip", "expected": wts_updates[25020]})
    checks_def.append({"type": "unit", "id": "H0J7", "field": "ubertip", "expected": wts_updates[31876]})

    # H0J8: Полубог (Голдринн) (C)
    wts_updates[25049] = "|cffe4cfa3Полубог|r"
    wts_updates[25048] = "|cffe4cfa3Голдринн|r"
    wts_updates[25052] = "|cffe4cfa3Полубог|r (|cffffffffC|r)"
    wts_updates[25050] = "|cffe4cfa3Полубог|r"
    wts_updates[25051] = "|cffe4cfa3Полубог|r"
    wts_updates[31877] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный полубог-волк древности. Обладает сокрушительными ударами по площади, вампиризмом и боевым ревом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСокрушение|cffced4da: наносит урон по области при атаке.|n"
        "- |cffa9c7deПоглощение урона|cffced4da: снижает урон врагов и поглощает входящие удары.|n"
        "- |cffa9c7deВампирическая аура|cffced4da: союзники ближнего боя восстанавливают здоровье от нанесённого урона.|n"
        "- |cffa9c7deЗов Полубога|cffced4da: издаёт боевой рёв, временно усиливающий урон союзников.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H0J8", "field": "name", "expected": wts_updates[25049]})
    checks_def.append({"type": "unit", "id": "H0J8", "field": "propernames", "expected": wts_updates[25048]})
    checks_def.append({"type": "unit", "id": "H0J8", "field": "tip", "expected": wts_updates[25052]})
    checks_def.append({"type": "unit", "id": "H0J8", "field": "awakentip", "expected": wts_updates[25050]})
    checks_def.append({"type": "unit", "id": "H0J8", "field": "revivetip", "expected": wts_updates[25051]})
    checks_def.append({"type": "unit", "id": "H0J8", "field": "ubertip", "expected": wts_updates[31877]})

    # =========================================================================
    # 6. UPGRADES (14 upgrades)
    # =========================================================================
    # R0EY: Улучшенные инструменты (4 уровня, E)
    wts_updates[19103] = "|cffe4cfa3Улучшенные инструменты — уровень 1|r"
    wts_updates[19367] = "|cffe4cfa3Улучшенные инструменты — уровень 2|r"
    wts_updates[19565] = "|cffe4cfa3Улучшенные инструменты — уровень 3|r"
    wts_updates[21119] = "|cffe4cfa3Улучшенные инструменты — уровень 4|r"
    wts_updates[21127] = "|cffe4cfa3Улучшенные инструменты — уровень 1|r (|cffffffffE|r)"
    wts_updates[21188] = "|cffe4cfa3Улучшенные инструменты — уровень 2|r (|cffffffffE|r)"
    wts_updates[21324] = "|cffe4cfa3Улучшенные инструменты — уровень 3|r (|cffffffffE|r)"
    wts_updates[21343] = "|cffe4cfa3Улучшенные инструменты — уровень 4|r (|cffffffffE|r)"
    wts_updates[24798] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой древесины рабочими на |cffc8e0878|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПостройщик|cffced4da.|n|n"
        "Уровень исследования: |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[24793] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой древесины рабочими ещё на |cffc8e0878|cffced4da ед. (суммарно +|cffffffff16|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПостройщик|cffced4da.|n|n"
        "Уровень исследования: |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[24794] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой древесины рабочими ещё на |cffc8e0878|cffced4da ед. (суммарно +|cffffffff24|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПостройщик|cffced4da.|n|n"
        "Уровень исследования: |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[24795] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой древесины рабочими ещё на |cffc8e0878|cffced4da ед. (суммарно +|cffffffff32|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПостройщик|cffced4da.|n|n"
        "Уровень исследования: |cffffffff4/4|cffced4da.|r"
    )

    # R0EM: Оружие ближнего боя (6 уровней, Q)
    wts_updates[24439] = "|cffe4cfa3Железные мечи|r"
    wts_updates[24437] = "|cffe4cfa3Железные мечи|r"
    wts_updates[24436] = "|cffe4cfa3Стальные мечи|r"
    wts_updates[24435] = "|cffe4cfa3Стальные мечи|r"
    wts_updates[24434] = "|cffe4cfa3Мифриловые мечи|r"
    wts_updates[24433] = "|cffe4cfa3Мифриловые мечи|r"
    wts_updates[24444] = "|cffe4cfa3Железные мечи — уровень 1|r (|cffffffffQ|r)"
    wts_updates[24443] = "|cffe4cfa3Железные мечи — уровень 2|r (|cffffffffQ|r)"
    wts_updates[24442] = "|cffe4cfa3Стальные мечи — уровень 3|r (|cffffffffQ|r)"
    wts_updates[24441] = "|cffe4cfa3Стальные мечи — уровень 4|r (|cffffffffQ|r)"
    wts_updates[24440] = "|cffe4cfa3Мифриловые мечи — уровень 5|r (|cffffffffQ|r)"
    wts_updates[24438] = "|cffe4cfa3Мифриловые мечи — уровень 6|r (|cffffffffQ|r)"
    wts_updates[24445] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон в ближнем бою пехотинцев, рыцарей, друидов и полудиких воргенов на |cffc8e0871|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|n|n"
        "Уровень исследования: |cffffffff1/6|cffced4da.|r"
    )
    wts_updates[24446] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон в ближнем бою пехотинцев, рыцарей, друидов и полудиких воргенов ещё на |cffc8e0871|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|n|n"
        "Уровень исследования: |cffffffff2/6|cffced4da.|r"
    )
    wts_updates[24447] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон в ближнем бою пехотинцев, рыцарей, друидов и полудиких воргенов ещё на |cffc8e0871|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|n|n"
        "Уровень исследования: |cffffffff3/6|cffced4da.|r"
    )
    wts_updates[24449] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон в ближнем бою пехотинцев, рыцарей, друидов и полудиких воргенов ещё на |cffc8e0871|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|n|n"
        "Уровень исследования: |cffffffff4/6|cffced4da.|r"
    )
    wts_updates[24448] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон в ближнем бою пехотинцев, рыцарей, друидов и полудиких воргенов ещё на |cffc8e0871|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|n|n"
        "Уровень исследования: |cffffffff5/6|cffced4da.|r"
    )
    wts_updates[24450] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон в ближнем бою пехотинцев, рыцарей, друидов и полудиких воргенов ещё на |cffc8e0871|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|n|n"
        "Уровень исследования: |cffffffff6/6|cffced4da.|r"
    )

    # R0EN: Кованая броня (6 уровней, A)
    wts_updates[24454] = "|cffe4cfa3Железная броня|r"
    wts_updates[24456] = "|cffe4cfa3Железная броня|r"
    wts_updates[24455] = "|cffe4cfa3Стальная броня|r"
    wts_updates[24459] = "|cffe4cfa3Стальная броня|r"
    wts_updates[24458] = "|cffe4cfa3Мифриловая броня|r"
    wts_updates[24457] = "|cffe4cfa3Мифриловая броня|r"
    wts_updates[24460] = "|cffe4cfa3Железная броня — уровень 1|r (|cffffffffA|r)"
    wts_updates[24461] = "|cffe4cfa3Железная броня — уровень 2|r (|cffffffffA|r)"
    wts_updates[24462] = "|cffe4cfa3Стальная броня — уровень 3|r (|cffffffffA|r)"
    wts_updates[24465] = "|cffe4cfa3Стальная броня — уровень 4|r (|cffffffffA|r)"
    wts_updates[24464] = "|cffe4cfa3Мифриловая броня — уровень 5|r (|cffffffffA|r)"
    wts_updates[24463] = "|cffe4cfa3Мифриловая броня — уровень 6|r (|cffffffffA|r)"
    for sid, lvl in [(24466, 1), (24467, 2), (24468, 3), (24473, 4), (24474, 5), (24475, 6)]:
        wts_updates[sid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает защиту пехотинцев, рыцарей, друидов и полудиких воргенов на |cffc8e0871.5|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R0EO: Оружие дальнего боя (6 уровней, W)
    wts_updates[24476] = "|cffe4cfa3Черный порох|r"
    wts_updates[24477] = "|cffe4cfa3Черный порох|r"
    wts_updates[24478] = "|cffe4cfa3Бездымный порох|r"
    wts_updates[24494] = "|cffe4cfa3Бездымный порох|r"
    wts_updates[24493] = "|cffe4cfa3Обогащенный порох|r"
    wts_updates[24492] = "|cffe4cfa3Обогащенный порох|r"
    wts_updates[24479] = "|cffe4cfa3Черный порох — уровень 1|r (|cffffffffW|r)"
    wts_updates[24480] = "|cffe4cfa3Черный порох — уровень 2|r (|cffffffffW|r)"
    wts_updates[24481] = "|cffe4cfa3Бездымный порох — уровень 3|r (|cffffffffW|r)"
    wts_updates[24497] = "|cffe4cfa3Бездымный порох — уровень 4|r (|cffffffffW|r)"
    wts_updates[24496] = "|cffe4cfa3Обогащенный порох — уровень 5|r (|cffffffffW|r)"
    wts_updates[24495] = "|cffe4cfa3Обогащенный порох — уровень 6|r (|cffffffffW|r)"
    for sid, lvl in [(24482, 1), (24483, 2), (24484, 3), (24498, 4), (24499, 5), (24500, 6)]:
        wts_updates[sid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон стрелков, топорометателей, магов и катапульт на |cffc8e0871|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deТопорометатель|cffced4da|n- |cffa9c7deВорген маг|cffced4da|n- |cffa9c7deКатапульта|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R0EP: Кожаная броня (6 уровней, S)
    wts_updates[24522] = "|cffe4cfa3Накидки из клепаной кожи|r"
    wts_updates[24501] = "|cffe4cfa3Накидки из клепаной кожи|r"
    wts_updates[24502] = "|cffe4cfa3Накидки из армированной кожи|r"
    wts_updates[24511] = "|cffe4cfa3Накидки из армированной кожи|r"
    wts_updates[24510] = "|cffe4cfa3Накидки из драконьей кожи|r"
    wts_updates[24509] = "|cffe4cfa3Накидки из драконьей кожи|r"
    wts_updates[24503] = "|cffe4cfa3Накидки из клепаной кожи — уровень 1|r (|cffffffffS|r)"
    wts_updates[24504] = "|cffe4cfa3Накидки из клепаной кожи — уровень 2|r (|cffffffffS|r)"
    wts_updates[24505] = "|cffe4cfa3Накидки из армированной кожи — уровень 3|r (|cffffffffS|r)"
    wts_updates[24508] = "|cffe4cfa3Накидки из армированной кожи — уровень 4|r (|cffffffffS|r)"
    wts_updates[24507] = "|cffe4cfa3Накидки из драконьей кожи — уровень 5|r (|cffffffffS|r)"
    wts_updates[24506] = "|cffe4cfa3Накидки из драконьей кожи — уровень 6|r (|cffffffffS|r)"
    for sid, lvl in [(24519, 1), (24520, 2), (24521, 3), (24512, 4), (24513, 5), (24514, 6)]:
        wts_updates[sid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает защиту стрелков, топорометателей, магов и катапульт на |cffc8e0871.5|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deТопорометатель|cffced4da|n- |cffa9c7deВорген маг|cffced4da|n- |cffa9c7deКатапульта|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R0EQ: Нутро зверя (3 уровня, D)
    wts_updates[24815] = "|cffe4cfa3Нутро зверя — уровень 1|r"
    wts_updates[24816] = "|cffe4cfa3Нутро зверя — уровень 2|r"
    wts_updates[24817] = "|cffe4cfa3Нутро зверя — уровень 3|r"
    wts_updates[24530] = "|cffe4cfa3Нутро зверя — уровень 1|r (|cffffffffD|r)"
    wts_updates[24531] = "|cffe4cfa3Нутро зверя — уровень 2|r (|cffffffffD|r)"
    wts_updates[24532] = "|cffe4cfa3Нутро зверя — уровень 3|r (|cffffffffD|r)"
    wts_updates[24818] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет воинам воргенов пробивать среднюю броню цели на |cffc8e08715%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Войскам воргенов.|n|n"
        "Уровень исследования: |cffffffff1/3|cffced4da.|r"
    )
    wts_updates[24819] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет воинам воргенов пробивать среднюю и тяжёлую броню цели на |cffc8e08715%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Войскам воргенов.|n|n"
        "Уровень исследования: |cffffffff2/3|cffced4da.|r"
    )
    wts_updates[24820] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно вызывает |cffc8e087кровотечение|cffced4da при атаках воргенов.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Войскам воргенов.|n|n"
        "Уровень исследования: |cffffffff3/3|cffced4da.|r"
    )

    # R0IP: Дрессировка Топорометателей (A)
    wts_updates[32816] = "|cffe4cfa3Дрессировка Топорометателей|r"
    wts_updates[32817] = "|cffe4cfa3Дрессировка Топорометателей|r (|cffffffffA|r)"
    wts_updates[32818] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья топорометателей на |cffc8e087100|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deТопорометатель|cffced4da.|r"
    )

    # R0F6: Волчья кровь (A)
    wts_updates[24938] = "|cffe4cfa3Волчья кровь|r"
    wts_updates[24939] = "|cffe4cfa3Волчья кровь|r (|cffffffffA|r)"
    wts_updates[24940] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обостряет рефлексы воргенов, увеличивая скорость перемещения на |cffc8e08735|cffced4da ед. и скорость атаки на |cffc8e08710%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deРыцарь|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deВорген маг|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da|n- |cffa9c7deТопорометатель|cffced4da.|r"
    )

    # R0F5: Дрессировка (S)
    wts_updates[24930] = "|cffe4cfa3Дрессировка рыцарей|r"
    wts_updates[24931] = "|cffe4cfa3Дрессировка рыцарей|r (|cffffffffS|r)"
    wts_updates[24932] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья рыцарей на |cffc8e087100|cffced4da ед. и скорость атаки на |cffc8e08720%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРыцарь|cffced4da.|r"
    )

    # R0EZ: Познания магии (2 уровня, A)
    wts_updates[24838] = "|cffe4cfa3Познания магии — посвящение|r"
    wts_updates[24839] = "|cffe4cfa3Познания магии — мастерство|r"
    wts_updates[24840] = "|cffe4cfa3Познания магии — посвящение|r (|cffffffffA|r)"
    wts_updates[24841] = "|cffe4cfa3Познания магии — мастерство|r (|cffffffffA|r)"
    wts_updates[24867] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас маны воргенов-магов на |cffc8e087100|cffced4da ед., скорость восстановления маны на |cffc8e0870.325|cffced4da/сек. и запас здоровья на |cffc8e08740|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВорген маг|cffced4da.|n|n"
        "Уровень исследования: |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[24868] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас маны воргенов-магов ещё на |cffc8e087100|cffced4da ед., скорость восстановления маны на |cffc8e0870.325|cffced4da/сек. и запас здоровья на |cffc8e08740|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВорген маг|cffced4da.|n|n"
        "Уровень исследования: |cffffffff2/2|cffced4da.|r"
    )

    # R0F1: Звериные рефлексы (X)
    wts_updates[27941] = "|cffe4cfa3Звериные рефлексы|r"
    wts_updates[28001] = "|cffe4cfa3Звериные рефлексы|r (|cffffffffX|r)"
    wts_updates[24857] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует полудиким воргенам способность «|cffa9c7deЗвериные рефлексы|cffced4da», позволяющую с вероятностью |cffc8e0875%|cffced4da уклониться от атаки и с вероятностью |cffc8e0876%|cffced4da нанести |cffffffff1.5|cffced4da-кратный урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da.|r"
    )

    # R0F0: Волчьи конечности (A)
    wts_updates[24851] = "|cffe4cfa3Волчьи конечности|r"
    wts_updates[24852] = "|cffe4cfa3Волчьи конечности|r (|cffffffffA|r)"
    wts_updates[25986] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость перемещения стрелков, друидов, магов, полудиких воргенов и топорометателей на |cffc8e08735|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deВорген друид|cffced4da|n- |cffa9c7deВорген маг|cffced4da|n- |cffa9c7deПолудикий ворген|cffced4da|n- |cffa9c7deТопорометатель|cffced4da.|r"
    )

    # R0F2: Слияние с природой (2 уровня, S)
    wts_updates[24858] = "|cffe4cfa3Слияние с природой — посвящение|r"
    wts_updates[24859] = "|cffe4cfa3Слияние с природой — мастерство|r"
    wts_updates[24860] = "|cffe4cfa3Слияние с природой — посвящение|r (|cffffffffS|r)"
    wts_updates[24861] = "|cffe4cfa3Слияние с природой — мастерство|r (|cffffffffS|r)"
    wts_updates[24862] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас маны друидов на |cffc8e087100|cffced4da ед., скорость восстановления маны на |cffc8e0870.325|cffced4da/сек. и запас здоровья на |cffc8e08740|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВорген друид|cffced4da.|n|n"
        "Уровень исследования: |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[24863] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас маны друидов ещё на |cffc8e087100|cffced4da ед., скорость восстановления маны на |cffc8e0870.325|cffced4da/сек. и запас здоровья на |cffc8e08740|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВорген друид|cffced4da.|n|n"
        "Уровень исследования: |cffffffff2/2|cffced4da.|r"
    )

    # =========================================================================
    # 7. ABILITIES
    # =========================================================================
    # A11I: Копье охотника (Q)
    wts_updates[24957] = "|cffe4cfa3Копье охотника|r"
    wts_updates[24958] = "|cffe4cfa3Копье охотника|r (|cffffffffQ|r)"
    wts_updates[24959] = "|cffe4cfa3Копье охотника — уровень 1|r (|cffffffffQ|r)"
    wts_updates[24960] = "|cffe4cfa3Копье охотника — уровень 2|r (|cffffffffQ|r)"
    wts_updates[24961] = "|cffe4cfa3Копье охотника — уровень 3|r (|cffffffffQ|r)"
    wts_updates[24962] = "|cffe4cfa3Копье охотника — уровень 4|r (|cffffffffQ|r)"
    wts_updates[24963] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает копьё во врага, нанося |cffffffff475|cffced4da ед. урона и оглушая цель на |cffffffff4.5|cffced4da сек. (|cffffffff1.5|cffced4da сек. для героев).|r"

    # A11H: Сокрушающий удар (W)
    wts_updates[24951] = "|cffe4cfa3Сокрушающий удар|r"
    wts_updates[24952] = "|cffe4cfa3Сокрушающий удар|r (|cffffffffW|r)"
    wts_updates[40363] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бьёт по земле, нанося урон наземным противникам вокруг и замедляя их скорость перемещения и атаки.|r"
    wts_updates[24954] = "|cffe4cfa3Сокрушающий удар — уровень 1|r (|cffffffffW|r)"
    wts_updates[24955] = "|cffe4cfa3Сокрушающий удар — уровень 2|r (|cffffffffW|r)"
    wts_updates[24956] = "|cffe4cfa3Сокрушающий удар — уровень 3|r (|cffffffffW|r)"
    wts_updates[24949] = "|cffe4cfa3Сокрушающий удар — уровень 4|r (|cffffffffW|r)"
    wts_updates[24950] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff300|cffced4da ед. урона наземным врагам вокруг, замедляя их перемещение на |cffe69a8d60%|cffced4da и скорость атаки на |cffe69a8d50%|cffced4da на |cffffffff5|cffced4da сек. (|cffffffff3|cffced4da сек. для героев).|r"

    # A11J: Слабое место (E)
    wts_updates[24967] = "|cffe4cfa3Слабое место|r"
    wts_updates[24968] = "|cffe4cfa3Слабое место|r (|cffffffffE|r)"
    wts_updates[24972] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс нанести критический урон при атаке.|r"
    wts_updates[24969] = "|cffe4cfa3Слабое место — уровень 1|r"
    wts_updates[24970] = "|cffe4cfa3Слабое место — уровень 2|r"
    wts_updates[24971] = "|cffe4cfa3Слабое место — уровень 3|r"
    wts_updates[24965] = "|cffe4cfa3Слабое место — уровень 4|r"
    wts_updates[24966] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff15%|cffced4da шанс нанести |cffffffff5|cffced4da-кратный критический урон при атаке.|r"

    # A11K: Дух древнего волка (R)
    wts_updates[24975] = "|cffe4cfa3Дух древнего волка|r"
    wts_updates[24976] = "|cffe4cfa3Дух древнего волка|r (|cffffffffR|r)"
    wts_updates[32099] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взывает к духам древних волков, призывая их на поле боя.|r"
    wts_updates[24977] = "|cffe4cfa3Дух древнего волка — уровень 1|r (|cffffffffR|r)"
    wts_updates[24978] = "|cffe4cfa3Дух древнего волка — уровень 2|r (|cffffffffR|r)"
    wts_updates[32100] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff1|cffced4da духа древнего волка на помощь герою. Время действия: |cffffffff60|cffced4da сек.|r"
    wts_updates[32101] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da духов древних волков на помощь герою. Время действия: |cffffffff60|cffced4da сек.|r"

    # A11L: Цепная молния (Q)
    wts_updates[39550] = "|cffe4cfa3Цепная молния|r"
    wts_updates[24983] = "|cffe4cfa3Цепная молния|r (|cffffffffQ|r)"
    wts_updates[24987] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает разряд молнии, который поражает цель и рикошетит по врагам рядом.|r"
    wts_updates[24984] = "|cffe4cfa3Цепная молния — уровень 1|r (|cffffffffQ|r)"
    wts_updates[24985] = "|cffe4cfa3Цепная молния — уровень 2|r (|cffffffffQ|r)"
    wts_updates[24986] = "|cffe4cfa3Цепная молния — уровень 3|r (|cffffffffQ|r)"
    wts_updates[24980] = "|cffe4cfa3Цепная молния — уровень 4|r (|cffffffffQ|r)"
    wts_updates[24981] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff275|cffced4da ед. урона основной цели и рикошетит до |cffffffff14|cffced4da раз. С каждым рикошетом урон снижается на |cffe69a8d15%|cffced4da.|r"

    # A11N: Благословение духов (E)
    wts_updates[25024] = "|cffe4cfa3Благословение духов|r"
    wts_updates[25025] = "|cffe4cfa3Благословение духов|r (|cffffffffE|r)"
    wts_updates[25026] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура, ускоряющая восстановление маны находящихся рядом союзных войск.|r"
    wts_updates[25027] = "|cffe4cfa3Благословение духов — уровень 1|r"
    wts_updates[25028] = "|cffe4cfa3Благословение духов — уровень 2|r"
    wts_updates[25029] = "|cffe4cfa3Благословение духов — уровень 3|r"
    wts_updates[25030] = "|cffe4cfa3Благословение духов — уровень 4|r"
    wts_updates[32183] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию маны находящихся рядом союзников на |cffc8e0873.00|cffced4da ед./сек.|r"

    # A11M: Щит маны (W)
    wts_updates[24988] = "|cffe4cfa3Щит маны|r"
    wts_updates[24989] = "|cffe4cfa3Щит маны|r (|cffffffffW|r)"
    wts_updates[24999] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт защитный барьер, поглощающий входящий урон за счёт маны.|r"
    wts_updates[24990] = "|cffe4cfa3Щит маны — уровень 1|r (|cffffffffW|r)"
    wts_updates[24991] = "|cffe4cfa3Щит маны — уровень 2|r (|cffffffffW|r)"
    wts_updates[24992] = "|cffe4cfa3Щит маны — уровень 3|r (|cffffffffW|r)"
    wts_updates[24993] = "|cffe4cfa3Щит маны — уровень 4|r (|cffffffffW|r)"
    wts_updates[24994] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт щит, поглощающий |cffffffff2.5|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|r"

    # A11O: Зов Духов (R)
    wts_updates[25037] = "|cffe4cfa3Зов Духов|r"
    wts_updates[25035] = "|cffe4cfa3Зов Духов|r (|cffffffffR|r)"
    wts_updates[35420] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Постоянно ускоряет регенерацию здоровья и маны героя.|r"
    wts_updates[25031] = "|cffe4cfa3Зов Духов — уровень 1|r"
    wts_updates[25032] = "|cffe4cfa3Зов Духов — уровень 2|r"
    wts_updates[35411] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость регенерации здоровья и маны героя на |cffc8e0875|cffced4da ед./сек.|r"
    wts_updates[35412] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость регенерации здоровья и маны героя на |cffc8e0878|cffced4da ед./сек.|r"

    # A11Q: Волчьи рефлексы (W)
    wts_updates[41962] = "|cffe4cfa3Волчьи рефлексы|r"
    wts_updates[41963] = "|cffe4cfa3Волчьи рефлексы|r (|cffffffffW|r)"
    wts_updates[41964] = "|cffe4cfa3Волчьи рефлексы — уровень 1|r"
    wts_updates[41965] = "|cffe4cfa3Волчьи рефлексы — уровень 2|r"
    wts_updates[41966] = "|cffe4cfa3Волчьи рефлексы — уровень 3|r"
    wts_updates[41967] = "|cffe4cfa3Волчьи рефлексы — уровень 4|r"
    wts_updates[42005] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff5%|cffced4da шанс уклониться от атаки и |cffffffff10%|cffced4da шанс нанести |cffffffff1.5|cffced4da-кратный критический урон.|r"
    wts_updates[42006] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10%|cffced4da шанс уклониться от атаки и |cffffffff10%|cffced4da шанс нанести |cffffffff2.0|cffced4da-кратный критический урон.|r"
    wts_updates[42007] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff15%|cffced4da шанс уклониться от атаки и |cffffffff10%|cffced4da шанс нанести |cffffffff2.5|cffced4da-кратный критический урон.|r"
    wts_updates[42008] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff20%|cffced4da шанс уклониться от атаки и |cffffffff10%|cffced4da шанс нанести |cffffffff3.0|cffced4da-кратный критический урон.|r"

    # A11P: Волна силы (Q)
    wts_updates[38289] = "|cffe4cfa3Волна силы|r"
    wts_updates[38290] = "|cffe4cfa3Волна силы|r (|cffffffffQ|r)"
    wts_updates[27940] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает перед собой волну энергии, наносящую урон врагам на своём пути.|r"
    wts_updates[38291] = "|cffe4cfa3Волна силы — уровень 1|r (|cffffffffQ|r)"
    wts_updates[25059] = "|cffe4cfa3Волна силы — уровень 2|r (|cffffffffQ|r)"
    wts_updates[25060] = "|cffe4cfa3Волна силы — уровень 3|r (|cffffffffQ|r)"
    wts_updates[25054] = "|cffe4cfa3Волна силы — уровень 4|r (|cffffffffQ|r)"
    wts_updates[25061] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну энергии, наносящую |cffffffff100|cffced4da ед. урона противникам на пути.|r"
    wts_updates[25062] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну энергии, наносящую |cffffffff150|cffced4da ед. урона противникам на пути.|r"
    wts_updates[25063] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну энергии, наносящую |cffffffff200|cffced4da ед. урона противникам на пути.|r"
    wts_updates[25055] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну энергии, наносящую |cffffffff300|cffced4da ед. урона противникам на пути.|r"

    # A11R: Аура командира (E)
    wts_updates[25071] = "|cffe4cfa3Аура командира|r"
    wts_updates[25073] = "|cffe4cfa3Аура командира|r (|cffffffffE|r)"
    wts_updates[20168] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура, увеличивающая урон находящихся рядом союзных войск.|r"
    wts_updates[25072] = "|cffe4cfa3Аура командира — уровень 1|r"
    wts_updates[25074] = "|cffe4cfa3Аура командира — уровень 2|r"
    wts_updates[25075] = "|cffe4cfa3Аура командира — уровень 3|r"
    wts_updates[25076] = "|cffe4cfa3Аура командира — уровень 4|r"
    wts_updates[32196] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзных войск рядом на |cffc8e0877%|cffced4da.|r"
    wts_updates[32102] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзных войск рядом на |cffc8e08710%|cffced4da.|r"
    wts_updates[32138] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзных войск рядом на |cffc8e08715%|cffced4da.|r"
    wts_updates[20167] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзных войск рядом на |cffc8e08730%|cffced4da.|r"

    # A11S: Аватара зверя (R)
    wts_updates[25082] = "|cffe4cfa3Аватара зверя|r"
    wts_updates[25083] = "|cffe4cfa3Аватара зверя|r (|cffffffffR|r)"
    wts_updates[25086] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Временно наделяет генерала колоссальной силой, увеличивая броню, здоровье, урон и даруя невосприимчивость к магии.|r"
    wts_updates[25084] = "|cffe4cfa3Аватара зверя — уровень 1|r (|cffffffffR|r)"
    wts_updates[25087] = "|cffe4cfa3Аватара зверя — уровень 2|r (|cffffffffR|r)"
    wts_updates[25088] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует генералу +|cffc8e0875|cffced4da к броне, +|cffc8e087500|cffced4da к здоровью, +|cffc8e08720|cffced4da к урону и невосприимчивость к магии на |cffffffff60|cffced4da сек.|r"
    wts_updates[25089] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует генералу +|cffc8e08710|cffced4da к броне, +|cffc8e0871000|cffced4da к здоровью, +|cffc8e08740|cffced4da к урону и невосприимчивость к магии на |cffffffff60|cffced4da сек.|r"

    # A11Z: Сокрушение (Q)
    wts_updates[25133] = "|cffe4cfa3Сокрушение|r"
    wts_updates[25134] = "|cffe4cfa3Сокрушение|r (|cffffffffQ|r)"
    wts_updates[31917] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При атаке наносит урон по области находящимся рядом врагам.|r"
    wts_updates[25135] = "|cffe4cfa3Сокрушение — уровень 1|r"
    wts_updates[25136] = "|cffe4cfa3Сокрушение — уровень 2|r"
    wts_updates[25137] = "|cffe4cfa3Сокрушение — уровень 3|r"
    wts_updates[25138] = "|cffe4cfa3Сокрушение — уровень 4|r"
    wts_updates[31918] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff17%|cffced4da атака наносит |cffffffff40|cffced4da ед. урона врагам поблизости.|r"
    wts_updates[31919] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff23%|cffced4da атака наносит |cffffffff50|cffced4da ед. урона врагам поблизости.|r"
    wts_updates[31920] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff30%|cffced4da атака наносит |cffffffff60|cffced4da ед. урона врагам поблизости.|r"
    wts_updates[31921] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff35%|cffced4da атака наносит |cffffffff90|cffced4da ед. урона врагам поблизости.|r"

    # A11U: Поглощение урона (W)
    wts_updates[20281] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[16590] = "|cffe4cfa3Поглощение урона|r (|cffffffffW|r)"
    wts_updates[16675] = "|cffe4cfa3Поглощение урона — уровень 1|r (|cffffffffW|r)"
    wts_updates[16676] = "|cffe4cfa3Поглощение урона — уровень 2|r (|cffffffffW|r)"
    wts_updates[17828] = "|cffe4cfa3Поглощение урона — уровень 3|r (|cffffffffW|r)"
    wts_updates[17830] = "|cffe4cfa3Поглощение урона — уровень 4|r (|cffffffffW|r)"

    # A11V, A11W, A11X, A11Y
    wts_updates[25100] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[25107] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[25108] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[25110] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[25111] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[25113] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[25114] = "|cffe4cfa3Поглощение урона|r"
    wts_updates[25116] = "|cffe4cfa3Поглощение урона|r"

    # A11T: Вампирическая аура (E)
    wts_updates[25091] = "|cffe4cfa3Вампирическая аура|r"
    wts_updates[25092] = "|cffe4cfa3Вампирическая аура|r (|cffffffffE|r)"
    wts_updates[24736] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Союзные войска ближнего боя восстанавливают здоровье в размере части наносимого ими урона.|r"
    wts_updates[25093] = "|cffe4cfa3Вампирическая аура — уровень 1|r"
    wts_updates[25094] = "|cffe4cfa3Вампирическая аура — уровень 2|r"
    wts_updates[25095] = "|cffe4cfa3Вампирическая аура — уровень 3|r"
    wts_updates[25096] = "|cffe4cfa3Вампирическая аура — уровень 4|r"
    wts_updates[25185] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Союзные войска ближнего боя рядом восстанавливают здоровье в объёме |cffc8e08720%|cffced4da от наносимого урона.|r"
    wts_updates[25591] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Союзные войска ближнего боя рядом восстанавливают здоровье в объёме |cffc8e08724%|cffced4da от наносимого урона.|r"
    wts_updates[27000] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Союзные войска ближнего боя рядом восстанавливают здоровье в объёме |cffc8e08731%|cffced4da от наносимого урона.|r"
    wts_updates[20570] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Союзные войска ближнего боя рядом восстанавливают здоровье в объёме |cffc8e08738%|cffced4da от наносимого урона.|r"

    # A120: Зов Полубога (R)
    wts_updates[25142] = "|cffe4cfa3Зов Полубога|r"
    wts_updates[25143] = "|cffe4cfa3Зов Полубога|r (|cffffffffR|r)"
    wts_updates[25149] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издаёт первобытный боевой рёв, временно усиливающий урон всех союзных войск.|r"
    wts_updates[25140] = "|cffe4cfa3Зов Полубога — уровень 1|r (|cffffffffR|r)"
    wts_updates[25141] = "|cffe4cfa3Зов Полубога — уровень 2|r (|cffffffffR|r)"
    wts_updates[9804] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон находящихся рядом союзных войск на |cffc8e08750%|cffced4da на |cffffffff45|cffced4da сек.|r"

    # --- UNIT ABILITIES ---
    # A117, A118, A119: Нутро зверя
    wts_updates[24527] = "|cffe4cfa3Нутро зверя|r"
    wts_updates[24528] = "|cffe4cfa3Нутро зверя|r"

    wts_updates[24529] = "|cffe4cfa3Нутро зверя|r"
    wts_updates[24803] = "|cffe4cfa3Нутро зверя|r"

    wts_updates[24805] = "|cffe4cfa3Нутро зверя|r"
    wts_updates[24804] = "|cffe4cfa3Нутро зверя|r"
    wts_updates[24807] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Когти воргенов пробивают среднюю и тяжёлую броню цели на |cffc8e08715%|cffced4da, оставляя кровотечение при атаках.|r"

    # A11A: Кровотечение
    wts_updates[29198] = "|cffe4cfa3Кровотечение|r"
    wts_updates[29199] = "|cffe4cfa3Кровотечение|r"
    wts_updates[36630] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ранит цель, нанося |cffffffff5|cffced4da ед. урона в секунду в течение |cffffffff5|cffced4da сек. Эффект не суммируется.|r"

    # A11B: Дух зверя (W)
    wts_updates[24825] = "|cffe4cfa3Дух зверя|r"
    wts_updates[24826] = "|cffe4cfa3Дух зверя|r (|cffffffffW|r)"

    # A11C: Звериные рефлексы
    wts_updates[27938] = "|cffe4cfa3Звериные рефлексы|r"
    wts_updates[27939] = "|cffe4cfa3Звериные рефлексы|r"
    wts_updates[15379] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff5%|cffced4da шанс уклониться от вражеской атаки и |cffffffff6%|cffced4da шанс нанести |cffffffff1.5|cffced4da-кратный критический урон.|r"

    # A11D: Вой (W)
    wts_updates[24879] = "|cffe4cfa3Вой|r"
    wts_updates[24878] = "|cffe4cfa3Вой|r (|cffffffffW|r)"

    # A11E: Эссенция здоровья (Q)
    wts_updates[24881] = "|cffe4cfa3Эссенция здоровья|r"
    wts_updates[24882] = "|cffe4cfa3Эссенция здоровья|r (|cffffffffQ|r)"

    # A1F0: Яростный бросок
    wts_updates[32795] = "|cffe4cfa3Яростный бросок|r"
    wts_updates[32796] = "|cffe4cfa3Яростный бросок|r"

    # A1F1: Метнуть топор (Q)
    wts_updates[32807] = "|cffe4cfa3Метнуть топор|r"
    wts_updates[25343] = "|cffe4cfa3Метнуть топор|r"
    wts_updates[29427] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает топор во врага, нанося урон и оглушая цель.|r"
    wts_updates[32801] = "|cffe4cfa3Метнуть топор|r (|cffffffffQ|r)"
    wts_updates[32809] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает топор во врага, нанося |cffffffff75|cffced4da ед. урона и оглушая цель на |cffffffff2|cffced4da сек.|r"

    # A0PE: Темная стая (E)
    wts_updates[39816] = "|cffe4cfa3Темная стая|r"
    wts_updates[40259] = "|cffe4cfa3Темная стая|r (|cffffffffE|r)"
    wts_updates[41717] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стаю нетопырей, наносящую до |cffffffff90|cffced4da ед. урона наземным врагам на прямой линии (максимум |cffffffff400|cffced4da ед.).|r"

    # Adis: Рассеивание чар (Q)
    wts_updates[25772] = "|cffe4cfa3Рассеивание чар|r"
    wts_updates[25785] = "|cffe4cfa3Рассеивание чар|r (|cffffffffQ|r)"
    wts_updates[25774] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает положительные эффекты с врагов в выбранной области и наносит |cffffffff200|cffced4da ед. урона призванным существам.|r"

    # =========================================================================
    # 8. BUFFS (4 custom buffs)
    # =========================================================================
    # B06A
    wts_updates[29471] = "|cffe4cfa3Кровотечение|r"
    wts_updates[24811] = "|cffa6afb8ЭФФЕКТ:|cffced4da Этот юнит ранен когтями воргена и получает периодический урон.|r"
    checks_def.append({"type": "buff", "id": "B06A", "field": "bufftip", "expected": wts_updates[29471]})
    checks_def.append({"type": "buff", "id": "B06A", "field": "buffubertip", "expected": wts_updates[24811]})

    # B06B
    wts_updates[29472] = "|cffe4cfa3Кровотечение|r"
    wts_updates[24813] = "|cffa6afb8ЭФФЕКТ:|cffced4da Этот юнит ранен когтями воргена и получает периодический урон.|r"
    checks_def.append({"type": "buff", "id": "B06B", "field": "bufftip", "expected": wts_updates[29472]})
    checks_def.append({"type": "buff", "id": "B06B", "field": "buffubertip", "expected": wts_updates[24813]})

    # B06C
    wts_updates[25038] = "|cffe4cfa3Зов Духов|r"
    wts_updates[25039] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость восстановления здоровья и маны этого героя увеличена.|r"
    checks_def.append({"type": "buff", "id": "B06C", "field": "bufftip", "expected": wts_updates[25038]})
    checks_def.append({"type": "buff", "id": "B06C", "field": "buffubertip", "expected": wts_updates[25039]})

    # B06D
    wts_updates[25144] = "|cffe4cfa3Зов Полубога|r"
    wts_updates[25145] = "|cffa6afb8ЭФФЕКТ:|cffced4da Боевой рёв Полубога увеличивает урон от атак этого воина.|r"
    checks_def.append({"type": "buff", "id": "B06D", "field": "bufftip", "expected": wts_updates[25144]})
    checks_def.append({"type": "buff", "id": "B06D", "field": "buffubertip", "expected": wts_updates[25145]})

    # Checks for ability and upgrade fields
    checks_def.append({"type": "ability", "id": "A11I", "field": "name", "expected": wts_updates[24957]})
    checks_def.append({"type": "ability", "id": "A11I", "field": "tip1", "expected": wts_updates[24959]})
    checks_def.append({"type": "ability", "id": "A11H", "field": "name", "expected": wts_updates[24951]})
    checks_def.append({"type": "ability", "id": "A11H", "field": "tip1", "expected": wts_updates[24954]})
    checks_def.append({"type": "ability", "id": "A11J", "field": "name", "expected": wts_updates[24967]})
    checks_def.append({"type": "ability", "id": "A11J", "field": "tip1", "expected": wts_updates[24969]})
    checks_def.append({"type": "ability", "id": "A11K", "field": "name", "expected": wts_updates[24975]})
    checks_def.append({"type": "ability", "id": "A11K", "field": "tip1", "expected": wts_updates[24977]})
    checks_def.append({"type": "ability", "id": "A11K", "field": "ubertip1", "expected": wts_updates[32100]})
    checks_def.append({"type": "ability", "id": "A11L", "field": "name", "expected": wts_updates[39550]})
    checks_def.append({"type": "ability", "id": "A11L", "field": "tip1", "expected": wts_updates[24984]})
    checks_def.append({"type": "ability", "id": "A11N", "field": "name", "expected": wts_updates[25024]})
    checks_def.append({"type": "ability", "id": "A11N", "field": "tip1", "expected": wts_updates[25027]})
    checks_def.append({"type": "ability", "id": "A11M", "field": "name", "expected": wts_updates[24988]})
    checks_def.append({"type": "ability", "id": "A11M", "field": "tip1", "expected": wts_updates[24990]})
    checks_def.append({"type": "ability", "id": "A11O", "field": "name", "expected": wts_updates[25037]})
    checks_def.append({"type": "ability", "id": "A11O", "field": "tip1", "expected": wts_updates[25031]})
    checks_def.append({"type": "ability", "id": "A11O", "field": "ubertip1", "expected": wts_updates[35411]})
    checks_def.append({"type": "ability", "id": "A11Q", "field": "name", "expected": wts_updates[41962]})
    checks_def.append({"type": "ability", "id": "A11Q", "field": "tip1", "expected": wts_updates[41964]})
    checks_def.append({"type": "ability", "id": "A11Q", "field": "ubertip1", "expected": wts_updates[42005]})
    checks_def.append({"type": "ability", "id": "A11P", "field": "name", "expected": wts_updates[38289]})
    checks_def.append({"type": "ability", "id": "A11P", "field": "tip1", "expected": wts_updates[38291]})
    checks_def.append({"type": "ability", "id": "A11P", "field": "ubertip1", "expected": wts_updates[25061]})
    checks_def.append({"type": "ability", "id": "A11R", "field": "name", "expected": wts_updates[25071]})
    checks_def.append({"type": "ability", "id": "A11R", "field": "tip1", "expected": wts_updates[25072]})
    checks_def.append({"type": "ability", "id": "A11R", "field": "ubertip1", "expected": wts_updates[32196]})
    checks_def.append({"type": "ability", "id": "A11S", "field": "name", "expected": wts_updates[25082]})
    checks_def.append({"type": "ability", "id": "A11S", "field": "tip1", "expected": wts_updates[25084]})
    checks_def.append({"type": "ability", "id": "A11S", "field": "ubertip1", "expected": wts_updates[25088]})
    checks_def.append({"type": "ability", "id": "A11Z", "field": "name", "expected": wts_updates[25133]})
    checks_def.append({"type": "ability", "id": "A11Z", "field": "tip1", "expected": wts_updates[25135]})
    checks_def.append({"type": "ability", "id": "A11Z", "field": "ubertip1", "expected": wts_updates[31918]})
    checks_def.append({"type": "ability", "id": "A11U", "field": "name", "expected": wts_updates[20281]})
    checks_def.append({"type": "ability", "id": "A11U", "field": "tip1", "expected": wts_updates[16675]})
    checks_def.append({"type": "ability", "id": "A11T", "field": "name", "expected": wts_updates[25091]})
    checks_def.append({"type": "ability", "id": "A11T", "field": "tip1", "expected": wts_updates[25093]})
    checks_def.append({"type": "ability", "id": "A11T", "field": "ubertip1", "expected": wts_updates[25185]})
    checks_def.append({"type": "ability", "id": "A120", "field": "name", "expected": wts_updates[25142]})
    checks_def.append({"type": "ability", "id": "A120", "field": "tip1", "expected": wts_updates[25140]})

    checks_def.append({"type": "ability", "id": "A11A", "field": "name", "expected": wts_updates[29198]})
    checks_def.append({"type": "ability", "id": "A11A", "field": "tip1", "expected": wts_updates[29199]})
    checks_def.append({"type": "ability", "id": "A11A", "field": "ubertip1", "expected": wts_updates[36630]})
    checks_def.append({"type": "ability", "id": "A11B", "field": "name", "expected": wts_updates[24825]})
    checks_def.append({"type": "ability", "id": "A11B", "field": "tip1", "expected": wts_updates[24826]})
    checks_def.append({"type": "ability", "id": "A11C", "field": "name", "expected": wts_updates[27938]})
    checks_def.append({"type": "ability", "id": "A11C", "field": "tip1", "expected": wts_updates[27939]})
    checks_def.append({"type": "ability", "id": "A11C", "field": "ubertip1", "expected": wts_updates[15379]})
    checks_def.append({"type": "ability", "id": "A11D", "field": "name", "expected": wts_updates[24879]})
    checks_def.append({"type": "ability", "id": "A11D", "field": "tip1", "expected": wts_updates[24878]})
    checks_def.append({"type": "ability", "id": "A11E", "field": "name", "expected": wts_updates[24881]})
    checks_def.append({"type": "ability", "id": "A11E", "field": "tip1", "expected": wts_updates[24882]})
    checks_def.append({"type": "ability", "id": "A1F0", "field": "name", "expected": wts_updates[32795]})
    checks_def.append({"type": "ability", "id": "A1F0", "field": "tip1", "expected": wts_updates[32796]})
    checks_def.append({"type": "ability", "id": "A1F1", "field": "name", "expected": wts_updates[32807]})
    checks_def.append({"type": "ability", "id": "A1F1", "field": "tip1", "expected": wts_updates[32801]})
    checks_def.append({"type": "ability", "id": "A1F1", "field": "ubertip1", "expected": wts_updates[32809]})
    checks_def.append({"type": "ability", "id": "A0PE", "field": "name", "expected": wts_updates[39816]})
    checks_def.append({"type": "ability", "id": "A0PE", "field": "tip1", "expected": wts_updates[40259]})
    checks_def.append({"type": "ability", "id": "A0PE", "field": "ubertip1", "expected": wts_updates[41717]})
    checks_def.append({"type": "ability", "id": "Adis", "field": "name", "expected": wts_updates[25772]})
    checks_def.append({"type": "ability", "id": "Adis", "field": "tip1", "expected": wts_updates[25785]})
    checks_def.append({"type": "ability", "id": "Adis", "field": "ubertip1", "expected": wts_updates[25774]})

    checks_def.append({"type": "upgrade", "id": "R0EY", "field": "name1", "expected": wts_updates[19103]})
    checks_def.append({"type": "upgrade", "id": "R0EY", "field": "tip1", "expected": wts_updates[21127]})
    checks_def.append({"type": "upgrade", "id": "R0EY", "field": "ubertip1", "expected": wts_updates[24798]})
    checks_def.append({"type": "upgrade", "id": "R0EM", "field": "name1", "expected": wts_updates[24439]})
    checks_def.append({"type": "upgrade", "id": "R0EM", "field": "tip1", "expected": wts_updates[24444]})
    checks_def.append({"type": "upgrade", "id": "R0EM", "field": "ubertip1", "expected": wts_updates[24445]})
    checks_def.append({"type": "upgrade", "id": "R0EN", "field": "name1", "expected": wts_updates[24454]})
    checks_def.append({"type": "upgrade", "id": "R0EN", "field": "tip1", "expected": wts_updates[24460]})
    checks_def.append({"type": "upgrade", "id": "R0EN", "field": "ubertip1", "expected": wts_updates[24466]})
    checks_def.append({"type": "upgrade", "id": "R0EO", "field": "name1", "expected": wts_updates[24476]})
    checks_def.append({"type": "upgrade", "id": "R0EO", "field": "tip1", "expected": wts_updates[24479]})
    checks_def.append({"type": "upgrade", "id": "R0EO", "field": "ubertip1", "expected": wts_updates[24482]})
    checks_def.append({"type": "upgrade", "id": "R0EP", "field": "name1", "expected": wts_updates[24522]})
    checks_def.append({"type": "upgrade", "id": "R0EP", "field": "tip1", "expected": wts_updates[24503]})
    checks_def.append({"type": "upgrade", "id": "R0EP", "field": "ubertip1", "expected": wts_updates[24519]})
    checks_def.append({"type": "upgrade", "id": "R0EQ", "field": "name1", "expected": wts_updates[24815]})
    checks_def.append({"type": "upgrade", "id": "R0EQ", "field": "tip1", "expected": wts_updates[24530]})
    checks_def.append({"type": "upgrade", "id": "R0EQ", "field": "ubertip1", "expected": wts_updates[24818]})
    checks_def.append({"type": "upgrade", "id": "R0IP", "field": "name1", "expected": wts_updates[32816]})
    checks_def.append({"type": "upgrade", "id": "R0IP", "field": "tip1", "expected": wts_updates[32817]})
    checks_def.append({"type": "upgrade", "id": "R0IP", "field": "ubertip1", "expected": wts_updates[32818]})
    checks_def.append({"type": "upgrade", "id": "R0F6", "field": "name1", "expected": wts_updates[24938]})
    checks_def.append({"type": "upgrade", "id": "R0F6", "field": "tip1", "expected": wts_updates[24939]})
    checks_def.append({"type": "upgrade", "id": "R0F6", "field": "ubertip1", "expected": wts_updates[24940]})
    checks_def.append({"type": "upgrade", "id": "R0F5", "field": "name1", "expected": wts_updates[24930]})
    checks_def.append({"type": "upgrade", "id": "R0F5", "field": "tip1", "expected": wts_updates[24931]})
    checks_def.append({"type": "upgrade", "id": "R0F5", "field": "ubertip1", "expected": wts_updates[24932]})
    checks_def.append({"type": "upgrade", "id": "R0EZ", "field": "name1", "expected": wts_updates[24838]})
    checks_def.append({"type": "upgrade", "id": "R0EZ", "field": "tip1", "expected": wts_updates[24840]})
    checks_def.append({"type": "upgrade", "id": "R0EZ", "field": "ubertip1", "expected": wts_updates[24867]})
    checks_def.append({"type": "upgrade", "id": "R0F1", "field": "name1", "expected": wts_updates[27941]})
    checks_def.append({"type": "upgrade", "id": "R0F1", "field": "tip1", "expected": wts_updates[28001]})
    checks_def.append({"type": "upgrade", "id": "R0F1", "field": "ubertip1", "expected": wts_updates[24857]})
    checks_def.append({"type": "upgrade", "id": "R0F0", "field": "name1", "expected": wts_updates[24851]})
    checks_def.append({"type": "upgrade", "id": "R0F0", "field": "tip1", "expected": wts_updates[24852]})
    checks_def.append({"type": "upgrade", "id": "R0F0", "field": "ubertip1", "expected": wts_updates[25986]})
    checks_def.append({"type": "upgrade", "id": "R0F2", "field": "name1", "expected": wts_updates[24858]})
    checks_def.append({"type": "upgrade", "id": "R0F2", "field": "tip1", "expected": wts_updates[24860]})
    checks_def.append({"type": "upgrade", "id": "R0F2", "field": "ubertip1", "expected": wts_updates[24862]})

    categories = {
        "selection": ["A121", "R0FX"],
        "buildings": [
            "h0IJ", "h0IK", "h0IL", "h0IM", "h0IN", "h0IO",
            "h0IP", "h0IQ", "h0IR", "h0IS", "h0JT"
        ],
        "worker": ["h0IT"],
        "units": [
            "h0IU", "h0IV", "h0IW", "h0IX", "h0IY",
            "h0IZ", "h0J0", "h0J1", "h0NA", "o02T"
        ],
        "heroes": ["H0J2", "H0J6", "H0J7", "H0J8"],
        "upgrades": [
            "R0FX", "R0EY", "R0EM", "R0EN", "R0EO", "R0EP", "R0EQ",
            "R0IP", "R0F6", "R0F5", "R0EZ", "R0F1", "R0F0", "R0F2"
        ],
        "abilities": [
            "A121", "A11I", "A11H", "A11J", "A11K",
            "A11L", "A11N", "A11M", "A11O",
            "A11Q", "A11P", "A11R", "A11S",
            "A11Z", "A11U", "A11T", "A120",
            "A11V", "A11W", "A11X", "A11Y",
            "A117", "A118", "A119", "A11A", "A11B", "A11C",
            "A11D", "A11E", "A1F0", "A1F1", "A0PE", "Adis"
        ],
        "buffs": ["B06A", "B06B", "B06C", "B06D"]
    }

    return wts_updates, checks_def, categories

if __name__ == "__main__":
    wts_updates, checks_def, categories = build_plan()
    print(f"Built plan: {len(wts_updates)} WTS updates, {len(checks_def)} checks.")
