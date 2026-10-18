import sys, json, re, subprocess
sys.path.insert(0, 'scripts')
from wc3_project import settings

s = settings()
cli = s['cli']
map_path = s['map']

with open('docs/ui_text/elements_buildings_audit.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

# Collect all trains and researches
all_units = set()
all_res = set()
for b_id, d in audit.items():
    for u in d.get('trains', '').split(','):
        u = u.strip()
        if u:
            for sub in u.split('.'):
                if len(sub) == 4:
                    all_units.add(sub)
    for r in d.get('researches', '').split(','):
        r = r.strip()
        if r and len(r) == 4:
            all_res.add(r)

# Bulk query units
cmd_u = [cli, 'get-objects-bulk', '--map', map_path, '--type', 'unit', '--ids', ','.join(sorted(list(all_units))), '--fields', 'name,editorsuffix']
res_u = subprocess.run(cmd_u, capture_output=True, text=True, encoding='utf-8')
data_u = json.loads(res_u.stdout)

# Bulk query researches
cmd_r = [cli, 'get-objects-bulk', '--map', map_path, '--type', 'upgrade', '--ids', ','.join(sorted(list(all_res))), '--fields', 'name,name1,editorsuffix']
res_r = subprocess.run(cmd_r, capture_output=True, text=True, encoding='utf-8')
data_r = json.loads(res_r.stdout)

wts = {}
with open('map.w3x/war3map.wts', 'r', encoding='utf-8') as f:
    blocks = re.findall(r'STRING\s+(\d+)\s*\{\s*(.*?)\s*\}', f.read(), re.DOTALL)
    for num, val in blocks:
        wts[f'TRIGSTR_{num}'] = val

def resolve(val):
    if isinstance(val, str) and val in wts:
        return wts[val]
    return val

resolved_units = {}
for obj in data_u.get('objects', []):
    raw_name = obj['fields'].get('name', '')
    res_name = resolve(raw_name)
    suffix = resolve(obj['fields'].get('editorsuffix', ''))
    resolved_units[obj['id']] = res_name

resolved_res = {}
for obj in data_r.get('objects', []):
    raw_name = obj['fields'].get('name1', obj['fields'].get('name', ''))
    res_name = resolve(raw_name)
    suffix = resolve(obj['fields'].get('editorsuffix', ''))
    resolved_res[obj['id']] = res_name

out_data = {
    'units': resolved_units,
    'researches': resolved_res,
    'missing_units': data_u.get('missing', []),
    'missing_researches': data_r.get('missing', []),
}

with open('docs/ui_text/elements_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

print('Saved docs/ui_text/elements_catalog.json')
