# -*- coding: utf-8 -*-
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

wts_keys = [
    14143, 14144, 6490,   # h070
    14153, 14154, 20481,  # h077
    14145, 14146, 11989,  # h073
    14147, 14148, 11990,  # h074
    14149, 14150, 19556,  # h075
    14151, 14152, 20476,  # h076
    14157, 14158, 20488,  # h079
    14159, 14160, 20627,  # h07S
    14186, 14187, 18417,  # o016
    14184, 14185, 20646,  # h0D7
]

print(f"Total building keys to check: {len(wts_keys)}")
sids = [f"TRIGSTR_{k}".encode("ascii") for k in wts_keys]

map_dir = ROOT / "map.w3x"
for f in map_dir.glob("war3map*.*"):
    if f.suffix in [".w3u", ".w3a", ".w3q", ".w3h", ".w3t", ".w3b", ".w3d"]:
        data = f.read_bytes()
        for k, sid in zip(wts_keys, sids):
            cnt = data.count(sid)
            if cnt > 1:
                print(f"WARNING: {f.name} has TRIGSTR_{k} occurring {cnt} times!")
            elif cnt == 1:
                pass
print("Check completed.")
