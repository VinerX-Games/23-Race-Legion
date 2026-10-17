"""Overlay placed doodad footprints on a temporary WPM, then query HiveWE pathing."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import struct
import subprocess
from pathlib import Path

from PIL import Image

from wc3_project import CACHE, settings, read
from wc3_object_tools import cli, require, compact_output


class Reader:
    def __init__(self, data):
        self.data, self.offset = data, 0

    def take(self, size):
        end = self.offset + size
        if end > len(self.data):
            raise ValueError("Truncated Warcraft binary file")
        result = self.data[self.offset:end]; self.offset = end
        return result

    def number(self, format="I"):
        return struct.unpack("<" + format, self.take(struct.calcsize("<" + format)))[0]


def placed_doodads(data, skins):
    reader = Reader(data)
    if reader.take(4) != b"W3do":
        raise ValueError("Not a doodad placement file")
    version = reader.number(); reader.number()
    if version not in (7, 8, 13):
        raise ValueError(f"Unsupported doodad version {version}")
    count = reader.number()
    if count > 1000000:
        raise ValueError("Invalid doodad count")
    result = []
    for _ in range(count):
        rawcode = reader.take(4).decode("ascii")
        reader.number()
        x, y, z, angle, sx, sy, sz = struct.unpack("<7f", reader.take(28))
        if skins:
            reader.take(4)
        if version >= 13:
            reader.number()
        state, life = reader.number("B"), reader.number("B")
        if version >= 8:
            reader.number("i")
            sets = reader.number()
            if sets > 100000:
                raise ValueError("Invalid item-set count")
            for _ in range(sets):
                items = reader.number()
                if items > 100000:
                    raise ValueError("Invalid drop-item count")
                reader.take(items * 8)
        if version >= 13:
            reader.number()
        creation = reader.number()
        if version >= 13:
            reader.take(8)
            lights = reader.number()
            if lights > 100000:
                raise ValueError("Invalid doodad light count")
            reader.take(lights * 36)
        result.append({"id": rawcode, "x": x, "y": y, "angle": angle,
                       "state": state, "life": life, "creation": creation})
    return result


def terrain_offset(data):
    reader = Reader(data)
    if reader.take(4) != b"W3E!":
        raise ValueError("Not a terrain file")
    reader.number(); reader.take(1); reader.number()
    ground = reader.number(); reader.take(ground * 4)
    cliffs = reader.number(); reader.take(cliffs * 4)
    reader.take(8)
    return reader.number("f"), reader.number("f")


def game_has_skins(data):
    reader = Reader(data)
    version = reader.number()
    if version not in (15, 18, 25, 28, 31, 32, 33, 39):
        raise ValueError(f"Unsupported map-info version {version}")
    if version < 28:
        return False
    reader.take(8)
    return reader.number() * 100 + reader.number() >= 132


def footprint(path):
    with Image.open(path) as image:
        image = image.convert("RGB")
        pixels = image.get_flattened_data()
        flags = bytes((2 if red > 250 else 0) | (4 if green > 250 else 0) |
                      (8 if blue > 250 else 0) for red, green, blue in pixels)
        return image.width, image.height, flags


def blit(cells, width, height, x, y, angle, texture):
    tw, th, flags = texture
    degrees = (math.degrees(angle) + 90) % 360
    rotation = round(degrees / 90) * 90 % 360
    if min(abs(degrees - rotation), abs(degrees - rotation - 360)) > 0.1:
        if tw == th and len(set(flags)) == 1:
            rotation = 0  # a uniform square is invariant to its visual rotation
        else:
            raise ValueError("Non-cardinal asymmetric footprint; cannot model it exactly")
    dw, dh = (th, tw) if rotation % 180 else (tw, th)
    changes = 0
    for j in range(th):
        for i in range(tw):
            xx, yy = i, j
            if rotation == 90:
                xx, yy = th - 1 - j, i
            elif rotation == 180:
                xx, yy = tw - 1 - i, th - 1 - j
            elif rotation == 270:
                xx, yy = j, tw - 1 - i
            xx, yy = int(x + xx - dw // 2), int(y + yy - dh // 2)
            if 0 <= xx < width and 0 <= yy < height:
                offset = yy * width + xx
                before = cells[offset]
                cells[offset] |= flags[(th - 1 - j) * tw + i]
                changes += cells[offset] != before
    return changes


def build_overlay(root):
    root = Path(root)
    config = settings()
    key = hashlib.sha256()
    for name in ("war3map.wpm", "war3map.w3e", "war3map.doo", "war3map.w3i", "war3map.w3d", "war3map.w3b"):
        file = root / name
        key.update(name.encode()); key.update(file.read_bytes() if file.exists() else b"missing")
    build_info = Path(config["warcraft"]) / ".build.info"
    key.update(build_info.read_bytes())
    key.update(Path(config["cli"]).read_bytes())
    key.update(b"placed-overlay-v1")
    stage = CACHE / "pathing" / key.hexdigest()
    summary_path = stage / "overlay.json"
    if summary_path.exists():
        summary = json.loads(read(summary_path))
        unchanged = all((root / asset["path"]).exists() and
                        hashlib.sha256((root / asset["path"]).read_bytes()).hexdigest() == asset["sha256"]
                        for asset in summary.get("local_assets", []))
        if unchanged:
            return stage, summary
    stage.mkdir(parents=True, exist_ok=True)
    instances = placed_doodads((root / "war3map.doo").read_bytes(), game_has_skins((root / "war3map.w3i").read_bytes()))
    ids = sorted({i["id"] for i in instances if i["state"] == 2 and i["life"] > 0})
    paths = {}
    for kind in ("doodad", "destructible"):
        for offset in range(0, len(ids), 100):
            data = require(cli(["get-objects-bulk", "--type", kind, "--ids", ",".join(ids[offset:offset + 100]),
                                "--fields", "pathtex"], root))
            for obj in data["objects"]:
                paths[obj["id"]] = obj["fields"].get("pathtex", "").strip()
    unknown = sorted(set(ids) - set(paths))
    if unknown:
        raise ValueError(f"Unknown placed objects: {unknown[:10]}")
    textures = {}
    local_assets = []
    env = {**os.environ, "WC3_DIR": config["warcraft"], "MDLXL_HOME": config["mdlxl_home"]}
    for asset in sorted(set(paths.values()) - {"", "_", "none", "None"}):
        local = (root / asset.replace("\\", "/")).resolve()
        if not local.is_relative_to(root.resolve()):
            raise ValueError("Footprint path escapes map")
        if local.is_file():
            source = local
            local_assets.append({"path": str(local.relative_to(root.resolve())),
                                 "sha256": hashlib.sha256(local.read_bytes()).hexdigest()})
        else:
            source = stage / (hashlib.sha256(asset.encode()).hexdigest() + Path(asset).suffix)
            if not source.exists():
                proc = subprocess.run(["node", config["model_cli"], "casc-get", asset, str(source)],
                                      capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=60)
                if proc.returncode or not source.exists():
                    raise ValueError(f"Cannot resolve footprint: {asset}: {proc.stderr[:200]}")
        textures[asset] = footprint(source)
    data = (root / "war3map.wpm").read_bytes()
    if data[:4] != b"MP3W":
        raise ValueError("Not a pathing map")
    width, height = struct.unpack_from("<II", data, 8)
    if len(data) != 16 + width * height:
        raise ValueError("Invalid WPM size")
    cells = bytearray(data[16:])
    ox, oy = terrain_offset((root / "war3map.w3e").read_bytes())
    applied, changed = 0, 0
    for instance in instances:
        asset = paths.get(instance["id"])
        if instance["state"] != 2 or instance["life"] <= 0 or asset not in textures:
            continue
        changed += blit(cells, width, height, (instance["x"] - ox) / 32,
                        (instance["y"] - oy) / 32, instance["angle"], textures[asset])
        applied += 1
    (stage / "war3map.wpm").write_bytes(data[:16] + cells)
    shutil.copy2(root / "war3map.w3e", stage / "war3map.w3e")
    summary = {"placed": len(instances), "applied": applied, "textures": len(textures), "changed_cells": changed,
               "local_assets": local_assets,
               "limitations": ["Initial placement only; live destroyed trees, opened gates, units and scripted obstacles are not synchronized."]}
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return stage, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("path", "islands"))
    parser.add_argument("--from", dest="origin")
    parser.add_argument("--to", dest="target")
    parser.add_argument("--move", choices=("foot", "water", "amphibious", "fly"), default="foot")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if args.limit < 1 or (args.command == "path" and not (args.origin and args.target)):
        parser.error("positive limit and path endpoints are required")
    try:
        stage, summary = build_overlay(settings()["map"])
        command = ["pathing-" + args.command, "--move", args.move]
        if args.command == "path":
            command += ["--from", args.origin, "--to", args.target]
        else:
            command += ["--limit", str(args.limit), "--min-cells", "100"]
        result = cli(command, stage)
        result["placed_obstacles"] = summary
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        result = {"ok": False, "error": str(exc)}
    CACHE.mkdir(parents=True, exist_ok=True)
    artifact = CACHE / "pathing-report.json"
    artifact.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    output = compact_output(result, args.limit)
    output["artifact"] = str(artifact)
    print(json.dumps(output, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
