# -*- coding: utf-8 -*-
import json
from pathlib import Path

dump = json.loads(Path("scripts/nagi_raw_dump.json").read_text("utf-8"))

def check_obj(category, items):
    print(f"\n==================== {category.upper()} ({len(items)}) ====================")
    for it in items:
        oid = it.get('id')
        name = it.get('name')
        raw_name = it.get('raw_name')
        tip = it.get('tip')
        raw_tip = it.get('raw_tip')
        ubertip = it.get('ubertip')
        raw_ubertip = it.get('raw_ubertip')
        hotkey = it.get('hotkey')
        raw_hotkey = it.get('raw_hotkey')
        
        # for abilities/upgrades
        tips = it.get('tips', {})
        ubertips = it.get('ubertips', {})
        names = it.get('names', {})
        
        print(f"[{oid}] Name: {raw_name} -> {repr(name)}")
        if raw_tip or tip:
            print(f"      Tip: {raw_tip} -> {repr(tip)}")
        if raw_ubertip or ubertip:
            print(f"      Ubertip: {raw_ubertip} -> {repr(ubertip)[:100]}...")
        if raw_hotkey or hotkey:
            print(f"      Hotkey: {raw_hotkey} -> {repr(hotkey)}")
            
        if names:
            for k, v in names.items():
                print(f"      {k}: {v.get('raw')} (sid={v.get('sid')}) -> {repr(v.get('val'))}")
        if tips:
            for k, v in tips.items():
                print(f"      {k}: {v.get('raw')} (sid={v.get('sid')}) -> {repr(v.get('val'))}")
        if ubertips:
            for k, v in ubertips.items():
                print(f"      {k}: {v.get('raw')} (sid={v.get('sid')}) -> {repr(v.get('val'))[:80]}...")
                
        # check buffs
        if 'bufftip' in it:
            print(f"      bufftip: {it.get('raw_bufftip')} (sid={it.get('bufftip_sid')}) -> {repr(it.get('bufftip'))}")
            print(f"      buffubertip: {it.get('raw_buffubertip')} (sid={it.get('buffubertip_sid')}) -> {repr(it.get('buffubertip'))}")

if __name__ == '__main__':
    check_obj("selection", [dump['selection']])
    check_obj("selection_markers", dump['selection_markers'])
    check_obj("buildings", dump['buildings'])
    check_obj("worker", dump['worker'])
    check_obj("heroes", dump['heroes'])
    check_obj("units", dump['units'])
    check_obj("upgrades", dump['upgrades'])
    check_obj("abilities", dump['abilities'])
    check_obj("buffs", dump['buffs'])
