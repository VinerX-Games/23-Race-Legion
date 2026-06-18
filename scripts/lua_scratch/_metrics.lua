-- Per-race metrics for 4:30 checkpoints. One compact line per bot + summary.
-- Fields: units(army) navy transp grade/cap tier ecoI cap(tured) cities struct stalled food capAlive
local function id2s(id)
    if id == nil or id == 0 then return "----" end
    return string.char((id >> 24) & 0xFF, (id >> 16) & 0xFF, (id >> 8) & 0xFF, id & 0xFF)
end

local lines = {}
local g = CreateGroup()
local zah = udg_ZahvatBuildings
local nBots = 0
local S = { units=0, navy=0, transp=0, grade=0, tier=0, eco=0, cap=0, struct=0, stalled=0, food=0, capAlive=0, t2=0, t3=0 }

-- count captured ZahvatBuildings per owner (one pass)
local capByPi = {}
if zah then
    local zsz = BlzGroupGetSize(zah)
    for i = 0, zsz - 1 do
        local u = BlzGroupUnitAt(zah, i)
        if u and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local op = GetPlayerId(GetOwningPlayer(u))
            capByPi[op] = (capByPi[op] or 0) + 1
        end
    end
end

for pi = 0, 27 do
    local race = AiRace and AiRace[pi]
    if race ~= nil then
        local def = AiRaces[race]
        local p = Player(pi)
        nBots = nBots + 1
        -- structures: eco from ecoWeights, stalled = <90% hp
        local eco, nStruct, stalled = 0, 0, 0
        local typeset = {}
        GroupEnumUnitsOfPlayer(g, p, nil)
        local sz = BlzGroupGetSize(g)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, i)
            if u and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                local tid = GetUnitTypeId(u)
                if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
                    nStruct = nStruct + 1
                    if def and def.ecoWeights and def.ecoWeights[tid] then eco = eco + def.ecoWeights[tid] end
                    if GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < 90 then stalled = stalled + 1 end
                else
                    typeset[tid] = true
                end
            end
        end
        GroupClear(g)
        local captured = capByPi[pi] or 0
        eco = eco + captured * 8
        -- army / navy / transports
        local army = (udg_Ai_army and udg_Ai_army[pi] and BlzGroupGetSize(udg_Ai_army[pi])) or 0
        local navy, transp = 0, 0
        if udg_Ai_navy and udg_Ai_navy[pi] then
            local ng = udg_Ai_navy[pi]; local nsz = BlzGroupGetSize(ng)
            navy = nsz
            for i = 0, nsz - 1 do
                local u = BlzGroupUnitAt(ng, i)
                if u and AiTransportSet and AiTransportSet[GetUnitTypeId(u)] then transp = transp + 1 end
            end
        end
        -- unit variety in army group
        local variety = 0
        if udg_Ai_army and udg_Ai_army[pi] then
            local ag = udg_Ai_army[pi]; local asz = BlzGroupGetSize(ag); local vs = {}
            for i = 0, asz - 1 do
                local u = BlzGroupUnitAt(ag, i)
                if u then vs[GetUnitTypeId(u)] = true end
            end
            for _ in pairs(vs) do variety = variety + 1 end
        end
        local grade = (Grades and Grades[pi]) or 0
        local gcap = (def and def.strategData and def.strategData.gradeCap) or 0
        -- tier: count techUp steps whose 'to' building exists
        local tier = 1
        if def and def.strategData and def.strategData.steps then
            for _, st in ipairs(def.strategData.steps) do
                if st.action == "techUp" and getAiCount(pi, st.to) >= 1 then tier = tier + 1 end
            end
        end
        local food = GetPlayerState(p, PLAYER_STATE_RESOURCE_FOOD_USED)
        local cap = playerCapital and playerCapital[pi]
        local capAlive = (cap and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405) and 1 or 0
        S.units=S.units+army; S.navy=S.navy+navy; S.transp=S.transp+transp; S.grade=S.grade+grade
        S.tier=S.tier+tier; S.eco=S.eco+eco; S.cap=S.cap+captured; S.struct=S.struct+nStruct
        S.stalled=S.stalled+stalled; S.food=S.food+food; S.capAlive=S.capAlive+capAlive
        if tier>=2 then S.t2=S.t2+1 end
        if tier>=3 then S.t3=S.t3+1 end
        local line = string.format(
            "M pi=%d %-12s u=%d var=%d nav=%d tr=%d grd=%d/%d t%d eco=%d cap=%d str=%d stl=%d food=%d capAlive=%d",
            pi, tostring(race), army, variety, navy, transp, grade, gcap, tier, eco, captured,
            nStruct, stalled, food, capAlive)
        lines[#lines+1] = line
        if ProbeLogWrite then ProbeLogWrite(line) end
    end
end
DestroyGroup(g)
local n = math.max(nBots, 1)
local summary = string.format(
    "METRICS bots=%d avgU=%.1f navy=%d transp=%d avgGrd=%.1f t2=%d t3=%d avgEco=%.1f avgCap=%.2f avgStr=%.1f avgStl=%.1f capAlive=%d/%d",
    nBots, S.units/n, S.navy, S.transp, S.grade/n, S.t2, S.t3, S.eco/n, S.cap/n, S.struct/n, S.stalled/n, S.capAlive, nBots)
if ProbeLogWrite then ProbeLogWrite(summary) end
return summary .. "\n" .. table.concat(lines, "\n")
