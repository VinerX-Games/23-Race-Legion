import json, re, sys
from pathlib import Path

ROOT = Path('f:/Gemini_23Race')
sys.path.insert(0, str(ROOT / 'scripts'))
from wc3_object_tools import cli

with open('docs/ui_text/elements_heroes_raw.json', 'r', encoding='utf-8') as f:
    heroes = json.load(f)

# Collect all abilities
all_abils = set()
for h in heroes:
    fld = h.get('fields', {})
    for a_str in [fld.get('abillist', ''), fld.get('heroabillist', '')]:
        for ab in a_str.split(','):
            ab = ab.strip()
            if ab and len(ab) == 4:
                all_abils.add(ab)

# Bulk query abilities
res_a = cli(['get-objects-bulk', '--type', 'ability', '--ids', ','.join(sorted(list(all_abils))), '--fields', 'name,tip,ubertip,editorsuffix'])

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
for obj in res_a.get('objects', []):
    raw_name = obj['fields'].get('name', '')
    res_name = resolve(raw_name)
    suffix = resolve(obj['fields'].get('editorsuffix', ''))
    resolved_abils[obj['id']] = f'{res_name} {suffix}'.strip()

lines = []
lines.append('# Аудит героев Элементалей (Elements)\n')
for h in heroes:
    fld = h.get('fields', {})
    hid = h['id']
    name = resolve(fld.get('name', ''))
    lines.append(f"## [{hid}] {name}")
    lines.append(f"- **Name Raw**: `{fld.get('name')}` -> `{name}`")
    lines.append(f"- **Propernames Raw**: `{fld.get('propernames')}` -> `{resolve(fld.get('propernames'))}`")
    lines.append(f"- **Tip Raw**: `{fld.get('tip')}` -> `{resolve(fld.get('tip'))}`")
    lines.append(f"- **Ubertip Raw**: `{fld.get('ubertip')}` -> `{resolve(fld.get('ubertip'))}`")
    lines.append(f"- **Hotkey**: `{fld.get('hotkey')}` -> `{resolve(fld.get('hotkey'))}`")
    lines.append(f"- **Revivetip**: `{fld.get('revivetip')}` -> `{resolve(fld.get('revivetip'))}`")
    lines.append(f"- **Awakentip**: `{fld.get('awakentip')}` -> `{resolve(fld.get('awakentip'))}`")
    lines.append(f"- **Primary Stat**: `{fld.get('primary')}` (STR {fld.get('str')}, AGI {fld.get('agi')}, INT {fld.get('int')})")
    lines.append(f"- **HP/Mana**: {fld.get('hp')} / {fld.get('mana0')}, Armor: {fld.get('def')} ({fld.get('deftype')})")
    lines.append(f"- **Attack 1**: type={fld.get('atktype1')}, targ={fld.get('targs1')}, range={fld.get('rangen1')}, weap={fld.get('weaptype1')}")
    lines.append(f"- **Attack 2**: type={fld.get('atktype2')}, targ={fld.get('targs2')}, range={fld.get('rangen2')}, weap={fld.get('weaptype2')}")
    
    hero_abils = [f"`{ab}` ({resolved_abils.get(ab, ab)})" for ab in fld.get('heroabillist', '').split(',') if ab.strip()]
    norm_abils = [f"`{ab}` ({resolved_abils.get(ab, ab)})" for ab in fld.get('abillist', '').split(',') if ab.strip()]
    lines.append(f"- **Hero Abilities**: {', '.join(hero_abils) if hero_abils else 'нет'}")
    lines.append(f"- **Normal Abilities**: {', '.join(norm_abils) if norm_abils else 'нет'}")
    lines.append('')

with open('docs/ui_text/elements_heroes_audit.md', 'w', encoding='utf-8') as out:
    out.write('\n'.join(lines))

print('Saved docs/ui_text/elements_heroes_audit.md')
