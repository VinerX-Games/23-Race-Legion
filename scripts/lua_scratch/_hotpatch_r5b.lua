-- R5b hot-patch: Fix 1 (no yank) + Fix 2 (resume w/ capital priority) + REVERT Fix 3

-- Revert Fix 3: AiCountBuildingsOfType back to original (count incomplete too)
AiCountBuildingsOfType = function(pi, bldType)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return 0 end
    local n = 0
    local sz = BlzGroupGetSize(grp)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(grp, i)
        if u ~= nil and GetUnitTypeId(u) == bldType
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            n = n + 1
        end
    end
    return n
end

-- Fix 1: AiRecycleBuilders — only idle workers, never yank channeling
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

-- Fix 2 v2: BrainResumeBuildings — prioritize seed (capital), then other buildings
BrainResumeBuildings = function(pi, wm)
    local grp = udg_Ai_buildings[pi]
    if grp == nil then return 0 end
    local sz = BlzGroupGetSize(grp)
    if sz == 0 then return 0 end
    local race = AiRaceOf(pi)
    local seedType = race and race.buildings and race.buildings.seed
    local resumed = 0
    local maxN = AiBrainMaxBuild or 6

    -- Helper: try to send a worker to resume building b
    local function tryResume(b)
        if resumed >= maxN then return end
        local worker = AiFindFreeWorker(pi)
        if worker == nil then return end
        GroupAddUnit(udg_Ai_buildersT[pi], worker)
        GroupRemoveUnit(udg_Ai_builders[pi], worker)
        GroupRemoveUnit(udg_Ai_harvest[pi], worker)
        AiBuildClaim[worker] = AiBrainTickCounter or 0
        IssueTargetOrder(worker, "repair", b)
        resumed = resumed + 1
    end

    -- PASS 1: prioritize seed (capital) — if incomplete, resume it FIRST
    if seedType then
        for i = 0, sz - 1 do
            local b = BlzGroupUnitAt(grp, i)
            if b ~= nil
                and GetUnitTypeId(b) == seedType
                and GetUnitState(b, UNIT_STATE_LIFE) > 0.405 then
                local hp = GetUnitState(b, UNIT_STATE_LIFE)
                local maxHp = BlzGetUnitMaxHP(b)
                if maxHp > 1 and hp < maxHp - 0.5 then
                    tryResume(b)
                    if resumed >= maxN then return resumed end
                end
            end
        end
    end

    -- PASS 2: other incomplete buildings
    for i = 0, sz - 1 do
        if resumed >= maxN then break end
        local b = BlzGroupUnitAt(grp, i)
        if b ~= nil and GetUnitState(b, UNIT_STATE_LIFE) > 0.405 then
            if seedType and GetUnitTypeId(b) == seedType then
                -- already handled in pass 1
            else
                local hp = GetUnitState(b, UNIT_STATE_LIFE)
                local maxHp = BlzGetUnitMaxHP(b)
                if maxHp > 1 and hp < maxHp - 0.5 then
                    tryResume(b)
                end
            end
        end
    end
    return resumed
end

-- Wrap BrainBuild: add resume pass (BEFORE AiRecycleBuilders, which is inside old BrainBuild)
local _oldBrainBuild = BrainBuild
BrainBuild = function(pi, wm, race)
    local built = _oldBrainBuild(pi, wm, race)
    -- Resume runs AFTER old BrainBuild (which includes AiRecycleBuilders).
    -- But AiRecycleBuilders moved idle workers to harvest, so harvest has workers.
    local resumed = BrainResumeBuildings(pi, wm)
    return built
end

return "R5b: revert Fix3(count) + Fix1(no-yank) + Fix2(capital-priority-resume) + BrainBuild wrap"
