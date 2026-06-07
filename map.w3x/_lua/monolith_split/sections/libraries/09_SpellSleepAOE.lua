-- library SpellSleepAOE:
---@param level integer
---@return integer
function SpellSleepAOE___getRange(level)
	local range = {}
	range[1] = 185	--  2 уровень
	range[2] = 275	--  3 уровень
	range[3] = 365
	range[4] = 430
	return range[level]
end
---@param caster unit
---@param target unit
---@return nothing
function SpellSleepAOE___DummyCastBuff(caster, target)
	if (GetUnitState(target, UNIT_STATE_LIFE) > 0.405) then
		SetUnitX(SpellSleepAOE___DummyUnit, GetUnitX(target))
		SetUnitY(SpellSleepAOE___DummyUnit, GetUnitY(target))
		SetUnitAbilityLevel(SpellSleepAOE___DummyUnit, SpellSleepAOE___SpellCast, GetUnitAbilityLevel(caster, SpellSleepAOE___SpellHero))
		IssueTargetOrder(SpellSleepAOE___DummyUnit, SpellSleepAOE___SpellOrder, target)
	end
end
---@return boolean
function SpellSleepAOE___anon__2()
	return GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0.405 and  not (IsPlayerAlly(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetFilterUnit()))) and  not (IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE))
end
---@return nothing
function SpellSleepAOE___anon__1()
	local loc = GetSpellTargetLoc()
	local x = GetLocationX(loc)
	local y = GetLocationY(loc)
	local g = CreateGroup()
	local u
	GroupEnumUnitsInRange(g, x, y, I2R(SpellSleepAOE___getRange(GetUnitAbilityLevel(GetTriggerUnit(), SpellSleepAOE___SpellHero))), Condition(SpellSleepAOE___anon__2))
	while true do
		u = FirstOfGroup(g)
		if (u == nil) then
			if true then break end
		end
		SpellSleepAOE___DummyCastBuff(GetTriggerUnit(), u)
		GroupRemoveUnit(g, u)
	end
	RemoveLocation(loc)
	DestroyGroup(g)
	loc = nil
	g = nil
end
---@return nothing
function SpellSleepAOE___onInit()
	local t = CreateTrigger()
	local i
	SpellSleepAOE___DummyUnit = CreateUnit(SpellSleepAOE___DummyOwner, SpellSleepAOE___DummyID, 0, 0, 0)
	UnitAddAbility(SpellSleepAOE___DummyUnit, SpellSleepAOE___SpellCast)
	i = 0
	while true do
		if (i >= bj_MAX_PLAYER_SLOTS) then break end
		TriggerRegisterPlayerUnitEvent(t, Player(i), EVENT_PLAYER_UNIT_SPELL_EFFECT, nil)
		i = i + 1
	end
	TriggerAddAction(t, function()
        if SpellSleepAOE___SpellHero ~= GetSpellAbilityId() then return end
        SpellSleepAOE___anon__1()
    end)
	t = nil
end
-- library SpellSleepAOE ends
