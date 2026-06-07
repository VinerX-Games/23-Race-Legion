"""
Refactor: inline GetSpellAbilityId condition checks into TriggerAddAction.
Replaces the Condition+Action split pattern with a single inline action.

Handles three categories:
  A) condition = "return GetSpellAbilityId() == FourCC('XXXX')"
  B) condition = "return GetSpellAbilityId() == FourCC('XXXX') and ..."
  C) condition = multi-line "if not GetSpellAbilityId() == ... then return false end" + other checks
"""

import re
import os
import sys
from pathlib import Path


SECTION_DIR = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections")


# Pattern: standalone block-opening keyword (excluding 'do' which always pairs with for/while)
_OPEN_RE = re.compile(r'\b(function|if|for|while|repeat)\b')
_CLOSE_RE = re.compile(r'\b(end|until)\b')


def _line_depth_delta(line):
    """Net block depth change for this line, ignoring Lua comments."""
    code = line.split('--', 1)[0]  # strip line comment
    opens = len(_OPEN_RE.findall(code))
    closes = len(_CLOSE_RE.findall(code))
    return opens - closes


def skip_to_matching_end(lines, start_idx):
    """From start_idx (which is the 'function' line), return the line index
    of the matching 'end'. Properly counts ALL block keywords per line."""
    depth = 1  # We're already inside the function
    i = start_idx + 1
    while i < len(lines):
        depth += _line_depth_delta(lines[i])
        if depth == 0:
            return i
        i += 1
    return len(lines) - 1  # Fallback


def find_init_trig(content, lines):
    """Find all InitTrig_* function definitions and their line ranges."""
    inits = []
    i = 0
    while i < len(lines):
        m = re.match(r'^function\s+(InitTrig_\w+)\(\)$', lines[i])
        if m:
            name = m.group(1)
            start = i
            end = skip_to_matching_end(lines, i)
            body = '\n'.join(lines[start:end+1])
            inits.append((name, start, end, body))
            i = end + 1
            continue
        i += 1
    return inits


def extract_condition_action_from_init(init_body):
    """Extract (trigger_var, condition_func, action_func) from InitTrig body."""
    cond_match = re.search(
        r'TriggerAddCondition\s*\(\s*(\w+)\s*,\s*Condition\s*\(\s*(\w+)\s*\)\s*\)',
        init_body
    )
    action_match = re.search(
        r'TriggerAddAction\s*\(\s*(\w+)\s*,\s*(\w+)\s*\)',
        init_body
    )
    if cond_match and action_match:
        trigger_var = cond_match.group(1)
        cond_func = cond_match.group(2)
        action_func = action_match.group(2)
        return trigger_var, cond_func, action_func
    return None, None, None


def find_cond_func_body(lines, cond_func_name):
    """Find the body lines of a condition function (lines between function and matching end)."""
    for i, line in enumerate(lines):
        m = re.match(r'^function\s+' + re.escape(cond_func_name) + r'\(\)$', line)
        if m:
            end = skip_to_matching_end(lines, i)
            body_lines = lines[i+1:end]
            return i, end, body_lines
    return None, None, None


def extract_spell_fourcc(cond_body_text):
    """Extract the FourCC code from a GetSpellAbilityId check in the condition body.
    Returns (fourcc_code, has_extra_conditions, cond_type)
    cond_type: 'simple' | 'and' | 'multi'
    """
    # Try simple: return GetSpellAbilityId() == FourCC('XXXX')
    m = re.match(
        r'^\s*return\s+GetSpellAbilityId\s*\(\s*\)\s*==\s*FourCC\s*\(\s*\'(\w+)\'\s*\)\s*$',
        cond_body_text.strip()
    )
    if m:
        return m.group(1), False, 'simple'

    # Try AND: return GetSpellAbilityId() == FourCC('XXXX') and ...
    m = re.search(
        r'return\s+GetSpellAbilityId\s*\(\s*\)\s*==\s*FourCC\s*\(\s*\'(\w+)\'\s*\)\s+and\s+(.+)',
        cond_body_text
    )
    if m:
        return m.group(1), m.group(2).strip(), 'and'

    # Try multi-line (if-not pattern): if ( not (GetSpellAbilityId() == FourCC('XXXX'))) then return false end
    # Extract the FourCC from any line containing GetSpellAbilityId
    m = re.search(
        r'GetSpellAbilityId\s*\(\s*\)\s*==\s*FourCC\s*\(\s*\'(\w+)\'\s*\)',
        cond_body_text
    )
    if m:
        return m.group(1), None, 'multi'

    return None, None, None


def generate_guard_clause(fourcc_code):
    """Generate the guard clause line."""
    return f"        if GetSpellAbilityId() ~= FourCC('{fourcc_code}') then return end"


def generate_new_init(init_body, trigger_var, action_func, fourcc_code, extra_cond, cond_type, cond_func_name=None):
    """Generate new InitTrig body with inline condition."""
    new_lines = []
    in_action = False
    
    for line in init_body.split('\n'):
        stripped = line.strip()
        
        # Skip TriggerAddCondition lines
        if re.search(r'TriggerAddCondition', stripped):
            continue
        
        # Transform TriggerAddAction into inline version
        if re.search(rf'TriggerAddAction\s*\(\s*{trigger_var}\s*,\s*{action_func}\s*\)', stripped):
            new_lines.append(f"    TriggerAddAction({trigger_var}, function()")
            new_lines.append(generate_guard_clause(fourcc_code))
            
            if cond_type == 'and' and extra_cond:
                # AND condition: must also check the extra condition
                new_lines.append(f"        if not ({extra_cond}) then return end")
            elif cond_type == 'multi' and cond_func_name:
                # Multi-line condition: call the stripped version
                # For multi, we keep the original condition function but remove the spell check
                new_lines.append(f"        if not {cond_func_name}() then return end")
            
            new_lines.append(f"        {action_func}()")
            new_lines.append(f"    end)")
            continue
        
        new_lines.append(line)
    
    return '\n'.join(new_lines)


def strip_spell_check_from_cond_func(body_lines, fourcc_code):
    """Remove the GetSpellAbilityId check from a multi-line condition.
    Handles the typical 3-line if-block:
        if ( not (GetSpellAbilityId() == FourCC('XXXX'))) then
            return false
        end
    Returns (new_body_lines, was_modified)
    """
    new_lines = []
    modified = False
    i = 0
    while i < len(body_lines):
        line = body_lines[i]
        if re.search(r'GetSpellAbilityId\s*\(\s*\)\s*==\s*FourCC\s*\(\s*\'' + re.escape(fourcc_code) + r'\'\s*\)', line):
            modified = True
            # Check 3-line if/return/end pattern
            if (i + 2 < len(body_lines)
                and re.match(r'\s*return\s+false\s*$', body_lines[i + 1])
                and re.match(r'\s*end\s*$', body_lines[i + 2])):
                i += 3  # Skip all 3 lines: if-then, return false, end
            else:
                i += 1  # Fallback: skip just this line
            continue
        new_lines.append(line)
        i += 1
    return new_lines, modified


def find_all_condition_functions(lines):
    """Find all Condition function definitions (Trig_*_Conditions) and their line ranges.
    Returns dict: name -> (start, end, body_lines)
    """
    conds = {}
    i = 0
    while i < len(lines):
        m = re.match(r'^function\s+(Trigg?_\w+_Conditions)\(\)$', lines[i])
        if m:
            name = m.group(1)
            start = i
            end = skip_to_matching_end(lines, i)
            body_lines = lines[start+1:end]
            conds[name] = (start, end, body_lines)
            i = end + 1
            continue
        i += 1
    return conds


def process_file(filepath):
    """Process a single Lua file."""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find all condition functions (for later cleanup)
    conds = find_all_condition_functions(lines)
    
    # Find all InitTrig functions
    inits = find_init_trig(content, lines)
    
    modifications = []
    conds_to_strip = {}  # name -> (start, end, new_body_lines)
    conds_to_delete = set()  # names of condition functions to delete entirely
    action_refs = {}  # track which action functions are referenced
    
    for init_name, init_start, init_end, init_body in inits:
        trigger_var, cond_func, action_func = extract_condition_action_from_init(init_body)
        
        if not cond_func or not action_func:
            continue
        
        if cond_func not in conds:
            continue
        
        cond_start, cond_end, cond_body_lines = conds[cond_func]
        cond_body_text = '\n'.join(cond_body_lines)
        
        if 'GetSpellAbilityId' not in cond_body_text:
            continue
        
        fourcc_code, extra_cond, cond_type = extract_spell_fourcc(cond_body_text)
        
        if not fourcc_code:
            print(f"  WARNING: Could not extract FourCC from {cond_func}")
            continue
        
        action_refs[action_func] = True
        
        print(f"  {init_name}: {cond_func} -> inline FourCC('{fourcc_code}') [{cond_type}]")
        
        if cond_type == 'simple':
            # Category A: delete condition function entirely
            new_init = generate_new_init(init_body, trigger_var, action_func, fourcc_code, None, 'simple')
            modifications.append((init_start, init_end + 1, new_init))
            conds_to_delete.add(cond_func)
            
        elif cond_type == 'and':
            # Category B: delete condition function, inline AND check
            new_init = generate_new_init(init_body, trigger_var, action_func, fourcc_code, extra_cond, 'and')
            modifications.append((init_start, init_end + 1, new_init))
            conds_to_delete.add(cond_func)
            
        elif cond_type == 'multi':
            # Category C: strip spell check from condition function, keep rest
            new_cond_lines, modified = strip_spell_check_from_cond_func(cond_body_lines, fourcc_code)
            if modified:
                if len(new_cond_lines) == 1 and re.match(r'^\s*return\s+true\s*$', new_cond_lines[0].strip()):
                    # Condition became just "return true" => delete it entirely
                    conds_to_delete.add(cond_func)
                    new_init = generate_new_init(init_body, trigger_var, action_func, fourcc_code, None, 'simple')
                else:
                    # Keep stripped condition function
                    conds_to_strip[cond_func] = new_cond_lines
                    new_init = generate_new_init(init_body, trigger_var, action_func, fourcc_code, None, 'multi', cond_func_name=cond_func)
                modifications.append((init_start, init_end + 1, new_init))
            else:
                print(f"  WARNING: Could not strip spell check from {cond_func}")
    
    if not modifications:
        print("  No modifications needed.")
        return
    
    # Check which condition functions are safe to delete
    for cond_name in list(conds_to_delete):
        occurrences = content.count(cond_name)
        func_def_count = 1 if f'function {cond_name}()' in content else 0
        cond_ref_count = content.count(f'Condition({cond_name})')
        if occurrences > (func_def_count + cond_ref_count):
            print(f"  SKIP deleting {cond_name}: used elsewhere ({occurrences} occurrences)")
            conds_to_delete.discard(cond_name)
    
    # Collect ALL edit operations as (start, end, replacement_lines)
    # replacement_lines = None means DELETE the range
    # Using original line numbers (before any modifications)
    all_ops = []
    
    # Init modifications
    for init_start, init_end, new_init in modifications:
        all_ops.append((init_start, init_end, new_init.split('\n')))
    
    # Condition deletions (original positions)
    for cond_name in conds_to_delete:
        if cond_name in conds:
            c_start, c_end, _ = conds[cond_name]
            all_ops.append((c_start, c_end + 1, None))  # None = delete
    
    # Condition strips (original positions)
    for cond_name, new_body in conds_to_strip.items():
        if cond_name in conds:
            c_start, c_end, c_body = conds[cond_name]
            # Build the new condition function with stripped body
            full_func = [f'function {cond_name}()'] + new_body + ['end']
            all_ops.append((c_start, c_end + 1, full_func))
    
    # Sort by start position descending (process end-of-file first)
    all_ops.sort(key=lambda x: x[0], reverse=True)
    
    # Apply all operations in a single pass
    result_lines = list(lines)
    for op_start, op_end, replacement in all_ops:
        if replacement is None:
            result_lines[op_start:op_end] = []
        else:
            result_lines[op_start:op_end] = replacement
    
    # Write back
    new_content = '\n'.join(result_lines)
    with open(filepath, 'w', encoding='utf-8-sig') as f:
        f.write(new_content)
    
    total_removed = len(conds_to_delete) + len(conds_to_strip)
    print(f"  Done: {len(modifications)} triggers refactored, {len(conds_to_delete)} condition functions removed, {len(conds_to_strip)} stripped.")


def fix_orphan_condition_vars(filepath):
    """Remove orphaned Condition variables that were only used in now-deleted TriggerAddCondition calls.
    E.g. Remove lines like: local cond = Condition(Func)  when Func has been inlined.
    """
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Find orphaned Condition assignments (Condition(func) assignments that are never used)
    # This handles library patterns where a local variable holds the Condition
    # e.g. local cond = Condition(func) -- if func is now inlined, remove this
    
    # Simple heuristic: find Condition(func) on its own line with a variable assignment
    # Pattern: local varname = Condition(funcname)
    patches = []
    for m in re.finditer(r'(\s*)(local\s+)?(\w+)\s*=\s*Condition\s*\(\s*(\w+)\s*\)', content):
        varname = m.group(3)
        funcname = m.group(4)
        # Check if varname is used in TriggerAddCondition elsewhere
        # If no TriggerAddCondition using this varname exists, it's orphaned
        # Actually, this is complex. Let's skip this for now and handle manually.
        pass
    
    return


def process_libraries():
    """Process library files that use Condition+Action pattern with GetSpellAbilityId."""
    
    # SpellSleepAOE
    spell_file = SECTION_DIR / "libraries" / "09_SpellSleepAOE.lua"
    if spell_file.exists():
        with open(spell_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        # Pattern: TriggerAddCondition(t, Condition(SpellSleepAOE___anon__0))
        # and: TriggerAddAction(t, SpellSleepAOE___anon__1)
        # where SpellSleepAOE___anon__0 checks: return SpellSleepAOE___SpellHero == GetSpellAbilityId()
        
        new_content = content.replace(
            'TriggerAddCondition(t, Condition(SpellSleepAOE___anon__0))\n\tTriggerAddAction(t, SpellSleepAOE___anon__1)',
            '''TriggerAddAction(t, function()
        if SpellSleepAOE___SpellHero ~= GetSpellAbilityId() then return end
        SpellSleepAOE___anon__1()
    end)'''
        )
        
        # Remove the condition function definition
        new_content = re.sub(
            r'---@return boolean\n---@param \w+ \w+\nfunction SpellSleepAOE___anon__0\(\)\n\treturn SpellSleepAOE___SpellHero == GetSpellAbilityId\(\)\nend\n',
            '',
            new_content
        )
        # Try simpler pattern
        new_content = re.sub(
            r'function SpellSleepAOE___anon__0\(\)\n\treturn SpellSleepAOE___SpellHero == GetSpellAbilityId\(\)\nend\n',
            '',
            new_content
        )
        
        with open(spell_file, 'w', encoding='utf-8-sig') as f:
            f.write(new_content)
        print(f"Processed libraries/09_SpellSleepAOE.lua")
    
    # SanctifiedEnchantment
    enchant_file = SECTION_DIR / "libraries" / "12_SanctifiedEnchantment.lua"
    if enchant_file.exists():
        with open(enchant_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        # Pattern: TriggerAddCondition(trg, Condition(SanctifiedEnchantment___SkillCondition_EFFECT))
        # and: TriggerAddAction(trg, SanctifiedEnchantment___SkillAction_EFFECT)
        # where condition checks: return GetSpellAbilityId() == SanctifiedEnchantment_SkillId
        
        new_content = content.replace(
            'TriggerAddCondition(trg, Condition(SanctifiedEnchantment___SkillCondition_EFFECT))\n\tTriggerAddAction(trg, SanctifiedEnchantment___SkillAction_EFFECT)',
            '''TriggerAddAction(trg, function()
        if GetSpellAbilityId() ~= SanctifiedEnchantment_SkillId then return end
        SanctifiedEnchantment___SkillAction_EFFECT()
    end)'''
        )
        
        # Remove the condition function definition
        new_content = re.sub(
            r'function SanctifiedEnchantment___SkillCondition_EFFECT\(\)\n\treturn GetSpellAbilityId\(\) == SanctifiedEnchantment_SkillId\nend\n',
            '',
            new_content
        )
        
        with open(enchant_file, 'w', encoding='utf-8-sig') as f:
            f.write(new_content)
        print(f"Processed libraries/12_SanctifiedEnchantment.lua")


def main():
    print("=" * 60)
    print("Spell Condition Inline Refactoring")
    print("=" * 60)
    
    # Process 80_generated_runtime.lua (main file)
    runtime_file = SECTION_DIR / "80_generated_runtime.lua"
    if runtime_file.exists():
        process_file(runtime_file)
    else:
        print(f"ERROR: {runtime_file} not found!")
    
    # Process library files
    process_libraries()
    
    # Also check other section files for TriggerAddCondition with GetSpellAbilityId
    for lua_file in SECTION_DIR.glob("*.lua"):
        if lua_file.name == "80_generated_runtime.lua":
            continue
        with open(lua_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        if 'TriggerAddCondition' in content and 'GetSpellAbilityId' in content:
            print(f"Found additional file with spell conditions: {lua_file.name}")
    
    # Check 90_InitCustomTriggers.lua - this calls InitTrig functions, doesn't need mod
    print("\nDone!")


if __name__ == "__main__":
    main()
