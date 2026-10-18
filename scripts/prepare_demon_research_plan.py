# -*- coding: utf-8 -*-
"""Generate complete plan for Demon researches standardization."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def build_plan():
    wts_updates = {
        # R004: Эволюция: Кровавый палач (h0DY)
        15970: "S",
        13295: "|cffe4cfa3Эволюция: Кровавый палач|r",
        13298: "|cffe4cfa3Эволюция: Кровавый палач|r (|cffffffffS|r)",
        18682: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Трансформирует всех Властителей в более могучих Кровавых палачей, повышая их запас здоровья, урон и боевые характеристики.|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da.|r",

        # R08H: Эволюция: Кровавое отродье (h0DY)
        32190: "X",
        13301: "|cffe4cfa3Эволюция: Кровавое отродье|r",
        13302: "|cffe4cfa3Эволюция: Кровавое отродье|r (|cffffffffX|r)",
        18683: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Трансформирует всех Кровавых палачей в свирепых Кровавых отродий, наделяя их пассивной способностью «Рассекающий удар» (25% урона по площади) и повышая характеристики.|n|nЗатрагивает: |cffa9c7deКровавый палач|cffced4da.|r",

        # R08I: Эволюция: Кровопускатель (h0DY)
        25098: "C",
        13272: "|cffe4cfa3Эволюция: Кровопускатель|r",
        13296: "|cffe4cfa3Эволюция: Кровопускатель|r (|cffffffffC|r)",
        18684: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Трансформирует всех Кровавых отродий в элитных демонических пехотинцев — Кровопускателей. Усиливает «Рассекающий удар» до 40% урона по площади и открывает возможность использовать способность «Укрыться за щитом».|n|nЗатрагивает: |cffa9c7deКровавое отродье|cffced4da.|r",

        # R08O: Защита (h0DY)
        28641: "Z",
        13856: "|cffe4cfa3Защита|r (|cffffffffZ|r)",
        13869: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Кровопускателей способности «Укрыться за щитом», позволяющей снижать урон от дальних пронзающих атак до 50% в обмен на снижение скорости передвижения на 30%.|n|nЗатрагивает: |cffa9c7deКровопускатель|cffced4da.|r",

        # R08J: Оружие Скверны (h0DZ, 6 ур.)
        35999: "Q", 36355: "Q", 36356: "Q", 36619: "Q", 36620: "Q", 36671: "Q",
        13745: "|cffe4cfa3Оружие Скверны|r", 13743: "|cffe4cfa3Оружие Скверны|r", 13742: "|cffe4cfa3Оружие Скверны|r",
        13741: "|cffe4cfa3Оружие Скверны|r", 13740: "|cffe4cfa3Оружие Скверны|r", 13739: "|cffe4cfa3Оружие Скверны|r",
        13750: "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 1|r] (|cffffffffQ|r)",
        13749: "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 2|r] (|cffffffffQ|r)",
        13748: "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 3|r] (|cffffffffQ|r)",
        13747: "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 4|r] (|cffffffffQ|r)",
        13746: "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 5|r] (|cffffffffQ|r)",
        13744: "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 6|r] (|cffffffffQ|r)",
        8987: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак воинов ближнего боя Легиона на |cffffffff+3|cffced4da ед.|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",
        8988: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от атак воинов ближнего боя Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",
        8989: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от атак воинов ближнего боя Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+9|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",
        9008: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от атак воинов ближнего боя Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+12|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",
        8996: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от атак воинов ближнего боя Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+15|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",
        9009: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон от атак воинов ближнего боя Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+18|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",

        # R08K: Осквернённая броня (h0DZ, 6 ур.)
        17541: "A", 17542: "A", 17615: "A", 17616: "A", 17617: "A", 17640: "A",
        13760: "|cffe4cfa3Осквернённая броня|r", 13762: "|cffe4cfa3Осквернённая броня|r", 13761: "|cffe4cfa3Осквернённая броня|r",
        13765: "|cffe4cfa3Осквернённая броня|r", 13764: "|cffe4cfa3Осквернённая броня|r", 13763: "|cffe4cfa3Осквернённая броня|r",
        13766: "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 1|r] (|cffffffffA|r)",
        13767: "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 2|r] (|cffffffffA|r)",
        13768: "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 3|r] (|cffffffffA|r)",
        13771: "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 4|r] (|cffffffffA|r)",
        13770: "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 5|r] (|cffffffffA|r)",
        13769: "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 6|r] (|cffffffffA|r)",
        13772: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню воинов ближнего боя Легиона на |cffffffff+2|cffced4da ед.|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",
        13773: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню воинов ближнего боя Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+4|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",
        13774: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню воинов ближнего боя Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r",

        # R08L: Магия Скверны (h0DZ, 6 ур.)
        37067: "W", 37068: "W", 37423: "W", 37443: "W", 37444: "W", 37445: "W",
        13779: "|cffe4cfa3Магия Скверны|r", 13780: "|cffe4cfa3Магия Скверны|r", 13781: "|cffe4cfa3Магия Скверны|r",
        13797: "|cffe4cfa3Магия Скверны|r", 13796: "|cffe4cfa3Магия Скверны|r", 13795: "|cffe4cfa3Магия Скверны|r",
        13782: "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 1|r] (|cffffffffW|r)",
        13783: "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 2|r] (|cffffffffW|r)",
        13784: "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 3|r] (|cffffffffW|r)",
        13800: "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 4|r] (|cffffffffW|r)",
        13799: "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 5|r] (|cffffffffW|r)",
        13798: "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 6|r] (|cffffffffW|r)",
        13785: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон магических атак и атак дальнего боя войск Легиона на |cffffffff+3|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deИнфернал|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        13786: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон магических атак и атак дальнего боя войск Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deИнфернал|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        13787: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон магических атак и атак дальнего боя войск Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+9|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deИнфернал|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        13801: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон магических атак и атак дальнего боя войск Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+12|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deИнфернал|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        13802: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон магических атак и атак дальнего боя войск Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+15|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deИнфернал|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        13803: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон магических атак и атак дальнего боя войск Легиона на |cffffffff+3|cffced4da ед. (всего |cffffffff+18|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deИнфернал|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",

        # R08M: Укрепление Скверной (h0DZ, 6 ур.)
        16328: "S", 16329: "S", 16331: "S", 16332: "S", 16335: "S", 16336: "S",
        13804: "|cffe4cfa3Укрепление Скверной|r", 13805: "|cffe4cfa3Укрепление Скверной|r", 13806: "|cffe4cfa3Укрепление Скверной|r",
        13815: "|cffe4cfa3Укрепление Скверной|r", 13814: "|cffe4cfa3Укрепление Скверной|r", 13813: "|cffe4cfa3Укрепление Скверной|r",
        13807: "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 1|r] (|cffffffffS|r)",
        13808: "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 2|r] (|cffffffffS|r)",
        13809: "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 3|r] (|cffffffffS|r)",
        13812: "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 4|r] (|cffffffffS|r)",
        13811: "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 5|r] (|cffffffffS|r)",
        13810: "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 6|r] (|cffffffffS|r)",
        12783: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню стрелков, осадных орудий и заклинателей Легиона на |cffffffff+2|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deТюремщик|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        12784: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню стрелков, осадных орудий и заклинателей Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+4|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deТюремщик|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        12786: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню стрелков, осадных орудий и заклинателей Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+6|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deТюремщик|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        12776: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню стрелков, осадных орудий и заклинателей Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+8|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deТюремщик|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        12777: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню стрелков, осадных орудий и заклинателей Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+10|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deТюремщик|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",
        12780: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню стрелков, осадных орудий и заклинателей Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+12|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deТюремщик|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r",

        # R08N: Познание Скверны (h0DZ, 6 ур.)
        18403: "D", 18405: "D", 18406: "D", 18407: "D", 18408: "D", 18432: "D",
        13829: "|cffe4cfa3Познание Скверны|r", 13830: "|cffe4cfa3Познание Скверны|r", 13831: "|cffe4cfa3Познание Скверны|r",
        13845: "|cffe4cfa3Познание Скверны|r", 13846: "|cffe4cfa3Познание Скверны|r", 13872: "|cffe4cfa3Познание Скверны|r",
        13875: "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 1|r] (|cffffffffD|r)",
        13876: "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 2|r] (|cffffffffD|r)",
        13898: "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 3|r] (|cffffffffD|r)",
        13909: "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 4|r] (|cffffffffD|r)",
        13910: "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 5|r] (|cffffffffD|r)",
        13911: "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 6|r] (|cffffffffD|r)",
        15205: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья войск Легиона на |cffffffff+40|cffced4da ед., ускоряет регенерацию здоровья на |cffffffff+1|cffced4da ед./сек. и регенерацию маны на |cffffffff+0.125|cffced4da ед./сек.|n|nЗатрагивает: все боевые единицы Легиона.|r",
        15206: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье на |cffffffff+40|cffced4da ед. (всего |cffffffff+80|cffced4da), регенерацию здоровья на |cffffffff+1|cffced4da (всего |cffffffff+2|cffced4da) и регенерацию маны на |cffffffff+0.125|cffced4da (всего |cffffffff+0.25|cffced4da).|n|nЗатрагивает: все боевые единицы Легиона.|r",
        15207: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье на |cffffffff+40|cffced4da ед. (всего |cffffffff+120|cffced4da), регенерацию здоровья на |cffffffff+1|cffced4da (всего |cffffffff+3|cffced4da) и регенерацию маны на |cffffffff+0.125|cffced4da (всего |cffffffff+0.375|cffced4da).|n|nЗатрагивает: все боевые единицы Легиона.|r",
        15208: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье на |cffffffff+40|cffced4da ед. (всего |cffffffff+160|cffced4da), регенерацию здоровья на |cffffffff+1|cffced4da (всего |cffffffff+4|cffced4da) и регенерацию маны на |cffffffff+0.125|cffced4da (всего |cffffffff+0.5|cffced4da).|n|nЗатрагивает: все боевые единицы Легиона.|r",
        15209: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье на |cffffffff+40|cffced4da ед. (всего |cffffffff+200|cffced4da), регенерацию здоровья на |cffffffff+1|cffced4da (всего |cffffffff+5|cffced4da) и регенерацию маны на |cffffffff+0.125|cffced4da (всего |cffffffff+0.625|cffced4da).|n|nЗатрагивает: все боевые единицы Легиона.|r",
        15210: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает здоровье на |cffffffff+40|cffced4da ед. (всего |cffffffff+240|cffced4da), регенерацию здоровья на |cffffffff+1|cffced4da (всего |cffffffff+6|cffced4da) и регенерацию маны на |cffffffff+0.125|cffced4da (всего |cffffffff+0.75|cffced4da).|n|nЗатрагивает: все боевые единицы Легиона.|r",

        # R0EG: Улучшенная добыча (h0DZ, 5 ур.)
        33628: "Z", 33810: "Z", 33827: "Z", 34384: "Z", 34397: "Z",
        22165: "|cffe4cfa3Улучшенная добыча|r", 22166: "|cffe4cfa3Улучшенная добыча|r", 22175: "|cffe4cfa3Улучшенная добыча|r",
        22176: "|cffe4cfa3Улучшенная добыча|r", 22177: "|cffe4cfa3Улучшенная добыча|r",
        22167: "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 1|r] (|cffffffffZ|r)",
        22168: "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 2|r] (|cffffffffZ|r)",
        22178: "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 3|r] (|cffffffffZ|r)",
        22179: "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 4|r] (|cffffffffZ|r)",
        22180: "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 5|r] (|cffffffffZ|r)",
        22181: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает вместимость переносимой рабочими древесины на |cffffffff+5|cffced4da ед. (всего |cffffffff+15|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАрхитектор Скверны|cffced4da.|r",
        22182: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает вместимость переносимой рабочими древесины на |cffffffff+5|cffced4da ед. (всего |cffffffff+20|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАрхитектор Скверны|cffced4da.|r",
        22183: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает вместимость переносимой рабочими древесины на |cffffffff+5|cffced4da ед. (всего |cffffffff+25|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАрхитектор Скверны|cffced4da.|r",

        # R08P: Древние знания эредаров (h0E0)
        17641: "A", 17642: "A",
        30833: "|cffe4cfa3Древние знания эредаров|r", 30834: "|cffe4cfa3Древние знания эредаров|r",
        30835: "|cffe4cfa3Древние знания эредаров|r (|cffffffffA|r)",
        30836: "|cffe4cfa3Древние знания эредаров|r (|cffffffffA|r)",
        12593: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Эредаров-чернокнижников способности «Перст боли», а также увеличивает их запас здоровья на |cffffffff+40|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет регенерацию маны.|n|nЗатрагивает: |cffa9c7deЭредар-чернокнижник|cffced4da.|r",
        12597: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Эредаров-чернокнижников способности «Перст боли», а также увеличивает их запас здоровья на |cffffffff+40|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет регенерацию маны.|n|nЗатрагивает: |cffa9c7deЭредар-чернокнижник|cffced4da.|r",

        # R08Q: Мастерство владения Скверной (h0E0, 3 ур.)
        12787: "S", 12810: "S", 13816: "S",
        12606: "|cffe4cfa3Мастерство владения Скверной|r", 12609: "|cffe4cfa3Мастерство владения Скверной|r", 12643: "|cffe4cfa3Мастерство владения Скверной|r",
        12612: "|cffe4cfa3Мастерство владения Скверной|r [|cffffffffУровень 1|r] (|cffffffffS|r)",
        12619: "|cffe4cfa3Мастерство владения Скверной|r [|cffffffffУровень 2|r] (|cffffffffS|r)",
        12644: "|cffe4cfa3Мастерство владения Скверной|r [|cffffffffУровень 3|r] (|cffffffffS|r)",
        15211: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Стражей ужаса способности «Огненный ливень», а также увеличивает их урон на |cffffffff+4|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deСтраж ужаса|cffced4da.|r",
        15212: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон Стражей ужаса на |cffffffff+4|cffced4da ед. (всего |cffffffff+8|cffced4da), запас маны на |cffffffff+100|cffced4da (всего |cffffffff+200|cffced4da) и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deСтраж ужаса|cffced4da.|r",
        15213: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает урон Стражей ужаса на |cffffffff+4|cffced4da ед. (всего |cffffffff+12|cffced4da), запас маны на |cffffffff+100|cffced4da (всего |cffffffff+300|cffced4da) и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deСтраж ужаса|cffced4da.|r",

        # R08R: Дрессировка зверей (h0E1)
        17665: "A", 13817: "A", 13818: "A",
        12709: "|cffe4cfa3Дрессировка зверей|r", 12710: "|cffe4cfa3Дрессировка зверей|r", 12720: "|cffe4cfa3Дрессировка зверей|r",
        12712: "|cffe4cfa3Дрессировка зверей|r (|cffffffffA|r)",
        12713: "|cffe4cfa3Дрессировка зверей|r (|cffffffffA|r)",
        12721: "|cffe4cfa3Дрессировка зверей|r (|cffffffffA|r)",
        12714: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон Ловчих Скверны на |cffffffff+4|cffced4da ед., запас здоровья на |cffffffff+75|cffced4da ед. и повышает их скорость боя на |cffffffff30%|cffced4da.|n|nЗатрагивает: |cffa9c7deЛовчий Скверны|cffced4da.|r",
        12639: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон Ловчих Скверны на |cffffffff+4|cffced4da ед., запас здоровья на |cffffffff+75|cffced4da ед. и повышает их скорость боя на |cffffffff30%|cffced4da.|n|nЗатрагивает: |cffa9c7deЛовчий Скверны|cffced4da.|r",
        12640: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон Ловчих Скверны на |cffffffff+4|cffced4da ед., запас здоровья на |cffffffff+75|cffced4da ед. и повышает их скорость боя на |cffffffff30%|cffced4da.|n|nЗатрагивает: |cffa9c7deЛовчий Скверны|cffced4da.|r",

        # R08S: Мастерство устрашения (h0E1)
        13826: "S", 13827: "S", 13828: "S",
        12729: "|cffe4cfa3Мастерство устрашения|r", 12730: "|cffe4cfa3Мастерство устрашения|r", 12738: "|cffe4cfa3Мастерство устрашения|r",
        12732: "|cffe4cfa3Мастерство устрашения|r (|cffffffffS|r)",
        12733: "|cffe4cfa3Мастерство устрашения|r (|cffffffffS|r)",
        12740: "|cffe4cfa3Мастерство устрашения|r (|cffffffffS|r)",
        12734: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Тюремщиков способности «Сон», а также увеличивает их урон на |cffffffff+4|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deТюремщик|cffced4da.|r",
        12645: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Тюремщиков способности «Сон», а также увеличивает их урон на |cffffffff+4|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deТюремщик|cffced4da.|r",
        12716: "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Тюремщиков способности «Сон», а также увеличивает их урон на |cffffffff+4|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deТюремщик|cffced4da.|r",
    }

    # Skin operations for war3mapSkin.w3q
    skin_w3q_ops = [
        # R08O name (shared WTS 2867 override)
        {"id": "R08O", "field": "name1", "value": "|cffe4cfa3Защита|r"},

        # R0EG inline ubertips for lvl 1 and 2
        {"id": "R0EG", "field": "ubertip1", "value": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает вместимость переносимой рабочими древесины на |cffffffff+5|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАрхитектор Скверны|cffced4da.|r"},
        {"id": "R0EG", "field": "ubertip2", "value": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно увеличивает вместимость переносимой рабочими древесины на |cffffffff+5|cffced4da ед. (всего |cffffffff+10|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deАрхитектор Скверны|cffced4da.|r"},

        # R08K ubertips for lvl 4, 5, 6
        {"id": "R08K", "field": "ubertip4", "value": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню воинов ближнего боя Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+8|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r"},
        {"id": "R08K", "field": "ubertip5", "value": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню воинов ближнего боя Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+10|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r"},
        {"id": "R08K", "field": "ubertip6", "value": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дополнительно усиливает броню воинов ближнего боя Легиона на |cffffffff+2|cffced4da ед. (всего |cffffffff+12|cffced4da ед.).|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r"},
    ]

    # Checks definition
    checks_def = [
        # R004
        {"id": "R004", "field": "name1", "expected": "|cffe4cfa3Эволюция: Кровавый палач|r"},
        {"id": "R004", "field": "tip1", "expected": "|cffe4cfa3Эволюция: Кровавый палач|r (|cffffffffS|r)"},
        {"id": "R004", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Трансформирует всех Властителей в более могучих Кровавых палачей, повышая их запас здоровья, урон и боевые характеристики.|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da.|r"},

        # R08H
        {"id": "R08H", "field": "name1", "expected": "|cffe4cfa3Эволюция: Кровавое отродье|r"},
        {"id": "R08H", "field": "tip1", "expected": "|cffe4cfa3Эволюция: Кровавое отродье|r (|cffffffffX|r)"},
        {"id": "R08H", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Трансформирует всех Кровавых палачей в свирепых Кровавых отродий, наделяя их пассивной способностью «Рассекающий удар» (25% урона по площади) и повышая характеристики.|n|nЗатрагивает: |cffa9c7deКровавый палач|cffced4da.|r"},

        # R08I
        {"id": "R08I", "field": "name1", "expected": "|cffe4cfa3Эволюция: Кровопускатель|r"},
        {"id": "R08I", "field": "tip1", "expected": "|cffe4cfa3Эволюция: Кровопускатель|r (|cffffffffC|r)"},
        {"id": "R08I", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Трансформирует всех Кровавых отродий в элитных демонических пехотинцев — Кровопускателей. Усиливает «Рассекающий удар» до 40% урона по площади и открывает возможность использовать способность «Укрыться за щитом».|n|nЗатрагивает: |cffa9c7deКровавое отродье|cffced4da.|r"},

        # R08O
        {"id": "R08O", "field": "name1", "expected": "|cffe4cfa3Защита|r"},
        {"id": "R08O", "field": "tip1", "expected": "|cffe4cfa3Защита|r (|cffffffffZ|r)"},
        {"id": "R08O", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Кровопускателей способности «Укрыться за щитом», позволяющей снижать урон от дальних пронзающих атак до 50% в обмен на снижение скорости передвижения на 30%.|n|nЗатрагивает: |cffa9c7deКровопускатель|cffced4da.|r"},

        # R08J
        {"id": "R08J", "field": "name1", "expected": "|cffe4cfa3Оружие Скверны|r"},
        {"id": "R08J", "field": "tip1", "expected": "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 1|r] (|cffffffffQ|r)"},
        {"id": "R08J", "field": "tip2", "expected": "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 2|r] (|cffffffffQ|r)"},
        {"id": "R08J", "field": "tip3", "expected": "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 3|r] (|cffffffffQ|r)"},
        {"id": "R08J", "field": "tip4", "expected": "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 4|r] (|cffffffffQ|r)"},
        {"id": "R08J", "field": "tip5", "expected": "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 5|r] (|cffffffffQ|r)"},
        {"id": "R08J", "field": "tip6", "expected": "|cffe4cfa3Оружие Скверны|r [|cffffffffУровень 6|r] (|cffffffffQ|r)"},
        {"id": "R08J", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон от атак воинов ближнего боя Легиона на |cffffffff+3|cffced4da ед.|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r"},

        # R08K
        {"id": "R08K", "field": "name1", "expected": "|cffe4cfa3Осквернённая броня|r"},
        {"id": "R08K", "field": "tip1", "expected": "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 1|r] (|cffffffffA|r)"},
        {"id": "R08K", "field": "tip2", "expected": "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 2|r] (|cffffffffA|r)"},
        {"id": "R08K", "field": "tip3", "expected": "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 3|r] (|cffffffffA|r)"},
        {"id": "R08K", "field": "tip4", "expected": "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 4|r] (|cffffffffA|r)"},
        {"id": "R08K", "field": "tip5", "expected": "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 5|r] (|cffffffffA|r)"},
        {"id": "R08K", "field": "tip6", "expected": "|cffe4cfa3Осквернённая броня|r [|cffffffffУровень 6|r] (|cffffffffA|r)"},
        {"id": "R08K", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню воинов ближнего боя Легиона на |cffffffff+2|cffced4da ед.|n|nЗатрагивает: |cffa9c7deВластитель|cffced4da, |cffa9c7deКровавый палач|cffced4da, |cffa9c7deКровавое отродье|cffced4da, |cffa9c7deКровопускатель|cffced4da, |cffa9c7deЗверь Саргераса|cffced4da, |cffa9c7deГромила Скверны|cffced4da.|r"},

        # R08L
        {"id": "R08L", "field": "name1", "expected": "|cffe4cfa3Магия Скверны|r"},
        {"id": "R08L", "field": "tip1", "expected": "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 1|r] (|cffffffffW|r)"},
        {"id": "R08L", "field": "tip2", "expected": "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 2|r] (|cffffffffW|r)"},
        {"id": "R08L", "field": "tip3", "expected": "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 3|r] (|cffffffffW|r)"},
        {"id": "R08L", "field": "tip4", "expected": "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 4|r] (|cffffffffW|r)"},
        {"id": "R08L", "field": "tip5", "expected": "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 5|r] (|cffffffffW|r)"},
        {"id": "R08L", "field": "tip6", "expected": "|cffe4cfa3Магия Скверны|r [|cffffffffУровень 6|r] (|cffffffffW|r)"},
        {"id": "R08L", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон магических атак и атак дальнего боя войск Легиона на |cffffffff+3|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deИнфернал|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r"},

        # R08M
        {"id": "R08M", "field": "name1", "expected": "|cffe4cfa3Укрепление Скверной|r"},
        {"id": "R08M", "field": "tip1", "expected": "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 1|r] (|cffffffffS|r)"},
        {"id": "R08M", "field": "tip2", "expected": "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 2|r] (|cffffffffS|r)"},
        {"id": "R08M", "field": "tip3", "expected": "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 3|r] (|cffffffffS|r)"},
        {"id": "R08M", "field": "tip4", "expected": "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 4|r] (|cffffffffS|r)"},
        {"id": "R08M", "field": "tip5", "expected": "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 5|r] (|cffffffffS|r)"},
        {"id": "R08M", "field": "tip6", "expected": "|cffe4cfa3Укрепление Скверной|r [|cffffffffУровень 6|r] (|cffffffffS|r)"},
        {"id": "R08M", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Усиливает броню стрелков, осадных орудий и заклинателей Легиона на |cffffffff+2|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАдская колесница|cffced4da, |cffa9c7deЭредар-чернокнижник|cffced4da, |cffa9c7deТюремщик|cffced4da, |cffa9c7deЛовчий Скверны|cffced4da, |cffa9c7deСтраж ужаса|cffced4da.|r"},

        # R08N
        {"id": "R08N", "field": "name1", "expected": "|cffe4cfa3Познание Скверны|r"},
        {"id": "R08N", "field": "tip1", "expected": "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 1|r] (|cffffffffD|r)"},
        {"id": "R08N", "field": "tip2", "expected": "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 2|r] (|cffffffffD|r)"},
        {"id": "R08N", "field": "tip3", "expected": "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 3|r] (|cffffffffD|r)"},
        {"id": "R08N", "field": "tip4", "expected": "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 4|r] (|cffffffffD|r)"},
        {"id": "R08N", "field": "tip5", "expected": "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 5|r] (|cffffffffD|r)"},
        {"id": "R08N", "field": "tip6", "expected": "|cffe4cfa3Познание Скверны|r [|cffffffffУровень 6|r] (|cffffffffD|r)"},
        {"id": "R08N", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья войск Легиона на |cffffffff+40|cffced4da ед., ускоряет регенерацию здоровья на |cffffffff+1|cffced4da ед./сек. и регенерацию маны на |cffffffff+0.125|cffced4da ед./сек.|n|nЗатрагивает: все боевые единицы Легиона.|r"},

        # R0EG
        {"id": "R0EG", "field": "name1", "expected": "|cffe4cfa3Улучшенная добыча|r"},
        {"id": "R0EG", "field": "tip1", "expected": "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 1|r] (|cffffffffZ|r)"},
        {"id": "R0EG", "field": "tip2", "expected": "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 2|r] (|cffffffffZ|r)"},
        {"id": "R0EG", "field": "tip3", "expected": "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 3|r] (|cffffffffZ|r)"},
        {"id": "R0EG", "field": "tip4", "expected": "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 4|r] (|cffffffffZ|r)"},
        {"id": "R0EG", "field": "tip5", "expected": "|cffe4cfa3Улучшенная добыча|r [|cffffffffУровень 5|r] (|cffffffffZ|r)"},
        {"id": "R0EG", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает вместимость переносимой рабочими древесины на |cffffffff+5|cffced4da ед.|n|nЗатрагивает: |cffa9c7deАрхитектор Скверны|cffced4da.|r"},

        # R08P
        {"id": "R08P", "field": "name1", "expected": "|cffe4cfa3Древние знания эредаров|r"},
        {"id": "R08P", "field": "tip1", "expected": "|cffe4cfa3Древние знания эредаров|r (|cffffffffA|r)"},
        {"id": "R08P", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Эредаров-чернокнижников способности «Перст боли», а также увеличивает их запас здоровья на |cffffffff+40|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет регенерацию маны.|n|nЗатрагивает: |cffa9c7deЭредар-чернокнижник|cffced4da.|r"},

        # R08Q
        {"id": "R08Q", "field": "name1", "expected": "|cffe4cfa3Мастерство владения Скверной|r"},
        {"id": "R08Q", "field": "tip1", "expected": "|cffe4cfa3Мастерство владения Скверной|r [|cffffffffУровень 1|r] (|cffffffffS|r)"},
        {"id": "R08Q", "field": "tip2", "expected": "|cffe4cfa3Мастерство владения Скверной|r [|cffffffffУровень 2|r] (|cffffffffS|r)"},
        {"id": "R08Q", "field": "tip3", "expected": "|cffe4cfa3Мастерство владения Скверной|r [|cffffffffУровень 3|r] (|cffffffffS|r)"},
        {"id": "R08Q", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Стражей ужаса способности «Огненный ливень», а также увеличивает их урон на |cffffffff+4|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deСтраж ужаса|cffced4da.|r"},

        # R08R
        {"id": "R08R", "field": "name1", "expected": "|cffe4cfa3Дрессировка зверей|r"},
        {"id": "R08R", "field": "tip1", "expected": "|cffe4cfa3Дрессировка зверей|r (|cffffffffA|r)"},
        {"id": "R08R", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон Ловчих Скверны на |cffffffff+4|cffced4da ед., запас здоровья на |cffffffff+75|cffced4da ед. и повышает их скорость боя на |cffffffff30%|cffced4da.|n|nЗатрагивает: |cffa9c7deЛовчий Скверны|cffced4da.|r"},

        # R08S
        {"id": "R08S", "field": "name1", "expected": "|cffe4cfa3Мастерство устрашения|r"},
        {"id": "R08S", "field": "tip1", "expected": "|cffe4cfa3Мастерство устрашения|r (|cffffffffS|r)"},
        {"id": "R08S", "field": "ubertip1", "expected": "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Обучает Тюремщиков способности «Сон», а также увеличивает их урон на |cffffffff+4|cffced4da ед., запас маны на |cffffffff+100|cffced4da ед. и ускоряет восстановление маны.|n|nЗатрагивает: |cffa9c7deТюремщик|cffced4da.|r"}
    ]

    plan = {
        "wts_updates": {str(k): v for k, v in wts_updates.items()},
        "skin_w3q_ops": skin_w3q_ops,
        "checks_def": checks_def
    }

    out_path = ROOT / "docs/ui_text/demon_research_plan.json"
    out_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated research plan with {len(wts_updates)} WTS updates, {len(skin_w3q_ops)} skin_w3q ops, and {len(checks_def)} checks.")

if __name__ == "__main__":
    build_plan()
