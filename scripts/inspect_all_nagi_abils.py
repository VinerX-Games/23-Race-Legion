# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_ability

candidate_abils = [
    'A14O', # Selection
    # Hero Vashj & Huntress & Guard & Giant & Murloc Sorcerer
    'A13A', 'A136', 'A137', 'A138', 'A139', 'A13B', 'A13C', 'A13D',
    'A14F', 'A14G', 'A14H', 'A14I',
    'A16B', 'A16C', 'A16D', 'A16E', 'A16F',
    'AEbl', 'AEtq', 'AHbn', 'AHab', 'ANrf',
    # Units & Buildings abilities
    'A01C', 'A06U', 'A0I3', 'A0IQ', 'A0LI', 'A0LJ',
    'A14J', 'A14K', 'A14L', 'A14M', 'A14N', 'A1KB', 'A1LT',
    'A1OL', 'A1OM', 'A1ON', 'A1OO', 'A1OP', 'A1OQ', 'A1OR',
    'A1R9', 'A135', 'A1LV', 'AChx', 'AGbu', 'S00A', 'S00E',
    'ACcb', 'ACcv', 'ACen', 'ACfu', 'ACpv', 'ACsk', 'ACwe',
    'ANen', 'ANha', 'ANpa', 'Acny', 'Advc', 'Arep', 'Argl', 'Arlm',
    'Asb1', 'Asb2', 'Asb3', 'drAq'
]

print(f"Total abilities to inspect: {len(candidate_abils)}")
res = {}
for aid in candidate_abils:
    try:
        data = inspect_ability(aid)
        res[aid] = data
        name = data.get('name')
        name_sid = data.get('name_sid')
        # Check if it has any WTS string or overrides
        has_wts = name_sid is not None
        for k, v in data.get('tips', {}).items():
            if v.get('sid'): has_wts = True
        for k, v in data.get('ubertips', {}).items():
            if v.get('sid'): has_wts = True
        if data.get('researchtip_sid') or data.get('researchubertip_sid'):
            has_wts = True
        print(f"Ability {aid}: name={name} (sid={name_sid}) levels={data.get('levels')} has_wts={has_wts}")
    except Exception as e:
        print(f"Error inspecting {aid}: {e}")

out_file = ROOT / "scripts/nagi_abils_dump.json"
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
print(f"Saved to {out_file}")
