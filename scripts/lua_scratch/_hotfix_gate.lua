-- HOTFIX: BrainProduce gate-aware trainability filtering
-- When computing isTrainable/trainableSum, skip units whose gate is not met.
-- This prevents gated units from bloating trainableSum and starving actually-trainable units.

do
    local _origBrainProduce = BrainProduce
    function BrainProduce(pi, wm, race)
        local prod = race.production
        local comp = race.compTarget
        if not prod then return 0 end

        local ordered = 0
        local maxN = AiBrainMaxProduce
        local now = AiBrainTickCounter or 0

        -- R7: isBldType set
        local isBldType = {}
        local buildList = race.buildings
        if buildList then
            isBldType[buildList.seed] = true
            for _, row in ipairs(buildList) do
                if type(row[1]) == "number" then isBldType[row[1]] = true end
            end
        end
        for k, _ in pairs(prod) do
            if type(k) == "number" then isBldType[k] = true end
        end

        -- 1) Workers
        local w = prod.worker
        if w and w.from and w.id then
            local wCnt = getAiCount(pi, w.id) or 0
            if wCnt < (w.cap or 40) then
                for _, fromBldType in ipairs(w.from) do
                    local bld = AiFindProdBuilding(pi, fromBldType)
                    if bld ~= nil then
                        local key = pi * 1000000 + w.id
                        local last = g_AiOrdered[key]
                        if not last or (now - last) > AiRetrainInterval then
                            IssueImmediateOrderById(bld, w.id)
                            g_AiOrdered[key] = now
                            ordered = ordered + 1
                        end
                        break
                    end
                end
            end
        end

        if not comp then return ordered end

        local totalMil = wm.armyCount or 0
        if totalMil < 1 then totalMil = 1 end
        local ratioBase = math.max(totalMil, AiBrainMinArmy)

        -- HOTFIX: gate check helper
        local function gateOk(gateName)
            if gateName == nil then return true end
            local gates = race.gates
            if gates == nil then return true end
            local fn = gates[gateName]
            if fn == nil then return true end
            local ok, res = pcall(fn, pi)
            return ok and res
        end

        -- R15 + GATE: compute trainableSum only for units whose gate is met
        local trainableSum = 0.0
        local isTrainable = {}
        for unitId, targetRatio in pairs(comp) do
            if type(unitId) ~= "number" then goto nextSum2 end
            for bldType, rows in pairs(prod) do
                if bldType == "worker" then goto nextBldSum2 end
                if type(rows) ~= "table" then goto nextBldSum2 end
                if not isBldType[bldType] then goto nextBldSum2 end
                for _, row in ipairs(rows) do
                    if row.branch then
                        local pick
                        if race.branches and race.branches[row.branch] then
                            pick = race.branches[row.branch](pi)
                        end
                        pick = pick and row.black or row.other
                        if pick == unitId then
                            if gateOk(row.gate) and AiFindProdBuilding(pi, bldType) ~= nil then
                                isTrainable[unitId] = true
                                trainableSum = trainableSum + targetRatio
                                goto found2
                            end
                        end
                    elseif row[1] == unitId and row[1] ~= nil and row[1] ~= 0 then
                        if gateOk(row.gate) and AiFindProdBuilding(pi, bldType) ~= nil then
                            isTrainable[unitId] = true
                            trainableSum = trainableSum + targetRatio
                            goto found2
                        end
                    end
                end
                ::found2::
                ::nextBldSum2::
            end
            ::nextSum2::
        end
        if trainableSum <= 0 then trainableSum = 1.0 end

        -- 2) Military: scan compTarget, skip untrainable or gated
        for unitId, targetRatio in pairs(comp) do
            if ordered >= maxN then break end
            if type(unitId) ~= "number" or targetRatio == nil then goto skipU2 end
            if not isTrainable[unitId] then goto skipU2 end

            local current = getAiCount(pi, unitId) or 0
            if current < 0 then current = 0 end
            local scaledTarget = targetRatio / trainableSum
            local currentRatio = current / ratioBase
            if currentRatio >= scaledTarget then goto skipU2 end

            for bldType, rows in pairs(prod) do
                if bldType == "worker" then goto skipB2 end
                if type(rows) ~= "table" then goto skipB2 end
                if not isBldType[bldType] then goto skipB2 end
                for _, row in ipairs(rows) do
                    local uid = row[1]
                    if uid ~= nil and uid ~= 0 then
                        if uid == unitId then
                            local bld = AiFindProdBuilding(pi, bldType)
                            if bld ~= nil then
                                local key = pi * 1000000 + unitId
                                local last = g_AiOrdered[key]
                                if not last or (now - last) > AiRetrainInterval then
                                    IssueImmediateOrderById(bld, unitId)
                                    g_AiOrdered[key] = now
                                    ordered = ordered + 1
                                end
                            end
                            goto skipB2
                        end
                    elseif row.branch then
                        local pick
                        if race.branches and race.branches[row.branch] then
                            pick = race.branches[row.branch](pi)
                        end
                        pick = pick and row.black or row.other
                        if pick == unitId then
                            local bld = AiFindProdBuilding(pi, bldType)
                            if bld ~= nil then
                                local key = pi * 1000000 + unitId
                                local last = g_AiOrdered[key]
                                if not last or (now - last) > AiRetrainInterval then
                                    IssueImmediateOrderById(bld, unitId)
                                    g_AiOrdered[key] = now
                                    ordered = ordered + 1
                                end
                            end
                            goto skipB2
                        end
                    end
                end
                ::skipB2::
            end
            ::skipU2::
        end

        return ordered
    end

    ProbeLogWrite("[HOTFIX] BrainProduce: gate-aware trainability filtering")
end

return 'BrainProduce gate-hotfix applied'
