-- Measure per-bot neutral-building capture + the REAL Strateg eco score i.
-- i mirrors ZahType: +8 per owned ZahvatBuilding, else +ecoWeights[type].
local g = CreateGroup()
local lines = {}
local sumI, sumCap, n = 0, 0, 0
for pi = 0, 27 do
    local race = AiRace and AiRace[pi]
    if race ~= nil then
        local def = AiRaces[race]
        local p = Player(pi)
        n = n + 1
        local i, cap, cities = 0, 0, 0
        GroupEnumUnitsOfPlayer(g, p, nil)
        local sz = BlzGroupGetSize(g)
        for k = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, k)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                if IsUnitInGroup(u, udg_ZahvatBuildings) then
                    i = i + 8; cap = cap + 1
                elseif udg_StolicaGroups ~= nil and IsUnitInGroup(u, udg_StolicaGroups) then
                    cities = cities + 1
                    if def and def.ecoWeights and def.ecoWeights[GetUnitTypeId(u)] then
                        i = i + def.ecoWeights[GetUnitTypeId(u)]
                    end
                elseif def and def.ecoWeights and def.ecoWeights[GetUnitTypeId(u)] then
                    i = i + def.ecoWeights[GetUnitTypeId(u)]
                end
            end
        end
        GroupClear(g)
        local grade = (Grades and Grades[pi]) or 0
        sumI = sumI + i; sumCap = sumCap + cap
        lines[#lines + 1] = string.format("CAP pi=%d %s i=%d captured=%d cities=%d grade=%d", pi, tostring(race), i, cap, cities, grade)
    end
end
DestroyGroup(g)
local summary = string.format("CAPSUM bots=%d avgRealI=%.1f avgCaptured=%.2f", n, sumI/math.max(n,1), sumCap/math.max(n,1))
return summary .. "\n" .. table.concat(lines, "\n")
