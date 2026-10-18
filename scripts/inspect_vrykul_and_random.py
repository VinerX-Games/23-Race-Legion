# -*- coding: utf-8 -*-
"""Inspect objects for Race 36: Vryculs and Race 37: Random and dump raw data to JSON files."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import inspect_race_base as base
import wc3_hivewe as hw
from inspect_5_races import crawl_race

def main():
    print("Crawling Vryculs...")
    vrykul_blds = ['h0BQ', 'h0BR', 'h0BS', 'h0BT', 'h0BU', 'h0BV', 'h0BW', 'h0BX', 'wk01']
    vrykul_heroes = ['H0C4', 'H0C5', 'H0C6', 'H0C7']
    vrykul_units = ['h0C9', 'h0AA', 'h0AD', 'h0A5', 'h0A6', 'h0BP', 'h0A9', 'h0AC', 'h0AE', 'wk08', 'wk02', 'wk00', 'h0A8', 'h0A7']
    vrykul_markers = ['R07F', 'R067', 'R068']
    
    vrykul_data = crawl_race(
        "Vryculs", "A0HP", vrykul_markers,
        vrykul_blds, explicit_unit_ids=vrykul_units, explicit_hero_ids=vrykul_heroes
    )
    with open(ROOT / "scripts/vrykul_raw_dump.json", "w", encoding="utf-8") as f:
        json.dump(vrykul_data, f, ensure_ascii=False, indent=2)

    print("\nCrawling Random...")
    random_data = {
        'race': 'Random',
        'selection': base.inspect_ability('A12Q'),
        'selection_markers': [],
        'buildings': [],
        'units': [],
        'heroes': [],
        'upgrades': [],
        'abilities': [base.inspect_ability('A12Q')],
        'buffs': []
    }
    with open(ROOT / "scripts/random_raw_dump.json", "w", encoding="utf-8") as f:
        json.dump(random_data, f, ensure_ascii=False, indent=2)
        
    print("\nDone crawling Vryculs and Random!")

if __name__ == '__main__':
    main()
