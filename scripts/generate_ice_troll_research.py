# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

# Color constants
C_TITLE = "|cffe4cfa3"
C_TAG = "|cffa6afb8"
C_BODY = "|cffced4da"
C_NUM = "|cffffffff"
C_BUFF = "|cffc8e087"
C_DEBUFF = "|cffe69a8d"
C_REF = "|cffa9c7de"
C_RESET = "|r"

def fmt_research_tip(name, level=None, max_level=None, hotkey=None):
    base = f"{C_TITLE}{name}{C_RESET}"
    if max_level and max_level > 1 and level is not None:
        base += f" — уровень {C_NUM}{level}{C_RESET}"
    if hotkey:
        base += f" ({C_NUM}{hotkey}{C_RESET})"
    return base

def fmt_research_desc(effect_body, targets_body, level=None, max_level=None, extra_notes=None):
    res = f"{C_TAG}ИССЛЕДОВАНИЕ:{C_BODY} {effect_body}"
    if targets_body:
        res += f"|n|nЗатрагивает: {targets_body}."
    if extra_notes:
        res += f"|n|n{extra_notes}"
    if max_level and max_level > 1 and level is not None:
        res += f"|n|n{C_TAG}Уровень исследования:{C_BODY} {C_NUM}{level}/{max_level}{C_BODY}."
    res += C_RESET
    return res

# 20 Ice Troll Upgrades
RESEARCH_DATA = {
    # 1. Melee Weapons (3 levels)
    "R0HZ": {
        "name": "Оружие ближнего боя",
        "hotkey": "M",
        "max_level": 3,
        "targets": f"{C_REF}Воителей{C_BODY}, {C_REF}Белых медведей{C_BODY}, {C_REF}Лютых мамонтов{C_BODY}, {C_REF}Магнатавров-разрушителей{C_BODY}, {C_REF}Берсерков{C_BODY}, {C_REF}Големов{C_BODY}, {C_REF}Восставших{C_BODY} и Лоа ({C_REF}Акали{C_BODY}, {C_REF}Мам'тота{C_BODY}, {C_REF}Рунока{C_BODY})",
        "levels": {
            1: {"effect": f"Увеличивает урон от атак немагических воинов ближнего боя на {C_NUM}1{C_BODY} ед."},
            2: {"effect": f"Увеличивает урон от атак немагических воинов ближнего боя ещё на {C_NUM}1{C_BODY} ед. (всего {C_NUM}+2{C_BODY} ед.)."},
            3: {"effect": f"Увеличивает урон от атак немагических воинов ближнего боя ещё на {C_NUM}1{C_BODY} ед. (всего {C_NUM}+3{C_BODY} ед.)."}
        }
    },
    # 2. Steel Armor (3 levels)
    "R0I0": {
        "name": "Стальная броня",
        "hotkey": "A",
        "max_level": 3,
        "targets": f"все войска и чудовищ {C_REF}Драккари{C_BODY}",
        "levels": {
            1: {"effect": f"Увеличивает защиту всех наземных и летающих войск на {C_NUM}1{C_BODY} ед."},
            2: {"effect": f"Увеличивает защиту всех наземных и летающих войск ещё на {C_NUM}1{C_BODY} ед. (всего {C_NUM}+2{C_BODY} ед.)."},
            3: {"effect": f"Увеличивает защиту всех наземных и летающих войск ещё на {C_NUM}1{C_BODY} ед. (всего {C_NUM}+3{C_BODY} ед.)."}
        }
    },
    # 3. Ranged Weapons (3 levels)
    "R0I1": {
        "name": "Оружие дальнего боя",
        "hotkey": "R",
        "max_level": 3,
        "targets": f"{C_REF}Охотников{C_BODY}, {C_REF}Катапульты{C_BODY}, {C_REF}Жрецов{C_BODY}, {C_REF}Жрецов Лоа{C_BODY}, {C_REF}Взывателей душ{C_BODY} и {C_REF}Ледяных Змей{C_BODY}",
        "levels": {
            1: {"effect": f"Увеличивает урон стрелковых и осадных атак на {C_NUM}1{C_BODY} ед."},
            2: {"effect": f"Увеличивает урон стрелковых и осадных атак ещё на {C_NUM}1{C_BODY} ед. (всего {C_NUM}+2{C_BODY} ед.)."},
            3: {"effect": f"Увеличивает урон стрелковых и осадных атак ещё на {C_NUM}1{C_BODY} ед. (всего {C_NUM}+3{C_BODY} ед.)."}
        }
    },
    # 4. Troll Regeneration (3 levels)
    "R0I2": {
        "name": "Тролльская регенерация",
        "hotkey": "T",
        "max_level": 3,
        "targets": f"всех троллей ({C_REF}Работников{C_BODY}, {C_REF}Воителей{C_BODY}, {C_REF}Охотников{C_BODY}, {C_REF}Жрецов{C_BODY}, {C_REF}Жрецов Лоа{C_BODY}, {C_REF}Взывателей душ{C_BODY}, {C_REF}Берсерков{C_BODY} и героев)",
        "levels": {
            1: {"effect": f"Ускоряет естественное восстановление здоровья троллей на {C_NUM}0,3{C_BODY} ед. в секунду."},
            2: {"effect": f"Ускоряет естественное восстановление здоровья троллей ещё на {C_NUM}0,3{C_BODY} ед. в секунду (всего {C_NUM}+0,6{C_BODY} ед./сек.)."},
            3: {"effect": f"Ускоряет естественное восстановление здоровья троллей ещё на {C_NUM}0,3{C_BODY} ед. в секунду (всего {C_NUM}+0,9{C_BODY} ед./сек.)."}
        }
    },
    # 5. Drakkari Vitality (3 levels)
    "R0I3": {
        "name": "Живучесть Драккари",
        "hotkey": "V",
        "max_level": 3,
        "targets": f"всех троллей ({C_REF}Работников{C_BODY}, {C_REF}Воителей{C_BODY}, {C_REF}Охотников{C_BODY}, {C_REF}Жрецов{C_BODY}, {C_REF}Жрецов Лоа{C_BODY}, {C_REF}Взывателей душ{C_BODY}, {C_REF}Берсерков{C_BODY} и героев)",
        "levels": {
            1: {"effect": f"Увеличивает максимальный запас здоровья троллей на {C_NUM}50{C_BODY} ед."},
            2: {"effect": f"Увеличивает максимальный запас здоровья троллей ещё на {C_NUM}50{C_BODY} ед. (всего {C_NUM}+100{C_BODY} ед.)."},
            3: {"effect": f"Увеличивает максимальный запас здоровья троллей ещё на {C_NUM}50{C_BODY} ед. (всего {C_NUM}+150{C_BODY} ед.)."}
        }
    },
    # 6. Improved Axes (1 level)
    "R0IF": {
        "name": "Улучшенные топоры",
        "hotkey": "X",
        "max_level": 1,
        "targets": f"{C_REF}Работников{C_BODY}",
        "levels": {
            1: {"effect": f"Увеличивает объём древесины, переносимой работниками за один раз, на {C_NUM}5{C_BODY} ед."}
        }
    },
    # 7. Light Axes (1 level)
    "R0I7": {
        "name": "Облегченные топоры",
        "hotkey": "L",
        "max_level": 1,
        "targets": f"{C_REF}Воителей{C_BODY} и {C_REF}Охотников{C_BODY}",
        "levels": {
            1: {"effect": f"Делает боевые и метательные топоры легче, увеличивая скорость атаки воинов на {C_NUM}10%{C_BODY}."}
        }
    },
    # 8. Troll Training (3 levels)
    "R0IE": {
        "name": "Тренировки троллей",
        "hotkey": "T",
        "max_level": 3,
        "targets": f"всех троллей ({C_REF}Работников{C_BODY}, {C_REF}Воителей{C_BODY}, {C_REF}Охотников{C_BODY}, {C_REF}Жрецов{C_BODY}, {C_REF}Жрецов Лоа{C_BODY}, {C_REF}Взывателей душ{C_BODY}, {C_REF}Берсерков{C_BODY})",
        "levels": {
            1: {"effect": f"Увеличивает скорость передвижения троллей на {C_NUM}40{C_BODY} ед. и урон от атак на {C_NUM}4{C_BODY} ед."},
            2: {"effect": f"Увеличивает скорость передвижения троллей ещё на {C_NUM}40{C_BODY} ед. и урон на {C_NUM}4{C_BODY} ед. (всего {C_NUM}+80{C_BODY} скорости и {C_NUM}+8{C_BODY} урона)."},
            3: {"effect": f"Увеличивает скорость передвижения троллей ещё на {C_NUM}40{C_BODY} ед. и урон на {C_NUM}4{C_BODY} ед. (всего {C_NUM}+120{C_BODY} скорости и {C_NUM}+12{C_BODY} урона)."}
        }
    },
    # 9. Priest Training (1 level)
    "R0EU": {
        "name": "Познания жреца",
        "hotkey": "P",
        "max_level": 1,
        "targets": f"{C_REF}Жрецов{C_BODY}",
        "levels": {
            1: {"effect": f"Повышает мастерство Жрецов: увеличивает их запас здоровья на {C_NUM}40{C_BODY} ед., маны — на {C_NUM}100{C_BODY} ед., скорость восстановления маны — на {C_NUM}0,325{C_BODY} ед./сек. и открывает способности «Рассеивание заклинаний» и «Морозный доспех»."}
        }
    },
    # 10. Loa Knowledge (1 level)
    "R0I4": {
        "name": "Знания Лоа",
        "hotkey": "K",
        "max_level": 1,
        "targets": f"{C_REF}Жрецов Лоа{C_BODY}",
        "levels": {
            1: {"effect": f"Повышает мастерство Жрецов Лоа: увеличивает их запас здоровья на {C_NUM}50{C_BODY} ед., маны — на {C_NUM}70{C_BODY} ед., скорость восстановления маны — на {C_NUM}0,325{C_BODY} ед./сек. и открывает способности «Злоба Лоа» и «Призыв змеи»."}
        }
    },
    # 11. Soul Caller Training (2 levels)
    "R09L": {
        "name": "Азы загробного мира",
        "hotkey": "S",
        "max_level": 2,
        "targets": f"{C_REF}Взывателей душ{C_BODY}",
        "levels": {
            1: {"effect": f"Обучает Взывателей душ: увеличивает их здоровье на {C_NUM}40{C_BODY} ед., урон — на {C_NUM}4{C_BODY} ед., ману — на {C_NUM}35{C_BODY} ед. и открывает способность «Похищение жизни»."},
            2: {"effect": f"Возводит Взывателей душ в ранг мастеров смерти: увеличивает здоровье ещё на {C_NUM}40{C_BODY} ед., урон — на {C_NUM}4{C_BODY} ед., ману — на {C_NUM}35{C_BODY} ед. (всего {C_NUM}+80{C_BODY} HP, {C_NUM}+8{C_BODY} урона, {C_NUM}+70{C_BODY} MP) и открывает способность «Воскрешение падших»."}
        }
    },
    # 12. Beast Training (3 levels)
    "R0I6": {
        "name": "Тренировка зверей",
        "hotkey": "B",
        "max_level": 3,
        "targets": f"{C_REF}Белых медведей{C_BODY}, {C_REF}Лютых мамонтов{C_BODY}, {C_REF}Магнатавров-разрушителей{C_BODY} и Лоа ({C_REF}Акали{C_BODY}, {C_REF}Мам'тота{C_BODY}, {C_REF}Рунока{C_BODY})",
        "levels": {
            1: {"effect": f"Увеличивает скорость передвижения подчинённых зверей на {C_NUM}15{C_BODY} ед., урон от атак — на {C_NUM}5{C_BODY} ед. и здоровье — на {C_NUM}50{C_BODY} ед."},
            2: {"effect": f"Увеличивает скорость передвижения зверей ещё на {C_NUM}15{C_BODY} ед., урон — на {C_NUM}5{C_BODY} ед. и здоровье — на {C_NUM}50{C_BODY} ед. (всего {C_NUM}+30{C_BODY} скорости, {C_NUM}+10{C_BODY} урона, {C_NUM}+100{C_BODY} HP)."},
            3: {"effect": f"Увеличивает скорость передвижения зверей ещё на {C_NUM}15{C_BODY} ед., урон — на {C_NUM}5{C_BODY} ед. и здоровье — на {C_NUM}50{C_BODY} ед. (всего {C_NUM}+45{C_BODY} скорости, {C_NUM}+15{C_BODY} урона, {C_NUM}+150{C_BODY} HP)."}
        }
    },
    # 13. Wild Ice Magic (2 levels)
    "R0I5": {
        "name": "Дикая магия льда",
        "hotkey": "W",
        "max_level": 2,
        "targets": f"{C_REF}Магнатавров-разрушителей{C_BODY}",
        "levels": {
            1: {"effect": f"Увеличивает здоровье Магнатавра на {C_NUM}40{C_BODY} ед., урон — на {C_NUM}4{C_BODY} ед., ману — на {C_NUM}35{C_BODY} ед. и открывает способность «Кольцо льда»."},
            2: {"effect": f"Увеличивает здоровье Магнатавра ещё на {C_NUM}40{C_BODY} ед., урон — на {C_NUM}4{C_BODY} ед., ману — на {C_NUM}35{C_BODY} ед. (всего {C_NUM}+80{C_BODY} HP, {C_NUM}+8{C_BODY} урона, {C_NUM}+70{C_BODY} MP) и открывает способность «Невосприимчивость к магии»."}
        }
    },
    # 14. Countless Battles (2 levels)
    "R0IG": {
        "name": "Бесчисленные бои",
        "hotkey": "C",
        "max_level": 2,
        "targets": f"{C_REF}Берсерков{C_BODY}",
        "levels": {
            1: {"effect": f"Закаляет Берсерка в непрестанных сражениях: увеличивает его здоровье на {C_NUM}40{C_BODY} ед. и открывает способности «Берсерк» и «Сокрушение»."},
            2: {"effect": f"Возводит Берсерка в ранг непобедимого гладиатора: увеличивает здоровье ещё на {C_NUM}40{C_BODY} ед. (всего {C_NUM}+80{C_BODY} HP) и улучшает способность до «Усиленного сокрушения» (урон по области {C_NUM}60{C_BODY} ед. в радиусе {C_NUM}350{C_BODY})."}
        }
    },
    # 15. Dark Elements (2 levels)
    "R09P": {
        "name": "Тёмные элементы",
        "hotkey": "D",
        "max_level": 2,
        "targets": f"{C_REF}Големов{C_BODY}",
        "levels": {
            1: {"effect": f"Внедряет в голема древние тёмные кристаллы: увеличивает его здоровье на {C_NUM}50{C_BODY} ед., атаку — на {C_NUM}4{C_BODY} ед. и открывает способность «Пожирание магии»."},
            2: {"effect": f"Завершает насыщение голема магией Бездны: увеличивает здоровье ещё на {C_NUM}50{C_BODY} ед. и атаку — на {C_NUM}4{C_BODY} ед. (всего {C_NUM}+100{C_BODY} HP, {C_NUM}+8{C_BODY} урона) и открывает способность «Магический обстрел»."}
        }
    },
    # 16. Runok Absorption (3 levels)
    "R0AD": {
        "name": "Поглощение Рунока",
        "hotkey": "Q",
        "max_level": 3,
        "targets": f"все войска троллей ({C_REF}Работников{C_BODY}, {C_REF}Воителей{C_BODY}, {C_REF}Охотников{C_BODY}, {C_REF}Жрецов{C_BODY}, {C_REF}Жрецов Лоа{C_BODY}, {C_REF}Взывателей душ{C_BODY}, {C_REF}Берсерков{C_BODY})",
        "levels": {
            1: {"effect": f"Поглощает яростную силу Лоа Рунока, увеличивая скорость атаки всех войск на {C_NUM}10%{C_BODY}."},
            2: {"effect": f"Усиливает приток энергии Рунока, увеличивая скорость атаки войск ещё на {C_NUM}10%{C_BODY} (всего {C_NUM}+20%{C_BODY})."},
            3: {"effect": f"Достигает полного слияния с духом Рунока, увеличивая скорость атаки войск ещё на {C_NUM}10%{C_BODY} (всего {C_NUM}+30%{C_BODY})."}
        }
    },
    # 17. Akali Absorption (3 levels)
    "R0AI": {
        "name": "Поглощение Акали",
        "hotkey": "W",
        "max_level": 3,
        "targets": f"все войска троллей ({C_REF}Работников{C_BODY}, {C_REF}Воителей{C_BODY}, {C_REF}Охотников{C_BODY}, {C_REF}Жрецов{C_BODY}, {C_REF}Жрецов Лоа{C_BODY}, {C_REF}Взывателей душ{C_BODY}, {C_REF}Берсерков{C_BODY})",
        "levels": {
            1: {"effect": f"Поглощает хищную мощь Лоа Акали, увеличивая урон от любых атак всех войск на {C_NUM}4{C_BODY} ед."},
            2: {"effect": f"Усиливает приток энергии Акали, увеличивая урон от атак войск ещё на {C_NUM}4{C_BODY} ед. (всего {C_NUM}+8{C_BODY} ед.)."},
            3: {"effect": f"Достигает полного слияния с духом Акали, увеличивая урон от атак войск ещё на {C_NUM}4{C_BODY} ед. (всего {C_NUM}+12{C_BODY} ед.)."}
        }
    },
    # 18. Mam'toth Absorption (3 levels)
    "R0AJ": {
        "name": "Поглощение Мам'Тота",
        "hotkey": "E",
        "max_level": 3,
        "targets": f"все войска троллей ({C_REF}Работников{C_BODY}, {C_REF}Воителей{C_BODY}, {C_REF}Охотников{C_BODY}, {C_REF}Жрецов{C_BODY}, {C_REF}Жрецов Лоа{C_BODY}, {C_REF}Взывателей душ{C_BODY}, {C_REF}Берсерков{C_BODY})",
        "levels": {
            1: {"effect": f"Поглощает несокрушимую стойкость Лоа Мам'тота, увеличивая максимальный запас здоровья всех войск на {C_NUM}75{C_BODY} ед."},
            2: {"effect": f"Усиливает приток энергии Мам'тота, увеличивая здоровье войск ещё на {C_NUM}75{C_BODY} ед. (всего {C_NUM}+150{C_BODY} ед.)."},
            3: {"effect": f"Достигает полного слияния с духом Мам'тота, увеличивая здоровье войск ещё на {C_NUM}75{C_BODY} ед. (всего {C_NUM}+225{C_BODY} ед.)."}
        }
    },
    # 19. Emergency Measures Marker (1 level)
    "R0IX": {
        "name": "Чрезвычайные меры",
        "hotkey": "",
        "max_level": 1,
        "targets": f"армию {C_REF}Драккари{C_BODY}",
        "extra_notes": f"{C_DEBUFF}Внутренний маркер:{C_BODY} выдаётся при завершении ритуала «Чрезвычайные меры».",
        "levels": {
            1: {"effect": f"Обозначает выбор пути жертвоприношения Лоа: разблокирует наём {C_REF}Взывателей душ{C_BODY}, создание {C_REF}Големов{C_BODY}, найм героя {C_REF}Властелина Холода{C_BODY} и {C_NUM}3{C_BODY} уровня исследований поглощения Лоа."}
        }
    },
    # 20. Loa Worship Marker (1 level)
    "R0IY": {
        "name": "Ритуал поклонения",
        "hotkey": "",
        "max_level": 1,
        "targets": f"армию {C_REF}Драккари{C_BODY}",
        "extra_notes": f"{C_DEBUFF}Внутренний маркер:{C_BODY} выдаётся при завершении ритуала «Ритуал поклонения».",
        "levels": {
            1: {"effect": f"Обозначает выбор пути служения Лоа: разблокирует наём {C_REF}Лютых мамонтов{C_BODY}, {C_REF}Магнатавров-разрушителей{C_BODY} и святилища для призыва Лоа — {C_REF}Рунока{C_BODY}, {C_REF}Мам'тота{C_BODY} и {C_REF}Акали{C_BODY}."}
        }
    }
}

operations = []
registry_entries = []

for qid, info in RESEARCH_DATA.items():
    name = info["name"]
    hotkey = info["hotkey"]
    max_level = info["max_level"]
    targets = info["targets"]
    extra_notes = info.get("extra_notes")
    
    clean_name = f"{C_TITLE}{name}{C_RESET}"
    entry_levels = []
    for l in range(1, max_level + 1):
        lvl_info = info["levels"][l]
        tip_val = fmt_research_tip(name, level=l, max_level=max_level, hotkey=hotkey if l == 1 and hotkey else None)
        ub_val = fmt_research_desc(lvl_info["effect"], targets, level=l, max_level=max_level, extra_notes=extra_notes)
        name_val = f"{C_TITLE}{name}{C_RESET}"
        if max_level > 1:
            name_val += f" — уровень {C_NUM}{l}{C_RESET}"
            
        operations.append({"type": "upgrade", "id": qid, "field": f"name{l}", "value": name_val})
        operations.append({"type": "upgrade", "id": qid, "field": f"tip{l}", "value": tip_val})
        operations.append({"type": "upgrade", "id": qid, "field": f"ubertip{l}", "value": ub_val})
        
        entry_levels.append({
            "level": l,
            "name": name_val,
            "tip": tip_val,
            "ubertip": ub_val
        })
        
    registry_entries.append({
        "id": qid,
        "name": clean_name,
        "hotkey": hotkey,
        "max_level": max_level,
        "targets": targets,
        "levels": entry_levels
    })

# Save plan
plan_doc = {"operations": operations}
plan_path = ROOT / "docs" / "ui_text" / "ice_troll_research_plan.json"
plan_path.write_text(json.dumps(plan_doc, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(operations)} operations in {plan_path}")

# Save registry
registry_doc = {
    "scope": "Ледяные тролли: вся категория исследований — 20 объектов (включая расовые маркеры R0IX и R0IY), 45 действующих уровней",
    "total_upgrades": len(RESEARCH_DATA),
    "total_operations": len(operations),
    "upgrades": registry_entries
}
registry_path = ROOT / "docs" / "ui_text" / "ice_troll_research.json"
registry_path.write_text(json.dumps(registry_doc, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated registry in {registry_path}")
