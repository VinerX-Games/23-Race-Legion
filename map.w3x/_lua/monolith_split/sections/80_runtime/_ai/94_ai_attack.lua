
-- ***************************************************************************
-- *  TryToAttack2 Uni
---@param u unit
---@param l__gEnemyGroup group
---@param l__gX real
---@param l__gY real
---@param i integer
---@return nothing
function TryPortalMovement(u, l__gEnemyGroup, l__gX, l__gY, i)
	local abilityLevel = GetUnitAbilityLevel(u, FourCC('A1GZ'))
	if i == 0 then
		i = 20
	end
	
	Counter = 0
	EnemyCapital = nil
	if abilityLevel == 1 then
		GroupEnumUnitsInRange(l__gEnemyGroup, l__gX, l__gY, 3000.00 * (Pow(1.5, I2R(i))), udg_B_EnemyUnitP)
	elseif abilityLevel >= 2 then
		GroupEnumUnitsInRange(l__gEnemyGroup, l__gX, l__gY, 3000.00 * (Pow(1.5, I2R(i))), udg_B_EnemyUnit)
		UnitRemoveAbility(u, FourCC('A1GZ'))
	else
		GroupEnumUnitsInRange(l__gEnemyGroup, l__gX, l__gY, 3000.00 * (Pow(1.5, I2R(i))), udg_B_EnemyUnitP)
	end
	
	-- trace: check if dark portal waygates (n006) are alive/active
	local pi = GetPlayerId(GetOwningPlayer(u))
	local logKey = StringHash("Log_TPM_n006")
	if not (AiData[pi][logKey] or false) then
		AiData[pi][logKey] = true
		local dp1_active = WaygateIsActive(gg_unit_n006_0023)
		local dp1_hp = GetUnitState(gg_unit_n006_0023, UNIT_STATE_LIFE)
		local dp2_active = WaygateIsActive(gg_unit_n006_0438)
		local dp2_hp = GetUnitState(gg_unit_n006_0438, UNIT_STATE_LIFE)
		local dp1_in_group = IsUnitInGroup(gg_unit_n006_0023, l__gEnemyGroup)
		local dp2_in_group = IsUnitInGroup(gg_unit_n006_0438, l__gEnemyGroup)
		ProbeLogWrite("[TPM] pi=" .. tostring(pi) .. " Counter=" .. tostring(Counter) .. " i=" .. tostring(i) .. " n006_0023 active=" .. tostring(dp1_active) .. " hp=" .. tostring(dp1_hp) .. " inGroup=" .. tostring(dp1_in_group) .. " n006_0438 active=" .. tostring(dp2_active) .. " hp=" .. tostring(dp2_hp) .. " inGroup=" .. tostring(dp2_in_group) .. " x=" .. tostring(l__gX) .. " y=" .. tostring(l__gY))
	end
end
---@return nothing
function TryAttack()
	local i
	gUnit = udg_LocalUnit2
	gPlayer = GetOwningPlayer(gUnit)
	local pi_attack = GetPlayerId(gPlayer)
	gX = GetUnitX(gUnit)
	gY = GetUnitY(gUnit)
	--    ------------------- ? ????? -------------------
	
	if gAllyGroup == nil then
		gAllyGroup = CreateGroup()
	end
	if gSubGroup == nil then
		gSubGroup = CreateGroup()
	end
	
	CheckPlayer = gPlayer
	-- // ??????? ????????????
	if Random(1, 8) then
		
		-- ????????? ??????? ? ?????? ????? ??????
		TryPortalMovement(gUnit, gEnemyGroup, gX, gY, 0)
		
		-- /??????????????? ?????
		local cRace = AiRaceOf(GetPlayerId(gPlayer))
		if cRace ~= nil and cRace.continentalNaga then
			ProcessContinentalStuffNaga(gX, gY, gEnemyGroup)
		else
			ProcessContinentalStuff(gX, gY, gEnemyGroup)
		end
		
		Counter = BlzGroupGetSize(gEnemyGroup)
		EnemyCapital = nil
		for i = 0, Counter - 1 do
			local u = BlzGroupUnitAt(gEnemyGroup, i)
			if u ~= nil and IsUnitInGroup(u, udg_StolicaGroups) then
				EnemyCapital = u
				break
			end
		end
		
		--  ???? ???????? ?????? ?? ???????
		if EnemyCapital ~= nil and Random(1, 2) then
			gEnemy = EnemyCapital
		else
			if Counter > 0 then
				gEnemy = BlzGroupUnitAt(gEnemyGroup, GetRandomInt(0, Counter - 1))
			else
				gEnemy = nil
				AiProbeLogLimited(pi_attack, "Log_TryAttack_NoEnemyFast", 8, "[AIARMY] no-enemy pi=" .. tostring(pi_attack) .. " mode=fast seekerId=" .. tostring(GetUnitTypeId(gUnit)))
			end
		end
		
		-- ???? ?? ?????? - ??????????? ??!
		if gEnemy == nil then
			AiProbeLogLimited(pi_attack, "Log_TryAttack_RequestPortFast", 8, "[AIARMY] request-port pi=" .. tostring(pi_attack) .. " mode=fast seekerId=" .. tostring(GetUnitTypeId(gUnit)))
			RequestPort(gUnit)
		else
			
			gX2 = GetUnitX(gEnemy)
			gY2 = GetUnitY(gEnemy)
			
			--  ???? ??? ??????
			if WaygateIsActive(gEnemy) then
				
				gDx = gX - gX2
				gDy = gY - gY2
				gDx = SquareRoot(gDx * gDx + gDy * gDy)
				GroupEnumUnitsInRange(gAllyGroup, gX, gY, 2500 * AiRadius / 5, B_LazyF)
				local allyCount = CountUnitsInGroup(gAllyGroup)
				
				
				-- ? ????? ?????? ????? ???????? ??????? ???????
				
			GroupClear(gSubGroup)
			gSubGroupCounter = 0
			local gSize = BlzGroupGetSize(gAllyGroup)
			for gIdx = 1, gSize do
				gUnit2 = BlzGroupUnitAt(gAllyGroup, gIdx)
				if gUnit2 ~= nil then
					UnitAddAbility(gUnit2, FourCC('A1GZ'))
					GroupAddUnit(gSubGroup, gUnit2)
					gSubGroupCounter = gSubGroupCounter + 1
				end
			end
			-- ?? ??????? ????? ??????
			if gDx <= 2500 then
				
				IssueImmediateOrder(gEnemy, "web")
				BlzEndUnitAbilityCooldown(gEnemy, FourCC('A0HY'))
				
				-- ?? ??????? ???? ???
			else
				local attackLogCount = AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] or 0
				if allyCount == 0 then
					AiProbeLogLimited(pi_attack, "Log_TryAttack_NoPortalAlliesFast", 8, "[AIARMY] no-allies pi=" .. tostring(pi_attack) .. " mode=portal-fast targetId=" .. tostring(GetUnitTypeId(gEnemy)))
				end
				if attackLogCount < 10 then
					AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] = attackLogCount + 1
					ProbeLogWrite("[AIARMY] attack-order pi=" .. tostring(pi_attack) .. " via=portal targetId=" .. tostring(GetUnitTypeId(gEnemy)) .. " allies=" .. tostring(allyCount) .. " x=" .. tostring(gX2) .. " y=" .. tostring(gY2))
				end
				GroupPointOrder(gSubGroup, "smart", gX2, gY2)
				GroupClear(gSubGroup)
				gSubGroupCounter = 0
			end
				
				
				
				
				--  ???????? ??????
			else
				-- set CheckPlayer = gPlayer
				GroupEnumUnitsInRange(gAllyGroup, gX, gY, 1500 * AiRadius / 5, B_LazyF)
				local allyCount = CountUnitsInGroup(gAllyGroup)
				if allyCount == 0 then
					AiProbeLogLimited(pi_attack, "Log_TryAttack_NoGroupAlliesFast", 8, "[AIARMY] no-allies pi=" .. tostring(pi_attack) .. " mode=group-fast targetId=" .. tostring(GetUnitTypeId(gEnemy)))
				end
				gSubGroupCounter = 0
				GroupClear(gSubGroup)
				local gSize = BlzGroupGetSize(gAllyGroup)
				local gIdx = 0
				while gIdx < gSize do
					gIdx = gIdx + 1
					gUnit2 = BlzGroupUnitAt(gAllyGroup, gIdx)
					if gUnit2 == nil then
						local attackLogCount = AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] or 0
						if attackLogCount < 10 then
							AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] = attackLogCount + 1
							ProbeLogWrite("[AIARMY] attack-order pi=" .. tostring(pi_attack) .. " via=group targetId=" .. tostring(GetUnitTypeId(gEnemy)) .. " allies=" .. tostring(allyCount) .. " x=" .. tostring(gX2) .. " y=" .. tostring(gY2))
						end
						GroupPointOrder(gSubGroup, "attack", gX2, gY2)
						GroupClear(gSubGroup)
						gSubGroupCounter = 0
						if true then break end
					end

					GroupAddUnit(gSubGroup, gUnit2)
					gSubGroupCounter = gSubGroupCounter + 1
					if gSubGroupCounter >= 12 then
						GroupPointOrder(gSubGroup, "attack", gX2, gY2)
						GroupClear(gSubGroup)
						gSubGroupCounter = 0
					end

					if GetUnitAbilityLevel(gUnit2, FourCC('Bvul')) > 0 then
						ReplaceUnit2(gUnit2, GetUnitTypeId(gUnit2), bj_UNIT_STATE_METHOD_RELATIVE)
					end

					gUnit2 = nil
				end
			end
		end
		
		
		-- // ????????? ????????????, ???????? ?????????? ?????? ???? ?? ?????? ???? ?? ?????? ?????
	else
		
		
		i = 0
		while true do
			if i > 8 then break end
			i = i + 1
			if i == 8 then
				i = 100
			end
			
			
			-- set CheckPlayer = gPlayer
			
			TryPortalMovement(gUnit, gEnemyGroup, gX, gY, i)
			
			-- /??????????????? ?????
			local cRace = AiRaceOf(GetPlayerId(gPlayer))
			if cRace ~= nil and cRace.continentalNaga then
				ProcessContinentalStuffNaga(gX, gY, gEnemyGroup)
			else
				ProcessContinentalStuff(gX, gY, gEnemyGroup)
			end
			
			Counter = BlzGroupGetSize(gEnemyGroup)
			EnemyCapital = nil
			for i = 0, Counter - 1 do
				local u = BlzGroupUnitAt(gEnemyGroup, i)
				if u ~= nil and IsUnitInGroup(u, udg_StolicaGroups) then
					EnemyCapital = u
					break
				end
			end
			
			--  ???? ???????? ?????? ?? ???????
			if EnemyCapital ~= nil and Random(1, 4) then
				gEnemy = EnemyCapital
			else
				if Counter > 0 then
					gEnemy = BlzGroupUnitAt(gEnemyGroup, GetRandomInt(0, Counter - 1))
				else
					gEnemy = nil
					AiProbeLogLimited(pi_attack, "Log_TryAttack_NoEnemyWide", 8, "[AIARMY] no-enemy pi=" .. tostring(pi_attack) .. " mode=wide seekerId=" .. tostring(GetUnitTypeId(gUnit)) .. " pass=" .. tostring(i))
				end
			end
			
			-- ???? ?? ?????? - ??????????? ??!
			if gEnemy == nil then
				if i == 100 then
					AiProbeLogLimited(pi_attack, "Log_TryAttack_RequestPortWide", 8, "[AIARMY] request-port pi=" .. tostring(pi_attack) .. " mode=wide seekerId=" .. tostring(GetUnitTypeId(gUnit)))
					RequestPort(gUnit)
				end
				-- ???? ??????
			else
				i = 15
				gX2 = GetUnitX(gEnemy)
				gY2 = GetUnitY(gEnemy)
				
				if WaygateIsActive(gEnemy) then
					
					gDx = gX - gX2
					gDy = gY - gY2
					gDx = SquareRoot(gDx * gDx + gDy * gDy)
					GroupEnumUnitsInRange(gAllyGroup, gX, gY, 2500 * AiRadius / 5, B_LazyF)
					local allyCount = CountUnitsInGroup(gAllyGroup)
					
					
					-- ? ????? ?????? ????? ???????? ??????? ???????
					
				GroupClear(gSubGroup)
				gSubGroupCounter = 0
				local gSize = BlzGroupGetSize(gAllyGroup)
				for gIdx = 1, gSize do
					gUnit2 = BlzGroupUnitAt(gAllyGroup, gIdx)
					if gUnit2 ~= nil then
						UnitAddAbility(gUnit2, FourCC('A1GZ'))
						GroupAddUnit(gSubGroup, gUnit2)
						gSubGroupCounter = gSubGroupCounter + 1
					end
				end
				-- ?? ??????? ????? ??????
				if gDx <= 2500 then
					AiProbeLogLimited(pi_attack, "Log_TryAttack_PortalNearby", 8, "[AIARMY] portal-near pi=" .. tostring(pi_attack) .. " targetId=" .. tostring(GetUnitTypeId(gEnemy)) .. " allies=" .. tostring(allyCount))
					
					IssueImmediateOrder(gEnemy, "web")
					BlzEndUnitAbilityCooldown(gEnemy, FourCC('A0HY'))
					
				-- ?? ??????? ???? ???
				else
					if allyCount == 0 then
						AiProbeLogLimited(pi_attack, "Log_TryAttack_NoPortalAlliesWide", 8, "[AIARMY] no-allies pi=" .. tostring(pi_attack) .. " mode=portal-wide targetId=" .. tostring(GetUnitTypeId(gEnemy)))
					end
					local attackLogCount = AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] or 0
					if attackLogCount < 10 then
						AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] = attackLogCount + 1
						ProbeLogWrite("[AIARMY] attack-order pi=" .. tostring(pi_attack) .. " via=portal-wide targetId=" .. tostring(GetUnitTypeId(gEnemy)) .. " allies=" .. tostring(allyCount) .. " x=" .. tostring(gX2) .. " y=" .. tostring(gY2))
					end
					GroupPointOrder(gSubGroup, "smart", gX2, gY2)
					GroupClear(gSubGroup)
					gSubGroupCounter = 0
				end
					
					-- ??????? ????
				else
					
					-- ????? ?????? ????? ? ????? ???????
					
					-- set CheckPlayer = gPlayer
					GroupEnumUnitsInRange(gAllyGroup, gX, gY, 1500 * AiRadius / 5, B_LazyF)
					local allyCount = CountUnitsInGroup(gAllyGroup)
					if allyCount == 0 then
						AiProbeLogLimited(pi_attack, "Log_TryAttack_NoGroupAlliesWide", 8, "[AIARMY] no-allies pi=" .. tostring(pi_attack) .. " mode=group-wide targetId=" .. tostring(GetUnitTypeId(gEnemy)))
					end
				gSubGroupCounter = 0
				GroupClear(gSubGroup)
				local gSize = BlzGroupGetSize(gAllyGroup)
				local gIdx = 0
				while gIdx < gSize do
					gIdx = gIdx + 1
					gUnit2 = BlzGroupUnitAt(gAllyGroup, gIdx)

					if gUnit2 == nil then
						local attackLogCount = AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] or 0
						if attackLogCount < 10 then
							AiData[pi_attack][StringHash("Log_TryAttackOrderCount")] = attackLogCount + 1
							ProbeLogWrite("[AIARMY] attack-order pi=" .. tostring(pi_attack) .. " via=group-wide targetId=" .. tostring(GetUnitTypeId(gEnemy)) .. " allies=" .. tostring(allyCount) .. " x=" .. tostring(gX2) .. " y=" .. tostring(gY2))
						end
						GroupPointOrder(gSubGroup, "attack", gX2, gY2)
						GroupClear(gSubGroup)
						gSubGroupCounter = 0
						if true then break end
					end


					GroupAddUnit(gSubGroup, gUnit2)
					gSubGroupCounter = gSubGroupCounter + 1
					if gSubGroupCounter >= 12 then
						GroupPointOrder(gSubGroup, "attack", gX2, gY2)
						GroupClear(gSubGroup)
						gSubGroupCounter = 0
					end

					--  ???????? ? ???????
					if GetUnitAbilityLevel(gUnit2, FourCC('Bvul')) > 0 then
						ReplaceUnit2(gUnit2, GetUnitTypeId(gUnit2), bj_UNIT_STATE_METHOD_RELATIVE)
					end

					gUnit2 = nil
				end
					
					
					
				end
				
				
			end
			
		end
		
		UnitRemoveAbility(gUnit, FourCC('A1GZ'))
		
	end
	
end