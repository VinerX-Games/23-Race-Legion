-- Hotfix: Fix GroupAddUnitSimple & GroupRemoveUnitSimple + clean dead units + rebuild pools
do
    local _origGaus = GroupAddUnitSimple
    local _origGrus = GroupRemoveUnitSimple

    function GroupAddUnitSimple(u, g)
        if u ~= nil and g ~= nil then
            pcall(function() GroupAddUnit(g, u) end)
        end
    end

    function GroupRemoveUnitSimple(u, g)
        if u ~= nil and g ~= nil then
            pcall(function() GroupRemoveUnit(g, u) end)
        end
    end

    ProbeLogWrite("[HOTFIX] GroupAddUnitSimple/GroupRemoveUnitSimple patched")
end

-- Clean all dead units from a group (iterates safely via collecting live indices first)
function AiCleanDeadFromGroup(grp)
    if grp == nil then return 0 end
    local sz = BlzGroupGetSize(grp)
    if sz == 0 then return 0 end
    local dead = {}
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u == nil or GetWidgetLife(u) <= 0.405 then
            dead[#dead + 1] = u or i
        end
    end
    for _, u in ipairs(dead) do
        if type(u) ~= "number" then
            GroupRemoveUnit(grp, u)
        end
    end
    return #dead
end

-- Rebuild all AI groups for a player: collect alive units FIRST via ForGroup,
-- THEN clear, THEN repopulate. Never use BlzGroupUnitAt on pre-placed groups.
function AiRebuildGroups(pi)
    if AiRace[pi] == nil then return 0, "no race" end

    -- Collect alive units from ALL groups BEFORE clearing (ForGroup works reliably)
    local allUnits = {}
    local seen = {}

    local function collector()
        local u = GetEnumUnit()
        if u ~= nil and GetWidgetLife(u) > 0.405 then
            local h = GetHandleId(u)
            if not seen[h] then
                seen[h] = true
                allUnits[#allUnits + 1] = u
            end
        end
    end

    -- Also try GroupEnumUnitsOfPlayer first (works for some players)
    local gAll = CreateGroup()
    GroupEnumUnitsOfPlayer(gAll, Player(pi - 1), nil)
    ForGroup(gAll, collector)
    DestroyGroup(gAll)

    -- Supplement with ForGroup on each Ai_* group
    for _, g in ipairs({udg_Ai_units[pi], udg_Ai_army[pi], udg_Ai_buildings[pi],
                         udg_Ai_builders[pi], udg_Ai_buildersT[pi], udg_Ai_harvest[pi]}) do
        if g ~= nil then ForGroup(g, collector) end
    end

    -- NOW clear all groups
    for _, g in ipairs({udg_Ai_units[pi], udg_Ai_army[pi], udg_Ai_buildings[pi],
                         udg_Ai_builders[pi], udg_Ai_buildersT[pi], udg_Ai_harvest[pi]}) do
        if g ~= nil then GroupClear(g) end
    end

    -- Repopulate from collected alive units
    local stats = {units=0, army=0, bld=0, workers=0}
    for _, u in ipairs(allUnits) do
        stats.units = stats.units + 1
        GroupAddUnit(udg_Ai_units[pi], u)

        if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
            GroupAddUnit(udg_Ai_buildings[pi], u)
            stats.bld = stats.bld + 1
        elseif IsUnitType(u, UNIT_TYPE_PEON) then
            GroupAddUnit(udg_Ai_harvest[pi], u)
            stats.workers = stats.workers + 1
        else
            GroupAddUnit(udg_Ai_army[pi], u)
            stats.army = stats.army + 1
        end
    end

    return stats.units, string.format("%d units, %d bld, %d army, %d workers", stats.units, stats.bld, stats.army, stats.workers)
end

-- Clean + rebuild all bots
local totalDead = 0
local totalRebuilt = 0
local lines = {}
for pi = 2, 23 do
    if AiRace[pi] ~= nil then
        local deadSum = 0
        for _, g in ipairs({udg_Ai_units[pi], udg_Ai_army[pi], udg_Ai_buildings[pi],
                             udg_Ai_builders[pi], udg_Ai_buildersT[pi], udg_Ai_harvest[pi]}) do
            deadSum = deadSum + AiCleanDeadFromGroup(g)
        end
        totalDead = totalDead + deadSum
        local n, desc = AiRebuildGroups(pi)
        totalRebuilt = totalRebuilt + (n or 0)
        lines[#lines + 1] = string.format("pi=%02d deadClean=%d rebuilt=%s", pi, deadSum, desc)
    end
end

-- Also clean AiBuildClaim of dead handles
local claimDead = 0
for h, t in pairs(AiBuildClaim or {}) do
    local alive = false
    pcall(function()
        if GetWidgetLife(h) > 0.405 then alive = true end
    end)
    if not alive then
        AiBuildClaim[h] = nil
        claimDead = claimDead + 1
    end
end

return string.format("HOTFIX: deadCleaned=%d rebuilt=%d claimDead=%d\n%s",
    totalDead, totalRebuilt, claimDead, table.concat(lines, "\n"))
