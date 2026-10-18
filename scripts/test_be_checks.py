import json
from pathlib import Path
import re
import sys
sys.path.insert(0, 'scripts')
import wc3_hivewe as hw

ROOT = Path('.')
plan_path = ROOT / 'docs/ui_text/blood_elves_plan.json'
plan_data = json.loads(plan_path.read_text(encoding='utf-8'))
wts_updates = {int(k): v for k, v in plan_data['wts_updates'].items()}

wts_path = hw.DEFAULT_MAP / 'war3map.wts'
wts_raw = wts_path.read_text(encoding='utf-8')
sim_wts = wts_raw
for sid, val in sorted(wts_updates.items()):
    pattern = rf'(STRING 0*{sid}\s*\{{\s*\r?\n)([\s\S]*?)(\r?\n\}})'
    sim_wts = re.sub(pattern, rf'\g<1>{val}\g<3>', sim_wts, count=1)

temp_wts = hw.load_wts_strings()
# update temp_wts with simulated updates
for sid, val in wts_updates.items():
    temp_wts[sid] = val

resolve = lambda s: temp_wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

obj_cache = {}
from collections import defaultdict
ids_by_type = defaultdict(set)
for c in plan_data['checks_def']:
    ids_by_type[c['type']].add(c['id'])

for ctype, ids in ids_by_type.items():
    id_list = sorted(list(ids))
    for i in range(0, len(id_list), 50):
        chunk = id_list[i:i+50]
        res = hw.run_cli_json(['get-objects-bulk', '--map', str(hw.DEFAULT_MAP), '--type', ctype, '--ids', ','.join(chunk)])
        if res.get('ok'):
            for item in res.get('objects', []):
                obj_cache[(ctype, item['id'])] = item.get('fields', {})

mismatches = []
for c in plan_data['checks_def']:
    fields = obj_cache.get((c['type'], c['id']), {})
    actual = resolve(fields.get(c['field']))
    expected = c.get('expected')
    if actual != expected:
        mismatches.append((c['type'], c['id'], c['field'], actual, expected))

print(f"Blood Elves checks total: {len(plan_data['checks_def'])}, mismatches: {len(mismatches)}")
if mismatches:
    for m in mismatches[:10]:
        print(m[0], m[1], m[2], 'ACTUAL:', repr(m[3])[:40], 'EXPECTED:', repr(m[4])[:40])
