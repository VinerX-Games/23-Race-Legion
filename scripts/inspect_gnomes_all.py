# -*- coding: utf-8 -*-
"""Inspect all Gnomes (Race 23) objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff, resolve

def main():
    print("=== INSPECTING GNOMES (RACE 23) OBJECTS ===")

    # 1. Selection & Markers
    selection_ability = inspect_ability('A0SD')
    marker_ids = ['R0BX', 'R0HW']
    selection_markers = [inspect_upgrade(m) for m in marker_ids]

    # 2. Buildings (10)
    bld_ids = ['h0FI', 'h0FK', 'h0FL', 'h0FR', 'h0FS', 'h0FY', 'h0FZ', 'h0G0', 'h0G3', 'h0G7']
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Workers (2)
    worker_ids = ['h0FA', 'h0FX']
    worker_data = [inspect_unit(w) for w in worker_ids]

    # 4. Units (21)
    unit_ids = [
        'h0FB', 'h0FC', 'h0FD', 'h0FE', 'h0FF', 'h0FG', 'h0FH', 'h0FJ', 'h0FM', 'h0FN',
        'h0FO', 'h0FP', 'h0FQ', 'h0FT', 'h0FU', 'h0FV', 'h0FW', 'h0G1', 'h0G2', 'h0G4', 'h0G5'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 5. Heroes (8)
    hero_ids = ['H0GC', 'H0GD', 'H0GE', 'H0GF', 'H0GG', 'H0HQ', 'H0HS', 'MIMH']
    hero_data = [inspect_unit(h) for h in hero_ids]

    # Collect all upgrades and abilities referenced by buildings, units, heroes
    all_units = worker_data + unit_data + hero_data + bld_data
    
    referenced_upgrades = set(marker_ids)
    referenced_abilities = {selection_ability['id']}

    for b in bld_data:
        res = b.get('researches')
        if res:
            for item in res.split(','):
                item = item.strip()
                if item:
                    referenced_upgrades.add(item)
        abl = b.get('abillist')
        if abl:
            for item in abl.split(','):
                item = item.strip()
                if item:
                    referenced_abilities.add(item)

    for u in worker_data + unit_data:
        abl = u.get('abillist')
        if abl:
            for item in abl.split(','):
                item = item.strip()
                if item:
                    referenced_abilities.add(item)
        upg = u.get('upgrades')
        if upg:
            for item in upg.split(','):
                item = item.strip()
                if item:
                    referenced_upgrades.add(item)

    for h in hero_data:
        abl = h.get('abillist')
        if abl:
            for item in abl.split(','):
                item = item.strip()
                if item:
                    referenced_abilities.add(item)
        habl = h.get('heroabillist')
        if habl:
            for item in habl.split(','):
                item = item.strip()
                if item:
                    referenced_abilities.add(item)
        upg = h.get('upgrades')
        if upg:
            for item in upg.split(','):
                item = item.strip()
                if item:
                    referenced_upgrades.add(item)

    # Let's inspect upgrades
    upgrade_data = []
    for uid in sorted(referenced_upgrades):
        try:
            upg = inspect_upgrade(uid)
            upgrade_data.append(upg)
        except Exception as e:
            print(f"Warning: could not inspect upgrade {uid}: {e}")

    # Inspect abilities
    ability_data = []
    for aid in sorted(referenced_abilities):
        try:
            ab = inspect_ability(aid)
            ability_data.append(ab)
        except Exception as e:
            print(f"Warning: could not inspect ability {aid}: {e}")

    # Also check referenced buffs from abilities
    referenced_buffs = set()
    for ab in ability_data:
        f = ab.get('fields', {})
        ov = ab.get('overrides', {})
        for k, v in {**f, **ov}.items():
            if 'buff' in k.lower() and isinstance(v, str):
                for b_item in v.split(','):
                    b_item = b_item.strip()
                    if len(b_item) == 4:
                        referenced_buffs.add(b_item)

    buff_data = []
    for bid in sorted(referenced_buffs):
        try:
            buf = inspect_buff(bid)
            buff_data.append(buf)
        except Exception as e:
            pass

    out_file = ROOT / "scripts/gnomes_raw_dump.json"
    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'workers': worker_data,
        'units': unit_data,
        'heroes': hero_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data,
        'referenced_upgrades': sorted(list(referenced_upgrades)),
        'referenced_abilities': sorted(list(referenced_abilities)),
        'referenced_buffs': sorted(list(referenced_buffs))
    }
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary for Gnomes:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Workers: {len(worker_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
