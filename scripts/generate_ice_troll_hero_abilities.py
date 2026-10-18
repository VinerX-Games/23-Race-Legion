# -*- coding: utf-8 -*-
"""Generate UI texts, plan, and registry for Ice Troll hero abilities (Batch 1).

Adheres strictly to docs/UI_TEXT_STYLE.md and docs/UI_COLOR_PALETTE.md.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ABILITIES = [
    # 1. AOhw - Волна исцеления (Dark Hunter Q, 4 lvls)
    {
        "id": "AOhw",
        "name": "|cffe4cfa3Волна исцеления|r",
        "researchtip": "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт цепную волну исцеляющей энергии, которая восполняет здоровье "
            "выбранного союзника и переходит на ближайшие раненые дружественные цели. "
            "С каждым переходом эффективность снижается на |cffffffff5|cffced4da%.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Восстанавливает |cffffffff130|cffced4da здоровья, до |cffffffff5|cffced4da целей.|n"
            "- |cffffffff2|cffced4da: Восстанавливает |cffffffff215|cffced4da здоровья, до |cffffffff10|cffced4da целей.|n"
            "- |cffffffff3|cffced4da: Восстанавливает |cffffffff300|cffced4da здоровья, до |cffffffff15|cffced4da целей.|n"
            "- |cffffffff4|cffced4da: Восстанавливает |cffffffff385|cffced4da здоровья, до |cffffffff20|cffced4da целей.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт цепную волну исцеляющей энергии, восполняющую |cffffffff130|cffced4da "
                    "здоровья первой цели и переходящую максимум на |cffffffff5|cffced4da союзников. "
                    "С каждым переходом сила исцеления снижается на |cffffffff5|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт цепную волну исцеляющей энергии, восполняющую |cffffffff215|cffced4da "
                    "здоровья первой цели и переходящую максимум на |cffffffff10|cffced4da союзников. "
                    "С каждым переходом сила исцеления снижается на |cffffffff5|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт цепную волну исцеляющей энергии, восполняющую |cffffffff300|cffced4da "
                    "здоровья первой цели и переходящую максимум на |cffffffff15|cffced4da союзников. "
                    "С каждым переходом сила исцеления снижается на |cffffffff5|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Волна исцеления|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт цепную волну исцеляющей энергии, восполняющую |cffffffff385|cffced4da "
                    "здоровья первой цели и переходящую максимум на |cffffffff20|cffced4da союзников. "
                    "С каждым переходом сила исцеления снижается на |cffffffff5|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 2. A1DL - Огненная стрела (Dark Hunter W, 4 lvls)
    {
        "id": "A1DL",
        "name": "|cffe4cfa3Огненная стрела|r",
        "researchtip": "|cffe4cfa3Огненная стрела|r (|cffffffffW|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает в указанного врага огненную стрелу, которая наносит магический урон "
            "и оглушает цель. Дополнительный урон зависит от интеллекта героя.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Наносит |cffffffff150|cffced4da урона плюс |cffffffff100|cffced4da% от интеллекта; оглушает цель.|n"
            "- |cffffffff2|cffced4da: Наносит |cffffffff225|cffced4da урона плюс |cffffffff100|cffced4da% от интеллекта; оглушает цель.|n"
            "- |cffffffff3|cffced4da: Наносит |cffffffff300|cffced4da урона плюс |cffffffff100|cffced4da% от интеллекта; оглушает цель.|n"
            "- |cffffffff4|cffced4da: Наносит |cffffffff375|cffced4da урона плюс |cffffffff100|cffced4da% от интеллекта; оглушает цель.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Огненная стрела|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает огненную стрелу, наносящую цели |cffffffff150|cffced4da урона "
                    "плюс |cffffffff100|cffced4da% от интеллекта героя, и оглушающую её.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Огненная стрела|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает огненную стрелу, наносящую цели |cffffffff225|cffced4da урона "
                    "плюс |cffffffff100|cffced4da% от интеллекта героя, и оглушающую её.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Огненная стрела|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает огненную стрелу, наносящую цели |cffffffff300|cffced4da урона "
                    "плюс |cffffffff100|cffced4da% от интеллекта героя, и оглушающую её.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Огненная стрела|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает огненную стрелу, наносящую цели |cffffffff375|cffced4da урона "
                    "плюс |cffffffff100|cffced4da% от интеллекта героя, и оглушающую её.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 3. AOsw - Змеиный идол (Dark Hunter E, 4 lvls)
    {
        "id": "AOsw",
        "name": "|cffe4cfa3Змеиный идол|r",
        "researchtip": "|cffe4cfa3Змеиный идол|r (|cffffffffE|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного и невосприимчивого к магии стража-змея, "
            "атакующего наземные и воздушные цели.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Страж существует |cffffffff40|cffced4da сек.; наносит |cffffffff11-13|cffced4da урона, |cffffffff75|cffced4da здоровья.|n"
            "- |cffffffff2|cffced4da: Страж существует |cffffffff65|cffced4da сек.; наносит |cffffffff21-26|cffced4da урона, |cffffffff135|cffced4da здоровья.|n"
            "- |cffffffff3|cffced4da: Страж существует |cffffffff90|cffced4da сек.; наносит |cffffffff41-46|cffced4da урона, |cffffffff135|cffced4da здоровья.|n"
            "- |cffffffff4|cffced4da: Страж существует |cffffffff115|cffced4da сек.; наносит |cffffffff40-45|cffced4da урона, |cffffffff135|cffced4da здоровья.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Змеиный идол|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного невосприимчивого к магии стража-змея с |cffffffff75|cffced4da "
                    "ед. здоровья, наносящего |cffffffff11-13|cffced4da урона по наземным и воздушным целям. "
                    "Время действия: |cffffffff40|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Змеиный идол|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного невосприимчивого к магии стража-змея с |cffffffff135|cffced4da "
                    "ед. здоровья, наносящего |cffffffff21-26|cffced4da урона по наземным и воздушным целям. "
                    "Время действия: |cffffffff65|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Змеиный идол|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного невосприимчивого к магии стража-змея с |cffffffff135|cffced4da "
                    "ед. здоровья, наносящего |cffffffff41-46|cffced4da урона по наземным и воздушным целям. "
                    "Время действия: |cffffffff90|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Змеиный идол|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает неподвижного невосприимчивого к магии стража-змея с |cffffffff135|cffced4da "
                    "ед. здоровья, наносящего |cffffffff40-45|cffced4da урона по наземным и воздушным целям. "
                    "Время действия: |cffffffff115|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 4. AOvd - Страшное вуду (Dark Hunter R, 2 lvls)
    {
        "id": "AOvd",
        "name": "|cffe4cfa3Страшное вуду|r",
        "researchtip": "|cffe4cfa3Страшное вуду|r (|cffffffffR|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Делает всех союзных юнитов в области вокруг героя неуязвимыми к любому урону. "
            "Сам тёмный охотник остаётся уязвимым.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Время действия: |cffffffff30|cffced4da сек.|n"
            "- |cffffffff2|cffced4da: Время действия: |cffffffff45|cffced4da сек.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Страшное вуду|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует полную неуязвимость союзным юнитам вокруг героя. "
                    "Сам герой остаётся уязвимым. Время действия: |cffffffff30|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Страшное вуду|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует полную неуязвимость союзным юнитам вокруг героя. "
                    "Сам герой остаётся уязвимым. Время действия: |cffffffff45|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
                )
            }
        ]
    },

    # 5. A1DR - Яростный удар (Warlord Q, 4 lvls)
    {
        "id": "A1DR",
        "name": "|cffe4cfa3Яростный удар|r",
        "researchtip": "|cffe4cfa3Яростный удар|r (|cffffffffQ|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит мгновенный урон врагам в секторе перед героем и вызывает кровотечение, "
            "наносящее периодический урон в течение |cffffffff5|cffced4da сек.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff130|cffced4da мгновенного урона, |cffffffff10|cffced4da урона/сек. кровотечением.|n"
            "- |cffffffff2|cffced4da: |cffffffff180|cffced4da мгновенного урона, |cffffffff15|cffced4da урона/сек. кровотечением.|n"
            "- |cffffffff3|cffced4da: |cffffffff250|cffced4da мгновенного урона, |cffffffff25|cffced4da урона/сек. кровотечением.|n"
            "- |cffffffff4|cffced4da: |cffffffff350|cffced4da мгновенного урона, |cffffffff30|cffced4da урона/сек. кровотечением.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Яростный удар|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff130|cffced4da урона в секторе перед героем и вызывает у врагов кровотечение, "
                    "наносящее |cffffffff10|cffced4da урона/сек. в течение |cffffffff5|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Яростный удар|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff180|cffced4da урона в секторе перед героем и вызывает у врагов кровотечение, "
                    "наносящее |cffffffff15|cffced4da урона/сек. в течение |cffffffff5|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Яростный удар|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff250|cffced4da урона в секторе перед героем и вызывает у врагов кровотечение, "
                    "наносящее |cffffffff25|cffced4da урона/сек. в течение |cffffffff5|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Яростный удар|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff350|cffced4da урона в секторе перед героем и вызывает у врагов кровотечение, "
                    "наносящее |cffffffff30|cffced4da урона/сек. в течение |cffffffff5|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 6. A1DA - Рывок (Warlord E, 4 lvls)
    {
        "id": "A1DA",
        "name": "|cffe4cfa3Рывок|r",
        "researchtip": "|cffe4cfa3Рывок|r (|cffffffffE|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Совершает стремительный рывок в направлении взгляда героя, "
            "нанося урон всем врагам на пути.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Наносит |cffffffff50|cffced4da ед. урона.|n"
            "- |cffffffff2|cffced4da: Наносит |cffffffff100|cffced4da ед. урона.|n"
            "- |cffffffff3|cffced4da: Наносит |cffffffff150|cffced4da ед. урона.|n"
            "- |cffffffff4|cffced4da: Наносит |cffffffff200|cffced4da ед. урона.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Рывок|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Совершает стремительный рывок вперёд, "
                    "нанося |cffffffff50|cffced4da ед. урона всем врагам на своём пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Рывок|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Совершает стремительный рывок вперёд, "
                    "нанося |cffffffff100|cffced4da ед. урона всем врагам на своём пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Рывок|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Совершает стремительный рывок вперёд, "
                    "нанося |cffffffff150|cffced4da ед. урона всем врагам на своём пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Рывок|r (|cffffffffE|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Совершает стремительный рывок вперёд, "
                    "нанося |cffffffff200|cffced4da ед. урона всем врагам на своём пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 7. A1DS - Мощь тролля (Warlord W, 4 lvls)
    {
        "id": "A1DS",
        "name": "|cffe4cfa3Мощь тролля|r",
        "researchtip": "|cffe4cfa3Мощь тролля|r (|cffffffffW|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Взывает к древней силе троллей, временно многократно "
            "увеличивая скорость восстановления здоровья героя.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff100|cffced4da ед. регенерации в секунду, действует |cffffffff10|cffced4da сек.|n"
            "- |cffffffff2|cffced4da: |cffffffff150|cffced4da ед. регенерации в секунду, действует |cffffffff13|cffced4da сек.|n"
            "- |cffffffff3|cffced4da: |cffffffff200|cffced4da ед. регенерации в секунду, действует |cffffffff14|cffced4da сек.|n"
            "- |cffffffff4|cffced4da: |cffffffff250|cffced4da ед. регенерации в секунду, действует |cffffffff16|cffced4da сек.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Мощь тролля|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость регенерации здоровья героя на |cffffffff100|cffced4da ед./сек. "
                    "Время действия: |cffffffff10|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Мощь тролля|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость регенерации здоровья героя на |cffffffff150|cffced4da ед./сек. "
                    "Время действия: |cffffffff13|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Мощь тролля|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость регенерации здоровья героя на |cffffffff200|cffced4da ед./сек. "
                    "Время действия: |cffffffff14|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Мощь тролля|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость регенерации здоровья героя на |cffffffff250|cffced4da ед./сек. "
                    "Время действия: |cffffffff16|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 8. A1EB - Вихрь клинков (Warlord R, 2 lvls)
    {
        "id": "A1EB",
        "name": "|cffe4cfa3Вихрь клинков|r",
        "researchtip": "|cffe4cfa3Вихрь клинков|r (|cffffffffR|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает героя разрушительным вихрем клинков на |cffffffff8|cffced4da сек., "
            "даруя невосприимчивость к магии и нанося урон находящимся рядом наземным врагам.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Наносит |cffffffff110|cffced4da урона/сек.|n"
            "- |cffffffff2|cffced4da: Наносит |cffffffff180|cffced4da урона/сек.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Вихрь клинков|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит окружающим наземным врагам |cffffffff110|cffced4da урона/сек. "
                    "и дарует невосприимчивость к магии. Время действия: |cffffffff8|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Вихрь клинков|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит окружающим наземным врагам |cffffffff180|cffced4da урона/сек. "
                    "и дарует невосприимчивость к магии. Время действия: |cffffffff8|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
                )
            }
        ]
    },

    # 9. A1EE - Большой шакрам (Loa Priest Q, 4 lvls)
    {
        "id": "A1EE",
        "name": "|cffe4cfa3Большой шакрам|r",
        "researchtip": "|cffe4cfa3Большой шакрам|r (|cffffffffQ|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Запускает массивный вращающийся шакрам по прямой линии, "
            "наносящий урон всем врагам на своём пути.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Наносит |cffffffff100|cffced4da урона.|n"
            "- |cffffffff2|cffced4da: Наносит |cffffffff150|cffced4da урона.|n"
            "- |cffffffff3|cffced4da: Наносит |cffffffff200|cffced4da урона.|n"
            "- |cffffffff4|cffced4da: Наносит |cffffffff250|cffced4da урона.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Большой шакрам|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Запускает большой шакрам по прямой линии, "
                    "наносящий |cffffffff100|cffced4da урона всем врагам на пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Большой шакрам|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Запускает большой шакрам по прямой линии, "
                    "наносящий |cffffffff150|cffced4da урона всем врагам на пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Большой шакрам|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Запускает большой шакрам по прямой линии, "
                    "наносящий |cffffffff200|cffced4da урона всем врагам на пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Большой шакрам|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Запускает большой шакрам по прямой линии, "
                    "наносящий |cffffffff250|cffced4da урона всем врагам на пути.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 10. A1ED - Веер шакрамов (Loa Priest W, 4 lvls)
    {
        "id": "A1ED",
        "name": "|cffe4cfa3Веер шакрамов|r",
        "researchtip": "|cffe4cfa3Веер шакрамов|r (|cffffffffW|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Разбрасывает веер острых шакрамов, "
            "наносящий урон всем противникам вокруг героя.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Наносит |cffffffff100|cffced4da урона в радиусе |cffffffff400|cffced4da.|n"
            "- |cffffffff2|cffced4da: Наносит |cffffffff165|cffced4da урона в радиусе |cffffffff500|cffced4da.|n"
            "- |cffffffff3|cffced4da: Наносит |cffffffff230|cffced4da урона в радиусе |cffffffff600|cffced4da.|n"
            "- |cffffffff4|cffced4da: Наносит |cffffffff295|cffced4da урона в радиусе |cffffffff700|cffced4da.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Веер шакрамов|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер шакрамов, наносящий |cffffffff100|cffced4da урона "
                    "противникам в радиусе |cffffffff400|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Веер шакрамов|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер шакрамов, наносящий |cffffffff165|cffced4da урона "
                    "противникам в радиусе |cffffffff500|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Веер шакрамов|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер шакрамов, наносящий |cffffffff230|cffced4da урона "
                    "противникам в радиусе |cffffffff600|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Веер шакрамов|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает веер шакрамов, наносящий |cffffffff295|cffced4da урона "
                    "противникам в радиусе |cffffffff700|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 11. A1EC - Аура меткости (Loa Priest E, 4 lvls, passive)
    {
        "id": "A1EC",
        "name": "|cffe4cfa3Аура меткости|r",
        "researchtip": "|cffe4cfa3Аура меткости|r (|cffffffffE|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает силу дистанционных атак находящихся рядом союзников.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff+10|cffced4da% к урону дальнего боя.|n"
            "- |cffffffff2|cffced4da: |cffffffff+20|cffced4da% к урону дальнего боя.|n"
            "- |cffffffff3|cffced4da: |cffffffff+30|cffced4da% к урону дальнего боя.|n"
            "- |cffffffff4|cffced4da: |cffffffff+40|cffced4da% к урону дальнего боя.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Аура меткости|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон дистанционных атак союзников поблизости на |cffffffff10|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Аура меткости|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон дистанционных атак союзников поблизости на |cffffffff20|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Аура меткости|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон дистанционных атак союзников поблизости на |cffffffff30|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Аура меткости|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон дистанционных атак союзников поблизости на |cffffffff40|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 12. A1EF - Ускользание (Loa Priest R, 2 lvls, passive)
    {
        "id": "A1EF",
        "name": "|cffe4cfa3Ускользание|r",
        "researchtip": "|cffe4cfa3Ускользание|r (|cffffffffR|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует герою шанс уклониться от вражеской физической атаки.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff25|cffced4da% шанс уклонения.|n"
            "- |cffffffff2|cffced4da: |cffffffff50|cffced4da% шанс уклонения.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Ускользание|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff25|cffced4da% шанс полностью избежать урона от физической атаки.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ускользание|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт |cffffffff50|cffced4da% шанс полностью избежать урона от физической атаки.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
                )
            }
        ]
    },

    # 13. A1CE - Всплеск ярости (Loa Vessel Q, 4 lvls)
    {
        "id": "A1CE",
        "name": "|cffe4cfa3Всплеск ярости|r",
        "researchtip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой впадает в боевую ярость на |cffffffff12|cffced4da сек., "
            "значительно увеличивая скорость атаки, но получая повышенный урон.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff+170|cffced4da% к скорости атаки, |cffe69a8d+40|cffced4da% к получаемому урону.|n"
            "- |cffffffff2|cffced4da: |cffffffff+240|cffced4da% к скорости атаки, |cffe69a8d+45|cffced4da% к получаемому урону.|n"
            "- |cffffffff3|cffced4da: |cffffffff+310|cffced4da% к скорости атаки, |cffe69a8d+40|cffced4da% к получаемому урону.|n"
            "- |cffffffff4|cffced4da: |cffffffff+380|cffced4da% к скорости атаки, |cffe69a8d+35|cffced4da% к получаемому урону.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "untip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffffffff170|cffced4da%, но повышает входящий урон на |cffe69a8d40|cffced4da%. "
                    "Время действия: |cffffffff12|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "untip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffffffff240|cffced4da%, но повышает входящий урон на |cffe69a8d45|cffced4da%. "
                    "Время действия: |cffffffff12|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "untip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffffffff310|cffced4da%, но повышает входящий урон на |cffe69a8d40|cffced4da%. "
                    "Время действия: |cffffffff12|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "untip": "|cffe4cfa3Всплеск ярости|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость боя на |cffffffff380|cffced4da%, но повышает входящий урон на |cffe69a8d35|cffced4da%. "
                    "Время действия: |cffffffff12|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 14. A1CB - Неуязвимость (Loa Vessel W, 4 lvls)
    {
        "id": "A1CB",
        "name": "|cffe4cfa3Неуязвимость|r",
        "researchtip": "|cffe4cfa3Неуязвимость|r (|cffffffffW|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает с героя все отрицательные эффекты и дарует временную полную неуязвимость "
            "к урону. Автоматически срабатывает, когда здоровье героя опускается до |cffffffff400|cffced4da ед.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Время действия: |cffffffff6|cffced4da сек.|n"
            "- |cffffffff2|cffced4da: Время действия: |cffffffff7|cffced4da сек.|n"
            "- |cffffffff3|cffced4da: Время действия: |cffffffff8|cffced4da сек.|n"
            "- |cffffffff4|cffced4da: Время действия: |cffffffff9|cffced4da сек.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Неуязвимость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает отрицательные эффекты и дарует полную неуязвимость к урону "
                    "на |cffffffff6|cffced4da сек. Срабатывает автоматически при падении здоровья ниже |cffffffff400|cffced4da ед.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Неуязвимость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает отрицательные эффекты и дарует полную неуязвимость к урону "
                    "на |cffffffff7|cffced4da сек. Срабатывает автоматически при падении здоровья ниже |cffffffff400|cffced4da ед.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Неуязвимость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает отрицательные эффекты и дарует полную неуязвимость к урону "
                    "на |cffffffff8|cffced4da сек. Срабатывает автоматически при падении здоровья ниже |cffffffff400|cffced4da ед.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Неуязвимость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает отрицательные эффекты и дарует полную неуязвимость к урону "
                    "на |cffffffff9|cffced4da сек. Срабатывает автоматически при падении здоровья ниже |cffffffff400|cffced4da ед.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 15. A1CC - Рассекающий удар (Loa Vessel E, 4 lvls, passive)
    {
        "id": "A1CC",
        "name": "|cffe4cfa3Рассекающий удар|r",
        "researchtip": "|cffe4cfa3Рассекающий удар|r (|cffffffffE|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака героя наносит часть урона всем противникам по площади вокруг цели.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff10|cffced4da% урона в радиусе |cffffffff150|cffced4da.|n"
            "- |cffffffff2|cffced4da: |cffffffff15|cffced4da% урона в радиусе |cffffffff175|cffced4da.|n"
            "- |cffffffff3|cffced4da: |cffffffff20|cffced4da% урона в радиусе |cffffffff200|cffced4da.|n"
            "- |cffffffff4|cffced4da: |cffffffff25|cffced4da% урона в радиусе |cffffffff225|cffced4da.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Рассекающий удар|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff10|cffced4da% урона всем врагам в радиусе |cffffffff150|cffced4da вокруг цели.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Рассекающий удар|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff15|cffced4da% урона всем врагам в радиусе |cffffffff175|cffced4da вокруг цели.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Рассекающий удар|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff20|cffced4da% урона всем врагам в радиусе |cffffffff200|cffced4da вокруг цели.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Рассекающий удар|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки наносят |cffffffff25|cffced4da% урона всем врагам в радиусе |cffffffff225|cffced4da вокруг цели.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 16. A1CD - Воплощение Лоа (Loa Vessel R, 2 lvls)
    {
        "id": "A1CD",
        "name": "|cffe4cfa3Воплощение Лоа|r",
        "researchtip": "|cffe4cfa3Воплощение Лоа|r (|cffffffffR|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой принимает облик аватара Лоа на |cffffffff35|cffced4da сек., "
            "получая бонусы к броне, здоровью, урону и невосприимчивость к магии. Восстанавливает здоровье при превращении.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff+3|cffced4da к броне, |cffffffff+350|cffced4da к здоровью, |cffffffff+5|cffced4da к урону.|n"
            "- |cffffffff2|cffced4da: |cffffffff+5|cffced4da к броне, |cffffffff+500|cffced4da к здоровью, |cffffffff+10|cffced4da к урону.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Воплощение Лоа|r (|cffffffffR|r)",
                "untip": "|cffe4cfa3Воплощение Лоа|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff+3|cffced4da к броне, |cffffffff+350|cffced4da к здоровью, "
                    "|cffffffff+5|cffced4da к урону и невосприимчивость к магии. Время действия: |cffffffff35|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
                ),
                "unubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Находится в облике аватара Лоа.|n|n"
                    "|cffa6afb8Состояние:|cffced4da активно; повторное нажатие отменяет превращение.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Воплощение Лоа|r (|cffffffffR|r)",
                "untip": "|cffe4cfa3Воплощение Лоа|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff+5|cffced4da к броне, |cffffffff+500|cffced4da к здоровью, "
                    "|cffffffff+10|cffced4da к урону и невосприимчивость к магии. Время действия: |cffffffff35|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
                ),
                "unubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Находится в облике аватара Лоа.|n|n"
                    "|cffa6afb8Состояние:|cffced4da активно; повторное нажатие отменяет превращение.|r"
                )
            }
        ]
    },

    # 17. A1PD - Ледяной порыв (Frost Lord Q, 4 lvls)
    {
        "id": "A1PD",
        "name": "|cffe4cfa3Ледяной порыв|r",
        "researchtip": "|cffe4cfa3Ледяной порыв|r (|cffffffffQ|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяных шипов по прямой линии, подбрасывая врагов в воздух, "
            "нанося урон и оглушая их.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff150|cffced4da урона, оглушение на |cffffffff3|cffced4da сек.|n"
            "- |cffffffff2|cffced4da: |cffffffff200|cffced4da урона, оглушение на |cffffffff4|cffced4da сек.|n"
            "- |cffffffff3|cffced4da: |cffffffff250|cffced4da урона, оглушение на |cffffffff5|cffced4da сек.|n"
            "- |cffffffff4|cffced4da: |cffffffff300|cffced4da урона, оглушение на |cffffffff6|cffced4da сек.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Ледяной порыв|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff150|cffced4da урона врагам по линии удара и оглушает их "
                    "на |cffffffff3|cffced4da сек. (на героях — |cffffffff0,3|cffced4da сек.).|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяной порыв|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff200|cffced4da урона врагам по линии удара и оглушает их "
                    "на |cffffffff4|cffced4da сек. (на героях — |cffffffff0,3|cffced4da сек.).|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяной порыв|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff250|cffced4da урона врагам по линии удара и оглушает их "
                    "на |cffffffff5|cffced4da сек. (на героях — |cffffffff0,3|cffced4da сек.).|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяной порыв|r (|cffffffffQ|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff300|cffced4da урона врагам по линии удара и оглушает их "
                    "на |cffffffff6|cffced4da сек. (на героях — |cffffffff0,3|cffced4da сек.).|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 18. A1PE - Аура мороза (Frost Lord E, 4 lvls, passive)
    {
        "id": "A1PE",
        "name": "|cffe4cfa3Аура мороза|r",
        "researchtip": "|cffe4cfa3Аура мороза|r (|cffffffffE|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывающий холод вокруг героя снижает скорость передвижения "
            "и атаки окружающих врагов в радиусе |cffffffff450|cffced4da.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Замедление скорости передвижения и атаки на |cffffffff5|cffced4da%.|n"
            "- |cffffffff2|cffced4da: Замедление скорости передвижения и атаки на |cffffffff10|cffced4da%.|n"
            "- |cffffffff3|cffced4da: Замедление скорости передвижения и атаки на |cffffffff15|cffced4da%.|n"
            "- |cffffffff4|cffced4da: Замедление скорости передвижения и атаки на |cffffffff20|cffced4da%.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Аура мороза|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки и передвижения противников "
                    "в радиусе |cffffffff450|cffced4da на |cffffffff5|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Аура мороза|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки и передвижения противников "
                    "в радиусе |cffffffff450|cffced4da на |cffffffff10|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Аура мороза|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки и передвижения противников "
                    "в радиусе |cffffffff450|cffced4da на |cffffffff15|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Аура мороза|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки и передвижения противников "
                    "в радиусе |cffffffff450|cffced4da на |cffffffff20|cffced4da%.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 19. A1PF - Ледяная стойкость (Frost Lord W, 4 lvls)
    {
        "id": "A1PF",
        "name": "|cffe4cfa3Ледяная стойкость|r",
        "researchtip": "|cffe4cfa3Ледяная стойкость|r (|cffffffffW|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Временно покрывает союзных воинов в радиусе |cffffffff700|cffced4da "
            "ледяной коркой на |cffffffff20|cffced4da сек., повышая их защиту.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Повышает броню на |cffffffff4|cffced4da ед.|n"
            "- |cffffffff2|cffced4da: Повышает броню на |cffffffff6|cffced4da ед.|n"
            "- |cffffffff3|cffced4da: Повышает броню на |cffffffff8|cffced4da ед.|n"
            "- |cffffffff4|cffced4da: Повышает броню на |cffffffff10|cffced4da ед.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Ледяная стойкость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню героя и союзных воинов в радиусе |cffffffff700|cffced4da "
                    "на |cffffffff4|cffced4da ед. Время действия: |cffffffff20|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяная стойкость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню героя и союзных воинов в радиусе |cffffffff700|cffced4da "
                    "на |cffffffff6|cffced4da ед. Время действия: |cffffffff20|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяная стойкость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню героя и союзных воинов в радиусе |cffffffff700|cffced4da "
                    "на |cffffffff8|cffced4da ед. Время действия: |cffffffff20|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяная стойкость|r (|cffffffffW|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню героя и союзных воинов в радиусе |cffffffff700|cffced4da "
                    "на |cffffffff10|cffced4da ед. Время действия: |cffffffff20|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 20. A1PG - Ледяная аватара (Frost Lord R, 2 lvls)
    {
        "id": "A1PG",
        "name": "|cffe4cfa3Ледяная аватара|r",
        "researchtip": "|cffe4cfa3Ледяная аватара|r (|cffffffffR|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает героя в исполинского ледяного аватара на |cffffffff45|cffced4da сек., "
            "наделяя бонусами к защите, здоровью, урону и невосприимчивостью к магии. Восстанавливает здоровье при превращении.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: |cffffffff+5|cffced4da к броне, |cffffffff+500|cffced4da к здоровью, |cffffffff+30|cffced4da к урону.|n"
            "- |cffffffff2|cffced4da: |cffffffff+10|cffced4da к броне, |cffffffff+1000|cffced4da к здоровью, |cffffffff+60|cffced4da к урону.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Ледяная аватара|r (|cffffffffR|r)",
                "untip": "|cffe4cfa3Ледяная аватара|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует герою |cffffffff+5|cffced4da к броне, |cffffffff+500|cffced4da к здоровью, "
                    "|cffffffff+30|cffced4da к урону и невосприимчивость к магии. Время действия: |cffffffff45|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
                ),
                "unubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Находится в облике ледяного аватара.|n|n"
                    "|cffa6afb8Состояние:|cffced4da активно; повторное нажатие отменяет превращение.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяная аватара|r (|cffffffffR|r)",
                "untip": "|cffe4cfa3Ледяная аватара|r (|cffffffffR|r)",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует герою |cffffffff+10|cffced4da к броне, |cffffffff+1000|cffced4da к здоровью, "
                    "|cffffffff+60|cffced4da к урону и невосприимчивость к магии. Время действия: |cffffffff45|cffced4da сек.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
                ),
                "unubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Находится в облике ледяного аватара.|n|n"
                    "|cffa6afb8Состояние:|cffced4da активно; повторное нажатие отменяет превращение.|r"
                )
            }
        ]
    },

    # 21. A1PH - Ледяное сокрушение (Frost Lord S, 4 lvls, passive)
    {
        "id": "A1PH",
        "name": "|cffe4cfa3Ледяное сокрушение|r",
        "researchtip": "|cffe4cfa3Ледяное сокрушение|r (|cffffffffS|r)",
        "researchubertip": (
            "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При атаке дарует |cffffffff10|cffced4da% шанс сокрушить землю льдом, "
            "нанося урон всем окружающим врагам в радиусе |cffffffff300|cffced4da.|n|n"
            "|cffa6afb8Уровни:|cffced4da|n"
            "- |cffffffff1|cffced4da: Наносит |cffffffff15|cffced4da ед. урона.|n"
            "- |cffffffff2|cffced4da: Наносит |cffffffff20|cffced4da ед. урона.|n"
            "- |cffffffff3|cffced4da: Наносит |cffffffff25|cffced4da ед. урона.|n"
            "- |cffffffff4|cffced4da: Наносит |cffffffff30|cffced4da ед. урона.|r"
        ),
        "levels": [
            {
                "tip": "|cffe4cfa3Ледяное сокрушение|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10|cffced4da% шанс при атаке нанести |cffffffff15|cffced4da "
                    "ед. урона всем врагам в радиусе |cffffffff300|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяное сокрушение|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10|cffced4da% шанс при атаке нанести |cffffffff20|cffced4da "
                    "ед. урона всем врагам в радиусе |cffffffff300|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяное сокрушение|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10|cffced4da% шанс при атаке нанести |cffffffff25|cffced4da "
                    "ед. урона всем врагам в радиусе |cffffffff300|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
                )
            },
            {
                "tip": "|cffe4cfa3Ледяное сокрушение|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10|cffced4da% шанс при атаке нанести |cffffffff30|cffced4da "
                    "ед. урона всем врагам в радиусе |cffffffff300|cffced4da.|n|n"
                    "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
                )
            }
        ]
    },

    # 22. A1CA - Второе дыхание (Racial passive, 1 lvl)
    {
        "id": "A1CA",
        "name": "|cffe4cfa3Второе дыхание|r",
        "levels": [
            {
                "tip": "|cffe4cfa3Второе дыхание|r",
                "ubertip": (
                    "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Когда в бою здоровье героя падает ниже |cffffffff50|cffced4da%, его скорость "
                    "регенерации увеличивается на |cffffffff1|cffced4da ед./сек., а при падении ниже |cffffffff25|cffced4da% — "
                    "на |cffffffff3|cffced4da ед./сек.|n|n"
                    "Когда здоровье восстанавливается выше |cffffffff50|cffced4da%, дополнительная регенерация пропадает.|r"
                )
            }
        ]
    }
]


def main():
    plan_ops = []
    registry_abils = []

    for a in ABILITIES:
        aid = a["id"]
        reg_entry = {
            "id": aid,
            "name": a["name"],
            "levels_count": len(a["levels"])
        }
        plan_ops.append({
            "type": "ability",
            "id": aid,
            "field": "name",
            "value": a["name"]
        })

        if "researchtip" in a:
            reg_entry["researchtip"] = a["researchtip"]
            plan_ops.append({
                "type": "ability",
                "id": aid,
                "field": "researchtip",
                "value": a["researchtip"]
            })
        if "researchubertip" in a:
            reg_entry["researchubertip"] = a["researchubertip"]
            plan_ops.append({
                "type": "ability",
                "id": aid,
                "field": "researchubertip",
                "value": a["researchubertip"]
            })

        for i, lvl in enumerate(a["levels"], start=1):
            if "tip" in lvl:
                field_name = f"tip{i}" if len(a["levels"]) > 1 or i > 1 else "tip"
                # in FIELDS: tip -> atp1, tip2 -> atp2, etc.
                plan_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": f"tip{i}",
                    "value": lvl["tip"]
                })
            if "ubertip" in lvl:
                plan_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": f"ubertip{i}",
                    "value": lvl["ubertip"]
                })
            if "untip" in lvl:
                plan_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": f"untip{i}",
                    "value": lvl["untip"]
                })
            if "unubertip" in lvl:
                plan_ops.append({
                    "type": "ability",
                    "id": aid,
                    "field": f"unubertip{i}",
                    "value": lvl["unubertip"]
                })

        registry_abils.append(reg_entry)

    # Save registry
    registry_path = ROOT / "docs" / "ui_text" / "ice_troll_hero_abilities.json"
    registry_data = {
        "race": "IceTrolls",
        "category": "Способности и эффекты: партия 1 — способности героев",
        "scope": "Все 21 геройская способность и расовое пассивное Второе дыхание (22 объекта, 73 уровня)",
        "abilities": registry_abils,
        "evidence": [
            "war3map.w3a object data: AOhw, A1DL, AOsw, AOvd (Dark Hunter)",
            "war3map.w3a object data: A1DR, A1DA, A1DS, A1EB (Warlord)",
            "war3map.w3a object data: A1EE, A1ED, A1EC, A1EF (Loa Priest)",
            "war3map.w3a object data: A1CE, A1CB, A1CC, A1CD (Loa Vessel)",
            "war3map.w3a object data: A1PD, A1PE, A1PF, A1PG, A1PH (Frost Lord)",
            "war3map.w3a object data: A1CA (Racial hero passive)",
            "Lua trigger scripts: IceTrolls.lua (A1DA dash damage formula, A1CB invuln duration and trigger purge/heal)"
        ],
        "remaining": [
            "Партия 2: Способности войск, Лоа и призывов",
            "Партия 3: Строительные способности, ритуалы и связанные эффекты (баффы)"
        ]
    }
    registry_path.write_text(json.dumps(registry_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Save plan
    plan_path = ROOT / "docs" / "ui_text" / "ice_troll_hero_abilities_plan.json"
    plan_data = {"operations": plan_ops}
    plan_path.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Generated ice troll hero abilities registry and plan with {len(plan_ops)} operations.")


if __name__ == "__main__":
    main()
