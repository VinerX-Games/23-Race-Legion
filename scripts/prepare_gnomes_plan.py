# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Gnomes race (Race 23).

Generates:
- docs/ui_text/gnomes_plan.json
- docs/ui_text/gnomes_selection.json
- docs/ui_text/gnomes_buildings.json
- docs/ui_text/gnomes_units.json
- docs/ui_text/gnomes_heroes.json
- docs/ui_text/gnomes_abilities.json
- docs/ui_text/gnomes_research.json
- docs/ui_text/gnomes_audit.json
"""
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
    # 1. RACE SELECTION & MARKERS: A0SD, R0BX, R0HW
    # =========================================================================
    # A0SD
    wts_updates[38895] = "|cffe4cfa3Гномы|r"
    wts_updates[38896] = "|cffe4cfa3Гномы|r (|cffffffffQ|r)"
    wts_updates[35199] = (
        "|cffa6afb8РАСА:|cffced4da Гениальные инженеры и изобретатели Азерота, опирающиеся на боевые машины, шагоходы и передовые технологии.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●●|cffa6afb8○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«World of Warcraft: Classic — Battle for Azeroth»|r|n|n"
        "|cffced4daУмные, дерзкие и чудаковатые гномы — одна из самых удивительных цивилизаций Азерота. "
        "Пережив катастрофу в Гномрегане и потерю родного дома, неугомонные изобретатели обратили всю мощь своего гения "
        "на военное дело: паровые танки, роботизированные экзоскелеты, скорострельные шагоходы и колоссальную артиллерию.|r"
    )
    checks_def.append({"type": "ability", "id": "A0SD", "field": "name", "expected": wts_updates[38895]})
    checks_def.append({"type": "ability", "id": "A0SD", "field": "tip1", "expected": wts_updates[38896]})
    checks_def.append({"type": "ability", "id": "A0SD", "field": "ubertip1", "expected": wts_updates[35199]})

    # Marker R0BX
    wts_updates[9241] = "|cffe4cfa3Гномы|r"
    wts_updates[9242] = "|cffe4cfa3Гномы|r"
    wts_updates[20125] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Гномам (Гномреган).|r"
    checks_def.append({"type": "upgrade", "id": "R0BX", "field": "name1", "expected": wts_updates[9241]})
    checks_def.append({"type": "upgrade", "id": "R0BX", "field": "tip1", "expected": wts_updates[9242]})
    checks_def.append({"type": "upgrade", "id": "R0BX", "field": "ubertip1", "expected": wts_updates[20125]})

    # Marker R0HW
    wts_updates[30254] = "|cffe4cfa3Гномы|r"
    wts_updates[29941] = "|cffe4cfa3Гномы|r"
    checks_def.append({"type": "upgrade", "id": "R0HW", "field": "name1", "expected": wts_updates[30254]})
    checks_def.append({"type": "upgrade", "id": "R0HW", "field": "tip1", "expected": wts_updates[29941]})

    # =========================================================================
    # 2. BUILDINGS (10)
    # =========================================================================
    # h0FI: Энергобашня (активна) (Z)
    wts_updates[20141] = "|cffe4cfa3Энергобашня (активна)|r"
    wts_updates[20139] = "|cffe4cfa3Энергобашня (активна)|r (|cffffffffZ|r)"
    wts_updates[31820] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Энергетическое оборонительное сооружение гномов. Обеспечивает доход и ведёт огонь по врагам.|n|n"
        "|cffa6afb8Особенности:|cffced4da боевой режим активирован сразу.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FI", "field": "name", "expected": wts_updates[20141]})
    checks_def.append({"type": "unit", "id": "h0FI", "field": "tip", "expected": wts_updates[20139]})
    checks_def.append({"type": "unit", "id": "h0FI", "field": "ubertip", "expected": wts_updates[31820]})

    # h0FK: Главный цех (Q)
    wts_updates[17459] = "|cffe4cfa3Главный цех|r"
    wts_updates[17460] = "|cffe4cfa3Главный цех|r (|cffffffffQ|r)"
    wts_updates[8105] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание гномов первой ступени. Обеспечивает добычу ресурсов и обучает рабочих.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deИнженер|cffced4da: рабочий строитель и ремонтник.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deВооружение|cffced4da|n- |cffa9c7deПрочные детали|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deГлавный цех, V2|cffced4da: открывает доступ к передовым сооружениям и технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FK", "field": "name", "expected": wts_updates[17459]})
    checks_def.append({"type": "unit", "id": "h0FK", "field": "tip", "expected": wts_updates[17460]})
    checks_def.append({"type": "unit", "id": "h0FK", "field": "ubertip", "expected": wts_updates[8105]})

    # h0FL: Энергобашня (A)
    wts_updates[2750] = "|cffe4cfa3Энергобашня|r"
    wts_updates[2757] = "|cffe4cfa3Энергобашня|r (|cffffffffA|r)"
    wts_updates[2764] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Энергетическое сооружение гномов, обеспечивающее запас пищи и доход.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСменить режим|cffced4da: переходит в активный боевой режим для обороны базы.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FL", "field": "name", "expected": wts_updates[2750]})
    checks_def.append({"type": "unit", "id": "h0FL", "field": "tip", "expected": wts_updates[2757]})
    checks_def.append({"type": "unit", "id": "h0FL", "field": "ubertip", "expected": wts_updates[2764]})

    # h0FR: Главный цех, V2 (Z)
    wts_updates[17461] = "|cffe4cfa3Главный цех, V2|r"
    wts_updates[17462] = "|cffe4cfa3Главный цех, V2|r (|cffffffffZ|r)"
    wts_updates[8114] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание гномов второй ступени. Существенно увеличивает запас пищи и открывает новые постройки.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deИнженер|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deВооружение|cffced4da|n- |cffa9c7deПрочные детали|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deГлавный цех, V3|cffced4da: открывает высшие военные проекты гномов.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FR", "field": "name", "expected": wts_updates[17461]})
    checks_def.append({"type": "unit", "id": "h0FR", "field": "tip", "expected": wts_updates[17462]})
    checks_def.append({"type": "unit", "id": "h0FR", "field": "ubertip", "expected": wts_updates[8114]})

    # h0FS: Главный цех, V3 (Z)
    wts_updates[17463] = "|cffe4cfa3Главный цех, V3|r"
    wts_updates[17464] = "|cffe4cfa3Главный цех, V3|r (|cffffffffZ|r)"
    wts_updates[8127] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание гномов третьей ступени. Обеспечивает максимальный запас пищи.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deИнженер|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deВооружение|cffced4da|n- |cffa9c7deПрочные детали|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FS", "field": "name", "expected": wts_updates[17463]})
    checks_def.append({"type": "unit", "id": "h0FS", "field": "tip", "expected": wts_updates[17464]})
    checks_def.append({"type": "unit", "id": "h0FS", "field": "ubertip", "expected": wts_updates[8127]})

    # h0FY: Фабрика (F)
    wts_updates[5673] = "|cffe4cfa3Фабрика|r"
    wts_updates[5674] = "|cffe4cfa3Фабрика|r (|cffffffffF|r)"
    wts_updates[18623] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Предприятие по производству боевых роботов, шагоходов и специализированных машин гномов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРеженоги|cffced4da: быстрый сферический робот-мясорубка.|n"
        "- |cffa9c7deМеханобоец|cffced4da: экзоскелет ближнего боя с молотами.|n"
        "- |cffa9c7deКлап Клап (v0.58889)|cffced4da: экспериментальный робот-рубщик.|n"
        "- |cffa9c7deКлап Клап (v1.0 Opt)|cffced4da: облегчённый дешёвый рабочий робот.|n"
        "- |cffa9c7deКлап Клап (v1.0 Big)|cffced4da: тяжёлый взрывной робот.|n"
        "- |cffa9c7deШагоход|cffced4da: скоростной пулемётный шагоход.|n"
        "- |cffa9c7deНаногном|cffced4da: электрический спецбоец.|n"
        "- |cffa9c7deМехагигант|cffced4da: тяжёлый боевой колосс.|n"
        "- |cffa9c7deМеханопаук|cffced4da: ракетный многоногий паук.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенное управление|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FY", "field": "name", "expected": wts_updates[5673]})
    checks_def.append({"type": "unit", "id": "h0FY", "field": "tip", "expected": wts_updates[5674]})
    checks_def.append({"type": "unit", "id": "h0FY", "field": "ubertip", "expected": wts_updates[18623]})

    # h0FZ: Энергоядро (E)
    wts_updates[17476] = "|cffe4cfa3Энергоядро|r"
    wts_updates[17477] = "|cffe4cfa3Энергоядро|r (|cffffffffE|r)"
    wts_updates[18234] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главный научно-технический центр гномов. Открывает инновационные инженерные проекты, новые боевые машины и модификации вооружения.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FZ", "field": "name", "expected": wts_updates[17476]})
    checks_def.append({"type": "unit", "id": "h0FZ", "field": "tip", "expected": wts_updates[17477]})
    checks_def.append({"type": "unit", "id": "h0FZ", "field": "ubertip", "expected": wts_updates[18234]})

    # h0G0: Мастерская (D)
    wts_updates[8083] = "|cffe4cfa3Мастерская|r"
    wts_updates[8084] = "|cffe4cfa3Мастерская|r (|cffffffffD|r)"
    wts_updates[18624] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Завод по производству бронемашин, танков и артиллерии гномов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБронемашина|cffced4da: бронетранспортёр поддержки с аурой логистики.|n"
        "- |cffa9c7deМинитанк|cffced4da: маневренный танк с артвыстрелом.|n"
        "- |cffa9c7deЭкспериментальный ГГТ|cffced4da: многоцелевая модульная платформа.|n"
        "- |cffa9c7deСамоходная артиллерия|cffced4da: дальнобойное осадное орудие.|n"
        "- |cffa9c7deУниверсальный танк|cffced4da: тяжёлый танк с пулемётами и огнемётом.|n"
        "- |cffa9c7deТанк «Венец»|cffced4da: сверхтяжёлый флагманский танк.|n"
        "- |cffa9c7deМега-Артиллерия|cffced4da: осадное суперорудие.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенные компоненты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0G0", "field": "name", "expected": wts_updates[8083]})
    checks_def.append({"type": "unit", "id": "h0G0", "field": "tip", "expected": wts_updates[8084]})
    checks_def.append({"type": "unit", "id": "h0G0", "field": "ubertip", "expected": wts_updates[18624]})

    # h0G3: Мехаказармы (W)
    wts_updates[8089] = "|cffe4cfa3Мехаказармы|r"
    wts_updates[8118] = "|cffe4cfa3Мехаказармы|r (|cffffffffW|r)"
    wts_updates[8121] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает пехоту, стрелков и заклинателей гномов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deГном-пехотинец|cffced4da: боец ближнего боя с оглушающим ударом.|n"
        "- |cffa9c7deСтрелок|cffced4da: стрелок с длинноствольным мушкетом.|n"
        "- |cffa9c7deШпион|cffced4da: невидимый диверсант с отравленным кинжалом.|n"
        "- |cffa9c7deПодрывник|cffced4da: стрелок с зажигательными гранатами.|n"
        "- |cffa9c7deГном-маг|cffced4da: заклинатель поддержки с ледяной бронёй и бурей.|n"
        "- |cffa9c7deГном-чернокнижник|cffced4da: тёмный маг с проклятиями и увечьем.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенная тренировка пехоты|cffced4da|n- |cffa9c7deУсиленная броня|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0G3", "field": "name", "expected": wts_updates[8089]})
    checks_def.append({"type": "unit", "id": "h0G3", "field": "tip", "expected": wts_updates[8118]})
    checks_def.append({"type": "unit", "id": "h0G3", "field": "ubertip", "expected": wts_updates[8121]})

    # h0G7: Алтарь Великих Умов (S)
    wts_updates[18238] = "|cffe4cfa3Алтарь Великих Умов|r"
    wts_updates[18239] = "|cffe4cfa3Алтарь Великих Умов|r (|cffffffffS|r)"
    wts_updates[19759] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священное сооружение гномской науки для призыва и воскрешения павших героев.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deТанк УТ v1.23|cffced4da: боевая машина огневой поддержки.|n"
        "- |cffa9c7deФронтовой Гений|cffced4da: изобретатель в экзоскелете ближнего боя.|n"
        "- |cffa9c7deСтрелок-ветеран|cffced4da: дальнобойный снайпер с ракетным комплексом.|r"
    )
    checks_def.append({"type": "unit", "id": "h0G7", "field": "name", "expected": wts_updates[18238]})
    checks_def.append({"type": "unit", "id": "h0G7", "field": "tip", "expected": wts_updates[18239]})
    checks_def.append({"type": "unit", "id": "h0G7", "field": "ubertip", "expected": wts_updates[19759]})

    # =========================================================================
    # 3. WORKERS (2)
    # =========================================================================
    # h0FA: Инженер (Q)
    wts_updates[20084] = "|cffe4cfa3Инженер|r"
    wts_updates[20087] = "|cffe4cfa3Инженер|r (|cffffffffQ|r)"
    wts_updates[839] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий гномов. Добывает золото и древесину, возводит сооружения и ремонтирует боевую технику.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРемонтировать|cffced4da: восстанавливает прочность зданий и механизмов.|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на небольшое расстояние.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FA", "field": "name", "expected": wts_updates[20084]})
    checks_def.append({"type": "unit", "id": "h0FA", "field": "tip", "expected": wts_updates[20087]})
    checks_def.append({"type": "unit", "id": "h0FA", "field": "ubertip", "expected": wts_updates[839]})

    # h0FX: Клап Клап (v0.58889) (Q)
    wts_updates[18136] = "|cffe4cfa3Клап Клап (v0.58889)|r"
    wts_updates[18592] = "|cffe4cfa3Клап Клап (v0.58889)|r (|cffffffffQ|r)"
    wts_updates[42329] = (
        "|cffa6afb8ЮНИТ:|cffced4da Экспериментальный робот-помощник ранней модели. Способен рубить лес и взрываться при уничтожении.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДобывать ресурсы|cffced4da: рубит древесину.|n"
        "- |cffa9c7deБа-бах!|cffced4da: взрывается при гибели, нанося урон по области.|r"
    )
    checks_def.append({"type": "unit", "id": "h0FX", "field": "name", "expected": wts_updates[18136]})
    checks_def.append({"type": "unit", "id": "h0FX", "field": "tip", "expected": wts_updates[18592]})
    checks_def.append({"type": "unit", "id": "h0FX", "field": "ubertip", "expected": wts_updates[42329]})

    # =========================================================================
    # 4. UNITS (21)
    # =========================================================================
    # h0FB: Стрелок (W)
    wts_updates[17474] = "|cffe4cfa3Стрелок|r"
    wts_updates[17475] = "|cffe4cfa3Стрелок|r (|cffffffffW|r)"
    wts_updates[31816] = (
        "|cffa6afb8ЮНИТ:|cffced4da Меткий стрелок армии гномов, вооружённый длинноствольным мушкетом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМеткий выстрел|cffced4da: шанс нанести критический урон.|n"
        "- |cffa9c7deФазовый спаситель|cffced4da: кратковременный уход от урона при ранении.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FC: Гном-пехотинец (Q)
    wts_updates[11598] = "|cffe4cfa3Гном-пехотинец|r"
    wts_updates[11599] = "|cffe4cfa3Гном-пехотинец|r (|cffffffffQ|r)"
    wts_updates[42317] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый боец ближнего боя армии гномов, оснащённый щитом и топором.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСильный удар|cffced4da: шанс оглушить противника и нанести дополнительный урон.|n"
        "- |cffa9c7deФазовый спаситель|cffced4da: кратковременная защита от урона.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )

    # h0FD: Шпион (R)
    wts_updates[776] = "|cffe4cfa3Шпион|r"
    wts_updates[4474] = "|cffe4cfa3Шпион|r (|cffffffffR|r)"
    wts_updates[42318] = (
        "|cffa6afb8ЮНИТ:|cffced4da Разведчик и диверсант гномов, обученный скрытному перемещению и ликвидации целей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСкрыться|cffced4da: переход в невидимость.|n"
        "- |cffa9c7deОтравленный кинжал|cffced4da: поражает врага замедляющим ядом.|n"
        "- |cffa9c7deОтточенные навыки|cffced4da: уклонение от атак и критические удары.|n"
        "- |cffa9c7deФазовый спаситель|cffced4da.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )

    # h0FE: Подрывник (E)
    wts_updates[13559] = "|cffe4cfa3Подрывник|r"
    wts_updates[13561] = "|cffe4cfa3Подрывник|r (|cffffffffE|r)"
    wts_updates[42319] = (
        "|cffa6afb8ЮНИТ:|cffced4da Осадный стрелок гномов, метающий зажигательные гранаты по скоплениям врага.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗажигательная граната|cffced4da: создаёт область бушующего пламени с периодическим уроном.|n"
        "- |cffa9c7deФазовый спаситель|cffced4da.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FF: Универсальный танк (R)
    wts_updates[4480] = "|cffe4cfa3Универсальный танк|r"
    wts_updates[8122] = "|cffe4cfa3Универсальный танк|r (|cffffffffR|r)"
    wts_updates[9731] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлая многоцелевая боевая машина гномов с пушечным и огнемётным вооружением.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСгусток огня|cffced4da: обжигает противников струёй пламени.|n"
        "- |cffa9c7deПрицельная пальба из пулемётов|cffced4da: непрерывный огонь по выбранной цели.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FG: Танк «Венец» (S)
    wts_updates[11615] = "|cffe4cfa3Танк «Венец»|r"
    wts_updates[4630] = "|cffe4cfa3Танк «Венец»|r (|cffffffffS|r)"
    wts_updates[42320] = (
        "|cffa6afb8ЮНИТ:|cffced4da Сверхтяжёлый бронированный колосс гномов, флагман сухопутной армии.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДвойной выстрел|cffced4da: повторный выстрел главного калибра.|n"
        "- |cffa9c7deПереключить режим|cffced4da: смена типа орудий.|n"
        "- |cffa9c7deЗалп ракет|cffced4da: обстрел площади ракетами с оглушением.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FH: Шагоход (S)
    wts_updates[9886] = "|cffe4cfa3Шагоход|r"
    wts_updates[11609] = "|cffe4cfa3Шагоход|r (|cffffffffS|r)"
    wts_updates[13861] = (
        "|cffa6afb8ЮНИТ:|cffced4da Скоростная двуногая боевая машина с автоматическим орудием.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРазрывные снаряды|cffced4da: повышенный урон по лёгкой броне.|n"
        "- |cffa9c7deБронебойные снаряды|cffced4da: повышенный урон по тяжёлой броне.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FJ: Самоходная артиллерия (A)
    wts_updates[8119] = "|cffe4cfa3Самоходная артиллерия|r"
    wts_updates[12262] = "|cffe4cfa3Самоходная артиллерия|r (|cffffffffA|r)"
    wts_updates[42321] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мобильное дальнобойное осадное орудие, сокрушающее вражеские укрепления на огромной дистанции.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FM: Гном-чернокнижник (S)
    wts_updates[17465] = "|cffe4cfa3Гном-чернокнижник|r"
    wts_updates[17466] = "|cffe4cfa3Гном-чернокнижник|r (|cffffffffS|r)"
    wts_updates[42322] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг тёмных искусств гномов, ослабляющий противников проклятиями и разрушительными чарами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПроклятие|cffced4da: накладывает промах при атаке.|n"
        "- |cffa9c7deУвечье|cffced4da: замедляет бег, атаку и снижает урон цели.|n"
        "- |cffa9c7deВолшебный огонь|cffced4da: снижает броню и открывает видимость.|n"
        "- |cffa9c7deФазовый спаситель|cffced4da.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FN: Минитанк (W)
    wts_updates[13563] = "|cffe4cfa3Минитанк|r"
    wts_updates[13565] = "|cffe4cfa3Минитанк|r (|cffffffffW|r)"
    wts_updates[42323] = (
        "|cffa6afb8ЮНИТ:|cffced4da Компактный маневренный танк поддержки с артиллерийской пушкой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАртвыстрел|cffced4da: мощный залп по выбранной области.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FO: Экспериментальный ГГТ (E)
    wts_updates[12328] = "|cffe4cfa3Экспериментальный ГГТ|r"
    wts_updates[13240] = "|cffe4cfa3Экспериментальный ГГТ|r (|cffffffffE|r)"
    wts_updates[22324] = (
        "|cffa6afb8ЮНИТ:|cffced4da Гениальное Гномье Творение — модульная боевая машина с широкими возможностями модификации.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПроизвести реженоги|cffced4da: временная сборка боевых роботов.|n"
        "- |cffa9c7deЗакопать мину|cffced4da: устанавливает скрытую мину в указанной точке.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FP: Реженоги (W)
    wts_updates[17443] = "|cffe4cfa3Реженоги|r"
    wts_updates[1383] = "|cffe4cfa3Реженоги|r (|cffffffffW|r)"
    wts_updates[42324] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый сферический робот-мясорубка с вращающимися лезвиями.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРезня|cffced4da: круговые удары лезвиями по нескольким целям одновременно.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FQ: Бронемашина (Q)
    wts_updates[4555] = "|cffe4cfa3Бронемашина|r"
    wts_updates[5279] = "|cffe4cfa3Бронемашина|r (|cffffffffQ|r)"
    wts_updates[42325] = (
        "|cffa6afb8ЮНИТ:|cffced4da Бронированный транспорт для перевозки пехоты, оснащённый пулемётом и системой логистики.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВзять на борт|cffced4da / |cffa9c7deВыгрузить|cffced4da: транспортировка десанта.|n"
        "- |cffa9c7deХорошая логистика|cffced4da: аура ускорения атаки и движения союзных машин.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FT: Мега-Артиллерия (D)
    wts_updates[17817] = "|cffe4cfa3Мега-Артиллерия|r"
    wts_updates[17818] = "|cffe4cfa3Мега-Артиллерия|r (|cffffffffD|r)"
    wts_updates[26721] = (
        "|cffa6afb8ЮНИТ:|cffced4da Колоссальное осадное орудие гномов, стреляющее на сверхдальние дистанции.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВыстрелить один снаряд|cffced4da: залп на колоссальное расстояние.|n"
        "- |cffa9c7deАннигиляция|cffced4da: сокрушительный ядерный удар по указанной зоне.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FU: Гном-маг (A)
    wts_updates[8074] = "|cffe4cfa3Гном-маг|r"
    wts_updates[8075] = "|cffe4cfa3Гном-маг|r (|cffffffffA|r)"
    wts_updates[42326] = (
        "|cffa6afb8ЮНИТ:|cffced4da Волшебник гномов, повелевающий силами тайной магии и льда.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУскорение|cffced4da: повышает скорость атаки и бега союзника.|n"
        "- |cffa9c7deМорозный доспех|cffced4da: ледяной щит, повышающий броню и замедляющий врагов.|n"
        "- |cffa9c7deСнежная буря|cffced4da: ледяной град по области.|n"
        "- |cffa9c7deФазовый спаситель|cffced4da.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FV: Механопаук (R)
    wts_updates[17468] = "|cffe4cfa3Механопаук|r"
    wts_updates[17469] = "|cffe4cfa3Механопаук|r (|cffffffffR|r)"
    wts_updates[42327] = (
        "|cffa6afb8ЮНИТ:|cffced4da Скоростной многоногий механизм с мощными клешнями и ракетным комплексом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗалп ракет|cffced4da: обстрел площади ракетами.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0FW: Мехагигант (D)
    wts_updates[17448] = "|cffe4cfa3Мехагигант|r"
    wts_updates[17449] = "|cffe4cfa3Мехагигант|r (|cffffffffD|r)"
    wts_updates[42328] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий бронированный робот-великан передовой гномской инженерии.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deШокоудары|cffced4da: мощные круговые удары с уроном по области.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0G1: Механобоец (E)
    wts_updates[930] = "|cffe4cfa3Механобоец|r"
    wts_updates[17565] = "|cffe4cfa3Механобоец|r (|cffffffffE|r)"
    wts_updates[42330] = (
        "|cffa6afb8ЮНИТ:|cffced4da Механизированный штурмовой экзоскелет с гидравлическими силовыми молотами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСильный удар|cffced4da: шанс оглушить врага и нанести повышенный урон.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )

    # h0G2: Наногном (A)
    wts_updates[13571] = "|cffe4cfa3Наногном|r"
    wts_updates[13591] = "|cffe4cfa3Наногном|r (|cffffffffA|r)"
    wts_updates[42331] = (
        "|cffa6afb8ЮНИТ:|cffced4da Высокотехнологичный боец, использующий направленную энергию электричества.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЭМИ|cffced4da: снимает заклинания и наносит урон призывам.|n"
        "- |cffa9c7deСожжение|cffced4da: сжигает ману врага при атаках.|n"
        "- |cffa9c7deЭлектрическое поле|cffced4da: окружает цель наносящим урон вихрем молний.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )

    # h0G4: Клап Клап (v1.0 Opt) (Q)
    wts_updates[18137] = "|cffe4cfa3Клап Клап (v1.0 Opt)|r"
    wts_updates[18593] = "|cffe4cfa3Клап Клап (v1.0 Opt)|r (|cffffffffQ|r)"
    wts_updates[42332] = (
        "|cffa6afb8ЮНИТ:|cffced4da Оптимизированная облегчённая версия робота «Клап Клап». Дешёвый в сборке и эффективный в работе.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДобывать ресурсы|cffced4da: рубит древесину.|n"
        "- |cffa9c7deБа-бах!|cffced4da: взрывается при уничтожении.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    # h0G5: Клап Клап (v1.0 Big) (Q)
    wts_updates[18140] = "|cffe4cfa3Клап Клап (v1.0 Big)|r"
    wts_updates[18141] = "|cffe4cfa3Клап Клап (v1.0 Big)|r (|cffffffffQ|r)"
    wts_updates[42333] = (
        "|cffa6afb8ЮНИТ:|cffced4da Укрупнённый тяжеловесный робот модели «Клап Клап» с повышенной прочностью и мощным зарядом взрывчатки.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДобывать ресурсы|cffced4da: рубит древесину.|n"
        "- |cffa9c7deБа-бах!|cffced4da: взрывается при уничтожении с повышенным уроном.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    for uid, name_sid, tip_sid, ub_sid in [
        ('h0FB', 17474, 17475, 31816), ('h0FC', 11598, 11599, 42317), ('h0FD', 776, 4474, 42318),
        ('h0FE', 13559, 13561, 42319), ('h0FF', 4480, 8122, 9731), ('h0FG', 11615, 4630, 42320),
        ('h0FH', 9886, 11609, 13861), ('h0FJ', 8119, 12262, 42321), ('h0FM', 17465, 17466, 42322),
        ('h0FN', 13563, 13565, 42323), ('h0FO', 12328, 13240, 22324), ('h0FP', 17443, 1383, 42324),
        ('h0FQ', 4555, 5279, 42325), ('h0FT', 17817, 17818, 26721), ('h0FU', 8074, 8075, 42326),
        ('h0FV', 17468, 17469, 42327), ('h0FW', 17448, 17449, 42328), ('h0G1', 930, 17565, 42330),
        ('h0G2', 13571, 13591, 42331), ('h0G4', 18137, 18593, 42332), ('h0G5', 18140, 18141, 42333)
    ]:
        checks_def.append({"type": "unit", "id": uid, "field": "name", "expected": wts_updates[name_sid]})
        checks_def.append({"type": "unit", "id": uid, "field": "tip", "expected": wts_updates[tip_sid]})
        checks_def.append({"type": "unit", "id": uid, "field": "ubertip", "expected": wts_updates[ub_sid]})

    # =========================================================================
    # 5. HEROES (8)
    # =========================================================================
    # H0GC: Танк УТ v1.23
    wts_updates[24597] = "|cffe4cfa3Танк УТ v1.23|r"
    wts_updates[19650] = "Экипаж «Улёт», Экипаж «Сила Гномрегана», Команда Мегабрякса, Команда Всюдублеска"
    wts_updates[25190] = "|cffe4cfa3Танк УТ v1.23|r"
    wts_updates[24630] = "|cffe4cfa3Танк УТ v1.23|r"
    wts_updates[25191] = "|cffe4cfa3Танк УТ v1.23|r"
    wts_updates[20027] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Элитный боевой танк гномов под управлением опытного экипажа. Специализируется на подавлении пехоты и огневой поддержке союзников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненный столб|cffced4da: обрушивает бушующее пламя на указанную область.|n"
        "- |cffa9c7deРасстрел|cffced4da: поражает веером пуль врагов в секторе перед собой.|n"
        "- |cffa9c7deКислотная бомба|cffced4da: разъедает броню цели и наносит периодический урон.|n"
        "- |cffa9c7deЭкспериментальные аккумуляторы|cffced4da: повышает интеллект героя.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )

    # H0GD / H0GE / H0GF: Фронтовой Гений
    wts_updates[25193] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[25194] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[25252] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[19664] = "Шайботайло, Стальнокрут, Шурупоклакс, Всюдунилли"
    wts_updates[19696] = "Шайботайло, Стальнокрут, Шурупоклакс, Всюдунилли"
    wts_updates[19702] = "Шайботайло, Стальнокрут, Шурупоклакс, Всюдунилли"
    wts_updates[19666] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[19665] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[19667] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[25196] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[25195] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[25249] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[19698] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[19697] = "|cffe4cfa3Фронтовой Гений|r"
    wts_updates[19699] = "|cffe4cfa3Фронтовой Гений|r"
    fg_ubertip = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Инженер-изобретатель в тяжёлом экзоскелете. Специализируется на ближнем бое, контроле поля боя и ремонте союзных машин.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРаскат грома|cffced4da: сотрясает землю, замедляя и раня врагов.|n"
        "- |cffa9c7deРазобрать бедолагу|cffced4da: уничтожает механизм, восполняя собственное здоровье.|n"
        "- |cffa9c7deРемонтная аура|cffced4da: ускоряет движение и восстановление союзных машин.|n"
        "- |cffa9c7deКод Красный|cffced4da: переход в режим предельной боевой мощности.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )
    wts_updates[20032] = fg_ubertip
    wts_updates[20033] = fg_ubertip
    wts_updates[20034] = fg_ubertip

    # H0GG: Стрелок-ветеран
    wts_updates[25253] = "|cffe4cfa3Стрелок-ветеран|r"
    wts_updates[19749] = "Дзынекрут, Брякобаск, Пародзяньс, Искроватт"
    wts_updates[25255] = "|cffe4cfa3Стрелок-ветеран|r"
    wts_updates[25254] = "|cffe4cfa3Стрелок-ветеран|r"
    wts_updates[25256] = "|cffe4cfa3Стрелок-ветеран|r"
    wts_updates[20028] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Закалённый в битвах стрелок-снайпер гномов. Наносит сокрушительный дистанционный урон и усиливает союзных стрелков.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРазрывные снаряды|cffced4da: атаки наносят дополнительный урон по площади.|n"
        "- |cffa9c7deОсколочная граната|cffced4da: поражает врагов гранатой в указанной области.|n"
        "- |cffa9c7deАура меткости|cffced4da: повышает урон дистанционных атак союзников.|n"
        "- |cffa9c7deРакетопад|cffced4da: обрушивает град ракет на вражеские войска.|n|n"
        "|cffced4daАтакует наземные цели.|r"
    )

    # H0HQ / H0HS: Король Гномрегана (Гелбин Меггакрут)
    wts_updates[21549] = "|cffe4cfa3Король Гномрегана|r"
    wts_updates[21576] = "|cffe4cfa3Король Гномрегана|r"
    wts_updates[12789] = "Гелбин Меггакрут"
    wts_updates[21577] = "Гелбин Меггакрут"
    wts_updates[21550] = "|cffe4cfa3Король Гномрегана|r"
    wts_updates[21578] = "|cffe4cfa3Король Гномрегана|r"
    wts_updates[21551] = "|cffe4cfa3Король Гномрегана|r"
    wts_updates[21630] = "|cffe4cfa3Король Гномрегана|r"
    wts_updates[21552] = "|cffe4cfa3Король Гномрегана|r"
    wts_updates[21631] = "|cffe4cfa3Король Гномрегана|r"
    gelbin_ubertip = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Лидер и верховный главный механик Гномрегана на борту персонального боевого мехакостюма.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПерегрузка|cffced4da: резкое ускорение атаки ценой скорости перемещения.|n"
        "- |cffa9c7deРаздвоенная молния|cffced4da: поражает молниями веер целей перед собой.|n"
        "- |cffa9c7deКомпозитная броня|cffced4da: снижает получаемый от атак урон.|n"
        "- |cffa9c7deРежим дальнего боя|cffced4da: переключает мехакостюм в дистанционный режим атаки.|n"
        "- |cffa9c7deЗащитные алгоритмы|cffced4da: повышает броню при потере здоровья.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )
    wts_updates[21570] = gelbin_ubertip
    wts_updates[21632] = gelbin_ubertip

    # MIMH: Перекованный хранитель (Мимирон V2.0)
    wts_updates[1238] = "|cffe4cfa3Перекованный хранитель|r"
    wts_updates[17674] = "Мимирон V2.0"
    wts_updates[1239] = "|cffe4cfa3Перекованный хранитель|r"
    wts_updates[1241] = "|cffe4cfa3Перекованный хранитель|r"
    wts_updates[1240] = "|cffe4cfa3Перекованный хранитель|r"
    wts_updates[17696] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный титанический хранитель-изобретатель, перекованный гномами. Создаёт несокрушимых боевых автоматонов и восстанавливает технику союзников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМеха-гвардия|cffced4da: призывает автоматонов на поле боя.|n"
        "- |cffa9c7deПолевой ремонт|cffced4da: восстанавливает здоровье союзной технике.|n"
        "- |cffa9c7deПерегрузка|cffced4da: значительно ускоряет атаку союзника взамен на здоровье.|n"
        "- |cffa9c7deМастерство хранителя|cffced4da: конструирует гигантского Железного хранителя.|n|n"
        "|cffced4daАтакует наземные и воздушные цели.|r"
    )

    for hid, name_sid, tip_sid, ub_sid in [
        ('H0GC', 24597, 25190, 20027),
        ('H0GD', 25193, 19666, 20032),
        ('H0GE', 25194, 25196, 20033),
        ('H0GF', 25252, 19698, 20034),
        ('H0GG', 25253, 25255, 20028),
        ('H0HQ', 21549, 21550, 21570),
        ('H0HS', 21576, 21578, 21632),
        ('MIMH', 1238, 1239, 17696),
    ]:
        checks_def.append({"type": "unit", "id": hid, "field": "name", "expected": wts_updates[name_sid]})
        checks_def.append({"type": "unit", "id": hid, "field": "tip", "expected": wts_updates[tip_sid]})
        checks_def.append({"type": "unit", "id": hid, "field": "ubertip", "expected": wts_updates[ub_sid]})

    # =========================================================================
    # 6. UPGRADES (60)
    # =========================================================================
    # Helper to add single-level upgrade
    def add_upg_1(uid, name_sid, tip_sid, ub_sid, name, hotkey, effect_desc, applied_units=None):
        wts_updates[name_sid] = f"|cffe4cfa3{name}|r"
        hk_str = f" (|cffffffff{hotkey}|r)" if hotkey else ""
        wts_updates[tip_sid] = f"|cffe4cfa3{name}|r{hk_str}"
        ub_lines = [f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da {effect_desc}|r"]
        if applied_units:
            ub_lines.append("|n|n|cffa6afb8Применяется к:|cffced4da")
            for u in applied_units:
                ub_lines.append(f"|n- |cffa9c7de{u}|cffced4da")
            ub_lines.append(".|r")
        wts_updates[ub_sid] = "".join(ub_lines)
        checks_def.append({"type": "upgrade", "id": uid, "field": "name1", "expected": wts_updates[name_sid]})
        checks_def.append({"type": "upgrade", "id": uid, "field": "tip1", "expected": wts_updates[tip_sid]})
        checks_def.append({"type": "upgrade", "id": uid, "field": "ubertip1", "expected": wts_updates[ub_sid]})

    add_upg_1('R0B5', 9575, 9576, 9586, 'Проект «Механопаук»', 'S',
              'Открывает сборку Механопауков на Фабрике.', ['Механопаук'])
    add_upg_1('R0B7', 17569, 17570, 17530, 'Закрыть проект «Клап Клап»', 'R',
              'Останавливает дальнейшее производство базовой версии роботов Клап Клап.')
    add_upg_1('R0B8', 9457, 9461, 9462, 'Клап Клап в военной сфере', 'Q',
              'Увеличивает атаку роботов серии Клап Клап на |cffc8e087+5|cffced4da ед.',
              ['Клап Клап (v0.58889)', 'Клап Клап (v1.0 Opt)', 'Клап Клап (v1.0 Big)'])
    add_upg_1('R0B9', 9467, 9478, 9482, 'Проект «Реженоги»', 'W',
              'Открывает производство скоростных роботов Реженоги на Фабрике.', ['Реженоги'])
    add_upg_1('R0BA', 9483, 9549, 9550, 'Проект «Механобоец»', 'A',
              'Открывает сборку штурмовых Механобойцев на Фабрике.', ['Механобоец'])
    add_upg_1('R0BB', 9572, 9573, 9574, 'Проект «Минитанк»', 'X',
              'Открывает производство маневренных Минитанков в Мастерской.', ['Минитанк'])
    add_upg_1('R0BC', 9587, 9588, 17680, 'Проект «Наногном»', 'A',
              'Открывает подготовку Наногномов на Фабрике.', ['Наногном'])
    add_upg_1('R0BD', 9589, 9744, 9745, 'Проект «Экспериментальный ГГТ»', 'Z',
              'Открывает производство модульных боевых машин ГГТ в Мастерской.', ['Экспериментальный ГГТ'])
    add_upg_1('R0BE', 9746, 9753, 9818, 'Проект «Шагоход»', 'S',
              'Открывает производство автоматических Шагоходов на Фабрике.', ['Шагоход'])
    add_upg_1('R0BF', 9819, 9820, 9821, 'Проект «Универсальный танк»', 'X',
              'Открывает производство Универсальных танков в Мастерской.', ['Универсальный танк'])
    add_upg_1('R0BG', 9833, 9834, 9836, 'Проект «Танк Венец»', 'X',
              'Открывает производство сверхтяжёлого танка «Венец» в Мастерской.', ['Танк «Венец»'])
    add_upg_1('R0BH', 9837, 9838, 17806, 'Проект «Мехагигант»', 'A',
              'Открывает сборку титанических Мехагигантов на Фабрике.', ['Мехагигант'])
    add_upg_1('R0BI', 9839, 9841, 9855, 'Проект «Бронемашина»', 'Z',
              'Открывает сборку Бронемашин десанта и снабжения в Мастерской.', ['Бронемашина'])
    add_upg_1('R0BJ', 9857, 9860, 9914, 'Клап Клап на производственном фронте', 'W',
              'Увеличивает скорость перемещения роботов на |cffc8e087+15%|cffced4da и добычу древесины на |cffc8e087+15|cffced4da ед.',
              ['Клап Клап (v0.58889)', 'Клап Клап (v1.0 Opt)', 'Клап Клап (v1.0 Big)'])
    add_upg_1('R0BK', 9915, 9916, 9917, 'Клап Клап подрывник', 'S',
              'Оснащает роботов Клап Клап взрывчаткой, открывая способность взрываться при гибели.',
              ['Клап Клап (v0.58889)', 'Клап Клап (v1.0 Opt)', 'Клап Клап (v1.0 Big)'])
    add_upg_1('R0BL', 9918, 9919, 9920, 'Клап Клап — механический щит', 'S',
              'Повышает броню на |cffc8e087+1|cffced4da и здоровье на |cffc8e087+150|cffced4da ед.',
              ['Клап Клап (v0.58889)', 'Клап Клап (v1.0 Opt)', 'Клап Клап (v1.0 Big)'])
    add_upg_1('R0BM', 9921, 9922, 9923, 'Клап Клап — добытчик древесины', 'S',
              'Увеличивает объём добываемой древесины на |cffc8e087+25|cffced4da ед.',
              ['Клап Клап (v0.58889)', 'Клап Клап (v1.0 Opt)', 'Клап Клап (v1.0 Big)'])
    add_upg_1('R0BN', 9927, 9928, 18027, 'Поставить Клап Клап на поток', 'S',
              'Снижает затраты ресурсов на производство всех моделей роботов Клап Клап.',
              ['Клап Клап (v0.58889)', 'Клап Клап (v1.0 Opt)', 'Клап Клап (v1.0 Big)'])
    add_upg_1('R0BO', 9948, 9950, 10532, 'Огромный Клап Клап', 'S',
              'Открывает сборку тяжёлой модификации робота Клап Клап (v1.0 Big) на Фабрике.',
              ['Клап Клап (v1.0 Big)'])
    add_upg_1('R0BP', 10626, 10629, 18109, 'Улучшение добычи Клап Клапа', 'X',
              'Увеличивает объём собираемой древесины на |cffc8e087+50|cffced4da ед.',
              ['Клап Клап (v0.58889)', 'Клап Клап (v1.0 Opt)', 'Клап Клап (v1.0 Big)'])
    add_upg_1('R0BQ', 10635, 10636, 10639, 'Мехавоин-защитник', 'Q',
              'Увеличивает броню Механобойца на |cffc8e087+1|cffced4da ед.', ['Механобоец'])
    add_upg_1('R0BR', 10641, 10994, 18207, 'Улучшенные поршни', 'W',
              'Повышает вероятность оглушения цели атаками Механобойца с |cffffffff15%|cffced4da до |cffc8e08725%|cffced4da.', ['Механобоец'])
    add_upg_1('R0BT', 10995, 10996, 10997, 'Переделать шасси', 'E',
              'Увеличивает скорость перемещения Минитанка.', ['Минитанк'])
    add_upg_1('R0C0', 10998, 10999, 18450, 'Проект «Самоходная артиллерия»', 'Z',
              'Открывает производство Самоходной артиллерии в Мастерской.', ['Самоходная артиллерия'])
    add_upg_1('R0C1', 11000, 11001, 19392, 'Проект «Сверхмассивная артиллерия»', 'F',
              'Открывает производство Мега-Артиллерии в Мастерской.', ['Мега-Артиллерия'])
    add_upg_1('R0C2', 11002, 11003, 11004, 'Управление электронами', 'Q',
              'Открывает Наногномам способность «Электрическое поле».', ['Наногном'])
    add_upg_1('R0C3', 19997, 19998, 20083, 'Улучшенный мотор', 'W',
              'Увеличивает скорость перемещения Самоходной артиллерии.', ['Самоходная артиллерия'])
    add_upg_1('R0C4', 11005, 11006, 11007, 'Проект «Мега-бомба»', 'F',
              'Открывает для Мега-Артиллерии разрушительную ядерную способность «Аннигиляция».', ['Мега-Артиллерия'])
    add_upg_1('R0C5', 11008, 11009, 11010, 'Оптимизировать перезарядку', 'Q',
              'Увеличивает скорость атаки Минитанка на |cffc8e087+20%|cffced4da.', ['Минитанк'])
    add_upg_1('R0C6', 11011, 11012, 11014, 'Новая модель артпушки', 'W',
              'Усиливает урон способности «Артвыстрел» у Минитанка.', ['Минитанк'])
    add_upg_1('R0C7', 22044, 22045, 22046, 'Улучшенная моторика', 'W',
              'Увеличивает скорость перемещения Шагоходов.', ['Шагоход'])
    add_upg_1('R0C8', 7359, 7360, 11017, 'Разрядка', 'W',
              'Атаки Наногнома сжигают ману цели и наносят равный дополнительный урон.', ['Наногном'])
    add_upg_1('R0C9', 11018, 11019, 11020, 'Дополнительный слой брони', 'Q',
              'Увеличивает запас здоровья танка «Венец» на |cffc8e087+250|cffced4da ед., снижая его скорость бега на |cffe69a8d30|cffced4da ед.', ['Танк «Венец»'])
    add_upg_1('R0CA', 11021, 11022, 11023, 'Качественные снаряды', 'W',
              'Увеличивает урон основных орудий танка «Венец».', ['Танк «Венец»'])
    add_upg_1('R0CB', 11024, 11025, 11027, 'Продвинутая система подачи ракет', 'E',
              'Увеличивает урон ракетных залпов танка «Венец».', ['Танк «Венец»'])
    add_upg_1('R0CC', 11028, 11029, 11030, 'Усилить пулемёты', 'W',
              'Повышает урон пулемётного огня Универсального танка.', ['Универсальный танк'])
    add_upg_1('R0CD', 11031, 11032, 19383, 'Улучшенная перезарядка огнемёта', 'E',
              'Сокращает время перезарядки способности «Сгусток огня» Универсального танка.', ['Универсальный танк'])
    add_upg_1('R0CE', 11033, 11034, 11035, 'Усилить снаряды', 'Q',
              'Увеличивает урон орудийных атак Универсального танка.', ['Универсальный танк'])
    add_upg_1('R0CF', 6996, 7000, 20551, 'Бронебойные снаряды', 'Q',
              'Увеличивает урон Шагохода по целям с тяжёлой бронёй на |cffc8e087+10%|cffced4da.', ['Шагоход'])
    add_upg_1('R0CG', 11038, 11039, 11040, 'Разрывные снаряды', 'W',
              'Увеличивает урон Шагохода по целям с лёгкой бронёй на |cffc8e087+20%|cffced4da.', ['Шагоход'])
    add_upg_1('R0CH', 11041, 11042, 11043, 'ГГТ — Огнемётный танк', 'Q',
              'Открывает огнемётную атаку для экспериментального танка ГГТ.', ['Экспериментальный ГГТ'])
    add_upg_1('R0CI', 11044, 11045, 11046, 'ГГТ — минизавод на колёсах', 'W',
              'Позволяет экспериментальному танку ГГТ производить роботов Реженоги на поле боя.', ['Экспериментальный ГГТ'])
    add_upg_1('R0CJ', 11047, 11048, 11049, 'Усилить моторы бронемашины', 'Q',
              'Увеличивает скорость передвижения Бронемашины.', ['Бронемашина'])
    add_upg_1('R0CK', 11050, 11051, 19809, 'Машина для снабжения', 'E',
              'Наделяет Бронемашину аурой хорошей логистики, повышающей скорость перемещения и атаки союзной техники.', ['Бронемашина'])
    add_upg_1('R0CL', 11052, 11053, 11054, 'Улучшенный пулемёт', 'W',
              'Увеличивает урон бортового пулемёта Бронемашины.', ['Бронемашина'])
    add_upg_1('R0CM', 11055, 11056, 11057, 'ГГТ — миноукладчик', 'E',
              'Позволяет экспериментальному танку ГГТ устанавливать скрытые мины.', ['Экспериментальный ГГТ'])
    add_upg_1('R0CN', 11058, 11059, 11060, 'Улучшенная калибровка', 'W',
              'Увеличивает дальность стрельбы Самоходной артиллерии.', ['Самоходная артиллерия'])
    add_upg_1('R0CO', 11061, 11062, 11063, 'Сверхмассивные снаряды', 'Q',
              'Увеличивает урон снарядов Самоходной артиллерии.', ['Самоходная артиллерия'])
    add_upg_1('R0CP', 11064, 11072, 11073, 'Сверхмассивная броня', 'Q',
              'Увеличивает максимальный запас здоровья Мехагиганта.', ['Мехагигант'])
    add_upg_1('R0CQ', 11074, 11075, 11076, 'Шокоудары', 'W',
              'Атаки Мехагиганта получают способность наносить урон по области.', ['Мехагигант'])
    add_upg_1('R0CR', 11077, 11078, 11079, 'Урон от когтей', 'Q',
              'Увеличивает урон атак Механопаука.', ['Механопаук'])
    add_upg_1('R0CS', 11080, 11081, 11082, 'Улучшенный ракетомёт', 'W',
              'Усиливает урон способности «Залп ракет» у Механопаука.', ['Механопаук'])

    # Multi-level upgrades (6 levels each):
    # R0CT: Вооружение (6 levels)
    r0ct_names = [38987, 38988, 38989, 38991, 38992, 38993]
    r0ct_tips = [38990, 38994, 38995, 38996, 38997, 38998]
    r0ct_ubs = [11189, 11190, 11214, 11215, 11216, 11217]
    for lvl in range(1, 7):
        wts_updates[r0ct_names[lvl - 1]] = f"|cffe4cfa3Вооружение — уровень {lvl}|r"
        wts_updates[r0ct_tips[lvl - 1]] = f"|cffe4cfa3Вооружение — уровень {lvl}|r (|cffffffffX|r)"
        wts_updates[r0ct_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон дальнобойных боевых единиц гномов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deПодрывник|cffced4da|n- |cffa9c7deШагоход|cffced4da|n- |cffa9c7deСамоходная артиллерия|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R0CT", "field": "name1", "expected": wts_updates[38987]})
    checks_def.append({"type": "upgrade", "id": "R0CT", "field": "tip1", "expected": wts_updates[38990]})
    checks_def.append({"type": "upgrade", "id": "R0CT", "field": "ubertip1", "expected": wts_updates[11189]})

    # R0CU: Прочные детали (6 levels)
    r0cu_names = [11218, 11219, 11220, 11222, 11223, 11224]
    r0cu_tips = [11221, 11225, 11226, 11227, 11228, 11229]
    r0cu_ubs = [11230, 11231, 11232, 11233, 11234, 11235]
    for lvl in range(1, 7):
        wts_updates[r0cu_names[lvl - 1]] = f"|cffe4cfa3Прочные детали — уровень {lvl}|r"
        wts_updates[r0cu_tips[lvl - 1]] = f"|cffe4cfa3Прочные детали — уровень {lvl}|r (|cffffffffC|r)"
        wts_updates[r0cu_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню всех боевых единиц и техники гномов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПехота и техника гномов|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R0CU", "field": "name1", "expected": wts_updates[11218]})
    checks_def.append({"type": "upgrade", "id": "R0CU", "field": "tip1", "expected": wts_updates[11221]})
    checks_def.append({"type": "upgrade", "id": "R0CU", "field": "ubertip1", "expected": wts_updates[11230]})

    # R0CV: Улучшенная тренировка пехоты (6 levels)
    r0cv_names = [11236, 11237, 11238, 11240, 11241, 11242]
    r0cv_tips = [11239, 11243, 11244, 11245, 11246, 11247]
    r0cv_ubs = [11248, 11249, 11250, 11251, 11252, 11253]
    for lvl in range(1, 7):
        wts_updates[r0cv_names[lvl - 1]] = f"|cffe4cfa3Улучшенная тренировка пехоты — уровень {lvl}|r"
        wts_updates[r0cv_tips[lvl - 1]] = f"|cffe4cfa3Улучшенная тренировка пехоты — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0cv_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки и перемещения пехоты, а также повышает запас и регенерацию маны заклинателей.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГном-пехотинец|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deШпион|cffced4da|n- |cffa9c7deГном-маг|cffced4da|n- |cffa9c7deГном-чернокнижник|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R0CV", "field": "name1", "expected": wts_updates[11236]})
    checks_def.append({"type": "upgrade", "id": "R0CV", "field": "tip1", "expected": wts_updates[11239]})
    checks_def.append({"type": "upgrade", "id": "R0CV", "field": "ubertip1", "expected": wts_updates[11248]})

    # R0CW: Улучшенные компоненты (6 levels)
    r0cw_names = [11254, 11255, 11256, 11258, 11259, 11260]
    r0cw_tips = [11257, 11261, 11361, 11362, 11363, 11515]
    r0cw_ubs = [12660, 12836, 12839, 12852, 12853, 14450]
    for lvl in range(1, 7):
        wts_updates[r0cw_names[lvl - 1]] = f"|cffe4cfa3Улучшенные компоненты — уровень {lvl}|r"
        wts_updates[r0cw_tips[lvl - 1]] = f"|cffe4cfa3Улучшенные компоненты — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0cw_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки, перемещения и максимальный запас здоровья боевой техники Мастерской.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deУниверсальный танк|cffced4da|n- |cffa9c7deТанк «Венец»|cffced4da|n- |cffa9c7deМинитанк|cffced4da|n- |cffa9c7deЭкспериментальный ГГТ|cffced4da|n- |cffa9c7deБронемашина|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R0CW", "field": "name1", "expected": wts_updates[11254]})
    checks_def.append({"type": "upgrade", "id": "R0CW", "field": "tip1", "expected": wts_updates[11257]})
    checks_def.append({"type": "upgrade", "id": "R0CW", "field": "ubertip1", "expected": wts_updates[12660]})

    # R0CX: Улучшенное управление (6 levels)
    r0cx_names = [17162, 17175, 17176, 17178, 17179, 17180]
    r0cx_tips = [17177, 18358, 18359, 18360, 18361, 19473]
    r0cx_ubs = [19508, 19509, 19871, 19873, 19874, 19996]
    for lvl in range(1, 7):
        wts_updates[r0cx_names[lvl - 1]] = f"|cffe4cfa3Улучшенное управление — уровень {lvl}|r"
        wts_updates[r0cx_tips[lvl - 1]] = f"|cffe4cfa3Улучшенное управление — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0cx_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки, перемещения и максимальный запас здоровья боевых единиц Фабрики.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШагоход|cffced4da|n- |cffa9c7deРеженоги|cffced4da|n- |cffa9c7deМехагигант|cffced4da|n- |cffa9c7deМеханобоец|cffced4da|n- |cffa9c7deНаногном|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R0CX", "field": "name1", "expected": wts_updates[17162]})
    checks_def.append({"type": "upgrade", "id": "R0CX", "field": "tip1", "expected": wts_updates[17177]})
    checks_def.append({"type": "upgrade", "id": "R0CX", "field": "ubertip1", "expected": wts_updates[19508]})

    # R0J2: Усиленная броня (6 levels)
    r0j2_names = [22047, 22295, 23110, 23339, 23340, 25937]
    r0j2_tips = [40979, 40980, 40981, 40982, 40983, 40984]
    r0j2_ubs = [25947, 25949, 25952, 25953, 25954, 28910]
    for lvl in range(1, 7):
        wts_updates[r0j2_names[lvl - 1]] = f"|cffe4cfa3Усиленная броня — уровень {lvl}|r"
        wts_updates[r0j2_tips[lvl - 1]] = f"|cffe4cfa3Усиленная броня — уровень {lvl}|r (|cffffffffX|r)"
        hp_bonus = lvl * 65
        wts_updates[r0j2_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье пехоты гномов на |cffc8e087+{hp_bonus}|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГном-пехотинец|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deПодрывник|cffced4da|n- |cffa9c7deГном-маг|cffced4da|n- |cffa9c7deГном-чернокнижник|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R0J2", "field": "name1", "expected": wts_updates[22047]})
    checks_def.append({"type": "upgrade", "id": "R0J2", "field": "tip1", "expected": wts_updates[40979]})
    checks_def.append({"type": "upgrade", "id": "R0J2", "field": "ubertip1", "expected": wts_updates[25947]})

    # =========================================================================
    # 7. ABILITIES
    # =========================================================================
    # A00S: Сильный удар (пехотинец)
    wts_updates[931] = "|cffe4cfa3Сильный удар|r"
    wts_updates[2000] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт с вероятностью |cffffffff12%|cffced4da нанести при атаке на |cffc8e087+10|cffced4da урона больше и оглушить цель на |cffffffff1|cffced4da сек. Не оглушает героев.|r"

    # A0D5: Осколочная граната (Стрелок-ветеран) (4 levels)
    wts_updates[22232] = "|cffe4cfa3Осколочная граната|r"
    wts_updates[22233] = "|cffe4cfa3Осколочная граната|r (|cffffffffW|r)"
    wts_updates[9516] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает в указанную область гранату, наносящую урон всем врагам в радиусе взрыва.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff40|cffced4da урона.|n"
        "|cffa6afb82-й уровень:|r |cffffffff60|cffced4da урона.|n"
        "|cffa6afb83-й уровень:|r |cffffffff80|cffced4da урона.|n"
        "|cffa6afb84-й уровень:|r |cffffffff100|cffced4da урона.|r"
    )
    a0d5_tips = [22238, 22253, 22254, 22264]
    a0d5_ubs = [18414, 18415, 18412, 19754]
    a0d5_dmg = [40, 60, 80, 100]
    for lvl in range(1, 5):
        wts_updates[a0d5_tips[lvl - 1]] = f"|cffe4cfa3Осколочная граната — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0d5_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает гранату в область, нанося |cffffffff{a0d5_dmg[lvl - 1]}|cffced4da ед. урона всем врагам в радиусе взрыва.|r"

    # A0GW: Аура меткости (Стрелок-ветеран) (4 levels)
    wts_updates[10220] = "|cffe4cfa3Аура меткости|r"
    wts_updates[10221] = "|cffe4cfa3Аура меткости|r (|cffffffffE|r)"
    wts_updates[39408] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон дистанционных атак находящихся рядом союзных войск.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+10%|cffced4da к урону.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+20%|cffced4da к урону.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087+30%|cffced4da к урону.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087+40%|cffced4da к урону.|r"
    )
    a0gw_tips = [10222, 10223, 10224, 10218]
    a0gw_ubs = [39409, 39410, 39411, 39407]
    a0gw_pct = [10, 20, 30, 40]
    for lvl in range(1, 5):
        wts_updates[a0gw_tips[lvl - 1]] = f"|cffe4cfa3Аура меткости — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[a0gw_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон находящихся рядом союзных стрелков на |cffc8e087+{a0gw_pct[lvl - 1]}%|cffced4da.|r"

    # A0I3: Небольшой скачок (Инженер)
    wts_updates[26484] = "|cffe4cfa3Небольшой скачок|r"
    wts_updates[10064] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[10976] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит работника на небольшое расстояние.|r"
    wts_updates[26476] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[26477] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит работника на небольшое расстояние.|r"

    # A0S2: Двойной выстрел (Танк «Венец»)
    wts_updates[26299] = "|cffe4cfa3Двойной выстрел|r"
    wts_updates[26302] = "|cffe4cfa3Двойной выстрел|r"
    wts_updates[11607] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При каждой атаке танк совершает повторный сдвоенный залп по цели.|r"

    # A0S6: Переключить режим (Танк «Венец»)
    wts_updates[15070] = "|cffe4cfa3Переключить режим|r"
    wts_updates[15670] = "|cffe4cfa3Переключить режим|r (|cffffffffW|r)"
    wts_updates[15671] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переключает орудия танка между осадным дальним огнём и скорострельными орудиями.|r"

    # A0S7: Залп ракет (Танк «Венец») (2 levels)
    wts_updates[26303] = "|cffe4cfa3Залп ракет|r"
    wts_updates[26304] = "|cffe4cfa3Залп ракет — уровень 1|r (|cffffffffQ|r)"
    wts_updates[26305] = "|cffe4cfa3Залп ракет — уровень 2|r (|cffffffffQ|r)"
    wts_updates[30204] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область ракетами, нанося до |cffffffff10|cffced4da ед. урона наземным врагам и оглушая их.|r"
    wts_updates[31138] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область ракетами, нанося до |cffffffff20|cffced4da ед. урона наземным врагам и оглушая их.|r"

    # A0S8: Сгусток огня (Универсальный танк)
    wts_updates[17430] = "|cffe4cfa3Сгусток огня|r"
    wts_updates[17432] = "|cffe4cfa3Сгусток огня|r (|cffffffffQ|r)"
    wts_updates[17433] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает струю раскалённого пламени из миниатюрного огнемёта, обжигая врагов в секторе перед танком.|r"

    # A0S9: Прицельная пальба из пулеметов (Универсальный танк)
    wts_updates[78] = "|cffe4cfa3Прицельная пальба из пулемётов|r"
    wts_updates[17436] = "|cffe4cfa3Прицельная пальба из пулемётов|r (|cffffffffW|r)"
    wts_updates[3057] = "|cffe4cfa3Прицельная пальба из пулемётов|r (|cffffffffW|r)"
    wts_updates[17439] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Открывает непрерывный огонь из спаренных пулемётов по конкретной выбранной цели.|r"

    # A0SA: Залп ракет (Механопаук) (2 levels)
    wts_updates[26306] = "|cffe4cfa3Залп ракет|r"
    wts_updates[26307] = "|cffe4cfa3Залп ракет — уровень 1|r (|cffffffffQ|r)"
    wts_updates[26308] = "|cffe4cfa3Залп ракет — уровень 2|r (|cffffffffQ|r)"
    wts_updates[19926] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область ракетами, нанося урон вражеским войскам.|r"
    wts_updates[19927] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область ракетами, нанося повышенный урон вражеским войскам.|r"

    # A0SB: Артвыстрел (Минитанк) (2 levels)
    wts_updates[26313] = "|cffe4cfa3Артвыстрел|r"
    wts_updates[26314] = "|cffe4cfa3Артвыстрел — уровень 1|r (|cffffffffQ|r)"
    wts_updates[26317] = "|cffe4cfa3Артвыстрел — уровень 2|r (|cffffffffQ|r)"
    wts_updates[32906] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Производит мощный выстрел по выбранной области. Наносит |cffffffff75%|cffced4da урона зданиям.|r"
    wts_updates[32907] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Производит мощный выстрел по выбранной области с повышенным уроном. Наносит |cffffffff75%|cffced4da урона зданиям.|r"

    # A0SC: Резня (Реженоги)
    wts_updates[4475] = "|cffe4cfa3Резня|r"
    wts_updates[4479] = "|cffe4cfa3Резня|r"
    wts_updates[4484] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки лезвиями рассекают нескольких противников одновременно. Дополнительные цели получают |cffffffff50%|cffced4da урона.|r"

    # A0SG: Сменить режим (Энергобашня)
    wts_updates[3058] = "|cffe4cfa3Сменить режим|r"
    wts_updates[8097] = "|cffe4cfa3Сменить режим|r (|cffffffffQ|r)"
    wts_updates[8098] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переводит энергобашню в активный боевой режим для обороны базы.|r"
    wts_updates[3059] = "|cffe4cfa3Сменить режим|r (|cffffffffQ|r)"
    wts_updates[5283] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переводит энергобашню в активный боевой режим для обороны базы.|r"

    # A0SH: Аннигиляция (Мега-Артиллерия)
    wts_updates[39534] = "|cffe4cfa3Аннигиляция|r"
    wts_updates[39535] = "|cffe4cfa3Аннигиляция|r (|cffffffffR|r)"
    wts_updates[6224] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Производит выстрел снарядом с расщепляющимся ядром, нанося колоссальный урон в огромном радиусе поражения.|r"

    # A0SK: Сильный удар (Механобоец)
    wts_updates[34320] = "|cffe4cfa3Сильный удар|r"
    wts_updates[34321] = "|cffe4cfa3Сильный удар — уровень 1|r"
    wts_updates[34319] = "|cffe4cfa3Сильный удар — уровень 2|r"
    wts_updates[18149] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff25%|cffced4da наносит дополнительный урон и оглушает цель на |cffffffff2|cffced4da сек.|r"

    # A0SN: Разрывные снаряды (Шагоход)
    wts_updates[6226] = "|cffe4cfa3Разрывные снаряды|r"
    wts_updates[6225] = "|cffe4cfa3Разрывные снаряды|r"
    wts_updates[16893] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки шагохода наносят на |cffc8e087+20%|cffced4da больше урона по целям с лёгкой бронёй.|r"

    # A0SO: Бронебойные снаряды (Шагоход)
    wts_updates[1269] = "|cffe4cfa3Бронебойные снаряды|r"
    wts_updates[1268] = "|cffe4cfa3Бронебойные снаряды|r"
    wts_updates[20165] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки шагохода наносят на |cffc8e087+10%|cffced4da больше урона по целям с тяжёлой бронёй.|r"

    # A0SZ: Выстрелить один снаряд (Мега-Артиллерия)
    wts_updates[7001] = "|cffe4cfa3Выстрелить один снаряд|r"
    wts_updates[7346] = "|cffe4cfa3Выстрелить один снаряд|r (|cffffffffQ|r)"
    wts_updates[27703] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Производит одиночный выстрел на огромную дистанцию, нанося урон в области падения снаряда.|r"

    # A0T0: ЭМИ (Наногном)
    wts_updates[26318] = "|cffe4cfa3ЭМИ|r"
    wts_updates[26523] = "|cffe4cfa3ЭМИ|r (|cffffffffQ|r)"

    # A0TC: Расстрел (Танк УТ v1.23) (4 levels)
    wts_updates[19671] = "|cffe4cfa3Расстрел|r"
    wts_updates[19672] = "|cffe4cfa3Расстрел|r (|cffffffffW|r)"
    wts_updates[19673] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает пулемётным огнём врагов в секторе перед собой.|n|n"
        "|cffa6afb81-й уровень:|r до |cffffffff4|cffced4da целей, |cffffffff40|cffced4da ед. урона.|n"
        "|cffa6afb82-й уровень:|r до |cffffffff6|cffced4da целей, |cffffffff70|cffced4da ед. урона.|n"
        "|cffa6afb83-й уровень:|r до |cffffffff8|cffced4da целей, |cffffffff100|cffced4da ед. урона.|n"
        "|cffa6afb84-й уровень:|r до |cffffffff10|cffced4da целей, |cffffffff130|cffced4da ед. урона.|r"
    )
    a0tc_tips = [19674, 19675, 19676, 19677]
    a0tc_ubs = [19678, 19679, 19680, 19681]
    a0tc_vals = [(4, 40), (6, 70), (8, 100), (10, 130)]
    for lvl in range(1, 5):
        targs, dmg = a0tc_vals[lvl - 1]
        wts_updates[a0tc_tips[lvl - 1]] = f"|cffe4cfa3Расстрел — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0tc_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает пулями до |cffffffff{targs}|cffced4da врагов в секторе перед собой, нанося |cffffffff{dmg}|cffced4da ед. урона каждому.|r"

    # A0TD: Экспериментальные аккумуляторы (Танк УТ v1.23) (2 levels)
    wts_updates[19682] = "|cffe4cfa3Экспериментальные аккумуляторы|r"
    wts_updates[19683] = "|cffe4cfa3Экспериментальные аккумуляторы|r"
    wts_updates[19684] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает интеллект героя.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+25|cffced4da к интеллекту.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+50|cffced4da к интеллекту.|r"
    )
    wts_updates[19685] = "|cffe4cfa3Экспериментальные аккумуляторы — уровень 1|r"
    wts_updates[26828] = "|cffe4cfa3Экспериментальные аккумуляторы — уровень 2|r"
    wts_updates[27230] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает интеллект героя на |cffc8e087+25|cffced4da.|r"
    wts_updates[27231] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает интеллект героя на |cffc8e087+50|cffced4da.|r"

    # A0TE: Ремонтная аура (Фронтовой Гений) (4 levels)
    wts_updates[19712] = "|cffe4cfa3Ремонтная аура|r"
    wts_updates[19713] = "|cffe4cfa3Ремонтная аура|r"
    wts_updates[19789] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение и восстанавливает здоровье находящихся рядом механизмов.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+10%|cffced4da к скорости бега, регенерация HP.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+15%|cffced4da к скорости бега, регенерация HP.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087+20%|cffced4da к скорости бега, регенерация HP.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087+25%|cffced4da к скорости бега, регенерация HP.|r"
    )
    a0te_tips = [19718, 19719, 19720, 19710]
    a0te_ubs = [19715, 19716, 19717, 19711]
    a0te_pct = [10, 15, 20, 25]
    for lvl in range(1, 5):
        wts_updates[a0te_tips[lvl - 1]] = f"|cffe4cfa3Ремонтная аура — уровень {lvl}|r"
        wts_updates[a0te_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения союзных механизмов на |cffc8e087+{a0te_pct[lvl - 1]}%|cffced4da и повышает восстановление их здоровья.|r"

    # A0TF: Разобрать бедолагу (Фронтовой Гений) (4 levels)
    wts_updates[20949] = "|cffe4cfa3Разобрать бедолагу|r"
    wts_updates[25621] = "|cffe4cfa3Разобрать бедолагу|r (|cffffffffW|r)"
    wts_updates[25622] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Уничтожает союзного механического юнита, восстанавливая собственное здоровье в размере его очков жизни.|r"
    a0tf_tips = [19722, 20950, 20951, 20952]
    a0tf_ubs = [20948, 20953, 20954, 20955]
    for lvl in range(1, 5):
        wts_updates[a0tf_tips[lvl - 1]] = f"|cffe4cfa3Разобрать бедолагу — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0tf_ubs[lvl - 1]] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Уничтожает механического юнита, поглощая его здоровье.|r"

    # A0TG: Раскат грома (Фронтовой Гений) (level 4)
    wts_updates[19734] = "|cffe4cfa3Раскат грома — уровень 4|r (|cffffffffQ|r)"
    wts_updates[19735] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бьёт по земле, нанося |cffffffff180|cffced4da ед. урона находящимся рядом наземным врагам и замедляя их бег и атаку.|r"

    # A0TH: Код Красный (Фронтовой Гений) (2 levels)
    wts_updates[34334] = "|cffe4cfa3Код Красный|r"
    wts_updates[19738] = "|cffe4cfa3Код Красный|r (|cffffffffR|r)"
    wts_updates[36658] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Экзоскелет переходит в режим предельной боевой мощности, резко ускоряя передвижение и скорость атаки.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+30%|cffced4da к скорости бега, |cffc8e087+50%|cffced4da к скорости атаки.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+40%|cffced4da к скорости бега, |cffc8e087+100%|cffced4da к скорости атаки.|r"
    )
    wts_updates[36050] = "|cffe4cfa3Код Красный — уровень 1|r (|cffffffffR|r)"
    wts_updates[36106] = "|cffe4cfa3Код Красный — уровень 2|r (|cffffffffR|r)"
    wts_updates[19741] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение на |cffc8e087+30%|cffced4da и скорость атаки на |cffc8e087+50%|cffced4da.|r"
    wts_updates[19742] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение на |cffc8e087+40%|cffced4da и скорость атаки на |cffc8e087+100%|cffced4da.|r"

    # A0TJ: Разрывные снаряды (Стрелок-ветеран) (4 levels)
    wts_updates[18559] = "|cffe4cfa3Разрывные снаряды|r"
    wts_updates[19762] = "|cffe4cfa3Разрывные снаряды|r (|cffffffffQ|r)"
    wts_updates[19772] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снаряжает мушкет разрывными патронами, повышая урон от атак и нанося урон по области.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+10|cffced4da к урону.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+20|cffced4da к урону.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087+30|cffced4da к урону.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087+40|cffced4da к урону.|r"
    )
    a0tj_tips = [19761, 18560, 18573, 18576]
    a0tj_ubs = [19764, 19765, 19766, 19767]
    a0tj_dmg = [10, 20, 30, 40]
    for lvl in range(1, 5):
        wts_updates[a0tj_tips[lvl - 1]] = f"|cffe4cfa3Разрывные снаряды — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a0tj_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffc8e087+{a0tj_dmg[lvl - 1]}|cffced4da к урону от атак героя. Атаки наносят урон по площади.|r"

    # A0TK: Ракетопад (Стрелок-ветеран) (2 levels)
    wts_updates[19773] = "|cffe4cfa3Ракетопад|r"
    wts_updates[19774] = "|cffe4cfa3Ракетопад|r (|cffffffffR|r)"
    wts_updates[19775] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на окружающих врагов волны падающих ракет.|n|n"
        "|cffa6afb81-й уровень:|r волны ракет по |cffffffff40|cffced4da ед. урона.|n"
        "|cffa6afb82-й уровень:|r волны ракет по |cffffffff80|cffced4da ед. урона.|r"
    )
    wts_updates[19776] = "|cffe4cfa3Ракетопад — уровень 1|r (|cffffffffR|r)"
    wts_updates[19777] = "|cffe4cfa3Ракетопад — уровень 2|r (|cffffffffR|r)"
    wts_updates[19778] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на находящихся рядом врагов волны падающих ракет, наносящих по |cffffffff40|cffced4da ед. урона.|r"
    wts_updates[19779] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на находящихся рядом врагов волны падающих ракет, наносящих по |cffffffff80|cffced4da ед. урона.|r"

    # A0TL: Хорошая логистика (Бронемашина)
    wts_updates[19800] = "|cffe4cfa3Хорошая логистика|r"
    wts_updates[19801] = "|cffe4cfa3Хорошая логистика|r"
    wts_updates[19802] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения и атаки находящихся рядом союзных боевых машин.|r"

    # A0TX: Проклятие (Гном-чернокнижник)
    wts_updates[39539] = "|cffe4cfa3Проклятие|r"
    wts_updates[39540] = "|cffe4cfa3Проклятие|r (|cffffffffW|r)"

    # A0TZ: Меткий выстрел (Стрелок)
    wts_updates[6950] = "|cffe4cfa3Меткий выстрел|r"
    wts_updates[7934] = "|cffe4cfa3Меткий выстрел|r"

    # A0U0: Отравленный кинжал (Шпион)
    wts_updates[5627] = "|cffe4cfa3Отравленный кинжал|r"
    wts_updates[5628] = "|cffe4cfa3Отравленный кинжал|r (|cffffffffW|r)"
    wts_updates[11557] = "|cffe4cfa3Отравленный кинжал|r (|cffffffffW|r)"
    wts_updates[12483] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает во врага отравленный кинжал, нанося |cffffffff50|cffced4da ед. урона мгновенно и периодический урон в течение |cffffffff7|cffced4da сек. Яд замедляет передвижение цели.|r"

    # A0U1: Отточенные навыки (Шпион)
    wts_updates[14120] = "|cffe4cfa3Отточенные навыки|r"
    wts_updates[14121] = "|cffe4cfa3Отточенные навыки|r"

    # A0U2: Снежная буря (Гном-маг)
    wts_updates[7347] = "|cffe4cfa3Снежная буря|r"
    wts_updates[7348] = "|cffe4cfa3Снежная буря|r (|cffffffffE|r)"
    wts_updates[40052] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область |cffffffff4|cffced4da волны ледяных осколков, наносящих урон врагам в радиусе действия.|r"

    # A0U3: Ускорение (Гном-маг)
    wts_updates[7357] = "|cffe4cfa3Ускорение|r"
    wts_updates[7356] = "|cffe4cfa3Ускорение|r (|cffffffffQ|r)"
    wts_updates[30451] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки союзника на |cffc8e087+10%|cffced4da и скорость передвижения на |cffc8e087+10%|cffced4da на |cffffffff30|cffced4da сек.|r"

    # A0U4: Морозный доспех (Гном-маг)
    wts_updates[39542] = "|cffe4cfa3Морозный доспех|r"
    wts_updates[39541] = "|cffe4cfa3Морозный доспех|r (|cffffffffW|r)"
    wts_updates[19865] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Укрывает союзника ледяным щитом, дающим |cffc8e087+3|cffced4da к броне и замедляющим атакующих в ближнем бою врагов.|r"

    # A0U5: Зажигательная граната (Подрывник)
    wts_updates[19868] = "|cffe4cfa3Зажигательная граната|r"
    wts_updates[19869] = "|cffe4cfa3Зажигательная граната|r (|cffffffffQ|r)"
    wts_updates[40053] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт столб пламени, наносящий врагам |cffffffff3|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек. Поражённые цели продолжают получать периодический урон.|r"

    # A0U7: Сожжение (Наногном)
    wts_updates[39552] = "|cffe4cfa3Сожжение|r"
    wts_updates[39553] = "|cffe4cfa3Сожжение|r"
    wts_updates[19803] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака уничтожает ману цели и наносит ей равный дополнительный урон.|r"

    # A0U8: Шокоудары (Мехагигант)
    wts_updates[26537] = "|cffe4cfa3Шокоудары|r"
    wts_updates[26538] = "|cffe4cfa3Шокоудары|r"

    # A0U9: Произвести реженоги (Экспериментальный ГГТ)
    wts_updates[7362] = "|cffe4cfa3Произвести реженоги|r"
    wts_updates[7363] = "|cffe4cfa3Произвести реженоги|r (|cffffffffQ|r)"
    wts_updates[7364] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт боевого робота «Реженоги» со сроком службы |cffffffff3|cffced4da мин.|r"

    # A0UA: Закопать мину (Экспериментальный ГГТ)
    wts_updates[9498] = "|cffe4cfa3Закопать мину|r"
    wts_updates[9499] = "|cffe4cfa3Закопать мину|r (|cffffffffW|r)"
    wts_updates[10633] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Устанавливает скрытую мину в указанной точке, взрывающуюся при приближении противника.|r"

    # A0UW: Ба-бах! (Клап Клап v1.0 Big)
    wts_updates[12485] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При гибели взрывается, нанося до |cffffffff65|cffced4da ед. урона в небольшой области.|r"

    # A0XB: Композитная броня (Король Гномрегана) (4 levels)
    wts_updates[86] = "|cffe4cfa3Композитная броня|r"
    wts_updates[20440] = "|cffe4cfa3Композитная броня|r (|cffffffffE|r)"
    wts_updates[20441] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Укреплённые пластины брони снижают получаемый урон от вражеских атак.|n|n"
        "|cffa6afb81-й уровень:|r поглощает до |cffffffff10|cffced4da ед. урона.|n"
        "|cffa6afb82-й уровень:|r поглощает до |cffffffff20|cffced4da ед. урона.|n"
        "|cffa6afb83-й уровень:|r поглощает до |cffffffff30|cffced4da ед. урона.|n"
        "|cffa6afb84-й уровень:|r поглощает до |cffffffff40|cffced4da ед. урона.|r"
    )
    a0xb_tips = [20379, 20442, 20443, 20444]
    a0xb_ubs = [20445, 20446, 20453]  # Note: lvl 1 has no custom wts ubtip
    for lvl in range(1, 5):
        wts_updates[a0xb_tips[lvl - 1]] = f"|cffe4cfa3Композитная броня — уровень {lvl}|r (|cffffffffE|r)"
    wts_updates[20445] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает входящий урон от атак, поглощая до |cffffffff20|cffced4da ед. урона.|r"
    wts_updates[20446] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает входящий урон от атак, поглощая до |cffffffff30|cffced4da ед. урона.|r"
    wts_updates[20453] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает входящий урон от атак, поглощая до |cffffffff40|cffced4da ед. урона.|r"

    # A0XC: Защитные алгоритмы (Король Гномрегана)
    wts_updates[21646] = "|cffe4cfa3Защитные алгоритмы|r"
    wts_updates[21647] = "|cffe4cfa3Защитные алгоритмы|r (|cffffffffD|r)"
    wts_updates[21648] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Чем меньше запас здоровья героя, тем выше его броня. При активации мгновенно восполняет |cffc8e08710%|cffced4da здоровья.|r"

    # A0XE: Перегрузка (Король Гномрегана) (4 levels)
    wts_updates[19379] = "|cffe4cfa3Перегрузка|r"
    wts_updates[21382] = "|cffe4cfa3Перегрузка|r (|cffffffffQ|r)"
    wts_updates[21384] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Временно значительно повышает скорость атаки костюма ценой снижения скорости передвижения.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+30%|cffced4da к скорости атаки, |cffe69a8d-20%|cffced4da к скорости бега.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+50%|cffced4da к скорости атаки, |cffe69a8d-20%|cffced4da к скорости бега.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087+70%|cffced4da к скорости атаки, |cffe69a8d-20%|cffced4da к скорости бега.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087+90%|cffced4da к скорости атаки, |cffe69a8d-20%|cffced4da к скорости бега.|r"
    )
    a0xe_tips = [21383, 21387, 21389, 21393]
    a0xe_ubs = [21399, 21401, 21402, 21403]
    a0xe_atk = [30, 50, 70, 90]
    for lvl in range(1, 5):
        wts_updates[a0xe_tips[lvl - 1]] = f"|cffe4cfa3Перегрузка — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a0xe_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+{a0xe_atk[lvl - 1]}%|cffced4da, но снижает скорость перемещения на |cffe69a8d20%|cffced4da.|r"

    # A0XF: Раздвоенная молния (Король Гномрегана) (level 4)
    wts_updates[26897] = "|cffe4cfa3Раздвоенная молния — уровень 4|r (|cffffffffW|r)"
    wts_updates[21352] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молниями врагов в секторе перед собой, нанося |cffffffff300|cffced4da ед. урона.|r"

    # A0XG: Режим дальнего боя (Король Гномрегана) (2 levels)
    wts_updates[26574] = "|cffe4cfa3Режим дальнего боя|r"
    wts_updates[21637] = "|cffe4cfa3Режим дальнего боя|r (|cffffffffR|r)"
    wts_updates[21638] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переключает боевой костюм короля в дальнобойный режим атаки ракетами и орудиями.|r"
    wts_updates[26580] = "|cffe4cfa3Режим дальнего боя — уровень 1|r (|cffffffffR|r)"
    wts_updates[26572] = "|cffe4cfa3Режим дальнего боя — уровень 2|r (|cffffffffR|r)"
    wts_updates[21641] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Гелбин активирует дальнобойные орудия боевого костюма.|r"
    wts_updates[21633] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Гелбин активирует дальнобойные орудия боевого костюма.|r"

    # A165: Скрыться (Шпион)
    wts_updates[5396] = "|cffe4cfa3Скрыться|r"
    wts_updates[5403] = "|cffe4cfa3Скрыться|r (|cffffffffQ|r)"
    wts_updates[39020] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет шпиону стать невидимым для противников.|r"

    # A16A: Электрическое поле (Наногном)
    wts_updates[26539] = "|cffe4cfa3Электрическое поле|r"
    wts_updates[26540] = "|cffe4cfa3Электрическое поле|r (|cffffffffW|r)"
    wts_updates[33884] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает цель вихрем молний, наносящим |cffffffff15|cffced4da ед. урона/сек. находящимся рядом войскам и механизмам.|r"

    # A1B9: Фазовый спаситель (Пехота и стрелки)
    wts_updates[7947] = "|cffe4cfa3Фазовый спаситель|r"
    wts_updates[7948] = "|cffe4cfa3Фазовый спаситель|r"
    wts_updates[30454] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При получении урона боец на |cffffffff0.5|cffced4da сек. переходит в иное измерение, получая неуязвимость к дальнейшему урону.|r"

    # AHfs: Огненный столб (Танк УТ v1.23) (level 4)
    wts_updates[5617] = "|cffe4cfa3Огненный столб — уровень 4|r (|cffffffffQ|r)"
    wts_updates[1441] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает столб огня, наносящий |cffffffff150|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек. и умеренный урон ещё |cffffffff6|cffced4da сек.|r"

    # ANab: Кислотная бомба (Танк УТ v1.23) (level 4)
    wts_updates[10969] = "|cffe4cfa3Кислотная бомба — уровень 4|r (|cffffffffE|r)"
    wts_updates[10970] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель и ближайших врагов кислотой на |cffffffff15|cffced4da сек., снижая броню на |cffffffff7|cffced4da ед. и нанося |cffffffff20|cffced4da ед. урона/сек. основной цели (|cffffffff13|cffced4da ед./сек. дополнительным целям).|r"

    # MIM1: Меха-гвардия (Мимирон MIMH) (4 levels)
    wts_updates[17896] = "|cffe4cfa3Меха-гвардия|r"
    wts_updates[18062] = "|cffe4cfa3Меха-гвардия|r (|cffffffffQ|r)"
    wts_updates[18068] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает защитников перекованного хранителя.|n|n"
        "|cffa6afb81-й уровень:|r призывает |cffffffff2|cffced4da Механобойца.|n"
        "|cffa6afb82-й уровень:|r призывает |cffffffff4|cffced4da Механобойца.|n"
        "|cffa6afb83-й уровень:|r призывает |cffffffff4|cffced4da Наногнома.|n"
        "|cffa6afb84-й уровень:|r призывает |cffffffff3|cffced4da Мехагиганта.|r"
    )
    mim1_tips = [17935, 17938, 17944, 17977]
    mim1_ubs = [17980, 18018, 18021, 18059]
    mim1_spawns = ["2 Механобойцов", "4 Механобойцов", "4 Наногномов", "3 Мехагигантов"]
    for lvl in range(1, 5):
        wts_updates[mim1_tips[lvl - 1]] = f"|cffe4cfa3Меха-гвардия — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[mim1_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff{mim1_spawns[lvl - 1]}|cffced4da на поле боя.|r"

    # MIM2: Полевой ремонт (Мимирон MIMH) (4 levels)
    wts_updates[18100] = "|cffe4cfa3Полевой ремонт|r"
    wts_updates[18103] = "|cffe4cfa3Полевой ремонт|r (|cffffffffW|r)"
    wts_updates[18729] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Используя технологии титанов, восстанавливает здоровье союзной технике вокруг героя.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087100|cffced4da ед. здоровья.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087150|cffced4da ед. здоровья.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087200|cffced4da ед. здоровья.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087300|cffced4da ед. здоровья.|r"
    )
    mim2_tips = [18157, 18160, 18166, 18198]
    mim2_ubs = [18201, 18563, 18564, 18728]
    mim2_hp = [100, 150, 200, 300]
    for lvl in range(1, 5):
        wts_updates[mim2_tips[lvl - 1]] = f"|cffe4cfa3Полевой ремонт — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[mim2_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087{mim2_hp[lvl - 1]}|cffced4da ед. здоровья союзной технике в радиусе действия.|r"

    # MIM3: Перегрузка (Мимирон MIMH) (4 levels)
    wts_updates[21398] = "|cffe4cfa3Перегрузка|r"
    wts_updates[19398] = "|cffe4cfa3Перегрузка|r (|cffffffffE|r)"
    wts_updates[19407] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Значительно повышает скорость атаки цели взамен на постепенную потерю здоровья.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+30%|cffced4da к скорости атаки, |cffe69a8d-10|cffced4da HP/сек.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+50%|cffced4da к скорости атаки, |cffe69a8d-15|cffced4da HP/сек.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087+70%|cffced4da к скорости атаки, |cffe69a8d-20|cffced4da HP/сек.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087+100%|cffced4da к скорости атаки, |cffe69a8d-25|cffced4da HP/сек.|r"
    )
    mim3_tips = [19382, 19391, 19395, 19396]
    mim3_ubs = [19386, 19387, 19388, 19390]
    mim3_vals = [(30, 10), (50, 15), (70, 20), (100, 25)]
    for lvl in range(1, 5):
        atk, hp = mim3_vals[lvl - 1]
        wts_updates[mim3_tips[lvl - 1]] = f"|cffe4cfa3Перегрузка — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[mim3_ubs[lvl - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки цели на |cffc8e087+{atk}%|cffced4da взамен на потерю |cffe69a8d{hp}|cffced4da HP/сек.|r"

    # MIM6: Мастерство хранителя (Мимирон MIMH) (2 levels)
    wts_updates[18794] = "|cffe4cfa3Мастерство хранителя|r"
    wts_updates[19377] = "|cffe4cfa3Мастерство хранителя|r (|cffffffffR|r)"
    wts_updates[18803] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da За |cffffffff8000|cffced4da золота и дерева в течение |cffffffff50|cffced4da сек. создаёт колоссального Железного хранителя.|n"
        "|cffe6c07bПроцесс нельзя прервать; контроль над героем будет временно утерян.|r|n|n"
        "|cffa6afb81-й уровень:|r максимум |cffffffff1|cffced4da хранитель.|n"
        "|cffa6afb82-й уровень:|r максимум |cffffffff2|cffced4da хранителя.|r"
    )
    wts_updates[19053] = "|cffe4cfa3Мастерство хранителя — уровень 1|r (|cffffffffR|r)"
    wts_updates[19128] = "|cffe4cfa3Мастерство хранителя — уровень 2|r (|cffffffffR|r)"
    wts_updates[19363] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da В течение |cffffffff50|cffced4da сек. конструирует Железного хранителя. Лимит: |cffffffff1|cffced4da хранитель.|r"
    wts_updates[19376] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da В течение |cffffffff50|cffced4da сек. конструирует Железного хранителя. Лимит: |cffffffff2|cffced4da хранителя.|r"

    # =========================================================================
    # 8. BUFFS
    # =========================================================================
    # B03Y: Аура меткости
    wts_updates[10231] = "|cffe4cfa3Аура меткости|r"
    wts_updates[207] = "|cffa6afb8ЭФФЕКТ:|cffced4da Увеличивает урон союзных войск дальнего боя.|r"

    # B05H: Перегрузка (Код Красный)
    wts_updates[7950] = "|cffe4cfa3Перегрузка (Код Красный)|r"
    wts_updates[19744] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и атаки героя значительно |cffc8e087увеличена|cffced4da благодаря экзоскелету.|r"

    # B05J: Аура логистики
    wts_updates[8382] = "|cffe4cfa3Аура логистики|r"
    wts_updates[8392] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и атаки союзной боевой техники |cffc8e087увеличена|cffced4da.|r"

    # B05L: Ускорение
    wts_updates[9446] = "|cffe4cfa3Ускорение|r"
    wts_updates[19872] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и атаки цели |cffc8e087увеличена|cffced4da на |cffffffff30|cffced4da сек.|r"

    # Save plan
    plan_data = {
        "race": "Gnomes",
        "race_id": 23,
        "total_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A0SD"],
            "markers": ["R0BX", "R0HW"],
            "buildings": [
                "h0FI", "h0FK", "h0FL", "h0FR", "h0FS", "h0FY", "h0FZ", "h0G0", "h0G3", "h0G7"
            ],
            "workers": ["h0FA", "h0FX"],
            "units": [
                "h0FB", "h0FC", "h0FD", "h0FE", "h0FF", "h0FG", "h0FH", "h0FJ", "h0FM", "h0FN",
                "h0FO", "h0FP", "h0FQ", "h0FT", "h0FU", "h0FV", "h0FW", "h0G1", "h0G2", "h0G4", "h0G5"
            ],
            "heroes": ["H0GC", "H0GD", "H0GE", "H0GF", "H0GG", "H0HQ", "H0HS", "MIMH"],
            "upgrades": [
                "R0B5", "R0B7", "R0B8", "R0B9", "R0BA", "R0BB", "R0BC", "R0BD", "R0BE", "R0BF",
                "R0BG", "R0BH", "R0BI", "R0BJ", "R0BK", "R0BL", "R0BM", "R0BN", "R0BO", "R0BP",
                "R0BQ", "R0BR", "R0BT", "R0BX", "R0C0", "R0C1", "R0C2", "R0C3", "R0C4", "R0C5",
                "R0C6", "R0C7", "R0C8", "R0C9", "R0CA", "R0CB", "R0CC", "R0CD", "R0CE", "R0CF",
                "R0CG", "R0CH", "R0CI", "R0CJ", "R0CK", "R0CL", "R0CM", "R0CN", "R0CO", "R0CP",
                "R0CQ", "R0CR", "R0CS", "R0CT", "R0CU", "R0CV", "R0CW", "R0CX", "R0HW", "R0J2"
            ],
            "abilities": [
                "A00S", "A0D5", "A0GW", "A0I3", "A0S2", "A0S6", "A0S7", "A0S8", "A0S9",
                "A0SA", "A0SB", "A0SC", "A0SD", "A0SG", "A0SH", "A0SK", "A0SN", "A0SO",
                "A0SZ", "A0T0", "A0TC", "A0TD", "A0TE", "A0TF", "A0TG", "A0TH", "A0TJ",
                "A0TK", "A0TL", "A0TX", "A0TZ", "A0U0", "A0U1", "A0U2", "A0U3", "A0U4",
                "A0U5", "A0U7", "A0U8", "A0U9", "A0UA", "A0UW", "A0XB", "A0XC", "A0XE",
                "A0XF", "A0XG", "A165", "A16A", "A1B9", "AHfs", "ANab", "MIM1", "MIM2",
                "MIM3", "MIM6"
            ],
            "buffs": ["B03Y", "B05H", "B05J", "B05L"]
        }
    }

    out_file = folder / "gnomes_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {out_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

    # -------------------------------------------------------------
    # GENERATE CATEGORY REGISTRIES
    # -------------------------------------------------------------
    dump_path = ROOT / "scripts/gnomes_raw_dump.json"
    dump = json.loads(dump_path.read_text(encoding="utf-8"))

    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    # 1. gnomes_selection.json
    sel_data = {
        "scope": "Гномы (Gnomes): подсказка выбора расы A0SD и маркеры",
        "object": "A0SD",
        "variants": ["SD"],
        "hotkey": {"value": "Q"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Gnomes регистрирует способность A0SD.",
            "При выборе создаются 5 рабочих Инженеров h0FA, 1 Клап Клап h0FX, исследуются маркеры R0BX и R0HW, удаляется выбирающий юнит, запускается триггер GnomesOn.",
            "Горячая клавиша Q, создатель VinerX, куратор VinerX, сложность 4/5 (●●●●○), период «World of Warcraft: Classic — Battle for Azeroth»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38895, "after": wts_updates[38895]},
            {"field": "tip1", "wts_id": 38896, "after": wts_updates[38896]},
            {"field": "ubertip1", "wts_id": 35199, "after": wts_updates[35199]}
        ],
        "markers": [
            {
                "id": "R0BX",
                "name": "Гномы (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 9241, "after": wts_updates[9241]},
                    {"field": "tip1", "wts_id": 9242, "after": wts_updates[9242]},
                    {"field": "ubertip1", "wts_id": 20125, "after": wts_updates[20125]}
                ]
            },
            {
                "id": "R0HW",
                "name": "Гномы (маркер альянса)",
                "strings": [
                    {"field": "name1", "wts_id": 30254, "after": wts_updates[30254]},
                    {"field": "tip1", "wts_id": 29941, "after": wts_updates[29941]}
                ]
            }
        ]
    }
    (folder / "gnomes_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote gnomes_selection.json")

    # 2. gnomes_buildings.json
    bld_entries = []
    for b in dump["buildings"]:
        b_id = b["id"]
        if b_id not in plan_data["categories"]["buildings"]:
            continue
        entry = {"id": b_id, "hotkey": b.get("hotkey"), "strings": []}
        for f in ["name", "tip", "ubertip"]:
            sid = parse_str_id(b.get(f"raw_{f}"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        bld_entries.append(entry)
    bld_data = {
        "scope": f"Гномы (Gnomes): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "gnomes_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gnomes_buildings.json ({len(bld_entries)} buildings)")

    # 3. gnomes_units.json
    unit_entries = []
    for u in dump["workers"] + dump["units"]:
        u_id = u["id"]
        entry = {"id": u_id, "hotkey": u.get("hotkey"), "strings": []}
        for f in ["name", "tip", "ubertip"]:
            sid = parse_str_id(u.get(f"raw_{f}"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        unit_entries.append(entry)
    unit_data = {
        "scope": f"Гномы (Gnomes): категория 2 — Юниты и рабочие ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "gnomes_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gnomes_units.json ({len(unit_entries)} units)")

    # 4. gnomes_heroes.json
    hero_entries = []
    for h in dump["heroes"]:
        h_id = h["id"]
        entry = {"id": h_id, "hotkey": h.get("hotkey"), "strings": []}
        for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            sid = parse_str_id(h.get(f"raw_{f}"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        hero_entries.append(entry)
    hero_data = {
        "scope": f"Гномы (Gnomes): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "gnomes_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gnomes_heroes.json ({len(hero_entries)} heroes)")

    # 5. gnomes_abilities.json
    abil_entries = []
    for a in dump["abilities"]:
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
        "scope": f"Гномы (Gnomes): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "gnomes_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gnomes_abilities.json ({len(abil_entries)} abilities)")

    # 6. gnomes_research.json
    upg_entries = []
    for u in dump["upgrades"]:
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
        upg_entries.append(entry)
    upg_data = {
        "scope": f"Гномы (Gnomes): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "gnomes_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gnomes_research.json ({len(upg_entries)} upgrades)")

    # 7. gnomes_audit.json
    audit_data = {
        "race": "Гномы (Gnomes)",
        "race_id": 23,
        "selection_ability": "A0SD",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries]
            },
            "workers": {
                "count": 2,
                "ids": ["h0FA", "h0FX"]
            },
            "units": {
                "count": 21,
                "ids": [
                    "h0FB", "h0FC", "h0FD", "h0FE", "h0FF", "h0FG", "h0FH", "h0FJ", "h0FM", "h0FN",
                    "h0FO", "h0FP", "h0FQ", "h0FT", "h0FU", "h0FV", "h0FW", "h0G1", "h0G2", "h0G4", "h0G5"
                ]
            },
            "heroes": {
                "count": len(hero_entries),
                "ids": [h["id"] for h in hero_entries],
                "names": {
                    "H0GC": "Танк УТ v1.23 (Интеллект, поддержка, наземная атака)",
                    "H0GD": "Фронтовой Гений (Сила, ближний бой, экзоскелет)",
                    "H0GE": "Фронтовой Гений (Сила, ближний бой, экзоскелет)",
                    "H0GF": "Фронтовой Гений (Сила, ближний бой, экзоскелет)",
                    "H0GG": "Стрелок-ветеран (Ловкость, дальний бой, ракеты)",
                    "H0HQ": "Король Гномрегана (Гелбин Меггакрут — Главный механик)",
                    "H0HS": "Король Гномрегана (Гелбин Меггакрут — Главный механик)",
                    "MIMH": "Перекованный хранитель (Мимирон V2.0 — Легендарный герой, Интеллект)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(plan_data["wts_updates"])
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0BX": "Маркер расы Гномы",
                    "R0HW": "Маркер альянса/гномов"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items or inventory artifacts found in war3map.w3t for Gnomes."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages or game UI strings found in war3map.wts for Gnomes."
        },
        "buffs_audit": {
            "custom_buffs": ["B03Y", "B05H", "B05J", "B05L"],
            "status": "Standardized custom buffs with secondary color labels and clean descriptions."
        },
        "total_wts_updates": len(plan_data["wts_updates"]),
        "total_checks": len(plan_data["checks_def"])
    }
    (folder / "gnomes_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote gnomes_audit.json")

if __name__ == "__main__":
    main()
