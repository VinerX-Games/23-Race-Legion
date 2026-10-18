# -*- coding: utf-8 -*-
"""Generate complete plan and registry for Stromgard researches."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RESEARCHES = [
    # 1. Профессиональная армия
    {
        "id": "R0D5",
        "levels": 1,
        "hotkey": "Q",
        "name_template": "|cffe4cfa3Профессиональная армия|r",
        "tip_template": "|cffe4cfa3Профессиональная армия|r (|cffffffffQ|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Переводит армию королевства на регулярную основу. Увеличивает запас здоровья войск на |cffffffff20%|cffced4da, урон на |cffffffff+5|cffced4da ед. и скорость атаки на |cffffffff10%|cffced4da.|n|n"
            "Затрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deАрбалетчиков|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОхотников на троллей|cffced4da, |cffa9c7deЖрецов|cffced4da и |cffa9c7deЗаклинателей|cffced4da.|n|n"
            "|cffe69a8dВнимание:|cffced4da взаимоисключает «Призывную армию».|r"
        )
    },
    # 2. Призывная армия
    {
        "id": "R0D6",
        "levels": 1,
        "hotkey": "Q",
        "name_template": "|cffe4cfa3Призывная армия|r",
        "tip_template": "|cffe4cfa3Призывная армия|r (|cffffffffQ|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Объявляет всеобщую мобилизацию. Позволяет казармам и магическим башням обучать сразу по |cffffffff2|cffced4da воина за цикл, но снижает их запас здоровья на |cffffffff75|cffced4da ед. и урон на |cffffffff3|cffced4da ед.|n|n"
            "Затрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deАрбалетчиков|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОхотников на троллей|cffced4da, |cffa9c7deЖрецов|cffced4da и |cffa9c7deЗаклинателей|cffced4da.|n|n"
            "|cffe69a8dВнимание:|cffced4da взаимоисключает «Профессиональную армию».|r"
        )
    },
    # 3. Мечи ближнего боя (6 уровней)
    {
        "id": "R0DA",
        "levels": 6,
        "hotkey": "Q",
        "names": [
            "|cffe4cfa3Железные мечи|r — уровень |cffffffff1|r",
            "|cffe4cfa3Железные мечи|r — уровень |cffffffff2|r",
            "|cffe4cfa3Стальные мечи|r — уровень |cffffffff3|r",
            "|cffe4cfa3Стальные мечи|r — уровень |cffffffff4|r",
            "|cffe4cfa3Мифриловые мечи|r — уровень |cffffffff5|r",
            "|cffe4cfa3Мифриловые мечи|r — уровень |cffffffff6|r"
        ],
        "ubertips": [
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя на |cffffffff1|cffced4da ед.|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+2|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+3|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+4|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+5|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
        ]
    },
    # 4. Железная броня (6 уровней)
    {
        "id": "R0DC",
        "levels": 6,
        "hotkey": "A",
        "names": [
            "|cffe4cfa3Железная броня|r — уровень |cffffffff1|r",
            "|cffe4cfa3Железная броня|r — уровень |cffffffff2|r",
            "|cffe4cfa3Стальная броня|r — уровень |cffffffff3|r",
            "|cffe4cfa3Стальная броня|r — уровень |cffffffff4|r",
            "|cffe4cfa3Мифриловая броня|r — уровень |cffffffff5|r",
            "|cffe4cfa3Мифриловая броня|r — уровень |cffffffff6|r"
        ],
        "ubertips": [
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню воинов ближнего боя на |cffffffff+1|cffced4da ед.|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню воинов ближнего боя ещё на |cffffffff+1|cffced4da ед. (всего |cffffffff+2|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню воинов ближнего боя ещё на |cffffffff+1|cffced4da ед. (всего |cffffffff+3|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню воинов ближнего боя ещё на |cffffffff+1|cffced4da ед. (всего |cffffffff+4|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню воинов ближнего боя ещё на |cffffffff+1|cffced4da ед. (всего |cffffffff+5|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню воинов ближнего боя ещё на |cffffffff+1|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deЗащитников|cffced4da, |cffa9c7deРыцарей|cffced4da, |cffa9c7deОполченцев|cffced4da и |cffa9c7deПаладинов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
        ]
    },
    # 5. Черный порох (6 уровней)
    {
        "id": "R0DB",
        "levels": 6,
        "hotkey": "W",
        "names": [f"|cffe4cfa3Черный порох|r — уровень |cffffffff{i}|r" for i in range(1, 7)],
        "ubertips": [
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон стрелков и осадных орудий на |cffffffff{i}|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАрбалетчиков|cffced4da, |cffa9c7deОхотников на троллей|cffced4da, |cffa9c7deКатапульты|cffced4da и |cffa9c7deБоевые танки|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r" if i == 1 else
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон стрелков и осадных орудий ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+{i}|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАрбалетчиков|cffced4da, |cffa9c7deОхотников на троллей|cffced4da, |cffa9c7deКатапульты|cffced4da и |cffa9c7deБоевые танки|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r"
            for i in range(1, 7)
        ]
    },
    # 6. Накидки из клепаной кожи (6 уровней)
    {
        "id": "R0DE",
        "levels": 6,
        "hotkey": "S",
        "names": [f"|cffe4cfa3Клепаная кожа|r — уровень |cffffffff{i}|r" for i in range(1, 7)],
        "ubertips": [
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню стрелков и магов на |cffffffff+{i}|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАрбалетчиков|cffced4da, |cffa9c7deОхотников на троллей|cffced4da, |cffa9c7deЖрецов|cffced4da и |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r" if i == 1 else
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню стрелков и магов ещё на |cffffffff+1|cffced4da ед. (всего |cffffffff+{i}|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАрбалетчиков|cffced4da, |cffa9c7deОхотников на троллей|cffced4da, |cffa9c7deЖрецов|cffced4da и |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r"
            for i in range(1, 7)
        ]
    },
    # 7. Магическая атака (6 уровней)
    {
        "id": "R0DD",
        "levels": 6,
        "hotkey": "E",
        "names": [f"|cffe4cfa3Магическое оружие|r — уровень |cffffffff{i}|r" for i in range(1, 7)],
        "ubertips": [
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон магических атак на |cffffffff{i}|cffced4da ед.|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da и |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r" if i == 1 else
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон магических атак ещё на |cffffffff1|cffced4da ед. (всего |cffffffff+{i}|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da и |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r"
            for i in range(1, 7)
        ]
    },
    # 8. Огненные стрелы
    {
        "id": "R0E2",
        "levels": 1,
        "hotkey": "R",
        "name_template": "|cffe4cfa3Огненные стрелы|r",
        "tip_template": "|cffe4cfa3Огненные стрелы|r (|cffffffffR|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Снаряжает арбалетчиков зажигательными болтами, позволяя использовать способность «Огненные стрелы».|n|n"
            "Затрагивает: |cffa9c7deАрбалетчиков|cffced4da.|r"
        )
    },
    # 9. Защита
    {
        "id": "R0DJ",
        "levels": 1,
        "hotkey": "Z",
        "name_template": "|cffe4cfa3Защита|r",
        "tip_template": "|cffe4cfa3Защита|r (|cffffffffZ|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает пехоту правильному построению со щитами, позволяя использовать способность «Защита».|n|n"
            "Затрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da, |cffa9c7deАрбалетчиков|cffced4da.|r"
        )
    },
    # 10. Выучка рыцарей
    {
        "id": "R0DG",
        "levels": 1,
        "hotkey": "S",
        "name_template": "|cffe4cfa3Выучка рыцарей|r",
        "tip_template": "|cffe4cfa3Выучка рыцарей|r (|cffffffffS|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает боевых коней повышенной выносливости, увеличивая запас здоровья рыцарей на |cffffffff150|cffced4da ед.|n|n"
            "Затрагивает: |cffa9c7deРыцарей|cffced4da.|r"
        )
    },
    # 11. Тренировки Защитников / Специализация «Защита» (3 уровня)
    {
        "id": "R0DN",
        "levels": 3,
        "hotkeys": ["D", "D", "A"],
        "names": [
            "|cffe4cfa3Тренировки Защитников|r — уровень |cffffffff1|r",
            "|cffe4cfa3Тренировки Защитников|r — уровень |cffffffff2|r",
            "|cffe4cfa3Специализация «Защита»|r — уровень |cffffffff3|r"
        ],
        "ubertips": [
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает боевые характеристики и показатели брони тяжёлой пехоты.|n|nЗатрагивает: |cffa9c7deЗащитников|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно улучшает боевые характеристики и показатели брони тяжёлой пехоты.|n|nЗатрагивает: |cffa9c7deЗащитников|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Завершает обучение рыцарей Света защитного направления, открывая наём и совершенствуя способности Паладинов специализации «Защита».|n|nЗатрагивает: |cffa9c7deПаладинов (Защита)|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
        ]
    },
    # 12. Прочные топоры (6 уровней)
    {
        "id": "R0DL",
        "levels": 6,
        "hotkey": "Q",
        "names": [f"|cffe4cfa3Прочные топоры|r — уровень |cffffffff{i}|r" for i in range(1, 7)],
        "ubertips": [
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём переносимой работниками древесины на |cffffffff+{i * 5}|cffced4da.|n|nЗатрагивает: |cffa9c7deРаботников|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r" if i == 1 else
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём переносимой работниками древесины ещё на |cffffffff+5|cffced4da (всего |cffffffff+{i * 5}|cffced4da).|n|nЗатрагивает: |cffa9c7deРаботников|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r"
            for i in range(1, 7)
        ]
    },
    # 13. Улучшенная кладка (6 уровней)
    {
        "id": "R0DM",
        "levels": 6,
        "hotkey": "W",
        "names": [f"|cffe4cfa3Улучшенная кладка|r — уровень |cffffffff{i}|r" for i in range(1, 7)],
        "ubertips": [
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню и увеличивает запас прочности всех построек королевства.|n|nЗатрагивает: |cffa9c7deВсе здания Стромгарда|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff{i}/6|cffced4da.|r"
            for i in range(1, 7)
        ]
    },
    # 14. Зачарованные мечи
    {
        "id": "R0DH",
        "levels": 1,
        "hotkey": "A",
        "name_template": "|cffe4cfa3Зачарованные мечи|r",
        "tip_template": "|cffe4cfa3Зачарованные мечи|r (|cffffffffA|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Накладывает магические чары на клинки воинов передовой, увеличивая их урон в ближнем бою на |cffffffff10|cffced4da ед.|n|n"
            "Затрагивает: |cffa9c7deПехотинцев|cffced4da, |cffa9c7deКапитанов|cffced4da.|r"
        )
    },
    # 15. Посвящение жрецов (6 уровней)
    {
        "id": "R0DI",
        "levels": 6,
        "hotkey": "A",
        "names": [
            "|cffe4cfa3Посвящение жрецов|r — уровень |cffffffff1|r",
            "|cffe4cfa3Посвящение жрецов|r — уровень |cffffffff2|r",
            "|cffe4cfa3Мастерство жрецов|r — уровень |cffffffff3|r",
            "|cffe4cfa3Мастерство жрецов|r — уровень |cffffffff4|r",
            "|cffe4cfa3Высшее мастерство жрецов|r — уровень |cffffffff5|r",
            "|cffe4cfa3Высшее мастерство жрецов|r — уровень |cffffffff6|r"
        ],
        "ubertips": [
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья жрецов на |cffffffff40|cffced4da ед., запас маны на |cffffffff100|cffced4da ед., ускоряет регенерацию маны и обучает заклинанию «Рассеивание заклинаний».|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас здоровья и маны жрецов, а также ускоряет её регенерацию.|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья жрецов ещё на |cffffffff60|cffced4da ед., запас маны на |cffffffff100|cffced4da ед., ускоряет регенерацию маны и обучает заклинанию «Внутренний огонь».|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас здоровья и маны жрецов, а также ускоряет её регенерацию.|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас здоровья и маны жрецов, а также ускоряет её регенерацию.|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Доводит магические способности жрецов до совершенства, максимально увеличивая здоровье, запас и регенерацию маны.|n|nЗатрагивает: |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
        ]
    },
    # 16. Посвящение заклинателей (6 уровней)
    {
        "id": "R0DK",
        "levels": 6,
        "hotkey": "S",
        "names": [
            "|cffe4cfa3Посвящение заклинателей|r — уровень |cffffffff1|r",
            "|cffe4cfa3Посвящение заклинателей|r — уровень |cffffffff2|r",
            "|cffe4cfa3Мастерство заклинателей|r — уровень |cffffffff3|r",
            "|cffe4cfa3Мастерство заклинателей|r — уровень |cffffffff4|r",
            "|cffe4cfa3Высшее мастерство заклинателей|r — уровень |cffffffff5|r",
            "|cffe4cfa3Высшее мастерство заклинателей|r — уровень |cffffffff6|r"
        ],
        "ubertips": [
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья заклинателей на |cffffffff40|cffced4da ед., запас маны на |cffffffff100|cffced4da ед., ускоряет регенерацию маны и обучает заклинанию «Огненная стрела».|n|nЗатрагивает: |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас здоровья и маны заклинателей, а также ускоряет её регенерацию.|n|nЗатрагивает: |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья заклинателей ещё на |cffffffff60|cffced4da ед., запас маны на |cffffffff100|cffced4da ед., ускоряет регенерацию маны и обучает заклинанию «Разъедающий огонь».|n|nЗатрагивает: |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас здоровья и маны заклинателей, а также ускоряет её регенерацию.|n|nЗатрагивает: |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает запас здоровья и маны заклинателей, а также ускоряет её регенерацию.|n|nЗатрагивает: |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Доводит магические способности заклинателей до совершенства, максимально увеличивая здоровье, запас и регенерацию маны, и обучая заклинанию «Проклятие».|n|nЗатрагивает: |cffa9c7deЗаклинателей|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
        ]
    },
    # 17. Шрапнель
    {
        "id": "R0H1",
        "levels": 1,
        "hotkey": "E",
        "name_template": "|cffe4cfa3Шрапнель|r",
        "tip_template": "|cffe4cfa3Шрапнель|r (|cffffffffE|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Снаряжает охотников на троллей осколочными боеприпасами, увеличивая их урон по небронированным целям и целям со средней бронёй.|n|n"
            "Затрагивает: |cffa9c7deОхотников на троллей|cffced4da.|r"
        )
    },
    # 18. Длинноствольные мушкеты
    {
        "id": "R0H2",
        "levels": 1,
        "hotkey": "X",
        "name_template": "|cffe4cfa3Длинноствольные мушкеты|r",
        "tip_template": "|cffe4cfa3Длинноствольные мушкеты|r (|cffffffffX|r)",
        "ubertip_template": (
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Удлиняет стволы стрелкового оружия, увеличивая дальность атаки стрелков на |cffffffff100|cffced4da.|n|n"
            "Затрагивает: |cffa9c7deАрбалетчиков|cffced4da, |cffa9c7deОхотников на троллей|cffced4da.|r"
        )
    },
    # 19. Специализация «Свет» (3 уровня)
    {
        "id": "R0DO",
        "levels": 3,
        "hotkey": "S",
        "names": [
            "|cffe4cfa3Специализация «Свет»|r — уровень |cffffffff1|r",
            "|cffe4cfa3Специализация «Свет»|r — уровень |cffffffff2|r",
            "|cffe4cfa3Специализация «Свет»|r — уровень |cffffffff3|r"
        ],
        "ubertips": [
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает паладинов путям священного Света, открывая наём и совершенствуя целительные способности паладинов и жрецов.|n|nЗатрагивает: |cffa9c7deПаладинов (Свет)|cffced4da, |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает священную ауру и запас маны паладинов Света и жрецов.|n|nЗатрагивает: |cffa9c7deПаладинов (Свет)|cffced4da, |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Доводит мастерство исцеления паладинов Света до совершенства, максимально увеличивая исцеление и запас здоровья.|n|nЗатрагивает: |cffa9c7deПаладинов (Свет)|cffced4da, |cffa9c7deЖрецов|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
        ]
    },
    # 20. Специализация «Возмездие» (3 уровня)
    {
        "id": "R0DP",
        "levels": 3,
        "hotkey": "R",
        "names": [
            "|cffe4cfa3Специализация «Возмездие»|r — уровень |cffffffff1|r",
            "|cffe4cfa3Специализация «Возмездие»|r — уровень |cffffffff2|r",
            "|cffe4cfa3Специализация «Возмездие»|r — уровень |cffffffff3|r"
        ],
        "ubertips": [
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает паладинов путям священного Возмездия, открывая наём и усиливая боевой урон и карающие заклинания паладинов.|n|nЗатрагивает: |cffa9c7deПаладинов (Возмездие)|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает командирскую ауру и боевой урон паладинов Возмездия.|n|nЗатрагивает: |cffa9c7deПаладинов (Возмездие)|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r",
            "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Доводит мастерство Возмездия паладинов до совершенства, максимально увеличивая боевую мощь и силу освящённого оружия.|n|nЗатрагивает: |cffa9c7deПаладинов (Возмездие)|cffced4da.|n|n|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
        ]
    }
]

def main():
    operations = []
    registry = {
        "race": "Стромгард",
        "category": "Исследования",
        "researches_count": len(RESEARCHES),
        "researches": {}
    }

    for res in RESEARCHES:
        rid = res["id"]
        levels = res["levels"]
        reg_entry = {"levels": levels, "levels_data": {}}

        if levels == 1:
            name_val = res["name_template"]
            tip_val = res["tip_template"]
            ub_val = res["ubertip_template"]
            operations.append({"type": "upgrade", "id": rid, "field": "name1", "value": name_val})
            operations.append({"type": "upgrade", "id": rid, "field": "tip1", "value": tip_val})
            operations.append({"type": "upgrade", "id": rid, "field": "ubertip1", "value": ub_val})
            reg_entry["levels_data"]["1"] = {"name": name_val, "tip": tip_val, "ubertip": ub_val}
        else:
            names = res["names"]
            ubertips = res["ubertips"]
            hotkeys = res.get("hotkeys")
            hotkey = res.get("hotkey", "")
            for i in range(1, levels + 1):
                hk = hotkeys[i - 1] if hotkeys else hotkey
                name_val = names[i - 1]
                tip_val = f"{name_val} (|cffffffff{hk}|r)" if hk else name_val
                ub_val = ubertips[i - 1]
                operations.append({"type": "upgrade", "id": rid, "field": f"name{i}", "value": name_val})
                operations.append({"type": "upgrade", "id": rid, "field": f"tip{i}", "value": tip_val})
                operations.append({"type": "upgrade", "id": rid, "field": f"ubertip{i}", "value": ub_val})
                reg_entry["levels_data"][str(i)] = {"name": name_val, "tip": tip_val, "ubertip": ub_val}

        registry["researches"][rid] = reg_entry

    plan_file = ROOT / "docs/ui_text/stromgard_research_plan.json"
    registry_file = ROOT / "docs/ui_text/stromgard_research.json"

    with open(plan_file, "w", encoding="utf-8") as f:
        json.dump({"operations": operations}, f, ensure_ascii=False, indent=2)

    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(operations)} operations across {len(RESEARCHES)} researches ({sum(r['levels'] for r in RESEARCHES)} total levels).")
    print(f"Saved plan to {plan_file}")
    print(f"Saved registry to {registry_file}")

if __name__ == "__main__":
    main()
