# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wc3_hivewe as hw
from wc3_object_tools import cli, require

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

hero_abils = [
    # Nozdormu
    'A0RB', 'A0QY', 'A0R0', 'A0QX', 'A0QZ',
    # Ysera
    'A0RD', 'A0R4', 'A0R3', 'A0R2', 'A1MX',
    # Alexstrasza
    'A0RA', 'A0R5', 'A0R6', 'A0R7', 'A0R8',
    # Malygos
    'A0RC', 'A0QV', 'A0QU', 'A0QT', 'A10E'
]

bulk_sd = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(hero_abils)]))
bulk_hd = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(hero_abils), '--hd']))

sd_by_id = {o['id']: o['fields'] for o in bulk_sd['objects']}
hd_by_id = {o['id']: o['fields'] for o in bulk_hd['objects']}

audit = {}
for aid in hero_abils:
    sd_f = sd_by_id.get(aid, {})
    hd_f = hd_by_id.get(aid, {})
    
    levels = int(sd_f.get('levels') or 1)
    hotkey = resolve(sd_f.get('hotkey'))
    r_hotkey = resolve(sd_f.get('researchhotkey'))
    
    fields = {}
    keys = ['name', 'researchtip', 'researchubertip']
    for lvl in range(1, levels + 1):
        keys.extend([f'tip{lvl}', f'ubertip{lvl}'])
        
    for k in keys:
        raw_sd = sd_f.get(k)
        raw_hd = hd_f.get(k)
        fields[k] = {
            'raw_sd': raw_sd,
            'raw_hd': raw_hd,
            'resolved_sd': resolve(raw_sd),
            'resolved_hd': resolve(raw_hd),
            'is_wts': isinstance(raw_sd, str) and raw_sd.startswith('TRIGSTR_'),
            'wts_id': int(raw_sd[8:]) if isinstance(raw_sd, str) and raw_sd.startswith('TRIGSTR_') else None
        }
        
    audit[aid] = {
        'id': aid,
        'levels': levels,
        'hotkey': hotkey,
        'researchhotkey': r_hotkey,
        'buttonpos': (sd_f.get('buttonpos'), sd_f.get('buttonpos2')),
        'fields': fields
    }

output_path = ROOT / "docs/ui_text/dragon_hero_abils_audit.json"
output_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Audited {len(hero_abils)} hero abilities. Written to {output_path}")
