"""Apply audited WTS replacements while preserving all binary object data."""
import hashlib
import json
import re
import sys
from pathlib import Path

from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent


def apply_wts_batch(inventory_path):
    inventory_path = Path(inventory_path)
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    path = ROOT / "map.w3x/war3map.wts"
    original = path.read_bytes()
    updated = original
    replacements = {}
    for row in inventory["strings"]:
        reference = row["reference_before"]
        if not reference.startswith("TRIGSTR_"):
            raise ValueError("WTS-only batch cannot edit a literal field: " + reference)
        sid = int(reference[8:])
        if sid in replacements:
            assert replacements[sid] == row["after"], sid
            continue
        replacements[sid] = row["after"]
        pattern = re.compile(rb"(STRING\s+" + str(sid).encode() + rb"\s*\{\r?\n)(.*?)(\r?\n\})", re.S)
        matches = list(pattern.finditer(updated))
        assert len(matches) == 1, sid
        assert matches[0][2].decode("utf-8").replace("\r\n", "\n") == row["before"], sid
        updated = pattern.sub(lambda m: m[1] + row["after"].encode("utf-8") + m[3], updated)
    binaries = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in (ROOT / "map.w3x").glob("*.w3*") if p.is_file()}
    parse = lambda data: {int(m[1]): m[2] for m in re.finditer(rb"STRING\s+(\d+)\s*\{\r?\n(.*?)\r?\n\}", data, re.S)}
    before, raw_after = parse(original), parse(updated)
    assert before.keys() == raw_after.keys()
    changed = sorted(sid for sid in before if before[sid] != raw_after[sid])
    assert set(changed) <= replacements.keys()
    backup = ROOT / ".cache/wc3" / (inventory_path.stem + "_before.wts")
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_bytes(original)
    path.write_bytes(updated)
    after = load_wts_strings(path)
    assert all(after[sid] == value for sid, value in replacements.items())
    assert all(hashlib.sha256((ROOT / "map.w3x" / name).read_bytes()).hexdigest() == digest
               for name, digest in binaries.items())
    report = dict(ok=True, applied=True, method="WTS-only", changed_wts_ids=changed,
                  binary_sha256_unchanged=binaries, before_wts_sha256=hashlib.sha256(original).hexdigest(),
                  after_wts_sha256=hashlib.sha256(updated).hexdigest())
    inventory_path.with_name(inventory_path.stem + "_apply.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    report = apply_wts_batch(sys.argv[1])
    print(json.dumps(dict(ok=report["ok"], changed_strings=len(report["changed_wts_ids"]))))
