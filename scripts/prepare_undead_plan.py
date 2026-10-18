# -*- coding: utf-8 -*-
"""Comprehensive plan preparation for Race 13: Нежить (Undead / Scourge) UI text standardization.

Generates docs/ui_text/undead_plan.json containing:
- wts_updates: dict mapping string_id -> new_standardized_value
- checks_def: verification definitions for HiveWE object inspection
- statistics and metadata
"""
import hashlib
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

wts_path = ROOT / "map.w3x/war3map.wts"
wts_content = wts_path.read_text(encoding="utf-8")

def check_wts_has(sid):
    pattern = rf"STRING 0*{sid}\s*\{{\s*\r?\n"
    return bool(re.search(pattern, wts_content))

wts_updates = {}
checks_def = []

# =========================================================================
# 1. SELECTION (A0HV)
# =========================================================================
wts_updates[38877] = "|cffe4cfa3Плеть|r"
wts_updates[38878] = "|cffe4cfa3Плеть|r (|cffffffffA|r)"
wts_updates[25783] = (
    "|cffa6afb8РАСА:|cffced4da Армия нежити под предводительством Короля-лича, несущая чуму и смерть всему живому на Азероте.|r|n|n"
    "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor|r|n"
    "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
    "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8●●|r|n"
    "|cffa6afb8Период:|r |cffa9c7de«Wrath of the Lich King»|r|n|n"
    "|cffced4daПлеть — одна из могущественнейших фракций нежити Азерота. Созданная изначально как предвестник вторжения Пылающего Легиона, "
    "Плеть освободилась от власти демонов и под железной волей ужасающего Короля-лича утвердила своё господство на ледяном континенте Нордскол, "
    "стремясь подчинить себе все народы мира.|r"
)

checks_def.append({"type": "ability", "id": "A0HV", "field": "name", "expected_sid": 38877})
checks_def.append({"type": "ability", "id": "A0HV", "field": "tip1", "expected_sid": 38878})
checks_def.append({"type": "ability", "id": "A0HV", "field": "ubertip1", "expected_sid": 25783})

# =========================================================================
# 2. BUILDINGS (13)
# =========================================================================

# n014: Некрополь (Q)
wts_updates[8527] = "|cffe4cfa3Некрополь|r"
wts_updates[1236] = "|cffe4cfa3Некрополь|r (|cffffffffQ|r)"
wts_updates[41914] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Главный оплот и центр сбора ресурсов Плети. Позволяет призывать послушников и складировать добытую древесину.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deПослушник|cffced4da: базовый рабочий, строитель и добытчик ресурсов.|n|n"
    "|cffa6afb8Улучшается до:|cffced4da|n"
    "- |cffa9c7deЧертоги мертвых|cffced4da: открывает новые постройки и войска.|r"
)

# u00F: Чертоги мертвых (Z)
wts_updates[8554] = "|cffe4cfa3Чертоги мертвых|r"
wts_updates[1234] = "|cffe4cfa3Чертоги мертвых|r (|cffffffffZ|r)"
wts_updates[41907] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Укреплённый оплот Плети (вторая ступень). Открывает доступ к Храму проклятых, Бойне и новым улучшениям.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deПослушник|cffced4da: базовый рабочий, строитель и добытчик ресурсов.|n|n"
    "|cffa6afb8Улучшается до:|cffced4da|n"
    "- |cffa9c7deТемная цитадель|cffced4da: высшая ступень оплота Плети.|r"
)

# u00G: Темная цитадель (Z)
wts_updates[8555] = "|cffe4cfa3Темная цитадель|r"
wts_updates[1235] = "|cffe4cfa3Темная цитадель|r (|cffffffffZ|r)"
wts_updates[41908] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Цитадель владык Плети (третья ступень). Открывает высшие технологии, Костяной завод и сильнейших воинов армии тьмы.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deПослушник|cffced4da: базовый рабочий, строитель и добытчик ресурсов.|r"
)

# u00H: Зиккурат (A)
wts_updates[8556] = "|cffe4cfa3Зиккурат|r"
wts_updates[12019] = "|cffe4cfa3Зиккурат|r (|cffffffffA|r)"
wts_updates[41909] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Опорное строение Плети. Обеспечивает базу припасами и приносит регулярный доход в казну. Может быть перестроено в оборонительную башню.|n|n"
    "|cffa6afb8Особенности:|cffced4da|n"
    "- Даёт |cffc8e087+40|cffced4da к доходу за выплату.|n|n"
    "|cffa6afb8Улучшается до:|cffced4da|n"
    "- |cffa9c7deБашня духов|cffced4da: сторожевая башня дальнего боя.|n"
    "- |cffa9c7deНерубская башня|cffced4da: леденящая башня, замедляющая врагов.|r"
)

# u00I: Башня духов (Z)
wts_updates[8557] = "|cffe4cfa3Башня духов|r"
wts_updates[40236] = "|cffe4cfa3Башня духов|r (|cffffffffZ|r)"
wts_updates[41910] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение Плети. Атакует наземные и воздушные цели быстрыми залпами духов.|n|n"
    "|cffa6afb8Особенности:|cffced4da|n"
    "- Снижает доход на |cffe69a8d40|cffced4da при улучшении из зиккурата.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# u00J: Нерубская башня (X)
wts_updates[8558] = "|cffe4cfa3Нерубская башня|r"
wts_updates[40237] = "|cffe4cfa3Нерубская башня|r (|cffffffffX|r)"
wts_updates[41911] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение нерубов. Атакует ледяными снарядами, замедляющими скорость атаки и передвижения целей.|n|n"
    "|cffa6afb8Особенности:|cffced4da|n"
    "- Снижает доход на |cffe69a8d40|cffced4da при улучшении из зиккурата.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# u00K: Алтарь тьмы (S)
wts_updates[8559] = "|cffe4cfa3Алтарь тьмы|r"
wts_updates[13004] = "|cffe4cfa3Алтарь тьмы|r (|cffffffffS|r)"
wts_updates[13016] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище тёмных сил. Позволяет призывать и воскрешать павших героев Плети.|n|n"
    "|cffa6afb8Герои:|cffced4da|n"
    "- |cffa9c7deРыцарь Смерти|cffced4da: предводитель нежити и мастер ближнего боя.|n"
    "- |cffa9c7deВладыка склепа|cffced4da: несокрушимый царь нерубов.|n"
    "- |cffa9c7deНекромант|cffced4da: повелитель мёртвых и чумной чародей.|r"
)

# u00L: Кладбище (E)
wts_updates[8560] = "|cffe4cfa3Кладбище|r"
wts_updates[13006] = "|cffe4cfa3Кладбище|r (|cffffffffE|r)"
wts_updates[41517] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Хранилище древесины и источник тел для армии нежити. Позволяет проводить исследования вооружения и защиты войск.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deУлучшенные инструменты|cffced4da: увеличивают сбор древесины.|n"
    "- |cffa9c7deНечестивая сила|cffced4da: усиливает атаку ближнего боя.|n"
    "- |cffa9c7deНечестивая броня|cffced4da: усиливает защиту ближнего боя.|n"
    "- |cffa9c7deАтаки чудовищ|cffced4da: усиливают атаку дальнего боя и чудовищ.|n"
    "- |cffa9c7deБроня чудовищ|cffced4da: усиливает броню дальнего боя и чудовищ.|n"
    "- |cffa9c7deУсугубить разложение|cffced4da: увеличивает урон ценой здоровья.|n"
    "- |cffa9c7deОстановить разложение|cffced4da: увеличивает здоровье ценой урона.|r"
)

# u00M: Бойня (D)
wts_updates[8561] = "|cffe4cfa3Бойня|r"
wts_updates[13007] = "|cffe4cfa3Бойня|r (|cffffffffD|r)"
wts_updates[41912] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Мастерская создания тяжёлых чудовищ и осадных механизмов Плети.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deПоганище|cffced4da: мощный штурмовой боец ближнего боя.|n"
    "- |cffa9c7deМясной фургон|cffced4da: дальнобойное осадное орудие и перевозчик тел.|n"
    "- |cffa9c7deОбсидиановая статуя|cffced4da: летающий страж поддержки.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deБолезнетворное облако|cffced4da: ядовитое заражение от атак.|n"
    "- |cffa9c7deЭксгумация|cffced4da: автоматическое производство тел фургонами.|r"
)

# u00N: Храм проклятых (R)
wts_updates[8562] = "|cffe4cfa3Храм проклятых|r"
wts_updates[12020] = "|cffe4cfa3Храм проклятых|r (|cffffffffR|r)"
wts_updates[41913] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель тёмных магов, алхимиков чумы и культистов Плети.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deНекромант|cffced4da: заклинатель, поднимающий скелетов из трупов.|n"
    "- |cffa9c7deБезумный ученый|cffced4da: алхимик чумы и ядовитых зелий.|n"
    "- |cffa9c7deСкелет-маг|cffced4da: боевой маг дальнего боя с огненными шарами.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deСделать некромантов адептами|cffced4da: открывает Нечестивое бешенство.|n"
    "- |cffa9c7deБезумная наука|cffced4da: усиливает безумных ученых.|n"
    "- |cffa9c7deИзучить магию смерти|cffced4da: усиливает скелетов-магов.|r"
)

# n012: Склеп (W)
wts_updates[8519] = "|cffe4cfa3Склеп|r"
wts_updates[12017] = "|cffe4cfa3Склеп|r (|cffffffffW|r)"
wts_updates[41832] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Основное военное сооружение Плети для подготовки передовых воинов.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deВурдалак|cffced4da: пехотинец ближнего боя и лесоруб.|n"
    "- |cffa9c7deГоргулья|cffced4da: летающий крылатый охотник.|n"
    "- |cffa9c7deНекроарахнид|cffced4da: стрелок дальнего боя с паутиной.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n"
    "- |cffa9c7deКаннибализм|cffced4da: поедание трупов для лечения.|n"
    "- |cffa9c7deЯрость вурдалака|cffced4da: повышает скорость атаки и бега.|n"
    "- |cffa9c7deПаутина|cffced4da: притягивает воздушных врагов к земле.|n"
    "- |cffa9c7deЗакопаться|cffced4da: скрытность под землёй с регенерацией.|r"
)

# u03B: Костяной завод (X)
wts_updates[2658] = "|cffe4cfa3Костяной завод|r"
wts_updates[8999] = "|cffe4cfa3Костяной завод|r (|cffffffffX|r)"
wts_updates[13000] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Место сборки и оживления колоссальных костяных созданий Плети.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n"
    "- |cffa9c7deЛедяной змей|cffced4da: могучий летающий дракон с леденящим дыханием.|r"
)

# u017: Алтарь перевоплощения (R)
wts_updates[9890] = "|cffe4cfa3Алтарь перевоплощения|r"
wts_updates[9891] = "|cffe4cfa3Алтарь перевоплощения|r (|cffffffffR|r)"
wts_updates[13021] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Жертвенный алтарь Плети для ритуалов тьмы. Позволяет приносить послушников в жертву, превращая их в невидимых теней-разведчиков.|r"
)

bld_checks = {
    'n014': (8527, 1236, 41914),
    'u00F': (8554, 1234, 41907),
    'u00G': (8555, 1235, 41908),
    'u00H': (8556, 12019, 41909),
    'u00I': (8557, 40236, 41910),
    'u00J': (8558, 40237, 41911),
    'u00K': (8559, 13004, 13016),
    'u00L': (8560, 13006, 41517),
    'u00M': (8561, 13007, 41912),
    'u00N': (8562, 12020, 41913),
    'n012': (8519, 12017, 41832),
    'u03B': (2658, 8999, 13000),
    'u017': (9890, 9891, 13021),
}
for bid, (nsid, tsid, usid) in bld_checks.items():
    checks_def.append({"type": "unit", "id": bid, "field": "name", "expected_sid": nsid})
    checks_def.append({"type": "unit", "id": bid, "field": "tip", "expected_sid": tsid})
    checks_def.append({"type": "unit", "id": bid, "field": "ubertip", "expected_sid": usid})

# =========================================================================
# 3. HEROES (7)
# =========================================================================

# U00O: Рыцарь Смерти (Z)
wts_updates[24784] = "|cffe4cfa3Рыцарь Смерти|r"
wts_updates[41834] = "|cffa9c7deОрбаз Кровопорч|r"
wts_updates[41841] = "|cffe4cfa3Рыцарь Смерти|r (|cffffffffZ|r)"
wts_updates[41840] = "|cffe4cfa3Рыцарь Смерти|r"
wts_updates[41842] = "|cffe4cfa3Рыцарь Смерти|r"
wts_updates[31686] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Тяжеловооружённый рыцарь тьмы и верховный предводитель войск Плети. Основная характеристика — |cffffffffсила|cffced4da.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЛик смерти|cffced4da: поражает врагов или исцеляет союзную нежить.|n"
    "- |cffa9c7deЗов смерти|cffced4da: временно увеличивает урон союзников вокруг.|n"
    "- |cffa9c7deНечистая аура|cffced4da: пассивно повышает скорость бега и исцеление.|n"
    "- |cffa9c7deОживление мертвых|cffced4da: поднимает неуязвимых воинов из трупов.|n|n"
    "Атакует наземные цели.|r"
)

# U00V: Владыка склепа (X)
wts_updates[9055] = "|cffe4cfa3Владыка склепа|r"
wts_updates[9058] = "|cffa9c7deФебис-Ра|r"
wts_updates[1237] = "|cffe4cfa3Владыка склепа|r (|cffffffffX|r)"
wts_updates[9056] = "|cffe4cfa3Владыка склепа|r"
wts_updates[9057] = "|cffe4cfa3Владыка склепа|r"
wts_updates[31687] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Могучий правитель нерубов, обращённый на службу Королю-личу. Основная характеристика — |cffffffffсила|cffced4da.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deПронзание|cffced4da: шипы подбрасывают и оглушают врагов на линии.|n"
    "- |cffa9c7deЖуки-падальщики|cffced4da: призывает рой жуков из трупов.|n"
    "- |cffa9c7deШипастый панцирь|cffced4da: повышает броню и отражает урон в ближнем бою.|n"
    "- |cffa9c7deРой саранчи|cffced4da: рой ранит врагов и исцеляет героя.|n|n"
    "Атакует наземные цели.|r"
)

# U00U: Некромант (C)
wts_updates[18652] = "|cffe4cfa3Некромант|r"
wts_updates[41829] = "|cffa9c7deНот Чумной|r"
wts_updates[15177] = "|cffe4cfa3Некромант|r (|cffffffffC|r)"
wts_updates[9001] = "|cffe4cfa3Некромант|r"
wts_updates[41839] = "|cffe4cfa3Некромант|r"
wts_updates[31685] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Искусный тёмный чародей и повелитель мертвецов. Основная характеристика — |cffffffffинтеллект|cffced4da.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deВоскрешение мертвых|cffced4da: поднимает воинов нежити из тел павших.|n"
    "- |cffa9c7deМорозный доспех|cffced4da: ледяной щит даёт броню и замедляет атакующих.|n"
    "- |cffa9c7deМассовое проклятие|cffced4da: проклинает толпу врагов, снижая точность.|n"
    "- |cffa9c7deСоздание Лоскутика|cffced4da: создает могучее чудовище Лоскутика.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# U030: Ануб`Арак (X)
wts_updates[40365] = "|cffe4cfa3Ануб'Арак|r"
wts_updates[25220] = "|cffa9c7deАнуб'Арак|r"
wts_updates[27913] = "|cffe4cfa3Ануб'Арак|r (|cffffffffX|r)"
wts_updates[25109] = "|cffe4cfa3Ануб'Арак|r"
wts_updates[25118] = "|cffe4cfa3Ануб'Арак|r"
wts_updates[29594] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный правитель Азжол-Неруба, павший в Войне Паука и воскрешённый служить Плети. Основная характеристика — |cffffffffсила|cffced4da.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deПодкоп|cffced4da: бросок под землёй с подбрасыванием врагов.|n"
    "- |cffa9c7deСмертельный союз|cffced4da: поглощает союзника для восстановления здоровья.|n"
    "- |cffa9c7deШипастый панцирь|cffced4da: даёт броню и отражает урон от силы героя.|n"
    "- |cffa9c7deРой саранчи|cffced4da: плотный рой наносит урон и лечит царя нерубов.|n|n"
    "Атакует наземные цели.|r"
)

# U014: Король-Лич (Q)
wts_updates[20994] = "|cffe4cfa3Король-Лич|r"
wts_updates[9111] = "|cffa9c7deАртас|r"
wts_updates[20993] = "|cffe4cfa3Король-Лич|r (|cffffffffQ|r)"
wts_updates[20990] = "|cffe4cfa3Король-Лич|r"
wts_updates[20991] = "|cffe4cfa3Король-Лич|r"
wts_updates[20992] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Верховный владыка Плети, слившийся с Ледяным Троном и Ледяной Скорбью. Основная характеристика — |cffffffffсила|cffced4da.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЛики смерти|cffced4da: град снарядов ранит врагов и лечит нежить в области.|n"
    "- |cffa9c7deНеистовство Ледяной Скорби|cffced4da: круговой ледяной взрыв с замедлением.|n"
    "- |cffa9c7deМощь Ледяной Скорби|cffced4da: шанс нанести десятикратный урон при атаке.|n"
    "- |cffa9c7deВоскрешение мертвых|cffced4da: поднимает десятки неуязвимых воинов из трупов.|n"
    "- |cffa9c7deПравосудие смерти|cffced4da: убитые враги переходят на сторону Плети.|n|n"
    "Атакует наземные цели.|r"
)

# CM00: Мертвый капитан Марвин (C)
wts_updates[1225] = "|cffe4cfa3Мертвый капитан|r"
wts_updates[1226] = "|cffa9c7deМарвин|r"
wts_updates[1227] = "|cffe4cfa3Мертвый капитан|r (|cffffffffC|r)"
wts_updates[1229] = "|cffe4cfa3Мертвый капитан|r"
wts_updates[1228] = "|cffe4cfa3Мертвый капитан|r"
wts_updates[40360] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Командир стражи Артаса, павший в Нордсколе и воскрешённый в виде верного слуги Трона.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЛик смерти|cffced4da: ранит живых врагов или исцеляет союзную нежить.|n"
    "- |cffa9c7deПеро под ребро|cffced4da: шанс нанести критический удар при атаке.|n"
    "- |cffa9c7deНечистая аура|cffced4da: повышает скорость бега и исцеление союзников.|n"
    "- |cffa9c7deОживление мертвых|cffced4da: временно поднимает неуязвимых воинов из трупов.|n|n"
    "Атакует наземные цели.|r"
)

# FL00: Мертвый капитан Фалрик (X)
wts_updates[701] = "|cffe4cfa3Мертвый капитан|r"
wts_updates[703] = "|cffa9c7deФалрик|r"
wts_updates[707] = "|cffe4cfa3Мертвый капитан|r (|cffffffffX|r)"
wts_updates[1224] = "|cffe4cfa3Мертвый капитан|r"
wts_updates[708] = "|cffe4cfa3Мертвый капитан|r"
wts_updates[40358] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Капитан королевской гвардии Лордерона, последовавший за Артасом до самого конца.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deСокрушительный удар|cffced4da: выпускает ударную волну по наземным врагам.|n"
    "- |cffa9c7deСильный удар|cffced4da: шанс оглушить врага и нанести дополнительный урон.|n"
    "- |cffa9c7deМертвый надзор|cffced4da: пассивно увеличивает урон союзных войск рядом.|n"
    "- |cffa9c7deАватар|cffced4da: даёт защиту, здоровье, урон и магический иммунитет.|n|n"
    "Атакует наземные цели.|r"
)

hero_checks = {
    'U00O': (24784, 41834, 41841, 31686, 41840, 41842),
    'U00V': (9055, 9058, 1237, 31687, 9056, 9057),
    'U00U': (18652, 41829, 15177, 31685, 9001, 41839),
    'U030': (40365, 25220, 27913, 29594, 25109, 25118),
    'U014': (20994, 9111, 20993, 20992, 20990, 20991),
    'CM00': (1225, 1226, 1227, 40360, 1229, 1228),
    'FL00': (701, 703, 707, 40358, 1224, 708),
}
for hid, (nsid, psid, tsid, usid, asid, rsid) in hero_checks.items():
    checks_def.append({"type": "unit", "id": hid, "field": "name", "expected_sid": nsid})
    checks_def.append({"type": "unit", "id": hid, "field": "propernames", "expected_sid": psid})
    checks_def.append({"type": "unit", "id": hid, "field": "tip", "expected_sid": tsid})
    checks_def.append({"type": "unit", "id": hid, "field": "ubertip", "expected_sid": usid})
    checks_def.append({"type": "unit", "id": hid, "field": "awakentip", "expected_sid": asid})
    checks_def.append({"type": "unit", "id": hid, "field": "revivetip", "expected_sid": rsid})

# =========================================================================
# 4. UNITS (18)
# =========================================================================

# u00P: Послушник (Q)
wts_updates[8530] = "|cffe4cfa3Послушник|r"
wts_updates[41915] = (
    "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий и культист Плети. Призывает и ремонтирует здания, собирает золото и служит жертвой для создания теней.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deРемонт|cffced4da: чинит здания и технику за счёт ресурсов.|n"
    "- |cffa9c7deРазвоплотить здание|cffced4da: возвращает часть ресурсов при разборке.|n|n"
    "Атакует наземные цели.|r"
)

# n011: Вурдалак (Q)
wts_updates[8517] = "|cffe4cfa3Вурдалак|r"
wts_updates[8675] = "|cffe4cfa3Вурдалак|r (|cffffffffQ|r)"
wts_updates[38398] = (
    "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец ближнего боя и сборщик древесины Плети.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n"
    "- |cffa9c7deКаннибализм|cffced4da: пожирает трупы для исцеления; требует исследования.|n"
    "- |cffa9c7deДобыча древесины|cffced4da: эффективно рубит лес.|n|n"
    "Атакует наземные цели.|r"
)

# n013: Горгулья (E)
wts_updates[30586] = "|cffe4cfa3Горгулья|r"
wts_updates[30604] = "|cffe4cfa3Горгулья|r (|cffffffffE|r)"
wts_updates[38399] = (
    "|cffa6afb8ЮНИТ:|cffced4da Летающий крылатый охотник дальнего боя.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deКаменная статуя|cffced4da: приземляется, ускоренно восстанавливая здоровье.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# u03E: Некроарахнид (W)
wts_updates[8520] = "|cffe4cfa3Некроарахнид|r"
wts_updates[33298] = "|cffe4cfa3Некроарахнид|r (|cffffffffW|r)"
wts_updates[42347] = (
    "|cffa6afb8ЮНИТ:|cffced4da Стрелок дальнего боя и воин поддержки Плети.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deПаутина|cffced4da: притягивает летающих врагов к земле; требует исследования.|n"
    "- |cffa9c7deЗакопаться|cffced4da: скрывается под землёй с регенерацией; требует исследования.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные цели.|r"
)

# u02B: Некроарахнид (E) (alternate)
wts_updates[3848] = "|cffe4cfa3Некроарахнид|r"
wts_updates[3849] = "|cffe4cfa3Некроарахнид|r (|cffffffffE|r)"
wts_updates[3954] = (
    "|cffa6afb8ЮНИТ:|cffced4da Стрелок дальнего боя и воин поддержки Плети.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deПаутина|cffced4da: притягивает летающих врагов к земле; требует исследования.|n"
    "- |cffa9c7deЗакопаться|cffced4da: скрывается под землёй с регенерацией; требует исследования.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные цели.|r"
)

# u00A: Поганище (E)
wts_updates[8523] = "|cffe4cfa3Поганище|r"
wts_updates[8607] = "|cffe4cfa3Поганище|r (|cffffffffE|r)"
wts_updates[38400] = (
    "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый штурмовой боец ближнего боя армии тьмы.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deБолезнетворное облако|cffced4da: отравляет окружающих врагов; требует исследования.|n"
    "- |cffa9c7deКаннибализм|cffced4da: пожирает трупы для исцеления; требует исследования.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные цели.|r"
)

# u00B: Мясной фургон (Q)
wts_updates[8524] = "|cffe4cfa3Мясной фургон|r"
wts_updates[8679] = "|cffe4cfa3Мясной фургон|r (|cffffffffQ|r)"
wts_updates[38401] = (
    "|cffa6afb8ЮНИТ:|cffced4da Дальнобойное осадное орудие и сборщик трупов для армии нежити.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deПогрузить труп|cffced4da: собирает тела павших воинов.|n"
    "- |cffa9c7deВыгрузить труп|cffced4da: выгружает собранные тела на поле боя.|n"
    "- |cffa9c7deЭксгумация|cffced4da: автоматически производит тела; требует исследования.|n"
    "- |cffa9c7deБолезнетворное облако|cffced4da: осадные снаряды заражают цели чумой; требует исследования.|n|n"
    "Атакует наземные цели и деревья.|r"
)

# u00D: Обсидиановая статуя (W)
wts_updates[8526] = "|cffe4cfa3Обсидиановая статуя|r"
wts_updates[8681] = "|cffe4cfa3Обсидиановая статуя|r (|cffffffffW|r)"
wts_updates[38403] = (
    "|cffa6afb8ЮНИТ:|cffced4da Оживлённый страж поддержки армии тьмы.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЧумная эссенция|cffced4da: периодически восстанавливает здоровье союзникам.|n"
    "- |cffa9c7deПризрачное касание|cffced4da: периодически восполняет ману заклинателям.|n"
    "- |cffa9c7deНевосприимчивость к магии|cffced4da: полная защита от способностей.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# u00C: Некромант (Q)
wts_updates[8525] = "|cffe4cfa3Некромант|r"
wts_updates[8680] = "|cffe4cfa3Некромант|r (|cffffffffQ|r)"
wts_updates[38402] = (
    "|cffa6afb8ЮНИТ:|cffced4da Заклинатель тёмных чар и повелитель мертвецов.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deВоскрешение мертвых|cffced4da: поднимает скелетов-воинов из трупов.|n"
    "- |cffa9c7deНечестивое бешенство|cffced4da: ускоряет атаку союзников ценой здоровья; требует исследования.|n"
    "- |cffa9c7deУвечье|cffced4da: замедляет скорость атаки и перемещения врага.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# u008: Безумный ученый (W)
wts_updates[31243] = "|cffe4cfa3Безумный ученый|r"
wts_updates[8682] = "|cffe4cfa3Безумный ученый|r (|cffffffffW|r)"
wts_updates[33326] = (
    "|cffa6afb8ЮНИТ:|cffced4da Неатакующий алхимик чумы и заклинатель поддержки.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЯдовитое вещество|cffced4da: призывает исцеляющий идол союзникам.|n"
    "- |cffa9c7deОтравление|cffced4da: отравляет и замедляет выбранного врага.|n"
    "- |cffa9c7deСбор слизи|cffced4da: рассеивает магические эффекты в области.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|r"
)

# u00E: Скелет-маг (E)
wts_updates[8568] = "|cffe4cfa3Скелет-маг|r"
wts_updates[8683] = "|cffe4cfa3Скелет-маг|r (|cffffffffE|r)"
wts_updates[41921] = (
    "|cffa6afb8ЮНИТ:|cffced4da Боевой скелет-чародей дальнего боя армии тьмы.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deОгненный шар|cffced4da: огненный снаряд, наносящий урон и оглушающий врага.|n"
    "- |cffa9c7deПорча|cffced4da: наносит периодический урон ядом.|n"
    "- |cffa9c7deПроклятие|cffced4da: заставляет атаки цели промахиваться.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# u034: Ледяной змей (Q)
wts_updates[39891] = "|cffe4cfa3Ледяной змей|r"
wts_updates[39892] = "|cffe4cfa3Ледяной змей|r (|cffffffffQ|r)"
wts_updates[42345] = (
    "|cffa6afb8ЮНИТ:|cffced4da Колоссальный летающий дракон-скелет армии Плети.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deЛеденящее дыхание|cffced4da: атаки замедляют врагов и выводят из строя здания; требует исследования.|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные и воздушные цели.|r"
)

# ft00: Скелет-воин
wts_updates[39427] = "|cffe4cfa3Скелет-воин|r"
wts_updates[3806] = "|cffe4cfa3Скелет-воин|r"

# ft01: Скелет-лучник
wts_updates[630] = "|cffe4cfa3Скелет-лучник|r"

# n07H: Скелет-орк
wts_updates[22330] = "|cffe4cfa3Скелет-орк|r"
wts_updates[12380] = "|cffe4cfa3Скелет-орк|r"
wts_updates[12381] = (
    "|cffa6afb8ЮНИТ:|cffced4da Призванный воин ближнего боя армии нежити.|n|n"
    "|cffa6afb8Способности:|cffced4da|n"
    "- |cffa9c7deРазложение трупа|cffced4da: характеристики изменяются ритуалами на кладбище.|n|n"
    "Атакует наземные цели.|r"
)

# u03D: Скелет-лучник
wts_updates[632] = "|cffe4cfa3Скелет-лучник|r"
wts_updates[637] = "|cffe4cfa3Скелет-лучник|r"

# n016: Вурдалак (alternate)
wts_updates[8684] = "|cffe4cfa3Вурдалак|r"

# n017: Хилой вурдалак (alternate)
wts_updates[12337] = "|cffe4cfa3Хилой вурдалак|r"

unit_checks = {
    'u00P': (8530, None, 41915),
    'n011': (8517, 8675, 38398),
    'n013': (30586, 30604, 38399),
    'u03E': (8520, 33298, 42347),
    'u02B': (3848, 3849, 3954),
    'u00A': (8523, 8607, 38400),
    'u00B': (8524, 8679, 38401),
    'u00D': (8526, 8681, 38403),
    'u00C': (8525, 8680, 38402),
    'u008': (31243, 8682, 33326),
    'u00E': (8568, 8683, 41921),
    'u034': (39891, 39892, 42345),
    'ft00': (39427, 3806, None),
    'n07H': (22330, 12380, 12381),
    'u03D': (632, 637, None),
    'n016': (8684, None, None),
    'n017': (12337, None, None),
}
for uid, (nsid, tsid, usid) in unit_checks.items():
    if nsid: checks_def.append({"type": "unit", "id": uid, "field": "name", "expected_sid": nsid})
    if tsid: checks_def.append({"type": "unit", "id": uid, "field": "tip", "expected_sid": tsid})
    if usid: checks_def.append({"type": "unit", "id": uid, "field": "ubertip", "expected_sid": usid})

# =========================================================================
# 5. RESEARCHES (18)
# =========================================================================

# R0DQ: Улучшенные инструменты (E) [6 уровней]
r0dq_names = [3216, 3217, 3218, 3219, 16877, 16891]
r0dq_tips = [3222, 3223, 3224, 3225, 20620, 20786]
r0dq_ubs = [21585, 21344, 21455, 21467, 21507, 21508]
for lvl in range(1, 7):
    bonus = 8 if lvl <= 4 else 5
    wts_updates[r0dq_names[lvl-1]] = f"|cffe4cfa3Улучшенные инструменты — уровень {lvl}|r"
    wts_updates[r0dq_tips[lvl-1]] = f"|cffe4cfa3Улучшенные инструменты — уровень {lvl}|r (|cffffffffE|r)"
    wts_updates[r0dq_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём древесины, переносимой рабочими и вурдалаками на |cffc8e087+{bonus}|cffced4da.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n"
        "- |cffa9c7deПослушник|cffced4da|n"
        "- |cffa9c7deВурдалак|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
    )

# R05I: Усугубить Разложение (X) [4 уровня]
r05i_names = [8706, 8707, 8714, 8715]
r05i_tips = [8708, 8709, 8716, 8717]
r05i_ubs = [29577, 29578, 29579, 29580]
for lvl in range(1, 5):
    wts_updates[r05i_names[lvl-1]] = f"|cffe4cfa3Усугубить Разложение — ступень {lvl}|r"
    wts_updates[r05i_tips[lvl-1]] = f"|cffe4cfa3Усугубить Разложение — ступень {lvl}|r (|cffffffffX|r)"
    wts_updates[r05i_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Ускоряет тление плоти нежити, увеличивая урон атак на |cffc8e087+4|cffced4da ценой снижения запаса здоровья на |cffe69a8d35|cffced4da.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n"
        "- Всех существ нежити со способностью «Разложение трупа».|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# R05J: Остановить разложение (Z) [4 уровня]
r05j_names = [8724, 8725, 8732, 8733]
r05j_tips = [8726, 8727, 8734, 8735]
r05j_ubs = [29581, 29582, 29583, 29584]
for lvl in range(1, 5):
    wts_updates[r05j_names[lvl-1]] = f"|cffe4cfa3Остановить разложение — ступень {lvl}|r"
    wts_updates[r05j_tips[lvl-1]] = f"|cffe4cfa3Остановить разложение — ступень {lvl}|r (|cffffffffZ|r)"
    wts_updates[r05j_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Замедляет распад мёртвой плоти, увеличивая запас здоровья на |cffc8e087+35|cffced4da ценой снижения урона на |cffe69a8d4|cffced4da.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n"
        "- Всех существ нежити со способностью «Разложение трупа».|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# R05N: Атаки чудовищ (W) [6 уровней]
r05n_names = [8844, 8845, 8846, 8849, 8848, 8847]
r05n_tips = [8850, 8851, 8852, 8856, 8855, 8854]
r05n_ubs = {1: 8853, 4: 8857, 5: 8858, 6: 8859}
for lvl in range(1, 7):
    wts_updates[r05n_names[lvl-1]] = f"|cffe4cfa3Атаки чудовищ — уровень {lvl}|r"
    wts_updates[r05n_tips[lvl-1]] = f"|cffe4cfa3Атаки чудовищ — уровень {lvl}|r (|cffffffffW|r)"
for lvl, sid in r05n_ubs.items():
    wts_updates[sid] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак чудовищ, стрелков и летающих созданий Плети.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n"
        "- |cffa9c7deНекроарахнид|cffced4da|n"
        "- |cffa9c7deГоргулья|cffced4da|n"
        "- |cffa9c7deОбсидиановая статуя|cffced4da|n"
        "- |cffa9c7deНекромант|cffced4da|n"
        "- |cffa9c7deБезумный ученый|cffced4da|n"
        "- |cffa9c7deСкелет-маг|cffced4da|n"
        "- |cffa9c7deЛедяной змей|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
    )

# R05O: Нечестивая сила (Q) [6 уровней]
r05o_names = [8877, 8876, 8874, 8875, 8873, 8872]
r05o_tips = [8880, 8879, 8878, 8883, 8882, 8881]
r05o_ubs = {4: 8884, 5: 8885, 6: 8886}
for lvl in range(1, 7):
    wts_updates[r05o_names[lvl-1]] = f"|cffe4cfa3Нечестивая сила — уровень {lvl}|r"
    wts_updates[r05o_tips[lvl-1]] = f"|cffe4cfa3Нечестивая сила — уровень {lvl}|r (|cffffffffQ|r)"
for lvl, sid in r05o_ubs.items():
    wts_updates[sid] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак бойцов ближнего боя и осадных фургонов Плети.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n"
        "- |cffa9c7deВурдалак|cffced4da|n"
        "- |cffa9c7deПоганище|cffced4da|n"
        "- |cffa9c7deМясной фургон|cffced4da|n"
        "- |cffa9c7deСкелет-воин|cffced4da|n"
        "- |cffa9c7deСкелет-орк|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
    )

# R05P: Броня чудовищ (S) [6 уровней]
r05p_names = [8887, 8888, 8889, 8892, 8891, 8890]
r05p_tips = [8895, 8894, 8893, 8898, 8897, 8896]
r05p_ubs = [5867, 5868, 5869, 558, 5859, 5860]
for lvl in range(1, 7):
    wts_updates[r05p_names[lvl-1]] = f"|cffe4cfa3Броня чудовищ — уровень {lvl}|r"
    wts_updates[r05p_tips[lvl-1]] = f"|cffe4cfa3Броня чудовищ — уровень {lvl}|r (|cffffffffS|r)"
    wts_updates[r05p_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает броню чудовищ, стрелков и летающих созданий Плети.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n"
        "- |cffa9c7deНекроарахнид|cffced4da|n"
        "- |cffa9c7deГоргулья|cffced4da|n"
        "- |cffa9c7deОбсидиановая статуя|cffced4da|n"
        "- |cffa9c7deНекромант|cffced4da|n"
        "- |cffa9c7deБезумный ученый|cffced4da|n"
        "- |cffa9c7deСкелет-маг|cffced4da|n"
        "- |cffa9c7deЛедяной змей|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
    )

# R05Q: Нечестивая броня (A) [6 уровней]
r05q_names = [8908, 8909, 8910, 8913, 8912, 8911]
r05q_tips = [8914, 8915, 8916, 8919, 8918, 8917]
r05q_ubs = [9709, 10748, 12064, 6453, 6454, 6455]
for lvl in range(1, 7):
    wts_updates[r05q_names[lvl-1]] = f"|cffe4cfa3Нечестивая броня — уровень {lvl}|r"
    wts_updates[r05q_tips[lvl-1]] = f"|cffe4cfa3Нечестивая броня — уровень {lvl}|r (|cffffffffA|r)"
    wts_updates[r05q_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает броню воинов ближнего боя армии нежити.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n"
        "- |cffa9c7deВурдалак|cffced4da|n"
        "- |cffa9c7deПоганище|cffced4da|n"
        "- |cffa9c7deСкелет-воин|cffced4da|n"
        "- |cffa9c7deСкелет-орк|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
    )

# R05L: Эксгумация (Z)
wts_updates[8759] = "|cffe4cfa3Эксгумация|r"
wts_updates[8760] = "|cffe4cfa3Эксгумация|r (|cffffffffZ|r)"
wts_updates[8761] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет мясным фургонам автоматически производить мёртвые тела через равные промежутки времени.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deМясной фургон|cffced4da.|r"
)

# R05H: Болезнетворное облако (X)
wts_updates[8705] = "|cffe4cfa3Болезнетворное облако|r"
wts_updates[8824] = "|cffe4cfa3Болезнетворное облако|r (|cffffffffX|r)"
wts_updates[13010] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Снаряды мясных фургонов и удары поганищ заражают живых врагов чумой, наносящей урон в секунду.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deПоганище|cffced4da|n"
    "- |cffa9c7deМясной фургон|cffced4da.|r"
)

# R05E: Сделать некромантов адептами (A)
wts_updates[8639] = "|cffe4cfa3Адепты некромантов|r"
wts_updates[8640] = "|cffe4cfa3Адепты некромантов|r"
wts_updates[8641] = "|cffe4cfa3Адепты некромантов|r (|cffffffffA|r)"
wts_updates[8642] = "|cffe4cfa3Адепты некромантов|r (|cffffffffA|r)"

# R05F: Изучить магию смерти (D)
wts_updates[8643] = "|cffe4cfa3Магия смерти|r"
wts_updates[8644] = "|cffe4cfa3Магия смерти|r"
wts_updates[8645] = "|cffe4cfa3Магия смерти|r (|cffffffffD|r)"
wts_updates[8646] = "|cffe4cfa3Магия смерти|r (|cffffffffD|r)"
wts_updates[8647] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает характеристики скелетов-магов, увеличивая их запас здоровья, маны и силу заклинаний.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deСкелет-маг|cffced4da.|r"
)
wts_updates[8648] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает характеристики скелетов-магов, увеличивая их запас здоровья, маны и силу заклинаний.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deСкелет-маг|cffced4da.|r"
)

# R05G: Безумная наука (S)
wts_updates[8657] = "|cffe4cfa3Безумная наука|r"
wts_updates[8658] = "|cffe4cfa3Безумная наука|r"
wts_updates[8659] = "|cffe4cfa3Безумная наука|r (|cffffffffS|r)"
wts_updates[8660] = "|cffe4cfa3Безумная наука|r (|cffffffffS|r)"
wts_updates[31439] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и скорость восстановления маны безумных ученых.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deБезумный ученый|cffced4da.|r"
)
wts_updates[39817] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и скорость восстановления маны безумных ученых.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deБезумный ученый|cffced4da.|r"
)

# R05A: Каннибализм (Z)
wts_updates[8628] = "|cffe4cfa3Каннибализм|r"
wts_updates[8629] = "|cffe4cfa3Каннибализм|r (|cffffffffZ|r)"
wts_updates[8630] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает вурдалаков и поганищ способности пожирать тела павших воинов для восстановления здоровья.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deВурдалак|cffced4da|n"
    "- |cffa9c7deПоганище|cffced4da.|r"
)

# R05R: Ярость вурдалака (A)
wts_updates[8929] = "|cffe4cfa3Ярость вурдалака|r"
wts_updates[8930] = "|cffe4cfa3Ярость вурдалака|r (|cffffffffA|r)"
wts_updates[9632] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки вурдалаков на |cffc8e087+35%|cffced4da и повышает скорость их передвижения.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deВурдалак|cffced4da.|r"
)

# R05D: Закопаться (X)
wts_updates[8638] = "|cffe4cfa3Закопаться|r"
wts_updates[8637] = "|cffe4cfa3Закопаться|r (|cffffffffX|r)"

# R05C: Паутина (S)
wts_updates[8634] = "|cffe4cfa3Паутина|r"
wts_updates[8635] = "|cffe4cfa3Паутина|r (|cffffffffS|r)"
wts_updates[8636] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает некроарахнидов опутывать воздушных противников паутиной, притягивая их к земле для наземных атак.|n|n"
    "|cffa6afb8Затрагивает:|cffced4da|n"
    "- |cffa9c7deНекроарахнид|cffced4da.|r"
)

# R07I: Плеть
wts_updates[10664] = "|cffe4cfa3Плеть|r"
wts_updates[10665] = "|cffe4cfa3Плеть|r"
wts_updates[20116] = "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Расовый маркер технологий Плети.|r"

# R0J5: Плеть или Культ проклятых
wts_updates[34715] = "|cffe4cfa3Плеть или Культ проклятых|r"
wts_updates[34716] = "|cffe4cfa3Плеть или Культ проклятых|r"
wts_updates[34717] = "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Расовый маркер фракций нежити.|r"

# =========================================================================
# 6. HERO ABILITIES
# =========================================================================

# A0CO: Лик смерти (Q) [4 уровня]
wts_updates[9006] = "|cffe4cfa3Лик смерти|r"
wts_updates[9007] = "|cffe4cfa3Лик смерти|r [|cffffffffуровень %d|r]"
wts_updates[15504] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит урон живому противнику или восполняет здоровье союзному существу нежити.|n|n"
    "|cffa6afb8Урон по врагу / лечение союзника:|cffced4da|n"
    "- Уровень 1: |cffffffff100|cffced4da урона / |cffc8e087200|cffced4da лечения.|n"
    "- Уровень 2: |cffffffff200|cffced4da урона / |cffc8e087400|cffced4da лечения.|n"
    "- Уровень 3: |cffffffff300|cffced4da урона / |cffc8e087600|cffced4da лечения.|n"
    "- Уровень 4: |cffffffff400|cffced4da урона / |cffc8e087800|cffced4da лечения.|r"
)
a0co_tips = [15505, 15506, 15507, 15502]
a0co_ubs = [15508, 15509, 15510, 15503]
a0co_dmg = [100, 200, 300, 400]
for lvl in range(1, 5):
    d = a0co_dmg[lvl-1]
    h = d * 2
    wts_updates[a0co_tips[lvl-1]] = f"|cffe4cfa3Лик смерти — уровень {lvl}|r (|cffffffffQ|r)"
    wts_updates[a0co_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff{d}|cffced4da урона живому противнику или восстанавливает |cffc8e087{h}|cffced4da здоровья союзной нежити.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0CP: Зов смерти (W) [4 уровня]
wts_updates[9010] = "|cffe4cfa3Зов смерти|r"
wts_updates[1267] = "|cffe4cfa3Зов смерти|r [|cffffffffуровень %d|r]"
wts_updates[15514] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Временно увеличивает урон атак находящихся рядом союзных войск.|n|n"
    "|cffa6afb8Бонус к урону:|cffced4da|n"
    "- Уровень 1: |cffc8e087+15%|cffced4da к урону.|n"
    "- Уровень 2: |cffc8e087+20%|cffced4da к урону.|n"
    "- Уровень 3: |cffc8e087+25%|cffced4da к урону.|n"
    "- Уровень 4: |cffc8e087+35%|cffced4da к урону.|r"
)
a0cp_tips = [9011, 9012, 9013, 9014]
a0cp_ubs = [15515, 15511, 15512, 15513]
a0cp_bonus = [15, 20, 25, 35]
for lvl in range(1, 5):
    b = a0cp_bonus[lvl-1]
    wts_updates[a0cp_tips[lvl-1]] = f"|cffe4cfa3Зов смерти — уровень {lvl}|r (|cffffffffW|r)"
    wts_updates[a0cp_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон окружающих союзных войск на |cffc8e087+{b}%|cffced4da.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0CR: Нечистая аура (E) [4 уровня]
wts_updates[9066] = "|cffe4cfa3Нечистая аура|r"
wts_updates[9067] = "|cffe4cfa3Нечистая аура|r [|cffffffffуровень %d|r]"
wts_updates[15523] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно ускоряет передвижение и регенерацию здоровья окружающих союзников.|n|n"
    "|cffa6afb8Параметры ауры:|cffced4da|n"
    "- Уровень 1: |cffc8e087+10%|cffced4da к скорости бега, |cffc8e087+0.5|cffced4da здоровья/сек.|n"
    "- Уровень 2: |cffc8e087+15%|cffced4da к скорости бега, |cffc8e087+1.0|cffced4da здоровья/сек.|n"
    "- Уровень 3: |cffc8e087+20%|cffced4da к скорости бега, |cffc8e087+1.5|cffced4da здоровья/сек.|n"
    "- Уровень 4: |cffc8e087+25%|cffced4da к скорости бега, |cffc8e087+2.0|cffced4da здоровья/сек.|r"
)
a0cr_tips = [9070, 9071, 9072, 9068]
a0cr_ubs = [15520, 15521, 15522, 15519]
a0cr_spd = [10, 15, 20, 25]
for lvl in range(1, 5):
    s = a0cr_spd[lvl-1]
    wts_updates[a0cr_tips[lvl-1]] = f"|cffe4cfa3Нечистая аура — уровень {lvl}|r"
    wts_updates[a0cr_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение союзников рядом на |cffc8e087+{s}%|cffced4da и повышает скорость регенерации здоровья.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0CN: Оживление мертвых (R) [2 уровня]
wts_updates[8992] = "|cffe4cfa3Оживление мертвых|r"
wts_updates[8993] = "|cffe4cfa3Оживление мертвых|r [|cffffffffуровень %d|r]"
wts_updates[15500] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает из трупов в выбранной области неуязвимых воинов, сражающихся на стороне героя в течение ограниченного времени.|n|n"
    "- Уровень 1: воскрешает |cffffffff8|cffced4da трупов.|n"
    "- Уровень 2: воскрешает |cffffffff12|cffced4da трупов.|r"
)
wts_updates[8994] = "|cffe4cfa3Оживление мертвых — уровень 1|r (|cffffffffR|r)"
wts_updates[13587] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает |cffffffff8|cffced4da неуязвимых воинов из трупов в области действия на ограниченное время.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
)
wts_updates[8995] = "|cffe4cfa3Оживление мертвых — уровень 2|r (|cffffffffR|r)"
wts_updates[13547] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает |cffffffff12|cffced4da неуязвимых воинов из трупов в области действия на ограниченное время.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
)

# AQ95: Рой саранчи (R) [2 уровня]
wts_updates[41933] = "|cffe4cfa3Рой саранчи — уровень 2|r (|cffffffffR|r)"
wts_updates[41934] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает свирепый рой саранчи, который атакует окружающих врагов и передаёт похищенное здоровье герою.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
)

# UN99: Шипастый панцирь (E) [4 уровня]
wts_updates[35526] = "|cffe4cfa3Шипастый панцирь — уровень 4|r"
wts_updates[35527] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно укрепляет панцирь шипами, повышая броню на |cffc8e087+13|cffced4da и отражая |cffc8e08745%|cffced4da входящего урона ближнего боя во врагов.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
)

# A0CS: Пронзание (Q) [4 уровня]
wts_updates[9073] = "|cffe4cfa3Пронзание|r"
wts_updates[9074] = "|cffe4cfa3Пронзание|r [|cffffffffуровень %d|r]"
wts_updates[14093] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает шипы из-под земли на прямой линии, нанося урон наземным врагам и подбрасывая их в воздух с оглушением.|n|n"
    "|cffa6afb8Параметры удара:|cffced4da|n"
    "- Уровень 1: |cffffffff50|cffced4da урона, |cffffffff1.0|cffced4da сек. оглушения.|n"
    "- Уровень 2: |cffffffff80|cffced4da урона, |cffffffff1.5|cffced4da сек. оглушения.|n"
    "- Уровень 3: |cffffffff110|cffced4da урона, |cffffffff2.0|cffced4da сек. оглушения.|n"
    "- Уровень 4: |cffffffff140|cffced4da урона, |cffffffff2.4|cffced4da сек. оглушения.|r"
)
a0cs_tips = [9075, 9076, 9077, 9078]
a0cs_ubs = [14889, 15034, 15056, 21830]
a0cs_data = [(50, "1.0"), (80, "1.5"), (110, "2.0"), (140, "2.4")]
for lvl in range(1, 5):
    dmg, stun = a0cs_data[lvl-1]
    wts_updates[a0cs_tips[lvl-1]] = f"|cffe4cfa3Пронзание — уровень {lvl}|r (|cffffffffQ|r)"
    wts_updates[a0cs_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает шипы на прямой линии, нанося |cffffffff{dmg}|cffced4da урона и оглушая врагов на |cffffffff{stun}|cffced4da сек.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0CK: Воскрешение мертвых (Q) [4 уровня]
wts_updates[8939] = "|cffe4cfa3Воскрешение мертвых|r"
wts_updates[20090] = "|cffe4cfa3Воскрешение мертвых|r [|cffffffffуровень %d|r]"
wts_updates[15484] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает из трупов верных слуг нежити на службу Королю-личу.|n|n"
    "- Уровень 1: призывает |cffa9c7deСкелета-воина|cffced4da.|n"
    "- Уровень 2: призывает |cffa9c7deВурдалака|cffced4da.|n"
    "- Уровень 3: призывает |cffa9c7deПоганище|cffced4da.|n"
    "- Уровень 4: призывает |cffa9c7deРыцаря Смерти|cffced4da.|r"
)
a0ck_tips = [8940, 8965, 15107, 15108]
a0ck_ubs = [15480, 15481, 15482, 15483]
a0ck_units = ["Скелета-воина", "Вурдалака", "Поганище", "Рыцаря Смерти"]
for lvl in range(1, 5):
    u = a0ck_units[lvl-1]
    wts_updates[a0ck_tips[lvl-1]] = f"|cffe4cfa3Воскрешение мертвых — уровень {lvl}|r (|cffffffffQ|r)"
    wts_updates[a0ck_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает из трупа |cffa9c7de{u}|cffced4da.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0CM: Массовое проклятие (E) [4 уровня]
wts_updates[8971] = "|cffe4cfa3Массовое проклятие|r"
wts_updates[41279] = "|cffe4cfa3Массовое проклятие|r [|cffffffffуровень %d|r]"
wts_updates[41305] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает врагов вокруг героя, нанося мгновенный урон и заставляя их атаки промахиваться.|n|n"
    "- Уровень 1: |cffffffff100|cffced4da урона.|n"
    "- Уровень 2: |cffffffff150|cffced4da урона.|n"
    "- Уровень 3: |cffffffff200|cffced4da урона.|n"
    "- Уровень 4: |cffffffff250|cffced4da урона.|r"
)
a0cm_tips = [8972, 8973, 8974, 8975]
a0cm_ubs = [41290, 41291, 41292, 41293]
a0cm_dmg = [100, 150, 200, 250]
for lvl in range(1, 5):
    d = a0cm_dmg[lvl-1]
    wts_updates[a0cm_tips[lvl-1]] = f"|cffe4cfa3Массовое проклятие — уровень {lvl}|r (|cffffffffE|r)"
    wts_updates[a0cm_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает всех окружающих противников, нанося |cffffffff{d}|cffced4da урона и вызывая промахи при атаке.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0BW: Создание Лоскутика (R) [2 уровня]
wts_updates[41617] = "|cffe4cfa3Создание Лоскутика|r"
wts_updates[41665] = "|cffe4cfa3Создание Лоскутика|r [|cffffffffуровень %d|r]"
wts_updates[41716] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создает совершенное чудовище Плети — гигантское поганище Лоскутика («воплощение войны»).|n|n"
    "Лоскутик обладает колоссальным запасом здоровья и наносит сокрушительный урон в ближнем бою.|r"
)
wts_updates[41843] = "|cffe4cfa3Создание Лоскутика — уровень 1|r (|cffffffffR|r)"
wts_updates[41844] = "|cffe4cfa3Создание Лоскутика — уровень 2|r (|cffffffffR|r)"
wts_updates[41739] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает колоссальное поганище Лоскутика на поле боя.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
)
wts_updates[41628] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает усиленное поганище Лоскутика с повышенным здоровьем и уроном.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
)

# A1LI: Подкоп (Q) [4 уровня]
wts_updates[30949] = "|cffe4cfa3Подкоп|r"
wts_updates[32930] = "|cffe4cfa3Подкоп|r [|cffffffffуровень %d|r]"
wts_updates[36134] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ануб'арак погружается под землю и совершает стремительный рывок к цели, подбрасывая всех врагов на пути.|n|n"
    "Урон зависит от силы героя:|n"
    "- Уровень 1: |cffffffff1.2|cffced4da * силу + |cffffffff50|cffced4da урона.|n"
    "- Уровень 2: |cffffffff2.4|cffced4da * силу + |cffffffff100|cffced4da урона.|n"
    "- Уровень 3: |cffffffff3.6|cffced4da * силу + |cffffffff150|cffced4da урона.|n"
    "- Уровень 4: |cffffffff4.8|cffced4da * силу + |cffffffff150|cffced4da урона.|r"
)
a1li_tips = [33507, 34354, 34687, 38108]
a1li_ubs = [36889, 37032, 38107, 38658]
a1li_mult = [("1.2", 50), ("2.4", 100), ("3.6", 150), ("4.8", 150)]
for lvl in range(1, 5):
    m, b = a1li_mult[lvl-1]
    wts_updates[a1li_tips[lvl-1]] = f"|cffe4cfa3Подкоп — уровень {lvl}|r (|cffffffffQ|r)"
    wts_updates[a1li_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Рывок под землёй, подбрасывающий врагов и наносящий |cffffffff{m}|cffced4da * силу + |cffffffff{b}|cffced4da урона.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A1LJ: Шипастый панцирь (E) [4 уровня]
wts_updates[38827] = "|cffe4cfa3Шипастый панцирь|r"
wts_updates[38828] = "|cffe4cfa3Шипастый панцирь|r [|cffffffffуровень %d|r]"
a1lj_tips = [38845, 38847, 38848, 38800]
a1lj_ubs = [38960, 38961, 38962, 38959]
a1lj_arm = [4, 7, 10, 13]
for lvl in range(1, 5):
    arm = a1lj_arm[lvl-1]
    wts_updates[a1lj_tips[lvl-1]] = f"|cffe4cfa3Шипастый панцирь — уровень {lvl}|r"
    wts_updates[a1lj_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffc8e087+{arm}|cffced4da к броне и отражает урон в ближнем бою во врагов в размере |cffffffff0.5|cffced4da * силу героя.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A1LL: Смертельный союз (W) [4 уровня]
wts_updates[38932] = "|cffe4cfa3Смертельный союз|r"
wts_updates[38933] = "|cffe4cfa3Смертельный союз|r [|cffffffffуровень %d|r]"
a1ll_tips = [38934, 38935, 38936, 38937]
a1ll_ubs = [38939, 38940, 38941, 38938]
for lvl in range(1, 5):
    wts_updates[a1ll_tips[lvl-1]] = f"|cffe4cfa3Смертельный союз — уровень {lvl}|r (|cffffffffW|r)"
    wts_updates[a1ll_ubs[lvl-1]] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Уничтожает выбранного союзника-нежить, восполняя здоровье Ануб'арака пропорционально запасу здоровья жертвы.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A1LM: Рой саранчи (R) [2 уровня]
wts_updates[38945] = "|cffe4cfa3Рой саранчи|r"
wts_updates[38946] = "|cffe4cfa3Рой саранчи|r [|cffffffffуровень %d|r]"
wts_updates[38947] = "|cffe4cfa3Рой саранчи — уровень 1|r (|cffffffffR|r)"
wts_updates[38942] = "|cffe4cfa3Рой саранчи — уровень 2|r (|cffffffffR|r)"
wts_updates[38943] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает рой саранчи, который непрерывно атакует врагов вокруг и передаёт высосанное здоровье Ануб'араку.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
)

# A1LK: Аура Ануб'арака
wts_updates[39640] = "|cffe4cfa3Аура склепа|r"
wts_updates[39639] = "|cffe4cfa3Аура склепа|r"
wts_updates[39641] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная аура царя нерубов, поддерживающая окружающие войска.|r"

# A0WD: Лики смерти (Q) [4 уровня]
wts_updates[21846] = "|cffe4cfa3Лики смерти|r"
wts_updates[15316] = "|cffe4cfa3Лики смерти|r [|cffffffffуровень %d|r]"
wts_updates[19730] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает всех юнитов в указанной области градом ликов смерти, раня живых врагов и исцеляя союзную нежить.|r"
)
a0wd_tips = [21831, 21832, 21833, 21834]
a0wd_ubs = [15584, 19726, 19727, 19728]
for lvl in range(1, 5):
    wts_updates[a0wd_tips[lvl-1]] = f"|cffe4cfa3Лики смерти — уровень {lvl}|r (|cffffffffQ|r)"
    wts_updates[a0wd_ubs[lvl-1]] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает лики смерти по всем юнитам в выбранной области, раня врагов и исцеляя дружественную нежить.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0CX: Мощь Ледяной Скорби (E) [4 уровня]
wts_updates[41306] = "|cffe4cfa3Мощь Ледяной Скорби|r"
wts_updates[41360] = "|cffe4cfa3Мощь Ледяной Скорби|r [|cffffffffуровень %d|r]"
wts_updates[21838] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс нанести сокрушительный десятикратный урон при атаке.|n|n"
    "- Уровень 1: |cffffffff5%|cffced4da шанс, |cffffffff10-кратный|cffced4da урон.|n"
    "- Уровень 2: |cffffffff7%|cffced4da шанс, |cffffffff10-кратный|cffced4da урон.|n"
    "- Уровень 3: |cffffffff9%|cffced4da шанс, |cffffffff10-кратный|cffced4da урон.|n"
    "- Уровень 4: |cffffffff11%|cffced4da шанс, |cffffffff10-кратный|cffced4da урон.|r"
)
a0cx_tips = [21014, 21015, 21016, 21017]
a0cx_chances = [5, 7, 9, 11]
for lvl in range(1, 5):
    c = a0cx_chances[lvl-1]
    wts_updates[a0cx_tips[lvl-1]] = f"|cffe4cfa3Мощь Ледяной Скорби — уровень {lvl}|r"
wts_updates[6389] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff11%|cffced4da шанс нанести |cffffffff10-кратный|cffced4da урон при атаке.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
)

# A0WE: Неистовство Ледяной Скорби (W) [4 уровня]
wts_updates[41246] = "|cffe4cfa3Неистовство Ледяной Скорби|r"
wts_updates[41407] = "|cffe4cfa3Неистовство Ледяной Скорби|r [|cffffffffуровень %d|r]"
wts_updates[23357] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит урон и замедляет противников в радиусе вокруг Короля-лича.|n|n"
    "- Уровень 1: |cffffffff125|cffced4da урона.|n"
    "- Уровень 2: |cffffffff175|cffced4da урона.|n"
    "- Уровень 3: |cffffffff250|cffced4da урона.|n"
    "- Уровень 4: |cffffffff350|cffced4da урона.|r"
)
a0we_tips = [41241, 41247, 41248, 41251]
a0we_ubs = [23353, 23354, 23355, 23356]
a0we_dmg = [125, 175, 250, 350]
for lvl in range(1, 5):
    d = a0we_dmg[lvl-1]
    wts_updates[a0we_tips[lvl-1]] = f"|cffe4cfa3Неистовство Ледяной Скорби — уровень {lvl}|r (|cffffffffW|r)"
    wts_updates[a0we_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff{d}|cffced4da урона всем противникам поблизости и замедляет их.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A0CZ: Воскрешение мертвых (R) [2 уровня]
wts_updates[39443] = "|cffe4cfa3Воскрешение мертвых|r"
wts_updates[41405] = "|cffe4cfa3Воскрешение мертвых|r [|cffffffffуровень %d|r]"
wts_updates[41438] = "|cffe4cfa3Воскрешение мертвых — уровень 1|r (|cffffffffR|r)"
wts_updates[41471] = "|cffe4cfa3Воскрешение мертвых — уровень 2|r (|cffffffffR|r)"
wts_updates[41239] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оживляет |cffffffff10|cffced4da неуязвимых мертвецов в радиусе 1500.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
)
wts_updates[41238] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оживляет |cffffffff25|cffced4da неуязвимых мертвецов в радиусе 1500.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
)

# A0WB: Правосудие смерти (passive)
wts_updates[39497] = "|cffe4cfa3Правосудие смерти|r"
wts_updates[39498] = "|cffe4cfa3Правосудие смерти|r"
wts_updates[20999] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Убитые Королём-личом органические существа после гибели восстают на его стороне.|r"
)
for sid in [7837, 7838, 7839, 7840, 7848]:
    wts_updates[sid] = "|cffe4cfa3Правосудие смерти|r"
for sid in [10057, 10658, 10863, 10866, 10420]:
    wts_updates[sid] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Убитые Королём-личом органические существа после гибели восстают на его стороне.|r"
    )

# A0WC: Дамми гальванизация
wts_updates[21011] = "|cffe4cfa3Гальванизация|r"
wts_updates[21010] = "|cffe4cfa3Гальванизация|r"

# CM01: Лик смерти Марвина [4 уровня]
wts_updates[40147] = "|cffe4cfa3Лик смерти — уровень 4|r (|cffffffffQ|r)"
cm01_ubs = [40048, 40151, 40152, 40148]
cm01_dmg = [100, 150, 200, 250]
for lvl in range(1, 5):
    d = cm01_dmg[lvl-1]
    wts_updates[cm01_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет |cffc8e087{d}|cffced4da здоровья союзной нежити или наносит вдвое меньший урон живому врагу.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# CM02: Оживление мертвых Марвина [2 уровня]
wts_updates[39677] = "|cffe4cfa3Оживление мертвых — уровень 2|r (|cffffffffR|r)"
wts_updates[40085] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оживляет |cffffffff12|cffced4da трупов в области действия на ограниченное время.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
)

# CM04: Перо под ребро Марвина [4 уровня]
wts_updates[40094] = "|cffe4cfa3Перо под ребро|r"
wts_updates[40095] = "|cffe4cfa3Перо под ребро — уровень 4|r"
cm04_ubs = [40156, 10426, 9201, 5371]
cm04_chances = [5, 8, 11, 14]
for lvl in range(1, 5):
    c = cm04_chances[lvl-1]
    wts_updates[cm04_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff{c}%|cffced4da шанс нанести |cffffffff2-кратный|cffced4da урон при атаке.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# CM05: Нечистая аура Марвина [4 уровня]
wts_updates[27412] = "|cffe4cfa3Нечистая аура — уровень 4|r"
cm05_ubs = [40402, 40403, 40519, 35536]
cm05_spds = [5, 10, 15, 20]
for lvl in range(1, 5):
    s = cm05_spds[lvl-1]
    wts_updates[cm05_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение союзников рядом на |cffc8e087+{s}%|cffced4da и повышает скорость регенерации здоровья.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# FL01: Сильный удар Фалрика [4 уровня]
wts_updates[40067] = "|cffe4cfa3Сильный удар|r"
wts_updates[40132] = "|cffe4cfa3Сильный удар — уровень 4|r (|cffffffffW|r)"
fl01_ubs = [40134, 40133, 40169, 26399]
fl01_data = [(15, 15), (20, 20), (30, 25), (35, 30)]
for lvl in range(1, 5):
    ch, dmg = fl01_data[lvl-1]
    wts_updates[fl01_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff{ch}%|cffced4da атака наносит на |cffffffff{dmg}|cffced4da больше урона и оглушает цель.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# FL02: Аватар Фалрика [2 уровня]
wts_updates[40118] = "|cffe4cfa3Аватар|r"
wts_updates[40136] = "|cffe4cfa3Аватар — уровень 2|r (|cffffffffR|r)"
wts_updates[40070] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет Фалрика защитой, повышая броню, здоровье, урон и давая невосприимчивость к магии.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
)
wts_updates[40137] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт Фалрику |cffc8e087+10|cffced4da к броне, |cffc8e087+750|cffced4da к здоровью, |cffc8e087+30|cffced4da к урону и невосприимчивость к магии.|n|n"
    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
)

# FL03: Сокрушительный удар Фалрика [4 уровня]
wts_updates[40072] = "|cffe4cfa3Сокрушительный удар|r"
wts_updates[40138] = "|cffe4cfa3Сокрушительный удар — уровень 4|r (|cffffffffQ|r)"
fl03_ubs = [40143, 40142, 40140, 40139]
fl03_dmg = [100, 150, 200, 250]
for lvl in range(1, 5):
    d = fl03_dmg[lvl-1]
    wts_updates[fl03_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну энергии, наносящую |cffffffff{d}|cffced4da урона наземным противникам на прямой линии.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# FL04: Мертвый надзор Фалрика [4 уровня]
wts_updates[40174] = "|cffe4cfa3Мертвый надзор|r"
wts_updates[40180] = "|cffe4cfa3Мертвый надзор|r [|cffffffffуровень %d|r]"
wts_updates[40179] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон от всех атак окружающих союзников.|r"
fl04_tips = [40181, 40182, 40178, 40175]
fl04_ubs = [40183, 3594, 40177, 40176]
fl04_bonus = [3, 6, 9, 12]
for lvl in range(1, 5):
    b = fl04_bonus[lvl-1]
    wts_updates[fl04_tips[lvl-1]] = f"|cffe4cfa3Мертвый надзор — уровень {lvl}|r"
    wts_updates[fl04_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзников поблизости на |cffc8e087+{b}%|cffced4da.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# =========================================================================
# 7. UNIT ABILITIES
# =========================================================================

# A0BO: Разложение трупа
wts_updates[8588] = "|cffe4cfa3Разложение трупа|r"
wts_updates[8589] = "|cffe4cfa3Разложение трупа|r"
wts_updates[8590] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Базовые параметры тления плоти нежити. С помощью ритуалов на кладбище можно усугубить разложение "
    "(повышая урон ценой здоровья) или остановить его (повышая здоровье ценой урона).|r"
)

# A0BP: Каннибализм
wts_updates[8592] = "|cffe4cfa3Каннибализм|r"
wts_updates[8593] = "|cffe4cfa3Каннибализм|r (|cffffffffQ|r)"

# A0C5: Болезнетворное облако
wts_updates[8670] = "|cffe4cfa3Болезнетворное облако|r"
wts_updates[8671] = "|cffe4cfa3Болезнетворное облако|r"

# A0C7: Болезнетворное облако (фургон)
wts_updates[8688] = "|cffe4cfa3Болезнетворное облако|r"
wts_updates[8689] = "|cffe4cfa3Болезнетворное облако|r"

# A0C8: Эксгумация (фургон)
wts_updates[8690] = "|cffe4cfa3Эксгумация|r"
wts_updates[8691] = "|cffe4cfa3Эксгумация|r"

# A0BT: Воскрешение мертвых (некромант)
wts_updates[8602] = "|cffe4cfa3Воскрешение мертвых|r"
wts_updates[8601] = "|cffe4cfa3Воскрешение мертвых|r (|cffffffffQ|r)"
wts_updates[8936] = "|cffe4cfa3Воскрешение мертвых — уровень 2|r (|cffffffffQ|r)"
wts_updates[22351] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает скелета-воина из трупа павшего бойца.|r"
)
wts_updates[22473] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает двух скелетов-воинов из трупов павших бойцов.|r"
)
wts_updates[12805] = "|cffe4cfa3Воскрешение мертвых|r"
wts_updates[13453] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Автоматически поднимает скелетов из доступных трупов.|r"

# A0BU: Нечестивое бешенство (некромант)
wts_updates[8603] = "|cffe4cfa3Нечестивое бешенство|r"
wts_updates[8604] = "|cffe4cfa3Нечестивое бешенство|r (|cffffffffW|r)"

# A1PV: Увечье (некромант)
wts_updates[17792] = "|cffe4cfa3Увечье|r"
wts_updates[20363] = "|cffe4cfa3Увечье|r (|cffffffffE|r)"
wts_updates[2596] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки и скорость передвижения выбранного врага.|r"
)

# A0C4: Невосприимчивость к магии
wts_updates[8668] = "|cffe4cfa3Невосприимчивость к магии|r"
wts_updates[8669] = "|cffe4cfa3Невосприимчивость к магии|r"

# Arpl: Чумная эссенция (статуя)
wts_updates[1244] = "|cffe4cfa3Чумная эссенция|r"
wts_updates[1245] = "|cffe4cfa3Чумная эссенция|r (|cffffffffQ|r)"

# Arpm: Призрачное касание (статуя)
wts_updates[1242] = "|cffe4cfa3Призрачное касание|r"
wts_updates[1243] = "|cffe4cfa3Призрачное касание|r (|cffffffffW|r)"

# A0BX: Порча (скелет-маг)
wts_updates[8610] = "|cffe4cfa3Порча|r"
wts_updates[8611] = "|cffe4cfa3Порча|r"
wts_updates[33330] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отравляет цель ядом, нанося |cffffffff5|cffced4da урона в секунду в течение |cffffffff25|cffced4da сек.|r"
)

# unA5: Проклятие (скелет-маг)
wts_updates[40320] = "|cffe4cfa3Проклятие|r"
wts_updates[40321] = "|cffe4cfa3Проклятие|r (|cffffffffQ|r)"

# A1PY: Огненный шар (скелет-маг)
wts_updates[41762] = "|cffe4cfa3Огненный шар|r"
wts_updates[41756] = "|cffe4cfa3Огненный шар|r (|cffffffffW|r)"
wts_updates[41777] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает огненный шар, наносящий |cffffffff100|cffced4da урона и оглушающий цель.|r"
)

# A0C0: Ядовитое вещество (ученый)
wts_updates[8618] = "|cffe4cfa3Ядовитое вещество|r"
wts_updates[8619] = "|cffe4cfa3Ядовитое вещество|r (|cffffffffQ|r)"
wts_updates[20572] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает целебный идол, восстанавливающий окружающим союзникам |cffc8e0871.5%|cffced4da здоровья в секунду.|r"
)

# A0C2: Отравление (ученый)
wts_updates[8651] = "|cffe4cfa3Отравление|r"
wts_updates[8652] = "|cffe4cfa3Отравление|r"
wts_updates[8686] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Яд отравляет и существенно замедляет вражескую цель.|r"
)

# A1PX: Сбор слизи (ученый)
wts_updates[22599] = "|cffe4cfa3Сбор слизи|r"
wts_updates[41075] = "|cffe4cfa3Сбор слизи|r (|cffffffffW|r)"
wts_updates[40062] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает магические эффекты, действующие на войска в выбранной области.|r"
)

# unA0: Леденящее дыхание (ледяной змей)
wts_updates[33334] = "|cffe4cfa3Леденящее дыхание|r"
wts_updates[33338] = "|cffe4cfa3Леденящее дыхание|r (|cffffffffZ|r)"
wts_updates[16400] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Леденящее дыхание замедляет атаки и передвижение врагов, а также замораживает вражеские постройки.|r"
)

# A1N8: Закопаться (некроарахнид)
wts_updates[8596] = "|cffe4cfa3Закопаться|r"
wts_updates[8597] = "|cffe4cfa3Закопаться|r (|cffffffffW|r)"
wts_updates[39903] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Некроарахнид зарывается под землю, становясь невидимым и ускоренно восстанавливая здоровье.|n|n"
    "Закопавшийся арахнид не может атаковать. При критическом падении здоровья закапывается автоматически.|r"
)
wts_updates[8598] = "|cffe4cfa3Выкопаться|r (|cffffffffW|r)"

# A0BR: Воскрешение мертвых (кладбище)
wts_updates[42120] = "|cffe4cfa3Воскрешение мертвых|r"
wts_updates[41512] = "|cffe4cfa3Воскрешение мертвых|r (|cffffffffR|r)"
wts_updates[42240] = "|cffe4cfa3Воскрешение мертвых|r"

# A0CA: Удар смерти
wts_updates[39433] = "|cffe4cfa3Удар смерти|r"
wts_updates[8770] = "|cffe4cfa3Удар смерти|r"
wts_updates[42125] = "|cffe4cfa3Удар смерти|r (|cffffffffQ|r)"
wts_updates[41159] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит удар по врагу, причиняя |cffffffff50|cffced4da урона. С вероятностью |cffffffff5%|cffced4da срабатывает автоматически при атаке.|r"
)

# A0CC: Ледяной удар
wts_updates[42129] = "|cffe4cfa3Ледяной удар|r"
wts_updates[8782] = "|cffe4cfa3Ледяной удар|r"
wts_updates[42166] = "|cffe4cfa3Ледяной удар|r (|cffffffffQ|r)"
wts_updates[39438] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит удар по врагу, причиняя |cffffffff100|cffced4da урона. С вероятностью |cffffffff5%|cffced4da срабатывает автоматически при атаке.|r"
)

# A1ND: Антимагический панцирь (активный)
wts_updates[42241] = "|cffe4cfa3Антимагический панцирь|r"
wts_updates[42243] = "|cffe4cfa3Антимагический панцирь|r (|cffffffffW|r)"
wts_updates[41833] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает рыцаря антимагическим щитом, поглощающим до |cffffffff600|cffced4da магического урона в течение |cffffffff40|cffced4da сек.|r"
)

# A0CG: Антимагический панцирь (эффект)
wts_updates[42232] = "|cffe4cfa3Антимагический панцирь|r"
wts_updates[42231] = "|cffe4cfa3Антимагический панцирь|r"

# kel0: Смерть и разложение [4 уровня]
wts_updates[39346] = "|cffe4cfa3Смерть и разложение|r"
wts_updates[39168] = "|cffe4cfa3Смерть и разложение|r [|cffffffffуровень %d|r]"
wts_updates[39288] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит периодический процентный урон всем вражеским войскам и зданиям в выбранной области.|n|n"
    "- Уровень 1: |cffffffff1%|cffced4da макс. здоровья в секунду (16 сек.).|n"
    "- Уровень 2: |cffffffff2%|cffced4da макс. здоровья в секунду (26 сек.).|n"
    "- Уровень 3: |cffffffff3%|cffced4da макс. здоровья в секунду (36 сек.).|n"
    "- Уровень 4: |cffffffff4%|cffced4da макс. здоровья в секунду (46 сек.).|r"
)
kel0_tips = [36995, 36996, 37808, 39061]
kel0_ubs = [39062, 39063, 39064, 39167]
kel0_data = [(1, 16), (2, 26), (3, 36), (4, 46)]
for lvl in range(1, 5):
    pct, dur = kel0_data[lvl-1]
    wts_updates[kel0_tips[lvl-1]] = f"|cffe4cfa3Смерть и разложение — уровень {lvl}|r (|cffffffffW|r)"
    wts_updates[kel0_ubs[lvl-1]] = (
        f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Враги в выбранной области теряют |cffffffff{pct}%|cffced4da максимального здоровья каждую секунду в течение |cffffffff{dur}|cffced4da сек. Действует на здания.|n|n"
        f"|cffa6afb8Уровень способности:|cffced4da |cffffffff{lvl}/4|cffced4da.|r"
    )

# A1E7: Смерть и разложение (канал)
wts_updates[32145] = "|cffe4cfa3Смерть и разложение|r"

def main():
    print(f"=== UNDEAD PLAN GENERATION ===")
    print(f"Total WTS updates prepared: {len(wts_updates)}")
    print(f"Total checks defined: {len(checks_def)}")

    # Check that all SIDs exist in war3map.wts
    missing_sids = [sid for sid in wts_updates if not check_wts_has(sid)]
    if missing_sids:
        print(f"ERROR: {len(missing_sids)} SIDs not found in war3map.wts: {missing_sids}")
        sys.exit(1)
    else:
        print("All SIDs cleanly matched in war3map.wts.")

    plan_payload = {
        "race": "Undead",
        "total_wts_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "metadata": {
            "buildings_count": len(bld_checks),
            "heroes_count": len(hero_checks),
            "units_count": len(unit_checks),
            "researches_count": 18
        }
    }

    docs_dir = ROOT / "docs/ui_text"
    docs_dir.mkdir(parents=True, exist_ok=True)
    plan_file = docs_dir / "undead_plan.json"
    plan_file.write_text(json.dumps(plan_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Plan saved to {plan_file} (size: {plan_file.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
