-- Silitids economy diagnostic for P1..P4.
local function fourcc(id) return string.pack(">I4", id) end
local out = {}
for _, pid in ipairs({1,2,3,4}) do
    if AiRace[pid] == "Silitids" then
        local p = Player(pid)
        local g = CreateGroup()
        GroupEnumUnitsOfPlayer(g, p, nil)
        local sz = BlzGroupGetSize(g)
        local byType = {}
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, i)
            if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
                local t = GetUnitTypeId(u)
                byType[t] = (byType[t] or 0) + 1
            end
        end
        DestroyGroup(g)
        -- key counts via getAiCount vs actual
        local droneActual = byType[FourCC('e01G')] or 0
        local droneAi = getAiCount(pid, FourCC('e01G')) or 0
        local larva = byType[FourCC('e01I')] or 0
        local mother = byType[FourCC('e01R')] or 0
        -- biggest non-worker types
        local arr = {}
        for t, c in pairs(byType) do arr[#arr+1] = {t=t,c=c} end
        table.sort(arr, function(a,b) return a.c > b.c end)
        local top = ""
        for i = 1, math.min(6, #arr) do top = top .. fourcc(arr[i].t) .. "=" .. arr[i].c .. " " end
        local gold = GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD)
        out[#out+1] = "P"..pid.." drones e01G actual="..droneActual.." getAiCount="..droneAi
            .." larvae e01I="..larva.." mothers e01R="..mother.." gold="..gold.."\n   top: "..top
    end
end
return table.concat(out, "\n")
