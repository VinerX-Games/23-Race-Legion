
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

    -- Workers: immediate harvest, PlayerBuilders timer will assign building tasks
    if IsUnitType(u, UNIT_TYPE_PEON) then
        IssueImmediateOrder(u, "autoharvestlumber")
    end
end