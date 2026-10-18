# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
gnomes_lua = ROOT / "map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races/Gnomes.lua"
content = gnomes_lua.read_text(encoding="utf-8")

# Find all string literals
strings = set(re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', content))
print("String literals found in Gnomes.lua:")
for s in sorted(strings):
    print(" ", repr(s))

# Find specific function calls
print("\nInteresting function calls:")
for line_no, line in enumerate(content.splitlines(), 1):
    for pat in ["Display", "Text", "Item", "Message", "Quest"]:
        if pat.lower() in line.lower() and not line.strip().startswith("--"):
            print(f"  Line {line_no}: {line.strip()}")
