# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Draeneis race (Race 19)."""
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
    # 1. RACE SELECTION & MARKERS: A0HS, R07G
    # =========================================================================
    wts_updates[38873] = "|cffe4cfa3Дренеи|r"
    wts_updates[38874] = "|cffe4cfa3Дренеи|r (|cffffffffX|r)"
    wts_updates[35194] = (
        "|cffa6afb8РАСА:|cffced4da Благородный народ эредаров, бежавший с Аргуса под предводительством пророка Велена и ведомый священным Светом Наару.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor (Яхве)|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deVinerX|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●|cffa6afb8●●●|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«The Burning Crusade»|r|n|n"
        "|cffced4daДренеи — непреклонные защитники Света, отвергшие скверну Пылающего Легиона. Обладая высокими технологиями Аргуса, "
        "силой священных кристаллов и поддержкой Наару, они объединяют под своим знаменем благочестивых паладинов Озарённых и мудрых "
        "изгнанников Сломленных. Их армия опирается на крепкую оборону, исцеляющие чары и разрушительную магию Света.|r"
    )

    checks_def.append({"type": "ability", "id": "A0HS", "field": "name", "expected": wts_updates[38873]})
    checks_def.append({"type": "ability", "id": "A0HS", "field": "tip1", "expected": wts_updates[38874]})
    checks_def.append({"type": "ability", "id": "A0HS", "field": "ubertip1", "expected": wts_updates[35194]})

    # Selection marker: R07G
    wts_updates[10628] = "|cffe4cfa3Дренеи|r"
    wts_updates[10653] = "|cffe4cfa3Дренеи|r"
    wts_updates[20114] = "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Дренеям.|r"

    checks_def.append({"type": "upgrade", "id": "R07G", "field": "name1", "expected": wts_updates[10628]})
    checks_def.append({"type": "upgrade", "id": "R07G", "field": "tip1", "expected": wts_updates[10653]})
    checks_def.append({"type": "upgrade", "id": "R07G", "field": "ubertip1", "expected": wts_updates[20114]})

    # =========================================================================
    # 2. BUILDINGS (12 buildings)
    # =========================================================================
    # h015: Ратуша (Q)
    wts_updates[23144] = "|cffe4cfa3Ратуша|r"
    wts_updates[23148] = "|cffe4cfa3Ратуша|r (|cffffffffQ|r)"
    wts_updates[10181] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Дренеев первой ступени. Обучает работников и служит складом ресурсов.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deИнженер|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЮвелирное мастерство|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deФорт|cffced4da: открывает доступ к передовым сооружениям и войскам Дренеев.|r"
    )
    checks_def.append({"type": "unit", "id": "h015", "field": "name", "expected": wts_updates[23144]})
    checks_def.append({"type": "unit", "id": "h015", "field": "tip", "expected": wts_updates[23148]})
    checks_def.append({"type": "unit", "id": "h015", "field": "ubertip", "expected": wts_updates[10181]})

    # h016: Форт (Z)
    wts_updates[23149] = "|cffe4cfa3Форт|r"
    wts_updates[23150] = "|cffe4cfa3Форт|r (|cffffffffZ|r)"
    wts_updates[10182] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Дренеев второй ступени. Открывает доступ к новым сооружениям и войскам.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deИнженер|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЮвелирное мастерство|cffced4da.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deБастион|cffced4da: открывает доступ к высшим технологиям, войскам Озарённых и Сломленных.|r"
    )
    checks_def.append({"type": "unit", "id": "h016", "field": "name", "expected": wts_updates[23149]})
    checks_def.append({"type": "unit", "id": "h016", "field": "tip", "expected": wts_updates[23150]})
    checks_def.append({"type": "unit", "id": "h016", "field": "ubertip", "expected": wts_updates[10182]})

    # h017: Бастион (Z)
    wts_updates[23151] = "|cffe4cfa3Бастион|r"
    wts_updates[23152] = "|cffe4cfa3Бастион|r (|cffffffffZ|r)"
    wts_updates[10183] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание Дренеев третьей ступени. Открывает доступ к высшим технологиям, элитным силам Озарённых и Сломленных.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deИнженер|cffced4da.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deЮвелирное мастерство|cffced4da|n- |cffa9c7deПривлечь Сломленных|cffced4da|n- |cffa9c7deПосвящение Озаренных|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h017", "field": "name", "expected": wts_updates[23151]})
    checks_def.append({"type": "unit", "id": "h017", "field": "tip", "expected": wts_updates[23152]})
    checks_def.append({"type": "unit", "id": "h017", "field": "ubertip", "expected": wts_updates[10183]})

    # h033: Казармы Аргуса (W) - Name: 23167, Tip: 23168
    wts_updates[23167] = "|cffe4cfa3Казармы Аргуса|r"
    wts_updates[23168] = "|cffe4cfa3Казармы Аргуса|r (|cffffffffW|r)"

    # h055: Мастерская (E)
    wts_updates[23170] = "|cffe4cfa3Мастерская|r"
    wts_updates[23171] = "|cffe4cfa3Мастерская|r (|cffffffffE|r)"
    wts_updates[31659] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Производственное сооружение Дренеев. Исследует улучшения оружия, доспехов и инструментов работников.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deРуническое оружие|cffced4da|n"
        "- |cffa9c7deАпекситовый доспех|cffced4da|n"
        "- |cffa9c7deЗаточенные наконечники|cffced4da|n"
        "- |cffa9c7deУлучшенные инструменты|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h055", "field": "name", "expected": wts_updates[23170]})
    checks_def.append({"type": "unit", "id": "h055", "field": "tip", "expected": wts_updates[23171]})
    checks_def.append({"type": "unit", "id": "h055", "field": "ubertip", "expected": wts_updates[31659]})

    # h056: Чародейский кластер (R)
    wts_updates[23172] = "|cffe4cfa3Чародейский кластер|r"
    wts_updates[23173] = "|cffe4cfa3Чародейский кластер|r (|cffffffffR|r)"
    wts_updates[20564] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Магическое святилище Дренеев. Обучает заклинателей и исследует магические улучшения.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЧароплетница|cffced4da: маг контроля и подавления.|n"
        "- |cffa9c7deЖрец|cffced4da: священник поддержки и защиты.|n"
        "- |cffa9c7deЧародей|cffced4da: боевой маг дальнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deТаинство Магии|cffced4da|n"
        "- |cffa9c7deДар Наару|cffced4da|n"
        "- |cffa9c7deЧародейские познания|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h056", "field": "name", "expected": wts_updates[23172]})
    checks_def.append({"type": "unit", "id": "h056", "field": "tip", "expected": wts_updates[23173]})
    checks_def.append({"type": "unit", "id": "h056", "field": "ubertip", "expected": wts_updates[20564]})

    # h057: Алтарь Наару (S) - Name: 23174, Tip: 23175
    wts_updates[23174] = "|cffe4cfa3Алтарь Наару|r"
    wts_updates[23175] = "|cffe4cfa3Алтарь Наару|r (|cffffffffS|r)"

    # h058: Храм Озаренных (F)
    wts_updates[17256] = "|cffe4cfa3Храм Озаренных|r"
    wts_updates[17257] = "|cffe4cfa3Храм Озаренных|r (|cffffffffF|r)"
    wts_updates[12973] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Священная обитель воинов Света. Обучает элитных бойцов Озарённых и исследует священные улучшения.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deМечник Озаренный|cffced4da: стойкий воин со священным клинком.|n"
        "- |cffa9c7deЖрица Наару|cffced4da: целительница с благословением Света.|n"
        "- |cffa9c7deМаг Озаренный|cffced4da: заклинатель с чарами исцеления и молний.|n"
        "- |cffa9c7deОзаренный Паладин|cffced4da: могучий рыцарь передовой.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deПосвящение Паладина|cffced4da|n"
        "- |cffa9c7deУчение наару|cffced4da|n"
        "- |cffa9c7deИзучение магии|cffced4da|n"
        "- |cffa9c7deОсвящение оружия|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h058", "field": "name", "expected": wts_updates[17256]})
    checks_def.append({"type": "unit", "id": "h058", "field": "tip", "expected": wts_updates[17257]})
    checks_def.append({"type": "unit", "id": "h058", "field": "ubertip", "expected": wts_updates[12973]})

    # h05A: Логово Сломленных (D)
    wts_updates[23176] = "|cffe4cfa3Логово Сломленных|r"
    wts_updates[23177] = "|cffe4cfa3Логово Сломленных|r (|cffffffffD|r)"
    wts_updates[12974] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Убежище изгнанников и Сломленных дренеев. Обучает ловких воинов и шаманов Тени.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deСломленный страж|cffced4da: пехотинец ближнего боя с уклонением.|n"
        "- |cffa9c7deСломленный мастер|cffced4da: стремительный боец с отравленным клинком.|n"
        "- |cffa9c7deСломленный провидец|cffced4da: шаман с молниями и исцеляющим идолом.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deМастерство Пеплоустов|cffced4da|n"
        "- |cffa9c7deМастерство Сломленных|cffced4da|n"
        "- |cffa9c7deМудрость предков|cffced4da|n"
        "- |cffa9c7deМастерство танца ветра|cffced4da|n"
        "- |cffa9c7deОтравленное оружие|cffced4da.|r"
    )
    checks_def.append({"type": "unit", "id": "h05A", "field": "name", "expected": wts_updates[23176]})
    checks_def.append({"type": "unit", "id": "h05A", "field": "tip", "expected": wts_updates[23177]})
    checks_def.append({"type": "unit", "id": "h05A", "field": "ubertip", "expected": wts_updates[12974]})

    # h05B: Сторожевая башня (Z)
    wts_updates[23179] = "|cffe4cfa3Сторожевая башня|r"
    wts_updates[23178] = "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)"
    wts_updates[10725] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Оборонительное сооружение Дренеев. Атакует наземные и воздушные цели стрелами света.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные и воздушные.|r"
    )
    checks_def.append({"type": "unit", "id": "h05B", "field": "name", "expected": wts_updates[23179]})
    checks_def.append({"type": "unit", "id": "h05B", "field": "tip", "expected": wts_updates[23178]})
    checks_def.append({"type": "unit", "id": "h05B", "field": "ubertip", "expected": wts_updates[10725]})

    # h05C: Лазарет (A)
    wts_updates[23180] = "|cffe4cfa3Лазарет|r"
    wts_updates[23181] = "|cffe4cfa3Лазарет|r (|cffffffffA|r)"
    wts_updates[18670] = (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Дренеев продовольствием и приносит регулярный доход.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n"
        "Приносит доход |cffc8e087+40|cffced4da золота каждые |cffffffff25|cffced4da сек.|r"
    )
    checks_def.append({"type": "unit", "id": "h05C", "field": "name", "expected": wts_updates[23180]})
    checks_def.append({"type": "unit", "id": "h05C", "field": "tip", "expected": wts_updates[23181]})
    checks_def.append({"type": "unit", "id": "h05C", "field": "ubertip", "expected": wts_updates[18670]})

    # =========================================================================
    # 3. UNITS (16 units)
    # =========================================================================
    # h012: Инженер (Q)
    wts_updates[22902] = "|cffe4cfa3Инженер|r"
    wts_updates[22980] = "|cffe4cfa3Инженер|r (|cffffffffQ|r)"
    wts_updates[19476] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Дренеев. Добывает золото и древесину, возводит и чинит здания.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРемонт|cffced4da: восстанавливает прочность зданий и механизмов.|n"
        "- |cffa9c7deНебольшой скачок|cffced4da: мгновенно перемещается на короткую дистанцию.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные.|r"
    )
    checks_def.append({"type": "unit", "id": "h012", "field": "name", "expected": wts_updates[22902]})
    checks_def.append({"type": "unit", "id": "h012", "field": "tip", "expected": wts_updates[22980]})
    checks_def.append({"type": "unit", "id": "h012", "field": "ubertip", "expected": wts_updates[19476]})

    # e000: Рангари (W)
    wts_updates[23159] = "|cffe4cfa3Рангари|r"
    wts_updates[23160] = "|cffe4cfa3Рангари|r (|cffffffffW|r)"
    checks_def.append({"type": "unit", "id": "e000", "field": "name", "expected": wts_updates[23159]})
    checks_def.append({"type": "unit", "id": "e000", "field": "tip", "expected": wts_updates[23160]})

    # h01O: Озаренный Паладин (R)
    wts_updates[19484] = "|cffe4cfa3Озаренный Паладин|r"
    wts_updates[10509] = "|cffe4cfa3Озаренный Паладин|r (|cffffffffR|r)"
    checks_def.append({"type": "unit", "id": "h01O", "field": "name", "expected": wts_updates[19484]})
    checks_def.append({"type": "unit", "id": "h01O", "field": "tip", "expected": wts_updates[10509]})

    # h01P: Лазутчик (Q)
    wts_updates[23153] = "|cffe4cfa3Лазутчик|r"
    wts_updates[23154] = "|cffe4cfa3Лазутчик|r (|cffffffffQ|r)"
    wts_updates[31620] = (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый пехотинец Дренеев. Быстрый разведчик ближнего боя, владеющий уклонением.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУскользание|cffced4da: даёт шанс уклониться от физической атаки.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные.|r"
    )
    checks_def.append({"type": "unit", "id": "h01P", "field": "name", "expected": wts_updates[23153]})
    checks_def.append({"type": "unit", "id": "h01P", "field": "tip", "expected": wts_updates[23154]})
    checks_def.append({"type": "unit", "id": "h01P", "field": "ubertip", "expected": wts_updates[31620]})

    # h01Q: Жрец (W)
    wts_updates[23156] = "|cffe4cfa3Жрец|r"
    wts_updates[23157] = "|cffe4cfa3Жрец|r (|cffffffffW|r)"
    wts_updates[15] = (
        "|cffa6afb8ЮНИТ:|cffced4da Священник Дренеев. Поддерживает войска исцелением, рассеиванием чар и благословением Света.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deИсцеление|cffced4da: восстанавливает здоровье раненому союзнику.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает положительные эффекты с врагов и отрицательные с союзников.|n"
        "- |cffa9c7deПламя света|cffced4da: наполняет союзника силой Света.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные и воздушные.|r"
    )
    checks_def.append({"type": "unit", "id": "h01Q", "field": "name", "expected": wts_updates[23156]})
    checks_def.append({"type": "unit", "id": "h01Q", "field": "tip", "expected": wts_updates[23157]})
    checks_def.append({"type": "unit", "id": "h01Q", "field": "ubertip", "expected": wts_updates[15]})

    # h01R: Жрица Наару (W)
    wts_updates[40965] = "|cffe4cfa3Жрица Наару|r"
    wts_updates[3742] = "|cffe4cfa3Жрица Наару|r (|cffffffffW|r)"
    checks_def.append({"type": "unit", "id": "h01R", "field": "name", "expected": wts_updates[40965]})
    checks_def.append({"type": "unit", "id": "h01R", "field": "tip", "expected": wts_updates[3742]})

    # h01S: Всадник на Элекке (E)
    wts_updates[23162] = "|cffe4cfa3Всадник на Элекке|r"
    wts_updates[23163] = "|cffe4cfa3Всадник на Элекке|r (|cffffffffE|r)"
    wts_updates[2439] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлая кавалерия Дренеев. Мощный всадник ближнего боя с высоким запасом здоровья и сокрушительным ударом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deТяжелые удары|cffced4da: наносит повышенный урон по тяжелобронированным целям.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные.|r"
    )
    checks_def.append({"type": "unit", "id": "h01S", "field": "name", "expected": wts_updates[23162]})
    checks_def.append({"type": "unit", "id": "h01S", "field": "tip", "expected": wts_updates[23163]})
    checks_def.append({"type": "unit", "id": "h01S", "field": "ubertip", "expected": wts_updates[2439]})

    # h01T: Маг Озаренный (E)
    wts_updates[9738] = "|cffe4cfa3Маг Озаренный|r"
    wts_updates[25683] = "|cffe4cfa3Маг Озаренный|r (|cffffffffE|r)"
    wts_updates[2440] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный маг поддержки Озарённых. Владеет исцелением, цепными молниями и сглазом.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deИсцеление|cffced4da: восстанавливает здоровье союзнику.|n"
        "- |cffa9c7deЦепная молния|cffced4da: поражает молнией группу врагов.|n"
        "- |cffa9c7deСглаз|cffced4da: временно превращает врага в безобидное существо.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные и воздушные.|r"
    )
    checks_def.append({"type": "unit", "id": "h01T", "field": "name", "expected": wts_updates[9738]})
    checks_def.append({"type": "unit", "id": "h01T", "field": "tip", "expected": wts_updates[25683]})
    checks_def.append({"type": "unit", "id": "h01T", "field": "ubertip", "expected": wts_updates[2440]})

    # h01U: Чароплетница (Q)
    wts_updates[23165] = "|cffe4cfa3Чароплетница|r"
    wts_updates[23166] = "|cffe4cfa3Чароплетница|r (|cffffffffQ|r)"
    wts_updates[2783] = (
        "|cffa6afb8ЮНИТ:|cffced4da Магический боец поддержки Дренеев. Специализируется на контроле вражеских заклинателей и подавлении противников.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deЗамедление|cffced4da: снижает скорость перемещения и атаки цели.|n"
        "- |cffa9c7deПохищение маны|cffced4da: вытягивает запас маны у врага.|n"
        "- |cffa9c7deНемота|cffced4da: запрещает цели применять заклинания.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные и воздушные.|r"
    )
    checks_def.append({"type": "unit", "id": "h01U", "field": "name", "expected": wts_updates[23165]})
    checks_def.append({"type": "unit", "id": "h01U", "field": "tip", "expected": wts_updates[23166]})
    checks_def.append({"type": "unit", "id": "h01U", "field": "ubertip", "expected": wts_updates[2783]})

    # h059: Мечник Озаренный (Q)
    wts_updates[25827] = "|cffe4cfa3Мечник Озаренный|r"
    wts_updates[25828] = "|cffe4cfa3Мечник Озаренный|r (|cffffffffQ|r)"
    checks_def.append({"type": "unit", "id": "h059", "field": "name", "expected": wts_updates[25827]})
    checks_def.append({"type": "unit", "id": "h059", "field": "tip", "expected": wts_updates[25828]})

    # h05D: Сломленный страж (Q)
    wts_updates[3628] = "|cffe4cfa3Сломленный страж|r"
    wts_updates[3704] = "|cffe4cfa3Сломленный страж|r (|cffffffffQ|r)"
    wts_updates[21866] = (
        "|cffa6afb8ЮНИТ:|cffced4da Скрытный боец Сломленных ближнего боя. Владеет уклонением и способен избежать гибели в тени.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deУскользание|cffced4da: даёт шанс уклониться от атаки.|n"
        "- |cffa9c7deСпасение в тени|cffced4da: при гибели может возродиться у логова Сломленных.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные.|r"
    )
    checks_def.append({"type": "unit", "id": "h05D", "field": "name", "expected": wts_updates[3628]})
    checks_def.append({"type": "unit", "id": "h05D", "field": "tip", "expected": wts_updates[3704]})
    checks_def.append({"type": "unit", "id": "h05D", "field": "ubertip", "expected": wts_updates[21866]})

    # h05E: Сломленный мастер (W)
    wts_updates[17266] = "|cffe4cfa3Сломленный мастер|r"
    wts_updates[3705] = "|cffe4cfa3Сломленный мастер|r (|cffffffffW|r)"
    wts_updates[21867] = (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный боец Сломленных ближнего боя. Быстро сближается с противником, нанося круговые и ядовитые удары.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСтремительное приближение|cffced4da: быстрый рывок к цели.|n"
        "- |cffa9c7deРассекающий удар|cffced4da: наносит урон окружающим врагам.|n"
        "- |cffa9c7deОтравленное оружие|cffced4da: поражает цель ядом.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные.|r"
    )
    checks_def.append({"type": "unit", "id": "h05E", "field": "name", "expected": wts_updates[17266]})
    checks_def.append({"type": "unit", "id": "h05E", "field": "tip", "expected": wts_updates[3705]})
    checks_def.append({"type": "unit", "id": "h05E", "field": "ubertip", "expected": wts_updates[21867]})

    # n005: Сломленный провидец (E)
    wts_updates[3632] = "|cffe4cfa3Сломленный провидец|r"
    wts_updates[3633] = "|cffe4cfa3Сломленный провидец|r (|cffffffffE|r)"
    checks_def.append({"type": "unit", "id": "n005", "field": "name", "expected": wts_updates[3632]})
    checks_def.append({"type": "unit", "id": "n005", "field": "tip", "expected": wts_updates[3633]})

    # o00H: Осадная машина (R)
    wts_updates[12375] = "|cffe4cfa3Осадная машина|r"
    wts_updates[12376] = "|cffe4cfa3Осадная машина|r (|cffffffffR|r)"
    wts_updates[9320] = (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжёлое осадное орудие Дренеев дальнего боя. Наносит высокий урон зданиям и укреплениям врага.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные здания и войска.|r"
    )
    checks_def.append({"type": "unit", "id": "o00H", "field": "name", "expected": wts_updates[12375]})
    checks_def.append({"type": "unit", "id": "o00H", "field": "tip", "expected": wts_updates[12376]})
    checks_def.append({"type": "unit", "id": "o00H", "field": "ubertip", "expected": wts_updates[9320]})

    # n00P: Чародей (E)
    wts_updates[2745] = "|cffe4cfa3Чародей|r"
    wts_updates[4477] = "|cffe4cfa3Чародей|r (|cffffffffE|r)"
    wts_updates[15390] = (
        "|cffa6afb8ЮНИТ:|cffced4da Боевой заклинатель Дренеев дальнего боя. Владеет магической атакой и способен повергнуть союзников в ярость.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deБезумие|cffced4da: увеличивает скорость атаки выбранного союзника ценой потери здоровья.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные и воздушные.|r"
    )
    checks_def.append({"type": "unit", "id": "n00P", "field": "name", "expected": wts_updates[2745]})
    checks_def.append({"type": "unit", "id": "n00P", "field": "tip", "expected": wts_updates[4477]})
    checks_def.append({"type": "unit", "id": "n00P", "field": "ubertip", "expected": wts_updates[15390]})

    # =========================================================================
    # 4. HEROES (4 heroes)
    # =========================================================================
    # H05K: Дреней Паладин (E)
    wts_updates[4316] = "|cffe4cfa3Дреней Паладин|r"
    wts_updates[4317] = "Мараад,Нобундо,Ирель,Барос Алекстон,Виндикатор Борос,Аргус,Карабор,Велен"
    wts_updates[4319] = "|cffe4cfa3Дреней Паладин|r (|cffffffffE|r)"
    wts_updates[31663] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Несокрушимый защитник Света и борец с Легионом. Обладает мощной защитой, целительной силой и священным молотом правосудия.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deВолна исцеления|cffced4da: исцеляет цепочку раненых союзников.|n"
        "- |cffa9c7deБлагодать|cffced4da: дарует неуязвимость окружающим союзникам.|n"
        "- |cffa9c7deАура Доблести|cffced4da: увеличивает урон находящихся рядом союзников.|n"
        "- |cffa9c7deСокрушение|cffced4da: даёт шанс нанести дополнительный урон по площади.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные.|r"
    )
    checks_def.append({"type": "unit", "id": "H05K", "field": "name", "expected": wts_updates[4316]})
    checks_def.append({"type": "unit", "id": "H05K", "field": "propernames", "expected": wts_updates[4317]})
    checks_def.append({"type": "unit", "id": "H05K", "field": "tip", "expected": wts_updates[4319]})
    checks_def.append({"type": "unit", "id": "H05K", "field": "ubertip", "expected": wts_updates[31663]})

    # H05L: Капитан Гвардии (W)
    wts_updates[4391] = "|cffe4cfa3Капитан Гвардии|r"
    wts_updates[4393] = "|cffe4cfa3Капитан Гвардии|r (|cffffffffW|r)"
    wts_updates[31664] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Непревзойдённый воин ближнего боя и военачальник стражи Дренеев. Сочетает фехтовальное мастерство и священный гнев.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deКара света|cffced4da: пассивно наносит урон окружающим противникам вспышками Света.|n"
        "- |cffa9c7deИдеальный Удар|cffced4da: наносит мощный удар и оглушает цель.|n"
        "- |cffa9c7deУдачливость|cffced4da: даёт шанс уклониться от ударов и нанести критический урон.|n"
        "- |cffa9c7deСвященная кара|cffced4da: поражает волной света цель и окружающих врагов.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные.|r"
    )
    checks_def.append({"type": "unit", "id": "H05L", "field": "name", "expected": wts_updates[4391]})
    checks_def.append({"type": "unit", "id": "H05L", "field": "tip", "expected": wts_updates[4393]})
    checks_def.append({"type": "unit", "id": "H05L", "field": "ubertip", "expected": wts_updates[31664]})

    # H05M: Пророк Сломленных (Q)
    wts_updates[4433] = "|cffe4cfa3Пророк Сломленных|r"
    wts_updates[4435] = "|cffe4cfa3Пророк Сломленных|r (|cffffffffQ|r)"
    wts_updates[31665] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Духовный вождь изгнанников, овладевший стихиями и шаманскими силами. Способен призывать ледяные бури и защищать соратников силой природы.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deСнежная буря|cffced4da: обрушивает ледяные осколки на область.|n"
        "- |cffa9c7deЗов помощи|cffced4da: призывает союзных бойцов дренеев.|n"
        "- |cffa9c7deВнушение|cffced4da: ускоряет союзников и усиливает их восстановление.|n"
        "- |cffa9c7deСпокойствие|cffced4da: непрерывно исцеляет всех союзников вокруг.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные и воздушные.|r"
    )
    checks_def.append({"type": "unit", "id": "H05M", "field": "name", "expected": wts_updates[4433]})
    checks_def.append({"type": "unit", "id": "H05M", "field": "tip", "expected": wts_updates[4435]})
    checks_def.append({"type": "unit", "id": "H05M", "field": "ubertip", "expected": wts_updates[31665]})

    # H0MI: Наару (Z)
    wts_updates[20071] = "|cffe4cfa3Наару|r"
    wts_updates[22531] = "А'дал"
    wts_updates[30152] = "|cffe4cfa3Наару|r (|cffffffffZ|r)"
    wts_updates[30207] = (
        "|cffa6afb8ГЕРОЙ:|cffced4da Легендарное существо из чистой энергии Света, лидер Ша'тар и защитник Шаттрата. Обладает неисчерпаемой мощью исцеления и священной защиты.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Спасения|cffced4da: ослабляет броню врагов и предотвращает гибель союзников.|n"
        "- |cffa9c7deМассовое исцеление|cffced4da: восполняет здоровье окружающим соратникам.|n"
        "- |cffa9c7deБлагословление|cffced4da: дарует божественный щит союзникам вокруг.|n"
        "- |cffa9c7deВоскрешение|cffced4da: возвращает к жизни павших союзных воинов.|n|n"
        "|cffa6afb8Цели атаки:|cffced4da наземные и воздушные.|r"
    )
    checks_def.append({"type": "unit", "id": "H0MI", "field": "name", "expected": wts_updates[20071]})
    checks_def.append({"type": "unit", "id": "H0MI", "field": "propernames", "expected": wts_updates[22531]})
    checks_def.append({"type": "unit", "id": "H0MI", "field": "tip", "expected": wts_updates[30152]})
    checks_def.append({"type": "unit", "id": "H0MI", "field": "ubertip", "expected": wts_updates[30207]})

    # =========================================================================
    # 5. HERO ABILITIES
    # =========================================================================
    # AOhw: Волна исцеления (Q)
    wts_updates[28015] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создает волну энергии, восстанавливающую здоровье цели и переходящую к ближайшим союзникам.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff130|cffced4da ед., до |cffffffff3|cffced4da целей.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff205|cffced4da ед., до |cffffffff4|cffced4da целей.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff280|cffced4da ед., до |cffffffff5|cffced4da целей.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff385|cffced4da ед., до |cffffffff20|cffced4da целей.|r"
    )
    wts_updates[63] = "|cffe4cfa3Волна исцеления|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[627] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff130|cffced4da ед. здоровья цели и переходит к |cffffffff3|cffced4da союзникам.|r"
    wts_updates[628] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff205|cffced4da ед. здоровья цели и переходит к |cffffffff4|cffced4da союзникам.|r"
    wts_updates[4411] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff280|cffced4da ед. здоровья цели и переходит к |cffffffff5|cffced4da союзникам.|r"
    wts_updates[28014] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff385|cffced4da ед. здоровья цели и переходит к |cffffffff20|cffced4da союзникам.|r"

    checks_def.append({"type": "ability", "id": "AOhw", "field": "researchubertip", "expected": wts_updates[28015]})
    checks_def.append({"type": "ability", "id": "AOhw", "field": "tip4", "expected": wts_updates[63]})
    checks_def.append({"type": "ability", "id": "AOhw", "field": "ubertip1", "expected": wts_updates[627]})
    checks_def.append({"type": "ability", "id": "AOhw", "field": "ubertip2", "expected": wts_updates[628]})
    checks_def.append({"type": "ability", "id": "AOhw", "field": "ubertip3", "expected": wts_updates[4411]})
    checks_def.append({"type": "ability", "id": "AOhw", "field": "ubertip4", "expected": wts_updates[28014]})

    # A06C: Благодать (R)
    wts_updates[4380] = "|cffe4cfa3Благодать|r"
    wts_updates[4381] = "|cffe4cfa3Благодать|r (|cffffffffR|r)"
    wts_updates[5843] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует неуязвимость окружающим союзникам. Сам паладин остаётся уязвимым.|n|n"
        "|cffa6afb8Уровень 1:|r длительность |cffffffff30|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|r длительность |cffffffff40|cffced4da сек.|r"
    )
    wts_updates[4384] = "|cffe4cfa3Благодать|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[4385] = "|cffe4cfa3Благодать|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[5861] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует неуязвимость окружающим союзникам на |cffffffff30|cffced4da сек.|r"
    wts_updates[5844] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует неуязвимость окружающим союзникам на |cffffffff40|cffced4da сек.|r"

    checks_def.append({"type": "ability", "id": "A06C", "field": "name", "expected": wts_updates[4380]})
    checks_def.append({"type": "ability", "id": "A06C", "field": "researchtip", "expected": wts_updates[4381]})
    checks_def.append({"type": "ability", "id": "A06C", "field": "researchubertip", "expected": wts_updates[5843]})
    checks_def.append({"type": "ability", "id": "A06C", "field": "tip1", "expected": wts_updates[4384]})
    checks_def.append({"type": "ability", "id": "A06C", "field": "tip2", "expected": wts_updates[4385]})
    checks_def.append({"type": "ability", "id": "A06C", "field": "ubertip1", "expected": wts_updates[5861]})
    checks_def.append({"type": "ability", "id": "A06C", "field": "ubertip2", "expected": wts_updates[5844]})

    # A068: Аура Доблести (E)
    wts_updates[4321] = "|cffe4cfa3Аура Доблести|r"
    wts_updates[4323] = "|cffe4cfa3Аура Доблести|r (|cffffffffE|r)"
    wts_updates[8176] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон от атак находящихся рядом союзников.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+10%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+20%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+30%|cffced4da к урону.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+40%|cffced4da к урону.|r"
    )
    wts_updates[4322] = "|cffe4cfa3Аура Доблести|r [|cffffffff1|r]"
    wts_updates[4325] = "|cffe4cfa3Аура Доблести|r [|cffffffff2|r]"
    wts_updates[4326] = "|cffe4cfa3Аура Доблести|r [|cffffffff3|r]"
    wts_updates[4327] = "|cffe4cfa3Аура Доблести|r [|cffffffff4|r]"
    wts_updates[4324] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзников на |cffc8e087+20%|cffced4da.|r"
    wts_updates[4328] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзников на |cffc8e087+30%|cffced4da.|r"
    wts_updates[4329] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает урон союзников на |cffc8e087+40%|cffced4da.|r"

    checks_def.append({"type": "ability", "id": "A068", "field": "name", "expected": wts_updates[4321]})
    checks_def.append({"type": "ability", "id": "A068", "field": "researchtip", "expected": wts_updates[4323]})
    checks_def.append({"type": "ability", "id": "A068", "field": "researchubertip", "expected": wts_updates[8176]})
    checks_def.append({"type": "ability", "id": "A068", "field": "tip1", "expected": wts_updates[4322]})
    checks_def.append({"type": "ability", "id": "A068", "field": "tip2", "expected": wts_updates[4325]})
    checks_def.append({"type": "ability", "id": "A068", "field": "tip3", "expected": wts_updates[4326]})
    checks_def.append({"type": "ability", "id": "A068", "field": "tip4", "expected": wts_updates[4327]})
    checks_def.append({"type": "ability", "id": "A068", "field": "ubertip2", "expected": wts_updates[4324]})
    checks_def.append({"type": "ability", "id": "A068", "field": "ubertip3", "expected": wts_updates[4328]})
    checks_def.append({"type": "ability", "id": "A068", "field": "ubertip4", "expected": wts_updates[4329]})

    # A069: Сокрушение (Q)
    wts_updates[4346] = "|cffe4cfa3Сокрушение|r"
    wts_updates[4347] = "|cffe4cfa3Сокрушение|r (|cffffffffQ|r)"
    wts_updates[25661] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс нанести дополнительный урон окружающим войскам при атаке.|n|n"
        "|cffa6afb8Уровень 1:|r шанс |cffffffff15%|cffced4da, |cffffffff80|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 2:|r шанс |cffffffff20%|cffced4da, |cffffffff100|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 3:|r шанс |cffffffff25%|cffced4da, |cffffffff150|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 4:|r шанс |cffffffff30%|cffced4da, |cffffffff180|cffced4da ед. урона.|r"
    )
    wts_updates[4339] = "|cffe4cfa3Сокрушение|r [|cffffffff1|r]"
    wts_updates[4340] = "|cffe4cfa3Сокрушение|r [|cffffffff2|r]"
    wts_updates[4341] = "|cffe4cfa3Сокрушение|r [|cffffffff3|r]"
    wts_updates[4342] = "|cffe4cfa3Сокрушение|r [|cffffffff4|r]"
    wts_updates[25662] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При атаке с шансом |cffffffff15%|cffced4da наносит |cffffffff80|cffced4da ед. урона по площади.|r"
    wts_updates[25663] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При атаке с шансом |cffffffff20%|cffced4da наносит |cffffffff100|cffced4da ед. урона по площади.|r"
    wts_updates[25654] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При атаке с шансом |cffffffff25%|cffced4da наносит |cffffffff150|cffced4da ед. урона по площади.|r"
    wts_updates[25655] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При атаке с шансом |cffffffff30%|cffced4da наносит |cffffffff180|cffced4da ед. урона по площади.|r"

    checks_def.append({"type": "ability", "id": "A069", "field": "name", "expected": wts_updates[4346]})
    checks_def.append({"type": "ability", "id": "A069", "field": "researchtip", "expected": wts_updates[4347]})
    checks_def.append({"type": "ability", "id": "A069", "field": "researchubertip", "expected": wts_updates[25661]})
    checks_def.append({"type": "ability", "id": "A069", "field": "tip1", "expected": wts_updates[4339]})
    checks_def.append({"type": "ability", "id": "A069", "field": "tip2", "expected": wts_updates[4340]})
    checks_def.append({"type": "ability", "id": "A069", "field": "tip3", "expected": wts_updates[4341]})
    checks_def.append({"type": "ability", "id": "A069", "field": "tip4", "expected": wts_updates[4342]})
    checks_def.append({"type": "ability", "id": "A069", "field": "ubertip1", "expected": wts_updates[25662]})
    checks_def.append({"type": "ability", "id": "A069", "field": "ubertip2", "expected": wts_updates[25663]})
    checks_def.append({"type": "ability", "id": "A069", "field": "ubertip3", "expected": wts_updates[25654]})
    checks_def.append({"type": "ability", "id": "A069", "field": "ubertip4", "expected": wts_updates[25655]})

    # A0Z0: Кара света (пассивная)
    wts_updates[26659] = "|cffe4cfa3Кара света|r"
    wts_updates[26658] = "|cffe4cfa3Кара света|r"
    wts_updates[7585] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обрушивает вспышки Света на врагов вокруг героя, нанося урон раз в несколько секунд.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff50|cffced4da ед. урона раз в |cffffffff4|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff80|cffced4da ед. урона раз в |cffffffff3.5|cffced4da сек.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff100|cffced4da ед. урона раз в |cffffffff3|cffced4da сек.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff120|cffced4da ед. урона раз в |cffffffff2|cffced4da сек.|r"
    )
    wts_updates[26373] = "|cffe4cfa3Кара света|r [|cffffffff1|r]"
    wts_updates[26408] = "|cffe4cfa3Кара света|r [|cffffffff2|r]"
    wts_updates[26411] = "|cffe4cfa3Кара света|r [|cffffffff3|r]"
    wts_updates[26468] = "|cffe4cfa3Кара света|r [|cffffffff4|r]"
    wts_updates[26661] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff50|cffced4da ед. урона врагам вокруг раз в |cffffffff4|cffced4da сек.|r"
    wts_updates[26662] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff80|cffced4da ед. урона врагам вокруг раз в |cffffffff3.5|cffced4da сек.|r"
    wts_updates[26663] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff100|cffced4da ед. урона врагам вокруг раз в |cffffffff3|cffced4da сек.|r"
    wts_updates[26664] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff120|cffced4da ед. урона врагам вокруг раз в |cffffffff2|cffced4da сек.|r"

    checks_def.append({"type": "ability", "id": "A0Z0", "field": "name", "expected": wts_updates[26659]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "researchtip", "expected": wts_updates[26658]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "researchubertip", "expected": wts_updates[7585]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "tip1", "expected": wts_updates[26373]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "tip2", "expected": wts_updates[26408]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "tip3", "expected": wts_updates[26411]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "tip4", "expected": wts_updates[26468]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "ubertip1", "expected": wts_updates[26661]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "ubertip2", "expected": wts_updates[26662]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "ubertip3", "expected": wts_updates[26663]})
    checks_def.append({"type": "ability", "id": "A0Z0", "field": "ubertip4", "expected": wts_updates[26664]})

    # A06F: Идеальный Удар (B)
    wts_updates[4427] = "|cffe4cfa3Идеальный Удар|r"
    wts_updates[4428] = "|cffe4cfa3Идеальный Удар|r (|cffffffffB|r)"
    wts_updates[3615] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит мощный удар в ближнем бою, нанося урон и оглушая цель.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff100|cffced4da ед. урона, оглушение |cffffffff2|cffced4da сек.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff200|cffced4da ед. урона, оглушение |cffffffff3|cffced4da сек.|r"
    )
    wts_updates[4429] = "|cffe4cfa3Идеальный Удар|r [|cffffffff1|r]"
    wts_updates[4430] = "|cffe4cfa3Идеальный Удар|r [|cffffffff2|r]"
    wts_updates[3658] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff100|cffced4da ед. урона цели и оглушает её на |cffffffff2|cffced4da сек.|r"
    wts_updates[5830] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff200|cffced4da ед. урона цели и оглушает её на |cffffffff3|cffced4da сек.|r"

    checks_def.append({"type": "ability", "id": "A06F", "field": "name", "expected": wts_updates[4427]})
    checks_def.append({"type": "ability", "id": "A06F", "field": "researchtip", "expected": wts_updates[4428]})
    checks_def.append({"type": "ability", "id": "A06F", "field": "researchubertip", "expected": wts_updates[3615]})
    checks_def.append({"type": "ability", "id": "A06F", "field": "tip1", "expected": wts_updates[4429]})
    checks_def.append({"type": "ability", "id": "A06F", "field": "tip2", "expected": wts_updates[4430]})
    checks_def.append({"type": "ability", "id": "A06F", "field": "ubertip1", "expected": wts_updates[3658]})
    checks_def.append({"type": "ability", "id": "A06F", "field": "ubertip2", "expected": wts_updates[5830]})

    # A06E: Удачливость (E)
    wts_updates[4420] = "|cffe4cfa3Удачливость|r"
    wts_updates[4421] = "|cffe4cfa3Удачливость|r (|cffffffffE|r)"
    wts_updates[3557] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс уклониться от ударов противника и нанести критический урон.|n|n"
        "|cffa6afb8Уровень 1:|r шанс |cffffffff10%|cffced4da.|n"
        "|cffa6afb8Уровень 2:|r шанс |cffffffff15%|cffced4da.|n"
        "|cffa6afb8Уровень 3:|r шанс |cffffffff20%|cffced4da.|n"
        "|cffa6afb8Уровень 4:|r шанс |cffffffff25%|cffced4da.|r"
    )
    wts_updates[4422] = "|cffe4cfa3Удачливость|r [|cffffffff1|r]"
    wts_updates[4423] = "|cffe4cfa3Удачливость|r [|cffffffff2|r]"
    wts_updates[4424] = "|cffe4cfa3Удачливость|r [|cffffffff3|r]"
    wts_updates[4425] = "|cffe4cfa3Удачливость|r [|cffffffff4|r]"
    wts_updates[4426] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует шанс |cffffffff25%|cffced4da уклониться от ударов или нанести критический урон.|r"

    checks_def.append({"type": "ability", "id": "A06E", "field": "name", "expected": wts_updates[4420]})
    checks_def.append({"type": "ability", "id": "A06E", "field": "researchtip", "expected": wts_updates[4421]})
    checks_def.append({"type": "ability", "id": "A06E", "field": "researchubertip", "expected": wts_updates[3557]})
    checks_def.append({"type": "ability", "id": "A06E", "field": "tip1", "expected": wts_updates[4422]})
    checks_def.append({"type": "ability", "id": "A06E", "field": "tip2", "expected": wts_updates[4423]})
    checks_def.append({"type": "ability", "id": "A06E", "field": "tip3", "expected": wts_updates[4424]})
    checks_def.append({"type": "ability", "id": "A06E", "field": "tip4", "expected": wts_updates[4425]})
    checks_def.append({"type": "ability", "id": "A06E", "field": "ubertip4", "expected": wts_updates[4426]})

    # A06A: Священная кара (Q)
    wts_updates[7583] = "|cffe4cfa3Священная кара|r"
    wts_updates[4396] = "|cffe4cfa3Священная кара|r (|cffffffffQ|r)"
    wts_updates[31512] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает цель и врагов вокруг волной святой энергии.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff100|cffced4da ед. цели, |cffffffff50|cffced4da по области.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff150|cffced4da ед. цели, |cffffffff100|cffced4da по области.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff200|cffced4da ед. цели, |cffffffff150|cffced4da по области.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff350|cffced4da ед. цели, |cffffffff200|cffced4da по области.|r"
    )
    wts_updates[4397] = "|cffe4cfa3Священная кара|r [|cffffffff1|r] (|cffffffffQ|r)"
    wts_updates[4398] = "|cffe4cfa3Священная кара|r [|cffffffff2|r] (|cffffffffQ|r)"
    wts_updates[4399] = "|cffe4cfa3Священная кара|r [|cffffffff3|r] (|cffffffffQ|r)"
    wts_updates[4400] = "|cffe4cfa3Священная кара|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[2177] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff100|cffced4da ед. цели и |cffffffff50|cffced4da ед. врагам по области.|r"
    wts_updates[889] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff150|cffced4da ед. цели и |cffffffff100|cffced4da ед. врагам по области.|r"
    wts_updates[1010] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff200|cffced4da ед. цели и |cffffffff150|cffced4da ед. врагам по области.|r"
    wts_updates[1281] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит |cffffffff350|cffced4da ед. цели и |cffffffff200|cffced4da ед. врагам по области.|r"

    checks_def.append({"type": "ability", "id": "A06A", "field": "name", "expected": wts_updates[7583]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "researchtip", "expected": wts_updates[4396]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "researchubertip", "expected": wts_updates[31512]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "tip1", "expected": wts_updates[4397]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "tip2", "expected": wts_updates[4398]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "tip3", "expected": wts_updates[4399]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "tip4", "expected": wts_updates[4400]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "ubertip1", "expected": wts_updates[2177]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "ubertip2", "expected": wts_updates[889]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "ubertip3", "expected": wts_updates[1010]})
    checks_def.append({"type": "ability", "id": "A06A", "field": "ubertip4", "expected": wts_updates[1281]})

    # A06J: Снежная буря (Q)
    wts_updates[4458] = "|cffe4cfa3Снежная буря|r"
    wts_updates[4459] = "|cffe4cfa3Снежная буря|r (|cffffffffQ|r)"
    wts_updates[500] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает волны ледяных осколков, наносящих урон в области действия.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff6|cffced4da волн по |cffffffff25|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff8|cffced4da волн по |cffffffff35|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff10|cffced4da волн по |cffffffff45|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff14|cffced4da волн по |cffffffff60|cffced4da ед. урона.|r"
    )
    wts_updates[4460] = "|cffe4cfa3Снежная буря|r [|cffffffff1|r] (|cffffffffQ|r)"
    wts_updates[4461] = "|cffe4cfa3Снежная буря|r [|cffffffff2|r] (|cffffffffQ|r)"
    wts_updates[4462] = "|cffe4cfa3Снежная буря|r [|cffffffff3|r] (|cffffffffQ|r)"
    wts_updates[4463] = "|cffe4cfa3Снежная буря|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[501] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff6|cffced4da волн ледяных осколков по |cffffffff25|cffced4da ед. урона.|r"
    wts_updates[502] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff8|cffced4da волн ледяных осколков по |cffffffff35|cffced4da ед. урона.|r"
    wts_updates[539] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff10|cffced4da волн ледяных осколков по |cffffffff45|cffced4da ед. урона.|r"
    wts_updates[490] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff14|cffced4da волн ледяных осколков по |cffffffff60|cffced4da ед. урона.|r"

    checks_def.append({"type": "ability", "id": "A06J", "field": "name", "expected": wts_updates[4458]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "researchtip", "expected": wts_updates[4459]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "researchubertip", "expected": wts_updates[500]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "tip1", "expected": wts_updates[4460]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "tip2", "expected": wts_updates[4461]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "tip3", "expected": wts_updates[4462]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "tip4", "expected": wts_updates[4463]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "ubertip1", "expected": wts_updates[501]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "ubertip2", "expected": wts_updates[502]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "ubertip3", "expected": wts_updates[539]})
    checks_def.append({"type": "ability", "id": "A06J", "field": "ubertip4", "expected": wts_updates[490]})

    # A06I: Зов помощи (W)
    wts_updates[4447] = "|cffe4cfa3Зов помощи|r"
    wts_updates[4448] = "|cffe4cfa3Зов помощи|r (|cffffffffW|r)"
    wts_updates[352] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает на помощь верных воинов дренеев.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff1|cffced4da воин дреней.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff2|cffced4da воина дренея.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff3|cffced4da воина дренея.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff4|cffced4da воина дренея.|r"
    )
    wts_updates[4450] = "|cffe4cfa3Зов помощи|r [|cffffffff1|r] (|cffffffffW|r)"
    wts_updates[4451] = "|cffe4cfa3Зов помощи|r [|cffffffff2|r] (|cffffffffW|r)"
    wts_updates[4452] = "|cffe4cfa3Зов помощи|r [|cffffffff3|r] (|cffffffffW|r)"
    wts_updates[4453] = "|cffe4cfa3Зов помощи|r [|cffffffff4|r] (|cffffffffW|r)"
    wts_updates[353] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff1|cffced4da воина дренея на помощь.|r"
    wts_updates[354] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff2|cffced4da воинов дренеев на помощь.|r"
    wts_updates[355] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff3|cffced4da воинов дренеев на помощь.|r"
    wts_updates[444] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает |cffffffff4|cffced4da воинов дренеев на помощь.|r"

    checks_def.append({"type": "ability", "id": "A06I", "field": "name", "expected": wts_updates[4447]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "researchtip", "expected": wts_updates[4448]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "researchubertip", "expected": wts_updates[352]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "tip1", "expected": wts_updates[4450]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "tip2", "expected": wts_updates[4451]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "tip3", "expected": wts_updates[4452]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "tip4", "expected": wts_updates[4453]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "ubertip1", "expected": wts_updates[353]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "ubertip2", "expected": wts_updates[354]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "ubertip3", "expected": wts_updates[355]})
    checks_def.append({"type": "ability", "id": "A06I", "field": "ubertip4", "expected": wts_updates[444]})

    # A06H: Внушение (E)
    wts_updates[4440] = "|cffe4cfa3Внушение|r"
    wts_updates[4441] = "|cffe4cfa3Внушение|r (|cffffffffE|r)"
    wts_updates[32283] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет передвижение и регенерацию здоровья находящихся рядом союзников.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+10%|cffced4da к скорости, малый бонус к регенерации.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+20%|cffced4da к скорости, средний бонус к регенерации.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+30%|cffced4da к скорости, высокий бонус к регенерации.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+40%|cffced4da к скорости, высший бонус к регенерации.|r"
    )
    wts_updates[4442] = "|cffe4cfa3Внушение|r [|cffffffff1|r]"
    wts_updates[4443] = "|cffe4cfa3Внушение|r [|cffffffff2|r]"
    wts_updates[4444] = "|cffe4cfa3Внушение|r [|cffffffff3|r]"
    wts_updates[4445] = "|cffe4cfa3Внушение|r [|cffffffff4|r]"
    wts_updates[20574] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения на |cffc8e087+10%|cffced4da и повышает восстановление здоровья.|r"
    wts_updates[20575] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения на |cffc8e087+20%|cffced4da и повышает восстановление здоровья.|r"
    wts_updates[20576] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения на |cffc8e087+30%|cffced4da и повышает восстановление здоровья.|r"
    wts_updates[20573] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость перемещения на |cffc8e087+40%|cffced4da и повышает восстановление здоровья.|r"

    checks_def.append({"type": "ability", "id": "A06H", "field": "name", "expected": wts_updates[4440]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "researchtip", "expected": wts_updates[4441]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "researchubertip", "expected": wts_updates[32283]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "tip1", "expected": wts_updates[4442]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "tip2", "expected": wts_updates[4443]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "tip3", "expected": wts_updates[4444]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "tip4", "expected": wts_updates[4445]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "ubertip1", "expected": wts_updates[20574]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "ubertip2", "expected": wts_updates[20575]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "ubertip3", "expected": wts_updates[20576]})
    checks_def.append({"type": "ability", "id": "A06H", "field": "ubertip4", "expected": wts_updates[20573]})

    # A06G: Спокойствие (R)
    wts_updates[201] = "|cffe4cfa3Спокойствие|r"
    wts_updates[4438] = "|cffe4cfa3Спокойствие|r (|cffffffffR|r)"
    wts_updates[62] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает поток целительной энергии, восполняющей здоровье союзникам в обширной области.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff20|cffced4da ед. здоровья в сек.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff30|cffced4da ед. здоровья в сек.|r"
    )
    wts_updates[4437] = "|cffe4cfa3Спокойствие|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[4439] = "|cffe4cfa3Спокойствие|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[663] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет союзникам |cffffffff20|cffced4da ед. здоровья в сек. в обширной области.|r"
    wts_updates[667] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет союзникам |cffffffff30|cffced4da ед. здоровья в сек. в обширной области.|r"

    checks_def.append({"type": "ability", "id": "A06G", "field": "name", "expected": wts_updates[201]})
    checks_def.append({"type": "ability", "id": "A06G", "field": "researchtip", "expected": wts_updates[4438]})
    checks_def.append({"type": "ability", "id": "A06G", "field": "researchubertip", "expected": wts_updates[62]})
    checks_def.append({"type": "ability", "id": "A06G", "field": "tip1", "expected": wts_updates[4437]})
    checks_def.append({"type": "ability", "id": "A06G", "field": "tip2", "expected": wts_updates[4439]})
    checks_def.append({"type": "ability", "id": "A06G", "field": "ubertip1", "expected": wts_updates[663]})
    checks_def.append({"type": "ability", "id": "A06G", "field": "ubertip2", "expected": wts_updates[667]})

    # A1L6: Аура Спасения (E)
    wts_updates[38809] = "|cffe4cfa3Аура Спасения|r"
    wts_updates[15567] = "|cffe4cfa3Аура Спасения|r (|cffffffffE|r)"
    wts_updates[38811] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню находящихся рядом врагов и даёт шанс предотвратить гибель союзника рядом.|n|n"
        "|cffa6afb8Уровень 1:|r |cffff8080-1|cffced4da к броне врагов.|n"
        "|cffa6afb8Уровень 2:|r |cffff8080-2|cffced4da к броне врагов.|n"
        "|cffa6afb8Уровень 3:|r |cffff8080-3|cffced4da к броне врагов.|n"
        "|cffa6afb8Уровень 4:|r |cffff8080-4|cffced4da к броне врагов.|r"
    )
    wts_updates[38759] = "|cffe4cfa3Аура Спасения|r [|cffffffff1|r]"
    wts_updates[38760] = "|cffe4cfa3Аура Спасения|r [|cffffffff2|r]"
    wts_updates[23417] = "|cffe4cfa3Аура Спасения|r [|cffffffff3|r]"
    wts_updates[35178] = "|cffe4cfa3Аура Спасения|r [|cffffffff4|r]"
    wts_updates[38813] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню врагов на |cffff8080-1|cffced4da и предотвращает гибель союзников.|r"
    wts_updates[38814] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню врагов на |cffff8080-2|cffced4da и предотвращает гибель союзников.|r"
    wts_updates[35200] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню врагов на |cffff8080-3|cffced4da и предотвращает гибель союзников.|r"
    wts_updates[35184] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает броню врагов на |cffff8080-4|cffced4da и предотвращает гибель союзников.|r"

    checks_def.append({"type": "ability", "id": "A1L6", "field": "name", "expected": wts_updates[38809]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "researchtip", "expected": wts_updates[15567]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "researchubertip", "expected": wts_updates[38811]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "tip1", "expected": wts_updates[38759]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "tip2", "expected": wts_updates[38760]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "tip3", "expected": wts_updates[23417]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "tip4", "expected": wts_updates[35178]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "ubertip1", "expected": wts_updates[38813]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "ubertip2", "expected": wts_updates[38814]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "ubertip3", "expected": wts_updates[35200]})
    checks_def.append({"type": "ability", "id": "A1L6", "field": "ubertip4", "expected": wts_updates[35184]})

    # A1L7: Массовое исцеление (R)
    wts_updates[16463] = "|cffe4cfa3Массовое исцеление|r"
    wts_updates[16461] = "|cffe4cfa3Массовое исцеление|r (|cffffffffR|r)"
    wts_updates[16462] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает здоровье союзникам поблизости.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff250|cffced4da ед. здоровья.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff350|cffced4da ед. здоровья.|r"
    )
    wts_updates[11597] = "|cffe4cfa3Массовое исцеление|r [|cffffffff1|r] (|cffffffffR|r)"
    wts_updates[16456] = "|cffe4cfa3Массовое исцеление|r [|cffffffff2|r] (|cffffffffR|r)"
    wts_updates[12655] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff250|cffced4da ед. здоровья союзникам поблизости.|r"
    wts_updates[16457] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff350|cffced4da ед. здоровья союзникам поблизости.|r"

    checks_def.append({"type": "ability", "id": "A1L7", "field": "name", "expected": wts_updates[16463]})
    checks_def.append({"type": "ability", "id": "A1L7", "field": "researchtip", "expected": wts_updates[16461]})
    checks_def.append({"type": "ability", "id": "A1L7", "field": "researchubertip", "expected": wts_updates[16462]})
    checks_def.append({"type": "ability", "id": "A1L7", "field": "tip1", "expected": wts_updates[11597]})
    checks_def.append({"type": "ability", "id": "A1L7", "field": "tip2", "expected": wts_updates[16456]})
    checks_def.append({"type": "ability", "id": "A1L7", "field": "ubertip1", "expected": wts_updates[12655]})
    checks_def.append({"type": "ability", "id": "A1L7", "field": "ubertip2", "expected": wts_updates[16457]})

    # A1L4: Благословление (W)
    wts_updates[38599] = "|cffe4cfa3Благословление|r"
    wts_updates[38713] = "|cffe4cfa3Благословление|r (|cffffffffW|r)"
    wts_updates[38714] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает божественным щитом союзников вокруг, повышая урон на |cffc8e087+10%|cffced4da и регенерацию здоровья на |cffc8e087+5|cffced4da ед./сек. на |cffffffff20|cffced4da сек.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087+10|cffced4da к броне.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087+20|cffced4da к броне.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087+30|cffced4da к броне.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087+40|cffced4da к броне.|r"
    )
    wts_updates[38598] = "|cffe4cfa3Благословление|r [|cffffffff1|r] (|cffffffffW|r)"
    wts_updates[38601] = "|cffe4cfa3Благословление|r [|cffffffff2|r] (|cffffffffW|r)"
    wts_updates[38604] = "|cffe4cfa3Благословление|r [|cffffffff3|r] (|cffffffffW|r)"
    wts_updates[38616] = "|cffe4cfa3Благословление|r [|cffffffff4|r] (|cffffffffW|r)"
    wts_updates[775] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает щитом союзников вокруг на |cffffffff30|cffced4da сек., даруя |cffc8e087+2|cffced4da к броне.|r"
    wts_updates[779] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает щитом союзников вокруг на |cffffffff30|cffced4da сек., даруя |cffc8e087+3|cffced4da к броне.|r"
    wts_updates[780] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает щитом союзников вокруг на |cffffffff30|cffced4da сек., даруя |cffc8e087+4|cffced4da к броне.|r"
    wts_updates[810] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Покрывает щитом союзников вокруг на |cffffffff30|cffced4da сек., даруя |cffc8e087+6|cffced4da к броне.|r"

    checks_def.append({"type": "ability", "id": "A1L4", "field": "name", "expected": wts_updates[38599]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "researchtip", "expected": wts_updates[38713]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "researchubertip", "expected": wts_updates[38714]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "tip1", "expected": wts_updates[38598]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "tip2", "expected": wts_updates[38601]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "tip3", "expected": wts_updates[38604]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "tip4", "expected": wts_updates[38616]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "ubertip1", "expected": wts_updates[775]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "ubertip2", "expected": wts_updates[779]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "ubertip3", "expected": wts_updates[780]})
    checks_def.append({"type": "ability", "id": "A1L4", "field": "ubertip4", "expected": wts_updates[810]})

    # A1L5: Воскрешение (Q)
    wts_updates[38736] = "|cffe4cfa3Воскрешение|r"
    wts_updates[38737] = "|cffe4cfa3Воскрешение|r (|cffffffffQ|r)"
    wts_updates[38743] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни павших союзных воинов вокруг героя.|n|n"
        "|cffa6afb8Уровень 1:|r до |cffffffff6|cffced4da союзников.|n"
        "|cffa6afb8Уровень 2:|r до |cffffffff8|cffced4da союзников.|n"
        "|cffa6afb8Уровень 3:|r до |cffffffff10|cffced4da союзников.|n"
        "|cffa6afb8Уровень 4:|r до |cffffffff12|cffced4da союзников.|r"
    )
    wts_updates[38738] = "|cffe4cfa3Воскрешение|r [|cffffffff1|r] (|cffffffffQ|r)"
    wts_updates[38734] = "|cffe4cfa3Воскрешение|r [|cffffffff2|r] (|cffffffffQ|r)"
    wts_updates[38739] = "|cffe4cfa3Воскрешение|r [|cffffffff3|r] (|cffffffffQ|r)"
    wts_updates[38740] = "|cffe4cfa3Воскрешение|r [|cffffffff4|r] (|cffffffffQ|r)"
    wts_updates[38600] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни до |cffffffff8|cffced4da павших союзников.|r"
    wts_updates[38741] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни до |cffffffff10|cffced4da павших союзников.|r"
    wts_updates[38742] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Возвращает к жизни до |cffffffff12|cffced4da павших союзников.|r"

    checks_def.append({"type": "ability", "id": "A1L5", "field": "name", "expected": wts_updates[38736]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "researchtip", "expected": wts_updates[38737]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "researchubertip", "expected": wts_updates[38743]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "tip1", "expected": wts_updates[38738]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "tip2", "expected": wts_updates[38734]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "tip3", "expected": wts_updates[38739]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "tip4", "expected": wts_updates[38740]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "ubertip2", "expected": wts_updates[38600]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "ubertip3", "expected": wts_updates[38741]})
    checks_def.append({"type": "ability", "id": "A1L5", "field": "ubertip4", "expected": wts_updates[38742]})

    # A1L3: Свет Надежды
    wts_updates[38806] = "|cffe4cfa3Свет Надежды|r"
    wts_updates[38807] = "|cffe4cfa3Свет Надежды|r"
    wts_updates[38802] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Каждые |cffffffff12|cffced4da сек. наару выпускает волну света, исцеляющую союзника на |cffffffff100|cffced4da ед. здоровья и переходящую к другим целям.|r"

    checks_def.append({"type": "ability", "id": "A1L3", "field": "name", "expected": wts_updates[38806]})
    checks_def.append({"type": "ability", "id": "A1L3", "field": "tip1", "expected": wts_updates[38807]})
    checks_def.append({"type": "ability", "id": "A1L3", "field": "ubertip1", "expected": wts_updates[38802]})

    # A1L2: Волна исцеления
    wts_updates[37764] = "|cffe4cfa3Волна исцеления|r"
    wts_updates[38654] = (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создает волну энергии, восстанавливающую здоровье цели и переходящую к ближайшим союзникам.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff130|cffced4da ед., до |cffffffff3|cffced4da целей.|r"
    )
    wts_updates[38655] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Создает волну энергии, восстанавливающую |cffffffff130|cffced4da ед. здоровья цели и переходящую к |cffffffff3|cffced4da союзникам.|r"

    checks_def.append({"type": "ability", "id": "A1L2", "field": "name", "expected": wts_updates[37764]})
    checks_def.append({"type": "ability", "id": "A1L2", "field": "researchubertip", "expected": wts_updates[38654]})
    checks_def.append({"type": "ability", "id": "A1L2", "field": "ubertip1", "expected": wts_updates[38655]})

    # A1L1: Исцеление
    wts_updates[28012] = "|cffe4cfa3Исцеление|r"
    checks_def.append({"type": "ability", "id": "A1L1", "field": "name", "expected": wts_updates[28012]})

    # =========================================================================
    # 6. UNIT ABILITIES
    # =========================================================================
    # A0Z3: Ювелирное мастерство
    wts_updates[23313] = "|cffe4cfa3Ювелирное мастерство|r"
    wts_updates[23314] = "|cffe4cfa3Ювелирное мастерство|r"
    wts_updates[23315] = "|cffe4cfa3Ювелирное мастерство|r"
    wts_updates[23321] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Инженер имеет |cffffffff50%|cffced4da шанс начать строительство здания с |cffffffff20%|cffced4da начального прогресса.|r"

    checks_def.append({"type": "ability", "id": "A0Z3", "field": "name", "expected": wts_updates[23313]})
    checks_def.append({"type": "ability", "id": "A0Z3", "field": "researchtip", "expected": wts_updates[23314]})
    checks_def.append({"type": "ability", "id": "A0Z3", "field": "tip1", "expected": wts_updates[23315]})
    checks_def.append({"type": "ability", "id": "A0Z3", "field": "ubertip1", "expected": wts_updates[23321]})

    # A04Y: Свет небес (Q)
    wts_updates[3736] = "|cffe4cfa3Свет небес|r"
    wts_updates[3735] = "|cffe4cfa3Свет небес|r (|cffffffffQ|r)"
    wts_updates[3737] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восполняет |cffffffff150|cffced4da ед. здоровья живому союзнику или наносит вдвое меньший урон нежити.|r"

    checks_def.append({"type": "ability", "id": "A04Y", "field": "name", "expected": wts_updates[3736]})
    checks_def.append({"type": "ability", "id": "A04Y", "field": "tip1", "expected": wts_updates[3735]})
    checks_def.append({"type": "ability", "id": "A04Y", "field": "ubertip1", "expected": wts_updates[3737]})

    # A04W: Свет небес (R)
    wts_updates[3715] = "|cffe4cfa3Свет небес|r"
    wts_updates[3716] = "|cffe4cfa3Свет небес|r (|cffffffffR|r)"
    checks_def.append({"type": "ability", "id": "A04W", "field": "name", "expected": wts_updates[3715]})
    checks_def.append({"type": "ability", "id": "A04W", "field": "tip1", "expected": wts_updates[3716]})

    # A04U: Аура света
    wts_updates[3709] = "|cffe4cfa3Аура света|r"
    wts_updates[3710] = "|cffe4cfa3Аура света|r"
    wts_updates[8515] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость регенерации здоровья всем союзникам поблизости на |cffc8e087+0.5|cffced4da ед./сек.|r"

    checks_def.append({"type": "ability", "id": "A04U", "field": "name", "expected": wts_updates[3709]})
    checks_def.append({"type": "ability", "id": "A04U", "field": "tip1", "expected": wts_updates[3710]})
    checks_def.append({"type": "ability", "id": "A04U", "field": "ubertip1", "expected": wts_updates[8515]})

    # A04T: Возрождение
    wts_updates[3706] = "|cffe4cfa3Возрождение|r"
    wts_updates[3707] = "|cffe4cfa3Возрождение|r"
    wts_updates[3708] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Озарённый паладин мгновенно возрождается после гибели.|r"

    checks_def.append({"type": "ability", "id": "A04T", "field": "name", "expected": wts_updates[3706]})
    checks_def.append({"type": "ability", "id": "A04T", "field": "tip1", "expected": wts_updates[3707]})
    checks_def.append({"type": "ability", "id": "A04T", "field": "ubertip1", "expected": wts_updates[3708]})

    # A05V: Ускользание
    wts_updates[2175] = "|cffe4cfa3Ускользание|r"
    wts_updates[30855] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Даёт шанс |cffffffff17%|cffced4da уклониться от вражеской атаки.|r"

    checks_def.append({"type": "ability", "id": "A05V", "field": "tip1", "expected": wts_updates[2175]})
    checks_def.append({"type": "ability", "id": "A05V", "field": "ubertip1", "expected": wts_updates[30855]})

    # A05T: Пламя света
    wts_updates[3950] = "|cffe4cfa3Пламя света|r"
    wts_updates[3951] = "|cffe4cfa3Пламя света|r"
    wts_updates[4022] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Священный огонь атакует ближайших врагов, нанося |cffffffff20|cffced4da ед. урона и поджигая их на |cffffffff1|cffced4da ед./сек.|r"

    checks_def.append({"type": "ability", "id": "A05T", "field": "name", "expected": wts_updates[3950]})
    checks_def.append({"type": "ability", "id": "A05T", "field": "tip1", "expected": wts_updates[3951]})
    checks_def.append({"type": "ability", "id": "A05T", "field": "ubertip1", "expected": wts_updates[4022]})

    # A05C: Пламя света
    wts_updates[23187] = "|cffe4cfa3Пламя света|r"
    wts_updates[23188] = "|cffe4cfa3Пламя света|r"
    wts_updates[1587] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поджигает находящихся рядом врагов, нанося |cffffffff20|cffced4da ед. урона и |cffffffff2|cffced4da ед./сек.|r"

    checks_def.append({"type": "ability", "id": "A05C", "field": "name", "expected": wts_updates[23187]})
    checks_def.append({"type": "ability", "id": "A05C", "field": "tip1", "expected": wts_updates[23188]})
    checks_def.append({"type": "ability", "id": "A05C", "field": "ubertip1", "expected": wts_updates[1587]})

    # A05A: Рассеивание заклинаний (W)
    wts_updates[23185] = "|cffe4cfa3Рассеивание заклинаний|r"
    wts_updates[23186] = "|cffe4cfa3Рассеивание заклинаний|r (|cffffffffW|r)"
    checks_def.append({"type": "ability", "id": "A05A", "field": "name", "expected": wts_updates[23185]})
    checks_def.append({"type": "ability", "id": "A05A", "field": "tip1", "expected": wts_updates[23186]})

    # A059: Исцеление (Q)
    wts_updates[23183] = "|cffe4cfa3Исцеление|r"
    wts_updates[23184] = "|cffe4cfa3Исцеление|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "A059", "field": "name", "expected": wts_updates[23183]})
    checks_def.append({"type": "ability", "id": "A059", "field": "tip1", "expected": wts_updates[23184]})

    # A055: Воскрешение (E)
    wts_updates[3826] = "|cffe4cfa3Воскрешение|r"
    wts_updates[3827] = "|cffe4cfa3Воскрешение|r (|cffffffffE|r)"
    wts_updates[4203] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Воскрешает |cffffffff1|cffced4da павшего союзного воина поблизости.|r"

    checks_def.append({"type": "ability", "id": "A055", "field": "name", "expected": wts_updates[3826]})
    checks_def.append({"type": "ability", "id": "A055", "field": "tip1", "expected": wts_updates[3827]})
    checks_def.append({"type": "ability", "id": "A055", "field": "ubertip1", "expected": wts_updates[4203]})

    # A054: Внутреннее жжение (W)
    wts_updates[3823] = "|cffe4cfa3Внутреннее жжение|r"
    wts_updates[3824] = "|cffe4cfa3Внутреннее жжение|r (|cffffffffW|r)"
    wts_updates[3825] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает урон врагов и уменьшает их показатель брони.|r"

    checks_def.append({"type": "ability", "id": "A054", "field": "name", "expected": wts_updates[3823]})
    checks_def.append({"type": "ability", "id": "A054", "field": "tip1", "expected": wts_updates[3824]})
    checks_def.append({"type": "ability", "id": "A054", "field": "ubertip1", "expected": wts_updates[3825]})

    # A05X: Тяжелые удары
    wts_updates[3968] = "|cffe4cfa3Тяжелые удары|r"
    wts_updates[3969] = "|cffe4cfa3Тяжелые удары|r"
    wts_updates[3970] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит дополнительный урон по целям с тяжёлой бронёй.|r"

    checks_def.append({"type": "ability", "id": "A05X", "field": "name", "expected": wts_updates[3968]})
    checks_def.append({"type": "ability", "id": "A05X", "field": "tip1", "expected": wts_updates[3969]})
    checks_def.append({"type": "ability", "id": "A05X", "field": "ubertip1", "expected": wts_updates[3970]})

    # A05W: Усиленная броня (Q)
    wts_updates[23192] = "|cffe4cfa3Усиленная броня|r"
    wts_updates[23193] = "|cffe4cfa3Усиленная броня|r (|cffffffffQ|r)"
    wts_updates[23348] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает получаемый юнитом урон от вражеских атак.|r"

    checks_def.append({"type": "ability", "id": "A05W", "field": "name", "expected": wts_updates[23192]})
    checks_def.append({"type": "ability", "id": "A05W", "field": "tip1", "expected": wts_updates[23193]})
    checks_def.append({"type": "ability", "id": "A05W", "field": "ubertip1", "expected": wts_updates[23348]})

    # A052: Древние знания Света
    wts_updates[4201] = "|cffe4cfa3Древние знания Света|r"
    wts_updates[4202] = "|cffe4cfa3Древние знания Света|r"
    wts_updates[8535] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию маны находящихся рядом союзников на |cffc8e087+0.55|cffced4da ед./сек.|r"

    checks_def.append({"type": "ability", "id": "A052", "field": "name", "expected": wts_updates[4201]})
    checks_def.append({"type": "ability", "id": "A052", "field": "tip1", "expected": wts_updates[4202]})
    checks_def.append({"type": "ability", "id": "A052", "field": "ubertip1", "expected": wts_updates[8535]})

    # A051: Цепная молния (Q)
    wts_updates[3813] = "|cffe4cfa3Цепная молния|r"
    wts_updates[3814] = "|cffe4cfa3Цепная молния|r (|cffffffffQ|r)"
    wts_updates[3815] = "|cffe4cfa3Цепная молния|r (|cffffffffQ|r)"
    wts_updates[41155] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молнией цель, нанося |cffffffff85|cffced4da ед. урона, и переходит до |cffffffff4|cffced4da раз к другим врагам.|r"

    checks_def.append({"type": "ability", "id": "A051", "field": "name", "expected": wts_updates[3813]})
    checks_def.append({"type": "ability", "id": "A051", "field": "researchtip", "expected": wts_updates[3814]})
    checks_def.append({"type": "ability", "id": "A051", "field": "tip1", "expected": wts_updates[3815]})
    checks_def.append({"type": "ability", "id": "A051", "field": "ubertip1", "expected": wts_updates[41155]})

    # A050: Сглаз (E)
    wts_updates[3755] = "|cffe4cfa3Сглаз|r"
    wts_updates[3754] = "|cffe4cfa3Сглаз|r (|cffffffffE|r)"
    wts_updates[3757] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Изгоняет вражескую цель в астрал, замедляя её и лишая возможности атаковать.|r"

    checks_def.append({"type": "ability", "id": "A050", "field": "name", "expected": wts_updates[3755]})
    checks_def.append({"type": "ability", "id": "A050", "field": "tip1", "expected": wts_updates[3754]})
    checks_def.append({"type": "ability", "id": "A050", "field": "ubertip1", "expected": wts_updates[3757]})

    # A04Z: Сглаз (E)
    wts_updates[3751] = "|cffe4cfa3Сглаз|r"
    wts_updates[3752] = "|cffe4cfa3Сглаз|r (|cffffffffE|r)"
    wts_updates[8528] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Временно превращает врага в безобидное животное.|r"

    checks_def.append({"type": "ability", "id": "A04Z", "field": "name", "expected": wts_updates[3751]})
    checks_def.append({"type": "ability", "id": "A04Z", "field": "tip1", "expected": wts_updates[3752]})
    checks_def.append({"type": "ability", "id": "A04Z", "field": "ubertip1", "expected": wts_updates[8528]})

    # A058: Немота (E)
    wts_updates[3837] = "|cffe4cfa3Немота|r"
    wts_updates[3838] = "|cffe4cfa3Немота|r (|cffffffffE|r)"

    checks_def.append({"type": "ability", "id": "A058", "field": "name", "expected": wts_updates[3837]})
    checks_def.append({"type": "ability", "id": "A058", "field": "tip1", "expected": wts_updates[3838]})

    # A057: Замедление (Q)
    wts_updates[3835] = "|cffe4cfa3Замедление|r"
    wts_updates[3836] = "|cffe4cfa3Замедление|r (|cffffffffQ|r)"
    wts_updates[38968] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Замедляет скорость атаки врага на |cffff808025%|cffced4da и скорость передвижения на |cffff808035%|cffced4da.|r"

    checks_def.append({"type": "ability", "id": "A057", "field": "name", "expected": wts_updates[3835]})
    checks_def.append({"type": "ability", "id": "A057", "field": "tip1", "expected": wts_updates[3836]})
    checks_def.append({"type": "ability", "id": "A057", "field": "ubertip1", "expected": wts_updates[38968]})

    # A056: Похищение маны (W)
    wts_updates[3833] = "|cffe4cfa3Похищение маны|r"
    wts_updates[3834] = "|cffe4cfa3Похищение маны|r (|cffffffffW|r)"
    wts_updates[15187] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Вытягивает запас маны из вражеского юнита или передаёт ману союзнику.|r"

    checks_def.append({"type": "ability", "id": "A056", "field": "name", "expected": wts_updates[3833]})
    checks_def.append({"type": "ability", "id": "A056", "field": "tip1", "expected": wts_updates[3834]})
    checks_def.append({"type": "ability", "id": "A056", "field": "ubertip1", "expected": wts_updates[15187]})

    # A05L .. A05R: Посвященное оружие
    for sid_name, sid_tip, sid_ub in [
        (3922, 3923, 3974),
        (3929, 3930, 3927),
        (3937, 3938, 3935),
        (3925, 3926, 3924),
        (3933, 3934, 3931),
        (3941, 3942, 3939),
        (3945, 3946, 3943),
    ]:
        wts_updates[sid_name] = "|cffe4cfa3Посвященное оружие|r"
        wts_updates[sid_tip] = "|cffe4cfa3Посвященное оружие|r"
        wts_updates[sid_ub] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит дополнительный урон целям со всеми типами брони.|r"

    # A061: Сжигание маны
    wts_updates[3985] = "|cffe4cfa3Сжигание маны|r"
    wts_updates[3986] = "|cffe4cfa3Сжигание маны|r"
    checks_def.append({"type": "ability", "id": "A061", "field": "name", "expected": wts_updates[3985]})
    checks_def.append({"type": "ability", "id": "A061", "field": "tip1", "expected": wts_updates[3986]})

    # A060: Рассекающий удар
    wts_updates[3984] = "|cffe4cfa3Рассекающий удар|r"
    wts_updates[3982] = "|cffe4cfa3Рассекающий удар|r"
    wts_updates[13096] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит круговой урон по площади врагам рядом с основной целью.|r"

    checks_def.append({"type": "ability", "id": "A060", "field": "name", "expected": wts_updates[3984]})
    checks_def.append({"type": "ability", "id": "A060", "field": "tip1", "expected": wts_updates[3982]})
    checks_def.append({"type": "ability", "id": "A060", "field": "ubertip1", "expected": wts_updates[13096]})

    # A1C6: Спасение в тени
    wts_updates[30865] = "|cffe4cfa3Спасение в тени|r"
    wts_updates[30866] = "|cffe4cfa3Спасение в тени|r"
    wts_updates[30867] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da При гибели воина есть |cffffffff50%|cffced4da шанс, что он возродится у логова Сломленных.|r"

    checks_def.append({"type": "ability", "id": "A1C6", "field": "name", "expected": wts_updates[30865]})
    checks_def.append({"type": "ability", "id": "A1C6", "field": "tip1", "expected": wts_updates[30866]})
    checks_def.append({"type": "ability", "id": "A1C6", "field": "ubertip1", "expected": wts_updates[30867]})

    # A1C5: Скачок (B)
    wts_updates[30861] = "|cffe4cfa3Скачок|r (|cffffffffB|r)"
    wts_updates[30863] = "|cffe4cfa3Скачок|r (|cffffffffB|r)"
    checks_def.append({"type": "ability", "id": "A1C5", "field": "researchtip", "expected": wts_updates[30861]})
    checks_def.append({"type": "ability", "id": "A1C5", "field": "tip1", "expected": wts_updates[30863]})

    # A1C4: Стремительное приближение (E)
    wts_updates[30856] = "|cffe4cfa3Стремительное приближение|r"
    wts_updates[30857] = "|cffe4cfa3Стремительное приближение|r (|cffffffffE|r)"
    wts_updates[30858] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выбранные мастера совершают стремительный телепорт в указанную точку.|r"

    checks_def.append({"type": "ability", "id": "A1C4", "field": "name", "expected": wts_updates[30856]})
    checks_def.append({"type": "ability", "id": "A1C4", "field": "tip1", "expected": wts_updates[30857]})
    checks_def.append({"type": "ability", "id": "A1C4", "field": "ubertip1", "expected": wts_updates[30858]})

    # A05Z: Отравленное оружие
    wts_updates[3979] = "|cffe4cfa3Отравленное оружие|r"
    wts_updates[3980] = "|cffe4cfa3Отравленное оружие|r"
    checks_def.append({"type": "ability", "id": "A05Z", "field": "name", "expected": wts_updates[3979]})
    checks_def.append({"type": "ability", "id": "A05Z", "field": "tip1", "expected": wts_updates[3980]})

    # A05Y: Танец ветра (W)
    wts_updates[3975] = "|cffe4cfa3Танец ветра|r"
    wts_updates[3976] = "|cffe4cfa3Танец ветра|r (|cffffffffW|r)"
    wts_updates[3977] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует невидимость и ускорение. Первая атака из невидимости наносит повышенный урон.|r"

    checks_def.append({"type": "ability", "id": "A05Y", "field": "name", "expected": wts_updates[3975]})
    checks_def.append({"type": "ability", "id": "A05Y", "field": "tip1", "expected": wts_updates[3976]})
    checks_def.append({"type": "ability", "id": "A05Y", "field": "ubertip1", "expected": wts_updates[3977]})

    # A1C8: Поле слома (R)
    wts_updates[30875] = "|cffe4cfa3Поле слома|r"
    wts_updates[10266] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Значительно снижает скорость дальнобойной атаки врагов в указанной области.|r"

    checks_def.append({"type": "ability", "id": "A1C8", "field": "name", "expected": wts_updates[30875]})
    checks_def.append({"type": "ability", "id": "A1C8", "field": "ubertip1", "expected": wts_updates[10266]})

    # A063: Щит молний (E)
    wts_updates[3991] = "|cffe4cfa3Щит молний|r"
    wts_updates[3992] = "|cffe4cfa3Щит молний|r (|cffffffffE|r)"
    checks_def.append({"type": "ability", "id": "A063", "field": "name", "expected": wts_updates[3991]})
    checks_def.append({"type": "ability", "id": "A063", "field": "tip1", "expected": wts_updates[3992]})

    # A067: Массовое исцеление (W)
    wts_updates[4023] = "|cffe4cfa3Массовое исцеление|r"
    wts_updates[4101] = "|cffe4cfa3Массовое исцеление|r (|cffffffffW|r)"
    wts_updates[13106] = "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Восстанавливает |cffffffff125|cffced4da ед. здоровья всем союзникам в радиусе |cffffffff300|cffced4da.|r"

    checks_def.append({"type": "ability", "id": "A067", "field": "name", "expected": wts_updates[4023]})
    checks_def.append({"type": "ability", "id": "A067", "field": "tip1", "expected": wts_updates[4101]})
    checks_def.append({"type": "ability", "id": "A067", "field": "ubertip1", "expected": wts_updates[13106]})

    # A066: Безумие (Q)
    wts_updates[4016] = "|cffe4cfa3Безумие|r"
    wts_updates[4017] = "|cffe4cfa3Безумие|r (|cffffffffQ|r)"
    checks_def.append({"type": "ability", "id": "A066", "field": "name", "expected": wts_updates[4016]})
    checks_def.append({"type": "ability", "id": "A066", "field": "tip1", "expected": wts_updates[4017]})

    # =========================================================================
    # 7. UPGRADES / RESEARCHES
    # =========================================================================
    # R023: Руническое оружие (Q, 6 уровней)
    r023_names = [23194, 23195, 23196, 23203, 23204, 23205]
    r023_tips = [23197, 23198, 23199, 23206, 23207, 23208]
    r023_ubs = [23200, 23201, 23202, 23209, 23210, 23211]
    for i in range(6):
        lvl = i + 1
        wts_updates[r023_names[i]] = f"|cffe4cfa3Руническое оружие [{lvl}/6]|r"
        wts_updates[r023_tips[i]] = f"|cffe4cfa3Руническое оружие [{lvl}/6]|r (|cffffffffQ|r)"
        wts_updates[r023_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает силу атаки воинов ближнего боя Дренеев на |cffc8e087+{lvl * 2}|cffced4da ед. (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЛазутчик|cffced4da|n"
            f"- |cffa9c7deВсадник на Элекке|cffced4da|n"
            f"- |cffa9c7deМечник Озаренный|cffced4da|n"
            f"- |cffa9c7deОзаренный Паладин|cffced4da|n"
            f"- |cffa9c7deСломленный страж|cffced4da|n"
            f"- |cffa9c7deСломленный мастер|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R023", "field": f"name{lvl}", "expected": wts_updates[r023_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R023", "field": f"tip{lvl}", "expected": wts_updates[r023_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R023", "field": f"ubertip{lvl}", "expected": wts_updates[r023_ubs[i]]})

    # R024: Апекситовый доспех (A, 6 уровней)
    r024_names = [23215, 23216, 23217, 23212, 23213, 23214]
    r024_tips = [23218, 23219, 23220, 23221, 23222, 23223]
    r024_ubs = [23224, 23225, 23226, 23227, 23229, 23228]
    for i in range(6):
        lvl = i + 1
        wts_updates[r024_names[i]] = f"|cffe4cfa3Апекситовый доспех [{lvl}/6]|r"
        wts_updates[r024_tips[i]] = f"|cffe4cfa3Апекситовый доспех [{lvl}/6]|r (|cffffffffA|r)"
        wts_updates[r024_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает показатель брони всех сухопутных войск Дренеев на |cffc8e087+{lvl * 2}|cffced4da ед. (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- Все сухопутные войска Дренеев.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R024", "field": f"name{lvl}", "expected": wts_updates[r024_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R024", "field": f"tip{lvl}", "expected": wts_updates[r024_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R024", "field": f"ubertip{lvl}", "expected": wts_updates[r024_ubs[i]]})

    # R02P: Заточенные наконечники (W, 6 уровней)
    r02p_names = [23251, 23252, 23253, 23266, 23267, 23268]
    r02p_tips = [23254, 23255, 23256, 23260, 23261, 23262]
    r02p_ubs = [23257, 23258, 23259, 23263, 23264, 23265]
    for i in range(6):
        lvl = i + 1
        wts_updates[r02p_names[i]] = f"|cffe4cfa3Заточенные наконечники [{lvl}/6]|r"
        wts_updates[r02p_tips[i]] = f"|cffe4cfa3Заточенные наконечники [{lvl}/6]|r (|cffffffffW|r)"
        wts_updates[r02p_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает силу атаки стрелков и осадных машин Дренеев на |cffc8e087+{lvl * 2}|cffced4da ед. (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deРангари|cffced4da|n"
            f"- |cffa9c7deОсадная машина|cffced4da|n"
            f"- |cffa9c7deСломленный провидец|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R02P", "field": f"name{lvl}", "expected": wts_updates[r02p_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R02P", "field": f"tip{lvl}", "expected": wts_updates[r02p_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R02P", "field": f"ubertip{lvl}", "expected": wts_updates[r02p_ubs[i]]})

    # R02R: Посвящение Озаренных (R)
    wts_updates[4307] = "|cffe4cfa3Посвящение Озаренных|r"
    wts_updates[4308] = "|cffe4cfa3Посвящение Озаренных|r (|cffffffffR|r)"
    wts_updates[11682] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает возможность возводить Храм Озаренных и нанимать элитные войска Озарённых дренеев.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deХрам Озаренных|cffced4da: открывает постройку и доступ к священным воинам.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02R", "field": "name1", "expected": wts_updates[4307]})
    checks_def.append({"type": "upgrade", "id": "R02R", "field": "tip1", "expected": wts_updates[4308]})
    checks_def.append({"type": "upgrade", "id": "R02R", "field": "ubertip1", "expected": wts_updates[11682]})

    # R02Q: Привлечь Сломленных (E)
    wts_updates[40968] = "|cffe4cfa3Привлечь Сломленных|r"
    wts_updates[40969] = "|cffe4cfa3Привлечь Сломленных|r (|cffffffffE|r)"
    wts_updates[4303] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает возможность возводить Логово Сломленных и нанимать войска Сломленных дренеев и Пеплоустов.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЛогово Сломленных|cffced4da: открывает постройку и доступ к изгнанникам.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02Q", "field": "name1", "expected": wts_updates[40968]})
    checks_def.append({"type": "upgrade", "id": "R02Q", "field": "tip1", "expected": wts_updates[40969]})
    checks_def.append({"type": "upgrade", "id": "R02Q", "field": "ubertip1", "expected": wts_updates[4303]})

    # R0D8: Улучшенные инструменты (Z, 4 уровня)
    r0d8_names = [40971, 40972, 40973, 40974]
    r0d8_tips = [40975, 40976, 40977, 40978]
    r0d8_ubs = [8002, 7999, 8000, 8001]
    for i in range(4):
        lvl = i + 1
        wts_updates[r0d8_names[i]] = f"|cffe4cfa3Улучшенные инструменты [{lvl}/4]|r"
        wts_updates[r0d8_tips[i]] = f"|cffe4cfa3Улучшенные инструменты [{lvl}/4]|r (|cffffffffZ|r)"
        wts_updates[r0d8_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает объём переносимой работниками древесины на |cffc8e087+{lvl * 8}|cffced4da ед. (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deИнженер|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R0D8", "field": f"name{lvl}", "expected": wts_updates[r0d8_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R0D8", "field": f"tip{lvl}", "expected": wts_updates[r0d8_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R0D8", "field": f"ubertip{lvl}", "expected": wts_updates[r0d8_ubs[i]]})

    # R029: Дренейское мастерство (A, 3 уровня)
    r029_names = [41092, 41102, 41116]
    r029_tips = [41117, 41118, 41119]
    r029_ubs = [20601, 20602, 20603]
    for i in range(3):
        lvl = i + 1
        wts_updates[r029_names[i]] = f"|cffe4cfa3Дренейское мастерство [{lvl}/3]|r"
        wts_updates[r029_tips[i]] = f"|cffe4cfa3Дренейское мастерство [{lvl}/3]|r (|cffffffffA|r)"
        wts_updates[r029_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает боевые характеристики лазутчиков, рангари и всадников на элекках: увеличивает здоровье на |cffc8e087+{lvl * 40}|cffced4da ед. и скорость передвижения (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЛазутчик|cffced4da|n"
            f"- |cffa9c7deРангари|cffced4da|n"
            f"- |cffa9c7deВсадник на Элекке|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R029", "field": f"name{lvl}", "expected": wts_updates[r029_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R029", "field": f"tip{lvl}", "expected": wts_updates[r029_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R029", "field": f"ubertip{lvl}", "expected": wts_updates[r029_ubs[i]]})

    # R02B: Тяжелые доспехи (D)
    wts_updates[23233] = "|cffe4cfa3Тяжелые доспехи|r"
    wts_updates[23234] = "|cffe4cfa3Тяжелые доспехи|r (|cffffffffD|r)"
    wts_updates[23235] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Оснащает всадников на элекках массивными доспехами, увеличивая запас здоровья на |cffc8e087+150|cffced4da ед. и показатель брони на |cffc8e087+2|cffced4da.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deВсадник на Элекке|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02B", "field": "name1", "expected": wts_updates[23233]})
    checks_def.append({"type": "upgrade", "id": "R02B", "field": "tip1", "expected": wts_updates[23234]})
    checks_def.append({"type": "upgrade", "id": "R02B", "field": "ubertip1", "expected": wts_updates[23235]})

    # R02C: Ковка оружия (C)
    wts_updates[4067] = "|cffe4cfa3Ковка оружия|r"
    wts_updates[4070] = "|cffe4cfa3Ковка оружия|r (|cffffffffC|r)"
    wts_updates[4073] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Изготавливает усиленное вооружение для всадников на элекках, увеличивая силу атаки на |cffc8e087+8|cffced4da ед.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deВсадник на Элекке|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02C", "field": "name1", "expected": wts_updates[4067]})
    checks_def.append({"type": "upgrade", "id": "R02C", "field": "tip1", "expected": wts_updates[4070]})
    checks_def.append({"type": "upgrade", "id": "R02C", "field": "ubertip1", "expected": wts_updates[4073]})

    # R02D: Таинство Магии (A, 2 уровня)
    wts_updates[23236] = "|cffe4cfa3Таинство Магии [1/2]|r"
    wts_updates[23237] = "|cffe4cfa3Таинство Магии [2/2]|r"
    wts_updates[23238] = "|cffe4cfa3Таинство Магии [1/2]|r (|cffffffffA|r)"
    wts_updates[23239] = "|cffe4cfa3Таинство Магии [2/2]|r (|cffffffffA|r)"
    wts_updates[23240] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает ранг чароплетниц до адептов: увеличивает здоровье на |cffc8e087+40|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед., скорость регенерации маны и открывает заклинание «Похищение маны» (уровень |cffffffff1|cffced4da).|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЧароплетница|cffced4da.|r"
    )
    wts_updates[23241] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает ранг чароплетниц до мастеров: увеличивает здоровье на |cffc8e087+40|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед., скорость регенерации маны и открывает заклинание «Немота» (уровень |cffffffff2|cffced4da).|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЧароплетница|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02D", "field": "name1", "expected": wts_updates[23236]})
    checks_def.append({"type": "upgrade", "id": "R02D", "field": "name2", "expected": wts_updates[23237]})
    checks_def.append({"type": "upgrade", "id": "R02D", "field": "tip1", "expected": wts_updates[23238]})
    checks_def.append({"type": "upgrade", "id": "R02D", "field": "tip2", "expected": wts_updates[23239]})
    checks_def.append({"type": "upgrade", "id": "R02D", "field": "ubertip1", "expected": wts_updates[23240]})
    checks_def.append({"type": "upgrade", "id": "R02D", "field": "ubertip2", "expected": wts_updates[23241]})

    # R02E: Дар Наару (S, 3 уровня)
    r02e_names = [23242, 23243, 23244]
    r02e_tips = [23245, 23246, 23247]
    r02e_ubs = [23248, 23249, 23250]
    for i in range(3):
        lvl = i + 1
        wts_updates[r02e_names[i]] = f"|cffe4cfa3Дар Наару [{lvl}/3]|r"
        wts_updates[r02e_tips[i]] = f"|cffe4cfa3Дар Наару [{lvl}/3]|r (|cffffffffS|r)"
        wts_updates[r02e_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Посвящает жрецов в таинства Света: увеличивает запас маны на |cffc8e087+{lvl * 50}|cffced4da ед., её регенерацию и открывает новые заклинания (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЖрец|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R02E", "field": f"name{lvl}", "expected": wts_updates[r02e_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R02E", "field": f"tip{lvl}", "expected": wts_updates[r02e_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R02E", "field": f"ubertip{lvl}", "expected": wts_updates[r02e_ubs[i]]})

    # R02F: Чародейские познания (D)
    wts_updates[4104] = "|cffe4cfa3Чародейские познания|r"
    wts_updates[4105] = "|cffe4cfa3Чародейские познания|r (|cffffffffD|r)"
    wts_updates[4106] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает максимальный запас маны чародеев на |cffc8e087+25|cffced4da ед. и открывает способность «Безумие».|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЧародей|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02F", "field": "name1", "expected": wts_updates[4104]})
    checks_def.append({"type": "upgrade", "id": "R02F", "field": "tip1", "expected": wts_updates[4105]})
    checks_def.append({"type": "upgrade", "id": "R02F", "field": "ubertip1", "expected": wts_updates[4106]})

    # R022: Посвящение Паладина (F, 3 уровня)
    r022_names = [19558, 19559, 19564]
    r022_tips = [19562, 19563, 19573]
    r022_ubs = [3747, 3748, 4208]
    for i in range(3):
        lvl = i + 1
        wts_updates[r022_names[i]] = f"|cffe4cfa3Посвящение Паладина [{lvl}/3]|r"
        wts_updates[r022_tips[i]] = f"|cffe4cfa3Посвящение Паладина [{lvl}/3]|r (|cffffffffF|r)"
        wts_updates[r022_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья паладинов на |cffc8e087+{lvl * 50}|cffced4da ед., запас маны на |cffc8e087+{lvl * 40}|cffced4da ед., её регенерацию и открывает священные чары (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deОзаренный Паладин|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R022", "field": f"name{lvl}", "expected": wts_updates[r022_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R022", "field": f"tip{lvl}", "expected": wts_updates[r022_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R022", "field": f"ubertip{lvl}", "expected": wts_updates[r022_ubs[i]]})

    # R02M: Учение наару (S, 2 уровня)
    wts_updates[4224] = "|cffe4cfa3Учение наару [1/2]|r"
    wts_updates[4225] = "|cffe4cfa3Учение наару [2/2]|r"
    wts_updates[4227] = "|cffe4cfa3Учение наару [1/2]|r (|cffffffffS|r)"
    wts_updates[4228] = "|cffe4cfa3Учение наару [2/2]|r (|cffffffffS|r)"
    wts_updates[4230] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Жрицы Наару постигают глубокие знания Света: увеличивает запас маны на |cffc8e087+40|cffced4da ед. и скорость её регенерации на |cffc8e087+0.3|cffced4da ед./сек. (уровень |cffffffff1|cffced4da).|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЖрица Наару|cffced4da.|r"
    )
    wts_updates[4231] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Жрицы Наару постигают высшие знания Света: увеличивает запас маны на |cffc8e087+80|cffced4da ед. и скорость её регенерации на |cffc8e087+0.6|cffced4da ед./сек. (уровень |cffffffff2|cffced4da).|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deЖрица Наару|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02M", "field": "name1", "expected": wts_updates[4224]})
    checks_def.append({"type": "upgrade", "id": "R02M", "field": "name2", "expected": wts_updates[4225]})
    checks_def.append({"type": "upgrade", "id": "R02M", "field": "tip1", "expected": wts_updates[4227]})
    checks_def.append({"type": "upgrade", "id": "R02M", "field": "tip2", "expected": wts_updates[4228]})
    checks_def.append({"type": "upgrade", "id": "R02M", "field": "ubertip1", "expected": wts_updates[4230]})
    checks_def.append({"type": "upgrade", "id": "R02M", "field": "ubertip2", "expected": wts_updates[4231]})

    # R02L: Изучение магии (D, 2 уровня)
    wts_updates[4211] = "|cffe4cfa3Изучение магии [1/2]|r"
    wts_updates[4212] = "|cffe4cfa3Изучение магии [2/2]|r"
    wts_updates[4214] = "|cffe4cfa3Изучение магии [1/2]|r (|cffffffffD|r)"
    wts_updates[4215] = "|cffe4cfa3Изучение магии [2/2]|r (|cffffffffD|r)"
    wts_updates[4217] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья магов Озарённых на |cffc8e087+40|cffced4da ед., запас маны на |cffc8e087+50|cffced4da ед., её регенерацию на |cffc8e087+0.5|cffced4da ед./сек. и открывает способность «Цепная молния» (уровень |cffffffff1|cffced4da).|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deМаг Озаренный|cffced4da.|r"
    )
    wts_updates[4218] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья магов Озарённых на |cffc8e087+80|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед., её регенерацию на |cffc8e087+1.0|cffced4da ед./сек. и открывает способность «Сглаз» (уровень |cffffffff2|cffced4da).|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deМаг Озаренный|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02L", "field": "name1", "expected": wts_updates[4211]})
    checks_def.append({"type": "upgrade", "id": "R02L", "field": "name2", "expected": wts_updates[4212]})
    checks_def.append({"type": "upgrade", "id": "R02L", "field": "tip1", "expected": wts_updates[4214]})
    checks_def.append({"type": "upgrade", "id": "R02L", "field": "tip2", "expected": wts_updates[4215]})
    checks_def.append({"type": "upgrade", "id": "R02L", "field": "ubertip1", "expected": wts_updates[4217]})
    checks_def.append({"type": "upgrade", "id": "R02L", "field": "ubertip2", "expected": wts_updates[4218]})

    # R02N: Освящение оружия (A)
    wts_updates[4237] = "|cffe4cfa3Освящение оружия|r"
    wts_updates[4240] = "|cffe4cfa3Освящение оружия|r (|cffffffffA|r)"
    wts_updates[4243] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Наполняет клинки мечников Озарённых священной силой, наделяя их атаки способностью «Посвященное оружие» с повышенным уроном по всем типам брони.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deМечник Озаренный|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02N", "field": "name1", "expected": wts_updates[4237]})
    checks_def.append({"type": "upgrade", "id": "R02N", "field": "tip1", "expected": wts_updates[4240]})
    checks_def.append({"type": "upgrade", "id": "R02N", "field": "ubertip1", "expected": wts_updates[4243]})

    # R02J: Мастерство Пеплоустов (D)
    wts_updates[41093] = "|cffe4cfa3Мастерство Пеплоустов|r"
    wts_updates[41094] = "|cffe4cfa3Мастерство Пеплоустов|r (|cffffffffD|r)"
    wts_updates[4273] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает воинов Сломленных боевой ярости Пеплоустов: повышает скорость атаки, но снижает скорость передвижения.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deСломленный страж|cffced4da|n"
        "- |cffa9c7deСломленный мастер|cffced4da.|n|n"
        "|cffff8080Исключает исследование «Мастерство Сломленных».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02J", "field": "name1", "expected": wts_updates[41093]})
    checks_def.append({"type": "upgrade", "id": "R02J", "field": "tip1", "expected": wts_updates[41094]})
    checks_def.append({"type": "upgrade", "id": "R02J", "field": "ubertip1", "expected": wts_updates[4273]})

    # R02K: Мастерство Сломленных (D)
    wts_updates[41095] = "|cffe4cfa3Мастерство Сломленных|r"
    wts_updates[41096] = "|cffe4cfa3Мастерство Сломленных|r (|cffffffffD|r)"
    wts_updates[4274] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает воинов Сломленных ловкости и стремительности: повышает скорость передвижения, но незначительно снижает скорость атаки.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deСломленный страж|cffced4da|n"
        "- |cffa9c7deСломленный мастер|cffced4da.|n|n"
        "|cffff8080Исключает исследование «Мастерство Пеплоустов».|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02K", "field": "name1", "expected": wts_updates[41095]})
    checks_def.append({"type": "upgrade", "id": "R02K", "field": "tip1", "expected": wts_updates[41096]})
    checks_def.append({"type": "upgrade", "id": "R02K", "field": "ubertip1", "expected": wts_updates[4274]})

    # R02G: Мудрость предков (A, 3 уровня)
    r02g_names = [4126, 4127, 4128]
    r02g_tips = [4129, 4130, 4131]
    r02g_ubs = [20604, 20605, 20606]
    for i in range(3):
        lvl = i + 1
        wts_updates[r02g_names[i]] = f"|cffe4cfa3Мудрость предков [{lvl}/3]|r"
        wts_updates[r02g_tips[i]] = f"|cffe4cfa3Мудрость предков [{lvl}/3]|r (|cffffffffA|r)"
        wts_updates[r02g_ubs[i]] = (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Открывает Сломленным провидцам шаманские тайны: увеличивает дальность атаки, запас маны на |cffc8e087+{lvl * 25}|cffced4da ед. и наделяет новыми способностями (уровень |cffffffff{lvl}|cffced4da).|n|n"
            f"|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deСломленный провидец|cffced4da.|r"
        )
        checks_def.append({"type": "upgrade", "id": "R02G", "field": f"name{lvl}", "expected": wts_updates[r02g_names[i]]})
        checks_def.append({"type": "upgrade", "id": "R02G", "field": f"tip{lvl}", "expected": wts_updates[r02g_tips[i]]})
        checks_def.append({"type": "upgrade", "id": "R02G", "field": f"ubertip{lvl}", "expected": wts_updates[r02g_ubs[i]]})

    # R02H: Мастерство танца ветра (D)
    wts_updates[4141] = "|cffe4cfa3Мастерство танца ветра|r"
    wts_updates[4144] = "|cffe4cfa3Мастерство танца ветра|r (|cffffffffD|r)"
    wts_updates[4147] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Сломленных мастеров скрытности и внезапному нападению, открывая способность «Танец ветра».|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deСломленный мастер|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02H", "field": "name1", "expected": wts_updates[4141]})
    checks_def.append({"type": "upgrade", "id": "R02H", "field": "tip1", "expected": wts_updates[4144]})
    checks_def.append({"type": "upgrade", "id": "R02H", "field": "ubertip1", "expected": wts_updates[4147]})

    # R02I: Отравленное оружие (D)
    wts_updates[4154] = "|cffe4cfa3Отравленное оружие|r"
    wts_updates[4157] = "|cffe4cfa3Отравленное оружие|r (|cffffffffD|r)"
    wts_updates[4160] = (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Покрывает оружие Сломленных смертоносным ядом, замедляющим врагов и наносящим периодический урон.|n|n"
        "|cffa6afb8Затрагивает:|cffced4da|n- |cffa9c7deСломленный мастер|cffced4da.|r"
    )
    checks_def.append({"type": "upgrade", "id": "R02I", "field": "name1", "expected": wts_updates[4154]})
    checks_def.append({"type": "upgrade", "id": "R02I", "field": "tip1", "expected": wts_updates[4157]})
    checks_def.append({"type": "upgrade", "id": "R02I", "field": "ubertip1", "expected": wts_updates[4160]})

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
        "race": "Draeneis",
        "wts_updates": {str(k): v for k, v in sorted(wts_updates.items())},
        "checks_def": checks_def,
        "categories": {
            "selection": ["A0HS"],
            "markers": ["R07G"],
            "buildings": [
                "h015", "h016", "h017", "h033", "h055", "h056",
                "h057", "h058", "h05A", "h05B", "h05C", "h011"
            ],
            "units": [
                "h012", "e000", "h01O", "h01P", "h01Q", "h01R",
                "h01S", "h01T", "h01U", "h059", "h05D", "h05E",
                "n005", "nDr1", "o00H", "n00P"
            ],
            "heroes": ["H05K", "H05L", "H05M", "H0MI"],
            "upgrades": [
                "R07G", "R023", "R024", "R02P", "R02R", "R02Q", "R0D8", "R029",
                "R02B", "R02C", "R02D", "R02E", "R02F", "R022", "R02M", "R02L",
                "R02N", "R02J", "R02K", "R02G", "R02H", "R02I"
            ],
            "abilities": [
                "A0HS", "A0Z3", "A04Y", "A04W", "A04U", "A04T", "A05V", "A05T",
                "A05C", "A05A", "A059", "A055", "A054", "A05X", "A05W", "A052",
                "A051", "A050", "A04Z", "A058", "A057", "A056", "A05L", "A05N",
                "A05P", "A05M", "A05O", "A05Q", "A05R", "A061", "A060", "A1C6",
                "A1C5", "A1C4", "A05Z", "A05Y", "A1C8", "A063", "A067", "A066",
                "AOhw", "A06C", "A068", "A069", "A0Z0", "A06F", "A06E", "A06A",
                "A06J", "A06I", "A06H", "A06G", "A1L6", "A1L7", "A1L4", "A1L5",
                "A1L3", "A1L2", "A1L1"
            ]
        }
    }

    out_file = folder / "draenei_plan.json"
    out_file.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Master plan saved to {out_file} ({len(wts_updates)} string updates, {len(checks_def)} checks)")

if __name__ == "__main__":
    main()
