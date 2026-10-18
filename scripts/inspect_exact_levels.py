# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

hero_abils = ['A097', 'A09C', 'A09E', 'A09D', 'A09K', 'A09L', 'A09N', 'A09M', 'A09G', 'A09F', 'A09I', 'A09J']
unit_abils = [
    'A07I', 'A07X', 'A07Y', 'A07Z', 'A080', 'A081', 'A082', 'A083', 'A084',
    'A085', 'A087', 'A088', 'A089', 'A08A', 'A08B', 'A08C', 'A08D', 'A08E',
    'A08F', 'A08G', 'A08J', 'A08K', 'A08L', 'A08M', 'A08N', 'A08O', 'A08P',
    'A08X', 'A08Y', 'A09O'
]
upgrades = [
    'R03K', 'R03L', 'R03M', 'R03S', 'R03T', 'R03U', 'R03V', 'R03W', 'R03X',
    'R03Y', 'R03Z', 'R040', 'R041', 'R042', 'R043', 'R044', 'R045', 'R046',
    'R047', 'R048', 'R049', 'R04A', 'R04B', 'R04C', 'R07B', 'R0KG', 'R0KH'
]

print("=== ABILITIES LEVELS ===")
for aid in hero_abils + unit_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    print(f"{aid}: levels = {f.get('levels')}")

print("\n=== UPGRADES LEVELS ===")
for upg in upgrades:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', upg])
    f = res.get('object', {}) or res.get('fields', {})
    # check maxlevel or levels or stats
    print(f"{upg}: levels = {f.get('levels') or f.get('maxlevel')}")
