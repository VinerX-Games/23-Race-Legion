# -*- coding: utf-8 -*-
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys_dump = json.loads((ROOT / 'scripts/ogres_raw_dump.json').read_text(encoding='utf-8'))

from analyze_ogres_wts import with_wts
ogres_sids = set(v[0] for v in with_wts.values())
print(f"Total Ogres SIDs: {len(ogres_sids)}")

# Let's check other races' plan files to see if there is any overlap
plan_files = list((ROOT / 'docs/ui_text').glob('*_plan.json'))
overlaps = {}
for pf in plan_files:
    if 'ogres' in pf.name: continue
    pdata = json.loads(pf.read_text(encoding='utf-8'))
    wts_up = {int(k) for k in pdata.get('wts_updates', {}).keys()}
    common = ogres_sids.intersection(wts_up)
    if common:
        overlaps[pf.name] = sorted(list(common))

print(f"Overlaps with other race plans: {overlaps}")
