-- R5 hot-patch: don't yank channeling workers + resume stalled buildings
-- Fix 1: AiRecycleBuilders — only idle workers
AiRecycleBuilders = function(pi, maxMove)
    local grpT = udg_Ai_buildersT[pi]
    if grpT == nil then return end
    local grpH = udg_Ai_harvest[pi]
    if grpH == nil then return end
    local now = AiBrainTickCounter or 0
    if now % 60 == 0 then
        for k, t in pairs(g_BuildSpotReserved) do
            if now - t >= g_BuildReserveTicks then g_BuildSpotReserved[k] = nil end
        end
    end
    local sz = BlzGroupGetSize(grpT)
    local victims = nil
    local found = 0
    local cap = maxMove or 4
    for i = 0, sz - 1 do
        if found >= cap then break end
        local u = BlzGroupUnitAt(grpT, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local c = AiBuildClaim[u]
            local expired = c ~= nil and (now - c) >= AiBuildClaimTicks
            if GetUnitCurrentOrder(u) == 0 and (c == nil or expired) then
                if victims == nil then victims = {} end
                found = found + 1
                victims[found] = u
            end
        end
    end
    if victims == nil then return end
    for k = 1, found do
        local u = victims[k]
        GroupRemoveUnit(grpT, u)
        GroupAddUnit(grpH, u)
        AiBuildClaim[u] = nil
        IssueImmediateOrder(u, "autoharvestlumber")
    end
end

-- Fix 2: BrainResumeBuildings
BrainResumeBuildings = function(pi)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return 0 end
    local sz = BlzGroupGetSize(grp)
    if sz == 0 then return 0 end
    local resumed = 0
    local maxN = AiBrainMaxBuild or 6
    for i = 0, sz - 1 do
        if resumed >= maxN then break end
        local b = BlzGroupUnitAt(grp, i)
        if b ~= nil and GetUnitState(b, UNIT_STATE_LIFE) > 0.405 then
            local hp = GetUnitState(b, UNIT_STATE_LIFE)
            local maxHp = BlzGetUnitMaxHP(b)
            if maxHp > 1 and hp < maxHp - 0.5 then
                local worker = AiFindFreeWorker(pi)
                if worker ~= nil then
                    GroupAddUnit(udg_Ai_buildersT[pi], worker)
                    GroupRemoveUnit(udg_Ai_builders[pi], worker)
                    GroupRemoveUnit(udg_Ai_harvest[pi], worker)
                    AiBuildClaim[worker] = AiBrainTickCounter or 0
                    IssueTargetOrder(worker, "repair", b)
                    resumed = resumed + 1
                end
            end
        end
    end
    return resumed
end

-- Fix 3: AiCountBuildingsOfType — skip incomplete
AiCountBuildingsOfType = function(pi, bldType)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return 0 end
    local n = 0
    local sz = BlzGroupGetSize(grp)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitTypeId(u) == bldType
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local maxHp = BlzGetUnitMaxHP(u)
            if maxHp > 1 and GetUnitState(u, UNIT_STATE_LIFE) < maxHp - 0.5 then
                -- incomplete, skip
            else
                n = n + 1
            end
        end
    end
    return n
end

-- Inject resume call into BrainBuild (after normal build loop, before AiRecycleBuilders)
-- We do this by wrapping BrainBuild
local _oldBrainBuild = BrainBuild
BrainBuild = function(pi, wm, race)
    local built = _oldBrainBuild(pi, wm, race)
    local resumed = BrainResumeBuildings(pi)
    return built, resumed
end

return "R5 hot-patched: recycle(no-yank) + resume(stalled) + count(skip-incomplete) + BrainBuild wrap"
