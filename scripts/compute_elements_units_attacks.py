import json, sys
from pathlib import Path

ROOT = Path('f:/Gemini_23Race')
sys.path.insert(0, str(ROOT / 'scripts'))
from wc3_object_tools import cli

unit_ids = [
    'e00F',
    'n07Y', 'n07X', 'n07W', 'n07Z',
    'n02R', 'n036', 'n02S', 'n07O', 'h0F1',
    'n02U', 'n07C', 'n02T', 'n07T', 'n032', 'n02Z',
    'n02Q', 'n02V', 'n07P', 'n07R', 'n02P',
    'n02W', 'n07V', 'n02X', 'n034', 'n07N', 'n035', 'n031', 'n07Q', 'n07S', 'n033', 'n02Y',
]

fields = 'name,weapson,targs1,rangen1,atktype1,weaptype1,targs2,rangen2,atktype2,weaptype2'
res = cli(['get-objects-bulk', '--type', 'unit', '--ids', ','.join(unit_ids), '--fields', fields])

attacks = {}
for obj in res.get('objects', []):
    f = obj['fields']
    weapson = f.get('weapson', '0')
    r1 = int(f.get('rangen1') or 100)
    t1 = f.get('targs1', '')
    a1 = f.get('atktype1', '')
    
    r2 = int(f.get('rangen2') or 100) if f.get('rangen2') else 0
    t2 = f.get('targs2', '')
    a2 = f.get('atktype2', '')
    
    has_ground = 'ground' in t1 or 'ground' in t2
    has_air = 'air' in t1 or 'air' in t2
    
    target_desc = ''
    if weapson == '0':
        target_desc = 'Не атакует'
    elif has_ground and has_air:
        target_desc = 'наземные и воздушные цели'
    elif has_ground:
        target_desc = 'наземные цели'
    elif has_air:
        target_desc = 'воздушные цели'
    else:
        target_desc = 'цели'
        
    range_type = 'дальний бой' if (r1 > 150 or r2 > 150) else 'ближний бой'
    
    # Damage type translation
    dmg_names = {
        'normal': 'обычный урон',
        'pierce': 'колющий урон',
        'siege': 'осадный урон',
        'magic': 'магический урон',
        'chaos': 'урон от хаоса',
        'hero': 'урон героя',
        'spells': 'заклинания',
    }
    dmg1 = dmg_names.get(a1, a1)
    dmg2 = dmg_names.get(a2, a2)
    
    if weapson == '3' and t2:
        dmg_str = f'{dmg1} / {dmg2}'
    else:
        dmg_str = dmg1
        
    attacks[obj['id']] = {
        'weapson': weapson,
        'target_desc': target_desc,
        'range_type': range_type,
        'damage_type': dmg_str,
        'r1': r1,
        't1': t1,
        'a1': a1,
        'r2': r2,
        't2': t2,
        'a2': a2,
    }

with open('docs/ui_text/elements_units_attacks.json', 'w', encoding='utf-8') as out:
    json.dump(attacks, out, ensure_ascii=False, indent=2)

print('Saved attack definitions to docs/ui_text/elements_units_attacks.json')
