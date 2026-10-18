# -*- coding: utf-8 -*-
"""Update Dragon race researches (all 26 researches, 65 levels) with SD/HD validation."""
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
    w3q_path = ROOT / "map.w3x/war3map.w3q"
    w3q_skin_path = ROOT / "map.w3x/war3mapSkin.w3q"

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    original_w3q_hash = hashlib.sha256(w3q_path.read_bytes()).hexdigest()
    original_w3q_skin_hash = hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name not in ["war3map.wts", "war3map.w3q", "war3mapSkin.w3q"]
    }

    researches = [
        # --- 1. R0D9: Новое поколение (dra0) ---
        {
            "id": "R0D9", "maxlevel": 2,
            "levels_data": {
                "1": {
                    "wts": {"name1": 39650, "tip1": 39651, "ubertip1": 18672},
                    "values": {
                        "name1": "|cffe4cfa3Новое поколение|r — ступень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Новое поколение|r — ступень |cffffffff1|r (|cffffffffZ|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет выводить драконов второй ступени (Т2) и увеличивает лимит доступных гнёзд драконов.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
                    }
                },
                "2": {
                    "wts": {"name2": 39653, "tip2": 39652, "ubertip2": 18673},
                    "values": {
                        "name2": "|cffe4cfa3Новое поколение|r — ступень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Новое поколение|r — ступень |cffffffff2|r (|cffffffffZ|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет выводить древних драконов третьей ступени (Т3) и дополнительно увеличивает лимит доступных гнёзд драконов.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
                    }
                }
            }
        },
        # --- 2. R0DT: Улучшенная добыча (n03I) ---
        {
            "id": "R0DT", "maxlevel": 3,
            "levels_data": {
                "1": {
                    "wts": {"name1": 21956, "tip1": 21971},
                    "raw": {"ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём древесины, переносимой строителями, на |cffffffff+10|cffced4da ед.|n|nЗатрагивает: |cffa9c7deСтроитель|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"},
                    "values": {
                        "name1": "|cffe4cfa3Улучшенная добыча|r — ступень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Улучшенная добыча|r — ступень |cffffffff1|r (|cffffffffZ|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём древесины, переносимой строителями, на |cffffffff+10|cffced4da ед.|n|nЗатрагивает: |cffa9c7deСтроитель|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
                    }
                },
                "2": {
                    "wts": {"name2": 21970, "tip2": 21972},
                    "raw": {"ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает объём древесины, переносимой строителями, на |cffffffff+10|cffced4da ед. (суммарно |cffffffff+20|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deСтроитель|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"},
                    "values": {
                        "name2": "|cffe4cfa3Улучшенная добыча|r — ступень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Улучшенная добыча|r — ступень |cffffffff2|r (|cffffffffZ|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает объём древесины, переносимой строителями, на |cffffffff+10|cffced4da ед. (суммарно |cffffffff+20|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deСтроитель|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
                    }
                },
                "3": {
                    "wts": {"name3": 21979, "tip3": 21982, "ubertip3": 21985},
                    "values": {
                        "name3": "|cffe4cfa3Улучшенная добыча|r — ступень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Улучшенная добыча|r — ступень |cffffffff3|r (|cffffffffZ|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает объём древесины, переносимой строителями, на |cffffffff+10|cffced4da ед. (суммарно |cffffffff+30|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deСтроитель|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
                    }
                }
            }
        },
        # --- 3. R0B0: Практика полетов (n03I) ---
        {
            "id": "R0B0", "maxlevel": 3,
            "levels_data": {
                "1": {
                    "wts": {"name1": 39839, "tip1": 39840, "ubertip1": 39841},
                    "values": {
                        "name1": "|cffe4cfa3Практика полетов|r — ступень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Практика полетов|r — ступень |cffffffff1|r (|cffffffffS|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость передвижения драконов на |cffffffff+20|cffced4da ед.|n|nЗатрагивает: |cffa9c7deдраконов всех стай|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
                    }
                },
                "2": {
                    "wts": {"name2": 39842, "tip2": 39844, "ubertip2": 39846},
                    "values": {
                        "name2": "|cffe4cfa3Практика полетов|r — ступень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Практика полетов|r — ступень |cffffffff2|r (|cffffffffS|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает скорость передвижения драконов на |cffffffff+20|cffced4da ед. (суммарно |cffffffff+40|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deдраконов всех стай|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
                    }
                },
                "3": {
                    "wts": {"name3": 39843, "tip3": 39845, "ubertip3": 39847},
                    "values": {
                        "name3": "|cffe4cfa3Практика полетов|r — ступень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Практика полетов|r — ступень |cffffffff3|r (|cffffffffS|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает скорость передвижения драконов на |cffffffff+20|cffced4da ед. (суммарно |cffffffff+60|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deдраконов всех стай|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
                    }
                }
            }
        },
        # --- 4. R0AV: Мудрость зеленой стаи (n03I) ---
        {
            "id": "R0AV", "maxlevel": 6,
            "levels_data": {
                str(lvl): {
                    "wts": {
                        f"name{lvl}": [15873, 15871, 15870, 15869, 15868, 15867][lvl-1],
                        f"tip{lvl}": [15887, 15886, 15876, 15875, 15874, 15872][lvl-1],
                        f"ubertip{lvl}": [15888, 15889, 15892, 15894, 15893, 15895][lvl-1]
                    },
                    "values": {
                        f"name{lvl}": f"|cffe4cfa3Мудрость зеленой стаи|r — ступень |cffffffff{lvl}|r",
                        f"tip{lvl}": f"|cffe4cfa3Мудрость зеленой стаи|r — ступень |cffffffff{lvl}|r (|cffffffffQ|r)",
                        f"ubertip{lvl}": (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню зелёных драконов на |cffffffff+1|cffced4da и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deЗеленый дракончик|cffced4da, |cffa9c7deИзумрудный страж|cffced4da, |cffa9c7deДревний зеленый дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                        ) if lvl == 1 else (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает броню зелёных драконов на |cffffffff+1|cffced4da (суммарно |cffffffff+{lvl}|cffced4da) и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deЗеленый дракончик|cffced4da, |cffa9c7deИзумрудный страж|cffced4da, |cffa9c7deДревний зеленый дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
                        )
                    }
                } for lvl in range(1, 7)
            }
        },
        # --- 5. R0AW: Мудрость синей стаи (n03I) ---
        {
            "id": "R0AW", "maxlevel": 6,
            "levels_data": {
                str(lvl): {
                    "wts": {
                        f"name{lvl}": [16705, 16703, 16702, 16699, 16388, 16387][lvl-1],
                        f"tip{lvl}": [16987, 16958, 16936, 16913, 16912, 16704][lvl-1],
                        f"ubertip{lvl}": [16997, 17011, 17012, 17014, 17013, 17015][lvl-1]
                    },
                    "values": {
                        f"name{lvl}": f"|cffe4cfa3Мудрость синей стаи|r — ступень |cffffffff{lvl}|r",
                        f"tip{lvl}": f"|cffe4cfa3Мудрость синей стаи|r — ступень |cffffffff{lvl}|r (|cffffffffR|r)",
                        f"ubertip{lvl}": (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню синих драконов на |cffffffff+1|cffced4da и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deСиний дракончик|cffced4da, |cffa9c7deСиний дракон|cffced4da, |cffa9c7deДревний синий дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                        ) if lvl == 1 else (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает броню синих драконов на |cffffffff+1|cffced4da (суммарно |cffffffff+{lvl}|cffced4da) и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deСиний дракончик|cffced4da, |cffa9c7deСиний дракон|cffced4da, |cffa9c7deДревний синий дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
                        )
                    }
                } for lvl in range(1, 7)
            }
        },
        # --- 6. R0AX: Мудрость красной стаи (n03I) ---
        {
            "id": "R0AX", "maxlevel": 6,
            "levels_data": {
                str(lvl): {
                    "wts": {
                        f"name{lvl}": [17027, 17025, 17024, 17023, 17022, 17021][lvl-1],
                        f"tip{lvl}": [17032, 17031, 17030, 17029, 17028, 17026][lvl-1],
                        f"ubertip{lvl}": [39734, 39735, 39736, 39738, 39737, 39739][lvl-1]
                    },
                    "values": {
                        f"name{lvl}": f"|cffe4cfa3Мудрость красной стаи|r — ступень |cffffffff{lvl}|r",
                        f"tip{lvl}": f"|cffe4cfa3Мудрость красной стаи|r — ступень |cffffffff{lvl}|r (|cffffffffE|r)",
                        f"ubertip{lvl}": (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню красных драконов на |cffffffff+1|cffced4da и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deКрасный дракончик|cffced4da, |cffa9c7deКрасный дракон|cffced4da, |cffa9c7deДревний красный дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                        ) if lvl == 1 else (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает броню красных драконов на |cffffffff+1|cffced4da (суммарно |cffffffff+{lvl}|cffced4da) и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deКрасный дракончик|cffced4da, |cffa9c7deКрасный дракон|cffced4da, |cffa9c7deДревний красный дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
                        )
                    }
                } for lvl in range(1, 7)
            }
        },
        # --- 7. R0AY: Мудрость бронзовой стаи (n03I) ---
        {
            "id": "R0AY", "maxlevel": 6,
            "levels_data": {
                str(lvl): {
                    "wts": {
                        f"name{lvl}": [17050, 17048, 17047, 17046, 17045, 17044][lvl-1],
                        f"tip{lvl}": [17055, 17054, 17053, 17052, 17051, 17049][lvl-1],
                        f"ubertip{lvl}": [17056, 17057, 17058, 17060, 17059, 17061][lvl-1]
                    },
                    "values": {
                        f"name{lvl}": f"|cffe4cfa3Мудрость бронзовой стаи|r — ступень |cffffffff{lvl}|r",
                        f"tip{lvl}": f"|cffe4cfa3Мудрость бронзовой стаи|r — ступень |cffffffff{lvl}|r (|cffffffffW|r)",
                        f"ubertip{lvl}": (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню бронзовых драконов на |cffffffff+1|cffced4da и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deБронзовый дракончик|cffced4da, |cffa9c7deБронзовый дракон|cffced4da, |cffa9c7deДревний бронзовый дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                        ) if lvl == 1 else (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает броню бронзовых драконов на |cffffffff+1|cffced4da (суммарно |cffffffff+{lvl}|cffced4da) и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deБронзовый дракончик|cffced4da, |cffa9c7deБронзовый дракон|cffced4da, |cffa9c7deДревний бронзовый дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
                        )
                    }
                } for lvl in range(1, 7)
            }
        },
        # --- 8. R0AZ: Мудрость черной стаи (n03I) ---
        {
            "id": "R0AZ", "maxlevel": 6,
            "levels_data": {
                str(lvl): {
                    "wts": {
                        f"name{lvl}": [17073, 17071, 17070, 17069, 17068, 17067][lvl-1],
                        f"tip{lvl}": [17078, 17077, 17076, 17075, 17074, 17072][lvl-1],
                        f"ubertip{lvl}": [17079, 17080, 17081, 17083, 17082, 17084][lvl-1]
                    },
                    "values": {
                        f"name{lvl}": f"|cffe4cfa3Мудрость черной стаи|r — ступень |cffffffff{lvl}|r",
                        f"tip{lvl}": f"|cffe4cfa3Мудрость черной стаи|r — ступень |cffffffff{lvl}|r (|cffffffffA|r)",
                        f"ubertip{lvl}": (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню чёрных драконов и драконидов на |cffffffff+1|cffced4da и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deДраконид – следопыт|cffced4da, |cffa9c7deЧерный дракончик|cffced4da, |cffa9c7deЧерный дракон|cffced4da, |cffa9c7deДревний черный дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
                        ) if lvl == 1 else (
                            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает броню чёрных драконов и драконидов на |cffffffff+1|cffced4da (суммарно |cffffffff+{lvl}|cffced4da) и повышает их урон от атак.|n|n"
                            f"Затрагивает: |cffa9c7deДраконид – следопыт|cffced4da, |cffa9c7deЧерный дракончик|cffced4da, |cffa9c7deЧерный дракон|cffced4da, |cffa9c7deДревний черный дракон|cffced4da.|n|n"
                            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
                        )
                    }
                } for lvl in range(1, 7)
            }
        },
        # --- 9. R0AT: Магия времени (n03Z) ---
        {
            "id": "R0AT", "maxlevel": 4,
            "levels_data": {
                "1": {
                    "wts": {"name1": 16994, "tip1": 16995, "ubertip1": 39713},
                    "values": {
                        "name1": "|cffe4cfa3Магия времени|r — ступень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Магия времени|r — ступень |cffffffff1|r (|cffffffffA|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья и маны бронзовых драконов, ускоряет восстановление маны и открывает способность «Зеркальное изображение».|n|nЗатрагивает: |cffa9c7deБронзовый дракончик|cffced4da, |cffa9c7deБронзовый дракон|cffced4da, |cffa9c7deДревний бронзовый дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/4|cffced4da.|r"
                    }
                },
                "2": {
                    "wts": {"name2": 18685, "tip2": 18686, "ubertip2": 39749},
                    "values": {
                        "name2": "|cffe4cfa3Магия времени|r — ступень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Магия времени|r — ступень |cffffffff2|r (|cffffffffA|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает запас здоровья и маны бронзовых драконов и открывает способность «Возврат времени».|n|nЗатрагивает: |cffa9c7deБронзовый дракончик|cffced4da, |cffa9c7deБронзовый дракон|cffced4da, |cffa9c7deДревний бронзовый дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/4|cffced4da.|r"
                    }
                },
                "3": {
                    "wts": {"name3": 39750, "tip3": 39752, "ubertip3": 39837},
                    "values": {
                        "name3": "|cffe4cfa3Магия времени|r — ступень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Магия времени|r — ступень |cffffffff3|r (|cffffffffA|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает запас здоровья и маны бронзовых драконов и открывает способность «Ускорение времени».|n|nЗатрагивает: |cffa9c7deБронзовый дракончик|cffced4da, |cffa9c7deБронзовый дракон|cffced4da, |cffa9c7deДревний бронзовый дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/4|cffced4da.|r"
                    }
                },
                "4": {
                    "wts": {"name4": 39751, "tip4": 39835, "ubertip4": 39838},
                    "values": {
                        "name4": "|cffe4cfa3Магия времени|r — ступень |cffffffff4|r",
                        "tip4": "|cffe4cfa3Магия времени|r — ступень |cffffffff4|r (|cffffffffA|r)",
                        "ubertip4": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Доводит магические способности и боевые показатели бронзовых драконов до совершенства.|n|nЗатрагивает: |cffa9c7deБронзовый дракончик|cffced4da, |cffa9c7deБронзовый дракон|cffced4da, |cffa9c7deДревний бронзовый дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/4|cffced4da.|r"
                    }
                }
            }
        },
        # --- 10. R0AC: Эволюция бронзовых драконов Т2 (n03Z) ---
        {
            "id": "R0AC", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 36800, "tip1": 16421, "ubertip1": 25672},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция бронзовых драконов (Т2)|r",
                        "tip1": "|cffe4cfa3Эволюция бронзовых драконов (Т2)|r (|cffffffffX|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать бронзовых драконов второй ступени (Т2).|n|nОткрывает: |cffa9c7deБронзовый дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 11. R0AB: Эволюция бронзовых драконов Т3 (n03Z) ---
        {
            "id": "R0AB", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 33850, "tip1": 16420, "ubertip1": 25671},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция бронзовых драконов (Т3)|r",
                        "tip1": "|cffe4cfa3Эволюция бронзовых драконов (Т3)|r (|cffffffffC|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать древних бронзовых драконов третьей ступени (Т3).|n|nОткрывает: |cffa9c7deДревний бронзовый дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 12. R0AP: Изумрудная связь (n041) ---
        {
            "id": "R0AP", "maxlevel": 4,
            "levels_data": {
                "1": {
                    "wts": {"name1": 13756, "tip1": 14087, "ubertip1": 37790},
                    "values": {
                        "name1": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff1|r (|cffffffffA|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья и маны зелёных драконов, ускоряет восстановление маны и открывает способность «Изгнание».|n|nЗатрагивает: |cffa9c7deЗеленый дракончик|cffced4da, |cffa9c7deИзумрудный страж|cffced4da, |cffa9c7deДревний зеленый дракон|cffced4da.|r"
                    }
                },
                "2": {
                    "wts": {"name2": 39198, "tip2": 39630},
                    "values": {
                        "name2": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff2|r (|cffffffffA|r)"
                    }
                },
                "3": {
                    "wts": {"name3": 39298, "tip3": 39702},
                    "values": {
                        "name3": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff3|r (|cffffffffA|r)"
                    }
                },
                "4": {
                    "wts": {"name4": 39471, "tip4": 39703},
                    "values": {
                        "name4": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff4|r",
                        "tip4": "|cffe4cfa3Изумрудная связь|r — ступень |cffffffff4|r (|cffffffffA|r)"
                    }
                }
            }
        },
        # --- 13. R0A9: Эволюция зеленых драконов Т2 (n041) ---
        {
            "id": "R0A9", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17159, "tip1": 16412, "ubertip1": 25617},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция зеленых драконов (Т2)|r",
                        "tip1": "|cffe4cfa3Эволюция зеленых драконов (Т2)|r (|cffffffffX|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать зелёных драконов второй ступени (Т2).|n|nОткрывает: |cffa9c7deИзумрудный страж|cffced4da.|r"
                    }
                }
            }
        },
        # --- 14. R0AA: Эволюция зеленых драконов Т3 (n041) ---
        {
            "id": "R0AA", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 22395, "tip1": 16413, "ubertip1": 25670},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция зеленых драконов (Т3)|r",
                        "tip1": "|cffe4cfa3Эволюция зеленых драконов (Т3)|r (|cffffffffC|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать древних зелёных драконов третьей ступени (Т3).|n|nОткрывает: |cffa9c7deДревний зеленый дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 15. R0AS: Мудрость жизни (n042) ---
        {
            "id": "R0AS", "maxlevel": 4,
            "levels_data": {
                "1": {
                    "wts": {"name1": 39801, "tip1": 39802, "ubertip1": 39712},
                    "values": {
                        "name1": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff1|r (|cffffffffA|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья и маны красных драконов, ускоряет восстановление маны и открывает способность «Восстановление».|n|nЗатрагивает: |cffa9c7deКрасный дракончик|cffced4da, |cffa9c7deКрасный дракон|cffced4da, |cffa9c7deДревний красный дракон|cffced4da.|r"
                    }
                },
                "2": {
                    "wts": {"name2": 39804, "tip2": 39807},
                    "values": {
                        "name2": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff2|r (|cffffffffA|r)"
                    }
                },
                "3": {
                    "wts": {"name3": 39805, "tip3": 39808},
                    "values": {
                        "name3": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff3|r (|cffffffffA|r)"
                    }
                },
                "4": {
                    "wts": {"name4": 39806, "tip4": 39809},
                    "values": {
                        "name4": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff4|r",
                        "tip4": "|cffe4cfa3Мудрость жизни|r — ступень |cffffffff4|r (|cffffffffA|r)"
                    }
                }
            }
        },
        # --- 16. R0A5: Эволюция красных драконов Т2 (n042) ---
        {
            "id": "R0A5", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17087, "tip1": 16396, "ubertip1": 25607},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция красных драконов (Т2)|r",
                        "tip1": "|cffe4cfa3Эволюция красных драконов (Т2)|r (|cffffffffX|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать красных драконов второй ступени (Т2).|n|nОткрывает: |cffa9c7deКрасный дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 17. R0A6: Эволюция красных драконов Т3 (n042) ---
        {
            "id": "R0A6", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17100, "tip1": 16397, "ubertip1": 25610},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция красных драконов (Т3)|r",
                        "tip1": "|cffe4cfa3Эволюция красных драконов (Т3)|r (|cffffffffC|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать древних красных драконов третьей ступени (Т3).|n|nОткрывает: |cffa9c7deДревний красный дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 18. R0B3: Практика арканы (n043) ---
        {
            "id": "R0B3", "maxlevel": 4,
            "levels_data": {
                "1": {
                    "wts": {"name1": 39785, "tip1": 39789, "ubertip1": 39848},
                    "values": {
                        "name1": "|cffe4cfa3Практика арканы|r — ступень |cffffffff1|r",
                        "tip1": "|cffe4cfa3Практика арканы|r — ступень |cffffffff1|r (|cffffffffA|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья и маны синих драконов, ускоряет регенерацию маны и открывает способность «Буран».|n|nЗатрагивает: |cffa9c7deСиний дракончик|cffced4da, |cffa9c7deСиний дракон|cffced4da, |cffa9c7deДревний синий дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/4|cffced4da.|r"
                    }
                },
                "2": {
                    "wts": {"name2": 39786, "tip2": 39790, "ubertip2": 39849},
                    "values": {
                        "name2": "|cffe4cfa3Практика арканы|r — ступень |cffffffff2|r",
                        "tip2": "|cffe4cfa3Практика арканы|r — ступень |cffffffff2|r (|cffffffffA|r)",
                        "ubertip2": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает запас здоровья и маны синих драконов и открывает способность «Кольцо льда».|n|nЗатрагивает: |cffa9c7deСиний дракончик|cffced4da, |cffa9c7deСиний дракон|cffced4da, |cffa9c7deДревний синий дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/4|cffced4da.|r"
                    }
                },
                "3": {
                    "wts": {"name3": 39787, "tip3": 39791, "ubertip3": 39850},
                    "values": {
                        "name3": "|cffe4cfa3Практика арканы|r — ступень |cffffffff3|r",
                        "tip3": "|cffe4cfa3Практика арканы|r — ступень |cffffffff3|r (|cffffffffA|r)",
                        "ubertip3": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает запас здоровья и маны синих драконов и открывает способность «Похищение заклинаний».|n|nЗатрагивает: |cffa9c7deСиний дракончик|cffced4da, |cffa9c7deСиний дракон|cffced4da, |cffa9c7deДревний синий дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/4|cffced4da.|r"
                    }
                },
                "4": {
                    "wts": {"name4": 39788, "tip4": 39792, "ubertip4": 39851},
                    "values": {
                        "name4": "|cffe4cfa3Практика арканы|r — ступень |cffffffff4|r",
                        "tip4": "|cffe4cfa3Практика арканы|r — ступень |cffffffff4|r (|cffffffffA|r)",
                        "ubertip4": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает запас здоровья и маны синих драконов и открывает способность «Вспышка маны».|n|nЗатрагивает: |cffa9c7deСиний дракончик|cffced4da, |cffa9c7deСиний дракон|cffced4da, |cffa9c7deДревний синий дракон|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/4|cffced4da.|r"
                    }
                }
            }
        },
        # --- 19. R0A3: Эволюция синих драконов Т2 (n043) ---
        {
            "id": "R0A3", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 16985, "tip1": 17157, "ubertip1": 25604},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция синих драконов (Т2)|r",
                        "tip1": "|cffe4cfa3Эволюция синих драконов (Т2)|r (|cffffffffX|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать синих драконов второй ступени (Т2).|n|nОткрывает: |cffa9c7deСиний дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 20. R0A4: Эволюция синих драконов Т3 (n043) ---
        {
            "id": "R0A4", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 16991, "tip1": 19414, "ubertip1": 25606},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция синих драконов (Т3)|r",
                        "tip1": "|cffe4cfa3Эволюция синих драконов (Т3)|r (|cffffffffC|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать древних синих драконов третьей ступени (Т3).|n|nОткрывает: |cffa9c7deДревний синий дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 21. R0B4: Ярость земли (n044) ---
        {
            "id": "R0B4", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17120, "tip1": 17121, "ubertip1": 16934},
                    "values": {
                        "name1": "|cffe4cfa3Ярость земли|r",
                        "tip1": "|cffe4cfa3Ярость земли|r (|cffffffffZ|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Ярость земли», позволяющую древним чёрным драконам излучать ауру, увеличивающую урон союзников на |cffffffff+10%|cffced4da.|n|nЗатрагивает: |cffa9c7deДревний черный дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 22. R0B2: Ускользание (n044) ---
        {
            "id": "R0B2", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17113, "tip1": 17114, "ubertip1": 17117},
                    "values": {
                        "name1": "|cffe4cfa3Ускользание|r",
                        "tip1": "|cffe4cfa3Ускользание|r (|cffffffffZ|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Даёт драконам и драконидам шанс уклониться от вражеских физических атак.|n|nЗатрагивает: |cffa9c7deдраконов и драконидов|cffced4da.|r"
                    }
                }
            }
        },
        # --- 23. R0AU: Драконья ярость (n044) ---
        {
            "id": "R0AU", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17006, "tip1": 17007, "ubertip1": 17010},
                    "values": {
                        "name1": "|cffe4cfa3Драконья ярость|r",
                        "tip1": "|cffe4cfa3Драконья ярость|r (|cffffffffA|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает способность «Драконья ярость», дающую чёрным драконам шанс нанести критический удар при атаке.|n|nЗатрагивает: |cffa9c7deЧерный дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 24. R0A7: Эволюция черных драконов Т2 (n044) ---
        {
            "id": "R0A7", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17155, "tip1": 16404, "ubertip1": 25614},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция черных драконов (Т2)|r",
                        "tip1": "|cffe4cfa3Эволюция черных драконов (Т2)|r (|cffffffffD|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать чёрных драконов второй ступени (Т2).|n|nОткрывает: |cffa9c7deЧерный дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 25. R0A8: Эволюция черных драконов Т3 (n044) ---
        {
            "id": "R0A8", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17156, "tip1": 16405, "ubertip1": 25615},
                    "values": {
                        "name1": "|cffe4cfa3Эволюция черных драконов (Т3)|r",
                        "tip1": "|cffe4cfa3Эволюция черных драконов (Т3)|r (|cffffffffX|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет обучать древних чёрных драконов третьей ступени (Т3).|n|nОткрывает: |cffa9c7deДревний черный дракон|cffced4da.|r"
                    }
                }
            }
        },
        # --- 26. R0B1: Тренировки драконидов (n05Q dependency) ---
        {
            "id": "R0B1", "maxlevel": 1,
            "levels_data": {
                "1": {
                    "wts": {"name1": 17105, "tip1": 17106, "ubertip1": 17110},
                    "values": {
                        "name1": "|cffe4cfa3Тренировки драконидов|r",
                        "tip1": "|cffe4cfa3Тренировки драконидов|r (|cffffffffS|r)",
                        "ubertip1": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает драконидов боевым приёмам, открывая способность «Сильный удар» и увеличивая их скорость атаки на |cffffffff+20%|cffced4da.|n|nЗатрагивает: |cffa9c7deДраконид – следопыт|cffced4da.|r"
                    }
                }
            }
        }
    ]

    updated_wts = original_wts
    wts_changed_ids = []
    w3q_ops = []

    for r in researches:
        for lvl_str, ldata in r["levels_data"].items():
            wts_map = ldata.get("wts", {})
            vals = ldata.get("values", {})
            for field, wid in wts_map.items():
                val = vals[field]
                updated_wts = update_wts_string(updated_wts, wid, val)
                wts_changed_ids.append(wid)

            raw_map = ldata.get("raw", {})
            for field, val in raw_map.items():
                w3q_ops.append({
                    "type": "upgrade",
                    "id": r["id"],
                    "field": field,
                    "value": val
                })

    # Write updated WTS
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Patch w3q
    if w3q_ops:
        w3q_bytes = w3q_path.read_bytes()
        new_w3q, _ = patch_blob(w3q_bytes, w3q_ops, "upgrade", add_missing=True)
        w3q_path.write_bytes(new_w3q)
        new_w3q_hash = hashlib.sha256(w3q_path.read_bytes()).hexdigest()

        w3q_skin_bytes = w3q_skin_path.read_bytes()
        new_w3q_skin, _ = patch_blob(w3q_skin_bytes, w3q_ops, "upgrade", add_missing=True)
        w3q_skin_path.write_bytes(new_w3q_skin)
        new_w3q_skin_hash = hashlib.sha256(w3q_skin_path.read_bytes()).hexdigest()
    else:
        new_w3q_hash = original_w3q_hash
        new_w3q_skin_hash = original_w3q_skin_hash

    # Readback checks in SD and HD
    checks = []
    res_ids = [r["id"] for r in researches]

    for hd in (False, True):
        hd_flag = ["--hd"] if hd else []
        wts_dict = hw.load_wts_strings()
        resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

        bulk_res = require(cli(["get-objects-bulk", "--type", "upgrade", "--ids", ",".join(res_ids)] + hd_flag))
        res_by_id = {obj["id"]: obj["fields"] for obj in bulk_res.get("objects", [])}

        for r in researches:
            fields = res_by_id.get(r["id"], {})
            verified_fields = []
            for lvl_str, ldata in r["levels_data"].items():
                for f, expected_val in ldata["values"].items():
                    actual_val = resolve(fields.get(f, ""))
                    assert actual_val == expected_val, (
                        f"Mismatch for {r['id']}.{f} (hd={hd}):\nActual: '{actual_val}'\nExpected: '{expected_val}'"
                    )
                    verified_fields.append(f)

            checks.append({
                "id": r["id"],
                "type": "upgrade",
                "variant": "HD" if hd else "SD",
                "fields_verified": verified_fields
            })

    # Save artifacts
    registry = {
        "race": "Dragon",
        "category": "researches",
        "total_researches": len(researches),
        "total_levels": sum(r["maxlevel"] for r in researches),
        "researches": researches
    }
    (folder / "dragon_research.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    apply_artifact = {
        "race": "Dragon",
        "category": "researches",
        "wts_keys_updated": sorted(list(set(wts_changed_ids))),
        "wts_hash_before": original_wts_hash,
        "wts_hash_after": new_wts_hash,
        "w3q_hash_before": original_w3q_hash,
        "w3q_hash_after": new_w3q_hash,
        "w3q_skin_hash_before": original_w3q_skin_hash,
        "w3q_skin_hash_after": new_w3q_skin_hash,
        "other_binary_hashes": other_binary_hashes,
        "checks": checks
    }
    (folder / "dragon_research_apply.json").write_text(json.dumps(apply_artifact, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Successfully updated {len(researches)} Dragon researches ({sum(r['maxlevel'] for r in researches)} levels).")
    print(f"Updated {len(set(wts_changed_ids))} WTS keys, {len(w3q_ops)} w3q patches.")
    print(f"Verified {len(checks)} SD/HD object checks.")

if __name__ == "__main__":
    main()
