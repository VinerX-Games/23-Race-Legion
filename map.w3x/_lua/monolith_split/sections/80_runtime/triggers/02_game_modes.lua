
-- ===========================================================================
--  Trigger: ResoursesInterface Copy
-- ===========================================================================
---@return nothing
function Trig_ResoursesInterface_Copy_Actions()
	
	local p = GetLocalPlayer()
	local pi = GetPlayerId(p)
	local text
	local text2
	local other = corruption[pi] + additional[pi]
	
	-- if DisOn then
	--   call BlzFrameSetText(BlzGetFrameByName("Income0202",0), I2S(R2I(disincome[pi])))
	--  else
	--  call BlzFrameSetText(BlzGetFrameByName("Income0202",0), "|cffffff00"+I2S(R2I(disincome[pi]))+"(0)|r" )
	--  endif
	
	
	if balance[pi] > 0 then
		BlzFrameSetText(IncomeTextFr, "|cffbeffa0" .. I2S(R2I(balance[pi])))
		BlzFrameSetText(tooltipTitle, "|cffbeffa0????????")
	elseif balance[pi] == 0 then
		BlzFrameSetText(IncomeTextFr, I2S(R2I(balance[pi])))
		BlzFrameSetText(tooltipTitle, "??????? ??????")
	else
		BlzFrameSetText(IncomeTextFr, "|cffffb4a0" .. I2S(R2I(balance[pi])))
		BlzFrameSetText(tooltipTitle, "|cffffb4a0???????")
	end
	-- set balance[pi]=income[pi]-disincome[pi]+corruption[pi]-logistic[pi]+additional[pi]
	
	
	-- ?????
	text = "|cffbeffa0" .. I2S(R2I(income[pi])) .. "*(" .. R2S(IncomeMod) .. "-" .. R2S(AllyTax[pi]) .. ")|r-(|cffffb4a0" .. I2S(R2I(disincome[pi])) .. "|r+|cffffb4a0" .. I2S(R2I(logistic[pi])) .. "|r)"
	if GetPlayerTechCount(p, FourCC('R07E'), true) > 0 then
		text = text .. " + " .. I2S(R2I(corruption[pi]))
	end
	if GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true) > 0 then
		text = text .. " ? " .. I2S(R2I(additional[pi]))
	end
	
	-- ?????????
	text2 = "|n|cffbeffa0?????? * ???. ???? ? ?????|r - (|cffffb4a0???????|r+|cffffb4a0?????????|r)"
	if GetPlayerTechCount(p, FourCC('R07E'), true) > 0 then
		text2 = text2 .. "+?????????"
	end
	
	if GetPlayerTechCount(p, FourCC('R0DV'), true) + GetPlayerTechCount(p, FourCC('R0GZ'), true) > 0 then
		text2 = text2 .. " ? ?????????????"
	end
	-- set text = "?????("+R2S(income[pi])+")-??????("+R2S()+")|n-?????????("+R2S(logistic[pi])+")"+"|n ?????? ???????? ? ??????????"
	BlzFrameSetText(tooltipBody, text .. text2)
	
	
	text = nil
	p = nil
end
-- ===========================================================================
---@return nothing
function InitTrig_ResoursesInterface_Copy()
	gg_trg_ResoursesInterface_Copy = CreateTrigger()
	TriggerRegisterTimerEvent(gg_trg_ResoursesInterface_Copy, 0.10, true)
	TriggerAddAction(gg_trg_ResoursesInterface_Copy, Trig_ResoursesInterface_Copy_Actions)
end
-- ===========================================================================
--  Trigger: MainInfo
-- ===========================================================================
---@return nothing
function Trig_MainInfo_Actions()
	--  ???????
	CreateQuestBJ(bj_QUESTTYPE_REQ_DISCOVERED, "TRIGSTR_20894", "TRIGSTR_20895", "ReplaceableTextures\\CommandButtons\\BTNPhilosophersStone.blp")
	--  ???????
	CreateQuestBJ(bj_QUESTTYPE_OPT_DISCOVERED, "TRIGSTR_20896", "TRIGSTR_20914", "ReplaceableTextures\\CommandButtons\\BTNPhilosophersStone.blp")
	--  ?????????????
	CreateQuestBJ(bj_QUESTTYPE_OPT_DISCOVERED, "TRIGSTR_20922", "TRIGSTR_20987", "ReplaceableTextures\\CommandButtons\\BTNTransmute.blp")
end
-- ===========================================================================
---@return nothing
function InitTrig_MainInfo()
	gg_trg_MainInfo = CreateTrigger()
	TriggerAddAction(gg_trg_MainInfo, Trig_MainInfo_Actions)
end
-- ===========================================================================
--  Trigger: Initial things
-- 
--  ??? ????? ??????? ?????? ???? ???????? ??? ?????????????
-- ===========================================================================
---@return nothing
function Trig_Initial_things_Func003A()
	CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, gg_rct_Shops)
	CameraSetupApplyForPlayer(true, gg_cam_Camera_001, GetEnumPlayer(), 0)
	SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_RESOURCE_LUMBER, 4000)
	SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_RESOURCE_GOLD, 5000)
	SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_FOOD_CAP_CEILING, 3)
	SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_RESOURCE_FOOD_USED, 0)
	CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_MASKED, GetPlayableMapRect())
	udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())] = GetLastCreatedFogModifier()
end
---@return nothing
function Trig_Initial_things_Func019A()
	SetPlayerAbilityAvailableBJ(false, FourCC('A0IQ'), GetEnumPlayer())
end
---@return nothing
function Trig_Initial_things_Actions()
	AllPlayersStart()
	ForForce(udg_AllPlayers, Trig_Initial_things_Func003A)
	SetPlayerStateBJ(Player(PLAYER_NEUTRAL_AGGRESSIVE), PLAYER_STATE_RESOURCE_GOLD, 100000000)
	SetPlayerStateBJ(Player(PLAYER_NEUTRAL_AGGRESSIVE), PLAYER_STATE_RESOURCE_LUMBER, 100000000)
	SetPlayerStateBJ(Player(PLAYER_NEUTRAL_PASSIVE), PLAYER_STATE_RESOURCE_GOLD, 100000)
	SetPlayerStateBJ(Player(PLAYER_NEUTRAL_PASSIVE), PLAYER_STATE_RESOURCE_LUMBER, 100000)
	StartInc()
	InitThings()
	SetStartLocations()
	--  ------------------------------------------
	SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
	SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
	SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
	SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
	SetGameSpeed(MAP_SPEED_FASTEST)
	ForForce(udg_AllPlayers, Trig_Initial_things_Func019A)
end
-- ===========================================================================
---@return nothing
function InitTrig_Initial_things()
	gg_trg_Initial_things = CreateTrigger()
	TriggerAddAction(gg_trg_Initial_things, Trig_Initial_things_Actions)
end
-- ===========================================================================
--  Trigger: StartLobby
-- ===========================================================================
---@return nothing
function Trig_StartLobby_Func004Func001A()
	CameraSetupApplyForPlayer(true, gg_cam_GW1, GetEnumPlayer(), 0)
end
---@return boolean
function Trig_StartLobby_Func004C()
	return udg_LocalInteger == 1
end
---@return nothing
function Trig_StartLobby_Func005Func001A()
	CameraSetupApplyForPlayer(true, gg_cam_GW2, GetEnumPlayer(), 0)
end
---@return boolean
function Trig_StartLobby_Func005C()
	return udg_LocalInteger == 2
end
---@return nothing
function Trig_StartLobby_Func006Func001A()
	CameraSetupApplyForPlayer(true, gg_cam_GW3, GetEnumPlayer(), 0)
end
---@return boolean
function Trig_StartLobby_Func006C()
	return udg_LocalInteger == 3
end
---@return nothing
function Trig_StartLobby_Func007Func001A()
	CameraSetupApplyForPlayer(true, gg_cam_GW4, GetEnumPlayer(), 0)
end
---@return boolean
function Trig_StartLobby_Func007C()
	return udg_LocalInteger == 4
end
---@return nothing
function Trig_StartLobby_Func008Func001A()
	CameraSetupApplyForPlayer(true, gg_cam_GW5, GetEnumPlayer(), 0)
end
---@return boolean
function Trig_StartLobby_Func008C()
	return udg_LocalInteger == 5
end
---@return boolean
function Trig_StartLobby_Func015Func003C()
	return GetEnumPlayer() ~= Player(0)
end
---@return nothing
function Trig_StartLobby_Func015A()
	CameraSetupApplyForPlayer(true, gg_cam_HostRegion, GetEnumPlayer(), 0)
	SetCameraFieldForPlayer(GetEnumPlayer(), CAMERA_FIELD_TARGET_DISTANCE, 3400.00, 0.00)
	if Trig_StartLobby_Func015Func003C() then
		udg_LocalPosition2 = GetRandomLocInRect(gg_rct_HostRegion)
		CreateNUnitsAtLoc(1, FourCC('h0GA'), GetEnumPlayer(), udg_LocalPosition2, bj_UNIT_FACING)
		RemoveLocation(udg_LocalPosition2)
	end
end
---@return nothing
function Trig_StartLobby_Actions()
	udg_LocalPosition2 = GetRectCenter(gg_rct_HostRegion)
	udg_LocalInteger = GetRandomInt(1, 5)
	if Trig_StartLobby_Func004C() then
		ForForce(udg_AllPlayers, Trig_StartLobby_Func004Func001A)
	end
	if Trig_StartLobby_Func005C() then
		ForForce(udg_AllPlayers, Trig_StartLobby_Func005Func001A)
	end
	if Trig_StartLobby_Func006C() then
		ForForce(udg_AllPlayers, Trig_StartLobby_Func006Func001A)
	end
	if Trig_StartLobby_Func007C() then
		ForForce(udg_AllPlayers, Trig_StartLobby_Func007Func001A)
	end
	if Trig_StartLobby_Func008C() then
		ForForce(udg_AllPlayers, Trig_StartLobby_Func008Func001A)
	end
	udg_LocalInteger = 4
	DisplayTimedTextToForce(GetPlayersAll(), I2R(udg_LocalInteger), "TRIGSTR_10982")
	udg_LocalInteger = udg_LocalInteger - 3
	TriggerSleepAction(I2R(udg_LocalInteger))
	ForForce(udg_AllPlayers, Trig_StartLobby_Func015A)
	RemoveLocation(udg_LocalPosition2)
	StartTimerBJ(udg_LobbyTime, false, 60.00)
	CreateTimerDialogBJ(GetLastCreatedTimerBJ(), "TRIGSTR_19360")
	udg_LobbyTimerWindows = GetLastCreatedTimerDialogBJ()
	CreateNUnitsAtLoc(1, FourCC('n04G'), Player(0), GetRectCenter(GetPlayableMapRect()), bj_UNIT_FACING)
	ModeBuilding = GetLastCreatedUnit()
	SelectUnitForPlayerSingle(GetLastCreatedUnit(), Player(0))
end
-- ===========================================================================
---@return nothing
function InitTrig_StartLobby()
	gg_trg_StartLobby = CreateTrigger()
	TriggerRegisterTimerEventSingle(gg_trg_StartLobby, 0.01)
	TriggerAddAction(gg_trg_StartLobby, Trig_StartLobby_Actions)
end
-- ===========================================================================
--  Trigger: EndLobby and Start game
-- ===========================================================================
---@return boolean
function Trig_EndLobby_and_Start_game_Func004Func006C()
	return udg_Continents[0] == 0
end
---@return nothing
function Trig_EndLobby_and_Start_game_Func004A()
	CreateRaceCircles(GetEnumPlayer())
	ClearAllies(GetEnumPlayer())
	CreateArmyBonusUnit(GetEnumPlayer())
	FogModifierStop(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
	DestroyFogModifier(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
	if Trig_EndLobby_and_Start_game_Func004Func006C() then
		CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
		FogModifierStop(GetLastCreatedFogModifier())
		DestroyFogModifier(GetLastCreatedFogModifier())
	else
		ConditionalTriggerExecute(gg_trg_SeeOnlyNeedeed)
	end
end
---@return nothing
function Trig_EndLobby_and_Start_game_Func005A()
	RemoveUnit(GetEnumUnit())
end
---@return nothing
function Trig_EndLobby_and_Start_game_Actions()
	TimerDialogDisplayBJ(false, udg_LobbyTimerWindows)
	DestroyTimerDialogBJ(udg_LobbyTimerWindows)
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19369")
	ForForce(udg_AllPlayers, Trig_EndLobby_and_Start_game_Func004A)
	ForGroupBJ(GetUnitsInRectAll(gg_rct_HostReg2), Trig_EndLobby_and_Start_game_Func005A)
	DisableTrigger(gg_trg_SaveSelection)
	BlzEnableSelections(true, true)
	RemoveUnit(ModeBuilding)	--  INLINED!!
	ConditionalTriggerExecute(gg_trg_StartDal)
	ConditionalTriggerExecute(gg_trg_NaxStart)
	ConditionalTriggerExecute(gg_trg_TurtleStart)
	aiStart()
end
-- ===========================================================================
---@return nothing
function InitTrig_EndLobby_and_Start_game()
	gg_trg_EndLobby_and_Start_game = CreateTrigger()
	TriggerRegisterTimerExpireEventBJ(gg_trg_EndLobby_and_Start_game, udg_LobbyTime)
	TriggerAddAction(gg_trg_EndLobby_and_Start_game, Trig_EndLobby_and_Start_game_Actions)
end
-- ===========================================================================
--  Trigger: AddMinute
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_AddMinute_Actions()
	StartTimerBJ(udg_LobbyTime, false, TimerGetRemaining(udg_LobbyTime) + 60.00)
	DisableTrigger(GetTriggeringTrigger())
end
-- ===========================================================================
---@return nothing
function InitTrig_AddMinute()
	gg_trg_AddMinute = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_AddMinute, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AddMinute, function()
        if GetSpellAbilityId() ~= FourCC('A0UJ') then return end
        Trig_AddMinute_Actions()
    end)
end
-- ===========================================================================
--  Trigger: StartGameFast
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_StartGameFast_Actions()
	StartTimerBJ(udg_LobbyTime, false, 5.00)
end
-- ===========================================================================
---@return nothing
function InitTrig_StartGameFast()
	gg_trg_StartGameFast = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_StartGameFast, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_StartGameFast, function()
        if GetSpellAbilityId() ~= FourCC('A0UK') then return end
        Trig_StartGameFast_Actions()
    end)
end
-- ===========================================================================
--  Trigger: LeaveStart
-- ===========================================================================
---@return boolean
function Trig_LeaveStart_Conditions()
	return GetUnitTypeId(GetTriggerUnit()) == FourCC('H049')
end
---@return nothing
function Trig_LeaveStart_Actions()
	BlzSetUnitRealFieldBJ(GetTriggerUnit(), UNIT_RF_MANA_REGENERATION, 300)
end
-- ===========================================================================
---@return nothing
function InitTrig_LeaveStart()
	gg_trg_LeaveStart = CreateTrigger()
	TriggerRegisterLeaveRectSimple(gg_trg_LeaveStart, gg_rct_HostRegion)
	TriggerAddCondition(gg_trg_LeaveStart, Condition(Trig_LeaveStart_Conditions))
	TriggerAddAction(gg_trg_LeaveStart, Trig_LeaveStart_Actions)
end
-- ===========================================================================
--  Trigger: NextMenu
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_NextMenu_Actions()
	local l = Location(0, 0)
	
	-- call DisplayTextToPlayer(Player(0),0,0,"33")
	-- call DisplayTextToPlayer(Player(0),0,0, I2S(ModeBuildingI))
	
	
	if ModeBuildingI < 6 then
		ModeBuildingI = ModeBuildingI + 1
	else
		ModeBuildingI = 0
	end
	KillUnit(ModeBuilding)
	RemoveUnit(ModeBuilding)
	if ModeBuildingI == 0 then
		ModeBuilding = CreateUnitAtLoc(Player(0), FourCC('n04G'), l, 0)
	elseif ModeBuildingI == 1 then
		ModeBuilding = CreateUnitAtLoc(Player(0), FourCC('n04D'), l, 0)
	elseif ModeBuildingI == 2 then
		ModeBuilding = CreateUnitAtLoc(Player(0), FourCC('n04F'), l, 0)
	elseif ModeBuildingI == 3 then
		ModeBuilding = CreateUnitAtLoc(Player(0), FourCC('n04H'), l, 0)
	elseif ModeBuildingI == 4 then	--  ?????????
		ModeBuilding = CreateUnitAtLoc(Player(0), FourCC('n04I'), l, 0)
	elseif ModeBuildingI == 5 then	--  ??????
		ModeBuilding = CreateUnitAtLoc(Player(0), FourCC('n06Y'), l, 0)
	elseif ModeBuildingI == 6 then	--  ??????????
		ModeBuilding = CreateUnitAtLoc(Player(0), FourCC('n074'), l, 0)
	end
	ClearSelectionForPlayer(Player(0))
	SelectUnitForPlayerSingle(ModeBuilding, Player(0))
	
	
	RemoveLocation(l)
end
-- ===========================================================================
---@return nothing
function InitTrig_NextMenu()
	gg_trg_NextMenu = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_NextMenu, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_NextMenu, function()
        if GetSpellAbilityId() ~= FourCC('A0Y5') then return end
        Trig_NextMenu_Actions()
    end)
end
-- ===========================================================================
--  Trigger: SaveSelection
-- ===========================================================================
---@return nothing
function Trig_SaveSelection_Actions()
	local u = GetTriggerUnit()
	if u == ModeBuilding then
		SelectUnitForPlayerSingle(u, GetOwningPlayer(u))
	end
	
end
-- ===========================================================================
---@return nothing
function InitTrig_SaveSelection()
	gg_trg_SaveSelection = CreateTrigger()
	TriggerRegisterPlayerSelectionEventBJ(gg_trg_SaveSelection, Player(0), false)
	TriggerAddAction(gg_trg_SaveSelection, Trig_SaveSelection_Actions)
end
-- ===========================================================================
--  Trigger: UpgradeStolica
-- ===========================================================================
---@return boolean
function Trig_UpgradeStolica_Conditions()
	return IsUnitInGroup(GetTriggerUnit(), udg_StolicaGroups)
end
---@return nothing
function Trig_UpgradeStolica_Actions()
	BlzSetUnitArmor(GetTriggerUnit(), 30.00)
	BlzSetUnitMaxHP(GetTriggerUnit(), 10000)
	UnitAddAbilityBJ(FourCC('A0I6'), GetTriggerUnit())
	BlzSetUnitStringFieldBJ(GetTriggerUnit(), UNIT_SF_NAME, "|cffd45e19???????:|r " .. GetUnitName(GetTriggerUnit()))
	UnitAddAbilityBJ(FourCC('A145'), GetTriggerUnit())
end
-- ===========================================================================
---@return nothing
function InitTrig_UpgradeStolica()
	gg_trg_UpgradeStolica = CreateTrigger()
	DisableTrigger(gg_trg_UpgradeStolica)
	TriggerRegisterAnyUnitEventBJ(gg_trg_UpgradeStolica, EVENT_PLAYER_UNIT_UPGRADE_FINISH)
	TriggerAddCondition(gg_trg_UpgradeStolica, Condition(Trig_UpgradeStolica_Conditions))
	TriggerAddAction(gg_trg_UpgradeStolica, Trig_UpgradeStolica_Actions)
end
-- ===========================================================================
--  Trigger: MakeStolica
-- ===========================================================================
---@return boolean
function HaveCapitalAbility()
	return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A0IQ')) ~= 0 and UnitAlive(GetFilterUnit())
end
---@return boolean
function Capitals()
	return IsUnitInGroup(GetFilterUnit(), udg_StolicaGroups)
end
---@return boolean
---@param u unit
---@param flag boolean
---@return nothing
function unitShareVisionAll(u, flag)
	local i = 0
	while true do
		if i > 23 then break end
		UnitShareVision(u, Player(i), flag)
		i = i + 1
	end
end
---@param u unit
---@return nothing
function checkMovingCity(u)
	local x = GetUnitX(u)
	local y = GetUnitY(u)
	
	if RectContainsCoords(gg_rct_Naxramas, x, y) then
		unitShareVisionAll(gg_unit_e00D_0080, true)
	elseif RectContainsCoords(gg_rct_KillDalaran, x, y) then
		unitShareVisionAll(gg_unit_e00C_0590, true)
	elseif RectContainsCoords(gg_rct_TurtleIsland, x, y) then
		unitShareVisionAll(gg_unit_e00E_0085, true)
	end
	
	
end
---@param capital unit
---@return nothing
function MakeCapital(capital)
	UnitSetConstructionProgress(capital, 100)
	BlzSetUnitMaxHP(capital, 10000)
	SetUnitLifeBJ(capital, 10000.00)
	BlzSetUnitRealFieldBJ(capital, UNIT_RF_SIGHT_RADIUS, 750.00)
	BlzSetUnitArmor(capital, 30.00)
	UnitAddAbility(capital, FourCC('A0I6'))
	UnitAddAbility(capital, FourCC('A145'))
	BlzSetUnitStringFieldBJ(capital, UNIT_SF_NAME, "|cffd45e19???????:|r " .. GetUnitName(capital))
	GroupAddUnit(udg_StolicaGroups, capital)
	TriggerRegisterUnitEvent(gg_trg_StolicaAttacked, capital, EVENT_UNIT_ATTACKED)
	unitShareVisionAll(capital, true)
	checkMovingCity(capital)
	playerCapital[GetPlayerId(GetOwningPlayer(capital))] = capital
end
---@param p player
---@return nothing
function MakeFakeCapital(p)
	local u
	GroupEnumUnitsOfPlayer(gGroup, p, HaveCapitalAbility)
	u = BlzGroupUnitAt(gGroup, GetRandomInt(0, BlzGroupGetSize(gGroup) - 1))
	playerCapital[GetPlayerId(p)] = u
	aiCapitalEnter(u)
	u = nil
	GroupClear(gGroup)
end
---@return nothing
function Trig_MakeStolica_Actions()
	SetPlayerAbilityAvailableBJ(false, FourCC('A0IQ'), GetOwningPlayer(GetTriggerUnit()))
	MakeCapital(GetTriggerUnit())
	
end
-- ===========================================================================
---@return nothing
function InitTrig_MakeStolica()
	gg_trg_MakeStolica = CreateTrigger()
	DisableTrigger(gg_trg_MakeStolica)
	TriggerRegisterAnyUnitEventBJ(gg_trg_MakeStolica, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MakeStolica, function()
        if GetSpellAbilityId() ~= FourCC('A0IQ') then return end
        Trig_MakeStolica_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Mod classic
-- ===========================================================================
---@return nothing
function Trig_Mod_classic_Actions()
	udg_GameMode = 0
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19403")
end
-- ===========================================================================
---@return nothing
function InitTrig_Mod_classic()
	gg_trg_Mod_classic = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_Mod_classic, Player(0), "-mod cl", true)
	TriggerAddAction(gg_trg_Mod_classic, Trig_Mod_classic_Actions)
end
-- ===========================================================================
--  Trigger: Mod classic spell
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_Mod_classic_spell_Actions()
	udg_GameMode = 0
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_21887")
end
-- ===========================================================================
---@return nothing
function InitTrig_Mod_classic_spell()
	gg_trg_Mod_classic_spell = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Mod_classic_spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Mod_classic_spell, function()
        if GetSpellAbilityId() ~= FourCC('A0T4') then return end
        Trig_Mod_classic_spell_Actions()
    end)
end
-- ===========================================================================
--  Trigger: RebebmerToBuild
-- ===========================================================================
---@return nothing
function Trig_RebebmerToBuild_Actions()
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_2405")
	TriggerSleepAction(300.00)
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_4745")
	TriggerSleepAction(120.00)
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_27017")
	TriggerSleepAction(60.00)
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_27018")
	TriggerSleepAction(60.00)
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_27019")
	TriggerSleepAction(60.00)
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_27020")
end
-- ===========================================================================
---@return nothing
function InitTrig_RebebmerToBuild()
	gg_trg_RebebmerToBuild = CreateTrigger()
	TriggerAddAction(gg_trg_RebebmerToBuild, Trig_RebebmerToBuild_Actions)
end
-- ===========================================================================
--  Trigger: StolicaTime
-- ===========================================================================
---@param p player
---@return nothing
function CheckAndCreateCapital(p)
	local u
	local g = CreateGroup()
	GroupEnumUnitsOfPlayer(g, p, Capitals)
	if BlzGroupGetSize(g) == 0 then	-- ??????? ???
		
		GroupClear(g)
		Counter = 0
		GroupEnumUnitsOfPlayer(g, p, HaveCapitalAbility)
		
		if BlzGroupGetSize(g) > 0 then
			u = BlzGroupUnitAt(g, GetRandomInt(0, BlzGroupGetSize(g) - 1))
			SetPlayerAbilityAvailable(p, FourCC('A0IQ'), false)
			MakeCapital(u)
			DisplayTimedTextToForce(udg_AllPlayers, 5, GetPlayerName(p) .. " - |cffffff00????? ????????|r|r, ??? |cffd45e19???????|r ?? ?? ???? ????????? ?? ???????, ? ?????? ???? ??????????? ?????????????.")
		else
			if GetPlayerSlotState(p) == PLAYER_SLOT_STATE_PLAYING then
				DisplayTimedTextToForce(udg_AllPlayers, 5, GetPlayerName(p) .. " - |cffff0000????????|r, ??? |cffd45e19??????? |r ?? ????????? ?? ???????. :(")
			end
			
			ClearPlayer(p)
			
		end
		-- call DisplayTextToPlayer(Player(0),0,0,"????????????: ????? "+GetPlayerName(p)+"  ?? ????? ???????")
	else
		
		-- call DisplayTextToPlayer(Player(0),0,0,"????????????: ????? "+GetPlayerName(p)+"  ????? ???????")
	end
	
	
	
	u = nil
	DestroyGroup(g)
	g = nil
	
end
---@return nothing
function AllPlayersCapital()
	CheckAndCreateCapital(GetEnumPlayer())
end
---@return nothing
function Trig_StolicaTime_Actions()
	ForForce(udg_AllPlayers, AllPlayersCapital)
	ForForce(udg_Bots, AllPlayersCapital)
	-- call DisplayTextToPlayer(Player(0),0,0,"????????????: ????? ?? ?????????")
end
-- ===========================================================================
---@return nothing
function InitTrig_StolicaTime()
	gg_trg_StolicaTime = CreateTrigger()
	DisableTrigger(gg_trg_StolicaTime)
	TriggerRegisterTimerExpireEventBJ(gg_trg_StolicaTime, udg_IncomeTimerFirst)
	TriggerAddAction(gg_trg_StolicaTime, Trig_StolicaTime_Actions)
end
-- ===========================================================================
--  Trigger: MOD Combo
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_MOD_Combo_Actions()
	udg_GameMode = 5
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_5722")
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_Combo()
	gg_trg_MOD_Combo = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_MOD_Combo, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MOD_Combo, function()
        if GetSpellAbilityId() ~= FourCC('A1M4') then return end
        Trig_MOD_Combo_Actions()
    end)
end
-- ===========================================================================
--  Trigger: MOD stolica Start Copy
-- ===========================================================================
---@return boolean
function Trig_MOD_stolica_Start_Copy_Conditions()
	return udg_GameMode == 5
end
---@return nothing
function Trig_MOD_stolica_Start_Copy_Func005A()
	SetPlayerAbilityAvailableBJ(true, FourCC('A0IQ'), GetEnumPlayer())
end
---@return nothing
function Trig_MOD_stolica_Start_Copy_Actions()
	DisplayTextToForce(udg_AllPlayers, "TRIGSTR_5726")
	ForForce(udg_AllPlayers, Trig_MOD_stolica_Start_Copy_Func005A)
	EnableTrigger(gg_trg_MakeStolica)
	EnableTrigger(gg_trg_UpgradeStolica)
	EnableTrigger(gg_trg_StolicaDead)
	EnableTrigger(gg_trg_StolicaTime)
	TriggerExecute(gg_trg_RebebmerToBuild)
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_stolica_Start_Copy()
	gg_trg_MOD_stolica_Start_Copy = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_MOD_stolica_Start_Copy, Player(0), "-mod st", true)
	TriggerRegisterTimerExpireEventBJ(gg_trg_MOD_stolica_Start_Copy, udg_LobbyTime)
	TriggerAddCondition(gg_trg_MOD_stolica_Start_Copy, Condition(Trig_MOD_stolica_Start_Copy_Conditions))
	TriggerAddAction(gg_trg_MOD_stolica_Start_Copy, Trig_MOD_stolica_Start_Copy_Actions)
end
-- ===========================================================================
--  Trigger: StolicaDead
-- ===========================================================================
---@return boolean
function Trig_StolicaDead_Conditions()
	return IsUnitInGroup(GetTriggerUnit(), udg_StolicaGroups)
end
---@return nothing
function Trig_StolicaDead_Actions()
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	SetPlayerAbilityAvailableBJ(true, FourCC('A0IQ'), GetOwningPlayer(GetTriggerUnit()))
	DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. " - |cffff0000????????|r, ??? |cffd45e19??????? |r??????????.")
	ClearPlayer(Player(pi))
	AiLimitsSet()
end
-- ===========================================================================
---@return nothing
function InitTrig_StolicaDead()
	gg_trg_StolicaDead = CreateTrigger()
	DisableTrigger(gg_trg_StolicaDead)
	TriggerRegisterAnyUnitEventBJ(gg_trg_StolicaDead, EVENT_PLAYER_UNIT_DEATH)
	TriggerAddCondition(gg_trg_StolicaDead, Condition(Trig_StolicaDead_Conditions))
	TriggerAddAction(gg_trg_StolicaDead, Trig_StolicaDead_Actions)
end
-- ===========================================================================
--  Trigger: StolicaAttacked
-- ===========================================================================
---@return nothing
function CapTimeDel()
	local t = GetExpiredTimer()
	local tid = GetHandleId(t)
	local pi = LoadInteger(Hash, tid, 0)
	
	cap_time[pi] = true
	
	
	FlushChildHashtable(Hash, tid)
	DestroyTimer(t)
	t = nil
	
end
---@return boolean
function Trig_StolicaAttacked_Conditions()
	return IsUnitInGroup(GetTriggerUnit(), udg_StolicaGroups)
end
---@return nothing
function Trig_StolicaAttacked_Actions()
	local t = nil
	local tid = GetHandleId(t)
	local pi = GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
	if cap_time[pi] then
		t = CreateTimer()
		DisplayTextToPlayer(Player(pi), 0, 0, "TRIGSTR_27508")
		cap_time[pi] = false
		SaveInteger(Hash, tid, 0, pi)
		TimerStart(t, 90, false, CapTimeDel)
	end
	
	
	t = nil
	
end
-- ===========================================================================
---@return nothing
function InitTrig_StolicaAttacked()
	gg_trg_StolicaAttacked = CreateTrigger()
	-- call TriggerRegisterAnyUnitEventBJ( gg_trg_StolicaAttacked, EVENT_PLAYER_UNIT_ATTACKED )
	TriggerAddCondition(gg_trg_StolicaAttacked, Condition(Trig_StolicaAttacked_Conditions))
	TriggerAddAction(gg_trg_StolicaAttacked, Trig_StolicaAttacked_Actions)
end
-- ===========================================================================
--  Trigger: MOD feoda O set spell
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_MOD_feoda_O_set_spell_Actions()
	udg_GameMode = 1
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19606")
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_feoda_O_set_spell()
	gg_trg_MOD_feoda_O_set_spell = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_MOD_feoda_O_set_spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MOD_feoda_O_set_spell, function()
        if GetSpellAbilityId() ~= FourCC('A0T5') then return end
        Trig_MOD_feoda_O_set_spell_Actions()
    end)
end
-- ===========================================================================
--  Trigger: MOD stolica Set
-- ===========================================================================
---@return nothing
function Trig_MOD_stolica_Set_Actions()
	udg_GameMode = 1
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19394")
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_stolica_Set()
	gg_trg_MOD_stolica_Set = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_MOD_stolica_Set, Player(0), "-mod st", true)
	TriggerAddAction(gg_trg_MOD_stolica_Set, Trig_MOD_stolica_Set_Actions)
end
-- ===========================================================================
--  Trigger: MOD stolica Start
-- ===========================================================================
---@return boolean
function Trig_MOD_stolica_Start_Conditions()
	return udg_GameMode == 1
end
---@return nothing
function Trig_MOD_stolica_Start_Func005A()
	SetPlayerAbilityAvailableBJ(true, FourCC('A0IQ'), GetEnumPlayer())
end
---@return nothing
function Trig_MOD_stolica_Start_Actions()
	DisplayTextToForce(udg_AllPlayers, "TRIGSTR_19372")
	ForForce(udg_AllPlayers, Trig_MOD_stolica_Start_Func005A)
	EnableTrigger(gg_trg_MakeStolica)
	EnableTrigger(gg_trg_UpgradeStolica)
	EnableTrigger(gg_trg_StolicaDead)
	EnableTrigger(gg_trg_StolicaTime)
	TriggerExecute(gg_trg_RebebmerToBuild)
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_stolica_Start()
	gg_trg_MOD_stolica_Start = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_MOD_stolica_Start, Player(0), "-mod st", true)
	TriggerRegisterTimerExpireEventBJ(gg_trg_MOD_stolica_Start, udg_LobbyTime)
	TriggerAddCondition(gg_trg_MOD_stolica_Start, Condition(Trig_MOD_stolica_Start_Conditions))
	TriggerAddAction(gg_trg_MOD_stolica_Start, Trig_MOD_stolica_Start_Actions)
end
-- ===========================================================================
--  Trigger: MOD feoda O Set
-- ===========================================================================
---@return nothing
function Trig_MOD_feoda_O_Set_Actions()
	udg_GameMode = 2
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19397")
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_feoda_O_Set()
	gg_trg_MOD_feoda_O_Set = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_MOD_feoda_O_Set, Player(0), "-mod feod", true)
	TriggerAddAction(gg_trg_MOD_feoda_O_Set, Trig_MOD_feoda_O_Set_Actions)
end
-- ===========================================================================
--  Trigger: MOD feoda O Set Spell
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_MOD_feoda_O_Set_Spell_Actions()
	udg_GameMode = 2
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19605")
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_feoda_O_Set_Spell()
	gg_trg_MOD_feoda_O_Set_Spell = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_MOD_feoda_O_Set_Spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MOD_feoda_O_Set_Spell, function()
        if GetSpellAbilityId() ~= FourCC('A0T6') then return end
        Trig_MOD_feoda_O_Set_Spell_Actions()
    end)
end
-- ===========================================================================
--  Trigger: MOD feoda O Start
-- ===========================================================================
---@return boolean
function Trig_MOD_feoda_O_Start_Conditions()
	return udg_GameMode == 2
end
---@return nothing
function Trig_MOD_feoda_O_Start_Func006A()
	SetPlayerAbilityAvailableBJ(true, FourCC('A0IQ'), GetEnumPlayer())
end
---@return nothing
function Trig_MOD_feoda_O_Start_Actions()
	DisplayTextToForce(udg_AllPlayers, "TRIGSTR_19378")
	SetForceAllianceStateBJ(udg_AllPlayers, udg_AllPlayers, bj_ALLIANCE_UNALLIED)
	ForForce(udg_AllPlayers, Trig_MOD_feoda_O_Start_Func006A)
	EnableTrigger(gg_trg_MakeStolica)
	EnableTrigger(gg_trg_UpgradeStolica)
	EnableTrigger(gg_trg_StolicaTime)
	EnableTrigger(gg_trg_FeodalDead2)
	EnableTrigger(gg_trg_DoNotAttackSenior2)
	SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, true)
	SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, true)
end
-- ===========================================================================
---@return nothing
function InitTrig_MOD_feoda_O_Start()
	gg_trg_MOD_feoda_O_Start = CreateTrigger()
	TriggerRegisterTimerExpireEventBJ(gg_trg_MOD_feoda_O_Start, udg_LobbyTime)
	TriggerRegisterPlayerChatEvent(gg_trg_MOD_feoda_O_Start, Player(0), "-mod feod", true)
	TriggerAddCondition(gg_trg_MOD_feoda_O_Start, Condition(Trig_MOD_feoda_O_Start_Conditions))
	TriggerAddAction(gg_trg_MOD_feoda_O_Start, Trig_MOD_feoda_O_Start_Actions)
end
-- ===========================================================================
--  Trigger: FeodalDead
-- ===========================================================================
---@return boolean
function Trig_FeodalDead_Conditions()
	return IsUnitInGroup(GetTriggerUnit(), udg_StolicaGroups) and ((GetUnitLifePercent(GetTriggerUnit()) <= 15.00))
end
---@return boolean
function Trig_FeodalDead_Func004Func002Func001Func010Func001Func003C()
	return IsPlayerInForce(GetOwningPlayer(GetTriggerUnit()), udg_Vassals[GetForLoopIndexB()])
end
---@return nothing
function Trig_FeodalDead_Func004Func002Func001Func010A()
	for bj_forLoopBIndex = 1, 24 do
		SetPlayerAllianceStateBJ(GetEnumPlayer(), ConvertedPlayer(GetForLoopIndexB()), bj_ALLIANCE_UNALLIED)
		SetPlayerAllianceStateBJ(ConvertedPlayer(GetForLoopIndexB()), GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
		if Trig_FeodalDead_Func004Func002Func001Func010Func001Func003C() then
			ForceRemovePlayerSimple(GetOwningPlayer(GetTriggerUnit()), udg_Vassals[GetForLoopIndexB()])
		end
	end
	ForceAddPlayerSimple(GetEnumPlayer(), udg_Vassals[GetConvertedPlayerId(ConvertedPlayer(GetForLoopIndexA()))])
	SetPlayerAllianceStateBJ(GetEnumPlayer(), GetOwningPlayer(GetAttacker()), bj_ALLIANCE_ALLIED_VISION)
	SetPlayerAllianceStateBJ(GetEnumPlayer(), ConvertedPlayer(GetForLoopIndexA()), bj_ALLIANCE_ALLIED_UNITS)
	SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetEnumPlayer(), bj_ALLIANCE_ALLIED_VISION)
	SetPlayerAllianceStateBJ(ConvertedPlayer(GetForLoopIndexA()), GetEnumPlayer(), bj_ALLIANCE_ALLIED_VISION)
	SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetEnumPlayer(), bj_ALLIANCE_ALLIED_VISION)
	DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetEnumPlayer()) .. (" - ???? ???????? ?????? " .. GetPlayerName(ConvertedPlayer(GetForLoopIndexA()))))
end
---@return boolean
function Trig_FeodalDead_Func004Func002Func001C()
	return IsPlayerInForce(GetOwningPlayer(GetAttacker()), udg_Vassals[GetForLoopIndexA()])
end
---@return nothing
function Trig_FeodalDead_Func004Func011A()
	DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetEnumPlayer()) .. (" - ???? ???????? ?????? " .. GetPlayerName(GetOwningPlayer(GetAttacker()))))
	ForceAddPlayerSimple(GetEnumPlayer(), udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttacker()))])
	for bj_forLoopBIndex = 1, 24 do
		SetPlayerAllianceStateBJ(GetEnumPlayer(), ConvertedPlayer(GetForLoopIndexB()), bj_ALLIANCE_UNALLIED)
		SetPlayerAllianceStateBJ(ConvertedPlayer(GetForLoopIndexB()), GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
	end
end
---@return boolean
function Trig_FeodalDead_Func004Func017Func001C()
	return IsUnitInGroup(GetEnumUnit(), udg_ZahvatBuildings)
end
---@return nothing
function Trig_FeodalDead_Func004Func017A()
	if Trig_FeodalDead_Func004Func017Func001C() then
		SetUnitOwner(GetEnumUnit(), Player(PLAYER_NEUTRAL_AGGRESSIVE), true)
	else
		KillUnit(GetEnumUnit())
		RemoveUnit(GetEnumUnit())
	end
end
---@return nothing
function Trig_FeodalDead_Func004Func020A()
	DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetEnumPlayer()) .. (" ??????????? ?? ?????? " .. GetPlayerName(GetOwningPlayer(GetTriggerUnit()))))
	for bj_forLoopAIndex = 1, 24 do
		SetPlayerAllianceStateBJ(GetOwningPlayer(GetTriggerUnit()), ConvertedPlayer(GetForLoopIndexA()), bj_ALLIANCE_UNALLIED)
		SetPlayerAllianceStateBJ(GetEnumPlayer(), ConvertedPlayer(GetForLoopIndexA()), bj_ALLIANCE_UNALLIED)
		SetPlayerAllianceStateBJ(ConvertedPlayer(GetForLoopIndexA()), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_UNALLIED)
	end
end
---@return boolean
function Trig_FeodalDead_Func004C()
	return GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetAttacker())
end
---@return nothing
function Trig_FeodalDead_Actions()
	SetUnitLifePercentBJ(GetTriggerUnit(), 100)
	SetUnitInvulnerable(GetTriggerUnit(), true)
	SetUnitInvulnerable(GetTriggerUnit(), false)
	if Trig_FeodalDead_Func004C() then
		--  ??????? ??? ??????????
		DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. "|cffff0000 - ??????????! |r??????)")
		ForGroupBJ(GetUnitsOfPlayerAll(GetOwningPlayer(GetTriggerUnit())), Trig_FeodalDead_Func004Func017A)
		SetPlayerAbilityAvailableBJ(true, FourCC('A0IQ'), GetOwningPlayer(GetTriggerUnit()))
		--  ??????? ???????? ??????????. ?? ????????!
		ForForce(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))], Trig_FeodalDead_Func004Func020A)
		ForceClear(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))])
	else
		--  --------------------------------------------------------------------   ??????? ????-?? ????????
		for bj_forLoopAIndex = 1, 24 do
			if Trig_FeodalDead_Func004Func002Func001C() then
				for bj_forLoopBIndex = 1, 24 do
					SetPlayerAllianceStateBJ(GetTriggerPlayer(), ConvertedPlayer(GetForLoopIndexB()), bj_ALLIANCE_UNALLIED)
					SetPlayerAllianceStateBJ(ConvertedPlayer(GetForLoopIndexB()), GetTriggerPlayer(), bj_ALLIANCE_UNALLIED)
				end
				--  ???? ??????
				--  ???????????? ??????? ???????
				DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. (" - ???? ???????? ?????? " .. GetPlayerName(ConvertedPlayer(GetForLoopIndexA()))))
				ForceAddPlayerSimple(GetOwningPlayer(GetTriggerUnit()), udg_Vassals[GetConvertedPlayerId(ConvertedPlayer(GetForLoopIndexA()))])
				SetPlayerAllianceStateBJ(GetOwningPlayer(GetTriggerUnit()), ConvertedPlayer(GetForLoopIndexA()), bj_ALLIANCE_ALLIED_UNITS)
				SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_ALLIED_VISION)
				SetPlayerAllianceStateBJ(ConvertedPlayer(GetForLoopIndexA()), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_ALLIED_VISION)
				--  ???????????? ???????? ??????? ???????
				ForForce(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttackedUnitBJ()))], Trig_FeodalDead_Func004Func002Func001Func010A)
				ForceClear(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))])
				SetForceAllianceStateBJ(udg_Vassals[GetForLoopIndexA()], udg_Vassals[GetForLoopIndexA()], bj_ALLIANCE_ALLIED_VISION)
				SetForceAllianceStateBJ(udg_Vassals[GetForLoopIndexA()], GetForceOfPlayer(GetOwningPlayer(GetAttacker())), bj_ALLIANCE_ALLIED_UNITS)
				return
			end
		end
		--  --------------------------------------------------------------------   ?????? ????-?? ????????
		--  ???????????? ??????? ???????
		for bj_forLoopBIndex = 1, 24 do
			SetPlayerAllianceStateBJ(GetTriggerPlayer(), ConvertedPlayer(GetForLoopIndexB()), bj_ALLIANCE_UNALLIED)
			SetPlayerAllianceStateBJ(ConvertedPlayer(GetForLoopIndexB()), GetTriggerPlayer(), bj_ALLIANCE_UNALLIED)
		end
		DisplayTextToForce(GetPlayersAll(), GetPlayerName(GetOwningPlayer(GetTriggerUnit())) .. (" - ???? ???????? ?????? " .. GetPlayerName(GetOwningPlayer(GetAttacker()))))
		ForceAddPlayerSimple(GetOwningPlayer(GetTriggerUnit()), udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttacker()))])
		SetPlayerAllianceStateBJ(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker()), bj_ALLIANCE_ALLIED_UNITS)
		SetPlayerAllianceStateBJ(GetOwningPlayer(GetAttacker()), GetOwningPlayer(GetTriggerUnit()), bj_ALLIANCE_ALLIED_VISION)
		--  ???????????? ???????? ??????? ???????
		ForForce(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttackedUnitBJ()))], Trig_FeodalDead_Func004Func011A)
		SetForceAllianceStateBJ(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttacker()))], udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttacker()))], bj_ALLIANCE_ALLIED_VISION)
		SetForceAllianceStateBJ(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttacker()))], GetForceOfPlayer(GetOwningPlayer(GetAttacker())), bj_ALLIANCE_ALLIED_UNITS)
		ForceClear(udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))])
	end
end
-- ===========================================================================
---@return nothing
function InitTrig_FeodalDead()
	gg_trg_FeodalDead = CreateTrigger()
	DisableTrigger(gg_trg_FeodalDead)
	TriggerRegisterAnyUnitEventBJ(gg_trg_FeodalDead, EVENT_PLAYER_UNIT_ATTACKED)
	TriggerAddCondition(gg_trg_FeodalDead, Condition(Trig_FeodalDead_Conditions))
	TriggerAddAction(gg_trg_FeodalDead, Trig_FeodalDead_Actions)
end
-- ===========================================================================
--  Trigger: FeodalDead2
-- ===========================================================================
-- 3 ??? ??????
---@return nothing
function CapTime()
	local u = udg_LocalUnit3
	SetUnitLifePercentBJ(u, 100)
	UnitAddAbility(u, FourCC('Avul'))
	RemoveAbilityTimed(u, FourCC('Avul'), 3)
end
---@param p player
---@return nothing
function ClearOldAllies(p)
	local p0 = Senior[GetPlayerId(p)]
	ForceRemovePlayer(Vassals[GetPlayerId(p0)], p)
	SetPlayerAllianceStateBJ(p, p0, bj_ALLIANCE_UNALLIED)
	SetPlayerAllianceStateBJ(p0, p, bj_ALLIANCE_UNALLIED)
	SetForceAllianceStateBJ(GetForceOfPlayer(p), Vassals[GetPlayerId(p0)], bj_ALLIANCE_UNALLIED)
	SetForceAllianceStateBJ(Vassals[GetPlayerId(p0)], GetForceOfPlayer(p), bj_ALLIANCE_UNALLIED)
	p0 = nil
end
---@param p player
---@return nothing
function NewAlly(p)
	local p3 = Senior[GetPlayerId(p)]
	SetPlayerAllianceStateBJ(p, p3, bj_ALLIANCE_ALLIED_UNITS)
	SetPlayerAllianceStateBJ(p3, p, bj_ALLIANCE_ALLIED_VISION)
	SetForceAllianceStateBJ(GetForceOfPlayer(p), Vassals[GetPlayerId(p3)], bj_ALLIANCE_ALLIED_VISION)
	SetForceAllianceStateBJ(Vassals[GetPlayerId(p3)], GetForceOfPlayer(p), bj_ALLIANCE_ALLIED_VISION)
	p3 = nil
end
---@return nothing
function Freedom()
	local p = GetEnumPlayer()
	DisplayTextToForce(udg_AllPlayers, GetPlayerName(p) .. " - ???? ????????")
	ClearOldAllies(p)
	p = nil
end
---@return nothing
function ChangeAlly()
	local p = udg_LocalPlayer
	local p0 = GetEnumPlayer()
	
	DisplayTextToForce(udg_AllPlayers, GetPlayerName(p0) .. " - ??????? ???????? ??????? " .. GetPlayerName(p))
	ClearOldAllies(p0)
	Senior[GetPlayerId(p0)] = p
	ForceAddPlayer(Vassals[GetPlayerId(p)], p0)
	NewAlly(p0)
	
	p = nil
	p0 = nil
end
---@return boolean
function Trig_FeodalDead2_Conditions()
	return IsUnitInGroup(GetTriggerUnit(), udg_StolicaGroups) and GetUnitLifePercent(GetTriggerUnit()) <= 15.00
end
---@return nothing
function Trig_FeodalDead2_Actions()
	local p = GetOwningPlayer(GetTriggerUnit())
	local pi = GetPlayerId(p)
	
	local p2 = GetOwningPlayer(GetAttacker())
	local pi2 = GetPlayerId(p2)
	
	local pi3
	local p3
	
	
	
	-- ?????? ??????????
	if p == p2 then
		
		ClearPlayer(p)
		DisplayTextToForce(udg_AllPlayers, GetPlayerName(p) .. " - ????? ?????????? ???? ??????? - ??????")
		ForForce(Vassals[pi], Freedom)
		
		p = nil
		p2 = nil
		p3 = nil
		return 
	end
	
	
	
	
	udg_LocalUnit3 = GetTriggerUnit()
	ExecuteFunc("CapTime")
	
	
	
	-- ???????? ?????????
	if Senior[pi2] == nil then
		-- ??????????
		DisplayTextToForce(udg_AllPlayers, GetPlayerName(p) .. " - ??????? ???????? ??????? " .. GetPlayerName(p2))
		if Senior[pi] == nil then
			
			Senior[pi] = p2
			ForceAddPlayer(Vassals[pi2], p)
			NewAlly(p)
			
			if CountPlayersInForceBJ(Vassals[pi]) ~= 0 then
				udg_LocalPlayer = p2
				ForForce(Vassals[pi], ChangeAlly)
			end
			
			-- ?????? ???????
		else
			ClearOldAllies(p)
			Senior[pi] = p2
			ForceAddPlayer(Vassals[pi2], p)
			NewAlly(p)
			
		end
		-- ???????? ???-?? ??????
	else
		p3 = Senior[pi2]
		pi3 = GetPlayerId(p3)
		DisplayTextToForce(udg_AllPlayers, GetPlayerName(p) .. " - ??????? ???????? ??????? " .. GetPlayerName(p3))
		-- ??????????
		if Senior[pi] == nil then
			
			Senior[pi] = p3
			ForceAddPlayer(Vassals[pi3], p)
			NewAlly(p)
			
			if CountPlayersInForceBJ(Vassals[pi]) ~= 0 then
				udg_LocalPlayer = p3
				ForForce(Vassals[pi], ChangeAlly)
			end
			
			
			-- ?????? ???????
		else
			ClearOldAllies(p)
			Senior[pi] = p3
			ForceAddPlayer(Vassals[pi3], p)
			NewAlly(p)
			
		end
		
	end
	
	-- set u = nil
	p = nil
	p2 = nil
	p3 = nil
end
-- ===========================================================================
---@return nothing
function InitTrig_FeodalDead2()
	gg_trg_FeodalDead2 = CreateTrigger()
	DisableTrigger(gg_trg_FeodalDead2)
	TriggerRegisterAnyUnitEventBJ(gg_trg_FeodalDead2, EVENT_PLAYER_UNIT_ATTACKED)
	TriggerAddCondition(gg_trg_FeodalDead2, Condition(Trig_FeodalDead2_Conditions))
	TriggerAddAction(gg_trg_FeodalDead2, Trig_FeodalDead2_Actions)
end
-- ===========================================================================
--  Trigger: DoNotAttackSenior
-- ===========================================================================
---@return boolean
function Trig_DoNotAttackSenior_Conditions()
	return IsPlayerInForce(GetOwningPlayer(GetAttacker()), udg_Vassals[GetConvertedPlayerId(GetOwningPlayer(GetAttackedUnitBJ()))])
end
---@return nothing
function Trig_DoNotAttackSenior_Actions()
	IssueImmediateOrderBJ(GetAttacker(), "stop")
end
-- ===========================================================================
---@return nothing
function InitTrig_DoNotAttackSenior()
	gg_trg_DoNotAttackSenior = CreateTrigger()
	DisableTrigger(gg_trg_DoNotAttackSenior)
	TriggerRegisterAnyUnitEventBJ(gg_trg_DoNotAttackSenior, EVENT_PLAYER_UNIT_ATTACKED)
	TriggerAddCondition(gg_trg_DoNotAttackSenior, Condition(Trig_DoNotAttackSenior_Conditions))
	TriggerAddAction(gg_trg_DoNotAttackSenior, Trig_DoNotAttackSenior_Actions)
end
-- ===========================================================================
--  Trigger: DoNotAttackSenior2
-- ===========================================================================
---@return boolean
function Trig_DoNotAttackSenior2_Conditions()
	return IsPlayerInForce(GetOwningPlayer(GetAttacker()), Vassals[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))])
end
---@return nothing
function Trig_DoNotAttackSenior2_Actions()
	IssueImmediateOrder(GetAttacker(), "stop")
end
-- ===========================================================================
---@return nothing
function InitTrig_DoNotAttackSenior2()
	gg_trg_DoNotAttackSenior2 = CreateTrigger()
	DisableTrigger(gg_trg_DoNotAttackSenior2)
	TriggerRegisterAnyUnitEventBJ(gg_trg_DoNotAttackSenior2, EVENT_PLAYER_UNIT_ATTACKED)
	TriggerAddCondition(gg_trg_DoNotAttackSenior2, Condition(Trig_DoNotAttackSenior2_Conditions))
	TriggerAddAction(gg_trg_DoNotAttackSenior2, Trig_DoNotAttackSenior2_Actions)
end
-- ===========================================================================
--  Trigger: AllPlayers and vassals
-- ===========================================================================
---@return nothing
function Trig_AllPlayers_and_vassals_Actions()
	for bj_forLoopAIndex = 1, 24 do
		DisplayTextToForce(GetPlayersAll(), GetPlayerName(ConvertedPlayer(GetForLoopIndexA())))
		DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19436")
		DisplayTextToForce(GetPlayersAll(), I2S(CountPlayersInForceBJ(udg_Vassals[GetConvertedPlayerId(ConvertedPlayer(GetForLoopIndexA()))])))
	end
end
-- ===========================================================================
---@return nothing
function InitTrig_AllPlayers_and_vassals()
	gg_trg_AllPlayers_and_vassals = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_AllPlayers_and_vassals, Player(0), "-feodifo", true)
	TriggerAddAction(gg_trg_AllPlayers_and_vassals, Trig_AllPlayers_and_vassals_Actions)
end
-- ===========================================================================
--  Trigger: DominationButton
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_DominationButton_Actions()
	udg_GameMode = 3
	DisplayTextToForce(GetPlayersAll(), "????? ??????: ?????????")
end
-- ===========================================================================
---@return nothing
function InitTrig_DominationButton()
	gg_trg_DominationButton = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_DominationButton, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_DominationButton, function()
        if GetSpellAbilityId() ~= FourCC('A1KJ') then return end
        Trig_DominationButton_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Domination start
-- ===========================================================================
---@return boolean
function Trig_Domination_start_Conditions()
	return udg_GameMode == 3 or udg_GameMode == 5
end
-- function TimedMessageDomination takes player p returns nothing
--     local integer pi = GetPlayerId(p)
--     
--     //DisplayTextToPlayer()
-- 
-- endfunction
-- 
---@return nothing
function ExpandTable()
	local i = 0
	local l__max = 1
	MultiboardSetColumnCount(Multiboard, 3)
	
	
	ThirdColumn[24] = MultiboardGetItem(Multiboard, 0, 2)
	MultiboardSetItemValue(ThirdColumn[24], "Точек,%")
	MultiboardSetItemWidth(ThirdColumn[24], 0.06)
	MultiboardReleaseItem(ThirdColumn[24])
	
	while true do
		if i > 23 then break end
		CityPlayerCount[i] = 0
		if GetPlayerSlotState(Player(i)) == PLAYER_SLOT_STATE_PLAYING or IsPlayerInForce(Player(i), udg_Bots) then
			ThirdColumn[i] = MultiboardGetItem(Multiboard, l__max, 2)
			MultiboardSetItemValue(ThirdColumn[i], "0.000%")
			MultiboardSetItemWidth(ThirdColumn[i], 0.06)
			l__max = l__max + 1
		end
		i = i + 1
		
	end
	
	
	
	MultiboardDisplay(Multiboard, false)
	MultiboardDisplay(Multiboard, true)
	
	
end
-- ?????????? ? UpdateGraph
-- function PercentGraph takes integer pi returns nothing
--     call MultiboardSetItemValue( ThirdColumn[pi], R2SW( I2R(CityPlayerCount[pi])*100.0/I2R(CityCount),3,3)+"%")
-- endfunction
---@return nothing
function Trig_Domination_start_Actions()
	DisplayTextToForce(udg_AllPlayers, "??????? ????? ?????????. ????????? " .. I2S(PercentWin) .. "% ???????, ????? ????????!")
end
-- ===========================================================================
---@return nothing
function InitTrig_Domination_start()
	gg_trg_Domination_start = CreateTrigger()
	TriggerRegisterTimerExpireEventBJ(gg_trg_Domination_start, udg_LobbyTime)
	TriggerAddCondition(gg_trg_Domination_start, Condition(Trig_Domination_start_Conditions))
	TriggerAddAction(gg_trg_Domination_start, Trig_Domination_start_Actions)
end
-- ===========================================================================
--  Trigger: DomCheckCommand
-- ===========================================================================
---@return nothing
function Trig_DomCheckCommand_Actions()
	local pi = GetPlayerId(GetTriggerPlayer())
	DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "?? ????????????? " .. I2S(CityPlayerCount[pi]) .. " ????? ?? " .. I2S(CityCount) .. " ?? ????? ? ?? " .. I2S(MathRound(CityCount * 0.01 * PercentWin)) .. " ??????????? ??? ??????")
	DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "????? ??????? ??? ??????? " .. R2SW(I2R(CityPlayerCount[pi]) * 100.0 / I2R(CityCount), 3, 3) .. "% ?? ??????????? " .. I2S(PercentWin) .. "%")
end
-- ===========================================================================
---@return nothing
function InitTrig_DomCheckCommand()
	local i = 0
	gg_trg_DomCheckCommand = CreateTrigger()
	
	while true do
		if i >= 23 then break end
		TriggerRegisterPlayerChatEvent(gg_trg_DomCheckCommand, Player(i), "-domck", true)
		
		i = i + 1
	end
	
	TriggerAddAction(gg_trg_DomCheckCommand, Trig_DomCheckCommand_Actions)
end
-- ===========================================================================
--  Trigger: FastTestSpell
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_FastTestSpell_Actions()
	udg_GameMode = 4
	DisplayTextToForce(GetPlayersAll(), "????? ??????: ????. ?????? -fast ? -fastoff ")
end
-- ===========================================================================
---@return nothing
function InitTrig_FastTestSpell()
	gg_trg_FastTestSpell = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FastTestSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FastTestSpell, function()
        if GetSpellAbilityId() ~= FourCC('A1MB') then return end
        Trig_FastTestSpell_Actions()
    end)
end
-- ===========================================================================
--  Trigger: FastTest
-- ===========================================================================
---@return nothing
function Trig_FastTest_Actions()
	if udg_GameMode == 4 then
		fastTest[GetPlayerId(GetTriggerPlayer())] = true
		income[GetPlayerId(GetTriggerPlayer())] = income[GetPlayerId(GetTriggerPlayer())] + 25000
		incomeW[GetPlayerId(GetTriggerPlayer())] = incomeW[GetPlayerId(GetTriggerPlayer())] + 25000
		DisplayTimedTextToForce(udg_AllPlayers, 6, GetPlayerName(GetTriggerPlayer()) .. " - ??????? ???????? ?????!!!")
		SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_FOOD_CAP, 100)
	end
	
	
	
end
-- ===========================================================================
---@return nothing
function InitTrig_FastTest()
	local i = 0
	gg_trg_FastTest = CreateTrigger()
	while true do
		if i > 23 then break end
		
		TriggerRegisterPlayerChatEvent(gg_trg_FastTest, Player(i), "-fast", true)
		fastTest[i] = false
		i = i + 1
	end
	TriggerAddAction(gg_trg_FastTest, Trig_FastTest_Actions)
end
-- ===========================================================================
--  Trigger: FastTestOff
-- ===========================================================================
---@return nothing
function Trig_FastTestOff_Actions()
	if udg_GameMode == 4 then
		fastTest[GetPlayerId(GetTriggerPlayer())] = false
		income[GetPlayerId(GetTriggerPlayer())] = income[GetPlayerId(GetTriggerPlayer())] - 25000
		incomeW[GetPlayerId(GetTriggerPlayer())] = incomeW[GetPlayerId(GetTriggerPlayer())] - 25000
		DisplayTimedTextToForce(udg_AllPlayers, 6, GetPlayerName(GetTriggerPlayer()) .. " - ???????? ???????? ?????!")
	end
end
-- ===========================================================================
---@return nothing
function InitTrig_FastTestOff()
	local i = 0
	gg_trg_FastTestOff = CreateTrigger()
	while true do
		if i > 23 then break end
		
		TriggerRegisterPlayerChatEvent(gg_trg_FastTestOff, Player(i), "-fastoff", true)
		
		i = i + 1
	end
	TriggerAddAction(gg_trg_FastTestOff, Trig_FastTestOff_Actions)
end
-- ===========================================================================
--  Trigger: FastTrain
-- ===========================================================================
---@return boolean
function Trig_FastTrain_Conditions()
	
	return fastTest[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
---@return nothing
function Trig_FastTrain_Actions()
	CreateUnit(GetOwningPlayer(GetTriggerUnit()), GetTrainedUnitType(), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), 0.00)
	IssueImmediateOrderById(GetTriggerUnit(), 851976)
end
-- ===========================================================================
---@return nothing
function InitTrig_FastTrain()
	gg_trg_FastTrain = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FastTrain, EVENT_PLAYER_UNIT_TRAIN_START)
	TriggerAddCondition(gg_trg_FastTrain, Condition(Trig_FastTrain_Conditions))
	TriggerAddAction(gg_trg_FastTrain, Trig_FastTrain_Actions)
end
-- ===========================================================================
--  Trigger: FastBuild
-- ===========================================================================
---@return boolean
function Trig_FastBuild_Conditions()
	
	return fastTest[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
---@return nothing
function Trig_FastBuild_Actions()
	local id = GetUnitTypeId(GetConstructingStructure())
	local x = GetUnitX(GetConstructingStructure())
	local y = GetUnitY(GetConstructingStructure())
	local pi = GetPlayerId(GetOwningPlayer(GetConstructingStructure()))
	UnitSetConstructionProgress(GetTriggerUnit(), 100)
	-- call RemoveUnit(GetConstructingStructure())
	-- call CreateUnit(Player(pi),id,x,y,0.00)
	
end
-- ===========================================================================
---@return nothing
function InitTrig_FastBuild()
	gg_trg_FastBuild = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FastBuild, EVENT_PLAYER_UNIT_CONSTRUCT_START)
	TriggerAddCondition(gg_trg_FastBuild, Condition(Trig_FastBuild_Conditions))
	TriggerAddAction(gg_trg_FastBuild, Trig_FastBuild_Actions)
end
-- ===========================================================================
--  Trigger: FastResearch
-- ===========================================================================
---@return boolean
function Trig_FastResearch_Conditions()
	
	return fastTest[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
---@return nothing
function Trig_FastResearch_Actions()
	SetPlayerTechResearchedSwap(GetResearched(), GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), GetResearched(), true) + 1, GetOwningPlayer(GetTriggerUnit()))
	IssueImmediateOrderById(GetTriggerUnit(), 851976)
end
-- ===========================================================================
---@return nothing
function InitTrig_FastResearch()
	gg_trg_FastResearch = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FastResearch, EVENT_PLAYER_UNIT_RESEARCH_START)
	TriggerAddCondition(gg_trg_FastResearch, Condition(Trig_FastResearch_Conditions))
	TriggerAddAction(gg_trg_FastResearch, Trig_FastResearch_Actions)
end