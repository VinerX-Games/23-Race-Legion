# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Nightborne race (Race 18)."""
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
    # 1. RACE SELECTION: A0HU, R07J
    # =========================================================================
    wts_updates[38875] = "|cffe4cfa3Ночнорождённые|r"
    wts_updates[38876] = "|cffe4cfa3Ночнорождённые|r (|cffffffffE|r)"
    wts_updates[21994] = (
        "|cffa6afb8РАСА:|cffced4da Древняя эльфийская цивилизация Сурамара, овладевшая мощью тайной магии Ночного Колодца.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deNiCAmCHiK|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●|cffa6afb8●●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Legion — Battle for Azeroth»|r|n|n"
        "|cffced4daНочнорождённые — эльфы Сурамара, проведшие десять тысяч лет под защитой магического барьера. За долгие века изоляции "
        "они научились черпать неисчерпаемую силу из Ночного Колодца, создав непревзойдённую школу тайной магии. Отвоевав свободу "
        "в жестокой гражданской войне против демонов Пылающего Легиона, ночнорождённые присоединились к Орде. "
        "Их армия сочетает стойкую Сумеречную стражу, искусных лунных магов, зачарованные глефомёты и боевых зверей, защищённых древними чарами и щитами маны.|r"
    )

    checks_def.append({"type": "ability", "id": "A0HU", "field": "name", "expected": wts_updates[38875]})
    checks_def.append({"type": "ability", "id": "A0HU", "field": "tip1", "expected": wts_updates[38876]})
    checks_def.append({"type": "ability", "id": "A0HU", "field": "ubertip1", "expected": wts_updates[21994]})

    # Selection marker: R07J
    wts_updates[10667] = "|cffe4cfa3Ночнорождённые|r"
    wts_updates[10668] = "|cffe4cfa3Ночнорождённые|r"
    wts_updates[20117] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Ночнорождённым (Шал'дорай).|r"

    checks_def.append({"type": "upgrade", "id": "R07J", "field": "name1", "expected": wts_updates[10667]})
    checks_def.append({"type": "upgrade", "id": "R07J", "field": "tip1", "expected": wts_updates[10668]})
    checks_def.append({"type": "upgrade", "id": "R07J", "field": "ubertip1", "expected": wts_updates[20117]})

    # =========================================================================
    # 2. BUILDINGS (12 buildings)
    # =========================================================================
    # h0CB: Ратуша (Q)
    wts_updates[7295] = "|cffe4cfa3Ратуша|r"
    wts_updates[16271] = "|cffe4cfa3Ратуша|r (|cffffffffQ|r)"
    wts_updates[5692] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Ночнорождённых первой ступени. Обучает работников и служит складом ресурсов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deФорт|cffced4da: открывает доступ к передовым сооружениям и войскам Ночнорождённых.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CB", "field": "name", "expected": wts_updates[7295]})
    checks_def.append({"type": "unit", "id": "h0CB", "field": "tip", "expected": wts_updates[16271]})
    checks_def.append({"type": "unit", "id": "h0CB", "field": "ubertip", "expected": wts_updates[5692]})

    # h0CC: Форт (Z)
    wts_updates[7298] = "|cffe4cfa3Форт|r"
    wts_updates[16276] = "|cffe4cfa3Форт|r (|cffffffffZ|r)"
    wts_updates[13064] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Ночнорождённых второй ступени. Открывает доступ к новым сооружениям и улучшенным войскам.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЗамок|cffced4da: открывает доступ к высшим технологиям и элитным войскам.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CC", "field": "name", "expected": wts_updates[7298]})
    checks_def.append({"type": "unit", "id": "h0CC", "field": "tip", "expected": wts_updates[16276]})
    checks_def.append({"type": "unit", "id": "h0CC", "field": "ubertip", "expected": wts_updates[13064]})

    # h0CD: Замок (Z)
    wts_updates[7300] = "|cffe4cfa3Замок|r"
    wts_updates[16294] = "|cffe4cfa3Замок|r (|cffffffffZ|r)"
    wts_updates[13065] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Ночнорождённых третьей ступени. Открывает доступ к высшим ступеням улучшений и могущественной способности «Благодать маны».|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CD", "field": "name", "expected": wts_updates[7300]})
    checks_def.append({"type": "unit", "id": "h0CD", "field": "tip", "expected": wts_updates[16294]})
    checks_def.append({"type": "unit", "id": "h0CD", "field": "ubertip", "expected": wts_updates[13065]})

    # h0CE: Кристалл маны (A)
    wts_updates[7282] = "|cffe4cfa3Кристалл маны|r"
    wts_updates[7283] = "|cffe4cfa3Кристалл маны|r (|cffffffffA|r)"
    wts_updates[31698] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Ночнорождённых запасом пищи и вырабатывает регулярный доход.|n|n"
        "Даёт |cffffffff15|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+20|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CE", "field": "name", "expected": wts_updates[7282]})
    checks_def.append({"type": "unit", "id": "h0CE", "field": "tip", "expected": wts_updates[7283]})
    checks_def.append({"type": "unit", "id": "h0CE", "field": "ubertip", "expected": wts_updates[31698]})

    # h0CF: Казармы (W)
    wts_updates[7284] = "|cffe4cfa3Казармы|r"
    wts_updates[16303] = "|cffe4cfa3Казармы|r (|cffffffffW|r)"
    wts_updates[13026] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает базовые пехотные и осадные силы Ночнорождённых.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deШал'дорайская воительница|cffced4da: ловкая мечница ближнего боя.|n"
        "- |cffa9c7deНаследник Сумеречной стражи|cffced4da: бронированный передовой боевой маг.|n"
        "- |cffa9c7deГлефомет|cffced4da: осадное орудие дальнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da|n"
        "- |cffa9c7deЛунные глефы|cffced4da|n"
        "- |cffa9c7deЗачарованные доспехи|cffced4da|n"
        "- |cffa9c7deСтальные снаряды|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CF", "field": "name", "expected": wts_updates[7284]})
    checks_def.append({"type": "unit", "id": "h0CF", "field": "tip", "expected": wts_updates[16303]})
    checks_def.append({"type": "unit", "id": "h0CF", "field": "ubertip", "expected": wts_updates[13026]})

    # h0CG: Алтарь маны (S)
    wts_updates[7293] = "|cffe4cfa3Алтарь маны|r"
    wts_updates[27926] = "|cffe4cfa3Алтарь маны|r (|cffffffffS|r)"
    wts_updates[12972] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Позволяет призывать и воскрешать героев Ночнорождённых.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deКапитан Шал'дорайской стражи|cffced4da: могучий воин ближнего боя (Сила).|n"
        "- |cffa9c7deМрачная Тень|cffced4da: меткий стрелок дальнего боя (Ловкость).|n"
        "- |cffa9c7deВерховный лунный маг|cffced4da: повелитель тайной магии (Интеллект).|r"
    )
    checks_def.append({"type": "unit", "id": "h0CG", "field": "name", "expected": wts_updates[7293]})
    checks_def.append({"type": "unit", "id": "h0CG", "field": "tip", "expected": wts_updates[27926]})
    checks_def.append({"type": "unit", "id": "h0CG", "field": "ubertip", "expected": wts_updates[12972]})

    # h0CH: Лесопилка (E)
    wts_updates[7302] = "|cffe4cfa3Лесопилка|r"
    wts_updates[20964] = "|cffe4cfa3Лесопилка|r (|cffffffffE|r)"
    wts_updates[13068] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит складом древесины и центром боевых улучшений армии Ночнорождённых.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЗачарование силы|cffced4da|n"
        "- |cffa9c7deЛунные доспехи|cffced4da|n"
        "- |cffa9c7deМагическая атака|cffced4da|n"
        "- |cffa9c7deПрочные доспехи|cffced4da|n"
        "- |cffa9c7deРодство с маной|cffced4da|n"
        "- |cffa9c7deУлучшенные инструменты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CH", "field": "name", "expected": wts_updates[7302]})
    checks_def.append({"type": "unit", "id": "h0CH", "field": "tip", "expected": wts_updates[20964]})
    checks_def.append({"type": "unit", "id": "h0CH", "field": "ubertip", "expected": wts_updates[13068]})

    # h0CI: Святилище маны (D)
    wts_updates[7305] = "|cffe4cfa3Святилище маны|r"
    wts_updates[7306] = "|cffe4cfa3Святилище маны|r (|cffffffffD|r)"
    wts_updates[13009] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обучает заклинателей Ночнорождённых и открывает их магические способности.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЛунный маг|cffced4da: могущественный атакующий маг.|n"
        "- |cffa9c7deШал'дорайский аристократ|cffced4da: маг поддержки и призыватель.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deДревнее знание|cffced4da|n"
        "- |cffa9c7deКонтроль над маной|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CI", "field": "name", "expected": wts_updates[7305]})
    checks_def.append({"type": "unit", "id": "h0CI", "field": "tip", "expected": wts_updates[7306]})
    checks_def.append({"type": "unit", "id": "h0CI", "field": "ubertip", "expected": wts_updates[13009]})

    # h0CK: Храм жизни (R)
    wts_updates[7318] = "|cffe4cfa3Храм жизни|r"
    wts_updates[7319] = "|cffe4cfa3Храм жизни|r (|cffffffffR|r)"
    wts_updates[13069] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священная обитель, подготавливающая целителей и укротителей зверей Ночнорождённых.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЗвериный страж|cffced4da: всадник на боевом леопарде.|n"
        "- |cffa9c7deПоклонник|cffced4da: верховный целитель и темпомант.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПосвящение Темпомантов|cffced4da|n"
        "- |cffa9c7deТайная магия|cffced4da|n"
        "- |cffa9c7deМагическая сеть|cffced4da|n"
        "- |cffa9c7deСовместные тренировки|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CK", "field": "name", "expected": wts_updates[7318]})
    checks_def.append({"type": "unit", "id": "h0CK", "field": "tip", "expected": wts_updates[7319]})
    checks_def.append({"type": "unit", "id": "h0CK", "field": "ubertip", "expected": wts_updates[13069]})

    # h0CL: Дом Шал'дорайской стражи (D)
    wts_updates[7320] = "|cffe4cfa3Дом Шал'дорайской стражи|r"
    wts_updates[7321] = "|cffe4cfa3Дом Шал'дорайской стражи|r (|cffffffffD|r)"
    wts_updates[13070] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Военная академия, подготавливающая элитных бойцов и командиров Ночнорождённых.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deШал'дорайский гвардеец|cffced4da: тяжёлый пехотинец, подавляющий магию врагов.|n"
        "- |cffa9c7deТемный клинок|cffced4da: скрытный убийца, наносящий сокрушительные критические удары.|n"
        "- |cffa9c7deСумеречный страж|cffced4da: тактический командир с усиливающей аурой и замедляющими оковами.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМана-броня|cffced4da|n"
        "- |cffa9c7deРассекающие клинки|cffced4da|n"
        "- |cffa9c7deКомандирская аура|cffced4da|n"
        "- |cffa9c7deМагические оковы|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CL", "field": "name", "expected": wts_updates[7320]})
    checks_def.append({"type": "unit", "id": "h0CL", "field": "tip", "expected": wts_updates[7321]})
    checks_def.append({"type": "unit", "id": "h0CL", "field": "ubertip", "expected": wts_updates[13070]})

    # h0CM: Магическая башня (Z)
    wts_updates[3277] = "|cffe4cfa3Магическая башня|r"
    wts_updates[20965] = "|cffe4cfa3Магическая башня|r (|cffffffffZ|r)"
    wts_updates[8398] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение Ночнорождённых. Атакует цели всплесками чистой магии, сжигающими запас маны и наносящими повышенный урон призванным существам.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПротиводействие|cffced4da: уничтожает ману цели при попадании.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CM", "field": "name", "expected": wts_updates[3277]})
    checks_def.append({"type": "unit", "id": "h0CM", "field": "tip", "expected": wts_updates[20965]})
    checks_def.append({"type": "unit", "id": "h0CM", "field": "ubertip", "expected": wts_updates[8398]})

    # h0D8: Верфь (C)
    wts_updates[10907] = "|cffe4cfa3Верфь|r"
    wts_updates[10908] = "|cffe4cfa3Верфь|r (|cffffffffC|r)"
    wts_updates[10903] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Морское сооружение для строительства и оснащения боевых кораблей.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТранспортный корабль|cffced4da|n"
        "- |cffa9c7deФрегат|cffced4da|n"
        "- |cffa9c7deЛинкор|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h0D8", "field": "name", "expected": wts_updates[10907]})
    checks_def.append({"type": "unit", "id": "h0D8", "field": "tip", "expected": wts_updates[10908]})
    checks_def.append({"type": "unit", "id": "h0D8", "field": "ubertip", "expected": wts_updates[10903]})

    # =========================================================================
    # 3. UNITS (11 units)
    # =========================================================================
    # h0CJ: Работник (Q)
    wts_updates[7307] = "|cffe4cfa3Работник|r"
    wts_updates[7308] = "|cffe4cfa3Работник|r (|cffffffffQ|r)"
    wts_updates[13417] = (
        "|cffa6afb8ЮНИТ:|cffced4da Основной рабочий Ночнорождённых. Добывает золото и древесину, возводит и чинит сооружения.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДобыча ресурсов|cffced4da: заготовка древесины и золота.|n"
        "- |cffa9c7deРемонт|cffced4da: восстановление прочности повреждённых строений и механизмов.|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: быстрое перемещение на короткую дистанцию.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CJ", "field": "name", "expected": wts_updates[7307]})
    checks_def.append({"type": "unit", "id": "h0CJ", "field": "tip", "expected": wts_updates[7308]})
    checks_def.append({"type": "unit", "id": "h0CJ", "field": "ubertip", "expected": wts_updates[13417]})

    # e013: Шал'дорайская воительница (Q)
    wts_updates[6091] = "|cffe4cfa3Шал'дорайская воительница|r"
    wts_updates[6092] = "|cffe4cfa3Шал'дорайская воительница|r (|cffffffffQ|r)"
    wts_updates[12379] = (
        "|cffa6afb8ЮНИТ:|cffced4da Ловкая воительница ближнего боя. Может обучиться защитной стойке со щитом и усиленным лунным глефам, поражающим нескольких врагов за удар.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУкрыться за щитом|cffced4da: снижает урон от дальних атак за счёт скорости бега.|n"
        "- |cffa9c7deЛунные глефы|cffced4da: глефы отскакивают в дополнительных противников.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e013", "field": "name", "expected": wts_updates[6091]})
    checks_def.append({"type": "unit", "id": "e013", "field": "tip", "expected": wts_updates[6092]})
    checks_def.append({"type": "unit", "id": "e013", "field": "ubertip", "expected": wts_updates[12379]})

    # e014: Наследник Сумеречной стражи (W)
    wts_updates[6170] = "|cffe4cfa3Наследник Сумеречной стражи|r"
    wts_updates[6177] = "|cffe4cfa3Наследник Сумеречной стражи|r (|cffffffffW|r)"
    wts_updates[31709] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлый боевой маг передовой. Защищён зачарованными латами, значительно снижающими весь входящий физический урон.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗачарованный доспех|cffced4da: блокирует |cffffffff15|cffced4da ед. входящего урона от каждой атаки.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e014", "field": "name", "expected": wts_updates[6170]})
    checks_def.append({"type": "unit", "id": "e014", "field": "tip", "expected": wts_updates[6177]})
    checks_def.append({"type": "unit", "id": "e014", "field": "ubertip", "expected": wts_updates[31709]})

    # e015: Шал'дорайский аристократ (Q)
    wts_updates[6704] = "|cffe4cfa3Шал'дорайский аристократ|r"
    wts_updates[6722] = "|cffe4cfa3Шал'дорайский аристократ|r (|cffffffffQ|r)"
    wts_updates[31710] = (
        "|cffa6afb8ЮНИТ:|cffced4da Могущественный чародей дальнего боя. Способен похищать ману у вражеских заклинателей и призывать водяных элементалей.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПохищение маны|cffced4da: перекачивает |cffffffff20|cffced4da ед. маны в сек. у противника.|n"
        "- |cffa9c7deПризыв элементаля воды|cffced4da: вызывает верного водяного духа для поддержки в бою.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e015", "field": "name", "expected": wts_updates[6704]})
    checks_def.append({"type": "unit", "id": "e015", "field": "tip", "expected": wts_updates[6722]})
    checks_def.append({"type": "unit", "id": "e015", "field": "ubertip", "expected": wts_updates[31710]})

    # e016: Шал'дорайский гвардеец (W)
    wts_updates[6751] = "|cffe4cfa3Шал'дорайский гвардеец|r"
    wts_updates[6752] = "|cffe4cfa3Шал'дорайский гвардеец|r (|cffffffffW|r)"
    wts_updates[31711] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный страж ближнего боя. Подавляет заклинания вражеских магов мощным заклятием немоты.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deНемота|cffced4da: лишает противников возможности творить заклинания в выбранной области.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e016", "field": "name", "expected": wts_updates[6751]})
    checks_def.append({"type": "unit", "id": "e016", "field": "tip", "expected": wts_updates[6752]})
    checks_def.append({"type": "unit", "id": "e016", "field": "ubertip", "expected": wts_updates[31711]})

    # e017: Звериный страж (W)
    wts_updates[6784] = "|cffe4cfa3Звериный страж|r"
    wts_updates[6856] = "|cffe4cfa3Звериный страж|r (|cffffffffW|r)"
    wts_updates[31712] = (
        "|cffa6afb8ЮНИТ:|cffced4da Стремительный кавалерист верхом на свирепом сурамарском леопарде. Наносит сокрушительный урон осадным сооружениям и способен опутывать врагов сетью.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРазгром|cffced4da: наносит |cffffffff1.5|cffced4da-кратный урон по зданиям.|n"
        "- |cffa9c7deМагическая сетка|cffced4da: обездвиживает врага и спускает летающих существ на землю.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e017", "field": "name", "expected": wts_updates[6784]})
    checks_def.append({"type": "unit", "id": "e017", "field": "tip", "expected": wts_updates[6856]})
    checks_def.append({"type": "unit", "id": "e017", "field": "ubertip", "expected": wts_updates[31712]})

    # e018: Сумеречный страж (E)
    wts_updates[6906] = "|cffe4cfa3Сумеречный страж|r"
    wts_updates[6910] = "|cffe4cfa3Сумеречный страж|r (|cffffffffE|r)"
    wts_updates[31713] = (
        "|cffa6afb8ЮНИТ:|cffced4da Офицер поддержки Сумеречной стражи. Усиливает урон окружающих союзников командирской аурой и сковывает движения врагов магическими оковами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКомандирская аура|cffced4da: повышает урон находящихся поблизости союзных войск на |cffc8e087+10%|cffced4da.|n"
        "- |cffa9c7deМагические оковы|cffced4da: замедляет скорость атаки и передвижения цели.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e018", "field": "name", "expected": wts_updates[6906]})
    checks_def.append({"type": "unit", "id": "e018", "field": "tip", "expected": wts_updates[6910]})
    checks_def.append({"type": "unit", "id": "e018", "field": "ubertip", "expected": wts_updates[31713]})

    # e019: Темный клинок (Q)
    wts_updates[6969] = "|cffe4cfa3Темный клинок|r"
    wts_updates[6974] = "|cffe4cfa3Темный клинок|r (|cffffffffQ|r)"
    wts_updates[31714] = (
        "|cffa6afb8ЮНИТ:|cffced4da Мастер скрытных убийств. Способен сливаться с тенью и наносить смертоносные рассекающие критические удары.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСлияние с тенью|cffced4da: временно дарует невидимость и повышает скорость перемещения.|n"
        "- |cffa9c7deРассекание|cffced4da: с вероятностью |cffffffff15%|cffced4da наносит |cffffffff5|cffced4da-кратный критический урон.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e019", "field": "name", "expected": wts_updates[6969]})
    checks_def.append({"type": "unit", "id": "e019", "field": "tip", "expected": wts_updates[6974]})
    checks_def.append({"type": "unit", "id": "e019", "field": "ubertip", "expected": wts_updates[31714]})

    # e01A: Лунный маг (W)
    wts_updates[7154] = "|cffe4cfa3Лунный маг|r"
    wts_updates[7155] = "|cffe4cfa3Лунный маг|r (|cffffffffW|r)"
    wts_updates[20879] = (
        "|cffa6afb8ЮНИТ:|cffced4da Высший чародей дальнего боя. Атакует разрушительным уроном хаоса по области, ослабляет броню врагов волшебным огнём и обрушивает на ряды врагов всплески маны.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСфера разрушения|cffced4da: придает атакам рассеивающийся урон хаоса по области и даёт |cffc8e087+20|cffced4da к атаке.|n"
        "- |cffa9c7deВсплеск маны|cffced4da: наносит урон цели и области вокруг неё, замедляя врагов.|n"
        "- |cffa9c7deВолшебный огонь|cffced4da: снижает броню цели на |cffe69a8d-4|cffced4da ед. и раскрывает невидимость.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает урон ценой запаса маны.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01A", "field": "name", "expected": wts_updates[7154]})
    checks_def.append({"type": "unit", "id": "e01A", "field": "tip", "expected": wts_updates[7155]})
    checks_def.append({"type": "unit", "id": "e01A", "field": "ubertip", "expected": wts_updates[20879]})

    # e01B: Глефомет (E)
    wts_updates[7310] = "|cffe4cfa3Глефомет|r"
    wts_updates[7316] = "|cffe4cfa3Глефомет|r (|cffffffffE|r)"
    wts_updates[31718] = (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойное осадное орудие. Эффективно против укреплений и скоплений пехоты. После улучшения способно поражать цели на линии огня стальными снарядами.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСтальной снаряд|cffced4da: снаряды пробивают строй и поражают врагов позади основной цели.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "e01B", "field": "name", "expected": wts_updates[7310]})
    checks_def.append({"type": "unit", "id": "e01B", "field": "tip", "expected": wts_updates[7316]})
    checks_def.append({"type": "unit", "id": "e01B", "field": "ubertip", "expected": wts_updates[31718]})

    # h0CA: Поклонник (Q)
    wts_updates[25787] = "|cffe4cfa3Поклонник|r"
    wts_updates[25794] = "|cffe4cfa3Поклонник|r (|cffffffffQ|r)"
    wts_updates[25795] = (
        "|cffa6afb8ЮНИТ:|cffced4da Искусный маг поддержки и целитель (Темпомант). Исцеляет раненых соратников, рассеивает чары и призывает духов возмездия.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deДар исцеления|cffced4da: восстанавливает |cffc8e08725|cffced4da ед. здоровья союзнику.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает эффекты чар и наносит |cffffffff200|cffced4da ед. урона призванным существам.|n"
        "- |cffa9c7deДух возмездия|cffced4da: призывает мстительного призрака из останков павшего воина.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "h0CA", "field": "name", "expected": wts_updates[25787]})
    checks_def.append({"type": "unit", "id": "h0CA", "field": "tip", "expected": wts_updates[25794]})
    checks_def.append({"type": "unit", "id": "h0CA", "field": "ubertip", "expected": wts_updates[25795]})

    # =========================================================================
    # 4. HEROES (3 heroes)
    # =========================================================================
    # E01E: Капитан Шал'дорайской стражи (Z)
    wts_updates[10086] = "|cffe4cfa3Капитан Шал'дорайской стражи|r"
    wts_updates[10087] = "|cffe4cfa3Квенель|r"
    wts_updates[10280] = "|cffe4cfa3Капитан Шал'дорайской стражи|r (|cffffffffZ|r)"
    wts_updates[25232] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Могучий военачальник ближнего боя. Ведёт войска в атаку, отражает вражеские удары шипами и поддерживает солдат вампирической аурой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗачарованные доспехи|cffced4da: пассивно поглощает урон от заклинаний и магических атак.|n"
        "- |cffa9c7deПризыв леопарда|cffced4da: призывает верных боевых леопардов для сокрушения врагов.|n"
        "- |cffa9c7deШипастая броня|cffced4da: повышает броню и возвращает часть полученного урона атакующим врагам.|n"
        "- |cffa9c7deМагический вампиризм|cffced4da: аура, позволяющая союзникам восстанавливать здоровье при атаке.|n|n"
        "Атакует наземные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "E01E", "field": "name", "expected": wts_updates[10086]})
    checks_def.append({"type": "unit", "id": "E01E", "field": "tip", "expected": wts_updates[10280]})
    checks_def.append({"type": "unit", "id": "E01E", "field": "ubertip", "expected": wts_updates[25232]})

    # E01D: Мрачная Тень (X)
    wts_updates[10083] = "|cffe4cfa3Мрачная Тень|r"
    wts_updates[10082] = "|cffe4cfa3Калеастра|r"
    wts_updates[10279] = "|cffe4cfa3Мрачная Тень|r (|cffffffffX|r)"
    wts_updates[31719] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Непревзойдённая лучница дальнего боя. Лишает магов их энергии, поражает вражеские ряды проклятыми стрелами и вдохновляет союзных стрелков.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПротиводействие|cffced4da: сжигает ману врагов и наносит дополнительный урон.|n"
        "- |cffa9c7deСтрела проклятия|cffced4da: выпускает темную стрелу, поражающую нескольких врагов.|n"
        "- |cffa9c7deАура меткости|cffced4da: увеличивает урон от дистанционных атак находящихся рядом союзников.|n"
        "- |cffa9c7deРазящие стрелы|cffced4da: выпускает град стрел, наносящий колоссальный урон группе врагов.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "E01D", "field": "name", "expected": wts_updates[10083]})
    checks_def.append({"type": "unit", "id": "E01D", "field": "tip", "expected": wts_updates[10279]})
    checks_def.append({"type": "unit", "id": "E01D", "field": "ubertip", "expected": wts_updates[31719]})

    # E01F: Верховный лунный маг (C)
    wts_updates[10090] = "|cffe4cfa3Верховный лунный маг|r"
    wts_updates[10091] = "|cffe4cfa3Авнель|r"
    wts_updates[28308] = "|cffe4cfa3Верховный лунный маг|r (|cffffffffC|r)"
    wts_updates[31721] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Величайший мастер тайной магии Сурамара. Уничтожает скопления противников всплесками маны, защищает себя щитом маны и дарует союзникам неуязвимость.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВсплеск маны|cffced4da: наносит урон цели и расходится разрушительной волной по области.|n"
        "- |cffa9c7deЩит маны|cffced4da: поглощает входящий урон за счёт запаса маны.|n"
        "- |cffa9c7deАура познаний|cffced4da: ускоряет восстановление маны окружающих союзников.|n"
        "- |cffa9c7deЗащита маны|cffced4da: наделяет находящихся рядом союзников полной неуязвимостью.|n|n"
        "Атакует наземные и воздушные цели.|r"
    )
    checks_def.append({"type": "unit", "id": "E01F", "field": "name", "expected": wts_updates[10090]})
    checks_def.append({"type": "unit", "id": "E01F", "field": "tip", "expected": wts_updates[28308]})
    checks_def.append({"type": "unit", "id": "E01F", "field": "ubertip", "expected": wts_updates[31721]})

    # =========================================================================
    # 5. SPECIAL & FACTION ABILITIES
    # =========================================================================
    # A0GL: Дар маны (R)
    wts_updates[7976] = "|cffe4cfa3Дар маны|r"
    wts_updates[7978] = "|cffe4cfa3Дар маны|r (|cffffffffR|r)"
    wts_updates[28372] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Высвобождает прилив энергии Ночного Колодца, повышая урон всех войск Ночнорождённых на карте на |cffc8e087+25%|cffced4da.|n|n"
        "Время действия: |cffffffff45|cffced4da сек.|r"
    )
    checks_def.append({"type": "ability", "id": "A0GL", "field": "name", "expected": wts_updates[7976]})
    checks_def.append({"type": "ability", "id": "A0GL", "field": "tip1", "expected": wts_updates[7978]})
    checks_def.append({"type": "ability", "id": "A0GL", "field": "ubertip1", "expected": wts_updates[28372]})

    # A0GK: Благодать маны (X)
    wts_updates[7963] = "|cffe4cfa3Благодать маны|r"
    wts_updates[7971] = "|cffe4cfa3Благодать маны|r (|cffffffffX|r)"
    wts_updates[39169] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет армию Ночнорождённых благословением Колодца, повышая броню на |cffc8e087+3|cffced4da ед. и урон на |cffc8e087+50%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A0GK", "field": "name", "expected": wts_updates[7963]})
    checks_def.append({"type": "ability", "id": "A0GK", "field": "tip1", "expected": wts_updates[7971]})
    checks_def.append({"type": "ability", "id": "A0GK", "field": "ubertip1", "expected": wts_updates[39169]})

    # =========================================================================
    # 6. UNIT ABILITIES
    # =========================================================================
    # A0GE: Щит маны (D)
    wts_updates[7520] = "|cffe4cfa3Щит маны|r"
    wts_updates[7519] = "|cffe4cfa3Щит маны|r (|cffffffffD|r)"
    wts_updates[2953] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает бойца магическим барьером, поглощающим |cffffffff1|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|r"
    )
    checks_def.append({"type": "ability", "id": "A0GE", "field": "name", "expected": wts_updates[7520]})
    checks_def.append({"type": "ability", "id": "A0GE", "field": "tip1", "expected": wts_updates[7519]})
    checks_def.append({"type": "ability", "id": "A0GE", "field": "ubertip1", "expected": wts_updates[2953]})

    # A0G5: Родство с магией (passive)
    wts_updates[7428] = "|cffe4cfa3Родство с магией|r"
    wts_updates[7427] = "|cffe4cfa3Родство с магией|r"
    wts_updates[11455] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Пассивная защита Ночнорождённых. Снижает получаемый урон от физических атак на |cffc8e08765%|cffced4da и от заклинаний на |cffc8e08780%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A0G5", "field": "name", "expected": wts_updates[7428]})
    checks_def.append({"type": "ability", "id": "A0G5", "field": "tip1", "expected": wts_updates[7427]})
    checks_def.append({"type": "ability", "id": "A0G5", "field": "ubertip1", "expected": wts_updates[11455]})

    # A0G1: Укрыться за щитом (Q)
    wts_updates[970] = "|cffe4cfa3Укрыться за щитом|r"
    wts_updates[7344] = "|cffe4cfa3Укрыться за щитом|r (|cffffffffQ|r)"
    wts_updates[10852] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Защитная стойка. Снижает получаемый урон от дальних атак на |cffc8e08750%|cffced4da, но уменьшает скорость перемещения на |cffe69a8d30%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A0G1", "field": "name", "expected": wts_updates[970]})
    checks_def.append({"type": "ability", "id": "A0G1", "field": "tip1", "expected": wts_updates[7344]})
    checks_def.append({"type": "ability", "id": "A0G1", "field": "ubertip1", "expected": wts_updates[10852]})

    # A0FZ: Лунная глефа (passive)
    wts_updates[7324] = "|cffe4cfa3Лунная глефа|r"
    wts_updates[7325] = "|cffe4cfa3Лунная глефа|r"
    wts_updates[33470] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет глефам Шал'дорайских воительниц отскакивать в дополнительных противников, поражая до |cffffffff3|cffced4da целей за удар.|r"
    )
    checks_def.append({"type": "ability", "id": "A0FZ", "field": "name", "expected": wts_updates[7324]})
    checks_def.append({"type": "ability", "id": "A0FZ", "field": "tip1", "expected": wts_updates[7325]})
    checks_def.append({"type": "ability", "id": "A0FZ", "field": "ubertip1", "expected": wts_updates[33470]})

    # A0G2: Зачарованный доспех (passive)
    wts_updates[9763] = "|cffe4cfa3Зачарованный доспех|r"
    wts_updates[10645] = "|cffe4cfa3Зачарованный доспех|r"
    wts_updates[10856] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает до |cffffffff15|cffced4da ед. физического урона от каждой атаки врага. Минимальный получаемый урон: |cffffffff5|cffced4da ед.|r"
    )
    checks_def.append({"type": "ability", "id": "A0G2", "field": "name", "expected": wts_updates[9763]})
    checks_def.append({"type": "ability", "id": "A0G2", "field": "tip1", "expected": wts_updates[10645]})
    checks_def.append({"type": "ability", "id": "A0G2", "field": "ubertip1", "expected": wts_updates[10856]})

    # A0G4: Призыв элементаля воды (W)
    wts_updates[7406] = "|cffe4cfa3Призыв элементаля воды|r"
    wts_updates[7426] = "|cffe4cfa3Призыв элементаля воды|r (|cffffffffW|r)"
    wts_updates[11644] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает водяного элементаля для огневой поддержки. Элементаль обладает |cffffffff450|cffced4da ед. здоровья и атакой |cffffffff21-29|cffced4da ед.|n|n"
        "Время существования: |cffffffff60|cffced4da сек.|r"
    )
    checks_def.append({"type": "ability", "id": "A0G4", "field": "name", "expected": wts_updates[7406]})
    checks_def.append({"type": "ability", "id": "A0G4", "field": "tip1", "expected": wts_updates[7426]})
    checks_def.append({"type": "ability", "id": "A0G4", "field": "ubertip1", "expected": wts_updates[11644]})

    # A0G6: Похищение маны (Q)
    wts_updates[7429] = "|cffe4cfa3Похищение маны|r"
    wts_updates[7430] = "|cffe4cfa3Похищение маны|r (|cffffffffQ|r)"
    wts_updates[11645] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Перекачивает |cffffffff20|cffced4da ед. маны в сек. из цели в запас мага.|n|n"
        "Время действия: |cffffffff8|cffced4da сек.|r"
    )
    checks_def.append({"type": "ability", "id": "A0G6", "field": "name", "expected": wts_updates[7429]})
    checks_def.append({"type": "ability", "id": "A0G6", "field": "tip1", "expected": wts_updates[7430]})
    checks_def.append({"type": "ability", "id": "A0G6", "field": "ubertip1", "expected": wts_updates[11645]})

    # A0GG: Немота (W)
    wts_updates[7841] = "|cffe4cfa3Немота|r"
    wts_updates[11648] = "|cffe4cfa3Немота|r (|cffffffffW|r)"
    wts_updates[28371] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Лишает врагов в указанной области возможности произносить заклинания.|n|n"
        "Длительность: |cffffffff15|cffced4da сек. (|cffffffff1|cffced4da сек. по героям).|r"
    )
    checks_def.append({"type": "ability", "id": "A0GG", "field": "name", "expected": wts_updates[7841]})
    checks_def.append({"type": "ability", "id": "A0GG", "field": "tip1", "expected": wts_updates[11648]})
    checks_def.append({"type": "ability", "id": "A0GG", "field": "ubertip1", "expected": wts_updates[28371]})

    # A1O9: Разгром (passive)
    wts_updates[28664] = "|cffe4cfa3Разгром|r"
    wts_updates[28686] = "|cffe4cfa3Разгром|r"
    wts_updates[28912] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Свирепый боевой зверь наносит |cffffffff1.5|cffced4da-кратный урон по вражеским строениям.|r"
    )
    checks_def.append({"type": "ability", "id": "A1O9", "field": "name", "expected": wts_updates[28664]})
    checks_def.append({"type": "ability", "id": "A1O9", "field": "tip1", "expected": wts_updates[28686]})
    checks_def.append({"type": "ability", "id": "A1O9", "field": "ubertip1", "expected": wts_updates[28912]})

    # A0GJ: Магическая сетка (Q)
    wts_updates[5130] = "|cffe4cfa3Магическая сетка|r"
    wts_updates[5131] = "|cffe4cfa3Магическая сетка|r (|cffffffffQ|r)"
    wts_updates[106] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Опутывает врага сетью, прижимая к земле и лишая подвижности.|n|n"
        "Длительность: |cffffffff12|cffced4da сек. (|cffffffff3|cffced4da сек. по героям).|r"
    )
    checks_def.append({"type": "ability", "id": "A0GJ", "field": "name", "expected": wts_updates[5130]})
    checks_def.append({"type": "ability", "id": "A0GJ", "field": "tip1", "expected": wts_updates[5131]})
    checks_def.append({"type": "ability", "id": "A0GJ", "field": "ubertip1", "expected": wts_updates[106]})

    # A0GI: Магические оковы (E)
    wts_updates[10659] = "|cffe4cfa3Магические оковы|r"
    wts_updates[23412] = "|cffe4cfa3Магические оковы|r (|cffffffffE|r)"
    wts_updates[10861] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сковывает цель магическими узами, снижая скорость атаки на |cffe69a8d25%|cffced4da и скорость передвижения на |cffe69a8d60%|cffced4da.|n|n"
        "Длительность: |cffffffff60|cffced4da сек. (|cffffffff10|cffced4da сек. по героям).|r"
    )
    checks_def.append({"type": "ability", "id": "A0GI", "field": "name", "expected": wts_updates[10659]})
    checks_def.append({"type": "ability", "id": "A0GI", "field": "tip1", "expected": wts_updates[23412]})
    checks_def.append({"type": "ability", "id": "A0GI", "field": "ubertip1", "expected": wts_updates[10861]})

    # A0GH: Командирская аура (passive)
    wts_updates[7846] = "|cffe4cfa3Командирская аура|r"
    wts_updates[7847] = "|cffe4cfa3Командирская аура|r"
    wts_updates[10963] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон окружающих союзных войск на |cffc8e087+10%|cffced4da.|r"
    )
    checks_def.append({"type": "ability", "id": "A0GH", "field": "name", "expected": wts_updates[7846]})
    checks_def.append({"type": "ability", "id": "A0GH", "field": "tip1", "expected": wts_updates[7847]})
    checks_def.append({"type": "ability", "id": "A0GH", "field": "ubertip1", "expected": wts_updates[10963]})

    # A03C: Слияние с тенью (Q)
    wts_updates[7327] = "|cffe4cfa3Слияние с тенью|r"
    wts_updates[7329] = "|cffe4cfa3Слияние с тенью|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "A03C", "field": "name", "expected": wts_updates[7327]})
    checks_def.append({"type": "ability", "id": "A03C", "field": "tip1", "expected": wts_updates[7329]})

    # A0GF: Рассекание (passive)
    wts_updates[10876] = "|cffe4cfa3Рассекание|r"
    wts_updates[10877] = "|cffe4cfa3Рассекание|r"
    wts_updates[39222] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff15%|cffced4da наносит смертоносный |cffffffff5|cffced4da-кратный критический урон при атаке.|r"
    )
    checks_def.append({"type": "ability", "id": "A0GF", "field": "name", "expected": wts_updates[10876]})
    checks_def.append({"type": "ability", "id": "A0GF", "field": "tip1", "expected": wts_updates[10877]})
    checks_def.append({"type": "ability", "id": "A0GF", "field": "ubertip1", "expected": wts_updates[39222]})

    # A1MO: Сфера разрушения (E)
    wts_updates[28662] = "|cffe4cfa3Сфера разрушения|r"
    wts_updates[39398] = "|cffe4cfa3Сфера разрушения|r (|cffffffffE|r)"
    wts_updates[39399] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает атаку Лунного мага на |cffc8e087+20|cffced4da ед. и наделяет атаки рассеивающимся уроном по области.|r"
    )
    checks_def.append({"type": "ability", "id": "A1MO", "field": "name", "expected": wts_updates[28662]})
    checks_def.append({"type": "ability", "id": "A1MO", "field": "tip1", "expected": wts_updates[39398]})
    checks_def.append({"type": "ability", "id": "A1MO", "field": "ubertip1", "expected": wts_updates[39399]})

    # A0G7: Всплеск маны (Q)
    wts_updates[7467] = "|cffe4cfa3Всплеск маны|r"
    wts_updates[7468] = "|cffe4cfa3Всплеск маны|r (|cffffffffQ|r)"
    wts_updates[10859] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает волну чистой магии, нанося |cffffffff50|cffced4da ед. урона цели и |cffffffff50|cffced4da ед. по области, снижая скорость атаки и перемещения врагов на |cffffffff4|cffced4da сек. (|cffffffff2|cffced4da сек. по героям).|r"
    )
    checks_def.append({"type": "ability", "id": "A0G7", "field": "name", "expected": wts_updates[7467]})
    checks_def.append({"type": "ability", "id": "A0G7", "field": "tip1", "expected": wts_updates[7468]})
    checks_def.append({"type": "ability", "id": "A0G7", "field": "ubertip1", "expected": wts_updates[10859]})

    # A0GA: Волшебный огонь (W)
    wts_updates[10648] = "|cffe4cfa3Волшебный огонь|r"
    wts_updates[7507] = "|cffe4cfa3Волшебный огонь|r (|cffffffffW|r)"
    wts_updates[10860] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает цель мерцающим сиянием, снижая броню на |cffe69a8d-4|cffced4da ед. и лишая невидимости на |cffffffff90|cffced4da сек. (|cffffffff60|cffced4da сек. по героям).|r"
    )
    checks_def.append({"type": "ability", "id": "A0GA", "field": "name", "expected": wts_updates[10648]})
    checks_def.append({"type": "ability", "id": "A0GA", "field": "tip1", "expected": wts_updates[7507]})
    checks_def.append({"type": "ability", "id": "A0GA", "field": "ubertip1", "expected": wts_updates[10860]})

    # A0G3: Стальной снаряд (passive)
    wts_updates[2] = "|cffe4cfa3Стальной снаряд|r"
    wts_updates[10957] = "|cffe4cfa3Стальной снаряд|r"
    wts_updates[11643] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Оснащает глефомет тяжёлыми снарядами, пробивающими строй и поражающими врагов на линии огня позади цели.|r"
    )
    checks_def.append({"type": "ability", "id": "A0G3", "field": "name", "expected": wts_updates[2]})
    checks_def.append({"type": "ability", "id": "A0G3", "field": "tip1", "expected": wts_updates[10957]})
    checks_def.append({"type": "ability", "id": "A0G3", "field": "ubertip1", "expected": wts_updates[11643]})

    # A1RK: Дар Исцеления (Q)
    wts_updates[25798] = "|cffe4cfa3Дар исцеления|r"
    wts_updates[25799] = "|cffe4cfa3Дар исцеления|r (|cffffffffQ|r)"
    wts_updates[10040] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffc8e08725|cffced4da ед. здоровья раненому союзнику. Не действует на неживые объекты и механизмы.|r"
    )
    checks_def.append({"type": "ability", "id": "A1RK", "field": "name", "expected": wts_updates[25798]})
    checks_def.append({"type": "ability", "id": "A1RK", "field": "tip1", "expected": wts_updates[25799]})
    checks_def.append({"type": "ability", "id": "A1RK", "field": "ubertip1", "expected": wts_updates[10040]})

    # A1RJ: Рассеивание заклинаний (Q)
    wts_updates[41599] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[41600] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffQ|r)"
    wts_updates[42076] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Развеивает все положительные и отрицательные магические эффекты в выбранной области, нанося |cffffffff200|cffced4da ед. урона призванным существам.|r"
    )
    checks_def.append({"type": "ability", "id": "A1RJ", "field": "name", "expected": wts_updates[41599]})
    checks_def.append({"type": "ability", "id": "A1RJ", "field": "tip1", "expected": wts_updates[41600]})
    checks_def.append({"type": "ability", "id": "A1RJ", "field": "ubertip1", "expected": wts_updates[42076]})

    # A0I3: Небольшой скачок (C)
    wts_updates[26484] = "|cffe4cfa3Небольшой скачок|r"
    wts_updates[10064] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[10976] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит работника на небольшое расстояние.|r"
    wts_updates[26476] = "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"
    wts_updates[26477] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит работника на небольшое расстояние.|r"
    checks_def.append({"type": "ability", "id": "A0I3", "field": "name", "expected": wts_updates[26484]})
    checks_def.append({"type": "ability", "id": "A0I3", "field": "tip1", "expected": wts_updates[26476]})
    checks_def.append({"type": "ability", "id": "A0I3", "field": "ubertip1", "expected": wts_updates[26477]})

    # =========================================================================
    # 7. HERO ABILITIES
    # =========================================================================
    # Hero E01E - Капитан Шал'дорайской стражи
    # A0GM: Зачарованные доспехи (passive)
    wts_updates[10100] = "|cffe4cfa3Зачарованные доспехи|r"
    wts_updates[10094] = "|cffe4cfa3Зачарованные доспехи|r"
    wts_updates[40021] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Защитная магия доспехов поглощает урон от стрел, заклинаний и магических атак.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da снижает урон от стрел и магии.|n"
        "|cffa6afb8Уровень 2:|cffced4da среднее снижение урона.|n"
        "|cffa6afb8Уровень 3:|cffced4da сильное снижение урона.|n"
        "|cffa6afb8Уровень 4:|cffced4da максимальное снижение урона.|r"
    )
    wts_updates[10095] = "|cffe4cfa3Зачарованные доспехи|r"
    wts_updates[15453] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает урон от стрел, способностей и магических атак.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10097] = "|cffe4cfa3Зачарованные доспехи|r"
    wts_updates[15450] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Среднее поглощение урона от стрел, способностей и магических атак.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10098] = "|cffe4cfa3Зачарованные доспехи|r"
    wts_updates[15451] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сильное поглощение урона от стрел, способностей и магических атак.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10099] = "|cffe4cfa3Зачарованные доспехи|r"
    wts_updates[15452] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Максимальное поглощение урона от стрел, способностей и магических атак.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GM", "field": "name", "expected": wts_updates[10100]})

    # A0GO: Призыв леопарда (Q)
    wts_updates[10110] = "|cffe4cfa3Призыв леопарда|r"
    wts_updates[10128] = "|cffe4cfa3Призыв леопарда|r (|cffffffffQ|r)"
    wts_updates[31715] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает ловких сурамарских боевых леопардов для атаки противников.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da |cffffffff2|cffced4da леопарда.|n"
        "|cffa6afb8Уровень 2:|cffced4da |cffffffff2|cffced4da леопарда с повышенными параметрами.|n"
        "|cffa6afb8Уровень 3:|cffced4da |cffffffff4|cffced4da леопарда.|n"
        "|cffa6afb8Уровень 4:|cffced4da |cffffffff4|cffced4da свирепых леопарда.|r"
    )
    wts_updates[10118] = "|cffe4cfa3Призыв леопарда|r (|cffffffffQ|r)"
    wts_updates[101] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da боевых леопардов.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10119] = "|cffe4cfa3Призыв леопарда|r (|cffffffffQ|r)"
    wts_updates[15455] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da боевых леопарда с повышенными параметрами.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10120] = "|cffe4cfa3Призыв леопарда|r (|cffffffffQ|r)"
    wts_updates[202] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff4|cffced4da боевых леопарда.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10121] = "|cffe4cfa3Призыв леопарда|r (|cffffffffQ|r)"
    wts_updates[15457] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff4|cffced4da свирепых боевых леопарда.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GO", "field": "name", "expected": wts_updates[10110]})

    # A0GT: Шипастая броня (W)
    wts_updates[12940] = "|cffe4cfa3Шипастая броня|r"
    wts_updates[12941] = "|cffe4cfa3Шипастая броня|r (|cffffffffW|r)"
    wts_updates[15459] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает броню героя и отражает часть полученного в ближнем бою урона обратно в атакующих врагов.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da начальное отражение и бонус к броне.|n"
        "|cffa6afb8Уровень 2:|cffced4da умеренное отражение и бонус к броне.|n"
        "|cffa6afb8Уровень 3:|cffced4da высокое отражение и бонус к броне.|n"
        "|cffa6afb8Уровень 4:|cffced4da максимальное отражение и бонус к броне.|r"
    )
    wts_updates[12943] = "|cffe4cfa3Шипастая броня|r (|cffffffffW|r)"
    wts_updates[15460] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню и возвращает часть урона атакующим в ближнем бою врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[12944] = "|cffe4cfa3Шипастая броня|r (|cffffffffW|r)"
    wts_updates[15461] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню и возвращает умеренную часть урона врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[12945] = "|cffe4cfa3Шипастая броня|r (|cffffffffW|r)"
    wts_updates[15462] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню и возвращает значительную часть урона врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[12946] = "|cffe4cfa3Шипастая броня|r (|cffffffffW|r)"
    wts_updates[15463] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню и возвращает максимальную часть урона врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GT", "field": "name", "expected": wts_updates[12940]})

    # A0GU: Магический вампиризм (R)
    wts_updates[10191] = "|cffe4cfa3Магический вампиризм|r"
    wts_updates[10192] = "|cffe4cfa3Магический вампиризм|r (|cffffffffR|r)"
    wts_updates[39406] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Аура вампиризма. Союзные бойцы ближнего боя восполняют здоровье в размере части нанесённого урона.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da |cffffffff35%|cffced4da от нанесённого урона.|n"
        "|cffa6afb8Уровень 2:|cffced4da |cffffffff40%|cffced4da от нанесённого урона.|r"
    )
    wts_updates[10193] = "|cffe4cfa3Магический вампиризм|r (|cffffffffR|r)"
    wts_updates[15465] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье союзников ближнего боя в размере |cffffffff35%|cffced4da от нанесённого урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[10194] = "|cffe4cfa3Магический вампиризм|r (|cffffffffR|r)"
    wts_updates[15466] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье союзников ближнего боя в размере |cffffffff40%|cffced4da от нанесённого урона.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GU", "field": "name", "expected": wts_updates[10191]})

    # Hero E01D - Мрачная Тень
    # A0GS: Противодействие (Q)
    wts_updates[10103] = "|cffe4cfa3Противодействие|r"
    wts_updates[10175] = "|cffe4cfa3Противодействие|r (|cffffffffQ|r)"
    wts_updates[31181] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждая атака сжигает ману цели и наносит дополнительный урон.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da сжигает |cffffffff6|cffced4da ед. у героев, |cffffffff20|cffced4da ед. у воинов.|n"
        "|cffa6afb8Уровень 2:|cffced4da сжигает |cffffffff8|cffced4da ед. у героев, |cffffffff30|cffced4da ед. у воинов.|n"
        "|cffa6afb8Уровень 3:|cffced4da сжигает |cffffffff10|cffced4da ед. у героев, |cffffffff35|cffced4da ед. у воинов.|n"
        "|cffa6afb8Уровень 4:|cffced4da сжигает |cffffffff12|cffced4da ед. у героев, |cffffffff40|cffced4da ед. у воинов.|r"
    )
    wts_updates[10171] = "|cffe4cfa3Противодействие|r (|cffffffffQ|r)"
    wts_updates[31186] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает |cffffffff6|cffced4da ед. маны у героев, |cffffffff20|cffced4da ед. у воинов.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10172] = "|cffe4cfa3Противодействие|r (|cffffffffQ|r)"
    wts_updates[28827] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает |cffffffff8|cffced4da ед. маны у героев, |cffffffff30|cffced4da ед. у воинов.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10173] = "|cffe4cfa3Противодействие|r (|cffffffffQ|r)"
    wts_updates[28828] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает |cffffffff10|cffced4da ед. маны у героев, |cffffffff35|cffced4da ед. у воинов.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10174] = "|cffe4cfa3Противодействие|r (|cffffffffQ|r)"
    wts_updates[31171] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сжигает |cffffffff12|cffced4da ед. маны у героев, |cffffffff40|cffced4da ед. у воинов.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GS", "field": "name", "expected": wts_updates[10103]})

    # A0GV: Стрела проклятия (W)
    wts_updates[10195] = "|cffe4cfa3Стрела проклятия|r"
    wts_updates[10196] = "|cffe4cfa3Стрела проклятия|r (|cffffffffW|r)"
    wts_updates[11111] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает стрелу тёмной энергии, наносящую урон нескольким противникам.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da начальный урон целям.|n"
        "|cffa6afb8Уровень 2:|cffced4da умеренный урон целям.|n"
        "|cffa6afb8Уровень 3:|cffced4da высокий урон целям.|n"
        "|cffa6afb8Уровень 4:|cffced4da сокрушительный урон целям.|r"
    )
    wts_updates[10198] = "|cffe4cfa3Стрела проклятия|r (|cffffffffW|r)"
    wts_updates[11112] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает темную стрелу, поражающую нескольких врагов.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10199] = "|cffe4cfa3Стрела проклятия|r (|cffffffffW|r)"
    wts_updates[11113] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает темную стрелу с умеренным уроном.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10200] = "|cffe4cfa3Стрела проклятия|r (|cffffffffW|r)"
    wts_updates[11114] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает темную стрелу с высоким уроном.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10201] = "|cffe4cfa3Стрела проклятия|r (|cffffffffW|r)"
    wts_updates[11155] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает темную стрелу с максимальным уроном.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GV", "field": "name", "expected": wts_updates[10195]})

    # A0GW: Аура меткости (E)
    wts_updates[10220] = "|cffe4cfa3Аура меткости|r"
    wts_updates[10221] = "|cffe4cfa3Аура меткости|r (|cffffffffE|r)"
    wts_updates[39408] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон дистанционных атак находящихся рядом союзных войск.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da |cffc8e087+10%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 2:|cffced4da |cffc8e087+20%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 3:|cffced4da |cffc8e087+30%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 4:|cffced4da |cffc8e087+40%|cffced4da к урону.|r"
    )
    wts_updates[10222] = "|cffe4cfa3Аура меткости|r (|cffffffffE|r)"
    wts_updates[39409] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон союзных стрелков на |cffc8e087+10%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10223] = "|cffe4cfa3Аура меткости|r (|cffffffffE|r)"
    wts_updates[39410] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон союзных стрелков на |cffc8e087+20%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10224] = "|cffe4cfa3Аура меткости|r (|cffffffffE|r)"
    wts_updates[39411] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон союзных стрелков на |cffc8e087+30%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10218] = "|cffe4cfa3Аура меткости|r (|cffffffffE|r)"
    wts_updates[39407] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает урон союзных стрелков на |cffc8e087+40%|cffced4da.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GW", "field": "name", "expected": wts_updates[10220]})

    # A0GX: Разящие стрелы (R)
    wts_updates[10225] = "|cffe4cfa3Разящие стрелы|r"
    wts_updates[10226] = "|cffe4cfa3Разящие стрелы|r (|cffffffffR|r)"
    wts_updates[556] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Запускает шквал магических стрел, поражающих группу врагов.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da |cffffffff300|cffced4da урона каждой цели (до |cffffffff15|cffced4da целей).|n"
        "|cffa6afb8Уровень 2:|cffced4da |cffffffff500|cffced4da урона каждой цели (до |cffffffff20|cffced4da целей).|r"
    )
    wts_updates[10227] = "|cffe4cfa3Разящие стрелы|r (|cffffffffR|r)"
    wts_updates[39412] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff300|cffced4da урона каждой цели (до |cffffffff15|cffced4da целей).|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[10228] = "|cffe4cfa3Разящие стрелы|r (|cffffffffR|r)"
    wts_updates[39413] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff500|cffced4da урона каждой цели (до |cffffffff20|cffced4da целей).|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GX", "field": "name", "expected": wts_updates[10225]})

    # Hero E01F - Верховный лунный маг
    # A0GN: Всплеск маны (Q)
    wts_updates[7485] = "|cffe4cfa3Всплеск маны|r"
    wts_updates[1780] = "|cffe4cfa3Всплеск маны|r (|cffffffffQ|r)"
    wts_updates[9390] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает заряд тайной магии, нанося урон цели и расходясь взрывом по окружающим врагам.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da начальный урон цели и по области.|n"
        "|cffa6afb8Уровень 2:|cffced4da умеренный урон цели и по области.|n"
        "|cffa6afb8Уровень 3:|cffced4da высокий урон цели и по области.|n"
        "|cffa6afb8Уровень 4:|cffced4da максимальный урон цели и по области.|r"
    )
    wts_updates[10104] = "|cffe4cfa3Всплеск маны|r (|cffffffffQ|r)"
    wts_updates[9391] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит урон цели и окружающим врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10106] = "|cffe4cfa3Всплеск маны|r (|cffffffffQ|r)"
    wts_updates[8403] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит умеренный урон цели и окружающим врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10111] = "|cffe4cfa3Всплеск маны|r (|cffffffffQ|r)"
    wts_updates[9382] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит высокий урон цели и окружающим врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10112] = "|cffe4cfa3Всплеск маны|r (|cffffffffQ|r)"
    wts_updates[9389] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит максимальный урон цели и окружающим врагам.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GN", "field": "name", "expected": wts_updates[7485]})

    # A0GP: Щит маны (W)
    wts_updates[7820] = "|cffe4cfa3Щит маны|r"
    wts_updates[10130] = "|cffe4cfa3Щит маны|r (|cffffffffW|r)"
    wts_updates[39402] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создаёт магический барьер, поглощающий входящий урон за счёт запаса маны мага.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da поглощает |cffffffff3|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|n"
        "|cffa6afb8Уровень 2:|cffced4da поглощает |cffffffff4|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|n"
        "|cffa6afb8Уровень 3:|cffced4da поглощает |cffffffff5|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|n"
        "|cffa6afb8Уровень 4:|cffced4da поглощает |cffffffff6|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|r"
    )
    wts_updates[10131] = "|cffe4cfa3Щит маны|r (|cffffffffW|r)"
    wts_updates[39403] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff3|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10132] = "|cffe4cfa3Щит маны|r (|cffffffffW|r)"
    wts_updates[39404] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff4|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10133] = "|cffe4cfa3Щит маны|r (|cffffffffW|r)"
    wts_updates[39405] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff5|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10134] = "|cffe4cfa3Щит маны|r (|cffffffffW|r)"
    wts_updates[31720] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поглощает |cffffffff6|cffced4da ед. урона за |cffffffff1|cffced4da ед. маны.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GP", "field": "name", "expected": wts_updates[7820]})

    # A0GQ: Аура познаний (E)
    wts_updates[10142] = "|cffe4cfa3Аура познаний|r"
    wts_updates[10143] = "|cffe4cfa3Аура познаний|r (|cffffffffE|r)"
    wts_updates[10109] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет восстановление маны находящихся поблизости союзных войск.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da незначительный бонус к регенерации.|n"
        "|cffa6afb8Уровень 2:|cffced4da средний бонус к регенерации.|n"
        "|cffa6afb8Уровень 3:|cffced4da высокий бонус к регенерации.|n"
        "|cffa6afb8Уровень 4:|cffced4da максимальный бонус к регенерации.|r"
    )
    wts_updates[10144] = "|cffe4cfa3Аура познаний|r (|cffffffffE|r)"
    wts_updates[10126] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Незначительно ускоряет восстановление маны союзников.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/4|cffced4da.|r"
    wts_updates[10145] = "|cffe4cfa3Аура познаний|r (|cffffffffE|r)"
    wts_updates[10187] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Умеренно ускоряет восстановление маны союзников.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/4|cffced4da.|r"
    wts_updates[10146] = "|cffe4cfa3Аура познаний|r (|cffffffffE|r)"
    wts_updates[10188] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Значительно ускоряет восстановление маны союзников.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff3/4|cffced4da.|r"
    wts_updates[10147] = "|cffe4cfa3Аура познаний|r (|cffffffffE|r)"
    wts_updates[10102] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Максимально ускоряет восстановление маны союзников.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff4/4|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GQ", "field": "name", "expected": wts_updates[10142]})

    # A0GR: Защита маны (R)
    wts_updates[10148] = "|cffe4cfa3Защита маны|r"
    wts_updates[10149] = "|cffe4cfa3Защита маны|r (|cffffffffR|r)"
    wts_updates[10189] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наделяет союзников в области вокруг мага полной неуязвимостью к любому урону. Сам чародей остаётся уязвимым.|n|n"
        "|cffa6afb8Уровень 1:|cffced4da длительность |cffffffff15|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|cffced4da длительность |cffffffff30|cffced4da сек.|r"
    )
    wts_updates[10150] = "|cffe4cfa3Защита маны|r (|cffffffffR|r)"
    wts_updates[10190] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует полную неуязвимость союзникам вокруг заклинателя.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff1/2|cffced4da.|r"
    wts_updates[10152] = "|cffe4cfa3Защита маны|r (|cffffffffR|r)"
    wts_updates[10687] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует полную неуязвимость союзникам вокруг заклинателя на длительный срок.|n|n|cffa6afb8Уровень способности:|cffced4da |cffffffff2/2|cffced4da.|r"
    checks_def.append({"type": "ability", "id": "A0GR", "field": "name", "expected": wts_updates[10148]})

    # =========================================================================
    # 8. RESEARCHES (UPGRADES)
    # =========================================================================
    # R0DU: Улучшенные инструменты (6 levels)
    tools_names = [1781, 1782, 1783, 4560, 9326, 15564]
    tools_tips = [22228, 23632, 25260, 25261, 28665, 29062]
    tools_ubs = [21881, 21603, 21604, 21605, 21606, 21880]
    for i in range(6):
        lvl = i + 1
        wts_updates[tools_names[i]] = "|cffe4cfa3Улучшенные инструменты|r"
        wts_updates[tools_tips[i]] = f"|cffe4cfa3Улучшенные инструменты — уровень {lvl}|r (|cffffffffZ|r)"
        wts_updates[tools_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас переносимой работниками древесины на |cffc8e087+5|cffced4da ед.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРаботник|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R0DU", "field": "name1", "expected": wts_updates[1781]})

    # R06U: Зачарование силы (6 levels)
    str_names = [9649, 9650, 9665, 9668, 9667, 9666]
    str_tips = [40842, 40843, 40844, 40847, 40846, 40845]
    str_ubs = [10127, 11421, 11422, 6890, 3521, 8046]
    for i in range(6):
        lvl = i + 1
        wts_updates[str_names[i]] = "|cffe4cfa3Зачарование силы|r"
        wts_updates[str_tips[i]] = f"|cffe4cfa3Зачарование силы — уровень {lvl}|r (|cffffffffQ|r)"
        wts_updates[str_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает силу атаки бойцов Ночнорождённых ближнего боя.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайская воительница|cffced4da|n"
            f"- |cffa9c7deШал'дорайский гвардеец|cffced4da|n"
            f"- |cffa9c7deЗвериный страж|cffced4da|n"
            f"- |cffa9c7deСумеречный страж|cffced4da|n"
            f"- |cffa9c7deТемный клинок|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R06U", "field": "name1", "expected": wts_updates[9649]})

    # R06V: Лунные доспехи (6 levels)
    arm_names = [9946, 9989, 10000, 10006, 10005, 10004]
    arm_tips = [10001, 10002, 10003, 10009, 10008, 10007]
    arm_ubs = [11426, 11427, 11430, 11423, 11424, 11425]
    for i in range(6):
        lvl = i + 1
        wts_updates[arm_names[i]] = "|cffe4cfa3Лунные доспехи|r"
        wts_updates[arm_tips[i]] = f"|cffe4cfa3Лунные доспехи — уровень {lvl}|r (|cffffffffA|r)"
        wts_updates[arm_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает защиту и количество брони бойцов Ночнорождённых ближнего боя.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайская воительница|cffced4da|n"
            f"- |cffa9c7deШал'дорайский гвардеец|cffced4da|n"
            f"- |cffa9c7deЗвериный страж|cffced4da|n"
            f"- |cffa9c7deСумеречный страж|cffced4da|n"
            f"- |cffa9c7deТемный клинок|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R06V", "field": "name1", "expected": wts_updates[9946]})

    # R06W: Прочные доспехи (6 levels)
    rng_arm_names = [10013, 10014, 10015, 10018, 10017, 10016]
    rng_arm_tips = [10019, 10020, 10021, 10024, 10023, 10022]
    rng_arm_ubs = [11443, 11444, 11445, 11440, 11441, 11442]
    for i in range(6):
        lvl = i + 1
        wts_updates[rng_arm_names[i]] = "|cffe4cfa3Прочные доспехи|r"
        wts_updates[rng_arm_tips[i]] = f"|cffe4cfa3Прочные доспехи — уровень {lvl}|r (|cffffffffS|r)"
        wts_updates[rng_arm_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает броню стрелков и заклинателей Ночнорождённых.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайский аристократ|cffced4da|n"
            f"- |cffa9c7deЛунный маг|cffced4da|n"
            f"- |cffa9c7deПоклонник|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R06W", "field": "name1", "expected": wts_updates[10013]})

    # R06X: Магическая атака (6 levels)
    rng_atk_names = [10034, 10035, 10036, 10039, 10038, 10037]
    rng_atk_tips = [40848, 40849, 40850, 40853, 40852, 40851]
    rng_atk_ubs = [11449, 11450, 11451, 11447, 11446, 11448]
    for i in range(6):
        lvl = i + 1
        wts_updates[rng_atk_names[i]] = "|cffe4cfa3Магическая атака|r"
        wts_updates[rng_atk_tips[i]] = f"|cffe4cfa3Магическая атака — уровень {lvl}|r (|cffffffffW|r)"
        wts_updates[rng_atk_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон дальних атак и боевых заклинаний стрелков и магов Ночнорождённых.|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайский аристократ|cffced4da|n"
            f"- |cffa9c7deЛунный маг|cffced4da|n"
            f"- |cffa9c7deПоклонник|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/6|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R06X", "field": "name1", "expected": wts_updates[10034]})

    # R06Y: Родство с маной (3 levels)
    mana_names = [10056, 10061, 10062]
    mana_tips = [40854, 40855, 40856]
    mana_ubs = [11668, 11669, 11670]
    for i in range(3):
        lvl = i + 1
        wts_updates[mana_names[i]] = "|cffe4cfa3Родство с маной|r"
        wts_updates[mana_tips[i]] = f"|cffe4cfa3Родство с маной — уровень {lvl}|r (|cffffffffE|r)"
        extra_desc = " Наделяет всех бойцов способностью «Щит маны»." if lvl == 2 else ""
        wts_updates[mana_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Окружает войска Ночнорождённых магическим барьером, снижая получаемый физический урон на |cffc8e087-65%|cffced4da и магический урон на |cffc8e087-80%|cffced4da.{extra_desc}|n|n"
            f"|cffa6afb8Применяется к:|cffced4da|n- Войска Ночнорождённых.|n|n"
            f"|cffa6afb8Уровень исследования:|cffced4da |cffffffff{lvl}/3|cffced4da.|r"
        )
    checks_def.append({"type": "upgrade", "id": "R06Y", "field": "name1", "expected": wts_updates[10056]})

    # Barracks researches:
    # R06G: Укрыться за щитом (A)
    wts_updates[2975] = "|cffe4cfa3Укрыться за щитом|r"
    wts_updates[40479] = "|cffe4cfa3Укрыться за щитом|r (|cffffffffA|r)"
    wts_updates[7342] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Шал'дорайских воительниц защитной стойке «Укрыться за щитом», снижающей получаемый урон от стрелковых атак.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайская воительница|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06G", "field": "name1", "expected": wts_updates[2975]})

    # R06H: Лунные глефы (Z)
    wts_updates[40553] = "|cffe4cfa3Лунные глефы|r"
    wts_updates[40706] = "|cffe4cfa3Лунные глефы|r (|cffffffffZ|r)"
    wts_updates[211] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает глефы Шал'дорайских воительниц, позволяя им поражать до |cffffffff3|cffced4da целей за удар.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайская воительница|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06H", "field": "name1", "expected": wts_updates[40553]})

    # R06I: Зачарованные доспехи (S)
    wts_updates[10656] = "|cffe4cfa3Зачарованные доспехи|r"
    wts_updates[40712] = "|cffe4cfa3Зачарованные доспехи|r (|cffffffffS|r)"
    wts_updates[40713] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Наследников Сумеречной стражи зачарованными латами, блокирующими |cffffffff15|cffced4da ед. входящего урона от каждой атаки.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНаследник Сумеречной стражи|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06I", "field": "name1", "expected": wts_updates[10656]})

    # R06J: Стальные снаряды (D)
    wts_updates[10964] = "|cffe4cfa3Стальные снаряды|r"
    wts_updates[10965] = "|cffe4cfa3Стальные снаряды|r (|cffffffffD|r)"
    wts_updates[11651] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает глефомёты пробивающими стальными снарядами, поражающими цели на линии огня позади основной цели.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deГлефомет|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06J", "field": "name1", "expected": wts_updates[10964]})

    # Sanctum researches:
    # R06T: Древнее знание (2 levels, S)
    wts_updates[40836] = "|cffe4cfa3Древнее знание|r"
    wts_updates[40837] = "|cffe4cfa3Древнее знание — уровень 1|r (|cffffffffS|r)"
    wts_updates[40838] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Лунного мага способности «Всплеск маны», а также повышает запас маны на |cffc8e087+75|cffced4da ед. и здоровье на |cffc8e087+50|cffced4da ед. всем войскам Ночнорождённых.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛунный маг|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[40839] = "|cffe4cfa3Древнее знание|r"
    wts_updates[40840] = "|cffe4cfa3Древнее знание — уровень 2|r (|cffffffffS|r)"
    wts_updates[40841] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Лунного мага способности «Волшебный огонь», а также дополнительно повышает запас маны на |cffc8e087+75|cffced4da ед. и здоровье на |cffc8e087+50|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЛунный маг|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06T", "field": "name1", "expected": wts_updates[40836]})

    # R06S: Контроль над маной (2 levels, A)
    wts_updates[10862] = "|cffe4cfa3Контроль над маной|r"
    wts_updates[40834] = "|cffe4cfa3Контроль над маной — уровень 1|r (|cffffffffA|r)"
    wts_updates[10864] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Шал'дорайского аристократа способности «Похищение маны» и увеличивает его запас маны на |cffc8e087+50|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайский аристократ|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[10865] = "|cffe4cfa3Контроль над маной|r"
    wts_updates[40835] = "|cffe4cfa3Контроль над маной — уровень 2|r (|cffffffffA|r)"
    wts_updates[10867] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Шал'дорайского аристократа заклинанию «Призыв элементаля воды» и увеличивает его запас маны на |cffc8e087+50|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайский аристократ|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06S", "field": "name1", "expected": wts_updates[10862]})

    # Temple researches:
    # R06K: Посвящение Темпомантов (2 levels, A)
    wts_updates[11652] = "|cffe4cfa3Посвящение Темпомантов|r"
    wts_updates[40716] = "|cffe4cfa3Посвящение Темпомантов — уровень 1|r (|cffffffffA|r)"
    wts_updates[11654] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас маны Поклонника на |cffc8e087+60|cffced4da ед. и скорость её восстановления.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПоклонник|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff1/2|cffced4da.|r"
    )
    wts_updates[11653] = "|cffe4cfa3Посвящение Темпомантов|r"
    wts_updates[40717] = "|cffe4cfa3Посвящение Темпомантов — уровень 2|r (|cffffffffA|r)"
    wts_updates[11657] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно повышает запас маны Поклонника на |cffc8e087+60|cffced4da ед. и усиливает целительную силу.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПоклонник|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|cffced4da |cffffffff2/2|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06K", "field": "name1", "expected": wts_updates[11652]})

    # R06L: Тайная магия (Z)
    wts_updates[8026] = "|cffe4cfa3Тайная магия|r"
    wts_updates[40827] = "|cffe4cfa3Тайная магия|r (|cffffffffZ|r)"
    wts_updates[11659] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Поклонника заклинанию «Рассеивание заклинаний», повышает запас маны на |cffc8e087+60|cffced4da ед. и атаку на |cffc8e087+4|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deПоклонник|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06L", "field": "name1", "expected": wts_updates[8026]})

    # R06M: Магическая сеть (S)
    wts_updates[10627] = "|cffe4cfa3Магическая сеть|r"
    wts_updates[10646] = "|cffe4cfa3Магическая сеть|r (|cffffffffS|r)"
    wts_updates[40828] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Звериного стража способности «Магическая сетка», позволяющей связывать врагов и спускать воздушные цели на землю.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЗвериный страж|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06M", "field": "name1", "expected": wts_updates[10627]})

    # R06N: Совместные тренировки (X)
    wts_updates[8090] = "|cffe4cfa3Совместные тренировки|r"
    wts_updates[40829] = "|cffe4cfa3Совместные тренировки|r (|cffffffffX|r)"
    wts_updates[710] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает боевого леопарда Звериного стража, повышая его скорость атаки на |cffc8e087+20%|cffced4da и скорость передвижения на |cffc8e087+30|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЗвериный страж|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06N", "field": "name1", "expected": wts_updates[8090]})

    # House of Shal'dorei Guard researches:
    # R06P: Мана-броня (S)
    wts_updates[8531] = "|cffe4cfa3Мана-броня|r"
    wts_updates[40831] = "|cffe4cfa3Мана-броня|r (|cffffffffS|r)"
    wts_updates[10649] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Укрепляет защитные доспехи Шал'дорайского гвардейца, повышая показатель брони на |cffc8e087+2|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШал'дорайский гвардеец|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06P", "field": "name1", "expected": wts_updates[8531]})

    # R06O: Рассекающие клинки (A)
    wts_updates[10879] = "|cffe4cfa3Рассекающие клинки|r"
    wts_updates[40830] = "|cffe4cfa3Рассекающие клинки|r (|cffffffffA|r)"
    wts_updates[11660] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Темного клинка мастерству критического удара «Рассекание».|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deТемный клинок|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06O", "field": "name1", "expected": wts_updates[10879]})

    # R06Q: Командирская аура (D)
    wts_updates[8551] = "|cffe4cfa3Командирская аура|r"
    wts_updates[40832] = "|cffe4cfa3Командирская аура|r (|cffffffffD|r)"
    wts_updates[11661] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наделяет Сумеречного стража аурой командира, повышающей атаку окружающих союзных войск на |cffc8e087+10%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный страж|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06Q", "field": "name1", "expected": wts_updates[8551]})

    # R06R: Магические оковы (C)
    wts_updates[23414] = "|cffe4cfa3Магические оковы|r"
    wts_updates[40833] = "|cffe4cfa3Магические оковы|r (|cffffffffC|r)"
    wts_updates[10660] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Сумеречного стража способности «Магические оковы», сковывающей движения врага.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСумеречный страж|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R06R", "field": "name1", "expected": wts_updates[23414]})

    # =========================================================================
    # STYLE VALIDATION
    # =========================================================================
    forbidden_prefixes = [
        "Построить ", "Обучить ", "Нанять ", "Призвать ", "Исследовать ", "Улучшить до "
    ]
    style_violations = []
    color_tag_re = re.compile(r"\|c[0-9a-fA-F]{8}")

    for sid, val in wts_updates.items():
        # 1. Color tag reset check
        has_color = bool(color_tag_re.search(val))
        has_reset = "|r" in val
        if has_color and not has_reset:
            style_violations.append(f"STRING {sid}: opened color tag without any |r reset: {repr(val)}")

        # 2. Malformed hex
        malformed = re.findall(r"\|c[^f\r\n]{1,7}[^0-9a-fA-F]", val)
        if malformed:
            style_violations.append(f"STRING {sid}: potential malformed color tag: {malformed}")

        # 3. Trailing newline
        if val.endswith("|n") or val.endswith("\n") or val.endswith("\r"):
            style_violations.append(f"STRING {sid}: ends with newline: {repr(val[-10:])}")

        # 4. Forbidden command prefixes
        for verb in forbidden_prefixes:
            if verb in val:
                style_violations.append(f"STRING {sid}: contains forbidden command verb '{verb}': {val[:40]}")

    if style_violations:
        print("Style violations found:")
        for sv in style_violations:
            print("  ", sv)
        raise ValueError("Style check failed!")
    print(f"All style invariants passed 100%! Checked {len(wts_updates)} strings.")

    # Save plan JSON
    plan_data = {
        "race": "Nightborne",
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A0HU"],
            "markers": ["R07J"],
            "buildings": [
                "h0CB", "h0CC", "h0CD", "h0CE", "h0CF", "h0CG",
                "h0CH", "h0CI", "h0CK", "h0CL", "h0CM", "h0D8"
            ],
            "units": [
                "h0CJ", "e013", "e014", "e015", "e016", "e017",
                "e018", "e019", "e01A", "e01B", "h0CA"
            ],
            "heroes": ["E01E", "E01D", "E01F"],
            "upgrades": [
                "R07J", "R0DU", "R06U", "R06V", "R06W", "R06X", "R06Y",
                "R06G", "R06H", "R06I", "R06J", "R06T", "R06S",
                "R06K", "R06L", "R06M", "R06N", "R06P", "R06O", "R06Q", "R06R"
            ],
            "abilities": [
                "A0HU", "A0GL", "A0GK", "A0GE", "A0G5", "A0G1", "A0FZ",
                "A0G2", "A0G4", "A0G6", "A0GG", "A1O9", "A0GJ", "A0GI",
                "A0GH", "A03C", "A0GF", "A1MO", "A0G7", "A0GA", "A0G3",
                "A1RK", "A1RJ", "A0I3",
                "A0GM", "A0GO", "A0GT", "A0GU",
                "A0GS", "A0GV", "A0GW", "A0GX",
                "A0GN", "A0GP", "A0GQ", "A0GR"
            ]
        }
    }

    out_file = folder / "nightborne_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {out_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

if __name__ == "__main__":
    main()
