-- Compare research acceptance: Horde (working grades) vs Forsaken (stuck).
local function testRace(pi, bldId, techId, label)
    local p = Player(pi)
    local g = CreateGroup()
    GroupEnumUnitsOfPlayer(g, p, nil)
    local sz = BlzGroupGetSize(g)
    local tested, accepted = 0, 0
    local lvlBefore = GetPlayerTechCount(p, techId, true)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u and GetUnitTypeId(u) == bldId then
            tested = tested + 1
            IssueImmediateOrderById(u, techId)
            if GetUnitCurrentOrder(u) ~= 0 then accepted = accepted + 1 end
        end
    end
    DestroyGroup(g)
    return string.format("%s pi=%d bld=%s tech lvl=%d tested=%d accepted=%d",
        label, pi, tostring(bldId ~= nil), lvlBefore, tested, accepted)
end
-- Find Horde grade building dynamically: obar (barracks) researches R0EC etc.
local out = {}
out[#out+1] = testRace(12, FourCC('obar'), FourCC('R0EC'), "Horde-obar-R0EC")
out[#out+1] = testRace(12, FourCC('ogre'), FourCC('Ropg'), "Horde-ogre-Ropg")
out[#out+1] = testRace(10, FourCC('h0JO'), FourCC('R0FI'), "Forsaken-forge-R0FI")
out[#out+1] = testRace(10, FourCC('h0JO'), FourCC('R0FT'), "Forsaken-forge-R0FT")
return table.concat(out, "\n")
