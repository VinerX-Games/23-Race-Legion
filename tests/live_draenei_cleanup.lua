local t = DraeneiLiveTest
if t ~= nil then
    for _, u in ipairs(t.units) do
        DraeneiCombat.ClearProtection(u)
        DraeneiCombat.units[u] = nil
        if GetUnitTypeId(u) ~= 0 then RemoveUnit(u) end
    end
    for i = #DraeneiCombat.wards, 1, -1 do
        local data = DraeneiCombat.wards[i]
        if data.owner == t.player then
            if GetUnitTypeId(data.unit) ~= 0 then RemoveUnit(data.unit) end
            table.remove(DraeneiCombat.wards, i)
        end
    end
    for _, id in ipairs({'RDr1','RDr2','RDr3','RDr4','RDr5'}) do
        SetPlayerTechResearched(t.player, FourCC(id), 0)
    end
end
DraeneiLiveTest = nil
return 'cleaned'
