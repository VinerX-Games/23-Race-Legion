# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Ogres race (Race 28)."""
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
    # 1. RACE SELECTION & MARKER: A17N, R0HT
    # =========================================================================
    # A17N
    wts_updates[38905] = "|cffe4cfa3Огры|r"
    wts_updates[38906] = "|cffe4cfa3Огры|r (|cffffffffS|r)"
    wts_updates[25688] = (
        "|cffa6afb8РАСА:|cffced4da Могучие и свирепые великаны Дренора, полагающиеся на сокрушительную физическую мощь, древних исполинов и разрушительную магию.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deNiCAmCHiK|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deNiCAmCHiK|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●|cffa6afb8○○○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Burning Crusade — Legion»|r|n|n"
        "|cffced4daОгры — древняя раса великанов, уроженцев Дренора, ведущих свой род от колоссальных гроннов. "
        "Обладая огромной силой и выносливостью, огры покоряют диких зверей, возводят цитадели и призывают свирепых великанов. "
        "Их двухголовые маги и шаманы черпают силу из крови и стихий, обращая врагов в бегство несокрушимым натиском.|r"
    )
    checks_def.append({"type": "ability", "id": "A17N", "field": "name", "expected": wts_updates[38905]})
    checks_def.append({"type": "ability", "id": "A17N", "field": "tip1", "expected": wts_updates[38906]})
    checks_def.append({"type": "ability", "id": "A17N", "field": "ubertip1", "expected": wts_updates[25688]})

    # Marker: R0HT
    wts_updates[29642] = "|cffe4cfa3Огры|r"
    wts_updates[29643] = "|cffe4cfa3Огры|r"
    wts_updates[38930] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к расе Огров.|r"
    checks_def.append({"type": "upgrade", "id": "R0HT", "field": "name1", "expected": wts_updates[29642]})
    checks_def.append({"type": "upgrade", "id": "R0HT", "field": "tip1", "expected": wts_updates[29643]})

    # =========================================================================
    # 2. BUILDINGS (11 buildings)
    # =========================================================================
    # o035: Дом огров (Q)
    wts_updates[13118] = "|cffe4cfa3Дом огров|r"
    wts_updates[28368] = "|cffe4cfa3Дом огров|r (|cffffffffQ|r)"
    wts_updates[3536] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание первой ступени. Обеспечивает добычу ресурсов и начальный лимит пищи.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгр-Строитель|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКрепость огров|cffced4da: открывает доступ к передовым сооружениям и войскам.|r"
    )
    checks_def.append({"type": "unit", "id": "o035", "field": "name", "expected": wts_updates[13118]})
    checks_def.append({"type": "unit", "id": "o035", "field": "tip", "expected": wts_updates[28368]})
    checks_def.append({"type": "unit", "id": "o035", "field": "ubertip", "expected": wts_updates[3536]})

    # o03D: Крепость огров (Z)
    wts_updates[27835] = "|cffe4cfa3Крепость огров|r"
    wts_updates[28433] = "|cffe4cfa3Крепость огров|r (|cffffffffZ|r)"
    wts_updates[35441] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание второй ступени. Существенно увеличивает запас пищи и открывает доступ к новым постройкам.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгр-Строитель|cffced4da: базовый рабочий.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЦитадель огров|cffced4da: открывает доступ к высшим технологиям и древним исполинам.|r"
    )
    checks_def.append({"type": "unit", "id": "o03D", "field": "name", "expected": wts_updates[27835]})
    checks_def.append({"type": "unit", "id": "o03D", "field": "tip", "expected": wts_updates[28433]})
    checks_def.append({"type": "unit", "id": "o03D", "field": "ubertip", "expected": wts_updates[35441]})

    # o03E: Цитадель огров (Z)
    wts_updates[27839] = "|cffe4cfa3Цитадель огров|r"
    wts_updates[28434] = "|cffe4cfa3Цитадель огров|r (|cffffffffZ|r)"
    wts_updates[35442] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание третьей ступени. Обеспечивает максимальный запас пищи и открывает все технологии расы.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгр-Строитель|cffced4da: базовый рабочий.|r"
    )
    checks_def.append({"type": "unit", "id": "o03E", "field": "name", "expected": wts_updates[27839]})
    checks_def.append({"type": "unit", "id": "o03E", "field": "tip", "expected": wts_updates[28434]})
    checks_def.append({"type": "unit", "id": "o03E", "field": "ubertip", "expected": wts_updates[35442]})

    # o036: Свиноферма (A)
    wts_updates[19649] = "|cffe4cfa3Свиноферма|r"
    wts_updates[28420] = "|cffe4cfa3Свиноферма|r (|cffffffffA|r)"
    wts_updates[11344] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию огров провизией. Позволяет укрывать рабочих для защиты от врагов.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "o036", "field": "name", "expected": wts_updates[19649]})
    checks_def.append({"type": "unit", "id": "o036", "field": "tip", "expected": wts_updates[28420]})
    checks_def.append({"type": "unit", "id": "o036", "field": "ubertip", "expected": wts_updates[11344]})

    # o037: Алтарь крови (S)
    wts_updates[19663] = "|cffe4cfa3Алтарь крови|r"
    wts_updates[22728] = "|cffe4cfa3Алтарь крови|r (|cffffffffS|r)"
    wts_updates[23546] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит для призыва и воскрешения павших героев расы Огров.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deВоеначальник Огров|cffced4da: герой ближнего боя, повелитель натиска.|n"
        "- |cffa9c7deВождь Огров|cffced4da: стойкий герой ближнего боя с сокрушительными ударами.|n"
        "- |cffa9c7deЗнахарь Огров|cffced4da: герой-заклинатель поддержки и исцеления.|r"
    )
    checks_def.append({"type": "unit", "id": "o037", "field": "name", "expected": wts_updates[19663]})
    checks_def.append({"type": "unit", "id": "o037", "field": "tip", "expected": wts_updates[22728]})
    checks_def.append({"type": "unit", "id": "o037", "field": "ubertip", "expected": wts_updates[23546]})

    # o038: Сторожевая башня (Z)
    wts_updates[19704] = "|cffe4cfa3Сторожевая башня|r"
    wts_updates[28424] = "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)"
    wts_updates[19750] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение, атакующее врагов острыми кольями.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o038", "field": "name", "expected": wts_updates[19704]})
    checks_def.append({"type": "unit", "id": "o038", "field": "tip", "expected": wts_updates[28424]})
    checks_def.append({"type": "unit", "id": "o038", "field": "ubertip", "expected": wts_updates[19750]})

    # o03A: Арена (W)
    wts_updates[25549] = "|cffe4cfa3Арена|r"
    wts_updates[28431] = "|cffe4cfa3Арена|r (|cffffffffW|r)"
    wts_updates[35432] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает базовых воинов и стрелков армии Огров.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгр-воин|cffced4da: базовый боец ближнего боя.|n"
        "- |cffa9c7deОгр-Копьеметатель|cffced4da: стрелок дальнего боя с пробивающими копьями.|n"
        "- |cffa9c7deОгр-Камнеметатель|cffced4da: осадный стрелок, наносящий урон по площади.|n"
        "- |cffa9c7deОгр-Командир|cffced4da: тяжелый воин с защитной аурой.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУсиленное копьё|cffced4da|n"
        "- |cffa9c7deКрепость плоти|cffced4da|n"
        "- |cffa9c7deСила предков|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o03A", "field": "name", "expected": wts_updates[25549]})
    checks_def.append({"type": "unit", "id": "o03A", "field": "tip", "expected": wts_updates[28431]})
    checks_def.append({"type": "unit", "id": "o03A", "field": "ubertip", "expected": wts_updates[35432]})

    # o039: Пристанище (D)
    wts_updates[19751] = "|cffe4cfa3Пристанище|r"
    wts_updates[28418] = "|cffe4cfa3Пристанище|r (|cffffffffD|r)"
    wts_updates[35424] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает мобильных всадников, берсерков и барабанщиков поддержки.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгр-Наездник|cffced4da: быстрый всадник, способный опутывать врагов.|n"
        "- |cffa9c7deОгр-Барабанщик|cffced4da: боец поддержки с боевыми аурами.|n"
        "- |cffa9c7deОгр-Берсерк|cffced4da: свирепый воин с рассекающими ударами.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОпутывание|cffced4da|n"
        "- |cffa9c7deКожаная мембрана|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o039", "field": "name", "expected": wts_updates[19751]})
    checks_def.append({"type": "unit", "id": "o039", "field": "tip", "expected": wts_updates[28418]})
    checks_def.append({"type": "unit", "id": "o039", "field": "ubertip", "expected": wts_updates[35424]})

    # o03J: Пристанище магов (R)
    wts_updates[27851] = "|cffe4cfa3Пристанище магов|r"
    wts_updates[28421] = "|cffe4cfa3Пристанище магов|r (|cffffffffR|r)"
    wts_updates[41949] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает заклинателей и магов армии Огров.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгр-Маг|cffced4da: двухголовый колдун с жаждой крови и рассеиванием.|n"
        "- |cffa9c7deОгр-Боевой Маг|cffced4da: маг с духовной связью и огненным лассо.|n"
        "- |cffa9c7deШаман Мок'Натал|cffced4da: шаман со щитом молний, призывом вепря и цепной молнией.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбучение магов поддержки|cffced4da|n"
        "- |cffa9c7deОбучение боевых магов|cffced4da|n"
        "- |cffa9c7deОбучение Шаманов Мок'Натала|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o03J", "field": "name", "expected": wts_updates[27851]})
    checks_def.append({"type": "unit", "id": "o03J", "field": "tip", "expected": wts_updates[28421]})
    checks_def.append({"type": "unit", "id": "o03J", "field": "ubertip", "expected": wts_updates[41949]})

    # o03C: Пещера Древних (F)
    wts_updates[35433] = "|cffe4cfa3Пещера Древних|r"
    wts_updates[35434] = "|cffe4cfa3Пещера Древних|r (|cffffffffF|r)"
    wts_updates[35440] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель гигантских существ: свирепых огронов и колоссальных гроннов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОгрон|cffced4da: массивный боец ближнего боя.|n"
        "- |cffa9c7deОгрон-синий|cffced4da: морозный огрон с ледяным доспехом.|n"
        "- |cffa9c7deОгрон Красный|cffced4da: яростный огрон с повышенной скоростью атаки.|n"
        "- |cffa9c7deГронн Черный|cffced4da: исполин с шипастым панцирем, отражающим урон.|n"
        "- |cffa9c7deГронн Белый|cffced4da: северный гронн с сокрушительными ударами по площади.|n"
        "- |cffa9c7deГронн Красный|cffced4da: свирепый гронн с боевым бешенством.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКаменная плоть|cffced4da|n"
        "- |cffa9c7deЖажда Крови|cffced4da|n"
        "- |cffa9c7deМорозный Доспех|cffced4da|n"
        "- |cffa9c7deШипастый Панцирь|cffced4da|n"
        "- |cffa9c7deСокрушение|cffced4da|n"
        "- |cffa9c7deНеистовство|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o03C", "field": "name", "expected": wts_updates[35433]})
    checks_def.append({"type": "unit", "id": "o03C", "field": "tip", "expected": wts_updates[35434]})
    checks_def.append({"type": "unit", "id": "o03C", "field": "ubertip", "expected": wts_updates[35440]})

    # o03B: Лесопилка (E)
    wts_updates[27745] = "|cffe4cfa3Лесопилка|r"
    wts_updates[28432] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[21090] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит пунктом сдачи древесины и центром базовых улучшений армии Огров.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗаостренные дубины|cffced4da: повышает урон ближнего боя.|n"
        "- |cffa9c7deШкуры зверей|cffced4da: повышает броню воинов.|n"
        "- |cffa9c7deКрупные камни|cffced4da: повышает урон дальнего боя.|n"
        "- |cffa9c7deСбор древесины|cffced4da: увеличивает вместимость переносимой древесины.|r"
    )
    checks_def.append({"type": "unit", "id": "o03B", "field": "name", "expected": wts_updates[27745]})
    checks_def.append({"type": "unit", "id": "o03B", "field": "tip", "expected": wts_updates[28432]})
    checks_def.append({"type": "unit", "id": "o03B", "field": "ubertip", "expected": wts_updates[21090]})

    # =========================================================================
    # 3. HEROES (4 heroes)
    # =========================================================================
    # N05J: Военачальник Огров (X)
    wts_updates[27894] = "|cffe4cfa3Военачальник Огров|r"
    wts_updates[28438] = "|cffe4cfa3Военачальник Огров|r (|cffffffffX|r)"
    wts_updates[31835] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могучий военачальник ближнего боя. Подавляет противников сокрушительными ударами и неудержимым гневом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУдар по земле|cffced4da: наносит урон и оглушает окружающих врагов.|n"
        "- |cffa9c7deРывок|cffced4da: стремительный выпад к цели с уроном и оглушением.|n"
        "- |cffa9c7deСтойкость великана|cffced4da: пассивно увеличивает силу и запас здоровья.|n"
        "- |cffa9c7deГнев Гориана|cffced4da: значительно увеличивает урон, скорость атаки и дарует неуязвимость к магии.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    wts_updates[28437] = "|cffe4cfa3Военачальник Огров|r"
    wts_updates[28439] = "|cffe4cfa3Военачальник Огров|r (|cffffffffX|r)"
    checks_def.append({"type": "unit", "id": "N05J", "field": "name", "expected": wts_updates[27894]})
    checks_def.append({"type": "unit", "id": "N05J", "field": "tip", "expected": wts_updates[28438]})
    checks_def.append({"type": "unit", "id": "N05J", "field": "ubertip", "expected": wts_updates[31835]})
    checks_def.append({"type": "unit", "id": "N05J", "field": "awakentip", "expected": wts_updates[28437]})
    checks_def.append({"type": "unit", "id": "N05J", "field": "revivetip", "expected": wts_updates[28439]})

    # N05K: Вождь Огров (Z)
    wts_updates[27901] = "|cffe4cfa3Вождь Огров|r"
    wts_updates[28443] = "|cffe4cfa3Вождь Огров|r (|cffffffffZ|r)"
    wts_updates[31839] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Свирепый вождь племени. Черпает силу в бою, сотрясая врагов мощными ударами и разрушительными волнами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСтойкость огра|cffced4da: пассивно ускоряет регенерацию и атаку при низком здоровье.|n"
        "- |cffa9c7deСотрясение|cffced4da: шанс оглушить цель и нанести дополнительный урон при атаке.|n"
        "- |cffa9c7deСтойкость великана|cffced4da: пассивно увеличивает силу и максимальное здоровье.|n"
        "- |cffa9c7deУдарная волна|cffced4da: выпускает сокрушительную волну энергии по прямой.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    wts_updates[17191] = "|cffe4cfa3Вождь Огров|r"
    wts_updates[28442] = "|cffe4cfa3Вождь Огров|r (|cffffffffZ|r)"
    checks_def.append({"type": "unit", "id": "N05K", "field": "name", "expected": wts_updates[27901]})
    checks_def.append({"type": "unit", "id": "N05K", "field": "tip", "expected": wts_updates[28443]})
    checks_def.append({"type": "unit", "id": "N05K", "field": "ubertip", "expected": wts_updates[31839]})
    checks_def.append({"type": "unit", "id": "N05K", "field": "awakentip", "expected": wts_updates[17191]})
    checks_def.append({"type": "unit", "id": "N05K", "field": "revivetip", "expected": wts_updates[28442]})

    # N05L: Знахарь Огров (C)
    wts_updates[27908] = "|cffe4cfa3Знахарь Огров|r"
    wts_updates[28447] = "|cffe4cfa3Знахарь Огров|r (|cffffffffC|r)"
    wts_updates[31846] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Мудрый заклинатель и целитель. Поддерживает армию волнами исцеления, разведкой и вытягиванием жизненных сил.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолна исцеления|cffced4da: восстанавливает здоровье нескольким раненым союзникам.|n"
        "- |cffa9c7deРазведка|cffced4da: призывает зорких ястребов-разведчиков с аурами.|n"
        "- |cffa9c7deКислотная бомба|cffced4da: разъедает броню врагов и наносит периодический урон.|n"
        "- |cffa9c7deПохищение жизни|cffced4da: вытягивает здоровье у врага, восполняя собственное.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    wts_updates[28446] = "|cffe4cfa3Знахарь Огров|r"
    wts_updates[28448] = "|cffe4cfa3Знахарь Огров|r (|cffffffffC|r)"
    checks_def.append({"type": "unit", "id": "N05L", "field": "name", "expected": wts_updates[27908]})
    checks_def.append({"type": "unit", "id": "N05L", "field": "tip", "expected": wts_updates[28447]})
    checks_def.append({"type": "unit", "id": "N05L", "field": "ubertip", "expected": wts_updates[31846]})
    checks_def.append({"type": "unit", "id": "N05L", "field": "awakentip", "expected": wts_updates[28446]})
    checks_def.append({"type": "unit", "id": "N05L", "field": "revivetip", "expected": wts_updates[28448]})

    # N05O: Последний Гронн (X)
    wts_updates[29128] = "|cffe4cfa3Последний Гронн|r"
    wts_updates[29129] = "Груул"
    wts_updates[29682] = "|cffe4cfa3Последний Гронн|r (|cffffffffX|r)"
    wts_updates[42389] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный первобытный исполин Дренора. Обладает сокрушительной физической силой и каменной стойкостью.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБроски камней|cffced4da: обстреливает область валунами с уроном и оглушением.|n"
        "- |cffa9c7deПровокация|cffced4da: заставляет ближайших врагов атаковать исполина.|n"
        "- |cffa9c7deУдар по земле|cffced4da: сотрясает землю, замедляя врагов и нанося урон.|n"
        "- |cffa9c7deКаменная кожа|cffced4da: снижает получаемый урон от атак.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    wts_updates[29681] = "|cffe4cfa3Последний Гронн|r"
    wts_updates[29683] = "|cffe4cfa3Последний Гронн|r (|cffffffffX|r)"
    checks_def.append({"type": "unit", "id": "N05O", "field": "name", "expected": wts_updates[29128]})
    checks_def.append({"type": "unit", "id": "N05O", "field": "tip", "expected": wts_updates[29682]})
    checks_def.append({"type": "unit", "id": "N05O", "field": "ubertip", "expected": wts_updates[42389]})
    checks_def.append({"type": "unit", "id": "N05O", "field": "awakentip", "expected": wts_updates[29681]})
    checks_def.append({"type": "unit", "id": "N05O", "field": "revivetip", "expected": wts_updates[29683]})

    # =========================================================================
    # 4. UNITS (17 regular + 2 summons)
    # =========================================================================
    # o03W: Огр-Строитель (Q)
    wts_updates[28179] = "|cffe4cfa3Огр-Строитель|r"
    wts_updates[42467] = "|cffe4cfa3Огр-Строитель|r (|cffffffffQ|r)"
    wts_updates[42468] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий огров. Добывает золото и древесину, а также возводит и чинит строения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДобыча ресурсов|cffced4da: сбор золота и заготовка древесины.|n"
        "- |cffa9c7deРемонт|cffced4da: восстановление запаса прочности зданий.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03W", "field": "name", "expected": wts_updates[28179]})
    checks_def.append({"type": "unit", "id": "o03W", "field": "tip", "expected": wts_updates[42467]})
    checks_def.append({"type": "unit", "id": "o03W", "field": "ubertip", "expected": wts_updates[42468]})

    # o03I: Огр-воин (Q)
    wts_updates[27849] = "|cffe4cfa3Огр-воин|r"
    wts_updates[41062] = "|cffe4cfa3Огр-воин|r (|cffffffffQ|r)"
    wts_updates[42705] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый тяжелый боец ближнего боя армии Огров.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСильный удар|cffced4da: вероятность нанести удвоенный урон и оглушить цель.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03I", "field": "name", "expected": wts_updates[27849]})
    checks_def.append({"type": "unit", "id": "o03I", "field": "tip", "expected": wts_updates[41062]})
    checks_def.append({"type": "unit", "id": "o03I", "field": "ubertip", "expected": wts_updates[42705]})

    # o03H: Огр-Копьеметатель (W)
    wts_updates[25373] = "|cffe4cfa3Огр-Копьеметатель|r"
    wts_updates[36678] = "|cffe4cfa3Огр-Копьеметатель|r (|cffffffffW|r)"
    wts_updates[42704] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стрелок дальнего боя, метающий тяжелые копья.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУсиленное копьё|cffced4da: пробивает небронированные цели и среднюю броню (требует исследования).|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03H", "field": "name", "expected": wts_updates[25373]})
    checks_def.append({"type": "unit", "id": "o03H", "field": "tip", "expected": wts_updates[36678]})
    checks_def.append({"type": "unit", "id": "o03H", "field": "ubertip", "expected": wts_updates[42704]})

    # o03G: Огр-Камнеметатель (E)
    wts_updates[27845] = "|cffe4cfa3Огр-Камнеметатель|r"
    wts_updates[35483] = "|cffe4cfa3Огр-Камнеметатель|r (|cffffffffE|r)"
    wts_updates[42703] = (
        "|cffa6afb8ЮНИТ:|cffced4da Осадный боец дальнего боя, мечущий массивные валуны по площади.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03G", "field": "name", "expected": wts_updates[27845]})
    checks_def.append({"type": "unit", "id": "o03G", "field": "tip", "expected": wts_updates[35483]})
    checks_def.append({"type": "unit", "id": "o03G", "field": "ubertip", "expected": wts_updates[42703]})

    # o03F: Огр-Командир (R)
    wts_updates[27843] = "|cffe4cfa3Огр-Командир|r"
    wts_updates[35443] = "|cffe4cfa3Огр-Командир|r (|cffffffffR|r)"
    wts_updates[42702] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный командир ближнего боя, вдохновляющий союзников и усиливающий их защиту.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Защиты|cffced4da: увеличивает броню находящихся рядом союзников на |cffffffff2|cffced4da ед.|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03F", "field": "name", "expected": wts_updates[27843]})
    checks_def.append({"type": "unit", "id": "o03F", "field": "tip", "expected": wts_updates[35443]})
    checks_def.append({"type": "unit", "id": "o03F", "field": "ubertip", "expected": wts_updates[42702]})

    # o03K: Огр-Наездник (Q)
    wts_updates[27870] = "|cffe4cfa3Огр-Наездник|r"
    wts_updates[41951] = "|cffe4cfa3Огр-Наездник|r (|cffffffffQ|r)"
    wts_updates[42706] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый мобильный всадник, выслеживающий и связывающий вражеские войска.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВоля Охоты|cffced4da: увеличивает урон от атак по героям и юнитам в |cffffffff1.3|cffced4da раза.|n"
        "- |cffa9c7deОпутывание|cffced4da: обездвиживает цель и опускает воздушных врагов на землю (требует исследования).|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03K", "field": "name", "expected": wts_updates[27870]})
    checks_def.append({"type": "unit", "id": "o03K", "field": "tip", "expected": wts_updates[41951]})
    checks_def.append({"type": "unit", "id": "o03K", "field": "ubertip", "expected": wts_updates[42706]})

    # o03L: Огр-Барабанщик (W)
    wts_updates[27872] = "|cffe4cfa3Огр-Барабанщик|r"
    wts_updates[41952] = "|cffe4cfa3Огр-Барабанщик|r (|cffffffffW|r)"
    wts_updates[42707] = (
        "|cffa6afb8ЮНИТ:|cffced4da Воин поддержки, поддерживающий боевой дух армии грохотом барабанов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБоевые барабаны|cffced4da: повышает урон атак союзников на |cffffffff10%|cffced4da.|n"
        "- |cffa9c7deДеморализующий звук|cffced4da: снижает урон вражеских войск на |cffffffff10%|cffced4da (требует исследования).|n"
        "- |cffa9c7deУдарная волна|cffced4da: наносит урон врагам ударной волной от барабана.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03L", "field": "name", "expected": wts_updates[27872]})
    checks_def.append({"type": "unit", "id": "o03L", "field": "tip", "expected": wts_updates[41952]})
    checks_def.append({"type": "unit", "id": "o03L", "field": "ubertip", "expected": wts_updates[42707]})

    # o03M: Огр-Берсерк (E)
    wts_updates[27874] = "|cffe4cfa3Огр-Берсерк|r"
    wts_updates[42012] = "|cffe4cfa3Огр-Берсерк|r (|cffffffffE|r)"
    wts_updates[42708] = (
        "|cffa6afb8ЮНИТ:|cffced4da Неистовый боец ближнего боя, атакующий с сокрушительной скоростью и силой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: наносит урон соседним вражеским бойцам.|n"
        "- |cffa9c7deБешенство|cffced4da: ускоряет атаку и перемещение ценой получаемого урона.|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03M", "field": "name", "expected": wts_updates[27874]})
    checks_def.append({"type": "unit", "id": "o03M", "field": "tip", "expected": wts_updates[42012]})
    checks_def.append({"type": "unit", "id": "o03M", "field": "ubertip", "expected": wts_updates[42708]})

    # o03N: Огр-Маг (Q)
    wts_updates[27876] = "|cffe4cfa3Огр-Маг|r"
    wts_updates[42017] = "|cffe4cfa3Огр-Маг|r (|cffffffffQ|r)"
    wts_updates[29047] = (
        "|cffa6afb8ЮНИТ:|cffced4da Двухголовый колдун поддержки, усиливающий армию кровожадностью и рассеивающий чары.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненная стрела|cffced4da: наносит урон и оглушает врага.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты заклинаний и наносит урон призывным существам.|n"
        "- |cffa9c7deЖажда крови|cffced4da: существенно ускоряет атаку и бег союзного воина.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03N", "field": "name", "expected": wts_updates[27876]})
    checks_def.append({"type": "unit", "id": "o03N", "field": "tip", "expected": wts_updates[42017]})
    checks_def.append({"type": "unit", "id": "o03N", "field": "ubertip", "expected": wts_updates[29047]})

    # o03O: Огр-Боевой Маг (W)
    wts_updates[27878] = "|cffe4cfa3Огр-Боевой Маг|r"
    wts_updates[42421] = "|cffe4cfa3Огр-Боевой Маг|r (|cffffffffW|r)"
    wts_updates[31787] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелый боевой маг, связывающий союзников узами духа и сковывающий врагов огненным лассо.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДуховная Связь|cffced4da: распределяет получаемый урон между связанными союзниками.|n"
        "- |cffa9c7deЗачарованный руной Молот|cffced4da: поджигает атакованные вражеские здания.|n"
        "- |cffa9c7deОгненное лассо|cffced4da: сковывает цель, нанося периодический урон.|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03O", "field": "name", "expected": wts_updates[27878]})
    checks_def.append({"type": "unit", "id": "o03O", "field": "tip", "expected": wts_updates[42421]})
    checks_def.append({"type": "unit", "id": "o03O", "field": "ubertip", "expected": wts_updates[31787]})

    # o03P: Шаман Мок'Натал (E)
    wts_updates[27880] = "|cffe4cfa3Шаман Мок'Натал|r"
    wts_updates[42423] = "|cffe4cfa3Шаман Мок'Натал|r (|cffffffffE|r)"
    wts_updates[31834] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мудрый шаман полуорков-полуогров. Повелевает стихией молний и призывает свирепых зверей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЩит молний|cffced4da: окружает цель электрическим щитом, наносящим урон вокруг.|n"
        "- |cffa9c7deПризыв вепря|cffced4da: призывает боевого иглобрюха.|n"
        "- |cffa9c7deЦепная молния|cffced4da: поражает цепь врагов электрическим разрядом.|n|n"
        "Атакует |cffffffffназемные|cffced4da и |cffffffffвоздушные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03P", "field": "name", "expected": wts_updates[27880]})
    checks_def.append({"type": "unit", "id": "o03P", "field": "tip", "expected": wts_updates[42423]})
    checks_def.append({"type": "unit", "id": "o03P", "field": "ubertip", "expected": wts_updates[31834]})

    # o03Q: Огрон (Q)
    wts_updates[27882] = "|cffe4cfa3Огрон|r"
    wts_updates[42424] = "|cffe4cfa3Огрон|r (|cffffffffQ|r)"
    wts_updates[42712] = (
        "|cffa6afb8ЮНИТ:|cffced4da Массивный полу-гронн колоссальной силы, проламывающий ряды противника.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести удвоенный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03Q", "field": "name", "expected": wts_updates[27882]})
    checks_def.append({"type": "unit", "id": "o03Q", "field": "tip", "expected": wts_updates[42424]})
    checks_def.append({"type": "unit", "id": "o03Q", "field": "ubertip", "expected": wts_updates[42712]})

    # o03R: Огрон-синий (E)
    wts_updates[27884] = "|cffe4cfa3Огрон-синий|r"
    wts_updates[42457] = "|cffe4cfa3Огрон-синий|r (|cffffffffE|r)"
    wts_updates[42713] = (
        "|cffa6afb8ЮНИТ:|cffced4da Северный огрон, закаленный ледяными ветрами. Защищает себя морозным щитом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМорозный доспех|cffced4da: повышает броню и замедляет атакующих в ближнем бою врагов (требует исследования).|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03R", "field": "name", "expected": wts_updates[27884]})
    checks_def.append({"type": "unit", "id": "o03R", "field": "tip", "expected": wts_updates[42457]})
    checks_def.append({"type": "unit", "id": "o03R", "field": "ubertip", "expected": wts_updates[42713]})

    # o03S: Огрон Красный (W)
    wts_updates[27886] = "|cffe4cfa3Огрон Красный|r"
    wts_updates[42459] = "|cffe4cfa3Огрон Красный|r (|cffffffffW|r)"
    wts_updates[42714] = (
        "|cffa6afb8ЮНИТ:|cffced4da Свирепый огрон, впадающий в неистовство в гуще сражения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНеистовство|cffced4da: кратковременно увеличивает скорость атаки (требует исследования).|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03S", "field": "name", "expected": wts_updates[27886]})
    checks_def.append({"type": "unit", "id": "o03S", "field": "tip", "expected": wts_updates[42459]})
    checks_def.append({"type": "unit", "id": "o03S", "field": "ubertip", "expected": wts_updates[42714]})

    # o03T: Гронн Черный (A)
    wts_updates[28170] = "|cffe4cfa3Гронн Черный|r"
    wts_updates[42461] = "|cffe4cfa3Гронн Черный|r (|cffffffffA|r)"
    wts_updates[42715] = (
        "|cffa6afb8ЮНИТ:|cffced4da Древний исполин, покрытый каменными шипами. Отражает получаемый урон обратно во врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deШипастый панцирь|cffced4da: отражает часть урона ближнего боя и повышает броню (требует исследования).|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03T", "field": "name", "expected": wts_updates[28170]})
    checks_def.append({"type": "unit", "id": "o03T", "field": "tip", "expected": wts_updates[42461]})
    checks_def.append({"type": "unit", "id": "o03T", "field": "ubertip", "expected": wts_updates[42715]})

    # o03U: Гронн Белый (A)
    wts_updates[28173] = "|cffe4cfa3Гронн Белый|r"
    wts_updates[42463] = "|cffe4cfa3Гронн Белый|r (|cffffffffA|r)"
    wts_updates[42716] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий северный исполин, сотрясающий землю ударами колоссальной силы.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСокрушение|cffced4da: вероятность нанести урон по площади вокруг цели (требует исследования).|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03U", "field": "name", "expected": wts_updates[28173]})
    checks_def.append({"type": "unit", "id": "o03U", "field": "tip", "expected": wts_updates[42463]})
    checks_def.append({"type": "unit", "id": "o03U", "field": "ubertip", "expected": wts_updates[42716]})

    # o03V: Гронн Красный (A)
    wts_updates[28176] = "|cffe4cfa3Гронн Красный|r"
    wts_updates[42465] = "|cffe4cfa3Гронн Красный|r (|cffffffffA|r)"
    wts_updates[42717] = (
        "|cffa6afb8ЮНИТ:|cffced4da Неукротимый великан, черпающий мощь в жажде битвы.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЖажда Крови|cffced4da: накладывает на себя эффект ускорения атаки и бега (требует исследования).|n"
        "- |cffa9c7deСильный удар|cffced4da: вероятность оглушить цель и нанести дополнительный урон.|n|n"
        "Атакует |cffffffffназемные|cffced4da цели.|r"
    )
    checks_def.append({"type": "unit", "id": "o03V", "field": "name", "expected": wts_updates[28176]})
    checks_def.append({"type": "unit", "id": "o03V", "field": "tip", "expected": wts_updates[42465]})
    checks_def.append({"type": "unit", "id": "o03V", "field": "ubertip", "expected": wts_updates[42717]})

    # Summons
    wts_updates[27764] = "|cffe4cfa3Бешеный вепрь|r"
    wts_updates[27990] = "|cffe4cfa3Ястреб-разведчик|r"
    checks_def.append({"type": "unit", "id": "n05M", "field": "name", "expected": wts_updates[27764]})
    checks_def.append({"type": "unit", "id": "n05N", "field": "name", "expected": wts_updates[27990]})

    # =========================================================================
    # 5. UPGRADES (19 technologies & upgrades)
    # =========================================================================
    # R0GL: Заостренные дубины (6 levels, melee weapons)
    r0gl_names = [28231, 42499, 42500, 28236, 42489, 28219]
    r0gl_tips = [42501, 42502, 42503, 42490, 42491, 42492]
    r0gl_ubs = [42493, 42494, 42495, 42496, 42497, 42498]
    r0gl_dmg = [7, 14, 21, 28, 35, 42]
    for lvl in range(1, 7):
        wts_updates[r0gl_names[lvl-1]] = f"|cffe4cfa3Заостренные дубины|r — уровень {lvl}"
        wts_updates[r0gl_tips[lvl-1]] = f"|cffe4cfa3Заостренные дубины — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r0gl_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон бойцов ближнего боя на |cffc8e087+{r0gl_dmg[lvl-1]}|cffced4da.|n|n"
            "Применяется к:|n- |cffa9c7deОгр-воин|cffced4da, |cffa9c7deОгр-Командир|cffced4da, |cffa9c7deОгр-Наездник|cffced4da, "
            "|cffa9c7deОгр-Берсерк|cffced4da, |cffa9c7deОгр-Боевой Маг|cffced4da, |cffa9c7deОгроны|cffced4da, |cffa9c7deГронны|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GL", "field": f"name{lvl}", "expected": wts_updates[r0gl_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GL", "field": f"tip{lvl}", "expected": wts_updates[r0gl_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GL", "field": f"ubertip{lvl}", "expected": wts_updates[r0gl_ubs[lvl-1]]})

    # R0GM: Шкуры зверей (6 levels, armor)
    r0gm_names = [28253, 42513, 42514, 28255, 28241, 28242]
    r0gm_tips = [42517, 42516, 42515, 42504, 42505, 42506]
    r0gm_ubs = [42507, 42508, 42509, 42510, 42511, 42512]
    r0gm_def = [2, 4, 6, 8, 10, 12]
    for lvl in range(1, 7):
        wts_updates[r0gm_names[lvl-1]] = f"|cffe4cfa3Шкуры зверей|r — уровень {lvl}"
        wts_updates[r0gm_tips[lvl-1]] = f"|cffe4cfa3Шкуры зверей — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r0gm_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает защиту всех видов огров на |cffc8e087+{r0gm_def[lvl-1]}|cffced4da к броне.|n|n"
            "Применяется к:|n- |cffa9c7deВсем войскам армии Огров|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GM", "field": f"name{lvl}", "expected": wts_updates[r0gm_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GM", "field": f"tip{lvl}", "expected": wts_updates[r0gm_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GM", "field": f"ubertip{lvl}", "expected": wts_updates[r0gm_ubs[lvl-1]]})

    # R0GN: Крупные камни (6 levels, ranged weapons)
    r0gn_names = [28269, 42527, 42528, 28270, 28257, 28258]
    r0gn_tips = [42529, 42531, 42530, 42518, 42519, 42520]
    r0gn_ubs = [42524, 42525, 42526, 42521, 42522, 42523]
    r0gn_dmg = [6, 12, 18, 24, 30, 36]
    for lvl in range(1, 7):
        wts_updates[r0gn_names[lvl-1]] = f"|cffe4cfa3Крупные камни|r — уровень {lvl}"
        wts_updates[r0gn_tips[lvl-1]] = f"|cffe4cfa3Крупные камни — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[r0gn_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон стрелков и метателей огров на |cffc8e087+{r0gn_dmg[lvl-1]}|cffced4da.|n|n"
            "Применяется к:|n- |cffa9c7deОгр-Копьеметатель|cffced4da, |cffa9c7deОгр-Камнеметатель|cffced4da, "
            "|cffa9c7deОгр-Барабанщик|cffced4da, |cffa9c7deШаман Мок'Натал|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GN", "field": f"name{lvl}", "expected": wts_updates[r0gn_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GN", "field": f"tip{lvl}", "expected": wts_updates[r0gn_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GN", "field": f"ubertip{lvl}", "expected": wts_updates[r0gn_ubs[lvl-1]]})

    # R0GO: Крепость плоти (3 levels, hp)
    r0go_names = [28275, 28280, 28281]
    r0go_tips = [42532, 42535, 42536]
    r0go_ubs = [42537, 42533, 42534]
    r0go_hp = [100, 200, 300]
    for lvl in range(1, 4):
        wts_updates[r0go_names[lvl-1]] = f"|cffe4cfa3Крепость плоти|r — уровень {lvl}"
        wts_updates[r0go_tips[lvl-1]] = f"|cffe4cfa3Крепость плоти — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[r0go_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья воинов огров на |cffc8e087+{r0go_hp[lvl-1]}|cffced4da ед.|n|n"
            "Применяется к:|n- |cffa9c7deВсем воинам армии Огров|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GO", "field": f"name{lvl}", "expected": wts_updates[r0go_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GO", "field": f"tip{lvl}", "expected": wts_updates[r0go_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GO", "field": f"ubertip{lvl}", "expected": wts_updates[r0go_ubs[lvl-1]]})

    # R0GP: Сила предков (3 levels, regen)
    r0gp_names = [28284, 28285, 28286]
    r0gp_tips = [42538, 42539, 42540]
    r0gp_ubs = [28292, 28293, 28294]
    r0gp_reg = [1, 2, 3]
    for lvl in range(1, 4):
        wts_updates[r0gp_names[lvl-1]] = f"|cffe4cfa3Сила предков|r — уровень {lvl}"
        wts_updates[r0gp_tips[lvl-1]] = f"|cffe4cfa3Сила предков — уровень {lvl}|r (|cffffffffF|r)"
        wts_updates[r0gp_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость регенерации здоровья воинов огров на |cffc8e087+{r0gp_reg[lvl-1]}|cffced4da ед./сек.|n|n"
            "Применяется к:|n- |cffa9c7deВсем воинам армии Огров|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GP", "field": f"name{lvl}", "expected": wts_updates[r0gp_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GP", "field": f"tip{lvl}", "expected": wts_updates[r0gp_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GP", "field": f"ubertip{lvl}", "expected": wts_updates[r0gp_ubs[lvl-1]]})

    # R0GQ: Сбор древесины (6 levels, lumber)
    r0gq_names = [42541, 42542, 42543, 42544, 42545, 42546]
    r0gq_tips = [42669, 42670, 42671, 42672, 42673, 42674]
    r0gq_ubs = [27667, 25923, 25924, 25925, 25928, 28313]
    r0gq_lum = [10, 20, 30, 40, 50, 60]
    for lvl in range(1, 7):
        wts_updates[r0gq_names[lvl-1]] = f"|cffe4cfa3Сбор древесины|r — уровень {lvl}"
        wts_updates[r0gq_tips[lvl-1]] = f"|cffe4cfa3Сбор древесины — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0gq_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет рабочим переносить на |cffc8e087+{r0gq_lum[lvl-1]}|cffced4da ед. больше древесины.|n|n"
            "Применяется к:|n- |cffa9c7deОгр-Строитель|cffced4da.|n|n"
            f"Уровень исследования: |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GQ", "field": f"name{lvl}", "expected": wts_updates[r0gq_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GQ", "field": f"tip{lvl}", "expected": wts_updates[r0gq_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GQ", "field": f"ubertip{lvl}", "expected": wts_updates[r0gq_ubs[lvl-1]]})

    # R09W: Усиленное копьё (1 level)
    wts_updates[42587] = "|cffe4cfa3Усиленное копьё|r"
    wts_updates[42588] = "|cffe4cfa3Усиленное копьё|r (|cffffffffX|r)"
    wts_updates[42593] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Снаряжает копьеметателей утяжеленными наконечниками, эффективно пробивающими небронированные цели и среднюю броню.|n|n"
        "Применяется к:|n- |cffa9c7deОгр-Копьеметатель|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R09W", "field": "name1", "expected": wts_updates[42587]})
    checks_def.append({"type": "upgrade", "id": "R09W", "field": "tip1", "expected": wts_updates[42588]})
    checks_def.append({"type": "upgrade", "id": "R09W", "field": "ubertip1", "expected": wts_updates[42593]})

    # R0GU: Опутывание (1 level)
    wts_updates[28428] = "|cffe4cfa3Опутывание|r"
    wts_updates[42566] = "|cffe4cfa3Опутывание|r (|cffffffffZ|r)"
    checks_def.append({"type": "upgrade", "id": "R0GU", "field": "name1", "expected": wts_updates[28428]})
    checks_def.append({"type": "upgrade", "id": "R0GU", "field": "tip1", "expected": wts_updates[42566]})

    # R0L2: Кожаная мембрана (1 level)
    wts_updates[42594] = "|cffe4cfa3Кожаная мембрана|r"
    wts_updates[42596] = "|cffe4cfa3Кожаная мембрана|r (|cffffffffZ|r)"
    wts_updates[42598] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает барабанщиков прочной кожаной мембраной, открывая способность «Деморализующий звук», снижающую урон врагов на |cffe69a8d10%|cffced4da.|n|n"
        "Применяется к:|n- |cffa9c7deОгр-Барабанщик|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0L2", "field": "name1", "expected": wts_updates[42594]})
    checks_def.append({"type": "upgrade", "id": "R0L2", "field": "tip1", "expected": wts_updates[42596]})
    checks_def.append({"type": "upgrade", "id": "R0L2", "field": "ubertip1", "expected": wts_updates[42598]})

    # R0GR: Обучение боевых магов (3 levels)
    r0gr_names = [42547, 42548, 42551]
    r0gr_tips = [42549, 42550, 42552]
    r0gr_ubs = [42553, 28484, 36234]
    r0gr_spells = [
        "«Духовная Связь»",
        "«Духовная Связь», «Зачарованный руной Молот»",
        "«Духовная Связь», «Зачарованный руной Молот», «Огненное лассо»"
    ]
    for lvl in range(1, 4):
        wts_updates[r0gr_names[lvl-1]] = f"|cffe4cfa3Обучение боевых магов|r — ступень {lvl}"
        wts_updates[r0gr_tips[lvl-1]] = f"|cffe4cfa3Обучение боевых магов — ступень {lvl}|r (|cffffffffX|r)"
        wts_updates[r0gr_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, маны и регенерацию Огров-Боевых Магов, а также открывает заклинания: {r0gr_spells[lvl-1]}.|n|n"
            "Применяется к:|n- |cffa9c7deОгр-Боевой Маг|cffced4da.|n|n"
            f"Ступень обучения: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GR", "field": f"name{lvl}", "expected": wts_updates[r0gr_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GR", "field": f"tip{lvl}", "expected": wts_updates[r0gr_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GR", "field": f"ubertip{lvl}", "expected": wts_updates[r0gr_ubs[lvl-1]]})

    # R0GS: Обучение магов поддержки (3 levels)
    r0gs_names = [42554, 42555, 42558]
    r0gs_tips = [42556, 42557, 42559]
    r0gs_ubs = [28401, 28407, 28413]
    r0gs_spells = [
        "«Огненная стрела»",
        "«Огненная стрела», «Рассеивание заклинаний»",
        "«Огненная стрела», «Рассеивание заклинаний», «Жажда крови»"
    ]
    for lvl in range(1, 4):
        wts_updates[r0gs_names[lvl-1]] = f"|cffe4cfa3Обучение магов поддержки|r — ступень {lvl}"
        wts_updates[r0gs_tips[lvl-1]] = f"|cffe4cfa3Обучение магов поддержки — ступень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r0gs_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, маны и скорость восстановления маны Огров-Магов, а также открывает заклинания: {r0gs_spells[lvl-1]}.|n|n"
            "Применяется к:|n- |cffa9c7deОгр-Маг|cffced4da.|n|n"
            f"Ступень обучения: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GS", "field": f"name{lvl}", "expected": wts_updates[r0gs_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GS", "field": f"tip{lvl}", "expected": wts_updates[r0gs_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GS", "field": f"ubertip{lvl}", "expected": wts_updates[r0gs_ubs[lvl-1]]})

    # R0GT: Обучение Шаманов Мок'Натала (3 levels)
    r0gt_names = [42560, 42561, 42564]
    r0gt_tips = [42562, 42563, 42565]
    r0gt_ubs = [28414, 28885, 28886]
    r0gt_spells = [
        "«Щит молний»",
        "«Щит молний», «Призыв вепря»",
        "«Щит молний», «Призыв вепря», «Цепная молния»"
    ]
    for lvl in range(1, 4):
        wts_updates[r0gt_names[lvl-1]] = f"|cffe4cfa3Обучение Шаманов Мок'Натала|r — ступень {lvl}"
        wts_updates[r0gt_tips[lvl-1]] = f"|cffe4cfa3Обучение Шаманов Мок'Натала — ступень {lvl}|r (|cffffffffC|r)"
        wts_updates[r0gt_ubs[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья, маны и регенерацию маны Шаманов Мок'Натала, а также открывает заклинания: {r0gt_spells[lvl-1]}.|n|n"
            "Применяется к:|n- |cffa9c7deШаман Мок'Натал|cffced4da.|n|n"
            f"Ступень обучения: |cffffffff{lvl}|cffced4da/|cffffffff3|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0GT", "field": f"name{lvl}", "expected": wts_updates[r0gt_names[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GT", "field": f"tip{lvl}", "expected": wts_updates[r0gt_tips[lvl-1]]})
        checks_def.append({"type": "upgrade", "id": "R0GT", "field": f"ubertip{lvl}", "expected": wts_updates[r0gt_ubs[lvl-1]]})

    # R0GF: Каменная плоть (1 level)
    wts_updates[28061] = "|cffe4cfa3Каменная плоть|r"
    wts_updates[28062] = "|cffe4cfa3Каменная плоть|r (|cffffffffE|r)"
    wts_updates[28195] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет тело древних великанов, повышая броню на |cffc8e087+5|cffced4da ед.|n|n"
        "Применяется к:|n- |cffa9c7deОгронам|cffced4da, |cffa9c7deГроннам|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0GF", "field": "name1", "expected": wts_updates[28061]})
    checks_def.append({"type": "upgrade", "id": "R0GF", "field": "tip1", "expected": wts_updates[28062]})
    checks_def.append({"type": "upgrade", "id": "R0GF", "field": "ubertip1", "expected": wts_updates[28195]})

    # R0GG: Жажда Крови (1 level)
    wts_updates[28074] = "|cffe4cfa3Жажда Крови|r"
    wts_updates[28075] = "|cffe4cfa3Жажда Крови|r (|cffffffffW|r)"
    wts_updates[42485] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Жажда Крови» Красному Гронну, позволяя ускорять атаку и передвижение.|n|n"
        "Применяется к:|n- |cffa9c7deГронн Красный|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0GG", "field": "name1", "expected": wts_updates[28074]})
    checks_def.append({"type": "upgrade", "id": "R0GG", "field": "tip1", "expected": wts_updates[28075]})
    checks_def.append({"type": "upgrade", "id": "R0GG", "field": "ubertip1", "expected": wts_updates[42485]})

    # R0GH: Морозный Доспех (1 level)
    wts_updates[28087] = "|cffe4cfa3Морозный Доспех|r"
    wts_updates[28088] = "|cffe4cfa3Морозный Доспех|r (|cffffffffQ|r)"
    wts_updates[28197] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует Синему Огрону способность «Морозный доспех», увеличивающую броню и замедляющую атакующих врагов.|n|n"
        "Применяется к:|n- |cffa9c7deОгрон-синий|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0GH", "field": "name1", "expected": wts_updates[28087]})
    checks_def.append({"type": "upgrade", "id": "R0GH", "field": "tip1", "expected": wts_updates[28088]})
    checks_def.append({"type": "upgrade", "id": "R0GH", "field": "ubertip1", "expected": wts_updates[28197]})

    # R0GI: Шипастый Панцирь (1 level)
    wts_updates[28199] = "|cffe4cfa3Шипастый Панцирь|r"
    wts_updates[28475] = "|cffe4cfa3Шипастый Панцирь|r (|cffffffffS|r)"
    wts_updates[42486] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует Черному Гронну пассивный шипастый панцирь, отражающий |cffffffff15%|cffced4da урона ближнего боя и дающий |cffc8e087+3|cffced4da к броне.|n|n"
        "Применяется к:|n- |cffa9c7deГронн Черный|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0GI", "field": "name1", "expected": wts_updates[28199]})
    checks_def.append({"type": "upgrade", "id": "R0GI", "field": "tip1", "expected": wts_updates[28475]})
    checks_def.append({"type": "upgrade", "id": "R0GI", "field": "ubertip1", "expected": wts_updates[42486]})

    # R0GJ: Сокрушение (1 level)
    wts_updates[28100] = "|cffe4cfa3Сокрушение|r"
    wts_updates[28101] = "|cffe4cfa3Сокрушение|r (|cffffffffD|r)"
    wts_updates[42487] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует Белому Гронну способность «Сокрушение», позволяющую с вероятностью |cffffffff40%|cffced4da наносить урон по площади.|n|n"
        "Применяется к:|n- |cffa9c7deГронн Белый|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0GJ", "field": "name1", "expected": wts_updates[28100]})
    checks_def.append({"type": "upgrade", "id": "R0GJ", "field": "tip1", "expected": wts_updates[28101]})
    checks_def.append({"type": "upgrade", "id": "R0GJ", "field": "ubertip1", "expected": wts_updates[42487]})

    # R0GK: Неистовство (1 level)
    wts_updates[28214] = "|cffe4cfa3Неистовство|r"
    wts_updates[28476] = "|cffe4cfa3Неистовство|r (|cffffffffA|r)"
    wts_updates[42488] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Неистовство» Красному Огрону, существенно ускоряющую его атаки в бою.|n|n"
        "Применяется к:|n- |cffa9c7deОгрон Красный|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0GK", "field": "name1", "expected": wts_updates[28214]})
    checks_def.append({"type": "upgrade", "id": "R0GK", "field": "tip1", "expected": wts_updates[28476]})
    checks_def.append({"type": "upgrade", "id": "R0GK", "field": "ubertip1", "expected": wts_updates[42488]})

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # A176: Сильный удар (Bash)
    wts_updates[28183] = "|cffe4cfa3Сильный удар|r"
    wts_updates[28182] = "|cffe4cfa3Сильный удар|r"
    wts_updates[28961] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff12%|cffced4da наносит в |cffffffff2|cffced4da раза больше урона и оглушает цель на |cffffffff1|cffced4da сек. (|cffffffff0.2|cffced4da сек. для героев).|r"
    )
    checks_def.append({"type": "ability", "id": "A176", "field": "name", "expected": wts_updates[28183]})
    checks_def.append({"type": "ability", "id": "A176", "field": "tip1", "expected": wts_updates[28182]})
    checks_def.append({"type": "ability", "id": "A176", "field": "ubertip1", "expected": wts_updates[28961]})

    # A177: Усиленное Копьё
    wts_updates[42722] = "|cffe4cfa3Усиленное копьё|r"
    wts_updates[42723] = "|cffe4cfa3Усиленное копьё|r"
    wts_updates[42469] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Огр метает копьё с огромной силой, пробивая цели без брони и цели со средней бронёй.|r"
    )
    checks_def.append({"type": "ability", "id": "A177", "field": "name", "expected": wts_updates[42722]})
    checks_def.append({"type": "ability", "id": "A177", "field": "tip1", "expected": wts_updates[42723]})
    checks_def.append({"type": "ability", "id": "A177", "field": "ubertip1", "expected": wts_updates[42469]})

    # A178: Аура Защиты
    wts_updates[27766] = "|cffe4cfa3Аура Защиты|r"
    wts_updates[27767] = "|cffe4cfa3Аура Защиты|r"
    wts_updates[20305] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню находящихся рядом дружественных войск на |cffc8e087+2|cffced4da.|n|n"
        "Радиус действия: |cffffffff300|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A178", "field": "name", "expected": wts_updates[27766]})
    checks_def.append({"type": "ability", "id": "A178", "field": "tip1", "expected": wts_updates[27767]})
    checks_def.append({"type": "ability", "id": "A178", "field": "ubertip1", "expected": wts_updates[20305]})

    # A179: Воля Охоты
    wts_updates[42470] = "|cffe4cfa3Воля Охоты|r"
    wts_updates[42471] = "|cffe4cfa3Воля Охоты|r"
    wts_updates[27890] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон атак по героям и воинам в |cffffffff1.3|cffced4da раза.|r"
    )
    checks_def.append({"type": "ability", "id": "A179", "field": "name", "expected": wts_updates[42470]})
    checks_def.append({"type": "ability", "id": "A179", "field": "tip1", "expected": wts_updates[42471]})
    checks_def.append({"type": "ability", "id": "A179", "field": "ubertip1", "expected": wts_updates[27890]})

    # A17A: Опутывание
    wts_updates[27892] = "|cffe4cfa3Опутывание|r"
    wts_updates[28321] = "|cffe4cfa3Опутывание|r"
    checks_def.append({"type": "ability", "id": "A17A", "field": "name", "expected": wts_updates[27892]})
    checks_def.append({"type": "ability", "id": "A17A", "field": "tip1", "expected": wts_updates[28321]})

    # A17B: Боевые барабаны
    wts_updates[28322] = "|cffe4cfa3Боевые барабаны|r"
    wts_updates[28323] = "|cffe4cfa3Боевые барабаны|r"
    wts_updates[41136] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон от атак находящихся рядом союзных войск на |cffc8e087+10%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A17B", "field": "name", "expected": wts_updates[28322]})
    checks_def.append({"type": "ability", "id": "A17B", "field": "tip1", "expected": wts_updates[28323]})
    checks_def.append({"type": "ability", "id": "A17B", "field": "ubertip1", "expected": wts_updates[41136]})

    # A17O: Деморализующий звук
    wts_updates[28472] = "|cffe4cfa3Деморализующий звук|r"
    wts_updates[28473] = "|cffe4cfa3Деморализующий звук|r"
    wts_updates[28474] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Грохот барабанов подавляет боевой дух врагов, снижая наносимый ими урон на |cffe69a8d10%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A17O", "field": "name", "expected": wts_updates[28472]})
    checks_def.append({"type": "ability", "id": "A17O", "field": "tip1", "expected": wts_updates[28473]})
    checks_def.append({"type": "ability", "id": "A17O", "field": "ubertip1", "expected": wts_updates[28474]})

    # A0WU: Ударная волна (Барабанщик)
    wts_updates[28004] = "|cffe4cfa3Ударная волна|r"
    wts_updates[28829] = "|cffe4cfa3Ударная волна|r"
    wts_updates[28831] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощнейший удар по барабанам порождает ударную волну, наносящую урон врагам на своём пути.|r"
    )
    checks_def.append({"type": "ability", "id": "A0WU", "field": "name", "expected": wts_updates[28004]})
    checks_def.append({"type": "ability", "id": "A0WU", "field": "tip1", "expected": wts_updates[28829]})
    checks_def.append({"type": "ability", "id": "A0WU", "field": "ubertip1", "expected": wts_updates[28831]})

    # A17D: Рассекающий удар
    wts_updates[28326] = "|cffe4cfa3Рассекающий удар|r"
    wts_updates[28327] = "|cffe4cfa3Рассекающий удар|r"
    wts_updates[28963] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Массивные удары бойца задевают стоящих рядом врагов, нанося им |cffffffff13%|cffced4da урона.|r"
    )
    checks_def.append({"type": "ability", "id": "A17D", "field": "name", "expected": wts_updates[28326]})
    checks_def.append({"type": "ability", "id": "A17D", "field": "tip1", "expected": wts_updates[28327]})
    checks_def.append({"type": "ability", "id": "A17D", "field": "ubertip1", "expected": wts_updates[28963]})

    # A17E: Бешенство
    wts_updates[28329] = "|cffe4cfa3Бешенство|r"
    wts_updates[28330] = "|cffe4cfa3Бешенство|r"
    checks_def.append({"type": "ability", "id": "A17E", "field": "name", "expected": wts_updates[28329]})
    checks_def.append({"type": "ability", "id": "A17E", "field": "tip1", "expected": wts_updates[28330]})

    # A17C: Рассеивание заклинаний
    wts_updates[2423] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[2424] = "|cffe4cfa3Рассеивание заклинаний|r"
    checks_def.append({"type": "ability", "id": "A17C", "field": "name", "expected": wts_updates[2423]})
    checks_def.append({"type": "ability", "id": "A17C", "field": "tip1", "expected": wts_updates[2424]})

    # A17F: Жажда крови
    wts_updates[2425] = "|cffe4cfa3Жажда крови|r"
    wts_updates[2426] = "|cffe4cfa3Жажда крови|r"
    checks_def.append({"type": "ability", "id": "A17F", "field": "name", "expected": wts_updates[2425]})
    checks_def.append({"type": "ability", "id": "A17F", "field": "tip1", "expected": wts_updates[2426]})

    # A1RA: Огненная стрела
    wts_updates[2856] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[31646] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[31666] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает во врага сгусток огня, наносящий |cffffffff100|cffced4da ед. урона и оглушающий цель.|r"
    )
    checks_def.append({"type": "ability", "id": "A1RA", "field": "name", "expected": wts_updates[2856]})
    checks_def.append({"type": "ability", "id": "A1RA", "field": "tip1", "expected": wts_updates[31646]})
    checks_def.append({"type": "ability", "id": "A1RA", "field": "ubertip1", "expected": wts_updates[31666]})

    # A1R6: Духовная Связь
    wts_updates[2436] = "|cffe4cfa3Духовная Связь|r"
    wts_updates[31648] = "|cffe4cfa3Духовная Связь|r"
    wts_updates[42477] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Связывает до |cffffffff6|cffced4da воинов между собой. Половина (|cffffffff50%|cffced4da) получаемого урона распределяется поровну между всеми связанными целями.|r"
    )
    checks_def.append({"type": "ability", "id": "A1R6", "field": "name", "expected": wts_updates[2436]})
    checks_def.append({"type": "ability", "id": "A1R6", "field": "tip1", "expected": wts_updates[31648]})
    checks_def.append({"type": "ability", "id": "A1R6", "field": "ubertip1", "expected": wts_updates[42477]})

    # A1R7: Зачарованный руной Молот
    wts_updates[42478] = "|cffe4cfa3Зачарованный руной Молот|r"
    wts_updates[42479] = "|cffe4cfa3Зачарованный руной Молот|r"
    wts_updates[42727] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Зачаровывает руной оружие мага жидким огнем. При атаке зданий наносит им дополнительно |cffffffff32|cffced4da ед. периодического урона.|r"
    )
    checks_def.append({"type": "ability", "id": "A1R7", "field": "name", "expected": wts_updates[42478]})
    checks_def.append({"type": "ability", "id": "A1R7", "field": "tip1", "expected": wts_updates[42479]})
    checks_def.append({"type": "ability", "id": "A1R7", "field": "ubertip1", "expected": wts_updates[42727]})

    # A1R8: Огненное лассо
    wts_updates[2786] = "|cffe4cfa3Огненное лассо|r"
    wts_updates[31645] = "|cffe4cfa3Огненное лассо|r"
    wts_updates[42728] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывает вражескую цель лассо, лишая её возможности двигаться и атаковать, и наносит |cffffffff30|cffced4da ед. урона/сек.|n|n"
        "Время действия: |cffffffff15|cffced4da сек. (|cffffffff1.5|cffced4da сек. на героях).|r"
    )
    checks_def.append({"type": "ability", "id": "A1R8", "field": "name", "expected": wts_updates[2786]})
    checks_def.append({"type": "ability", "id": "A1R8", "field": "tip1", "expected": wts_updates[31645]})
    checks_def.append({"type": "ability", "id": "A1R8", "field": "ubertip1", "expected": wts_updates[42728]})

    # A17G: Призыв вепря
    wts_updates[28423] = "|cffe4cfa3Призыв вепря|r"
    wts_updates[28331] = "|cffe4cfa3Призыв вепря|r"
    wts_updates[28332] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает свирепого вепря, атакующего врагов иглами по площади.|r"
    )
    checks_def.append({"type": "ability", "id": "A17G", "field": "name", "expected": wts_updates[28423]})
    checks_def.append({"type": "ability", "id": "A17G", "field": "tip1", "expected": wts_updates[28331]})
    checks_def.append({"type": "ability", "id": "A17G", "field": "ubertip1", "expected": wts_updates[28332]})

    # A17H: Щит молний
    wts_updates[28333] = "|cffe4cfa3Щит молний|r"
    wts_updates[42472] = "|cffe4cfa3Щит молний|r"
    wts_updates[42473] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает выбранную цель электрическим щитом, наносящим |cffffffff15|cffced4da ед. урона/сек. находящимся рядом войскам (не наносит урон союзникам).|r"
    )
    checks_def.append({"type": "ability", "id": "A17H", "field": "name", "expected": wts_updates[28333]})
    checks_def.append({"type": "ability", "id": "A17H", "field": "tip1", "expected": wts_updates[42472]})
    checks_def.append({"type": "ability", "id": "A17H", "field": "ubertip1", "expected": wts_updates[42473]})

    # A17I: Цепная молния
    wts_updates[28336] = "|cffe4cfa3Цепная молния|r"
    wts_updates[28337] = "|cffe4cfa3Цепная молния|r"
    wts_updates[41321] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает молнию, наносящую |cffffffff100|cffced4da ед. урона цели и поражающую до |cffffffff4|cffced4da дополнительных целей с убывающим уроном.|r"
    )
    checks_def.append({"type": "ability", "id": "A17I", "field": "name", "expected": wts_updates[28336]})
    checks_def.append({"type": "ability", "id": "A17I", "field": "tip1", "expected": wts_updates[28337]})
    checks_def.append({"type": "ability", "id": "A17I", "field": "ubertip1", "expected": wts_updates[41321]})

    # A17M: Морозный доспех
    wts_updates[28357] = "|cffe4cfa3Морозный доспех|r"
    wts_updates[28358] = "|cffe4cfa3Морозный доспех|r"
    checks_def.append({"type": "ability", "id": "A17M", "field": "name", "expected": wts_updates[28357]})
    checks_def.append({"type": "ability", "id": "A17M", "field": "tip1", "expected": wts_updates[28358]})

    # A17L: Шипастый панцирь
    wts_updates[27440] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[28353] = "|cffe4cfa3Шипастый панцирь|r"
    checks_def.append({"type": "ability", "id": "A17L", "field": "name", "expected": wts_updates[27440]})
    checks_def.append({"type": "ability", "id": "A17L", "field": "tip1", "expected": wts_updates[28353]})

    # A17K: Сокрушение
    wts_updates[28349] = "|cffe4cfa3Сокрушение|r"
    wts_updates[38498] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff40%|cffced4da наносит |cffffffff10|cffced4da ед. дополнительного урона окружающим врагам при атаке.|r"
    )
    checks_def.append({"type": "ability", "id": "A17K", "field": "name", "expected": wts_updates[28349]})
    checks_def.append({"type": "ability", "id": "A17K", "field": "ubertip1", "expected": wts_updates[38498]})

    # A189 & A18A (Hawk auras)
    wts_updates[28969] = "|cffe4cfa3Аура меткости|r"
    wts_updates[28971] = "|cffe4cfa3Аура гениальности|r"
    checks_def.append({"type": "ability", "id": "A189", "field": "name", "expected": wts_updates[28969]})
    checks_def.append({"type": "ability", "id": "A18A", "field": "name", "expected": wts_updates[28971]})

    # Hero N05J Abilities:
    # A16Y: Удар по земле (Thunder Clap)
    wts_updates[27961] = "|cffe4cfa3Удар по земле|r"
    wts_updates[42729] = "|cffe4cfa3Удар по земле|r"
    wts_updates[42730] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощный удар по земле, наносящий урон и оглушающий окружающих врагов.|n|n"
        "Уровень 1: |cffffffff25|cffced4da урона.|n"
        "Уровень 2: |cffffffff50|cffced4da урона.|r"
    )
    wts_updates[27959] = "|cffe4cfa3Удар по земле|r — уровень 2"
    wts_updates[42731] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff25|cffced4da ед. урона окружающим врагам и оглушает их на |cffffffff3|cffced4da сек.|r"
    wts_updates[42683] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff50|cffced4da ед. урона окружающим врагам и оглушает их на |cffffffff3|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A16Y", "field": "name", "expected": wts_updates[27961]})
    checks_def.append({"type": "ability", "id": "A16Y", "field": "researchtip", "expected": wts_updates[42729]})

    # A170: Рывок
    wts_updates[28834] = "|cffe4cfa3Рывок|r"
    wts_updates[28835] = "|cffe4cfa3Рывок|r"
    wts_updates[42618] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стремительный рывок к цели, оглушающий её и наносящий урон.|n|n"
        "Уровень 1: |cffffffff50|cffced4da урона.|n"
        "Уровень 2: |cffffffff100|cffced4da урона.|n"
        "Уровень 3: |cffffffff150|cffced4da урона.|n"
        "Уровень 4: |cffffffff200|cffced4da урона.|r"
    )
    a170_tips = [42622, 42623, 42624, 42616]
    a170_ubs = [42621, 42620, 42619, 42617]
    a170_dmg = [50, 100, 150, 200]
    for lvl in range(1, 5):
        wts_updates[a170_tips[lvl-1]] = f"|cffe4cfa3Рывок|r — уровень {lvl}"
        wts_updates[a170_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стремительно бросается к цели, оглушая её на |cffffffff2|cffced4da сек. и нанося |cffffffff{a170_dmg[lvl-1]}|cffced4da ед. урона.|r"
        )
    checks_def.append({"type": "ability", "id": "A170", "field": "name", "expected": wts_updates[28834]})

    # A175: Стойкость великана
    wts_updates[27994] = "|cffe4cfa3Стойкость великана|r"
    wts_updates[42615] = "|cffe4cfa3Стойкость великана|r"
    wts_updates[42774] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает силу и максимальный запас здоровья героя.|n|n"
        "Уровень 1: |cffc8e087+3|cffced4da к силе, |cffc8e087+100|cffced4da к здоровью.|n"
        "Уровень 2: |cffc8e087+6|cffced4da к силе, |cffc8e087+200|cffced4da к здоровью.|n"
        "Уровень 3: |cffc8e087+9|cffced4da к силе, |cffc8e087+300|cffced4da к здоровью.|n"
        "Уровень 4: |cffc8e087+12|cffced4da к силе, |cffc8e087+400|cffced4da к здоровью.|r"
    )
    a175_tips = [42638, 42639, 42640, 42641]
    a175_ubs = [42778, 42775, 42776, 42777]
    a175_str = [3, 6, 9, 12]
    a175_hp = [100, 200, 300, 400]
    for lvl in range(1, 5):
        wts_updates[a175_tips[lvl-1]] = f"|cffe4cfa3Стойкость великана|r — уровень {lvl}"
        wts_updates[a175_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно дарует |cffc8e087+{a175_str[lvl-1]}|cffced4da к силе и |cffc8e087+{a175_hp[lvl-1]}|cffced4da к максимальному запасу здоровья.|r"
        )
    checks_def.append({"type": "ability", "id": "A175", "field": "name", "expected": wts_updates[27994]})

    # A171: Гнев Гориана
    wts_updates[27980] = "|cffe4cfa3Гнев Гориана|r"
    wts_updates[42611] = "|cffe4cfa3Гнев Гориана|r"
    wts_updates[42734] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Военачальник впадает в безудержный гнев, существенно повышая урон, скорость атаки и получая невосприимчивость к магии на |cffffffff20|cffced4da сек.|r"
    )
    a171_tips = [42738, 42739, 42740, 42732]
    a171_ubs = [42735, 42736, 42737, 42733]
    for lvl in range(1, 5):
        wts_updates[a171_tips[lvl-1]] = f"|cffe4cfa3Гнев Гориана|r — уровень {lvl}"
        wts_updates[a171_ubs[lvl-1]] = (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон на |cffc8e087+50%|cffced4da, скорость атаки на |cffc8e087+50%|cffced4da и дарует невосприимчивость к магии на |cffffffff20|cffced4da сек.|r"
        )
    checks_def.append({"type": "ability", "id": "A171", "field": "name", "expected": wts_updates[27980]})

    # Hero N05K Abilities:
    # A173: Стойкость огра
    wts_updates[42746] = "|cffe4cfa3Стойкость огра|r"
    wts_updates[42749] = "|cffe4cfa3Стойкость огра|r"
    wts_updates[28976] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Чем меньше здоровья у героя, тем выше его скорость атаки, регенерация здоровья и сопротивление магии.|r"
    )
    wts_updates[42747] = "|cffe4cfa3Стойкость огра|r — уровень 1"
    wts_updates[42748] = "|cffe4cfa3Стойкость огра|r — уровень 2"
    wts_updates[27996] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При снижении здоровья герой получает бонус к регенерации, сопротивлению магии и скорости атаки.|r"
    )
    wts_updates[27999] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При снижении здоровья герой получает повышенный бонус к регенерации, сопротивлению магии и скорости атаки.|r"
    )
    checks_def.append({"type": "ability", "id": "A173", "field": "name", "expected": wts_updates[42746]})

    # A172: Сотрясение
    wts_updates[27981] = "|cffe4cfa3Сотрясение|r"
    wts_updates[42741] = "|cffe4cfa3Сотрясение|r"
    wts_updates[27989] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс оглушить врага и нанести дополнительный урон при атаке.|n|n"
        "Уровень 1: |cffffffff10%|cffced4da шанс, |cffffffff40|cffced4da доп. урона.|n"
        "Уровень 2: |cffffffff15%|cffced4da шанс, |cffffffff50|cffced4da доп. урона.|n"
        "Уровень 3: |cffffffff20%|cffced4da шанс, |cffffffff60|cffced4da доп. урона.|n"
        "Уровень 4: |cffffffff25%|cffced4da шанс, |cffffffff70|cffced4da доп. урона.|r"
    )
    a172_tips = [42742, 42743, 42744, 42745]
    a172_ubs = [38721, 38722, 38723, 38720]
    a172_ch = [10, 15, 20, 25]
    a172_dmg = [40, 50, 60, 70]
    for lvl in range(1, 5):
        wts_updates[a172_tips[lvl-1]] = f"|cffe4cfa3Сотрясение|r — уровень {lvl}"
        wts_updates[a172_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff{a172_ch[lvl-1]}%|cffced4da оглушает цель при атаке и наносит |cffffffff{a172_dmg[lvl-1]}|cffced4da ед. дополнительного урона.|r"
        )
    checks_def.append({"type": "ability", "id": "A172", "field": "name", "expected": wts_updates[27981]})

    # A174: Ударная волна (Вождь)
    wts_updates[28830] = "|cffe4cfa3Ударная волна|r"
    wts_updates[28979] = "|cffe4cfa3Ударная волна|r"
    wts_updates[42759] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сокрушительную волну энергии, наносящую урон врагам по прямой линии.|n|n"
        "Уровень 1: |cffffffff75|cffced4da урона.|n"
        "Уровень 2: |cffffffff125|cffced4da урона.|n"
        "Уровень 3: |cffffffff200|cffced4da урона.|n"
        "Уровень 4: |cffffffff275|cffced4da урона.|r"
    )
    a174_tips = [28981, 28982, 28983, 28977]
    a174_ubs = [42760, 42761, 42762, 42758]
    a174_dmg = [75, 125, 200, 275]
    for lvl in range(1, 5):
        wts_updates[a174_tips[lvl-1]] = f"|cffe4cfa3Ударная волна|r — уровень {lvl}"
        wts_updates[a174_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну энергии, наносящую |cffffffff{a174_dmg[lvl-1]}|cffced4da ед. урона всем врагам на своём пути.|r"
        )
    checks_def.append({"type": "ability", "id": "A174", "field": "name", "expected": wts_updates[28830]})

    # Hero N05L Abilities:
    # A16V: Волна исцеления
    wts_updates[27948] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[42679] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[42599] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создает волну энергии, восстанавливающую здоровье союзников с убывающей силой при каждом переходе.|n|n"
        "Уровень 1: |cffc8e087130|cffced4da здоровья, до |cffffffff4|cffced4da целей.|n"
        "Уровень 2: |cffc8e087215|cffced4da здоровья, до |cffffffff5|cffced4da целей.|n"
        "Уровень 3: |cffc8e087300|cffced4da здоровья, до |cffffffff6|cffced4da целей.|n"
        "Уровень 4: |cffc8e087385|cffced4da здоровья, до |cffffffff7|cffced4da целей.|r"
    )
    a16v_tips = [42680, 42681, 42682, 42481]
    a16v_ubs = [27945, 27946, 27947, 27943]
    a16v_hp = [130, 215, 300, 385]
    a16v_targs = [4, 5, 6, 7]
    for lvl in range(1, 5):
        wts_updates[a16v_tips[lvl-1]] = f"|cffe4cfa3Волна исцеления|r — уровень {lvl}"
        wts_updates[a16v_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087{a16v_hp[lvl-1]}|cffced4da ед. здоровья цели и переходит на ближайших союзников (до |cffffffff{a16v_targs[lvl-1]}|cffced4da целей).|r"
        )
    checks_def.append({"type": "ability", "id": "A16V", "field": "name", "expected": wts_updates[27948]})

    # A16U: Разведка
    wts_updates[28966] = "|cffe4cfa3Разведка|r"
    wts_updates[42625] = "|cffe4cfa3Разведка|r"
    wts_updates[42634] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает зорких ястребов-разведчиков, наделенных аурами и обнаруживающих невидимых бойцов.|n|n"
        "Уровень 1: |cffffffff1|cffced4da ястреб на |cffffffff30|cffced4da сек.|n"
        "Уровень 2: |cffffffff2|cffced4da ястреба на |cffffffff60|cffced4da сек.|n"
        "Уровень 3: |cffffffff3|cffced4da ястреба на |cffffffff80|cffced4da сек.|n"
        "Уровень 4: |cffffffff4|cffced4da ястреба на |cffffffff100|cffced4da сек.|r"
    )
    a16u_tips = [42626, 42627, 42628, 42629]
    a16u_ubs = [42630, 42631, 42632, 42633]
    a16u_dur = [30, 60, 80, 100]
    for lvl in range(1, 5):
        wts_updates[a16u_tips[lvl-1]] = f"|cffe4cfa3Разведка|r — уровень {lvl}"
        wts_updates[a16u_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает ястребов-разведчиков с аурами и истинным зрением на |cffffffff{a16u_dur[lvl-1]}|cffced4da сек.|r"
        )
    checks_def.append({"type": "ability", "id": "A16U", "field": "name", "expected": wts_updates[28966]})

    # A16X: Кислотная бомба
    wts_updates[42752] = "|cffe4cfa3Кислотная бомба|r"
    wts_updates[42753] = "|cffe4cfa3Кислотная бомба|r"
    wts_updates[42751] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает сосуд с кислотой, разъедающий броню и наносящий периодический урон цели и соседним врагам.|n|n"
        "Уровень 1: до |cffffffff20|cffced4da урона/сек., |cffe69a8d-4|cffced4da к броне.|n"
        "Уровень 2: до |cffffffff40|cffced4da урона/сек., |cffe69a8d-8|cffced4da к броне.|r"
    )
    wts_updates[42756] = "|cffe4cfa3Кислотная бомба|r — уровень 1"
    wts_updates[42754] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Разъедает броню цели на |cffe69a8d-4|cffced4da ед. и наносит до |cffffffff20|cffced4da ед. урона/сек.|r"
    wts_updates[42757] = "|cffe4cfa3Кислотная бомба|r — уровень 2"
    wts_updates[42755] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Разъедает броню цели на |cffe69a8d-8|cffced4da ед. и наносит до |cffffffff40|cffced4da ед. урона/сек.|r"
    checks_def.append({"type": "ability", "id": "A16X", "field": "name", "expected": wts_updates[42752]})

    # A16W: Похищение жизни
    wts_updates[27954] = "|cffe4cfa3Похищение жизни|r"
    wts_updates[27955] = "|cffe4cfa3Похищение жизни|r"
    wts_updates[42602] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает здоровье у врага и передает его Знахарю в течение |cffffffff8|cffced4da сек.|n|n"
        "Уровень 1: |cffc8e08750|cffced4da здоровья/сек.|n"
        "Уровень 2: |cffc8e08770|cffced4da здоровья/сек.|n"
        "Уровень 3: |cffc8e08790|cffced4da здоровья/сек.|n"
        "Уровень 4: |cffc8e087110|cffced4da здоровья/сек.|r"
    )
    wts_updates[27952] = "|cffe4cfa3Похищение жизни|r — уровень 4"
    wts_updates[42603] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Похищает у цели |cffc8e08750|cffced4da ед. здоровья/сек. в течение |cffffffff8|cffced4da сек.|r"
    wts_updates[42604] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Похищает у цели |cffc8e08770|cffced4da ед. здоровья/сек. в течение |cffffffff8|cffced4da сек.|r"
    wts_updates[42605] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Похищает у цели |cffc8e08790|cffced4da ед. здоровья/сек. в течение |cffffffff8|cffced4da сек.|r"
    wts_updates[42601] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Похищает у цели |cffc8e087110|cffced4da ед. здоровья/сек. в течение |cffffffff8|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A16W", "field": "name", "expected": wts_updates[27954]})

    # Hero N05O Abilities:
    # A18U: Броски камней
    wts_updates[26483] = "|cffe4cfa3Броски камней|r"
    wts_updates[26541] = "|cffe4cfa3Броски камней|r"
    wts_updates[29595] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область валунами, нанося урон врагам и оглушая их.|r"
    )
    wts_updates[29592] = "|cffe4cfa3Броски камней|r — уровень 1"
    wts_updates[29593] = "|cffe4cfa3Броски камней|r — уровень 2"
    checks_def.append({"type": "ability", "id": "A18U", "field": "name", "expected": wts_updates[26483]})

    # A18Q: Провокация
    wts_updates[26569] = "|cffe4cfa3Провокация|r"
    wts_updates[26570] = "|cffe4cfa3Провокация|r — уровень 1"
    wts_updates[26585] = "|cffe4cfa3Провокация|r — уровень 2"
    wts_updates[26602] = "|cffe4cfa3Провокация|r — уровень 3"
    wts_updates[26622] = "|cffe4cfa3Провокация|r — уровень 4"
    wts_updates[26687] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заставляет ближайших врагов атаковать исполина.|r"
    wts_updates[27301] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заставляет ближайших врагов атаковать исполина.|r"
    wts_updates[27302] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заставляет ближайших врагов атаковать исполина.|r"
    checks_def.append({"type": "ability", "id": "A18Q", "field": "name", "expected": wts_updates[26569]})

    # A18R: Удар по земле (Груул)
    wts_updates[23525] = "|cffe4cfa3Удар по земле|r"
    wts_updates[25160] = "|cffe4cfa3Удар по земле|r"
    wts_updates[42764] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Груул бьет по земле, вызывая раскол, наносящий урон и замедляющий атаку и скорость врагов на |cffe69a8d50%|cffced4da.|n|n"
        "Уровень 1: |cffffffff120|cffced4da урона.|n"
        "Уровень 2: |cffffffff180|cffced4da урона.|n"
        "Уровень 3: |cffffffff220|cffced4da урона.|n"
        "Уровень 4: |cffffffff270|cffced4da урона.|r"
    )
    a18r_tips = [29544, 29545, 29546, 29539]
    a18r_ubs = [42765, 42766, 42767, 42763]
    a18r_dmg = [120, 180, 220, 270]
    for lvl in range(1, 5):
        wts_updates[a18r_tips[lvl-1]] = f"|cffe4cfa3Удар по земле|r — уровень {lvl}"
        wts_updates[a18r_ubs[lvl-1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сотрясает землю вокруг, нанося |cffffffff{a18r_dmg[lvl-1]}|cffced4da ед. урона и снижая скорость передвижения и атаки врагов на |cffe69a8d50%|cffced4da.|r"
        )
    checks_def.append({"type": "ability", "id": "A18R", "field": "name", "expected": wts_updates[23525]})

    # A18S: Каменная кожа
    wts_updates[26482] = "|cffe4cfa3Каменная кожа|r"
    wts_updates[25645] = "|cffe4cfa3Каменная кожа|r"
    wts_updates[19589] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает урон от атак врагов и ускоряет восстановление здоровья.|r"
    )
    wts_updates[29572] = "|cffe4cfa3Каменная кожа|r — уровень 2"
    wts_updates[29573] = "|cffe4cfa3Каменная кожа|r — уровень 3"
    wts_updates[29574] = "|cffe4cfa3Каменная кожа|r — уровень 4"
    wts_updates[29575] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает получаемый урон от атак врагов и ускоряет регенерацию здоровья.|r"
    wts_updates[29569] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает получаемый урон от атак врагов и ускоряет регенерацию здоровья.|r"
    wts_updates[29570] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает получаемый урон от атак врагов и ускоряет регенерацию здоровья.|r"
    wts_updates[29571] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает получаемый урон от атак врагов и ускоряет регенерацию здоровья.|r"
    checks_def.append({"type": "ability", "id": "A18S", "field": "name", "expected": wts_updates[26482]})

    # A1LF: Шипастый панцирь
    wts_updates[28354] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[30840] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[10391] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает тело шипами, дающими бонус к броне и отражающими урон в атакующих врагов.|r"
    )
    checks_def.append({"type": "ability", "id": "A1LF", "field": "name", "expected": wts_updates[28354]})

    # =========================================================================
    # 7. BUFFS (B083, B097, B098)
    # =========================================================================
    # B083: Аура защиты
    wts_updates[9532] = "|cffe4cfa3Аура Защиты|r"
    wts_updates[9533] = "|cffa6afb8ЭФФЕКТ:|cffced4da Броня этого воина |cffc8e087повышена|cffced4da под действием ауры командира.|r"
    checks_def.append({"type": "buff", "id": "B083", "field": "bufftip", "expected": wts_updates[9532]})
    checks_def.append({"type": "buff", "id": "B083", "field": "buffubertip", "expected": wts_updates[9533]})

    # B097: Деморализующий звук
    wts_updates[42482] = "|cffe4cfa3Деморализующий звук|r"
    wts_updates[42484] = "|cffa6afb8ЭФФЕКТ:|cffced4da Наносимый урон |cffe69a8dснижен|cffced4da под действием устрашающего боя барабанов.|r"
    checks_def.append({"type": "buff", "id": "B097", "field": "bufftip", "expected": wts_updates[42482]})
    checks_def.append({"type": "buff", "id": "B097", "field": "buffubertip", "expected": wts_updates[42484]})

    # B098: Аура силы
    wts_updates[42654] = "|cffe4cfa3Аура силы|r"
    wts_updates[42656] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость восстановления здоровья этого воина |cffc8e087повышена|cffced4da.|r"
    checks_def.append({"type": "buff", "id": "B098", "field": "bufftip", "expected": wts_updates[42654]})
    checks_def.append({"type": "buff", "id": "B098", "field": "buffubertip", "expected": wts_updates[42656]})

    # Save plan
    plan_data = {
        "race": "Ogres",
        "race_id": 28,
        "selection_ability": "A17N",
        "wts_updates": {str(k): v for k, v in wts_updates.items()},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A17N", "R0HT"],
            "buildings": [
                "o035", "o03D", "o03E", "o036", "o037", "o038",
                "o03A", "o039", "o03J", "o03C", "o03B"
            ],
            "units": [
                "o03W", "o03I", "o03H", "o03G", "o03F", "o03K", "o03L", "o03M",
                "o03N", "o03O", "o03P", "o03Q", "o03R", "o03S", "o03T", "o03U", "o03V",
                "n05M", "n05N"
            ],
            "heroes": ["N05J", "N05K", "N05L", "N05O"],
            "upgrades": [
                "R0HT", "R0GL", "R0GM", "R0GN", "R0GO", "R0GP", "R0GQ",
                "R09W", "R0GU", "R0L2", "R0GR", "R0GS", "R0GT",
                "R0GF", "R0GG", "R0GH", "R0GI", "R0GJ", "R0GK"
            ],
            "abilities": [
                "A17N", "A176", "A177", "A178", "A179", "A17A", "A17B", "A17O", "A0WU",
                "A17D", "A17E", "A17C", "A17F", "A1RA", "A1R6", "A1R7", "A1R8", "A17G",
                "A17H", "A17I", "A17M", "A17L", "A17K", "A189", "A18A",
                "A16Y", "A170", "A175", "A171", "A173", "A172", "A174",
                "A16V", "A16U", "A16X", "A16W",
                "A18U", "A18Q", "A18R", "A18S", "A1LF"
            ],
            "buffs": ["B083", "B097", "B098"]
        }
    }

    plan_path = folder / "ogres_plan.json"
    plan_path.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote plan to {plan_path} with {len(wts_updates)} strings and {len(checks_def)} checks.")

    # =========================================================================
    # GENERATE CATEGORY REGISTRIES IN docs/ui_text/
    # =========================================================================
    raw_dump = json.loads((ROOT / "scripts/ogres_raw_dump.json").read_text(encoding="utf-8"))

    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    # 1. ogres_selection.json
    sel_data = {
        "scope": "Огры (Ogres): подсказка выбора расы A17N и маркер фракции R0HT",
        "object": "A17N",
        "variants": ["SD"],
        "hotkey": {"value": "S"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Ogres регистрирует способность A17N.",
            "При выборе создаются 5 рабочих o03W, исследуется маркер R0HT, удаляется выбирающий юнит.",
            "Горячая клавиша S, создатель NiCAmCHiK, куратор NiCAmCHiK, сложность 1/5 (●○○○○), период «Burning Crusade — Legion»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38905, "after": wts_updates[38905]},
            {"field": "tip1", "wts_id": 38906, "after": wts_updates[38906]},
            {"field": "ubertip1", "wts_id": 25688, "after": wts_updates[25688]}
        ],
        "markers": [
            {
                "id": "R0HT",
                "name": "Огры (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 29642, "after": wts_updates[29642]},
                    {"field": "tip1", "wts_id": 29643, "after": wts_updates[29643]},
                    {"field": "ubertip1", "wts_id": 38930, "after": wts_updates[38930]}
                ]
            }
        ]
    }
    (folder / "ogres_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote ogres_selection.json")

    # 2. ogres_buildings.json
    bld_entries = []
    for b in raw_dump["buildings"]:
        b_id = b["id"]
        if b_id not in plan_data["categories"]["buildings"]:
            continue
        hk_val = b.get("hotkey")
        entry = {"id": b_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(b.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        bld_entries.append(entry)

    bld_data = {
        "scope": f"Огры (Ogres): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "ogres_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote ogres_buildings.json ({len(bld_entries)} buildings)")

    # 3. ogres_units.json
    unit_entries = []
    for u in raw_dump["units"]:
        u_id = u["id"]
        if u_id not in plan_data["categories"]["units"]:
            continue
        hk_val = u.get("hotkey")
        entry = {"id": u_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(u.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        unit_entries.append(entry)

    unit_data = {
        "scope": f"Огры (Ogres): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "ogres_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote ogres_units.json ({len(unit_entries)} units)")

    # 4. ogres_heroes.json
    hero_entries = []
    for h in raw_dump["heroes"]:
        h_id = h["id"]
        if h_id not in plan_data["categories"]["heroes"]:
            continue
        hk_val = h.get("hotkey")
        entry = {"id": h_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(h.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        hero_entries.append(entry)

    hero_data = {
        "scope": f"Огры (Ogres): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "ogres_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote ogres_heroes.json ({len(hero_entries)} heroes)")

    # 5. ogres_abilities.json
    abil_entries = []
    for a in raw_dump["abilities"]:
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
        "scope": f"Огры (Ogres): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "ogres_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote ogres_abilities.json ({len(abil_entries)} abilities)")

    # 6. ogres_research.json
    upg_entries = []
    for u in raw_dump["upgrades"]:
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
        "scope": f"Огры (Ogres): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "ogres_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote ogres_research.json ({len(upg_entries)} upgrades)")

    # 7. ogres_audit.json
    audit_data = {
        "race": "Огры (Ogres)",
        "race_id": 28,
        "selection_ability": "A17N",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "town_halls": {
                    "tier1": {"id": "o035", "name": "Дом огров", "food": 50},
                    "tier2": {"id": "o03D", "name": "Крепость огров", "food": 100},
                    "tier3": {"id": "o03E", "name": "Цитадель огров", "food": 150}
                }
            },
            "units": {
                "count": len(unit_entries),
                "ids": [u["id"] for u in unit_entries]
            },
            "heroes": {
                "count": len(hero_entries),
                "ids": [h["id"] for h in hero_entries],
                "names": {
                    "N05J": "Военачальник Огров (Сила, ближний бой)",
                    "N05K": "Вождь Огров (Сила, ближний бой)",
                    "N05L": "Знахарь Огров (Интеллект, дальний бой)",
                    "N05O": "Последний Гронн (Груул — Легендарный герой, Сила, ближний бой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(wts_updates)
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0HT": "Маркер расы Огры"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items found in war3map.w3t for Ogres."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific triggers/chat messages found for Ogres."
        },
        "buffs_audit": {
            "custom_buffs": ["B083", "B097", "B098"],
            "standard_buffs_used": ["BUfa", "BUts", "Bspl", "Bliq", "Bblo", "Bfzy", "Blsh", "B05G"],
            "status": "Standardized custom buffs with secondary color labels and clean descriptions."
        },
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def)
    }
    (folder / "ogres_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote ogres_audit.json")

if __name__ == "__main__":
    main()
