# -*- coding: utf-8 -*-
import json
from pathlib import Path

dump = json.loads(Path('scripts/jungletrolls_raw_dump.json').read_text(encoding='utf-8'))

with open('scripts/jt_sids_summary.txt', 'w', encoding='utf-8') as out:
    out.write("=== SELECTION ===\n")
    sel = dump['selection']
    out.write(f"Selection A1DZ: name_sid={sel.get('name_sid')}, tip_sid={sel['tips']['tip1']['sid']}, ub_sid={sel['ubertips']['ubertip1']['sid']}, hk={sel.get('hotkey')}\n")
    for m in dump['selection_markers']:
        out.write(f"Marker {m['id']}: name_sid={m['names']['name1']['sid']}, tip_sid={m['tips']['tip1']['sid']}, ub_sid={m['ubertips']['ubertip1']['sid']}\n")

    out.write("\n=== BUILDINGS ===\n")
    for b in dump['buildings']:
        out.write(f"{b['id']} ({b['name']}): name_sid={b.get('name_sid')}, tip_sid={b.get('tip_sid')}, ub_sid={b.get('ubertip_sid')}, hk={b.get('hotkey')}\n")

    out.write("\n=== UNITS ===\n")
    for u in dump['units']:
        out.write(f"{u['id']} ({u['name']}): name_sid={u.get('name_sid')}, tip_sid={u.get('tip_sid')}, ub_sid={u.get('ubertip_sid')}, hk={u.get('hotkey')}\n")

    out.write("\n=== HEROES ===\n")
    for h in dump['heroes']:
        out.write(f"{h['id']} ({h['name']}): name_sid={h.get('name_sid')}, proper={h.get('propernames')}, proper_sid={h.get('fields', {}).get('propernames')}, tip_sid={h.get('tip_sid')}, ub_sid={h.get('ubertip_sid')}, hk={h.get('hotkey')}\n")

    out.write("\n=== UPGRADES ===\n")
    for up in dump['upgrades']:
        out.write(f"{up['id']} ({up['levels']} lvls):\n")
        for l in range(1, up['levels']+1):
            out.write(f"  L{l}: name_sid={up['names'][f'name{l}']['sid']}, tip_sid={up['tips'][f'tip{l}']['sid']}, ub_sid={up['ubertips'][f'ubertip{l}']['sid']}, hk={up['hotkeys'][f'hotkey{l}']['val']}\n")
