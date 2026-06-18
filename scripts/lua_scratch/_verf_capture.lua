-- Capture every shipyard currently on the map: owner, type, x, y, continent.
gVerfTypes = {
    [FourCC('h0D8')] = true, [FourCC('h0D1')] = true, [FourCC('h0D3')] = true,
    [FourCC('h0E7')] = true, [FourCC('h0D7')] = true, [FourCC('h011')] = true,
    [FourCC('h0HO')] = true, [FourCC('h0M4')] = true,  -- h0M4 = generic "Верфь" placed by host P0
}
local g = CreateGroup()
GroupEnumUnitsInRect(g, bj_mapInitialPlayableArea, nil)
local sz = BlzGroupGetSize(g)
local lines = {}
local perOwner = {}
for i = 0, sz - 1 do
    local u = BlzGroupUnitAt(g, i)
    if u ~= nil and gVerfTypes[GetUnitTypeId(u)] and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
        local pid = GetPlayerId(GetOwningPlayer(u))
        local x, y = GetUnitX(u), GetUnitY(u)
        local cont = AiContinentOf(x, y) or "nil"
        lines[#lines + 1] = "P" .. pid .. " " .. string.pack(">I4", GetUnitTypeId(u))
            .. " " .. math.floor(x) .. " " .. math.floor(y) .. " " .. cont
        perOwner[pid] = (perOwner[pid] or 0) + 1
    end
end
DestroyGroup(g)
local owner = ""
for pid, c in pairs(perOwner) do owner = owner .. "P" .. pid .. "=" .. c .. " " end
return "TOTAL=" .. #lines .. "  byOwner: " .. owner .. "\n" .. table.concat(lines, "\n")
