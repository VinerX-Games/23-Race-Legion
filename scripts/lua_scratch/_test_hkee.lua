local pi = 10
local p = Player(pi)
SetPlayerTechResearched(p, FourCC('hkee'), 1)
local g = CreateGroup()
GroupEnumUnitsOfPlayer(g, p, nil)
local sz = BlzGroupGetSize(g)
local accepted, tested = 0, 0
for i = 0, sz - 1 do
    local u = BlzGroupUnitAt(g, i)
    if u and GetUnitTypeId(u) == FourCC('h0JO') then
        tested = tested + 1
        IssueImmediateOrderById(u, FourCC('R0FJ'))
        if GetUnitCurrentOrder(u) ~= 0 then accepted = accepted + 1 end
    end
end
DestroyGroup(g)
return "after granting hkee: forges tested=" .. tested .. " researchAccepted=" .. accepted
