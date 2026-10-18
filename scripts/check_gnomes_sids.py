# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
dump_file = ROOT / "scripts/gnomes_raw_dump.json"
d = json.loads(dump_file.read_text(encoding="utf-8"))

def check_obj(category, obj_list, name_attr='name'):
    print(f"=== {category.upper()} ({len(obj_list)}) ===")
    for o in obj_list:
        oid = o['id']
        name = o.get(name_attr)
        raw_name = o.get('raw_name')
        raw_tip = o.get('raw_tip')
        raw_ub = o.get('raw_ubertip')
        print(f"[{oid}] raw_name={raw_name} raw_tip={raw_tip} raw_ub={raw_ub}")

check_obj("Buildings", d['buildings'])
check_obj("Workers", d['workers'])
check_obj("Units", d['units'])
check_obj("Heroes", d['heroes'])
