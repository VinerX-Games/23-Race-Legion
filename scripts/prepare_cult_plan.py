# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Cult of the Damned race (Race 33)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. RACE SELECTION & MARKERS: A1HA, R0J4, R0J5
    # =========================================================================
    # Ability A1HA (Race Selection)
    wts_updates[38911] = "|cffe4cfa3Культ Проклятых|r"
    wts_updates[38912] = "|cffe4cfa3Культ Проклятых|r (|cffffffffD|r)"
    wts_updates[22000] = (
        "|cffa6afb8РАСА:|cffced4da Организация фанатиков и тёмных магов на службе Короля-лича, использующая некромантию, плотеобработку и силу чумы.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Warcraft III — Wrath of the Lich King»|r|n|n"
        "|cffced4daКульт Проклятых — тайное сообщество смертных, присягнувших на верность Королю-личу ради обретения могущества и бессмертия. "
        "Основанный верховным магом Кел'Тузадом по велению Нер'зула, Культ тайно распространял зерно чумы по Лордерону, подготавливая почву "
        "для победоносного шествия Плети. Сектанты возводят осквернённые цитадели, собирают колоссальных големов из тел павших и призывают "
        "легионы нежити во славу Ледяного Трона.|r"
    )
    checks_def.append({"type": "ability", "id": "A1HA", "field": "name", "expected": wts_updates[38911]})
    checks_def.append({"type": "ability", "id": "A1HA", "field": "tip1", "expected": wts_updates[38912]})
    checks_def.append({"type": "ability", "id": "A1HA", "field": "ubertip1", "expected": wts_updates[22000]})

    # Marker R0J4 (Cult marker)
    wts_updates[34712] = "|cffe4cfa3Культ Проклятых|r"
    wts_updates[34713] = "|cffe4cfa3Культ Проклятых|r"
    wts_updates[34714] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Культу Проклятых.|r"
    checks_def.append({"type": "upgrade", "id": "R0J4", "field": "name1", "expected": wts_updates[34712]})
    checks_def.append({"type": "upgrade", "id": "R0J4", "field": "tip1", "expected": wts_updates[34713]})
    checks_def.append({"type": "upgrade", "id": "R0J4", "field": "ubertip1", "expected": wts_updates[34714]})

    # Marker R0J5 (Undead / Cult marker)
    wts_updates[34715] = "|cffe4cfa3Плеть или Культ Проклятых|r"
    wts_updates[34716] = "|cffe4cfa3Плеть или Культ Проклятых|r"
    wts_updates[34717] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к силам нежити (Плеть или Культ Проклятых).|r"
    checks_def.append({"type": "upgrade", "id": "R0J5", "field": "name1", "expected": wts_updates[34715]})
    checks_def.append({"type": "upgrade", "id": "R0J5", "field": "tip1", "expected": wts_updates[34716]})
    checks_def.append({"type": "upgrade", "id": "R0J5", "field": "ubertip1", "expected": wts_updates[34717]})

    # =========================================================================
    # 2. BUILDINGS (10 buildings)
    # =========================================================================
    # cD26: Некрополь (Q)
    wts_updates[26281] = "|cffe4cfa3Некрополь|r"
    wts_updates[34731] = "|cffe4cfa3Некрополь|r (|cffffffffQ|r)"
    wts_updates[35949] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание первой ступени. Обеспечивает добычу ресурсов, сбор древесины и начальный запас пищи.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПослушник|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЧертоги мёртвых|cffced4da: открывает доступ к передовым сооружениям и войскам.|r"
    )
    checks_def.append({"type": "unit", "id": "cD26", "field": "name", "expected": wts_updates[26281]})
    checks_def.append({"type": "unit", "id": "cD26", "field": "tip", "expected": wts_updates[34731]})
    checks_def.append({"type": "unit", "id": "cD26", "field": "ubertip", "expected": wts_updates[35949]})

    # cD25: Чертоги мертвых (Z)
    wts_updates[26280] = "|cffe4cfa3Чертоги мёртвых|r"
    wts_updates[34729] = "|cffe4cfa3Чертоги мёртвых|r (|cffffffffZ|r)"
    wts_updates[35970] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание второй ступени. Существенно увеличивает запас пищи и открывает доступ к новым постройкам и улучшениям.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПослушник|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deТёмная цитадель|cffced4da: открывает доступ к высшим технологиям культа.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD25", "field": "name", "expected": wts_updates[26280]})
    checks_def.append({"type": "unit", "id": "cD25", "field": "tip", "expected": wts_updates[34729]})
    checks_def.append({"type": "unit", "id": "cD25", "field": "ubertip", "expected": wts_updates[35970]})

    # cD24: Темная цитадель (Z)
    wts_updates[26279] = "|cffe4cfa3Тёмная цитадель|r"
    wts_updates[34621] = "|cffe4cfa3Тёмная цитадель|r (|cffffffffZ|r)"
    wts_updates[35969] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание третьей ступени. Обеспечивает максимальный запас пищи и открывает все технологии Культа Проклятых.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПослушник|cffced4da: базовый рабочий.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD24", "field": "name", "expected": wts_updates[26279]})
    checks_def.append({"type": "unit", "id": "cD24", "field": "tip", "expected": wts_updates[34621]})
    checks_def.append({"type": "unit", "id": "cD24", "field": "ubertip", "expected": wts_updates[35969]})

    # cD12: Распылитель чумы (A)
    wts_updates[25807] = "|cffe4cfa3Распылитель чумы|r"
    wts_updates[34548] = "|cffe4cfa3Распылитель чумы|r (|cffffffffA|r)"
    wts_updates[35943] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное и экономическое сооружение Культа Проклятых. Распыляет чуму вокруг себя, поддерживает союзную нежить и приносит регулярный доход в казну.|n|n"
        "Приносит |cffffffff+75|cffced4da ед. дохода каждые |cffffffff25|cffced4da сек.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЧумная аура|cffced4da: ускоряет регенерацию здоровья союзной нежити.|n"
        "- |cffa9c7deЧумная эссенция|cffced4da: восполняет здоровье союзникам поблизости.|n"
        "- |cffa9c7deПризрачное касание|cffced4da: восполняет ману союзным магам.|n"
        "- |cffa9c7deЗащита распылителя|cffced4da: активирует атаку строения.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD12", "field": "name", "expected": wts_updates[25807]})
    checks_def.append({"type": "unit", "id": "cD12", "field": "tip", "expected": wts_updates[34548]})
    checks_def.append({"type": "unit", "id": "cD12", "field": "ubertip", "expected": wts_updates[35943]})

    # cD29: Пристанище (W)
    wts_updates[34736] = "|cffe4cfa3Пристанище|r"
    wts_updates[34737] = "|cffe4cfa3Пристанище|r (|cffffffffW|r)"
    wts_updates[35952] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает заклинателей культа и осадные орудия, а также исследует магические посвящения.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deНекромант|cffced4da: маг костей и проклятий.|n"
        "- |cffa9c7deОсквернитель|cffced4da: маг плоти и зачумления.|n"
        "- |cffa9c7deТёмный Адепт|cffced4da: мастер ледяной магии.|n"
        "- |cffa9c7deТруповозка|cffced4da: осадное орудие и сборщик тел.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deПосвящение некромантов|cffced4da|n"
        "- |cffa9c7deПосвящение осквернителей|cffced4da|n"
        "- |cffa9c7deПосвящение адептов|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "cD29", "field": "name", "expected": wts_updates[34736]})
    checks_def.append({"type": "unit", "id": "cD29", "field": "tip", "expected": wts_updates[34737]})
    checks_def.append({"type": "unit", "id": "cD29", "field": "ubertip", "expected": wts_updates[35952]})

    # cD31: Кладбище (E)
    wts_updates[26290] = "|cffe4cfa3Кладбище|r"
    wts_updates[34752] = "|cffe4cfa3Кладбище|r (|cffffffffE|r)"
    wts_updates[35954] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит складом древесины, непрерывно производит трупы и проводит базовые улучшения войск культа.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВоскрешение слуг / Воскрешение бойцов|cffced4da: переключает автоматический призыв скелетов-лесорубов или скелетов-воинов.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deАтака костей|cffced4da|n"
        "- |cffa9c7deЗащита костей|cffced4da|n"
        "- |cffa9c7deАтака плоти|cffced4da|n"
        "- |cffa9c7deЗащита плоти|cffced4da|n"
        "- |cffa9c7deАтака магов|cffced4da|n"
        "- |cffa9c7deЗащита магов|cffced4da|n"
        "- |cffa9c7deУлучшенные инструменты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "cD31", "field": "name", "expected": wts_updates[26290]})
    checks_def.append({"type": "unit", "id": "cD31", "field": "tip", "expected": wts_updates[34752]})
    checks_def.append({"type": "unit", "id": "cD31", "field": "ubertip", "expected": wts_updates[35954]})

    # cD30: Алтарь тьмы (S)
    wts_updates[26285] = "|cffe4cfa3Алтарь тьмы|r"
    wts_updates[34751] = "|cffe4cfa3Алтарь тьмы|r (|cffffffffS|r)"
    wts_updates[35953] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит для призыва и воскрешения павших героев Культа Проклятых.|n|n"
        "|cffa6afb8Герои:|cffced4da|n"
        "- |cffa9c7deРыцарь смерти|cffced4da: могучий воин ближнего боя с нечестивой аурой и темной магией.|n"
        "- |cffa9c7deВерховный некромант|cffced4da: могущественный призыватель нежити и мастер проклятий.|n"
        "- |cffa9c7deЛич|cffced4da: маг льда дальнего боя с разрушительными заклинаниями площади.|r"
    )
    checks_def.append({"type": "unit", "id": "cD30", "field": "name", "expected": wts_updates[26285]})
    checks_def.append({"type": "unit", "id": "cD30", "field": "tip", "expected": wts_updates[34751]})
    checks_def.append({"type": "unit", "id": "cD30", "field": "ubertip", "expected": wts_updates[35953]})

    # cD28: Мясопилка (R)
    wts_updates[26283] = "|cffe4cfa3Мясопилка|r"
    wts_updates[34735] = "|cffe4cfa3Мясопилка|r (|cffffffffR|r)"
    wts_updates[35951] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Создаёт и сшивает войска из плоти, а также проводит улучшения для мясных созданий.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deЗомби|cffced4da: базовый пехотинец ближнего боя, нанимаемый парами.|n"
        "- |cffa9c7deПоганище|cffced4da: тяжелый воин с высоким запасом здоровья.|n"
        "- |cffa9c7deМясной голем|cffced4da: мощный исполин ближнего боя.|n"
        "- |cffa9c7deЯдоголем|cffced4da: ядовитый осадный голем дальнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deПлоть не убить|cffced4da|n"
        "- |cffa9c7deЯрость воскрешённых|cffced4da|n"
        "- |cffa9c7deУскоренная эксгумация|cffced4da|n"
        "- |cffa9c7deЗаражённые снаряды|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "cD28", "field": "name", "expected": wts_updates[26283]})
    checks_def.append({"type": "unit", "id": "cD28", "field": "tip", "expected": wts_updates[34735]})
    checks_def.append({"type": "unit", "id": "cD28", "field": "ubertip", "expected": wts_updates[35951]})

    # cD27: Костомолка (D)
    wts_updates[26282] = "|cffe4cfa3Костомолка|r"
    wts_updates[34733] = "|cffe4cfa3Костомолка|r (|cffffffffD|r)"
    wts_updates[35950] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает костяные войска и проводит исследования для усиления скелетов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deСкелет-воин|cffced4da: базовый костяной боец ближнего боя.|n"
        "- |cffa9c7deСкелет-маг|cffced4da: стрелок с магической атакой.|n"
        "- |cffa9c7deКостяной страж|cffced4da: закалённый костяной боец.|n"
        "- |cffa9c7deКостяной привратник|cffced4da: мощный костяной стрелок дальнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deКости всех переживут|cffced4da|n"
        "- |cffa9c7deУлучшенное оживление|cffced4da|n"
        "- |cffa9c7deЖивучие скелеты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "cD27", "field": "name", "expected": wts_updates[26282]})
    checks_def.append({"type": "unit", "id": "cD27", "field": "tip", "expected": wts_updates[34733]})
    checks_def.append({"type": "unit", "id": "cD27", "field": "ubertip", "expected": wts_updates[35950]})

    # =========================================================================
    # 3. HEROES (3 heroes)
    # =========================================================================
    # CD01: Рыцарь смерти (Q)
    wts_updates[26294] = "|cffe4cfa3Рыцарь смерти|r"
    wts_updates[35022] = "|cffe4cfa3Рыцарь смерти|r (|cffffffffQ|r)"
    wts_updates[15201] = "|cffe4cfa3Рыцарь смерти|r"
    wts_updates[23335] = "|cffe4cfa3Рыцарь смерти|r (|cffffffffQ|r)"
    wts_updates[34755] = "Леди Селендрия, Лорд Фелина"
    checks_def.append({"type": "unit", "id": "CD01", "field": "name", "expected": wts_updates[26294]})
    checks_def.append({"type": "unit", "id": "CD01", "field": "tip", "expected": wts_updates[35022]})
    checks_def.append({"type": "unit", "id": "CD01", "field": "awakentip", "expected": wts_updates[15201]})
    checks_def.append({"type": "unit", "id": "CD01", "field": "revivetip", "expected": wts_updates[23335]})
    checks_def.append({"type": "unit", "id": "CD01", "field": "propernames", "expected": wts_updates[34755]})

    # CD02: Верховный некромант (A)
    wts_updates[34787] = "|cffe4cfa3Верховный некромант|r"
    wts_updates[34758] = "|cffe4cfa3Верховный некромант|r (|cffffffffA|r)"
    wts_updates[34759] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могущественный мастер тёмных искусств. Повелевает душами и телами усопших, сокрушая врагов массовыми проклятиями и легионами нежити.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВоскрешение мёртвых|cffced4da: поднимает из трупов скелетов, вурдалаков, поганищ или рыцарей смерти.|n"
        "- |cffa9c7deСоздать труп|cffced4da: извлекает из-под земли останки для некромантии.|n"
        "- |cffa9c7deМассовое проклятие|cffced4da: наносит урон окружающим врагам и проклинает их.|n"
        "- |cffa9c7deОживление мёртвых|cffced4da: временно поднимает группу неуязвимых воинов из трупов.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    wts_updates[34756] = "|cffe4cfa3Верховный некромант|r"
    wts_updates[34757] = "|cffe4cfa3Верховный некромант|r (|cffffffffA|r)"
    wts_updates[34776] = "Джандис Барова, Леди Смертный Шепот"
    checks_def.append({"type": "unit", "id": "CD02", "field": "name", "expected": wts_updates[34787]})
    checks_def.append({"type": "unit", "id": "CD02", "field": "tip", "expected": wts_updates[34758]})
    checks_def.append({"type": "unit", "id": "CD02", "field": "ubertip", "expected": wts_updates[34759]})
    checks_def.append({"type": "unit", "id": "CD02", "field": "awakentip", "expected": wts_updates[34756]})
    checks_def.append({"type": "unit", "id": "CD02", "field": "revivetip", "expected": wts_updates[34757]})
    checks_def.append({"type": "unit", "id": "CD02", "field": "propernames", "expected": wts_updates[34776]})

    # U02X: Лич (Z)
    wts_updates[34779] = "|cffe4cfa3Лич|r"
    wts_updates[34849] = "|cffe4cfa3Лич|r (|cffffffffZ|r)"
    wts_updates[34874] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Бессмертный владыка ледяной магии. Замораживает противников, черпает ману из союзной нежити и несёт гибель вражеским армиям.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deКольцо льда|cffced4da: поражает врагов ледяной волной, нанося урон и замедляя их.|n"
        "- |cffa9c7deПоток льда|cffced4da: обрушивает шквал ледяных стрел и временно изгоняет цели в астрал.|n"
        "- |cffa9c7deТёмный ритуал|cffced4da: приносит в жертву союзную нежить, восстанавливая ману.|n"
        "- |cffa9c7deСмерть и разложение|cffced4da: наносит процентный периодический урон в области действия и уничтожает деревья.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    wts_updates[34846] = "|cffe4cfa3Лич|r"
    wts_updates[34848] = "|cffe4cfa3Лич|r (|cffffffffZ|r)"
    checks_def.append({"type": "unit", "id": "U02X", "field": "name", "expected": wts_updates[34779]})
    checks_def.append({"type": "unit", "id": "U02X", "field": "tip", "expected": wts_updates[34849]})
    checks_def.append({"type": "unit", "id": "U02X", "field": "ubertip", "expected": wts_updates[34874]})
    checks_def.append({"type": "unit", "id": "U02X", "field": "awakentip", "expected": wts_updates[34846]})
    checks_def.append({"type": "unit", "id": "U02X", "field": "revivetip", "expected": wts_updates[34848]})

    # =========================================================================
    # 4. UNITS (15 Cult units with WTS strings)
    # =========================================================================
    # cD02: Послушник (Q)
    wts_updates[22859] = "|cffe4cfa3Послушник|r"
    wts_updates[19518] = "|cffe4cfa3Послушник|r (|cffffffffQ|r)"
    wts_updates[35936] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий отряд Культа Проклятых. Добывает золото из осквернённого рудника, призывает и ремонтирует здания культа.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткое расстояние.|n"
        "- |cffa9c7deРемонт|cffced4da: восстанавливает прочность повреждённых построек.|n"
        "- |cffa9c7deРазвоплотить здание|cffced4da: уничтожает строение, возвращая часть ресурсов.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD02", "field": "name", "expected": wts_updates[22859]})
    checks_def.append({"type": "unit", "id": "cD02", "field": "tip", "expected": wts_updates[19518]})
    checks_def.append({"type": "unit", "id": "cD02", "field": "ubertip", "expected": wts_updates[35936]})

    # cD11: Зомби (Q)
    wts_updates[11015] = "|cffe4cfa3Зомби|r"
    wts_updates[34546] = "|cffe4cfa3Зомби|r (|cffffffffQ|r)"
    wts_updates[28404] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец из плоти. Нанимается сразу по двое бойцов, служит расходным материалом для армии и плотеобработки.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЗаразительная атака|cffced4da: с вероятностью |cffffffff33%|cffced4da заражает атакуемую цель чумой.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD11", "field": "name", "expected": wts_updates[11015]})
    checks_def.append({"type": "unit", "id": "cD11", "field": "tip", "expected": wts_updates[34546]})
    checks_def.append({"type": "unit", "id": "cD11", "field": "ubertip", "expected": wts_updates[28404]})

    # cD10: Поганище (W)
    wts_updates[7358] = "|cffe4cfa3Поганище|r"
    wts_updates[34542] = "|cffe4cfa3Поганище|r (|cffffffffW|r)"
    wts_updates[28403] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий и выносливый боец из сшитой плоти. Принимает на себя основной урон в бою и служит основой для сбора големов.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD10", "field": "name", "expected": wts_updates[7358]})
    checks_def.append({"type": "unit", "id": "cD10", "field": "tip", "expected": wts_updates[34542]})
    checks_def.append({"type": "unit", "id": "cD10", "field": "ubertip", "expected": wts_updates[28403]})

    # cD09: Мясной голем (E)
    wts_updates[25792] = "|cffe4cfa3Мясной голем|r"
    wts_updates[34540] = "|cffe4cfa3Мясной голем|r (|cffffffffE|r)"
    wts_updates[28399] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый исполин ближнего боя, созданный из тел павших. Обладает огромным запасом здоровья и высокой сокрушительной мощью.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD09", "field": "name", "expected": wts_updates[25792]})
    checks_def.append({"type": "unit", "id": "cD09", "field": "tip", "expected": wts_updates[34540]})
    checks_def.append({"type": "unit", "id": "cD09", "field": "ubertip", "expected": wts_updates[28399]})

    # cD14: Ядоголем (R)
    wts_updates[26131] = "|cffe4cfa3Ядоголем|r"
    wts_updates[34560] = "|cffe4cfa3Ядоголем|r (|cffffffffR|r)"
    wts_updates[28406] = (
        "|cffa6afb8ЮНИТ:|cffced4da Чумной голем дальнего боя. Атакует ядовитыми сгустками на расстоянии и заражает врагов смертоносной чумой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЗаразительные атаки|cffced4da: атаки отравляют цели и распространяют болезнь.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD14", "field": "name", "expected": wts_updates[26131]})
    checks_def.append({"type": "unit", "id": "cD14", "field": "tip", "expected": wts_updates[34560]})
    checks_def.append({"type": "unit", "id": "cD14", "field": "ubertip", "expected": wts_updates[28406]})

    # cD19: Скелет-воин (Q) (уровень 1)
    wts_updates[26200] = "|cffe4cfa3Скелет-воин|r"
    wts_updates[34570] = "|cffe4cfa3Скелет-воин|r (|cffffffffQ|r)"
    wts_updates[3065] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый костяной боец ближнего боя. Служит передовым отрядом и материалом для костесборки.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD19", "field": "name", "expected": wts_updates[26200]})
    checks_def.append({"type": "unit", "id": "cD19", "field": "tip", "expected": wts_updates[34570]})
    checks_def.append({"type": "unit", "id": "cD19", "field": "ubertip", "expected": wts_updates[3065]})

    # cD34: Скелет-воин (Q) (уровень 2)
    wts_updates[34616] = "|cffe4cfa3Скелет-воин|r"
    wts_updates[35167] = "|cffe4cfa3Скелет-воин|r (|cffffffffQ|r)"
    wts_updates[36940] = (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный костяной боец ближнего боя. Обладает повышенными боевыми характеристиками.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD34", "field": "name", "expected": wts_updates[34616]})
    checks_def.append({"type": "unit", "id": "cD34", "field": "tip", "expected": wts_updates[35167]})
    checks_def.append({"type": "unit", "id": "cD34", "field": "ubertip", "expected": wts_updates[36940]})

    # cD35: Скелет-воин (Q) (уровень 3)
    wts_updates[36972] = "|cffe4cfa3Скелет-воин|r"
    wts_updates[38639] = "|cffe4cfa3Скелет-воин|r (|cffffffffQ|r)"
    wts_updates[38641] = (
        "|cffa6afb8ЮНИТ:|cffced4da Закалённый в битвах костяной боец ближнего боя высшего уровня подготовки.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD35", "field": "name", "expected": wts_updates[36972]})
    checks_def.append({"type": "unit", "id": "cD35", "field": "tip", "expected": wts_updates[38639]})
    checks_def.append({"type": "unit", "id": "cD35", "field": "ubertip", "expected": wts_updates[38641]})

    # cD22: Скелет-маг (W)
    wts_updates[26201] = "|cffe4cfa3Скелет-маг|r"
    wts_updates[34572] = "|cffe4cfa3Скелет-маг|r (|cffffffffW|r)"
    wts_updates[28498] = (
        "|cffa6afb8ЮНИТ:|cffced4da Костяной стрелок дальнего боя. Поражает врагов магическими снарядами, эффективными против тяжёлой брони.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD22", "field": "name", "expected": wts_updates[26201]})
    checks_def.append({"type": "unit", "id": "cD22", "field": "tip", "expected": wts_updates[34572]})
    checks_def.append({"type": "unit", "id": "cD22", "field": "ubertip", "expected": wts_updates[28498]})

    # cD18: Костяной привратник (E)
    wts_updates[26173] = "|cffe4cfa3Костяной привратник|r"
    wts_updates[34566] = "|cffe4cfa3Костяной привратник|r (|cffffffffE|r)"
    wts_updates[28412] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный костяной стрелок дальнего боя. Наносит высокий урон наземным и воздушным целям.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD18", "field": "name", "expected": wts_updates[26173]})
    checks_def.append({"type": "unit", "id": "cD18", "field": "tip", "expected": wts_updates[34566]})
    checks_def.append({"type": "unit", "id": "cD18", "field": "ubertip", "expected": wts_updates[28412]})

    # cD33: Костяной страж (R)
    wts_updates[26295] = "|cffe4cfa3Костяной страж|r"
    wts_updates[34777] = "|cffe4cfa3Костяной страж|r (|cffffffffR|r)"
    wts_updates[35955] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый костяной воин ближнего боя. Может впадать в неистовство, временно ускоряя атаку и бег.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deНеистовство чужой души|cffced4da: временно увеличивает скорость атаки на |cffffffff30%|cffced4da и скорость передвижения на |cffffffff25%|cffced4da.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD33", "field": "name", "expected": wts_updates[26295]})
    checks_def.append({"type": "unit", "id": "cD33", "field": "tip", "expected": wts_updates[34777]})
    checks_def.append({"type": "unit", "id": "cD33", "field": "ubertip", "expected": wts_updates[35955]})

    # cD03: Некромант (Q)
    wts_updates[23021] = "|cffe4cfa3Некромант|r"
    wts_updates[19522] = "|cffe4cfa3Некромант|r (|cffffffffQ|r)"
    wts_updates[28392] = (
        "|cffa6afb8ЮНИТ:|cffced4da Заклинатель культа, управляющий костями и душами. Поднимает скелетов из павших, проклинает врагов и объединяет скелетов в могучих стражей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deВоскрешение мёртвых|cffced4da: поднимает скелетов из трупа.|n"
        "- |cffa9c7deКостесборка|cffced4da: собирает группу скелетов в единого мощного воина.|n"
        "- |cffa9c7deПорча изнывания|cffced4da: замедляет атаку и передвижение врага.|n"
        "- |cffa9c7deЛик смерти|cffced4da: лечит нежить или наносит урон живому врагу; требует посвящения.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD03", "field": "name", "expected": wts_updates[23021]})
    checks_def.append({"type": "unit", "id": "cD03", "field": "tip", "expected": wts_updates[19522]})
    checks_def.append({"type": "unit", "id": "cD03", "field": "ubertip", "expected": wts_updates[28392]})

    # cD05: Осквернитель (W)
    wts_updates[24412] = "|cffe4cfa3Осквернитель|r"
    wts_updates[3525] = "|cffe4cfa3Осквернитель|r (|cffffffffW|r)"
    wts_updates[28393] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тёмный алхимик и маг плоти. Заражает врагов паразитами, собирает мясных големов и ослабляет врагов порчей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЗачумление|cffced4da: заражает цель паразитом, нанося урон и призывая прислужника при её гибели.|n"
        "- |cffa9c7deПлотеобработка|cffced4da: объединяет группу мясных созданий в мощного голема.|n"
        "- |cffa9c7deПорча издыхания|cffced4da: снижает урон и броню противника.|n"
        "- |cffa9c7deТёмная стая|cffced4da: выпускает стаю летучих мышей по прямой линии; требует посвящения.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD05", "field": "name", "expected": wts_updates[24412]})
    checks_def.append({"type": "unit", "id": "cD05", "field": "tip", "expected": wts_updates[3525]})
    checks_def.append({"type": "unit", "id": "cD05", "field": "ubertip", "expected": wts_updates[28393]})

    # cD08: Темный Адепт (R)
    wts_updates[25546] = "|cffe4cfa3Тёмный Адепт|r"
    wts_updates[34386] = "|cffe4cfa3Тёмный Адепт|r (|cffffffffR|r)"
    wts_updates[28398] = (
        "|cffa6afb8ЮНИТ:|cffced4da Высший маг культа, владеющий смертоносным холодом и рассеиванием магии.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЛедяные стрелы|cffced4da: автоприменяемая атака, наносящая урон от холода и замедляющая цель.|n"
        "- |cffa9c7deКольцо льда|cffced4da: ледяная волна с уроном цели и замедлением по области.|n"
        "- |cffa9c7deМорозный доспех|cffced4da: повышает броню союзника и замедляет атакующих его врагов; требует посвящения.|n"
        "- |cffa9c7deПожирание магии|cffced4da: поглощает чары в области, восстанавливая здоровье и ману; требует посвящения.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD08", "field": "name", "expected": wts_updates[25546]})
    checks_def.append({"type": "unit", "id": "cD08", "field": "tip", "expected": wts_updates[34386]})
    checks_def.append({"type": "unit", "id": "cD08", "field": "ubertip", "expected": wts_updates[28398]})

    # cD13: Труповозка (E)
    wts_updates[25936] = "|cffe4cfa3Труповозка|r"
    wts_updates[34550] = "|cffe4cfa3Труповозка|r (|cffffffffE|r)"
    wts_updates[28405] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойное осадное орудие и сборщик тел. Перевозит и добывает трупы для некромантов, а также обстреливает вражеские укрепления заражёнными снарядами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deПогрузить труп / Выгрузить все трупы|cffced4da: загрузка и выгрузка тел.|n"
        "- |cffa9c7deЭксгумация|cffced4da: периодически выкапывает свежие тела из земли.|n"
        "- |cffa9c7deБолезнетворное облако|cffced4da: оставляет ядовитый след в месте падения снаряда; требует «Заражённых снарядов».|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "cD13", "field": "name", "expected": wts_updates[25936]})
    checks_def.append({"type": "unit", "id": "cD13", "field": "tip", "expected": wts_updates[34550]})
    checks_def.append({"type": "unit", "id": "cD13", "field": "ubertip", "expected": wts_updates[28405]})

    # =========================================================================
    # 5. UPGRADES (17 upgrades with WTS strings)
    # =========================================================================
    # R0J6: Плоть не убить (3 levels, hotkey X)
    r0j6_names = [34394, 34638, 34654]
    r0j6_tips = [34395, 34786, 34805]
    r0j6_ubs = [34806, 34807, 34808]
    r0j6_hp = [12, 24, 36]
    r0j6_reg = [30, 60, 90]
    for lvl in range(1, 4):
        wts_updates[r0j6_names[lvl-1]] = f"|cffe4cfa3Плоть не убить|r — уровень {lvl}"
        wts_updates[r0j6_tips[lvl-1]] = f"|cffe4cfa3Плоть не убить — уровень {lvl}|r (|cffffffffX|r)"
        wts_updates[r0j6_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья существ из плоти на |cffc8e087+{r0j6_hp[lvl-1]}%|cffced4da "
            f"и скорость их регенерации на |cffc8e087+{r0j6_reg[lvl-1]}%|cffced4da.|n|n"
            "Применяется к:|n- |cffa9c7deЗомби|cffced4da, |cffa9c7deПоганище|cffced4da, |cffa9c7deМясной голем|cffced4da, |cffa9c7deЯдоголем|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0J6", "field": f"name{lvl}", "expected": wts_updates[r0j6_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J6", "field": f"tip{lvl}", "expected": wts_updates[r0j6_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J6", "field": f"ubertip{lvl}", "expected": wts_updates[r0j6_ubs[lvl-1]]})

    # R0J7: Улучшенные инструменты (4 levels, hotkey X)
    r0j7_names = [34814, 34815, 34816, 34817]
    r0j7_tips = [34820, 34821, 34822, 34823]
    r0j7_ubs = [28317, 28314, 28315, 28316]
    r0j7_lum = [8, 16, 24, 32]
    for lvl in range(1, 5):
        wts_updates[r0j7_names[lvl-1]] = f"|cffe4cfa3Улучшенные инструменты|r — уровень {lvl}"
        wts_updates[r0j7_tips[lvl-1]] = f"|cffe4cfa3Улучшенные инструменты — уровень {lvl}|r (|cffffffffX|r)"
        wts_updates[r0j7_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает вместимость переносимой рабочими древесины на |cffc8e087+{r0j7_lum[lvl-1]}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deПослушник|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0J7", "field": f"name{lvl}", "expected": wts_updates[r0j7_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J7", "field": f"tip{lvl}", "expected": wts_updates[r0j7_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J7", "field": f"ubertip{lvl}", "expected": wts_updates[r0j7_ubs[lvl-1]]})

    # R0J8: Кости всех переживут (3 levels, hotkey Z)
    r0j8_names = [34889, 34894, 34895]
    r0j8_tips = [34890, 34896, 34897]
    r0j8_ubs = [38431, 38432, 38433]
    r0j8_hp = [9, 18, 27]
    for lvl in range(1, 4):
        wts_updates[r0j8_names[lvl-1]] = f"|cffe4cfa3Кости всех переживут|r — уровень {lvl}"
        wts_updates[r0j8_tips[lvl-1]] = f"|cffe4cfa3Кости всех переживут — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0j8_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья костяных существ на |cffc8e087+{r0j8_hp[lvl-1]}%|cffced4da.|n|n"
            "Применяется к:|n- |cffa9c7deСкелет-воин|cffced4da, |cffa9c7deСкелет-маг|cffced4da, |cffa9c7deКостяной привратник|cffced4da, |cffa9c7deКостяной страж|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0J8", "field": f"name{lvl}", "expected": wts_updates[r0j8_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J8", "field": f"tip{lvl}", "expected": wts_updates[r0j8_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J8", "field": f"ubertip{lvl}", "expected": wts_updates[r0j8_ubs[lvl-1]]})

    # R0JH: Посвящение некромантов (4 levels, hotkey Z)
    r0jh_names = [34620, 35140, 35141, 35142]
    r0jh_tips = [35143, 35144, 35145, 35146]
    r0jh_ubs = [35147, 35148, 35149, 35150]
    for lvl in range(1, 5):
        wts_updates[r0jh_names[lvl-1]] = f"|cffe4cfa3Посвящение некромантов|r — ступень {lvl}"
        wts_updates[r0jh_tips[lvl-1]] = f"|cffe4cfa3Посвящение некромантов — ступень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0jh_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, ману и регенерацию маны некромантов, "
            f"открывает доступ к заклинанию «Лик смерти» и повышает эффективность «Костесборки» на |cffc8e087+{lvl * 5}%|cffced4da.|n|n"
            "Применяется к:|n- |cffa9c7deНекромант|cffced4da.|n|n"
            f"Ступень посвящения: |cffffffff{lvl}|cffced4da/|cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0JH", "field": f"name{lvl}", "expected": wts_updates[r0jh_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0JH", "field": f"tip{lvl}", "expected": wts_updates[r0jh_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0JH", "field": f"ubertip{lvl}", "expected": wts_updates[r0jh_ubs[lvl-1]]})

    # R0JI: Зараженные снаряды (1 level, hotkey S)
    wts_updates[35542] = "|cffe4cfa3Заражённые снаряды|r"
    wts_updates[35545] = "|cffe4cfa3Заражённые снаряды|r (|cffffffffS|r)"
    wts_updates[35546] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Снаряды труповозок создают в точке падения ядовитые болезнетворные облака, "
        "заражающие вражеских юнитов чумой и наносящие периодический урон.|n|n"
        "Применяется к:|n- |cffa9c7deТруповозка|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0JI", "field": "name1", "expected": wts_updates[35542]})
    checks_def.append({"type": "upgrade", "id": "R0JI", "field": "tip1", "expected": wts_updates[35545]})
    checks_def.append({"type": "upgrade", "id": "R0JI", "field": "ubertip1", "expected": wts_updates[35546]})

    # R0K4: Улучшенное оживление (2 levels, hotkey A)
    r0k4_names = [36945, 36949]
    r0k4_tips = [36947, 36950]
    r0k4_ubs = [38819, 38820]
    for lvl in range(1, 3):
        wts_updates[r0k4_names[lvl-1]] = f"|cffe4cfa3Улучшенное оживление|r — уровень {lvl}"
        wts_updates[r0k4_tips[lvl-1]] = f"|cffe4cfa3Улучшенное оживление — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r0k4_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Совершенствует мастерство некромантии, позволяя заклинателям поднимать "
            f"более мощных скелетов-воинов {lvl + 1}-го уровня из павших тел.|n|n"
            "Применяется к:|n- |cffa9c7deНекромант|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff2|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0K4", "field": f"name{lvl}", "expected": wts_updates[r0k4_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0K4", "field": f"tip{lvl}", "expected": wts_updates[r0k4_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0K4", "field": f"ubertip{lvl}", "expected": wts_updates[r0k4_ubs[lvl-1]]})

    # R0KE: Живучие скелеты (3 levels, hotkey X)
    r0ke_names = [34663, 36937, 36936]
    r0ke_tips = [34664, 36938, 36939]
    r0ke_ubs = [38824, 38825, 38826]
    r0ke_time = [15, 30, 45]
    for lvl in range(1, 4):
        wts_updates[r0ke_names[lvl-1]] = f"|cffe4cfa3Живучие скелеты|r — уровень {lvl}"
        wts_updates[r0ke_tips[lvl-1]] = f"|cffe4cfa3Живучие скелеты — уровень {lvl}|r (|cffffffffX|r)"
        wts_updates[r0ke_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Продлевает время существования призванных скелетов на |cffc8e087+{r0ke_time[lvl-1]}|cffced4da сек.|n|n"
            "Применяется к:|n- |cffa9c7deСкелет-воин|cffced4da, |cffa9c7deСкелет-маг|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0KE", "field": f"name{lvl}", "expected": wts_updates[r0ke_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0KE", "field": f"tip{lvl}", "expected": wts_updates[r0ke_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0KE", "field": f"ubertip{lvl}", "expected": wts_updates[r0ke_ubs[lvl-1]]})

    # cDR4: Атака магов (6 levels, hotkey E)
    cdr4_names = [34250, 34251, 34252, 34253, 34254, 34255]
    cdr4_tips = [31219, 31223, 31224, 31227, 32377, 32381]
    cdr4_ubs = [34263, 34347, 34348, 34349, 34350, 34351]
    for lvl in range(1, 7):
        wts_updates[cdr4_names[lvl-1]] = f"|cffe4cfa3Атака магов|r — уровень {lvl}"
        wts_updates[cdr4_tips[lvl-1]] = f"|cffe4cfa3Атака магов — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[cdr4_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон магических атак заклинателей культа на |cffc8e087+{lvl * 3}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deНекромант|cffced4da, |cffa9c7deОсквернитель|cffced4da, |cffa9c7deТёмный Адепт|cffced4da, |cffa9c7deСкелет-маг|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDR4", "field": f"name{lvl}", "expected": wts_updates[cdr4_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR4", "field": f"tip{lvl}", "expected": wts_updates[cdr4_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR4", "field": f"ubertip{lvl}", "expected": wts_updates[cdr4_ubs[lvl-1]]})

    # cDR5: Посвящение осквернителей (4 levels, hotkey X)
    cdr5_names = [34631, 34632, 35118, 35119]
    cdr5_tips = [35121, 35122, 35123, 35124]
    cdr5_ubs = [35125, 35126, 35127, 35128]
    for lvl in range(1, 5):
        wts_updates[cdr5_names[lvl-1]] = f"|cffe4cfa3Посвящение осквернителей|r — ступень {lvl}"
        wts_updates[cdr5_tips[lvl-1]] = f"|cffe4cfa3Посвящение осквернителей — ступень {lvl}|r (|cffffffffX|r)"
        wts_updates[cdr5_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, ману и регенерацию маны осквернителей, "
            f"открывает доступ к заклинанию «Тёмная стая» и повышает эффективность «Плотеобработки» на |cffc8e087+{lvl * 5}%|cffced4da.|n|n"
            "Применяется к:|n- |cffa9c7deОсквернитель|cffced4da.|n|n"
            f"Ступень посвящения: |cffffffff{lvl}|cffced4da/|cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDR5", "field": f"name{lvl}", "expected": wts_updates[cdr5_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR5", "field": f"tip{lvl}", "expected": wts_updates[cdr5_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR5", "field": f"ubertip{lvl}", "expected": wts_updates[cdr5_ubs[lvl-1]]})

    # cDR8: Посвящение адептов (4 levels, hotkey C)
    cdr8_names = [34594, 34595, 34596, 34597]
    cdr8_tips = [34850, 34876, 34877, 34878]
    cdr8_ubs = [35151, 35152, 35153, 35154]
    for lvl in range(1, 5):
        wts_updates[cdr8_names[lvl-1]] = f"|cffe4cfa3Посвящение адептов|r — ступень {lvl}"
        wts_updates[cdr8_tips[lvl-1]] = f"|cffe4cfa3Посвящение адептов — ступень {lvl}|r (|cffffffffC|r)"
        wts_updates[cdr8_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, ману и регенерацию маны тёмных адептов, "
            f"а также открывает заклинания «Морозный доспех» и «Пожирание магии».|n|n"
            "Применяется к:|n- |cffa9c7deТёмный Адепт|cffced4da.|n|n"
            f"Ступень посвящения: |cffffffff{lvl}|cffced4da/|cffffffff4|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDR8", "field": f"name{lvl}", "expected": wts_updates[cdr8_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR8", "field": f"tip{lvl}", "expected": wts_updates[cdr8_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR8", "field": f"ubertip{lvl}", "expected": wts_updates[cdr8_ubs[lvl-1]]})

    # cDR9: Защита магов (6 levels, hotkey D)
    cdr9_names = [34356, 34357, 34358, 34359, 34360, 34361]
    cdr9_tips = [35072, 35051, 35052, 35053, 35054, 35061]
    cdr9_ubs = [35161, 35162, 35163, 35164, 35165, 35166]
    for lvl in range(1, 7):
        wts_updates[cdr9_names[lvl-1]] = f"|cffe4cfa3Защита магов|r — уровень {lvl}"
        wts_updates[cdr9_tips[lvl-1]] = f"|cffe4cfa3Защита магов — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[cdr9_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню заклинателей культа на |cffc8e087+{lvl * 2}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deНекромант|cffced4da, |cffa9c7deОсквернитель|cffced4da, |cffa9c7deТёмный Адепт|cffced4da, |cffa9c7deСкелет-маг|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDR9", "field": f"name{lvl}", "expected": wts_updates[cdr9_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR9", "field": f"tip{lvl}", "expected": wts_updates[cdr9_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDR9", "field": f"ubertip{lvl}", "expected": wts_updates[cdr9_ubs[lvl-1]]})

    # cDr0: Атака костей (6 levels, hotkey W)
    cdr0_names = [34474, 34475, 34476, 34477, 34478, 34479]
    cdr0_tips = [34486, 34487, 34488, 34489, 34490, 34491]
    cdr0_ubs = [34492, 34493, 34494, 34495, 34496, 34497]
    for lvl in range(1, 7):
        wts_updates[cdr0_names[lvl-1]] = f"|cffe4cfa3Атака костей|r — уровень {lvl}"
        wts_updates[cdr0_tips[lvl-1]] = f"|cffe4cfa3Атака костей — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[cdr0_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак костяных созданий на |cffc8e087+{lvl * 3}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deСкелет-воин|cffced4da, |cffa9c7deКостяной привратник|cffced4da, |cffa9c7deКостяной страж|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDr0", "field": f"name{lvl}", "expected": wts_updates[cdr0_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr0", "field": f"tip{lvl}", "expected": wts_updates[cdr0_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr0", "field": f"ubertip{lvl}", "expected": wts_updates[cdr0_ubs[lvl-1]]})

    # cDr1: Защита костей (6 levels, hotkey S)
    cdr1_names = [34498, 34499, 34500, 34501, 34502, 34503]
    cdr1_tips = [34510, 34511, 34512, 34513, 34514, 34515]
    cdr1_ubs = [34516, 34517, 34518, 34519, 34520, 34521]
    for lvl in range(1, 7):
        wts_updates[cdr1_names[lvl-1]] = f"|cffe4cfa3Защита костей|r — уровень {lvl}"
        wts_updates[cdr1_tips[lvl-1]] = f"|cffe4cfa3Защита костей — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[cdr1_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню костяных созданий на |cffc8e087+{lvl * 2}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deСкелет-воин|cffced4da, |cffa9c7deКостяной привратник|cffced4da, |cffa9c7deКостяной страж|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDr1", "field": f"name{lvl}", "expected": wts_updates[cdr1_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr1", "field": f"tip{lvl}", "expected": wts_updates[cdr1_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr1", "field": f"ubertip{lvl}", "expected": wts_updates[cdr1_ubs[lvl-1]]})

    # cDr3: Атака плоти (6 levels, hotkey Q)
    cdr3_names = [34522, 34523, 34524, 34525, 34526, 34527]
    cdr3_tips = [34534, 34535, 34536, 35089, 35099, 35100]
    cdr3_ubs = [35101, 35102, 35103, 35104, 35105, 35106]
    for lvl in range(1, 7):
        wts_updates[cdr3_names[lvl-1]] = f"|cffe4cfa3Атака плоти|r — уровень {lvl}"
        wts_updates[cdr3_tips[lvl-1]] = f"|cffe4cfa3Атака плоти — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[cdr3_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак созданий из плоти на |cffc8e087+{lvl * 3}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deЗомби|cffced4da, |cffa9c7deПоганище|cffced4da, |cffa9c7deМясной голем|cffced4da, |cffa9c7deЯдоголем|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDr3", "field": f"name{lvl}", "expected": wts_updates[cdr3_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr3", "field": f"tip{lvl}", "expected": wts_updates[cdr3_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr3", "field": f"ubertip{lvl}", "expected": wts_updates[cdr3_ubs[lvl-1]]})

    # cDr4: Защита плоти (6 levels, hotkey A)
    cdr4_names = [34234, 34235, 34236, 34237, 34244, 34245]
    cdr4_tips = [35107, 35108, 35109, 35110, 35111, 38830]
    cdr4_ubs = [35039, 35040, 35041, 35042, 35112, 35113]
    for lvl in range(1, 7):
        wts_updates[cdr4_names[lvl-1]] = f"|cffe4cfa3Защита плоти|r — уровень {lvl}"
        wts_updates[cdr4_tips[lvl-1]] = f"|cffe4cfa3Защита плоти — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[cdr4_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню созданий из плоти на |cffc8e087+{lvl * 2}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deЗомби|cffced4da, |cffa9c7deПоганище|cffced4da, |cffa9c7deМясной голем|cffced4da, |cffa9c7deЯдоголем|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDr4", "field": f"name{lvl}", "expected": wts_updates[cdr4_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr4", "field": f"tip{lvl}", "expected": wts_updates[cdr4_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr4", "field": f"ubertip{lvl}", "expected": wts_updates[cdr4_ubs[lvl-1]]})

    # cDr6: Ярость воскрешенных (3 levels, hotkey Z)
    cdr6_names = [34669, 34698, 34699]
    cdr6_tips = [34704, 34705, 34706]
    cdr6_ubs = [34387, 34388, 34389]
    cdr6_speed = [12, 24, 36]
    for lvl in range(1, 4):
        wts_updates[cdr6_names[lvl-1]] = f"|cffe4cfa3Ярость воскрешённых|r — уровень {lvl}"
        wts_updates[cdr6_tips[lvl-1]] = f"|cffe4cfa3Ярость воскрешённых — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[cdr6_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки созданий из плоти на |cffc8e087+{cdr6_speed[lvl-1]}%|cffced4da.|n|n"
            "Применяется к:|n- |cffa9c7deЗомби|cffced4da, |cffa9c7deПоганище|cffced4da, |cffa9c7deМясной голем|cffced4da, |cffa9c7deЯдоголем|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "cDr6", "field": f"name{lvl}", "expected": wts_updates[cdr6_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr6", "field": f"tip{lvl}", "expected": wts_updates[cdr6_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "cDr6", "field": f"ubertip{lvl}", "expected": wts_updates[cdr6_ubs[lvl-1]]})

    # cDr7: Ускоренная эсгумация (1 level, hotkey A)
    wts_updates[34718] = "|cffe4cfa3Ускоренная эксгумация|r"
    wts_updates[34392] = "|cffe4cfa3Ускоренная эксгумация|r (|cffffffffA|r)"
    wts_updates[34393] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Сокращает интервал автоматической эксгумации тел труповозками с |cffffffff30|cffced4da до |cffffffff15|cffced4da сек.|n|n"
        "Применяется к:|n- |cffa9c7deТруповозка|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "cDr7", "field": "name1", "expected": wts_updates[34718]})
    checks_def.append({"type": "upgrade", "id": "cDr7", "field": "tip1", "expected": wts_updates[34392]})
    checks_def.append({"type": "upgrade", "id": "cDr7", "field": "ubertip1", "expected": wts_updates[34393]})

    # =========================================================================
    # 6. ABILITIES (43 abilities with WTS strings)
    # =========================================================================
    # A0CL: Создать Труп (Hero ability of CD02, 4 lvls, hotkey W)
    wts_updates[8955] = "|cffe4cfa3Создать труп|r"
    wts_updates[8956] = "|cffe4cfa3Создать труп|r (|cffffffffW|r)"
    wts_updates[15488] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Извлекает из-под земли останки для нужд некромантии.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff1|cffced4da труп, перезарядка |cffffffff32|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff2|cffced4da трупа, перезарядка |cffffffff32|cffced4da сек.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff3|cffced4da трупа, перезарядка |cffffffff32|cffced4da сек.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff4|cffced4da трупа, перезарядка |cffffffff35|cffced4da сек.|r"
    )
    a0cl_tips = [8958, 8963, 8964, 8962]
    a0cl_ubs = [15493, 15485, 15486, 15487]
    a0cl_cd = [32, 32, 32, 35]
    for lvl in range(1, 5):
        wts_updates[a0cl_tips[lvl-1]] = f"|cffe4cfa3Создать труп — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0cl_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Извлекает из глубин земли |cffffffff{lvl}|cffced4da труп(а) для использования в некромантии.|n|n"
            f"Расход маны: |cffffffff150|cffced4da. Перезарядка: |cffffffff{a0cl_cd[lvl-1]}|cffced4da сек.|r"
        )
        checks_def.append({"type": "ability", "id": "A0CL", "field": f"tip{lvl}", "expected": wts_updates[a0cl_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0CL", "field": f"ubertip{lvl}", "expected": wts_updates[a0cl_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0CL", "field": "name", "expected": wts_updates[8955]})
    checks_def.append({"type": "ability", "id": "A0CL", "field": "researchtip", "expected": wts_updates[8956]})
    checks_def.append({"type": "ability", "id": "A0CL", "field": "researchubertip", "expected": wts_updates[15488]})

    # A0CM: Массовое проклятие (Hero ability of CD02, 4 lvls, hotkey E)
    wts_updates[8971] = "|cffe4cfa3Массовое проклятие|r"
    wts_updates[41279] = "|cffe4cfa3Массовое проклятие|r (|cffffffffE|r)"
    wts_updates[41305] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает всех врагов поблизости, нанося им мгновенный урон.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff100|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff150|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff200|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff250|cffced4da ед. урона.|r"
    )
    a0cm_tips = [8972, 8973, 8974, 8975]
    a0cm_ubs = [41290, 41291, 41292, 41293]
    a0cm_dmg = [100, 150, 200, 250]
    a0cm_cd = [15, 20, 26, 30]
    for lvl in range(1, 5):
        wts_updates[a0cm_tips[lvl-1]] = f"|cffe4cfa3Массовое проклятие — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[a0cm_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff{a0cm_dmg[lvl-1]}|cffced4da ед. урона всем вражеским войскам вокруг героя в радиусе |cffffffff800|cffced4da.|n|n"
            f"Расход маны: |cffffffff125|cffced4da. Перезарядка: |cffffffff{a0cm_cd[lvl-1]}|cffced4da сек.|r"
        )
        checks_def.append({"type": "ability", "id": "A0CM", "field": f"tip{lvl}", "expected": wts_updates[a0cm_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0CM", "field": f"ubertip{lvl}", "expected": wts_updates[a0cm_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0CM", "field": "name", "expected": wts_updates[8971]})
    checks_def.append({"type": "ability", "id": "A0CM", "field": "researchtip", "expected": wts_updates[41279]})
    checks_def.append({"type": "ability", "id": "A0CM", "field": "researchubertip", "expected": wts_updates[41305]})

    # A0CN: Оживление мертвых (Hero ultimate of CD02, 2 lvls, hotkey R)
    wts_updates[8992] = "|cffe4cfa3Оживление мёртвых|r"
    wts_updates[8993] = "|cffe4cfa3Оживление мёртвых|r (|cffffffffR|r)"
    wts_updates[15500] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает из трупов неуязвимых бойцов, сражающихся на стороне героя.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff8|cffced4da трупов.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff12|cffced4da трупов.|r"
    )
    a0cn_tips = [8994, 8995]
    a0cn_ubs = [13587, 13547]
    a0cn_cnt = [8, 12]
    for lvl in range(1, 3):
        wts_updates[a0cn_tips[lvl-1]] = f"|cffe4cfa3Оживление мёртвых — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[a0cn_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает до |cffffffff{a0cn_cnt[lvl-1]}|cffced4da трупов в области действия в виде неуязвимых воинов, сражающихся на стороне героя.|r"
        )
        checks_def.append({"type": "ability", "id": "A0CN", "field": f"tip{lvl}", "expected": wts_updates[a0cn_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0CN", "field": f"ubertip{lvl}", "expected": wts_updates[a0cn_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0CN", "field": "name", "expected": wts_updates[8992]})
    checks_def.append({"type": "ability", "id": "A0CN", "field": "researchtip", "expected": wts_updates[8993]})
    checks_def.append({"type": "ability", "id": "A0CN", "field": "researchubertip", "expected": wts_updates[15500]})

    # A0CO: Лик смерти (Hero ability of CD01, 4 lvls, hotkey Q)
    wts_updates[9006] = "|cffe4cfa3Лик смерти|r"
    wts_updates[9007] = "|cffe4cfa3Лик смерти|r (|cffffffffQ|r)"
    wts_updates[15504] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит урон живому врагу или исцеляет союзника-нежить.|n|n"
        "|cffa6afb8Уровень 1:|r лечение |cffc8e087200|cffced4da или |cffffffff100|cffced4da урона.|n"
        "|cffa6afb8Уровень 2:|r лечение |cffc8e087400|cffced4da или |cffffffff200|cffced4da урона.|n"
        "|cffa6afb8Уровень 3:|r лечение |cffc8e087600|cffced4da или |cffffffff300|cffced4da урона.|n"
        "|cffa6afb8Уровень 4:|r лечение |cffc8e087800|cffced4da или |cffffffff400|cffced4da урона.|r"
    )
    a0co_tips = [15505, 15506, 15507, 15502]
    a0co_ubs = [15508, 15509, 15510, 15503]
    a0co_heal = [200, 400, 600, 800]
    a0co_dmg = [100, 200, 300, 400]
    for lvl in range(1, 5):
        wts_updates[a0co_tips[lvl-1]] = f"|cffe4cfa3Лик смерти — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a0co_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087{a0co_heal[lvl-1]}|cffced4da ед. здоровья союзнику-нежити "
            f"или наносит |cffffffff{a0co_dmg[lvl-1]}|cffced4da ед. урона живому противнику.|n|n"
            "Расход маны: |cffffffff75|cffced4da. Перезарядка: |cffffffff6|cffced4da сек.|r"
        )
        checks_def.append({"type": "ability", "id": "A0CO", "field": f"tip{lvl}", "expected": wts_updates[a0co_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0CO", "field": f"ubertip{lvl}", "expected": wts_updates[a0co_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0CO", "field": "name", "expected": wts_updates[9006]})
    checks_def.append({"type": "ability", "id": "A0CO", "field": "researchtip", "expected": wts_updates[9007]})
    checks_def.append({"type": "ability", "id": "A0CO", "field": "researchubertip", "expected": wts_updates[15504]})

    # A0CP: Зов смерти (Hero ability of CD01, 4 lvls, hotkey W)
    wts_updates[9010] = "|cffe4cfa3Зов смерти|r"
    wts_updates[1267] = "|cffe4cfa3Зов смерти|r (|cffffffffW|r)"
    wts_updates[15514] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзных войск поблизости на |cffffffff45|cffced4da сек.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+15%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+20%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+25%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+35%|cffced4da к урону.|r"
    )
    a0cp_tips = [9011, 9012, 9013, 9014]
    a0cp_ubs = [15515, 15511, 15512, 15513]
    a0cp_dmg = [15, 20, 25, 35]
    for lvl in range(1, 5):
        wts_updates[a0cp_tips[lvl-1]] = f"|cffe4cfa3Зов смерти — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0cp_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает атакуемый урон находящихся рядом союзных войск на |cffc8e087+{a0cp_dmg[lvl-1]}%|cffced4da на |cffffffff45|cffced4da сек.|r"
        )
        checks_def.append({"type": "ability", "id": "A0CP", "field": f"tip{lvl}", "expected": wts_updates[a0cp_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0CP", "field": f"ubertip{lvl}", "expected": wts_updates[a0cp_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0CP", "field": "name", "expected": wts_updates[9010]})
    checks_def.append({"type": "ability", "id": "A0CP", "field": "researchtip", "expected": wts_updates[1267]})
    checks_def.append({"type": "ability", "id": "A0CP", "field": "researchubertip", "expected": wts_updates[15514]})

    # A0CQ: Пожирание (Hero ultimate of CD01, 2 lvls, hotkey R)
    wts_updates[9049] = "|cffe4cfa3Пожирание|r"
    wts_updates[9050] = "|cffe4cfa3Пожирание|r (|cffffffffR|r)"
    wts_updates[16074] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну тёмных духов, поражающих окружающих противников.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff300|cffced4da урона, до |cffffffff18|cffced4da целей.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff450|cffced4da урона, до |cffffffff25|cffced4da целей.|r"
    )
    a0cq_tips = [9051, 9052]
    a0cq_ubs = [40049, 40050]
    a0cq_dmg = [300, 450]
    a0cq_cnt = [18, 25]
    for lvl in range(1, 3):
        wts_updates[a0cq_tips[lvl-1]] = f"|cffe4cfa3Пожирание — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[a0cq_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну тёмных духов, наносящих по |cffffffff{a0cq_dmg[lvl-1]}|cffced4da ед. урона "
            f"каждому противнику вокруг героя (до |cffffffff{a0cq_cnt[lvl-1]}|cffced4da целей).|r"
        )
        checks_def.append({"type": "ability", "id": "A0CQ", "field": f"tip{lvl}", "expected": wts_updates[a0cq_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0CQ", "field": f"ubertip{lvl}", "expected": wts_updates[a0cq_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0CQ", "field": "name", "expected": wts_updates[9049]})
    checks_def.append({"type": "ability", "id": "A0CQ", "field": "researchtip", "expected": wts_updates[9050]})
    checks_def.append({"type": "ability", "id": "A0CQ", "field": "researchubertip", "expected": wts_updates[16074]})

    # A0CR: Нечистая аура (Hero aura of CD01, 4 lvls, hotkey E)
    wts_updates[9066] = "|cffe4cfa3Нечистая аура|r"
    wts_updates[9067] = "|cffe4cfa3Нечистая аура|r (|cffffffffE|r)"
    wts_updates[15523] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно ускоряет передвижение и регенерацию здоровья союзников поблизости.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+10%|cffced4da к скорости, |cffc8e087+1|cffced4da хп/сек.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+15%|cffced4da к скорости, |cffc8e087+2|cffced4da хп/сек.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+20%|cffced4da к скорости, |cffc8e087+3|cffced4da хп/сек.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+25%|cffced4da к скорости, |cffc8e087+4|cffced4da хп/сек.|r"
    )
    a0cr_tips = [9070, 9071, 9072, 9068]
    a0cr_ubs = [15520, 15521, 15522, 15519]
    a0cr_spd = [10, 15, 20, 25]
    for lvl in range(1, 5):
        wts_updates[a0cr_tips[lvl-1]] = f"|cffe4cfa3Нечистая аура — уровень {lvl}|r"
        wts_updates[a0cr_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения союзных войск на |cffc8e087+{a0cr_spd[lvl-1]}%|cffced4da "
            "и повышает скорость восстановления их здоровья.|r"
        )
        checks_def.append({"type": "ability", "id": "A0CR", "field": f"tip{lvl}", "expected": wts_updates[a0cr_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0CR", "field": f"ubertip{lvl}", "expected": wts_updates[a0cr_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0CR", "field": "name", "expected": wts_updates[9066]})
    checks_def.append({"type": "ability", "id": "A0CR", "field": "researchtip", "expected": wts_updates[9067]})
    checks_def.append({"type": "ability", "id": "A0CR", "field": "researchubertip", "expected": wts_updates[15523]})

    # A0I3: Небольшой скачок (hotkey C, 1 lvl)
    wts_updates[26484] = "|cffe4cfa3Небольшой скачок|r"
    wts_updates[10064] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[10976] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает строителя на короткое расстояние.|r"
    wts_updates[26476] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[26477] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает строителя на короткое расстояние.|r"
    checks_def.append({"type": "ability", "id": "A0I3", "field": "name", "expected": wts_updates[26484]})
    checks_def.append({"type": "ability", "id": "A0I3", "field": "tip1", "expected": wts_updates[26476]})
    checks_def.append({"type": "ability", "id": "A0I3", "field": "ubertip1", "expected": wts_updates[26477]})

    # A0IQ: Обозначить столицу (hotkey X, 1 lvl)
    wts_updates[27193] = "|cffe4cfa3Обозначить столицу|r"
    wts_updates[27969] = "|cffe4cfa3Обозначить столицу|r (|cffffffffX|r)"
    wts_updates[27970] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обозначает главное здание в качестве столицы фракции, существенно увеличивая его запас прочности. "
        "При уничтожении столицы игрок терпит поражение либо становится вассалом победителя (в зависимости от настроек партии).|n|n"
        "|cffe6c07bЕсли столица не выбрана в течение первых 10 минут игры, она будет назначена автоматически.|r"
    )
    checks_def.append({"type": "ability", "id": "A0IQ", "field": "name", "expected": wts_updates[27193]})
    checks_def.append({"type": "ability", "id": "A0IQ", "field": "tip1", "expected": wts_updates[27969]})
    checks_def.append({"type": "ability", "id": "A0IQ", "field": "ubertip1", "expected": wts_updates[27970]})

    # A0LI: Обмен Золота на Дерево (hotkey S, 1 lvl)
    wts_updates[2888] = "|cffe4cfa3Обмен золота на дерево|r"
    wts_updates[3692] = "|cffe4cfa3Обмен золота на дерево|r (|cffffffffS|r)"
    wts_updates[20630] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обменивает |cffffffff500|cffced4da ед. золота на |cffffffff100|cffced4da ед. древесины.|r"
    checks_def.append({"type": "ability", "id": "A0LI", "field": "name", "expected": wts_updates[2888]})
    checks_def.append({"type": "ability", "id": "A0LI", "field": "tip1", "expected": wts_updates[3692]})
    checks_def.append({"type": "ability", "id": "A0LI", "field": "ubertip1", "expected": wts_updates[20630]})

    # A0LJ: Обмен Дерева на Золото (hotkey A, 1 lvl)
    wts_updates[12857] = "|cffe4cfa3Обмен дерева на золото|r"
    wts_updates[12886] = "|cffe4cfa3Обмен дерева на золото|r (|cffffffffA|r)"
    wts_updates[20631] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обменивает |cffffffff500|cffced4da ед. древесины на |cffffffff100|cffced4da ед. золота.|r"
    checks_def.append({"type": "ability", "id": "A0LJ", "field": "name", "expected": wts_updates[12857]})
    checks_def.append({"type": "ability", "id": "A0LJ", "field": "tip1", "expected": wts_updates[12886]})
    checks_def.append({"type": "ability", "id": "A0LJ", "field": "ubertip1", "expected": wts_updates[20631]})

    # A1HC: Защита распылителя (hotkey R, 1 lvl)
    wts_updates[34230] = "|cffe4cfa3Защита распылителя|r"
    wts_updates[34231] = "|cffe4cfa3Защита распылителя|r (|cffffffffR|r)"
    wts_updates[9513] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует орудия распылителя чумы на |cffffffff22|cffced4da сек., позволяя строению атаковать наземные и воздушные цели.|r"
    checks_def.append({"type": "ability", "id": "A1HC", "field": "name", "expected": wts_updates[34230]})
    checks_def.append({"type": "ability", "id": "A1HC", "field": "tip1", "expected": wts_updates[34231]})
    checks_def.append({"type": "ability", "id": "A1HC", "field": "ubertip1", "expected": wts_updates[9513]})

    # A1HE: Поток льда (Hero ability of U02X, 4 lvls, hotkey W)
    wts_updates[34372] = "|cffe4cfa3Поток льда|r"
    wts_updates[34379] = "|cffe4cfa3Поток льда|r (|cffffffffW|r)"
    wts_updates[34380] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на цели в указанной области ледяной шквал, нанося урон и временно изгоняя их в астральный план.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff75|cffced4da урона.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff150|cffced4da урона.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff225|cffced4da урона.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff300|cffced4da урона и изгнание в астрал.|r"
    )
    a1he_tips = [34370, 34373, 34374, 34375]
    a1he_ubs = [34371, 34376, 34377, 34378]
    a1he_dmg = [75, 150, 225, 300]
    for lvl in range(1, 4):
        wts_updates[a1he_tips[lvl-1]] = f"|cffe4cfa3Поток льда — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a1he_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цели в выбранной области потоком ледяных стрел, нанося им |cffffffff{a1he_dmg[lvl-1]}|cffced4da ед. урона.|r"
        )
        checks_def.append({"type": "ability", "id": "A1HE", "field": f"tip{lvl}", "expected": wts_updates[a1he_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A1HE", "field": f"ubertip{lvl}", "expected": wts_updates[a1he_ubs[lvl-1]]})
    wts_updates[34375] = "|cffe4cfa3Поток льда — уровень 4|r (|cffffffffW|r)"
    wts_updates[34378] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цели в области ледяным шквалом на |cffffffff300|cffced4da ед. урона "
        "и временно изгоняет их в астрал, делая неуязвимыми к физическим атакам, но восприимчивыми к магии.|r"
    )
    checks_def.append({"type": "ability", "id": "A1HE", "field": "tip4", "expected": wts_updates[34375]})
    checks_def.append({"type": "ability", "id": "A1HE", "field": "ubertip4", "expected": wts_updates[34378]})
    checks_def.append({"type": "ability", "id": "A1HE", "field": "name", "expected": wts_updates[34372]})
    checks_def.append({"type": "ability", "id": "A1HE", "field": "researchtip", "expected": wts_updates[34379]})
    checks_def.append({"type": "ability", "id": "A1HE", "field": "researchubertip", "expected": wts_updates[34380]})

    # A1HH: Темная стая (cD05, hotkey E, 1 lvl)
    wts_updates[34869] = "|cffe4cfa3Тёмная стая|r"
    wts_updates[34870] = "|cffe4cfa3Тёмная стая|r (|cffffffffE|r)"
    wts_updates[35073] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает рой нетопырей по прямой линии, наносящих по |cffffffff70|cffced4da ед. урона каждому поражённому наземному противнику (максимум |cffffffff300|cffced4da урона).|r"
    checks_def.append({"type": "ability", "id": "A1HH", "field": "name", "expected": wts_updates[34869]})
    checks_def.append({"type": "ability", "id": "A1HH", "field": "tip1", "expected": wts_updates[34870]})
    checks_def.append({"type": "ability", "id": "A1HH", "field": "ubertip1", "expected": wts_updates[35073]})

    # A1HI: Морозный доспех (cD08, hotkey Q, 1 lvl)
    wts_updates[34871] = "|cffe4cfa3Морозный доспех|r"
    wts_updates[34872] = "|cffe4cfa3Морозный доспех|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "A1HI", "field": "name", "expected": wts_updates[34871]})
    checks_def.append({"type": "ability", "id": "A1HI", "field": "tip1", "expected": wts_updates[34872]})

    # A1HM: Пожирание магии (cD08, hotkey W, 1 lvl)
    wts_updates[35092] = "|cffe4cfa3Пожирание магии|r"
    wts_updates[35093] = "|cffe4cfa3Пожирание магии|r (|cffffffffW|r)"
    wts_updates[35094] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает положительные и отрицательные заклинания с войск в указанной области. Восстанавливает заклинателю здоровье и ману за каждую цель, а также наносит урон призванным созданиям.|r"
    checks_def.append({"type": "ability", "id": "A1HM", "field": "name", "expected": wts_updates[35092]})
    checks_def.append({"type": "ability", "id": "A1HM", "field": "tip1", "expected": wts_updates[35093]})
    checks_def.append({"type": "ability", "id": "A1HM", "field": "ubertip1", "expected": wts_updates[35094]})

    # A1HN: Лик смерти (cD03, hotkey E, 1 lvl)
    wts_updates[35012] = "|cffe4cfa3Лик смерти|r"
    wts_updates[35074] = "|cffe4cfa3Лик смерти|r (|cffffffffE|r)"
    wts_updates[35076] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087160|cffced4da ед. здоровья союзнику-нежити или наносит |cffffffff80|cffced4da ед. урона живому противнику.|r"
    checks_def.append({"type": "ability", "id": "A1HN", "field": "name", "expected": wts_updates[35012]})
    checks_def.append({"type": "ability", "id": "A1HN", "field": "tip1", "expected": wts_updates[35074]})
    checks_def.append({"type": "ability", "id": "A1HN", "field": "ubertip1", "expected": wts_updates[35076]})

    # A1HO: Заразительная атака (cD11, 1 lvl, passive)
    wts_updates[36961] = "|cffe4cfa3Заразительная атака|r"
    wts_updates[36959] = "|cffe4cfa3Заразительная атака|r"
    wts_updates[36960] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff33%|cffced4da каждая атака бойца заражает цель смертоносной чумой, наносящей периодический урон.|r"
    checks_def.append({"type": "ability", "id": "A1HO", "field": "name", "expected": wts_updates[36961]})
    checks_def.append({"type": "ability", "id": "A1HO", "field": "tip1", "expected": wts_updates[36959]})
    checks_def.append({"type": "ability", "id": "A1HO", "field": "ubertip1", "expected": wts_updates[36960]})

    # A1IJ: Служебный маркер строения (1 lvl)
    wts_updates[35961] = "|cffa6afb8Служебный маркер|r"
    wts_updates[11590] = "|cffa6afb8Служебный маркер|r"
    wts_updates[11606] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер строения вне экономики.|r"
    checks_def.append({"type": "ability", "id": "A1IJ", "field": "name", "expected": wts_updates[35961]})
    checks_def.append({"type": "ability", "id": "A1IJ", "field": "tip1", "expected": wts_updates[11590]})
    checks_def.append({"type": "ability", "id": "A1IJ", "field": "ubertip1", "expected": wts_updates[11606]})

    # A1IK: Зачумнение (cD05, hotkey Q, 1 lvl)
    wts_updates[34365] = "|cffe4cfa3Зачумление|r"
    wts_updates[34366] = "|cffe4cfa3Зачумление|r (|cffffffffQ|r)"
    wts_updates[12071] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заражает врага паразитом, наносящим непрерывный периодический урон. "
        "Если цель погибает под действием заклятия, из её тела появляется прислужник нежити. "
        "Успешное применение восстанавливает заклинателю |cffc8e08715|cffced4da здоровья и |cffc8e0875|cffced4da маны.|r"
    )
    checks_def.append({"type": "ability", "id": "A1IK", "field": "name", "expected": wts_updates[34365]})
    checks_def.append({"type": "ability", "id": "A1IK", "field": "tip1", "expected": wts_updates[34366]})
    checks_def.append({"type": "ability", "id": "A1IK", "field": "ubertip1", "expected": wts_updates[12071]})

    # A1IL: Воскрешение мертвых (Hero ability of CD02, 4 lvls, hotkey Q)
    wts_updates[35974] = "|cffe4cfa3Воскрешение мёртвых|r"
    wts_updates[35989] = "|cffe4cfa3Воскрешение мёртвых|r (|cffffffffQ|r)"
    wts_updates[35990] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает из трупа могучего бойца нежити на службу культу.|n|n"
        "|cffa6afb8Уровень 1:|r Скелет-воин.|n"
        "|cffa6afb8Уровень 2:|r Вурдалак.|n"
        "|cffa6afb8Уровень 3:|r Поганище.|n"
        "|cffa6afb8Уровень 4:|r Рыцарь смерти.|r"
    )
    a1il_tips = [35975, 35976, 35977, 35978]
    a1il_ubs = [35979, 35980, 35981, 35982]
    a1il_units = [
        "|cffa9c7deСкелета-воина|cffced4da",
        "свирепого |cffa9c7deВурдалака|cffced4da",
        "массивное |cffa9c7deПоганище|cffced4da",
        "элитного |cffa9c7deРыцаря смерти|cffced4da"
    ]
    for lvl in range(1, 5):
        wts_updates[a1il_tips[lvl-1]] = f"|cffe4cfa3Воскрешение мёртвых — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a1il_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает из выбранного трупа {a1il_units[lvl-1]} на службу герою.|r"
        )
        checks_def.append({"type": "ability", "id": "A1IL", "field": f"tip{lvl}", "expected": wts_updates[a1il_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A1IL", "field": f"ubertip{lvl}", "expected": wts_updates[a1il_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A1IL", "field": "name", "expected": wts_updates[35974]})
    checks_def.append({"type": "ability", "id": "A1IL", "field": "researchtip", "expected": wts_updates[35989]})
    checks_def.append({"type": "ability", "id": "A1IL", "field": "researchubertip", "expected": wts_updates[35990]})

    # A1KB: Защита столицы (1 lvl)
    wts_updates[38201] = "|cffe4cfa3Защита столицы|r"
    wts_updates[38229] = "|cffe4cfa3Защита столицы|r"
    checks_def.append({"type": "ability", "id": "A1KB", "field": "name", "expected": wts_updates[38201]})
    checks_def.append({"type": "ability", "id": "A1KB", "field": "tip1", "expected": wts_updates[38229]})

    # A1L9: Воскрешать бойцов / Воскрешать слуг (cD31, hotkey C, 2 lvls)
    wts_updates[38662] = "|cffe4cfa3Призыв на кладбище|r"
    wts_updates[38679] = "|cffe4cfa3Воскрешать бойцов|r (|cffffffffC|r)"
    wts_updates[38698] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переключает кладбище на автоматическое воскрешение |cffa9c7deСкелетов-воинов|cffced4da вместо слуг-лесорубов.|r"
    wts_updates[38756] = "|cffe4cfa3Воскрешать слуг|r (|cffffffffC|r)"
    wts_updates[38757] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переключает кладбище на автоматическое воскрешение слуг-лесорубов для добычи древесины.|r"
    checks_def.append({"type": "ability", "id": "A1L9", "field": "name", "expected": wts_updates[38662]})
    checks_def.append({"type": "ability", "id": "A1L9", "field": "tip1", "expected": wts_updates[38679]})
    checks_def.append({"type": "ability", "id": "A1L9", "field": "ubertip1", "expected": wts_updates[38698]})
    checks_def.append({"type": "ability", "id": "A1L9", "field": "tip2", "expected": wts_updates[38756]})
    checks_def.append({"type": "ability", "id": "A1L9", "field": "ubertip2", "expected": wts_updates[38757]})

    # AUdr: Темный ритуал (U02X, hotkey E, 4 lvls)
    wts_updates[29627] = "|cffe4cfa3Тёмный ритуал — уровень 4|r (|cffffffffE|r)"
    wts_updates[29628] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приносит в жертву союзную нежить, восстанавливая личу ману в размере |cffffffff100%|cffced4da от запаса здоровья принесённого юнита.|r"
    checks_def.append({"type": "ability", "id": "AUdr", "field": "tip4", "expected": wts_updates[29627]})
    checks_def.append({"type": "ability", "id": "AUdr", "field": "ubertip4", "expected": wts_updates[29628]})

    # AUfn: Кольцо льда (U02X, hotkey Q, 4 lvls)
    wts_updates[30532] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает врагов вокруг цели волной мороза, нанося урон и замедляя их передвижение и атаку.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff100|cffced4da ед. урона цели, |cffffffff50|cffced4da по площади.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff150|cffced4da ед. урона цели, |cffffffff100|cffced4da по площади.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff275|cffced4da ед. урона цели, |cffffffff150|cffced4da по площади.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff450|cffced4da ед. урона цели, |cffffffff200|cffced4da по площади.|r"
    )
    wts_updates[2513] = "|cffe4cfa3Кольцо льда — уровень 4|r (|cffffffffQ|r)"
    wts_updates[21411] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает ледяную волну, нанося |cffffffff450|cffced4da ед. урона цели и |cffffffff200|cffced4da ед. урона врагам поблизости, замедляя их передвижение и скорость атаки на |cffffffff8|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "AUfn", "field": "researchubertip", "expected": wts_updates[30532]})
    checks_def.append({"type": "ability", "id": "AUfn", "field": "tip4", "expected": wts_updates[2513]})
    checks_def.append({"type": "ability", "id": "AUfn", "field": "ubertip4", "expected": wts_updates[21411]})

    # cDA1: Болезнетворное облако (cD13, 1 lvl, passive)
    wts_updates[30317] = "|cffe4cfa3Болезнетворное облако|r"
    wts_updates[35212] = "|cffe4cfa3Болезнетворное облако|r"
    checks_def.append({"type": "ability", "id": "cDA1", "field": "name", "expected": wts_updates[30317]})
    checks_def.append({"type": "ability", "id": "cDA1", "field": "tip1", "expected": wts_updates[35212]})

    # cDAZ: Автокаст воскрешения (cD29, hotkey A, 2 lvls)
    wts_updates[38637] = "|cffe4cfa3Автоматическое воскрешение|r"
    wts_updates[38638] = "|cffe4cfa3Отключить автоприменение воскрешения|r (|cffffffffA|r)"
    wts_updates[38660] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Новые некроманты, обученные в этом здании, будут появляться с выключенным автоприменением «Воскрешения мёртвых».|r"
    wts_updates[38640] = "|cffe4cfa3Включить автоприменение воскрешения|r (|cffffffffA|r)"
    wts_updates[38661] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Новые некроманты, обученные в этом здании, будут появляться со включённым автоприменением «Воскрешения мёртвых».|r"
    checks_def.append({"type": "ability", "id": "cDAZ", "field": "name", "expected": wts_updates[38637]})
    checks_def.append({"type": "ability", "id": "cDAZ", "field": "tip1", "expected": wts_updates[38638]})
    checks_def.append({"type": "ability", "id": "cDAZ", "field": "ubertip1", "expected": wts_updates[38660]})
    checks_def.append({"type": "ability", "id": "cDAZ", "field": "tip2", "expected": wts_updates[38640]})
    checks_def.append({"type": "ability", "id": "cDAZ", "field": "ubertip2", "expected": wts_updates[38661]})

    # cDa2: Воскрешение мертвых (cD03, hotkey Q, 3 lvls)
    wts_updates[35206] = "|cffe4cfa3Воскрешение мёртвых|r"
    wts_updates[26988] = "|cffe4cfa3Воскрешение мёртвых — уровень 1|r (|cffffffffQ|r)"
    wts_updates[12004] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает |cffffffff1|cffced4da скелета из трупа. При успешном поднятии восстанавливает заклинателю |cffc8e08715|cffced4da здоровья и |cffc8e0875|cffced4da маны.|r"
    wts_updates[35205] = "|cffe4cfa3Воскрешение мёртвых — уровень 2|r (|cffffffffQ|r)"
    wts_updates[12009] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает |cffffffff1|cffced4da скелета-воина 2-го уровня из трупа. При успешном поднятии восстанавливает заклинателю |cffc8e08715|cffced4da здоровья и |cffc8e0875|cffced4da маны.|r"
    wts_updates[36912] = "|cffe4cfa3Воскрешение мёртвых — уровень 3|r (|cffffffffQ|r)"
    wts_updates[12011] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает |cffffffff1|cffced4da скелета-воина 3-го уровня из трупа. При успешном поднятии восстанавливает заклинателю |cffc8e08715|cffced4da здоровья и |cffc8e0875|cffced4da маны.|r"
    checks_def.append({"type": "ability", "id": "cDa2", "field": "name", "expected": wts_updates[35206]})
    checks_def.append({"type": "ability", "id": "cDa2", "field": "tip1", "expected": wts_updates[26988]})
    checks_def.append({"type": "ability", "id": "cDa2", "field": "ubertip1", "expected": wts_updates[12004]})
    checks_def.append({"type": "ability", "id": "cDa2", "field": "tip2", "expected": wts_updates[35205]})
    checks_def.append({"type": "ability", "id": "cDa2", "field": "ubertip2", "expected": wts_updates[12009]})
    checks_def.append({"type": "ability", "id": "cDa2", "field": "tip3", "expected": wts_updates[36912]})
    checks_def.append({"type": "ability", "id": "cDa2", "field": "ubertip3", "expected": wts_updates[12011]})

    # cDa4: Воскрешение слуг (cD31, hotkey Z, 1 lvl)
    wts_updates[35071] = "|cffe4cfa3Воскрешение слуг|r"
    wts_updates[27222] = "|cffe4cfa3Воскрешение слуг|r (|cffffffffZ|r)"
    wts_updates[14535] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно воскрешает скелета-слугу для заготовки древесины.|r"
    checks_def.append({"type": "ability", "id": "cDa4", "field": "name", "expected": wts_updates[35071]})
    checks_def.append({"type": "ability", "id": "cDa4", "field": "tip1", "expected": wts_updates[27222]})
    checks_def.append({"type": "ability", "id": "cDa4", "field": "ubertip1", "expected": wts_updates[14535]})

    # cDa5: Плотеобработка (cD05, hotkey R, 1 lvl)
    wts_updates[27223] = "|cffe4cfa3Плотеобработка|r"
    wts_updates[35207] = "|cffe4cfa3Плотеобработка|r (|cffffffffR|r)"
    wts_updates[35971] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Собирает группу мясных созданий в одного могучего голема. "
        "Поглощает до |cffffffff12|cffced4da юнитов из плоти в области применения (максимум до |cffffffff6500|cffced4da суммарного здоровья). "
        "Эффективность слияния составляет |cffffffff50%|cffced4da и повышается на |cffc8e087+5%|cffced4da за каждый уровень «Посвящения осквернителей».|r"
    )
    checks_def.append({"type": "ability", "id": "cDa5", "field": "name", "expected": wts_updates[27223]})
    checks_def.append({"type": "ability", "id": "cDa5", "field": "tip1", "expected": wts_updates[35207]})
    checks_def.append({"type": "ability", "id": "cDa5", "field": "ubertip1", "expected": wts_updates[35971]})

    # cDa6: Дамми плоть (internal tag)
    wts_updates[27247] = "|cffa6afb8Создание из плоти|r"
    wts_updates[11016] = "|cffa6afb8Создание из плоти|r"
    checks_def.append({"type": "ability", "id": "cDa6", "field": "name", "expected": wts_updates[27247]})
    checks_def.append({"type": "ability", "id": "cDa6", "field": "tip1", "expected": wts_updates[11016]})

    # cDa8: Призрачное касание (cD12, hotkey W, 1 lvl)
    wts_updates[27250] = "|cffe4cfa3Призрачное касание|r"
    wts_updates[38651] = "|cffe4cfa3Призрачное касание|r (|cffffffffW|r)"
    wts_updates[38652] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет запас маны союзным заклинателям, находящимся поблизости от распылителя.|r"
    checks_def.append({"type": "ability", "id": "cDa8", "field": "name", "expected": wts_updates[27250]})
    checks_def.append({"type": "ability", "id": "cDa8", "field": "tip1", "expected": wts_updates[38651]})
    checks_def.append({"type": "ability", "id": "cDa8", "field": "ubertip1", "expected": wts_updates[38652]})

    # cDa9: Чумная эссенция (cD12, hotkey Q, 1 lvl)
    wts_updates[28581] = "|cffe4cfa3Чумная эссенция|r"
    wts_updates[34982] = "|cffe4cfa3Чумная эссенция|r (|cffffffffQ|r)"
    wts_updates[34983] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет по |cffc8e08715|cffced4da ед. здоровья находящимся рядом союзным бойцам нежити (до |cffffffff10|cffced4da целей).|r"
    checks_def.append({"type": "ability", "id": "cDa9", "field": "name", "expected": wts_updates[28581]})
    checks_def.append({"type": "ability", "id": "cDa9", "field": "tip1", "expected": wts_updates[34982]})
    checks_def.append({"type": "ability", "id": "cDa9", "field": "ubertip1", "expected": wts_updates[34983]})

    # cDaa: Посвящение некромантов (cD12 dummy)
    wts_updates[34218] = "|cffa6afb8Посвящение некромантов|r"
    wts_updates[34619] = "|cffa6afb8Посвящение некромантов|r"
    checks_def.append({"type": "ability", "id": "cDaa", "field": "name", "expected": wts_updates[34218]})
    checks_def.append({"type": "ability", "id": "cDaa", "field": "tip1", "expected": wts_updates[34619]})

    # cDad: Кольцо льда (cD08, hotkey R, 1 lvl)
    wts_updates[36971] = "|cffe4cfa3Кольцо льда|r"
    wts_updates[36970] = "|cffe4cfa3Кольцо льда|r (|cffffffffR|r)"
    wts_updates[12074] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну леденящего холода, наносящую |cffffffff75|cffced4da ед. урона основной цели и |cffffffff60|cffced4da ед. урона окружающим врагам, замедляя их на |cffffffff5|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "cDad", "field": "name", "expected": wts_updates[36971]})
    checks_def.append({"type": "ability", "id": "cDad", "field": "tip1", "expected": wts_updates[36970]})
    checks_def.append({"type": "ability", "id": "cDad", "field": "ubertip1", "expected": wts_updates[12074]})

    # cDae: Ледяные стрелы (cD08, hotkey E, 1 lvl)
    wts_updates[28776] = "|cffe4cfa3Ледяные стрелы|r"
    wts_updates[34992] = "|cffe4cfa3Ледяные стрелы|r (|cffffffffE|r)"
    checks_def.append({"type": "ability", "id": "cDae", "field": "name", "expected": wts_updates[28776]})
    checks_def.append({"type": "ability", "id": "cDae", "field": "tip1", "expected": wts_updates[34992]})

    # cDai: Порча издыхания (cD05, hotkey W, 1 lvl)
    wts_updates[30321] = "|cffe4cfa3Порча издыхания|r"
    wts_updates[34842] = "|cffe4cfa3Порча издыхания|r (|cffffffffW|r)"
    wts_updates[38659] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ослабляет вражеского бойца, снижая его атакуемый урон на |cffe69a8d15%|cffced4da и уменьшая показатель брони на |cffe69a8d3|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "cDai", "field": "name", "expected": wts_updates[30321]})
    checks_def.append({"type": "ability", "id": "cDai", "field": "tip1", "expected": wts_updates[34842]})
    checks_def.append({"type": "ability", "id": "cDai", "field": "ubertip1", "expected": wts_updates[38659]})

    # cDao: Неистовство чужой души (cD33, hotkey Q, 1 lvl)
    wts_updates[12145] = "|cffe4cfa3Неистовство чужой души|r"
    wts_updates[30331] = "|cffe4cfa3Неистовство чужой души|r (|cffffffffQ|r)"
    wts_updates[12146] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Временно ускоряет атаку бойца на |cffc8e087+30%|cffced4da и скорость передвижения на |cffc8e087+25%|cffced4da на |cffffffff15|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "cDao", "field": "name", "expected": wts_updates[12145]})
    checks_def.append({"type": "ability", "id": "cDao", "field": "tip1", "expected": wts_updates[30331]})
    checks_def.append({"type": "ability", "id": "cDao", "field": "ubertip1", "expected": wts_updates[12146]})

    # cDap: Порча изнывания (cD03, hotkey W, 1 lvl)
    wts_updates[696] = "|cffe4cfa3Порча изнывания|r"
    wts_updates[19994] = "|cffe4cfa3Порча изнывания|r (|cffffffffW|r)"
    wts_updates[1342] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки противника на |cffe69a8d50%|cffced4da и скорость его передвижения на |cffe69a8d50%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "cDap", "field": "name", "expected": wts_updates[696]})
    checks_def.append({"type": "ability", "id": "cDap", "field": "tip1", "expected": wts_updates[19994]})
    checks_def.append({"type": "ability", "id": "cDap", "field": "ubertip1", "expected": wts_updates[1342]})

    # cDaq: Эксгумация (cD13, passive, 2 lvls)
    wts_updates[28780] = "|cffe4cfa3Эксгумация|r"
    wts_updates[34984] = "|cffe4cfa3Эксгумация — уровень 1|r"
    wts_updates[34995] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Труповозка каждые |cffffffff30|cffced4da сек. автоматически извлекает из земли свежий труп.|r"
    wts_updates[34993] = "|cffe4cfa3Эксгумация — уровень 2|r"
    wts_updates[34994] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Труповозка каждые |cffffffff15|cffced4da сек. автоматически извлекает из земли свежий труп.|r"
    checks_def.append({"type": "ability", "id": "cDaq", "field": "name", "expected": wts_updates[28780]})
    checks_def.append({"type": "ability", "id": "cDaq", "field": "tip1", "expected": wts_updates[34984]})
    checks_def.append({"type": "ability", "id": "cDaq", "field": "ubertip1", "expected": wts_updates[34995]})
    checks_def.append({"type": "ability", "id": "cDaq", "field": "tip2", "expected": wts_updates[34993]})
    checks_def.append({"type": "ability", "id": "cDaq", "field": "ubertip2", "expected": wts_updates[34994]})

    # cDar: Костесборка (cD03, hotkey R, 1 lvl)
    wts_updates[30299] = "|cffe4cfa3Костесборка|r"
    wts_updates[35209] = "|cffe4cfa3Костесборка|r (|cffffffffR|r)"
    wts_updates[35972] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Собирает группу костяных созданий в одного могучего стража или титана. "
        "Поглощает до |cffffffff12|cffced4da скелетов в области применения (максимум до |cffffffff3500|cffced4da суммарного здоровья). "
        "Эффективность слияния составляет |cffffffff50%|cffced4da и повышается на |cffc8e087+5%|cffced4da за каждый уровень «Посвящения некромантов».|r"
    )
    checks_def.append({"type": "ability", "id": "cDar", "field": "name", "expected": wts_updates[30299]})
    checks_def.append({"type": "ability", "id": "cDar", "field": "tip1", "expected": wts_updates[35209]})
    checks_def.append({"type": "ability", "id": "cDar", "field": "ubertip1", "expected": wts_updates[35972]})

    # cDat: Дамми кости (internal tag)
    wts_updates[30301] = "|cffa6afb8Костяное создание|r"
    wts_updates[34666] = "|cffa6afb8Костяное создание|r"
    checks_def.append({"type": "ability", "id": "cDat", "field": "name", "expected": wts_updates[30301]})
    checks_def.append({"type": "ability", "id": "cDat", "field": "tip1", "expected": wts_updates[34666]})

    # cDaw: Чумная аура (cD12, passive, 1 lvl)
    wts_updates[30291] = "|cffe4cfa3Чумная аура|r"
    wts_updates[34996] = "|cffe4cfa3Чумная аура|r"
    wts_updates[35031] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно ускоряет восстановление здоровья находящейся поблизости союзной нежити.|r"
    checks_def.append({"type": "ability", "id": "cDaw", "field": "name", "expected": wts_updates[30291]})
    checks_def.append({"type": "ability", "id": "cDaw", "field": "tip1", "expected": wts_updates[34996]})
    checks_def.append({"type": "ability", "id": "cDaw", "field": "ubertip1", "expected": wts_updates[35031]})

    # cDay: Заразительные атаки (cD14, passive, 1 lvl)
    wts_updates[35211] = "|cffe4cfa3Заразительные атаки|r"
    wts_updates[30308] = "|cffe4cfa3Заразительные атаки|r"
    wts_updates[34840] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки ядоголема заражают поражённых противников чумой, наносящей периодический урон.|r"
    checks_def.append({"type": "ability", "id": "cDay", "field": "name", "expected": wts_updates[35211]})
    checks_def.append({"type": "ability", "id": "cDay", "field": "tip1", "expected": wts_updates[30308]})
    checks_def.append({"type": "ability", "id": "cDay", "field": "ubertip1", "expected": wts_updates[34840]})

    # =========================================================================
    # BUILD REGISTRY JSON ARTIFACTS
    # =========================================================================
    raw_dump = json.load(open(ROOT / "scripts/cult_raw_dump.json", encoding="utf-8"))

    # 1. cult_selection.json
    sel_data = {
        "scope": "Культ Проклятых (Cult of the Damned): подсказка выбора расы A1HA и маркеры фракции R0J4, R0J5",
        "object": "A1HA",
        "variants": ["SD"],
        "hotkey": {"value": "D"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_CultOfDamned регистрирует способность A1HA.",
            "При выборе создаются 3 рабочих cD02 (Послушник), исследуются маркеры R0J4 и R0J5, вызывается CultOn(), удаляется выбирающий юнит.",
            "Горячая клавиша D, создатель VinerX, куратор VinerX, сложность 5/5 (●●●●●), период «Warcraft III — Wrath of the Lich King»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38911, "after": wts_updates[38911]},
            {"field": "tip1", "wts_id": 38912, "after": wts_updates[38912]},
            {"field": "ubertip1", "wts_id": 22000, "after": wts_updates[22000]}
        ],
        "markers": [
            {
                "id": "R0J4",
                "name": "Культ Проклятых (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 34712, "after": wts_updates[34712]},
                    {"field": "tip1", "wts_id": 34713, "after": wts_updates[34713]},
                    {"field": "ubertip1", "wts_id": 34714, "after": wts_updates[34714]}
                ]
            },
            {
                "id": "R0J5",
                "name": "Плеть или Культ Проклятых (маркер нежити)",
                "strings": [
                    {"field": "name1", "wts_id": 34715, "after": wts_updates[34715]},
                    {"field": "tip1", "wts_id": 34716, "after": wts_updates[34716]},
                    {"field": "ubertip1", "wts_id": 34717, "after": wts_updates[34717]}
                ]
            }
        ]
    }
    (folder / "cult_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote cult_selection.json")

    # 2. cult_buildings.json
    bld_entries = []
    for b in raw_dump["buildings"]:
        bid = b["id"]
        entry = {"id": bid, "hotkey": b.get("hotkey"), "strings": []}
        for f, sid_field in [("name", "name_sid"), ("tip", "tip_sid"), ("ubertip", "ubertip_sid")]:
            sid = b.get(sid_field)
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        if entry["strings"]:
            bld_entries.append(entry)
    bld_data = {
        "scope": f"Культ Проклятых (Cult of the Damned): категория 1 — Здания ({len(raw_dump['buildings'])} зданий)",
        "buildings_count": len(raw_dump["buildings"]),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "cult_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote cult_buildings.json ({len(bld_entries)} entries)")

    # 3. cult_heroes.json
    hero_entries = []
    for h in raw_dump["heroes"]:
        hid = h["id"]
        entry = {"id": hid, "hotkey": h.get("hotkey"), "strings": []}
        for f, sid_field in [("name", "name_sid"), ("tip", "tip_sid"), ("ubertip", "ubertip_sid")]:
            sid = h.get(sid_field)
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        raw_aw = h.get("raw_awakentip", "")
        if raw_aw.startswith("TRIGSTR_") and int(raw_aw[8:]) in wts_updates:
            entry["strings"].append({"field": "awakentip", "wts_id": int(raw_aw[8:]), "after": wts_updates[int(raw_aw[8:])]})
        raw_rev = h.get("raw_revivetip", "")
        if raw_rev.startswith("TRIGSTR_") and int(raw_rev[8:]) in wts_updates:
            entry["strings"].append({"field": "revivetip", "wts_id": int(raw_rev[8:]), "after": wts_updates[int(raw_rev[8:])]})
        raw_prop = h.get("raw_propernames", "")
        if raw_prop.startswith("TRIGSTR_") and int(raw_prop[8:]) in wts_updates:
            entry["strings"].append({"field": "propernames", "wts_id": int(raw_prop[8:]), "after": wts_updates[int(raw_prop[8:])]})
        if entry["strings"]:
            hero_entries.append(entry)
    hero_data = {
        "scope": f"Культ Проклятых (Cult of the Damned): категория 2 — Герои ({len(raw_dump['heroes'])} героев)",
        "heroes_count": len(raw_dump["heroes"]),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "cult_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote cult_heroes.json ({len(hero_entries)} entries)")

    # 4. cult_units.json
    unit_entries = []
    for u in raw_dump["units"]:
        uid = u["id"]
        entry = {"id": uid, "hotkey": u.get("hotkey"), "strings": []}
        for f, sid_field in [("name", "name_sid"), ("tip", "tip_sid"), ("ubertip", "ubertip_sid")]:
            sid = u.get(sid_field)
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        if entry["strings"]:
            unit_entries.append(entry)
    unit_data = {
        "scope": f"Культ Проклятых (Cult of the Damned): категория 3 — Юниты ({len(raw_dump['units'])} юнитов)",
        "units_count": len(raw_dump["units"]),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "cult_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote cult_units.json ({len(unit_entries)} entries)")

    # 5. cult_research.json
    upg_entries = []
    for up in raw_dump["upgrades"]:
        upid = up["id"]
        entry = {"id": upid, "levels": up.get("levels", 1), "strings": []}
        for k in ["names", "tips", "ubertips"]:
            for subk, subv in up.get(k, {}).items():
                if isinstance(subv, dict) and subv.get("sid") and subv["sid"] in wts_updates:
                    entry["strings"].append({"field": f"{k}_{subk}", "wts_id": subv["sid"], "after": wts_updates[subv["sid"]]})
        if entry["strings"]:
            upg_entries.append(entry)
    upg_data = {
        "scope": f"Культ Проклятых (Cult of the Damned): категория 4 — Исследования и маркеры ({len(raw_dump['upgrades'])} технологий)",
        "upgrades_count": len(raw_dump["upgrades"]),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "cult_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote cult_research.json ({len(upg_entries)} entries)")

    # 6. cult_abilities.json
    abil_entries = []
    for ab in raw_dump["abilities"]:
        aid = ab["id"]
        entry = {"id": aid, "levels": ab.get("levels", 1), "strings": []}
        for f, sid_field in [("name", "name_sid"), ("researchtip", "researchtip_sid"), ("researchubertip", "researchubertip_sid"), ("untip", "untip_sid"), ("unubertip", "unubertip_sid")]:
            sid = ab.get(sid_field)
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        for k in ["tips", "ubertips"]:
            for subk, subv in ab.get(k, {}).items():
                if isinstance(subv, dict) and subv.get("sid") and subv["sid"] in wts_updates:
                    entry["strings"].append({"field": f"{k}_{subk}", "wts_id": subv["sid"], "after": wts_updates[subv["sid"]]})
        if entry["strings"]:
            abil_entries.append(entry)
    abil_data = {
        "scope": f"Культ Проклятых (Cult of the Damned): категория 5 — Способности ({len(raw_dump['abilities'])} способностей)",
        "abilities_count": len(raw_dump["abilities"]),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "cult_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote cult_abilities.json ({len(abil_entries)} entries)")

    # 7. cult_audit.json
    audit_data = {
        "race": "Культ Проклятых (Cult of the Damned)",
        "race_id": 33,
        "selection_ability": "A1HA",
        "objects_audit": {
            "buildings": {
                "count": len(raw_dump["buildings"]),
                "ids": [b["id"] for b in raw_dump["buildings"]],
                "town_halls": {
                    "tier1": {"id": "cD26", "name": "Некрополь", "food": 50},
                    "tier2": {"id": "cD25", "name": "Чертоги мёртвых", "food": 100},
                    "tier3": {"id": "cD24", "name": "Тёмная цитадель", "food": 150}
                },
                "income_farms": {
                    "cD12": {"name": "Распылитель чумы", "income": 75, "food": 75}
                }
            },
            "units": {
                "count": len(raw_dump["units"]),
                "ids": [u["id"] for u in raw_dump["units"]]
            },
            "heroes": {
                "count": len(raw_dump["heroes"]),
                "ids": [h["id"] for h in raw_dump["heroes"]],
                "names": {
                    "CD01": "Рыцарь смерти (Сила, ближний бой)",
                    "CD02": "Верховный некромант (Интеллект, дальний бой)",
                    "U02X": "Лич (Интеллект, дальний бой)"
                }
            },
            "abilities": {
                "count": len(raw_dump["abilities"]),
                "total_wts_updated": len(wts_updates)
            },
            "researches": {
                "count": len(raw_dump["upgrades"]),
                "markers_list": {
                    "R0J4": "Маркер расы Культ Проклятых",
                    "R0J5": "Маркер расы Плеть или Культ Проклятых"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items found for Cult of the Damned."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "Standardized race selection and activation triggers."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": ["BNlm", "BHab"],
            "status": "All abilities and buffs follow unified UI color palette."
        },
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def)
    }
    (folder / "cult_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote cult_audit.json")

    # 8. cult_plan.json (Master plan)
    plan_data = {
        "race": "CultOfDamned",
        "race_name_ru": "Культ Проклятых",
        "race_id": 33,
        "selection_ability": "A1HA",
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A1HA"],
            "markers": ["R0J4", "R0J5"],
            "buildings": [b["id"] for b in raw_dump["buildings"]],
            "units": [u["id"] for u in raw_dump["units"]],
            "heroes": [h["id"] for h in raw_dump["heroes"]],
            "upgrades": [up["id"] for up in raw_dump["upgrades"]],
            "abilities": [ab["id"] for ab in raw_dump["abilities"]]
        }
    }
    (folder / "cult_plan.json").write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to cult_plan.json ({len(wts_updates)} string updates, {len(checks_def)} checks)")

if __name__ == "__main__":
    main()
