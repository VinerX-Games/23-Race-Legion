-- Per-bot AI diagnostic snapshot. Returns a compact summary string and writes a
-- full per-bot dump to the probe log (tag SNAP).
local function id2s(id)
    if id == nil or id == 0 then return "----" end
    local a = string.char((id >> 24) & 0xFF, (id >> 16) & 0xFF, (id >> 8) & 0xFF, id & 0xFF)
    return a
end

local lines = {}
local g = CreateGroup()
local nBots = 0
local sumEco, sumBld, sumArmy, sumNavy, sumGrade = 0, 0, 0, 0, 0
local t3Reached = 0

for pi = 0, 27 do
    local race = AiRace and AiRace[pi]
    if race ~= nil then
        local def = AiRaces[race]
        local p = Player(pi)
        nBots = nBots + 1
        -- enumerate buildings, compute eco score + counts
        local eco = 0
        local nBld, nStruct = 0, 0
        local typeCount = {}
        GroupEnumUnitsOfPlayer(g, p, nil)
        local sz = BlzGroupGetSize(g)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, i)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                local tid = GetUnitTypeId(u)
                typeCount[tid] = (typeCount[tid] or 0) + 1
                if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
                    nStruct = nStruct + 1
                    if def and def.ecoWeights and def.ecoWeights[tid] then
                        eco = eco + def.ecoWeights[tid]
                    end
                end
            end
        end
        GroupClear(g)
        local gold = GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD)
        local lum = GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER)
        local grade = (Grades and Grades[pi]) or 0
        local army = (udg_Ai_army and udg_Ai_army[pi] and BlzGroupGetSize(udg_Ai_army[pi])) or 0
        local navy = (udg_Ai_navy and udg_Ai_navy[pi] and BlzGroupGetSize(udg_Ai_navy[pi])) or 0
        local hv = (udg_Ai_harvest and udg_Ai_harvest[pi] and BlzGroupGetSize(udg_Ai_harvest[pi])) or 0
        local blT = (udg_Ai_buildersT and udg_Ai_buildersT[pi] and BlzGroupGetSize(udg_Ai_buildersT[pi])) or 0
        local blI = (udg_Ai_builders and udg_Ai_builders[pi] and BlzGroupGetSize(udg_Ai_builders[pi])) or 0
        -- tier progression from techUp steps
        local tierStr = ""
        local maxTo, haveTop = 0, false
        if def and def.strategData and def.strategData.steps then
            for _, st in ipairs(def.strategData.steps) do
                if st.action == "techUp" then
                    local cf = getAiCount(pi, st.from)
                    local ct = getAiCount(pi, st.to)
                    tierStr = tierStr .. id2s(st.from) .. "=" .. ct
                        .. "(<-" .. cf .. ") "
                    -- last techUp 'to' = top tier
                    maxTo = st.to
                end
            end
            if maxTo ~= 0 and getAiCount(pi, maxTo) >= 1 then haveTop = true; t3Reached = t3Reached + 1 end
        end
        sumEco = sumEco + eco; sumBld = sumBld + nStruct
        sumArmy = sumArmy + army; sumNavy = sumNavy + navy; sumGrade = sumGrade + grade
        local line = string.format(
            "SNAP pi=%d %s eco=%d grd=%d g=%d l=%d struct=%d army=%d navy=%d hv=%d blT=%d blI=%d top=%s tiers[%s]",
            pi, tostring(race), eco, grade, R2I(gold), R2I(lum), nStruct, army, navy, hv, blT, blI,
            tostring(haveTop), tierStr)
        lines[#lines + 1] = line
        if ProbeLogWrite then ProbeLogWrite(line) end
    end
end
DestroyGroup(g)
local summary = string.format("BOTS=%d avgEco=%.1f avgStruct=%.1f avgArmy=%.1f avgNavy=%.2f avgGrade=%.1f topTierBots=%d",
    nBots, sumEco / math.max(nBots, 1), sumBld / math.max(nBots, 1),
    sumArmy / math.max(nBots, 1), sumNavy / math.max(nBots, 1),
    sumGrade / math.max(nBots, 1), t3Reached)
if ProbeLogWrite then ProbeLogWrite("SNAP " .. summary) end
return summary .. "\n" .. table.concat(lines, "\n")
