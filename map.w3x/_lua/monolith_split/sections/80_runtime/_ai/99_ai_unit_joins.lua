
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

    -- Workers: issue harvest immediately instead of waiting for PlayerBuilders tick
    if IsUnitType(u, UNIT_TYPE_PEON) then
        IssueImmediateOrder(u, "autoharvestlumber")
    end
end