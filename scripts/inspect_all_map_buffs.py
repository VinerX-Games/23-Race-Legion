import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw
from implement_draenei_rework import object_records

wts = hw.load_wts_strings()
def res(val):
    if isinstance(val, str) and val.startswith('TRIGSTR_'):
        sid = int(val[8:])
        return wts.get(sid, val)
    return val

for path_str in ['map.w3x/war3map.w3h', 'map.w3x/war3mapSkin.w3h']:
    p = Path(path_str)
    raw = p.read_bytes()
    v, tables = object_records(raw, False) # buffs are not extended
    print(f"=== {path_str} (tables={len(tables)}) ===")
    for t_idx, table in enumerate(tables):
        print(f"  Table {t_idx} count: {len(table)}")
        for r in table:
            mod_keys = [k for k, _ in r['mods']]
            # get details via HiveWE
            data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'buff', '--id', r['id'], '--warcraft', str(hw.DEFAULT_WARCRAFT)])
            f = data.get('fields', {})
            tip = res(f.get('bufftip', f.get('ftip', '')))
            ub = res(f.get('buffubertip', f.get('fube', '')))
            ed = res(f.get('editorname', f.get('fnam', '')))
            sfx = res(f.get('editorsuffix', ''))
            print(f"    {r['id']} (code={r['header'][4:8].decode('ascii', 'replace')}) name='{ed}' sfx='{sfx}' tip='{tip}' ub='{ub[:50] if ub else ''}'")
