#!/usr/bin/env python3
"""Agent <-> running-WC3 bridge: execute Lua live and read results back.

No map restart needed. Pairs with the in-map eval channel (BridgeConsumeEval).

Channel:
  IN  : sequential .pld files  <CustomMapData>/23race_eval_NNNN.pld
         payload sent via BlzSendSyncData inside the .pld, chunked if needed:
           eval|<seq>|<chunk_i>|<total>|<hex>
         + BlzSetAbilityTooltip flag so the game detects the file was loaded.
  OUT : fixed file              <CustomMapData>/23race_eval_out.pld
         payload  <seq>|<ok 0/1>|<base64-serialized-result>   (PreloadGenEnd)

Usage:
  python agent_bridge.py reset                 # call once after each map launch
  python agent_bridge.py exec "return AiRace[1]"
  python agent_bridge.py exec --file snippet.lua
  python agent_bridge.py exec "..." --timeout 12
"""
import sys, os, re, time, glob, argparse

# Russian Windows consoles default to cp1251 and crash on UTF-8 output; force UTF-8.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

CMD_DIR = os.path.join(os.environ["USERPROFILE"], "Documents", "Warcraft III", "CustomMapData")
EVAL_OUT = os.path.join(CMD_DIR, "23race_eval_out.pld")
IN_GLOB = os.path.join(CMD_DIR, "23race_eval_[0-9]*.pld")
IN_RE = re.compile(r"23race_eval_(\d+)\.pld$", re.I)

# BlzSendSyncData payload limit ~255 chars. We keep hex chunks at 200 to stay safe.
HEX_CHUNK = 200

# .pld template: BlzSendSyncData calls for chunked payload + BlzSetAbilityTooltip flag.
# The tooltip flag lets the game detect the file was loaded and advance EvalNextSeq.
PLD_TEMPLATE = (
    "function PreloadFiles takes nothing returns nothing\n"
    "\r\n"
    "\tcall PreloadStart()\r\n"
    '\tcall Preload( "")\n'
    "{chunk_calls}"
    '\tcall Preload("" )\r\n'
    "\tcall PreloadEnd( 0.0 )\r\n"
    "\n"
    "endfunction\n\n\r\n"
)


def write_pld(path, seq, hex_code):
    total = max(1, (len(hex_code) + HEX_CHUNK - 1) // HEX_CHUNK)
    calls = []
    for i in range(total):
        chunk = hex_code[i * HEX_CHUNK : (i + 1) * HEX_CHUNK]
        calls.append(
            'call BlzSendSyncData("23RaceEval","eval|%d|%d|%d|%s")\n' % (seq, i + 1, total, chunk)
        )
    calls.append("call BlzSetAbilityTooltip('AHbz',\"loaded\",0)\n")
    with open(path, "wb") as f:
        f.write(PLD_TEMPLATE.format(chunk_calls="".join(calls)).encode("utf-8"))


def next_seq():
    """Stateless: next inbox seq = (max existing inbox file)+1. Self-syncs with a fresh game after reset()."""
    n = 0
    for p in glob.glob(IN_GLOB):
        m = IN_RE.search(os.path.basename(p))
        if m:
            n = max(n, int(m.group(1)))
    return n + 1


def _dechex(hexstr):
    try:
        return bytes.fromhex(hexstr).decode("utf-8", errors="replace")
    except Exception:
        return "<undecodable hex len=%d>" % len(hexstr)


def parse_out(want_seq):
    """Return (seq, ok, value) for want_seq once ALL result chunks are present, else None.

    Chunked format (current):  <seq>|<ok>|<idx>|<total>|<hexchunk>
    Legacy format (fallback):  <seq>|<ok>|<hex>
    """
    if not os.path.exists(EVAL_OUT):
        return None
    try:
        data = open(EVAL_OUT, "r", encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    chunks, ok, total, legacy = {}, None, None, None
    for line in re.findall(r'Preload\(\s*"(.*?)"\s*\)', data):
        f = line.split("|")
        if len(f) < 3 or f[0] != str(want_seq):
            continue
        if len(f) >= 5 and f[2].isdigit() and f[3].isdigit():
            ok = f[1] == "1"
            total = int(f[3])
            chunks[int(f[2])] = f[4]
        elif len(f) == 3:
            legacy = (want_seq, f[1] == "1", f[2])
    if total is not None and len(chunks) >= total:
        return want_seq, ok, _dechex("".join(chunks.get(i, "") for i in range(1, total + 1)))
    if legacy is not None:
        return legacy[0], legacy[1], _dechex(legacy[2])
    return None


def cmd_reset():
    removed = 0
    for p in glob.glob(IN_GLOB) + [EVAL_OUT]:
        try:
            os.remove(p)
            removed += 1
        except OSError:
            pass
    print("reset: cleared %d bridge file(s)" % removed)
    return 0


def cmd_exec(code, timeout):
    seq = next_seq()
    try:
        os.remove(EVAL_OUT)  # drop stale result so we never read a previous one
    except OSError:
        pass
    hx = code.encode("utf-8").hex()
    write_pld(os.path.join(CMD_DIR, "23race_eval_%04d.pld" % seq), seq, hx)
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = parse_out(seq)
        if r and r[0] == seq:
            _, ok, val = r
            print(("OK   " if ok else "ERR  ") + val)
            return 0 if ok else 2
        time.sleep(0.2)
    print("TIMEOUT: no result for seq=%d within %ss (is the map running + reset done?)" % (seq, timeout))
    return 1


def main():
    ap = argparse.ArgumentParser(description="Live Lua bridge to running WC3 map")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("reset", help="clear bridge files; run once after each map launch")
    pe = sub.add_parser("exec", help="run a Lua snippet and print the result")
    pe.add_argument("code", nargs="?", default=None, help="Lua source (expression or statements)")
    pe.add_argument("--file", help="read Lua from a file instead")
    pe.add_argument("--timeout", type=float, default=8.0)
    a = ap.parse_args()
    if a.cmd == "reset":
        return cmd_reset()
    if a.cmd == "exec":
        code = open(a.file, "r", encoding="utf-8").read() if a.file else a.code
        if not code:
            ap.error("provide Lua code or --file")
        return cmd_exec(code, a.timeout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
