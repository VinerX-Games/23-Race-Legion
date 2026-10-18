# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Blood Elves race (Race 15)."""
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
    # 1. RACE SELECTION: A0HQ
    # =========================================================================
    wts_updates[38917] = "|cffe4cfa3Эльфы Крови|r"
    wts_updates[38918] = "|cffe4cfa3Эльфы Крови|r (|cffffffffE|r)"
    wts_updates[41060] = (
        "|cffa6afb8РАСА:|cffced4da Величественная цивилизация Кель'Таласа, черпающая колоссальную мощь из тайных и демонических источников магии.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Burning Crusade — Legion»|r|n|n"
        "|cffced4daЭльфы Крови — гордый и древний народ Син'Дорай, переживший падение своей родины и разрушение Солнечного Колодца под натиском Плети. "
        "В борьбе за выживание они научились подчинять опаснейшие школы магии: от чистой Арканы и священного Света до всепоглощающей Бездны и разрушительной Скверны. "
        "Армия Эльфов Крови сочетает метких следопытов, искусных ведьмаков, элитных паладинов и непревзойдённых заклинателей, а древние святилища позволяют выбрать "
        "одну из четырёх ветвей магической специализации и гибко адаптироваться к любой угрозе.|r"
    )

    checks_def.append({"type": "ability", "id": "A0HQ", "field": "name", "expected": wts_updates[38917]})
    checks_def.append({"type": "ability", "id": "A0HQ", "field": "tip1", "expected": wts_updates[38918]})
    checks_def.append({"type": "ability", "id": "A0HQ", "field": "ubertip1", "expected": wts_updates[41060]})

    # Selection markers: R07C, R0L0
    wts_updates[7984] = "|cffe4cfa3Эльфы Крови|r"
    wts_updates[7985] = "|cffe4cfa3Эльфы Крови|r"
    wts_updates[20110] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Эльфам Крови (Син'Дорай).|r"

    wts_updates[12039] = "|cffe4cfa3Эльфы Крови или Иллидари|r"
    wts_updates[12062] = "|cffe4cfa3Эльфы Крови или Иллидари|r"
    wts_updates[20115] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Эльфам Крови или Иллидари.|r"

    checks_def.append({"type": "upgrade", "id": "R07C", "field": "name1", "expected": wts_updates[7984]})
    checks_def.append({"type": "upgrade", "id": "R07C", "field": "tip1", "expected": wts_updates[7985]})
    checks_def.append({"type": "upgrade", "id": "R07C", "field": "ubertip1", "expected": wts_updates[20110]})

    # =========================================================================
    # 2. BUILDINGS (14 buildings)
    # =========================================================================
    # h04C: Ратуша (Q)
    wts_updates[17383] = "|cffe4cfa3Ратуша|r"
    wts_updates[17384] = "|cffe4cfa3Ратуша|r (|cffffffffQ|r)"
    wts_updates[6799] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Эльфов Крови первой ступени. Обучает строителей и служит складом древесины.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deФорт|cffced4da: открывает доступ к передовым сооружениям и войскам Эльфов Крови.|r"
    )
    checks_def.append({"type": "unit", "id": "h04C", "field": "name", "expected": wts_updates[17383]})
    checks_def.append({"type": "unit", "id": "h04C", "field": "tip", "expected": wts_updates[17384]})
    checks_def.append({"type": "unit", "id": "h04C", "field": "ubertip", "expected": wts_updates[6799]})

    # h04B: Форт (Z)
    wts_updates[17381] = "|cffe4cfa3Форт|r"
    wts_updates[17382] = "|cffe4cfa3Форт|r (|cffffffffZ|r)"
    wts_updates[28198] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Эльфов Крови второй ступени. Открывает доступ к Волшебному Святилищу, Хранилищу Энергии и передовым войскам.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЗамок|cffced4da: открывает доступ к высшим технологиям, элитным бойцам и осадным орудиям.|r"
    )
    checks_def.append({"type": "unit", "id": "h04B", "field": "name", "expected": wts_updates[17381]})
    checks_def.append({"type": "unit", "id": "h04B", "field": "tip", "expected": wts_updates[17382]})
    checks_def.append({"type": "unit", "id": "h04B", "field": "ubertip", "expected": wts_updates[28198]})

    # h04A: Замок (Z)
    wts_updates[17379] = "|cffe4cfa3Замок|r"
    wts_updates[17380] = "|cffe4cfa3Замок|r (|cffffffffZ|r)"
    wts_updates[6463] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Эльфов Крови третьей ступени. Открывает доступ к Мастерской, Рыцарям крови, Арканитовым големам и высшим ступеням улучшений.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h04A", "field": "name", "expected": wts_updates[17379]})
    checks_def.append({"type": "unit", "id": "h04A", "field": "tip", "expected": wts_updates[17380]})
    checks_def.append({"type": "unit", "id": "h04A", "field": "ubertip", "expected": wts_updates[6463]})

    # h04M: Сторожка (A)
    wts_updates[17389] = "|cffe4cfa3Сторожка|r"
    wts_updates[17390] = "|cffe4cfa3Сторожка|r (|cffffffffA|r)"
    wts_updates[31649] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Эльфов Крови запасом пищи и вырабатывает регулярный доход.|n|n"
        "Даёт |cffffffff15|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+40|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h04M", "field": "name", "expected": wts_updates[17389]})
    checks_def.append({"type": "unit", "id": "h04M", "field": "tip", "expected": wts_updates[17390]})
    checks_def.append({"type": "unit", "id": "h04M", "field": "ubertip", "expected": wts_updates[31649]})

    # h04D: Казармы (W)
    wts_updates[17386] = "|cffe4cfa3Казармы|r"
    wts_updates[17385] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[6494] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает базовые пехотные и кавалерийские силы Эльфов Крови.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтранник|cffced4da: базовый мечник ближнего боя.|n"
        "- |cffa9c7deСледопыт|cffced4da: меткий стрелок дальнего боя.|n"
        "- |cffa9c7deВсадник|cffced4da: быстрая конница ближнего боя.|n"
        "- |cffa9c7deРыцарь крови|cffced4da: элитный тяжеловооружённый паладин.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенные луки|cffced4da|n"
        "- |cffa9c7deЗащита от магии|cffced4da|n"
        "- |cffa9c7deТренировка следопытов|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h04D", "field": "name", "expected": wts_updates[17386]})
    checks_def.append({"type": "unit", "id": "h04D", "field": "tip", "expected": wts_updates[17385]})
    checks_def.append({"type": "unit", "id": "h04D", "field": "ubertip", "expected": wts_updates[6494]})

    # h04N: Дозорная Башня (Z)
    wts_updates[17392] = "|cffe4cfa3Дозорная Башня|r"
    wts_updates[17393] = "|cffe4cfa3Дозорная Башня|r (|cffffffffZ|r)"
    wts_updates[6508] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовая наблюдательная вышка. Обеспечивает обзор прилегающей территории. Не может атаковать до улучшения.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deСторожевая Башня|cffced4da: оснащается стрелковым оружием для отражения врагов.|n"
        "- |cffa9c7deМагическая Башня|cffced4da: атакует магической энергией, сжигающей ману врагов.|r"
    )
    checks_def.append({"type": "unit", "id": "h04N", "field": "name", "expected": wts_updates[17392]})
    checks_def.append({"type": "unit", "id": "h04N", "field": "tip", "expected": wts_updates[17393]})
    checks_def.append({"type": "unit", "id": "h04N", "field": "ubertip", "expected": wts_updates[6508]})

    # h04O: Сторожевая Башня (Z)
    wts_updates[17252] = "|cffe4cfa3Сторожевая Башня|r"
    wts_updates[17253] = "|cffe4cfa3Сторожевая Башня|r (|cffffffffZ|r)"
    wts_updates[6510] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительная стрелковая башня. Эффективна против лёгких войск и летающих существ.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h04O", "field": "name", "expected": wts_updates[17252]})
    checks_def.append({"type": "unit", "id": "h04O", "field": "tip", "expected": wts_updates[17253]})
    checks_def.append({"type": "unit", "id": "h04O", "field": "ubertip", "expected": wts_updates[6510]})

    # h04P: Магическая Башня (X)
    wts_updates[17254] = "|cffe4cfa3Магическая Башня|r"
    wts_updates[17255] = "|cffe4cfa3Магическая Башня|r (|cffffffffX|r)"
    wts_updates[6515] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Магическое оборонительное сооружение. Атакует магической энергией, уничтожая ману цели и нанося повышенный урон призванным существам.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПротиводействие|cffced4da: сжигает ману цели при попадании.|n"
        "- |cffa9c7deОбнаружение|cffced4da: раскрывает невидимых врагов в указанной области.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h04P", "field": "name", "expected": wts_updates[17254]})
    checks_def.append({"type": "unit", "id": "h04P", "field": "tip", "expected": wts_updates[17255]})
    checks_def.append({"type": "unit", "id": "h04P", "field": "ubertip", "expected": wts_updates[6515]})

    # h04Q: Лесопилка (E)
    wts_updates[17394] = "|cffe4cfa3Лесопилка|r"
    wts_updates[17395] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[12967] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Склад древесины и центр магических исследований энергосистемы.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенные инструменты|cffced4da|n"
        "- |cffa9c7deУлучшенная кладка|cffced4da|n"
        "- |cffa9c7deСтационарный магический источник|cffced4da|n"
        "- |cffa9c7deМобильные магические источники|cffced4da|n"
        "- |cffa9c7deМагическая выносливость|cffced4da|n"
        "- |cffa9c7deМагическая сила|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h04Q", "field": "name", "expected": wts_updates[17394]})
    checks_def.append({"type": "unit", "id": "h04Q", "field": "tip", "expected": wts_updates[17395]})
    checks_def.append({"type": "unit", "id": "h04Q", "field": "ubertip", "expected": wts_updates[12967]})

    # h04R: Кузница (R)
    wts_updates[17396] = "|cffe4cfa3Кузница|r"
    wts_updates[17397] = "|cffe4cfa3Кузница|r (|cffffffffR|r)"
    wts_updates[6516] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оружейная мастерская. Улучшает оружие, доспехи и артефакты войск Эльфов Крови, а также позволяет выбрать боевой приоритет армии.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОружие ближнего боя|cffced4da|n"
        "- |cffa9c7deОружие дальнего боя|cffced4da|n"
        "- |cffa9c7deТяжелая броня|cffced4da|n"
        "- |cffa9c7deЛегкая броня|cffced4da|n"
        "- |cffa9c7deАртефакты|cffced4da|n"
        "- |cffa9c7deПриоритет на Ведьмаках|cffced4da|n"
        "- |cffa9c7deПриоритет на Рыцарях крови|cffced4da|n"
        "- |cffa9c7deПриоритет на Анклаве магов|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h04R", "field": "name", "expected": wts_updates[17396]})
    checks_def.append({"type": "unit", "id": "h04R", "field": "tip", "expected": wts_updates[17397]})
    checks_def.append({"type": "unit", "id": "h04R", "field": "ubertip", "expected": wts_updates[6516]})

    # h05J: Алтарь Син'Дорай (S)
    wts_updates[17402] = "|cffe4cfa3Алтарь Син'Дорай|r"
    wts_updates[17403] = "|cffe4cfa3Алтарь Син'Дорай|r (|cffffffffS|r)"
    wts_updates[7762] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Призывает и воскрешает павших героев Эльфов Крови.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deМаг Крови|cffced4da: могущественный чародей, повелевающий огнём и поглощающий магическую энергию.|n"
        "- |cffa9c7deРенджер|cffced4da: искусный стрелок, усиливающий союзников аурой меткости и поражающий врагов зачарованными стрелами.|n"
        "- |cffa9c7deВерховный Рыцарь Крови|cffced4da: доблестный паладин Син'Дорай, владеющий исцеляющей волной и щитом света.|r"
    )
    checks_def.append({"type": "unit", "id": "h05J", "field": "name", "expected": wts_updates[17402]})
    checks_def.append({"type": "unit", "id": "h05J", "field": "tip", "expected": wts_updates[17403]})
    checks_def.append({"type": "unit", "id": "h05J", "field": "ubertip", "expected": wts_updates[7762]})

    # h04G: Мастерская (F)
    wts_updates[17262] = "|cffe4cfa3Мастерская|r"
    wts_updates[17263] = "|cffe4cfa3Мастерская|r (|cffffffffF|r)"
    wts_updates[6497] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Производит осадную технику, големов и элементалей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБаллиста|cffced4da: дальнобойное осадное орудие.|n"
        "- |cffa9c7deЭлементаль|cffced4da: магическое существо поддержки.|n"
        "- |cffa9c7deАрканитовый голем|cffced4da: несокрушимый страж ближнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПодпорки|cffced4da|n"
        "- |cffa9c7deАлгоритмы големов|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h04G", "field": "name", "expected": wts_updates[17262]})
    checks_def.append({"type": "unit", "id": "h04G", "field": "tip", "expected": wts_updates[17263]})
    checks_def.append({"type": "unit", "id": "h04G", "field": "ubertip", "expected": wts_updates[6497]})

    # h04E: Волшебное Святилище (D)
    wts_updates[17250] = "|cffe4cfa3Волшебное Святилище|r"
    wts_updates[17251] = "|cffe4cfa3Волшебное Святилище|r (|cffffffffD|r)"
    wts_updates[6495] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает заклинателей различных магических школ Эльфов Крови.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deВедьмак|cffced4da: элитный разрушитель чар, похищающий вражеские заклинания.|n"
        "- |cffa9c7deМагистр|cffced4da: повелитель стихии пламени.|n"
        "- |cffa9c7deАрканистка|cffced4da: чародейка Тайной магии.|n"
        "- |cffa9c7deЧернокнижник|cffced4da: мастер демонических искусств и порчи.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПосвящение магистров|cffced4da|n"
        "- |cffa9c7deПосвящение арканисток|cffced4da|n"
        "- |cffa9c7deПосвящение чернокнижников|cffced4da|n"
        "- |cffa9c7deМагический контроль|cffced4da|n"
        "- |cffa9c7deМагический страж|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h04E", "field": "name", "expected": wts_updates[17250]})
    checks_def.append({"type": "unit", "id": "h04E", "field": "tip", "expected": wts_updates[17251]})
    checks_def.append({"type": "unit", "id": "h04E", "field": "ubertip", "expected": wts_updates[6495]})

    # h04F: Хранилище Энергии (X)
    wts_updates[17387] = "|cffe4cfa3Хранилище Энергии|r"
    wts_updates[17388] = "|cffe4cfa3Хранилище Энергии|r (|cffffffffX|r)"
    wts_updates[6496] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Накапливает запасы маны для армии и определяет магическую специализацию Эльфов Крови (Аркана, Скверна, Бездна, Свет).|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМагическая повозка|cffced4da: мобильный источник маны для союзных войск.|n|n"
        "|cffa6afb8Исследования путей:|cffced4da|n- |cffa9c7deИзучение арканы|cffced4da: превращает в Колодец арканы.|n"
        "- |cffa9c7deИзучение скверны|cffced4da: превращает в Колодец скверны.|n"
        "- |cffa9c7deИзучение бездны|cffced4da: превращает в Колодец бездны.|n"
        "- |cffa9c7deИзучение света|cffced4da: превращает в Колодец света.|n"
        "- |cffa9c7deЕмкость хранилищ|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h04F", "field": "name", "expected": wts_updates[17387]})
    checks_def.append({"type": "unit", "id": "h04F", "field": "tip", "expected": wts_updates[17388]})
    checks_def.append({"type": "unit", "id": "h04F", "field": "ubertip", "expected": wts_updates[6496]})

    # =========================================================================
    # 3. UNITS (16 units)
    # =========================================================================
    # h04K: Строитель (Q)
    wts_updates[5713] = "|cffe4cfa3Строитель|r"
    wts_updates[28123] = "|cffe4cfa3Строитель|r (|cffffffffQ|r)"
    wts_updates[6526] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основной рабочий Эльфов Крови. Добывает золото и древесину, возводит и ремонтирует здания.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h04K", "field": "name", "expected": wts_updates[5713]})
    checks_def.append({"type": "unit", "id": "h04K", "field": "tip", "expected": wts_updates[28123]})
    checks_def.append({"type": "unit", "id": "h04K", "field": "ubertip", "expected": wts_updates[6526]})

    # h03V: Странник (Q)
    wts_updates[273] = "|cffe4cfa3Странник|r"
    wts_updates[274] = "|cffe4cfa3Странник|r (|cffffffffQ|r)"
    wts_updates[15322] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец ближнего боя. Может использовать ростовой щит для защиты от стрелковых атак.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da: снижает урон от атак дальнего боя.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h03V", "field": "name", "expected": wts_updates[273]})
    checks_def.append({"type": "unit", "id": "h03V", "field": "tip", "expected": wts_updates[274]})
    checks_def.append({"type": "unit", "id": "h03V", "field": "ubertip", "expected": wts_updates[15322]})

    # n00I: Следопыт (W)
    wts_updates[17375] = "|cffe4cfa3Следопыт|r"
    wts_updates[17376] = "|cffe4cfa3Следопыт|r (|cffffffffW|r)"
    wts_updates[15326] = (
        "|cffa6afb8ЮНИТ:|cffced4da Меткий эльфийский стрелок дальнего боя. Эффективен против пехоты и воздушных целей противника.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n00I", "field": "name", "expected": wts_updates[17375]})
    checks_def.append({"type": "unit", "id": "n00I", "field": "tip", "expected": wts_updates[17376]})
    checks_def.append({"type": "unit", "id": "n00I", "field": "ubertip", "expected": wts_updates[15326]})

    # h03X: Всадник (E)
    wts_updates[1362] = "|cffe4cfa3Всадник|r"
    wts_updates[1422] = "|cffe4cfa3Всадник|r (|cffffffffE|r)"
    wts_updates[16296] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый кавалерист ближнего боя. Идеален для стремительных атак и обхода противника с флангов.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h03X", "field": "name", "expected": wts_updates[1362]})
    checks_def.append({"type": "unit", "id": "h03X", "field": "tip", "expected": wts_updates[1422]})
    checks_def.append({"type": "unit", "id": "h03X", "field": "ubertip", "expected": wts_updates[16296]})

    # h03Y: Рыцарь крови (R)
    wts_updates[1440] = "|cffe4cfa3Рыцарь крови|r"
    wts_updates[9310] = "|cffe4cfa3Рыцарь крови|r (|cffffffffR|r)"
    wts_updates[16297] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжеловооружённый паладин ордена Син'Дорай. Обладает высоким запасом здоровья, тяжёлой бронёй и целительной магией.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолна исцеления|cffced4da: восстанавливает здоровье раненым союзникам.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h03Y", "field": "name", "expected": wts_updates[1440]})
    checks_def.append({"type": "unit", "id": "h03Y", "field": "tip", "expected": wts_updates[9310]})
    checks_def.append({"type": "unit", "id": "h03Y", "field": "ubertip", "expected": wts_updates[16297]})

    # e001: Баллиста (Q)
    wts_updates[16185] = "|cffe4cfa3Баллиста|r"
    wts_updates[20096] = "|cffe4cfa3Баллиста|r (|cffffffffQ|r)"
    wts_updates[35573] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойное осадное орудие. Наносит сокрушительный урон укреплениям и скоплениям вражеских войск.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПодпорки|cffced4da: закрепляется на позиции, увеличивая скорость стрельбы.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e001", "field": "name", "expected": wts_updates[16185]})
    checks_def.append({"type": "unit", "id": "e001", "field": "tip", "expected": wts_updates[20096]})
    checks_def.append({"type": "unit", "id": "e001", "field": "ubertip", "expected": wts_updates[35573]})

    # e030: Магическая повозка (A)
    wts_updates[20374] = "|cffe4cfa3Магическая повозка|r"
    wts_updates[20517] = "|cffe4cfa3Магическая повозка|r (|cffffffffA|r)"
    wts_updates[31822] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мобильный источник энергии. Непрерывно восполняет запас маны находящимся рядом союзным войскам.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВосполнение маны|cffced4da: передаёт запас маны союзникам.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e030", "field": "name", "expected": wts_updates[20374]})
    checks_def.append({"type": "unit", "id": "e030", "field": "tip", "expected": wts_updates[20517]})
    checks_def.append({"type": "unit", "id": "e030", "field": "ubertip", "expected": wts_updates[31822]})

    # h046: Элементаль (W)
    wts_updates[20331] = "|cffe4cfa3Элементаль|r"
    wts_updates[20332] = "|cffe4cfa3Элементаль|r (|cffffffffW|r)"
    wts_updates[37025] = (
        "|cffa6afb8ЮНИТ:|cffced4da Магическое существо поддержки. Использует защитные чары и выводит из строя башни врага.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deТуман|cffced4da: блокирует оборонительные строения противника.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h046", "field": "name", "expected": wts_updates[20331]})
    checks_def.append({"type": "unit", "id": "h046", "field": "tip", "expected": wts_updates[20332]})
    checks_def.append({"type": "unit", "id": "h046", "field": "ubertip", "expected": wts_updates[37025]})

    # h03Z: Арканитовый голем (E)
    wts_updates[9365] = "|cffe4cfa3Арканитовый голем|r"
    wts_updates[3197] = "|cffe4cfa3Арканитовый голем|r (|cffffffffE|r)"
    wts_updates[16298] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий механический страж ближнего боя. Обладает исключительной защитой и разрушительными ударами.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h03Z", "field": "name", "expected": wts_updates[9365]})
    checks_def.append({"type": "unit", "id": "h03Z", "field": "tip", "expected": wts_updates[3197]})
    checks_def.append({"type": "unit", "id": "h03Z", "field": "ubertip", "expected": wts_updates[16298]})

    # h03W: Ведьмак (R)
    wts_updates[17377] = "|cffe4cfa3Ведьмак|r"
    wts_updates[17378] = "|cffe4cfa3Ведьмак|r (|cffffffffR|r)"
    wts_updates[16289] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный боец ближнего боя, специализирующийся на нейтрализации вражеских заклинателей и подчинении призванных существ.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПохищение заклинаний|cffced4da: снимает положительные эффекты с врагов и рассеивает проклятия союзников.|n"
        "- |cffa9c7deМагический контроль|cffced4da: подчиняет вражеских призванных существ.|n"
        "- |cffa9c7deЗащита от магии|cffced4da: даёт иммунитет к вражеским заклинаниям.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h03W", "field": "name", "expected": wts_updates[17377]})
    checks_def.append({"type": "unit", "id": "h03W", "field": "tip", "expected": wts_updates[17378]})
    checks_def.append({"type": "unit", "id": "h03W", "field": "ubertip", "expected": wts_updates[16289]})

    # h040: Магистр (Q)
    wts_updates[12951] = "|cffe4cfa3Магистр|r"
    wts_updates[15529] = "|cffe4cfa3Магистр|r (|cffffffffQ|r)"
    wts_updates[16300] = (
        "|cffa6afb8ЮНИТ:|cffced4da Боевой маг школы Огня. Испепеляет противников огненными стрелами и накладывает воспламеняющие чары.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненная стрела|cffced4da: поражает врага огнём и кратковременно оглушает.|n"
        "- |cffa9c7deПоджигание|cffced4da: воспламеняет цель при атаках.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h040", "field": "name", "expected": wts_updates[12951]})
    checks_def.append({"type": "unit", "id": "h040", "field": "tip", "expected": wts_updates[15529]})
    checks_def.append({"type": "unit", "id": "h040", "field": "ubertip", "expected": wts_updates[16300]})

    # h041: Арканистка (W)
    wts_updates[15531] = "|cffe4cfa3Арканистка|r"
    wts_updates[15532] = "|cffe4cfa3Арканистка|r (|cffffffffW|r)"
    wts_updates[16301] = (
        "|cffa6afb8ЮНИТ:|cffced4da Заклинательница Тайной магии. Ослабляет противников искажениями времени и поражает чародейскими разрядами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЧародейская стрела|cffced4da: поражает врага арканой и замедляет его.|n"
        "- |cffa9c7deИскажение|cffced4da: замедляет скорость атаки цели при ударах.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h041", "field": "name", "expected": wts_updates[15531]})
    checks_def.append({"type": "unit", "id": "h041", "field": "tip", "expected": wts_updates[15532]})
    checks_def.append({"type": "unit", "id": "h041", "field": "ubertip", "expected": wts_updates[16301]})

    # h042: Чернокнижник (E)
    wts_updates[15533] = "|cffe4cfa3Чернокнижник|r"
    wts_updates[16140] = "|cffe4cfa3Чернокнижник|r (|cffffffffE|r)"
    wts_updates[21477] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мастер Скверны и тёмных искусств. Ослабляет броню врагов порчей и призывает демонических гончих.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСтрела скверны|cffced4da: снижает броню врага и оглушает его.|n"
        "- |cffa9c7deПорча|cffced4da: ослабляет защиту противника при атаках.|n"
        "- |cffa9c7deПризыв гончего|cffced4da: призывает демоническую гончую на поле боя.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h042", "field": "name", "expected": wts_updates[15533]})
    checks_def.append({"type": "unit", "id": "h042", "field": "tip", "expected": wts_updates[16140]})
    checks_def.append({"type": "unit", "id": "h042", "field": "ubertip", "expected": wts_updates[21477]})

    # n00O: Гончий
    wts_updates[39416] = "|cffe4cfa3Гончий|r"

    # h0BY: Арканитовый страж (E)
    wts_updates[20333] = "|cffe4cfa3Арканитовый страж|r"
    wts_updates[20341] = "|cffe4cfa3Арканитовый страж|r (|cffffffffE|r)"
    wts_updates[8396] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный призванный арканитовый защитник. Защищён магическим щитом и наносит сокрушительный урон типа хаос.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BY", "field": "name", "expected": wts_updates[20333]})
    checks_def.append({"type": "unit", "id": "h0BY", "field": "tip", "expected": wts_updates[20341]})
    checks_def.append({"type": "unit", "id": "h0BY", "field": "ubertip", "expected": wts_updates[8396]})

    # h0O6: Заступник Скверны (E)
    wts_updates[3189] = "|cffe4cfa3Заступник Скверны|r"
    wts_updates[9843] = "|cffe4cfa3Заступник Скверны|r (|cffffffffE|r)"
    wts_updates[42390] = (
        "|cffa6afb8ЮНИТ:|cffced4da Осквернённый исполин ближнего боя. Поражает нескольких врагов цепными молниями Скверны.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУдар скверны|cffced4da: поражает до трёх врагов цепной молнией.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0O6", "field": "name", "expected": wts_updates[3189]})
    checks_def.append({"type": "unit", "id": "h0O6", "field": "tip", "expected": wts_updates[9843]})
    checks_def.append({"type": "unit", "id": "h0O6", "field": "ubertip", "expected": wts_updates[42390]})

    # =========================================================================
    # 4. HEROES (7 heroes)
    # =========================================================================
    # H043: Маг Крови (A)
    wts_updates[4403] = "|cffe4cfa3Маг Крови|r"
    wts_updates[5839] = "|cffe4cfa3Маг Крови|r (|cffffffffA|r)"
    wts_updates[5011] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Верховный чародей Эльфов Крови, в совершенстве управляющий разрушительным пламенем и поглощающий магическую энергию врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненный столб|cffced4da: наносит урон огнём по площади в течение нескольких секунд.|n"
        "- |cffa9c7deИзгнание|cffced4da: перемещает цель в астральный план, делая её уязвимой к заклинаниям.|n"
        "- |cffa9c7deПохищение маны|cffced4da: вытягивает ману из противника или передаёт союзникам.|n"
        "- |cffa9c7deФеникс|cffced4da: призывает легендарную огненную птицу, перерождающуюся из яйца.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H043", "field": "name", "expected": wts_updates[4403]})
    checks_def.append({"type": "unit", "id": "H043", "field": "tip", "expected": wts_updates[5839]})
    checks_def.append({"type": "unit", "id": "H043", "field": "ubertip", "expected": wts_updates[5011]})

    # Hjnd: Ренджер (Q)
    wts_updates[262] = "|cffe4cfa3Ренджер|r"
    wts_updates[265] = "|cffe4cfa3Ренджер|r (|cffffffffQ|r)"
    wts_updates[848] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Искусный предводитель следопытов Кель'Таласа, усиливающий дальнобойных стрелков и поражающий множество целей зачарованными выстрелами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОтравленный кинжал|cffced4da: наносит урон ядом и замедляет противника.|n"
        "- |cffa9c7deЗачарованный лук|cffced4da: пассивно выпускает стрелы в дополнительные цели вокруг.|n"
        "- |cffa9c7deАура меткости|cffced4da: увеличивает урон от дальнобойных атак союзников.|n"
        "- |cffa9c7deМетка охотника|cffced4da: снижает броню врага и раскрывает его местоположение.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "Hjnd", "field": "name", "expected": wts_updates[262]})
    checks_def.append({"type": "unit", "id": "Hjnd", "field": "tip", "expected": wts_updates[265]})
    checks_def.append({"type": "unit", "id": "Hjnd", "field": "ubertip", "expected": wts_updates[848]})

    # H045: Верховный Рыцарь Крови (Z)
    wts_updates[5850] = "|cffe4cfa3Верховный Рыцарь Крови|r"
    wts_updates[5857] = "|cffe4cfa3Верховный Рыцарь Крови|r (|cffffffffZ|r)"
    wts_updates[6456] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Несокрушимый паладин ордена Рыцарей Крови, защищающий союзников щитами света и возвращающий к жизни павших воинов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВеер света|cffced4da: выпускает пучки света, поражая врагов вокруг героя.|n"
        "- |cffa9c7deЩит света|cffced4da: временно увеличивает показатель брони союзников.|n"
        "- |cffa9c7deСильный удар|cffced4da: даёт шанс оглушить врага и нанести дополнительный урон.|n"
        "- |cffa9c7deВоскрешение|cffced4da: возвращает к жизни павших союзных бойцов.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H045", "field": "name", "expected": wts_updates[5850]})
    checks_def.append({"type": "unit", "id": "H045", "field": "tip", "expected": wts_updates[5857]})
    checks_def.append({"type": "unit", "id": "H045", "field": "ubertip", "expected": wts_updates[6456]})

    # Capital Heroes:
    # H044: Верховный Магистр (Роммат) (Z)
    wts_updates[12430] = "|cffe4cfa3Верховный Магистр|r"
    wts_updates[12790] = "|cffe4cfa3Верховный Магистр|r (|cffffffffZ|r)"
    wts_updates[12795] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Верховный магистр Роммат — великий лидер магов Кель'Таласа, обрушивающий на врагов огненный ливень и призывающий несокрушимых арканитовых стражей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненная стрела|cffced4da: оглушающий огненный снаряд.|n"
        "- |cffa9c7deОгненный ливень|cffced4da: обрушивает волны всесожигающего пламени по площади.|n"
        "- |cffa9c7deАура Роммата|cffced4da: ускоряет регенерацию маны всех союзников.|n"
        "- |cffa9c7deАрканитовые Стражи|cffced4da: призывает мощных стражей с защитным щитом.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H044", "field": "name", "expected": wts_updates[12430]})
    checks_def.append({"type": "unit", "id": "H044", "field": "tip", "expected": wts_updates[12790]})
    checks_def.append({"type": "unit", "id": "H044", "field": "ubertip", "expected": wts_updates[12795]})

    # H05H: Матриарх Рыцарей Крови (Леди Лиадрин) (Z)
    wts_updates[26753] = "|cffe4cfa3Матриарх Рыцарей Крови|r"
    wts_updates[27339] = "|cffe4cfa3Матриарх Рыцарей Крови|r (|cffffffffZ|r)"
    wts_updates[9535] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Леди Лиадрин — матриарх ордена Рыцарей Крови, исцеляющая армию и карающая врагов священным сиянием Солнца.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолна исцеления|cffced4da: восстанавливает здоровье раненым войскам.|n"
        "- |cffa9c7deСолнечный удар|cffced4da: поражает врагов и исцеляет союзников в области.|n"
        "- |cffa9c7deАура Лиадрин|cffced4da: увеличивает скорость перемещения и регенерацию здоровья союзников.|n"
        "- |cffa9c7deВсепроникающий свет|cffced4da: многократно усиливает регенерацию союзников.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H05H", "field": "name", "expected": wts_updates[26753]})
    checks_def.append({"type": "unit", "id": "H05H", "field": "tip", "expected": wts_updates[27339]})
    checks_def.append({"type": "unit", "id": "H05H", "field": "ubertip", "expected": wts_updates[9535]})

    # H05I: Лорд-Регент (Лортемар Терон) (Z)
    wts_updates[13579] = "|cffe4cfa3Лорд-Регент|r"
    wts_updates[13581] = "|cffe4cfa3Лорд-Регент|r (|cffffffffZ|r)"
    wts_updates[5453] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Лортемар Терон — правящий лорд Кель'Таласа, непревзойдённый фехтовальщик и ветеран войн следопытов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВихрь клинков|cffced4da: смертоносный вихрь ударов, делающий героя невосприимчивым к магии.|n"
        "- |cffa9c7deСкачок|cffced4da: мгновенное перемещение на короткое расстояние.|n"
        "- |cffa9c7deКритический удар|cffced4da: шанс нанести многократный урон при атаке.|n"
        "- |cffa9c7deАнтимагическая броня|cffced4da: временно даёт высокую защиту от физических атак и заклинаний.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H05I", "field": "name", "expected": wts_updates[13579]})
    checks_def.append({"type": "unit", "id": "H05I", "field": "tip", "expected": wts_updates[13581]})
    checks_def.append({"type": "unit", "id": "H05I", "field": "ubertip", "expected": wts_updates[5453]})

    # Hkal: Принц Эльфов Крови (Кель'тас) (Z)
    wts_updates[257] = "|cffe4cfa3Принц Эльфов Крови|r"
    wts_updates[261] = "|cffe4cfa3Принц Эльфов Крови|r (|cffffffffZ|r)"
    wts_updates[19438] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Кель'тас Солнечный Скиталец — законный принц Кель'Таласа и верховный маг, повелевающий легендарным фениксом Ал'Аром и гигантскими огненными глыбами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненный столб|cffced4da: мощный огненный столб по области.|n"
        "- |cffa9c7deПоле астрала|cffced4da: перемещает всех юнитов в указанной области в астральный план.|n"
        "- |cffa9c7deУгольки|cffced4da: ракетный обстрел, оглушающий наземных врагов.|n"
        "- |cffa9c7deАл'Ар|cffced4da: призывает бессмертного феникса Ал'Ара.|n"
        "- |cffa9c7deОгромная огненная глыба|cffced4da: сокрушительный шар пламени, наносящий колоссальный урон.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "Hkal", "field": "name", "expected": wts_updates[257]})
    checks_def.append({"type": "unit", "id": "Hkal", "field": "tip", "expected": wts_updates[261]})
    checks_def.append({"type": "unit", "id": "Hkal", "field": "ubertip", "expected": wts_updates[19438]})

    # Propernames fixes for heroes:
    # 5616 (Hjnd propernames: Вериса Песнь Солнца, Адорис Тень Луны, ...) -> keep clean
    # 11338 (H045 propernames: Кельтиел Правдивый, Дар'Тел Искупитель, Тассариан Бесстрашный)
    # 3700 (H044 propername: Роммат)
    # 3702 (H05H propername: Леди Лиадрин)
    wts_updates[3702] = "Леди Лиадрин"
    # 3703 (H05I propername: Лортемар Терон)
    wts_updates[3703] = "Лортемар Терон"

    # =========================================================================
    # 5. RESEARCHES (33 researches)
    # =========================================================================
    # R01N: Улучшенная кладка (W)
    wts_updates[6113] = "|cffe4cfa3Улучшенная кладка|r"
    wts_updates[38384] = "|cffe4cfa3Улучшенная кладка|r (|cffffffffW|r)"
    wts_updates[3095] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает прочность и показатель брони всех зданий Эльфов Крови.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Все здания Эльфов Крови.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01N", "field": "name1", "expected": wts_updates[6113]})
    checks_def.append({"type": "upgrade", "id": "R01N", "field": "tip1", "expected": wts_updates[38384]})
    checks_def.append({"type": "upgrade", "id": "R01N", "field": "ubertip1", "expected": wts_updates[3095]})

    # R01K: Оружие дальнего боя (W)
    wts_updates[38361] = "|cffe4cfa3Оружие дальнего боя|r"
    wts_updates[38364] = "|cffe4cfa3Оружие дальнего боя|r (|cffffffffW|r)"
    wts_updates[3020] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон немагических дальнобойных войск Эльфов Крови.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСледопыт|cffced4da|n- |cffa9c7deБаллиста|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01K", "field": "name1", "expected": wts_updates[38361]})
    checks_def.append({"type": "upgrade", "id": "R01K", "field": "tip1", "expected": wts_updates[38364]})
    checks_def.append({"type": "upgrade", "id": "R01K", "field": "ubertip1", "expected": wts_updates[3020]})

    # R01L: Тяжелая броня (A)
    wts_updates[33784] = "|cffe4cfa3Тяжелая броня|r"
    wts_updates[40577] = "|cffe4cfa3Тяжелая броня|r (|cffffffffA|r)"
    wts_updates[3050] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает показатель брони воинов ближнего боя, кавалерии и ведьмаков.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтранник|cffced4da|n- |cffa9c7deВсадник|cffced4da|n"
        "- |cffa9c7deРыцарь крови|cffced4da|n- |cffa9c7deВедьмак|cffced4da|n- |cffa9c7deАрканитовый голем|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01L", "field": "name1", "expected": wts_updates[33784]})
    checks_def.append({"type": "upgrade", "id": "R01L", "field": "tip1", "expected": wts_updates[40577]})
    checks_def.append({"type": "upgrade", "id": "R01L", "field": "ubertip1", "expected": wts_updates[3050]})

    # R01M: Легкая броня (S)
    wts_updates[33785] = "|cffe4cfa3Легкая броня|r"
    wts_updates[38373] = "|cffe4cfa3Легкая броня|r (|cffffffffS|r)"
    wts_updates[3068] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает показатель брони стрелков, заклинателей и вспомогательных войск.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСледопыт|cffced4da|n- |cffa9c7deБаллиста|cffced4da|n"
        "- |cffa9c7deМагистр|cffced4da|n- |cffa9c7deАрканистка|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da|n"
        "- |cffa9c7deЭлементаль|cffced4da|n- |cffa9c7deМагическая повозка|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01M", "field": "name1", "expected": wts_updates[33785]})
    checks_def.append({"type": "upgrade", "id": "R01M", "field": "tip1", "expected": wts_updates[38373]})
    checks_def.append({"type": "upgrade", "id": "R01M", "field": "ubertip1", "expected": wts_updates[3068]})

    # R01R: Артефакты (E)
    wts_updates[33786] = "|cffe4cfa3Артефакты|r"
    wts_updates[38385] = "|cffe4cfa3Артефакты|r (|cffffffffE|r)"
    wts_updates[3202] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает магическую мощь и увеличивает урон атак заклинателей Эльфов Крови.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагистр|cffced4da|n- |cffa9c7deАрканистка|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01R", "field": "name1", "expected": wts_updates[33786]})
    checks_def.append({"type": "upgrade", "id": "R01R", "field": "tip1", "expected": wts_updates[38385]})
    checks_def.append({"type": "upgrade", "id": "R01R", "field": "ubertip1", "expected": wts_updates[3202]})

    # R01J: Оружие ближнего боя (Q)
    wts_updates[38349] = "|cffe4cfa3Оружие ближнего боя|r"
    wts_updates[38355] = "|cffe4cfa3Оружие ближнего боя|r (|cffffffffQ|r)"
    wts_updates[2980] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает силу атаки всех воинов ближнего боя Эльфов Крови.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтранник|cffced4da|n- |cffa9c7deВсадник|cffced4da|n"
        "- |cffa9c7deРыцарь крови|cffced4da|n- |cffa9c7deАрканитовый голем|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01J", "field": "name1", "expected": wts_updates[38349]})
    checks_def.append({"type": "upgrade", "id": "R01J", "field": "tip1", "expected": wts_updates[38355]})
    checks_def.append({"type": "upgrade", "id": "R01J", "field": "ubertip1", "expected": wts_updates[2980]})

    # R03I: Стационарный магический источник (A)
    wts_updates[42350] = "|cffe4cfa3Стационарный магический источник|r"
    wts_updates[42351] = "|cffe4cfa3Стационарный магический источник|r (|cffffffffA|r)"
    wts_updates[42352] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Ускоряет регенерацию маны в Хранилищах Энергии и Колодцах.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранилище Энергии|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03I", "field": "name1", "expected": wts_updates[42350]})
    checks_def.append({"type": "upgrade", "id": "R03I", "field": "tip1", "expected": wts_updates[42351]})
    checks_def.append({"type": "upgrade", "id": "R03I", "field": "ubertip1", "expected": wts_updates[42352]})

    # R03J: Мобильные магические источники (S)
    wts_updates[42262] = "|cffe4cfa3Мобильные магические источники|r"
    wts_updates[42263] = "|cffe4cfa3Мобильные магические источники|r (|cffffffffS|r)"
    wts_updates[5447] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость регенерации маны всех войск Эльфов Крови на |cffffffff0.05|cffced4da ед./сек.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Все войска Эльфов Крови.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03J", "field": "name1", "expected": wts_updates[42262]})
    checks_def.append({"type": "upgrade", "id": "R03J", "field": "tip1", "expected": wts_updates[42263]})
    checks_def.append({"type": "upgrade", "id": "R03J", "field": "ubertip1", "expected": wts_updates[5447]})

    # R01T: Улучшенные инструменты (Q)
    wts_updates[30796] = "|cffe4cfa3Улучшенные инструменты|r"
    wts_updates[19307] = "|cffe4cfa3Улучшенные инструменты|r (|cffffffffQ|r)"
    wts_updates[5090] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой строителями древесины на |cffffffff5|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01T", "field": "name1", "expected": wts_updates[30796]})
    checks_def.append({"type": "upgrade", "id": "R01T", "field": "tip1", "expected": wts_updates[19307]})
    checks_def.append({"type": "upgrade", "id": "R01T", "field": "ubertip1", "expected": wts_updates[5090]})

    # R03E: Магическая выносливость (X)
    wts_updates[42275] = "|cffe4cfa3Магическая выносливость|r"
    wts_updates[42278] = "|cffe4cfa3Магическая выносливость|r (|cffffffffX|r)"
    wts_updates[38408] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас маны всех войск на |cffffffff10%|cffced4da, но снижает регенерацию маны на |cffe69a8d0.05|cffced4da ед./сек.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Все войска Эльфов Крови.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03E", "field": "name1", "expected": wts_updates[42275]})
    checks_def.append({"type": "upgrade", "id": "R03E", "field": "tip1", "expected": wts_updates[42278]})
    checks_def.append({"type": "upgrade", "id": "R03E", "field": "ubertip1", "expected": wts_updates[38408]})

    # R03F: Магическая сила (Z)
    wts_updates[38224] = "|cffe4cfa3Магическая сила|r"
    wts_updates[38414] = "|cffe4cfa3Магическая сила|r (|cffffffffZ|r)"
    wts_updates[38420] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Ускоряет регенерацию маны войск на |cffffffff0.1|cffced4da ед./сек., но снижает максимальный запас маны на |cffe69a8d5%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Все войска Эльфов Крови.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03F", "field": "name1", "expected": wts_updates[38224]})
    checks_def.append({"type": "upgrade", "id": "R03F", "field": "tip1", "expected": wts_updates[38414]})
    checks_def.append({"type": "upgrade", "id": "R03F", "field": "ubertip1", "expected": wts_updates[38420]})

    # R01Y: Улучшенные луки (S)
    wts_updates[27326] = "|cffe4cfa3Улучшенные луки|r"
    wts_updates[27325] = "|cffe4cfa3Улучшенные луки|r (|cffffffffS|r)"
    wts_updates[3584] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает дальность стрельбы следопытов.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСледопыт|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01Y", "field": "name1", "expected": wts_updates[27326]})
    checks_def.append({"type": "upgrade", "id": "R01Y", "field": "tip1", "expected": wts_updates[27325]})
    checks_def.append({"type": "upgrade", "id": "R01Y", "field": "ubertip1", "expected": wts_updates[3584]})

    # R01X: Защита от магии (A)
    wts_updates[34865] = "|cffe4cfa3Защита от магии|r"
    wts_updates[35115] = "|cffe4cfa3Защита от магии|r (|cffffffffA|r)"
    wts_updates[35116] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует странникам и ведьмакам способность «Защита от магии», делающую их невосприимчивыми к заклинаниям.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтранник|cffced4da|n- |cffa9c7deВедьмак|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01X", "field": "name1", "expected": wts_updates[34865]})
    checks_def.append({"type": "upgrade", "id": "R01X", "field": "tip1", "expected": wts_updates[35115]})
    checks_def.append({"type": "upgrade", "id": "R01X", "field": "ubertip1", "expected": wts_updates[35116]})

    # R01W: Тренировка следопытов (X)
    wts_updates[40520] = "|cffe4cfa3Тренировка следопытов|r"
    wts_updates[19292] = "|cffe4cfa3Тренировка следопытов|r (|cffffffffX|r)"
    wts_updates[42348] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон следопытов на |cffffffff3|cffced4da ед. и увеличивает их максимальный запас здоровья на |cffffffff60|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСледопыт|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01W", "field": "name1", "expected": wts_updates[40520]})
    checks_def.append({"type": "upgrade", "id": "R01W", "field": "tip1", "expected": wts_updates[19292]})
    checks_def.append({"type": "upgrade", "id": "R01W", "field": "ubertip1", "expected": wts_updates[42348]})

    # R0BU: Магический страж (X)
    wts_updates[38429] = "|cffe4cfa3Магический страж|r"
    wts_updates[33776] = "|cffe4cfa3Магический страж|r (|cffffffffX|r)"
    wts_updates[16454] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет защитные башни способностью обнаруживать невидимых врагов.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДозорная Башня|cffced4da|n- |cffa9c7deСторожевая Башня|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0BU", "field": "name1", "expected": wts_updates[38429]})
    checks_def.append({"type": "upgrade", "id": "R0BU", "field": "tip1", "expected": wts_updates[33776]})
    checks_def.append({"type": "upgrade", "id": "R0BU", "field": "ubertip1", "expected": wts_updates[16454]})

    # R01O: Посвящение магистров (A)
    wts_updates[9654] = "|cffe4cfa3Посвящение магистров|r"
    wts_updates[5731] = "|cffe4cfa3Посвящение магистров|r (|cffffffffA|r)"
    wts_updates[41634] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, запас маны и скорость регенерации маны магистров.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагистр|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01O", "field": "name1", "expected": wts_updates[9654]})
    checks_def.append({"type": "upgrade", "id": "R01O", "field": "tip1", "expected": wts_updates[5731]})
    checks_def.append({"type": "upgrade", "id": "R01O", "field": "ubertip1", "expected": wts_updates[41634]})

    # R01P: Посвящение арканисток (S)
    wts_updates[9703] = "|cffe4cfa3Посвящение арканисток|r"
    wts_updates[6097] = "|cffe4cfa3Посвящение арканисток|r (|cffffffffS|r)"
    wts_updates[41831] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, запас маны и скорость регенерации маны арканисток.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАрканистка|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01P", "field": "name1", "expected": wts_updates[9703]})
    checks_def.append({"type": "upgrade", "id": "R01P", "field": "tip1", "expected": wts_updates[6097]})
    checks_def.append({"type": "upgrade", "id": "R01P", "field": "ubertip1", "expected": wts_updates[41831]})

    # R01Q: Посвящение чернокнижников (D)
    wts_updates[19446] = "|cffe4cfa3Посвящение чернокнижников|r"
    wts_updates[9710] = "|cffe4cfa3Посвящение чернокнижников|r (|cffffffffD|r)"
    wts_updates[42230] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, запас маны и скорость регенерации маны чернокнижников.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01Q", "field": "name1", "expected": wts_updates[19446]})
    checks_def.append({"type": "upgrade", "id": "R01Q", "field": "tip1", "expected": wts_updates[9710]})
    checks_def.append({"type": "upgrade", "id": "R01Q", "field": "ubertip1", "expected": wts_updates[42230]})

    # R01S: Магический контроль (C)
    wts_updates[30685] = "|cffe4cfa3Магический контроль|r"
    wts_updates[30688] = "|cffe4cfa3Магический контроль|r (|cffffffffC|r)"
    wts_updates[30795] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает ведьмаков способности «Магический контроль», позволяющей подчинять вражеских призванных существ.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВедьмак|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01S", "field": "name1", "expected": wts_updates[30685]})
    checks_def.append({"type": "upgrade", "id": "R01S", "field": "tip1", "expected": wts_updates[30688]})
    checks_def.append({"type": "upgrade", "id": "R01S", "field": "ubertip1", "expected": wts_updates[30795]})

    # Prioritets:
    # R025: Приоритет на Ведьмаках (X)
    wts_updates[32577] = "|cffe4cfa3Приоритет на Ведьмаках|r"
    wts_updates[33764] = "|cffe4cfa3Приоритет на Ведьмаках|r (|cffffffffX|r)"
    wts_updates[38199] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает боевые способности ведьмаков, уменьшая их уязвимость к физическому урону.|n|n"
        "|cffe69a8dОтменяет другие выбранные приоритеты!|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВедьмак|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R025", "field": "name1", "expected": wts_updates[32577]})
    checks_def.append({"type": "upgrade", "id": "R025", "field": "tip1", "expected": wts_updates[33764]})
    checks_def.append({"type": "upgrade", "id": "R025", "field": "ubertip1", "expected": wts_updates[38199]})

    # R026: Приоритет на Рыцарях крови (C)
    wts_updates[33772] = "|cffe4cfa3Приоритет на Рыцарях крови|r"
    wts_updates[33773] = "|cffe4cfa3Приоритет на Рыцарях крови|r (|cffffffffC|r)"
    wts_updates[38202] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет рыцарей крови способностью «Огненное лассо», сковывающей противника.|n|n"
        "|cffe69a8dОтменяет другие выбранные приоритеты!|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРыцарь крови|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R026", "field": "name1", "expected": wts_updates[33772]})
    checks_def.append({"type": "upgrade", "id": "R026", "field": "tip1", "expected": wts_updates[33773]})
    checks_def.append({"type": "upgrade", "id": "R026", "field": "ubertip1", "expected": wts_updates[38202]})

    # R03C: Приоритет на Странниках и Следопытах (Z)
    wts_updates[38203] = "|cffe4cfa3Приоритет на Странниках и Следопытах|r"
    wts_updates[38204] = "|cffe4cfa3Приоритет на Странниках и Следопытах|r (|cffffffffZ|r)"
    wts_updates[38205] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает странников и следопытов, даруя им огненные стрелы и защитные ауры.|n|n"
        "|cffe69a8dОтменяет другие выбранные приоритеты!|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтранник|cffced4da|n- |cffa9c7deСледопыт|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03C", "field": "name1", "expected": wts_updates[38203]})
    checks_def.append({"type": "upgrade", "id": "R03C", "field": "tip1", "expected": wts_updates[38204]})
    checks_def.append({"type": "upgrade", "id": "R03C", "field": "ubertip1", "expected": wts_updates[38205]})

    # R03D: Приоритет на Анклаве магов (Z)
    wts_updates[33774] = "|cffe4cfa3Приоритет на Анклаве магов|r"
    wts_updates[33775] = "|cffe4cfa3Приоритет на Анклаве магов|r (|cffffffffZ|r)"
    wts_updates[38208] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает магические стрелы магов и увеличивает скорость регенерации маны заклинателей.|n|n"
        "|cffe69a8dОтменяет другие выбранные приоритеты!|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагистр|cffced4da|n- |cffa9c7deАрканистка|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03D", "field": "name1", "expected": wts_updates[33774]})
    checks_def.append({"type": "upgrade", "id": "R03D", "field": "tip1", "expected": wts_updates[33775]})
    checks_def.append({"type": "upgrade", "id": "R03D", "field": "ubertip1", "expected": wts_updates[38208]})

    # R03N: Алгоритмы големов (C)
    wts_updates[33742] = "|cffe4cfa3Алгоритмы големов|r"
    wts_updates[33745] = "|cffe4cfa3Алгоритмы големов|r (|cffffffffC|r)"
    wts_updates[33748] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки големов на |cffffffff15%|cffced4da, но снижает регенерацию маны на |cffe69a8d1|cffced4da ед./сек.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАрканитовый голем|cffced4da|n- |cffa9c7deАрканитовый страж|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03N", "field": "name1", "expected": wts_updates[33742]})
    checks_def.append({"type": "upgrade", "id": "R03N", "field": "tip1", "expected": wts_updates[33745]})
    checks_def.append({"type": "upgrade", "id": "R03N", "field": "ubertip1", "expected": wts_updates[33748]})

    # R021: Подпорки (Z)
    wts_updates[38394] = "|cffe4cfa3Подпорки|r"
    wts_updates[38395] = "|cffe4cfa3Подпорки|r (|cffffffffZ|r)"
    wts_updates[20182] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет баллистам закрепляться на боевой позиции, увеличивая скорость стрельбы.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deБаллиста|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R021", "field": "name1", "expected": wts_updates[38394]})
    checks_def.append({"type": "upgrade", "id": "R021", "field": "tip1", "expected": wts_updates[38395]})
    checks_def.append({"type": "upgrade", "id": "R021", "field": "ubertip1", "expected": wts_updates[20182]})

    # R03Q: Гонка Вооружений (Q)
    wts_updates[33678] = "|cffe4cfa3Гонка Вооружений|r"
    wts_updates[33723] = "|cffe4cfa3Гонка Вооружений|r (|cffffffffQ|r)"

    # Rhcd: Туман (X)
    wts_updates[20181] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует элементалям способность «Туман», выводящую из строя оборонительные башни врага.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЭлементаль|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "Rhcd", "field": "ubertip1", "expected": wts_updates[20181]})

    # 4 Paths (Хранилище Энергии):
    # R03R: Емкость хранилищ (X)
    wts_updates[33763] = "|cffe4cfa3Емкость хранилищ|r"
    wts_updates[38426] = "|cffe4cfa3Емкость хранилищ|r (|cffffffffX|r)"
    wts_updates[33751] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас маны Хранилищ Энергии на |cffffffff1000|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранилище Энергии|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R03R", "field": "name1", "expected": wts_updates[33763]})
    checks_def.append({"type": "upgrade", "id": "R03R", "field": "tip1", "expected": wts_updates[38426]})
    checks_def.append({"type": "upgrade", "id": "R03R", "field": "ubertip1", "expected": wts_updates[33751]})

    # R01D: Изучение арканы (Q)
    wts_updates[3875] = "|cffe4cfa3Изучение арканы|r"
    wts_updates[5334] = "|cffe4cfa3Изучение арканы|r (|cffffffffQ|r)"
    wts_updates[5384] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Посвящает фракцию школе Тайной магии. Превращает Хранилища Энергии в Колодцы арканы и увеличивает максимальный запас маны големов, ведьмаков, магистров и арканисток.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранилище Энергии|cffced4da|n"
        "- Заклинатели и големы Эльфов Крови.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01D", "field": "name1", "expected": wts_updates[3875]})
    checks_def.append({"type": "upgrade", "id": "R01D", "field": "tip1", "expected": wts_updates[5334]})
    checks_def.append({"type": "upgrade", "id": "R01D", "field": "ubertip1", "expected": wts_updates[5384]})

    # R01G: Изучение скверны (W)
    wts_updates[5461] = "|cffe4cfa3Изучение скверны|r"
    wts_updates[5467] = "|cffe4cfa3Изучение скверны|r (|cffffffffW|r)"
    wts_updates[5471] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Посвящает фракцию магии Скверны. Превращает Хранилища Энергии в Колодцы скверны, открывает доступ к Заступникам Скверны и увеличивает запас маны чернокнижников.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранилище Энергии|cffced4da|n"
        "- |cffa9c7deЧернокнижник|cffced4da|n- |cffa9c7deЗаступник Скверны|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01G", "field": "name1", "expected": wts_updates[5461]})
    checks_def.append({"type": "upgrade", "id": "R01G", "field": "tip1", "expected": wts_updates[5467]})
    checks_def.append({"type": "upgrade", "id": "R01G", "field": "ubertip1", "expected": wts_updates[5471]})

    # R01H: Изучение бездны (R)
    wts_updates[5539] = "|cffe4cfa3Изучение бездны|r"
    wts_updates[5633] = "|cffe4cfa3Изучение бездны|r (|cffffffffR|r)"
    wts_updates[5649] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Посвящает фракцию магии Бездны. Превращает Хранилища Энергии в Колодцы бездны и увеличивает максимальный запас маны элементалей.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранилище Энергии|cffced4da|n- |cffa9c7deЭлементаль|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01H", "field": "name1", "expected": wts_updates[5539]})
    checks_def.append({"type": "upgrade", "id": "R01H", "field": "tip1", "expected": wts_updates[5633]})
    checks_def.append({"type": "upgrade", "id": "R01H", "field": "ubertip1", "expected": wts_updates[5649]})

    # R01I: Изучение света (E)
    wts_updates[5660] = "|cffe4cfa3Изучение света|r"
    wts_updates[5665] = "|cffe4cfa3Изучение света|r (|cffffffffE|r)"
    wts_updates[6031] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Посвящает фракцию магии Света. Превращает Хранилища Энергии в Колодцы света, увеличивает запас здоровья, маны и регенерацию рыцарей крови.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранилище Энергии|cffced4da|n- |cffa9c7deРыцарь крови|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R01I", "field": "name1", "expected": wts_updates[5660]})
    checks_def.append({"type": "upgrade", "id": "R01I", "field": "tip1", "expected": wts_updates[5665]})
    checks_def.append({"type": "upgrade", "id": "R01I", "field": "ubertip1", "expected": wts_updates[6031]})

    # Dummies: R01E, R01F, R020
    wts_updates[38347] = "|cffe4cfa3Аркана Колодцев|r"
    wts_updates[2808] = "|cffe4cfa3Аркана Колодцев|r"
    wts_updates[2817] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебное улучшение Колодцев арканы.|r"

    wts_updates[38348] = "|cffe4cfa3Аркана Големов|r"
    wts_updates[2831] = "|cffe4cfa3Аркана Големов|r"
    wts_updates[2840] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебное улучшение Арканитовых големов.|r"

    wts_updates[35342] = "|cffe4cfa3Тьма Элементалей|r"
    wts_updates[36378] = "|cffe4cfa3Тьма Элементалей|r"
    wts_updates[3683] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебное улучшение темных элементалей.|r"

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # AHfs: Огненный столб (Kael'thas)
    wts_updates[5617] = "|cffe4cfa3Огненный столб|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)"
    wts_updates[1441] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным войскам в области |cffffffff150|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., "
        "а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # AHdr: Похищение маны
    wts_updates[5619] = "|cffe4cfa3Похищение маны|r [|cffffffff4-й уровень|r] (|cffffffffE|r)"
    wts_updates[5620] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает |cffffffff60|cffced4da ед. маны/сек. из вражеского юнита или передаёт её союзнику.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )
    wts_updates[32062] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт магический канал, вытягивающий ману из вражеского юнита или передающий собственную ману союзнику.|n|n"
        "|cffa6afb8Уровни:|cffced4da|n"
        "- |cffffffff1|cffced4da: |cffffffff15|cffced4da маны/сек.|n"
        "- |cffffffff2|cffced4da: |cffffffff30|cffced4da маны/сек.|n"
        "- |cffffffff3|cffced4da: |cffffffff45|cffced4da маны/сек.|n"
        "- |cffffffff4|cffced4da: |cffffffff60|cffced4da маны/сек.|r"
    )

    # AHpx: Феникс
    wts_updates[16143] = "|cffe4cfa3Феникс|r"
    wts_updates[16142] = "|cffe4cfa3Феникс|r (|cffffffffR|r)"
    wts_updates[16144] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает могучего огненного феникса, обладающего иммунитетом к магии и огненной аурой. "
        "После гибели феникс превращается в яйцо и перерождается.|r"
    )
    wts_updates[5623] = "|cffe4cfa3Феникс|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
    wts_updates[5624] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da могучих огненных фениксов, обладающих иммунитетом к магии и огненной аурой.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # AHbn: Изгнание
    wts_updates[25760] = "|cffe4cfa3Изгнание|r"
    wts_updates[25761] = "|cffe4cfa3Изгнание|r (|cffffffffW|r)"
    wts_updates[25762] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Изгоняет выбранную цель в астральный план. Изгнанная цель замедляется, теряет способность атаковать, "
        "но получает значительно больше урона от магии и заклинаний.|r"
    )
    wts_updates[5621] = "|cffe4cfa3Изгнание|r [|cffffffff4-й уровень|r] (|cffffffffW|r)"
    wts_updates[5622] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Изгоняет цель в астральный план на |cffffffff5|cffced4da сек.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # A08R: Поле астрала (Kael'thas trigger spell)
    wts_updates[38033] = "|cffe4cfa3Поле астрала|r"
    wts_updates[38037] = "|cffe4cfa3Поле астрала|r (|cffffffffW|r)"
    wts_updates[6083] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Перемещает всех бойцов в указанной области в астральный план, делая их уязвимыми к магии.|r"
    wts_updates[38032] = "|cffe4cfa3Поле астрала — уровень 1|r (|cffffffffW|r)"
    wts_updates[6074] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех бойцов в области в астральный план на короткое время.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[38034] = "|cffe4cfa3Поле астрала — уровень 2|r (|cffffffffW|r)"
    wts_updates[6079] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех бойцов в области в астральный план на умеренное время.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38035] = "|cffe4cfa3Поле астрала — уровень 3|r (|cffffffffW|r)"
    wts_updates[6080] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех бойцов в области в астральный план на длительное время.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38036] = "|cffe4cfa3Поле астрала — уровень 4|r (|cffffffffW|r)"
    wts_updates[6081] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех бойцов в области в астральный план на максимальное время.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A07U: Зачарованный лук (Hjnd passive)
    wts_updates[38000] = "|cffe4cfa3Зачарованный лук|r"
    wts_updates[38006] = "|cffe4cfa3Зачарованный лук|r"
    wts_updates[38005] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая стрелковая атака дополнительно поражает случайные цели рядом с основной.|r"
    wts_updates[37996] = "|cffe4cfa3Зачарованный лук — уровень 1|r"
    wts_updates[2601] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелы в дополнительные цели рядом.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[37997] = "|cffe4cfa3Зачарованный лук — уровень 2|r"
    wts_updates[2605] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелы в дополнительные цели рядом с повышенным уроном.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[37998] = "|cffe4cfa3Зачарованный лук — уровень 3|r"
    wts_updates[2606] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелы в дополнительные цели рядом со значительным уроном.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[37999] = "|cffe4cfa3Зачарованный лук — уровень 4|r"
    wts_updates[10695] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелы в дополнительные цели рядом с максимальным уроном.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0LQ: Отравленный кинжал (Hjnd Q)
    wts_updates[40570] = "|cffe4cfa3Отравленный кинжал|r"
    wts_updates[40571] = "|cffe4cfa3Отравленный кинжал|r (|cffffffffQ|r)"
    wts_updates[40572] = "|cffe4cfa3Отравленный кинжал — уровень 1|r (|cffffffffQ|r)"
    wts_updates[40573] = "|cffe4cfa3Отравленный кинжал — уровень 2|r (|cffffffffQ|r)"
    wts_updates[40574] = "|cffe4cfa3Отравленный кинжал — уровень 3|r (|cffffffffQ|r)"
    wts_updates[40575] = "|cffe4cfa3Отравленный кинжал — уровень 4|r (|cffffffffQ|r)"

    # AEar: Аура меткости
    wts_updates[4964] = "|cffe4cfa3Аура меткости — уровень 4|r"
    wts_updates[4967] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон от дальнобойных атак находящихся рядом союзников на |cffffffff40%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A07V: Метка охотника (Hjnd R)
    wts_updates[38010] = "|cffe4cfa3Метка охотника|r"
    wts_updates[38012] = "|cffe4cfa3Метка охотника|r (|cffffffffR|r)"
    wts_updates[6023] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ослабляет броню выбранного врага и раскрывает его местоположение на длительное время.|r"
    wts_updates[38007] = "|cffe4cfa3Метка охотника — уровень 1|r (|cffffffffR|r)"
    wts_updates[38008] = "|cffe4cfa3Метка охотника — уровень 2|r (|cffffffffR|r)"
    wts_updates[5640] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ослабляет броню врага на |cffe69a8d10|cffced4da ед. и раскрывает его местоположение на |cffffffff120|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A16M / A0DD: Доспехи ведьмака / Антимагическая броня (H05I / Hjnd)
    wts_updates[38129] = "|cffe4cfa3Антимагическая броня|r"
    wts_updates[27687] = "|cffe4cfa3Антимагическая броня|r (|cffffffffR|r)"
    wts_updates[27689] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Временно дарует владельцу высокую броню и полную невосприимчивость к магии.|r"
    wts_updates[38130] = "|cffe4cfa3Антимагическая броня — уровень 1|r (|cffffffffR|r)"
    wts_updates[27688] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует повышенную защиту и невосприимчивость к магии на |cffffffff20|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[38131] = "|cffe4cfa3Антимагическая броня — уровень 2|r (|cffffffffR|r)"
    wts_updates[27692] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует максимальную защиту и невосприимчивость к магии на |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    wts_updates[38065] = "|cffe4cfa3Доспехи ведьмака|r"
    wts_updates[9730] = "|cffe4cfa3Доспехи ведьмака|r"
    wts_updates[9651] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню и даёт полную защиту от вражеских заклинаний.|r"
    wts_updates[38061] = "|cffe4cfa3Доспехи ведьмака — уровень 1|r"
    wts_updates[38063] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт временную броню и защиту от магии.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[38062] = "|cffe4cfa3Доспехи ведьмака — уровень 2|r"
    wts_updates[38064] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт мощную броню и полную защиту от магии.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A08H: Веер света (H045 Q)
    wts_updates[40564] = "|cffe4cfa3Веер света|r"
    wts_updates[40565] = "|cffe4cfa3Веер света|r (|cffffffffQ|r)"
    wts_updates[6011] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну сияющих лезвий света, наносящих урон всем врагам вокруг паладина.|r"
    wts_updates[40566] = "|cffe4cfa3Веер света — уровень 1|r (|cffffffffQ|r)"
    wts_updates[6016] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff75|cffced4da ед. урона находящимся рядом врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[40567] = "|cffe4cfa3Веер света — уровень 2|r (|cffffffffQ|r)"
    wts_updates[6017] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff125|cffced4da ед. урона находящимся рядом врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[40568] = "|cffe4cfa3Веер света — уровень 3|r (|cffffffffQ|r)"
    wts_updates[6018] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff190|cffced4da ед. урона находящимся рядом врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[40569] = "|cffe4cfa3Веер света — уровень 4|r (|cffffffffQ|r)"
    wts_updates[6019] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff260|cffced4da ед. урона находящимся рядом врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A07W: Щит света (H045 W)
    wts_updates[38020] = "|cffe4cfa3Щит света|r"
    wts_updates[38021] = "|cffe4cfa3Щит света|r (|cffffffffW|r)"
    wts_updates[6028] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзников благословенным сиянием, временно увеличивая их защиту на |cffffffff15|cffced4da сек.|r"
    wts_updates[3064] = "|cffe4cfa3Щит света — уровень 1|r (|cffffffffW|r)"
    wts_updates[5650] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников на |cffc8e087+2|cffced4da ед. на |cffffffff15|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[38013] = "|cffe4cfa3Щит света — уровень 2|r (|cffffffffW|r)"
    wts_updates[6024] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников на |cffc8e087+4|cffced4da ед. на |cffffffff15|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38014] = "|cffe4cfa3Щит света — уровень 3|r (|cffffffffW|r)"
    wts_updates[6025] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников на |cffc8e087+6|cffced4da ед. на |cffffffff15|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38015] = "|cffe4cfa3Щит света — уровень 4|r (|cffffffffW|r)"
    wts_updates[6026] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников на |cffc8e087+8|cffced4da ед. на |cffffffff15|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A1LX: Сильный удар (H045 Passive)
    wts_updates[39045] = "|cffe4cfa3Сильный удар|r"
    wts_updates[39044] = "|cffe4cfa3Сильный удар|r"
    wts_updates[39041] = "|cffe4cfa3Сильный удар — уровень 1|r"
    wts_updates[39042] = "|cffe4cfa3Сильный удар — уровень 2|r"
    wts_updates[39038] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff20%|cffced4da атака нанесёт дополнительный урон и оглушит цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[39043] = "|cffe4cfa3Сильный удар — уровень 3|r"
    wts_updates[39039] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff25%|cffced4da атака нанесёт дополнительный урон и оглушит цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[39037] = "|cffe4cfa3Сильный удар — уровень 4|r"
    wts_updates[39040] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff30%|cffced4da атака нанесёт дополнительный урон и оглушит цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    wts_updates[29445] = "|cffe4cfa3Сильный удар — уровень 4|r"
    wts_updates[29446] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff20%|cffced4da атака нанесёт дополнительный урон и оглушит цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[29447] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff25%|cffced4da атака нанесёт дополнительный урон и оглушит цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[29448] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff30%|cffced4da атака нанесёт дополнительный урон и оглушит цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # AHre: Воскрешение (H045 R)
    wts_updates[173] = "|cffe4cfa3Воскрешение — уровень 2|r (|cffffffffR|r)"
    wts_updates[182] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни до |cffffffff12|cffced4da находящихся рядом союзных бойцов.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A1KU: Всепроникающий свет (H05H R)
    wts_updates[38473] = "|cffe4cfa3Всепроникающий свет|r"
    wts_updates[38647] = "|cffe4cfa3Всепроникающий свет|r (|cffffffffR|r)"
    wts_updates[38648] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da На |cffffffff15|cffced4da сек. колоссально увеличивает регенерацию здоровья союзных войск в области.|r"
    wts_updates[38645] = "|cffe4cfa3Всепроникающий свет — уровень 1|r (|cffffffffR|r)"
    wts_updates[38646] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da На |cffffffff15|cffced4da сек. значительно повышает регенерацию союзников в области.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[38649] = "|cffe4cfa3Всепроникающий свет — уровень 2|r (|cffffffffR|r)"
    wts_updates[38650] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da На |cffffffff15|cffced4da сек. колоссально повышает регенерацию союзников в области.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A1KV: Лиадрин ульта dummy
    wts_updates[24377] = "|cffe4cfa3Всепроникающий свет|r"

    # A1KY: Свет небес дамми
    wts_updates[38675] = "|cffe4cfa3Свет небес|r"

    # A05J / Asps: Похищение заклинаний (Spellbreaker Q/W)
    wts_updates[37896] = "|cffe4cfa3Похищение заклинаний|r"
    wts_updates[37897] = "|cffe4cfa3Похищение заклинаний|r (|cffffffffQ|r)"
    wts_updates[16062] = "|cffe4cfa3Похищение заклинаний|r"
    wts_updates[16064] = "|cffe4cfa3Похищение заклинаний|r (|cffffffffW|r)"

    # A05K / A049: Магический контроль (Spellbreaker X)
    wts_updates[37898] = "|cffe4cfa3Магический контроль|r"
    wts_updates[37899] = "|cffe4cfa3Магический контроль|r (|cffffffffX|r)"
    wts_updates[37900] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подчиняет вражеское призванное существо. Требует |cffffffff45%|cffced4da от текущего здоровья цели.|r"
    wts_updates[36829] = "|cffe4cfa3Магический контроль|r"
    wts_updates[36830] = "|cffe4cfa3Магический контроль|r (|cffffffffX|r)"
    wts_updates[36831] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подчиняет вражеское призванное существо. Требует |cffffffff45%|cffced4da от текущего здоровья цели.|r"

    # A07L / A037 / A1KW: Волна исцеления
    wts_updates[37983] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[36828] = "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)"
    wts_updates[37984] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает волну целительной энергии, последовательно восстанавливающую здоровье до |cffffffff8|cffced4da союзников.|r"

    wts_updates[36798] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[35539] = "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)"
    wts_updates[259] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает волну целительной энергии, последовательно восстанавливающую здоровье до |cffffffff6|cffced4da союзников.|r"

    wts_updates[37985] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[37830] = "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)"
    wts_updates[36614] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт волну энергии, восстанавливающую здоровье союзных войск.|n|n"
        "|cffa6afb8Уровни:|cffced4da|n"
        "- |cffffffff1|cffced4da: |cffc8e087130|cffced4da ед. здоровья, до |cffffffff3|cffced4da целей.|n"
        "- |cffffffff2|cffced4da: |cffc8e087215|cffced4da ед. здоровья, до |cffffffff5|cffced4da целей.|n"
        "- |cffffffff3|cffced4da: |cffc8e087300|cffced4da ед. здоровья, до |cffffffff8|cffced4da целей.|n"
        "- |cffffffff4|cffced4da: |cffc8e087385|cffced4da ед. здоровья, до |cffffffff20|cffced4da целей.|r"
    )
    wts_updates[35540] = "|cffe4cfa3Волна исцеления — уровень 1|r (|cffffffffQ|r)"
    wts_updates[36615] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087130|cffced4da ед. здоровья выбранной цели и переходит на союзников рядом.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[35541] = "|cffe4cfa3Волна исцеления — уровень 2|r (|cffffffffQ|r)"
    wts_updates[36659] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087215|cffced4da ед. здоровья выбранной цели и переходит на союзников рядом.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[36988] = "|cffe4cfa3Волна исцеления — уровень 3|r (|cffffffffQ|r)"
    wts_updates[36660] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087300|cffced4da ед. здоровья выбранной цели и переходит на союзников рядом.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[24378] = "|cffe4cfa3Волна исцеления — уровень 4|r (|cffffffffQ|r)"
    wts_updates[36613] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087385|cffced4da ед. здоровья выбранной цели и переходит на союзников рядом.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A07K: Огненное лассо (R026)
    wts_updates[37981] = "|cffe4cfa3Огненное лассо|r"
    wts_updates[37982] = "|cffe4cfa3Огненное лассо|r (|cffffffffW|r)"
    wts_updates[5380] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывает цель огненными путами, лишая её возможности двигаться и атаковать.|r"

    # A07P / A07Q / A02J / A00W: Огненная стрела
    wts_updates[25643] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[33619] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[5504] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня, наносящий урон, кратковременно оглушающий цель и поджигающий её на |cffffffff9|cffced4da сек.|r"

    wts_updates[33673] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[33679] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[5510] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня, наносящий урон, оглушающий цель и накладывающий поджигание.|r"

    wts_updates[20501] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[20502] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[2259] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня, оглушающий цель и поджигающий её на |cffffffff9|cffced4da сек.|r"

    wts_updates[19732] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[20498] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[2273] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток пламени, оглушающий цель и наносящий урон от огня.|r"

    # A07N / A07O / A030 / A02Z: Стрела скверны
    wts_updates[33739] = "|cffe4cfa3Стрела скверны|r"
    wts_updates[33738] = "|cffe4cfa3Стрела скверны|r (|cffffffffQ|r)"
    wts_updates[5484] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток демонической Скверны, оглушающий цель и снижающий её показатель брони.|r"

    wts_updates[33740] = "|cffe4cfa3Стрела скверны|r"
    wts_updates[33741] = "|cffe4cfa3Стрела скверны|r (|cffffffffQ|r)"
    wts_updates[5492] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток демонической Скверны, оглушающий цель и снижающий показатель брони врагов.|r"

    wts_updates[33734] = "|cffe4cfa3Стрела скверны|r"
    wts_updates[33733] = "|cffe4cfa3Стрела скверны|r (|cffffffffQ|r)"
    wts_updates[2345] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком Скверны, кратковременно оглушая её и снижая показатель брони.|r"

    wts_updates[33731] = "|cffe4cfa3Стрела скверны|r"
    wts_updates[33732] = "|cffe4cfa3Стрела скверны|r (|cffffffffQ|r)"
    wts_updates[2336] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком Скверны, оглушая её и ослабляя показатель брони.|r"

    # A02G / A07D / A02R / A02U: Чародейская стрела
    wts_updates[37989] = "|cffe4cfa3Чародейская стрела|r"
    wts_updates[37988] = "|cffe4cfa3Чародейская стрела|r (|cffffffffQ|r)"
    wts_updates[5464] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток арканы, наносящий урон, оглушающий цель и замедляющий её скорость атаки.|r"

    wts_updates[37990] = "|cffe4cfa3Чародейская стрела|r"
    wts_updates[37991] = "|cffe4cfa3Чародейская стрела|r (|cffffffffQ|r)"
    wts_updates[5472] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток арканы, наносящий урон, оглушающий цель и снижающий скорость её атаки.|r"

    wts_updates[32700] = "|cffe4cfa3Чародейская стрела|r"
    wts_updates[32699] = "|cffe4cfa3Чародейская стрела|r (|cffffffffQ|r)"
    wts_updates[2280] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель разрядом Тайной магии, кратковременно оглушая её и замедляя скорость атаки.|r"

    wts_updates[32705] = "|cffe4cfa3Чародейская стрела|r"
    wts_updates[32706] = "|cffe4cfa3Чародейская стрела|r (|cffffffffQ|r)"
    wts_updates[2298] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель разрядом Тайной магии, оглушая её и замедляя скорость атаки.|r"

    # A07M: Укрыться (E)
    wts_updates[37986] = "|cffe4cfa3Укрыться|r"
    wts_updates[37987] = "|cffe4cfa3Укрыться|r (|cffffffffE|r)"
    wts_updates[5386] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует невидимость, но снижает скорость перемещения вдвое. Первая атака из невидимости наносит повышенный урон.|r"

    # A07S / A07R: Неуловимый щит (D)
    wts_updates[37992] = "|cffe4cfa3Неуловимый щит|r"
    wts_updates[37993] = "|cffe4cfa3Неуловимый щит|r (|cffffffffD|r)"
    wts_updates[33680] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт энергетический щит, поглощающий |cffffffff75%|cffced4da получаемого урона за счёт расхода маны.|r"

    wts_updates[3019] = "|cffe4cfa3Неуловимый щит|r"
    wts_updates[3062] = "|cffe4cfa3Неуловимый щит|r (|cffffffffD|r)"
    wts_updates[22333] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт энергетический щит, поглощающий |cffffffff45%|cffced4da получаемого урона за счёт расхода маны.|r"

    # A07T: Огненные стрелы
    wts_updates[2179] = "|cffe4cfa3Огненные стрелы|r (|cffffffffQ|r)"
    wts_updates[2178] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffc8e087+10|cffced4da ед. урона от огня к каждой стрелковой атаке. Расходует |cffffffff10|cffced4da ед. маны за выстрел.|r"

    # A02D: Передача маны
    wts_updates[32692] = "|cffe4cfa3Передача маны|r"
    wts_updates[32693] = "|cffe4cfa3Передача маны|r (|cffffffffN|r)"
    wts_updates[32694] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает |cffffffff15|cffced4da ед. маны/сек. из вражеского юнита или передаёт её союзнику.|r"

    # A02E: Восполнение маны
    wts_updates[32695] = "|cffe4cfa3Восполнение маны|r"
    wts_updates[32696] = "|cffe4cfa3Восполнение маны|r (|cffffffffZ|r)"

    # A02N: Поджигание
    wts_updates[38118] = "|cffe4cfa3Поджигание|r"
    wts_updates[38117] = "|cffe4cfa3Поджигание|r"
    wts_updates[2234] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff10%|cffced4da атака воспламенит противника на |cffffffff10|cffced4da сек., нанося урон огнём.|r"

    # A02S / A02T: Искажение
    wts_updates[2487] = "|cffe4cfa3Искажение|r"
    wts_updates[2486] = "|cffe4cfa3Искажение|r"
    wts_updates[20057] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff10%|cffced4da атака исказит время вокруг цели, снизив её скорость атаки на |cffe69a8d10%|cffced4da.|r"

    wts_updates[32701] = "|cffe4cfa3Искажение|r"
    wts_updates[2289] = "|cffe4cfa3Искажение|r"
    wts_updates[5727] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает скорость атаки цели на |cffe69a8d15%|cffced4da.|r"

    # A02X: Порча
    wts_updates[2834] = "|cffe4cfa3Порча|r"
    wts_updates[2811] = "|cffe4cfa3Порча|r"
    wts_updates[2321] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff10%|cffced4da атака поразит цель порчей, снизив показатель её брони на |cffe69a8d2|cffced4da ед.|r"

    # A02Y: Кровавый союз
    wts_updates[2988] = "|cffe4cfa3Кровавый союз|r"
    wts_updates[2987] = "|cffe4cfa3Кровавый союз|r (|cffffffffW|r)"
    wts_updates[27538] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает максимальный запас здоровья выбранного союзника на |cffc8e087130|cffced4da ед.|r"

    # A032: Призыв гончего
    wts_updates[38024] = "|cffe4cfa3Призыв гончего|r"
    wts_updates[38023] = "|cffe4cfa3Призыв гончего|r (|cffffffffE|r)"
    wts_updates[789] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на поле боя демоническую гончую на |cffffffff3|cffced4da мин. для терзания врагов.|r"

    # A035: Сфера разрушения
    wts_updates[36797] = "|cffe4cfa3Сфера разрушения|r"
    wts_updates[40560] = "|cffe4cfa3Сфера разрушения|r (|cffffffffQ|r)"
    wts_updates[39034] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет |cffc8e087+20|cffced4da к урону от атак. Атаки начинают поражать цели по площади.|r"

    # A0SY: Магический страж
    wts_updates[38109] = "|cffe4cfa3Магический страж|r"
    wts_updates[38110] = "|cffe4cfa3Магический страж|r"

    # A1LW: Удар скверны (Заступник Скверны W)
    wts_updates[3201] = "|cffe4cfa3Удар скверны|r"
    wts_updates[36886] = "|cffe4cfa3Удар скверны|r (|cffffffffW|r)"
    wts_updates[38963] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает до |cffffffff3|cffced4da врагов перед собой цепной молнией Скверны, нанося |cffffffff35|cffced4da ед. урона.|r"

    # Dummy stat abilities:
    wts_updates[31861] = "|cffe4cfa3Бонус к здоровью|r"
    wts_updates[32104] = "|cffe4cfa3Бонус к скорости атаки|r"
    wts_updates[32193] = "|cffe4cfa3Бонус к броне|r"

    # Rommath abilities:
    # A0DJ: Арканитовые Стражи
    wts_updates[38106] = "|cffe4cfa3Арканитовые Стражи|r"
    wts_updates[38103] = "|cffe4cfa3Арканитовые Стражи|r (|cffffffffR|r)"
    wts_updates[9720] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на поле боя могучих арканитовых стражей с высоким здоровьем и магическим щитом.|n|n"
        "|cffa6afb8Уровни:|cffced4da|n"
        "- |cffffffff1|cffced4da: призывает стража с высоким запасом здоровья.|n"
        "- |cffffffff2|cffced4da: призывает двух стражей со способностью «Бешенство».|r"
    )
    wts_updates[38104] = "|cffe4cfa3Арканитовые Стражи — уровень 1|r (|cffffffffR|r)"
    wts_updates[26719] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает арканитового стража с высоким здоровьем и защитным щитом.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[38105] = "|cffe4cfa3Арканитовые Стражи — уровень 2|r (|cffffffffR|r)"
    wts_updates[26720] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает двух арканитовых стражей с высоким здоровьем и способностью «Бешенство».|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A0DI: Огненная стрела (Rommath Q)
    wts_updates[38100] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[38102] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[25609] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня во врага, нанося урон и кратковременно оглушая его.|r"
    wts_updates[38101] = "|cffe4cfa3Огненная стрела — уровень 1|r (|cffffffffQ|r)"
    wts_updates[38097] = "|cffe4cfa3Огненная стрела — уровень 2|r (|cffffffffQ|r)"
    wts_updates[6574] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня, наносящий |cffffffff100|cffced4da ед. урона и оглушающий цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38098] = "|cffe4cfa3Огненная стрела — уровень 3|r (|cffffffffQ|r)"
    wts_updates[6575] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня, наносящий |cffffffff150|cffced4da ед. урона и оглушающий цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38099] = "|cffe4cfa3Огненная стрела — уровень 4|r (|cffffffffQ|r)"
    wts_updates[6576] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня, наносящий |cffffffff200|cffced4da ед. урона и оглушающий цель.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A15O: Огненный ливень (Rommath W)
    wts_updates[38124] = "|cffe4cfa3Огненный ливень|r"
    wts_updates[38125] = "|cffe4cfa3Огненный ливень|r (|cffffffffW|r)"
    wts_updates[38126] = "|cffe4cfa3Огненный ливень — уровень 1|r (|cffffffffW|r)"
    wts_updates[38127] = "|cffe4cfa3Огненный ливень — уровень 2|r (|cffffffffW|r)"
    wts_updates[38128] = "|cffe4cfa3Огненный ливень — уровень 3|r (|cffffffffW|r)"
    wts_updates[38123] = "|cffe4cfa3Огненный ливень — уровень 4|r (|cffffffffW|r)"
    wts_updates[26722] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область волны огня, наносящие периодический урон всем противникам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0DH: Аура Роммата (Rommath E)
    wts_updates[3066] = "|cffe4cfa3Аура Роммата|r"
    wts_updates[38096] = "|cffe4cfa3Аура Роммата|r"
    wts_updates[7477] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Постоянная аура магистра, ускоряющая восстановление маны всех союзников поблизости.|r"
    wts_updates[38092] = "|cffe4cfa3Аура Роммата — уровень 1|r"
    wts_updates[38093] = "|cffe4cfa3Аура Роммата — уровень 2|r"
    wts_updates[38094] = "|cffe4cfa3Аура Роммата — уровень 3|r"
    wts_updates[38095] = "|cffe4cfa3Аура Роммата — уровень 4|r"
    wts_updates[6589] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию маны находящихся рядом союзников на |cffc8e087+2.0|cffced4da ед./сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0DE: Аура Лиадрин (Liadrin E)
    wts_updates[38066] = "|cffe4cfa3Аура Лиадрин|r"
    wts_updates[38067] = "|cffe4cfa3Аура Лиадрин|r"
    wts_updates[38068] = "|cffe4cfa3Аура Лиадрин — уровень 1|r"
    wts_updates[38072] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения союзников на |cffc8e087+10%|cffced4da и ускоряет регенерацию здоровья.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[38069] = "|cffe4cfa3Аура Лиадрин — уровень 2|r"
    wts_updates[38073] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения союзников на |cffc8e087+15%|cffced4da и ускоряет регенерацию здоровья.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38070] = "|cffe4cfa3Аура Лиадрин — уровень 3|r"
    wts_updates[38074] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения союзников на |cffc8e087+20%|cffced4da и ускоряет регенерацию здоровья.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38071] = "|cffe4cfa3Аура Лиадрин — уровень 4|r"
    wts_updates[38075] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения союзников на |cffc8e087+25%|cffced4da и ускоряет регенерацию здоровья.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A1KX: Солнечный удар (Liadrin W)
    wts_updates[38665] = "|cffe4cfa3Солнечный удар|r"
    wts_updates[38673] = "|cffe4cfa3Солнечный удар|r (|cffffffffW|r)"
    wts_updates[38674] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает поток солнечной энергии в указанную область, нанося урон врагам и исцеляя союзников.|r"
    wts_updates[38663] = "|cffe4cfa3Солнечный удар — уровень 1|r (|cffffffffW|r)"
    wts_updates[38664] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff80|cffced4da ед. урона врагам и восстанавливает |cffc8e08780|cffced4da ед. здоровья союзникам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[38667] = "|cffe4cfa3Солнечный удар — уровень 2|r (|cffffffffW|r)"
    wts_updates[38670] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff140|cffced4da ед. урона врагам и восстанавливает |cffc8e087140|cffced4da ед. здоровья союзникам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38668] = "|cffe4cfa3Солнечный удар — уровень 3|r (|cffffffffW|r)"
    wts_updates[38671] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff200|cffced4da ед. урона врагам и восстанавливает |cffc8e087200|cffced4da ед. здоровья союзникам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38669] = "|cffe4cfa3Солнечный удар — уровень 4|r (|cffffffffW|r)"
    wts_updates[38672] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff260|cffced4da ед. урона врагам и восстанавливает |cffc8e087260|cffced4da ед. здоровья союзникам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0DC: Критический удар (Lor'themar E)
    wts_updates[38056] = "|cffe4cfa3Критический удар|r"
    wts_updates[38057] = "|cffe4cfa3Критический удар|r"
    wts_updates[38058] = "|cffe4cfa3Критический удар — уровень 1|r"
    wts_updates[27681] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff15%|cffced4da шанс нанести двойной урон при атаке.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[38059] = "|cffe4cfa3Критический удар — уровень 2|r"
    wts_updates[27682] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff15%|cffced4da шанс нанести тройной урон при атаке.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38060] = "|cffe4cfa3Критический удар — уровень 3|r"
    wts_updates[27683] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff15%|cffced4da шанс нанести четырёхкратный урон при атаке.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38055] = "|cffe4cfa3Критический удар — уровень 4|r"
    wts_updates[27680] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff15%|cffced4da шанс нанести пятикратный урон при атаке.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # AEbl: Скачок (Lor'themar W)
    wts_updates[25764] = "|cffe4cfa3Скачок|r"
    wts_updates[25765] = "|cffe4cfa3Скачок|r (|cffffffffW|r)"
    wts_updates[25763] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает героя на короткое расстояние, позволяя быстро вступить в бой или выйти из окружения.|r"
    wts_updates[9615] = "|cffe4cfa3Скачок — уровень 4|r (|cffffffffW|r)"
    wts_updates[9616] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает героя на короткое расстояние. Перезарядка: |cffffffff1|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0DB: Вихрь клинков (Lor'themar Q)
    wts_updates[7248] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает Лортемара смертоносным вихрем ударов, делающим его невосприимчивым к магии и наносящим высокий урон окружающим врагам.|r"
    wts_updates[9618] = "|cffe4cfa3Вихрь клинков — уровень 2|r (|cffffffffQ|r)"
    wts_updates[27677] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff140|cffced4da ед. урона/сек. врагам вокруг и дарует невосприимчивость к магии.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[9619] = "|cffe4cfa3Вихрь клинков — уровень 3|r (|cffffffffQ|r)"
    wts_updates[27678] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff180|cffced4da ед. урона/сек. врагам вокруг и дарует невосприимчивость к магии.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[23515] = "|cffe4cfa3Вихрь клинков — уровень 4|r (|cffffffffQ|r)"
    wts_updates[27679] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff220|cffced4da ед. урона/сек. врагам вокруг и дарует невосприимчивость к магии.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    wts_updates[27676] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff110|cffced4da ед. урона/сек. врагам вокруг и дарует невосприимчивость к магии.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"

    # A08Q: Огненный столб (Kael'thas Hkal Q)
    wts_updates[38027] = "|cffe4cfa3Огненный столб|r"
    wts_updates[38028] = "|cffe4cfa3Огненный столб|r (|cffffffffQ|r)"
    wts_updates[38029] = "|cffe4cfa3Огненный столб — уровень 1|r (|cffffffffQ|r)"
    wts_updates[6070] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff45|cffced4da ед. урона/сек. в первые |cffffffff3|cffced4da сек., затем малый урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[38030] = "|cffe4cfa3Огненный столб — уровень 2|r (|cffffffffQ|r)"
    wts_updates[6071] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff80|cffced4da ед. урона/сек. в первые |cffffffff3|cffced4da сек., затем малый урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38031] = "|cffe4cfa3Огненный столб — уровень 3|r (|cffffffffQ|r)"
    wts_updates[6072] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff110|cffced4da ед. урона/сек. в первые |cffffffff3|cffced4da сек., затем малый урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38026] = "|cffe4cfa3Огненный столб — уровень 4|r (|cffffffffQ|r)"
    wts_updates[6068] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff150|cffced4da ед. урона/сек. в первые |cffffffff3|cffced4da сек., затем малый урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A08V: Угольки (Kael'thas Hkal E)
    wts_updates[38053] = "|cffe4cfa3Угольки|r"
    wts_updates[38047] = "|cffe4cfa3Угольки|r (|cffffffffE|r)"
    wts_updates[38048] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область огненными угольками, нанося урон и оглушая наземных врагов.|r"
    wts_updates[38049] = "|cffe4cfa3Угольки — уровень 1|r (|cffffffffE|r)"
    wts_updates[38050] = "|cffe4cfa3Угольки — уровень 2|r (|cffffffffE|r)"
    wts_updates[6100] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит до |cffffffff55|cffced4da ед. урона и оглушает врагов в области.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38051] = "|cffe4cfa3Угольки — уровень 3|r (|cffffffffE|r)"
    wts_updates[6101] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит до |cffffffff70|cffced4da ед. урона и оглушает врагов в области.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38052] = "|cffe4cfa3Угольки — уровень 4|r (|cffffffffE|r)"
    wts_updates[6102] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит до |cffffffff90|cffced4da ед. урона и оглушает врагов в области.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A08S: Ал'Ар (Kael'thas Hkal R)
    wts_updates[38039] = "|cffe4cfa3Ал'Ар|r"
    wts_updates[38040] = "|cffe4cfa3Ал'Ар|r (|cffffffffR|r)"
    wts_updates[38041] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает легендарного феникса Ал'Ара, наносящего урон огнём вокруг себя. "
        "Ал'Ар обладает иммунитетом к магии, а в момент гибели оставляет яйцо, из которого возрождается вновь.|r"
    )
    wts_updates[39429] = "|cffe4cfa3Ал'Ар|r (|cffffffffR|r)"
    wts_updates[38042] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает легендарного феникса Ал'Ара, наносящего урон огнём вокруг себя. "
        "Ал'Ар невосприимчив к магии и возрождается из яйца после гибели.|r"
    )

    # A08U: Огромная огненная глыба (Kael'thas Hkal D)
    wts_updates[38044] = "|cffe4cfa3Огромная огненная глыба|r"
    wts_updates[38045] = "|cffe4cfa3Огромная огненная глыба|r (|cffffffffD|r)"
    wts_updates[6116] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает гигантский шар пламени, наносящий колоссальный урон и оглушающий цель при попадании.|r"
    wts_updates[38046] = "|cffe4cfa3Огромная огненная глыба|r (|cffffffffD|r)"
    wts_updates[6093] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает огромный огненный шар, наносящий высокий урон и оглушающий цель.|r"

    # =========================================================================
    # STYLE VALIDATION
    # =========================================================================
    forbidden_prefixes = [
        "Построить ", "Обучить ", "Нанять ", "Призвать ", "Исследовать ", "Улучшить до "
    ]
    style_violations = []
    color_tag_re = re.compile(r"\|c[0-9a-fA-F]{8}")

    for sid, val in wts_updates.items():
        # 1. Color tag reset check
        has_color = bool(color_tag_re.search(val))
        has_reset = "|r" in val
        if has_color and not has_reset:
            style_violations.append(f"STRING {sid}: opened color tag without any |r reset: {repr(val)}")

        # 2. Malformed hex
        malformed = re.findall(r"\|c[^f\r\n]{1,7}[^0-9a-fA-F]", val)
        if malformed:
            style_violations.append(f"STRING {sid}: potential malformed color tag: {malformed}")

        # 3. Trailing newline
        if val.endswith("|n") or val.endswith("\n") or val.endswith("\r"):
            style_violations.append(f"STRING {sid}: ends with newline: {repr(val[-10:])}")

        # 4. Forbidden command prefixes
        for verb in forbidden_prefixes:
            if verb in val:
                style_violations.append(f"STRING {sid}: contains forbidden command verb '{verb}': {val[:40]}")

    if style_violations:
        print("Style violations found:")
        for sv in style_violations:
            print("  ", sv)
        raise ValueError("Style check failed!")
    print(f"All style invariants passed 100%! Checked {len(wts_updates)} strings.")

    # Save plan JSON
    plan_data = {
        "race": "BloodElves",
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A0HQ"],
            "markers": ["R07C", "R0L0"],
            "buildings": [
                "h04C", "h04B", "h04A", "h04M", "h04D", "h04N", "h04O", "h04P",
                "h04Q", "h04R", "h05J", "h04G", "h04E", "h04F"
            ],
            "units": [
                "h04K", "h03V", "n00I", "h03X", "h03Y", "e001", "e030",
                "h046", "h03Z", "h03W", "h040", "h041", "h042",
                "n00O", "h0BY", "h0O6"
            ],
            "heroes": ["H043", "Hjnd", "H045", "H044", "H05H", "H05I", "Hkal"],
            "upgrades": [
                "R01N", "R01K", "R01L", "R01M", "R01R", "R01J", "R03I", "R03J",
                "R01T", "R03E", "R03F", "R03K", "R01Y", "R01X", "R01W", "R0BU",
                "R01O", "R01P", "R01Q", "R01S", "R025", "R026", "R03C", "R03D",
                "R03N", "R021", "R03Q", "Rhcd", "R03R", "R01H", "R01I", "R01G", "R01D"
            ],
            "abilities": [
                "AHfs", "AHdr", "AHpx", "AHbn", "A08R", "A07U", "A0LQ", "AEar",
                "A07V", "A16M", "A0DD", "A08H", "A07W", "A1LX", "AHre", "A1KU",
                "A05J", "Asps", "A05K", "A049", "A07L", "A037", "A1KW", "A07K",
                "A07P", "A07Q", "A02J", "A00W", "A07N", "A07O", "A030", "A02Z",
                "A02G", "A07D", "A02R", "A02U", "A07M", "A07S", "A07R", "A07T",
                "A02D", "A02E", "A02N", "A02S", "A02T", "A02X", "A02Y", "A032",
                "A035", "A0SY", "A1LW", "A0DJ", "A0DI", "A15O", "A0DH", "A0DE",
                "A1KX", "A0DC", "AEbl", "A0DB", "A08Q", "A08V", "A08S", "A08U"
            ]
        }
    }

    out_file = folder / "blood_elves_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {out_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

if __name__ == "__main__":
    main()
