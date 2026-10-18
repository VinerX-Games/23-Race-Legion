import json, re, subprocess, sys
from pathlib import Path

ROOT = Path('f:/Gemini_23Race')
sys.path.insert(0, str(ROOT / 'scripts'))
from wc3_project import settings

s = settings()
cli = s['cli']
map_path = s['map']

unit_ids = [
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
]

with open('docs/ui_text/elements_units_audit.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

# Find all abilities and upgrades used by these units
all_abils = set()
for uid in unit_ids:
    d = audit.get(uid, {})
    for ab in d.get('abilities', '').split(','):
        ab = ab.strip()
        if ab and len(ab) == 4 and ab not in ('AInv', 'Ault'):
            all_abils.add(ab)

# Bulk query abilities
cmd_a = [cli, 'get-objects-bulk', '--map', map_path, '--type', 'ability', '--ids', ','.join(sorted(list(all_abils))), '--fields', 'name,tip,ubertip,editorsuffix']
res_a = subprocess.run(cmd_a, capture_output=True, text=True, encoding='utf-8')
data_a = json.loads(res_a.stdout)

wts = {}
with open('map.w3x/war3map.wts', 'r', encoding='utf-8') as f:
    blocks = re.findall(r'STRING\s+(\d+)\s*\{\s*(.*?)\s*\}', f.read(), re.DOTALL)
    for num, val in blocks:
        wts[f'TRIGSTR_{num}'] = val

def resolve(val):
    if isinstance(val, str) and val in wts:
        return wts[val]
    return val

resolved_abils = {}
for obj in data_a.get('objects', []):
    raw_name = obj['fields'].get('name', '')
    res_name = resolve(raw_name)
    suffix = resolve(obj['fields'].get('editorsuffix', ''))
    resolved_abils[obj['id']] = f'{res_name} {suffix}'.strip()

lines = []
lines.append('# Аудит 32 юнитов Элементалей (Elements)\n')
for uid in unit_ids:
    d = audit.get(uid, {})
    name = d.get('name_resolved', '')
    lines.append(f"## [{uid}] {name}")
    lines.append(f"- **Name Raw**: `{d.get('name_raw')}` -> `{d.get('name_resolved')}`")
    lines.append(f"- **Tip Raw**: `{d.get('tip_raw')}` -> `{d.get('tip_resolved')}`")
    lines.append(f"- **Ubertip Raw**: `{d.get('ubertip_raw')}` -> `{d.get('ubertip_resolved')}`")
    lines.append(f"- **Hotkey**: `{d.get('hotkey_raw')}` -> `{d.get('hotkey_resolved')}`")
    lines.append(f"- **Cost**: Gold {d.get('goldcost')}, Wood {d.get('lumbercost')}, Time {d.get('bldtm')}s, Food {d.get('fused')}")
    lines.append(f"- **HP/Mana**: {d.get('hp')} / {d.get('mana0')}, Armor: {d.get('def')} ({d.get('deftype')})")
    lines.append(f"- **Attack 1**: type={d.get('atktype1')}, targ={d.get('targtype1')}, weap={d.get('weaptype1')}")
    lines.append(f"- **Attack 2**: type={d.get('atktype2')}, targ={d.get('targtype2')}, weap={d.get('weaptype2')}")
    
    abils = [f"`{ab}` ({resolved_abils.get(ab, ab)})" for ab in d.get('abilities', '').split(',') if ab.strip()]
    lines.append(f"- **Abilities**: {', '.join(abils) if abils else 'нет'}")
    lines.append(f"- **Upgrades**: `{d.get('upgrades')}`")
    lines.append('')

with open('docs/ui_text/elements_units_audit.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Saved docs/ui_text/elements_units_audit.md')
