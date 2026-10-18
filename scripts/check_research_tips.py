# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wc3_object_tools import cli, require

abil_ids = [
    'A0AW', 'A0AV', 'A0A6', 'A0D6', 'A0AX', 'A0D2', 'A0Z4', 'A0D1', 'A0AB',
    'A0AR', 'A0A8', 'A0A7', 'A0A5', 'A0BL', 'A0A9', 'A1MT', 'A0LG', 'A0LF',
    'A0A4', 'A0D3', 'A0D4', 'Asds', 'A0AH', 'A0BK', 'A0AS', 'A0AT', 'A0AU',
    'A0KS', 'A0LD', 'A0LE', 'A0LH', 'S001', 'A15N', 'A0UU'
]

bulk = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(abil_ids)]))
for obj in bulk.get('objects', []):
    f = obj['fields']
    rt = f.get('researchtip')
    rut = f.get('researchubertip')
    if rt or rut:
        print(f"[{obj['id']}] researchtip={rt}, researchubertip={rut}")
