
-- ***************************************************************************
-- *  TimedUpdate
---@return nothing
function TimedUpdateCheck()
	local t = GetExpiredTimer()
	local id = GetHandleId(t)
	local u = LoadUnitHandle(Hash, id, 1)
	local p = LoadPlayerHandle(Hash, id, 2)
	local currentLevel = LoadInteger(Hash, id, 3)
	
	
	
	local levels = 4
	local pi = GetPlayerId(p)
	
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1N9')) > 0 then
		levels = levels - 2
	end
	
	
	if GetOwningPlayer(u) == p and UnitAlive(u) and currentLevel <= levels then
		
		-- Development
		BlzStartUnitAbilityCooldown(u, FourCC('A10G'), 300)
		-- call BlzSetUnitAbilityCooldown(u,'A10G',1,300)
		
		-- Golda
		if GetUnitAbilityLevel(u, FourCC('A0AY')) == 0 then
			UnitAddAbility(u, FourCC('A0AY'))
			income[pi] = income[pi] + 100
			
			
		elseif GetUnitAbilityLevel(u, FourCC('A0AY')) < levels then
			income[pi] = income[pi] + 100
			IncUnitAbilityLevel(u, FourCC('A0AY'))
			
		else	-- if GetUnitAbilityLevel(u, FourCC('A0AY')) >= levels then
			income[pi] = income[pi] + 100
			UnitRemoveAbility(u, FourCC('A0AZ'))
			
			
		end
		
		-- Lumber
		if GetUnitAbilityLevel(u, FourCC('A0B5')) == 0 then
			UnitAddAbility(u, FourCC('A0B5'))
			incomeW[pi] = incomeW[pi] + 50.00
		elseif GetUnitAbilityLevel(u, FourCC('A0B5')) < levels then
			IncUnitAbilityLevel(u, FourCC('A0B5'))
			incomeW[pi] = incomeW[pi] + 50.00
		else	-- if GetUnitAbilityLevel( u,FourCC('A0B5') ) >= levels then
			UnitRemoveAbility(u, FourCC('A0B1'))
			
		end
		
		if GetUnitAbilityLevel(u, FourCC('A0AY')) + GetUnitAbilityLevel(u, FourCC('A0B5')) >= levels * 2 then
			-- ????????
			BlzUnitHideAbility(u, FourCC('A10G'), true)
			BlzUnitDisableAbility(u, FourCC('A10G'), true, true)
			
			
		end
		
		UpdateGraf(pi)
		u = nil
		p = nil
		SaveInteger(Hash, id, 3, currentLevel + 1)
		TimerStart(t, 300, false, TimedUpdateCheck)
		t = nil
		
	else
		u = nil
		p = nil
        FlushChildHashtable(Hash, id)
        DestroyTimer(t)
        t = nil
	end
end
---@param u unit
---@param p player
---@return nothing
function TimedUpdate(u, p)
	local t = CreateTimer()
	local id = GetHandleId(t)
	
	UnitAddAbility(u, FourCC('A10G'))
	BlzStartUnitAbilityCooldown(u, FourCC('A10G'), 300)
	TimerStart(t, 300, false, TimedUpdateCheck)
	SaveUnitHandle(Hash, id, 1, u)
	SavePlayerHandle(Hash, id, 2, p)
	SaveInteger(Hash, id, 3, 1)
	
	u = nil
	p = nil
	t = nil
	
	
end