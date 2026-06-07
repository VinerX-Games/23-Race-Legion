"""Analyze Condition() variable patterns in the runtime file."""
import re
with open(r'C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Check all b/bex/Boolexpr/udg_Boolexpr assignments
vars_to_check = ['b', 'bex', 'Boolexpr', 'udg_Boolexpr']

for var in vars_to_check:
    assignments = 0
    local_count = 0
    func_map = {}
    for i, line in enumerate(lines):
        pat = re.compile(r'\b' + re.escape(var) + r'\s*=\s*Condition\((\w+)\)')
        m = pat.search(line)
        if m and not line.strip().startswith('--'):
            assignments += 1
            func_name = m.group(1)
            is_local = 'local' in line.split('--')[0]
            if is_local:
                local_count += 1
            func_map[func_name] = func_map.get(func_name, 0) + 1
    
    if assignments > 0:
        print(f'{var}: {assignments} assignments, {local_count} local, functions: {func_map}')

# Also check b in GroupEnum calls
group_enum_with_b = 0
for i, line in enumerate(lines):
    if re.search(r'GroupEnum\w+.*\bb\b', line) and not line.strip().startswith('--'):
        group_enum_with_b += 1
print(f'\nGroupEnum with variable b: {group_enum_with_b} lines')

# Check: is b ever used OUTSIDE of GroupEnum? 
# Count all uses of b in non-comment code
b_uses = 0
for i, line in enumerate(lines):
    code = line.split('--')[0]
    b_uses += len(re.findall(r'\bb\b(?!\s*=)', code))
print(f'Uses of b (non-assignment): {b_uses}')
