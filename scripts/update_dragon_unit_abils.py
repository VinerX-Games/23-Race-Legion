# -*- coding: utf-8 -*-
"""Update Dragon race unit abilities and buffs (37 abilities, 6 buffs) with SD/HD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require
from apply_faceless_object_text import patch_blob

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING {string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    w3a_path = ROOT / "map.w3x/war3map.w3a"
    w3a_skin_path = ROOT / "map.w3x/war3mapSkin.w3a"
    w3h_path = ROOT / "map.w3x/war3map.w3h"
    w3h_skin_path = ROOT / "map.w3x/war3mapSkin.w3h"

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    original_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()
    original_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()
    original_w3h_hash = hashlib.sha256(w3h_path.read_bytes()).hexdigest()
    original_w3h_skin_hash = hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name not in ["war3map.wts", "war3map.w3a", "war3mapSkin.w3a", "war3map.w3h", "war3mapSkin.w3h"]
    }

    # 34 custom abilities with visible command buttons
    unit_abilities = [
        # Worker / Scout
        {
            "id": "A1LR",
            "name": "|cffe4cfa3Связь с изумрудным сном|r",
            "wts": {"name": 39762, "tip1": 39761, "ubertip1": 21752},
            "values": {
                "name": "|cffe4cfa3Связь с изумрудным сном|r",
                "tip1": "|cffe4cfa3Связь с изумрудным сном|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При перемещении в Изумрудный Сон строитель не привлекает внимания местных духов.|r"
            }
        },
        {
            "id": "A0RK",
            "name": "|cffe4cfa3Родство с магией|r",
            "wts": {"name": 11988, "tip1": 13625, "ubertip1": 16379},
            "values": {
                "name": "|cffe4cfa3Родство с магией|r",
                "tip1": "|cffe4cfa3Родство с магией|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает получаемый магический урон на |cffffffff50%|cffced4da.|r"
            }
        },
        # Bronze Flight
        {
            "id": "drat",
            "name": "|cffe4cfa3Замедление|r",
            "hotkey": "Q",
            "wts": {"name": 39820, "tip1": 39821},
            "raw_patches": {
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет противника, снижая скорость его атаки на |cffffffff7,5%|cffced4da и скорость передвижения на |cffffffff10%|cffced4da на |cffffffff45|cffced4da сек. (на героях — |cffffffff10|cffced4da сек.).|r"
            },
            "values": {
                "name": "|cffe4cfa3Замедление|r",
                "tip1": "|cffe4cfa3Замедление|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет противника, снижая скорость его атаки на |cffffffff7,5%|cffced4da и скорость передвижения на |cffffffff10%|cffced4da на |cffffffff45|cffced4da сек. (на героях — |cffffffff10|cffced4da сек.).|r"
            }
        },
        {
            "id": "A0RE",
            "name": "|cffe4cfa3Ускользание|r",
            "wts": {"name": 16920, "tip1": 16921, "ubertip1": 16922},
            "values": {
                "name": "|cffe4cfa3Ускользание|r",
                "tip1": "|cffe4cfa3Ускользание|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff15%|cffced4da шанс уклониться от физической атаки врага.|r"
            }
        },
        {
            "id": "drAa",
            "name": "|cffe4cfa3Зеркальное изображение|r",
            "hotkey": "W",
            "wts": {"name": 39822, "tip1": 39823, "ubertip1": 23599},
            "values": {
                "name": "|cffe4cfa3Зеркальное изображение|r",
                "tip1": "|cffe4cfa3Зеркальное изображение|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт |cffffffff1|cffced4da иллюзорную копию дракона и снимает с него отрицательные эффекты. Копия наносит |cffffffff50%|cffced4da урона и получает |cffffffff100%|cffced4da урона.|nВремя действия: |cffffffff20|cffced4da сек.|r"
            }
        },
        {
            "id": "drAs",
            "name": "|cffe4cfa3Сингулярная перегрузка|r",
            "hotkey": "Q",
            "wts": {"name": 39825, "tip1": 39826, "ubertip1": 39827},
            "values": {
                "name": "|cffe4cfa3Сингулярная перегрузка|r",
                "tip1": "|cffe4cfa3Сингулярная перегрузка|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffffffff+20%|cffced4da и скорость передвижения на |cffffffff+15%|cffced4da на |cffffffff9|cffced4da сек.|r"
            }
        },
        {
            "id": "A0RO",
            "name": "|cffe4cfa3Возврат времени|r",
            "hotkey": "W",
            "wts": {"name": 17123, "tip1": 17124, "ubertip1": 39875},
            "values": {
                "name": "|cffe4cfa3Возврат времени|r",
                "tip1": "|cffe4cfa3Возврат времени|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет |cffffffff25|cffced4da ед. здоровья находящимся рядом союзникам в радиусе |cffffffff700|cffced4da.|r"
            }
        },
        {
            "id": "A0RJ",
            "name": "|cffe4cfa3Ускорение времени|r",
            "hotkey": "E",
            "wts": {"name": 16755, "tip1": 16990, "ubertip1": 2707},
            "values": {
                "name": "|cffe4cfa3Ускорение времени|r",
                "tip1": "|cffe4cfa3Ускорение времени|r (|cffffffffE|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки союзника на |cffffffff+15%|cffced4da и скорость передвижения на |cffffffff+10%|cffced4da на |cffffffff20|cffced4da сек.|r"
            }
        },
        {
            "id": "drAz",
            "name": "|cffe4cfa3Цепная молния|r",
            "hotkey": "Q",
            "wts": {"name": 11954, "tip1": 13753, "ubertip1": 41516},
            "values": {
                "name": "|cffe4cfa3Цепная молния|r",
                "tip1": "|cffe4cfa3Цепная молния|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель разрядом молнии, который наносит |cffffffff125|cffced4da ед. урона и перескакивает на соседних противников, поражая до |cffffffff5|cffced4da целей.|r"
            }
        },
        {
            "id": "drA2",
            "name": "|cffe4cfa3Перелет|r",
            "hotkey": "F",
            "wts": {"name": 3756, "tip1": 25492, "ubertip1": 25494},
            "values": {
                "name": "|cffe4cfa3Перелет|r",
                "tip1": "|cffe4cfa3Перелет|r (|cffffffffF|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дракон взмывает в воздух и перелетает в указанную точку на расстояние до |cffffffff4500|cffced4da, становясь уязвимым во время полёта.|r"
            }
        },
        # Green Flight
        {
            "id": "drAw",
            "name": "|cffe4cfa3Фазовый сдвиг|r",
            "hotkey": "D",
            "wts": {"name": 39764, "tip1": 39763},
            "raw_patches": {
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При получении урона дракончик мгновенно перемещается в иное измерение, избегая дальнейших атак.|nВремя действия: |cffffffff0,3|cffced4da сек.|r"
            },
            "values": {
                "name": "|cffe4cfa3Фазовый сдвиг|r",
                "tip1": "|cffe4cfa3Фазовый сдвиг|r (|cffffffffD|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При получении урона дракончик мгновенно перемещается в иное измерение, избегая дальнейших атак.|nВремя действия: |cffffffff0,3|cffced4da сек.|r"
            }
        },
        {
            "id": "drAy",
            "name": "|cffe4cfa3Множественная атака|r",
            "wts": {"name": 39773, "tip1": 39775, "ubertip1": 39774},
            "values": {
                "name": "|cffe4cfa3Множественная атака|r",
                "tip1": "|cffe4cfa3Множественная атака|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать до |cffffffff3|cffced4da целей одновременно в радиусе |cffffffff600|cffced4da.|r"
            }
        },
        {
            "id": "drAe",
            "name": "|cffe4cfa3Изгнание|r",
            "hotkey": "W",
            "wts": {"name": 39876, "tip1": 39765, "ubertip1": 39768},
            "values": {
                "name": "|cffe4cfa3Изгнание|r",
                "tip1": "|cffe4cfa3Изгнание|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Изгоняет цель в астральный план, снижая её скорость передвижения на |cffffffff50%|cffced4da. Изгнанная цель не может атаковать, но получает повышенный урон от заклинаний. Не действует на технику.|r"
            }
        },
        {
            "id": "drAr",
            "name": "|cffe4cfa3Гнев деревьев|r",
            "hotkey": "Q",
            "wts": {"name": 39769, "tip1": 39770, "ubertip1": 23598},
            "values": {
                "name": "|cffe4cfa3Гнев деревьев|r",
                "tip1": "|cffe4cfa3Гнев деревьев|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Опутывает противника корнями, обездвиживая его на |cffffffff12|cffced4da сек. (на героях — |cffffffff0,5|cffced4da сек.) и нанося |cffffffff20|cffced4da ед. урона в секунду.|r"
            }
        },
        {
            "id": "drEt",
            "name": "|cffe4cfa3Сон|r",
            "hotkey": "E",
            "wts": {"name": 39771, "tip1": 39772},
            "raw_patches": {
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Погружает выбранного противника в сон на |cffffffff13|cffced4da сек. (на героях — |cffffffff0,5|cffced4da сек.). Спящая цель не может действовать, но просыпается при получении урона.|r"
            },
            "values": {
                "name": "|cffe4cfa3Сон|r",
                "tip1": "|cffe4cfa3Сон|r (|cffffffffE|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Погружает выбранного противника в сон на |cffffffff13|cffced4da сек. (на героях — |cffffffff0,5|cffced4da сек.). Спящая цель не может действовать, но просыпается при получении урона.|r"
            }
        },
        # Red Flight
        {
            "id": "drAd",
            "name": "|cffe4cfa3Поджог|r",
            "wts": {"name": 39878, "tip1": 39879, "ubertip1": 39880},
            "values": {
                "name": "|cffe4cfa3Поджог|r",
                "tip1": "|cffe4cfa3Поджог|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки поджигают цель, нанося |cffffffff5|cffced4da ед. урона в секунду в течение |cffffffff12|cffced4da сек. (на героях — |cffffffff0,5|cffced4da сек.).|r"
            }
        },
        {
            "id": "drA0",
            "name": "|cffe4cfa3Исцеляющий огонь|r",
            "hotkey": "Q",
            "wts": {"name": 24658, "tip1": 25406, "ubertip1": 25407},
            "values": {
                "name": "|cffe4cfa3Исцеляющий огонь|r",
                "tip1": "|cffe4cfa3Исцеляющий огонь|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает струю живительного пламени в указанную область радиусом |cffffffff275|cffced4da, восстанавливая союзникам |cffffffff55|cffced4da ед. здоровья.|r"
            }
        },
        {
            "id": "drA3",
            "name": "|cffe4cfa3Благословение жизни|r",
            "hotkey": "W",
            "wts": {"name": 39708, "tip1": 39709, "ubertip1": 40054},
            "values": {
                "name": "|cffe4cfa3Благословение жизни|r",
                "tip1": "|cffe4cfa3Благословение жизни|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзника на |cffffffff+10%|cffced4da и броню на |cffffffff+2|cffced4da на |cffffffff60|cffced4da сек.|r"
            }
        },
        {
            "id": "drA4",
            "name": "|cffe4cfa3Восстановление|r",
            "hotkey": "E",
            "wts": {"name": 39710, "tip1": 39711, "ubertip1": 22815},
            "values": {
                "name": "|cffe4cfa3Восстановление|r",
                "tip1": "|cffe4cfa3Восстановление|r (|cffffffffE|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает выбранному союзнику |cffffffff800|cffced4da ед. здоровья в течение |cffffffff30|cffced4da сек.|r"
            }
        },
        {
            "id": "A1BD",
            "name": "|cffe4cfa3Пламенное дыхание|r",
            "hotkey": "Q",
            "wts": {"name": 17161, "tip1": 24632, "ubertip1": 22813},
            "values": {
                "name": "|cffe4cfa3Пламенное дыхание|r",
                "tip1": "|cffe4cfa3Пламенное дыхание|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выдыхает поток огня перед собой на расстояние |cffffffff400|cffced4da, нанося по |cffffffff100|cffced4da ед. урона целям в секторе (суммарно до |cffffffff800|cffced4da ед. урона).|r"
            }
        },
        {
            "id": "drA5",
            "name": "|cffe4cfa3Прочная чешуя|r",
            "wts": {"name": 16383, "tip1": 16402, "ubertip1": 16410},
            "values": {
                "name": "|cffe4cfa3Прочная чешуя|r",
                "tip1": "|cffe4cfa3Прочная чешуя|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает входящий урон от атак по дракону на |cffffffff12|cffced4da ед. Получаемый урон не может опуститься ниже |cffffffff5|cffced4da ед.|r"
            }
        },
        # Blue Flight
        {
            "id": "A0QB",
            "name": "|cffe4cfa3Рассеивание заклинаний|r",
            "hotkey": "Q",
            "wts": {"name": 22393, "tip1": 22394},
            "raw_patches": {
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает все магические эффекты с существ в области радиусом |cffffffff200|cffced4da и наносит |cffffffff200|cffced4da ед. урона призванным существам.|r"
            },
            "values": {
                "name": "|cffe4cfa3Рассеивание заклинаний|r",
                "tip1": "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает все магические эффекты с существ в области радиусом |cffffffff200|cffced4da и наносит |cffffffff200|cffced4da ед. урона призванным существам.|r"
            }
        },
        {
            "id": "dra3",
            "name": "|cffe4cfa3Телепортация|r",
            "hotkey": "D",
            "wts": {"name": 40316, "tip1": 40317, "ubertip1": 40318},
            "values": {
                "name": "|cffe4cfa3Телепортация|r",
                "tip1": "|cffe4cfa3Телепортация|r (|cffffffffD|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переносит дракона и до |cffffffff5|cffced4da находящихся рядом союзных воинов к выбранному союзному наземному юниту или зданию.|r"
            }
        },
        {
            "id": "drA6",
            "name": "|cffe4cfa3Буран|r",
            "hotkey": "E",
            "wts": {"name": 16418, "tip1": 16422, "ubertip1": 32868},
            "values": {
                "name": "|cffe4cfa3Буран|r",
                "tip1": "|cffe4cfa3Буран|r (|cffffffffE|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область ледяной шквал из |cffffffff8|cffced4da волн, каждая из которых наносит по |cffffffff25|cffced4da ед. урона целям в радиусе |cffffffff150|cffced4da.|r"
            }
        },
        {
            "id": "drA1",
            "name": "|cffe4cfa3Кольцо льда|r",
            "hotkey": "W",
            "wts": {"name": 17036, "tip1": 17037, "ubertip1": 23596},
            "values": {
                "name": "|cffe4cfa3Кольцо льда|r",
                "tip1": "|cffe4cfa3Кольцо льда|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взрыв льда наносит цели |cffffffff100|cffced4da ед. урона и |cffffffff85|cffced4da ед. урона целям вокруг в радиусе |cffffffff150|cffced4da, замедляя их атаку и передвижение на |cffffffff12|cffced4da сек. (на героях — |cffffffff1|cffced4da сек.).|r"
            }
        },
        {
            "id": "drAq",
            "name": "|cffe4cfa3Ледяная стрела|r",
            "hotkey": "Q",
            "wts": {"name": 17102, "tip1": 17107, "ubertip1": 23597},
            "values": {
                "name": "|cffe4cfa3Ледяная стрела|r",
                "tip1": "|cffe4cfa3Ледяная стрела|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает в противника ледяную стрелу, наносящую |cffffffff140|cffced4da ед. урона и оглушающую цель на |cffffffff7|cffced4da сек. (на героях — |cffffffff0,5|cffced4da сек.).|r"
            }
        },
        {
            "id": "drA7",
            "name": "|cffe4cfa3Пожирание магии|r",
            "hotkey": "Q",
            "wts": {"name": 22387, "tip1": 22389},
            "raw_patches": {
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает все заклинания в радиусе |cffffffff200|cffced4da, восстанавливая дракону |cffffffff50|cffced4da ед. здоровья и |cffffffff75|cffced4da ед. маны за каждый развеянный эффект, а также нанося |cffffffff160|cffced4da ед. урона призванным существам.|r"
            },
            "values": {
                "name": "|cffe4cfa3Пожирание магии|r",
                "tip1": "|cffe4cfa3Пожирание магии|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает все заклинания в радиусе |cffffffff200|cffced4da, восстанавливая дракону |cffffffff50|cffced4da ед. здоровья и |cffffffff75|cffced4da ед. маны за каждый развеянный эффект, а также нанося |cffffffff160|cffced4da ед. урона призванным существам.|r"
            }
        },
        {
            "id": "A0RM",
            "name": "|cffe4cfa3Похищение заклинаний|r",
            "hotkey": "W",
            "wts": {"name": 17118, "tip1": 17119},
            "raw_patches": {
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переносит полезный магический эффект с противника на случайного союзника либо вредный эффект с союзника на врага в радиусе |cffffffff700|cffced4da.|r"
            },
            "values": {
                "name": "|cffe4cfa3Похищение заклинаний|r",
                "tip1": "|cffe4cfa3Похищение заклинаний|r (|cffffffffW|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переносит полезный магический эффект с противника на случайного союзника либо вредный эффект с союзника на врага в радиусе |cffffffff700|cffced4da.|r"
            }
        },
        {
            "id": "drA8",
            "name": "|cffe4cfa3Восполнение маны|r",
            "hotkey": "R",
            "wts": {"name": 16989, "tip1": 16996, "ubertip1": 22816},
            "values": {
                "name": "|cffe4cfa3Восполнение маны|r",
                "tip1": "|cffe4cfa3Восполнение маны|r (|cffffffffR|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает находящимся поблизости союзникам |cffffffff65|cffced4da ед. маны в радиусе |cffffffff500|cffced4da.|r"
            }
        },
        {
            "id": "drA9",
            "name": "|cffe4cfa3Вспышка маны|r",
            "hotkey": "E",
            "wts": {
                "name": 17033,
                "tip1": 17034,
                "ubertip1": 23587,
                "untip1": 17035,
                "unubertip1": 23586
            },
            "values": {
                "name": "|cffe4cfa3Вспышка маны|r",
                "tip1": "|cffe4cfa3Вспышка маны|r (|cffffffffE|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню дракона на |cffffffff+12|cffced4da и испускает магические импульсы, наносящие урон врагам в радиусе |cffffffff750|cffced4da при произнесении ими заклинаний.|nВремя действия: |cffffffff30|cffced4da сек.|r",
                "untip1": "|cffe4cfa3Отменить вспышку маны|r (|cffffffffE|r)",
                "unubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Преждевременно прекращает действие Вспышки маны.|r"
            }
        },
        # Black Flight
        {
            "id": "A1BF",
            "name": "|cffe4cfa3Пленяющая атака|r",
            "hotkey": "Q",
            "wts": {"name": 30549, "tip1": 30550},
            "raw_patches": {
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню цели на |cffffffff4|cffced4da ед. и раскрывает её местоположение на |cffffffff30|cffced4da сек. (на героях — |cffffffff15|cffced4da сек.).|r"
            },
            "values": {
                "name": "|cffe4cfa3Пленяющая атака|r",
                "tip1": "|cffe4cfa3Пленяющая атака|r (|cffffffffQ|r)",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню цели на |cffffffff4|cffced4da ед. и раскрывает её местоположение на |cffffffff30|cffced4da сек. (на героях — |cffffffff15|cffced4da сек.).|r"
            }
        },
        {
            "id": "A0RL",
            "name": "|cffe4cfa3Сильный удар|r",
            "wts": {"name": 17089, "tip1": 17090, "ubertip1": 17091},
            "values": {
                "name": "|cffe4cfa3Сильный удар|r",
                "tip1": "|cffe4cfa3Сильный удар|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff15%|cffced4da шанс при атаке нанести на |cffffffff25|cffced4da ед. больше урона и оглушить цель на |cffffffff2|cffced4da сек.|r"
            }
        },
        {
            "id": "A0QO",
            "name": "|cffe4cfa3Драконья ярость|r",
            "wts": {"name": 16381, "tip1": 16382, "ubertip1": 16428},
            "values": {
                "name": "|cffe4cfa3Драконья ярость|r",
                "tip1": "|cffe4cfa3Драконья ярость|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff10%|cffced4da шанс нанести критический удар с |cffffffff2-кратным|cffced4da уроном при атаке.|r"
            }
        },
        {
            "id": "A0RN",
            "name": "|cffe4cfa3Ярость земли|r",
            "wts": {"name": 15866, "tip1": 15963, "ubertip1": 17122},
            "values": {
                "name": "|cffe4cfa3Ярость земли|r",
                "tip1": "|cffe4cfa3Ярость земли|r",
                "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура увеличивает урон от атак находящихся рядом союзников на |cffffffff+10%|cffced4da в радиусе |cffffffff900|cffced4da.|r"
            }
        }
    ]

    # 6 Custom Buffs
    buffs = [
        {
            "id": "B05D",
            "name": "|cffe4cfa3Манипуляция времени|r",
            "wts": {"bufftip": 16858},
            "raw_patches": {
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Песчаная воронка наносит периодический урон.|r"
            },
            "values": {
                "bufftip": "|cffe4cfa3Манипуляция времени|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Песчаная воронка наносит периодический урон.|r"
            }
        },
        {
            "id": "B05C",
            "name": "|cffe4cfa3Ускорение времени|r",
            "wts": {"bufftip": 16993},
            "raw_patches": {
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки увеличена на |cffffffff+400%|cffced4da, скорость передвижения — на |cffffffff+20%|cffced4da, но получаемый урон повышен.|r"
            },
            "values": {
                "bufftip": "|cffe4cfa3Ускорение времени|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки увеличена на |cffffffff+400%|cffced4da, скорость передвижения — на |cffffffff+20%|cffced4da, но получаемый урон повышен.|r"
            }
        },
        {
            "id": "B03U",
            "name": "|cffe4cfa3Владыка магии|r",
            "wts": {"bufftip": 10157},
            "raw_patches": {
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость восстановления маны увеличена аурой Малигоса.|r"
            },
            "values": {
                "bufftip": "|cffe4cfa3Владыка магии|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость восстановления маны увеличена аурой Малигоса.|r"
            }
        },
        {
            "id": "Bdr0",
            "name": "|cffe4cfa3Сингулярная перегрузка|r",
            "wts": {"bufftip": 13754},
            "raw_patches": {
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки и передвижения увеличена.|r"
            },
            "values": {
                "bufftip": "|cffe4cfa3Сингулярная перегрузка|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки и передвижения увеличена.|r"
            }
        },
        {
            "id": "B02J",
            "name": "|cffe4cfa3Поджог|r",
            "wts": {"bufftip": 2237, "buffubertip": 7949},
            "values": {
                "bufftip": "|cffe4cfa3Поджог|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Цель охвачена пламенем и получает периодический урон огнём.|r"
            }
        },
        {
            "id": "B05S",
            "name": "|cffe4cfa3Ярость земли|r",
            "wts": {"bufftip": 18378},
            "raw_patches": {
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак союзников увеличен на |cffffffff+10%|cffced4da аурой древнего чёрного дракона.|r"
            },
            "values": {
                "bufftip": "|cffe4cfa3Ярость земли|r",
                "buffubertip": "|cffa6afb8ЭФФЕКТ:|cffced4da Урон от атак союзников увеличен на |cffffffff+10%|cffced4da аурой древнего чёрного дракона.|r"
            }
        }
    ]

    # Collect WTS updates and patch_blob operations
    updated_wts = original_wts
    wts_changed_ids = []
    w3a_ops = []
    w3h_ops = []

    for a in unit_abilities:
        wts_map = a.get("wts", {})
        vals = a.get("values", {})
        for field, wid in wts_map.items():
            val = vals[field]
            updated_wts = update_wts_string(updated_wts, wid, val)
            wts_changed_ids.append(wid)

        raw_map = a.get("raw_patches", {})
        for field, val in raw_map.items():
            w3a_ops.append({
                "type": "ability",
                "id": a["id"],
                "field": field,
                "value": val
            })

    for b in buffs:
        wts_map = b.get("wts", {})
        vals = b.get("values", {})
        for field, wid in wts_map.items():
            val = vals[field]
            updated_wts = update_wts_string(updated_wts, wid, val)
            wts_changed_ids.append(wid)

        raw_map = b.get("raw_patches", {})
        for field, val in raw_map.items():
            w3h_ops.append({
                "type": "buff",
                "id": b["id"],
                "field": field,
                "value": val
            })

    # Write updated WTS
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Patch w3a
    if w3a_ops:
        w3a_bytes = w3a_path.read_bytes()
        new_w3a, _ = patch_blob(w3a_bytes, w3a_ops, "ability", add_missing=True)
        w3a_path.write_bytes(new_w3a)
        new_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()

        w3a_skin_bytes = w3a_skin_path.read_bytes()
        new_w3a_skin, _ = patch_blob(w3a_skin_bytes, w3a_ops, "ability", add_missing=True)
        w3a_skin_path.write_bytes(new_w3a_skin)
        new_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()
    else:
        new_w3a_hash = original_w3a_hash
        new_w3a_skin_hash = original_w3a_skin_hash

    # Patch w3h
    if w3h_ops:
        w3h_bytes = w3h_path.read_bytes()
        new_w3h, _ = patch_blob(w3h_bytes, w3h_ops, "buff", add_missing=True)
        w3h_path.write_bytes(new_w3h)
        new_w3h_hash = hashlib.sha256(w3h_path.read_bytes()).hexdigest()

        w3h_skin_bytes = w3h_skin_path.read_bytes()
        new_w3h_skin, _ = patch_blob(w3h_skin_bytes, w3h_ops, "buff", add_missing=True)
        w3h_skin_path.write_bytes(new_w3h_skin)
        new_w3h_skin_hash = hashlib.sha256(w3h_skin_path.read_bytes()).hexdigest()
    else:
        new_w3h_hash = original_w3h_hash
        new_w3h_skin_hash = original_w3h_skin_hash

    # Readback checks in SD and HD
    checks = []
    abil_ids = [a["id"] for a in unit_abilities]
    buff_ids = [b["id"] for b in buffs]

    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        wts_dict = hw.load_wts_strings()
        resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

        # Verify abilities
        bulk_abils = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(abil_ids)] + hd_flag))
        abils_by_id = {obj["id"]: obj["fields"] for obj in bulk_abils.get("objects", [])}

        for a in unit_abilities:
            fields = abils_by_id.get(a["id"], {})
            verified_fields = []
            for f, expected_val in a["values"].items():
                actual_val = resolve(fields.get(f, ""))
                assert actual_val == expected_val, (
                    f"Mismatch for {a['id']}.{f} (hd={hd}):\nActual: '{actual_val}'\nExpected: '{expected_val}'"
                )
                verified_fields.append(f)

            checks.append({
                "id": a["id"],
                "type": "ability",
                "variant": "HD" if hd else "SD",
                "fields_verified": verified_fields
            })

        # Verify buffs
        bulk_buffs = require(cli(["get-objects-bulk", "--type", "buff", "--ids", ",".join(buff_ids)] + hd_flag))
        buffs_by_id = {obj["id"]: obj["fields"] for obj in bulk_buffs.get("objects", [])}

        for b in buffs:
            fields = buffs_by_id.get(b["id"], {})
            verified_fields = []
            for f, expected_val in b["values"].items():
                actual_val = resolve(fields.get(f, ""))
                assert actual_val == expected_val, (
                    f"Mismatch for {b['id']}.{f} (hd={hd}):\nActual: '{actual_val}'\nExpected: '{expected_val}'"
                )
                verified_fields.append(f)

            checks.append({
                "id": b["id"],
                "type": "buff",
                "variant": "HD" if hd else "SD",
                "fields_verified": verified_fields
            })

    # Save artifacts
    registry = {
        "race": "Dragon",
        "category": "unit_abilities_and_buffs",
        "total_abilities": len(unit_abilities),
        "total_buffs": len(buffs),
        "unit_abilities": unit_abilities,
        "buffs": buffs
    }
    (folder / "dragon_unit_abils.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Dragon",
        "category": "unit_abilities_and_buffs",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "w3a_hash_before": original_w3a_hash,
        "w3a_hash_after": new_w3a_hash,
        "w3a_skin_hash_before": original_w3a_skin_hash,
        "w3a_skin_hash_after": new_w3a_skin_hash,
        "w3h_hash_before": original_w3h_hash,
        "w3h_hash_after": new_w3h_hash,
        "w3h_skin_hash_before": original_w3h_skin_hash,
        "w3h_skin_hash_after": new_w3h_skin_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "dragon_unit_abils_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(unit_abilities)} Dragon unit abilities and {len(buffs)} buffs.")
    print(f"Updated {len(set(wts_changed_ids))} WTS keys, {len(w3a_ops)} w3a patches, {len(w3h_ops)} w3h patches.")
    print(f"Verified {len(checks)} SD/HD object checks.")

if __name__ == "__main__":
    main()
