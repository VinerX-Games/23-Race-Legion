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

fields = 'name,weapson,atktype1,targtype1,rangeN1,cool1,mindmg1,maxdmg1,atktype2,targtype2,rangeN2,cool2,mindmg2,maxdmg2,spd,hp,mana0,def,deftype,abillist'
res = cli(['get-objects-bulk', '--type', 'unit', '--ids', ','.join(unit_ids), '--fields', fields])

combat_info = {}
for obj in res.get('objects', []):
    f = obj['fields']
    combat_info[obj['id']] = f

with open('docs/ui_text/elements_units_combat.json', 'w', encoding='utf-8') as out:
    json.dump(combat_info, out, ensure_ascii=False, indent=2)

print('Saved combat info for 32 units to docs/ui_text/elements_units_combat.json')
