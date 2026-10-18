"""Apply the audited text-only batch without reserializing ability object data."""
import hashlib
import json
import re
from pathlib import Path

from wc3_hivewe import load_wts_strings

ROOT = Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / "docs/ui_text"
    inventory = json.loads((folder / "faceless_abilities_01.json").read_text(encoding="utf-8"))
    path = ROOT / "map.w3x/war3map.wts"
    original = path.read_bytes()
    updated = original
    replacements = {}
    for row in inventory["strings"]:
        reference = row["reference_before"]
        assert reference.startswith("TRIGSTR_"), reference
        sid = int(reference[8:])
        assert sid not in replacements, sid
        replacements[sid] = row["after"]
        pattern = re.compile(rb"(STRING\s+" + str(sid).encode() + rb"\s*\{\r?\n)(.*?)(\r?\n\})", re.S)
        matches = list(pattern.finditer(updated))
        assert len(matches) == 1, sid
        assert matches[0].group(2).decode("utf-8").replace("\r\n", "\n") == row["before"], sid
        updated = pattern.sub(lambda m: m[1] + row["after"].encode("utf-8") + m[3], updated)
    binaries = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in (ROOT / "map.w3x").glob("*.w3*") if p.is_file()}
    path.write_bytes(updated)
    before = {int(m[1]): m[2] for m in re.finditer(rb"STRING\s+(\d+)\s*\{\r?\n(.*?)\r?\n\}", original, re.S)}
    after = load_wts_strings(path)
    raw_after = {int(m[1]): m[2] for m in re.finditer(rb"STRING\s+(\d+)\s*\{\r?\n(.*?)\r?\n\}", updated, re.S)}
    assert before.keys() == raw_after.keys()
    changed = sorted(sid for sid, value in raw_after.items() if value != before[sid])
    assert changed == sorted(replacements), changed
    assert all(after[sid] == value for sid, value in replacements.items())
    assert all(hashlib.sha256((ROOT / "map.w3x" / name).read_bytes()).hexdigest() == digest
               for name, digest in binaries.items())
    report = dict(ok=True, applied=True, method="WTS-only; failed HiveWE transaction was not applied",
                  changed_wts_ids=changed, binary_sha256_unchanged=binaries)
    (folder / "faceless_abilities_01_wts_apply.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(ok=True, changed_wts_ids=changed)))


if __name__ == "__main__":
    main()
