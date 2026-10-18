# -*- coding: utf-8 -*-
"""Map all Nerub objects, fields, and raw TRIGSTR IDs to war3map.wts."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def parse_trigstr(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        try:
            return int(s[8:])
        except ValueError:
            return None
    return None

def main():
    dump = json.loads((ROOT / "scripts/nerubs_raw_dump.json").read_text(encoding="utf-8"))

    print("=== SELECTION ===")
    sel = dump['selection']
    for f in ['name', 'tip1', 'ubertip1']:
        raw = sel.get(f'raw_{f}') or sel.get('tips', {}).get(f, {}).get('raw') or sel.get('ubertips', {}).get(f, {}).get('raw')
        sid = parse_trigstr(raw)
        print(f"  A0HT {f}: sid={sid} raw={raw} text={repr(wts.get(sid))}")

    for m in dump['selection_markers']:
        for l in range(1, m['levels'] + 1):
            for f in ['name', 'tip', 'ubertip']:
                raw = m.get(f'{f}s', {}).get(f'{f}{l}', {}).get('raw')
                sid = parse_trigstr(raw)
                print(f"  {m['id']} {f}{l}: sid={sid} raw={raw} text={repr(wts.get(sid))}")

    print("\n=== BUILDINGS ===")
    for b in dump['buildings']:
        for f in ['name', 'tip', 'ubertip']:
            raw = b.get(f'raw_{f}')
            sid = parse_trigstr(raw)
            print(f"  {b['id']} {f}: sid={sid} raw={raw} text={repr(wts.get(sid))}")

    print("\n=== UNITS ===")
    for u in dump['units']:
        for f in ['name', 'tip', 'ubertip']:
            raw = u.get(f'raw_{f}')
            sid = parse_trigstr(raw)
            print(f"  {u['id']} {f}: sid={sid} raw={raw} text={repr(wts.get(sid))}")

    print("\n=== HEROES ===")
    for h in dump['heroes']:
        for f in ['name', 'propernames', 'tip', 'ubertip', 'awakentip', 'revivetip']:
            raw = h.get(f'raw_{f}')
            sid = parse_trigstr(raw)
            print(f"  {h['id']} {f}: sid={sid} raw={raw} text={repr(wts.get(sid))}")

    print("\n=== UPGRADES ===")
    for u in dump['upgrades']:
        for l in range(1, u['levels'] + 1):
            for f in ['name', 'tip', 'ubertip']:
                raw = u.get(f'{f}s', {}).get(f'{f}{l}', {}).get('raw')
                sid = parse_trigstr(raw)
                print(f"  {u['id']} {f}{l}: sid={sid} raw={raw} text={repr(wts.get(sid))}")

    print("\n=== ABILITIES ===")
    for a in dump['abilities']:
        raw_n = a.get('raw_name')
        sid_n = parse_trigstr(raw_n)
        print(f"  {a['id']} name: sid={sid_n} raw={raw_n} text={repr(wts.get(sid_n))}")
        raw_rt = a.get('raw_researchtip')
        raw_rub = a.get('raw_researchubertip')
        if raw_rt or raw_rub:
            sid_rt = parse_trigstr(raw_rt)
            sid_rub = parse_trigstr(raw_rub)
            print(f"    researchtip: sid={sid_rt} raw={raw_rt} text={repr(wts.get(sid_rt))}")
            print(f"    researchubertip: sid={sid_rub} raw={raw_rub} text={repr(wts.get(sid_rub))}")
        for l in range(1, a['levels'] + 1):
            raw_t = a.get('tips', {}).get(f'tip{l}', {}).get('raw')
            raw_ub = a.get('ubertips', {}).get(f'ubertip{l}', {}).get('raw')
            sid_t = parse_trigstr(raw_t)
            sid_ub = parse_trigstr(raw_ub)
            print(f"    tip{l}: sid={sid_t} raw={raw_t} text={repr(wts.get(sid_t))}")
            print(f"    ubertip{l}: sid={sid_ub} raw={raw_ub} text={repr(wts.get(sid_ub))}")

if __name__ == '__main__':
    main()
