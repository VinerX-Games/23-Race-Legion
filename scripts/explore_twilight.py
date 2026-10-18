# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

bld_ids = ['o00K', 'o00T', 'o00L', 'o00R', 'o00V', 'o00P', 'o00U', 'o00Q', 'h0D3']
for bid in bld_ids:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'unit', '--id', bid, '--all'])
    f = data.get('fields', {})
    name = resolve(f.get('name'))
    trains = f.get('trains')
    res = f.get('researches')
    upg = f.get('upgrade')
    sellu = f.get('sellunits')
    selli = f.get('sellitems')
    print(f"{bid}: name={name} | trains={trains} | res={res} | upg={upg} | sellu={sellu} | selli={selli}")
