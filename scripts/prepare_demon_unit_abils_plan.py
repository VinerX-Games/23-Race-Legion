# -*- coding: utf-8 -*-
"""Generate complete plan for Demon unit/building abilities and buffs standardization."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def build_plan():
    # 1. WTS updates: unique string_id -> new_value
    wts_updates = {
        # A0LU (Аура Скверны, ферма)
        13308: "|cffe4cfa3Аура Скверны|r",
        13309: "|cffe4cfa3Аура Скверны|r",
        13310: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная аура строения. Постепенно восстанавливает здоровье окружающим союзным строениям Легиона.|r",

        # A0LV (Укрыться за щитом / Поднять щит, n02E)
        13330: "|cffe4cfa3Укрыться за щитом|r",
        13331: "|cffe4cfa3Укрыться за щитом|r (|cffffffffD|r)",
        13334: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Кровопускатель поднимает щит, снижая получаемый урон от дальних пронзающих атак до |cffffffff50%|cffced4da, но его скорость передвижения уменьшается на |cffffffff30%|cffced4da.|r",
        13332: "|cffe4cfa3Опустить щит|r (|cffffffffD|r)",
        13335: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Опустить щит, возвращая обычную скорость передвижения и стандартную защиту от пронзающих атак.|r",

        # A0LW (Рассекающий удар 1 ур., n02D)
        13337: "|cffe4cfa3Рассекающий удар|r",
        13338: "|cffe4cfa3Рассекающий удар|r",
        13339: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сокрушительные удары наносят |cffffffff25%|cffced4da урона всем наземным врагам в радиусе |cffffffff150|cffced4da ед. вокруг основной цели.|r",

        # A0LX (Рассекающий удар 2 ур., n02E)
        13341: "|cffe4cfa3Рассекающий удар|r",
        13342: "|cffe4cfa3Рассекающий удар|r",
        13343: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сокрушительные удары наносят |cffffffff40%|cffced4da урона всем наземным врагам в радиусе |cffffffff150|cffced4da ед. вокруг основной цели.|r",

        # A0LY (Ловушка Тюремщика, n028)
        13344: "|cffe4cfa3Ловушка Тюремщика|r",
        13345: "|cffe4cfa3Ловушка Тюремщика|r",
        15192: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака сковывает цель демоническими путами, замедляя её скорость передвижения на |cffffffff30%|cffced4da и скорость боя на |cffffffff15%|cffced4da. Время действия: |cffffffff5|cffced4da сек.|r",

        # A0LZ (Пленение, n028)
        13347: "|cffe4cfa3Пленение|r",
        13348: "|cffe4cfa3Пленение|r (|cffffffffE|r)",
        13349: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Захватывает вражеского воина в подпространство своей клетки, нанося ему |cffffffff25|cffced4da ед. урона в секунду, пока тот не погибнет. Если Тюремщик погибает, пленник освобождается.|r",

        # A0M0 (Разрушение заклинаний, n028)
        13350: "|cffe4cfa3Разрушение заклинаний|r",
        13351: "|cffe4cfa3Разрушение заклинаний|r (|cffffffffW|r)",
        15988: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Развеивает все положительные и отрицательные магические эффекты с существ в радиусе |cffffffff200|cffced4da ед., а также наносит |cffffffff250|cffced4da ед. урона призванным существам.|r",

        # A0M1 (Похищение жизни, n020)
        13362: "|cffe4cfa3Похищение жизни|r",
        13363: "|cffe4cfa3Похищение жизни|r (|cffffffffQ|r)",

        # A0M2 (Проклятие, n020)
        13364: "|cffe4cfa3Проклятие|r",
        13365: "|cffe4cfa3Проклятие|r (|cffffffffW|r)",

        # A0M3 (Сокрушительный удар, n027)
        13367: "|cffe4cfa3Сокрушительный удар|r",
        13368: "|cffe4cfa3Сокрушительный удар|r",
        13369: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff20%|cffced4da шанс при атаке нанести дополнительно |cffffffff25|cffced4da ед. урона и оглушить цель на |cffffffff2|cffced4da сек. (героев на |cffffffff0.5|cffced4da сек.).|r",

        # A0M4 (Вместилище Скверно-бота, n029)
        13371: "|cffe4cfa3Вместилище Скверно-бота|r",

        # A0M5 (Боевая тревога, n029)
        13372: "|cffe4cfa3Боевая тревога|r",
        13373: "|cffe4cfa3Боевая тревога|r (|cffffffffQ|r)",

        # A0M6 (Огненный ливень, n021)
        13380: "|cffe4cfa3Огненный ливень|r",
        13381: "|cffe4cfa3Огненный ливень|r (|cffffffffQ|r)",

        # A0M7 (Аура Скверны, n021)
        13311: "|cffe4cfa3Аура Скверны|r",
        13385: "|cffe4cfa3Аура Скверны|r",

        # A0MX (Аура страха, n021)
        12646: "|cffe4cfa3Аура страха|r",
        12647: "|cffe4cfa3Аура страха|r",
        12695: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Внушает первобытный ужас вражеским войскам в радиусе |cffffffff400|cffced4da ед., снижая наносимый ими урон от атак на |cffffffff10%|cffced4da.|r",

        # A16J (Перст боли, n020)
        13615: "|cffe4cfa3Перст боли|r",
        27583: "|cffe4cfa3Перст боли|r (|cffffffffE|r)",
        16065: "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает разрушительный темный разряд, поражающий до |cffffffff5|cffced4da противников. Первой цели наносится |cffffffff125|cffced4da ед. урона, а каждой последующей урон снижается на |cffffffff15%|cffced4da.|r",
        13287: "|cffe4cfa3Перст боли|r",
        13824: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Эредаров-чернокнижников способности «Перст боли».|r",

        # S003 (Эволюция: Кровавое отродье)
        13299: "|cffe4cfa3Эволюция: Кровавое отродье|r",

        # S004 (Эволюция: Кровавый палач)
        13292: "|cffe4cfa3Эволюция: Кровавый палач|r",

        # S005 (Эволюция: Кровопускатель)
        13198: "|cffe4cfa3Эволюция: Кровопускатель|r",

        # Buffs in WTS:
        # B04O
        13407: "|cffe4cfa3Аура Скверны|r",
        13855: "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость восстановления здоровья строения увеличена под воздействием Ауры Скверны.|r",

        # B04P
        13353: "|cffe4cfa3Ловушка Тюремщика|r",
        13354: "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и скорость боя снижены демоническими путами Тюремщика.|r",

        # B04Q
        13355: "|cffe4cfa3Ловушка Тюремщика|r",
        13356: "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и скорость боя снижены демоническими путами Тюремщика.|r",

        # B04R
        13408: "|cffe4cfa3Аура Скверны|r",
        13409: "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и скорость восстановления здоровья увеличены под воздействием Ауры Скверны.|r",

        # B04S
        13438: "|cffe4cfa3Осквернение|r",

        # B04U
        13455: "|cffe4cfa3Испепеление|r",

        # B04V
        14050: "|cffe4cfa3Дары Скверны|r",

        # B04W
        13489: "|cffe4cfa3Коррозия Скверны|r",
        13490: "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак снижен под действием разъедающей Скверны.|r",

        # B04Y
        10751: "|cffe4cfa3Щит Скверны|r",

        # B04Z
        13725: "|cffe4cfa3Поглощение Скверны|r",

        # B050
        12696: "|cffe4cfa3Аура страха|r",

        # B051
        17223: "|cffe4cfa3Повелевание Скверной|r",

        # BNbf
        30814: "|cffe4cfa3Сгусток Скверны|r"
    }

    # 2. Skin w3a ops: list of {id, field, value}
    skin_w3a_ops = [
        # A0M1
        {"id": "A0M1", "field": "ubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Чернокнижник поддерживает поток темной энергии, вытягивая по |cffffffff25|cffced4da ед. здоровья в секунду из цели и передавая его себе. Длительность: до |cffffffff6|cffced4da сек.|r"},

        # A0M2
        {"id": "A0M2", "field": "ubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает вражеского воина, в результате чего его атаки получают |cffffffff33%|cffced4da шанс промахнуться. Длительность: |cffffffff60|cffced4da сек. (на героях |cffffffff10|cffced4da сек.).|r"},
        {"id": "A0M2", "field": "untip1", "value": "|cffe4cfa3Автозаклинание включено|r"},
        {"id": "A0M2", "field": "unubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Правый клик мыши включает или выключает автоматическое наложение проклятия на врагов при их приближении.|r"},

        # A0M5
        {"id": "A0M5", "field": "ubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает ближайшим Архитекторам Скверны укрыться внутри Скверно-бота для усиления его огневой мощи.|r"},

        # A0M6
        {"id": "A0M6", "field": "ubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область |cffffffff4|cffced4da волны огня, каждая из которых наносит |cffffffff30|cffced4da ед. урона и поджигает пораженные войска.|r"},

        # A0M7
        {"id": "A0M7", "field": "ubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения союзных существ на |cffffffff10%|cffced4da и ускоряет регенерацию их здоровья на |cffffffff0.5|cffced4da ед./сек.|r"},

        # A0MW (Сон - shared WTS name/tip + inline ubertip)
        {"id": "A0MW", "field": "name", "value": "|cffe4cfa3Сон|r"},
        {"id": "A0MW", "field": "tip1", "value": "|cffe4cfa3Сон|r (|cffffffffR|r)"},
        {"id": "A0MW", "field": "ubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Погружает вражеское существо в глубокий сон на |cffffffff15|cffced4da сек. (героев на |cffffffff4|cffced4da сек.). Спящая цель не может действовать, но мгновенно просыпается при получении урона.|r"},

        # A0VY (Сбор ресурсов - all inline)
        {"id": "A0VY", "field": "name", "value": "|cffe4cfa3Сбор ресурсов|r"},
        {"id": "A0VY", "field": "tip1", "value": "|cffe4cfa3Сбор ресурсов|r (|cffffffffG|r)"},
        {"id": "A0VY", "field": "ubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает рабочему добывать древесину из указанных деревьев.|r"},
        {"id": "A0VY", "field": "untip1", "value": "|cffe4cfa3Вернуть ресурсы|r (|cffffffffE|r)"},
        {"id": "A0VY", "field": "unubertip1", "value": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Нести добытую древесину в ближайшее главное здание или лесопилку.|r"},
    ]

    # 3. Skin w3h ops: list of {id, field, value}
    skin_w3h_ops = [
        {"id": "B04S", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения снижена, а шанс промахнуться при атаке увеличен под действием оскверненной земли.|r"},
        {"id": "B04U", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Цель охвачена пламенем Скверны и взорвется при гибели, нанося урон ближайшим существам.|r"},
        {"id": "B04V", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Защита и урон от атак существенно увеличены темным благословением Кил'джедена.|r"},
        {"id": "B04Y", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Враги, атакующие это существо в ближнем бою, получают ответный урон пламенем Скверны.|r"},
        {"id": "B04Z", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Часть наносимого урона возвращается существу в виде здоровья.|r"},
        {"id": "B050", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак снижен под воздействием подавляющего ужаса.|r"},
        {"id": "B051", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак увеличен под воздействием воли Повелителя Легиона.|r"},
        {"id": "BNbf", "field": "ubertip", "value": "|cffa6afb8ЭФФЕКТ:|cffced4da Получает периодический урон от поражения сгустком темной магии.|r"},
    ]

    # 4. Expected checks definition for SD validation
    # Each entry: {"id": obj_id, "type": "ability"|"buff", "field": field_name, "expected": expected_text}
    checks_def = []

    # Abilities expected checks
    # A0LU
    checks_def.append({"id": "A0LU", "type": "ability", "field": "name", "expected": "|cffe4cfa3Аура Скверны|r"})
    checks_def.append({"id": "A0LU", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Аура Скверны|r"})
    checks_def.append({"id": "A0LU", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная аура строения. Постепенно восстанавливает здоровье окружающим союзным строениям Легиона.|r"})

    # A0LV
    checks_def.append({"id": "A0LV", "type": "ability", "field": "name", "expected": "|cffe4cfa3Укрыться за щитом|r"})
    checks_def.append({"id": "A0LV", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Укрыться за щитом|r (|cffffffffD|r)"})
    checks_def.append({"id": "A0LV", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Кровопускатель поднимает щит, снижая получаемый урон от дальних пронзающих атак до |cffffffff50%|cffced4da, но его скорость передвижения уменьшается на |cffffffff30%|cffced4da.|r"})
    checks_def.append({"id": "A0LV", "type": "ability", "field": "untip1", "expected": "|cffe4cfa3Опустить щит|r (|cffffffffD|r)"})
    checks_def.append({"id": "A0LV", "type": "ability", "field": "unubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Опустить щит, возвращая обычную скорость передвижения и стандартную защиту от пронзающих атак.|r"})

    # A0LW
    checks_def.append({"id": "A0LW", "type": "ability", "field": "name", "expected": "|cffe4cfa3Рассекающий удар|r"})
    checks_def.append({"id": "A0LW", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Рассекающий удар|r"})
    checks_def.append({"id": "A0LW", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сокрушительные удары наносят |cffffffff25%|cffced4da урона всем наземным врагам в радиусе |cffffffff150|cffced4da ед. вокруг основной цели.|r"})

    # A0LX
    checks_def.append({"id": "A0LX", "type": "ability", "field": "name", "expected": "|cffe4cfa3Рассекающий удар|r"})
    checks_def.append({"id": "A0LX", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Рассекающий удар|r"})
    checks_def.append({"id": "A0LX", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сокрушительные удары наносят |cffffffff40%|cffced4da урона всем наземным врагам в радиусе |cffffffff150|cffced4da ед. вокруг основной цели.|r"})

    # A0LY
    checks_def.append({"id": "A0LY", "type": "ability", "field": "name", "expected": "|cffe4cfa3Ловушка Тюремщика|r"})
    checks_def.append({"id": "A0LY", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Ловушка Тюремщика|r"})
    checks_def.append({"id": "A0LY", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака сковывает цель демоническими путами, замедляя её скорость передвижения на |cffffffff30%|cffced4da и скорость боя на |cffffffff15%|cffced4da. Время действия: |cffffffff5|cffced4da сек.|r"})

    # A0LZ
    checks_def.append({"id": "A0LZ", "type": "ability", "field": "name", "expected": "|cffe4cfa3Пленение|r"})
    checks_def.append({"id": "A0LZ", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Пленение|r (|cffffffffE|r)"})
    checks_def.append({"id": "A0LZ", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Захватывает вражеского воина в подпространство своей клетки, нанося ему |cffffffff25|cffced4da ед. урона в секунду, пока тот не погибнет. Если Тюремщик погибает, пленник освобождается.|r"})

    # A0M0
    checks_def.append({"id": "A0M0", "type": "ability", "field": "name", "expected": "|cffe4cfa3Разрушение заклинаний|r"})
    checks_def.append({"id": "A0M0", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Разрушение заклинаний|r (|cffffffffW|r)"})
    checks_def.append({"id": "A0M0", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Развеивает все положительные и отрицательные магические эффекты с существ в радиусе |cffffffff200|cffced4da ед., а также наносит |cffffffff250|cffced4da ед. урона призванным существам.|r"})

    # A0M1
    checks_def.append({"id": "A0M1", "type": "ability", "field": "name", "expected": "|cffe4cfa3Похищение жизни|r"})
    checks_def.append({"id": "A0M1", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Похищение жизни|r (|cffffffffQ|r)"})
    checks_def.append({"id": "A0M1", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Чернокнижник поддерживает поток темной энергии, вытягивая по |cffffffff25|cffced4da ед. здоровья в секунду из цели и передавая его себе. Длительность: до |cffffffff6|cffced4da сек.|r"})

    # A0M2
    checks_def.append({"id": "A0M2", "type": "ability", "field": "name", "expected": "|cffe4cfa3Проклятие|r"})
    checks_def.append({"id": "A0M2", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Проклятие|r (|cffffffffW|r)"})
    checks_def.append({"id": "A0M2", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает вражеского воина, в результате чего его атаки получают |cffffffff33%|cffced4da шанс промахнуться. Длительность: |cffffffff60|cffced4da сек. (на героях |cffffffff10|cffced4da сек.).|r"})
    checks_def.append({"id": "A0M2", "type": "ability", "field": "untip1", "expected": "|cffe4cfa3Автозаклинание включено|r"})
    checks_def.append({"id": "A0M2", "type": "ability", "field": "unubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Правый клик мыши включает или выключает автоматическое наложение проклятия на врагов при их приближении.|r"})

    # A0M3
    checks_def.append({"id": "A0M3", "type": "ability", "field": "name", "expected": "|cffe4cfa3Сокрушительный удар|r"})
    checks_def.append({"id": "A0M3", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Сокрушительный удар|r"})
    checks_def.append({"id": "A0M3", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff20%|cffced4da шанс при атаке нанести дополнительно |cffffffff25|cffced4da ед. урона и оглушить цель на |cffffffff2|cffced4da сек. (героев на |cffffffff0.5|cffced4da сек.).|r"})

    # A0M4
    checks_def.append({"id": "A0M4", "type": "ability", "field": "name", "expected": "|cffe4cfa3Вместилище Скверно-бота|r"})

    # A0M5
    checks_def.append({"id": "A0M5", "type": "ability", "field": "name", "expected": "|cffe4cfa3Боевая тревога|r"})
    checks_def.append({"id": "A0M5", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Боевая тревога|r (|cffffffffQ|r)"})
    checks_def.append({"id": "A0M5", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает ближайшим Архитекторам Скверны укрыться внутри Скверно-бота для усиления его огневой мощи.|r"})

    # A0M6
    checks_def.append({"id": "A0M6", "type": "ability", "field": "name", "expected": "|cffe4cfa3Огненный ливень|r"})
    checks_def.append({"id": "A0M6", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Огненный ливень|r (|cffffffffQ|r)"})
    checks_def.append({"id": "A0M6", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область |cffffffff4|cffced4da волны огня, каждая из которых наносит |cffffffff30|cffced4da ед. урона и поджигает пораженные войска.|r"})

    # A0M7
    checks_def.append({"id": "A0M7", "type": "ability", "field": "name", "expected": "|cffe4cfa3Аура Скверны|r"})
    checks_def.append({"id": "A0M7", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Аура Скверны|r"})
    checks_def.append({"id": "A0M7", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения союзных существ на |cffffffff10%|cffced4da и ускоряет регенерацию их здоровья на |cffffffff0.5|cffced4da ед./сек.|r"})

    # A0MW
    checks_def.append({"id": "A0MW", "type": "ability", "field": "name", "expected": "|cffe4cfa3Сон|r"})
    checks_def.append({"id": "A0MW", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Сон|r (|cffffffffR|r)"})
    checks_def.append({"id": "A0MW", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Погружает вражеское существо в глубокий сон на |cffffffff15|cffced4da сек. (героев на |cffffffff4|cffced4da сек.). Спящая цель не может действовать, но мгновенно просыпается при получении урона.|r"})

    # A0MX
    checks_def.append({"id": "A0MX", "type": "ability", "field": "name", "expected": "|cffe4cfa3Аура страха|r"})
    checks_def.append({"id": "A0MX", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Аура страха|r"})
    checks_def.append({"id": "A0MX", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Внушает первобытный ужас вражеским войскам в радиусе |cffffffff400|cffced4da ед., снижая наносимый ими урон от атак на |cffffffff10%|cffced4da.|r"})

    # A16J
    checks_def.append({"id": "A16J", "type": "ability", "field": "name", "expected": "|cffe4cfa3Перст боли|r"})
    checks_def.append({"id": "A16J", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Перст боли|r (|cffffffffE|r)"})
    checks_def.append({"id": "A16J", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает разрушительный темный разряд, поражающий до |cffffffff5|cffced4da противников. Первой цели наносится |cffffffff125|cffced4da ед. урона, а каждой последующей урон снижается на |cffffffff15%|cffced4da.|r"})

    # A0VY
    checks_def.append({"id": "A0VY", "type": "ability", "field": "name", "expected": "|cffe4cfa3Сбор ресурсов|r"})
    checks_def.append({"id": "A0VY", "type": "ability", "field": "tip1", "expected": "|cffe4cfa3Сбор ресурсов|r (|cffffffffG|r)"})
    checks_def.append({"id": "A0VY", "type": "ability", "field": "ubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приказывает рабочему добывать древесину из указанных деревьев.|r"})
    checks_def.append({"id": "A0VY", "type": "ability", "field": "untip1", "expected": "|cffe4cfa3Вернуть ресурсы|r (|cffffffffE|r)"})
    checks_def.append({"id": "A0VY", "type": "ability", "field": "unubertip1", "expected": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Нести добытую древесину в ближайшее главное здание или лесопилку.|r"})

    # S003, S004, S005
    checks_def.append({"id": "S003", "type": "ability", "field": "name", "expected": "|cffe4cfa3Эволюция: Кровавое отродье|r"})
    checks_def.append({"id": "S004", "type": "ability", "field": "name", "expected": "|cffe4cfa3Эволюция: Кровавый палач|r"})
    checks_def.append({"id": "S005", "type": "ability", "field": "name", "expected": "|cffe4cfa3Эволюция: Кровопускатель|r"})

    # Buffs expected checks
    buff_checks = [
        ("B04O", "tip", "|cffe4cfa3Аура Скверны|r"),
        ("B04O", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость восстановления здоровья строения увеличена под воздействием Ауры Скверны.|r"),
        ("B04P", "tip", "|cffe4cfa3Ловушка Тюремщика|r"),
        ("B04P", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и скорость боя снижены демоническими путами Тюремщика.|r"),
        ("B04Q", "tip", "|cffe4cfa3Ловушка Тюремщика|r"),
        ("B04Q", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и скорость боя снижены демоническими путами Тюремщика.|r"),
        ("B04R", "tip", "|cffe4cfa3Аура Скверны|r"),
        ("B04R", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и скорость восстановления здоровья увеличены под воздействием Ауры Скверны.|r"),
        ("B04S", "tip", "|cffe4cfa3Осквернение|r"),
        ("B04S", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения снижена, а шанс промахнуться при атаке увеличен под действием оскверненной земли.|r"),
        ("B04U", "tip", "|cffe4cfa3Испепеление|r"),
        ("B04U", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Цель охвачена пламенем Скверны и взорвется при гибели, нанося урон ближайшим существам.|r"),
        ("B04V", "tip", "|cffe4cfa3Дары Скверны|r"),
        ("B04V", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Защита и урон от атак существенно увеличены темным благословением Кил'джедена.|r"),
        ("B04W", "tip", "|cffe4cfa3Коррозия Скверны|r"),
        ("B04W", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак снижен под действием разъедающей Скверны.|r"),
        ("B04Y", "tip", "|cffe4cfa3Щит Скверны|r"),
        ("B04Y", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Враги, атакующие это существо в ближнем бою, получают ответный урон пламенем Скверны.|r"),
        ("B04Z", "tip", "|cffe4cfa3Поглощение Скверны|r"),
        ("B04Z", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Часть наносимого урона возвращается существу в виде здоровья.|r"),
        ("B050", "tip", "|cffe4cfa3Аура страха|r"),
        ("B050", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак снижен под воздействием подавляющего ужаса.|r"),
        ("B051", "tip", "|cffe4cfa3Повелевание Скверной|r"),
        ("B051", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак увеличен под воздействием воли Повелителя Легиона.|r"),
        ("BNbf", "tip", "|cffe4cfa3Сгусток Скверны|r"),
        ("BNbf", "ubertip", "|cffa6afb8ЭФФЕКТ:|cffced4da Получает периодический урон от поражения сгустком темной магии.|r"),
    ]
    for bid, f, exp in buff_checks:
        checks_def.append({"id": bid, "type": "buff", "field": f, "expected": exp})

    plan = {
        "wts_updates": {str(k): v for k, v in wts_updates.items()},
        "skin_w3a_ops": skin_w3a_ops,
        "skin_w3h_ops": skin_w3h_ops,
        "checks_def": checks_def
    }

    out_path = ROOT / "docs/ui_text/demon_unit_abils_plan.json"
    out_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated plan with {len(wts_updates)} WTS updates, {len(skin_w3a_ops)} skin_w3a ops, {len(skin_w3h_ops)} skin_w3h ops, and {len(checks_def)} checks.")

if __name__ == "__main__":
    build_plan()
