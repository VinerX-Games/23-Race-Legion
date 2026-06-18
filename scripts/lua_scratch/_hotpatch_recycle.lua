function AiWorkerIsBuilding(pi, u)
    local p = Player(pi)
    if gWorkerProbe == nil then gWorkerProbe = CreateGroup() end
    GroupEnumUnitsInRange(gWorkerProbe, GetUnitX(u), GetUnitY(u), 256, nil)
    local sz = BlzGroupGetSize(gWorkerProbe)
    local building = false
    for k = 0, sz - 1 do
        local b = BlzGroupUnitAt(gWorkerProbe, k)
        if b ~= nil and GetOwningPlayer(b) == p
            and IsUnitType(b, UNIT_TYPE_STRUCTURE)
            and GetUnitState(b, UNIT_STATE_LIFE) > 0.405
            and GetUnitStatePercent(b, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < 99.0 then
            building = true
            break
        end
    end
    GroupClear(gWorkerProbe)
    return building
end

function AiRecycleBuilders(pi, maxMove)
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
    local i = 0
    while i < sz and found < cap do
        local u = BlzGroupUnitAt(grpT, i)
        if u ~= nil and GetUnitState(u, UNIT_STATE_LIFE) > 0.405 then
            local c = AiBuildClaim[u]
            local expired = c == nil or (now - c) >= AiBuildClaimTicks
            if expired and not AiWorkerIsBuilding(pi, u) then
                if victims == nil then victims = {} end
                found = found + 1
                victims[found] = u
            end
        end
        i = i + 1
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
return "recycle+AiWorkerIsBuilding hot-patched"
