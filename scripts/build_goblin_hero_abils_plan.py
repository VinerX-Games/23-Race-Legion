# -*- coding: utf-8 -*-
"""Generate detailed plan and texts for all 25 Goblin hero abilities."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
raw_path = ROOT / "docs/ui_text/goblin_hero_abils_raw.json"
abils = json.loads(raw_path.read_text(encoding="utf-8"))

hero_map = {
    # H0BD: Спецназовец
    "A0D8": ("Шоковая граната", "H0BD", "Q", 4),
    "A0D5": ("Осколочная граната", "H0BD", "W", 4),
    "AEar": ("Аура меткости", "H0BD", "E", 4),
    "A0D7": ("Артобстрел", "H0BD", "R", 2),

    # Galh: Алхимик
    "ANhs": ("Исцеляющий газ", "Galh", "Q", 4),
    "ANcr": ("Эликсир ярости", "Galh", "W", 4),
    "ANab": ("Кислотная бомба", "Galh", "E", 4),
    "ANtm": ("Трансмутация", "Galh", "R", 2),

    # Gmex: Механик
    "ANsy": ("Портативная фабрика", "Gmex", "Q", 4),
    "ANcs": ("Кассетные ракеты", "Gmex", "W", 4),
    "ANeg": ("Улучшенная инженерия", "Gmex", "E", 4),
    "ANrg": ("Робогоблин", "Gmex", "R", 2),

    # N018: Шеф Кабестана
    "A0DK": ("Самодельная турель", "N018", "Q", 4),
    "A0DL": ("Бочка-взрывучка", "N018", "W", 4),
    "A1KK": ("Разряд!", "N018", "E", 4),
    "A0DR": ("Поле саморемонта", "N018", "R", 2),

    # N019: Мастер осады
    "A0DU": ("Взрыв", "N019", "Q", 4),
    "A1N0": ("Портативный завод", "N019", "W", 4),
    "A1N3": ("Ракетопад", "N019", "E", 4),
    "A1N1": ("Автоматический ракетомет", "N019", "D", 3),
    "A1N4": ("Перезагрузка", "N019", "R", 2),

    # N01A: Торговый Принц
    "A0E1": ("Большая Красная Кнопка", "N01A", "R", 2),
    "A0E0": ("Разрывные пули", "N01A", "W", 4),
    "A0E2": ("Аура пропаганды", "N01A", "E", 4),
    "A13G": ("Призвать мехи", "N01A", "E", 4),
}

plan = {}
for aid, (name, hero, hotkey, max_lvl) in hero_map.items():
    raw_data = abils.get(aid, {})
    plan[aid] = {
        "id": aid,
        "name": name,
        "hero": hero,
        "hotkey": hotkey,
        "max_lvl": max_lvl,
        "raw": raw_data
    }

with open(ROOT / "docs/ui_text/goblin_hero_abils_plan_raw.json", "w", encoding="utf-8") as out:
    json.dump(plan, out, ensure_ascii=False, indent=2)

print(f"Plan raw saved for {len(plan)} abilities.")
