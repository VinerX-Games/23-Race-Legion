-- library LibDifferentAiStuff:
-- ***************************************************************************
-- *  AiData
--  Для работы надо номер игрока, ид юнита
---@param pi integer
---@param id integer
---@return integer
g_AiCountCache = {}

function getAiCount(pi, id)
	local t = g_AiCountCache[pi]
	if t ~= nil then
		local v = t[id]
		if v ~= nil then return v end
	end
	return 0
end
--  Для работы надо номер игрока, ид юнита
---@param pi integer
---@param id integer
---@return boolean
function aiHasUnit(pi, id)
	local t = g_AiCountCache[pi]
	if t ~= nil then return (t[id] or 0) > 0 end
	return false
end
--  Для работы надо номер игрока, ид юнита
---@param pi integer
---@param id integer
---@return nothing
function NumberAdd(pi, id)
	local t = g_AiCountCache[pi]
	if t == nil then t = {}; g_AiCountCache[pi] = t end
	local c = (t[id] or 0) + 1
	t[id] = c
	AiData[pi][id] = c
end
function NumberSet(pi, id, amount)
	local t = g_AiCountCache[pi]
	if t == nil then t = {}; g_AiCountCache[pi] = t end
	t[id] = amount
	AiData[pi][id] = amount
end
---@param pi integer
---@param id integer
---@return nothing
function NumberRem(pi, id)
	local t = g_AiCountCache[pi]
	if t == nil then t = {}; g_AiCountCache[pi] = t end
	local c = (t[id] or 0) - 1
	t[id] = c
	AiData[pi][id] = c
end
---@param pi integer
---@param id integer
---@return nothing
function NumberReset(pi, id)
	local t = g_AiCountCache[pi]
	if t ~= nil then t[id] = nil end
	AiData[pi][id] = 0
end
---@param pi integer
---@return nothing
function NumberResetAll(pi)
	g_AiCountCache[pi] = nil
	AiData[pi] = nil
end
-- ***************************************************************************
-- *  HasEnemyNear
---@param u unit
---@return boolean
function HasEnemyNear(u)
	
	if u ~= nil then
		CheckPlayer = GetOwningPlayer(u)
		GroupEnumUnitsInRange(gGroup, GetUnitX(u), GetUnitY(u), 11000, udg_B_EnemyUnit)
		if FirstOfGroup(gGroup) ~= nil then
			return true
		end
	end
	
	return false
end
-- ***************************************************************************
-- *  PortToAction
---@param dest unit
---@param pi integer
---@param x real
---@param y real
---@return unit
function ChoseRandomSpot(dest, pi, x, y)
	Counter = 0
	CheckPlayer = Player(pi)
	GroupEnumUnitsInRange(gGroup, x, y, 3200, b_OwnBuldingsInRange)
	return BlzGroupUnitAt(gGroup, GetRandomInt(0, Counter - 1))
end
--  Создает мага тп и делат теп по позиции выбранного юнита
---@param dest unit
---@param u2 unit
---@param pi integer
---@return nothing
function MakeTPMage(dest, u2, pi)
	gX = GetUnitX(dest)
	gY = GetUnitY(dest)
	if (AiData[pi][gMageTP] or 0) < 10 and GetUnitAbilityLevel(dest, FourCC('A1RD')) == 0 then
		gUnit3 = ChoseRandomSpot(dest, pi, gX, gY)
		if gUnit3 ~= nil then
			gX = GetUnitX(gUnit3)
			gY = GetUnitY(gUnit3)
		else
			gUnit = CreateUnit(Player(pi), FourCC('h07A'), gX, gY, 0)
		end
		RemoveEffectTimed(AddSpecialEffect("Abilities\\Spells\\Human\\MassTeleport\\MassTeleportCaster.mdl", gX, gY), 3)
		IssuePointOrder(gUnit, "darksummoning", GetUnitX(u2), GetUnitY(u2))
		GroupAddUnit(udg_Ai_army[pi], gUnit)
		GroupAddUnit(AiUnitsToPort[pi], gUnit)
		NumberAdd(pi, gMageTP)
		AddAbilityTimed(dest, FourCC('A1RD'), 8)
	end
	
end
--  Выбирает юнита которого можно тепнуть к выбранному юниту
---@param u unit
---@return nothing
function PortTo(u)
	
	gPlayer = GetOwningPlayer(u)
	gPi = GetPlayerId(gPlayer)
	
	LazyCount = 0
	GroupEnumUnitsOfPlayer(gGroup, gPlayer, B_Lazy)
	gUnit2 = BlzGroupUnitAt(gGroup, GetRandomInt(0, LazyCount - 1))
	
	--  Точка
	if IsUnitInGroup(u, udg_ZahvatBuildings) then
		UnitAddAbility(u, FourCC('A0Y4'))
		IssuePointOrder(u, "darksummoning", GetUnitX(gUnit2), GetUnitY(gUnit2))
		
		--  Дополнительно маг тп
		if Random(1, 4) then
			MakeTPMage(u, gUnit2, gPi)
		end
		--  Маг тп 
	elseif GetUnitTypeId(u) == gMageTP then
		IssuePointOrder(u, "darksummoning", GetUnitX(gUnit2), GetUnitY(gUnit2))
	else
		
		MakeTPMage(u, gUnit2, gPi)
	end
	
end
--  Выбирает юнита которого можно тепнуть к выбранному юниту
---@param u unit
---@return nothing
function PortToFast(u)
	
	gPlayer = GetOwningPlayer(u)
	gPi = GetPlayerId(gPlayer)
	
	LazyCount = 0
	GroupEnumUnitsOfPlayer(gGroup, gPlayer, B_InAiArmy)
	gUnit2 = BlzGroupUnitAt(gGroup, GetRandomInt(0, LazyCount - 1))
	
	--  Точка
	if IsUnitInGroup(gAttacked, udg_ZahvatBuildings) then
		UnitAddAbility(u, FourCC('A0Y4'))
		IssuePointOrder(u, "darksummoning", GetUnitX(gUnit2), GetUnitY(gUnit2))
		
		--  Дополнительно маг тп
		if Random(1, 4) then
			MakeTPMage(u, gUnit2, gPi)
		end
		--  Здание
	else
		MakeTPMage(u, gUnit2, gPi)
	end
	
end
-- ***************************************************************************
-- *  WakPortToAction
--  Выбирает юнита которого можно тепнуть к выбранному юниту
---@param u unit
---@return nothing
function WalkPortTo(u)
	PortTo(u)
end
-- ***************************************************************************
-- *  TryPort
--  Выбирает юнитов к которым можно тепнуться и делает к ним теп
---@return nothing
function TryPort()
	local pi = TryPort_pi
	local u
	
	u = GroupPickRandomUnit2(AiUnitsToPort[pi])
	if u ~= nil then
		CheckPlayer = Player(pi)
		if HasEnemyNear(u) ~= nil then
			PortTo(u)
		end
	end
	
	u = nil
	
end
-- ***************************************************************************
-- *  RequestPort
--  Выбирает юнитов к которым можно тепнуться и делает к ним теп
---@param u unit
---@return nothing
function RequestPort(u)
	gPlayer = GetOwningPlayer(u)
	gPi = GetPlayerId(gPlayer)
	gInt = 0
	while true do
		if gInt > 3 then break end
		
		u = GroupPickRandomUnit2(AiUnitsToPort[gPi])
		if u ~= nil then
			CheckPlayer = gPlayer
			if HasEnemyNear(u) ~= nil then
				PortTo(u)
			end
			if true then break end
		end
		gInt = gInt + 1
		
	end
	
end
-- ***************************************************************************
-- *  WarRace
---@param grades integer
---@param p player
---@return nothing
function warRace(grades, p)
	SetPlayerTechResearched(p, FourCC('R03Q'), MathRound(grades / 75) - 1)
end
-- ***************************************************************************
-- *  BuildT
---@return nothing
function TType()
	if GetUnitTypeId(GetEnumUnit()) == udg_LocalInteger5 then
		GroupAddUnit(udg_LocalOtrad, GetEnumUnit())
	end
end
---@param p player
---@param before integer
---@param after integer
---@return nothing
function BuildT(p, before, after)
	local u = nil
	
	GroupClear(udg_LocalOtrad)
	GroupEnumUnitsOfPlayer(gGroup, p, nil)
	udg_LocalInteger5 = before
	ForGroup(gGroup, TType)
	
	
	gGroup = udg_LocalOtrad
	u = GroupPickRandomUnit2(gGroup)
	if u ~= nil then
		IssueImmediateOrderById(u, after)
		local pi = GetPlayerId(p)
		NumberRem(pi, before)
		NumberAdd(pi, after)
	end
	
	-- Зачистка
	udg_LocalOtrad = CreateGroup()
	
	u = nil
end
-- ***************************************************************************
-- *  TryBuy
---@param p player
---@param ePoints integer
---@return nothing
function TryBuy(p, ePoints)
	
	local u
	local itemId
	GroupEnumUnitsOfPlayer(gGroup, p, LiveHero)
	u = GroupPickRandomUnit2(gGroup)
	if u ~= nil then
		
		if UnitInventoryCount(u) >= 6 then
			RemoveItem(UnitItemInSlot(u, GetRandomInt(0, 5)))
		end
		
		gInt = GetRandomInt(1, 6)
		if ePoints < 35 then
			if gInt == 1 then
				itemId = FourCC('I02S')
			elseif gInt == 2 then
				itemId = FourCC('I030')
			elseif gInt == 3 then
				itemId = FourCC('I02Z')
			elseif gInt == 4 then
				itemId = FourCC('I02Y')
			elseif gInt == 5 then
				itemId = FourCC('I02T')
			elseif gInt == 6 then
				itemId = FourCC('I02X')
			end
		elseif ePoints < 150 then
			
			if gInt == 1 then
				itemId = FourCC('I010')
			elseif gInt == 2 then
				itemId = FourCC('I01A')
			elseif gInt == 3 then
				itemId = FourCC('I02Z')
			elseif gInt == 4 then
				itemId = FourCC('I01P')
			elseif gInt == 5 then
				itemId = FourCC('I002')
			elseif gInt == 6 then
				itemId = FourCC('I003')
			end
		else
			
			if gInt == 1 then
				itemId = FourCC('I00W')
			elseif gInt == 2 then
				itemId = FourCC('I030')
			elseif gInt == 3 then
				itemId = FourCC('I011')
			elseif gInt == 4 then
				itemId = FourCC('I00F')
			elseif gInt == 5 then
				itemId = FourCC('I017')
			elseif gInt == 6 then
				itemId = FourCC('I01C')
			end
		end
		
		
		if GetInventoryIndexOfItemTypeBJ(u, itemId) == 0 then
			UnitAddItemByIdSwapped(itemId, u)
		end
		
	end
	
	u = nil
end
-- ***************************************************************************
-- *  SpawnMageTp
---@param pi integer
---@return nothing
function MakeMageTp(pi)
	local race = AiRaces[AiRace[pi]]
	local mageUnit = (race and race.mageTpUnit) or FourCC('h07A')
	GroupEnumUnitsOfPlayer(gGroup, Player(pi), Altars)
	if FirstOfGroup(gGroup) ~= nil then
		gUnit2 = GroupPickRandomUnit2(gGroup)
		gUnit = CreateUnit(Player(pi), mageUnit, GetUnitX(gUnit2), GetUnitY(gUnit2), 0)
		GroupAddUnit(udg_Ai_army[pi], gUnit)
		GroupAddUnit(AiUnitsToPort[pi], gUnit)
		NumberAdd(pi, FourCC('h07A'))
		
	end
end
-- ***************************************************************************
-- *  LibDifferentAiStuff End
-- library LibDifferentAiStuff ends
