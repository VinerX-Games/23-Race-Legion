import luaparser.ast as a
source = open(r'C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\sections\83_ai_brain.lua', encoding='utf-8').read()
lines = source.split('\n')
lo, hi = 0, len(lines)
while lo < hi - 1:
    mid = (lo + hi) // 2
    try:
        a.parse('\n'.join(lines[:mid]))
        lo = mid
    except:
        hi = mid
print(f'Error around line {hi}')
if hi > 0:
    ctx_start = max(0, hi - 3)
    for i in range(ctx_start, min(len(lines), hi + 2)):
        print(f'{i+1}: {lines[i][:150]}')
