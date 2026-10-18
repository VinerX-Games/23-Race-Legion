# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Illidari race (Race 10)."""
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
    # 1. RACE SELECTION: A0OK
    # =========================================================================
    wts_updates[38887] = "|cffe4cfa3Иллидари|r"
    wts_updates[38888] = "|cffe4cfa3Иллидари|r (|cffffffffC|r)"
    wts_updates[35180] = (
        "|cffa6afb8РАСА:|cffced4da Элитная армия охотников на демонов, наг и эльфов крови под предводительством Иллидана Ярости Бури.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Легион»|r|n|n"
        "|cffced4daИллидари — войско, собранное и обученное Иллиданом Яростью Бури в Запределье для беспощадной войны против Пылающего Легиона. "
        "Объединив под своими знамёнами первых охотников на демонов, глубинных наг леди Вайш, эльфов крови и орков Скверны, Иллидан обратил оружие демонов против них самих. "
        "Воины Иллидари готовы пойти на любые жертвы и подчинить опаснейшие тёмные искусства, чтобы уничтожить демонических владык раз и навсегда.|r"
    )

    checks_def.append({"type": "ability", "id": "A0OK", "field": "name", "expected": wts_updates[38887]})
    checks_def.append({"type": "ability", "id": "A0OK", "field": "tip1", "expected": wts_updates[38888]})
    checks_def.append({"type": "ability", "id": "A0OK", "field": "ubertip1", "expected": wts_updates[35180]})

    # =========================================================================
    # 2. BUILDINGS: 13 buildings
    # =========================================================================
    # h0E9: Аванпост (Q)
    wts_updates[14055] = "|cffe4cfa3Аванпост|r"
    wts_updates[14056] = "|cffe4cfa3Аванпост|r (|cffffffffQ|r)"
    wts_updates[5699] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Иллидари первой ступени. Обучает строителей и служит складом древесины.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deТренировки Охотников|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКомандный центр|cffced4da: открывает доступ к передовым сооружениям и войскам Иллидари.|r"
    )
    checks_def.append({"type": "unit", "id": "h0E9", "field": "name", "expected": wts_updates[14055]})
    checks_def.append({"type": "unit", "id": "h0E9", "field": "tip", "expected": wts_updates[14056]})
    checks_def.append({"type": "unit", "id": "h0E9", "field": "ubertip", "expected": wts_updates[5699]})

    # h0EA: Командный центр (Z)
    wts_updates[2702] = "|cffe4cfa3Командный центр|r"
    wts_updates[14059] = "|cffe4cfa3Командный центр|r (|cffffffffZ|r)"
    wts_updates[14060] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Иллидари второй ступени. Открывает доступ к Храму магии и Нерестилищу, а также позволяет выбрать специализацию армии.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deТренировки Охотников|cffced4da|n- |cffa9c7deПриоритет Наги|cffced4da|n- |cffa9c7deПриоритет Эльфы|cffced4da|n- |cffa9c7deПриоритет Орки|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deШтаб|cffced4da: открывает доступ к Храму охоты и высшим технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EA", "field": "name", "expected": wts_updates[2702]})
    checks_def.append({"type": "unit", "id": "h0EA", "field": "tip", "expected": wts_updates[14059]})
    checks_def.append({"type": "unit", "id": "h0EA", "field": "ubertip", "expected": wts_updates[14060]})

    # h0EB: Штаб (Z)
    wts_updates[14062] = "|cffe4cfa3Штаб|r"
    wts_updates[14063] = "|cffe4cfa3Штаб|r (|cffffffffZ|r)"
    wts_updates[14064] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Иллидари третьей ступени. Открывает доступ к Храму охоты, элитным охотникам на демонов и высшим ступеням улучшений.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deТренировки Охотников|cffced4da|n- |cffa9c7deПриоритет Наги|cffced4da|n- |cffa9c7deПриоритет Эльфы|cffced4da|n- |cffa9c7deПриоритет Орки|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EB", "field": "name", "expected": wts_updates[14062]})
    checks_def.append({"type": "unit", "id": "h0EB", "field": "tip", "expected": wts_updates[14063]})
    checks_def.append({"type": "unit", "id": "h0EB", "field": "ubertip", "expected": wts_updates[14064]})

    # h0EC: Накопитель энергии (A)
    wts_updates[14066] = "|cffe4cfa3Накопитель энергии|r"
    wts_updates[14067] = "|cffe4cfa3Накопитель энергии|r (|cffffffffA|r)"
    wts_updates[42689] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Иллидари запасом пищи и вырабатывает регулярный доход.|n|n"
        "Даёт |cffffffff15|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+40|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EC", "field": "name", "expected": wts_updates[14066]})
    checks_def.append({"type": "unit", "id": "h0EC", "field": "tip", "expected": wts_updates[14067]})
    checks_def.append({"type": "unit", "id": "h0EC", "field": "ubertip", "expected": wts_updates[42689]})

    # h0ED: Алтарь охоты (S)
    wts_updates[14070] = "|cffe4cfa3Алтарь охоты|r"
    wts_updates[14071] = "|cffe4cfa3Алтарь охоты|r (|cffffffffS|r)"
    wts_updates[12976] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Призывает и воскрешает павших героев Иллидари.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deМаг Крови|cffced4da: герой дальнего боя, повелевающий пламенем и контролем маны.|n"
        "- |cffa9c7deОхотник на демонов|cffced4da: ловкий боец ближнего боя, сжигающий ману и способный принимать форму демона.|n"
        "- |cffa9c7deОхотник «Истребление»|cffced4da: стремительный воин с рывком Скверны, критическими ударами и яростью боя.|n"
        "- |cffa9c7deОхотник «Месть»|cffced4da: стойкий защитник, поглощающий здоровье врагов пламенем и возвращающий урон.|r"
    )
    checks_def.append({"type": "unit", "id": "h0ED", "field": "name", "expected": wts_updates[14070]})
    checks_def.append({"type": "unit", "id": "h0ED", "field": "tip", "expected": wts_updates[14071]})
    checks_def.append({"type": "unit", "id": "h0ED", "field": "ubertip", "expected": wts_updates[12976]})

    # h0EE: Казармы (W)
    wts_updates[15182] = "|cffe4cfa3Казармы|r"
    wts_updates[15183] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[13130] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военное сооружение для подготовки базовой пехоты, кавалерии и осадных орудий Иллидари.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСтранник|cffced4da: пехотинец ближнего боя с защитным щитом.|n"
        "- |cffa9c7deРубака|cffced4da: сильный орк-воин ближнего боя.|n"
        "- |cffa9c7deСумеречный налётчик|cffced4da: быстрый кавалерист на волке для стремительных атак.|n"
        "- |cffa9c7deРазрушитель|cffced4da: дальнобойная осадная машина против укреплений.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da|n- |cffa9c7deГрубая сила|cffced4da|n- |cffa9c7deЯростный рывок|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EE", "field": "name", "expected": wts_updates[15182]})
    checks_def.append({"type": "unit", "id": "h0EE", "field": "tip", "expected": wts_updates[15183]})
    checks_def.append({"type": "unit", "id": "h0EE", "field": "ubertip", "expected": wts_updates[13130]})

    # h0EF: Храм магии (F)
    wts_updates[14078] = "|cffe4cfa3Храм магии|r"
    wts_updates[14079] = "|cffe4cfa3Храм магии|r (|cffffffffF|r)"
    wts_updates[14080] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Магическое святилище для подготовки заклинателей огня и Скверны.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМагистр|cffced4da: чародей огня с огненным доспехом и огненными стрелами.|n"
        "- |cffa9c7deЧернокнижник|cffced4da: тёмный маг с рассеиванием чар и стрелами Скверны.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПосвящение магистров|cffced4da|n- |cffa9c7deПосвящение чернокнижников|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EF", "field": "name", "expected": wts_updates[14078]})
    checks_def.append({"type": "unit", "id": "h0EF", "field": "tip", "expected": wts_updates[14079]})
    checks_def.append({"type": "unit", "id": "h0EF", "field": "ubertip", "expected": wts_updates[14080]})

    # h0EG: Нерестилище (D)
    wts_updates[14082] = "|cffe4cfa3Нерестилище|r"
    wts_updates[14083] = "|cffe4cfa3Нерестилище|r (|cffffffffD|r)"
    wts_updates[5700] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель глубинных наг, сражающихся на стороне Иллидари.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМорской варан|cffced4da: стрелок дальнего боя с ядовитыми атаками.|n"
        "- |cffa9c7deМирмидон|cffced4da: могучий воин ближнего боя со способностью опутывания.|n"
        "- |cffa9c7deСирена|cffced4da: нага-колдунья с заклинаниями смерча, режущей воды и паразита.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМутация Наг|cffced4da|n- |cffa9c7deОпутывание|cffced4da|n- |cffa9c7deМагия воды|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EG", "field": "name", "expected": wts_updates[14082]})
    checks_def.append({"type": "unit", "id": "h0EG", "field": "tip", "expected": wts_updates[14083]})
    checks_def.append({"type": "unit", "id": "h0EG", "field": "ubertip", "expected": wts_updates[5700]})

    # h0EH: Лесопилка (E)
    wts_updates[15184] = "|cffe4cfa3Лесопилка|r"
    wts_updates[15185] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[3159] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Пункт приёма древесины и улучшения топоров строителей.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенные топоры|cffced4da: увеличивает объём переносимой работниками древесины.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EH", "field": "name", "expected": wts_updates[15184]})
    checks_def.append({"type": "unit", "id": "h0EH", "field": "tip", "expected": wts_updates[15185]})
    checks_def.append({"type": "unit", "id": "h0EH", "field": "ubertip", "expected": wts_updates[3159]})

    # h0EM: Кузница (R)
    wts_updates[14798] = "|cffe4cfa3Кузница|r"
    wts_updates[14799] = "|cffe4cfa3Кузница|r (|cffffffffR|r)"
    wts_updates[12968] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр разработки вооружения и брони для всех родов войск Иллидари.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПроклятое оружие|cffced4da: урон солдат ближнего боя.|n"
        "- |cffa9c7deОсквернённые доспехи|cffced4da: защита солдат ближнего боя.|n"
        "- |cffa9c7deОружие Скверны|cffced4da: урон стрелков и осадных орудий.|n"
        "- |cffa9c7deУкрепление Скверной|cffced4da: защита стрелков и заклинателей.|n"
        "- |cffa9c7deВладение магией|cffced4da: урон магов и заклинателей.|r"
    )
    checks_def.append({"type": "unit", "id": "h0EM", "field": "name", "expected": wts_updates[14798]})
    checks_def.append({"type": "unit", "id": "h0EM", "field": "tip", "expected": wts_updates[14799]})
    checks_def.append({"type": "unit", "id": "h0EM", "field": "ubertip", "expected": wts_updates[12968]})

    # h0EN: Магическая башня (X)
    wts_updates[14758] = "|cffe4cfa3Магическая башня|r"
    wts_updates[14759] = "|cffe4cfa3Магическая башня|r (|cffffffffX|r)"
    wts_updates[31765] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительная башня Иллидари, атаки которой сжигают ману противников и наносят эквивалентный урон.|n|n"
        "Атакует наземные и воздушные цели (дальний бой, магический урон).|r"
    )
    checks_def.append({"type": "unit", "id": "h0EN", "field": "name", "expected": wts_updates[14758]})
    checks_def.append({"type": "unit", "id": "h0EN", "field": "tip", "expected": wts_updates[14759]})
    checks_def.append({"type": "unit", "id": "h0EN", "field": "ubertip", "expected": wts_updates[31765]})

    # o01C: Храм охоты (Z)
    wts_updates[14374] = "|cffe4cfa3Храм охоты|r"
    wts_updates[14375] = "|cffe4cfa3Храм охоты|r (|cffffffffZ|r)"
    wts_updates[18691] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель элитных воинов Иллидари: покоренных демонов и обученных охотников на демонов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПокоренный демон|cffced4da: мощный верховой демон с яростью и рассекающими клинками.|n"
        "- |cffa9c7deОхотник «Истребление»|cffced4da: элитный пехотинец с аурой истребления и поглощением осколков.|n"
        "- |cffa9c7deОхотник «Месть»|cffced4da: элитный пехотинец с защитой от атак и противодействием магии.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deВладение Скверной|cffced4da: открывает способности покоренных демонов.|r"
    )
    checks_def.append({"type": "unit", "id": "o01C", "field": "name", "expected": wts_updates[14374]})
    checks_def.append({"type": "unit", "id": "o01C", "field": "tip", "expected": wts_updates[14375]})
    checks_def.append({"type": "unit", "id": "o01C", "field": "ubertip", "expected": wts_updates[18691]})

    # h011: Верфь (C)
    wts_updates[368] = "|cffe4cfa3Верфь|r"
    wts_updates[369] = "|cffe4cfa3Верфь|r (|cffffffffC|r)"
    wts_updates[370] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Строит боевые корабли и исследует улучшения флота.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТранспорт|cffced4da|n- |cffa9c7deФрегат|cffced4da|n- |cffa9c7deЛинкор|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбстрел|cffced4da|n- |cffa9c7deДополнительные паруса|cffced4da|n- |cffa9c7deПочинка|cffced4da|n- |cffa9c7deОрудия флота|cffced4da|n- |cffa9c7deУкреплённый корпус|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h011", "field": "name", "expected": wts_updates[368]})
    checks_def.append({"type": "unit", "id": "h011", "field": "tip", "expected": wts_updates[369]})
    checks_def.append({"type": "unit", "id": "h011", "field": "ubertip", "expected": wts_updates[370]})

    # =========================================================================
    # 3. UNITS: 13 units
    # =========================================================================
    # h0EI: Строитель (Q)
    wts_updates[14346] = "|cffe4cfa3Строитель|r"
    wts_updates[14348] = "|cffe4cfa3Строитель|r (|cffffffffQ|r)"
    wts_updates[20571] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Иллидари. Возводит и ремонтирует здания, а также добывает древесину.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСкачок|cffced4da: мгновенно перемещается на короткую дистанцию.|n"
        "- |cffa9c7deДобыча древесины|cffced4da: собирает древесину в лесу.|n"
        "- |cffa9c7deРемонт|cffced4da: восстанавливает прочность повреждённых построек.|n|n"
        "Атакует наземные цели (ближний бой).|r"
    )
    checks_def.append({"type": "unit", "id": "h0EI", "field": "name", "expected": wts_updates[14346]})
    checks_def.append({"type": "unit", "id": "h0EI", "field": "tip", "expected": wts_updates[14348]})
    checks_def.append({"type": "unit", "id": "h0EI", "field": "ubertip", "expected": wts_updates[20571]})

    # h0EJ: Странник (Q)
    wts_updates[14354] = "|cffe4cfa3Странник|r"
    wts_updates[14355] = "|cffe4cfa3Странник|r (|cffffffffQ|r)"
    wts_updates[35864] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец эльфов крови на службе Иллидари. Надёжный воин передовой линии.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЛовкость иллидари|cffced4da: даёт шанс уклониться от вражеской атаки.|n"
        "- |cffa9c7deПоглощение силы|cffced4da: атаки восстанавливают здоровье при изучении «Тренировок Охотников».|n"
        "- |cffa9c7deЗащита|cffced4da: укрывается за щитом, снижая урон от дальних атак (требуется исследование).|n|n"
        "Атакует наземные цели (ближний бой, обычный урон).|r"
    )
    checks_def.append({"type": "unit", "id": "h0EJ", "field": "name", "expected": wts_updates[14354]})
    checks_def.append({"type": "unit", "id": "h0EJ", "field": "tip", "expected": wts_updates[14355]})
    checks_def.append({"type": "unit", "id": "h0EJ", "field": "ubertip", "expected": wts_updates[35864]})

    # o01A: Рубака (W)
    wts_updates[14357] = "|cffe4cfa3Рубака|r"
    wts_updates[14358] = "|cffe4cfa3Рубака|r (|cffffffffW|r)"
    wts_updates[35865] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый пехотинец орков Скверны с высоким запасом здоровья и мощным ударом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЛовкость иллидари|cffced4da: даёт шанс уклониться от вражеской атаки.|n"
        "- |cffa9c7deПоглощение силы|cffced4da: атаки восстанавливают здоровье при изучении «Тренировок Охотников».|n"
        "- |cffa9c7deГрубая сила|cffced4da: значительно увеличивает запас здоровья и урон (требуется исследование).|n|n"
        "Атакует наземные цели (ближний бой, обычный урон).|r"
    )
    checks_def.append({"type": "unit", "id": "o01A", "field": "name", "expected": wts_updates[14357]})
    checks_def.append({"type": "unit", "id": "o01A", "field": "tip", "expected": wts_updates[14358]})
    checks_def.append({"type": "unit", "id": "o01A", "field": "ubertip", "expected": wts_updates[35865]})

    # o01B: Сумеречный налетчик (E)
    wts_updates[14361] = "|cffe4cfa3Сумеречный налётчик|r"
    wts_updates[14362] = "|cffe4cfa3Сумеречный налётчик|r (|cffffffffE|r)"
    wts_updates[35866] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый кавалерист на волке, предназначенный для стремительных рейдов и тыловых ударов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЛовкость иллидари|cffced4da: даёт шанс уклониться от вражеской атаки.|n"
        "- |cffa9c7deПоглощение силы|cffced4da: атаки восстанавливают здоровье при изучении «Тренировок Охотников».|n"
        "- |cffa9c7deЯростный рывок|cffced4da: резко повышает скорость передвижения ценой урона (требуется исследование).|n|n"
        "Атакует наземные цели (ближний бой, урон хаоса).|r"
    )
    checks_def.append({"type": "unit", "id": "o01B", "field": "name", "expected": wts_updates[14361]})
    checks_def.append({"type": "unit", "id": "o01B", "field": "tip", "expected": wts_updates[14362]})
    checks_def.append({"type": "unit", "id": "o01B", "field": "ubertip", "expected": wts_updates[35866]})

    # o019: Разрушитель (R)
    wts_updates[14351] = "|cffe4cfa3Разрушитель|r"
    wts_updates[14352] = "|cffe4cfa3Разрушитель|r (|cffffffffR|r)"
    wts_updates[35863] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлая осадная машина дальнего боя, сокрушающая вражеские укрепления и плотные скопления войск.|n|n"
        "Атакует наземные цели и здания (дальний бой, осадный урон).|r"
    )
    checks_def.append({"type": "unit", "id": "o019", "field": "name", "expected": wts_updates[14351]})
    checks_def.append({"type": "unit", "id": "o019", "field": "tip", "expected": wts_updates[14352]})
    checks_def.append({"type": "unit", "id": "o019", "field": "ubertip", "expected": wts_updates[35863]})

    # h0EK: Магистр (Q)
    wts_updates[14365] = "|cffe4cfa3Магистр|r"
    wts_updates[14366] = "|cffe4cfa3Магистр|r (|cffffffffQ|r)"
    wts_updates[35867] = (
        "|cffa6afb8ЮНИТ:|cffced4da Чародей эльфов крови, владеющий сокрушительной магией огня и защитными заклинаниями.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненный доспех|cffced4da: повышает броню союзника и замедляет атакующих его врагов.|n"
        "- |cffa9c7deОгненная стрела|cffced4da: выпускает сгусток пламени, наносящий урон и оглушающий цель.|n"
        "- |cffa9c7deМалый метеор|cffced4da: обрушивает огненный дождь на указанную область.|n"
        "- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n|n"
        "Атакует наземные и воздушные цели (дальний бой, магический урон).|r"
    )
    checks_def.append({"type": "unit", "id": "h0EK", "field": "name", "expected": wts_updates[14365]})
    checks_def.append({"type": "unit", "id": "h0EK", "field": "tip", "expected": wts_updates[14366]})
    checks_def.append({"type": "unit", "id": "h0EK", "field": "ubertip", "expected": wts_updates[35867]})

    # h0EL: Чернокнижник (W)
    wts_updates[9655] = "|cffe4cfa3Чернокнижник|r"
    wts_updates[10080] = "|cffe4cfa3Чернокнижник|r (|cffffffffW|r)"
    wts_updates[35868] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тёмный заклинатель, использующий первородную магию Скверны для ослабления и уничтожения противников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯрость Скверны|cffced4da: увеличивает урон союзника ценой входящего урона.|n"
        "- |cffa9c7deСтрела Скверны|cffced4da: поражает врага едким сгустком, нанося урон и снижая броню цели и врагов вокруг.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает положительные эффекты с врагов и отрицательные с союзников.|n"
        "- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n|n"
        "Атакует наземные и воздушные цели (дальний бой, магический урон).|r"
    )
    checks_def.append({"type": "unit", "id": "h0EL", "field": "name", "expected": wts_updates[9655]})
    checks_def.append({"type": "unit", "id": "h0EL", "field": "tip", "expected": wts_updates[10080]})
    checks_def.append({"type": "unit", "id": "h0EL", "field": "ubertip", "expected": wts_updates[35868]})

    # n02O: Морской варан (Q)
    wts_updates[14553] = "|cffe4cfa3Морской варан|r"
    wts_updates[14554] = "|cffe4cfa3Морской варан|r (|cffffffffQ|r)"
    wts_updates[42374] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрое морское земноводное на службе наг. Стреляет ядовитыми шипами с дальней дистанции.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n"
        "- |cffa9c7deПоглощение силы|cffced4da: атаки восстанавливают здоровье при изучении «Тренировок Охотников».|n|n"
        "Атакует наземные и воздушные цели (дальний бой, дальний урон).|r"
    )
    checks_def.append({"type": "unit", "id": "n02O", "field": "name", "expected": wts_updates[14553]})
    checks_def.append({"type": "unit", "id": "n02O", "field": "tip", "expected": wts_updates[14554]})
    checks_def.append({"type": "unit", "id": "n02O", "field": "ubertip", "expected": wts_updates[42374]})

    # n02M: Мирмидон (W)
    wts_updates[14349] = "|cffe4cfa3Мирмидон|r"
    wts_updates[14350] = "|cffe4cfa3Мирмидон|r (|cffffffffW|r)"
    wts_updates[35261] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий трёххвостый воин наг ближнего боя с высоким запасом здоровья и тяжелым вооружением.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОпутывание|cffced4da: бросает сеть, приковывая врага к земле и притягивая летающие цели (требуется исследование).|n"
        "- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n"
        "- |cffa9c7deПоглощение силы|cffced4da: атаки восстанавливают здоровье при изучении «Тренировок Охотников».|n|n"
        "Атакует наземные цели (ближний бой, обычный урон).|r"
    )
    checks_def.append({"type": "unit", "id": "n02M", "field": "name", "expected": wts_updates[14349]})
    checks_def.append({"type": "unit", "id": "n02M", "field": "tip", "expected": wts_updates[14350]})
    checks_def.append({"type": "unit", "id": "n02M", "field": "ubertip", "expected": wts_updates[35261]})

    # n02N: Сирена (E)
    wts_updates[14371] = "|cffe4cfa3Сирена|r"
    wts_updates[14372] = "|cffe4cfa3Сирена|r (|cffffffffE|r)"
    wts_updates[42373] = (
        "|cffa6afb8ЮНИТ:|cffced4da Верховная колдунья наг, управляющая водными стихиями и темными чарами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСмерч|cffced4da: поднимает вражеского воина в воздух, выводя его из сражения.|n"
        "- |cffa9c7deРежущая вода|cffced4da: обрушивает ледяной всплеск, нанося урон и замедляя врагов в радиусе действия.|n"
        "- |cffa9c7deПаразит|cffced4da: заражает цель паразитом, порождающим порождение после гибели жертвы.|n"
        "- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n|n"
        "Атакует наземные и воздушные цели (дальний бой, магический урон).|r"
    )
    checks_def.append({"type": "unit", "id": "n02N", "field": "name", "expected": wts_updates[14371]})
    checks_def.append({"type": "unit", "id": "n02N", "field": "tip", "expected": wts_updates[14372]})
    checks_def.append({"type": "unit", "id": "n02N", "field": "ubertip", "expected": wts_updates[42373]})

    # h04Y: Покоренный демон (E)
    wts_updates[14359] = "|cffe4cfa3Покоренный демон|r"
    wts_updates[14363] = "|cffe4cfa3Покоренный демон|r (|cffffffffE|r)"
    wts_updates[15194] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий верховой страж Скверны, присягнувший на верность Иллидану.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯрость демон-зверя|cffced4da: значительно увеличивает скорость передвижения (требуется исследование).|n"
        "- |cffa9c7deОстрые клинки|cffced4da: повышает урон против целей со средней бронёй (требуется исследование).|n"
        "- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n"
        "- |cffa9c7deПоглощение силы|cffced4da: атаки восстанавливают здоровье при изучении «Тренировок Охотников».|n|n"
        "Атакует наземные цели (ближний бой, обычный урон).|r"
    )
    checks_def.append({"type": "unit", "id": "h04Y", "field": "name", "expected": wts_updates[14359]})
    checks_def.append({"type": "unit", "id": "h04Y", "field": "tip", "expected": wts_updates[14363]})
    checks_def.append({"type": "unit", "id": "h04Y", "field": "ubertip", "expected": wts_updates[15194]})

    # h04Z: Охотник «Истребление» (Q)
    wts_updates[14681] = "|cffe4cfa3Охотник «Истребление»|r"
    wts_updates[14682] = "|cffe4cfa3Охотник «Истребление»|r (|cffffffffQ|r)"
    wts_updates[35056] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный охотник на демонов, обученный сокрушать врагов яростными выпадами и аурой истребления.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура истребления|cffced4da: повышает силу атаки союзных войск поблизости на |cffc8e08710%|cffced4da.|n"
        "- |cffa9c7deПоглощение осколков|cffced4da: восстанавливает здоровье в размере |cffffffff15%|cffced4da от нанесённого урона.|n"
        "- |cffa9c7deВзор Скверны|cffced4da: даёт шанс нанести критический удар при атаке.|n"
        "- |cffa9c7deПротиводействие|cffced4da: каждая атака сжигает ману цели и наносит дополнительный урон.|n"
        "- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n|n"
        "Атакует наземные цели (ближний бой, урон хаоса).|r"
    )
    checks_def.append({"type": "unit", "id": "h04Z", "field": "name", "expected": wts_updates[14681]})
    checks_def.append({"type": "unit", "id": "h04Z", "field": "tip", "expected": wts_updates[14682]})
    checks_def.append({"type": "unit", "id": "h04Z", "field": "ubertip", "expected": wts_updates[35056]})

    # h050: Охотник «Месть» (W)
    wts_updates[14685] = "|cffe4cfa3Охотник «Месть»|r"
    wts_updates[14686] = "|cffe4cfa3Охотник «Месть»|r (|cffffffffW|r)"
    wts_updates[35243] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный охотник на демонов, специализирующийся на поглощении урона и подавлении противников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПропитка Скверной|cffced4da: снижает получаемый от атак урон на фиксированную величину.|n"
        "- |cffa9c7deПоглощение осколков|cffced4da: восстанавливает здоровье в размере |cffffffff15%|cffced4da от нанесённого урона.|n"
        "- |cffa9c7deВзор Скверны|cffced4da: даёт шанс нанести критический удар при атаке.|n"
        "- |cffa9c7deПротиводействие|cffced4da: каждая атака сжигает ману цели и наносит дополнительный урон.|n"
        "- |cffa9c7deЛовкость иллидари|cffced4da: шанс уклониться от атаки.|n|n"
        "Атакует наземные цели (ближний бой, урон хаоса).|r"
    )
    checks_def.append({"type": "unit", "id": "h050", "field": "name", "expected": wts_updates[14685]})
    checks_def.append({"type": "unit", "id": "h050", "field": "tip", "expected": wts_updates[14686]})
    checks_def.append({"type": "unit", "id": "h050", "field": "ubertip", "expected": wts_updates[35243]})

    # =========================================================================
    # 4. HEROES: 4 heroes
    # =========================================================================
    # H043: Маг Крови (A)
    wts_updates[4403] = "|cffe4cfa3Маг Крови|r"
    wts_updates[5839] = "|cffe4cfa3Маг Крови|r (|cffffffffA|r)"
    wts_updates[5011] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Верховный чародей эльфов крови, в совершенстве управляющий разрушительным пламенем и потоками маны. Основная характеристика — |cffffffffинтеллект|cffced4da. Обрушивает огненные столбы на отряды врагов, изгоняет цели в астральный план, вытягивает запасы маны и призывает возрождающегося огненного феникса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОгненный столб|cffced4da: наносит периодический урон огнём войскам в выбранной области.|n"
        "- |cffa9c7deИзгнание|cffced4da: перемещает цель в астрал, делая её бессильной атаковать, но уязвимой к магии.|n"
        "- |cffa9c7deПохищение маны|cffced4da: перекачивает ману из врага себе или передаёт её союзнику.|n"
        "- |cffa9c7deФеникс|cffced4da: призывает могучего огненного феникса, перерождающегося после гибели.|n|n"
        "Атакует наземные и воздушные цели (дальний бой, урон героя).|r"
    )
    checks_def.append({"type": "unit", "id": "H043", "field": "name", "expected": wts_updates[4403]})
    checks_def.append({"type": "unit", "id": "H043", "field": "tip", "expected": wts_updates[5839]})
    checks_def.append({"type": "unit", "id": "H043", "field": "ubertip", "expected": wts_updates[5011]})

    # E01W: Охотник на демонов (Q)
    wts_updates[798] = "|cffe4cfa3Охотник на демонов|r"
    wts_updates[802] = "|cffe4cfa3Ярость Теней|r"
    wts_updates[20840] = "|cffe4cfa3Охотник на демонов|r (|cffffffffQ|r)"
    wts_updates[31755] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Мастер парных клинков и тайных демонических искусств. Основная характеристика — |cffffffffловкость|cffced4da. Сжигает запасы маны врагов, окружает себя обжигающим пламенем, уклоняется от вражеских ударов и принимает демоническую форму дальнего боя.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСожжение маны|cffced4da: уничтожает ману противника, нанося эквивалентный урон.|n"
        "- |cffa9c7deОбжигающий жар|cffced4da: окружает героя огненной аурой, сжигающей окружающих врагов.|n"
        "- |cffa9c7deУскользание|cffced4da: даёт шанс избежать получения урона от атак.|n"
        "- |cffa9c7deМетаморфоза|cffced4da: превращает героя в крылатого демона с дальней атакой и повышенным запасом здоровья.|n|n"
        "Атакует наземные цели (ближний бой, урон героя).|r"
    )
    checks_def.append({"type": "unit", "id": "E01W", "field": "name", "expected": wts_updates[798]})
    checks_def.append({"type": "unit", "id": "E01W", "field": "tip", "expected": wts_updates[20840]})
    checks_def.append({"type": "unit", "id": "E01W", "field": "ubertip", "expected": wts_updates[31755]})

    # E024: Охотник «Месть» (E)
    wts_updates[942] = "|cffe4cfa3Охотник «Месть»|r"
    wts_updates[1249] = "|cffe4cfa3Тихая смерть|r"
    wts_updates[14787] = "|cffe4cfa3Охотник «Месть»|r (|cffffffffE|r)"
    wts_updates[31757] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Несокрушимый защитник Иллидари, черпающий стойкость из боли и пламени Скверны. Основная характеристика — |cffffffffсила|cffced4da. Защищается вспышкой Скверны, вытягивает жизненные силы окружающих врагов жаром поглощения, наносит критические удары и возвращает полученный урон врагам.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВспышка Скверны|cffced4da: повышает броню и наносит урон применяющим заклинания врагам.|n"
        "- |cffa9c7deЖар поглощения|cffced4da: поглощает здоровье всех окружающих существ, исцеляя героя.|n"
        "- |cffa9c7deВзор Скверны|cffced4da: даёт шанс нанести многократный урон при атаке.|n"
        "- |cffa9c7deПламенная боль|cffced4da: окружает щитом, возвращающим нанесённый по войску урон атаковавшим врагам.|n|n"
        "Атакует наземные цели (ближний бой, урон героя).|r"
    )
    checks_def.append({"type": "unit", "id": "E024", "field": "name", "expected": wts_updates[942]})
    checks_def.append({"type": "unit", "id": "E024", "field": "tip", "expected": wts_updates[14787]})
    checks_def.append({"type": "unit", "id": "E024", "field": "ubertip", "expected": wts_updates[31757]})

    # E025: Охотник «Истребление» (W)
    wts_updates[14034] = "|cffe4cfa3Охотник «Истребление»|r"
    wts_updates[6900] = "|cffe4cfa3Яростный охотник|r"
    wts_updates[14789] = "|cffe4cfa3Охотник «Истребление»|r (|cffffffffW|r)"
    wts_updates[38606] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Молниеносный мастер истребления демонов, крушащий врагов вихрем ударов. Основная характеристика — |cffffffffловкость|cffced4da. Совершает стремительный рывок Скверны через ряды врагов, впадает в ярость боя, оглушает противников сокрушительным разломом и наделяет клинки рассекающей силой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРывок Скверны|cffced4da: совершает стремительный рывок вперёд, расталкивая и поражая всех врагов на пути.|n"
        "- |cffa9c7deЯрость Скверны|cffced4da: резко повышает темп атак ценой увеличенного входящего урона.|n"
        "- |cffa9c7deРазлом|cffced4da: даёт шанс нанести дополнительный урон и оглушить цель при ударе.|n"
        "- |cffa9c7deКлинки Скверны|cffced4da: атаки наносят рассекающий урон всем противникам рядом с целью.|n|n"
        "Атакует наземные цели (ближний бой, урон героя).|r"
    )
    checks_def.append({"type": "unit", "id": "E025", "field": "name", "expected": wts_updates[14034]})
    checks_def.append({"type": "unit", "id": "E025", "field": "tip", "expected": wts_updates[14789]})
    checks_def.append({"type": "unit", "id": "E025", "field": "ubertip", "expected": wts_updates[38606]})

    # =========================================================================
    # 5. ABILITIES: Hero & Unit Abilities
    # =========================================================================
    # AHfs (Огненный столб)
    wts_updates[5617] = "|cffe4cfa3Огненный столб|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)"
    wts_updates[1441] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным войскам в области |cffffffff150|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # AHbn (Изгнание)
    wts_updates[25760] = "|cffe4cfa3Изгнание|r"
    wts_updates[25761] = "|cffe4cfa3Изгнание|r (|cffffffffW|r)"
    wts_updates[25762] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Изгоняет выбранную цель в астральный план. Изгнанная цель замедляется, теряет способность атаковать, но получает значительно больше урона от магии и заклинаний.|r"
    wts_updates[5621] = "|cffe4cfa3Изгнание|r [|cffffffff4-й уровень|r] (|cffffffffW|r)"
    wts_updates[5622] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Изгоняет цель в астральный план на |cffffffff5|cffced4da сек. (героев на |cffffffff3|cffced4da сек.), замедляя её скорость передвижения на |cffffffff50%|cffced4da. Не действует на здания и технику.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # AHdr (Похищение маны)
    wts_updates[32062] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт магический канал, вытягивающий ману из вражеского юнита или передающий собственную ману союзнику.|r"
    wts_updates[5619] = "|cffe4cfa3Похищение маны|r [|cffffffff4-й уровень|r] (|cffffffffE|r)"
    wts_updates[5620] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает |cffffffff60|cffced4da ед. маны/сек. из вражеского юнита или передаёт союзнику. Запас маны мага крови может временно превысить максимальный.|nВремя действия: |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # AHpx (Феникс)
    wts_updates[16143] = "|cffe4cfa3Феникс|r"
    wts_updates[16142] = "|cffe4cfa3Феникс|r (|cffffffffR|r)"
    wts_updates[16144] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает могучего огненного феникса, обладающего иммунитетом к магии и огненной аурой. После гибели феникс превращается в яйцо и перерождается.|r"
    wts_updates[5623] = "|cffe4cfa3Феникс|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
    wts_updates[5624] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da могучих огненных фениксов. Фениксы невосприимчивы к магии, наносят периодический урон огнём вокруг себя и перерождаются из яиц после гибели.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # AEmb (Сожжение маны)
    wts_updates[14288] = "|cffe4cfa3Сожжение маны|r"
    wts_updates[14289] = "|cffe4cfa3Сожжение маны|r (|cffffffffQ|r)"
    wts_updates[14290] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выжигает часть запаса маны указанного врага и наносит урон, равный количеству сожжённой маны.|r"
    wts_updates[14291] = "|cffe4cfa3Сожжение маны|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14292] = "|cffe4cfa3Сожжение маны|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14293] = "|cffe4cfa3Сожжение маны|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14294] = "|cffe4cfa3Сожжение маны|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14295] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает до |cffffffff50|cffced4da ед. маны вражеского юнита и наносит ему столько же урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[14296] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает до |cffffffff100|cffced4da ед. маны вражеского юнита и наносит ему столько же урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[14297] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает до |cffffffff150|cffced4da ед. маны вражеского юнита и наносит ему столько же урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[14298] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает до |cffffffff200|cffced4da ед. маны вражеского юнита и наносит ему столько же урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # AEim (Обжигающий жар)
    wts_updates[2052] = "|cffe4cfa3Обжигающий жар|r"
    wts_updates[9742] = "|cffe4cfa3Обжигающий жар|r (|cffffffffW|r)"
    wts_updates[14287] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает охотника на демонов кольцом огня, наносящим непрерывный урон всем окружающим наземным противникам.|r"
    wts_updates[9756] = "|cffe4cfa3Обжигающий жар|r [|cffffffff1-й уровень|r] (|cffffffffW|r)"
    wts_updates[9758] = "|cffe4cfa3Обжигающий жар|r [|cffffffff2-й уровень|r] (|cffffffffW|r)"
    wts_updates[9760] = "|cffe4cfa3Обжигающий жар|r [|cffffffff3-й уровень|r] (|cffffffffW|r)"
    wts_updates[9910] = "|cffe4cfa3Обжигающий жар|r [|cffffffff4-й уровень|r] (|cffffffffW|r)"
    wts_updates[14227] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя огненным щитом, наносящим |cffffffff10|cffced4da ед. урона/сек. окружающим наземным врагам в радиусе |cffffffff160|cffced4da.|nРасходует ману при активации и каждую секунду до отмены.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[14230] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя огненным щитом, наносящим |cffffffff15|cffced4da ед. урона/сек. окружающим наземным врагам в радиусе |cffffffff160|cffced4da.|nРасходует ману при активации и каждую секунду до отмены.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[14233] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя огненным щитом, наносящим |cffffffff20|cffced4da ед. урона/сек. окружающим наземным врагам в радиусе |cffffffff160|cffced4da.|nРасходует ману при активации и каждую секунду до отмены.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[14236] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя огненным щитом, наносящим |cffffffff25|cffced4da ед. урона/сек. окружающим наземным врагам в радиусе |cffffffff160|cffced4da.|nРасходует ману при активации и каждую секунду до отмены.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    wts_updates[14237] = "|cffe4cfa3Отменить «Обжигающий жар»|r (|cffffffffW|r)"
    wts_updates[14240] = "|cffe4cfa3Отменить «Обжигающий жар»|r (|cffffffffW|r)"
    wts_updates[14281] = "|cffe4cfa3Отменить «Обжигающий жар»|r (|cffffffffW|r)"
    wts_updates[14282] = "|cffe4cfa3Отменить «Обжигающий жар»|r (|cffffffffW|r)"
    wts_updates[14283] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прекращает действие «Обжигающего жара» и останавливает расход маны.|r"
    wts_updates[14284] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прекращает действие «Обжигающего жара» и останавливает расход маны.|r"
    wts_updates[14285] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прекращает действие «Обжигающего жара» и останавливает расход маны.|r"
    wts_updates[14286] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прекращает действие «Обжигающего жара» и останавливает расход маны.|r"

    # AEev (Ускользание)
    wts_updates[5770] = "|cffe4cfa3Ускользание|r"
    wts_updates[8767] = "|cffe4cfa3Ускользание|r (|cffffffffE|r)"
    wts_updates[12249] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс полностью уклониться от физической атаки противника.|r"
    wts_updates[10941] = "|cffe4cfa3Ускользание|r [|cffffffff1-й уровень|r] (|cffffffffE|r)"
    wts_updates[8771] = "|cffe4cfa3Ускользание|r [|cffffffff2-й уровень|r] (|cffffffffE|r)"
    wts_updates[8772] = "|cffe4cfa3Ускользание|r [|cffffffff3-й уровень|r] (|cffffffffE|r)"
    wts_updates[8775] = "|cffe4cfa3Ускользание|r [|cffffffff4-й уровень|r] (|cffffffffE|r)"
    wts_updates[11335] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff10%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[8780] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff20%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[9392] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff30%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[12243] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff40%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0NZ (Метаморфоза)
    wts_updates[14310] = "|cffe4cfa3Метаморфоза|r"
    wts_updates[14311] = "|cffe4cfa3Метаморфоза|r (|cffffffffR|r)"
    wts_updates[14312] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает охотника на демонов в могущественного крылатого демона с дальней атакой и повышенным здоровьем.|r"
    wts_updates[14313] = "|cffe4cfa3Метаморфоза|r [|cffffffff1-й уровень|r] (|cffffffffR|r)"
    wts_updates[14314] = "|cffe4cfa3Метаморфоза|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
    wts_updates[14316] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой превращается в демона с дальней атакой, бонусом |cffc8e087+500|cffced4da к здоровью и повышенной скоростью боя.|nДлительность: |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[14315] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой превращается в демона с дальней атакой, бонусом |cffc8e087+700|cffced4da к здоровью и повышенной скоростью боя.|nДлительность: |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A0UV (Вспышка Скверны)
    wts_updates[6801] = "|cffe4cfa3Вспышка Скверны|r"
    wts_updates[10663] = "|cffe4cfa3Вспышка Скверны|r (|cffffffffE|r)"
    wts_updates[15469] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя защитной аурой Скверны, увеличивающей броню и наносящей урон врагам при сотворении ими заклинаний.|r"
    wts_updates[6802] = "|cffe4cfa3Вспышка Скверны|r [|cffffffff1-й уровень|r] (|cffffffffE|r)"
    wts_updates[6803] = "|cffe4cfa3Вспышка Скверны|r [|cffffffff2-й уровень|r] (|cffffffffE|r)"
    wts_updates[6806] = "|cffe4cfa3Вспышка Скверны|r [|cffffffff3-й уровень|r] (|cffffffffE|r)"
    wts_updates[10672] = "|cffe4cfa3Вспышка Скверны|r [|cffffffff4-й уровень|r] (|cffffffffE|r)"
    wts_updates[10666] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт бонус |cffc8e087+6|cffced4da к броне и поражает противников вспышкой на |cffffffff60|cffced4da ед. урона каждый раз, когда они сотворяют заклинание в радиусе |cffffffff600|cffced4da.|nДлительность: |cffffffff30|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10669] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт бонус |cffc8e087+9|cffced4da к броне и поражает противников вспышкой на |cffffffff80|cffced4da ед. урона каждый раз, когда они сотворяют заклинание в радиусе |cffffffff600|cffced4da.|nДлительность: |cffffffff30|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10675] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт бонус |cffc8e087+12|cffced4da к броне и поражает противников вспышкой на |cffffffff100|cffced4da ед. урона каждый раз, когда они сотворяют заклинание в радиусе |cffffffff600|cffced4da.|nДлительность: |cffffffff30|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    wts_updates[6807] = "|cffe4cfa3Отменить «Вспышку Скверны»|r (|cffffffffE|r)"
    wts_updates[7746] = "|cffe4cfa3Отменить «Вспышку Скверны»|r (|cffffffffE|r)"
    wts_updates[10283] = "|cffe4cfa3Отменить «Вспышку Скверны»|r (|cffffffffE|r)"
    wts_updates[10678] = "|cffe4cfa3Отменить «Вспышку Скверны»|r (|cffffffffE|r)"
    wts_updates[10618] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прерывает действие «Вспышки Скверны».|r"
    wts_updates[10622] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прерывает действие «Вспышки Скверны».|r"
    wts_updates[10654] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прерывает действие «Вспышки Скверны».|r"
    wts_updates[10681] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прерывает действие «Вспышки Скверны».|r"

    # A0NJ (Жар поглощения)
    wts_updates[9824] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[9828] = "|cffe4cfa3Жар поглощения|r (|cffffffffW|r)"
    wts_updates[14029] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает внутреннее пламя Скверны, вытягивающее здоровье окружающих противников и исцеляющее героя.|r"
    wts_updates[9826] = "|cffe4cfa3Жар поглощения|r [|cffffffff1-й уровень|r] (|cffffffffW|r)"
    wts_updates[9912] = "|cffe4cfa3Жар поглощения|r [|cffffffff2-й уровень|r] (|cffffffffW|r)"
    wts_updates[9911] = "|cffe4cfa3Жар поглощения|r [|cffffffff3-й уровень|r] (|cffffffffW|r)"
    wts_updates[11099] = "|cffe4cfa3Жар поглощения|r [|cffffffff4-й уровень|r] (|cffffffffW|r)"
    wts_updates[14035] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает пламя Скверны на |cffffffff15|cffced4da сек., поглощая |cffffffff10|cffced4da ед. здоровья/сек. у врагов в радиусе |cffffffff180|cffced4da и передавая его герою.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[14036] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает пламя Скверны на |cffffffff15|cffced4da сек., поглощая |cffffffff10|cffced4da ед. здоровья/сек. у врагов в радиусе |cffffffff220|cffced4da и передавая его герою.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[14039] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает пламя Скверны на |cffffffff15|cffced4da сек., поглощая |cffffffff20|cffced4da ед. здоровья/сек. у врагов в радиусе |cffffffff220|cffced4da и передавая его герою.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[14096] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает пламя Скверны на |cffffffff15|cffced4da сек., поглощая |cffffffff30|cffced4da ед. здоровья/сек. у врагов в радиусе |cffffffff220|cffced4da и передавая его герою.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0NS (Взор Скверны)
    wts_updates[14194] = "|cffe4cfa3Взор Скверны|r"
    wts_updates[14195] = "|cffe4cfa3Взор Скверны|r (|cffffffffQ|r)"
    wts_updates[14205] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс нанести критический удар увеличенной силы при атаке.|r"
    wts_updates[14196] = "|cffe4cfa3Взор Скверны|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14197] = "|cffe4cfa3Взор Скверны|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14198] = "|cffe4cfa3Взор Скверны|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14199] = "|cffe4cfa3Взор Скверны|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)"
    wts_updates[14201] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffffffff15%|cffced4da нанести удвоенный (|cffffffff2x|cffced4da) урон при ударе.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[14202] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffffffff15%|cffced4da нанести трёхкратный (|cffffffff3x|cffced4da) урон при ударе.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[14203] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffffffff15%|cffced4da нанести четырёхкратный (|cffffffff4x|cffced4da) урон при ударе.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[14200] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffffffff15%|cffced4da нанести шестикратный (|cffffffff6x|cffced4da) урон при ударе.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0NU (Пламенная боль)
    wts_updates[14211] = "|cffe4cfa3Пламенная боль|r"
    wts_updates[14215] = "|cffe4cfa3Пламенная боль|r (|cffffffffR|r)"
    wts_updates[14216] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзников барьером пламени, возвращающим нанесённый по ним урон атакующим врагам.|r"
    wts_updates[14212] = "|cffe4cfa3Пламенная боль|r [|cffffffff1-й уровень|r] (|cffffffffR|r)"
    wts_updates[14218] = "|cffe4cfa3Пламенная боль|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
    wts_updates[14213] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует защитный барьер в радиусе |cffffffff900|cffced4da на |cffffffff20|cffced4da сек., возвращающий нанесённый врагами в ближнем бою урон обратно атакующим.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[14220] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует усиленный защитный барьер в радиусе |cffffffff900|cffced4da на |cffffffff20|cffced4da сек., возвращающий повышенный урон атакующим врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A0NF (Рывок Скверны)
    wts_updates[6918] = "|cffe4cfa3Рывок Скверны|r"
    wts_updates[6920] = "|cffe4cfa3Рывок Скверны|r (|cffffffffQ|r)"
    wts_updates[2752] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Совершает стремительный рывок вперёд, расталкивая противников и нанося урон всем задетым целям.|r"
    wts_updates[6922] = "|cffe4cfa3Рывок Скверны|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)"
    wts_updates[6925] = "|cffe4cfa3Рывок Скверны|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)"
    wts_updates[6928] = "|cffe4cfa3Рывок Скверны|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)"
    wts_updates[6933] = "|cffe4cfa3Рывок Скверны|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)"
    wts_updates[7132] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Охотник на демонов совершает рывок в выбранном направлении, расталкивая врагов и нанося им |cffffffff75|cffced4da ед. урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[7202] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Охотник на демонов совершает рывок в выбранном направлении, расталкивая врагов и нанося им |cffffffff150|cffced4da ед. урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[12043] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Охотник на демонов совершает рывок в выбранном направлении, расталкивая врагов и нанося им |cffffffff220|cffced4da ед. урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[12053] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Охотник на демонов совершает рывок в выбранном направлении, расталкивая врагов и нанося им |cffffffff300|cffced4da ед. урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0NX (Ярость Скверны)
    wts_updates[14248] = "|cffe4cfa3Ярость Скверны|r"
    wts_updates[14249] = "|cffe4cfa3Ярость Скверны|r (|cffffffffW|r)"
    wts_updates[14258] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Резко ускоряет скорость атаки героя ценой повышенного получаемого урона.|r"
    wts_updates[14250] = "|cffe4cfa3Ярость Скверны|r [|cffffffff1-й уровень|r] (|cffffffffW|r)"
    wts_updates[14251] = "|cffe4cfa3Ярость Скверны|r [|cffffffff2-й уровень|r] (|cffffffffW|r)"
    wts_updates[14252] = "|cffe4cfa3Ярость Скверны|r [|cffffffff3-й уровень|r] (|cffffffffW|r)"
    wts_updates[14253] = "|cffe4cfa3Ярость Скверны|r [|cffffffff4-й уровень|r] (|cffffffffW|r)"
    wts_updates[14259] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт бонус |cffc8e087+400%|cffced4da к скорости атаки, но увеличивает получаемый урон на |cffe69a8d50%|cffced4da.|nДлительность: |cffffffff12|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[14260] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт бонус |cffc8e087+400%|cffced4da к скорости атаки, но увеличивает получаемый урон на |cffe69a8d40%|cffced4da.|nДлительность: |cffffffff12|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[14261] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт бонус |cffc8e087+400%|cffced4da к скорости атаки, но увеличивает получаемый урон на |cffe69a8d30%|cffced4da.|nДлительность: |cffffffff12|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[14262] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт бонус |cffc8e087+400%|cffced4da к скорости атаки, но увеличивает получаемый урон на |cffe69a8d20%|cffced4da.|nДлительность: |cffffffff12|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    wts_updates[14254] = "|cffe4cfa3Отменить «Ярость Скверны»|r (|cffffffffW|r)"
    wts_updates[14255] = "|cffe4cfa3Отменить «Ярость Скверны»|r (|cffffffffW|r)"
    wts_updates[14256] = "|cffe4cfa3Отменить «Ярость Скверны»|r (|cffffffffW|r)"
    wts_updates[14257] = "|cffe4cfa3Отменить «Ярость Скверны»|r (|cffffffffW|r)"

    # A0NW (Разлом)
    wts_updates[14235] = "|cffe4cfa3Разлом|r"
    wts_updates[14241] = "|cffe4cfa3Разлом|r (|cffffffffE|r)"
    wts_updates[14242] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс нанести дополнительный урон и оглушить цель при ударе.|r"
    wts_updates[14243] = "|cffe4cfa3Разлом|r [|cffffffff1-й уровень|r] (|cffffffffE|r)"
    wts_updates[14244] = "|cffe4cfa3Разлом|r [|cffffffff2-й уровень|r] (|cffffffffE|r)"
    wts_updates[14245] = "|cffe4cfa3Разлом|r [|cffffffff3-й уровень|r] (|cffffffffE|r)"
    wts_updates[14246] = "|cffe4cfa3Разлом|r [|cffffffff4-й уровень|r] (|cffffffffE|r)"

    # A0NV (Клинки Скверны)
    wts_updates[14228] = "|cffe4cfa3Клинки Скверны|r"
    wts_updates[14232] = "|cffe4cfa3Клинки Скверны|r (|cffffffffR|r)"
    wts_updates[14277] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наполняет клинки энергией Скверны, заставляя атаки наносить рассекающий урон окружающим целям.|r"
    wts_updates[14264] = "|cffe4cfa3Клинки Скверны|r [|cffffffff1-й уровень|r] (|cffffffffR|r)"
    wts_updates[14265] = "|cffe4cfa3Клинки Скверны|r [|cffffffff2-й уровень|r] (|cffffffffR|r)"
    wts_updates[14276] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки героя наносят |cffffffff40%|cffced4da рассекающего урона всем врагам в радиусе |cffffffff180|cffced4da от цели.|nДлительность: |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[14278] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки героя наносят |cffffffff60%|cffced4da рассекающего урона всем врагам в радиусе |cffffffff220|cffced4da от цели.|nДлительность: |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"

    # A0O2 (Ловкость иллидари)
    wts_updates[38522] = "|cffe4cfa3Ловкость иллидари|r"
    wts_updates[38524] = "|cffe4cfa3Ловкость иллидари|r [|cffffffff1-й уровень|r]"
    wts_updates[38525] = "|cffe4cfa3Ловкость иллидари|r [|cffffffff2-й уровень|r]"
    wts_updates[38526] = "|cffe4cfa3Ловкость иллидари|r [|cffffffff3-й уровень|r]"
    wts_updates[38546] = "|cffe4cfa3Ловкость иллидари|r [|cffffffff4-й уровень|r]"
    wts_updates[38523] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт воину постоянный шанс |cffffffff6%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[38527] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт воину постоянный шанс |cffffffff12%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[38528] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт воину постоянный шанс |cffffffff18%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[38529] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт воину постоянный шанс |cffffffff24%|cffced4da уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"

    # A0O5 (Поглощение силы)
    wts_updates[38548] = "|cffe4cfa3Поглощение силы|r"
    wts_updates[38550] = "|cffe4cfa3Поглощение силы|r"
    wts_updates[14533] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При изученном исследовании «Тренировки Охотников» любая атака восстанавливает |cffc8e0870,5%|cffced4da от максимального здоровья воина (урон способностями — |cffc8e0870,25%|cffced4da).|r"

    # A0OH (Ярость демон-зверя)
    wts_updates[14769] = "|cffe4cfa3Ярость демон-зверя|r"
    wts_updates[14770] = "|cffe4cfa3Ярость демон-зверя|r"
    wts_updates[14771] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения покоренного демона на |cffc8e087+50|cffced4da.|r"

    # A0OG (Острые клинки)
    wts_updates[14766] = "|cffe4cfa3Острые клинки|r"
    wts_updates[14767] = "|cffe4cfa3Острые клинки|r"
    wts_updates[14768] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон покоренного демона по противникам со средней бронёй на |cffc8e087+25%|cffced4da.|r"

    # A1GU (Поглощение осколков)
    wts_updates[794] = "|cffe4cfa3Поглощение осколков|r"
    wts_updates[2215] = "|cffe4cfa3Поглощение осколков|r"
    wts_updates[2219] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атакуя цель, охотник раскалывает её душу на осколки, восстанавливая себе здоровье в размере |cffffffff15%|cffced4da от нанесённого урона.|r"

    # A0OF (Аура истребления)
    wts_updates[14763] = "|cffe4cfa3Аура истребления|r"
    wts_updates[14764] = "|cffe4cfa3Аура истребления|r"
    wts_updates[14765] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атаки союзных войск в радиусе |cffffffff400|cffced4da на |cffc8e087+10%|cffced4da.|r"

    # A0OE (Пропитка Скверной)
    wts_updates[14760] = "|cffe4cfa3Пропитка Скверной|r"
    wts_updates[14761] = "|cffe4cfa3Пропитка Скверной|r"
    wts_updates[15038] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает любой получаемый от физических атак урон на |cffc8e08715|cffced4da ед. Минимальный получаемый урон: |cffffffff3|cffced4da.|r"

    # A0O1 (Взор Скверны unit)
    wts_updates[14329] = "|cffe4cfa3Взор Скверны|r"
    wts_updates[14330] = "|cffe4cfa3Взор Скверны|r"
    wts_updates[14340] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс нанести критический удар увеличенной силы при атаке.|r"
    wts_updates[14331] = "|cffe4cfa3Взор Скверны|r"
    wts_updates[14332] = "|cffe4cfa3Взор Скверны|r"
    wts_updates[14333] = "|cffe4cfa3Взор Скверны|r"
    wts_updates[14334] = "|cffe4cfa3Взор Скверны|r"
    wts_updates[14336] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff15%|cffced4da нанести удвоенный (|cffffffff2x|cffced4da) урон при ударе.|r"
    wts_updates[14337] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff15%|cffced4da нанести удвоенный (|cffffffff2x|cffced4da) урон при ударе.|r"
    wts_updates[14338] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff15%|cffced4da нанести удвоенный (|cffffffff2x|cffced4da) урон при ударе.|r"
    wts_updates[14335] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт постоянный шанс |cffffffff15%|cffced4da нанести удвоенный (|cffffffff2x|cffced4da) урон при ударе.|r"

    # A0O0 (Противодействие)
    wts_updates[14317] = "|cffe4cfa3Противодействие|r"
    wts_updates[14318] = "|cffe4cfa3Противодействие|r"
    wts_updates[12939] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака уничтожает ману цели, нанося дополнительный урон: |cffffffff6|cffced4da ед. маны у героев и |cffffffff20|cffced4da ед. маны у обычных воинов.|r"

    # A048 (Инфернальный прыжок)
    wts_updates[2967] = "|cffe4cfa3Инфернальный прыжок|r"
    wts_updates[2968] = "|cffe4cfa3Инфернальный прыжок|r (|cffffffffQ|r)"
    wts_updates[927] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Стремительно совершает прыжок к противнику, нанося урон при приземлении.|r"

    # A1KL (Огненная стрела автокаст)
    wts_updates[38565] = "|cffe4cfa3Огненная стрела|r"
    wts_updates[38566] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[38568] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[38569] = "|cffe4cfa3Огненная стрела|r (|cffffffffQ|r)"
    wts_updates[38607] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня во врага, нанося урон и оглушая цель на |cffffffff2|cffced4da сек.|r"
    wts_updates[38570] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня во врага, нанося урон и оглушая цель на |cffffffff2|cffced4da сек.|r"
    wts_updates[38571] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток огня во врага, нанося урон и оглушая цель на |cffffffff2|cffced4da сек.|r"

    # A1KO (Стрела Скверны автокаст)
    wts_updates[38590] = "|cffe4cfa3Стрела Скверны|r"
    wts_updates[38591] = "|cffe4cfa3Стрела Скверны|r (|cffffffffQ|r)"
    wts_updates[38593] = "|cffe4cfa3Стрела Скверны|r (|cffffffffQ|r)"
    wts_updates[38594] = "|cffe4cfa3Стрела Скверны|r (|cffffffffQ|r)"
    wts_updates[38595] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком Скверны, нанося урон и снижая броню цели и окружающих врагов на |cffe69a8d3|cffced4da ед.|r"
    wts_updates[38596] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком Скверны, нанося урон и снижая броню цели и окружающих врагов на |cffe69a8d3|cffced4da ед.|r"
    wts_updates[38597] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель сгустком Скверны, нанося урон и снижая броню цели и окружающих врагов на |cffe69a8d3|cffced4da ед.|r"

    # A0NI (Ускользание technical trigger)
    wts_updates[9741] = "|cffe4cfa3Ускользание|r"

    # A0NT (Пламенная боль trigger aura)
    wts_updates[14208] = "|cffe4cfa3Пламенная боль|r"
    wts_updates[14209] = "|cffe4cfa3Пламенная боль|r"
    wts_updates[14206] = "|cffe4cfa3Пламенная боль|r"
    wts_updates[14207] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает нанесённый по союзникам в ближнем бою урон атакующим врагам.|r"

    # A0NY (Клинки Скверны trigger cleave)
    wts_updates[14279] = "|cffe4cfa3Клинки Скверны|r"
    wts_updates[14280] = "|cffe4cfa3Клинки Скверны|r"

    # Technical trigger lifesteal auras (A0NO, A0NM, A0NP, A0NK, A0NR, A0NL, A0NQ, A0NN)
    wts_updates[11509] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[11563] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[9069] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает жизненную силу противников, передавая её герою.|r"
    wts_updates[11291] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[11548] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[11978] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[11507] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает жизненную силу противников, передавая её герою.|r"
    wts_updates[11138] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[12850] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[13306] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[12246] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает жизненную силу противников, передавая её герою.|r"
    wts_updates[11282] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[12252] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[12846] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[11546] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает жизненную силу противников, передавая её герою.|r"
    wts_updates[11352] = "|cffe4cfa3Жар поглощения|r"
    wts_updates[11366] = "|cffe4cfa3Жар поглощения|r"

    # =========================================================================
    # 6. RESEARCHES: 19 technologies + 3 markers
    # =========================================================================
    # R08W: Оружие Скверны (6 уровней, hotkey W)
    w_name_sids = [14495, 14493, 14492, 14491, 14490, 14489]
    w_tip_sids = [14500, 14499, 14498, 14497, 14496, 14494]
    w_ub_sids = [14501, 14502, 14503, 14505, 14504, 14506]
    for lvl in range(1, 7):
        wts_updates[w_name_sids[lvl-1]] = f"|cffe4cfa3Оружие Скверны — уровень {lvl}|r"
        wts_updates[w_tip_sids[lvl-1]] = f"|cffe4cfa3Оружие Скверны — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[w_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает силу атаки стрелков и осадных орудий Иллидари.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМорской варан|cffced4da|n- |cffa9c7deРазрушитель|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R08T: Проклятое оружие (6 уровней, hotkey Q)
    t_name_sids = [14410, 14411, 14412, 14415, 14414, 14413]
    t_tip_sids = [14416, 14417, 14418, 14421, 14420, 14419]
    t_ub_sids = [14431, 14432, 14433, 14423, 14422, 14424]
    for lvl in range(1, 7):
        wts_updates[t_name_sids[lvl-1]] = f"|cffe4cfa3Проклятое оружие — уровень {lvl}|r"
        wts_updates[t_tip_sids[lvl-1]] = f"|cffe4cfa3Проклятое оружие — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[t_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя Иллидари.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтранник|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da|n- |cffa9c7deМирмидон|cffced4da|n- |cffa9c7deПокоренный демон|cffced4da|n- |cffa9c7deОхотник «Истребление»|cffced4da|n- |cffa9c7deОхотник «Месть»|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R08U: Осквернённые доспехи (6 уровней, hotkey A)
    u_name_sids = [14435, 14436, 14437, 14446, 14445, 14444]
    u_tip_sids = [14438, 14439, 14440, 14449, 14448, 14447]
    u_ub_sids = [15974, 15975, 15976, 15971, 15972, 15973]
    for lvl in range(1, 7):
        wts_updates[u_name_sids[lvl-1]] = f"|cffe4cfa3Осквернённые доспехи — уровень {lvl}|r"
        wts_updates[u_tip_sids[lvl-1]] = f"|cffe4cfa3Осквернённые доспехи — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[u_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает показатель брони всех воинов ближнего боя Иллидари.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтранник|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da|n- |cffa9c7deМирмидон|cffced4da|n- |cffa9c7deПокоренный демон|cffced4da|n- |cffa9c7deОхотник «Истребление»|cffced4da|n- |cffa9c7deОхотник «Месть»|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R08V: Укрепление Скверной (6 уровней, hotkey S)
    v_name_sids = [14457, 14458, 14459, 14468, 14467, 14466]
    v_tip_sids = [14460, 14461, 14462, 14465, 14464, 14463]
    v_ub_sids = [14479, 14480, 14481, 14469, 14470, 13833]
    for lvl in range(1, 7):
        wts_updates[v_name_sids[lvl-1]] = f"|cffe4cfa3Укрепление Скверной — уровень {lvl}|r"
        wts_updates[v_tip_sids[lvl-1]] = f"|cffe4cfa3Укрепление Скверной — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[v_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает показатель брони стрелков, заклинателей и осадных орудий Иллидари.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагистр|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da|n- |cffa9c7deМорской варан|cffced4da|n- |cffa9c7deСирена|cffced4da|n- |cffa9c7deРазрушитель|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R08X: Владение магией (6 уровней, hotkey Z)
    x_name_sids = [14508, 14509, 14510, 14513, 14512, 14511]
    x_tip_sids = [14514, 14515, 14516, 14519, 14518, 14517]
    x_ub_sids = [14529, 14530, 14531, 14521, 14520, 14522]
    for lvl in range(1, 7):
        wts_updates[x_name_sids[lvl-1]] = f"|cffe4cfa3Владение магией — уровень {lvl}|r"
        wts_updates[x_tip_sids[lvl-1]] = f"|cffe4cfa3Владение магией — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[x_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает магический урон от атак заклинателей Иллидари.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагистр|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da|n- |cffa9c7deСирена|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R096: Тренировки Охотников (3 уровня, hotkey X)
    wts_updates[14802] = "|cffe4cfa3Тренировки Охотников — уровень 1|r"
    wts_updates[14728] = "|cffe4cfa3Тренировки Охотников — уровень 1|r (|cffffffffX|r)"
    wts_updates[38530] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Охотники на демонов и воины Иллидари проходят суровые тренировки, повышая боевое мастерство и активируя способность «Поглощение силы».|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Скорость атаки: |cffc8e087+5%|cffced4da.|n- Урон от атак: |cffc8e087+4|cffced4da.|n- Шанс уклонения: |cffc8e087+6%|cffced4da.|n- Активирует вампиризм способности |cffa9c7de«Поглощение силы»|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da всем регулярным войскам Иллидари.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
    )
    wts_updates[14806] = "|cffe4cfa3Тренировки Охотников — уровень 2|r"
    wts_updates[14737] = "|cffe4cfa3Тренировки Охотников — уровень 2|r (|cffffffffX|r)"
    wts_updates[38531] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Охотники на демонов углубляют боевые тренировки, развивая скорость ударов и выживаемость.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Скорость атаки: |cffc8e087+10%|cffced4da.|n- Урон от атак: |cffc8e087+8|cffced4da.|n- Шанс уклонения: |cffc8e087+12%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da всем регулярным войскам Иллидари.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
    )
    wts_updates[14807] = "|cffe4cfa3Тренировки Охотников — уровень 3|r"
    wts_updates[14738] = "|cffe4cfa3Тренировки Охотников — уровень 3|r (|cffffffffX|r)"
    wts_updates[38532] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Высшая ступень тренировок охотников на демонов, наделяющая армию совершенными рефлексами.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Скорость атаки: |cffc8e087+15%|cffced4da.|n- Урон от атак: |cffc8e087+12|cffced4da.|n- Шанс уклонения: |cffc8e087+18%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da всем регулярным войскам Иллидари.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
    )

    # R099: Приоритет Наги (1 уровень, hotkey W)
    wts_updates[14852] = "|cffe4cfa3Приоритет Наги|r"
    wts_updates[15228] = "|cffe4cfa3Приоритет Наги|r (|cffffffffW|r)"
    wts_updates[14858] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Направляет военные ресурсы на подготовку и усиление глубинных войск наг.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Урон от атак: |cffc8e087+4|cffced4da.|n- Скорость передвижения: |cffc8e087+20|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМорской варан|cffced4da|n- |cffa9c7deМирмидон|cffced4da|n- |cffa9c7deСирена|cffced4da.|n|n"
        "|cffe6c07bВнимание:|cffced4da исключает выбор «Приоритета Эльфов» и «Приоритета Орков».|r"
    )

    # R09A: Приоритет Эльфы (1 уровень, hotkey E)
    wts_updates[14859] = "|cffe4cfa3Приоритет Эльфы|r"
    wts_updates[14860] = "|cffe4cfa3Приоритет Эльфы|r (|cffffffffE|r)"
    wts_updates[14865] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Направляет военные ресурсы на подготовку и укрепление эльфов крови и охотников.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+50|cffced4da.|n- Скорость атаки: |cffc8e087+15%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтранник|cffced4da|n- |cffa9c7deМагистр|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da|n- |cffa9c7deОхотник «Истребление»|cffced4da|n- |cffa9c7deОхотник «Месть»|cffced4da.|n|n"
        "|cffe6c07bВнимание:|cffced4da исключает выбор «Приоритета Наг» и «Приоритета Орков».|r"
    )

    # R09B: Приоритет Орки (1 уровень, hotkey R)
    wts_updates[14866] = "|cffe4cfa3Приоритет Орки|r"
    wts_updates[14867] = "|cffe4cfa3Приоритет Орки|r (|cffffffffR|r)"
    wts_updates[2950] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Направляет военные ресурсы на подготовку и свирепую мощь орков Скверны.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Урон от атак: |cffc8e087+10|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da.|n|n"
        "|cffe6c07bВнимание:|cffced4da исключает выбор «Приоритета Наг» и «Приоритета Эльфов».|r"
    )

    # R08Y: Укрыться за щитом (1 уровень, hotkey A)
    wts_updates[14541] = "|cffe4cfa3Укрыться за щитом|r"
    wts_updates[14550] = "|cffe4cfa3Укрыться за щитом|r (|cffffffffA|r)"

    # R091: Грубая сила (3 уровня, hotkey S)
    wts_updates[14628] = "|cffe4cfa3Грубая сила — уровень 1|r"
    wts_updates[14629] = "|cffe4cfa3Грубая сила — уровень 1|r (|cffffffffS|r)"
    wts_updates[14637] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Развивает ярость и физическую мощь орков Скверны.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+100|cffced4da.|n- Урон от атак: |cffc8e087+3|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
    )
    wts_updates[14633] = "|cffe4cfa3Грубая сила — уровень 2|r"
    wts_updates[14636] = "|cffe4cfa3Грубая сила — уровень 2|r (|cffffffffS|r)"
    wts_updates[14638] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дальнейшее развитие силы и выносливости орков Скверны.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+200|cffced4da.|n- Урон от атак: |cffc8e087+6|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
    )
    wts_updates[14634] = "|cffe4cfa3Грубая сила — уровень 3|r"
    wts_updates[14635] = "|cffe4cfa3Грубая сила — уровень 3|r (|cffffffffS|r)"
    wts_updates[14639] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Высшая степень закалки и неистовства орков Скверны.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+300|cffced4da.|n- Урон от атак: |cffc8e087+9|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
    )

    # R095: Яростный рывок (2 уровня, hotkey D)
    wts_updates[14716] = "|cffe4cfa3Яростный рывок — уровень 1|r"
    wts_updates[14720] = "|cffe4cfa3Яростный рывок — уровень 1|r (|cffffffffD|r)"
    wts_updates[14722] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает сумеречных налётчиков стремительному галопу ценой снижения силы атаки.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Скорость передвижения: |cffc8e087+35|cffced4da.|n|n"
        "|cffe69a8dШтраф:|cffced4da|n- Урон от атак: |cffe69a8d-3|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[14717] = "|cffe4cfa3Яростный рывок — уровень 2|r"
    wts_updates[14721] = "|cffe4cfa3Яростный рывок — уровень 2|r (|cffffffffD|r)"
    wts_updates[14725] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно разгоняет волков сумеречных налётчиков до предельной скорости.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Скорость передвижения: |cffc8e087+70|cffced4da.|n|n"
        "|cffe69a8dШтраф:|cffced4da|n- Урон от атак: |cffe69a8d-6|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный налётчик|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # R08Z: Посвящение магистров (6 уровней, hotkey A)
    z_name_sids = [14585, 14580, 14581, 14582, 14583, 14584]
    z_tip_sids = [14586, 14587, 14588, 14589, 14590, 14591]
    z_ub_sids = [15215, 15216, 15217, 15218, 15219, 15220]
    for lvl in range(1, 7):
        wts_updates[z_name_sids[lvl-1]] = f"|cffe4cfa3Посвящение магистров — уровень {lvl}|r"
        wts_updates[z_tip_sids[lvl-1]] = f"|cffe4cfa3Посвящение магистров — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[z_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает ранг магистров, увеличивая их характеристики и открывая новые заклинания огня.|n|n"
            f"|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+{lvl * 40}|cffced4da.|n- Запас маны: |cffc8e087+{lvl * 50}|cffced4da.|n- Восстановление маны: |cffc8e087+{round(lvl * 0.3, 1)}|cffced4da ед./сек.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМагистр|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R090: Посвящение чернокнижников (6 уровней, hotkey S)
    n_name_sids = [14610, 14605, 14606, 14607, 14608, 14609]
    n_tip_sids = [14611, 14612, 14613, 14614, 14615, 14616]
    n_ub_sids = [15221, 15222, 15223, 15224, 15225, 15226]
    for lvl in range(1, 7):
        wts_updates[n_name_sids[lvl-1]] = f"|cffe4cfa3Посвящение чернокнижников — уровень {lvl}|r"
        wts_updates[n_tip_sids[lvl-1]] = f"|cffe4cfa3Посвящение чернокнижников — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[n_ub_sids[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает ранг чернокнижников, увеличивая их характеристики и открывая новые тёмные заклинания Скверны.|n|n"
            f"|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+{lvl * 40}|cffced4da.|n- Запас маны: |cffc8e087+{lvl * 40}|cffced4da.|n- Восстановление маны: |cffc8e087+{round(lvl * 0.5, 1)}|cffced4da ед./сек.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЧернокнижник|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R094: Мутация Наг (2 уровня, hotkey A)
    wts_updates[14705] = "|cffe4cfa3Мутация Наг — уровень 1|r"
    wts_updates[14709] = "|cffe4cfa3Мутация Наг — уровень 1|r (|cffffffffA|r)"
    wts_updates[14711] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает телосложение глубинных войск наг темными мутациями Скверны.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+35|cffced4da.|n- Скорость передвижения: |cffc8e087+20|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМорской варан|cffced4da|n- |cffa9c7deМирмидон|cffced4da|n- |cffa9c7deСирена|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[14706] = "|cffe4cfa3Мутация Наг — уровень 2|r"
    wts_updates[14710] = "|cffe4cfa3Мутация Наг — уровень 2|r (|cffffffffA|r)"
    wts_updates[14714] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дальнейшая мутация наг Скверны, усиливающая стойкость и проворство.|n|n"
        "|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+70|cffced4da.|n- Скорость передвижения: |cffc8e087+40|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМорской варан|cffced4da|n- |cffa9c7deМирмидон|cffced4da|n- |cffa9c7deСирена|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # R092: Опутывание (1 уровень, hotkey S)
    wts_updates[40385] = "|cffe4cfa3Опутывание|r"
    wts_updates[40386] = "|cffe4cfa3Опутывание|r (|cffffffffS|r)"
    wts_updates[14645] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Даёт мирмидонам способность бросать сеть, приковывая противника к земле и опуская летающие цели.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМирмидон|cffced4da.|r"
    )

    # R093: Магия воды (6 уровней, hotkey D)
    w_name_sids2 = [14659, 14654, 14655, 14656, 14657, 14658]
    w_tip_sids2 = [14660, 14661, 14662, 14663, 14664, 14665]
    w_ub_sids2 = [16042, 16043, 16044, 16045, 16046, 16047]
    for lvl in range(1, 7):
        wts_updates[w_name_sids2[lvl-1]] = f"|cffe4cfa3Магия воды — уровень {lvl}|r"
        wts_updates[w_tip_sids2[lvl-1]] = f"|cffe4cfa3Магия воды — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[w_ub_sids2[lvl-1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает ранг сирен наг, раскрывая высшие секреты управления стихией воды.|n|n"
            f"|cffa6afb8Бонусы:|cffced4da|n- Запас здоровья: |cffc8e087+{lvl * 70}|cffced4da.|n- Запас маны: |cffc8e087+{lvl * 50}|cffced4da.|n- Восстановление маны: |cffc8e087+{round(lvl * 0.3, 1)}|cffced4da ед./сек.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСирена|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R097: Улучшенные топоры (6 уровней, hotkey Q)
    wts_updates[14745] = "|cffe4cfa3Улучшенные топоры — уровень 1|r"
    wts_updates[14749] = "|cffe4cfa3Улучшенные топоры — уровень 1|r (|cffffffffQ|r)"
    wts_updates[14751] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой строителями древесины на |cffc8e087+10|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
    )
    wts_updates[14746] = "|cffe4cfa3Улучшенные топоры — уровень 2|r"
    wts_updates[14750] = "|cffe4cfa3Улучшенные топоры — уровень 2|r (|cffffffffQ|r)"
    wts_updates[14752] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой строителями древесины на |cffc8e087+20|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
    )
    wts_updates[14755] = "|cffe4cfa3Улучшенные топоры — уровень 3|r"
    wts_updates[14756] = "|cffe4cfa3Улучшенные топоры — уровень 3|r (|cffffffffQ|r)"
    wts_updates[14757] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой строителями древесины на |cffc8e087+30|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
    )
    wts_updates[18382] = "|cffe4cfa3Улучшенные топоры — уровень 4|r"
    wts_updates[20837] = "|cffe4cfa3Улучшенные топоры — уровень 4|r (|cffffffffQ|r)"
    wts_updates[20846] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой строителями древесины на |cffc8e087+40|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
    )
    wts_updates[18383] = "|cffe4cfa3Улучшенные топоры — уровень 5|r"
    wts_updates[20844] = "|cffe4cfa3Улучшенные топоры — уровень 5|r (|cffffffffQ|r)"
    wts_updates[20847] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой строителями древесины на |cffc8e087+50|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
    )
    wts_updates[19466] = "|cffe4cfa3Улучшенные топоры — уровень 6|r"
    wts_updates[20845] = "|cffe4cfa3Улучшенные топоры — уровень 6|r (|cffffffffQ|r)"
    wts_updates[20848] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой строителями древесины на |cffc8e087+60|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтроитель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
    )

    # R098: Владение Скверной (2 уровня, hotkey A)
    wts_updates[14815] = "|cffe4cfa3Владение Скверной — уровень 1|r"
    wts_updates[14816] = "|cffe4cfa3Владение Скверной — уровень 1|r (|cffffffffA|r)"
    wts_updates[14809] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Раскрывает боевую мощь покоренных демонов, обучая их способностям «Ярость демон-зверя» и «Острые клинки».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПокоренный демон|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[14810] = "|cffe4cfa3Владение Скверной — уровень 2|r"
    wts_updates[14817] = "|cffe4cfa3Владение Скверной — уровень 2|r (|cffffffffA|r)"
    wts_updates[14822] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно раскрывает потенциал покоренных демонов, усиливая их боевые навыки.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПокоренный демон|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # R07H: Маркер выбора расы «Иллидари» (1 уровень)
    wts_updates[9219] = "|cffe4cfa3Иллидари|r"
    wts_updates[9220] = "|cffe4cfa3Иллидари|r"
    wts_updates[9444] = "|cffa6afb8РАСА:|cffced4da Войско, созданное и обученное Иллиданом Яростью Бури из преданных последователей для беспощадной войны против Пылающего Легиона.|r"

    # R0KZ: Маркер «Иллидари или Наги» (1 уровень)
    wts_updates[5721] = "|cffe4cfa3Иллидари или Наги|r"
    wts_updates[9416] = "|cffe4cfa3Иллидари или Наги|r"
    wts_updates[12518] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Иллидари или Нагам.|r"

    # R0L0: Маркер «Эльфы Крови или Иллидари» (1 уровень)
    wts_updates[12039] = "|cffe4cfa3Эльфы Крови или Иллидари|r"
    wts_updates[12062] = "|cffe4cfa3Эльфы Крови или Иллидари|r"
    wts_updates[20115] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Эльфам Крови или Иллидари.|r"

    print(f"Total planned WTS updates: {len(wts_updates)}")

    # Verify that all target string IDs exist in war3map.wts
    missing_sids = [sid for sid in wts_updates if sid not in wts]
    if missing_sids:
        raise ValueError(f"Missing WTS string IDs: {missing_sids}")
    print("All string IDs exist in current war3map.wts!")

    # Verify style invariants across all new values
    style_violations = []
    color_tag_re = re.compile(r"\|c[0-9a-fA-F]{8}")
    for sid, val in wts_updates.items():
        # Check that if color tag is opened, the string ends with |r (or has at least one |r)
        has_color = bool(color_tag_re.search(val))
        has_reset = "|r" in val
        if has_color and not has_reset:
            style_violations.append(f"STRING {sid}: opened color tag without any |r reset: {repr(val)}")
        # Check for malformed color tags
        malformed = re.findall(r"\|c[^f\r\n]{1,7}[^0-9a-fA-F]", val)
        if malformed:
            style_violations.append(f"STRING {sid}: potential malformed color tag: {malformed}")
        # Check trailing \n or spaces
        if val.endswith("\n") or val.endswith("\r") or val.endswith("|n"):
            style_violations.append(f"STRING {sid}: unwanted trailing newline")
        # Check command verbs in short tips
        for verb in ["Построить ", "Обучить ", "Призвать ", "Исследовать ", "Улучшить до "]:
            if val.startswith(verb) or f">{verb}" in val:
                style_violations.append(f"STRING {sid}: contains forbidden command verb '{verb}': {val[:40]}")

    if style_violations:
        print("Style violations found:")
        for sv in style_violations:
            print("  ", sv)
        raise ValueError("Style check failed!")
    print("All style invariants passed 100%!")

    # Save master plan JSON
    plan_data = {
        "race": "Illidari",
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A0OK"],
            "buildings": ["h0E9", "h0EA", "h0EB", "h0EC", "h0ED", "h0EE", "h0EF", "h0EG", "h0EH", "h0EM", "h0EN", "o01C", "h011"],
            "units": ["h0EI", "h0EJ", "o01A", "o01B", "o019", "h0EK", "h0EL", "n02O", "n02M", "n02N", "h04Y", "h04Z", "h050"],
            "heroes": ["H043", "E01W", "E024", "E025"],
            "upgrades": ["R08W", "R08T", "R08U", "R08V", "R08X", "R096", "R099", "R09A", "R09B", "R08Y", "R091", "R095", "R08Z", "R090", "R094", "R092", "R093", "R097", "R098", "R07H", "R0KZ", "R0L0"],
            "abilities": [
                "AHfs", "AHbn", "AHdr", "AHpx", "AEmb", "AEim", "AEev", "A0NZ",
                "A0UV", "A0NJ", "A0NS", "A0NU", "A0NF", "A0NX", "A0NW", "A0NV",
                "A0O2", "A0O5", "A0OH", "A0OG", "A1GU", "A0OF", "A0OE", "A0O1", "A0O0",
                "A048", "A1KL", "A1KO", "A0NI", "A0NT", "A0NY",
                "A0NO", "A0NM", "A0NP", "A0NK", "A0NR", "A0NL", "A0NQ", "A0NN"
            ]
        }
    }

    (folder / "illidari_plan.json").write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Plan saved to {folder / 'illidari_plan.json'}")

if __name__ == "__main__":
    main()
