import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
upgrades = hw.run_cli_json(['get-objects', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--warcraft', str(hw.DEFAULT_WARCRAFT)])
# wait, get-objects didn't work for HiveWE earlier.
# Let's inspect war3map.w3q with implement_draenei_rework
from implement_draenei_rework import object_records

raw = open('map.w3x/war3map.w3q', 'rb').read()
v, tables = object_records(raw, True)
for t in tables:
    for r in t:
        text = str(r['mods'])
        if 'A1OV' in text:
            print(f"Found A1OV in upgrade: {r['id']}")
            for k, m in r['mods']:
                print(f"  {k}: {m}")
