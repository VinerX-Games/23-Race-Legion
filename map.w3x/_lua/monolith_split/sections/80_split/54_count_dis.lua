-- *  CountAddDis and CountDelDis
---@param u unit
---@param pi integer
---@return nothing
function AddCountDis(u, pi)
	local i
	-- ????????? ??????????? ? ?????    
	
	if u == nil then
		return 
	end
	
	--  ???? ?????? ??? ??? ?????????
	if (IsUnitType(u, UNIT_TYPE_STRUCTURE) or GetUnitAbilityLevel(u, FourCC('A1IJ')) > 0) then
		if IsUnitInGroup(u, udg_BuildedSctructure[1]) then
			income[pi] = income[pi] + I2R(GetUnitFoodMade(u))
			
			-- ????????? ?????????? 
			if GetUnitAbilityLevel(u, FourCC('A0AY')) >= 1 then
				income[pi] = (income[pi] + (100.00 * I2R(GetUnitAbilityLevel(u, FourCC('A0AY')))))
			elseif GetUnitAbilityLevel(u, FourCC('A0SM')) >= 1 then
				income[pi] = (income[pi] + (75.00 * I2R(GetUnitAbilityLevel(u, FourCC('A0SM')))))
			elseif GetUnitAbilityLevel(u, FourCC('A0VS')) == 1 then
				income[pi] = (income[pi] + 100)
			end
			
			if GetUnitAbilityLevel(u, FourCC('A1HS')) > 0 then
				income[pi] = (income[pi] - 5)
				i = LoadInteger(Hash, GetHandleId(u), 0)
				income[i] = (income[i] + 5)
			end
			
			
			i = GetUnitAbilityLevel(u, FourCC('A0B5'))
			if i > 0 then
				incomeW[pi] = incomeW[pi] + (50.00 * i)
			end
		end
		
		--  ???? ?????
	else
		-- ??? ?? ????????? ???????, ?? ??????
		if  not IsUnitType(u, UNIT_TYPE_SUMMONED) then
			
			udg_UnitsCount[pi] = udg_UnitsCount[pi] + 1
			-- call DisplayTextToPlayer(p,0,0,I2S(udg_UnitsCount[pi]))
			
			
			if IsUnitType(u, UNIT_TYPE_HERO) then
				disincome[pi] = (disincome[pi] + 100.00)
				if GetUnitAbilityLevel(u, FourCC('A0XV')) ~= 0 then	--  ???????????? ??????
					income[pi] = income[pi] + (100 + GetUnitAbilityLevel(u, FourCC('A0XV')) * 100)
				end
				
			else
				udg_Price = GetUnitGoldCost(GetUnitTypeId(u)) or 0
				disincome[pi] = (disincome[pi] + (udg_Price * Tax))
				--  ---------------------------?????? ???????-----------------------------          +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				--  ---------------------------??????? ????????-----------------------------
				if GetUnitAbilityLevel(u, FourCC('A0A5')) ~= 0 then
					disincome[pi] = disincome[pi] + ((udg_Price * Tax) * (1.60 - (0.10 * I2R(GetUnitAbilityLevel(u, FourCC('A0A5'))))))
					
					--  ---------------------------????????? ?????????-------------------------
				elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 1 then
					disincome[pi] = disincome[pi] - (udg_Price * Tax / 2)
				elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 2 then
					disincome[pi] = disincome[pi] - (udg_Price * Tax / 3 * 2)
					
					-- Horde land
					--    elseif  GetUnitAbilityLevel(u,'OR00')!=0 then
					
					--   set disincome[pi] = disincome[pi] + ( ( udg_Price * Tax ) * ( ( GetUnitAbilityLevel(u,'OR00')-35 )/100.0) )
					
				end
				
				
			end
			
			
			-- ?????? ????????? ? ??????.
		elseif GetUnitAbilityLevel(u, FourCC('A1HL')) > 0 then
			udg_UnitsCount[pi] = udg_UnitsCount[pi] + 1
			udg_Price = GetUnitGoldCost(GetUnitTypeId(u)) or 0
			disincome[pi] = (disincome[pi] + (udg_Price * Tax / 2))
		end
		
	end
	
	
	
	
	UpdateGraf(pi)
	
end
---@param u unit
---@param pi integer
---@return nothing
function DelCountDis(u, pi)
	local i
	-- ??????? ??????????? ? ?????
	
	if u == nil then
		return 
	end
	
	
	-- ????
	-- ??????
	if (IsUnitType(u, UNIT_TYPE_STRUCTURE) or GetUnitAbilityLevel(u, FourCC('A1IJ')) > 0) then
		
		if IsUnitInGroup(u, udg_BuildedSctructure[1]) then
			income[pi] = income[pi] - I2R(GetUnitFoodMade(u))
			
			-- ????????? ??????????
			if GetUnitAbilityLevel(u, FourCC('A0AY')) >= 1 then
				income[pi] = (income[pi] - (100.00 * I2R(GetUnitAbilityLevel(u, FourCC('A0AY')))))
			elseif GetUnitAbilityLevel(u, FourCC('A0SM')) >= 1 then
				income[pi] = (income[pi] - (75.00 * I2R(GetUnitAbilityLevel(u, FourCC('A0SM')))))
			end
			
			if GetUnitAbilityLevel(u, FourCC('A0VS')) == 1 then
				income[pi] = (income[pi] - 100)
			end
			
			if GetUnitAbilityLevel(u, FourCC('A1HS')) > 0 then
				income[pi] = (income[pi] + 5)
				i = LoadInteger(Hash, GetHandleId(u), 0)
				income[i] = (income[i] - 5)
				FlushChildHashtable(Hash, GetHandleId(u))
			end
			
			
			
			i = GetUnitAbilityLevel(u, FourCC('A0B5'))
			if i > 0 then
				incomeW[pi] = incomeW[pi] - (50.00 * i)
			end
		end
		
		-- ?? ??????
		-- ??? ?? ????????? ???????, ?? ??????
	elseif  not IsUnitType(u, UNIT_TYPE_SUMMONED) then
		udg_UnitsCount[pi] = udg_UnitsCount[pi] - 1
		-- ???
		if IsUnitType(u, UNIT_TYPE_HERO) then
			disincome[pi] = (disincome[pi] - 100.00)
			
			
			-- ????????? ??????????
			if GetUnitAbilityLevel(u, FourCC('A0XV')) ~= 0 then
				income[pi] = income[pi] - (100 + GetUnitAbilityLevel(u, FourCC('A0XV')) * 100)
			end
			
			-- ????
		else
			
			
			--  call DisplayTextToPlayer(p,0,0,("?????? ?????? ?? ????? "+GetUnitName(u)))
			udg_Price = GetUnitGoldCost(GetUnitTypeId(u)) or 0
			disincome[pi] = (disincome[pi] - (udg_Price * Tax))
			
			
			-- ????????? ??????????
			--  ---------------------------??????? ????????-----------------------------
			if GetUnitAbilityLevel(u, FourCC('A0A5')) ~= 0 then
				disincome[pi] = disincome[pi] - ((udg_Price * Tax) * (1.60 - (0.10 * I2R(GetUnitAbilityLevel(u, FourCC('A0A5'))))))
				
				--  ---------------------------????????? ?????????------------------------- ??
			elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 1 then
				disincome[pi] = disincome[pi] + (udg_Price * Tax / 2)
			elseif GetUnitAbilityLevel(u, FourCC('A0VH')) == 2 then
				disincome[pi] = disincome[pi] + (udg_Price * Tax / 3 * 2)
			elseif GetUnitAbilityLevel(u, FourCC('OR00')) ~= 0 then
				disincome[pi] = disincome[pi] - ((udg_Price * Tax) * ((GetUnitAbilityLevel(u, FourCC('OR00')) - 35) / 100.0))
				
				-- Horde land
				--  elseif  GetUnitAbilityLevel(u,'OR00')!=0 then                  
				--     set disincome[pi] = disincome[pi] - ( ( udg_Price * Tax ) * ( ( GetUnitAbilityLevel(u,'OR00')-35 )/100.0) )
				
			end
		end
		
		
		
		
		-- ?????? ????????? ? ??????.
	elseif GetUnitAbilityLevel(u, FourCC('A1HL')) > 0 then
		udg_UnitsCount[pi] = udg_UnitsCount[pi] - 1
		udg_Price = GetUnitGoldCost(GetUnitTypeId(u)) or 0
		disincome[pi] = (disincome[pi] - (udg_Price * Tax / 2))
		
	end
	
	UpdateGraf(pi)
	u = nil
end
---@return nothing
function TimedCount(u)
	local t = CreateTimer()
	TimerStart(t, 0.3, false, function()
		DelCountDis(u, GetPlayerId(GetOwningPlayer(u)))
		DestroyTimer(t)
	end)
end
-- ***************************************************************************
