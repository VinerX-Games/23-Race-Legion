# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and category registries for Race 25: Nagi (Наги)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    # =========================================================================
    # 1. RACE SELECTION & TECH MARKERS
    # =========================================================================
    # A14O: Выбор расы Наги
    wts_updates[38901] = "|cffe4cfa3Наги|r"
    wts_updates[38902] = "|cffe4cfa3Наги|r (|cffffffffD|r)"
    wts_updates[32513] = (
        "|cffa6afb8РАСА:|cffced4da Древний змееподобный народ глубин под предводительством королевы Азшары, повелевающий водной стихией, штормами и армиями мурлоков.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●|cffa6afb8○○○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Cataclysm»|r|n|n"
        "|cffced4daНаги — древний змееподобный народ, обитающий в глубинах океанов и на побережьях Азерота. Бывшие высокорождённые эльфы королевы Азшары, "
        "преображённые шёпотом Древних богов на дне Великого моря, создали могущественную империю Назжатар. Владея разрушительной магией воды и молний, "
        "подчиняя свирепых морских чудовищ и орды преданных мурлоков, наги выходят на сушу, дабы сокрушить всех врагов своей бессмертной владычицы.|r"
    )
    checks_def.append({"type": "ability", "id": "A14O", "field": "name", "expected": wts_updates[38901]})
    checks_def.append({"type": "ability", "id": "A14O", "field": "tip1", "expected": wts_updates[38902]})
    checks_def.append({"type": "ability", "id": "A14O", "field": "ubertip1", "expected": wts_updates[32513]})

    # R0FS: Служебный маркер расы Наги
    wts_updates[43187] = "|cffe4cfa3Наги|r"
    wts_updates[43188] = "|cffe4cfa3Наги|r"
    wts_updates[43189] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к расе Нагов (Империя Назжатар).|r"
    checks_def.append({"type": "upgrade", "id": "R0FS", "field": "name1", "expected": wts_updates[43187]})
    checks_def.append({"type": "upgrade", "id": "R0FS", "field": "tip1", "expected": wts_updates[43188]})
    checks_def.append({"type": "upgrade", "id": "R0FS", "field": "ubertip1", "expected": wts_updates[43189]})

    # R0KZ: Маркер союза Иллидари или Наги
    wts_updates[5721] = "|cffe4cfa3Иллидари или Наги|r"
    wts_updates[9416] = "|cffe4cfa3Иллидари или Наги|r"
    wts_updates[12518] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер союза Иллидари и Нагов в борьбе против общего врага.|r"
    checks_def.append({"type": "upgrade", "id": "R0KZ", "field": "name1", "expected": wts_updates[5721]})
    checks_def.append({"type": "upgrade", "id": "R0KZ", "field": "tip1", "expected": wts_updates[9416]})
    checks_def.append({"type": "upgrade", "id": "R0KZ", "field": "ubertip1", "expected": wts_updates[12518]})

    # =========================================================================
    # 2. BUILDINGS (10 buildings)
    # =========================================================================
    # h0JW: Коралловая кузница (E)
    wts_updates[42986] = "|cffe4cfa3Коралловая кузница|r"
    wts_updates[42987] = "|cffe4cfa3Коралловая кузница|r (|cffffffffE|r)"
    wts_updates[42985] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оружейная нагов. Позволяет исследовать улучшения оружия, брони и особых боевых навыков войск.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deКоралловые клинки|cffced4da: увеличивает урон войск нагов и мурлоков.|n"
        "- |cffa9c7deКоралловая чешуя|cffced4da: повышает броню войск нагов и мурлоков.|n"
        "- |cffa9c7deУлучшенный хват|cffced4da: увеличивает вместимость древесины для рабочих.|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: даёт мурлокам и черепахам отражение урона в ближнем бою.|n"
        "- |cffa9c7deПогружение|cffced4da: позволяет бойцам погружаться под воду, становясь невидимыми.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JW", "field": "name", "expected": wts_updates[42986]})
    checks_def.append({"type": "unit", "id": "h0JW", "field": "tip", "expected": wts_updates[42987]})
    checks_def.append({"type": "unit", "id": "h0JW", "field": "ubertip", "expected": wts_updates[42985]})

    # h0JX: Храм Бездны (Z)
    wts_updates[42992] = "|cffe4cfa3Храм Бездны|r"
    wts_updates[42991] = "|cffe4cfa3Храм Бездны|r (|cffffffffZ|r)"
    wts_updates[42993] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание нагов второй ступени. Служит центром сбора ресурсов и увеличивает запас пищи.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deРаб мурлоков|cffced4da: рабочий строитель и добытчик ресурсов.|n"
        "- |cffa9c7deМурлок-налётчик|cffced4da: лёгкий боец ближнего боя.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n"
        "- |cffa9c7deКоралловый храм|cffced4da: открывает доступ к высшим технологиям нагов.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JX", "field": "name", "expected": wts_updates[42992]})
    checks_def.append({"type": "unit", "id": "h0JX", "field": "tip", "expected": wts_updates[42991]})
    checks_def.append({"type": "unit", "id": "h0JX", "field": "ubertip", "expected": wts_updates[42993]})

    # h0JY: Коралловый храм (Z)
    wts_updates[42994] = "|cffe4cfa3Коралловый храм|r"
    wts_updates[42995] = "|cffe4cfa3Коралловый храм|r (|cffffffffZ|r)"
    wts_updates[42996] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание нагов третьей ступени. Обеспечивает максимальный запас пищи и открывает высшие технологии расы.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deРаб мурлоков|cffced4da: рабочий строитель и добытчик ресурсов.|n"
        "- |cffa9c7deМурлок-налётчик|cffced4da: лёгкий боец ближнего боя.|r"
    )
    checks_def.append({"type": "unit", "id": "h0JY", "field": "name", "expected": wts_updates[42994]})
    checks_def.append({"type": "unit", "id": "h0JY", "field": "tip", "expected": wts_updates[42995]})
    checks_def.append({"type": "unit", "id": "h0JY", "field": "ubertip", "expected": wts_updates[42996]})

    # n04L: Змеиное логово (X)
    wts_updates[43006] = "|cffe4cfa3Змеиное логово|r"
    wts_updates[43007] = "|cffe4cfa3Змеиное логово|r (|cffffffffX|r)"
    wts_updates[43008] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Специализированное логово для призыва исполинских морских змеев.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deМорской змей|cffced4da: мощный тяжелобронированный гигант с хаотической атакой и ядовитым плевком.|r"
    )
    checks_def.append({"type": "unit", "id": "n04L", "field": "name", "expected": wts_updates[43006]})
    checks_def.append({"type": "unit", "id": "n04L", "field": "tip", "expected": wts_updates[43007]})
    checks_def.append({"type": "unit", "id": "n04L", "field": "ubertip", "expected": wts_updates[43008]})

    # n055: Морские врата (D)
    wts_updates[42982] = "|cffe4cfa3Морские врата|r"
    wts_updates[42983] = "|cffe4cfa3Морские врата|r (|cffffffffD|r)"
    wts_updates[42984] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военный портал глубин. Призывает элитных бойцов, морских охотников, тяжелых стражей и воздушных коатлей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deМурлок-мутант|cffced4da: свирепый гигант ближнего боя с хаотической атакой.|n"
        "- |cffa9c7deСтраж нагов|cffced4da: элитный тяжеловооружённый боец с ледяными стрелами и волной.|n"
        "- |cffa9c7deМорской охотник|cffced4da: ловкий боец ближнего боя со сокрушающим ударом и аурой.|n"
        "- |cffa9c7deКоатль|cffced4da: летающий стрелок поддержки, сжигающий ману противника.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deГосподство на море|cffced4da: увеличивает здоровье Мурлоков-мутантов.|n"
        "- |cffa9c7deСокрушительный удар|cffced4da: обучает Морских охотников оглушающему удару.|n"
        "- |cffa9c7deАнтимагический коатль|cffced4da: обучает Коатлей сжиганию маны при атаке.|r"
    )
    checks_def.append({"type": "unit", "id": "n055", "field": "name", "expected": wts_updates[42982]})
    checks_def.append({"type": "unit", "id": "n055", "field": "tip", "expected": wts_updates[42983]})
    checks_def.append({"type": "unit", "id": "n055", "field": "ubertip", "expected": wts_updates[42984]})

    # nnfm: Коралловый риф (A)
    wts_updates[31829] = "|cffe4cfa3Коралловый риф|r"
    wts_updates[35837] = "|cffe4cfa3Коралловый риф|r (|cffffffffA|r)"
    wts_updates[35937] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Ферма и источник дохода нагов. Обеспечивает войско пропитанием и приносит регулярный золотой доход.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит |cffffffff30|cffced4da ед. золота каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "nnfm", "field": "name", "expected": wts_updates[31829]})
    checks_def.append({"type": "unit", "id": "nnfm", "field": "tip", "expected": wts_updates[35837]})
    checks_def.append({"type": "unit", "id": "nnfm", "field": "ubertip", "expected": wts_updates[35937]})

    # nnsa: Святилище Азшары (R)
    wts_updates[28025] = "|cffe4cfa3Святилище Азшары|r"
    wts_updates[29009] = "|cffe4cfa3Святилище Азшары|r (|cffffffffR|r)"
    wts_updates[29010] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Магическое святилище королевы Азшары. Обучает заклинателей нагов и мурлоков.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deГлубинный житель|cffced4da: целитель и маг поддержки, владеющий рассеиванием чар.|n"
        "- |cffa9c7deСирена|cffced4da: могущественная волшебница, атакующая торнадо, паразитами и ледяной бронёй.|n"
        "- |cffa9c7deМурлок-чернокнижник|cffced4da: тёмный чародей, исцеляющий союзников и проклинающий врагов сглазом.|n"
        "- |cffa9c7deМурлок-шаман|cffced4da: повелитель молний, накладывающий щит молний и поражающий врагов цепной молнией.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deКоралловая магия|cffced4da: улучшает заклинателей поддержки.|n"
        "- |cffa9c7deСилы стихий|cffced4da: улучшает боевых магов.|r"
    )
    checks_def.append({"type": "unit", "id": "nnsa", "field": "name", "expected": wts_updates[28025]})
    checks_def.append({"type": "unit", "id": "nnsa", "field": "tip", "expected": wts_updates[29009]})
    checks_def.append({"type": "unit", "id": "nnsa", "field": "ubertip", "expected": wts_updates[29010]})

    # nnsg: Нерестилище (W)
    wts_updates[29028] = "|cffe4cfa3Нерестилище|r"
    wts_updates[29077] = "|cffe4cfa3Нерестилище|r (|cffffffffW|r)"
    wts_updates[29079] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Основное военное сооружение нагов. Подготавливает базовые наземные войска, стрелков и осадных черепах.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deВоин волн|cffced4da: базовый боец ближнего боя с шипастым панцирем.|n"
        "- |cffa9c7deМурлок-охотник|cffced4da: выносливый охотник, способный опутывать врагов сетью.|n"
        "- |cffa9c7deМирмидон|cffced4da: тяжелый воин нагов, опутывающий цели и погружающийся под воду.|n"
        "- |cffa9c7deМорской василиск|cffced4da: стрелок дальнего боя, замедляющий врагов ядовитыми иглами.|n"
        "- |cffa9c7deДраконья черепаха|cffced4da: гигантская бронированная осадная черепаха, сокрушающая здания врага.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deЗамедляющий яд|cffced4da: позволяет василискам отравлять атакованных врагов.|n"
        "- |cffa9c7deОпутывание|cffced4da: обучает мирмидонов прижимать воздушные и наземные цели к земле.|r"
    )
    checks_def.append({"type": "unit", "id": "nnsg", "field": "name", "expected": wts_updates[29028]})
    checks_def.append({"type": "unit", "id": "nnsg", "field": "tip", "expected": wts_updates[29077]})
    checks_def.append({"type": "unit", "id": "nnsg", "field": "ubertip", "expected": wts_updates[29079]})

    # nntg: Защитник приливов (Z)
    wts_updates[42941] = "|cffe4cfa3Защитник приливов|r"
    wts_updates[42942] = "|cffe4cfa3Защитник приливов|r (|cffffffffZ|r)"
    wts_updates[42943] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Основное защитное сооружение нагов. Ведёт скорострельный обстрел наземных и воздушных врагов, приближающихся к поселению.|r"
    )
    checks_def.append({"type": "unit", "id": "nntg", "field": "name", "expected": wts_updates[42941]})
    checks_def.append({"type": "unit", "id": "nntg", "field": "tip", "expected": wts_updates[42942]})
    checks_def.append({"type": "unit", "id": "nntg", "field": "ubertip", "expected": wts_updates[42943]})

    # nntt: Храм Глубин (Q)
    wts_updates[8060] = "|cffe4cfa3Храм Глубин|r"
    wts_updates[8036] = "|cffe4cfa3Храм Глубин|r (|cffffffffQ|r)"
    wts_updates[25675] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание нагов первой ступени. Обеспечивает запас пищи, добычу ресурсов и выбор пути развития королевства.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n"
        "- |cffa9c7deРаб мурлоков|cffced4da: рабочий строитель и добытчик ресурсов.|n"
        "- |cffa9c7deМурлок-налётчик|cffced4da: лёгкий боец ближнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n"
        "- |cffa9c7deВладычество нагов|cffced4da: открывает элитные войска нагов и героя Владыку-стража.|n"
        "- |cffa9c7deВладычество мурлоков|cffced4da: открывает орды мурлоков и героя Мурлока-гиганта.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n"
        "- |cffa9c7deХрам Бездны|cffced4da: открывает доступ к передовым сооружениям и технологиям.|r"
    )
    checks_def.append({"type": "unit", "id": "nntt", "field": "name", "expected": wts_updates[8060]})
    checks_def.append({"type": "unit", "id": "nntt", "field": "tip", "expected": wts_updates[8036]})
    checks_def.append({"type": "unit", "id": "nntt", "field": "ubertip", "expected": wts_updates[25675]})

    # =========================================================================
    # 3. WORKER & COMBAT UNITS (1 worker + 16 combat units)
    # =========================================================================
    # nmpe: Раб мурлоков (Q)
    wts_updates[42944] = "|cffe4cfa3Раб мурлоков|r"
    wts_updates[42945] = "|cffe4cfa3Раб мурлоков|r (|cffffffffQ|r)"
    wts_updates[42946] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основной рабочий нагов. Добывает золото и древесину, возводит и ремонтирует сооружения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткое расстояние.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: находясь в воде, получает бонус к скорости передвижения и атаки.|n"
        "- |cffa9c7deРемонт|cffced4da: восстанавливает прочность повреждённых зданий.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "nmpe", "field": "name", "expected": wts_updates[42944]})
    checks_def.append({"type": "unit", "id": "nmpe", "field": "tip", "expected": wts_updates[42945]})
    checks_def.append({"type": "unit", "id": "nmpe", "field": "ubertip", "expected": wts_updates[42946]})

    # n04Z: Воин волн (Q)
    wts_updates[42958] = "|cffe4cfa3Воин волн|r"
    wts_updates[42959] = "|cffe4cfa3Воин волн|r (|cffffffffQ|r)"
    wts_updates[42960] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец армии мурлоков. Оснащён шипастым панцирем, отражающим удары врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает часть урона, полученного в ближнем бою.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: находясь в воде, получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n04Z", "field": "name", "expected": wts_updates[42958]})
    checks_def.append({"type": "unit", "id": "n04Z", "field": "tip", "expected": wts_updates[42959]})
    checks_def.append({"type": "unit", "id": "n04Z", "field": "ubertip", "expected": wts_updates[42960]})

    # n050: Мурлок-мутант (Q)
    wts_updates[42961] = "|cffe4cfa3Мурлок-мутант|r"
    wts_updates[42962] = "|cffe4cfa3Мурлок-мутант|r (|cffffffffQ|r)"
    wts_updates[42963] = (
        "|cffa6afb8ЮНИТ:|cffced4da Чудовищный мутировавший мурлок ближнего боя с хаотическим типом атаки. Поедает трупы для регенерации и уклоняется от ударов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deКаннибализм|cffced4da: пожирает трупы поверженных врагов, восстанавливая здоровье.|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает урон противников в ближнем бою.|n"
        "- |cffa9c7deУклонение|cffced4da: даёт шанс избежать вражеской атаки.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и передвижения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n050", "field": "name", "expected": wts_updates[42961]})
    checks_def.append({"type": "unit", "id": "n050", "field": "tip", "expected": wts_updates[42962]})
    checks_def.append({"type": "unit", "id": "n050", "field": "ubertip", "expected": wts_updates[42963]})

    # n051: Глубинный житель (Q)
    wts_updates[42998] = "|cffe4cfa3Глубинный житель|r"
    wts_updates[42997] = "|cffe4cfa3Глубинный житель|r (|cffffffffQ|r)"
    wts_updates[42999] = (
        "|cffa6afb8ЮНИТ:|cffced4da Маг поддержки нагов дальнего боя. Исцеляет раненых соратников, рассеивает вражеские чары и ускоряет союзников приливом сил.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЦелительная вода|cffced4da: восстанавливает здоровье раненому союзнику.|n"
        "- |cffa9c7deРассеивание чар|cffced4da: снимает положительные эффекты с врагов и наносит урон призванным существам.|n"
        "- |cffa9c7deПрилив сил|cffced4da: аура, увеличивающая скорость передвижения ближайших войск.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n051", "field": "name", "expected": wts_updates[42998]})
    checks_def.append({"type": "unit", "id": "n051", "field": "tip", "expected": wts_updates[42997]})
    checks_def.append({"type": "unit", "id": "n051", "field": "ubertip", "expected": wts_updates[42999]})

    # n052: Мурлок-охотник (E)
    wts_updates[42976] = "|cffe4cfa3Мурлок-охотник|r"
    wts_updates[42977] = "|cffe4cfa3Мурлок-охотник|r (|cffffffffE|r)"
    wts_updates[42978] = (
        "|cffa6afb8ЮНИТ:|cffced4da Выносливый боец ближнего боя. Опутывает вражеские цели сетями, прижимая их к земле.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deОпутывание|cffced4da: притягивает воздушную цель к земле и лишает возможности двигаться.|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает часть урона в ближнем бою.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и передвижения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n052", "field": "name", "expected": wts_updates[42976]})
    checks_def.append({"type": "unit", "id": "n052", "field": "tip", "expected": wts_updates[42977]})
    checks_def.append({"type": "unit", "id": "n052", "field": "ubertip", "expected": wts_updates[42978]})

    # n053: Мурлок-чернокнижник (Q)
    wts_updates[42979] = "|cffe4cfa3Мурлок-чернокнижник|r"
    wts_updates[42980] = "|cffe4cfa3Мурлок-чернокнижник|r (|cffffffffQ|r)"
    wts_updates[42981] = (
        "|cffa6afb8ЮНИТ:|cffced4da Заклинатель мурлоков дальнего боя. Превращает противников в беспомощных животных, исцеляет союзников и рассеивает магию.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deСглаз|cffced4da: превращает вражеского воина в безобидное животное.|n"
        "- |cffa9c7deЦелительная вода|cffced4da: восстанавливает здоровье раненым войскам.|n"
        "- |cffa9c7deРассеивание чар|cffced4da: снимает заклинания в выбранной области.|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает урон в ближнем бою.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает прибавку к скорости атаки и перемещения.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n053", "field": "name", "expected": wts_updates[42979]})
    checks_def.append({"type": "unit", "id": "n053", "field": "tip", "expected": wts_updates[42980]})
    checks_def.append({"type": "unit", "id": "n053", "field": "ubertip", "expected": wts_updates[42981]})

    # n054: Мурлок-шаман (W)
    wts_updates[43003] = "|cffe4cfa3Мурлок-шаман|r"
    wts_updates[43004] = "|cffe4cfa3Мурлок-шаман|r (|cffffffffW|r)"
    wts_updates[43005] = (
        "|cffa6afb8ЮНИТ:|cffced4da Боевой маг мурлоков дальнего боя. Повелевает разрушительной мощью электрических разрядов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЦепь молний|cffced4da: поражает молнией несколько вражеских целей подряд.|n"
        "- |cffa9c7deЩит молний|cffced4da: окружает цель электрическим щитом, наносящим урон окружающим войскам.|n"
        "- |cffa9c7deСила молний|cffced4da: даёт шанс при атаке рассеять чары с поражённой цели.|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает урон в ближнем бою.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и передвижения.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n054", "field": "name", "expected": wts_updates[43003]})
    checks_def.append({"type": "unit", "id": "n054", "field": "tip", "expected": wts_updates[43004]})
    checks_def.append({"type": "unit", "id": "n054", "field": "ubertip", "expected": wts_updates[43005]})

    # n056: Морской охотник (E)
    wts_updates[42988] = "|cffe4cfa3Морской охотник|r"
    wts_updates[42989] = "|cffe4cfa3Морской охотник|r (|cffffffffE|r)"
    wts_updates[42990] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стремительный воин нагов ближнего боя. Наносит оглушающие удары и усиливает окружающих союзников боевой аурой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deСокрушение|cffced4da: даёт шанс нанести дополнительный урон и оглушить противника.|n"
        "- |cffa9c7deОпутывание|cffced4da: притягивает воздушную цель к земле и обездвиживает её.|n"
        "- |cffa9c7deСтойкость моря|cffced4da: аура, увеличивающая скорость атаки и перемещения окружающих союзников.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает прибавку к скорости атаки и перемещения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n056", "field": "name", "expected": wts_updates[42988]})
    checks_def.append({"type": "unit", "id": "n056", "field": "tip", "expected": wts_updates[42989]})
    checks_def.append({"type": "unit", "id": "n056", "field": "ubertip", "expected": wts_updates[42990]})

    # n057: Древний нага
    wts_updates[43001] = "|cffe4cfa3Древний нага|r"
    wts_updates[43000] = "|cffe4cfa3Древний нага|r"
    wts_updates[43002] = (
        "|cffa6afb8ЮНИТ:|cffced4da Невероятно сильный древний исполин нагов ближнего боя с хаотической атакой. Защищён устойчивой кожей и поражает врагов ледяными выпадами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЛедяная стрела|cffced4da: наносит урон врагу и оглушает его.|n"
        "- |cffa9c7deУстойчивая кожа|cffced4da: снижает время действия отрицательных эффектов и даёт устойчивость к магии.|n"
        "- |cffa9c7deПогружение|cffced4da: уходит под воду, становясь невидимым.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и передвижения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n057", "field": "name", "expected": wts_updates[43001]})
    checks_def.append({"type": "unit", "id": "n057", "field": "tip", "expected": wts_updates[43000]})
    checks_def.append({"type": "unit", "id": "n057", "field": "ubertip", "expected": wts_updates[43002]})

    # n079: Морской змей (Q)
    wts_updates[43009] = "|cffe4cfa3Морской змей|r"
    wts_updates[43010] = "|cffe4cfa3Морской змей|r (|cffffffffQ|r)"
    wts_updates[43011] = (
        "|cffa6afb8ЮНИТ:|cffced4da Громадный тяжелобронированный морской змей ближнего боя с хаотическим типом атаки. Плюётся разъедающей кислотой, ослабляющей броню врагов.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЕдкая слюна|cffced4da: кислотный плевок, наносящий урон по площади и снижающий броню противников.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "n079", "field": "name", "expected": wts_updates[43009]})
    checks_def.append({"type": "unit", "id": "n079", "field": "tip", "expected": wts_updates[43010]})
    checks_def.append({"type": "unit", "id": "n079", "field": "ubertip", "expected": wts_updates[43011]})

    # nmyr: Мирмидон (E)
    wts_updates[42929] = "|cffe4cfa3Мирмидон|r"
    wts_updates[42930] = "|cffe4cfa3Мирмидон|r (|cffffffffE|r)"
    wts_updates[42931] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжеловооружённый элитный пехотинец нагов ближнего боя. Опутывает врагов сетями и способен скрытно передвигаться под водой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deОпутывание|cffced4da: притягивает летающих врагов к земле и лишает подвижности.|n"
        "- |cffa9c7deПогружение|cffced4da: ныряет под воду, получая постоянную невидимость.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает прибавку к скорости атаки и перемещения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "nmyr", "field": "name", "expected": wts_updates[42929]})
    checks_def.append({"type": "unit", "id": "nmyr", "field": "tip", "expected": wts_updates[42930]})
    checks_def.append({"type": "unit", "id": "nmyr", "field": "ubertip", "expected": wts_updates[42931]})

    # nnmg: Мурлок-налётчик (W)
    wts_updates[42920] = "|cffe4cfa3Мурлок-налётчик|r"
    wts_updates[42921] = "|cffe4cfa3Мурлок-налётчик|r (|cffffffffW|r)"
    wts_updates[42922] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый легковооружённый пехотинец ближнего боя. Быстро обучается и защищён шипастым панцирем.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает урон противников в ближнем бою.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "nnmg", "field": "name", "expected": wts_updates[42920]})
    checks_def.append({"type": "unit", "id": "nnmg", "field": "tip", "expected": wts_updates[42921]})
    checks_def.append({"type": "unit", "id": "nnmg", "field": "ubertip", "expected": wts_updates[42922]})

    # nnrg: Страж нагов (Q)
    wts_updates[42933] = "|cffe4cfa3Страж нагов|r"
    wts_updates[42932] = "|cffe4cfa3Страж нагов|r (|cffffffffQ|r)"
    wts_updates[42934] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный королевский страж нагов ближнего боя с хаотическим типом атаки. Выпускает сокрушительные волны, поражает врагов ледяными стрелами и защищён устойчивой кожей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deСокрушительная волна|cffced4da: выпускает волну воды, наносящую урон врагам на линии.|n"
        "- |cffa9c7deЛедяная стрела|cffced4da: наносит урон и оглушает вражескую цель.|n"
        "- |cffa9c7deУстойчивая кожа|cffced4da: сокращает длительность негативных эффектов и даёт устойчивость к магии.|n"
        "- |cffa9c7deПогружение|cffced4da: уходит под воду, становясь невидимым.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "nnrg", "field": "name", "expected": wts_updates[42933]})
    checks_def.append({"type": "unit", "id": "nnrg", "field": "tip", "expected": wts_updates[42932]})
    checks_def.append({"type": "unit", "id": "nnrg", "field": "ubertip", "expected": wts_updates[42934]})

    # nnsw: Сирена (W)
    wts_updates[42924] = "|cffe4cfa3Сирена|r"
    wts_updates[42923] = "|cffe4cfa3Сирена|r (|cffffffffW|r)"
    wts_updates[42925] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могущественная морская волшебница дальнего боя. Накладывает ледяную броню на союзников, поднимает врагов в вихри торнадо и заражает смертоносными паразитами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЛедяная броня|cffced4da: окутывает союзника щитом льда, повышающим броню и замедляющим атакующих врагов.|n"
        "- |cffa9c7deТорнадо|cffced4da: поднимает противника в воздух, полностью выводя его из боя.|n"
        "- |cffa9c7deПаразит|cffced4da: заражает врага паразитом, наносящим периодический урон.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "nnsw", "field": "name", "expected": wts_updates[42924]})
    checks_def.append({"type": "unit", "id": "nnsw", "field": "tip", "expected": wts_updates[42923]})
    checks_def.append({"type": "unit", "id": "nnsw", "field": "ubertip", "expected": wts_updates[42925]})

    # nwgs: Коатль (W)
    wts_updates[42952] = "|cffe4cfa3Коатль|r"
    wts_updates[42953] = "|cffe4cfa3Коатль|r (|cffffffffW|r)"
    wts_updates[42954] = (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый летающий стрелок дальнего боя. Сжигает ману противников при каждой атаке, нанося дополнительный урон.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deПротиводействие|cffced4da: каждая атака сжигает ману у цели и наносит дополнительный урон.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "nwgs", "field": "name", "expected": wts_updates[42952]})
    checks_def.append({"type": "unit", "id": "nwgs", "field": "tip", "expected": wts_updates[42953]})
    checks_def.append({"type": "unit", "id": "nwgs", "field": "ubertip", "expected": wts_updates[42954]})

    # nsnp: Морской василиск (W)
    wts_updates[42926] = "|cffe4cfa3Морской василиск|r"
    wts_updates[42927] = "|cffe4cfa3Морской василиск|r (|cffffffffW|r)"
    wts_updates[42928] = (
        "|cffa6afb8ЮНИТ:|cffced4da Легкий стрелок нагов дальнего боя. Плюётся ядовитыми иглами, замедляющими врагов и наносящими периодический урон.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deЗамедляющий яд|cffced4da: атаки отравляют цель, снижая скорость передвижения и нанося периодический урон.|n"
        "- |cffa9c7deПогружение|cffced4da: ныряет под воду, получая невидимость.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "nsnp", "field": "name", "expected": wts_updates[42926]})
    checks_def.append({"type": "unit", "id": "nsnp", "field": "tip", "expected": wts_updates[42927]})
    checks_def.append({"type": "unit", "id": "nsnp", "field": "ubertip", "expected": wts_updates[42928]})

    # nhyc: Драконья черепаха (R)
    wts_updates[42935] = "|cffe4cfa3Драконья черепаха|r"
    wts_updates[42936] = "|cffe4cfa3Драконья черепаха|r (|cffffffffR|r)"
    wts_updates[42937] = (
        "|cffa6afb8ЮНИТ:|cffced4da Колоссальная бронированная черепаха с осадным типом атаки. Наносит огромный урон вражеским зданиям и защищена шипастым панцирем.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deШипастый панцирь|cffced4da: отражает часть урона, полученного в ближнем бою.|n"
        "- |cffa9c7deСвоя стихия|cffced4da: в воде получает бонус к скорости атаки и перемещения.|n|n"
        "Атакует только наземные цели и здания.|r"
    )
    checks_def.append({"type": "unit", "id": "nhyc", "field": "name", "expected": wts_updates[42935]})
    checks_def.append({"type": "unit", "id": "nhyc", "field": "tip", "expected": wts_updates[42936]})
    checks_def.append({"type": "unit", "id": "nhyc", "field": "ubertip", "expected": wts_updates[42937]})

    # =========================================================================
    # 4. HEROES (4 heroes + 1 duplicate)
    # =========================================================================
    # H0JU: Владыка-страж (X)
    wts_updates[42964] = "|cffe4cfa3Владыка-страж|r"
    wts_updates[42967] = "|cffe4cfa3Владыка-страж|r (|cffffffffX|r)"
    wts_updates[42969] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могучий военачальник нагов ближнего боя. Обладает сокрушительным ударом хвоста, ледяным кольцом и невероятной живучестью.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deКольцо льда|cffced4da: ледяная волна, наносящая урон и замедляющая противников вокруг цели.|n"
        "- |cffa9c7deУдар хвостом|cffced4da: сотрясает землю хвостом, оглушая врагов и нанося урон.|n"
        "- |cffa9c7deУклонение|cffced4da: даёт шанс полностью избежать вражеской атаки.|n"
        "- |cffa9c7deМесть вод|cffced4da: призывает воплощение Древнего нага на помощь в битве.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H0JU", "field": "name", "expected": wts_updates[42964]})
    checks_def.append({"type": "unit", "id": "H0JU", "field": "tip", "expected": wts_updates[42967]})
    checks_def.append({"type": "unit", "id": "H0JU", "field": "ubertip", "expected": wts_updates[42969]})

    # H0JV: Глубинная охотница (C)
    wts_updates[42970] = "|cffe4cfa3Глубинная охотница|r"
    wts_updates[42974] = "|cffe4cfa3Глубинная охотница|r (|cffffffffC|r)"
    wts_updates[42975] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Быстрая и смертоносная воительница глубин дальнего боя. Разит врагов трезубцем, стремительно перемещается по полю боя и способна поражать две цели одновременно.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deБезумие|cffced4da: впадает в ярость, значительно увеличивая скорость атаки.|n"
        "- |cffa9c7deСкачок|cffced4da: мгновенно переносит охотницу на короткое расстояние.|n"
        "- |cffa9c7deДвойной удар|cffced4da: позволяет атаковать две цели одновременно и пассивно увеличивает ловкость.|n"
        "- |cffa9c7deПовелитель моря|cffced4da: даёт шанс уклониться от удара и нанести критический урон.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H0JV", "field": "name", "expected": wts_updates[42970]})
    checks_def.append({"type": "unit", "id": "H0JV", "field": "tip", "expected": wts_updates[42974]})
    checks_def.append({"type": "unit", "id": "H0JV", "field": "ubertip", "expected": wts_updates[42975]})

    # H0OZ: Мурлок-гигант (X)
    wts_updates[41066] = "|cffe4cfa3Мурлок-гигант|r"
    wts_updates[41069] = "|cffe4cfa3Мурлок-гигант|r (|cffffffffX|r)"
    wts_updates[41071] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Исполинский вождь племени мурлоков ближнего боя. Обладает колоссальной силой, сокрушает землю хвостом и замораживает противников ледяным кольцом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deКольцо льда|cffced4da: ледяная волна, наносящая урон и замедляющая противников вокруг цели.|n"
        "- |cffa9c7deУдар хвостом|cffced4da: сотрясает землю, нанося урон и оглушая окружающих врагов.|n"
        "- |cffa9c7deУклонение|cffced4da: даёт шанс уклониться от вражеской атаки.|n"
        "- |cffa9c7deМесть вод|cffced4da: призывает древнего морского воина на помощь в сражении.|n|n"
        "Атакует только наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "H0OZ", "field": "name", "expected": wts_updates[41066]})
    checks_def.append({"type": "unit", "id": "H0OZ", "field": "tip", "expected": wts_updates[41069]})
    checks_def.append({"type": "unit", "id": "H0OZ", "field": "ubertip", "expected": wts_updates[41071]})

    # N07A: Мурлок-чародей (Z)
    wts_updates[43012] = "|cffe4cfa3Мурлок-чародей|r"
    wts_updates[43014] = "|cffe4cfa3Мурлок-чародей|r (|cffffffffZ|r)"
    wts_updates[43017] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарный правитель и верховный шаман мурлоков дальнего боя. Обрушивает огненный дождь на врагов, изгоняет цели в астрал и исцеляет союзников великим покоем.|n|n"
        "|cffa6afb8Способности:|cffced4da|n"
        "- |cffa9c7deОгненный ливень|cffced4da: обрушивает волны огня на указанную область, нанося периодический урон.|n"
        "- |cffa9c7deИзгнание|cffced4da: переносит цель в астральный план, запрещая атаковать и увеличивая получаемый магический урон.|n"
        "- |cffa9c7deАура гениальности|cffced4da: значительно ускоряет восстановление маны окружающих союзников.|n"
        "- |cffa9c7deПокой|cffced4da: призывает поток целительной энергии, мощно восстанавливающий здоровье войскам в области.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "N07A", "field": "name", "expected": wts_updates[43012]})
    checks_def.append({"type": "unit", "id": "N07A", "field": "tip", "expected": wts_updates[43014]})
    checks_def.append({"type": "unit", "id": "N07A", "field": "ubertip", "expected": wts_updates[43017]})

    # N054: Мурлок-чародей (дубликат/сломанный)
    wts_updates[25735] = "|cffe4cfa3Мурлок-чародей|r"
    wts_updates[25738] = "|cffe4cfa3Мурлок-чародей|r (|cffffffffZ|r)"
    wts_updates[26681] = wts_updates[43017]
    checks_def.append({"type": "unit", "id": "N054", "field": "name", "expected": wts_updates[25735]})
    checks_def.append({"type": "unit", "id": "N054", "field": "tip", "expected": wts_updates[25738]})
    checks_def.append({"type": "unit", "id": "N054", "field": "ubertip", "expected": wts_updates[26681]})

    # =========================================================================
    # 5. RESEARCHES & UPGRADES (13 upgrades, 37 strings)
    # =========================================================================
    # R0FE: Владычество нагов
    wts_updates[43151] = "|cffe4cfa3Владычество нагов|r"
    wts_updates[43153] = "|cffe4cfa3Владычество нагов|r"
    wts_updates[43152] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Утверждает власть нагов в королевстве, открывая доступ к обучению элитных войск нагов и героя Владыки-стража.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deГлубинный житель|cffced4da|n"
        "- |cffa9c7deСирена|cffced4da|n"
        "- |cffa9c7deМирмидон|cffced4da|n"
        "- |cffa9c7deСтраж нагов|cffced4da|n"
        "- |cffa9c7deДревний нага|cffced4da|n"
        "- |cffa9c7deВладыка-страж|cffced4da.|n|n"
        "|cffe6c07bБлокирует исследование «Владычество мурлоков».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0FE", "field": "name1", "expected": wts_updates[43151]})
    checks_def.append({"type": "upgrade", "id": "R0FE", "field": "tip1", "expected": wts_updates[43153]})
    checks_def.append({"type": "upgrade", "id": "R0FE", "field": "ubertip1", "expected": wts_updates[43152]})

    # R0FF: Владычество мурлоков
    wts_updates[43154] = "|cffe4cfa3Владычество мурлоков|r"
    wts_updates[43155] = "|cffe4cfa3Владычество мурлоков|r"
    wts_updates[43156] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Утверждает власть мурлоков в королевстве, открывая доступ к ордам специализированных бойцов мурлоков и герою Мурлоку-гиганту.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМурлок-охотник|cffced4da|n"
        "- |cffa9c7deМурлок-чернокнижник|cffced4da|n"
        "- |cffa9c7deМурлок-шаман|cffced4da|n"
        "- |cffa9c7deМурлок-мутант|cffced4da|n"
        "- |cffa9c7deМурлок-гигант|cffced4da.|n|n"
        "|cffe6c07bБлокирует исследование «Владычество нагов».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0FF", "field": "name1", "expected": wts_updates[43154]})
    checks_def.append({"type": "upgrade", "id": "R0FF", "field": "tip1", "expected": wts_updates[43155]})
    checks_def.append({"type": "upgrade", "id": "R0FF", "field": "ubertip1", "expected": wts_updates[43156]})

    # R0FD: Шипастый панцирь
    wts_updates[43148] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[43149] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[43150] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает панцири воинов острыми шипами, позволяя отражать |cffffffff15%|cffced4da урона, полученного в ближнем бою.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deВоин волн|cffced4da|n"
        "- |cffa9c7deМурлок-налётчик|cffced4da|n"
        "- |cffa9c7deМурлок-охотник|cffced4da|n"
        "- |cffa9c7deМурлок-чернокнижник|cffced4da|n"
        "- |cffa9c7deМурлок-шаман|cffced4da|n"
        "- |cffa9c7deМурлок-мутант|cffced4da|n"
        "- |cffa9c7deДраконья черепаха|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0FD", "field": "name1", "expected": wts_updates[43148]})
    checks_def.append({"type": "upgrade", "id": "R0FD", "field": "tip1", "expected": wts_updates[43149]})
    checks_def.append({"type": "upgrade", "id": "R0FD", "field": "ubertip1", "expected": wts_updates[43150]})

    # R0FH: Улучшенный хват (4 уровня)
    wts_updates[43160] = "|cffe4cfa3Улучшенный хват — уровень 1|r"
    wts_updates[43161] = "|cffe4cfa3Улучшенный хват — уровень 2|r"
    wts_updates[43162] = "|cffe4cfa3Улучшенный хват — уровень 3|r"
    wts_updates[43163] = "|cffe4cfa3Улучшенный хват — уровень 4|r"
    wts_updates[43164] = "|cffe4cfa3Улучшенный хват — уровень 1|r"
    wts_updates[43165] = "|cffe4cfa3Улучшенный хват — уровень 2|r"
    wts_updates[43166] = "|cffe4cfa3Улучшенный хват — уровень 3|r"
    wts_updates[43167] = "|cffe4cfa3Улучшенный хват — уровень 4|r"
    wts_updates[43171] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Позволяет рабочим переносить |cffc8e087+8|cffced4da ед. древесины за один раз.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deРаб мурлоков|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[43168] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает количество переносимой древесины на |cffc8e087+8|cffced4da ед. (суммарно |cffffffff+16|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deРаб мурлоков|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[43169] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает количество переносимой древесины на |cffc8e087+8|cffced4da ед. (суммарно |cffffffff+24|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deРаб мурлоков|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[43170] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает количество переносимой древесины на |cffc8e087+8|cffced4da ед. (суммарно |cffffffff+32|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deРаб мурлоков|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # R0FP: Сокрушительный удар
    wts_updates[43172] = "|cffe4cfa3Сокрушительный удар|r"
    wts_updates[43173] = "|cffe4cfa3Сокрушительный удар|r"
    wts_updates[43174] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Морских охотников приёму «Сокрушение», дающему шанс нанести дополнительный урон и оглушить цель.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМорской охотник|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0FP", "field": "name1", "expected": wts_updates[43172]})
    checks_def.append({"type": "upgrade", "id": "R0FP", "field": "tip1", "expected": wts_updates[43173]})
    checks_def.append({"type": "upgrade", "id": "R0FP", "field": "ubertip1", "expected": wts_updates[43174]})

    # R0FQ: Господство на море (3 уровня)
    wts_updates[43175] = "|cffe4cfa3Господство на море — уровень 1|r"
    wts_updates[43178] = "|cffe4cfa3Господство на море — уровень 2|r"
    wts_updates[43179] = "|cffe4cfa3Господство на море — уровень 3|r"
    wts_updates[43176] = "|cffe4cfa3Господство на море — уровень 1|r"
    wts_updates[43180] = "|cffe4cfa3Господство на море — уровень 2|r"
    wts_updates[43181] = "|cffe4cfa3Господство на море — уровень 3|r"
    wts_updates[43177] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья Мурлоков-мутантов на |cffc8e087+40|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМурлок-мутант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/3|cffced4da.|r"
    )
    wts_updates[43182] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье Мурлоков-мутантов на |cffc8e087+40|cffced4da ед. (суммарно |cffffffff+80|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМурлок-мутант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/3|cffced4da.|r"
    )
    wts_updates[43183] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье Мурлоков-мутантов на |cffc8e087+40|cffced4da ед. (суммарно |cffffffff+120|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМурлок-мутант|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/3|cffced4da.|r"
    )

    # R0FR: Замедляющий яд
    wts_updates[43184] = "|cffe4cfa3Замедляющий яд|r"
    wts_updates[43185] = "|cffe4cfa3Замедляющий яд|r"
    wts_updates[43186] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет атаки Морских василисков смертоносным ядом, замедляющим скорость бега и атаки врага и наносящим периодический урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМорской василиск|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0FR", "field": "name1", "expected": wts_updates[43184]})
    checks_def.append({"type": "upgrade", "id": "R0FR", "field": "tip1", "expected": wts_updates[43185]})
    checks_def.append({"type": "upgrade", "id": "R0FR", "field": "ubertip1", "expected": wts_updates[43186]})

    # R0KP: Антимагический коатль
    wts_updates[26369] = "|cffe4cfa3Антимагический коатль|r"
    wts_updates[26370] = "|cffe4cfa3Антимагический коатль|r"
    wts_updates[26371] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Коатлей способности «Противодействие», позволяя сжигать ману противника при каждой атаке и наносить дополнительный урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deКоатль|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R0KP", "field": "name1", "expected": wts_updates[26369]})
    checks_def.append({"type": "upgrade", "id": "R0KP", "field": "tip1", "expected": wts_updates[26370]})
    checks_def.append({"type": "upgrade", "id": "R0KP", "field": "ubertip1", "expected": wts_updates[26371]})

    # Rnam: Коралловая чешуя (6 уровней)
    wts_updates[43038] = "|cffe4cfa3Коралловая чешуя — уровень 1|r"
    wts_updates[43024] = "|cffe4cfa3Коралловая чешуя — уровень 2|r"
    wts_updates[43021] = "|cffe4cfa3Хитиновая чешуя — уровень 3|r"
    wts_updates[43025] = "|cffe4cfa3Хитиновая чешуя — уровень 4|r"
    wts_updates[43023] = "|cffe4cfa3Костяная чешуя — уровень 5|r"
    wts_updates[43022] = "|cffe4cfa3Костяная чешуя — уровень 6|r"
    wts_updates[43026] = "|cffe4cfa3Коралловая чешуя — уровень 1|r"
    wts_updates[43027] = "|cffe4cfa3Коралловая чешуя — уровень 2|r"
    wts_updates[43028] = "|cffe4cfa3Хитиновая чешуя — уровень 3|r"
    wts_updates[43031] = "|cffe4cfa3Хитиновая чешуя — уровень 4|r"
    wts_updates[43030] = "|cffe4cfa3Костяная чешуя — уровень 5|r"
    wts_updates[43029] = "|cffe4cfa3Костяная чешуя — уровень 6|r"
    wts_updates[43032] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает защиту войск нагов и мурлоков на |cffc8e087+2|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
    )
    wts_updates[43033] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает защиту войск нагов и мурлоков на |cffc8e087+2|cffced4da ед. (суммарно |cffffffff+4|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
    )
    wts_updates[43034] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает защиту войск нагов и мурлоков на |cffc8e087+2|cffced4da ед. (суммарно |cffffffff+6|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
    )
    wts_updates[43035] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает защиту войск нагов и мурлоков на |cffc8e087+2|cffced4da ед. (суммарно |cffffffff+8|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
    )
    wts_updates[43036] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает защиту войск нагов и мурлоков на |cffc8e087+2|cffced4da ед. (суммарно |cffffffff+10|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
    )
    wts_updates[43037] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает защиту войск нагов и мурлоков на |cffc8e087+2|cffced4da ед. (суммарно |cffffffff+12|cffced4da).|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
    )

    # Rnat: Коралловые клинки (6 уровней)
    wts_updates[43039] = "|cffe4cfa3Коралловые клинки — уровень 1|r"
    wts_updates[43043] = "|cffe4cfa3Коралловые клинки — уровень 2|r"
    wts_updates[43040] = "|cffe4cfa3Хитиновые клинки — уровень 3|r"
    wts_updates[43044] = "|cffe4cfa3Хитиновые клинки — уровень 4|r"
    wts_updates[43042] = "|cffe4cfa3Костяные клинки — уровень 5|r"
    wts_updates[43041] = "|cffe4cfa3Костяные клинки — уровень 6|r"
    wts_updates[43045] = "|cffe4cfa3Коралловые клинки — уровень 1|r"
    wts_updates[43049] = "|cffe4cfa3Коралловые клинки — уровень 2|r"
    wts_updates[43046] = "|cffe4cfa3Хитиновые клинки — уровень 3|r"
    wts_updates[43050] = "|cffe4cfa3Хитиновые клинки — уровень 4|r"
    wts_updates[43048] = "|cffe4cfa3Костяные клинки — уровень 5|r"
    wts_updates[43047] = "|cffe4cfa3Костяные клинки — уровень 6|r"
    wts_updates[43051] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон войск нагов и мурлоков.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/6|cffced4da.|r"
    )
    wts_updates[43052] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон войск нагов и мурлоков.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/6|cffced4da.|r"
    )
    wts_updates[43053] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон войск нагов и мурлоков.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff3/6|cffced4da.|r"
    )
    wts_updates[43054] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон войск нагов и мурлоков.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff4/6|cffced4da.|r"
    )
    wts_updates[43055] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон войск нагов и мурлоков.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff5/6|cffced4da.|r"
    )
    wts_updates[43056] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон войск нагов и мурлоков.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- Войскам нагов и мурлоков.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff6/6|cffced4da.|r"
    )

    # Rnen: Опутывание
    wts_updates[25898] = "|cffe4cfa3Опутывание|r"
    wts_updates[25944] = "|cffe4cfa3Опутывание|r"
    wts_updates[26330] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Мирмидонов способности «Опутывание», позволяя прижимать воздушные и наземные цели к земле.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМирмидон|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "Rnen", "field": "name1", "expected": wts_updates[25898]})
    checks_def.append({"type": "upgrade", "id": "Rnen", "field": "tip1", "expected": wts_updates[25944]})
    checks_def.append({"type": "upgrade", "id": "Rnen", "field": "ubertip1", "expected": wts_updates[26330]})

    # Rnsb: Погружение
    wts_updates[26331] = "|cffe4cfa3Погружение|r"
    wts_updates[26332] = "|cffe4cfa3Погружение|r"
    wts_updates[26333] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает войска нагов погружению под воду, даруя постоянную невидимость при нахождении в воде.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deМирмидон|cffced4da|n"
        "- |cffa9c7deМорской василиск|cffced4da|n"
        "- |cffa9c7deСтраж нагов|cffced4da|n"
        "- |cffa9c7deДревний нага|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "Rnsb", "field": "name1", "expected": wts_updates[26331]})
    checks_def.append({"type": "upgrade", "id": "Rnsb", "field": "tip1", "expected": wts_updates[26332]})
    checks_def.append({"type": "upgrade", "id": "Rnsb", "field": "ubertip1", "expected": wts_updates[26333]})

    # Rnsi: Коралловая магия (2 уровня)
    wts_updates[26334] = "|cffe4cfa3Коралловая магия — уровень 1|r"
    wts_updates[26337] = "|cffe4cfa3Коралловая магия — уровень 2|r"
    wts_updates[26335] = "|cffe4cfa3Коралловая магия — уровень 1|r"
    wts_updates[26338] = "|cffe4cfa3Коралловая магия — уровень 2|r"
    wts_updates[26336] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья магов поддержки на |cffc8e087+45|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед. и скорость восстановления маны.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deГлубинный житель|cffced4da|n"
        "- |cffa9c7deМурлок-чернокнижник|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[26339] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье магов поддержки на |cffc8e087+45|cffced4da ед., ману на |cffc8e087+100|cffced4da ед. и скорость восстановления маны.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deГлубинный житель|cffced4da|n"
        "- |cffa9c7deМурлок-чернокнижник|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # Rnsw: Силы стихий (2 уровня)
    wts_updates[26340] = "|cffe4cfa3Силы стихий — уровень 1|r"
    wts_updates[26341] = "|cffe4cfa3Силы стихий — уровень 2|r"
    wts_updates[26342] = "|cffe4cfa3Силы стихий — уровень 1|r"
    wts_updates[26343] = "|cffe4cfa3Силы стихий — уровень 2|r"
    wts_updates[26344] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья боевых магов на |cffc8e087+45|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед. и скорость восстановления маны.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deСирена|cffced4da|n"
        "- |cffa9c7deМурлок-шаман|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[26345] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье боевых магов на |cffc8e087+45|cffced4da ед., ману на |cffc8e087+100|cffced4da ед. и скорость восстановления маны.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n"
        "- |cffa9c7deСирена|cffced4da|n"
        "- |cffa9c7deМурлок-шаман|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # =========================================================================
    # 6. HERO ABILITIES
    # =========================================================================
    # A13C: Безумие (Q) — Deep Huntress
    wts_updates[35885] = "|cffe4cfa3Безумие|r"
    wts_updates[35887] = "|cffe4cfa3Безумие — уровень 1|r (|cffffffffQ|r)"
    wts_updates[35888] = "|cffe4cfa3Безумие — уровень 2|r (|cffffffffQ|r)"
    wts_updates[35889] = "|cffe4cfa3Безумие — уровень 3|r (|cffffffffQ|r)"
    wts_updates[35890] = "|cffe4cfa3Безумие — уровень 4|r (|cffffffffQ|r)"
    wts_updates[35896] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пробуждает ярость глубин, увеличивая скорость атаки на |cffc8e087+50%|cffced4da и скорость передвижения на |cffc8e087+20%|cffced4da, но повышая получаемый урон на |cffe69a8d+25%|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[36108] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пробуждает ярость глубин, увеличивая скорость атаки на |cffc8e087+75%|cffced4da и скорость передвижения на |cffc8e087+25%|cffced4da, но повышая получаемый урон на |cffe69a8d+25%|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[40069] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пробуждает ярость глубин, увеличивая скорость атаки на |cffc8e087+100%|cffced4da и скорость передвижения на |cffc8e087+30%|cffced4da, но повышая получаемый урон на |cffe69a8d+25%|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[40705] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пробуждает ярость глубин, увеличивая скорость атаки на |cffc8e087+125%|cffced4da и скорость передвижения на |cffc8e087+35%|cffced4da, но повышая получаемый урон на |cffe69a8d+25%|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A13C", "field": "name", "expected": wts_updates[35885]})
    checks_def.append({"type": "ability", "id": "A13C", "field": "tip1", "expected": wts_updates[35887]})
    checks_def.append({"type": "ability", "id": "A13C", "field": "ubertip1", "expected": wts_updates[35896]})

    # AEbl: Скачок (W) — Deep Huntress
    wts_updates[25764] = "|cffe4cfa3Скачок|r"
    wts_updates[9615] = "|cffe4cfa3Скачок — уровень 4|r (|cffffffffW|r)"
    wts_updates[9616] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно перемещает охотницу на короткое расстояние, позволяя вступить в бой или выйти из него.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "AEbl", "field": "name", "expected": wts_updates[25764]})

    # A13A: Двойной удар (E) — Deep Huntress
    wts_updates[35222] = "|cffe4cfa3Двойной удар|r"
    wts_updates[35223] = "|cffe4cfa3Двойной удар — уровень 1|r (|cffffffffE|r)"
    wts_updates[35230] = "|cffe4cfa3Двойной удар — уровень 2|r (|cffffffffE|r)"
    wts_updates[35354] = "|cffe4cfa3Двойной удар — уровень 3|r (|cffffffffE|r)"
    wts_updates[35355] = "|cffe4cfa3Двойной удар — уровень 4|r (|cffffffffE|r)"
    wts_updates[35224] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать две цели одновременно и пассивно увеличивает ловкость на |cffc8e087+2|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[35566] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать две цели одновременно и пассивно увеличивает ловкость на |cffc8e087+4|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[35818] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать две цели одновременно и пассивно увеличивает ловкость на |cffc8e087+6|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[35875] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет атаковать две цели одновременно и пассивно увеличивает ловкость на |cffc8e087+8|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A13A", "field": "name", "expected": wts_updates[35222]})
    checks_def.append({"type": "ability", "id": "A13A", "field": "tip1", "expected": wts_updates[35223]})
    checks_def.append({"type": "ability", "id": "A13A", "field": "ubertip1", "expected": wts_updates[35224]})

    # A13D: Повелитель моря (R) — Deep Huntress
    wts_updates[40925] = "|cffe4cfa3Повелитель моря|r"
    wts_updates[40932] = "|cffe4cfa3Повелитель моря — уровень 1|r (|cffffffffR|r)"
    wts_updates[40962] = "|cffe4cfa3Повелитель моря — уровень 2|r (|cffffffffR|r)"
    wts_updates[40995] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff20%|cffced4da шанс уклониться от вражеской атаки и |cffffffff20%|cffced4da шанс нанести критический удар в |cffffffff2|cffced4da-кратном размере.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[40996] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff30%|cffced4da шанс уклониться от вражеской атаки и |cffffffff30%|cffced4da шанс нанести критический удар в |cffffffff3|cffced4da-кратном размере.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A13D", "field": "name", "expected": wts_updates[40925]})
    checks_def.append({"type": "ability", "id": "A13D", "field": "tip1", "expected": wts_updates[40932]})
    checks_def.append({"type": "ability", "id": "A13D", "field": "ubertip1", "expected": wts_updates[40995]})

    # A136..A139: Стригущий трезубец (пассивные бонусы трезубца)
    wts_updates[25756] = "|cffe4cfa3Стригущий трезубец|r"
    wts_updates[25757] = "|cffe4cfa3Стригущий трезубец|r"
    wts_updates[25758] = "|cffe4cfa3Стригущий трезубец|r"
    wts_updates[25759] = "|cffe4cfa3Стригущий трезубец|r"

    # A135: Пронзающий трезубец (4 уровня)
    wts_updates[31589] = "|cffe4cfa3Пронзающий трезубец|r"
    wts_updates[31591] = "|cffe4cfa3Пронзающий трезубец — уровень 1|r"
    wts_updates[31592] = "|cffe4cfa3Пронзающий трезубец — уровень 2|r"
    wts_updates[31716] = "|cffe4cfa3Пронзающий трезубец — уровень 3|r"
    wts_updates[31900] = "|cffe4cfa3Пронзающий трезубец — уровень 4|r"
    wts_updates[31902] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Брошенный трезубец пронзает первую цель и летит дальше по прямой, поражая стоящих позади врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[35219] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Брошенный трезубец пронзает первую цель и летит дальше по прямой, поражая стоящих позади врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[35220] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Брошенный трезубец пронзает первую цель и летит дальше по прямой, поражая стоящих позади врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[35221] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Брошенный трезубец пронзает первую цель и летит дальше по прямой, поражая стоящих позади врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # A14F: Удар хвостом (W) — Lord Guardian / Murloc Giant
    wts_updates[41000] = "|cffe4cfa3Удар хвостом|r"
    wts_updates[41001] = "|cffe4cfa3Удар хвостом — уровень 1|r (|cffffffffW|r)"
    wts_updates[41002] = "|cffe4cfa3Удар хвостом — уровень 2|r (|cffffffffW|r)"
    wts_updates[41003] = "|cffe4cfa3Удар хвостом — уровень 3|r (|cffffffffW|r)"
    wts_updates[41006] = "|cffe4cfa3Удар хвостом — уровень 4|r (|cffffffffW|r)"
    wts_updates[41012] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощный удар хвостом по земле, наносящий |cffffffff100|cffced4da ед. урона окружающим врагам и оглушающий их на |cffffffff2|cffced4da сек.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[41013] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощный удар хвостом по земле, наносящий |cffffffff175|cffced4da ед. урона окружающим врагам и оглушающий их на |cffffffff2.5|cffced4da сек.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[41014] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощный удар хвостом по земле, наносящий |cffffffff250|cffced4da ед. урона окружающим врагам и оглушающий их на |cffffffff3|cffced4da сек.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[41015] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мощный удар хвостом по земле, наносящий |cffffffff325|cffced4da ед. урона окружающим врагам и оглушающий их на |cffffffff3.5|cffced4da сек.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A14F", "field": "name", "expected": wts_updates[41000]})
    checks_def.append({"type": "ability", "id": "A14F", "field": "tip1", "expected": wts_updates[41001]})
    checks_def.append({"type": "ability", "id": "A14F", "field": "ubertip1", "expected": wts_updates[41012]})

    # A14G: Месть вод (R) — Lord Guardian / Murloc Giant
    wts_updates[41029] = "|cffe4cfa3Месть вод|r"
    wts_updates[41041] = "|cffe4cfa3Месть вод — уровень 1|r (|cffffffffR|r)"
    wts_updates[41042] = "|cffe4cfa3Месть вод — уровень 2|r (|cffffffffR|r)"
    wts_updates[41043] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает проклятие на врага. Если цель погибает под действием заклинания, из её останков восстаёт свирепый Древний нага.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[41044] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Накладывает проклятие на врага. Если цель погибает под действием заклинания, из её останков восстаёт свирепый Древний нага большего могущества.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A14G", "field": "name", "expected": wts_updates[41029]})
    checks_def.append({"type": "ability", "id": "A14G", "field": "tip1", "expected": wts_updates[41041]})
    checks_def.append({"type": "ability", "id": "A14G", "field": "ubertip1", "expected": wts_updates[41043]})

    # A14H: Уклонение (E) — Lord Guardian / Murloc Giant
    wts_updates[41045] = "|cffe4cfa3Уклонение|r"
    wts_updates[41047] = "|cffe4cfa3Уклонение — уровень 1|r"
    wts_updates[41048] = "|cffe4cfa3Уклонение — уровень 2|r"
    wts_updates[41049] = "|cffe4cfa3Уклонение — уровень 3|r"
    wts_updates[41050] = "|cffe4cfa3Уклонение — уровень 4|r"
    wts_updates[41051] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff10%|cffced4da шанс полностью избежать вражеской атаки.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[41052] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff20%|cffced4da шанс полностью избежать вражеской атаки.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[41053] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff30%|cffced4da шанс полностью избежать вражеской атаки.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[41054] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff40%|cffced4da шанс полностью избежать вражеской атаки.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A14H", "field": "name", "expected": wts_updates[41045]})
    checks_def.append({"type": "ability", "id": "A14H", "field": "tip1", "expected": wts_updates[41047]})
    checks_def.append({"type": "ability", "id": "A14H", "field": "ubertip1", "expected": wts_updates[41051]})

    # A14I: Кольцо льда (Q) — Lord Guardian / Murloc Giant
    wts_updates[41056] = "|cffe4cfa3Кольцо льда|r"
    wts_updates[41078] = "|cffe4cfa3Кольцо льда — уровень 1|r (|cffffffffQ|r)"
    wts_updates[41079] = "|cffe4cfa3Кольцо льда — уровень 2|r (|cffffffffQ|r)"
    wts_updates[43057] = "|cffe4cfa3Кольцо льда — уровень 3|r (|cffffffffQ|r)"
    wts_updates[43058] = "|cffe4cfa3Кольцо льда — уровень 4|r (|cffffffffQ|r)"
    wts_updates[41063] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода, наносящую |cffffffff100|cffced4da ед. урона цели и |cffffffff50|cffced4da ед. урона окружающим врагам, замедляя их скорость атаки и бега.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[41064] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода, наносящую |cffffffff150|cffced4da ед. урона цели и |cffffffff75|cffced4da ед. урона окружающим врагам, замедляя их скорость атаки и бега.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[41065] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода, наносящую |cffffffff200|cffced4da ед. урона цели и |cffffffff100|cffced4da ед. урона окружающим врагам, замедляя их скорость атаки и бега.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[41074] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода, наносящую |cffffffff250|cffced4da ед. урона цели и |cffffffff125|cffced4da ед. урона окружающим врагам, замедляя их скорость атаки и бега.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A14I", "field": "name", "expected": wts_updates[41056]})
    checks_def.append({"type": "ability", "id": "A14I", "field": "tip1", "expected": wts_updates[41078]})
    checks_def.append({"type": "ability", "id": "A14I", "field": "ubertip1", "expected": wts_updates[41063]})

    # AEtq: Покой (R) — Murloc Sorcerer
    wts_updates[25766] = "|cffe4cfa3Покой|r"
    wts_updates[2292] = "|cffe4cfa3Покой — уровень 2|r (|cffffffffR|r)"
    wts_updates[2306] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает мощный поток целительной энергии, восстанавливающий союзникам в области |cffffffff90|cffced4da ед. здоровья в секунду в течение |cffffffff25|cffced4da сек.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # AHbn: Изгнание (W) — Murloc Sorcerer
    wts_updates[25760] = "|cffe4cfa3Изгнание|r"
    wts_updates[5621] = "|cffe4cfa3Изгнание — уровень 4|r (|cffffffffW|r)"
    wts_updates[5622] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Изгоняет цель в астральный план, запрещая атаковать, замедляя передвижение и увеличивая получаемый магический урон.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # AHab: Аура гениальности (E) — Murloc Sorcerer
    wts_updates[23080] = "|cffe4cfa3Аура гениальности|r"
    wts_updates[2016] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет восстановление маны у находящихся рядом союзных войск.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # ANrf: Огненный ливень (Q) — Murloc Sorcerer
    wts_updates[25841] = "|cffe4cfa3Огненный ливень|r"
    wts_updates[2014] = "|cffe4cfa3Огненный ливень — уровень 4|r (|cffffffffQ|r)"
    wts_updates[2015] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает на указанную область волны огня. Каждая волна наносит мгновенный урон и поджигает врагов, нанося периодический урон.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # Vashj Spells: A16B, A16C, A16D, A16E
    # A16B: Расщеплённая молния (Q)
    wts_updates[43079] = "|cffe4cfa3Расщеплённая молния|r"
    wts_updates[43085] = "|cffe4cfa3Расщеплённая молния — уровень 1|r (|cffffffffQ|r)"
    wts_updates[43086] = "|cffe4cfa3Расщеплённая молния — уровень 2|r (|cffffffffQ|r)"
    wts_updates[43087] = "|cffe4cfa3Расщеплённая молния — уровень 3|r (|cffffffffQ|r)"
    wts_updates[43078] = "|cffe4cfa3Расщеплённая молния — уровень 4|r (|cffffffffQ|r)"
    wts_updates[43082] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молниями противников в секторе перед героем, нанося урон нескольким целям одновременно.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[43083] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молниями противников в секторе перед героем, нанося урон нескольким целям одновременно.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[43084] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молниями противников в секторе перед героем, нанося урон нескольким целям одновременно.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[43077] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молниями противников в секторе перед героем, нанося урон нескольким целям одновременно.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # A16C: Ледяные стрелы (W)
    wts_updates[43096] = "|cffe4cfa3Ледяные стрелы|r"
    wts_updates[43100] = "|cffe4cfa3Ледяные стрелы — уровень 1|r (|cffffffffW|r)"
    wts_updates[43102] = "|cffe4cfa3Ледяные стрелы — уровень 2|r (|cffffffffW|r)"
    wts_updates[43104] = "|cffe4cfa3Ледяные стрелы — уровень 3|r (|cffffffffW|r)"
    wts_updates[43088] = "|cffe4cfa3Ледяные стрелы — уровень 4|r (|cffffffffW|r)"
    wts_updates[43099] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет выстрелы силой льда, нанося дополнительный урон и замедляя скорость атаки и бега врага.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[43101] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет выстрелы силой льда, нанося дополнительный урон и замедляя скорость атаки и бега врага.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[43103] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет выстрелы силой льда, нанося дополнительный урон и замедляя скорость атаки и бега врага.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[43089] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет выстрелы силой льда, нанося дополнительный урон и замедляя скорость атаки и бега врага.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # A16D: Кольцо холода
    wts_updates[43110] = "|cffe4cfa3Кольцо холода|r"
    wts_updates[43113] = "|cffe4cfa3Кольцо холода — уровень 1|r"
    wts_updates[43115] = "|cffe4cfa3Кольцо холода — уровень 2|r"
    wts_updates[43117] = "|cffe4cfa3Кольцо холода — уровень 3|r"
    wts_updates[43108] = "|cffe4cfa3Кольцо холода — уровень 4|r"
    wts_updates[43107] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода вокруг цели, нанося урон и замедляя врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    )
    wts_updates[43114] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода вокруг цели, нанося урон и замедляя врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    )
    wts_updates[43116] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода вокруг цели, нанося урон и замедляя врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    )
    wts_updates[43109] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну ледяного холода вокруг цели, нанося урон и замедляя врагов.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    )

    # A16E: Буря (R)
    wts_updates[43118] = "|cffe4cfa3Буря|r"
    wts_updates[43119] = "|cffe4cfa3Буря — уровень 1|r (|cffffffffR|r)"
    wts_updates[43124] = "|cffe4cfa3Буря — уровень 2|r (|cffffffffR|r)"
    wts_updates[43122] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает мощный водяной смерч в указанную точку на |cffffffff30|cffced4da сек., наносящий урон зданиям и поднимающий врагов в воздух.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[43123] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает мощный водяной смерч в указанную точку на |cffffffff30|cffced4da сек., наносящий урон зданиям и поднимающий врагов в воздух.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    )

    # =========================================================================
    # 7. UNIT ABILITIES
    # =========================================================================
    # A1LT: Своя стихия (D)
    wts_updates[43125] = "|cffe4cfa3Своя стихия|r"
    wts_updates[43126] = "|cffe4cfa3Своя стихия|r (|cffffffffD|r)"
    wts_updates[43127] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Находясь в воде, юнит может активировать заклинание, получая на |cffffffff180|cffced4da сек. бонус |cffc8e087+10%|cffced4da к скорости атаки и |cffc8e087+35%|cffced4da к скорости передвижения.|r"
    )
    checks_def.append({"type": "ability", "id": "A1LT", "field": "name", "expected": wts_updates[43125]})
    checks_def.append({"type": "ability", "id": "A1LT", "field": "tip1", "expected": wts_updates[43126]})
    checks_def.append({"type": "ability", "id": "A1LT", "field": "ubertip1", "expected": wts_updates[43127]})

    # S00E: Своя стихия (эффект)
    wts_updates[43132] = "|cffe4cfa3Своя стихия|r"
    wts_updates[43133] = "|cffe4cfa3Своя стихия|r"
    wts_updates[43134] = "|cffa6afb8ЭФФЕКТ:|cffced4da Дарует бонус |cffc8e087+10%|cffced4da к скорости атаки и |cffc8e087+35%|cffced4da к скорости передвижения в воде.|r"

    # A1LV: Скорость нагов
    wts_updates[43128] = "|cffe4cfa3Скорость нагов|r"

    # A13B: Шипастый панцирь
    wts_updates[35882] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[35883] = "|cffe4cfa3Шипастый панцирь|r"
    wts_updates[35884] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Острые шипы на панцире возвращают |cffffffff15%|cffced4da урона, полученного в ближнем бою, атакующему противнику.|r"
    )
    checks_def.append({"type": "ability", "id": "A13B", "field": "name", "expected": wts_updates[35882]})
    checks_def.append({"type": "ability", "id": "A13B", "field": "tip1", "expected": wts_updates[35883]})
    checks_def.append({"type": "ability", "id": "A13B", "field": "ubertip1", "expected": wts_updates[35884]})

    # A14J: Замедляющий яд
    wts_updates[43059] = "|cffe4cfa3Замедляющий яд|r"
    wts_updates[43060] = "|cffe4cfa3Замедляющий яд|r"
    wts_updates[43061] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Отравляет цель при атаке, нанося периодический урон, снижая скорость передвижения на |cffe69a8d50%|cffced4da и скорость атаки на |cffe69a8d25%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A14J", "field": "name", "expected": wts_updates[43059]})
    checks_def.append({"type": "ability", "id": "A14J", "field": "tip1", "expected": wts_updates[43060]})
    checks_def.append({"type": "ability", "id": "A14J", "field": "ubertip1", "expected": wts_updates[43061]})

    # A14K: Уклонение (Мурлок-мутант)
    wts_updates[43062] = "|cffe4cfa3Уклонение|r"
    wts_updates[43063] = "|cffe4cfa3Уклонение|r"
    wts_updates[43064] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует |cffffffff15%|cffced4da шанс полностью избежать вражеской атаки.|r"
    )
    checks_def.append({"type": "ability", "id": "A14K", "field": "name", "expected": wts_updates[43062]})
    checks_def.append({"type": "ability", "id": "A14K", "field": "tip1", "expected": wts_updates[43063]})
    checks_def.append({"type": "ability", "id": "A14K", "field": "ubertip1", "expected": wts_updates[43064]})

    # A14L: Рассеивание чар (Q)
    wts_updates[27493] = "|cffe4cfa3Рассеивание чар|r"
    wts_updates[27494] = "|cffe4cfa3Рассеивание чар|r (|cffffffffQ|r)"
    wts_updates[27502] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает положительные эффекты с врагов и отрицательные с союзников в указанной области, а также наносит урон призванным существам.|r"
    )
    checks_def.append({"type": "ability", "id": "A14L", "field": "name", "expected": wts_updates[27493]})
    checks_def.append({"type": "ability", "id": "A14L", "field": "tip1", "expected": wts_updates[27494]})
    checks_def.append({"type": "ability", "id": "A14L", "field": "ubertip1", "expected": wts_updates[27502]})

    # A14M: Прилив сил (W, 2 уровня)
    wts_updates[43065] = "|cffe4cfa3Прилив сил|r"
    wts_updates[43066] = "|cffe4cfa3Прилив сил — уровень 1|r (|cffffffffW|r)"
    wts_updates[43067] = "|cffe4cfa3Прилив сил — уровень 2|r (|cffffffffW|r)"
    wts_updates[43068] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура воодушевления, увеличивающая скорость перемещения окружающих союзных войск на |cffc8e087+10%|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[43069] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура воодушевления, увеличивающая скорость перемещения окружающих союзных войск на |cffc8e087+20%|cffced4da.|n|n"
        "|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A14M", "field": "name", "expected": wts_updates[43065]})
    checks_def.append({"type": "ability", "id": "A14M", "field": "tip1", "expected": wts_updates[43066]})
    checks_def.append({"type": "ability", "id": "A14M", "field": "ubertip1", "expected": wts_updates[43068]})

    # A14N: Целительная вода (W)
    wts_updates[43072] = "|cffe4cfa3Целительная вода|r"
    wts_updates[43073] = "|cffe4cfa3Целительная вода|r (|cffffffffW|r)"
    wts_updates[43074] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e087+25|cffced4da ед. здоровья раненому живому союзнику.|r"
    )
    checks_def.append({"type": "ability", "id": "A14N", "field": "name", "expected": wts_updates[43072]})
    checks_def.append({"type": "ability", "id": "A14N", "field": "tip1", "expected": wts_updates[43073]})
    checks_def.append({"type": "ability", "id": "A14N", "field": "ubertip1", "expected": wts_updates[43074]})

    # A1OL: Противодействие (Коатль)
    wts_updates[43130] = "|cffe4cfa3Противодействие|r"
    wts_updates[43129] = "|cffe4cfa3Противодействие|r"
    wts_updates[43131] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака сжигает |cffffffff20|cffced4da ед. маны у обычных целей (|cffffffff4|cffced4da у героев) и наносит сожжённый объём в виде дополнительного урона.|r"
    )
    checks_def.append({"type": "ability", "id": "A1OL", "field": "name", "expected": wts_updates[43130]})
    checks_def.append({"type": "ability", "id": "A1OL", "field": "tip1", "expected": wts_updates[43129]})
    checks_def.append({"type": "ability", "id": "A1OL", "field": "ubertip1", "expected": wts_updates[43131]})

    # A1OM: Едкая слюна (Q)
    wts_updates[43018] = "|cffe4cfa3Едкая слюна|r"
    wts_updates[43019] = "|cffe4cfa3Едкая слюна|r (|cffffffffQ|r)"
    wts_updates[43020] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Плюёт кислотой во вражескую цель, нанося урон по площади и снижая защиту поражённых врагов на |cffe69a8d5|cffced4da ед.|r"
    )
    checks_def.append({"type": "ability", "id": "A1OM", "field": "name", "expected": wts_updates[43018]})
    checks_def.append({"type": "ability", "id": "A1OM", "field": "tip1", "expected": wts_updates[43019]})
    checks_def.append({"type": "ability", "id": "A1OM", "field": "ubertip1", "expected": wts_updates[43020]})

    # A1ON: Щит молний (W)
    wts_updates[43136] = "|cffe4cfa3Щит молний|r"
    wts_updates[43135] = "|cffe4cfa3Щит молний|r (|cffffffffW|r)"
    wts_updates[43137] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает выбранную цель электрическим щитом, наносящим |cffffffff20|cffced4da ед. урона в секунду находящимся рядом войскам.|r"
    )
    checks_def.append({"type": "ability", "id": "A1ON", "field": "name", "expected": wts_updates[43136]})
    checks_def.append({"type": "ability", "id": "A1ON", "field": "tip1", "expected": wts_updates[43135]})
    checks_def.append({"type": "ability", "id": "A1ON", "field": "ubertip1", "expected": wts_updates[43137]})

    # A1OO: Сила молний (Q)
    wts_updates[43138] = "|cffe4cfa3Сила молний|r"

    # A1OP: Цепь молний (E)
    wts_updates[43139] = "|cffe4cfa3Цепь молний|r"
    wts_updates[43140] = "|cffe4cfa3Цепь молний|r (|cffffffffE|r)"
    wts_updates[43141] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает разряд молнии, наносящий |cffffffff100|cffced4da ед. урона цели и перескакивающий на несколько стоящих рядом противников.|r"
    )
    checks_def.append({"type": "ability", "id": "A1OP", "field": "name", "expected": wts_updates[43139]})
    checks_def.append({"type": "ability", "id": "A1OP", "field": "tip1", "expected": wts_updates[43140]})
    checks_def.append({"type": "ability", "id": "A1OP", "field": "ubertip1", "expected": wts_updates[43141]})

    # A1OQ: Сила молний
    wts_updates[43142] = "|cffe4cfa3Сила молний|r"
    wts_updates[43143] = "|cffe4cfa3Сила молний|r"
    wts_updates[43144] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс при атаке применить к цели рассеивание чар, снимая положительные эффекты.|r"
    )
    checks_def.append({"type": "ability", "id": "A1OQ", "field": "name", "expected": wts_updates[43142]})
    checks_def.append({"type": "ability", "id": "A1OQ", "field": "tip1", "expected": wts_updates[43143]})
    checks_def.append({"type": "ability", "id": "A1OQ", "field": "ubertip1", "expected": wts_updates[43144]})

    # A1OR: Каннибализм (Q)
    wts_updates[43145] = "|cffe4cfa3Каннибализм|r"
    wts_updates[43146] = "|cffe4cfa3Каннибализм|r (|cffffffffQ|r)"
    wts_updates[43147] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пожирает находящийся рядом труп, восстанавливая по |cffc8e087+15|cffced4da ед. здоровья в секунду.|r"
    )
    checks_def.append({"type": "ability", "id": "A1OR", "field": "name", "expected": wts_updates[43145]})
    checks_def.append({"type": "ability", "id": "A1OR", "field": "tip1", "expected": wts_updates[43146]})
    checks_def.append({"type": "ability", "id": "A1OR", "field": "ubertip1", "expected": wts_updates[43147]})

    # AChx: Сглаз (E)
    wts_updates[26682] = "|cffe4cfa3Сглаз|r"
    wts_updates[29612] = "|cffe4cfa3Сглаз|r (|cffffffffE|r)"
    wts_updates[25830] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Превращает вражеского воина в случайное беззащитное животное на несколько секунд, запрещая атаковать и применять заклинания.|r"
    )
    checks_def.append({"type": "ability", "id": "AChx", "field": "name", "expected": wts_updates[26682]})
    checks_def.append({"type": "ability", "id": "AChx", "field": "tip1", "expected": wts_updates[29612]})
    checks_def.append({"type": "ability", "id": "AChx", "field": "ubertip1", "expected": wts_updates[25830]})

    # S00A: Стойкость моря
    wts_updates[25867] = "|cffe4cfa3Стойкость моря|r"
    wts_updates[25882] = "|cffe4cfa3Стойкость моря|r"
    wts_updates[25892] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура глубин, увеличивающая скорость атаки и скорость перемещения ближайших союзников.|r"
    )
    checks_def.append({"type": "ability", "id": "S00A", "field": "name", "expected": wts_updates[25867]})
    checks_def.append({"type": "ability", "id": "S00A", "field": "tip1", "expected": wts_updates[25882]})
    checks_def.append({"type": "ability", "id": "S00A", "field": "ubertip1", "expected": wts_updates[25892]})

    # ACcb: Ледяная стрела (W) — Ancient Naga
    wts_updates[25822] = "|cffe4cfa3Ледяная стрела|r"
    wts_updates[25826] = "|cffe4cfa3Ледяная стрела|r (|cffffffffW|r)"
    wts_updates[25829] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит цели урон льдом и оглушает её на короткое время.|r"
    )
    checks_def.append({"type": "ability", "id": "ACcb", "field": "name", "expected": wts_updates[25822]})
    checks_def.append({"type": "ability", "id": "ACcb", "field": "tip1", "expected": wts_updates[25826]})
    checks_def.append({"type": "ability", "id": "ACcb", "field": "ubertip1", "expected": wts_updates[25829]})

    # ACen: Опутывание (E) — Murloc Hunter
    wts_updates[26448] = "|cffe4cfa3Опутывание|r"
    wts_updates[26452] = "|cffe4cfa3Опутывание|r (|cffffffffE|r)"
    wts_updates[26453] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Опутывает цель сетью, прижимая воздушных врагов к земле и лишая подвижности.|r"
    )
    checks_def.append({"type": "ability", "id": "ACen", "field": "name", "expected": wts_updates[26448]})
    checks_def.append({"type": "ability", "id": "ACen", "field": "tip1", "expected": wts_updates[26452]})
    checks_def.append({"type": "ability", "id": "ACen", "field": "ubertip1", "expected": wts_updates[26453]})

    # ACfu: Ледяная броня (W) — Siren
    wts_updates[26410] = "|cffe4cfa3Ледяная броня|r"
    wts_updates[26412] = "|cffe4cfa3Ледяная броня|r (|cffffffffW|r)"
    wts_updates[26413] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает союзника ледяным щитом, увеличивающим броню и замедляющим скорость атаки и передвижения нападающих врагов ближнего боя.|r"
    )
    checks_def.append({"type": "ability", "id": "ACfu", "field": "name", "expected": wts_updates[26410]})
    checks_def.append({"type": "ability", "id": "ACfu", "field": "tip1", "expected": wts_updates[26412]})
    checks_def.append({"type": "ability", "id": "ACfu", "field": "ubertip1", "expected": wts_updates[26413]})

    # ACpv: Сокрушение — Sea Hunter
    wts_updates[25786] = "|cffe4cfa3Сокрушение|r"
    wts_updates[25800] = "|cffe4cfa3Сокрушение|r"
    wts_updates[25817] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс при атаке нанести дополнительный урон и оглушить цель.|r"
    )
    checks_def.append({"type": "ability", "id": "ACpv", "field": "name", "expected": wts_updates[25786]})
    checks_def.append({"type": "ability", "id": "ACpv", "field": "tip1", "expected": wts_updates[25800]})
    checks_def.append({"type": "ability", "id": "ACpv", "field": "ubertip1", "expected": wts_updates[25817]})

    # ACsk: Устойчивая кожа — Ancient Naga & Naga Guard
    wts_updates[26379] = "|cffe4cfa3Устойчивая кожа|r"
    wts_updates[26380] = "|cffe4cfa3Устойчивая кожа|r"
    checks_def.append({"type": "ability", "id": "ACsk", "field": "name", "expected": wts_updates[26379]})
    checks_def.append({"type": "ability", "id": "ACsk", "field": "tip1", "expected": wts_updates[26380]})

    # ANen: Опутывание (Q) — Myrmidon
    wts_updates[25812] = "|cffe4cfa3Опутывание|r"
    wts_updates[29831] = "|cffe4cfa3Опутывание|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "ANen", "field": "name", "expected": wts_updates[25812]})
    checks_def.append({"type": "ability", "id": "ANen", "field": "tip1", "expected": wts_updates[29831]})

    # ANpa: Паразит (R) — Siren
    wts_updates[26402] = "|cffe4cfa3Паразит|r"
    wts_updates[26403] = "|cffe4cfa3Паразит|r (|cffffffffR|r)"
    wts_updates[26404] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Заражает врага смертоносным паразитом, наносящим периодический урон в секунду.|r"
    )
    checks_def.append({"type": "ability", "id": "ANpa", "field": "name", "expected": wts_updates[26402]})
    checks_def.append({"type": "ability", "id": "ANpa", "field": "tip1", "expected": wts_updates[26403]})
    checks_def.append({"type": "ability", "id": "ANpa", "field": "ubertip1", "expected": wts_updates[26404]})

    # Acny: Торнадо (C) — Siren
    wts_updates[26405] = "|cffe4cfa3Торнадо|r"
    wts_updates[26406] = "|cffe4cfa3Торнадо|r (|cffffffffC|r)"
    wts_updates[26407] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает вражеского воина в воздух во вращающийся вихрь, лишая возможности атаковать, передвигаться и применять заклинания.|r"
    )
    checks_def.append({"type": "ability", "id": "Acny", "field": "name", "expected": wts_updates[26405]})
    checks_def.append({"type": "ability", "id": "Acny", "field": "tip1", "expected": wts_updates[26406]})
    checks_def.append({"type": "ability", "id": "Acny", "field": "ubertip1", "expected": wts_updates[26407]})

    # Asb2: Погружение (U) — Naga Guard & Ancient Naga
    wts_updates[26454] = "|cffe4cfa3Погружение|r"
    wts_updates[26455] = "|cffe4cfa3Погружение|r (|cffffffffU|r)"
    wts_updates[26456] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Воин погружается под воду, становясь невидимым для противников.|r"
    )
    checks_def.append({"type": "ability", "id": "Asb2", "field": "name", "expected": wts_updates[26454]})
    checks_def.append({"type": "ability", "id": "Asb2", "field": "tip1", "expected": wts_updates[26455]})
    checks_def.append({"type": "ability", "id": "Asb2", "field": "ubertip1", "expected": wts_updates[26456]})

    # drAq: Ледяная стрела (Q) — Naga Guard
    wts_updates[17102] = "|cffe4cfa3Ледяная стрела|r"
    wts_updates[17107] = "|cffe4cfa3Ледяная стрела|r (|cffffffffQ|r)"
    wts_updates[23597] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелу льда, наносящую |cffffffff140|cffced4da ед. урона врагу и оглушающую его на |cffffffff7|cffced4da сек. (|cffffffff0.5|cffced4da сек. для героев).|r"
    )
    checks_def.append({"type": "ability", "id": "drAq", "field": "name", "expected": wts_updates[17102]})
    checks_def.append({"type": "ability", "id": "drAq", "field": "tip1", "expected": wts_updates[17107]})
    checks_def.append({"type": "ability", "id": "drAq", "field": "ubertip1", "expected": wts_updates[23597]})

    # =========================================================================
    # 8. BUFFS
    # =========================================================================
    # B06G: Безумие
    wts_updates[25851] = "|cffe4cfa3Безумие|r"
    checks_def.append({"type": "buff", "id": "B06G", "field": "bufftip", "expected": wts_updates[25851]})

    # B08I: Своя стихия
    wts_updates[30405] = "|cffe4cfa3Своя стихия|r"
    wts_updates[35313] = "|cffa6afb8ЭФФЕКТ:|cffced4da Скорость атаки и перемещения в воде увеличена.|r"
    checks_def.append({"type": "buff", "id": "B08I", "field": "bufftip", "expected": wts_updates[30405]})
    checks_def.append({"type": "buff", "id": "B08I", "field": "buffubertip", "expected": wts_updates[35313]})

    # =========================================================================
    # BUILD MASTER PLAN DATA
    # =========================================================================
    categories = {
        "selection": ["A14O"],
        "markers": ["R0FS", "R0KZ"],
        "buildings": [
            "h0JW", "h0JX", "h0JY", "n04L", "n055",
            "nnfm", "nnsa", "nnsg", "nntg", "nntt"
        ],
        "worker": ["nmpe"],
        "units": [
            "n04Z", "n050", "n051", "n052", "n053", "n054", "n056", "n057",
            "n079", "nmyr", "nnmg", "nnrg", "nnsw", "nwgs", "nsnp", "nhyc"
        ],
        "heroes": ["H0JU", "H0JV", "H0OZ", "N07A", "N054"],
        "upgrades": [
            "R0FE", "R0FF", "R0FD", "R0FH", "R0FP", "R0FQ", "R0FR",
            "R0KP", "Rnam", "Rnat", "Rnen", "Rnsb", "Rnsi", "Rnsw"
        ],
        "abilities": [
            "A14O", "A13C", "AEbl", "A13A", "A13D", "A136", "A137", "A138", "A139", "A135",
            "A14F", "A14G", "A14H", "A14I", "AEtq", "AHbn", "AHab", "ANrf",
            "A16B", "A16C", "A16D", "A16E", "A1LT", "S00E", "A1LV", "A13B", "A14J",
            "A14K", "A14L", "A14M", "A14N", "A1OL", "A1OM", "A1ON", "A1OO", "A1OP",
            "A1OQ", "A1OR", "AChx", "S00A", "ACcb", "ACen", "ACfu", "ACpv", "ACsk",
            "ANen", "ANpa", "Acny", "Asb2", "drAq"
        ],
        "buffs": ["B06G", "B08I"]
    }

    plan_data = {
        "race": "Nagi",
        "race_name_ru": "Наги",
        "race_id": 25,
        "total_updates": len(wts_updates),
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": categories
    }

    plan_file = folder / "nagi_plan.json"
    plan_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {plan_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

    # =========================================================================
    # GENERATE CATEGORY REGISTRIES (docs/ui_text/nagi_*.json)
    # =========================================================================
    raw_dump_path = ROOT / "scripts/nagi_raw_dump.json"
    dump = json.loads(raw_dump_path.read_text(encoding="utf-8")) if raw_dump_path.exists() else {}

    # 1. nagi_selection.json
    sel_data = {
        "scope": "Наги (Nagi): подсказка выбора расы A14O и маркеры",
        "object": "A14O",
        "variants": ["SD"],
        "hotkey": {"value": "D"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Nagi регистрирует способность A14O.",
            "При выборе создаются 5 рабочих nmpe, исследуется маркер R0FS, удаляется выбирающий юнит.",
            "Горячая клавиша D, создатель Escanor (Яхве), куратор VinerX, сложность 1/5 (●○○○○), период «Cataclysm»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38901, "after": wts_updates[38901]},
            {"field": "tip1", "wts_id": 38902, "after": wts_updates[38902]},
            {"field": "ubertip1", "wts_id": 32513, "after": wts_updates[32513]}
        ],
        "markers": [
            {
                "id": "R0FS",
                "name": "Наги (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 43187, "after": wts_updates.get(43187)},
                    {"field": "tip1", "wts_id": 43188, "after": wts_updates.get(43188)},
                    {"field": "ubertip1", "wts_id": 43189, "after": wts_updates.get(43189)}
                ]
            },
            {
                "id": "R0KZ",
                "name": "Иллидари или Наги (маркер союза)",
                "strings": [
                    {"field": "name1", "wts_id": 5721, "after": wts_updates.get(5721)},
                    {"field": "tip1", "wts_id": 9416, "after": wts_updates.get(9416)},
                    {"field": "ubertip1", "wts_id": 12518, "after": wts_updates.get(12518)}
                ]
            }
        ]
    }
    (folder / "nagi_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nagi_selection.json")

    def parse_str_id(raw):
        if isinstance(raw, str) and raw.startswith("TRIGSTR_"):
            try:
                return int(raw[8:])
            except ValueError:
                return None
        return None

    # 2. nagi_buildings.json
    bld_entries = []
    for b in dump.get("buildings", []):
        b_id = b["id"]
        entry = {
            "id": b_id,
            "hotkey": b.get("hotkey"),
            "strings": []
        }
        for f in ["name", "tip", "ubertip"]:
            raw_v = b.get(f"raw_{f}")
            sid = parse_str_id(raw_v)
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        bld_entries.append(entry)

    bld_data = {
        "scope": "Наги (Nagi): категория 2 — Здания (10 объектов)",
        "count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "nagi_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nagi_buildings.json")

    # 3. nagi_units.json (worker + 16 combat units)
    unit_entries = []
    for u in dump.get("worker", []) + dump.get("units", []):
        u_id = u["id"]
        if u_id == "ntor":
            continue
        entry = {
            "id": u_id,
            "hotkey": u.get("hotkey"),
            "strings": []
        }
        for f in ["name", "tip", "ubertip"]:
            raw_v = u.get(f"raw_{f}")
            sid = parse_str_id(raw_v)
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        unit_entries.append(entry)

    unit_data = {
        "scope": "Наги (Nagi): категория 3 — Юниты и рабочий (17 объектов)",
        "count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "nagi_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nagi_units.json")

    # 4. nagi_heroes.json
    hero_entries = []
    for h in dump.get("heroes", []):
        h_id = h["id"]
        entry = {
            "id": h_id,
            "hotkey": h.get("hotkey"),
            "strings": []
        }
        for f in ["name", "tip", "ubertip"]:
            raw_v = h.get(f"raw_{f}")
            sid = parse_str_id(raw_v)
            if sid and sid in wts_updates:
                entry["strings"].append({
                    "field": f,
                    "wts_id": sid,
                    "after": wts_updates[sid]
                })
        hero_entries.append(entry)

    hero_data = {
        "scope": "Наги (Nagi): категория 4 — Герои (5 объектов: 3 обычных, 1 легендарный + дубликат)",
        "count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "nagi_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nagi_heroes.json")

    # 5. nagi_research.json
    upg_entries = []
    for up in dump.get("upgrades", []):
        up_id = up["id"]
        entry = {
            "id": up_id,
            "levels": up.get("levels", 1),
            "strings": []
        }
        for k, v in up.get("names", {}).items():
            sid = v.get("sid")
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"name_{k}", "wts_id": sid, "after": wts_updates[sid]})
        for k, v in up.get("tips", {}).items():
            sid = v.get("sid")
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"tip_{k}", "wts_id": sid, "after": wts_updates[sid]})
        for k, v in up.get("ubertips", {}).items():
            sid = v.get("sid")
            if sid and sid in wts_updates:
                entry["strings"].append({"field": f"ubertip_{k}", "wts_id": sid, "after": wts_updates[sid]})
        if entry["strings"]:
            upg_entries.append(entry)

    research_data = {
        "scope": "Наги (Nagi): категория 5 — Исследования и технологии",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "nagi_research.json").write_text(json.dumps(research_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nagi_research.json")

    # 6. nagi_abilities.json
    abil_entries = []
    for ab in dump.get("abilities", []):
        ab_id = ab["id"]
        entry = {
            "id": ab_id,
            "levels": ab.get("levels", 1),
            "strings": []
        }
        name_sid = ab.get("name_sid")
        if name_sid and name_sid in wts_updates:
            entry["strings"].append({"field": "name", "wts_id": name_sid, "after": wts_updates[name_sid]})
        for k, v in ab.get("tips", {}).items():
            sid = v.get("sid")
            if sid and sid in wts_updates:
                entry["strings"].append({"field": k, "wts_id": sid, "after": wts_updates[sid]})
        for k, v in ab.get("ubertips", {}).items():
            sid = v.get("sid")
            if sid and sid in wts_updates:
                entry["strings"].append({"field": k, "wts_id": sid, "after": wts_updates[sid]})
        if entry["strings"]:
            abil_entries.append(entry)

    abil_data = {
        "scope": "Наги (Nagi): категория 6 — Способности зданий, юнитов и героев",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "nagi_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nagi_abilities.json")

    # 7. nagi_audit.json
    audit_data = {
        "race": "Наги (Nagi)",
        "race_id": 25,
        "selection_ability": "A14O",
        "selection_marker": "R0FS",
        "objects_audit": {
            "buildings": {
                "count": 10,
                "ids": ["h0JW", "h0JX", "h0JY", "n04L", "n055", "nnfm", "nnsa", "nnsg", "nntg", "nntt"],
                "economy_building": {
                    "id": "nnfm",
                    "name": "Коралловый риф",
                    "food_provided": 40,
                    "gold_income_per_25s": 30,
                    "limit": 15,
                    "verified_via": "01_core_economy.lua and unit object stats"
                }
            },
            "worker": {
                "count": 1,
                "ids": ["nmpe"]
            },
            "units": {
                "count": 16,
                "ids": [
                    "n04Z", "n050", "n051", "n052", "n053", "n054", "n056", "n057",
                    "n079", "nmyr", "nnmg", "nnrg", "nnsw", "nwgs", "nsnp", "nhyc"
                ]
            },
            "heroes": {
                "count": 4,
                "ids": ["H0JU", "H0JV", "H0OZ", "N07A"],
                "duplicate_ids": ["N054"],
                "names": {
                    "H0JU": "Владыка-страж (Сила, ближний бой)",
                    "H0JV": "Глубинная охотница (Ловкость, дальний бой)",
                    "H0OZ": "Мурлок-гигант (Сила, ближний бой)",
                    "N07A": "Мурлок-чародей (Легендарный герой, Интеллект, дальний бой)",
                    "N054": "Мурлок-чародей (дубликат/сломанный)"
                }
            },
            "researches": {
                "count": 14,
                "ids": [
                    "R0FS", "R0KZ", "R0FE", "R0FF", "R0FD", "R0FH", "R0FP", "R0FQ", "R0FR",
                    "R0KP", "Rnam", "Rnat", "Rnen", "Rnsb", "Rnsi", "Rnsw"
                ]
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(wts_updates)
            },
            "buffs": {
                "count": 2,
                "ids": ["B06G", "B08I"]
            }
        },
        "triggers_audit": {
            "file": "80_runtime/triggers/races/Naga.lua",
            "findings": [
                "InitTrig_NagaStart sets tech limits at 2s (n054, n053, n052, n050, n051, n057, nnsw, nmyr, nnrg, N07A=1, H0OZ=0, H0JU=0, H0JV=1, R0FQ=0).",
                "InitTrig_Coatl sets flight height 240 for nwgs.",
                "InitTrig_MurlokCan, InitTrig_MurlokBeg, InitTrig_MurlocFin handle mutual exclusivity for R0FF and unlocks n053, n052, n050, n054, H0OZ, R0FQ.",
                "InitTrig_Nagi, InitTrig_Nagi2, InitTrig_NagaFinishCode handle mutual exclusivity for R0FE and unlocks n051, n057, nnsw, nmyr, nnrg, R0KZ, H0JU.",
                "InitTrig_VaishBuria summons tornado ntor on A16E cast for 30s.",
                "InitTrig_VaishArrow triggers dummy frost nova A16D on A16C attack.",
                "InitTrig_NagaPas manages passive trident abilities A136..A139 based on A13A level.",
                "InitTrig_NagaCommonSpell grants S00E for 180s on A1LT cast in water.",
                "No custom items or player-facing chat/screen messages found in trigger code."
            ]
        }
    }
    (folder / "nagi_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote nagi_audit.json")

if __name__ == "__main__":
    main()
