
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

    -- Workers: join builder pool, call TryBuild immediately.
    -- PlayerBuilders will retry from buildersT pool on timer.
    if IsUnitType(u, UNIT_TYPE_PEON) then
        GroupAddUnit(udg_Ai_builders[pi], u)
        TryBuild_u = u
        TryBuild()
    end
end