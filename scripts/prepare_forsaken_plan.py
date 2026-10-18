# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Forsaken race (Race 27)."""
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
    # 1. RACE SELECTION: A155, R0G3
    # =========================================================================
    # A155
    wts_updates[38903] = "|cffe4cfa3Отрекшиеся|r"
    wts_updates[38904] = "|cffe4cfa3Отрекшиеся|r (|cffffffffD|r)"
    wts_updates[25784] = (
        "|cffa6afb8РАСА:|cffced4da Мятежная нежить, освободившаяся от власти Короля-лича под предводительством Сильваны Ветрокрылой.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Classic — Legion»|r|n|n"
        "|cffced4daОтрекшиеся — фракция разумной нежити, сбросившая оковы Плети и отвоевавшая руины Лордерона в ходе Третьей войны. "
        "Обосновавшись в мрачных катакомбах Подгорода под знамёнами Тёмной Госпожи Сильваны Ветрокрылой, Отрекшиеся сражаются за выживание "
        "своего народа, применяя смертоносные штаммы гнили, тёмную магию следопытов и алхимию ядов.|r"
    )
    checks_def.append({"type": "ability", "id": "A155", "field": "name", "expected": wts_updates[38903]})
    checks_def.append({"type": "ability", "id": "A155", "field": "tip1", "expected": wts_updates[38904]})
    checks_def.append({"type": "ability", "id": "A155", "field": "ubertip1", "expected": wts_updates[25784]})

    # Marker: R0G3
    wts_updates[11618] = "|cffe4cfa3Отрекшиеся|r"
    wts_updates[15431] = "|cffe4cfa3Отрекшиеся|r"
    wts_updates[20163] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Отрекшимся (Подгород).|r"
    checks_def.append({"type": "upgrade", "id": "R0G3", "field": "name1", "expected": wts_updates[11618]})
    checks_def.append({"type": "upgrade", "id": "R0G3", "field": "tip1", "expected": wts_updates[15431]})
    checks_def.append({"type": "upgrade", "id": "R0G3", "field": "ubertip1", "expected": wts_updates[20163]})

    # =========================================================================
    # 2. BUILDINGS (11 Forsaken buildings)
    # =========================================================================
    # h0JP: Ратуша (Q)
    wts_updates[33955] = "|cffe4cfa3Ратуша|r"
    wts_updates[33956] = "|cffe4cfa3Ратуша|r (|cffffffffQ|r)"
    wts_updates[35934] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Отрекшихся первой ступени. Обеспечивает добычу ресурсов и базовый запас пищи.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da: рабочий отряд расы.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКрепость|cffced4da: открывает доступ к продвинутым технологиям и войскам.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JP", "field": "name", "expected": wts_updates[33955]})
    checks_def.append({"type": "unit", "id": "h0JP", "field": "tip", "expected": wts_updates[33956]})
    checks_def.append({"type": "unit", "id": "h0JP", "field": "ubertip", "expected": wts_updates[35934]})

    # h0JQ: Крепость (Z)
    wts_updates[33957] = "|cffe4cfa3Крепость|r"
    wts_updates[33958] = "|cffe4cfa3Крепость|r (|cffffffffZ|r)"
    wts_updates[31895] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Отрекшихся второй ступени. Существенно увеличивает запас пищи и открывает передовые сооружения.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da: рабочий отряд расы.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deБастион|cffced4da: открывает доступ к высшим технологиям и защите столицы.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JQ", "field": "name", "expected": wts_updates[33957]})
    checks_def.append({"type": "unit", "id": "h0JQ", "field": "tip", "expected": wts_updates[33958]})
    checks_def.append({"type": "unit", "id": "h0JQ", "field": "ubertip", "expected": wts_updates[31895]})

    # h0JL: Бастион (Z)
    wts_updates[33949] = "|cffe4cfa3Бастион|r"
    wts_updates[33950] = "|cffe4cfa3Бастион|r (|cffffffffZ|r)"
    wts_updates[31890] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Отрекшихся третьей ступени. Обеспечивает максимальный запас пищи и защиту королевства.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da: рабочий отряд расы.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JL", "field": "name", "expected": wts_updates[33949]})
    checks_def.append({"type": "unit", "id": "h0JL", "field": "tip", "expected": wts_updates[33950]})
    checks_def.append({"type": "unit", "id": "h0JL", "field": "ubertip", "expected": wts_updates[31890]})

    # h0JD: Дом Брошенных (A)
    wts_updates[33941] = "|cffe4cfa3Дом Брошенных|r"
    wts_updates[33942] = "|cffe4cfa3Дом Брошенных|r (|cffffffffA|r)"
    wts_updates[31786] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Жилое сооружение Отрекшихся. Обеспечивает запас пищи и приносит регулярный доход в казну.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит |cffffffff+20|cffced4da ед. дохода каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JD", "field": "name", "expected": wts_updates[33941]})
    checks_def.append({"type": "unit", "id": "h0JD", "field": "tip", "expected": wts_updates[33942]})
    checks_def.append({"type": "unit", "id": "h0JD", "field": "ubertip", "expected": wts_updates[31786]})

    # h0JJ: Казармы (W)
    wts_updates[33945] = "|cffe4cfa3Казармы|r"
    wts_updates[33946] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[31888] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает базовые пехотные и стрелковые силы армии Отрекшихся.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deМёртвый воин|cffced4da: лёгкий боец ближнего боя с каннибализмом.|n"
        "- |cffa9c7deЛучница|cffced4da: стрелок дальнего боя с отравленными стрелами.|n"
        "- |cffa9c7deТёмный следопыт|cffced4da: элитный стрелок дальнего боя с отравленным кинжалом.|n"
        "- |cffa9c7deСтраж Смерти|cffced4da: тяжёлый пехотинец с защитной стойкой и замедляющей поступью.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deСмертоносные ингредиенты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JJ", "field": "name", "expected": wts_updates[33945]})
    checks_def.append({"type": "unit", "id": "h0JJ", "field": "tip", "expected": wts_updates[33946]})
    checks_def.append({"type": "unit", "id": "h0JJ", "field": "ubertip", "expected": wts_updates[31888]})

    # h0JI: Лаборатория (R)
    wts_updates[33943] = "|cffe4cfa3Лаборатория|r"
    wts_updates[33944] = "|cffe4cfa3Лаборатория|r (|cffffffffR|r)"
    wts_updates[31887] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Производственный и исследовательский центр боевых штаммов чумы и осадных орудий Отрекшихся.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deГнилевозка|cffced4da: осадное орудие дальнего боя с выбором типа чумы.|n"
        "- |cffa9c7deВождь Орды|cffced4da: могучий командир поддержки с чумным облаком.|n"
        "- |cffa9c7deУлучшенная Гнилевозка|cffced4da: передовая осадная машина с усиленными штаммами гнили.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deЭксперименты с Гнилью|cffced4da|n"
        "- |cffa9c7deМетоды Изоляции|cffced4da|n"
        "- |cffa9c7deУсилить смертоносность|cffced4da|n"
        "- |cffa9c7deУлучшенные поршни|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JI", "field": "name", "expected": wts_updates[33943]})
    checks_def.append({"type": "unit", "id": "h0JI", "field": "tip", "expected": wts_updates[33944]})
    checks_def.append({"type": "unit", "id": "h0JI", "field": "ubertip", "expected": wts_updates[31887]})

    # h0JO: Кузница (E)
    wts_updates[33953] = "|cffe4cfa3Кузница|r"
    wts_updates[33954] = "|cffe4cfa3Кузница|r (|cffffffffE|r)"
    wts_updates[31893] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит складом древесины и центром кузнечных разработок оружия и доспехов Отрекшихся.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deЖелезные мечи|cffced4da|n"
        "- |cffa9c7deЖелезная броня|cffced4da|n"
        "- |cffa9c7deЖелезные снаряды|cffced4da|n"
        "- |cffa9c7deЛёгкая броня|cffced4da|n"
        "- |cffa9c7deМагическая практика|cffced4da|n"
        "- |cffa9c7deУлучшенные инструменты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JO", "field": "name", "expected": wts_updates[33953]})
    checks_def.append({"type": "unit", "id": "h0JO", "field": "tip", "expected": wts_updates[33954]})
    checks_def.append({"type": "unit", "id": "h0JO", "field": "ubertip", "expected": wts_updates[31893]})

    # h0JR: Алтарь Королевы (S)
    wts_updates[33965] = "|cffe4cfa3Алтарь Королевы|r"
    wts_updates[33966] = "|cffe4cfa3Алтарь Королевы|r (|cffffffffS|r)"
    wts_updates[31899] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Позволяет призывать и воскрешать героев Отрекшихся.|n|n"
        "|cffa6afb8Герои:|cffced4da|n"
        "- |cffa9c7deТёмный Следопыт|cffced4da: стрелок дальнего боя с немотой и похищением жизни.|n"
        "- |cffa9c7deАптекарь|cffced4da: алхимик поддержки с регенерацией, стимуляторами и рунами.|n"
        "- |cffa9c7deУстранитель|cffced4da: смертоносный убийца с невидимостью и критами.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JR", "field": "name", "expected": wts_updates[33965]})
    checks_def.append({"type": "unit", "id": "h0JR", "field": "tip", "expected": wts_updates[33966]})
    checks_def.append({"type": "unit", "id": "h0JR", "field": "ubertip", "expected": wts_updates[31899]})

    # h0JK: Мастерская смерти (D)
    wts_updates[33947] = "|cffe4cfa3Мастерская смерти|r"
    wts_updates[33948] = "|cffe4cfa3Мастерская смерти|r (|cffffffffD|r)"
    wts_updates[31889] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр подготовки магов, призраков и служителей культа смерти Отрекшихся.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deБанши|cffced4da: бесплотный дух с проклятием, пожиранием магии и подчинением.|n"
        "- |cffa9c7deМёртвый маг|cffced4da: заклинатель с тёмной стаей, огненным ливнем и вытягиванием жизни.|n"
        "- |cffa9c7deУбийца|cffced4da: невидимый диверсант со скрытностью и ядами.|n"
        "- |cffa9c7deВалькира|cffced4da: крылатая вестница смерти, способная воскрешать павших.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deПосвящение Банши|cffced4da|n"
        "- |cffa9c7deОбучение магов|cffced4da|n"
        "- |cffa9c7deОбучение Убийц|cffced4da|n"
        "- |cffa9c7deУсиление Валь'Кир|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JK", "field": "name", "expected": wts_updates[33947]})
    checks_def.append({"type": "unit", "id": "h0JK", "field": "tip", "expected": wts_updates[33948]})
    checks_def.append({"type": "unit", "id": "h0JK", "field": "ubertip", "expected": wts_updates[31889]})

    # h0JM: Башня (Z)
    wts_updates[33951] = "|cffe4cfa3Башня|r"
    wts_updates[33952] = "|cffe4cfa3Башня|r (|cffffffffZ|r)"
    wts_updates[31891] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое сторожевое укрепление Отрекшихся.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deОборонительная башня|cffced4da: оснащается мощным стрелковым орудием.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JM", "field": "name", "expected": wts_updates[33951]})
    checks_def.append({"type": "unit", "id": "h0JM", "field": "tip", "expected": wts_updates[33952]})
    checks_def.append({"type": "unit", "id": "h0JM", "field": "ubertip", "expected": wts_updates[31891]})

    # h0JZ: Оборонительная башня (Z)
    wts_updates[33968] = "|cffe4cfa3Оборонительная башня|r"
    wts_updates[33969] = "|cffe4cfa3Оборонительная башня|r (|cffffffffZ|r)"
    wts_updates[35935] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Укреплённая сторожевая башня, ведущая прицельный огонь по вражеским силам.|n|n"
        "Атакует |cffffffffназемные и воздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JZ", "field": "name", "expected": wts_updates[33968]})
    checks_def.append({"type": "unit", "id": "h0JZ", "field": "tip", "expected": wts_updates[33969]})
    checks_def.append({"type": "unit", "id": "h0JZ", "field": "ubertip", "expected": wts_updates[35935]})

    # =========================================================================
    # 3. HEROES (5 heroes)
    # =========================================================================
    # N059: Королева Отрекшихся (Сильвана Ветрокрылая)
    wts_updates[28906] = "|cffe4cfa3Королева Отрекшихся|r"
    wts_updates[25180] = "Сильвана Ветрокрылая"
    wts_updates[33972] = "|cffe4cfa3Королева Отрекшихся|r (|cffffffffZ|r)"
    wts_updates[33973] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарная предводительница Отрекшихся, повелевающая силами тьмы, призраков и нежити.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВоскрешение мёртвых|cffced4da: поднимает скелетов из трупов павших воинов.|n"
        "- |cffa9c7deПревратиться в Банши|cffced4da: принимает форму бесплотного духа с сокрушительным уроном.|n"
        "- |cffa9c7deТёмная стрела|cffced4da: наполняет выстрелы тёмной энергией, ослабляя броню цели.|n"
        "- |cffa9c7deАбсолютная немота|cffced4da: лишает врагов возможности творить заклинания.|n|n"
        "Атакует |cffffffffназемные и воздушные|cffced4da цели.|r"
    )
    wts_updates[33970] = "|cffe4cfa3Королева Отрекшихся|r"
    wts_updates[33971] = "|cffe4cfa3Королева Отрекшихся|r"
    checks_def.append({"type": "unit", "id": "N059", "field": "name", "expected": wts_updates[28906]})
    checks_def.append({"type": "unit", "id": "N059", "field": "propernames", "expected": wts_updates[25180]})
    checks_def.append({"type": "unit", "id": "N059", "field": "tip", "expected": wts_updates[33972]})
    checks_def.append({"type": "unit", "id": "N059", "field": "ubertip", "expected": wts_updates[33973]})

    # N05E: Королева Отрекшихся (Банши-форма)
    wts_updates[23533] = "|cffe4cfa3Королева Отрекшихся|r"
    wts_updates[26826] = "Сильвана Ветрокрылая"
    wts_updates[33976] = "|cffe4cfa3Королева Отрекшихся|r (|cffffffffZ|r)"
    wts_updates[33974] = "|cffe4cfa3Королева Отрекшихся|r"
    wts_updates[33975] = "|cffe4cfa3Королева Отрекшихся|r"
    checks_def.append({"type": "unit", "id": "N05E", "field": "name", "expected": wts_updates[23533]})
    checks_def.append({"type": "unit", "id": "N05E", "field": "propernames", "expected": wts_updates[26826]})

    # N058: Тёмный Следопыт (C)
    wts_updates[2246] = "|cffe4cfa3Тёмный Следопыт|r"
    wts_updates[25333] = "|cffe4cfa3Тёмный Следопыт|r (|cffffffffC|r)"
    wts_updates[24758] = "|cffe4cfa3Тёмный Следопыт|r"
    wts_updates[25184] = "|cffe4cfa3Тёмный Следопыт|r"
    checks_def.append({"type": "unit", "id": "N058", "field": "name", "expected": wts_updates[2246]})
    checks_def.append({"type": "unit", "id": "N058", "field": "tip", "expected": wts_updates[25333]})

    # O031: Аптекарь (X)
    wts_updates[20078] = "|cffe4cfa3Аптекарь|r"
    wts_updates[26513] = "Бакстер,Фрай,Хаммел"
    wts_updates[9465] = "|cffe4cfa3Аптекарь|r (|cffffffffX|r)"
    wts_updates[26514] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Мастер алхимии Королевского фармацевтического общества, создающий смертельные штаммы и защитные стимуляторы.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deАура Регенерации|cffced4da: ускоряет союзников и восстанавливает их здоровье.|n"
        "- |cffa9c7deСтимуляторы|cffced4da: повышает скорость атаки и бега выбранного союзника.|n"
        "- |cffa9c7deКислотная бомба|cffced4da: разъедает броню врагов и наносит периодический урон.|n"
        "- |cffa9c7deИзобрести руну|cffced4da: создаёт могущественную руну для усиления союзных сил.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    wts_updates[2247] = "|cffe4cfa3Аптекарь|r"
    wts_updates[7961] = "|cffe4cfa3Аптекарь|r"
    checks_def.append({"type": "unit", "id": "O031", "field": "name", "expected": wts_updates[20078]})
    checks_def.append({"type": "unit", "id": "O031", "field": "propernames", "expected": wts_updates[26513]})
    checks_def.append({"type": "unit", "id": "O031", "field": "tip", "expected": wts_updates[9465]})
    checks_def.append({"type": "unit", "id": "O031", "field": "ubertip", "expected": wts_updates[26514]})

    # O030: Устранитель (Z)
    wts_updates[1994] = "|cffe4cfa3Устранитель|r"
    wts_updates[27470] = "Уиндем,Грегори Чарльз,Давитт Хиксон,Виктор Уорд,Вильям Монтегю"
    wts_updates[2049] = "|cffe4cfa3Устранитель|r (|cffffffffZ|r)"
    wts_updates[3872] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Смертоносный клинок карателей Отрекшихся, специализирующийся на скрытных диверсиях и уничтожении одиночных целей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВсеобщий мрак|cffced4da: погружает союзные войска вокруг в невидимость.|n"
        "- |cffa9c7deОтравленный кинжал|cffced4da: наносит урон ядом и замедляет противника.|n"
        "- |cffa9c7deМастерство|cffced4da: даёт шанс уклониться от удара и нанести критический урон.|n"
        "- |cffa9c7deТанец ветра|cffced4da: дарует невидимость и ускорение с дополнительным уроном при выходе.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    wts_updates[2046] = "|cffe4cfa3Устранитель|r"
    wts_updates[2970] = "|cffe4cfa3Устранитель|r"
    checks_def.append({"type": "unit", "id": "O030", "field": "name", "expected": wts_updates[1994]})
    checks_def.append({"type": "unit", "id": "O030", "field": "propernames", "expected": wts_updates[27470]})
    checks_def.append({"type": "unit", "id": "O030", "field": "tip", "expected": wts_updates[2049]})
    checks_def.append({"type": "unit", "id": "O030", "field": "ubertip", "expected": wts_updates[3872]})

    # =========================================================================
    # 4. UNITS (20 units)
    # =========================================================================
    # h0J5: Строитель (Q)
    wts_updates[33936] = "|cffe4cfa3Строитель|r"
    wts_updates[33937] = "|cffe4cfa3Строитель|r (|cffffffffQ|r)"
    wts_updates[20377] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основной рабочий Отрекшихся. Добывает древесину, возводит и ремонтирует сооружения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещает строителя на короткое расстояние.|n"
        "- |cffa9c7deДобывать ресурсы|cffced4da: сбор ресурсов.|n"
        "- |cffa9c7deРемонтировать|cffced4da: починка зданий и техники.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0J5", "field": "name", "expected": wts_updates[33936]})
    checks_def.append({"type": "unit", "id": "h0J5", "field": "tip", "expected": wts_updates[33937]})
    checks_def.append({"type": "unit", "id": "h0J5", "field": "ubertip", "expected": wts_updates[20377]})

    # n04T: Мёртвый воин (Q)
    wts_updates[25176] = "|cffe4cfa3Мёртвый воин|r"
    wts_updates[26950] = "|cffe4cfa3Мёртвый воин|r (|cffffffffQ|r)"
    wts_updates[27201] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый лёгкий пехотинец ближнего боя армии Отрекшихся.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deКаннибализм|cffced4da: поедает труп для быстрого восполнения здоровья.|n"
        "- |cffa9c7deИзолирующая броня|cffced4da: снижает получаемый урон от ядов и гнили.|n"
        "- |cffa9c7deРазъедающий яд|cffced4da: наносит повышенный урон живым целям и технике.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n04T", "field": "name", "expected": wts_updates[25176]})
    checks_def.append({"type": "unit", "id": "n04T", "field": "tip", "expected": wts_updates[26950]})
    checks_def.append({"type": "unit", "id": "n04T", "field": "ubertip", "expected": wts_updates[27201]})

    # h0JC: Лучница (W)
    wts_updates[22462] = "|cffe4cfa3Лучница|r"
    wts_updates[26955] = "|cffe4cfa3Лучница|r (|cffffffffW|r)"
    wts_updates[31882] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый стрелок дальнего боя армии Отрекшихся.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deНакопительный яд|cffced4da: выстрелы отравляют жертву, замедляя и ослабляя её.|n"
        "- |cffa9c7deИзолирующая броня|cffced4da: снижает урон от ядов и чумы.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JC", "field": "name", "expected": wts_updates[22462]})
    checks_def.append({"type": "unit", "id": "h0JC", "field": "tip", "expected": wts_updates[26955]})
    checks_def.append({"type": "unit", "id": "h0JC", "field": "ubertip", "expected": wts_updates[31882]})

    # h0JN: Тёмный следопыт (R)
    wts_updates[25585] = "|cffe4cfa3Тёмный следопыт|r"
    wts_updates[26499] = "|cffe4cfa3Тёмный следопыт|r (|cffffffffR|r)"
    wts_updates[31892] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный дальнобойный стрелок следопытов Сильваны.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deКинжал теней|cffced4da: метает отравленный кинжал, замедляющий противника.|n"
        "- |cffa9c7deНакопительный яд|cffced4da: атаки накладывают суммирующийся токсичный эффект.|n"
        "- |cffa9c7deИзолирующая броня|cffced4da: защита от ядовитых эффектов.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JN", "field": "name", "expected": wts_updates[25585]})
    checks_def.append({"type": "unit", "id": "h0JN", "field": "tip", "expected": wts_updates[26499]})
    checks_def.append({"type": "unit", "id": "h0JN", "field": "ubertip", "expected": wts_updates[31892]})

    # n04U: Страж Смерти (E)
    wts_updates[25179] = "|cffe4cfa3Страж Смерти|r"
    wts_updates[26951] = "|cffe4cfa3Страж Смерти|r (|cffffffffE|r)"
    wts_updates[31878] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелобронированный пехотинец ближнего боя, сдерживающий натиск врага.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЗащита|cffced4da: прикрывается щитом, снижая урон от стрел.|n"
        "- |cffa9c7deТяжёлая поступь|cffced4da: сотрясает землю, оглушая находящихся рядом врагов.|n"
        "- |cffa9c7deСмердящий запах|cffced4da: замедляет скорость атаки и бега врагов вокруг.|n"
        "- |cffa9c7deКаннибализм|cffced4da: поедает труп для исцеления.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n04U", "field": "name", "expected": wts_updates[25179]})
    checks_def.append({"type": "unit", "id": "n04U", "field": "tip", "expected": wts_updates[26951]})
    checks_def.append({"type": "unit", "id": "n04U", "field": "ubertip", "expected": wts_updates[31878]})

    # o02X: Гнилевозка (Q)
    wts_updates[33938] = "|cffe4cfa3Гнилевозка|r"
    wts_updates[33939] = "|cffe4cfa3Гнилевозка|r (|cffffffffQ|r)"
    wts_updates[31880] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойная осадная машина, распыляющая штаммы чумы в зоне поражения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВыбор типа Гнили|cffced4da: переключение между обычной, коррозийной и ослабляющей чумой.|n"
        "- |cffa9c7deЗаряд Гнили|cffced4da: выпускает снаряд с выбранным болезнетворным составом.|n|n"
        "Атакует |cffffffffназемные цели и здания|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o02X", "field": "name", "expected": wts_updates[33938]})
    checks_def.append({"type": "unit", "id": "o02X", "field": "tip", "expected": wts_updates[33939]})
    checks_def.append({"type": "unit", "id": "o02X", "field": "ubertip", "expected": wts_updates[31880]})

    # u02C: Вождь Орды (W)
    wts_updates[22498] = "|cffe4cfa3Вождь Орды|r"
    wts_updates[26956] = "|cffe4cfa3Вождь Орды|r (|cffffffffW|r)"
    wts_updates[31883] = (
        "|cffa6afb8ЮНИТ:|cffced4da Громадный сшитый боец ближнего боя, поглощающий огромное количество урона.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deБолезнетворное облако|cffced4da: заражает окружающих врагов чумным газом.|n"
        "- |cffa9c7deКаннибализм|cffced4da: восполняет здоровье, пожирая трупы.|n"
        "- |cffa9c7deИзолирующая броня|cffced4da: снижает урон от токсинов.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u02C", "field": "name", "expected": wts_updates[22498]})
    checks_def.append({"type": "unit", "id": "u02C", "field": "tip", "expected": wts_updates[26956]})
    checks_def.append({"type": "unit", "id": "u02C", "field": "ubertip", "expected": wts_updates[31883]})

    # o02Y: Улучшенная Гнилевозка (E)
    wts_updates[33963] = "|cffe4cfa3Улучшенная Гнилевозка|r"
    wts_updates[33964] = "|cffe4cfa3Улучшенная Гнилевозка|r (|cffffffffE|r)"
    wts_updates[31898] = (
        "|cffa6afb8ЮНИТ:|cffced4da Усовершенствованная осадная машина Отрекшихся с усиленной чумной артиллерией.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВыбор типа Гнили|cffced4da: переключение между убийственной, заразной и заградительной чумой.|n"
        "- |cffa9c7deЗаряд Гнили|cffced4da: бомбардирует позиции врага смертоносными составами.|n|n"
        "Атакует |cffffffffназемные цели и здания|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o02Y", "field": "name", "expected": wts_updates[33963]})
    checks_def.append({"type": "unit", "id": "o02Y", "field": "tip", "expected": wts_updates[33964]})
    checks_def.append({"type": "unit", "id": "o02Y", "field": "ubertip", "expected": wts_updates[31898]})

    # n04Y: Банши (Q)
    wts_updates[33961] = "|cffe4cfa3Банши|r"
    wts_updates[33962] = "|cffe4cfa3Банши|r (|cffffffffQ|r)"
    wts_updates[31897] = (
        "|cffa6afb8ЮНИТ:|cffced4da Бесплотный летающий призрак поддержки, повелевающий душами и проклятиями.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deПроклятие|cffced4da: заставляет вражеские атаки промахиваться.|n"
        "- |cffa9c7deПожирание магии|cffced4da: развеивает чары и восстанавливает собственную ману.|n"
        "- |cffa9c7deОдержимость|cffced4da: вселяется во вражеского бойца и захватывает контроль над ним.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n04Y", "field": "name", "expected": wts_updates[33961]})
    checks_def.append({"type": "unit", "id": "n04Y", "field": "tip", "expected": wts_updates[33962]})
    checks_def.append({"type": "unit", "id": "n04Y", "field": "ubertip", "expected": wts_updates[31897]})

    # n04X: Мёртвый маг (W)
    wts_updates[33959] = "|cffe4cfa3Мёртвый маг|r"
    wts_updates[33960] = "|cffe4cfa3Мёртвый маг|r (|cffffffffW|r)"
    wts_updates[31896] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тёмный чернокнижник Отрекшихся, черпающий силу из смерти и магии огня.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deТёмная стая|cffced4da: направляет рой нетопырей, наносящих урон по области.|n"
        "- |cffa9c7deОгненный ливень|cffced4da: обрушивает потоки пламени на скопления врагов.|n"
        "- |cffa9c7deПоглощение жизни|cffced4da: выкачивает жизненную силу из врага в своё здоровье.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n04X", "field": "name", "expected": wts_updates[33959]})
    checks_def.append({"type": "unit", "id": "n04X", "field": "tip", "expected": wts_updates[33960]})
    checks_def.append({"type": "unit", "id": "n04X", "field": "ubertip", "expected": wts_updates[31896]})

    # n04V: Убийца (E)
    wts_updates[22457] = "|cffe4cfa3Убийца|r"
    wts_updates[33940] = "|cffe4cfa3Убийца|r (|cffffffffE|r)"
    wts_updates[31881] = (
        "|cffa6afb8ЮНИТ:|cffced4da Невидимый лазутчик ближнего боя, устраняющий ключевые цели внезапными ударами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deСкрыться|cffced4da: входит в режим невидимости.|n"
        "- |cffa9c7deРазъедающий яд|cffced4da: наносит дополнительный урон и ослабляет цель.|n"
        "- |cffa9c7deКаннибализм|cffced4da: поедает труп для исцеления.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n04V", "field": "name", "expected": wts_updates[22457]})
    checks_def.append({"type": "unit", "id": "n04V", "field": "tip", "expected": wts_updates[33940]})
    checks_def.append({"type": "unit", "id": "n04V", "field": "ubertip", "expected": wts_updates[31881]})

    # h0JA: Валькира (R)
    wts_updates[4184] = "|cffe4cfa3Валькира|r"
    wts_updates[5063] = "|cffe4cfa3Валькира|r (|cffffffffR|r)"
    wts_updates[31879] = (
        "|cffa6afb8ЮНИТ:|cffced4da Крылатая вестница загробного мира, управляющая таинствами воскрешения павших.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВоскрешение|cffced4da: возвращает к жизни павших союзных бойцов.|n"
        "- |cffa9c7deОживление мёртвых|cffced4da: поднимает неуязвимых воинов из трупов на поле боя.|n"
        "- |cffa9c7deСтрела Света|cffced4da: поражает врагов святой карающей энергией.|n|n"
        "Атакует |cffffffffназемные и воздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JA", "field": "name", "expected": wts_updates[4184]})
    checks_def.append({"type": "unit", "id": "h0JA", "field": "tip", "expected": wts_updates[5063]})
    checks_def.append({"type": "unit", "id": "h0JA", "field": "ubertip", "expected": wts_updates[31879]})

    # e034: Гнильной слизень
    wts_updates[26265] = "|cffe4cfa3Гнильной слизень|r"
    wts_updates[26266] = "|cffe4cfa3Гнильной слизень|r"
    wts_updates[32921] = (
        "|cffa6afb8ЮНИТ:|cffced4da Чумное порождение, возникающее из тел погибших под действием заразной гнили.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deАура Гнили|cffced4da: ускоряет атаку и бег союзников вокруг.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e034", "field": "name", "expected": wts_updates[26265]})

    # u02J - u02O: Гниль (уровни)
    for sid in [22282, 25623, 25624, 25632, 25634, 25635]:
        wts_updates[sid] = "|cffe4cfa3Гниль|r"

    # u02P: Скелет-воин
    wts_updates[33967] = "|cffe4cfa3Скелет-воин|r"

    # =========================================================================
    # 5. UPGRADES (17 upgrades)
    # =========================================================================
    # R0FI: Улучшенные инструменты (6 levels)
    for i in range(1, 7):
        # names: 34069..34074
        sid_n = 34068 + i
        wts_updates[sid_n] = "|cffe4cfa3Улучшенные инструменты|r"
        # tips: 21599, 21600, 21871..21874
        sid_t = [21599, 21600, 21871, 21872, 21873, 21874][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Улучшенные инструменты — уровень {i}|r (|cffffffffE|r)"
        # ubertips: 25927, 23120, 23121, 24796, 24797, 25926
        sid_ub = [25927, 23120, 23121, 24796, 24797, 25926][i-1]
        cap = 10 if i == 1 else 10 + (i - 1) * 8
        bonus = "+10" if i == 1 else "+8"
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает переносимый работниками объём древесины на |cffc8e087{bonus}|cffced4da ед. "
            f"(суммарный бонус: |cffffffff+{cap}|cffced4da ед.).|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FJ: Железные мечи (6 levels)
    for i in range(1, 7):
        sid_n = [26006, 26008, 26007, 26011, 26010, 26009][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Железные мечи|r"
        sid_t = [26012, 26014, 26013, 26017, 26016, 26015][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Железные мечи — уровень {i}|r (|cffffffffQ|r)"
        sid_ub = [26024, 26026, 26025, 26029, 26028, 26027][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон ближнего боя пехоты и бойцов Отрекшихся.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deМёртвый воин|cffced4da|n"
            f"- |cffa9c7deСтраж Смерти|cffced4da|n"
            f"- |cffa9c7deВождь Орды|cffced4da|n"
            f"- |cffa9c7deУбийца|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FK: Железная броня (6 levels)
    for i in range(1, 7):
        sid_n = [26031, 26032, 26033, 26036, 26035, 26034][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Железная броня|r"
        sid_t = [26037, 26038, 26039, 26042, 26041, 26040][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Железная броня — уровень {i}|r (|cffffffffW|r)"
        sid_ub = [26049, 26050, 26051, 26054, 26053, 26052][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает защиту и броню воинов ближнего боя Отрекшихся.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deМёртвый воин|cffced4da|n"
            f"- |cffa9c7deСтраж Смерти|cffced4da|n"
            f"- |cffa9c7deВождь Орды|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FL: Железные снаряды (6 levels)
    for i in range(1, 7):
        sid_n = [26056, 26058, 26057, 26061, 26060, 26059][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Железные снаряды|r"
        sid_t = [26062, 26064, 26063, 26067, 26066, 26065][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Железные снаряды — уровень {i}|r (|cffffffffA|r)"
        sid_ub = [26074, 26076, 26075, 26079, 26078, 26077][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон стрелковых войск и осадных орудий Отрекшихся.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deЛучница|cffced4da|n"
            f"- |cffa9c7deТёмный следопыт|cffced4da|n"
            f"- |cffa9c7deГнилевозка|cffced4da|n"
            f"- |cffa9c7deУлучшенная Гнилевозка|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FM: Лёгкая броня (6 levels)
    for i in range(1, 7):
        sid_n = [26081, 26082, 26083, 26086, 26085, 26084][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Лёгкая броня|r"
        sid_t = [26087, 26088, 26089, 26092, 26091, 26090][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Лёгкая броня — уровень {i}|r (|cffffffffS|r)"
        sid_ub = [26099, 26100, 26101, 26104, 26103, 26102][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает показатель брони стрелков, осадных машин и диверсантов Отрекшихся.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deЛучница|cffced4da|n"
            f"- |cffa9c7deТёмный следопыт|cffced4da|n"
            f"- |cffa9c7deГнилевозка|cffced4da|n"
            f"- |cffa9c7deУлучшенная Гнилевозка|cffced4da|n"
            f"- |cffa9c7deУбийца|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FT: Магическая практика (6 levels)
    for i in range(1, 7):
        sid_n = [34099, 34100, 34101, 34102, 34107, 34108][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Магическая практика|r"
        sid_t = [34103, 34104, 34105, 34106, 34109, 34110][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Магическая практика — уровень {i}|r (|cffffffffD|r)"
        sid_ub = [26343, 26344, 26345, 26346, 26353, 26354][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает силу заклинаний и магическую защиту служителей смерти Отрекшихся.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deБанши|cffced4da|n"
            f"- |cffa9c7deМёртвый маг|cffced4da|n"
            f"- |cffa9c7deВалькира|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FY: Смертоносные ингредиенты (4 levels)
    for i in range(1, 5):
        sid_n = [34127, 34129, 34130, 34131][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Смертоносные ингредиенты|r"
        sid_t = [34128, 34132, 34133, 34134][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Смертоносные ингредиенты — уровень {i}|r (|cffffffffQ|r)"
        sid_ub = [26685, 26687, 26688, 26689][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает ядовитые эффекты атак пехоты и стрелков армии Отрекшихся.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deМёртвый воин|cffced4da|n"
            f"- |cffa9c7deЛучница|cffced4da|n"
            f"- |cffa9c7deТёмный следопыт|cffced4da|n"
            f"- |cffa9c7deСтраж Смерти|cffced4da|n"
            f"- |cffa9c7deУбийца|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/4|r."
        )

    # R0FU: Эксперименты с Гнилью (1 level)
    wts_updates[34111] = "|cffe4cfa3Эксперименты с Гнилью|r"
    wts_updates[34112] = "|cffe4cfa3Эксперименты с Гнилью|r (|cffffffffQ|r)"
    wts_updates[26569] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает доступ к производству Улучшенных Гнилевозок и смертоносных штаммов чумы в Лаборатории.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deЛаборатория|cffced4da|n"
        "- |cffa9c7deУлучшенная Гнилевозка|cffced4da.|r"
    )

    # R0FV: Методы Изоляции (3 levels)
    for i in range(1, 4):
        sid_n = [34113, 34115, 34116][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Методы Изоляции|r"
        sid_t = [34114, 34117, 34118][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Методы Изоляции — уровень {i}|r (|cffffffffW|r)"
        sid_ub = [26601, 26603, 26604][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает сопротивляемость войск Отрекшихся к чумным и ядовитым испарениям.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- войскам с изолирующей бронёй.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/3|r."
        )

    # R0FB: Усилить смертоносность (5 levels)
    for i in range(1, 6):
        sid_n = [34059, 34061, 34062, 34063, 34064][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Усилить смертоносность|r"
        sid_t = [34060, 34065, 34066, 34067, 34068][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Усилить смертоносность — уровень {i}|r (|cffffffffE|r)"
        sid_ub = [25969, 25971, 25972, 25973, 25974][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает периодический урон от всех штаммов боевой гнили и чумных облаков.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deГнилевозка|cffced4da|n"
            f"- |cffa9c7deУлучшенная Гнилевозка|cffced4da|n"
            f"- |cffa9c7deВождь Орды|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/5|r."
        )

    # R0KJ: Улучшенные поршни (1 level)
    wts_updates[39294] = "|cffe4cfa3Улучшенные поршни|r"
    wts_updates[39295] = "|cffe4cfa3Улучшенные поршни|r (|cffffffffA|r)"
    wts_updates[39300] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки осадных машин на |cffc8e087+15%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deГнилевозка|cffced4da|n"
        "- |cffa9c7deУлучшенная Гнилевозка|cffced4da.|r"
    )

    # R0FW: Усилить смертоносность (5 levels, служебный маркер)
    for i in range(1, 6):
        sid_n = [34119, 26219, 34121, 26220, 34122][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Усилить смертоносность|r"
        sid_t = [34120, 34123, 34124, 34125, 34126][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Усилить смертоносность — уровень {i}|r"
        sid_ub = [26637, 26647, 26648, 26649, 26650][i-1]
        wts_updates[sid_ub] = f"|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер усиления урона гнили (уровень {i}/5).|r"

    # R0G0: Обучение Убийц (6 levels)
    for i in range(1, 7):
        sid_n = [34148, 34149, 34150, 34151, 34156, 34157][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Обучение Убийц|r"
        sid_t = [34152, 34153, 34154, 34155, 34158, 34159][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Обучение Убийц — уровень {i}|r (|cffffffffD|r)"
        sid_ub = [27001, 27002, 27003, 27004, 27011, 27012][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, маны, скорость регенерации и скорость бега Убийц.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deУбийца|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FZ: Усиление Валь'Кир (6 levels)
    for i in range(1, 7):
        sid_n = [34136, 34137, 34138, 34139, 34144, 34145][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Усиление Валь'Кир|r"
        sid_t = [34140, 34141, 34142, 34143, 34146, 34147][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Усиление Валь'Кир — уровень {i}|r (|cffffffffC|r)"
        sid_ub = [26737, 26738, 26739, 26740, 26747, 26748][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и скорость восстановления маны Валькир.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВалькира|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FN: Посвящение Банши (6 levels)
    for i in range(1, 7):
        sid_n = [34075, 34076, 34077, 34078, 34083, 34084][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Посвящение Банши|r"
        sid_t = [34079, 34080, 34081, 34082, 34085, 34086][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Посвящение Банши — уровень {i}|r (|cffffffffA|r)"
        sid_ub = [26286, 26287, 26288, 26289, 26296, 26297][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и скорость восстановления маны Банши.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deБанши|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # R0FO: Обучение магов (6 levels)
    for i in range(1, 7):
        sid_n = [34087, 34088, 34089, 34090, 34095, 34096][i-1]
        wts_updates[sid_n] = "|cffe4cfa3Обучение магов|r"
        sid_t = [34091, 34092, 34093, 34094, 34097, 34098][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Обучение магов — уровень {i}|r (|cffffffffS|r)"
        sid_ub = [26309, 26310, 26311, 26312, 26319, 26320][i-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и скорость восстановления маны Мёртвых магов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМёртвый маг|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{i}/6|r."
        )

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # Sylvanas spells
    # A166: Воскрешение мёртвых (R)
    wts_updates[26752] = "|cffe4cfa3Воскрешение мёртвых|r"
    wts_updates[38636] = "|cffe4cfa3Воскрешение мёртвых|r"
    wts_updates[38635] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает скелетов из трупов павших воинов.|r"
    for lvl in range(1, 5):
        tip_id = [35079, 38637, 38638, 38639][lvl-1]
        wts_updates[tip_id] = f"|cffe4cfa3Воскрешение мёртвых — [уровень {lvl}]|r (|cffffffffR|r)"
    checks_def.append({"type": "ability", "id": "A166", "field": "name", "expected": wts_updates[26752]})

    # A15S: Превратиться в Банши (W)
    wts_updates[28908] = "|cffe4cfa3Превратиться в Банши|r"
    wts_updates[38472] = "|cffe4cfa3Превратиться в Банши|r"
    wts_updates[38474] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сильвана принимает облик бесплотной Банши, сокрушая врагов тёмной магией.|r"
    wts_updates[38470] = "|cffe4cfa3Превратиться в Банши — [уровень 1]|r (|cffffffffW|r)"
    wts_updates[38471] = "|cffe4cfa3Превратиться в Банши — [уровень 2]|r (|cffffffffW|r)"
    wts_updates[103] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает Королеву в указанную точку, нанося урон врагам вокруг и временно обращая её в форму Банши.|r"
    checks_def.append({"type": "ability", "id": "A15S", "field": "name", "expected": wts_updates[28908]})

    # A15R: Тёмная стрела (E)
    wts_updates[27259] = "|cffe4cfa3Тёмная стрела|r"
    wts_updates[27260] = "|cffe4cfa3Тёмная стрела|r"
    wts_updates[28907] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наполняет выстрелы тёмной энергией, ослабляющей броню противника и наносящей периодический урон.|r"
    for lvl in range(1, 5):
        sid_t = [27261, 27262, 27263, 38463][lvl-1]
        wts_updates[sid_t] = f"|cffe4cfa3Тёмная стрела — [уровень {lvl}]|r (|cffffffffE|r)"
        sid_ub = [27264, 27265, 27266, 38467][lvl-1]
        wts_updates[sid_ub] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая стрела накладывает на врага эффект тёмной скверны, снижая его броню и нанося периодический урон.|n|n"
            f"|cffa6afb8Уровень {lvl}:|cffced4da урон и снижение брони увеличены.|r"
        )
    checks_def.append({"type": "ability", "id": "A15R", "field": "name", "expected": wts_updates[27259]})

    # A15Q: Абсолютная немота (Q)
    wts_updates[38464] = "|cffe4cfa3Абсолютная немота|r"
    wts_updates[38465] = "|cffe4cfa3Абсолютная немота|r"
    wts_updates[27255] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подавляет любую магию в указанной области, запрещая врагам применять способности.|r"
    for lvl in range(1, 5):
        sid_t = [38466, 38468, 38469, 27256][lvl-1]
        wts_updates[sid_t] = f"|cffe4cfa3Абсолютная немота — [уровень {lvl}]|r (|cffffffffQ|r)"
    wts_updates[9540] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт обширную зону абсолютного безмолвия, полностью блокируя заклинания врагов.|r"
    checks_def.append({"type": "ability", "id": "A15Q", "field": "name", "expected": wts_updates[38464]})

    # A15T: Форма банши скрыто
    wts_updates[28909] = "|cffe4cfa3Форма банши|r"

    # Dark Ranger: ANba, ANdr, A0W4
    wts_updates[9772] = "|cffe4cfa3Чёрная стрела|r"
    wts_updates[9785] = "|cffe4cfa3Чёрная стрела|r"
    wts_updates[9781] = "|cffe4cfa3Чёрная стрела — [уровень 1]|r (|cffffffffF|r)"
    wts_updates[9782] = "|cffe4cfa3Чёрная стрела — [уровень 2]|r (|cffffffffF|r)"
    wts_updates[9783] = "|cffe4cfa3Чёрная стрела — [уровень 3]|r (|cffffffffF|r)"
    wts_updates[9784] = "|cffe4cfa3Чёрная стрела — [уровень 4]|r (|cffffffffF|r)"

    wts_updates[26525] = "|cffe4cfa3Похищение жизни — [уровень 4]|r (|cffffffffD|r)"
    wts_updates[25587] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Похищает здоровье у вражеского юнита или передаёт своё здоровье союзнику.|r"

    wts_updates[27232] = "|cffe4cfa3Подчинение — [уровень 2]|r (|cffffffffC|r)"
    wts_updates[26271] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Захватывает полный контроль над разумом выбранного вражеского воина.|r"
    wts_updates[22171] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Захватывает полный контроль над разумом вражеского воина. Позволяет подчинять могущественных бойцов.|r"

    # Apothecary: A15D, A15C, A15B, A15A
    # A15D: Аура Регенерации
    wts_updates[34034] = "|cffe4cfa3Аура Регенерации|r"
    wts_updates[34035] = "|cffe4cfa3Аура Регенерации|r"
    wts_updates[34036] = "|cffe4cfa3Аура Регенерации — [уровень 1]|r"
    wts_updates[34037] = "|cffe4cfa3Аура Регенерации — [уровень 2]|r"
    wts_updates[34038] = "|cffe4cfa3Аура Регенерации — [уровень 3]|r"
    wts_updates[38473] = "|cffe4cfa3Аура Регенерации — [уровень 4]|r"
    checks_def.append({"type": "ability", "id": "A15D", "field": "name", "expected": wts_updates[34034]})

    # A15C: Стимуляторы (B)
    wts_updates[9786] = "|cffe4cfa3Стимуляторы|r"
    wts_updates[9787] = "|cffe4cfa3Стимуляторы|r"
    wts_updates[26844] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вводит союзному воину боевую сыворотку, временно увеличивая скорость атаки и бега.|r"
    wts_updates[26832] = "|cffe4cfa3Стимуляторы — [уровень 1]|r (|cffffffffB|r)"
    wts_updates[26833] = "|cffe4cfa3Стимуляторы — [уровень 2]|r (|cffffffffB|r)"
    wts_updates[26834] = "|cffe4cfa3Стимуляторы — [уровень 3]|r (|cffffffffB|r)"
    wts_updates[26835] = "|cffe4cfa3Стимуляторы — [уровень 4]|r (|cffffffffB|r)"
    checks_def.append({"type": "ability", "id": "A15C", "field": "name", "expected": wts_updates[9786]})

    # A15B: Изобрести руну (T)
    wts_updates[38460] = "|cffe4cfa3Изобрести руну|r"
    wts_updates[38462] = "|cffe4cfa3Изобрести руну|r"
    wts_updates[27225] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аптекарь создаёт случайную боевую руну исцеления, защиты или скорости в указанной точке.|r"
    wts_updates[38461] = "|cffe4cfa3Изобрести руну — [уровень 1]|r (|cffffffffT|r)"
    wts_updates[27224] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Синтезирует мощную боевую руну, дарующую союзникам мгновенное исцеление, защитный барьер или ускорение.|r"
    checks_def.append({"type": "ability", "id": "A15B", "field": "name", "expected": wts_updates[38460]})

    # A15A: Кислотная бомба
    wts_updates[19669] = "|cffe4cfa3Кислотная бомба — [уровень 4]|r (|cffffffffB|r)"
    wts_updates[19670] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает колбу с концентрированной кислотой, разъедая броню цели и нанося периодический урон по области.|r"

    # Eliminator: A158, A157, A156, AOwk
    # A158: Всеобщий мрак (R)
    wts_updates[38457] = "|cffe4cfa3Всеобщий мрак|r"
    wts_updates[38459] = "|cffe4cfa3Всеобщий мрак|r"
    wts_updates[26794] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Погружает находящиеся рядом союзные силы в плотную пелену невидимости.|r"
    wts_updates[38456] = "|cffe4cfa3Всеобщий мрак — [уровень 1]|r (|cffffffffR|r)"
    wts_updates[38458] = "|cffe4cfa3Всеобщий мрак — [уровень 2]|r (|cffffffffR|r)"
    wts_updates[26786] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окутывает окружающие войска мраком, скрывая их от взора противника.|r"
    checks_def.append({"type": "ability", "id": "A158", "field": "name", "expected": wts_updates[38457]})

    # A157: Отравленный кинжал (D)
    wts_updates[12521] = "|cffe4cfa3Отравленный кинжал|r"
    wts_updates[12531] = "|cffe4cfa3Отравленный кинжал|r"

    # A156: Мастерство (пассивная)
    wts_updates[20595] = "|cffe4cfa3Мастерство|r"
    wts_updates[26781] = "|cffe4cfa3Мастерство|r"
    wts_updates[26531] = "|cffe4cfa3Мастерство — [уровень 1]|r"
    wts_updates[26532] = "|cffe4cfa3Мастерство — [уровень 2]|r"
    wts_updates[26533] = "|cffe4cfa3Мастерство — [уровень 3]|r"
    wts_updates[26534] = "|cffe4cfa3Мастерство — [уровень 4]|r"
    checks_def.append({"type": "ability", "id": "A156", "field": "name", "expected": wts_updates[20595]})

    # AOwk: Танец ветра
    wts_updates[23502] = "|cffe4cfa3Танец ветра — [уровень 4]|r (|cffffffffW|r)"
    wts_updates[20908] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует невидимость и ускорение. Атака из невидимости наносит критический дополнительный урон.|r"

    # Worker: A0I3
    wts_updates[26484] = "|cffe4cfa3Небольшой скачок|r"
    wts_updates[10064] = "|cffe4cfa3Небольшой скачок|r"
    wts_updates[10976] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает строителя на короткое расстояние.|r"
    wts_updates[26476] = "|cffe4cfa3Небольшой скачок|r (|cffffffffB|r)"
    wts_updates[26477] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит рабочего на небольшое расстояние для преодоления препятствий.|r"

    # Barracks & Combat abils:
    # A15J: Каннибализм
    wts_updates[34053] = "|cffe4cfa3Каннибализм|r"
    wts_updates[34054] = "|cffe4cfa3Каннибализм|r (|cffffffffC|r)"
    wts_updates[26912] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поедает труп павшего существа, восстанавливая здоровье воина.|r"

    # A15I: Изолирующая броня
    wts_updates[26759] = "|cffe4cfa3Изолирующая броня|r"
    wts_updates[34052] = "|cffe4cfa3Изолирующая броня — уровень 1|r"
    wts_updates[34048] = "|cffe4cfa3Изолирующая броня — уровень 2|r"
    wts_updates[34049] = "|cffe4cfa3Изолирующая броня — уровень 3|r"
    wts_updates[34050] = "|cffe4cfa3Изолирующая броня — уровень 4|r"
    wts_updates[34051] = "|cffe4cfa3Изолирующая броня — уровень 5|r"
    wts_updates[27710] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Защитное покрытие доспехов, снижающее урон от ядов и болезнетворных испарений.|r"

    # A14U: Уязвимость к магии света (пассивная)
    wts_updates[34008] = "|cffe4cfa3Уязвимость к магии света|r"
    wts_updates[34009] = "|cffe4cfa3Уязвимость к магии света — уровень 1|r"
    wts_updates[34010] = "|cffe4cfa3Уязвимость к магии света — уровень 2|r"
    wts_updates[34011] = "|cffe4cfa3Уязвимость к магии света — уровень 3|r"
    wts_updates[34012] = "|cffe4cfa3Уязвимость к магии света — уровень 4|r"
    wts_updates[34026] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Нежить получает повышенный урон от заклинаний и атак магии Света.|r"

    # A14T: Разъедающий яд (по технике)
    wts_updates[33997] = "|cffe4cfa3Разъедающий яд|r"
    for i in range(1, 6):
        sid_t = [33998, 33999, 34000, 34001, 34002][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Разъедающий яд — уровень {i}|r"
    wts_updates[34007] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки бойца наносят дополнительный разъедающий урон технике и осадным орудиям.|r"

    # A14S: Разъедающий яд (по живым)
    wts_updates[26520] = "|cffe4cfa3Разъедающий яд|r"
    wts_updates[4418] = "|cffe4cfa3Разъедающий яд — уровень 1|r"
    wts_updates[4419] = "|cffe4cfa3Разъедающий яд — уровень 2|r"
    wts_updates[12288] = "|cffe4cfa3Разъедающий яд — уровень 3|r"
    wts_updates[12289] = "|cffe4cfa3Разъедающий яд — уровень 4|r"
    wts_updates[26524] = "|cffe4cfa3Разъедающий яд — уровень 5|r"

    # A14W: Накопительный яд
    wts_updates[34040] = "|cffe4cfa3Накопительный яд|r"
    for i in range(1, 6):
        sid_t = [34039, 34041, 34042, 34043, 34044][i-1]
        wts_updates[sid_t] = f"|cffe4cfa3Накопительный яд — уровень {i}|r"
    wts_updates[26198] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стрелы пропитаны токсином, замедляющим цель и наносящим периодический урон.|r"

    # A14X: Кинжал теней
    wts_updates[34014] = "|cffe4cfa3Кинжал теней|r"
    wts_updates[34013] = "|cffe4cfa3Кинжал теней|r (|cffffffffD|r)"
    wts_updates[34015] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно бросает отравленный кинжал, замедляя врага и нанося урон.|r"

    # A15L & A15M: Смердящий запах / Тяжёлая поступь (Страж Смерти)
    wts_updates[26973] = "|cffe4cfa3Смердящий запах|r"
    wts_updates[34049] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Трупный смрад замедляет скорость атаки и бега окружающих вражеских воинов.|r"
    wts_updates[34057] = "|cffe4cfa3Тяжёлая поступь|r"
    wts_updates[34058] = "|cffe4cfa3Тяжёлая поступь|r (|cffffffffW|r)"
    wts_updates[26977] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сотрясает землю тяжёлой поступью, нанося урон и кратковременно оглушая противников вокруг.|r"

    # Laboratory & Wagons:
    # A13J & A13K: Выбор типа Гнили
    wts_updates[33982] = "|cffe4cfa3Выбрать тип Гнили|r"
    wts_updates[33983] = "|cffe4cfa3Выбрать тип Гнили|r"
    wts_updates[26886] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Открывает меню выбора штамма чумы для артиллерии Гнилевозки.|r"
    wts_updates[26887] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет выбрать активный боевой штамм гнили для осадной машины.|r"

    wts_updates[33984] = "|cffe4cfa3Выбрать тип Гнили|r"
    wts_updates[33985] = "|cffe4cfa3Выбрать тип Гнили|r"
    wts_updates[26888] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Открывает меню выбора усиленных штаммов чумы для Улучшенной Гнилевозки.|r"

    # A13L: Заряд Гнили
    wts_updates[26106] = "|cffe4cfa3Заряд Гнили|r"
    wts_updates[26122] = "|cffe4cfa3Заряд Гнили|r"
    wts_updates[26268] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает чумной снаряд, поражающий врагов болезнетворным облаком.|r"

    # Plague switching spells:
    # A142 / A132: Обычная чума
    wts_updates[26210] = "|cffe4cfa3Обычная чума|r"
    wts_updates[26967] = "|cffe4cfa3Обычная чума|r (|cffffffffQ|r)"
    wts_updates[26873] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заряжает катапульту обычной гнилью, наносящей базовый урон живым существам.|r"
    wts_updates[22480] = "|cffe4cfa3Обычная чума|r"
    wts_updates[25636] = "|cffe4cfa3Обычная чума|r"

    # A143 / A13U / A15H: Коррозийная чума
    wts_updates[26212] = "|cffe4cfa3Коррозийная чума|r"
    wts_updates[26213] = "|cffe4cfa3Коррозийная чума|r (|cffffffffW|r)"
    wts_updates[26874] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заряжает катапульту едкой гнилью, разъедающей броню врагов и наносящей урон технике.|r"
    wts_updates[26142] = "|cffe4cfa3Коррозийная чума|r"
    wts_updates[26144] = "|cffe4cfa3Коррозийная чума|r"
    wts_updates[26179] = "|cffe4cfa3Коррозия брони|r"
    wts_updates[26185] = "|cffe4cfa3Коррозия брони|r"

    # A144 / A13R: Ослабляющая чума
    wts_updates[26214] = "|cffe4cfa3Ослабляющая чума|r"
    wts_updates[26215] = "|cffe4cfa3Ослабляющая чума|r (|cffffffffE|r)"
    wts_updates[26875] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заряжает катапульту ослабляющей гнилью, замедляющей атаку и бег противников.|r"
    wts_updates[33986] = "|cffe4cfa3Ослабляющая чума|r"
    wts_updates[33987] = "|cffe4cfa3Ослабляющая чума|r"

    # A14C / A13M / A13T: Убийственная чума
    wts_updates[16507] = "|cffe4cfa3Убийственная чума|r"
    wts_updates[26968] = "|cffe4cfa3Убийственная чума|r (|cffffffffQ|r)"
    wts_updates[26877] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Передовой смертоносный состав, наносящий огромный периодический урон живой силе врага.|r"
    wts_updates[26107] = "|cffe4cfa3Убийственная чума|r"
    wts_updates[27221] = "|cffe4cfa3Убийственная чума|r"
    wts_updates[26269] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает заряд концентрированной убийственной чумы.|r"
    wts_updates[26139] = "|cffe4cfa3Убийственная чума|r"
    wts_updates[26141] = "|cffe4cfa3Убийственная чума|r"

    # A14E / A13N / A13S: Заразная чума
    wts_updates[24397] = "|cffe4cfa3Заразная чума|r"
    wts_updates[26970] = "|cffe4cfa3Заразная чума|r (|cffffffffE|r)"
    wts_updates[26879] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заражает врагов штаммом, порождающим чумного слизня при гибели заражённого воина.|r"
    wts_updates[26123] = "|cffe4cfa3Заразная чума|r"
    wts_updates[26856] = "|cffe4cfa3Заразная чума|r"
    wts_updates[26270] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает заряд заразной чумы, создающей слизней из павших врагов.|r"
    wts_updates[22524] = "|cffe4cfa3Заразная чума|r"
    wts_updates[26138] = "|cffe4cfa3Заразная чума|r"

    # A14D / A13O / A13V: Заградительная чума
    wts_updates[20738] = "|cffe4cfa3Заградительная чума|r"
    wts_updates[26969] = "|cffe4cfa3Заградительная чума|r (|cffffffffW|r)"
    wts_updates[26878] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт токсичный барьер, сковывающий врагов и лишающий их возможности двигаться.|r"
    wts_updates[26125] = "|cffe4cfa3Заградительная чума|r"
    wts_updates[26868] = "|cffe4cfa3Заградительная чума|r"
    wts_updates[18834] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает заряд заградительной чумы, обездвиживающий поражённые цели.|r"
    wts_updates[26145] = "|cffe4cfa3Заградительная чума|r"
    wts_updates[26147] = "|cffe4cfa3Заградительная чума|r"

    # Sanctum abils:
    # A14P / A14Q: Одержимость (Банши)
    wts_updates[34046] = "|cffe4cfa3Одержимость|r"
    wts_updates[34045] = "|cffe4cfa3Одержимость|r (|cffffffffC|r)"
    wts_updates[34047] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Банши вселяется во вражеского воина, подчиняя его волю. При этом тело банши уничтожается.|r"
    wts_updates[33992] = "|cffe4cfa3Одержимость|r"
    wts_updates[33993] = "|cffe4cfa3Одержимость|r (|cffffffffC|r)"

    # A14R: Пожирание магии (Банши)
    wts_updates[33994] = "|cffe4cfa3Пожирание магии|r"
    wts_updates[33995] = "|cffe4cfa3Пожирание магии|r (|cffffffffB|r)"
    wts_updates[33996] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает положительные и отрицательные чары в выбранной области, восполняя ману заклинательницы.|r"

    # A1H7: Проклятие (Банши)
    wts_updates[20549] = "|cffe4cfa3Проклятие|r"
    wts_updates[20550] = "|cffe4cfa3Проклятие|r (|cffffffffE|r)"

    # Dead Mage spells: A154, A153, A152
    # A154: Тёмная стая (D)
    wts_updates[34029] = "|cffe4cfa3Тёмная стая|r"
    wts_updates[34030] = "|cffe4cfa3Тёмная стая|r (|cffffffffD|r)"
    wts_updates[34031] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Направляет вперёд стаю нетопырей, наносящих урон всем врагам на своём пути.|r"

    # A153: Огненный ливень (F)
    wts_updates[34026] = "|cffe4cfa3Огненный ливень|r"
    wts_updates[34027] = "|cffe4cfa3Огненный ливень|r (|cffffffffF|r)"
    wts_updates[34028] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает волны раскалённого огня на выбранную область, поджигая врагов.|r"

    # A152: Поглощение жизни (E)
    wts_updates[34023] = "|cffe4cfa3Поглощение жизни|r"
    wts_updates[34024] = "|cffe4cfa3Поглощение жизни|r (|cffffffffE|r)"
    wts_updates[34025] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выкачивает здоровье из врага в течение нескольких секунд, исцеляя мага.|r"

    # Assassin: A14Y (Скрыться)
    wts_updates[1270] = "|cffe4cfa3Скрыться|r"
    wts_updates[1271] = "|cffe4cfa3Скрыться|r (|cffffffffI|r)"
    wts_updates[1272] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет убийце раствориться в тенях и стать невидимым для врагов.|r"

    # Valkyr: A151, A14Z, A150
    # A151: Оживление мёртвых (D)
    wts_updates[34020] = "|cffe4cfa3Оживление мёртвых|r"
    wts_updates[34021] = "|cffe4cfa3Оживление мёртвых|r (|cffffffffD|r)"
    wts_updates[31518] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает павших воинов в виде неуязвимой нежити на короткий промежуток времени.|r"

    # A14Z: Воскрешение мёртвых (F)
    wts_updates[34016] = "|cffe4cfa3Воскрешение мёртвых|r"
    wts_updates[34017] = "|cffe4cfa3Воскрешение мёртвых|r (|cffffffffF|r)"
    wts_updates[34018] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Воскрешает павших союзных бойцов вокруг с полным запасом сил.|r"

    # A150: Воскрешение (R)
    wts_updates[26756] = "|cffe4cfa3Воскрешение|r"
    wts_updates[26757] = "|cffe4cfa3Воскрешение|r (|cffffffffR|r)"
    wts_updates[34019] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни павших союзников на поле боя.|r"

    # Slime & Rot abils:
    wts_updates[9930] = "|cffe4cfa3Аура Гнили|r"
    wts_updates[26930] = "|cffe4cfa3Урон Гнили|r"
    for sid in [23363, 23364, 23378, 23381, 23382]:
        wts_updates[sid] = "|cffe4cfa3Урон Гнили|r"

    wts_updates[26184] = "|cffe4cfa3Обычная Гниль|r"
    for sid in [26168, 26174, 26176, 26177, 26178]:
        wts_updates[sid] = "|cffe4cfa3Обычная Гниль|r"

    wts_updates[33990] = "|cffe4cfa3Порождение Гнили|r"
    wts_updates[33991] = "|cffe4cfa3Порождение Гнили|r"
    wts_updates[26209] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вызывает появление гнильного слизня при гибели заражённой цели.|r"

    wts_updates[26195] = "|cffe4cfa3Заразная Гниль|r"
    for sid in [26196, 26869, 26870, 26871, 26872]:
        wts_updates[sid] = "|cffe4cfa3Заразная Гниль|r"

    wts_updates[26117] = "|cffe4cfa3Смертоносная Гниль|r"
    for sid in [25648, 26118, 26119, 26120, 26121]:
        wts_updates[sid] = "|cffe4cfa3Смертоносная Гниль|r"

    wts_updates[26151] = "|cffe4cfa3Загрязняющая Гниль|r"
    for sid in [26150, 26152, 26154, 26155, 26156]:
        wts_updates[sid] = "|cffe4cfa3Загрязняющая Гниль|r"

    wts_updates[26162] = "|cffe4cfa3Коррозийная Гниль|r"
    for sid in [26157, 26163, 26165, 26166, 26167]:
        wts_updates[sid] = "|cffe4cfa3Коррозийная Гниль|r"

    wts_updates[33988] = "|cffe4cfa3Безопасная Гниль|r"
    for sid in [33989, 39457, 39458, 39459, 39460]:
        wts_updates[sid] = "|cffe4cfa3Безопасная Гниль|r"

    # A15P: Подчинение воли
    wts_updates[27236] = "|cffe4cfa3Подчинение воли|r"
    wts_updates[27456] = "|cffe4cfa3Подчинение воли|r"
    wts_updates[27243] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Массовое подавление воли вражеских отрядов в выбранной области.|r"
    wts_updates[27234] = "|cffe4cfa3Подчинение воли — [уровень 1]|r (|cffffffffC|r)"
    wts_updates[27235] = "|cffe4cfa3Подчинение воли — [уровень 2]|r (|cffffffffC|r)"
    wts_updates[27233] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подчиняет волю группы вражеских воинов в указанной зоне.|r"
    wts_updates[27438] = "|cffa6afb8Отрекшиеся:|cffced4da Подчинение воли успешно осуществлено.|r"

    # =========================================================================
    # 7. BUFFS
    # =========================================================================
    # B06I: Стимуляторы
    wts_updates[26842] = "|cffe4cfa3Стимуляторы|r"
    # B06J: Гниль
    wts_updates[26187] = "|cffe4cfa3Гниль|r"
    wts_updates[26899] = "|cffa6afb8ЭФФЕКТ:|cffced4da Боец заражён болезнетворной гнилью и непрерывно получает периодический урон.|r"
    # B06K: Коррозийная атака
    wts_updates[26916] = "|cffe4cfa3Коррозийная атака|r"
    # B06L: Тёмная стрела
    wts_updates[27267] = "|cffe4cfa3Тёмная стрела|r"

    # =========================================================================
    # MASTER PLAN STRUCTURE
    # =========================================================================
    plan_data = {
        "race": "Отрекшиеся (Forsaken)",
        "race_id": 27,
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A155"],
            "markers": ["R0G3"],
            "buildings": [
                "h0JP", "h0JQ", "h0JL", "h0JD", "h0JJ", "h0JI",
                "h0JO", "h0JR", "h0JK", "h0JM", "h0JZ", "h0D1"
            ],
            "units": [
                "h0J5", "n04T", "h0JC", "h0JN", "n04U", "o02X",
                "u02C", "o02Y", "n04Y", "n04X", "n04V", "h0JA",
                "e034", "u02J", "u02K", "u02L", "u02M", "u02N", "u02O", "u02P"
            ],
            "heroes": ["N059", "N05E", "N058", "O031", "O030"],
            "upgrades": [
                "R0G3", "R0FI", "R0FJ", "R0FK", "R0FL", "R0FM",
                "R0FT", "R0FY", "R0FU", "R0FV", "R0FB", "R0KJ",
                "R0FW", "R0G0", "R0FZ", "R0FN", "R0FO"
            ],
            "abilities": [
                "A155", "A166", "A15S", "A15R", "A15Q", "A15T",
                "ANsi", "ANba", "ANdr", "A0W4",
                "A15D", "A15C", "A15B", "A15A",
                "A158", "A157", "A156", "AOwk",
                "A0I3", "ANha", "Ahrp",
                "A15J", "A15I", "A14U", "A14T", "A14S", "A14W", "A14X", "A15L", "A15M", "Adef",
                "A13J", "A13L", "A15E", "A13K",
                "A142", "A132", "A143", "A13U", "A15H", "A144", "A13R",
                "A14C", "A13M", "A13T", "A14E", "A13N", "A13S", "A14D", "A13O", "A13V",
                "A14P", "A14R", "A1H7", "A14Q", "Aiun",
                "A154", "A153", "A152", "A14Y", "A151", "A14Z", "A150",
                "A13H", "A15F", "A13Z", "A141", "A140", "A133", "A13W", "A16G", "A13X", "A13Y",
                "A15P", "A15V", "ACch", "A159"
            ],
            "buffs": ["B06I", "B06J", "B06K", "B06L"],
            "items": ["I01X", "I01V", "I01W", "I01Y"]
        }
    }

    out_file = folder / "forsaken_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {out_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

if __name__ == "__main__":
    main()
