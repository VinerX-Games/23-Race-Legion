# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw

# Color constants
C_TITLE = "|cffe4cfa3"
C_TAG = "|cffa6afb8"
C_BODY = "|cffced4da"
C_NUM = "|cffffffff"
C_RESET = "|r"

def fmt_title(name, hotkey=None):
    if hotkey:
        return f"{C_TITLE}{name}{C_RESET} ({C_NUM}{hotkey}{C_RESET})"
    return f"{C_TITLE}{name}{C_RESET}"

def fmt_desc(effect_body, autocast=False):
    res = f"{C_TAG}СПОСОБНОСТЬ:{C_BODY} {effect_body}{C_RESET}"
    if autocast:
        res = f"{C_TAG}СПОСОБНОСТЬ:{C_BODY} {effect_body}|n|n{C_TAG}Автоприменение:{C_BODY} переключается правой кнопкой мыши.{C_RESET}"
    return res

# Define the dictionary of all 31 unit abilities
ABILITIES_DATA = {
    "A10O": {
        "name": "Опутывание",
        "hotkey": "E",
        "levels": 1,
        "holders": ["n05T (Охотник)"],
        "desc": {
            1: f"Притягивает врага сетями к земле и обездвиживает его на {C_NUM}2{C_BODY} сек. (героев — на {C_NUM}1{C_BODY} сек.). Опутанные летающие цели становятся уязвимы для ближнего боя."
        }
    },
    "A1CL": {
        "name": "Рассеивание заклинаний",
        "hotkey": "W",
        "levels": 1,
        "holders": ["n05U (Жрец)"],
        "desc": {
            1: f"Снимает все магические эффекты с юнитов в области радиусом {C_NUM}200{C_BODY} и наносит {C_NUM}200{C_BODY} ед. урона призванным существам."
        }
    },
    "A1CM": {
        "name": "Ледяная стрела",
        "hotkey": "Q",
        "levels": 1,
        "holders": ["n05Z (Жрец Лоа)", "n05X (Магнатавр-разрушитель)"],
        "desc": {
            1: f"Выпускает во врага ледяной заряд, наносящий {C_NUM}100{C_BODY} ед. урона и оглушающий цель на {C_NUM}0,5{C_BODY} сек."
        }
    },
    "A1CN": {
        "name": "Злоба Лоа",
        "hotkey": "W",
        "levels": 1,
        "autocast": True,
        "holders": ["n05Z (Жрец Лоа)"],
        "desc": {
            1: f"Взывает к ярости Лоа, увеличивая скорость атаки союзника на {C_NUM}20%{C_BODY} и скорость передвижения на {C_NUM}20%{C_BODY} на {C_NUM}60{C_BODY} сек."
        }
    },
    "A1CO": {
        "name": "Исцеление",
        "hotkey": "Q",
        "levels": 1,
        "autocast": True,
        "holders": ["n05U (Жрец)"],
        "desc": {
            1: f"Восстанавливает раненому живому союзнику {C_NUM}15{C_BODY} ед. здоровья. Не действует на технику."
        }
    },
    "A1CP": {
        "name": "Морозный доспех",
        "hotkey": "E",
        "levels": 1,
        "autocast": True,
        "holders": ["n05U (Жрец)"],
        "desc": {
            1: f"Укрывает союзника ледяным щитом на {C_NUM}45{C_BODY} сек., повышающим защиту на {C_NUM}3{C_BODY} ед. Ближние атаки врагов по защищённой цели замедляют их на {C_NUM}3{C_BODY} сек."
        }
    },
    "A1CR": {
        "name": "Разрывающие удары",
        "hotkey": "",
        "levels": 1,
        "holders": ["n05V (Белый медведь)", "n061 (Рунок)"],
        "desc": {
            1: f"Атаки наносят на {C_NUM}10%{C_BODY} больше урона целям с тяжёлой бронёй."
        }
    },
    "A1CS": {
        "name": "Сильный удар",
        "hotkey": "",
        "levels": 1,
        "holders": ["n05V (Белый медведь)", "n061 (Рунок)"],
        "desc": {
            1: f"Даёт {C_NUM}15%{C_BODY}-й шанс при атаке нанести дополнительно {C_NUM}25{C_BODY} ед. урона и оглушить цель на {C_NUM}2{C_BODY} сек. (героев — на {C_NUM}1{C_BODY} сек.)."
        }
    },
    "A1CT": {
        "name": "Рассекающий удар",
        "hotkey": "",
        "levels": 1,
        "holders": ["n05W (Лютый мамонт)", "n062 (Мам'тот)"],
        "desc": {
            1: f"Удары по наземным противникам передают {C_NUM}13%{C_BODY} урона соседним вражеским целям в радиусе {C_NUM}150{C_BODY}."
        }
    },
    "A1CV": {
        "name": "Кольцо льда",
        "hotkey": "E",
        "levels": 1,
        "holders": ["n05X (Магнатавр-разрушитель)"],
        "desc": {
            1: f"Выпускает ледяную волну, наносящую {C_NUM}100{C_BODY} ед. урона цели и {C_NUM}50{C_BODY} ед. урона по области радиусом {C_NUM}200{C_BODY}, замедляя передвижение и атаку поражённых врагов на {C_NUM}2{C_BODY} сек."
        }
    },
    "A1CW": {
        "name": "Критический удар",
        "hotkey": "",
        "levels": 1,
        "holders": ["n05T (Охотник)"],
        "desc": {
            1: f"Даёт {C_NUM}20%{C_BODY}-й шанс при атаке нанести {C_NUM}2{C_BODY}-кратный урон."
        }
    },
    "A1D6": {
        "name": "Сокрушение",
        "hotkey": "",
        "levels": 2,
        "holders": ["n05Y (Берсерк)"],
        "level_names": {
            1: "Сокрушение",
            2: "Усиленное сокрушение"
        },
        "desc": {
            1: f"При каждой атаке даёт {C_NUM}25%{C_BODY}-й шанс нанести {C_NUM}15{C_BODY} ед. урона ближайшим наземным противникам в радиусе {C_NUM}200{C_BODY}.",
            2: f"При каждой атаке даёт {C_NUM}25%{C_BODY}-й шанс нанести {C_NUM}60{C_BODY} ед. урона ближайшим наземным противникам в радиусе {C_NUM}350{C_BODY}."
        }
    },
    "A1D7": {
        "name": "Берсерк",
        "hotkey": "W",
        "levels": 1,
        "holders": ["n05Y (Берсерк)"],
        "desc": {
            1: f"На {C_NUM}12{C_BODY} сек. повышает скорость атаки берсерка на {C_NUM}50%{C_BODY}, но увеличивает весь получаемый им урон на {C_NUM}40%{C_BODY}."
        }
    },
    "A1DP": {
        "name": "Невосприимчивость к магии",
        "hotkey": "",
        "levels": 1,
        "holders": ["n05X (Магнатавр-разрушитель)"],
        "desc": {
            1: f"Дарует полную невосприимчивость к враждебным заклинаниям и большинству магических воздействий."
        }
    },
    "A1FF": {
        "name": "Морозное оружие",
        "hotkey": "",
        "levels": 1,
        "holders": ["n05S (Воитель)", "n05T (Охотник)", "n05U (Жрец)", "n05Z (Жрец Лоа)", "n05Y (Берсерк)", "n07F (Ледяная Змея)"],
        "desc": {
            1: f"Атаки покрывают цель льдом, снижая скорость её передвижения на {C_NUM}20%{C_BODY}, скорость атаки — на {C_NUM}15%{C_BODY} и нанося {C_NUM}1{C_BODY} ед. урона в секунду. Действует {C_NUM}5{C_BODY} сек. (героев — {C_NUM}1{C_BODY} сек.)."
        }
    },
    "A1FU": {
        "name": "Муссон",
        "hotkey": "W",
        "levels": 1,
        "holders": ["o05B (Акали)"],
        "desc": {
            1: f"Призывает грозовой фронт в область радиусом {C_NUM}500{C_BODY} на {C_NUM}12{C_BODY} сек., периодически поражающий противников ударами молний с уроном {C_NUM}50{C_BODY} ед."
        }
    },
    "A1FV": {
        "name": "Цепная молния",
        "hotkey": "Q",
        "levels": 1,
        "holders": ["o05B (Акали)"],
        "desc": {
            1: f"Выпускает молнию, наносящую {C_NUM}120{C_BODY} ед. урона выбранному противнику и рикошетящую до {C_NUM}5{C_BODY} раз. Каждый последующий скачок наносит на {C_NUM}10%{C_BODY} меньше урона."
        }
    },
    "A1FX": {
        "name": "Реинкарнация",
        "hotkey": "",
        "levels": 1,
        "holders": ["n062 (Мам'тот)"],
        "desc": {
            1: f"После гибели Мам'тот возрождается на месте своей смерти через {C_NUM}5{C_BODY} сек. с полным запасом здоровья и маны.|n|nВремя восстановления: {C_NUM}240{C_BODY} сек."
        }
    },
    "A1FY": {
        "name": "Ярость",
        "hotkey": "E",
        "levels": 1,
        "holders": ["n061 (Рунок)"],
        "desc": {
            1: f"Вводит Рунока в состояние ярости, увеличивая скорость его атаки на {C_NUM}50%{C_BODY} на {C_NUM}20{C_BODY} сек. без увеличения получаемого урона."
        }
    },
    "A1OV": {
        "name": "Воскрешение падших",
        "hotkey": "E",
        "levels": 2,
        "autocast": True,
        "holders": ["n07B (Взыватель душ)"],
        "desc": {
            1: f"Поднимает из трупа союзного воина скелета-восставшего на {C_NUM}45{C_BODY} сек. Способность действует только на трупы союзников.",
            2: f"Поднимает из трупа союзного воина скелета-восставшего на {C_NUM}45{C_BODY} сек. Способность действует только на трупы союзников."
        }
    },
    "A1OW": {
        "name": "Угасание жизни",
        "hotkey": "Q",
        "levels": 1,
        "autocast": True,
        "holders": ["n07B (Взыватель душ)"],
        "desc": {
            1: f"Проклинает противника на {C_NUM}15{C_BODY} сек., нанося ему {C_NUM}10{C_BODY} ед. урона каждую секунду (всего {C_NUM}150{C_BODY} ед.)."
        }
    },
    "A1P4": {
        "name": "Похищение жизни",
        "hotkey": "W",
        "levels": 1,
        "holders": ["n07B (Взыватель душ)"],
        "desc": {
            1: f"Вытягивает у выбранного противника {C_NUM}45{C_BODY} ед. здоровья в секунду и передаёт его заклинателю. Действует до {C_NUM}8{C_BODY} сек."
        }
    },
    "A1P5": {
        "name": "Призыв змеи",
        "hotkey": "E",
        "levels": 1,
        "holders": ["n05Z (Жрец Лоа)"],
        "desc": {
            1: f"Призывает на {C_NUM}70{C_BODY} сек. Ледяную Змею с дальней атакой, замораживающей цели."
        }
    },
    "A1P6": {
        "name": "Проклятый шепот",
        "hotkey": "",
        "levels": 1,
        "holders": ["o04T (Голем)"],
        "desc": {
            1: f"Аура тёмной магии снижает защиту всех ближайших противников в радиусе {C_NUM}300{C_BODY} на {C_NUM}2{C_BODY} ед."
        }
    },
    "A1P9": {
        "name": "Аура Рунока",
        "hotkey": "",
        "levels": 1,
        "holders": ["n061 (Рунок)"],
        "desc": {
            1: f"Мощь духа Рунока повышает защиту союзных войск в радиусе {C_NUM}3000{C_BODY} на {C_NUM}4{C_BODY} ед."
        }
    },
    "A1PA": {
        "name": "Аура Акали",
        "hotkey": "",
        "levels": 1,
        "holders": ["o05B (Акали)"],
        "desc": {
            1: f"Аура хищного Лоа увеличивает урон от любых атак союзных войск в радиусе {C_NUM}3000{C_BODY} на {C_NUM}15%{C_BODY}."
        }
    },
    "A1PB": {
        "name": "Дикий натиск",
        "hotkey": "W",
        "levels": 1,
        "holders": ["n062 (Мам'тот)"],
        "desc": {
            1: f"Призывает стадо разъярённых мамонтов на {C_NUM}30{C_BODY} сек., бегущих вперёд и взрывающихся при столкновении с врагами, нанося по {C_NUM}60{C_BODY} ед. урона каждому."
        }
    },
    "A1PC": {
        "name": "Раздвоенная молния",
        "hotkey": "E",
        "levels": 1,
        "holders": ["o05B (Акали)"],
        "desc": {
            1: f"Выпускает веер молний в секторе перед собой, поражающий до {C_NUM}10{C_BODY} противников и наносящий каждому {C_NUM}500{C_BODY} ед. урона."
        }
    },
    "A1PI": {
        "name": "Пожирание магии",
        "hotkey": "W",
        "levels": 1,
        "holders": ["o04T (Голем)"],
        "desc": {
            1: f"Поглощает все магические эффекты с юнитов в радиусе {C_NUM}200{C_BODY}, восстанавливая голему {C_NUM}50{C_BODY} ед. здоровья и {C_NUM}75{C_BODY} ед. маны за каждый снятый эффект, а также наносит {C_NUM}160{C_BODY} ед. урона призванным существам."
        }
    },
    "A1PJ": {
        "name": "Магический обстрел",
        "hotkey": "E",
        "levels": 1,
        "holders": ["o04T (Голем)"],
        "desc": {
            1: f"Обрушивает на указанную область радиусом {C_NUM}350{C_BODY} залп тёмных снарядов, наносящий противникам {C_NUM}100{C_BODY} ед. урона и оглушающий их."
        }
    },
    "S00F": {
        "name": "Аура Мам'Тота",
        "hotkey": "",
        "levels": 1,
        "holders": ["n062 (Мам'тот)"],
        "desc": {
            1: f"Величественная аура Мам'тота увеличивает скорость передвижения на {C_NUM}20%{C_BODY} и скорость атаки на {C_NUM}20%{C_BODY} всех союзных войск в радиусе {C_NUM}3000{C_BODY}."
        }
    }
}

# Load raw before data
raw_path = ROOT / "docs" / "ui_text" / "ice_troll_unit_abilities_raw.json"
raw_data = json.loads(raw_path.read_text(encoding="utf-8"))
raw_lookup = {item["id"]: item for item in raw_data}

operations = []
registry_entries = []

for aid, info in ABILITIES_DATA.items():
    raw_item = raw_lookup.get(aid, {})
    raw_fields = raw_item.get("fields", {})
    name = info["name"]
    hotkey = info["hotkey"]
    levels = info["levels"]
    autocast = info.get("autocast", False)
    level_names = info.get("level_names", {})
    
    # name
    clean_name = f"{C_TITLE}{name}{C_RESET}"
    operations.append({
        "type": "ability",
        "id": aid,
        "field": "name",
        "value": clean_name
    })
    
    # per-level tips, ubertips, and autocasts
    entry_levels = []
    for l in range(1, levels + 1):
        lvl_name = level_names.get(l, name)
        tip_val = fmt_title(lvl_name, hotkey if hotkey else None)
        ub_body = info["desc"][l]
        ub_val = fmt_desc(ub_body, autocast=autocast)
        
        operations.append({
            "type": "ability",
            "id": aid,
            "field": f"tip{l}",
            "value": tip_val
        })
        operations.append({
            "type": "ability",
            "id": aid,
            "field": f"ubertip{l}",
            "value": ub_val
        })
        
        lvl_entry = {
            "level": l,
            "tip": tip_val,
            "ubertip": ub_val
        }
        
        if autocast:
            untip_val = tip_val
            unub_val = ub_val
            operations.append({
                "type": "ability",
                "id": aid,
                "field": f"untip{l}",
                "value": untip_val
            })
            operations.append({
                "type": "ability",
                "id": aid,
                "field": f"unubertip{l}",
                "value": unub_val
            })
            lvl_entry["untip"] = untip_val
            lvl_entry["unubertip"] = unub_val
            
        entry_levels.append(lvl_entry)
        
    registry_entries.append({
        "id": aid,
        "code": raw_item.get("code", aid),
        "name": clean_name,
        "hotkey": hotkey,
        "levels": levels,
        "autocast": autocast,
        "holders": info["holders"],
        "levels_data": entry_levels
    })

# Save plan
plan_doc = {"operations": operations}
plan_path = ROOT / "docs" / "ui_text" / "ice_troll_unit_abilities_plan.json"
plan_path.write_text(json.dumps(plan_doc, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(operations)} operations in {plan_path}")

# Save registry
registry_doc = {
    "scope": "Ледяные тролли: способности войск, Лоа и призывов (партия 2) — 31 способность",
    "total_abilities": len(ABILITIES_DATA),
    "total_operations": len(operations),
    "abilities": registry_entries
}
registry_path = ROOT / "docs" / "ui_text" / "ice_troll_unit_abilities.json"
registry_path.write_text(json.dumps(registry_doc, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated registry in {registry_path}")
