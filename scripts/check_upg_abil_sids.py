# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

print("=== UPGRADES WTS STRINGS ===")
for u in d['upgrades']:
    uid = u['id']
    lvls = u['levels']
    names_sids = [u['names'][f'name{i}']['sid'] for i in range(1, lvls+1) if f'name{i}' in u['names']]
    tips_sids = [u['tips'][f'tip{i}']['sid'] for i in range(1, lvls+1) if f'tip{i}' in u['tips']]
    ubs_sids = [u['ubertips'][f'ubertip{i}']['sid'] for i in range(1, lvls+1) if f'ubertip{i}' in u['ubertips']]
    print(f"[{uid}] lvls={lvls} names={names_sids} tips={tips_sids} ubs={ubs_sids}")

print("\n=== ABILITIES WTS STRINGS ===")
for a in d['abilities']:
    aid = a['id']
    lvls = a['levels']
    nsid = a.get('name_sid')
    rtip_sid = a.get('researchtip_sid')
    rub_sid = a.get('researchubertip_sid')
    tips_sids = [a['tips'][f'tip{i}']['sid'] for i in range(1, lvls+1) if f'tip{i}' in a['tips']]
    ubs_sids = [a['ubertips'][f'ubertip{i}']['sid'] for i in range(1, lvls+1) if f'ubertip{i}' in a['ubertips']]
    print(f"[{aid}] lvls={lvls} name={nsid} rtip={rtip_sid} rub={rub_sid} tips={tips_sids} ubs={ubs_sids}")
