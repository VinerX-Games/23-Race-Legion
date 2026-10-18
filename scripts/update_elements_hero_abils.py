# -*- coding: utf-8 -*-
"""Update Elements race hero abilities (27 abilities) with complete SD validation."""
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

# Definitions of all 27 hero abilities
HERO_ABILITIES = [
    # ==========================================
    # HERO: H0EZ Кристальный владыка
    # ==========================================
    {
        "id": "A1MR",
        "hero_id": "H0EZ",
        "name": "|cffe4cfa3Морозный доспех|r",
        "hotkey": "W",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Морозный доспех|r",
            "researchtip": "Изучить «|cffe4cfa3Морозный доспех|r» [|cffffffff%d-й уровень|r] (|cffffffffW|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает кристальной бронёй союзников вокруг владыки, "
                "временно увеличивая их защиту на |cffffffff45|cffced4da сек.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff+2|cffced4da к броне|n"
                "- |cffffffff2|cffced4da: |cffffffff+3|cffced4da к броне|n"
                "- |cffffffff3|cffced4da: |cffffffff+4|cffced4da к броне|n"
                "- |cffffffff4|cffced4da: |cffffffff+5|cffced4da к броне.|r"
            ),
            "tip1": "|cffe4cfa3Морозный доспех|r [|cffffffff1-й уровень|r] (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает на ближайших союзников кристальную броню, увеличивающую защиту на |cffffffff2|cffced4da ед. на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Морозный доспех|r [|cffffffff2-й уровень|r] (|cffffffffW|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает на ближайших союзников кристальную броню, увеличивающую защиту на |cffffffff3|cffced4da ед. на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Морозный доспех|r [|cffffffff3-й уровень|r] (|cffffffffW|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает на ближайших союзников кристальную броню, увеличивающую защиту на |cffffffff4|cffced4da ед. на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Морозный доспех|r [|cffffffff4-й уровень|r] (|cffffffffW|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает на ближайших союзников кристальную броню, увеличивающую защиту на |cffffffff5|cffced4da ед. на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0P4",
        "hero_id": "H0EZ",
        "name": "|cffe4cfa3Бросок валуна|r",
        "hotkey": "Q",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Бросок валуна|r",
            "researchtip": "Изучить «|cffe4cfa3Бросок валуна|r» [|cffffffff%d-й уровень|r] (|cffffffffQ|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает во врага тяжёлый валун, нанося урон и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff3|cffced4da сек. для героев).|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff100|cffced4da ед. урона|n"
                "- |cffffffff2|cffced4da: |cffffffff200|cffced4da ед. урона|n"
                "- |cffffffff3|cffced4da: |cffffffff300|cffced4da ед. урона|n"
                "- |cffffffff4|cffced4da: |cffffffff400|cffced4da ед. урона.|r"
            ),
            "tip1": "|cffe4cfa3Бросок валуна|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает во врага тяжёлый валун, нанося |cffffffff100|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff3|cffced4da сек. для героев).|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Бросок валуна|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает во врага тяжёлый валун, нанося |cffffffff200|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff3|cffced4da сек. для героев).|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Бросок валуна|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает во врага тяжёлый валун, нанося |cffffffff300|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff3|cffced4da сек. для героев).|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Бросок валуна|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает во врага тяжёлый валун, нанося |cffffffff400|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff3|cffced4da сек. для героев).|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0P2",
        "hero_id": "H0EZ",
        "name": "|cffe4cfa3Каменная кожа|r",
        "hotkey": "E",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Каменная кожа|r",
            "researchtip": "Изучить «|cffe4cfa3Каменная кожа|r» [|cffffffff%d-й уровень|r] (|cffffffffE|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно укрепляет каменную кожу исполина, поглощая часть входящего физического урона от атак (минимальный урон: |cffffffff3|cffced4da ед.).|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: снижает урон на |cffffffff5|cffced4da ед.|n"
                "- |cffffffff2|cffced4da: снижает урон на |cffffffff9|cffced4da ед.|n"
                "- |cffffffff3|cffced4da: снижает урон на |cffffffff13|cffced4da ед.|n"
                "- |cffffffff4|cffced4da: снижает урон на |cffffffff18|cffced4da ед.|r"
            ),
            "tip1": "|cffe4cfa3Каменная кожа|r [|cffffffff1-й уровень|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно снижает получаемый физический урон от атак на |cffffffff5|cffced4da ед. Минимальный получаемый урон: |cffffffff3|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Каменная кожа|r [|cffffffff2-й уровень|r]",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно снижает получаемый физический урон от атак на |cffffffff9|cffced4da ед. Минимальный получаемый урон: |cffffffff3|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Каменная кожа|r [|cffffffff3-й уровень|r]",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно снижает получаемый физический урон от атак на |cffffffff13|cffced4da ед. Минимальный получаемый урон: |cffffffff3|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Каменная кожа|r [|cffffffff4-й уровень|r]",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно снижает получаемый физический урон от атак на |cffffffff18|cffced4da ед. Минимальный получаемый урон: |cffffffff3|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "AEtq",
        "hero_id": "H0EZ",
        "name": "|cffe4cfa3Умиротворение|r",
        "hotkey": "R",
        "levels": 2,
        "values": {
            "name": "|cffe4cfa3Умиротворение|r",
            "researchtip": "Изучить «|cffe4cfa3Умиротворение|r» [|cffffffff%d-й уровень|r] (|cffffffffR|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает поток целительной энергии, непрерывно восстанавливающий здоровье союзным войскам в большой области вокруг героя в течение |cffffffff25|cffced4da сек.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff48|cffced4da ед. здоровья/сек.|n"
                "- |cffffffff2|cffced4da: |cffffffff25|cffced4da ед. здоровья/сек.|r"
            ),
            "tip1": "|cffe4cfa3Умиротворение|r [|cffffffff1-й уровень|r] (|cffffffffR|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает поток целительной энергии, восстанавливающий союзникам в области |cffffffff48|cffced4da ед. здоровья в секунду в течение |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r",
            "tip2": "|cffe4cfa3Умиротворение|r [|cffffffff2-й уровень|r] (|cffffffffR|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает поток целительной энергии, восстанавливающий союзникам в области |cffffffff25|cffced4da ед. здоровья в секунду в течение |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
        }
    },

    # ==========================================
    # HERO: H0F0 Мастер ветра
    # ==========================================
    {
        "id": "A0P9",
        "hero_id": "H0F0",
        "name": "|cffe4cfa3Скачок|r",
        "hotkey": "W",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Скачок|r",
            "researchtip": "Изучить «|cffe4cfa3Скачок|r» [|cffffffff%d-й уровень|r] (|cffffffffW|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает героя на указанное расстояние, позволяя быстро вступить в бой или выйти из него.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: дистанция |cffffffff1000|cffced4da, перезарядка |cffffffff15|cffced4da сек., расход маны: |cffffffff50|cffced4da|n"
                "- |cffffffff2|cffced4da: дистанция |cffffffff1075|cffced4da, перезарядка |cffffffff12|cffced4da сек., расход маны: |cffffffff40|cffced4da|n"
                "- |cffffffff3|cffced4da: дистанция |cffffffff1150|cffced4da, перезарядка |cffffffff10|cffced4da сек., расход маны: |cffffffff30|cffced4da|n"
                "- |cffffffff4|cffced4da: дистанция |cffffffff1400|cffced4da, перезарядка |cffffffff10|cffced4da сек., расход маны: |cffffffff20|cffced4da.|r"
            ),
            "tip1": "|cffe4cfa3Скачок|r [|cffffffff1-й уровень|r] (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит героя на расстояние до |cffffffff1000|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Скачок|r [|cffffffff2-й уровень|r] (|cffffffffW|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит героя на расстояние до |cffffffff1075|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Скачок|r [|cffffffff3-й уровень|r] (|cffffffffW|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит героя на расстояние до |cffffffff1150|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Скачок|r [|cffffffff4-й уровень|r] (|cffffffffW|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит героя на расстояние до |cffffffff1400|cffced4da ед.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0PA",
        "hero_id": "H0F0",
        "name": "|cffe4cfa3Ловкий как ветер|r",
        "hotkey": "E",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Ловкий как ветер|r",
            "researchtip": "Изучить «|cffe4cfa3Ловкий как ветер|r» [|cffffffff%d-й уровень|r] (|cffffffffE|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно дарует герою шанс уклониться от вражеской атаки.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff10%|cffced4da шанс уклонения|n"
                "- |cffffffff2|cffced4da: |cffffffff20%|cffced4da шанс уклонения|n"
                "- |cffffffff3|cffced4da: |cffffffff30%|cffced4da шанс уклонения|n"
                "- |cffffffff4|cffced4da: |cffffffff40%|cffced4da шанс уклонения.|r"
            ),
            "tip1": "|cffe4cfa3Ловкий как ветер|r [|cffffffff1-й уровень|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff10%|cffced4da шанс уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Ловкий как ветер|r [|cffffffff2-й уровень|r]",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff20%|cffced4da шанс уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Ловкий как ветер|r [|cffffffff3-й уровень|r]",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff30%|cffced4da шанс уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Ловкий как ветер|r [|cffffffff4-й уровень|r]",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff40%|cffced4da шанс уклониться от вражеской атаки.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A1LE",
        "hero_id": "H0F0",
        "name": "|cffe4cfa3Множественная атака|r",
        "hotkey": "Q",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Множественная атака|r",
            "tip1": "|cffe4cfa3Множественная атака|r [|cffffffff1-й уровень|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать до |cffffffff2|cffced4da наземных противников одновременно в радиусе |cffffffff600|cffced4da, нанося |cffffffff200|cffced4da ед. урона дополнительным целям.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Множественная атака|r [|cffffffff2-й уровень|r]",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать до |cffffffff3|cffced4da наземных противников одновременно в радиусе |cffffffff600|cffced4da, нанося |cffffffff275|cffced4da ед. урона дополнительным целям.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Множественная атака|r [|cffffffff3-й уровень|r]",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать до |cffffffff4|cffced4da наземных противников одновременно в радиусе |cffffffff600|cffced4da, нанося |cffffffff350|cffced4da ед. урона дополнительным целям.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Множественная атака|r [|cffffffff4-й уровень|r]",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать до |cffffffff5|cffced4da наземных противников одновременно в радиусе |cffffffff600|cffced4da, нанося |cffffffff425|cffced4da ед. урона дополнительным целям.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "AHpx",
        "hero_id": "H0F0",
        "name": "|cffe4cfa3Феникс|r",
        "hotkey": "R",
        "levels": 2,
        "values": {
            "name": "|cffe4cfa3Феникс|r",
            "researchtip": "Изучить «|cffe4cfa3Феникс|r» [|cffffffff%d-й уровень|r] (|cffffffffR|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает могучего огненного феникса, сжигающего врагов в бою. "
                "Феникс невосприимчив к магии, обладает устойчивой кожей, а при гибели превращается в яйцо, из которого возрождается заново.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: призывает |cffffffff1|cffced4da феникса, перезарядка |cffffffff180|cffced4da сек.|n"
                "- |cffffffff2|cffced4da: призывает |cffffffff2|cffced4da фениксов, перезарядка |cffffffff120|cffced4da сек.|r"
            ),
            "tip1": "|cffe4cfa3Феникс|r [|cffffffff1-й уровень|r] (|cffffffffR|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает могучего огненного феникса. Феникс невосприимчив к магии, наносит периодический урон огнём вокруг себя и перерождается из яйца после гибели.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r",
            "tip2": "|cffe4cfa3Феникс|r [|cffffffff2-й уровень|r] (|cffffffffR|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da могучих огненных фениксов. Фениксы невосприимчивы к магии, наносят периодический урон огнём вокруг себя и перерождаются из яиц после гибели.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
        }
    },

    # ==========================================
    # HERO: N037 Повелитель огня
    # ==========================================
    {
        "id": "ANic",
        "hero_id": "N037",
        "name": "|cffe4cfa3Испепеление|r",
        "hotkey": "E",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Испепеление|r",
            "researchtip": "Изучить «|cffe4cfa3Испепеление|r» [|cffffffff%d-й уровень|r] (|cffffffffE|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает каждую атаку огненным жаром. Первая атака наносит дополнительный урон, вторая — вдвое больший, третья — втрое и т. д. При гибели цель взрывается, нанося урон врагам поблизости.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff+2|cffced4da к урону за удар, |cffffffff30|cffced4da урона от взрыва|n"
                "- |cffffffff2|cffced4da: |cffffffff+3|cffced4da к урону за удар, |cffffffff45|cffced4da урона от взрыва|n"
                "- |cffffffff3|cffced4da: |cffffffff+4|cffced4da к урону за удар, |cffffffff60|cffced4da урона от взрыва|n"
                "- |cffffffff4|cffced4da: |cffffffff+5|cffced4da к урону за удар, |cffffffff80|cffced4da урона от взрыва.|r"
            ),
            "tip1": "|cffe4cfa3Испепеление|r [|cffffffff1-й уровень|r] (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая последовательная атака по цели наносит на |cffffffff2|cffced4da ед. больше урона. При гибели цель взрывается, нанося до |cffffffff30|cffced4da ед. урона врагам поблизости.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Испепеление|r [|cffffffff2-й уровень|r] (|cffffffffE|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая последовательная атака по цели наносит на |cffffffff3|cffced4da ед. больше урона. При гибели цель взрывается, нанося до |cffffffff45|cffced4da ед. урона врагам поблизости.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Испепеление|r [|cffffffff3-й уровень|r] (|cffffffffE|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая последовательная атака по цели наносит на |cffffffff4|cffced4da ед. больше урона. При гибели цель взрывается, нанося до |cffffffff60|cffced4da ед. урона врагам поблизости.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Испепеление|r [|cffffffff4-й уровень|r] (|cffffffffE|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая последовательная атака по цели наносит на |cffffffff5|cffced4da ед. больше урона. При гибели цель взрывается, нанося до |cffffffff80|cffced4da ед. урона врагам поблизости.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "AHfs",
        "hero_id": "N037",
        "name": "|cffe4cfa3Огненный столб|r",
        "hotkey": "Q",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Огненный столб|r",
            "researchtip": "Изучить «|cffe4cfa3Огненный столб|r» [|cffffffff%d-й уровень|r] (|cffffffffQ|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область столб бушующего пламени, "
                "наносящий высокий урон в первые |cffffffff3|cffced4da сек. и малый урон в последующие |cffffffff6|cffced4da сек.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff45|cffced4da ед. урона/сек.|n"
                "- |cffffffff2|cffced4da: |cffffffff80|cffced4da ед. урона/сек.|n"
                "- |cffffffff3|cffced4da: |cffffffff110|cffced4da ед. урона/сек.|n"
                "- |cffffffff4|cffced4da: |cffffffff150|cffced4da ед. урона/сек.|r"
            ),
            "tip1": "|cffe4cfa3Огненный столб|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным войскам в области |cffffffff45|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Огненный столб|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным войскам в области |cffffffff80|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Огненный столб|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным войскам в области |cffffffff110|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Огненный столб|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит наземным войскам в области |cffffffff150|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "ANlm",
        "hero_id": "N037",
        "name": "|cffe4cfa3Призыв порождения лавы|r",
        "hotkey": "W",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Призыв порождения лавы|r",
            "researchtip": "Изучить «|cffe4cfa3Призыв порождения лавы|r» [|cffffffff%d-й уровень|r] (|cffffffffW|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает лавовое создание. Нанося удары, оно насыщается и разделяется на два полноценных создания с полным здоровьем.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff425|cffced4da ед. здоровья, |cffffffff15-21|cffced4da ед. урона, жизнь |cffffffff70|cffced4da сек.|n"
                "- |cffffffff2|cffced4da: |cffffffff550|cffced4da ед. здоровья, |cffffffff22-31|cffced4da ед. урона, жизнь |cffffffff75|cffced4da сек.|n"
                "- |cffffffff3|cffced4da: |cffffffff700|cffced4da ед. здоровья, |cffffffff29-41|cffced4da ед. урона, жизнь |cffffffff80|cffced4da сек.|n"
                "- |cffffffff4|cffced4da: |cffffffff900|cffced4da ед. здоровья, |cffffffff37-61|cffced4da ед. урона, жизнь |cffffffff85|cffced4da сек.|r"
            ),
            "tip1": "|cffe4cfa3Призыв порождения лавы|r [|cffffffff1-й уровень|r] (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает порождение лавы (|cffffffff425|cffced4da ед. здоровья, |cffffffff15-21|cffced4da ед. урона). При атаках оно разделяется на двух созданий. Время жизни: |cffffffff70|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Призыв порождения лавы|r [|cffffffff2-й уровень|r] (|cffffffffW|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает порождение лавы (|cffffffff550|cffced4da ед. здоровья, |cffffffff22-31|cffced4da ед. урона). При атаках оно разделяется на двух созданий. Время жизни: |cffffffff75|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Призыв порождения лавы|r [|cffffffff3-й уровень|r] (|cffffffffW|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает порождение лавы (|cffffffff700|cffced4da ед. здоровья, |cffffffff29-41|cffced4da ед. урона). При атаках оно разделяется на двух созданий. Время жизни: |cffffffff80|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Призыв порождения лавы|r [|cffffffff4-й уровень|r] (|cffffffffW|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает порождение лавы (|cffffffff900|cffced4da ед. здоровья, |cffffffff37-61|cffced4da ед. урона). При атаках оно разделяется на двух созданий. Время жизни: |cffffffff85|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0P7",
        "hero_id": "N037",
        "name": "|cffe4cfa3Кольцо огня|r",
        "hotkey": "R",
        "levels": 2,
        "values": {
            "name": "|cffe4cfa3Кольцо огня|r",
            "researchtip": "Изучить «|cffe4cfa3Кольцо огня|r» [|cffffffff%d-й уровень|r] (|cffffffffR|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает выбранную цель огненным кольцом на |cffffffff30|cffced4da сек., которое выжигает здоровье врагов вокруг и передаёт жизненную силу герою и союзникам.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff30|cffced4da ед. урона/сек. врагам, исцеляет |cffffffff20|cffced4da ед./сек., перезарядка |cffffffff55|cffced4da сек.|n"
                "- |cffffffff2|cffced4da: |cffffffff40|cffced4da ед. урона/сек. врагам, исцеляет |cffffffff20|cffced4da ед./сек., перезарядка |cffffffff45|cffced4da сек.|r"
            ),
            "tip1": "|cffe4cfa3Кольцо огня|r [|cffffffff1-й уровень|r] (|cffffffffR|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает цель кольцом огня на |cffffffff30|cffced4da сек., наносящим врагам |cffffffff30|cffced4da ед. урона/сек. и восстанавливающим герою и союзникам по |cffffffff20|cffced4da ед. здоровья/сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r",
            "tip2": "|cffe4cfa3Кольцо огня|r [|cffffffff2-й уровень|r] (|cffffffffR|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает цель кольцом огня на |cffffffff30|cffced4da сек., наносящим врагам |cffffffff40|cffced4da ед. урона/сек. и восстанавливающим герою и союзникам по |cffffffff20|cffced4da ед. здоровья/сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
        }
    },

    # ==========================================
    # HERO: E029 Владыка морей
    # ==========================================
    {
        "id": "A0OU",
        "hero_id": "E029",
        "name": "|cffe4cfa3Сокрушительная волна|r",
        "hotkey": "Q",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Сокрушительная волна|r",
            "researchtip": "Изучить «|cffe4cfa3Сокрушительная волна|r» [|cffffffff%d-й уровень|r] (|cffffffffQ|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на ряды врагов мощную волну океанских вод, наносящую урон целям по линии удара на расстоянии до |cffffffff800|cffced4da.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff175|cffced4da ед. урона|n"
                "- |cffffffff2|cffced4da: |cffffffff225|cffced4da ед. урона|n"
                "- |cffffffff3|cffced4da: |cffffffff275|cffced4da ед. урона|n"
                "- |cffffffff4|cffced4da: |cffffffff350|cffced4da ед. урона.|r"
            ),
            "tip1": "|cffe4cfa3Сокрушительная волна|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну океанских вод, наносящую |cffffffff175|cffced4da ед. урона врагам на расстоянии до |cffffffff800|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Сокрушительная волна|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну океанских вод, наносящую |cffffffff225|cffced4da ед. урона врагам на расстоянии до |cffffffff800|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Сокрушительная волна|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну океанских вод, наносящую |cffffffff275|cffced4da ед. урона врагам на расстоянии до |cffffffff800|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Сокрушительная волна|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну океанских вод, наносящую |cffffffff350|cffced4da ед. урона врагам на расстоянии до |cffffffff800|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0OT",
        "hero_id": "E029",
        "name": "|cffe4cfa3Поле астрала|r",
        "hotkey": "W",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Поле астрала|r",
            "researchtip": "Изучить «|cffe4cfa3Поле астрала|r» [|cffffffff%d-й уровень|r] (|cffffffffW|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Перемещает всех существ в выбранной области в астральный мир. Астральные существа не могут атаковать или подвергаться физическим атакам, но получают повышенный урон от магии.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: область |cffffffff150|cffced4da, расход маны: |cffffffff100|cffced4da|n"
                "- |cffffffff2|cffced4da: область |cffffffff175|cffced4da, расход маны: |cffffffff125|cffced4da|n"
                "- |cffffffff3|cffced4da: область |cffffffff200|cffced4da, расход маны: |cffffffff150|cffced4da|n"
                "- |cffffffff4|cffced4da: область |cffffffff225|cffced4da, расход маны: |cffffffff200|cffced4da.|r"
            ),
            "tip1": "|cffe4cfa3Поле астрала|r [|cffffffff1-й уровень|r] (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех существ в радиусе |cffffffff150|cffced4da в астральный мир. Они не могут атаковать, но получают на |cffffffff66%|cffced4da больше магического урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Поле астрала|r [|cffffffff2-й уровень|r] (|cffffffffW|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех существ в радиусе |cffffffff175|cffced4da в астральный мир. Они не могут атаковать, но получают на |cffffffff66%|cffced4da больше магического урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Поле астрала|r [|cffffffff3-й уровень|r] (|cffffffffW|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех существ в радиусе |cffffffff200|cffced4da в астральный мир. Они не могут атаковать, но получают на |cffffffff66%|cffced4da больше магического урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Поле астрала|r [|cffffffff4-й уровень|r] (|cffffffffW|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Помещает всех существ в радиусе |cffffffff225|cffced4da в астральный мир. Они не могут атаковать, но получают на |cffffffff66%|cffced4da больше магического урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0QL",
        "hero_id": "E029",
        "name": "|cffe4cfa3Щит маны|r",
        "hotkey": "E",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Щит маны|r",
            "researchtip": "Изучить «|cffe4cfa3Щит маны|r» [|cffffffff%d-й уровень|r] (|cffffffffE|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт магический барьер, поглощающий входящий урон за счёт запаса маны владыки.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: поглощает |cffffffff1|cffced4da ед. урона за единицу маны|n"
                "- |cffffffff2|cffced4da: поглощает |cffffffff1,5|cffced4da ед. урона за единицу маны|n"
                "- |cffffffff3|cffced4da: поглощает |cffffffff2|cffced4da ед. урона за единицу маны|n"
                "- |cffffffff4|cffced4da: поглощает |cffffffff2,5|cffced4da ед. урона за единицу маны.|r"
            ),
            "tip1": "|cffe4cfa3Щит маны|r [|cffffffff1-й уровень|r] (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует щит, поглощающий |cffffffff1|cffced4da ед. входящего урона за каждую единицу маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Щит маны|r [|cffffffff2-й уровень|r] (|cffffffffE|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует щит, поглощающий |cffffffff1,5|cffced4da ед. входящего урона за каждую единицу маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Щит маны|r [|cffffffff3-й уровень|r] (|cffffffffE|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует щит, поглощающий |cffffffff2|cffced4da ед. входящего урона за каждую единицу маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Щит маны|r [|cffffffff4-й уровень|r] (|cffffffffE|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует щит, поглощающий |cffffffff2,5|cffced4da ед. входящего урона за каждую единицу маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0OR",
        "hero_id": "E029",
        "name": "|cffe4cfa3Наводнение|r",
        "hotkey": "R",
        "levels": 2,
        "values": {
            "name": "|cffe4cfa3Наводнение|r",
            "researchtip": "Изучить «|cffe4cfa3Наводнение|r» [|cffffffff%d-й уровень|r] (|cffffffffR|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает мощь океанских приливов, позволяя владыке морей атаковать до |cffffffff11|cffced4da вражеских целей одновременно.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: время действия |cffffffff10|cffced4da сек., перезарядка |cffffffff80|cffced4da сек.|n"
                "- |cffffffff2|cffced4da: время действия |cffffffff10|cffced4da сек., перезарядка |cffffffff70|cffced4da сек.|r"
            ),
            "tip1": "|cffe4cfa3Наводнение|r [|cffffffff1-й уровень|r] (|cffffffffR|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет поражать до |cffffffff11|cffced4da противников одновременно при каждой атаке в течение |cffffffff10|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r",
            "tip2": "|cffe4cfa3Наводнение|r [|cffffffff2-й уровень|r] (|cffffffffR|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет поражать до |cffffffff11|cffced4da противников одновременно при каждой атаке в течение |cffffffff10|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
        }
    },
    {
        "id": "A0YH",
        "hero_id": "E029",
        "name": "|cffe4cfa3Морской владыка|r",
        "hotkey": "",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Морской владыка|r",
            "tip1": "|cffe4cfa3Морской владыка|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения находящихся рядом союзников на |cffffffff20%|cffced4da и повышает скорость регенерации их здоровья на |cffffffff0,6|cffced4da ед./сек.|r"
        }
    },

    # ==========================================
    # HERO: E027 Владыка ветра
    # ==========================================
    {
        "id": "A0P0",
        "hero_id": "E027",
        "name": "|cffe4cfa3Торнадо|r",
        "hotkey": "Q",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Торнадо|r",
            "researchtip": "Изучить «|cffe4cfa3Торнадо|r» [|cffffffff%d-й уровень|r] (|cffffffffQ|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт бушующий вихрь, наносящий высокий периодический урон наземным войскам в области в первые |cffffffff3|cffced4da сек. и малый урон в последующие |cffffffff6|cffced4da сек.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff45|cffced4da ед. урона/сек.|n"
                "- |cffffffff2|cffced4da: |cffffffff80|cffced4da ед. урона/сек.|n"
                "- |cffffffff3|cffced4da: |cffffffff110|cffced4da ед. урона/сек.|n"
                "- |cffffffff4|cffced4da: |cffffffff150|cffced4da ед. урона/сек.|r"
            ),
            "tip1": "|cffe4cfa3Торнадо|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт разрушительный вихрь, наносящий наземным войскам |cffffffff45|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Торнадо|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт разрушительный вихрь, наносящий наземным войскам |cffffffff80|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Торнадо|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт разрушительный вихрь, наносящий наземным войскам |cffffffff110|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Торнадо|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт разрушительный вихрь, наносящий наземным войскам |cffffffff150|cffced4da ед. урона/сек. в течение |cffffffff3|cffced4da сек., а затем незначительный урон ещё |cffffffff6|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0OX",
        "hero_id": "E027",
        "name": "|cffe4cfa3Разрушающий взмах|r",
        "hotkey": "",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Разрушающий взмах|r",
            "researchtip": "Изучить «|cffe4cfa3Разрушающий взмах|r» [|cffffffff%d-й уровень|r]",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс при атаке нанести мощный круговой удар, поражающий противников вокруг цели.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff25%|cffced4da шанс, |cffffffff125|cffced4da ед. урона вокруг цели|n"
                "- |cffffffff2|cffced4da: |cffffffff30%|cffced4da шанс, |cffffffff150|cffced4da ед. урона вокруг цели|n"
                "- |cffffffff3|cffced4da: |cffffffff35%|cffced4da шанс, |cffffffff175|cffced4da ед. урона вокруг цели|n"
                "- |cffffffff4|cffced4da: |cffffffff40%|cffced4da шанс, |cffffffff200|cffced4da ед. урона вокруг цели.|r"
            ),
            "tip1": "|cffe4cfa3Разрушающий взмах|r [|cffffffff1-й уровень|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff25%|cffced4da шанс при атаке нанести |cffffffff125|cffced4da ед. урона врагам вокруг основной цели.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Разрушающий взмах|r [|cffffffff2-й уровень|r]",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff30%|cffced4da шанс при атаке нанести |cffffffff150|cffced4da ед. урона врагам вокруг основной цели.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Разрушающий взмах|r [|cffffffff3-й уровень|r]",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff35%|cffced4da шанс при атаке нанести |cffffffff175|cffced4da ед. урона врагам вокруг основной цели.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Разрушающий взмах|r [|cffffffff4-й уровень|r]",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт |cffffffff40%|cffced4da шанс при атаке нанести |cffffffff200|cffced4da ед. урона врагам вокруг основной цели.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0OW",
        "hero_id": "E027",
        "name": "|cffe4cfa3Скорость ветра|r",
        "hotkey": "E",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Скорость ветра|r",
            "researchtip": "Изучить «|cffe4cfa3Скорость ветра|r» [|cffffffff%d-й уровень|r] (|cffffffffE|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура попутного ветра ускоряет перемещение и атаки находящихся рядом союзных войск.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff+10%|cffced4da к скорости бега, |cffffffff+15%|cffced4da к скорости атаки|n"
                "- |cffffffff2|cffced4da: |cffffffff+15%|cffced4da к скорости бега, |cffffffff+20%|cffced4da к скорости атаки|n"
                "- |cffffffff3|cffced4da: |cffffffff+20%|cffced4da к скорости бега, |cffffffff+25%|cffced4da к скорости атаки|n"
                "- |cffffffff4|cffced4da: |cffffffff+40%|cffced4da к скорости бега, |cffffffff+30%|cffced4da к скорости атаки.|r"
            ),
            "tip1": "|cffe4cfa3Скорость ветра|r [|cffffffff1-й уровень|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения союзников на |cffffffff10%|cffced4da и скорость их атаки на |cffffffff15%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Скорость ветра|r [|cffffffff2-й уровень|r]",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения союзников на |cffffffff15%|cffced4da и скорость их атаки на |cffffffff20%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Скорость ветра|r [|cffffffff3-й уровень|r]",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения союзников на |cffffffff20%|cffced4da и скорость их атаки на |cffffffff25%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Скорость ветра|r [|cffffffff4-й уровень|r]",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения союзников на |cffffffff40%|cffced4da и скорость их атаки на |cffffffff30%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0P1",
        "hero_id": "E027",
        "name": "|cffe4cfa3Грозовые Облака|r",
        "hotkey": "R",
        "levels": 2,
        "values": {
            "name": "|cffe4cfa3Грозовые Облака|r",
            "researchtip": "Изучить «|cffe4cfa3Грозовые Облака|r» [|cffffffff%d-й уровень|r] (|cffffffffR|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на поле боя стаю грозовых туч, непрерывно поражающих врагов электрическими разрядами.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: призывает от |cffffffff3|cffced4da до |cffffffff5|cffced4da грозовых облаков|n"
                "- |cffffffff2|cffced4da: призывает от |cffffffff3|cffced4da до |cffffffff6|cffced4da грозовых облаков.|r"
            ),
            "tip1": "|cffe4cfa3Грозовые Облака|r [|cffffffff1-й уровень|r] (|cffffffffR|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает от |cffffffff3|cffced4da до |cffffffff5|cffced4da грозовых облаков, непрерывно атакующих молниями врагов вокруг себя.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r",
            "tip2": "|cffe4cfa3Грозовые Облака|r [|cffffffff2-й уровень|r] (|cffffffffR|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает от |cffffffff3|cffced4da до |cffffffff6|cffced4da грозовых облаков, непрерывно атакующих молниями врагов вокруг себя.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
        }
    },
    {
        "id": "A0YI",
        "hero_id": "E027",
        "name": "|cffe4cfa3Ускользание|r",
        "hotkey": "",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Ускользание|r",
            "tip1": "|cffe4cfa3Ускользание|r",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно даёт владыке ветра |cffffffff35%|cffced4da шанс уклониться от вражеской физической атаки.|r"
        }
    },

    # ==========================================
    # HERO: E028 Владыка Огня
    # ==========================================
    {
        "id": "A0OP",
        "hero_id": "E028",
        "name": "|cffe4cfa3Колоссальный удар|r",
        "hotkey": "Q",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Колоссальный удар|r",
            "researchtip": "Изучить «|cffe4cfa3Колоссальный удар|r» [|cffffffff%d-й уровень|r] (|cffffffffQ|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет атаки Рагнароса силой сокрушительного огненного удара, наносящего |cffffffff70%|cffced4da урона по области в радиусе |cffffffff200|cffced4da от цели в течение |cffffffff25|cffced4da сек.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: перезарядка |cffffffff50|cffced4da сек.|n"
                "- |cffffffff2|cffced4da: перезарядка |cffffffff45|cffced4da сек.|n"
                "- |cffffffff3|cffced4da: перезарядка |cffffffff40|cffced4da сек.|n"
                "- |cffffffff4|cffced4da: перезарядка |cffffffff35|cffced4da сек.|r"
            ),
            "tip1": "|cffe4cfa3Колоссальный удар|r [|cffffffff1-й уровень|r] (|cffffffffQ|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет атаки владыки огня способностью наносить |cffffffff70%|cffced4da урона по области в радиусе |cffffffff200|cffced4da от цели на |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Колоссальный удар|r [|cffffffff2-й уровень|r] (|cffffffffQ|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет атаки владыки огня способностью наносить |cffffffff70%|cffced4da урона по области в радиусе |cffffffff200|cffced4da от цели на |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Колоссальный удар|r [|cffffffff3-й уровень|r] (|cffffffffQ|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет атаки владыки огня способностью наносить |cffffffff70%|cffced4da урона по области в радиусе |cffffffff200|cffced4da от цели на |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Колоссальный удар|r [|cffffffff4-й уровень|r] (|cffffffffQ|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет атаки владыки огня способностью наносить |cffffffff70%|cffced4da урона по области в радиусе |cffffffff200|cffced4da от цели на |cffffffff25|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0ON",
        "hero_id": "E028",
        "name": "|cffe4cfa3Благодать Пламени|r",
        "hotkey": "W",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Благодать Пламени|r",
            "researchtip": "Изучить «|cffe4cfa3Благодать Пламени|r» [|cffffffff%d-й уровень|r] (|cffffffffW|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вдохновляет союзников жаром стихии, временно увеличивая их урон на |cffffffff45|cffced4da сек.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: |cffffffff+25%|cffced4da к урону, радиус |cffffffff500|cffced4da|n"
                "- |cffffffff2|cffced4da: |cffffffff+35%|cffced4da к урону, радиус |cffffffff600|cffced4da|n"
                "- |cffffffff3|cffced4da: |cffffffff+45%|cffced4da к урону, радиус |cffffffff700|cffced4da|n"
                "- |cffffffff4|cffced4da: |cffffffff+55%|cffced4da к урону, радиус |cffffffff800|cffced4da.|r"
            ),
            "tip1": "|cffe4cfa3Благодать Пламени|r [|cffffffff1-й уровень|r] (|cffffffffW|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атаки ближайших союзников на |cffffffff25%|cffced4da в радиусе |cffffffff500|cffced4da на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Благодать Пламени|r [|cffffffff2-й уровень|r] (|cffffffffW|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атаки ближайших союзников на |cffffffff35%|cffced4da в радиусе |cffffffff600|cffced4da на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Благодать Пламени|r [|cffffffff3-й уровень|r] (|cffffffffW|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атаки ближайших союзников на |cffffffff45%|cffced4da в радиусе |cffffffff700|cffced4da на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Благодать Пламени|r [|cffffffff4-й уровень|r] (|cffffffffW|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу атаки ближайших союзников на |cffffffff55%|cffced4da в радиусе |cffffffff800|cffced4da на |cffffffff45|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0QJ",
        "hero_id": "E028",
        "name": "|cffe4cfa3Ярость Пламени|r",
        "hotkey": "E",
        "levels": 4,
        "values": {
            "name": "|cffe4cfa3Ярость Пламени|r",
            "researchtip": "Изучить «|cffe4cfa3Ярость Пламени|r» [|cffffffff%d-й уровень|r] (|cffffffffE|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает во врагов сокрушительный огненный вихрь в радиусе |cffffffff1000|cffced4da, осыпающий цели пылающими сгустками.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: перезарядка |cffffffff40|cffced4da сек., расход маны: |cffffffff100|cffced4da|n"
                "- |cffffffff2|cffced4da: перезарядка |cffffffff35|cffced4da сек., расход маны: |cffffffff125|cffced4da|n"
                "- |cffffffff3|cffced4da: перезарядка |cffffffff30|cffced4da сек., расход маны: |cffffffff150|cffced4da|n"
                "- |cffffffff4|cffced4da: перезарядка |cffffffff25|cffced4da сек., расход маны: |cffffffff175|cffced4da.|r"
            ),
            "tip1": "|cffe4cfa3Ярость Пламени|r [|cffffffff1-й уровень|r] (|cffffffffE|r)",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сокрушительный поток огненных сгустков по всем врагам в радиусе |cffffffff1000|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r",
            "tip2": "|cffe4cfa3Ярость Пламени|r [|cffffffff2-й уровень|r] (|cffffffffE|r)",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сокрушительный поток огненных сгустков по всем врагам в радиусе |cffffffff1000|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r",
            "tip3": "|cffe4cfa3Ярость Пламени|r [|cffffffff3-й уровень|r] (|cffffffffE|r)",
            "ubertip3": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сокрушительный поток огненных сгустков по всем врагам в радиусе |cffffffff1000|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r",
            "tip4": "|cffe4cfa3Ярость Пламени|r [|cffffffff4-й уровень|r] (|cffffffffE|r)",
            "ubertip4": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сокрушительный поток огненных сгустков по всем врагам в радиусе |cffffffff1000|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
        }
    },
    {
        "id": "A0OQ",
        "hero_id": "E028",
        "name": "|cffe4cfa3Пламенное перерождение|r",
        "hotkey": "R",
        "levels": 2,
        "values": {
            "name": "|cffe4cfa3Пламенное перерождение|r",
            "researchtip": "Изучить «|cffe4cfa3Пламенное перерождение|r» [|cffffffff%d-й уровень|r] (|cffffffffR|r)",
            "researchubertip": (
                "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует Рагнаросу способность мгновенно возродиться на месте гибели с полным запасом сил.|n|n"
                "|cffa6afb8Уровни:|cffced4da|n"
                "- |cffffffff1|cffced4da: перезарядка |cffffffff240|cffced4da сек.|n"
                "- |cffffffff2|cffced4da: перезарядка |cffffffff150|cffced4da сек.|r"
            ),
            "tip1": "|cffe4cfa3Пламенное перерождение|r [|cffffffff1-й уровень|r]",
            "ubertip1": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно возвращает Рагнароса к жизни на месте гибели с полным запасом здоровья и маны. Перезарядка: |cffffffff240|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r",
            "tip2": "|cffe4cfa3Пламенное перерождение|r [|cffffffff2-й уровень|r]",
            "ubertip2": "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно возвращает Рагнароса к жизни на месте гибели с полным запасом здоровья и маны. Перезарядка: |cffffffff150|cffced4da сек.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
        }
    },
    {
        "id": "A0YG",
        "hero_id": "E028",
        "name": "|cffe4cfa3Сожжение доспехов|r",
        "hotkey": "",
        "levels": 1,
        "values": {
            "name": "|cffe4cfa3Сожжение доспехов|r"
        }
    }
]

def main():
    folder = ROOT / "docs/ui_text"
    wts_path = ROOT / "map.w3x/war3map.wts"
    w3a_path = ROOT / "map.w3x/war3map.w3a"
    w3a_skin_path = ROOT / "map.w3x/war3mapSkin.w3a"

    original_wts = wts_path.read_text(encoding="utf-8")
    original_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    original_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()
    original_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()

    source = ROOT / "map.w3x"
    other_binary_hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in source.glob("war3map*")
        if p.is_file() and p.name not in ["war3map.wts", "war3map.w3a", "war3mapSkin.w3a"]
    }

    raw_data = json.loads((folder / "elements_hero_abils_raw.json").read_text(encoding="utf-8"))

    # Process WTS updates and patch_blob operations
    updated_wts = original_wts
    wts_changed = []
    object_ops = []

    for abil in HERO_ABILITIES:
        aid = abil["id"]
        raw_fields = raw_data.get(aid, {})
        vals = abil.get("values", {})
        for field, val in vals.items():
            f_info = raw_fields.get(field)
            if isinstance(f_info, dict) and "wts_id" in f_info:
                wid = f_info["wts_id"]
                updated_wts = update_wts_string(updated_wts, wid, val)
                wts_changed.append(wid)
            else:
                object_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": field,
                    "value": val
                })

    print(f"Total WTS keys to update: {len(wts_changed)}")
    print(f"Total inline object_ops to patch: {len(object_ops)}")
    for op in object_ops:
        print(f"  Op: [{op['id']}] {op['field']} -> {repr(op['value'][:50])}")

    # Write WTS
    wts_path.write_text(updated_wts, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()

    # Write binary patches if any
    if object_ops:
        w3a_bytes = w3a_path.read_bytes()
        new_w3a, _ = patch_blob(w3a_bytes, object_ops, "ability", add_missing=True)
        w3a_path.write_bytes(new_w3a)
        new_w3a_hash = hashlib.sha256(w3a_path.read_bytes()).hexdigest()

        w3a_skin_bytes = w3a_skin_path.read_bytes()
        new_w3a_skin, _ = patch_blob(w3a_skin_bytes, object_ops, "ability", add_missing=True)
        w3a_skin_path.write_bytes(new_w3a_skin)
        new_w3a_skin_hash = hashlib.sha256(w3a_skin_path.read_bytes()).hexdigest()
    else:
        new_w3a_hash = original_w3a_hash
        new_w3a_skin_hash = original_w3a_skin_hash

    # Readback checks in SD mode ONLY (User instruction: SD only, no HD)
    abil_ids = [a["id"] for a in HERO_ABILITIES]
    bulk = require(cli(["get-objects-bulk", "--type", "ability", "--ids", ",".join(abil_ids)]))
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    objects_by_id = {obj["id"]: obj["fields"] for obj in bulk.get("objects", [])}
    checks = []
    mismatches = []

    for a in HERO_ABILITIES:
        aid = a["id"]
        fields = objects_by_id.get(aid, {})
        for f, expected in a["values"].items():
            actual = resolve(fields.get(f, ""))
            matched = (actual == expected)
            checks.append({
                "id": aid,
                "field": f,
                "matched": matched,
                "expected": expected,
                "actual": actual
            })
            if not matched:
                mismatches.append((aid, f, expected, actual))

    print(f"\nSD readback validation: {len(checks) - len(mismatches)}/{len(checks)} fields matched.")
    if mismatches:
        print(f"FAILED: {len(mismatches)} mismatches:")
        for aid, f, exp, act in mismatches:
            print(f"  [{aid}] {f}:\n    Expected: {repr(exp)}\n    Actual:   {repr(act)}")
        sys.exit(1)

    # Save application report and registry
    apply_report = {
        "race": "elements",
        "category": "hero_abilities",
        "total_abilities": len(HERO_ABILITIES),
        "total_checks": len(checks),
        "all_matched": len(mismatches) == 0,
        "wts_keys_updated": len(wts_changed),
        "inline_ops": len(object_ops),
        "hashes": {
            "wts": {"before": original_wts_hash, "after": new_wts_hash},
            "w3a": {"before": original_w3a_hash, "after": new_w3a_hash},
            "w3a_skin": {"before": original_w3a_skin_hash, "after": new_w3a_skin_hash}
        },
        "other_binaries_untouched": all(
            hashlib.sha256((source / name).read_bytes()).hexdigest() == h
            for name, h in other_binary_hashes.items()
        )
    }
    (folder / "elements_hero_abils_apply.json").write_text(
        json.dumps(apply_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (folder / "elements_hero_abils.json").write_text(
        json.dumps(HERO_ABILITIES, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Report saved to docs/ui_text/elements_hero_abils_apply.json")
    print("All 27 hero abilities successfully validated in SD mode!")

if __name__ == "__main__":
    main()
