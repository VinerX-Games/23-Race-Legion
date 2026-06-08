
-- ***************************************************************************
-- *  XpLevelW2
---@param u unit
---@param addXp real
---@return nothing
function AddXp(u, addXp)
	local uh = GetHandleId(u)
	local lvl = LoadInteger(Hash, uh, 0)
	local xp = LoadReal(Hash, uh, 1)
	local r
	
	
	if lvl < 10 then
		xp = xp + addXp
		
		while true do
			
			if xp < 100 + 25 * lvl then break end
			
			
			r = GetUnitLifePercent(u)
			BlzSetUnitMaxHP(u, MathRound(BlzGetUnitMaxHP(u) * 1.035))
			SetUnitLifePercentBJ(u, r)
			
			r = GetUnitManaPercent(u)
			BlzSetUnitMaxMana(u, MathRound(BlzGetUnitMaxMana(u) * 1.035))
			SetUnitManaPercentBJ(u, r)
			BlzSetUnitBaseDamage(u, MathRound(BlzGetUnitBaseDamage(u, 0) * 1.04), 0)
			BlzSetUnitBaseDamage(u, MathRound(BlzGetUnitBaseDamage(u, 1) * 1.04), 1)
			
			
			
			
			
			xp = xp - (100 + 25 * lvl)
			lvl = lvl + 1
			
			SetUnitAbilityLevel(u, FourCC('w2a0'), lvl)
			
		end
		
		
		
		SaveInteger(Hash, uh, 0, lvl)	-- StringHash("lvl"),lvl)
		SaveReal(Hash, uh, 1, xp)	-- StringHash("xp"),xp)
	end
	
end