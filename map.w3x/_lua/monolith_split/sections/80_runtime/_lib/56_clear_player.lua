
-- call ClearEc(GetPlayerId(GetEnumPlayer()))
-- ***************************************************************************
-- *  ClearPlayer
---@return nothing
function KillAll()
	local u = GetEnumUnit()
	local id = GetUnitTypeId(u)
	local p = GetOwningPlayer(u)
	if IsUnitInGroup(u, udg_ZahvatBuildings) or GetUnitAbilityLevel(u, FourCC('A1HJ')) > 0 then
		SetUnitOwner(u, Player(25), true)
		SetUnitLifePercentBJ(u, 100)
	elseif IsUnitInGroup(u, udg_StolicaGroups) then
		RemoveUnit(u)
	else
		-- ?????? ?????? ?????
		if id == FourCC('h0KS') then
			UnitRemoveAbility(u, FourCC('A18O'))
		end
		if IsUnitType(u, UNIT_TYPE_HERO) then
			SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
		end
		RemoveUnit(u)
	end
	
	u = nil
	p = nil
end
---@param p player
---@return nothing
function ClearPlayer(p)
	local pi = GetPlayerId(p)
	local g = CreateGroup()
	
	GroupEnumUnitsOfPlayer(g, p, nil)
	ForGroup(g, KillAll)
	GroupClear(g)
	SetPlayerStateBJ(Player(pi), PLAYER_STATE_RESOURCE_GOLD, 0)
	SetPlayerStateBJ(Player(pi), PLAYER_STATE_RESOURCE_LUMBER, 0)
	
	SetPlayerAbilityAvailable(Player(pi), FourCC('A0IQ'), true)
	ClearEc(pi)
	turnOffAi(pi)
	UpdateGraf(pi)
	playerCapital[pi] = nil
	ArmyExp[pi] = 0.0
	
	-- Vassal cleanup when in Feoda mode
	if IsTriggerEnabled(gg_trg_FeodalDead) and CountPlayersInForceBJ(Vassals[pi]) > 0 then
		local inheritedSenior = Senior[pi]
		if FeodalVassalMode == 1 then
			-- Mode 1: transfer vassals to the senior's senior
			if inheritedSenior ~= nil then
				local inheritedPi = GetPlayerId(inheritedSenior)
				ForForce(Vassals[pi], function()
					local v = GetEnumPlayer()
					local vi = GetPlayerId(v)
					ClearOldAllies(v)
					Senior[vi] = inheritedSenior
					ForceAddPlayer(Vassals[inheritedPi], v)
					NewAlly(v)
				end)
				DisplayTextToForce(udg_AllPlayers, GetPlayerName(inheritedSenior) .. " inherited vassals of dead player " .. GetPlayerName(p))
			else
				-- No senior — free all vassals
				ForForce(Vassals[pi], Freedom)
			end
		else
			-- Mode 2: all vassals are eliminated
			ForForce(Vassals[pi], function()
				local v = GetEnumPlayer()
				ClearPlayer(v)
			end)
			DisplayTextToForce(udg_AllPlayers, "Vassals of dead player " .. GetPlayerName(p) .. " are eliminated!")
		end
		-- Remove ourselves from our senior's vassal force
		if inheritedSenior ~= nil then
			ForceRemovePlayer(Vassals[GetPlayerId(inheritedSenior)], Player(pi))
		end
	end
	ForceClear(Vassals[pi])
	Senior[pi] = nil
	
	DestroyGroup(g)
	g = nil
end