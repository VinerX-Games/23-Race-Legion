"""Smoke-run war3map.lua under Lua 5.3 with auto-generated WC3 native stubs.

Usage: python -I init_smoke.py <war3map.lua> <jass_dir>
Every native / BJ function becomes a stub returning a default for its declared
return type; handles are unique tables. Runs config(), main(), then fires all
registered timers/trigger callbacks once (best-effort) and reports Lua errors.
"""
import re
import sys
from pathlib import Path

from lupa.lua53 import LuaRuntime

src, jdir = sys.argv[1:3]
natives = {}
consts = []
for f in sorted(Path(jdir).glob("*")):
    t = f.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r"^\s*(?:constant\s+)?(?:native|function)\s+(\w+)\s+takes\s+.*?\s+returns\s+(\w+)", t, re.M):
        natives.setdefault(m.group(1), m.group(2))
    for block in re.findall(r"^globals(.*?)^endglobals", t, re.M | re.S):
        for m in re.finditer(r"^\s*(?:constant\s+)?(\w+)\s+(array\s+)?(\w+)\s*(?:=\s*(.+?))?\s*(?://.*)?$", block, re.M):
            consts.append((m.group(1), bool(m.group(2)), m.group(3), m.group(4)))

lua = LuaRuntime(unpack_returned_tuples=True)
lua.execute(r"""
HANDLE_N = 0
CALLBACKS = {}        -- every function handed to an engine API
ERRORS = {}
function __handle(kind)
    HANDLE_N = HANDLE_N + 1
    return setmetatable({__kind = kind, __id = HANDLE_N}, {__tostring = function(s) return kind .. "#" .. s.__id end})
end
function __default(rt)
    if rt == "integer" then return 0
    elseif rt == "real" then return 0.0
    elseif rt == "boolean" then return false
    elseif rt == "string" then return ""
    elseif rt == "nothing" then return nil
    elseif rt == "code" then return nil
    else return __handle(rt) end
end
-- Лимит инструкций на один вызов: стабы не меняют состояние, и циклы вида
-- `while not Cond() do` иначе крутятся вечно.
function __guarded(fn, limit)
    debug.sethook(function()
        local info = debug.getinfo(2, "Sl")
        error("INSTRUCTION LIMIT at " .. tostring(info and info.short_src) .. ":" .. tostring(info and info.currentline))
    end, "", limit or 20000000)
    local ok, e = xpcall(fn, debug.traceback)
    debug.sethook()
    return ok, e
end
function __mkstub(name, rt)
    return function(...)
        for i = 1, select("#", ...) do
            local a = select(i, ...)
            if type(a) == "function" then CALLBACKS[#CALLBACKS + 1] = {name = name, fn = a} end
        end
        return __default(rt)
    end
end
""")
mk = lua.globals().__mkstub
G = lua.globals()
for name, rt in natives.items():
    G[name] = mk(name, rt)
# Lua-only natives in Reforged
lua.execute(r"""
function GetPlayerNeutralPassive() return 27 end
function GetPlayerNeutralAggressive() return 24 end
function GetBJMaxPlayers() return 24 end
function GetBJMaxPlayerSlots() return 28 end
function GetBJPlayerNeutralVictim() return 25 end
function GetBJPlayerNeutralExtra() return 26 end
function FourCC(s) return (s:byte(1) << 24) + (s:byte(2) << 16) + (s:byte(3) << 8) + s:byte(4) end
function GetHandleId(h) if type(h) == "table" then return h.__id or 0 end return 0 end
function Player(i) PLAYERS = PLAYERS or {}; if not PLAYERS[i] then PLAYERS[i] = __handle("player"); PLAYERS[i].__pid = i end return PLAYERS[i] end
function GetPlayerId(p) return type(p) == "table" and p.__pid or 0 end
function GetRandomInt(a, b) return a end
function GetRandomReal(a, b) return a end
function I2S(i) return tostring(math.tointeger(i) or i) end
function R2S(r) return tostring(r) end
function R2I(r) return math.tointeger(r >= 0 and math.floor(r) or math.ceil(r)) end
function I2R(i) return i + 0.0 end
function S2I(s) return math.tointeger(tonumber(s) or 0) or 0 end
function S2R(s) return tonumber(s) or 0.0 end
function StringLength(s) return #s end
function SubString(s, a, b) return string.sub(s, a + 1, b) end
function StringCase(s, up) return up and s:upper() or s:lower() end
function StringHash(s) local h = 0 for i = 1, #s do h = (h * 31 + s:byte(i)) & 0x7fffffff end return h end
function SquareRoot(x) return math.sqrt(math.max(x, 0)) end
function Atan2(y, x) return math.atan(y, x) end
function Sin(x) return math.sin(x) end
function Cos(x) return math.cos(x) end
function Pow(a, b) return a ^ b end
function ModuloInteger(a, b) return a % b end
function InitHashtable() return __handle("hashtable") end
function OrderId(s) return 851971 end
function OrderId2String(i) return "" end
function GetObjectName(i) return "obj" end
function GetPlayerName(p) return "player" end
function GetLocalPlayer() return Player(0) end
function BlzGetFrameByName() return __handle("framehandle") end
function Condition(f) local h = __handle("conditionfunc"); h.__fn = f; CALLBACKS[#CALLBACKS+1] = {name="Condition", fn=f}; return h end
Filter = Condition
function CreateGroup() return __handle("group") end
function GetPlayerController(p) return MAP_CONTROL_USER end
function GetPlayerSlotState(p) return PLAYER_SLOT_STATE_PLAYING end
""")

# constants / BJ globals
const_lua = []
for typ, is_arr, name, val in consts:
    if is_arr:
        const_lua.append(f"{name} = {{}}")
        continue
    if val is None:
        continue
    v = val.strip()
    m = re.match(r"(Convert\w+)\(\s*(-?\d+)\s*\)$", v)
    if m:
        const_lua.append(f"{name} = __handle('{typ}'); {name}.__v = {m.group(2)}")
    elif re.match(r"^-?\d+(\.\d+)?$", v) or v in ("true", "false", "null"):
        const_lua.append(f"{name} = {'nil' if v == 'null' else v}")
    elif re.match(r"^'(.{4})'$", v):
        const_lua.append(f"{name} = FourCC('{v[1:5]}')")
    elif re.match(r'^"', v):
        const_lua.append(f"{name} = {v}")
    else:
        expr = re.sub(r"null", "nil", v).replace("!=", "~=")
        expr = re.sub(r"'(.{4})'", lambda m: f"FourCC('{m.group(1)}')", expr)
        const_lua.append(f"{name} = {expr}")
for line in const_lua:
    try:
        lua.execute(line)
    except Exception:
        pass
lua.execute("if MAP_CONTROL_USER == nil then MAP_CONTROL_USER = __handle('mapcontrol') end")

code = Path(src).read_text(encoding="utf-8-sig")
run = lua.eval(r"""function(code)
    local chunk, err = load(code, "=war3map.lua")
    if not chunk then return "COMPILE: " .. tostring(err) end
    local ok, e = __guarded(chunk, 200000000)
    if not ok then return "LOAD: " .. tostring(e) end
    for _, f in ipairs({"config", "main"}) do
        if type(_G[f]) == "function" then
            local ok2, e2 = __guarded(_G[f], 200000000)
            if not ok2 then ERRORS[#ERRORS + 1] = f .. ": " .. tostring(e2) end
        end
    end
    return "ok"
end""")
stage = run(code)
print("stage:", stage)

fire = lua.eval(r"""function(rounds)
    local seen = {}
    local n = 0
    for r = 1, rounds do
        local list = CALLBACKS
        CALLBACKS = {}
        for _, cb in ipairs(list) do
            if not seen[cb.fn] then
                seen[cb.fn] = true
                n = n + 1
                local ok, e = __guarded(cb.fn)
                if not ok then ERRORS[#ERRORS + 1] = "[" .. cb.name .. "] " .. tostring(e) end
            end
        end
    end
    return n
end""")
print("callbacks fired:", fire(4))
errs = lua.globals().ERRORS
ie = lua.globals().InitErrors
seen = set()
out = []
for coll in (errs, ie):
    if coll is None:
        continue
    for i in range(1, len(coll) + 1):
        e = str(coll[i])
        key = re.sub(r"#\d+", "#", e)
        if key not in seen:
            seen.add(key)
            out.append(e)
print("unique errors:", len(out))
for e in out:
    print(" -", e[:1200])

raise SystemExit(1 if stage != "ok" or out else 0)
