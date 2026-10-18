# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

d = json.load(open(ROOT / "scripts/nightborne_raw_dump.json", encoding="utf-8"))

for k in ['buildings', 'units', 'heroes']:
    print(f"\n=== {k.upper()} ===")
    for obj in d[k]:
        print(f"{obj['id']} ({obj['name']}):")
        print(f"  tip: {obj.get('tip')}")
        print(f"  ubertip: {obj.get('ubertip')}")
        print(f"  hotkey: {obj.get('hotkey')}")
        print(f"  trains: {obj.get('trains')}")
        print(f"  researches: {obj.get('researches')}")
        print(f"  upgrades_to: {obj.get('upgrades_to')}")
        print(f"  abils: {obj.get('abils')}")
        print(f"  heroabils: {obj.get('heroabils')}")
        print(f"  upgrades: {obj.get('upgrades')}")
        print(f"  targs1: {obj.get('targs1')}, targs2: {obj.get('targs2')}")
