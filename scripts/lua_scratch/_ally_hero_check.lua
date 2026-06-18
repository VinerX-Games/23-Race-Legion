local out = {}
for _, pid in ipairs({10, 11, 12}) do
    if AiRace[pid] == "Alliance" then
        local p = Player(pid)
        local hp = GetPlayerTechMaxAllowed(p, FourCC('Hpal'))
        local ha = GetPlayerTechMaxAllowed(p, FourCC('Hamg'))
        local hm = GetPlayerTechMaxAllowed(p, FourCC('Hmkg'))
        local g = CreateGroup()
        GroupEnumUnitsOfPlayer(g, p, nil)
        local sz = BlzGroupGetSize(g)
        local altars, heroes = 0, 0
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(g, i)
            if u ~= nil then
                if GetUnitTypeId(u) == FourCC('halt') then altars = altars + 1 end
                if IsUnitType(u, UNIT_TYPE_HERO) and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then heroes = heroes + 1 end
            end
        end
        DestroyGroup(g)
        out[#out + 1] = "P" .. pid .. " maxAllowed Hpal=" .. hp .. " Hamg=" .. ha .. " Hmkg=" .. hm
            .. " | altars=" .. altars .. " heroes=" .. heroes
    end
end
return table.concat(out, "\n")
