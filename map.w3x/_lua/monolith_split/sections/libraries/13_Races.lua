-- library Races:
-- ***************************************************************************
-- *  BuildTemplate
--  Добавляет строение во варианты постройки
---@param buildingId integer
---@param count integer
---@return nothing
function AddBuilding(buildingId, count)
	tB = 1	--  Базовый шанс
	while true do
		tArray[0] = tArray[0] + 1
		tArray[tArray[0]] = buildingId
		tB = tB + 1
		if tB > count then break end
	end
end
--  Проверяет лимит и добавляет во варианты постройки
---@param pi integer
---@param buildingId integer
---@param limit integer
---@param power integer
---@return nothing
function CheckAndAddBuilding(pi, buildingId, limit, power)
	if (AiData[pi][buildingId] or 0) < limit then
		AddBuilding(buildingId, power)
	end
end
-- ***************************************************************************
-- *  UnitTrainTemplate
--  Добавляет юнит в массив tArray с учетом количества
---@param unitId integer
---@param power integer
---@return nothing
function AddUnit(unitId, power)
	tB = 1
	while true do
		tArray[0] = tArray[0] + 1
		tArray[tArray[0]] = unitId
		tB = tB + 1
		if tB > power then break end
	end
end
--  Проверяет лимит и добавляет юнит в массив tArray с учетом мощности
---@param pi integer
---@param unitId integer
---@param limit integer
---@param power integer
---@return nothing
function CheckAndAddUnit(pi, unitId, limit, power)
	if limit == 0 or (AiData[pi][unitId] or 0) < limit then
		AddUnit(unitId, power)
	end
end
--  Заказывает юнита рандомом массива если не пуст, очищает кол-во на случай если забуду
---@param u unit
---@return nothing
function aiOrderUnit(u)
	if tArray[0] > 0 then
		IssueImmediateOrderById(u, tArray[GetRandomInt(1, tArray[0])])
		tArray[0] = 0
	end
end
-- ***************************************************************************
-- *  MakeGrade
---@return boolean
function ThisType()
	if GetUnitTypeId(GetFilterUnit()) == udg_LocalInteger5 then
		Counter = Counter + 1
		return true
	end
	return false
end
---@param gamer player
---@param GradeUnit integer
---@param Grade integer
---@return nothing
function MakeGrade(gamer, GradeUnit, Grade)
	local b = nil
	
	udg_LocalInteger5 = GradeUnit
	Counter = 0
	b = Condition(ThisType)
	GroupEnumUnitsOfPlayer(gGroup, gamer, b)
	gUnit = BlzGroupUnitAt(gGroup, GetRandomInt(0, Counter - 1))
	if gUnit ~= nil then
		IssueImmediateOrderById(gUnit, Grade)
	end
	
	DestroyBoolExpr(b)
	b = nil
end
---@param gamer player
---@param GradeUnit integer
---@param Grade integer
---@param Cap integer
---@return nothing
function MakeGradeCheckCap(gamer, GradeUnit, Grade, Cap)
	if GetPlayerTechCount(gamer, Grade, true) <= Cap then
		MakeGrade(gamer, GradeUnit, Grade)
	end
end
-- ***************************************************************************
-- *  JoinArmyUnit
---@param u unit
---@param pi integer
---@return nothing
function aiUnitJoinsArmy(u, pi)
	-- set gX = GetUnitX(u)
	-- set gY = GetUnitY(u)
	-- set gUnit = OwnCapitalInRange(pi,gX,gY,3500)
	-- if not aiUnitJoinsCapitalGuard(u,gUnit,pi) then
	GroupAddUnit(udg_Ai_army[pi], u)
	NumberAdd(pi, StringHash("Number"))
	local joinLogCount = (AiData[pi][StringHash("Log_AiArmyJoinCount")] or 0)
	if joinLogCount < 12 then
		AiData[pi][StringHash("Log_AiArmyJoinCount")] = joinLogCount + 1
		ProbeLogWrite("[AIARMY] join pi=" .. tostring(pi) .. " unitId=" .. tostring(GetUnitTypeId(u)) .. " count=" .. tostring(joinLogCount + 1))
	end
	-- endif
end
-- ***************************************************************************
-- *  aiUnitJoinsCapitalGuard
---@param u unit
---@param pi integer
---@return boolean
function aiUnitJoinsCapitalGuard(u, pi)
	if playerCapital[pi] == nil then
		if udg_Octhet then
			-- call BJDebugMsg("Не прошел в стражу нет столицы")
		end
		return false
	elseif DistanceBetweenUnits(playerCapital[pi], u) > 3000 then
		if udg_Octhet then
			-- call BJDebugMsg("Не прошел в стражу расстояние "+ R2SW_Polyfill(DistanceBetweenUnits(playerCapital[pi],u))) 
		end
		return false
	elseif (AiData[pi][StringHash("NumberGuard")] or 0) + 15 > (AiData[pi][StringHash("Number")] or 0) / 5 then
		-- call BJDebugMsg("Не прошел в стражу стража больше "+I2S((AiData[pi][StringHash("NumberGuard")] or 0))+I2S((AiData[pi][StringHash("Number")] or 0)/5))
		return false
	end
	
	NumberAdd(pi, StringHash("NumberGuard"))
	GroupAddUnit(AiCapitalGuard[pi], u)
	IssuePointOrder(u, "smart", GetUnitX(playerCapital[pi]), GetUnitY(playerCapital[pi]))
	
	return true
end
-- ***************************************************************************
-- *  AttackerHumanFleet
---@param id integer
---@param u unit
---@param target unit
---@param x real
---@param y real
---@return nothing
function Attacker_HumanFleet(id, u, target, x, y)
	
	if id == FourCC('h00Z') or id == FourCC('h00Y') and IsUnitType(target, UNIT_TYPE_STRUCTURE) == false then
		gInt = GetRandomInt(1, 6)
		if gInt == 1 and GetUnitStatePercent(target, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) then
			gX2 = GetUnitX(u) - GetUnitX(target)
			gY2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(gX2 * gX2 + gY2 * gY2) < 125 then
				IssueTargetOrder(u, "ancestralspirit", target)
			else
				-- call IssuePointOrder(u, "Move", x,y)
			end
		elseif gInt == 2 then
			gX2 = GetUnitX(u) - GetUnitX(target)
			gY2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(gX2 * gX2 + gY2 * gY2) < 300 then
				IssuePointOrder(u, "clusterrockets", x, y)
			else
				-- call IssuePointOrder(u, "Move", x,y)
			end
			
			
		elseif gInt == 3 and GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < 40 then
			IssueImmediateOrder(u, "tranquility")
		end
	end
	
end
-- ***************************************************************************
-- *  NavalTrainCommon
---@param u unit
---@param pi integer
---@return nothing
function aiNavalTrain_Common(u, pi)
	if Random(1, 2) and (AiData[pi][FourCC('h00Y')] or 0) < 50 then
		IssueImmediateOrderById(u, FourCC('h00Y'))
	elseif (AiData[pi][FourCC('h00Z')] or 0) < 75 then
		IssueImmediateOrderById(u, FourCC('h00Z'))
	end
end
-- ***************************************************************************
-- *  StrategFleetGrades
---@param i integer
---@param p player
---@param id integer
---@return nothing
function strategFleetGrades(i, p, id)
	if i > 45 then
		MakeGradeCheckCap(p, id, FourCC('R005'), 6)
		MakeGradeCheckCap(p, id, FourCC('R006'), 6)
		MakeGradeCheckCap(p, id, FourCC('R007'), 6)
		MakeGradeCheckCap(p, id, FourCC('R002'), 6)
		MakeGradeCheckCap(p, id, FourCC('R003'), 6)
	end
end
-- ***************************************************************************
-- *  StartBloodElves
---@param pi integer
---@return nothing
function startBloodElves(pi)
	CreateNUnitsAtLoc(8, FourCC('h04K'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
	CreateNUnitsAtLoc(1, FourCC('h04C'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
	GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
	AiData[pi][FourCC('h04K')] = 8
	AiData[pi][FourCC('h04C')] = 1
	SetPlayerName(Player(pi), "Эльфы Крови (" .. I2S(pi + 1) .. ")")
	AiData[pi][StringHash("Race")] = "BE"
	TriggerExecute(gg_trg_BloodElvesOn)
	AiRace[pi] = "BloodElves"
	ProbeLogWrite("[AI] startBloodElves pi=" .. tostring(pi) .. " workers=8h04K building=1h04C")
end
-- ***************************************************************************
-- *  JoinBloodElves
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_BloodElves(id, pi, u)
	
	
	if id == FourCC('h04K') then
		GroupAddUnit(udg_Ai_builders[pi], u)
	elseif id == FourCC('h00X') or id == FourCC('h00Y') or id == FourCC('h00Z') then
		GroupAddUnit(udg_Ai_navy[pi], u)
		NumberAdd(pi, StringHash("NumberN"))
	elseif aiUnitJoinsCapitalGuard(u, pi) then
	else
		aiUnitJoinsArmy(u, pi)
	end
	
	
	
	-- Герои
	-- Герой ЧАродей
	if id == FourCC('H034') then
		gInt = GetRandomInt(1, 3)
		if gInt == 1 then
			SelectHeroSkill(u, FourCC('AHfs'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('AHbn'))
		else
			SelectHeroSkill(u, FourCC('AHdr'))
		end
		
		
		-- Герой Странник
	elseif id == FourCC('Hjnd') then
		gInt = GetRandomInt(1, 3)
		if gInt == 1 then
			SelectHeroSkill(u, FourCC('A07U'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A0LQ'))
		else
			SelectHeroSkill(u, FourCC('A07V'))
		end
		
		
		-- Герой Паладин
	elseif id == FourCC('H045') then
		gInt = GetRandomInt(1, 3)
		if gInt == 1 then
			SelectHeroSkill(u, FourCC('A08H'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A07W'))
		else
			SelectHeroSkill(u, FourCC('AHbh'))
		end
		
		
		-- Флот 
	elseif id == FourCC('h00Z') then
		IssueImmediateOrder(u, "nagabuild")
		IssueImmediateOrder(u, "spellbook")
		gInt = GetRandomInt(1, 3)
		if gInt == 1 then
			IssueImmediateOrder(u, "nagabuild")
		elseif gInt == 2 then
			IssueImmediateOrder(u, "mounthippogryph")
		else
			IssueImmediateOrder(u, "monsoon")
		end
		
	end
end
-- ***************************************************************************
-- *  AttackedBloodElves
---@param u unit
---@return nothing
function AttackedBloodElves(u)
	-- Мечник
	if GetUnitTypeId(u) == FourCC('h03V') then
		gInt = GetRandomInt(1, 5)
		if gInt == 1 then
			IssueImmediateOrder(u, "defend")
		elseif gInt == 2 then
			IssueImmediateOrder(u, "manashieldon")
		elseif gInt == 3 then
			IssueImmediateOrder(u, "undefend")
		end
		
	elseif GetUnitTypeId(u) == FourCC('h03B') then
		gInt = GetRandomInt(1, 3)
		if gInt == 1 then
			IssueImmediateOrder(u, "defend")
		elseif gInt == 2 then
			IssueImmediateOrder(u, "undefend")
			
		end
	end
	
end
-- ***************************************************************************
-- *  AttackerBloodElves
---@param id integer
---@param u unit
---@param target unit
---@param p player
---@return nothing
function Attacker_BloodElves(id, u, target, p)
	local i
	local x = GetUnitX(target)
	local y = GetUnitY(target)
	local x2
	local y2
	
	-- Чародей
	if id == FourCC('H043') then
		i = GetRandomInt(1, 6)
		if i == 1 then
			IssueTargetOrder(u, "banish", target)
		elseif i == 2 then
			IssueTargetOrder(u, "steal", target)
		elseif i == 3 then
			IssuePointOrder(u, "flamestrike", x, y)
		elseif i == 4 then
			IssueImmediateOrder(u, "summonphoenix")
		end
		
		-- /Если герой Ренджер
	elseif id == FourCC('Hjnd') then
		i = GetRandomInt(1, 3)
		if i == 1 and  not IsUnitType(target, UNIT_TYPE_STRUCTURE) then
			IssueTargetOrder(u, "shadowstrike", target)
		elseif IsUnitType(target, UNIT_TYPE_HERO) then
			IssueTargetOrder(u, "faeriefire", target)
		end
		
		
		-- /Если герой Паладин
	elseif id == FourCC('H045') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			IssueImmediateOrder(u, "roar")
		elseif i == 2 then
			IssueImmediateOrder(u, "fanofknives")
		elseif i == 3 then
			IssueImmediateOrder(u, "ressurection")
		end
		
		--  ------ Юниты    
		
		-- /Всадник
	elseif id == FourCC('H03H') then
		i = GetRandomInt(1, 4)
		if i == 1 then
			IssueImmediateOrder(u, "berserk")
		end
		
		
		-- /Магистр
	elseif id == FourCC('n040') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			IssueImmediateOrder(u, "frostarmoron")
			IssueImmediateOrder(u, "curseoff")
		elseif i == 2 then
			IssueImmediateOrder(u, "frostarmoroff")
			IssueImmediateOrder(u, "curseon")
			
		elseif i == 3 then
			x2 = GetUnitX(u) - GetUnitX(target)
			y2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(x2 * x2 + y2 * y2) < 490 then
				IssueTargetOrder(u, "carrionswarm", target)
			end
		end
		
		-- / Арканистка
	elseif id == FourCC('h041') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			IssueTargetOrder(u, "polymorph", target)
		elseif i == 2 then
			x2 = GetUnitX(u) - GetUnitX(target)
			y2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(x2 * x2 + y2 * y2) < 490 then
				IssueTargetOrder(u, "devourmagic", target)
			end
		end
		-- Чернокнижник
	elseif id == FourCC('h042') then
		i = GetRandomInt(1, 6)
		if i == 1 then
			IssueImmediateOrder(u, "faeriefireoff")
			IssueImmediateOrder(u, "curseon")
			IssueImmediateOrder(u, "bloodlustoff")
		elseif i == 2 then
			IssueImmediateOrder(u, "faeriefireoff")
			IssueImmediateOrder(u, "curseoff")
			IssueImmediateOrder(u, "bloodluston")
		elseif i == 3 then
			IssueImmediateOrder(u, "faeriefireon")
			IssueImmediateOrder(u, "curseoff")
			IssueImmediateOrder(u, "bloodluston")
			
		end
		--  Рыцарь крови
	elseif id == FourCC('H03Y') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			CheckPlayer = p
			GroupEnumUnitsInRange(gGroup, x, y, 550, ToHeal)
			gUnit2 = GroupPickRandomUnit2(gGroup)
			IssueTargetOrder(u, "healingwave", gUnit2)
			
		end
		
		--  ФЛот
	else
		Attacker_HumanFleet(id, u, target, x, y)
	end
	
end
-- ***************************************************************************
-- *  StrategBloodElves
---@param id integer
---@return nothing
function Strateg_BloodElves_EC(id)
	-- Это ферма
	if id == FourCC('h04M') then
		udg_LocalInteger3 = udg_LocalInteger3 + 1
		-- Это Т1
	elseif id == FourCC('h04C') then
		udg_LocalInteger3 = udg_LocalInteger3 + 2
		-- Это Т2
	elseif id == FourCC('h04B') then
		udg_LocalInteger3 = udg_LocalInteger3 + 5
		-- Это Т3
	elseif id == FourCC('h04A') then
		udg_LocalInteger3 = udg_LocalInteger3 + 8
	end
end
---@param i integer
---@param pi integer
---@param p player
---@return nothing
function Strateg_BloodElves(i, pi, p)
	local r = 0
	if Grades[pi] < 100 then
		if i > 17 then
			
			
			r = GetRandomInt(1, 3)
			
			if r == 1 then
				--  Кузница
				MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01L'), 6)
				MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01J'), 6)
				MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01K'), 6)
				MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01M'), 6)
			elseif r == 2 then
				MakeGradeCheckCap(p, FourCC('h04R'), FourCC('R01R'), 6)
				
				--  Лесопилка
				MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03I'), 6)
				MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03J'), 6)
				MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R01N'), 6)
			else
				MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R01T'), 6)
				
				MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03E'), 6)
				MakeGradeCheckCap(p, FourCC('h04Q'), FourCC('R03F'), 6)
				
				-- Казармы
				MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R03K'), 1)
				
				-- Покупка предмета
			end
		end
		
		
		
		
		if i > 35 and ((AiData[pi][FourCC('h04B')] or 0) + (AiData[pi][FourCC('h04A')] or 0) >= 1) then
			
			
			r = GetRandomInt(1, 3)
			if r == 1 then
				--  Казармы R01Y,R01X,R01V,R01W
				MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01Y'), 1)
				MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01X'), 1)
				
				MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01W'), 1)
				MakeGradeCheckCap(p, FourCC('h04D'), FourCC('R01W'), 1)
				
				--  Здание магов R0BU,R01O,R01P,R01Q,R01S
				MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R0BU'), 1)
				MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01O'), 6)
				
			elseif r == 2 then
				MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01P'), 6)
				MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01Q'), 6)
				MakeGradeCheckCap(p, FourCC('h04E'), FourCC('R01S'), 1)
				
				
				-- Мастерская R03N,R021,R0KF
				
				MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R03N'), 6)
				MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R021'), 6)
			else
				MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R021'), 6)
				MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R03Q'), 6)
				MakeGradeCheckCap(p, FourCC('h04G'), FourCC('R021'), 6)
				MakeGradeCheckCap(p, FourCC('h04G'), FourCC('Rhcd'), 6)
			end
			
			
			-- Хранилище маны
			
			r = GetRandomInt(0, 4)
			if r == 0 then
				MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R03R'), 3)
			elseif r == 1 then
				MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01H'), 3)
			elseif r == 2 then
				MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01I'), 3)
			elseif r == 3 then
				MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01G'), 3)
			else
				MakeGradeCheckCap(p, FourCC('h04F'), FourCC('R01D'), 3)
			end
			
			--  Флот
			if i > 45 then
				MakeGradeCheckCap(p, FourCC('h011'), FourCC('R005'), 6)
				MakeGradeCheckCap(p, FourCC('h011'), FourCC('R006'), 6)
				MakeGradeCheckCap(p, FourCC('h011'), FourCC('R007'), 6)
				MakeGradeCheckCap(p, FourCC('h011'), FourCC('R002'), 6)
				MakeGradeCheckCap(p, FourCC('h011'), FourCC('R003'), 6)
			end
			
			
			
			
			
		end
	else
		warRace(Grades[pi], p)
		
	end
	
	
	-- Купи предмет простой
	if i > 20 and GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
		TryBuy(p, i)
	end
	
	-- Делай т2
	if i > 25 and (AiData[pi][FourCC('h04B')] or 0) < 3 then
		BuildT(p, FourCC('h04C'), FourCC('h04B'))
	end
	
	-- Делай т3
	if i > 55 and (AiData[pi][FourCC('h04A')] or 0) < 3 then
		BuildT(p, FourCC('h04B'), FourCC('h04A'))
	end
	
	-- Спавн мага тп
	if i > 60 and (AiData[pi][FourCC('h07A')] or 0) < 3 then
		MakeMageTp(pi)
	end
	
	
	
	
	
end
-- ***************************************************************************
-- *  BuildBloodElves
---@param pi integer
---@return integer
function ChooseBuildings_BloodElves(pi)
	local i
	
	--  Инициализируем массив и добавляем стартовый вариант
	tArray[0] = 1
	tArray[1] = FourCC('h04M')	--  1 Ферма
	
	--  Добавляем здания по условиям
	CheckAndAddBuilding(pi, FourCC('h04C'), 4, 4)	--  Ратуша
	CheckAndAddBuilding(pi, FourCC('h04M'), 15, 4)	--  Дополнительные фермы
	CheckAndAddBuilding(pi, FourCC('h04D'), 15, 4)	--  Казарма
	CheckAndAddBuilding(pi, FourCC('h04N'), 25, 1)	--  Башня
	CheckAndAddBuilding(pi, FourCC('h04Q'), 5, 2)	--  Лесопилка
	CheckAndAddBuilding(pi, FourCC('h04R'), 6, 2)	--  Кузница
	CheckAndAddBuilding(pi, FourCC('h05J'), 3, 8)	--  Алтарь
	
	--  Проверяем условия для Мастерской и Храма
	if (AiData[pi][FourCC('h04B')] or 0) + (AiData[pi][FourCC('h04A')] or 0) >= 1 then
		CheckAndAddBuilding(pi, FourCC('h04G'), 15, 8)	--  Мастерская
		CheckAndAddBuilding(pi, FourCC('h04E'), 15, 8)	--  Храм
	end
	
	--  Хранилище энергии
	CheckAndAddBuilding(pi, FourCC('h04F'), 12, 2)
	
	--  Выбираем случайный вариант из массива
	i = GetRandomInt(1, tArray[0])
	return tArray[i]
end
-- ***************************************************************************
-- *  BuildingsBloodElves
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function PereborBuildings2_BloodElves(id, pi, u)
	local b = 0
	local i = 0
	local a = {}
	if id == FourCC('h04D') then	-- Казармы
		
		
		a[0] = 1	-- Кол-во вариантов со старта
		a[1] = FourCC('h03V')	--  1 Пехотинец
		
		--  Доп. варианты при условиях
		
		--  2 Лучница
		if (AiData[pi][FourCC('h04R')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('n00I')
				
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  3 Всадник
		if (AiData[pi][FourCC('h04B')] or 0) + (AiData[pi][FourCC('h04A')] or 0) >= 1 then
			i = 4	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h03X')
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  4 Рыцарь крови
		if (AiData[pi][FourCC('h04A')] or 0) >= 1 then
			i = 6	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h03Y')
				b = b + 1
				if b >= i then break end
			end
		end
		i = GetRandomInt(1, a[0])
		IssueImmediateOrderById(u, a[i])
		
		
		--  Ратуша
	elseif id == FourCC('h04C') then
		
		
		-- Строитель
		if (AiData[pi][FourCC('h04K')] or 0) < 20 then
			IssueImmediateOrderById(u, FourCC('h04K'))
		end
		
		--  Мастеская
	elseif id == FourCC('h04G') then
		a[0] = 0	-- Кол-во вариантов со старта
		
		
		--  Доп. варианты при условиях
		-- Баллиста
		if (AiData[pi][FourCC('h04B')] or 0) + (AiData[pi][FourCC('h04A')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('e001')
				
				b = b + 1
				if b >= i then break end
			end
		end
		
		
		
		--  2 Элем
		if (AiData[pi][FourCC('h04B')] or 0) + (AiData[pi][FourCC('h04A')] or 0) >= 1 then
			i = 2	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h046')
				
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  3 Повозка
		if (AiData[pi][FourCC('h04B')] or 0) + (AiData[pi][FourCC('h04A')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('e030')
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  4 Голем
		if (AiData[pi][FourCC('h04A')] or 0) >= 1 then
			i = 6	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h03Z')
				b = b + 1
				if b >= i then break end
			end
		end
		i = GetRandomInt(1, a[0])
		IssueImmediateOrderById(u, a[i])
		
		
		--  Волшебное святилище
	elseif id == FourCC('h04E') then
		udg_LocalInteger3 = GetRandomInt(1, 4)
		if udg_LocalInteger3 == 1 then
			IssueImmediateOrderById(u, FourCC('h03W'))
		elseif udg_LocalInteger3 == 2 then
			IssueImmediateOrderById(u, FourCC('h040'))
		elseif udg_LocalInteger3 == 3 then
			IssueImmediateOrderById(u, FourCC('h041'))
		else
			IssueImmediateOrderById(u, FourCC('h042'))
		end
		
		
		--  Алтарь
	elseif id == FourCC('h05J') then
		udg_LocalInteger3 = GetRandomInt(1, 3)
		if udg_LocalInteger3 == 1 then
			IssueImmediateOrderById(u, FourCC('Hjnd'))
		end
		if udg_LocalInteger3 == 2 then
			IssueImmediateOrderById(u, FourCC('H043'))
		end
		if udg_LocalInteger3 == 3 then
			IssueImmediateOrderById(u, FourCC('H045'))
		end
		
		
	end
	
	
end
-- ***************************************************************************
-- *  UpgradeBloodElves
---@param pi integer
---@param id integer
---@return nothing
function UpgradeBloodElves(pi, id)
	if id == FourCC('h05V') then
		NumberRem(pi, FourCC('h05U'))
	elseif id == FourCC('h05W') then
		NumberRem(pi, FourCC('h05V'))
	end
end
-- ***************************************************************************
-- *  GetLvlBloodElves
---@param u unit
---@return nothing
function GetLvlBloodElves(u)
	-- Герой ЧАродей
	if GetUnitTypeId(u) == FourCC('H043') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('AHpx'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('AHfs'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('AHdr'))
		else
			SelectHeroSkill(u, FourCC('AHpx'))
		end
		
		
		
		
		-- Герой Ренодежр
	elseif GetUnitTypeId(u) == FourCC('Hjnd') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A07V'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A07U'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A0LQ'))
		else
			SelectHeroSkill(u, FourCC('AEar'))
		end
		
		
		
		-- Герой Паладин
	elseif GetUnitTypeId(u) == FourCC('H045') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('AHre'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A08H'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A07W'))
		else
			SelectHeroSkill(u, FourCC('AHbh'))
		end
	end
	
end
-- ***************************************************************************
-- *  StartScarlet
---@param pi integer
---@return nothing
function startScarlet(pi)
	-- Старт юниты
	CreateNUnitsAtLoc(8, FourCC('h014'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
	CreateNUnitsAtLoc(1, FourCC('h05U'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
	GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())

	AiData[pi][FourCC('h014')] = 8
	AiData[pi][FourCC('h05U')] = 1
	SetPlayerName(Player(pi), "Алый Орден (" .. I2S(pi + 1) .. ")")
	AiData[pi][StringHash("Race")] = "AO"
	
	AiRace[pi] = "Scarlet"
	ProbeLogWrite("[AI] startScarlet pi=" .. tostring(pi) .. " workers=8h014 building=1h05U")
end
-- ***************************************************************************
-- *  JoinScarlet
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_Skarlet(id, pi, u)
	local i
	if id == FourCC('h014') then
		GroupAddUnit(udg_Ai_builders[pi], u)
	elseif id == FourCC('h00X') or id == FourCC('h00Y') or id == FourCC('h00Z') then
		GroupAddUnit(udg_Ai_navy[pi], u)
		NumberAdd(pi, StringHash("NumberN"))
	elseif aiUnitJoinsCapitalGuard(u, pi) then
	else
		aiUnitJoinsArmy(u, pi)
	end
	
	
	-- Герои
	-- Герой маг
	if id == FourCC('H06C') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A09K'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A09L'))
		else
			SelectHeroSkill(u, FourCC('A09N'))
		end
		
		
		-- Герой Капитан
	elseif id == FourCC('H06B') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A09G'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A09F'))
		else
			SelectHeroSkill(u, FourCC('A09I'))
		end
		
		
		-- Герой Паладин
	elseif id == FourCC('H03H') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A097'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A09C'))
		else
			SelectHeroSkill(u, FourCC('A09D'))
		end
		
		
		-- Флот 
	elseif id == FourCC('h00Z') then
		IssueImmediateOrder(u, "nagabuild")
		IssueImmediateOrder(u, "spellbook")
		i = GetRandomInt(1, 3)
		if i == 1 then
			IssueImmediateOrder(u, "nagabuild")
		elseif i == 2 then
			IssueImmediateOrder(u, "mounthippogryph")
		else
			IssueImmediateOrder(u, "monsoon")
		end
		
	end
	
	
end
-- ***************************************************************************
-- *  AttackerScarlet
---@param id integer
---@param u unit
---@param target unit
---@param p player
---@return nothing
function Attacker_Skarlet(id, u, target, p)
	local i
	local x = GetUnitX(target)
	local y = GetUnitY(target)
	local x2
	local y2
	
	if id == FourCC('H06C') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			IssueTargetOrder(u, "firebolt", target)
		elseif i == 2 then
			IssuePointOrder(u, "flamestrike", x, y)
		elseif i == 3 then
			IssueImmediateOrder(u, "waterelemental")
		end
		
		-- /Если герой Капиатн
	elseif id == FourCC('H06B') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			IssueImmediateOrder(u, "berserk")
		elseif i == 2 then
			IssueImmediateOrder(u, "thanderclap")
		elseif i == 3 then
			IssueImmediateOrder(u, "roar")
		end
		
		
		-- /Если герой Паладин
	elseif id == FourCC('H03H') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			CheckPlayer = p
			GroupEnumUnitsInRange(gGroup, x, y, 450, ToHeal)
			gUnit2 = GroupPickRandomUnit2(gGroup)
			IssueTargetOrder(u, "firebolt", gUnit2)
		elseif i == 2 then
			IssueImmediateOrder(u, "roar")
		elseif i == 3 then
			IssueImmediateOrder(u, "ressurection")
		end
		
		--  ------ Юниты    
		
		-- /Монахиня
	elseif id == FourCC('h067') then
		i = GetRandomInt(1, 4)
		if i == 1 then
			IssueTargetOrder(u, "flamingarrows", target)
		elseif i == 2 then
			x2 = GetUnitX(u) - GetUnitX(target)
			y2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(x2 * x2 + y2 * y2) < 525 then
				IssueTargetOrder(u, "devourmagic", target)
			end
		end
		
		
		-- /Жрец
	elseif id == FourCC('n008') then
		i = GetRandomInt(1, 4)
		if i == 1 then
			IssueTargetOrder(u, "flamingarrows", target)
		elseif i == 2 then
			x2 = GetUnitX(u) - GetUnitX(target)
			y2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(x2 * x2 + y2 * y2) < 490 then
				IssueTargetOrder(u, "dispel", target)
			end
		end
		
		-- /Гладиатор
	elseif id == FourCC('h03G') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			IssueTargetOrder(u, "berserk", target)
		elseif i == 2 then
			IssuePointOrder(u, "roar", x, y)
		end
		
		
	elseif id == FourCC('h00Z') or id == FourCC('h00Y') and IsUnitType(target, UNIT_TYPE_STRUCTURE) == false then
		i = GetRandomInt(1, 6)
		if i == 1 and GetUnitStatePercent(target, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) then
			x2 = GetUnitX(u) - GetUnitX(target)
			y2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(x2 * x2 + y2 * y2) < 125 then
				IssueTargetOrder(u, "ancestralspirit", target)
			else
				-- call IssuePointOrder(u, "Move", x,y)
			end
		elseif i == 2 then
			x2 = GetUnitX(u) - GetUnitX(target)
			y2 = GetUnitY(u) - GetUnitY(target)
			if SquareRoot(x2 * x2 + y2 * y2) < 300 then
				IssuePointOrder(u, "clusterrockets", x, y)
			else
				-- call IssuePointOrder(u, "Move", x,y)
			end
			
			
		elseif i == 3 and GetUnitStatePercent(u, UNIT_STATE_LIFE, UNIT_STATE_MAX_LIFE) < 45 then
			IssueImmediateOrder(u, "tranquility")
		end
	end
	
end
-- ***************************************************************************
-- *  AttackedScarlet
---@param u unit
---@return nothing
function AttackedScarlet(u)
	-- Тяж Пехотинец
	if GetUnitTypeId(u) == FourCC('h039') then
		gInt = GetRandomInt(1, 5)
		if gInt == 1 then
			IssueImmediateOrder(u, "defend")
		elseif gInt == 2 then
			IssueImmediateOrder(u, "magicdefense")
		elseif gInt == 3 then
			IssueImmediateOrder(u, "undefend")
		elseif gInt == 4 then
			IssueImmediateOrder(u, "magicundefense")
			
		end
		
		-- Мечник
	elseif GetUnitTypeId(u) == FourCC('h03B') then
		gInt = GetRandomInt(1, 3)
		if gInt == 1 then
			IssueImmediateOrder(u, "defend")
		elseif gInt == 2 then
			IssueImmediateOrder(u, "undefend")
			
		end
	end
end
-- ***************************************************************************
-- *  StrategScarlet
---@param id integer
---@return nothing
function Strateg_Scarlet_EC(id)
	-- Это ферма
	if id == FourCC('h05Y') then
		udg_LocalInteger3 = udg_LocalInteger3 + 1
		-- Это Т1
	elseif id == FourCC('h05U') then
		udg_LocalInteger3 = udg_LocalInteger3 + 2
		-- Это Т2
	elseif id == FourCC('h05V') then
		udg_LocalInteger3 = udg_LocalInteger3 + 5
		-- Это Т3
	elseif id == FourCC('h05W') then
		udg_LocalInteger3 = udg_LocalInteger3 + 8
	end
end
---@param i integer
---@param pi integer
---@param p player
---@return nothing
function Strateg_Scarlet(i, pi, p)
	local r = 0
	
	
	if Grades[pi] < 100 then
		if i > 17 then
			
			--  Кузница
			MakeGradeCheckCap(p, FourCC('h060'), FourCC('R04B'), 6)
			MakeGradeCheckCap(p, FourCC('h060'), FourCC('R04A'), 6)
			MakeGradeCheckCap(p, FourCC('h060'), FourCC('R049'), 6)
			MakeGradeCheckCap(p, FourCC('h060'), FourCC('R048'), 6)
			MakeGradeCheckCap(p, FourCC('h060'), FourCC('R04C'), 6)
			
			--  Лесопилка
			MakeGradeCheckCap(p, FourCC('h062'), FourCC('RHac'), 6)
			MakeGradeCheckCap(p, FourCC('h062'), FourCC('Rhlh'), 6)
			
			-- Казармы
			MakeGradeCheckCap(p, FourCC('h05Z'), FourCC('R03K'), 3)
			
			-- Покупка предмета
			if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
				TryBuy(p, i)
			end
		end
		
		
		
		
		if i > 35 and ((AiData[pi][FourCC('h05V')] or 0) + (AiData[pi][FourCC('h05W')] or 0) >= 1) then
			
			--  Казармы
			MakeGradeCheckCap(p, FourCC('h05Z'), FourCC('R03W'), 2)
			MakeGradeCheckCap(p, FourCC('h05Z'), FourCC('R03V'), 2)
			
			MakeGradeCheckCap(p, FourCC('h05Z'), FourCC('R03L'), 2)
			MakeGradeCheckCap(p, FourCC('h05Z'), FourCC('R03M'), 2)
			
			--  Храм
			MakeGradeCheckCap(p, FourCC('h061'), FourCC('R03Y'), 3)
			MakeGradeCheckCap(p, FourCC('h061'), FourCC('R03X'), 3)
			
			-- Мастерская
			r = GetRandomInt(1, 2)
			if r == 1 then
				MakeGradeCheckCap(p, FourCC('h064'), FourCC('R03T'), 6)
			else
				MakeGradeCheckCap(p, FourCC('h064'), FourCC('R03S'), 6)
			end
			MakeGradeCheckCap(p, FourCC('h064'), FourCC('R047'), 6)
			MakeGradeCheckCap(p, FourCC('h064'), FourCC('R046'), 6)
			MakeGradeCheckCap(p, FourCC('h064'), FourCC('R045'), 6)
			MakeGradeCheckCap(p, FourCC('h064'), FourCC('R03U'), 6)
		end
		
		--  Флот
		if i > 45 then
			MakeGradeCheckCap(p, FourCC('h011'), FourCC('R005'), 6)
			MakeGradeCheckCap(p, FourCC('h011'), FourCC('R006'), 6)
			MakeGradeCheckCap(p, FourCC('h011'), FourCC('R007'), 6)
			MakeGradeCheckCap(p, FourCC('h011'), FourCC('R002'), 6)
			MakeGradeCheckCap(p, FourCC('h011'), FourCC('R003'), 6)
		end
	else
		warRace(Grades[pi], p)
		
	end
	
	-- Делай т2
	if i > 25 and (AiData[pi][FourCC('h05V')] or 0) < 3 then
		BuildT(p, FourCC('h05U'), FourCC('h05V'))
	end
	
	-- Делай т3
	if i > 55 and (AiData[pi][FourCC('h05W')] or 0) < 3 then
		BuildT(p, FourCC('h05V'), FourCC('h05W'))
	end
	
	-- Спавн мага тп
	if i > 60 and (AiData[pi][FourCC('h07A')] or 0) < i / 35 then
		MakeMageTp(pi)
	end
	
	-- Выбор Пути Ордена
	if i > 65 and (AiData[pi][FourCC('h05V')] or 0) >= 1 then
		r = GetRandomInt(1, 2)
		if r == 1 then
			MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R040'), 1)
			AiData[pi][FourCC('R040')] = true
		else
			MakeGradeCheckCap(p, FourCC('h05W'), FourCC('R03Z'), 1)
			AiData[pi][FourCC('R03Z')] = true
		end
		
		
		--  Церковь
		MakeGradeCheckCap(p, FourCC('h068'), FourCC('R044'), 3)
		MakeGradeCheckCap(p, FourCC('h068'), FourCC('R043'), 3)
		MakeGradeCheckCap(p, FourCC('h068'), FourCC('R042'), 3)
		MakeGradeCheckCap(p, FourCC('h068'), FourCC('R041'), 3)
	end
	
	
	
	
	
	
	
	
	
	
end
-- ***************************************************************************
-- *  BuildScarlet
---@param pi integer
---@return integer
function ChooseBuildings_ScarletOrden(pi)
	local i
	
	--  Инициализируем массив и добавляем стартовый вариант
	tArray[0] = 1
	tArray[1] = FourCC('h05Y')	--  1 Ферма
	
	--  Добавляем здания по условиям
	CheckAndAddBuilding(pi, FourCC('h05U'), 4, 4)	--  Ратуша
	CheckAndAddBuilding(pi, FourCC('h05Y'), 15, 4)	--  Дополнительные фермы
	CheckAndAddBuilding(pi, FourCC('h05Z'), 15, 4)	--  Казарма
	CheckAndAddBuilding(pi, FourCC('h063'), 25, 1)	--  Башня
	CheckAndAddBuilding(pi, FourCC('h062'), 5, 2)	--  Лесопилка
	CheckAndAddBuilding(pi, FourCC('h060'), 6, 2)	--  Кузница
	CheckAndAddBuilding(pi, FourCC('h05X'), 3, 5)	--  Алтарь
	
	--  Проверяем условия для Мастерской и Храма
	if (AiData[pi][FourCC('h05V')] or 0) + (AiData[pi][FourCC('h05W')] or 0) >= 1 then
		CheckAndAddBuilding(pi, FourCC('h064'), 7, 8)	--  Мастерская
		CheckAndAddBuilding(pi, FourCC('h061'), 15, 8)	--  Храм
	end
	
	--  Церковь
	if (AiData[pi][FourCC('h05W')] or 0) >= 1 and (AiData[pi][FourCC('h068')] or 0) < 15 then
		AddBuilding(FourCC('h068'), 10)
	end
	
	--  Выбираем случайный вариант из массива
	i = GetRandomInt(1, tArray[0])
	return tArray[i]
end
-- ***************************************************************************
-- *  BuildingsScarletOrden
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function PereborBuildings_ScarletOrden(id, pi, u)
	local b = 0
	local i = 0
	local a = {}
	
	if id == FourCC('h05Z') then	-- Казармы
		
		a[0] = 1	-- Кол-во вариантов со старта
		a[1] = FourCC('h03B')	--  1 Пехотинец
		
		--  Доп. варианты при условиях
		
		--  2 Лучник
		if (AiData[pi][FourCC('h060')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('n007')
				
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  3 Тяж Мечник
		if (AiData[pi][FourCC('h05V')] or 0) + (AiData[pi][FourCC('h05W')] or 0) >= 1 then
			i = 4	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h039')
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  4 Всадник
		if (AiData[pi][FourCC('h05W')] or 0) >= 1 then
			i = 6	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h066')
				b = b + 1
				if b >= i then break end
			end
		end
		i = GetRandomInt(1, a[0])
		IssueImmediateOrderById(u, a[i])
		
		
		--  Ратуша
	elseif id == FourCC('h05U') then
		
		
		udg_LocalInteger3 = GetRandomInt(1, 3)
		if udg_LocalInteger3 == 1 and (AiData[pi][FourCC('h014')] or 0) < 20 then
			IssueImmediateOrderById(u, FourCC('h014'))
			
		elseif udg_LocalInteger3 == 2 and (AiData[pi][FourCC('h03C')] or 0) < 15 then
			IssueImmediateOrderById(u, FourCC('h03C'))
			
		elseif udg_LocalInteger3 == 3 and (AiData[pi][FourCC('h03A')] or 0) < 15 then
			IssueImmediateOrderById(u, FourCC('h03A'))
		else
		end
		
		--  Мастеская
	elseif id == FourCC('h064') then
		IssueImmediateOrderById(u, FourCC('o00I'))
		
		
	elseif id == FourCC('h061') then
		udg_LocalInteger3 = GetRandomInt(1, 2)
		if udg_LocalInteger3 == 1 then
			IssueImmediateOrderById(u, FourCC('h067'))
		elseif udg_LocalInteger3 == 2 then
			IssueImmediateOrderById(u, FourCC('n008'))
		end
		
		--  Алтарь
	elseif id == FourCC('h05X') then
		udg_LocalInteger3 = GetRandomInt(1, 3)
		if udg_LocalInteger3 == 1 then
			IssueImmediateOrderById(u, FourCC('H06C'))
		end
		if udg_LocalInteger3 == 2 then
			IssueImmediateOrderById(u, FourCC('H03H'))
		end
		if udg_LocalInteger3 == 3 then
			IssueImmediateOrderById(u, FourCC('H06B'))
		end
		--  Церковь
	elseif id == FourCC('h068') then
		
		a[0] = 1	-- Кол-во вариантов со старта
		a[1] = 0	--  Никто
		
		--  Доп. варианты при условиях
		
		--  1 Паладин
		if (AiData[pi][FourCC('R040')] or false) and (AiData[pi][FourCC('h05W')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h03F')
				
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  3 Берсерк
		if (AiData[pi][FourCC('R040')] or false) and (AiData[pi][FourCC('h05W')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h03D')
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  3 Инквизитор
		if (AiData[pi][FourCC('R03Z')] or false) and (AiData[pi][FourCC('h05W')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h03I')
				
				b = b + 1
				if b >= i then break end
			end
		end
		
		--  4 Гладиатор
		if (AiData[pi][FourCC('R03Z')] or false) and (AiData[pi][FourCC('h05W')] or 0) >= 1 then
			i = 1	-- мошь выбора
			b = 1
			
			while true do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('h03G')
				b = b + 1
				if b >= i then break end
			end
		end
		
		i = GetRandomInt(1, a[0])
		IssueImmediateOrderById(u, a[i])
		
	end
	
	
end
-- ***************************************************************************
-- *  UpgradeScarlet
---@param pi integer
---@param id integer
---@return nothing
function UpgradeScarlet(pi, id)
	if id == FourCC('h04B') then
		NumberRem(pi, FourCC('h04C'))
	elseif id == FourCC('h05A') then
		NumberRem(pi, FourCC('h04B'))
	end
end
-- ***************************************************************************
-- *  GetLvlScarlet
---@param u unit
---@return nothing
function GetLvlScarlet(u)
	--  Герои
	-- Герой маг
	if GetUnitTypeId(u) == FourCC('H06C') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A09M'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A09K'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A09L'))
		else
			SelectHeroSkill(u, FourCC('A09N'))
		end
		
		
		
		
		-- Герой Капитан
	elseif GetUnitTypeId(u) == FourCC('H06B') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A09J'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A09F'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A09G'))
		else
			SelectHeroSkill(u, FourCC('A09I'))
		end
		
		
		
		-- Герой Паладин
	elseif GetUnitTypeId(u) == FourCC('H03H') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A09E'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A097'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A09C'))
		else
			SelectHeroSkill(u, FourCC('A09D'))
		end
	end
end
-- ***************************************************************************
-- *  StartGoblins
---@param pi integer
---@return nothing
function startGoblins(pi)
	-- Старт юниты
	CreateNUnitsAtLoc(8, FourCC('n00V'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
	CreateNUnitsAtLoc(1, FourCC('h070'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
	GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())

	AiData[pi][FourCC('n00V')] = 8
	AiData[pi][FourCC('h070')] = 1
	SetPlayerName(Player(pi), "Картель (" .. I2S(pi + 1) .. ")")
	AiData[pi][StringHash("Race")] = "GB"
	TriggerExecute(gg_trg_GoblinsOn)
	TriggerExecute(gg_trg_StartG)
	
	AiRace[pi] = "Goblins"
	ProbeLogWrite("[AI] startGoblins pi=" .. tostring(pi) .. " workers=8n00V building=1h070")
end
-- ***************************************************************************
-- *  JoinGoblins
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_Goblins(id, pi, u)
	local i
	if id == FourCC('n00V') then
		GroupAddUnit(udg_Ai_builders[pi], u)
	elseif id == FourCC('h06W') or id == FourCC('h0DM') or id == FourCC('h06V') or id == FourCC('h06X') then	-- Гоблины then
		GroupAddUnit(udg_Ai_navy[pi], u)
		NumberAdd(pi, StringHash("NumberN"))
	elseif aiUnitJoinsCapitalGuard(u, pi) then
	else
		aiUnitJoinsArmy(u, pi)
	end
	
	
	-- Герои
	-- Герой маг
	if id == FourCC('H06C') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A09K'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A09L'))
		else
			SelectHeroSkill(u, FourCC('A09N'))
		end
		
		
		-- Герой Капитан
	elseif id == FourCC('H06B') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A09G'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A09F'))
		else
			SelectHeroSkill(u, FourCC('A09I'))
		end
		
		
		-- Герой Паладин
	elseif id == FourCC('H03H') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A097'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A09C'))
		else
			SelectHeroSkill(u, FourCC('A09D'))
		end
		
		
		-- Флот 
	elseif id == FourCC('h00Z') then
		IssueImmediateOrder(u, "nagabuild")
		IssueImmediateOrder(u, "spellbook")
		i = GetRandomInt(1, 3)
		if i == 1 then
			IssueImmediateOrder(u, "nagabuild")
		elseif i == 2 then
			IssueImmediateOrder(u, "mounthippogryph")
		else
			IssueImmediateOrder(u, "monsoon")
		end
		
	end
	
	
end
-- ***************************************************************************
-- *  AttackerGoblins
---@param id integer
---@param u unit
---@param target unit
---@param p player
---@return nothing
function Attacker_Goblins(id, u, target, p)
	local i
	local x = GetUnitX(target)
	local y = GetUnitY(target)
	local x2
	local y2
	
	--  Спец
	if id == FourCC('H0BD') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			IssuePointOrder(u, "silence", x, y)
		elseif i == 2 then
			IssuePointOrder(u, "clusterrockets", x, y)
		elseif i == 3 then
			IssuePointOrder(u, "blizzard", x, y)
		end
		
		-- /Если герой алх
	elseif id == FourCC('Galh') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			IssueTargetOrder(u, "transmute", target)
		elseif i == 2 then
			IssueTargetOrder(u, "acidbomb", target)
		elseif i == 3 then
			IssueImmediateOrder(u, "chemicalrage")
		elseif i == 4 then
			IssuePointOrder(u, "healingspray", GetUnitX(u), GetUnitY(u))
		end
		
		
		-- /Если герой механик
	elseif id == FourCC('Gmex') then
		i = GetRandomInt(1, 5)
		if i == 1 then
			IssuePointOrder(u, "summonfactory", x, y)
		elseif i == 2 then
			IssuePointOrder(u, "clusterrockets", x, y)
		elseif i == 3 then
			IssueImmediateOrder(u, "robogoblin")
		end
		
		--  ------ Юниты 
		
		-- / рекрут
	elseif id == FourCC('h06K') then
		i = GetRandomInt(1, 4)
		if i == 1 then
			IssuePointOrder(u, "flamestrike", x, y)
		end
		-- / Арта
	elseif id == FourCC('h06Y') or id == FourCC('h06Z') then
		if Random(1, 4) then
			IssueImmediateOrder(u, "bearform")
		elseif Random(1, 4) then
			IssueImmediateOrder(u, "unbearform")
		end
		-- / СуперБоец
	elseif id == FourCC('h06P') then
		i = GetRandomInt(1, 6)
		if i == 1 then
			IssueImmediateOrder(u, "berserk")
		elseif i == 2 and DistanceBetweenUnitsXY(x, y, target) < 280 then
			IssuePointOrder(u, "dispel", x, y)
		elseif i == 3 then
			IssuePointOrder(u, "ward", x, y)
		end
	end
	
	-- Машины c ускорением
	if GetUnitAbilityLevel(u, FourCC('A0BL')) > 0 and Random(1, 4) then
		IssueImmediateOrder(u, "berserk")
	end
end
-- ***************************************************************************
-- *  AttackedGoblins
---@param u unit
---@return nothing
function AttackedGoblins(u)
	
end
-- ***************************************************************************
-- *  StrategGoblins
---@param id integer
---@return nothing
function Strateg_Goblins_EC(id)
	-- Это ферма
	if id == FourCC('h077') then
		udg_LocalInteger3 = udg_LocalInteger3 + 1
		-- Это Т1
	elseif id == FourCC('h070') then
		udg_LocalInteger3 = udg_LocalInteger3 + 4
	end
end
---@param i integer
---@param pi integer
---@param p player
---@return nothing
function Strateg_Goblins(i, pi, p)
	
	if Grades[pi] < 150 then
		if i > 17 then
			
			--  Лаборатория
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04P'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04E'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04F'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04G'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04H'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04I'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04J'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04K'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04L'), 6)
			MakeGradeCheckCap(p, FourCC('h076'), FourCC('R04M'), 6)
			
			--  Бюро
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R056'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R07A'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R05X'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R05Y'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R04N'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R04Q'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R04R'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R053'), 6)
			MakeGradeCheckCap(p, FourCC('h079'), FourCC('R05W'), 6)
			
			--  База
			MakeGradeCheckCap(p, FourCC('h070'), FourCC('R0D4'), 6)
			
			-- Покупка предмета
			if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
				TryBuy(p, i)
			end
		end
		
	else
		warRace(Grades[pi], p)
		
	end
	
	-- Спавн мага тп
	if i > 60 and (AiData[pi][FourCC('h07A')] or 0) < i / 35 then
		MakeMageTp(pi)
	end
	
end
-- ***************************************************************************
-- *  BuildGoblins
---@param pi integer
---@return integer
function ChooseBuildings_Goblins(pi)
	--  Инициализируем массив и добавляем стартовый вариант
	tArray[0] = 1
	tArray[1] = FourCC('h077')	--  1 Банк
	
	--  Добавляем здания по условиям
	CheckAndAddBuilding(pi, FourCC('h070'), 4, 5)	--  Штаб
	CheckAndAddBuilding(pi, FourCC('h077'), 20, 3)	--  Доп. банки на старте
	CheckAndAddBuilding(pi, FourCC('h073'), 18, 7)	--  Казарма
	CheckAndAddBuilding(pi, FourCC('h07S'), 30, 1)	--  Турель
	CheckAndAddBuilding(pi, FourCC('h079'), 5, 3)	--  Бюро
	CheckAndAddBuilding(pi, FourCC('h076'), 18, 4)	--  Ларабаратория
	CheckAndAddBuilding(pi, FourCC('o016'), 3, 8)	--  Алтарь
	if Grades[pi] > 8 then	-- R04P,R04E,R04F,R04G,R04H,R04I,R04J,R04K,R04L,R04M
		CheckAndAddBuilding(pi, FourCC('h074'), 15, 2)	--  Завод
		CheckAndAddBuilding(pi, FourCC('h075'), 15, 2)	--  Фабрика
	end
	
	
	--  Выбираем случайный вариант из массива
	gInt = GetRandomInt(1, tArray[0])
	return tArray[gInt]
end
-- ***************************************************************************
-- *  BuildingsGoblins
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function PereborBuildings_Goblins(id, pi, u)
	tArray[0] = 0	--  Очистка массива перед выбором
	--  Казармы h06K h06O,h06Q,h06L,h06N,,h078,h06M
	if id == FourCC('h073') then
		if Random(1, 6) then
			IssueNeutralImmediateOrderById(Player(pi), u, FourCC('h07R'))
		else
			
			--  Добавление юнитов
			AddUnit(FourCC('h06K'), 2)	--  Рекрут
			if Grades[pi] > 8 then
				AddUnit(FourCC('h060'), 1)	--  
				AddUnit(FourCC('h06Q'), 3)	--  
				AddUnit(FourCC('h06L'), 3)	--  
				AddUnit(FourCC('h06N'), 3)	--  
				AddUnit(FourCC('h078'), 3)	--  
				AddUnit(FourCC('h06M'), 3)	--  
			end
			
		end
		
		--  Штаб
	elseif id == FourCC('h070') then
		CheckAndAddUnit(pi, FourCC('n00V'), 25, 2)
		--  Завод
	elseif id == FourCC('h074') then	--  h06S,h06U,h06Y,h06R,h06T
		AddUnit(FourCC('h06S'), 2)	--  Базовый юнит завода
		AddUnit(FourCC('h06U'), 2)	--  
		AddUnit(FourCC('h06Y'), 4)	--  
		AddUnit(FourCC('h06R'), 3)	--  
		AddUnit(FourCC('h06T'), 3)	--  
		
		--  Фабрика o00W,o00Y,o00X,h06P
	elseif id == FourCC('h075') then
		AddUnit(FourCC('o00W'), 2)	--  
		AddUnit(FourCC('o00Y'), 2)	--  
		AddUnit(FourCC('o00X'), 3)	--  
		AddUnit(FourCC('h06P'), 3)	--  
		--  Алтарь  H0BD,Galh,Gmex
	elseif id == FourCC('o016') then
		CheckAndAddUnit(pi, FourCC('H0BD'), 1, 1)
		CheckAndAddUnit(pi, FourCC('Galh'), 1, 1)
		CheckAndAddUnit(pi, FourCC('Gmex'), 1, 1)
	end
	aiOrderUnit(u)
end
---@param u unit
---@param pi integer
---@return nothing
function aiNavalTrain_Goblins(u, pi)
	udg_LocalInteger3 = GetRandomInt(1, 5)
	
	if udg_LocalInteger3 == 1 then
		IssueImmediateOrderById(u, FourCC('h06X'))
	elseif udg_LocalInteger3 == 2 then
		IssueImmediateOrderById(u, FourCC('h06U'))
	elseif udg_LocalInteger3 == 3 then
		IssueImmediateOrderById(u, FourCC('h06V'))
	elseif udg_LocalInteger3 == 4 then
		IssueImmediateOrderById(u, FourCC('h06W'))
	elseif udg_LocalInteger3 == 5 and (AiData[pi][FourCC('h0OD')] or 0) < 1 then
		IssueImmediateOrderById(u, FourCC('h0OD'))
	end
end
-- ***************************************************************************
-- *  UpgradeGoblins
---@param pi integer
---@param id integer
---@return nothing
function UpgradeGoblins(pi, id)
	
end
-- ***************************************************************************
-- *  GetLvlGoblins
---@param u unit
---@return nothing
function GetLvlGoblins(u)
	--  Герои
	-- Снайпер
	if GetUnitTypeId(u) == FourCC('H0BD') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A0D7'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A0D8'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('AEar'))
		else
			SelectHeroSkill(u, FourCC('A0D5'))
		end
		-- Galh
	elseif GetUnitTypeId(u) == FourCC('Galh') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('ANtm'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('ANhs'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('ANab'))
		else
			SelectHeroSkill(u, FourCC('ANcr'))
		end
		
		-- Gmex
	elseif GetUnitTypeId(u) == FourCC('Gmex') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('ANrg'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('ANsy'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('ANcs'))
		else
			SelectHeroSkill(u, FourCC('ANeg'))
		end
	end
end
-- ***************************************************************************
-- *  StartHorde2
---@param pi integer
---@return nothing
function startHorde(pi)
	-- Старт юниты
	CreateNUnitsAtLoc(8, FourCC('opeo'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
	CreateNUnitsAtLoc(1, FourCC('ogre'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
	GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())

	AiData[pi][FourCC('opeo')] = 8
	AiData[pi][FourCC('ogre')] = 1
	SetPlayerName(Player(pi), "Орда (" .. I2S(pi + 1) .. ")")
	AiData[pi][StringHash("Race")] = "NG"
	TriggerExecute(gg_trg_StartHorde)
	TriggerExecute(gg_trg_HordeOn)
	
	AiRace[pi] = "Horde"
	ProbeLogWrite("[AI] startHorde pi=" .. tostring(pi) .. " workers=8opeo building=1ogre")
end
-- ***************************************************************************
-- *  JoinHorde
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_Horde(id, pi, u)
	local i
	if id == FourCC('opeo') then
		GroupAddUnit(udg_Ai_builders[pi], u)
	elseif GetUnitAbilityLevel(u, FourCC('A00A')) > 0 then
		GroupAddUnit(udg_Ai_navy[pi], u)
		NumberAdd(pi, StringHash("NumberN"))
	elseif aiUnitJoinsCapitalGuard(u, pi) then
	else
		aiUnitJoinsArmy(u, pi)
	end
	
	
	-- Герои Obla,Ofar,Otch
	--   A12F,AOwk,AOcr,AOww
	if id == FourCC('obla') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A12F'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A12F'))
		else
			SelectHeroSkill(u, FourCC('AOcr'))
		end
		
		
		--  far AOfs,AOsf,AOcl,A12E
	elseif id == FourCC('Ofar') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('AOfs'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('AOsf'))
		else
			SelectHeroSkill(u, FourCC('AOsf'))
		end
		
		
		--  A026,AOr2,AOre,AOw2
	elseif id == FourCC('Otch') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A026'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A026'))
		else
			SelectHeroSkill(u, FourCC('AOw2'))
		end
		
	end
	
	
end
-- ***************************************************************************
-- *  AttackeHorde
---@param id integer
---@param u unit
---@param target unit
---@param p player
---@return nothing
function Attacker_Horde(id, u, target, p)
	local x = GetUnitX(target)
	local y = GetUnitY(target)
	local x2 = GetUnitY(u)
	local y2 = GetUnitY(u)
	
	-- Obla,Ofar,Otch
	if IsUnitType(u, UNIT_TYPE_HERO) then
		--  blade master A12F,AOwk,AOcr,AOww
		if id == FourCC('obla') then
			gInt = GetRandomInt(1, 5)
			if gInt <= 2 then
				IssueImmediateOrder(u, "windwalk")
			elseif gInt == 3 then
				IssueImmediateOrder(u, "roar")
			elseif gInt == 4 then
				IssueImmediateOrder(u, "whirlwind")
			end
			
			-- / farseer
		elseif id == FourCC('Ofar') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
				IssueTargetOrder(u, "chainlightning", target)
			elseif gInt == 2 then
				IssuePointOrder(u, "farsight", x + GetRandomReal(-5000, 5000), y + GetRandomReal(-5000, 5000))
			elseif gInt == 3 then
				IssueImmediateOrder(u, "spiritwolf")
			elseif gInt == 4 then
				IssuePointOrder(u, "monsoon", x, y)
			end
			
			
			-- / Tauren or general
		elseif id == FourCC('Otch') or id == FourCC('O02Z') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
				IssueImmediateOrder(u, "stomp")
			elseif gInt == 3 then
				IssuePointOrder(u, "carrionswarm", x, y)
			end
		end
	else
		--  ------ Юниты 
		
		-- / Shaman
		if id == FourCC('o01J') then
			gInt = GetRandomInt(1, 5)
			if gInt == 1 then
				IssueTargetOrder(u, "lightningshield", target)
			elseif gInt == 2 then
				IssuePointOrder(u, "dispel", x, y)
			elseif gInt == 3 then
				IssueTargetOrder(u, "purge", target)
			end	-- + спелл без приказа
			-- / dark sham
		elseif id == FourCC('o01V') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
				IssueTargetOrder(u, "soulburn", target)
			elseif gInt == 2 then
				IssueImmediateOrder(u, "waterelemental")
			elseif gInt == 3 then
				IssuePointOrder(u, "monsoon", x, y)
			end
			-- / Blood elf
		elseif id == FourCC('o023') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
			elseif gInt == 2 then
				IssuePointOrder(u, "flamestrike", x, y)
			elseif gInt == 3 then
				IssuePointOrder(u, "stampede", x, y)
			end
			
			-- / Troll or Dark mage
		elseif id == FourCC('o024') or id == FourCC('o02L') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
				IssuePointOrder(u, "evileye", x, y)
			elseif gInt == 2 then
				IssuePointOrder(u, "stasistrap", x, y)
			elseif gInt == 3 then
				IssuePointOrder(u, "healingward", x2, y2)
			end
		end
	end
	
	
end
-- ***************************************************************************
-- *  AttackedHorde
---@param u unit
---@return nothing
function AttackedHorde(u)
	
end
-- ***************************************************************************
-- *  StrategHorde
---@param id integer
---@return nothing
function Strateg_Horde_EC(id)
	-- Это ферма
	if id == FourCC('nnfm') then
		udg_LocalInteger3 = udg_LocalInteger3 + 1
		-- Это Т1
	elseif id == FourCC('ogre') then
		udg_LocalInteger3 = udg_LocalInteger3 + 4
		-- Это Т2
	elseif id == FourCC('ostr') then
		udg_LocalInteger3 = udg_LocalInteger3 + 6
		-- Это Т3
	elseif id == FourCC('ofrt') then
		udg_LocalInteger3 = udg_LocalInteger3 + 8
	end
end
---@param i integer
---@param pi integer
---@param p player
---@return nothing
function Strateg_Horde(i, pi, p)
	if Grades[pi] < 150 then
		
		--  nnsg (второй набор)
		if i < 50 then
			MakeGradeCheckCap(p, FourCC('nntt'), FourCC('R0FE'), 1)
			MakeGradeCheckCap(p, FourCC('nntt'), FourCC('R0FF'), 1)
		end
		
		if i > 17 then
			
			
			
			MakeGradeCheckCap(p, FourCC('ogre'), FourCC('Ropg'), 1)
			--  Ofor
			MakeGradeCheckCap(p, FourCC('ofor'), FourCC('R0G5'), 6)
			MakeGradeCheckCap(p, FourCC('ofor'), FourCC('R0E6'), 6)
			MakeGradeCheckCap(p, FourCC('ofor'), FourCC('Rome'), 6)
			MakeGradeCheckCap(p, FourCC('ofor'), FourCC('Roar'), 6)
			MakeGradeCheckCap(p, FourCC('ofor'), FourCC('Rora'), 6)
			MakeGradeCheckCap(p, FourCC('ofor'), FourCC('Rosp'), 3)
			MakeGradeCheckCap(p, FourCC('ofor'), FourCC('Rorb'), 3)
			
			
			--  пех даль тех
			MakeGradeCheckCap(p, FourCC('obar'), FourCC('R0EC'), 3)
			MakeGradeCheckCap(p, FourCC('obea'), FourCC('R0ED'), 3)
			MakeGradeCheckCap(p, FourCC('otto'), FourCC('R0EF'), 3)
			
			--  маги  Rost,Rowt,Rowd
			MakeGradeCheckCap(p, FourCC('osld'), FourCC('Rost'), 3)
			MakeGradeCheckCap(p, FourCC('osld'), FourCC('Rost'), 3)
			MakeGradeCheckCap(p, FourCC('osld'), FourCC('Rowd'), 3)
			
			-- Покупка предмета
			if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
				TryBuy(p, i)
			end
			
			strategFleetGrades(i, p, FourCC('h0HO'))
		end
		
		--  Посольство
		gInt = GetRandomInt(1, 5)
		if gInt == 1 then
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0F3'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0F4'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0EH'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0EI'), 1)
		elseif gInt == 2 then
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0EE'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0EA'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0E9'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0E5'), 1)
		elseif gInt == 3 then
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0E4'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0E3'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0E1'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0E0'), 1)
		elseif gInt == 4 then
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0DZ'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0D2'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0D3'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0D1'), 1)
		elseif gInt == 5 then
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0DX'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0DY'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0DZ'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0DW'), 1)
			MakeGradeCheckCap(p, FourCC('ovln'), FourCC('R0KO'), 1)
		end
		
		
	else
		warRace(Grades[pi], p)
	end
	-- Делай т2
	if i > 25 and (AiData[pi][FourCC('ostr')] or 0) < 3 then
		BuildT(p, FourCC('ogre'), FourCC('ostr'))
	end
	
	-- Делай т3
	if i > 55 and (AiData[pi][FourCC('ofrt')] or 0) < 3 then
		BuildT(p, FourCC('ostr'), FourCC('ofrt'))
	end
	
	-- Спавн мага тп
	if i > 60 and (AiData[pi][FourCC('h07A')] or 0) < i / 35 then
		MakeMageTp(pi)
	end
	
	
end
-- ***************************************************************************
-- *  BuildHorde
---@param pi integer
---@return integer
function ChooseBuildings_Horde(pi)
	--  Инициализируем массив и добавляем стартовый вариант
	tArray[0] = 1
	tArray[1] = FourCC('otrb')	--  1 землянка
	
	--  h0HO,ogre obar  otrb    ,,,,,oalt,,osld,otto,owtw,ovln
	CheckAndAddBuilding(pi, FourCC('ogre'), 3, 5)	--  T1
	CheckAndAddBuilding(pi, FourCC('otrb'), 20, 3)	--  Доп. землянки на старте
	CheckAndAddBuilding(pi, FourCC('obar'), 3, 7)	--  Доп казармы на старте
	CheckAndAddBuilding(pi, FourCC('obar'), 18, 3)	--  Казарма
	CheckAndAddBuilding(pi, FourCC('obea'), 18, 2)	--  Стрельбище
	CheckAndAddBuilding(pi, FourCC('owtw'), 30, 1)	--  Tower
	CheckAndAddBuilding(pi, FourCC('ofor'), 5, 3)	--  Лесопилка
	CheckAndAddBuilding(pi, FourCC('oalt'), 3, 6)	--  Алтарь
	if (AiData[pi][FourCC('ostr')] or 0) + (AiData[pi][FourCC('ofrt')] or 0) > 0 then	--  (pi,FourCC('ostr')) or aiHasUnit(pi,FourCC('ofrt')) then
		CheckAndAddBuilding(pi, FourCC('osld'), 15, 10)	--  Обитель духов
		CheckAndAddBuilding(pi, FourCC('otto'), 15, 10)	--  Мастерская
	end
	CheckAndAddBuilding(pi, FourCC('osld'), 15, 1)	--  Обитель духов
	CheckAndAddBuilding(pi, FourCC('otto'), 15, 1)	--  Мастерская
	
	
	CheckAndAddBuilding(pi, FourCC('ovln'), 1, 6)	--  Посольство
	--  Выбираем случайный вариант из массива
	gInt = GetRandomInt(1, tArray[0])
	return tArray[gInt]
end
-- ***************************************************************************
-- *  BuildingsHorde
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function PereborBuildings_Horde(id, pi, u)
	local HasMage = GetPlayerTechResearched(Player(pi), FourCC('R0E9'), true)
	local IronHorde = GetPlayerTechResearched(Player(pi), FourCC('R0EA'), true)
	
	--  h0HO,ogre,otrb,orbr,obar,ofor,oalt,obea,osld,otto,owtw,ovln
	tArray[0] = 0
	--  Barracks ogru,o029,o01N,orai,otau
	if id == FourCC('obar') then
		
		if IronHorde then
			AddUnit(FourCC('o01N'), 2)	--  T2 Iron
		else
			AddUnit(FourCC('ogru'), 2)	--  T1
			if ((AiData[(pi)][(FourCC('ostr'))] or 0) > 0) or ((AiData[(pi)][(FourCC('ofrt'))] or 0) > 0) then	--  INLINED!!
				AddUnit(FourCC('o029'), 3)	--  T2
			end
		end
		
		if ((AiData[(pi)][(FourCC('ofrt'))] or 0) > 0) then	--  INLINED!!
			AddUnit(FourCC('orai'), 5)	--  
			AddUnit(FourCC('otau'), 5)	--  
		end
		--  strel o01P,okod,o02B,ohun
	elseif id == FourCC('obea') then
		
		if IronHorde then
			AddUnit(FourCC('o02B'), 2)	--  T2 Iron
		else
			AddUnit(FourCC('ohun'), 2)	--  T1
			if ((AiData[(pi)][(FourCC('ostr'))] or 0) > 0) or ((AiData[(pi)][(FourCC('ofrt'))] or 0) > 0) then	--  INLINED!!
				AddUnit(FourCC('o01P'), 3)	--  T2
			end
		end
		
		if ((AiData[(pi)][(FourCC('ofrt'))] or 0) > 0) then	--  INLINED!!
			AddUnit(FourCC('okod'), 5)	--  
		end
		
		--  Тиры
	elseif id == FourCC('ogre') or id == FourCC('ostr') or id == FourCC('ofrt') then
		if (AiData[pi][FourCC('opeo')] or 0) < 25 then
			IssueImmediateOrderById(u, FourCC('opeo'))
		end
		--  Обитель духов o01W,oshm,odoc
	elseif id == FourCC('osld') then
		AddUnit(FourCC('oshm'), 4)	--  
		AddUnit(FourCC('o01W'), 2)	--  M damage
		AddUnit(FourCC('oshm'), 4)	--  
		--  Мастерская h0CY,ocat,o022
	elseif id == FourCC('otto') then
		
		AddUnit(FourCC('ocat'), 2)
		AddUnit(FourCC('o022'), 1)
		if IronHorde then
			AddUnit(FourCC('h0CY'), 2)	--  iron star
		end
		
		
		--  Алтарь oalt Obla,Ofar,Otch
	elseif id == FourCC('oalt') then
		CheckAndAddUnit(pi, FourCC('Ofar'), 1, 1)
		CheckAndAddUnit(pi, FourCC('Obla'), 1, 1)
		CheckAndAddUnit(pi, FourCC('Otch'), 1, 1)
	end
	
	aiOrderUnit(u)
end
--   h0HO,h0D4,h0HN,h0HK
---@param u unit
---@param pi integer
---@return nothing
function aiNavalTrain_Horde(u, pi)
	udg_LocalInteger3 = GetRandomInt(1, 2)
	
	if udg_LocalInteger3 == 1 then
		IssueImmediateOrderById(u, FourCC('h0HN'))
	elseif udg_LocalInteger3 == 2 then
		IssueImmediateOrderById(u, FourCC('h0HK'))
	end
end
-- ***************************************************************************
-- *  UpgradeHorde
---@param pi integer
---@param id integer
---@return nothing
function UpgradeHorde(pi, id)
	if id == FourCC('ostr') then
		NumberRem(pi, FourCC('ogre'))
	elseif id == FourCC('ofrt') then
		NumberRem(pi, FourCC('ostr'))
	end
end
-- ***************************************************************************
-- *  GetLvlHorde
---@param u unit
---@return nothing
function GetLvlHorde(u)
	--  Герои Obla,Ofar,Otch
	--  A12F,AOwk,AOcr,AOww
	if GetUnitTypeId(u) == FourCC('Obla') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('AOww'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A12F'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A12F'))
		elseif gInt == 3 then
			SelectHeroSkill(u, FourCC('AOcr'))
		else
			-- call SelectHeroSkill( u, 'A0D5' )
		end
		-- AOfs,AOsf,AOcl,A12E
	elseif GetUnitTypeId(u) == FourCC('Ofar') then
		gInt = GetRandomInt(0, 3)
		if gInt == 0 then
			SelectHeroSkill(u, FourCC('A12E'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('AOcl'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('AOsf'))
		else
			SelectHeroSkill(u, FourCC('AOfs'))
		end
		
		--  A026,AOr2,AOre,AOw2
	elseif GetUnitTypeId(u) == FourCC('Otch') or GetUnitTypeId(u) == FourCC('O02Z') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('AOre'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('AOre'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('AOr2'))
		else
			SelectHeroSkill(u, FourCC('A026'))
		end
	end
end
-- ***************************************************************************
-- *  StartNaga
---@param pi integer
---@return nothing
function startNaga(pi)
	-- Старт юниты
	CreateNUnitsAtLoc(8, FourCC('nmpe'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
	CreateNUnitsAtLoc(1, FourCC('nntt'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
	GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())

	AiData[pi][FourCC('nmpe')] = 8
	AiData[pi][FourCC('nntt')] = 1
	SetPlayerName(Player(pi), "Стая (" .. I2S(pi + 1) .. ")")
	AiData[pi][StringHash("Race")] = "NG"
	TriggerExecute(gg_trg_NagaStart)
	
	AiRace[pi] = "Naga"
	ProbeLogWrite("[AI] startNaga pi=" .. tostring(pi) .. " workers=8nmpe building=1nntt")
end
-- ***************************************************************************
-- *  JoinNaga
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_Naga(id, pi, u)
	local i
	if id == FourCC('nmpe') then
		GroupAddUnit(udg_Ai_builders[pi], u)
	elseif id == FourCC('n079') then
		GroupAddUnit(udg_Ai_navy[pi], u)
		NumberAdd(pi, StringHash("NumberN"))
	elseif aiUnitJoinsCapitalGuard(u, pi) then
	else
		aiUnitJoinsArmy(u, pi)
	end
	
	
	-- Герои N07A,H0JU,H0JV
	-- Маг мурлок AEtq,AHbn,AHab,ANrf
	if id == FourCC('N07A') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('AHbn'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('AHab'))
		else
			SelectHeroSkill(u, FourCC('AHab'))
		end
		
		
		-- Нага Охотница A13D  A13C,AEbl,A13A,
	elseif id == FourCC('H0JV') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A13C'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A13C'))
		else
			SelectHeroSkill(u, FourCC('A13A'))
		end
		
		
		-- Герой нага A14G-   A14I,A14F,,A14H
	elseif id == FourCC('H0JU') then
		i = GetRandomInt(1, 3)
		if i == 1 then
			SelectHeroSkill(u, FourCC('A14I'))
		elseif i == 2 then
			SelectHeroSkill(u, FourCC('A14I'))
		else
			SelectHeroSkill(u, FourCC('A14H'))
		end
		
	end
	
	
end
-- ***************************************************************************
-- *  AttackerNaga
---@param id integer
---@param u unit
---@param target unit
---@param p player
---@return nothing
function Attacker_Naga(id, u, target, p)
	local x = GetUnitX(target)
	local y = GetUnitY(target)
	local x2 = GetUnitY(u)
	local y2 = GetUnitY(u)
	
	-- Наги в воде c ускорением
	if  not IsTerrainPathable(x2, y2, PATHING_TYPE_WALKABILITY) and GetUnitAbilityLevel(u, FourCC('S00E')) == 0 then
		IssueImmediateOrder(u, "blight")
		return 
	end
	
	
	if IsUnitType(u, UNIT_TYPE_HERO) then
		--  Охотница
		if id == FourCC('H0JV') then
			gInt = GetRandomInt(1, 5)
			if gInt <= 2 then
				IssueImmediateOrder(u, "berserk")
			elseif gInt == 3 then
				IssuePointOrder(u, "clusterrockets", x, y)
			elseif gInt == 4 then
				IssuePointOrder(u, "blink", x2 + GetRandomReal(-500, 500), y2 + GetRandomReal(-500, 500))
			end
			
			-- / Мурлок шам
		elseif id == FourCC('N07A') then
			gInt = GetRandomInt(1, 5)
			if gInt == 1 then
				IssueTargetOrder(u, "banish", target)
			elseif gInt == 2 then
				IssuePointOrder(u, "rainoffire", x, y)
			elseif gInt == 3 then
				IssueImmediateOrder(u, "tranquility")
			end
			
			
			-- / Нага воин или аналог мурлок
		elseif id == FourCC('H0JU') or id == FourCC('H0OZ') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
				IssueTargetOrder(u, "doom", target)
			elseif gInt == 2 then
				IssueTargetOrder(u, "frostnova", target)
			elseif gInt == 3 then
				IssueImmediateOrder(u, "stomp")
			end
		end
	else
		--  ------ Юниты 
		
		-- / Глубинница
		if id == FourCC('n051') then
			gInt = GetRandomInt(1, 4)
			if gInt == 1 then
				IssueImmediateOrder(u, "healon")
			elseif gInt == 2 then
				IssuePointOrder(u, "dispel", x, y)
			end	-- + спелл без приказа
			-- / Сирена
		elseif id == FourCC('nnsw') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
				IssueTargetOrder(u, "cyclone", target)
			elseif gInt == 2 then
				IssueImmediateOrder(u, "frostarmoron")
			elseif gInt == 3 then
				IssueImmediateOrder(u, "parasiteon")
			end
			-- / Нага гвардеец
		elseif id == FourCC('nnrg') then
			gInt = GetRandomInt(1, 6)
			if gInt == 1 then
				IssueTargetOrder(u, "thunderbolt", target)
			elseif gInt == 2 then
				IssuePointOrder(u, "carrionswarm", x, y)
			end
		end
	end
	
	
end
-- ***************************************************************************
-- *  AttackedNaga
---@param u unit
---@return nothing
function AttackedNaga(u)
	
end
-- ***************************************************************************
-- *  StrategNaga
---@param id integer
---@return nothing
function Strateg_Naga_EC(id)
	-- Это ферма
	if id == FourCC('nnfm') then
		udg_LocalInteger3 = udg_LocalInteger3 + 1
		-- Это Т1
	elseif id == FourCC('nntt') then
		udg_LocalInteger3 = udg_LocalInteger3 + 4
		-- Это Т2
	elseif id == FourCC('h0JX') then
		udg_LocalInteger3 = udg_LocalInteger3 + 6
		-- Это Т3
	elseif id == FourCC('h0JY') then
		udg_LocalInteger3 = udg_LocalInteger3 + 8
	end
end
---@param i integer
---@param pi integer
---@param p player
---@return nothing
function Strateg_Naga(i, pi, p)
	if Grades[pi] < 150 then
		
		--  nnsg (второй набор)
		if i < 50 then
			MakeGradeCheckCap(p, FourCC('nntt'), FourCC('R0FE'), 1)
			MakeGradeCheckCap(p, FourCC('nntt'), FourCC('R0FF'), 1)
		end
		
		if i > 17 then
			
			--  h0JW
			MakeGradeCheckCap(p, FourCC('h0JW'), FourCC('R0FD'), 6)
			MakeGradeCheckCap(p, FourCC('h0JW'), FourCC('R0FH'), 6)
			MakeGradeCheckCap(p, FourCC('h0JW'), FourCC('Rnat'), 6)
			MakeGradeCheckCap(p, FourCC('h0JW'), FourCC('Rnam'), 6)
			MakeGradeCheckCap(p, FourCC('h0JW'), FourCC('Rnsb'), 6)
			
			--  nnsa (первый набор)
			MakeGradeCheckCap(p, FourCC('nnsa'), FourCC('Rnsw'), 6)
			MakeGradeCheckCap(p, FourCC('nnsa'), FourCC('Rnsi'), 6)
			
			--  nnsg (второй набор)
			MakeGradeCheckCap(p, FourCC('nnsg'), FourCC('R0FR'), 6)
			MakeGradeCheckCap(p, FourCC('nnsg'), FourCC('Rnen'), 6)
			
			-- Покупка предмета
			if GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
				TryBuy(p, i)
			end
		end
		
	else
		warRace(Grades[pi], p)
		
	end
	-- Делай т2
	if i > 25 and (AiData[pi][FourCC('h0JX')] or 0) < 3 then
		BuildT(p, FourCC('nntt'), FourCC('h0JX'))
	end
	
	-- Делай т3
	if i > 55 and (AiData[pi][FourCC('h0JY')] or 0) < 3 then
		BuildT(p, FourCC('h0JX'), FourCC('h0JY'))
	end
	
	-- Спавн мага тп
	if i > 60 and (AiData[pi][FourCC('h07A')] or 0) < i / 35 then
		MakeMageTp(pi)
	end
	
end
-- ***************************************************************************
-- *  BuildNaga
---@param pi integer
---@return integer
function ChooseBuildings_Naga(pi)
	--  Инициализируем массив и добавляем стартовый вариант
	tArray[0] = 1
	tArray[1] = FourCC('nnfm')	--  1 Риф
	
	
	--  Добавляем здания по условиям
	CheckAndAddBuilding(pi, FourCC('nntt'), 3, 5)	--  T1
	CheckAndAddBuilding(pi, FourCC('nnfm'), 20, 4)	--  Доп. рифы на старте
	CheckAndAddBuilding(pi, FourCC('nnsg'), 18, 6)	--  Казарма
	CheckAndAddBuilding(pi, FourCC('nntg'), 30, 1)	--  Приливной страж
	CheckAndAddBuilding(pi, FourCC('h0JW'), 5, 2)	--  Морская дробильня грейды
	CheckAndAddBuilding(pi, FourCC('nnad'), 3, 6)	--  Алтарь
	CheckAndAddBuilding(pi, FourCC('nnsa'), 15, 2)	--  Святилеще Азары
	CheckAndAddBuilding(pi, FourCC('n055'), 15, 3)	--  Морские врата
	
	--  Выбираем случайный вариант из массива
	gInt = GetRandomInt(1, tArray[0])
	return tArray[gInt]
end
-- ***************************************************************************
-- *  BuildingsNaga
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function PereborBuildings_Naga(id, pi, u)
	local MurlocPath = GetPlayerTechResearched(Player(pi), FourCC('R0FF'), true)
	
	tArray[0] = 0
	--  Нерестилище
	if id == FourCC('nnsg') then
		
		AddUnit(FourCC('n04Z'), 2)	--  Воин волн
		if ((AiData[(pi)][(FourCC('h0JW'))] or 0) > 0) then	--  INLINED!!
			AddUnit(FourCC('nsnp'), 2)	--  Варан
		end
		
		if ((AiData[(pi)][(FourCC('h0JX'))] or 0) > 0) then	--  INLINED!!
			AddUnit(FourCC('nhyc'), 1)	--  Черепаха
			if MurlocPath then
				AddUnit(FourCC('n052'), 3)	--  Доп. вариант для пути мурлоков
			else
				AddUnit(FourCC('nmyr'), 3)	--  Доп. вариант для пути наг
			end
		end
		
		--  Тиры
	elseif id == FourCC('nntt') or id == FourCC('h0JX') or id == FourCC('h0JY') then
		if (AiData[pi][FourCC('nmpe')] or 0) < 25 then
			IssueImmediateOrderById(u, FourCC('nmpe'))
		elseif Random(1, 2) then
			IssueImmediateOrderById(u, FourCC('nnmg'))
		end
		--  Святилище
	elseif id == FourCC('nnsa') then
		if ((AiData[(pi)][(FourCC('h0JX'))] or 0) > 0) then	--  INLINED!!
			if MurlocPath then
				AddUnit(FourCC('n053'), 6)	--  Маг
				AddUnit(FourCC('n054'), 6)	--  Шаман
			else
				AddUnit(FourCC('n051'), 1)	--  Глубинница 1
				AddUnit(FourCC('nnsw'), 4)	--  Сирена
			end
		end
		--  Морские врата
	elseif id == FourCC('n055') then
		
		if ((AiData[(pi)][(FourCC('h0JY'))] or 0) > 0) then	--  INLINED!!
			if MurlocPath then
				AddUnit(FourCC('n050'), 2)	--  Мурлок-мунтан
			else
				AddUnit(FourCC('nnrg'), 2)	--  Нага-гвардеец
			end
			AddUnit(FourCC('n056'), 1)	--  Гигант
		end
		AddUnit(FourCC('nwgs'), 1)	--  Коатль
		
		--  Алтарь
	elseif id == FourCC('nnad') then
		CheckAndAddUnit(pi, FourCC('N07A'), 1, 1)
		CheckAndAddUnit(pi, FourCC('H0JV'), 1, 1)
		if MurlocPath then
			CheckAndAddUnit(pi, FourCC('H0OZ'), 1, 1)
		else
			CheckAndAddUnit(pi, FourCC('H0JU'), 1, 1)
		end
	end
	
	aiOrderUnit(u)
end
---@param u unit
---@param pi integer
---@return nothing
function aiNavalTrain_Naga(u, pi)
	IssueImmediateOrderById(u, FourCC('n079'))
end
-- ***************************************************************************
-- *  UpgradeNaga
---@param pi integer
---@param id integer
---@return nothing
function UpgradeNaga(pi, id)
	if id == FourCC('h0JX') then
		NumberRem(pi, FourCC('nntt'))
	elseif id == FourCC('h0JY') then
		NumberRem(pi, FourCC('h0JX'))
	end
end
-- ***************************************************************************
-- *  GetLvlNaga
---@param u unit
---@return nothing
function GetLvlNaga(u)
	--  Герои N07A,H0JU,H0JV
	-- Охоттница A13C,A13A,A13D
	if GetUnitTypeId(u) == FourCC('H0JV') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A13C'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A13A'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('AEbl'))
		else
			-- call SelectHeroSkill( u, 'A0D5' )
		end
		-- Нага A14I,A14F,A14G,A14H
	elseif GetUnitTypeId(u) == FourCC('H0JU') then
		gInt = GetRandomInt(0, 3)
		if gInt == 0 then
			SelectHeroSkill(u, FourCC('A14I'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A14I'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A14G'))
		else
			SelectHeroSkill(u, FourCC('A14G'))
		end
		
		-- Мурлок A14I,A14F,A14G,A14H
	elseif GetUnitTypeId(u) == FourCC('N07A') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('ANrg'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('ANsy'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('ANcs'))
		else
			SelectHeroSkill(u, FourCC('ANeg'))
		end
	end
end
-- ***************************************************************************
-- *  JungleTrolls AI
-- Per-race AI for the Jungle Trolls (editor suffix "Тролли джунглей").
-- Two sub-branches selected per AI player: BlackSpear / Gurubashy.
-- ***************************************************************************
---@param pi integer
---@return nothing
function AiChooseJungleTrollsBranch(pi)
	local p = Player(pi)
	local blackSpear = ModuloInteger(pi, 2) == 0
	if blackSpear then
		SetPlayerTechMaxAllowedSwap(FourCC('o04P'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('O05L'), 1, p)
		SetPlayerAbilityAvailableBJ(false, FourCC('A1EP'), p)
		SetPlayerAbilityAvailableBJ(false, FourCC('A1EQ'), p)
		SetPlayerTechResearchedSwap(FourCC('R0IR'), 1, p)
		AiData[pi][StringHash("JTBranch")] = "BlackSpear"
	else
		SetPlayerTechMaxAllowedSwap(FourCC('o04N'), -1, p)
		SetPlayerTechMaxAllowedSwap(FourCC('O055'), 1, p)
		SetPlayerAbilityAvailableBJ(false, FourCC('A1EP'), p)
		SetPlayerAbilityAvailableBJ(false, FourCC('A1EQ'), p)
		AiData[pi][StringHash("JTBranch")] = "Gurubashy"
	end
	p = nil
end
---@param pi integer
---@return boolean
function JungleTrollsBranchIsBlack(pi)
	return (AiData[pi][StringHash("JTBranch")] or "") == "BlackSpear"
end
---@param pi integer
---@return nothing
function startJungleTrolls(pi)
	CreateNUnitsAtLoc(5, FourCC('o04Q'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
	GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
	CreateNUnitsAtLoc(1, FourCC('h0N5'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
	GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
	GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
	AiData[pi][FourCC('o04Q')] = 5
	AiData[pi][FourCC('h0N5')] = 1
	AiData[pi][StringHash("Race")] = "JT"
	SetPlayerTechResearchedSwap(FourCC('R0IH'), 1, Player(pi))
	SetPlayerName(Player(pi), "Jungle Trolls (" .. I2S(pi + 1) .. ")")
	StartJungleTrolls()
	AiChooseJungleTrollsBranch(pi)
	AiRace[pi] = "JungleTrolls"
	ProbeLogWrite("[AI] startJungleTrolls pi=" .. tostring(pi) .. " workers=5o04Q building=1h0N5")
end
---@param u unit
---@param pi integer
---@return nothing
function aiNavalTrain_JungleTrolls(u, pi)
	if Random(1, 2) and (AiData[pi][FourCC('h0D6')] or 0) < 50 then
		IssueImmediateOrderById(u, FourCC('h0D6'))
	elseif (AiData[pi][FourCC('h0D5')] or 0) < 75 then
		IssueImmediateOrderById(u, FourCC('h0D5'))
	end
end
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function Join_JungleTrolls(id, pi, u)
	if id == FourCC('o04Q') then
		GroupAddUnit(udg_Ai_builders[pi], u)
	elseif id == FourCC('h0D3') then
		-- Верфь: производит флот в naval-цикле
		GroupAddUnit(udg_Ai_navy[pi], u)
		NumberAdd(pi, StringHash("NumberN"))
	elseif aiUnitJoinsCapitalGuard(u, pi) then
	else
		aiUnitJoinsArmy(u, pi)
	end
	if id == FourCC('O054') or id == FourCC('O055') or id == FourCC('O05A') or id == FourCC('O05D') or id == FourCC('O05L') then
		GetLvlJungleTrolls(u)
	end
end
---@param u unit
---@return nothing
function AttackedJungleTrolls(u)
end
---@param id integer
---@param u unit
---@param target unit
---@param p player
---@return nothing
function Attacker_JungleTrolls(id, u, target, p)
	if id == FourCC('o04U') then
		if GetRandomInt(1, 3) == 1 then
			IssueImmediateOrder(u, "berserk")
		end
	elseif id == FourCC('O054') then
		if GetRandomInt(1, 3) == 1 and not IsUnitType(target, UNIT_TYPE_STRUCTURE) then
			IssueTargetOrder(u, "hex", target)
		end
	elseif id == FourCC('O05A') then
		if GetRandomInt(1, 4) == 1 then
			IssueImmediateOrder(u, "whirlwind")
		end
	end
end
---@param id integer
---@return nothing
function Strateg_JungleTrolls_EC(id)
	if id == FourCC('h0N2') then
		udg_LocalInteger3 = udg_LocalInteger3 + 1
	elseif id == FourCC('h0N5') then
		udg_LocalInteger3 = udg_LocalInteger3 + 2
	elseif id == FourCC('h0N1') then
		udg_LocalInteger3 = udg_LocalInteger3 + 5
	elseif id == FourCC('h0N6') then
		udg_LocalInteger3 = udg_LocalInteger3 + 8
	end
end
---@param i integer
---@param pi integer
---@param p player
---@return nothing
function Strateg_JungleTrolls(i, pi, p)
	local r = 0
	if Grades[pi] < 100 then
		if i > 17 then
			r = GetRandomInt(1, 4)
			if r == 1 then
				MakeGradeCheckCap(p, FourCC('h0N3'), FourCC('R0I8'), 6)
				MakeGradeCheckCap(p, FourCC('h0N3'), FourCC('R0I9'), 6)
				MakeGradeCheckCap(p, FourCC('h0N3'), FourCC('R0IA'), 6)
				MakeGradeCheckCap(p, FourCC('h0N3'), FourCC('R0II'), 2)
			elseif r == 2 then
				MakeGradeCheckCap(p, FourCC('h0MY'), FourCC('R0IK'), 6)
				MakeGradeCheckCap(p, FourCC('h0MY'), FourCC('R0IM'), 6)
				MakeGradeCheckCap(p, FourCC('h0N2'), FourCC('R0IJ'), 6)
			elseif r == 3 then
				MakeGradeCheckCap(p, FourCC('h0MX'), FourCC('R0IB'), 6)
				MakeGradeCheckCap(p, FourCC('h0MX'), FourCC('R0IC'), 6)
				MakeGradeCheckCap(p, FourCC('h0MX'), FourCC('R0ID'), 6)
			else
				MakeGradeCheckCap(p, FourCC('h0MW'), FourCC('R0IL'), 6)
				MakeGradeCheckCap(p, FourCC('h0MW'), FourCC('R0IN'), 6)
				MakeGradeCheckCap(p, FourCC('h0MW'), FourCC('R0IJ'), 6)
			end
		end
		if i > 45 then
			MakeGradeCheckCap(p, FourCC('h0D3'), FourCC('R005'), 6)
			MakeGradeCheckCap(p, FourCC('h0D3'), FourCC('R006'), 6)
			MakeGradeCheckCap(p, FourCC('h0D3'), FourCC('R007'), 6)
			MakeGradeCheckCap(p, FourCC('h0D3'), FourCC('R002'), 6)
			MakeGradeCheckCap(p, FourCC('h0D3'), FourCC('R003'), 6)
		end
	else
		warRace(Grades[pi], p)
	end
	if i > 20 and GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) > 2000 then
		TryBuy(p, i)
	end
	if i > 25 and getAiCount(pi, FourCC('h0N1')) < 3 then
		BuildT(p, FourCC('h0N5'), FourCC('h0N1'))
	end
	if i > 55 and getAiCount(pi, FourCC('h0N6')) < 3 then
		BuildT(p, FourCC('h0N1'), FourCC('h0N6'))
	end
end
---@param pi integer
---@return integer
function ChooseBuildings_JungleTrolls(pi)
	local i
	tArray[0] = 1
	tArray[1] = FourCC('h0N2')
	CheckAndAddBuilding(pi, FourCC('h0N5'), 4, 4)
	CheckAndAddBuilding(pi, FourCC('h0N2'), 18, 4)
	CheckAndAddBuilding(pi, FourCC('h0MY'), 10, 4)
	CheckAndAddBuilding(pi, FourCC('h0N3'), 5, 2)
	CheckAndAddBuilding(pi, FourCC('h0N0'), 3, 6)
	if getAiCount(pi, FourCC('h0N1')) + getAiCount(pi, FourCC('h0N6')) >= 1 then
		CheckAndAddBuilding(pi, FourCC('h0MX'), 8, 6)
		CheckAndAddBuilding(pi, FourCC('h0MW'), 8, 6)
		CheckAndAddBuilding(pi, FourCC('h0D3'), 2, 1)
	end
	i = GetRandomInt(1, tArray[0])
	return tArray[i]
end
---@param id integer
---@param pi integer
---@param u unit
---@return nothing
function PereborBuildings2_JungleTrolls(id, pi, u)
	local a = {}
	if id == FourCC('h0MY') then
		a[0] = 0
		for _ = 1, 5 do
			a[0] = a[0] + 1
			a[a[0]] = FourCC('o04M')
		end
		for _ = 1, 4 do
			a[0] = a[0] + 1
			a[a[0]] = FourCC('o04L')
		end
		if getAiCount(pi, FourCC('h0N1')) + getAiCount(pi, FourCC('h0N6')) >= 1 then
			a[0] = a[0] + 1
			a[a[0]] = FourCC('o05E')
		end
		local trainId = a[GetRandomInt(1, a[0])]
		IssueImmediateOrderById(u, trainId)
	elseif id == FourCC('h0MX') then
		a[0] = 0
		for _ = 1, 3 do
			a[0] = a[0] + 1
			a[a[0]] = FourCC('o04O')
		end
		for _ = 1, 3 do
			a[0] = a[0] + 1
			a[a[0]] = FourCC('o04R')
		end
		if JungleTrollsBranchIsBlack(pi) then
			for _ = 1, 4 do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('o04N')
			end
		else
			for _ = 1, 4 do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('o04P')
			end
		end
		local trainId = a[GetRandomInt(1, a[0])]
		IssueImmediateOrderById(u, trainId)
	elseif id == FourCC('h0MW') then
		a[0] = 0
		for _ = 1, 3 do
			a[0] = a[0] + 1
			a[a[0]] = FourCC('o04S')
		end
		for _ = 1, 4 do
			a[0] = a[0] + 1
			a[a[0]] = FourCC('o04U')
		end
		if getAiCount(pi, FourCC('h0N1')) + getAiCount(pi, FourCC('h0N6')) >= 1 then
			for _ = 1, 2 do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('o05J')
			end
		end
		if getAiCount(pi, FourCC('h0N6')) >= 1 then
			for _ = 1, 2 do
				a[0] = a[0] + 1
				a[a[0]] = FourCC('o05G')
			end
		end
		local trainId = a[GetRandomInt(1, a[0])]
		IssueImmediateOrderById(u, trainId)
	elseif id == FourCC('h0N0') then
		a[0] = 4
		a[1] = FourCC('O054')
		a[2] = FourCC('O05A')
		a[3] = FourCC('O05D')
		a[4] = JungleTrollsBranchIsBlack(pi) and FourCC('O05L') or FourCC('O055')
		local trainId = a[GetRandomInt(1, a[0])]
		IssueImmediateOrderById(u, trainId)
	elseif id == FourCC('h0N5') or id == FourCC('h0N1') or id == FourCC('h0N6') then
		if getAiCount(pi, FourCC('o04Q')) < 18 then
			IssueImmediateOrderById(u, FourCC('o04Q'))
		end
	end
end
---@param pi integer
---@param id integer
---@return nothing
function UpgradeJungleTrolls(pi, id)
	if id == FourCC('h0N1') then
		NumberRem(pi, FourCC('h0N5'))
	elseif id == FourCC('h0N6') then
		NumberRem(pi, FourCC('h0N1'))
	end
end
---@param u unit
---@return nothing
function GetLvlJungleTrolls(u)
	local id = GetUnitTypeId(u)
	if id == FourCC('O054') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('AOsw'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('AOhw'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A1E0'))
		else
			SelectHeroSkill(u, FourCC('A1D0'))
		end
	elseif id == FourCC('O05A') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A1E4'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A1E2'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A1E3'))
		else
			SelectHeroSkill(u, FourCC('A1D0'))
		end
	elseif id == FourCC('O05D') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A1E8'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A1E6'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A1E9'))
		else
			SelectHeroSkill(u, FourCC('A1EA'))
		end
	elseif id == FourCC('O055') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A1DM'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A1DB'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A1DC'))
		else
			SelectHeroSkill(u, FourCC('A1EL'))
		end
	elseif id == FourCC('O05L') then
		gInt = GetRandomInt(1, 3)
		if GetHeroLevel(u) == 6 or GetHeroLevel(u) == 10 then
			SelectHeroSkill(u, FourCC('A1ET'))
		elseif gInt == 1 then
			SelectHeroSkill(u, FourCC('A1ES'))
		elseif gInt == 2 then
			SelectHeroSkill(u, FourCC('A1EV'))
		else
			SelectHeroSkill(u, FourCC('A1EY'))
		end
	end
end
-- ***************************************************************************
-- *  LibRacesEnd

-- ====================================================================
-- HordeW2 AI (Phase 3: data-driven)
-- ====================================================================
---@param pi integer
---@return nothing
function startHordeW2(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('w200'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('w20q'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('w200')] = 5
    AiData[pi][FourCC('w20q')] = 1
    AiData[pi][StringHash("Race")] = "H2"
    SetPlayerTechResearchedSwap(FourCC('R0KB'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0KD'), 1, p)
    SetPlayerName(p, "Horde W2 (" .. I2S(pi + 1) .. ")")
    HordeW2On()
    AiRace[pi] = "HordeW2"
    ProbeLogWrite("[AI] startHordeW2 pi=" .. tostring(pi) .. " workers=5w200 building=1w20q")
end
---@param pi integer
---@return nothing
function startNerubs(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(3, FourCC('h0BE'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0CO'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h0BE')] = 3
    AiData[pi][FourCC('h0CO')] = 1
    AiData[pi][StringHash("Race")] = "NE"
    SetPlayerTechResearchedSwap(FourCC('R07N'), 1, p)
    SetPlayerName(p, "Nerubs (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Nerubs"
    ProbeLogWrite("[AI] startNerubs pi=" .. tostring(pi) .. " workers=3h0BE building=1h0CO")
end
---@param pi integer
---@return nothing
function startForestTrolls(pi)
    CreateNUnitsAtLoc(5, FourCC('o04V'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0MT'), Player(pi), udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('o04V')] = 5
    AiData[pi][FourCC('h0MT')] = 1
    AiData[pi][StringHash("Race")] = "FT"
    SetPlayerTechResearchedSwap(FourCC('R0J1'), 1, Player(pi))
    -- ForestTrolls unit limits (mirrors ForestStart in 80_generated_runtime.lua)
    local p = Player(pi)
    SetPlayerTechMaxAllowedSwap(FourCC('o05N'), 3, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o05M'), 3, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o05O'), 3, p)
    SetPlayerTechMaxAllowedSwap(FourCC('O056'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('O057'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('O058'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('O059'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o04Y'), 0, p)
    SetPlayerName(Player(pi), "Forest Trolls (" .. I2S(pi + 1) .. ")")
    StartForestTrolls()
    AiRace[pi] = "ForestTrolls"
    ProbeLogWrite("[AI] startForestTrolls pi=" .. tostring(pi) .. " workers=5o04V building=1h0MT")
end
---@param pi integer
---@return nothing
function startForsaken(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h0J5'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0JP'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h0J5')] = 5
    AiData[pi][FourCC('h0JP')] = 1
    AiData[pi][StringHash("Race")] = "UD"
    SetPlayerTechResearchedSwap(FourCC('R0G3'), 1, p)
    SetPlayerName(p, "Forsaken (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Forsaken"
    ProbeLogWrite("[AI] startForsaken pi=" .. tostring(pi) .. " workers=5h0J5 building=1h0JP")
end
---@param pi integer
---@return nothing
function startAlliance(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('hpea'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('htow'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('hpea')] = 5
    AiData[pi][FourCC('htow')] = 1
    AiData[pi][StringHash("Race")] = "AL"
    SetPlayerTechResearchedSwap(FourCC('R0GZ'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, p)
    ConditionalTriggerExecute(gg_trg_AllyOn)
    SetPlayerName(p, "Alliance (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Alliance"
    ProbeLogWrite("[AI] startAlliance pi=" .. tostring(pi) .. " workers=5hpea building=1htow")
end
---@param pi integer
---@return nothing
function startBandits(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h002'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h007'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h002')] = 5
    AiData[pi][FourCC('h007')] = 1
    AiData[pi][StringHash("Race")] = "BD"
    SetPlayerTechResearchedSwap(FourCC('R00G'), 1, p)
    SetPlayerName(p, "Bandits (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Bandits"
    ProbeLogWrite("[AI] startBandits pi=" .. tostring(pi) .. " workers=5h002 building=1h007")
end
---@param pi integer
---@return nothing
function startUndead(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(3, FourCC('u00P'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('n014'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('u00P')] = 3
    AiData[pi][FourCC('n014')] = 1
    AiData[pi][StringHash("Race")] = "UD"
    SetPlayerTechResearchedSwap(FourCC('R07I'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0J5'), 1, p)
    SetPlayerName(p, "Undead (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Undead"
    ProbeLogWrite("[AI] startUndead pi=" .. tostring(pi) .. " workers=3u00P building=1n014")
end
---@param pi integer
---@return nothing
function startDemons(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(8, FourCC('e02Y'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0DU'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('e02Y')] = 8
    AiData[pi][FourCC('h0DU')] = 1
    AiData[pi][StringHash("Race")] = "DE"
    SetPlayerTechResearchedSwap(FourCC('R0AO'), 1, p)
    SetPlayerName(p, "Demons (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Demons"
    ProbeLogWrite("[AI] startDemons pi=" .. tostring(pi) .. " workers=8e02Y building=1h0DU")
end
---@param pi integer
---@return nothing
function startDraenei(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h012'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h015'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h012')] = 5
    AiData[pi][FourCC('h015')] = 1
    AiData[pi][StringHash("Race")] = "DR"
    SetPlayerTechResearchedSwap(FourCC('R07G'), 1, p)
    SetPlayerName(p, "Draenei (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Draenei"
    ProbeLogWrite("[AI] startDraenei pi=" .. tostring(pi) .. " workers=5h012 building=1h015")
end
---@param pi integer
---@return nothing
function startStromgard(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h0G9'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0GZ'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h0G9')] = 5
    AiData[pi][FourCC('h0GZ')] = 1
    AiData[pi][StringHash("Race")] = "SG"
    SetPlayerTechResearchedSwap(FourCC('R0H3'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, p)
    TriggerExecute(gg_trg_StromgardOn)
    SetPlayerName(p, "Stromgard (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Stromgard"
    ProbeLogWrite("[AI] startStromgard pi=" .. tostring(pi) .. " workers=5h0G9 building=1h0GZ")
end
---@param pi integer
---@return nothing
function startIllidari(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h0EI'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0E9'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h0EI')] = 5
    AiData[pi][FourCC('h0E9')] = 1
    AiData[pi][StringHash("Race")] = "IL"
    SetPlayerTechResearchedSwap(FourCC('R07H'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0KZ'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, p)
    ConditionalTriggerExecute(gg_trg_IllidaryOn)
    SetPlayerName(p, "Illidari (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Illidari"
    ProbeLogWrite("[AI] startIllidari pi=" .. tostring(pi) .. " workers=5h0EI building=1h0E9")
end
---@param pi integer
---@return nothing
function startWorgen(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h0IT'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0IK'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h0IT')] = 5
    AiData[pi][FourCC('h0IK')] = 1
    AiData[pi][StringHash("Race")] = "WG"
    SetPlayerTechResearchedSwap(FourCC('R0FX'), 1, p)
    SetPlayerName(p, "Worgen (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Worgen"
    ProbeLogWrite("[AI] startWorgen pi=" .. tostring(pi) .. " workers=5h0IT building=1h0IK")
end
---@param pi integer
---@return nothing
function startOgres(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('o03W'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('o035'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('o03W')] = 5
    AiData[pi][FourCC('o035')] = 1
    AiData[pi][StringHash("Race")] = "OG"
    SetPlayerTechResearchedSwap(FourCC('R0HT'), 1, p)
    SetPlayerName(p, "Ogres (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Ogres"
    ProbeLogWrite("[AI] startOgres pi=" .. tostring(pi) .. " workers=5o03W building=1o035")
end
---@param pi integer
---@return nothing
function startGnomes(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h0FA'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0FK'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h0FA')] = 5
    AiData[pi][FourCC('h0FK')] = 1
    AiData[pi][StringHash("Race")] = "GN"
    SetPlayerTechResearchedSwap(FourCC('R0BX'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
    ConditionalTriggerExecute(gg_trg_GnomesOn)
    SetPlayerName(p, "Gnomes (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Gnomes"
    ProbeLogWrite("[AI] startGnomes pi=" .. tostring(pi) .. " workers=5h0FA building=1h0FK")
end
---@param pi integer
---@return nothing
function startSilitids(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(8, FourCC('e01G'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('e01H'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('e01G')] = 8
    AiData[pi][FourCC('e01H')] = 1
    AiData[pi][StringHash("Race")] = "SL"
    SetPlayerTechResearchedSwap(FourCC('R0BV'), 1, p)
    ConditionalTriggerExecute(gg_trg_SilitidsOn)
    SetPlayerName(p, "Silitids (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Silitids"
    ProbeLogWrite("[AI] startSilitids pi=" .. tostring(pi) .. " workers=8e01G building=1e01H")
end
---@param pi integer
---@return nothing
function startPandarens(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('pa01'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('pa23'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('pa01')] = 5
    AiData[pi][FourCC('pa23')] = 1
    AiData[pi][StringHash("Race")] = "PA"
    SetPlayerTechResearchedSwap(FourCC('R0L3'), 1, p)
    Pstart(p)
    SetPlayerName(p, "Pandarens (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Pandarens"
    ProbeLogWrite("[AI] startPandarens pi=" .. tostring(pi) .. " workers=5pa01 building=1pa23")
end
---@param pi integer
---@return nothing
function startBezlikie(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(3, FourCC('u02D'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0HZ'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('u02D')] = 3
    AiData[pi][FourCC('h0HZ')] = 1
    AiData[pi][StringHash("Race")] = "BL"
    SetPlayerTechResearchedSwap(FourCC('R0F9'), 1, p)
    SetPlayerName(p, "Bezlikie (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Bezlikie"
    ProbeLogWrite("[AI] startBezlikie pi=" .. tostring(pi) .. " workers=3u02D building=1h0HZ")
end
---@param pi integer
---@return nothing
function startVrykul(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h0C9'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h0BQ'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h0C9')] = 5
    AiData[pi][FourCC('h0BQ')] = 1
    AiData[pi][StringHash("Race")] = "VR"
    SetPlayerTechResearchedSwap(FourCC('R07F'), 1, p)
    SetPlayerName(p, "Vrykul (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Vrykul"
    ProbeLogWrite("[AI] startVrykul pi=" .. tostring(pi) .. " workers=5h0C9 building=1h0BQ")
end
---@param pi integer
---@return nothing
function startKulTiras(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('h013'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h01X'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('h013')] = 5
    AiData[pi][FourCC('h01X')] = 1
    AiData[pi][StringHash("Race")] = "KT"
    SetPlayerTechResearchedSwap(FourCC('R07D'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, p)
    SetPlayerName(p, "KulTiras (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "KulTiras"
    ProbeLogWrite("[AI] startKulTiras pi=" .. tostring(pi) .. " workers=5h013 building=1h01X")
end
---@param pi integer
---@return nothing
function startDalaran(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(3, FourCC('u001'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('h030'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('u001')] = 3
    AiData[pi][FourCC('h030')] = 1
    AiData[pi][StringHash("Race")] = "DL"
    SetPlayerTechResearchedSwap(FourCC('R0BW'), 1, p)
    SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, p)
    SetPlayerName(p, "Dalaran (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "Dalaran"
    ProbeLogWrite("[AI] startDalaran pi=" .. tostring(pi) .. " workers=3u001 building=1h030")
end
---@param pi integer
---@return nothing
function startIceTrolls(pi)
    local p = Player(pi)
    CreateNUnitsAtLoc(5, FourCC('o045'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_units[pi])
    GroupAddGroup(GetLastCreatedGroup(), udg_Ai_builders[pi])
    CreateNUnitsAtLoc(1, FourCC('o046'), p, udg_LocalPoint, bj_UNIT_FACING)
    GroupAddUnit(udg_Ai_units[pi], GetLastCreatedUnit())
    GroupAddUnit(udg_Ai_buildings[pi], GetLastCreatedUnit())
    AiData[pi][FourCC('o045')] = 5
    AiData[pi][FourCC('o046')] = 1
    AiData[pi][StringHash("Race")] = "IT"
    SetPlayerTechResearchedSwap(FourCC('R0L1'), 1, p)
    SetPlayerName(p, "IceTrolls (" .. I2S(pi + 1) .. ")")
    AiRace[pi] = "IceTrolls"
    ProbeLogWrite("[AI] startIceTrolls pi=" .. tostring(pi) .. " workers=5o045 building=1o046")
end
-- library Races ends
