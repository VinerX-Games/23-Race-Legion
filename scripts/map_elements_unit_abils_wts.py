import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def main():
    abils = [
        'A01N', 'A01R', 'A01S', 'A0CE', 'A0I3', 'A0OZ', 'A0PG', 'A0PH', 'A0Q8', 'A0Q9',
        'A0QA', 'A0QC', 'A0QD', 'A0QE', 'A0QF', 'A0QG', 'A0QH', 'A0QI', 'A0QM',
        'A0W7', 'A0W8', 'A0W9', 'A0WA', 'A18B', 'A1MQ', 'Adis'
    ]
    buffs = ['B008', 'B054', 'B055', 'B056', 'B071']

    data_a = hw.run_cli_json([
        'get-objects-bulk',
        '--map', str(hw.DEFAULT_MAP),
        '--warcraft', str(hw.DEFAULT_WARCRAFT),
        '--type', 'ability',
        '--ids', ','.join(abils)
    ])
    data_b = hw.run_cli_json([
        'get-objects-bulk',
        '--map', str(hw.DEFAULT_MAP),
        '--warcraft', str(hw.DEFAULT_WARCRAFT),
        '--type', 'buff',
        '--ids', ','.join(buffs)
    ])

    wts_dict = hw.load_wts_strings()
    
    mapping = {}
    for obj in data_a.get("objects", []):
        aid = obj["id"]
        f = obj.get("fields", {})
        mapping[aid] = {
            "type": "ability",
            "name": {"raw": f.get("name"), "wts_id": int(f.get("name")[8:]) if f.get("name", "").startswith("TRIGSTR_") else None},
            "tip1": {"raw": f.get("tip1"), "wts_id": int(f.get("tip1")[8:]) if f.get("tip1", "").startswith("TRIGSTR_") else None},
            "ubertip1": {"raw": f.get("ubertip1"), "wts_id": int(f.get("ubertip1")[8:]) if f.get("ubertip1", "").startswith("TRIGSTR_") else None},
            "hotkey": f.get("hotkey")
        }

    for obj in data_b.get("objects", []):
        bid = obj["id"]
        f = obj.get("fields", {})
        mapping[bid] = {
            "type": "buff",
            "bufftip": {"raw": f.get("bufftip"), "wts_id": int(f.get("bufftip")[8:]) if f.get("bufftip", "").startswith("TRIGSTR_") else None},
            "buffubertip": {"raw": f.get("buffubertip"), "wts_id": int(f.get("buffubertip")[8:]) if f.get("buffubertip", "").startswith("TRIGSTR_") else None}
        }

    out_file = ROOT / "docs/ui_text/elements_unit_abils_wts_map.json"
    out_file.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved mapping to {out_file}")

    for k, v in mapping.items():
        print(f"[{k}] ({v['type']}):")
        for field, fv in v.items():
            if field != "type":
                print(f"   {field}: {fv}")

if __name__ == "__main__":
    main()
