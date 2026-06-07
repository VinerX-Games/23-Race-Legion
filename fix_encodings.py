import os, re
root = r'C:\Games\23 Race\23-Race_Legion_Worktree3'
scripts = ['inline_condition_vars.py', 'inline_spell_conditions.py', 'null_to_nil.py',
           'timer_to_closure.py', 'timer_closure_batch2.py', 'group_condition_to_direct.py',
           'for_loop_convert.py', 'collapse_colors.py']
for s in scripts:
    p = os.path.join(root, s)
    if os.path.exists(p):
        with open(p, 'r') as f: c = f.read()
        c = c.replace("encoding='utf-8-sig'", "encoding='utf-8'")
        with open(p, 'w') as f: f.write(c)
        print(f'Fixed: {s}')
print('Done')
