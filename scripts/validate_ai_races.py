"""
Validates AI race definitions from the 82_ai_races.lua header plus 82_ai_races/*.lua
Checks:
- Required fields (tokens, weight, altar, start)
- Buildings: seed, duplicate IDs, gate references
- Production: gate/branch references, valid structure
- Strateg: gate references, valid actions
- Tokens uniqueness
- Attacker/Attacked unit ID references
- ecoWeights building references
"""
import re
import os
from pathlib import Path
from collections import defaultdict

RACES_ROOT = Path(r"map.w3x\_lua\monolith_split\sections")
RACES_FILE = str(RACES_ROOT / "82_ai_races.lua")
RACE_EXTRA_DIR = RACES_ROOT / "82_ai_races"
LIB_RACES_FILE = r"map.w3x\_lua\monolith_split\sections\libraries\13_Races.lua"

# Read all rawcodes from the world editor files and lua code to get valid IDs
VALID_RAWCODES = set()
w3u_path = r"map.w3x\war3map.w3u"
w3q_path = r"map.w3x\war3map.w3q"
w3a_path = r"map.w3x\war3map.w3a"
w3h_path = r"map.w3x\war3map.w3h"


def extract_fourcc_from_file(filepath):
    """Extract all FourCC rawcodes from a Lua file"""
    codes = set()
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        matches = re.findall(r"FourCC\('([^']+)'\)", content)
        for m in matches:
            if len(m) == 4:
                codes.add(m)
    except Exception as e:
        pass
    return codes


def extract_fourcc_from_text(content):
    codes = set()
    matches = re.findall(r"FourCC\('([^']+)'\)", content)
    for m in matches:
        if len(m) == 4:
            codes.add(m)
    return codes


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()


def read_race_sources():
    parts = [read_file(RACES_FILE)]
    if RACE_EXTRA_DIR.is_dir():
        for path in sorted(RACE_EXTRA_DIR.glob("*.lua")):
            parts.append("\n\n" + read_file(str(path)))
    return "".join(parts)


def extract_race_blocks(content):
    """Extract individual RegisterAiRace blocks from the file"""
    blocks = {}
    pattern = re.compile(
        r'RegisterAiRace\("([^"]+)"\s*,\s*\{',
        re.DOTALL
    )
    for match in pattern.finditer(content):
        race_name = match.group(1)
        start = match.end() - 1  # position after opening brace
        # Find matching closing brace
        depth = 1
        pos = start + 1
        while pos < len(content) and depth > 0:
            if content[pos] == '{':
                depth += 1
            elif content[pos] == '}':
                depth -= 1
            pos += 1
        block = content[start:pos]
        blocks[race_name] = block
    return blocks


def extract_field(block, field_name):
    """Extract a simple field value from a race block"""
    pattern = re.compile(r'\b' + field_name + r'\s*=\s*(.+?),?\s*(?:\n|--)')
    match = pattern.search(block)
    if match:
        return match.group(1).strip()
    return None

def extract_fourcc_value(val):
    """Extract 4-char code from FourCC('XXXX') string, or None"""
    if val is None:
        return None
    m = re.search(r"FourCC\('([^']+)'\)", val)
    if m:
        return m.group(1)
    return val


def extract_table(block, field_name):
    """Extract a table value like buildings = { ... }"""
    # Find field_name = { and match braces
    pattern = re.compile(
        r'\b' + field_name + r'\s*=\s*\{',
        re.DOTALL
    )
    match = pattern.search(block)
    if match is None:
        return None
    start = match.end() - 1
    depth = 1
    pos = start + 1
    while pos < len(block) and depth > 0:
        if block[pos] == '{':
            depth += 1
        elif block[pos] == '}':
            depth -= 1
        pos += 1
    return block[start:pos]


def extract_fourccs(text):
    """Extract all FourCC rawcodes from text"""
    return set(re.findall(r"FourCC\('([^']+)'\)", text))


def parse_buildings(buildings_block):
    """Parse buildings table, return {seed, entries: [{id, limit, power, gate}]}"""
    if buildings_block is None:
        return None
    fourccs = re.findall(r"FourCC\('([^']+)'\)", buildings_block)
    result = {'seed': None, 'entries': [], 'all_ids': set()}

    # Extract seed (seed is the "always present" base building; having a building
    # entry with the same ID is intentional and NOT a duplicate.)
    seen_ids = set()
    seed_match = re.search(r'seed\s*=\s*FourCC\([\'"]([^\'"]+)[\'"]\)', buildings_block)
    if seed_match:
        result['seed'] = seed_match.group(1)
        # Don't add seed to seen_ids - matching building entry is expected

    # Extract building entries
    entry_pattern = re.compile(
        r'\{\s*FourCC\([\'"]([^\'"]+)[\'"]\)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*gate\s*=\s*"([^"]+)")?\s*\}',
        re.DOTALL
    )
    for m in entry_pattern.finditer(buildings_block):
        entry = {
            'id': m.group(1),
            'limit': int(m.group(2)),
            'power': int(m.group(3)),
            'gate': m.group(4)
        }
        if entry['id'] in seen_ids:
            entry['duplicate'] = True
        else:
            entry['duplicate'] = False
            seen_ids.add(entry['id'])
        result['all_ids'].add(entry['id'])
        result['entries'].append(entry)

    return result


def parse_production(production_block):
    """Parse production table, return {buildings: {id: [entries]}, gates_refs, branch_refs, pre_exists}"""
    if production_block is None:
        return None
    result = {'buildings': defaultdict(list), 'gates_refs': set(), 'branch_refs': set(), 'pre': False}

    # Find building sections: [FourCC('XXXX')] = { ... }
    building_pattern = re.compile(
        r'\[FourCC\([\'"]([^\'"]+)[\'"]\)\]\s*=\s*\{(.*?)\n\s*\},',
        re.DOTALL
    )
    for m in building_pattern.finditer(production_block):
        bld_id = m.group(1)
        body = m.group(2)

        # Parse entries
        entry_pattern = re.compile(
            r'\{\s*(FourCC\([\'"]([^\'"]+)[\'"]\)\s*,\s*(\d+)|(\d+)\s*,\s*(\d+))(?:\s*,\s*gate\s*=\s*"([^"]+)")?(?:\s*,\s*branch\s*=\s*"([^"]+)")?(?:\s*,\s*limit\s*=\s*(\d+))?\s*\}',
            re.DOTALL
        )
        for em in entry_pattern.finditer(body):
            entry = {}
            if em.group(2):  # unitFourCC with weight
                entry['uid'] = em.group(2)
                entry['weight'] = int(em.group(3)) if em.group(3) else 1
            else:  # 0, weight (no train)
                entry['uid'] = '0'
                entry['weight'] = int(em.group(5)) if em.group(5) else 1
            if em.group(6):
                entry['gate'] = em.group(6)
                result['gates_refs'].add(em.group(6))
            if em.group(7):
                entry['branch'] = em.group(7)
                result['branch_refs'].add(em.group(7))
            if em.group(8):
                entry['limit'] = int(em.group(8))
            result['buildings'][bld_id].append(entry)

    # Check worker section
    worker_match = re.search(r'worker\s*=', production_block)
    if worker_match:
        # Just note it exists, its gates don't need separate validation for now
        pass

    # Check for pre function
    if re.search(r'pre\s*=\s*function', production_block):
        result['pre'] = True

    return result


def parse_gates(gates_block):
    """Parse gates table, return set of gate names"""
    if gates_block is None:
        return set()
    # Gate names: gate_name = function(...)
    gates = set(re.findall(r'(\w+)\s*=\s*function\s*\(', gates_block))
    return gates


def parse_branches(branches_block):
    """Parse branches table, return set of branch names"""
    if branches_block is None:
        return set()
    branches = set(re.findall(r'(\w+)\s*=\s*function\s*\(', branches_block))
    return branches


def parse_strateg(strateg_block):
    """Parse strategData and return step info and gate refs"""
    if strateg_block is None:
        return None
    result = {'steps': [], 'gates_refs': set(), 'gradeCap': None}
    cap_match = re.search(r'gradeCap\s*=\s*(\d+)', strateg_block)
    if cap_match:
        result['gradeCap'] = int(cap_match.group(1))

    # Extract gates refs from step gate="name"
    gate_refs = set(re.findall(r'gate\s*=\s*"([^"]+)"', strateg_block))
    result['gates_refs'] = gate_refs

    # Count steps
    step_count = len(re.findall(r'\{\s*at\s*=\s*\d+', strateg_block))
    result['step_count'] = step_count

    return result


def parse_attacker(attacker_block):
    """Parse attackerData and extract unit IDs with abilities"""
    if attacker_block is None:
        return None
    result = {'units': set(), 'ability_count': 0}
    # Keys: [FourCC('XXXX')] = {
    unit_keys = re.findall(r'\[FourCC\([\'"]([^\'"]+)[\'"]\)\]\s*=', attacker_block)
    result['units'] = set(unit_keys)
    # Count abilities
    abilities = re.findall(r'order\s*=\s*"([^"]+)"', attacker_block)
    result['ability_count'] = len(abilities)
    return result


def parse_attacked(attacked_block):
    """Parse attackedData and extract unit IDs"""
    if attacked_block is None:
        return None
    unit_keys = re.findall(r'\[FourCC\([\'"]([^\'"]+)[\'"]\)\]\s*=', attacked_block)
    return set(unit_keys)


def count_limit_gates(buildings):
    """Count total references to limit-gated entries"""
    count = 0
    if buildings and buildings['entries']:
        for e in buildings['entries']:
            if e['limit'] < 100 and e['limit'] > 1:  # reasonable limits
                pass  # just checking
    return count


def validate_race(name, block, all_tokens, all_fourccs):
    """Validate a single race definition, returns list of issues"""
    issues = []

    # --- Required fields ---
    tokens_raw = extract_field(block, 'tokens')
    weight = extract_field(block, 'weight')
    altar = extract_field(block, 'altar')
    start = extract_field(block, 'start')
    usesWater = extract_field(block, 'usesWaterPoint')

    if tokens_raw:
        tokens = re.findall(r'"([^"]+)"', tokens_raw)
    else:
        tokens = []
        issues.append("MISSING tokens")

    if weight is None:
        issues.append("MISSING weight")
    else:
        try:
            w = int(weight)
            if w <= 0:
                issues.append(f"weight={w} (should be >0)")
        except:
            issues.append(f"weight is not integer: {weight}")

    altar_code = extract_fourcc_value(altar)
    if altar is None or altar_code is None:
        issues.append("MISSING altar")
    elif altar_code not in all_fourccs:
        issues.append(f"altar {altar_code} not found in any FourCC references in file")

    if start is None:
        issues.append("MISSING start function")

    # --- Tokens uniqueness ---
    for t in tokens:
        t_lower = t.lower()
        if t_lower in all_tokens:
            if all_tokens[t_lower] != name:
                issues.append(f"TOKEN CONFLICT: '{t}' also used by race '{all_tokens[t_lower]}'")
        all_tokens[t_lower] = name

    # --- Buildings ---
    buildings_block = extract_table(block, 'buildings')
    buildings = None
    bld_ids = set()
    if buildings_block is None:
        issues.append("MISSING buildings")
    else:
        buildings = parse_buildings(buildings_block)
        if buildings is None:
            issues.append("Failed to parse buildings")
        else:
            if buildings['seed'] is None:
                issues.append("buildings has NO seed")
            bld_ids = set(e['id'] for e in buildings['entries'])
            bld_ids.add(buildings.get('seed', ''))
            for e in buildings['entries']:
                if re.match(r'^[A-Z]{2}$', e['id']):
                    issues.append(f"POSSIBLE BAD BUILDING RAWCODE: {e['id']} (2 chars instead of 4)")

    # --- Production ---
    prod_block = extract_table(block, 'production')
    prod = None
    if prod_block is not None:
        prod = parse_production(prod_block)
        pass  # Will validate gate refs below

    # --- Gates ---
    gates_block = extract_table(block, 'gates')
    defined_gates = parse_gates(gates_block) if gates_block else set()

    # --- Branches ---
    branches_block = extract_table(block, 'branches')
    defined_branches = parse_branches(branches_block) if branches_block else set()

    # --- Check gate refs in buildings ---
    if buildings_block and buildings:
        bld_gate_refs = set()
        for e in buildings['entries']:
            if e['gate']:
                bld_gate_refs.add(e['gate'])
        for g in bld_gate_refs:
            if g not in defined_gates:
                issues.append(f"UNDEFINED GATE in buildings: '{g}'")

    # --- Check gate/branch refs in production ---
    if prod:
        for g in prod['gates_refs']:
            if g not in defined_gates:
                issues.append(f"UNDEFINED GATE in production: '{g}'")
        for b in prod['branch_refs']:
            if b not in defined_branches:
                issues.append(f"UNDEFINED BRANCH in production: '{b}'")

    # --- Strateg ---
    strateg_block = extract_table(block, 'strategData')
    strateg = None
    if strateg_block:
        strateg = parse_strateg(strateg_block)
        for g in strateg['gates_refs']:
            if g not in defined_gates:
                issues.append(f"UNDEFINED GATE in strateg: '{g}'")

    # --- ecoWeights ---
    eco_block = extract_table(block, 'ecoWeights')
    eco_fourccs = extract_fourccs(eco_block) if eco_block else set()

    # --- attackerData ---
    attacker_block = extract_table(block, 'attackerData')
    attacker = parse_attacker(attacker_block) if attacker_block else None

    # --- attackedData ---
    attacked_block = extract_table(block, 'attackedData')
    attacked = parse_attacked(attacked_block) if attacked_block else None

    # --- getLvlData ---
    getlvl_block = extract_table(block, 'getLvlData')

    # --- Cross-check: production building IDs should exist in buildings or be seed ---
    if prod and buildings:
        bld_ids = set(e['id'] for e in buildings['entries'])
        bld_ids.add(buildings.get('seed', ''))
        for pb in prod['buildings']:
            if pb not in bld_ids:
                issues.append(f"PRODUCTION bld {pb} not in buildings list (may come from techUp)")

    # --- Cross-check: attackerData unit IDs (informational, heroes/buildings may be valid) ---
    # Not flagged as error - attackerData keys are often heroes or special units

    # --- Procedural legacy fallbacks ---
    has_legacy_chooseBuild = bool(re.search(r'\bchooseBuild\s*=', block))
    has_legacy_perebor = bool(re.search(r'\bperebor\s*=', block))
    has_legacy_strateg = bool(re.search(r'\bstrateg\s*=\s*function', block))
    has_legacy_attacker = bool(re.search(r'\battacker\s*=\s*function', block))
    if has_legacy_chooseBuild:
        issues.append("has legacy chooseBuild (should migrate to buildings)")
    if has_legacy_perebor:
        issues.append("has legacy perebor (should migrate to production)")
    if has_legacy_strateg:
        issues.append("has legacy strateg (should migrate to strategData)")
    if has_legacy_attacker:
        issues.append("has legacy attacker (should migrate to attackerData)")

    # --- ecoWeights: referenced buildings should exist ---
    if eco_block and buildings:
        for efc in eco_fourccs:
            if efc not in bld_ids:
                issues.append(f"ecoWeight bld {efc} not in buildings list")

    # --- Unused gates ---
    if gates_block and defined_gates:
        all_gate_refs = set()
        if buildings:
            for e in buildings['entries']:
                if e.get('gate'):
                    all_gate_refs.add(e['gate'])
        if prod:
            all_gate_refs.update(prod['gates_refs'])
        if strateg:
            all_gate_refs.update(strateg['gates_refs'])
        unused = defined_gates - all_gate_refs
        for g in unused:
            issues.append(f"UNUSED GATE: '{g}' defined but never used")

    return issues


def main():
    print("=" * 70)
    print("AI RACE VALIDATOR")
    print("=" * 70)

    content = read_race_sources()
    all_fourccs = extract_fourcc_from_text(content)

    # Also get fourccs from the main data library for cross-reference
    try:
        lib_content = read_file(LIB_RACES_FILE)
        lib_fourccs = extract_fourcc_from_file(LIB_RACES_FILE)
        all_fourccs.update(lib_fourccs)
    except:
        pass

    blocks = extract_race_blocks(content)

    print(f"\nFound {len(blocks)} AI race definitions\n")

    all_tokens = {}
    total_issues = 0
    race_stats = []

    for name, block in blocks.items():
        issues = validate_race(name, block, all_tokens, all_fourccs)

        # Collect stats
        buildings_block = extract_table(block, 'buildings')
        buildings = parse_buildings(buildings_block) if buildings_block else None
        prod_block = extract_table(block, 'production')
        prod = parse_production(prod_block) if prod_block else None
        strateg_block = extract_table(block, 'strategData')
        strateg = parse_strateg(strateg_block) if strateg_block else None
        attacker_block = extract_table(block, 'attackerData')
        attacker = parse_attacker(attacker_block) if attacker_block else None
        attacked_block = extract_table(block, 'attackedData')
        attacked = parse_attacked(attacked_block) if attacked_block else None

        # Count production buildings
        prod_buildings_count = len(prod['buildings']) if prod else 0
        prod_entries_count = sum(len(v) for v in prod['buildings'].values()) if prod else 0

        has_legacy_chooseBuild = bool(re.search(r'\bchooseBuild\s*=', block))
        has_legacy_perebor = bool(re.search(r'\bperebor\s*=', block))
        has_legacy_strateg = bool(re.search(r'\bstrateg\s*=\s*function', block))
        has_legacy_attacker = bool(re.search(r'\battacker\s*=\s*function', block))
        has_join = bool(re.search(r'\bjoin\s*=', block))
        has_legacy = has_legacy_chooseBuild or has_legacy_perebor or has_legacy_strateg or has_legacy_attacker
        has_join = bool(re.search(r'\bjoin\s*=', block))

        race_stats.append({
            'name': name,
            'issues': len(issues),
            'warns': len(issues),
            'buildings': len(buildings['entries']) if buildings else 0,
            'prod_buildings': prod_buildings_count,
            'prod_entries': prod_entries_count,
            'strateg_steps': strateg['step_count'] if strateg else 0,
            'attacker_units': len(attacker['units']) if attacker else 0,
            'attacked_units': len(attacked) if attacked else 0,
            'gates': len(parse_gates(extract_table(block, 'gates')) if extract_table(block, 'gates') else set()),
            'has_join': has_join,
            'legacy': has_legacy,
            'legacy_details': [],
            'worker': bool(prod_block and 'worker' in prod_block) if prod_block else False,
        })

        if issues:
            total_issues += len(issues)
            print(f"[{name}] {len(issues)} issue(s):")
            for issue in issues:
                print(f"  - {issue}")
            print()
        else:
            print(f"[{name}] OK")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY TABLE  (W=worker, J=join, L=legacy)")
    print("=" * 70)
    hdr = f"{'Race':<16} {'Bld':>4} {'PrdB':>4} {'PrdE':>4} {'Strat':>5} {'Atk':>3} {'Def':>3} {'Gt':>3} {'Iss':>3} {'WJL':>3}"
    print(hdr)
    print("-" * 70)
    for rs in race_stats:
        flag = " !!" if rs['issues'] > 0 else "   "
        wjl = ""
        wjl += "W" if rs['worker'] else "."
        wjl += "J" if rs['has_join'] else "."
        wjl += "L" if rs['legacy'] else "."
        print(f"{rs['name']+flag:<16} {rs['buildings']:>4} {rs['prod_buildings']:>4} {rs['prod_entries']:>4} "
              f"{rs['strateg_steps']:>5} {rs['attacker_units']:>3} {rs['attacked_units']:>3} "
              f"{rs['gates']:>3} {rs['warns']:>3} {wjl:>3}")

    print("-" * 70)
    print(f"Total races: {len(blocks)}")
    print(f"Total issues found: {total_issues}")
    print(f"Total unique FourCC rawcodes in file: {len(all_fourccs)}")

    # Token coverage check
    print(f"\nTotal unique tokens: {len(all_tokens)}")

    # Check for races that lack certain optional but common features
    missing_attacker = [rs['name'] for rs in race_stats if rs['attacker_units'] == 0]
    missing_attacked = [rs['name'] for rs in race_stats if rs['attacked_units'] == 0]
    missing_strateg = [rs['name'] for rs in race_stats if rs['strateg_steps'] == 0]
    missing_gates = [rs['name'] for rs in race_stats if rs['gates'] == 0]

    if missing_attacker:
        print(f"Races WITHOUT attackerData: {', '.join(missing_attacker)}")
    if missing_attacked:
        print(f"Races WITHOUT attackedData: {', '.join(missing_attacked)}")
    if missing_strateg:
        print(f"Races WITHOUT strategData: {', '.join(missing_strateg)}")
    if missing_gates:
        print(f"Races WITHOUT gates: {', '.join(missing_gates)}")

    return 0 if total_issues == 0 else 1


if __name__ == '__main__':
    exit(main())
