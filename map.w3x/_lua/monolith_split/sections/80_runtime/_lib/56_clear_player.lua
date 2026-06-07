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
	
	
	DestroyGroup(g)
	g = nil
end
-- ***************************************************************************
