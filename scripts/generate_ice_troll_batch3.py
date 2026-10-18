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

def fmt_ability_title(name, hotkey=None):
    if hotkey:
        return f"{C_TITLE}{name}{C_RESET} ({C_NUM}{hotkey}{C_RESET})"
    return f"{C_TITLE}{name}{C_RESET}"

def fmt_ability_desc(effect_body):
    return f"{C_TAG}СПОСОБНОСТЬ:{C_BODY} {effect_body}{C_RESET}"

def fmt_buff_desc(effect_body):
    return f"{C_TAG}ЭФФЕКТ:{C_BODY} {effect_body}{C_RESET}"

# 1. Building abilities / rituals
ABILITIES_DATA = {
    "A1FR": {
        "name": "Ритуал поклонения",
        "hotkey": "E",
        "desc": f"Подтверждает нерушимый союз племени Драккари с дикими богами. Открывает наём {C_REF}Лютых мамонтов{C_BODY}, {C_REF}Магнатавров-разрушителей{C_BODY} и строительство святилищ для призыва могущественных Лоа — {C_REF}Рунока{C_BODY}, {C_REF}Мам'тота{C_BODY} и {C_REF}Акали{C_BODY}.|n|n{C_DEBUFF}Внимание:{C_BODY} навсегда блокирует «Чрезвычайные меры» и поглощение сил Лоа."
    },
    "A1FS": {
        "name": "Чрезвычайные меры",
        "hotkey": "R",
        "desc": f"Приносит священных Лоа в жертву ради выживания племени. Открывает наём {C_REF}Взывателей душ{C_BODY}, создание {C_REF}Големов{C_BODY}, найм героя {C_REF}Властелина Холода{C_BODY} и {C_NUM}3{C_BODY} уровня исследований поглощения сил Лоа.|n|n{C_DEBUFF}Внимание:{C_BODY} навсегда блокирует «Ритуал поклонения» и призыв Лоа на поле боя."
    }
}

# 2. Buffs
BUFFS_DATA = {
    "B07I": {
        "name": "Морозное оружие",
        "desc": f"Цель заморожена: скорость передвижения {C_DEBUFF}снижена на 20%{C_BODY}, скорость атаки — {C_DEBUFF}на 15%{C_BODY}, цель получает {C_DEBUFF}1{C_BODY} ед. урона каждую секунду."
    },
    "B08L": {
        "name": "Угасание жизни",
        "desc": f"На цель наложено проклятье: юнит каждую секунду {C_DEBUFF}теряет 10 ед. здоровья{C_BODY}."
    },
    "B08M": {
        "name": "Проклятый шепот",
        "desc": f"Тёмный шепот древних духов {C_DEBUFF}снижает броню цели на 2 ед.{C_BODY}"
    },
    "B08N": {
        "name": "Вспышка маны",
        "desc": f"Любая попытка сотворить заклинание {C_DEBUFF}вызовет взрыв маны{C_BODY}, наносящий урон цели и находящимся рядом союзникам."
    },
    "B08O": {
        "name": "Тёмная перегрузка",
        "desc": f"Цель поражена тёмной магией шакрамов и периодически {C_DEBUFF}получает урон{C_BODY}."
    },
    "B08P": {
        "name": "Аура Рунока",
        "desc": f"Дух Рунока наполняет союзника стойкостью: броня {C_BUFF}увеличена на 4 ед.{C_BODY}"
    },
    "B08Q": {
        "name": "Аура Мам'Тота",
        "desc": f"Мощь Мам'тота ведёт воинов вперёд: скорость передвижения {C_BUFF}увеличена на 20%{C_BODY}, скорость атаки — {C_BUFF}на 20%{C_BODY}."
    },
    "B08R": {
        "name": "Аура Акали",
        "desc": f"Благословение хищного Лоа: урон от любых атак {C_BUFF}увеличен на 15%{C_BODY}."
    },
    "B08S": {
        "name": "Ярость",
        "desc": f"Рунок охвачен боевой яростью: скорость атаки {C_BUFF}увеличена на 50%{C_BODY}."
    },
    "B08T": {
        "name": "Приморозка",
        "desc": f"Скован вечной мерзлотой: цель {C_DEBUFF}не может двигаться{C_BODY}."
    },
    "B08U": {
        "name": "Ледяная стойкость",
        "desc": f"Ледяной панцирь защищает героя: броня {C_BUFF}увеличена{C_BODY}."
    }
}

operations = []

# Ability operations
for aid, info in ABILITIES_DATA.items():
    name = info["name"]
    hotkey = info["hotkey"]
    clean_name = f"{C_TITLE}{name}{C_RESET}"
    tip = fmt_ability_title(name, hotkey)
    ub = fmt_ability_desc(info["desc"])
    
    operations.append({"type": "ability", "id": aid, "field": "name", "value": clean_name})
    operations.append({"type": "ability", "id": aid, "field": "tip1", "value": tip})
    operations.append({"type": "ability", "id": aid, "field": "ubertip1", "value": ub})

# Buff operations
for bid, info in BUFFS_DATA.items():
    name = info["name"]
    clean_name = f"{C_TITLE}{name}{C_RESET}"
    desc = fmt_buff_desc(info["desc"])
    
    operations.append({"type": "buff", "id": bid, "field": "editorname", "value": clean_name})
    operations.append({"type": "buff", "id": bid, "field": "bufftip", "value": clean_name})
    operations.append({"type": "buff", "id": bid, "field": "buffubertip", "value": desc})

# Save plan
plan_doc = {"operations": operations}
plan_path = ROOT / "docs" / "ui_text" / "ice_troll_batch3_plan.json"
plan_path.write_text(json.dumps(plan_doc, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(operations)} operations in {plan_path}")

# Save registry
registry_doc = {
    "scope": "Ледяные тролли: строительные способности/ритуалы (A1FR, A1FS) и 11 собственных эффектов (баффов) — партия 3",
    "total_abilities": len(ABILITIES_DATA),
    "total_buffs": len(BUFFS_DATA),
    "total_operations": len(operations),
    "abilities": [
        {
            "id": aid,
            "name": f"{C_TITLE}{info['name']}{C_RESET}",
            "tip1": fmt_ability_title(info["name"], info["hotkey"]),
            "ubertip1": fmt_ability_desc(info["desc"])
        } for aid, info in ABILITIES_DATA.items()
    ],
    "buffs": [
        {
            "id": bid,
            "editorname": f"{C_TITLE}{info['name']}{C_RESET}",
            "bufftip": f"{C_TITLE}{info['name']}{C_RESET}",
            "buffubertip": fmt_buff_desc(info["desc"])
        } for bid, info in BUFFS_DATA.items()
    ]
}
registry_path = ROOT / "docs" / "ui_text" / "ice_troll_batch3.json"
registry_path.write_text(json.dumps(registry_doc, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated registry in {registry_path}")
