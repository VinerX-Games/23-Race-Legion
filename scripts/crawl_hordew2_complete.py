# -*- coding: utf-8 -*-
"""Complete, thorough object crawler for Race 35: Horde of the Second War (HordeW2)."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import inspect_race_base as base
import wc3_hivewe as hw

def main():
    race_name = "HordeW2"
    selection_aid = "A1JN"
    marker_ids = ["R0KB", "R0KC", "R0KD"]
    
    # All known starting buildings for HordeW2
    starter_blds = ['w20q', 'w20w', 'w20e', 'w20r', 'w20y', 'w214', 'w20a', 'w20u', 'w20t', 'w20i', 'w210', 'w218', 'w219']
    starter_heroes = ['W200', 'W201', 'W202', 'W203']
    starter_units = ['w200']

    sel_abil = base.inspect_ability(selection_aid) if selection_aid else None
    markers = [base.inspect_upgrade(m) for m in marker_ids]

    bld_visited = set()
    bld_queue = list(starter_blds)
    all_bld_data = []

    unit_visited = set()
    unit_queue = list(starter_units)
    all_unit_data = []

    hero_visited = set()
    hero_queue = list(starter_heroes)
    all_hero_data = []

    upgrade_ids = set(marker_ids)
    ability_ids = set([selection_aid])

    while bld_queue:
        bid = bld_queue.pop(0)
        if bid in bld_visited:
            continue
        bld_visited.add(bid)
        try:
            b_info = base.inspect_unit(bid)
            all_bld_data.append(b_info)
        except Exception as e:
            print(f"Error inspecting building {bid}: {e}")
            continue

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
                # Check if hero
                if u in starter_heroes:
                    if u not in hero_visited:
                        hero_queue.append(u)
                else:
                    try:
                        u_raw = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', u, '--all'])
                        f = u_raw.get('fields', {}) or u_raw.get('object', {})
                        ov = u_raw.get('overrides', {})
                        get_v = lambda k: ov.get(k) if ov.get(k) is not None else f.get(k)
                        if get_v('heroabillist') or get_v('propernames') or (get_v('atktype1') == 'hero'):
                            if u not in hero_visited and u not in hero_queue:
                                hero_queue.append(u)
                        else:
                            if u not in unit_visited and u not in unit_queue:
                                unit_queue.append(u)
                    except Exception:
                        if u not in unit_visited and u not in unit_queue:
                            unit_queue.append(u)

        # Check researches
        res = b_info.get('researches')
        if res:
            for r in res.split(','):
                r = r.strip()
                if r:
                    upgrade_ids.add(r)

        # Building abilities
        ab = b_info.get('abillist')
        if ab:
            for a in ab.split(','):
                a = a.strip()
                if a:
                    ability_ids.add(a)

    # Process units
    while unit_queue:
        uid = unit_queue.pop(0)
        if uid in unit_visited:
            continue
        unit_visited.add(uid)
        try:
            u_info = base.inspect_unit(uid)
            all_unit_data.append(u_info)
        except Exception as e:
            print(f"Error inspecting unit {uid}: {e}")
            continue

        blds = u_info.get('builds')
        if blds:
            for b in blds.split(','):
                b = b.strip()
                if b and b not in bld_visited:
                    bld_queue.append(b)

        ab = u_info.get('abillist')
        if ab:
            for a in ab.split(','):
                a = a.strip()
                if a:
                    ability_ids.add(a)

        up = u_info.get('upgrades')
        if up:
            for r in up.split(','):
                r = r.strip()
                if r:
                    upgrade_ids.add(r)

    # Process heroes
    while hero_queue:
        hid = hero_queue.pop(0)
        if hid in hero_visited:
            continue
        hero_visited.add(hid)
        try:
            h_info = base.inspect_unit(hid)
            all_hero_data.append(h_info)
        except Exception as e:
            print(f"Error inspecting hero {hid}: {e}")
            continue

        hab = h_info.get('heroabillist')
        if hab:
            for a in hab.split(','):
                a = a.strip()
                if a:
                    ability_ids.add(a)

        ab = h_info.get('abillist')
        if ab:
            for a in ab.split(','):
                a = a.strip()
                if a:
                    ability_ids.add(a)

    # Process upgrades
    all_upgrade_data = []
    for r in sorted(upgrade_ids):
        try:
            up_info = base.inspect_upgrade(r)
            all_upgrade_data.append(up_info)
        except Exception as e:
            print(f"Error inspecting upgrade {r}: {e}")

    # Process abilities
    all_ability_data = []
    buff_ids = set()
    for a in sorted(ability_ids):
        try:
            ab_info = base.inspect_ability(a)
            all_ability_data.append(ab_info)
            # check buffs if any
            for b_field in ['buff1', 'buff2', 'buff3', 'buff4', 'buffid']:
                bid = ab_info.get(b_field)
                if bid and bid != '-' and len(bid) == 4:
                    buff_ids.add(bid)
        except Exception as e:
            print(f"Error inspecting ability {a}: {e}")

    all_buff_data = []
    for b in sorted(buff_ids):
        try:
            b_info = base.inspect_buff(b)
            all_buff_data.append(b_info)
        except Exception as e:
            print(f"Error inspecting buff {b}: {e}")

    result = {
        "race": race_name,
        "selection": sel_abil,
        "selection_markers": markers,
        "buildings": all_bld_data,
        "units": all_unit_data,
        "heroes": all_hero_data,
        "upgrades": all_upgrade_data,
        "abilities": all_ability_data,
        "buffs": all_buff_data
    }

    out_file = ROOT / "scripts/hordew2_raw_dump.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\nDump complete! Written to {out_file}:")
    print(f"  Buildings: {len(all_bld_data)}")
    print(f"  Heroes: {len(all_hero_data)}")
    print(f"  Units: {len(all_unit_data)}")
    print(f"  Upgrades: {len(all_upgrade_data)}")
    print(f"  Abilities: {len(all_ability_data)}")
    print(f"  Buffs: {len(all_buff_data)}")

if __name__ == '__main__':
    main()
