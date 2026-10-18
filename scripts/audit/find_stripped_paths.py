import re
import glob

# Read original jass strings for lookup
jass_text = open('war3map.j', encoding='utf-16le').read()
jass_paths = set(re.findall(r'"([^\"]+\.(?:mdl|mdx|blp))"', jass_text, re.I))

# Map stripped version -> original full path
stripped_to_full = {}
for p in jass_paths:
    clean = p.replace('\\', '').replace('/', '')
    stripped_to_full[clean.lower()] = p

print(f"Total JASS asset paths: {len(jass_paths)}, mapped: {len(stripped_to_full)}")

# Now scan all lua files
pat = re.compile(r'"([A-Za-z0-9_]+\.(?:mdl|mdx|blp))"', re.I)
found = []
for f in glob.glob('map.w3x/_lua/monolith_split/sections/**/*.lua', recursive=True):
    content = open(f, encoding='utf-8').read()
    for m in pat.finditer(content):
        val = m.group(1)
        if '\\' not in val and '/' not in val:
            low = val.lower()
            if low in stripped_to_full and ('\\' in stripped_to_full[low] or '/' in stripped_to_full[low]):
                found.append((f, val, stripped_to_full[low]))

print(f"Found {len(found)} corrupted stripped paths in Lua:")
for f, val, orig in found:
    print(f"{f}: '{val}' -> '{orig}'")
