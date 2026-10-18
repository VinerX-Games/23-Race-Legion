# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

race_abils = [
    'A0HX', 'A01Z', 'A09Q', 'A09R', 'A09S', 'A09T', 'A09U', 'A09V', 'A09W', 'A09X',
    'A0A0', 'A0A1', 'A0A2', 'A0AI', 'A0AJ', 'A0AK', 'A0AL', 'A0AM', 'A0AN', 'A1QQ',
    'A09Z', 'A0AO', 'A0AP', 'A0B6', 'A0B8', 'A0B9', 'A0BA', 'A0BB', 'A0BC', 'A0BD',
    'A0BE', 'A0BF', 'A0B7'
]

results = {}
for aid in race_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid, '--all'])
    f = res.get('fields', {})
    ov = res.get('overrides', {})
    levels = int(f.get('levels') or 1)
    results[aid] = {
        'id': aid,
        'levels': levels,
        'name': {'raw': f.get('name'), 'val': resolve(f.get('name'))},
        'hotkey': {'raw': f.get('hotkey'), 'val': resolve(f.get('hotkey'))},
        'researchhotkey': {'raw': f.get('researchhotkey'), 'val': resolve(f.get('researchhotkey'))},
        'researchtip': {'raw': f.get('researchtip'), 'val': resolve(f.get('researchtip'))},
        'researchubertip': {'raw': f.get('researchubertip'), 'val': resolve(f.get('researchubertip'))},
        'levels_data': {}
    }
    for i in range(1, levels + 1):
        results[aid]['levels_data'][f'level{i}'] = {
            'tip': {'raw': f.get(f'tip{i}'), 'val': resolve(f.get(f'tip{i}'))},
            'ubertip': {'raw': f.get(f'ubertip{i}'), 'val': resolve(f.get(f'ubertip{i}'))},
            'untip': {'raw': f.get(f'untip{i}'), 'val': resolve(f.get(f'untip{i}'))},
            'unubertip': {'raw': f.get(f'unubertip{i}'), 'val': resolve(f.get(f'unubertip{i}'))},
        }

(ROOT / "scripts/twilight_race_abils_detailed.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved twilight_race_abils_detailed.json")
