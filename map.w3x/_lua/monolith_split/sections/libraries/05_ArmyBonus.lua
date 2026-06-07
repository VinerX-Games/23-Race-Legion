-- library ArmyBonus:
---@param p player
---@return nothing
function CreateArmyBonusUnit(p)
	gPi = GetPlayerId(p)
	if ArmyExpBonus[gPi] == nil then
		ArmyExpBonus[gPi] = CreateUnit(p, FourCC('arbo'), 0, 0, 0.0)
		UnitAddAbility(ArmyExpBonus[gPi], FourCC('arb1'))
		UnitAddAbility(ArmyExpBonus[gPi], FourCC('arb0'))
	end
	
end
-- library ArmyBonus ends
