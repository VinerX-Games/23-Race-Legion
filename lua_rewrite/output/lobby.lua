--===========================================================================
-- Lobby, UI, Continents, and Game Start Systems
-- Converted from vJASS to Lua
-- Uses G.* and G.udg_* globals
--===========================================================================

--===========================================================================
-- InitThings
--===========================================================================
function InitThings()
    for i = 0, 24 do
        G.cap_time[i] = true
        G.Vassals[i] = CreateForce()
        G.Senior[i] = nil
        G.Capital[i] = nil
    end
end

--===========================================================================
-- PlayerUI / UISetup
--===========================================================================
function UISetup()
    local fh = nil
    local chatButton = nil
    local questButton = nil
    local allyButton = nil
    local MiniMap = nil
    local gridButtons = nil
    local imageTest = BlzCreateFrameByType("BACKDROP", "image", BlzGetFrameByName("ConsoleUIBackdrop", 0), "ButtonBackdropTemplate", 0)

    -- Top UI & System Buttons
    fh = BlzGetFrameByName("UpperButtonBarFrame", 0)
    BlzFrameSetVisible(fh, true)
    allyButton = BlzGetFrameByName("UpperButtonBarAlliesButton", 0)
    fh = BlzGetFrameByName("UpperButtonBarMenuButton", 0)
    chatButton = BlzGetFrameByName("UpperButtonBarChatButton", 0)
    questButton = BlzGetFrameByName("UpperButtonBarQuestsButton", 0)
    BlzFrameClearAllPoints(fh)
    BlzFrameClearAllPoints(allyButton)
    BlzFrameClearAllPoints(chatButton)
    BlzFrameClearAllPoints(questButton)
    BlzFrameSetAbsPoint(questButton, FRAMEPOINT_TOPLEFT, 0.05, 0.6)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPLEFT, -0.03, 0.6)
    BlzFrameSetAbsPoint(allyButton, FRAMEPOINT_TOPLEFT, 0.05, 0.583)
    BlzFrameSetAbsPoint(chatButton, FRAMEPOINT_TOPLEFT, -0.03, 0.583)

    -- Hiding clock UI and creating new frame bar
    BlzFrameSetTexture(imageTest, "UI\\ResourceBar.tga", 0, true)
    BlzFrameSetPoint(imageTest, FRAMEPOINT_TOP, BlzGetOriginFrame(ORIGIN_FRAME_WORLD_FRAME, 0), FRAMEPOINT_TOP, 0, 0)
    BlzFrameSetSize(imageTest, 0.52, 0.025)
    BlzFrameSetLevel(imageTest, 1)

    -- Food
    fh = BlzGetFrameByName("ResourceBarSupplyText", 0)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.640, 0.5965)

    -- Upkeep
    fh = BlzGetFrameByName("ResourceBarUpkeepText", 0)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.8, 0.6965)

    -- Gold
    fh = BlzGetFrameByName("ResourceBarGoldText", 0)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.329, 0.5965)

    -- Lumber
    fh = BlzGetFrameByName("ResourceBarLumberText", 0)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.546, 0.5965)

    -- Bottom UI & Idle Worker Icon
    fh = BlzGetFrameByName("ConsoleBottomBar", 0)
    fh = BlzFrameGetChild(fh, 3)
    BlzFrameClearAllPoints(fh)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.09, 0.179)

    -- Remove Deadspace
    fh = BlzGetFrameByName("ConsoleUI", 0)
    BlzFrameSetVisible(BlzFrameGetChild(fh, 5), false)

    -- Minimap
    MiniMap = BlzGetFrameByName("MiniMapFrame", 0)
    BlzFrameSetVisible(MiniMap, true)
    BlzFrameClearAllPoints(MiniMap)
    BlzFrameSetAbsPoint(MiniMap, FRAMEPOINT_BOTTOMLEFT, 0.0525, 0.0)
    BlzFrameSetAbsPoint(MiniMap, FRAMEPOINT_TOPRIGHT, 0.2125, 0.141)

    -- Minimap Buttons
    fh = BlzGetFrameByName("MiniMapCreepButton", 0)
    BlzFrameClearAllPoints(fh)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.214, 0.116)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.234, 0.136)
    BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
    fh = BlzGetFrameByName("MiniMapAllyButton", 0)
    BlzFrameClearAllPoints(fh)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.234, 0.116)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.254, 0.136)
    BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
    fh = BlzGetFrameByName("MiniMapTerrainButton", 0)
    BlzFrameClearAllPoints(fh)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.254, 0.116)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.274, 0.136)
    BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)
    fh = BlzGetFrameByName("MinimapSignalButton", 0)
    BlzFrameSetVisible(fh, false)
    fh = BlzGetFrameByName("FormationButton", 0)
    BlzFrameClearAllPoints(fh)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.274, 0.116)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.294, 0.136)
    BlzFrameSetTexture(fh, "UI\\ButtonBorder.dds", 0, true)

    -- Minimap Border
    fh = BlzCreateFrameByType("BACKDROP", "MinimapBorder", MiniMap, "", 0)
    BlzFrameSetPoint(fh, FRAMEPOINT_TOPLEFT, MiniMap, FRAMEPOINT_TOPLEFT, 0, 0)
    BlzFrameSetPoint(fh, FRAMEPOINT_BOTTOMRIGHT, MiniMap, FRAMEPOINT_BOTTOMRIGHT, 0, 0)
    BlzFrameSetTexture(fh, "UI\\MiniMapBorder.dds", 0, true)

    -- Tooltips
    fh = BlzGetOriginFrame(ORIGIN_FRAME_TOOLTIP, 0)
    BlzFrameSetVisible(fh, true)
    fh = BlzGetOriginFrame(ORIGIN_FRAME_UBERTOOLTIP, 0)
    BlzFrameSetVisible(fh, true)
    BlzFrameClearAllPoints(fh)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMRIGHT, 0.7725, 0.141)

    -- Command Buttons
    gridButtons = BlzGetFrameByName("CommandBarFrame", 0)
    BlzFrameSetVisible(gridButtons, true)
    BlzFrameClearAllPoints(gridButtons)
    BlzFrameSetAbsPoint(gridButtons, FRAMEPOINT_BOTTOMLEFT, 0.5950, 0.005)

    -- Backdrop
    fh = BlzGetFrameByName("ConsoleUIBackdrop", 0)
    BlzFrameClearAllPoints(fh)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_BOTTOMLEFT, 0.052, 0)
    BlzFrameSetAbsPoint(fh, FRAMEPOINT_TOPRIGHT, 0.770, 0.141)

    -- Command buttons border
    fh = BlzCreateFrameByType("BACKDROP", "CommandBorder", MiniMap, "", 0)
    BlzFrameSetPoint(fh, FRAMEPOINT_TOPLEFT, gridButtons, FRAMEPOINT_TOPLEFT, -0.007, 0.007)
    BlzFrameSetPoint(fh, FRAMEPOINT_BOTTOMRIGHT, gridButtons, FRAMEPOINT_BOTTOMRIGHT, 0.0025, -0.005)
    BlzFrameSetTexture(fh, "UI\\CommandCard.dds", 0, true)

    -- Expand TextArea
    BlzFrameSetPoint(BlzGetFrameByName("QuestDisplay", 0), FRAMEPOINT_TOPLEFT, BlzGetFrameByName("QuestDetailsTitle", 0), FRAMEPOINT_BOTTOMLEFT, 0.003, -0.003)
    BlzFrameSetPoint(BlzGetFrameByName("QuestDisplay", 0), FRAMEPOINT_BOTTOMRIGHT, BlzGetFrameByName("QuestDisplayBackdrop", 0), FRAMEPOINT_BOTTOMRIGHT, -0.003, 0.)

    -- Relocate button
    BlzFrameSetPoint(BlzGetFrameByName("QuestDisplayBackdrop", 0), FRAMEPOINT_BOTTOM, BlzGetFrameByName("QuestBackdrop", 0), FRAMEPOINT_BOTTOM, 0., 0.017)
    BlzFrameClearAllPoints(BlzGetFrameByName("QuestAcceptButton", 0))
    BlzFrameSetPoint(BlzGetFrameByName("QuestAcceptButton", 0), FRAMEPOINT_TOPRIGHT, BlzGetFrameByName("QuestBackdrop", 0), FRAMEPOINT_TOPRIGHT, -0.016, -0.016)
    BlzFrameSetText(BlzGetFrameByName("QuestAcceptButton", 0), "\195\151")
    BlzFrameSetSize(BlzGetFrameByName("QuestAcceptButton", 0), 0.03, 0.03)

    -- Add back ally resource icons
    BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyGoldIcon", 7), "UI\\RGReplacement.dds", 0, false)
    BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyWoodIcon", 7), "UI\\RLReplacement.dds", 0, false)
    BlzFrameSetTexture(BlzGetFrameByName("InfoPanelIconAllyFoodIcon", 7), "UI\\RSReplacement.dds", 0, false)
end

--===========================================================================
-- Face2 / IncomeTooltip
--===========================================================================
function Face2()
    BlzLoadTOCFile("war3mapimported\\BoxedText.toc")
    G.face = BlzCreateFrameByType("BACKDROP", "Face", BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0), "", 0)
    G.faceHover = BlzCreateFrameByType("FRAME", "FaceFrame", G.face, "", 0)
    G.IncomeTextFr = BlzCreateFrameByType("TEXT", "MyTextFrame", BlzGetOriginFrame(ORIGIN_FRAME_GAME_UI, 0), "", 0)
    G.tooltip = BlzCreateFrame("BoxedText", G.face, 0, 0)
    G.tooltipBody = BlzGetFrameByName("BoxedTextValue", 0)
    G.tooltipTitle = BlzGetFrameByName("BoxedTextTitle", 0)
    BlzFrameSetText(G.IncomeTextFr, "999999")
    BlzFrameSetAbsPoint(G.IncomeTextFr, FRAMEPOINT_TOPRIGHT, 0.2337, 0.5937)
    BlzFrameSetEnable(G.IncomeTextFr, false)
    BlzFrameSetScale(G.IncomeTextFr, 1.075)
    BlzFrameSetTextAlignment(G.IncomeTextFr, TEXT_JUSTIFY_CENTER, TEXT_JUSTIFY_LEFT)
    BlzFrameSetAllPoints(G.faceHover, G.face)
    BlzFrameSetTooltip(G.faceHover, G.tooltip)

    BlzFrameSetSize(G.face, 0.085, 0.015)
    BlzFrameSetAbsPoint(G.face, FRAMEPOINT_TOPRIGHT, 0.239, 0.5965)
    BlzFrameSetAbsPoint(G.tooltip, FRAMEPOINT_TOPRIGHT, 0.289, 0.5685)
    BlzFrameSetPoint(G.tooltip, FRAMEPOINT_BOTTOM, G.face, FRAMEPOINT_TOP, 0.0, -0.1)
    BlzFrameSetSize(G.tooltip, 0.03, 0.03)

    BlzFrameSetText(G.tooltipBody, "\208\152\208\189\208\186\208\190\208\188 = \208\148\208\190\209\133\208\190\208\180\209\139-\208\160\208\176\209\129\209\133\208\190\208\180\209\139")
    BlzFrameSetText(G.tooltipTitle, "\208\152\208\189\208\186\208\190\208\188")

    BlzFrameSetTexture(G.face, "ResourceBar222.tga", 0, true)
end

--===========================================================================
-- AllPlayersStart
--===========================================================================
function AllPlayersStart()
    for i = 0, 22 do
        if GetPlayerSlotState(Player(i)) == PLAYER_SLOT_STATE_PLAYING then
            ForceAddPlayer(G.udg_AllPlayers, Player(i))
            ForceAddPlayer(G.udg_AllPlayers2, Player(i))
        end
    end
end

--===========================================================================
-- aiStart
--===========================================================================
function aiStart()
    for i = 0, 22 do
        if GetPlayerController(Player(i)) == MAP_CONTROL_COMPUTER then
            createAiPlayer(i)
        end
    end
end

--===========================================================================
-- ClearAllies
--===========================================================================
function BrokeOneAlliance()
    SetPlayerAllianceStateBJ(G.gPlayer, GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
    SetPlayerAllianceStateBJ(GetEnumPlayer(), G.gPlayer, bj_ALLIANCE_UNALLIED)
end

function ClearAllies(p)
    G.gPlayer = p
    ForForce(GetPlayersAllies(G.gPlayer), BrokeOneAlliance)
end

--===========================================================================
-- DelUnitStart
--===========================================================================
function DelUnut()
    RemoveUnit(G.ModeBuilding)
end

--===========================================================================
-- CreateRaceCircles
--===========================================================================
function CreateRaceCircles(p)
    local l = G.StartLoc[GetRandomInt(0, G.StartLocCount - 1)]
    CreateUnitAtLoc(p, FourCC("h0HJ"), l, 0)
    PanCameraToTimedLocForPlayer(p, l, 0)
end

--===========================================================================
-- MainInfo Trigger
--===========================================================================
function Trig_MainInfo_Actions()
    CreateQuestBJ(bj_QUESTTYPE_REQ_DISCOVERED, "TRIGSTR_20894", "TRIGSTR_20895", "ReplaceableTextures\\CommandButtons\\BTNPhilosophersStone.blp")
    CreateQuestBJ(bj_QUESTTYPE_OPT_DISCOVERED, "TRIGSTR_20896", "TRIGSTR_20914", "ReplaceableTextures\\CommandButtons\\BTNPhilosophersStone.blp")
    CreateQuestBJ(bj_QUESTTYPE_OPT_DISCOVERED, "TRIGSTR_20922", "TRIGSTR_20987", "ReplaceableTextures\\CommandButtons\\BTNTransmute.blp")
end

--===========================================================================
-- Initial_things Trigger
--===========================================================================
function Trig_Initial_things_Func003A()
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, G.gg_rct_Shops)
    CameraSetupApplyForPlayer(true, G.gg_cam_Camera_001, GetEnumPlayer(), 0)
    SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_RESOURCE_LUMBER, 4000)
    SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_RESOURCE_GOLD, 5000)
    SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_FOOD_CAP_CEILING, 3)
    SetPlayerStateBJ(GetEnumPlayer(), PLAYER_STATE_RESOURCE_FOOD_USED, 0)
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_MASKED, GetPlayableMapRect())
    G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())] = GetLastCreatedFogModifier()
end

function Trig_Initial_things_Func019A()
    SetPlayerAbilityAvailableBJ(false, FourCC("A0IQ"), GetEnumPlayer())
end

function Trig_Initial_things_Actions()
    AllPlayersStart()
    ForForce(G.udg_AllPlayers, Trig_Initial_things_Func003A)
    SetPlayerStateBJ(Player(PLAYER_NEUTRAL_AGGRESSIVE), PLAYER_STATE_RESOURCE_GOLD, 100000000)
    SetPlayerStateBJ(Player(PLAYER_NEUTRAL_AGGRESSIVE), PLAYER_STATE_RESOURCE_LUMBER, 100000000)
    SetPlayerStateBJ(Player(PLAYER_NEUTRAL_PASSIVE), PLAYER_STATE_RESOURCE_GOLD, 100000)
    SetPlayerStateBJ(Player(PLAYER_NEUTRAL_PASSIVE), PLAYER_STATE_RESOURCE_LUMBER, 100000)
    StartInc()
    InitThings()
    SetStartLocations()
    SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
    SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
    SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
    SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
    SetGameSpeed(MAP_SPEED_FASTEST)
    ForForce(G.udg_AllPlayers, Trig_Initial_things_Func019A)
end

--===========================================================================
-- StartLobby Trigger
--===========================================================================
function Trig_StartLobby_Func004Func001A()
    CameraSetupApplyForPlayer(true, G.gg_cam_GW1, GetEnumPlayer(), 0)
end

function Trig_StartLobby_Func005Func001A()
    CameraSetupApplyForPlayer(true, G.gg_cam_GW2, GetEnumPlayer(), 0)
end

function Trig_StartLobby_Func006Func001A()
    CameraSetupApplyForPlayer(true, G.gg_cam_GW3, GetEnumPlayer(), 0)
end

function Trig_StartLobby_Func007Func001A()
    CameraSetupApplyForPlayer(true, G.gg_cam_GW4, GetEnumPlayer(), 0)
end

function Trig_StartLobby_Func008Func001A()
    CameraSetupApplyForPlayer(true, G.gg_cam_GW5, GetEnumPlayer(), 0)
end

function Trig_StartLobby_Func015Func003C()
    return GetEnumPlayer() ~= Player(0)
end

function Trig_StartLobby_Func015A()
    CameraSetupApplyForPlayer(true, G.gg_cam_HostRegion, GetEnumPlayer(), 0)
    SetCameraFieldForPlayer(GetEnumPlayer(), CAMERA_FIELD_TARGET_DISTANCE, 3400.00, 0.00)
    if Trig_StartLobby_Func015Func003C() then
        G.udg_LocalPosition2 = GetRandomLocInRect(G.gg_rct_HostRegion)
        CreateNUnitsAtLoc(1, FourCC("h0GA"), GetEnumPlayer(), G.udg_LocalPosition2, bj_UNIT_FACING)
        RemoveLocation(G.udg_LocalPosition2)
    end
end

function Trig_StartLobby_Actions()
    local li = GetRandomInt(1, 5)
    G.udg_LocalPosition2 = GetRectCenter(G.gg_rct_HostRegion)
    G.udg_LocalInteger = li
    if li == 1 then
        ForForce(G.udg_AllPlayers, Trig_StartLobby_Func004Func001A)
    elseif li == 2 then
        ForForce(G.udg_AllPlayers, Trig_StartLobby_Func005Func001A)
    elseif li == 3 then
        ForForce(G.udg_AllPlayers, Trig_StartLobby_Func006Func001A)
    elseif li == 4 then
        ForForce(G.udg_AllPlayers, Trig_StartLobby_Func007Func001A)
    elseif li == 5 then
        ForForce(G.udg_AllPlayers, Trig_StartLobby_Func008Func001A)
    end
    G.udg_LocalInteger = 4
    DisplayTimedTextToForce(GetPlayersAll(), G.udg_LocalInteger, "TRIGSTR_10982")
    TriggerSleepAction(1)
    ForForce(G.udg_AllPlayers, Trig_StartLobby_Func015A)
    RemoveLocation(G.udg_LocalPosition2)
    StartTimerBJ(G.udg_LobbyTime, false, 60.00)
    CreateTimerDialogBJ(GetLastCreatedTimerBJ(), "TRIGSTR_19360")
    G.udg_LobbyTimerWindows = GetLastCreatedTimerDialogBJ()
    CreateNUnitsAtLoc(1, FourCC("n04G"), Player(0), GetRectCenter(GetPlayableMapRect()), bj_UNIT_FACING)
    G.ModeBuilding = GetLastCreatedUnit()
    SelectUnitForPlayerSingle(GetLastCreatedUnit(), Player(0))
end

--===========================================================================
-- EndLobby_and_Start_game Trigger
--===========================================================================
function Trig_EndLobby_and_Start_game_Func004A()
    CreateRaceCircles(GetEnumPlayer())
    ClearAllies(GetEnumPlayer())
    CreateArmyBonusUnit(GetEnumPlayer())
    FogModifierStop(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    if G.udg_Continents[0] == 0 then
        CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
        ConditionalTriggerExecute(G.gg_trg_SeeOnlyNeedeed)
    end
end

function Trig_EndLobby_and_Start_game_Func005A()
    RemoveUnit(GetEnumUnit())
end

function Trig_EndLobby_and_Start_game_Actions()
    TimerDialogDisplayBJ(false, G.udg_LobbyTimerWindows)
    DestroyTimerDialogBJ(G.udg_LobbyTimerWindows)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19369")
    ForForce(G.udg_AllPlayers, Trig_EndLobby_and_Start_game_Func004A)
    ForGroupBJ(GetUnitsInRectAll(G.gg_rct_HostReg2), Trig_EndLobby_and_Start_game_Func005A)
    DisableTrigger(G.gg_trg_SaveSelection)
    BlzEnableSelections(true, true)
    RemoveUnit(G.ModeBuilding)
    ConditionalTriggerExecute(G.gg_trg_StartDal)
    ConditionalTriggerExecute(G.gg_trg_NaxStart)
    ConditionalTriggerExecute(G.gg_trg_TurtleStart)
    aiStart()
end

--===========================================================================
-- AddMinute Trigger
--===========================================================================
function Trig_AddMinute_Conditions()
    return GetSpellAbilityId() == FourCC("A0UJ")
end

function Trig_AddMinute_Actions()
    StartTimerBJ(G.udg_LobbyTime, false, TimerGetRemaining(G.udg_LobbyTime) + 60.00)
    DisableTrigger(GetTriggeringTrigger())
end

--===========================================================================
-- StartGameFast Trigger
--===========================================================================
function Trig_StartGameFast_Conditions()
    return GetSpellAbilityId() == FourCC("A0UK")
end

function Trig_StartGameFast_Actions()
    StartTimerBJ(G.udg_LobbyTime, false, 5.00)
end

--===========================================================================
-- LeaveStart Trigger
--===========================================================================
function Trig_LeaveStart_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC("H049")
end

function Trig_LeaveStart_Actions()
    BlzSetUnitRealFieldBJ(GetTriggerUnit(), UNIT_RF_MANA_REGENERATION, 300)
end

--===========================================================================
-- NextMenu Trigger
--===========================================================================
function Trig_NextMenu_Conditions()
    return GetSpellAbilityId() == FourCC("A0Y5")
end

function Trig_NextMenu_Actions()
    local l = Location(0, 0)

    G.ModeBuildingI = G.ModeBuildingI + 1
    if G.ModeBuildingI > 6 then
        G.ModeBuildingI = 0
    end
    KillUnit(G.ModeBuilding)
    RemoveUnit(G.ModeBuilding)
    if G.ModeBuildingI == 0 then
        G.ModeBuilding = CreateUnitAtLoc(Player(0), FourCC("n04G"), l, 0)
    elseif G.ModeBuildingI == 1 then
        G.ModeBuilding = CreateUnitAtLoc(Player(0), FourCC("n04D"), l, 0)
    elseif G.ModeBuildingI == 2 then
        G.ModeBuilding = CreateUnitAtLoc(Player(0), FourCC("n04F"), l, 0)
    elseif G.ModeBuildingI == 3 then
        G.ModeBuilding = CreateUnitAtLoc(Player(0), FourCC("n04H"), l, 0)
    elseif G.ModeBuildingI == 4 then
        G.ModeBuilding = CreateUnitAtLoc(Player(0), FourCC("n04I"), l, 0)
    elseif G.ModeBuildingI == 5 then
        G.ModeBuilding = CreateUnitAtLoc(Player(0), FourCC("n06Y"), l, 0)
    elseif G.ModeBuildingI == 6 then
        G.ModeBuilding = CreateUnitAtLoc(Player(0), FourCC("n074"), l, 0)
    end
    ClearSelectionForPlayer(Player(0))
    SelectUnitForPlayerSingle(G.ModeBuilding, Player(0))

    RemoveLocation(l)
end

--===========================================================================
-- SaveSelection Trigger
--===========================================================================
function Trig_SaveSelection_Actions()
    local u = GetTriggerUnit()
    if u == G.ModeBuilding then
        SelectUnitForPlayerSingle(u, GetOwningPlayer(u))
    end
end

--===========================================================================
-- Page1 (Race Page 1: Alliance, Horde, etc.)
--===========================================================================
function Trig_Page1_Conditions()
    return GetSpellAbilityId() == FourCC("A0I1")
end

function Trig_Page1_Actions()
    local u = GetTriggerUnit()
    UnitAddAbilityBJ(FourCC("A0HZ"), u)
    UnitRemoveAbilityBJ(FourCC("A0I1"), u)

    UnitAddAbilityBJ(FourCC("A02A"), u)
    UnitAddAbilityBJ(FourCC("A0YV"), u)
    UnitAddAbilityBJ(FourCC("A0HV"), u)
    UnitAddAbilityBJ(FourCC("A0HL"), u)

    UnitAddAbilityBJ(FourCC("A0HQ"), u)
    UnitAddAbilityBJ(FourCC("A14O"), u)
    UnitAddAbilityBJ(FourCC("A0OK"), u)
    UnitAddAbilityBJ(FourCC("A0MY"), u)
    UnitAddAbilityBJ(FourCC("A0HS"), u)

    UnitRemoveAbilityBJ(FourCC("A0QN"), u)
    UnitRemoveAbilityBJ(FourCC("A0HT"), u)
    UnitRemoveAbilityBJ(FourCC("A0QQ"), u)

    UnitRemoveAbilityBJ(FourCC("A0RQ"), u)
    UnitRemoveAbilityBJ(FourCC("A0J7"), u)
    UnitRemoveAbilityBJ(FourCC("A1HA"), u)

    UnitRemoveAbilityBJ(FourCC("A1JN"), u)
    UnitRemoveAbilityBJ(FourCC("A0HW"), u)
end

--===========================================================================
-- Page2 (Race Page 2: Scarlet, Strom, etc.)
--===========================================================================
function Trig_Page2_Conditions()
    return GetSpellAbilityId() == FourCC("A0HZ")
end

function Trig_Page2_Actions()
    local u = GetTriggerUnit()
    UnitRemoveAbilityBJ(GetSpellAbilityId(), u)
    UnitAddAbilityBJ(FourCC("A1GW"), u)

    UnitAddAbilityBJ(FourCC("A0HM"), u)
    UnitAddAbilityBJ(FourCC("A0Y0"), u)
    UnitAddAbilityBJ(FourCC("A1EG"), u)

    UnitAddAbilityBJ(FourCC("A121"), u)
    UnitAddAbilityBJ(FourCC("A0HN"), u)
    UnitAddAbilityBJ(FourCC("A1FN"), u)

    UnitAddAbilityBJ(FourCC("A0HR"), u)
    UnitAddAbilityBJ(FourCC("A0HO"), u)
    UnitAddAbilityBJ(FourCC("A1DZ"), u)

    UnitRemoveAbilityBJ(FourCC("A02A"), u)
    UnitRemoveAbilityBJ(FourCC("A0YV"), u)
    UnitRemoveAbilityBJ(FourCC("A0HV"), u)
    UnitRemoveAbilityBJ(FourCC("A0HL"), u)

    UnitRemoveAbilityBJ(FourCC("A0HQ"), u)
    UnitRemoveAbilityBJ(FourCC("A14O"), u)
    UnitRemoveAbilityBJ(FourCC("A0OK"), u)
    UnitRemoveAbilityBJ(FourCC("A0MY"), u)
    UnitRemoveAbilityBJ(FourCC("A0HS"), u)
end

--===========================================================================
-- Page3 (Race Page 3: Gnomes, Goblins, etc.)
--===========================================================================
function Trig_Page3_Conditions()
    return GetSpellAbilityId() == FourCC("A1GW")
end

function Trig_Page3_Actions()
    local u = GetTriggerUnit()
    UnitAddAbilityBJ(FourCC("A0SD"), u)
    UnitAddAbilityBJ(FourCC("A0AC"), u)
    UnitAddAbilityBJ(FourCC("A0HU"), u)

    UnitAddAbilityBJ(FourCC("A0HP"), u)
    UnitAddAbilityBJ(FourCC("A17N"), u)
    UnitAddAbilityBJ(FourCC("A155"), u)

    UnitAddAbilityBJ(FourCC("A1I6"), u)
    UnitAddAbilityBJ(FourCC("A0HX"), u)
    UnitAddAbilityBJ(FourCC("A1JL"), u)

    UnitRemoveAbilityBJ(FourCC("A0HM"), u)
    UnitRemoveAbilityBJ(FourCC("A0Y0"), u)
    UnitRemoveAbilityBJ(FourCC("A1EG"), u)

    UnitRemoveAbilityBJ(FourCC("A121"), u)
    UnitRemoveAbilityBJ(FourCC("A0HN"), u)
    UnitRemoveAbilityBJ(FourCC("A1FN"), u)

    UnitRemoveAbilityBJ(FourCC("A0HR"), u)
    UnitRemoveAbilityBJ(FourCC("A0HO"), u)
    UnitRemoveAbilityBJ(FourCC("A1DZ"), u)

    UnitAddAbilityBJ(FourCC("A0QR"), u)
    UnitRemoveAbilityBJ(GetSpellAbilityId(), u)
end

--===========================================================================
-- Page4 (Race Page 4: Elementals, Nerubians, etc.)
--===========================================================================
function Trig_Page4_Conditions()
    return GetSpellAbilityId() == FourCC("A0QR")
end

function Trig_Page4_Actions()
    local u = GetTriggerUnit()
    UnitAddAbilityBJ(FourCC("A0QN"), u)
    UnitAddAbilityBJ(FourCC("A0HT"), u)
    UnitAddAbilityBJ(FourCC("A0QQ"), u)

    UnitAddAbilityBJ(FourCC("A0RQ"), u)
    UnitAddAbilityBJ(FourCC("A0J7"), u)
    UnitAddAbilityBJ(FourCC("A1HA"), u)

    UnitAddAbilityBJ(FourCC("A1JN"), u)
    UnitAddAbilityBJ(FourCC("A0HW"), u)

    UnitRemoveAbilityBJ(FourCC("A0SD"), u)
    UnitRemoveAbilityBJ(FourCC("A0AC"), u)
    UnitRemoveAbilityBJ(FourCC("A0HU"), u)

    UnitRemoveAbilityBJ(FourCC("A0HP"), u)
    UnitRemoveAbilityBJ(FourCC("A17N"), u)
    UnitRemoveAbilityBJ(FourCC("A155"), u)

    UnitRemoveAbilityBJ(FourCC("A1I6"), u)
    UnitRemoveAbilityBJ(FourCC("A0HX"), u)
    UnitRemoveAbilityBJ(FourCC("A1JL"), u)

    UnitAddAbility(u, FourCC("A0I1"))
    UnitRemoveAbility(u, GetSpellAbilityId())
end

--===========================================================================
-- Mod_classic Trigger
--===========================================================================
function Trig_Mod_classic_Actions()
    G.udg_GameMode = 0
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19403")
end

function Trig_Mod_classic_spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0T4")
end

function Trig_Mod_classic_spell_Actions()
    G.udg_GameMode = 0
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_21887")
end

--===========================================================================
-- MOD Combo Trigger
--===========================================================================
function Trig_MOD_Combo_Conditions()
    return GetSpellAbilityId() == FourCC("A1M4")
end

function Trig_MOD_Combo_Actions()
    G.udg_GameMode = 5
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_5722")
end

--===========================================================================
-- MOD_stolica_Set Trigger
--===========================================================================
function Trig_MOD_stolica_Set_Actions()
    G.udg_GameMode = 1
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19369")
end

--===========================================================================
-- MOD_stolica_Start Trigger
--===========================================================================
function Trig_MOD_stolica_Start_Conditions()
    return G.udg_GameMode == 1
end

function Trig_MOD_stolica_Start_Func005A()
    SetPlayerAbilityAvailableBJ(true, FourCC("A0IQ"), GetEnumPlayer())
end

function Trig_MOD_stolica_Start_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "TRIGSTR_19372")
    ForForce(G.udg_AllPlayers, Trig_MOD_stolica_Start_Func005A)
    EnableTrigger(G.gg_trg_MakeStolica)
    EnableTrigger(G.gg_trg_UpgradeStolica)
    EnableTrigger(G.gg_trg_StolicaDead)
    EnableTrigger(G.gg_trg_StolicaTime)
    TriggerExecute(G.gg_trg_RebebmerToBuild)
end

--===========================================================================
-- MOD_stolica_Start_Copy (GameMode == 5: Combo)
--===========================================================================
function Trig_MOD_stolica_Start_Copy_Conditions()
    return G.udg_GameMode == 5
end

function Trig_MOD_stolica_Start_Copy_Func005A()
    SetPlayerAbilityAvailableBJ(true, FourCC("A0IQ"), GetEnumPlayer())
end

function Trig_MOD_stolica_Start_Copy_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "TRIGSTR_5726")
    ForForce(G.udg_AllPlayers, Trig_MOD_stolica_Start_Copy_Func005A)
    EnableTrigger(G.gg_trg_MakeStolica)
    EnableTrigger(G.gg_trg_UpgradeStolica)
    EnableTrigger(G.gg_trg_StolicaDead)
    EnableTrigger(G.gg_trg_StolicaTime)
    TriggerExecute(G.gg_trg_RebebmerToBuild)
end

--===========================================================================
-- MOD_feoda_O_Set Trigger
--===========================================================================
function Trig_MOD_feoda_O_Set_Actions()
    G.udg_GameMode = 2
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19397")
end

function Trig_MOD_feoda_O_Set_Spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0T6")
end

function Trig_MOD_feoda_O_Set_Spell_Actions()
    G.udg_GameMode = 2
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19605")
end

--===========================================================================
-- MOD_feoda_O_Start Trigger
--===========================================================================
function Trig_MOD_feoda_O_Start_Conditions()
    return G.udg_GameMode == 2
end

function Trig_MOD_feoda_O_Start_Func006A()
    SetPlayerAbilityAvailableBJ(true, FourCC("A0IQ"), GetEnumPlayer())
end

function Trig_MOD_feoda_O_Start_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "TRIGSTR_19378")
    SetForceAllianceStateBJ(G.udg_AllPlayers, G.udg_AllPlayers, bj_ALLIANCE_UNALLIED)
    ForForce(G.udg_AllPlayers, Trig_MOD_feoda_O_Start_Func006A)
    EnableTrigger(G.gg_trg_MakeStolica)
    EnableTrigger(G.gg_trg_UpgradeStolica)
    EnableTrigger(G.gg_trg_StolicaTime)
    EnableTrigger(G.gg_trg_StolicaDead)
    TriggerExecute(G.gg_trg_RebebmerToBuild)
end

--===========================================================================
-- FastTestSpell Trigger
--===========================================================================
function Trig_FastTestSpell_Conditions()
    return GetSpellAbilityId() == FourCC("A1MB")
end

function Trig_FastTestSpell_Actions()
    G.udg_GameMode = 4
    DisplayTextToForce(GetPlayersAll(), "\208\160\208\181\208\182\208\184\208\188 \208\178\209\139\208\177\209\128\208\176\208\189: \208\162\208\181\209\129\209\130. \208\159\208\184\209\136\208\184\209\130\208\181 -fast \208\184 -fastoff ")
end

--===========================================================================
-- Timer Trigger
--===========================================================================
function Trig_Timer_Func009Func001A()
    SetPlayerAbilityAvailableBJ(false, FourCC("A0IQ"), GetEnumPlayer())
end

function Trig_Timer_Func009C()
    return G.udg_GameMode == 0
end

function Trig_Timer_Actions()
    G.udg_AllPlayers = GetPlayersAll()
    StartTimerBJ(G.udg_IncomeTimerSecond, true, G.udg_SET_TimerTime)
    CreateTimerDialogBJ(GetLastCreatedTimerBJ(), "TRIGSTR_4633")
    G.udg_TimerSecond = GetLastCreatedTimerDialogBJ()
    StartTimerBJ(G.udg_IncomeTimerFirst, false, 600.00)
    CreateTimerDialogBJ(GetLastCreatedTimerBJ(), "TRIGSTR_7397")
    G.udg_TimerToDis = GetLastCreatedTimerDialogBJ()
    if Trig_Timer_Func009C() then
        ForForce(G.udg_AllPlayers, Trig_Timer_Func009Func001A)
    end
end

--===========================================================================
-- ChangeTimerHost Trigger
--===========================================================================
function Trig_ChangeTimerHost_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19902")
    G.udg_SET_TimerTime = S2I(SubStringBJ(GetEventPlayerChatString(), 7, 8))
    StartTimerBJ(G.udg_IncomeTimerSecond, true, G.udg_SET_TimerTime)
end

--===========================================================================
-- Standart Trigger (visibility mode)
--===========================================================================
function Trig_Standart_Conditions()
    return GetSpellAbilityId() == FourCC("A0UT")
end

function Trig_Standart_Actions()
    G.udg_SET_VISIBLE_MODE = 0
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19654")
end

--===========================================================================
-- DarkMode Spell Trigger
--===========================================================================
function Trig_DarkMode_Spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UL")
end

function Trig_DarkMode_Spell_Actions()
    G.udg_SET_VISIBLE_MODE = 1
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19693")
end

--===========================================================================
-- OpenModeSpell Trigger
--===========================================================================
function Trig_OpenModeSpell_Conditions()
    return GetSpellAbilityId() == FourCC("A131")
end

function Trig_OpenModeSpell_Actions()
    G.udg_SET_VISIBLE_MODE = 2
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_25625")
end

--===========================================================================
-- StartDarkMode Trigger
--===========================================================================
function Trig_StartDarkMode_Conditions()
    return G.udg_SET_VISIBLE_MODE == 1
end

function Trig_StartDarkMode_Func006A()
    FogModifierStop(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_MASKED, GetPlayableMapRect())
end

function Trig_StartDarkMode_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20065")
    TriggerSleepAction(30.00)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20066")
    TriggerSleepAction(30.00)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20067")
    ForForce(G.udg_AllPlayers, Trig_StartDarkMode_Func006A)
end

--===========================================================================
-- StartOpenMode Trigger
--===========================================================================
function Trig_StartOpenMode_Conditions()
    return G.udg_SET_VISIBLE_MODE == 2
end

function Trig_StartOpenMode_Func002A()
    FogModifierStop(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
end

function Trig_StartOpenMode_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_7375")
    ForForce(G.udg_AllPlayers, Trig_StartOpenMode_Func002A)
end

--===========================================================================
-- StartDarkMode_Command / OfDarkModeCommand
--===========================================================================
function Trig_StartDarkMode_Command_Func003A()
    FogModifierStop(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_MASKED, GetPlayableMapRect())
end

function Trig_StartDarkMode_Command_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20055")
    ForForce(G.udg_AllPlayers, Trig_StartDarkMode_Command_Func003A)
end

function Trig_OfDarkModeCommand_Func002A()
    FogModifierStop(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(G.udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
end

function Trig_OfDarkModeCommand_Actions()
    ForForce(G.udg_AllPlayers, Trig_OfDarkModeCommand_Func002A)
end

--===========================================================================
-- StartAlly Trigger
--===========================================================================
function WritePlayerName()
    DisplayTextToForce(G.udg_AllPlayers, "\208\152\208\179\209\128\208\190\208\186\208\190\208\188: " .. GetPlayerName(GetEnumPlayer()))
end

function Trig_StartAlly_Actions()
    local p = GetTriggerPlayer()
    local AllyCount = 0
    ForceEnumAllies(G.gForce, p, nil)
    AllyCount = CountPlayersInForceBJ(G.gForce)
    if G.DipMode == 0 then
        if AllyCount > 1 then
            DisplayTextToForce(G.udg_AllPlayers, "\208\152\208\179\209\128\208\190\208\186 " .. GetPlayerName(p) .. " \208\183\208\176\208\186\208\187\209\142\209\135\208\184\208\187 \209\129\208\190\209\142\208\183 \209\129 \208\177\208\190\208\187\208\181\208\181 \209\135\208\181\208\188 \208\190\208\180\208\189\208\184\208\188!")
            ForForce(G.gForce, WritePlayerName)
        end
    else
        if AllyCount > G.DipMode then
            ClearAllies(p)
            DisplayTextToForce(G.udg_AllPlayers, "\208\152\208\179\209\128\208\190\208\186 " .. GetPlayerName(p) .. " \208\183\208\176\208\186\208\187\209\142\209\135\208\184\208\187 \209\129\208\187\208\184\209\136\208\186\208\190\208\188 \208\188\208\189\208\190\208\179\208\190 \209\129\208\190\209\142\208\183\208\190\208\178, \208\181\208\179\208\190 \208\176\208\187\209\140\209\143\208\189\209\129\209\139 \209\129\208\177\209\128\208\190\209\136\208\181\208\189\209\139")
        end
    end
    G.AllyTax[GetPlayerId(p)] = 0.1 * AllyCount
    ForceClear(G.gForce)
end

--===========================================================================
-- NoDipFFA Trigger
--===========================================================================
function Trig_NoDipFFA_Conditions()
    return GetSpellAbilityId() == FourCC("A1KR")
end

function Trig_NoDipFFA_Actions()
    G.DipMode = 1
    DisplayTextToForce(GetPlayersAll(), "\208\161\208\190\209\142\208\183\209\139 \208\190\209\130\208\186\208\187\209\142\209\135\208\181\208\189\209\139. \208\148\208\176 \208\189\208\176\209\135\208\189\209\131\209\130\209\129\209\143 \208\179\208\190\208\187\208\190\208\180\208\189\209\139\208\181 \208\184\208\179\209\128\209\139.")
end

--===========================================================================
-- Dip2 Trigger
--===========================================================================
function Trig_Dip2_Conditions()
    return GetSpellAbilityId() == FourCC("A1KS")
end

function Trig_Dip2_Actions()
    G.DipMode = 2
    DisplayTextToForce(GetPlayersAll(), "\208\146\208\186\208\187\209\142\209\135\208\181\208\189\209\139 \209\129\208\190\209\142\208\183\209\139 \208\191\208\190 2")
end

--===========================================================================
-- Dip3 Trigger
--===========================================================================
function Trig_Dip3_Conditions()
    return GetSpellAbilityId() == FourCC("A1KT")
end

function Trig_Dip3_Actions()
    G.DipMode = 3
    DisplayTextToForce(GetPlayersAll(), "\208\146\208\186\208\187\209\142\209\135\208\181\208\189\209\139 \209\129\208\190\209\142\208\183\209\139 \208\191\208\190 3")
end

--===========================================================================
-- FreeDip Trigger
--===========================================================================
function Trig_FreeDip_Conditions()
    return GetSpellAbilityId() == FourCC("A1KQ")
end

function Trig_FreeDip_Actions()
    G.DipMode = 0
    DisplayTextToForce(GetPlayersAll(), "\208\146\208\186\208\187\209\142\209\135\208\181\208\189\208\176 \209\129\208\178\208\190\208\177\208\190\208\180\208\189\208\176\209\143 \208\180\208\184\208\191\208\187\208\190\208\188\208\176\209\130\208\184\209\143")
end

--===========================================================================
-- DipStart Trigger
--===========================================================================
function ClearPlayerEach()
    ClearOldAllies(GetEnumPlayer())
end

function Trig_DipStart_Actions()
    if G.DipMode == 1 then
        SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, true)
        SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, true)
        SetMapFlag(MAP_LOCK_RESOURCE_TRADING, true)
        ForForce(G.udg_AllPlayers2, ClearPlayerEach)
    else
        SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
        SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
        SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
    end
end

--===========================================================================
-- Income075 / Income100 Triggers
--===========================================================================
function Trig_Income075_Conditions()
    return GetSpellAbilityId() == FourCC("A1N6")
end

function Trig_Income075_Actions()
    G.IncomeMod = 0.75
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\209\133\208\190\208\180\209\139 \209\130\208\181\208\191\208\181\209\128\209\140 75% \208\190\209\130 \208\189\208\190\209\128\208\188\208\176\208\187\209\140\208\189\209\139\209\133")
end

function Trig_Income100_Conditions()
    return GetSpellAbilityId() == FourCC("A1N7")
end

function Trig_Income100_Actions()
    G.IncomeMod = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\209\133\208\190\208\180\209\139 \209\131\209\129\209\130\208\176\208\189\208\190\208\178\208\187\208\181\208\189\209\139 \208\191\208\190 \209\131\208\188\208\190\208\187\209\135\208\176\208\189\208\184\209\142")
end

--===========================================================================
-- StartTotalProductionCommon / StartTotalProductionPlayer / EndTotalProductionPlayer
--===========================================================================
function Trig_StartTotalProductionCommon_Conditions()
    return GetSpellAbilityId() == FourCC("A1KC")
end

function Trig_StartTotalProductionCommon_Actions()
    G.TotalProduction = true
    for i = 0, 22 do
        SetPlayerAbilityAvailable(Player(i), FourCC("A1KH"), true)
    end
end

function Trig_StartTotalProductionPlayer_Conditions()
    return GetSpellAbilityId() == FourCC("A1KH")
end

function Trig_StartTotalProductionPlayer_Actions()
    G.TotalProductionP[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))] = true
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC("A1KI"), true)
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC("A1KH"), false)
end

function Trig_EndTotalProductionPlayer_Conditions()
    return GetSpellAbilityId() == FourCC("A1KI")
end

function Trig_EndTotalProductionPlayer_Actions()
    G.TotalProductionP[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))] = false
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC("A1KH"), true)
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC("A1KI"), false)
end

--===========================================================================
-- TotalProductionTrain / TotalProductionDeath
--===========================================================================
function Trig_TotalProductionTrain_Conditions()
    return G.TotalProduction
end

function Trig_TotalProductionTrain_Actions()
    local u = GetTrainedUnit()
    local uh = GetHandleId(u)
    SaveInteger(G.Hash, S2I(tostring(uh) .. "a"), 0, GetUnitTypeId(GetTriggerUnit()))
end

function ThisId()
    return GetUnitTypeId(GetFilterUnit()) == G.udg_LocalInteger5
end

function Trig_TotalProductionDeath_Conditions()
    return G.TotalProductionP[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end

function Trig_TotalProductionDeath_Actions()
    local u = GetTriggerUnit()
    local uh = GetHandleId(u)
    local id = LoadInteger(G.Hash, S2I(tostring(uh) .. "a"), 0)
    local p = GetOwningPlayer(u)
    local u2 = nil
    local g = CreateGroup()
    local b = Condition(ThisId)
    G.udg_LocalInteger5 = id

    FlushChildHashtable(G.Hash, S2I(tostring(uh) .. "a"))
    GroupEnumUnitsOfPlayer(g, p, b)
    u2 = GroupPickRandomUnit(g)
    if u2 ~= nil then
        IssueImmediateOrderById(u2, GetUnitTypeId(u))
    end

    DestroyGroup(g)
    DestroyBoolExpr(b)
end

--===========================================================================
-- DisIncomeStart Trigger
--===========================================================================
function Trig_DisIncomeStart_Func002A()
    TimerDialogDisplayForPlayerBJ(false, G.udg_TimerToDis, GetEnumPlayer())
end

function Trig_DisIncomeStart_Actions()
    ForForce(G.udg_AllPlayers, Trig_DisIncomeStart_Func002A)
    TimerDialogDisplayBJ(false, G.udg_TimerToDis)
    G.DisOn = true
end

--===========================================================================
-- Continental Bool Expressions
--===========================================================================
function InNord()
    return RectContainsUnit(G.gg_rct_Nord, GetFilterUnit()) ~= true and RectContainsUnit(G.gg_rct_Azgel, GetFilterUnit()) ~= true
end

function InVK()
    return (RectContainsUnit(G.gg_rct_EastenKingdoms, GetFilterUnit()) ~= true and RectContainsUnit(G.gg_rct_EasternDungeons, GetFilterUnit()) ~= true and RectContainsUnit(G.gg_rct_BlackMountain, GetFilterUnit()) ~= true) or RectContainsUnit(G.gg_rct_OutNoVk, GetFilterUnit())
end

function InBisles()
    return RectContainsUnit(G.gg_rct_BrokenIsles, GetFilterUnit()) ~= true
end

function InOutland()
    return RectContainsUnit(G.gg_rct_Outland, GetFilterUnit()) ~= true or RectContainsUnit(G.gg_rct_VknotOut, GetFilterUnit())
end

function InArgus()
    return RectContainsUnit(G.gg_rct_Argus, GetFilterUnit()) ~= true
end

function InPandaria()
    return RectContainsUnit(G.gg_rct_Pandaria, GetFilterUnit()) ~= true
end

function InAnkirag()
    return RectContainsUnit(G.gg_rct_Ankirag, GetFilterUnit()) ~= true
end

function InAzgel()
    return RectContainsUnit(G.gg_rct_Azgel, GetFilterUnit()) ~= true
end

function InBlackRock()
    return RectContainsUnit(G.gg_rct_BlackMountain, GetFilterUnit()) ~= true
end

function InOrgrimmar()
    return RectContainsUnit(G.gg_rct_Orgrimmar, GetFilterUnit()) ~= true
end

function InDeadMines()
    return RectContainsUnit(G.gg_rct_DeadMines, GetFilterUnit()) ~= true
end

function InStalgorn()
    return RectContainsUnit(G.gg_rct_Stalgorn, GetFilterUnit()) ~= true
end

function InUldum()
    return RectContainsUnit(G.gg_rct_Uldum, GetFilterUnit()) ~= true
end

function InMaradon()
    return RectContainsUnit(G.gg_rct_Maradon, GetFilterUnit()) ~= true
end

function InUndercity()
    return RectContainsUnit(G.gg_rct_Undercity, GetFilterUnit()) ~= true
end

function InDalaran()
    return RectContainsUnit(G.gg_rct_KillDalaran, GetFilterUnit()) ~= true
end

function InNaxramas()
    return RectContainsUnit(G.gg_rct_Naxramas, GetFilterUnit()) ~= true
end

function SetContinetsBooleprs()
    G.udg_B_InKalim = Condition(InKalim)
    G.udg_B_InNord = Condition(InNord)
    G.udg_B_InVK = Condition(InVK)
    G.udg_B_InOutland = Condition(InOutland)
    G.udg_B_InBIsles = Condition(InBisles)
    G.udg_B_InArgus = Condition(InArgus)
    G.udg_B_InPandaria = Condition(InPandaria)

    G.udg_B_Ankirag = Condition(InAnkirag)
    G.udg_B_Azgel = Condition(InAzgel)
    G.udg_B_BlackRock = Condition(InBlackRock)
    G.udg_B_Orgrimmar = Condition(InOrgrimmar)
    G.udg_B_DeadMines = Condition(InDeadMines)
    G.udg_B_Stalgorn = Condition(InStalgorn)
    G.udg_B_Uldum = Condition(InUldum)
    G.udg_B_Maradon = Condition(InMaradon)
    G.udg_B_Undercity = Condition(InUndercity)

    G.udg_B_Dalaran = Condition(InDalaran)
    G.udg_B_Naxramas = Condition(InNaxramas)
end

--===========================================================================
-- ContinentalTemplates
--===========================================================================
function RemoveOutsiders(g, fromThisArea)
    GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, fromThisArea)
    GroupRemoveGroup2(G.gSubGroup, g)
end

function AddOutsiders(g, fromAreaRect)
    GroupEnumUnitsInRect(G.gSubGroup, fromAreaRect, G.udg_B_EnemyUnit)
    GroupAddGroup2(G.gSubGroup, g)
end

function DestroyRocksAct()
    G.gDestructable = GetEnumDestructable()
    if GetDestructableTypeId(G.gDestructable) == FourCC("B01K") then
        SetDestructableLife(G.gDestructable, GetDestructableLife(G.gDestructable) - 350)
    end
end

function DestroyRocks(r)
    EnumDestructablesInRect(r, nil, DestroyRocksAct)
end

--===========================================================================
-- Dungeon Handlers
--===========================================================================
function HandleAzgel(x, y, g)
    if RectContainsCoords(G.gg_rct_Azgel, x, y) then
        RemoveOutsiders(g, G.udg_B_Azgel)
        AddOutsiders(g, G.gg_rct_Nord)
        if RectContainsCoords(G.gg_rct_AzNerRocks, x, y) then
            EnumDestructablesInRect(G.gg_rct_AzNerRocks, nil, DestroyRocksAct)
        end
        return true
    end
    return false
end

function HandleAnkirag(x, y, g)
    if RectContainsCoords(G.gg_rct_Ankirag, x, y) then
        RemoveOutsiders(g, G.udg_B_Ankirag)
        AddOutsiders(g, G.gg_rct_KalimSouth)
        return true
    end
    return false
end

function HandleBlackRock(x, y, g)
    if RectContainsCoords(G.gg_rct_BlackMountain, x, y) then
        RemoveOutsiders(g, G.udg_B_BlackRock)
        AddOutsiders(g, G.gg_rct_EKsouth)
        return true
    end
    return false
end

function HandleOrgrimmar(x, y, g)
    if RectContainsCoords(G.gg_rct_Orgrimmar, x, y) then
        RemoveOutsiders(g, G.udg_B_Orgrimmar)
        AddOutsiders(g, G.gg_rct_KalimCentral)
        return true
    end
    return false
end

function HandleDeadMines(x, y, g)
    if RectContainsCoords(G.gg_rct_DeadMines, x, y) then
        RemoveOutsiders(g, G.udg_B_DeadMines)
        AddOutsiders(g, G.gg_rct_EKsouth)
        return true
    end
    return false
end

function HandleStalgorn(x, y, g)
    if RectContainsCoords(G.gg_rct_Stalgorn2, x, y) and not RectContainsCoords(G.gg_rct_UldumNotStalgorn, x, y) then
        RemoveOutsiders(g, G.udg_B_Stalgorn)
        AddOutsiders(g, G.gg_rct_EKsouth)
        return true
    end
    return false
end

function HandleUldum(x, y, g)
    if RectContainsCoords(G.gg_rct_Uldum, x, y) then
        RemoveOutsiders(g, G.udg_B_Uldum)
        AddOutsiders(g, G.gg_rct_EKsouth)
        return true
    end
    return false
end

function HandleMaradon(x, y, g)
    if RectContainsCoords(G.gg_rct_Maradon, x, y) then
        RemoveOutsiders(g, G.udg_B_Maradon)
        AddOutsiders(g, G.gg_rct_KalimCentral)
        return true
    end
    return false
end

function HandleUndercity(x, y, g)
    if RectContainsCoords(G.gg_rct_Undercity, x, y) then
        RemoveOutsiders(g, G.udg_B_Undercity)
        AddOutsiders(g, G.gg_rct_EKWest)
        return true
    end
    return false
end

function HandleWestDungeons(x, y, g)
    if RectContainsCoords(G.gg_rct_NoWater1, x, y) then
        HandleAzgel(x, y, g)
        HandleAnkirag(x, y, g)
        HandleBlackRock(x, y, g)
        HandleOrgrimmar(x, y, g)
        HandleDeadMines(x, y, g)
        HandleStalgorn(x, y, g)
        HandleUldum(x, y, g)
    end
    return false
end

function HandleCentralDungeons(x, y, g)
    if RectContainsCoords(G.gg_rct_NoWater3, x, y) then
        HandleMaradon(x, y, g)
        HandleUndercity(x, y, g)
    end
    return false
end

--===========================================================================
-- Continental Main: Continent Removers
--===========================================================================
function RemKalim(x)
    GroupRemoveUnit(x, G.gg_unit_h0E2_0011)
    GroupRemoveUnit(x, G.gg_unit_h08O_0444)
    GroupRemoveUnit(x, G.gg_unit_h09B_0508)
    GroupRemoveUnit(x, G.gg_unit_h09C_0509)
    GroupRemoveUnit(x, G.gg_unit_h097_0502)
end

function RemKalim_P(x)
    GroupRemoveUnit(x, G.gg_unit_n003_0123)
    GroupRemoveUnit(x, G.gg_unit_n003_0124)
end

function RemKalim_P2(x)
    GroupRemoveUnit(x, G.gg_unit_n003_0118)
    GroupRemoveUnit(x, G.gg_unit_n003_0117)
end

function RemNord(x)
    GroupRemoveUnit(x, G.gg_unit_h09A_0506)
    GroupRemoveUnit(x, G.gg_unit_h09N_0346)
end

function RemPandaria(x)
    GroupRemoveUnit(x, G.gg_unit_h09V_0137)
    GroupRemoveUnit(x, G.gg_unit_h0BH_0601)
end

function RemVK(x)
    GroupRemoveUnit(x, G.gg_unit_h0BJ_0602)
    GroupRemoveUnit(x, G.gg_unit_h0BG_0600)
    GroupRemoveUnit(x, G.gg_unit_h0BF_0012)
    GroupRemoveUnit(x, G.gg_unit_h09P_0009)
end

function RemBisles(x)
    GroupRemoveUnit(x, G.gg_unit_h0BL_0603)
    GroupRemoveUnit(x, G.gg_unit_h0BM_0604)
    GroupRemoveUnit(x, G.gg_unit_h0OK_0337)
end

function RemWaterPortals(x)
    GroupRemoveUnit(x, G.gg_unit_n01D_0904)
    GroupRemoveUnit(x, G.gg_unit_n01D_0903)
end

function RemEmeraldPortals(x)
    GroupRemoveUnit(x, G.gg_unit_n01Y_0934)
    GroupRemoveUnit(x, G.gg_unit_n01Y_0896)
    GroupRemoveUnit(x, G.gg_unit_n01Y_0889)
    GroupRemoveUnit(x, G.gg_unit_n01Y_0897)
end

--===========================================================================
-- Continental Main: Continent Handlers
--===========================================================================
function HandleKalim(x, y, g)
    if RectContainsCoords(G.gg_rct_Kalim, x, y) and not RectContainsCoords(G.gg_rct_NordNotKalim, x, y) then
        GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, G.udg_B_InKalim)
        GroupRemoveGroup2(G.gSubGroup, g)
        RemKalim(g)
        RemKalim_P(g)
        return true
    end
    return false
end

function HandleNord(x, y, g)
    if RectContainsCoords(G.gg_rct_Nord, x, y) or RectContainsCoords(G.gg_rct_Azgel, x, y) or RectContainsCoords(G.gg_rct_NordNotKalim, x, y) then
        GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, G.udg_B_InNord)
        GroupRemoveGroup2(G.gSubGroup, g)
        RemNord(g)
        AddOutsiders(g, G.gg_rct_Azgel)
        return true
    end
    return false
end

function HandleVK(x, y, g)
    if (RectContainsCoords(G.gg_rct_EastenKingdoms, x, y) or RectContainsCoords(G.gg_rct_EasternDungeons, x, y) or RectContainsCoords(G.gg_rct_BlackMountain, x, y) or RectContainsCoords(G.gg_rct_VknotOut, x, y)) and not (RectContainsCoords(G.gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(G.gg_rct_OkeaniaNoVk, x, y) or RectContainsCoords(G.gg_rct_KillDalaran, x, y)) then
        GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, G.udg_B_InVK)
        GroupRemoveGroup2(G.gSubGroup, g)
        RemVK(g)
        return true
    end
    return false
end

function HandleOutland(x, y, g)
    if (RectContainsCoords(G.gg_rct_Outland, x, y) or RectContainsCoords(G.gg_rct_OutNoVk, x, y)) and not RectContainsCoords(G.gg_rct_VknotOut, x, y) then
        GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, G.udg_B_InOutland)
        GroupRemoveGroup2(G.gSubGroup, g)
        return true
    end
    return false
end

function HandleBrokenIsles(x, y, g)
    if RectContainsCoords(G.gg_rct_BrokenIsles, x, y) then
        GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, G.udg_B_InBIsles)
        GroupRemoveGroup2(G.gSubGroup, g)
        RemBisles(g)
        return true
    end
    return false
end

function HandleArgus(x, y, g)
    if RectContainsCoords(G.gg_rct_Argus, x, y) then
        GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, G.udg_B_InArgus)
        GroupRemoveGroup2(G.gSubGroup, g)
        return true
    end
    return false
end

function HandlePandaria(x, y, g)
    if RectContainsCoords(G.gg_rct_Pandaria, x, y) then
        GroupEnumUnitsInRect(G.gSubGroup, bj_mapInitialPlayableArea, G.udg_B_InPandaria)
        GroupRemoveGroup2(G.gSubGroup, g)
        RemPandaria(g)
        return true
    end
    return false
end

--===========================================================================
-- ProcessContinentalStuff / ProcessContinentalStuffNaga
--===========================================================================
function ProcessContinentalStuff(x, y, g)
    if HandleKalim(x, y, g) then
    elseif HandleVK(x, y, g) then
    elseif HandleNord(x, y, g) then
    elseif HandlePandaria(x, y, g) then
    elseif HandleOutland(x, y, g) then
    elseif HandleBrokenIsles(x, y, g) then
    elseif HandleArgus(x, y, g) then
    elseif HandleWestDungeons(x, y, g) then
    elseif HandleCentralDungeons(x, y, g) then
    end

    RemWaterPortals(g)
    RemEmeraldPortals(g)
end

function ProcessContinentalStuffNaga(x, y, g)
    if HandleOutland(x, y, g) then
    elseif HandleArgus(x, y, g) then
    elseif HandleAnkirag(x, y, g) then
    elseif HandleWestDungeons(x, y, g) then
    elseif HandleCentralDungeons(x, y, g) then
    end

    RemWaterPortals(g)
    RemEmeraldPortals(g)
end

--===========================================================================
-- TryPortalMovement
--===========================================================================
function TryPortalMovement(u, l__gEnemyGroup, l__gX, l__gY, i)
    local abilityLevel = GetUnitAbilityLevel(u, FourCC("A1GZ"))
    if i == 0 then
        i = 20
    end

    G.Counter = 0
    G.EnemyCapital = nil
    if abilityLevel == 1 then
        GroupEnumUnitsInRange(l__gEnemyGroup, l__gX, l__gY, 3000.00 * (math.pow(1.5, i)), G.udg_B_EnemyUnitP)
    elseif abilityLevel >= 2 then
        GroupEnumUnitsInRange(l__gEnemyGroup, l__gX, l__gY, 3000.00 * (math.pow(1.5, i)), G.udg_B_EnemyUnit)
        UnitRemoveAbility(u, FourCC("A1GZ"))
    else
        GroupEnumUnitsInRange(l__gEnemyGroup, l__gX, l__gY, 3000.00 * (math.pow(1.5, i)), G.udg_B_EnemyUnitP)
    end
end

--===========================================================================
-- AllowedPosition / KillIf / Continents (boundary enforcement)
--===========================================================================
function AllowedPosition(u)
    local x = GetUnitX(u)
    local y = GetUnitY(u)

    if G.udg_Continents[1] == 1 and (RectContainsCoords(G.gg_rct_EastenKingdoms, x, y) or RectContainsCoords(G.gg_rct_BlackMountain, x, y) or RectContainsCoords(G.gg_rct_EasternDungeons, x, y)) then
        return true
    end
    if G.udg_Continents[2] == 1 and (RectContainsCoords(G.gg_rct_Kalim, x, y) or RectContainsCoords(G.gg_rct_Ankirag, x, y) and RectContainsCoords(G.gg_rct_Maradon, x, y) and RectContainsCoords(G.gg_rct_Orgrimmar, x, y)) then
        return true
    end
    if G.udg_Continents[3] == 1 and RectContainsCoords(G.gg_rct_Outland, x, y) then
        return true
    end
    if G.udg_Continents[4] == 1 and (RectContainsCoords(G.gg_rct_Nord, x, y) or RectContainsCoords(G.gg_rct_Azgel, x, y)) then
        return true
    end
    if G.udg_Continents[5] == 1 and RectContainsCoords(G.gg_rct_Pandaria, x, y) then
        return true
    end
    if G.udg_Continents[6] == 1 and RectContainsCoords(G.gg_rct_Argus, x, y) then
        return true
    end
    if G.udg_Continents[7] == 1 and RectContainsCoords(G.gg_rct_BrokenIsles, x, y) then
        return true
    end
    if RectContainsCoords(G.gg_rct_EmeraldDream, x, y) then
        return true
    end
    return false
end

function KillIf()
    local t = GetExpiredTimer()
    local id = GetHandleId(t)
    local u = LoadUnitHandle(G.Hash, id, 0)
    local time = LoadInteger(G.Hash, id, 1)
    local e = LoadEffectHandle(G.Hash, id, 2)

    if time > 0 then
        if GetUnitAbilityLevel(u, FourCC("A0U6")) == 0 or AllowedPosition(u) then
            UnitRemoveAbility(u, FourCC("A0U6"))
            UnitRemoveAbility(u, FourCC("B05M"))
            DestroyEffect(e)
            DestroyTimer(t)
            FlushChildHashtable(G.Hash, id)
        else
            time = time - 2
            SaveInteger(G.Hash, id, 1, time)
        end
    else
        KillUnit(u)
        DestroyEffect(e)
        DestroyTimer(t)
        FlushChildHashtable(G.Hash, id)
    end
end

function Continents(u)
    local t = CreateTimer()
    local id = GetHandleId(t)
    local e = nil

    if AllowedPosition(u) then
        if GetUnitAbilityLevel(u, FourCC("A0U6")) > 0 then
            UnitRemoveAbility(u, FourCC("A0U6"))
            UnitRemoveAbility(u, FourCC("B05M"))
        end
    else
        if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
            ExplodeUnitBJ(u)
        elseif GetUnitTypeId(u) == FourCC("H049") then
            -- do nothing for race circles
        else
            if GetUnitAbilityLevel(u, FourCC("A0U6")) > 0 then
                SetUnitPosition(u, 0, 0)
                DisplayTextToPlayer(GetOwningPlayer(u), 0, 0, "\208\146\208\176\209\136 \208\186\209\128\209\131\208\179 \209\130\208\181\208\187\208\181\208\191\208\190\209\128\209\130\208\184\209\128\208\190\208\178\208\176\208\189 \208\178 \209\134\208\181\208\189\209\130 \208\186\208\176\209\128\209\130\209\139")
            else
                UnitAddAbility(u, FourCC("A0U6"))
                e = AddSpecialEffectTarget("Abilities\\Spells\\Other\\TalkToMe\\TalkToMe", u, "overhead")
                TimerStart(t, 2, true, KillIf)
                SaveUnitHandle(G.Hash, id, 0, u)
                SaveInteger(G.Hash, id, 1, 30)
                SaveEffectHandle(G.Hash, id, 2, e)
            end
        end
    end
end

--===========================================================================
-- Continents_Spell Trigger (reset all)
--===========================================================================
function Trig_Continents_Spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UI")
end

function Trig_Continents_Spell_Actions()
    local u = GetTriggerUnit()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_12041")
    G.udg_Continents[0] = 0
    for i = 1, 15 do
        G.udg_Continents[i] = 0
    end
    UnitAddAbilityBJ(FourCC("A0UB"), u)
    UnitRemoveAbilityBJ(FourCC("A0UM"), u)
    UnitAddAbilityBJ(FourCC("A0UC"), u)
    UnitRemoveAbilityBJ(FourCC("A0UN"), u)
    UnitRemoveAbilityBJ(FourCC("A0UO"), u)
    UnitAddAbilityBJ(FourCC("A0UD"), u)
    UnitAddAbilityBJ(FourCC("A0UE"), u)
    UnitRemoveAbilityBJ(FourCC("A0UP"), u)
    UnitAddAbilityBJ(FourCC("A0UF"), u)
    UnitRemoveAbilityBJ(FourCC("A0UQ"), u)
    UnitAddAbilityBJ(FourCC("A0UH"), u)
    UnitRemoveAbilityBJ(FourCC("A0UR"), u)
    UnitAddAbilityBJ(FourCC("A0UG"), u)
    UnitRemoveAbilityBJ(FourCC("A0US"), u)
end

--===========================================================================
-- Continents_set_On Trigger
--===========================================================================
function Trig_Continents_set_On_Conditions()
    return G.udg_Continents[0] == 1
end

function Trig_Continents_set_On_Func013001002()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_Continents_set_On_Func013A()
    WaygateActivateBJ(false, GetEnumUnit())
end

function Trig_Continents_set_On_Actions()
    local text2 = "\208\160\208\181\208\182\208\184\208\188 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130\208\190\208\178:|cffffff00 \208\178\208\186\208\187\209\142\209\135\208\181\208\189|r"
    DisplayTextToForce(GetPlayersAll(), text2)
    text2 = "|cff00ff00\208\152\209\130\208\190\208\179\208\190 \208\180\208\190\209\129\209\130\209\131\208\191\208\189\209\139 \208\180\208\187\209\143 \208\184\208\179\209\128\209\139: |r"
    if G.udg_Continents[1] == 1 then
        text2 = text2 .. "\208\146\208\190\209\129\209\130\208\190\209\135\208\189\209\139\208\181 \208\186\208\190\209\128\208\190\208\187\208\181\208\178\209\129\209\130\208\178\208\176\\"
    end
    if G.udg_Continents[2] == 1 then
        text2 = text2 .. "\208\154\208\176\208\187\208\184\208\188\208\180\208\190\209\128\\"
    end
    if G.udg_Continents[3] == 1 then
        text2 = text2 .. "\208\151\208\176\208\191\209\128\208\181\208\180\208\181\208\187\209\140\208\181\\"
    end
    if G.udg_Continents[4] == 1 then
        text2 = text2 .. "\208\157\208\190\209\128\208\180\209\129\208\186\208\190\208\187\\"
    end
    if G.udg_Continents[5] == 1 then
        text2 = text2 .. "\208\159\208\176\208\189\208\180\208\176\209\128\208\184\209\143\\"
    end
    if G.udg_Continents[6] == 1 then
        text2 = text2 .. "\208\144\209\128\208\179\209\131\209\129\\"
    end
    if G.udg_Continents[7] == 1 then
        text2 = text2 .. "\208\160\208\176\209\129\208\186\208\190\208\187\208\190\209\130\209\139\208\181 \208\190\209\129\209\130\209\128\208\190\208\178\208\176 \208\184 \208\158\208\186\208\181\208\176\208\189\208\184\209\143"
    end
    DisplayTextToForce(GetPlayersAll(), text2)
    EnableTrigger(G.gg_trg_LeaveNeadedRegions)
    ForGroupBJ(GetUnitsInRectMatching(GetPlayableMapRect(), Condition(Trig_Continents_set_On_Func013001002)), Trig_Continents_set_On_Func013A)
    StartTimerBJ(G.udg_TimerToCont, false, 0.50)
end

--===========================================================================
-- Continents_Off Trigger
--===========================================================================
function Trig_Continents_Off_Conditions()
    return G.udg_Continents[0] == 0
end

function Trig_Continents_Off_Func005001002()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_Continents_Off_Func005A()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_Continents_Off_Func006A()
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
    FogModifierStop(GetLastCreatedFogModifier())
    DestroyFogModifier(GetLastCreatedFogModifier())
end

function Trig_Continents_Off_Actions()
    DisplayTextToForce(GetPlayersAll(), "\208\160\208\181\208\182\208\184\208\188 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130\208\190\208\178:|cffffff00 \208\190\209\130\208\186\208\187\209\142\209\135\208\181\208\189, \208\184\208\179\209\128\208\176 \208\189\208\176 \208\178\209\129\208\181\208\185 \208\186\208\176\209\128\209\130\208\181|r")
    ForGroupBJ(GetUnitsInRectMatching(GetPlayableMapRect(), Condition(Trig_Continents_Off_Func005001002)), Trig_Continents_Off_Func005A)
    ForForce(G.udg_AllPlayers, Trig_Continents_Off_Func006A)
end

--===========================================================================
-- LeaveNeadedRegions Trigger
--===========================================================================
function Trig_LeaveNeadedRegions_Conditions()
    return G.udg_Continents[0] == 1
end

function Trig_LeaveNeadedRegions_Actions()
    Continents(GetTriggerUnit())
end

--===========================================================================
-- UseMassProssvet Trigger
--===========================================================================
function Trig_UseMassProssvet_Conditions()
    return GetItemTypeId(GetManipulatedItem()) == FourCC("I00C") and G.udg_Continents[0] == 1
end

function Trig_UseMassProssvet_Actions()
    TriggerSleepAction(7.00)
    FogModifierStop(GetLastCreatedFogModifier())
    DestroyFogModifier(GetLastCreatedFogModifier())
    TriggerExecute(G.gg_trg_SeeOnlyNeedeed)
end

--===========================================================================
-- SeeOnlyNeedeed Trigger
--===========================================================================
function Trig_SeeOnlyNeedeed_Actions()
    if G.udg_Continents[1] == 1 then
        for _ = 1, 3 do
            FogModifierStop(GetLastCreatedFogModifier())
            DestroyFogModifier(GetLastCreatedFogModifier())
        end
    end
    if G.udg_Continents[2] == 1 then
        for _ = 1, 2 do
            FogModifierStop(GetLastCreatedFogModifier())
            DestroyFogModifier(GetLastCreatedFogModifier())
        end
    end
    if G.udg_Continents[3] == 1 then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    end
    if G.udg_Continents[4] == 1 then
        for _ = 1, 2 do
            FogModifierStop(GetLastCreatedFogModifier())
            DestroyFogModifier(GetLastCreatedFogModifier())
        end
    end
    if G.udg_Continents[5] == 1 then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    end
    if G.udg_Continents[6] == 1 then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    end
    if G.udg_Continents[7] == 1 then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    end
end

--===========================================================================
-- NoBuild Trigger
--===========================================================================
function Trig_NoBuild_Conditions()
    return G.udg_Continents[0] == 1
end

function Trig_NoBuild_Actions()
    Continents(GetTriggerUnit())
end

--===========================================================================
-- EasternKingdoms On/Off (1)
--===========================================================================
function Trig_EasternOn_1_Conditions()
    return G.udg_Continents[1] == 1
end

function Trig_EasternOn_1_ActivateWaygate()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_EasternOn_1_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_EasternOn_1_Actions()
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_EastenKingdoms, Condition(Trig_EasternOn_1_WaygateFilter)), Trig_EasternOn_1_ActivateWaygate)
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_EasternDungeons, Condition(Trig_EasternOn_1_WaygateFilter)), Trig_EasternOn_1_ActivateWaygate)
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_BlackMountain, Condition(Trig_EasternOn_1_WaygateFilter)), Trig_EasternOn_1_ActivateWaygate)
end

function Trig_EasternOn_Spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UB")
end

function Trig_EasternOn_Spell_Actions()
    G.udg_Continents[1] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\146\208\190\209\129\209\130\208\190\209\135\208\189\209\139\208\181 \208\154\208\190\209\128\208\190\208\187\208\181\208\178\209\129\209\130\208\178\208\176|r")
    UnitAddAbilityBJ(FourCC("A0UM"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UB"), GetTriggerUnit())
end

function Trig_EasternOn_Spell_Off_Conditions()
    return GetSpellAbilityId() == FourCC("A0UM")
end

function Trig_EasternOn_Spell_Off_Actions()
    G.udg_Continents[1] = 0
    DisplayTextToForce(GetPlayersAll(), "\208\163\208\177\209\128\208\176\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\146\208\190\209\129\209\130\208\190\209\135\208\189\209\139\208\181 \208\154\208\190\209\128\208\190\208\187\208\181\208\178\209\129\209\130\208\178\208\176|r")
    UnitAddAbilityBJ(FourCC("A0UB"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UM"), GetTriggerUnit())
end

function Trig_EasternOn_Set_Actions()
    G.udg_Continents[1] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\146\208\190\209\129\209\130\208\190\209\135\208\189\209\139\208\181 \208\154\208\190\209\128\208\190\208\187\208\181\208\178\209\129\209\130\208\178\208\176|r")
end

--===========================================================================
-- Kalimdor On/Off (2)
--===========================================================================
function Trig_KalimOn_2_Conditions()
    return G.udg_Continents[2] == 1
end

function Trig_KalimOn_2_ActivateWaygate()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_KalimOn_2_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_KalimOn_2_Actions()
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Kalim, Condition(Trig_KalimOn_2_WaygateFilter)), Trig_KalimOn_2_ActivateWaygate)
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Ankirag, Condition(Trig_KalimOn_2_WaygateFilter)), Trig_KalimOn_2_ActivateWaygate)
end

function Trig_KalimOn_2_Spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UC")
end

function Trig_KalimOn_2_Spell_Actions()
    G.udg_Continents[2] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\154\208\176\208\187\208\184\208\188\208\180\208\190\209\128|r")
    UnitAddAbilityBJ(FourCC("A0UN"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UC"), GetTriggerUnit())
end

function Trig_KalimOn_2_Spell_off_Conditions()
    return GetSpellAbilityId() == FourCC("A0UN")
end

function Trig_KalimOn_2_Spell_off_Actions()
    G.udg_Continents[2] = 0
    DisplayTextToForce(GetPlayersAll(), "\208\163\208\177\209\128\208\176\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\154\208\176\208\187\208\184\208\188\208\180\208\190\209\128|r")
    UnitAddAbilityBJ(FourCC("A0UC"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UN"), GetTriggerUnit())
end

function Trig_KalimOn_2_set_Actions()
    G.udg_Continents[2] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\154\208\176\208\187\208\184\208\188\208\180\208\190\209\128|r")
end

--===========================================================================
-- Outland On/Off (3)
--===========================================================================
function Trig_Outland_3_Conditions()
    return G.udg_Continents[3] == 1
end

function Trig_Outland_3_ActivateWaygate()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_Outland_3_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_Outland_3_Actions()
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Outland, Condition(Trig_Outland_3_WaygateFilter)), Trig_Outland_3_ActivateWaygate)
end

function Trig_Outland_3_spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UD")
end

function Trig_Outland_3_spell_Actions()
    G.udg_Continents[3] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\151\208\176\208\191\209\128\208\181\208\180\208\181\208\187\209\140\208\181|r")
    UnitAddAbilityBJ(FourCC("A0UO"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UD"), GetTriggerUnit())
end

function Trig_Outland_3_spell_off_Conditions()
    return GetSpellAbilityId() == FourCC("A0UO")
end

function Trig_Outland_3_spell_off_Actions()
    G.udg_Continents[3] = 0
    DisplayTextToForce(GetPlayersAll(), "\208\163\208\177\209\128\208\176\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\151\208\176\208\191\209\128\208\181\208\180\208\181\208\187\209\140\208\181|r")
    UnitRemoveAbilityBJ(FourCC("A0UO"), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC("A0UD"), GetTriggerUnit())
end

function Trig_Outland_3_set_Actions()
    G.udg_Continents[3] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\151\208\176\208\191\209\128\208\181\208\180\208\181\208\187\209\140\208\181|r")
end

--===========================================================================
-- Northrend On/Off (4)
--===========================================================================
function Trig_NordOn_4_Conditions()
    return G.udg_Continents[4] == 1
end

function Trig_NordOn_4_ActivateWaygate()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_NordOn_4_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_NordOn_4_Actions()
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Nord, Condition(Trig_NordOn_4_WaygateFilter)), Trig_NordOn_4_ActivateWaygate)
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Azgel, Condition(Trig_NordOn_4_WaygateFilter)), Trig_NordOn_4_ActivateWaygate)
end

function Trig_NordOn_4_spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UE")
end

function Trig_NordOn_4_spell_Actions()
    G.udg_Continents[4] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\157\208\190\209\128\208\180\209\129\208\186\208\190\208\187|r")
    UnitRemoveAbilityBJ(FourCC("A0UE"), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC("A0UP"), GetTriggerUnit())
end

function Trig_NordOn_4_spell_off_Conditions()
    return GetSpellAbilityId() == FourCC("A0UP")
end

function Trig_NordOn_4_spell_off_Actions()
    G.udg_Continents[4] = 0
    DisplayTextToForce(GetPlayersAll(), "\208\163\208\177\209\128\208\176\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\157\208\190\209\128\208\180\209\129\208\186\208\190\208\187|r")
    UnitAddAbilityBJ(FourCC("A0UE"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UP"), GetTriggerUnit())
end

function Trig_NordOn_4_set_Actions()
    G.udg_Continents[4] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\157\208\190\209\128\208\180\209\129\208\186\208\190\208\187|r")
end

--===========================================================================
-- Pandaria On/Off (5)
--===========================================================================
function Trig_Pandaria_5_Conditions()
    return G.udg_Continents[5] == 1
end

function Trig_Pandaria_5_ActivateWaygate()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_Pandaria_5_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_Pandaria_5_Actions()
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Pandaria, Condition(Trig_Pandaria_5_WaygateFilter)), Trig_Pandaria_5_ActivateWaygate)
end

function Trig_Pandaria_5_spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UF")
end

function Trig_Pandaria_5_spell_Actions()
    G.udg_Continents[5] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\159\208\176\208\189\208\180\208\176\209\128\208\184\209\143|r")
    UnitAddAbilityBJ(FourCC("A0UQ"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UF"), GetTriggerUnit())
end

function Trig_Pandaria_5_spell_off_Conditions()
    return GetSpellAbilityId() == FourCC("A0UQ")
end

function Trig_Pandaria_5_spell_off_Actions()
    G.udg_Continents[5] = 0
    DisplayTextToForce(GetPlayersAll(), "\208\163\208\177\209\128\208\176\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\159\208\176\208\189\208\180\208\176\209\128\208\184\209\143|r")
    UnitAddAbilityBJ(FourCC("A0UF"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UQ"), GetTriggerUnit())
end

function Trig_Pandaria_5_set_Actions()
    G.udg_Continents[5] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\159\208\176\208\189\208\180\208\176\209\128\208\184\209\143|r")
end

--===========================================================================
-- Argus On/Off (6)
--===========================================================================
function Trig_Argus_6_Conditions()
    return G.udg_Continents[6] == 1
end

function Trig_Argus_6_ActivateWaygate()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_Argus_6_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_Argus_6_Actions()
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Argus, Condition(Trig_Argus_6_WaygateFilter)), Trig_Argus_6_ActivateWaygate)
end

function Trig_Argus_6_spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UH")
end

function Trig_Argus_6_spell_Actions()
    G.udg_Continents[6] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\144\209\128\208\179\209\131\209\129|r")
    UnitAddAbilityBJ(FourCC("A0UR"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UH"), GetTriggerUnit())
end

function Trig_Argus_6_spell_off_Conditions()
    return GetSpellAbilityId() == FourCC("A0UR")
end

function Trig_Argus_6_spell_off_Actions()
    G.udg_Continents[6] = 0
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\144\209\128\208\179\209\131\209\129|r")
    UnitAddAbilityBJ(FourCC("A0UH"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UR"), GetTriggerUnit())
end

function Trig_Argus_6_set_Actions()
    G.udg_Continents[6] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\144\209\128\208\179\209\131\209\129|r")
end

--===========================================================================
-- BrokenIsles On/Off (7)
--===========================================================================
function Trig_BrokenIsled_7_Conditions()
    return G.udg_Continents[7] == 1
end

function Trig_BrokenIsled_7_ActivateWaygate()
    WaygateActivateBJ(true, GetEnumUnit())
end

function Trig_BrokenIsled_7_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_BrokenIsled_7_Actions()
    ForGroupBJ(GetUnitsInRectMatching(G.gg_rct_Broken_Island, Condition(Trig_BrokenIsled_7_WaygateFilter)), Trig_BrokenIsled_7_ActivateWaygate)
end

function Trig_BrokenIsled_7_spell_Conditions()
    return GetSpellAbilityId() == FourCC("A0UG")
end

function Trig_BrokenIsled_7_spell_Actions()
    G.udg_Continents[7] = 1
    G.udg_Continents[0] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\160\208\176\209\129\208\186\208\190\208\187\208\190\209\130\209\139\208\181 \208\158\209\129\209\130\209\128\208\190\208\178\208\176|r")
    UnitAddAbilityBJ(FourCC("A0US"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0UG"), GetTriggerUnit())
end

function Trig_BrokenIsled_7_spell_off_Conditions()
    return GetSpellAbilityId() == FourCC("A0US")
end

function Trig_BrokenIsled_7_spell_off_Actions()
    G.udg_Continents[7] = 0
    DisplayTextToForce(GetPlayersAll(), "\208\163\208\177\209\128\208\176\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\160\208\176\209\129\208\186\208\190\208\187\208\190\209\130\209\139\208\181 \208\158\209\129\209\130\209\128\208\190\208\178\208\176|r")
    UnitAddAbilityBJ(FourCC("A0UG"), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC("A0US"), GetTriggerUnit())
end

function Trig_BrokenIsled_7_set_Actions()
    G.udg_Continents[7] = 1
    DisplayTextToForce(GetPlayersAll(), "\208\148\208\190\208\177\208\176\208\178\208\187\208\181\208\189 \208\186\208\190\208\189\209\130\208\184\208\189\208\181\208\189\209\130: |cffffff00\208\160\208\176\209\129\208\186\208\190\208\187\208\190\209\130\209\139\208\181 \208\158\209\129\209\130\209\128\208\190\208\178\208\176|r")
end

--===========================================================================
-- Only_Eastern Trigger
--===========================================================================
function Trig_Only_Eastern_WaygateFilter()
    return GetUnitAbilityLevelSwapped(FourCC("Awrp"), GetFilterUnit()) >= 1
end

function Trig_Only_Eastern_Func004A()
    WaygateActivateBJ(false, GetEnumUnit())
end

function Trig_Only_Eastern_Actions()
    DisplayTextToForce(G.udg_AllPlayers, "TRIGSTR_19899")
    EnableTrigger(G.gg_trg_Leave_Easten)
    EnableTrigger(G.gg_trg_Back_Easten)
    ForGroupBJ(GetUnitsInRectMatching(GetPlayableMapRect(), Condition(Trig_Only_Eastern_WaygateFilter)), Trig_Only_Eastern_Func004A)
end

--===========================================================================
-- Leave_Easten / Back_Easten
--===========================================================================
function Trig_Leave_Easten_Actions()
    G.udg_LocalUnit2 = GetTriggerUnit()
    UnitAddAbilityBJ(FourCC("A0U6"), GetTriggerUnit())
end

function Trig_Back_Easten_Actions()
    UnitRemoveAbilityBJ(FourCC("A0U6"), GetTriggerUnit())
end

--===========================================================================
-- ArchontMode / ArchontModeOff
--===========================================================================
function Trig_ArchontMode_Actions()
    local s = SubStringBJ(GetEventPlayerChatString(), 8, 10)
    local pi2 = S2I(s) - 1
    local pi1 = GetPlayerId(GetTriggerPlayer())
    if CorrectNumber(pi2) then
        DisplayTextToPlayer(Player(pi1), 0, 0, "\208\146\209\139 \208\191\208\190\208\191\209\139\209\130\208\176\208\187\208\184\209\129\209\140 \208\180\208\176\209\130\209\140 \208\191\208\190\208\187\208\189\209\139\208\185 \208\186\208\190\208\189\209\130\208\190\208\187\209\140 \208\184\208\179\209\128\208\190\208\186\209\131 " .. GetPlayerName(Player(pi2)) .. " \208\189\208\190\208\188\208\181\209\128 " .. I2S(pi2))
        DisplayTextToPlayer(Player(pi2), 0, 0, "\208\146\208\176\208\188 \208\191\208\190\208\191\209\139\209\130\208\176\208\187\209\129\209\143 \208\180\208\176\209\130\209\140 \208\191\208\190\208\187\208\189\209\139\208\185 \208\186\208\190\208\189\209\130\208\190\208\187\209\140 \208\184\208\179\209\128\208\190\208\186 " .. GetPlayerName(Player(pi1)))
        SetPlayerAllianceStateBJ(Player(pi1), Player(pi2), bj_ALLIANCE_ALLIED_ADVUNITS)
    end
    MultiboardAllowDisplayBJ(true)
end

function Trig_ArchontModeOff_Actions()
    local s = SubStringBJ(GetEventPlayerChatString(), 8, 10)
    local pi2 = S2I(s) - 1
    local pi1 = GetPlayerId(GetTriggerPlayer())
    if CorrectNumber(pi2) and G.DipMode ~= 1 then
        DisplayTextToPlayer(Player(pi1), 0, 0, "\208\146\209\139 \208\191\208\190\208\191\209\139\209\130\208\176\208\187\208\184\209\129\209\140 \208\190\209\130\208\186\208\187\209\142\209\135\208\184\209\130\209\140 \208\191\208\190\208\187\208\189\209\139\208\185 \208\186\208\190\208\189\209\130\208\190\208\187\209\140 \208\184\208\179\209\128\208\190\208\186\209\131 " .. GetPlayerName(Player(pi2)) .. " \208\189\208\190\208\188\208\181\209\128 " .. I2S(pi2))
        DisplayTextToPlayer(Player(pi1), 0, 0, "\208\146\208\176\208\188 \208\191\208\190\208\191\209\139\209\130\208\176\208\187\209\129\209\143 \208\190\209\130\208\186\208\187\209\142\209\135\208\184\209\130\209\140 \208\191\208\190\208\187\208\189\209\139\208\185 \208\186\208\190\208\189\209\130\208\190\208\187\209\140 \208\184\208\179\209\128\208\190\208\186 " .. GetPlayerName(Player(pi1)))
        SetPlayerAllianceBJ(Player(pi1), ALLIANCE_SHARED_ADVANCED_CONTROL, false, Player(pi2))
    end
end

--===========================================================================
-- Chat Commands: Kill
--===========================================================================
function Trig_Kill_Func002A()
    local id = GetUnitTypeId(GetEnumUnit())
    if not IsUnitInGroup(GetEnumUnit(), G.udg_ZahvatBuildings) and GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() and not IsUnitInGroup(GetEnumUnit(), G.udg_StolicaGroups) and id ~= FourCC("e00C") and id ~= FourCC("e00D") then
        KillUnit(GetEnumUnit())
    else
        if IsUnitInGroup(GetEnumUnit(), G.udg_StolicaGroups) and GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() then
            if G.udg_GameMode == 2 then
                SetUnitLifePercentBJ(GetEnumUnit(), 15.00)
            else
                KillUnit(GetEnumUnit())
                G.udg_LocalPlayer = GetTriggerPlayer()
                ConditionalTriggerExecute(G.gg_trg_StolicaKill)
            end
        end
    end
end

function Trig_Kill_Actions()
    local p = GetTriggerPlayer()
    local g = CreateGroup()
    GroupEnumUnitsSelected(g, p, nil)
    ForGroup(g, Trig_Kill_Func002A)
    DestroyGroup(g)
end

--===========================================================================
-- Chat Commands: Rep
--===========================================================================
function RepConditions()
    if GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() and not IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE) then
        ReplaceUnit2(GetEnumUnit(), GetUnitTypeId(GetEnumUnit()), bj_UNIT_STATE_METHOD_RELATIVE)
    end
end

function Trig_Rep_Actions()
    local p = GetTriggerPlayer()
    local g = CreateGroup()
    GroupEnumUnitsSelected(g, p, nil)
    ForGroup(g, RepConditions)
    DestroyGroup(g)
end

--===========================================================================
-- Chat Commands: RepEc
--===========================================================================
function Trig_RepEc_Actions()
    local pi = GetPlayerId(GetTriggerPlayer())
    FixEc(pi)
end

--===========================================================================
-- Chat Commands: F2_Start
--===========================================================================
function Trig_F2_Start_Conditions()
    return CountLivingPlayerUnitsOfTypeId(FourCC("h0GR"), GetTriggerPlayer()) == 0
end

function Trig_F2_Start_Actions()
    G.udg_LocalPosition2 = GetRectCenter(G.gg_rct_HostRegion)
    ClearSelectionForPlayer(GetTriggerPlayer())
    CreateNUnitsAtLoc(1, FourCC("h0GR"), GetTriggerPlayer(), G.udg_LocalPosition2, bj_UNIT_FACING)
    SelectUnitAddForPlayer(GetLastCreatedUnit(), GetTriggerPlayer())
end

--===========================================================================
-- Chat Commands: Camera
--===========================================================================
function Trig_Camera_command_O_Actions()
    G.udg_wawt = S2R(SubStringBJ(GetEventPlayerChatString(), 6, 9))
    SetCameraFieldForPlayer(GetTriggerPlayer(), CAMERA_FIELD_TARGET_DISTANCE, G.udg_wawt, 1.00)
end

--===========================================================================
-- Chat Commands: FastTest / FastTestOff
--===========================================================================
function Trig_FastTest_Actions()
    if G.udg_GameMode == 4 then
        G.fastTest[GetPlayerId(GetTriggerPlayer())] = true
        G.income[GetPlayerId(GetTriggerPlayer())] = G.income[GetPlayerId(GetTriggerPlayer())] + 25000
        G.incomeW[GetPlayerId(GetTriggerPlayer())] = G.incomeW[GetPlayerId(GetTriggerPlayer())] + 25000
        DisplayTimedTextToForce(G.udg_AllPlayers, 6, GetPlayerName(GetTriggerPlayer()) .. " - \208\178\208\186\208\187\209\142\209\135\208\184\209\130 \209\130\208\181\209\129\209\130\208\190\208\178\209\139\208\185 \209\128\208\181\208\182\208\184\208\188!!!")
        SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_FOOD_CAP, 100)
    end
end

function Trig_FastTestOff_Actions()
    if G.udg_GameMode == 4 then
        G.fastTest[GetPlayerId(GetTriggerPlayer())] = false
        G.income[GetPlayerId(GetTriggerPlayer())] = G.income[GetPlayerId(GetTriggerPlayer())] - 25000
        G.incomeW[GetPlayerId(GetTriggerPlayer())] = G.incomeW[GetPlayerId(GetTriggerPlayer())] - 25000
        DisplayTimedTextToForce(G.udg_AllPlayers, 6, GetPlayerName(GetTriggerPlayer()) .. " - \208\178\209\139\208\186\208\187\209\142\209\135\208\184\208\187 \209\130\208\181\209\129\209\130\208\190\208\178\209\139\208\185 \209\128\208\181\208\182\208\184\208\188!")
    end
end

--===========================================================================
-- Chat Commands: DomCheckCommand
--===========================================================================
function Trig_DomCheckCommand_Actions()
    local s = SubStringBJ(GetEventPlayerChatString(), 7, 8)
    local pi = S2I(s) - 1
    if CorrectNumber(pi) then
        local g = CreateGroup()
        GroupEnumUnitsOfPlayer(g, Player(pi), nil)
        local title = GetPlayerName(Player(pi)) .. "   \208\181\208\180\208\184\208\189\208\184\209\134: " .. BlzGroupGetSize(g) .. "   \208\168\208\176\208\189\209\129 \209\131\208\188\208\181\209\128\209\130\209\140 \208\180\208\190\208\188\208\184\208\189\208\184\209\128\208\190\208\178\208\176\209\130\209\140: "
        local rate = (BlzGroupGetSize(g) + 1) / (G.DomLimit[pi] + 1)
        title = title .. R2SW(rate * 100, 1, 1) .. "%"
        DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, title)
        DestroyGroup(g)
    end
end

--===========================================================================
-- FastBuild / FastResearch / FastTrain
--===========================================================================
function Trig_FastBuild_Conditions()
    return G.fastTest[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end

function Trig_FastBuild_Actions()
    UnitSetConstructionProgress(GetTriggerUnit(), 100)
end

function Trig_FastResearch_Conditions()
    return G.fastTest[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end

function Trig_FastResearch_Actions()
    SetPlayerTechResearchedSwap(GetResearched(), GetPlayerTechCount(GetOwningPlayer(GetTriggerUnit()), GetResearched(), true) + 1, GetOwningPlayer(GetTriggerUnit()))
    IssueImmediateOrderById(GetTriggerUnit(), 851976)
end

function Trig_FastTrain_Conditions()
    return G.fastTest[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end

function Trig_FastTrain_Actions()
    CreateUnit(GetOwningPlayer(GetTriggerUnit()), GetTrainedUnitType(), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), 0.00)
    IssueImmediateOrderById(GetTriggerUnit(), 851976)
end

--===========================================================================
-- StartInc
--===========================================================================
function StartInc()
    for i = 0, 23 do
        G.income[i] = 0
        G.incomeW[i] = 0
        G.disincome[i] = 0
        G.logistic[i] = 0
        G.corruption[i] = 0
        G.balance[i] = 0
        G.additional[i] = 0
        G.AllyTax[i] = 0
    end
    RegionAddRect(G.Allmap, GetWorldBounds())
end

--===========================================================================
-- Initialize scope functions (called on map init)
--===========================================================================
function init___Init()
    UISetup()
end

function init2___Init()
    Face2()
end

function initContinentalBoolExprs___Init()
    SetContinetsBooleprs()
end
