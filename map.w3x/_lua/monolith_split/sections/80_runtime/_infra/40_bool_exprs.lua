-- *  gGlobal objects
-- ***************************************************************************
-- *  UnitForBoolexprs
--  scope initBoolExprs begins
---@return boolean
function UnitsWithReviveHeroSpellEach()
	gUnit = GetFilterUnit()
	if UnitAlive(gUnit) and BlzGetUnitBooleanField(gUnit, ConvertUnitBooleanField(FourCC('urev'))) then
		Counter = Counter + 1
		return true
	else
		return false
	end
end
---@return boolean
function f_OwnBuildingsInRange()
	gUnit = GetFilterUnit()
	if UnitAlive(gUnit) and GetOwningPlayer(gUnit) == CheckPlayer and IsUnitType(gUnit, UNIT_TYPE_STRUCTURE) then
		Counter = Counter + 1
		return true
	else
		return false
	end
end
---@return boolean
function f_OwnHeroes()
	gUnit = GetFilterUnit()
	if UnitAlive(gUnit) and IsUnitType(gUnit, UNIT_TYPE_HERO) then
		Counter = Counter + 1
		return true
	else
		return false
	end
end
---@return boolean
function f_OwnCapitalInRange()
	gUnit = GetFilterUnit()
	if IsUnitInGroup(gUnit, udg_StolicaGroups) and GetOwningPlayer(gUnit) == CheckPlayer and UnitAlive(gUnit) then
		return true
	else
		return false
	end
end
---@return nothing
function initBoolExprs___Init()
	UnitsWithReviveHeroSpell = Condition(UnitsWithReviveHeroSpellEach)
	b_OwnBuldingsInRange = Condition(f_OwnBuildingsInRange)
	b_OwnCapitalInRange = Condition(f_OwnCapitalInRange)
	b_OwnHeroes = Condition(f_OwnHeroes)
	
end
--  scope initBoolExprs ends
-- ***************************************************************************
