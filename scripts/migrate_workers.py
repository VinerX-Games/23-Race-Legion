"""
Migrate 22 AI races from production-table workers to declarative worker section.
Skips Scarlet (3 worker types via pre), ForestTrolls (town hall + military), 
Goblins (perebor), and already-migrated races.
"""
import re
import os

RACES_FILE = r"map.w3x\_lua\monolith_split\sections\82_ai_races.lua"

# Worker data for each race to migrate:
# race_name -> (worker_id, cap, [t1, t2, t3])
RACE_WORKERS = {
    "HordeW2":     ("w200", 20, ["w20q", "w20w", "w20e"]),
    "Nerubs":      ("h0BE", 20, ["h0CO", "h0CP", "h0CQ"]),
    "Forsaken":    ("h0J5", 22, ["h0JP", "h0JQ", "h0JL"]),
    "Alliance":    ("hpea", 18, ["htow", "hkee", "hcas"]),
    "Bandits":     ("h002", 18, ["h007", "h008", "h009"]),
    "Undead":      ("u00P", 18, ["n014", "u00F", "u00G"]),
    "Demons":      ("e02Y", 20, ["h0DU", "h0DV", "h0DW"]),
    "Draenei":     ("h012", 18, ["h015", "h016", "h017"]),
    "Stromgard":   ("h0G9", 18, ["h0GZ", "h0H0", "h0H1"]),
    "Illidari":    ("h0EI", 18, ["h0E9", "h0EA", "h0EB"]),
    "Worgen":      ("h0IT", 18, ["h0IK", "h0IL"]),   # only 2 tiers
    "Ogres":       ("o03W", 18, ["o035", "o03D", "o03E"]),
    "Gnomes":      ("h0FA", 18, ["h0FK", "h0FR", "h0FS"]),
    "Silitids":    ("e01R", 18, ["e01H", "e021", "e020"]),
    "Pandarens":   ("pa01", 20, ["pa23", "pa24", "pa25"]),
    "Bezlikie":    ("u02D", 18, ["h0HZ", "h0I7", "h0I8"]),
    "Vrykul":      ("h0C9", 18, ["h0BQ", "h0BR", "h0BS"]),
    "KulTiras":    ("h013", 18, ["h01X", "h01Y", "h01Z"]),
    "Dalaran":     ("u001", 18, ["h030"]),            # only 1 tier
    "IceTrolls":   ("o045", 18, ["o046", "o047", "o048"]),
    "FelOrc":      ("n06B", 18, ["o05V", "o05W", "o05X"]),
    "Ents":        ("e02T", 18, ["e02B", "e02C", "e02D"]),
}

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def build_worker_section(worker_id, cap, from_buildings):
    """Build the worker = { ... } section"""
    from_list = ", ".join(f"FourCC('{b}')" for b in from_buildings)
    return f"worker = {{ id = FourCC('{worker_id}'), cap = {cap}, from = {{ {from_list} }} }},"

def remove_worker_entries(production_body, from_buildings, worker_id):
    """Remove production entries for town halls that produce workers.
    Uses brace counting instead of regex for reliability with nested braces."""
    
    for bld in from_buildings:
        marker = f"[FourCC('{bld}')]"
        # Also try double-quoted variant
        marker_dq = f'[FourCC("{bld}")]'
        
        idx = production_body.find(marker)
        if idx == -1:
            idx = production_body.find(marker_dq)
        
        while idx != -1:
            # Find the = { start
            eq_pos = production_body.find('=', idx)
            if eq_pos == -1:
                break
            brace_open = production_body.find('{', eq_pos)
            if brace_open == -1:
                break
            
            # Count braces to find matching closing }
            depth = 1
            pos = brace_open + 1
            while pos < len(production_body) and depth > 0:
                if production_body[pos] == '{':
                    depth += 1
                elif production_body[pos] == '}':
                    depth -= 1
                    if depth == 0:
                        break
                pos += 1
            
            if depth != 0:
                break  # unbalanced
            
            # pos is at the matching }
            # Check for optional comma after the }
            if pos + 1 < len(production_body) and production_body[pos + 1] == ',':
                pos += 1
            
            # Remove from the start of the line containing [FourCC...] to pos+1
            line_start = production_body.rfind('\n', 0, idx)
            if line_start == -1:
                line_start = 0
            else:
                line_start += 1  # keep the newline
            
            production_body = production_body[:line_start] + production_body[pos + 1:]
            
            # Find next occurrence
            idx = production_body.find(marker, line_start)
            if idx == -1:
                idx = production_body.find(marker_dq, line_start)
    
    return production_body

def process_race_block(block, race_name, worker_info):
    """Replace production entries with worker section for one race"""
    worker_id, cap, from_buildings = worker_info
    
    # Find the production = { ... } block within this race block
    prod_start = re.search(r'\bproduction\s*=\s*\{', block)
    if not prod_start:
        print(f"  WARNING: no production block found for {race_name}")
        return block, False, "no production block"
    
    start_idx = prod_start.end() - 1  # position after opening {
    
    # Find matching closing brace
    depth = 1
    pos = start_idx + 1
    while pos < len(block) and depth > 0:
        if block[pos] == '{':
            depth += 1
        elif block[pos] == '}':
            depth -= 1
        pos += 1
    
    prod_body = block[start_idx:pos-1]  # content between { and }
    prod_close_idx = pos - 1
    
    # Remove old worker entries using brace-counting
    new_body = prod_body
    entries_removed = 0
    for bld in from_buildings:
        body_before = len(new_body)
        new_body = remove_worker_entries(new_body, [bld], worker_id)
        body_after = len(new_body)
        if body_before != body_after:
            entries_removed += 1
    
    if entries_removed == 0:
        print(f"  WARNING: no worker entries found to remove for {race_name}")
        return block, False, "no worker entries found"
    
    # Clean up double blank lines and trailing whitespace
    new_body = re.sub(r'\n\s*\n\s*\n', '\n\n', new_body)
    new_body = re.sub(r'\n\s+$', '\n', new_body, flags=re.MULTILINE)
    new_body = new_body.rstrip()
    
    # Ensure we end with a newline then the worker section
    if not new_body.endswith('\n'):
        new_body += '\n'
    
    # Add worker section
    worker_section = build_worker_section(worker_id, cap, from_buildings)
    new_body += "\n        " + worker_section + "\n"
    
    # Reconstruct the block
    new_block = block[:start_idx] + new_body + block[prod_close_idx:]
    
    return new_block, True, f"removed {entries_removed} entries, added worker section"


def main():
    print("=" * 70)
    print("AI RACE WORKER MIGRATION")
    print("=" * 70)
    
    content = read_file(RACES_FILE)
    original_lines = content.count('\n')
    
    # Split file into segments: text_before_race1, race1_block, text_between, race2_block, ..., text_after
    race_pattern = re.compile(r'RegisterAiRace\("([^"]+)"\s*,\s*\{', re.DOTALL)
    
    segments = []
    last_end = 0
    races_found = []
    
    for m in race_pattern.finditer(content):
        name = m.group(1)
        race_start = m.start()
        block_start = m.end() - 1  # position of opening {
        
        # Text between previous race and this race block (including "RegisterAiRace(\"Name\", ")
        segments.append(content[last_end:block_start])
        
        # Find the race block (matching braces for the table)
        block_start = m.end() - 1  # position of opening {
        depth = 1
        pos = block_start + 1
        while pos < len(content) and depth > 0:
            if content[pos] == '{':
                depth += 1
            elif content[pos] == '}':
                depth -= 1
            pos += 1
        block_end = pos  # position after closing }
        block = content[block_start:block_end]
        
        segments.append(("RACE", name, block))
        last_end = block_end
        races_found.append(name)
    
    # Text after last race
    segments.append(content[last_end:])
    
    # Process race blocks
    total_migrated = 0
    total_skipped = 0
    
    for i, seg in enumerate(segments):
        if not isinstance(seg, tuple) or seg[0] != "RACE":
            continue
        
        name = seg[1]
        block = seg[2]
        
        # Skip already-migrated
        if name in ("BloodElves", "Naga", "Horde", "JungleTrolls"):
            print(f"[{name}] SKIP (already migrated)")
            total_skipped += 1
            continue
        
        # Skip special cases
        if name in ("Scarlet", "ForestTrolls"):
            print(f"[{name}] SKIP (complex worker pattern)")
            total_skipped += 1
            continue
        
        if name == "Goblins":
            print(f"[{name}] SKIP (perebor handles workers)")
            total_skipped += 1
            continue
        
        if name not in RACE_WORKERS:
            print(f"[{name}] SKIP (not in migration list)")
            total_skipped += 1
            continue
        
        if re.search(r'\bworker\s*=\s*\{', block):
            print(f"[{name}] SKIP (already has worker section)")
            total_skipped += 1
            continue
        
        worker_info = RACE_WORKERS[name]
        new_block, success, msg = process_race_block(block, name, worker_info)
        
        if success:
            segments[i] = new_block
            print(f"[{name}] MIGRATED: {msg}")
            total_migrated += 1
        else:
            print(f"[{name}] FAILED: {msg}")
    
    # Rebuild content
    new_content = ''
    for seg in segments:
        if isinstance(seg, tuple) and seg[0] == "RACE":
            new_content += seg[2]  # it's the modified block
        else:
            new_content += seg
    
    new_lines = new_content.count('\n')
    print(f"\nTotal migrated: {total_migrated}")
    print(f"Total skipped: {total_skipped}")
    print(f"Lines: {original_lines} -> {new_lines} (delta: {new_lines - original_lines})")
    
    with open(RACES_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Written to {RACES_FILE}")
    return 0

if __name__ == '__main__':
    exit(main())
