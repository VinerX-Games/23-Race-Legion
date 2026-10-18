import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def get_obj(oid):
    wts = hw.load_wts_strings()
    for otype in ['unit', 'ability', 'upgrade', 'buff']:
        res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', otype, '--id', oid])
        if res.get('success'):
            fields = res.get('object', {}) or res.get('fields', {})
            name = fields.get('name') or fields.get('name1')
            if isinstance(name, str) and name.startswith('TRIGSTR_'):
                sid = int(name[8:])
                name = wts.get(sid, name)
            return otype, name
    return 'unknown', 'UNKNOWN'

def inspect():
    horde_ai = (ROOT / "map.w3x/_lua/monolith_split/sections/82_ai_races/05_horde.lua").read_text(encoding="utf-8")
    be_ai = (ROOT / "map.w3x/_lua/monolith_split/sections/82_ai_races/02_blood_elves.lua").read_text(encoding="utf-8")

    h_ai_codes = sorted(list(set(re.findall(r"FourCC\('([A-Za-z0-9_]{4})'\)", horde_ai))))
    be_ai_codes = sorted(list(set(re.findall(r"FourCC\('([A-Za-z0-9_]{4})'\)", be_ai))))

    print("=== HORDE AI OBJECTS ===")
    for c in h_ai_codes:
        otype, name = get_obj(c)
        print(f"  {c} ({otype}): {name}")

    print("\n=== BLOOD ELVES AI OBJECTS ===")
    for c in be_ai_codes:
        otype, name = get_obj(c)
        print(f"  {c} ({otype}): {name}")

if __name__ == "__main__":
    inspect()
