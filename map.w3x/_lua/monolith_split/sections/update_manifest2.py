import json
from pathlib import Path

manifest_path = Path(r"C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\manifest.json")
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

# Remove any existing generated runtime entries (old 80_split, old 80_runtime, and old generated_runtime)
new_sections = []
skip = False
for s in manifest["sections"]:
    cat = s.get("category","")
    name = s.get("name","")
    if cat == "generated_runtime" or name == "generated_runtime":
        skip = True
        continue
    new_sections.append(s)

# Now find the insertion point (before 81_ai.lua)
insert_idx = None
for i, s in enumerate(new_sections):
    if "81_ai.lua" in s.get("file",""):
        insert_idx = i
        break

if insert_idx is None:
    print("ERROR: 81_ai.lua not found")
    exit(1)

# Build new entries from 80_runtime directory structure
runtime_dir = Path(r"C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\sections\80_runtime")

# Order: infiles need to be in file-system concatenation order
# The files are named such that alphabetical sort = correct order within each dir
# But the dir order matters: _infra, _lib, _player, _ui, _races, _ai, _continental, _features, _data, triggers
dir_order = ["_infra", "_lib", "_player", "_ui", "_races", "_ai", "_continental", "_features", "_data", "triggers"]

new_entries = []
for d in dir_order:
    dp = runtime_dir / d
    if not dp.is_dir():
        continue
    for f in sorted(dp.iterdir()):
        if not f.suffix == '.lua':
            continue
        rel = f"80_runtime/{d}/{f.name}"
        new_entries.append({
            "name": f"gen:{d.replace('_','')}_{f.stem}",
            "file": rel,
            "category": "generated_runtime",
            "start_line": 0,
            "end_line": 0,
            "library_name": None
        })

# Insert at the right position
all_sections = new_sections[:insert_idx] + new_entries + new_sections[insert_idx:]
manifest["sections"] = all_sections
manifest["section_count"] = len(all_sections)

manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated manifest: {len(all_sections)} sections ({len(new_entries)} from 80_runtime)")
