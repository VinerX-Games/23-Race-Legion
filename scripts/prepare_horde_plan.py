# -*- coding: utf-8 -*-
"""Comprehensive plan preparation for Race 14: Орда (Horde) UI text standardization.

Generates docs/ui_text/horde_plan.json containing:
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
import wc3_hivewe as hw

wts = hw.load_wts_strings()
dump = json.loads((ROOT / "scripts/horde_raw_dump.json").read_text(encoding="utf-8"))

def check_wts_has(sid):
    pattern = rf"STRING 0*{sid}\s*\{{\s*\r?\n"
    return bool(re.search(pattern, Path(ROOT / "map.w3x/war3map.wts").read_text(encoding="utf-8")))

wts_updates = {}
checks_def = []

# =========================================================================
# 1. SELECTION & SELECTION MARKERS
# =========================================================================
# A0YV: Орда (W)
wts_updates[5644] = "|cffe4cfa3Орда|r"
wts_updates[6032] = "|cffe4cfa3Орда|r (|cffffffffW|r)"
wts_updates[22344] = (
    "|cffa6afb8РАСА:|cffced4da Могущественный союз свободных народов, объединённых идеалами чести, воинской доблести и выживания в суровом мире.|r|n|n"
    "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
    "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
    "|cffa6afb8Сложность:|r |cffffffff●●●●|cffa6afb8●|r|n"
    "|cffa6afb8Период:|r |cffa9c7de«The Frozen Throne — Legion»|r|n|n"
    "|cffced4daОрда (также известная как Новая Орда Тралла) — одна из двух величайших сил Азерота. "
    "Руководствуясь единством и честью, Орда объединяет разрозненные народы орков, тауренов, троллей и их союзников в единый нерушимый союз. "
    "Обладая свирепыми воинами, мощной шаманской магией и несокрушимой волей, Орда готова отстаивать своё право на жизнь против любых угроз.|r"
)
checks_def.append({"type": "ability", "id": "A0YV", "field": "name", "expected": wts_updates[5644]})
checks_def.append({"type": "ability", "id": "A0YV", "field": "tip1", "expected": wts_updates[6032]})
checks_def.append({"type": "ability", "id": "A0YV", "field": "ubertip1", "expected": wts_updates[22344]})

# R0DV: Орда
wts_updates[22733] = "|cffe4cfa3Орда|r"
wts_updates[22734] = "|cffe4cfa3Орда|r"
wts_updates[22735] = "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Символ принадлежности к фракции Орды.|r"
checks_def.append({"type": "upgrade", "id": "R0DV", "field": "name1", "expected": wts_updates[22733]})
checks_def.append({"type": "upgrade", "id": "R0DV", "field": "tip1", "expected": wts_updates[22734]})

# R0IR: Черное Копье или Орда
wts_updates[32959] = "|cffe4cfa3Черное Копье или Орда|r"
wts_updates[32960] = "|cffe4cfa3Черное Копье или Орда|r"
checks_def.append({"type": "upgrade", "id": "R0IR", "field": "name1", "expected": wts_updates[32959]})
checks_def.append({"type": "upgrade", "id": "R0IR", "field": "tip1", "expected": wts_updates[32960]})

# R0J3: Гоблины или Орда
wts_updates[17624] = "|cffe4cfa3Гоблины или Орда|r"
wts_updates[17630] = "|cffe4cfa3Гоблины или Орда|r"
wts_updates[20112] = "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Символ союза гоблинов и Орды.|r"
checks_def.append({"type": "upgrade", "id": "R0J3", "field": "name1", "expected": wts_updates[17624]})
checks_def.append({"type": "upgrade", "id": "R0J3", "field": "tip1", "expected": wts_updates[17630]})

# =========================================================================
# 2. BUILDINGS (14)
# =========================================================================
# ogre: Дом вождей (Q)
wts_updates[36026] = "|cffe4cfa3Дом вождей|r"
wts_updates[36027] = "|cffe4cfa3Дом вождей|r (|cffffffffQ|r)"
wts_updates[29700] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Главный оплот и центр сбора ресурсов Орды. Обучает батраков и складирует ресурсы.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБатрак|cffced4da: базовый рабочий, строитель и добытчик ресурсов.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deГрабеж|cffced4da: войска ближнего боя воруют золото при атаке вражеских зданий.|n|n"
    "|cffa6afb8Улучшается до:|cffced4da|n- |cffa9c7deКрепость|cffced4da: открывает новые постройки и войска.|r"
)
checks_def.append({"type": "unit", "id": "ogre", "field": "name", "expected": wts_updates[36026]})
checks_def.append({"type": "unit", "id": "ogre", "field": "tip", "expected": wts_updates[36027]})

# ostr: Крепость (Z)
wts_updates[36028] = "|cffe4cfa3Крепость|r"
wts_updates[36029] = "|cffe4cfa3Крепость|r (|cffffffffZ|r)"
checks_def.append({"type": "unit", "id": "ostr", "field": "name", "expected": wts_updates[36028]})
checks_def.append({"type": "unit", "id": "ostr", "field": "tip", "expected": wts_updates[36029]})

# ofrt: Цитадель (Z)
wts_updates[36030] = "|cffe4cfa3Цитадель|r"
wts_updates[36031] = "|cffe4cfa3Цитадель|r (|cffffffffZ|r)"
checks_def.append({"type": "unit", "id": "ofrt", "field": "name", "expected": wts_updates[36030]})
checks_def.append({"type": "unit", "id": "ofrt", "field": "tip", "expected": wts_updates[36031]})

# otrb: Землянка (A)
wts_updates[36060] = "|cffe4cfa3Землянка|r"
wts_updates[36061] = "|cffe4cfa3Землянка|r (|cffffffffA|r)"
checks_def.append({"type": "unit", "id": "otrb", "field": "name", "expected": wts_updates[36060]})
checks_def.append({"type": "unit", "id": "otrb", "field": "tip", "expected": wts_updates[36061]})

# obar: Казармы (W)
wts_updates[36024] = "|cffe4cfa3Казармы|r"
wts_updates[36025] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
checks_def.append({"type": "unit", "id": "obar", "field": "name", "expected": wts_updates[36024]})
checks_def.append({"type": "unit", "id": "obar", "field": "tip", "expected": wts_updates[36025]})

# obea: Стрельбище (R)
wts_updates[36074] = "|cffe4cfa3Стрельбище|r"
wts_updates[36075] = "|cffe4cfa3Стрельбище|r (|cffffffffR|r)"
checks_def.append({"type": "unit", "id": "obea", "field": "name", "expected": wts_updates[36074]})
checks_def.append({"type": "unit", "id": "obea", "field": "tip", "expected": wts_updates[36075]})

# owtw: Сторожевая башня (Z)
wts_updates[36068] = "|cffe4cfa3Сторожевая башня|r"
wts_updates[36069] = "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)"
checks_def.append({"type": "unit", "id": "owtw", "field": "name", "expected": wts_updates[36068]})
checks_def.append({"type": "unit", "id": "owtw", "field": "tip", "expected": wts_updates[36069]})

# ofor: Лесопилка (E)
wts_updates[36064] = "|cffe4cfa3Лесопилка|r"
wts_updates[36065] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
checks_def.append({"type": "unit", "id": "ofor", "field": "name", "expected": wts_updates[36064]})
checks_def.append({"type": "unit", "id": "ofor", "field": "tip", "expected": wts_updates[36065]})

# oalt: Алтарь бури (S)
wts_updates[36072] = "|cffe4cfa3Алтарь бури|r"
wts_updates[36073] = "|cffe4cfa3Алтарь бури|r (|cffffffffS|r)"
checks_def.append({"type": "unit", "id": "oalt", "field": "name", "expected": wts_updates[36072]})
checks_def.append({"type": "unit", "id": "oalt", "field": "tip", "expected": wts_updates[36073]})

# osld: Обитель духов (D)
wts_updates[36066] = "|cffe4cfa3Обитель духов|r"
wts_updates[36067] = "|cffe4cfa3Обитель духов|r (|cffffffffD|r)"
checks_def.append({"type": "unit", "id": "osld", "field": "name", "expected": wts_updates[36066]})
checks_def.append({"type": "unit", "id": "osld", "field": "tip", "expected": wts_updates[36067]})

# otto: Мастерская (F)
wts_updates[36070] = "|cffe4cfa3Мастерская|r"
wts_updates[36071] = "|cffe4cfa3Мастерская|r (|cffffffffF|r)"
wts_updates[22877] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Производственное сооружение Орды. Выпускает тяжелую технику, осадные машины и сокрушительные механизмы.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОсадная машина Орды|cffced4da: мощное стенобитное орудие.|n"
    "- |cffa9c7deТехника Орды|cffced4da: тяжелая бронированная машина.|n"
    "- |cffa9c7deЖелезная звезда|cffced4da: разрушительный катящийся снаряд.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКомплектование техники|cffced4da: повышает запас здоровья осадных машин.|r"
)
checks_def.append({"type": "unit", "id": "otto", "field": "name", "expected": wts_updates[36070]})
checks_def.append({"type": "unit", "id": "otto", "field": "tip", "expected": wts_updates[36071]})
checks_def.append({"type": "unit", "id": "otto", "field": "ubertip", "expected": wts_updates[22877]})

# ovln: Посольство Орды (X)
wts_updates[36062] = "|cffe4cfa3Посольство Орды|r"
wts_updates[36063] = "|cffe4cfa3Посольство Орды|r (|cffffffffX|r)"
wts_updates[22725] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Дипломатический центр Орды. Позволяет заключать союзы с другими народами и кланами Азерота, расширяя состав армии и доступные технологии.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОтказаться от Расширения|cffced4da: укрепляет текущую армию Орды.|n"
    "- |cffa9c7deВоссоединение орков|cffced4da: открывает кланы Черной Горы и Драконьей Пасти.|n"
    "- |cffa9c7deПоиск союзников|cffced4da: открывает союз с Отрекшимися и эльфами крови.|n"
    "- |cffa9c7deВопросы безопасности|cffced4da: открывает союз с гоблинами и рыцарями смерти.|n"
    "- |cffa9c7deДорога к компромису|cffced4da: компромиссное дипломатическое решение.|r"
)
checks_def.append({"type": "unit", "id": "ovln", "field": "name", "expected": wts_updates[36062]})
checks_def.append({"type": "unit", "id": "ovln", "field": "tip", "expected": wts_updates[36063]})
checks_def.append({"type": "unit", "id": "ovln", "field": "ubertip", "expected": wts_updates[22725]})

# h0D3: Верфь (C)
wts_updates[10901] = "|cffe4cfa3Верфь|r"
wts_updates[10902] = "|cffe4cfa3Верфь|r (|cffffffffC|r)"
wts_updates[22662] = (
    "|cffa6afb8ЗДАНИЕ:|cffced4da Строит корабли и исследует улучшения флота.|n|n"
    "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТранспорт|cffced4da.|n- |cffa9c7deФрегат|cffced4da.|n- |cffa9c7deДредноут|cffced4da.|n|n"
    "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбстрел|cffced4da.|n- |cffa9c7deДополнительные паруса|cffced4da.|n- |cffa9c7deПочинка|cffced4da.|n- |cffa9c7deОрудия флота|cffced4da.|n- |cffa9c7deУкреплённый корпус|cffced4da.|n|n"
    "|cffa9c7deЗона ремонта|cffced4da восстанавливает |cff60dc702,5|cffced4da здоровья/сек. союзным кораблям поблизости.|r"
)
checks_def.append({"type": "unit", "id": "h0D3", "field": "name", "expected": wts_updates[10901]})
checks_def.append({"type": "unit", "id": "h0D3", "field": "tip", "expected": wts_updates[10902]})
checks_def.append({"type": "unit", "id": "h0D3", "field": "ubertip", "expected": wts_updates[22662]})

# =========================================================================
# 3. HEROES (7)
# =========================================================================
# Obla: Мастер клинка (Z)
wts_updates[36081] = "|cffe4cfa3Мастер клинка|r"
wts_updates[36083] = "|cffe4cfa3Мастер клинка|r (|cffffffffZ|r)"
wts_updates[36082] = "|cffe4cfa3Мастер клинка|r (|cffffffffZ|r)"
wts_updates[36080] = "|cffe4cfa3Мастер клинка|r (|cffffffffZ|r)"
checks_def.append({"type": "unit", "id": "Obla", "field": "name", "expected": wts_updates[36081]})
checks_def.append({"type": "unit", "id": "Obla", "field": "tip", "expected": wts_updates[36083]})

# Ofar: Предсказатель (X)
wts_updates[36084] = "|cffe4cfa3Предсказатель|r"
wts_updates[36086] = "|cffe4cfa3Предсказатель|r (|cffffffffX|r)"
wts_updates[36087] = "|cffe4cfa3Предсказатель|r (|cffffffffX|r)"
wts_updates[36085] = "|cffe4cfa3Предсказатель|r (|cffffffffX|r)"
checks_def.append({"type": "unit", "id": "Ofar", "field": "name", "expected": wts_updates[36084]})
checks_def.append({"type": "unit", "id": "Ofar", "field": "tip", "expected": wts_updates[36086]})

# Otch: Вождь тауренов (C)
wts_updates[36077] = "|cffe4cfa3Вождь тауренов|r"
wts_updates[36078] = "|cffe4cfa3Вождь тауренов|r (|cffffffffC|r)"
wts_updates[36079] = "|cffe4cfa3Вождь тауренов|r (|cffffffffC|r)"
wts_updates[36076] = "|cffe4cfa3Вождь тауренов|r (|cffffffffC|r)"
checks_def.append({"type": "unit", "id": "Otch", "field": "name", "expected": wts_updates[36077]})
checks_def.append({"type": "unit", "id": "Otch", "field": "tip", "expected": wts_updates[36078]})

# O02Z: Генерал Орды (T)
wts_updates[9961] = "|cffe4cfa3Генерал Орды|r"
wts_updates[25819] = "|cffe4cfa3Генерал Орды|r (|cffffffffT|r)"
wts_updates[25820] = "|cffe4cfa3Генерал Орды|r (|cffffffffT|r)"
wts_updates[25818] = "|cffe4cfa3Генерал Орды|r (|cffffffffT|r)"
wts_updates[29064] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Могучий полководец Орды, закалённый в бесчисленных битвах. Вдохновляет воинов и сокрушает врагов тяжелыми ударами.|n|n"
    "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУдарная волна|cffced4da: выпускает волну энергии, наносящую урон врагам на прямой линии.|n"
    "- |cffa9c7deГромовая поступь|cffced4da: сотрясает землю, нанося урон и оглушая врагов вокруг.|n"
    "- |cffa9c7deАура выносливости|cffced4da: увеличивает скорость перемещения и атаки союзников.|n"
    "- |cffa9c7deРеинкарнация|cffced4da: воскрешает героя после гибели.|n|n"
    "Атакует наземные цели.|r"
)
checks_def.append({"type": "unit", "id": "O02Z", "field": "name", "expected": wts_updates[9961]})
checks_def.append({"type": "unit", "id": "O02Z", "field": "tip", "expected": wts_updates[25819]})
checks_def.append({"type": "unit", "id": "O02Z", "field": "ubertip", "expected": wts_updates[29064]})

# O02P: Вождь Орды (Z) - Гаррош
wts_updates[22493] = "|cffe4cfa3Вождь Орды|r"
wts_updates[22499] = "|cffe4cfa3Вождь Орды|r (|cffffffffZ|r)"
wts_updates[22500] = "|cffe4cfa3Вождь Орды|r (|cffffffffZ|r)"
wts_updates[22498] = "|cffe4cfa3Вождь Орды|r (|cffffffffZ|r)"
wts_updates[29061] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Свирепый верховный вождь Орды. Ведёт армию в бой неукротимой яростью, сокрушает врагов и вдохновляет союзников.|n|n"
    "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: наносит урон по области вокруг атакуемой цели.|n"
    "- |cffa9c7deПризвать Охрану|cffced4da: призывает преданных воинов Кор'Крона.|n"
    "- |cffa9c7deЗа Орду!|cffced4da: накладывает эффект жажды крови на всех ближайших союзников.|n"
    "- |cffa9c7deЯрость Адского Крика|cffced4da: значительно увеличивает здоровье, броню, урон и даёт защиту от магии.|n|n"
    "Атакует наземные цели.|r"
)
checks_def.append({"type": "unit", "id": "O02P", "field": "name", "expected": wts_updates[22493]})
checks_def.append({"type": "unit", "id": "O02P", "field": "tip", "expected": wts_updates[22499]})
checks_def.append({"type": "unit", "id": "O02P", "field": "ubertip", "expected": wts_updates[29061]})

# Othr: Лидер Орды (Z) - Тралл
wts_updates[40232] = "|cffe4cfa3Лидер Орды|r"
wts_updates[40235] = "|cffe4cfa3Лидер Орды|r (|cffffffffZ|r)"
wts_updates[40234] = "|cffe4cfa3Лидер Орды|r (|cffffffffZ|r)"
wts_updates[40233] = "|cffe4cfa3Лидер Орды|r (|cffffffffZ|r)"
wts_updates[16896] = (
    "|cffa6afb8ГЕРОЙ:|cffced4da Великий шаман и основатель Новой Орды. Повелевает стихиями, призывает волков и сковывает врагов мощью земли.|n|n"
    "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЦепная молния|cffced4da: поражает группу врагов разрядом стихийной молнии.|n"
    "- |cffa9c7deДух волка|cffced4da: призывает свирепых призрачных волков.|n"
    "- |cffa9c7deЗемляные оковы|cffced4da: обездвиживает вражеских воинов в выбранной области.|n"
    "- |cffa9c7deИспепеление|cffced4da: обрушивает на цель и её окружение шквал разрушительной магии.|n|n"
    "Атакует наземные и воздушные цели.|r"
)
checks_def.append({"type": "unit", "id": "Othr", "field": "name", "expected": wts_updates[40232]})
checks_def.append({"type": "unit", "id": "Othr", "field": "tip", "expected": wts_updates[40235]})
checks_def.append({"type": "unit", "id": "Othr", "field": "ubertip", "expected": wts_updates[16896]})

# H0BN: Дамми Гер
wts_updates[9613] = "|cffa6afb8Дамми Гер|r"

# =========================================================================
# 4. CORE UNITS & DIPLOMATIC VARIANTS (70+)
# =========================================================================
units_data = [
    # (id, name_sid, tip_sid, ub_sid, name, hotkey, role_desc, attacks_air)
    ('opeo', 36036, 22070, 36035, 'Батрак', 'Q', 'Базовый рабочий Орды. Добывает золото и древесину, возводит и ремонтирует постройки.', False),
    ('ogru', 36032, 16473, 12530, 'Рядовой воин Орды', 'R', 'Основной пехотинец Орды ближнего боя. Наносит стабильный урон и принимает удар на передовой.', False),
    ('o01N', 36088, 36089, 36090, 'Основной воин Орды', 'R', 'Тяжеловооруженный пехотинец Железной Орды в закалённых доспехах.', False),
    ('otau', 36054, 36055, 36056, 'Элитный воин Орды', 'T', 'Могучий тяжелый воин-таурен. Обладает огромным запасом здоровья и сокрушительной силой удара.', False),
    ('orai', 36045, 36046, 36047, 'Кавалерия Орды', 'R', 'Стремительный волчий всадник. Владеет сетью для прижатия воздушных и наземных целей к земле.', False),
    ('ocat', 36051, 36052, 36053, 'Осадная машина Орды', 'D', 'Тяжелая катапульта Орды. Наносит сокрушительный осадный урон по зданиям и группам врагов.', False),
    ('ohun', 36048, 36049, 16134, 'Рядовой стрелок Орды', 'T', 'Меткий метатель копий троллей. Эффективен против легких и летающих целей.', True),
    ('otbk', 22973, 22974, 22975, 'Берсерк', 'B', 'Тролль-берсерк. Может впадать в ярость, значительно увеличивая скорость атаки.', True),
    ('okod', 36042, 36043, 36044, 'Элитный стрелок Орды', 'K', 'Огромный боевой кодо с наездниками. Усиливает союзников боевыми барабанами и пожирает врагов.', True),
    ('o029', 36094, 36095, 36096, 'Основной воин Орды', 'C', 'Тяжелый наездник на кодо, бронированный для затяжных фронтовых столкновений.', False),
    ('o01P', 36091, 36092, 36093, 'Основной стрелок Орды', 'W', 'Летающий наездник на ветрокрыле, поражающий врагов отравленными копьями.', True),
    ('oshm', 36057, 36058, 36059, 'Маг Орды (поддержка)', 'S', 'Шаман Орды. Владеет очищением, щитом молний и накладывает жажду крови.', True),
    ('odoc', 36039, 36040, 36041, 'Маг Орды (специализированный)', 'W', 'Знахарь троллей. Расставляет тотемы разведки, стазисные ловушки и целительные тотемы.', True),
    ('ospw', 22722, 22723, 22724, 'Духостранник', 'W', 'Мистический таурен. Связывает души воинов, рассеивает чары и возвращает павших тауренов к жизни.', True),
    ('o01W', 36130, 22143, 9593, 'Маг Орды (Урон)', 'S', 'Верховный шаман стихий. Обрушивает на врагов разрушительные молнии и бури.', True),
    ('o022', 36136, 22445, 22452, 'Техника Орды', 'E', 'Тяжелая бронированная машина. Эффективно разрушает укрепления и осадные орудия врага.', False),
    ('h0CY', 36128, 22141, 28310, 'Железная звезда', 'Z', 'Сокрушительное катящееся осадное колесо Железной Орды. Взрывается при контакте с врагом.', False),
    ('h0OL', 39577, 39579, 39580, 'Железная звезда', 'Z', 'Штурмовая взрывная звезда Железной Орды.', False),
    ('o02B', 36144, 12372, 36097, 'Основной стрелок Орды', 'G', 'Стрелок Железной Орды с тяжелым крупнокалиберным мушкетом.', True),

    # Fleet
    ('h0D5', 10916, 10918, 6926, 'Дредноут', 'E', 'Тяжелый бронированный флагман флота Орды дальнего боя.', True),
    ('h0D6', 3002, 10911, 5542, 'Фрегат', 'W', 'Боевой патрульный корабль Орды, атакующий морские и береговые цели.', True),
    ('h0HM', 22186, 22147, 12225, 'Броненосец', 'E', 'Сверхтяжелый бронированный корабль Орды с усиленной защитой.', True),
    ('h0HT', 3003, 22189, 12270, 'Фрегат Син\'Дорай', 'W', 'Изящный эльфийский боевой корабль с магическим артиллерийским вооружением.', True),
    ('h0I5', 25318, 25321, 22145, 'Линкор Отрекшихся', 'E', 'Грозный линкор нежити, оснащенный метателями чумы и тяжелыми пушками.', True),
    ('h0IH', 36157, 22450, 15432, 'Отрекшийся-убийца', 'K', 'Скрытный убийца Отрекшихся, наносящий смертоносные удары из тени.', False),
    ('h0J3', 3005, 25326, 16131, 'Фрегат Отррекшихся', 'W', 'Быстроходный фрегат Отрекшихся с чумными орудиями.', True),
    ('h0J4', 3006, 25328, 20463, 'Гордость Зандалара', 'W', 'Боевой корабль зандаларских троллей, защищенный благословением Лоа.', True),
    ('h0JB', 25322, 25323, 22190, 'Судно Гоблинов', 'W', 'Гоблинский паровой катер с ракетными установками.', True),
    ('n04J', 10043, 10044, 10045, 'Отголосок Ненависти', 'N', 'Тёмное порождение Ша, питающееся гневом и ненавистью врагов.', False),

    # Clan & Diplomatic variants
    ('o01I', 36116, 36033, 16474, 'Бугай', 'R', 'Крепкий орочий пехотинец ближнего боя с тяжелым топором.', False),
    ('o01E', 36110, 15725, 15726, 'Рубака Черной Горы', 'R', 'Опытный ветеран клана Черной Горы, обученный жестоким приемам второй войны.', False),
    ('o01F', 36111, 15736, 15735, 'Эльф-воин (Орда)', 'R', 'Мечник эльфов крови на службе Орды, искусный фехтовальщик.', False),
    ('o01H', 36115, 16563, 16562, 'Отрекшийся-воин (Орда)', 'R', 'Пехотинец нежити Отрекшихся, не знающий усталости и боли.', False),
    ('o01J', 22702, 22703, 22704, 'Шаман', 'S', 'Шаман Орды, призывающий благословение духов стихий.', True),
    ('o01K', 36119, 25612, 25613, 'Огр-маг', 'S', 'Двуглавый огр-заклинатель, сочетающий грубую физическую мощь и магию крови.', True),
    ('o01L', 36120, 25614, 25615, 'Таурен-воитель', 'T', 'Могучий защитник племени тауренов с огромным ритуальным бревном.', False),
    ('o01M', 36121, 25616, 25617, 'Огр-воитель', 'T', 'Огромный бронированный огр-бугай, сокрушающий ряды врагов.', False),
    ('o01O', 10081, 10082, 10083, 'Огр-воин', 'R', 'Сильный боец ближнего боя из союзных кланов огров.', False),
    ('o01Q', 36123, 4110, 4111, 'Орк-воин', 'Q', 'Отважный воин Орды, готовый отдать жизнь за вождя.', False),
    ('o01R', 36124, 25622, 25623, 'Наездник на Кодо', 'K', 'Тяжелый всадник на кодо, воодушевляющий союзников громким боем барабанов.', True),
    ('o01S', 36125, 25624, 25625, 'Наездник на Драконе', 'D', 'Элитный всадник клана Драконьей Пасти верхом на порабощенном драконе.', True),
    ('o01T', 36126, 25626, 25627, 'Разрушитель', 'D', 'Осадная баллиста Орды, наносящая сокрушительный урон укреплениям.', False),
    ('o01U', 36127, 25628, 25629, 'Воин Кор\'Крона', 'T', 'Элитный гвардеец вождя из ударного корпуса Кор\'Крон.', False),
    ('o01V', 36129, 25631, 25632, 'Темный шаман', 'S', 'Темный шаман, подчиняющий стихии силой и использующий темную магию.', True),
    ('o01X', 36131, 3764, 3765, 'Орк-копьеметатель', 'T', 'Опытный орочий стрелок дальнего боя.', True),
    ('o01Y', 36132, 14454, 14455, 'Копьеметатель Черной Горы', 'T', 'Стрелок клана Черной Горы с тяжелыми зазубренными копьями.', True),
    ('o01Z', 36133, 25639, 25640, 'Всадник Драконьей Пасти', 'R', 'Быстрый налетчик клана Драконьей Пасти.', False),
    ('o020', 3646, 25641, 25642, 'Железный Разрушитель', 'D', 'Бронированная тяжелая осадная машина Железной Орды.', False),
    ('o021', 36135, 25643, 25644, 'Рыцарь смерти', 'T', 'Падший рыцарь на службе Орды, использующий силу льда и тьмы.', False),
    ('o023', 36137, 25645, 25646, 'Магистр', 'S', 'Верховный эльфийский маг, повелевающий огнем и чародейством.', True),
    ('o024', 36138, 25647, 25648, 'Знахарь', 'W', 'Мудрый тролль-знахарь, расставляющий поддерживающие тотемы.', True),
    ('o025', 36139, 25649, 25650, 'Ведьмак', 'W', 'Заклинатель троллей, ослабляющий и проклинающий врагов.', True),
    ('o026', 36140, 25651, 25652, 'Арканитовый страж', 'D', 'Массивный механический голем, защищенный прочной арканитовой броней.', False),
    ('o027', 36141, 25653, 25654, 'Налетчик', 'R', 'Маневренный волчий всадник, обученный молниеносным атакам.', False),
    ('o028', 36142, 25655, 25656, 'Гоблинский уничтожитель-3000', 'D', 'Экспериментальный боевой шагоход гоблинов с ракетным вооружением.', False),
    ('o02A', 36143, 4377, 4378, 'Орк-воин', 'Q', 'Отважный пехотинец Орды.', False),
    ('o02C', 36145, 15195, 15196, 'Копьеметатель Черной Горы', 'T', 'Закалённый стрелок клана Черной Горы.', True),
    ('o02D', 36146, 15828, 15829, 'Бронированный Копьеметатель', 'T', 'Стрелок в усиленных пластинчатых доспехах.', True),
    ('o02E', 36147, 25663, 25664, 'Магнатавр', 'R', 'Огромный северный магнатавр, сокрушающий вражескую пехоту чудовищной массой.', False),
    ('o02F', 36148, 19841, 19842, 'Стрелок-гоблин', 'T', 'Гоблинский стрелок с дальнобойным пороховым мушкетом.', True),
    ('o02G', 36149, 25667, 25668, 'Колдун', 'S', 'Темный чернокнижник, призывающий силы Скверны.', True),
    ('o02H', 36150, 25669, 25670, 'Всадник Син\'Дорай', 'R', 'Эльфийский наездник на крылобеге, наносящий быстрые удары.', False),
    ('o02I', 36151, 25671, 25672, 'Медик', 'W', 'Полевой лекарь, восстанавливающий здоровье раненым бойцам.', True),
    ('o02J', 36152, 23349, 23350, 'Стрелок-гоблин', 'T', 'Наемный стрелок гоблинов с модифицированным карабином.', True),
    ('o02K', 36153, 25675, 28312, 'Баллиста', 'D', 'Тяжелая осадная баллиста, пробивающая укрепления огромными болтами.', False),
    ('o02L', 36154, 25677, 25678, 'Темный маг', 'W', 'Заклинатель тьмы, ослабляющий противников проклятиями.', True),
    ('o02M', 36155, 25679, 25680, 'Темный следопыт', 'K', 'Ловкий следопыт нежити, поражающий врагов темными стрелами.', True),
    ('o02S', 36156, 4692, 4693, 'Мастер боя', 'Q', 'Искусный воин, мастерски владеющий оружием ближнего боя.', False),
    ('o02U', 36158, 25683, 25684, 'Зачарователь', 'S', 'Маг-чародей, усиливающий атаки союзных войск магическими чарами.', True),
    ('o02W', 36159, 25685, 25686, 'Воин Шадо-Пан', 'T', 'Элитный пандаренский монах ордена Шадо-Пан, мастер рукопашного боя.', False),
    ('o032', 3007, 36160, 25688, 'Тен Тотем', 'T', 'Легендарный воитель тауренов, несущий гигантский тотем предков.', False),
    ('o00A', 36122, 25618, 25619, 'Огр-воин', 'R', 'Могучий боец ближнего боя из племени огров.', False)
]

dump = json.loads((ROOT / "scripts/horde_raw_dump.json").read_text(encoding="utf-8"))

for uid, nsid, tsid, usid, uname, hk, urole, attacks_air in units_data:
    f = dump['units'].get(uid, {}).get('fields', {})
    act_name = f.get('name')
    act_tip = f.get('tip')
    act_ub = f.get('ubertip')

    if act_name == f'TRIGSTR_{nsid}':
        wts_updates[nsid] = f"|cffe4cfa3{uname}|r"
        checks_def.append({"type": "unit", "id": uid, "field": "name", "expected": wts_updates[nsid]})

    if act_tip == f'TRIGSTR_{tsid}':
        wts_updates[tsid] = f"|cffe4cfa3{uname}|r (|cffffffff{hk}|r)"
        checks_def.append({"type": "unit", "id": uid, "field": "tip", "expected": wts_updates[tsid]})

    if act_ub == f'TRIGSTR_{usid}':
        atk_str = "Атакует наземные и воздушные цели." if attacks_air else "Атакует наземные цели."
        wts_updates[usid] = (
            f"|cffa6afb8ЮНИТ:|cffced4da {urole}|n|n"
            f"{atk_str}|r"
        )
        checks_def.append({"type": "unit", "id": uid, "field": "ubertip", "expected": wts_updates[usid]})

# =========================================================================
# 5. RESEARCHES & UPGRADES
# =========================================================================

# --- 5.1 Blacksmith 6-tier upgrades ---
# Rome: Оружие ближнего боя (Q)
rome_names = [36197, 36198, 36199, 36191, 36192, 36193]
rome_tips = [36200, 36201, 36202, 36194, 36195, 36196]
rome_ubs = [22775, 22776, 22794, 22795, 22796, 22797]
rome_bonuses = [1, 2, 3, 4, 5, 6]
for lvl in range(1, 7):
    wts_updates[rome_names[lvl-1]] = f"|cffe4cfa3Оружие ближнего боя — уровень {lvl}|r"
    wts_updates[rome_tips[lvl-1]] = f"|cffe4cfa3Оружие ближнего боя — уровень {lvl}|r (|cffffffffQ|r)"
    wts_updates[rome_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак ближнего боя воинов Орды на |cff60dc70+{rome_bonuses[lvl-1]}|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРядовой воин Орды|cffced4da|n- |cffa9c7deОсновной воин Орды|cffced4da|n- |cffa9c7deЭлитный воин Орды|cffced4da|n- |cffa9c7deКавалерия Орды|cffced4da.|r"
    )

# Roar: Улучшенная броня (A)
roar_names = [36184, 36185, 36186, 36181, 36182, 36183]
roar_tips = [36187, 36188, 36189, 36178, 36179, 36180]
roar_ubs = [36190, 22765, 22766, 22767, 22768, 22769]
roar_bonuses = [1, 2, 3, 4, 5, 6]
for lvl in range(1, 7):
    wts_updates[roar_names[lvl-1]] = f"|cffe4cfa3Улучшенная броня — уровень {lvl}|r"
    wts_updates[roar_tips[lvl-1]] = f"|cffe4cfa3Улучшенная броня — уровень {lvl}|r (|cffffffffA|r)"
    wts_updates[roar_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает защиту наземных войск Орды на |cff60dc70+{roar_bonuses[lvl-1]}|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРядовой воин Орды|cffced4da|n- |cffa9c7deОсновной воин Орды|cffced4da|n- |cffa9c7deРядовой стрелок Орды|cffced4da|n- |cffa9c7deКавалерия Орды|cffced4da|n- |cffa9c7deЭлитный воин Орды|cffced4da.|r"
    )

# Rora: Оружие дальнего боя (W)
rora_names = [36167, 36168, 36169, 36161, 36162, 36163]
rora_tips = [36170, 36171, 36172, 36164, 36165, 36166]
rora_ubs = [22746, 22747, 22748, 22743, 22744, 22745]
rora_bonuses = [1, 2, 3, 4, 5, 6]
for lvl in range(1, 7):
    wts_updates[rora_names[lvl-1]] = f"|cffe4cfa3Оружие дальнего боя — уровень {lvl}|r"
    wts_updates[rora_tips[lvl-1]] = f"|cffe4cfa3Оружие дальнего боя — уровень {lvl}|r (|cffffffffW|r)"
    wts_updates[rora_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак дальнего боя стрелков Орды на |cff60dc70+{rora_bonuses[lvl-1]}|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРядовой стрелок Орды|cffced4da|n- |cffa9c7deОсновной стрелок Орды|cffced4da|n- |cffa9c7deБерсерк|cffced4da.|r"
    )

# R0G5: Артефакты (E)
r0g5_names = [40617, 40623, 40618, 40619, 40621, 40622]
r0g5_tips = [40620, 40624, 40625, 40626, 40627, 40628]
r0g5_ubs = [27327, 27328, 27329, 27330, 27331, 27332]
for lvl in range(1, 7):
    wts_updates[r0g5_names[lvl-1]] = f"|cffe4cfa3Артефакты — уровень {lvl}|r"
    wts_updates[r0g5_tips[lvl-1]] = f"|cffe4cfa3Артефакты — уровень {lvl}|r (|cffffffffE|r)"
    wts_updates[r0g5_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает магическую мощь и запас маны заклинателей Орды.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМаг Орды (поддержка)|cffced4da|n- |cffa9c7deМаг Орды (специализированный)|cffced4da|n- |cffa9c7deДухостранник|cffced4da|n- |cffa9c7deМаг Орды (Урон)|cffced4da.|r"
    )

# R0E6: Улучшенные пилы (Z)
r0e6_names = [40596, 40606, 40597, 40598, 40599, 40600]
r0e6_tips = [40601, 40607, 40602, 40603, 40604, 40605]
r0e6_ubs = [22010, 22005, 22006, 22007, 22008, 22009]
for lvl in range(1, 7):
    wts_updates[r0e6_names[lvl-1]] = f"|cffe4cfa3Улучшенные пилы — уровень {lvl}|r"
    wts_updates[r0e6_tips[lvl-1]] = f"|cffe4cfa3Улучшенные пилы — уровень {lvl}|r (|cffffffffZ|r)"
    wts_updates[r0e6_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой батраками древесины на |cff60dc70+5|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deБатрак|cffced4da.|r"
    )

# --- 5.2 Unit specialization 3-tier upgrades ---
# R0EC: Тренировка ближнего боя (Z)
r0ec_names = [36247, 23419, 23420]
r0ec_tips = [23425, 23426, 23427]
r0ec_ubs = [23403, 23404, 23405]
for lvl in range(1, 4):
    wts_updates[r0ec_names[lvl-1]] = f"|cffe4cfa3Тренировка ближнего боя — уровень {lvl}|r"
    wts_updates[r0ec_tips[lvl-1]] = f"|cffe4cfa3Тренировка ближнего боя — уровень {lvl}|r (|cffffffffZ|r)"
    wts_updates[r0ec_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья воинов ближнего боя на |cff60dc70+{lvl*100}|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/3|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРядовой воин Орды|cffced4da|n- |cffa9c7deОсновной воин Орды|cffced4da|n- |cffa9c7deЭлитный воин Орды|cffced4da.|r"
    )

# R0ED: Тренировка дальнего боя (Z)
r0ed_names = [36248, 23460, 23461]
r0ed_tips = [23466, 23467, 23468]
r0ed_ubs = [23483, 23484, 23485]
for lvl in range(1, 4):
    wts_updates[r0ed_names[lvl-1]] = f"|cffe4cfa3Тренировка дальнего боя — уровень {lvl}|r"
    wts_updates[r0ed_tips[lvl-1]] = f"|cffe4cfa3Тренировка дальнего боя — уровень {lvl}|r (|cffffffffZ|r)"
    wts_updates[r0ed_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья стрелков Орды на |cff60dc70+{lvl*75}|cffced4da.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/3|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРядовой стрелок Орды|cffced4da|n- |cffa9c7deОсновной стрелок Орды|cffced4da|n- |cffa9c7deБерсерк|cffced4da.|r"
    )

# R0EF: Комплектование техники (Z)
r0ef_names = [40611, 24304, 24305]
r0ef_tips = [24310, 24311, 24312]
r0ef_ubs = [25336, 25337, 25338]
for lvl in range(1, 4):
    wts_updates[r0ef_names[lvl-1]] = f"|cffe4cfa3Комплектование техники — уровень {lvl}|r"
    wts_updates[r0ef_tips[lvl-1]] = f"|cffe4cfa3Комплектование техники — уровень {lvl}|r (|cffffffffZ|r)"
    wts_updates[r0ef_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает прочность и броню осадных машин Орды.|n|n"
        f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/3|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОсадная машина Орды|cffced4da|n- |cffa9c7deТехника Орды|cffced4da|n- |cffa9c7deЖелезная звезда|cffced4da.|r"
    )

# Rosp: Шипастые укрепления (S)
rosp_names = [36226, 36227, 36228]
rosp_tips = [36229, 36230, 36231]
for lvl in range(1, 4):
    wts_updates[rosp_names[lvl-1]] = f"|cffe4cfa3Шипастые укрепления — уровень {lvl}|r"
    wts_updates[rosp_tips[lvl-1]] = f"|cffe4cfa3Шипастые укрепления — уровень {lvl}|r (|cffffffffS|r)"

# Rost: Обучение магов поддержки (Z)
rost_names = [36203, 36204, 36207]
rost_tips = [36205, 36206, 36208]
rost_ubs = [23130, 23133, 23134]
for lvl in range(1, 4):
    wts_updates[rost_names[lvl-1]] = f"|cffe4cfa3Обучение магов поддержки — ступень {lvl}|r"
    wts_updates[rost_tips[lvl-1]] = f"|cffe4cfa3Обучение магов поддержки — ступень {lvl}|r (|cffffffffZ|r)"
    wts_updates[rost_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас маны, скорость её восстановления и открывает новые заклинания шаманов Орды.|n|n"
        f"|cffa6afb8Ступень обучения:|cffced4da |cffffffff{lvl}/3|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМаг Орды (поддержка)|cffced4da.|r"
    )

# Rowd: Обучение специализированных магов (C)
rowd_names = [36215, 36216, 36219]
rowd_tips = [36217, 36218, 36220]
rowd_ubs = [36221, 36222, 36223]
for lvl in range(1, 4):
    wts_updates[rowd_names[lvl-1]] = f"|cffe4cfa3Обучение специализированных магов — ступень {lvl}|r"
    wts_updates[rowd_tips[lvl-1]] = f"|cffe4cfa3Обучение специализированных магов — ступень {lvl}|r (|cffffffffC|r)"
    wts_updates[rowd_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас маны, скорость её восстановления и открывает новые тотемы знахарей.|n|n"
        f"|cffa6afb8Ступень обучения:|cffced4da |cffffffff{lvl}/3|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМаг Орды (специализированный)|cffced4da.|r"
    )

# Rowt: Обучение боевых магов (X)
rowt_names = [36209, 36210, 36213]
rowt_tips = [36211, 36212, 36214]
rowt_ubs = [22153, 28385, 28483]
for lvl in range(1, 4):
    wts_updates[rowt_names[lvl-1]] = f"|cffe4cfa3Обучение боевых магов — ступень {lvl}|r"
    wts_updates[rowt_tips[lvl-1]] = f"|cffe4cfa3Обучение боевых магов — ступень {lvl}|r (|cffffffffX|r)"
    wts_updates[rowt_ubs[lvl-1]] = (
        f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, маны и боевой потенциал старших шаманов Орды.|n|n"
        f"|cffa6afb8Ступень обучения:|cffced4da |cffffffff{lvl}/3|cffced4da.|n|n"
        f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМаг Орды (Урон)|cffced4da.|r"
    )

# Single-tier base researches
# Ropg: Грабеж
wts_updates[22401] = "|cffe4cfa3Грабеж|r"
wts_updates[22402] = "|cffe4cfa3Грабеж|r"
wts_updates[22403] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Воины ближнего боя Орды воруют золото при нанесении урона вражеским постройкам.|n|n"
    "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРядовой воин Орды|cffced4da|n- |cffa9c7deОсновной воин Орды|cffced4da|n- |cffa9c7deКавалерия Орды|cffced4da.|r"
)

# Rorb: Укрепленные стены
wts_updates[36224] = "|cffe4cfa3Укрепленные стены|r"
wts_updates[36225] = "|cffe4cfa3Укрепленные стены|r"

# --- 5.3 Diplomatic & Iron Horde Branches (17+) ---
# R0D1: Амнистия Клана Черной Горы (E)
wts_updates[22950] = "|cffe4cfa3Амнистия Клана Черной Горы|r"
wts_updates[22987] = "|cffe4cfa3Амнистия Клана Черной Горы|r (|cffffffffE|r)"
wts_updates[36917] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Вождь дарует амнистию оркам клана Черной Горы, привлекая их опытных рубак в армию.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает доступ к тренировке |cffa9c7deРубака Черной Горы|cffced4da.|n"
    "- Снижает затраты на содержание пехоты на |cff60dc704%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0D1", "field": "name1", "expected": wts_updates[22950]})
checks_def.append({"type": "upgrade", "id": "R0D1", "field": "tip1", "expected": wts_updates[22987]})
checks_def.append({"type": "upgrade", "id": "R0D1", "field": "ubertip1", "expected": wts_updates[36917]})

# R0D2: Эльфы в беде (Q)
wts_updates[36236] = "|cffe4cfa3Эльфы в беде|r"
wts_updates[22892] = "|cffe4cfa3Эльфы в беде|r (|cffffffffQ|r)"
wts_updates[36918] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Принимает эльфов крови под знамена Орды по рекомендации Отрекшихся.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает эльфийских мечников, магов и боевые корабли Син'Дорай.|n"
    "- Снижает затраты на содержание на |cff60dc704%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0D2", "field": "name1", "expected": wts_updates[36236]})
checks_def.append({"type": "upgrade", "id": "R0D2", "field": "tip1", "expected": wts_updates[22892]})
checks_def.append({"type": "upgrade", "id": "R0D2", "field": "ubertip1", "expected": wts_updates[36918]})

# R0D3: Предложение отрекшихся (Q)
wts_updates[36237] = "|cffe4cfa3Предложение отрекшихся|r"
wts_updates[40584] = "|cffe4cfa3Предложение отрекшихся|r (|cffffffffQ|r)"
wts_updates[36919] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заключает полноценный союз с Отрекшимися Лордерона.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает воинов нежити, убийц и чумные боевые корабли.|n"
    "- Снижает затраты на содержание на |cff60dc702%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0D3", "field": "name1", "expected": wts_updates[36237]})
checks_def.append({"type": "upgrade", "id": "R0D3", "field": "tip1", "expected": wts_updates[40584]})
checks_def.append({"type": "upgrade", "id": "R0D3", "field": "ubertip1", "expected": wts_updates[36919]})

# R0DW: Отказаться от Расширения (R)
wts_updates[36238] = "|cffe4cfa3Отказаться от Расширения|r"
wts_updates[40585] = "|cffe4cfa3Отказаться от Расширения|r (|cffffffffR|r)"
wts_updates[36920] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Отказ от дипломатической экспансии в пользу укрепления классической армии Орды.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Снижает общее потребление ресурсов на |cff60dc7015%|cffced4da.|n"
    "- |cffdc6060Закрывает доступ к присоединению других рас.|r"
)
checks_def.append({"type": "upgrade", "id": "R0DW", "field": "name1", "expected": wts_updates[36238]})
checks_def.append({"type": "upgrade", "id": "R0DW", "field": "tip1", "expected": wts_updates[40585]})
checks_def.append({"type": "upgrade", "id": "R0DW", "field": "ubertip1", "expected": wts_updates[36920]})

# R0DX: Воссоединение орков (E)
wts_updates[40586] = "|cffe4cfa3Воссоединение орков|r"
wts_updates[40587] = "|cffe4cfa3Воссоединение орков|r (|cffffffffE|r)"
wts_updates[1350] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Объединение разрозненных орочьих кланов Восточных королевств под знаменем Орды.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает ветки присоединения орочьих кланов (Черная Гора, Драконья Пасть, Кор'Крон).|n"
    "- |cffdc6060Блокирует исследование «Отказаться от Расширения».|r"
)
checks_def.append({"type": "upgrade", "id": "R0DX", "field": "name1", "expected": wts_updates[40586]})
checks_def.append({"type": "upgrade", "id": "R0DX", "field": "tip1", "expected": wts_updates[40587]})
checks_def.append({"type": "upgrade", "id": "R0DX", "field": "ubertip1", "expected": wts_updates[1350]})

# R0DY: Поиск союзников (Q)
wts_updates[36239] = "|cffe4cfa3Поиск союзников|r"
wts_updates[40588] = "|cffe4cfa3Поиск союзников|r (|cffffffffQ|r)"
wts_updates[22930] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Установление дипломатических связей с другими народами Азерота.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает ветки присоединения Отрекшихся, эльфов крови и пандаренов.|n"
    "- |cffdc6060Блокирует исследование «Отказаться от Расширения».|r"
)
checks_def.append({"type": "upgrade", "id": "R0DY", "field": "name1", "expected": wts_updates[36239]})
checks_def.append({"type": "upgrade", "id": "R0DY", "field": "tip1", "expected": wts_updates[40588]})
checks_def.append({"type": "upgrade", "id": "R0DY", "field": "ubertip1", "expected": wts_updates[22930]})

# R0DZ: Вопросы безопасности (W)
wts_updates[40589] = "|cffe4cfa3Вопросы безопасности|r"
wts_updates[40590] = "|cffe4cfa3Вопросы безопасности|r (|cffffffffW|r)"
wts_updates[22944] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепление обороны Орды за счёт договоров с нейтральными фракциями и наёмниками.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает ветки присоединения гоблинов, магнатавров и рыцарей смерти.|n"
    "- |cffdc6060Блокирует исследование «Отказаться от Расширения».|r"
)
checks_def.append({"type": "upgrade", "id": "R0DZ", "field": "name1", "expected": wts_updates[40589]})
checks_def.append({"type": "upgrade", "id": "R0DZ", "field": "tip1", "expected": wts_updates[40590]})
checks_def.append({"type": "upgrade", "id": "R0DZ", "field": "ubertip1", "expected": wts_updates[22944]})

# R0E0: Усилить Кор'Крон (E)
wts_updates[36240] = "|cffe4cfa3Усилить Кор'Крон|r"
wts_updates[22999] = "|cffe4cfa3Усилить Кор'Крон|r (|cffffffffE|r)"
wts_updates[36921] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Превращает личную гвардию вождя в полноценный ударный корпус элитных воинов.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает элитных бойцов |cffa9c7deВоин Кор'Крона|cffced4da.|n"
    "- Повышает расходы на содержание на |cffdc60605%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0E0", "field": "name1", "expected": wts_updates[36240]})
checks_def.append({"type": "upgrade", "id": "R0E0", "field": "tip1", "expected": wts_updates[22999]})
checks_def.append({"type": "upgrade", "id": "R0E0", "field": "ubertip1", "expected": wts_updates[36921]})

# R0E1: Связаться с кланом Драконьей Пасти (E)
wts_updates[36241] = "|cffe4cfa3Связаться с кланом Драконьей Пасти|r"
wts_updates[40591] = "|cffe4cfa3Связаться с кланом Драконьей Пасти|r (|cffffffffE|r)"
wts_updates[36922] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Привлечение в Орду орков клана Драконьей Пасти вместе с их наездниками.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает наездников на драконах и тяжелую пехоту клана.|n"
    "- Снижает затраты на содержание на |cff60dc704%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0E1", "field": "name1", "expected": wts_updates[36241]})
checks_def.append({"type": "upgrade", "id": "R0E1", "field": "tip1", "expected": wts_updates[40591]})
checks_def.append({"type": "upgrade", "id": "R0E1", "field": "ubertip1", "expected": wts_updates[36922]})

# R0E3: Дом Рыцарям смерти (X)
wts_updates[40592] = "|cffe4cfa3Дом Рыцарям смерти|r"
wts_updates[40593] = "|cffe4cfa3Дом Рыцарям смерти|r (|cffffffffX|r)"
wts_updates[36923] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Предоставляет убежище свободным рыцарям смерти в рядах Орды.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает элитных воинов |cffa9c7deРыцарь смерти|cffced4da.|n"
    "- Повышает расходы на содержание на |cffdc60601%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0E3", "field": "name1", "expected": wts_updates[40592]})
checks_def.append({"type": "upgrade", "id": "R0E3", "field": "tip1", "expected": wts_updates[40593]})
checks_def.append({"type": "upgrade", "id": "R0E3", "field": "ubertip1", "expected": wts_updates[36923]})

# R0E4: Сделка с Гоблинами (W)
wts_updates[36242] = "|cffe4cfa3Сделка с Гоблинами|r"
wts_updates[40594] = "|cffe4cfa3Сделка с Гоблинами|r (|cffffffffW|r)"
wts_updates[36924] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заключает торговый и военный пакт с картелем Трюмных Вод.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает гоблинских стрелков, уничтожителей-3000 и боевые катера.|n"
    "- Повышает расходы на содержание на |cffdc60602%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0E4", "field": "name1", "expected": wts_updates[36242]})
checks_def.append({"type": "upgrade", "id": "R0E4", "field": "tip1", "expected": wts_updates[40594]})
checks_def.append({"type": "upgrade", "id": "R0E4", "field": "ubertip1", "expected": wts_updates[36924]})

# R0E5: Подчинить Магнатавров (S)
wts_updates[36243] = "|cffe4cfa3Подчинить Магнатавров|r"
wts_updates[40595] = "|cffe4cfa3Подчинить Магнатавров|r (|cffffffffS|r)"
wts_updates[36925] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Подчинение свирепых нордскольких магнатавров для войны на передовой.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает сверхтяжелых воинов |cffa9c7deМагнатавр|cffced4da.|n"
    "- Повышает расходы на содержание на |cffdc60602%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0E5", "field": "name1", "expected": wts_updates[36243]})
checks_def.append({"type": "upgrade", "id": "R0E5", "field": "tip1", "expected": wts_updates[40595]})
checks_def.append({"type": "upgrade", "id": "R0E5", "field": "ubertip1", "expected": wts_updates[36925]})

# R0E7: Фракция с магами (урон)
wts_updates[36244] = "|cffe4cfa3Фракция с магами (урон)|r"
wts_updates[3802] = "|cffe4cfa3Фракция с магами (урон)|r"

# R0E8: Фракция с особой техникой
wts_updates[36245] = "|cffe4cfa3Фракция с особой техникой|r"
wts_updates[4084] = "|cffe4cfa3Фракция с особой техникой|r"

# R0E9: Сформировать Истинную Орду (E)
wts_updates[24790] = "|cffe4cfa3Сформировать Истинную Орду|r"
wts_updates[36246] = "|cffe4cfa3Сформировать Истинную Орду|r (|cffffffffE|r)"
wts_updates[36926] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Объединение всех орочьих сил в непреклонную Истинную Орду.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает доступ к постройке Железной Орды или призыву сил Ша.|n"
    "- Значительно усиливает боевой дух и натиск воинов.|r"
)
checks_def.append({"type": "upgrade", "id": "R0E9", "field": "name1", "expected": wts_updates[24790]})
checks_def.append({"type": "upgrade", "id": "R0E9", "field": "tip1", "expected": wts_updates[36246]})
checks_def.append({"type": "upgrade", "id": "R0E9", "field": "ubertip1", "expected": wts_updates[36926]})

# R0EA: Начать строительство Железной Орды (E)
wts_updates[36232] = "|cffe4cfa3Начать строительство Железной Орды|r"
wts_updates[40608] = "|cffe4cfa3Начать строительство Железной Орды|r (|cffffffffE|r)"
wts_updates[36927] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Индустриализация Орды: переход на тяжелое машиностроение, пушки и бронированную пехоту.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Заменяет рубак на |cffa9c7deОсновной воин Орды|cffced4da (Железный рубака).|n"
    "- Заменяет стрелков на |cffa9c7deОсновной стрелок Орды|cffced4da (Железный стрелок).|n"
    "- Открывает производство |cffa9c7deЖелезная звезда|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0EA", "field": "name1", "expected": wts_updates[36232]})
checks_def.append({"type": "upgrade", "id": "R0EA", "field": "tip1", "expected": wts_updates[40608]})
checks_def.append({"type": "upgrade", "id": "R0EA", "field": "ubertip1", "expected": wts_updates[36927]})

# R0EB: Ювелирное мастерство (Z)
wts_updates[23324] = "|cffe4cfa3Ювелирное мастерство|r"
wts_updates[23327] = "|cffe4cfa3Ювелирное мастерство|r (|cffffffffZ|r)"
wts_updates[23330] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Изучение ювелирного дела и обработки драгоценных камней для зачарования экипировки.|r"
)
checks_def.append({"type": "upgrade", "id": "R0EB", "field": "name1", "expected": wts_updates[23324]})
checks_def.append({"type": "upgrade", "id": "R0EB", "field": "tip1", "expected": wts_updates[23327]})

# R0EE: Пандаренский вопрос (Q)
wts_updates[36249] = "|cffe4cfa3Пандаренский вопрос|r"
wts_updates[36929] = "|cffe4cfa3Пандаренский вопрос|r (|cffffffffQ|r)"
wts_updates[36928] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заключение союза с монахами ордена Шадо-Пан из Пандарии.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает элитных рукопашных бойцов |cffa9c7deВоин Шадо-Пан|cffced4da.|n"
    "- Снижает затраты на содержание на |cff60dc702%|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0EE", "field": "name1", "expected": wts_updates[36249]})
checks_def.append({"type": "upgrade", "id": "R0EE", "field": "tip1", "expected": wts_updates[36929]})
checks_def.append({"type": "upgrade", "id": "R0EE", "field": "ubertip1", "expected": wts_updates[36928]})

# R0EH: Орда - общий дом (Q)
wts_updates[36233] = "|cffe4cfa3Орда — общий дом|r"
wts_updates[40612] = "|cffe4cfa3Орда — общий дом|r (|cffffffffQ|r)"
wts_updates[36930] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Провозглашение Орды единым домом для всех свободных рас.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает доступ к союзу с зандаларскими троллями и ночнорождёнными Сурамара.|r"
)
checks_def.append({"type": "upgrade", "id": "R0EH", "field": "name1", "expected": wts_updates[36233]})
checks_def.append({"type": "upgrade", "id": "R0EH", "field": "tip1", "expected": wts_updates[40612]})
checks_def.append({"type": "upgrade", "id": "R0EH", "field": "ubertip1", "expected": wts_updates[36930]})

# R0EI: Дорога к компромису (W)
wts_updates[40613] = "|cffe4cfa3Дорога к компромису|r"
wts_updates[40614] = "|cffe4cfa3Дорога к компромису|r (|cffffffffW|r)"
wts_updates[36931] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Поиск сбалансированного компромисса между экспансией и традициями Орды.|r"
)
checks_def.append({"type": "upgrade", "id": "R0EI", "field": "name1", "expected": wts_updates[40613]})
checks_def.append({"type": "upgrade", "id": "R0EI", "field": "tip1", "expected": wts_updates[40614]})

# R0F3: Присоединение Зандаларов (Q)
wts_updates[36250] = "|cffe4cfa3Присоединение Зандаларов|r"
wts_updates[40615] = "|cffe4cfa3Присоединение Зандаларов|r (|cffffffffQ|r)"
wts_updates[36932] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Вхождение древней империи Зандалар в состав Орды.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает зандаларский тяжелый боевой корабль |cffa9c7deГордость Зандалара|cffced4da.|n"
    "- Дарует благословение Лоа союзным войскам.|r"
)
checks_def.append({"type": "upgrade", "id": "R0F3", "field": "name1", "expected": wts_updates[36250]})
checks_def.append({"type": "upgrade", "id": "R0F3", "field": "tip1", "expected": wts_updates[40615]})
checks_def.append({"type": "upgrade", "id": "R0F3", "field": "ubertip1", "expected": wts_updates[36932]})

# R0F4: Принять Сурамарцев (W)
wts_updates[36251] = "|cffe4cfa3Принять Сурамарцев|r"
wts_updates[40616] = "|cffe4cfa3Принять Сурамарцев|r (|cffffffffW|r)"
wts_updates[36933] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Союз с ночнорождёнными Сурамара и открытие их тайных чар.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Открывает магов-чародеев Сурамара и элитные технологии Ночнорождённых.|r"
)
checks_def.append({"type": "upgrade", "id": "R0F4", "field": "name1", "expected": wts_updates[36251]})
checks_def.append({"type": "upgrade", "id": "R0F4", "field": "tip1", "expected": wts_updates[40616]})
checks_def.append({"type": "upgrade", "id": "R0F4", "field": "ubertip1", "expected": wts_updates[36933]})

# R0KO: Использовать Сердце И'Шараджа (E)
wts_updates[21998] = "|cffe4cfa3Использовать Сердце И'Шараджа|r"
wts_updates[22034] = "|cffe4cfa3Использовать Сердце И'Шараджа|r (|cffffffffE|r)"
wts_updates[23115] = (
    "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Высвобождение скверны Древнего Бога И'Шараджа для наделения воинов темной мощью.|n|n"
    "|cffa6afb8Эффект:|cffced4da|n- Дарует войскам способность |cffa9c7deВоин Ша|cffced4da.|n"
    "- Открывает способность |cffa9c7deСнаряд Ша|cffced4da у осадных орудий.|n"
    "- При атаке порождает |cffa9c7deОтголоски Ненависти|cffced4da.|r"
)
checks_def.append({"type": "upgrade", "id": "R0KO", "field": "name1", "expected": wts_updates[21998]})
checks_def.append({"type": "upgrade", "id": "R0KO", "field": "tip1", "expected": wts_updates[22034]})
checks_def.append({"type": "upgrade", "id": "R0KO", "field": "ubertip1", "expected": wts_updates[23115]})

# =========================================================================
# 6. HERO & UNIT ABILITIES
# =========================================================================

# --- 6.1 Hero Abilities ---
# A12F: Боевой рев (W) - Blademaster
wts_updates[36103] = "|cffe4cfa3Боевой рев|r"
wts_updates[36104] = "|cffe4cfa3Боевой рев|r [|cffffffff1-й уровень|r] (|cffffffffW|r)"
wts_updates[36105] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издает боевой клич, увеличивающий урон союзников поблизости на |cff60dc70+25%|cffced4da на |cffffffff30|cffced4da сек.|r"
wts_updates[36106] = "|cffe4cfa3Боевой рев|r [|cffffffff2-й уровень|r] (|cffffffffW|r)"
wts_updates[36107] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издает боевой клич, увеличивающий урон союзников поблизости на |cff60dc70+50%|cffced4da на |cffffffff30|cffced4da сек.|r"
wts_updates[36108] = "|cffe4cfa3Боевой рев|r [|cffffffff3-й уровень|r] (|cffffffffW|r)"
wts_updates[36109] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издает боевой клич, увеличивающий урон союзников поблизости на |cff60dc70+75%|cffced4da на |cffffffff30|cffced4da сек.|r"
wts_updates[36112] = "|cffe4cfa3Боевой рев|r [|cffffffff4-й уровень|r] (|cffffffffW|r)"
checks_def.append({"type": "ability", "id": "A12F", "field": "name", "expected": wts_updates[36103]})

# A12E: Муссон (R) - Farseer
wts_updates[24599] = "|cffe4cfa3Муссон|r"
wts_updates[24600] = "|cffe4cfa3Муссон|r [|cffffffff1-й уровень|r] (|cffffffffR|r)"
wts_updates[24601] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает грозовой шквал молний, наносящий периодический урон врагам в области действия.|r"
wts_updates[24602] = "|cffe4cfa3Муссон|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
checks_def.append({"type": "ability", "id": "A12E", "field": "name", "expected": wts_updates[24599]})

# A12M: За Орду! (W) - Garrosh
wts_updates[23649] = "|cffe4cfa3За Орду!|r"
garrosh_w_tips = [23650, 23652, 23654, 23656]
for i, sid in enumerate(garrosh_w_tips, 1):
    wts_updates[sid] = f"|cffe4cfa3За Орду!|r [|cffffffff{i}-й уровень|r] (|cffffffffW|r)"
garrosh_w_ubs = [23651, 23653, 23655]
for sid in garrosh_w_ubs:
    wts_updates[sid] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Воодушевляет войска вокруг, значительно повышая их скорость передвижения и атаки.|r"
checks_def.append({"type": "ability", "id": "A12M", "field": "name", "expected": wts_updates[23649]})

# A12N: Рассекающий удар (W) - Garrosh
wts_updates[24708] = "|cffe4cfa3Рассекающий удар|r"
for i, sid in enumerate([24709, 24711, 24713, 24715], 1):
    wts_updates[sid] = f"|cffe4cfa3Рассекающий удар|r [|cffffffff{i}-й уровень|r]"
wts_updates[24710] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит сокрушительный удар, поражающий врагов поблизости от основной цели на |cffffffff7%|cffced4da урона.|r"
wts_updates[24712] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит сокрушительный удар, поражающий врагов поблизости от основной цели на |cffffffff12%|cffced4da урона.|r"
wts_updates[24714] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит сокрушительный удар, поражающий врагов поблизости от основной цели на |cffffffff17%|cffced4da урона.|r"
checks_def.append({"type": "ability", "id": "A12N", "field": "name", "expected": wts_updates[24708]})

# A12O: Призвать Охрану (Q) - Garrosh
wts_updates[24401] = "|cffe4cfa3Призвать Охрану|r"
for i, sid in enumerate([24402, 24404, 24406, 24408], 1):
    wts_updates[sid] = f"|cffe4cfa3Призвать Охрану|r [|cffffffff{i}-й уровень|r] (|cffffffffQ|r)"
for sid in [24403, 24405, 24407]:
    wts_updates[sid] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь верных воинов Кор'Крона.|r"
checks_def.append({"type": "ability", "id": "A12O", "field": "name", "expected": wts_updates[24401]})

# A12P: Ярость Адского Крика (R) - Garrosh
wts_updates[24742] = "|cffe4cfa3Ярость Адского Крика|r"
wts_updates[24743] = "|cffe4cfa3Ярость Адского Крика|r [|cffffffff1-й уровень|r] (|cffffffffR|r)"
wts_updates[24744] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Гаррош впадает в неистовую ярость, получая бонус к броне, здоровью, урону и |cffffffff50%|cffced4da защиту от магии на |cffffffff40|cffced4da сек.|r"
)
wts_updates[24745] = "|cffe4cfa3Ярость Адского Крика|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
checks_def.append({"type": "ability", "id": "A12P", "field": "name", "expected": wts_updates[24742]})

# A12X: Цепная молния (Q) - Thrall
wts_updates[23661] = "|cffe4cfa3Цепная молния|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)"
wts_updates[23662] = "|cffe4cfa3Цепная молния|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)"
wts_updates[23663] = "|cffe4cfa3Цепная молния|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)"
wts_updates[23664] = "|cffe4cfa3Цепная молния|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)"

# A12Z: Земляные оковы (W) - Thrall
wts_updates[3149] = "|cffe4cfa3Земляные оковы|r"
for i, sid in enumerate([3150, 3152, 3154, 3156], 1):
    wts_updates[sid] = f"|cffe4cfa3Земляные оковы|r [|cffffffff{i}-й уровень|r] (|cffffffffW|r)"
for sid in [3151, 3153, 3155]:
    wts_updates[sid] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает силу земли, сковывая и обездвиживая врагов в выбранной области.|r"
checks_def.append({"type": "ability", "id": "A12Z", "field": "name", "expected": wts_updates[3149]})

# A130: Испепеление (R) - Thrall
wts_updates[25570] = "|cffe4cfa3Испепеление|r"
wts_updates[25571] = "|cffe4cfa3Испепеление|r [|cffffffff1-й уровень|r] (|cffffffffR|r)"
wts_updates[25572] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает колоссальный разряд стихийного пламени, наносящий огромный урон цели и ближайшим врагам.|r"
wts_updates[25573] = "|cffe4cfa3Испепеление|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
checks_def.append({"type": "ability", "id": "A130", "field": "name", "expected": wts_updates[25570]})

# A14V: Цепная молния (Q) - Dummy
wts_updates[36910] = "|cffe4cfa3Цепная молния|r"
for i, sid in enumerate([36911, 36913, 36915, 36934], 1):
    wts_updates[sid] = f"|cffe4cfa3Цепная молния|r [|cffffffff{i}-й уровень|r]"

# A12L, A12Y: Bloodlust / Firebolt triggers
wts_updates[39010] = "|cffe4cfa3Жажда крови|r"
wts_updates[39011] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения и атаки союзника.|r"
wts_updates[23665] = "|cffe4cfa3Огненная стрела|r"
wts_updates[23666] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток пламени, оглушающий цель.|r"

# --- 6.2 Unit Abilities ---
# A0ZA: Скрытая ярость
wts_updates[36869] = "|cffe4cfa3Скрытая ярость|r"
wts_updates[36870] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff4%|cffced4da при получении урона боец впадает в ярость, получая бонус к скорости атаки и перемещения.|r"
)
checks_def.append({"type": "ability", "id": "A0ZA", "field": "name", "expected": wts_updates[36869]})

# A0ZB: Опутывание (Q)
wts_updates[24788] = "|cffe4cfa3Опутывание|r"
wts_updates[24789] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Набрасывает прочную сеть, притягивая летающих врагов к земле и обездвиживая цель на |cffffffff8|cffced4da сек.|r"
)
checks_def.append({"type": "ability", "id": "A0ZB", "field": "name", "expected": wts_updates[24788]})

# A0ZC: Состояние берсерка
wts_updates[36871] = "|cffe4cfa3Состояние берсерка|r"
wts_updates[36872] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff10%|cffced4da при атаке боец впадает в состояние берсерка: увеличивает скорость атаки, но получает повышенный урон.|r"
)
checks_def.append({"type": "ability", "id": "A0ZC", "field": "name", "expected": wts_updates[36871]})

# A0ZX: Пламенное дыхание (Q)
wts_updates[36884] = "|cffe4cfa3Пламенное дыхание|r"
wts_updates[36885] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выдыхает конус пламени, нанося |cffffffff30|cffced4da ед. урона врагам перед собой. С шансом |cffffffff8%|cffced4da срабатывает автоматически при атаке.|r"
)
checks_def.append({"type": "ability", "id": "A0ZX", "field": "name", "expected": wts_updates[36884]})

# A103: Запустить протокол подрыва (Q)
wts_updates[36891] = "|cffe4cfa3Запустить протокол подрыва|r"
wts_updates[36892] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Значительно повышает скорость перемещения, но механизм гарантированно взрывается через |cffffffff10|cffced4da сек., нанося сокрушительный урон.|r"
)
checks_def.append({"type": "ability", "id": "A103", "field": "name", "expected": wts_updates[36891]})

# A124: Антимагический щит (Q)
wts_updates[39014] = "|cffe4cfa3Антимагический щит|r"
wts_updates[39015] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзника барьером тьмы, поглощающим до |cffffffff300|cffced4da ед. магического урона.|r"
)
checks_def.append({"type": "ability", "id": "A124", "field": "name", "expected": wts_updates[39014]})

# A129: Неожиданный удар
wts_updates[36907] = "|cffe4cfa3Неожиданный удар|r"
wts_updates[36909] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Скрытная атака, наносящая два быстрых удара подряд.|r"
checks_def.append({"type": "ability", "id": "A129", "field": "name", "expected": wts_updates[36907]})

# A1LO, A1MG: Жажда крови
wts_updates[39019] = "|cffe4cfa3Жажда крови|r"
wts_updates[39020] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки и перемещения цели.|r"
wts_updates[39202] = "|cffe4cfa3Жажда крови|r"
wts_updates[39203] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки и перемещения цели.|r"

# A1OJ: Воин Ша (D)
wts_updates[10871] = "|cffe4cfa3Воин Ша|r"
wts_updates[10872] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cff60dc70+20%|cffced4da к скорости атаки и перемещения, но повышает получаемый урон на |cffdc606020%|cffced4da. При атаке с шансом |cffffffff1%|cffced4da порождает Отголоски Ненависти.|r"
)
checks_def.append({"type": "ability", "id": "A1OJ", "field": "name", "expected": wts_updates[10871]})

# A1OK: Снаряд Ша (R)
wts_updates[11397] = "|cffe4cfa3Снаряд Ша|r"
wts_updates[11398] = (
    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает сгусток скверны Ша, поражающий врагов по области. Снижает броню на |cffdc60603|cffced4da и наносит |cffffffff5|cffced4da урона/сек. на |cffffffff15|cffced4da сек.|r"
)
checks_def.append({"type": "ability", "id": "A1OK", "field": "name", "expected": wts_updates[11397]})

# A13H: Берсек
wts_updates[9930] = "|cffe4cfa3Берсерк|r"
# A13I: Бонус к скорости атаки 50%
wts_updates[9960] = "|cffa6afb8Бонус к скорости атаки 50%|r"

# =========================================================================
# 7. BUFFS
# =========================================================================
# B05V: Жажда крови
wts_updates[30280] = "|cffe4cfa3Жажда крови|r"
wts_updates[6835] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и атаки воина значительно увеличены.|r"

# B06E: Оковы
wts_updates[22410] = "|cffe4cfa3Земляные оковы|r"

# B06F: Воин Ша
wts_updates[25347] = "|cffe4cfa3Воин Ша|r"
wts_updates[25348] = "|cffa6afb8ЭФФЕКТ:|cffced4da Юнит наделён силой Ша: увеличена скорость боя, но снижена сопротивляемость урону.|r"

# B08G, B08H: Снаряд Ша
wts_updates[11656] = "|cffe4cfa3Снаряд Ша|r"
wts_updates[11658] = "|cffa6afb8ЭФФЕКТ:|cffced4da Броня снижена, юнит получает периодический урон от скверны Ша.|r"
wts_updates[11663] = "|cffe4cfa3Снаряд Ша|r"

# BNbf: Боевой рев
wts_updates[30814] = "|cffe4cfa3Боевой рев|r"

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)
    plan_file = folder / "horde_plan.json"

    # Verify all updated SIDs exist in war3map.wts
    missing_sids = [sid for sid in wts_updates if not check_wts_has(sid)]
    if missing_sids:
        print(f"ERROR: {len(missing_sids)} SIDs not found in war3map.wts: {missing_sids[:10]}")
        sys.exit(1)

    payload = {
        "race": "Horde",
        "total_wts_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "metadata": {
            "categories": {
                "selection": 1,
                "selection_markers": 3,
                "buildings": 14,
                "heroes": 7,
                "units": len(units_data),
                "researches": 37,
                "abilities": 25,
                "buffs": 6
            },
            "total_checks": len(checks_def)
        }
    }

    plan_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Horde standardization plan successfully written to {plan_file}")
    print(f"Total WTS updates: {len(wts_updates)}")
    print(f"Total checks planned: {len(checks_def)}")

if __name__ == "__main__":
    main()
