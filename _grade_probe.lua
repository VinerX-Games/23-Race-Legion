-- Diagnose grade pipeline: for each bot, does Strateg run, does it own GradeUnit
-- buildings, and are grade upgrades researched? Replicates Strateg's eco calc.
local function id2s(id)
    if id == nil or id == 0 then return "----" end
    return string.char((id >> 24) & 0xFF, (id >> 16) & 0xFF, (id >> 8) & 0xFF, id & 0xFF)
end
local lines = {}
local g = CreateGroup()
for pi = 0, 27 do
    local race = AiRace and AiRace[pi]
    if race ~= nil then
        local def = AiRaces[race]
        local p = Player(pi)
        -- real eco i like Strateg/ZahType
        local i = 0
        GroupEnumUnitsOfPlayer(g, p, nil)
        local sz = BlzGroupGetSize(g)
        for k = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, k)
            if u and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                if IsUnitInGroup(u, udg_ZahvatBuildings) then i = i + 8
                else
                    local tid = GetUnitTypeId(u)
                    if def and def.ecoWeights and def.ecoWeights[tid] then i = i + def.ecoWeights[tid] end
                end
            end
        end
        GroupClear(g)
        local grade = (Grades and Grades[pi]) or 0
        local ctrl = udg_AiControl and udg_AiControl[pi]
        local sd = def and def.strategData
        local detail = {}
        if sd and sd.steps then
            for _, st in ipairs(sd.steps) do
                if (st.action == "research" or st.action == "random") then
                    local rows = st.rows
                    if st.action == "random" and st.branches then rows = st.branches[1] end
                    if rows then
                        for _, up in ipairs(rows) do
                            local gu, tech = up[1], up[2]
                            local own = getAiCount(pi, gu)
                            local lvl = GetPlayerTechCount(p, tech, true)
                            detail[#detail+1] = id2s(gu).."x"..own.."/"..id2s(tech).."="..lvl
                        end
                    end
                end
            end
        end
        lines[#lines+1] = string.format("G pi=%d %-12s i=%d grd=%d ctrl=%s sd=%s [%s]",
            pi, tostring(race), i, grade, tostring(ctrl), tostring(sd ~= nil),
            table.concat(detail, " "))
    end
end
DestroyGroup(g)
return table.concat(lines, "\n")
