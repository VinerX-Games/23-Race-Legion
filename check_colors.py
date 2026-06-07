import re
with open(r'C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua', encoding='utf-8-sig') as f:
    c = f.read()

# Find all chat command strings used in color triggers
names = [
    'Red', 'Blue', 'Teal', 'Lightblue', 'Yelow', 'Orange', 'Green', 'Pink',
    'Gray', 'LightBlue', 'Dark_green', 'Brown', 'Maroon', 'Navy', 'Turquoise',
    'Violet', 'Wheat', 'Peach', 'Mint', 'Lavender', 'Coal', 'Snow', 'Emerald', 'Peanut'
]

for color_name in names:
    fn_name = f'InitTrig_{color_name}_color'
    # Find the InitTrig function body
    pat = rf'function {fn_name}\(\)\n(.*?)end'
    m = re.search(pat, c, re.DOTALL)
    if m:
        cmd_match = re.search(r'"([^"]*)"', m.group(1))
        cmd = cmd_match.group(1) if cmd_match else '???'
        # Find Actions function
        act_name = f'Trig_{color_name}_color_Actions'
        act_pat = rf'function {act_name}\(\)\n(.*?)end'
        am = re.search(act_pat, c, re.DOTALL)
        col = '???'
        if am:
            cm = re.search(r'PLAYER_COLOR_(\w+)', am.group(1))
            col = cm.group(1) if cm else '???'
        print(f'  ["{cmd}"] = PLAYER_COLOR_{col},')
