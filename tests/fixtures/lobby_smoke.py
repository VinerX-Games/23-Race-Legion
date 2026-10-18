import re
import sys
from pathlib import Path
from lupa.lua53 import LuaRuntime

ROOT = Path(__file__).resolve().parents[2]
jdir = ROOT / 'jass'
natives = {}
consts = []
for f in sorted(Path(jdir).glob('*')):
    t = f.read_text(encoding='utf-8', errors='replace')
    for m in re.finditer(r'^\s*(?:constant\s+)?(?:native|function)\s+(\w+)\s+takes\s+.*?\s+returns\s+(\w+)', t, re.M):
        natives.setdefault(m.group(1), m.group(2))
    for block in re.findall(r'^globals(.*?)^endglobals', t, re.M | re.S):
        for m in re.finditer(r'^\s*(?:constant\s+)?(\w+)\s+(array\s+)?(\w+)\s*(?:=\s*(.+?))?\s*(?://.*)?$', block, re.M):
            consts.append((m.group(1), bool(m.group(2)), m.group(3), m.group(4)))

lua = LuaRuntime(unpack_returned_tuples=True)
lua.execute(r'''
HANDLE_N = 0
CALLBACKS = {}
LOBBY_EXPIRY_TRIGGERS = {}
function __handle(kind)
    HANDLE_N = HANDLE_N + 1
    return setmetatable({__kind = kind, __id = HANDLE_N}, {__tostring = function(s) return kind .. '#' .. s.__id end})
end
function __default(rt)
    if rt == 'integer' then return 0
    elseif rt == 'real' then return 0.0
    elseif rt == 'boolean' then return false
    elseif rt == 'string' then return ''
    elseif rt == 'nothing' then return nil
    elseif rt == 'code' then return nil
    else return __handle(rt) end
end
function __guarded(fn, limit)
    debug.sethook(function()
        local info = debug.getinfo(2, 'Sl')
        error('INSTRUCTION LIMIT at ' .. tostring(info and info.short_src) .. ':' .. tostring(info and info.currentline))
    end, '', limit or 10000000)
    local ok, e = xpcall(fn, debug.traceback)
    debug.sethook()
    return ok, e
end
function __mkstub(name, rt)
    return function(...)
        return __default(rt)
    end
end
''')
mk = lua.globals().__mkstub
G = lua.globals()
for name, rt in natives.items():
    G[name] = mk(name, rt)

lua.execute(r'''
function GetPlayerNeutralPassive() return 27 end
function GetPlayerNeutralAggressive() return 24 end
function GetBJMaxPlayers() return 24 end
function GetBJMaxPlayerSlots() return 28 end
function GetBJPlayerNeutralVictim() return 25 end
function GetBJPlayerNeutralExtra() return 26 end
function FourCC(s) return (s:byte(1) << 24) + (s:byte(2) << 16) + (s:byte(3) << 8) + s:byte(4) end
function GetHandleId(h) if type(h) == 'table' then return h.__id or 0 end return 0 end
PLAYERS = {}
for i = 0, 27 do PLAYERS[i] = __handle('player'); PLAYERS[i].__pid = i end
function Player(i) return PLAYERS[i] or __handle('player') end
function GetPlayerId(p) return type(p) == 'table' and p.__pid or 0 end
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
function InitHashtable() return __handle('hashtable') end
function OrderId(s) return 851971 end
function OrderId2String(i) return '' end
function GetObjectName(i) return 'obj' end
function GetPlayerName(p) return 'player' end
function GetLocalPlayer() return Player(0) end
function BlzGetFrameByName() return __handle('framehandle') end
function Condition(f) local h = __handle('conditionfunc'); h.__fn = f; return h end
Filter = Condition
function CreateGroup() return __handle('group') end
function GetPlayerController(p)
    local pid = GetPlayerId(p)
    if pid == 0 then return MAP_CONTROL_USER end
    return MAP_CONTROL_COMPUTER
end
function GetPlayerSlotState(p) return PLAYER_SLOT_STATE_PLAYING end
function TriggerRegisterTimerExpireEventBJ(trig, timer)
    LOBBY_EXPIRY_TRIGGERS[#LOBBY_EXPIRY_TRIGGERS + 1] = {trig = trig, timer = timer}
end
function TriggerAddAction(trig, action)
    trig.__action = action
end
function TriggerAddCondition(trig, cond)
    trig.__cond = cond
end
''')

# Constants
const_lua = []
for typ, is_arr, name, val in consts:
    if is_arr:
        const_lua.append(f'{name} = {{}}')
        continue
    if val is None: continue
    v = val.strip()
    m = re.match(r'(Convert\w+)\(\s*(-?\d+)\s*\)$', v)
    if m:
        const_lua.append(f'{name} = __handle("{typ}"); {name}.__v = {m.group(2)}')
    elif re.match(r'^-?\d+(\.\d+)?$', v) or v in ('true', 'false', 'null'):
        const_lua.append(f'{name} = {"nil" if v == "null" else v}')
    elif re.match(r"^'(.{4})'$", v):
        const_lua.append(f'{name} = FourCC("{v[1:5]}")')
    elif re.match(r'^"', v):
        const_lua.append(f'{name} = {v}')
    else:
        expr = re.sub(r' null ', 'nil', v).replace('!=', '~=')
        expr = re.sub(r"'(.{4})'", lambda m: f'FourCC("{m.group(1)}")', expr)
        const_lua.append(f'{name} = {expr}')
for line in const_lua:
    try: lua.execute(line)
    except: pass

lua.execute('if MAP_CONTROL_USER == nil then MAP_CONTROL_USER = __handle("mapcontrol") end')
lua.execute('if MAP_CONTROL_COMPUTER == nil then MAP_CONTROL_COMPUTER = __handle("mapcontrol") end')

code = (ROOT / 'map.w3x/war3map.lua').read_text(encoding='utf-8-sig')
load_fn = lua.eval(r'''function(code)
    local chunk, err = load(code, "=war3map.lua")
    if not chunk then return "COMPILE: " .. tostring(err) end
    local ok, e = __guarded(chunk)
    if not ok then return "LOAD: " .. tostring(e) end
    -- Allmap must exist before preplaced units are created, and keep its identity.
    -- Moving CreateRegion into InitGlobals caused the fec12de movement regression.
    if Allmap == nil then return "ORDER: Allmap missing before main" end
    local allmapBeforeMain = Allmap
    if main then
        local ok2, e2 = __guarded(main)
        if not ok2 then return "MAIN: " .. tostring(e2) end
    end
    if Allmap ~= allmapBeforeMain then return "ORDER: Allmap replaced during main" end
    return "ok"
end''')
res = load_fn(code)
if res != 'ok':
    raise AssertionError(res)

test_lobby = lua.eval(r'''function()
    local fired = 0
    for i, entry in ipairs(LOBBY_EXPIRY_TRIGGERS) do
        local tr = entry.trig
        local isLobby = (entry.timer == udg_LobbyTime)
        if isLobby then
            fired = fired + 1
            print(string.format("Firing lobby trigger #%d (timer==udg_LobbyTime)", i))
            if tr.__action then
                local ok, err = __guarded(tr.__action)
                if not ok then
                    error("lobby trigger: " .. tostring(err))
                else
                    print("  Trigger action OK")
                end
            end
        end
    end
    assert(fired > 0, "no lobby expiry triggers registered")
    return fired
end''')
print('Lobby triggers passed:', test_lobby())
