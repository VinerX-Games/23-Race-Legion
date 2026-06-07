"""Convert timer+hashtable utility functions to closure-based timers.
Uses line-based parsing for reliability, not fragile regex.
"""
import re
from pathlib import Path

FILEPATH = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua")


def apply_op(lines, ops):
    """Apply line-range operations in reverse (end-of-file first), rebuilding lines.
    ops: list of (start_line_idx, end_line_idx, replacement_lines_or_None)
         None means DELETE. Sorted descending by start before calling.
    """
    ops.sort(key=lambda x: x[0], reverse=True)
    result = list(lines)
    for start, end, replacement in ops:
        if replacement is None:
            result[start:end] = []
        else:
            result[start:end] = replacement
    return result


def find_function(lines, name):
    """Find a function by name. Returns (start_idx, end_idx) or (None, None)."""
    for i, line in enumerate(lines):
        m = re.match(r'^function\s+' + re.escape(name) + r'\s*\b', line)
        if m:
            return i, _skip_to_matching_end(lines, i)
    return None, None


def _line_depth_delta(line):
    code = line.split('--', 1)[0]
    opens = len(re.findall(r'\b(function|if|for|while|repeat)\b', code))
    closes = len(re.findall(r'\b(end|until)\b', code))
    return opens - closes


def _skip_to_matching_end(lines, start_idx):
    depth = 1
    i = start_idx + 1
    while i < len(lines):
        depth += _line_depth_delta(lines[i])
        if depth == 0:
            return i
        i += 1
    return len(lines) - 1


def make_closure_func(name, params, body_lines, doc_lines=None):
    """Generate new function with closure-based timer."""
    out = []
    if doc_lines:
        out.extend(doc_lines)
    out.append(f'function {name}({", ".join(params)})')
    out.extend(f'\t{line}' for line in body_lines)
    out.append('end')
    return out


# ============================================================
# Each transformation: (entry_func, params, closure_body_lines, doc_lines)
# The callback function will be auto-detected and deleted
# ============================================================

TRANSFORMS = [
    {
        'entry': 'RemoveUnitTimed',
        'params': ['u', 'time'],
        'body': [
            'local t = CreateTimer()',
            'TimerStart(t, time, false, function()',
            '\tRemoveUnit(u)',
            '\tDestroyTimer(t)',
            'end)',
        ],
        'delete_callbacks': ['ToKillAct'],
    },
    {
        'entry': 'ReviveHeroTimed',
        'params': ['u', 'time'],
        'body': [
            'local t = CreateTimer()',
            'TimerStart(t, time, false, function()',
            '\tgUnit = u',
            '\tCounter = 0',
            '\tGroupEnumUnitsOfPlayer(gGroup, GetOwningPlayer(gUnit), UnitsWithReviveHeroSpell)',
            '\tif FirstOfGroup(gGroup) ~= nil then',
            '\t\tgUnit2 = GroupPickRandomUnit2(gGroup)',
            '\t\tReviveHero(gUnit, GetUnitX(gUnit2), GetUnitY(gUnit2), true)',
            '\tend',
            '\tDestroyTimer(t)',
            'end)',
        ],
        'delete_callbacks': ['ReviveHeroTimedAct'],
    },
    {
        'entry': 'RemoveLigtingTimed',
        'params': ['l', 'time'],
        'body': [
            'local t = CreateTimer()',
            'TimerStart(t, time, false, function()',
            '\tDestroyLightning(l)',
            '\tDestroyTimer(t)',
            'end)',
        ],
        'delete_callbacks': ['RemoveLigtingTimedAct'],
    },
    {
        'entry': 'RemoveTextTagTimed',
        'params': ['ft', 'time'],
        'body': [
            'local t = CreateTimer()',
            'TimerStart(t, time, false, function()',
            '\tDestroyTextTag(ft)',
            '\tDestroyTimer(t)',
            'end)',
        ],
        'delete_callbacks': ['RemoveTextTagTimedAct'],
    },
    {
        'entry': 'CollisionTimed',
        'params': ['u', 'CollisionOn', 'time'],
        'body': [
            'local t = CreateTimer()',
            'TimerStart(t, time, false, function()',
            '\tSetUnitPathing(u, CollisionOn)',
            '\tDestroyTimer(t)',
            'end)',
        ],
        'delete_callbacks': ['CollisionTimedAct'],
    },
    {
        'entry': 'SetBuildingProgressTimed',
        'params': ['u', 'BuildingProgress', 'time'],
        'body': [
            'local t = CreateTimer()',
            'TimerStart(t, time, false, function()',
            '\tUnitSetConstructionProgress(u, BuildingProgress)',
            '\tDestroyTimer(t)',
            'end)',
        ],
        'delete_callbacks': ['SetBuildingProgressTimedAct'],
    },
    {
        'entry': 'IssuerImmediateOrderTimed',
        'params': ['order', 'u', 'time'],
        'body': [
            'local t = CreateTimer()',
            'TimerStart(t, time, false, function()',
            '\tIssueImmediateOrder(u, order)',
            '\tDestroyTimer(t)',
            'end)',
        ],
        'delete_callbacks': ['IssuerImmedeateOrderTimedAct'],
    },
]


def main():
    with open(FILEPATH, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    ops = []

    for t in TRANSFORMS:
        entry_name = t['entry']
        params = t['params']
        body = t['body']

        # Find entry function
        entry_start, entry_end = find_function(lines, entry_name)
        if entry_start is None:
            print(f"  SKIP {entry_name}: not found")
            continue

        # Get comment block before the function (---@param lines + comment header)
        # Search backwards from entry_start for the comment block
        comment_start = entry_start
        while comment_start > 0:
            prev = lines[comment_start - 1].strip()
            if prev.startswith('--') or prev == '':
                comment_start -= 1
            else:
                break
        # Collect annotation lines
        doc_lines = []
        for j in range(comment_start, entry_start):
            stripped = lines[j].strip()
            if stripped.startswith('--'):
                doc_lines.append(lines[j])

        # Build new function lines
        new_func = []
        if doc_lines:
            new_func.extend(doc_lines)
        new_func.append(f'function {entry_name}({", ".join(params)})')
        new_func.extend(f'\t{line}' for line in body)
        new_func.append('end')

        # Apply: replace everything from comment_start to entry_end
        ops.append((comment_start, entry_end + 1, new_func))
        print(f"  OK {entry_name}")

        # Mark callbacks for deletion
        for cb_name in t['delete_callbacks']:
            cb_start, cb_end = find_function(lines, cb_name)
            if cb_start is not None:
                # Include surrounding comments/whitespace
                del_start = cb_start
                while del_start > 0:
                    prev = lines[del_start - 1].strip()
                    if prev.startswith('--') or prev == '':
                        del_start -= 1
                    else:
                        break
                ops.append((del_start, cb_end + 1, None))
                print(f"  DEL {cb_name}")
            else:
                print(f"  WARN: {cb_name} not found for deletion")

    # Apply all operations
    result_lines = apply_op(lines, ops)
    result = '\n'.join(result_lines)

    # Remove triple+ blank lines (clean up)
    result = re.sub(r'\n{4,}', '\n\n\n', result)

    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"\nDone! {len(TRANSFORMS)} functions converted, {sum(len(t['delete_callbacks']) for t in TRANSFORMS)} callbacks deleted.")


if __name__ == '__main__':
    main()
