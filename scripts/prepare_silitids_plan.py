# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Silitids race (Race 22)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. RACE SELECTION: A0J7, R0BV
    # =========================================================================
    # A0J7
    wts_updates[38883] = "|cffe4cfa3Аз'Акиры|r"
    wts_updates[38884] = "|cffe4cfa3Аз'Акиры|r (|cffffffffS|r)"
    wts_updates[36636] = (
        "|cffa6afb8РАСА:|cffced4da Древняя насекомоподобная цивилизация служителей Древних Богов, повелевающая роем силитидов, армиями киражей и нечестивыми мутациями.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«World of Warcraft: Vanilla»|r|n|n"
        "|cffced4daАз'Акиры — древняя раса инсектоидов, порождённая Древними Богами на заре времён Калимдора. В бескрайних пустынях Силитуса и цитадели Анкиража их владыки направляют бесконечный рой: личинки непрерывно мутируют в специализированных воинов, летающих ос, бронированных танков и гигантских анубисатов, сокрушающих врагов во славу К'Туна.|r"
    )
    checks_def.append({"type": "ability", "id": "A0J7", "field": "name", "expected": wts_updates[38883]})
    checks_def.append({"type": "ability", "id": "A0J7", "field": "tip1", "expected": wts_updates[38884]})
    checks_def.append({"type": "ability", "id": "A0J7", "field": "ubertip1", "expected": wts_updates[36636]})

    # Marker: R0BV
    wts_updates[30499] = "|cffe4cfa3Силитиды и Аз'Акиры|r"
    wts_updates[30500] = "|cffe4cfa3Силитиды и Аз'Акиры|r"
    wts_updates[30501] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к империи Аз'Акиров и рою Силитидов.|r"
    checks_def.append({"type": "upgrade", "id": "R0BV", "field": "name1", "expected": wts_updates[30499]})
    checks_def.append({"type": "upgrade", "id": "R0BV", "field": "tip1", "expected": wts_updates[30500]})
    checks_def.append({"type": "upgrade", "id": "R0BV", "field": "ubertip1", "expected": wts_updates[30501]})

    # =========================================================================
    # 2. BUILDINGS (16 buildings/structures)
    # =========================================================================
    # e01H: Улей (Q)
    wts_updates[12707] = "|cffe4cfa3Улей|r"
    wts_updates[13685] = "|cffe4cfa3Улей|r (|cffffffffQ|r)"
    wts_updates[9657] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание первой ступени. Обеспечивает запас пищи и производит личинок роя.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМать роя|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗащитная оболочка зданий|cffced4da|n- |cffa9c7deПосвящение матерей|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deМегаулей|cffced4da: открывает доступ к передовым мутациям и сооружениям.|r"
    )
    checks_def.append({"type": "unit", "id": "e01H", "field": "name", "expected": wts_updates[12707]})
    checks_def.append({"type": "unit", "id": "e01H", "field": "tip", "expected": wts_updates[13685]})
    checks_def.append({"type": "unit", "id": "e01H", "field": "ubertip", "expected": wts_updates[9657]})

    # e021: Мегаулей (Z)
    wts_updates[13693] = "|cffe4cfa3Мегаулей|r"
    wts_updates[13694] = "|cffe4cfa3Мегаулей|r (|cffffffffZ|r)"
    wts_updates[9719] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание второй ступени. Существенно увеличивает запас пищи.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМать роя|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗащитная оболочка зданий|cffced4da|n- |cffa9c7deПосвящение матерей|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deСверхулей|cffced4da: открывает высшие технологии и силу Древних Богов.|r"
    )
    checks_def.append({"type": "unit", "id": "e021", "field": "name", "expected": wts_updates[13693]})
    checks_def.append({"type": "unit", "id": "e021", "field": "tip", "expected": wts_updates[13694]})
    checks_def.append({"type": "unit", "id": "e021", "field": "ubertip", "expected": wts_updates[9719]})

    # e020: Сверхулей (Z)
    wts_updates[13129] = "|cffe4cfa3Сверхулей|r"
    wts_updates[13458] = "|cffe4cfa3Сверхулей|r (|cffffffffZ|r)"
    wts_updates[9708] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Высшее главное здание третьей ступени. Обеспечивает максимальный запас пищи роя.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМать роя|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗащитная оболочка зданий|cffced4da|n- |cffa9c7deПосвящение матерей|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "e020", "field": "name", "expected": wts_updates[13129]})
    checks_def.append({"type": "unit", "id": "e020", "field": "tip", "expected": wts_updates[13458]})
    checks_def.append({"type": "unit", "id": "e020", "field": "ubertip", "expected": wts_updates[9708]})

    # e01I: Личинка (Q)
    wts_updates[12719] = "|cffe4cfa3Личинка|r"
    wts_updates[12723] = "|cffe4cfa3Личинка|r (|cffffffffQ|r)"
    checks_def.append({"type": "unit", "id": "e01I", "field": "name", "expected": wts_updates[12719]})
    checks_def.append({"type": "unit", "id": "e01I", "field": "tip", "expected": wts_updates[12723]})

    # e01J: Кокон (A)
    wts_updates[12727] = "|cffe4cfa3Кокон|r"
    wts_updates[13686] = "|cffe4cfa3Кокон|r (|cffffffffA|r)"
    checks_def.append({"type": "unit", "id": "e01J", "field": "name", "expected": wts_updates[12727]})
    checks_def.append({"type": "unit", "id": "e01J", "field": "tip", "expected": wts_updates[13686]})

    # e01K: Эволюционный бассейн (W)
    wts_updates[12735] = "|cffe4cfa3Эволюционный бассейн|r"
    wts_updates[13687] = "|cffe4cfa3Эволюционный бассейн|r (|cffffffffW|r)"
    wts_updates[9658] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр генетических модификаций роя. Исследует улучшения атаки, защиты, скорости и особые ветви эволюции силитидов.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКогти|cffced4da|n- |cffa9c7deДальнобойные атаки|cffced4da|n- |cffa9c7deПанцирь|cffced4da|n- |cffa9c7deВыживаемость|cffced4da|n- |cffa9c7deЯрость|cffced4da|n- |cffa9c7deПовышенный метаболизм|cffced4da|n- Ветви эволюции: |cffa9c7deПлодовитость|cffced4da, |cffa9c7deСилитиды-танки|cffced4da, |cffa9c7deПлодовитость (Осы)|cffced4da, |cffa9c7deУсиленные крылья|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "e01K", "field": "name", "expected": wts_updates[12735]})
    checks_def.append({"type": "unit", "id": "e01K", "field": "tip", "expected": wts_updates[13687]})
    checks_def.append({"type": "unit", "id": "e01K", "field": "ubertip", "expected": wts_updates[9658]})

    # e01L: Колония (Z)
    wts_updates[12741] = "|cffe4cfa3Колония|r"
    wts_updates[13688] = "|cffe4cfa3Колония|r (|cffffffffZ|r)"
    wts_updates[9660] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение и склад древесины. Атакует наземные цели.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенная добыча|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "e01L", "field": "name", "expected": wts_updates[12741]})
    checks_def.append({"type": "unit", "id": "e01L", "field": "tip", "expected": wts_updates[13688]})
    checks_def.append({"type": "unit", "id": "e01L", "field": "ubertip", "expected": wts_updates[9660]})

    # e01M: Логово членистоногих (E)
    wts_updates[13689] = "|cffe4cfa3Логово членистоногих|r"
    wts_updates[13690] = "|cffe4cfa3Логово членистоногих|r (|cffffffffE|r)"
    wts_updates[9661] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Передовая мутационная лаборатория. Открывает и развивает высшие боевые свойства пауков-стражей и слизней.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЭволюция «Делимость»|cffced4da|n- |cffa9c7deЭволюция «Вязкая слизь»|cffced4da|n- |cffa9c7deЭволюция «Паразит»|cffced4da|n- |cffa9c7deЭволюция «Кислотный снаряд»|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "e01M", "field": "name", "expected": wts_updates[13689]})
    checks_def.append({"type": "unit", "id": "e01M", "field": "tip", "expected": wts_updates[13690]})
    checks_def.append({"type": "unit", "id": "e01M", "field": "ubertip", "expected": wts_updates[9661]})

    # e01X: Антенны (F)
    wts_updates[9944] = "|cffe4cfa3Антенны|r"
    wts_updates[10613] = "|cffe4cfa3Антенны|r (|cffffffffF|r)"
    wts_updates[9707] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Органическая биовышка роя. Увеличивает скорость передвижения союзников на |cffc8e087+7%|cffced4da и ускоряет регенерацию их здоровья в радиусе |cffffffff600|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "e01X", "field": "name", "expected": wts_updates[9944]})
    checks_def.append({"type": "unit", "id": "e01X", "field": "tip", "expected": wts_updates[10613]})
    checks_def.append({"type": "unit", "id": "e01X", "field": "ubertip", "expected": wts_updates[9707]})

    # e00B: Антенны (спелл, F)
    wts_updates[12820] = "|cffe4cfa3Антенны|r"
    wts_updates[12821] = "|cffe4cfa3Антенны|r (|cffffffffF|r)"
    wts_updates[10614] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Органическая биовышка роя. Увеличивает скорость передвижения союзников на |cffc8e087+7%|cffced4da и ускоряет регенерацию их здоровья в радиусе |cffffffff600|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "e00B", "field": "name", "expected": wts_updates[12820]})
    checks_def.append({"type": "unit", "id": "e00B", "field": "tip", "expected": wts_updates[12821]})
    checks_def.append({"type": "unit", "id": "e00B", "field": "ubertip", "expected": wts_updates[10614]})

    # h00C: Алтарь Песков (S)
    wts_updates[12809] = "|cffe4cfa3Алтарь Песков|r"
    wts_updates[12812] = "|cffe4cfa3Алтарь Песков|r (|cffffffffS|r)"
    wts_updates[9699] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священный алтарь, где подготавливаются и воскрешаются герои Киражей.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deПророк|cffced4da: маг дальнего боя с уроном по области.|n- |cffa9c7deГенерал Киражей|cffced4da: могучий воин-полководец ближнего боя.|n- |cffa9c7deКоролева|cffced4da: владычица роя с исцелением и аурой поддержки.|r"
    )
    checks_def.append({"type": "unit", "id": "h00C", "field": "name", "expected": wts_updates[12809]})
    checks_def.append({"type": "unit", "id": "h00C", "field": "tip", "expected": wts_updates[12812]})
    checks_def.append({"type": "unit", "id": "h00C", "field": "ubertip", "expected": wts_updates[9699]})

    # o015: Храм Аз'Акиров (D)
    wts_updates[12801] = "|cffe4cfa3Храм Аз'Акиров|r"
    wts_updates[12803] = "|cffe4cfa3Храм Аз'Акиров|r (|cffffffffD|r)"
    wts_updates[9676] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Культовое сооружение империи Аз'Акиров. Пробуждает древних обсидиановых исполинов и чудовищных сфинксов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОбсидиановая статуя|cffced4da|n- |cffa9c7deСфинкс|cffced4da|n- |cffa9c7deАнубисат|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКаменная оболочка|cffced4da|n- |cffa9c7deПрочность|cffced4da|n- |cffa9c7deАтака анубисатов|cffced4da|n- |cffa9c7deСокрушение|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o015", "field": "name", "expected": wts_updates[12801]})
    checks_def.append({"type": "unit", "id": "o015", "field": "tip", "expected": wts_updates[12803]})
    checks_def.append({"type": "unit", "id": "o015", "field": "ubertip", "expected": wts_updates[9676]})

    # o017: Обелиск Аз'Акиров (R)
    wts_updates[13691] = "|cffe4cfa3Обелиск Аз'Акиров|r"
    wts_updates[13692] = "|cffe4cfa3Обелиск Аз'Акиров|r (|cffffffffR|r)"
    wts_updates[9704] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обелиск тёмной магии, концентрирующий энергию древних владык Киражей.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПосвящение пророков|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "o017", "field": "name", "expected": wts_updates[13691]})
    checks_def.append({"type": "unit", "id": "o017", "field": "tip", "expected": wts_updates[13692]})
    checks_def.append({"type": "unit", "id": "o017", "field": "ubertip", "expected": wts_updates[9704]})

    # h08L: Храм Анкиража (Столица)
    wts_updates[30037] = "|cffe4cfa3Храм Анкиража|r"
    checks_def.append({"type": "unit", "id": "h08L", "field": "name", "expected": wts_updates[30037]})

    # h0MG: Стать слугой К'Туна (X)
    wts_updates[39424] = "|cffe4cfa3Стать слугой К'Туна|r"
    wts_updates[19427] = "|cffe4cfa3Стать слугой К'Туна|r (|cffffffffX|r)"
    wts_updates[19428] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Ритуал присяги Древнему Богу. Передаёт К'Туна под ваш контроль и перемещает столицу в священный центр Анкиража.|r"
    )
    checks_def.append({"type": "unit", "id": "h0MG", "field": "name", "expected": wts_updates[39424]})
    checks_def.append({"type": "unit", "id": "h0MG", "field": "tip", "expected": wts_updates[19427]})
    checks_def.append({"type": "unit", "id": "h0MG", "field": "ubertip", "expected": wts_updates[19428]})

    # h0DL: Паутина
    wts_updates[12455] = "|cffe4cfa3Паутина|r"
    checks_def.append({"type": "unit", "id": "h0DL", "field": "name", "expected": wts_updates[12455]})

    # =========================================================================
    # 3. UNITS (16 units)
    # =========================================================================
    # e01G: Трутень (Q)
    wts_updates[12699] = "|cffe4cfa3Трутень|r"
    wts_updates[13623] = "|cffe4cfa3Трутень|r (|cffffffffQ|r)"
    wts_updates[35286] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий силитидов. Добывает ресурсы и возводит органические строения роя.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткую дистанцию.|n"
        "- |cffa9c7deЧасть поколения|cffced4da: снижает затраты на содержание рабочего.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01G", "field": "name", "expected": wts_updates[12699]})
    checks_def.append({"type": "unit", "id": "e01G", "field": "tip", "expected": wts_updates[13623]})
    checks_def.append({"type": "unit", "id": "e01G", "field": "ubertip", "expected": wts_updates[35286]})

    # e01N: Анубисат (E)
    wts_updates[12746] = "|cffe4cfa3Анубисат|r"
    wts_updates[12748] = "|cffe4cfa3Анубисат|r (|cffffffffE|r)"
    wts_updates[14796] = (
        "|cffa6afb8ЮНИТ:|cffced4da Колоссальный обсидиановый страж, обладающий огромным запасом здоровья и сокрушительным ударом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСокрушение|cffced4da: шанс нанести урон по области при атаке.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01N", "field": "name", "expected": wts_updates[12746]})
    checks_def.append({"type": "unit", "id": "e01N", "field": "tip", "expected": wts_updates[12748]})
    checks_def.append({"type": "unit", "id": "e01N", "field": "ubertip", "expected": wts_updates[14796]})

    # e01O: Солдат Киражей (D)
    wts_updates[12750] = "|cffe4cfa3Солдат Киражей|r"
    wts_updates[13624] = "|cffe4cfa3Солдат Киражей|r (|cffffffffD|r)"
    wts_updates[14797] = (
        "|cffa6afb8ЮНИТ:|cffced4da Выносливый боец ближнего боя, составляющий основу штурмовых легионов Киражей.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01O", "field": "name", "expected": wts_updates[12750]})
    checks_def.append({"type": "unit", "id": "e01O", "field": "tip", "expected": wts_updates[13624]})
    checks_def.append({"type": "unit", "id": "e01O", "field": "ubertip", "expected": wts_updates[14797]})

    # e01P: Силитид-танк (W)
    wts_updates[12758] = "|cffe4cfa3Силитид-танк|r"
    wts_updates[9830] = "|cffe4cfa3Силитид-танк|r (|cffffffffW|r)"
    wts_updates[31653] = (
        "|cffa6afb8ЮНИТ:|cffced4da Сверхтяжелый бронированный инсектоид, поглощающий огромное количество урона и сокрушающий вражеский авангард.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01P", "field": "name", "expected": wts_updates[12758]})
    checks_def.append({"type": "unit", "id": "e01P", "field": "tip", "expected": wts_updates[9830]})
    checks_def.append({"type": "unit", "id": "e01P", "field": "ubertip", "expected": wts_updates[31653]})

    # e01Q: Силитид-оса (E)
    wts_updates[12768] = "|cffe4cfa3Силитид-оса|r"
    wts_updates[13626] = "|cffe4cfa3Силитид-оса|r (|cffffffffE|r)"
    wts_updates[31654] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стремительный летающий хищник с высокой скоростью атаки и ядовитым жалом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯдовитое жало|cffced4da: отравляет цель, нанося периодический урон.|n"
        "- |cffa9c7deБешенство|cffced4da: временно увеличивает скорость атаки и перемещения (требуется эволюция).|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01Q", "field": "name", "expected": wts_updates[12768]})
    checks_def.append({"type": "unit", "id": "e01Q", "field": "tip", "expected": wts_updates[13626]})
    checks_def.append({"type": "unit", "id": "e01Q", "field": "ubertip", "expected": wts_updates[31654]})

    # e01R: Мать роя (R)
    wts_updates[12774] = "|cffe4cfa3Мать роя|r"
    wts_updates[13627] = "|cffe4cfa3Мать роя|r (|cffffffffR|r)"
    wts_updates[31759] = (
        "|cffa6afb8ЮНИТ:|cffced4da Ключевой маг поддержки роя. Порождает личинки, исцеляет союзников и усиливает армию священной аурой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСоздать личинку|cffced4da: порождает новые личинки для мутации.|n"
        "- |cffa9c7deВолна исцеления|cffced4da: восстанавливает здоровье цепочке раненых союзников.|n"
        "- |cffa9c7deАура Матери Роя|cffced4da: повышает скорость передвижения и атаки союзников на |cffc8e087+9%|cffced4da.|n"
        "- |cffa9c7deСон|cffced4da: усыпляет вражескую цель.|n"
        "- |cffa9c7deСигнал рою|cffced4da: приказывает рою атаковать выбранную точку.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01R", "field": "name", "expected": wts_updates[12774]})
    checks_def.append({"type": "unit", "id": "e01R", "field": "tip", "expected": wts_updates[13627]})
    checks_def.append({"type": "unit", "id": "e01R", "field": "ubertip", "expected": wts_updates[31759]})

    # e01S: Скарабей (S)
    wts_updates[12779] = "|cffe4cfa3Скарабей|r"
    wts_updates[13628] = "|cffe4cfa3Скарабей|r (|cffffffffS|r)"
    wts_updates[31760] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый осадный инсектоид с каменным панцирем, эффективно разрушающий вражеские укрепления.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКаменная кожа|cffced4da: поглощает часть входящего физического урона.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01S", "field": "name", "expected": wts_updates[12779]})
    checks_def.append({"type": "unit", "id": "e01S", "field": "tip", "expected": wts_updates[13628]})
    checks_def.append({"type": "unit", "id": "e01S", "field": "ubertip", "expected": wts_updates[31760]})

    # e01T: Пророк Киражей (F)
    wts_updates[12785] = "|cffe4cfa3Пророк Киражей|r"
    wts_updates[13629] = "|cffe4cfa3Пророк Киражей|r (|cffffffffF|r)"
    wts_updates[31761] = (
        "|cffa6afb8ЮНИТ:|cffced4da Верховный чародей Киражей, владеющий магией тёмных москитов и аурой ускорения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМоскиты|cffced4da: призывает рой, атакующий врагов и исцеляющий мага.|n"
        "- |cffa9c7deВолшебный огонь|cffced4da: снижает броню цели и раскрывает её местоположение.|n"
        "- |cffa9c7deЭмпатия|cffced4da: связывает союзников, распределяя входящий урон.|n"
        "- |cffa9c7deАура Пророка|cffced4da: повышает скорость атаки и перемещения союзников на |cffc8e087+7%|cffced4da.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01T", "field": "name", "expected": wts_updates[12785]})
    checks_def.append({"type": "unit", "id": "e01T", "field": "tip", "expected": wts_updates[13629]})
    checks_def.append({"type": "unit", "id": "e01T", "field": "ubertip", "expected": wts_updates[31761]})

    # e01U: Паук-страж (A)
    wts_updates[12794] = "|cffe4cfa3Паук-страж|r"
    wts_updates[13630] = "|cffe4cfa3Паук-страж|r (|cffffffffA|r)"
    wts_updates[31762] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тактический боец поддержки. Создаёт зоны паутины, заражает врагов паразитами и ведёт огонь кислотой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПаутина|cffced4da: создаёт паутину, ускоряющую силитидов на |cffc8e087+15%|cffced4da.|n"
        "- |cffa9c7deПаразит|cffced4da: заражает цель, порождая паучка после её гибели (требуется эволюция).|n"
        "- |cffa9c7deКислотный снаряд|cffced4da: снижает броню и наносит урон по области (требуется эволюция).|n"
        "- |cffa9c7deЛогово паучков|cffced4da: возводит временное логово паучков.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01U", "field": "name", "expected": wts_updates[12794]})
    checks_def.append({"type": "unit", "id": "e01U", "field": "tip", "expected": wts_updates[13630]})
    checks_def.append({"type": "unit", "id": "e01U", "field": "ubertip", "expected": wts_updates[31762]})

    # e01V: Командир Киражей (Z)
    wts_updates[12815] = "|cffe4cfa3Командир Киражей|r"
    wts_updates[13632] = "|cffe4cfa3Командир Киражей|r (|cffffffffZ|r)"
    wts_updates[42392] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый военачальник роя. Увеличивает мощь союзных воинов дисциплинирующей аурой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДисциплина|cffced4da: увеличивает урон окружающих органических союзников на |cffc8e087+10%|cffced4da.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01V", "field": "name", "expected": wts_updates[12815]})
    checks_def.append({"type": "unit", "id": "e01V", "field": "tip", "expected": wts_updates[13632]})
    checks_def.append({"type": "unit", "id": "e01V", "field": "ubertip", "expected": wts_updates[42392]})

    # e01Y: Паучок (A)
    wts_updates[12822] = "|cffe4cfa3Паучок|r"
    wts_updates[12823] = "|cffe4cfa3Паучок|r"
    wts_updates[12826] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мелкий агрессивный арахнид, порождённый паразитом из тела павшего врага.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01Y", "field": "name", "expected": wts_updates[12822]})
    checks_def.append({"type": "unit", "id": "e01Y", "field": "tip", "expected": wts_updates[12823]})
    checks_def.append({"type": "unit", "id": "e01Y", "field": "ubertip", "expected": wts_updates[12826]})

    # e01Z: Слизень (R)
    wts_updates[12827] = "|cffe4cfa3Слизень|r"
    wts_updates[13633] = "|cffe4cfa3Слизень|r (|cffffffffR|r)"
    wts_updates[42393] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стрелок дальнего боя, поражающий врагов сгустками едкой биомассы.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДелимость|cffced4da: после гибели распадается на двух малых слизней (требуется эволюция).|n`"
        "- |cffa9c7deВязкая слизь|cffced4da: замедляет атакованных врагов на |cffe69a8d4%|cffced4da за удар (требуется эволюция).|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01Z", "field": "name", "expected": wts_updates[12827]})
    checks_def.append({"type": "unit", "id": "e01Z", "field": "tip", "expected": wts_updates[13633]})
    checks_def.append({"type": "unit", "id": "e01Z", "field": "ubertip", "expected": wts_updates[42393]})

    # e023: Малый слизень (R)
    wts_updates[13614] = "|cffe4cfa3Малый слизень|r"
    wts_updates[13621] = "|cffe4cfa3Малый слизень|r"
    wts_updates[36843] = (
        "|cffa6afb8ЮНИТ:|cffced4da Отколовшаяся часть крупного слизня, продолжающая вести огонь на дальней дистанции.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e023", "field": "name", "expected": wts_updates[13614]})
    checks_def.append({"type": "unit", "id": "e023", "field": "tip", "expected": wts_updates[13621]})
    checks_def.append({"type": "unit", "id": "e023", "field": "ubertip", "expected": wts_updates[36843]})

    # e02W: Силитид-воин (W)
    wts_updates[18452] = "|cffe4cfa3Силитид-воин|r"
    wts_updates[18453] = "|cffe4cfa3Силитид-воин|r (|cffffffffW|r)"
    wts_updates[42394] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый лёгкий боец роя. Быстро выращивается из личинок в больших количествах.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЧасть поколения|cffced4da: снижает затраты на содержание бойца.|n"
        "- |cffa9c7deПлодовитость|cffced4da: появление трёх воинов из одной личинки (требуется эволюция).|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e02W", "field": "name", "expected": wts_updates[18452]})
    checks_def.append({"type": "unit", "id": "e02W", "field": "tip", "expected": wts_updates[18453]})
    checks_def.append({"type": "unit", "id": "e02W", "field": "ubertip", "expected": wts_updates[42394]})

    # u020: Обсидиановая статуя (Q)
    wts_updates[3042] = "|cffe4cfa3Обсидиановая статуя|r"
    wts_updates[3043] = "|cffe4cfa3Обсидиановая статуя|r (|cffffffffQ|r)"
    wts_updates[31763] = (
        "|cffa6afb8ЮНИТ:|cffced4da Магическое сооружение поддержки, невосприимчивое к заклинаниям. Восстанавливает здоровье и ману окружающим войскам.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЧумная эссенция|cffced4da: восстанавливает здоровье союзникам поблизости.|n"
        "- |cffa9c7deПризрачное касание|cffced4da: восстанавливает ману союзникам поблизости.|n"
        "- |cffa9c7deНевосприимчивость к магии|cffced4da: защищает от любых заклинаний.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u020", "field": "name", "expected": wts_updates[3042]})
    checks_def.append({"type": "unit", "id": "u020", "field": "tip", "expected": wts_updates[3043]})
    checks_def.append({"type": "unit", "id": "u020", "field": "ubertip", "expected": wts_updates[31763]})

    # u022: Сфинкс (W)
    wts_updates[12806] = "|cffe4cfa3Сфинкс|r"
    wts_updates[13631] = "|cffe4cfa3Сфинкс|r (|cffffffffW|r)"
    wts_updates[31764] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могущественный парящий разрушитель, поглощающий магию и наносящий тяжёлый урон по площади.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПожирание магии|cffced4da: рассеивает чары в области, исцеляя сфинкса и нанося урон призывам.|n"
        "- |cffa9c7deСфера разрушения|cffced4da: увеличивает урон атак и наносит урон по области.|n"
        "- |cffa9c7deПоглощение маны|cffced4da: забирает ману у союзного воина для питания своих сфер.|n"
        "- |cffa9c7deНевосприимчивость к магии|cffced4da: иммунитет к вражеским чарам.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "u022", "field": "name", "expected": wts_updates[12806]})
    checks_def.append({"type": "unit", "id": "u022", "field": "tip", "expected": wts_updates[13631]})
    checks_def.append({"type": "unit", "id": "u022", "field": "ubertip", "expected": wts_updates[31764]})

    # =========================================================================
    # 4. HEROES (6 heroes)
    # =========================================================================
    # U023: Пророк (C)
    wts_updates[230] = "|cffe4cfa3Пророк|r"
    wts_updates[10798] = "Гор'аман,Скеррам"
    wts_updates[12362] = "|cffe4cfa3Пророк|r (|cffffffffC|r)"
    wts_updates[11289] = "|cffe4cfa3Пророк|r"
    wts_updates[12363] = "|cffe4cfa3Пророк|r"
    wts_updates[19311] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Верховный жрец Древних Богов, специализирующийся на контроле поля боя, призыве щупалец и тёмной магии стаи.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПорождение щупальца|cffced4da: призывает щупальца бездны, атакующие врагов.|n"
        "- |cffa9c7deПронзание|cffced4da: подземные шипы подбрасывают и оглушают наземные цели на линии.|n"
        "- |cffa9c7deТёмная стая|cffced4da: выпускает конус нетопырей, наносящих урон врагам.|n"
        "- |cffa9c7deПризыв Силитидов-Танков|cffced4da: призывает на помощь свирепых Силитидов-танков.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U023", "field": "name", "expected": wts_updates[230]})
    checks_def.append({"type": "unit", "id": "U023", "field": "tip", "expected": wts_updates[12362]})
    checks_def.append({"type": "unit", "id": "U023", "field": "ubertip", "expected": wts_updates[19311]})

    # U024: Генерал Киражей (Z)
    wts_updates[659] = "|cffe4cfa3Генерал Киражей|r"
    wts_updates[12364] = "Раджакс,Ссинкрикс,Кву'рик"
    wts_updates[662] = "|cffe4cfa3Генерал Киражей|r (|cffffffffZ|r)"
    wts_updates[660] = "|cffe4cfa3Генерал Киражей|r"
    wts_updates[665] = "|cffe4cfa3Генерал Киражей|r"
    wts_updates[13888] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могучий полководец ближнего боя, ведущий легионы Киражей. Отражает атаки шипастым панцирем и сокрушает врагов раскатами грома.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРаскат грома|cffced4da: удар по земле наносит урон и замедляет врагов поблизости.|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: повышает броню и отражает часть урона ближнего боя.|n"
        "- |cffa9c7deАура шипов|cffced4da: наделяет окружающих союзников щитом, отражающим урон ближнего боя.|n"
        "- |cffa9c7deРой саранчи|cffced4da: призывает рой кровожадных насекомых, исцеляющих генерала.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U024", "field": "name", "expected": wts_updates[659]})
    checks_def.append({"type": "unit", "id": "U024", "field": "tip", "expected": wts_updates[662]})
    checks_def.append({"type": "unit", "id": "U024", "field": "ubertip", "expected": wts_updates[13888]})

    # U025: Королева (X)
    wts_updates[666] = "|cffe4cfa3Королева|r"
    wts_updates[12964] = "Аямисси,Ксааршедж,Лапресс"
    wts_updates[680] = "|cffe4cfa3Королева|r (|cffffffffX|r)"
    wts_updates[679] = "|cffe4cfa3Королева|r"
    wts_updates[681] = "|cffe4cfa3Королева|r"
    wts_updates[19828] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Быстрая владычица роя. Поддерживает войско исцеляющими волнами, нечистой аурой скорости и выводит врагов из боя сглазом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолна исцеления|cffced4da: восстанавливает здоровье цепочке раненых союзников.|n"
        "- |cffa9c7deСглаз|cffced4da: временно превращает врага в беззащитное существо.|n"
        "- |cffa9c7deНечистая аура|cffced4da: увеличивает скорость передвижения и регенерацию здоровья союзников.|n"
        "- |cffa9c7deУмиротворение|cffced4da: мощный целительный поток, восстанавливающий здоровье всем союзникам в области.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U025", "field": "name", "expected": wts_updates[666]})
    checks_def.append({"type": "unit", "id": "U025", "field": "tip", "expected": wts_updates[680]})
    checks_def.append({"type": "unit", "id": "U025", "field": "ubertip", "expected": wts_updates[19828]})

    # U02A: Пророк Секарим (C)
    wts_updates[12773] = "|cffe4cfa3Пророк Секарим|r"
    wts_updates[15672] = "Секарим"
    wts_updates[17002] = "|cffe4cfa3Пророк Секарим|r (|cffffffffC|r)"
    wts_updates[17001] = "|cffe4cfa3Пророк Секарим|r"
    wts_updates[17003] = "|cffe4cfa3Пророк Секарим|r"
    wts_updates[17004] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Мифический глашатай бездны. Ослабляет врагов разрушительным проклятием и призывает подземные шипы роя.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПроклятие|cffced4da: окружает цель разрушительным полем бездны, наносящим урон окружающим.|n"
        "- |cffa9c7deПронзание|cffced4da: подземные шипы оглушают наземные цели на линии.|n"
        "- |cffa9c7deТёмная стая|cffced4da: стая нетопырей поражает врагов перед магом.|n"
        "- |cffa9c7deПризыв Силитидов-Танков|cffced4da: призывает на помощь тяжелых бронированных танков.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U02A", "field": "name", "expected": wts_updates[12773]})
    checks_def.append({"type": "unit", "id": "U02A", "field": "tip", "expected": wts_updates[17002]})
    checks_def.append({"type": "unit", "id": "U02A", "field": "ubertip", "expected": wts_updates[17004]})

    # U02R: Император-близнец Век'нилаш (Z)
    wts_updates[16077] = "|cffe4cfa3Император-близнец Век'нилаш|r"
    wts_updates[28925] = "Век'нилаш"
    wts_updates[28927] = "|cffe4cfa3Император-близнец Век'нилаш|r (|cffffffffZ|r)"
    wts_updates[28926] = "|cffe4cfa3Император-близнец Век'нилаш|r"
    wts_updates[28929] = "|cffe4cfa3Император-близнец Век'нилаш|r"
    wts_updates[28928] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный владыка империи Аз'Акиров. Обладает сокрушительной физической силой, яростью в бою и неразрывной связью со своим братом-магом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЯрость|cffced4da: существенно ускоряет атаку и перемещение императора.|n"
        "- |cffa9c7deМощь Акиров|cffced4da: ослабляет броню врагов вокруг героя.|n"
        "- |cffa9c7deДвойная телепортация|cffced4da: мгновенно меняется местами с братом и восстанавливает здоровье.|n"
        "- |cffa9c7deСоздание Логова|cffced4da: возводит особое логово, порождающее Силитидов-танков.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U02R", "field": "name", "expected": wts_updates[16077]})
    checks_def.append({"type": "unit", "id": "U02R", "field": "tip", "expected": wts_updates[28927]})
    checks_def.append({"type": "unit", "id": "U02R", "field": "ubertip", "expected": wts_updates[28928]})

    # U02S: Император-близнец Век'лор (Z)
    wts_updates[28935] = "|cffe4cfa3Император-близнец Век'лор|r"
    wts_updates[28936] = "Век'лор"
    wts_updates[28938] = "|cffe4cfa3Император-близнец Век'лор|r (|cffffffffZ|r)"
    wts_updates[28937] = "|cffe4cfa3Император-близнец Век'лор|r"
    wts_updates[28941] = "|cffe4cfa3Император-близнец Век'лор|r"
    wts_updates[28940] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный владыка-чародей империи Аз'Акиров. Повелевает древней магией тьмы, передаёт жизненную силу и возводит усиливающие антенны роя.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДревняя магия|cffced4da: обрушивает на область волны тьмы с периодическим уроном.|n"
        "- |cffa9c7deПередача Жизни|cffced4da: отдаёт запас здоровья союзнику в обмен на ману.|n"
        "- |cffa9c7deДвойная телепортация|cffced4da: меняется местами с братом и восстанавливает здоровье.|n"
        "- |cffa9c7deСоздание Антенн|cffced4da: возводит полевую антенну усиления роя.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "U02S", "field": "name", "expected": wts_updates[28935]})
    checks_def.append({"type": "unit", "id": "U02S", "field": "tip", "expected": wts_updates[28938]})
    checks_def.append({"type": "unit", "id": "U02S", "field": "ubertip", "expected": wts_updates[28940]})

    # =========================================================================
    # 5. UPGRADES (23 upgrades)
    # =========================================================================
    # R08G: Защитная оболочка зданий (уровни 1..6, X)
    r08g_names = [37251, 37240, 37241, 37242, 37243, 37244]
    r08g_tips = [37245, 37246, 37247, 37248, 37249, 37250]
    r08g_ubs = [12494, 12495, 12496, 12497, 12498, 12499]
    for lvl in range(1, 7):
        wts_updates[r08g_names[lvl - 1]] = f"|cffe4cfa3Защитная оболочка зданий — уровень {lvl}|r"
        wts_updates[r08g_tips[lvl - 1]] = f"|cffe4cfa3Защитная оболочка зданий — уровень {lvl}|r (|cffffffffX|r)"
        wts_updates[r08g_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню всех зданий Силитидов на |cffc8e087+2|cffced4da.|n|n"
            f"|cffa6afb8Применяется ко:|cffced4da всем зданиям.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R08G", "field": "name1", "expected": wts_updates[r08g_names[0]]})
    checks_def.append({"type": "upgrade", "id": "R08G", "field": "tip1", "expected": wts_updates[r08g_tips[0]]})
    checks_def.append({"type": "upgrade", "id": "R08G", "field": "ubertip1", "expected": wts_updates[r08g_ubs[0]]})

    # R088: Посвящение матерей (уровни 1..6, E)
    r088_names = [37210, 37205, 37206, 37207, 37208, 37209]
    r088_tips = [37211, 37212, 37213, 37214, 37215, 37216]
    r088_ubs = [37204, 37217, 37218, 37219, 37220, 37221]
    for lvl in range(1, 7):
        wts_updates[r088_names[lvl - 1]] = f"|cffe4cfa3Посвящение матерей — уровень {lvl}|r"
        wts_updates[r088_tips[lvl - 1]] = f"|cffe4cfa3Посвящение матерей — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[r088_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья на |cffc8e087+100|cffced4da, запас маны на |cffc8e087+100|cffced4da и ускоряет регенерацию маны Матерей роя.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМать роя|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R088", "field": "name1", "expected": wts_updates[r088_names[0]]})

    # R089: Эволюция «Плодовитость» (lvl 1)
    wts_updates[37222] = "|cffe4cfa3Эволюция «Плодовитость»|r"
    wts_updates[37223] = "|cffe4cfa3Эволюция «Плодовитость»|r"
    wts_updates[28348] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Из каждой личинки появляется сразу |cffffffff3|cffced4da Силитида-воина вместо 2, повышается их здоровье и скорость.|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Силитиды-танки» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСилитид-воин|cffced4da.|r"
    )

    # R08B: Эволюция «Плодовитость (Осы)» (lvl 1, D)
    wts_updates[37227] = "|cffe4cfa3Эволюция «Плодовитость (Осы)»|r"
    wts_updates[37228] = "|cffe4cfa3Эволюция «Плодовитость (Осы)»|r (|cffffffffD|r)"
    wts_updates[12435] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Из одной личинки появляется сразу |cffffffff2|cffced4da Силитида-осы.|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Усиленные крылья» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСилитид-оса|cffced4da.|r"
    )

    # R085: Эволюция «Силитиды-танки» (lvl 1, R)
    wts_updates[28344] = "|cffe4cfa3Эволюция «Силитиды-танки»|r"
    wts_updates[28345] = "|cffe4cfa3Эволюция «Силитиды-танки»|r (|cffffffffR|r)"
    wts_updates[28347] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает мутацию личинок в тяжелых Силитидов-танков.|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Плодовитость» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛичинка|cffced4da.|r"
    )

    # R08A: Эволюция «Усиленные крылья» (lvl 1, F)
    wts_updates[37224] = "|cffe4cfa3Эволюция «Усиленные крылья»|r"
    wts_updates[37225] = "|cffe4cfa3Эволюция «Усиленные крылья»|r (|cffffffffF|r)"
    wts_updates[37226] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает скорость перемещения Силитидов-ос и наделяет их способностью «Бешенство».|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Плодовитость (Осы)» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСилитид-оса|cffced4da.|r"
    )

    # R083: Ярость (уровни 1..6, X)
    r083_names = [37161, 37167, 37168, 37169, 37170, 37171]
    r083_tips = [37162, 37163, 37164, 37165, 37166, 16442]
    r083_ubs = [6738, 6999, 7007, 7009, 7090, 11365]
    for lvl in range(1, 7):
        wts_updates[r083_names[lvl - 1]] = f"|cffe4cfa3Ярость — уровень {lvl}|r"
        wts_updates[r083_tips[lvl - 1]] = f"|cffe4cfa3Ярость — уровень {lvl}|r (|cffffffffX|r)"
        wts_updates[r083_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость атаки всех органических войск роя на |cffc8e087+3%|cffced4da.|n|n"
            f"|cffa6afb8Применяется ко:|cffced4da всем органическим воинам.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R084: Повышенный метаболизм (уровни 1..6, Z)
    r084_names = [37172, 37174, 37175, 37176, 37177, 37178]
    r084_tips = [37173, 37179, 37180, 37181, 37182, 37183]
    r084_ubs = [22283, 22284, 22285, 22286, 22287, 22288]
    for lvl in range(1, 7):
        wts_updates[r084_names[lvl - 1]] = f"|cffe4cfa3Повышенный метаболизм — уровень {lvl}|r"
        wts_updates[r084_tips[lvl - 1]] = f"|cffe4cfa3Повышенный метаболизм — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[r084_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость перемещения всех органических войск роя на |cffc8e087+4%|cffced4da.|n|n"
            f"|cffa6afb8Применяется ко:|cffced4da всем органическим воинам.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R07Z: Выживаемость (уровни 1..6, S)
    r07z_names = [37124, 37119, 37120, 37121, 37122, 37123]
    r07z_tips = [37125, 37126, 37127, 37128, 37129, 37130]
    r07z_ubs = [33709, 33710, 33711, 33712, 33713, 33714]
    for lvl in range(1, 7):
        wts_updates[r07z_names[lvl - 1]] = f"|cffe4cfa3Выживаемость — уровень {lvl}|r"
        wts_updates[r07z_tips[lvl - 1]] = f"|cffe4cfa3Выживаемость — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r07z_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас здоровья всех органических войск роя на |cffc8e087+7%|cffced4da.|n|n"
            f"|cffa6afb8Применяется ко:|cffced4da всем органическим воинам.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R07Y: Панцирь (уровни 1..6, A)
    r07y_names = [37112, 37107, 37108, 37109, 37110, 37111]
    r07y_tips = [37113, 37114, 37115, 37116, 37117, 37118]
    r07y_ubs = [11796, 11797, 11798, 11799, 11800, 11801]
    for lvl in range(1, 7):
        wts_updates[r07y_names[lvl - 1]] = f"|cffe4cfa3Панцирь — уровень {lvl}|r"
        wts_updates[r07y_tips[lvl - 1]] = f"|cffe4cfa3Панцирь — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r07y_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает броню всех воинов роя на |cffc8e087+1,5|cffced4da.|n|n"
            f"|cffa6afb8Применяется ко:|cffced4da всем воинам Силитидов.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R009: Когти (уровни 1..6, Q)
    r009_names = [36862, 36951, 36969, 36973, 36981, 37069]
    r009_tips = [37079, 37084, 37091, 37092, 37093, 37094]
    r009_ubs = [5322, 11732, 11733, 11734, 11735, 11736]
    for lvl in range(1, 7):
        wts_updates[r009_names[lvl - 1]] = f"|cffe4cfa3Когти — уровень {lvl}|r"
        wts_updates[r009_tips[lvl - 1]] = f"|cffe4cfa3Когти — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r009_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов ближнего боя.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСилитид-воин|cffced4da|n- |cffa9c7deСилитид-оса|cffced4da|n- |cffa9c7deСкарабей|cffced4da|n- |cffa9c7deСолдат Киражей|cffced4da|n- |cffa9c7deПаук-страж|cffced4da|n- |cffa9c7deКомандир Киражей|cffced4da|n- |cffa9c7deСилитид-танк|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R07X: Дальнобойные атаки (уровни 1..6, W)
    r07x_names = [37095, 37096, 37097, 37098, 37099, 37100]
    r07x_tips = [37101, 37102, 37103, 37104, 37105, 37106]
    r07x_ubs = [11744, 11757, 11758, 11759, 11760, 11761]
    for lvl in range(1, 7):
        wts_updates[r07x_names[lvl - 1]] = f"|cffe4cfa3Дальнобойные атаки — уровень {lvl}|r"
        wts_updates[r07x_tips[lvl - 1]] = f"|cffe4cfa3Дальнобойные атаки — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[r07x_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон стрелков дальнего боя.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСлизень|cffced4da|n- |cffa9c7deМалый слизень|cffced4da|n- |cffa9c7deМать роя|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R0D0: Улучшенная добыча (уровни 1..5, Z)
    r0d0_names = [12977, 13609, 15711, 15712, 15846]
    r0d0_tips = [15013, 15014, 15713, 15714, 15849]
    r0d0_ubs = [20802, 21361, 21372]
    for lvl in range(1, 6):
        wts_updates[r0d0_names[lvl - 1]] = f"|cffe4cfa3Улучшенная добыча — уровень {lvl}|r"
        wts_updates[r0d0_tips[lvl - 1]] = f"|cffe4cfa3Улучшенная добыча — уровень {lvl}|r (|cffffffffZ|r)"
    for idx, sid in enumerate(r0d0_ubs):
        lvl = idx + 3
        wts_updates[sid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой трутнями древесины на |cffc8e087+10|cffced4da.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deТрутень|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/5|cffced4da.|r"
        )

    # R08C: Эволюция «Делимость» (lvl 1, S)
    wts_updates[37229] = "|cffe4cfa3Эволюция «Делимость»|r"
    wts_updates[37230] = "|cffe4cfa3Эволюция «Делимость»|r (|cffffffffS|r)"
    wts_updates[37231] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Слизни после гибели распадаются на двух Малых слизней.|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Вязкая слизь» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСлизень|cffced4da.|r"
    )

    # R08D: Эволюция «Вязкая слизь» (lvl 1, A)
    wts_updates[37232] = "|cffe4cfa3Эволюция «Вязкая слизь»|r"
    wts_updates[37233] = "|cffe4cfa3Эволюция «Вязкая слизь»|r (|cffffffffA|r)"
    wts_updates[37234] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Атаки Слизней замедляют передвижение цели на |cffe69a8d4%|cffced4da за удар (эффект суммируется).|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Делимость» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСлизень|cffced4da.|r"
    )

    # R08F: Эволюция «Паразит» (lvl 1, Q)
    wts_updates[37238] = "|cffe4cfa3Эволюция «Паразит»|r"
    wts_updates[37239] = "|cffe4cfa3Эволюция «Паразит»|r (|cffffffffQ|r)"
    wts_updates[12451] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Пауки-стражи обучаются внедрять во врагов паразитов, наносящих урон и порождающих паучков.|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Кислотный снаряд» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПаук-страж|cffced4da.|r"
    )

    # R08E: Эволюция «Кислотный снаряд» (lvl 1, W)
    wts_updates[38479] = "|cffe4cfa3Эволюция «Кислотный снаряд»|r"
    wts_updates[38480] = "|cffe4cfa3Эволюция «Кислотный снаряд»|r (|cffffffffW|r)"
    wts_updates[38481] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Пауки-стражи обучаются метать кислотные снаряды, наносящие урон по области и снижающие броню на |cffe69a8d3|cffced4da.|n|n"
        "|cffe6c07bВзаимоисключение: исследование «Паразит» станет недоступно.|r|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПаук-страж|cffced4da.|r"
    )

    # R086: Сокрушение (lvl 1, C)
    wts_updates[12205] = "|cffe4cfa3Сокрушение|r (|cffffffffC|r)"
    wts_updates[12404] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Анубисатов шансом |cffffffff20%|cffced4da нанести сокрушительный удар по области вокруг цели.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАнубисат|cffced4da.|r"
    )

    # R080: Каменная оболочка (уровни 1..6, A)
    r080_names = [37142, 37131, 37132, 37133, 37134, 37135]
    r080_tips = [37136, 37137, 37138, 37139, 37140, 37141]
    r080_ubs = [18419, 18420, 18421, 18422, 18423, 18424]
    for lvl in range(1, 7):
        wts_updates[r080_names[lvl - 1]] = f"|cffe4cfa3Каменная оболочка — уровень {lvl}|r"
        wts_updates[r080_tips[lvl - 1]] = f"|cffe4cfa3Каменная оболочка — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[r080_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню Обсидиановых статуй и Сфинксов на |cffc8e087+{lvl}|cffced4da.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОбсидиановая статуя|cffced4da|n- |cffa9c7deСфинкс|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R081: Атака анубисатов (уровни 1..6, D)
    r081_names = [37144, 37145, 37146, 37147, 37148, 37149]
    r081_tips = [37150, 37151, 37152, 37153, 37154, 37155]
    r081_ubs = [37143, 37156, 37157, 37158, 37159, 37160]
    for lvl in range(1, 7):
        wts_updates[r081_names[lvl - 1]] = f"|cffe4cfa3Атака анубисатов — уровень {lvl}|r"
        wts_updates[r081_tips[lvl - 1]] = f"|cffe4cfa3Атака анубисатов — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[r081_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон атак Анубисатов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deАнубисат|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R082: Прочность (уровни 1..6, S)
    r082_names = [11917, 11912, 11913, 11914, 11915, 11916]
    r082_tips = [11918, 11919, 11920, 11921, 11922, 11923]
    r082_ubs = [11924, 11925, 11926, 11927, 11928, 11929]
    for lvl in range(1, 7):
        wts_updates[r082_names[lvl - 1]] = f"|cffe4cfa3Прочность — уровень {lvl}|r"
        wts_updates[r082_tips[lvl - 1]] = f"|cffe4cfa3Прочность — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[r082_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья Обсидиановых статуй и Сфинксов на |cffc8e087+4%|cffced4da.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deОбсидиановая статуя|cffced4da|n- |cffa9c7deСфинкс|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # R087: Посвящение пророков (уровни 1..6, Q)
    r087_names = [37192, 37187, 37188, 37189, 37190, 37191]
    r087_tips = [37193, 37194, 37195, 37196, 37197, 37198]
    r087_ubs = [37186, 37199, 37200, 37201, 37202, 37203]
    for lvl in range(1, 7):
        wts_updates[r087_names[lvl - 1]] = f"|cffe4cfa3Посвящение пророков — уровень {lvl}|r"
        wts_updates[r087_tips[lvl - 1]] = f"|cffe4cfa3Посвящение пророков — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[r087_ubs[lvl - 1]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья, маны и ускоряет регенерацию маны Пророков Киражей.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПророк Киражей|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )

    # =========================================================================
    # 6. ABILITIES
    # =========================================================================
    # A1B7: Стать Слугой К'Туна (X)
    wts_updates[7232] = "|cffe4cfa3Стать слугой К'Туна|r"
    wts_updates[6794] = "|cffe4cfa3Стать слугой К'Туна|r (|cffffffffX|r)"
    wts_updates[30493] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Приносит клятву верности Древнему Богу К'Туну, передавая его под ваш контроль и перемещая столицу в Анкираж.|r"
    )

    # A1B8: Око К'Туна (E)
    wts_updates[30495] = "|cffe4cfa3Око К'Туна|r"
    wts_updates[30496] = "|cffe4cfa3Око К'Туна|r (|cffffffffE|r)"
    wts_updates[30497] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает всевидящее Око К'Туна в указанную точку карты на |cffffffff20|cffced4da мин.|r"
    )

    # A0T1: Выбрать личинки (Q - Улей)
    wts_updates[9171] = "|cffe4cfa3Выбрать личинки|r"
    wts_updates[12737] = "|cffe4cfa3Выбрать личинки|r (|cffffffffQ|r)"
    wts_updates[9172] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выделяет всех свободных личинок в радиусе действия Улья.|r"
    )

    # A0SW: Выбрать личинки (Q - Мать роя)
    wts_updates[1149] = "|cffe4cfa3Выбрать личинки|r"
    wts_updates[2765] = "|cffe4cfa3Выбрать личинки|r (|cffffffffQ|r)"
    wts_updates[4272] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выделяет всех свободных личинок вокруг Матери роя.|r"
    )

    # A0ML: Выпустить силитида-воина (Q - Кокон)
    wts_updates[682] = "|cffe4cfa3Выпустить силитида-воина|r"
    wts_updates[684] = "|cffe4cfa3Выпустить силитида-воина|r (|cffffffffQ|r)"
    wts_updates[726] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Разрушает кокон, немедленно освобождая Силитида-воина.|r"
    )

    # A0J0: Аура Антенн
    wts_updates[39514] = "|cffe4cfa3Аура Антенн|r"
    wts_updates[39515] = "|cffe4cfa3Аура Антенн|r"
    wts_updates[12888] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения союзников на |cffc8e087+7%|cffced4da и ускоряет регенерацию их здоровья в радиусе |cffffffff600|cffced4da.|r"
    )

    # A0KP: Скорость на паутине
    wts_updates[12465] = "|cffe4cfa3Скорость на паутине|r"

    # A0VH: Часть поколения
    wts_updates[39545] = "|cffe4cfa3Часть поколения|r"
    wts_updates[39543] = "|cffe4cfa3Часть поколения (Половина)|r"
    wts_updates[39544] = "|cffe4cfa3Часть поколения (Треть)|r"
    wts_updates[4168] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Юнит расходует только |cffffffff50%|cffced4da от стандартного лимита пищи.|r"
    wts_updates[4279] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Юнит расходует только |cffffffff33%|cffced4da от стандартного лимита пищи.|r"

    # A1KD: Бешенство (Q)
    wts_updates[39555] = "|cffe4cfa3Бешенство|r"
    wts_updates[39556] = "|cffe4cfa3Бешенство|r (|cffffffffQ|r)"
    wts_updates[37268] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки осы на |cffc8e087+20%|cffced4da и скорость передвижения на |cffc8e087+15%|cffced4da на |cffffffff9|cffced4da сек.|r"
    )

    # A0SX: Сигнал рою (F)
    wts_updates[9176] = "|cffe4cfa3Сигнал рою|r"
    wts_updates[30490] = "|cffe4cfa3Сигнал рою|r (|cffffffffF|r)"
    wts_updates[30491] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает всех воинов роя первой ступени в области атаковать указанную точку.|r"
    )

    # A0KR: Сон (R)
    wts_updates[11856] = "|cffe4cfa3Сон|r (|cffffffffR|r)"

    # A0KQ: Волна исцеления (E)
    wts_updates[39521] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[39520] = "|cffe4cfa3Волна исцеления|r (|cffffffffE|r)"

    # A0ZU: Создать личинку (W)
    wts_updates[39548] = "|cffe4cfa3Создать личинку|r"
    wts_updates[39549] = "|cffe4cfa3Создать личинку|r (|cffffffffW|r)"
    wts_updates[30610] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мать роя откладывает яйцо, из которого появляется новая личинка силитидов.|r"
    )

    # A0IW: Аура Матери Роя
    wts_updates[35320] = "|cffe4cfa3Аура Матери Роя|r"
    wts_updates[36650] = "|cffe4cfa3Аура Матери Роя|r"
    wts_updates[22230] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения и атаки союзников в радиусе действия на |cffc8e087+9%|cffced4da.|r"
    )

    # A0JG: Москиты (W)
    wts_updates[12098] = "|cffe4cfa3Москиты|r"
    wts_updates[12099] = "|cffe4cfa3Москиты|r (|cffffffffW|r)"
    wts_updates[12097] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает рой москитов, атакующих врагов вокруг и исцеляющих мага на величину нанесённого урона.|r"
    )

    # A0IY: Эмпатия (E)
    wts_updates[39511] = "|cffe4cfa3Эмпатия|r"
    wts_updates[7205] = "|cffe4cfa3Эмпатия|r (|cffffffffE|r)"

    # A0JF: Аура Пророка
    wts_updates[39517] = "|cffe4cfa3Аура Пророка|r"
    wts_updates[39518] = "|cffe4cfa3Аура Пророка|r"
    wts_updates[12887] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения и атаки окружающих войск Киражей на |cffc8e087+7%|cffced4da.|r"
    )

    # A0KO: Паутина (Q)
    wts_updates[26823] = "|cffe4cfa3Паутина|r"
    wts_updates[26824] = "|cffe4cfa3Паутина|r (|cffffffffQ|r)"
    wts_updates[12474] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Плетёт на земле обширную паутину, ускоряющую передвижение союзных войск на |cffc8e087+15%|cffced4da. Время действия: |cffffffff5|cffced4da мин.|r"
    )

    # A0IZ: Паразит (W)
    wts_updates[39512] = "|cffe4cfa3Паразит|r"
    wts_updates[39513] = "|cffe4cfa3Паразит|r (|cffffffffW|r)"
    wts_updates[26788] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заражает врага паразитом, наносящим |cffffffff4|cffced4da ед. урона/сек. в течение |cffffffff35|cffced4da сек. При гибели жертвы из неё вылупляется Паучок.|r"
    )

    # A1KF: Кислотный снаряд (W)
    wts_updates[27254] = "|cffe4cfa3Кислотный снаряд|r"
    wts_updates[27447] = "|cffe4cfa3Кислотный снаряд|r (|cffffffffW|r)"
    wts_updates[27448] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает в цель снаряд с кислотой, снижающий броню на |cffe69a8d3|cffced4da и наносящий |cffffffff5|cffced4da ед. урона/сек. основной цели в течение |cffffffff15|cffced4da сек.|r"
    )

    # A1KG: Логово паучков (E)
    wts_updates[38210] = "|cffe4cfa3Логово паучков|r"
    wts_updates[38475] = "|cffe4cfa3Логово паучков|r (|cffffffffE|r)"
    wts_updates[38476] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт органическое гнездо, периодически порождающее Паучков на поле боя.|r"
    )

    # A1KE: Дисциплина
    wts_updates[27245] = "|cffe4cfa3Дисциплина|r"
    wts_updates[27246] = "|cffe4cfa3Дисциплина|r"
    wts_updates[27251] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура военачальника увеличивает урон окружающих органических союзников на |cffc8e087+10%|cffced4da.|r"
    )

    # A0KN: Вязкая слизь
    wts_updates[12458] = "|cffe4cfa3Вязкая слизь|r"
    wts_updates[11991] = "|cffe4cfa3Вязкая слизь|r"
    wts_updates[11541] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака слизня замедляет передвижение цели на |cffe69a8d4%|cffced4da. Эффект суммируется.|r"
    )

    # A0KM: Породить малого слизня
    wts_updates[39519] = "|cffe4cfa3Породить малого слизня|r"

    # A1R4: Пожирание магии (Q)
    wts_updates[42396] = "|cffe4cfa3Пожирание магии|r"
    wts_updates[42397] = "|cffe4cfa3Пожирание магии|r (|cffffffffQ|r)"

    # A0J2: Порождение щупальца (Q)
    wts_updates[23371] = "|cffe4cfa3Порождение щупальца|r"
    wts_updates[23026] = "|cffe4cfa3Порождение щупальца|r"
    wts_updates[7761] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из-под земли щупальца бездны, атакующие врагов.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff1|cffced4da щупальце.|n"
        "|cffa6afb82-й уровень:|r |cffffffff2|cffced4da щупальца.|n"
        "|cffa6afb83-й уровень:|r |cffffffff3|cffced4da щупальца.|n"
        "|cffa6afb84-й уровень:|r |cffffffff4|cffced4da щупальца.|r"
    )
    a0j2_tips = [23370, 22148, 22149, 22372]
    a0j2_ubs = [15031, 30476, 30477, 30478]
    for lvl in range(1, 5):
        wts_updates[a0j2_tips[lvl - 1]] = f"|cffe4cfa3Порождение щупальца — уровень {lvl}|r (|cffffffffQ|r)"
        cnt_str = f"{lvl} щупальце" if lvl == 1 else f"{lvl} щупальца"
        wts_updates[a0j2_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из-под земли |cffffffff{cnt_str}|cffced4da бездны, атакующие врагов в области.|r"
        )

    # A0SU: Пронзание (W, lvl 4)
    wts_updates[18439] = "|cffe4cfa3Пронзание — уровень 4|r (|cffffffffW|r)"
    wts_updates[18440] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из-под земли шипы, наносящие урон наземным врагам на прямой линии, подбрасывая и оглушая их.|r"
    )

    # A0SV: Темная стая (E, lvl 4)
    wts_updates[12016] = "|cffe4cfa3Тёмная стая — уровень 4|r (|cffffffffE|r)"
    wts_updates[12028] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает в секторе перед собой стаю нетопырей, наносящих урон врагам на своём пути.|r"
    )

    # A0J1: Призыв Силитидов-Танков (R)
    wts_updates[19977] = "|cffe4cfa3Призыв Силитидов-Танков|r"
    wts_updates[11939] = "|cffe4cfa3Призыв Силитидов-Танков|r"
    wts_updates[11938] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь пророку тяжелых Силитидов-танков.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff2|cffced4da танка.|n"
        "|cffa6afb82-й уровень:|r |cffffffff5|cffced4da танков.|r"
    )
    wts_updates[11940] = "|cffe4cfa3Призыв Силитидов-Танков — уровень 1|r (|cffffffffR|r)"
    wts_updates[11945] = "|cffe4cfa3Призыв Силитидов-Танков — уровень 2|r (|cffffffffR|r)"
    wts_updates[30963] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da мощных Силитидов-танков.|r"
    )
    wts_updates[18436] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff5|cffced4da мощных Силитидов-танков.|r"
    )

    # AUls: Рой саранчи (R, lvl 2)
    wts_updates[11973] = "|cffe4cfa3Рой саранчи — уровень 2|r (|cffffffffR|r)"
    wts_updates[11974] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает рой саранчи, атакующий окружающих врагов и исцеляющий генерала пропорционально нанесённому урону.|r"
    )

    # AEah: Аура шипов (E, lvl 4)
    wts_updates[15762] = "|cffe4cfa3Аура шипов|r"
    wts_updates[15763] = "|cffe4cfa3Аура шипов|r"
    wts_updates[7792] = "|cffe4cfa3Аура шипов — уровень 4|r (|cffffffffE|r)"
    wts_updates[2643] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт окружающим союзникам щит, отражающий часть получаемого в ближнем бою урона обратно в атакующих.|r"
    )

    # AUts: Шипастый панцирь (lvl 4)
    wts_updates[11933] = "|cffe4cfa3Шипастый панцирь — уровень 4|r"
    wts_updates[11934] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает панцирь прочными хитиновыми шипами, увеличивающими броню и отражающими урон ближнего боя.|r"
    )

    # A0SQ: Раскат грома (Q)
    wts_updates[6528] = "|cffe4cfa3Раскат грома|r"
    wts_updates[6529] = "|cffe4cfa3Раскат грома|r"
    wts_updates[15387] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сотрясает землю, нанося урон и замедляя передвижение и атаку окружающих врагов.|n|n"
        "|cffa6afb81-й уровень:|r |cffffffff100|cffced4da урона.|n"
        "|cffa6afb82-й уровень:|r |cffffffff150|cffced4da урона.|n"
        "|cffa6afb83-й уровень:|r |cffffffff200|cffced4da урона.|n"
        "|cffa6afb84-й уровень:|r |cffffffff400|cffced4da урона.|r"
    )
    a0sq_tips = [6530, 6531, 9521, 9522]
    a0sq_ubs = [15388, 15416, 15389, 15386]
    a0sq_dmgs = [100, 150, 200, 400]
    for lvl in range(1, 5):
        wts_updates[a0sq_tips[lvl - 1]] = f"|cffe4cfa3Раскат грома — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a0sq_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff{a0sq_dmgs[lvl - 1]}|cffced4da ед. урона окружающим наземным врагам и замедляет их передвижение на |cffe69a8d50%|cffced4da и атаку на |cffe69a8d50%|cffced4da.|r"
        )

    # AEtq: Умиротворение (R, lvl 2)
    wts_updates[25766] = "|cffe4cfa3Умиротворение|r"
    wts_updates[25768] = "|cffe4cfa3Умиротворение|r"
    wts_updates[25770] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает поток целительной энергии, восстанавливающий здоровье всем союзникам в обширной области.|r"
    )
    wts_updates[2292] = "|cffe4cfa3Умиротворение — уровень 2|r (|cffffffffR|r)"
    wts_updates[2306] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает мощный целительный поток, восстанавливающий союзникам в области |cffffffff80|cffced4da ед. здоровья в секунду.|r"
    )

    # AUau: Нечистая аура (lvl 4)
    wts_updates[495] = "|cffe4cfa3Нечистая аура — уровень 4|r"
    wts_updates[508] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения окружающих союзников на |cffc8e087+30%|cffced4da и ускоряет регенерацию их здоровья.|r"
    )

    # AOhx: Сглаз (W, lvl 4)
    wts_updates[11976] = "|cffe4cfa3Сглаз — уровень 4|r (|cffffffffW|r)"
    wts_updates[11977] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает врага в случайное беззащитное существо на |cffffffff15|cffced4da сек., блокируя атаки и способности.|r"
    )

    # A0ST: Волна исцеления (Q)
    wts_updates[4405] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт волну энергии, восстанавливающую здоровье цепочке раненых союзников.|r"
    )
    wts_updates[15434] = "|cffe4cfa3Волна исцеления — уровень 4|r (|cffffffffQ|r)"
    wts_updates[18214] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087130|cffced4da ед. здоровья первой цели, исцеляя до |cffffffff3|cffced4da союзников.|r"
    )
    wts_updates[18249] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087215|cffced4da ед. здоровья первой цели, исцеляя до |cffffffff4|cffced4da союзников.|r"
    )
    wts_updates[18253] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087300|cffced4da ед. здоровья первой цели, исцеляя до |cffffffff5|cffced4da союзников.|r"
    )
    wts_updates[4404] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087385|cffced4da ед. здоровья первой цели, исцеляя до |cffffffff6|cffced4da союзников.|r"
    )

    # A0Y2: Проклятие (Q - Секарим)
    wts_updates[17154] = "|cffe4cfa3Проклятие|r"
    wts_updates[21237] = "|cffe4cfa3Проклятие|r"
    wts_updates[21236] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает цель губительным щитом бездны, наносящим урон окружающим союзникам и врагам.|r"
    )
    wts_updates[17427] = "|cffe4cfa3Проклятие — уровень 1|r (|cffffffffQ|r)"
    wts_updates[17428] = "|cffe4cfa3Проклятие — уровень 2|r (|cffffffffQ|r)"
    wts_updates[19555] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает поле бездны, наносящее |cffffffff25|cffced4da ед. урона/сек. существам вокруг цели в течение |cffffffff20|cffced4da сек.|r"
    )

    # A1B6: Создание Логова (R)
    wts_updates[30479] = "|cffe4cfa3Создание Логова|r"
    wts_updates[30480] = "|cffe4cfa3Создание Логова|r"
    wts_updates[30481] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возводит в указанной точке особое логово роя, периодически выпускающее Силитидов-танков.|r"
    )
    wts_updates[30484] = "|cffe4cfa3Создание Логова — уровень 1|r (|cffffffffR|r)"
    wts_updates[30482] = "|cffe4cfa3Создание Логова — уровень 2|r (|cffffffffR|r)"
    wts_updates[30483] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт в указанной точке логово роя, периодически выпускающее Силитидов-танков.|r"
    )
    wts_updates[30485] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт в указанной точке логово роя, периодически выпускающее Силитидов-танков.|r"
    )

    # A193: Ярость (Q)
    wts_updates[23434] = "|cffe4cfa3Ярость|r"
    wts_updates[29743] = "|cffe4cfa3Ярость|r"
    wts_updates[29755] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вводит императора в состояние ярости, существенно повышая скорость атаки и передвижения.|r"
    )
    a193_tips = [23450, 28660, 28661, 29742]
    a193_ubs = [28939, 29493, 29678]
    for lvl in range(1, 5):
        wts_updates[a193_tips[lvl - 1]] = f"|cffe4cfa3Ярость — уровень {lvl}|r (|cffffffffQ|r)"
    for idx, sid in enumerate(a193_ubs):
        lvl = idx + 2
        wts_updates[sid] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+{lvl * 25}%|cffced4da и скорость передвижения на |cffc8e087+25%|cffced4da.|r"
        )

    # A192: Мощь Акиров (W)
    wts_updates[3176] = "|cffe4cfa3Мощь Акиров|r"
    wts_updates[3171] = "|cffe4cfa3Мощь Акиров|r"
    wts_updates[29739] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура подавления снижает броню всех вражеских войск вокруг императора.|r"
    )
    a192_tips = [3172, 3173, 3174, 3175]
    a192_ubs = [29735, 29736, 29737, 29738]
    for lvl in range(1, 5):
        wts_updates[a192_tips[lvl - 1]] = f"|cffe4cfa3Мощь Акиров — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a192_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню врагов вокруг героя на |cffe69a8d{lvl * 2}|cffced4da.|r"
        )

    # A188: Двойная телепортация (E)
    wts_updates[23372] = "|cffe4cfa3Двойная телепортация|r"
    wts_updates[23374] = "|cffe4cfa3Двойная телепортация|r"
    wts_updates[28948] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно меняет братьев-императоров местами на поле боя и восстанавливает каждому часть здоровья.|r"
    )
    a188_tips = [23375, 23376, 23387, 23388]
    a188_ubs = [28953, 28954, 28955, 28956]
    for lvl in range(1, 5):
        wts_updates[a188_tips[lvl - 1]] = f"|cffe4cfa3Двойная телепортация — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[a188_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Меняет близнецов местами и восполняет обоим |cffc8e087+{lvl * 10}%|cffced4da здоровья.|r"
        )

    # A197: Создание Антенн (R)
    wts_updates[29784] = "|cffe4cfa3Создание Антенн|r"
    wts_updates[29785] = "|cffe4cfa3Создание Антенн|r"
    wts_updates[17160] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возводит полевую антенну, усиливающую скорость и регенерацию союзников поблизости.|r"
    )
    wts_updates[29787] = "|cffe4cfa3Создание Антенн — уровень 1|r (|cffffffffR|r)"
    wts_updates[29789] = "|cffe4cfa3Создание Антенн — уровень 2|r (|cffffffffR|r)"
    wts_updates[29788] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт полевую биовышку Антенн, усиливающую войска роя поблизости.|r"
    )
    wts_updates[29790] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт полевую биовышку Антенн, усиливающую войска роя поблизости.|r"
    )

    # A195: Древняя магия (Q)
    wts_updates[29767] = "|cffe4cfa3Древняя магия|r"
    wts_updates[30410] = "|cffe4cfa3Древняя магия|r"
    wts_updates[30411] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область сокрушительные волны тьмы, наносящие мгновенный и периодический урон.|r"
    )
    a195_tips = [29768, 29770, 29771, 29772]
    a195_ubs = [30406, 30407, 30408, 30409]
    for lvl in range(1, 5):
        wts_updates[a195_tips[lvl - 1]] = f"|cffe4cfa3Древняя магия — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[a195_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на область волны тьмы, наносящие мгновенный и периодический урон всем врагам.|r"
        )

    # A191: Передача Жизни (W)
    wts_updates[29722] = "|cffe4cfa3Передача Жизни|r"
    wts_updates[29723] = "|cffe4cfa3Передача Жизни|r"
    a191_tips = [29719, 29720, 29721, 29717]
    a191_ubs = [29724, 29725, 29726, 29716]
    for lvl in range(1, 5):
        wts_updates[a191_tips[lvl - 1]] = f"|cffe4cfa3Передача Жизни — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[a191_ubs[lvl - 1]] = (
            f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет союзнику здоровье в обмен на запас маны императора.|r"
        )

    # =========================================================================
    # 7. BUFFS (Custom buffs)
    # =========================================================================
    # B04G: Аура антенн
    wts_updates[11675] = "|cffe4cfa3Аура антенн|r"
    wts_updates[11677] = "|cffe4cfa3Аура антенн|r"

    # B04H: Аура Матери Роя
    wts_updates[11684] = "|cffe4cfa3Аура Матери Роя|r"
    wts_updates[12082] = "|cffe4cfa3Аура Матери Роя|r"
    wts_updates[12466] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и атаки |cffc8e087увеличены|cffced4da.|r"

    # B04I: Аура Пророка
    wts_updates[12085] = "|cffe4cfa3Аура Пророка|r"
    wts_updates[12086] = "|cffe4cfa3Аура Пророка|r"
    wts_updates[12467] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения и атаки |cffc8e087увеличены|cffced4da.|r"

    # B04K: Вязкая слизь
    wts_updates[12459] = "|cffe4cfa3Вязкая слизь|r"
    wts_updates[12061] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения |cffe69a8dснижена|cffced4da на |cffffffff15%|cffced4da.|r"

    # B05Z: Проклятие
    wts_updates[21819] = "|cffe4cfa3Проклятие|r"

    # B06W: Воздействие Акиров
    wts_updates[29744] = "|cffe4cfa3Воздействие Акиров|r"
    wts_updates[29745] = "|cffa6afb8ЭФФЕКТ:|cffced4da Броня цели |cffe69a8dснижена|cffced4da.|r"

    # B06X: Магия акиров
    wts_updates[29793] = "|cffe4cfa3Магия акиров|r"

    # B082: Дисциплина
    wts_updates[38477] = "|cffe4cfa3Дисциплина|r"
    wts_updates[38478] = "|cffa6afb8ЭФФЕКТ:|cffced4da Урон атак |cffc8e087увеличен|cffced4da на |cffffffff10%|cffced4da.|r"

    # =========================================================================
    # 8. TRIGGER MESSAGES
    # =========================================================================
    wts_updates[38642] = "|cffe4cfa3Один из игроков стал слугой Древнего Бога К'Туна...|r"

    # Plan payload
    plan_data = {
        "race": "Silitids",
        "race_id": 22,
        "total_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A0J7"],
            "markers": ["R0BV"],
            "buildings": [
                "e01H", "e021", "e020", "e01I", "e01J", "e01K",
                "e01L", "e01M", "e01X", "e00B", "h00C", "o015",
                "o017", "h08L", "h0MG", "h0DL"
            ],
            "units": [
                "e01G", "e01N", "e01O", "e01P", "e01Q", "e01R",
                "e01S", "e01T", "e01U", "e01V", "e01Y", "e01Z",
                "e023", "e02W", "u020", "u022"
            ],
            "heroes": [
                "U023", "U024", "U025", "U02A", "U02R", "U02S"
            ],
            "upgrades": [
                "R0BV", "R08G", "R088", "R089", "R08B", "R085",
                "R08A", "R083", "R084", "R07Z", "R07Y", "R009",
                "R07X", "R0D0", "R08C", "R08D", "R08F", "R08E",
                "R086", "R080", "R081", "R082", "R087"
            ],
            "abilities": [
                "A0J7", "A1B7", "A1B8", "A0T1", "A0SW", "A0ML",
                "A0J0", "A0VH", "A1KD", "A0SX", "A0KR", "A0KQ",
                "A0ZU", "A0IW", "A0JG", "A0IY", "A0JF", "A0KO",
                "A0IZ", "A1KF", "A1KG", "A1KE", "A0KN", "A0KM",
                "A1R4", "A0J2", "A0SU", "A0SV", "A0J1", "AUls",
                "AEah", "AUts", "A0SQ", "AEtq", "AUau", "AOhx",
                "A0ST", "A0Y2", "A1B6", "A193", "A192", "A188",
                "A197", "A195", "A191"
            ],
            "buffs": [
                "B04G", "B04H", "B04I", "B04K", "B05Z", "B06W", "B06X", "B082"
            ]
        }
    }

    out_file = folder / "silitids_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {out_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

    # =========================================================================
    # GENERATE CATEGORY REGISTRIES (docs/ui_text/silitids_*.json)
    # =========================================================================
    dump_path = ROOT / "scripts/silitids_raw_dump.json"
    dump = json.loads(dump_path.read_text(encoding="utf-8"))

    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    # 1. silitids_selection.json
    sel_data = {
        "scope": "Силитиды (Silitids / Аз'Акиры): подсказка выбора расы A0J7 и маркер фракции R0BV",
        "object": "A0J7",
        "variants": ["SD"],
        "hotkey": {"value": "S"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Silitids_O регистрирует способность A0J7.",
            "При выборе создаются 8 рабочих e01G, исследуется маркер R0BV, активируется gg_trg_SilitidsOn.",
            "Горячая клавиша S, создатель VinerX, куратор VinerX, сложность 5/5 (●●●●●), период «World of Warcraft: Vanilla»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38883, "after": wts_updates[38883]},
            {"field": "tip1", "wts_id": 38884, "after": wts_updates[38884]},
            {"field": "ubertip1", "wts_id": 36636, "after": wts_updates[36636]}
        ],
        "markers": [
            {
                "id": "R0BV",
                "name": "Силитиды и Аз'Акиры (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 30499, "after": wts_updates.get(30499)},
                    {"field": "tip1", "wts_id": 30500, "after": wts_updates.get(30500)},
                    {"field": "ubertip1", "wts_id": 30501, "after": wts_updates.get(30501)}
                ]
            }
        ]
    }
    (folder / "silitids_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote silitids_selection.json")

    # 2. silitids_buildings.json
    bld_entries = []
    for b in dump["buildings"]:
        b_id = b["id"]
        if b_id not in plan_data["categories"]["buildings"]:
            continue
        hk_val = b.get("hotkey")
        entry = {"id": b_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(b.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        bld_entries.append(entry)

    bld_data = {
        "scope": f"Силитиды (Silitids / Аз'Акиры): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "silitids_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote silitids_buildings.json ({len(bld_entries)} buildings)")

    # 3. silitids_units.json
    unit_entries = []
    for u in dump["units"]:
        u_id = u["id"]
        if u_id not in plan_data["categories"]["units"]:
            continue
        hk_val = u.get("hotkey")
        entry = {"id": u_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "tip", "ubertip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(u.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        unit_entries.append(entry)

    unit_data = {
        "scope": f"Силитиды (Silitids / Аз'Акиры): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "silitids_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote silitids_units.json ({len(unit_entries)} units)")

    # 4. silitids_heroes.json
    hero_entries = []
    for h in dump["heroes"]:
        h_id = h["id"]
        if h_id not in plan_data["categories"]["heroes"]:
            continue
        hk_val = h.get("hotkey")
        entry = {"id": h_id, "hotkey": hk_val, "strings": []}
        for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            raw_field = f"raw_{f}"
            sid = parse_str_id(h.get(raw_field))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        hero_entries.append(entry)

    hero_data = {
        "scope": f"Силитиды (Silitids / Аз'Акиры): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "silitids_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote silitids_heroes.json ({len(hero_entries)} heroes)")

    # 5. silitids_abilities.json
    abil_entries = []
    for a in dump["abilities"]:
        a_id = a["id"]
        if a_id not in plan_data["categories"]["abilities"]:
            continue
        entry = {"id": a_id, "levels": a.get("levels", 1), "strings": []}
        sid_name = parse_str_id(a.get("raw_name"))
        if sid_name and sid_name in wts_updates:
            entry["strings"].append({"field": "name", "wts_id": sid_name, "after": wts_updates[sid_name]})
        sid_rtip = parse_str_id(a.get("raw_researchtip"))
        if sid_rtip and sid_rtip in wts_updates:
            entry["strings"].append({"field": "researchtip", "wts_id": sid_rtip, "after": wts_updates[sid_rtip]})
        sid_rub = parse_str_id(a.get("raw_researchubertip"))
        if sid_rub and sid_rub in wts_updates:
            entry["strings"].append({"field": "researchubertip", "wts_id": sid_rub, "after": wts_updates[sid_rub]})
        for lvl_str, tips in a.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"tip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        for lvl_str, ubertips in a.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"ubertip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        if entry["strings"]:
            abil_entries.append(entry)

    abil_data = {
        "scope": f"Силитиды (Silitids / Аз'Акиры): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "silitids_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote silitids_abilities.json ({len(abil_entries)} abilities)")

    # 6. silitids_research.json
    upg_entries = []
    for u in dump["upgrades"]:
        u_id = u["id"]
        if u_id not in plan_data["categories"]["upgrades"]:
            continue
        entry = {"id": u_id, "levels": u.get("levels", 1), "strings": []}
        for lvl_str, names in u.get("names", {}).items():
            sid = parse_str_id(names.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"name_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        for lvl_str, tips in u.get("tips", {}).items():
            sid = parse_str_id(tips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"tip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        for lvl_str, ubertips in u.get("ubertips", {}).items():
            sid = parse_str_id(ubertips.get("raw"))
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"ubertip_{lvl_str}", "wts_id": sid, "after": wts_updates[sid]})
        upg_entries.append(entry)

    upg_data = {
        "scope": f"Силитиды (Silitids / Аз'Акиры): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "silitids_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote silitids_research.json ({len(upg_entries)} upgrades)")

    # 7. silitids_audit.json
    audit_data = {
        "race": "Силитиды и Аз'Акиры (Silitids)",
        "race_id": 22,
        "selection_ability": "A0J7",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "capital": {
                    "id": "h08L",
                    "name": "Храм Анкиража",
                    "food_provided": 200,
                    "verified_via": "01_core_economy.lua and unit object stats"
                }
            },
            "units": {
                "count": len(unit_entries),
                "ids": [u["id"] for u in unit_entries]
            },
            "heroes": {
                "count": len(hero_entries),
                "ids": [h["id"] for h in hero_entries],
                "names": {
                    "U023": "Пророк (Гор'аман / Скеррам — Интеллект, дальний бой)",
                    "U024": "Генерал Киражей (Раджакс — Сила, ближний бой)",
                    "U025": "Королева (Аямисси — Ловкость, дальний бой)",
                    "U02A": "Пророк Секарим (Секарим — Мифический герой, Интеллект, дальний бой)",
                    "U02R": "Император-близнец Век'нилаш (Легендарный герой, Сила, ближний бой)",
                    "U02S": "Император-близнец Век'лор (Легендарный герой, Интеллект, дальний бой)"
                },
                "unused_clones_checked": {
                    "U037": "Урсол (Клон с моделью FurbolgElder.mdl, в триггерах не используется)",
                    "U038": "Урсок (Клон с моделью FurbolgElder.mdl, в триггерах не используется)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(wts_updates)
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0BV": "Маркер расы Силитиды и Аз'Акиры"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items found in war3map.w3t for Silitids."
        },
        "messages_audit": {
            "race_specific_messages": ["TRIGSTR_38642"],
            "status": "Standardized TRIGSTR_38642: «Один из игроков стал слугой Древнего Бога К'Туна...»"
        },
        "buffs_audit": {
            "custom_buffs": ["B04G", "B04H", "B04I", "B04K", "B05Z", "B06W", "B06X", "B082"],
            "standard_buffs_used": [
                "BEah", "BHad", "BHtc", "BNab", "BNcg", "BNfy", "BNpa", "BNpm", "BNrf", "BOae",
                "BOhx", "BOwd", "BUau", "BUcs", "BUim", "BUsl", "BUsp", "BUts", "Bfae", "Bfzy",
                "Blsa", "Bpoi", "Bpsd", "Brpl", "Brpm", "Bspl", "Bust"
            ],
            "status": "Standardized custom buffs with secondary color labels and clean descriptions."
        },
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def)
    }
    (folder / "silitids_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote silitids_audit.json")

if __name__ == "__main__":
    main()
