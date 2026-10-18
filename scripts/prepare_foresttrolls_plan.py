# -*- coding: utf-8 -*-
"""Prepare complete UI text standardization plan and registries for Forest Trolls (Лесные тролли, Race 32)."""
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
    # A1FN: Выбор расы Лесные тролли (D)
    wts_updates[38909] = "|cffe4cfa3Лесные тролли|r"
    wts_updates[38910] = "|cffe4cfa3Лесные тролли|r (|cffffffffD|r)"
    wts_updates[32514] = (
        "|cffa6afb8РАСА:|cffced4da Свирепые лесные воители Зул'Амана с прирождённой регенерацией ран, боевым безумием и благословением звериных Лоа.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«The Burning Crusade» — «Cataclysm»|r|n|n"
        "|cffced4daЛесные тролли — древняя и могущественная ветвь троллей Азерота, некогда правившая обширными землями империи Амани. Обладая непревзойдённой регенерацией тканей и яростью, они становятся смертоноснее по мере получения ран. В боях лесные тролли черпают силу звериных богов — Лоа Медведя, Волка и Ястреба, обращаясь в могучих полубожественных исполинов и сокрушая врагов неодолимым натиском.|r"
    )
    checks_def.append({"type": "ability", "id": "A1FN", "field": "name", "expected": wts_updates[38909]})
    checks_def.append({"type": "ability", "id": "A1FN", "field": "tip1", "expected": wts_updates[38910]})
    checks_def.append({"type": "ability", "id": "A1FN", "field": "ubertip1", "expected": wts_updates[32514]})

    # R0J1: Маркер расы (Лесные тролли)
    wts_updates[34173] = "|cffe4cfa3Лесные тролли|r"
    wts_updates[34174] = "|cffe4cfa3Лесные тролли|r"
    checks_def.append({"type": "upgrade", "id": "R0J1", "field": "name1", "expected": wts_updates[34173]})
    checks_def.append({"type": "upgrade", "id": "R0J1", "field": "tip1", "expected": wts_updates[34174]})

    # =========================================================================
    # 2. BUILDINGS (11 buildings)
    # =========================================================================
    # h0MT: Дом вождей (Q)
    wts_updates[21796] = "|cffe4cfa3Дом вождей|r"
    wts_updates[33538] = "|cffe4cfa3Дом вождей|r (|cffffffffQ|r)"
    wts_updates[32614] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание лесных троллей первой ступени. Обеспечивает добычу ресурсов, начальный запас пищи и основу базы.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРемесленник|cffced4da: строитель, добывающий древесину и возводящий строения.|n- |cffa9c7deСобиратель|cffced4da: базовый охотник и сборщик ресурсов.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКрепость вождей|cffced4da: открывает доступ к передовым сооружениям и технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MT", "field": "name", "expected": wts_updates[21796]})
    checks_def.append({"type": "unit", "id": "h0MT", "field": "tip", "expected": wts_updates[33538]})
    checks_def.append({"type": "unit", "id": "h0MT", "field": "ubertip", "expected": wts_updates[32614]})

    # h0N8: Крепость вождей (Z)
    wts_updates[32338] = "|cffe4cfa3Крепость вождей|r"
    wts_updates[32345] = "|cffe4cfa3Крепость вождей|r (|cffffffffZ|r)"
    wts_updates[33548] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание лесных троллей второй ступени. Существенно увеличивает запас пищи и открывает доступ к новым постройкам.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРемесленник|cffced4da: рабочий-строитель.|n- |cffa9c7deСобиратель|cffced4da: охотник и добытчик.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЦитадель вождей|cffced4da: высшая ступень развития столицы.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N8", "field": "name", "expected": wts_updates[32338]})
    checks_def.append({"type": "unit", "id": "h0N8", "field": "tip", "expected": wts_updates[32345]})
    checks_def.append({"type": "unit", "id": "h0N8", "field": "ubertip", "expected": wts_updates[33548]})

    # h0N9: Цитадель вождей (Z)
    wts_updates[32665] = "|cffe4cfa3Цитадель вождей|r"
    wts_updates[32710] = "|cffe4cfa3Цитадель вождей|r (|cffffffffZ|r)"
    wts_updates[33549] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание лесных троллей третьей ступени. Обеспечивает максимальный запас пищи и открывает доступ ко всем технологиям расы.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРемесленник|cffced4da: рабочий-строитель.|n- |cffa9c7deСобиратель|cffced4da: охотник и добытчик.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N9", "field": "name", "expected": wts_updates[32665]})
    checks_def.append({"type": "unit", "id": "h0N9", "field": "tip", "expected": wts_updates[32710]})
    checks_def.append({"type": "unit", "id": "h0N9", "field": "ubertip", "expected": wts_updates[33549]})

    # h0MV: Лачуга (A)
    wts_updates[31459] = "|cffe4cfa3Лачуга|r"
    wts_updates[33539] = "|cffe4cfa3Лачуга|r (|cffffffffA|r)"
    wts_updates[37485] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Традиционное жилище троллей. Обеспечивает лимит пищи и приносит регулярный доход золота в казну каждые |cffffffff25|cffced4da сек.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MV", "field": "name", "expected": wts_updates[31459]})
    checks_def.append({"type": "unit", "id": "h0MV", "field": "tip", "expected": wts_updates[33539]})
    checks_def.append({"type": "unit", "id": "h0MV", "field": "ubertip", "expected": wts_updates[37485]})

    # h0MS: Казармы (W)
    wts_updates[31375] = "|cffe4cfa3Казармы|r"
    wts_updates[33537] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[32323] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военный лагерь для подготовки базовой пехоты, стрелков и осадных орудий лесных троллей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМетатель топоров|cffced4da: воин дальнего боя.|n- |cffa9c7deСобиратель|cffced4da: лёгкий боец с яростью.|n- |cffa9c7deКатапульта|cffced4da: дальнобойное осадное орудие.|n- |cffa9c7deМастер топора|cffced4da: усиленный стрелок (требует исследования).|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМастер топора|cffced4da: улучшает метателей топоров до мастеров топора.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MS", "field": "name", "expected": wts_updates[31375]})
    checks_def.append({"type": "unit", "id": "h0MS", "field": "tip", "expected": wts_updates[33537]})
    checks_def.append({"type": "unit", "id": "h0MS", "field": "ubertip", "expected": wts_updates[32323]})

    # h0MR: Колизей (D)
    wts_updates[31447] = "|cffe4cfa3Колизей|r"
    wts_updates[10895] = "|cffe4cfa3Колизей|r (|cffffffffD|r)"
    wts_updates[33545] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Боевая арена для тренировки элитных воинов, всадников и берсерков, а также усиления их выносливости.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБерсерк|cffced4da: неистовый боец ближнего боя.|n- |cffa9c7deМастер копья|cffced4da: тяжёлый копейщик с оглушающим броском.|n- |cffa9c7deНаездник на медведе|cffced4da: мощная тяжёлая кавалерия.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deСнадобья силы|cffced4da: повышает запас здоровья берсерков и наездников на медведях.|n- |cffa9c7deШипы на медведе|cffced4da: дарует всадникам шипастую броню, отражающую урон.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MR", "field": "name", "expected": wts_updates[31447]})
    checks_def.append({"type": "unit", "id": "h0MR", "field": "tip", "expected": wts_updates[10895]})
    checks_def.append({"type": "unit", "id": "h0MR", "field": "ubertip", "expected": wts_updates[33545]})

    # h0MZ: Ложе Вуду (R)
    wts_updates[31486] = "|cffe4cfa3Ложе Вуду|r"
    wts_updates[27806] = "|cffe4cfa3Ложе Вуду|r (|cffffffffR|r)"
    wts_updates[33541] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Ритуальное святилище магии вуду. Обучает заклинателей и жрецов, а также совершенствует их магическое искусство.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЖрец|cffced4da: целитель, рассеивающий вражеские чары и усиливающий соратников пламенем.|n- |cffa9c7deЗаклинатель|cffced4da: боевой маг, призывающий змеиные идолы и вызывающий безумие в бою.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбучение жрецов|cffced4da: повышает характеристики и открывает способности жрецов.|n- |cffa9c7deОбучение заклинателей|cffced4da: повышает характеристики и открывает способности заклинателей.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MZ", "field": "name", "expected": wts_updates[31486]})
    checks_def.append({"type": "unit", "id": "h0MZ", "field": "tip", "expected": wts_updates[27806]})
    checks_def.append({"type": "unit", "id": "h0MZ", "field": "ubertip", "expected": wts_updates[33541]})

    # h0MU: Алтарь Лоа (S)
    wts_updates[24551] = "|cffe4cfa3Алтарь Лоа|r"
    wts_updates[27805] = "|cffe4cfa3Алтарь Лоа|r (|cffffffffS|r)"
    wts_updates[37464] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священный алтарь духов Лоа. Служит для призыва и воскрешения павших героев, а также найма воинов, впитавших силу звериных богов.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deПовелитель проклятий|cffced4da, |cffa9c7deМастер клинка|cffced4da, |cffa9c7deВоеначальник|cffced4da.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТролль-ястреб|cffced4da: маг воздуха с грозовой бурей и аурой маны.|n- |cffa9c7deТролль-медведь|cffced4da: исполин с рассекающим ударом и аурой защиты.|n- |cffa9c7deТролль-волк|cffced4da: свирепый зверь с аурой атаки и жаждой битвы.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМетоды поглощения Лоа|cffced4da: усиливает аватары Лоа и открывает их способности.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MU", "field": "name", "expected": wts_updates[24551]})
    checks_def.append({"type": "unit", "id": "h0MU", "field": "tip", "expected": wts_updates[27805]})
    checks_def.append({"type": "unit", "id": "h0MU", "field": "ubertip", "expected": wts_updates[37464]})

    # h0N4: Сторожевой пост (Z)
    wts_updates[31513] = "|cffe4cfa3Сторожевой пост|r"
    wts_updates[32936] = "|cffe4cfa3Сторожевой пост|r (|cffffffffZ|r)"
    wts_updates[32935] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение лесных троллей. Обстреливает приближающихся противников метательными снарядами.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N4", "field": "name", "expected": wts_updates[31513]})
    checks_def.append({"type": "unit", "id": "h0N4", "field": "tip", "expected": wts_updates[32936]})
    checks_def.append({"type": "unit", "id": "h0N4", "field": "ubertip", "expected": wts_updates[32935]})

    # h0N7: Лесопилка (E)
    wts_updates[32326] = "|cffe4cfa3Лесопилка|r"
    wts_updates[33635] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[33547] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр сбора древесины и кузница улучшений оружия, доспехов, регенерации и прочности укреплений лесных троллей.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deСтальное оружие|cffced4da: повышает урон немагических войск.|n- |cffa9c7deСтальная броня|cffced4da: увеличивает броню всех видов войск.|n- |cffa9c7deМетоды регенерации|cffced4da: ускоряет восстановление здоровья воинов.|n- |cffa9c7deКорпуса построек|cffced4da: увеличивает запас здоровья и броню зданий.|n- |cffa9c7deУлучшенные топоры|cffced4da: повышает количество древесины, переносимой работниками.|r"
    )
    checks_def.append({"type": "unit", "id": "h0N7", "field": "name", "expected": wts_updates[32326]})
    checks_def.append({"type": "unit", "id": "h0N7", "field": "tip", "expected": wts_updates[33635]})
    checks_def.append({"type": "unit", "id": "h0N7", "field": "ubertip", "expected": wts_updates[33547]})

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
    # 3. UNITS (16 units)
    # =========================================================================
    # o04V: Ремесленник (Q)
    wts_updates[31180] = "|cffe4cfa3Ремесленник|r"
    wts_updates[39299] = "|cffe4cfa3Ремесленник|r (|cffffffffQ|r)"
    wts_updates[36601] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий лесных троллей. Добывает древесину, возводит и ремонтирует постройки.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНебольшой скачок|cffced4da: мгновенно переносит рабочего на небольшое расстояние.|n- |cffa9c7deСвирепость Лесов|cffced4da: расовая ярость, ускоряющая атаки при получении ранений.|n- |cffa9c7deРемонт|cffced4da: чинит повреждённые здания за счёт ресурсов.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04V", "field": "name", "expected": wts_updates[31180]})
    checks_def.append({"type": "unit", "id": "o04V", "field": "tip", "expected": wts_updates[39299]})
    checks_def.append({"type": "unit", "id": "o04V", "field": "ubertip", "expected": wts_updates[36601]})

    # o04X: Собиратель (W)
    wts_updates[31234] = "|cffe4cfa3Собиратель|r"
    wts_updates[31464] = "|cffe4cfa3Собиратель|r (|cffffffffW|r)"
    wts_updates[6796] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый разведчик и охотник племени. Способен сражаться на передовой и заготавливать древесину.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСвирепость Лесов|cffced4da: ускоряет скорость атаки при потере здоровья.|n- |cffa9c7deСбор древесины|cffced4da: способен рубить и носить лес.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04X", "field": "name", "expected": wts_updates[31234]})
    checks_def.append({"type": "unit", "id": "o04X", "field": "tip", "expected": wts_updates[31464]})
    checks_def.append({"type": "unit", "id": "o04X", "field": "ubertip", "expected": wts_updates[6796]})

    # o04W: Метатель топоров (Q)
    wts_updates[31200] = "|cffe4cfa3Метатель топоров|r"
    wts_updates[32946] = "|cffe4cfa3Метатель топоров|r (|cffffffffQ|r)"
    wts_updates[6795] = (
        "|cffa6afb8ЮНИТ:|cffced4da Рядовой стрелок лесных троллей. Поражает врагов тяжёлыми метательными топорами на средней дистанции.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБерсерк|cffced4da: кратковременно увеличивает скорость атаки ценой получаемого урона.|n- |cffa9c7deСвирепость Лесов|cffced4da: увеличивает скорость боя при получении ранений.|n- |cffa9c7deМастер топора|cffced4da: может быть улучшен в казармах до мастера топора.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04W", "field": "name", "expected": wts_updates[31200]})
    checks_def.append({"type": "unit", "id": "o04W", "field": "tip", "expected": wts_updates[32946]})
    checks_def.append({"type": "unit", "id": "o04W", "field": "ubertip", "expected": wts_updates[6795]})

    # o04Y: Мастер топора (Q)
    wts_updates[31237] = "|cffe4cfa3Мастер топора|r"
    wts_updates[35547] = "|cffe4cfa3Мастер топора|r (|cffffffffQ|r)"
    wts_updates[8212] = (
        "|cffa6afb8ЮНИТ:|cffced4da Закалённый в бесчисленных битвах стрелок. Обладает повышенными характеристиками и смертоносной точностью бросков.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБерсерк|cffced4da: повышает скорость атаки на |cffffffff+35%|cffced4da, увеличивая получаемый урон на |cffe69a8d+30%|cffced4da.|n- |cffa9c7deСвирепость Лесов|cffced4da: повышает боевые характеристики по мере потери здоровья.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04Y", "field": "name", "expected": wts_updates[31237]})
    checks_def.append({"type": "unit", "id": "o04Y", "field": "tip", "expected": wts_updates[35547]})
    checks_def.append({"type": "unit", "id": "o04Y", "field": "ubertip", "expected": wts_updates[8212]})

    # o05F: Катапульта (E)
    wts_updates[31537] = "|cffe4cfa3Катапульта|r"
    wts_updates[33633] = "|cffe4cfa3Катапульта|r (|cffffffffE|r)"
    wts_updates[10753] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлое осадное орудие лесных троллей дальнего действия. Наносит колоссальный урон вражеским укреплениям и скоплениям пехоты.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05F", "field": "name", "expected": wts_updates[31537]})
    checks_def.append({"type": "unit", "id": "o05F", "field": "tip", "expected": wts_updates[33633]})
    checks_def.append({"type": "unit", "id": "o05F", "field": "ubertip", "expected": wts_updates[10753]})

    # o04Z: Берсерк (Q)
    wts_updates[31321] = "|cffe4cfa3Берсерк|r"
    wts_updates[32961] = "|cffe4cfa3Берсерк|r (|cffffffffQ|r)"
    wts_updates[36647] = (
        "|cffa6afb8ЮНИТ:|cffced4da Свирепый воин ближнего боя, не знающий страха и боли. Прорубает ряды противника сокрушительным шквалом ударов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБерсерк|cffced4da: активирует боевое безумие, ускоряя атаки на |cffffffff+35%|cffced4da ценой получаемого урона.|n- |cffa9c7deСвирепость Лесов|cffced4da: ускоряет удары по мере потери здоровья.|n- |cffa9c7deСнадобья силы|cffced4da: увеличивает запас здоровья после исследования в Колизее.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o04Z", "field": "name", "expected": wts_updates[31321]})
    checks_def.append({"type": "unit", "id": "o04Z", "field": "tip", "expected": wts_updates[32961]})
    checks_def.append({"type": "unit", "id": "o04Z", "field": "ubertip", "expected": wts_updates[36647]})

    # o053: Мастер копья (W)
    wts_updates[32934] = "|cffe4cfa3Мастер копья|r"
    wts_updates[32440] = "|cffe4cfa3Мастер копья|r (|cffffffffW|r)"
    wts_updates[10615] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый копейщик лесных троллей. Поражает врагов с дистанции и выводит из строя опасные цели тяжёлым аманийским копьём.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАманийское копьё|cffced4da: бросает копьё во врага, нанося |cffffffff65|cffced4da ед. урона и оглушая его на |cffffffff2|cffced4da сек.|n- |cffa9c7deБерсерк|cffced4da: кратковременно увеличивает скорость атаки на |cffffffff+35%|cffced4da.|n- |cffa9c7deСвирепость Лесов|cffced4da: усиливает боевые характеристики при получении ранений.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o053", "field": "name", "expected": wts_updates[32934]})
    checks_def.append({"type": "unit", "id": "o053", "field": "tip", "expected": wts_updates[32440]})
    checks_def.append({"type": "unit", "id": "o053", "field": "ubertip", "expected": wts_updates[10615]})

    # o050: Наездник на медведе (E)
    wts_updates[31324] = "|cffe4cfa3Наездник на медведе|r"
    wts_updates[31534] = "|cffe4cfa3Наездник на медведе|r (|cffffffffE|r)"
    wts_updates[9380] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий всадник на боевом медведе. Обладает огромным запасом здоровья, оглушает противников и держит передовую строя.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСильный удар|cffced4da: с вероятностью |cffffffff15%|cffced4da наносит |cffffffff+15|cffced4da ед. урона и оглушает врага на |cffffffff1|cffced4da сек.|n- |cffa9c7deАманийские шипы|cffced4da: после исследования «Шипов на медведе» повышает броню на |cffc8e087+2|cffced4da и отражает |cffffffff7%|cffced4da урона ближнего боя.|n- |cffa9c7deСвирепость Лесов|cffced4da: боевой расовый бонус при потере здоровья.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o050", "field": "name", "expected": wts_updates[31324]})
    checks_def.append({"type": "unit", "id": "o050", "field": "tip", "expected": wts_updates[31534]})
    checks_def.append({"type": "unit", "id": "o050", "field": "ubertip", "expected": wts_updates[9380]})

    # o052: Жрец (Q)
    wts_updates[31330] = "|cffe4cfa3Жрец|r"
    wts_updates[32321] = "|cffe4cfa3Жрец|r (|cffffffffQ|r)"
    wts_updates[9695] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг-целитель лесных троллей. Поддерживает армию целебными ритуалами, развеивает вражеские чары и благословляет воинов огненной мощью.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЦелительный ритуал|cffced4da: восстанавливает |cffc8e08725|cffced4da ед. здоровья раненому союзнику.|n- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты магии в области и наносит |cffe69a8d200|cffced4da ед. урона призванным существам.|n- |cffa9c7deОгонь Амани|cffced4da: дарует соратнику |cffc8e087+15%|cffced4da к урону и |cffc8e087+3|cffced4da к броне на |cffffffff60|cffced4da сек.|n- |cffa9c7deЖертва кровью|cffced4da: приносит в жертву |cffe69a8d100|cffced4da ед. здоровья ради |cffc8e087100|cffced4da ед. маны.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o052", "field": "name", "expected": wts_updates[31330]})
    checks_def.append({"type": "unit", "id": "o052", "field": "tip", "expected": wts_updates[32321]})
    checks_def.append({"type": "unit", "id": "o052", "field": "ubertip", "expected": wts_updates[9695]})

    # o051: Заклинатель (W)
    wts_updates[31327] = "|cffe4cfa3Заклинатель|r"
    wts_updates[31535] = "|cffe4cfa3Заклинатель|r (|cffffffffW|r)"
    wts_updates[9656] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тёмный шаман армии троллей. Поражает врагов ударами духов, расставляет защитные тотемы и вводит воинов в безудержное неистовство.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУдары духов|cffced4da: обстреливает выбранную область сгустками магии вуду.|n- |cffa9c7deЗмеиный идол|cffced4da: призывает стреляющий тотем, атакующий наземные и воздушные цели.|n- |cffa9c7deБешенство|cffced4da: ускоряет атаку до |cffffffff4|cffced4da союзников на |cffffffff+30%|cffced4da ценой потери |cffe69a8d3|cffced4da ед. здоровья/сек.|n- |cffa9c7deЖертва кровью|cffced4da: жертвует здоровьем ради мгновенного восстановления маны.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o051", "field": "name", "expected": wts_updates[31327]})
    checks_def.append({"type": "unit", "id": "o051", "field": "tip", "expected": wts_updates[31535]})
    checks_def.append({"type": "unit", "id": "o051", "field": "ubertip", "expected": wts_updates[9656]})

    # o05O: Тролль-ястреб (Q)
    wts_updates[31402] = "|cffe4cfa3Тролль-ястреб|r"
    wts_updates[32942] = "|cffe4cfa3Тролль-ястреб|r (|cffffffffQ|r)"
    wts_updates[37776] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могущественный аватар Лоа Ястреба. Обрушивает на врагов разрушительные бури, молнии и питает союзных магов неисчерпаемой маной.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Ястреба|cffced4da: ускоряет регенерацию маны ближайших союзников на |cffc8e087+3|cffced4da ед./сек.|n- |cffa9c7deЦепная молния|cffced4da: поражает молнией до |cffffffff10|cffced4da врагов, нанося от |cffffffff70|cffced4da ед. урона.|n- |cffa9c7deБуря|cffced4da: призывает грозовой шторм, наносящий |cffffffff50|cffced4da ед. урона/сек. в области в течение |cffffffff15|cffced4da сек.|n- |cffa9c7deСмерть врагам Амани|cffced4da: атаки поражают сразу несколько целей.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05O", "field": "name", "expected": wts_updates[31402]})
    checks_def.append({"type": "unit", "id": "o05O", "field": "tip", "expected": wts_updates[32942]})
    checks_def.append({"type": "unit", "id": "o05O", "field": "ubertip", "expected": wts_updates[37776]})

    # o05M: Тролль-медведь (S) (clean from corrupted TRIGSTR_32950 'Отряды Тьмы')
    wts_updates[32950] = "|cffe4cfa3Тролль-медведь|r"
    wts_updates[33636] = "|cffe4cfa3Тролль-медведь|r (|cffffffffS|r)"
    wts_updates[37605] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий исполин, воплотивший силу Лоа Медведя. Обладает сокрушительными ударами по площади и защищает войско священным рёвом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Медведя|cffced4da: увеличивает броню окружающих союзников на |cffc8e087+4|cffced4da.|n- |cffa9c7deПрыжок медведя|cffced4da: совершает сокрушительный прыжок в цель, нанося урон по приземлении.|n- |cffa9c7deЧудодейственный рёв|cffced4da: дарует союзникам |cffc8e087+2|cffced4da к броне и ускоряет регенерацию здоровья на |cffffffff20|cffced4da сек.|n- |cffa9c7deОгромная сила|cffced4da: наносит |cffffffff15%|cffced4da рассекающего урона по площади вокруг цели.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05M", "field": "name", "expected": wts_updates[32950]})
    checks_def.append({"type": "unit", "id": "o05M", "field": "tip", "expected": wts_updates[33636]})
    checks_def.append({"type": "unit", "id": "o05M", "field": "ubertip", "expected": wts_updates[37605]})

    # o05N: Тролль-волк (X) (clean from corrupted TRIGSTR_32951 'Надавить на Даларан')
    wts_updates[32951] = "|cffe4cfa3Тролль-волк|r"
    wts_updates[33637] = "|cffe4cfa3Тролль-волк|r (|cffffffffX|r)"
    wts_updates[37750] = (
        "|cffa6afb8ЮНИТ:|cffced4da Грозный хищный аватар Лоа Волка. Направляет первобытную ярость на усиление союзных войск и терзает врагов в ближнем бою.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Волка|cffced4da: увеличивает силу атак ближайших союзников на |cffc8e087+20%|cffced4da.|n- |cffa9c7deБезрассудный берсерк|cffced4da: дарует |cffffffff+100%|cffced4da к скорости атаки и |cffffffff+25%|cffced4da к скорости бега ценой получаемого урона.|n- |cffa9c7deУжасающий вой|cffced4da: снижает броню окружающих врагов на |cffe69a8d-3|cffced4da.|n- |cffa9c7deВкус битвы|cffced4da: наделяет окружающих союзников |cffc8e08725%|cffced4da вампиризмом на |cffffffff20|cffced4da сек.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o05N", "field": "name", "expected": wts_updates[32951]})
    checks_def.append({"type": "unit", "id": "o05N", "field": "tip", "expected": wts_updates[33637]})
    checks_def.append({"type": "unit", "id": "o05N", "field": "ubertip", "expected": wts_updates[37750]})

    # Naval: h0D6 (Фрегат), h0D5 (Дредноут)
    wts_updates[3002] = "|cffe4cfa3Фрегат|r"
    wts_updates[5542] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый боевой корабль Орды, патрулирующий прибрежные воды и атакующий морские и береговые цели.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0D6", "field": "name", "expected": wts_updates[3002]})
    checks_def.append({"type": "unit", "id": "h0D6", "field": "ubertip", "expected": wts_updates[5542]})

    wts_updates[10916] = "|cffe4cfa3Дредноут|r"
    wts_updates[10918] = "|cffe4cfa3Дредноут|r (|cffffffffE|r)"
    wts_updates[6926] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий бронированный флагман флота дальнего действия. Наносит сокрушительный урон кораблям и укреплениям противника.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0D5", "field": "name", "expected": wts_updates[10916]})
    checks_def.append({"type": "unit", "id": "h0D5", "field": "tip", "expected": wts_updates[10918]})
    checks_def.append({"type": "unit", "id": "h0D5", "field": "ubertip", "expected": wts_updates[6926]})

    # =========================================================================
    # 4. HEROES (3 heroes)
    # =========================================================================
    # O057: Мастер клинка (A)
    wts_updates[32962] = "|cffe4cfa3Мастер клинка|r"
    wts_updates[32965] = "|cffe4cfa3Мастер клинка|r (|cffffffffA|r)"
    wts_updates[32963] = "|cffe4cfa3Мастер клинка|r"
    wts_updates[32964] = "|cffe4cfa3Мастер клинка|r (|cffffffffA|r)"
    checks_def.append({"type": "unit", "id": "O057", "field": "name", "expected": wts_updates[32962]})
    checks_def.append({"type": "unit", "id": "O057", "field": "tip", "expected": wts_updates[32965]})
    checks_def.append({"type": "unit", "id": "O057", "field": "awakentip", "expected": wts_updates[32963]})
    checks_def.append({"type": "unit", "id": "O057", "field": "revivetip", "expected": wts_updates[32964]})

    # O058: Повелитель проклятий (Q)
    wts_updates[32966] = "|cffe4cfa3Повелитель проклятий|r"
    wts_updates[32969] = "|cffe4cfa3Повелитель проклятий|r (|cffffffffQ|r)"
    wts_updates[32967] = "|cffe4cfa3Повелитель проклятий|r"
    wts_updates[32968] = "|cffe4cfa3Повелитель проклятий|r (|cffffffffQ|r)"
    wts_updates[32978] = "Малакрас"
    checks_def.append({"type": "unit", "id": "O058", "field": "name", "expected": wts_updates[32966]})
    checks_def.append({"type": "unit", "id": "O058", "field": "tip", "expected": wts_updates[32969]})
    checks_def.append({"type": "unit", "id": "O058", "field": "awakentip", "expected": wts_updates[32967]})
    checks_def.append({"type": "unit", "id": "O058", "field": "revivetip", "expected": wts_updates[32968]})
    checks_def.append({"type": "unit", "id": "O058", "field": "propernames", "expected": wts_updates[32978]})

    # O059: Военачальник (Z)
    wts_updates[32970] = "|cffe4cfa3Военачальник|r"
    wts_updates[32973] = "|cffe4cfa3Военачальник|r (|cffffffffZ|r)"
    wts_updates[32971] = "|cffe4cfa3Военачальник|r"
    wts_updates[32972] = "|cffe4cfa3Военачальник|r (|cffffffffZ|r)"
    wts_updates[32979] = "Дакаара"
    checks_def.append({"type": "unit", "id": "O059", "field": "name", "expected": wts_updates[32970]})
    checks_def.append({"type": "unit", "id": "O059", "field": "tip", "expected": wts_updates[32973]})
    checks_def.append({"type": "unit", "id": "O059", "field": "awakentip", "expected": wts_updates[32971]})
    checks_def.append({"type": "unit", "id": "O059", "field": "revivetip", "expected": wts_updates[32972]})
    checks_def.append({"type": "unit", "id": "O059", "field": "propernames", "expected": wts_updates[32979]})

    # =========================================================================
    # 5. UPGRADES (12 technologies)
    # =========================================================================
    # R01Z: Корпуса построек (3 levels, Q)
    r01z_names = [19404, 19406, 19408]
    r01z_tips = [19410, 19607, 19668]
    r01z_ubs = [32395, 32396, 32397]
    for lvl in range(1, 4):
        wts_updates[r01z_names[lvl-1]] = f"|cffe4cfa3Корпуса построек|r — уровень {lvl}"
        wts_updates[r01z_tips[lvl-1]] = f"|cffe4cfa3Корпуса построек — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r01z_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет стены и каркасы зданий лесных троллей, увеличивая их запас прочности и броню на |cffc8e087+{lvl*10}%|cffced4da.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- Всем зданиям лесных троллей.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R01Z", "field": f"name{lvl}", "expected": wts_updates[r01z_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R01Z", "field": f"tip{lvl}", "expected": wts_updates[r01z_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R01Z", "field": f"ubertip{lvl}", "expected": wts_updates[r01z_ubs[lvl-1]]})

    # R03O: Методы регенерации (6 levels, R)
    r03o_names = [29695, 31107, 31108, 19825, 22818, 24572]
    r03o_tips = [32584, 32585, 32586, 32579, 32580, 32581]
    r03o_ubs = [33460, 33461, 33462, 33463, 33464, 33465]
    for lvl in range(1, 7):
        wts_updates[r03o_names[lvl-1]] = f"|cffe4cfa3Методы регенерации|r — уровень {lvl}"
        wts_updates[r03o_tips[lvl-1]] = f"|cffe4cfa3Методы регенерации — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[r03o_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Ускоряет естественное исцеление ран, повышая восстановление здоровья органических войск на |cffc8e087+{lvl}|cffced4da ед./сек.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- Всем живым воинам лесных троллей.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R03O", "field": f"name{lvl}", "expected": wts_updates[r03o_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R03O", "field": f"tip{lvl}", "expected": wts_updates[r03o_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R03O", "field": f"ubertip{lvl}", "expected": wts_updates[r03o_ubs[lvl-1]]})

    # R03P: Снадобья силы (3 levels, Q)
    r03p_names = [32621, 32623, 32640]
    r03p_tips = [32703, 32704, 32855]
    r03p_ubs = [32596, 32597, 32598]
    r03p_bonuses = [75, 135, 195]
    for lvl in range(1, 4):
        wts_updates[r03p_names[lvl-1]] = f"|cffe4cfa3Снадобья силы|r — уровень {lvl}"
        wts_updates[r03p_tips[lvl-1]] = f"|cffe4cfa3Снадобья силы — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r03p_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Закаляет тело воинов особыми настойками трав, увеличивая максимальный запас здоровья берсерков и наездников на медведях на |cffc8e087+{r03p_bonuses[lvl-1]}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deБерсерк|cffced4da, |cffa9c7deНаездник на медведе|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R03P", "field": f"name{lvl}", "expected": wts_updates[r03p_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R03P", "field": f"tip{lvl}", "expected": wts_updates[r03p_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R03P", "field": f"ubertip{lvl}", "expected": wts_updates[r03p_ubs[lvl-1]]})

    # R0IQ: Улучшить до мастера топора (1 level, R)
    wts_updates[32937] = "|cffe4cfa3Мастер топора|r"
    wts_updates[32938] = "|cffe4cfa3Мастер топора|r (|cffffffffR|r)"
    wts_updates[33004] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Совершенствует мастерство владения метательным оружием, повышая ранг метателей топоров до |cffa9c7deМастеров топора|cffced4da и существенно увеличивая их боевые характеристики.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМетатель топоров|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0IQ", "field": "name1", "expected": wts_updates[32937]})
    checks_def.append({"type": "upgrade", "id": "R0IQ", "field": "tip1", "expected": wts_updates[32938]})
    checks_def.append({"type": "upgrade", "id": "R0IQ", "field": "ubertip1", "expected": wts_updates[33004]})

    # R0IS: Улучшенные топоры (6 levels, W)
    r0is_names = [33073, 33070, 33056, 33057, 33058, 33059]
    r0is_tips = [33074, 33071, 33060, 33061, 33062, 33063]
    r0is_ubs = {3: 33064, 4: 33065, 5: 33066, 6: 33067}
    for lvl in range(1, 7):
        wts_updates[r0is_names[lvl-1]] = f"|cffe4cfa3Улучшенные топоры|r — уровень {lvl}"
        wts_updates[r0is_tips[lvl-1]] = f"|cffe4cfa3Улучшенные топоры — уровень {lvl}|r (|cffffffffW|r)"
        checks_def.append({"type": "upgrade", "id": "R0IS", "field": f"name{lvl}", "expected": wts_updates[r0is_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IS", "field": f"tip{lvl}", "expected": wts_updates[r0is_tips[lvl-1]]})
        if lvl in r0is_ubs:
            wts_updates[r0is_ubs[lvl]] = (
                f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает лесорубные инструменты, позволяя рабочим переносить на |cffc8e087+{lvl*10}|cffced4da ед. больше древесины.|n|n"
                "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРемесленник|cffced4da, |cffa9c7deСобиратель|cffced4da.|n|n"
                f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
            )
            checks_def.append({"type": "upgrade", "id": "R0IS", "field": f"ubertip{lvl}", "expected": wts_updates[r0is_ubs[lvl]]})

    # R0IT: Стальная броня (6 levels, A)
    r0it_names = [33091, 33093, 33094, 33079, 33080, 33081]
    r0it_tips = [33098, 33099, 33100, 33082, 33083, 33084]
    r0it_ubs = [33085, 33086, 33087, 33088, 33089, 33090]
    for lvl in range(1, 7):
        wts_updates[r0it_names[lvl-1]] = f"|cffe4cfa3Стальная броня|r — уровень {lvl}"
        wts_updates[r0it_tips[lvl-1]] = f"|cffe4cfa3Стальная броня — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r0it_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет доспехи и щиты воинов, повышая броню на |cffc8e087+{lvl*2}|cffced4da.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- Всем боевым войскам лесных троллей.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0IT", "field": f"name{lvl}", "expected": wts_updates[r0it_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IT", "field": f"tip{lvl}", "expected": wts_updates[r0it_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IT", "field": f"ubertip{lvl}", "expected": wts_updates[r0it_ubs[lvl-1]]})

    # R0IU: Стальное оружие (6 levels, Q)
    r0iu_names = [33117, 33119, 33120, 33105, 33106, 33107]
    r0iu_tips = [33124, 33125, 33126, 33108, 33109, 33110]
    r0iu_ubs = [33111, 33112, 33113, 33114, 33115, 33116]
    for lvl in range(1, 7):
        wts_updates[r0iu_names[lvl-1]] = f"|cffe4cfa3Стальное оружие|r — уровень {lvl}"
        wts_updates[r0iu_tips[lvl-1]] = f"|cffe4cfa3Стальное оружие — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r0iu_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Закаляет клинки, топоры и наконечники копий, увеличивая урон немагических атак войск лесных троллей.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- Войскам ближнего и дальнего боя лесных троллей.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0IU", "field": f"name{lvl}", "expected": wts_updates[r0iu_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IU", "field": f"tip{lvl}", "expected": wts_updates[r0iu_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IU", "field": f"ubertip{lvl}", "expected": wts_updates[r0iu_ubs[lvl-1]]})

    # R0IV: Обучение заклинателей (3 levels, W)
    r0iv_names = [33138, 33127, 33130]
    r0iv_tips = [33128, 33129, 33131]
    r0iv_ubs = [33132, 33136, 33137]
    for lvl in range(1, 4):
        wts_updates[r0iv_names[lvl-1]] = f"|cffe4cfa3Обучение заклинателей|r — ступень {lvl}"
        wts_updates[r0iv_tips[lvl-1]] = f"|cffe4cfa3Обучение заклинателей — ступень {lvl}|r (|cffffffffW|r)"
        wts_updates[r0iv_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья заклинателей на |cffc8e087+{lvl*60}|cffced4da, запас маны на |cffc8e087+{lvl*150}|cffced4da, ускоряет восстановление маны и открывает доступ к новым заклинаниям вуду.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЗаклинатель|cffced4da.|n|n"
            f"Ступень обучения: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0IV", "field": f"name{lvl}", "expected": wts_updates[r0iv_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IV", "field": f"tip{lvl}", "expected": wts_updates[r0iv_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IV", "field": f"ubertip{lvl}", "expected": wts_updates[r0iv_ubs[lvl-1]]})

    # R0IW: Обучение жрецов (3 levels, Q)
    r0iw_names = [33140, 33141, 33144]
    r0iw_tips = [33142, 33143, 33145]
    r0iw_ubs = [33146, 33150, 33151]
    for lvl in range(1, 4):
        wts_updates[r0iw_names[lvl-1]] = f"|cffe4cfa3Обучение жрецов|r — ступень {lvl}"
        wts_updates[r0iw_tips[lvl-1]] = f"|cffe4cfa3Обучение жрецов — ступень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r0iw_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья жрецов на |cffc8e087+{lvl*60}|cffced4da, запас маны на |cffc8e087+{lvl*150}|cffced4da, ускоряет регенерацию маны и открывает новые целительные и очищающие ритуалы.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЖрец|cffced4da.|n|n"
            f"Ступень обучения: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0IW", "field": f"name{lvl}", "expected": wts_updates[r0iw_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IW", "field": f"tip{lvl}", "expected": wts_updates[r0iw_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0IW", "field": f"ubertip{lvl}", "expected": wts_updates[r0iw_ubs[lvl-1]]})

    # R0J0: Методы поглощения Лоа (3 levels, E)
    r0j0_names = [33491, 33493, 33494]
    r0j0_tips = [33498, 33499, 33500]
    r0j0_ubs = [33485, 33486, 33487]
    for lvl in range(1, 4):
        wts_updates[r0j0_names[lvl-1]] = f"|cffe4cfa3Методы поглощения Лоа|r — уровень {lvl}"
        wts_updates[r0j0_tips[lvl-1]] = f"|cffe4cfa3Методы поглощения Лоа — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[r0j0_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет духовную связь воинов со звериными богами, открывая новые способности и усиливая характеристики аватаров Лоа.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deТролль-медведь|cffced4da, |cffa9c7deТролль-волк|cffced4da, |cffa9c7deТролль-ястреб|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0J0", "field": f"name{lvl}", "expected": wts_updates[r0j0_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J0", "field": f"tip{lvl}", "expected": wts_updates[r0j0_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0J0", "field": f"ubertip{lvl}", "expected": wts_updates[r0j0_ubs[lvl-1]]})

    # R0KI: Шипы на медведе (1 level, W)
    wts_updates[39316] = "|cffe4cfa3Шипы на медведе|r"
    wts_updates[39317] = "|cffe4cfa3Шипы на медведе|r (|cffffffffW|r)"
    wts_updates[39320] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает сбрую боевых медведей острыми стальными шипами, повышая их броню на |cffc8e087+2|cffced4da и отражая |cffffffff7%|cffced4da урона ближнего боя обратно атакующим.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНаездник на медведе|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0KI", "field": "name1", "expected": wts_updates[39316]})
    checks_def.append({"type": "upgrade", "id": "R0KI", "field": "tip1", "expected": wts_updates[39317]})
    checks_def.append({"type": "upgrade", "id": "R0KI", "field": "ubertip1", "expected": wts_updates[39320]})

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # A0P8: Смерть врагам Амани
    wts_updates[33643] = "|cffe4cfa3Смерть врагам Амани|r"
    wts_updates[33644] = "|cffe4cfa3Смерть врагам Амани|r"
    wts_updates[33647] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атакам дальнего боя поражать сразу несколько целей одновременно.|r"
    checks_def.append({"type": "ability", "id": "A0P8", "field": "name", "expected": wts_updates[33643]})
    checks_def.append({"type": "ability", "id": "A0P8", "field": "tip1", "expected": wts_updates[33644]})
    checks_def.append({"type": "ability", "id": "A0P8", "field": "ubertip1", "expected": wts_updates[33647]})

    # A1DX: Жертва кровью (R)
    wts_updates[32011] = "|cffe4cfa3Жертва кровью|r"
    wts_updates[32012] = "|cffe4cfa3Жертва кровью|r (|cffffffffR|r)"
    wts_updates[36104] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приносит в жертву |cffe69a8d100|cffced4da ед. здоровья, мгновенно восстанавливая |cffc8e087100|cffced4da ед. маны.|r"
    checks_def.append({"type": "ability", "id": "A1DX", "field": "name", "expected": wts_updates[32011]})
    checks_def.append({"type": "ability", "id": "A1DX", "field": "tip1", "expected": wts_updates[32012]})
    checks_def.append({"type": "ability", "id": "A1DX", "field": "ubertip1", "expected": wts_updates[36104]})

    # A1E3: Хитроумный ритуал (E) - Hero O059
    wts_updates[32118] = "|cffe4cfa3Хитроумный ритуал|r"
    wts_updates[32041] = "|cffe4cfa3Хитроумный ритуал|r [|cffffffff1|r] (|cffffffffE|r)"
    wts_updates[32042] = "|cffe4cfa3Хитроумный ритуал|r [|cffffffff2|r] (|cffffffffE|r)"
    wts_updates[32043] = "|cffe4cfa3Хитроумный ритуал|r [|cffffffff3|r] (|cffffffffE|r)"
    wts_updates[32111] = "|cffe4cfa3Хитроумный ритуал|r [|cffffffff4|r] (|cffffffffE|r)"
    for sid in [32112, 32113, 32114, 32115]:
        wts_updates[sid] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой жертвует |cffe69a8d50%|cffced4da текущего здоровья, после чего в течение |cffffffff7|cffced4da сек. восстанавливает существенно больше здоровья.|r"
    checks_def.append({"type": "ability", "id": "A1E3", "field": "name", "expected": wts_updates[32118]})
    checks_def.append({"type": "ability", "id": "A1E3", "field": "tip1", "expected": wts_updates[32041]})
    checks_def.append({"type": "ability", "id": "A1E3", "field": "ubertip1", "expected": wts_updates[32112]})

    # A1F9: Свирепость лесов (D) - Innate
    wts_updates[29586] = "|cffe4cfa3Свирепость лесов|r"
    wts_updates[29588] = "|cffe4cfa3Свирепость лесов|r (|cffffffffD|r)"
    wts_updates[39303] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает скорость атаки тролля пропорционально недостающему здоровью.|n|n"
        "При активации отнимает |cffe69a8d25%|cffced4da текущего здоровья, но повышает урон от атак на |cffc8e087+25%|cffced4da на |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "ability", "id": "A1F9", "field": "name", "expected": wts_updates[29586]})
    checks_def.append({"type": "ability", "id": "A1F9", "field": "tip1", "expected": wts_updates[29588]})
    checks_def.append({"type": "ability", "id": "A1F9", "field": "ubertip1", "expected": wts_updates[39303]})

    # A1FB: Удары духов (Q) - Заклинатель o051
    wts_updates[33434] = "|cffe4cfa3Удары духов|r"
    wts_updates[33435] = "|cffe4cfa3Удары духов|r (|cffffffffQ|r)"
    wts_updates[33436] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область потоками магии духов, нанося урон вражеским войскам.|r"
    checks_def.append({"type": "ability", "id": "A1FB", "field": "name", "expected": wts_updates[33434]})
    checks_def.append({"type": "ability", "id": "A1FB", "field": "tip1", "expected": wts_updates[33435]})
    checks_def.append({"type": "ability", "id": "A1FB", "field": "ubertip1", "expected": wts_updates[33436]})

    # A1FC: Сети Амани (W) - Hero O059
    wts_updates[16197] = "|cffe4cfa3Сети Амани|r"
    wts_updates[15255] = "|cffe4cfa3Сети Амани|r [|cffffffff1|r] (|cffffffffW|r)"
    wts_updates[32990] = "|cffe4cfa3Сети Амани|r [|cffffffff2|r] (|cffffffffW|r)"
    wts_updates[32991] = "|cffe4cfa3Сети Амани|r [|cffffffff3|r] (|cffffffffW|r)"
    wts_updates[33697] = "|cffe4cfa3Сети Амани|r [|cffffffff4|r] (|cffffffffW|r)"
    for sid in [10425, 32992, 33700, 33701]:
        wts_updates[sid] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает прочные сети, опутывая всех врагов в указанной области и не позволяя им передвигаться.|n|nДлительность: |cffffffff7|cffced4da сек. (герои |cffffffff2|cffced4da сек.).|r"
    checks_def.append({"type": "ability", "id": "A1FC", "field": "name", "expected": wts_updates[16197]})
    checks_def.append({"type": "ability", "id": "A1FC", "field": "tip1", "expected": wts_updates[15255]})
    checks_def.append({"type": "ability", "id": "A1FC", "field": "ubertip1", "expected": wts_updates[10425]})

    # A1FE: Зачарованный Топор (Q) - Hero O059
    wts_updates[32998] = "|cffe4cfa3Зачарованный топор|r"
    wts_updates[33000] = "|cffe4cfa3Зачарованный топор|r [|cffffffff1|r] (|cffffffffQ|r)"
    wts_updates[33001] = "|cffe4cfa3Зачарованный топор|r [|cffffffff2|r] (|cffffffffQ|r)"
    wts_updates[33002] = "|cffe4cfa3Зачарованный топор|r [|cffffffff3|r] (|cffffffffQ|r)"
    wts_updates[32996] = "|cffe4cfa3Зачарованный топор|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[33503] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает зачарованный топор по прямой, нанося |cffffffff90|cffced4da ед. урона всем врагам на своём пути.|r"
    wts_updates[33504] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает зачарованный топор по прямой, нанося |cffffffff180|cffced4da ед. урона всем врагам на своём пути.|r"
    wts_updates[35836] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает зачарованный топор по прямой, нанося |cffffffff270|cffced4da ед. урона всем врагам на своём пути.|r"
    wts_updates[33501] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает зачарованный топор по прямой, нанося |cffffffff360|cffced4da ед. урона всем врагам на своём пути.|r"
    checks_def.append({"type": "ability", "id": "A1FE", "field": "name", "expected": wts_updates[32998]})
    checks_def.append({"type": "ability", "id": "A1FE", "field": "tip1", "expected": wts_updates[33000]})
    checks_def.append({"type": "ability", "id": "A1FE", "field": "ubertip1", "expected": wts_updates[33503]})

    # A1FG: Аура Медведя - Unit o05M
    wts_updates[31403] = "|cffe4cfa3Аура Медведя|r"
    wts_updates[31404] = "|cffe4cfa3Аура Медведя|r"
    wts_updates[13008] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает защиту окружающих союзников на |cffc8e087+4|cffced4da к броне.|r"
    checks_def.append({"type": "ability", "id": "A1FG", "field": "name", "expected": wts_updates[31403]})
    checks_def.append({"type": "ability", "id": "A1FG", "field": "tip1", "expected": wts_updates[31404]})
    checks_def.append({"type": "ability", "id": "A1FG", "field": "ubertip1", "expected": wts_updates[13008]})

    # A1FH: Аура Ястреба - Unit o05O
    wts_updates[33019] = "|cffe4cfa3Аура Ястреба|r"
    wts_updates[33020] = "|cffe4cfa3Аура Ястреба|r"
    wts_updates[33021] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию маны находящихся рядом союзников на |cffc8e087+3|cffced4da ед./сек.|r"
    checks_def.append({"type": "ability", "id": "A1FH", "field": "name", "expected": wts_updates[33019]})
    checks_def.append({"type": "ability", "id": "A1FH", "field": "tip1", "expected": wts_updates[33020]})
    checks_def.append({"type": "ability", "id": "A1FH", "field": "ubertip1", "expected": wts_updates[33021]})

    # A1FI: Аура Волка - Unit o05N
    wts_updates[33023] = "|cffe4cfa3Аура Волка|r"
    wts_updates[33024] = "|cffe4cfa3Аура Волка|r"
    wts_updates[33025] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атак находящихся рядом союзных войск на |cffc8e087+20%|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A1FI", "field": "name", "expected": wts_updates[33023]})
    checks_def.append({"type": "ability", "id": "A1FI", "field": "tip1", "expected": wts_updates[33024]})
    checks_def.append({"type": "ability", "id": "A1FI", "field": "ubertip1", "expected": wts_updates[33025]})

    # A1FJ: Прыжок медведя (Q) - Unit o05M
    wts_updates[33037] = "|cffe4cfa3Прыжок медведя|r"
    wts_updates[33027] = "|cffe4cfa3Прыжок медведя|r (|cffffffffQ|r)"
    wts_updates[33031] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Совершает мощный прыжок в указанную точку, нанося урон врагам при приземлении.|r"
    checks_def.append({"type": "ability", "id": "A1FJ", "field": "name", "expected": wts_updates[33037]})
    checks_def.append({"type": "ability", "id": "A1FJ", "field": "tip1", "expected": wts_updates[33027]})
    checks_def.append({"type": "ability", "id": "A1FJ", "field": "ubertip1", "expected": wts_updates[33031]})

    # A1FK: Целительный ритуал (Q) - Жрец o052
    wts_updates[33157] = "|cffe4cfa3Целительный ритуал|r"
    wts_updates[33158] = "|cffe4cfa3Целительный ритуал|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "A1FK", "field": "name", "expected": wts_updates[33157]})
    checks_def.append({"type": "ability", "id": "A1FK", "field": "tip1", "expected": wts_updates[33158]})

    # A1FL: Рассеивание заклинаний (W) - Жрец o052
    wts_updates[33163] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[33164] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffW|r)"
    checks_def.append({"type": "ability", "id": "A1FL", "field": "name", "expected": wts_updates[33163]})
    checks_def.append({"type": "ability", "id": "A1FL", "field": "tip1", "expected": wts_updates[33164]})

    # A1FM: Огонь Амани (E) - Жрец o052
    wts_updates[33165] = "|cffe4cfa3Огонь Амани|r"
    wts_updates[33166] = "|cffe4cfa3Огонь Амани|r (|cffffffffE|r)"
    wts_updates[36023] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Благословляет союзного воина священным пламенем, повышая его урон на |cffc8e087+15%|cffced4da и броню на |cffc8e087+3|cffced4da.|n|nВремя действия: |cffffffff60|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1FM", "field": "name", "expected": wts_updates[33165]})
    checks_def.append({"type": "ability", "id": "A1FM", "field": "tip1", "expected": wts_updates[33166]})
    checks_def.append({"type": "ability", "id": "A1FM", "field": "ubertip1", "expected": wts_updates[36023]})

    # A1FO: Буря (R) - Unit o05O
    wts_updates[33175] = "|cffe4cfa3Буря|r"
    wts_updates[33176] = "|cffe4cfa3Буря|r (|cffffffffR|r)"
    checks_def.append({"type": "ability", "id": "A1FO", "field": "name", "expected": wts_updates[33175]})
    checks_def.append({"type": "ability", "id": "A1FO", "field": "tip1", "expected": wts_updates[33176]})

    # A1G1: Змеиный идол (W) - Заклинатель o051
    wts_updates[33440] = "|cffe4cfa3Змеиный идол|r"
    wts_updates[33441] = "|cffe4cfa3Змеиный идол|r (|cffffffffW|r)"
    wts_updates[33442] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного и невосприимчивого к магии идола, наносящего пронзающий урон наземным и воздушным целям.|n|nВремя действия: |cffffffff40|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1G1", "field": "name", "expected": wts_updates[33440]})
    checks_def.append({"type": "ability", "id": "A1G1", "field": "tip1", "expected": wts_updates[33441]})
    checks_def.append({"type": "ability", "id": "A1G1", "field": "ubertip1", "expected": wts_updates[33442]})

    # A1G3: Хочешь топор?
    wts_updates[33509] = "|cffe4cfa3Хочешь топор?|r"
    wts_updates[33510] = "|cffe4cfa3Хочешь топор?|r"
    wts_updates[33511] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Любой урон, нанесённый троллем, оставляет на цели метку охотника, снижающую её броню на |cffe69a8d-4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A1G3", "field": "name", "expected": wts_updates[33509]})
    checks_def.append({"type": "ability", "id": "A1G3", "field": "tip1", "expected": wts_updates[33510]})
    checks_def.append({"type": "ability", "id": "A1G3", "field": "ubertip1", "expected": wts_updates[33511]})

    # A1G5: Заклятие жизни (R) - Hero O059 Ultimate
    wts_updates[33527] = "|cffe4cfa3Заклятие жизни|r"
    wts_updates[33528] = "|cffe4cfa3Заклятие жизни|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[33529] = "|cffe4cfa3Заклятие жизни|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[33530] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da В течение |cffffffff15|cffced4da сек. здоровье героя не может опуститься ниже смертельного порога, предотвращая гибель.|r"
    wts_updates[33531] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da В течение |cffffffff30|cffced4da сек. здоровье героя не может опуститься ниже смертельного порога, предотвращая гибель.|r"
    checks_def.append({"type": "ability", "id": "A1G5", "field": "name", "expected": wts_updates[33527]})
    checks_def.append({"type": "ability", "id": "A1G5", "field": "tip1", "expected": wts_updates[33528]})
    checks_def.append({"type": "ability", "id": "A1G5", "field": "ubertip1", "expected": wts_updates[33530]})

    # A1G7: Проклятье Слабой Руки (Q) - Hero O058
    wts_updates[33564] = "|cffe4cfa3Проклятье Слабой Руки|r"
    wts_updates[33550] = "|cffe4cfa3Проклятье Слабой Руки|r [|cffffffff1|r] (|cffffffffQ|r)"
    wts_updates[33551] = "|cffe4cfa3Проклятье Слабой Руки|r [|cffffffff2|r] (|cffffffffQ|r)"
    wts_updates[33552] = "|cffe4cfa3Проклятье Слабой Руки|r [|cffffffff3|r] (|cffffffffQ|r)"
    wts_updates[33553] = "|cffe4cfa3Проклятье Слабой Руки|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[33554] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает врага. Жертва промахивается при атаках с вероятностью |cffe69a8d33%|cffced4da.|n|nВремя действия: |cffffffff15|cffced4da сек.|r"
    wts_updates[33555] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает врага. Жертва промахивается при атаках с вероятностью |cffe69a8d43%|cffced4da.|n|nВремя действия: |cffffffff20|cffced4da сек.|r"
    wts_updates[33556] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает врага. Жертва промахивается при атаках с вероятностью |cffe69a8d53%|cffced4da.|n|nВремя действия: |cffffffff25|cffced4da сек.|r"
    wts_updates[33557] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает врага. Жертва промахивается при атаках с вероятностью |cffe69a8d63%|cffced4da.|n|nВремя действия: |cffffffff30|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1G7", "field": "name", "expected": wts_updates[33564]})
    checks_def.append({"type": "ability", "id": "A1G7", "field": "tip1", "expected": wts_updates[33550]})
    checks_def.append({"type": "ability", "id": "A1G7", "field": "ubertip1", "expected": wts_updates[33554]})

    # A1G8: Проклятие хрупких доспехов (W) - Hero O058
    wts_updates[33568] = "|cffe4cfa3Проклятие хрупких доспехов|r"
    wts_updates[33569] = "|cffe4cfa3Проклятие хрупких доспехов|r [|cffffffff1|r] (|cffffffffW|r)"
    wts_updates[33570] = "|cffe4cfa3Проклятие хрупких доспехов|r [|cffffffff2|r] (|cffffffffW|r)"
    wts_updates[33571] = "|cffe4cfa3Проклятие хрупких доспехов|r [|cffffffff3|r] (|cffffffffW|r)"
    wts_updates[33572] = "|cffe4cfa3Проклятие хрупких доспехов|r [|cffffffff4|r] (|cffffffffW|r)"
    wts_updates[30682] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ослабляет броню врага на |cffe69a8d-5|cffced4da и раскрывает его местоположение на |cffffffff45|cffced4da сек.|r"
    wts_updates[33574] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ослабляет броню врага на |cffe69a8d-6|cffced4da и раскрывает его местоположение на |cffffffff45|cffced4da сек.|r"
    wts_updates[33575] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ослабляет броню врага на |cffe69a8d-7|cffced4da и раскрывает его местоположение на |cffffffff45|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1G8", "field": "name", "expected": wts_updates[33568]})
    checks_def.append({"type": "ability", "id": "A1G8", "field": "tip1", "expected": wts_updates[33569]})
    checks_def.append({"type": "ability", "id": "A1G8", "field": "ubertip2", "expected": wts_updates[30682]})

    # A1G9: Тёмная аура - Hero O058
    wts_updates[33586] = "|cffe4cfa3Тёмная аура|r"
    wts_updates[33588] = "|cffe4cfa3Тёмная аура|r [|cffffffff1|r]"
    wts_updates[33589] = "|cffe4cfa3Тёмная аура|r [|cffffffff2|r]"
    wts_updates[33590] = "|cffe4cfa3Тёмная аура|r [|cffffffff3|r]"
    wts_updates[33584] = "|cffe4cfa3Тёмная аура|r [|cffffffff4|r]"
    wts_updates[33585] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения ближайших союзников на |cffc8e087+24%|cffced4da и повышает скорость регенерации их здоровья на |cffc8e087+4|cffced4da ед./сек.|r"
    checks_def.append({"type": "ability", "id": "A1G9", "field": "name", "expected": wts_updates[33586]})
    checks_def.append({"type": "ability", "id": "A1G9", "field": "tip1", "expected": wts_updates[33588]})
    checks_def.append({"type": "ability", "id": "A1G9", "field": "ubertip4", "expected": wts_updates[33585]})

    # A1GA: Ритуал Поглощения (R) - Hero O058 Ultimate
    wts_updates[33591] = "|cffe4cfa3Ритуал Поглощения|r"
    wts_updates[33592] = "|cffe4cfa3Ритуал Поглощения|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[33593] = "|cffe4cfa3Ритуал Поглощения|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[35232] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает выбранного союзного тролля в могучего аватара Лоа (пехота — в Тролля-медведя, стрелки — в Тролля-волка, маги — в Тролля-ястреба).|r"
    wts_updates[35233] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает выбранного союзного тролля в могучего аватара Лоа (пехота — в Тролля-медведя, стрелки — в Тролля-волка, маги — в Тролля-ястреба).|r"
    checks_def.append({"type": "ability", "id": "A1GA", "field": "name", "expected": wts_updates[33591]})
    checks_def.append({"type": "ability", "id": "A1GA", "field": "tip1", "expected": wts_updates[33592]})
    checks_def.append({"type": "ability", "id": "A1GA", "field": "ubertip1", "expected": wts_updates[35232]})

    # A1GB: Веер клинков (E) - Hero O057
    wts_updates[33598] = "|cffe4cfa3Веер клинков|r"
    wts_updates[33600] = "|cffe4cfa3Веер клинков|r [|cffffffff1|r] (|cffffffffE|r)"
    wts_updates[33601] = "|cffe4cfa3Веер клинков|r [|cffffffff2|r] (|cffffffffE|r)"
    wts_updates[33602] = "|cffe4cfa3Веер клинков|r [|cffffffff3|r] (|cffffffffE|r)"
    wts_updates[33603] = "|cffe4cfa3Веер клинков|r [|cffffffff4|r] (|cffffffffE|r)"
    wts_updates[35854] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер смертоносных кинжалов, нанося по |cffffffff85|cffced4da ед. урона окружающим врагам.|r"
    wts_updates[35855] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер смертоносных кинжалов, нанося по |cffffffff210|cffced4da ед. урона окружающим врагам.|r"
    wts_updates[35856] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер смертоносных кинжалов, нанося по |cffffffff335|cffced4da ед. урона окружающим врагам.|r"
    wts_updates[35853] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер смертоносных кинжалов, нанося по |cffffffff460|cffced4da ед. урона окружающим врагам.|r"
    checks_def.append({"type": "ability", "id": "A1GB", "field": "name", "expected": wts_updates[33598]})
    checks_def.append({"type": "ability", "id": "A1GB", "field": "tip1", "expected": wts_updates[33600]})
    checks_def.append({"type": "ability", "id": "A1GB", "field": "ubertip1", "expected": wts_updates[35854]})

    # A1GC: Танец ветра (Q) - Hero O057
    wts_updates[33607] = "|cffe4cfa3Танец ветра|r"
    wts_updates[33608] = "|cffe4cfa3Танец ветра|r [|cffffffff1|r] (|cffffffffQ|r)"
    wts_updates[33609] = "|cffe4cfa3Танец ветра|r [|cffffffff2|r] (|cffffffffQ|r)"
    wts_updates[33610] = "|cffe4cfa3Танец ветра|r [|cffffffff3|r] (|cffffffffQ|r)"
    wts_updates[33605] = "|cffe4cfa3Танец ветра|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[25065] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует невидимость и |cffc8e087+100%|cffced4da к скорости передвижения на |cffffffff65|cffced4da сек. Атака из невидимости наносит |cffffffff+150|cffced4da ед. дополнительного урона.|r"
    checks_def.append({"type": "ability", "id": "A1GC", "field": "name", "expected": wts_updates[33607]})
    checks_def.append({"type": "ability", "id": "A1GC", "field": "tip1", "expected": wts_updates[33608]})
    checks_def.append({"type": "ability", "id": "A1GC", "field": "ubertip4", "expected": wts_updates[25065]})

    # A1GD: Критический удар - Hero O057
    wts_updates[33616] = "|cffe4cfa3Критический удар|r"
    wts_updates[33614] = "|cffe4cfa3Критический удар|r [|cffffffff1|r]"
    wts_updates[33613] = "|cffe4cfa3Критический удар|r [|cffffffff2|r]"
    wts_updates[33615] = "|cffe4cfa3Критический удар|r [|cffffffff3|r]"
    wts_updates[33611] = "|cffe4cfa3Критический удар|r [|cffffffff4|r]"
    wts_updates[28789] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff15%|cffced4da шанс нанести |cffffffff5-кратный|cffced4da урон при атаке.|r"
    checks_def.append({"type": "ability", "id": "A1GD", "field": "name", "expected": wts_updates[33616]})
    checks_def.append({"type": "ability", "id": "A1GD", "field": "tip1", "expected": wts_updates[33614]})
    checks_def.append({"type": "ability", "id": "A1GD", "field": "ubertip4", "expected": wts_updates[28789]})

    # A1GF: Берсерк (Q)
    wts_updates[33421] = "|cffe4cfa3Берсерк|r"
    wts_updates[33424] = "|cffe4cfa3Берсерк|r (|cffffffffQ|r)"
    wts_updates[33425] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+35%|cffced4da, но повышает получаемый урон на |cffe69a8d+30%|cffced4da.|n|nВремя действия: |cffffffff12|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1GF", "field": "name", "expected": wts_updates[33421]})
    checks_def.append({"type": "ability", "id": "A1GF", "field": "tip1", "expected": wts_updates[33424]})
    checks_def.append({"type": "ability", "id": "A1GF", "field": "ubertip1", "expected": wts_updates[33425]})

    # A1GG: Чудодейственный рёв (E) - Unit o05M
    wts_updates[33649] = "|cffe4cfa3Чудодейственный рёв|r"
    wts_updates[33650] = "|cffe4cfa3Чудодейственный рёв|r (|cffffffffE|r)"
    wts_updates[33651] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню окружающих союзников на |cffc8e087+2|cffced4da и значительно ускоряет их регенерацию здоровья на |cffffffff20|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1GG", "field": "name", "expected": wts_updates[33649]})
    checks_def.append({"type": "ability", "id": "A1GG", "field": "tip1", "expected": wts_updates[33650]})
    checks_def.append({"type": "ability", "id": "A1GG", "field": "ubertip1", "expected": wts_updates[33651]})

    # A1GH: Огромная сила - Unit o05M
    wts_updates[33654] = "|cffe4cfa3Огромная сила|r"
    wts_updates[33652] = "|cffe4cfa3Огромная сила|r"
    wts_updates[33653] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Удары тролля-медведя наносят |cffffffff15%|cffced4da рассекающего урона окружающим врагам в радиусе |cffffffff200|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A1GH", "field": "name", "expected": wts_updates[33654]})
    checks_def.append({"type": "ability", "id": "A1GH", "field": "tip1", "expected": wts_updates[33652]})
    checks_def.append({"type": "ability", "id": "A1GH", "field": "ubertip1", "expected": wts_updates[33653]})

    # A1GI: Цепная молния (Q) - Unit o05O
    wts_updates[33655] = "|cffe4cfa3Цепная молния|r"
    wts_updates[33657] = "|cffe4cfa3Цепная молния|r (|cffffffffQ|r)"
    wts_updates[33658] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель электрическим разрядом, наносящим |cffffffff70|cffced4da ед. урона и перескакивающим до |cffffffff10|cffced4da раз по соседним врагам.|r"
    checks_def.append({"type": "ability", "id": "A1GI", "field": "name", "expected": wts_updates[33655]})
    checks_def.append({"type": "ability", "id": "A1GI", "field": "tip1", "expected": wts_updates[33657]})
    checks_def.append({"type": "ability", "id": "A1GI", "field": "ubertip1", "expected": wts_updates[33658]})

    # A1GJ: Ужасающий вой (E) - Unit o05N
    wts_updates[33659] = "|cffe4cfa3Ужасающий вой|r"
    wts_updates[33661] = "|cffe4cfa3Ужасающий вой|r (|cffffffffE|r)"
    wts_updates[33662] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оглушительный вой снижает броню вражеских войск поблизости на |cffe69a8d-3|cffced4da.|n|nВремя действия: |cffffffff15|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1GJ", "field": "name", "expected": wts_updates[33659]})
    checks_def.append({"type": "ability", "id": "A1GJ", "field": "tip1", "expected": wts_updates[33661]})
    checks_def.append({"type": "ability", "id": "A1GJ", "field": "ubertip1", "expected": wts_updates[33662]})

    # A1GL: Вкус битвы (R) - Unit o05N
    wts_updates[33705] = "|cffe4cfa3Вкус битвы|r"
    wts_updates[33706] = "|cffe4cfa3Вкус битвы|r (|cffffffffR|r)"
    wts_updates[33669] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пробуждает жажду крови, наделяя всех ближайших союзников |cffc8e08725%|cffced4da вампиризмом на |cffffffff20|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1GL", "field": "name", "expected": wts_updates[33705]})
    checks_def.append({"type": "ability", "id": "A1GL", "field": "tip1", "expected": wts_updates[33706]})
    checks_def.append({"type": "ability", "id": "A1GL", "field": "ubertip1", "expected": wts_updates[33669]})

    # A1GM: Безрассудный берсерк (Q) - Unit o05N
    wts_updates[33670] = "|cffe4cfa3Безрассудный берсерк|r"
    wts_updates[33671] = "|cffe4cfa3Безрассудный берсерк|r (|cffffffffQ|r)"
    wts_updates[33672] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffc8e087+100%|cffced4da к скорости атаки и |cffc8e087+25%|cffced4da к скорости бега, но повышает получаемый урон на |cffe69a8d+70%|cffced4da.|n|nВремя действия: |cffffffff12|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A1GM", "field": "name", "expected": wts_updates[33670]})
    checks_def.append({"type": "ability", "id": "A1GM", "field": "tip1", "expected": wts_updates[33671]})
    checks_def.append({"type": "ability", "id": "A1GM", "field": "ubertip1", "expected": wts_updates[33672]})

    # A1GN: Сильный удар - Unit o050
    wts_updates[33674] = "|cffe4cfa3Сильный удар|r"
    wts_updates[30955] = "|cffe4cfa3Сильный удар|r"
    wts_updates[15254] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff15%|cffced4da шанс нанести |cffffffff+15|cffced4da ед. урона и оглушить цель на |cffffffff1|cffced4da сек. (героев на |cffffffff0,1|cffced4da сек.).|r"
    checks_def.append({"type": "ability", "id": "A1GN", "field": "name", "expected": wts_updates[33674]})
    checks_def.append({"type": "ability", "id": "A1GN", "field": "tip1", "expected": wts_updates[30955]})
    checks_def.append({"type": "ability", "id": "A1GN", "field": "ubertip1", "expected": wts_updates[15254]})

    # A1GP: Заклятие силы (R) - Hero O057 Ultimate
    wts_updates[33250] = "|cffe4cfa3Заклятие силы|r"
    wts_updates[33272] = "|cffe4cfa3Заклятие силы|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[33273] = "|cffe4cfa3Заклятие силы|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[10096] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da В течение |cffffffff20|cffced4da сек. возвращает |cffffffff100%|cffced4da всего полученного героем урона обратно врагам поблизости.|r"
    wts_updates[10101] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da В течение |cffffffff40|cffced4da сек. возвращает |cffffffff100%|cffced4da всего полученного героем урона обратно врагам поблизости.|r"
    checks_def.append({"type": "ability", "id": "A1GP", "field": "name", "expected": wts_updates[33250]})
    checks_def.append({"type": "ability", "id": "A1GP", "field": "tip1", "expected": wts_updates[33272]})
    checks_def.append({"type": "ability", "id": "A1GP", "field": "ubertip1", "expected": wts_updates[10096]})

    # A1GX: Регенерация троллей скрыто (служебная)
    wts_updates[35857] = "|cffa6afb8Регенерация троллей (служебное)|r"
    checks_def.append({"type": "ability", "id": "A1GX", "field": "name", "expected": wts_updates[35857]})

    # A1ID: Бешенство (E) - Заклинатель o051
    wts_updates[31333] = "|cffe4cfa3Бешенство|r"
    wts_updates[31460] = "|cffe4cfa3Бешенство|r (|cffffffffE|r)"
    wts_updates[5422] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вводит до |cffffffff4|cffced4da воинов в радиусе в состояние бешенства: увеличивает скорость атаки на |cffc8e087+30%|cffced4da ценой потери |cffe69a8d3|cffced4da ед. здоровья/сек.|r"
    checks_def.append({"type": "ability", "id": "A1ID", "field": "name", "expected": wts_updates[31333]})
    checks_def.append({"type": "ability", "id": "A1ID", "field": "tip1", "expected": wts_updates[31460]})
    checks_def.append({"type": "ability", "id": "A1ID", "field": "ubertip1", "expected": wts_updates[5422]})

    # A1MI: Аманийское копьё (X) - Unit o053
    wts_updates[39307] = "|cffe4cfa3Аманийское копьё|r"
    wts_updates[39308] = "|cffe4cfa3Аманийское копьё|r (|cffffffffX|r)"
    wts_updates[39309] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает тяжёлое копьё во врага, нанося |cffffffff65|cffced4da ед. урона и оглушая цель на |cffffffff2|cffced4da сек. (героев на |cffffffff0,1|cffced4da сек.).|r"
    checks_def.append({"type": "ability", "id": "A1MI", "field": "name", "expected": wts_updates[39307]})
    checks_def.append({"type": "ability", "id": "A1MI", "field": "tip1", "expected": wts_updates[39308]})
    checks_def.append({"type": "ability", "id": "A1MI", "field": "ubertip1", "expected": wts_updates[39309]})

    # A1MJ: Аманийские шипы - Unit o050
    wts_updates[39310] = "|cffe4cfa3Аманийские шипы|r"
    wts_updates[39311] = "|cffe4cfa3Аманийские шипы|r"
    wts_updates[39312] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Острые шипы на броне медведя повышают защиту на |cffc8e087+2|cffced4da к броне и возвращают атакующим |cffffffff7%|cffced4da урона ближнего боя.|r"
    checks_def.append({"type": "ability", "id": "A1MJ", "field": "name", "expected": wts_updates[39310]})
    checks_def.append({"type": "ability", "id": "A1MJ", "field": "tip1", "expected": wts_updates[39311]})
    checks_def.append({"type": "ability", "id": "A1MJ", "field": "ubertip1", "expected": wts_updates[39312]})

    # =========================================================================
    # BUILD PLAN PAYLOAD & CATEGORIES
    # =========================================================================
    plan_payload = {
        "race": "ForestTrolls",
        "race_name_ru": "Лесные тролли",
        "race_id": 32,
        "total_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "categories": {
            "selection": ["A1FN", "R0J1"],
            "buildings": [
                "h0MT", "h0N8", "h0N9", "h0MV", "h0MS",
                "h0MR", "h0MZ", "h0MU", "h0N4", "h0N7", "h0D3"
            ],
            "units": [
                "o04V", "o04X", "o04W", "o04Y", "o05F",
                "o04Z", "o053", "o050", "o052", "o051",
                "o05O", "o05M", "o05N", "h0D4", "h0D6", "h0D5"
            ],
            "heroes": [
                "O057", "O058", "O059"
            ],
            "upgrades": [
                "R01Z", "R03O", "R03P", "R0IQ", "R0IS",
                "R0IT", "R0IU", "R0IV", "R0IW", "R0J0", "R0J1", "R0KI"
            ],
            "abilities": [
                "A1FN", "A0P8", "A1DU", "A1DX", "A1E3", "A1F9",
                "A1FB", "A1FC", "A1FE", "A1FG", "A1FH", "A1FI",
                "A1FJ", "A1FK", "A1FL", "A1FM", "A1FO", "A1G1",
                "A1G3", "A1G5", "A1G7", "A1G8", "A1G9", "A1GA",
                "A1GB", "A1GC", "A1GD", "A1GF", "A1GG", "A1GH",
                "A1GI", "A1GJ", "A1GL", "A1GM", "A1GN", "A1GP",
                "A1GX", "A1ID", "A1MI", "A1MJ"
            ],
            "buffs": []
        },
        "checks_def": checks_def
    }

    plan_file = folder / "foresttrolls_plan.json"
    plan_file.write_text(json.dumps(plan_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved foresttrolls_plan.json ({len(wts_updates)} strings, {len(checks_def)} checks)")

    # =========================================================================
    # GENERATE 7 CATEGORY JSON FILES
    # =========================================================================
    dump_path = ROOT / "scripts/foresttrolls_raw_dump.json"
    dump = json.loads(dump_path.read_text(encoding="utf-8")) if dump_path.exists() else {}

    # 1. foresttrolls_selection.json
    sel_data = {
        "scope": "Лесные тролли (ForestTrolls): подсказка выбора расы A1FN и маркер R0J1",
        "object": "A1FN",
        "variants": ["SD"],
        "hotkey": {"value": "D"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: регистрирует способность A1FN.",
            "При выборе создаются базовые рабочие, исследуется маркер R0J1, запускается StartForestTrolls.",
            "Горячая клавиша D, создатель и куратор VinerX, сложность 3/5 (●●●○○), период «The Burning Crusade» — «Cataclysm»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38909, "after": wts_updates[38909]},
            {"field": "tip1", "wts_id": 38910, "after": wts_updates[38910]},
            {"field": "ubertip1", "wts_id": 32514, "after": wts_updates[32514]}
        ],
        "markers": [
            {
                "id": "R0J1",
                "name": "Лесные тролли (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 34173, "after": wts_updates[34173]},
                    {"field": "tip1", "wts_id": 34174, "after": wts_updates[34174]}
                ]
            }
        ]
    }
    (folder / "foresttrolls_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote foresttrolls_selection.json")

    # 2. foresttrolls_buildings.json
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
        "scope": "Лесные тролли (ForestTrolls): категория 1 — Здания",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "foresttrolls_buildings.json").write_text(json.dumps(bld_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote foresttrolls_buildings.json")

    # 3. foresttrolls_units.json
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
        "scope": "Лесные тролли (ForestTrolls): категория 2 — Юниты",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "foresttrolls_units.json").write_text(json.dumps(unit_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote foresttrolls_units.json")

    # 4. foresttrolls_heroes.json
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
            # If awakentip or revivetip sid not in dump, check manual mapping
            if not sid:
                manual_sids = {
                    ("O057", "awakentip"): 32963,
                    ("O057", "revivetip"): 32964,
                    ("O058", "awakentip"): 32967,
                    ("O058", "revivetip"): 32968,
                    ("O059", "awakentip"): 32971,
                    ("O059", "revivetip"): 32972,
                }
                sid = manual_sids.get((h_id, fld))
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": fld,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        hero_entries.append(entry)

    hero_payload = {
        "scope": "Лесные тролли (ForestTrolls): категория 3 — Герои",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "foresttrolls_heroes.json").write_text(json.dumps(hero_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote foresttrolls_heroes.json")

    # 5. foresttrolls_abilities.json
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
        if entry["strings"]:
            abil_entries.append(entry)

    abil_payload = {
        "scope": "Лесные тролли (ForestTrolls): категория 4 — Способности",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "foresttrolls_abilities.json").write_text(json.dumps(abil_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote foresttrolls_abilities.json")

    # 6. foresttrolls_research.json
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
        "scope": "Лесные тролли (ForestTrolls): категория 5 — Исследования",
        "upgrades_count": len(res_entries),
        "variants": ["SD"],
        "upgrades": res_entries
    }
    (folder / "foresttrolls_research.json").write_text(json.dumps(res_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote foresttrolls_research.json")

    # 7. foresttrolls_audit.json
    audit_payload = {
        "race": "Лесные тролли (ForestTrolls)",
        "race_id": 32,
        "selection_ability": "A1FN",
        "selection_markers": ["R0J1"],
        "objects_audit": {
            "buildings": {
                "count": len(plan_payload["categories"]["buildings"]),
                "ids": plan_payload["categories"]["buildings"],
                "economy_building": {
                    "id": "h0MV",
                    "name": "Лачуга",
                    "food_provided": 40,
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
                    "O057": "Мастер клинка (Ловкость, ближний бой)",
                    "O058": "Повелитель проклятий (Интеллект, дальний бой)",
                    "O059": "Военачальник (Сила, ближний бой)"
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
                "count": 0,
                "ids": []
            }
        },
        "wts_summary": {
            "total_updates": len(wts_updates),
            "string_ids": sorted(list(wts_updates.keys()))
        }
    }
    (folder / "foresttrolls_audit.json").write_text(json.dumps(audit_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote foresttrolls_audit.json")
    print("All preparation and registries completed successfully!")

if __name__ == "__main__":
    main()
