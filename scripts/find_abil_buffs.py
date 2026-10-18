# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import json

abils = [
    'A0J7', 'A1B7', 'A1B8',
    'A0T1', 'A0SW', 'A0LJ', 'A0LI', 'A0IQ', 'Argl', 'A0ML', 'Arlm', 'A0J0', 'A0Z5', 'A0KP',
    'A0B0', 'A0B1', 'A0B2', 'A0AZ', 'AHad',
    'A0I3', 'Aren', 'ANha', 'A0VH', 'A0J9', 'A1KD', 'Apoi',
    'A0SX', 'A0KR', 'A0KQ', 'A0ZU', 'A0IW', 'Ansk', 'Afae', 'A0JG', 'A0IY', 'A0JF',
    'A0KO', 'A0IZ', 'A1KF', 'A1KG', 'A1KE', 'A0KN', 'A0KM', 'A0C4', 'Arpl', 'Arpm',
    'A1R4', 'Afak', 'Aabs', 'ACmi', 'A1JE',
    'A0J2', 'A0SU', 'A0SV', 'A0J1',
    'AUls', 'AEah', 'AUts', 'A0SQ',
    'AEtq', 'AUau', 'AOhx', 'A0ST',
    'A0Y2',
    'A1B6', 'A193', 'A192', 'A188',
    'A197', 'A195', 'A191'
]

buff_ids = set()
for a in abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', a, '--all'])
    f = res.get('fields', {}) or res.get('object', {})
    ov = res.get('overrides', {})
    get_v = lambda k: ov.get(k) if ov.get(k) is not None else f.get(k)
    for i in range(1, 5):
        b = get_v(f'buff{i}') or get_v(f'buffart{i}') or get_v(f'buff')
        if b and isinstance(b, str) and len(b.strip()) == 4:
            buff_ids.add(b.strip())

print("Found buffs in abilities:", sorted(list(buff_ids)))
