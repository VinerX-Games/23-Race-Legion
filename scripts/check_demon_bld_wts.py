# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

bld_wts = [
    13204, 13205, 31733,
    13208, 13209, 19467,
    13242, 13243, 31740,
    13246, 13247, 31741,
    13250, 13251, 31742,
    13254, 13255, 31743,
    13258, 13259, 31744,
    13262, 13263, 31745,
    13266, 13267, 31746,
    13284, 13285, 31748,
    13269, 13270, 31747,
]

wts_set = {f"TRIGSTR_{x}" for x in bld_wts}
bld_ids = {'h0DS', 'h0DT', 'h0DU', 'h0DV', 'h0DW', 'h0DX', 'h0DY', 'h0DZ', 'h0E0', 'h0E1', 'n02C'}

print("Checking shared usages for Demon buildings WTS strings...")

# Check using hivewe get-object or scan w3u/w3a/w3q/w3h
from wc3_object_tools import cli, require

for typ in ['unit', 'ability', 'buff', 'upgrade', 'item']:
    # Let's inspect objects by scanning raw data
    pass

# We can search war3map.wts references or scan via wc3_tools
import re

wts_content = (ROOT / "map.w3x/war3map.wts").read_text(encoding="utf-8")
print(f"Total target WTS keys: {len(bld_wts)}")

# Check binary object files directly by reading raw strings in files
bin_files = [
    ROOT / "map.w3x/war3map.w3u",
    ROOT / "map.w3x/war3mapSkin.w3u",
    ROOT / "map.w3x/war3map.w3a",
    ROOT / "map.w3x/war3mapSkin.w3a",
    ROOT / "map.w3x/war3map.w3q",
    ROOT / "map.w3x/war3mapSkin.w3q",
    ROOT / "map.w3x/war3map.w3h",
    ROOT / "map.w3x/war3mapSkin.w3h",
    ROOT / "map.w3x/war3map.w3t",
    ROOT / "map.w3x/war3mapSkin.w3t",
]

found_counts = {k: 0 for k in bld_wts}
for bf in bin_files:
    if not bf.exists(): continue
    raw = bf.read_bytes()
    for sid in bld_wts:
        target = f"TRIGSTR_{sid}".encode('utf-8')
        count = raw.count(target)
        if count > 0:
            found_counts[sid] += count

print("Usage counts across all binary object files:")
for sid, cnt in sorted(found_counts.items()):
    print(f"  TRIGSTR_{sid}: {cnt} usages")
