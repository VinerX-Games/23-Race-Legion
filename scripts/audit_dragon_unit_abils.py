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

unit_abils = [
    'A0I3', 'A1LR', 'A0RK', 'drat', 'A0RE',
    'drAa', 'drAs', 'Alit', 'A0RO', 'A0RJ',
    'drAz', 'drA2', 'drAw', 'drAy', 'drAe',
    'drAr', 'drEt', 'drAd', 'drA0', 'drA3',
    'drA4', 'A1BD', 'drA5', 'A0QB', 'Afrb',
    'dra3', 'drA6', 'drA1', 'drAq', 'drA7',
    'A0RM', 'drA8', 'drA9', 'A1BF', 'A0RL',
    'A0QO', 'A0RN'
]

bulk_abils_sd = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(unit_abils)]))
bulk_abils_hd = require(cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(unit_abils), '--hd']))

abils_audit = {}
for o in bulk_abils_sd['objects']:
    aid = o['id']
    f_sd = o['fields']
    f_hd = next((x['fields'] for x in bulk_abils_hd['objects'] if x['id'] == aid), {})
    levels = int(f_sd.get('levels') or 1)
    
    fields = {}
    keys = ['name', 'hotkey', 'unhotkey']
    for lvl in range(1, levels + 1):
        keys.extend([f'tip{lvl}', f'ubertip{lvl}', f'untip{lvl}', f'unubertip{lvl}'])
        
    for k in keys:
        raw_sd = f_sd.get(k)
        raw_hd = f_hd.get(k)
        if raw_sd is not None or raw_hd is not None:
            fields[k] = {
                'raw_sd': raw_sd,
                'raw_hd': raw_hd,
                'resolved_sd': resolve(raw_sd),
                'resolved_hd': resolve(raw_hd),
                'is_wts': isinstance(raw_sd, str) and raw_sd.startswith('TRIGSTR_'),
                'wts_id': int(raw_sd[8:]) if isinstance(raw_sd, str) and raw_sd.startswith('TRIGSTR_') else None
            }
            
    abils_audit[aid] = {
        'id': aid,
        'levels': levels,
        'buttonpos': (f_sd.get('buttonpos'), f_sd.get('buttonpos2')),
        'fields': fields
    }

# Buffs audit
buff_ids = ['B05D', 'B05C', 'B03U', 'Bdr0', 'B02J', 'B05S']
buffs_audit = {}
for bid in buff_ids:
    b_sd = require(cli(['get-object', '--type', 'buff', '--id', bid]))['fields']
    b_hd = require(cli(['get-object', '--type', 'buff', '--id', bid, '--hd']))['fields']
    
    fields = {}
    for k in ['bufftip', 'buffubertip']:
        raw_sd = b_sd.get(k)
        raw_hd = b_hd.get(k)
        fields[k] = {
            'raw_sd': raw_sd,
            'raw_hd': raw_hd,
            'resolved_sd': resolve(raw_sd),
            'resolved_hd': resolve(raw_hd),
            'is_wts': isinstance(raw_sd, str) and raw_sd.startswith('TRIGSTR_'),
            'wts_id': int(raw_sd[8:]) if isinstance(raw_sd, str) and raw_sd.startswith('TRIGSTR_') else None
        }
    buffs_audit[bid] = {
        'id': bid,
        'fields': fields
    }

output = {
    'abilities': abils_audit,
    'buffs': buffs_audit
}
output_path = ROOT / "docs/ui_text/dragon_unit_abils_audit.json"
output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Audited {len(unit_abils)} unit abilities and {len(buff_ids)} buffs. Written to {output_path}")
