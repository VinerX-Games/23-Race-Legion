
-- ***************************************************************************
-- *  EnterGreen2
---@return boolean
function greencreature()
	return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0LR')) > 0
end
local greencreatureFilter
local function GreenCreatureFilter()
	if greencreatureFilter == nil then
		greencreatureFilter = Condition(greencreature)
	end
	return greencreatureFilter
end
---@return boolean
function alienToDream()
	return UnitAlive(GetFilterUnit()) and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0LR')) == 0 and  not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) and GetUnitTypeId(GetFilterUnit()) ~= Dummy and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Awrp')) == 0
end
---@return nothing
function WakeGreenUpEach()
	PauseUnit(GetEnumUnit(), false)
	-- call UnitWakeUp(GetEnumUnit())
end
---@return nothing
function SleepGreenEach()
	PauseUnit(GetEnumUnit(), true)
	-- call UnitWakeUp(GetEnumUnit())
end
-- Своя группа: WakeGreenUp вызывается из ForGroup(gGroup, ...) телепорта порталов
-- (TeleportUnitsEach -> EnterGreen) и из checkGreenArea, перебирающей gGroup.
-- Enum/GroupClear той же gGroup внутри перебора -> краш ACCESS_VIOLATION.
local greenGroup
local function GreenGroup()
	if greenGroup == nil then
		greenGroup = CreateGroup()
	end
	return greenGroup
end
---@return nothing
function WakeGreenUp()
	local g = GreenGroup()
	GroupEnumUnitsInRect(g, gg_rct_EmeraldDream, GreenCreatureFilter())
	ForGroup(g, WakeGreenUpEach)
	GroupClear(g)
end
---@return nothing
function SleepGreen()
	-- call BJDebugMsg("??????")
	local g = GreenGroup()
	GroupEnumUnitsInRect(g, gg_rct_EmeraldDream, GreenCreatureFilter())
	ForGroup(g, SleepGreenEach)
	GroupClear(g)
end
---@return nothing
function checkGreenArea()
	local u
	GroupClear(gGroup)
	GroupEnumUnitsInRect(gGroup, gg_rct_EmeraldDream, nil)
	while true do
		u = FirstOfGroup(gGroup)
		if u ~= nil then
			-- Inline alienToDream check: alive, non-structure, non-dummy, non-WRP
			if GetUnitAbilityLevel(u, FourCC('A1LR')) == 0
				and UnitAlive(u)
				and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
				and GetUnitTypeId(u) ~= Dummy
				and GetUnitAbilityLevel(u, FourCC('Awrp')) == 0 then
					u = nil
					WakeGreenUp()
					return 
				end
		end
		if u == nil then break end
		GroupRemoveUnit(gGroup, u)
		u = nil
	end
	GroupClear(gGroup)
	SleepGreen()
	u = nil
end
---@param u unit
---@return nothing
function EnterGreen(u)
	if GetUnitAbilityLevel(u, FourCC('A1LR')) > 0 then
		
	else
		WakeGreenUp()
	end
	
end
