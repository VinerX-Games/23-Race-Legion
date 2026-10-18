# -*- coding: utf-8 -*-
"""Inspect all Night Elf race objects and dump raw data to JSON."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff, extract_wts_id, resolve, wts

def main():
    print("=== INSPECTING RACE 26: NIGHT ELF (НОЧНЫЕ ЭЛЬФЫ) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A0HL')
    selection_markers = [inspect_upgrade('R07L')]

    # 2. Worker
    worker_ids = ['ewsp']
    worker_data = [inspect_unit(w) for w in worker_ids]

    # 3. Buildings (14)
    bld_ids = [
        # Town Halls
        'etol', 'etoa', 'etoe',
        # Production & tech
        'emow', 'eaom', 'eate', 'eaow', 'eaoe', 'edob', 'etrp', 'edos',
        'e03X', 'e03W',
        # Naval
        'h0D8'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 4. Units
    unit_ids = [
        # Ancient of War
        'earc', 'esen', 'ebal', 'e00I', 'e00J', 'n05H',
        # Ancient of Wind
        'edot', 'edtm', 'efdr', 'e00H', 'n064',
        # Ancient of Lore
        'edry', 'edoc', 'edcm', 'emtg', 'n05D', 'n05G',
        # Chimaera Roost
        'echm', 'ehip',
        # Naval
        'h0D9', 'h0DB', 'h0DA',
        # Summons
        'efon', 'espv', 'eave', 'eowl'
    ]
    unit_data = []
    for uid in unit_ids:
        try:
            ud = inspect_unit(uid)
            if ud.get('name') or ud.get('fields'):
                unit_data.append(ud)
        except Exception as e:
            print(f"Warning: unit {uid} error: {e}")

    # 5. Heroes
    hero_ids = [
        'E00V', 'E011', 'E00W',
        'Ewar', 'Edem', 'Ekee', 'Emoo'
    ]
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 6. Upgrades
    # Collect all upgrades from buildings, units, triggers
    upgrade_ids = [
        # Selection marker
        'R07L',
        # Tier & Core path
        'Renb', 'R0G1', 'R0G2', 'R0GB',
        # Hunter's Hall researches
        'Resm', 'Rema', 'Resw', 'Rerh', 'Reuv', 'Rews', 'Resc', 'R0GC',
        # Ancient of War researches
        'Reib', 'Remk', 'Remg', 'Repb', 'R0LC', 'R0GA', 'R0G9', 'R0G7',
        # Ancient of Wind researches
        'Redt', 'Reec', 'R0G6',
        # Ancient of Lore researches
        'Redc', 'Reeb', 'Resi', 'Rers', 'Rehs', 'R0G8',
        # Chimaera Roost
        'Recb',
        # Shrines
        'R0KS', 'R0KT', 'R0KU', 'R0CY', 'R0KV', 'R0KW',
        # Naval
        'R002', 'R003', 'R004', 'R005', 'R006', 'R007'
    ]
    # Remove duplicates preserving order
    seen_upg = set()
    uniq_upg_ids = []
    for u in upgrade_ids:
        if u not in seen_upg:
            seen_upg.add(u)
            uniq_upg_ids.append(u)

    upgrade_data = []
    for uid in uniq_upg_ids:
        try:
            ud = inspect_upgrade(uid)
            upgrade_data.append(ud)
        except Exception as e:
            print(f"Warning: upgrade {uid} error: {e}")

    # 7. Abilities
    # Collect all abilities across buildings, units, heroes, triggers
    ability_ids = [
        # Selection
        'A0HL',
        # Worker
        'A0I3', 'Adtn', 'Aren', 'Awha', 'Ault',
        # Buildings
        'Abds', 'Aeat', 'Aro1', 'Aro2', 'Atol', 'Arlm', 'Ambt', 'A15N',
        'A0LJ', 'A0LI', 'A0IQ',
        # Ancient of War units
        'Aco2', 'Ashm', 'Aegr', 'Aeib', 'Aemk', # Archer
        'Aesn', 'Amgl', 'Amgi', # Huntress
        'Aimp', # Demolisher
        'A0FD', 'A0EF', # Lunar warrior
        'A0FC', # Forest spirit
        'A16K', # Furbolg tracker
        # Ancient of Wind units
        'Acyc', 'Arav', 'Afae', 'Afa2', # Druid of the Talon
        'A12K', 'A16L', 'Amfl', 'Apsh', # Faerie Dragon
        'A16I', 'A0FA', 'A0FB', # Ancient Guardian
        # Ancient of Lore units
        'Aadm', 'Aspo', 'Aien', # Dryad
        'Abrf', 'Arej', 'Aroa', 'Ara2', # Druid of the Claw
        'Atau', 'Agra', 'Arsk', 'Assk', # Mountain giant
        'A164', 'Absk', 'ACfb', 'Anhe', 'ACbh', # Druid owl
        # Chimaera Roost
        'Acor', 'Alit', 'Aco3',
        # Hero E00V (Keeper/Malfurion)
        'A0FJ', 'A0FH', 'A0FI', 'ken0', 'A1MW', 'A160', 'A161',
        # Hero E011 (Moon huntress)
        'A0FL', 'A0FQ', 'A0FS', 'A0FT',
        # Hero E00W (Druid master)
        'AEbl', 'ANfl', 'AEev', 'A0FM', 'A01C',
        # Standard heroes abilities
        'AEfk', 'AEsh', 'AEsv', 'AEav', 'Aven', # Warden
        'AEmb', 'AEim', 'AEme', # Demon Hunter
        'AEer', 'AEfn', 'AEah', 'AEtq', # Keeper of Grove
        'AHfa', 'AEst', 'AEar', 'AEsf', # Priestess of Moon
        # Naval
        'A001', 'A002', 'A003', 'A009', 'A00A', 'A00B', 'A00G', 'A00I', 'A1PP',
        'Sch5', 'Sdro', 'Slo3'
    ]
    seen_abils = set()
    uniq_abil_ids = []
    for a in ability_ids:
        if a not in seen_abils:
            seen_abils.add(a)
            uniq_abil_ids.append(a)

    ability_data = []
    for aid in uniq_abil_ids:
        try:
            ad = inspect_ability(aid)
            ability_data.append(ad)
        except Exception as e:
            print(f"Warning: ability {aid} error: {e}")

    # 8. Buffs
    buff_ids = [
        'B040', 'B04A', 'B04E', 'B01D', 'Bcyc', 'Bfae', 'Bfro', 'Bblo', 'Bspe', 'Bprg',
        'Broa', 'Brej', 'Bspl', 'Bpoi', 'Bbar', 'Btrv', 'Bams', 'Bpsh', 'Bcor'
    ]
    seen_buffs = set()
    uniq_buff_ids = []
    for b in buff_ids:
        if b not in seen_buffs:
            seen_buffs.add(b)
            uniq_buff_ids.append(b)

    buff_data = []
    for bid in uniq_buff_ids:
        try:
            bd = inspect_buff(bid)
            buff_data.append(bd)
        except Exception as e:
            print(f"Warning: buff {bid} error: {e}")

    out_file = ROOT / "scripts/nightelf_raw_dump.json"
    dump_data = {
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'workers': worker_data,
        'buildings': bld_data,
        'units': unit_data,
        'heroes': hero_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data
    }
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary for Night Elf:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Workers: {len(worker_data)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
