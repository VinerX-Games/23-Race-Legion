# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Nerubs race (Race 21)."""
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
    # 1. RACE SELECTION: A0HT, R07N
    # =========================================================================
    # A0HT
    wts_updates[38926] = "|cffe4cfa3Нерубы|r"
    wts_updates[38927] = "|cffe4cfa3Нерубы|r (|cffffffffW|r)"
    wts_updates[35195] = (
        "|cffa6afb8РАСА:|cffced4da Древняя подземная цивилизация разумных арахноидов Нордскола, повелевающих ядами, паутиной и роем.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Wrath of the Lich King»|r|n|n"
        "|cffced4daНерубы — древняя раса высокоинтеллектуальных инсектоидов-арахнидов, чья великая империя Азжол-Неруб тысячелетиями "
        "простиралась под ледяными просторами Нордскола. Владея секретами алхимии ядов, паутинных ловушек и подземного строительства, "
        "нерубианцы возводят коконы, связывают укрепления туннелями и направляют на врагов легионы бронированных воинов, пророков и свирепых лордов роя.|r"
    )
    checks_def.append({"type": "ability", "id": "A0HT", "field": "name", "expected": wts_updates[38926]})
    checks_def.append({"type": "ability", "id": "A0HT", "field": "tip1", "expected": wts_updates[38927]})
    checks_def.append({"type": "ability", "id": "A0HT", "field": "ubertip1", "expected": wts_updates[35195]})

    # Marker: R07N
    wts_updates[10679] = "|cffe4cfa3Нерубы|r"
    wts_updates[10680] = "|cffe4cfa3Нерубы|r"
    wts_updates[20121] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к королевству Нерубов (Азжол-Неруб).|r"
    checks_def.append({"type": "upgrade", "id": "R07N", "field": "name1", "expected": wts_updates[10679]})
    checks_def.append({"type": "upgrade", "id": "R07N", "field": "tip1", "expected": wts_updates[10680]})
    checks_def.append({"type": "upgrade", "id": "R07N", "field": "ubertip1", "expected": wts_updates[20121]})

    # =========================================================================
    # 2. BUILDINGS (12 buildings)
    # =========================================================================
    # h0CO: Залы Нерубов (Q)
    wts_updates[10299] = "|cffe4cfa3Залы Нерубов|r"
    wts_updates[10300] = "|cffe4cfa3Залы Нерубов|r (|cffffffffQ|r)"
    wts_updates[13023] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Нерубов первой ступени. Обеспечивает запас пищи и добычу ресурсов.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deПалаты Нерубов|cffced4da: открывает доступ к передовым сооружениям и технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CO", "field": "name", "expected": wts_updates[10299]})
    checks_def.append({"type": "unit", "id": "h0CO", "field": "tip", "expected": wts_updates[10300]})
    checks_def.append({"type": "unit", "id": "h0CO", "field": "ubertip", "expected": wts_updates[13023]})

    # h0CP: Палаты Нерубов (Z)
    wts_updates[10302] = "|cffe4cfa3Палаты Нерубов|r"
    wts_updates[10303] = "|cffe4cfa3Палаты Нерубов|r (|cffffffffZ|r)"
    wts_updates[20412] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Нерубов второй ступени. Существенно увеличивает запас пищи.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКрепость Нерубов|cffced4da: открывает доступ к высшим технологиям и защите столицы.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CP", "field": "name", "expected": wts_updates[10302]})
    checks_def.append({"type": "unit", "id": "h0CP", "field": "tip", "expected": wts_updates[10303]})
    checks_def.append({"type": "unit", "id": "h0CP", "field": "ubertip", "expected": wts_updates[20412]})

    # h0CQ: Крепость Нерубов (Z)
    wts_updates[10305] = "|cffe4cfa3Крепость Нерубов|r"
    wts_updates[15181] = "|cffe4cfa3Крепость Нерубов|r (|cffffffffZ|r)"
    wts_updates[20416] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Нерубов третьей ступени. Обеспечивает максимальный запас пищи и защиту королевства.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CQ", "field": "name", "expected": wts_updates[10305]})
    checks_def.append({"type": "unit", "id": "h0CQ", "field": "tip", "expected": wts_updates[15181]})
    checks_def.append({"type": "unit", "id": "h0CQ", "field": "ubertip", "expected": wts_updates[20416]})

    # h0CR: Казармы Нерубов (W)
    wts_updates[10308] = "|cffe4cfa3Казармы Нерубов|r"
    wts_updates[10309] = "|cffe4cfa3Казармы Нерубов|r (|cffffffffW|r)"
    wts_updates[13072] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает базовые боевые силы армии Нерубов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМолодой неруб|cffced4da: быстрый лёгкий боец ближнего боя.|n"
        "- |cffa9c7deВоин Нерубов|cffced4da: стрелок дальнего боя, способный сжигать ману цели.|n"
        "- |cffa9c7deЯдовитый Неруб|cffced4da: стрелок поддержки, отравляющий атакованные цели.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deШипастый панцирь|cffced4da|n"
        "- |cffa9c7deЯд нерубов|cffced4da|n"
        "- |cffa9c7deМутации Ядовитого неруба|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CR", "field": "name", "expected": wts_updates[10308]})
    checks_def.append({"type": "unit", "id": "h0CR", "field": "tip", "expected": wts_updates[10309]})
    checks_def.append({"type": "unit", "id": "h0CR", "field": "ubertip", "expected": wts_updates[13072]})

    # h0CS: Хранилище (E)
    wts_updates[10311] = "|cffe4cfa3Хранилище|r"
    wts_updates[10312] = "|cffe4cfa3Хранилище|r (|cffffffffE|r)"
    wts_updates[13027] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит складом древесины и центром генетических мутаций всей расы Нерубов.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deСильные передние конечности|cffced4da|n"
        "- |cffa9c7deБроня туловища|cffced4da|n"
        "- |cffa9c7deБроня чрева|cffced4da|n"
        "- |cffa9c7deМутация Панциря|cffced4da|n"
        "- |cffa9c7deМутация крови|cffced4da|n"
        "- |cffa9c7deМутация здоровья|cffced4da|n"
        "- |cffa9c7deМутация конечностей|cffced4da|n"
        "- |cffa9c7deМутация нерубов|cffced4da|n"
        "- |cffa9c7deУлучшенные инструменты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CS", "field": "name", "expected": wts_updates[10311]})
    checks_def.append({"type": "unit", "id": "h0CS", "field": "tip", "expected": wts_updates[10312]})
    checks_def.append({"type": "unit", "id": "h0CS", "field": "ubertip", "expected": wts_updates[13027]})

    # h0CT: Храм Нерубов (R)
    wts_updates[10317] = "|cffe4cfa3Храм Нерубов|r"
    wts_updates[10318] = "|cffe4cfa3Храм Нерубов|r (|cffffffffR|r)"
    wts_updates[13029] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает специализированных и тяжёлых воинов подземного роя.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deКисло-плюй|cffced4da: кислотный штурмовик, внедряющий паразитов.|n"
        "- |cffa9c7deГлубинный Неруб|cffced4da: мутировавший боец с хаотической атакой.|n"
        "- |cffa9c7deНерубский броненосец|cffced4da: сверхтяжёлый бронированный защитник.|n"
        "- |cffa9c7deНеруб Страж|cffced4da: элитный командир с усиливающей аурой.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУсилить Конечности|cffced4da|n"
        "- |cffa9c7deКомандирская аура|cffced4da|n"
        "- |cffa9c7deТолстый Панцирь|cffced4da|n"
        "- |cffa9c7deПаучья слизь|cffced4da|n"
        "- |cffa9c7deСильные конечности|cffced4da|n"
        "- |cffa9c7deМутация ДНК ядов|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CT", "field": "name", "expected": wts_updates[10317]})
    checks_def.append({"type": "unit", "id": "h0CT", "field": "tip", "expected": wts_updates[10318]})
    checks_def.append({"type": "unit", "id": "h0CT", "field": "ubertip", "expected": wts_updates[13029]})

    # h0CU: Паучий Алтарь (S)
    wts_updates[10320] = "|cffe4cfa3Паучий Алтарь|r"
    wts_updates[10321] = "|cffe4cfa3Паучий Алтарь|r (|cffffffffS|r)"
    checks_def.append({"type": "unit", "id": "h0CU", "field": "name", "expected": wts_updates[10320]})
    checks_def.append({"type": "unit", "id": "h0CU", "field": "tip", "expected": wts_updates[10321]})

    # h0CV: Святилище Нерубов (D)
    wts_updates[10323] = "|cffe4cfa3Святилище Нерубов|r"
    wts_updates[10324] = "|cffe4cfa3Святилище Нерубов|r (|cffffffffD|r)"
    wts_updates[13030] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель магов и мастеров паутины Нерубов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deНеруб Лекарь|cffced4da: маг поддержки с исцелением и щитом.|n"
        "- |cffa9c7deВязальщик|cffced4da: чародей паутины, связывающий и замедляющий врагов.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗнания Нерубов|cffced4da|n"
        "- |cffa9c7deЯдовитый щит|cffced4da|n"
        "- |cffa9c7deМастерство плетения|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CV", "field": "name", "expected": wts_updates[10323]})
    checks_def.append({"type": "unit", "id": "h0CV", "field": "tip", "expected": wts_updates[10324]})
    checks_def.append({"type": "unit", "id": "h0CV", "field": "ubertip", "expected": wts_updates[13030]})

    # h0GH: Туннель нерубов (F)
    wts_updates[19368] = "|cffe4cfa3Туннель нерубов|r"
    wts_updates[19370] = "|cffe4cfa3Туннель нерубов|r (|cffffffffF|r)"
    wts_updates[19366] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подземный ход сообщения Нерубов. Позволяет связывать две точки карты и мгновенно перемещать войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0GH", "field": "name", "expected": wts_updates[19368]})
    checks_def.append({"type": "unit", "id": "h0GH", "field": "tip", "expected": wts_updates[19370]})
    checks_def.append({"type": "unit", "id": "h0GH", "field": "ubertip", "expected": wts_updates[19366]})

    # lorE: Кокон Лорда (Q)
    wts_updates[37973] = "|cffe4cfa3Кокон Лорда|r"
    wts_updates[37974] = "|cffe4cfa3Кокон Лорда|r (|cffffffffQ|r)"
    wts_updates[31848] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Особый инкубационный кокон. Через |cffffffff60|cffced4da сек. созревает и порождает могучего |cffa9c7deНеруба Лорда|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "lorE", "field": "name", "expected": wts_updates[37973]})
    checks_def.append({"type": "unit", "id": "lorE", "field": "tip", "expected": wts_updates[37974]})
    checks_def.append({"type": "unit", "id": "lorE", "field": "ubertip", "expected": wts_updates[31848]})

    # u019: Кокон (Q)
    wts_updates[10296] = "|cffe4cfa3Кокон|r"
    wts_updates[10297] = "|cffe4cfa3Кокон|r (|cffffffffQ|r)"
    wts_updates[21249] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовая основа для возведения любых сооружений Нерубов. Даёт лимит пищи и доход.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+30|cffced4da золота каждые |cffffffff25|cffced4da сек.|n|n"
        "|cffa6afb8Мутирует в:|cffced4da любое здание Нерубов.|r"
    )
    checks_def.append({"type": "unit", "id": "u019", "field": "name", "expected": wts_updates[10296]})
    checks_def.append({"type": "unit", "id": "u019", "field": "tip", "expected": wts_updates[10297]})
    checks_def.append({"type": "unit", "id": "u019", "field": "ubertip", "expected": wts_updates[21249]})

    # u01A: Башня Оплетения (A)
    wts_updates[10314] = "|cffe4cfa3Башня Оплетения|r"
    wts_updates[10315] = "|cffe4cfa3Башня Оплетения|r (|cffffffffA|r)"
    wts_updates[13028] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Защитное оборонительное сооружение Нерубов. Опутывает врагов паутиной и поражает цели на расстоянии.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01A", "field": "name", "expected": wts_updates[10314]})
    checks_def.append({"type": "unit", "id": "u01A", "field": "tip", "expected": wts_updates[10315]})
    checks_def.append({"type": "unit", "id": "u01A", "field": "ubertip", "expected": wts_updates[13028]})

    # =========================================================================
    # 3. UNITS (15 units)
    # =========================================================================
    # h0BE: Постройщик (Q)
    wts_updates[10605] = "|cffe4cfa3Постройщик|r"
    wts_updates[10610] = "|cffe4cfa3Постройщик|r (|cffffffffQ|r)"
    wts_updates[6459] = (
        "|cffa6afb8ЮНИТ:|cffced4da Рабочий нерубов. Плетёт коконы, ремонтирует здания, собирает древесину и добывает золото.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНебольшой скачок|cffced4da: мгновенный телепорт на короткое расстояние.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BE", "field": "name", "expected": wts_updates[10605]})
    checks_def.append({"type": "unit", "id": "h0BE", "field": "tip", "expected": wts_updates[10610]})
    checks_def.append({"type": "unit", "id": "h0BE", "field": "ubertip", "expected": wts_updates[6459]})

    # u01J: Молодой неруб (Q)
    wts_updates[10359] = "|cffe4cfa3Молодой неруб|r"
    wts_updates[10360] = "|cffe4cfa3Молодой неруб|r (|cffffffffQ|r)"
    wts_updates[12544] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый легковооружённый боец ближнего боя. Эффективен в массовых атаках на ранних этапах игры.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deШипастый панцирь|cffced4da: повышает защиту и отражает получаемый урон.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01J", "field": "name", "expected": wts_updates[10359]})
    checks_def.append({"type": "unit", "id": "u01J", "field": "tip", "expected": wts_updates[10360]})
    checks_def.append({"type": "unit", "id": "u01J", "field": "ubertip", "expected": wts_updates[12544]})

    # u01G: Воин Нерубов (E)
    wts_updates[10368] = "|cffe4cfa3Воин Нерубов|r"
    wts_updates[10369] = "|cffe4cfa3Воин Нерубов|r (|cffffffffE|r)"
    wts_updates[4455] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основной стрелок армии Нерубов. Атакует цели колющими снарядами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСожжение|cffced4da: каждая атака сжигает ману цели и наносит дополнительный урон.|n"
        "- |cffa9c7deПаутина|cffced4da: при атаке замедляет скорость атаки и передвижения врага.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01G", "field": "name", "expected": wts_updates[10368]})
    checks_def.append({"type": "unit", "id": "u01G", "field": "tip", "expected": wts_updates[10369]})
    checks_def.append({"type": "unit", "id": "u01G", "field": "ubertip", "expected": wts_updates[4455]})

    # u01F: Ядовитый Неруб (W)
    wts_updates[10339] = "|cffe4cfa3Ядовитый Неруб|r"
    wts_updates[7610] = "|cffe4cfa3Ядовитый Неруб|r (|cffffffffW|r)"
    wts_updates[4454] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стрелок поддержки дальнего боя. Отравляет поражённые цели смертоносным ядом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯд нерубов|cffced4da: наносит периодический урон отравленным врагам.|n"
        "- |cffa9c7deАнтимагический панцирь|cffced4da: даёт защиту от заклинаний после мутации.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01F", "field": "name", "expected": wts_updates[10339]})
    checks_def.append({"type": "unit", "id": "u01F", "field": "tip", "expected": wts_updates[7610]})
    checks_def.append({"type": "unit", "id": "u01F", "field": "ubertip", "expected": wts_updates[4454]})

    # u01C: Кисло-плюй (Q)
    wts_updates[10366] = "|cffe4cfa3Кисло-плюй|r"
    wts_updates[10367] = "|cffe4cfa3Кисло-плюй|r (|cffffffffQ|r)"
    wts_updates[986] = (
        "|cffa6afb8ЮНИТ:|cffced4da Ударный передовой боец роя. Плюётся едкой кислотой и заражает врагов паразитами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПаучий Паразит|cffced4da: заражает врага паразитом, порождающим паучка при гибели цели.|n"
        "- |cffa9c7deПарализующий яд|cffced4da: шанс оглушить врага и нанести дополнительный урон.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01C", "field": "name", "expected": wts_updates[10366]})
    checks_def.append({"type": "unit", "id": "u01C", "field": "tip", "expected": wts_updates[10367]})
    checks_def.append({"type": "unit", "id": "u01C", "field": "ubertip", "expected": wts_updates[986]})

    # u01K: Глубинный Неруб (W)
    wts_updates[10362] = "|cffe4cfa3Глубинный Неруб|r"
    wts_updates[10363] = "|cffe4cfa3Глубинный Неруб|r (|cffffffffW|r)"
    wts_updates[5518] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мутировавший тяжелобронированный воин с типом атаки «Хаос». Проламывает любую броню.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deШипастый панцирь|cffced4da: усиливает защиту и отражает урон ближнего боя.|n"
        "- |cffa9c7deПаутина|cffced4da: замедляет скорость атаки и перемещения цели.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01K", "field": "name", "expected": wts_updates[10362]})
    checks_def.append({"type": "unit", "id": "u01K", "field": "tip", "expected": wts_updates[10363]})
    checks_def.append({"type": "unit", "id": "u01K", "field": "ubertip", "expected": wts_updates[5518]})

    # u01B: Нерубский броненосец (R)
    wts_updates[10327] = "|cffe4cfa3Нерубский броненосец|r"
    wts_updates[11993] = "|cffe4cfa3Нерубский броненосец|r (|cffffffffR|r)"
    wts_updates[963] = (
        "|cffa6afb8ЮНИТ:|cffced4da Сверхтяжёлый штурмовой танк Нерубов, защищённый толстым хитиновым панцирем.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deТолстый Панцирь|cffced4da: поглощает значительную часть входящего урона.|n"
        "- |cffa9c7deОстрые конечности|cffced4da: шанс нанести сокрушительный критический удар.|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает урон ближнего боя в атакующих.|n"
        "- |cffa9c7deПаутина|cffced4da: замедляет скорость цели при атаке.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01B", "field": "name", "expected": wts_updates[10327]})
    checks_def.append({"type": "unit", "id": "u01B", "field": "tip", "expected": wts_updates[11993]})
    checks_def.append({"type": "unit", "id": "u01B", "field": "ubertip", "expected": wts_updates[963]})

    # u01I: Неруб Страж (E)
    wts_updates[10348] = "|cffe4cfa3Неруб Страж|r"
    wts_updates[12542] = "|cffe4cfa3Неруб Страж|r (|cffffffffE|r)"
    wts_updates[4457] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный воин-командир дальнего боя. Вдохновляет окружающих союзников боевой аурой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКомандирская аура|cffced4da: повышает урон от атак находящихся рядом союзников.|n"
        "- |cffa9c7deПаутина|cffced4da: замедляет скорость поражённых целей.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01I", "field": "name", "expected": wts_updates[10348]})
    checks_def.append({"type": "unit", "id": "u01I", "field": "tip", "expected": wts_updates[12542]})
    checks_def.append({"type": "unit", "id": "u01I", "field": "ubertip", "expected": wts_updates[4457]})

    # u01H: Неруб Лекарь (Q)
    wts_updates[10345] = "|cffe4cfa3Неруб Лекарь|r"
    wts_updates[12540] = "|cffe4cfa3Неруб Лекарь|r (|cffffffffQ|r)"
    wts_updates[4456] = (
        "|cffa6afb8ЮНИТ:|cffced4da Магический лекарь и защитник армии Нерубов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deИсцеление|cffced4da: восстанавливает здоровье раненым союзникам.|n"
        "- |cffa9c7deЯдовитый щит|cffced4da: окружает цель ядовитым облаком, ранящим врагов вокруг.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты чар и наносит урон призванным существам.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01H", "field": "name", "expected": wts_updates[10345]})
    checks_def.append({"type": "unit", "id": "u01H", "field": "tip", "expected": wts_updates[12540]})
    checks_def.append({"type": "unit", "id": "u01H", "field": "ubertip", "expected": wts_updates[4456]})

    # u01D: Вязальщик (W)
    wts_updates[4003] = "|cffe4cfa3Вязальщик|r"
    wts_updates[6798] = "|cffe4cfa3Вязальщик|r (|cffffffffW|r)"
    wts_updates[2613] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг-паутинник дальнего боя. Контролирует перемещение врагов и ускоряет союзников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКомок паутины|cffced4da: оглушает цель и наносит урон.|n"
        "- |cffa9c7deПаутина|cffced4da: создаёт поле паутины, ускоряющее союзные войска.|n"
        "- |cffa9c7deБритвенно-острая паутина|cffced4da: сковывает цель корнями из паутины и наносит периодический урон.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01D", "field": "name", "expected": wts_updates[4003]})
    checks_def.append({"type": "unit", "id": "u01D", "field": "tip", "expected": wts_updates[6798]})
    checks_def.append({"type": "unit", "id": "u01D", "field": "ubertip", "expected": wts_updates[2613]})

    # u01T: Неруб паразит (Q)
    wts_updates[10414] = "|cffe4cfa3Неруб паразит|r"
    wts_updates[10415] = "|cffe4cfa3Неруб паразит|r (|cffffffffQ|r)"
    wts_updates[5646] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маленький арахнид, порождённый способностью «Паучий Паразит».|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deШипастый панцирь|cffced4da: отражает часть урона ближнего боя.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01T", "field": "name", "expected": wts_updates[10414]})
    checks_def.append({"type": "unit", "id": "u01T", "field": "tip", "expected": wts_updates[10415]})
    checks_def.append({"type": "unit", "id": "u01T", "field": "ubertip", "expected": wts_updates[5646]})

    # u01E: Пророк Нерубов (E)
    wts_updates[10336] = "|cffe4cfa3Пророк Нерубов|r"
    wts_updates[10337] = "|cffe4cfa3Пророк Нерубов|r (|cffffffffE|r)"
    wts_updates[3198] = (
        "|cffa6afb8ЮНИТ:|cffced4da Подземный жрец и прорицатель роя. Опутывает летающих врагов сетью и поднимает мертвецов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПаутина|cffced4da: притягивает воздушную цель к земле.|n"
        "- |cffa9c7deВоскрешение мертвых|cffced4da: поднимает скелетов из павших тел.|n"
        "- |cffa9c7deРазложение трупа|cffced4da: регулирует баланс здоровья и урона нежити.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u01E", "field": "name", "expected": wts_updates[10336]})
    checks_def.append({"type": "unit", "id": "u01E", "field": "tip", "expected": wts_updates[10337]})
    checks_def.append({"type": "unit", "id": "u01E", "field": "ubertip", "expected": wts_updates[3198]})

    # lord & nq01: Неруб Лорд
    wts_updates[37571] = "|cffe4cfa3Неруб Лорд|r"
    wts_updates[29729] = "|cffe4cfa3Неруб Лорд|r"
    checks_def.append({"type": "unit", "id": "lord", "field": "name", "expected": wts_updates[37571]})
    checks_def.append({"type": "unit", "id": "nq01", "field": "name", "expected": wts_updates[29729]})

    # =========================================================================
    # 4. HEROES (4 heroes)
    # =========================================================================
    # U01U: Пророк (Гор'аман, Int/Ranged, Z)
    wts_updates[7233] = "|cffe4cfa3Пророк|r"
    wts_updates[7234] = "|cffa9c7deГор'аман|r"
    wts_updates[7236] = "|cffe4cfa3Пророк|r (|cffffffffZ|r)"
    wts_updates[31723] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Мудрый нерубианский провидец, повелевающий ядовитыми испарениями, нитями судьбы и оплетением врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСтолб яда|cffced4da: создаёт столб яда, наносящий урон по площади.|n"
        "- |cffa9c7deЭссенция яда|cffced4da: исцеляет союзников живительной эссенцией.|n"
        "- |cffa9c7deДар пророка|cffced4da: даёт шанс уклониться от вражеских атак.|n"
        "- |cffa9c7deОплетение|cffced4da: заключает врагов в коконы, оглушая и нанося урон.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U01U", "field": "name", "expected": wts_updates[7233]})
    checks_def.append({"type": "unit", "id": "U01U", "field": "propernames", "expected": wts_updates[7234]})
    checks_def.append({"type": "unit", "id": "U01U", "field": "tip", "expected": wts_updates[7236]})
    checks_def.append({"type": "unit", "id": "U01U", "field": "ubertip", "expected": wts_updates[31723]})

    # U01V: Паучий лорд (Str/Melee, X)
    wts_updates[9411] = "|cffe4cfa3Паучий лорд|r"
    wts_updates[9428] = "|cffa9c7deАнуб'арак|r"
    wts_updates[9429] = "|cffe4cfa3Паучий лорд|r (|cffffffffX|r)"
    wts_updates[31724] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могучий владыка старейшин нерубов. Сокрушает ряды врагов тяжёлыми клешнями, кровотечением и роем темной энергии.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deТемная стая|cffced4da: выпускает темную волну, поражающую врагов на прямой.|n"
        "- |cffa9c7deПоражающий удар|cffced4da: каждая атака оставляет кровоточащие раны.|n"
        "- |cffa9c7deКритический удар|cffced4da: даёт шанс нанести многократный урон при атаке.|n"
        "- |cffa9c7deАура метаморфоз|cffced4da: ускоряет передвижение и восстановление здоровья союзников.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U01V", "field": "name", "expected": wts_updates[9411]})
    checks_def.append({"type": "unit", "id": "U01V", "field": "propernames", "expected": wts_updates[9428]})
    checks_def.append({"type": "unit", "id": "U01V", "field": "tip", "expected": wts_updates[9429]})
    checks_def.append({"type": "unit", "id": "U01V", "field": "ubertip", "expected": wts_updates[31724]})

    # U01W: Высший Страж (Омун-ул, Agi/Ranged, C)
    wts_updates[11132] = "|cffe4cfa3Высший Страж|r"
    wts_updates[11135] = "|cffa9c7deОмун-ул|r"
    wts_updates[11136] = "|cffe4cfa3Высший Страж|r (|cffffffffC|r)"
    wts_updates[31725] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Древний хранитель врат Азжол-Неруба. Подбрасывает врагов шипами, плетёт боевые коконы и призывает рой саранчи.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПронзание|cffced4da: вздымает шипы из-под земли, оглушая врагов на линии.|n"
        "- |cffa9c7deСоздание кокона|cffced4da: создаёт коконы, из которых со временем появляются новые бойцы.|n"
        "- |cffa9c7deРассекающий удар|cffced4da: наносит урон нескольким врагам вокруг цели.|n"
        "- |cffa9c7deРой саранчи|cffced4da: призывает рой саранчи, кусающей врагов и исцеляющей героя.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffЛовкость|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U01W", "field": "name", "expected": wts_updates[11132]})
    checks_def.append({"type": "unit", "id": "U01W", "field": "propernames", "expected": wts_updates[11135]})
    checks_def.append({"type": "unit", "id": "U01W", "field": "tip", "expected": wts_updates[11136]})
    checks_def.append({"type": "unit", "id": "U01W", "field": "ubertip", "expected": wts_updates[31725]})

    # NERH: Королева Нерубов (Нер-мун, Legendary, Int/Ranged, Q)
    wts_updates[20984] = "|cffe4cfa3Королева Нерубов|r"
    wts_updates[29476] = "|cffa9c7deНер-мун|r"
    wts_updates[29519] = "|cffe4cfa3Королева Нерубов|r (|cffffffffQ|r)"
    wts_updates[29477] = "|cffe4cfa3Королева Нерубов|r"
    wts_updates[30218] = "|cffe4cfa3Королева Нерубов|r"
    wts_updates[30237] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарная правительница Азжол-Неруба. Ведёт свой народ в бой, сокрушая разум противников и порождая свирепых лордов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолна роя|cffced4da: выпускает волну низших нерубов, наносящую урон на пути.|n"
        "- |cffa9c7deПодавление|cffced4da: подавляет разум врага, запрещая применять чары и ослабляя атаку.|n"
        "- |cffa9c7deВоля королевы|cffced4da: аура, повышающая броню и регенерацию здоровья и маны союзников.|n"
        "- |cffa9c7deПородить лорда|cffced4da: создаёт кокон, из которого через минуту появляется Неруб Лорд.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "NERH", "field": "name", "expected": wts_updates[20984]})
    checks_def.append({"type": "unit", "id": "NERH", "field": "propernames", "expected": wts_updates[29476]})
    checks_def.append({"type": "unit", "id": "NERH", "field": "tip", "expected": wts_updates[29519]})
    checks_def.append({"type": "unit", "id": "NERH", "field": "awakentip", "expected": wts_updates[29477]})
    checks_def.append({"type": "unit", "id": "NERH", "field": "revivetip", "expected": wts_updates[30218]})
    checks_def.append({"type": "unit", "id": "NERH", "field": "ubertip", "expected": wts_updates[30237]})

    # =========================================================================
    # 5. UPGRADES (22 researches)
    # =========================================================================
    # R074 (6 lvls, Q): Сильные передние конечности
    r074_names = [10544, 10543, 10541, 10542, 10540, 10539]
    r074_tips = [10547, 10546, 10545, 10550, 10549, 10548]
    r074_ubs = [13923, 15289, 15290, 2009, 2010, 13229]
    for lvl in range(1, 7):
        wts_updates[r074_names[lvl - 1]] = f"|cffe4cfa3Сильные передние конечности — уровень {lvl}|r"
        wts_updates[r074_tips[lvl - 1]] = f"|cffe4cfa3Сильные передние конечности — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r074_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает силу ударов передних клешней, увеличивая урон от атак всех воинов Нерубов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем боевым единицам Нерубов.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        )

    # R075 (6 lvls, A): Броня туловища (melee armor)
    r075_names = [10554, 10555, 10556, 10559, 10558, 10557]
    r075_tips = [10560, 10561, 10562, 10565, 10564, 10563]
    r075_ubs = [18387, 18388, 18389, 18384, 18385, 18386]
    for lvl in range(1, 7):
        wts_updates[r075_names[lvl - 1]] = f"|cffe4cfa3Броня туловища — уровень {lvl}|r"
        wts_updates[r075_tips[lvl - 1]] = f"|cffe4cfa3Броня туловища — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r075_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наращивает прочные хитиновые пластины на туловище, усиливая броню бойцов ближнего боя.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМолодой неруб|cffced4da, |cffa9c7deНерубский броненосец|cffced4da, |cffa9c7deГлубинный Неруб|cffced4da, |cffa9c7deКисло-плюй|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        )

    # R076 (6 lvls, S): Броня чрева (ranged armor)
    r076_names = [10575, 10576, 10577, 10580, 10579, 10578]
    r076_tips = [10583, 10582, 10581, 10586, 10585, 10584]
    r076_ubs = [18393, 18394, 18395, 18390, 18391, 18392]
    for lvl in range(1, 7):
        wts_updates[r076_names[lvl - 1]] = f"|cffe4cfa3Броня чрева — уровень {lvl}|r"
        wts_updates[r076_tips[lvl - 1]] = f"|cffe4cfa3Броня чрева — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r076_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет уязвимое брюшко нерубианцев, повышая показатель защиты стрелков и заклинателей.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВоин Нерубов|cffced4da, |cffa9c7deЯдовитый Неруб|cffced4da, |cffa9c7deНеруб Страж|cffced4da, |cffa9c7deНеруб Лекарь|cffced4da, |cffa9c7deВязальщик|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        )

    # R070 (3 lvls, E): Мутация Панциря
    r070_names = [10477, 10479, 10480]
    r070_tips = [10478, 10481, 10482]
    r070_ubs = [18372, 18373, 18374]
    for lvl in range(1, 4):
        wts_updates[r070_names[lvl - 1]] = f"|cffe4cfa3Мутация Панциря — уровень {lvl}|r"
        wts_updates[r070_tips[lvl - 1]] = f"|cffe4cfa3Мутация Панциря — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[r070_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Генетическая трансформация, утолщающая наружный хитиновый скелет всех нерубов на |cffc8e087+{lvl * 2}|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем воинам армии Нерубов.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R06Z (3 lvls, R): Мутация крови
    r06z_names = [10470, 10472, 10473]
    r06z_tips = [10471, 10474, 10475]
    r06z_ubs = [18375, 18376, 18377]
    for lvl in range(1, 4):
        wts_updates[r06z_names[lvl - 1]] = f"|cffe4cfa3Мутация крови — уровень {lvl}|r"
        wts_updates[r06z_tips[lvl - 1]] = f"|cffe4cfa3Мутация крови — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[r06z_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Насыщает гемолимфу нерубов регенеративными токсинами, увеличивая скорость восстановления здоровья на |cffc8e087+0.3|cffced4da ед./сек.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем воинам армии Нерубов.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R071 (3 lvls, D): Мутация здоровья
    r071_names = [10484, 10486, 10487]
    r071_tips = [10485, 10488, 10489]
    r071_ubs = [18378, 18379, 18380]
    for lvl in range(1, 4):
        wts_updates[r071_names[lvl - 1]] = f"|cffe4cfa3Мутация здоровья — уровень {lvl}|r"
        wts_updates[r071_tips[lvl - 1]] = f"|cffe4cfa3Мутация здоровья — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[r071_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет жизненную силу органов нерубов, увеличивая базовый запас здоровья на |cffc8e087+{lvl * 25}|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем воинам армии Нерубов.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R072 (3 lvls, F): Мутация конечностей
    r072_names = [10491, 10493, 10494]
    r072_tips = [10492, 10495, 10496]
    r072_ubs = [18381, 18382, 18383]
    for lvl in range(1, 4):
        wts_updates[r072_names[lvl - 1]] = f"|cffe4cfa3Мутация конечностей — уровень {lvl}|r"
        wts_updates[r072_tips[lvl - 1]] = f"|cffe4cfa3Мутация конечностей — уровень {lvl}|r (|cffffffffF|r)"
        wts_updates[r072_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Удлиняет и облегчает лапы нерубов, повышая скорость передвижения на |cffc8e087+20|cffced4da и скорость боя на |cffc8e087+20%|cffced4da.|n|n"
            f"|cffe6c07bВнимание: исключает возможность исследования «Мутация нерубов».|r|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем воинам армии Нерубов.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R073 (3 lvls, C): Мутация нерубов
    r073_names = [10502, 10504, 10505]
    r073_tips = [10503, 10506, 10507]
    r073_ubs = [18368, 18369, 18370]
    for lvl in range(1, 4):
        bonus_pct = "30%" if lvl == 1 else "15%"
        wts_updates[r073_names[lvl - 1]] = f"|cffe4cfa3Мутация нерубов — уровень {lvl}|r"
        wts_updates[r073_tips[lvl - 1]] = f"|cffe4cfa3Мутация нерубов — уровень {lvl}|r (|cffffffffC|r)"
        wts_updates[r073_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Глубинная трансформация массы тела, увеличивающая максимальный запас здоровья нерубов на |cffc8e087+{bonus_pct}|cffced4da.|n|n"
            f"|cffe6c07bВнимание: исключает возможность исследования «Мутация конечностей».|r|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Всем воинам армии Нерубов.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R0DR (4 lvls, E): Улучшенные инструменты
    r0dr_names = [16897, 16901, 16904, 18220]
    r0dr_tips = [16898, 16902, 16905, 18221]
    r0dr_ubs = [16899, 16903, 16906, 18222]
    for lvl in range(1, 5):
        wts_updates[r0dr_names[lvl - 1]] = f"|cffe4cfa3Улучшенные инструменты — уровень {lvl}|r"
        wts_updates[r0dr_tips[lvl - 1]] = f"|cffe4cfa3Улучшенные инструменты — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[r0dr_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Затачивает клешни и жвала работников, увеличивая количество переносимой древесины на |cffc8e087+{lvl * 8}|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПостройщик|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/4|r."
        )

    # R077 (1 lvl, Z): Шипастый панцирь
    wts_updates[10596] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[10597] = "|cffe4cfa3Шипастый панцирь|r (|cffffffffZ|r)"
    wts_updates[18396] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Покрывает наружный панцирь воинов острыми шипами, увеличивая броню на |cffc8e087+2|cffced4da и отражая |cffc8e08715%|cffced4da урона ближнего боя.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМолодой неруб|cffced4da.|r"
    )

    # R078 (1 lvl, X): Яд нерубов
    wts_updates[10600] = "|cffe4cfa3Яд нерубов|r"
    wts_updates[10601] = "|cffe4cfa3Яд нерубов|r (|cffffffffX|r)"
    wts_updates[18397] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность заражать атакованные цели смертоносным токсином Нерубов.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЯдовитый Неруб|cffced4da.|r"
    )

    # R079 (3 lvls, C): Мутации Ядовитого неруба
    r079_names = [10604, 10609, 10757]
    r079_tips = [10608, 10611, 10759]
    r079_ubs = [10756, 10758, 10762]
    r079_desc = [
        "Увеличивает скорость перемещения Ядовитого неруба на |cffc8e087+30%|cffced4da.",
        "Увеличивает скорость перемещения Ядовитого неруба на |cffc8e087+30%|cffced4da и наделяет способностью |cffa9c7deАнтимагический панцирь|cffced4da.",
        "Увеличивает скорость перемещения Ядовитого неруба на |cffc8e087+30%|cffced4da, наделяет способностями |cffa9c7deАнтимагический панцирь|cffced4da и |cffa9c7deСожжение|cffced4da."
    ]
    for lvl in range(1, 4):
        wts_updates[r079_names[lvl - 1]] = f"|cffe4cfa3Мутации Ядовитого неруба — уровень {lvl}|r"
        wts_updates[r079_tips[lvl - 1]] = f"|cffe4cfa3Мутации Ядовитого неруба — уровень {lvl}|r (|cffffffffC|r)"
        wts_updates[r079_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da {r079_desc[lvl - 1]}|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЯдовитый Неруб|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # R07T (1 lvl, Q): Усилить Конечности
    wts_updates[10802] = "|cffe4cfa3Усилить Конечности|r"
    wts_updates[10803] = "|cffe4cfa3Усилить Конечности|r (|cffffffffQ|r)"
    wts_updates[18402] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет мышечные волокна лап, увеличивая скорость передвижения и силу удара в ближнем бою.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГлубинный Неруб|cffced4da, |cffa9c7deНерубский броненосец|cffced4da.|r"
    )

    # R07R (1 lvl, E): Командирская аура
    wts_updates[10785] = "|cffe4cfa3Командирская аура|r"
    wts_updates[10786] = "|cffe4cfa3Командирская аура|r (|cffffffffE|r)"
    wts_updates[18400] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Нерубов Стражей аурой полководца, повышающей урон окружающих союзных войск.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНеруб Страж|cffced4da.|r"
    )

    # R07S (1 lvl, X): Толстый Панцирь
    wts_updates[10792] = "|cffe4cfa3Толстый Панцирь|r"
    wts_updates[10793] = "|cffe4cfa3Толстый Панцирь|r (|cffffffffX|r)"
    wts_updates[18401] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наращивает сверхпрочный панцирь, уменьшающий получаемый урон от вражеских атак.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНерубский броненосец|cffced4da.|r"
    )

    # R07P (1 lvl, S): Паучья слизь
    wts_updates[10767] = "|cffe4cfa3Паучья слизь|r"
    wts_updates[10768] = "|cffe4cfa3Паучья слизь|r (|cffffffffS|r)"
    wts_updates[18398] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Покрывает Глубинного неруба прозрачной вязкой слизью, увеличивающей показатель брони.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГлубинный Неруб|cffced4da.|r"
    )

    # R07Q (1 lvl, Z): Сильные конечности
    wts_updates[10775] = "|cffe4cfa3Сильные конечности|r"
    wts_updates[10776] = "|cffe4cfa3Сильные конечности|r (|cffffffffZ|r)"
    wts_updates[18399] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Ускоряет передвижение и повышает скорость атаки Глубинного неруба.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГлубинный Неруб|cffced4da.|r"
    )

    # R07O (2 lvls, W): Мутация ДНК ядов
    r07o_names = [10760, 10764]
    r07o_tips = [10761, 10765]
    r07o_ubs = [18405, 18406]
    for lvl in range(1, 3):
        wts_updates[r07o_names[lvl - 1]] = f"|cffe4cfa3Мутация ДНК ядов — уровень {lvl}|r"
        wts_updates[r07o_tips[lvl - 1]] = f"|cffe4cfa3Мутация ДНК ядов — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[r07o_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Модифицирует ядовитые железы, увеличивая силу и продолжительность токсинов роя.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЯдовитый Неруб|cffced4da, |cffa9c7deКисло-плюй|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/2|r."
        )

    # R07U (2 lvls, A): Знания Нерубов
    r07u_names = [10778, 10811]
    r07u_tips = [10779, 10812]
    r07u_ubs = [18403, 18404]
    for lvl in range(1, 3):
        wts_updates[r07u_names[lvl - 1]] = f"|cffe4cfa3Знания Нерубов — уровень {lvl}|r"
        wts_updates[r07u_tips[lvl - 1]] = f"|cffe4cfa3Знания Нерубов — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r07u_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Нерубов Лекарей новым заклинаниям, увеличивает здоровье на |cffc8e087+25|cffced4da, запас маны на |cffc8e087+30%|cffced4da и регенерацию маны на |cffc8e087+40%|cffced4da.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНеруб Лекарь|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/2|r."
        )

    # R07V (1 lvl, Z): Ядовитый щит
    wts_updates[10816] = "|cffe4cfa3Ядовитый щит|r"
    wts_updates[10817] = "|cffe4cfa3Ядовитый щит|r (|cffffffffZ|r)"
    wts_updates[18407] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует Нерубу Лекарю способность окружать цель ядовитыми испарениями, ранящими врагов.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНеруб Лекарь|cffced4da.|r"
    )

    # R07W (3 lvls, S): Мастерство плетения
    r07w_names = [10823, 10827, 10830]
    r07w_tips = [10824, 10828, 10831]
    r07w_ubs = [18408, 18409, 18410]
    for lvl in range(1, 4):
        wts_updates[r07w_names[lvl - 1]] = f"|cffe4cfa3Мастерство плетения — уровень {lvl}|r"
        wts_updates[r07w_tips[lvl - 1]] = f"|cffe4cfa3Мастерство плетения — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r07w_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает мастерство управления паутиной Вязальщиков, повышая прочность нитей и силу заклинаний.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВязальщик|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r."
        )

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # A186: Подземные жители
    wts_updates[39035] = "|cffe4cfa3Подземные жители|r"
    wts_updates[39036] = "|cffe4cfa3Подземные жители|r"
    wts_updates[39037] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Расовая особенность Нерубов. У нерубов отсутствует исследование «Торговля», "
        "однако их здания сохраняют выработку дохода даже после улучшений.|r"
    )

    # A0TQ: Прокопать туннель (Q)
    wts_updates[10041] = "|cffe4cfa3Прокопать туннель|r"
    wts_updates[10042] = "|cffe4cfa3Прокопать туннель|r (|cffffffffQ|r)"
    wts_updates[10043] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Прокладывает подземный проход между двумя туннелями нерубов, "
        "позволяя мгновенно перебрасывать войска между ними.|r"
    )

    # A0I3: Небольшой скачок (C)
    wts_updates[26484] = "|cffe4cfa3Небольшой скачок|r"
    wts_updates[26476] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[26477] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит работника на небольшое расстояние.|r"
    wts_updates[10064] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[10976] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит работника на небольшое расстояние.|r"

    # A0HJ: Толстый Панцирь
    wts_updates[10460] = "|cffe4cfa3Толстый Панцирь|r"
    wts_updates[10461] = "|cffe4cfa3Толстый Панцирь|r"
    wts_updates[20587] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Массивные хитиновые наросты поглощают входящий физический урон от вражеских атак.|r"
    )

    # A0HD: Острые конечности
    wts_updates[10444] = "|cffe4cfa3Острые конечности|r"
    wts_updates[10445] = "|cffe4cfa3Острые конечности|r"

    # A0H9: Шипастый панцирь
    wts_updates[10389] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[10390] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[40051] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Острые хитиновые шипы повышают броню на |cffc8e087+2|cffced4da и отражают часть получаемого урона ближнего боя во врага.|r"
    )

    # A0H4: Паутина (замедление)
    wts_updates[10407] = "|cffe4cfa3Паутина|r"
    wts_updates[10408] = "|cffe4cfa3Паутина|r"
    wts_updates[15253] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При атаке опутывает цель липкими нитями, замедляя скорость передвижения на |cffe69a8d15%|cffced4da и скорость атаки на |cffe69a8d15%|cffced4da.|r"
    )
    wts_updates[2911] = "|cffe4cfa3Опутывание|r"
    wts_updates[3267] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки и перемещения атакованного врага.|r"

    # A0HC: Паучий Паразит (W)
    wts_updates[10436] = "|cffe4cfa3Паучий Паразит|r"
    wts_updates[10437] = "|cffe4cfa3Паучий Паразит|r (|cffffffffW|r)"
    wts_updates[20586] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Внедряет во врага смертоносного паразита, наносящего периодический урон. "
        "Если жертва погибает под действием эффекта, из её тела вылупляется молодой паучок.|r"
    )

    # A0HB: Парализующий яд
    wts_updates[10416] = "|cffe4cfa3Парализующий яд|r"
    wts_updates[10431] = "|cffe4cfa3Парализующий яд|r"

    # A0H7: Комок паутины (Q)
    wts_updates[10357] = "|cffe4cfa3Комок паутины|r"
    wts_updates[10364] = "|cffe4cfa3Комок паутины|r (|cffffffffQ|r)"
    wts_updates[10365] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает во врага плотный ком паутины, наносящий урон и оглушающий цель.|r"
    )

    # A0H5: Паутина (ускорение, W)
    wts_updates[10417] = "|cffe4cfa3Паутина|r"
    wts_updates[10429] = "|cffe4cfa3Паутина|r (|cffffffffW|r)"
    wts_updates[20585] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт в указанной области плотное полотно паутины, увеличивающее скорость передвижения союзных войск на |cffc8e087+50%|cffced4da.|r"
    )

    # A0H6: Бритвенно-острая паутина (E)
    wts_updates[10330] = "|cffe4cfa3Бритвенно-острая паутина|r"
    wts_updates[10331] = "|cffe4cfa3Бритвенно-острая паутина|r (|cffffffffE|r)"
    wts_updates[10342] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выплёвывает сеть бритвенно-острых нитей, которые сковывают врага на месте и наносят периодический урон.|r"
    )

    # A0BO: Разложение трупа
    wts_updates[8588] = "|cffe4cfa3Разложение трупа|r"
    wts_updates[8589] = "|cffe4cfa3Разложение трупа|r"
    wts_updates[8590] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет тление мертвой плоти, уменьшая запас здоровья, но увеличивая наносимый урон.|r"
    )

    # A0BS: Паутина (сеть)
    wts_updates[8599] = "|cffe4cfa3Паутина|r"
    wts_updates[8600] = "|cffe4cfa3Паутина|r (|cffffffffQ|r)"

    # A0BR: Воскрешение мертвых (R)
    wts_updates[42120] = "|cffe4cfa3Воскрешение мертвых|r"
    wts_updates[41512] = "|cffe4cfa3Воскрешение мертвых|r (|cffffffffR|r)"

    # A0HK: Антимагический панцирь
    wts_updates[10462] = "|cffe4cfa3Антимагический панцирь|r"
    wts_updates[10463] = "|cffe4cfa3Антимагический панцирь|r"

    # A0HA: Яд нерубов
    wts_updates[10392] = "|cffe4cfa3Яд нерубов|r"
    wts_updates[10405] = "|cffe4cfa3Яд нерубов|r"
    wts_updates[10406] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отравляет поражённую цель, нанося периодический урон в течение времени действия.|r"
    )

    # A0HF: Сожжение
    wts_updates[10448] = "|cffe4cfa3Сожжение|r"
    wts_updates[10449] = "|cffe4cfa3Сожжение|r"

    # A0HI: Ядовитый щит (W)
    wts_updates[10457] = "|cffe4cfa3Ядовитый щит|r"
    wts_updates[10458] = "|cffe4cfa3Ядовитый щит|r (|cffffffffW|r)"
    wts_updates[10459] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзника завесой ядовитых испарений, наносящих урон всем врагам поблизости.|r"
    )

    # A0HH: Рассеивание заклинаний (E)
    wts_updates[10455] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[10454] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffE|r)"

    # A0HG: Исцеление (Q)
    wts_updates[10450] = "|cffe4cfa3Исцеление|r"
    wts_updates[10451] = "|cffe4cfa3Исцеление|r (|cffffffffQ|r)"

    # A0HE: Командирская аура
    wts_updates[10446] = "|cffe4cfa3Командирская аура|r"
    wts_updates[10447] = "|cffe4cfa3Командирская аура|r"

    # NQ11: Особенности Лорда
    wts_updates[37924] = "|cffe4cfa3Особенности Лорда|r"
    wts_updates[37927] = "|cffe4cfa3Особенности Лорда|r"
    wts_updates[37926] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Синхронизирует атаки Неруба Лорда с волей Королевы Нерубов.|r"
    wts_updates[37928] = "|cffe4cfa3Особенности Лорда|r"
    wts_updates[37925] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Неруб Лорд применяет способность «Воля королевы» совместно с Королевой. "
        "Когда Королева поражает врага «Подавлением», стоящие рядом Лорды выжигают ману и наносят пропорциональный урон.|r"
    )

    # NQ04: Сменить дистанцию боя (Q)
    wts_updates[37963] = "|cffe4cfa3Сменить дистанцию боя|r"
    wts_updates[37964] = "|cffe4cfa3Сменить дистанцию боя|r (|cffffffffQ|r)"
    wts_updates[37965] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переключает боевой режим Неруба Лорда на ближний бой.|r"

    # Hero Spells: Prophet U01U
    # A0I7: Столб яда (Q)
    wts_updates[7241] = "|cffe4cfa3Столб яда|r"
    wts_updates[7242] = "|cffe4cfa3Столб яда|r (|cffffffffQ|r)"
    wts_updates[5870] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт ядовитый гейзер, наносящий концентрированный периодический урон в указанной области.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff45|cffced4da урона/сек. в первые 3 сек.|n"
        "|cffa6afb82-й уровень:|r |cffffffff80|cffced4da урона/сек. в первые 3 сек.|n"
        "|cffa6afb83-й уровень:|r |cffffffff110|cffced4da урона/сек. в первые 3 сек.|n"
        "|cffa6afb84-й уровень:|r |cffffffff140|cffced4da урона/сек. в первые 3 сек.|r"
    )
    a0i7_tips = [7455, 7456, 7457, 7239]
    a0i7_ubs = [7458, 7459, 7460, 5864]
    a0i7_dmg = [45, 80, 110, 140]
    for lvl in range(1, 5):
        wts_updates[a0i7_tips[lvl - 1]] = f"|cffe4cfa3Столб яда — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a0i7_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт столб яда, наносящий войскам в области |cffffffff{a0i7_dmg[lvl - 1]}|cffced4da урона/сек. в течение |cffffffff3|cffced4da сек., с последующим остаточным отравлением.|r"
        )

    # A0I9: Эссенция яда (W)
    wts_updates[8408] = "|cffe4cfa3Эссенция яда|r"
    wts_updates[8409] = "|cffe4cfa3Эссенция яда|r (|cffffffffW|r)"
    wts_updates[12454] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает сгусток целебного токсина, восполняющий здоровье союзникам в области.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087100|cffced4da ед. здоровья.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087150|cffced4da ед. здоровья.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087200|cffced4da ед. здоровья.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087300|cffced4da ед. здоровья.|r"
    )
    a0i9_tips = [8410, 8411, 8412, 9381]
    a0i9_ubs = [10063, 10708, 11623, 11691]
    a0i9_heal = [100, 150, 200, 300]
    for lvl in range(1, 5):
        wts_updates[a0i9_tips[lvl - 1]] = f"|cffe4cfa3Эссенция яда — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0i9_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает эссенцию яда, исцеляющую союзников на |cffc8e087{a0i9_heal[lvl - 1]}|cffced4da ед. здоровья.|r"
        )

    # A0IA: Дар пророка (E)
    wts_updates[9406] = "|cffe4cfa3Дар пророка|r"
    wts_updates[9405] = "|cffe4cfa3Дар пророка|r (|cffffffffE|r)"
    wts_updates[12818] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Провидец вглядывается в будущее, получая шанс избежать физических атак противника.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e08710%|cffced4da шанс уклонения.|n"
        "|cffa6afb82-й уровень:|r |cffc8e08720%|cffced4da шанс уклонения.|n"
        "|cffa6afb83-й уровень:|r |cffc8e08730%|cffced4da шанс уклонения.|n"
        "|cffa6afb84-й уровень:|r |cffc8e08740%|cffced4da шанс уклонения.|r"
    )
    a0ia_tips = [9402, 9403, 9404, 9407]
    a0ia_ubs = [12966, 12983, 13013, 12782]
    a0ia_pct = [10, 20, 30, 40]
    for lvl in range(1, 5):
        wts_updates[a0ia_tips[lvl - 1]] = f"|cffe4cfa3Дар пророка — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[a0ia_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует Пророку |cffc8e087{a0ia_pct[lvl - 1]}%|cffced4da шанс уклониться от вражеской атаки.|r"
        )

    # A1M9: Оплетение (R)
    wts_updates[11671] = "|cffe4cfa3Оплетение|r"
    a1m9_tips = [39194, 39195]
    a1m9_ubs = [12060, 12083]
    for lvl in range(1, 3):
        wts_updates[a1m9_tips[lvl - 1]] = f"|cffe4cfa3Оплетение — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[a1m9_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Опутывает врагов плотным коконом, оглушая наземных противников вокруг и нанося им урон.|r"
        )

    # Hero Spells: Crypt Lord U01V
    # A0ID: Темная стая (Q)
    wts_updates[11104] = "|cffe4cfa3Темная стая|r"
    wts_updates[11105] = "|cffe4cfa3Темная стая|r (|cffffffffQ|r)"
    wts_updates[13384] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну темной энергии, наносящую урон врагам на своём пути.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff75|cffced4da урона каждой цели.|n"
        "|cffa6afb82-й уровень:|r |cffffffff125|cffced4da урона каждой цели.|n"
        "|cffa6afb83-й уровень:|r |cffffffff180|cffced4da урона каждой цели.|n"
        "|cffa6afb84-й уровень:|r |cffffffff250|cffced4da урона каждой цели.|r"
    )
    a0id_tips = [11107, 11108, 11109, 11110]
    a0id_ubs = [13523, 13531, 13599, 13600]
    a0id_dmg = [75, 125, 180, 250]
    for lvl in range(1, 5):
        wts_updates[a0id_tips[lvl - 1]] = f"|cffe4cfa3Темная стая — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a0id_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Направляет рой тёмной энергии, наносящий |cffffffff{a0id_dmg[lvl - 1]}|cffced4da урона каждому поражённому врагу.|r"
        )

    # A0IC: Поражающий удар (W)
    wts_updates[9438] = "|cffe4cfa3Поражающий удар|r"
    wts_updates[10683] = "|cffe4cfa3Поражающий удар|r (|cffffffffW|r)"
    wts_updates[13014] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака оставляет глубокие рваные раны, вызывая кровотечение.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff3|cffced4da урона/сек. в течение |cffffffff10|cffced4da сек.|n"
        "|cffa6afb82-й уровень:|r |cffffffff4|cffced4da урона/сек. в течение |cffffffff15|cffced4da сек.|n"
        "|cffa6afb83-й уровень:|r |cffffffff5|cffced4da урона/сек. в течение |cffffffff20|cffced4da сек.|n"
        "|cffa6afb84-й уровень:|r |cffffffff6|cffced4da урона/сек. в течение |cffffffff25|cffced4da сек.|r"
    )
    a0ic_tips = [10688, 10691, 10986, 10987]
    a0ic_ubs = [13018, 13024, 13025, 13178]
    a0ic_vals = [(3, 10), (4, 15), (5, 20), (6, 25)]
    for lvl in range(1, 5):
        dmg_s, dur_s = a0ic_vals[lvl - 1]
        wts_updates[a0ic_tips[lvl - 1]] = f"|cffe4cfa3Поражающий удар — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0ic_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атака оставляет рану, наносящую |cffffffff{dmg_s}|cffced4da урона/сек. в течение |cffffffff{dur_s}|cffced4da сек.|r"
        )

    # A0IB: Критический удар (E)
    wts_updates[9430] = "|cffe4cfa3Критический удар|r"
    wts_updates[9431] = "|cffe4cfa3Критический удар|r (|cffffffffE|r)"
    wts_updates[18371] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс нанести сокрушительный многократный урон при физической атаке.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff15%|cffced4da шанс, |cffffffff1.5x|cffced4da урон.|n"
        "|cffa6afb82-й уровень:|r |cffffffff15%|cffced4da шанс, |cffffffff2.0x|cffced4da урон.|n"
        "|cffa6afb83-й уровень:|r |cffffffff15%|cffced4da шанс, |cffffffff2.5x|cffced4da урон.|n"
        "|cffa6afb84-й уровень:|r |cffffffff15%|cffced4da шанс, |cffffffff3.0x|cffced4da урон.|r"
    )
    a0ib_tips = [9432, 9434, 9435, 9436]
    for lvl in range(1, 5):
        wts_updates[a0ib_tips[lvl - 1]] = f"|cffe4cfa3Критический удар — уровень {lvl}|r (|cffffffffE|r)"
    wts_updates[9437] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс нанести сокрушительный многократный урон при атаке.|r"

    # A0IE: Аура метаморфоз (R)
    wts_updates[11117] = "|cffe4cfa3Аура метаморфоз|r"
    wts_updates[11118] = "|cffe4cfa3Аура метаморфоз|r (|cffffffffR|r)"
    wts_updates[13601] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение и усиливает естественную регенерацию здоровья союзников вокруг.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+15%|cffced4da к скорости бега, малый бонус к регенерации.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+30%|cffced4da к скорости бега, средний бонус к регенерации.|r"
    )
    a0ie_tips = [11115, 11116]
    a0ie_ubs = [13602, 13617]
    for lvl in range(1, 3):
        wts_updates[a0ie_tips[lvl - 1]] = f"|cffe4cfa3Аура метаморфоз — уровень {lvl}|r (|cffffffffR|r)"
        wts_updates[a0ie_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения и регенерацию здоровья находящихся рядом союзников.|r"
        )

    # Hero Spells: High Warden U01W
    # A0IF: Пронзание (Q)
    wts_updates[11149] = "|cffe4cfa3Пронзание|r"
    wts_updates[11150] = "|cffe4cfa3Пронзание|r (|cffffffffQ|r)"
    wts_updates[20130] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает ряд подземных шипов, наносящих урон и оглушающих врагов на линии.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff80|cffced4da урона, |cffffffff0.6|cffced4da сек. оглушения.|n"
        "|cffa6afb82-й уровень:|r |cffffffff100|cffced4da урона, |cffffffff1.2|cffced4da сек. оглушения.|n"
        "|cffa6afb83-й уровень:|r |cffffffff120|cffced4da урона, |cffffffff1.7|cffced4da сек. оглушения.|n"
        "|cffa6afb84-й уровень:|r |cffffffff140|cffced4da урона, |cffffffff2.4|cffced4da сек. оглушения.|r"
    )
    a0if_tips = [11151, 11152, 11153, 11154]
    a0if_ubs = [15539, 15540, 15541, 13665]
    a0if_vals = [(80, "0.6"), (100, "1.2"), (120, "1.7"), (140, "2.4")]
    for lvl in range(1, 5):
        dmg_v, dur_v = a0if_vals[lvl - 1]
        wts_updates[a0if_tips[lvl - 1]] = f"|cffe4cfa3Пронзание — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a0if_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вздымает шипы, нанося |cffffffff{dmg_v}|cffced4da урона наземным врагам на линии и оглушая их на |cffffffff{dur_v}|cffced4da сек.|r"
        )

    # A0IG: Создание кокона (W)
    wts_updates[11160] = "|cffe4cfa3Создание кокона|r"
    wts_updates[11161] = "|cffe4cfa3Создание кокона|r (|cffffffffW|r)"
    wts_updates[20591] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Плетёт паучьи коконы, из которых со временем появляются новые бойцы роя.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff1|cffced4da кокон.|n"
        "|cffa6afb82-й уровень:|r |cffffffff2|cffced4da кокона.|n"
        "|cffa6afb83-й уровень:|r |cffffffff3|cffced4da кокона.|n"
        "|cffa6afb84-й уровень:|r |cffffffff4|cffced4da кокона.|r"
    )
    a0ig_tips = [11163, 11164, 11165, 11159]
    a0ig_ubs = [20592, 20588, 20589, 20590]
    for lvl in range(1, 5):
        wts_updates[a0ig_tips[lvl - 1]] = f"|cffe4cfa3Создание кокона — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a0ig_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт |cffffffff{lvl}|cffced4da кокон(а), рождающих новых воинов роя.|r"
        )

    # A0IL: Рассекающий удар (E)
    wts_updates[11191] = "|cffe4cfa3Рассекающий удар|r"
    wts_updates[11192] = "|cffe4cfa3Рассекающий удар|r (|cffffffffE|r)"
    wts_updates[15441] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощные круговые взмахи наносят процентный сплеш-урон соседним целям.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff20%|cffced4da урона по области.|n"
        "|cffa6afb82-й уровень:|r |cffffffff30%|cffced4da урона по области.|n"
        "|cffa6afb83-й уровень:|r |cffffffff40%|cffced4da урона по области.|n"
        "|cffa6afb84-й уровень:|r |cffffffff50%|cffced4da урона по области.|r"
    )
    a0il_tips = [11194, 11195, 11196, 11197]
    a0il_ubs = [15443, 15444, 15445, 15442]
    a0il_pct = [20, 30, 40, 50]
    for lvl in range(1, 5):
        wts_updates[a0il_tips[lvl - 1]] = f"|cffe4cfa3Рассекающий удар — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[a0il_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки героя наносят |cffffffff{a0il_pct[lvl - 1]}%|cffced4da урона врагам рядом с основной целью.|r"
        )

    # A0IM: Рой саранчи (R)
    wts_updates[11199] = "|cffe4cfa3Рой саранчи|r"
    wts_updates[11200] = "|cffe4cfa3Рой саранчи|r (|cffffffffR|r)"
    wts_updates[20593] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя роем плотоядной саранчи, кусающей врагов и передающей жизненную силу владельцу.|r"
    )
    wts_updates[11201] = "|cffe4cfa3Рой саранчи — уровень 1|r (|cffffffffR|r)"
    wts_updates[11202] = "|cffe4cfa3Рой саранчи — уровень 2|r (|cffffffffR|r)"
    wts_updates[11203] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает рой саранчи, непрерывно атакующей врагов и восполняющей здоровье герою.|r"
    )

    # Hero Spells: Queen NERH
    # NQ02: Волна роя (Q)
    wts_updates[27568] = "|cffe4cfa3Волна роя|r"
    wts_updates[31785] = "|cffe4cfa3Волна роя|r (|cffffffffQ|r)"
    wts_updates[595] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Королева выпускает стремительную волну низших арахнидов, сминающую врагов на пути.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff100|cffced4da урона.|n"
        "|cffa6afb82-й уровень:|r |cffffffff175|cffced4da урона.|n"
        "|cffa6afb83-й уровень:|r |cffffffff250|cffced4da урона.|n"
        "|cffa6afb84-й уровень:|r |cffffffff325|cffced4da урона.|r"
    )
    nq02_tips = [33191, 33384, 33536, 34598]
    nq02_ubs = [3107, 17819, 18142, 20150]
    nq02_dmg = [100, 175, 250, 325]
    for lvl in range(1, 5):
        wts_updates[nq02_tips[lvl - 1]] = f"|cffe4cfa3Волна роя — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[nq02_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff{nq02_dmg[lvl - 1]}|cffced4da урона врагам на линии движения роя.|r"
        )

    # NQ03: Подавление (W)
    wts_updates[37930] = "|cffe4cfa3Подавление|r"
    wts_updates[37935] = "|cffe4cfa3Подавление|r (|cffffffffW|r)"
    wts_updates[37934] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Королева подавляет волю противника, нанося периодический урон, блокируя заклинания и замедляя атаку и скорость перемещения.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff25|cffced4da урона/сек., снижение скорости атаки и бега на |cffe69a8d20%|cffced4da.|n"
        "|cffa6afb82-й уровень:|r |cffffffff45|cffced4da урона/сек., снижение скорости атаки и бега на |cffe69a8d30%|cffced4da.|n"
        "|cffa6afb83-й уровень:|r |cffffffff65|cffced4da урона/сек., снижение скорости атаки и бега на |cffe69a8d40%|cffced4da.|n"
        "|cffa6afb84-й уровень:|r |cffffffff85|cffced4da урона/сек., снижение скорости атаки и бега на |cffe69a8d50%|cffced4da.|r"
    )
    nq03_tips = [37938, 37939, 37940, 37932]
    nq03_ubs = [37933, 37936, 37937, 37931]
    nq03_vals = [(25, 20), (45, 30), (65, 40), (85, 50)]
    for lvl in range(1, 5):
        d_val, s_val = nq03_vals[lvl - 1]
        wts_updates[nq03_tips[lvl - 1]] = f"|cffe4cfa3Подавление — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[nq03_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подавляет цель, нанося |cffffffff{d_val}|cffced4da урона/сек., блокируя применение магии и замедляя атаку и бег на |cffe69a8d{s_val}%|cffced4da.|r"
        )

    # NQ07: Воля королевы (E)
    wts_updates[37943] = "|cffe4cfa3Воля королевы|r"
    wts_updates[37949] = "|cffe4cfa3Воля королевы|r (|cffffffffE|r)"
    wts_updates[37948] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура верховной владычицы укрепляет подданных роя, повышая их броню и регенерацию здоровья и маны.|n|n"
        "|cffa6afb81-й уровень:|r |cffc8e087+2|cffced4da к броне, |cffc8e087+5|cffced4da к регенерации HP/маны.|n"
        "|cffa6afb82-й уровень:|r |cffc8e087+3|cffced4da к броне, |cffc8e087+6|cffced4da к регенерации HP/маны.|n"
        "|cffa6afb83-й уровень:|r |cffc8e087+4|cffced4da к броне, |cffc8e087+7|cffced4da к регенерации HP/маны.|n"
        "|cffa6afb84-й уровень:|r |cffc8e087+5|cffced4da к броне, |cffc8e087+8|cffced4da к регенерации HP/маны.|r"
    )
    nq07_tips = [37944, 37945, 37946, 37947]
    nq07_ubs = [32660, 24363, 32662, 32663]
    nq07_vals = [(2, 5), (3, 6), (4, 7), (5, 8)]
    for lvl in range(1, 5):
        arm_v, reg_v = nq07_vals[lvl - 1]
        wts_updates[nq07_tips[lvl - 1]] = f"|cffe4cfa3Воля королевы — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[nq07_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню союзников на |cffc8e087+{arm_v}|cffced4da, а восстановление здоровья и маны на |cffc8e087+{reg_v}|cffced4da.|r"
        )

    # NQ06: Породить лорда (R)
    wts_updates[37955] = "|cffe4cfa3Породить лорда|r"
    wts_updates[37959] = "|cffe4cfa3Породить лорда|r (|cffffffffR|r)"
    wts_updates[37960] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Плетёт особый кокон, из которого через |cffffffff60|cffced4da сек. появляется могучий Неруб Лорд.|n|n"
        "|cffa6afb81-й уровень:|r максимум |cffffffff1|cffced4da Лорд.|n"
        "|cffa6afb82-й уровень:|r максимум |cffffffff3|cffced4da Лорда.|r"
    )
    wts_updates[37962] = "|cffe4cfa3Породить лорда — уровень 1|r (|cffffffffR|r)"
    wts_updates[37957] = "|cffe4cfa3Породить лорда — уровень 2|r (|cffffffffR|r)"
    wts_updates[37961] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Через |cffffffff60|cffced4da сек. из кокона появляется Неруб Лорд. Лимит: |cffffffff1|cffced4da Лорд.|r"
    )
    wts_updates[37956] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Через |cffffffff60|cffced4da сек. из кокона появляется Неруб Лорд. Лимит: |cffffffff3|cffced4da Лорда.|r"
    )

    plan_data = {
        "race": "Nerubs",
        "race_id": 21,
        "total_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A0HT"],
            "markers": ["R07N"],
            "buildings": [
                "h0CO", "h0CP", "h0CQ", "h0CR", "h0CS", "h0CT",
                "h0CU", "h0CV", "h0GH", "lorE", "u019", "u01A"
            ],
            "units": [
                "h0BE", "u01B", "u01C", "u01D", "u01E", "u01F",
                "u01G", "u01H", "u01I", "u01J", "u01K", "u01T",
                "lord", "nq01"
            ],
            "heroes": ["U01U", "U01V", "U01W", "NERH"],
            "upgrades": [
                "R07N", "R074", "R075", "R076", "R070", "R06Z",
                "R071", "R072", "R073", "R0DR", "R077", "R078",
                "R079", "R07T", "R07R", "R07S", "R07P", "R07Q",
                "R07O", "R07U", "R07V", "R07W"
            ],
            "abilities": [
                "A0HT", "A186", "A0TQ", "A0I3",
                "A0HJ", "A0HD", "A0H9", "A0H4", "A0HC", "A0HB",
                "A0H7", "A0H5", "A0H6", "A0BO", "A0BS", "A0BR",
                "A0HK", "A0HA", "A0HF", "A0HI", "A0HH", "A0HG",
                "A0HE", "NQ11", "NQ04",
                "A0I7", "A0I9", "A0IA", "A1M9",
                "A0ID", "A0IC", "A0IB", "A0IE",
                "A0IF", "A0IG", "A0IL", "A0IM",
                "NQ02", "NQ03", "NQ07", "NQ06"
            ]
        }
    }

    out_file = folder / "nerubs_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {out_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

if __name__ == "__main__":
    main()
