"""Replace GroupEnum* + Condition(func) with direct function reference.
Safer line-based approach.
"""
import re
from pathlib import Path

FILEPATH = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua")


def main():
    with open(FILEPATH, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    count = 0
    new_lines = []
    
    for line in content.split('\n'):
        code = line.split('--', 1)[0]
        has_group_enum = bool(re.search(r'GroupEnum\w+', code))
        has_condition = 'Condition(' in code
        
        if has_group_enum and has_condition:
            new_line = re.sub(r'Condition\((\w+)\)', r'\1', line)
            if new_line != line:
                count += 1
                print(f'  {line.strip()[:90]}')
                print(f'  -> {new_line.strip()[:90]}')
                print()
            line = new_line
        
        new_lines.append(line)
    
    print(f'\nTotal: {count} replacements')
    
    with open(FILEPATH, 'w', encoding='utf-8-sig') as f:
        f.write('\n'.join(new_lines))


if __name__ == '__main__':
    main()
