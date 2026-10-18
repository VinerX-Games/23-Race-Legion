# -*- coding: utf-8 -*-
import json
from pathlib import Path

dump = json.loads(Path('scripts/gilneas_raw_dump.json').read_text(encoding='utf-8'))
for a in dump['abilities']:
    has_wts = any(isinstance(v.get('raw'), str) and v.get('raw').startswith('TRIGSTR_') for v in a['tips'].values()) or \
              any(isinstance(v.get('raw'), str) and v.get('raw').startswith('TRIGSTR_') for v in a['ubertips'].values()) or \
              (isinstance(a.get('raw_name'), str) and a.get('raw_name').startswith('TRIGSTR_'))
    name_str = a.get('name') or ''
    suff = a.get('editorsuffix') or ''
    print(f"{a['id']:6s} | name: {name_str:30s} | levels: {a['levels']} | has_wts: {str(has_wts):5s} | suffix: {suff}")
