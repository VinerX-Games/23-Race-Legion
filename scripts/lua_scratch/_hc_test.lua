-- Empirically test SetPlayerHandicap on a real bot unit's max HP.
local pi = 1
local p = Player(pi)
-- pick first alive non-structure unit
local g = CreateGroup()
GroupEnumUnitsOfPlayer(g, p, nil)
local sz = BlzGroupGetSize(g)
local u = nil
for i = 0, sz - 1 do
    local x = BlzGroupUnitAt(g, i)
    if x ~= nil and GetUnitState(x, UNIT_STATE_LIFE) > 0.405
        and not IsUnitType(x, UNIT_TYPE_STRUCTURE) then u = x; break end
end
DestroyGroup(g)
if u == nil then return "no unit found for P" .. pi end
local name = GetUnitName(u)

local function hpAt(h)
    SetPlayerHandicap(p, h)
    return BlzGetUnitMaxHP(u)
end
local hp100 = hpAt(1.0)
local hp150 = hpAt(1.5)
local hp200 = hpAt(2.0)
-- damage handicap getter (if present)
local dmgGet = (GetPlayerHandicapDamage ~= nil) and GetPlayerHandicapDamage(p) or -1
SetPlayerHandicap(p, 1.5)  -- restore test value
return "P" .. pi .. " unit=" .. name
    .. " | maxHP @100%=" .. hp100 .. " @150%=" .. hp150 .. " @200%=" .. hp200
    .. " | handicapDamage getter=" .. tostring(dmgGet)
