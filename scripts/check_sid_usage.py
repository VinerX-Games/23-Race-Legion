# -*- coding: utf-8 -*-
"""Check usage of Nightborne string IDs across all map objects."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()

# Let's inspect all units, abilities, upgrades, buffs in the map to find where TRIGSTR_... are used
# We can read the raw w3u, w3a, w3q, etc. or use HiveWE
