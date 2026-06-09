

UHData = UHData or {}
-- *  XpLevelW2
---@param u unit
---@param addXp real
---@return nothing
function AddXp(u, addXp)
	local uh = GetHandleId(u)
	local d = UHData[uh]
	if d == nil then d = {lvl = 0, xp = 0} end
	local lvl = d.lvl
	local xp = d.xp
	local r
	
	if lvl < 10 then
		xp = xp + addXp
		while xp >= 100 + 25 * lvl do
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
		d.lvl = lvl
		d.xp = xp
		UHData[uh] = d
	end
end