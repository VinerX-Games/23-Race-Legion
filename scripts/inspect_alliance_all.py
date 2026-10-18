# -*- coding: utf-8 -*-
"""Inspect all Alliance race objects and output structured JSON and summary."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_unit, inspect_ability, inspect_upgrade, inspect_buff

def main():
    print("=== INSPECTING ALLIANCE (RACE 29) OBJECTS ===")

    # 1. Selection
    selection_ability = inspect_ability('A02A')
    marker_ids = ['R0GZ', 'R0HX', 'R0HW', 'R0HY', 'R0KK']
    selection_markers = [inspect_upgrade(m) for m in marker_ids]

    # 2. Buildings (16)
    bld_ids = [
        'htow', 'hkee', 'hcas', 'hhou', 'hbar', 'hbla', 'hwtw', 'hgtw',
        'hctw', 'hatw', 'halt', 'harm', 'hars', 'hlum', 'hgra', 'h0M4'
    ]
    bld_data = [inspect_unit(b) for b in bld_ids]

    # 3. Heroes (11)
    hero_ids = [
        'H0H7', 'H0H9', 'H0H8', 'H0ME', 'H0MF', 'H0MD',
        'Hamg', 'Hmkg', 'Hpal', 'Hblm', 'Hlgr'
    ]
    hero_data = [inspect_unit(h) for h in hero_ids]

    # 4. Units (56)
    unit_ids = [
        # Base units (17)
        'hpea', 'hfoo', 'h0K4', 'h0K7', 'hrif', 'h0K5', 'h0K6', 'hkni',
        'hmtm', 'hmtt', 'h0KI', 'hmpr', 'hsor', 'hspt', 'h00X', 'h0L0', 'h0L1',
        # Dynamic / Embassy units (39)
        'h0KD', 'h0KH', 'h0LW', 'h0KE', 'h0LU', 'h0OW',
        'h0KR', 'h0KC', 'h0KK', 'h0KW',
        'h0M9', 'h0MA',
        'h0M7', 'h0M5', 'h0M6',
        'h0M2', 'h0M3',
        'h0KN', 'h0L2', 'h0LZ', 'h0KT',
        'h0KO', 'h0KY', 'h0KJ', 'h0KS', 'h0LY', 'h0KP', 'h0KZ', 'o044',
        'h0MB', 'h0MC', 'h0KX',
        'o042', 'o043',
        'h0M8', 'o040',
        'h0KA', 'h0KB', 'h0K9', 'h0KL', 'h0KM', 'h0KQ', 'h0KU', 'h0KV', 'h0KF', 'h0KG'
    ]
    unit_data = [inspect_unit(u) for u in unit_ids]

    # 5. Upgrades (58)
    upgrade_ids = [
        'R002', 'R003', 'R004', 'R005', 'R006', 'R007', 'R0GV', 'R0GW',
        'R0GX', 'R0GY', 'R0GZ', 'R0H5', 'R0H6', 'R0H7', 'R0H8', 'R0H9',
        'R0HA', 'R0HB', 'R0HC', 'R0HD', 'R0HE', 'R0HF', 'R0HG', 'R0HH',
        'R0HI', 'R0HJ', 'R0HK', 'R0HL', 'R0HM', 'R0HN', 'R0HO', 'R0HQ',
        'R0HR', 'R0HS', 'R0HU', 'R0HV', 'R0HW', 'R0HX', 'R0HY', 'R0KK',
        'Rgfo', 'Rguv', 'Rhac', 'Rhan', 'Rhar', 'Rhde', 'Rhla', 'Rhlh',
        'Rhme', 'Rhpm', 'Rhpt', 'Rhra', 'Rhri', 'Rhrt', 'Rhsb', 'Rhse',
        'Rhss', 'Rhst'
    ]
    upgrade_data = [inspect_upgrade(u) for u in upgrade_ids]

    # 6. Abilities (147)
    ability_ids = [
        'A001', 'A002', 'A009', 'A00A', 'A00B', 'A00G', 'A00I', 'A00Z',
        'A02A', 'A0I3', 'A0IQ', 'A0LI', 'A0LJ', 'A0WZ', 'A0X0', 'A0X3',
        'A0X4', 'A0X5', 'A0X6', 'A0X7', 'A0X8', 'A0X9', 'A0XA', 'A0XH',
        'A0XI', 'A0XJ', 'A0Z5', 'A10C', 'A127', 'A129', 'A15N', 'A165',
        'A17Y', 'A180', 'A183', 'A184', 'A185', 'A18C', 'A18D', 'A18E',
        'A18F', 'A18G', 'A18H', 'A18I', 'A18K', 'A18L', 'A18M', 'A18N',
        'A18O', 'A18P', 'A18V', 'A18W', 'A18X', 'A190', 'A198', 'A199',
        'A19A', 'A19B', 'A19D', 'A19E', 'A19F', 'A19G', 'A19I', 'A19K',
        'A19M', 'A19N', 'A19O', 'A19P', 'A19Q', 'A19R', 'A19S', 'A19W',
        'A19X', 'A19Y', 'A19Z', 'A1A0', 'A1A1', 'A1A2', 'A1A3', 'A1A4',
        'A1A5', 'A1A6', 'A1A8', 'A1A9', 'A1AA', 'A1AB', 'A1AC', 'A1AD',
        'A1AE', 'A1AG', 'A1AH', 'A1AI', 'A1AL', 'A1AN', 'A1NO', 'A1OA',
        'A1OB', 'A1OD', 'A1OE', 'A1PS', 'A1PT', 'ACcs', 'AHab', 'AHad',
        'AHav', 'AHbh', 'AHbn', 'AHbz', 'AHdr', 'AHds', 'AHfs', 'AHhb',
        'AHmt', 'AHpx', 'AHre', 'AHta', 'AHtb', 'AHtc', 'AHwe', 'AInv',
        'Adef', 'Adts', 'Afae', 'Afbt', 'Ahar', 'Ahea', 'Ahri', 'Ahrp',
        'Aihn', 'Ainf', 'Amic', 'Amil', 'Aply', 'Argl', 'Arlm', 'Aslo',
        'Asph', 'Aspo', 'Asps', 'S00C', 'Sch5', 'Sdro', 'Slo3', 'alA0',
        'alA1', 'alA2', 'alA3'
    ]
    ability_data = [inspect_ability(a) for a in ability_ids]

    # 7. Buffs
    buff_ids = [
        'AEtr', 'B002', 'B004', 'B007', 'B011', 'B023', 'B030', 'B06A',
        'B06B', 'B06T', 'B06U', 'B06V', 'B06Y', 'B06Z', 'B073', 'BEah',
        'BEer', 'BHab', 'BHad', 'BHbd', 'BHbn', 'BHbz', 'BHca', 'BHds',
        'BHfs', 'BHtc', 'BHwe', 'BNbf', 'BNcs', 'BNlm', 'BNpa', 'BNpi',
        'BNpm', 'BNss', 'BOae', 'BOsh', 'BOwk', 'BPSE', 'BUau', 'BUcs',
        'BUhf', 'Bcri', 'Bcrs', 'Bcsd', 'Bcsi', 'Bcy2', 'Bcyc', 'Bdbb',
        'Bdbl', 'Bdbm', 'Bdcb', 'Bdcl', 'Bdcm', 'Bdtb', 'Bdtl', 'Bdtm',
        'Bfae', 'Bfro', 'Bfzy', 'Bhea', 'Binf', 'Bmfa', 'Bmfl', 'Bpig',
        'Bply', 'Bpoi', 'Bpsd', 'Brpl', 'Bslo', 'Bspo', 'Bssd'
    ]
    buff_data = [inspect_buff(b) for b in buff_ids]

    out_file = ROOT / "scripts/alliance_raw_dump.json"
    dump_data = {
        'race': 'Alliance',
        'race_id': 29,
        'selection': selection_ability,
        'selection_markers': selection_markers,
        'buildings': bld_data,
        'heroes': hero_data,
        'units': unit_data,
        'upgrades': upgrade_data,
        'abilities': ability_data,
        'buffs': buff_data
    }
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dump_data, f, ensure_ascii=False, indent=2)

    print(f"\nInspection summary for Alliance:")
    print(f"  Selection ability: 1 ({selection_ability['id']})")
    print(f"  Selection markers: {len(selection_markers)}")
    print(f"  Buildings: {len(bld_data)}")
    print(f"  Heroes: {len(hero_data)}")
    print(f"  Units: {len(unit_data)}")
    print(f"  Upgrades: {len(upgrade_data)}")
    print(f"  Abilities: {len(ability_data)}")
    print(f"  Buffs: {len(buff_data)}")
    print(f"Saved raw dump to {out_file}")

if __name__ == '__main__':
    main()
