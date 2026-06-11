-- Diagnose: army volume (food), incomplete/stalled buildings, capture opportunity.
local lines = {}
local g = CreateGroup()
local zah = udg_ZahvatBuildings
for _, pi in ipairs({6, 9, 11, 4, 22, 2}) do  -- Undead, Forsaken, KulTiras, + strong refs
    local race = AiRace and AiRace[pi]
    if race then
        local p = Player(pi)
        local cap = playerCapital[pi]
        local cx, cy = 0, 0
        if cap then cx, cy = GetUnitX(cap), GetUnitY(cap) end
        -- buildings: complete vs low-hp (possibly stalled/constructing)
        local struct, lowhp = 0, 0
        GroupEnumUnitsOfPlayer(g, p, nil)
        local sz = BlzGroupGetSize(g)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, i)
            if u and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 and IsUnitType(u, UNIT_TYPE_STRUCTURE) then
                struct = struct + 1
                if GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < 90 then lowhp = lowhp + 1 end
            end
        end
        GroupClear(g)
        -- nearby uncaptured neutral ZahvatBuildings within 5000 of capital
        local near = 0
        if zah and cap then
            local zsz = BlzGroupGetSize(zah)
            for i = 0, zsz - 1 do
                local u = BlzGroupUnitAt(zah, i)
                if u and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                    local ow = GetOwningPlayer(u)
                    if ow ~= p and not IsPlayerAlly(ow, p) then
                        local dx, dy = GetUnitX(u) - cx, GetUnitY(u) - cy
                        if dx*dx + dy*dy < 5000*5000 then near = near + 1 end
                    end
                end
            end
        end
        local fu = GetPlayerState(p, PLAYER_STATE_RESOURCE_FOOD_USED)
        local fc = GetPlayerState(p, PLAYER_STATE_RESOURCE_FOOD_CAP)
        local army = (udg_Ai_army[pi] and BlzGroupGetSize(udg_Ai_army[pi])) or 0
        local blT = (udg_Ai_buildersT[pi] and BlzGroupGetSize(udg_Ai_buildersT[pi])) or 0
        lines[#lines+1] = string.format("DIAG pi=%d %s food=%d/%d army=%d struct=%d lowHP=%d nearNeutral=%d blT=%d",
            pi, tostring(race), fu, fc, army, struct, lowhp, near, blT)
    end
end
DestroyGroup(g)
return table.concat(lines, "\n")
