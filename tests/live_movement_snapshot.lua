-- Read-only movement diagnostics. Run twice while a stuck unit has a move order:
-- python agent_bridge.py exec --file tests/live_movement_snapshot.lua
-- MovementProbeSlot defaults to 0; MovementProbeUnit can target an exact unit.
-- No orders, teleports, collision changes, or unit creation are performed.
if type(DebugChatAllowed) == "function" then
    assert(DebugChatAllowed(), "movement diagnostics require a solo debug session")
end

local function rawcode(id)
    if id == 0 then return "0000" end
    return string.char((id >> 24) & 255, (id >> 16) & 255,
        (id >> 8) & 255, id & 255)
end

local previous = MovementProbeHistory or {}
local history = {}
local result = {slot = MovementProbeSlot or 0, units = {}}
local targets = CreateGroup()
if MovementProbeUnit ~= nil then
    GroupAddUnit(targets, MovementProbeUnit)
else
    GroupEnumUnitsOfPlayer(targets, Player(result.slot), nil)
end

local function snapshot(u)
    local x, y = GetUnitX(u), GetUnitY(u)
    local h = GetHandleId(u)
    local old = previous[h]
    local row = {
        handle = h, id = rawcode(GetUnitTypeId(u)), name = GetUnitName(u),
        x = x, y = y, order = GetUnitCurrentOrder(u),
        speed = GetUnitMoveSpeed(u), default_speed = GetUnitDefaultMoveSpeed(u),
        paused = IsUnitPaused(u), hidden = IsUnitHidden(u),
        move_ability = GetUnitAbilityLevel(u, FourCC('Amov')),
        fly_height = GetUnitFlyHeight(u), collision = BlzGetUnitCollisionSize(u),
        life = GetWidgetLife(u), terrain = {}, nearby_units = {}, destructables = {},
    }
    if old ~= nil then
        row.displacement = math.sqrt((x - old.x)^2 + (y - old.y)^2)
    end
    history[h] = {x = x, y = y}
    for dx = -64, 64, 64 do
        for dy = -64, 64, 64 do
            row.terrain[#row.terrain + 1] = {
                dx = dx, dy = dy,
                walk_blocked = IsTerrainPathable(x + dx, y + dy, PATHING_TYPE_WALKABILITY),
                float_blocked = IsTerrainPathable(x + dx, y + dy, PATHING_TYPE_FLOATABILITY),
            }
        end
    end

    local neighbors = CreateGroup()
    GroupEnumUnitsInRange(neighbors, x, y, 384, nil)
    row.nearby_count = BlzGroupGetSize(neighbors)
    for i = 0, BlzGroupGetSize(neighbors) - 1 do
        local other = BlzGroupUnitAt(neighbors, i)
        if other ~= nil and other ~= u and #row.nearby_units < 24 then
            row.nearby_units[#row.nearby_units + 1] = {
                handle = GetHandleId(other), id = rawcode(GetUnitTypeId(other)),
                owner = GetPlayerId(GetOwningPlayer(other)),
                x = GetUnitX(other), y = GetUnitY(other),
                structure = IsUnitType(other, UNIT_TYPE_STRUCTURE),
                hidden = IsUnitHidden(other), life = GetWidgetLife(other),
                collision = BlzGetUnitCollisionSize(other),
            }
        end
    end
    DestroyGroup(neighbors)

    local area = Rect(x - 384, y - 384, x + 384, y + 384)
    EnumDestructablesInRect(area, nil, function()
        if #row.destructables >= 24 then return end
        local d = GetEnumDestructable()
        row.destructables[#row.destructables + 1] = {
            handle = GetHandleId(d), id = rawcode(GetDestructableTypeId(d)),
            name = GetDestructableName(d), x = GetDestructableX(d),
            y = GetDestructableY(d), life = GetWidgetLife(d),
        }
    end)
    RemoveRect(area)
    return row
end

-- Workers/heroes first, so a large army does not hide the reported problem.
for pass = 1, 2 do
    for i = 0, BlzGroupGetSize(targets) - 1 do
        local u = BlzGroupUnitAt(targets, i)
        if u ~= nil and GetWidgetLife(u) > 0.405
            and not IsUnitType(u, UNIT_TYPE_STRUCTURE) then
            local priority = IsUnitType(u, UNIT_TYPE_PEON) or IsUnitType(u, UNIT_TYPE_HERO)
            if priority == (pass == 1) and #result.units < 16 then
                result.units[#result.units + 1] = snapshot(u)
            end
        end
    end
end
DestroyGroup(targets)
MovementProbeHistory = history
result.previous_snapshot = next(previous) ~= nil
return result
