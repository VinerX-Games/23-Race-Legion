-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/utils.lua — Core utility functions
-- ============================================================
-- Sources: LIBRARY_A1, LIBRARY_Global, LIBRARY_LibNewFunctions, LIBRARY_common
-- ============================================================

-- ============================================================
-- LIBRARY_A1: Enemy filter
-- ============================================================

function EnemEl()
    return GetOwningPlayer(GetFilterUnit()) ~= G.udg_LocalPlayer
end

-- ============================================================
-- LIBRARY_common: Enemy filter with counter
-- ============================================================

function isEnemy()
    G.udg_LocalInteger2 = G.udg_LocalInteger2 + 1
    return IsPlayerEnemy(GetOwningPlayer(GetFilterUnit()), G.udg_LocalPlayer)
end

-- ============================================================
-- LIBRARY_Global: Geometry & utility
-- ============================================================

function GetPosZ(x, y)
    MoveLocation(G.Global_TempLoc, x, y)
    return GetLocationZ(G.Global_TempLoc)
end

function GetUnitZ(u)
    return GetPosZ(GetUnitX(u), GetUnitY(u)) + GetUnitFlyHeight(u)
end

function SetUnitZ(u, z)
    SetUnitFlyHeight(u, z - GetPosZ(GetUnitX(u), GetUnitY(u)), 0)
end

-- Distance
function DistanceBetweenCoords(x1, y1, x2, y2)
    return math.sqrt((x2 - x1)^2 + (y2 - y1)^2)
end

function DistanceBetweenWidgetAndCoords(w, x, y)
    return math.sqrt((x - GetWidgetX(w))^2 + (y - GetWidgetY(w))^2)
end

function DistanceBetweenCoordsAndWidget(x, y, w)
    return math.sqrt((GetWidgetX(w) - x)^2 + (GetWidgetY(w) - y)^2)
end

function DistanceBetweenWidgets(w1, w2)
    return math.sqrt((GetWidgetX(w2) - GetWidgetX(w1))^2 + (GetWidgetY(w2) - GetWidgetY(w1))^2)
end

-- Angle
local RADTODEG = bj_RADTODEG
local DEGTORAD = bj_DEGTORAD

function AngleBetweenCoords(x1, y1, x2, y2)
    return math.atan(y2 - y1, x2 - x1) * RADTODEG
end

function AngleBetweenWidgetAndCoords(w, x, y)
    return math.atan(y - GetWidgetY(w), x - GetWidgetX(w)) * RADTODEG
end

function AngleBetweenCoordsAndWidget(x, y, w)
    return math.atan(GetWidgetY(w) - y, GetWidgetX(w) - x) * RADTODEG
end

function AngleBetweenWidgets(w1, w2)
    return math.atan(GetWidgetY(w2) - GetWidgetY(w1), GetWidgetX(w2) - GetWidgetX(w1)) * RADTODEG
end

-- Polar projection
function PolarProjectionX(x, d, a)
    return x + d * math.cos(a * DEGTORAD)
end

function PolarProjectionY(y, d, a)
    return y + d * math.sin(a * DEGTORAD)
end

-- Angle difference (shortest arc)
function AngleDifference(a, b)
    if a > 180 then a = a - 360
    elseif a < -180 then a = a + 360 end
    if b > 180 then b = b - 360
    elseif b < -180 then b = b + 360 end
    local r = math.max(a, b) - math.min(a, b)
    return math.min(r, 360 - r)
end

-- Bezier curves
function BezierCurves_2C(c1, c2, t)
    local u = 1 - t
    return c1 * u + c2 * t
end

function BezierCurves_3C(c1, c2, c3, t)
    local u = 1 - t
    return c1 * u * u + c2 * 2 * t * u + c3 * t * t
end

function BezierCurves_4C(c1, c2, c3, c4, t)
    local u = 1 - t
    return c1 * u^3 + c2 * 3 * t * u^2 + c3 * 3 * t^2 * u + c4 * t^3
end

-- Unit availability checks
function AvalibleUnit(u)
    return not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_ANCIENT) and UnitAlive(u)
end

function AvalibleUnitAlly(s, u)
    return IsUnitAlly(u, GetOwningPlayer(s)) and AvalibleUnit(u)
end

function AvalibleUnitEnemy(s, u)
    return IsUnitEnemy(u, GetOwningPlayer(s)) and AvalibleUnit(u)
end

-- Group operations
function GroupCountUnits(g)
    local count = 0
    ForGroup(g, function() count = count + 1 end)
    return count
end

function GroupRandomUnit(g)
    local count = GroupCountUnits(g)
    if count == 0 then return nil end
    local pick = GetRandomInt(1, count)
    local i = 0
    local result = nil
    ForGroup(g, function()
        i = i + 1
        if i == pick then result = GetEnumUnit() end
    end)
    return result
end

function KillDestructablesInRange(x, y, r, filter)
    local rect = Rect(x - r, y - r, x + r, y + r)
    EnumDestructablesInRect(rect, filter, function()
        if DistanceBetweenWidgetAndCoords(GetEnumDestructable(), x, y) <= r then
            KillDestructable(GetEnumDestructable())
        end
    end)
    RemoveRect(rect)
end

-- Order interrupt check
function InterruptOrderCheck(i)
    if i == 852002 or i == 852003 or i == 852004 or i == 852005 or i == 852006 or i == 852007 or i == 852537 or i > 1000000 then
        return false
    end
    return true
end

-- Temporary item addition
function UnitAddPowerUpItem(u, itemId)
    local it = CreateItem(itemId, GetUnitX(u), GetUnitY(u))
    local invAdded = false
    local added = true
    if GetUnitAbilityLevel(u, FourCC('AInv')) == 0 then
        invAdded = true
        UnitAddAbility(u, FourCC('AInv'))
    end
    if not UnitAddItem(u, it) then
        added = false
    elseif GetWidgetLife(it) > 0.0 then
        added = false
    end
    RemoveItem(it)
    if invAdded then
        UnitRemoveAbility(u, FourCC('AInv'))
    end
    return added
end

-- Stack template (from LIBRARY_Global)
local StackTemplate = {
    _I = 0,
    _V = {},
    _F = 0,
    STACK = {},
    COUNT = 0,
    NOW = {}
}

function StackTemplate__allocate()
    local this
    if StackTemplate._F ~= 0 then
        this = StackTemplate._F
        StackTemplate._F = StackTemplate._V[this]
    else
        StackTemplate._I = StackTemplate._I + 1
        this = StackTemplate._I
    end
    if this > 8190 then return 0 end
    StackTemplate._V[this] = -1
    return this
end

function StackTemplate_deallocate(this)
    if this == nil then return end
    if StackTemplate._V[this] ~= -1 then return end
    StackTemplate._V[this] = StackTemplate._F
    StackTemplate._F = this
end

function s__StackTemplate_create()
    local this = StackTemplate__allocate()
    StackTemplate.COUNT = StackTemplate.COUNT + 1
    StackTemplate.STACK[StackTemplate.COUNT] = this
    StackTemplate.NOW[StackTemplate.STACK[StackTemplate.COUNT]] = StackTemplate.COUNT
    return this
end

function s__StackTemplate_destroy(this)
    if StackTemplate.NOW[this] > 0 then
        StackTemplate.STACK[StackTemplate.NOW[this]] = StackTemplate.STACK[StackTemplate.COUNT]
        StackTemplate.NOW[StackTemplate.STACK[StackTemplate.NOW[this]]] = StackTemplate.NOW[this]
        StackTemplate.STACK[StackTemplate.COUNT] = 0
        StackTemplate.COUNT = StackTemplate.COUNT - 1
    end
    StackTemplate_deallocate(this)
end

-- ============================================================
-- LIBRARY_LibNewFunctions: Extended utilities
-- ============================================================

-- Real to String With 2 decimal places
function R2SW_Polyfill(value)
    local ten_off = math.floor(value / 0.01) % 10
    local on_off = math.floor(value / 0.1) % 10
    return math.floor(value) .. "." .. on_off .. ten_off
end

-- Group pick random
function GroupPickRandomUnit2(g)
    bj_groupRandomConsidered = 0
    bj_groupRandomCurrentPick = nil
    ForGroup(g, function()
        bj_groupRandomConsidered = bj_groupRandomConsidered + 1
        if GetRandomInt(1, bj_groupRandomConsidered) == 1 then
            bj_groupRandomCurrentPick = GetEnumUnit()
        end
    end)
    return bj_groupRandomCurrentPick
end

-- Distance with scratch globals
G.gX2 = 0
G.gY2 = 0

function DistanceBetweenUnits(u, target)
    G.gX2 = GetUnitX(u) - GetUnitX(target)
    G.gY2 = GetUnitY(u) - GetUnitY(target)
    return math.sqrt(G.gX2 * G.gX2 + G.gY2 * G.gY2)
end

function DistanceBetweenCoords2(x, y, x2, y2)
    G.gX2 = x - x2
    G.gY2 = y - y2
    return math.sqrt(G.gX2 * G.gX2 + G.gY2 * G.gY2)
end

function DistanceBetweenUnitsXY(x, y, target)
    G.gX2 = x - GetUnitX(target)
    G.gY2 = y - GetUnitY(target)
    return math.sqrt(G.gX2 * G.gX2 + G.gY2 * G.gY2)
end

-- Group add/remove
function GroupRemoveGroup2(sourceGroup, destGroup)
    ForGroup(sourceGroup, function()
        GroupRemoveUnit(destGroup, GetEnumUnit())
    end)
end

function GroupAddGroup2(sourceGroup, destGroup)
    ForGroup(sourceGroup, function()
        GroupAddUnit(destGroup, GetEnumUnit())
    end)
end

-- Random chance
function Random(chance, fromAll)
    return GetRandomInt(1, fromAll) <= chance
end

-- Timed ability operations
function RemoveAbilityTimed(u, abilid, time)
    local t = CreateTimer()
    TimerStart(t, time, false, function()
        UnitRemoveAbility(u, abilid)
        DestroyTimer(t)
    end)
end

function AddAbilityTimed(u, abilid, time)
    local t = CreateTimer()
    TimerStart(t, time, false, function()
        UnitAddAbility(u, abilid)
        DestroyTimer(t)
    end)
end

function RemoveAbilityTimedCD(u, abilid, time)
    local t = CreateTimer()
    TimerStart(t, time, false, function()
        if BlzGetUnitAbilityCooldownRemaining(u, abilid) == 0 then
            UnitRemoveAbility(u, abilid)
        end
        DestroyTimer(t)
    end)
end

function RemoveEffectTimed(e, time)
    local t = CreateTimer()
    TimerStart(t, time, false, function()
        DestroyEffect(e)
        DestroyTimer(t)
    end)
end

-- Capital functions
G.CheckPlayer = nil
G.gGroup = nil
G.b_OwnCapitalInRange = nil

function OwnCapitalInRange(pi, x, y, radius)
    G.CheckPlayer = Player(pi)
    GroupEnumUnitsInRange(G.gGroup, x, y, radius, G.b_OwnCapitalInRange)
    return FirstOfGroup(G.gGroup)
end

function isCapital(u)
    return IsUnitInGroup(u, G.udg_StolicaGroups)
end

-- ============================================================
-- Global___Init
-- ============================================================

function Global___Init()
    TimerStart(G.Global_Timer, 999999, false, nil)
end
