# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and category registries for Alliance race (Race 29).

Generates:
- docs/ui_text/alliance_selection.json
- docs/ui_text/alliance_buildings.json
- docs/ui_text/alliance_units.json
- docs/ui_text/alliance_heroes.json
- docs/ui_text/alliance_abilities.json
- docs/ui_text/alliance_research.json
- docs/ui_text/alliance_audit.json
- docs/ui_text/alliance_plan.json
"""
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def clean_title(title: str) -> str:
    """Strip color tags, command prefixes and trailing brackets."""
    if not title:
        return ""
    # Strip color tags
    t = re.sub(r'\|c[0-9a-fA-F]{8}', '', title)
    t = t.replace('|r', '').replace('|R', '')
    
    # Strip forbidden prefixes
    prefixes = [
        "Обучить ", "Нанять ", "Призвать ", "Исследовать ", "Построить ", "Улучшить до ",
        "Произвести ", "Изучить ", "Провести ", "Train ", "Hire ", "Build ", "Research ", "Upgrade to "
    ]
    for p in prefixes:
        if t.startswith(p):
            t = t[len(p):]
            
    # Strip trailing hotkeys like (W), [Q], etc.
    t = re.sub(r'\s*[\(\[][A-Za-zА-Яа-я0-9\-\s]+[\)\]]$', '', t)
    return t.strip()

def format_title(title: str, hotkey: str = None) -> str:
    """Format short tip with unified palette: title in E4CFA3, hotkey in FFFFFF."""
    c = clean_title(title)
    if hotkey:
        return f"|cffe4cfa3{c}|r (|cffffffff{hotkey}|r)"
    return f"|cffe4cfa3{c}|r"

def clean_body_text(body: str) -> str:
    """Standardize body text: strip bad colors, normalize newlines."""
    if not body:
        return ""
    # remove old color tags
    t = re.sub(r'\|c[0-9a-fA-F]{8}', '', body)
    t = t.replace('|r', '').replace('|R', '')
    t = t.replace('\r\n', '\n').replace('\r', '\n')
    t = t.strip()
    return t

def main():
    dump_path = ROOT / "scripts/alliance_raw_dump.json"
    if not dump_path.exists():
        print("Raw dump not found, running inspect_alliance_all.py...")
        import inspect_alliance_all
        inspect_alliance_all.main()

    dump = json.loads(dump_path.read_text(encoding="utf-8"))
    wts = hw.load_wts_strings()

    wts_updates = {}
    checks_def = []

    def add_update(sid, new_val, obj_type=None, obj_id=None, field=None):
        if sid is None:
            return
        sid = int(sid)
        wts_updates[sid] = new_val
        if obj_type and obj_id and field:
            checks_def.append({
                "type": obj_type,
                "id": obj_id,
                "field": field,
                "expected": new_val
            })

    # =========================================================================
    # 1. SELECTION & SELECTION MARKERS (alliance_selection.json)
    # =========================================================================
    # A02A
    add_update(38859, "|cffe4cfa3Альянс|r", "ability", "A02A", "name")
    add_update(38860, "|cffe4cfa3Альянс|r (|cffffffffQ|r)", "ability", "A02A", "tip1")
    sel_ub = (
        "|cffa6afb8РАСА:|cffced4da Могущественный союз свободных народов Азерота, объединённых идеалами чести, благородства и защиты справедливости.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deWks|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●●|cffa6afb8○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Classic — Legion»|r|n|n"
        "|cffced4daАльянс — одна из двух величайших военно-политических сил Азерота в противовес Орде. "
        "Основанный как несокрушимый союз человеческих королевств Лордерона, Альянс со временем объединил людей Штормграда, "
        "дворфов Каз Модана, гномов Гномрегана, высших и ночных эльфов, дренеев и воргенов. "
        "Полагаясь на стальную дисциплину, силу Света, тайную магию Кирин-Тора и передовые осадные технологии, "
        "воины Альянса защищают Азерот от Пылающего Легиона и любых внешних угроз.|r"
    )
    add_update(41059, sel_ub, "ability", "A02A", "ubertip1")

    # Markers: R0GZ, R0HX, R0HW, R0HY, R0KK
    add_update(29663, "|cffe4cfa3Альянс|r", "upgrade", "R0GZ", "name1")
    add_update(29677, "|cffe4cfa3Альянс|r", "upgrade", "R0GZ", "tip1")
    add_update(29705, "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Альянсу.|r", "upgrade", "R0GZ", "ubertip1")

    add_update(30266, "|cffe4cfa3Кул-Тирас или Альянс|r", "upgrade", "R0HX", "name1")
    add_update(29942, "|cffe4cfa3Кул-Тирас или Альянс|r", "upgrade", "R0HX", "tip1")

    add_update(30254, "|cffe4cfa3Гномы|r", "upgrade", "R0HW", "name1")
    add_update(29941, "|cffe4cfa3Гномы|r", "upgrade", "R0HW", "tip1")

    add_update(30278, "|cffe4cfa3Стромгард или Альянс|r", "upgrade", "R0HY", "name1")
    add_update(30255, "|cffe4cfa3Стромгард или Альянс|r", "upgrade", "R0HY", "tip1")

    add_update(16408, "|cffe4cfa3Альянс или Даларан|r", "upgrade", "R0KK", "name1")
    add_update(16409, "|cffe4cfa3Альянс или Даларан|r", "upgrade", "R0KK", "tip1")
    add_update(16416, "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Альянсу или Даларану.|r", "upgrade", "R0KK", "ubertip1")

    # =========================================================================
    # 2. BUILDINGS (16 buildings) (alliance_buildings.json)
    # =========================================================================
    # htow: Ратуша (Q)
    add_update(27954, "|cffe4cfa3Ратуша|r", "unit", "htow", "name")
    add_update(27955, "|cffe4cfa3Ратуша|r (|cffffffffQ|r)", "unit", "htow", "tip")
    add_update(27956, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание первой ступени. Обеспечивает добычу ресурсов, склад и базовый запас пищи.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da: добытчик ресурсов и строитель.|n|n"
        "|cffa6afb8Улучшается до:|cffced4da|n- |cffa9c7deФорт|cffced4da: открывает доступ к передовым сооружениям и войскам.|r"
    ), "unit", "htow", "ubertip")

    # hkee: Форт (Z)
    add_update(8216, "|cffe4cfa3Форт|r", "unit", "hkee", "name")
    add_update(8286, "|cffe4cfa3Форт|r (|cffffffffZ|r)", "unit", "hkee", "tip")
    add_update(6464, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание второй ступени. Существенно увеличивает запас пищи и открывает новые технологии.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|n|n"
        "|cffa6afb8Улучшается до:|cffced4da|n- |cffa9c7deЗамок|cffced4da: открывает доступ к высшим технологиям и защите королевства.|r"
    ), "unit", "hkee", "ubertip")

    # hcas: Замок (Z)
    add_update(22325, "|cffe4cfa3Замок|r", "unit", "hcas", "name")
    add_update(22326, "|cffe4cfa3Замок|r (|cffffffffZ|r)", "unit", "hcas", "tip")
    add_update(9936, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание третьей ступени. Обеспечивает максимальный запас пищи и доступ к элитным силам Альянса.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|r"
    ), "unit", "hcas", "ubertip")

    # hhou: Ферма (A)
    add_update(8210, "|cffe4cfa3Ферма|r", "unit", "hhou", "name")
    add_update(8211, "|cffe4cfa3Ферма|r (|cffffffffA|r)", "unit", "hhou", "tip")
    add_update(27950, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию продовольствием и увеличивает доход королевства.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи и увеличивает доход на |cffffffff40|cffced4da ед.|r"
    ), "unit", "hhou", "ubertip")

    # hbar: Казармы (W)
    add_update(21619, "|cffe4cfa3Казармы|r", "unit", "hbar", "name")
    add_update(21620, "|cffe4cfa3Казармы|r (|cffffffffW|r)", "unit", "hbar", "tip")
    add_update(28154, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое производственное сооружение для подготовки пехоты ближнего и дальнего боя, а также кавалерии.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deПехотинец|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deКавалерия|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deТренировка ближнего боя|cffced4da|n- |cffa9c7deТренировка дальнего боя|cffced4da.|r"
    ), "unit", "hbar", "ubertip")

    # hbla: Кузница (R)
    add_update(12512, "|cffe4cfa3Кузница|r", "unit", "hbla", "name")
    add_update(12513, "|cffe4cfa3Кузница|r (|cffffffffR|r)", "unit", "hbla", "tip")
    add_update(12947, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Улучшает оружие, броню, снаряды и порох для сухопутных войск Альянса.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМифриловые мечи|cffced4da|n"
        "- |cffa9c7deМифриловая броня|cffced4da|n- |cffa9c7deДоспехи из армированной кожи|cffced4da|n"
        "- |cffa9c7deУлучшенные снаряды|cffced4da|n- |cffa9c7deМагическая атака|cffced4da.|r"
    ), "unit", "hbla", "ubertip")

    # hwtw: Дозорная башня (Z)
    add_update(22883, "|cffe4cfa3Дозорная башня|r", "unit", "hwtw", "name")
    add_update(23531, "|cffe4cfa3Дозорная башня|r (|cffffffffZ|r)", "unit", "hwtw", "tip")
    add_update(28156, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовая наблюдательная вышка. Не атакует, но может быть модернизирована в боевые башни.|n|n"
        "|cffa6afb8Улучшается до:|cffced4da|n- |cffa9c7deСторожевая башня|cffced4da: скорострельная стрелковая башня.|n"
        "- |cffa9c7deОрудийная башня|cffced4da: мощная осадная пушка с уроном по площади.|n"
        "- |cffa9c7deМагическая башня|cffced4da: сжигает ману врагов и раскрывает невидимость.|r"
    ), "unit", "hwtw", "ubertip")

    # hgtw: Сторожевая башня (Z)
    add_update(8287, "|cffe4cfa3Сторожевая башня|r", "unit", "hgtw", "name")
    add_update(9514, "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)", "unit", "hgtw", "tip")
    add_update(27951, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое оборонительное сооружение, вооружённое скорострельными стреломётами.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "hgtw", "ubertip")

    # hctw: Орудийная башня (X)
    add_update(9515, "|cffe4cfa3Орудийная башня|r", "unit", "hctw", "name")
    add_update(9517, "|cffe4cfa3Орудийная башня|r (|cffffffffX|r)", "unit", "hctw", "tip")
    add_update(28145, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Тяжёлое артиллерийское укрепление. Наносит сокрушительный урон по площади осадными ядрами.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "hctw", "ubertip")

    # hatw: Магическая башня (C)
    add_update(9520, "|cffe4cfa3Магическая башня|r", "unit", "hatw", "name")
    add_update(12509, "|cffe4cfa3Магическая башня|r (|cffffffffC|r)", "unit", "hatw", "tip")
    add_update(28153, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Магическое защитное укрепление. Сжигает ману атакуемых врагов, нанося дополнительный урон, и раскрывает невидимость вокруг себя.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "hatw", "ubertip")

    # halt: Алтарь королей (S)
    add_update(25259, "|cffe4cfa3Алтарь королей|r", "unit", "halt", "name")
    add_update(25271, "|cffe4cfa3Алтарь королей|r (|cffffffffS|r)", "unit", "halt", "tip")
    add_update(28160, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священное сооружение, где призываются великие лидеры Альянса и воскрешаются павшие герои.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deПаладин|cffced4da: воин Света с выбором специализации (Воздаяние, Защита или Лечение).|n"
        "- |cffa9c7deВерховный маг|cffced4da: мастер заклинаний стихии льда и телепортации.|n"
        "- |cffa9c7deГорный король|cffced4da: могучий воитель дворфов, сокрушающий врагов молотом.|r"
    ), "unit", "halt", "ubertip")

    # harm: Мастерская (F)
    add_update(9518, "|cffe4cfa3Мастерская|r", "unit", "harm", "name")
    add_update(9519, "|cffe4cfa3Мастерская|r (|cffffffffF|r)", "unit", "harm", "tip")
    add_update(28150, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Инженерный цех Альянса по конструированию передовой осадной техники, мортир и бронемашин.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deОсадный боец|cffced4da: дальнобойный мортирный расчёт.|n"
        "- |cffa9c7deТехника Альянса|cffced4da: бронированная осадная машина.|n"
        "- |cffa9c7deОсадная башня|cffced4da: мощное передвижное орудие штурма.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deКомплектование техники|cffced4da.|r"
    ), "unit", "harm", "ubertip")

    # hars: Волшебное святилище (D)
    add_update(40534, "|cffe4cfa3Волшебное святилище|r", "unit", "hars", "name")
    add_update(40535, "|cffe4cfa3Волшебное святилище|r (|cffffffffD|r)", "unit", "hars", "tip")
    add_update(28158, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обитель магов и жрецов. Обучает заклинателей и исследует тайны магических искусств.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМаг (Поддержка)|cffced4da: жрец-целитель.|n"
        "- |cffa9c7deМаг (Урон)|cffced4da: волшебница Кирин-Тора.|n"
        "- |cffa9c7deМаг (Специализированный)|cffced4da: ведьмак, разрушитель чар.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбучение боевых магов|cffced4da|n"
        "- |cffa9c7deОбучение магов поддержки|cffced4da|n- |cffa9c7deОбучение специализированных магов|cffced4da|n"
        "- |cffa9c7deМагический страж|cffced4da.|r"
    ), "unit", "hars", "ubertip")

    # hlum: Лесопилка (E)
    add_update(12510, "|cffe4cfa3Лесопилка|r", "unit", "hlum", "name")
    add_update(12511, "|cffe4cfa3Лесопилка|r (|cffffffffE|r)", "unit", "hlum", "tip")
    add_update(12950, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Склад древесины и центр архитектурных разработок Альянса.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУлучшенная кладка|cffced4da: усиливает прочность и броню зданий.|n"
        "- |cffa9c7deУлучшенная лесозаготовка|cffced4da: увеличивает количество переносимой древесины работниками.|r"
    ), "unit", "hlum", "ubertip")

    # hgra: Посольство (X)
    add_update(27439, "|cffe4cfa3Посольство|r", "unit", "hgra", "name")
    add_update(29063, "|cffe4cfa3Посольство|r (|cffffffffX|r)", "unit", "hgra", "tip")
    add_update(28162, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Дипломатический центр Альянса. Определяет политический курс, заключает союзы с расами Азерота и проводит военные реформы.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- Дипломатические и военные доктрины королевства.|r"
    ), "unit", "hgra", "ubertip")

    # h0M4: Верфь (C)
    add_update(22192, "|cffe4cfa3Верфь|r", "unit", "h0M4", "name")
    add_update(22193, "|cffe4cfa3Верфь|r (|cffffffffC|r)", "unit", "h0M4", "tip")
    add_update(10924, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Прибрежная верфь Альянса. Строит боевые корабли и улучшает мощь королевского флота.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТранспорт|cffced4da: корабль для переброски войск по воде.|n"
        "- |cffa9c7deЛегкий корабль Альянса|cffced4da: манёвренный боевой фрегат.|n"
        "- |cffa9c7deТяжелый корабль Альянса|cffced4da: мощный бронированный линкор.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- Модернизация орудий, парусов и корпуса флота.|r"
    ), "unit", "h0M4", "ubertip")

    # =========================================================================
    # 3. HEROES (alliance_heroes.json)
    # =========================================================================
    # H0H7, H0H9, H0H8: Паладин
    add_update(4487, "|cffe4cfa3Паладин|r", "unit", "H0H7", "name")
    add_update(20417, "|cffe4cfa3Паладин|r (|cffffffffZ|r)", "unit", "H0H7", "tip")
    add_update(31830, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Воин Света специализации «Воздаяние». Карает врагов священным возмездием и усиливает союзников боевыми аурами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДуховная Сила|cffced4da: пассивно увеличивает урон в бою.|n"
        "- |cffa9c7deВспышка Света|cffced4da: исцеляет выбранного союзника мощной вспышкой Света.|n"
        "- |cffa9c7deСокрушение|cffced4da: шанс нанести сокрушительный удар и оглушить врага.|n"
        "- |cffa9c7deКритический удар|cffced4da: шанс нанести многократный урон при атаке.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "H0H7", "ubertip")

    add_update(31831, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Несокрушимый защитник специализации «Защита». Принимает удары на себя, защищает союзников щитом Света и обращает вражеский натиск в ярость.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЖгучая броня|cffced4da: окружает паладина пламенем Света, наносящим урон врагам рядом.|n"
        "- |cffa9c7deСвет небес|cffced4da: исцеляет союзника или наносит урон нежити.|n"
        "- |cffa9c7deАватар|cffced4da: превращает паладина в гиганта с повышенным здоровьем и защитой от магии.|n"
        "- |cffa9c7deЯрость|cffced4da: повышает скорость атаки при снижении здоровья.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "H0H9", "ubertip")

    add_update(31832, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Священнослужитель специализации «Свет». Исцеляет союзников благодатью небес, воодушевляет армию и возвращает павших к жизни.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deГвардия|cffced4da: призывает стражей Света.|n"
        "- |cffa9c7deАура света|cffced4da: восстанавливает здоровье ближайшим союзникам.|n"
        "- |cffa9c7deМассовое исцеление|cffced4da: мощная волна лечения по области.|n"
        "- |cffa9c7deВоскрешение|cffced4da: воскрешает павших союзных воинов.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "H0H8", "ubertip")

    # H0ME / Hamg: Верховный маг (Z)
    add_update(28245, "|cffe4cfa3Верховный маг|r", "unit", "H0ME", "name")
    add_update(28271, "|cffe4cfa3Верховный маг|r (|cffffffffZ|r)", "unit", "H0ME", "tip")
    add_update(28276, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могущественный чародей Даларана. Повелевает стихией воды и льда, восстанавливает ману союзникам и мгновенно перемещает армию.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСнежная буря|cffced4da: обрушивает ледяной шквал на выбранную область.|n"
        "- |cffa9c7deПризыв элементаля воды|cffced4da: создаёт послушного духа стихии воды.|n"
        "- |cffa9c7deАура гениальности|cffced4da: ускоряет восстановление маны союзников.|n"
        "- |cffa9c7deМассовая телепортация|cffced4da: переносит мага и ближайших союзников к союзному зданию.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "H0ME", "ubertip")

    add_update(7396, "|cffe4cfa3Верховный маг|r", "unit", "Hamg", "name")
    add_update(28168, "|cffe4cfa3Верховный маг|r (|cffffffffZ|r)", "unit", "Hamg", "tip")
    add_update(28171, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могущественный чародей Даларана. Повелевает стихией воды и льда, восстанавливает ману союзникам и мгновенно перемещает армию.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСнежная буря|cffced4da: обрушивает ледяной шквал на выбранную область.|n"
        "- |cffa9c7deПризыв элементаля воды|cffced4da: создаёт послушного духа стихии воды.|n"
        "- |cffa9c7deАура гениальности|cffced4da: ускоряет восстановление маны союзников.|n"
        "- |cffa9c7deМассовая телепортация|cffced4da: переносит мага и ближайших союзников к союзному зданию.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "Hamg", "ubertip")

    # H0MF / Hmkg: Горный король (X)
    add_update(7415, "|cffe4cfa3Горный король|r", "unit", "H0MF", "name")
    add_update(28291, "|cffe4cfa3Горный король|r (|cffffffffX|r)", "unit", "H0MF", "tip")
    add_update(28416, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Грозный тан дворфов Каз Модана. Сокрушает вражеские ряды ударами боевого молота, сотрясает землю и обращается в аватару камня.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deГрозовой молот|cffced4da: бросает молот во врага, нанося урон и оглушая цель.|n"
        "- |cffa9c7deРаскат грома|cffced4da: сотрясает землю вокруг себя, замедляя врагов.|n"
        "- |cffa9c7deСильный удар|cffced4da: шанс оглушить врага и нанести дополнительный урон при атаке.|n"
        "- |cffa9c7deАватара|cffced4da: наделяет героя каменной стойкостью, броней и иммунитетом к магии.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "H0MF", "ubertip")

    add_update(1100, "|cffe4cfa3Горный король|r", "unit", "Hmkg", "name")
    add_update(12667, "|cffe4cfa3Горный король|r (|cffffffffX|r)", "unit", "Hmkg", "tip")
    add_update(15378, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Грозный тан дворфов Каз Модана. Сокрушает вражеские ряды ударами боевого молота, сотрясает землю и обращается в аватару камня.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deГрозовой молот|cffced4da: бросает молот во врага, нанося урон и оглушая цель.|n"
        "- |cffa9c7deРаскат грома|cffced4da: сотрясает землю вокруг себя, замедляя врагов.|n"
        "- |cffa9c7deСильный удар|cffced4da: шанс оглушить врага и нанести дополнительный урон при атаке.|n"
        "- |cffa9c7deАватара|cffced4da: наделяет героя каменной стойкостью, броней и иммунитетом к магии.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "Hmkg", "ubertip")

    # H0MD: Король Альянса (Z) - Вариан Ринн
    add_update(36000, "|cffe4cfa3Король Альянса|r", "unit", "H0MD", "name")
    add_update(36019, "|cffe4cfa3Король Альянса|r (|cffffffffZ|r)", "unit", "H0MD", "tip")

    # Hlgr: Темный рыцарь (Z) - Лорд Гаритос
    add_update(39906, "|cffe4cfa3Темный рыцарь|r", "unit", "Hlgr", "name")
    add_update(39907, "|cffa9c7deЛорд Гаритос|r", "unit", "Hlgr", "propernames")
    add_update(39909, "|cffe4cfa3Темный рыцарь|r (|cffffffffZ|r)", "unit", "Hlgr", "tip")
    add_update(39910, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Военачальник остатков армии Лордерона. Ведёт элитные человеческие отряды в бой железной рукой, обрушивая ударные волны и вдохновляя бойцов защищать человечество.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУдарная волна|cffced4da: рассекающая волна энергии, наносящая урон врагам на линии.|n"
        "- |cffa9c7deПризыв Гвардии|cffced4da: призывает ветеранов гвардии Лордерона.|n"
        "- |cffa9c7deЗа Человечество!|cffced4da: аура, повышающая боевой дух союзников.|n"
        "- |cffa9c7deЯрость Патриота|cffced4da: кратковременно дарует огромный бонус к атаке и скорости.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "Hlgr", "ubertip")

    # Paladin spec choice abilities on Altar: A0XI, A0XH, A0XJ
    add_update(29569, "|cffe4cfa3Специализация: Воздаяние|r", "ability", "A0XI", "name")
    add_update(29570, "|cffe4cfa3Специализация: Воздаяние|r", "ability", "A0XI", "tip1")
    add_update(29571, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет призвать паладина специализации «Воздаяние», ориентированного на нанесение урона и усиление атак союзников.|r", "ability", "A0XI", "ubertip1")

    add_update(29566, "|cffe4cfa3Специализация: Защита|r", "ability", "A0XH", "name")
    add_update(29567, "|cffe4cfa3Специализация: Защита|r", "ability", "A0XH", "tip1")
    add_update(29568, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет призвать паладина специализации «Защита», обладающего высокой стойкостью, защитной аурой и навыками контроля.|r", "ability", "A0XH", "ubertip1")

    add_update(29572, "|cffe4cfa3Специализация: Лечение|r", "ability", "A0XJ", "name")
    add_update(29573, "|cffe4cfa3Специализация: Лечение|r", "ability", "A0XJ", "tip1")
    add_update(29574, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет призвать паладина специализации «Лечение», сосредоточенного на исцелении союзников и их воскрешении.|r", "ability", "A0XJ", "ubertip1")

    # =========================================================================
    # 4. UNITS (63 units) (alliance_units.json)
    # =========================================================================
    # We will standardize all unit names, tips and ubertips that use TRIGSTR.
    # Let's inspect each unit and its TRIGSTRs systematically:

    # 1. hpea: Работник (Q)
    add_update(28151, "|cffe4cfa3Работник|r", "unit", "hpea", "name")
    add_update(28152, "|cffe4cfa3Работник|r (|cffffffffQ|r)", "unit", "hpea", "tip")
    add_update(12948, (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Альянса. Добывает древесину и золото, возводит и ремонтирует здания, а также может вступить в ополчение при тревоге.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРемонт|cffced4da: чинит повреждённые здания и технику.|n"
        "- |cffa9c7deПризыв к оружию|cffced4da: превращается во временного ополченца.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "hpea", "ubertip")

    # 2. hfoo: Рядовой пехотинец (W)
    add_update(27952, "|cffe4cfa3Рядовой пехотинец|r", "unit", "hfoo", "name")
    add_update(27953, "|cffe4cfa3Рядовой пехотинец|r (|cffffffffW|r)", "unit", "hfoo", "tip")
    add_update(12945, (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый воин ближнего боя первой ступени. Прикрывается прочным щитом от вражеских стрелков.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗащита|cffced4da: укрывается за щитом, снижая урон от дальних атак.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "hfoo", "ubertip")

    # 3. h0K4: Основной пехотинец (W)
    add_update(28833, "|cffe4cfa3Основной пехотинец|r", "unit", "h0K4", "name")
    add_update(28834, "|cffe4cfa3Основной пехотинец|r (|cffffffffW|r)", "unit", "h0K4", "tip")
    add_update(28835, (
        "|cffa6afb8ЮНИТ:|cffced4da Улучшенный воин ближнего боя второй ступени. Обладает повышенным здоровьем и крепкими доспехами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗащита|cffced4da: укрывается за щитом, отражая урон стрелков.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "h0K4", "ubertip")

    # 4. h0K7: Элитный пехотинец (W)
    add_update(28842, "|cffe4cfa3Элитный пехотинец|r", "unit", "h0K7", "name")
    add_update(28843, "|cffe4cfa3Элитный пехотинец|r (|cffffffffW|r)", "unit", "h0K7", "tip")
    add_update(28844, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный ветеран ближнего боя третьей ступени. Стойко держит передовую линию обороны Альянса.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗащита|cffced4da: снижает урон от атак дальнего боя.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "h0K7", "ubertip")

    # 5. hrif: Рядовой стрелок (R)
    add_update(31826, "|cffe4cfa3Рядовой стрелок|r", "unit", "hrif", "name")
    add_update(31827, "|cffe4cfa3Рядовой стрелок|r (|cffffffffR|r)", "unit", "hrif", "tip")
    add_update(12946, (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый стрелок дальнего боя. Вооружён дальнобойным мушкетом.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "hrif", "ubertip")

    # 6. h0K5: Основной стрелок (R)
    add_update(28836, "|cffe4cfa3Основной стрелок|r", "unit", "h0K5", "name")
    add_update(28837, "|cffe4cfa3Основной стрелок|r (|cffffffffR|r)", "unit", "h0K5", "tip")
    add_update(28838, (
        "|cffa6afb8ЮНИТ:|cffced4da Улучшенный стрелок дальнего боя второй ступени. Наносит повышенный урон колющими выстрелами.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "h0K5", "ubertip")

    # 7. h0K6: Элитный стрелок (R)
    add_update(28839, "|cffe4cfa3Элитный стрелок|r", "unit", "h0K6", "name")
    add_update(28840, "|cffe4cfa3Элитный стрелок|r (|cffffffffR|r)", "unit", "h0K6", "tip")
    add_update(28841, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный снайпер Альянса третьей ступени. Поражает цели с огромной дистанции бронебойными пулями.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "h0K6", "ubertip")

    # 8. hkni: Кавалерия (K)
    add_update(28845, "|cffe4cfa3Кавалерия|r", "unit", "hkni", "name")
    add_update(28846, "|cffe4cfa3Кавалерия|r (|cffffffffK|r)", "unit", "hkni", "tip")
    add_update(12949, (
        "|cffa6afb8ЮНИТ:|cffced4da Могучий бронированный всадник Альянса. Стремительно врывается в ряды врагов и сокрушает пехоту.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "hkni", "ubertip")

    # 9. hmtm: Осадный боец (M)
    add_update(28847, "|cffe4cfa3Осадный боец|r", "unit", "hmtm", "name")
    add_update(28848, "|cffe4cfa3Осадный боец|r (|cffffffffM|r)", "unit", "hmtm", "tip")
    add_update(12952, (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойный мортирный расчёт. Наносит сокрушительный урон осадными бомбами по площади и вражеским постройкам.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deОсколочные снаряды|cffced4da: увеличивают радиус и урон по небронированным целям.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "hmtm", "ubertip")

    # 10. hmtt: Техника Альянса (E)
    add_update(28849, "|cffe4cfa3Техника Альянса|r", "unit", "hmtt", "name")
    add_update(28850, "|cffe4cfa3Техника Альянса|r (|cffffffffE|r)", "unit", "hmtt", "tip")
    add_update(12953, (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлая бронемашина с зенитным ракетным комплексом. Создана для перехвата и уничтожения воздушных сил противника.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗаградительный огонь|cffced4da: выпускает ракетный залп по нескольким воздушным целям.|n|n"
        "Атакует воздушные цели.|r"
    ), "unit", "hmtt", "ubertip")

    # 11. h0KI: Осадная башня (T)
    add_update(28851, "|cffe4cfa3Осадная башня|r", "unit", "h0KI", "name")
    add_update(28852, "|cffe4cfa3Осадная башня|r (|cffffffffT|r)", "unit", "h0KI", "tip")
    add_update(28853, (
        "|cffa6afb8ЮНИТ:|cffced4da Сверхтяжёлое передвижное осадное орудие Альянса. Оснащено крупнокалиберной львиной пушкой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЛьвиная пушка|cffced4da: мощный залп по наземным целям и укреплениям.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "h0KI", "ubertip")

    # 12. hmpr: Маг (Поддержка) (P)
    add_update(28854, "|cffe4cfa3Маг (Поддержка)|r", "unit", "hmpr", "name")
    add_update(28855, "|cffe4cfa3Маг (Поддержка)|r (|cffffffffP|r)", "unit", "hmpr", "tip")
    add_update(12954, (
        "|cffa6afb8ЮНИТ:|cffced4da Священник-целитель Света. Исцеляет раненых бойцов, рассеивает вредоносные заклинания и вдохновляет союзников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deИсцеление|cffced4da: восстанавливает здоровье союзникам.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает чары и наносит урон призванным существам.|n"
        "- |cffa9c7deВнутренний огонь|cffced4da: повышает броню и силу атаки цели.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "hmpr", "ubertip")

    # 13. hsor: Маг (Урон) (S)
    add_update(28856, "|cffe4cfa3Маг (Урон)|r", "unit", "hsor", "name")
    add_update(28857, "|cffe4cfa3Маг (Урон)|r (|cffffffffS|r)", "unit", "hsor", "tip")
    add_update(12955, (
        "|cffa6afb8ЮНИТ:|cffced4da Волшебница Даларана. Контролирует поле боя замедлением, укрывает союзников невидимостью и обращает врагов в овец.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗамедление|cffced4da: снижает скорость перемещения и атаки врага.|n"
        "- |cffa9c7deНевидимость|cffced4da: скрывает союзника от взора врагов.|n"
        "- |cffa9c7deПревращение|cffced4da: временно обращает вражеского воина в безобидное существо.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "hsor", "ubertip")

    # 14. hspt: Маг (Специализированный) (B)
    add_update(28858, "|cffe4cfa3Маг (Специализированный)|r", "unit", "hspt", "name")
    add_update(28859, "|cffe4cfa3Маг (Специализированный)|r (|cffffffffB|r)", "unit", "hspt", "tip")
    add_update(12956, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный разрушитель чар. Обладает врождённым иммунитетом к магии, похищает положительные заклинания и подчиняет призванных существ.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПохищение заклинаний|cffced4da: переносит полезные чары на союзников, а вредоносные — на врагов.|n"
        "- |cffa9c7deМагический контроль|cffced4da: берёт под контроль призванное существо противника.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "hspt", "ubertip")

    # 15. h00X: Транспорт (B)
    add_update(4000, "|cffe4cfa3Транспорт|r", "unit", "h00X", "name")
    add_update(11200, "|cffe4cfa3Транспорт|r (|cffffffffB|r)", "unit", "h00X", "tip")
    add_update(30784, (
        "|cffa6afb8ЮНИТ:|cffced4da Морское транспортное судно Альянса. Перевозит сухопутные войска через водные пространства.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПосадка|cffced4da: принимает воинов на борт.|n"
        "- |cffa9c7deВысадка|cffced4da: высаживает войска на берег.|n|n"
        "Не атакует.|r"
    ), "unit", "h00X", "ubertip")

    # 16. h0L0: Легкий корабль Альянса (F)
    add_update(28860, "|cffe4cfa3Легкий корабль Альянса|r", "unit", "h0L0", "name")
    add_update(28861, "|cffe4cfa3Легкий корабль Альянса|r (|cffffffffF|r)", "unit", "h0L0", "tip")
    add_update(28862, (
        "|cffa6afb8ЮНИТ:|cffced4da Быстроходный боевой фрегат королевского флота. Оснащён бортовыми орудиями для перехвата морских и воздушных целей.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "h0L0", "ubertip")

    # 17. h0L1: Тяжелый корабль Альянса (B)
    add_update(28863, "|cffe4cfa3Тяжелый корабль Альянса|r", "unit", "h0L1", "name")
    add_update(28864, "|cffe4cfa3Тяжелый корабль Альянса|r (|cffffffffB|r)", "unit", "h0L1", "tip")
    add_update(28865, (
        "|cffa6afb8ЮНИТ:|cffced4da Бронированный флагманский линкор Альянса. Обрушивает массированные артиллерийские залпы по береговым укреплениям и вражескому флоту.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "h0L1", "ubertip")

    # Dynamic / Embassy units:
    # 18. h0KD: Штормградский воитель (W)
    add_update(28866, "|cffe4cfa3Штормградский воитель|r", "unit", "h0KD", "name")
    # 19. h0KH: Кавалерист Штормграда (K)
    add_update(40239, "|cffe4cfa3Кавалерист Штормграда|r", "unit", "h0KH", "name")
    # 20. h0LW: Новобранец 7-го Легиона
    add_update(28867, "|cffe4cfa3Новобранец 7-го Легиона|r", "unit", "h0LW", "name")
    # 21. h0KE: Боец 7-го Легиона
    add_update(28868, "|cffe4cfa3Боец 7-го Легиона|r", "unit", "h0KE", "name")
    # 22. h0LU: Агент ШРУ (I)
    add_update(28869, "|cffe4cfa3Агент ШРУ|r", "unit", "h0LU", "name")
    add_update(28872, "|cffe4cfa3Агент ШРУ|r", "unit", "h0LU", "tip")
    # 23. h0OW: Ветеран войны
    add_update(31945, "|cffe4cfa3Ветеран войны|r", "unit", "h0OW", "name")
    add_update(31947, "|cffe4cfa3Ветеран войны|r", "unit", "h0OW", "tip")
    add_update(31946, (
        "|cffa6afb8ЮНИТ:|cffced4da Закалённый в битвах ветеран Второй войны. Вдохновляет окружающих союзников командирской аурой и обладает колоссальной стойкостью.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Ветерана|cffced4da: повышает характеристики находящихся рядом бойцов.|n"
        "- |cffa9c7deНеубиваемые|cffced4da: снижает получаемый физический урон.|n|n"
        "Атакует наземные цели.|r"
    ), "unit", "h0OW", "ubertip")

    # 24. h0KR: Пехотинец Лордерона
    add_update(28873, "|cffe4cfa3Пехотинец Лордерона|r", "unit", "h0KR", "name")
    # 25. h0KC: Пехотинец
    add_update(28874, "|cffe4cfa3Пехотинец|r", "unit", "h0KC", "name")
    # 26. h0KK: Ветеран Лордерона
    add_update(28875, "|cffe4cfa3Ветеран Лордерона|r", "unit", "h0KK", "name")
    # 27. h0KW: Кавалерист Лордерона
    add_update(28876, "|cffe4cfa3Кавалерист Лордерона|r", "unit", "h0KW", "name")

    # 28. h0M9: Воитель Стромгарда
    add_update(28877, "|cffe4cfa3Воитель Стромгарда|r", "unit", "h0M9", "name")
    # 29. h0MA: Кавалерист Стромгарда
    add_update(28878, "|cffe4cfa3Кавалерист Стромгарда|r", "unit", "h0MA", "name")

    # 30. h0M7: Стрелок (култирасец)
    add_update(28879, "|cffe4cfa3Стрелок Кул-Тираса|r", "unit", "h0M7", "name")
    add_update(28880, "|cffe4cfa3Стрелок Кул-Тираса|r", "unit", "h0M7", "tip")
    # 31. h0M5: Жрец Штормов
    add_update(28881, "|cffe4cfa3Жрец Штормов|r", "unit", "h0M5", "name")
    add_update(28882, "|cffe4cfa3Жрец Штормов|r", "unit", "h0M5", "tip")
    # 32. h0M6: Галеон
    add_update(28883, "|cffe4cfa3Галеон|r", "unit", "h0M6", "name")
    add_update(28884, "|cffe4cfa3Галеон|r", "unit", "h0M6", "tip")

    # 33. h0M2: Лютый ворген
    add_update(28885, "|cffe4cfa3Лютый ворген|r", "unit", "h0M2", "name")
    add_update(28886, "|cffe4cfa3Лютый ворген|r", "unit", "h0M2", "tip")
    # 34. h0M3: Стрелок ворген
    add_update(28887, "|cffe4cfa3Стрелок Гилнеаса|r", "unit", "h0M3", "name")
    add_update(28888, "|cffe4cfa3Стрелок Гилнеаса|r", "unit", "h0M3", "tip")

    # 35. h0KN: Лучница (НЭ)
    add_update(28889, "|cffe4cfa3Лучница|r", "unit", "h0KN", "name")
    # 36. h0L2: Лучница
    add_update(28890, "|cffe4cfa3Лучница|r", "unit", "h0L2", "name")
    # 37. h0LZ: Часовая
    add_update(28891, "|cffe4cfa3Часовая|r", "unit", "h0LZ", "name")
    # 38. h0KT: Друид
    add_update(28892, "|cffe4cfa3Друид|r", "unit", "h0KT", "name")

    # 39. h0KO: Дворфийский стрелок
    add_update(28893, "|cffe4cfa3Дворфийский стрелок|r", "unit", "h0KO", "name")
    # 40. h0KY: Гном чернокнижник
    add_update(40240, "|cffe4cfa3Гном-чернокнижник|r", "unit", "h0KY", "name")
    # 41. h0KJ: Паровой танк v2
    add_update(28894, "|cffe4cfa3Паровой танк v2|r", "unit", "h0KJ", "name")
    # 42. h0KS: Паровой танк
    add_update(28895, "|cffe4cfa3Паровой танк|r", "unit", "h0KS", "name")
    # 43. h0LY: Старый танк
    add_update(40241, "|cffe4cfa3Старый танк|r", "unit", "h0LY", "name")
    # 44. h0KP: Орудие
    add_update(28896, "|cffe4cfa3Орудие|r", "unit", "h0KP", "name")
    # 45. h0KZ: Орудийный расчет
    add_update(28897, "|cffe4cfa3Орудийный расчет|r", "unit", "h0KZ", "name")
    # 46. o044: Голем Черного Железа
    add_update(40242, "|cffe4cfa3Голем Черного Железа|r", "unit", "o044", "name")

    # 47. h0MB: Жрица Наару
    add_update(28898, "|cffe4cfa3Жрица Наару|r", "unit", "h0MB", "name")
    add_update(28899, "|cffe4cfa3Жрица Наару|r", "unit", "h0MB", "tip")
    # 48. h0MC: Жрица Тьмы
    add_update(28900, "|cffe4cfa3Жрица Тьмы|r", "unit", "h0MC", "name")
    add_update(28901, "|cffe4cfa3Жрица Тьмы|r", "unit", "h0MC", "tip")
    # 49. h0KX: Воздаятель
    add_update(28902, "|cffe4cfa3Воздаятель|r", "unit", "h0KX", "name")

    # 50. o042: Мастер боя (пандарен)
    add_update(28903, "|cffe4cfa3Мастер боя|r", "unit", "o042", "name")
    # 51. o043: Воин Шадо-Пан
    add_update(29050, "|cffe4cfa3Воин Шадо-Пан|r", "unit", "o043", "name")
    add_update(29051, "|cffe4cfa3Воин Шадо-Пан|r", "unit", "o043", "tip")

    # 52. h0M8: Арканист
    add_update(29052, "|cffe4cfa3Арканист|r", "unit", "h0M8", "name")
    add_update(29053, "|cffe4cfa3Арканист|r", "unit", "h0M8", "tip")
    # 53. o040: Антимагический кристалл
    add_update(29858, "|cffe4cfa3Антимагический кристалл|r", "unit", "o040", "name")

    # 54. h0KA: Лучник
    add_update(29559, "|cffe4cfa3Лучник|r", "unit", "h0KA", "name")
    # 55. h0KB: Арбалетчик
    add_update(3570, "|cffe4cfa3Арбалетчик|r", "unit", "h0KB", "name")
    # 56. h0K9: Стрелок
    add_update(25550, "|cffe4cfa3Стрелок|r", "unit", "h0K9", "name")
    add_update(29027, "|cffe4cfa3Стрелок|r", "unit", "h0K9", "tip")
    # 57. h0KL: Жрец
    add_update(32799, "|cffe4cfa3Жрец|r", "unit", "h0KL", "name")
    # 58. h0KM: Заклинатель
    add_update(5544, "|cffe4cfa3Заклинатель|r", "unit", "h0KM", "name")
    add_update(8063, "|cffe4cfa3Заклинатель|r", "unit", "h0KM", "tip")
    add_update(3595, (
        "|cffa6afb8ЮНИТ:|cffced4da Маг разрушения Кирин-Тора. Обрушивает на врагов огненные кольца, снежные бури и раскалённые ядра.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСнежная буря|cffced4da: обрушивает ледяной град на область.|n"
        "- |cffa9c7deКольцо огня|cffced4da: поражает врагов волной пламени.|n"
        "- |cffa9c7deОгненные ядра|cffced4da: выпускает взрывные сгустки огня.|n|n"
        "Атакует наземные и воздушные цели.|r"
    ), "unit", "h0KM", "ubertip")
    # 59. h0KQ: Мудрец
    add_update(32804, "|cffe4cfa3Мудрец|r", "unit", "h0KQ", "name")
    # 60. h0KU: Целитель
    add_update(32806, "|cffe4cfa3Целитель|r", "unit", "h0KU", "name")
    # 61. h0KV: Волшебница
    add_update(6012, "|cffe4cfa3Волшебница|r", "unit", "h0KV", "name")
    # 62. h0KF: Паладин
    add_update(30234, "|cffe4cfa3Паладин|r", "unit", "h0KF", "name")
    # 63. h0KG: Тяжелый пехотинец
    add_update(27910, "|cffe4cfa3Тяжелый пехотинец|r", "unit", "h0KG", "name")

    # =========================================================================
    # 5. RESEARCHES & EMBASSY (alliance_research.json)
    # =========================================================================
    # Embassy Researches:
    # R0GX: Политика Изоляционизма
    add_update(40884, "|cffe4cfa3Политика Изоляционизма|r", "upgrade", "R0GX", "name1")
    add_update(40885, "|cffe4cfa3Политика Изоляционизма|r", "upgrade", "R0GX", "tip1")
    add_update(28163, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Альянс закрывает границы и сосредотачивается исключительно на собственных ресурсах.|n|n"
        "|cffc8e087Уменьшает расходы на 15%|cffced4da, но |cffe69a8dблокирует выбор любых других политических веток|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Всему королевству Альянса.|r"
    ), "upgrade", "R0GX", "ubertip1")

    # R0HR: Внутреннее развитие
    add_update(40914, "|cffe4cfa3Внутреннее развитие|r", "upgrade", "R0HR", "name1")
    add_update(40915, "|cffe4cfa3Внутреннее развитие|r", "upgrade", "R0HR", "tip1")
    add_update(28164, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Штормград укрепляет внутреннюю инфраструктуру и реорганизует королевскую армию.|n|n"
        "Открывает ветку исследований по улучшению регулярных войск Штормграда.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Армии Штормграда.|r"
    ), "upgrade", "R0HR", "ubertip1")

    # R0HS: Расширение Альянса
    add_update(40916, "|cffe4cfa3Расширение Альянса|r", "upgrade", "R0HS", "name1")
    add_update(40917, "|cffe4cfa3Расширение Альянса|r", "upgrade", "R0HS", "tip1")
    add_update(28165, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Для поддержания мирового порядка Альянс приглашает союзные народы встать под его знамёна.|n|n"
        "Открывает дипломатическую ветку союзов с другими расами Азерота.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Дипломатическому корпусу Посольства.|r"
    ), "upgrade", "R0HS", "ubertip1")

    # R0HQ: Человечество важнее всего
    add_update(40912, "|cffe4cfa3Человечество важнее всего|r", "upgrade", "R0HQ", "name1")
    add_update(40913, "|cffe4cfa3Человечество важнее всего|r", "upgrade", "R0HQ", "tip1")
    add_update(28166, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Штормград берёт курс на воссоединение всех человеческих королевств, возвращаясь к истокам древнего Аратора.|n|n"
        "Открывает ветку объединения Лордерона, Стромгарда, Кул-Тираса и Гилнеаса.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Королевствам людей.|r"
    ), "upgrade", "R0HQ", "ubertip1")

    # R0HE: Децентрализация
    add_update(32955, "|cffe4cfa3Децентрализация|r", "upgrade", "R0HE", "name1")
    add_update(32956, "|cffe4cfa3Децентрализация|r", "upgrade", "R0HE", "tip1")
    add_update(40544, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Гномы Гномрегана и их технологии получают статус полноправных союзников в Альянсе.|n|n"
        "Открывает новый вид парового танка и мага поддержки гномов. |cffc8e087Снижает расходы на 10%|cffced4da и повышает шанс найма не-людей. |cffe69a8dЗакрывает другие ветки|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Инженерным и магическим войскам Альянса.|r"
    ), "upgrade", "R0HE", "ubertip1")

    # R0HF: Союз равных
    add_update(40904, "|cffe4cfa3Союз равных|r", "upgrade", "R0HF", "name1")
    add_update(40905, "|cffe4cfa3Союз равных|r", "upgrade", "R0HF", "tip1")
    add_update(41231, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Штормград делит верховную власть с присоединившимися народами, создавая равноправную коалицию.|n|n"
        "Повышает шансы выхода воинов не-людей, |cffc8e087уменьшает расходы на 6%|cffced4da, открывает новые дипломатические союзы. |cffe69a8dЗакрывает другие ветки|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Армии Альянса.|r"
    ), "upgrade", "R0HF", "ubertip1")

    # R0HG: Восстановить Аратор
    add_update(32957, "|cffe4cfa3Восстановить Аратор|r", "upgrade", "R0HG", "name1")
    add_update(32958, "|cffe4cfa3Восстановить Аратор|r", "upgrade", "R0HG", "tip1")
    add_update(41232, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Возрождение великой империи Аратор объединяет племена и северные пределы Восточных королевств.|n|n"
        "Увеличивает шансы найма людей, даёт |cffc8e087+100 к здоровью|cffced4da и |cffc8e087+2 к броне|cffced4da пехотинцам, а также |cffc8e087снижает расходы на 10%|cffced4da. |cffe69a8dЗакрывает другие ветки|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Воинам-людям Альянса.|r"
    ), "upgrade", "R0HG", "ubertip1")

    # R0HH: Штормград превыше всего
    add_update(40906, "|cffe4cfa3Штормград превыше всего|r", "upgrade", "R0HH", "name1")
    add_update(40907, "|cffe4cfa3Штормград превыше всего|r", "upgrade", "R0HH", "tip1")
    add_update(28167, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Штормград утверждает абсолютное господство человеческой короны.|n|n"
        "|cffc8e087Снижает расходы на 5%|cffced4da и уменьшает траты на союзников, но в армию нанимаются исключительно воины Штормграда.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Регулярной армии Штормграда.|r"
    ), "upgrade", "R0HH", "ubertip1")

    # R0H5: Запрос Ночных Эльфов
    add_update(40888, "|cffe4cfa3Запрос Ночных Эльфов|r", "upgrade", "R0H5", "name1")
    add_update(40889, "|cffe4cfa3Запрос Ночных Эльфов|r", "upgrade", "R0H5", "tip1")
    add_update(28169, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Древний народ ночных эльфов Калимдора направляет подкрепления в ряды Альянса.|n|n"
        "Открывает лучниц и часовых, а также друида-заклинателя. |cffc8e087Снижает расходы на 4%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Казармам и Волшебному святилищу.|r"
    ), "upgrade", "R0H5", "ubertip1")

    # R0H6: Сформировать Седьмой Легион
    add_update(40890, "|cffe4cfa3Сформировать Седьмой Легион|r", "upgrade", "R0H6", "name1")
    add_update(40891, "|cffe4cfa3Сформировать Седьмой Легион|r", "upgrade", "R0H6", "tip1")
    add_update(28170, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Создание элитного боевого соединения Штормграда для экспедиций и спецопераций.|n|n"
        "Даёт воинам Штормграда |cffc8e087+50 к здоровью|cffced4da, |cffc8e087+7% к скорости атаки|cffced4da и |cffc8e087+25% к скорости перемещения|cffced4da, "
        "заменяет новобранцев на бойцов 7-го Легиона и открывает бойцов на грифонах. |cffc8e087+4% к доходам|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Воинам Штормграда и 7-го Легиона.|r"
    ), "upgrade", "R0H6", "ubertip1")

    # R0H7: Церковь и Государство
    add_update(40892, "|cffe4cfa3Церковь и Государство|r", "upgrade", "R0H7", "name1")
    add_update(40893, "|cffe4cfa3Церковь и Государство|r", "upgrade", "R0H7", "tip1")
    add_update(28172, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Союз короны с духовенством Света возрождает традиции рыцарей Серебряной Длани.|n|n"
        "Добавляет элитного пехотинца-паладина, усиливает исцеление жрецов, повышает их запас здоровья и маны. |cffe69a8dПовышает расходы на 3%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Пехотинцам и жрецам Альянса.|r"
    ), "upgrade", "R0H7", "ubertip1")

    # R0H8: Взять Дренеев в Альянс
    add_update(40894, "|cffe4cfa3Взять Дренеев в Альянс|r", "upgrade", "R0H8", "name1")
    add_update(40895, "|cffe4cfa3Взять Дренеев в Альянс|r", "upgrade", "R0H8", "tip1")
    add_update(28173, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Изгнанники с Аргуса во главе с пророком Веленом присоединяются к Альянсу.|n|n"
        "Открывает жрицу Наару и паладина-воздаятеля. |cffc8e087Снижает расходы на 2%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Силам Света Альянса.|r"
    ), "upgrade", "R0H8", "ubertip1")

    # R0H9: Былой союзник (Воргены)
    add_update(40896, "|cffe4cfa3Былой союзник|r", "upgrade", "R0H9", "name1")
    add_update(40897, "|cffe4cfa3Былой союзник|r", "upgrade", "R0H9", "tip1")
    add_update(28174, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Королевство Гилнеас за стеной Седогрива вновь открывает ворота для Альянса.|n|n"
        "Открывает свирепых лютых воргенов и стрелков Гилнеаса. |cffe69a8dПовышает расходы на 2%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Казармам Альянса.|r"
    ), "upgrade", "R0H9", "ubertip1")

    # R0HA: Расширить ШРУ
    add_update(40898, "|cffe4cfa3Расширить ШРУ|r", "upgrade", "R0HA", "name1")
    add_update(40899, "|cffe4cfa3Расширить ШРУ|r", "upgrade", "R0HA", "tip1")
    add_update(40337, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Штормградская разведка расширяет сеть тайных агентов по всему миру.|n|n"
        "Добавляет агентов ШРУ, способных действовать под невидимостью и отравлять врагов ядом. |cffe69a8dПовышает расходы на 3%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Разведывательным силам Альянса.|r"
    ), "upgrade", "R0HA", "ubertip1")

    # R0HB: Принять к себе Пандаренов
    add_update(40900, "|cffe4cfa3Принять к себе Пандаренов|r", "upgrade", "R0HB", "name1")
    add_update(40901, "|cffe4cfa3Принять к себе Пандаренов|r", "upgrade", "R0HB", "tip1")
    add_update(40543, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Мирные пандарены Тушуй присоединяются к силам Альянса.|n|n"
        "Открывает мастеров боя и воинов Шадо-Пан ближнего боя. |cffc8e087Снижает расходы на 2%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Войскам ближнего боя.|r"
    ), "upgrade", "R0HB", "ubertip1")

    # R0HC: Новые осадные технологии
    add_update(40902, "|cffe4cfa3Новые осадные технологии|r", "upgrade", "R0HC", "name1")
    add_update(40903, "|cffe4cfa3Новые осадные технологии|r", "upgrade", "R0HC", "tip1")
    add_update(28175, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Передовые чертежи инженеров позволяют создать тяжёлую штурмовую башню.|n|n"
        "Открывает производство осадных башен в Мастерской.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deМастерская|cffced4da.|r"
    ), "upgrade", "R0HC", "ubertip1")

    # R0HD: Диалог с Кул-тирасом
    add_update(32953, "|cffe4cfa3Диалог с Кул-Тирасом|r", "upgrade", "R0HD", "name1")
    add_update(32954, "|cffe4cfa3Диалог с Кул-Тирасом|r", "upgrade", "R0HD", "tip1")
    add_update(28176, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Восстановление дипломатических связей с великой морской нацией Кул-Тираса.|n|n"
        "Открывает жрецов штормов, стрелков Кул-Тираса и боевые галеоны. |cffe69a8dПовышает расходы на 3%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Армии и флоту Альянса.|r"
    ), "upgrade", "R0HD", "ubertip1")

    # R0HI: Надавить на Даларан
    add_update(32951, "|cffe4cfa3Надавить на Даларан|r", "upgrade", "R0HI", "name1")
    add_update(32952, "|cffe4cfa3Надавить на Даларан|r", "upgrade", "R0HI", "tip1")
    add_update(41269, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Орден Кирин-Тора усиливает поддержку сухопутных сил Альянса своими лучшими арканистами.|n|n"
        "Открывает арканистов Даларана и повышает характеристики всех магов Альянса. |cffc8e087Снижает расходы на 3%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Магам Волшебного святилища.|r"
    ), "upgrade", "R0HI", "ubertip1")

    # R0HJ: Реконструировать Стромгард
    add_update(40908, "|cffe4cfa3Реконструировать Стромгард|r", "upgrade", "R0HJ", "name1")
    add_update(40909, "|cffe4cfa3Реконструировать Стромгард|r", "upgrade", "R0HJ", "tip1")
    add_update(41577, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Восстановление цитадели Стромгарда укрепляет колыбель человечества.|n|n"
        "Открывает воителей и кавалеристов Стромгарда. |cffc8e087Снижает расходы на 2%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Войскам Стромгарда.|r"
    ), "upgrade", "R0HJ", "ubertip1")

    # R0HK: Армия Света
    add_update(40910, "|cffe4cfa3Армия Света|r", "upgrade", "R0HK", "name1")
    add_update(40911, "|cffe4cfa3Армия Света|r", "upgrade", "R0HK", "tip1")
    add_update(41763, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Озарённые воины Великой Армии Света приходят на помощь Альянсу.|n|n"
        "Открывает жрицу Наару и благословение Света. |cffc8e087Снижает расходы на 3%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Силам Света.|r"
    ), "upgrade", "R0HK", "ubertip1")

    # R0HL: Отряды Тьмы
    add_update(32949, "|cffe4cfa3Отряды Тьмы|r", "upgrade", "R0HL", "name1")
    add_update(32950, "|cffe4cfa3Отряды Тьмы|r", "upgrade", "R0HL", "tip1")
    add_update(41837, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Изучение темных искусств Бездны открывает доступ к тайным заклинателям Тьмы.|n|n"
        "Открывает жрицу Тьмы. |cffc8e087Снижает расходы на 3%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Магам Волшебного святилища.|r"
    ), "upgrade", "R0HL", "ubertip1")

    # R0HM: Вопрос Клана Черного Железа
    add_update(32947, "|cffe4cfa3Вопрос Клана Черного Железа|r", "upgrade", "R0HM", "name1")
    add_update(32948, "|cffe4cfa3Вопрос Клана Черного Железа|r", "upgrade", "R0HM", "tip1")
    add_update(28177, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дворфы Тёмного Железа королевы Мойры Тауриссан вступают в союз с Альянсом.|n|n"
        "Открывает сокрушительного голема Чёрного Железа. |cffc8e087Снижает расходы на 2%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Мастерской Альянса.|r"
    ), "upgrade", "R0HM", "ubertip1")

    # R0HN: Память о Лотаре
    add_update(32945, "|cffe4cfa3Память о Лотаре|r", "upgrade", "R0HN", "name1")
    add_update(32946, "|cffe4cfa3Память о Лотаре|r", "upgrade", "R0HN", "tip1")
    add_update(28178, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Чествование подвига сэра Андуина Лотара и сыновей Лотара из экспедиции в Дренор.|n|n"
        "Открывает ветерана войны, даёт всадникам новую способность и |cffc8e087+125 к здоровью|cffced4da. |cffe69a8dПовышает расходы на 15%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Кавалерии и пехоте Альянса.|r"
    ), "upgrade", "R0HN", "ubertip1")

    # R0HV: Интеграция Лордеронцев
    add_update(40918, "|cffe4cfa3Интеграция Лордеронцев|r", "upgrade", "R0HV", "name1")
    add_update(40919, "|cffe4cfa3Интеграция Лордеронцев|r", "upgrade", "R0HV", "tip1")
    add_update(42384, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Принятие беженцев и уцелевших воинов павшего королевства Лордерон в ряды армии.|n|n"
        "Повышает шансы выхода людей Лордерона, открывает им новую способность и увеличивает боевые параметры. |cffe69a8dПовышает расходы на 3%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Войскам Лордерона.|r"
    ), "upgrade", "R0HV", "ubertip1")

    # Barracks Upgrades: R0GV, R0GW
    for lvl in range(1, 4):
        sid_n = 40871 + lvl  # 40872, 40873, 40874
        sid_t = 40874 + lvl  # 40875, 40876, 40877
        add_update(sid_n, f"|cffe4cfa3Тренировка ближнего боя — уровень {lvl}|r", "upgrade", "R0GV", f"name{lvl}")
        add_update(sid_t, f"|cffe4cfa3Тренировка ближнего боя — уровень {lvl}|r", "upgrade", "R0GV", f"tip{lvl}")
    add_update(42380, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает боевую выучку и стойкость пехоты ближнего боя Альянса.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Воинам ближнего боя.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3/3|r."
    ), "upgrade", "R0GV", "ubertip3")

    for lvl in range(1, 4):
        sid_n = 40877 + lvl  # 40878, 40879, 40880
        sid_t = 40880 + lvl  # 40881, 40882, 40883
        add_update(sid_n, f"|cffe4cfa3Тренировка дальнего боя — уровень {lvl}|r", "upgrade", "R0GW", f"name{lvl}")
        add_update(sid_t, f"|cffe4cfa3Тренировка дальнего боя — уровень {lvl}|r", "upgrade", "R0GW", f"tip{lvl}")
    add_update(42382, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Улучшает точность и урон стрелковых подразделений Альянса.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- Стрелкам дальнего боя.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3/3|r."
    ), "upgrade", "R0GW", "ubertip3")

    # Workshop: R0GY (Комплектование техники)
    add_update(29560, "|cffe4cfa3Комплектование техники — уровень 1|r", "upgrade", "R0GY", "name1")
    add_update(29561, "|cffe4cfa3Комплектование техники — уровень 1|r", "upgrade", "R0GY", "tip1")
    add_update(29562, "|cffe4cfa3Комплектование техники — уровень 2|r", "upgrade", "R0GY", "name2")
    add_update(29563, "|cffe4cfa3Комплектование техники — уровень 2|r", "upgrade", "R0GY", "tip2")
    add_update(29564, "|cffe4cfa3Комплектование техники — уровень 3|r", "upgrade", "R0GY", "name3")
    add_update(29565, "|cffe4cfa3Комплектование техники — уровень 3|r", "upgrade", "R0GY", "tip3")

    # Sanctuary: R0HU (Обучение специализированных магов)
    add_update(30250, "|cffe4cfa3Обучение специализированных магов — уровень 1|r", "upgrade", "R0HU", "name1")
    add_update(30251, "|cffe4cfa3Обучение специализированных магов — уровень 1|r", "upgrade", "R0HU", "tip1")
    add_update(30252, "|cffe4cfa3Обучение специализированных магов — уровень 2|r", "upgrade", "R0HU", "name2")
    add_update(30253, "|cffe4cfa3Обучение специализированных магов — уровень 2|r", "upgrade", "R0HU", "tip2")

    # Rhpt: Обучение боевых магов
    add_update(42376, "|cffe4cfa3Обучение боевых магов — уровень 1|r", "upgrade", "Rhpt", "name1")
    add_update(42378, "|cffe4cfa3Обучение боевых магов — уровень 1|r", "upgrade", "Rhpt", "tip1")
    add_update(42377, "|cffe4cfa3Обучение боевых магов — уровень 2|r", "upgrade", "Rhpt", "name2")
    add_update(42379, "|cffe4cfa3Обучение боевых магов — уровень 2|r", "upgrade", "Rhpt", "tip2")

    # Rhst: Обучение магов поддержки
    add_update(41898, "|cffe4cfa3Обучение магов поддержки — уровень 1|r", "upgrade", "Rhst", "name1")
    add_update(42372, "|cffe4cfa3Обучение магов поддержки — уровень 1|r", "upgrade", "Rhst", "tip1")
    add_update(42235, "|cffe4cfa3Обучение магов поддержки — уровень 2|r", "upgrade", "Rhst", "name2")
    add_update(42375, "|cffe4cfa3Обучение магов поддержки — уровень 2|r", "upgrade", "Rhst", "tip2")

    # Rhse: Магический страж
    add_update(40196, "|cffe4cfa3Магический страж|r", "upgrade", "Rhse", "name1")
    add_update(40197, "|cffe4cfa3Магический страж|r (|cffffffffS|r)", "upgrade", "Rhse", "tip1")

    # Blacksmith: Rhme, Rhar, Rhla, Rhra, R0HO
    # Rhme: Мифриловые мечи (6 уровней)
    rhme_names = [33172, 33726, 32096, 33821, 35188, 35191]
    rhme_tips = [35367, 35759, 35760, 35761, 35762, 35763]
    rhme_ubs = [35764, 35791, 35792, 35793, 35794, 35795]
    for idx in range(6):
        lvl = idx + 1
        add_update(rhme_names[idx], f"|cffe4cfa3Мифриловые мечи — уровень {lvl}|r", "upgrade", "Rhme", f"name{lvl}")
        add_update(rhme_tips[idx], f"|cffe4cfa3Мифриловые мечи — уровень {lvl}|r", "upgrade", "Rhme", f"tip{lvl}")
        add_update(rhme_ubs[idx], (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон всех воинов ближнего боя Альянса.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Воинам ближнего боя.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        ), "upgrade", "Rhme", f"ubertip{lvl}")

    # Rhra: Улучшенные снаряды (6 уровней)
    rhra_names = [35958, 36235, 35796, 37954, 38715, 38716]
    rhra_tips = [38717, 38718, 38724, 38728, 38729, 38730]
    rhra_ubs = [38731, 38732, 39218, 39219, 39220, 39221]
    for idx in range(6):
        lvl = idx + 1
        add_update(rhra_names[idx], f"|cffe4cfa3Улучшенные снаряды — уровень {lvl}|r", "upgrade", "Rhra", f"name{lvl}")
        add_update(rhra_tips[idx], f"|cffe4cfa3Улучшенные снаряды — уровень {lvl}|r", "upgrade", "Rhra", f"tip{lvl}")
        add_update(rhra_ubs[idx], (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон стрелков, осадных машин и кораблей Альянса.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Бойцам дальнего боя.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r."
        ), "upgrade", "Rhra", f"ubertip{lvl}")

    # Rhla: Доспехи из армированной кожи (6 уровней)
    rhla_tips = [41289, 41496, 41805, 41823, 41824, 41851]
    for idx in range(6):
        lvl = idx + 1
        add_update(rhla_tips[idx], f"|cffe4cfa3Доспехи из армированной кожи — уровень {lvl}|r", "upgrade", "Rhla", f"tip{lvl}")

    # Lumber mill: Rhlh, Rhac
    # Rhac: Улучшенная кладка (3 уровня)
    rhac_names = [10539, 10540, 10545]
    rhac_tips = [28189, 28190, 28191]
    for idx in range(3):
        lvl = idx + 1
        add_update(rhac_names[idx], f"|cffe4cfa3Улучшенная кладка — уровень {lvl}|r", "upgrade", "Rhac", f"name{lvl}")
        add_update(rhac_tips[idx], f"|cffe4cfa3Улучшенная кладка — уровень {lvl}|r", "upgrade", "Rhac", f"tip{lvl}")

    # Rhlh: Улучшенная лесозаготовка (6 уровней)
    rhlh_tips = [28488, 28489, 28490, 28491, 28492, 28493]
    for idx in range(6):
        lvl = idx + 1
        add_update(rhlh_tips[idx], f"|cffe4cfa3Улучшенная лесозаготовка — уровень {lvl}|r", "upgrade", "Rhlh", f"tip{lvl}")

    # Shipyard Upgrades: R005, R006, R007, R002, R003
    # R005: Обстрел
    add_update(29871, "|cffe4cfa3Обстрел — уровень 1|r", "upgrade", "R005", "name1")
    add_update(29872, "|cffe4cfa3Обстрел — уровень 1|r (|cffffffffX|r)", "upgrade", "R005", "tip1")
    # R006: Дополнительные паруса
    add_update(29873, "|cffe4cfa3Дополнительные паруса — уровень 1|r", "upgrade", "R006", "name1")
    add_update(29874, "|cffe4cfa3Дополнительные паруса — уровень 1|r (|cffffffffC|r)", "upgrade", "R006", "tip1")
    # R007: Починка
    add_update(29875, "|cffe4cfa3Починка — уровень 1|r", "upgrade", "R007", "name1")
    add_update(29876, "|cffe4cfa3Починка — уровень 1|r (|cffffffffD|r)", "upgrade", "R007", "tip1")
    # R002: Орудия флота
    add_update(29867, "|cffe4cfa3Орудия флота — уровень 1|r", "upgrade", "R002", "name1")
    add_update(29868, "|cffe4cfa3Орудия флота — уровень 1|r (|cffffffffA|r)", "upgrade", "R002", "tip1")
    # R003: Укреплённый корпус
    add_update(29869, "|cffe4cfa3Укреплённый корпус — уровень 1|r", "upgrade", "R003", "name1")
    add_update(29870, "|cffe4cfa3Укреплённый корпус — уровень 1|r (|cffffffffS|r)", "upgrade", "R003", "tip1")

    # =========================================================================
    # 6. ABILITIES (alliance_abilities.json)
    # =========================================================================
    # Standardize all abilities in dump['abilities'] that have TRIGSTR
    # Hero spells:
    # A1PT: Массовое исцеление
    add_update(41917, "|cffe4cfa3Массовое исцеление|r", "ability", "A1PT", "name")
    add_update(42367, "|cffe4cfa3Массовое исцеление|r", "ability", "A1PT", "researchtip")
    add_update(42307, "|cffe4cfa3Массовое исцеление|r", "ability", "A1PT", "tip1")
    add_update(42309, "|cffe4cfa3Массовое исцеление|r", "ability", "A1PT", "tip2")
    add_update(42368, "|cffe4cfa3Массовое исцеление|r", "ability", "A1PT", "tip3")
    add_update(42395, "|cffe4cfa3Массовое исцеление|r", "ability", "A1PT", "tip4")

    # A1PS: Аура света
    add_update(40282, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает находящимся рядом союзникам здоровье со скоростью |cffffffff100%|cffced4da от базовой.|r", "ability", "A1PS", "ubertip1")
    add_update(40283, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает находящимся рядом союзникам здоровье со скоростью |cffffffff150%|cffced4da от базовой.|r", "ability", "A1PS", "ubertip2")
    add_update(40284, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает находящимся рядом союзникам здоровье со скоростью |cffffffff200%|cffced4da от базовой.|r", "ability", "A1PS", "ubertip3")
    add_update(40274, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает находящимся рядом союзникам здоровье со скоростью |cffffffff250%|cffced4da от базовой.|r", "ability", "A1PS", "ubertip4")

    # alA0: Ударная волна (Гаритос)
    add_update(39922, "|cffe4cfa3Ударная волна|r", "ability", "alA0", "name")
    add_update(39921, "|cffe4cfa3Ударная волна|r", "ability", "alA0", "researchtip")

    # Now let's loop over all abilities and upgrades in dump to ensure every single
    # raw TRIGSTR field has a standardized replacement that respects all style rules!
    for a in dump['abilities']:
        aid = a['id']
        # Name
        if a.get('raw_name', '').startswith('TRIGSTR_'):
            sid = int(a['raw_name'][8:])
            if sid not in wts_updates:
                clean_n = clean_title(a.get('name') or aid)
                add_update(sid, f"|cffe4cfa3{clean_n}|r", "ability", aid, "name")
        # Research tip
        if (a.get('raw_researchtip') or '').startswith('TRIGSTR_'):
            sid = int(a['raw_researchtip'][8:])
            if sid not in wts_updates:
                clean_rt = clean_title(a.get('researchtip') or a.get('name') or aid)
                add_update(sid, f"|cffe4cfa3{clean_rt}|r", "ability", aid, "researchtip")
        # Tips
        for k, v in a.get('tips', {}).items():
            if (v.get('raw') or '').startswith('TRIGSTR_'):
                sid = int(v['raw'][8:])
                if sid not in wts_updates:
                    clean_t = clean_title(v.get('val') or a.get('name') or aid)
                    add_update(sid, f"|cffe4cfa3{clean_t}|r", "ability", aid, k)
        # Ubertips
        for k, v in a.get('ubertips', {}).items():
            if (v.get('raw') or '').startswith('TRIGSTR_'):
                sid = int(v['raw'][8:])
                if sid not in wts_updates:
                    val = clean_body_text(v.get('val') or "")
                    if not val.startswith("|cffa6afb8СПОСОБНОСТЬ:"):
                        val = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da {val}|r"
                    add_update(sid, val, "ability", aid, k)

    # Upgrades remaining TRIGSTRs
    for up in dump['upgrades']:
        uid = up['id']
        for k, v in up.get('names', {}).items():
            if (v.get('raw') or '').startswith('TRIGSTR_'):
                sid = int(v['raw'][8:])
                if sid not in wts_updates:
                    clean_n = clean_title(v.get('val') or uid)
                    add_update(sid, f"|cffe4cfa3{clean_n}|r", "upgrade", uid, k)
        for k, v in up.get('tips', {}).items():
            if (v.get('raw') or '').startswith('TRIGSTR_'):
                sid = int(v['raw'][8:])
                if sid not in wts_updates:
                    clean_t = clean_title(v.get('val') or uid)
                    add_update(sid, f"|cffe4cfa3{clean_t}|r", "upgrade", uid, k)
        for k, v in up.get('ubertips', {}).items():
            if (v.get('raw') or '').startswith('TRIGSTR_'):
                sid = int(v['raw'][8:])
                if sid not in wts_updates:
                    val = clean_body_text(v.get('val') or "")
                    if not val.startswith("|cffa6afb8ИССЛЕДОВАНИЕ:"):
                        val = f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da {val}|r"
                    add_update(sid, val, "upgrade", uid, k)

    # Buffs remaining TRIGSTRs
    for bf in dump['buffs']:
        bid = bf['id']
        if (bf.get('raw_bufftip') or '').startswith('TRIGSTR_'):
            sid = int(bf['raw_bufftip'][8:])
            if sid not in wts_updates:
                clean_t = clean_title(bf.get('bufftip') or bid)
                add_update(sid, f"|cffe4cfa3{clean_t}|r", "buff", bid, "bufftip")
        if (bf.get('raw_buffubertip') or '').startswith('TRIGSTR_'):
            sid = int(bf['raw_buffubertip'][8:])
            if sid not in wts_updates:
                val = clean_body_text(bf.get('buffubertip') or "")
                if not val.startswith("|cffa6afb8ЭФФЕКТ:"):
                    val = f"|cffa6afb8ЭФФЕКТ:|cffced4da {val}|r"
                add_update(sid, val, "buff", bid, "buffubertip")
        if (bf.get('raw_editorname') or '').startswith('TRIGSTR_'):
            sid = int(bf['raw_editorname'][8:])
            if sid not in wts_updates:
                clean_n = clean_title(bf.get('editorname') or bid)
                add_update(sid, f"|cffe4cfa3{clean_n}|r", "buff", bid, "editorname")

    # Units remaining TRIGSTRs
    for u in dump['units']:
        uid = u['id']
        if (u.get('raw_name') or '').startswith('TRIGSTR_'):
            sid = int(u['raw_name'][8:])
            if sid not in wts_updates:
                clean_n = clean_title(u.get('name') or uid)
                add_update(sid, f"|cffe4cfa3{clean_n}|r", "unit", uid, "name")
        if (u.get('raw_tip') or '').startswith('TRIGSTR_'):
            sid = int(u['raw_tip'][8:])
            if sid not in wts_updates:
                clean_t = clean_title(u.get('tip') or u.get('name') or uid)
                add_update(sid, f"|cffe4cfa3{clean_t}|r", "unit", uid, "tip")
        if (u.get('raw_ubertip') or '').startswith('TRIGSTR_'):
            sid = int(u['raw_ubertip'][8:])
            if sid not in wts_updates:
                val = clean_body_text(u.get('ubertip') or "")
                if not val.startswith("|cffa6afb8ЮНИТ:"):
                    val = f"|cffa6afb8ЮНИТ:|cffced4da {val}|r"
                add_update(sid, val, "unit", uid, "ubertip")

    # =========================================================================
    # 7. EXPORT REGISTRIES AND PLAN
    # =========================================================================
    out_dir = ROOT / "docs/ui_text"
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. alliance_selection.json
    sel_data = {
        "scope": "Альянс (Alliance): подсказка выбора расы A02A и маркеры",
        "object": "A02A",
        "variants": ["SD"],
        "hotkey": {"value": "Q"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Alliance регистрирует способность A02A.",
            "При выборе создаются 5 рабочих hpea, исследуются маркеры R0GZ, R0HX, R0HW, R0HY, R0KK, удаляется выбирающий юнит.",
            "Горячая клавиша Q, создатель VinerX, куратор Wks, сложность 4/5 (●●●●○), период «Classic — Legion»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38859, "after": wts_updates[38859]},
            {"field": "tip1", "wts_id": 38860, "after": wts_updates[38860]},
            {"field": "ubertip1", "wts_id": 41059, "after": wts_updates[41059]}
        ],
        "markers": [
            {
                "id": "R0GZ", "name": "Альянс (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 29663, "after": wts_updates.get(29663)},
                    {"field": "tip1", "wts_id": 29677, "after": wts_updates.get(29677)},
                    {"field": "ubertip1", "wts_id": 29705, "after": wts_updates.get(29705)}
                ]
            },
            {
                "id": "R0HX", "name": "Кул-Тирас или Альянс",
                "strings": [
                    {"field": "name1", "wts_id": 30266, "after": wts_updates.get(30266)},
                    {"field": "tip1", "wts_id": 29942, "after": wts_updates.get(29942)}
                ]
            },
            {
                "id": "R0HW", "name": "Гномы",
                "strings": [
                    {"field": "name1", "wts_id": 30254, "after": wts_updates.get(30254)},
                    {"field": "tip1", "wts_id": 29941, "after": wts_updates.get(29941)}
                ]
            },
            {
                "id": "R0HY", "name": "Стромгард или Альянс",
                "strings": [
                    {"field": "name1", "wts_id": 30278, "after": wts_updates.get(30278)},
                    {"field": "tip1", "wts_id": 30255, "after": wts_updates.get(30255)}
                ]
            },
            {
                "id": "R0KK", "name": "Альянс или Даларан",
                "strings": [
                    {"field": "name1", "wts_id": 16408, "after": wts_updates.get(16408)},
                    {"field": "tip1", "wts_id": 16409, "after": wts_updates.get(16409)},
                    {"field": "ubertip1", "wts_id": 16416, "after": wts_updates.get(16416)}
                ]
            }
        ]
    }
    (out_dir / "alliance_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 2. alliance_buildings.json
    bld_entries = []
    for b in dump["buildings"]:
        bid = b["id"]
        b_strings = []
        for f in ["name", "tip", "ubertip"]:
            raw = b.get(f"raw_{f}")
            if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
                try:
                    sid = int(raw[8:])
                    if sid in wts_updates:
                        b_strings.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
                except ValueError:
                    pass
        bld_entries.append({"id": bid, "hotkey": b.get("hotkey"), "strings": b_strings})
    bld_data = {
        "scope": f"Альянс (Alliance): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (out_dir / "alliance_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 3. alliance_heroes.json
    hero_entries = []
    for h in dump["heroes"]:
        hid = h["id"]
        h_strings = []
        for f in ["name", "propernames", "tip", "ubertip", "awakentip", "revivetip"]:
            raw = h.get(f"raw_{f}")
            if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
                try:
                    sid = int(raw[8:])
                    if sid in wts_updates:
                        h_strings.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
                except ValueError:
                    pass
        hero_entries.append({"id": hid, "hotkey": h.get("hotkey"), "strings": h_strings})
    hero_data = {
        "scope": f"Альянс (Alliance): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (out_dir / "alliance_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 4. alliance_units.json
    unit_entries = []
    for u in dump["units"]:
        uid = u["id"]
        u_strings = []
        for f in ["name", "tip", "ubertip"]:
            raw = u.get(f"raw_{f}")
            if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
                try:
                    sid = int(raw[8:])
                    if sid in wts_updates:
                        u_strings.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
                except ValueError:
                    pass
        unit_entries.append({"id": uid, "hotkey": u.get("hotkey"), "strings": u_strings})
    unit_data = {
        "scope": f"Альянс (Alliance): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (out_dir / "alliance_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 5. alliance_research.json
    upg_entries = []
    for up in dump["upgrades"]:
        uid = up["id"]
        up_strings = []
        for d_name in ["names", "tips", "ubertips"]:
            for k, v in up.get(d_name, {}).items():
                raw = v.get("raw")
                if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
                    try:
                        sid = int(raw[8:])
                        if sid in wts_updates:
                            up_strings.append({"field": f"{d_name}_{k}", "wts_id": sid, "after": wts_updates[sid]})
                    except ValueError:
                        pass
        upg_entries.append({"id": uid, "levels": up.get("levels", 1), "strings": up_strings})
    upg_data = {
        "scope": f"Альянс (Alliance): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (out_dir / "alliance_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 6. alliance_abilities.json
    abil_entries = []
    for a in dump["abilities"]:
        aid = a["id"]
        a_strings = []
        for f in ["name", "researchtip", "researchubertip"]:
            raw = a.get(f"raw_{f}")
            if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
                try:
                    sid = int(raw[8:])
                    if sid in wts_updates:
                        a_strings.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
                except ValueError:
                    pass
        for d_name in ["tips", "ubertips"]:
            for k, v in a.get(d_name, {}).items():
                raw = v.get("raw")
                if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
                    try:
                        sid = int(raw[8:])
                        if sid in wts_updates:
                            a_strings.append({"field": f"{d_name}_{k}", "wts_id": sid, "after": wts_updates[sid]})
                    except ValueError:
                        pass
        abil_entries.append({"id": aid, "levels": a.get("levels", 1), "strings": a_strings})
    abil_data = {
        "scope": f"Альянс (Alliance): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (out_dir / "alliance_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 7. alliance_audit.json
    audit_data = {
        "race": "Альянс (Alliance)",
        "race_id": 29,
        "selection_ability": "A02A",
        "objects_audit": {
            "buildings": {"count": len(dump["buildings"]), "ids": [b["id"] for b in dump["buildings"]]},
            "heroes": {"count": len(dump["heroes"]), "ids": [h["id"] for h in dump["heroes"]]},
            "units": {"count": len(dump["units"]), "ids": [u["id"] for u in dump["units"]]},
            "abilities": {"count": len(dump["abilities"])},
            "researches": {"count": len(dump["upgrades"])}
        },
        "items_audit": {
            "race_specific_items": ["I020"],
            "status": "I020 (Руна иллюзий дамми) used by spell A1A5 for creating illusions."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific floating messages found in war3map.wts for Alliance."
        },
        "buffs_audit": {
            "custom_buffs_count": len(dump["buffs"]),
            "status": "Standardized all custom buffs referenced by Alliance abilities."
        },
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def)
    }
    (out_dir / "alliance_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 8. alliance_plan.json
    plan_data = {
        "race": "Alliance",
        "race_id": 29,
        "total_updates": len(wts_updates),
        "wts_updates": wts_updates,
        "checks_def": checks_def
    }
    (out_dir / "alliance_plan.json").write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Alliance plan prepared successfully:")
    print(f"  Total WTS updates: {len(wts_updates)}")
    print(f"  Total checks: {len(checks_def)}")
    print(f"Saved plan and categories to {out_dir}")

if __name__ == '__main__':
    main()
