
-- ***************************************************************************
-- *  TryToBuild
---@return nothing
function TryBuild()
	gUnit = TryBuild_u
	if gUnit == nil then
		return 
	end
	gPi = GetPlayerId(GetOwningPlayer(gUnit))
	gX = GetUnitX(gUnit)
	gY = GetUnitY(gUnit)
	
	
	-- call DisplayTimedTextFromPlayer( Player( 0x00 ), 0, 0, 4, "????? ? ????" )
	
	GroupAddUnit(udg_Ai_buildersT[gPi], gUnit)
	GroupRemoveUnit(udg_Ai_builders[gPi], gUnit)
	GroupRemoveUnit(udg_Ai_harvest[gPi], gUnit)
	
	
	-- Стены и порты: стройка на месте (если рядом берег)
	gInt = AiData[gPi][StringHash("NumberPorts")] or 0
	if gInt < 12 and ( not IsTerrainPathable(gX, gY, PATHING_TYPE_WALKABILITY) and not (RectContainsCoords(gg_rct_Outland, gX, gY)) and not (RectContainsCoords(gg_rct_Azgel, gX, gY))) then
		
		if Random(1, 2) then
			
			gInt2 = 0
			
			while true do
				if gInt2 >= 12 then break end
				gInt2 = gInt2 + 1
				
				gX2 = gX + GetRandomReal(200.00, 1000.00) * Cos(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
				gY2 = gY + GetRandomReal(200.00, 1000.00) * Sin(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
				
				if  not (IsTerrainPathable(gX2, gY2, PATHING_TYPE_WALKABILITY) or IsTerrainPathable(gX2, gY2, PATHING_TYPE_FLOATABILITY) or RectContainsCoords(gg_rct_Outland, gX2, gY2)) then
					
					
					if AiDispatchWallBuild(gPi, gUnit, gX2, gY2) then
						return 
					end
				end
				
			end
		end
		
		
	end
	
	-- Стены и порты: поход к водной точке (шанс тем выше, чем меньше верфей)
	if gInt < 8 and AiRaceUsesWaterPoint(gPi) and GoToWaterPoint(gPi, gUnit, gX, gY) then
		return 
	end
	
	-- ???? ??????? ?? ????? ????
	if Random(1, 25) then
		gX = gX + AiBuildingRadius * 7 * Cos(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
		gY = gY + AiBuildingRadius * 7 * Sin(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
		IssuePointOrder(gUnit, "move", gX, gY)
		return 
	end
	
	
	--  ??????????? ????? ????????? 
	gX = gX + AiBuildingRadius * Cos(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
	gY = gY + AiBuildingRadius * Sin(GetRandomReal(0.00, 360.00) * bj_DEGTORAD)
	
	
	
	gInt = AiDispatchChooseBuild(gPi)
	
	IssueBuildOrderById(gUnit, gInt, gX, gY)
	
end