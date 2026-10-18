import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wc3_hivewe as hw
import json

troll_upgs = [
    'R09L', 'R09P', 'R0AD', 'R0AI', 'R0AJ', 'R0EU', 'R0HZ', 'R0I0', 'R0I1', 'R0I2',
    'R0I3', 'R0I4', 'R0I5', 'R0I6', 'R0I7', 'R0IE', 'R0IF', 'R0IG', 'R0IX', 'R0IY'
]

wts = hw.load_wts_strings()
def res(val):
    if isinstance(val, str) and val.startswith('TRIGSTR_'):
        sid = int(val[8:])
        return wts.get(sid, val)
    return val

info = {}
for qid in troll_upgs:
    data = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', qid, '--warcraft', str(hw.DEFAULT_WARCRAFT)])
    f = data.get('fields', {})
    
    # Check max level based on how many levels have distinct cost/effects
    levels_data = []
    for l in range(1, 7):
        name = res(f.get(f'name{l}', ''))
        tip = res(f.get(f'tip{l}', ''))
        ub = res(f.get(f'ubertip{l}', ''))
        gold = f.get(f'gold{l}', f.get('gold', ''))
        lumb = f.get(f'lumb{l}', f.get('lumb', ''))
        time = f.get(f'time{l}', f.get('time', ''))
        req = f.get(f'req{l}', f.get(f'requires{l}', f.get('requires', '')))
        
        # calculate effect values
        # effect1: base1 + (l-1)*mod1
        effects = []
        for e_idx in range(1, 5):
            ecode = f.get(f'effect{e_idx}', '')
            if ecode and ecode != '-':
                base = f.get(f'base{e_idx}', '0')
                mod = f.get(f'mod{e_idx}', '0')
                try:
                    val = float(base) + (l - 1) * float(mod)
                except:
                    val = f"{base} + {mod}*l"
                effects.append(f"{ecode}={val}")
                
        levels_data.append({
            'level': l,
            'name': name,
            'tip': tip,
            'ubertip': ub,
            'gold': gold,
            'lumb': lumb,
            'time': time,
            'req': req,
            'effects': effects
        })
    info[qid] = {
        'id': qid,
        'code': f.get('code', qid),
        'hotkey': res(f.get('hotkey', '')),
        'levels': levels_data
    }

(Path('docs/ui_text/ice_troll_upgrades_detailed.json')).write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved to docs/ui_text/ice_troll_upgrades_detailed.json")
