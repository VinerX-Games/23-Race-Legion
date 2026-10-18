# -*- coding: utf-8 -*-
"""Prepare complete standardization plan and registries for Fel Orcs (Race 31)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

# Static mapping of object fields to WTS string IDs
BY_CAT = {   'abilities': {   'A01C': [('name', 2038), ('tip1', 2039)],
                     'A0B7': [   ('name', 8169),
                                 ('tip1', 8170),
                                 ('tip2', 8172),
                                 ('ubertip2', 10177),
                                 ('ubertip1', 10178),
                                 ('researchtip', 10179),
                                 ('researchubertip', 10197)],
                     'A0BE': [   ('name', 8252),
                                 ('tip1', 8253),
                                 ('researchtip', 8254),
                                 ('tip2', 8256),
                                 ('tip3', 8257),
                                 ('tip4', 8258),
                                 ('ubertip4', 13534),
                                 ('researchubertip', 15470),
                                 ('ubertip2', 15471),
                                 ('ubertip3', 15472),
                                 ('ubertip1', 15474)],
                     'A0EN': [   ('name', 328),
                                 ('researchtip', 329),
                                 ('tip1', 331),
                                 ('tip2', 332),
                                 ('tip3', 333),
                                 ('tip4', 334),
                                 ('ubertip1', 15346),
                                 ('ubertip2', 15347),
                                 ('ubertip3', 15348),
                                 ('ubertip4', 35263),
                                 ('researchubertip', 35266)],
                     'A0I3': [   ('researchtip', 10064),
                                 ('researchubertip', 10976),
                                 ('tip1', 26476),
                                 ('ubertip1', 26477),
                                 ('name', 26484)],
                     'A0IQ': [('name', 27193), ('tip1', 27969), ('ubertip1', 27970)],
                     'A0LI': [('name', 2888), ('tip1', 3692), ('ubertip1', 20630)],
                     'A0LJ': [('name', 12857), ('tip1', 12886), ('ubertip1', 20631)],
                     'A0N7': [   ('name', 12036),
                                 ('tip3', 12040),
                                 ('researchtip', 12831),
                                 ('tip2', 13207),
                                 ('tip1', 13211),
                                 ('ubertip2', 13224),
                                 ('ubertip1', 13245),
                                 ('ubertip3', 13249),
                                 ('tip4', 13261),
                                 ('researchubertip', 29002),
                                 ('ubertip4', 30564)],
                     'A14L': [('name', 27493), ('tip1', 27494), ('ubertip1', 27502)],
                     'A1HW': [('name', 24916), ('tip1', 25175), ('ubertip1', 34734)],
                     'A1HX': [('name', 34458), ('tip1', 34459), ('ubertip1', 34753)],
                     'A1HY': [('name', 30203), ('tip1', 30243), ('ubertip1', 35501)],
                     'A1HZ': [('name', 34240), ('tip1', 34241), ('ubertip1', 35236)],
                     'A1I0': [('name', 34555), ('tip1', 34556), ('ubertip1', 35838)],
                     'A1I1': [('name', 34247), ('tip1', 34248), ('ubertip1', 35839)],
                     'A1I2': [('name', 9353), ('tip1', 12215), ('ubertip1', 35840)],
                     'A1I3': [('ubertip1', 23431), ('name', 26566), ('tip1', 26571)],
                     'A1II': [   ('tip4', 35906),
                                 ('ubertip4', 35907),
                                 ('name', 35908),
                                 ('researchtip', 35909),
                                 ('researchubertip', 35910),
                                 ('tip1', 35911),
                                 ('tip2', 35912),
                                 ('tip3', 35913)],
                     'A1IM': [('name', 28119), ('tip1', 28127), ('ubertip1', 35753)],
                     'A1IN': [('name', 34538), ('tip1', 34539), ('ubertip1', 35754)],
                     'A1IO': [('name', 31567), ('tip1', 32051), ('ubertip1', 35755)],
                     'A1IP': [('name', 34242), ('tip1', 35017), ('ubertip1', 35756)],
                     'A1IQ': [('name', 34557), ('tip1', 34561), ('ubertip1', 35757)],
                     'A1IR': [('name', 34249), ('tip1', 34257), ('ubertip1', 35758)],
                     'A1IS': [('name', 12302), ('tip1', 12845), ('ubertip1', 35769)],
                     'A1IT': [('name', 26581), ('tip1', 26601), ('ubertip1', 35770)],
                     'A1IU': [('ubertip1', 30229), ('name', 36339), ('tip1', 36340)],
                     'A1IV': [('ubertip1', 36342)],
                     'A1IW': [('ubertip1', 36344)],
                     'A1IX': [('ubertip1', 36345)],
                     'A1IY': [('ubertip1', 36347)],
                     'A1IZ': [('name', 36348), ('tip1', 36349), ('ubertip1', 36350)],
                     'A1J1': [('tip1', 26991), ('name', 26997), ('ubertip1', 26998)],
                     'A1J3': [('ubertip1', 26999)],
                     'A1J4': [('ubertip1', 37641)],
                     'A1J5': [('name', 30230), ('tip1', 30231), ('ubertip1', 30296)],
                     'A1J7': [('tip1', 36597), ('ubertip1', 36598)],
                     'A1J8': [   ('ubertip2', 19976),
                                 ('ubertip3', 21300),
                                 ('ubertip1', 31220),
                                 ('ubertip4', 32754),
                                 ('name', 35204),
                                 ('researchtip', 35281),
                                 ('tip1', 35283),
                                 ('tip2', 35285),
                                 ('tip3', 35289),
                                 ('tip4', 35295),
                                 ('researchubertip', 35316)],
                     'A1J9': [   ('name', 36680),
                                 ('researchubertip', 37034),
                                 ('researchtip', 37035),
                                 ('ubertip1', 37036),
                                 ('ubertip2', 37037)],
                     'A1JG': [('ubertip2', 7614), ('tip2', 11947)],
                     'A1JH': [('name', 11982), ('tip1', 11983), ('ubertip1', 23530)],
                     'A1JI': [('name', 11987), ('tip1', 23429), ('ubertip1', 35841)],
                     'A1JK': [   ('name', 14299),
                                 ('researchtip', 14300),
                                 ('ubertip1', 15269),
                                 ('ubertip2', 15270),
                                 ('researchubertip', 15273),
                                 ('tip2', 15961),
                                 ('tip3', 17725),
                                 ('tip4', 17731),
                                 ('ubertip3', 17797),
                                 ('ubertip4', 17800),
                                 ('tip1', 26358)],
                     'A1JL': [('ubertip1', 25691), ('name', 38915), ('tip1', 38916)],
                     'A1JP': [('ubertip1', 39228)],
                     'A1KB': [('name', 38201), ('tip1', 38229)],
                     'A1MC': [('ubertip1', 22257), ('name', 39203), ('tip1', 39204)],
                     'A1MD': [   ('researchubertip', 8749),
                                 ('name', 39207),
                                 ('tip1', 39209),
                                 ('tip2', 39210),
                                 ('tip3', 39211),
                                 ('tip4', 39212),
                                 ('ubertip4', 39213),
                                 ('ubertip1', 39214),
                                 ('ubertip2', 39215),
                                 ('ubertip3', 39216)],
                     'AOcr': [('ubertip4', 5166), ('tip4', 9628)],
                     'AOwk': [('ubertip4', 20908), ('tip4', 23502)],
                     'AOww': [('tip2', 9617), ('ubertip2', 23512)],
                     'Aabr': [('ubertip1', 7613)]},
    'buildings': {   'h0D3': [('name', 10901), ('tip', 10902), ('ubertip', 22662)],
                     'o05T': [('ubertip', 30681)],
                     'o05V': [('ubertip', 20727)],
                     'o05W': [('ubertip', 21453)],
                     'o05X': [('ubertip', 25409)],
                     'o05Y': [('ubertip', 28995), ('name', 33453), ('tip', 33905)],
                     'o05Z': [('ubertip', 28988)],
                     'o060': [('ubertip', 31830), ('name', 33924), ('tip', 33925)],
                     'o061': [('ubertip', 30653)],
                     'o062': [('tip', 22879), ('ubertip', 30660)],
                     'o066': [('ubertip', 30686), ('name', 34730), ('tip', 34732)],
                     'o067': [('name', 3807), ('ubertip', 30687), ('tip', 33444)],
                     'owtw': [('name', 36068), ('tip', 36069)]},
    'heroes': {   'N06P': [   ('name', 3617),
                              ('propernames', 3618),
                              ('awakentip', 35901),
                              ('tip', 35902),
                              ('revivetip', 35903),
                              ('ubertip', 37008)],
                  'N072': [   ('propernames', 35020),
                              ('name', 35033),
                              ('tip', 35075),
                              ('awakentip', 36706),
                              ('ubertip', 37009)],
                  'N073': [   ('name', 30703),
                              ('awakentip', 36705),
                              ('propernames', 36968),
                              ('tip', 36976),
                              ('ubertip', 37010)]},
    'markers': {   'R0KA': [('ubertip1', 26689), ('name1', 37022), ('tip1', 37023)],
                   'R0KC': [('name1', 5595), ('tip1', 5596), ('ubertip1', 27305)]},
    'selection': {'A1JL': [('ubertip1', 25691), ('name', 38915), ('tip1', 38916)]},
    'units': {   'h0D5': [('ubertip', 6926), ('name', 10916), ('tip', 10918)],
                 'h0D6': [('name', 3002), ('ubertip', 5542)],
                 'n067': [('ubertip', 10616)],
                 'n068': [('ubertip', 15344)],
                 'n069': [('ubertip', 15345)],
                 'n06A': [('ubertip', 33385)],
                 'n06B': [('ubertip', 29065)],
                 'n06C': [('name', 17861), ('ubertip', 33386), ('tip', 34537)],
                 'n06D': [('name', 20943), ('ubertip', 33387), ('tip', 34261)],
                 'n06F': [('name', 30675), ('ubertip', 35248), ('tip', 35722)],
                 'n06G': [('name', 26975), ('tip', 34565), ('ubertip', 35251)],
                 'n06I': [('ubertip', 35254)],
                 'n06J': [('name', 34551), ('tip', 35723), ('ubertip', 36712)],
                 'n06K': [('ubertip', 36713)],
                 'n06L': [('ubertip', 36714)],
                 'n06M': [('name', 31903), ('tip', 35721), ('ubertip', 36715)],
                 'n06N': [('ubertip', 36718)],
                 'n06O': [('name', 34385), ('tip', 35720), ('ubertip', 36719)],
                 'n06Q': [('name', 35808), ('tip', 35810), ('ubertip', 36720)],
                 'n06R': [('ubertip', 36721)],
                 'n06S': [('name', 35814), ('tip', 35816), ('ubertip', 36722)],
                 'n06T': [('ubertip', 36723)],
                 'n06U': [('ubertip', 36724)],
                 'n06V': [('ubertip', 36725)],
                 'n06W': [('name', 35804), ('tip', 35805), ('ubertip', 36728)],
                 'n070': [('name', 36729), ('tip', 36730), ('ubertip', 36731)],
                 'o05Q': [('tip', 33391), ('name', 33452), ('ubertip', 35245)],
                 'o05R': [('ubertip', 29076)],
                 'o063': [('name', 34547), ('tip', 36716), ('ubertip', 36717)],
                 'o065': [('name', 35812), ('tip', 36726), ('ubertip', 36727)]},
    'upgrades': {   'R00Y': [('ubertip1', 20159)],
                    'R0JQ': [   ('name4', 22737),
                                ('name5', 22738),
                                ('name6', 22739),
                                ('tip4', 22740),
                                ('tip5', 22741),
                                ('tip6', 22742),
                                ('ubertip4', 31052),
                                ('ubertip5', 31053),
                                ('ubertip6', 31054),
                                ('ubertip1', 31055),
                                ('ubertip2', 31056),
                                ('ubertip3', 31057)],
                    'R0JR': [   ('name4', 22754),
                                ('name5', 22755),
                                ('name6', 22756),
                                ('tip4', 22757),
                                ('tip5', 22758),
                                ('tip6', 22759),
                                ('ubertip1', 28247),
                                ('ubertip2', 28248),
                                ('ubertip3', 28249),
                                ('ubertip4', 28250),
                                ('ubertip5', 28251),
                                ('ubertip6', 28252),
                                ('name1', 29426)],
                    'R0JS': [   ('name1', 20134),
                                ('name4', 22769),
                                ('name5', 22770),
                                ('name6', 22771),
                                ('tip4', 31575),
                                ('tip5', 31576),
                                ('tip6', 31969),
                                ('ubertip1', 31972),
                                ('ubertip2', 31973),
                                ('ubertip3', 31974),
                                ('ubertip4', 31975),
                                ('ubertip5', 31976),
                                ('ubertip6', 31977)],
                    'R0JU': [   ('ubertip1', 30348),
                                ('ubertip2', 30402),
                                ('ubertip3', 33003),
                                ('name3', 33426),
                                ('tip3', 33429),
                                ('name1', 33573),
                                ('name2', 33583),
                                ('tip1', 34160),
                                ('tip2', 34161)],
                    'R0JV': [   ('ubertip1', 25331),
                                ('name3', 25332),
                                ('tip3', 25334),
                                ('ubertip2', 36524),
                                ('ubertip3', 36528),
                                ('name1', 36530),
                                ('name2', 36531),
                                ('tip1', 36533),
                                ('tip2', 36534)],
                    'R0JW': [('ubertip1', 36537), ('name1', 36546), ('tip1', 36548)],
                    'R0JX': [   ('ubertip1', 34162),
                                ('ubertip2', 34163),
                                ('name1', 34164),
                                ('name2', 34165),
                                ('tip1', 34166),
                                ('tip2', 34167)],
                    'R0JY': [('ubertip1', 36565)],
                    'R0JZ': [   ('name1', 34168),
                                ('name2', 34346),
                                ('tip1', 35872),
                                ('tip2', 36105),
                                ('ubertip1', 36568),
                                ('ubertip2', 36572)],
                    'R0K0': [   ('ubertip1', 36583),
                                ('ubertip2', 36587),
                                ('ubertip3', 36588),
                                ('name3', 36589),
                                ('tip3', 36590),
                                ('name1', 36592),
                                ('name2', 36593),
                                ('tip1', 36594),
                                ('tip2', 36595)],
                    'R0K1': [   ('name1', 36520),
                                ('ubertip2', 36756),
                                ('ubertip3', 36757),
                                ('ubertip4', 36758),
                                ('ubertip5', 36759),
                                ('ubertip6', 36760),
                                ('ubertip1', 36761),
                                ('name3', 37390),
                                ('name4', 37486),
                                ('name5', 37594),
                                ('name6', 38549),
                                ('tip1', 38572),
                                ('tip3', 39059),
                                ('tip4', 39350),
                                ('tip5', 39357),
                                ('tip6', 39824),
                                ('name2', 39877),
                                ('tip2', 39928)],
                    'R0K2': [   ('ubertip1', 11069),
                                ('ubertip2', 20381),
                                ('ubertip3', 20384),
                                ('ubertip4', 20386),
                                ('ubertip5', 24421),
                                ('ubertip6', 24539),
                                ('name3', 36771),
                                ('tip3', 36772),
                                ('name1', 36774),
                                ('name2', 36775),
                                ('tip1', 36776),
                                ('tip2', 36777),
                                ('name4', 36778),
                                ('name5', 36779),
                                ('name6', 36780),
                                ('tip4', 36785),
                                ('tip5', 36786),
                                ('tip6', 36787)],
                    'R0K3': [   ('ubertip1', 24546),
                                ('ubertip2', 24549),
                                ('ubertip3', 24550),
                                ('ubertip4', 24884),
                                ('ubertip5', 24885),
                                ('ubertip6', 25424),
                                ('name3', 36806),
                                ('tip3', 36807),
                                ('name1', 36809),
                                ('name2', 36810),
                                ('tip1', 36811),
                                ('tip2', 36812),
                                ('name4', 36813),
                                ('name5', 36814),
                                ('name6', 36815),
                                ('tip4', 36820),
                                ('tip5', 36821),
                                ('tip6', 36822)],
                    'R0K5': [   ('ubertip1', 25326),
                                ('ubertip2', 25330),
                                ('name1', 39974),
                                ('name2', 39975),
                                ('tip1', 39980),
                                ('tip2', 39982)],
                    'R0K6': [('ubertip1', 26495)],
                    'R0K7': [('ubertip1', 28946)],
                    'R0KA': [('ubertip1', 26689), ('name1', 37022), ('tip1', 37023)],
                    'R0KC': [('name1', 5595), ('tip1', 5596), ('ubertip1', 27305)],
                    'Roen': [('name1', 26346), ('tip1', 26347), ('ubertip1', 26366)],
                    'Ropg': [('name1', 22401), ('tip1', 22402), ('ubertip1', 22403)]}}

def main():
    folder = ROOT / "docs/ui_text"
    folder.mkdir(parents=True, exist_ok=True)

    wts_updates = {}
    checks_def = []

    def add_u(sid, text, check=None):
        assert sid not in wts_updates, f"Duplicate sid {sid}"
        wts_updates[sid] = text
        if check:
            if check.get("expected") is None:
                check["expected"] = text
            checks_def.append(check)

    # =========================================================================
    # 1. SELECTION & MARKERS (6 SIDs, 9 references)
    # =========================================================================
    # A1JL
    add_u(38915, "|cffe4cfa3Орда Скверны|r", {"type": "ability", "id": "A1JL", "field": "name", "expected": "|cffe4cfa3Орда Скверны|r"})
    add_u(38916, "|cffe4cfa3Орда Скверны|r (|cffffffffC|r)", {"type": "ability", "id": "A1JL", "field": "tip1", "expected": "|cffe4cfa3Орда Скверны|r (|cffffffffC|r)"})
    add_u(25691, (
        "|cffa6afb8РАСА:|cffced4da Свирепые орки Дренора, порабощённые демонической скверной, обладающие несокрушимой яростью, тёмной магией и разрушительными осадными машинами.|r|n|n"
        "|cffa6afb8Создатель расы:|r |cffa9c7deEscanor(Яхве)|r|n"
        "|cffa6afb8Куратор расы:|r |cffa9c7deNiCAmCHiK|r|n"
        "|cffa6afb8Сложность:|r |cffffffff●●●|cffa6afb8○○|r|n"
        "|cffa6afb8Период:|r |cffa9c7de«Warcraft III — Battle for Azeroth»|r|n|n"
        "|cffced4daОрда Скверны — орки Дренора, испившие демонической крови и подчинившиеся владыкам Пылающего Легиона и властителю Преисподней Магтеридону. "
        "Изменившись под воздействием скверны, они обрели кроваво-красную кожу, чудовищную силу и неутолимую жажду битвы. "
        "Опираясь на свирепых рубак, чернокнижников, налётчиков и некромантию, Орда Скверны сокрушает любые преграды на своём пути.|r"
    ), {"type": "ability", "id": "A1JL", "field": "ubertip1", "expected": None})
    
    # Marker R0KA
    add_u(37022, "|cffe4cfa3Орда Скверны|r", {"type": "upgrade", "id": "R0KA", "field": "name1", "expected": "|cffe4cfa3Орда Скверны|r"})
    add_u(37023, "|cffe4cfa3Орда Скверны|r", {"type": "upgrade", "id": "R0KA", "field": "tip1", "expected": "|cffe4cfa3Орда Скверны|r"})
    add_u(26689, "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Орде Скверны.|r", {"type": "upgrade", "id": "R0KA", "field": "ubertip1", "expected": None})
    
    # Marker R0KC
    add_u(5595, "|cffe4cfa3Орда Скверны|r", {"type": "upgrade", "id": "R0KC", "field": "name1", "expected": "|cffe4cfa3Орда Скверны|r"})
    add_u(5596, "|cffe4cfa3Орда Скверны|r", {"type": "upgrade", "id": "R0KC", "field": "tip1", "expected": "|cffe4cfa3Орда Скверны|r"})
    add_u(27305, "|cffa6afb8ТЕХНОЛОГИЯ:|cffced4da Служебный маркер фракционной принадлежности к Орде Скверны или Орде Второй Войны.|r", {"type": "upgrade", "id": "R0KC", "field": "ubertip1", "expected": None})
    
    # =========================================================================
    # 2. BUILDINGS (25 SIDs across 13 buildings)
    # =========================================================================
    # o05V: Дом вождей (Q)
    add_u(20727, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание первой ступени. Обеспечивает добычу ресурсов и начальный лимит пищи.|n|n"
        "Даёт |cffffffff50|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБатрак Скверны|cffced4da: базовый рабочий.|n"
        "- |cffa9c7deМутировавший Батрак|cffced4da: рабочий-воин с рассекающим ударом.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deГрабеж|cffced4da: воины добывают золото при атаке зданий.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deКрепость|cffced4da: открывает доступ к передовым сооружениям и войскам.|r"
    ), {"type": "unit", "id": "o05V", "field": "ubertip", "expected": None})
    
    # o05W: Крепость (U)
    add_u(21453, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание второй ступени. Существенно увеличивает запас пищи и открывает доступ к новым постройкам.|n|n"
        "Даёт |cffffffff100|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБатрак Скверны|cffced4da: базовый рабочий.|n"
        "- |cffa9c7deМутировавший Батрак|cffced4da: рабочий-воин с рассекающим ударом.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deГрабеж|cffced4da: воины добывают золото при атаке зданий.|n|n"
        "|cffa6afb8Улучшение:|cffced4da|n- |cffa9c7deЦитадель|cffced4da: открывает доступ к высшим технологиям расы.|r"
    ), {"type": "unit", "id": "o05W", "field": "ubertip", "expected": None})
    
    # o05X: Цитадель (U)
    add_u(25409, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Главное здание третьей ступени. Обеспечивает максимальный запас пищи и открывает все технологии расы.|n|n"
        "Даёт |cffffffff150|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deБатрак Скверны|cffced4da: базовый рабочий.|n"
        "- |cffa9c7deМутировавший Батрак|cffced4da: рабочий-воин с рассекающим ударом.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deГрабеж|cffced4da: воины добывают золото при атаке зданий.|r"
    ), {"type": "unit", "id": "o05X", "field": "ubertip", "expected": None})
    
    # o060: Свиноферма (A)
    add_u(33924, "|cffe4cfa3Свиноферма|r", {"type": "unit", "id": "o060", "field": "name", "expected": "|cffe4cfa3Свиноферма|r"})
    add_u(33925, "|cffe4cfa3Свиноферма|r (|cffffffffA|r)", {"type": "unit", "id": "o060", "field": "tip", "expected": "|cffe4cfa3Свиноферма|r (|cffffffffA|r)"})
    add_u(31830, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Обеспечивает армию Орды Скверны провизией. Позволяет укрывать батраков для защиты базы.|n|n"
        "Даёт |cffffffff40|cffced4da ед. лимита пищи.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели|cffced4da (при укрытии батраков).|r"
    ), {"type": "unit", "id": "o060", "field": "ubertip", "expected": None})
    
    # o05Y: Алтарь скверны (S)
    add_u(33453, "|cffe4cfa3Алтарь скверны|r", {"type": "unit", "id": "o05Y", "field": "name", "expected": "|cffe4cfa3Алтарь скверны|r"})
    add_u(33905, "|cffe4cfa3Алтарь скверны|r (|cffffffffS|r)", {"type": "unit", "id": "o05Y", "field": "tip", "expected": "|cffe4cfa3Алтарь скверны|r (|cffffffffS|r)"})
    add_u(28995, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Позволяет призывать и воскрешать павших героев Орды Скверны.|n|n"
        "|cffa6afb8Герои:|cffced4da|n- |cffa9c7deВоенный лорд|cffced4da: герой-воин ближнего боя (Сила).|n"
        "- |cffa9c7deМастер меча|cffced4da: мастер клинка ближнего боя (Ловкость).|n"
        "- |cffa9c7deОскверненный шаман|cffced4da: темный шаман дальнего боя (Интеллект).|r"
    ), {"type": "unit", "id": "o05Y", "field": "ubertip", "expected": None})
    
    # o05Z: Казармы (W)
    add_u(28988, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Базовое производственное сооружение Орды Скверны. Подготавливает пехоту, стрелков и осадные орудия.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deРубака Скверны|cffced4da: базовый боец ближнего боя.|n"
        "- |cffa9c7deСтрелок|cffced4da: стрелок с арбалетом.|n"
        "- |cffa9c7deКопьеметатель|cffced4da: метатель копий дальнего боя.|n"
        "- |cffa9c7deТелохранитель вождя|cffced4da: тяжелый воин с аурой защиты.|n"
        "- |cffa9c7deРазрушитель|cffced4da: осадная катапульта дальнего боя.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deГорючая смесь|cffced4da: поджигает землю при атаке разрушителей.|n"
        "- |cffa9c7deГрубая сила|cffced4da: повышает здоровье и урон рубак.|n"
        "- |cffa9c7deСверхлегкие копья|cffced4da: увеличивает дальность атаки копьеметателей.|n"
        "- |cffa9c7deЗаточеный болт|cffced4da: повышает урон стрелков по тяжелой броне.|r"
    ), {"type": "unit", "id": "o05Z", "field": "ubertip", "expected": None})
    
    # o05T: Лесопилка (R)
    add_u(30681, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Служит пунктом сбора древесины и центром кузнечных разработок Орды Скверны.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОружие ближнего боя|cffced4da: повышает урон немагических войск ближнего боя.|n"
        "- |cffa9c7deОружие дальнего боя|cffced4da: повышает урон войск дальнего боя.|n"
        "- |cffa9c7deСтальная броня|cffced4da: повышает броню воинов ближнего боя.|n"
        "- |cffa9c7deУлучшенные пилы|cffced4da: увеличивает сбор древесины батраками.|n"
        "- |cffa9c7deПоощрять ярость|cffced4da: увеличивает урон бойцов ценой снижения здоровья.|n"
        "- |cffa9c7deПодавлять ярость|cffced4da: увеличивает здоровье бойцов ценой снижения урона.|n"
        "- |cffa9c7deГрабеж|cffced4da: воины добывают золото при атаке зданий.|r"
    ), {"type": "unit", "id": "o05T", "field": "ubertip", "expected": None})
    
    # o061: Обитель духов (D)
    add_u(30653, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Подготавливает могущественных заклинателей и магов поддержки Орды Скверны.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deЧернокнижник Скверны|cffced4da: темный маг с рассеиванием и огненной стрелой.|n"
        "- |cffa9c7deШаман|cffced4da: заклинатель с раздвоенной молнией и жаждой крови.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбучение шаманов|cffced4da: открывает новые ранги и способности шаманов.|n"
        "- |cffa9c7deЧерная магия|cffced4da: открывает новые ранги и способности чернокнижников.|r"
    ), {"type": "unit", "id": "o061", "field": "ubertip", "expected": None})
    
    # o062: Зверинец (E)
    add_u(22879, "|cffe4cfa3Зверинец|r (|cffffffffE|r)", {"type": "unit", "id": "o062", "field": "tip", "expected": "|cffe4cfa3Зверинец|r (|cffffffffE|r)"})
    add_u(30660, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Содержит и тренирует боевых зверей, кавалерию и элитную охрану Орды Скверны.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deНалетчик Скверны|cffced4da: быстрая волчья кавалерия с опутыванием и воем.|n"
        "- |cffa9c7deКодо Скверны|cffced4da: массивный зверь с пожиранием и аурой выносливости.|n"
        "- |cffa9c7deТелохранитель вождя|cffced4da: элитный тяжелый воин с аурой защиты.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deТренировки с волками|cffced4da: повышает скорость и урон налетчиков.|n"
        "- |cffa9c7deОбучение телохранителя|cffced4da: усиливает телохранителей вождя.|n"
        "- |cffa9c7deТренировки кодо|cffced4da: увеличивает запас здоровья и урон боевых кодо.|r"
    ), {"type": "unit", "id": "o062", "field": "ubertip", "expected": None})
    
    # o066: Оскверненный источник (X)
    add_u(34730, "|cffe4cfa3Оскверненный источник|r", {"type": "unit", "id": "o066", "field": "name", "expected": "|cffe4cfa3Оскверненный источник|r"})
    add_u(34732, "|cffe4cfa3Оскверненный источник|r (|cffffffffX|r)", {"type": "unit", "id": "o066", "field": "tip", "expected": "|cffe4cfa3Оскверненный источник|r (|cffffffffX|r)"})
    add_u(30686, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Мистический источник демонической энергии. Насыщает войска Скверной и открывает ритуалы развития армии.|n|n"
        "|cffa6afb8Ритуалы:|cffced4da|n- |cffa9c7deРитуал некромантии|cffced4da: открывает постройку Чертогов мертвых.|n"
        "- |cffa9c7deРитуал мутации|cffced4da: открывает обучение Мутировавших батраков.|n|n"
        "|cffa6afb8Улучшения:|cffced4da|n- Позволяет улучшать войска Орды Скверны до третьего ранга.|r"
    ), {"type": "unit", "id": "o066", "field": "ubertip", "expected": None})
    
    # o067: Чертоги мертвых (F)
    add_u(3807, "|cffe4cfa3Чертоги мертвых|r", {"type": "unit", "id": "o067", "field": "name", "expected": "|cffe4cfa3Чертоги мертвых|r"})
    add_u(33444, "|cffe4cfa3Чертоги мертвых|r (|cffffffffF|r)", {"type": "unit", "id": "o067", "field": "tip", "expected": "|cffe4cfa3Чертоги мертвых|r (|cffffffffF|r)"})
    add_u(30687, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Центр изучения тёмных искусств и некромантии Орды Скверны.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deНекромант|cffced4da: темный маг, поднимающий скелетов из трупов.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deИскусное воскрешение|cffced4da: позволяет призывать скелетов-защитников.|n"
        "- |cffa9c7deЖивучие скелеты|cffced4da: увеличивает длительность существования скелетов.|r"
    ), {"type": "unit", "id": "o067", "field": "ubertip", "expected": None})
    
    # h0D3: Верфь (C)
    add_u(10901, "|cffe4cfa3Верфь|r", {"type": "unit", "id": "h0D3", "field": "name", "expected": "|cffe4cfa3Верфь|r"})
    add_u(10902, "|cffe4cfa3Верфь|r (|cffffffffC|r)", {"type": "unit", "id": "h0D3", "field": "tip", "expected": "|cffe4cfa3Верфь|r (|cffffffffC|r)"})
    add_u(22662, (
        "|cffa6afb8ЗДАНИЕ:|cffced4da Строит корабли и исследует улучшения морского флота.|n|n"
        "|cffa6afb8Обучает:|cffced4da|n- |cffa9c7deТранспорт|cffced4da: перевозка сухопутных войск по воде.|n"
        "- |cffa9c7deФрегат|cffced4da: патрульный артиллерийский корабль.|n"
        "- |cffa9c7deДредноут|cffced4da: тяжелый бронированный флагман флота.|n|n"
        "|cffa6afb8Исследования:|cffced4da|n- |cffa9c7deОбстрел|cffced4da.|n"
        "- |cffa9c7deДополнительные паруса|cffced4da.|n"
        "- |cffa9c7deПочинка|cffced4da.|n"
        "- |cffa9c7deОрудия флота|cffced4da.|n"
        "- |cffa9c7deУкреплённый корпус|cffced4da.|n|n"
        "|cffa9c7deЗона ремонта|cffced4da восстанавливает |cffc8e0872,5|cffced4da ед. здоровья в секунду союзным кораблям поблизости.|r"
    ), {"type": "unit", "id": "h0D3", "field": "ubertip", "expected": None})
    
    # owtw: Сторожевая башня (Z)
    add_u(36068, "|cffe4cfa3Сторожевая башня|r", {"type": "unit", "id": "owtw", "field": "name", "expected": "|cffe4cfa3Сторожевая башня|r"})
    add_u(36069, "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)", {"type": "unit", "id": "owtw", "field": "tip", "expected": "|cffe4cfa3Сторожевая башня|r (|cffffffffZ|r)"})
    
    # =========================================================================
    # 3. HEROES (16 SIDs across 3 heroes)
    # =========================================================================
    # N06P: Оскверненный шаман (Z)
    add_u(3617, "|cffe4cfa3Оскверненный шаман|r", {"type": "unit", "id": "N06P", "field": "name", "expected": "|cffe4cfa3Оскверненный шаман|r"})
    add_u(3618, "Ман-Шуру")
    add_u(35902, "|cffe4cfa3Оскверненный шаман|r (|cffffffffZ|r)", {"type": "unit", "id": "N06P", "field": "tip", "expected": "|cffe4cfa3Оскверненный шаман|r (|cffffffffZ|r)"})
    add_u(35901, "|cffe4cfa3Оскверненный шаман|r", {"type": "unit", "id": "N06P", "field": "awakentip", "expected": "|cffe4cfa3Оскверненный шаман|r"})
    add_u(35903, "|cffe4cfa3Оскверненный шаман|r (|cffffffffZ|r)", {"type": "unit", "id": "N06P", "field": "revivetip", "expected": "|cffe4cfa3Оскверненный шаман|r (|cffffffffZ|r)"})
    add_u(37008, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Предводитель шаманов Скверны дальнего боя. Сокрушает противников молниями и призывает древних чудовищ из глубин.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deПерст боли|cffced4da: темный разряд, последовательно поражающий нескольких врагов.|n"
        "- |cffa9c7deРассеивание заклинаний|cffced4da: снимает магические эффекты и наносит урон призванным существам.|n"
        "- |cffa9c7deОтражение скверны|cffced4da: пассивный щит, отражающий часть урона ближнего боя обратно врагам.|n"
        "- |cffa9c7deПризыв Забытого|cffced4da: призывает колоссального Забытого, атакующего врагов и порождающего щупальца.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffИнтеллект|r|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "N06P", "field": "ubertip", "expected": None})
    
    # N072: Военный лорд (C)
    add_u(35033, "|cffe4cfa3Военный лорд|r", {"type": "unit", "id": "N072", "field": "name", "expected": "|cffe4cfa3Военный лорд|r"})
    add_u(35020, "Дантур")
    add_u(35075, "|cffe4cfa3Военный лорд|r (|cffffffffC|r)", {"type": "unit", "id": "N072", "field": "tip", "expected": "|cffe4cfa3Военный лорд|r (|cffffffffC|r)"})
    add_u(36706, "|cffe4cfa3Военный лорд|r", {"type": "unit", "id": "N072", "field": "awakentip", "expected": "|cffe4cfa3Военный лорд|r"})
    add_u(37009, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Грозный полководец ближнего боя. Ведёт солдат в бой, подавляя врагов аурой страха и сокрушительным расколом земли.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deМетнуть топор|cffced4da: бросок топора, наносящий урон и оглушающий цель.|n"
        "- |cffa9c7deВсплеск ярости|cffced4da: значительно ускоряет атаку ценой увеличения получаемого урона.|n"
        "- |cffa9c7deАура Страха|cffced4da: снижает скорость передвижения и атаки находящихся рядом врагов.|n"
        "- |cffa9c7deРазкол|cffced4da: сокрушительный удар по земле с колоссальным уроном и замедлением.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffСила|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "N072", "field": "ubertip", "expected": None})
    
    # N073: Мастер меча (X)
    add_u(30703, "|cffe4cfa3Мастер меча|r", {"type": "unit", "id": "N073", "field": "name", "expected": "|cffe4cfa3Мастер меча|r"})
    add_u(36968, "Тантур")
    add_u(36976, "|cffe4cfa3Мастер меча|r (|cffffffffX|r)", {"type": "unit", "id": "N073", "field": "tip", "expected": "|cffe4cfa3Мастер меча|r (|cffffffffX|r)"})
    add_u(36705, "|cffe4cfa3Мастер меча|r", {"type": "unit", "id": "N073", "field": "awakentip", "expected": "|cffe4cfa3Мастер меча|r"})
    add_u(37010, (
        "|cffa6afb8ГЕРОЙ:|cffced4da Непревзойденный дуэлянт и мастер клинка. Рассекает врагов молниеносными атаками из тени и смертоносным вихрем стали.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deТанец ветра|cffced4da: невидимость и ускорение с критическим ударом при выходе.|n"
        "- |cffa9c7deУскользание|cffced4da: вероятность уклониться от вражеских атак.|n"
        "- |cffa9c7deКритический удар|cffced4da: шанс нанести многократный урон при атаке.|n"
        "- |cffa9c7deВихрь клинков|cffced4da: вихрь ударов с невосприимчивостью к магии и уроном в секунду вокруг.|n|n"
        "|cffa6afb8Основная характеристика:|r |cffffffffЛовкость|r|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "N073", "field": "ubertip", "expected": None})
    
    # =========================================================================
    # 4. UNITS (61 SIDs across 30 objects)
    # =========================================================================
    # h0D5: Дредноут (E)
    add_u(10916, "|cffe4cfa3Дредноут|r", {"type": "unit", "id": "h0D5", "field": "name", "expected": "|cffe4cfa3Дредноут|r"})
    add_u(10918, "|cffe4cfa3Дредноут|r (|cffffffffE|r)", {"type": "unit", "id": "h0D5", "field": "tip", "expected": "|cffe4cfa3Дредноут|r (|cffffffffE|r)"})
    add_u(6926, (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелый бронированный флагман флота Орды дальнего боя.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "h0D5", "field": "ubertip", "expected": None})
    
    # h0D6: Фрегат (W)
    add_u(3002, "|cffe4cfa3Фрегат|r", {"type": "unit", "id": "h0D6", "field": "name", "expected": "|cffe4cfa3Фрегат|r"})
    add_u(5542, (
        "|cffa6afb8ЮНИТ:|cffced4da Боевой патрульный корабль Орды, атакующий морские и береговые цели.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "h0D6", "field": "ubertip", "expected": None})
    
    # n06B: Батрак Скверны (Q)
    add_u(29065, (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый рабочий Орды Скверны. Добывает золото и древесину, возводит и ремонтирует постройки.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n06B", "field": "ubertip", "expected": None})
    
    # n06F: Мутировавший Батрак (W)
    add_u(30675, "|cffe4cfa3Мутировавший Батрак|r", {"type": "unit", "id": "n06F", "field": "name", "expected": "|cffe4cfa3Мутировавший Батрак|r"})
    add_u(35722, "|cffe4cfa3Мутировавший Батрак|r (|cffffffffW|r)", {"type": "unit", "id": "n06F", "field": "tip", "expected": "|cffe4cfa3Мутировавший Батрак|r (|cffffffffW|r)"})
    add_u(35248, (
        "|cffa6afb8ЮНИТ:|cffced4da Мутировавший рабочий-воин Орды Скверны.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deРассекающий удар|cffced4da: наносит урон по области рядом с основной целью.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n06F", "field": "ubertip", "expected": None})
    
    # Рубаки Скверны: n068 (T1), n06L (T2), n06T (T3) (Q)
    add_u(15344, (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый воин ближнего боя первого ранга.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n068", "field": "ubertip", "expected": None})
    add_u(36714, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный воин ближнего боя второго ранга.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n06L", "field": "ubertip", "expected": None})
    add_u(36723, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный ветеран ближнего боя третьего ранга с повышенным запасом здоровья и уроном.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n06T", "field": "ubertip", "expected": None})
    
    # Стрелки: n06D (T1), n06M (T2), n06Q (T3) (E)
    add_u(20943, "|cffe4cfa3Стрелок|r", {"type": "unit", "id": "n06D", "field": "name", "expected": "|cffe4cfa3Стрелок|r"})
    add_u(34261, "|cffe4cfa3Стрелок|r (|cffffffffE|r)", {"type": "unit", "id": "n06D", "field": "tip", "expected": "|cffe4cfa3Стрелок|r (|cffffffffE|r)"})
    add_u(33387, (
        "|cffa6afb8ЮНИТ:|cffced4da Базовый стрелок первого ранга с арбалетом.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06D", "field": "ubertip", "expected": None})
    
    add_u(31903, "|cffe4cfa3Стрелок|r", {"type": "unit", "id": "n06M", "field": "name", "expected": "|cffe4cfa3Стрелок|r"})
    add_u(35721, "|cffe4cfa3Стрелок|r (|cffffffffE|r)", {"type": "unit", "id": "n06M", "field": "tip", "expected": "|cffe4cfa3Стрелок|r (|cffffffffE|r)"})
    add_u(36715, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный стрелок второго ранга с арбалетом.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06M", "field": "ubertip", "expected": None})
    
    add_u(35808, "|cffe4cfa3Стрелок|r", {"type": "unit", "id": "n06Q", "field": "name", "expected": "|cffe4cfa3Стрелок|r"})
    add_u(35810, "|cffe4cfa3Стрелок|r (|cffffffffE|r)", {"type": "unit", "id": "n06Q", "field": "tip", "expected": "|cffe4cfa3Стрелок|r (|cffffffffE|r)"})
    add_u(36720, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный стрелок третьего ранга с увеличенной дальностью и бронебойными болтами.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06Q", "field": "ubertip", "expected": None})
    
    # Копьеметатели: n06G (T1), n06J (T2), n06W (T3) (W)
    add_u(26975, "|cffe4cfa3Копьеметатель|r", {"type": "unit", "id": "n06G", "field": "name", "expected": "|cffe4cfa3Копьеметатель|r"})
    add_u(34565, "|cffe4cfa3Копьеметатель|r (|cffffffffW|r)", {"type": "unit", "id": "n06G", "field": "tip", "expected": "|cffe4cfa3Копьеметатель|r (|cffffffffW|r)"})
    add_u(35251, (
        "|cffa6afb8ЮНИТ:|cffced4da Метатель тяжелых копий первого ранга дальнего боя.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06G", "field": "ubertip", "expected": None})
    
    add_u(34551, "|cffe4cfa3Копьеметатель|r", {"type": "unit", "id": "n06J", "field": "name", "expected": "|cffe4cfa3Копьеметатель|r"})
    add_u(35723, "|cffe4cfa3Копьеметатель|r (|cffffffffW|r)", {"type": "unit", "id": "n06J", "field": "tip", "expected": "|cffe4cfa3Копьеметатель|r (|cffffffffW|r)"})
    add_u(36712, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный метатель тяжелых копий второго ранга дальнего боя.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06J", "field": "ubertip", "expected": None})
    
    add_u(35804, "|cffe4cfa3Копьеметатель|r", {"type": "unit", "id": "n06W", "field": "name", "expected": "|cffe4cfa3Копьеметатель|r"})
    add_u(35805, "|cffe4cfa3Копьеметатель|r (|cffffffffW|r)", {"type": "unit", "id": "n06W", "field": "tip", "expected": "|cffe4cfa3Копьеметатель|r (|cffffffffW|r)"})
    add_u(36728, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный метатель тяжелых копий третьего ранга с повышенной дальностью поражения.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06W", "field": "ubertip", "expected": None})
    
    # Телохранители вождя: o05Q (T1), o065 (T2), o063 (T3) (E)
    add_u(33452, "|cffe4cfa3Телохранитель вождя|r", {"type": "unit", "id": "o05Q", "field": "name", "expected": "|cffe4cfa3Телохранитель вождя|r"})
    add_u(33391, "|cffe4cfa3Телохранитель вождя|r (|cffffffffE|r)", {"type": "unit", "id": "o05Q", "field": "tip", "expected": "|cffe4cfa3Телохранитель вождя|r (|cffffffffE|r)"})
    add_u(35245, (
        "|cffa6afb8ЮНИТ:|cffced4da Тяжелый пехотинец первого ранга, защищающий вождей Орды.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Защиты|cffced4da: повышает броню находящихся рядом союзников.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "o05Q", "field": "ubertip", "expected": None})
    
    add_u(35812, "|cffe4cfa3Телохранитель вождя|r", {"type": "unit", "id": "o065", "field": "name", "expected": "|cffe4cfa3Телохранитель вождя|r"})
    add_u(36726, "|cffe4cfa3Телохранитель вождя|r (|cffffffffE|r)", {"type": "unit", "id": "o065", "field": "tip", "expected": "|cffe4cfa3Телохранитель вождя|r (|cffffffffE|r)"})
    add_u(36727, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный тяжелый пехотинец второго ранга.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Защиты|cffced4da: повышает броню находящихся рядом союзников.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "o065", "field": "ubertip", "expected": None})
    
    add_u(34547, "|cffe4cfa3Телохранитель вождя|r", {"type": "unit", "id": "o063", "field": "name", "expected": "|cffe4cfa3Телохранитель вождя|r"})
    add_u(36716, "|cffe4cfa3Телохранитель вождя|r (|cffffffffE|r)", {"type": "unit", "id": "o063", "field": "tip", "expected": "|cffe4cfa3Телохранитель вождя|r (|cffffffffE|r)"})
    add_u(36717, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный тяжелый пехотинец третьего ранга с непревзойденной защитой.|n|n"
        "|cffa6afb8Способности:|cffced4da|n- |cffa9c7deАура Защиты|cffced4da: повышает броню находящихся рядом союзников.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "o063", "field": "ubertip", "expected": None})
    
    # o05R: Разрушитель (R)
    add_u(29076, (
        "|cffa6afb8ЮНИТ:|cffced4da Дальнобойная осадная катапульта, эффективная против зданий и укреплений.|n|n"
        "|cffa6afb8Атакует наземные цели и деревья.|r"
    ), {"type": "unit", "id": "o05R", "field": "ubertip", "expected": None})
    
    # Чернокнижники: n067 (T1), n06R (T2), n06N (T3) (Q)
    add_u(10616, (
        "|cffa6afb8ЮНИТ:|cffced4da Темный маг первого ранга, владеющий огненными стрелами и рассеиванием.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n067", "field": "ubertip", "expected": None})
    add_u(36721, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный темный маг второго ранга.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06R", "field": "ubertip", "expected": None})
    add_u(36718, (
        "|cffa6afb8ЮНИТ:|cffced4da Высший чернокнижник третьего ранга с максимальным запасом маны.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06N", "field": "ubertip", "expected": None})
    
    # Шаманы: n06C (T1), n06S (T2), n06O (T3) (W)
    add_u(17861, "|cffe4cfa3Шаман|r", {"type": "unit", "id": "n06C", "field": "name", "expected": "|cffe4cfa3Шаман|r"})
    add_u(34537, "|cffe4cfa3Шаман|r (|cffffffffW|r)", {"type": "unit", "id": "n06C", "field": "tip", "expected": "|cffe4cfa3Шаман|r (|cffffffffW|r)"})
    add_u(33386, (
        "|cffa6afb8ЮНИТ:|cffced4da Заклинатель поддержки первого ранга с раздвоенной молнией и жаждой крови.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06C", "field": "ubertip", "expected": None})
    
    add_u(35814, "|cffe4cfa3Шаман|r", {"type": "unit", "id": "n06S", "field": "name", "expected": "|cffe4cfa3Шаман|r"})
    add_u(35816, "|cffe4cfa3Шаман|r (|cffffffffW|r)", {"type": "unit", "id": "n06S", "field": "tip", "expected": "|cffe4cfa3Шаман|r (|cffffffffW|r)"})
    add_u(36722, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный заклинатель поддержки второго ранга.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06S", "field": "ubertip", "expected": None})
    
    add_u(34385, "|cffe4cfa3Шаман|r", {"type": "unit", "id": "n06O", "field": "name", "expected": "|cffe4cfa3Шаман|r"})
    add_u(35720, "|cffe4cfa3Шаман|r (|cffffffffW|r)", {"type": "unit", "id": "n06O", "field": "tip", "expected": "|cffe4cfa3Шаман|r (|cffffffffW|r)"})
    add_u(36719, (
        "|cffa6afb8ЮНИТ:|cffced4da Высший шаман третьего ранга с мощными стихийными чарами.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06O", "field": "ubertip", "expected": None})
    
    # Налетчики: n069 (T1), n06U (T2), n06K (T3) (Q)
    add_u(15345, (
        "|cffa6afb8ЮНИТ:|cffced4da Быстрый кавалерист первого ранга на волке, способный обездвиживать врагов сетью.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n069", "field": "ubertip", "expected": None})
    add_u(36724, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный кавалерист второго ранга с боевым кличем.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n06U", "field": "ubertip", "expected": None})
    add_u(36713, (
        "|cffa6afb8ЮНИТ:|cffced4da Элитный налетчик третьего ранга с высокой скоростью и сокрушительным уроном.|n|n"
        "|cffa6afb8Атакует наземные цели.|r"
    ), {"type": "unit", "id": "n06K", "field": "ubertip", "expected": None})
    
    # Кодо: n06A (T1), n06I (T2), n06V (T3) (W)
    add_u(33385, (
        "|cffa6afb8ЮНИТ:|cffced4da Массивный боевой зверь первого ранга с барабанами и пожиранием.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06A", "field": "ubertip", "expected": None})
    add_u(35254, (
        "|cffa6afb8ЮНИТ:|cffced4da Усиленный боевой зверь второго ранга с аурой выносливости.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06I", "field": "ubertip", "expected": None})
    add_u(36725, (
        "|cffa6afb8ЮНИТ:|cffced4da Исполинский кодо третьего ранга с колоссальным запасом здоровья.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n06V", "field": "ubertip", "expected": None})
    
    # n070: Некромант (Q)
    add_u(36729, "|cffe4cfa3Некромант|r", {"type": "unit", "id": "n070", "field": "name", "expected": "|cffe4cfa3Некромант|r"})
    add_u(36730, "|cffe4cfa3Некромант|r (|cffffffffQ|r)", {"type": "unit", "id": "n070", "field": "tip", "expected": "|cffe4cfa3Некромант|r (|cffffffffQ|r)"})
    add_u(36731, (
        "|cffa6afb8ЮНИТ:|cffced4da Темный маг Орды Скверны, поднимающий скелетов из трупов врагов.|n|n"
        "|cffa6afb8Атакует наземные и воздушные цели.|r"
    ), {"type": "unit", "id": "n070", "field": "ubertip", "expected": None})
    
    # =========================================================================
    # 5. UPGRADES (156 SIDs across 21 upgrades)
    # =========================================================================
    # R00Y: Горючая смесь (catapults)
    add_u(20159, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Покрывает снаряды катапульт горючей смесью, позволяя им поджигать землю и наносить периодический урон.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРазрушитель|cffced4da.|r"
    ), {"type": "upgrade", "id": "R00Y", "field": "ubertip1", "expected": None})
    
    # R0JQ: Оружие дальнего боя (6 levels, hotkey R)
    # SIDs: names: 22737, 22738, 22739 (lvls 4,5,6)
    #       tips: 22740, 22741, 22742 (lvls 4,5,6)
    #       ubs: 31055, 31056, 31057, 31052, 31053, 31054 (lvls 1..6)
    r0jq_dmg = [5, 10, 15, 20, 25, 30]
    for lvl in range(1, 7):
        ub_sid = [31055, 31056, 31057, 31052, 31053, 31054][lvl-1]
        add_u(ub_sid, (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон немагических войск дальнего боя на |cffc8e087+{r0jq_dmg[lvl-1]}|cffced4da.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da|n- |cffa9c7deКопьеметатель|cffced4da|n- |cffa9c7deРазрушитель|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        ), {"type": "upgrade", "id": "R0JQ", "field": f"ubertip{lvl}", "expected": None})
    
    add_u(22737, "|cffe4cfa3Оружие дальнего боя|r — уровень 4", {"type": "upgrade", "id": "R0JQ", "field": "name4", "expected": "|cffe4cfa3Оружие дальнего боя|r — уровень 4"})
    add_u(22738, "|cffe4cfa3Оружие дальнего боя|r — уровень 5", {"type": "upgrade", "id": "R0JQ", "field": "name5", "expected": "|cffe4cfa3Оружие дальнего боя|r — уровень 5"})
    add_u(22739, "|cffe4cfa3Оружие дальнего боя|r — уровень 6", {"type": "upgrade", "id": "R0JQ", "field": "name6", "expected": "|cffe4cfa3Оружие дальнего боя|r — уровень 6"})
    add_u(22740, "|cffe4cfa3Оружие дальнего боя — уровень 4|r (|cffffffffR|r)", {"type": "upgrade", "id": "R0JQ", "field": "tip4", "expected": "|cffe4cfa3Оружие дальнего боя — уровень 4|r (|cffffffffR|r)"})
    add_u(22741, "|cffe4cfa3Оружие дальнего боя — уровень 5|r (|cffffffffR|r)", {"type": "upgrade", "id": "R0JQ", "field": "tip5", "expected": "|cffe4cfa3Оружие дальнего боя — уровень 5|r (|cffffffffR|r)"})
    add_u(22742, "|cffe4cfa3Оружие дальнего боя — уровень 6|r (|cffffffffR|r)", {"type": "upgrade", "id": "R0JQ", "field": "tip6", "expected": "|cffe4cfa3Оружие дальнего боя — уровень 6|r (|cffffffffR|r)"})
    
    # R0JR: Стальная броня (6 levels, hotkey A)
    # SIDs: names: 29426 (lvl 1), 22754 (4), 22755 (5), 22756 (6)
    #       tips: 22757 (4), 22758 (5), 22759 (6)
    #       ubs: 28247..28252 (lvls 1..6)
    r0jr_def = [2, 4, 6, 8, 10, 12]
    for lvl in range(1, 7):
        ub_sid = [28247, 28248, 28249, 28250, 28251, 28252][lvl-1]
        add_u(ub_sid, (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает броню воинов ближнего боя Орды Скверны на |cffc8e087+{r0jr_def[lvl-1]}|cffced4da.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака Скверны|cffced4da|n- |cffa9c7deТелохранитель вождя|cffced4da|n- |cffa9c7deНалетчик Скверны|cffced4da|n- |cffa9c7deКодо Скверны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        ), {"type": "upgrade", "id": "R0JR", "field": f"ubertip{lvl}", "expected": None})
    
    add_u(29426, "|cffe4cfa3Стальная броня|r — уровень 1", {"type": "upgrade", "id": "R0JR", "field": "name1", "expected": "|cffe4cfa3Стальная броня|r — уровень 1"})
    add_u(22754, "|cffe4cfa3Стальная броня|r — уровень 4", {"type": "upgrade", "id": "R0JR", "field": "name4", "expected": "|cffe4cfa3Стальная броня|r — уровень 4"})
    add_u(22755, "|cffe4cfa3Стальная броня|r — уровень 5", {"type": "upgrade", "id": "R0JR", "field": "name5", "expected": "|cffe4cfa3Стальная броня|r — уровень 5"})
    add_u(22756, "|cffe4cfa3Стальная броня|r — уровень 6", {"type": "upgrade", "id": "R0JR", "field": "name6", "expected": "|cffe4cfa3Стальная броня|r — уровень 6"})
    add_u(22757, "|cffe4cfa3Стальная броня — уровень 4|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JR", "field": "tip4", "expected": "|cffe4cfa3Стальная броня — уровень 4|r (|cffffffffA|r)"})
    add_u(22758, "|cffe4cfa3Стальная броня — уровень 5|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JR", "field": "tip5", "expected": "|cffe4cfa3Стальная броня — уровень 5|r (|cffffffffA|r)"})
    add_u(22759, "|cffe4cfa3Стальная броня — уровень 6|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JR", "field": "tip6", "expected": "|cffe4cfa3Стальная броня — уровень 6|r (|cffffffffA|r)"})
    
    # R0JS: Оружие ближнего боя (6 levels, hotkey M)
    # SIDs: names: 20134 (lvl 1), 22769 (4), 22770 (5), 22771 (6)
    #       tips: 31575 (4), 31576 (5), 31969 (6)
    #       ubs: 31972..31977 (lvls 1..6)
    r0js_dmg = [6, 12, 18, 24, 30, 36]
    for lvl in range(1, 7):
        ub_sid = [31972, 31973, 31974, 31975, 31976, 31977][lvl-1]
        add_u(ub_sid, (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон немагических войск ближнего боя на |cffc8e087+{r0js_dmg[lvl-1]}|cffced4da.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака Скверны|cffced4da|n- |cffa9c7deТелохранитель вождя|cffced4da|n- |cffa9c7deНалетчик Скверны|cffced4da|n- |cffa9c7deМутировавший Батрак|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        ), {"type": "upgrade", "id": "R0JS", "field": f"ubertip{lvl}", "expected": None})
    
    add_u(20134, "|cffe4cfa3Оружие ближнего боя|r — уровень 1", {"type": "upgrade", "id": "R0JS", "field": "name1", "expected": "|cffe4cfa3Оружие ближнего боя|r — уровень 1"})
    add_u(22769, "|cffe4cfa3Оружие ближнего боя|r — уровень 4", {"type": "upgrade", "id": "R0JS", "field": "name4", "expected": "|cffe4cfa3Оружие ближнего боя|r — уровень 4"})
    add_u(22770, "|cffe4cfa3Оружие ближнего боя|r — уровень 5", {"type": "upgrade", "id": "R0JS", "field": "name5", "expected": "|cffe4cfa3Оружие ближнего боя|r — уровень 5"})
    add_u(22771, "|cffe4cfa3Оружие ближнего боя|r — уровень 6", {"type": "upgrade", "id": "R0JS", "field": "name6", "expected": "|cffe4cfa3Оружие ближнего боя|r — уровень 6"})
    add_u(31575, "|cffe4cfa3Оружие ближнего боя — уровень 4|r (|cffffffffM|r)", {"type": "upgrade", "id": "R0JS", "field": "tip4", "expected": "|cffe4cfa3Оружие ближнего боя — уровень 4|r (|cffffffffM|r)"})
    add_u(31576, "|cffe4cfa3Оружие ближнего боя — уровень 5|r (|cffffffffM|r)", {"type": "upgrade", "id": "R0JS", "field": "tip5", "expected": "|cffe4cfa3Оружие ближнего боя — уровень 5|r (|cffffffffM|r)"})
    add_u(31969, "|cffe4cfa3Оружие ближнего боя — уровень 6|r (|cffffffffM|r)", {"type": "upgrade", "id": "R0JS", "field": "tip6", "expected": "|cffe4cfa3Оружие ближнего боя — уровень 6|r (|cffffffffM|r)"})
    
    # R0JU: Обучение шаманов (3 levels, hotkey S)
    # SIDs: names: 33573, 33583, 33426
    #       tips: 34160, 34161, 33429
    #       ubs: 30348, 30402, 33003
    add_u(33573, "|cffe4cfa3Обучение шаманов|r — уровень 1", {"type": "upgrade", "id": "R0JU", "field": "name1", "expected": "|cffe4cfa3Обучение шаманов|r — уровень 1"})
    add_u(33583, "|cffe4cfa3Обучение шаманов|r — уровень 2", {"type": "upgrade", "id": "R0JU", "field": "name2", "expected": "|cffe4cfa3Обучение шаманов|r — уровень 2"})
    add_u(33426, "|cffe4cfa3Обучение шаманов|r — уровень 3", {"type": "upgrade", "id": "R0JU", "field": "name3", "expected": "|cffe4cfa3Обучение шаманов|r — уровень 3"})
    add_u(34160, "|cffe4cfa3Обучение шаманов — уровень 1|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0JU", "field": "tip1", "expected": "|cffe4cfa3Обучение шаманов — уровень 1|r (|cffffffffS|r)"})
    add_u(34161, "|cffe4cfa3Обучение шаманов — уровень 2|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0JU", "field": "tip2", "expected": "|cffe4cfa3Обучение шаманов — уровень 2|r (|cffffffffS|r)"})
    add_u(33429, "|cffe4cfa3Обучение шаманов — уровень 3|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0JU", "field": "tip3", "expected": "|cffe4cfa3Обучение шаманов — уровень 3|r (|cffffffffS|r)"})
    add_u(30348, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья шаманов на |cffc8e087+40|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед. и скорость регенерации маны на |cffc8e087+33%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШаман|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JU", "field": "ubertip1", "expected": None})
    add_u(30402, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья шаманов на |cffc8e087+40|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед. и скорость регенерации маны на |cffc8e087+33%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШаман|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JU", "field": "ubertip2", "expected": None})
    add_u(33003, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья шаманов на |cffc8e087+40|cffced4da ед., запас маны на |cffc8e087+100|cffced4da ед. и скорость регенерации маны на |cffc8e087+33%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deШаман|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JU", "field": "ubertip3", "expected": None})
    
    # R0JV: Черная магия (3 levels, hotkey A)
    # SIDs: names: 36530, 36531, 25332
    #       tips: 36533, 36534, 25334
    #       ubs: 25331, 36524, 36528
    add_u(36530, "|cffe4cfa3Черная магия|r — уровень 1", {"type": "upgrade", "id": "R0JV", "field": "name1", "expected": "|cffe4cfa3Черная магия|r — уровень 1"})
    add_u(36531, "|cffe4cfa3Черная магия|r — уровень 2", {"type": "upgrade", "id": "R0JV", "field": "name2", "expected": "|cffe4cfa3Черная магия|r — уровень 2"})
    add_u(25332, "|cffe4cfa3Черная магия|r — уровень 3", {"type": "upgrade", "id": "R0JV", "field": "name3", "expected": "|cffe4cfa3Черная магия|r — уровень 3"})
    add_u(36533, "|cffe4cfa3Черная магия — уровень 1|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JV", "field": "tip1", "expected": "|cffe4cfa3Черная магия — уровень 1|r (|cffffffffA|r)"})
    add_u(36534, "|cffe4cfa3Черная магия — уровень 2|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JV", "field": "tip2", "expected": "|cffe4cfa3Черная магия — уровень 2|r (|cffffffffA|r)"})
    add_u(25334, "|cffe4cfa3Черная магия — уровень 3|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JV", "field": "tip3", "expected": "|cffe4cfa3Черная магия — уровень 3|r (|cffffffffA|r)"})
    add_u(25331, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья чернокнижников на |cffc8e087+60|cffced4da ед., запас маны на |cffc8e087+50|cffced4da ед. и скорость регенерации маны на |cffc8e087+33%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЧернокнижник Скверны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JV", "field": "ubertip1", "expected": None})
    add_u(36524, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья чернокнижников на |cffc8e087+60|cffced4da ед., запас маны на |cffc8e087+50|cffced4da ед. и скорость регенерации маны на |cffc8e087+33%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЧернокнижник Скверны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JV", "field": "ubertip2", "expected": None})
    add_u(36528, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья чернокнижников на |cffc8e087+60|cffced4da ед., запас маны на |cffc8e087+50|cffced4da ед. и скорость регенерации маны на |cffc8e087+33%|cffced4da.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deЧернокнижник Скверны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JV", "field": "ubertip3", "expected": None})
    
    # R0JW: Заточеный болт (1 level, hotkey D)
    add_u(36546, "|cffe4cfa3Заточеный болт|r", {"type": "upgrade", "id": "R0JW", "field": "name1", "expected": "|cffe4cfa3Заточеный болт|r"})
    add_u(36548, "|cffe4cfa3Заточеный болт|r (|cffffffffD|r)", {"type": "upgrade", "id": "R0JW", "field": "tip1", "expected": "|cffe4cfa3Заточеный болт|r (|cffffffffD|r)"})
    add_u(36537, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает урон стрелков на |cffc8e087+5|cffced4da ед. и увеличивает эффективность пробития тяжелой брони.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deСтрелок|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JW", "field": "ubertip1", "expected": None})
    
    # R0JX: Сверхлегкие копья (2 levels, hotkey S)
    add_u(34164, "|cffe4cfa3Сверхлегкие копья|r — уровень 1", {"type": "upgrade", "id": "R0JX", "field": "name1", "expected": "|cffe4cfa3Сверхлегкие копья|r — уровень 1"})
    add_u(34165, "|cffe4cfa3Сверхлегкие копья|r — уровень 2", {"type": "upgrade", "id": "R0JX", "field": "name2", "expected": "|cffe4cfa3Сверхлегкие копья|r — уровень 2"})
    add_u(34166, "|cffe4cfa3Сверхлегкие копья — уровень 1|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0JX", "field": "tip1", "expected": "|cffe4cfa3Сверхлегкие копья — уровень 1|r (|cffffffffS|r)"})
    add_u(34167, "|cffe4cfa3Сверхлегкие копья — уровень 2|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0JX", "field": "tip2", "expected": "|cffe4cfa3Сверхлегкие копья — уровень 2|r (|cffffffffS|r)"})
    add_u(34162, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает дальность атаки копьеметателей на |cffc8e087+50|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deКопьеметатель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JX", "field": "ubertip1", "expected": None})
    add_u(34163, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает дальность атаки копьеметателей на |cffc8e087+50|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deКопьеметатель|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JX", "field": "ubertip2", "expected": None})
    
    # R0JY: Грубая сила (1 level, hotkey A)
    add_u(36565, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Повышает запас здоровья рубак на |cffc8e087+100|cffced4da ед. и урон от их атак на |cffc8e087+3|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака Скверны|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JY", "field": "ubertip1", "expected": None})
    
    # R0JZ: Тренировки с волками (2 levels, hotkey A)
    add_u(34168, "|cffe4cfa3Тренировки с волками|r — уровень 1", {"type": "upgrade", "id": "R0JZ", "field": "name1", "expected": "|cffe4cfa3Тренировки с волками|r — уровень 1"})
    add_u(34346, "|cffe4cfa3Тренировки с волками|r — уровень 2", {"type": "upgrade", "id": "R0JZ", "field": "name2", "expected": "|cffe4cfa3Тренировки с волками|r — уровень 2"})
    add_u(35872, "|cffe4cfa3Тренировки с волками — уровень 1|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JZ", "field": "tip1", "expected": "|cffe4cfa3Тренировки с волками — уровень 1|r (|cffffffffA|r)"})
    add_u(36105, "|cffe4cfa3Тренировки с волками — уровень 2|r (|cffffffffA|r)", {"type": "upgrade", "id": "R0JZ", "field": "tip2", "expected": "|cffe4cfa3Тренировки с волками — уровень 2|r (|cffffffffA|r)"})
    add_u(36568, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость передвижения налетчиков на |cffc8e087+15|cffced4da ед. и повышает их урон на |cffc8e087+5|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНалетчик Скверны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JZ", "field": "ubertip1", "expected": None})
    add_u(36572, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает скорость передвижения налетчиков на |cffc8e087+15|cffced4da ед. и повышает их урон на |cffc8e087+5|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНалетчик Скверны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0JZ", "field": "ubertip2", "expected": None})
    
    # R0K0: Обучение телохранителя (3 levels, hotkey D)
    add_u(36592, "|cffe4cfa3Обучение телохранителя|r — уровень 1", {"type": "upgrade", "id": "R0K0", "field": "name1", "expected": "|cffe4cfa3Обучение телохранителя|r — уровень 1"})
    add_u(36593, "|cffe4cfa3Обучение телохранителя|r — уровень 2", {"type": "upgrade", "id": "R0K0", "field": "name2", "expected": "|cffe4cfa3Обучение телохранителя|r — уровень 2"})
    add_u(36589, "|cffe4cfa3Обучение телохранителя|r — уровень 3", {"type": "upgrade", "id": "R0K0", "field": "name3", "expected": "|cffe4cfa3Обучение телохранителя|r — уровень 3"})
    add_u(36594, "|cffe4cfa3Обучение телохранителя — уровень 1|r (|cffffffffD|r)", {"type": "upgrade", "id": "R0K0", "field": "tip1", "expected": "|cffe4cfa3Обучение телохранителя — уровень 1|r (|cffffffffD|r)"})
    add_u(36595, "|cffe4cfa3Обучение телохранителя — уровень 2|r (|cffffffffD|r)", {"type": "upgrade", "id": "R0K0", "field": "tip2", "expected": "|cffe4cfa3Обучение телохранителя — уровень 2|r (|cffffffffD|r)"})
    add_u(36590, "|cffe4cfa3Обучение телохранителя — уровень 3|r (|cffffffffD|r)", {"type": "upgrade", "id": "R0K0", "field": "tip3", "expected": "|cffe4cfa3Обучение телохранителя — уровень 3|r (|cffffffffD|r)"})
    add_u(36583, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья телохранителей на |cffc8e087+30|cffced4da ед. и повышает их боевые характеристики.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deТелохранитель вождя|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0K0", "field": "ubertip1", "expected": None})
    add_u(36587, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья телохранителей на |cffc8e087+30|cffced4da ед. и повышает их боевые характеристики.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deТелохранитель вождя|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0K0", "field": "ubertip2", "expected": None})
    add_u(36588, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья телохранителей на |cffc8e087+30|cffced4da ед. и повышает их боевые характеристики.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deТелохранитель вождя|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff3|cffced4da/|cffffffff3|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0K0", "field": "ubertip3", "expected": None})
    
    # R0K1: Улучшенные пилы (6 levels, hotkey S)
    r0k1_wood = [5, 10, 15, 20, 25, 30]
    for lvl in range(1, 7):
        name_sid = [36520, 39877, 37390, 37486, 37594, 38549][lvl-1]
        tip_sid = [38572, 39928, 39059, 39350, 39357, 39824][lvl-1]
        ub_sid = [36761, 36756, 36757, 36758, 36759, 36760][lvl-1]
        add_u(name_sid, f"|cffe4cfa3Улучшенные пилы|r — уровень {lvl}", {"type": "upgrade", "id": "R0K1", "field": f"name{lvl}", "expected": f"|cffe4cfa3Улучшенные пилы|r — уровень {lvl}"})
        add_u(tip_sid, f"|cffe4cfa3Улучшенные пилы — уровень {lvl}|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0K1", "field": f"tip{lvl}", "expected": f"|cffe4cfa3Улучшенные пилы — уровень {lvl}|r (|cffffffffS|r)"})
        add_u(ub_sid, (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает количество переносимой батраками древесины на |cffc8e087+{r0k1_wood[lvl-1]}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deБатрак Скверны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        ), {"type": "upgrade", "id": "R0K1", "field": f"ubertip{lvl}", "expected": None})
    
    # R0K2: Поощрять ярость (6 levels, hotkey D)
    r0k2_dmg = [8, 16, 24, 32, 40, 48]
    r0k2_hp = [60, 120, 180, 240, 300, 360]
    for lvl in range(1, 7):
        name_sid = [36774, 36775, 36771, 36778, 36779, 36780][lvl-1]
        tip_sid = [36776, 36777, 36772, 36785, 36786, 36787][lvl-1]
        ub_sid = [11069, 20381, 20384, 20386, 24421, 24539][lvl-1]
        add_u(name_sid, f"|cffe4cfa3Поощрять ярость|r — уровень {lvl}", {"type": "upgrade", "id": "R0K2", "field": f"name{lvl}", "expected": f"|cffe4cfa3Поощрять ярость|r — уровень {lvl}"})
        add_u(tip_sid, f"|cffe4cfa3Поощрять ярость — уровень {lvl}|r (|cffffffffD|r)", {"type": "upgrade", "id": "R0K2", "field": f"tip{lvl}", "expected": f"|cffe4cfa3Поощрять ярость — уровень {lvl}|r (|cffffffffD|r)"})
        add_u(ub_sid, (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает урон воинов на |cffc8e087+{r0k2_dmg[lvl-1]}|cffced4da ед. ценой снижения их здоровья на |cffe69a8d-{r0k2_hp[lvl-1]}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВойскам Орды Скверны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        ), {"type": "upgrade", "id": "R0K2", "field": f"ubertip{lvl}", "expected": None})
    
    # R0K3: Подавлять ярость (6 levels, hotkey F)
    r0k3_hp = [60, 120, 180, 240, 300, 360]
    r0k3_dmg = [8, 16, 24, 32, 40, 48]
    for lvl in range(1, 7):
        name_sid = [36809, 36810, 36806, 36813, 36814, 36815][lvl-1]
        tip_sid = [36811, 36812, 36807, 36820, 36821, 36822][lvl-1]
        ub_sid = [24546, 24549, 24550, 24884, 24885, 25424][lvl-1]
        add_u(name_sid, f"|cffe4cfa3Подавлять ярость|r — уровень {lvl}", {"type": "upgrade", "id": "R0K3", "field": f"name{lvl}", "expected": f"|cffe4cfa3Подавлять ярость|r — уровень {lvl}"})
        add_u(tip_sid, f"|cffe4cfa3Подавлять ярость — уровень {lvl}|r (|cffffffffF|r)", {"type": "upgrade", "id": "R0K3", "field": f"tip{lvl}", "expected": f"|cffe4cfa3Подавлять ярость — уровень {lvl}|r (|cffffffffF|r)"})
        add_u(ub_sid, (
            f"|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает здоровье воинов на |cffc8e087+{r0k3_hp[lvl-1]}|cffced4da ед. ценой снижения их урона на |cffe69a8d-{r0k3_dmg[lvl-1]}|cffced4da ед.|n|n"
            "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deВойскам Орды Скверны|cffced4da.|n|n"
            f"|cffa6afb8Уровень исследования:|r |cffffffff{lvl}|cffced4da/|cffffffff6|cffced4da.|r"
        ), {"type": "upgrade", "id": "R0K3", "field": f"ubertip{lvl}", "expected": None})
    
    # R0K5: Тренировки кодо (2 levels, hotkey S)
    add_u(39974, "|cffe4cfa3Тренировки кодо|r — уровень 1", {"type": "upgrade", "id": "R0K5", "field": "name1", "expected": "|cffe4cfa3Тренировки кодо|r — уровень 1"})
    add_u(39975, "|cffe4cfa3Тренировки кодо|r — уровень 2", {"type": "upgrade", "id": "R0K5", "field": "name2", "expected": "|cffe4cfa3Тренировки кодо|r — уровень 2"})
    add_u(39980, "|cffe4cfa3Тренировки кодо — уровень 1|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0K5", "field": "tip1", "expected": "|cffe4cfa3Тренировки кодо — уровень 1|r (|cffffffffS|r)"})
    add_u(39982, "|cffe4cfa3Тренировки кодо — уровень 2|r (|cffffffffS|r)", {"type": "upgrade", "id": "R0K5", "field": "tip2", "expected": "|cffe4cfa3Тренировки кодо — уровень 2|r (|cffffffffS|r)"})
    add_u(25326, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья кодо Скверны на |cffc8e087+50|cffced4da ед. и повышает их урон на |cffc8e087+5|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deКодо Скверны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff1|cffced4da/|cffffffff2|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0K5", "field": "ubertip1", "expected": None})
    add_u(25330, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает запас здоровья кодо Скверны на |cffc8e087+50|cffced4da ед. и повышает их урон на |cffc8e087+5|cffced4da ед.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deКодо Скверны|cffced4da.|n|n"
        "|cffa6afb8Уровень исследования:|r |cffffffff2|cffced4da/|cffffffff2|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0K5", "field": "ubertip2", "expected": None})
    
    # R0K6: Искусное воскрешение (1 level, hotkey A)
    add_u(26495, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Один из скелетов, призываемых некромантами с помощью «Воскрешения мертвых», становится усиленным Орком-защитником.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНекромант|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0K6", "field": "ubertip1", "expected": None})
    
    # R0K7: Живучие скелеты (1 level, hotkey Z)
    add_u(28946, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Увеличивает время жизни призванных скелетов-воинов и скелетов-магов на |cffc8e087+15|cffced4da сек.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНекромант|cffced4da.|r"
    ), {"type": "upgrade", "id": "R0K7", "field": "ubertip1", "expected": None})
    
    # Roen: Опутывание (1 level, hotkey N)
    add_u(26346, "|cffe4cfa3Опутывание|r", {"type": "upgrade", "id": "Roen", "field": "name1", "expected": "|cffe4cfa3Опутывание|r"})
    add_u(26347, "|cffe4cfa3Опутывание|r (|cffffffffN|r)", {"type": "upgrade", "id": "Roen", "field": "tip1", "expected": "|cffe4cfa3Опутывание|r (|cffffffffN|r)"})
    add_u(26366, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Дарует налетчикам способность «Опутывание», притягивающую врага к земле и лишающую его возможности двигаться.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deНалетчик Скверны|cffced4da.|r"
    ), {"type": "upgrade", "id": "Roen", "field": "ubertip1", "expected": None})
    
    # Ropg: Грабеж (1 level, hotkey R)
    add_u(22401, "|cffe4cfa3Грабеж|r", {"type": "upgrade", "id": "Ropg", "field": "name1", "expected": "|cffe4cfa3Грабеж|r"})
    add_u(22402, "|cffe4cfa3Грабеж|r (|cffffffffR|r)", {"type": "upgrade", "id": "Ropg", "field": "tip1", "expected": "|cffe4cfa3Грабеж|r (|cffffffffR|r)"})
    add_u(22403, (
        "|cffa6afb8ИССЛЕДОВАНИЕ:|cffced4da Воины ближнего боя Орды Скверны добывают золото при нанесении урона вражеским постройкам.|n|n"
        "|cffa6afb8Применяется к:|cffced4da|n- |cffa9c7deРубака Скверны|cffced4da|n- |cffa9c7deТелохранитель вождя|cffced4da|n- |cffa9c7deНалетчик Скверны|cffced4da.|r"
    ), {"type": "upgrade", "id": "Ropg", "field": "ubertip1", "expected": None})
    
    # =========================================================================
    # 6. ABILITIES (196 SIDs across 53 objects)
    # =========================================================================
    # A01C: Свечение героя
    add_u(2038, "|cffe4cfa3Свечение героя|r", {"type": "ability", "id": "A01C", "field": "name", "expected": "|cffe4cfa3Свечение героя|r"})
    add_u(2039, "|cffe4cfa3Свечение героя|r", {"type": "ability", "id": "A01C", "field": "tip1", "expected": "|cffe4cfa3Свечение героя|r"})
    
    # A0B7: Призыв Забытого (R, 2 levels)
    add_u(8169, "|cffe4cfa3Призыв Забытого|r", {"type": "ability", "id": "A0B7", "field": "name", "expected": "|cffe4cfa3Призыв Забытого|r"})
    add_u(8170, "|cffe4cfa3Призыв Забытого — уровень 1|r (|cffffffffR|r)", {"type": "ability", "id": "A0B7", "field": "tip1", "expected": "|cffe4cfa3Призыв Забытого — уровень 1|r (|cffffffffR|r)"})
    add_u(8172, "|cffe4cfa3Призыв Забытого — уровень 2|r (|cffffffffR|r)", {"type": "ability", "id": "A0B7", "field": "tip2", "expected": "|cffe4cfa3Призыв Забытого — уровень 2|r (|cffffffffR|r)"})
    add_u(10178, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из глубин |cffffffff1|cffced4da Забытого, способного атаковать врагов и порождать щупальца.|r", {"type": "ability", "id": "A0B7", "field": "ubertip1", "expected": None})
    add_u(10177, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из глубин |cffffffff3|cffced4da Забытых, способных атаковать врагов и порождать щупальца.|r", {"type": "ability", "id": "A0B7", "field": "ubertip2", "expected": None})
    add_u(10179, "|cffe4cfa3Призыв Забытого|r", {"type": "ability", "id": "A0B7", "field": "researchtip", "expected": "|cffe4cfa3Призыв Забытого|r"})
    add_u(10197, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Призывает из глубин древних Забытых, способных порождать щупальца и сокрушать армии врагов.|n|n"
        "|cffa6afb8Уровень 1:|r призывает |cffffffff1|cffced4da Забытого.|n"
        "|cffa6afb8Уровень 2:|r призывает |cffffffff3|cffced4da Забытых.|r"
    ), {"type": "ability", "id": "A0B7", "field": "researchubertip", "expected": None})
    
    # A0BE: Рассеивание заклинаний (W, 4 levels)
    add_u(8252, "|cffe4cfa3Рассеивание заклинаний|r", {"type": "ability", "id": "A0BE", "field": "name", "expected": "|cffe4cfa3Рассеивание заклинаний|r"})
    add_u(8253, "|cffe4cfa3Рассеивание заклинаний — уровень 1|r (|cffffffffW|r)", {"type": "ability", "id": "A0BE", "field": "tip1", "expected": "|cffe4cfa3Рассеивание заклинаний — уровень 1|r (|cffffffffW|r)"})
    add_u(8256, "|cffe4cfa3Рассеивание заклинаний — уровень 2|r (|cffffffffW|r)", {"type": "ability", "id": "A0BE", "field": "tip2", "expected": "|cffe4cfa3Рассеивание заклинаний — уровень 2|r (|cffffffffW|r)"})
    add_u(8257, "|cffe4cfa3Рассеивание заклинаний — уровень 3|r (|cffffffffW|r)", {"type": "ability", "id": "A0BE", "field": "tip3", "expected": "|cffe4cfa3Рассеивание заклинаний — уровень 3|r (|cffffffffW|r)"})
    add_u(8258, "|cffe4cfa3Рассеивание заклинаний — уровень 4|r (|cffffffffW|r)", {"type": "ability", "id": "A0BE", "field": "tip4", "expected": "|cffe4cfa3Рассеивание заклинаний — уровень 4|r (|cffffffffW|r)"})
    add_u(15474, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает магические эффекты в указанной области и наносит |cffe69a8d200|cffced4da ед. урона призванным существам.|r", {"type": "ability", "id": "A0BE", "field": "ubertip1", "expected": None})
    add_u(15471, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает магические эффекты в указанной области и наносит |cffe69a8d300|cffced4da ед. урона призванным существам.|r", {"type": "ability", "id": "A0BE", "field": "ubertip2", "expected": None})
    add_u(15472, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает магические эффекты в указанной области и наносит |cffe69a8d400|cffced4da ед. урона призванным существам.|r", {"type": "ability", "id": "A0BE", "field": "ubertip3", "expected": None})
    add_u(13534, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает магические эффекты в указанной области и наносит |cffe69a8d600|cffced4da ед. урона призванным существам.|r", {"type": "ability", "id": "A0BE", "field": "ubertip4", "expected": None})
    add_u(8254, "|cffe4cfa3Рассеивание заклинаний|r", {"type": "ability", "id": "A0BE", "field": "researchtip", "expected": "|cffe4cfa3Рассеивание заклинаний|r"})
    add_u(15470, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает магические эффекты с войск в указанной области и наносит урон призванным существам.|n|n"
        "|cffa6afb8Уровень 1:|r наносит |cffe69a8d200|cffced4da урона призывам.|n"
        "|cffa6afb8Уровень 2:|r наносит |cffe69a8d300|cffced4da урона призывам.|n"
        "|cffa6afb8Уровень 3:|r наносит |cffe69a8d400|cffced4da урона призывам.|n"
        "|cffa6afb8Уровень 4:|r наносит |cffe69a8d600|cffced4da урона призывам.|r"
    ), {"type": "ability", "id": "A0BE", "field": "researchubertip", "expected": None})
    
    # A0EN: Метнуть топор (Q, 4 levels)
    add_u(328, "|cffe4cfa3Метнуть топор|r", {"type": "ability", "id": "A0EN", "field": "name", "expected": "|cffe4cfa3Метнуть топор|r"})
    add_u(331, "|cffe4cfa3Метнуть топор — уровень 1|r (|cffffffffQ|r)", {"type": "ability", "id": "A0EN", "field": "tip1", "expected": "|cffe4cfa3Метнуть топор — уровень 1|r (|cffffffffQ|r)"})
    add_u(332, "|cffe4cfa3Метнуть топор — уровень 2|r (|cffffffffQ|r)", {"type": "ability", "id": "A0EN", "field": "tip2", "expected": "|cffe4cfa3Метнуть топор — уровень 2|r (|cffffffffQ|r)"})
    add_u(333, "|cffe4cfa3Метнуть топор — уровень 3|r (|cffffffffQ|r)", {"type": "ability", "id": "A0EN", "field": "tip3", "expected": "|cffe4cfa3Метнуть топор — уровень 3|r (|cffffffffQ|r)"})
    add_u(334, "|cffe4cfa3Метнуть топор — уровень 4|r (|cffffffffQ|r)", {"type": "ability", "id": "A0EN", "field": "tip4", "expected": "|cffe4cfa3Метнуть топор — уровень 4|r (|cffffffffQ|r)"})
    add_u(15346, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает топор, нанося |cffc8e087100|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff0,3|cffced4da сек. героев).|r", {"type": "ability", "id": "A0EN", "field": "ubertip1", "expected": None})
    add_u(15347, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает топор, нанося |cffc8e087200|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff0,4|cffced4da сек. героев).|r", {"type": "ability", "id": "A0EN", "field": "ubertip2", "expected": None})
    add_u(15348, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает топор, нанося |cffc8e087325|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff0,5|cffced4da сек. героев).|r", {"type": "ability", "id": "A0EN", "field": "ubertip3", "expected": None})
    add_u(35263, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает топор, нанося |cffc8e087500|cffced4da ед. урона и оглушая цель на |cffffffff5|cffced4da сек. (|cffffffff0,6|cffced4da сек. героев).|r", {"type": "ability", "id": "A0EN", "field": "ubertip4", "expected": None})
    add_u(329, "|cffe4cfa3Метнуть топор|r", {"type": "ability", "id": "A0EN", "field": "researchtip", "expected": "|cffe4cfa3Метнуть топор|r"})
    add_u(35266, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бросает топор, оглушая цель и нанося ей урон.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087100|cffced4da ед. урона, оглушение 5/0,3 сек.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087200|cffced4da ед. урона, оглушение 5/0,4 сек.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087325|cffced4da ед. урона, оглушение 5/0,5 сек.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087500|cffced4da ед. урона, оглушение 5/0,6 сек.|r"
    ), {"type": "ability", "id": "A0EN", "field": "researchubertip", "expected": None})
    
    # A0I3: Небольшой скачок (C)
    add_u(26484, "|cffe4cfa3Небольшой скачок|r", {"type": "ability", "id": "A0I3", "field": "name", "expected": "|cffe4cfa3Небольшой скачок|r"})
    add_u(26476, "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)", {"type": "ability", "id": "A0I3", "field": "tip1", "expected": "|cffe4cfa3Небольшой скачок|r (|cffffffffC|r)"})
    add_u(26477, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит рабочего на небольшое расстояние.|r", {"type": "ability", "id": "A0I3", "field": "ubertip1", "expected": None})
    add_u(10064, "|cffe4cfa3Небольшой скачок|r", {"type": "ability", "id": "A0I3", "field": "researchtip", "expected": "|cffe4cfa3Небольшой скачок|r"})
    add_u(10976, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Мгновенно переносит рабочего на небольшое расстояние.|r", {"type": "ability", "id": "A0I3", "field": "researchubertip", "expected": None})
    
    # A0IQ: Обозначить столицу (X)
    add_u(27193, "|cffe4cfa3Обозначить столицу|r", {"type": "ability", "id": "A0IQ", "field": "name", "expected": "|cffe4cfa3Обозначить столицу|r"})
    add_u(27969, "|cffe4cfa3Обозначить столицу|r (|cffffffffX|r)", {"type": "ability", "id": "A0IQ", "field": "tip1", "expected": "|cffe4cfa3Обозначить столицу|r (|cffffffffX|r)"})
    add_u(27970, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Назначает главное здание столицей игрока, многократно увеличивая его запас прочности.|n|n"
        "|cffe6c07bВнимание:|r при потере столицы вы терпите поражение или переходите в статус вассала.|r"
    ), {"type": "ability", "id": "A0IQ", "field": "ubertip1", "expected": None})
    
    # A0LI: Обмен Золота на Дерево (S)
    add_u(2888, "|cffe4cfa3Обмен золота на дерево|r", {"type": "ability", "id": "A0LI", "field": "name", "expected": "|cffe4cfa3Обмен золота на дерево|r"})
    add_u(3692, "|cffe4cfa3Обмен золота на дерево|r (|cffffffffS|r)", {"type": "ability", "id": "A0LI", "field": "tip1", "expected": "|cffe4cfa3Обмен золота на дерево|r (|cffffffffS|r)"})
    add_u(20630, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обменивает |cffe69a8d500|cffced4da ед. золота на |cffc8e087100|cffced4da ед. древесины.|r", {"type": "ability", "id": "A0LI", "field": "ubertip1", "expected": None})
    
    # A0LJ: Обмен Дерева на Золото (A)
    add_u(12857, "|cffe4cfa3Обмен дерева на золото|r", {"type": "ability", "id": "A0LJ", "field": "name", "expected": "|cffe4cfa3Обмен дерева на золото|r"})
    add_u(12886, "|cffe4cfa3Обмен дерева на золото|r (|cffffffffA|r)", {"type": "ability", "id": "A0LJ", "field": "tip1", "expected": "|cffe4cfa3Обмен дерева на золото|r (|cffffffffA|r)"})
    add_u(20631, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Обменивает |cffe69a8d500|cffced4da ед. древесины на |cffc8e087100|cffced4da ед. золота.|r", {"type": "ability", "id": "A0LJ", "field": "ubertip1", "expected": None})
    
    # A0N7: Перст боли (Q, 4 levels)
    add_u(12036, "|cffe4cfa3Перст боли|r", {"type": "ability", "id": "A0N7", "field": "name", "expected": "|cffe4cfa3Перст боли|r"})
    add_u(13211, "|cffe4cfa3Перст боли — уровень 1|r (|cffffffffQ|r)", {"type": "ability", "id": "A0N7", "field": "tip1", "expected": "|cffe4cfa3Перст боли — уровень 1|r (|cffffffffQ|r)"})
    add_u(13207, "|cffe4cfa3Перст боли — уровень 2|r (|cffffffffQ|r)", {"type": "ability", "id": "A0N7", "field": "tip2", "expected": "|cffe4cfa3Перст боли — уровень 2|r (|cffffffffQ|r)"})
    add_u(12040, "|cffe4cfa3Перст боли — уровень 3|r (|cffffffffQ|r)", {"type": "ability", "id": "A0N7", "field": "tip3", "expected": "|cffe4cfa3Перст боли — уровень 3|r (|cffffffffQ|r)"})
    add_u(13261, "|cffe4cfa3Перст боли — уровень 4|r (|cffffffffQ|r)", {"type": "ability", "id": "A0N7", "field": "tip4", "expected": "|cffe4cfa3Перст боли — уровень 4|r (|cffffffffQ|r)"})
    add_u(13245, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Темный разряд, последовательно поражающий до |cffffffff4|cffced4da врагов и наносящий первому |cffc8e08785|cffced4da ед. урона.|r", {"type": "ability", "id": "A0N7", "field": "ubertip1", "expected": None})
    add_u(13224, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Темный разряд, последовательно поражающий до |cffffffff6|cffced4da врагов и наносящий первому |cffc8e087160|cffced4da ед. урона.|r", {"type": "ability", "id": "A0N7", "field": "ubertip2", "expected": None})
    add_u(13249, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Темный разряд, последовательно поражающий до |cffffffff8|cffced4da врагов и наносящий первому |cffc8e087250|cffced4da ед. урона.|r", {"type": "ability", "id": "A0N7", "field": "ubertip3", "expected": None})
    add_u(30564, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Темный разряд, последовательно поражающий до |cffffffff12|cffced4da врагов и наносящий первому |cffc8e087355|cffced4da ед. урона.|r", {"type": "ability", "id": "A0N7", "field": "ubertip4", "expected": None})
    add_u(12831, "|cffe4cfa3Перст боли|r", {"type": "ability", "id": "A0N7", "field": "researchtip", "expected": "|cffe4cfa3Перст боли|r"})
    add_u(29002, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Темный разряд, последовательно поражающий нескольких противников с постепенным снижением урона.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e08785|cffced4da ед. урона, до 4 целей.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087160|cffced4da ед. урона, до 6 целей.|n"
        "|cffa6afb8Уровень 3:|r |cffc8e087250|cffced4da ед. урона, до 8 целей.|n"
        "|cffa6afb8Уровень 4:|r |cffc8e087355|cffced4da ед. урона, до 12 целей.|r"
    ), {"type": "ability", "id": "A0N7", "field": "researchubertip", "expected": None})
    
    # A14L: Рассеивание чар (Q)
    add_u(27493, "|cffe4cfa3Рассеивание чар|r", {"type": "ability", "id": "A14L", "field": "name", "expected": "|cffe4cfa3Рассеивание чар|r"})
    add_u(27494, "|cffe4cfa3Рассеивание чар|r (|cffffffffQ|r)", {"type": "ability", "id": "A14L", "field": "tip1", "expected": "|cffe4cfa3Рассеивание чар|r (|cffffffffQ|r)"})
    add_u(27502, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снимает положительные эффекты с врагов и отрицательные с союзников в указанной области, а также наносит урон призывам.|r", {"type": "ability", "id": "A14L", "field": "ubertip1", "expected": None})
    
    # Tier 2 Upgrade Abilities: A1HW, A1HX, A1HY, A1HZ, A1I0, A1I1, A1I2, A1I3
    # A1HW: Кодо T2 (X)
    add_u(24916, "|cffe4cfa3Кодо Скверны — ранг 2|r", {"type": "ability", "id": "A1HW", "field": "name", "expected": "|cffe4cfa3Кодо Скверны — ранг 2|r"})
    add_u(25175, "|cffe4cfa3Кодо Скверны — ранг 2|r (|cffffffffX|r)", {"type": "ability", "id": "A1HW", "field": "tip1", "expected": "|cffe4cfa3Кодо Скверны — ранг 2|r (|cffffffffX|r)"})
    add_u(34734, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает кодо Скверны, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deНалетчиков Скверны|r.|r"
    ), {"type": "ability", "id": "A1HW", "field": "ubertip1", "expected": None})
    
    # A1HX: Копьеметатель T2 (X)
    add_u(34458, "|cffe4cfa3Копьеметатель — ранг 2|r", {"type": "ability", "id": "A1HX", "field": "name", "expected": "|cffe4cfa3Копьеметатель — ранг 2|r"})
    add_u(34459, "|cffe4cfa3Копьеметатель — ранг 2|r (|cffffffffX|r)", {"type": "ability", "id": "A1HX", "field": "tip1", "expected": "|cffe4cfa3Копьеметатель — ранг 2|r (|cffffffffX|r)"})
    add_u(34753, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает копьеметателей, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deСтрелков|r.|r"
    ), {"type": "ability", "id": "A1HX", "field": "ubertip1", "expected": None})
    
    # A1HY: Налетчик T2 (Q)
    add_u(30203, "|cffe4cfa3Налетчик Скверны — ранг 2|r", {"type": "ability", "id": "A1HY", "field": "name", "expected": "|cffe4cfa3Налетчик Скверны — ранг 2|r"})
    add_u(30243, "|cffe4cfa3Налетчик Скверны — ранг 2|r (|cffffffffQ|r)", {"type": "ability", "id": "A1HY", "field": "tip1", "expected": "|cffe4cfa3Налетчик Скверны — ранг 2|r (|cffffffffQ|r)"})
    add_u(35501, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает налетчиков Скверны, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deКодо Скверны|r.|r"
    ), {"type": "ability", "id": "A1HY", "field": "ubertip1", "expected": None})
    
    # A1HZ: Рубака T2 (Z)
    add_u(34240, "|cffe4cfa3Рубака Скверны — ранг 2|r", {"type": "ability", "id": "A1HZ", "field": "name", "expected": "|cffe4cfa3Рубака Скверны — ранг 2|r"})
    add_u(34241, "|cffe4cfa3Рубака Скверны — ранг 2|r (|cffffffffZ|r)", {"type": "ability", "id": "A1HZ", "field": "tip1", "expected": "|cffe4cfa3Рубака Скверны — ранг 2|r (|cffffffffZ|r)"})
    add_u(35236, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает рубак Скверны, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deТелохранителей вождя|r.|r"
    ), {"type": "ability", "id": "A1HZ", "field": "ubertip1", "expected": None})
    
    # A1I0: Стрелок T2 (C)
    add_u(34555, "|cffe4cfa3Стрелок — ранг 2|r", {"type": "ability", "id": "A1I0", "field": "name", "expected": "|cffe4cfa3Стрелок — ранг 2|r"})
    add_u(34556, "|cffe4cfa3Стрелок — ранг 2|r (|cffffffffC|r)", {"type": "ability", "id": "A1I0", "field": "tip1", "expected": "|cffe4cfa3Стрелок — ранг 2|r (|cffffffffC|r)"})
    add_u(35838, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает стрелков, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deКопьеметателей|r.|r"
    ), {"type": "ability", "id": "A1I0", "field": "ubertip1", "expected": None})
    
    # A1I1: Телохранитель T2 (C)
    add_u(34247, "|cffe4cfa3Телохранитель вождя — ранг 2|r", {"type": "ability", "id": "A1I1", "field": "name", "expected": "|cffe4cfa3Телохранитель вождя — ранг 2|r"})
    add_u(34248, "|cffe4cfa3Телохранитель вождя — ранг 2|r (|cffffffffC|r)", {"type": "ability", "id": "A1I1", "field": "tip1", "expected": "|cffe4cfa3Телохранитель вождя — ранг 2|r (|cffffffffC|r)"})
    add_u(35839, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает телохранителей вождя, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deРубак Скверны|r.|r"
    ), {"type": "ability", "id": "A1I1", "field": "ubertip1", "expected": None})
    
    # A1I2: Чернокнижник T2 (Q)
    add_u(9353, "|cffe4cfa3Чернокнижник Скверны — ранг 2|r", {"type": "ability", "id": "A1I2", "field": "name", "expected": "|cffe4cfa3Чернокнижник Скверны — ранг 2|r"})
    add_u(12215, "|cffe4cfa3Чернокнижник Скверны — ранг 2|r (|cffffffffQ|r)", {"type": "ability", "id": "A1I2", "field": "tip1", "expected": "|cffe4cfa3Чернокнижник Скверны — ранг 2|r (|cffffffffQ|r)"})
    add_u(35840, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает чернокнижников Скверны, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deШаманов|r.|r"
    ), {"type": "ability", "id": "A1I2", "field": "ubertip1", "expected": None})
    
    # A1I3: Шаман T2 (Q)
    add_u(26566, "|cffe4cfa3Шаман — ранг 2|r", {"type": "ability", "id": "A1I3", "field": "name", "expected": "|cffe4cfa3Шаман — ранг 2|r"})
    add_u(26571, "|cffe4cfa3Шаман — ранг 2|r (|cffffffffQ|r)", {"type": "ability", "id": "A1I3", "field": "tip1", "expected": "|cffe4cfa3Шаман — ранг 2|r (|cffffffffQ|r)"})
    add_u(23431, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает шаманов, повышая их боевые характеристики до 2 ранга.|n|n"
        "|cffe6c07bВнимание:|r исключает возможность усиления |cffa9c7deЧернокнижников Скверны|r.|r"
    ), {"type": "ability", "id": "A1I3", "field": "ubertip1", "expected": None})
    
    # A1II: Отражение скверны (E, 4 levels)
    add_u(35908, "|cffe4cfa3Отражение скверны|r", {"type": "ability", "id": "A1II", "field": "name", "expected": "|cffe4cfa3Отражение скверны|r"})
    add_u(35911, "|cffe4cfa3Отражение скверны — уровень 1|r (|cffffffffE|r)", {"type": "ability", "id": "A1II", "field": "tip1", "expected": "|cffe4cfa3Отражение скверны — уровень 1|r (|cffffffffE|r)"})
    add_u(35912, "|cffe4cfa3Отражение скверны — уровень 2|r (|cffffffffE|r)", {"type": "ability", "id": "A1II", "field": "tip2", "expected": "|cffe4cfa3Отражение скверны — уровень 2|r (|cffffffffE|r)"})
    add_u(35913, "|cffe4cfa3Отражение скверны — уровень 3|r (|cffffffffE|r)", {"type": "ability", "id": "A1II", "field": "tip3", "expected": "|cffe4cfa3Отражение скверны — уровень 3|r (|cffffffffE|r)"})
    add_u(35906, "|cffe4cfa3Отражение скверны — уровень 4|r (|cffffffffE|r)", {"type": "ability", "id": "A1II", "field": "tip4", "expected": "|cffe4cfa3Отражение скверны — уровень 4|r (|cffffffffE|r)"})
    add_u(35907, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает союзников щитом, отражающим |cffc8e08721%|cffced4da полученного урона ближнего боя обратно атакующим врагам.|r", {"type": "ability", "id": "A1II", "field": "ubertip4", "expected": None})
    add_u(35909, "|cffe4cfa3Отражение скверны|r", {"type": "ability", "id": "A1II", "field": "researchtip", "expected": "|cffe4cfa3Отражение скверны|r"})
    add_u(35910, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует щит, отражающий часть получаемого в ближнем бою урона обратно врагам.|n|n"
        "|cffa6afb8Уровень 1:|r отражает |cffc8e08710%|cffced4da урона.|n"
        "|cffa6afb8Уровень 2:|r отражает |cffc8e08713%|cffced4da урона.|n"
        "|cffa6afb8Уровень 3:|r отражает |cffc8e08717%|cffced4da урона.|n"
        "|cffa6afb8Уровень 4:|r отражает |cffc8e08721%|cffced4da урона.|r"
    ), {"type": "ability", "id": "A1II", "field": "researchubertip", "expected": None})
    
    # Tier 3 Upgrade Abilities: A1IM, A1IN, A1IO, A1IP, A1IQ, A1IR, A1IS, A1IT
    # A1IM: Кодо T3 (X)
    add_u(28119, "|cffe4cfa3Кодо Скверны — ранг 3|r", {"type": "ability", "id": "A1IM", "field": "name", "expected": "|cffe4cfa3Кодо Скверны — ранг 3|r"})
    add_u(28127, "|cffe4cfa3Кодо Скверны — ранг 3|r (|cffffffffX|r)", {"type": "ability", "id": "A1IM", "field": "tip1", "expected": "|cffe4cfa3Кодо Скверны — ранг 3|r (|cffffffffX|r)"})
    add_u(35753, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает кодо Скверны, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IM", "field": "ubertip1", "expected": None})
    
    # A1IN: Копьеметатель T3 (Q)
    add_u(34538, "|cffe4cfa3Копьеметатель — ранг 3|r", {"type": "ability", "id": "A1IN", "field": "name", "expected": "|cffe4cfa3Копьеметатель — ранг 3|r"})
    add_u(34539, "|cffe4cfa3Копьеметатель — ранг 3|r (|cffffffffQ|r)", {"type": "ability", "id": "A1IN", "field": "tip1", "expected": "|cffe4cfa3Копьеметатель — ранг 3|r (|cffffffffQ|r)"})
    add_u(35754, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает копьеметателей, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IN", "field": "ubertip1", "expected": None})
    
    # A1IO: Налетчик T3 (Q)
    add_u(31567, "|cffe4cfa3Налетчик Скверны — ранг 3|r", {"type": "ability", "id": "A1IO", "field": "name", "expected": "|cffe4cfa3Налетчик Скверны — ранг 3|r"})
    add_u(32051, "|cffe4cfa3Налетчик Скверны — ранг 3|r (|cffffffffQ|r)", {"type": "ability", "id": "A1IO", "field": "tip1", "expected": "|cffe4cfa3Налетчик Скверны — ранг 3|r (|cffffffffQ|r)"})
    add_u(35755, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает налетчиков Скверны, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IO", "field": "ubertip1", "expected": None})
    
    # A1IP: Рубака T3 (Z)
    add_u(34242, "|cffe4cfa3Рубака Скверны — ранг 3|r", {"type": "ability", "id": "A1IP", "field": "name", "expected": "|cffe4cfa3Рубака Скверны — ранг 3|r"})
    add_u(35017, "|cffe4cfa3Рубака Скверны — ранг 3|r (|cffffffffZ|r)", {"type": "ability", "id": "A1IP", "field": "tip1", "expected": "|cffe4cfa3Рубака Скверны — ранг 3|r (|cffffffffZ|r)"})
    add_u(35756, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает рубак Скверны, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IP", "field": "ubertip1", "expected": None})
    
    # A1IQ: Стрелок T3 (Q)
    add_u(34557, "|cffe4cfa3Стрелок — ранг 3|r", {"type": "ability", "id": "A1IQ", "field": "name", "expected": "|cffe4cfa3Стрелок — ранг 3|r"})
    add_u(34561, "|cffe4cfa3Стрелок — ранг 3|r (|cffffffffQ|r)", {"type": "ability", "id": "A1IQ", "field": "tip1", "expected": "|cffe4cfa3Стрелок — ранг 3|r (|cffffffffQ|r)"})
    add_u(35757, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает стрелков, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IQ", "field": "ubertip1", "expected": None})
    
    # A1IR: Телохранитель T3 (C)
    add_u(34249, "|cffe4cfa3Телохранитель вождя — ранг 3|r", {"type": "ability", "id": "A1IR", "field": "name", "expected": "|cffe4cfa3Телохранитель вождя — ранг 3|r"})
    add_u(34257, "|cffe4cfa3Телохранитель вождя — ранг 3|r (|cffffffffC|r)", {"type": "ability", "id": "A1IR", "field": "tip1", "expected": "|cffe4cfa3Телохранитель вождя — ранг 3|r (|cffffffffC|r)"})
    add_u(35758, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает телохранителей вождя, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IR", "field": "ubertip1", "expected": None})
    
    # A1IS: Чернокнижник T3 (Q)
    add_u(12302, "|cffe4cfa3Чернокнижник Скверны — ранг 3|r", {"type": "ability", "id": "A1IS", "field": "name", "expected": "|cffe4cfa3Чернокнижник Скверны — ранг 3|r"})
    add_u(12845, "|cffe4cfa3Чернокнижник Скверны — ранг 3|r (|cffffffffQ|r)", {"type": "ability", "id": "A1IS", "field": "tip1", "expected": "|cffe4cfa3Чернокнижник Скверны — ранг 3|r (|cffffffffQ|r)"})
    add_u(35769, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает чернокнижников Скверны, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IS", "field": "ubertip1", "expected": None})
    
    # A1IT: Шаман T3 (Q)
    add_u(26581, "|cffe4cfa3Шаман — ранг 3|r", {"type": "ability", "id": "A1IT", "field": "name", "expected": "|cffe4cfa3Шаман — ранг 3|r"})
    add_u(26601, "|cffe4cfa3Шаман — ранг 3|r (|cffffffffQ|r)", {"type": "ability", "id": "A1IT", "field": "tip1", "expected": "|cffe4cfa3Шаман — ранг 3|r (|cffffffffQ|r)"})
    add_u(35770, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Усиливает шаманов, повышая их боевые характеристики до высшего 3 ранга.|r", {"type": "ability", "id": "A1IT", "field": "ubertip1", "expected": None})
    
    # A1IU: Ярость (passive)
    add_u(36339, "|cffe4cfa3Ярость|r", {"type": "ability", "id": "A1IU", "field": "name", "expected": "|cffe4cfa3Ярость|r"})
    add_u(36340, "|cffe4cfa3Ярость|r", {"type": "ability", "id": "A1IU", "field": "tip1", "expected": "|cffe4cfa3Ярость|r"})
    add_u(30229, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Позволяет воинам Скверны балансировать между повышенным уроном и запасом здоровья.|r", {"type": "ability", "id": "A1IU", "field": "ubertip1", "expected": None})
    
    # A1IV: Огненная стрела (чернокнижник, W)
    add_u(36342, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Выпускает сгусток темного огня, наносящий |cffc8e087100|cffced4da ед. урона и оглушающий цель.|r", {"type": "ability", "id": "A1IV", "field": "ubertip1", "expected": None})
    
    # A1IW: Раздвоенная молния (шаман, Q)
    add_u(36344, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поражает молнией до |cffffffff3|cffced4da врагов в секторе перед собой, нанося |cffc8e087100|cffced4da ед. урона.|r", {"type": "ability", "id": "A1IW", "field": "ubertip1", "expected": None})
    
    # A1IX: Жажда крови (шаман, W)
    add_u(36345, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает скорость атаки союзника на |cffc8e087+40%|cffced4da и скорость передвижения на |cffc8e087+25%|cffced4da на |cffffffff30|cffced4da сек.|r", {"type": "ability", "id": "A1IX", "field": "ubertip1", "expected": None})
    
    # A1IY: Критический удар (passive)
    add_u(36347, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff15%|cffced4da шанс нанести двукратный урон при атаке.|r", {"type": "ability", "id": "A1IY", "field": "ubertip1", "expected": None})
    
    # A1IZ: Заточеный болт (стрелок, passive)
    add_u(36348, "|cffe4cfa3Заточеный болт|r", {"type": "ability", "id": "A1IZ", "field": "name", "expected": "|cffe4cfa3Заточеный болт|r"})
    add_u(36349, "|cffe4cfa3Заточеный болт|r", {"type": "ability", "id": "A1IZ", "field": "tip1", "expected": "|cffe4cfa3Заточеный болт|r"})
    add_u(36350, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Наносит дополнительный урон по врагам с тяжелым типом брони.|r", {"type": "ability", "id": "A1IZ", "field": "ubertip1", "expected": None})
    
    # A1J1: Вой (налетчик, E)
    add_u(26997, "|cffe4cfa3Вой|r", {"type": "ability", "id": "A1J1", "field": "name", "expected": "|cffe4cfa3Вой|r"})
    add_u(26991, "|cffe4cfa3Вой|r (|cffffffffE|r)", {"type": "ability", "id": "A1J1", "field": "tip1", "expected": "|cffe4cfa3Вой|r (|cffffffffE|r)"})
    add_u(26998, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Издает свирепый вой, повышающий урон союзников на |cffc8e087+25%|cffced4da и броню на |cffc8e087+4|cffced4da ед. на |cffffffff30|cffced4da сек.|r", {"type": "ability", "id": "A1J1", "field": "ubertip1", "expected": None})
    
    # A1J3: Берсерк (Q)
    add_u(26999, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+50%|cffced4da ценой увеличения получаемого урона на |cffe69a8d+20%|cffced4da.|r", {"type": "ability", "id": "A1J3", "field": "ubertip1", "expected": None})
    
    # A1J4: Сильный удар (passive)
    add_u(37641, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da С вероятностью |cffffffff15%|cffced4da наносит на |cffc8e087+20|cffced4da ед. больше урона и оглушает цель на |cffffffff2|cffced4da сек.|r", {"type": "ability", "id": "A1J4", "field": "ubertip1", "expected": None})
    
    # A1J5: Огненный болт (W)
    add_u(30230, "|cffe4cfa3Огненный болт|r", {"type": "ability", "id": "A1J5", "field": "name", "expected": "|cffe4cfa3Огненный болт|r"})
    add_u(30231, "|cffe4cfa3Огненный болт|r (|cffffffffW|r)", {"type": "ability", "id": "A1J5", "field": "tip1", "expected": "|cffe4cfa3Огненный болт|r (|cffffffffW|r)"})
    add_u(30296, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Добавляет дополнительный огненный урон к каждой дистанционной атаке.|r", {"type": "ability", "id": "A1J5", "field": "ubertip1", "expected": None})
    
    # A1J7: Аура выносливости (кодо, passive)
    add_u(36597, "|cffe4cfa3Аура выносливости|r", {"type": "ability", "id": "A1J7", "field": "tip1", "expected": "|cffe4cfa3Аура выносливости|r"})
    add_u(36598, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость передвижения находящихся рядом союзников на |cffc8e087+10%|cffced4da и скорость их атаки на |cffc8e087+5%|cffced4da.|r", {"type": "ability", "id": "A1J7", "field": "ubertip1", "expected": None})
    
    # A1J8: Всплеск ярости (W, 4 levels)
    add_u(35204, "|cffe4cfa3Всплеск ярости|r", {"type": "ability", "id": "A1J8", "field": "name", "expected": "|cffe4cfa3Всплеск ярости|r"})
    add_u(35283, "|cffe4cfa3Всплеск ярости — уровень 1|r (|cffffffffW|r)", {"type": "ability", "id": "A1J8", "field": "tip1", "expected": "|cffe4cfa3Всплеск ярости — уровень 1|r (|cffffffffW|r)"})
    add_u(35285, "|cffe4cfa3Всплеск ярости — уровень 2|r (|cffffffffW|r)", {"type": "ability", "id": "A1J8", "field": "tip2", "expected": "|cffe4cfa3Всплеск ярости — уровень 2|r (|cffffffffW|r)"})
    add_u(35289, "|cffe4cfa3Всплеск ярости — уровень 3|r (|cffffffffW|r)", {"type": "ability", "id": "A1J8", "field": "tip3", "expected": "|cffe4cfa3Всплеск ярости — уровень 3|r (|cffffffffW|r)"})
    add_u(35295, "|cffe4cfa3Всплеск ярости — уровень 4|r (|cffffffffW|r)", {"type": "ability", "id": "A1J8", "field": "tip4", "expected": "|cffe4cfa3Всплеск ярости — уровень 4|r (|cffffffffW|r)"})
    add_u(31220, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+400%|cffced4da, но увеличивает получаемый урон на |cffe69a8d+50%|cffced4da на |cffffffff12|cffced4da сек.|r", {"type": "ability", "id": "A1J8", "field": "ubertip1", "expected": None})
    add_u(19976, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+400%|cffced4da, но увеличивает получаемый урон на |cffe69a8d+45%|cffced4da на |cffffffff12|cffced4da сек.|r", {"type": "ability", "id": "A1J8", "field": "ubertip2", "expected": None})
    add_u(21300, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+400%|cffced4da, но увеличивает получаемый урон на |cffe69a8d+40%|cffced4da на |cffffffff12|cffced4da сек.|r", {"type": "ability", "id": "A1J8", "field": "ubertip3", "expected": None})
    add_u(32754, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Увеличивает скорость атаки на |cffc8e087+400%|cffced4da, но увеличивает получаемый урон на |cffe69a8d+35%|cffced4da на |cffffffff12|cffced4da сек.|r", {"type": "ability", "id": "A1J8", "field": "ubertip4", "expected": None})
    add_u(35281, "|cffe4cfa3Всплеск ярости|r", {"type": "ability", "id": "A1J8", "field": "researchtip", "expected": "|cffe4cfa3Всплеск ярости|r"})
    add_u(35316, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Многократно увеличивает скорость боя ценой получения повышенного урона. Действует 12 сек.|n|n"
        "|cffa6afb8Уровень 1:|r +400% скорости, +50% получаемого урона.|n"
        "|cffa6afb8Уровень 2:|r +400% скорости, +45% получаемого урона.|n"
        "|cffa6afb8Уровень 3:|r +400% скорости, +40% получаемого урона.|n"
        "|cffa6afb8Уровень 4:|r +400% скорости, +35% получаемого урона.|r"
    ), {"type": "ability", "id": "A1J8", "field": "researchubertip", "expected": None})
    
    # A1J9: Разкол (R, 2 levels)
    add_u(36680, "|cffe4cfa3Разкол|r", {"type": "ability", "id": "A1J9", "field": "name", "expected": "|cffe4cfa3Разкол|r"})
    add_u(37036, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сокрушает землю, нанося |cffc8e087400|cffced4da ед. урона наземным врагам и замедляя их скорость передвижения и атаки.|r", {"type": "ability", "id": "A1J9", "field": "ubertip1", "expected": None})
    add_u(37037, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сокрушает землю, нанося |cffc8e087500|cffced4da ед. урона наземным врагам и замедляя их скорость передвижения и атаки.|r", {"type": "ability", "id": "A1J9", "field": "ubertip2", "expected": None})
    add_u(37035, "|cffe4cfa3Разкол|r", {"type": "ability", "id": "A1J9", "field": "researchtip", "expected": "|cffe4cfa3Разкол|r"})
    add_u(37034, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Сокрушает землю, нанося урон наземным врагам вокруг и существенно замедляя их атаку и бег.|n|n"
        "|cffa6afb8Уровень 1:|r |cffc8e087400|cffced4da ед. урона.|n"
        "|cffa6afb8Уровень 2:|r |cffc8e087500|cffced4da ед. урона.|r"
    ), {"type": "ability", "id": "A1J9", "field": "researchubertip", "expected": None})
    
    # A1JG: Воскрешение мертвых (Q, 2 levels)
    add_u(11947, "|cffe4cfa3Воскрешение мертвых|r (|cffffffffQ|r)", {"type": "ability", "id": "A1JG", "field": "tip2", "expected": "|cffe4cfa3Воскрешение мертвых|r (|cffffffffQ|r)"})
    add_u(7614, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Поднимает |cffffffff2|cffced4da скелетов из трупа павшего воина.|r", {"type": "ability", "id": "A1JG", "field": "ubertip2", "expected": None})
    
    # A1JH: Ритуал некромантии (R)
    add_u(11982, "|cffe4cfa3Ритуал некромантии|r", {"type": "ability", "id": "A1JH", "field": "name", "expected": "|cffe4cfa3Ритуал некромантии|r"})
    add_u(11983, "|cffe4cfa3Ритуал некромантии|r (|cffffffffR|r)", {"type": "ability", "id": "A1JH", "field": "tip1", "expected": "|cffe4cfa3Ритуал некромантии|r (|cffffffffR|r)"})
    add_u(23530, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Открывает доступ к возведению |cffa9c7deЧертогов мертвых|cffced4da и подготовке некромантов.|n|n"
        "|cffe6c07bВнимание:|r исключает проведение |cffa9c7deРитуала мутации|r.|r"
    ), {"type": "ability", "id": "A1JH", "field": "ubertip1", "expected": None})
    
    # A1JI: Ритуал мутации (E)
    add_u(11987, "|cffe4cfa3Ритуал мутации|r", {"type": "ability", "id": "A1JI", "field": "name", "expected": "|cffe4cfa3Ритуал мутации|r"})
    add_u(23429, "|cffe4cfa3Ритуал мутации|r (|cffffffffE|r)", {"type": "ability", "id": "A1JI", "field": "tip1", "expected": "|cffe4cfa3Ритуал мутации|r (|cffffffffE|r)"})
    add_u(35841, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Открывает доступ к подготовке |cffa9c7deМутировавших батраков|cffced4da в Доме вождей.|n|n"
        "|cffe6c07bВнимание:|r исключает проведение |cffa9c7deРитуала некромантии|r.|r"
    ), {"type": "ability", "id": "A1JI", "field": "ubertip1", "expected": None})
    
    # A1JK: Ускользание (passive, 4 levels)
    add_u(14299, "|cffe4cfa3Ускользание|r", {"type": "ability", "id": "A1JK", "field": "name", "expected": "|cffe4cfa3Ускользание|r"})
    add_u(26358, "|cffe4cfa3Ускользание — уровень 1|r", {"type": "ability", "id": "A1JK", "field": "tip1", "expected": "|cffe4cfa3Ускользание — уровень 1|r"})
    add_u(15961, "|cffe4cfa3Ускользание — уровень 2|r", {"type": "ability", "id": "A1JK", "field": "tip2", "expected": "|cffe4cfa3Ускользание — уровень 2|r"})
    add_u(17725, "|cffe4cfa3Ускользание — уровень 3|r", {"type": "ability", "id": "A1JK", "field": "tip3", "expected": "|cffe4cfa3Ускользание — уровень 3|r"})
    add_u(17731, "|cffe4cfa3Ускользание — уровень 4|r", {"type": "ability", "id": "A1JK", "field": "tip4", "expected": "|cffe4cfa3Ускользание — уровень 4|r"})
    add_u(15269, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff10%|cffced4da шанс уклониться от вражеской атаки.|r", {"type": "ability", "id": "A1JK", "field": "ubertip1", "expected": None})
    add_u(15270, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff20%|cffced4da шанс уклониться от вражеской атаки.|r", {"type": "ability", "id": "A1JK", "field": "ubertip2", "expected": None})
    add_u(17797, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff30%|cffced4da шанс уклониться от вражеской атаки.|r", {"type": "ability", "id": "A1JK", "field": "ubertip3", "expected": None})
    add_u(17800, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff40%|cffced4da шанс уклониться от вражеской атаки.|r", {"type": "ability", "id": "A1JK", "field": "ubertip4", "expected": None})
    add_u(14300, "|cffe4cfa3Ускользание|r", {"type": "ability", "id": "A1JK", "field": "researchtip", "expected": "|cffe4cfa3Ускользание|r"})
    add_u(15273, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает вероятность уклониться от физической атаки противника.|n|n"
        "|cffa6afb8Уровень 1:|r |cffffffff10%|cffced4da шанс уклонения.|n"
        "|cffa6afb8Уровень 2:|r |cffffffff20%|cffced4da шанс уклонения.|n"
        "|cffa6afb8Уровень 3:|r |cffffffff30%|cffced4da шанс уклонения.|n"
        "|cffa6afb8Уровень 4:|r |cffffffff40%|cffced4da шанс уклонения.|r"
    ), {"type": "ability", "id": "A1JK", "field": "researchubertip", "expected": None})
    
    # A1JP: Рассекающий удар (мутировавший батрак, passive)
    add_u(39228, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Бьет с огромной силой, нанося |cffc8e08715%|cffced4da урона врагам рядом с основной целью.|r", {"type": "ability", "id": "A1JP", "field": "ubertip1", "expected": None})
    
    # A1KB: Защита столицы (passive)
    add_u(38201, "|cffe4cfa3Защита столицы|r", {"type": "ability", "id": "A1KB", "field": "name", "expected": "|cffe4cfa3Защита столицы|r"})
    add_u(38229, "|cffe4cfa3Защита столицы|r", {"type": "ability", "id": "A1KB", "field": "tip1", "expected": "|cffe4cfa3Защита столицы|r"})
    
    # A1MC: Аура Защиты (телохранитель, passive)
    add_u(39203, "|cffe4cfa3Аура Защиты|r", {"type": "ability", "id": "A1MC", "field": "name", "expected": "|cffe4cfa3Аура Защиты|r"})
    add_u(39204, "|cffe4cfa3Аура Защиты|r", {"type": "ability", "id": "A1MC", "field": "tip1", "expected": "|cffe4cfa3Аура Защиты|r"})
    add_u(22257, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Повышает броню находящихся рядом союзников на |cffc8e087+3|cffced4da ед.|r", {"type": "ability", "id": "A1MC", "field": "ubertip1", "expected": None})
    
    # A1MD: Аура Страха (N072, passive, 4 levels)
    add_u(39207, "|cffe4cfa3Аура Страха|r", {"type": "ability", "id": "A1MD", "field": "name", "expected": "|cffe4cfa3Аура Страха|r"})
    add_u(39209, "|cffe4cfa3Аура Страха — уровень 1|r", {"type": "ability", "id": "A1MD", "field": "tip1", "expected": "|cffe4cfa3Аура Страха — уровень 1|r"})
    add_u(39210, "|cffe4cfa3Аура Страха — уровень 2|r", {"type": "ability", "id": "A1MD", "field": "tip2", "expected": "|cffe4cfa3Аура Страха — уровень 2|r"})
    add_u(39211, "|cffe4cfa3Аура Страха — уровень 3|r", {"type": "ability", "id": "A1MD", "field": "tip3", "expected": "|cffe4cfa3Аура Страха — уровень 3|r"})
    add_u(39212, "|cffe4cfa3Аура Страха — уровень 4|r", {"type": "ability", "id": "A1MD", "field": "tip4", "expected": "|cffe4cfa3Аура Страха — уровень 4|r"})
    add_u(39214, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает скорость передвижения врагов на |cffe69a8d-7%|cffced4da и скорость атаки на |cffe69a8d-5%|cffced4da.|r", {"type": "ability", "id": "A1MD", "field": "ubertip1", "expected": None})
    add_u(39215, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает скорость передвижения врагов на |cffe69a8d-14%|cffced4da и скорость атаки на |cffe69a8d-10%|cffced4da.|r", {"type": "ability", "id": "A1MD", "field": "ubertip2", "expected": None})
    add_u(39216, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает скорость передвижения врагов на |cffe69a8d-21%|cffced4da и скорость атаки на |cffe69a8d-15%|cffced4da.|r", {"type": "ability", "id": "A1MD", "field": "ubertip3", "expected": None})
    add_u(39213, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Снижает скорость передвижения врагов на |cffe69a8d-28%|cffced4da и скорость атаки на |cffe69a8d-20%|cffced4da.|r", {"type": "ability", "id": "A1MD", "field": "ubertip4", "expected": None})
    add_u(8749, (
        "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Подавляет боевой дух находящихся рядом врагов, замедляя их скорость атаки и передвижения.|n|n"
        "|cffa6afb8Уровень 1:|r -7% к скорости бега, -5% к скорости боя.|n"
        "|cffa6afb8Уровень 2:|r -14% к скорости бега, -10% к скорости боя.|n"
        "|cffa6afb8Уровень 3:|r -21% к скорости бега, -15% к скорости боя.|n"
        "|cffa6afb8Уровень 4:|r -28% к скорости бега, -20% к скорости боя.|r"
    ), {"type": "ability", "id": "A1MD", "field": "researchubertip", "expected": None})
    
    # AOcr: Критический удар (N073, passive, level 4)
    add_u(9628, "|cffe4cfa3Критический удар — уровень 4|r", {"type": "ability", "id": "AOcr", "field": "tip4", "expected": "|cffe4cfa3Критический удар — уровень 4|r"})
    add_u(5166, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дает |cffffffff15%|cffced4da шанс нанести четырехкратный урон при атаке.|r", {"type": "ability", "id": "AOcr", "field": "ubertip4", "expected": None})
    
    # AOwk: Танец ветра (N073, hotkey Q, level 4)
    add_u(23502, "|cffe4cfa3Танец ветра — уровень 4|r (|cffffffffQ|r)", {"type": "ability", "id": "AOwk", "field": "tip4", "expected": "|cffe4cfa3Танец ветра — уровень 4|r (|cffffffffQ|r)"})
    add_u(20908, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Дарует невидимость и ускорение на |cffffffff30|cffced4da сек. Атака из невидимости наносит |cffc8e087110|cffced4da ед. дополнительного урона.|r", {"type": "ability", "id": "AOwk", "field": "ubertip4", "expected": None})
    
    # AOww: Вихрь клинков (N073 Ultimate, hotkey R, level 2)
    add_u(9617, "|cffe4cfa3Вихрь клинков — уровень 2|r (|cffffffffR|r)", {"type": "ability", "id": "AOww", "field": "tip2", "expected": "|cffe4cfa3Вихрь клинков — уровень 2|r (|cffffffffR|r)"})
    add_u(23512, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Окружает мастера клинка вихрем стали, даруя невосприимчивость к магии и нанося |cffc8e087160|cffced4da ед. урона в секунду всем врагам вокруг.|r", {"type": "ability", "id": "AOww", "field": "ubertip2", "expected": None})
    
    # Aabr: Чумная аура (passive)
    add_u(7613, "|cffa6afb8СПОСОБНОСТЬ:|cffced4da Ускоряет регенерацию здоровья находящихся рядом союзников.|r", {"type": "ability", "id": "Aabr", "field": "ubertip1", "expected": None})
    
    # =========================================================================
    # GENERATE 8 JSON FILES IN docs/ui_text/
    # =========================================================================
    raw_dump = json.loads((ROOT / "scripts/felork_raw_dump.json").read_text(encoding="utf-8"))

    # 1. felork_plan.json
    plan_data = {
        "race": "Fel Orcs",
        "race_name_ru": "Орда Скверны",
        "race_id": 31,
        "selection_ability": "A1JL",
        "faction_markers": ["R0KA", "R0KC"],
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def),
        "wts_updates": {str(k): v for k, v in wts_updates.items()},
        "checks_def": checks_def,
        "categories": {
            "buildings": [
                "o05V", "o05W", "o05X", "o060", "o05Y", "o05Z", "o05T", "o061", "o062", "o066", "o067", "h0D3", "owtw"
            ],
            "units": [
                "n06B", "n06F", "n068", "n06L", "n06T", "n06D", "n06M", "n06Q",
                "n06G", "n06J", "n06W", "o05Q", "o065", "o063", "o05R", "n067",
                "n06R", "n06N", "n06C", "n06S", "n06O", "n069", "n06U", "n06K",
                "n06A", "n06I", "n06V", "n070", "h0D4", "h0D6", "h0D5"
            ],
            "heroes": ["N06P", "N072", "N073"],
            "upgrades": [
                "R0KA", "R0KC", "R00Y", "R0JQ", "R0JR", "R0JS", "R0JU", "R0JV",
                "R0JW", "R0JX", "R0JY", "R0JZ", "R0K0", "R0K1", "R0K2", "R0K3",
                "R0K5", "R0K6", "R0K7", "Roen", "Ropg"
            ],
            "abilities": [
                "A1JL", "A01C", "A0B7", "A0BE", "A0EN", "A0I3", "A0IQ", "A0LI",
                "A0LJ", "A0N7", "A14L", "A1HW", "A1HX", "A1HY", "A1HZ", "A1I0",
                "A1I1", "A1I2", "A1I3", "A1II", "A1IM", "A1IN", "A1IO", "A1IP",
                "A1IQ", "A1IR", "A1IS", "A1IT", "A1IU", "A1IV", "A1IW", "A1IX",
                "A1IY", "A1IZ", "A1J1", "A1J3", "A1J4", "A1J5", "A1J7", "A1J8",
                "A1J9", "A1JG", "A1JH", "A1JI", "A1JK", "A1JP", "A1KB", "A1MC",
                "A1MD", "AOcr", "AOwk", "AOww", "Aabr"
            ],
            "buffs": []
        }
    }
    (folder / "felork_plan.json").write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote felork_plan.json")

    # 2. felork_selection.json
    sel_data = {
        "scope": "Орда Скверны (Fel Orcs): подсказка выбора расы A1JL и маркеры фракции R0KA, R0KC",
        "object": "A1JL",
        "variants": ["SD"],
        "hotkey": {"value": "C"},
        "levels": 1,
        "evidence": [
            "04_race_selection.lua: InitTrig_Race_Fel_Orcs регистрирует способность A1JL.",
            "При выборе создаются 5 рабочих n06B, исследуются маркеры R0KA и R0KC, удаляется выбирающий юнит.",
            "Горячая клавиша C, создатель Escanor(Яхве), куратор NiCAmCHiK, сложность 3/5 (●●●○○), период «Warcraft III — Battle for Azeroth»."
        ],
        "strings": [
            {"field": "name", "wts_id": 38915, "after": wts_updates[38915]},
            {"field": "tip1", "wts_id": 38916, "after": wts_updates[38916]},
            {"field": "ubertip1", "wts_id": 25691, "after": wts_updates[25691]}
        ],
        "markers": [
            {
                "id": "R0KA",
                "name": "Орда Скверны (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 37022, "after": wts_updates[37022]},
                    {"field": "tip1", "wts_id": 37023, "after": wts_updates[37023]},
                    {"field": "ubertip1", "wts_id": 26689, "after": wts_updates[26689]}
                ]
            },
            {
                "id": "R0KC",
                "name": "Орда Скверны или Орда Второй Войны (маркер расы)",
                "strings": [
                    {"field": "name1", "wts_id": 5595, "after": wts_updates[5595]},
                    {"field": "tip1", "wts_id": 5596, "after": wts_updates[5596]},
                    {"field": "ubertip1", "wts_id": 27305, "after": wts_updates[27305]}
                ]
            }
        ]
    }
    (folder / "felork_selection.json").write_text(json.dumps(sel_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote felork_selection.json")

    # 3. felork_buildings.json
    bld_entries = []
    for b_id in plan_data["categories"]["buildings"]:
        raw_b = next((x for x in raw_dump["buildings"] if x["id"] == b_id), {})
        hk = raw_b.get("hotkey")
        strings_list = []
        if b_id in BY_CAT.get("buildings", {}):
            for f, sid in sorted(BY_CAT["buildings"][b_id], key=lambda x: x[0]):
                if sid in wts_updates:
                    strings_list.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        bld_entries.append({"id": b_id, "hotkey": hk, "strings": strings_list})

    bld_data = {
        "scope": f"Орда Скверны (Fel Orcs): категория 1 — Здания ({len(bld_entries)} зданий)",
        "buildings_count": len(bld_entries),
        "variants": ["SD"],
        "buildings": bld_entries
    }
    (folder / "felork_buildings.json").write_text(json.dumps(bld_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote felork_buildings.json ({len(bld_entries)} buildings)")

    # 4. felork_units.json
    unit_entries = []
    for u_id in plan_data["categories"]["units"]:
        raw_u = next((x for x in raw_dump["units"] if x["id"] == u_id), {})
        hk = raw_u.get("hotkey")
        strings_list = []
        if u_id in BY_CAT.get("units", {}):
            for f, sid in sorted(BY_CAT["units"][u_id], key=lambda x: x[0]):
                if sid in wts_updates:
                    strings_list.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        unit_entries.append({"id": u_id, "hotkey": hk, "strings": strings_list})

    unit_data = {
        "scope": f"Орда Скверны (Fel Orcs): категория 2 — Юниты ({len(unit_entries)} юнитов)",
        "units_count": len(unit_entries),
        "variants": ["SD"],
        "units": unit_entries
    }
    (folder / "felork_units.json").write_text(json.dumps(unit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote felork_units.json ({len(unit_entries)} units)")

    # 5. felork_heroes.json
    hero_entries = []
    for h_id in plan_data["categories"]["heroes"]:
        raw_h = next((x for x in raw_dump["heroes"] if x["id"] == h_id), {})
        hk = raw_h.get("hotkey")
        strings_list = []
        if h_id in BY_CAT.get("heroes", {}):
            for f, sid in sorted(BY_CAT["heroes"][h_id], key=lambda x: x[0]):
                if sid in wts_updates:
                    strings_list.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        hero_entries.append({"id": h_id, "hotkey": hk, "strings": strings_list})

    hero_data = {
        "scope": f"Орда Скверны (Fel Orcs): категория 3 — Герои ({len(hero_entries)} героев)",
        "heroes_count": len(hero_entries),
        "variants": ["SD"],
        "heroes": hero_entries
    }
    (folder / "felork_heroes.json").write_text(json.dumps(hero_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote felork_heroes.json ({len(hero_entries)} heroes)")

    # 6. felork_abilities.json
    abil_entries = []
    for a_id in plan_data["categories"]["abilities"]:
        raw_a = next((x for x in raw_dump["abilities"] if x["id"] == a_id), {})
        lvls = raw_a.get("levels", 1)
        strings_list = []
        if a_id in BY_CAT.get("abilities", {}):
            for f, sid in sorted(BY_CAT["abilities"][a_id], key=lambda x: x[0]):
                if sid in wts_updates:
                    strings_list.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        abil_entries.append({"id": a_id, "levels": lvls, "strings": strings_list})

    abil_data = {
        "scope": f"Орда Скверны (Fel Orcs): категория 4 — Способности ({len(abil_entries)} способностей)",
        "abilities_count": len(abil_entries),
        "variants": ["SD"],
        "abilities": abil_entries
    }
    (folder / "felork_abilities.json").write_text(json.dumps(abil_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote felork_abilities.json ({len(abil_entries)} abilities)")

    # 7. felork_research.json
    upg_entries = []
    for u_id in plan_data["categories"]["upgrades"]:
        raw_u = next((x for x in raw_dump["upgrades"] if x["id"] == u_id), {})
        lvls = raw_u.get("levels", 1)
        strings_list = []
        if u_id in BY_CAT.get("upgrades", {}):
            for f, sid in sorted(BY_CAT["upgrades"][u_id], key=lambda x: x[0]):
                if sid in wts_updates:
                    strings_list.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        elif u_id in BY_CAT.get("markers", {}):
            for f, sid in sorted(BY_CAT["markers"][u_id], key=lambda x: x[0]):
                if sid in wts_updates:
                    strings_list.append({"field": f, "wts_id": sid, "after": wts_updates[sid]})
        upg_entries.append({"id": u_id, "levels": lvls, "strings": strings_list})

    upg_data = {
        "scope": f"Орда Скверны (Fel Orcs): категория 5 — Исследования и маркеры ({len(upg_entries)} технологий)",
        "upgrades_count": len(upg_entries),
        "variants": ["SD"],
        "upgrades": upg_entries
    }
    (folder / "felork_research.json").write_text(json.dumps(upg_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote felork_research.json ({len(upg_entries)} upgrades)")

    # 8. felork_audit.json
    audit_data = {
        "race": "Орда Скверны (Fel Orcs)",
        "race_id": 31,
        "selection_ability": "A1JL",
        "objects_audit": {
            "buildings": {
                "count": len(bld_entries),
                "ids": [b["id"] for b in bld_entries],
                "town_halls": {
                    "tier1": {"id": "o05V", "name": "Дом вождей", "food": 50},
                    "tier2": {"id": "o05W", "name": "Крепость", "food": 100},
                    "tier3": {"id": "o05X", "name": "Цитадель", "food": 150}
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
                    "N06P": "Оскверненный шаман (Интеллект, дальний бой)",
                    "N072": "Военный лорд (Сила, ближний бой)",
                    "N073": "Мастер меча (Ловкость, ближний бой)"
                }
            },
            "abilities": {
                "count": len(abil_entries),
                "total_wts_updated": len(wts_updates)
            },
            "researches": {
                "count": len(upg_entries),
                "markers_list": {
                    "R0KA": "Маркер расы Орда Скверны",
                    "R0KC": "Маркер расы Орда Скверны или Орда Второй Войны"
                }
            }
        },
        "items_audit": {
            "race_specific_items": [],
            "status": "No race-specific shop items found in war3map.w3t for Fel Orcs."
        },
        "messages_audit": {
            "race_specific_messages": [],
            "status": "No race-specific triggers/chat messages found for Fel Orcs."
        },
        "buffs_audit": {
            "custom_buffs": [],
            "standard_buffs_used": ["Bblo", "Bbsk", "Bfro"],
            "status": "Standardized buffs used."
        },
        "total_wts_updates": len(wts_updates),
        "total_checks": len(checks_def)
    }
    (folder / "felork_audit.json").write_text(json.dumps(audit_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote felork_audit.json")

if __name__ == "__main__":
    main()
