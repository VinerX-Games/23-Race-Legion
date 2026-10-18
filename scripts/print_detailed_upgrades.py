import json
from pathlib import Path

data = json.loads(Path('docs/ui_text/ice_troll_upgrades_detailed.json').read_text(encoding='utf-8'))

for qid, obj in data.items():
    print("=" * 60)
    print(f"Upgrade {qid} (code={obj['code']}, hotkey='{obj['hotkey']}')")
    for lvl in obj['levels']:
        l = lvl['level']
        name = lvl['name']
        tip = lvl['tip']
        ub = lvl['ubertip']
        eff = lvl['effects']
        gold = lvl['gold']
        lumb = lvl['lumb']
        time = lvl['time']
        req = lvl['req']
        # only print if there's meaningful data or level <= 3
        if name or tip or ub or (gold and int(gold) > 0):
            print(f"  Level {l}:")
            print(f"    name='{name}', tip='{tip}'")
            print(f"    ub='{ub}'")
            print(f"    effects: {eff}")
            print(f"    cost: gold={gold}, lumb={lumb}, time={time}, req='{req}'")
