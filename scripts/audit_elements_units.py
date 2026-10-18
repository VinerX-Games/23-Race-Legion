import sys, json, re, subprocess
sys.path.insert(0, 'scripts')
from wc3_project import settings

s = settings()
cli = s['cli']
map_path = s['map']

all_units = [
    # Worker
    'e00F',
    # T3 Specials (h0ES)
    'n07Y', 'n07X', 'n07W', 'n07Z',
    # Fire (h0EO)
    'n02R', 'n036', 'n02S', 'n07O', 'h0F1',
    # Water (h0ET)
    'n02U', 'n07C', 'n02T', 'n07T', 'n032', 'n02Z',
    # Air (h0EU)
    'n02Q', 'n02V', 'n07P', 'n07R', 'n02P',
    # Earth (h0EW)
    'n02W', 'n07V', 'n02X', 'n034', 'n07N', 'n035', 'n031', 'n07Q', 'n07S', 'n033', 'n02Y',
    # Other candidates (summons or alternate heroes)
    'E027', 'E028', 'E029', 'n00E',
    # Heroes (h0EY)
    'H0EZ', 'H0F0', 'N037'
]

cmd_sd = [cli, 'get-objects-bulk', '--map', map_path, '--type', 'unit', '--ids', ','.join(all_units)]
res_sd = subprocess.run(cmd_sd, capture_output=True, text=True, encoding='utf-8')
data_sd = json.loads(res_sd.stdout)
objects_sd = {item['id']: item for item in data_sd.get('objects', [])}

cmd_hd = [cli, 'get-objects-bulk', '--map', map_path, '--type', 'unit', '--ids', ','.join(all_units), '--graphics', 'hd']
res_hd = subprocess.run(cmd_hd, capture_output=True, text=True, encoding='utf-8')
data_hd = json.loads(res_hd.stdout)
objects_hd = {item['id']: item for item in data_hd.get('objects', [])}

wts = {}
with open('map.w3x/war3map.wts', 'r', encoding='utf-8') as f:
    blocks = re.findall(r'STRING\s+(\d+)\s*\{\s*(.*?)\s*\}', f.read(), re.DOTALL)
    for num, val in blocks:
        wts[f'TRIGSTR_{num}'] = val

def resolve(val):
    if isinstance(val, str) and val in wts:
        return wts[val]
    return val

audit = {}
for u_id in all_units:
    item_sd = objects_sd.get(u_id, {})
    item_hd = objects_hd.get(u_id, {})
    f_sd = item_sd.get('fields', {})
    f_hd = item_hd.get('fields', {})

    audit[u_id] = {
        'id': u_id,
        'name_raw': f_sd.get('name'),
        'name_resolved': resolve(f_sd.get('name')),
        'tip_raw': f_sd.get('tip'),
        'tip_resolved': resolve(f_sd.get('tip')),
        'ubertip_raw': f_sd.get('ubertip'),
        'ubertip_resolved': resolve(f_sd.get('ubertip')),
        'hotkey_raw': f_sd.get('hotkey'),
        'hotkey_resolved': resolve(f_sd.get('hotkey')),
        'propernames_raw': f_sd.get('propernames'),
        'propernames_resolved': resolve(f_sd.get('propernames')),
        'revivetip_raw': f_sd.get('revivetip'),
        'awakentip_raw': f_sd.get('awakentip'),
        'abilities': f_sd.get('abillist', f_sd.get('abilskinlist', '')),
        'upgrades': f_sd.get('upgrades', ''),
        'goldcost': f_sd.get('goldcost'),
        'lumbercost': f_sd.get('lumbercost'),
        'bldtm': f_sd.get('bldtm'),
        'fused': f_sd.get('fused'),
        'atktype1': f_sd.get('atktype1'),
        'targtype1': f_sd.get('targtype1'),
        'weaptype1': f_sd.get('weaptype1'),
        'atktype2': f_sd.get('atktype2'),
        'targtype2': f_sd.get('targtype2'),
        'weaptype2': f_sd.get('weaptype2'),
        'def': f_sd.get('def'),
        'deftype': f_sd.get('deftype'),
        'hp': f_sd.get('hp'),
        'mana0': f_sd.get('mana0'),
        'isbldg': f_sd.get('isbldg'),
        'editorsuffix': resolve(f_sd.get('editorsuffix')),
    }

with open('docs/ui_text/elements_units_audit.json', 'w', encoding='utf-8') as out:
    json.dump(audit, out, ensure_ascii=False, indent=2)

print('Saved audit for all units to docs/ui_text/elements_units_audit.json')
