function AiEnsureBuilderReserve(pi, minCount)
    local want = minCount or 2
    local grp = udg_Ai_builders[pi]
    local grpH = udg_Ai_harvest[pi]
    if grp == nil or grpH == nil then return 0 end
    local aliveBuilders = 0
    local sz = BlzGroupGetSize(grp)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            aliveBuilders = aliveBuilders + 1
            if aliveBuilders >= want then return 0 end
        end
    end
    local moved = 0
    local szH = BlzGroupGetSize(grpH)
    for i = 0, szH - 1 do
        if aliveBuilders + moved >= want then break end
        local u = BlzGroupUnitAt(grpH, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 and GetUnitCurrentOrder(u) ~= 851972 and GetUnitCurrentOrder(u) ~= 851976 then
            GroupAddUnit(grp, u)
            GroupRemoveUnit(grpH, u)
            moved = moved + 1
        end
    end
    return moved
end
local _BrainBuild = BrainBuild
function BrainBuild(pi, wm, race)
    AiEnsureBuilderReserve(pi, 3)
    return _BrainBuild(pi, wm, race)
end
local r={}
for _,pi in ipairs({5,6,7}) do r[#r+1]={pi=pi,moved=AiEnsureBuilderReserve(pi,3),b=BlzGroupGetSize(udg_Ai_builders[pi]),h=BlzGroupGetSize(udg_Ai_harvest[pi])} end
return r
