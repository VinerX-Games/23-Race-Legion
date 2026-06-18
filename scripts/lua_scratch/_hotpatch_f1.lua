-- F1 hot-patch (test-only): build pipeline footprint + anti-thrash + recycle + anchor.
AiBuildClaim = AiBuildClaim or {}
AiBuildClaimTicks = AiBuildClaimTicks or 8

function AiBuildPlaceable(x, y, half)
    half = half or (AiBuildingRadius and AiBuildingRadius * 0.2) or 192.0
    if IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then return false end
    if IsTerrainPathable(x, y, PATHING_TYPE_FLOATABILITY) then return false end
    local offs = { {half,0},{-half,0},{0,half},{0,-half} }
    for i = 1, 4 do
        if IsTerrainPathable(x + offs[i][1], y + offs[i][2], PATHING_TYPE_FLOATABILITY) then
            return false
        end
    end
    return true
end

function AiScanBuildRings(ax, ay, rad, phase)
    local minSpacing = rad * 0.9
    local sectors = 12
    local ring = 0
    while ring < 10 do
        local r = rad * 1.5 + ring * rad * 1.2
        local s = 0
        while s < sectors do
            local ang = (I2R(s + phase) / I2R(sectors)) * 2.0 * bj_PI
            local x = ax + r * Cos(ang)
            local y = ay + r * Sin(ang)
            if AiBuildPlaceable(x, y) and not AiBuildSpotOccupied(x, y, minSpacing) then
                return x, y
            end
            s = s + 1
        end
        ring = ring + 1
    end
    return nil, nil
end

function AiFindBuildSpot(pi, builder)
    local rad = AiBuildingRadius
    if rad == nil or rad <= 0 then rad = 256.0 end
    local phase = pi % 12
    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then
        local x, y = AiScanBuildRings(GetUnitX(cap), GetUnitY(cap), rad, phase)
        if x ~= nil then return x, y end
    end
    if builder ~= nil then
        return AiScanBuildRings(GetUnitX(builder), GetUnitY(builder), rad, phase)
    end
    return nil, nil
end

function AiEnsureCapital(pi)
    local cap = playerCapital[pi]
    if cap ~= nil and GetUnitState(cap, UNIT_STATE_LIFE) > 0.405 then return end
    playerCapital[pi] = nil
    AiCapEnumGroup = AiCapEnumGroup or CreateGroup()
    local g = AiCapEnumGroup
    GroupEnumUnitsOfPlayer(g, Player(pi), nil)
    local sz = BlzGroupGetSize(g)
    local pick = nil
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and GetUnitAbilityLevel(u, FourCC('A0IQ')) ~= 0 then
            pick = u; break
        end
    end
    GroupClear(g)
    if pick ~= nil then
        playerCapital[pi] = pick
        if aiCapitalEnter ~= nil then pcall(aiCapitalEnter, pick) end
    end
end

function AiFindFreeWorker(pi)
    local function alive(u)
        return u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
    end
    local now = AiBrainTickCounter or 0
    local grp = udg_Ai_builders[pi]
    if grp ~= nil then
        local sz = BlzGroupGetSize(grp)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grp, i)
            if alive(u) then return u end
        end
    end
    local grpT = udg_Ai_buildersT[pi]
    if grpT ~= nil then
        local sz = BlzGroupGetSize(grpT)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grpT, i)
            if alive(u) and GetUnitCurrentOrder(u) == 0 then
                local c = AiBuildClaim[u]
                if c == nil or (now - c) >= AiBuildClaimTicks then return u end
            end
        end
    end
    local grpH = udg_Ai_harvest[pi]
    if grpH ~= nil then
        local sz = BlzGroupGetSize(grpH)
        for i = 0, sz - 1 do
            local u = BlzGroupUnitAt(grpH, i)
            if alive(u) then return u end
        end
    end
    return nil
end

function AiRecycleBuilders(pi, maxMove)
    local grpT = udg_Ai_buildersT[pi]
    if grpT == nil then return end
    local grpH = udg_Ai_harvest[pi]
    if grpH == nil then return end
    local now = AiBrainTickCounter or 0
    local sz = BlzGroupGetSize(grpT)
    local moved = 0
    local i = 0
    while i < sz and moved < (maxMove or 4) do
        local u = BlzGroupUnitAt(grpT, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
            and GetUnitCurrentOrder(u) == 0 then
            local c = AiBuildClaim[u]
            if c == nil or (now - c) >= AiBuildClaimTicks then
                GroupRemoveUnit(grpT, u)
                GroupAddUnit(grpH, u)
                AiBuildClaim[u] = nil
                IssueImmediateOrder(u, "autoharvestlumber")
                moved = moved + 1
            end
        end
        i = i + 1
    end
end

function TryBuildWithType(bldType, fx, fy)
    local u = TryBuild_u
    if u == nil or bldType == nil then return end
    local pi = GetPlayerId(GetOwningPlayer(u))
    GroupAddUnit(udg_Ai_buildersT[pi], u)
    GroupRemoveUnit(udg_Ai_builders[pi], u)
    GroupRemoveUnit(udg_Ai_harvest[pi], u)
    AiBuildClaim[u] = AiBrainTickCounter or 0
    if fx ~= nil and fy ~= nil then
        IssueBuildOrderById(u, bldType, fx, fy)
        return
    end
    if AiSmartBuild then
        local bx, by = AiFindBuildSpot(pi, u)
        if bx ~= nil then
            IssueBuildOrderById(u, bldType, bx, by)
            return
        end
    end
    local ux0, uy0 = GetUnitX(u), GetUnitY(u)
    for _ = 1, 8 do
        local ang = GetRandomReal(0, 360) * bj_DEGTORAD
        local ux = ux0 + AiBuildingRadius * Cos(ang)
        local uy = uy0 + AiBuildingRadius * Sin(ang)
        if AiBuildPlaceable(ux, uy) then
            IssueBuildOrderById(u, bldType, ux, uy)
            return
        end
    end
    IssueBuildOrderById(u, bldType,
        ux0 + AiBuildingRadius * Cos(0), uy0 + AiBuildingRadius * Sin(0))
end

-- BrainBuild with a self-advancing per-tick counter (the running game's old tick
-- has no AiBrainTickCounter; bump it here so the claim window works in this test).
function BrainBuild(pi, wm, race)
    AiBrainTickCounter = (AiBrainTickCounter or 0) + 1
    local buildOrder = race.buildings
    if not buildOrder then return 0 end
    local built = 0
    local maxN = AiBrainMaxBuild
    local seedType = buildOrder.seed
    if seedType and type(seedType) == "number" then
        local count = AiCountBuildingsOfType(pi, seedType)
        if count < 1 then
            local worker = AiFindFreeWorker(pi)
            if worker ~= nil then
                TryBuild_u = worker
                TryBuildWithType(seedType)
                built = built + 1
            end
        end
    end
    for _, row in ipairs(buildOrder) do
        if built >= maxN then break end
        local bldType = row[1]
        if type(bldType) == "number" then
            local limit = row[2] or 1
            local count = AiCountBuildingsOfType(pi, bldType)
            local gateOk = true
            if row.gate then
                local gateFn = race.gates and race.gates[row.gate]
                if gateFn and not gateFn(pi) then gateOk = false end
            end
            if count < limit and gateOk then
                local worker = AiFindFreeWorker(pi)
                if worker ~= nil then
                    TryBuild_u = worker
                    TryBuildWithType(bldType)
                    built = built + 1
                end
            end
        end
    end
    if wm.tick % AiBrainExpansionEvery == 0 then BrainExpandDecision(pi, wm, race) end
    if wm.tick > AiBrainNavalStartTick and wm.tick % AiBrainNavalEvery == 0 then
        BrainNavalDecision(pi, wm, race)
    end
    AiRecycleBuilders(pi, 4)
    return built
end

return "F1 hotpatch applied"
