AiNavalBuildUntil = AiNavalBuildUntil or {}
AiNavalBuildGrace = 200
g_NavalSpots = {}

local function AiTerrainWater(x, y) return not IsTerrainPathable(x, y, PATHING_TYPE_FLOATABILITY) end
local function AiTerrainLand(x, y)  return not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) end

local function AiNavalFootprintWater(x, y)
    if not AiTerrainWater(x, y) then return false end
    local r1, r2 = 256.0, 128.0
    local o = { {r1,0},{-r1,0},{0,r1},{0,-r1},{r1,r1},{-r1,-r1},{r1,-r1},{-r1,r1},
                {r2,0},{-r2,0},{0,r2},{0,-r2} }
    for i = 1, 12 do
        if not AiTerrainWater(x + o[i][1], y + o[i][2]) then return false end
    end
    return true
end
local function AiNavalLandWithin(x, y, rad)
    for i = 0, 11 do
        local a = (I2R(i) / 12.0) * 2.0 * bj_PI
        if AiTerrainLand(x + rad * Cos(a), y + rad * Sin(a)) then return true end
    end
    return false
end

function AiFindNavalSpots(pi, cx, cy)
    if g_NavalSpots[pi] ~= nil then return g_NavalSpots[pi] end
    local spots = {}
    local r = 384.0
    while r <= 8000.0 and #spots < 8 do
        local s = 0
        while s < 36 do
            local ang = (I2R(s) / 36.0) * 2.0 * bj_PI
            local x = cx + r * Cos(ang)
            local y = cy + r * Sin(ang)
            if AiNavalFootprintWater(x, y) and AiNavalLandWithin(x, y, 640.0) then
                spots[#spots + 1] = { x = x, y = y }
            end
            s = s + 1
        end
        r = r + 384.0
    end
    g_NavalSpots[pi] = spots
    return spots
end

function BrainNavalDecision(pi, wm, race)
    local shipType = race.wall
    if shipType == nil or not AiTransportTypes[shipType] then shipType = race.shipyard end
    if shipType == nil or not AiTransportTypes[shipType] then return end
    if AiCountBuildingsOfType(pi, shipType) >= AiBrainMaxPorts then return end
    local cx, cy = wm.capX, wm.capY
    if cx == nil then return end
    local spots = AiFindNavalSpots(pi, cx, cy)
    if #spots == 0 then return end
    local worker = AiFindFreeWorker(pi)
    if worker == nil then return end
    local now = AiBrainTickCounter or 0
    for _, sp in ipairs(spots) do
        local key = pi .. ",nav," .. R2I(sp.x) .. "," .. R2I(sp.y)
        local resAt = g_BuildSpotReserved[key]
        if resAt == nil or (now - resAt) >= g_BuildReserveTicks then
            g_BuildSpotReserved[key] = now
            TryBuild_u = worker
            if TryBuildWithType(shipType, sp.x, sp.y) then
                AiNavalBuildUntil[worker] = now + AiNavalBuildGrace
            end
            return
        end
    end
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
            local navalUntil = AiNavalBuildUntil[u]
            local navalBusy = navalUntil ~= nil and now < navalUntil
            if expired and not navalBusy and not AiWorkerIsBuilding(pi, u) then
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
        AiNavalBuildUntil[u] = nil
        IssueImmediateOrder(u, "autoharvestlumber")
    end
end
return "naval logic + recycle exemption hot-patched"
