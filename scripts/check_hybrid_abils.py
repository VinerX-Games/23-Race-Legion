# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_ability

for aid in ['ANab', 'AHfs', 'A0TG', 'A0XF']:
    ab = inspect_ability(aid)
    print(f"=== {aid} ===")
    print("overrides:", ab['overrides'])
