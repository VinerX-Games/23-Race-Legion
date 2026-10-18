# -*- coding: utf-8 -*-
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

def get_sid(s):
    if isinstance(s, str) and s.startswith('TRIGSTR_'):
        try:
            return int(s[8:])
        except ValueError:
            return None
    return None

objects_to_check = {
    'selection': [('ability', 'A0HV')],
    'buildings': [
        ('unit', 'n014'), ('unit', 'u00F'), ('unit', 'u00G'), ('unit', 'u00H'),
        ('unit', 'u00I'), ('unit', 'u00J'), ('unit', 'u00K'), ('unit', 'u00L'),
        ('unit', 'u00M'), ('unit', 'u00N'), ('unit', 'n012'), ('unit', 'u03B'),
        ('unit', 'u017')
    ],
    'heroes': [
        ('unit', 'U00O'), ('unit', 'U00V'), ('unit', 'U00U'), ('unit', 'U030'),
        ('unit', 'U014'), ('unit', 'CM00'), ('unit', 'FL00')
    ],
    'units': [
        ('unit', 'u00P'), ('unit', 'n011'), ('unit', 'n013'), ('unit', 'u03E'),
        ('unit', 'u02B'), ('unit', 'u00A'), ('unit', 'u00B'), ('unit', 'u00D'),
        ('unit', 'u00C'), ('unit', 'u008'), ('unit', 'u00E'), ('unit', 'u034'),
        ('unit', 'ft00'), ('unit', 'ft01'), ('unit', 'n07H'), ('unit', 'u03D'),
        ('unit', 'n016'), ('unit', 'n017')
    ],
    'researches': [
        ('upgrade', 'R0DQ'), ('upgrade', 'R05I'), ('upgrade', 'R05J'), ('upgrade', 'R05N'),
        ('upgrade', 'R05O'), ('upgrade', 'R05P'), ('upgrade', 'R05Q'), ('upgrade', 'R05L'),
        ('upgrade', 'R05H'), ('upgrade', 'R05E'), ('upgrade', 'R05F'), ('upgrade', 'R05G'),
        ('upgrade', 'R05A'), ('upgrade', 'R05R'), ('upgrade', 'R05D'), ('upgrade', 'R05C'),
        ('upgrade', 'R07I'), ('upgrade', 'R0J5')
    ],
    'hero_abilities': [
        ('ability', 'A0CO'), ('ability', 'A0CP'), ('ability', 'A0CR'), ('ability', 'A0CN'),
        ('ability', 'AQ95'), ('ability', 'UN99'), ('ability', 'A0CS'), ('ability', 'AQ11'),
        ('ability', 'A0CK'), ('ability', 'A0CM'), ('ability', 'A0BW'), ('ability', 'A1Q7'),
        ('ability', 'A1LI'), ('ability', 'A1LJ'), ('ability', 'A1LL'), ('ability', 'A1LM'),
        ('ability', 'A1LK'),
        ('ability', 'A0WD'), ('ability', 'A0CX'), ('ability', 'A0WE'), ('ability', 'A0CZ'),
        ('ability', 'A0WB'), ('ability', 'A0WC'), ('ability', 'A0WF'),
        ('ability', 'CM01'), ('ability', 'CM02'), ('ability', 'CM04'), ('ability', 'CM05'),
        ('ability', 'FL01'), ('ability', 'FL02'), ('ability', 'FL03'), ('ability', 'FL04')
    ],
    'unit_abilities': [
        ('ability', 'A0BO'), ('ability', 'A0BP'), ('ability', 'A0C5'),
        ('ability', 'Amel'), ('ability', 'Amed'), ('ability', 'A0C7'), ('ability', 'A0C8'),
        ('ability', 'A0BT'), ('ability', 'A0BU'), ('ability', 'A1PV'), ('ability', 'A0C4'),
        ('ability', 'Arpl'), ('ability', 'Arpm'), ('ability', 'A0BX'), ('ability', 'unA5'),
        ('ability', 'A1PY'), ('ability', 'A0C0'), ('ability', 'A0C2'), ('ability', 'A1PX'),
        ('ability', 'unA0'), ('ability', 'Aspa'), ('ability', 'A1N8'), ('ability', 'Arst'),
        ('ability', 'Auns'), ('ability', 'Afra'), ('ability', 'A0BR'), ('ability', 'Agyd'),
        ('ability', 'Arlm'), ('ability', 'A0CA'), ('ability', 'A0CC'), ('ability', 'A1ND'),
        ('ability', 'A0CG'), ('ability', 'kel0'), ('ability', 'A1E7')
    ]
}

inventory = {}

for cat, items in objects_to_check.items():
    inventory[cat] = {}
    for otype, oid in items:
        res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', otype, '--id', oid])
        ov = res.get('overrides', {})
        fields = res.get('object', {}) or res.get('fields', {})
        
        # Collect relevant text fields
        f_map = {}
        # From overrides
        for k, v in ov.items():
            if any(tk in k.lower() for tk in ['name', 'tip', 'ubertip', 'propernames', 'hotkey']):
                sid = get_sid(v)
                f_map[k] = {
                    'raw': v,
                    'sid': sid,
                    'current_val': wts.get(sid, v) if sid else v
                }
        
        # Also check levels for abilities/upgrades if not all in overrides
        levels = int(fields.get('levels') or 1)
        for i in range(1, levels + 1):
            for prefix in ['tip', 'ubertip', 'name', 'hotkey']:
                k = f"{prefix}{i}"
                if k in fields and k not in f_map:
                    v = fields[k]
                    sid = get_sid(v)
                    if sid:
                        f_map[k] = {
                            'raw': v,
                            'sid': sid,
                            'current_val': wts.get(sid, v)
                        }
        
        inventory[cat][oid] = {
            'type': otype,
            'levels': levels,
            'hotkey': fields.get('hotkey'),
            'researchhotkey': fields.get('researchhotkey'),
            'fields': f_map,
            'trains': fields.get('train') or fields.get('trains'),
            'researches': fields.get('researches'),
            'upgrades_to': fields.get('upgrade') or fields.get('upgrades_to'),
            'upgrades': fields.get('upgrades'),
            'abils': fields.get('abillist'),
            'heroabils': fields.get('heroabillist'),
            'targs1': fields.get('targs1'),
            'targs2': fields.get('targs2')
        }

out_file = ROOT / "scripts/undead_complete_inventory.json"
out_file.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Inventory saved to {out_file}")

# Count total unique WTS strings across inventory
all_sids = set()
for cat, objs in inventory.items():
    for oid, oinfo in objs.items():
        for fld, finfo in oinfo['fields'].items():
            if finfo['sid']:
                all_sids.add(finfo['sid'])
print(f"Total unique WTS string IDs across all Undead objects: {len(all_sids)}")
