import json
from pathlib import Path

manifest_path = Path(r"C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\manifest.json")
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

# Find the generated_runtime entry
gen_rt_idx = None
gen_rt_start = None
for i, s in enumerate(manifest["sections"]):
    if s["name"] == "generated_runtime":
        gen_rt_idx = i
        gen_rt_start = s["start_line"]
        break

if gen_rt_idx is None:
    print("ERROR: generated_runtime not found in manifest")
    exit(1)

# Read the _manifest.lua from the split to get file ordering
split_manifest = Path(r"C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\sections\80_split\_manifest.lua")
lines = split_manifest.read_text(encoding="utf-8").splitlines()

split_files = []
for line in lines:
    if line.strip().startswith('"') and '.lua' in line:
        fname = line.split('"')[1]
        line_count = int(line.split('(')[1].split()[0])
        split_files.append((fname, line_count))

print(f"Split files: {len(split_files)}")

# Build new section entries
new_entries = []
current_start = gen_rt_start
for fname, lcount in split_files:
    new_entries.append({
        "name": "generated:" + fname.replace('.lua',''),
        "file": "80_split/" + fname,
        "category": "generated_runtime",
        "start_line": current_start,
        "end_line": current_start + lcount - 1,
        "library_name": None
    })
    current_start += lcount

# Replace the single entry with the split entries
old_count = len(manifest["sections"])
manifest["sections"] = (
    manifest["sections"][:gen_rt_idx] +
    new_entries +
    manifest["sections"][gen_rt_idx + 1:]
)

manifest["section_count"] = len(manifest["sections"])
print(f"Sections: {old_count} -> {len(manifest['sections'])}")

# Write updated manifest
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
print("Updated manifest.json")
