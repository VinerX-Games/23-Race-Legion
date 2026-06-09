
-- ***************************************************************************
-- *  AiUnitJoins
---@param u unit
---@param pi integer
---@return nothing
function aiUnitJoins(u, pi)
    local id = GetUnitTypeId(u)

    GroupAddUnit(udg_Ai_units[pi], u)
    NumberAdd(pi, id)

    AiDispatchJoin(id, pi, u)

    -- Workers: if under builder target, try building; else harvest
    if IsUnitType(u, UNIT_TYPE_PEON) then
        local T = AiData[pi][StringHash("T")] or 0
        local totalWrk = getAiCount(pi, StringHash("T")) + (AiData[pi][StringHash("HV")] or 0)
        local desiredBld = AiBuildersTarget(pi, totalWrk)
        if T < desiredBld then
            NumberAdd(pi, StringHash("T"))
            GroupAddUnit(udg_Ai_buildersT[pi], u)
            GroupRemoveUnit(udg_Ai_builders[pi], u)
            TryBuild_u = u
            TryBuild()
        else
            IssueImmediateOrder(u, "autoharvestlumber")
        end
    end
end