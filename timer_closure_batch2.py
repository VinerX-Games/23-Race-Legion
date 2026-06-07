"""Convert 5 simple Category B one-shot timer callbacks to closures.
Line-based approach - reliable, no fragile regex multiline matching.
"""
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


def find_func(lines, name):
    for i, line in enumerate(lines):
        if line.strip().startswith(f'function {name}('):
            return i, find_end(lines, i)
    return None, None


def comment_back(lines, idx):
    while idx > 0 and (lines[idx - 1].strip().startswith('--') or lines[idx - 1].strip() == ''):
        idx -= 1
    return idx


def do_replace(lines, ops):
    ops.sort(key=lambda x: x[0], reverse=True)
    result = list(lines)
    for s, e, r in ops:
        if r is None:
            result[s:e] = []
        else:
            result[s:e] = r
    return result


def main():
    with open(FILEPATH, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    lines = content.split('\n')

    ops = []

    # ---- 1. TimedCountAct + TimedCount ----
    cb_s, cb_e = find_func(lines, 'TimedCountAct')
    fn_s, fn_e = find_func(lines, 'TimedCount')
    if cb_s and fn_s:
        cb_s = comment_back(lines, cb_s)
        ops.append((cb_s, cb_e + 1, None))
        ops.append((comment_back(lines, fn_s), fn_e + 1, [
            '---@param u unit',
            '---@return nothing',
            'function TimedCount(u)',
            '\tlocal t = CreateTimer()',
            '\tTimerStart(t, 0.3, false, function()',
            '\t\tDelCountDis(u, GetPlayerId(GetOwningPlayer(u)))',
            '\t\tDestroyTimer(t)',
            '\tend)',
            'end',
        ]))
        print('  OK TimedCountAct')

    # ---- 2. zlifeend (inline in Trig_ZacliatieOfLive_Actions) ----
    cb_s, cb_e = find_func(lines, 'zlifeend')
    if cb_s:
        # Find the TimerStart line referencing zlifeend
        timer_ln = None
        for i, line in enumerate(lines):
            if 'TimerStart' in line and 'zlifeend' in line:
                timer_ln = i
                break
        if timer_ln:
            cb_s = comment_back(lines, cb_s)
            ops.append((cb_s, cb_e + 1, None))
            # Replace: "TimerStart(t, 15*... , false, zlifeend)" + "SaveUnitHandle(Hash, id, 1, u)"
            # with closure, remove SaveUnitHandle line
            # Find the SaveUnitHandle line nearby
            save_ln = None
            for j in range(max(0, timer_ln - 3), min(len(lines), timer_ln + 4)):
                if 'SaveUnitHandle' in lines[j]:
                    save_ln = j
                    break
            
            # Determine range to replace (TimerStart line through SaveUnitHandle)
            rep_start = timer_ln
            # Also remove the CreateTimer + GetHandleId lines before TimerStart  
            for j in range(timer_ln - 1, max(0, timer_ln - 6), -1):
                if 'CreateTimer' in lines[j] or ('GetHandleId' in lines[j] and 'local id' in lines[j]):
                    rep_start = j
                else:
                    break
            rep_end = max(timer_ln, save_ln) + 1 if save_ln else timer_ln + 1
            
            ops.append((rep_start, rep_end, [
                '\tlocal t = CreateTimer()',
                '\tTimerStart(t, 15 * GetUnitAbilityLevel(u, FourCC(\'A1G6\')), false, function()',
                '\t\tUnitRemoveAbility(u, FourCC(\'A1G6\'))',
                '\t\tDestroyTimer(t)',
                '\tend)',
            ]))
            print('  OK zlifeend')

    # ---- 3. toporend (inline in Trig_WantAxe_Actions) ----
    cb_s, cb_e = find_func(lines, 'toporend')
    if cb_s:
        timer_ln = None
        for i, line in enumerate(lines):
            if 'TimerStart' in line and 'toporend' in line:
                timer_ln = i
                break
        if timer_ln:
            cb_s = comment_back(lines, cb_s)
            ops.append((cb_s, cb_e + 1, None))
            save_ln = None
            for j in range(max(0, timer_ln - 3), min(len(lines), timer_ln + 4)):
                if 'SaveUnitHandle' in lines[j]:
                    save_ln = j
                    break
            rep_start = timer_ln
            rep_end = max(timer_ln, save_ln if save_ln else timer_ln) + 1
            ops.append((rep_start, rep_end, [
                '\tlocal t = CreateTimer()',
                '\tTimerStart(t, 7, false, function()',
                '\t\tUnitRemoveAbility(u2, FourCC(\'A1G4\'))',
                '\t\tDestroyTimer(t)',
                '\tend)',
            ]))
            print('  OK toporend')

    # ---- 4. CorriptionTimerPlus ----
    cb_s, cb_e = find_func(lines, 'CorriptionTimerPlus')
    if cb_s:
        timer_ln = None
        for i, line in enumerate(lines):
            if 'TimerStart' in line and 'CorriptionTimerPlus' in line:
                timer_ln = i
                break
        if timer_ln:
            cb_s = comment_back(lines, cb_s)
            ops.append((cb_s, cb_e + 1, None))
            # Find SaveInteger nearby
            save_ln = None
            for j in range(max(0, timer_ln - 3), timer_ln):
                if 'SaveInteger' in lines[j]:
                    save_ln = j
                    break
            rep_start = save_ln if save_ln else timer_ln
            rep_end = timer_ln + 1
            ops.append((rep_start, rep_end, [
                '\tlocal p2 = p',
                '\tTimerStart(t, 60, false, function()',
                '\t\tif GetPlayerTechCountSimple(FourCC(\'R04O\'), p2) == 6 then',
                '\t\t\tSetPlayerAbilityAvailableBJ(true, FourCC(\'A0AT\'), p2)',
                '\t\telse',
                '\t\t\tSetPlayerAbilityAvailableBJ(true, FourCC(\'A0AS\'), p2)',
                '\t\t\tSetPlayerAbilityAvailableBJ(true, FourCC(\'A0AT\'), p2)',
                '\t\tend',
                '\t\tDestroyTimer(t)',
                '\tend)',
            ]))
            print('  OK CorriptionTimerPlus')

    # ---- 5. CorriptionTimerMinus ----
    cb_s, cb_e = find_func(lines, 'CorriptionTimerMinus')
    if cb_s:
        timer_ln = None
        for i, line in enumerate(lines):
            if 'TimerStart' in line and 'CorriptionTimerMinus' in line:
                timer_ln = i
                break
        if timer_ln:
            cb_s = comment_back(lines, cb_s)
            ops.append((cb_s, cb_e + 1, None))
            save_ln = None
            for j in range(max(0, timer_ln - 3), timer_ln):
                if 'SaveInteger' in lines[j]:
                    save_ln = j
                    break
            rep_start = save_ln if save_ln else timer_ln
            rep_end = timer_ln + 1
            ops.append((rep_start, rep_end, [
                '\tlocal p2 = p',
                '\tTimerStart(t, 60, false, function()',
                '\t\tif GetPlayerTechCountSimple(FourCC(\'R04O\'), p2) == 1 then',
                '\t\t\tSetPlayerAbilityAvailableBJ(true, FourCC(\'A0AS\'), p2)',
                '\t\telse',
                '\t\t\tSetPlayerAbilityAvailableBJ(true, FourCC(\'A0AS\'), p2)',
                '\t\t\tSetPlayerAbilityAvailableBJ(true, FourCC(\'A0AT\'), p2)',
                '\t\tend',
                '\t\tDestroyTimer(t)',
                '\tend)',
            ]))
            print('  OK CorriptionTimerMinus')

    result = do_replace(lines, ops)
    output = '\n'.join(result)
    output = re.sub(r'\n{4,}', '\n\n\n', output)

    with open(FILEPATH, 'w', encoding='utf-8-sig') as f:
        f.write(output)

    print(f'\nDone! {len([o for o in ops if o[2] is None])} callbacks deleted.')


if __name__ == '__main__':
    main()
