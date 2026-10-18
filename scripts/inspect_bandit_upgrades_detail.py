# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

wts = hw.load_wts_strings()
resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith('TRIGSTR_') else s

upgs = [
    'R00J', 'R00L', 'R00M', 'R00V', 'R00U', 'R00X', 'R00K', 'R00N', 'R00W', 'R0HP', 'R00Y', 'R00G',
    'R00D', 'R00A', 'R00B', 'R00E', 'R00F', 'R00C', 'R00I', 'R0BS'
]

print(f"Inspecting {len(upgs)} upgrades...")
for uid in upgs:
    res = hw.run_cli_json(['get-object', '--map', str(hw.DEFAULT_MAP), '--type', 'upgrade', '--id', uid])
    f = res.get('object', {}) or res.get('fields', {})
    levels = int(f.get('levels') or 1)
    print(f"\nUpgrade {uid}: levels={levels}, class={f.get('class')}")
    for i in range(1, levels + 1):
        name_k = f'name{i}' if f.get(f'name{i}') else 'name'
        tip_k = f'tip{i}'
        ub_k = f'ubertip{i}'
        hk_k = f'hotkey{i}' if f.get(f'hotkey{i}') else 'hotkey'
        print(f"  L{i}: name={f.get(name_k)} ({resolve(f.get(name_k))!r})")
        print(f"       tip={f.get(tip_k)} ({resolve(f.get(tip_k))!r})")
        print(f"       ub={f.get(ub_k)} ({resolve(f.get(ub_k))!r})")
        print(f"       hk={f.get(hk_k)} ({resolve(f.get(hk_k))!r})")
    print(f"       applies_to (effects/targets): effect1={f.get('effect1')}, code1={f.get('code1')}, mod1={f.get('mod1')}")
