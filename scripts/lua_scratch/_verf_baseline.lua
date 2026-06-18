gVerfTypes = {
    [FourCC('h0D8')] = true, [FourCC('h0D1')] = true, [FourCC('h0D3')] = true,
    [FourCC('h0E7')] = true, [FourCC('h0D7')] = true, [FourCC('h011')] = true,
    [FourCC('h0HO')] = true,
}
gVerfBaseline = {}
local g = CreateGroup()
GroupEnumUnitsInRect(g, bj_mapInitialPlayableArea, nil)
local sz = BlzGroupGetSize(g)
local c = 0
for i = 0, sz - 1 do
    local u = BlzGroupUnitAt(g, i)
    if u ~= nil and gVerfTypes[GetUnitTypeId(u)] then
        gVerfBaseline[GetHandleId(u)] = true
        c = c + 1
    end
end
DestroyGroup(g)
return "baseline shipyards recorded: " .. c
