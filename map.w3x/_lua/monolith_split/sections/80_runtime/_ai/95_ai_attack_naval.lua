
-- ***************************************************************************
-- *  TryToAttackN Uni
---@return nothing
function TryAttackN()
	local ChosenUnit = udg_LocalUnit3
	local u2
	local x = GetUnitX(ChosenUnit)
	local y = GetUnitY(ChosenUnit)
	local x2
	local y2
	
	
	--  ???? ?? ??????? ????????????
	if Random(1, 10) then
		gInt = 10
	else
		gInt = 1
	end
	
	
	while true do
		
		-- call BJDebugMsg("???? ????? ????? ?????: "+GetUnitName(ChosenUnit)+" ??????:"+GetPlayerName(CheckPlayer))
		-- ???? ?????? ??????
		
		Counter = 0
		CheckPlayer = GetOwningPlayer(ChosenUnit)
		GroupEnumUnitsInRange(gEnemyGroup, x, y, 5500.00 * (Pow(1.5, I2R(gInt))), udg_B_EnemyUnitN)
		
		-- call BJDebugMsg("???-?? ????????? ??????"+I2S(Counter))
		-- ???? ?????? ???????
		u2 = BlzGroupUnitAt(gEnemyGroup, GetRandomInt(0, Counter - 1))
		if u2 ~= nil then
			
			-- call BJDebugMsg("????????? ???? "+GetUnitName(u2))
			x2 = GetUnitX(u2)
			y2 = GetUnitY(u2)
			u2 = nil
			
			LazyCount = 0
			CheckPlayer = GetOwningPlayer(ChosenUnit)
			GroupEnumUnitsInRange(gAllyGroup, x, y, (2000 * AiRadius) / 5, B_LazyN)
			gSubGroupCounter = 0
			GroupClear(gSubGroup)
			
			while true do
				u2 = FirstOfGroup(gAllyGroup)
				
				if u2 == nil then
					GroupPointOrder(gSubGroup, "attack", x2, y2)
					GroupClear(gSubGroup)
					gSubGroupCounter = 0
					if true then break end
				end
				GroupRemoveUnit(gAllyGroup, u2)
				
				
				GroupAddUnit(gSubGroup, u2)
				gSubGroupCounter = gSubGroupCounter + 1
				if gSubGroupCounter >= 12 then
					GroupPointOrder(gSubGroup, "attack", x2, y2)
					GroupClear(gSubGroup)
					gSubGroupCounter = 0
				end
			end
			
			gInt = 11
		else
			gInt = gInt + 1
		end
		
		if gInt > 10 then break end
		
		
	end
	
	-- call BJDebugMsg("------------------------- ")
	
	ChosenUnit = nil
	u2 = nil
	
end