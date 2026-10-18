import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw

def main():
    b_data = json.load(open(ROOT / "docs/ui_text/elements_buildings.json", encoding="utf-8"))["buildings"]
    u_data = json.load(open(ROOT / "docs/ui_text/elements_units.json", encoding="utf-8"))["units"]

    all_ids = [b["id"] for b in b_data] + [u["id"] for u in u_data]
    args = [
        "get-objects-bulk",
        "--map", str(hw.DEFAULT_MAP),
        "--warcraft", str(hw.DEFAULT_WARCRAFT),
        "--type", "unit",
        "--ids", ",".join(all_ids),
        "--fields", "abillist,abilskinlist"
    ]
    data = hw.run_cli_json(args)
    obj_abils = {}
    for obj in data.get("objects", []):
        f = obj.get("fields", {})
        abils = [a.strip() for a in f.get("abillist", "").split(",") if a.strip()]
        abils += [a.strip() for a in f.get("abilskinlist", "").split(",") if a.strip()]
        obj_abils[obj["id"]] = abils

    all_unique = sorted(set(a for ab in obj_abils.values() for a in ab))
    print(f"Total unique abilities on Elements units/buildings: {len(all_unique)}")

    # Fetch details for each ability
    args2 = [
        "get-objects-bulk",
        "--map", str(hw.DEFAULT_MAP),
        "--warcraft", str(hw.DEFAULT_WARCRAFT),
        "--type", "ability",
        "--ids", ",".join(all_unique)
    ]
    data2 = hw.run_cli_json(args2)
    wts = hw.load_wts_strings()
    resolve = lambda s: wts.get(int(s[8:]), s) if isinstance(s, str) and s.startswith("TRIGSTR_") else s

    abil_details = {}
    for obj in data2.get("objects", []):
        aid = obj["id"]
        f = obj.get("fields", {})
        # check which units have it
        carriers = [uid for uid, alist in obj_abils.items() if aid in alist]
        abil_details[aid] = {
            "id": aid,
            "name": resolve(f.get("name", "")),
            "raw_name": f.get("name", ""),
            "tip1": resolve(f.get("tip1", "")),
            "raw_tip1": f.get("tip1", ""),
            "ubertip1": resolve(f.get("ubertip1", "")),
            "raw_ubertip1": f.get("ubertip1", ""),
            "hotkey": f.get("hotkey", ""),
            "buttonpos": f.get("buttonpos", ""),
            "buttonpos2": f.get("buttonpos2", ""),
            "buff1": f.get("buff1", ""),
            "carriers": carriers
        }

    out_file = ROOT / "docs/ui_text/elements_unit_abils_raw.json"
    out_file.write_text(json.dumps(abil_details, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved raw details to {out_file}")

    for aid, info in sorted(abil_details.items()):
        name = info["name"]
        carriers = ", ".join(info["carriers"])
        print(f"[{aid}] {name} (Carriers: {carriers})")
        if info["tip1"]:
            print(f"  Tip: {info['tip1']}")
        if info["ubertip1"]:
            print(f"  Ubertip: {info['ubertip1'][:100]}...")

if __name__ == "__main__":
    main()
