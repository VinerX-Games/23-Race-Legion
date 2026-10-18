# -*- coding: utf-8 -*-
"""Analyze Nightborne raw dump and print detailed report for standardizing UI texts."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def parse_sid(val):
    if isinstance(val, str) and val.startswith("TRIGSTR_"):
        try:
            return int(val[8:])
        except ValueError:
            pass
    return None

def analyze():
    dump = json.load(open(ROOT / "scripts/nightborne_raw_dump.json", encoding="utf-8"))

    report = []
    def p(line=""):
        report.append(line)

    p("===============================================================================")
    p("1. SELECTION & MARKERS")
    p("===============================================================================")
    sel = dump['selection']
    p(f"Selection Ability: {sel['id']}")
    p(f"  Name: {sel['name']} (raw: {sel['raw_name']}, sid: {parse_sid(sel['raw_name'])})")
    p(f"  Hotkey: {sel['hotkey']} (raw: {sel['raw_hotkey']})")
    for k, v in sel['tips'].items():
        p(f"  {k}: {v['val']} (sid: {parse_sid(v['raw'])})")
    for k, v in sel['ubertips'].items():
        p(f"  {k}: {v['val']} (sid: {parse_sid(v['raw'])})")

    for m in dump['selection_markers']:
        p(f"\nSelection Marker: {m['id']}")
        for k, v in m['names'].items():
            p(f"  {k}: {v['val']} (sid: {parse_sid(v['raw'])})")
        for k, v in m['tips'].items():
            p(f"  {k}: {v['val']} (sid: {parse_sid(v['raw'])})")
        for k, v in m['ubertips'].items():
            p(f"  {k}: {v['val']} (sid: {parse_sid(v['raw'])})")

    p("\n===============================================================================")
    p("2. BUILDINGS")
    p("===============================================================================")
    for b in dump['buildings']:
        p(f"\nBuilding: {b['id']} -> {b['name']}")
        p(f"  Name sid: {parse_sid(b['raw_name'])}")
        p(f"  Tip: {b['tip']} (sid: {parse_sid(b['raw_tip'])})")
        p(f"  Ubertip: {b['ubertip']} (sid: {parse_sid(b['raw_ubertip'])})")
        p(f"  Hotkey: {b['hotkey']} (raw: {b['raw_hotkey']})")
        p(f"  Trains: {b['train']}")
        p(f"  Researches: {b['researches']}")
        p(f"  Upgrades to: {b['upgrades_to']}")
        p(f"  Abilities: {b['abillist']}")
        p(f"  Targs1: {b['targs1']}, Targs2: {b['targs2']}")

    p("\n===============================================================================")
    p("3. UNITS")
    p("===============================================================================")
    for u in dump['units']:
        p(f"\nUnit: {u['id']} -> {u['name']}")
        p(f"  Name sid: {parse_sid(u['raw_name'])}")
        p(f"  Tip: {u['tip']} (sid: {parse_sid(u['raw_tip'])})")
        p(f"  Ubertip: {u['ubertip']} (sid: {parse_sid(u['raw_ubertip'])})")
        p(f"  Hotkey: {u['hotkey']} (raw: {u['raw_hotkey']})")
        p(f"  Abilities: {u['abillist']}")
        p(f"  Upgrades: {u['upgrades']}")
        p(f"  HP: {u['hp']}, Mana: {u['mana']}")
        p(f"  Atk1: {u['atktype1']}, Targs1: {u['targs1']}, Weap1: {u['weaptype1']}")
        p(f"  Atk2: {u['atktype2']}, Targs2: {u['targs2']}, Weap2: {u['weaptype2']}")

    p("\n===============================================================================")
    p("4. HEROES")
    p("===============================================================================")
    for h in dump['heroes']:
        p(f"\nHero: {h['id']} -> {h['name']}")
        p(f"  Name sid: {parse_sid(h['raw_name'])}")
        p(f"  Propernames: {h['propernames']} (sid: {parse_sid(h['raw_propernames'])})")
        p(f"  Tip: {h['tip']} (sid: {parse_sid(h['raw_tip'])})")
        p(f"  Ubertip: {h['ubertip']} (sid: {parse_sid(h['raw_ubertip'])})")
        p(f"  Hotkey: {h['hotkey']} (raw: {h['raw_hotkey']})")
        p(f"  Hero abils: {h['heroabillist']}")
        p(f"  Other abils: {h['abillist']}")
        p(f"  Primary stat: {h['fields'].get('primary')}")
        p(f"  Atk1: {h['atktype1']}, Targs1: {h['targs1']}")

    p("\n===============================================================================")
    p("5. UPGRADES")
    p("===============================================================================")
    for upg in dump['upgrades']:
        p(f"\nUpgrade: {upg['id']} (levels: {upg['levels']})")
        for lvl in range(1, upg['levels'] + 1):
            nm = upg['names'].get(f'name{lvl}', {})
            tp = upg['tips'].get(f'tip{lvl}', {})
            ub = upg['ubertips'].get(f'ubertip{lvl}', {})
            hk = upg['hotkeys'].get(f'hotkey{lvl}', {})
            p(f"  Level {lvl}:")
            p(f"    Name: {nm.get('val')} (sid: {parse_sid(nm.get('raw'))})")
            p(f"    Hotkey: {hk.get('val')} (raw: {hk.get('raw')})")
            p(f"    Tip: {tp.get('val')} (sid: {parse_sid(tp.get('raw'))})")
            p(f"    Ubertip: {ub.get('val')} (sid: {parse_sid(ub.get('raw'))})")

    p("\n===============================================================================")
    p("6. ABILITIES")
    p("===============================================================================")
    for a in dump['abilities']:
        p(f"\nAbility: {a['id']} -> {a['name']} (levels: {a['levels']})")
        p(f"  Name sid: {parse_sid(a['raw_name'])}")
        p(f"  Hotkey: {a['hotkey']} (raw: {a['raw_hotkey']})")
        p(f"  Research hotkey: {a['researchhotkey']} (raw: {a['fields'].get('researchhotkey')})")
        p(f"  Research tip: {a['researchtip']} (sid: {parse_sid(a['raw_researchtip'])})")
        p(f"  Research ubertip: {a['researchubertip']} (sid: {parse_sid(a['raw_researchubertip'])})")
        for lvl in range(1, a['levels'] + 1):
            tp = a['tips'].get(f'tip{lvl}', {})
            ub = a['ubertips'].get(f'ubertip{lvl}', {})
            p(f"  Level {lvl}:")
            p(f"    Tip: {tp.get('val')} (sid: {parse_sid(tp.get('raw'))})")
            p(f"    Ubertip: {ub.get('val')} (sid: {parse_sid(ub.get('raw'))})")

    out_path = ROOT / "scripts/nightborne_analysis.txt"
    out_path.write_text("\n".join(report), encoding="utf-8")
    print(f"Analysis written to {out_path} ({len(report)} lines)")

if __name__ == '__main__':
    analyze()
