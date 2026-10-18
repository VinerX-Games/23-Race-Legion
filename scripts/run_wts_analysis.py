# -*- coding: utf-8 -*-
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import wc3_hivewe as hw
wts = hw.load_wts_strings()

def parse_str_id(raw):
    if isinstance(raw, str) and raw.startswith('TRIGSTR_'):
        try:
            return int(raw[8:])
        except ValueError:
            return None
    return None

dump = json.loads((ROOT / 'scripts/hordew2_raw_dump.json').read_text(encoding='utf-8'))
out = []

out.append('=== SELECTION ===')
sel = dump.get('selection', {})
sid_name = parse_str_id(sel.get('raw_name'))
out.append(f'A1JN name: sid={sid_name} -> {repr(wts.get(sid_name))}')
for f in ['tips', 'ubertips']:
    val = sel.get(f, {})
    for k, v in val.items():
        sid = parse_str_id(v.get('raw'))
        out.append(f'A1JN {f}[{k}]: sid={sid} -> {repr(wts.get(sid))}')

out.append('\n=== MARKERS ===')
for m in dump.get('selection_markers', []):
    mid = m.get('id')
    for f in ['names', 'tips', 'ubertips']:
        val = m.get(f, {})
        for k, v in val.items():
            sid = parse_str_id(v.get('raw'))
            out.append(f'Marker {mid} {f}[{k}]: sid={sid} -> {repr(wts.get(sid))}')

out.append('\n=== BUILDINGS (13) ===')
for b in dump.get('buildings', []):
    bid = b.get('id')
    name_sid = parse_str_id(b.get('raw_name'))
    tip_sid = parse_str_id(b.get('raw_tip'))
    ub_sid = parse_str_id(b.get('raw_ubertip'))
    hk = b.get('hotkey')
    out.append(f'[{bid}] HK={hk} name_sid={name_sid} ({repr(wts.get(name_sid))}) tip_sid={tip_sid} ({repr(wts.get(tip_sid))}) ub_sid={ub_sid} ({repr(wts.get(ub_sid))[:60] if ub_sid else None})')

out.append('\n=== HEROES (4) ===')
for h in dump.get('heroes', []):
    hid = h.get('id')
    name_sid = parse_str_id(h.get('raw_name'))
    tip_sid = parse_str_id(h.get('raw_tip'))
    ub_sid = parse_str_id(h.get('raw_ubertip'))
    prop_sid = parse_str_id(h.get('raw_propernames'))
    awk_sid = parse_str_id(h.get('raw_awakentip'))
    rev_sid = parse_str_id(h.get('raw_revivetip'))
    hk = h.get('hotkey')
    out.append(f'[{hid}] HK={hk} name_sid={name_sid} ({repr(wts.get(name_sid))}) tip_sid={tip_sid} ({repr(wts.get(tip_sid))}) ub_sid={ub_sid} ({repr(wts.get(ub_sid))[:50] if ub_sid else None}) prop_sid={prop_sid} ({repr(wts.get(prop_sid))}) awk_sid={awk_sid} ({repr(wts.get(awk_sid))}) rev_sid={rev_sid} ({repr(wts.get(rev_sid))})')

out.append('\n=== UNITS (21) ===')
for u in dump.get('units', []):
    uid = u.get('id')
    name_sid = parse_str_id(u.get('raw_name'))
    tip_sid = parse_str_id(u.get('raw_tip'))
    ub_sid = parse_str_id(u.get('raw_ubertip'))
    hk = u.get('hotkey')
    out.append(f'[{uid}] HK={hk} name_sid={name_sid} ({repr(wts.get(name_sid))}) tip_sid={tip_sid} ({repr(wts.get(tip_sid))}) ub_sid={ub_sid} ({repr(wts.get(ub_sid))[:50] if ub_sid else None})')

out.append('\n=== UPGRADES (40) ===')
for up in dump.get('upgrades', []):
    upid = up.get('id')
    sids = []
    for f in ['names', 'tips', 'ubertips']:
        val = up.get(f, {})
        for k, v in val.items():
            sid = parse_str_id(v.get('raw'))
            if sid:
                sids.append((f, k, sid, repr(wts.get(sid))[:40]))
    if sids:
        out.append(f'[{upid}] levels={up.get("levels")} (sids: {len(sids)})')
        for s in sids:
            out.append(f'   {s[0]}[{s[1]}]: sid={s[2]} -> {s[3]}')

out.append('\n=== ABILITIES (86) ===')
for a in dump.get('abilities', []):
    aid = a.get('id')
    sids = []
    name_sid = parse_str_id(a.get('raw_name'))
    if name_sid:
        sids.append(('name', name_sid, repr(wts.get(name_sid))[:40]))
    res_tip_sid = parse_str_id(a.get('raw_researchtip'))
    if res_tip_sid:
        sids.append(('researchtip', res_tip_sid, repr(wts.get(res_tip_sid))[:40]))
    res_ub_sid = parse_str_id(a.get('raw_researchubertip'))
    if res_ub_sid:
        sids.append(('researchubertip', res_ub_sid, repr(wts.get(res_ub_sid))[:40]))
    for f in ['tips', 'ubertips']:
        val = a.get(f, {})
        for k, v in val.items():
            sid = parse_str_id(v.get('raw'))
            if sid:
                sids.append((f'{f}_{k}', sid, repr(wts.get(sid))[:40]))
    if sids:
        out.append(f'[{aid}] {a.get("name")} (levels: {a.get("levels")}) sids: {len(sids)}')
        for s in sids:
            out.append(f'   {s[0]}: sid={s[1]} -> {s[2]}')

(ROOT / 'scripts/hordew2_wts_analysis.txt').write_text('\n'.join(out), encoding='utf-8')
print('Successfully wrote scripts/hordew2_wts_analysis.txt')
