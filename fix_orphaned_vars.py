"""Fix orphaned udg_Boolexpr references and broken bex conditional assignments."""
import re
from pathlib import Path

FILEPATH = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua")


def depth(line):
    code = line.split('--', 1)[0]
    return len(re.findall(r'\b(function|if|for|while|repeat)\b', code)) - \
           len(re.findall(r'\b(end|until)\b', code))


def find_end(lines, start):
    d = 1; i = start + 1
    while i < len(lines):
        d += depth(lines[i])
        if d == 0:
            return i
        i += 1
    return len(lines) - 1


def main():
    with open(FILEPATH, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    lines = content.split('\n')

    # === FIX 1: Restore udg_Boolexpr assignments (without Condition wrapper) ===
    # udg_Boolexpr was assigned in these functions:
    # Type_1 -> in functions with farm/filter logic (line ~6139 orig)
    # Trig_Gob_Potreblenie_Func001002 -> in Trig_Gob_Potreblenie_Actions
    # HaveSilitidSpell -> in Trig_Silitid_Potreblenie_Actions  
    # ItIsCity -> in Trig_Cities_Start_2_Actions

    # Strategy: find the FIRST occurrence of udg_Boolexpr in each function
    # and insert the assignment right before it
    
    functions_to_fix = {}
    
    # Find all udg_Boolexpr usages and group by enclosing function
    i = 0
    current_func = None
    func_start = 0
    func_end = 0
    while i < len(lines):
        m = re.match(r'^function\s+(\w+)', lines[i])
        if m:
            current_func = m.group(1)
            func_start = i
            func_end = find_end(lines, i)
            i = func_end + 1
            continue
        
        if current_func and 'udg_Boolexpr' in lines[i].split('--')[0]:
            if current_func not in functions_to_fix:
                functions_to_fix[current_func] = {
                    'first_use': i,
                    'function_name': current_func,
                    'func_start': func_start,
                    'func_end': func_end,
                }
        i += 1

    # Map functions to their original boolexpr assignments
    # Based on git blame analysis:
    func_to_expr = {
        'Trig_GnomeNotToMuch_Actions': 'Type_1',
        'Trig_FarmTier2_Actions': 'Type_1',
        'Trig_FarmTier3_Actions': 'Type_1',
        'Trig_TLimit_Actions': 'Type_1',
        'Trig_Gob_Potreblenie_Actions': 'Trig_Gob_Potreblenie_Func001002',
        'Trig_Silitid_Potreblenie_Actions': 'HaveSilitidSpell',
        'Trig_Cities_Start_2_Actions': 'ItIsCity',
    }

    # Actually, just scan ALL functions with udg_Boolexpr and add the assignment
    # The assignment was always at the START of the function, before the first use
    ops = []
    
    for func_name, info in functions_to_fix.items():
        # Find the first udg_Boolexpr use
        first_use = info['first_use']
        func_start = info['func_start']
        
        # Check if there's already an assignment nearby
        has_assign = False
        for j in range(func_start, first_use):
            if 'udg_Boolexpr =' in lines[j].split('--')[0]:
                has_assign = True
                break
        
        if not has_assign:
            # Determine which expr based on function name
            # Default: Type_1 (most common for farm/filter functions)
            expr = func_to_expr.get(func_name)
            if expr:
                # Insert assignment before first use
                assign_line = f'\tudg_Boolexpr = {expr}'
                ops.append((first_use, first_use, [assign_line, lines[first_use]]))  # replace line with insert+original
                print(f'  +assign {func_name}: udg_Boolexpr = {expr}')
            else:
                print(f'  WARN: unknown expr for {func_name}')

    # Apply ops (reverse order)
    ops.sort(key=lambda x: x[0], reverse=True)
    for start, end, replacement in ops:
        lines[start:end] = replacement

    # === FIX 2: Fix bex conditional assignments (restore without Condition) ===
    # Find pattern: "local bex" followed by if/else and later use
    for i, line in enumerate(lines):
        if re.match(r'\s*local bex\s*$', line) and i + 2 < len(lines):
            # Check if the next lines have if/elseif/else assigning Condition
            j = i + 1
            has_conditions = False
            while j < min(i + 30, len(lines)):
                if 'end' in lines[j] and re.match(r'\s*end\s*$', lines[j]):
                    # Check if this end closes the if block
                    if has_conditions:
                        break
                if 'Condition(isEnemy)' in lines[j] or 'Condition(isAlly)' in lines[j] or 'Condition(isOwner)' in lines[j]:
                    has_conditions = True
                j += 1
            
            if has_conditions:
                # Restore without Condition()
                for k in range(i, j + 1):
                    lines[k] = lines[k].replace('Condition(isEnemy)', 'isEnemy')
                    lines[k] = lines[k].replace('Condition(isAlly)', 'isAlly')
                    lines[k] = lines[k].replace('Condition(isOwner)', 'isOwner')
                print(f'  FIX bex conditional at L{i+1}')

    # Write back
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f'\nDone! {len([o for o in ops if len(o[2]) == 2])} udg_Boolexpr restored.')


if __name__ == '__main__':
    main()
