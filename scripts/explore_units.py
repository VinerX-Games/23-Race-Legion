# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

unit_ids = ['n00D', 'n00C', 'o00O', 'n00S', 'u005', 'h0G8', 'h07A']
for uid in unit_ids:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', uid, '--all'])
    f = data.get('fields', {})
    name = resolve(f.get('name'))
    suffix = resolve(f.get('editorsuffix'))
    bld = f.get('isbldg')
    print(f"{uid}: name={name} | suffix={suffix} | isbldg={bld} | trains={f.get('trains')} | res={f.get('researches')} | abils={f.get('abillist')} | upg={f.get('upgrades')}")
