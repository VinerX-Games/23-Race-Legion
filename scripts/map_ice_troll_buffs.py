import json
from pathlib import Path

raw_hero = json.loads(Path('docs/ui_text/ice_troll_hero_abilities_raw.json').read_text(encoding='utf-8'))
raw_unit = json.loads(Path('docs/ui_text/ice_troll_unit_abilities_raw.json').read_text(encoding='utf-8'))

buff_map = {}
for h in raw_hero:
    for k, v in h['fields'].items():
        if k.startswith('abuf') or k.startswith('buff'):
            for b in str(v).split(','):
                b = b.strip()
                if b and b not in ('-', '0'):
                    buff_map.setdefault(b, []).append(f"Hero {h['id']} ({h['name']})")

for u in raw_unit:
    for k, v in u['fields'].items():
        if k.startswith('abuf') or k.startswith('buff'):
            for b in str(v).split(','):
                b = b.strip()
                if b and b not in ('-', '0'):
                    buff_map.setdefault(b, []).append(f"Unit {u['id']} ({u['name']})")

for b, sources in sorted(buff_map.items()):
    print(f"Buff {b}: {sources}")
