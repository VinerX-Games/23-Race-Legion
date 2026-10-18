# -*- coding: utf-8 -*-
"""Update Ents (Argvinol) race researches (14 researches, 42 levels, 126 text fields) with complete SD/HD validation."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    w3q_path = ROOT / "map.w3x/war3map.w3q"
    w3q_skin_path = ROOT / "map.w3x/war3mapSkin.w3q"

    original_hashes = {
        "wts": hashlib.sha256(wts_path.read_bytes()).hexdigest(),
        "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest(),
        "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
        "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
        "w3q": hashlib.sha256(w3q_path.read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest(),
    }

    ent_research_data = [
        # 1. R0AG — Сила природы (6 уровней, горячая клавиша W)
        {
            "id": "R0AG",
            "name": "Сила природы",
            "maxlevel": 6,
            "hotkey": "W",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41701, "tip": 41702, "ubertip": 20301},
                    "values": {
                        "name1": "|cffe4cfa3Сила природы|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Сила природы|r — уровень |cffffffff1|r (|cffffffffW|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак лесных воинов на |cffffffff2|cffced4da ед.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41703, "tip": 41704, "ubertip": 20302},
                    "values": {
                        "name2": "|cffe4cfa3Сила природы|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Сила природы|r — уровень |cffffffff2|r (|cffffffffW|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак лесных воинов ещё на |cffffffff2|cffced4da ед. (всего |cffffffff+4|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
                    }
                },
                {
                    "level": 3,
                    "wts": {"name": 41705, "tip": 41706, "ubertip": 20303},
                    "values": {
                        "name3": "|cffe4cfa3Мощь природы|r — уровень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Мощь природы|r — уровень |cffffffff3|r (|cffffffffW|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак лесных воинов ещё на |cffffffff2|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
                    }
                },
                {
                    "level": 4,
                    "wts": {"name": 41709, "tip": 41712, "ubertip": 20310},
                    "values": {
                        "name4": "|cffe4cfa3Мощь природы|r — уровень |cffffffff4|r",
                        "tip4": "|cffe4cfa3Мощь природы|r — уровень |cffffffff4|r (|cffffffffW|r)",
                        "ubertip4": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак лесных воинов ещё на |cffffffff2|cffced4da ед. (всего |cffffffff+8|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
                    }
                },
                {
                    "level": 5,
                    "wts": {"name": 41708, "tip": 41711, "ubertip": 20311},
                    "values": {
                        "name5": "|cffe4cfa3Могущество природы|r — уровень |cffffffff5|r",
                        "tip5": "|cffe4cfa3Могущество природы|r — уровень |cffffffff5|r (|cffffffffW|r)",
                        "ubertip5": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак лесных воинов ещё на |cffffffff2|cffced4da ед. (всего |cffffffff+10|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
                    }
                },
                {
                    "level": 6,
                    "wts": {"name": 41707, "tip": 41710, "ubertip": 20312},
                    "values": {
                        "name6": "|cffe4cfa3Могущество природы|r — уровень |cffffffff6|r",
                        "tip6": "|cffe4cfa3Могущество природы|r — уровень |cffffffff6|r (|cffffffffW|r)",
                        "ubertip6": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак лесных воинов ещё на |cffffffff2|cffced4da ед. (всего |cffffffff+12|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
                    }
                }
            ]
        },

        # 2. R0AE — Прочная кора (6 уровней, горячая клавиша E)
        {
            "id": "R0AE",
            "name": "Прочная кора",
            "maxlevel": 6,
            "hotkey": "E",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41683, "tip": 41686, "ubertip": 41689},
                    "values": {
                        "name1": "|cffe4cfa3Прочная кора|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Прочная кора|r — уровень |cffffffff1|r (|cffffffffE|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню лесных воинов на |cffffffff1|cffced4da ед.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41684, "tip": 41687, "ubertip": 41690},
                    "values": {
                        "name2": "|cffe4cfa3Прочная кора|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Прочная кора|r — уровень |cffffffff2|r (|cffffffffE|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню лесных воинов ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+2|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
                    }
                },
                {
                    "level": 3,
                    "wts": {"name": 41685, "tip": 41688, "ubertip": 41691},
                    "values": {
                        "name3": "|cffe4cfa3Усиленная кора|r — уровень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Усиленная кора|r — уровень |cffffffff3|r (|cffffffffE|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню лесных воинов ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+3|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
                    }
                },
                {
                    "level": 4,
                    "wts": {"name": 41694, "tip": 41697, "ubertip": 41698},
                    "values": {
                        "name4": "|cffe4cfa3Усиленная кора|r — уровень |cffffffff4|r",
                        "tip4": "|cffe4cfa3Усиленная кора|r — уровень |cffffffff4|r (|cffffffffE|r)",
                        "ubertip4": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню лесных воинов ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+4|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
                    }
                },
                {
                    "level": 5,
                    "wts": {"name": 41693, "tip": 41696, "ubertip": 41699},
                    "values": {
                        "name5": "|cffe4cfa3Непробиваемая кора|r — уровень |cffffffff5|r",
                        "tip5": "|cffe4cfa3Непробиваемая кора|r — уровень |cffffffff5|r (|cffffffffE|r)",
                        "ubertip5": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню лесных воинов ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+5|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
                    }
                },
                {
                    "level": 6,
                    "wts": {"name": 41692, "tip": 41695, "ubertip": 41700},
                    "values": {
                        "name6": "|cffe4cfa3Непробиваемая кора|r — уровень |cffffffff6|r",
                        "tip6": "|cffe4cfa3Непробиваемая кора|r — уровень |cffffffff6|r (|cffffffffE|r)",
                        "ubertip6": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню лесных воинов ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
                    }
                }
            ]
        },

        # 3. R09M — Благословение природы (6 уровней, горячая клавиша R)
        {
            "id": "R09M",
            "name": "Благословение природы",
            "maxlevel": 6,
            "hotkey": "R",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41671, "tip": 41677, "ubertip": 12993},
                    "values": {
                        "name1": "|cffe4cfa3Благословение природы|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Благословение природы|r — уровень |cffffffff1|r (|cffffffffR|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья лесных воинов на |cffffffff20|cffced4da ед. и открывает доступ к новым войскам.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41672, "tip": 41678, "ubertip": 13011},
                    "values": {
                        "name2": "|cffe4cfa3Благословение природы|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Благословение природы|r — уровень |cffffffff2|r (|cffffffffR|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья лесных воинов ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+40|cffced4da ед.) и открывает доступ к новым войскам.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
                    }
                },
                {
                    "level": 3,
                    "wts": {"name": 41673, "tip": 41679, "ubertip": 13022},
                    "values": {
                        "name3": "|cffe4cfa3Благословение природы|r — уровень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Благословение природы|r — уровень |cffffffff3|r (|cffffffffR|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья лесных воинов ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+60|cffced4da ед.) и открывает доступ к новым войскам.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
                    }
                },
                {
                    "level": 4,
                    "wts": {"name": 41674, "tip": 41680, "ubertip": 13073},
                    "values": {
                        "name4": "|cffe4cfa3Благословение природы|r — уровень |cffffffff4|r",
                        "tip4": "|cffe4cfa3Благословение природы|r — уровень |cffffffff4|r (|cffffffffR|r)",
                        "ubertip4": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья лесных воинов ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+80|cffced4da ед.) и открывает доступ к новым войскам.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
                    }
                },
                {
                    "level": 5,
                    "wts": {"name": 41675, "tip": 41681, "ubertip": 20054},
                    "values": {
                        "name5": "|cffe4cfa3Благословение природы|r — уровень |cffffffff5|r",
                        "tip5": "|cffe4cfa3Благословение природы|r — уровень |cffffffff5|r (|cffffffffR|r)",
                        "ubertip5": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья лесных воинов ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+100|cffced4da ед.) и открывает доступ к новым войскам.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
                    }
                },
                {
                    "level": 6,
                    "wts": {"name": 41676, "tip": 41682, "ubertip": 20145},
                    "values": {
                        "name6": "|cffe4cfa3Благословение природы|r — уровень |cffffffff6|r",
                        "tip6": "|cffe4cfa3Благословение природы|r — уровень |cffffffff6|r (|cffffffffR|r)",
                        "ubertip6": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья лесных воинов ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+120|cffced4da ед.) и открывает доступ к новым войскам.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deЭнт дробитель|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da|n- |cffa9c7deДрево Познания|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
                    }
                }
            ]
        },

        # 4. R09K — Ядовитый Сок (1 уровень, горячая клавиша Z)
        {
            "id": "R09K",
            "name": "Ядовитый Сок",
            "maxlevel": 1,
            "hotkey": "Z",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41719, "tip": 41720, "ubertip": 41721},
                    "values": {
                        "name1": "|cffe4cfa3Ядовитый Сок|r",
                        "tip1": "|cffe4cfa3Ядовитый Сок|r (|cffffffffZ|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Ядовитый сок»: атаки отравляют противника, снижая скорость передвижения на |cffffffff15%|cffced4da, скорость атаки на |cffffffff10%|cffced4da и нанося |cffffffff4|cffced4da ед. урона в секунду в течение |cffffffff5|cffced4da сек. (по героям — |cffffffff1|cffced4da сек.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДревень|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deГончая Маны|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da|n- |cffa9c7deДриада|cffced4da|n- |cffa9c7deМалый Древень|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|r"
                    }
                }
            ]
        },

        # 5. R09N — Усиление Ядра Маны (2 уровня, горячая клавиша D)
        {
            "id": "R09N",
            "name": "Усиление Ядра Маны",
            "maxlevel": 2,
            "hotkey": "D",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41724, "tip": 41725, "ubertip": 41726},
                    "values": {
                        "name1": "|cffe4cfa3Усиление Ядра Маны|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Усиление Ядра Маны|r — уровень |cffffffff1|r (|cffffffffD|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Ядро Маны», увеличивает запас маны на |cffffffff20|cffced4da ед. и урон от атак на |cffffffff4|cffced4da ед.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГончая Маны|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41727, "tip": 41728, "ubertip": 41729},
                    "values": {
                        "name2": "|cffe4cfa3Усиление Ядра Маны|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Усиление Ядра Маны|r — уровень |cffffffff2|r (|cffffffffD|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Аура магического ядра», дополнительно увеличивает запас маны ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+40|cffced4da ед.) и урон от атак на |cffffffff4|cffced4da ед. (всего |cffffffff+8|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГончая Маны|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
                    }
                }
            ]
        },

        # 6. R0AF — Усиление Ядра Жизни (2 уровня, горячая клавиша S)
        {
            "id": "R0AF",
            "name": "Усиление Ядра Жизни",
            "maxlevel": 2,
            "hotkey": "S",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41732, "tip": 41733, "ubertip": 41734},
                    "values": {
                        "name1": "|cffe4cfa3Усиление Ядра Жизни|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Усиление Ядра Жизни|r — уровень |cffffffff1|r (|cffffffffS|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Ядро Жизни», увеличивает запас маны на |cffffffff20|cffced4da ед. и урон от атак на |cffffffff4|cffced4da ед.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41735, "tip": 41736, "ubertip": 41737},
                    "values": {
                        "name2": "|cffe4cfa3Усиление Ядра Жизни|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Усиление Ядра Жизни|r — уровень |cffffffff2|r (|cffffffffS|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Аура ядра жизни», дополнительно увеличивает запас маны ещё на |cffffffff20|cffced4da ед. (всего |cffffffff+40|cffced4da ед.) и урон от атак на |cffffffff4|cffced4da ед. (всего |cffffffff+8|cffced4da ед.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГончая Жизни|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
                    }
                }
            ]
        },

        # 7. R0AH — Мастерство Войны (2 уровня, горячая клавиша X)
        {
            "id": "R0AH",
            "name": "Мастерство Войны",
            "maxlevel": 2,
            "hotkey": "X",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41740, "tip": 41741, "ubertip": 41742},
                    "values": {
                        "name1": "|cffe4cfa3Мастерство Войны|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Мастерство Войны|r — уровень |cffffffff1|r (|cffffffffX|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Рассекающий удар», увеличивает запас здоровья на |cffffffff40|cffced4da ед., урон от атак на |cffffffff6|cffced4da ед. и скорость атаки на |cffffffff20%|cffced4da.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41744, "tip": 41745, "ubertip": 41746},
                    "values": {
                        "name2": "|cffe4cfa3Мастерство Войны|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Мастерство Войны|r — уровень |cffffffff2|r (|cffffffffX|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас здоровья ещё на |cffffffff40|cffced4da ед. (всего |cffffffff+80|cffced4da ед.), урон от атак на |cffffffff6|cffced4da ед. (всего |cffffffff+12|cffced4da ед.) и скорость атаки на |cffffffff10%|cffced4da (всего |cffffffff+30%|cffced4da).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМалое Древо Войны|cffced4da|n- |cffa9c7deДух Леса|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
                    }
                }
            ]
        },

        # 8. R0AL — Крепкий панцирь (1 уровень, горячая клавиша A)
        {
            "id": "R0AL",
            "name": "Крепкий панцирь",
            "maxlevel": 1,
            "hotkey": "A",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41713, "tip": 41714, "ubertip": 41715},
                    "values": {
                        "name1": "|cffe4cfa3Крепкий панцирь|r",
                        "tip1": "|cffe4cfa3Крепкий панцирь|r (|cffffffffA|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Крепкий панцирь» (поглощение до |cffffffff12|cffced4da ед. урона при каждой вражеской атаке) и увеличивает запас здоровья на |cffffffff100|cffced4da ед.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛесной Голем|cffced4da.|r"
                    }
                }
            ]
        },

        # 9. R0AK — Благословение Ветра (2 уровня, горячая клавиша Z)
        {
            "id": "R0AK",
            "name": "Благословение Ветра",
            "maxlevel": 2,
            "hotkey": "Z",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41749, "tip": 41750, "ubertip": 41751},
                    "values": {
                        "name1": "|cffe4cfa3Благословение Ветра|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Благословение Ветра|r — уровень |cffffffff1|r (|cffffffffZ|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Смерч», увеличивает дальность атаки на |cffffffff50|cffced4da ед. и скорость атаки на |cffffffff15%|cffced4da.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41753, "tip": 41754, "ubertip": 41755},
                    "values": {
                        "name2": "|cffe4cfa3Благословение Ветра|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Благословение Ветра|r — уровень |cffffffff2|r (|cffffffffZ|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Аура Ветров», дополнительно увеличивает дальность атаки ещё на |cffffffff50|cffced4da ед. (всего |cffffffff+100|cffced4da ед.) и скорость атаки на |cffffffff15%|cffced4da (всего |cffffffff+30%|cffced4da).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДрево Ветров|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
                    }
                }
            ]
        },

        # 10. R09O — Учения Леса (3 уровня, горячая клавиша D)
        {
            "id": "R09O",
            "name": "Учения Леса",
            "maxlevel": 3,
            "hotkey": "D",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41759, "tip": 41760, "ubertip": 41761},
                    "values": {
                        "name1": "|cffe4cfa3Учения Леса|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Учения Леса|r — уровень |cffffffff1|r (|cffffffffD|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас маны на |cffffffff40|cffced4da ед. и скорость восстановления маны на |cffffffff0,45|cffced4da ед./сек.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДрево Познания|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41764, "tip": 41765, "ubertip": 41766},
                    "values": {
                        "name2": "|cffe4cfa3Учения Леса|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Учения Леса|r — уровень |cffffffff2|r (|cffffffffD|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Покровительство Леса», дополнительно увеличивает запас маны ещё на |cffffffff40|cffced4da ед. (всего |cffffffff+80|cffced4da ед.) и скорость восстановления маны на |cffffffff0,45|cffced4da ед./сек. (всего |cffffffff+0,9|cffced4da ед./сек.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДрево Познания|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
                    }
                },
                {
                    "level": 3,
                    "wts": {"name": 41768, "tip": 41769, "ubertip": 41770},
                    "values": {
                        "name3": "|cffe4cfa3Учения Леса|r — уровень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Учения Леса|r — уровень |cffffffff3|r (|cffffffffD|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Мудрость Лесов», дополнительно увеличивает запас маны ещё на |cffffffff40|cffced4da ед. (всего |cffffffff+120|cffced4da ед.) и скорость восстановления маны на |cffffffff0,45|cffced4da ед./сек. (всего |cffffffff+1,35|cffced4da ед./сек.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДрево Познания|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
                    }
                }
            ]
        },

        # 11. R0AM — Магия Духа (3 уровня, горячая клавиша S)
        {
            "id": "R0AM",
            "name": "Магия Духа",
            "maxlevel": 3,
            "hotkey": "S",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41774, "tip": 41775, "ubertip": 41776},
                    "values": {
                        "name1": "|cffe4cfa3Магия Духа|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Магия Духа|r — уровень |cffffffff1|r (|cffffffffS|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Контроль Магии», увеличивает запас маны на |cffffffff40|cffced4da ед. и скорость восстановления маны на |cffffffff0,25|cffced4da ед./сек.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41779, "tip": 41780, "ubertip": 41781},
                    "values": {
                        "name2": "|cffe4cfa3Магия Духа|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Магия Духа|r — уровень |cffffffff2|r (|cffffffffS|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Гнев деревьев», дополнительно увеличивает запас маны ещё на |cffffffff40|cffced4da ед. (всего |cffffffff+80|cffced4da ед.) и скорость восстановления маны на |cffffffff0,25|cffced4da ед./сек. (всего |cffffffff+0,5|cffced4da ед./сек.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
                    }
                },
                {
                    "level": 3,
                    "wts": {"name": 16568, "tip": 16569, "ubertip": 41785},
                    "values": {
                        "name3": "|cffe4cfa3Магия Духа|r — уровень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Магия Духа|r — уровень |cffffffff3|r (|cffffffffS|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Эссенция Яда», дополнительно увеличивает запас маны ещё на |cffffffff40|cffced4da ед. (всего |cffffffff+120|cffced4da ед.) и скорость восстановления маны на |cffffffff0,25|cffced4da ед./сек. (всего |cffffffff+0,75|cffced4da ед./сек.).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛесной Дух|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
                    }
                }
            ]
        },

        # 12. R0KR — Мудрость Дракончиков (3 уровня, горячая клавиша D)
        {
            "id": "R0KR",
            "name": "Мудрость Дракончиков",
            "maxlevel": 3,
            "hotkey": "D",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 16535, "tip": 16540, "ubertip": 16541},
                    "values": {
                        "name1": "|cffe4cfa3Мудрость Дракончиков|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Мудрость Дракончиков|r — уровень |cffffffff1|r (|cffffffffD|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Слияние с Лесом»: временный уход в астральное состояние при получении урона для уклонения от атак.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 16543, "tip": 16544, "ubertip": 16566},
                    "values": {
                        "name2": "|cffe4cfa3Мудрость Дракончиков|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Мудрость Дракончиков|r — уровень |cffffffff2|r (|cffffffffD|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Вспышка маны»: дракончик повышает свою броню и выпускает сгустки магии, наносящие урон врагам при сотворении ими заклинаний.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
                    }
                },
                {
                    "level": 3,
                    "wts": {"name": 41811, "tip": 41812, "ubertip": 16571},
                    "values": {
                        "name3": "|cffe4cfa3Мудрость Дракончиков|r — уровень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Мудрость Дракончиков|r — уровень |cffffffff3|r (|cffffffffD|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Невосприимчивость к магии», обеспечивая абсолютную защиту от любых вражеских заклинаний.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛесной Дракончик|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
                    }
                }
            ]
        },

        # 13. R0AN — Азы Дриад (2 уровня, горячая клавиша A)
        {
            "id": "R0AN",
            "name": "Азы Дриад",
            "maxlevel": 2,
            "hotkey": "A",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41789, "tip": 41790, "ubertip": 41791},
                    "values": {
                        "name1": "|cffe4cfa3Азы Дриад|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Азы Дриад|r — уровень |cffffffff1|r (|cffffffffA|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Рассеяние чар», увеличивает дальность атаки на |cffffffff25|cffced4da ед. и скорость атаки на |cffffffff10%|cffced4da.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДриада|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41794, "tip": 41795, "ubertip": 41796},
                    "values": {
                        "name2": "|cffe4cfa3Мастерство Дриад|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Мастерство Дриад|r — уровень |cffffffff2|r (|cffffffffA|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Неуязвимость к магии», дополнительно увеличивает дальность атаки ещё на |cffffffff25|cffced4da ед. (всего |cffffffff+50|cffced4da ед.) и скорость атаки на |cffffffff10%|cffced4da (всего |cffffffff+20%|cffced4da).|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deДриада|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
                    }
                }
            ]
        },

        # 14. R0KQ — Знание Хранителей (3 уровня, горячая клавиша S)
        {
            "id": "R0KQ",
            "name": "Знание Хранителей",
            "maxlevel": 3,
            "hotkey": "S",
            "levels": [
                {
                    "level": 1,
                    "wts": {"name": 41802, "tip": 41803, "ubertip": 41804},
                    "values": {
                        "name1": "|cffe4cfa3Знание Хранителей|r — уровень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Знание Хранителей|r — уровень |cffffffff1|r (|cffffffffS|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Древесный покров», повышающую броню и стойкость союзников защитным слоем листвы.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
                    }
                },
                {
                    "level": 2,
                    "wts": {"name": 41807, "tip": 41808, "ubertip": 41809},
                    "values": {
                        "name2": "|cffe4cfa3Знание Хранителей|r — уровень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Знание Хранителей|r — уровень |cffffffff2|r (|cffffffffS|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Зов Древних», позволяющую призывать на поле боя малых древней.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
                    }
                },
                {
                    "level": 3,
                    "wts": {"name": 41798, "tip": 41799, "ubertip": 41813},
                    "values": {
                        "name3": "|cffe4cfa3Знание Хранителей|r — уровень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Знание Хранителей|r — уровень |cffffffff3|r (|cffffffffS|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Спокойствие Леса», восполняющую здоровье раненым союзникам в области действия.|n|n|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deХранитель Рощи|cffced4da.|n|n|cffa6afb8Предлагаемый уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
                    }
                }
            ]
        }
    ]

    # Collect all WTS updates
    wts_updates = {}
    for r in ent_research_data:
        for lvl in r["levels"]:
            wts_map = lvl["wts"]
            for field, val in lvl["values"].items():
                if field.startswith("name"):
                    sid = wts_map["name"]
                elif field.startswith("tip"):
                    sid = wts_map["tip"]
                elif field.startswith("ubertip"):
                    sid = wts_map["ubertip"]
                else:
                    raise ValueError(f"Unknown field: {field}")
                wts_updates[sid] = val

    print(f"Applying {len(wts_updates)} WTS updates for Ent researches...")
    wts_content = wts_path.read_text(encoding="utf-8")
    for sid, new_val in sorted(wts_updates.items()):
        wts_content = update_wts_string(wts_content, sid, new_val)

    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print("WTS updated successfully.")

    # Reset HiveWE cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    # Verify all 14 researches in SD and HD
    res_ids = [r["id"] for r in ent_research_data]
    fields_to_check = [
        "name1", "name2", "name3", "name4", "name5", "name6",
        "tip1", "tip2", "tip3", "tip4", "tip5", "tip6",
        "ubertip1", "ubertip2", "ubertip3", "ubertip4", "ubertip5", "ubertip6"
    ]

    checks = []
    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        bulk = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(res_ids), "--fields", ",".join(fields_to_check)] + hd_flag))
        objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}

        for r in ent_research_data:
            fields = objects_by_id.get(r["id"], {})
            for lvl in r["levels"]:
                for f, expected in lvl["values"].items():
                    actual = resolve(fields.get(f, ""))
                    assert actual == expected, f"{f} mismatch for research {r['id']} (hd={hd}):\nActual: '{actual}'\nExpected: '{expected}'"
                    checks.append({
                        "id": r["id"],
                        "field": f,
                        "hd": hd,
                        "status": "OK"
                    })

    print(f"All {len(checks)} readback checks passed in SD and HD!")

    # Verify binary integrity
    current_hashes = {
        "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3u").read_bytes()).hexdigest(),
        "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
        "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
        "w3q": hashlib.sha256(w3q_path.read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest(),
    }
    for k in current_hashes:
        assert current_hashes[k] == original_hashes[k], f"Binary file {k} was unexpectedly modified!"

    print("All other binary file hashes preserved exactly!")

    # Write artifacts
    out_data = {
        "race": "Ents",
        "category": "research",
        "total_researches": len(ent_research_data),
        "total_levels": sum(len(r["levels"]) for r in ent_research_data),
        "total_fields": len(wts_updates),
        "researches": ent_research_data
    }
    (folder / "ent_research.json").write_text(json.dumps(out_data, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_data = {
        "wts_updates_count": len(wts_updates),
        "sd_checks_count": len(checks) // 2,
        "hd_checks_count": len(checks) // 2,
        "total_checks": len(checks),
        "original_hashes": original_hashes,
        "new_wts_hash": new_wts_hash,
        "current_hashes": current_hashes
    }
    (folder / "ent_research_apply.json").write_text(json.dumps(apply_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Artifacts generated in docs/ui_text/.")

if __name__ == "__main__":
    main()
