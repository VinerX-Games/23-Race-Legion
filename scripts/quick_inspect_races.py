# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path("scripts").resolve()))
import wc3_hivewe as hw

races_to_test = [
    'Даларан', 'даларан',
    'Кул-Тирас', 'Кул тирас',
    'Ночнорожденные', 'Ночнорождённые', 'ночнорожденные', 'ночнорождённые',
    'Дренеи', 'дренеи',
    'Сумеречный Молот', 'сумеречный Молот'
]

for r in races_to_test:
    res = hw.run_cli_json(['inspect-race', '--map', str(hw.DEFAULT_MAP), '--race', r])
    if res.get('success'):
        b = len(res.get("buildings", []))
        u = len(res.get("units", []))
        h = len(res.get("heroes", []))
        print(f"Race: {r} -> buildings: {b}, units: {u}, heroes: {h}")
