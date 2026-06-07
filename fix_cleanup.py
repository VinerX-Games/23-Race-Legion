import re
path = r'C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# Clean DestroyBoolExpr(bex) - no longer needed since no Condition() is used
before = len(re.findall(r'DestroyBoolExpr\(bex\)', c))
c = re.sub(r'\s*DestroyBoolExpr\(bex\)\s*\n\s*bex\s*=\s*nil\s*\n', '\n', c)
c = re.sub(r'\s*DestroyBoolExpr\(bex\)\s*\n', '\n', c)
after = len(re.findall(r'DestroyBoolExpr\(bex\)', c))

# Verify bex assignments exist
bex_assigns = len(re.findall(r'\bbex\s*=', c))

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'DestroyBoolExpr(bex): {before} -> {after}')
print(f'bex assignments: {bex_assigns}')
print(f'udg_Boolexpr in GroupEnum: {len(re.findall(r"GroupEnum\w+.*udg_Boolexpr", c))}')
