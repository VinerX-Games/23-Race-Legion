# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent

inv = json.loads((ROOT / "scripts/scarlet_complete_inventory.json").read_text(encoding="utf-8"))

active_sids = {}

def record(sid, obj_type, obj_id, field, val):
    if not sid: return
    try:
        sid = int(sid)
    except (ValueError, TypeError):
        return
    if sid not in active_sids:
        active_sids[sid] = []
    active_sids[sid].append({"type": obj_type, "id": obj_id, "field": field, "val": val})

# 1. Selection
sel = inv['selection']
for f in ['name', 'tip1', 'ubertip1']:
    record(sel[f]['sid'], "ability", "A0HM", f, sel[f]['val'])

# 2. Buildings
for bid, b in inv['buildings'].items():
    for f in ['name', 'tip', 'ubertip']:
        record(b[f]['sid'], "building", bid, f, b[f]['val'])

# 3. Heroes
for hid, h in inv['heroes'].items():
    for f in ['name', 'tip', 'ubertip', 'propernames']:
        record(h[f]['sid'], "hero", hid, f, h[f]['val'])

# 4. Units
for uid, u in inv['units'].items():
    for f in ['name', 'tip', 'ubertip']:
        record(u[f]['sid'], "unit", uid, f, u[f]['val'])

# 5. Hero abils
hero_abils_levels = {
    'A097': 4, 'A09C': 4, 'A09E': 2, 'A09D': 4,
    'A09K': 4, 'A09L': 4, 'A09N': 4, 'A09M': 2,
    'A09G': 4, 'A09F': 4, 'A09I': 4, 'A09J': 2
}
for aid, max_lvl in hero_abils_levels.items():
    a = inv['abilities'][aid]
    f = a['fields']
    record(a['name']['sid'], "ability", aid, "name", a['name']['val'])
    # research
    rt = f.get('researchtip')
    if rt and rt.startswith('TRIGSTR_'): record(int(rt[8:]), "ability", aid, "researchtip", "")
    ru = f.get('researchubertip')
    if ru and ru.startswith('TRIGSTR_'): record(int(ru[8:]), "ability", aid, "researchubertip", "")
    for lvl in range(1, max_lvl + 1):
        t = a['tips'].get(str(lvl))
        u = a['ubertips'].get(str(lvl))
        ut = a['untips'].get(str(lvl))
        uu = a['unubertips'].get(str(lvl))
        if t and t['sid']: record(t['sid'], "ability", aid, f"tip{lvl}", t['val'])
        if u and u['sid']: record(u['sid'], "ability", aid, f"ubertip{lvl}", u['val'])
        if ut and ut['sid']: record(ut['sid'], "ability", aid, f"untip{lvl}", ut['val'])
        if uu and uu['sid']: record(uu['sid'], "ability", aid, f"unubertip{lvl}", uu['val'])

# 6. Unit abils (each 1 level)
for aid, a in inv['abilities'].items():
    if aid in hero_abils_levels: continue
    record(a['name']['sid'], "ability", aid, "name", a['name']['val'])
    t = a['tips'].get('1')
    u = a['ubertips'].get('1')
    ut = a['untips'].get('1')
    uu = a['unubertips'].get('1')
    if t and t['sid']: record(t['sid'], "ability", aid, "tip1", t['val'])
    if u and u['sid']: record(u['sid'], "ability", aid, "ubertip1", u['val'])
    if ut and ut['sid']: record(ut['sid'], "ability", aid, "untip1", ut['val'])
    if uu and uu['sid']: record(uu['sid'], "ability", aid, "unubertip1", uu['val'])

# 7. Buffs
from implement_draenei_rework import object_records
w3h_skin_bytes = (ROOT / 'map.w3x/war3mapSkin.w3h').read_bytes()
header, tables = object_records(w3h_skin_bytes, False)
buff_ids = ['B01K', 'B01L', 'B01M', 'B01N', 'B01P', 'B01R', 'B01W', 'B01X', 'B01Y', 'B01Z', 'B020', 'B021', 'B022']
for table in tables:
    for obj in table:
        oid = obj['id']
        if oid in buff_ids:
            for mod_key, raw_bytes in obj['mods']:
                tag = mod_key[0]
                val_bytes = raw_bytes[8:]
                try:
                    val_str = val_bytes.split(b'\x00')[0].decode('utf-8', errors='ignore')
                    if val_str.startswith('TRIGSTR_'):
                        record(int(val_str[8:]), "buff", oid, tag, "")
                except Exception:
                    pass

# 8. Upgrades
upgrades_levels = {
    'R03K': 1, 'R03L': 1, 'R03M': 2, 'R03S': 2, 'R03T': 2, 'R03U': 1, 'R03V': 2,
    'R03W': 1, 'R03X': 3, 'R03Y': 3, 'R03Z': 1, 'R040': 1, 'R041': 3, 'R042': 3,
    'R043': 1, 'R044': 2, 'R045': 1, 'R046': 1, 'R047': 1, 'R048': 1, 'R049': 6,
    'R04A': 6, 'R04B': 6, 'R04C': 6, 'R07B': 1, 'R0KG': 3, 'R0KH': 6
}
for upg, max_lvl in upgrades_levels.items():
    u = inv['upgrades'][upg]
    record(u['name']['sid'], "upgrade", upg, "name", u['name']['val'])
    for lvl in range(1, max_lvl + 1):
        n = u['names'].get(str(lvl))
        t = u['tips'].get(str(lvl))
        ub = u['ubertips'].get(str(lvl))
        if n and n['sid']: record(n['sid'], "upgrade", upg, f"name{lvl}", n['val'])
        if t and t['sid']: record(t['sid'], "upgrade", upg, f"tip{lvl}", t['val'])
        if ub and ub['sid']: record(ub['sid'], "upgrade", upg, f"ubertip{lvl}", ub['val'])

print(f"Total active distinct WTS strings for Scarlet: {len(active_sids)}")
