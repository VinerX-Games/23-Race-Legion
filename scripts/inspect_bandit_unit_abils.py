# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

unit_abils = [
    'A0I3', 'A00M', 'ANha', 'Ahrp', 'A000', 'A00L', 'A01A', 'A00P', 'A01B',
    'A013', 'A00J', 'A00N', 'A016', 'A017', 'A169', 'A00X', 'A00V',
    'A00K', 'A165', 'A00R', 'A19T', 'A00U', 'Aspo', 'A00S', 'A00T',
    'A012', 'A00Z', 'A00Y', 'ACbh', 'Ashm', 'A17Q', 'A011', 'A010', 'Abof',
    'Afbt'
]

print(f"Inspecting {len(unit_abils)} abilities...")
for aid in unit_abils:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'ability', '--id', aid])
    f = res.get('object', {}) or res.get('fields', {})
    name = resolve(f.get('name'))
    raw_name = f.get('name')
    tip1 = resolve(f.get('tip1'))
    raw_tip1 = f.get('tip1')
    ubertip1 = resolve(f.get('ubertip1'))
    raw_ubertip1 = f.get('ubertip1')
    hotkey = resolve(f.get('hotkey'))
    print(f"{aid}: {name} (raw={raw_name}) | hotkey={hotkey}")
    print(f"   tip1: {tip1} (raw={raw_tip1})")
    print(f"   ubertip1: {ubertip1} (raw={raw_ubertip1})")
