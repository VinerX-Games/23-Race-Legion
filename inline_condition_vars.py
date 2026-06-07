"""Replace Condition() variable assignments with direct function references.
Handles b, bex, Boolexpr, udg_Boolexpr with scope-aware replacement.
"""
import re
from pathlib import Path

FILEPATH = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua")

TARGET_VARS = ['b', 'Boolexpr']


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
    with open(FILEPATH, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')

    total_removed = 0
    total_replaced = 0

    i = 0
    while i < len(lines):
        # Check if this line starts a function
        m = re.match(r'^function\s+', lines[i])
        if not m:
            i += 1
            continue
        
        func_start = i
        func_end = find_end(lines, i)
        func_lines = lines[func_start:func_end + 1]

        # Find Condition variable assignments in this function
        replacements = []  # (var_name, func_ref, search_start_line)

        for j, line in enumerate(func_lines):
            code = line.split('--', 1)[0]
            for var in TARGET_VARS:
                cm = re.search(r'\b' + re.escape(var) + r'\s*=\s*Condition\((\w+)\)', code)
                if cm:
                    func_ref = cm.group(1)
                    replacements.append((var, func_ref, j))
                    break

        if not replacements:
            i = func_end + 1
            continue

        # Process replacements within this function scope
        # Sort by line (earliest first) so we handle reassignments correctly
        replacements.sort(key=lambda x: x[2])
        
        new_func_lines = list(func_lines)
        lines_to_delete = set()

        for idx, (var, func_ref, assign_line) in enumerate(replacements):
            # Determine scope: from assign_line+1 to next reassignment of SAME var, or function end
            scope_end = len(func_lines)
            for j in range(assign_line + 1, len(func_lines)):
                if re.search(r'\b' + re.escape(var) + r'\s*=\s*Condition\(', func_lines[j].split('--', 1)[0]):
                    scope_end = j
                    break

            # Replace uses of var in this scope
            scope_lines = new_func_lines[assign_line + 1:scope_end]
            old_var_pat = re.compile(r'\b' + re.escape(var) + r'\b')

            for sj in range(len(scope_lines)):
                line = scope_lines[sj]
                code = line.split('--', 1)
                comment = ('--' + code[1]) if len(code) > 1 else ''
                code_part = code[0]

                if var in code_part:
                    new_code = old_var_pat.sub(func_ref, code_part)
                    if new_code != code_part:
                        scope_lines[sj] = new_code + comment
                        total_replaced += 1

            # Mark assignment line for deletion
            lines_to_delete.add(assign_line)

        # Remove assignment lines (reverse order)
        for dl in sorted(lines_to_delete, reverse=True):
            del new_func_lines[dl]
            total_removed += 1

        # Apply modification
        lines = lines[:func_start] + new_func_lines + lines[func_end + 1:]
        i = func_start + len(new_func_lines)

    # Write back
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Removed {total_removed} Condition() variable assignments")
    print(f"Replaced {total_replaced} variable references with direct function")


if __name__ == '__main__':
    main()
