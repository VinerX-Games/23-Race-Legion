
-- ***************************************************************************
-- *  TryToBuild
---@return nothing
function TryBuild()
    gUnit = TryBuild_u
    if gUnit == nil then return end
    gPi = GetPlayerId(GetOwningPlayer(gUnit))
    gX = GetUnitX(gUnit)
    gY = GetUnitY(gUnit)

    GroupAddUnit(udg_Ai_buildersT[gPi], gUnit)
    GroupRemoveUnit(udg_Ai_builders[gPi], gUnit)
    GroupRemoveUnit(udg_Ai_harvest[gPi], gUnit)

    gInt = AiData[gPi][StringHash("NumberPorts")] or 0
    if gInt < 3 and AiRaceUsesWaterPoint(gPi) and Random(1, 15) and GoToWaterPoint(gPi, gUnit, gX, gY) then
        return
    end

    -- 4% chance: walk far away to expand to a new base location
    if Random(1, 25) then
        gX = gX + AiBuildingRadius * 7 * Cos(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
        gY = gY + AiBuildingRadius * 7 * Sin(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
        IssuePointOrder(gUnit, "move", gX, gY)
        return
    end

    gInt = AiDispatchChooseBuild(gPi)
    if AiSmartBuild then
        local bx, by = AiFindBuildSpot(gPi, gUnit)
        if bx ~= nil then
            BrainLogEvery(gPi, "build", 6, "smart spot x=" .. tostring(R2I(bx)) .. " y=" .. tostring(R2I(by)) .. " build=" .. tostring(gInt), "BRAINBLD")
            IssueBuildOrderById(gUnit, gInt, bx, by)
            return
        end
    end
    gX = gX + AiBuildingRadius * Cos(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
    gY = gY + AiBuildingRadius * Sin(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
    IssueBuildOrderById(gUnit, gInt, gX, gY)
end