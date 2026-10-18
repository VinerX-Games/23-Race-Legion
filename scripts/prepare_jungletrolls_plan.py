# -*- coding: utf-8 -*-
"""Prepare complete UI text standardization plan and registries for Jungle Trolls (Race 30)."""
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
    # 1. RACE SELECTION & FACTION MARKERS
    # =========================================================================
    # A1DZ: Выбор расы Тролли джунглей (C)
    wts_updates[32019] = "|cffe4cfa3Тролли джунглей|r"
    wts_updates[32430] = "|cffe4cfa3Тролли джунглей|r (|cffffffffC|r)"
    wts_updates[35186] = (
        "|cffa6afb8РАСА:|cffced4da Древняя цивилизация троллей Тернистой долины и островов Эхо, владеющая магией вуду, ядами и благословением свирепых Лоа.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«World of Warcraft: Classic» — «Battle for Azeroth»|r|n|n"
        "|cffced4daТролли джунглей — древнейшая раса Азерота, некогда создавшая великую империю Гурубаши. Расколотые на племена после падения империи, они сохранили непревзойдённые навыки засад, метания копий и тайны кровавой магии вуду. В критический момент вожди джунглей могут избрать путь верности Орде и Лоа Смерти Бвонсамди (племя Чёрного Копья) либо предаться первобытной кровавой ярости и возродить культ Кровавого бога Хаккара (империя Гурубаши).|r"
    )
    checks_def.append({"type": "ability", "id": "A1DZ", "field": "name", "expected": wts_updates[32019]})
    checks_def.append({"type": "ability", "id": "A1DZ", "field": "tip1", "expected": wts_updates[32430]})
    checks_def.append({"type": "ability", "id": "A1DZ", "field": "ubertip1", "expected": wts_updates[35186]})

    # R0IH: Маркер расы (Тролли джунглей)
    wts_updates[32049] = "|cffe4cfa3Тролли джунглей|r"
    wts_updates[32050] = "|cffe4cfa3Тролли джунглей|r"
    checks_def.append({"type": "upgrade", "id": "R0IH", "field": "name1", "expected": wts_updates[32049]})
    checks_def.append({"type": "upgrade", "id": "R0IH", "field": "tip1", "expected": wts_updates[32050]})

    # R0IR: Маркер подфракции Чёрного Копья
    wts_updates[32959] = "|cffe4cfa3Чёрное Копьё|r"
    wts_updates[32960] = "|cffe4cfa3Чёрное Копьё|r"
    checks_def.append({"type": "upgrade", "id": "R0IR", "field": "name1", "expected": wts_updates[32959]})
    checks_def.append({"type": "upgrade", "id": "R0IR", "field": "tip1", "expected": wts_updates[32960]})

    # A1EP: Выбор подфракции Чёрного Копья (E)
    wts_updates[32646] = "|cffe4cfa3Чёрное Копьё|r"
    wts_updates[32647] = "|cffe4cfa3Чёрное Копьё|r (|cffffffffE|r)"
    wts_updates[32862] = (
        "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Избрать путь племени |cffa9c7deЧёрного Копья|cffced4da, союзников Орды. Открывает доступ к |cffa9c7deМагам Чёрного Копья|cffced4da и призыву |cffa9c7deЛоа Смерти Бвонсамди|cffced4da.|n|n"
        "|cffe6c07bВнимание:|cffced4da взаимоисключающий выбор с империей Гурубаши.|r"
    )
    checks_def.append({"type": "ability", "id": "A1EP", "field": "name", "expected": wts_updates[32646]})
    checks_def.append({"type": "ability", "id": "A1EP", "field": "tip1", "expected": wts_updates[32647]})
    checks_def.append({"type": "ability", "id": "A1EP", "field": "ubertip1", "expected": wts_updates[32862]})

    # A1EQ: Выбор подфракции Гурубаши (R)
    wts_updates[32650] = "|cffe4cfa3Империя Гурубаши|r"
    wts_updates[32651] = "|cffe4cfa3Империя Гурубаши|r (|cffffffffR|r)"
    wts_updates[32863] = (
        "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Избрать путь древней империи |cffa9c7deГурубаши|cffced4da. Открывает доступ к |cffa9c7deКолдунам Вуду|cffced4da и призыву |cffa9c7deХаккара Свежевателя Душ|cffced4da.|n|n"
        "|cffe6c07bВнимание:|cffced4da взаимоисключающий выбор с Чёрным Копьём.|r"
    )
    checks_def.append({"type": "ability", "id": "A1EQ", "field": "name", "expected": wts_updates[32650]})
    checks_def.append({"type": "ability", "id": "A1EQ", "field": "tip1", "expected": wts_updates[32651]})
    checks_def.append({"type": "ability", "id": "A1EQ", "field": "ubertip1", "expected": wts_updates[32863]})

    # =========================================================================
    # 2. BUILDINGS (10 buildings)
    # =========================================================================
    # h0N5: Дом вождей (Q)
    wts_updates[31502] = "|cffe4cfa3Дом вождей|r"
    wts_updates[32078] = "|cffe4cfa3Дом вождей|r (|cffffffffQ|r)"
    wts_updates[33542] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Троллей джунглей первой ступени. Обеспечивает запас пищи, добычу ресурсов и выбор направления развития расы.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРемесленник|cffced4da: рабочий, добывающий древесину и возводящий строения.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЧёрное Копьё|cffced4da: союз с Ордой, доступ к магам и Бвонсамди.|n"
        "- |cffa9c7deИмперия Гурубаши|cffced4da: культ крови, доступ к колдунам вуду и Хаккару.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКрепость вождей|cffced4da: открывает доступ к передовым сооружениям и войскам.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N5", "field": "name", "expected": wts_updates[31502]})
    checks_def.append({"type": "unit", "id": "h0N5", "field": "tip", "expected": wts_updates[32078]})
    checks_def.append({"type": "unit", "id": "h0N5", "field": "ubertip", "expected": wts_updates[33542]})

    # h0N1: Крепость вождей (Z)
    wts_updates[31529] = "|cffe4cfa3Крепость вождей|r"
    wts_updates[32053] = "|cffe4cfa3Крепость вождей|r (|cffffffffZ|r)"
    wts_updates[32605] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Троллей джунглей второй ступени. Существенно увеличивает запас пищи и открывает доступ к новым постройкам.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРемесленник|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЦитадель вождей|cffced4da: открывает доступ к высшим технологиям и защите столицы.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N1", "field": "name", "expected": wts_updates[31529]})
    checks_def.append({"type": "unit", "id": "h0N1", "field": "tip", "expected": wts_updates[32053]})
    checks_def.append({"type": "unit", "id": "h0N1", "field": "ubertip", "expected": wts_updates[32605]})

    # h0N6: Цитадель вождей (Z)
    wts_updates[31543] = "|cffe4cfa3Цитадель вождей|r"
    wts_updates[32348] = "|cffe4cfa3Цитадель вождей|r (|cffffffffZ|r)"
    wts_updates[32615] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Троллей джунглей третьей ступени. Обеспечивает максимальный запас пищи и защиту племени.|n|n"
        "Даёт |cffffffff160|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРемесленник|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗащита столицы|cffced4da: укрепляет оборону главного здания.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N6", "field": "name", "expected": wts_updates[31543]})
    checks_def.append({"type": "unit", "id": "h0N6", "field": "tip", "expected": wts_updates[32348]})
    checks_def.append({"type": "unit", "id": "h0N6", "field": "ubertip", "expected": wts_updates[32615]})

    # h0N2: Жилище (A)
    wts_updates[31506] = "|cffe4cfa3Жилище|r"
    wts_updates[32505] = "|cffe4cfa3Жилище|r (|cffffffffA|r)"
    wts_updates[32612] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое жилище троллей. Обеспечивает лимит пищи, приносит регулярный доход золота и способно обороняться дистанционными атаками.|n|n"
        "Даёт |cffffffff10|cffced4da ед. лимита пищи.|n"
        "Приносит регулярный доход золота каждые |cffffffff25|cffced4da сек.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N2", "field": "name", "expected": wts_updates[31506]})
    checks_def.append({"type": "unit", "id": "h0N2", "field": "tip", "expected": wts_updates[32505]})
    checks_def.append({"type": "unit", "id": "h0N2", "field": "ubertip", "expected": wts_updates[32612]})

    # h0MY: Казармы (W)
    wts_updates[31497] = "|cffe4cfa3Казармы|r"
    wts_updates[31207] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[33540] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военный лагерь для подготовки пехоты, стрелков и осадных орудий Троллей джунглей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deВоитель|cffced4da: выносливый пехотинец ближнего боя.|n"
        "- |cffa9c7deОхотник за головами|cffced4da: меткий копейщик дальнего боя.|n"
        "- |cffa9c7deКатапульта|cffced4da: осадное орудие для разрушения укреплений.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЭликсиры жизни|cffced4da: увеличивает запас здоровья воителей и охотников.|n"
        "- |cffa9c7deОтравленные копья|cffced4da: наделяет стрелков отравляющей атакой.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MY", "field": "name", "expected": wts_updates[31497]})
    checks_def.append({"type": "unit", "id": "h0MY", "field": "tip", "expected": wts_updates[31207]})
    checks_def.append({"type": "unit", "id": "h0MY", "field": "ubertip", "expected": wts_updates[33540]})

    # h0MW: Колизей (D)
    wts_updates[31494] = "|cffe4cfa3Колизей|r"
    wts_updates[32076] = "|cffe4cfa3Колизей|r (|cffffffffD|r)"
    wts_updates[31956] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Арена и питомник для приручения свирепых зверей и подготовки тяжёлых бойцов джунглей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deНаездник|cffced4da: мобильный кавалерист, переключающийся между дальним и ближним боем.|n"
        "- |cffa9c7deБерсерк|cffced4da: свирепый гигант с огромным запасом здоровья и оглушающими ударами.|n"
        "- |cffa9c7deГидра|cffced4da: могучее чудовище дальнего боя с ядовитым дыханием.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deДрессировка животных|cffced4da: повышает скорость наездников и гидр.|n"
        "- |cffa9c7deЧары гидр|cffced4da: разделение погибшей гидры на малых гидр.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MW", "field": "name", "expected": wts_updates[31494]})
    checks_def.append({"type": "unit", "id": "h0MW", "field": "tip", "expected": wts_updates[32076]})
    checks_def.append({"type": "unit", "id": "h0MW", "field": "ubertip", "expected": wts_updates[31956]})

    # h0MX: Обитель (R)
    wts_updates[31495] = "|cffe4cfa3Обитель|r"
    wts_updates[32341] = "|cffe4cfa3Обитель|r (|cffffffffR|r)"
    wts_updates[32271] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Святилище духов вуду и тайных искусств Троллей джунглей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЖрец|cffced4da: маг поддержки с жаждой крови и рассеиванием.|n"
        "- |cffa9c7deЗнахарь|cffced4da: мастер тотемов исцеления, стазиса и разведки.|n"
        "- |cffa9c7deКолдун Вуду|cffced4da: боевой маг Гурубаши с тёмными проклятиями и сглазом.|n"
        "- |cffa9c7deМаг Чёрного Копья|cffced4da: чародей льда с бураном и морозным доспехом.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбучение жрецов|cffced4da|n"
        "- |cffa9c7deОбучение знахарей|cffced4da|n"
        "- |cffa9c7deОбучение высших магов|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MX", "field": "name", "expected": wts_updates[31495]})
    checks_def.append({"type": "unit", "id": "h0MX", "field": "tip", "expected": wts_updates[32341]})
    checks_def.append({"type": "unit", "id": "h0MX", "field": "ubertip", "expected": wts_updates[32271]})

    # h0N0: Алтарь Крови (S)
    wts_updates[31499] = "|cffe4cfa3Алтарь Крови|r"
    wts_updates[31235] = "|cffe4cfa3Алтарь Крови|r (|cffffffffS|r)"
    wts_updates[32604] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священный алтарь духов и предков. Позволяет призывать и воскрешать героев Троллей джунглей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТемный охотник|cffced4da: герой поддержки и контроля.|n"
        "- |cffa9c7deМастер клинка|cffced4da: ловкий боец передовой с вихрем клинков.|n"
        "- |cffa9c7deНизвергатель|cffced4da: могущественный боевой маг разрушения.|n"
        "- |cffa9c7deХаккар Свежеватель Душ|cffced4da: легендарный кровавый бог Гурубаши.|n"
        "- |cffa9c7deЛоа Смерти Бвонсамди|cffced4da: легендарный покровитель Чёрного Копья.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N0", "field": "name", "expected": wts_updates[31499]})
    checks_def.append({"type": "unit", "id": "h0N0", "field": "tip", "expected": wts_updates[31235]})
    checks_def.append({"type": "unit", "id": "h0N0", "field": "ubertip", "expected": wts_updates[32604]})

    # h0N3: Лесопилка (E)
    wts_updates[31958] = "|cffe4cfa3Лесопилка|r"
    wts_updates[31311] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[32613] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр обработки древесины и кузница племени. Принимает добытую древесину и разрабатывает базовые улучшения армии.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deСтальное оружие|cffced4da: повышает урон немагических войск.|n"
        "- |cffa9c7deСтальная броня|cffced4da: повышает защиту всех войск.|n"
        "- |cffa9c7deМетоды регенерации|cffced4da: ускоряет восстановление здоровья.|n"
        "- |cffa9c7deУлучшенные топоры|cffced4da: увеличивает сбор древесины.|n"
        "- |cffa9c7deКорпуса построек|cffced4da: укрепляет здания.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N3", "field": "name", "expected": wts_updates[31958]})
    checks_def.append({"type": "unit", "id": "h0N3", "field": "tip", "expected": wts_updates[31311]})
    checks_def.append({"type": "unit", "id": "h0N3", "field": "ubertip", "expected": wts_updates[32613]})

    # =========================================================================
    # 3. UNITS (14 units)
    # =========================================================================
    # o04Q: Ремесленник (Q)
    wts_updates[30969] = "|cffe4cfa3Ремесленник|r"
    wts_updates[31177] = "|cffe4cfa3Ремесленник|r (|cffffffffQ|r)"
    wts_updates[28587] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Троллей джунглей. Добывает древесину, возводит и ремонтирует постройки племени.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНебольшой скачок|cffced4da: мгновенный телепорт на короткое расстояние.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: ускоренное восстановление здоровья.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04Q", "field": "name", "expected": wts_updates[30969]})
    checks_def.append({"type": "unit", "id": "o04Q", "field": "tip", "expected": wts_updates[31177]})
    checks_def.append({"type": "unit", "id": "o04Q", "field": "ubertip", "expected": wts_updates[28587]})

    # o04M: Воитель (W)
    wts_updates[30951] = "|cffe4cfa3Воитель|r"
    wts_updates[31952] = "|cffe4cfa3Воитель|r (|cffffffffW|r)"
    wts_updates[14341] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стойкий боец ближнего боя. Может использовать боевой эликсир для резкого ускорения атаки и перемещения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБодрящий эликсир|cffced4da: расходует |cffe69a8d75|cffced4da ед. здоровья, взамен временно значительно увеличивая скорость атаки и передвижения.|n"
        "- |cffa9c7deЯрость Джунглей|cffced4da: увеличивает наносимый урон при потере здоровья.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: быстрое восстановление здоровья вне боя.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04M", "field": "name", "expected": wts_updates[30951]})
    checks_def.append({"type": "unit", "id": "o04M", "field": "tip", "expected": wts_updates[31952]})
    checks_def.append({"type": "unit", "id": "o04M", "field": "ubertip", "expected": wts_updates[14341]})

    # o05K: Воитель (ярость) (W)
    wts_updates[32351] = "|cffe4cfa3Воитель (ярость)|r"
    wts_updates[32352] = "|cffe4cfa3Воитель (ярость)|r (|cffffffffW|r)"
    wts_updates[32281] = (
        "|cffa6afb8ЮНИТ:|cffced4da Воитель, находящийся под действием «Бодрящего эликсира». Обладает повышенной скоростью боя и передвижения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯрость Джунглей|cffced4da: увеличивает наносимый урон при потере здоровья.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: ускоренное восстановление здоровья.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05K", "field": "name", "expected": wts_updates[32351]})
    checks_def.append({"type": "unit", "id": "o05K", "field": "tip", "expected": wts_updates[32352]})
    checks_def.append({"type": "unit", "id": "o05K", "field": "ubertip", "expected": wts_updates[32281]})

    # o04L: Охотник за головами (Q)
    wts_updates[30948] = "|cffe4cfa3Охотник за головами|r"
    wts_updates[15178] = "|cffe4cfa3Охотник за головами|r (|cffffffffQ|r)"
    wts_updates[11854] = (
        "|cffa6afb8ЮНИТ:|cffced4da Меткий копьеметатель дальнего боя. Эффективен против пехоты и летающих противников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОтравленные копья|cffced4da: после исследования атаки отравляют цель, нанося |cffe69a8d5|cffced4da ед. урона/сек. в течение |cffffffff25|cffced4da сек.|n"
        "- |cffa9c7deЯрость Джунглей|cffced4da: усиливает урон при получении ранений.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: ускоренное восстановление здоровья.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04L", "field": "name", "expected": wts_updates[30948]})
    checks_def.append({"type": "unit", "id": "o04L", "field": "tip", "expected": wts_updates[15178]})
    checks_def.append({"type": "unit", "id": "o04L", "field": "ubertip", "expected": wts_updates[11854]})

    # o05E: Катапульта (E)
    wts_updates[31533] = "|cffe4cfa3Катапульта|r"
    wts_updates[31322] = "|cffe4cfa3Катапульта|r (|cffffffffE|r)"
    wts_updates[20162] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойная осадная машина троллей. Наносит сокрушительный осадный урон по площади, разрушая строения и пробивая укрепления врага.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05E", "field": "name", "expected": wts_updates[31533]})
    checks_def.append({"type": "unit", "id": "o05E", "field": "tip", "expected": wts_updates[31322]})
    checks_def.append({"type": "unit", "id": "o05E", "field": "ubertip", "expected": wts_updates[20162]})

    # o04O: Жрец (Q)
    wts_updates[15590] = "|cffe4cfa3Жрец|r"
    wts_updates[32304] = "|cffe4cfa3Жрец|r (|cffffffffQ|r)"
    wts_updates[15419] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг поддержки армии троллей. Усиливает союзников боевой яростью и ослабляет ряды противника чарами замедления.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЖажда крови|cffced4da: значительно ускоряет атаку и перемещение союзника.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает положительные эффекты с врагов и наносит урон призванным целям.|n"
        "- |cffa9c7deЗамедление|cffced4da: снижает скорость перемещения и атаки врага.|n"
        "- |cffa9c7deЖертва кровью|cffced4da: жертвует здоровьем ради мгновенного восстановления маны.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04O", "field": "name", "expected": wts_updates[15590]})
    checks_def.append({"type": "unit", "id": "o04O", "field": "tip", "expected": wts_updates[32304]})
    checks_def.append({"type": "unit", "id": "o04O", "field": "ubertip", "expected": wts_updates[15419]})

    # o04R: Знахарь (W)
    wts_updates[30621] = "|cffe4cfa3Знахарь|r"
    wts_updates[32314] = "|cffe4cfa3Знахарь|r (|cffffffffW|r)"
    wts_updates[15433] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мудрый шаман-тотемщик. Расставляет идолы, исцеляющие соратников, оглушающие врагов и разведывающие местность.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСтазисная ловушка|cffced4da: устанавливает невидимый тотем, оглушающий приближающихся врагов.|n"
        "- |cffa9c7deСторожевой идол|cffced4da: невидимый тотем разведки с истинным зрением, повышающий урон союзников на |cffc8e087+5|cffced4da.|n"
        "- |cffa9c7deИсцеляющий идол|cffced4da: тотем, восстанавливающий процент здоровья окружающим войскам.|n"
        "- |cffa9c7deЖертва кровью|cffced4da: восстанавливает ману за счёт запаса здоровья.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04R", "field": "name", "expected": wts_updates[30621]})
    checks_def.append({"type": "unit", "id": "o04R", "field": "tip", "expected": wts_updates[32314]})
    checks_def.append({"type": "unit", "id": "o04R", "field": "ubertip", "expected": wts_updates[15433]})

    # o04N: Колдун Вуду (E)
    wts_updates[27731] = "|cffe4cfa3Колдун Вуду|r"
    wts_updates[27825] = "|cffe4cfa3Колдун Вуду|r (|cffffffffE|r)"
    wts_updates[15417] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный маг империи Гурубаши. Владеет разрушительными чарами вуду, преобразует врагов в зверей и поднимает мстительных духов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУсиление вуду|cffced4da: наполняет атаки тёмным пламенем, нанося |cffc8e087+13|cffced4da ед. урона.|n"
        "- |cffa9c7deТёмный дух|cffced4da: поднимает из трупа неуязвимого дикого духа.|n"
        "- |cffa9c7deСглаз|cffced4da: превращает цель в беззащитное животное на |cffffffff15|cffced4da сек.|n"
        "- |cffa9c7deЖертва кровью|cffced4da: обмен здоровья на ману.|n|n"
        "|cffa6afb8Требуется выбор:|r |cffa9c7deИмперия Гурубаши|r.|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04N", "field": "name", "expected": wts_updates[27731]})
    checks_def.append({"type": "unit", "id": "o04N", "field": "tip", "expected": wts_updates[27825]})
    checks_def.append({"type": "unit", "id": "o04N", "field": "ubertip", "expected": wts_updates[15417]})

    # o04P: Маг Чёрного Копья (E)
    wts_updates[30965] = "|cffe4cfa3Маг Чёрного Копья|r"
    wts_updates[32306] = "|cffe4cfa3Маг Чёрного Копья|r (|cffffffffE|r)"
    wts_updates[15430] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный маг племени Чёрного Копья, обученный магии льда. Защищает союзников ледяным щитом и замораживает наступающих врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМорозный доспех|cffced4da: повышает броню цели и замедляет атакующих её в ближнем бою.|n"
        "- |cffa9c7deБуран|cffced4da: обрушивает ледяные волны, наносящие урон по площади.|n"
        "- |cffa9c7deЛедяные стрелы|cffced4da: замедляют цель при каждой атаке.|n|n"
        "|cffa6afb8Требуется выбор:|r |cffa9c7deЧёрное Копьё|r.|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04P", "field": "name", "expected": wts_updates[30965]})
    checks_def.append({"type": "unit", "id": "o04P", "field": "tip", "expected": wts_updates[32306]})
    checks_def.append({"type": "unit", "id": "o04P", "field": "ubertip", "expected": wts_updates[15430]})

    # o04S: Наездник (Q)
    wts_updates[31105] = "|cffe4cfa3Наездник|r"
    wts_updates[31957] = "|cffe4cfa3Наездник|r (|cffffffffQ|r)"
    wts_updates[20155] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый и манёвренный всадник. В дальнем бою метает копья, а при сближении с врагом может перейти в ближний бой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСменить дистанцию боя|cffced4da: переключает режим между дальним и ближним боем.|n"
        "- |cffa9c7deОтравленные копья|cffced4da: отравляет врагов при атаке в дальнем бою.|n"
        "- |cffa9c7deЯрость Джунглей|cffced4da: увеличивает урон при потере здоровья.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: быстрое восстановление здоровья.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04S", "field": "name", "expected": wts_updates[31105]})
    checks_def.append({"type": "unit", "id": "o04S", "field": "tip", "expected": wts_updates[31957]})
    checks_def.append({"type": "unit", "id": "o04S", "field": "ubertip", "expected": wts_updates[20155]})

    # o05J: Наездник (ближний бой) (A)
    wts_updates[32002] = "|cffe4cfa3Наездник (ближний бой)|r"
    wts_updates[32079] = "|cffe4cfa3Наездник (ближний бой)|r (|cffffffffA|r)"
    wts_updates[20166] = (
        "|cffa6afb8ЮНИТ:|cffced4da Наездник в режиме ближнего боя. Сражается тяжёлым копьём и может вернуться к дистанционному бою.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСменить дистанцию боя|cffced4da: возвращает всадника в режим дальнего боя.|n"
        "- |cffa9c7deЯрость Джунглей|cffced4da: увеличивает урон при потере здоровья.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: быстрое восстановление здоровья.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05J", "field": "name", "expected": wts_updates[32002]})
    checks_def.append({"type": "unit", "id": "o05J", "field": "tip", "expected": wts_updates[32079]})
    checks_def.append({"type": "unit", "id": "o05J", "field": "ubertip", "expected": wts_updates[20166]})

    # o04U: Берсерк (W)
    wts_updates[31173] = "|cffe4cfa3Берсерк|r"
    wts_updates[28991] = "|cffe4cfa3Берсерк|r (|cffffffffW|r)"
    wts_updates[20160] = (
        "|cffa6afb8ЮНИТ:|cffced4da Колоссальный тролль-гигант с сокрушительными ударами и колоссальным запасом здоровья. Проламывает оборону противника.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУстрашение|cffced4da: с вероятностью |cffffffff20%|cffced4da наносит сплеш-урон окружающим войскам.|n"
        "- |cffa9c7deЯрость Джунглей|cffced4da: увеличивает силу атак при ранениях.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: ускоренное восстановление здоровья.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04U", "field": "name", "expected": wts_updates[31173]})
    checks_def.append({"type": "unit", "id": "o04U", "field": "tip", "expected": wts_updates[28991]})
    checks_def.append({"type": "unit", "id": "o04U", "field": "ubertip", "expected": wts_updates[20160]})

    # o05G: Гидра (E)
    wts_updates[31959] = "|cffe4cfa3Гидра|r"
    wts_updates[32419] = "|cffe4cfa3Гидра|r (|cffffffffE|r)"
    wts_updates[32625] = (
        "|cffa6afb8ЮНИТ:|cffced4da Чудовищный зверь тернистых джунглей. Плюётся ядовитыми сгустками на большую дистанцию, отравляя землю под ногами врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯдовитый остаток|cffced4da: каждый выстрел создаёт лужу яда, замедляющую врагов.|n"
        "- |cffa9c7deВторое поколение|cffced4da: после исследования «Чар гидр» при гибели распадается на двух малых гидр.|n"
        "- |cffa9c7deОтравленные копья|cffced4da: периодический урон ядом.|n"
        "- |cffa9c7deЯрость Джунглей|cffced4da: бонус к урону при низком здоровье.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05G", "field": "name", "expected": wts_updates[31959]})
    checks_def.append({"type": "unit", "id": "o05G", "field": "tip", "expected": wts_updates[32419]})
    checks_def.append({"type": "unit", "id": "o05G", "field": "ubertip", "expected": wts_updates[32625]})

    # o05I: Малая гидра (Q)
    wts_updates[27853] = "|cffe4cfa3Малая гидра|r"
    wts_updates[22887] = "|cffe4cfa3Малая гидра|r (|cffffffffQ|r)"
    wts_updates[20164] = (
        "|cffa6afb8ЮНИТ:|cffced4da Молодое потомство гидры, порождённое способностью «Второе поколение». Продолжает атаковать врагов ядовитыми плевками.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯрость Джунглей|cffced4da: увеличивает урон при потере здоровья.|n"
        "- |cffa9c7deРегенерация троллей|cffced4da: быстрое восстановление здоровья.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05I", "field": "name", "expected": wts_updates[27853]})
    checks_def.append({"type": "unit", "id": "o05I", "field": "tip", "expected": wts_updates[22887]})
    checks_def.append({"type": "unit", "id": "o05I", "field": "ubertip", "expected": wts_updates[20164]})

    # =========================================================================
    # 4. HEROES (6 heroes)
    # =========================================================================
    # O054: Темный охотник (Z)
    wts_updates[31336] = "|cffe4cfa3Темный охотник|r"
    wts_updates[32484] = "|cffe4cfa3Темный охотник|r (|cffffffffZ|r)"
    wts_updates[31259] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Верховный темный охотник, направляющий магию лоа на спасение союзников и ослабление врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолна исцеления|cffced4da: восстанавливает здоровье цели и передаётся нескольким союзникам.|n"
        "- |cffa9c7deСглаз|cffced4da: превращает группы врагов в беззащитных зверушек.|n"
        "- |cffa9c7deЗмеиный идол|cffced4da: призывает стреляющий тотем, атакующий наземные и воздушные цели.|n"
        "- |cffa9c7deДухи вуду|cffced4da: выпускает стаю духов, похищающих жизнь у врагов.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "O054", "field": "name", "expected": wts_updates[31336]})
    checks_def.append({"type": "unit", "id": "O054", "field": "tip", "expected": wts_updates[32484]})
    checks_def.append({"type": "unit", "id": "O054", "field": "ubertip", "expected": wts_updates[31259]})

    # O05A: Мастер клинка (Q)
    wts_updates[31346] = "|cffe4cfa3Мастер клинка|r"
    wts_updates[31514] = "|cffe4cfa3Мастер клинка|r (|cffffffffQ|r)"
    wts_updates[31908] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Неуловимый и смертоносный воин джунглей, молниеносно перемещающийся по полю боя и сокрушающий врагов вихрем стали.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПрыжок Вуду|cffced4da: совершает прыжок в указанную точку, нанося урон при приземлении.|n"
        "- |cffa9c7deВкус крови|cffced4da: преобразует процент наносимого урона в собственное здоровье.|n"
        "- |cffa9c7deХитроумный ритуал|cffced4da: жертвует половиной здоровья, чтобы затем восстановить значительно больше.|n"
        "- |cffa9c7deВихрь клинков|cffced4da: кружится в смертоносном вихре, взмывая в воздух и нанося урон врагам.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffЛовкость|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "O05A", "field": "name", "expected": wts_updates[31346]})
    checks_def.append({"type": "unit", "id": "O05A", "field": "tip", "expected": wts_updates[31514]})
    checks_def.append({"type": "unit", "id": "O05A", "field": "ubertip", "expected": wts_updates[31908]})

    # O05D: Низвергатель (A)
    wts_updates[31524] = "|cffe4cfa3Низвергатель|r"
    wts_updates[32333] = "|cffe4cfa3Низвергатель|r (|cffffffffA|r)"
    wts_updates[31955] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Разрушительный шаман джунглей, обрушивающий на врагов электрические разряды и создающий зоны распада плоти.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКолдовской удар|cffced4da: поражает врагов молнией в секторе перед собой.|n"
        "- |cffa9c7deАура гениальности|cffced4da: ускоряет восстановление маны окружающих союзников.|n"
        "- |cffa9c7deМёртвая зона|cffced4da: область разложения, наносящая процентный урон войскам и зданиям.|n"
        "- |cffa9c7deПленение|cffced4da: сковывает цель магическими узами, лишая возможности двигаться и атаковать.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "O05D", "field": "name", "expected": wts_updates[31524]})
    checks_def.append({"type": "unit", "id": "O05D", "field": "tip", "expected": wts_updates[32333]})
    checks_def.append({"type": "unit", "id": "O05D", "field": "ubertip", "expected": wts_updates[31955]})

    # O055: Хаккар Свежеватель Душ (S)
    wts_updates[27215] = "|cffe4cfa3Хаккар Свежеватель Душ|r"
    wts_updates[25323] = "|cffa9c7deХаккар|r"
    wts_updates[357] = "|cffe4cfa3Хаккар Свежеватель Душ|r (|cffffffffS|r)"
    wts_updates[39637] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный кровавый бог империи Гурубаши. Пожирает плоть и души подданных, взамен даруя армии колоссальную мощь.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПоток крови|cffced4da: кровавая волна, поражающая врагов на пути.|n"
        "- |cffa9c7deВлияние Хаккара|cffced4da: глобальная аура, усиливающая дальнобойный урон всех войск на карте.|n"
        "- |cffa9c7deКровяной взрыв|cffced4da: взрыв крови вокруг цели; при взрыве союзника мгновенно перезаряжается.|n"
        "- |cffa9c7deПорченая кровь|cffced4da: заражает врага смертоносной эпидемией, перекидывающейся на соседей.|n"
        "- |cffa9c7deСвежеватель душ|cffced4da: поглощает союзных воинов для насыщения здоровьем и маной.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "|cffa6afb8Требуется выбор:|r |cffa9c7deИмперия Гурубаши|r.|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "O055", "field": "name", "expected": wts_updates[27215]})
    checks_def.append({"type": "unit", "id": "O055", "field": "propernames", "expected": wts_updates[25323]})
    checks_def.append({"type": "unit", "id": "O055", "field": "tip", "expected": wts_updates[357]})
    checks_def.append({"type": "unit", "id": "O055", "field": "ubertip", "expected": wts_updates[39637]})

    # O05L: Лоа Смерти Бвонсамди (S)
    wts_updates[31348] = "|cffe4cfa3Лоа Смерти Бвонсамди|r"
    wts_updates[30633] = "|cffa9c7deБвонсамди|r"
    wts_updates[30654] = "|cffe4cfa3Лоа Смерти Бвонсамди|r (|cffffffffS|r)"
    wts_updates[39638] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный повелитель загробного мира и душ племени Чёрного Копья. Обитает в астрале, черпая силу из смертей врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСила иного мира / Поток смерти|cffced4da: усиливает воинов или насылает стаю призрачных нетопырей.|n"
        "- |cffa9c7deСлуги смерти|cffced4da: поднимает павших воинов из трупов на службу духам.|n"
        "- |cffa9c7deЧеред ещё не настал|cffced4da: воскрешает павших союзных героев и воинов.|n"
        "- |cffa9c7deМатериальная форма|cffced4da: воплощается в физическом мире, получая возможность напрямую разить врагов.|n"
        "- |cffa9c7deЛоа Смерти|cffced4da: пассивно усиливает здоровье, ману и регенерацию за каждую гибель врагов.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Требуется выбор:|r |cffa9c7deЧёрное Копьё|r.|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "O05L", "field": "name", "expected": wts_updates[31348]})
    checks_def.append({"type": "unit", "id": "O05L", "field": "propernames", "expected": wts_updates[30633]})
    checks_def.append({"type": "unit", "id": "O05L", "field": "tip", "expected": wts_updates[30654]})
    checks_def.append({"type": "unit", "id": "O05L", "field": "ubertip", "expected": wts_updates[39638]})

    # O05C: Лоа Смерти Бвонсамди (материальная форма)
    wts_updates[30632] = "|cffe4cfa3Бвонсамди (материальная форма)|r"
    wts_updates[25511] = "|cffa9c7deБвонсамди|r"
    wts_updates[32860] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Физическое воплощение Лоа Смерти в мире живых. В этой форме Бвонсамди уязвим, но способен наносить сокрушительный урон.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСила иного мира / Поток смерти|cffced4da: усиление союзников или выпуск призрачных нетопырей.|n"
        "- |cffa9c7deСлуги смерти|cffced4da: оживление трупов на поле боя.|n"
        "- |cffa9c7deЧеред ещё не настал|cffced4da: воскрешение погибших союзников.|n"
        "- |cffa9c7deМатериальная форма|cffced4da: возвращение в безопасный астральный мир при падении здоровья.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "O05C", "field": "name", "expected": wts_updates[30632]})
    checks_def.append({"type": "unit", "id": "O05C", "field": "propernames", "expected": wts_updates[25511]})
    checks_def.append({"type": "unit", "id": "O05C", "field": "ubertip", "expected": wts_updates[32860]})

    # =========================================================================
    # 5. UPGRADES (14 upgrades)
    # =========================================================================
    # R0I8: Стальное оружие (6 lvls, Q)
    r0i8_names = [32155, 32403, 32408, 31501, 31505, 31507]
    r0i8_tips = [32529, 32530, 32531, 32525, 32526, 32527]
    r0i8_ubs = [31516, 32020, 32021, 32151, 32152, 32153]
    for lvl in range(1, 7):
        wts_updates[r0i8_names[lvl - 1]] = f"|cffe4cfa3Стальное оружие — уровень {lvl}|r"
        wts_updates[r0i8_tips[lvl - 1]] = f"|cffe4cfa3Стальное оружие — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r0i8_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак немагических воинов Троллей джунглей.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Воителям, Охотникам за головами, Наездникам, Берсеркам и Гидрам.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        )

    # R0I9: Стальная броня (6 lvls, W)
    r0i9_names = [31583, 31586, 31587, 31571, 31572, 31573]
    r0i9_tips = [32540, 32541, 32542, 32532, 32533, 32534]
    r0i9_ubs = [32422, 32535, 32536, 32537, 32538, 32539]
    for lvl in range(1, 7):
        wts_updates[r0i9_names[lvl - 1]] = f"|cffe4cfa3Стальная броня — уровень {lvl}|r"
        wts_updates[r0i9_tips[lvl - 1]] = f"|cffe4cfa3Стальная броня — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[r0i9_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает защиту и прочность доспехов всех войск Троллей джунглей.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем боевым единицам Троллей джунглей.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        )

    # R0IA: Методы регенерации (6 lvls, A)
    r0ia_names = [32496, 32497, 32498, 32490, 32491, 32492]
    r0ia_tips = [32420, 32455, 32464, 27308, 27309, 27310]
    r0ia_ubs = [27312, 27313, 27314, 27686, 28589, 29044]
    for lvl in range(1, 7):
        wts_updates[r0ia_names[lvl - 1]] = f"|cffe4cfa3Методы регенерации — уровень {lvl}|r"
        wts_updates[r0ia_tips[lvl - 1]] = f"|cffe4cfa3Методы регенерации — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r0ia_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Ускоряет естественное восстановление здоровья у всех органических войск Троллей джунглей.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем органическим воинам Троллей джунглей.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        )

    # R0IB: Обучение жрецов (3 lvls, Z)
    r0ib_names = [16588, 16589, 17414]
    r0ib_tips = [17346, 17391, 18237]
    r0ib_ubs = [18366, 18650, 18651]
    for lvl in range(1, 4):
        wts_updates[r0ib_names[lvl - 1]] = f"|cffe4cfa3Обучение жрецов — ступень {lvl}|r"
        wts_updates[r0ib_tips[lvl - 1]] = f"|cffe4cfa3Обучение жрецов — ступень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0ib_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны, скорость её восстановления и открывает новые заклинания Жрецов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Жрецам.|n|n"
            f"|cffa6afb8Ступень обучения:|r |cffffffff{lvl}/3|r."
        )

    # R0IC: Обучение знахарей (3 lvls, X)
    r0ic_names = [32550, 19900, 32545]
    r0ic_tips = [32543, 32544, 32546]
    r0ic_ubs = [32547, 32548, 32549]
    for lvl in range(1, 4):
        wts_updates[r0ic_names[lvl - 1]] = f"|cffe4cfa3Обучение знахарей — ступень {lvl}|r"
        wts_updates[r0ic_tips[lvl - 1]] = f"|cffe4cfa3Обучение знахарей — ступень {lvl}|r (|cffffffffX|r)"
        wts_updates[r0ic_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны, скорость её восстановления и открывает новые тотемы Знахарей.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Знахарям.|n|n"
            f"|cffa6afb8Ступень обучения:|r |cffffffff{lvl}/3|r."
        )

    # R0ID: Обучение высших магов (3 lvls, C)
    r0id_names = [19961, 19979, 20097]
    r0id_tips = [20005, 20056, 20140]
    r0id_ubs = [19287, 19830, 19893]
    for lvl in range(1, 4):
        wts_updates[r0id_names[lvl - 1]] = f"|cffe4cfa3Обучение высших магов — ступень {lvl}|r"
        wts_updates[r0id_tips[lvl - 1]] = f"|cffe4cfa3Обучение высших магов — ступень {lvl}|r (|cffffffffC|r)"
        wts_updates[r0id_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, запас маны и открывает новые заклинания Колдунов Вуду и Магов Чёрного Копья.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Колдунам Вуду и Магам Чёрного Копья.|n|n"
            f"|cffa6afb8Ступень обучения:|r |cffffffff{lvl}/3|r."
        )

    # R0II: Улучшенные топоры (6 lvls, X)
    r0ii_names = [32075, 32072, 32058, 32059, 32060, 32061]
    r0ii_tips = [32723, 32722, 32460, 32461, 32462, 32721]
    for lvl in range(1, 7):
        wts_updates[r0ii_names[lvl - 1]] = f"|cffe4cfa3Улучшенные топоры — уровень {lvl}|r"
        wts_updates[r0ii_tips[lvl - 1]] = f"|cffe4cfa3Улучшенные топоры — уровень {lvl}|r (|cffffffffX|r)"
    r0ii_ubs_map = {3: 32066, 4: 32067, 5: 32068, 6: 32069}
    for lvl, sid in r0ii_ubs_map.items():
        wts_updates[sid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает топоры Ремесленников, увеличивая количество переносимой древесины на |cffc8e087+10|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Ремесленникам.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        )

    # R0IJ: Корпуса построек (3 lvls, Z)
    r0ij_names = [32094, 32095, 32389]
    r0ij_tips = [32392, 32393, 32394]
    r0ij_ubs = [19352, 19354, 19355]
    for lvl in range(1, 4):
        wts_updates[r0ij_names[lvl - 1]] = f"|cffe4cfa3Корпуса построек — уровень {lvl}|r"
        wts_updates[r0ij_tips[lvl - 1]] = f"|cffe4cfa3Корпуса построек — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0ij_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет стены и каркасы зданий, повышая их прочность и броню.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем зданиям Троллей джунглей.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R0IK: Эликсиры жизни (3 lvls, Z)
    r0ik_names = [32502, 32503, 32504]
    r0ik_tips = [32506, 32507, 33046]
    r0ik_ubs = [32105, 32107, 32108]
    for lvl in range(1, 4):
        wts_updates[r0ik_names[lvl - 1]] = f"|cffe4cfa3Эликсиры жизни — уровень {lvl}|r"
        wts_updates[r0ik_tips[lvl - 1]] = f"|cffe4cfa3Эликсиры жизни — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0ik_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья Воителей и Охотников за головами на |cffc8e087+100|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Воителям и Охотникам за головами.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R0IL: Дрессировка животных (1 lvl, Z)
    wts_updates[32307] = "|cffe4cfa3Дрессировка животных|r"
    wts_updates[32310] = "|cffe4cfa3Дрессировка животных|r (|cffffffffZ|r)"
    wts_updates[32301] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает боевую выучку зверей, повышая скорость атаки и передвижения Наездников и Гидр.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Наездникам и Гидрам.|r"
    )

    # R0IM: Отравленные копья (1 lvl, A)
    wts_updates[32206] = "|cffe4cfa3Отравленные копья|r"
    wts_updates[32730] = "|cffe4cfa3Отравленные копья|r (|cffffffffA|r)"
    wts_updates[32409] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Смазывает наконечники копий ядом джунглей. Атаки отравляют цель, нанося |cffe69a8d5|cffced4da ед. урона/сек. в течение |cffffffff25|cffced4da сек.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Охотникам за головами и Наездникам.|r"
    )

    # R0IN: Чары гидр (1 lvl, X)
    wts_updates[32510] = "|cffe4cfa3Чары гидр|r"
    wts_updates[32511] = "|cffe4cfa3Чары гидр|r (|cffffffffX|r)"
    wts_updates[32340] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Пробуждает древнее разделение плоти гидр. При гибели взрослая Гидра порождает двух Малых гидр.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Гидрам.|r"
    )

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # A1D0: Ярость Джунглей
    wts_updates[15083] = "|cffe4cfa3Ярость джунглей|r"
    wts_updates[15090] = "|cffe4cfa3Ярость джунглей|r"
    wts_updates[15091] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Расовая ярость троллей. Чем больше здоровья потеряно воином, тем выше наносимый им урон от атак.|r"
    checks_def.append({"type": "ability", "id": "A1D0", "field": "name", "expected": wts_updates[15083]})
    checks_def.append({"type": "ability", "id": "A1D0", "field": "tip1", "expected": wts_updates[15090]})
    checks_def.append({"type": "ability", "id": "A1D0", "field": "ubertip1", "expected": wts_updates[15091]})

    # A1D1: Ярость джунглей (triggered aura)
    wts_updates[15133] = "|cffe4cfa3Ярость джунглей|r"

    # A1CX: Перезарядка
    wts_updates[31479] = "|cffe4cfa3Перезарядка ярости|r"
    wts_updates[31379] = "|cffe4cfa3Перезарядка ярости|r"

    # A1DU: Регенерация троллей
    wts_updates[31994] = "|cffe4cfa3Регенерация троллей|r"

    # A1EJ: Бодрящий эликсир (Q)
    wts_updates[32436] = "|cffe4cfa3Бодрящий эликсир|r"
    wts_updates[32437] = "|cffe4cfa3Бодрящий эликсир|r (|cffffffffQ|r)"
    wts_updates[20548] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Воитель выпивает укрепляющее зелье, жертвуя |cffe69a8d75|cffced4da ед. здоровья ради резкого увеличения скорости атаки и передвижения на |cffffffff15|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1EJ", "field": "name", "expected": wts_updates[32436]})
    checks_def.append({"type": "ability", "id": "A1EJ", "field": "tip1", "expected": wts_updates[32437]})
    checks_def.append({"type": "ability", "id": "A1EJ", "field": "ubertip1", "expected": wts_updates[20548]})

    # A1EI: Отравленные копья
    wts_updates[31563] = "|cffe4cfa3Отравленные копья|r"
    wts_updates[31566] = "|cffe4cfa3Отравленные копья|r"
    wts_updates[32489] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака отравляет цель, нанося |cffe69a8d5|cffced4da ед. урона каждую секунду. Время действия: |cffffffff25|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1EI", "field": "name", "expected": wts_updates[31563]})
    checks_def.append({"type": "ability", "id": "A1EI", "field": "tip1", "expected": wts_updates[31566]})
    checks_def.append({"type": "ability", "id": "A1EI", "field": "ubertip1", "expected": wts_updates[32489]})

    # A1DF: Жажда крови (Q)
    wts_updates[28146] = "|cffe4cfa3Жажда крови|r"
    wts_updates[28147] = "|cffe4cfa3Жажда крови|r (|cffffffffQ|r)"

    # A1DG: Рассеивание заклинаний (W)
    wts_updates[28149] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[28151] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffW|r)"

    # A1DH: Замедление (E)
    wts_updates[28152] = "|cffe4cfa3Замедление|r"
    wts_updates[28155] = "|cffe4cfa3Замедление|r (|cffffffffE|r)"

    # A1DX: Жертва кровью (R)
    wts_updates[32011] = "|cffe4cfa3Жертва кровью|r"
    wts_updates[32012] = "|cffe4cfa3Жертва кровью|r (|cffffffffR|r)"
    wts_updates[36104] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приносит в жертву |cffe69a8d100|cffced4da ед. здоровья, мгновенно восстанавливая |cffc8e087100|cffced4da ед. маны.|r"
    checks_def.append({"type": "ability", "id": "A1DX", "field": "name", "expected": wts_updates[32011]})
    checks_def.append({"type": "ability", "id": "A1DX", "field": "tip1", "expected": wts_updates[32012]})
    checks_def.append({"type": "ability", "id": "A1DX", "field": "ubertip1", "expected": wts_updates[36104]})

    # A1D2: Стазисная ловушка
    wts_updates[15666] = "|cffe4cfa3Стазисная ловушка|r"

    # A1D3: Сторожевой идол (Q)
    wts_updates[15954] = "|cffe4cfa3Сторожевой идол|r"
    wts_updates[30920] = "|cffe4cfa3Сторожевой идол|r (|cffffffffQ|r)"
    wts_updates[15169] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Устанавливает невидимый тотем, открывающий обзор и обнаруживающий невидимых врагов. Увеличивает урон союзников поблизости на |cffc8e087+5|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A1D3", "field": "name", "expected": wts_updates[15954]})
    checks_def.append({"type": "ability", "id": "A1D3", "field": "tip1", "expected": wts_updates[30920]})
    checks_def.append({"type": "ability", "id": "A1D3", "field": "ubertip1", "expected": wts_updates[15169]})

    # A1D5: Исцеляющий идол
    wts_updates[15964] = "|cffe4cfa3Исцеляющий идол|r"

    # A1DT: Усиление вуду (Q)
    wts_updates[31991] = "|cffe4cfa3Усиление вуду|r"
    wts_updates[31992] = "|cffe4cfa3Усиление вуду|r (|cffffffffQ|r)"
    wts_updates[31993] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наполняет атаки тёмным огнём вуду, добавляя |cffc8e087+13|cffced4da ед. урона. Расходует ману при каждом выстреле.|r"
    checks_def.append({"type": "ability", "id": "A1DT", "field": "name", "expected": wts_updates[31991]})
    checks_def.append({"type": "ability", "id": "A1DT", "field": "tip1", "expected": wts_updates[31992]})
    checks_def.append({"type": "ability", "id": "A1DT", "field": "ubertip1", "expected": wts_updates[31993]})

    # A1DV: Тёмный дух
    wts_updates[31996] = "|cffe4cfa3Тёмный дух|r"

    # A1DW: Сглаз (E)
    wts_updates[30312] = "|cffe4cfa3Сглаз|r"
    wts_updates[30314] = "|cffe4cfa3Сглаз|r (|cffffffffE|r)"
    wts_updates[32010] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает вражеского воина в случайное животное на |cffffffff15|cffced4da сек. На героев действует кратковременно.|r"
    checks_def.append({"type": "ability", "id": "A1DW", "field": "name", "expected": wts_updates[30312]})
    checks_def.append({"type": "ability", "id": "A1DW", "field": "tip1", "expected": wts_updates[30314]})
    checks_def.append({"type": "ability", "id": "A1DW", "field": "ubertip1", "expected": wts_updates[32010]})

    # A1F4: Морозный доспех (Q)
    wts_updates[32864] = "|cffe4cfa3Морозный доспех|r"
    wts_updates[32865] = "|cffe4cfa3Морозный доспех|r (|cffffffffQ|r)"

    # A1F5: Буран (E)
    wts_updates[32866] = "|cffe4cfa3Буран|r"
    wts_updates[32867] = "|cffe4cfa3Буран|r (|cffffffffE|r)"
    wts_updates[16953] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область |cffffffff5|cffced4da волн ледяных осколков. Каждая волна наносит по |cffe69a8d100|cffced4da ед. урона.|r"
    checks_def.append({"type": "ability", "id": "A1F5", "field": "name", "expected": wts_updates[32866]})
    checks_def.append({"type": "ability", "id": "A1F5", "field": "tip1", "expected": wts_updates[32867]})
    checks_def.append({"type": "ability", "id": "A1F5", "field": "ubertip1", "expected": wts_updates[16953]})

    # A1F6: Ледяные стрелы (W)
    wts_updates[32869] = "|cffe4cfa3Ледяные стрелы|r"
    wts_updates[32870] = "|cffe4cfa3Ледяные стрелы|r (|cffffffffW|r)"

    # A1DY: Сменить дистанцию боя
    wts_updates[32014] = "|cffe4cfa3Сменить дистанцию боя|r"
    wts_updates[32015] = "|cffe4cfa3Сменить дистанцию боя|r"
    wts_updates[32016] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переключает наездника между режимами дальнего метания копий и ближнего боя.|r"

    # A1EH: Устрашение
    wts_updates[32735] = "|cffe4cfa3Устрашение|r"
    wts_updates[32736] = "|cffe4cfa3Устрашение|r"
    wts_updates[32737] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки берсерка с вероятностью |cffffffff20%|cffced4da наносят сокрушительный круговой урон окружающим наземным войскам.|r"

    # A1DK: Второе поколение
    wts_updates[29025] = "|cffe4cfa3Второе поколение|r"
    wts_updates[29029] = "|cffe4cfa3Второе поколение|r"
    wts_updates[29042] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da После исследования «Чар гидр» при гибели взрослая гидра распадается на двух малых гидр.|r"

    # A1DN: Ядовитый остаток
    wts_updates[31146] = "|cffe4cfa3Ядовитый остаток|r"
    wts_updates[31152] = "|cffe4cfa3Ядовитый остаток|r"
    wts_updates[31154] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждый плевок оставляет на земле ядовитую лужу, снижающую скорость атаки и передвижения противников.|r"

    # A1DI: Поколение гидры
    wts_updates[28159] = "|cffe4cfa3Поколение гидры|r"

    # Hero: Dark Hunter (O054)
    # AOhw: Волна исцеления
    wts_updates[63] = "|cffe4cfa3Волна исцеления|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[627] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff130|cffced4da ед. здоровья цели и переходит к |cffffffff3|cffced4da союзникам.|r"
    wts_updates[628] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff205|cffced4da ед. здоровья цели и переходит к |cffffffff4|cffced4da союзникам.|r"
    wts_updates[4411] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff280|cffced4da ед. здоровья цели и переходит к |cffffffff5|cffced4da союзникам.|r"
    wts_updates[28014] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff385|cffced4da ед. здоровья цели и переходит к |cffffffff20|cffced4da союзникам.|r"
    wts_updates[28015] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создает волну энергии, восстанавливающую здоровье цели и переходящую к ближайшим союзникам.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff130|cffced4da ед., до |cffffffff3|cffced4da целей.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff205|cffced4da ед., до |cffffffff4|cffced4da целей.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff280|cffced4da ед., до |cffffffff5|cffced4da целей.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff385|cffced4da ед., до |cffffffff20|cffced4da целей.|r"
    )

    # A1E0: Сглаз (4 lvls, W)
    wts_updates[32008] = "|cffe4cfa3Сглаз|r"
    a1e0_tips = [30315, 32009, 32675, 32676]
    a1e0_durs = ["5", "10", "15", "20"]
    for l in range(1, 5):
        wts_updates[a1e0_tips[l - 1]] = f"|cffe4cfa3Сглаз|r [|cffffffff{l}|r] (|cffffffffW|r)"
    wts_updates[30313] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает всех врагов в указанной области в беззащитных зверушек на |cffffffff5|cffced4da сек.|r"
    wts_updates[32034] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает всех врагов в указанной области в беззащитных зверушек на |cffffffff10|cffced4da сек.|r"
    wts_updates[32985] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает всех врагов в указанной области в беззащитных зверушек на |cffffffff15|cffced4da сек.|r"
    wts_updates[32986] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает всех врагов в указанной области в беззащитных зверушек на |cffffffff20|cffced4da сек.|r"
    wts_updates[32980] = "|cffe4cfa3Сглаз|r [|cffffffff%d|r] (|cffffffffW|r)"
    wts_updates[32987] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает противников в указанной области в беззащитных зверушек, лишая их возможности атаковать и применять заклинания.|r"

    # AOsw: Змеиный идол (E)
    wts_updates[31438] = "|cffe4cfa3Змеиный идол|r [|cffffffff4|r] (|cffffffffE|r)"
    wts_updates[3451] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного невосприимчивого к магии идола со |cffffffff135|cffced4da ед. здоровья, наносящего |cffffffff40-45|cffced4da ед. урона. Время действия: |cffffffff115|cffced4da сек.|n|n|cffa9c7deИдол атакует наземные и воздушные цели.|r"
    wts_updates[31413] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного невосприимчивого к магии идола, атакующего наземные и воздушные цели.|r"

    # Hero: Blademaster (O05A)
    # A1E2: Прыжок Вуду (4 lvls, Q)
    wts_updates[32040] = "|cffe4cfa3Прыжок Вуду|r"
    a1e2_tips = [31542, 31544, 31984, 31985]
    a1e2_ubs = [32636, 32637, 32638, 32639]
    a1e2_dmgs = ["1.2x силы + 50", "2.4x силы + 100", "3.6x силы + 150", "4.8x силы + 200"]
    a1e2_cds = ["40", "30", "20", "10"]
    for l in range(1, 5):
        wts_updates[a1e2_tips[l - 1]] = f"|cffe4cfa3Прыжок Вуду|r [|cffffffff{l}|r] (|cffffffffQ|r)"
        wts_updates[a1e2_ubs[l - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой стремительно прыгает в указанную точку, нанося |cffe69a8d{a1e2_dmgs[l-1]}|cffced4da ед. урона врагам в точке приземления. Перезарядка: |cffffffff{a1e2_cds[l-1]}|cffced4da сек.|r"
        )
    wts_updates[32038] = "|cffe4cfa3Прыжок Вуду|r [|cffffffff%d|r] (|cffffffffQ|r)"
    wts_updates[32039] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой прыгает в указанное место, нанося урон врагам. С уровнем увеличивается дальность и снижается время перезарядки.|r"

    # A1E5: Вкус Крови (4 lvls, W)
    wts_updates[20580] = "|cffe4cfa3Вкус крови|r"
    a1e5_tips = [32126, 32127, 32129, 32130]
    a1e5_ubs = [20581, 32128, 32134, 32135]
    for l in range(1, 5):
        pct = l * 4
        wts_updates[a1e5_tips[l - 1]] = f"|cffe4cfa3Вкус крови|r [|cffffffff{l}|r] (|cffffffffW|r)"
        wts_updates[a1e5_ubs[l - 1]] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Любой урон, наносимый героем, преобразуется в собственное здоровье в объёме |cffc8e087{pct}%|cffced4da от нанесённых повреждений.|r"
    wts_updates[32131] = "|cffe4cfa3Вкус крови|r [|cffffffff%d|r] (|cffffffffW|r)"
    wts_updates[32136] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Преобразует часть наносимого урона в здоровье героя. С каждым уровнем процент возрастает на |cffc8e087+4%|cffced4da.|r"

    # A1E3: Хитроумный ритуал (4 lvls, E)
    wts_updates[32118] = "|cffe4cfa3Хитроумный ритуал|r"
    a1e3_tips = [32041, 32042, 32043, 32111]
    a1e3_ubs = [32112, 32113, 32114, 32115]
    for l in range(1, 5):
        wts_updates[a1e3_tips[l - 1]] = f"|cffe4cfa3Хитроумный ритуал|r [|cffffffff{l}|r] (|cffffffffE|r)"
        wts_updates[a1e3_ubs[l - 1]] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой жертвует |cffe69a8d50%|cffced4da текущего здоровья, после чего в течение |cffffffff7|cffced4da сек. восстанавливает существенно больше здоровья.|r"
    wts_updates[32116] = "|cffe4cfa3Хитроумный ритуал|r [|cffffffff%d|r] (|cffffffffE|r)"
    wts_updates[32896] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ритуал самопожертвования: отнимает половину текущего здоровья, взамен восстанавливая его с избытком в течение нескольких секунд.|r"

    # A1E4: Вихрь клинков (2 lvls, R)
    wts_updates[32121] = "|cffe4cfa3Вихрь клинков|r"
    wts_updates[32123] = "|cffe4cfa3Вихрь клинков|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[32119] = "|cffe4cfa3Вихрь клинков|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[32631] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает мастера клинка вихрем стали, даруя неуязвимость к магии и нанося урон врагам поблизости. Перезарядка: |cffffffff180|cffced4da сек.|r"
    wts_updates[32630] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает мастера клинка вихрем стали, даруя неуязвимость к магии и нанося урон врагам поблизости. Перезарядка: |cffffffff180|cffced4da сек.|r"
    wts_updates[32122] = "|cffe4cfa3Вихрь клинков|r [|cffffffff%d|r] (|cffffffffR|r)"

    # Hero: Demolisher (O05D)
    # A1E6: Колдовской удар (4 lvls, Q)
    wts_updates[32140] = "|cffe4cfa3Колдовской удар|r"
    a1e6_tips = [32522, 32523, 32524, 31279]
    a1e6_ubs = [32633, 32634, 32635, 32632]
    for l in range(1, 5):
        wts_updates[a1e6_tips[l - 1]] = f"|cffe4cfa3Колдовской удар|r [|cffffffff{l}|r] (|cffffffffQ|r)"
        wts_updates[a1e6_ubs[l - 1]] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цепной молнией врагов в секторе перед собой, нанося урон каждой цели. Перезарядка: |cffffffff11|cffced4da сек.|r"
    wts_updates[32521] = "|cffe4cfa3Колдовской удар|r [|cffffffff%d|r] (|cffffffffQ|r)"
    wts_updates[32139] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молнией противников в секторе перед героем. С уровнем растёт урон и число поражаемых целей.|r"

    # A1EA: Аура гениальности
    wts_updates[35514] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Значительно ускоряет регенерацию маны всех находящихся рядом союзников.|r"

    # A1E8: Мёртвая зона (4 lvls, W)
    wts_updates[32147] = "|cffe4cfa3Мёртвая зона|r"
    a1e8_tips = [20912, 20915, 20916, 20917]
    a1e8_ubs = [20918, 20919, 20920, 20921]
    a1e8_durs = ["16", "26", "36", "46"]
    for l in range(1, 5):
        wts_updates[a1e8_tips[l - 1]] = f"|cffe4cfa3Мёртвая зона|r [|cffffffff{l}|r] (|cffffffffW|r)"
        wts_updates[a1e8_ubs[l - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт область тёмного разложения. В течение |cffffffff{a1e8_durs[l-1]}|cffced4da сек. вражеские войска и здания теряют по |cffe69a8d{l}%|cffced4da максимального запаса здоровья каждую секунду.|r"
        )
    wts_updates[32146] = "|cffe4cfa3Мёртвая зона|r [|cffffffff%d|r] (|cffffffffW|r)"
    wts_updates[25170] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Насылает проклятие разложения на область, нанося процентный урон здоровью противников и строений.|r"

    # A1E9: Пленение (2 lvls, R)
    wts_updates[32172] = "|cffe4cfa3Пленение|r"
    wts_updates[32173] = "|cffe4cfa3Пленение|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[32175] = "|cffe4cfa3Пленение|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[35065] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывает цель магическими цепями. Враг не может двигаться и атаковать, получая периодический урон. Длительность: |cffffffff6|cffced4da сек. (герои) / |cffffffff40|cffced4da сек. (войска).|r"
    wts_updates[35066] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывает цель магическими цепями. Враг не может двигаться и атаковать, получая периодический урон. Длительность: |cffffffff8|cffced4da сек. (герои) / |cffffffff40|cffced4da сек. (войска).|r"
    wts_updates[32174] = "|cffe4cfa3Пленение|r [|cffffffff%d|r] (|cffffffffR|r)"
    wts_updates[32176] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывает противника цепями, нанося урон и лишая возможности двигаться и атаковать.|r"

    # Hero: Soulflayer Hakkar (O055)
    # A1DC: Поток крови (4 lvls, Q)
    wts_updates[32732] = "|cffe4cfa3Поток крови|r"
    a1dc_tips = [10272, 10273, 32442, 10269]
    a1dc_ubs = [32609, 32610, 32611, 32608]
    a1dc_hps = ["150", "250", "350", "450"]
    a1dc_dmgs = ["45", "80", "115", "150"]
    for l in range(1, 5):
        wts_updates[a1dc_tips[l - 1]] = f"|cffe4cfa3Поток крови|r [|cffffffff{l}|r] (|cffffffffQ|r)"
        wts_updates[a1dc_ubs[l - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит урон врагам на прямой к выбранной точке. Снимает |cffe69a8d{a1dc_hps[l-1]}|cffced4da ед. здоровья Хаккара за применение. Наносит |cffe69a8d{a1dc_dmgs[l-1]}|cffced4da ед. урона. Перезарядка: |cffffffff1|cffced4da сек.|r"
        )
    wts_updates[32733] = "|cffe4cfa3Поток крови|r [|cffffffff%d|r] (|cffffffffQ|r)"
    wts_updates[32734] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает струю кипящей крови, поражающую врагов на пути ценой собственного здоровья Хаккара.|r"

    # A1DM: Влияние Хаккара (4 lvls, W)
    wts_updates[31135] = "|cffe4cfa3Влияние Хаккара|r"
    a1dm_tips = [32472, 32473, 32474, 31491]
    a1dm_ubs = [30318, 30325, 35064, 35050]
    a1dm_pcts = ["7%", "14%", "21%", "28%"]
    a1dm_degens = ["4", "8", "12", "16"]
    for l in range(1, 5):
        wts_updates[a1dm_tips[l - 1]] = f"|cffe4cfa3Влияние Хаккара|r [|cffffffff{l}|r] (|cffffffffW|r)"
        wts_updates[a1dm_ubs[l - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Глобальная аура бога крови. Увеличивает урон дальнобойных атак всех ваших войск на карте на |cffc8e087+{a1dm_pcts[l-1]}|cffced4da, но снижает регенерацию Хаккара на |cffe69a8d{a1dm_degens[l-1]}|cffced4da ед.|r"
        )
    wts_updates[32478] = "|cffe4cfa3Влияние Хаккара|r [|cffffffff%d|r] (|cffffffffW|r)"
    wts_updates[32479] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон войск по всей карте, но уменьшает регенерацию Хаккара, требуя частых жертвоприношений.|r"

    # A1EL: Кровяной взрыв (4 lvls, E)
    wts_updates[20583] = "|cffe4cfa3Кровяной взрыв|r"
    a1el_tips = [21448, 21452, 32452, 20582]
    a1el_ubs = [32617, 32618, 32619, 32616]
    a1el_dmgs = ["100", "150", "200", "250"]
    for l in range(1, 5):
        wts_updates[a1el_tips[l - 1]] = f"|cffe4cfa3Кровяной взрыв|r [|cffffffff{l}|r] (|cffffffffE|r)"
        wts_updates[a1el_ubs[l - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взрывает кровь вокруг цели, нанося |cffe69a8d{a1el_dmgs[l-1]}|cffced4da ед. урона окружающим врагам. Если цель — союзник, время перезарядки сбрасывается. Перезарядка: |cffffffff15|cffced4da сек.|r"
        )
    wts_updates[20584] = "|cffe4cfa3Кровяной взрыв|r [|cffffffff%d|r] (|cffffffffE|r)"
    wts_updates[25512] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает врагов вокруг цели взрывом крови ценой здоровья Хаккара. При применении на союзника перезарядка сбрасывается.|r"

    # A1DB: Порченая кровь (2 lvls, R)
    wts_updates[15168] = "|cffe4cfa3Порченая кровь|r"
    wts_updates[25359] = "|cffe4cfa3Порченая кровь|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[32439] = "|cffe4cfa3Порченая кровь|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[21378] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заражает врага чумой порченой крови. Цель получает периодический урон, а инфекция перекидывается на ближайших противников. Перезарядка: |cffffffff120|cffced4da сек.|r"
    wts_updates[21475] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заражает врага чумой порченой крови. Цель получает периодический урон, а инфекция перекидывается на ближайших противников. Перезарядка: |cffffffff75|cffced4da сек.|r"
    wts_updates[27209] = "|cffe4cfa3Порченая кровь|r [|cffffffff%d|r] (|cffffffffR|r)"
    wts_updates[27210] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Насылает страшную эпидемию порченой крови, перескакивающую между врагами и наносящую нарастающий урон.|r"

    # A1DD: Свежеватель душ (passive)
    wts_updates[27216] = "|cffe4cfa3Свежеватель душ|r"
    wts_updates[31232] = "|cffe4cfa3Свежеватель душ|r"
    wts_updates[31487] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Хаккар требует кровавых жертв. При здоровье ниже |cffffffff75%|cffced4da он поглощает союзников поблизости, восстанавливая здоровье и ману. Каждая смерть органического юнита увеличивает максимальное здоровье и ману Хаккара на |cffc8e087+5|cffced4da.|r"

    # A1EM: Поглощение душ (active button D)
    wts_updates[31275] = "|cffe4cfa3Поглощение душ|r"
    wts_updates[31337] = "|cffe4cfa3Поглощение душ|r (|cffffffffD|r)"
    wts_updates[30860] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно приносит в жертву союзных воинов поблизости до полного восстановления запаса здоровья и маны Хаккара.|r"

    # A1EK: Влияние Хаккара (hidden debuff)
    wts_updates[19419] = "|cffe4cfa3Влияние Хаккара (дебафф)|r"

    # Hero: Bwonsamdi (O05L / O05C)
    # A1EV: Сила иного мира (4 lvls, Q)
    wts_updates[31205] = "|cffe4cfa3Сила иного мира|r"
    a1ev_tips = [31206, 31208, 31238, 31951]
    a1ev_ubs = [32342, 32343, 32344, 32347]
    for l in range(1, 5):
        wts_updates[a1ev_tips[l - 1]] = f"|cffe4cfa3Сила иного мира|r [|cffffffff{l}|r] (|cffffffffQ|r)"
        wts_updates[a1ev_ubs[l - 1]] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наполняет выбранного воина астральной силой Лоа, повышая его броню и урон от атак.|r"
    wts_updates[32063] = "|cffe4cfa3Сила иного мира|r [|cffffffff%d|r] (|cffffffffQ|r)"
    wts_updates[32339] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает броню и атаку выбранного союзного воина астральной мощью.|r"

    # A1EW: Поток смерти (4 lvls, Q alternate)
    wts_updates[27213] = "|cffe4cfa3Поток смерти|r"
    a1ew_tips = [32742, 32743, 32744, 32740]
    a1ew_ubs = [32745, 32746, 32747, 32741]
    for l in range(1, 5):
        wts_updates[a1ew_tips[l - 1]] = f"|cffe4cfa3Поток смерти|r [|cffffffff{l}|r] (|cffffffffQ|r)"
        wts_updates[a1ew_ubs[l - 1]] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает в секторе перед собой стаю призрачных нетопырей, наносящих урон врагам на пути.|r"
    wts_updates[27214] = "|cffe4cfa3Поток смерти|r [|cffffffff%d|r] (|cffffffffQ|r)"
    wts_updates[32748] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стаю призрачных нетопырей, поражающих противников на своём пути.|r"

    # A1EX: Слуги смерти (4 lvls, W)
    wts_updates[32749] = "|cffe4cfa3Слуги смерти|r"
    a1ex_tips = [32750, 32751, 32752, 32753]
    a1ex_ubs = [35067, 35068, 35069, 35070]
    a1ex_counts = ["2", "4", "9", "14"]
    a1ex_durs = ["40", "60", "80", "100"]
    for l in range(1, 5):
        wts_updates[a1ex_tips[l - 1]] = f"|cffe4cfa3Слуги смерти|r [|cffffffff{l}|r] (|cffffffffW|r)"
        wts_updates[a1ex_ubs[l - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оживляет |cffffffff{a1ex_counts[l-1]}|cffced4da павших воинов из трупов в области действия на |cffffffff{a1ex_durs[l-1]}|cffced4da сек.|r"
        )
    wts_updates[32758] = "|cffe4cfa3Слуги смерти|r [|cffffffff%d|r] (|cffffffffW|r)"
    wts_updates[32759] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает павших воинов из трупов в указанной области на службу Лоа Смерти.|r"

    # A1EY: Черед ещё не настал (4 lvls, E)
    wts_updates[32762] = "|cffe4cfa3Черед ещё не настал|r"
    a1ey_tips = [32763, 32760, 32764, 32765]
    a1ey_ubs = [34243, 34239, 34587, 34591]
    a1ey_counts = ["1", "4", "8", "13"]
    for l in range(1, 5):
        wts_updates[a1ey_tips[l - 1]] = f"|cffe4cfa3Черед ещё не настал|r [|cffffffff{l}|r] (|cffffffffE|r)"
        wts_updates[a1ey_ubs[l - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает души погибших из загробного мира, воскрешая до |cffffffff{a1ey_counts[l-1]}|cffced4da павших союзников вокруг героя.|r"
        )
    wts_updates[32769] = "|cffe4cfa3Черед ещё не настал|r [|cffffffff%d|r] (|cffffffffE|r)"
    wts_updates[32770] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Воскрешает павших союзных воинов и героев вокруг Бвонсамди.|r"

    # A1ER: Материальная форма (2 lvls, R)
    wts_updates[30656] = "|cffe4cfa3Материальная форма|r"
    wts_updates[30658] = "|cffe4cfa3Материальная форма|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[30659] = "|cffe4cfa3Материальная форма|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[30662] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бвонсамди переносится в материальный мир живых, нанося |cffe69a8d225|cffced4da ед. урона окружающим врагам при приземлении и получая возможность напрямую сражаться.|r"
    wts_updates[30663] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бвонсамди переносится в материальный мир живых, нанося |cffe69a8d225|cffced4da ед. урона окружающим врагам при приземлении и получая возможность напрямую сражаться.|r"
    wts_updates[32882] = "|cffe4cfa3Материальная форма|r [|cffffffff%d|r] (|cffffffffR|r)"
    wts_updates[32883] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет Бвонсамди переходить в физический мир для прямого участия в битве.|r"

    # A1ES: Иной мир
    wts_updates[30679] = "|cffe4cfa3Иной мир|r"
    wts_updates[30680] = "|cffe4cfa3Иной мир|r"

    # A1ET: Лоа Смерти (passive)
    wts_updates[32738] = "|cffe4cfa3Лоа Смерти|r"
    wts_updates[32739] = "|cffe4cfa3Лоа Смерти|r"
    wts_updates[40244] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бвонсамди черпает силу из мира духов. Каждая гибель противника перманентно увеличивает максимальный запас здоровья (+1), маны (+6) и скорость регенерации маны (+0.05) героя.|r"

    # A1EZ: Астральная невидимость
    wts_updates[10894] = "|cffe4cfa3Астральная невидимость|r"

    # A1EU: Метка смерти
    wts_updates[31193] = "|cffe4cfa3Метка смерти|r"

    # Dummies
    wts_updates[38702] = "|cffe4cfa3Сглаз (эффект)|r"
    wts_updates[32145] = "|cffe4cfa3Смерть и разложение (эффект)|r"

    # =========================================================================
    # 7. BUFFS (7 custom buffs)
    # =========================================================================
    # B076: Зрение идола
    wts_updates[15968] = "|cffe4cfa3Зрение идола|r"
    wts_updates[16119] = "|cffa6afb8ЭФФЕКТ:|cffced4da Урон атак увеличен на |cffc8e087+5|cffced4da благодаря близости Сторожевого идола.|r"

    # B07A: Жажда крови
    wts_updates[28163] = "|cffe4cfa3Жажда крови|r"
    wts_updates[28165] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки и передвижения цели |cffc8e087значительно увеличена|cffced4da.|r"

    # B07B: Ярость Джунглей
    wts_updates[31179] = "|cffe4cfa3Ярость джунглей|r"
    wts_updates[31183] = "|cffa6afb8ЭФФЕКТ:|cffced4da Полученные ранения пробуждают ярость: урон от атак |cffc8e087увеличен|cffced4da.|r"

    # B07C: Влияние Хаккара
    wts_updates[31142] = "|cffe4cfa3Влияние Хаккара|r"
    wts_updates[31209] = "|cffa6afb8ЭФФЕКТ:|cffced4da Под действием тёмной силы Хаккара урон дистанционных атак войск |cffc8e087увеличен|cffced4da.|r"

    # B07D: Ядовитый остаток
    wts_updates[31211] = "|cffe4cfa3Ядовитый остаток|r"
    wts_updates[31231] = "|cffa6afb8ЭФФЕКТ:|cffced4da Цель находится в ядовитой слизи: скорость передвижения и атаки |cffe69a8dснижена|cffced4da.|r"

    # B07E: Пленение
    wts_updates[32179] = "|cffe4cfa3Пленение|r"

    # B07G: Сила Лоа Смерти
    wts_updates[32480] = "|cffe4cfa3Сила Лоа Смерти|r"

    # =========================================================================
    # BUILD PLAN PAYLOAD & CATEGORIES
    # =========================================================================
    plan_payload = {
        "race": "JungleTrolls",
        "race_id": 30,
        "total_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "categories": {
            "selection": ["A1DZ", "R0IH", "R0IR", "A1EP", "A1EQ"],
            "buildings": [
                "h0N5", "h0N1", "h0N6", "h0N2", "h0MY",
                "h0MW", "h0MX", "h0N0", "h0N3", "h0D3"
            ],
            "units": [
                "o04Q", "o04M", "o05K", "o04L", "o05E", "o04O", "o04R",
                "o04N", "o04P", "o04S", "o05J", "o04U", "o05G", "o05I"
            ],
            "heroes": [
                "O054", "O05A", "O05D", "O055", "O05L", "O05C"
            ],
            "upgrades": [
                "R0IH", "R0IR", "R0I8", "R0I9", "R0IA", "R0IB", "R0IC",
                "R0ID", "R0II", "R0IJ", "R0IK", "R0IL", "R0IM", "R0IN"
            ],
            "abilities": [
                "A1DZ", "A1EP", "A1EQ", "A1D0", "A1D1", "A1CX", "A1DU",
                "A1EJ", "A1EI", "A1DF", "A1DG", "A1DH", "A1DX", "A1D2",
                "A1D3", "A1D5", "A1DT", "A1DV", "A1DW", "A1F4", "A1F5", "A1F6",
                "A1DY", "A1EH", "A1DK", "A1DN", "A1DI",
                "AOhw", "A1E0", "AOsw",
                "A1E2", "A1E5", "A1E3", "A1E4",
                "A1E6", "A1EA", "A1E8", "A1E9",
                "A1DC", "A1DM", "A1EL", "A1DB", "A1DD", "A1EM", "A1EK",
                "A1EV", "A1EW", "A1EX", "A1EY", "A1ER", "A1ES", "A1ET", "A1EZ", "A1EU",
                "A1E1", "A1E7"
            ],
            "buffs": [
                "B076", "B07A", "B07B", "B07C", "B07D", "B07E", "B07G"
            ]
        },
        "checks_def": checks_def
    }

    plan_file = folder / "jungletrolls_plan.json"
    plan_file.write_text(json.dumps(plan_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved jungletrolls_plan.json ({len(wts_updates)} strings, {len(checks_def)} checks)")

    # =========================================================================
    # GENERATE 7 CATEGORY JSON FILES
    # =========================================================================
    dump_path = ROOT / "scripts/jungletrolls_raw_dump.json"
    dump = json.loads(dump_path.read_text(encoding="utf-8")) if dump_path.exists() else {}

    # 1. jungletrolls_selection.json
    sel_data = {
        "scope": "Тролли джунглей (JungleTrolls): подсказка выбора расы A1DZ, маркеры и выбор фракций",
        "object": "A1DZ",
        "variants": ["SD"],
        "hotkey": {"value": "C"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_JungleTrolls регистрирует способность A1DZ.",
            "При выборе создаются 5 рабочих o04Q, исследуется маркер R0IH, запускается StartJungleTrolls.",
            "Горячая клавиша C, создатель и куратор VinerX, сложность 3/5 (●●●○○), период «WoW: Classic» — «Battle for Azeroth»."
        ],
        "strings": [
            {"field": "name", "wts_id": 32019, "after": wts_updates[32019]},
            {"field": "tip1", "wts_id": 32430, "after": wts_updates[32430]},
            {"field": "ubertip1", "wts_id": 35186, "after": wts_updates[35186]}
        ],
        "markers": [
            {
                "id": "R0IH",
                "name": "Тролли джунглей (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 32049, "after": wts_updates[32049]},
                    {"field": "tip1", "wts_id": 32050, "after": wts_updates[32050]}
                ]
            },
            {
                "id": "R0IR",
                "name": "Чёрное Копьё (маркер подфракции)",
                "strings": [
                    {"field": "name1", "wts_id": 32959, "after": wts_updates[32959]},
                    {"field": "tip1", "wts_id": 32960, "after": wts_updates[32960]}
                ]
            }
        ],
        "branch_choices": [
            {
                "id": "A1EP",
                "name": "Чёрное Копьё",
                "hotkey": "E",
                "strings": [
                    {"field": "name", "wts_id": 32646, "after": wts_updates[32646]},
                    {"field": "tip1", "wts_id": 32647, "after": wts_updates[32647]},
                    {"field": "ubertip1", "wts_id": 32862, "after": wts_updates[32862]}
                ]
            },
            {
                "id": "A1EQ",
                "name": "Империя Гурубаши",
                "hotkey": "R",
                "strings": [
                    {"field": "name", "wts_id": 32650, "after": wts_updates[32650]},
                    {"field": "tip1", "wts_id": 32651, "after": wts_updates[32651]},
                    {"field": "ubertip1", "wts_id": 32863, "after": wts_updates[32863]}
                ]
            }
        ]
    }
    (folder / "jungletrolls_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote jungletrolls_selection.json")

    # 2. jungletrolls_buildings.json
    bld_entries = []
    for b in dump.get("buildings", []):
        b_id = b["id"]
        if b_id not in plan_payload["categories"]["buildings"]:
            continue
        hk_val = b.get("hotkey")
        entry = {
            "id": b_id,
            "hotkey": hk_val,
            "strings": []
        }
        for fld in ["name", "tip", "ubertip"]:
            sid = b.get(f"{fld}_sid")
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": fld,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        bld_entries.append(entry)

    bld_payload = {
        "scope": "Тролли джунглей (JungleTrolls): категория 1 — Здания",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "jungletrolls_buildings.json").write_text(json.dumps(bld_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote jungletrolls_buildings.json")

    # 3. jungletrolls_units.json
    unit_entries = []
    for u in dump.get("units", []):
        u_id = u["id"]
        if u_id not in plan_payload["categories"]["units"]:
            continue
        hk_val = u.get("hotkey")
        entry = {
            "id": u_id,
            "hotkey": hk_val,
            "strings": []
        }
        for fld in ["name", "tip", "ubertip"]:
            sid = u.get(f"{fld}_sid")
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": fld,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        unit_entries.append(entry)

    unit_payload = {
        "scope": "Тролли джунглей (JungleTrolls): категория 2 — Юниты",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "jungletrolls_units.json").write_text(json.dumps(unit_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote jungletrolls_units.json")

    # 4. jungletrolls_heroes.json
    hero_entries = []
    for h in dump.get("heroes", []):
        h_id = h["id"]
        if h_id not in plan_payload["categories"]["heroes"]:
            continue
        hk_val = h.get("hotkey")
        entry = {
            "id": h_id,
            "hotkey": hk_val,
            "propernames": h.get("propernames"),
            "strings": []
        }
        for fld in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            sid = h.get(f"{fld}_sid")
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": fld,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        hero_entries.append(entry)

    hero_payload = {
        "scope": "Тролли джунглей (JungleTrolls): категория 3 — Герои",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "jungletrolls_heroes.json").write_text(json.dumps(hero_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote jungletrolls_heroes.json")

    # 5. jungletrolls_abilities.json
    abil_entries = []
    for a in dump.get("abilities", []):
        a_id = a["id"]
        if a_id not in plan_payload["categories"]["abilities"]:
            continue
        entry = {
            "id": a_id,
            "levels": a.get("levels", 1),
            "strings": []
        }
        name_sid = a.get("name_sid")
        if name_sid and name_sid in wts_updates:
            entry["strings"].append({"field": "name", "wts_id": name_sid, "after": wts_updates[name_sid]})
        for l in range(1, a.get("levels", 1) + 1):
            t_sid = a.get("tips", {}).get(f"tip{l}", {}).get("sid")
            if t_sid and t_sid in wts_updates:
                entry["strings"].append({"field": f"tip{l}", "wts_id": t_sid, "after": wts_updates[t_sid]})
            ub_sid = a.get("ubertips", {}).get(f"ubertip{l}", {}).get("sid")
            if ub_sid and ub_sid in wts_updates:
                entry["strings"].append({"field": f"ubertip{l}", "wts_id": ub_sid, "after": wts_updates[ub_sid]})
        rtip_sid = a.get("researchtip_sid")
        if rtip_sid and rtip_sid in wts_updates:
            entry["strings"].append({"field": "researchtip", "wts_id": rtip_sid, "after": wts_updates[rtip_sid]})
        rub_sid = a.get("researchubertip_sid")
        if rub_sid and rub_sid in wts_updates:
            entry["strings"].append({"field": "researchubertip", "wts_id": rub_sid, "after": wts_updates[rub_sid]})
        if entry["strings"]:
            abil_entries.append(entry)

    abil_payload = {
        "scope": "Тролли джунглей (JungleTrolls): категория 4 — Способности",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "jungletrolls_abilities.json").write_text(json.dumps(abil_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote jungletrolls_abilities.json")

    # 6. jungletrolls_research.json
    res_entries = []
    for up in dump.get("upgrades", []):
        u_id = up["id"]
        if u_id not in plan_payload["categories"]["upgrades"]:
            continue
        entry = {
            "id": u_id,
            "levels": up.get("levels", 1),
            "strings": []
        }
        for l in range(1, up.get("levels", 1) + 1):
            n_sid = up.get("names", {}).get(f"name{l}", {}).get("sid")
            if n_sid and n_sid in wts_updates:
                entry["strings"].append({"field": f"name{l}", "wts_id": n_sid, "after": wts_updates[n_sid]})
            t_sid = up.get("tips", {}).get(f"tip{l}", {}).get("sid")
            if t_sid and t_sid in wts_updates:
                entry["strings"].append({"field": f"tip{l}", "wts_id": t_sid, "after": wts_updates[t_sid]})
            ub_sid = up.get("ubertips", {}).get(f"ubertip{l}", {}).get("sid")
            if ub_sid and ub_sid in wts_updates:
                entry["strings"].append({"field": f"ubertip{l}", "wts_id": ub_sid, "after": wts_updates[ub_sid]})
        if entry["strings"]:
            res_entries.append(entry)

    res_payload = {
        "scope": "Тролли джунглей (JungleTrolls): категория 5 — Исследования",
        "upgrades_count": len(res_entries),
        "variants": ["SD"],
        "upgrades": res_entries
    }
    (folder / "jungletrolls_research.json").write_text(json.dumps(res_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote jungletrolls_research.json")

    # 7. jungletrolls_audit.json
    audit_payload = {
        "race": "Тролли джунглей (JungleTrolls)",
        "race_id": 30,
        "selection_ability": "A1DZ",
        "selection_markers": ["R0IH", "R0IR"],
        "branch_choices": ["A1EP", "A1EQ"],
        "objects_audit": {
            "buildings": {
                "count": len(plan_payload["categories"]["buildings"]),
                "ids": plan_payload["categories"]["buildings"],
                "economy_building": {
                    "id": "h0N2",
                    "name": "Жилище",
                    "food_provided": 10,
                    "gold_income_per_25s": True,
                    "verified_via": "01_core_economy.lua and unit object stats"
                }
            },
            "units": {
                "count": len(plan_payload["categories"]["units"]),
                "ids": plan_payload["categories"]["units"]
            },
            "heroes": {
                "count": len(plan_payload["categories"]["heroes"]),
                "ids": plan_payload["categories"]["heroes"],
                "names": {
                    "O054": "Темный охотник (Интеллект, дальний бой)",
                    "O05A": "Мастер клинка (Ловкость, ближний бой)",
                    "O05D": "Низвергатель (Интеллект, дальний бой)",
                    "O055": "Хаккар Свежеватель Душ (Легендарный герой Гурубаши — Сила, ближний бой)",
                    "O05L": "Лоа Смерти Бвонсамди (Легендарный герой Чёрного Копья — Интеллект, дальний бой, астрал)",
                    "O05C": "Бвонсамди (материальная форма — Интеллект, дальний бой)"
                }
            },
            "upgrades": {
                "count": len(plan_payload["categories"]["upgrades"]),
                "ids": plan_payload["categories"]["upgrades"]
            },
            "abilities": {
                "count": len(plan_payload["categories"]["abilities"]),
                "ids": plan_payload["categories"]["abilities"]
            },
            "buffs": {
                "count": len(plan_payload["categories"]["buffs"]),
                "ids": plan_payload["categories"]["buffs"]
            }
        },
        "wts_summary": {
            "total_updates": len(wts_updates),
            "string_ids": sorted(list(wts_updates.keys()))
        }
    }
    (folder / "jungletrolls_audit.json").write_text(json.dumps(audit_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote jungletrolls_audit.json")
    print("All preparation and registries completed successfully!")

if __name__ == "__main__":
    main()
