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

pat = re.compile(r'"([A-Za-z0-9_]+\.(?:mdl|mdx|blp))"', re.I)

def process_file(f):
    content = open(f, encoding='utf-8').read()
    changed = [False]
    
    def repl(m):
        val = m.group(1)
        low = val.lower()
        if low in stripped_to_full:
            full = stripped_to_full[low]
            if '\\' in full or '/' in full:
                # full already has double backslashes in JASS text
                changed[0] = True
                return f'"{full}"'
        return m.group(0)

    new_content = pat.sub(repl, content)
    if changed[0]:
        open(f, 'w', encoding='utf-8').write(new_content)
        print(f"Updated {f}")
        return 1
    return 0

total_replacements = sum(process_file(f) for f in glob.glob('map.w3x/_lua/monolith_split/sections/**/*.lua', recursive=True))
print(f"Total files updated: {total_replacements}")
