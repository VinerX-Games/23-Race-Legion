# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import wc3_hivewe as hw
wts = hw.load_wts_strings()

def main():
    dump = json.loads((ROOT / 'scripts/hordew2_raw_dump.json').read_text(encoding='utf-8'))

    # Inspect upgrades details
    print("=== UPGRADES DETAILS ===")
    for u in dump.get("upgrades", []):
        uid = u["id"]
        if not (uid.startswith("w2") or uid in ("R0KB", "R0KC", "R0KD")):
            continue
        print(f"\n--- Upgrade {uid} ({u.get('levels')} lvls) ---")
        res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid, '--all'])
        f = res.get('fields', {}) or res.get('object', {})
        ov = res.get('overrides', {})
        get_v = lambda k: ov.get(k) if ov.get(k) is not None else f.get(k)
        for k in ['effect1', 'effect2', 'effect3', 'effect4', 'base1', 'base2', 'mod1', 'mod2', 'applies1', 'applies2', 'applies3', 'applies4']:
            v = get_v(k)
            if v:
                print(f"  {k}: {v}")

    # Inspect abilities details
    print("\n=== ABILITIES DETAILS ===")
    for a in dump.get("abilities", []):
        aid = a["id"]
        if not (aid.startswith("w2") or aid in ("A1JN", "A0QO", "A0RE", "A0Z7", "A0ZA", "A176", "A178", "A1OJ")):
            continue
        print(f"\n--- Ability {aid} ({a.get('name')}) ---")
        res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
        f = res.get('fields', {}) or res.get('object', {})
        ov = res.get('overrides', {})
        get_v = lambda k: ov.get(k) if ov.get(k) is not None else f.get(k)
        for k, v in sorted(ov.items()):
            if any(k.startswith(p) for p in ['data', 'dur', 'cool', 'cost', 'targ', 'cast', 'area', 'rng', 'eff', 'req']):
                print(f"  {k}: {v}")

if __name__ == '__main__':
    main()
