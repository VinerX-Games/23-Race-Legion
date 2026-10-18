# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Twilight Hammer race (Race 20).

Outputs:
- docs/ui_text/twilight_hammer_plan.json
"""
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
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
    # 1. RACE SELECTION & TECH MARKERS: A0HX, R07K, R0KD
    # =========================================================================
    wts_updates[38881] = "|cffe4cfa3Культ Сумеречного Молота|r"
    wts_updates[38882] = "|cffe4cfa3Культ Сумеречного Молота|r (|cffffffffX|r)"
    wts_updates[35196] = (
        "|cffa6afb8РАСА:|cffced4da Зловещая апокалиптическая организация слуг Древних Богов, стремящаяся повергнуть Азерот в хаос и забвение.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Cataclysm»|r|n|n"
        "|cffced4daКульт Сумеречного Молота — фанатичная организация, объединившая выживших орков клана Сумеречного Молота, огров под предводительством двухголового мага Чо'Галла, а также сектантов самых разных рас Азерота. Поклоняясь Бездне и Древним Богам, культисты фанатично приближают конец времён. Их армия сочетает яростных рубак и огров, жрецов Бездны, гигантских мутировавших аберраций и осквернённых драконов Пустоты, черпающих тёмную мощь из всепоглощающего фанатизма.|r"
    )

    checks_def.append({"type": "ability", "id": "A0HX", "field": "name", "expected": wts_updates[38881]})
    checks_def.append({"type": "ability", "id": "A0HX", "field": "tip1", "expected": wts_updates[38882]})
    checks_def.append({"type": "ability", "id": "A0HX", "field": "ubertip1", "expected": wts_updates[35196]})

    # Selection markers: R07K, R0KD
    wts_updates[10670] = "|cffe4cfa3Культ Сумеречного Молота|r"
    wts_updates[10671] = "|cffe4cfa3Культ Сумеречного Молота|r"
    wts_updates[20118] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Культу Сумеречного Молота.|r"

    checks_def.append({"type": "upgrade", "id": "R07K", "field": "name1", "expected": wts_updates[10670]})
    checks_def.append({"type": "upgrade", "id": "R07K", "field": "tip1", "expected": wts_updates[10671]})
    checks_def.append({"type": "upgrade", "id": "R07K", "field": "ubertip1", "expected": wts_updates[20118]})

    wts_updates[5598] = "|cffe4cfa3Культ Сумеречного Молота|r"
    wts_updates[5599] = "|cffe4cfa3Культ Сумеречного Молота|r"
    wts_updates[37033] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер выбора ветви развития Культа Сумеречного Молота.|r"

    checks_def.append({"type": "upgrade", "id": "R0KD", "field": "name1", "expected": wts_updates[5598]})
    checks_def.append({"type": "upgrade", "id": "R0KD", "field": "tip1", "expected": wts_updates[5599]})
    checks_def.append({"type": "upgrade", "id": "R0KD", "field": "ubertip1", "expected": wts_updates[37033]})

    # =========================================================================
    # 2. BUILDINGS (9 buildings)
    # =========================================================================
    # o00K: Бастион Сумеречного Молота (Q)
    wts_updates[6718] = "|cffe4cfa3Бастион Сумеречного Молота|r"
    wts_updates[6719] = "|cffe4cfa3Бастион Сумеречного Молота|r (|cffffffffQ|r)"
    wts_updates[12989] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное святилище Культа Сумеречного Молота. Обучает батраков, исследует уровни «Фанатизма» и служит складом ресурсов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБатрак|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deФанатизм|cffced4da.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "o00K", "field": "name", "expected": wts_updates[6718]})
    checks_def.append({"type": "unit", "id": "o00K", "field": "tip", "expected": wts_updates[6719]})
    checks_def.append({"type": "unit", "id": "o00K", "field": "ubertip", "expected": wts_updates[12989]})

    # o00T: Землянка (A)
    wts_updates[6770] = "|cffe4cfa3Землянка|r"
    wts_updates[6771] = "|cffe4cfa3Землянка|r (|cffffffffA|r)"
    wts_updates[31676] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Культа Сумеречного Молота припасами. Позволяет батракам укрыться внутри и вести огонь по противникам.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+20|cffced4da золота каждые |cffffffff25|cffced4da сек.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o00T", "field": "name", "expected": wts_updates[6770]})
    checks_def.append({"type": "unit", "id": "o00T", "field": "tip", "expected": wts_updates[6771]})
    checks_def.append({"type": "unit", "id": "o00T", "field": "ubertip", "expected": wts_updates[31676]})

    # o00L: Казармы (W)
    wts_updates[6720] = "|cffe4cfa3Казармы|r"
    wts_updates[6721] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[12990] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военное сооружение, подготавливающее базовые боевые единицы и осадные орудия Культа Сумеречного Молота.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРубака|cffced4da.|n- |cffa9c7deСумеречный жнец|cffced4da.|n- |cffa9c7deРазрушитель|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deГрубая Сила|cffced4da.|n- |cffa9c7deТяжелые удары|cffced4da.|n- |cffa9c7deФанатичная Вера|cffced4da.|n- |cffa9c7deПорченные снаряды|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o00L", "field": "name", "expected": wts_updates[6720]})
    checks_def.append({"type": "unit", "id": "o00L", "field": "tip", "expected": wts_updates[6721]})
    checks_def.append({"type": "unit", "id": "o00L", "field": "ubertip", "expected": wts_updates[12990]})

    # o00R: Лесопилка (E)
    wts_updates[6764] = "|cffe4cfa3Лесопилка|r"
    wts_updates[6765] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[12991] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Пункт приёма древесины. Исследует улучшения вооружения, защиты и добычи ресурсов для войск Культа Сумеречного Молота.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенные инструменты|cffced4da.|n- |cffa9c7deОружие ближнего боя|cffced4da.|n- |cffa9c7deБроня ближнего боя|cffced4da.|n- |cffa9c7deМагия бездны|cffced4da.|n- |cffa9c7deПокровительство Бездны|cffced4da.|r"
    )
    wts_updates[12992] = wts_updates[12991]
    checks_def.append({"type": "unit", "id": "o00R", "field": "name", "expected": wts_updates[6764]})
    checks_def.append({"type": "unit", "id": "o00R", "field": "tip", "expected": wts_updates[6765]})
    checks_def.append({"type": "unit", "id": "o00R", "field": "ubertip", "expected": wts_updates[12992]})

    # o00V: Алтарь приношений (R)
    wts_updates[6730] = "|cffe4cfa3Алтарь приношений|r"
    wts_updates[6731] = "|cffe4cfa3Алтарь приношений|r (|cffffffffR|r)"
    wts_updates[6781] = "|cffe4cfa3Алтарь приношений|r"
    wts_updates[6782] = "|cffe4cfa3Алтарь приношений|r (|cffffffffR|r)"
    wts_updates[31678] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Мрачное святилище, призывающее чудовищ Бездны, аберраций и тёмных жрецов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deКаратель|cffced4da.|n- |cffa9c7deЖрец Бездны|cffced4da.|n- |cffa9c7deАберрация|cffced4da.|n- |cffa9c7deАстральная аберрация|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deДробящий удар|cffced4da.|n- |cffa9c7deВлияние бездны|cffced4da.|n- |cffa9c7deЗащита бездны|cffced4da.|n- |cffa9c7deХаотичная атака|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o00V", "field": "name", "expected": wts_updates[6781]})
    checks_def.append({"type": "unit", "id": "o00V", "field": "tip", "expected": wts_updates[6782]})
    checks_def.append({"type": "unit", "id": "o00V", "field": "ubertip", "expected": wts_updates[31678]})

    # o00P: Алтарь культа (S)
    wts_updates[6758] = "|cffe4cfa3Алтарь культа|r"
    wts_updates[6759] = "|cffe4cfa3Алтарь культа|r (|cffffffffS|r)"
    wts_updates[12993] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Позволяет призывать и воскрешать героев Культа Сумеречного Молота.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deВерховный Жрец бездны|cffced4da: маг Бездны, призывающий щупальца и ослабляющий врагов.|n"
        "- |cffa9c7deВоеначальник Культа|cffced4da: могучий воин ближнего боя, сокрушающий врагов в дуэлях.|n"
        "- |cffa9c7deТемный волшебник|cffced4da: чародей тёмной магии, призывающий Забытого.|r"
    )
    wts_updates[13003] = wts_updates[12993]
    checks_def.append({"type": "unit", "id": "o00P", "field": "name", "expected": wts_updates[6758]})
    checks_def.append({"type": "unit", "id": "o00P", "field": "tip", "expected": wts_updates[6759]})
    checks_def.append({"type": "unit", "id": "o00P", "field": "ubertip", "expected": wts_updates[13003]})

    # o00U: Обитель (D)
    wts_updates[6723] = "|cffe4cfa3Обитель|r"
    wts_updates[6739] = "|cffe4cfa3Обитель|r (|cffffffffD|r)"
    wts_updates[6779] = "|cffe4cfa3Обитель|r"
    wts_updates[6780] = "|cffe4cfa3Обитель|r (|cffffffffD|r)"
    wts_updates[12994] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Лагерь огров клана Сумеречного Молота. Нанимает огров-воинов и огров-магов, а также исследует их улучшения.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгр-воин|cffced4da.|n- |cffa9c7deОгр-маг|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deБлагодать древних богов|cffced4da.|n- |cffa9c7deВыносливость|cffced4da.|r"
    )
    wts_updates[31677] = wts_updates[12994]
    checks_def.append({"type": "unit", "id": "o00U", "field": "name", "expected": wts_updates[6779]})
    checks_def.append({"type": "unit", "id": "o00U", "field": "tip", "expected": wts_updates[6780]})
    checks_def.append({"type": "unit", "id": "o00U", "field": "ubertip", "expected": wts_updates[31677]})

    # o00Q: Сторожевая башня (Z)
    wts_updates[6761] = "|cffe4cfa3Сторожевая башня|r"
    wts_updates[6762] = "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)"
    wts_updates[1421] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение Культа Сумеречного Молота. Атакует наземных и воздушных противников с высокой дистанции.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o00Q", "field": "name", "expected": wts_updates[6761]})
    checks_def.append({"type": "unit", "id": "o00Q", "field": "tip", "expected": wts_updates[6762]})
    checks_def.append({"type": "unit", "id": "o00Q", "field": "ubertip", "expected": wts_updates[1421]})

    # h0D3: Верфь (C) - shared Horde shipyard
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
    # 3. HEROES (3 heroes)
    # =========================================================================
    # O011: Верховный Жрец бездны (C)
    wts_updates[7751] = "|cffe4cfa3Верховный Жрец бездны|r"
    wts_updates[7752] = "|cffe4cfa3Верховный Жрец бездны|r"
    wts_updates[7754] = "|cffe4cfa3Верховный Жрец бездны|r (|cffffffffC|r)"
    wts_updates[7755] = "|cffe4cfa3Верховный Жрец бездны|r"
    wts_updates[7753] = "|cffe4cfa3Верховный Жрец бездны|r"
    wts_updates[31679] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могущественный жрец Древних Богов, черпающий силу из глубин Бездны для призыва щупалец и ослабления армий врага.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПорождение щупальца|cffced4da: призывает щупальца из земли, атакующие противников.|n"
        "- |cffa9c7deДар бездны|cffced4da: восстанавливает здоровье союзникам и наносит урон врагам в области.|n"
        "- |cffa9c7deНечистая аура|cffced4da: аура, снижающая регенерацию здоровья врагов поблизости.|n"
        "- |cffa9c7deУжасающий вой|cffced4da: устрашающий крик, снижающий урон от атак противников.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "O011", "field": "name", "expected": wts_updates[7751]})
    checks_def.append({"type": "unit", "id": "O011", "field": "propernames", "expected": wts_updates[7752]})
    checks_def.append({"type": "unit", "id": "O011", "field": "tip", "expected": wts_updates[7754]})
    checks_def.append({"type": "unit", "id": "O011", "field": "ubertip", "expected": wts_updates[31679]})

    # N010: Военачальник Культа (X)
    wts_updates[8190] = "|cffe4cfa3Военачальник Культа|r"
    wts_updates[8191] = "|cffe4cfa3Военачальник Культа|r"
    wts_updates[8193] = "|cffe4cfa3Военачальник Культа|r (|cffffffffX|r)"
    wts_updates[8194] = "|cffe4cfa3Военачальник Культа|r"
    wts_updates[8192] = "|cffe4cfa3Военачальник Культа|r"
    wts_updates[31681] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Грозный двухголовый огр-полководец, сокрушающий врагов в одиночных поединках и вдохновляющий культистов на бой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКостолом|cffced4da: оглушающий удар, наносящий дополнительный урон цели.|n"
        "- |cffa9c7deДуэлянт|cffced4da: повышает шансы на уклонение от атак и критические удары.|n"
        "- |cffa9c7deУстрашающий рев|cffced4da: повергает врагов в трепет, снижая их урон и скорость.|n"
        "- |cffa9c7deРеинкарнация|cffced4da: позволяет герою мгновенно возродиться после гибели.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "N010", "field": "name", "expected": wts_updates[8190]})
    checks_def.append({"type": "unit", "id": "N010", "field": "propernames", "expected": wts_updates[8191]})
    checks_def.append({"type": "unit", "id": "N010", "field": "tip", "expected": wts_updates[8193]})
    checks_def.append({"type": "unit", "id": "N010", "field": "ubertip", "expected": wts_updates[31681]})

    # N00Z: Темный волшебник (Z)
    wts_updates[8239] = "|cffe4cfa3Темный волшебник|r"
    wts_updates[8240] = "|cffe4cfa3Темный волшебник|r"
    wts_updates[8242] = "|cffe4cfa3Темный волшебник|r (|cffffffffZ|r)"
    wts_updates[8243] = "|cffe4cfa3Темный волшебник|r"
    wts_updates[8241] = "|cffe4cfa3Темный волшебник|r"
    wts_updates[31680] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Чародей Бездны, полностью отдавший разум Древним Богам и призывающий древнее хтоническое зло.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВзрыв бездны|cffced4da: мощный всплеск тёмной энергии, наносящий урон по площади.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает положительные эффекты с врагов и наносит урон призывам.|n"
        "- |cffa9c7deЗамедляющий яд|cffced4da: отравляет врагов при атаке, снижая скорость и нанося периодический урон.|n"
        "- |cffa9c7deПризыв Забытого|cffced4da: призывает чудовищного Забытого для сокрушения врагов.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "N00Z", "field": "name", "expected": wts_updates[8239]})
    checks_def.append({"type": "unit", "id": "N00Z", "field": "propernames", "expected": wts_updates[8240]})
    checks_def.append({"type": "unit", "id": "N00Z", "field": "tip", "expected": wts_updates[8242]})
    checks_def.append({"type": "unit", "id": "N00Z", "field": "ubertip", "expected": wts_updates[31680]})

    # =========================================================================
    # 4. UNITS (13 units)
    # =========================================================================
    # o00J: Батрак (Q)
    wts_updates[6725] = "|cffe4cfa3Батрак|r"
    wts_updates[40940] = "|cffe4cfa3Батрак|r (|cffffffffQ|r)"
    wts_updates[11592] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Культа Сумеречного Молота. Добывает золото и древесину, возводит и ремонтирует здания, а также способен укрываться в землянках для обороны базы.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o00J", "field": "name", "expected": wts_updates[6725]})
    checks_def.append({"type": "unit", "id": "o00J", "field": "tip", "expected": wts_updates[40940]})
    checks_def.append({"type": "unit", "id": "o00J", "field": "ubertip", "expected": wts_updates[11592]})

    # o00M: Рубака (Q)
    wts_updates[6727] = "|cffe4cfa3Рубака|r"
    wts_updates[40941] = "|cffe4cfa3Рубака|r (|cffffffffQ|r)"
    wts_updates[38157] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основной пехотинец ближнего боя Культа Сумеречного Молота.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deТяжелые удары|cffced4da: шанс оглушить цель и нанести дополнительный урон (требует исследования).|n"
        "- |cffa9c7deГрубая Сила|cffced4da: увеличивает урон от атак (требует исследования).|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o00M", "field": "name", "expected": wts_updates[6727]})
    checks_def.append({"type": "unit", "id": "o00M", "field": "tip", "expected": wts_updates[40941]})
    checks_def.append({"type": "unit", "id": "o00M", "field": "ubertip", "expected": wts_updates[38157]})

    # o00N: Сумеречный жнец (W)
    wts_updates[6741] = "|cffe4cfa3Сумеречный жнец|r"
    wts_updates[40949] = "|cffe4cfa3Сумеречный жнец|r (|cffffffffW|r)"
    wts_updates[31675] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стрелок дальнего боя Культа Сумеречного Молота. Способен поражать врагов проклятиями и замедлять их передвижение.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПорча|cffced4da: накладывает на цель эффект, наносящий периодический урон.|n"
        "- |cffa9c7deЗамедление|cffced4da: снижает скорость перемещения и атаки противника.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o00N", "field": "name", "expected": wts_updates[6741]})
    checks_def.append({"type": "unit", "id": "o00N", "field": "tip", "expected": wts_updates[40949]})
    checks_def.append({"type": "unit", "id": "o00N", "field": "ubertip", "expected": wts_updates[31675]})

    # o00S: Разрушитель (E)
    wts_updates[6767] = "|cffe4cfa3Разрушитель|r"
    wts_updates[40955] = "|cffe4cfa3Разрушитель|r (|cffffffffE|r)"
    wts_updates[38172] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойное осадное орудие, крайне эффективное против зданий и скоплений пехоты противника.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПорченные снаряды|cffced4da: снаряды заражают область взрыва, нанося периодический урон (требует исследования).|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o00S", "field": "name", "expected": wts_updates[6767]})
    checks_def.append({"type": "unit", "id": "o00S", "field": "tip", "expected": wts_updates[40955]})
    checks_def.append({"type": "unit", "id": "o00S", "field": "ubertip", "expected": wts_updates[38172]})

    # o002: Каратель (Q)
    wts_updates[9247] = "|cffe4cfa3Каратель|r"
    wts_updates[40948] = "|cffe4cfa3Каратель|r (|cffffffffQ|r)"
    wts_updates[38161] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий боец ближнего боя из рядов Безликих. Наносит урон типа «Хаос» и пробивает защиту врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДробящий удар|cffced4da: сокрушительный удар, оглушающий цель и наносящий дополнительный урон (требует исследования).|n"
        "- |cffa9c7deЗащита Бездны|cffced4da: увеличивает сопротивление магии.|n"
        "- |cffa9c7deЯрость Бездны|cffced4da: усиливает боевые характеристики при потере здоровья.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o002", "field": "name", "expected": wts_updates[9247]})
    checks_def.append({"type": "unit", "id": "o002", "field": "tip", "expected": wts_updates[40948]})
    checks_def.append({"type": "unit", "id": "o002", "field": "ubertip", "expected": wts_updates[38161]})

    # u004: Жрец Бездны (W)
    wts_updates[40951] = "|cffe4cfa3Жрец Бездны|r"
    wts_updates[40952] = "|cffe4cfa3Жрец Бездны|r (|cffffffffW|r)"
    wts_updates[38171] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основной заклинатель Культа Сумеречного Молота. Манипулирует силами Бездны для исцеления союзников и призыва щупалец.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПорождение щупальца|cffced4da: призывает щупальце из земли для атаки врагов.|n"
        "- |cffa9c7deЭссенция бездны|cffced4da: восстанавливает здоровье союзной единице.|n"
        "- |cffa9c7deЗащита Бездны|cffced4da: снижает получаемый магический урон.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u004", "field": "name", "expected": wts_updates[40951]})
    checks_def.append({"type": "unit", "id": "u004", "field": "tip", "expected": wts_updates[40952]})
    checks_def.append({"type": "unit", "id": "u004", "field": "ubertip", "expected": wts_updates[38171]})

    # n00R: Аберрация (E)
    wts_updates[40946] = "|cffe4cfa3Аберрация|r"
    wts_updates[40947] = "|cffe4cfa3Аберрация|r (|cffffffffE|r)"
    wts_updates[38160] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучее порождение Древних Богов, сотворённое из искажённой плоти. Наносит урон типа «Хаос» и ослабляет противников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура поглощения|cffced4da: обращает часть наносимого урона в здоровье союзников.|n"
        "- |cffa9c7deКоррозия бездны|cffced4da: разъедает броню противника при каждой атаке.|n"
        "- |cffa9c7deЗащита Бездны|cffced4da: снижает получаемый магический урон.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n00R", "field": "name", "expected": wts_updates[40946]})
    checks_def.append({"type": "unit", "id": "n00R", "field": "tip", "expected": wts_updates[40947]})
    checks_def.append({"type": "unit", "id": "n00R", "field": "ubertip", "expected": wts_updates[38160]})

    # n00U: Астральная аберрация (R)
    wts_updates[6870] = "|cffe4cfa3Астральная аберрация|r"
    wts_updates[40956] = "|cffe4cfa3Астральная аберрация|r (|cffffffffR|r)"
    wts_updates[38173] = (
        "|cffa6afb8ЮНИТ:|cffced4da Высшая форма аберрации, напитанная мощью астральной магии и Бездны. Наносит колоссальный урон типа «Хаос».|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКоррозия бездны|cffced4da: разъедает броню цели при попадании, ослабляя защиту.|n"
        "- |cffa9c7deЗащита Бездны|cffced4da: снижает получаемый магический урон.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n00U", "field": "name", "expected": wts_updates[6870]})
    checks_def.append({"type": "unit", "id": "n00U", "field": "tip", "expected": wts_updates[40956]})
    checks_def.append({"type": "unit", "id": "n00U", "field": "ubertip", "expected": wts_updates[38173]})

    # n00D: Огр-воин (Q)
    wts_updates[6732] = "|cffe4cfa3Огр-воин|r"
    wts_updates[40944] = "|cffe4cfa3Огр-воин|r (|cffffffffQ|r)"
    wts_updates[38159] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стойкий и могучий воин ближнего боя из клана огров Сумеречного Молота.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deТяжелые удары|cffced4da: шанс оглушить врага и нанести дополнительный урон (требует исследования).|n"
        "- |cffa9c7deВыносливость|cffced4da: увеличивает максимальный запас здоровья (требует исследования).|n"
        "- |cffa9c7deЗащита Бездны|cffced4da: повышает устойчивость к магии.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n00D", "field": "name", "expected": wts_updates[6732]})
    checks_def.append({"type": "unit", "id": "n00D", "field": "tip", "expected": wts_updates[40944]})
    checks_def.append({"type": "unit", "id": "n00D", "field": "ubertip", "expected": wts_updates[38159]})

    # n00C: Огр-маг (W)
    wts_updates[40942] = "|cffe4cfa3Огр-маг|r"
    wts_updates[40943] = "|cffe4cfa3Огр-маг|r (|cffffffffW|r)"
    wts_updates[38158] = (
        "|cffa6afb8ЮНИТ:|cffced4da Двухголовый огр-заклинатель, владеющий боевой магией и чарами Древних Богов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЖажда крови|cffced4da: повышает скорость перемещения и атаки союзника.|n"
        "- |cffa9c7deБлагодать древних богов|cffced4da: дарует союзнику щит, поглощающий урон (требует исследования).|n"
        "- |cffa9c7deЗатуманенный рассудок|cffced4da: лишает цель возможности применять заклинания.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n00C", "field": "name", "expected": wts_updates[40942]})
    checks_def.append({"type": "unit", "id": "n00C", "field": "tip", "expected": wts_updates[40943]})
    checks_def.append({"type": "unit", "id": "n00C", "field": "ubertip", "expected": wts_updates[38158]})

    # o00O: Сумеречный налетчик (E)
    wts_updates[6744] = "|cffe4cfa3Сумеречный налетчик|r"
    wts_updates[40950] = "|cffe4cfa3Сумеречный налетчик|r (|cffffffffE|r)"
    wts_updates[12517] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый кавалерист на волке, наносящий урон типа «Хаос» и сковывающий противников сетью.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОпутывание|cffced4da: обездвиживает врага и притягивает летающие цели к земле.|n"
        "- |cffa9c7deТяжелые удары|cffced4da: шанс оглушить врага при ударе (требует исследования).|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o00O", "field": "name", "expected": wts_updates[6744]})
    checks_def.append({"type": "unit", "id": "o00O", "field": "tip", "expected": wts_updates[40950]})
    checks_def.append({"type": "unit", "id": "o00O", "field": "ubertip", "expected": wts_updates[12517]})

    # n00S: Древний дракон Пустоты (D)
    wts_updates[6755] = "|cffe4cfa3Древний дракон Пустоты|r"
    wts_updates[40954] = "|cffe4cfa3Древний дракон Пустоты|r (|cffffffffD|r)"
    checks_def.append({"type": "unit", "id": "n00S", "field": "name", "expected": wts_updates[6755]})
    checks_def.append({"type": "unit", "id": "n00S", "field": "tip", "expected": wts_updates[40954]})

    # u005: Наездник сумрака (Q)
    wts_updates[7630] = "|cffe4cfa3Наездник сумрака|r"
    wts_updates[40953] = "|cffe4cfa3Наездник сумрака|r (|cffffffffQ|r)"
    wts_updates[2418] = (
        "|cffa6afb8ЮНИТ:|cffced4da Опытный наездник на драконе Пустоты, атакующий противников с воздуха и защищённый тёмными чарами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗащита Бездны|cffced4da: снижает получаемый магический урон.|n"
        "- |cffa9c7deЯрость Бездны|cffced4da: усиливает урон при потере здоровья.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u005", "field": "name", "expected": wts_updates[7630]})
    checks_def.append({"type": "unit", "id": "u005", "field": "tip", "expected": wts_updates[40953]})
    checks_def.append({"type": "unit", "id": "u005", "field": "ubertip", "expected": wts_updates[2418]})

    # =========================================================================
    # 5. RESEARCHES (16 upgrades, 52 levels)
    # =========================================================================
    # R04D: Фанатизм (levels 1-6) (Z)
    r04d_names = [40024, 40026, 40027, 40028, 40084, 40104]
    r04d_tips = [12523, 12524, 12525, 12526, 12527, 12528]
    r04d_ubs = [8454, 8453, 8448, 8449, 8451, 8452]
    for lvl in range(1, 7):
        wts_updates[r04d_names[lvl-1]] = f"|cffe4cfa3Фанатизм|r [|cffffffff{lvl}|r]"
        wts_updates[r04d_tips[lvl-1]] = f"|cffe4cfa3Фанатизм|r [|cffffffff{lvl}|r] (|cffffffffZ|r)"
        wts_updates[r04d_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья культистов на |cffffffff30|cffced4da ед., урон на |cffffffff2|cffced4da ед., повышает запас и регенерацию маны, а также открывает доступ к передовым технологиям и войскам.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Войскам и постройкам Культа Сумеречного Молота.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R04D", "field": f"name{lvl}", "expected": wts_updates[r04d_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R04D", "field": f"tip{lvl}", "expected": wts_updates[r04d_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R04D", "field": f"ubertip{lvl}", "expected": wts_updates[r04d_ubs[lvl-1]]})

    # R04V: Грубая Сила (level 1) (A)
    wts_updates[7680] = "|cffe4cfa3Грубая Сила|r"
    wts_updates[7681] = "|cffe4cfa3Грубая Сила|r (|cffffffffA|r)"
    wts_updates[7682] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак рубак на |cffffffff2|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R04V", "field": "name1", "expected": wts_updates[7680]})
    checks_def.append({"type": "upgrade", "id": "R04V", "field": "tip1", "expected": wts_updates[7681]})
    checks_def.append({"type": "upgrade", "id": "R04V", "field": "ubertip1", "expected": wts_updates[7682]})

    # R00O: Тяжелые удары (level 1) (Z)
    wts_updates[7661] = "|cffe4cfa3Тяжелые удары|r"
    wts_updates[7662] = "|cffe4cfa3Тяжелые удары|r (|cffffffffZ|r)"
    wts_updates[7663] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет рубак и огров-воинов способностью «Тяжелые удары», дающей шанс оглушить врага и нанести дополнительный урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da.|n- |cffa9c7deОгр-воин|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R00O", "field": "name1", "expected": wts_updates[7661]})
    checks_def.append({"type": "upgrade", "id": "R00O", "field": "tip1", "expected": wts_updates[7662]})
    checks_def.append({"type": "upgrade", "id": "R00O", "field": "ubertip1", "expected": wts_updates[7663]})

    # R04S: Фанатичная Вера (levels 1-2) (S)
    wts_updates[7664] = "|cffe4cfa3Фанатичная Вера|r [|cffffffff1|r]"
    wts_updates[7665] = "|cffe4cfa3Фанатичная Вера|r [|cffffffff1|r] (|cffffffffS|r)"
    wts_updates[7666] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает боевые качества сумеречных жнецов, повышая их боевую стойкость и эффективность.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный жнец|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    )
    wts_updates[7667] = "|cffe4cfa3Фанатичная Вера|r [|cffffffff2|r]"
    wts_updates[7668] = "|cffe4cfa3Фанатичная Вера|r [|cffffffff2|r] (|cffffffffS|r)"
    wts_updates[7669] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает боевые качества сумеречных жнецов.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный жнец|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R04S", "field": "name1", "expected": wts_updates[7664]})
    checks_def.append({"type": "upgrade", "id": "R04S", "field": "tip1", "expected": wts_updates[7665]})
    checks_def.append({"type": "upgrade", "id": "R04S", "field": "ubertip1", "expected": wts_updates[7666]})
    checks_def.append({"type": "upgrade", "id": "R04S", "field": "name2", "expected": wts_updates[7667]})
    checks_def.append({"type": "upgrade", "id": "R04S", "field": "tip2", "expected": wts_updates[7668]})
    checks_def.append({"type": "upgrade", "id": "R04S", "field": "ubertip2", "expected": wts_updates[7669]})

    # R04U: Порченные снаряды (level 1) (C)
    wts_updates[7673] = "|cffe4cfa3Порченные снаряды|r"
    wts_updates[7674] = "|cffe4cfa3Порченные снаряды|r (|cffffffffC|r)"
    wts_updates[7675] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет разрушителей способностью «Порченные снаряды», заражающей поражённую область и наносящей периодический урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРазрушитель|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R04U", "field": "name1", "expected": wts_updates[7673]})
    checks_def.append({"type": "upgrade", "id": "R04U", "field": "tip1", "expected": wts_updates[7674]})
    checks_def.append({"type": "upgrade", "id": "R04U", "field": "ubertip1", "expected": wts_updates[7675]})

    # R0EJ: Улучшенные инструменты (levels 1-6) (Z)
    r0ej_names = [40857, 40858, 40859, 40860, 40861, 40862]
    r0ej_tips = [40863, 40864, 40865, 40866, 40867, 40868]
    r0ej_ubs = [22416, 22411, 22412, 22413, 22414, 22415]
    for lvl in range(1, 7):
        wts_updates[r0ej_names[lvl-1]] = f"|cffe4cfa3Улучшенные инструменты|r [|cffffffff{lvl}|r]"
        wts_updates[r0ej_tips[lvl-1]] = f"|cffe4cfa3Улучшенные инструменты|r [|cffffffff{lvl}|r] (|cffffffffZ|r)"
        wts_updates[r0ej_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой батраками древесины на |cffffffff5|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deБатрак|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0EJ", "field": f"name{lvl}", "expected": wts_updates[r0ej_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0EJ", "field": f"tip{lvl}", "expected": wts_updates[r0ej_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0EJ", "field": f"ubertip{lvl}", "expected": wts_updates[r0ej_ubs[lvl-1]]})

    # R05S: Оружие ближнего боя (levels 1-6) (Q)
    r05s_names = [9163, 9165, 9164, 9168, 9167, 9166]
    r05s_tips = [11687, 11834, 11868, 11871, 11870, 11869]
    r05s_ubs = [11948, 12031, 12032, 11873, 11872, 11946]
    r05s_prefixes = [
        "Стальное оружие ближнего боя", "Стальное оружие ближнего боя",
        "Ториевое оружие ближнего боя", "Ториевое оружие ближнего боя",
        "Арканитовое оружие ближнего боя", "Арканитовое оружие ближнего боя"
    ]
    for lvl in range(1, 7):
        pfx = r05s_prefixes[lvl-1]
        wts_updates[r05s_names[lvl-1]] = f"|cffe4cfa3{pfx}|r [|cffffffff{lvl}|r]"
        wts_updates[r05s_tips[lvl-1]] = f"|cffe4cfa3{pfx}|r [|cffffffff{lvl}|r] (|cffffffffQ|r)"
        wts_updates[r05s_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак бойцов ближнего боя Культа Сумеречного Молота.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da.|n- |cffa9c7deОгр-воин|cffced4da.|n- |cffa9c7deКаратель|cffced4da.|n- |cffa9c7deСумеречный налетчик|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R05S", "field": f"name{lvl}", "expected": wts_updates[r05s_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05S", "field": f"tip{lvl}", "expected": wts_updates[r05s_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05S", "field": f"ubertip{lvl}", "expected": wts_updates[r05s_ubs[lvl-1]]})

    # R05T: Броня ближнего боя (levels 1-6) (A)
    r05t_names = [9188, 9189, 9190, 9193, 9192, 9191]
    r05t_tips = [12033, 13612, 13635, 18265, 14376, 13870]
    r05t_ubs = [18455, 18456, 18582, 18454, 18451, 18267]
    r05t_prefixes = [
        "Стальная броня", "Стальная броня",
        "Ториевая броня", "Ториевая броня",
        "Арканитовая броня", "Арканитовая броня"
    ]
    for lvl in range(1, 7):
        pfx = r05t_prefixes[lvl-1]
        wts_updates[r05t_names[lvl-1]] = f"|cffe4cfa3{pfx}|r [|cffffffff{lvl}|r]"
        wts_updates[r05t_tips[lvl-1]] = f"|cffe4cfa3{pfx}|r [|cffffffff{lvl}|r] (|cffffffffA|r)"
        wts_updates[r05t_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню бойцов ближнего боя Культа Сумеречного Молота.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da.|n- |cffa9c7deОгр-воин|cffced4da.|n- |cffa9c7deКаратель|cffced4da.|n- |cffa9c7deСумеречный налетчик|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R05T", "field": f"name{lvl}", "expected": wts_updates[r05t_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05T", "field": f"tip{lvl}", "expected": wts_updates[r05t_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05T", "field": f"ubertip{lvl}", "expected": wts_updates[r05t_ubs[lvl-1]]})

    # R05U: Магия бездны (levels 1-6) (W)
    r05u_names = [9210, 9211, 9212, 9215, 9214, 9213]
    r05u_tips = [18594, 18595, 18625, 18628, 18627, 18626]
    r05u_ubs = [18632, 18633, 18634, 18629, 18630, 18631]
    for lvl in range(1, 7):
        wts_updates[r05u_names[lvl-1]] = f"|cffe4cfa3Магия бездны|r [|cffffffff{lvl}|r]"
        wts_updates[r05u_tips[lvl-1]] = f"|cffe4cfa3Магия бездны|r [|cffffffff{lvl}|r] (|cffffffffW|r)"
        wts_updates[r05u_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от дистанционных и магических атак войск Культа Сумеречного Молота.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный жнец|cffced4da.|n- |cffa9c7deЖрец Бездны|cffced4da.|n- |cffa9c7deОгр-маг|cffced4da.|n- |cffa9c7deРазрушитель|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R05U", "field": f"name{lvl}", "expected": wts_updates[r05u_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05U", "field": f"tip{lvl}", "expected": wts_updates[r05u_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05U", "field": f"ubertip{lvl}", "expected": wts_updates[r05u_ubs[lvl-1]]})

    # R05V: Покровительство Бездны (levels 1-6) (S)
    r05v_names = [9231, 9232, 9233, 9234, 9235, 9236]
    r05v_tips = [18635, 18636, 18637, 18638, 18639, 18640]
    r05v_ubs = [18644, 18645, 18646, 18641, 18642, 18643]
    for lvl in range(1, 7):
        wts_updates[r05v_names[lvl-1]] = f"|cffe4cfa3Покровительство Бездны|r [|cffffffff{lvl}|r]"
        wts_updates[r05v_tips[lvl-1]] = f"|cffe4cfa3Покровительство Бездны|r [|cffffffff{lvl}|r] (|cffffffffS|r)"
        wts_updates[r05v_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает броню стрелков и магов Культа Сумеречного Молота.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный жнец|cffced4da.|n- |cffa9c7deЖрец Бездны|cffced4da.|n- |cffa9c7deОгр-маг|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R05V", "field": f"name{lvl}", "expected": wts_updates[r05v_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05V", "field": f"tip{lvl}", "expected": wts_updates[r05v_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R05V", "field": f"ubertip{lvl}", "expected": wts_updates[r05v_ubs[lvl-1]]})

    # R04Z: Дробящий удар (level 1) (A)
    wts_updates[7720] = "|cffe4cfa3Дробящий удар|r"
    wts_updates[7721] = "|cffe4cfa3Дробящий удар|r (|cffffffffA|r)"
    wts_updates[7722] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет карателей способностью «Дробящий удар», позволяющей оглушать врага и наносить дополнительный урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deКаратель|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R04Z", "field": "name1", "expected": wts_updates[7720]})
    checks_def.append({"type": "upgrade", "id": "R04Z", "field": "tip1", "expected": wts_updates[7721]})
    checks_def.append({"type": "upgrade", "id": "R04Z", "field": "ubertip1", "expected": wts_updates[7722]})

    # R050: Влияние бездны (levels 1-2) (S)
    wts_updates[7727] = "|cffe4cfa3Влияние бездны|r [|cffffffff1|r]"
    wts_updates[7728] = "|cffe4cfa3Влияние бездны|r [|cffffffff1|r] (|cffffffffS|r)"
    wts_updates[7729] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет жрецов Бездны новыми заклинаниями и повышает их запас характеристик.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЖрец Бездны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    )
    wts_updates[7730] = "|cffe4cfa3Влияние бездны|r [|cffffffff2|r]"
    wts_updates[7731] = "|cffe4cfa3Влияние бездны|r [|cffffffff2|r] (|cffffffffS|r)"
    wts_updates[7732] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет жрецов Бездны высшими заклинаниями и максимально увеличивает их характеристики.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЖрец Бездны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R050", "field": "name1", "expected": wts_updates[7727]})
    checks_def.append({"type": "upgrade", "id": "R050", "field": "tip1", "expected": wts_updates[7728]})
    checks_def.append({"type": "upgrade", "id": "R050", "field": "ubertip1", "expected": wts_updates[7729]})
    checks_def.append({"type": "upgrade", "id": "R050", "field": "name2", "expected": wts_updates[7730]})
    checks_def.append({"type": "upgrade", "id": "R050", "field": "tip2", "expected": wts_updates[7731]})
    checks_def.append({"type": "upgrade", "id": "R050", "field": "ubertip2", "expected": wts_updates[7732]})

    # R051: Защита бездны (level 1) (C)
    wts_updates[7737] = "|cffe4cfa3Защита бездны|r"
    wts_updates[7738] = "|cffe4cfa3Защита бездны|r (|cffffffffC|r)"
    wts_updates[7739] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает сопротивление магическому урону у аберраций и созданий Бездны.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАберрация|cffced4da.|n- |cffa9c7deКаратель|cffced4da.|n- |cffa9c7deЖрец Бездны|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R051", "field": "name1", "expected": wts_updates[7737]})
    checks_def.append({"type": "upgrade", "id": "R051", "field": "tip1", "expected": wts_updates[7738]})
    checks_def.append({"type": "upgrade", "id": "R051", "field": "ubertip1", "expected": wts_updates[7739]})

    # R052: Хаотичная атака (level 1) (D)
    wts_updates[8467] = "|cffe4cfa3Хаотичная атака|r"
    wts_updates[7745] = "|cffe4cfa3Хаотичная атака|r (|cffffffffD|r)"
    wts_updates[20108] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет атаки аберраций типом урона «Хаос», пробивающим любые виды брони.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАберрация|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R052", "field": "name1", "expected": wts_updates[8467]})
    checks_def.append({"type": "upgrade", "id": "R052", "field": "tip1", "expected": wts_updates[7745]})
    checks_def.append({"type": "upgrade", "id": "R052", "field": "ubertip1", "expected": wts_updates[20108]})

    # R04W: Благодать богов (levels 1-3) (A)
    wts_updates[7691] = "|cffe4cfa3Благодать древних богов|r [|cffffffff1|r]"
    wts_updates[7692] = "|cffe4cfa3Благодать древних богов|r [|cffffffff1|r] (|cffffffffA|r)"
    wts_updates[15196] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет огров-магов заклинанием «Благодать древних богов» и увеличивает их запас маны на |cffffffff45|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОгр-маг|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff3|cffced4da.|r"
    )
    wts_updates[7694] = "|cffe4cfa3Благодать древних богов|r [|cffffffff2|r]"
    wts_updates[7695] = "|cffe4cfa3Благодать древних богов|r [|cffffffff2|r] (|cffffffffA|r)"
    wts_updates[15197] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас маны огров-магов ещё на |cffffffff45|cffced4da ед. и усиливает эффект благодати.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОгр-маг|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff3|cffced4da.|r"
    )
    wts_updates[7698] = "|cffe4cfa3Благодать древних богов|r [|cffffffff3|r]"
    wts_updates[7699] = "|cffe4cfa3Благодать древних богов|r [|cffffffff3|r] (|cffffffffA|r)"
    wts_updates[15198] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Максимально увеличивает запас маны огров-магов ещё на |cffffffff45|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОгр-маг|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3|cffced4da/|cffffffff3|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "name1", "expected": wts_updates[7691]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "tip1", "expected": wts_updates[7692]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "ubertip1", "expected": wts_updates[15196]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "name2", "expected": wts_updates[7694]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "tip2", "expected": wts_updates[7695]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "ubertip2", "expected": wts_updates[15197]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "name3", "expected": wts_updates[7698]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "tip3", "expected": wts_updates[7699]})
    checks_def.append({"type": "upgrade", "id": "R04W", "field": "ubertip3", "expected": wts_updates[15198]})

    # R04X: Выносливость (level 1) (S)
    wts_updates[7702] = "|cffe4cfa3Выносливость|r"
    wts_updates[7703] = "|cffe4cfa3Выносливость|r (|cffffffffS|r)"
    wts_updates[15199] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья огров-воинов на |cffffffff150|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОгр-воин|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R04X", "field": "name1", "expected": wts_updates[7702]})
    checks_def.append({"type": "upgrade", "id": "R04X", "field": "tip1", "expected": wts_updates[7703]})
    checks_def.append({"type": "upgrade", "id": "R04X", "field": "ubertip1", "expected": wts_updates[15199]})

    # =========================================================================
    # 6. HERO ABILITIES (12 abilities)
    # =========================================================================
    # --- O011 Верховный Жрец бездны ---
    # A0AO: Порождение щупальца (Q)
    wts_updates[7644] = "|cffe4cfa3Порождение щупальца|r"
    wts_updates[7759] = "|cffe4cfa3Порождение щупальца|r"
    wts_updates[9840] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из земли могучие щупальца Древних Богов, атакующие противников на средней дистанции.|n|n"
        "|cffa6afb8Уровень 1:|r призывает |cffffffff2|cffced4da щупальца.|n"
        "|cffa6afb8Уровень 2:|r призывает |cffffffff3|cffced4da щупальца.|n"
        "|cffa6afb8Уровень 3:|r призывает |cffffffff4|cffced4da щупальца.|n"
        "|cffa6afb8Уровень 4:|r призывает |cffffffff5|cffced4da щупалец.|r"
    )
    ao_tips = [7646, 7656, 7757, 7758]
    ao_ubs = [12545, 11633, 12541, 12543]
    ao_counts = [2, 3, 4, 5]
    for lvl in range(1, 5):
        wts_updates[ao_tips[lvl-1]] = f"|cffe4cfa3Порождение щупальца|r [|cffffffff{lvl}|r] (|cffffffffQ|r)"
        wts_updates[ao_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из земли |cffffffff{ao_counts[lvl-1]}|cffced4da щупальца Древних Богов, атакующих противников на средней дистанции.|r"
        )
        checks_def.append({"type": "ability", "id": "A0AO", "field": f"tip{lvl}", "expected": wts_updates[ao_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0AO", "field": f"ubertip{lvl}", "expected": wts_updates[ao_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0AO", "field": "name", "expected": wts_updates[7644]})

    # A0AP: Дар бездны (W)
    wts_updates[7780] = "|cffe4cfa3Дар бездны|r"
    wts_updates[9698] = "|cffe4cfa3Дар бездны|r"
    wts_updates[10117] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вызывает волну тёмной энергии, восстанавливающую здоровье союзникам вокруг героя.|n|n"
        "|cffa6afb8Уровень 1:|r восстанавливает |cffc8e087125|cffced4da ед. здоровья.|n"
        "|cffa6afb8Уровень 2:|r восстанавливает |cffc8e087200|cffced4da ед. здоровья.|n"
        "|cffa6afb8Уровень 3:|r восстанавливает |cffc8e087275|cffced4da ед. здоровья.|n"
        "|cffa6afb8Уровень 4:|r восстанавливает |cffc8e087350|cffced4da ед. здоровья.|r"
    )
    ap_tips = [7781, 7783, 7784, 7785]
    ap_ubs = [8218, 8222, 8223, 8224]
    ap_heals = [125, 200, 275, 350]
    for lvl in range(1, 5):
        wts_updates[ap_tips[lvl-1]] = f"|cffe4cfa3Дар бездны|r [|cffffffff{lvl}|r] (|cffffffffW|r)"
        wts_updates[ap_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087{ap_heals[lvl-1]}|cffced4da ед. здоровья союзникам в области вокруг героя.|r"
        )
        checks_def.append({"type": "ability", "id": "A0AP", "field": f"tip{lvl}", "expected": wts_updates[ap_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0AP", "field": f"ubertip{lvl}", "expected": wts_updates[ap_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0AP", "field": "name", "expected": wts_updates[7780]})

    # A0B6: Нечистая аура (E, passive)
    wts_updates[8158] = "|cffe4cfa3Нечистая аура|r"
    wts_updates[8159] = "|cffe4cfa3Нечистая аура|r"
    wts_updates[10135] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная аура, подавляющая восстановление здоровья у находящихся поблизости противников.|n|n"
        "|cffa6afb8Уровень 1:|r снижает регенерацию здоровья на |cffe69a8d1|cffced4da ед./сек.|n"
        "|cffa6afb8Уровень 2:|r снижает регенерацию здоровья на |cffe69a8d1,5|cffced4da ед./сек.|n"
        "|cffa6afb8Уровень 3:|r снижает регенерацию здоровья на |cffe69a8d2|cffced4da ед./сек.|n"
        "|cffa6afb8Уровень 4:|r снижает регенерацию здоровья на |cffe69a8d2,5|cffced4da ед./сек.|r"
    )
    b6_tips = [8161, 8162, 8163, 8164]
    b6_ubs = [10151, 10153, 10154, 10176]
    b6_vals = ["1", "1,5", "2", "2,5"]
    for lvl in range(1, 5):
        wts_updates[b6_tips[lvl-1]] = f"|cffe4cfa3Нечистая аура|r [|cffffffff{lvl}|r]"
        wts_updates[b6_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно снижает скорость восстановления здоровья врагов поблизости на |cffe69a8d{b6_vals[lvl-1]}|cffced4da ед./сек.|r"
        )
        checks_def.append({"type": "ability", "id": "A0B6", "field": f"tip{lvl}", "expected": wts_updates[b6_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0B6", "field": f"ubertip{lvl}", "expected": wts_updates[b6_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0B6", "field": "name", "expected": wts_updates[8158]})

    # A0B8: Ужасающий вой (R)
    wts_updates[8179] = "|cffe4cfa3Ужасающий вой|r"
    wts_updates[10204] = "|cffe4cfa3Ужасающий вой|r"
    wts_updates[10203] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издаёт леденящий душу вой Бездны, повергающий врагов в панику и снижающий их урон от атак.|n|n"
        "|cffa6afb8Уровень 1:|r снижает урон от атак врагов на |cffe69a8d55%|cffced4da.|n"
        "|cffa6afb8Уровень 2:|r снижает урон от атак врагов на |cffe69a8d70%|cffced4da.|r"
    )
    wts_updates[8180] = "|cffe4cfa3Ужасающий вой|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[10205] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает урон от атак противников поблизости на |cffe69a8d55%|cffced4da.|r"
    wts_updates[8181] = "|cffe4cfa3Ужасающий вой|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[10202] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает урон от атак противников поблизости на |cffe69a8d70%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0B8", "field": "name", "expected": wts_updates[8179]})
    checks_def.append({"type": "ability", "id": "A0B8", "field": "tip1", "expected": wts_updates[8180]})
    checks_def.append({"type": "ability", "id": "A0B8", "field": "ubertip1", "expected": wts_updates[10205]})
    checks_def.append({"type": "ability", "id": "A0B8", "field": "tip2", "expected": wts_updates[8181]})
    checks_def.append({"type": "ability", "id": "A0B8", "field": "ubertip2", "expected": wts_updates[10202]})

    # --- N010 Военачальник Культа ---
    # A0B9: Костолом (E, passive)
    wts_updates[8196] = "|cffe4cfa3Костолом|r"
    wts_updates[8197] = "|cffe4cfa3Костолом|r"
    wts_updates[10229] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс при каждой атаке оглушить цель и нанести ей дополнительный урон.|n|n"
        "|cffa6afb8Уровень 1:|r шанс оглушения, оглушает героев на |cffffffff0,4|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|r шанс оглушения, оглушает героев на |cffffffff0,5|cffced4da сек.|n"
        "|cffa6afb8Уровень 3:|r шанс оглушения, оглушает героев на |cffffffff0,6|cffced4da сек.|n"
        "|cffa6afb8Уровень 4:|r шанс оглушения, оглушает героев на |cffffffff0,7|cffced4da сек.|r"
    )
    b9_tips = [8198, 8199, 8200, 8201]
    b9_ubs = [10230, 12914, 12919, 10219]
    b9_times = ["0,4", "0,5", "0,6", "0,7"]
    for lvl in range(1, 5):
        wts_updates[b9_tips[lvl-1]] = f"|cffe4cfa3Костолом|r [|cffffffff{lvl}|r]"
        wts_updates[b9_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс оглушить цель при атаке и нанести ей дополнительный урон. Длительность оглушения героев: |cffffffff{b9_times[lvl-1]}|cffced4da сек.|r"
        )
        checks_def.append({"type": "ability", "id": "A0B9", "field": f"tip{lvl}", "expected": wts_updates[b9_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0B9", "field": f"ubertip{lvl}", "expected": wts_updates[b9_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0B9", "field": "name", "expected": wts_updates[8196]})

    # A0BA: Дуэлянт (W, passive)
    wts_updates[8203] = "|cffe4cfa3Дуэлянт|r"
    wts_updates[8204] = "|cffe4cfa3Дуэлянт|r"
    wts_updates[225] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой специализируется на смертельных поединках, нанося увеличенный урон вражеским героям.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+15%|cffced4da к урону по героям.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+25%|cffced4da к урону по героям.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+35%|cffced4da к урону по героям.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+45%|cffced4da к урону по героям.|r"
    )
    ba_tips = [8206, 8207, 8208, 8209]
    ba_ubs = [4382, 762, 764, 4345]
    ba_pcts = [15, 25, 35, 45]
    for lvl in range(1, 5):
        wts_updates[ba_tips[lvl-1]] = f"|cffe4cfa3Дуэлянт|r [|cffffffff{lvl}|r]"
        wts_updates[ba_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает урон героя по вражеским героям на |cffc8e087+{ba_pcts[lvl-1]}%|cffced4da.|r"
        )
        checks_def.append({"type": "ability", "id": "A0BA", "field": f"tip{lvl}", "expected": wts_updates[ba_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0BA", "field": f"ubertip{lvl}", "expected": wts_updates[ba_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0BA", "field": "name", "expected": wts_updates[8203]})

    # A0BB: Устрашающий рев (Q)
    wts_updates[8214] = "|cffe4cfa3Устрашающий рев|r"
    wts_updates[8217] = "|cffe4cfa3Устрашающий рев|r"
    wts_updates[7240] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издаёт громогласный боевой рёв, сокрушающий боевой дух врагов и снижающий их защиту.|n|n"
        "|cffa6afb8Уровень 1:|r снижает броню врагов на |cffe69a8d2|cffced4da ед.|n"
        "|cffa6afb8Уровень 2:|r снижает броню врагов на |cffe69a8d3|cffced4da ед.|n"
        "|cffa6afb8Уровень 3:|r снижает броню врагов на |cffe69a8d4|cffced4da ед.|n"
        "|cffa6afb8Уровень 4:|r снижает броню врагов на |cffe69a8d5|cffced4da ед.|r"
    )
    bb_tips = [8215, 8219, 8220, 8221]
    bb_ubs = [4383, 7454, 8402, 8401]
    bb_armor = [2, 3, 4, 5]
    for lvl in range(1, 5):
        wts_updates[bb_tips[lvl-1]] = f"|cffe4cfa3Устрашающий рев|r [|cffffffff{lvl}|r] (|cffffffffQ|r)"
        wts_updates[bb_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню противников поблизости на |cffe69a8d{bb_armor[lvl-1]}|cffced4da ед.|r"
        )
        checks_def.append({"type": "ability", "id": "A0BB", "field": f"tip{lvl}", "expected": wts_updates[bb_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0BB", "field": f"ubertip{lvl}", "expected": wts_updates[bb_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0BB", "field": "name", "expected": wts_updates[8214]})

    # A0BC: Реинкарнация (R, passive)
    wts_updates[8226] = "|cffe4cfa3Реинкарнация|r"
    wts_updates[8227] = "|cffe4cfa3Реинкарнация|r"
    wts_updates[14961] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет военачальнику мгновенно возродиться на поле боя после гибели с полным запасом здоровья и маны.|n|n"
        "|cffa6afb8Уровень 1:|r время восстановления: |cffffffff240|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|r время восстановления: |cffffffff180|cffced4da сек.|r"
    )
    wts_updates[8229] = "|cffe4cfa3Реинкарнация|r [|cffffffff1|r]"
    wts_updates[13519] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно воскрешает героя после гибели. Время восстановления: |cffffffff240|cffced4da сек.|r"
    wts_updates[8230] = "|cffe4cfa3Реинкарнация|r [|cffffffff2|r]"
    wts_updates[13518] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно воскрешает героя после гибели. Время восстановления: |cffffffff180|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0BC", "field": "name", "expected": wts_updates[8226]})
    checks_def.append({"type": "ability", "id": "A0BC", "field": "tip1", "expected": wts_updates[8229]})
    checks_def.append({"type": "ability", "id": "A0BC", "field": "ubertip1", "expected": wts_updates[13519]})
    checks_def.append({"type": "ability", "id": "A0BC", "field": "tip2", "expected": wts_updates[8230]})
    checks_def.append({"type": "ability", "id": "A0BC", "field": "ubertip2", "expected": wts_updates[13518]})

    # --- N00Z Темный волшебник ---
    # A0BD: Взрыв бездны (Q)
    wts_updates[8246] = "|cffe4cfa3Взрыв бездны|r"
    wts_updates[8247] = "|cffe4cfa3Взрыв бездны|r"
    wts_updates[12938] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт столб тёмного пламени Бездны, наносящий периодический урон наземным войскам в указанной области.|n|n"
        "|cffa6afb8Уровень 1:|r наносит |cffe69a8d45|cffced4da урона/сек. в первые |cffffffff3|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|r наносит |cffe69a8d80|cffced4da урона/сек. в первые |cffffffff3|cffced4da сек.|n"
        "|cffa6afb8Уровень 3:|r наносит |cffe69a8d110|cffced4da урона/сек. в первые |cffffffff3|cffced4da сек.|n"
        "|cffa6afb8Уровень 4:|r наносит |cffe69a8d140|cffced4da урона/сек. в первые |cffffffff4|cffced4da сек.|r"
    )
    bd_tips = [12931, 12932, 12933, 12930]
    bd_ubs = [13521, 13529, 13532, 13520]
    bd_dmgs = [45, 80, 110, 140]
    bd_times = [3, 3, 3, 4]
    for lvl in range(1, 5):
        wts_updates[bd_tips[lvl-1]] = f"|cffe4cfa3Взрыв бездны|r [|cffffffff{lvl}|r] (|cffffffffQ|r)"
        wts_updates[bd_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным войскам в области |cffe69a8d{bd_dmgs[lvl-1]}|cffced4da урона/сек. в течение |cffffffff{bd_times[lvl-1]}|cffced4da сек. Поражённые войска продолжают получать периодический урон.|r"
        )
        checks_def.append({"type": "ability", "id": "A0BD", "field": f"tip{lvl}", "expected": wts_updates[bd_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0BD", "field": f"ubertip{lvl}", "expected": wts_updates[bd_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0BD", "field": "name", "expected": wts_updates[8246]})

    # A0BE: Рассеивание заклинаний (W)
    wts_updates[8252] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[8254] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[15470] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает положительные эффекты с войск в указанной области и наносит урон призванным существам.|n|n"
        "|cffa6afb8Уровень 1:|r наносит |cffe69a8d200|cffced4da урона призывам.|n"
        "|cffa6afb8Уровень 2:|r наносит |cffe69a8d300|cffced4da урона призывам.|n"
        "|cffa6afb8Уровень 3:|r наносит |cffe69a8d400|cffced4da урона призывам.|n"
        "|cffa6afb8Уровень 4:|r наносит |cffe69a8d600|cffced4da урона призывам.|r"
    )
    be_tips = [8253, 8256, 8257, 8258]
    be_ubs = [15474, 15471, 15472, 13534]
    be_dmgs = [200, 300, 400, 600]
    for lvl in range(1, 5):
        wts_updates[be_tips[lvl-1]] = f"|cffe4cfa3Рассеивание заклинаний|r [|cffffffff{lvl}|r] (|cffffffffW|r)"
        wts_updates[be_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Рассеивает магические эффекты в указанной области и наносит |cffe69a8d{be_dmgs[lvl-1]}|cffced4da урона призванным существам.|r"
        )
        checks_def.append({"type": "ability", "id": "A0BE", "field": f"tip{lvl}", "expected": wts_updates[be_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0BE", "field": f"ubertip{lvl}", "expected": wts_updates[be_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0BE", "field": "name", "expected": wts_updates[8252]})

    # A0BF: Замедляющий яд (passive)
    wts_updates[8263] = "|cffe4cfa3Замедляющий яд|r"
    wts_updates[8264] = "|cffe4cfa3Замедляющий яд|r"
    wts_updates[15475] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отравляет атакованных противников ядом Бездны, замедляя их скорость и нанося периодический урон.|n|n"
        "|cffa6afb8Уровень 1:|r замедляет атаку на |cffe69a8d25%|cffced4da, скорость на |cffe69a8d50%|cffced4da, наносит |cffe69a8d4|cffced4da урона/сек.|n"
        "|cffa6afb8Уровень 2:|r замедляет атаку на |cffe69a8d35%|cffced4da, скорость на |cffe69a8d50%|cffced4da, наносит |cffe69a8d5|cffced4da урона/сек.|n"
        "|cffa6afb8Уровень 3:|r замедляет атаку на |cffe69a8d45%|cffced4da, скорость на |cffe69a8d50%|cffced4da, наносит |cffe69a8d6|cffced4da урона/сек.|n"
        "|cffa6afb8Уровень 4:|r замедляет атаку на |cffe69a8d55%|cffced4da, скорость на |cffe69a8d50%|cffced4da, наносит |cffe69a8d7|cffced4da урона/сек.|r"
    )
    bf_tips = [8266, 8267, 8269, 8268]
    bf_ubs = [15479, 15476, 15477, 15478]
    bf_aslow = [25, 35, 45, 55]
    bf_dots = [4, 5, 6, 7]
    for lvl in range(1, 5):
        wts_updates[bf_tips[lvl-1]] = f"|cffe4cfa3Замедляющий яд|r [|cffffffff{lvl}|r]"
        wts_updates[bf_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки отравляют цель, снижая скорость атаки на |cffe69a8d{bf_aslow[lvl-1]}%|cffced4da, передвижения на |cffe69a8d50%|cffced4da и нанося |cffe69a8d{bf_dots[lvl-1]}|cffced4da урона/сек.|r"
        )
        checks_def.append({"type": "ability", "id": "A0BF", "field": f"tip{lvl}", "expected": wts_updates[bf_tips[lvl-1]]})
        checks_def.append({"type": "ability", "id": "A0BF", "field": f"ubertip{lvl}", "expected": wts_updates[bf_ubs[lvl-1]]})
    checks_def.append({"type": "ability", "id": "A0BF", "field": "name", "expected": wts_updates[8263]})

    # A0B7: Призыв Забытого (R, ultimate)
    wts_updates[8169] = "|cffe4cfa3Призыв Забытого|r"
    wts_updates[10179] = "|cffe4cfa3Призыв Забытого|r"
    wts_updates[10197] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из глубин древнего Забытого, способного порождать щупальца и уничтожать армии врагов.|n|n"
        "|cffa6afb8Уровень 1:|r призывает |cffffffff1|cffced4da Забытого.|n"
        "|cffa6afb8Уровень 2:|r призывает |cffffffff3|cffced4da Забытых.|r"
    )
    wts_updates[8170] = "|cffe4cfa3Призыв Забытого|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[10178] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff1|cffced4da могучего Забытого, способного атаковать врагов и порождать щупальца.|r"
    wts_updates[8172] = "|cffe4cfa3Призыв Забытого|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[10177] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff3|cffced4da могучих Забытых, способных атаковать врагов и порождать щупальца.|r"
    checks_def.append({"type": "ability", "id": "A0B7", "field": "name", "expected": wts_updates[8169]})
    checks_def.append({"type": "ability", "id": "A0B7", "field": "tip1", "expected": wts_updates[8170]})
    checks_def.append({"type": "ability", "id": "A0B7", "field": "ubertip1", "expected": wts_updates[10178]})
    checks_def.append({"type": "ability", "id": "A0B7", "field": "tip2", "expected": wts_updates[8172]})
    checks_def.append({"type": "ability", "id": "A0B7", "field": "ubertip2", "expected": wts_updates[10177]})

    # =========================================================================
    # 7. UNIT ABILITIES (20 abilities)
    # =========================================================================
    # A01Z: Коррозия бездны (passive)
    wts_updates[1936] = "|cffe4cfa3Коррозия бездны|r"
    wts_updates[1937] = "|cffe4cfa3Коррозия бездны|r"
    wts_updates[1938] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки разъедают плоть и броню цели, нанося периодический урон в течение |cffffffff5|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A01Z", "field": "name", "expected": wts_updates[1936]})
    checks_def.append({"type": "ability", "id": "A01Z", "field": "tip1", "expected": wts_updates[1937]})
    checks_def.append({"type": "ability", "id": "A01Z", "field": "ubertip1", "expected": wts_updates[1938]})

    # A09Q: Тяжелые удары (passive)
    wts_updates[6819] = "|cffe4cfa3Тяжелые удары|r"
    wts_updates[6820] = "|cffe4cfa3Тяжелые удары|r"
    wts_updates[20136] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон от атак по целям с тяжёлой бронёй и даёт шанс оглушить противника при ударе.|r"
    checks_def.append({"type": "ability", "id": "A09Q", "field": "name", "expected": wts_updates[6819]})
    checks_def.append({"type": "ability", "id": "A09Q", "field": "tip1", "expected": wts_updates[6820]})
    checks_def.append({"type": "ability", "id": "A09Q", "field": "ubertip1", "expected": wts_updates[20136]})

    # A09R: Порча (T)
    wts_updates[6823] = "|cffe4cfa3Порча|r"
    wts_updates[6824] = "|cffe4cfa3Порча|r (|cffffffffT|r)"
    wts_updates[7658] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает на врага проклятие порчи, наносящее периодический урон цели.|r"
    checks_def.append({"type": "ability", "id": "A09R", "field": "name", "expected": wts_updates[6823]})
    checks_def.append({"type": "ability", "id": "A09R", "field": "tip1", "expected": wts_updates[6824]})
    checks_def.append({"type": "ability", "id": "A09R", "field": "ubertip1", "expected": wts_updates[7658]})

    # A09S: Замедление (W)
    wts_updates[6826] = "|cffe4cfa3Замедление|r"
    wts_updates[6827] = "|cffe4cfa3Замедление|r (|cffffffffW|r)"
    wts_updates[39177] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает скорость перемещения цели на |cffe69a8d35%|cffced4da и скорость атаки на |cffe69a8d25%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A09S", "field": "name", "expected": wts_updates[6826]})
    checks_def.append({"type": "ability", "id": "A09S", "field": "tip1", "expected": wts_updates[6827]})
    checks_def.append({"type": "ability", "id": "A09S", "field": "ubertip1", "expected": wts_updates[39177]})

    # A09T: Опутывание (E)
    wts_updates[6830] = "|cffe4cfa3Опутывание|r"
    wts_updates[6831] = "|cffe4cfa3Опутывание|r (|cffffffffE|r)"
    wts_updates[6829] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Притягивает цель к земле и обездвиживает её на |cffffffff8|cffced4da сек. Опутанные воздушные цели считаются наземными.|r"
    checks_def.append({"type": "ability", "id": "A09T", "field": "name", "expected": wts_updates[6830]})
    checks_def.append({"type": "ability", "id": "A09T", "field": "tip1", "expected": wts_updates[6831]})
    checks_def.append({"type": "ability", "id": "A09T", "field": "ubertip1", "expected": wts_updates[6829]})

    # A09U: Опутывание (W)
    wts_updates[6832] = "|cffe4cfa3Опутывание|r"
    wts_updates[6834] = "|cffe4cfa3Опутывание|r (|cffffffffW|r)"
    wts_updates[965] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Притягивает цель к земле и обездвиживает её на |cffffffff8|cffced4da сек. Опутанные воздушные цели считаются наземными.|r"
    checks_def.append({"type": "ability", "id": "A09U", "field": "name", "expected": wts_updates[6832]})
    checks_def.append({"type": "ability", "id": "A09U", "field": "tip1", "expected": wts_updates[6834]})
    checks_def.append({"type": "ability", "id": "A09U", "field": "ubertip1", "expected": wts_updates[965]})

    # A09V: Жажда крови (W)
    wts_updates[6836] = "|cffe4cfa3Жажда крови|r"
    wts_updates[6837] = "|cffe4cfa3Жажда крови|r (|cffffffffW|r)"
    checks_def.append({"type": "ability", "id": "A09V", "field": "name", "expected": wts_updates[6836]})
    checks_def.append({"type": "ability", "id": "A09V", "field": "tip1", "expected": wts_updates[6837]})

    # A09W: Благодать древних богов (Q)
    wts_updates[6839] = "|cffe4cfa3Благодать древних богов|r"
    wts_updates[6841] = "|cffe4cfa3Благодать древних богов|r (|cffffffffQ|r)"
    wts_updates[4102] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье союзным бойцам поблизости.|r"
    checks_def.append({"type": "ability", "id": "A09W", "field": "name", "expected": wts_updates[6839]})
    checks_def.append({"type": "ability", "id": "A09W", "field": "tip1", "expected": wts_updates[6841]})
    checks_def.append({"type": "ability", "id": "A09W", "field": "ubertip1", "expected": wts_updates[4102]})

    # A09X: Затуманенный рассудок (E)
    wts_updates[6843] = "|cffe4cfa3Затуманенный рассудок|r"
    wts_updates[6844] = "|cffe4cfa3Затуманенный рассудок|r (|cffffffffE|r)"
    checks_def.append({"type": "ability", "id": "A09X", "field": "name", "expected": wts_updates[6843]})
    checks_def.append({"type": "ability", "id": "A09X", "field": "tip1", "expected": wts_updates[6844]})

    # A09Z: Знамя Культа (passive aura)
    wts_updates[6855] = "|cffe4cfa3Знамя Культа|r"
    wts_updates[6869] = "|cffe4cfa3Знамя Культа|r"
    checks_def.append({"type": "ability", "id": "A09Z", "field": "name", "expected": wts_updates[6855]})
    checks_def.append({"type": "ability", "id": "A09Z", "field": "tip1", "expected": wts_updates[6869]})

    # A0A0: Выносливость (passive)
    wts_updates[6857] = "|cffe4cfa3Выносливость|r"
    wts_updates[6858] = "|cffe4cfa3Выносливость|r"
    wts_updates[6859] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает максимальный запас здоровья воина.|r"
    wts_updates[6860] = "|cffe4cfa3Выносливость|r"
    wts_updates[6861] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает максимальный запас здоровья воина.|r"
    checks_def.append({"type": "ability", "id": "A0A0", "field": "name", "expected": wts_updates[6857]})
    checks_def.append({"type": "ability", "id": "A0A0", "field": "tip1", "expected": wts_updates[6858]})
    checks_def.append({"type": "ability", "id": "A0A0", "field": "ubertip1", "expected": wts_updates[6859]})

    # A0A1: Выносливость (passive)
    wts_updates[6863] = "|cffe4cfa3Выносливость|r"
    wts_updates[6864] = "|cffe4cfa3Выносливость|r"
    wts_updates[6865] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает максимальный запас здоровья воина.|r"
    checks_def.append({"type": "ability", "id": "A0A1", "field": "name", "expected": wts_updates[6863]})
    checks_def.append({"type": "ability", "id": "A0A1", "field": "tip1", "expected": wts_updates[6864]})
    checks_def.append({"type": "ability", "id": "A0A1", "field": "ubertip1", "expected": wts_updates[6865]})

    # A0A2: Защита Бездны (passive)
    wts_updates[6871] = "|cffe4cfa3Защита Бездны|r"
    wts_updates[6872] = "|cffe4cfa3Защита Бездны|r"
    wts_updates[13114] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Тёмный панцирь снижает весь получаемый магический урон.|r"
    checks_def.append({"type": "ability", "id": "A0A2", "field": "name", "expected": wts_updates[6871]})
    checks_def.append({"type": "ability", "id": "A0A2", "field": "tip1", "expected": wts_updates[6872]})
    checks_def.append({"type": "ability", "id": "A0A2", "field": "ubertip1", "expected": wts_updates[13114]})

    # A0AI: Ярость Бездны (D)
    wts_updates[7632] = "|cffe4cfa3Ярость Бездны|r"
    wts_updates[7633] = "|cffe4cfa3Ярость Бездны|r (|cffffffffD|r)"
    wts_updates[40957] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки на |cffc8e087+50%|cffced4da и скорость передвижения на |cffc8e087+20%|cffced4da, но увеличивает получаемый урон на |cffe69a8d+10%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0AI", "field": "name", "expected": wts_updates[7632]})
    checks_def.append({"type": "ability", "id": "A0AI", "field": "tip1", "expected": wts_updates[7633]})
    checks_def.append({"type": "ability", "id": "A0AI", "field": "ubertip1", "expected": wts_updates[40957]})

    # A0AJ: Аура поглощения (passive aura)
    wts_updates[7638] = "|cffe4cfa3Аура поглощения|r"
    wts_updates[7639] = "|cffe4cfa3Аура поглощения|r"
    wts_updates[40958] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Союзные бойцы ближнего боя поблизости восполняют здоровье в объёме |cffc8e0877%|cffced4da от наносимого урона.|r"
    checks_def.append({"type": "ability", "id": "A0AJ", "field": "name", "expected": wts_updates[7638]})
    checks_def.append({"type": "ability", "id": "A0AJ", "field": "tip1", "expected": wts_updates[7639]})
    checks_def.append({"type": "ability", "id": "A0AJ", "field": "ubertip1", "expected": wts_updates[40958]})

    # A0AK: Дробящий удар (passive)
    wts_updates[7640] = "|cffe4cfa3Дробящий удар|r"
    wts_updates[7641] = "|cffe4cfa3Дробящий удар|r"
    wts_updates[7642] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит дробящий удар при атаке, снижая скорость атаки и передвижения цели.|r"
    checks_def.append({"type": "ability", "id": "A0AK", "field": "name", "expected": wts_updates[7640]})
    checks_def.append({"type": "ability", "id": "A0AK", "field": "tip1", "expected": wts_updates[7641]})
    checks_def.append({"type": "ability", "id": "A0AK", "field": "ubertip1", "expected": wts_updates[7642]})

    # A0AL: Порождение щупальца (Q)
    wts_updates[1950] = "|cffe4cfa3Порождение щупальца|r"
    wts_updates[7643] = "|cffe4cfa3Порождение щупальца|r (|cffffffffQ|r)"
    wts_updates[15189] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из-под земли могучее щупальце, атакующее противников.|r"
    checks_def.append({"type": "ability", "id": "A0AL", "field": "name", "expected": wts_updates[1950]})
    checks_def.append({"type": "ability", "id": "A0AL", "field": "tip1", "expected": wts_updates[7643]})
    checks_def.append({"type": "ability", "id": "A0AL", "field": "ubertip1", "expected": wts_updates[15189]})

    # A0AM: Эссенция бездны (W)
    wts_updates[7645] = "|cffe4cfa3Эссенция бездны|r"
    wts_updates[7719] = "|cffe4cfa3Эссенция бездны|r (|cffffffffW|r)"
    checks_def.append({"type": "ability", "id": "A0AM", "field": "name", "expected": wts_updates[7645]})
    checks_def.append({"type": "ability", "id": "A0AM", "field": "tip1", "expected": wts_updates[7719]})

    # A0AN: Порченные снаряды (passive)
    wts_updates[7655] = "|cffe4cfa3Порченные снаряды|r"
    wts_updates[7659] = "|cffe4cfa3Порченные снаряды|r"
    checks_def.append({"type": "ability", "id": "A0AN", "field": "name", "expected": wts_updates[7655]})
    checks_def.append({"type": "ability", "id": "A0AN", "field": "tip1", "expected": wts_updates[7659]})

    # A1QQ: Ярость maksikа (R)
    wts_updates[31775] = "|cffe4cfa3Ярость maksikа|r"
    wts_updates[31777] = "|cffe4cfa3Ярость maksikа|r (|cffffffffR|r)"
    wts_updates[31778] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Рассеивает положительные эффекты с врагов и наносит |cffe69a8d200|cffced4da урона призванным существам.|r"
    checks_def.append({"type": "ability", "id": "A1QQ", "field": "name", "expected": wts_updates[31775]})
    checks_def.append({"type": "ability", "id": "A1QQ", "field": "tip1", "expected": wts_updates[31777]})
    checks_def.append({"type": "ability", "id": "A1QQ", "field": "ubertip1", "expected": wts_updates[31778]})

    # =========================================================================
    # 8. BUFFS (11 buffs)
    # =========================================================================
    wts_updates[6867] = "|cffe4cfa3Порча|r"
    wts_updates[6868] = "|cffe4cfa3Порча|r"
    wts_updates[7649] = "|cffe4cfa3Дробящий удар|r"
    wts_updates[7650] = "|cffe4cfa3Дробящий удар|r"
    wts_updates[8183] = "|cffe4cfa3Нечистая аура|r"
    wts_updates[8184] = "|cffa6afb8ЭФФЕКТ:|cffced4da Регенерация здоровья цели |cffe69a8dснижена|cffced4da.|r"
    wts_updates[1943] = "|cffe4cfa3Коррозия бездны|r"
    wts_updates[1944] = "|cffe4cfa3Коррозия бездны|r"
    wts_updates[7648] = "|cffe4cfa3Аура поглощения|r"
    wts_updates[7763] = "|cffe4cfa3Щупальце|r"
    wts_updates[7660] = "|cffe4cfa3Порченные снаряды|r"

    checks_def.append({"type": "buff", "id": "B025", "field": "bufftip", "expected": wts_updates[6867]})
    checks_def.append({"type": "buff", "id": "B026", "field": "bufftip", "expected": wts_updates[6868]})
    checks_def.append({"type": "buff", "id": "B02C", "field": "bufftip", "expected": wts_updates[7649]})
    checks_def.append({"type": "buff", "id": "B02D", "field": "bufftip", "expected": wts_updates[7650]})
    checks_def.append({"type": "buff", "id": "B02K", "field": "bufftip", "expected": wts_updates[8183]})
    checks_def.append({"type": "buff", "id": "B02K", "field": "buffubertip", "expected": wts_updates[8184]})
    checks_def.append({"type": "buff", "id": "B00A", "field": "bufftip", "expected": wts_updates[1943]})
    checks_def.append({"type": "buff", "id": "B00B", "field": "bufftip", "expected": wts_updates[1944]})
    checks_def.append({"type": "buff", "id": "B02B", "field": "bufftip", "expected": wts_updates[7648]})
    checks_def.append({"type": "buff", "id": "B02G", "field": "bufftip", "expected": wts_updates[7763]})
    checks_def.append({"type": "buff", "id": "B02E", "field": "bufftip", "expected": wts_updates[7660]})

    categories = {
        "selection": ["A0HX"],
        "markers": ["R07K", "R0KD"],
        "buildings": [
            "o00K", "o00T", "o00L", "o00R", "o00V", "o00P", "o00U", "o00Q", "h0D3"
        ],
        "units": [
            "o00J", "o00M", "o00N", "o00S", "o002", "u004", "n00R", "n00U",
            "n00D", "n00C", "o00O", "n00S", "u005"
        ],
        "heroes": ["O011", "N010", "N00Z"],
        "upgrades": [
            "R07K", "R0KD",
            "R04D", "R04V", "R00O", "R04S", "R04U", "R0EJ", "R05S", "R05T",
            "R05U", "R05V", "R04Z", "R050", "R051", "R052", "R04W", "R04X"
        ],
        "abilities": [
            "A0HX", "A01Z", "A09Q", "A09R", "A09S", "A09T", "A09U", "A09V",
            "A09W", "A09X", "A0A0", "A0A1", "A0A2", "A0AI", "A0AJ", "A0AK",
            "A0AL", "A0AM", "A0AN", "A1QQ", "A09Z",
            "A0AO", "A0AP", "A0B6", "A0B8",
            "A0B9", "A0BA", "A0BB", "A0BC",
            "A0BD", "A0BE", "A0BF", "A0B7"
        ],
        "buffs": [
            "B025", "B026", "B02C", "B02D", "B02K", "B00A", "B00B", "B02B",
            "B02G", "B02E", "B02L"
        ]
    }

    plan_payload = {
        "race": "Twilight Hammer",
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": categories
    }

    out_path = folder / "twilight_hammer_plan.json"
    out_path.write_text(json.dumps(plan_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Plan saved to {out_path}")
    print(f"Total WTS updates: {len(wts_updates)}")
    print(f"Total checks planned: {len(checks_def)}")

if __name__ == '__main__':
    main()
