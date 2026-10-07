-- library LibDifferentAiStuff:
-- ***************************************************************************
-- *  AiData
--  Для работы надо номер игрока, ид юнита
---@param pi integer
---@param id integer
---@return integer
g_AiCounts = {}

function getAiCount(pi, id)
	local t = g_AiCounts[pi]
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
	local t = g_AiCounts[pi]
	if t ~= nil then return (t[id] or 0) > 0 end
	return false
end
--  Для работы надо номер игрока, ид юнита
---@param pi integer
---@param id integer
---@return nothing
function NumberAdd(pi, id)
	local t = g_AiCounts[pi]
	if t == nil then t = {}; g_AiCounts[pi] = t end
	local c = (t[id] or 0) + 1
	t[id] = c
end
function NumberSet(pi, id, amount)
	local t = g_AiCounts[pi]
	if t == nil then t = {}; g_AiCounts[pi] = t end
	t[id] = amount
end
---@param pi integer
---@param id integer
---@return nothing
function NumberRem(pi, id)
	local t = g_AiCounts[pi]
	if t == nil then t = {}; g_AiCounts[pi] = t end
	local c = (t[id] or 0) - 1
	t[id] = c
end
---@param pi integer
---@param id integer
---@return nothing
function NumberReset(pi, id)
	local t = g_AiCounts[pi]
	if t ~= nil then t[id] = nil end
end
---@param pi integer
---@return nothing
function NumberResetAll(pi)
	g_AiCounts[pi] = nil
end
---@param pi integer
---@return number
function AiSyncCounts(pi)
	local tbl = {}
	ForGroup(udg_Ai_units[pi], function()
		local id = GetUnitTypeId(GetEnumUnit())
		tbl[id] = (tbl[id] or 0) + 1
	end)
	local drifted = 0
	local cts = g_AiCounts[pi]
	if cts == nil then cts = {}; g_AiCounts[pi] = cts end
	for id, cnt in pairs(tbl) do
		local old = cts[id] or 0
		if old ~= cnt then
			cts[id] = cnt
			drifted = drifted + 1
			ProbeLogWrite("[AISYNC] pi=" .. pi .. " id=" .. id .. " old=" .. old .. " new=" .. cnt)
		end
	end
	return drifted
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
local function AiTeleportOwnsUnit(pi, u)
	return udg_AiControl[pi] == true and u ~= nil and UnitAlive(u) and GetOwningPlayer(u) == Player(pi)
end

function ChoseRandomSpot(dest, pi, x, y)
	local group = CreateGroup()
	GroupEnumUnitsInRange(group, x, y, 3200, nil)
	local buildings = {}
	for i = 0, BlzGroupGetSize(group) - 1 do
		local u = BlzGroupUnitAt(group, i)
		if AiTeleportOwnsUnit(pi, u) and IsUnitType(u, UNIT_TYPE_STRUCTURE) then
			buildings[#buildings + 1] = u
		end
	end
	DestroyGroup(group)
	if #buildings == 0 then return nil end
	return buildings[GetRandomInt(1, #buildings)]
end

function MakeTPMage(dest, u2, pi)
	if not AiTeleportOwnsUnit(pi, dest) or not AiTeleportOwnsUnit(pi, u2) then return end
	if getAiCount(pi, gMageTP) >= 10 or GetUnitAbilityLevel(dest, FourCC('A1RD')) > 0 then return end
	local x, y = GetUnitX(dest), GetUnitY(dest)
	local building = ChoseRandomSpot(dest, pi, x, y)
	if building ~= nil then x, y = GetUnitX(building), GetUnitY(building) end
	local mage = CreateUnit(Player(pi), gMageTP, x, y, 0)
	if mage == nil then return end
	GroupAddUnit(udg_Ai_army[pi], mage)
	GroupAddUnit(AiUnitsToPort[pi], mage)
	NumberAdd(pi, gMageTP)
	AddAbilityTimed(dest, FourCC('A1RD'), 8)
	RemoveEffectTimed(AddSpecialEffect("Abilities\\Spells\\Human\\MassTeleport\\MassTeleportCaster.mdl", x, y), 3)
	IssuePointOrder(mage, "darksummoning", GetUnitX(u2), GetUnitY(u2))
end

local function AiTeleportPickArmyUnit(pi, fast)
	local group = CreateGroup()
	GroupEnumUnitsOfPlayer(group, Player(pi), nil)
	local army = {}
	for i = 0, BlzGroupGetSize(group) - 1 do
		local u = BlzGroupUnitAt(group, i)
		if AiTeleportOwnsUnit(pi, u) and IsUnitInGroup(u, udg_Ai_army[pi])
			and (fast or IsAiCombatRetaskable(u)) then
			army[#army + 1] = u
		end
	end
	DestroyGroup(group)
	if #army == 0 then return nil end
	return army[GetRandomInt(1, #army)]
end

local function AiTeleportTo(u, fast)
	if u == nil or not UnitAlive(u) then return end
	local pi = GetPlayerId(GetOwningPlayer(u))
	if not AiTeleportOwnsUnit(pi, u) then return end
	local target = AiTeleportPickArmyUnit(pi, fast)
	if target == nil then return end
	if IsUnitInGroup(u, udg_ZahvatBuildings) then
		UnitAddAbility(u, FourCC('A0Y4'))
		IssuePointOrder(u, "darksummoning", GetUnitX(target), GetUnitY(target))
		if Random(1, 4) then MakeTPMage(u, target, pi) end
	elseif GetUnitTypeId(u) == gMageTP then
		IssuePointOrder(u, "darksummoning", GetUnitX(target), GetUnitY(target))
	else
		MakeTPMage(u, target, pi)
	end
end

function PortTo(u)
	AiTeleportTo(u, false)
end

function PortToFast(u)
	AiTeleportTo(u, true)
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
	if udg_AiControl[pi] ~= true then return end
	local u = GroupPickRandomUnit2(AiUnitsToPort[pi])
	if not AiTeleportOwnsUnit(pi, u) then
		if u ~= nil then GroupRemoveUnit(AiUnitsToPort[pi], u) end
		return
	end
	if HasEnemyNear(u) then PortTo(u) end
end
-- ***************************************************************************
-- *  RequestPort
---@param u unit
function RequestPort(u)
	if u == nil or not UnitAlive(u) then return end
	local pi = GetPlayerId(GetOwningPlayer(u))
	if udg_AiControl[pi] ~= true then return end
	local caster = GroupPickRandomUnit2(AiUnitsToPort[pi])
	if not AiTeleportOwnsUnit(pi, caster) then
		if caster ~= nil then GroupRemoveUnit(AiUnitsToPort[pi], caster) end
		return
	end
	if HasEnemyNear(caster) then PortTo(caster) end
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
	local itemGoldCost = 1000
	GroupEnumUnitsOfPlayer(gGroup, p, LiveHero)
	u = GroupPickRandomUnit2(gGroup)
	if u ~= nil then
		local invSize = UnitInventorySize(u)
		if invSize <= 0 then invSize = 6 end

		if UnitInventoryCount(u) >= invSize then
			u = nil
			return
		end

		-- Build set of item types the hero already owns (manual scan avoids
		-- GetInventoryIndexOfItemTypeBJ bugs and WC3's no-duplicate-items rule)
		local owned = {}
		for s = 0, invSize - 1 do
			local slotItem = UnitItemInSlot(u, s)
			if slotItem ~= nil then
				owned[GetItemTypeId(slotItem)] = true
			end
		end

		-- Collect available items from the tier (skip already-owned)
		local available = {}
		local tierItems
		if ePoints < 35 then
			tierItems = {FourCC('I02S'), FourCC('I030'), FourCC('I02Z'), FourCC('I02Y'), FourCC('I02T'), FourCC('I02X')}
		elseif ePoints < 150 then
			tierItems = {FourCC('I010'), FourCC('I01A'), FourCC('I02Z'), FourCC('I01P'), FourCC('I002'), FourCC('I003')}
		else
			tierItems = {FourCC('I00W'), FourCC('I030'), FourCC('I011'), FourCC('I00F'), FourCC('I017'), FourCC('I01C')}
		end
		for _, tid in ipairs(tierItems) do
			if not owned[tid] then
				available[#available + 1] = tid
			end
		end

		if #available > 0 then
			itemId = available[GetRandomInt(1, #available)]
			if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) >= itemGoldCost then
				local it = UnitAddItemById(u, itemId)
				if it ~= nil and UnitHasItem(u, it) then
					SetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) - itemGoldCost)
				elseif it ~= nil then
					RemoveItem(it)
				end
			end
		end

	end

	u = nil
end
-- ***************************************************************************
-- *  SpawnMageTp
---@param pi integer
---@return nothing
function MakeMageTp(pi)
	if udg_AiControl[pi] ~= true then return end
	local race = AiRaces[AiRace[pi]]
	local mageUnit = (race and race.mageTpUnit) or FourCC('h07A')
	local group = CreateGroup()
	GroupEnumUnitsOfPlayer(group, Player(pi), Altars)
	local altar = GroupPickRandomUnit2(group)
	DestroyGroup(group)
	if altar == nil then return end
	local mage = CreateUnit(Player(pi), mageUnit, GetUnitX(altar), GetUnitY(altar), 0)
	if mage == nil then return end
	GroupAddUnit(udg_Ai_army[pi], mage)
	GroupAddUnit(AiUnitsToPort[pi], mage)
	NumberAdd(pi, FourCC('h07A'))
end
-- ***************************************************************************
-- *  LibDifferentAiStuff End
-- library LibDifferentAiStuff ends
