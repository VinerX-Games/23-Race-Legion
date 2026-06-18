-- Find P11's altar, try to train a Paladin, report gold/food and whether the order took.
local p = Player(11)
local g = CreateGroup()
GroupEnumUnitsOfPlayer(g, p, nil)
local sz = BlzGroupGetSize(g)
local altar = nil
for i = 0, sz - 1 do
    local u = BlzGroupUnitAt(g, i)
    if u ~= nil and GetUnitTypeId(u) == FourCC('halt') and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
        altar = u; break
    end
end
DestroyGroup(g)
if altar == nil then return "no altar found for P11" end
local gold = GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD)
local lum  = GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER)
local foodU = GetPlayerState(p, PLAYER_STATE_RESOURCE_FOOD_USED)
local foodC = GetPlayerState(p, PLAYER_STATE_RESOURCE_FOOD_CAP)
local ordBefore = GetUnitCurrentOrder(altar)
local ok = IssueImmediateOrderById(altar, FourCC('Hpal'))
local ordAfter = GetUnitCurrentOrder(altar)
return "altar found. gold=" .. gold .. " lumber=" .. lum .. " food=" .. foodU .. "/" .. foodC
    .. " | IssueOrder ret=" .. tostring(ok)
    .. " ordBefore=" .. ordBefore .. " ordAfter=" .. ordAfter
