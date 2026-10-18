# -*- coding: utf-8 -*-
"""Inspect objects for Races 31, 32, 33, 34, 35 and dump raw data to JSON files."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import inspect_race_base as base
import wc3_hivewe as hw

def crawl_race(race_name, selection_aid, marker_ids, starter_bld_ids, explicit_unit_ids=None, explicit_hero_ids=None):
    print(f"\n=======================================================")
    print(f"Crawling Race: {race_name}")
    print(f"=======================================================")
    
    # 1. Selection & markers
    sel_abil = base.inspect_ability(selection_aid) if selection_aid else None
    markers = [base.inspect_upgrade(m) for m in marker_ids]
    
    # 2. Buildings
    bld_visited = set()
    bld_queue = list(starter_bld_ids)
    all_bld_data = []
    
    unit_ids_discovered = set(explicit_unit_ids or [])
    hero_ids_discovered = set(explicit_hero_ids or [])
    upgrade_ids_discovered = set(marker_ids)
    ability_ids_discovered = set([selection_aid] if selection_aid else [])
    
    while bld_queue:
        bid = bld_queue.pop(0)
        if bid in bld_visited:
            continue
        bld_visited.add(bid)
        try:
            b_info = base.inspect_unit(bid)
        except Exception as e:
            print(f"Error inspecting building {bid}: {e}")
            continue
        all_bld_data.append(b_info)
        
        # Check upgrades_to
        upg_to = b_info.get('upgrades_to')
        if upg_to:
            for nxt in upg_to.split(','):
                nxt = nxt.strip()
                if nxt and nxt not in bld_visited:
                    bld_queue.append(nxt)
                    
        # Check trains
        tr = b_info.get('train')
        if tr:
            for u in tr.split(','):
                u = u.strip()
                if not u:
                    continue
                # Determine if hero or unit
                if u[0].isupper() and u[0] not in ('H', 'O', 'E', 'U') and not u.startswith('pa') and not u.startswith('cD'):
                    hero_ids_discovered.add(u)
                else:
                    # Let's inspect briefly to check hero status
                    try:
                        u_raw = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', u, '--all'])
                        f = u_raw.get('fields', {}) or u_raw.get('object', {})
                        overrides = u_raw.get('overrides', {})
                        get_v = lambda k: overrides.get(k) if overrides.get(k) is not None else f.get(k)
                        if get_v('heroabillist') or get_v('propernames'):
                            hero_ids_discovered.add(u)
                        else:
                            unit_ids_discovered.add(u)
                    except Exception:
                        unit_ids_discovered.add(u)
                        
        # Check researches
        res = b_info.get('researches')
        if res:
            for r in res.split(','):
                r = r.strip()
                if r:
                    upgrade_ids_discovered.add(r)
                    
        # Check building abilities
        ab = b_info.get('abillist')
        if ab:
            for a in ab.split(','):
                a = a.strip()
                if a:
                    ability_ids_discovered.add(a)
                    
    # Also inspect builder units to find what they build!
    unit_visited = set()
    all_unit_data = []
    unit_queue = list(unit_ids_discovered)
    
    while unit_queue:
        uid = unit_queue.pop(0)
        if uid in unit_visited:
            continue
        unit_visited.add(uid)
        try:
            u_info = base.inspect_unit(uid)
        except Exception as e:
            print(f"Error inspecting unit {uid}: {e}")
            continue
        all_unit_data.append(u_info)
        
        # Check if builder
        blds = u_info.get('builds')
        if blds:
            for b in blds.split(','):
                b = b.strip()
                if b and b not in bld_visited:
                    bld_queue.append(b)
                    
        # Abilities
        ab = u_info.get('abillist')
        if ab:
            for a in ab.split(','):
                a = a.strip()
                if a:
                    ability_ids_discovered.add(a)
                    
        # Upgrades
        up = u_info.get('upgrades')
        if up:
            for r in up.split(','):
                r = r.strip()
                if r:
                    upgrade_ids_discovered.add(r)
                    
    # Inspect any newly discovered buildings
    while bld_queue:
        bid = bld_queue.pop(0)
        if bid in bld_visited:
            continue
        bld_visited.add(bid)
        try:
            b_info = base.inspect_unit(bid)
            all_bld_data.append(b_info)
            tr = b_info.get('train')
            if tr:
                for u in tr.split(','):
                    u = u.strip()
                    if u and u not in unit_visited and u not in hero_ids_discovered:
                        unit_queue.append(u)
        except Exception as e:
            print(f"Error inspecting building {bid}: {e}")
            
    # Re-run unit_queue if newly added
    while unit_queue:
        uid = unit_queue.pop(0)
        if uid in unit_visited:
            continue
        unit_visited.add(uid)
        try:
            u_info = base.inspect_unit(uid)
            all_unit_data.append(u_info)
        except Exception as e:
            pass

    # Inspect Heroes
    all_hero_data = []
    for hid in sorted(hero_ids_discovered):
        try:
            h_info = base.inspect_unit(hid)
            all_hero_data.append(h_info)
            hab = h_info.get('heroabillist')
            if hab:
                for a in hab.split(','):
                    a = a.strip()
                    if a:
                        ability_ids_discovered.add(a)
            ab = h_info.get('abillist')
            if ab:
                for a in ab.split(','):
                    a = a.strip()
                    if a:
                        ability_ids_discovered.add(a)
        except Exception as e:
            print(f"Error inspecting hero {hid}: {e}")
            
    # Inspect Upgrades
    all_upgrade_data = []
    for rid in sorted(upgrade_ids_discovered):
        try:
            r_info = base.inspect_upgrade(rid)
            all_upgrade_data.append(r_info)
        except Exception as e:
            # Maybe it's an ability mistakenly put in researches
            ability_ids_discovered.add(rid)
            
    # Inspect Abilities
    all_ability_data = []
    buff_ids_discovered = set()
    for aid in sorted(ability_ids_discovered):
        try:
            a_info = base.inspect_ability(aid)
            all_ability_data.append(a_info)
            # Check for buffs
            bf = a_info.get('buffs')
            if bf:
                for b in bf.split(','):
                    b = b.strip()
                    if b:
                        buff_ids_discovered.add(b)
        except Exception as e:
            pass
            
    all_buff_data = []
    for bid in sorted(buff_ids_discovered):
        try:
            b_info = base.inspect_buff(bid)
            all_buff_data.append(b_info)
        except Exception as e:
            pass
            
    dump_data = {
        'race': race_name,
        'selection': sel_abil,
        'selection_markers': markers,
        'buildings': all_bld_data,
        'units': all_unit_data,
        'heroes': all_hero_data,
        'upgrades': all_upgrade_data,
        'abilities': all_ability_data,
        'buffs': all_buff_data
    }
    
    print(f"Summary for {race_name}:")
    print(f"  Buildings: {len(all_bld_data)}: {[b['id'] for b in all_bld_data]}")
    print(f"  Units:     {len(all_unit_data)}: {[u['id'] for u in all_unit_data]}")
    print(f"  Heroes:    {len(all_hero_data)}: {[h['id'] for h in all_hero_data]}")
    print(f"  Upgrades:  {len(all_upgrade_data)}: {[u['id'] for u in all_upgrade_data]}")
    print(f"  Abilities: {len(all_ability_data)}")
    print(f"  Buffs:     {len(all_buff_data)}")
    
    return dump_data

def main():
    # 31. FelOrk (Орда погані)
    felork_blds = ['o05V', 'o05T', 'o05Y', 'o05Z', 'o060', 'o061', 'o062', 'o066', 'o067']
    felork_heroes = ['N072', 'N073', 'N06P']
    felork_data = crawl_race(
        "FelOrk", "A1JL", ["R0KA", "R0KC", "R0JS", "R0JQ", "R0JR", "R0K1"],
        felork_blds, explicit_hero_ids=felork_heroes
    )
    with open(ROOT / "scripts/felork_raw_dump.json", "w", encoding="utf-8") as f:
        json.dump(felork_data, f, ensure_ascii=False, indent=2)

    # 32. ForestTrolls (Лесные)
    ft_blds = ['h0MT', 'h0MR', 'h0MS', 'h0MU', 'h0MV', 'h0MZ', 'h0N4', 'h0N7']
    ft_heroes = ['O057', 'O058', 'O059']
    ft_data = crawl_race(
        "ForestTrolls", "A1FN", ["R0J1"],
        ft_blds, explicit_hero_ids=ft_heroes
    )
    with open(ROOT / "scripts/foresttrolls_raw_dump.json", "w", encoding="utf-8") as f:
        json.dump(ft_data, f, ensure_ascii=False, indent=2)

    # 33. CultOfDamned (КП)
    cult_blds = ['cD26', 'cD12', 'cD29', 'cD31', 'cD30', 'cD28', 'cD27']
    cult_heroes = ['U02S', 'U02T', 'U02U'] # Let's see altar trains in cD
    cult_data = crawl_race(
        "CultOfDamned", "A1HA", ["R0J4", "R0J5"],
        cult_blds, explicit_unit_ids=['cD02']
    )
    with open(ROOT / "scripts/cult_raw_dump.json", "w", encoding="utf-8") as f:
        json.dump(cult_data, f, ensure_ascii=False, indent=2)

    # 34. Pandarens (ПА)
    pa_blds = ['pa23', 'pa24', 'pa25', 'pa26', 'pa27', 'pa28', 'pa30', 'pa31', 'pa32', 'pa33', 'pa34', 'h0NZ', 'h0P5']
    pa_heroes = ['PA36', 'PA37', 'PA38', 'PA39', 'PA40']
    pa_data = crawl_race(
        "Pandarens", "A1I6", ["R0L3"],
        pa_blds, explicit_hero_ids=pa_heroes
    )
    with open(ROOT / "scripts/pandarens_raw_dump.json", "w", encoding="utf-8") as f:
        json.dump(pa_data, f, ensure_ascii=False, indent=2)

    # 35. HordeW2 (Ор2)
    hw2_blds = ['w214', 'w210', 'w218', 'w219'] # We'll discover what w200 builds
    hw2_heroes = ['W202', 'W203']
    hw2_data = crawl_race(
        "HordeW2", "A1JN", ["R0KB", "R0KC", "R0KD"],
        hw2_blds, explicit_unit_ids=['w200'], explicit_hero_ids=hw2_heroes
    )
    with open(ROOT / "scripts/hordew2_raw_dump.json", "w", encoding="utf-8") as f:
        json.dump(hw2_data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
