
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
	local radius = 3000.00 * (Pow(1.5, I2R(i)))
	local useP = (abilityLevel ~= 2)
	GroupEnumUnitsInRange(l__gEnemyGroup, l__gX, l__gY, radius, nil)
	if abilityLevel >= 2 then
		UnitRemoveAbility(u, FourCC('A1GZ'))
	end
	-- Post-enum filter loop: same logic as f_EnemyUnitP/f_EnemyUnit but safe (Lua context)
	local sz = BlzGroupGetSize(l__gEnemyGroup)
	local keep = {}
	local ki = 0
	for idx = 0, sz - 1 do
		local eu = BlzGroupUnitAt(l__gEnemyGroup, idx)
		if eu ~= nil and GetUnitState(eu, UNIT_STATE_LIFE) > 0.405 then
			local ep = GetOwningPlayer(eu)
			if IsPlayerEnemy(ep, CheckPlayer) then
				local isWaygate = WaygateIsActive(eu)
				if useP then
					-- f_EnemyUnitP: keep if alive-enemy OR (waygate and not navy/mage)
					local keepIt = true
					if isWaygate and (IsUnitInGroup(eu, Navy) or GetUnitAbilityLevel(eu, FourCC('A1MS')) > 0) then
						keepIt = false
					end
					if keepIt then
						Counter = Counter + 1
						if IsUnitInGroup(eu, udg_StolicaGroups) then EnemyCapital = eu end
						ki = ki + 1; keep[ki] = eu
					end
				else
					-- f_EnemyUnit: keep if alive-enemy AND NOT (waygate/navy/mage)
					if not isWaygate and not IsUnitInGroup(eu, Navy) and GetUnitAbilityLevel(eu, FourCC('A1MS')) == 0 then
						Counter = Counter + 1
						if IsUnitInGroup(eu, udg_StolicaGroups) then EnemyCapital = eu end
						ki = ki + 1; keep[ki] = eu
					end
				end
			end
		end
	end
	-- Rebuild group with kept units only
	GroupClear(l__gEnemyGroup)
	for j = 1, ki do GroupAddUnit(l__gEnemyGroup, keep[j]) end
	
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
	-- Safe post-filter: replaces B_LazyF Condition filter on gAllyGroup.
	-- Removes units that fail IsAiCombatRetaskable + IsUnitInGroup(army), returns count.
	local function LazyFilterAllyGroup(g)
		local armyGrp = udg_Ai_army[GetPlayerId(CheckPlayer)]
		local count = 0
		local sz = BlzGroupGetSize(g)
		local i = 0
		while i < sz do
			local u = BlzGroupUnitAt(g, i)
			if u ~= nil and IsAiCombatRetaskable(u) and armyGrp ~= nil and IsUnitInGroup(u, armyGrp) then
				count = count + 1; i = i + 1
			else
				if u ~= nil then GroupRemoveUnit(g, u) end
				sz = sz - 1
			end
		end
		return count
	end
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
				GroupEnumUnitsInRange(gAllyGroup, gX, gY, 2500 * AiRadius / 5, nil)
				local allyCount = LazyFilterAllyGroup(gAllyGroup)
				
				
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
				GroupEnumUnitsInRange(gAllyGroup, gX, gY, 1500 * AiRadius / 5, nil)
				local allyCount = LazyFilterAllyGroup(gAllyGroup)
				if allyCount == 0 then
					AiProbeLogLimited(pi_attack, "Log_TryAttack_NoGroupAlliesFast", 8, "[AIARMY] no-allies pi=" .. tostring(pi_attack) .. " mode=group-fast targetId=" .. tostring(GetUnitTypeId(gEnemy)))
				end
				gSubGroupCounter = 0
            GroupClear(gSubGroup)
                local gSize = BlzGroupGetSize(gAllyGroup)
                local gIdx = gSize
                while gIdx >= 1 do
                    gUnit2 = BlzGroupUnitAt(gAllyGroup, gIdx)
                    gIdx = gIdx - 1
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

                    if GetUnitAbilityLevel(gUnit2, FourCC('Bvul')) > 0 then
                        gUnit2 = ReplaceUnit2(gUnit2, GetUnitTypeId(gUnit2), bj_UNIT_STATE_METHOD_RELATIVE)
                    end

                    GroupAddUnit(gSubGroup, gUnit2)
                    gSubGroupCounter = gSubGroupCounter + 1
                    if gSubGroupCounter >= 12 then
                        GroupPointOrder(gSubGroup, "attack", gX2, gY2)
                        GroupClear(gSubGroup)
                        gSubGroupCounter = 0
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
					GroupEnumUnitsInRange(gAllyGroup, gX, gY, 2500 * AiRadius / 5, nil)
					local allyCount = LazyFilterAllyGroup(gAllyGroup)
					
					
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
					GroupEnumUnitsInRange(gAllyGroup, gX, gY, 1500 * AiRadius / 5, nil)
					local allyCount = LazyFilterAllyGroup(gAllyGroup)
					if allyCount == 0 then
						AiProbeLogLimited(pi_attack, "Log_TryAttack_NoGroupAlliesWide", 8, "[AIARMY] no-allies pi=" .. tostring(pi_attack) .. " mode=group-wide targetId=" .. tostring(GetUnitTypeId(gEnemy)))
					end
				gSubGroupCounter = 0
			GroupClear(gSubGroup)
                local gSize = BlzGroupGetSize(gAllyGroup)
                local gIdx = gSize
                while gIdx >= 1 do
                    gUnit2 = BlzGroupUnitAt(gAllyGroup, gIdx)
                    gIdx = gIdx - 1

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

                    --  ???????? ? ???????
                    if GetUnitAbilityLevel(gUnit2, FourCC('Bvul')) > 0 then
                        gUnit2 = ReplaceUnit2(gUnit2, GetUnitTypeId(gUnit2), bj_UNIT_STATE_METHOD_RELATIVE)
                    end

                    GroupAddUnit(gSubGroup, gUnit2)
                    gSubGroupCounter = gSubGroupCounter + 1
                    if gSubGroupCounter >= 12 then
                        GroupPointOrder(gSubGroup, "attack", gX2, gY2)
                        GroupClear(gSubGroup)
                        gSubGroupCounter = 0
                    end

                    gUnit2 = nil
				end
					
					
					
				end
				
				
			end
			
		end
		
		UnitRemoveAbility(gUnit, FourCC('A1GZ'))
		
	end
	
end