-- Remove ALL units of the given players (shipyards already captured to _verf_data.txt).
local targets = { [8] = true, [9] = true, [16] = true }
local removed = {}
local g = CreateGroup()
GroupEnumUnitsInRect(g, bj_mapInitialPlayableArea, nil)
local sz = BlzGroupGetSize(g)
-- collect first (can't RemoveUnit while iterating the live enum safely)
local kill = {}
for i = 0, sz - 1 do
    local u = BlzGroupUnitAt(g, i)
    if u ~= nil then
        local pid = GetPlayerId(GetOwningPlayer(u))
        if targets[pid] then
            kill[#kill + 1] = u
            removed[pid] = (removed[pid] or 0) + 1
        end
    end
end
DestroyGroup(g)
for _, u in ipairs(kill) do RemoveUnit(u) end
local s = ""
for pid, c in pairs(removed) do s = s .. "P" .. pid .. "=" .. c .. " " end
return "removed units: " .. s
