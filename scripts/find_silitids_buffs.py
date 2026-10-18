# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
import inspect_race_base as ib

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

res = hw.run_cli_json(['list-objects', '--map', str(hw.DEFAULT_MAP), '--type', 'buff'])
buff_ids = res.get('objects', [])
print(f"Total buffs: {len(buff_ids)}")

matched = []
for bid in buff_ids:
    binfo = ib.inspect_buff(bid)
    ed = binfo.get('editorname') or ''
    bt = binfo.get('bufftip') or ''
    bub = binfo.get('buffubertip') or ''
    s = f"{ed} {bt} {bub}".lower()
    if any(k in s for k in ['силит', 'кираж', 'акир', 'к\'тун', 'антенн', 'улей', 'слизень', 'статуя', 'сфинкс', 'мутаци', 'москит', 'эмпати']):
        matched.append(binfo)

print(f"Matched {len(matched)} buffs:")
for m in matched:
    print(f"[{m['id']}] editor={m.get('editorname')} | tip={m.get('bufftip')} | ubertip={m.get('buffubertip')}")
