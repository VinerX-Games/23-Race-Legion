"""Apply the scoped subfaction object plan without rewriting unrelated records."""
import argparse
import copy
import hashlib
import json
import re
import struct
from pathlib import Path

from implement_draenei_rework import object_records

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "map.w3x"
OUT = ROOT / ".cache/wc3/subfactions"
TITLE = "|cffebc56c"
BODY = "|cffced4da"
TYPE = "|cffb99d66"


def text(kind, description):
    return f"{TYPE}{kind}:{BODY} {color_numbers(description)}|r"


def color_numbers(value):
    color = BODY
    parts = re.split(r"(\|c[0-9a-fA-F]{8}|\|r|\|n)", value)
    for index, part in enumerate(parts):
        if part.startswith("|c"):
            color = part
        elif part == "|r":
            color = BODY
        elif part != "|n" and color == BODY:
            parts[index] = re.sub(r"(?<![\w])\d+(?:[.,]\d+)?%?", lambda match: "|cffffffff" + match.group() + BODY, part)
    return "".join(parts)


def source_fields(ext):
    path = OUT / "before" / ("war3map." + ext)
    if not path.exists():
        path = MAP / ("war3map." + ext)
    _, tables = object_records(path.read_bytes(), ext != "w3u")
    from wc3_hivewe import load_wts_strings
    strings = load_wts_strings()
    result = {}
    for record in (r for table in tables for r in table):
        fields = {}
        for key, raw in record["mods"]:
            kind = struct.unpack_from("<I", raw, 4)[0]
            offset = 8 if ext == "w3u" else 16
            value = raw[offset:-4]
            if kind == 3:
                value = value[:-1].decode("utf-8")
                if value.startswith("TRIGSTR_"):
                    value = strings.get(int(value[8:]), value)
            elif kind == 0:
                value = struct.unpack("<i", value)[0]
            else:
                value = struct.unpack("<f", value)[0]
            fields[key] = value
        result[record["id"]] = fields
    return result


def patch_record(record, values, extended, code):
    pending = dict(values)
    mods = []
    for key, raw in record["mods"]:
        if key not in values:
            mods.append(raw)
            continue
        if key in pending:
            mods.append(encode_mod(key, pending.pop(key), extended, code))
    mods.extend(encode_mod(key, value, extended, code) for key, value in pending.items())
    return record["header"] + struct.pack("<I", len(mods)) + b"".join(mods)


def encode_mod(key, item, extended, code):
    field, level, pointer = key
    value_type, value = item
    raw = field.encode("ascii") + struct.pack("<I", value_type)
    if extended:
        raw += struct.pack("<II", level, pointer)
    if value_type == 3:
        raw += str(value).encode("utf-8") + b"\0"
    elif value_type == 0:
        raw += struct.pack("<i", int(value))
    else:
        raw += struct.pack("<f", float(value))
    return raw + code.encode("ascii")


def plan():
    changes = {"w3u": {}, "w3a": {}, "w3q": {}}
    clones = {"w3u": {}, "w3a": {}, "w3q": {}}

    def put(ext, code, values, level=0):
        changes[ext].setdefault(code, {}).update({(field, level, 0): item for field, item in values.items()})

    def unit(code, source, name, desc, fields):
        clones["w3u"][code] = source
        values = {"unam": (3, TITLE + name + "|r"), "utip": (3, TITLE + name + "|r"),
                  "utub": (3, text("ГЕРОЙ" if code[0].isupper() else "ЮНИТ", desc)),
                  "ureq": (3, ""), "urqa": (3, ""), "uspa": (3, ""), **fields}
        put("w3u", code, values)

    def ability(code, source, name, desc, fields=None):
        clones["w3a"][code] = source
        put("w3a", code, {"anam": (3, TITLE + name + "|r"), "areq": (3, ""),
                           "achd": (0, 0), "aher": (0, 0), "aite": (0, 0), "alev": (0, 1)})
        put("w3a", code, {"atp1": (3, TITLE + name + "|r"), "aub1": (3, text("СПОСОБНОСТЬ", desc)), **(fields or {})}, 1)

    ability("xdA1", "Acrs", "Проклятие Тёмной Орды", "Проклинает противника, заставляя его промахиваться при атаках.")
    ability("xdA2", "Acri", "Истощение", "Снижает скорость перемещения, скорость атаки и урон противника.")
    ability("xdA3", "ACfb", "Драконье пламя", "Наносит цели 100 урона и оглушает на 1 сек. Дальность 600; 65 маны; восстановление 10 сек.",
            {"adur": (1, 1), "ahdu": (1, 1), "aran": (1, 600), "amcs": (0, 65), "acdn": (1, 10)})
    ability("xdA4", "Ainf", "Пламенный доспех", "Внутренний огонь повышает урон союзника на |cffc8e08710%|cffced4da и броню на |cffc8e0875|cffced4da. Действует 60 сек.; 35 маны.")
    ability("xdA5", "Aens", "Цепи укротителя", "Обездвиживает цель сетью. Не даёт цели двигаться, но сохраняет возможность атаковать.")
    ability("xdA6", "Aprg", "Усмирение", "Развеивает магические эффекты цели и замедляет противника.")
    ability("xdA7", "w2a1", "Полевое снабжение", "При смертельном ударе по собственному ветерану в радиусе 1000 даёт шанс предотвратить урон и сохранить не менее 15% здоровья. Шанс 50%, повышается Разведкой. Для каждого спасённого бойца: восстановление 45 сек.")
    ability("xdA8", "w2a1", "Эвакуация ветеранов", "При смертельном ударе по собственному ветерану в радиусе 1000 даёт шанс отменить удар и перенести его к погонщику. Шанс 60%, повышается Разведкой. Для каждого спасённого бойца: восстановление 45 сек.")

    unit("xd01", "w211", "Чернокнижник Тёмной Орды",
         "Колдун поддержки. Способности: Проклятие Тёмной Орды заставляет врага промахиваться; Истощение снижает его боевые характеристики; Кузня войны даёт ветеранство. Атакует наземные и воздушные цели.",
         {"umdl": (3, "units\\creeps\\ChaosWarlockGreen\\ChaosWarlockGreen.mdl"), "uabi": (3, "w2a0,xdA1,xdA2"), "umpm": (0, 400), "umpi": (0, 400), "upgr": (3, "w2r0,w2r6"), "uhot": (3, "Q"), "ubpx": (0, 1), "ubpy": (0, 0), "uico": (3, "ReplaceableTextures\\CommandButtons\\BTNChaosWarlock.blp")})
    unit("xd02", "w204", "Осадный огр",
         "Тяжёлый штурмовик с осадным типом атаки. Способности: Кузня войны повышает характеристики с опытом; сохраняет боевые способности огра-воина. Атакует наземные цели.",
         {"ureq": (3, "w20e"), "ua1t": (3, "siege"), "uhpm": (0, 1100), "ua1b": (0, 44), "ugol": (0, 385), "ulum": (0, 130), "uhot": (3, "Q"), "ubpx": (0, 2), "ubpy": (0, 0)})
    unit("xd03", "w204", "Чёрный драконид",
         "Поздний тяжёлый боец ближнего боя. Способности: Кузня войны даёт ветеранство; Прочная чешуя после исследования усиливает защиту; сохраняет боевые способности огра-воина. Атакует наземные цели.",
         {"ureq": (3, "w20e"), "umdl": (3, "Dragon\\DragonSpawnGuard.mdl"), "uico": (3, "ReplaceableTextures\\CommandButtons\\BTNIconBlackDragonSpawn.blp"), "uabi": (3, "w2a0,w290,w285,w2ag,w284"), "upgr": (3, "w2r0,w2r1,w2r8,w2ra,w292"), "uhpm": (0, 1400), "ua1b": (0, 65), "ugol": (0, 550), "ulum": (0, 180), "uhot": (3, "Q"), "ubpx": (0, 0), "ubpy": (0, 0)})
    unit("xd04", "w203", "Копьеметатель Драконьей Пасти",
         "Орочий стрелок. Способности: Кузня войны даёт ветеранство. Использует улучшения оружия и брони Старой Орды. Атакует наземные и воздушные цели.",
         {"ureq": (3, "w214"), "umdl": (3, "Horde\\OrcSpearThrower.mdl"), "ua1m": (3, "Abilities\\Weapons\\Spear\\SpearMissile.mdl"), "uhot": (3, "R"), "ubpx": (0, 1), "ubpy": (0, 0)})
    unit("xd05", "w202", "Наездник Драконьей Пасти",
         "Орк на боевом драконе; мобильная наземная элита. Способности: сохраняет драконьи способности Красного дракона и Кузню войны. Не является свободной авиацией. Атакует наземные цели.",
         {"ureq": (3, "w20e"), "umdl": (3, "Horde\\DragonmawRider.mdl"), "umvt": (3, "hover"), "umvh": (1, 65), "usca": (1, 0.9), "uhpm": (0, 900), "ugol": (0, 480), "ulum": (0, 160), "uhot": (3, "Q"), "ubpx": (0, 0), "ubpy": (0, 0)})
    unit("xd06", "w211", "Укротитель драконов",
         "Орочий заклинатель контроля. Способности: Цепи укротителя обездвиживают цель; Усмирение развеивает магию и замедляет врагов; Кузня войны даёт ветеранство. Атакует наземные и воздушные цели.",
         {"umdl": (3, "units\\orc\\SpiritWalker\\SpiritWalker.mdl"), "uabi": (3, "w2a0,xdA5,xdA6"), "umpm": (0, 400), "umpi": (0, 400), "uhot": (3, "Q"), "ubpx": (0, 1), "ubpy": (0, 0)})
    unit("xd07", "w202", "Чёрный дракончик",
         "Мобильный экспериментальный дракон Тёмной Орды. Способности: сохраняет драконьи способности Красного дракона и Кузню войны. Атакует наземные цели.",
         {"ureq": (3, "w20e"), "umdl": (3, "units\\creeps\\BlackDragonWelp\\BlackDragonWelp.mdl"), "uhpm": (0, 670), "ugol": (0, 300), "ulum": (0, 100), "ua1b": (0, 24), "uhot": (3, "Q"), "ubpx": (0, 0), "ubpy": (0, 0)})
    for code, name, desc, marker, model in [
        ("xd08", "Интендант Тёмной Орды", "Наземный обоз поддержки. Способности: Полевое снабжение спасает собственных ветеранов от смертельного удара поблизости; Кузня войны даёт ветеранство. Не атакует.", "xdA7", "units\\orc\\KotoBeast\\KotoBeast.mdl"),
        ("xd0A", "Погонщик Драконьей Пасти", "Наземный орочий спасатель. Способности: Эвакуация ветеранов выводит собственных бойцов из-под смертельного удара; Кузня войны даёт ветеранство. Не атакует.", "xdA8", "units\\orc\\Raider\\Raider.mdl"),
    ]:
        unit(code, "w201", name, desc, {"umdl": (3, model), "umvt": (3, "foot"), "umvh": (1, 0), "ucol": (1, 24), "uabi": (3, "w2a0," + marker), "uaen": (0, 0), "uhot": (3, "Z"), "ubpx": (0, 1), "ubpy": (0, 0)})
    unit("xd09", "w205", "Погонщик драконьего пламени",
         "Орочий заклинатель огня и поддержки. Способности: Драконье пламя наносит урон и оглушает; Пламенный доспех повышает урон и броню союзника; Кузня войны даёт ветеранство. Атакует наземные цели.",
         {"umdl": (3, "units\\orc\\Shaman\\Shaman.mdl"), "uabi": (3, "w2a0,xdA3,xdA4"), "umpm": (0, 450), "umpi": (0, 450), "uhot": (3, "W"), "ubpx": (0, 2), "ubpy": (0, 0)})
    unit("W204", "W200", "Повелитель драконов",
         "Орочий командир Драконьей Пасти. Способности: Огненный столб поражает область; Аура выносливости ускоряет союзников; Критический удар усиливает атаки; Реинкарнация возвращает героя к жизни. Атакует наземные цели.",
         {"upro": (3, "Зулухед"), "uhab": (3, "AHfs,AOae,AOcr,AOre"), "ureq": (3, "w20e"), "uhot": (3, "E"), "ubpx": (0, 2), "ubpy": (0, 0)})

    put("w3u", "w200", {"ubui": (3, "w214,w20i,w210,w212,w20a,w20q,w20r,w20t,w20u,w20y,w218")})
    lists = {"w20i": "w207,w201,w206,xd02,xd08,xd0A", "w20t": "w209,w211,w205,xd01,xd06,xd09",
             "w210": "w202,xd07,xd05", "w212": "xd03", "w20a": "W200,W202,W201,W203,W204"}
    for code, units in lists.items():
        put("w3u", code, {"utra": (3, units)})
    put("w3u", "w20q", {"ures": (3, "w2r3")})
    put("w3u", "nntt", {"ures": (3, "")})
    put("w3u", "w212", {"ures": (3, "w2ra"), "uhot": (3, "V"), "ubpx": (0, 2), "ubpy": (0, 2), "unam": (3, TITLE + "Логово чёрных драконов|r"), "utip": (3, TITLE + "Логово чёрных драконов|r")})
    put("w3u", "xd04", {"upgr": (3, "w2r9,w2r0,w2r2")})
    for code, icon in [("xd04", "BTN_Horde_Strel2"), ("xd06", "BTNSpiritWalker"),
                       ("xd07", "BTNBlackDragon"), ("xd08", "BTNKotoBeast"),
                       ("xd09", "BTNShaman"), ("xd0A", "BTNRaider")]:
        put("w3u", code, {"uico": (3, "ReplaceableTextures\\CommandButtons\\" + icon + ".blp")})
    for code in ["xd08", "xd0A"]:
        put("w3u", code, {"utyp": (3, "")})
    for code, icon in [("xdA7", "BTNKotoBeast"), ("xdA8", "BTNRaider")]:
        put("w3a", code, {"aart": (3, "ReplaceableTextures\\CommandButtons\\" + icon + ".blp"), "abpx": (0, 0), "abpy": (0, 1)})
    for code in ["xdR1", "xdR2"]:
        put("w3q", code, {"gglb": (0, 0), "glmb": (0, 0), "gtib": (0, 0)})
        put("w3q", code, {"gef1": (3, "")}, 1)
        put("w3q", code, {"gef2": (3, "")}, 2)
    for code in ["w291", "w292", "w293"]:
        put("w3q", code, {"greq": (3, "w20w")})
        put("w3q", code, {"greq": (3, "w20w")}, 1)
    for level in range(1, 16):
        put("w3a", "w2a0", {"atp1": (3, TITLE + f"Кузня войны — уровень {level - 1}|r"),
                               "aub1": (3, text("СПОСОБНОСТЬ", "Накапливает опыт в бою. Каждый уровень повышает максимальное здоровье и ману на |cffc8e0873,5%|cffced4da, базовый урон на |cffc8e0874%|cffced4da и даёт дополнительный урон атакой по уровню. Пределы веток: Орда Второй Войны — 10, Тёмная Орда — 12, Драконья Пасть — 8."))}, level)

    original_units = source_fields("w3u")
    for code, fields in original_units.items():
        researches = str(fields.get(("ures", 0, 0), "")).split(",")
        kept = [value for value in researches if value not in ["R0FE", "R0FF"]]
        if kept != researches:
            put("w3u", code, {"ures": (3, ",".join(kept))})
    effective = {code: dict(fields) for code, fields in original_units.items()}
    for code, source in clones["w3u"].items():
        effective[code] = dict(original_units[source])
    for code, fields in changes["w3u"].items():
        effective.setdefault(code, {}).update({key: value for key, (_, value) in fields.items()})

    def name(code):
        return str(effective[code].get(("unam", 0, 0), code))

    buildings = {
        "w20q": "Основное здание Старой Орды. Подфракция выбирается до начала строительства.",
        "w20r": "Казармы основных войск Старой Орды. Состав найма зависит от подфракции.",
        "w20i": "Производство осадных войск и поддержки. Состав найма зависит от подфракции.",
        "w20t": "Подготовка заклинателей Старой Орды. Состав найма зависит от подфракции.",
        "w20a": "Возвращает павших героев и обучает героев выбранной подфракции. Повелителю драконов требуется Цитадель.",
        "w210": "Подготовка драконьих войск выбранной подфракции. Базовая Орда дополнительно выбирает специализацию драконов.",
        "w212": "Поздняя подготовка чёрных драконидов Тёмной Орды.",
        "nntt": "Основное здание наг и мурлоков. Владычество выбирается на стартовом экране подфракций.",
    }
    upgrades = source_fields("w3q")
    for code, role in buildings.items():
        unit_fields = effective[code]
        body = role
        trained = unit_fields.get(("utra", 0, 0), "")
        if trained:
            body += "|n|n" + TYPE + "Обучает:" + BODY + "|n" + "|n".join("- " + name(uid) for uid in trained.split(","))
        researches = unit_fields.get(("ures", 0, 0), "")
        if researches:
            body += "|n|n" + TYPE + "Исследования:" + BODY + "|n" + "|n".join("- " + str(upgrades.get(uid, {}).get(("gnam", 1, 0), uid)) for uid in researches.split(","))
        put("w3u", code, {"utub": (3, text("ЗДАНИЕ", body))})

    veteran = ("Кузня войны", "накапливает опыт и повышает характеристики")
    ogre = [("Сопротивление магии", "снижает урон вражеских заклинаний"), ("Сильный удар", "даёт шанс дополнительного урона и оглушения")]
    dragon = [("Прочная чешуя", "после исследования снижает урон атак"), ("Огненный столб", "поджигает область"), ("Пламенное дыхание", "поражает врагов конусом огня")]
    tips = {
        "xd01": ("Колдун поддержки Тёмной Орды.", [("Проклятие Тёмной Орды", "заставляет врагов промахиваться"), ("Истощение", "снижает урон и скорость врага")], "наземные и воздушные"),
        "xd02": ("Тяжёлый штурмовик с осадным типом атаки.", ogre, "наземные"),
        "xd03": ("Поздний тяжёлый боец Тёмной Орды.", ogre + [dragon[0]], "наземные"),
        "xd04": ("Орочий стрелок Драконьей Пасти.", [], "наземные и воздушные"),
        "xd05": ("Орк на боевом драконе; мобильная наземная элита.", dragon, "наземные"),
        "xd06": ("Орочий заклинатель контроля.", [("Цепи укротителя", "обездвиживают врага"), ("Усмирение", "развеивает магию и замедляет врага")], "наземные и воздушные"),
        "xd07": ("Молодой экспериментальный дракон Тёмной Орды.", dragon, "наземные"),
        "xd08": ("Наземный обоз поддержки Тёмной Орды.", [("Полевое снабжение", "спасает собственных ветеранов от смертельного удара поблизости")], None),
        "xd09": ("Орочий заклинатель огня и поддержки.", [("Драконье пламя", "наносит урон и оглушает"), ("Пламенный доспех", "повышает урон и броню союзника")], "наземные"),
        "xd0A": ("Наземный орочий спасатель Драконьей Пасти.", [("Эвакуация ветеранов", "выводит собственных бойцов из-под смертельного удара")], None),
    }
    for code, (role, abilities, targets) in tips.items():
        body = role + "|n|n" + TYPE + "Способности:" + BODY + "|n"
        body += "|n".join("- " + TITLE + label + BODY + ": " + desc + "." for label, desc in abilities + [veteran])
        body += "|n|n" + ("Атакует " + targets + " цели." if targets else "Не атакует.")
        put("w3u", code, {"utub": (3, text("ЮНИТ", body))})
    put("w3u", "W204", {"utub": (3, text("ГЕРОЙ", "Орочий командир Драконьей Пасти.|n|n" + TYPE + "Способности:" + BODY + "|n- Огненный столб: поражает врагов в области.|n- Аура выносливости: ускоряет союзников.|n- Критический удар: даёт шанс усиленной атаки.|n- Реинкарнация: возвращает героя к жизни.|n|nАтакует наземные цели."))})

    affected = ["w2r0", "w2r1", "w2r2", "w2r4", "w2r6", "w2r8", "w2r9", "w2ra", "w291", "w292", "w293"]
    for upgrade in affected:
        targets = [code for code, fields in effective.items() if upgrade in str(fields.get(("upgr", 0, 0), "")).split(",") and (code.startswith("w2") or code in clones["w3u"])]
        maximum = upgrades.get(upgrade, {}).get(("glvl", 0, 0), 1)
        for key, old_tip in upgrades.get(upgrade, {}).items():
            if key[0] != "gub1" or key[1] > maximum or not isinstance(old_tip, str):
                continue
            body = re.split(r"\|n\|n(?:\|c[0-9a-fA-F]{8})?Применяется к:", old_tip)[0].removesuffix("|r")
            body = re.split(r"\|n\|n(?:\|c[0-9a-fA-F]{8})?Уровень исследования:", body)[0]
            body = body.replace("ТЕХНОЛОГИЯ:", "ИССЛЕДОВАНИЕ:")
            if upgrade == "w2r4":
                body = body.replace("у огров-магов", "у огров-магов и погонщиков драконьего пламени").replace("а также открывает", "а также у огров-магов открывает")
            if upgrade == "w2r6":
                body = body.replace("у жрецов", "у жрецов, чернокнижников Тёмной Орды и укротителей драконов").replace("а также открывает", "а также у жрецов открывает")
            body += "|n|n" + TYPE + "Применяется к:" + BODY + "|n" + "|n".join("- " + name(uid) for uid in sorted(targets))
            if maximum > 1:
                body += f"|n|n{TYPE}Уровень исследования:{BODY} {key[1]}/{maximum}."
            put("w3q", upgrade, {"gub1": (3, color_numbers(body.removesuffix("|r")) + "|r")}, key[1])
    for level in [1, 2]:
        put("w3q", "w2rq", {"gub1": (3, text("ИССЛЕДОВАНИЕ", f"Оснащает Дирижабль ракетными установками. Каждый уровень повышает шанс спасения собственных ветеранов на 10 процентных пунктов.|n|nПрименяется к:|n- Дирижабль|n- Интендант Тёмной Орды|n- Погонщик Драконьей Пасти|n|nУровень исследования: {level}/2."))}, level)
    for code in ["xdA7", "xdA8"]:
        key = ("aub1", 1, 0)
        changes["w3a"][code][key] = (3, changes["w3a"][code][key][1].replace("повышается Разведкой", "повышается Комплектованием дирижаблей"))
    return changes, clones


def build_file(original, ext, changes, clones, main_original):
    extended = ext != "w3u"
    version, tables = object_records(original, extended)
    _, main_tables = object_records(main_original, extended)
    lookup = {r["id"]: r for table in main_tables for r in table}
    lookup.update({r["id"]: r for table in tables for r in table})
    records = copy.deepcopy(tables)
    for code, source in clones.items():
        if source in lookup:
            record = copy.deepcopy(lookup[source])
            record["header"] = record["header"][:4] + code.encode("ascii") + record["header"][8:]
            record["mods"] = [(key, raw[:-4] + code.encode("ascii")) for key, raw in record["mods"]]
        else:
            assert ext == "w3a", source
            extra = struct.pack("<II", 1, 0) if version >= 3 else b""
            record = {"header": source.encode("ascii") + code.encode("ascii") + extra, "mods": []}
        record["id"] = code
        record["raw"] = patch_record(record, {}, extended, code)
        for table in records:
            table[:] = [r for r in table if r["id"] != code]
        records[1].append(record)
    known = {r["id"] for table in records for r in table}
    for code in set(changes) - known:
        assert code in lookup, code
        records[1 if lookup[code]["header"][4:8] != b"\0" * 4 else 0].append(copy.deepcopy(lookup[code]))
    result = bytearray(struct.pack("<I", version))
    for table in records:
        result += struct.pack("<I", len(table))
        for record in table:
            code = record["id"]
            result += patch_record(record, changes[code], extended, code) if code in changes else record["raw"]
    _, after = object_records(bytes(result), extended)
    by_id = {r["id"]: r for table in after for r in table}
    for table in tables:
        for record in table:
            if record["id"] not in changes and record["id"] not in clones:
                assert record["raw"] == by_id[record["id"]]["raw"], record["id"]
    return bytes(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    before, stage = OUT / "before", OUT / "stage"
    before.mkdir(exist_ok=True)
    stage.mkdir(exist_ok=True)
    report_path = OUT / "object-plan.json"
    previous = json.loads(report_path.read_text(encoding="utf-8")) if report_path.exists() else {"files": []}
    last_hashes = {entry["file"]: entry["after"] for entry in previous["files"]}
    changes, clones = plan()
    report = {"files": [], "objects": {ext: sorted(ops) for ext, ops in changes.items()}}
    payload = {}
    for ext in changes:
        main_original = (MAP / ("war3map." + ext)).read_bytes()
        for prefix in ["war3map", "war3mapSkin"]:
            name = prefix + "." + ext
            original = (MAP / name).read_bytes()
            if (before / name).exists():
                current_hash = hashlib.sha256(original).hexdigest()
                original = (before / name).read_bytes()
                assert current_hash in {hashlib.sha256(original).hexdigest(), last_hashes.get(name)}, f"Concurrent object changes: {name}"
            else:
                (before / name).write_bytes(original)
            source_main = (before / ("war3map." + ext)).read_bytes() if (before / ("war3map." + ext)).exists() else main_original
            edited = build_file(original, ext, changes[ext], clones[ext], source_main)
            (stage / name).write_bytes(edited)
            payload[name] = edited
            report["files"].append({"file": name, "before": hashlib.sha256((MAP / name).read_bytes()).hexdigest(), "after": hashlib.sha256(edited).hexdigest()})
    for path in MAP.glob("war3map*"):
        if path.is_file() and path.name not in payload:
            (stage / path.name).write_bytes(path.read_bytes())
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.apply:
        for entry in report["files"]:
            target = MAP / entry["file"]
            assert hashlib.sha256(target.read_bytes()).hexdigest() == entry["before"], target
        for name, edited in payload.items():
            (MAP / name).write_bytes(edited)
    print(json.dumps({"applied": args.apply, **report}, ensure_ascii=False))


if __name__ == "__main__":
    main()
