

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
	if subrace == "dark" then
		return 12
	elseif subrace == "dragonmaw" then
		return 8
	end
	return 10
end

---@param p player
---@return nothing
function HordeW2ApplyDragonPreset(p)
	local subrace = HordeW2GetSubrace(p)
	SetPlayerTechResearched(p, FourCC('xdR1'), subrace == "dark" and 1 or 0)
	SetPlayerTechResearched(p, FourCC('xdR2'), subrace == "dragonmaw" and 1 or 0)
	for _, id in ipairs({ 'w291', 'w292', 'w293' }) do SetPlayerTechResearched(p, FourCC(id), 0) end
	for _, id in ipairs({ 'w294', 'w297', 'w295' }) do
		SetPlayerAbilityAvailable(p, FourCC(id), subrace == "base")
	end
	if subrace == "dark" then
		SetPlayerTechResearchedSwap(FourCC('w292'), 1, p)
		SetPlayerAbilityAvailableBJ(true, FourCC('w290'), p)
	elseif subrace == "dragonmaw" then
		SetPlayerTechResearchedSwap(FourCC('w293'), 1, p)
	end
end

---@param p player
---@return nothing
function HordeW2ApplySubraceRoster(p)
	local subrace = HordeW2GetSubrace(p)

	local common = { 'w201', 'w202', 'w203', 'w205', 'w206', 'w209', 'w211', 'w213' }
	local unique = { 'xd01', 'xd02', 'xd03', 'xd04', 'xd05', 'xd06', 'xd07', 'xd08', 'xd09', 'xd0A' }
	for _, id in ipairs(common) do SetPlayerTechMaxAllowed(p, FourCC(id), -1) end
	for _, id in ipairs(unique) do SetPlayerTechMaxAllowed(p, FourCC(id), 0) end
	for _, id in ipairs({ 'W200', 'W201', 'W202' }) do SetPlayerTechMaxAllowed(p, FourCC(id), 1) end
	SetPlayerTechMaxAllowed(p, FourCC('W203'), 0)
	SetPlayerTechMaxAllowed(p, FourCC('W204'), 0)
	SetPlayerTechMaxAllowed(p, FourCC('w212'), subrace == "dark" and -1 or 0)
	SetPlayerTechMaxAllowed(p, FourCC('w213'), 0)
	local disabled, enabled = {}, {}
	if subrace == "dark" then
		disabled = { 'w201', 'w202', 'w206', 'w211', 'w213' }
		enabled = { 'xd01', 'xd02', 'xd03', 'xd07', 'xd08' }
		SetPlayerTechMaxAllowed(p, FourCC('W202'), 0)
		SetPlayerTechMaxAllowed(p, FourCC('W203'), 1)
	elseif subrace == "dragonmaw" then
		disabled = { 'w201', 'w202', 'w203', 'w205', 'w209', 'w211', 'w213' }
		enabled = { 'xd04', 'xd05', 'xd06', 'xd09', 'xd0A' }
		SetPlayerTechMaxAllowed(p, FourCC('W202'), 0)
		SetPlayerTechMaxAllowed(p, FourCC('W204'), 1)
	end
	for _, id in ipairs(disabled) do SetPlayerTechMaxAllowed(p, FourCC(id), 0) end
	for _, id in ipairs(enabled) do SetPlayerTechMaxAllowed(p, FourCC(id), -1) end
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
			SetUnitAbilityLevel(u, FourCC('w2a0'), lvl + 1)
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
