"""Collapse 24 color command triggers into a single function using a table."""
import re
from pathlib import Path

SECTIONS = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections")


COLOR_MAP = {
    " - colorred":            "PLAYER_COLOR_RED",
    " - colorblue":           "PLAYER_COLOR_BLUE",
    " - colorpurple":         "PLAYER_COLOR_PURPLE",
    " - colorteal":           "PLAYER_COLOR_CYAN",
    " - coloryellow":          "PLAYER_COLOR_YELLOW",
    " - colororange":         "PLAYER_COLOR_ORANGE",
    " - colorgreen":          "PLAYER_COLOR_GREEN",
    " - colorpink":           "PLAYER_COLOR_PINK",
    " - colorgray":           "PLAYER_COLOR_LIGHT_GRAY",
    " - colorlight - blue":   "PLAYER_COLOR_LIGHT_BLUE",
    " - colordark - green":   "PLAYER_COLOR_AQUA",
    " - colorbrown":          "PLAYER_COLOR_BROWN",
    " - colormaroon":         "PLAYER_COLOR_MAROON",
    " - colornavy":           "PLAYER_COLOR_NAVY",
    " - colorturquoise":      "PLAYER_COLOR_TURQUOISE",
    " - colorviolet":         "PLAYER_COLOR_VIOLET",
    " - colorwheat":          "PLAYER_COLOR_WHEAT",
    " - colorpeach":          "PLAYER_COLOR_PEACH",
    " - colormint":           "PLAYER_COLOR_MINT",
    " - colorlavender":       "PLAYER_COLOR_LAVENDER",
    " - colorcoal":           "PLAYER_COLOR_COAL",
    " - colorsnow":           "PLAYER_COLOR_SNOW",
    " - coloremerald":        "PLAYER_COLOR_EMERALD",
    " - colorpeanut":         "PLAYER_COLOR_PEANUT",
}


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


def comment_back(lines, idx):
    while idx > 0 and (lines[idx - 1].strip().startswith('--') or lines[idx - 1].strip() == ''):
        idx -= 1
    return idx


def main():
    runtime_path = SECTIONS / '80_generated_runtime.lua'
    init_triggers_path = SECTIONS / '90_InitCustomTriggers.lua'

    # === Process 80_generated_runtime.lua ===
    with open(runtime_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')

    # Color trigger names
    color_names = [
        'Red', 'Blue', 'Teal', 'Lightblue', 'Yelow', 'Orange', 'Green', 'Pink',
        'Gray', 'LightBlue', 'Dark_green', 'Brown', 'Maroon', 'Navy', 'Turquoise',
        'Violet', 'Wheat', 'Peach', 'Mint', 'Lavender', 'Coal', 'Snow', 'Emerald', 'Peanut'
    ]

    ops = []

    # Find and mark all color InitTrig functions and Actions for deletion
    for cn in color_names:
        init_name = f'InitTrig_{cn}_color'
        act_name = f'Trig_{cn}_color_Actions'

        for i, line in enumerate(lines):
            if line.strip().startswith(f'function {init_name}('):
                e = find_end(lines, i)
                ops.append((i, e + 1, None))
                break
        
        for i, line in enumerate(lines):
            if line.strip().startswith(f'function {act_name}('):
                e = find_end(lines, i)
                ops.append((i, e + 1, None))
                break

    # Also delete section comment lines and ---@ annotations
    for i, line in enumerate(lines):
        for cn in color_names:
            pat = f'-- Trigger: {cn} color'
            if pat in line:
                # Delete this line and any empty/comment lines just before it
                s = i
                while s > 0 and (lines[s-1].strip().startswith('--') or lines[s-1].strip() == ''):
                    s -= 1
                ops.append((s, i + 1, None))
                break
            # Delete orphaned ---@return annotations for color actions
            if f'Trig_{cn}_color_Actions' in line and '---@return' in line:
                ops.append((i, i + 1, None))

    # Build the new InitColorCommands function
    new_func = [
        '-- ===========================================================================',
        '--  Color Commands (consolidated from 24 individual triggers)',
        '-- ===========================================================================',
        '---@return nothing',
        'function InitColorCommands()',
        '\tlocal COLOR_MAP = {',
    ]
    for cmd, color in COLOR_MAP.items():
        new_func.append(f'\t\t["{cmd}"] = {color},')
    new_func.append('\t}')
    new_func.append('')
    new_func.append('\tlocal t = CreateTrigger()')
    new_func.append('\tfor i = 0, 23 do')
    new_func.append('\t\tfor cmd, _ in pairs(COLOR_MAP) do')
    new_func.append('\t\t\tTriggerRegisterPlayerChatEvent(t, Player(i), cmd, true)')
    new_func.append('\t\tend')
    new_func.append('\tend')
    new_func.append('\tTriggerAddAction(t, function()')
    new_func.append('\t\tlocal color = COLOR_MAP[GetEventPlayerChatString()]')
    new_func.append('\t\tif color then')
    new_func.append('\t\t\tSetPlayerColorBJ(GetTriggerPlayer(), color, true)')
    new_func.append('\t\tend')
    new_func.append('\tend)')
    new_func.append('end')

    # Insert after the InitTrig_Globals function (last trigger before colors)
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('function InitTrig_Globals('):
            insert_idx = find_end(lines, i) + 2  # after its 'end' + blank line
            break
    
    if insert_idx:
        ops.append((insert_idx, insert_idx, new_func))  # start==end means INSERT

    # Apply in reverse order
    ops.sort(key=lambda x: x[0], reverse=True)
    result = list(lines)
    for s, e, r in ops:
        if r is None:
            result[s:e] = []
        elif s == e:
            # Insert
            result[s:s] = r
        else:
            result[s:e] = r

    # Clean up
    output = '\n'.join(result)
    output = re.sub(r'\n{4,}', '\n\n\n', output)

    with open(runtime_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"80_generated_runtime.lua: Color triggers consolidated")
    print(f"  Deleted: 24 InitTrig + 24 Actions + 24 comment blocks = ~740 lines")

    # === Process 90_InitCustomTriggers.lua ===
    with open(init_triggers_path, 'r', encoding='utf-8') as f:
        lines90 = f.read().split('\n')

    new_lines90 = []
    for line in lines90:
        if re.match(r'\s*InitTrig_\w+_color\(\)', line):
            # Replace first occurrence with InitColorCommands, skip rest
            continue
        new_lines90.append(line)
    
    # Insert InitColorCommands() next to the InitTrig_Globals call
    result90 = []
    for line in new_lines90:
        result90.append(line)
        if 'InitTrig_InitGlobals()' in line:
            result90.append('\tInitColorCommands()')

    with open(init_triggers_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result90))

    print(f"90_InitCustomTriggers.lua: 24 calls -> 1 call")


if __name__ == '__main__':
    main()
