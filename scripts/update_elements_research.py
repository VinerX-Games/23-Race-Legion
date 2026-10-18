# -*- coding: utf-8 -*-
"""Update Elements race researches (17 researches, 47 levels, 141 fields) with complete SD validation."""
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
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

RESEARCHES = [
    # ========================================================
    # Workshop: h0EV Элементальная мастерская
    # ========================================================
    {
        "id": "R09G",
        "name": "|cffe4cfa3Огонь|r",
        "hotkey": "Q",
        "maxlevel": 6,
        "levels": {
            1: {
                "name": "|cffe4cfa3Огонь|r",
                "tip": "|cffe4cfa3Огонь|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff1|cffced4da ед. и броню на |cffffffff1|cffced4da ед. всем созданиям стихии Огня: Элементалям Огня, Гончим пламени, Возжигателям, Загробникам Огня, Огненным птицам и Особым Огня.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Огонь|r",
                "tip": "|cffe4cfa3Огонь|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff2|cffced4da ед. и броню на |cffffffff2|cffced4da ед. всем созданиям стихии Огня: Элементалям Огня, Гончим пламени, Возжигателям, Загробникам Огня, Огненным птицам и Особым Огня.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
            },
            3: {
                "name": "|cffe4cfa3Огонь|r",
                "tip": "|cffe4cfa3Огонь|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff3|cffced4da ед. и броню на |cffffffff3|cffced4da ед. всем созданиям стихии Огня: Элементалям Огня, Гончим пламени, Возжигателям, Загробникам Огня, Огненным птицам и Особым Огня.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
            },
            4: {
                "name": "|cffe4cfa3Огонь|r",
                "tip": "|cffe4cfa3Огонь|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff4|cffced4da ед. и броню на |cffffffff4|cffced4da ед. всем созданиям стихии Огня: Элементалям Огня, Гончим пламени, Возжигателям, Загробникам Огня, Огненным птицам и Особым Огня.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
            },
            5: {
                "name": "|cffe4cfa3Огонь|r",
                "tip": "|cffe4cfa3Огонь|r [|cffffffff5-й уровень|r] (|cffffffffQ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff5|cffced4da ед. и броню на |cffffffff5|cffced4da ед. всем созданиям стихии Огня: Элементалям Огня, Гончим пламени, Возжигателям, Загробникам Огня, Огненным птицам и Особым Огня.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
            },
            6: {
                "name": "|cffe4cfa3Огонь|r",
                "tip": "|cffe4cfa3Огонь|r [|cffffffff6-й уровень|r] (|cffffffffQ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff6|cffced4da ед. и броню на |cffffffff6|cffced4da ед. всем созданиям стихии Огня: Элементалям Огня, Гончим пламени, Возжигателям, Загробникам Огня, Огненным птицам и Особым Огня.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
            }
        }
    },
    {
        "id": "R09H",
        "name": "|cffe4cfa3Вода|r",
        "hotkey": "S",
        "maxlevel": 6,
        "levels": {
            1: {
                "name": "|cffe4cfa3Вода|r",
                "tip": "|cffe4cfa3Вода|r [|cffffffff1-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff1|cffced4da ед. и броню на |cffffffff1|cffced4da ед. всем созданиям стихии Воды: Элементалям Воды, Элементалям Океана, Элементалям Морей, Загробникам Глубин, Рифовым Элементалям, Грязевым Элементалям и Особым Воды.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Вода|r",
                "tip": "|cffe4cfa3Вода|r [|cffffffff2-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff2|cffced4da ед. и броню на |cffffffff2|cffced4da ед. всем созданиям стихии Воды: Элементалям Воды, Элементалям Океана, Элементалям Морей, Загробникам Глубин, Рифовым Элементалям, Грязевым Элементалям и Особым Воды.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
            },
            3: {
                "name": "|cffe4cfa3Вода|r",
                "tip": "|cffe4cfa3Вода|r [|cffffffff3-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff3|cffced4da ед. и броню на |cffffffff3|cffced4da ед. всем созданиям стихии Воды: Элементалям Воды, Элементалям Океана, Элементалям Морей, Загробникам Глубин, Рифовым Элементалям, Грязевым Элементалям и Особым Воды.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
            },
            4: {
                "name": "|cffe4cfa3Вода|r",
                "tip": "|cffe4cfa3Вода|r [|cffffffff4-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff4|cffced4da ед. и броню на |cffffffff4|cffced4da ед. всем созданиям стихии Воды: Элементалям Воды, Элементалям Океана, Элементалям Морей, Загробникам Глубин, Рифовым Элементалям, Грязевым Элементалям и Особым Воды.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
            },
            5: {
                "name": "|cffe4cfa3Вода|r",
                "tip": "|cffe4cfa3Вода|r [|cffffffff5-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff5|cffced4da ед. и броню на |cffffffff5|cffced4da ед. всем созданиям стихии Воды: Элементалям Воды, Элементалям Океана, Элементалям Морей, Загробникам Глубин, Рифовым Элементалям, Грязевым Элементалям и Особым Воды.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
            },
            6: {
                "name": "|cffe4cfa3Вода|r",
                "tip": "|cffe4cfa3Вода|r [|cffffffff6-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff6|cffced4da ед. и броню на |cffffffff6|cffced4da ед. всем созданиям стихии Воды: Элементалям Воды, Элементалям Океана, Элементалям Морей, Загробникам Глубин, Рифовым Элементалям, Грязевым Элементалям и Особым Воды.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
            }
        }
    },
    {
        "id": "R09I",
        "name": "|cffe4cfa3Земля|r",
        "hotkey": "A",
        "maxlevel": 6,
        "levels": {
            1: {
                "name": "|cffe4cfa3Земля|r",
                "tip": "|cffe4cfa3Земля|r [|cffffffff1-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff1|cffced4da ед. и броню на |cffffffff1|cffced4da ед. всем созданиям стихии Земли и големам: Элементалям Земли, Песчаным Элементалям, големам и Особым Земли.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Земля|r",
                "tip": "|cffe4cfa3Земля|r [|cffffffff2-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff2|cffced4da ед. и броню на |cffffffff2|cffced4da ед. всем созданиям стихии Земли и големам: Элементалям Земли, Песчаным Элементалям, големам и Особым Земли.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
            },
            3: {
                "name": "|cffe4cfa3Земля|r",
                "tip": "|cffe4cfa3Земля|r [|cffffffff3-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff3|cffced4da ед. и броню на |cffffffff3|cffced4da ед. всем созданиям стихии Земли и големам: Элементалям Земли, Песчаным Элементалям, големам и Особым Земли.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
            },
            4: {
                "name": "|cffe4cfa3Земля|r",
                "tip": "|cffe4cfa3Земля|r [|cffffffff4-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff4|cffced4da ед. и броню на |cffffffff4|cffced4da ед. всем созданиям стихии Земли и големам: Элементалям Земли, Песчаным Элементалям, големам и Особым Земли.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
            },
            5: {
                "name": "|cffe4cfa3Земля|r",
                "tip": "|cffe4cfa3Земля|r [|cffffffff5-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff5|cffced4da ед. и броню на |cffffffff5|cffced4da ед. всем созданиям стихии Земли и големам: Элементалям Земли, Песчаным Элементалям, големам и Особым Земли.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
            },
            6: {
                "name": "|cffe4cfa3Земля|r",
                "tip": "|cffe4cfa3Земля|r [|cffffffff6-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff6|cffced4da ед. и броню на |cffffffff6|cffced4da ед. всем созданиям стихии Земли и големам: Элементалям Земли, Песчаным Элементалям, големам и Особым Земли.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
            }
        }
    },
    {
        "id": "R09J",
        "name": "|cffe4cfa3Ветер|r",
        "hotkey": "W",
        "maxlevel": 6,
        "levels": {
            1: {
                "name": "|cffe4cfa3Ветер|r",
                "tip": "|cffe4cfa3Ветер|r [|cffffffff1-й уровень|r] (|cffffffffW|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff1|cffced4da ед. и броню на |cffffffff1|cffced4da ед. всем созданиям стихии Ветра: Элементалям Ветра, Грозовым Элементалям, Воздушным волкам, Загробникам Бури, Штормовым Элементалям и Особым Ветра.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Ветер|r",
                "tip": "|cffe4cfa3Ветер|r [|cffffffff2-й уровень|r] (|cffffffffW|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff2|cffced4da ед. и броню на |cffffffff2|cffced4da ед. всем созданиям стихии Ветра: Элементалям Ветра, Грозовым Элементалям, Воздушным волкам, Загробникам Бури, Штормовым Элементалям и Особым Ветра.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
            },
            3: {
                "name": "|cffe4cfa3Ветер|r",
                "tip": "|cffe4cfa3Ветер|r [|cffffffff3-й уровень|r] (|cffffffffW|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff3|cffced4da ед. и броню на |cffffffff3|cffced4da ед. всем созданиям стихии Ветра: Элементалям Ветра, Грозовым Элементалям, Воздушным волкам, Загробникам Бури, Штормовым Элементалям и Особым Ветра.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
            },
            4: {
                "name": "|cffe4cfa3Ветер|r",
                "tip": "|cffe4cfa3Ветер|r [|cffffffff4-й уровень|r] (|cffffffffW|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff4|cffced4da ед. и броню на |cffffffff4|cffced4da ед. всем созданиям стихии Ветра: Элементалям Ветра, Грозовым Элементалям, Воздушным волкам, Загробникам Бури, Штормовым Элементалям и Особым Ветра.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
            },
            5: {
                "name": "|cffe4cfa3Ветер|r",
                "tip": "|cffe4cfa3Ветер|r [|cffffffff5-й уровень|r] (|cffffffffW|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff5|cffced4da ед. и броню на |cffffffff5|cffced4da ед. всем созданиям стихии Ветра: Элементалям Ветра, Грозовым Элементалям, Воздушным волкам, Загробникам Бури, Штормовым Элементалям и Особым Ветра.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
            },
            6: {
                "name": "|cffe4cfa3Ветер|r",
                "tip": "|cffe4cfa3Ветер|r [|cffffffff6-й уровень|r] (|cffffffffW|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает атаку на |cffffffff6|cffced4da ед. и броню на |cffffffff6|cffced4da ед. всем созданиям стихии Ветра: Элементалям Ветра, Грозовым Элементалям, Воздушным волкам, Загробникам Бури, Штормовым Элементалям и Особым Ветра.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
            }
        }
    },
    {
        "id": "R0DS",
        "name": "|cffe4cfa3Улучшенная добыча|r",
        "hotkey": "Z",
        "maxlevel": 5,
        "levels": {
            1: {
                "name": "|cffe4cfa3Улучшенная добыча|r",
                "tip": "|cffe4cfa3Улучшенная добыча|r [|cffffffff1-й уровень|r] (|cffffffffZ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой Духами стихий древесины на |cffffffff10|cffced4da ед.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/5|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Улучшенная добыча|r",
                "tip": "|cffe4cfa3Улучшенная добыча|r [|cffffffff2-й уровень|r] (|cffffffffZ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой Духами стихий древесины ещё на |cffffffff10|cffced4da ед. (всего |cffffffff+20|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/5|cffced4da.|r"
            },
            3: {
                "name": "|cffe4cfa3Улучшенная добыча|r",
                "tip": "|cffe4cfa3Улучшенная добыча|r [|cffffffff3-й уровень|r] (|cffffffffZ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой Духами стихий древесины ещё на |cffffffff10|cffced4da ед. (всего |cffffffff+30|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/5|cffced4da.|r"
            },
            4: {
                "name": "|cffe4cfa3Улучшенная добыча|r",
                "tip": "|cffe4cfa3Улучшенная добыча|r [|cffffffff4-й уровень|r] (|cffffffffZ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой Духами стихий древесины ещё на |cffffffff10|cffced4da ед. (всего |cffffffff+40|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/5|cffced4da.|r"
            },
            5: {
                "name": "|cffe4cfa3Улучшенная добыча|r",
                "tip": "|cffe4cfa3Улучшенная добыча|r [|cffffffff5-й уровень|r] (|cffffffffZ|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой Духами стихий древесины ещё на |cffffffff10|cffced4da ед. (всего |cffffffff+50|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/5|cffced4da.|r"
            }
        }
    },

    # ========================================================
    # Fire Sanctum: h0EO Огненные недра
    # ========================================================
    {
        "id": "R09Q",
        "name": "|cffe4cfa3Ярость|r",
        "hotkey": "A",
        "maxlevel": 1,
        "levels": {
            1: {
                "name": "|cffe4cfa3Ярость|r",
                "tip": "|cffe4cfa3Ярость|r (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Воспламеняет ярость всех созданий стихии Огня, повышая их урон на |cffffffff5|cffced4da ед., но снижая максимальный запас здоровья на |cffffffff50|cffced4da ед.|r"
            }
        }
    },
    {
        "id": "R09R",
        "name": "|cffe4cfa3Повышение температуры|r",
        "hotkey": "S",
        "maxlevel": 2,
        "levels": {
            1: {
                "name": "|cffe4cfa3Повышение температуры|r",
                "tip": "|cffe4cfa3Повышение температуры|r [|cffffffff1-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья Возжигателей на |cffffffff25|cffced4da ед. и их запас маны на |cffffffff20|cffced4da ед.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Повышение температуры|r",
                "tip": "|cffe4cfa3Повышение температуры|r [|cffffffff2-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья Возжигателей ещё на |cffffffff25|cffced4da ед. (всего |cffffffff+50|cffced4da ед.) и их запас маны ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+40|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
            }
        }
    },
    {
        "id": "R09S",
        "name": "|cffe4cfa3Рассекающий удар|r",
        "hotkey": "D",
        "maxlevel": 1,
        "levels": {
            1: {
                "name": "|cffe4cfa3Рассекающий удар|r",
                "tip": "|cffe4cfa3Рассекающий удар|r (|cffffffffD|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Гончих пламени способностью «Рассекающий удар», позволяя наносить |cffffffff13%|cffced4da урона другим наземным противникам в радиусе |cffffffff150|cffced4da от цели атаки.|r"
            }
        }
    },

    # ========================================================
    # Water Sanctum: h0ET Морской бассейн
    # ========================================================
    {
        "id": "R09T",
        "name": "|cffe4cfa3Магия воды|r",
        "hotkey": "A",
        "maxlevel": 1,
        "levels": {
            1: {
                "name": "|cffe4cfa3Магия воды|r",
                "tip": "|cffe4cfa3Магия воды|r (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наполняет Элементалей воды первозданной влагой, увеличивая их запас маны на |cffffffff50|cffced4da ед.|r"
            }
        }
    },
    {
        "id": "R09U",
        "name": "|cffe4cfa3Ледяные стрелы|r",
        "hotkey": "S",
        "maxlevel": 2,
        "levels": {
            1: {
                "name": "|cffe4cfa3Ледяные стрелы|r",
                "tip": "|cffe4cfa3Ледяные стрелы|r [|cffffffff1-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Элементалей морей способностью «Ледяные стрелы» и увеличивает их запас маны на |cffffffff30|cffced4da ед.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Ледяные стрелы|r",
                "tip": "|cffe4cfa3Ледяные стрелы|r [|cffffffff2-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает эффект способности «Ледяные стрелы» и увеличивает запас маны Элементалей морей ещё на |cffffffff30|cffced4da ед. (всего |cffffffff+60|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
            }
        }
    },
    {
        "id": "R09V",
        "name": "|cffe4cfa3Магия морей|r",
        "hotkey": "D",
        "maxlevel": 2,
        "levels": {
            1: {
                "name": "|cffe4cfa3Магия морей|r",
                "tip": "|cffe4cfa3Магия морей|r [|cffffffff1-й уровень|r] (|cffffffffD|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает Рифовым элементалям заклинание «Кольцо льда» и увеличивает их запас маны на |cffffffff30|cffced4da ед.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Магия морей|r",
                "tip": "|cffe4cfa3Магия морей|r [|cffffffff2-й уровень|r] (|cffffffffD|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает морскую магию Рифовых элементалей и увеличивает их запас маны ещё на |cffffffff30|cffced4da ед. (всего |cffffffff+60|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
            }
        }
    },
    {
        "id": "Resi",
        "name": "|cffe4cfa3Рассеивание чар|r",
        "hotkey": "A",
        "maxlevel": 1,
        "levels": {
            1: {
                "name": "|cffe4cfa3Рассеивание чар|r",
                "tip": "|cffe4cfa3Рассеивание чар|r (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Элементалей воды и Элементалей океана способностью «Рассеивание чар», позволяющей снимать положительные эффекты с врагов и отрицательные с союзников, а также наносить урон призванным существам.|r"
            }
        }
    },

    # ========================================================
    # Wind Sanctum: h0EU Ветролом
    # ========================================================
    {
        "id": "R09Z",
        "name": "|cffe4cfa3Лёгкость воздуха|r",
        "hotkey": "A",
        "maxlevel": 2,
        "levels": {
            1: {
                "name": "|cffe4cfa3Лёгкость воздуха|r",
                "tip": "|cffe4cfa3Лёгкость воздуха|r [|cffffffff1-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость передвижения всех созданий стихии Ветра на |cffffffff30|cffced4da ед.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Лёгкость воздуха|r",
                "tip": "|cffe4cfa3Лёгкость воздуха|r [|cffffffff2-й уровень|r] (|cffffffffA|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость передвижения всех созданий стихии Ветра ещё на |cffffffff30|cffced4da ед. (всего |cffffffff+60|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
            }
        }
    },
    {
        "id": "R0A0",
        "name": "|cffe4cfa3Критический удар|r",
        "hotkey": "S",
        "maxlevel": 1,
        "levels": {
            1: {
                "name": "|cffe4cfa3Критический удар|r",
                "tip": "|cffe4cfa3Критический удар|r (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Грозовых элементалей способностью «Критический удар», даруя |cffffffff10%|cffced4da шанс нанести двойной урон при атаке.|r"
            }
        }
    },
    {
        "id": "R0A1",
        "name": "|cffe4cfa3Ярость грома|r",
        "hotkey": "D",
        "maxlevel": 1,
        "levels": {
            1: {
                "name": "|cffe4cfa3Ярость грома|r",
                "tip": "|cffe4cfa3Ярость грома|r (|cffffffffD|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Штормовых элементалей способностью «Ярость грома», позволяя их молниям атаковать сразу несколько целей одновременно.|r"
            }
        }
    },

    # ========================================================
    # Earth Sanctum: h0EW Каменоломня
    # ========================================================
    {
        "id": "R09X",
        "name": "|cffe4cfa3Каменное здоровье|r",
        "hotkey": "S",
        "maxlevel": 3,
        "levels": {
            1: {
                "name": "|cffe4cfa3Каменное здоровье|r",
                "tip": "|cffe4cfa3Каменное здоровье|r [|cffffffff1-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья созданий стихии Земли и големов на |cffffffff30|cffced4da ед.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
            },
            2: {
                "name": "|cffe4cfa3Каменное здоровье|r",
                "tip": "|cffe4cfa3Каменное здоровье|r [|cffffffff2-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья созданий стихии Земли и големов ещё на |cffffffff30|cffced4da ед. (всего |cffffffff+60|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
            },
            3: {
                "name": "|cffe4cfa3Каменное здоровье|r",
                "tip": "|cffe4cfa3Каменное здоровье|r [|cffffffff3-й уровень|r] (|cffffffffS|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья созданий стихии Земли и големов ещё на |cffffffff30|cffced4da ед. (всего |cffffffff+90|cffced4da ед.).|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
            }
        }
    },
    {
        "id": "R09Y",
        "name": "|cffe4cfa3Сокрушение|r",
        "hotkey": "D",
        "maxlevel": 1,
        "levels": {
            1: {
                "name": "|cffe4cfa3Сокрушение|r",
                "tip": "|cffe4cfa3Сокрушение|r (|cffffffffD|r)",
                "ubertip": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Яростных големов способностью «Сокрушение», давая |cffffffff25%|cffced4da шанс нанести |cffffffff15|cffced4da ед. урона всем противникам поблизости от цели атаки.|r"
            }
        }
    }
]

def main():
    folder = ROOT / "docs/ui_text"
    raw_map = json.load(open(folder / "elements_research_wts_map.json", encoding="utf-8"))

    source = ROOT / "map.w3x"
    wts_path = source / "war3map.wts"
    w3q_skin_path = source / "war3mapSkin.w3q"

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    wts_changed = []
    upgrade_ops = []

    updated_wts = original_wts

    for item in RESEARCHES:
        rid = item["id"]
        meta_levels = raw_map.get(rid, {}).get("levels", {})
        for lvl, values in item["levels"].items():
            lvl_meta = meta_levels.get(str(lvl), {})
            for field in ("name", "tip", "ubertip"):
                val = values[field]
                f_meta = lvl_meta.get(field, {})
                wid = f_meta.get("wts_id")
                if wid:
                    updated_wts = update_wts_string(updated_wts, wid, val)
                    wts_changed.append((rid, lvl, field, wid, val))
                else:
                    upgrade_ops.append({
                        "type": "upgrade",
                        "id": rid,
                        "field": f"{field}{lvl}",
                        "value": val
                    })

    print(f"Total WTS keys to update: {len(wts_changed)}")
    print(f"Total upgrade ops to patch: {len(upgrade_ops)}")
    for op in upgrade_ops:
        print(f"  Op: [{op['id']}] {op['field']} -> {repr(op['value'][:50])}")

    # Write WTS
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Patch binary skin if needed
    if upgrade_ops:
        skin_bytes = w3q_skin_path.read_bytes()
        new_skin_bytes, _ = patch_blob(skin_bytes, upgrade_ops, "upgrade", add_missing=True)
        w3q_skin_path.write_bytes(new_skin_bytes)

    # Readback checks in SD mode
    all_rids = [r["id"] for r in RESEARCHES]
    bulk = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(all_rids)]))

    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    lookup = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

    checks = []
    mismatches = []

    for item in RESEARCHES:
        rid = item["id"]
        fields = lookup.get(rid, {})
        for lvl, values in item["levels"].items():
            for f in ("name", "tip", "ubertip"):
                key = f"{f}{lvl}"
                expected = values[f]
                actual = resolve(fields.get(key, ""))
                matched = (actual == expected)
                checks.append({
                    "id": rid,
                    "level": lvl,
                    "field": key,
                    "expected": expected,
                    "actual": actual,
                    "matched": matched
                })
                if not matched:
                    mismatches.append((rid, key, expected, actual))

    print(f"\nSD readback validation: {len(checks) - len(mismatches)}/{len(checks)} fields matched.")
    if mismatches:
        print(f"FAILED: {len(mismatches)} mismatches:")
        for obj_id, k, exp, act in mismatches:
            print(f"  [{obj_id}] {k}:\n    Expected: {repr(exp)}\n    Actual:   {repr(act)}")
        sys.exit(1)

    report = {
        "race": "elements",
        "category": "researches",
        "total_researches": len(RESEARCHES),
        "total_levels": sum(r["maxlevel"] for r in RESEARCHES),
        "total_checks": len(checks),
        "all_matched": len(mismatches) == 0,
        "wts_keys_updated": len(wts_changed),
        "upgrade_ops": len(upgrade_ops),
        "hashes": {
            "wts": {"before": original_wts_hash, "after": new_wts_hash}
        }
    }
    (folder / "elements_research_apply.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / "elements_research.json").write_text(json.dumps(RESEARCHES, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Report saved to docs/ui_text/elements_research_apply.json")
    print("Registry saved to docs/ui_text/elements_research.json")
    print("All 17 researches (47 levels) successfully validated in SD mode!")

if __name__ == "__main__":
    main()
