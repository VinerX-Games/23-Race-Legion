"""Convert bj_forLoopA/B GUI-style loops to idiomatic Lua for loops."""
import re
from pathlib import Path

FILEPATH = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua")

FOR_LOOP_START = re.compile(r'(\s*)(bj_forLoop[A-Z]Index)\s*=\s*(-?\d+)')


def main():
    with open(FILEPATH, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    lines = content.split('\n')
    count = 0
    i = 0
    
    while i < len(lines):
        m = FOR_LOOP_START.match(lines[i])
        if not m:
            i += 1
            continue
        
        indent = m.group(1)
        var_name = m.group(2)      # bj_forLoopAIndex or bj_forLoopBIndex
        start_val = m.group(3)
        
        # Determine variable prefix (A or B)
        suffix = var_name.replace('bj_forLoop', '').replace('Index', '')
        end_var = f'bj_forLoop{suffix}IndexEnd'
        
        # Search forward up to 3 lines for the End assignment
        for j in range(i + 1, min(i + 4, len(lines))):
            stripped = lines[j].strip()
            if re.match(rf'{end_var}\s*=\s*(-?\d+)', stripped):
                end_val = re.match(rf'{end_var}\s*=\s*(-?\d+)', stripped).group(1)
                end_line_idx = j
                break
        
        if end_val is None:
            i += 1
            continue
        
        # Find the "while true do" line (should be within ~3 lines after End)
        while_line = None
        for j in range(end_line_idx + 1, min(end_line_idx + 4, len(lines))):
            if re.match(rf'\s*while true do\s*$', lines[j]):
                while_line = j
                break
        
        if while_line is None:
            i += 1
            continue
        
        # Find the break condition line (should be next after while)
        break_line = while_line + 1
        if break_line >= len(lines):
            i += 1
            continue
        
        break_pattern = rf'if\s+{re.escape(var_name)}\s*>\s*{end_var}\s+then\s+break\s+end'
        if not re.match(break_pattern, lines[break_line].strip()):
            i += 1
            continue
        
        # Find the increment line: should be the line BEFORE the final "end"
        # We need to find the matching "end" for the while loop
        # Use depth tracking
        
        depth = 1  # for the while loop
        end_loop_line = None
        increment_line = None
        
        for j in range(while_line + 1, min(while_line + 500, len(lines))):
            code = lines[j].split('--', 1)[0]
            depth += len(re.findall(r'\b(while|for|if|function|repeat)\b', code))
            depth -= len(re.findall(r'\b(end|until)\b', code))
            if depth == 0:
                end_loop_line = j
                break
        
        if end_loop_line is None:
            i += 1
            continue
        
        # Find increment line: var = var + 1 (may be a few lines before end, skipping blank lines)
        increment_line = None
        for j in range(end_loop_line - 1, break_line, -1):
            inc_pattern = rf'{re.escape(var_name)}\s*=\s*{re.escape(var_name)}\s*\+\s*1'
            if re.match(inc_pattern, lines[j].strip()):
                increment_line = j
                break
        
        # Rebuild: for loop replaces everything from start to end_loop_line
        # New lines: "for var_name = start_val, end_val do" + body + "end"
        new_lines = []
        
        # The for loop header
        new_lines.append(f'{indent}for {var_name} = {start_val}, {end_val} do')
        
        # Body: everything between break_line+1 and increment_line (or end_loop_line)
        body_start = break_line + 1
        body_end = increment_line if increment_line else end_loop_line
        
        for j in range(body_start, body_end):
            new_lines.append(lines[j])
        
        new_lines.append(f'{indent}end')
        
        # Replace the range
        lines = lines[:i] + new_lines + lines[end_loop_line + 1:]
        count += 1
        
        # Move to after the replacement (need to account for length change)
        i = i + len(new_lines)
    
    print(f'Converted {count} bj_forLoop blocks')

    with open(FILEPATH, 'w', encoding='utf-8-sig') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    main()
