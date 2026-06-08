
-- ***************************************************************************
-- *  EnterGreen2
---@return boolean
function greencreature()
	return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0LR')) > 0
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
---@return nothing
function WakeGreenUp()
	GroupEnumUnitsInRect(gGroup, gg_rct_EmeraldDream, greencreature)
	ForGroup(gGroup, WakeGreenUpEach)
	GroupClear(gGroup)
end
---@return nothing
function SleepGreen()
	-- call BJDebugMsg("??????")
	GroupEnumUnitsInRect(gGroup, gg_rct_EmeraldDream, greencreature)
	ForGroup(gGroup, SleepGreenEach)
	GroupClear(gGroup)
end
---@return nothing
function checkGreenArea()
	local u
	GroupClear(gGroup)
	GroupEnumUnitsInRect(gGroup, gg_rct_EmeraldDream, alienToDream)
	while true do
		u = FirstOfGroup(gGroup)
		
		
		if u ~= nil and GetUnitAbilityLevel(u, FourCC('A1LR')) == 0 then
			-- call BJDebugMsg("??????????"+GetUnitName(u))
			u = nil
			
			WakeGreenUp()
			return 
		end
		
		if u == nil then break end
		
		GroupRemoveUnit(gGroup, u)
		u = nil
		
	end
	GroupClear(gGroup)
	-- call BJDebugMsg("????? ????")
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