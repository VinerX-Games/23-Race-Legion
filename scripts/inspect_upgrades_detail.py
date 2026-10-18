# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_upgrade

for uid in ['R0GF', 'R0GG', 'R0GH', 'R0GI', 'R0GJ', 'R0GK', 'R09W', 'R0GO', 'R0GP', 'R0GL', 'R0GM', 'R0GN', 'R0GQ', 'R0GR', 'R0GS', 'R0GT', 'R0GU', 'R0L2', 'R0HT']:
    u = inspect_upgrade(uid)
    print(f"=== Upgrade {uid} (lvls={u['levels']}) ===")
    for lvl in range(1, u['levels'] + 1):
        print(f"  L{lvl}: name={u['names'].get(f'name{lvl}')} hk={u['hotkeys'].get(f'hotkey{lvl}')}")
        print(f"       tip={u['tips'].get(f'tip{lvl}')}")
        print(f"       ub={u['ubertips'].get(f'ubertip{lvl}')}")
