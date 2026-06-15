

UHData = UHData or {}
HordeW2SubraceByPlayer = HordeW2SubraceByPlayer or {}
-- Set true when a bot's subrace was explicitly chosen (via -ai token); blocks the
-- random bot pick so a forced "base"/"dark"/"dragonmaw" is respected.
HordeW2SubraceForced = HordeW2SubraceForced or {}
-- When true, HordeW2 bots without a forced subrace roll a random branch so the AI
-- actually exercises the dark/dragonmaw rosters in normal games.
if HordeW2BotRandomSubrace == nil then HordeW2BotRandomSubrace = true end

local function HordeW2ResolvePi(pOrPi)
	if type(pOrPi) == "number" then
		return pOrPi
	end
	if pOrPi == nil then
		return nil
	end
	return GetPlayerId(pOrPi)
end

---@param key string|nil
---@return string
function HordeW2NormalizeSubrace(key)
	if key == nil or key == "" then
		return "base"
	end
	key = string.lower(key)
	if key == "dark" or key == "darkhorde" or key == "temnayaorda" then
		return "dark"
	end
	if key == "dragonmaw" or key == "dragonmawclan" or key == "dragon" then
		return "dragonmaw"
	end
	return "base"
end

---@param pOrPi player|integer
---@param key string|nil
---@return string
function HordeW2SetSubrace(pOrPi, key)
	local pi = HordeW2ResolvePi(pOrPi)
	if pi == nil then
		return "base"
	end
	local normalized = HordeW2NormalizeSubrace(key)
	HordeW2SubraceByPlayer[pi] = normalized
	return normalized
end

-- Mark a player's subrace as explicitly forced (or clear the flag).
---@param pOrPi player|integer
---@param forced boolean
---@return nothing
function HordeW2SetSubraceForced(pOrPi, forced)
	local pi = HordeW2ResolvePi(pOrPi)
	if pi == nil then
		return
	end
	HordeW2SubraceForced[pi] = forced and true or nil
end

-- For a bot: unless its subrace was forced via token, roll a random branch.
-- Returns the resulting subrace key.
---@param pOrPi player|integer
---@return string
function HordeW2PickBotSubrace(pOrPi)
	local pi = HordeW2ResolvePi(pOrPi)
	if pi == nil then
		return "base"
	end
	if HordeW2SubraceForced[pi] or not HordeW2BotRandomSubrace then
		return HordeW2GetSubrace(pi)
	end
	local roll = GetRandomInt(0, 2)
	local key = "base"
	if roll == 1 then
		key = "dark"
	elseif roll == 2 then
		key = "dragonmaw"
	end
	HordeW2SubraceByPlayer[pi] = key
	return key
end

---@param pOrPi player|integer
---@return string
function HordeW2GetSubrace(pOrPi)
	local pi = HordeW2ResolvePi(pOrPi)
	if pi == nil then
		return "base"
	end
	return HordeW2SubraceByPlayer[pi] or "base"
end

---@param pOrPi player|integer
---@return string
function HordeW2GetSubraceLabel(pOrPi)
	local subrace = HordeW2GetSubrace(pOrPi)
	if subrace == "dark" then
		return "Dark Horde"
	elseif subrace == "dragonmaw" then
		return "Dragonmaw"
	end
	return "Base"
end

---@param pOrPi player|integer
---@return real
function HordeW2GetXpFactor(pOrPi)
	local subrace = HordeW2GetSubrace(pOrPi)
	if subrace == "dark" then
		return 0.85
	elseif subrace == "dragonmaw" then
		return 1.15
	end
	return 1.0
end

---@param pOrPi player|integer
---@return integer
function HordeW2GetVeterancyCap(pOrPi)
	local subrace = HordeW2GetSubrace(pOrPi)
	if subrace == "dragonmaw" then
		return 8
	end
	return 10
end

---@param p player
---@return nothing
function HordeW2ApplyDragonPreset(p)
	local subrace = HordeW2GetSubrace(p)
	if subrace == "dark" then
		SetPlayerTechResearchedSwap(FourCC('w292'), 1, p)
		SetPlayerAbilityAvailableBJ(true, FourCC('w290'), p)
		SetPlayerAbilityAvailableBJ(false, FourCC('w294'), p)
		SetPlayerAbilityAvailableBJ(false, FourCC('w297'), p)
		SetPlayerAbilityAvailableBJ(false, FourCC('w295'), p)
	elseif subrace == "dragonmaw" then
		SetPlayerTechResearchedSwap(FourCC('w293'), 1, p)
		SetPlayerAbilityAvailableBJ(false, FourCC('w294'), p)
		SetPlayerAbilityAvailableBJ(false, FourCC('w297'), p)
		SetPlayerAbilityAvailableBJ(false, FourCC('w295'), p)
	end
end

---@param p player
---@return nothing
function HordeW2ApplySubraceRoster(p)
	local subrace = HordeW2GetSubrace(p)

	SetPlayerTechMaxAllowedSwap(FourCC('xd01'), 0, p)
	SetPlayerTechMaxAllowedSwap(FourCC('xd02'), 0, p)
	SetPlayerTechMaxAllowedSwap(FourCC('xd03'), 0, p)
	SetPlayerTechMaxAllowedSwap(FourCC('xd04'), 0, p)
	SetPlayerTechMaxAllowedSwap(FourCC('xd05'), 0, p)
	SetPlayerTechMaxAllowedSwap(FourCC('xd06'), 0, p)
	SetPlayerTechMaxAllowedSwap(FourCC('xd07'), 0, p)

	SetPlayerTechMaxAllowedSwap(FourCC('w201'), -1, p)
	SetPlayerTechMaxAllowedSwap(FourCC('w202'), -1, p)
	SetPlayerTechMaxAllowedSwap(FourCC('w203'), -1, p)
	SetPlayerTechMaxAllowedSwap(FourCC('w205'), -1, p)
	SetPlayerTechMaxAllowedSwap(FourCC('w206'), -1, p)
	SetPlayerTechMaxAllowedSwap(FourCC('w213'), -1, p)

	-- Heroes (uppercase rawcodes). All branches keep W200 + W201 (Cho'gall).
	-- The 3rd slot: W202 Troll Leader on base/dragonmaw, W203 Maim on Dark Horde
	-- (full unit swap, same altar card slot — never both visible).
	SetPlayerTechMaxAllowedSwap(FourCC('W201'), -1, p)
	SetPlayerTechMaxAllowedSwap(FourCC('W202'), -1, p)
	SetPlayerTechMaxAllowedSwap(FourCC('W203'), 0, p)

	if subrace == "dark" then
		-- Dark Horde replaces the Troll Leader with Maim Blackhand.
		SetPlayerTechMaxAllowedSwap(FourCC('W202'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('W203'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('w202'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('w205'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('w206'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('w213'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('xd01'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('xd02'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('xd03'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('xd07'), -1, p)
	elseif subrace == "dragonmaw" then
		SetPlayerTechMaxAllowedSwap(FourCC('w201'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('w203'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('w205'), 0, p)
		SetPlayerTechMaxAllowedSwap(FourCC('xd04'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('xd05'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('xd06'), -1, p)
	end
end

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
	local maxLvl = HordeW2GetVeterancyCap(GetOwningPlayer(u))
	local r
	
	if lvl < maxLvl then
		xp = xp + addXp * HordeW2GetXpFactor(GetOwningPlayer(u))
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
			if lvl >= maxLvl then
				xp = 0
				break
			end
		end
		d.lvl = lvl
		d.xp = xp
		UHData[uh] = d
	end
end
