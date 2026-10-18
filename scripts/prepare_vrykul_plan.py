# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Race 36: Vryculs (Врайкулы)."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. RACE SELECTION & MARKERS: A0HP, R07F, R067, R068
    # =========================================================================
    # A0HP: Врайкулы (A)
    wts_updates[38871] = "|cffe4cfa3Врайкулы|r"
    wts_updates[38872] = "|cffe4cfa3Врайкулы|r (|cffffffffA|r)"
    wts_updates[35175] = (
        "|cffa6afb8РАСА:|r |cffced4daМогучие полугиганты Нордскола, свирепые воины и наездники на протодраконах, служащие Королю-личу.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●|r|cffa6afb8○○○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Wrath of the Lich King»|r|n|n"
        "|cffced4daРодина могучих полугигантов врайкулов — Ревущий Фьорд на юго-востоке Нордскола. В древности этот народ создал процветающую цивилизацию, однако затем мистически исчез, оставив пустынные поселения и заброшенные храмы. "
        "Когда в их землях был основан Вальгард, лагерь Альянса, врайкулы пробудились от векового сна. "
        "Под предводительством короля Имирона свирепые воины обрушились на чужеземцев из Крепости Утгард, встав под знамёна Короля-лича.|r"
    )
    checks_def.append({"type": "ability", "id": "A0HP", "field": "name", "expected": wts_updates[38871]})
    checks_def.append({"type": "ability", "id": "A0HP", "field": "tip1", "expected": wts_updates[38872]})
    checks_def.append({"type": "ability", "id": "A0HP", "field": "ubertip1", "expected": wts_updates[35175]})

    # R07F: Маркер расы Врайкулов
    wts_updates[10619] = "|cffe4cfa3Врайкулы|r"
    wts_updates[10620] = "|cffe4cfa3Врайкулы|r"
    wts_updates[20113] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер принадлежности к фракции Врайкулов.|r"
    checks_def.append({"type": "upgrade", "id": "R07F", "field": "name1", "expected": wts_updates[10619]})
    checks_def.append({"type": "upgrade", "id": "R07F", "field": "tip1", "expected": wts_updates[10620]})
    checks_def.append({"type": "upgrade", "id": "R07F", "field": "ubertip1", "expected": wts_updates[20113]})

    # R067: Примкнуть к Королю Личу (D)
    wts_updates[1442] = "|cffe4cfa3Примкнуть к Королю-личу|r"
    wts_updates[1452] = "|cffe4cfa3Примкнуть к Королю-личу|r (|cffffffffD|r)"
    wts_updates[10874] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Врайкулы переходят на сторону Короля-лича, получая тёмную силу в обмен на часть жизненных сил.|n|n"
        "|cffa6afb8Эффект:|r|cffced4da|n"
        "- Урон воинов: |cffc8e087+12|cffced4da ед.|n"
        "- Скорость атаки: |cffc8e087+30%|cffced4da|n"
        "- Восстановление здоровья: |cffc8e087+0,5|cffced4da ед./с|n"
        "- Максимальное здоровье: |cffe69a8d-150|cffced4da ед.|n|n"
        "|cffe6c07bВзаимоисключение: блокирует исследование «Поддерживать верность хранителям».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R067", "field": "name1", "expected": wts_updates[1442]})
    checks_def.append({"type": "upgrade", "id": "R067", "field": "tip1", "expected": wts_updates[1452]})
    checks_def.append({"type": "upgrade", "id": "R067", "field": "ubertip1", "expected": wts_updates[10874]})

    # R068: Поддерживать верность хранителям (S)
    wts_updates[1072] = "|cffe4cfa3Поддерживать верность хранителям|r"
    wts_updates[1073] = "|cffe4cfa3Поддерживать верность хранителям|r (|cffffffffS|r)"
    wts_updates[25922] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Врайкулы сохраняют древние титанические традиции предков, укрепляя тело и дух.|n|n"
        "|cffa6afb8Эффект:|r|cffced4da|n"
        "- Максимальное здоровье: |cffc8e087+200|cffced4da ед.|n"
        "- Урон воинов: |cffc8e087+7|cffced4da ед.|n"
        "- Восстановление маны: |cffc8e087+0,5|cffced4da ед./с|n"
        "- Восстановление здоровья: |cffc8e087+0,3|cffced4da ед./с|n|n"
        "|cffe6c07bВзаимоисключение: блокирует исследование «Примкнуть к Королю-личу».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R068", "field": "name1", "expected": wts_updates[1072]})
    checks_def.append({"type": "upgrade", "id": "R068", "field": "tip1", "expected": wts_updates[1073]})
    checks_def.append({"type": "upgrade", "id": "R068", "field": "ubertip1", "expected": wts_updates[25922]})

    # =========================================================================
    # 2. BUILDINGS (9 buildings)
    # =========================================================================
    # h0BQ: Дом Ярла (Q)
    wts_updates[9900] = "|cffe4cfa3Дом Ярла|r"
    wts_updates[9901] = "|cffe4cfa3Дом Ярла|r (|cffffffffQ|r)"
    wts_updates[13012] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daГлавное здание первой ступени. Обеспечивает добычу ресурсов, сбор золота и древесины.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n"
        "- |cffa9c7deСтроитель|cffced4da: базовый рабочий и строитель.|n"
        "- |cffa9c7deУльфхендар|cffced4da: прирученный волк.|n"
        "- |cffa9c7deДикий Ульфхендар|cffced4da: свирепый зверь.|n|n"
        "|cffa6afb8Улучшение:|r|cffced4da|n"
        "- |cffa9c7deЗалы Ярла|cffced4da: открывает передовые постройки и войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BQ", "field": "name", "expected": wts_updates[9900]})
    checks_def.append({"type": "unit", "id": "h0BQ", "field": "tip", "expected": wts_updates[9901]})
    checks_def.append({"type": "unit", "id": "h0BQ", "field": "ubertip", "expected": wts_updates[13012]})

    # h0BR: Залы Ярла (Z)
    wts_updates[9902] = "|cffe4cfa3Залы Ярла|r"
    wts_updates[9903] = "|cffe4cfa3Залы Ярла|r (|cffffffffZ|r)"
    wts_updates[12978] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daГлавное здание второй ступени. Служит центром сбора ресурсов и открывает доступ к передовым военным постройкам.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n"
        "- |cffa9c7deСтроитель|cffced4da|n"
        "- |cffa9c7deУльфхендар|cffced4da|n"
        "- |cffa9c7deДикий Ульфхендар|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|r|cffced4da|n"
        "- |cffa9c7deКрепость Ярла|cffced4da: завершающая ступень развития.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BR", "field": "name", "expected": wts_updates[9902]})
    checks_def.append({"type": "unit", "id": "h0BR", "field": "tip", "expected": wts_updates[9903]})
    checks_def.append({"type": "unit", "id": "h0BR", "field": "ubertip", "expected": wts_updates[12978]})

    # h0BS: Крепость Ярла (Z)
    wts_updates[9904] = "|cffe4cfa3Крепость Ярла|r"
    wts_updates[9905] = "|cffe4cfa3Крепость Ярла|r (|cffffffffZ|r)"
    wts_updates[12979] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daГлавное здание третьей ступени. Служит оплотом ярла и открывает выбор глобального пути развития.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n"
        "- |cffa9c7deСтроитель|cffced4da|n"
        "- |cffa9c7deУльфхендар|cffced4da|n"
        "- |cffa9c7deДикий Ульфхендар|cffced4da.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n"
        "- |cffa9c7deПримкнуть к Королю-личу|cffced4da|n"
        "- |cffa9c7deПоддерживать верность хранителям|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BS", "field": "name", "expected": wts_updates[9904]})
    checks_def.append({"type": "unit", "id": "h0BS", "field": "tip", "expected": wts_updates[9905]})
    checks_def.append({"type": "unit", "id": "h0BS", "field": "ubertip", "expected": wts_updates[12979]})

    # h0BT: Дом (A)
    wts_updates[9906] = "|cffe4cfa3Дом|r"
    wts_updates[9907] = "|cffe4cfa3Дом|r (|cffffffffA|r)"
    wts_updates[31667] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daЖилое жилище врайкулов. Обеспечивает поселение припасами и увеличивает базовый доход.|n|n"
        "Приносит |cffc8e087+20|cffced4da ед. золотого дохода каждые 25 сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BT", "field": "name", "expected": wts_updates[9906]})
    checks_def.append({"type": "unit", "id": "h0BT", "field": "tip", "expected": wts_updates[9907]})
    checks_def.append({"type": "unit", "id": "h0BT", "field": "ubertip", "expected": wts_updates[31667]})

    # h0BU: Алтарь Героев (S)
    wts_updates[9873] = "|cffe4cfa3Алтарь Героев|r"
    wts_updates[9874] = "|cffe4cfa3Алтарь Героев|r (|cffffffffS|r)"
    wts_updates[19458] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daСвятилище предков. Позволяет призывать вождей врайкулов и воскрешать павших героев.|n|n"
        "|cffa6afb8Герои:|r|cffced4da|n"
        "- |cffa9c7deТан|cffced4da: могучий правитель и мастер защиты.|n"
        "- |cffa9c7deБерсерк|cffced4da: яростный мастер ближнего боя.|n"
        "- |cffa9c7deВерховный жрец|cffced4da: заклинатель рун и повелитель духов.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BU", "field": "name", "expected": wts_updates[9873]})
    checks_def.append({"type": "unit", "id": "h0BU", "field": "tip", "expected": wts_updates[9874]})
    checks_def.append({"type": "unit", "id": "h0BU", "field": "ubertip", "expected": wts_updates[19458]})

    # h0BV: Дом Воинов (W)
    wts_updates[9879] = "|cffe4cfa3Дом Воинов|r"
    wts_updates[9880] = "|cffe4cfa3Дом Воинов|r (|cffffffffW|r)"
    wts_updates[13017] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daКазармы для подготовки базовых пехотинцев и воинов авангарда.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n"
        "- |cffa9c7deВоин-волк|cffced4da: свирепый боец передовой.|n"
        "- |cffa9c7deЛендрман|cffced4da: универсальный воин ближнего и дальнего боя.|n"
        "- |cffa9c7deВоин|cffced4da: стойкий тяжелый пехотинец.|n"
        "- |cffa9c7deХёвдинг|cffced4da: мастер дальнего боя.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n"
        "- |cffa9c7deЗащита|cffced4da|n"
        "- |cffa9c7deМорозные клинки|cffced4da|n"
        "- |cffa9c7deИспытание крови|cffced4da|n"
        "- |cffa9c7deВолчьи навыки|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BV", "field": "name", "expected": wts_updates[9879]})
    checks_def.append({"type": "unit", "id": "h0BV", "field": "tip", "expected": wts_updates[9880]})
    checks_def.append({"type": "unit", "id": "h0BV", "field": "ubertip", "expected": wts_updates[13017]})

    # h0BW: Лесопилка (E)
    wts_updates[9877] = "|cffe4cfa3Лесопилка|r"
    wts_updates[9878] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[20432] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daСлужит складом древесины и центром кузнечных разработок врайкулов.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n"
        "- |cffa9c7deЖелезные мечи|cffced4da: урон ближнего боя.|n"
        "- |cffa9c7deЖелезная броня|cffced4da: броня ближнего боя.|n"
        "- |cffa9c7deТренировки меткости|cffced4da: урон стрелков.|n"
        "- |cffa9c7deДоспехи из кожи|cffced4da: броня стрелков.|n"
        "- |cffa9c7deУлучшенные топоры|cffced4da: добыча древесины.|n"
        "- |cffa9c7deМастерство владения мечом|cffced4da: урон героев.|n"
        "- |cffa9c7deМастерство защиты|cffced4da: броня героев.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BW", "field": "name", "expected": wts_updates[9877]})
    checks_def.append({"type": "unit", "id": "h0BW", "field": "tip", "expected": wts_updates[9878]})
    checks_def.append({"type": "unit", "id": "h0BW", "field": "ubertip", "expected": wts_updates[20432]})

    # h0BX: Дом Покорителей севера (R)
    wts_updates[9966] = "|cffe4cfa3Дом Покорителей севера|r"
    wts_updates[9967] = "|cffe4cfa3Дом Покорителей севера|r (|cffffffffR|r)"
    wts_updates[13019] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daОбитель заклинательниц и элитных наездников на зверях Нордскола.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n"
        "- |cffa9c7deЗаклинательница Рун|cffced4da: маг поддержки и очищения.|n"
        "- |cffa9c7deНаездница Ульфхендар|cffced4da: стрелок на звере с ледяными стрелами.|n"
        "- |cffa9c7deСкальд|cffced4da: могучий воин с рассекающим ударом.|n"
        "- |cffa9c7deНаездник на прото-драконе|cffced4da: тяжелый летающий всадник.|n|n"
        "|cffa6afb8Исследования:|r|cffced4da|n"
        "- |cffa9c7deДревнее учение Титанорожденных|cffced4da|n"
        "- |cffa9c7deДревнее учение Короля-Лича|cffced4da|n"
        "- |cffa9c7deЛедяные стрелы|cffced4da|n"
        "- |cffa9c7deДополнительные доспехи|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BX", "field": "name", "expected": wts_updates[9966]})
    checks_def.append({"type": "unit", "id": "h0BX", "field": "tip", "expected": wts_updates[9967]})
    checks_def.append({"type": "unit", "id": "h0BX", "field": "ubertip", "expected": wts_updates[13019]})

    # wk01: Тёмные казармы (F)
    wts_updates[7371] = "|cffe4cfa3Тёмные казармы|r"
    wts_updates[29441] = "|cffe4cfa3Тёмные казармы|r (|cffffffffF|r)"
    wts_updates[27912] = (
        "|cffa6afb8ЗДАНИЕ:|r |cffced4daЭлитное святилище культа Плети. Служит для подготовки крылатых валь'кир и драконьих всадников.|n|n"
        "|cffa6afb8Обучает:|r|cffced4da|n"
        "- |cffa9c7deВалькира|cffced4da: крылатая дева смерти, поднимающая мертвецов.|n"
        "- |cffa9c7deВсадник прото-дракона (меч и щит)|cffced4da: защищенный всадник.|n"
        "- |cffa9c7deВсадник прото-дракона|cffced4da: бронебойный всадник.|r"
    )
    checks_def.append({"type": "unit", "id": "wk01", "field": "name", "expected": wts_updates[7371]})
    checks_def.append({"type": "unit", "id": "wk01", "field": "tip", "expected": wts_updates[29441]})
    checks_def.append({"type": "unit", "id": "wk01", "field": "ubertip", "expected": wts_updates[27912]})

    # =========================================================================
    # 3. HEROES (4 heroes)
    # =========================================================================
    # H0C4: Король Имирон (Z)
    wts_updates[9866] = "|cffe4cfa3Король Имирон|r"
    wts_updates[9867] = "|cffe4cfa3Имирон|r"
    wts_updates[9869] = "|cffe4cfa3Король Имирон|r (|cffffffffZ|r)"
    wts_updates[9868] = "|cffe4cfa3Король Имирон|r"
    wts_updates[9870] = "|cffe4cfa3Король Имирон|r"
    wts_updates[19272] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daЛегендарный правитель врайкулов, могучий исполин в тяжелых доспехах. "
        "Специализируется на подавлении противников, нанесении сокрушительных фронтальных ударов и усилении союзников боевым ревом.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deЯростный удар|cffced4da: рассекающий удар с кровотечением.|n"
        "- |cffa9c7deИзнурение|cffced4da: замедление окружающих врагов.|n"
        "- |cffa9c7deСильный Удар|cffced4da: шанс нанести дополнительный урон и оглушить цель.|n"
        "- |cffa9c7deРев|cffced4da: боевой клич, повышающий урон и броню союзников.|n"
        "- |cffa9c7deРассекающий Удар|cffced4da: пассивный урон по соседним целям.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "H0C4", "field": "name", "expected": wts_updates[9866]})
    checks_def.append({"type": "unit", "id": "H0C4", "field": "propernames", "expected": wts_updates[9867]})
    checks_def.append({"type": "unit", "id": "H0C4", "field": "tip", "expected": wts_updates[9869]})
    checks_def.append({"type": "unit", "id": "H0C4", "field": "awakentip", "expected": wts_updates[9868]})
    checks_def.append({"type": "unit", "id": "H0C4", "field": "revivetip", "expected": wts_updates[9870]})
    checks_def.append({"type": "unit", "id": "H0C4", "field": "ubertip", "expected": wts_updates[19272]})

    # H0C5: Берсерк (X)
    wts_updates[646] = "|cffe4cfa3Берсерк|r"
    wts_updates[644] = "|cffe4cfa3Вандер Убийца|r"
    wts_updates[653] = "|cffe4cfa3Берсерк|r (|cffffffffX|r)"
    wts_updates[648] = "|cffe4cfa3Берсерк|r"
    wts_updates[655] = "|cffe4cfa3Берсерк|r"
    wts_updates[31699] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daЯростный воин ближнего боя, черпающий силу в неистовстве сражения. "
        "Специализируется на метании топоров, руническом замедлении при атаках, ауре стремительности и превращении в неостановимого аватара.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deМетнуть топор|cffced4da: оглушающий бросок топора с уроном.|n"
        "- |cffa9c7deРунические топоры|cffced4da: замедление врагов при ударах.|n"
        "- |cffa9c7deАура безумия|cffced4da: ускорение атаки и движения союзников.|n"
        "- |cffa9c7deАватар берсерка|cffced4da: превращение с иммунитетом к магии, бонусом здоровья и урона.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "H0C5", "field": "name", "expected": wts_updates[646]})
    checks_def.append({"type": "unit", "id": "H0C5", "field": "propernames", "expected": wts_updates[644]})
    checks_def.append({"type": "unit", "id": "H0C5", "field": "tip", "expected": wts_updates[653]})
    checks_def.append({"type": "unit", "id": "H0C5", "field": "awakentip", "expected": wts_updates[648]})
    checks_def.append({"type": "unit", "id": "H0C5", "field": "revivetip", "expected": wts_updates[655]})
    checks_def.append({"type": "unit", "id": "H0C5", "field": "ubertip", "expected": wts_updates[31699]})

    # H0C6: Тан (Z)
    wts_updates[524] = "|cffe4cfa3Тан|r"
    wts_updates[506] = "|cffe4cfa3Бор Камнелом|r"
    wts_updates[526] = "|cffe4cfa3Тан|r (|cffffffffZ|r)"
    wts_updates[525] = "|cffe4cfa3Тан|r"
    wts_updates[527] = "|cffe4cfa3Тан|r"
    wts_updates[31700] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daМогучий вождь и тан врайкулов, несокрушимый защитник своих воинов. "
        "Специализируется на укреплении союзной брони, сокрушительных круговых ударах и призыве клинков предков.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deЯростный удар|cffced4da: рассекающий фронтальный удар с кровотечением.|n"
        "- |cffa9c7deСокрушение|cffced4da: шанс нанести круговой урон по площади при атаке.|n"
        "- |cffa9c7deТяжелые доспехи|cffced4da: пассивное увеличение брони.|n"
        "- |cffa9c7deЗов|cffced4da: аура, повышающая защиту союзников.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "H0C6", "field": "name", "expected": wts_updates[524]})
    checks_def.append({"type": "unit", "id": "H0C6", "field": "propernames", "expected": wts_updates[506]})
    checks_def.append({"type": "unit", "id": "H0C6", "field": "tip", "expected": wts_updates[526]})
    checks_def.append({"type": "unit", "id": "H0C6", "field": "awakentip", "expected": wts_updates[525]})
    checks_def.append({"type": "unit", "id": "H0C6", "field": "revivetip", "expected": wts_updates[527]})
    checks_def.append({"type": "unit", "id": "H0C6", "field": "ubertip", "expected": wts_updates[31700]})

    # H0C7: Верховный жрец (C)
    wts_updates[529] = "|cffe4cfa3Верховный жрец|r"
    wts_updates[531] = "|cffe4cfa3Далар Ткач|r"
    wts_updates[535] = "|cffe4cfa3Верховный жрец|r (|cffffffffC|r)"
    wts_updates[533] = "|cffe4cfa3Верховный жрец|r"
    wts_updates[536] = "|cffe4cfa3Верховный жрец|r"
    wts_updates[31701] = (
        "|cffa6afb8ГЕРОЙ:|r |cffced4daМудрый жрец древних рун и хранитель северных духов. "
        "Специализируется на артиллерийском обстреле сгустками духов, наложении рун каменной защиты, проклятии врагов и спасительном исцелении павших воинов.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deПомощь Предков|cffced4da: залп духов по указанной области с уроном.|n"
        "- |cffa9c7deРуны защиты|cffced4da: наложение щита брони на союзников.|n"
        "- |cffa9c7deРуны проклятия|cffced4da: периодический урон атакованным целям.|n"
        "- |cffa9c7deРуны Спасения|cffced4da: спасение и полное восстановление здоровья союзных войск.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные и воздушные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "H0C7", "field": "name", "expected": wts_updates[529]})
    checks_def.append({"type": "unit", "id": "H0C7", "field": "propernames", "expected": wts_updates[531]})
    checks_def.append({"type": "unit", "id": "H0C7", "field": "tip", "expected": wts_updates[535]})
    checks_def.append({"type": "unit", "id": "H0C7", "field": "awakentip", "expected": wts_updates[533]})
    checks_def.append({"type": "unit", "id": "H0C7", "field": "revivetip", "expected": wts_updates[536]})
    checks_def.append({"type": "unit", "id": "H0C7", "field": "ubertip", "expected": wts_updates[31701]})

    # =========================================================================
    # 4. UNITS (14 units)
    # =========================================================================
    # h0C9: Строитель (Q)
    wts_updates[9885] = "|cffe4cfa3Строитель|r"
    wts_updates[778] = "|cffe4cfa3Строитель|r (|cffffffffQ|r)"
    wts_updates[20569] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daБазовый рабочий врайкулов. Добывает золото и древесину, возводит и ремонтирует здания.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: короткий телепорт.|n"
        "- |cffa9c7deДобывать ресурсы|cffced4da: добыча ресурсов.|n"
        "- |cffa9c7deРемонтировать|cffced4da: починка зданий.|n"
        "- |cffa9c7deПризыв к оружию|cffced4da: ополчение.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0C9", "field": "name", "expected": wts_updates[9885]})
    checks_def.append({"type": "unit", "id": "h0C9", "field": "tip", "expected": wts_updates[778]})
    checks_def.append({"type": "unit", "id": "h0C9", "field": "ubertip", "expected": wts_updates[20569]})

    # h0AA: Лендрман (W)
    wts_updates[9272] = "|cffe4cfa3Лендрман|r"
    wts_updates[9274] = "|cffe4cfa3Лендрман|r (|cffffffffW|r)"
    wts_updates[29270] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daУниверсальный солдат врайкулов, способный мгновенно переключаться между ближним боем топором и метанием дротиков на дистанции.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deПерейти в дальний бой|cffced4da: смена стойки.|n"
        "- |cffa9c7deЯрость севера|cffced4da: боевой раж с увеличением скорости атаки.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0AA", "field": "name", "expected": wts_updates[9272]})
    checks_def.append({"type": "unit", "id": "h0AA", "field": "tip", "expected": wts_updates[9274]})
    checks_def.append({"type": "unit", "id": "h0AA", "field": "ubertip", "expected": wts_updates[29270]})

    # h0AD: Воин-волк (Q)
    wts_updates[9281] = "|cffe4cfa3Воин-волк|r"
    wts_updates[7370] = "|cffe4cfa3Воин-волк|r (|cffffffffQ|r)"
    wts_updates[32629] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daБыстрый и яростный боец передовой, облачённый в волчью шкуру. Нападает внезапными выпадами и черпает силы в ярости севера.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deЯрость севера|cffced4da: повышение скорости боя.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0AD", "field": "name", "expected": wts_updates[9281]})
    checks_def.append({"type": "unit", "id": "h0AD", "field": "tip", "expected": wts_updates[7370]})
    checks_def.append({"type": "unit", "id": "h0AD", "field": "ubertip", "expected": wts_updates[32629]})

    # h0A5: Воин (E)
    wts_updates[9257] = "|cffe4cfa3Воин|r"
    wts_updates[9259] = "|cffe4cfa3Воин|r (|cffffffffE|r)"
    wts_updates[21503] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daСтойкий пехотинец регулярной армии врайкулов с тяжелым щитом и мечом. Способен закрываться щитом от стрел и замедлять врагов морозными клинками.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deЗащита|cffced4da: снижение входящего урона от пронзающих атак.|n"
        "- |cffa9c7deМорозные клинки|cffced4da: замедление атакуемых целей.|n"
        "- |cffa9c7deЯрость севера|cffced4da: кратковременное ускорение атаки.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0A5", "field": "name", "expected": wts_updates[9257]})
    checks_def.append({"type": "unit", "id": "h0A5", "field": "tip", "expected": wts_updates[9259]})
    checks_def.append({"type": "unit", "id": "h0A5", "field": "ubertip", "expected": wts_updates[21503]})

    # h0A6: Хёвдинг (R)
    wts_updates[9260] = "|cffe4cfa3Хёвдинг|r"
    wts_updates[9262] = "|cffe4cfa3Хёвдинг|r (|cffffffffR|r)"
    wts_updates[22350] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМеткий стрелок и командир отделения, вооруженный метательными копьями. Наносит критические удары на средней дистанции.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deТочный удар|cffced4da: шанс нанести критический урон при атаке.|n"
        "- |cffa9c7deЯрость севера|cffced4da: ускорение боя.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0A6", "field": "name", "expected": wts_updates[9260]})
    checks_def.append({"type": "unit", "id": "h0A6", "field": "tip", "expected": wts_updates[9262]})
    checks_def.append({"type": "unit", "id": "h0A6", "field": "ubertip", "expected": wts_updates[22350]})

    # h0BP: Заклинательница Рун (Q)
    wts_updates[9634] = "|cffe4cfa3Заклинательница Рун|r"
    wts_updates[9635] = "|cffe4cfa3Заклинательница Рун|r (|cffffffffQ|r)"
    wts_updates[33634] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daМагическая жрица врайкулов. Накладывает на союзников ледяные щиты, усиливает их атаку вдохновением и снимает вражеские чары.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deСеверный доспех|cffced4da: повышение защиты союзников на |cffc8e087+3|cffced4da ед.|n"
        "- |cffa9c7deВдохновение|cffced4da: увеличение урона союзника на |cffc8e087+25%|cffced4da.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: развеивание магии в области и урон призванным.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные и воздушные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0BP", "field": "name", "expected": wts_updates[9634]})
    checks_def.append({"type": "unit", "id": "h0BP", "field": "tip", "expected": wts_updates[9635]})
    checks_def.append({"type": "unit", "id": "h0BP", "field": "ubertip", "expected": wts_updates[33634]})

    # h0A9: Наездница Ульфхендар (W)
    wts_updates[9269] = "|cffe4cfa3Наездница Ульфхендар|r"
    wts_updates[9271] = "|cffe4cfa3Наездница Ульфхендар|r (|cffffffffW|r)"
    wts_updates[29269] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daБыстрый стрелок верхом на свирепом звере севера. Ведет огонь ледяными стрелами, замедляя врагов на ходу.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deЛедяные стрелы|cffced4da: дополнительный урон холодом и замедление.|n"
        "- |cffa9c7deЯрость севера|cffced4da: ускорение атаки.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0A9", "field": "name", "expected": wts_updates[9269]})
    checks_def.append({"type": "unit", "id": "h0A9", "field": "tip", "expected": wts_updates[9271]})
    checks_def.append({"type": "unit", "id": "h0A9", "field": "ubertip", "expected": wts_updates[29269]})

    # h0AC: Скальд (E)
    wts_updates[9630] = "|cffe4cfa3Скальд|r"
    wts_updates[9631] = "|cffe4cfa3Скальд|r (|cffffffffE|r)"
    wts_updates[32103] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daЭлитный наездник и воин-сказитель в укреплённых латах. Рассекает вражеские ряды мощными ударами секиры.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deРассекающий удар|cffced4da: урон соседним врагам при каждой атаке.|n"
        "- |cffa9c7deДополнительные доспехи|cffced4da: пассивное увеличение брони и здоровья.|n"
        "- |cffa9c7deЯрость севера|cffced4da: кратковременное ускорение атаки.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0AC", "field": "name", "expected": wts_updates[9630]})
    checks_def.append({"type": "unit", "id": "h0AC", "field": "tip", "expected": wts_updates[9631]})
    checks_def.append({"type": "unit", "id": "h0AC", "field": "ubertip", "expected": wts_updates[32103]})

    # h0AE: Наездник на прото-драконе (R)
    wts_updates[9898] = "|cffe4cfa3Наездник на прото-драконе|r"
    wts_updates[9899] = "|cffe4cfa3Наездник на прото-драконе|r (|cffffffffR|r)"
    wts_updates[32859] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daТяжелый летающий зверь Нордскола с наездником-врайкулом. Выдыхает потоки пламени и внушает ужас вражеским армиям.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deПламенное дыхание|cffced4da: конус огня перед собой.|n"
        "- |cffa9c7deУжасающий вой|cffced4da: снижение урона ближайших врагов на |cffe69a8d-35%|cffced4da.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0AE", "field": "name", "expected": wts_updates[9898]})
    checks_def.append({"type": "unit", "id": "h0AE", "field": "tip", "expected": wts_updates[9899]})
    checks_def.append({"type": "unit", "id": "h0AE", "field": "ubertip", "expected": wts_updates[32859]})

    # wk08: Валькира (E)
    wts_updates[699] = "|cffe4cfa3Валькира|r"
    wts_updates[700] = "|cffe4cfa3Валькира|r (|cffffffffE|r)"
    wts_updates[33814] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daКрылатая дева смерти, парящая над полем боя. Поднимает павших воинов в виде нежити и усиливает союзников нечестивой аурой.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deОживление мертвых|cffced4da: поднимает до 3 трупов на поле боя.|n"
        "- |cffa9c7deНечистая аура|cffced4da: аура скорости движения и регенерации союзников.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные и воздушные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "wk08", "field": "name", "expected": wts_updates[699]})
    checks_def.append({"type": "unit", "id": "wk08", "field": "tip", "expected": wts_updates[700]})
    checks_def.append({"type": "unit", "id": "wk08", "field": "ubertip", "expected": wts_updates[33814]})

    # wk02: Всадник прото-дракона (меч и щит) (Q)
    wts_updates[40141] = "|cffe4cfa3Всадник прото-дракона (меч и щит)|r"
    wts_updates[30181] = "|cffe4cfa3Всадник прото-дракона (меч и щит)|r (|cffffffffQ|r)"
    wts_updates[40301] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daТяжелобронированный всадник на протодраконе, снаряженный щитом и чешуйчатым покровом для поглощения вражеских атак.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deЗащита|cffced4da: уменьшение урона от дальних атак до 90%.|n"
        "- |cffa9c7deБроня из драконьей чешуи|cffced4da: поглощение входящего урона.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "wk02", "field": "name", "expected": wts_updates[40141]})
    checks_def.append({"type": "unit", "id": "wk02", "field": "tip", "expected": wts_updates[30181]})
    checks_def.append({"type": "unit", "id": "wk02", "field": "ubertip", "expected": wts_updates[40301]})

    # wk00: Всадник прото-дракона (W)
    wts_updates[40099] = "|cffe4cfa3Всадник прото-дракона|r"
    wts_updates[3045] = "|cffe4cfa3Всадник прото-дракона|r (|cffffffffW|r)"
    wts_updates[3044] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daШтурмовой всадник на протодраконе, специализирующийся на пробитии вражеских доспехов и сокрушении защитных порядков.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deПробитие доспехов|cffced4da: снижение брони цели.|n"
        "- |cffa9c7deБроня из драконьей чешуи|cffced4da: поглощение входящего урона.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "wk00", "field": "name", "expected": wts_updates[40099]})
    checks_def.append({"type": "unit", "id": "wk00", "field": "tip", "expected": wts_updates[3045]})
    checks_def.append({"type": "unit", "id": "wk00", "field": "ubertip", "expected": wts_updates[3044]})

    # h0A8: Дикий Ульфхендар (W)
    wts_updates[9266] = "|cffe4cfa3Дикий Ульфхендар|r"
    wts_updates[9268] = "|cffe4cfa3Дикий Ульфхендар|r (|cffffffffW|r)"
    wts_updates[22365] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daСвирепый волк северных пустошей. Отравляет врагов замедляющим ядом и впадает в ярость севера.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deСильный укус|cffced4da: ядовитый укус с замедлением и периодическим уроном.|n"
        "- |cffa9c7deЯрость севера|cffced4da: ускорение боя.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0A8", "field": "name", "expected": wts_updates[9266]})
    checks_def.append({"type": "unit", "id": "h0A8", "field": "tip", "expected": wts_updates[9268]})
    checks_def.append({"type": "unit", "id": "h0A8", "field": "ubertip", "expected": wts_updates[22365]})

    # h0A7: Ульфхендар (E)
    wts_updates[9263] = "|cffe4cfa3Ульфхендар|r"
    wts_updates[9265] = "|cffe4cfa3Ульфхендар|r (|cffffffffE|r)"
    wts_updates[31691] = (
        "|cffa6afb8ЮНИТ:|r |cffced4daПрирученный волк врайкулов. Быстрый разведчик и зверь поддержки с ядовитым укусом.|n|n"
        "|cffa6afb8Способности:|r|cffced4da|n"
        "- |cffa9c7deСильный укус|cffced4da: замедляющий яд.|n"
        "- |cffa9c7deЯрость севера|cffced4da: ускорение боя.|n|n"
        "|cffa6afb8Цели атаки:|r |cffced4daназемные войска.|r"
    )
    checks_def.append({"type": "unit", "id": "h0A7", "field": "name", "expected": wts_updates[9263]})
    checks_def.append({"type": "unit", "id": "h0A7", "field": "tip", "expected": wts_updates[9265]})
    checks_def.append({"type": "unit", "id": "h0A7", "field": "ubertip", "expected": wts_updates[31691]})

    # =========================================================================
    # 5. RESEARCH (17 upgrades / 47 levels)
    # =========================================================================
    # R05Z: Защита (F)
    wts_updates[9982] = "|cffe4cfa3Защита|r"
    wts_updates[9983] = "|cffe4cfa3Защита|r (|cffffffffF|r)"
    wts_updates[12014] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Воинов использованию больших щитов для отражения стрел и снижения урона от пронзающих атак.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deВоин|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R05Z", "field": "name1", "expected": wts_updates[9982]})
    checks_def.append({"type": "upgrade", "id": "R05Z", "field": "tip1", "expected": wts_updates[9983]})
    checks_def.append({"type": "upgrade", "id": "R05Z", "field": "ubertip1", "expected": wts_updates[12014]})

    # R060: Испытание крови (2 levels, S)
    wts_updates[21] = "|cffe4cfa3Испытание крови — уровень 1|r"
    wts_updates[22] = "|cffe4cfa3Испытание крови — уровень 1|r (|cffffffffS|r)"
    wts_updates[17104] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Закаляет воинов в ритуальных боях, повышая запас здоровья и силу атаки пехотинцев.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deВоин|cffced4da, |cffa9c7deВоин-волк|cffced4da, |cffa9c7deЛендрман|cffced4da, |cffa9c7deХёвдинг|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r.|r"
    )
    wts_updates[38] = "|cffe4cfa3Испытание крови — уровень 2|r"
    wts_updates[39] = "|cffe4cfa3Испытание крови — уровень 2|r (|cffffffffS|r)"
    wts_updates[20089] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно закаляет воинов, ещё сильнее увеличивая их стойкость и боевую мощь.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deВоин|cffced4da, |cffa9c7deВоин-волк|cffced4da, |cffa9c7deЛендрман|cffced4da, |cffa9c7deХёвдинг|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R060", "field": "name1", "expected": wts_updates[21]})
    checks_def.append({"type": "upgrade", "id": "R060", "field": "tip1", "expected": wts_updates[22]})
    checks_def.append({"type": "upgrade", "id": "R060", "field": "ubertip1", "expected": wts_updates[17104]})
    checks_def.append({"type": "upgrade", "id": "R060", "field": "name2", "expected": wts_updates[38]})
    checks_def.append({"type": "upgrade", "id": "R060", "field": "tip2", "expected": wts_updates[39]})
    checks_def.append({"type": "upgrade", "id": "R060", "field": "ubertip2", "expected": wts_updates[20089]})

    # R061: Дополнительные доспехи (D)
    wts_updates[41] = "|cffe4cfa3Дополнительные доспехи|r"
    wts_updates[42] = "|cffe4cfa3Дополнительные доспехи|r (|cffffffffD|r)"
    wts_updates[44] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет доспехи Скальда, повышая его броню и запас здоровья.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deСкальд|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R061", "field": "name1", "expected": wts_updates[41]})
    checks_def.append({"type": "upgrade", "id": "R061", "field": "tip1", "expected": wts_updates[42]})
    checks_def.append({"type": "upgrade", "id": "R061", "field": "ubertip1", "expected": wts_updates[44]})

    # R062: Ледяные стрелы (2 levels, S)
    wts_updates[25704] = "|cffe4cfa3Ледяные стрелы — уровень 1|r"
    wts_updates[51] = "|cffe4cfa3Ледяные стрелы — уровень 1|r (|cffffffffS|r)"
    wts_updates[52] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Зачаровывает стрелы Наездниц холодом, добавляя дополнительный урон и замедляющий эффект.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deНаездница Ульфхендар|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/2|r.|r"
    )
    wts_updates[25706] = "|cffe4cfa3Ледяные стрелы — уровень 2|r"
    wts_updates[18373] = "|cffe4cfa3Ледяные стрелы — уровень 2|r (|cffffffffS|r)"
    wts_updates[8633] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает морозные чары стрел, повышая урон холодом и силу замедления.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deНаездница Ульфхендар|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/2|r.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R062", "field": "name1", "expected": wts_updates[25704]})
    checks_def.append({"type": "upgrade", "id": "R062", "field": "tip1", "expected": wts_updates[51]})
    checks_def.append({"type": "upgrade", "id": "R062", "field": "ubertip1", "expected": wts_updates[52]})
    checks_def.append({"type": "upgrade", "id": "R062", "field": "name2", "expected": wts_updates[25706]})
    checks_def.append({"type": "upgrade", "id": "R062", "field": "tip2", "expected": wts_updates[18373]})
    checks_def.append({"type": "upgrade", "id": "R062", "field": "ubertip2", "expected": wts_updates[8633]})

    # R063: Морозные клинки (D)
    wts_updates[9975] = "|cffe4cfa3Морозные клинки|r"
    wts_updates[1152] = "|cffe4cfa3Морозные клинки|r (|cffffffffD|r)"
    wts_updates[15100] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Зачаровывает мечи пехотинцев, позволяя атакам замедлять скорость перемещения и боя врагов.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deВоин|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R063", "field": "name1", "expected": wts_updates[9975]})
    checks_def.append({"type": "upgrade", "id": "R063", "field": "tip1", "expected": wts_updates[1152]})
    checks_def.append({"type": "upgrade", "id": "R063", "field": "ubertip1", "expected": wts_updates[15100]})

    # R064: Волчьи навыки (A)
    wts_updates[1157] = "|cffe4cfa3Волчьи навыки|r"
    wts_updates[35335] = "|cffe4cfa3Волчьи навыки|r (|cffffffffA|r)"
    wts_updates[1166] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает бойцов и зверей диким повадкам волчьей стаи, увеличивая скорость перемещения и урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deВоин-волк|cffced4da, |cffa9c7deУльфхендар|cffced4da, |cffa9c7deДикий Ульфхендар|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R064", "field": "name1", "expected": wts_updates[1157]})
    checks_def.append({"type": "upgrade", "id": "R064", "field": "tip1", "expected": wts_updates[35335]})
    checks_def.append({"type": "upgrade", "id": "R064", "field": "ubertip1", "expected": wts_updates[1166]})

    # R065: Древнее учение Титанорожденных (3 levels, A)
    wts_updates[1076] = "|cffe4cfa3Древнее учение Титанорождённых — уровень 1|r"
    wts_updates[1196] = "|cffe4cfa3Древнее учение Титанорождённых — уровень 1|r (|cffffffffA|r)"
    wts_updates[20091] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заклинательницы рун познают тайны титанов, увеличивая запас маны, скорость её восстановления и силу чар.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/3|r.|r"
    )
    wts_updates[1195] = "|cffe4cfa3Древнее учение Титанорождённых — уровень 2|r"
    wts_updates[1214] = "|cffe4cfa3Древнее учение Титанорождённых — уровень 2|r (|cffffffffA|r)"
    wts_updates[20092] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно углубляет познание магии титанов, повышая запас маны и открывая новые заклинания.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/3|r.|r"
    )
    wts_updates[1213] = "|cffe4cfa3Древнее учение Титанорождённых — уровень 3|r"
    wts_updates[1301] = "|cffe4cfa3Древнее учение Титанорождённых — уровень 3|r (|cffffffffA|r)"
    wts_updates[20093] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Завершает обучение тайнам титанов, максимально усиливая могущество заклинательниц.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3/3|r.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R065", "field": "name1", "expected": wts_updates[1076]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "tip1", "expected": wts_updates[1196]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "ubertip1", "expected": wts_updates[20091]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "name2", "expected": wts_updates[1195]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "tip2", "expected": wts_updates[1214]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "ubertip2", "expected": wts_updates[20092]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "name3", "expected": wts_updates[1213]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "tip3", "expected": wts_updates[1301]})
    checks_def.append({"type": "upgrade", "id": "R065", "field": "ubertip3", "expected": wts_updates[20093]})

    # R066: Древнее учение Короля-Лича (3 levels, Z)
    wts_updates[1303] = "|cffe4cfa3Древнее учение Короля-лича — уровень 1|r"
    wts_updates[3447] = "|cffe4cfa3Древнее учение Короля-лича — уровень 1|r (|cffffffffZ|r)"
    wts_updates[9286] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Заклинательницы рун постигают тёмные ритуалы Плети, увеличивая силу своих способностей и запас маны.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1/3|r.|r"
    )
    wts_updates[1379] = "|cffe4cfa3Древнее учение Короля-лича — уровень 2|r"
    wts_updates[4059] = "|cffe4cfa3Древнее учение Короля-лича — уровень 2|r (|cffffffffZ|r)"
    wts_updates[20094] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает тёмную магию Плети у заклинательниц рун.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2/3|r.|r"
    )
    wts_updates[1439] = "|cffe4cfa3Древнее учение Короля-лича — уровень 3|r"
    wts_updates[8457] = "|cffe4cfa3Древнее учение Короля-лича — уровень 3|r (|cffffffffZ|r)"
    wts_updates[20095] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует максимальное могущество тёмной магии Короля-лича.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3/3|r.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R066", "field": "name1", "expected": wts_updates[1303]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "tip1", "expected": wts_updates[3447]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "ubertip1", "expected": wts_updates[9286]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "name2", "expected": wts_updates[1379]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "tip2", "expected": wts_updates[4059]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "ubertip2", "expected": wts_updates[20094]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "name3", "expected": wts_updates[1439]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "tip3", "expected": wts_updates[8457]})
    checks_def.append({"type": "upgrade", "id": "R066", "field": "ubertip3", "expected": wts_updates[20095]})

    # R069: Мечи (6 levels, Q)
    melee_names = ["Железные мечи", "Железные мечи", "Стальные мечи", "Стальные мечи", "Мифриловые мечи", "Мифриловые мечи"]
    r069_sids = [
        (1497, 1571, 15112),
        (1499, 1591, 15114),
        (1510, 1627, 15113),
        (1570, 1628, 15109),
        (1569, 1629, 15110),
        (1568, 1630, 15111)
    ]
    for idx, (nsid, tsid, usid) in enumerate(r069_sids):
        lvl = idx + 1
        bname = melee_names[idx]
        wts_updates[nsid] = f"|cffe4cfa3{bname} — уровень {lvl}|r"
        wts_updates[tsid] = f"|cffe4cfa3{bname} — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[usid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон всех воинов врайкулов, сражающихся в ближнем бою.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deВоин|cffced4da, |cffa9c7deВоин-волк|cffced4da, |cffa9c7deЛендрман|cffced4da, |cffa9c7deСкальд|cffced4da, |cffa9c7deВсадники|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R069", "field": f"name{lvl}", "expected": wts_updates[nsid]})
        checks_def.append({"type": "upgrade", "id": "R069", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "upgrade", "id": "R069", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # R06A: Броня (6 levels, A)
    armor_names = ["Железная броня", "Железная броня", "Стальная броня", "Стальная броня", "Мифриловая броня", "Мифриловая броня"]
    r06a_sids = [
        (1655, 1676, 15118),
        (1656, 1677, 15119),
        (1657, 1678, 15120),
        (1673, 1681, 15115),
        (1659, 1680, 15116),
        (1658, 1679, 15117)
    ]
    for idx, (nsid, tsid, usid) in enumerate(r06a_sids):
        lvl = idx + 1
        bname = armor_names[idx]
        wts_updates[nsid] = f"|cffe4cfa3{bname} — уровень {lvl}|r"
        wts_updates[tsid] = f"|cffe4cfa3{bname} — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[usid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню всех воинов врайкулов, сражающихся в ближнем бою.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deВоин|cffced4da, |cffa9c7deВоин-волк|cffced4da, |cffa9c7deЛендрман|cffced4da, |cffa9c7deСкальд|cffced4da, |cffa9c7deВсадники|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R06A", "field": f"name{lvl}", "expected": wts_updates[nsid]})
        checks_def.append({"type": "upgrade", "id": "R06A", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "upgrade", "id": "R06A", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # R06B: Тренировки меткости (6 levels, W)
    r06b_sids = [
        (1968, 2037, 15124),
        (1976, 2121, 15125),
        (1978, 2130, 15126),
        (2011, 2131, 15121),
        (1985, 2132, 15122),
        (2034, 2133, 15123)
    ]
    for idx, (nsid, tsid, usid) in enumerate(r06b_sids):
        lvl = idx + 1
        wts_updates[nsid] = f"|cffe4cfa3Тренировки меткости — уровень {lvl}|r"
        wts_updates[tsid] = f"|cffe4cfa3Тренировки меткости — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[usid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон всех стрелков и метателей врайкулов в дальнем бою.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deХёвдинг|cffced4da, |cffa9c7deНаездница Ульфхендар|cffced4da, |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R06B", "field": f"name{lvl}", "expected": wts_updates[nsid]})
        checks_def.append({"type": "upgrade", "id": "R06B", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "upgrade", "id": "R06B", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # R06C: Доспехи из кожи (6 levels, S)
    leather_names = [
        "Доспехи из клёпаной кожи", "Доспехи из клёпаной кожи",
        "Доспехи из армированной кожи", "Доспехи из армированной кожи",
        "Доспехи из драконьей кожи", "Доспехи из драконьей кожи"
    ]
    r06c_sids = [
        (2144, 2171, 15130),
        (2145, 2172, 15132),
        (2159, 2174, 15131),
        (2170, 2201, 15127),
        (2169, 2200, 15128),
        (2160, 2181, 15129)
    ]
    for idx, (nsid, tsid, usid) in enumerate(r06c_sids):
        lvl = idx + 1
        bname = leather_names[idx]
        wts_updates[nsid] = f"|cffe4cfa3{bname} — уровень {lvl}|r"
        wts_updates[tsid] = f"|cffe4cfa3{bname} — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[usid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню стрелков и заклинательниц врайкулов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deХёвдинг|cffced4da, |cffa9c7deНаездница Ульфхендар|cffced4da, |cffa9c7deЗаклинательница Рун|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R06C", "field": f"name{lvl}", "expected": wts_updates[nsid]})
        checks_def.append({"type": "upgrade", "id": "R06C", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "upgrade", "id": "R06C", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # R06D: Улучшенные топоры (6 levels, Z)
    r06d_sids = [
        (2243, 20823, None),
        (20818, 2266, 20828),
        (20819, 20824, 20829),
        (20820, 20825, 20830),
        (20821, 20826, 20831),
        (20822, 20827, 20832)
    ]
    for idx, (nsid, tsid, usid) in enumerate(r06d_sids):
        lvl = idx + 1
        wts_updates[nsid] = f"|cffe4cfa3Улучшенные топоры — уровень {lvl}|r"
        wts_updates[tsid] = f"|cffe4cfa3Улучшенные топоры — уровень {lvl}|r (|cffffffffZ|r)"
        if usid:
            wts_updates[usid] = (
                f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём древесины, переносимой строителями за один раз.|n|n"
                f"|cffa6afb8Применяется к:|cffced4da|n"
                f"- |cffa9c7deСтроитель|cffced4da.|n|n"
                f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/6|r.|r"
            )
            checks_def.append({"type": "upgrade", "id": "R06D", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})
        checks_def.append({"type": "upgrade", "id": "R06D", "field": f"name{lvl}", "expected": wts_updates[nsid]})
        checks_def.append({"type": "upgrade", "id": "R06D", "field": f"tip{lvl}", "expected": wts_updates[tsid]})

    # R06E: Мастерство владения мечом (3 levels, E)
    r06e_sids = [
        (2270, 2313, 2319),
        (2311, 2314, 2326),
        (2312, 2318, 2327)
    ]
    for idx, (nsid, tsid, usid) in enumerate(r06e_sids):
        lvl = idx + 1
        wts_updates[nsid] = f"|cffe4cfa3Мастерство владения мечом — уровень {lvl}|r"
        wts_updates[tsid] = f"|cffe4cfa3Мастерство владения мечом — уровень {lvl}|r (|cffffffffE|r)"
        wts_updates[usid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает силу атаки героев врайкулов в ближнем бою.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deТан|cffced4da, |cffa9c7deБерсерк|cffced4da, |cffa9c7deКороль Имирон|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R06E", "field": f"name{lvl}", "expected": wts_updates[nsid]})
        checks_def.append({"type": "upgrade", "id": "R06E", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "upgrade", "id": "R06E", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # R06F: Мастерство защиты (3 levels, D)
    r06f_sids = [
        (2346, 2349, 2377),
        (2347, 2362, 2379),
        (2348, 2363, 2380)
    ]
    for idx, (nsid, tsid, usid) in enumerate(r06f_sids):
        lvl = idx + 1
        wts_updates[nsid] = f"|cffe4cfa3Мастерство защиты — уровень {lvl}|r"
        wts_updates[tsid] = f"|cffe4cfa3Мастерство защиты — уровень {lvl}|r (|cffffffffD|r)"
        wts_updates[usid] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню героев врайкулов.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n"
            f"- |cffa9c7deТан|cffced4da, |cffa9c7deБерсерк|cffced4da, |cffa9c7deКороль Имирон|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}/3|r.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R06F", "field": f"name{lvl}", "expected": wts_updates[nsid]})
        checks_def.append({"type": "upgrade", "id": "R06F", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "upgrade", "id": "R06F", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # =========================================================================
    # 6. ABILITIES & BUFFS
    # =========================================================================
    # A0E3: Ярость севера (D)
    wts_updates[9970] = "|cffe4cfa3Ярость севера|r"
    wts_updates[8] = "|cffe4cfa3Ярость севера|r (|cffffffffD|r)"
    wts_updates[6519] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Кратковременно вводит воина в боевое неистовство, увеличивая скорость атаки на |cffc8e087+50%|cffced4da на |cffffffff12|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0E3", "field": "name", "expected": wts_updates[9970]})
    checks_def.append({"type": "ability", "id": "A0E3", "field": "tip1", "expected": wts_updates[8]})
    checks_def.append({"type": "ability", "id": "A0E3", "field": "ubertip1", "expected": wts_updates[6519]})

    # A0E4: Морозные клинки
    wts_updates[1151] = "|cffe4cfa3Морозные клинки|r"
    wts_updates[9974] = "|cffe4cfa3Морозные клинки|r"
    wts_updates[9976] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивное зачарование оружия холодом. Удары воина замедляют скорость передвижения цели на |cffe69a8d50%|cffced4da на |cffffffff3|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0E4", "field": "name", "expected": wts_updates[1151]})
    checks_def.append({"type": "ability", "id": "A0E4", "field": "tip1", "expected": wts_updates[9974]})
    checks_def.append({"type": "ability", "id": "A0E4", "field": "ubertip1", "expected": wts_updates[9976]})

    # A0E5: Защита (W)
    wts_updates[9977] = "|cffe4cfa3Защита|r"
    wts_updates[9978] = "|cffe4cfa3Защита|r (|cffffffffW|r)"
    checks_def.append({"type": "ability", "id": "A0E5", "field": "name", "expected": wts_updates[9977]})
    checks_def.append({"type": "ability", "id": "A0E5", "field": "tip1", "expected": wts_updates[9978]})

    # A0E7: Перейти в дальний бой (W)
    wts_updates[9990] = "|cffe4cfa3Перейти в дальний бой|r"
    wts_updates[9991] = "|cffe4cfa3Перейти в дальний бой|r (|cffffffffW|r)"
    wts_updates[9992] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Переключает Лендрмана в режим дальнего боя, позволяя метать копья по наземным целям.|r"
    checks_def.append({"type": "ability", "id": "A0E7", "field": "name", "expected": wts_updates[9990]})
    checks_def.append({"type": "ability", "id": "A0E7", "field": "tip1", "expected": wts_updates[9991]})
    checks_def.append({"type": "ability", "id": "A0E7", "field": "ubertip1", "expected": wts_updates[9992]})

    # A0E8: Точный удар
    wts_updates[0] = "|cffe4cfa3Точный удар|r"
    wts_updates[6] = "|cffe4cfa3Точный удар|r"
    wts_updates[16425] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff5%|cffced4da шанс нанести |cffc8e0872-кратный|cffced4da урон при каждой атаке.|r"
    checks_def.append({"type": "ability", "id": "A0E8", "field": "name", "expected": wts_updates[0]})
    checks_def.append({"type": "ability", "id": "A0E8", "field": "tip1", "expected": wts_updates[6]})
    checks_def.append({"type": "ability", "id": "A0E8", "field": "ubertip1", "expected": wts_updates[16425]})

    # A0E9: Дополнительные доспехи
    wts_updates[26] = "|cffe4cfa3Дополнительные доспехи|r"
    wts_updates[28] = "|cffe4cfa3Дополнительные доспехи|r"
    wts_updates[30] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает броню Скальда на |cffc8e087+3|cffced4da ед. и запас здоровья на |cffc8e087+150|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "A0E9", "field": "name", "expected": wts_updates[26]})
    checks_def.append({"type": "ability", "id": "A0E9", "field": "tip1", "expected": wts_updates[28]})
    checks_def.append({"type": "ability", "id": "A0E9", "field": "ubertip1", "expected": wts_updates[30]})

    # A0EA: Рассекающий удар
    wts_updates[31] = "|cffe4cfa3Рассекающий удар|r"
    wts_updates[32] = "|cffe4cfa3Рассекающий удар|r"
    wts_updates[42239] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивный сокрушительный удар, наносящий |cffffffff10%|cffced4da урона ближайшим вражеским войскам рядом с целью атаки.|r"
    checks_def.append({"type": "ability", "id": "A0EA", "field": "name", "expected": wts_updates[31]})
    checks_def.append({"type": "ability", "id": "A0EA", "field": "tip1", "expected": wts_updates[32]})
    checks_def.append({"type": "ability", "id": "A0EA", "field": "ubertip1", "expected": wts_updates[42239]})

    # A0EB: Ледяные стрелы (C)
    wts_updates[34] = "|cffe4cfa3Ледяные стрелы|r"
    wts_updates[35] = "|cffe4cfa3Ледяные стрелы|r (|cffffffffC|r)"
    wts_updates[25703] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Зачаровывает выстрелы магией льда, нанося |cffc8e087+25|cffced4da ед. дополнительного урона холодом и замедляя цель.|r"
    checks_def.append({"type": "ability", "id": "A0EB", "field": "name", "expected": wts_updates[34]})
    checks_def.append({"type": "ability", "id": "A0EB", "field": "tip1", "expected": wts_updates[35]})
    checks_def.append({"type": "ability", "id": "A0EB", "field": "ubertip1", "expected": wts_updates[25703]})

    # A0ED: Вдохновение (W)
    wts_updates[66] = "|cffe4cfa3Вдохновение|r"
    wts_updates[77] = "|cffe4cfa3Вдохновение|r (|cffffffffW|r)"
    wts_updates[79] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вдохновляет дружественного воина, повышая наносимый им урон на |cffc8e087+25%|cffced4da на |cffffffff45|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0ED", "field": "name", "expected": wts_updates[66]})
    checks_def.append({"type": "ability", "id": "A0ED", "field": "tip1", "expected": wts_updates[77]})
    checks_def.append({"type": "ability", "id": "A0ED", "field": "ubertip1", "expected": wts_updates[79]})

    # A0EE: Рассеивание заклинаний (E)
    wts_updates[81] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[82] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffE|r)"
    checks_def.append({"type": "ability", "id": "A0EE", "field": "name", "expected": wts_updates[81]})
    checks_def.append({"type": "ability", "id": "A0EE", "field": "tip1", "expected": wts_updates[82]})

    # A0EI: Ужасающий вой (W)
    wts_updates[216] = "|cffe4cfa3Ужасающий вой|r"
    wts_updates[220] = "|cffe4cfa3Ужасающий вой|r (|cffffffffW|r)"
    wts_updates[40260] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издаёт леденящий душу рёв, снижая силу атаки ближайших противников на |cffe69a8d-35%|cffced4da на |cffffffff15|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0EI", "field": "name", "expected": wts_updates[216]})
    checks_def.append({"type": "ability", "id": "A0EI", "field": "tip1", "expected": wts_updates[220]})
    checks_def.append({"type": "ability", "id": "A0EI", "field": "ubertip1", "expected": wts_updates[40260]})

    # A0EM: Аура безумия (4 levels, E)
    wts_updates[314] = "|cffe4cfa3Аура безумия|r"
    wts_updates[315] = "|cffe4cfa3Аура безумия|r"
    wts_updates[15340] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение и атаку союзных войск рядом с героем.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+10%|cffced4da к скорости бега, |cffc8e087+5%|cffced4da к атаке.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+20%|cffced4da к скорости бега, |cffc8e087+10%|cffced4da к атаке.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+30%|cffced4da к скорости бега, |cffc8e087+15%|cffced4da к атаке.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+40%|cffced4da к скорости бега, |cffc8e087+20%|cffced4da к атаке.|r"
    )
    checks_def.append({"type": "ability", "id": "A0EM", "field": "name", "expected": wts_updates[314]})
    checks_def.append({"type": "ability", "id": "A0EM", "field": "researchtip", "expected": wts_updates[315]})
    checks_def.append({"type": "ability", "id": "A0EM", "field": "researchubertip", "expected": wts_updates[15340]})

    a0em_tips = [316, 317, 318, 319]
    a0em_ubs = [15341, 15342, 15343, 15339]
    a0em_vals = [(10, 5), (20, 10), (30, 15), (40, 20)]
    for idx, (tsid, usid) in enumerate(zip(a0em_tips, a0em_ubs)):
        lvl = idx + 1
        mv, at = a0em_vals[idx]
        wts_updates[tsid] = f"|cffe4cfa3Аура безумия — уровень {lvl}|r"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения союзников на |cffc8e087+{mv}%|cffced4da и скорость боя на |cffc8e087+{at}%|cffced4da.|r"
        checks_def.append({"type": "ability", "id": "A0EM", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0EM", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0EO: Рунические топоры (4 levels)
    wts_updates[341] = "|cffe4cfa3Рунические топоры|r"
    wts_updates[342] = "|cffe4cfa3Рунические топоры|r"
    wts_updates[15349] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наполняет топоры рунической силой, замедляя цель каждой атакой.|n|n"
        "|cffa6afb8Уровень 1:|r замедление |cffe69a8d30%|cffced4da (2/5 сек.).|n"
        "|cffa6afb8Уровень 2:|r замедление |cffe69a8d40%|cffced4da (3/5 сек.).|n"
        "|cffa6afb8Уровень 3:|r замедление |cffe69a8d50%|cffced4da (4/5 сек.).|n"
        "|cffa6afb8Уровень 4:|r замедление |cffe69a8d60%|cffced4da (5/5 сек.).|r"
    )
    checks_def.append({"type": "ability", "id": "A0EO", "field": "name", "expected": wts_updates[341]})
    checks_def.append({"type": "ability", "id": "A0EO", "field": "researchtip", "expected": wts_updates[342]})
    checks_def.append({"type": "ability", "id": "A0EO", "field": "researchubertip", "expected": wts_updates[15349]})

    a0eo_tips = [345, 346, 347, 351]
    a0eo_ubs = [15350, 15351, 15352, 15353]
    a0eo_slows = [(30, 2), (40, 3), (50, 4), (60, 5)]
    for idx, (tsid, usid) in enumerate(zip(a0eo_tips, a0eo_ubs)):
        lvl = idx + 1
        pct, hero_dur = a0eo_slows[idx]
        wts_updates[tsid] = f"|cffe4cfa3Рунические топоры — уровень {lvl}|r"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Атаки героя замедляют цель на |cffe69a8d{pct}%|cffced4da на |cffffffff5|cffced4da сек. (|cffffffff{hero_dur}|cffced4da сек. героев).|r"
        checks_def.append({"type": "ability", "id": "A0EO", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0EO", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0EP: Аватар берсерка (2 levels, R)
    wts_updates[356] = "|cffe4cfa3Аватар берсерка|r"
    wts_updates[358] = "|cffe4cfa3Аватар берсерка|r"
    wts_updates[359] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Герой обращается в исполинского берсерка, получая невосприимчивость к магии, бонус к здоровью, броне и урону на 30 сек.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+300|cffced4da HP, |cffc8e087+4|cffced4da брони, |cffc8e087+15|cffced4da урона.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+600|cffced4da HP, |cffc8e087+8|cffced4da брони, |cffc8e087+30|cffced4da урона.|r"
    )
    wts_updates[363] = "|cffe4cfa3Аватар берсерка — уровень 1|r (|cffffffffR|r)"
    wts_updates[360] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Берсерк получает невосприимчивость к магии, |cffc8e087+300|cffced4da ед. здоровья, |cffc8e087+4|cffced4da брони и |cffc8e087+15|cffced4da урона на |cffffffff30|cffced4da сек.|r"
    wts_updates[366] = "|cffe4cfa3Аватар берсерка — уровень 2|r (|cffffffffR|r)"
    wts_updates[15354] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Берсерк получает невосприимчивость к магии, |cffc8e087+600|cffced4da ед. здоровья, |cffc8e087+8|cffced4da брони и |cffc8e087+30|cffced4da урона на |cffffffff30|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0EP", "field": "name", "expected": wts_updates[356]})
    checks_def.append({"type": "ability", "id": "A0EP", "field": "researchtip", "expected": wts_updates[358]})
    checks_def.append({"type": "ability", "id": "A0EP", "field": "researchubertip", "expected": wts_updates[359]})
    checks_def.append({"type": "ability", "id": "A0EP", "field": "tip1", "expected": wts_updates[363]})
    checks_def.append({"type": "ability", "id": "A0EP", "field": "ubertip1", "expected": wts_updates[360]})
    checks_def.append({"type": "ability", "id": "A0EP", "field": "tip2", "expected": wts_updates[366]})
    checks_def.append({"type": "ability", "id": "A0EP", "field": "ubertip2", "expected": wts_updates[15354]})

    # A0EQ: Тяжелые доспехи (4 levels, W)
    wts_updates[486] = "|cffe4cfa3Тяжелые доспехи|r"
    wts_updates[487] = "|cffe4cfa3Тяжелые доспехи|r"
    wts_updates[15355] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивно увеличивает броню героя тяжелыми защитными пластинами.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+3|cffced4da к броне.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+4|cffced4da к броне.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+5|cffced4da к броне.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+6|cffced4da к броне.|r"
    )
    checks_def.append({"type": "ability", "id": "A0EQ", "field": "name", "expected": wts_updates[486]})
    checks_def.append({"type": "ability", "id": "A0EQ", "field": "researchtip", "expected": wts_updates[487]})
    checks_def.append({"type": "ability", "id": "A0EQ", "field": "researchubertip", "expected": wts_updates[15355]})

    a0eq_tips = [491, 494, 498, 497]
    a0eq_ubs = [40059, 40057, 40058, 15358]
    a0eq_vals = [3, 4, 5, 6]
    for idx, (tsid, usid) in enumerate(zip(a0eq_tips, a0eq_ubs)):
        lvl = idx + 1
        arm = a0eq_vals[idx]
        wts_updates[tsid] = f"|cffe4cfa3Тяжелые доспехи — уровень {lvl}|r"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает броню героя на |cffc8e087+{arm}|cffced4da ед.|r"
        checks_def.append({"type": "ability", "id": "A0EQ", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0EQ", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0ER: Яростный удар (4 levels, Q)
    wts_updates[537] = "|cffe4cfa3Яростный удар|r"
    wts_updates[538] = "|cffe4cfa3Яростный удар|r"
    wts_updates[31431] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит сокрушительный рассекающий удар в секторе перед собой, вызывая кровотечение у врагов.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087100|cffced4da ед. мгновенно, |cffc8e08710|cffced4da ед./с на 5 сек.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087175|cffced4da ед. мгновенно, |cffc8e08715|cffced4da ед./с на 5 сек.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087250|cffced4da ед. мгновенно, |cffc8e08720|cffced4da ед./с на 5 сек.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087350|cffced4da ед. мгновенно, |cffc8e08730|cffced4da ед./с на 5 сек.|r"
    )
    checks_def.append({"type": "ability", "id": "A0ER", "field": "name", "expected": wts_updates[537]})
    checks_def.append({"type": "ability", "id": "A0ER", "field": "researchtip", "expected": wts_updates[538]})
    checks_def.append({"type": "ability", "id": "A0ER", "field": "researchubertip", "expected": wts_updates[31431]})

    a0er_tips = [566, 583, 594, 596]
    a0er_ubs = [15361, 15362, 15363, 15364]
    a0er_dmgs = [(100, 10), (175, 15), (250, 20), (350, 30)]
    for idx, (tsid, usid) in enumerate(zip(a0er_tips, a0er_ubs)):
        lvl = idx + 1
        dmg, dot = a0er_dmgs[idx]
        wts_updates[tsid] = f"|cffe4cfa3Яростный удар — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffc8e087{dmg}|cffced4da ед. урона в секторе перед героем и вызывает кровотечение на |cffc8e087{dot}|cffced4da ед./с в течение |cffffffff5|cffced4da сек.|r"
        checks_def.append({"type": "ability", "id": "A0ER", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0ER", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0ES: Сокрушение (4 levels, E)
    wts_updates[656] = "|cffe4cfa3Сокрушение|r"
    wts_updates[688] = "|cffe4cfa3Сокрушение|r"
    wts_updates[15406] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс при атаке нанести сокрушительный круговой урон всем окружающим врагам.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff15%|cffced4da шанс, |cffc8e08725|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff20%|cffced4da шанс, |cffc8e08750|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff25%|cffced4da шанс, |cffc8e08775|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff30%|cffced4da шанс, |cffc8e087100|cffced4da ед. урона.|r"
    )
    checks_def.append({"type": "ability", "id": "A0ES", "field": "name", "expected": wts_updates[656]})
    checks_def.append({"type": "ability", "id": "A0ES", "field": "researchtip", "expected": wts_updates[688]})
    checks_def.append({"type": "ability", "id": "A0ES", "field": "researchubertip", "expected": wts_updates[15406]})

    a0es_tips = [658, 714, 716, 722]
    a0es_ubs = [15368, 15369, 15366, 15367]
    a0es_chances = [(15, 25), (20, 50), (25, 75), (30, 100)]
    for idx, (tsid, usid) in enumerate(zip(a0es_tips, a0es_ubs)):
        lvl = idx + 1
        ch, edmg = a0es_chances[idx]
        wts_updates[tsid] = f"|cffe4cfa3Сокрушение — уровень {lvl}|r"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff{ch}%|cffced4da атака наносит |cffc8e087{edmg}|cffced4da ед. кругового урона окружающим врагам.|r"
        checks_def.append({"type": "ability", "id": "A0ES", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0ES", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0ET: Зов (2 levels, R)
    wts_updates[768] = "|cffe4cfa3Зов|r"
    wts_updates[773] = "|cffe4cfa3Зов|r"
    wts_updates[770] = "|cffe4cfa3Зов — уровень 1|r (|cffffffffR|r)"
    wts_updates[15371] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура вождя, повышающая броню окружающих союзных войск на |cffc8e087+3|cffced4da ед.|r"
    wts_updates[777] = "|cffe4cfa3Зов — уровень 2|r (|cffffffffR|r)"
    wts_updates[15372] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура вождя, повышающая броню окружающих союзных войск на |cffc8e087+5|cffced4da ед.|r"
    checks_def.append({"type": "ability", "id": "A0ET", "field": "name", "expected": wts_updates[768]})
    checks_def.append({"type": "ability", "id": "A0ET", "field": "tip1", "expected": wts_updates[770]})
    checks_def.append({"type": "ability", "id": "A0ET", "field": "ubertip1", "expected": wts_updates[15371]})
    checks_def.append({"type": "ability", "id": "A0ET", "field": "tip2", "expected": wts_updates[777]})
    checks_def.append({"type": "ability", "id": "A0ET", "field": "ubertip2", "expected": wts_updates[15372]})

    # A0EU: Помощь Предков (4 levels, Q)
    wts_updates[807] = "|cffe4cfa3Помощь Предков|r"
    wts_updates[809] = "|cffe4cfa3Помощь Предков|r"
    wts_updates[15373] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает указанную область сгустками духов предков, нанося урон врагам.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e08760|cffced4da ед. урона/волну.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087110|cffced4da ед. урона/волну.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087160|cffced4da ед. урона/волну.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087220|cffced4da ед. урона/волну.|r"
    )
    checks_def.append({"type": "ability", "id": "A0EU", "field": "name", "expected": wts_updates[807]})
    checks_def.append({"type": "ability", "id": "A0EU", "field": "researchtip", "expected": wts_updates[809]})
    checks_def.append({"type": "ability", "id": "A0EU", "field": "researchubertip", "expected": wts_updates[15373]})

    a0eu_tips = [815, 816, 817, 820]
    a0eu_ubs = [15374, 15375, 15376, 15377]
    a0eu_dmgs = [60, 110, 160, 220]
    for idx, (tsid, usid) in enumerate(zip(a0eu_tips, a0eu_ubs)):
        lvl = idx + 1
        d = a0eu_dmgs[idx]
        wts_updates[tsid] = f"|cffe4cfa3Помощь Предков — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обстреливает выбранную область духами предков, нанося |cffc8e087{d}|cffced4da ед. урона за каждую волну.|r"
        checks_def.append({"type": "ability", "id": "A0EU", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0EU", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0EV: Руны защиты (4 levels, W)
    wts_updates[843] = "|cffe4cfa3Руны защиты|r"
    wts_updates[846] = "|cffe4cfa3Руны защиты|r"
    wts_updates[15407] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит магические защитные руны на доспехи союзников вокруг жреца.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+3|cffced4da к броне.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+5|cffced4da к броне.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+7|cffced4da к броне.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+9|cffced4da к броне.|r"
    )
    checks_def.append({"type": "ability", "id": "A0EV", "field": "name", "expected": wts_updates[843]})
    checks_def.append({"type": "ability", "id": "A0EV", "field": "researchtip", "expected": wts_updates[846]})
    checks_def.append({"type": "ability", "id": "A0EV", "field": "researchubertip", "expected": wts_updates[15407]})

    a0ev_tips = [850, 854, 858, 860]
    a0ev_ubs = [15408, 15409, 15410, 15411]
    a0ev_armors = [3, 5, 7, 9]
    for idx, (tsid, usid) in enumerate(zip(a0ev_tips, a0ev_ubs)):
        lvl = idx + 1
        arm = a0ev_armors[idx]
        wts_updates[tsid] = f"|cffe4cfa3Руны защиты — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзников руническим щитом, повышая их броню на |cffc8e087+{arm}|cffced4da ед. на |cffffffff30|cffced4da сек.|r"
        checks_def.append({"type": "ability", "id": "A0EV", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0EV", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0EW: Руны проклятия (4 levels)
    wts_updates[943] = "|cffe4cfa3Руны проклятия|r"
    wts_updates[962] = "|cffe4cfa3Руны проклятия|r"
    wts_updates[15412] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Жрец проклинает атакуемые цели рунами увядания, нанося периодический урон.|n|n"
        "|cffa6afb8Уровень 1:|r |cffe69a8d10|cffced4da ед./с на 8 сек.|n"
        "|cffa6afb8Уровень 2:|r |cffe69a8d18|cffced4da ед./с на 8 сек.|n"
        "|cffa6afb8Уровень 3:|r |cffe69a8d26|cffced4da ед./с на 8 сек.|n"
        "|cffa6afb8Уровень 4:|r |cffe69a8d35|cffced4da ед./с на 8 сек.|r"
    )
    checks_def.append({"type": "ability", "id": "A0EW", "field": "name", "expected": wts_updates[943]})
    checks_def.append({"type": "ability", "id": "A0EW", "field": "researchtip", "expected": wts_updates[962]})
    checks_def.append({"type": "ability", "id": "A0EW", "field": "researchubertip", "expected": wts_updates[15412]})

    a0ew_tips = [961, 966, 967, 968]
    a0ew_ubs = [974, 975, 976, 978]
    a0ew_dots = [10, 18, 26, 35]
    for idx, (tsid, usid) in enumerate(zip(a0ew_tips, a0ew_ubs)):
        lvl = idx + 1
        dot = a0ew_dots[idx]
        wts_updates[tsid] = f"|cffe4cfa3Руны проклятия — уровень {lvl}|r"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Проклинает атакуемых врагов, нанося им |cffe69a8d{dot}|cffced4da ед. урона в секунду в течение |cffffffff8|cffced4da сек.|r"
        checks_def.append({"type": "ability", "id": "A0EW", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0EW", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0EX: Руны Спасения (2 levels, R)
    wts_updates[980] = "|cffe4cfa3Руны Спасения|r"
    wts_updates[981] = "|cffe4cfa3Руны Спасения|r"
    wts_updates[15415] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает священные руны жизни, полностью исцеляя союзные войска в широком радиусе.|n|n"
        "|cffa6afb8Уровень 1:|r восстанавливает здоровье союзников.|n"
        "|cffa6afb8Уровень 2:|r восстанавливает здоровье и сокращает перезарядку.|r"
    )
    wts_updates[982] = "|cffe4cfa3Руны Спасения — уровень 1|r (|cffffffffR|r)"
    wts_updates[15413] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует целебные руны, полностью восстанавливая здоровье всем окружающим союзным войскам.|r"
    wts_updates[984] = "|cffe4cfa3Руны Спасения — уровень 2|r (|cffffffffR|r)"
    wts_updates[15414] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Активирует высшие целебные руны, мгновенно восстанавливая все жизненные силы окружающих союзников.|r"
    checks_def.append({"type": "ability", "id": "A0EX", "field": "name", "expected": wts_updates[980]})
    checks_def.append({"type": "ability", "id": "A0EX", "field": "researchtip", "expected": wts_updates[981]})
    checks_def.append({"type": "ability", "id": "A0EX", "field": "researchubertip", "expected": wts_updates[15415]})
    checks_def.append({"type": "ability", "id": "A0EX", "field": "tip1", "expected": wts_updates[982]})
    checks_def.append({"type": "ability", "id": "A0EX", "field": "ubertip1", "expected": wts_updates[15413]})
    checks_def.append({"type": "ability", "id": "A0EX", "field": "tip2", "expected": wts_updates[984]})
    checks_def.append({"type": "ability", "id": "A0EX", "field": "ubertip2", "expected": wts_updates[15414]})

    # A0EY: Изнурение (4 levels, X)
    wts_updates[1008] = "|cffe4cfa3Изнурение|r"
    wts_updates[1056] = "|cffe4cfa3Изнурение|r"
    wts_updates[1057] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура короля, подавляющая боевой дух врагов и замедляющая их передвижение и атаку.|n|n"
        "|cffa6afb8Уровень 1:|r замедление на |cffe69a8d10%|cffced4da.|n"
        "|cffa6afb8Уровень 2:|r замедление на |cffe69a8d18%|cffced4da.|n"
        "|cffa6afb8Уровень 3:|r замедление на |cffe69a8d26%|cffced4da.|n"
        "|cffa6afb8Уровень 4:|r замедление на |cffe69a8d35%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A0EY", "field": "name", "expected": wts_updates[1008]})
    checks_def.append({"type": "ability", "id": "A0EY", "field": "researchtip", "expected": wts_updates[1056]})
    checks_def.append({"type": "ability", "id": "A0EY", "field": "researchubertip", "expected": wts_updates[1057]})

    a0ey_tips = [1009, 1014, 1025, 1028]
    a0ey_ubs = [1012, 1013, 1026, 1027]
    a0ey_slows = [10, 18, 26, 35]
    for idx, (tsid, usid) in enumerate(zip(a0ey_tips, a0ey_ubs)):
        lvl = idx + 1
        sl = a0ey_slows[idx]
        wts_updates[tsid] = f"|cffe4cfa3Изнурение — уровень {lvl}|r"
        wts_updates[usid] = f"|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость передвижения и боя ближайших врагов на |cffe69a8d{sl}%|cffced4da.|r"
        checks_def.append({"type": "ability", "id": "A0EY", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
        checks_def.append({"type": "ability", "id": "A0EY", "field": f"ubertip{lvl}", "expected": wts_updates[usid]})

    # A0EZ: Сильный Удар (4 levels, E)
    wts_updates[1058] = "|cffe4cfa3Сильный Удар|r"
    wts_updates[1059] = "|cffe4cfa3Сильный Удар|r"
    a0ez_tips = [1060, 1061, 1062, 1063]
    for idx, tsid in enumerate(a0ez_tips):
        lvl = idx + 1
        wts_updates[tsid] = f"|cffe4cfa3Сильный Удар — уровень {lvl}|r"
        checks_def.append({"type": "ability", "id": "A0EZ", "field": f"tip{lvl}", "expected": wts_updates[tsid]})
    wts_updates[1064] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс оглушить врага при ударе и нанести дополнительный урон.|r"
    checks_def.append({"type": "ability", "id": "A0EZ", "field": "name", "expected": wts_updates[1058]})
    checks_def.append({"type": "ability", "id": "A0EZ", "field": "ubertip4", "expected": wts_updates[1064]})

    # A0F1: Северный доспех (Q)
    wts_updates[55] = "|cffe4cfa3Северный доспех|r"
    wts_updates[59] = "|cffe4cfa3Северный доспех|r (|cffffffffQ|r)"
    wts_updates[1142] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает дружественного воина покровом льда, увеличивая его защиту на |cffc8e087+3|cffced4da ед. на |cffffffff30|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0F1", "field": "name", "expected": wts_updates[55]})
    checks_def.append({"type": "ability", "id": "A0F1", "field": "tip1", "expected": wts_updates[59]})
    checks_def.append({"type": "ability", "id": "A0F1", "field": "ubertip1", "expected": wts_updates[1142]})

    # A0YQ: Рассекающий Удар
    wts_updates[22783] = "|cffe4cfa3Рассекающий Удар|r"
    checks_def.append({"type": "ability", "id": "A0YQ", "field": "tip1", "expected": wts_updates[22783]})

    # A0Z1: Рев (2 levels, R)
    wts_updates[23285] = "|cffe4cfa3Рёв|r"
    wts_updates[23283] = "|cffe4cfa3Рёв|r"
    wts_updates[23284] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издаёт громогласный боевой клич, временно увеличивая урон и броню союзников вокруг короля.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+35%|cffced4da к урону, |cffc8e087+6|cffced4da к броне.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+40%|cffced4da к урону, |cffc8e087+8|cffced4da к броне.|r"
    )
    wts_updates[23279] = "|cffe4cfa3Рёв — уровень 1|r (|cffffffffR|r)"
    wts_updates[32881] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон союзников на |cffc8e087+35%|cffced4da и броню на |cffc8e087+6|cffced4da ед. на |cffffffff30|cffced4da сек.|r"
    wts_updates[23280] = "|cffe4cfa3Рёв — уровень 2|r (|cffffffffR|r)"
    wts_updates[32924] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон союзников на |cffc8e087+40%|cffced4da и броню на |cffc8e087+8|cffced4da ед. на |cffffffff30|cffced4da сек.|r"
    checks_def.append({"type": "ability", "id": "A0Z1", "field": "name", "expected": wts_updates[23285]})
    checks_def.append({"type": "ability", "id": "A0Z1", "field": "researchtip", "expected": wts_updates[23283]})
    checks_def.append({"type": "ability", "id": "A0Z1", "field": "researchubertip", "expected": wts_updates[23284]})
    checks_def.append({"type": "ability", "id": "A0Z1", "field": "tip1", "expected": wts_updates[23279]})
    checks_def.append({"type": "ability", "id": "A0Z1", "field": "ubertip1", "expected": wts_updates[32881]})
    checks_def.append({"type": "ability", "id": "A0Z1", "field": "tip2", "expected": wts_updates[23280]})
    checks_def.append({"type": "ability", "id": "A0Z1", "field": "ubertip2", "expected": wts_updates[32924]})

    # wk03: Защита (Всадник, Q)
    wts_updates[40074] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Всадник поднимает тяжелый щит, снижая урон от дальних атак до |cffc8e08790%|cffced4da ценой скорости движения.|r"
    checks_def.append({"type": "ability", "id": "wk03", "field": "ubertip1", "expected": wts_updates[40074]})

    # wk04: Пробитие доспехов (Q)
    wts_updates[40303] = "|cffe4cfa3Пробитие доспехов|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "wk04", "field": "tip1", "expected": wts_updates[40303]})

    # wk07: Каменная кожа (Броня из драконьей чешуи)
    wts_updates[40307] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Плотная чешуя протодракона поглощает до |cffc8e08718|cffced4da ед. физического урона от каждой входящей атаки.|r"
    checks_def.append({"type": "ability", "id": "wk07", "field": "ubertip1", "expected": wts_updates[40307]})

    # wk09: Оживление мертвых (Q)
    wts_updates[3046] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает души павших, поднимая до |cffffffff3|cffced4da трупов в виде нежити на поле боя.|r"
    checks_def.append({"type": "ability", "id": "wk09", "field": "ubertip1", "expected": wts_updates[3046]})

    # wk10: Нечистая аура
    wts_updates[40404] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость перемещения союзников на |cffc8e087+15%|cffced4da и ускоряет регенерацию здоровья.|r"
    checks_def.append({"type": "ability", "id": "wk10", "field": "ubertip1", "expected": wts_updates[40404]})

    # Buffs: B033, B034, B037, B038, B03A, B03B
    wts_updates[9972] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки воина увеличена под действием ярости севера.|r"
    wts_updates[83] = "|cffe4cfa3Вдохновение|r"
    wts_updates[84] = "|cffa6afb8ЭФФЕКТ:|cffced4da Сила атаки воина повышена на |cffc8e087+25%|cffced4da под действием вдохновения.|r"
    wts_updates[448] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость боя и передвижения воина увеличена под действием ауры безумия.|r"
    wts_updates[449] = "|cffe4cfa3Рунические топоры|r"
    wts_updates[450] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость передвижения цели замедлена руническими чарами.|r"
    wts_updates[631] = "|cffa6afb8ЭФФЕКТ:|cffced4da Броня воина усилена тяжелыми защитными доспехами.|r"
    wts_updates[633] = "|cffa6afb8ЭФФЕКТ:|cffe69a8d Юнит истекает кровью от яростного удара и получает периодический урон.|r"

    checks_def.append({"type": "buff", "id": "B033", "field": "bufftip", "expected": wts_updates[9972]})
    checks_def.append({"type": "buff", "id": "B034", "field": "bufftip", "expected": wts_updates[83]})
    checks_def.append({"type": "buff", "id": "B034", "field": "buffubertip", "expected": wts_updates[84]})
    checks_def.append({"type": "buff", "id": "B037", "field": "bufftip", "expected": wts_updates[448]})
    checks_def.append({"type": "buff", "id": "B038", "field": "bufftip", "expected": wts_updates[449]})
    checks_def.append({"type": "buff", "id": "B038", "field": "buffubertip", "expected": wts_updates[450]})
    checks_def.append({"type": "buff", "id": "B03A", "field": "bufftip", "expected": wts_updates[631]})
    checks_def.append({"type": "buff", "id": "B03B", "field": "bufftip", "expected": wts_updates[633]})

    # =========================================================================
    # 7. REGISTRIES & MASTER PLAN
    # =========================================================================
    selection_registry = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "selection_ability": "A0HP",
        "strings": {
            "38871": {"field": "name", "text": wts_updates[38871]},
            "38872": {"field": "tip1", "text": wts_updates[38872]},
            "35175": {"field": "ubertip1", "text": wts_updates[35175]}
        }
    }
    (folder / "vrykul_selection.json").write_text(json.dumps(selection_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    buildings_registry = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "buildings": ["h0BQ", "h0BR", "h0BS", "h0BT", "h0BU", "h0BV", "h0BW", "h0BX", "wk01"],
        "count": 9
    }
    (folder / "vrykul_buildings.json").write_text(json.dumps(buildings_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    heroes_registry = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "heroes": ["H0C4", "H0C5", "H0C6", "H0C7"],
        "count": 4
    }
    (folder / "vrykul_heroes.json").write_text(json.dumps(heroes_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    units_registry = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "units": ["h0C9", "h0AA", "h0AD", "h0A5", "h0A6", "h0BP", "h0A9", "h0AC", "h0AE", "wk08", "wk02", "wk00", "h0A8", "h0A7"],
        "count": 14
    }
    (folder / "vrykul_units.json").write_text(json.dumps(units_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    research_registry = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "upgrades": ["R05Z", "R060", "R061", "R062", "R063", "R064", "R065", "R066", "R067", "R068", "R069", "R06A", "R06B", "R06C", "R06D", "R06E", "R06F", "R07F"],
        "count": 18
    }
    (folder / "vrykul_research.json").write_text(json.dumps(research_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    abilities_registry = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "abilities": [
            "A0E3", "A0E4", "A0E5", "A0E7", "A0E8", "A0E9", "A0EA", "A0EB",
            "A0ED", "A0EE", "A0EI", "A0EM", "A0EN", "A0EO", "A0EP", "A0EQ",
            "A0ER", "A0ES", "A0ET", "A0EU", "A0EV", "A0EW", "A0EX", "A0EY",
            "A0EZ", "A0F1", "A0YQ", "A0Z1", "wk03", "wk04", "wk07", "wk09", "wk10"
        ],
        "buffs": ["B033", "B034", "B037", "B038", "B03A", "B03B"],
        "count": 39
    }
    (folder / "vrykul_abilities.json").write_text(json.dumps(abilities_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    audit_registry = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "items": "Аудит подтвердил отсутствие собственных расовых предметов у зданий Врайкулов.",
        "messages": "Аудит подтвердил отсутствие специальных текстовых сообщений игроку в триггерах Vryculs.lua.",
        "interfaces": "Аудит подтвердил отсутствие специальных фреймов интерфейса Врайкулов."
    }
    (folder / "vrykul_audit.json").write_text(json.dumps(audit_registry, ensure_ascii=False, indent=2), encoding="utf-8")

    master_plan = {
        "race": "Vryculs",
        "race_name_ru": "Врайкулы",
        "race_id": 36,
        "wts_updates": {str(k): v for k, v in wts_updates.items()},
        "checks_def": checks_def
    }
    (folder / "vrykul_plan.json").write_text(json.dumps(master_plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Prepared Vryculs plan: {len(wts_updates)} WTS strings, {len(checks_def)} checks.")

if __name__ == '__main__':
    main()
