# -*- coding: utf-8 -*-
"""Analyze dumped Vryculs and Random data and print readable summary of strings and stats."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
def res(raw):
    if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
        try:
            return int(raw[8:]), wts.get(int(raw[8:]), raw)
        except:
            return None, raw
    return None, raw

def main():
    vdata = json.load(open(ROOT / "scripts/vrykul_raw_dump.json", encoding="utf-8"))
    rdata = json.load(open(ROOT / "scripts/random_raw_dump.json", encoding="utf-8"))
    
    print("=================== 1. SELECTION ABILITIES ===================")
    for data, name in [(vdata, "Vryculs"), (rdata, "Random")]:
        sel = data['selection']
        sid_name, txt_name = res(sel.get('raw_name'))
        sid_tip, txt_tip = res(sel.get('tips', {}).get('tip1', {}).get('raw'))
        sid_ub, txt_ub = res(sel.get('ubertips', {}).get('ubertip1', {}).get('raw'))
        hk = sel.get('hotkey')
        print(f"{name} ({sel['id']}):")
        print(f"  Name:   [{sid_name}] {txt_name}")
        print(f"  Tip:    [{sid_tip}] {txt_tip} (Hotkey: {hk})")
        print(f"  Ubertip:[{sid_ub}] {txt_ub}\n")

    print("=================== 2. SELECTION MARKERS ===================")
    for m in vdata['selection_markers']:
        sid_name, txt_name = res(m.get('raw_name'))
        sid_tip, txt_tip = res(m.get('tips', {}).get('tip1', {}).get('raw'))
        sid_ub, txt_ub = res(m.get('ubertips', {}).get('ubertip1', {}).get('raw'))
        print(f"Marker {m['id']} (levels={m.get('levels')}):")
        print(f"  Name:   [{sid_name}] {txt_name}")
        print(f"  Tip:    [{sid_tip}] {txt_tip}")
        print(f"  Ubertip:[{sid_ub}] {txt_ub}\n")

    print("=================== 3. BUILDINGS ===================")
    for b in vdata['buildings']:
        sid_name, txt_name = res(b.get('raw_name'))
        sid_tip, txt_tip = res(b.get('raw_tip'))
        sid_ub, txt_ub = res(b.get('raw_ubertip'))
        hk = b.get('hotkey')
        print(f"Building {b['id']} ({b.get('name')}):")
        print(f"  Name:   [{sid_name}] {txt_name}")
        print(f"  Tip:    [{sid_tip}] {txt_tip} (Hotkey: {hk})")
        print(f"  Ubertip:[{sid_ub}] {txt_ub[:80] if txt_ub else 'None'}...")
        print(f"  Trains: {b.get('train')} | Researches: {b.get('researches')} | UpgradesTo: {b.get('upgrades_to')} | Abils: {b.get('abillist')}\n")

    print("=================== 4. HEROES ===================")
    for h in vdata['heroes']:
        sid_name, txt_name = res(h.get('raw_name'))
        sid_prop, txt_prop = res(h.get('raw_propernames'))
        sid_tip, txt_tip = res(h.get('raw_tip'))
        sid_ub, txt_ub = res(h.get('raw_ubertip'))
        sid_aw, txt_aw = res(h.get('raw_awakentip'))
        sid_rev, txt_rev = res(h.get('raw_revivetip'))
        hk = h.get('hotkey')
        print(f"Hero {h['id']} ({h.get('name')}):")
        print(f"  Name:       [{sid_name}] {txt_name}")
        print(f"  Propernames:[{sid_prop}] {txt_prop}")
        print(f"  Tip:        [{sid_tip}] {txt_tip} (Hotkey: {hk})")
        print(f"  AwakenTip:  [{sid_aw}] {txt_aw}")
        print(f"  ReviveTip:  [{sid_rev}] {txt_rev}")
        print(f"  Ubertip:    [{sid_ub}] {txt_ub[:80] if txt_ub else 'None'}...")
        print(f"  HeroAbils:  {h.get('heroabillist')} | Abils: {h.get('abillist')} | Targs1: {h.get('targs1')}\n")

    print("=================== 5. UNITS ===================")
    for u in vdata['units']:
        sid_name, txt_name = res(u.get('raw_name'))
        sid_tip, txt_tip = res(u.get('raw_tip'))
        sid_ub, txt_ub = res(u.get('raw_ubertip'))
        hk = u.get('hotkey')
        print(f"Unit {u['id']} ({u.get('name')}):")
        print(f"  Name:   [{sid_name}] {txt_name}")
        print(f"  Tip:    [{sid_tip}] {txt_tip} (Hotkey: {hk})")
        print(f"  Ubertip:[{sid_ub}] {txt_ub[:80] if txt_ub else 'None'}...")
        print(f"  Abils:  {u.get('abillist')} | Upgrades: {u.get('upgrades')} | Targs1: {u.get('targs1')} | Weap1: {u.get('weaptype1')}\n")

    print("=================== 6. UPGRADES ===================")
    for up in vdata['upgrades']:
        lvls = up.get('levels', 1)
        print(f"Upgrade {up['id']} (levels={lvls}):")
        for l in range(1, lvls + 1):
            sid_name, txt_name = res(up.get('names', {}).get(f'name{l}', {}).get('raw'))
            sid_tip, txt_tip = res(up.get('tips', {}).get(f'tip{l}', {}).get('raw'))
            sid_ub, txt_ub = res(up.get('ubertips', {}).get(f'ubertip{l}', {}).get('raw'))
            hk = up.get('hotkeys', {}).get(f'hotkey{l}')
            print(f"  Lvl {l}: Name=[{sid_name}] {txt_name} | Tip=[{sid_tip}] {txt_tip} (HK: {hk}) | Ub=[{sid_ub}] {txt_ub[:60] if txt_ub else 'None'}...")
        print()

    print("=================== 7. ABILITIES ===================")
    for ab in vdata['abilities']:
        lvls = ab.get('levels', 1)
        sid_name, txt_name = res(ab.get('raw_name'))
        sid_rt, txt_rt = res(ab.get('raw_researchtip'))
        sid_rub, txt_rub = res(ab.get('raw_researchubertip'))
        hk = ab.get('hotkey')
        print(f"Ability {ab['id']} ({txt_name}) [levels={lvls}, HK={hk}]:")
        if sid_rt or sid_rub:
            print(f"  ResearchTip: [{sid_rt}] {txt_rt} | ResearchUb: [{sid_rub}] {txt_rub[:50] if txt_rub else ''}")
        for l in range(1, lvls + 1):
            sid_tip, txt_tip = res(ab.get('tips', {}).get(f'tip{l}', {}).get('raw'))
            sid_ub, txt_ub = res(ab.get('ubertips', {}).get(f'ubertip{l}', {}).get('raw'))
            print(f"  Lvl {l}: Tip=[{sid_tip}] {txt_tip} | Ub=[{sid_ub}] {txt_ub[:60] if txt_ub else ''}")
        print()

if __name__ == '__main__':
    main()
