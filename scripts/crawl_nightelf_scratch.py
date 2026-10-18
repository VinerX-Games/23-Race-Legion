# -*- coding: utf-8 -*-
"""Crawl and inspect all Night Elf race elements."""
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import inspect_race_base as ib

def crawl():
    print("=== CRAWLING NIGHT ELF RACE ===")
    
    # 1. Selection
    sel_abil = ib.inspect_ability('A0HL')
    sel_marker = ib.inspect_upgrade('R07L')
    print(f"Selection: {sel_abil['name']} ({sel_abil['id']}), Marker: {sel_marker['names'].get('name1', {}).get('val')} ({sel_marker['id']})")

    # 2. Worker
    worker = ib.inspect_unit('ewsp')
    print(f"Worker: {worker['name']} ({worker['id']}), builds: {worker['builds']}")
    
    # Buildings to crawl
    bld_ids = set()
    if worker['builds']:
        for b in worker['builds'].split(','):
            bld_ids.add(b.strip())
            
    # Add any known additional buildings
    known_blds = ['h0D8', 'etol', 'emow', 'eaom', 'eate', 'eaow', 'eaoe', 'edob', 'etrp', 'edos', 'e03X', 'e03W', 'etoa', 'etoe']
    for b in known_blds:
        bld_ids.add(b)

    # Crawl building upgrades
    queue = list(bld_ids)
    blds = {}
    while queue:
        bid = queue.pop(0)
        data = ib.inspect_unit(bid)
        blds[bid] = data
        upg = data.get('upgrades_to')
        if upg:
            for u in upg.split(','):
                u = u.strip()
                if u and u not in blds and u not in queue:
                    queue.append(u)
                    bld_ids.add(u)

    print(f"\nFound {len(blds)} buildings:")
    units_to_crawl = set()
    heroes_to_crawl = set()
    upgrades_to_crawl = set()
    bld_abilities = set()

    for bid, b in sorted(blds.items()):
        print(f"  [{bid}] {b['name']} (hotkey: {b.get('hotkey')})")
        print(f"       trains: {b.get('train')}")
        print(f"       researches: {b.get('researches')}")
        print(f"       upgrades_to: {b.get('upgrades_to')}")
        print(f"       abillist: {b.get('abillist')}")
        
        if b.get('train'):
            for u in b['train'].split(','):
                u = u.strip()
                if u:
                    if bid == 'eaom': # Altar trains heroes
                        heroes_to_crawl.add(u)
                    else:
                        units_to_crawl.add(u)
        if b.get('researches'):
            for r in b['researches'].split(','):
                r = r.strip()
                if r:
                    upgrades_to_crawl.add(r)
        if b.get('abillist'):
            for a in b['abillist'].split(','):
                a = a.strip()
                if a:
                    bld_abilities.add(a)

    # Add known units from prompt
    prompt_units = ['earc', 'esen', 'ebal', 'edry', 'edot', 'edoc', 'emtg', 'ehip', 'echm', 'e00J', 'n064', 'n05D', 'n05H', 'ehap', 'n05G']
    for u in prompt_units:
        units_to_crawl.add(u)
        
    # Add known heroes from prompt
    prompt_heroes = ['Ewar', 'Edem', 'Ekee', 'Emoo', 'E00V', 'E011', 'E00W']
    for h in prompt_heroes:
        heroes_to_crawl.add(h)

    # Also worker upgrades
    if worker.get('upgrades'):
        for u in worker['upgrades'].split(','):
            u = u.strip()
            if u:
                upgrades_to_crawl.add(u)
    if worker.get('abillist'):
        for a in worker['abillist'].split(','):
            a = a.strip()
            if a:
                bld_abilities.add(a)

    print(f"\nCrawling {len(units_to_crawl)} units...")
    units = {}
    unit_abilities = set()
    for uid in sorted(units_to_crawl):
        udata = ib.inspect_unit(uid)
        units[uid] = udata
        print(f"  [{uid}] {udata['name']} (tip: {udata.get('tip')})")
        print(f"       abillist: {udata.get('abillist')}")
        print(f"       upgrades: {udata.get('upgrades')}")
        if udata.get('abillist'):
            for a in udata['abillist'].split(','):
                a = a.strip()
                if a:
                    unit_abilities.add(a)
        if udata.get('upgrades'):
            for up in udata['upgrades'].split(','):
                up = up.strip()
                if up:
                    upgrades_to_crawl.add(up)

    print(f"\nCrawling {len(heroes_to_crawl)} heroes...")
    heroes = {}
    hero_abilities = set()
    for hid in sorted(heroes_to_crawl):
        hdata = ib.inspect_unit(hid)
        heroes[hid] = hdata
        print(f"  [{hid}] {hdata['name']} (propernames: {hdata.get('propernames')})")
        print(f"       heroabillist: {hdata.get('heroabillist')}")
        print(f"       abillist: {hdata.get('abillist')}")
        if hdata.get('heroabillist'):
            for a in hdata['heroabillist'].split(','):
                a = a.strip()
                if a:
                    hero_abilities.add(a)
        if hdata.get('abillist'):
            for a in hdata['abillist'].split(','):
                a = a.strip()
                if a:
                    hero_abilities.add(a)

    print(f"\nUpgrades found: {len(upgrades_to_crawl)}")
    print(sorted(list(upgrades_to_crawl)))

    print(f"\nHero abilities found: {len(hero_abilities)}")
    print(sorted(list(hero_abilities)))

    print(f"\nUnit abilities found: {len(unit_abilities)}")
    print(sorted(list(unit_abilities)))

    print(f"\nBuilding abilities found: {len(bld_abilities)}")
    print(sorted(list(bld_abilities)))

if __name__ == '__main__':
    crawl()
