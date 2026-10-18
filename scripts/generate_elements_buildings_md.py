import json

with open('docs/ui_text/elements_buildings_audit.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

lines = []
lines.append('# Аудит зданий Элементалей (Elements)\n')
for b_id, d in audit.items():
    name = d.get('name_resolved', '')
    lines.append(f"## [{b_id}] {name}")
    lines.append(f"- **Raw Name**: `{d.get('name_raw')}` -> `{d.get('name_resolved')}`")
    lines.append(f"- **Raw Tip**: `{d.get('tip_raw')}` -> `{d.get('tip_resolved')}`")
    lines.append(f"- **Raw Ubertip**: `{d.get('ubertip_raw')}` -> `{d.get('ubertip_resolved')}`")
    lines.append(f"- **Hotkey**: `{d.get('hotkey_raw')}` -> `{d.get('hotkey_resolved')}`")
    lines.append(f"- **Trains**: `{d.get('trains')}`")
    lines.append(f"- **Researches**: `{d.get('researches')}`")
    lines.append(f"- **Upgrades To**: `{d.get('upgrades_to')}`")
    lines.append(f"- **Abilities**: `{d.get('abilities')}`")
    lines.append(f"- **Cost**: Gold {d.get('goldcost')}, Wood {d.get('lumbercost')}, Time {d.get('bldtm')}s")
    lines.append(f"- **Food**: `{d.get('fmade')}`")
    lines.append(f"- **Attack**: `{d.get('atktype1')}`, target: `{d.get('targtype1')}`")
    lines.append('')

with open('docs/ui_text/elements_buildings_audit.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Saved docs/ui_text/elements_buildings_audit.md')
