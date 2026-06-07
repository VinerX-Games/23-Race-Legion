import json
from pathlib import Path

manifest_path = Path(r"C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\manifest.json")
order_path = Path(r"C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\sections\80_runtime\_file_order.txt")

manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
file_order = order_path.read_text(encoding="utf-8").strip().splitlines()

# Remove all generated_runtime category entries
new_sections = []
for s in manifest["sections"]:
    if s.get("category") == "generated_runtime" or s.get("name") == "generated_runtime":
        continue
    new_sections.append(s)

# Find insertion point (before 81_ai.lua)
insert_idx = None
for i, s in enumerate(new_sections):
    if "81_ai.lua" in s.get("file", ""):
        insert_idx = i
        break

if insert_idx is None:
    print("ERROR: 81_ai.lua not found")
    exit(1)

# Build new entries in file_order order
new_entries = []
for rel in file_order:
    parts = rel.replace("\\", "/").split("/")
    dirname = parts[1]
    fname = parts[2]
    stem = Path(fname).stem
    new_entries.append({
        "name": f"gen:{dirname}_{stem}",
        "file": rel,
        "category": "generated_runtime",
        "start_line": 0,
        "end_line": 0,
        "library_name": None
    })

all_sections = new_sections[:insert_idx] + new_entries + new_sections[insert_idx:]
manifest["sections"] = all_sections
manifest["section_count"] = len(all_sections)

manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated: {len(all_sections)} sections ({len(new_entries)} from 80_runtime)")
