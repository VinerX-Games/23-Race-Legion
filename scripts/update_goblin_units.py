# -*- coding: utf-8 -*-
"""Update all 24 Goblin units with SD validation and artifacts."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wc3_hivewe as hw
from apply_faceless_object_text import patch_blob

def update_wts_string(wts_content: str, string_id: int, new_val: str) -> str:
    pattern = rf"(STRING 0*{string_id}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})"
    match = re.search(pattern, wts_content)
    if not match:
        raise ValueError(f"STRING {string_id} not found in WTS")
    return re.sub(pattern, rf"\g<1>{new_val}\g<3>", wts_content, count=1)

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)
    wts_path = ROOT / "map.w3x/war3map.wts"
    skin_u_path = ROOT / "map.w3x/war3mapSkin.w3u"

    original_hashes = {
        "wts": hashlib.sha256(wts_path.read_bytes()).hexdigest(),
        "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
        "w3u_skin": hashlib.sha256(skin_u_path.read_bytes()).hexdigest(),
        "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
        "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
        "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
        "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
        "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
        "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
    }

    wts_updates = {
        # n00V: Крошшер (Q)
        14109: "|cffe4cfa3Крошшер|r",
        14193: "|cffe4cfa3Крошшер|r (|cffffffffQ|r)",
        24374: "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый рабочий механизм картеля. Добывает древесину, возводит сооружения и ремонтирует технику.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deСкачок|r: мгновенно перемещается на короткую дистанцию.|n- |cffa9c7deРемонт|r: чинит повреждённые здания и технику за ресурсы.|n- |cffa9c7deСбор ресурсов|r: быстро спиливает деревья и добывает древесину.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h06K: Рекрут ТК (Q)
        14118: "|cffe4cfa3Рекрут ТК|r",
        14119: "|cffe4cfa3Рекрут ТК|r (|cffffffffQ|r)",
        13914: "|cffa6afb8ЮНИТ:|cffced4da Базовый стрелок картеля. Ведёт беглый огонь из самодельного карабина и забрасывает врагов зажигательными смесями.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deКоктейль Молотова|r: бросает зажигательную смесь, поджигающую область на земле.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06L: Пулеметчик (W)
        18717: "|cffe4cfa3Пулеметчик|r",
        19269: "|cffe4cfa3Пулеметчик|r (|cffffffffW|r)",
        13919: "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый стрелок поддержки. Ведёт непрерывный скорострельный огонь из станкового пулемёта, подавляя скопления пехоты.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06M: Снайпер (E)
        14122: "|cffe4cfa3Снайпер|r",
        14123: "|cffe4cfa3Снайпер|r (|cffffffffE|r)",
        19267: "|cffa6afb8ЮНИТ:|cffced4da Дальнобойный стрелок-ликвидатор. Оснащён высокоточной оптической винтовкой и поражает ключевые цели с предельной дистанции.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06N: Ракетчик (R)
        14124: "|cffe4cfa3Ракетчик|r",
        14125: "|cffe4cfa3Ракетчик|r (|cffffffffR|r)",
        14132: "|cffa6afb8ЮНИТ:|cffced4da Осадный стрелок картеля. Запускает реактивные фугасные снаряды, наносящие разрушительный осадный урон по площади.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deСамоподрыв|r: при критических повреждениях взрывается, нанося урон окружающим.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06O: Медик (S)
        14100: "|cffe4cfa3Медик|r",
        14101: "|cffe4cfa3Медик|r (|cffffffffS|r)",
        38178: "|cffa6afb8ЮНИТ:|cffced4da Полевой специалист поддержки. Исцеляет раненых бойцов направленным энергетическим лучом.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deЛечение|r: непрерывно восстанавливает здоровье союзных органических бойцов.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06Q: Огнеметчик (A)
        14102: "|cffe4cfa3Огнеметчик|r",
        14103: "|cffe4cfa3Огнеметчик|r (|cffffffffA|r)",
        17472: "|cffa6afb8ЮНИТ:|cffced4da Штурмовой боец ближнего боя. Заливает вражеские ряды горючей смесью, нанося магический урон и поджигая цели.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deПоджог|r: воспламеняет врагов, нанося периодический урон огнём.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h078: Сапер (D)
        14155: "|cffe4cfa3Сапер|r",
        14156: "|cffe4cfa3Сапер|r (|cffffffffD|r)",
        38396: "|cffa6afb8ЮНИТ:|cffced4da Инженер-диверсант. Устанавливает скрытые фугасные мины и способен подорвать себя ради уничтожения укреплений врага.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deУстановить мину|r: закапывает скрытую противопехотную мину.|n- |cffa9c7deБа-бах!|r: взрывает заряд взрывчатки, нанося колоссальный урон по области ценой своей жизни.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h07R: Огр-Костолом (Z)
        30212: "|cffe4cfa3Огр-Костолом|r",
        30283: "|cffe4cfa3Огр-Костолом|r (|cffffffffZ|r)",
        38397: "|cffa6afb8ЮНИТ:|cffced4da Наёмный тяжелый пехотинец ближнего боя. Обладает огромным запасом здоровья и сдерживает натиск врага на передовой.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h06S: Огнестрельный танк «Напалм-4000» (R)
        14190: "|cffe4cfa3Огнестрельный танк «Напалм-4000»|r",
        14130: "|cffe4cfa3Огнестрельный танк «Напалм-4000»|r (|cffffffffR|r)",
        38185: "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый огнемётный танк. Выжигает передовые порядки противника потоками напалма и способен кратковременно ускоряться.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deПоджог|r: воспламеняет цели струями горючей смеси.|n- |cffa9c7deУскорение|r: временно увеличивает скорость передвижения танка.|n- |cffa9c7deДетонация|r: взрывается при уничтожении, нанося урон врагам поблизости.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h06U: Вездеход «Мурлок-3000» (W)
        14133: "|cffe4cfa3Вездеход «Мурлок-3000»|r",
        14134: "|cffe4cfa3Вездеход «Мурлок-3000»|r (|cffffffffW|r)",
        19186: "|cffa6afb8ЮНИТ:|cffced4da Универсальная боевая машина-амфибия. Способна свободно передвигаться как по суше, так и по воде, ведя огонь из скорострельной пушки.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deДетонация|r: взрывается при уничтожении, поражая окружающих.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06Y: Мобильная артиллерия (E)
        14105: "|cffe4cfa3Мобильная артиллерия|r",
        14106: "|cffe4cfa3Мобильная артиллерия|r (|cffffffffE|r)",
        19291: "|cffa6afb8ЮНИТ:|cffced4da Самоходная артиллерийская установка. Ведёт огонь крупнокалиберными снарядами на дальние дистанции и может закрепиться на позиции.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deЗакрепиться|r: переходит в стационарный осадный режим с повышенной дальностью стрельбы.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06Z: Мобильная артиллерия (осадный режим) (E)
        14107: "|cffe4cfa3Мобильная артиллерия|r",
        14108: "|cffe4cfa3Мобильная артиллерия|r (|cffffffffE|r)",

        # h06R: БРДМ-2000 (Q)
        14128: "|cffe4cfa3БРДМ-2000|r",
        14129: "|cffe4cfa3БРДМ-2000|r (|cffffffffQ|r)",
        19300: "|cffa6afb8ЮНИТ:|cffced4da Быстроходная бронированная машина картеля. Перевозит пехотные отряды под защитой брони и прикрывает высадку пулемётным огнём.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deТранспортировка|r: вмещает и защищает до 4 пехотинцев.|n- |cffa9c7deУскорение|r: временно увеличивает скорость движения.|n- |cffa9c7deДетонация|r: взрывается при уничтожении.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06T: Штурмовой танк «Вепрь-5000» (A)
        14131: "|cffe4cfa3Штурмовой танк «Вепрь-5000»|r",
        2767:  "|cffe4cfa3Штурмовой танк «Вепрь-5000»|r (|cffffffffA|r)",
        18786: "|cffa6afb8ЮНИТ:|cffced4da Сверхтяжёлый танк прорыва. Обладает толстой лобовой бронёй и мощным орудием, подавляющим любые наземные и воздушные силы.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deУскорение|r: кратковременно форсирует двигатель танка.|n- |cffa9c7deДетонация|r: взрывается при гибели машины.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # o00W: Меха «Линчеватель-6000» (E)
        14104: "|cffe4cfa3Меха «Линчеватель-6000»|r",
        6489:  "|cffe4cfa3Меха «Линчеватель-6000»|r (|cffffffffE|r)",
        19266: "|cffa6afb8ЮНИТ:|cffced4da Шагающий боевой робот ближнего боя. Оснащён гидравлическими клешнями и пилами, крушащими броню вражеской техники.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deДетонация|r: взрывается при критическом уроне.|r|n|n|cffced4daАтакует наземные цели.|r",

        # o00Y: Оператор силовой брони (Q)
        14191: "|cffe4cfa3Оператор силовой брони|r",
        14192: "|cffe4cfa3Оператор силовой брони|r (|cffffffffQ|r)",
        19268: "|cffa6afb8ЮНИТ:|cffced4da Элитный штурмовик в тяжёлом экзоскелете. Наносит сокрушительные удары в ближнем бою, оглушая врагов силовой дубиной.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deСильный удар|r: шанс нанести дополнительный урон и оглушить цель при атаке.|r|n|n|cffced4daАтакует наземные цели.|r",

        # o00X: Огнемеха «Пожар-7000» (R)
        14141: "|cffe4cfa3Огнемеха «Пожар-7000»|r",
        14142: "|cffe4cfa3Огнемеха «Пожар-7000»|r (|cffffffffR|r)",
        38189: "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый шагающий механизм с двумя огнемётными установками. Заливает поле боя огненными вихрями и поджигает позиции противника.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deПоджог|r: воспламеняет вражеские цели потоками пламени.|n- |cffa9c7deДетонация|r: взрывается при разрушении корпуса.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h06P: Супербоец (W)
        14126: "|cffe4cfa3Супербоец|r",
        14127: "|cffe4cfa3Супербоец|r (|cffffffffW|r)",
        17467: "|cffa6afb8ЮНИТ:|cffced4da Элитный диверсант картеля, усиленный мутагенами. Применяет технологичные гранаты, турели и стимуляторы в бою.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deОгнемётная турель|r: разворачивает автономную турель с огнемётом.|n- |cffa9c7deЭМИ-граната|r: выжигает ману и парализует призванных существ и технику.|n- |cffa9c7deАдреналиновые инъекции|r: временно увеличивает скорость атаки и бега.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r",

        # h06X: Универсальный линкор (Q)
        14139: "|cffe4cfa3Универсальный линкор|r",
        14140: "|cffe4cfa3Универсальный линкор|r (|cffffffffQ|r)",
        21614: "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый флагманский корабль картеля. Перевозит войска, прикрывает десант мощной дальнобойной артиллерией и берет корабли на абордаж.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deФорсаж|r: кратковременно повышает скорость хода.|n- |cffa9c7deАбордаж!|r: захватывает вражеский корабль в ближнем морском бою.|n- |cffa9c7deТранспортировка|r: перевозит сухопутные отряды картеля.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h06V: Субмарина (E)
        14135: "|cffe4cfa3Субмарина|r",
        14136: "|cffe4cfa3Субмарина|r (|cffffffffE|r)",
        21612: "|cffa6afb8ЮНИТ:|cffced4da Тяжёлое подводное судно картеля. Ведёт дальнобойную бомбардировку береговых укреплений и кораблей противника из полупогружённого состояния.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deФорсаж|r: временно увеличивает скорость хода.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h06W: Подводная лодка (R)
        14137: "|cffe4cfa3Подводная лодка|r",
        14138: "|cffe4cfa3Подводная лодка|r (|cffffffffR|r)",
        21613: "|cffa6afb8ЮНИТ:|cffced4da Торпедный боевой корабль картеля. Атакует цели на поверхности и способна полностью погружаться под воду для скрытного маневрирования.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deФорсаж|r: ускоряет ход лодки.|n- |cffa9c7deПогрузиться|r: уходит под воду, становясь невидимой для обычного обзора.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h0DM: Подводная лодка (подводная) (R)
        14188: "|cffe4cfa3Подводная лодка|r",
        14189: "|cffe4cfa3Подводная лодка|r (|cffffffffR|r)",
        10900: "|cffa6afb8ЮНИТ:|cffced4da Торпедный боевой корабль картеля в подводном режиме. Постоянно скрыта под водой и незаметна для противников без детекторов невидимости.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deФорсаж|r: кратковременно ускоряет движение.|n- |cffa9c7deВсплыть|r: поднимается на поверхность воды.|r|n|n|cffced4daАтакует наземные цели.|r",

        # h0OD: Нефтяной танкер (A)
        34845: "|cffe4cfa3Нефтяной танкер|r",
        39480: "|cffe4cfa3Нефтяной танкер|r (|cffffffffA|r)",
        22697: "|cffa6afb8ЮНИТ:|cffced4da Специализированное судно обеспечения. Возводит морские нефтяные вышки и доставляет ресурсы на верфи картеля.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deФорсаж|r: кратковременно повышает скорость движения судна.|r|n|n|cffced4daАтакует наземные цели.|r",
    }

    # Patch h06Z ubertip in war3mapSkin.w3u
    h06z_ubertip = "|cffa6afb8ЮНИТ:|cffced4da Самоходная артиллерийская установка в стационарном режиме. Ведёт сокрушительный залповый огонь по укреплениям и скоплениям врага.|r|n|n|cffa6afb8Способности:|r|n- |cffa9c7deСняться с позиции|r: возвращается в мобильный походный режим.|r|n|n|cffced4daАтакует наземные и воздушные цели.|r"
    skin_ops = [
        {"id": "h06Z", "field": "ubertip", "value": h06z_ubertip}
    ]

    print(f"Applying {len(wts_updates)} WTS updates for Goblin units...")
    wts_content = wts_path.read_text(encoding="utf-8")
    for sid, new_val in sorted(wts_updates.items()):
        wts_content = update_wts_string(wts_content, sid, new_val)

    wts_path.write_text(wts_content, encoding="utf-8")
    new_wts_hash = hashlib.sha256(wts_path.read_bytes()).hexdigest()
    print("WTS updated successfully.")

    print(f"Patching h06Z inline ubertip in war3mapSkin.w3u...")
    patched_blob, changed = patch_blob(skin_u_path.read_bytes(), skin_ops, "unit", add_missing=True)
    skin_u_path.write_bytes(patched_blob)
    new_skin_hash = hashlib.sha256(skin_u_path.read_bytes()).hexdigest()
    print(f"war3mapSkin.w3u patched ({len(changed)} mods changed).")

    # Reset HiveWE cache
    hw._WTS_CACHE = None
    hw._WTS_CACHE_KEY = None
    wts_dict = hw.load_wts_strings()
    resolve = lambda s: wts_dict.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    unit_keys = {
        "n00V": (14109, 14193, 24374),
        "h06K": (14118, 14119, 13914),
        "h06L": (18717, 19269, 13919),
        "h06M": (14122, 14123, 19267),
        "h06N": (14124, 14125, 14132),
        "h06O": (14100, 14101, 38178),
        "h06Q": (14102, 14103, 17472),
        "h078": (14155, 14156, 38396),
        "h07R": (30212, 30283, 38397),
        "h06S": (14190, 14130, 38185),
        "h06U": (14133, 14134, 19186),
        "h06Y": (14105, 14106, 19291),
        "h06Z": (14107, 14108, None),
        "h06R": (14128, 14129, 19300),
        "h06T": (14131, 2767, 18786),
        "o00W": (14104, 6489, 19266),
        "o00Y": (14191, 14192, 19268),
        "o00X": (14141, 14142, 38189),
        "h06P": (14126, 14127, 17467),
        "h06X": (14139, 14140, 21614),
        "h06V": (14135, 14136, 21612),
        "h06W": (14137, 14138, 21613),
        "h0DM": (14188, 14189, 10900),
        "h0OD": (34845, 39480, 22697),
    }

    checks = []
    for uid, (nid, tid, ubid) in unit_keys.items():
        res = hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", uid])
        if not res.get("ok"):
            raise RuntimeError(f"Failed to fetch {uid}: {res}")
        f = res.get("object", {}) or res.get("fields", {})
        actual_name = resolve(f.get("name"))
        actual_tip = resolve(f.get("tip"))
        actual_ubertip = resolve(f.get("ubertip"))

        expected_name = wts_updates[nid]
        expected_tip = wts_updates[tid]
        expected_ubertip = h06z_ubertip if uid == "h06Z" else wts_updates[ubid]

        n_ok = (actual_name == expected_name)
        t_ok = (actual_tip == expected_tip)
        u_ok = (actual_ubertip == expected_ubertip)

        checks.append({"id": uid, "field": "name", "expected": expected_name, "actual": actual_name, "ok": n_ok})
        checks.append({"id": uid, "field": "tip", "expected": expected_tip, "actual": actual_tip, "ok": t_ok})
        checks.append({"id": uid, "field": "ubertip", "expected": expected_ubertip, "actual": actual_ubertip, "ok": u_ok})

    all_ok = all(c["ok"] for c in checks)
    print(f"SD Verification checks: {sum(c['ok'] for c in checks)}/{len(checks)} passed.")
    for c in checks:
        if not c["ok"]:
            print(f"  MISMATCH on {c['id']} {c['field']}")

    apply_payload = {
        "race": "Goblins",
        "category": "units",
        "total_units": len(unit_keys),
        "total_fields": len(checks),
        "wts_updated": list(wts_updates.keys()),
        "skin_patch_count": len(skin_ops),
        "hashes_before": original_hashes,
        "hashes_after": {
            "wts": new_wts_hash,
            "w3u": hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest(),
            "w3u_skin": new_skin_hash,
            "w3a": hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest(),
            "w3a_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest(),
            "w3h": hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest(),
            "w3h_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest(),
            "w3q": hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest(),
            "w3q_skin": hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest(),
        },
        "binary_files_unchanged": (
            original_hashes["w3u"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3u").read_bytes()).hexdigest() and
            original_hashes["w3a"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3a").read_bytes()).hexdigest() and
            original_hashes["w3a_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3a").read_bytes()).hexdigest() and
            original_hashes["w3h"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3h").read_bytes()).hexdigest() and
            original_hashes["w3h_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3h").read_bytes()).hexdigest() and
            original_hashes["w3q"] == hashlib.sha256((ROOT / "map.w3x/war3map.w3q").read_bytes()).hexdigest() and
            original_hashes["w3q_skin"] == hashlib.sha256((ROOT / "map.w3x/war3mapSkin.w3q").read_bytes()).hexdigest()
        ),
        "checks": checks,
        "all_checks_passed": all_ok
    }

    with open(folder / "goblins_units_apply.json", "w", encoding="utf-8") as f:
        json.dump(apply_payload, f, ensure_ascii=False, indent=2)

    registry_payload = {
        "scope": "Гоблины (Goblins): категория 2 — Юниты (24 юнита)",
        "units_count": len(unit_keys),
        "variants": ["SD"],
        "units": [
            {
                "id": uid,
                "hotkey": resolve(hw.run_cli_json(["get-object", "--map", str(ROOT / "map.w3x"), "--type", "unit", "--id", uid]).get("object", {}).get("hotkey")),
                "strings": [
                    {"field": "name", "wts_id": nid, "after": wts_updates[nid]},
                    {"field": "tip", "wts_id": tid, "after": wts_updates[tid]},
                    {"field": "ubertip", "wts_id": ubid, "after": h06z_ubertip if uid == "h06Z" else wts_updates[ubid]}
                ]
            }
            for uid, (nid, tid, ubid) in unit_keys.items()
        ]
    }

    with open(folder / "goblins_units.json", "w", encoding="utf-8") as f:
        json.dump(registry_payload, f, ensure_ascii=False, indent=2)

    print("Artifacts generated.")

if __name__ == "__main__":
    main()
