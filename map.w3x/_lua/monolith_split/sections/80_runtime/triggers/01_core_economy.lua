-- *  Triggers
-- 
-- ***************************************************************************
-- ===========================================================================
--  Trigger: sek5
-- 
--  ??? ????? ??????????? 
-- ===========================================================================
---@return nothing
function Trig_sek5_Func001A()
	
	local pe = GetEnumPlayer()
	
	local i = 0
	-- ????? ?????????????
	SetPlayerTechMaxAllowed(pe, FourCC('n026'), i)	-- ???????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('H0H8'), i)	-- ??????? ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H0H9'), i)	-- ??????? ?????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H0H7'), i)	-- ??????? ????????? ?????
	
	-- ?????
	
	SetPlayerTechMaxAllowed(pe, FourCC('o03Q'), i)	-- ????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('o03V'), i)	-- ???? ??????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('o03T'), i)	-- ???? ?????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('o03S'), i)	-- ????? ??????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('o03R'), i)	-- ????? ????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('o03T'), i)	-- ???? ?????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('o03U'), i)	-- ???? ?????
	
	i = 1
	
	SetPlayerTechMaxAllowed(pe, FourCC('E029'), i)	-- ????????
	SetPlayerTechMaxAllowed(pe, FourCC('U02X'), i)	-- ????? ???????? 2 ??
	SetPlayerTechMaxAllowed(pe, FourCC('H048'), i)	-- ??????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('N072'), i)	-- ??????
	SetPlayerTechMaxAllowed(pe, FourCC('N06P'), i)	-- ???-????
	SetPlayerTechMaxAllowed(pe, FourCC('U02W'), i)	-- ???-???
	SetPlayerTechMaxAllowed(pe, FourCC('O05U'), i)	-- ???????
	SetPlayerTechMaxAllowed(pe, FourCC('U02U'), i)	-- ???-???
	SetPlayerTechMaxAllowed(pe, FourCC('O04K'), i)	-- ??????? ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('O04H'), i)	-- ??????? ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('O04G'), i)	-- ???'??? ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('O04I'), i)	-- ?????-??? ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H0JU'), i)	-- ???? ?????????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('N054'), i)	-- ???????? ???? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H0JV'), i)	-- ???????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('H03S'), i)	-- ?????? ?????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H028'), i)	-- ??????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H03H'), i)	-- ??????? ?????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H018'), i)	-- ?????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H05K'), i)	-- ?????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H04S'), i)	-- ????????? ??? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H053'), i)	-- ????????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H04W'), i)	-- ???????? ?????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H052'), i)	-- ????? ?????-???? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H04X'), i)	-- ?????? ?????? ????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H05M'), i)	-- ?????? ??????????
	SetPlayerTechMaxAllowed(pe, FourCC('H06B'), i)	-- ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H05L'), i)	-- ??????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H054'), i)	-- ?????
	SetPlayerTechMaxAllowed(pe, FourCC('H03J'), i)	-- ????? ????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H06C'), i)	-- ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('H01K'), i)	-- ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H01N'), i)	-- ?????????? ????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('H01J'), i)	-- ?????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H01M'), i)	-- ?????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H01L'), i)	-- ???????
	SetPlayerTechMaxAllowed(pe, FourCC('O011'), i)	-- ????????? ???? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('N010'), i)	-- ???????????? ?????? ?????????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('N00Z'), i)	-- ?????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('U007'), i)	-- ??-???
	SetPlayerTechMaxAllowed(pe, FourCC('H0C4'), i)	-- ?????? ?????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H0C7'), i)	-- ????????? ???? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H0C5'), i)	-- ??????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H0C6'), i)	-- ??? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('U00O'), i)	-- ?????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('U015'), i)	-- ????????? ???
	SetPlayerTechMaxAllowed(pe, FourCC('U01W'), i)	-- ?????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('U01V'), i)	-- ?????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('U01U'), i)	-- ??????
	SetPlayerTechMaxAllowed(pe, FourCC('U00V'), i)	-- ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('U00U'), i)	-- ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('U014'), i)	-- ??????-??? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('E01W'), i)	-- ??????? ?? ??????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('E01F'), i)	-- ??????
	SetPlayerTechMaxAllowed(pe, FourCC('E01D'), i)	-- ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('E01E'), i)	-- ???????
	SetPlayerTechMaxAllowed(pe, FourCC('E01C'), i)	-- ????????
	SetPlayerTechMaxAllowed(pe, FourCC('E025'), i)	-- ??????? ??????????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('E024'), i)	-- ??????? ????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('E026'), i)	-- ???????
	SetPlayerTechMaxAllowed(pe, FourCC('N02F'), i)	-- ?????????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('N02H'), i)	-- ?????
	SetPlayerTechMaxAllowed(pe, FourCC('N02G'), i)	-- ????????
	SetPlayerTechMaxAllowed(pe, FourCC('N02B'), i)	-- ???'??????
	SetPlayerTechMaxAllowed(pe, FourCC('N02A'), i)	-- ????????????
	SetPlayerTechMaxAllowed(pe, FourCC('U027'), i)	-- ??????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('U028'), i)	-- ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('N046'), i)	-- ???????????
	SetPlayerTechMaxAllowed(pe, FourCC('N047'), i)	-- ?????
	SetPlayerTechMaxAllowed(pe, FourCC('N045'), i)	-- ???????
	SetPlayerTechMaxAllowed(pe, FourCC('N040'), i)	-- ????????
	SetPlayerTechMaxAllowed(pe, FourCC('H0EZ'), i)	-- ??????????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('H0F0'), i)	-- ?????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('N037'), i)	-- ?????????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('H0HP'), i)	-- ????? ??? ????
	SetPlayerTechMaxAllowed(pe, FourCC('H0HQ'), i)	-- ?????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('U02H'), i)	-- ????????? ??????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('U02G'), i)	-- ??????? ?'???????
	SetPlayerTechMaxAllowed(pe, FourCC('U02I'), i)	-- ??? ???????????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('H0HL'), i)	-- ???????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('H0HB'), i)	-- ??????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('H0HA'), i)	-- ????????? ??? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('H0L4'), i)	-- ????? ????????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('U035'), i)	-- ????'?????
	SetPlayerTechMaxAllowed(pe, FourCC('U030'), i)	-- ????'????
	SetPlayerTechMaxAllowed(pe, FourCC('U02F'), i)	-- ????????? ??????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('NE02'), i)	-- ???? ????? ??
	SetPlayerTechMaxAllowed(pe, FourCC('E02Q'), i)	-- ??? ????
	SetPlayerTechMaxAllowed(pe, FourCC('E02R'), i)	-- ????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('E02S'), i)	-- ?????? ?????????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('PA37'), i)	-- ?????? ???????? ???? ??
	SetPlayerTechMaxAllowed(pe, FourCC('PA38'), i)	-- ?????? ????? ??
	SetPlayerTechMaxAllowed(pe, FourCC('PA36'), i)	-- ????? ????-???
	SetPlayerTechMaxAllowed(pe, FourCC('PA40'), i)	-- ????????? ? ?????? ??
	SetPlayerTechMaxAllowed(pe, FourCC('E02R'), i)	-- ????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('E011'), i)	-- ?????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('E02Q'), i)	-- ??? ????
	SetPlayerTechMaxAllowed(pe, FourCC('N073'), i)	-- ?????? ?????? ???? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('E02S'), i)	-- ?????? ?????????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('W2Og'), i)	-- ????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('W202'), i)	-- ???????????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('W201'), i)	-- ?????????? ???
	SetPlayerTechMaxAllowed(pe, FourCC('N05J'), i)	-- ???????????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('N05K'), i)	-- ????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('N05L'), i)	-- ??????? ?????
	
	-- ?????
	SetPlayerTechMaxAllowed(pe, FourCC('W200'), i)	-- ?????? ???? ?????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('CD01'), i)	-- ??????? ??????????
	SetPlayerTechMaxAllowed(pe, FourCC('CD02'), i)	-- ????????? ??
	SetPlayerTechMaxAllowed(pe, FourCC('CD03'), i)	-- ????????? ??
	
	i = 0
	
	SetPlayerTechMaxAllowed(pe, FourCC('cD34'), i)	-- ?????? ???? 2 ??
	SetPlayerTechMaxAllowed(pe, FourCC('cD35'), i)	-- ?????? ???? 3 ??
	SetPlayerTechMaxAllowed(pe, FourCC('n02D'), i)	-- ???????? ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('n02E'), i)	-- ??????????????
	
	-- ????? 
	i = 5
	
	SetPlayerTechMaxAllowed(pe, FourCC('cD12'), i)	-- ??????????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('h0OE'), i)	-- ????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('w219'), i)	-- ????????? ?????????? ?? 2
	
	i = 10
	
	SetPlayerTechMaxAllowed(pe, FourCC('h0DT'), i)	-- ????????? ???????
	
	i = 15
	
	SetPlayerTechMaxAllowed(pe, FourCC('h0H2'), i)	-- ????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('hhou'), i)	-- ????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('nnfm'), i)	-- ????????? ???
	SetPlayerTechMaxAllowed(pe, FourCC('w20y'), i)	-- ??????????
	SetPlayerTechMaxAllowed(pe, FourCC('h0N2'), i)	-- ?????? ?????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('o04C'), i)	-- ??????? ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('h05Y'), i)	-- ????? ???? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('h05C'), i)	-- ??????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('h024'), i)	-- ????? ??? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('h0IM'), i)	-- ????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('h031'), i)	-- ??????????? ???? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('h04M'), i)	-- ????????
	SetPlayerTechMaxAllowed(pe, FourCC('h00A'), i)	-- ??????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('h0FL'), i)	-- ??????????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('h0NW'), i)	-- ???????? ????? ??? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('o003'), i)	-- ???????
	SetPlayerTechMaxAllowed(pe, FourCC('o00T'), i)	-- ???????? ?????????? ?????
	SetPlayerTechMaxAllowed(pe, FourCC('emow'), i)	-- ??????? ????????????
	SetPlayerTechMaxAllowed(pe, FourCC('h0BT'), i)	-- ??? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('u00H'), i)	-- ????????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('e00N'), i)	-- ?????? ??????? ????
	SetPlayerTechMaxAllowed(pe, FourCC('e02E'), i)	-- ??????? ????????????
	SetPlayerTechMaxAllowed(pe, FourCC('h0CE'), i)	-- ???????? ???? ??????????????
	SetPlayerTechMaxAllowed(pe, FourCC('h0DS'), i)	-- ?????????? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('h0MV'), i)	-- ?????? ??????
	SetPlayerTechMaxAllowed(pe, FourCC('h0EC'), i)	-- ?????????? ??????? ?????????
	SetPlayerTechMaxAllowed(pe, FourCC('h0EX'), i)	-- ????????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('h0F9'), i)	-- ?????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('otrb'), i)	-- ????????
	SetPlayerTechMaxAllowed(pe, FourCC('u02E'), i)	-- ????? ?????????? ????????
	SetPlayerTechMaxAllowed(pe, FourCC('h0JD'), i)	-- ??? ????????? ??????????
	SetPlayerTechMaxAllowed(pe, FourCC('o036'), i)	-- ??????????
	SetPlayerTechMaxAllowed(pe, FourCC('o060'), i)	-- ?????????? ???? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('h0NZ'), i)	-- ???????? ??? ?????????
	
	i = 20
	
	SetPlayerTechMaxAllowed(pe, FourCC('h077'), i)	-- ???? ???????
	SetPlayerTechMaxAllowed(pe, FourCC('u019'), i)	-- ????? ??????
	
	i = 25
	SetPlayerTechMaxAllowed(pe, FourCC('h0NZ'), i)	-- ?????????? ????? ??? ?????
	
	i = 30
	SetPlayerTechMaxAllowed(pe, FourCC('e01J'), i)	-- ????? ????????
	
	i = 100
	SetPlayerTechMaxAllowed(pe, FourCC('pa26'), i)	-- ????? ??????????
	
	-- ?????
	SetPlayerAbilityAvailable(pe, FourCC('w290'), false)	-- ??????? ????? ???? 2 ?????
	SetPlayerAbilityAvailable(pe, FourCC('w289'), false)	-- ???????? ????? ???? 2 ?????
	SetPlayerAbilityAvailable(pe, FourCC('w288'), false)	-- ????????? ???????? ???? 2 ?????
	
	pe = nil
	
end
---@return nothing
function Trig_sek5_Actions()
	ForForce(GetPlayersAll(), Trig_sek5_Func001A)
end
-- ===========================================================================
---@return nothing
function InitTrig_sek5()
	gg_trg_sek5 = CreateTrigger()
	TriggerRegisterTimerEventSingle(gg_trg_sek5, 5)
	TriggerAddAction(gg_trg_sek5, Trig_sek5_Actions)
end
-- ===========================================================================
--  Trigger: RRR
-- ===========================================================================
---@return boolean
function Trig_RRR_Func001001003()
	
	return IsUnitEnemy(GetFilterUnit(), GetOwningPlayer(udg_LocalUnit2)) and  not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE)
	
end
---@return nothing
function Trig_RRR_Func001A()
	
	local l = PolarProjectionBJ(GetUnitLoc(GetEnumUnit()), (7.00 + (4.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A18Q'), udg_LocalUnit2)))), (GetUnitFacing(GetEnumUnit()) + 180.00))
	--  ??? ?????????? ???????? ?? ???????? ?????? 7+ 3 ?????? ???
	
	--  ??? ???????? ?? ???????? ????? ?????????? ?? ??????????
	SetUnitPositionLoc(GetEnumUnit(), l)
	--  ???? ?????? 0.04 ??? 1+ 2 ?????? ??? 
	UnitDamageTargetBJ(udg_LocalUnit2, GetEnumUnit(), (1.00 + (2.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A18Q'), udg_LocalUnit2)))), ATTACK_TYPE_HERO, DAMAGE_TYPE_NORMAL)
	
	--  ???????? ??????????
	l = nil
	RemoveLocation(l)
	
end
---@return nothing
function GruulForce()
	
	local pi = GetPlayerId(GetEnumPlayer())
	if Gruul[pi] ~= nil then
		udg_LocalUnit2 = Gruul[pi]
		ForGroup(GetUnitsInRangeOfLocMatching((450.00 + (55.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A18Q'), Gruul[pi])))), GetUnitLoc(Gruul[pi]), Condition(Trig_RRR_Func001001003)), Trig_RRR_Func001A)
		
	end
end
---@return nothing
function Trig_RRR_Actions()
	
	ForForce(udg_AllPlayers, GruulForce)
	
end
-- ===========================================================================
---@return nothing
function InitTrig_RRR()
	gg_trg_RRR = CreateTrigger()
	TriggerRegisterTimerEventPeriodic(gg_trg_RRR, 0.04)
	TriggerAddAction(gg_trg_RRR, Trig_RRR_Actions)
end
---@param u unit
---@param time real
---@return nothing
function RemoveUnitTimed(u, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		RemoveUnit(u)
		DestroyTimer(t)
	end)
end
---@param u unit
---@param time real
---@return nothing
function ReviveHeroTimed(u, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		gUnit = u
		Counter = 0
		GroupEnumUnitsOfPlayer(gGroup, GetOwningPlayer(gUnit), UnitsWithReviveHeroSpell)
		if FirstOfGroup(gGroup) ~= nil then
			gUnit2 = GroupPickRandomUnit2(gGroup)
			ReviveHero(gUnit, GetUnitX(gUnit2), GetUnitY(gUnit2), true)
		end
		DestroyTimer(t)
	end)
end
---@param l lightning
---@param time real
---@return nothing
function RemoveLigtingTimed(l, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		DestroyLightning(l)
		DestroyTimer(t)
	end)
end
---@param ft texttag
---@param time real
---@return nothing
function RemoveTextTagTimed(ft, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		DestroyTextTag(ft)
		DestroyTimer(t)
	end)
end
---@param u unit
---@param CollisionOn boolean
---@param time real
---@return nothing
function CollisionTimed(u, CollisionOn, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		SetUnitPathing(u, CollisionOn)
		DestroyTimer(t)
	end)
end
---@param u unit
---@param BuildingProgress integer
---@param time real
---@return nothing
function SetBuildingProgressTimed(u, BuildingProgress, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		UnitSetConstructionProgress(u, BuildingProgress)
		DestroyTimer(t)
	end)
end
---@param order string
---@param u unit
---@param time real
---@return nothing
function IssuerImmediateOrderTimed(order, u, time)
	local t = CreateTimer()
	TimerStart(t, time, false, function()
		IssueImmediateOrder(u, order)
		DestroyTimer(t)
	end)
end
-- ===========================================================================
--  Trigger: IsEnemyAllyOwner
-- 
--  ????? ???? ????? ??? ???????, ??????? ?? ????? ?????? LocalUni2
-- ===========================================================================
-- 
-- function isEnemy takes nothing returns boolean
--         return IsPlayerEnemy(GetOwningPlayer(GetFilterUnit()),udg_LocalPlayer)
-- endfunction
-- 
---@return boolean
function isAlly()
	return IsPlayerAlly(GetOwningPlayer(GetFilterUnit()), udg_LocalPlayer)
end
---@return boolean
function isOwner()
	return GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer
end
-- ===========================================================================
--  Trigger: CommandIssueAllUnitsOfType
-- ===========================================================================
---@return boolean
function typeBool()
	return GetUnitTypeId(GetFilterUnit()) == gInt
end
---@param unitid integer
---@param p player
---@param order string
---@return nothing
function GlobalIssue(unitid, p, order)
	gInt = unitid
	GroupEnumUnitsOfPlayer(gGroup, p, typeBool)
	GroupImmediateOrder(gGroup, order)
end
-- ===========================================================================
--  Trigger: DummyCastSpelll
-- ===========================================================================
---@param spellid integer
---@param order string
---@param caster unit
---@param target unit
---@return nothing
function DummyCastTarget(spellid, order, caster, target)
	local dummy = CreateUnit(GetOwningPlayer(caster), gDummy, GetUnitX(caster), GetUnitY(caster), 0.00)
	UnitAddAbility(dummy, spellid)
	IssueTargetOrder(dummy, order, target)
	
	RemoveUnitTimed(dummy, 4.0)
	-- call BJDebugMsg( GetUnitName(caster)+" "+GetUnitName(dummy)+" "+GetUnitName(target)+" "+I2S(spellid) )
	dummy = nil
	
end
---@param spellid integer
---@param order string
---@param caster unit
---@param target unit
---@param lvl integer
---@return nothing
function DummyCastTargetLevel(spellid, order, caster, target, lvl)
	local dummy = CreateUnit(GetOwningPlayer(caster), gDummy, GetUnitX(caster), GetUnitY(caster), 0.00)
	UnitAddAbility(dummy, spellid)
	SetUnitAbilityLevel(dummy, spellid, lvl)
	IssueTargetOrder(dummy, order, target)
	
	RemoveUnitTimed(dummy, 4.0)
	-- call BJDebugMsg( GetUnitName(caster)+" "+GetUnitName(dummy)+" "+GetUnitName(target)+" "+I2S(spellid) )
	dummy = nil
	
end
---@param spellid integer
---@param order string
---@param caster unit
---@return nothing
function DummyCastImmedate(spellid, order, caster)
	local dummy = CreateUnit(GetOwningPlayer(caster), gDummy, GetUnitX(caster), GetUnitY(caster), 0.00)
	UnitAddAbility(dummy, spellid)
	IssueImmediateOrder(dummy, order)
	
	RemoveUnitTimed(dummy, 4.0)
	-- call BJDebugMsg( GetUnitName(caster)+" "+GetUnitName(dummy)+" "+GetUnitName(target)+" "+I2S(spellid) )
	dummy = nil
	
end
---@param spellid integer
---@param order string
---@param caster unit
---@param target unit
---@return nothing
function DummyCastImmedateOnTarget(spellid, order, caster, target)
	local dummy = CreateUnit(GetOwningPlayer(caster), gDummy, GetUnitX(target), GetUnitY(target), 0.00)
	UnitAddAbility(dummy, spellid)
	IssueImmediateOrder(dummy, order)
	
	RemoveUnitTimed(dummy, 4.0)
	-- call BJDebugMsg( GetUnitName(caster)+" "+GetUnitName(dummy)+" "+GetUnitName(target)+" "+I2S(spellid) )
	dummy = nil
	
end
--  call DummyCastImmedate('A0WC',"animatedead",GetKillingUnit())
-- ===========================================================================
--  Trigger: SpellMassSomeThing
-- ===========================================================================
---@param caster unit
---@param unitability integer
---@param dammyAbility integer
---@param order string
---@param targetloc location
---@param radious real
---@param targetOwning integer
---@param includeCaster boolean
---@return nothing
function MassSpell(caster, unitability, dammyAbility, order, targetloc, radious, targetOwning, includeCaster)
	local p = GetOwningPlayer(caster)
	local bex
	local level = GetUnitAbilityLevel(caster, unitability)
	local g = CreateGroup()
	local target
	local dummyCaster
	local i = 0
	--  call BJDebugMsg("?????????")
	udg_LocalPlayer = p
	if targetOwning == 1 then
		bex = isEnemy
	elseif targetOwning == 2 then
		bex = isAlly
	else
		bex = isOwner
	end
	
	if targetloc == nil then
		targetloc = GetUnitLoc(caster)
	end
	
	GroupEnumUnitsInRangeOfLoc(g, targetloc, radious, bex)
	
	if  not includeCaster then
		GroupRemoveUnit(g, caster)
	end
	
	
	if FirstOfGroup(g) == nil then
		-- ???? ??????
		BlzStartUnitAbilityCooldown(caster, unitability, BlzGetUnitAbilityCooldown(caster, unitability, level))
		-- call SetUnitState( caster,UNIT_STATE_MANA, GetUnitState( caster,UNIT_STATE_MANA)+100+35*level )
	else
		RemoveLocation(targetloc)
		targetloc = GetUnitLoc(caster)
		while true do
			target = FirstOfGroup(g)
			if target == nil then break end
			
			dummyCaster = CreateUnitAtLoc(p, gDummy, targetloc, bj_UNIT_FACING)
			--  call BJDebugMsg("???")
			UnitAddAbility(dummyCaster, dammyAbility)
			SetUnitAbilityLevel(dummyCaster, dammyAbility, level)
			IssueTargetOrder(dummyCaster, order, target)
			RemoveUnitTimed(dummyCaster, 3)
			i = i + 1
			GroupRemoveUnit(g, target)
		end
	end
	
	DestroyGroup(g)
	g = nil
	RemoveLocation(targetloc)
	p = nil
	dummyCaster = nil
	bex = nil
	
end
-- ===========================================================================
--  Trigger: SpellChannel
-- ===========================================================================
---@param caster unit
---@param spellid integer
---@param spellidD integer
---@param order string
---@param x real
---@param y real
---@param time real
---@return nothing
function SpellChannel(caster, spellid, spellidD, order, x, y, time)
	local p = GetOwningPlayer(caster)
	-- local integer level = GetUnitAbilityLevel( caster, spellid )
	
	local dummy = CreateUnit(p, Dummy, x, y, bj_UNIT_FACING)
	UnitAddAbility(dummy, spellidD)
	SetUnitState(dummy, UNIT_STATE_MANA, 10000)
	IssuePointOrder(dummy, order, x, y)
	
	RemoveUnitTimed(dummy, time + 2)
	
	
	dummy = nil
	
end
---@param caster unit
---@param spellid integer
---@param spellidD integer
---@param order string
---@param x real
---@param y real
---@param time real
---@return nothing
function SpellChannelLevel(caster, spellid, spellidD, order, x, y, time)
	local p = GetOwningPlayer(caster)
	local level = GetUnitAbilityLevel(caster, spellid)
	
	local dummy = CreateUnit(p, Dummy, x, y, bj_UNIT_FACING)
	UnitAddAbility(dummy, spellidD)
	SetUnitAbilityLevel(dummy, spellidD, level)
	SetUnitState(dummy, UNIT_STATE_MANA, 10000)
	IssuePointOrder(dummy, order, x, y)
	
	RemoveUnitTimed(dummy, time + 2)
	
	
	dummy = nil
	
end
-- ===========================================================================
--  Trigger: Unit Indexer
-- 
--  This trigger works in two key phases:
--  1) During map initialization, enumerate all units of all players to give them an index.
--  2) Adds a second event to itself to index new units as they enter the map.
--  As a unit enters the map, check for any old units that may have been removed at some point in order to free their index.
-- ===========================================================================
---@return boolean
function Trig_Unit_Indexer_Func017Func004C()
	return (udg_UDexRecycle == 0)
end
---@return boolean
function Trig_Unit_Indexer_Func017C()
	return (udg_UnitIndexerEnabled == true)
end
---@return boolean
function Trig_Unit_Indexer_Func030Func005C()
	return (GetUnitUserData(udg_UDexUnits[udg_UDex]) == 0)
end
---@return boolean
function Trig_Unit_Indexer_Func030C()
	return (udg_UDexWasted == 15)
end
---@return boolean
function Trig_Unit_Indexer_Func034C()
	return (GetUnitUserData(GetFilterUnit()) == 0)
end
---@return nothing
function Trig_Unit_Indexer_Actions()
	ExecuteFunc("InitializeUnitIndexer")
end
--   
--  This is the most important function - it provides an index for units as they enter the map
--   
---@return boolean
function IndexUnit()
	local pdex = udg_UDex
	--   
	--  You can use the boolean UnitIndexerEnabled to protect some of your undesirable units from being indexed
	--  - Example:
	--  -- Set UnitIndexerEnabled = False
	--  -- Unit - Create 1 Dummy for (Triggering player) at TempLoc facing 0.00 degrees
	--  -- Set UnitIndexerEnabled = True
	--   
	--  You can also customize the following block - if conditions are false the (Matching unit) won't be indexed.
	--   
	if (Trig_Unit_Indexer_Func017C()) then
		--   
		--  Generate a unique integer index for this unit
		--   
		if (Trig_Unit_Indexer_Func017Func004C()) then
			udg_UDex = (udg_UDexGen + 1)
			udg_UDexGen = udg_UDex
		else
			udg_UDex = udg_UDexRecycle
			udg_UDexRecycle = udg_UDexNext[udg_UDex]
		end
		--   
		--  Link index to unit, unit to index
		--   
		udg_UDexUnits[udg_UDex] = GetFilterUnit()
		SetUnitUserData(udg_UDexUnits[udg_UDex], udg_UDex)
		--   
		--  Use a doubly-linked list to store all active indexes
		--   
		udg_UDexPrev[udg_UDexNext0] = udg_UDex
		udg_UDexNext[udg_UDex] = udg_UDexNext[0]
		udg_UDexNext[0] = udg_UDex
		--   
		--  Fire index event for UDex
		--   
		udg_UnitIndexEvent = 0.00
		udg_UnitIndexEvent = 1.00
		udg_UnitIndexEvent = 0.00
		udg_UDex = pdex
	else
	end
	return false
end
--   
--  The next function is called each time a unit enters the map
--   
---@return boolean
function IndexNewUnit()
	local pdex = udg_UDex
	local ndex
	--   
	--  Recycle indices of units no longer in-play every (15) units created
	--   
	udg_UDexWasted = (udg_UDexWasted + 1)
	if (Trig_Unit_Indexer_Func030C()) then
		udg_UDexWasted = 0
		udg_UDex = udg_UDexNext[0]
		while true do
			if udg_UDex == 0 then break end
			if (Trig_Unit_Indexer_Func030Func005C()) then
				--   
				--  Remove index from linked list
				--   
				ndex = udg_UDexNext[udg_UDex]
				udg_UDexNext[udg_UDexPrevudg_UDex] = ndex
				udg_UDexPrev[ndex] = udg_UDexPrev[udg_UDex]
				udg_UDexPrev[udg_UDex] = 0
				--   
				--  Fire deindex event for UDex
				--   
				udg_UnitIndexEvent = 2.00
				udg_UnitIndexEvent = 0.00
				--   
				--  Recycle the index for later use
				--   
				udg_UDexUnits[udg_UDex] = nil
				udg_UDexNext[udg_UDex] = udg_UDexRecycle
				udg_UDexRecycle = udg_UDex
				udg_UDex = ndex
			else
				udg_UDex = udg_UDexNext[udg_UDex]
			end
		end
		udg_UDex = pdex
	else
	end
	--   
	--  Handle the entering unit (Matching unit)
	--   
	if (Trig_Unit_Indexer_Func034C()) then
		IndexUnit()
	else
	end
	return false
end
--   
--  The next function initializes the core of the system
--   
---@return nothing
function InitializeUnitIndexer()
	local i = 0
	local re = CreateRegion()
	local r = GetWorldBounds()
	udg_UnitIndexerEnabled = true
	RegionAddRect(re, r)
	TriggerRegisterEnterRegion(CreateTrigger(), re, Filter(IndexNewUnit))
	RemoveRect(r)
	re = nil
	r = nil
	while true do
		GroupEnumUnitsOfPlayer(bj_lastCreatedGroup, Player(i), Filter(IndexUnit))
		i = i + 1
		if i == 16 then break end
	end
	--   
	--  This is the "Unit Indexer Initialized" event, use it instead of "Map Initialization" for best results
	--   
	udg_UnitIndexEvent = 3.00
	udg_UnitIndexEvent = 0.00
end
-- ===========================================================================
---@return nothing
function InitTrig_Unit_Indexer()
	gg_trg_Unit_Indexer = CreateTrigger()
	TriggerAddAction(gg_trg_Unit_Indexer, Trig_Unit_Indexer_Actions)
end
-- ===========================================================================
--  Trigger: AiScore0
-- ===========================================================================
---@return nothing
function Trig_AiScore0_Actions()
	BJDebugMsg(R2SW_Polyfill(ArmyExp[0]))
end
-- ===========================================================================
---@return nothing
function InitTrig_AiScore0()
	gg_trg_AiScore0 = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_AiScore0, Player(0), "a", true)
	TriggerAddAction(gg_trg_AiScore0, Trig_AiScore0_Actions)
end
-- ===========================================================================
--  Trigger: FarmTier2
-- ===========================================================================
---@return boolean
function Trig_FarmTier2_Func001Func002C()
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0FR'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0H0'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h01Y'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h04B'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h05V'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h016'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0GP'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h008'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h034'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0CP'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0BR'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('e021'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('u00F'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('cD25'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('e020'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('etoa'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('e00L'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('e02C'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0CC'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0EA'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0DV'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0N8'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0ER'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('ostr'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0I7'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0JQ'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('hkee'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('o03D'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('o047'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0N1'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('w20w'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('o05W'))) then
		return true
	end
	if ((GetUnitTypeId(GetTriggerUnit()) == FourCC('h0IK'))) then
		return true
	end
	return false
end
---@return boolean
function Trig_FarmTier2_Func001C()
	return ((udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] <= 1)) and (Trig_FarmTier2_Func001Func002C())
end
---@return boolean
function Trig_FarmTier2_Conditions()
	return Trig_FarmTier2_Func001C()
end
---@return nothing
function Trig_FarmTier2_Actions()
	udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
	udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] = 2
	DisplayTextToForce(GetForceOfPlayer(udg_LocalPlayer), "TRIGSTR_1960")
	SetPlayerTechResearchedSwap(FourCC('R0HP'), 1, udg_LocalPlayer)
	udg_LocalInteger = 10
	SetPlayerTechMaxAllowedSwap(FourCC('cD12'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('w219'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 12
	SetPlayerTechMaxAllowedSwap(FourCC('h0HU'), udg_LocalInteger, udg_LocalPlayer)
	
	udg_LocalInteger = 20
	SetPlayerTechMaxAllowedSwap(FourCC('h0DT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0OE'), udg_LocalInteger, udg_LocalPlayer)	--  ????? ?????????
	udg_LocalInteger = 30
	SetPlayerTechMaxAllowedSwap(FourCC('h0NW'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0N2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o04C'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0H2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05Y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05C'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h024'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h031'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h04M'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h00A'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('w20y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o003'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o00T'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0BT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u00H'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e00N'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('emow'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0CE'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0DS'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EX'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0MV'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0F9'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0FL'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EC'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('otrb'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0JD'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o036'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('hhou'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o036'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o060'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	
	udg_LocalInteger = 40
	SetPlayerTechMaxAllowedSwap(FourCC('h077'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u019'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 60
	SetPlayerTechMaxAllowedSwap(FourCC('e01J'), udg_LocalInteger, udg_LocalPlayer)
	FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
-- ===========================================================================
---@return nothing
function InitTrig_FarmTier2()
	gg_trg_FarmTier2 = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FarmTier2, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
	TriggerAddCondition(gg_trg_FarmTier2, Condition(Trig_FarmTier2_Conditions))
	TriggerAddAction(gg_trg_FarmTier2, Trig_FarmTier2_Actions)
end
-- ===========================================================================
--  Trigger: FarmTier2 Res
-- ===========================================================================
---@return boolean
function Trig_FarmTier2_Res_Func001Func002Func001C()
	return ((GetPlayerTechCountSimple(FourCC('R0D4'), GetOwningPlayer(GetTriggerUnit())) == 1)) and ((GetResearched() == FourCC('R0D4')))
end
---@return boolean
function Trig_FarmTier2_Res_Func001Func002Func002C()
	return ((GetPlayerTechCountSimple(FourCC('R04D'), GetOwningPlayer(GetTriggerUnit())) == 2)) and ((GetResearched() == FourCC('R04D')))
end
---@return boolean
function Trig_FarmTier2_Res_Func001Func002Func003C()
	return ((GetPlayerTechCountSimple(FourCC('R0D9'), GetOwningPlayer(GetTriggerUnit())) == 1)) and ((GetResearched() == FourCC('R0D9')))
end
---@return boolean
function Trig_FarmTier2_Res_Func001Func002C()
	if (Trig_FarmTier2_Res_Func001Func002Func001C()) then
		return true
	end
	if (Trig_FarmTier2_Res_Func001Func002Func002C()) then
		return true
	end
	if (Trig_FarmTier2_Res_Func001Func002Func003C()) then
		return true
	end
	return false
end
---@return boolean
function Trig_FarmTier2_Res_Func001C()
	return ((udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] <= 1)) and (Trig_FarmTier2_Res_Func001Func002C())
end
---@return boolean
function Trig_FarmTier2_Res_Conditions()
	return Trig_FarmTier2_Res_Func001C()
end
---@return nothing
function Trig_FarmTier2_Res_Actions()
	udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
	udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] = 2
	DisplayTextToForce(GetForceOfPlayer(udg_LocalPlayer), "TRIGSTR_1961")
	udg_LocalInteger = 10
	SetPlayerTechMaxAllowedSwap(FourCC('cD12'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('w219'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 12
	SetPlayerTechMaxAllowedSwap(FourCC('h0HU'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 20
	SetPlayerTechMaxAllowedSwap(FourCC('h0DT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0OE'), udg_LocalInteger, udg_LocalPlayer)	--  ????? ?????????
	udg_LocalInteger = 30
	SetPlayerTechMaxAllowedSwap(FourCC('h0N2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0H2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05Y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05C'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h024'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h031'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h04M'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h00A'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0MV'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o003'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o00T'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0BT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u00H'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('emow'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e00N'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('w20y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0CE'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0DS'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EX'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0F9'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0FL'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EC'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('otrb'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0JD'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('hhou'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o036'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o060'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 40
	SetPlayerTechMaxAllowedSwap(FourCC('u019'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h077'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 60
	SetPlayerTechMaxAllowedSwap(FourCC('e01J'), udg_LocalInteger, udg_LocalPlayer)
	FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
-- ===========================================================================
---@return nothing
function InitTrig_FarmTier2_Res()
	gg_trg_FarmTier2_Res = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FarmTier2_Res, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
	TriggerAddCondition(gg_trg_FarmTier2_Res, Condition(Trig_FarmTier2_Res_Conditions))
	TriggerAddAction(gg_trg_FarmTier2_Res, Trig_FarmTier2_Res_Actions)
end
-- ===========================================================================
--  Trigger: FarmTier3
-- ===========================================================================
---@return boolean
function Trig_FarmTier3_Func002Func002C()
	local id = GetUnitTypeId(GetTriggerUnit())
	if id == FourCC('h0FS') then
		return true
	end
	if id == FourCC('h0H1') then
		return true
	end
	if id == FourCC('h01Z') then
		return true
	end
	if id == FourCC('h04A') then
		return true
	end
	if id == FourCC('h05W') then
		return true
	end
	if id == FourCC('h017') then
		return true
	end
	if id == FourCC('h035') then
		return true
	end
	if id == FourCC('h009') then
		return true
	end
	if id == FourCC('h0CQ') then
		return true
	end
	if id == FourCC('h0BS') then
		return true
	end
	if id == FourCC('u00G') then
		return true
	end
	if id == FourCC('cD24') then
		return true
	end
	if id == FourCC('e020') then
		return true
	end
	if id == FourCC('e00M') then
		return true
	end
	if id == FourCC('etoe') then
		return true
	end
	if id == FourCC('e02D') then
		return true
	end
	if id == FourCC('h0N9') then
		return true
	end
	if id == FourCC('h0CD') then
		return true
	end
	if id == FourCC('h0EB') then
		return true
	end
	if id == FourCC('h0DW') then
		return true
	end
	if id == FourCC('h0ES') then
		return true
	end
	if id == FourCC('ofrt') then
		return true
	end
	if id == FourCC('o03E') then
		return true
	end
	if id == FourCC('h0I8') then
		return true
	end
	if id == FourCC('h0JL') then
		return true
	end
	if id == FourCC('hcas') then
		return true
	end
	if id == FourCC('o048') then
		return true
	end
	if id == FourCC('h0N6') then
		return true
	end
	if id == FourCC('w20e') then
		return true
	end
	if id == FourCC('o05X') then
		return true
	end
	if id == FourCC('h0IL') then
		return true
	end
	return false
end
---@return boolean
function Trig_FarmTier3_Func002C()
	return ((udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] <= 2)) and (Trig_FarmTier3_Func002Func002C())
end
---@return boolean
function Trig_FarmTier3_Conditions()
	return Trig_FarmTier3_Func002C()
end
---@return nothing
function Trig_FarmTier3_Actions()
	udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] = 3
	udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
	DisplayTextToForce(GetForceOfPlayer(udg_LocalPlayer), "TRIGSTR_2384")
	udg_LocalInteger = 15
	SetPlayerTechMaxAllowedSwap(FourCC('cD12'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('w219'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 12
	
	SetPlayerTechMaxAllowedSwap(FourCC('h0HU'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechResearchedSwap(FourCC('R0HP'), 2, udg_LocalPlayer)
	udg_LocalInteger = 30
	SetPlayerTechMaxAllowedSwap(FourCC('h0DT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0OE'), udg_LocalInteger, udg_LocalPlayer)	--  ????? ?????????
	udg_LocalInteger = 45
	SetPlayerTechMaxAllowedSwap(FourCC('h0NW'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0N2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o04C'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0H2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0MV'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05Y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05C'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h024'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h031'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h04M'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h00A'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o003'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o00T'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0BT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u00H'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('emow'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e00N'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('w20y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0CE'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0DS'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EX'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0F9'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0FL'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EC'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('otrb'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0JD'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('hhou'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o036'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o060'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 60
	SetPlayerTechMaxAllowedSwap(FourCC('u019'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h077'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 90
	SetPlayerTechMaxAllowedSwap(FourCC('e01J'), udg_LocalInteger, udg_LocalPlayer)
	FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
-- ===========================================================================
---@return nothing
function InitTrig_FarmTier3()
	gg_trg_FarmTier3 = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FarmTier3, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
	TriggerAddCondition(gg_trg_FarmTier3, Condition(Trig_FarmTier3_Conditions))
	TriggerAddAction(gg_trg_FarmTier3, Trig_FarmTier3_Actions)
end
-- ===========================================================================
--  Trigger: FarmTier3 Res
-- ===========================================================================
---@return boolean
function Trig_FarmTier3_Res_Func002Func002Func001C()
	return ((GetPlayerTechCountSimple(FourCC('R0D4'), GetOwningPlayer(GetTriggerUnit())) == 2)) and ((GetResearched() == FourCC('R0D4')))
end
---@return boolean
function Trig_FarmTier3_Res_Func002Func002Func002C()
	return ((GetPlayerTechCountSimple(FourCC('R04D'), GetOwningPlayer(GetTriggerUnit())) == 4)) and ((GetResearched() == FourCC('R04D')))
end
---@return boolean
function Trig_FarmTier3_Res_Func002Func002Func003C()
	return ((GetPlayerTechCountSimple(FourCC('R0D9'), GetOwningPlayer(GetTriggerUnit())) == 2)) and ((GetResearched() == FourCC('R0D9')))
end
---@return boolean
function Trig_FarmTier3_Res_Func002Func002C()
	if (Trig_FarmTier3_Res_Func002Func002Func001C()) then
		return true
	end
	if (Trig_FarmTier3_Res_Func002Func002Func002C()) then
		return true
	end
	if (Trig_FarmTier3_Res_Func002Func002Func003C()) then
		return true
	end
	return false
end
---@return boolean
function Trig_FarmTier3_Res_Func002C()
	return ((udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] <= 2)) and (Trig_FarmTier3_Res_Func002Func002C())
end
---@return boolean
function Trig_FarmTier3_Res_Conditions()
	return Trig_FarmTier3_Res_Func002C()
end
---@return nothing
function Trig_FarmTier3_Res_Actions()
	udg_TierLevel[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))] = 3
	udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
	DisplayTextToForce(GetForceOfPlayer(udg_LocalPlayer), "TRIGSTR_683")
	udg_LocalInteger = 15
	SetPlayerTechMaxAllowedSwap(FourCC('w219'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('cD12'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 12
	
	SetPlayerTechMaxAllowedSwap(FourCC('h0HU'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 30
	SetPlayerTechMaxAllowedSwap(FourCC('h0DT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0OE'), udg_LocalInteger, udg_LocalPlayer)	--  ????? ?????????
	udg_LocalInteger = 45
	SetPlayerTechMaxAllowedSwap(FourCC('h0N2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0H2'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05Y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h05C'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h024'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h031'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h04M'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h00A'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o003'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o00T'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0BT'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u00H'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0MV'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e00N'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('emow'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('e02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0CE'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0DS'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EX'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0F9'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0FL'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0EC'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('otrb'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('u02E'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0JD'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('hhou'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o036'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('w20y'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('o060'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h0IM'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 60
	SetPlayerTechMaxAllowedSwap(FourCC('u019'), udg_LocalInteger, udg_LocalPlayer)
	SetPlayerTechMaxAllowedSwap(FourCC('h077'), udg_LocalInteger, udg_LocalPlayer)
	udg_LocalInteger = 90
	SetPlayerTechMaxAllowedSwap(FourCC('e01J'), udg_LocalInteger, udg_LocalPlayer)
	FaselessFarmLimit(GetOwningPlayer(GetTriggerUnit()))
end
-- ===========================================================================
---@return nothing
function InitTrig_FarmTier3_Res()
	gg_trg_FarmTier3_Res = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FarmTier3_Res, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
	TriggerAddCondition(gg_trg_FarmTier3_Res, Condition(Trig_FarmTier3_Res_Conditions))
	TriggerAddAction(gg_trg_FarmTier3_Res, Trig_FarmTier3_Res_Actions)
end
-- ===========================================================================
--  Trigger: TLimit
-- ===========================================================================
---@return boolean
function Trig_TLimit_Conditions()
	return (GetUnitAbilityLevelSwapped(FourCC('A0IQ'), GetConstructedStructure()) ~= 0)
end
---@return nothing
function Trig_TLimit_Actions()
	SetPlayerTechMaxAllowedSwap(GetUnitTypeId(GetConstructedStructure()), 15, GetOwningPlayer(GetTriggerUnit()))
end
-- ===========================================================================
---@return nothing
function InitTrig_TLimit()
	gg_trg_TLimit = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_TLimit, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
	TriggerAddCondition(gg_trg_TLimit, Condition(Trig_TLimit_Conditions))
	TriggerAddAction(gg_trg_TLimit, Trig_TLimit_Actions)
end
-- ===========================================================================
--  Trigger: GnomeNotToMuch
-- 
--  ?????????? ????????? ???? ????????(
-- ===========================================================================
---@return boolean
---@return boolean
function Type_1()
	return GetUnitTypeId(GetFilterUnit()) == FourCC('h0FL')
end
---@return nothing
function FG()
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	BlzEndUnitAbilityCooldown(GetEnumUnit(), FourCC('A0SG'))
	IssueImmediateOrder(GetEnumUnit(), "ravenform")
	income[pi] = (income[pi] - 40)
end
---@return nothing
function Trig_GnomeNotToMuch_Actions()
	local p = GetOwningPlayer(GetTriggerUnit())
	local pi = GetPlayerId(p)
	local Tl = udg_TierLevel[GetConvertedPlayerId(p)]
	udg_Boolexpr = Type_1
	
	if GetUnitTypeId(GetTriggerUnit()) ~= FourCC('h0FL') then	--  ???????? ??? ?????
		income[pi] = (income[pi] + 40)
		
		
		udg_LocalText2 = "???????? ?????. ????????? ????? ??????? ?????."
		GroupEnumUnitsOfPlayer(udg_LocalOtrad, p, udg_Boolexpr)
		udg_LocalInteger = CountUnitsInGroup(udg_LocalOtrad)
		if Tl == 1 and udg_LocalInteger >= 15 then
			
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			
			udg_LocalInteger2 = (udg_LocalInteger - 15 + 1)
			udg_LocalOtrad2 = GetRandomSubGroup(udg_LocalInteger2, udg_LocalOtrad)
			ForGroupBJ(udg_LocalOtrad2, FG)
		elseif Tl == 2 and udg_LocalInteger >= 30 then
			
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			udg_LocalInteger2 = (udg_LocalInteger - 30 + 1)
			udg_LocalOtrad2 = GetRandomSubGroup(udg_LocalInteger2, udg_LocalOtrad)
			ForGroupBJ(udg_LocalOtrad2, FG)
		elseif Tl == 3 and udg_LocalInteger >= 45 then
			
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			
			udg_LocalInteger2 = (udg_LocalInteger - 45 + 1)
			udg_LocalOtrad2 = GetRandomSubGroup(udg_LocalInteger2, udg_LocalOtrad)
			ForGroupBJ(udg_LocalOtrad2, FG)
			
		else
			-- nothing
			
		end
		GroupClear(udg_LocalOtrad)
		GroupClear(udg_LocalOtrad2)
	else
		income[pi] = income[pi] - 40
	end
	
	
	UpdateGraf(pi)
	
end
-- ===========================================================================
---@return nothing
function InitTrig_GnomeNotToMuch()
	gg_trg_GnomeNotToMuch = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_GnomeNotToMuch, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GnomeNotToMuch, function()
        if GetSpellAbilityId() ~= FourCC('A0SG') then return end
        Trig_GnomeNotToMuch_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Moneta C
-- ===========================================================================
---@return boolean
function Trig_Moneta_C_Conditions()
	return GetUnitTypeId(GetSoldUnit()) == FourCC('h0G8')
end
---@return nothing
function Trig_Moneta_C_Actions()
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	-- call KillUnit( GetSoldUnit() )
	RemoveUnit(GetSoldUnit())
	
	income[pi] = income[pi] + 75
	UpdateGraf(pi)
	
	
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0SM')) == 0 then
		UnitAddAbility(GetTriggerUnit(), FourCC('A0SM'))
		udg_LocalUnit2 = GetTriggerUnit()
		UnitMakeAbilityPermanent(udg_LocalUnit2, true, FourCC('A0SM'))
	else
		IncUnitAbilityLevel(GetTriggerUnit(), FourCC('A0SM'))
	end
end
-- ===========================================================================
---@return nothing
function InitTrig_Moneta_C()
	gg_trg_Moneta_C = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Moneta_C, EVENT_PLAYER_UNIT_SELL)
	TriggerAddCondition(gg_trg_Moneta_C, Condition(Trig_Moneta_C_Conditions))
	TriggerAddAction(gg_trg_Moneta_C, Trig_Moneta_C_Actions)
end
-- ===========================================================================
--  Trigger: InitForEconomics
-- ===========================================================================
---@return boolean
function f_IncomeBuildings()
	return GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0 and GetUnitFoodMade(GetFilterUnit()) >= 1 and IsUnitInGroup(GetFilterUnit(), udg_BuildedSctructure[1])
end
---@return boolean
function f_IncomeLumber()
	return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0B5')) >= 1
end
---@return boolean
function f_DisFilter()
	return IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE) == false and GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0
end
---@return nothing
function Trig_InitForEconomics_Actions()
	IncomeBuildings = Condition(f_IncomeBuildings)
	IncomeLumber = Condition(f_IncomeLumber)
	DisFilter = Condition(f_DisFilter)
end
-- ===========================================================================
---@return nothing
function InitTrig_InitForEconomics()
	gg_trg_InitForEconomics = CreateTrigger()
	TriggerAddAction(gg_trg_InitForEconomics, Trig_InitForEconomics_Actions)
end
-- ===========================================================================
--  Trigger: TimerIncome
-- ===========================================================================
---@return nothing
function Trig_TimerIncome_Actions()
	local i = 0
	local r
	local p
	local t = 0
	
	while true do
		if i >= 24 then break end
		p = Player(i)
		
		if DisOn then
			
			
			--  ---------------------------??????? ????????????????-----------------------------
			-- set logistic[i] = 500*R2I( udg_UnitsCount[i]/ 50.00 )
			-- set logistic[i] = 250*R2I( udg_UnitsCount[i]/ 25.00 )
			-- ?????? ??????
			
			
			r = R2I(udg_UnitsCount[i] / 25.00)
			logistic[i] = ((500 + 100 * (r - 1)) / 2 * r)	--  ??????????
			
			
			--  ---------------------------??????? ?????????-----------------------------
			t = GetPlayerTechCount(p, FourCC('R04O'), true)
			if t > 1 then
				corruption[i] = (disincome[i] * ((t - 1) * 0.15))
				if EcLog then
					udg_LocalText2 = ("?????????" .. I2S(R2I(corruption[i])))
					DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
				end
				
			end
			
			-- ????? ??????????? ????????
			t = GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true)
			if t >= 1 then
				additional[i] = disincome[i] * (udg_MainPrice[i] / (-100.0))
				if EcLog then
					udg_LocalText2 = ("?????????????: " .. I2S(R2I(additional[i])))
					DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
				end
				
			end
			
			balance[i] = income[i] * (IncomeMod - AllyTax[i]) - disincome[i] - logistic[i] + corruption[i] + additional[i]
		else
			balance[i] = income[i] * (IncomeMod - AllyTax[i])
		end
		
		
		
		
		if EcLog then
			udg_LocalText2 = ("?????: " .. R2S(income[i] * IncomeMod))
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			udg_LocalText2 = ("??????: " .. R2S(disincome[i]))
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			udg_LocalText2 = ("?????????: " .. R2S(logistic[i]))
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			udg_LocalText2 = ("??????: " .. I2S(udg_UnitsCount[i]))
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			udg_LocalText2 = ("?????: " .. R2S(balance[i]))
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
			udg_LocalText2 = ("?????????: " .. R2S(incomeW[i]))
			DisplayTimedTextToPlayer(p, 0, 0, 7, udg_LocalText2)
		end
		
		SetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(p, PLAYER_STATE_RESOURCE_GOLD) + R2I(balance[i]))
		SetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(p, PLAYER_STATE_RESOURCE_LUMBER) + R2I(incomeW[i]))
		ArmyExpSetBonus(i)
		
		i = i + 1
	end
	
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_TimerIncome()
	gg_trg_TimerIncome = CreateTrigger()
	TriggerRegisterTimerExpireEventBJ(gg_trg_TimerIncome, udg_IncomeTimerSecond)
	TriggerAddAction(gg_trg_TimerIncome, Trig_TimerIncome_Actions)
end
-- ===========================================================================
--  Trigger: EclogOn
-- ===========================================================================
---@return nothing
function Trig_EclogOn_Actions()
	EcLog = true
end
-- ===========================================================================
---@return nothing
function InitTrig_EclogOn()
	gg_trg_EclogOn = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_EclogOn, Player(0), "-EcLogOn", true)
	TriggerAddAction(gg_trg_EclogOn, Trig_EclogOn_Actions)
end
-- ===========================================================================
--  Trigger: EclogOff
-- ===========================================================================
---@return nothing
function Trig_EclogOff_Actions()
	EcLog = false
end
-- ===========================================================================
---@return nothing
function InitTrig_EclogOff()
	gg_trg_EclogOff = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_EclogOff, Player(0), "-EcLogOff", true)
	TriggerAddAction(gg_trg_EclogOff, Trig_EclogOff_Actions)
end
-- ===========================================================================
--  Trigger: UnitEnterMap
-- 
--  ??? ?????????????
-- ===========================================================================
---@return boolean
function Trig_UnitEnterMap_Conditions()
	gTriggerUnit = GetEnteringUnit()
	return GetUnitAbilityLevel(gTriggerUnit, FourCC('A0Z5')) == 0	-- ???????? ?? ??????? ??? ????? ??? ?????????
end
---@return nothing
function Trig_UnitEnterMap_Actions()
	
	if GetUnitState(gTriggerUnit, UNIT_STATE_LIFE) < 0.7 then
		if  not IsUnitInGroup(gTriggerUnit, DeadGroup) then
			GroupAddUnit(DeadGroup, gTriggerUnit)
			TriggerRegisterUnitStateEvent(gg_trg_UnitRevive, gTriggerUnit, UNIT_STATE_LIFE, GREATER_THAN, 0.60)
		end
		
		return 
	end
	
	AddCountDis(gTriggerUnit, GetPlayerId(GetOwningPlayer(gTriggerUnit)))
	
end
-- ===========================================================================
---@return nothing
function InitTrig_UnitEnterMap()
	gg_trg_UnitEnterMap = CreateTrigger()
	-- call TriggerRegisterEnterRegion( gg_trg_UnitEnterMap, Allmap,nil)
	TriggerRegisterEnterRectSimple(gg_trg_UnitEnterMap, GetPlayableMapRect())
	TriggerAddCondition(gg_trg_UnitEnterMap, Condition(Trig_UnitEnterMap_Conditions))
	TriggerAddAction(gg_trg_UnitEnterMap, Trig_UnitEnterMap_Actions)
end
-- ===========================================================================
--  Trigger: UnitBuilded
-- ===========================================================================
---@return boolean
function Trig_UnitBuilded_Conditions()
	return GetUnitState(GetConstructedStructure(), UNIT_STATE_LIFE) > 0 and GetUnitFoodMade(GetConstructedStructure()) >= 1	--  and IsUnitInGroup(GetConstructedStructure(), udg_BuildedSctructure[1])
end
---@return nothing
function Trig_UnitBuilded_Actions()
	local u = GetConstructedStructure()
	local p = GetOwningPlayer(u)
	local pi = GetPlayerId(p)
	
	GroupAddUnit(udg_BuildedSctructure[1], u)
	AddCountDis(u, pi)
	
	
	u = nil
end
-- ===========================================================================
---@return nothing
function InitTrig_UnitBuilded()
	gg_trg_UnitBuilded = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_UnitBuilded, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
	TriggerAddCondition(gg_trg_UnitBuilded, Condition(Trig_UnitBuilded_Conditions))
	TriggerAddAction(gg_trg_UnitBuilded, Trig_UnitBuilded_Actions)
end
-- ===========================================================================
--  Trigger: UnitUpgraded
-- ===========================================================================
---@return boolean
function Trig_UnitUpgraded_Conditions()
	return GetUnitState(GetTriggerUnit(), UNIT_STATE_LIFE) > 0 and GetUnitFoodMade(GetTriggerUnit()) >= 1
end
---@return nothing
function Trig_UnitUpgraded_Actions()
	local u = GetTriggerUnit()
	local p = GetOwningPlayer(u)
	local pi = GetPlayerId(p)
	local i = GetUnitFoodMade(u)
	
	-- ???????? ?????
	
	
	if GetUnitAbilityLevel(u, FourCC('A0LJ')) >= 1 then
		if i == 200 then
			income[pi] = income[pi] + 170
		elseif i == 300 then
			income[pi] = income[pi] + 100
			
		end
		
	elseif GetUnitTypeId(u) == FourCC('h0HU') then
		income[pi] = income[pi] + 35
	end
	
	
	UpdateGraf(pi)
	
	
	u = nil
end
-- ===========================================================================
---@return nothing
function InitTrig_UnitUpgraded()
	gg_trg_UnitUpgraded = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_UnitUpgraded, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
	TriggerAddCondition(gg_trg_UnitUpgraded, Condition(Trig_UnitUpgraded_Conditions))
	TriggerAddAction(gg_trg_UnitUpgraded, Trig_UnitUpgraded_Actions)
end
-- ===========================================================================
--  Trigger: UnitDead
-- ===========================================================================
---@return boolean
function DeadAddCheck_Conditions()
	return GetTriggerUnit() ~= nil and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0Z5')) == 0
	
end
---@return nothing
function Trig_UnitDead_Actions()
	local u = GetTriggerUnit()
	local p = GetOwningPlayer(u)
	local pi = GetPlayerId(p)
	
	addArmyExp(u, GetPlayerId(GetOwningPlayer(GetKillingUnit())))
	if GetUnitAbilityLevel(u, FourCC('BUan')) == 0 then
		DelCountDis(u, pi)
	else
		TimedCount(u)	-- ????????? ????????? ????? 0.3
	end
	
	
	
	
	SetUnitLifeBJ(u, 0)
	if  not IsUnitInGroup(u, DeadGroup) then
		GroupAddUnit(DeadGroup, u)
		TriggerRegisterUnitStateEvent(gg_trg_UnitRevive, u, UNIT_STATE_LIFE, GREATER_THAN, 0.01)
	end
	u = nil
	
	
		--     //?????? ??? ?????
	--    // call DisplayTextToPlayer(p,0,0,("?????? ?????? "+GetUnitName(u)))
	--     //??????
	--     if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
	--         if IsUnitInGroup(u, udg_BuildedSctructure[1]) then
	--             set income[pi] = income[pi] - I2R(GetUnitFoodMade(u)) 
	--             if GetUnitAbilityLevel(u,'A0AY') >= 1 then
	--                     set income[pi] = ( income[pi] - ( 100.00 * I2R(GetUnitAbilityLevel(u,'A0AY')) ) )
	--             elseif GetUnitAbilityLevel(u,'A0SM') >= 1 then
	--                 set income[pi] = ( income[pi] - ( 75.00 * I2R(GetUnitAbilityLevel(u,'A0SM')) ) )
	--             endif
	--             
	--             if GetUnitAbilityLevel(u,'A0VS') == 1 then
	--                 set income[pi] = ( income[pi] - 100 )
	--             endif
	--             
	--             set i = GetUnitAbilityLevel(u, 'A0B5')
	--             if i>0 then
	--                 set incomeW[pi] =  incomeW[pi] - ( 50.00 * i ) 
	--             endif
	--         endif
	--     //???
	--     elseif IsUnitType(u, UNIT_TYPE_HERO) then
	--             set disincome[pi] = ( disincome[pi] - 100.00 )
	--             set udg_UnitsCount[pi] = udg_UnitsCount[pi] - 1
	--             if  GetUnitAbilityLevel(u,'A0ZT')!=0 then        
	--                     set income[pi] = income[pi] - (100+GetUnitAbilityLevel(u,'A0ZT')*100)
	--             endif
	--     //????
	--     elseif GetTriggerUnit()!=nil then
	--             
	--             if not IsUnitType(u, UNIT_TYPE_SUMMONED) then
	--                // call DisplayTextToPlayer(p,0,0,("?????? ?????? ?? ????? "+GetUnitName(u)))
	--                 set udg_Price = GetUnitGoldCost(GetUnitTypeId(u))
	--                 set disincome[pi] = ( disincome[pi] - ( udg_Price * Tax ) )
	--                 set udg_UnitsCount[pi] = udg_UnitsCount[pi] - 1
	--                 
	--                 // ---------------------------?????? ???????-----------------------------          +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	--                 // ---------------------------??????? ????????-----------------------------
	--                 if GetUnitAbilityLevel(u,'A0A5') != 0 then
	--                     set disincome[pi] = disincome[pi] - ( ( udg_Price * Tax ) * ( 1.60 - ( 0.10 * I2R(GetUnitAbilityLevel(u,'A0A5')) ) ) )	--                 // ---------------------------????????? ?????????------------------------- ??
	--                 elseif GetUnitAbilityLevel(u,'A0VH') == 1 then
	--                     set disincome[pi] = disincome[pi] + ( udg_Price * Tax / 2  )
	--                 elseif GetUnitAbilityLevel(u,'A0VH') == 2 then
	--                     set disincome[pi] = disincome[pi] + ( udg_Price * Tax / 3 * 2  )
	--                 elseif  GetUnitAbilityLevel(u,'OR00')!=0 then
	--                     set disincome[pi] = disincome[pi] - (( udg_Price * Tax ) * (( GetUnitAbilityLevel(u,'OR00')-35 )/100.0))
	--                     //Horde land
	--                 elseif  GetUnitAbilityLevel(u,'OR00')!=0 then                  
	--                     set disincome[pi] = disincome[pi] - ( ( udg_Price * Tax ) * ( ( GetUnitAbilityLevel(u,'OR00')-35 )/100.0) )
	--                 
	--                 endif
	--             endif
	--     endif
	--     
	--      
	--     call MultiboardSetItemValue( MultiboardItem[ MultiboardItemOwnerIndex[ pi ] * 2+1], I2S( udg_UnitsCount[pi] ) )
	--     
	--     
	--     call UpdateGraf(pi)
	
	
	
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_UnitDead()
	gg_trg_UnitDead = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_UnitDead, EVENT_PLAYER_UNIT_DEATH)
	TriggerAddCondition(gg_trg_UnitDead, Condition(DeadAddCheck_Conditions))
	TriggerAddAction(gg_trg_UnitDead, Trig_UnitDead_Actions)
end
-- ===========================================================================
--  Trigger: UnitRevive
-- ===========================================================================
---@return boolean
function Trig_UnitRevive_Conditions()
	return UnitAlive(GetTriggerUnit()) and  not IsUnitType(GetTriggerUnit(), UNIT_TYPE_SUMMONED)	--  GetUnitAbilityLevel(GetTriggerUnit(), FourCC('BUan')) <= 0 and
end
---@return nothing
function Trig_UnitRevive_Actions()
	local u = GetTriggerUnit()
	local p = GetOwningPlayer(u)
	local pi = GetPlayerId(p)
	
	
	AddCountDis(u, pi)
	
	
	
	
	--     set udg_UnitsCount[pi]=udg_UnitsCount[pi]+1	--     call Enter(u)
	--     
	--     if IsUnitType(u, UNIT_TYPE_HERO) then
	--         set disincome[pi] = ( disincome[pi] + 100.00 )
	--         if  GetUnitAbilityLevel(u,'A0ZT')!=0 then        
	--             set income[pi] = income[pi] + (100+GetUnitAbilityLevel(u,'A0ZT')*100)
	--        
	--         endif
	--     else
	--         set udg_Price = GetUnitGoldCost(GetUnitTypeId(u))
	--         set disincome[pi] = ( disincome[pi] + ( udg_Price * Tax ) )
	--         
	--         // ---------------------------?????? ???????-----------------------------          +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	--         // ---------------------------??????? ????????-----------------------------
	--         if GetUnitAbilityLevel(u,'A0A5') != 0 then
	--             set disincome[pi] = disincome[pi] + ( ( udg_Price * Tax ) * ( 1.60 - ( 0.10 * I2R(GetUnitAbilityLevel(u,'A0A5')) ) ) )	--         // ---------------------------????????? ?????????-------------------------
	--         elseif GetUnitAbilityLevel(u,'A0VH') == 1 then
	--             set disincome[pi] = disincome[pi] + ( udg_Price * Tax / 2  )
	--         elseif GetUnitAbilityLevel(u,'A0VH') == 2 then
	--             set disincome[pi] = disincome[pi] + ( udg_Price * Tax / 3 * 2  )
	--         
	--          //Horde land
	--         elseif  GetUnitAbilityLevel(u,'OR00')!=0 then
	--             set disincome[pi] = disincome[pi] + ( udg_Price * Tax ) * (( GetUnitAbilityLevel(u,'OR00')-35 )/100)
	--         endif
	--     endif	--  	--     call UpdateGraf(pi)
	
	
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_UnitRevive()
	gg_trg_UnitRevive = CreateTrigger()
	TriggerAddCondition(gg_trg_UnitRevive, Condition(Trig_UnitRevive_Conditions))
	TriggerAddAction(gg_trg_UnitRevive, Trig_UnitRevive_Actions)
end
-- ===========================================================================
--  Trigger: RepEc
-- ===========================================================================
---@return nothing
function FixEcEnum()
	local u = GetEnumUnit()
	local pi = GetPlayerId(GetOwningPlayer(u))
	
	if GetUnitAbilityLevel(u, FourCC('AHad')) > 0 then
		CityPlayerCount[pi] = CityPlayerCount[pi] + 1
	end
	
	AddCountDis(u, pi)
	u = nil
end
---@return boolean
function UnitAliveBool()
	return UnitAlive(GetFilterUnit())
	
end
---@param pi integer
---@return nothing
function FixEc(pi)
	local r
	local g = CreateGroup()
	ClearEc(pi)
	
	
	GroupEnumUnitsOfPlayer(g, Player(pi), b)
	ForGroup(g, FixEcEnum)
	
	if udg_GameMode == 3 then
		PercentGraph(pi)
	end
	
	
	DestroyGroup(g)
	g = nil
	DestroyBoolExpr(b)
	b = nil
end
---@return nothing
function FixEcAll()
	local i = 0
	-- local timer t = GetExpiredTimer()
	
	
	while true do
		if i >= 23 then break end
		
		FixEc(i)
		DisplayTextToPlayer(Player(i), 0, 0, "????????? ???? ??????? ??????????? ????? ???????? ?????????????? ?????, ??? ???????????????? ???????")
		i = i + 1
	end
	
	
end
---@return nothing
function Trig_RepEc_Actions()
	
	local pi = GetPlayerId(GetTriggerPlayer())
	FixEc(pi)
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_RepEc()
	local i = 0
	local t = CreateTimer()
	gg_trg_RepEc = CreateTrigger()
	while true do
		if i >= 24 then break end
		TriggerRegisterPlayerChatEvent(gg_trg_RepEc, Player(i), "-repec", true)
		i = i + 1
		
	end
	
	
	TriggerAddAction(gg_trg_RepEc, Trig_RepEc_Actions)
	TimerStart(t, 60 * 7, true, FixEcAll)
end
-- ===========================================================================
--  Trigger: Gob Potreblenie
-- 
--  ???? ?? ?????)
-- ===========================================================================
---@return boolean
function Trig_Gob_Potreblenie_Conditions()
	return GetResearched() == FourCC('R04N')
end
---@return boolean
function Trig_Gob_Potreblenie_Func001002()
	return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0A5')) ~= 0
end
---@return nothing
function Trig_Gob_Potreblenie_Actions()
	local g = CreateGroup()
	local p = GetOwningPlayer(GetTriggerUnit())
	local pi = GetPlayerId(p)
	local u
	local r = GetPlayerTechCount(p, FourCC('R04N'), true)
	udg_Boolexpr = Trig_Gob_Potreblenie_Func001002
	GroupEnumUnitsOfPlayer(g, p, udg_Boolexpr)
	while true do
		u = FirstOfGroup(g)
		if u == nil then break end
		
		udg_Price = GetUnitGoldCost(GetUnitTypeId(u)) or 0
		if GetUnitAbilityLevel(u, FourCC('A0A5')) ~= 0 then
			disincome[pi] = disincome[pi] - (udg_Price * Tax) * (1.60 - (0.10 * (r - 1)))
			disincome[pi] = disincome[pi] + (udg_Price * Tax) * (1.60 - (0.10 * r))
		end
		
		
		
		GroupRemoveUnit(g, u)
	end
	UpdateGraf(pi)
	GroupClear(udg_LocalOtrad2)
	
	GroupClear(g)
	DestroyGroup(g)
	u = nil
	g = nil
end
-- ===========================================================================
---@return nothing
function InitTrig_Gob_Potreblenie()
	gg_trg_Gob_Potreblenie = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Gob_Potreblenie, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
	TriggerAddCondition(gg_trg_Gob_Potreblenie, Condition(Trig_Gob_Potreblenie_Conditions))
	TriggerAddAction(gg_trg_Gob_Potreblenie, Trig_Gob_Potreblenie_Actions)
end
-- ===========================================================================
--  Trigger: Silitid Potreblenie
-- 
--  ???? ?? ?????)
-- ===========================================================================
---@return boolean
function Trig_Silitid_Potreblenie_Conditions()
	return GetResearched() == FourCC('R089')
end
---@return boolean
function HaveSilitidSpell()
	return GetUnitTypeId(GetFilterUnit()) == FourCC('e02W')
	-- return ( GetUnitAbilityLevelSwapped('A0VH', GetFilterUnit()) >=1 )
end
---@return nothing
function Trig_Silitid_Potreblenie_Actions()
	local g = CreateGroup()
	local p = GetOwningPlayer(GetTriggerUnit())
	local pi = GetPlayerId(p)
	local u
	local r = GetPlayerTechCount(p, FourCC('R04N'), true)
	udg_Boolexpr = HaveSilitidSpell
	GroupEnumUnitsOfPlayer(g, p, udg_Boolexpr)
	while true do
		u = FirstOfGroup(g)
		if u == nil then break end
		
		udg_Price = GetUnitGoldCost(GetUnitTypeId(u)) or 0
		disincome[pi] = disincome[pi] - (udg_Price * Tax / 2)
		disincome[pi] = disincome[pi] + (udg_Price * Tax / 3)
		
		GroupRemoveUnit(g, u)
	end
	GroupClear(udg_LocalOtrad2)
	UpdateGraf(pi)
	GroupClear(g)
	DestroyGroup(g)
	u = nil
	g = nil
	p = nil
end
-- ===========================================================================
---@return nothing
function InitTrig_Silitid_Potreblenie()
	gg_trg_Silitid_Potreblenie = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Silitid_Potreblenie, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
	TriggerAddCondition(gg_trg_Silitid_Potreblenie, Condition(Trig_Silitid_Potreblenie_Conditions))
	TriggerAddAction(gg_trg_Silitid_Potreblenie, Trig_Silitid_Potreblenie_Actions)
end
-- ===========================================================================
--  Trigger: LimitEnd
-- ===========================================================================
---@return nothing
function Trig_LimitEnd_Actions()
	DisableTrigger(gg_trg_LimitGolda)
	DisableTrigger(gg_trg_LimitDereva)
end
-- ===========================================================================
---@return nothing
function InitTrig_LimitEnd()
	gg_trg_LimitEnd = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_LimitEnd, Player(0), "-limitend", true)
	TriggerAddAction(gg_trg_LimitEnd, Trig_LimitEnd_Actions)
end
-- ===========================================================================
--  Trigger: LimitGolda
-- ===========================================================================
---@return nothing
function Trig_LimitGolda_Actions()
	SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD, 25000)
end
-- ===========================================================================
---@return nothing
function InitTrig_LimitGolda()
	local i = 0
	gg_trg_LimitGolda = CreateTrigger()
	while true do
		if i >= 23 then break end
		TriggerRegisterPlayerStateEvent(gg_trg_LimitGolda, Player(i), PLAYER_STATE_RESOURCE_GOLD, GREATER_THAN, 25000.00)
		i = i + 1
	end
	TriggerAddAction(gg_trg_LimitGolda, Trig_LimitGolda_Actions)
end
-- ===========================================================================
--  Trigger: LimitDereva
-- ===========================================================================
---@return nothing
function Trig_LimitDereva_Actions()
	SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER, 25000)
end
-- ===========================================================================
---@return nothing
function InitTrig_LimitDereva()
	local i = 0
	gg_trg_LimitDereva = CreateTrigger()
	while true do
		if i >= 23 then break end
		TriggerRegisterPlayerStateEvent(gg_trg_LimitDereva, Player(i), PLAYER_STATE_RESOURCE_LUMBER, GREATER_THAN, 25000.00)
		i = i + 1
	end
	TriggerAddAction(gg_trg_LimitDereva, Trig_LimitDereva_Actions)
end
-- ===========================================================================
--  Trigger: Cities Start 2
-- 
--  ?????? ? ?????? ??????????? ??????
-- ===========================================================================
---@return boolean
function ItIsCity()
	return GetUnitAbilityLevel(GetFilterUnit(), FourCC('AHad')) == 1 and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Awrp')) == 0
end
---@return nothing
function Trig_Cities_Start_2_Func003A()
	local u = GetEnumUnit()
	local id = GetUnitTypeId(u)
	CityCount = CityCount + 1
	BlzSetUnitArmor(u, 3)
	SetUnitState(u, UNIT_STATE_LIFE, 5000)
	GroupAddUnit(udg_ZahvatBuildings, u)
	GroupAddUnit(udg_BuildedSctructure[1], u)
	if (id == FourCC('h08A') or id == FourCC('h08A') or id == FourCC('h004') or id == FourCC('h0B3') or id == FourCC('h081') or id == FourCC('h0AP') or id == FourCC('h00G') or id == FourCC('h08G') or id == FourCC('h05O') or id == FourCC('h089') or id == FourCC('h0AG') or id == FourCC('h097') or id == FourCC('h09Z') or id == FourCC('h088') or id == FourCC('h094') or id == FourCC('h00F') or id == FourCC('h09P') or id == FourCC('h00F') or id == FourCC('h0BB') or id == FourCC('h0E3') or id == FourCC('h06I')) then
		GroupAddUnit(PortalBuildingAi, u)
	end
	u = nil
end
---@return nothing
function Trig_Cities_Start_2_Actions()
	GroupEnumUnitsInRect(udg_LocalOtrad2, bj_mapInitialPlayableArea, Condition(ItIsCity))
	ForGroup(udg_LocalOtrad2, Trig_Cities_Start_2_Func003A)
	GroupClear(udg_LocalOtrad2)
end
-- ===========================================================================
---@return nothing
function InitTrig_Cities_Start_2()
	local i = 0
	gg_trg_Cities_Start_2 = CreateTrigger()
	TriggerRegisterTimerEvent(gg_trg_Cities_Start_2, 0.01, false)
	TriggerAddAction(gg_trg_Cities_Start_2, Trig_Cities_Start_2_Actions)
	
	while true do
		if i > 23 then break end
		
		CityPlayerCount[i] = 0
		i = i + 1
	end
	
end
-- ===========================================================================
--  Trigger: DeadSituastion
-- ===========================================================================
---@return boolean
function Trig_DeadSituastion_Conditions()
	return IsUnitInGroup(GetTriggerUnit(), udg_ZahvatBuildings)
end
---@return nothing
function Trig_DeadSituastion_Actions()
	local u = GetTriggerUnit()
	local u2
	local id = GetUnitTypeId(u)
	local u3 = GetKillingUnit()
	local p = GetOwningPlayer(u3)
	if p == nil then
		p = Player(PLAYER_NEUTRAL_AGGRESSIVE)
	end
	local pi0 = GetPlayerId(GetOwningPlayer(u))
	local pi = GetPlayerId(p)
	local i
	
	
	-- ??? ?????? ?????????
	
	CityPlayerCount[pi0] = (CityPlayerCount[pi0] or 0) - 1
	CityPlayerCount[pi] = (CityPlayerCount[pi] or 0) + 1
	PercentGraph(pi0)
	PercentGraph(pi)
	if udg_GameMode == 3 or udg_GameMode == 5 then
		CheckCity(p)
	end
	
	-- ????? ???????? ?????????? ????? ?????.
	u2 = CreateUnit(p, GetUnitTypeId(u), GetUnitX(u), GetUnitY(u), GetUnitFacing(u))
	GroupAddUnit(udg_ZahvatBuildings, u2)
	BlzSetUnitArmor(u2, 3)
	SetUnitState(u2, UNIT_STATE_LIFE, 5000)
	GroupAddUnit(udg_BuildedSctructure[1], u2)
	
	-- ??????? ??? ????? ??????
	if GetUnitAbilityLevel(u, FourCC('A1MS')) == 0 then
		UnitAddAbility(u2, FourCC('A0VJ'))
	end
	
	UnitRemoveAbility(u2, FourCC('A0B2'))
	UnitRemoveAbility(u2, FourCC('A0B0'))
	UnitRemoveAbility(u2, FourCC('A0MK'))
	
	
	
	
	
	
	
	
	
	-- ???????? ?? ?????????? ?????
	if IsUnitInGroup(u, udg_CityNearWater) then
		GroupRemoveUnit(udg_CityNearWater, u)
		GroupAddUnit(udg_CityNearWater, u2)
	end
	
	-- ???????? ?? ??
	if IsUnitInGroup(u, PortalBuildingAi) then
		GroupAddUnit(PortalBuildingAi, u2)
		
		if udg_AiControl[pi] then
			UnitAddAbility(u2, FourCC('A0Y4'))
			GroupAddUnit(AiUnitsToPort[pi], u2)
			if Random(1, 3) then
				PortTo(u2)
			end
		end
	elseif udg_AiControl[pi] then
		aiKilledCity(u3)
	end
	
	
	u = nil
	u3 = nil
	
	-- ??????????
	if GetUnitAbilityLevel(u2, FourCC('A1MS')) == 0 then
		TimedUpdate(u2, p)
	end
	
	u2 = nil
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_DeadSituastion()
	gg_trg_DeadSituastion = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_DeadSituastion, EVENT_PLAYER_UNIT_DEATH)
	TriggerAddCondition(gg_trg_DeadSituastion, Condition(Trig_DeadSituastion_Conditions))
	TriggerAddAction(gg_trg_DeadSituastion, Trig_DeadSituastion_Actions)
end
-- ===========================================================================
--  Trigger: Upgrade Gold C
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_Upgrade_Gold_C_Actions()
	local levels = 4
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	
	-- ???? ????? ?????, -2 ? ?????
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1N9')) > 0 then
		levels = levels - 2
	end
	income[pi] = income[pi] + 100
	
	UpdateGraf(pi)
	
	
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0AY')) == 0 then
		UnitAddAbility(GetTriggerUnit(), FourCC('A0AY'))
		
		return 
	end
	
	
	IncUnitAbilityLevel(GetTriggerUnit(), FourCC('A0AY'))
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0AY')) >= levels then
		UnitRemoveAbility(GetTriggerUnit(), FourCC('A0AZ'))
	end
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_Upgrade_Gold_C()
	gg_trg_Upgrade_Gold_C = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Upgrade_Gold_C, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Upgrade_Gold_C, function()
        if GetSpellAbilityId() ~= FourCC('A0AZ') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_Upgrade_Gold_C_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Upgrade Lumber
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_Upgrade_Lumber_Actions()
	local levels = 4
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	incomeW[pi] = incomeW[pi] + 50.00
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1N9')) > 0 then
		levels = levels - 2
	end
	
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0B5')) == 0 then
		UnitAddAbility(GetTriggerUnit(), FourCC('A0B5'))
		
		return 
		
	end
	
	IncUnitAbilityLevel(GetTriggerUnit(), FourCC('A0B5'))
	
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0B5')) >= levels then
		UnitRemoveAbility(GetTriggerUnit(), FourCC('A0B1'))
	end
	
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_Upgrade_Lumber()
	gg_trg_Upgrade_Lumber = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Upgrade_Lumber, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Upgrade_Lumber, function()
        if GetSpellAbilityId() ~= FourCC('A0B1') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_Upgrade_Lumber_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Upgrade Kontrol
-- ===========================================================================
---@return boolean
function Trig_Upgrade_Kontrol_Conditions()
	return (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit())) == true)
end
---@return nothing
function Trig_Upgrade_Kontrol_Actions()
	UnitAddAbilityBJ(FourCC('A0TW'), GetTriggerUnit())
	BlzUnitDisableAbility(GetTriggerUnit(), FourCC('A0TV'), true, true)
	BlzSetUnitRealFieldBJ(GetTriggerUnit(), UNIT_RF_SIGHT_RADIUS, 6500.00)
	UnitAddTypeBJ(UNIT_TYPE_FLYING, GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0VJ'), GetTriggerUnit())
	
	
	UnitAddAbilityBJ(FourCC('A1M5'), GetTriggerUnit())
	BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1M5'), 5)
	RemoveAbilityTimed(GetTriggerUnit(), FourCC('A1M5'), 5)
	AddAbilityTimed(GetTriggerUnit(), FourCC('A146'), 5)
	
end
-- ===========================================================================
---@return nothing
function InitTrig_Upgrade_Kontrol()
	gg_trg_Upgrade_Kontrol = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Upgrade_Kontrol, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Upgrade_Kontrol, function()
        if GetSpellAbilityId() ~= FourCC('A0VQ') then return end
        if not Trig_Upgrade_Kontrol_Conditions() then return end
        Trig_Upgrade_Kontrol_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Upgrade Razved
-- ===========================================================================
---@return boolean
function Trig_Upgrade_Razved_Conditions()
	return (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit())) == true)
end
---@return nothing
function Trig_Upgrade_Razved_Actions()
	UnitAddAbilityBJ(FourCC('A1C2'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0VJ'), GetTriggerUnit())
	
	UnitAddAbilityBJ(FourCC('A1M5'), GetTriggerUnit())
	BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1M5'), 5)
	RemoveAbilityTimed(GetTriggerUnit(), FourCC('A1M5'), 5)
	AddAbilityTimed(GetTriggerUnit(), FourCC('A146'), 5)
end
-- ===========================================================================
---@return nothing
function InitTrig_Upgrade_Razved()
	gg_trg_Upgrade_Razved = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Upgrade_Razved, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Upgrade_Razved, function()
        if GetSpellAbilityId() ~= FourCC('A0VP') then return end
        if not Trig_Upgrade_Razved_Conditions() then return end
        Trig_Upgrade_Razved_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Razved
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_Razved_Actions()
	udg_LocalPosition2 = GetSpellTargetLoc()
	CreateNUnitsAtLoc(1, FourCC('h0MM'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
	RemoveLocation(udg_LocalPosition2)
	
	UnitAddAbilityBJ(FourCC('A1M5'), GetTriggerUnit())
	BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1M5'), 5)
	RemoveAbilityTimed(GetTriggerUnit(), FourCC('A1M5'), 5)
	AddAbilityTimed(GetTriggerUnit(), FourCC('A146'), 5)
end
-- ===========================================================================
---@return nothing
function InitTrig_Razved()
	gg_trg_Razved = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Razved, EVENT_PLAYER_UNIT_SPELL_CHANNEL)
    TriggerAddAction(gg_trg_Razved, function()
        if GetSpellAbilityId() ~= FourCC('A1C2') then return end
        Trig_Razved_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Upgrade Oborona
-- ===========================================================================
---@return boolean
function Trig_Upgrade_Oborona_Conditions()
	return (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit())) == true)
end
---@return nothing
function Trig_Upgrade_Oborona_Actions()
	UnitAddAbilityBJ(FourCC('A0VR'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0VJ'), GetTriggerUnit())
	
	UnitAddAbilityBJ(FourCC('A1M5'), GetTriggerUnit())
	BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1M5'), 5)
	RemoveAbilityTimed(GetTriggerUnit(), FourCC('A1M5'), 5)
	AddAbilityTimed(GetTriggerUnit(), FourCC('A146'), 5)
end
-- ===========================================================================
---@return nothing
function InitTrig_Upgrade_Oborona()
	gg_trg_Upgrade_Oborona = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Upgrade_Oborona, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Upgrade_Oborona, function()
        if GetSpellAbilityId() ~= FourCC('A0VN') then return end
        if not Trig_Upgrade_Oborona_Conditions() then return end
        Trig_Upgrade_Oborona_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Upgrade Mobile
-- ===========================================================================
---@return boolean
function Trig_Upgrade_Mobile_Conditions()
	return (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit())) == true)
end
---@return nothing
function Trig_Upgrade_Mobile_Actions()
	UnitAddAbilityBJ(FourCC('A0VT'), GetTriggerUnit())
	BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A146'), 5)
	UnitRemoveAbilityBJ(FourCC('A0VJ'), GetTriggerUnit())
	
	UnitAddAbilityBJ(FourCC('A1M5'), GetTriggerUnit())
	BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1M5'), 5)
	RemoveAbilityTimed(GetTriggerUnit(), FourCC('A1M5'), 5)
	AddAbilityTimed(GetTriggerUnit(), FourCC('A146'), 5)
end
-- ===========================================================================
---@return nothing
function InitTrig_Upgrade_Mobile()
	gg_trg_Upgrade_Mobile = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Upgrade_Mobile, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Upgrade_Mobile, function()
        if GetSpellAbilityId() ~= FourCC('A0VO') then return end
        if not Trig_Upgrade_Mobile_Conditions() then return end
        Trig_Upgrade_Mobile_Actions()
    end)
end
-- ===========================================================================
--  Trigger: RazvedEnd
-- ===========================================================================
---@return boolean
---@return boolean
function Trig_RazvedEnd_Func002001003()
	return (GetUnitTypeId(GetFilterUnit()) == FourCC('h0MM'))
end
---@return nothing
function Trig_RazvedEnd_Func002A()
	RemoveUnit(GetEnumUnit())
end
---@return nothing
function Trig_RazvedEnd_Actions()
	local g = CreateGroup()
	GroupEnumUnitsInRange(g, GetSpellTargetX(), GetSpellTargetY(), 1500, Boolexpr)
	
	RemoveUnit(FirstOfGroup(g))
	DestroyGroup(g)
	
	-- set udg_LocalPosition2 = GetSpellTargetLoc()
	--  call ForGroup( GetUnitsInRangeOfLocMatching(25.00, udg_LocalPosition2, Condition(function Trig_RazvedEnd_Func002001003)), function Trig_RazvedEnd_Func002A )
	-- call RemoveLocation(udg_LocalPosition2)
end
-- ===========================================================================
---@return nothing
function InitTrig_RazvedEnd()
	gg_trg_RazvedEnd = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_RazvedEnd, EVENT_PLAYER_UNIT_SPELL_ENDCAST)
    TriggerAddAction(gg_trg_RazvedEnd, function()
        if GetSpellAbilityId() ~= FourCC('A1C2') then return end
        Trig_RazvedEnd_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Upgrade Income
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_Upgrade_Income_Actions()
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	UnitAddAbility(GetTriggerUnit(), FourCC('A0VS'))
	
	
	-- ???????? ?????
	income[pi] = income[pi] + 100
	UpdateGraf(pi)
	
	
	UnitRemoveAbility(GetTriggerUnit(), FourCC('A0VJ'))
	
	UnitAddAbilityBJ(FourCC('A1M5'), GetTriggerUnit())
	BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1M5'), 5)
	RemoveAbilityTimed(GetTriggerUnit(), FourCC('A1M5'), 5)
	AddAbilityTimed(GetTriggerUnit(), FourCC('A146'), 5)
end
-- ===========================================================================
---@return nothing
function InitTrig_Upgrade_Income()
	gg_trg_Upgrade_Income = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Upgrade_Income, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Upgrade_Income, function()
        if GetSpellAbilityId() ~= FourCC('A0VM') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_Upgrade_Income_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Demontag
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_Demontag_Actions()
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	UnitRemoveAbility(GetTriggerUnit(), FourCC('A146'))
	UnitAddAbility(GetTriggerUnit(), FourCC('A0VJ'))
	if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0VS')) == 1 then
		income[pi] = income[pi] - 100
		UnitRemoveAbility(GetTriggerUnit(), FourCC('A0VS'))
	end
	
	UnitRemoveAbility(GetTriggerUnit(), FourCC('A1C2'))
	UnitRemoveAbility(GetTriggerUnit(), FourCC('A0VR'))
	UnitRemoveAbility(GetTriggerUnit(), FourCC('A0VT'))
	UnitRemoveAbility(GetTriggerUnit(), FourCC('A0MK'))
end
-- ===========================================================================
---@return nothing
function InitTrig_Demontag()
