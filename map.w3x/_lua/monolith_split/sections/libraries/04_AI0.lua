-- library AI0:
--  Общие функции
---@param x real
---@param y real
---@return boolean
function isUnitInNoWaterArea(x, y)
	return RectContainsCoords(gg_rct_NoWater1, x, y) or RectContainsCoords(gg_rct_NoWater2, x, y) or RectContainsCoords(gg_rct_NoWater3, x, y)
end
---@param u unit
---@return boolean
function isUnitWaterRelated(u)
	return IsUnitInGroup(u, udg_CityNearWater) or IsUnitInGroup(u, Navy) or IsUnitInGroup(u, Port)
end
--   --------------    Функции для фильтров     --------------
---@return boolean
function f_EnemyUnitP()
	local u = GetFilterUnit()
	local p = GetOwningPlayer(u)
	if UnitAlive(u) and IsPlayerEnemy(p, CheckPlayer) or WaygateIsActive(u) and  not (IsUnitInGroup(u, Navy) or GetUnitAbilityLevel(u, FourCC('A1MS')) > 0) then	--  A1MS Стр точка
		Counter = Counter + 1
		if IsUnitInGroup(u, udg_StolicaGroups) then
			EnemyCapital = u
		end
		u = nil
		return true
	else
		u = nil
		return false
	end
end
---@return boolean
function f_EnemyUnit()
	local u = GetFilterUnit()
	if UnitAlive(u) and IsPlayerEnemy(GetOwningPlayer(u), CheckPlayer) and  not (WaygateIsActive(u) or IsUnitInGroup(u, Navy) or GetUnitAbilityLevel(u, FourCC('A1MS')) > 0) then
		Counter = Counter + 1
		if IsUnitInGroup(u, udg_StolicaGroups) then
			EnemyCapital = u
		end
		u = nil
		return true
	end
	return false
end
--  Цель для флота
---@return boolean
function f_EnemyUnitN()
	local u = GetFilterUnit()
	local p = GetOwningPlayer(u)
	local x = GetUnitX(u)
	local y = GetUnitY(u)
	
	if UnitAlive(u) and IsPlayerEnemy(p, CheckPlayer) and isUnitWaterRelated(u) and  not (isUnitInNoWaterArea(x, y) or WaygateIsActive(u)) then
		u = nil
		Counter = Counter + 1
		return true
	else
		u = nil
		return false
	end
	
	
end
---@return boolean
function f_ToHeal()
	local u = GetFilterUnit()
	if IsPlayerAlly(GetOwningPlayer(u), CheckPlayer) and IsUnitIdType(GetUnitTypeId(u), UNIT_TYPE_MECHANICAL) ~= true then
		u = nil
		return true
	else
		u = nil
		return false
end
end
---@return boolean
function f_FixZ()
	return GetUnitCurrentOrder(GetFilterUnit()) == 851983
end
---@return boolean
function f_FixUnvul()
	return BlzIsUnitInvulnerable(GetFilterUnit())
	-- return GetUnitAbilityLevel(GetFilterUnit(),'Bvul')>0
end
---@param u unit
---@return boolean
function IsAiCombatRetaskable(u)
	if not UnitAlive(u) then
		return false
	end
	if IsUnitType(u, UNIT_TYPE_STRUCTURE) or IsUnitType(u, UNIT_TYPE_PEON) then
		return false
	end
	-- "Lazy" = not committed to an order. Only retask idle-ish units (orders
	-- 851972 / 851976 / 0). Units already attacking/moving are left alone so the
	-- army doesn't get re-targeted every tick (was the re-tasking churn bug).
	local o = GetUnitCurrentOrder(u)
	return o == 851972 or o == 851976 or o == 0
end
---@param pi integer
---@param key string
---@param limit integer
---@param message string
---@return nothing
function AiProbeLogLimited(pi, key, limit, message)
	-- Army/diagnostic AI logging silenced (debug complete). Restore the body below
	-- (StringHash/LoadInteger gate + ProbeLogWrite) to re-enable for future debugging.
end
---@return boolean
function f_Lazy()
	gUnit = GetFilterUnit()
	if IsAiCombatRetaskable(gUnit) and IsUnitInGroup(gUnit, udg_Ai_army[GetPlayerId(GetOwningPlayer(gUnit))]) then
		LazyCount = LazyCount + 1
		return true
	else
		return false
	end
end
---@return boolean
function f_LazyF()
	gUnit = GetFilterUnit()
	return IsAiCombatRetaskable(gUnit) and IsUnitInGroup(gUnit, udg_Ai_army[GetPlayerId(CheckPlayer)])
end
---@return boolean
function f_LazyN()
	gUnit = GetFilterUnit()
	local o = GetUnitCurrentOrder(gUnit)
	if UnitAlive(gUnit) and IsUnitInGroup(gUnit, udg_Ai_navy[GetPlayerId(CheckPlayer)]) and (o == 851972 or o == 851976 or o == 0) then
		LazyCount = LazyCount + 1
		return true
	else
		return false
	end
end
---@return boolean
function f_LazyW()
	gUnit = GetFilterUnit()
	gInt = GetUnitCurrentOrder(gUnit)
	return GetUnitState(gUnit, UNIT_STATE_LIFE) > 0.405 and IsUnitInGroup(gUnit, udg_Ai_builders[GetPlayerId(GetOwningPlayer(gUnit))]) and (gInt == 851972 or gInt == 851976 or gInt == 0)
end
---@return boolean
function f_LazyT()
	gUnit = GetFilterUnit()
	gInt = GetUnitCurrentOrder(gUnit)
	return GetUnitState(gUnit, UNIT_STATE_LIFE) > 0.405 and IsUnitInGroup(gUnit, udg_Ai_buildersT[GetPlayerId(GetOwningPlayer(gUnit))]) and (gInt == 851972 or gInt == 851976 or gInt == 0)
end
---@return boolean
function f_PortB()
	return IsUnitInGroup(GetFilterUnit(), AiUnitsToPort[CheckId])
end
---@return boolean
function f_Worker()
	gUnit = GetFilterUnit()
	return GetUnitState(gUnit, UNIT_STATE_LIFE) > 0.405 and IsUnitInGroup(gUnit, udg_Ai_buildersT[GetPlayerId(GetOwningPlayer(gUnit))])
end
---@return boolean
function f_Harwest()
	gUnit = GetFilterUnit()
	if GetUnitState(gUnit, UNIT_STATE_LIFE) > 0.405 and IsUnitInGroup(gUnit, udg_Ai_harvest[GetPlayerId(GetOwningPlayer(gUnit))]) then
		return true
	else
		return false
	end
end
---@return boolean
function f_InAiArmy()
	gUnit = GetFilterUnit()
	return GetUnitState(gUnit, UNIT_STATE_LIFE) > 0.405 and IsUnitInGroup(gUnit, udg_Ai_army[GetPlayerId(GetOwningPlayer(gUnit))])
end
---@return boolean
function f_InAiNavy()
	gUnit = GetFilterUnit()
	return GetUnitState(gUnit, UNIT_STATE_LIFE) > 0.405 and IsUnitInGroup(gUnit, udg_Ai_navy[GetPlayerId(GetOwningPlayer(gUnit))])
end
--  Здания в которых надо делать найм - без работы, в группе, определенного типа
---@return boolean
function f_OnlyNeaded()
	gUnit = GetFilterUnit()
	
	if GetUnitState(gUnit, UNIT_STATE_LIFE) <= 0.405 then
		return false
	end
	
	gPi = GetPlayerId(GetOwningPlayer(gUnit))
	--  Проверка на принадлежность к группе сразу
	if  not IsUnitInGroup(gUnit, udg_Ai_buildings[gPi]) then
		return false
	end
	
	gInt = GetUnitTypeId(gUnit)
	--  Алый орден
	if AiRace[gPi] == "Scarlet" then
		if gInt == FourCC('h05Z') or gInt == FourCC('h05X') or gInt == FourCC('h011') or gInt == FourCC('h064') or gInt == FourCC('h05U') or gInt == FourCC('h068') or gInt == FourCC('h061') or gInt == FourCC('h05W') then
			Counter = Counter + 1
			return true
		end
		--  Эльфы крови
	elseif AiRace[gPi] == "BloodElves" then
		if gInt == FourCC('h04C') or gInt == FourCC('h04B') or gInt == FourCC('h04K') or gInt == FourCC('h04D') or gInt == FourCC('h05J') or gInt == FourCC('h04G') or gInt == FourCC('h04E') or gInt == FourCC('h011') then
			Counter = Counter + 1
			return true
		end
		--  Гоблины
	elseif AiRace[gPi] == "Goblins" then
		if gInt == FourCC('h0D7') or gInt == FourCC('o016') or gInt == FourCC('h070') or gInt == FourCC('h079') or gInt == FourCC('h074') or gInt == FourCC('h073') or gInt == FourCC('h076') or gInt == FourCC('h075') then
			Counter = Counter + 1
			return true
		end
		--  Наги
	elseif AiRace[gPi] == "Naga" then
		if gInt == FourCC('n055') or gInt == FourCC('h0JW') or gInt == FourCC('n04L') or gInt == FourCC('nntt') or gInt == FourCC('nnsg') or gInt == FourCC('nnsa') or gInt == FourCC('nnad') then
			Counter = Counter + 1
			return true
		end
		--  Орда
	elseif AiRace[gPi] == "Horde" then
		if gInt == FourCC('ogre') or gInt == FourCC('orbr') or gInt == FourCC('obar') or gInt == FourCC('oalt') or gInt == FourCC('obea') or gInt == FourCC('osld') or gInt == FourCC('otto') then
			Counter = Counter + 1
			return true
		end
		--  Jungle Trolls
	elseif AiRace[gPi] == "JungleTrolls" then
		if gInt == FourCC('h0N5') or gInt == FourCC('h0N2') or gInt == FourCC('h0MY') or gInt == FourCC('h0N3') or gInt == FourCC('h0N0') or gInt == FourCC('h0MX') or gInt == FourCC('h0MW') or gInt == FourCC('h0D3') or gInt == FourCC('h0N1') or gInt == FourCC('h0N6') then
			Counter = Counter + 1
			return true
		end
	--  ForestTrolls
	elseif AiRace[gPi] == "ForestTrolls" then
		if gInt == FourCC('h0MT') or gInt == FourCC('h0N8') or gInt == FourCC('h0N9') or gInt == FourCC('h0MV') or gInt == FourCC('h0MS') or gInt == FourCC('h0N7') or gInt == FourCC('h0MU') or gInt == FourCC('h0MZ') or gInt == FourCC('h0MR') or gInt == FourCC('h0N4') then
			Counter = Counter + 1
			return true
		end
	--  HordeW2
	elseif AiRace[gPi] == "HordeW2" then
		if gInt == FourCC('w20q') or gInt == FourCC('w20w') or gInt == FourCC('w20e') or gInt == FourCC('w20y') or gInt == FourCC('w20r') or gInt == FourCC('w214') or gInt == FourCC('w20a') or gInt == FourCC('w20i') or gInt == FourCC('w20t') or gInt == FourCC('w210') or gInt == FourCC('w212') or gInt == FourCC('w20u') then
			Counter = Counter + 1
			return true
		end
	--  Nerubs
	elseif AiRace[gPi] == "Nerubs" then
		if gInt == FourCC('h0CO') or gInt == FourCC('h0CP') or gInt == FourCC('h0CQ') or gInt == FourCC('h0GH') or gInt == FourCC('h0CR') or gInt == FourCC('h0CS') or gInt == FourCC('h0CU') or gInt == FourCC('h0CT') or gInt == FourCC('h0CV') or gInt == FourCC('u01A') or gInt == FourCC('u019') then
			Counter = Counter + 1
			return true
		end
	--  Forsaken
	elseif AiRace[gPi] == "Forsaken" then
		if gInt == FourCC('h0JP') or gInt == FourCC('h0JQ') or gInt == FourCC('h0JL') or gInt == FourCC('h0JD') or gInt == FourCC('h0JJ') or gInt == FourCC('h0JO') or gInt == FourCC('h0JR') or gInt == FourCC('h0JM') or gInt == FourCC('h0JI') or gInt == FourCC('h0JK') then
			Counter = Counter + 1
			return true
		end
	end
	return false
end
---@return boolean
function f_NavalBases()
	gUnit = GetFilterUnit()
	gId = GetUnitTypeId(gUnit)
	
	if GetUnitState(gUnit, UNIT_STATE_LIFE) > 0.405 and (gId == FourCC('h011') or gId == FourCC('h0D7') or gId == FourCC('n04L') or gId == FourCC('h0HO')) then
		Counter = Counter + 1
		return true
	else
		return false
	end
	
end
---@return boolean
function f_Hero()
	return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end
---@return boolean
function f_HeroD()
	return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO) and GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) <= 0
end
---@return boolean
function f_LiveHero()
	return GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0.6 and IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end
-- Расовые штуки
-- Алый орден
---@return boolean
function f_Altars()
	gUnit = GetFilterUnit()
	gId = GetUnitTypeId(gUnit)
	return UnitAlive(gUnit) and gId == FourCC('h05X') or gId == FourCC('h05J') or gId == FourCC('o016') or gId == FourCC('nnad') or gId == FourCC('oalt')
end
---@return nothing
function MakeHash()
	
	local i = 0
	-- call DisplayTimedTextFromPlayer(Player(0),0,0,4, "Залил хеш")
	while true do
		if i == 24 then break end
		SaveInteger(AiData, i, FourCC('h05W'), 0)
		SaveInteger(AiData, i, FourCC('h0ZX'), 0)
		SaveInteger(AiData, i, FourCC('h064'), 0)
		SaveInteger(AiData, i, FourCC('h05Z'), 0)
		SaveInteger(AiData, i, FourCC('h05W'), 0)
		SaveInteger(AiData, i, FourCC('h05Y'), 0)
		SaveInteger(AiData, i, FourCC('h05V'), 0)
		SaveInteger(AiData, i, FourCC('h061'), 0)
		SaveInteger(AiData, i, FourCC('h068'), 0)
		SaveInteger(AiData, i, FourCC('h05W'), 0)
		SaveInteger(AiData, i, FourCC('h062'), 0)
		SaveInteger(AiData, i, FourCC('h060'), 0)
		i = i + 1
	end
	-- call DisplayTimedTextFromPlayer(Player(0),0,0,4, "Залил хеш 2")
end
--  
---@return nothing
function SetPortalGroup()
	
	local i = 0
	
	while true do
		if i >= 24 then break end
		AiUnitsToPort[i] = CreateGroup()
		AiCapitalGuard[i] = CreateGroup()
		AiCapitalBuildigs[i] = CreateGroup()
		Grades[i] = 0
		i = i + 1
	end
end
---@return nothing
function AiLimitsSet()
	gInt = CountPlayersInForceBJ(udg_Bots)
	AiLimit = IMaxBJ(70, 200 - gInt * 5)
	
	AiMass = IMaxBJ(8 - gInt, 4)
	AiRepeat = 2 + IMinBJ(R2I(gInt / 2), 8)
	ProbeLogWrite("[AI] AiLimitsSet Bots=" .. tostring(gInt) .. " AiLimit=" .. tostring(AiLimit) .. " AiMass=" .. tostring(AiMass) .. " AiRepeat=" .. tostring(AiRepeat))
end
---@return nothing
function SetBools()
	-- call DisplayTimedTextFromPlayer(Player(1),0,0, 4,"Инициалзиация буллов")
	
	Altars = Condition(f_Altars)
	ToHeal = Condition(f_ToHeal)
	B_LazyW = Condition(f_LazyW)
	B_Worker = Condition(f_Worker)
	B_LazyT = Condition(f_LazyT)
	B_Lazy = Condition(f_Lazy)
	B_LazyN = Condition(f_LazyN)
	B_LazyF = Condition(f_LazyF)
	Harwest = Condition(f_Harwest)
	B_OnlyNeaded = Condition(f_OnlyNeaded)
	B_NavalBases = Condition(f_NavalBases)
	B_Hero = Condition(f_Hero)
	B_HeroD = Condition(f_HeroD)
	B_InAiArmy = Condition(f_InAiArmy)
	B_InAiNavy = Condition(f_InAiNavy)
	udg_B_EnemyUnitN = Condition(f_EnemyUnitN)
	udg_B_EnemyUnit = Condition(f_EnemyUnit)
	udg_B_EnemyUnitP = Condition(f_EnemyUnitP)
	PortB = Condition(f_PortB)
	FixZ = Condition(f_FixZ)
	LiveHero = Condition(f_LiveHero)
	
	B_FixUnvul = Condition(f_FixUnvul)
	
	-- call AiPoitsSet()
	SetPortalGroup()
	MakeHash()
end
-- library AI0 ends
