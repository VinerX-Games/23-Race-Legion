    gg_trg_DisIncomeStart=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_DisIncomeStart, udg_IncomeTimerFirst)
    TriggerAddAction(gg_trg_DisIncomeStart, Trig_DisIncomeStart_Actions)
end
--===========================================================================
-- Trigger: Globals
--===========================================================================
--===========================================================================
function InitTrig_Globals()
    --set gg_trg_Globals = CreateTrigger(  )
end
--===========================================================================
-- ===========================================================================
--  Color Commands (consolidated from 24 individual triggers)
-- ===========================================================================
---@return nothing
function InitColorCommands()
	local COLOR_MAP = {
		[" - colorred"] = PLAYER_COLOR_RED,
		[" - colorblue"] = PLAYER_COLOR_BLUE,
		[" - colorpurple"] = PLAYER_COLOR_PURPLE,
		[" - colorteal"] = PLAYER_COLOR_CYAN,
		[" - coloryellow"] = PLAYER_COLOR_YELLOW,
		[" - colororange"] = PLAYER_COLOR_ORANGE,
		[" - colorgreen"] = PLAYER_COLOR_GREEN,
		[" - colorpink"] = PLAYER_COLOR_PINK,
		[" - colorgray"] = PLAYER_COLOR_LIGHT_GRAY,
		[" - colorlight - blue"] = PLAYER_COLOR_LIGHT_BLUE,
		[" - colordark - green"] = PLAYER_COLOR_AQUA,
		[" - colorbrown"] = PLAYER_COLOR_BROWN,
		[" - colormaroon"] = PLAYER_COLOR_MAROON,
		[" - colornavy"] = PLAYER_COLOR_NAVY,
		[" - colorturquoise"] = PLAYER_COLOR_TURQUOISE,
		[" - colorviolet"] = PLAYER_COLOR_VIOLET,
		[" - colorwheat"] = PLAYER_COLOR_WHEAT,
		[" - colorpeach"] = PLAYER_COLOR_PEACH,
		[" - colormint"] = PLAYER_COLOR_MINT,
		[" - colorlavender"] = PLAYER_COLOR_LAVENDER,
		[" - colorcoal"] = PLAYER_COLOR_COAL,
		[" - colorsnow"] = PLAYER_COLOR_SNOW,
		[" - coloremerald"] = PLAYER_COLOR_EMERALD,
		[" - colorpeanut"] = PLAYER_COLOR_PEANUT,
	}

	local t = CreateTrigger()
	for i = 0, 23 do
		for cmd, _ in pairs(COLOR_MAP) do
			TriggerRegisterPlayerChatEvent(t, Player(i), cmd, true)
		end
	end
	TriggerAddAction(t, function()
		local color = COLOR_MAP[GetEventPlayerChatString()]
		if color then
			SetPlayerColorBJ(GetTriggerPlayer(), color, true)
		end
	end)
end
-- Trigger: StartTableCode
--===========================================================================
function ActivePlayers()
    return GetPlayerSlotState(GetFilterPlayer()) == PLAYER_SLOT_STATE_PLAYING and not IsPlayerInForce(GetFilterPlayer(), udg_Bots)
end
function GetPlayerNameCut(p)
    local s= GetPlayerName(p)
    local s2
    local s3= ""
    local i= 0
    while true do
        s2=SubString(s, i, i + 1)
        if s2 == "" or i > 18 or s2 == nil then break end
        
        
        s3=s3 .. s2
        i=i + 1
    end
    return s3
end
---@param pi integer
---@return integer|nil
function EnsureMultiboardPlayerRow(pi)
    local ownerIndex=MultiboardItemOwnerIndex[pi]
    if ownerIndex ~= nil then
        return ownerIndex
    end
    if Multiboard == nil then
        return nil
    end

    max=max + 1
    udg_PlayersCount=udg_PlayersCount + 1
    ownerIndex=max
    MultiboardItemOwnerIndex[pi]=ownerIndex

    MultiboardSetRowCount(Multiboard, udg_PlayersCount + 1)
    MultiboardItem[ownerIndex * 2]=MultiboardGetItem(Multiboard, ownerIndex, 0)
    MultiboardItem[ownerIndex * 2 + 1]=MultiboardGetItem(Multiboard, ownerIndex, 1)
    udg_LocalText2=I2S(GetConvertedPlayerId(Player(pi))) .. "." .. GetPlayerNameCut(Player(pi))
    MultiboardSetItemValue(MultiboardItem[ownerIndex * 2], udg_LocalText2)
    MultiboardSetItemWidth(MultiboardItem[ownerIndex * 2], 0.14)
    MultiboardSetItemValue(MultiboardItem[ownerIndex * 2 + 1], I2S(udg_UnitsCount[pi] or 0))
    MultiboardSetItemWidth(MultiboardItem[ownerIndex * 2 + 1], 0.06)

    if ThirdColumn[24] ~= nil then
        ThirdColumn[pi]=MultiboardGetItem(Multiboard, ownerIndex, 2)
        MultiboardSetItemValue(ThirdColumn[pi], "0.000%")
        MultiboardSetItemWidth(ThirdColumn[pi], 0.06)
    end
    if ArmyPowerColumn[24] ~= nil then
        ArmyPowerColumn[pi]=MultiboardGetItem(Multiboard, ownerIndex, 3)
        MultiboardSetItemValue(ArmyPowerColumn[pi], R2SW_Polyfill(ArmyExp[pi] or 0.001))
        MultiboardSetItemWidth(ArmyPowerColumn[pi], 0.06)
    end

    return ownerIndex
end
function Trig_StartTableCode_Actions()
    local i= 0
    udg_PlayersCount=CountPlayersInForceBJ(GetPlayersMatching(Condition(ActivePlayers)))
    udg_PlayersCount=udg_PlayersCount + CountPlayersInForceBJ(udg_Bots)
    
    Multiboard=CreateMultiboard()
    MultiboardSetRowCount(Multiboard, udg_PlayersCount + 1)
    MultiboardSetColumnCount(Multiboard, 2)
    MultiboardSetTitleText(Multiboard, "")
    MultiboardItem[0]=MultiboardGetItem(Multiboard, 0, 0)
    MultiboardItem[1]=MultiboardGetItem(Multiboard, 0, 1)
    MultiboardSetItemValue(MultiboardItem[0], "")
    MultiboardSetItemValue(MultiboardItem[1], "")
    MultiboardSetItemWidth(MultiboardItem[0], 0.12)
    MultiboardSetItemWidth(MultiboardItem[1], 0.06)
    MultiboardReleaseItem(MultiboardItem[0])
    MultiboardReleaseItem(MultiboardItem[1])
    while true do
        if GetPlayerSlotState(Player(i)) == PLAYER_SLOT_STATE_PLAYING or IsPlayerInForce(Player(i), udg_Bots) or udg_AiControl[i] then
            max=max + 1
            MultiboardItemOwnerIndex[i]=max
            MultiboardItem[max * 2]=MultiboardGetItem(Multiboard, max, 0)
            MultiboardItem[max * 2 + 1]=MultiboardGetItem(Multiboard, max, 1)
            udg_LocalText2=I2S(GetConvertedPlayerId(Player(i))) .. "." .. GetPlayerNameCut(Player(i))
                        
            --set udg_LocalText2 = SubString(udg_LocalText2, 0, StringLength(udg_LocalText2)-4 )
            MultiboardSetItemValue(MultiboardItem[max * 2], udg_LocalText2)
            MultiboardSetItemWidth(MultiboardItem[max * 2], 0.14)
            MultiboardSetItemValue(MultiboardItem[max * 2 + 1], "0")
            MultiboardSetItemWidth(MultiboardItem[max * 2 + 1], 0.06)
        end
        i=i + 1
        if i > 23 then break end
    end
    MultiboardSetItemsStyle(Multiboard, true, false)
    MultiboardDisplay(Multiboard, true)
    ExpandTable()
    ExpandTableArmyExpr()
    
end
--===========================================================================
function InitTrig_StartTableCode()
    gg_trg_StartTableCode=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_StartTableCode, udg_LobbyTime)
    TriggerAddAction(gg_trg_StartTableCode, Trig_StartTableCode_Actions)
end
--===========================================================================
-- Trigger: Untitled Trigger 015
--===========================================================================
function Trig_Untitled_Trigger_015_Actions()
    Trig_StartTableCode_Actions()
end
--===========================================================================
function InitTrig_Untitled_Trigger_015()
    gg_trg_Untitled_Trigger_015=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Untitled_Trigger_015, Player(0), "t", true)
    TriggerAddAction(gg_trg_Untitled_Trigger_015, Trig_Untitled_Trigger_015_Actions)
end
--===========================================================================
-- Trigger: UnitsToBuildingSituation2
--===========================================================================
function Trig_UnitsToBuildingSituation2_Func002C()
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e021') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e020') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e01H') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e01J') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e01L') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e01M') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e01X') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetTriggerUnit()) == FourCC('e01K') ) ) then
        return true
    end
    return false
end
function Trig_UnitsToBuildingSituation2_Conditions()
    if ( not ( IsUnitType(GetTriggerUnit(), UNIT_TYPE_STRUCTURE) == true ) ) then
        return false
    end
    if ( not Trig_UnitsToBuildingSituation2_Func002C() ) then
        return false
    end
    return true
end
function Trig_UnitsToBuildingSituation2_Actions()
    local i= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    udg_UnitsCount[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]=( udg_UnitsCount[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))] - 1 )
    MultiboardSetItemValue(MultiboardItem[MultiboardItemOwnerIndex[i] * 2 + 1], I2S(udg_UnitsCount[i]))
    i=0
end
--===========================================================================
function InitTrig_UnitsToBuildingSituation2()
    gg_trg_UnitsToBuildingSituation2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UnitsToBuildingSituation2, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_UnitsToBuildingSituation2, Condition(Trig_UnitsToBuildingSituation2_Conditions))
    TriggerAddAction(gg_trg_UnitsToBuildingSituation2, Trig_UnitsToBuildingSituation2_Actions)
end
--===========================================================================
-- Trigger: CanselSituation2
--===========================================================================
function Trig_CanselSituation2_Func001C()
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e021') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e020') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e01H') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e01J') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e01L') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e01M') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e01X') ) ) then
        return true
    end
    if ( ( GetUnitTypeId(GetCancelledStructure()) == FourCC('e01K') ) ) then
        return true
    end
    return false
end
function Trig_CanselSituation2_Conditions()
    if ( not Trig_CanselSituation2_Func001C() ) then
        return false
    end
    return true
end
function Trig_CanselSituation2_Actions()
    local i= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    udg_UnitsCount[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]=( udg_UnitsCount[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))] + 1 )
    MultiboardSetItemValue(MultiboardItem[MultiboardItemOwnerIndex[i] * 2 + 1], I2S(udg_UnitsCount[i]))
    i=0
end
--===========================================================================
function InitTrig_CanselSituation2()
    gg_trg_CanselSituation2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanselSituation2, EVENT_PLAYER_UNIT_CONSTRUCT_CANCEL)
    TriggerAddCondition(gg_trg_CanselSituation2, Condition(Trig_CanselSituation2_Conditions))
    TriggerAddAction(gg_trg_CanselSituation2, Trig_CanselSituation2_Actions)
end
--===========================================================================
-- Trigger: CircleMove Code
--===========================================================================
function Trig_CircleMove_Code_Conditions()
    return BlzGetTriggerPlayerMouseButton() == MOUSE_BUTTON_TYPE_RIGHT
end
function Trig_CircleMove_Code_Actions()
    local g= CreateGroup()
    local u
    udg_LocCircle=BlzGetTriggerPlayerMousePosition()
    if not ( IsTerrainPathableBJ(udg_LocCircle, PATHING_TYPE_WALKABILITY) or RectContainsLoc(gg_rct_HostRegion, udg_LocCircle) or RectContainsLoc(gg_rct_TestRegion, udg_LocCircle) or RectContainsLoc(gg_rct_EmeraldDream, udg_LocCircle) ) then
    
    
        if not ( RectContainsLoc(gg_rct_KillDalaran, udg_LocCircle) and not UnitAlive(gg_unit_e00C_0590) or RectContainsLoc(gg_rct_TurtleIsland, udg_LocCircle) and not UnitAlive(gg_unit_e00E_0085) or RectContainsLoc(gg_rct_Naxramas, udg_LocCircle) and not UnitAlive(gg_unit_e00D_0080) ) then
            bj_groupEnumTypeId=FourCC('h0HJ')
            GroupEnumUnitsOfPlayer(g, GetTriggerPlayer(), filterGetUnitsOfPlayerAndTypeId)
            while true do
                u=FirstOfGroup(g)
                if u == nil then break end
                SetUnitPositionLoc(u, udg_LocCircle)
                GroupRemoveUnit(g, u)
            end
        end
    
    end
    RemoveLocation(udg_LocCircle)
    GroupClear(g)
    DestroyGroup(g)
    u=nil
    g=nil
end
--===========================================================================
function InitTrig_CircleMove_Code()
    gg_trg_CircleMove_Code=CreateTrigger()
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(0), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(1), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(2), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(3), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(4), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(5), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(6), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(7), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(8), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(9), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(10), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(11), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(12), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(13), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(14), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(15), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(16), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(17), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(18), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(19), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(20), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(21), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(22), bj_MOUSEEVENTTYPE_DOWN)
    TriggerRegisterPlayerMouseEventBJ(gg_trg_CircleMove_Code, Player(23), bj_MOUSEEVENTTYPE_DOWN)
    TriggerAddCondition(gg_trg_CircleMove_Code, Condition(Trig_CircleMove_Code_Conditions))
    TriggerAddAction(gg_trg_CircleMove_Code, Trig_CircleMove_Code_Actions)
end
--===========================================================================
-- Trigger: Race Bezlikie O
--===========================================================================
function Trig_Race_Bezlikie_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('u02D'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0F9'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Bezlikie_O()
    gg_trg_Race_Bezlikie_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Bezlikie_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Bezlikie_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HW') then return end
        Trig_Race_Bezlikie_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race IceTrols
--===========================================================================
function Trig_Race_IceTrols_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o045'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0L1'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_IceTrols()
    gg_trg_Race_IceTrols=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_IceTrols, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_IceTrols, function()
        if GetSpellAbilityId() ~= FourCC('A1EG') then return end
        Trig_Race_IceTrols_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Stromgard O
--===========================================================================
function Trig_Race_Stromgard_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0G9'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0H3'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, GetOwningPlayer(GetTriggerUnit()))
    TriggerExecute(gg_trg_StromgardOn)
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Stromgard_O()
    gg_trg_Race_Stromgard_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Stromgard_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Stromgard_O, function()
        if GetSpellAbilityId() ~= FourCC('A0Y0') then return end
        Trig_Race_Stromgard_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Dragon O
--===========================================================================
function Trig_Race_Dragon_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(1, FourCC('dra1'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BY'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
    DragonsOn()
end
--===========================================================================
function InitTrig_Race_Dragon_O()
    gg_trg_Race_Dragon_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Dragon_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Dragon_O, function()
        if GetSpellAbilityId() ~= FourCC('A0RQ') then return end
        Trig_Race_Dragon_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Dragon2
--===========================================================================
function Trig_Race_Dragon2_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o01D'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    --call SetPlayerTechResearchedSwap( 'R0BY', 1, GetOwningPlayer(GetTriggerUnit()) )
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Dragon2()
    gg_trg_Race_Dragon2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Dragon2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Dragon2, function()
        if GetSpellAbilityId() ~= FourCC('A1MZ') then return end
        Trig_Race_Dragon2_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Argvinol O
--===========================================================================
function Trig_Race_Argvinol_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('e02T'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0BZ'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Argvinol_O()
    gg_trg_Race_Argvinol_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Argvinol_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Argvinol_O, function()
        if GetSpellAbilityId() ~= FourCC('A0QQ') then return end
        Trig_Race_Argvinol_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Elements O
--===========================================================================
function Trig_Race_Elements_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('e00F'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0A2'), 1, GetOwningPlayer(GetTriggerUnit()))
    ElemOn()
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Elements_O()
    gg_trg_Race_Elements_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Elements_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Elements_O, function()
        if GetSpellAbilityId() ~= FourCC('A0QN') then return end
        Trig_Race_Elements_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Goblins O
--===========================================================================
function Trig_Race_Goblins_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('n00V'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07E'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    TriggerExecute(gg_trg_GoblinsOn)
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Goblins_O()
    gg_trg_Race_Goblins_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Goblins_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Goblins_O, function()
        if GetSpellAbilityId() ~= FourCC('A0AC') then return end
        Trig_Race_Goblins_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Demon O
--===========================================================================
function Trig_Race_Demon_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(8, FourCC('e02Y'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0AO'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Demon_O()
    gg_trg_Race_Demon_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Demon_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Demon_O, function()
        if GetSpellAbilityId() ~= FourCC('A0MY') then return end
        Trig_Race_Demon_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Illidari O
--===========================================================================
function Trig_Race_Illidari_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0EI'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07H'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KZ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, GetOwningPlayer(GetTriggerUnit()))
    ConditionalTriggerExecute(gg_trg_IllidaryOn)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Illidari_O()
    gg_trg_Race_Illidari_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Illidari_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Illidari_O, function()
        if GetSpellAbilityId() ~= FourCC('A0OK') then return end
        Trig_Race_Illidari_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Bandits O
--===========================================================================
function Trig_Race_Bandits_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h002'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R00G'), 1, GetOwningPlayer(GetTriggerUnit()))
    TriggerExecute(gg_trg_BanditsOn)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Bandits_O()
    gg_trg_Race_Bandits_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Bandits_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Bandits_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HR') then return end
        Trig_Race_Bandits_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Red Orden O
--===========================================================================
function Trig_Race_Red_Orden_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h014'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07B'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Red_Orden_O()
    gg_trg_Race_Red_Orden_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Red_Orden_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Red_Orden_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HM') then return end
        Trig_Race_Red_Orden_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Undead O
--===========================================================================
function Trig_Race_Undead_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('u00P'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07I'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J5'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(gg_trg_UndeadOn)
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Undead_O()
    gg_trg_Race_Undead_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Undead_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Undead_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HV') then return end
        Trig_Race_Undead_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Horde
--===========================================================================
function Trig_Race_Horde_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('opeo'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0DV'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0IR'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, GetOwningPlayer(GetTriggerUnit()))
    ConditionalTriggerExecute(gg_trg_HordeOn)
    ConditionalTriggerExecute(gg_trg_StartHorde)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Horde()
    gg_trg_Race_Horde=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Horde, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Horde, function()
        if GetSpellAbilityId() ~= FourCC('A0YV') then return end
        Trig_Race_Horde_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Blood Elves O
--===========================================================================
function Trig_Race_Blood_Elves_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h04K'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07C'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, GetOwningPlayer(GetTriggerUnit()))
    ConditionalTriggerExecute(gg_trg_BloodElvesOn)
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Blood_Elves_O()
    gg_trg_Race_Blood_Elves_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Blood_Elves_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Blood_Elves_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HQ') then return end
        Trig_Race_Blood_Elves_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Dalaran O
--===========================================================================
function Trig_Race_Dalaran_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('u001'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BW'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Dalaran_O()
    gg_trg_Race_Dalaran_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Dalaran_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Dalaran_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HN') then return end
        Trig_Race_Dalaran_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race KulTiras O
--===========================================================================
function Trig_Race_KulTiras_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h013'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07D'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_KulTiras_O()
    gg_trg_Race_KulTiras_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_KulTiras_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_KulTiras_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HO') then return end
        Trig_Race_KulTiras_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Nocnorogdennue O
--===========================================================================
function Trig_Race_Nocnorogdennue_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0CJ'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R07J'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Nocnorogdennue_O()
    gg_trg_Race_Nocnorogdennue_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Nocnorogdennue_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Nocnorogdennue_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HU') then return end
        Trig_Race_Nocnorogdennue_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Draeneis O
--===========================================================================
function Trig_Race_Draeneis_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h012'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07G'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Draeneis_O()
    gg_trg_Race_Draeneis_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Draeneis_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Draeneis_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HS') then return end
        Trig_Race_Draeneis_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Vryculs O
--===========================================================================
function Trig_Race_Vryculs_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0C9'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07F'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Vryculs_O()
    gg_trg_Race_Vryculs_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Vryculs_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Vryculs_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HP') then return end
        Trig_Race_Vryculs_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Kult Sum Molota O
--===========================================================================
function Trig_Race_Kult_Sum_Molota_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o00J'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07K'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KD'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Kult_Sum_Molota_O()
    gg_trg_Race_Kult_Sum_Molota_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Kult_Sum_Molota_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Kult_Sum_Molota_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HX') then return end
        Trig_Race_Kult_Sum_Molota_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Nerubs O
--===========================================================================
function Trig_Race_Nerubs_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('h0BE'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07N'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Nerubs_O()
    gg_trg_Race_Nerubs_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Nerubs_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Nerubs_O, function()
        if GetSpellAbilityId() ~= FourCC('A0HT') then return end
        Trig_Race_Nerubs_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Silitids O
--===========================================================================
function Trig_Race_Silitids_O_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(8, FourCC('e01G'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BV'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('A1B7'), GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(gg_trg_SilitidsOn)
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Silitids_O()
    gg_trg_Race_Silitids_O=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Silitids_O, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Silitids_O, function()
        if GetSpellAbilityId() ~= FourCC('A0J7') then return end
        Trig_Race_Silitids_O_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Gnomes
--===========================================================================
function Trig_Race_Gnomes_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0FA'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    CreateNUnitsAtLoc(1, FourCC('h0FX'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0BX'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(gg_trg_GnomesOn)
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Gnomes()
    gg_trg_Race_Gnomes=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Gnomes, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Gnomes, function()
        if GetSpellAbilityId() ~= FourCC('A0SD') then return end
        Trig_Race_Gnomes_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Gilneas
--===========================================================================
function Trig_Race_Gilneas_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0IT'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0FX'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Gilneas()
    gg_trg_Race_Gilneas=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Gilneas, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Gilneas, function()
        if GetSpellAbilityId() ~= FourCC('A121') then return end
        Trig_Race_Gilneas_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Nagi
--===========================================================================
function Trig_Race_Nagi_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('nmpe'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0FS'), 1, GetOwningPlayer(GetTriggerUnit()))
    
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Nagi()
    gg_trg_Race_Nagi=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Nagi, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Nagi, function()
        if GetSpellAbilityId() ~= FourCC('A14O') then return end
        Trig_Race_Nagi_Actions()
    end)
end
--===========================================================================
-- Trigger: Race nightelf
--===========================================================================
function Trig_Race_nightelf_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(6, FourCC('ewsp'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R07L'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_nightelf()
    gg_trg_Race_nightelf=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_nightelf, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_nightelf, function()
        if GetSpellAbilityId() ~= FourCC('A0HL') then return end
        Trig_Race_nightelf_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Forsaken
--===========================================================================
function Trig_Race_Forsaken_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('h0J5'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0G3'), 1, GetOwningPlayer(GetTriggerUnit()))
    ForsakenOn()
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Forsaken()
    gg_trg_Race_Forsaken=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Forsaken, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Forsaken, function()
        if GetSpellAbilityId() ~= FourCC('A155') then return end
        Trig_Race_Forsaken_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Ogres
--===========================================================================
function Trig_Race_Ogres_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o03W'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerTechResearchedSwap(FourCC('R0HT'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveUnit(GetSpellAbilityUnit())
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Ogres()
    gg_trg_Race_Ogres=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Ogres, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Ogres, function()
        if GetSpellAbilityId() ~= FourCC('A17N') then return end
        Trig_Race_Ogres_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Alliance
--===========================================================================
function Trig_Race_Alliance_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('hpea'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    ConditionalTriggerExecute(gg_trg_AllyOn)
    SetPlayerTechResearchedSwap(FourCC('R0GZ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Alliance()
    gg_trg_Race_Alliance=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Alliance, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Alliance, function()
        if GetSpellAbilityId() ~= FourCC('A02A') then return end
        Trig_Race_Alliance_Actions()
    end)
end
--===========================================================================
-- Trigger: Race JungleTrolls
--===========================================================================
function Trig_Race_JungleTrolls_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o04Q'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    --call ConditionalTriggerExecute( gg_trg_AllyOn )
    SetPlayerTechResearchedSwap(FourCC('R0IH'), 1, GetOwningPlayer(GetTriggerUnit()))
    StartJungleTrolls()
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_JungleTrolls()
    gg_trg_Race_JungleTrolls=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_JungleTrolls, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_JungleTrolls, function()
        if GetSpellAbilityId() ~= FourCC('A1DZ') then return end
        Trig_Race_JungleTrolls_Actions()
    end)
end
--===========================================================================
-- Trigger: Race FelOrk
--===========================================================================
function Trig_Race_FelOrk_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('n06B'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    SetPlayerTechResearchedSwap(FourCC('R0KA'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, GetOwningPlayer(GetTriggerUnit()))
    
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_FelOrk()
    gg_trg_Race_FelOrk=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_FelOrk, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_FelOrk, function()
        if GetSpellAbilityId() ~= FourCC('A1JL') then return end
        Trig_Race_FelOrk_Actions()
    end)
end
--===========================================================================
-- Trigger: Race ForestTrolls
--===========================================================================
function Trig_Race_ForestTrolls_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('o04V'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    --call ConditionalTriggerExecute( gg_trg_AllyOn )
    SetPlayerTechResearchedSwap(FourCC('R0J1'), 1, GetOwningPlayer(GetTriggerUnit()))
    StartForestTrolls()
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_ForestTrolls()
    gg_trg_Race_ForestTrolls=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_ForestTrolls, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_ForestTrolls, function()
        if GetSpellAbilityId() ~= FourCC('A1FN') then return end
        Trig_Race_ForestTrolls_Actions()
    end)
end
--===========================================================================
-- Trigger: Race CultOfDamned
--===========================================================================
function Trig_Race_CultOfDamned_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(3, FourCC('cD02'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    
    SetPlayerTechResearchedSwap(FourCC('R0J4'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0J5'), 1, GetOwningPlayer(GetTriggerUnit()))
    CultOn()
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_CultOfDamned()
    gg_trg_Race_CultOfDamned=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_CultOfDamned, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_CultOfDamned, function()
        if GetSpellAbilityId() ~= FourCC('A1HA') then return end
        Trig_Race_CultOfDamned_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Pandarens
--===========================================================================
function Trig_Race_Pandarens_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('pa01'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    --call ConditionalTriggerExecute( gg_trg_AllyOn )
    SetPlayerTechResearchedSwap(FourCC('R0L3'), 1, GetOwningPlayer(GetTriggerUnit()))
    --call SetPlayerTechResearchedSwap( 'R0J5', 1, GetOwningPlayer(GetTriggerUnit()) )
    Pstart(GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(udg_LocalPosition2)
end
--===========================================================================
function InitTrig_Race_Pandarens()
    gg_trg_Race_Pandarens=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Pandarens, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Pandarens, function()
        if GetSpellAbilityId() ~= FourCC('A1I6') then return end
        Trig_Race_Pandarens_Actions()
    end)
end
--===========================================================================
-- Trigger: Race HordeW2
--===========================================================================
function Trig_Race_HordeW2_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    CreateNUnitsAtLoc(5, FourCC('w200'), GetOwningPlayer(GetSpellAbilityUnit()), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveUnit(GetSpellAbilityUnit())
    --call ConditionalTriggerExecute( gg_trg_AllyOn )
    SetPlayerTechResearchedSwap(FourCC('R0KB'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechResearchedSwap(FourCC('R0KD'), 1, GetOwningPlayer(GetTriggerUnit()))
    
    --call SetPlayerTechResearchedSwap( 'R0J5', 1, GetOwningPlayer(GetTriggerUnit()) )
    --call Pstart(GetOwningPlayer(GetTriggerUnit()))
    RemoveLocation(udg_LocalPosition2)
    HordeW2On()
end
--===========================================================================
function InitTrig_Race_HordeW2()
    gg_trg_Race_HordeW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_HordeW2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_HordeW2, function()
        if GetSpellAbilityId() ~= FourCC('A1JN') then return end
        Trig_Race_HordeW2_Actions()
    end)
end
--===========================================================================
-- Trigger: Race Random
--===========================================================================
function incN()
    icrisingN=icrisingN + 1
    return icrisingN
end
function Trig_Race_Random_Actions()
    local racecount= 34
    local racechance
    local l= GetUnitLoc(GetTriggerUnit())
    local p= GetOwningPlayer(GetTriggerUnit())
    RemoveUnit(GetSpellAbilityUnit())
    racechance=GetRandomInt(1, racecount)
    icrisingN=0
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h0G9'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0H3'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, p)
        TriggerExecute(gg_trg_StromgardOn)
    end
    
    --???????
    if racechance == incN() then
        
        CreateNUnitsAtLoc(1, FourCC('dra1'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BY'), 1, p)
        DragonsOn()
    end
    --??????????
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('e00F'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0A2'), 1, p)
        ElemOn()
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('n00V'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07E'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, p)
        TriggerExecute(gg_trg_GoblinsOn)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(8, FourCC('e02Y'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0AO'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h0EI'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07H'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KZ'), 1, p) --Illidary or Nagi
        SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, p) --Illidary or Blood elves
        ConditionalTriggerExecute(gg_trg_IllidaryOn)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h002'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R00G'), 1, p)
        TriggerExecute(gg_trg_BanditsOn)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h014'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07B'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(3, FourCC('u00P'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07I'), 1, p)
        ConditionalTriggerExecute(gg_trg_UndeadOn)
    end
    -- Blood elves
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h04K'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07C'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0L0'), 1, p)
        ConditionalTriggerExecute(gg_trg_BloodElvesOn)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('opeo'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0DV'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0J3'), 1, p)
        ConditionalTriggerExecute(gg_trg_HordeOn)
    end
    --Dalaran
    if racechance == incN() then
        CreateNUnitsAtLoc(3, FourCC('u001'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BW'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h013'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07D'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h0CJ'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07J'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h012'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07G'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h0C9'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07F'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('o00J'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07K'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(3, FourCC('h0BE'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07N'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(3, FourCC('h0BE'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R07N'), 1, p)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(8, FourCC('e01G'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BV'), 1, p)
        SetPlayerAbilityAvailableBJ(true, FourCC('A1B7'), p)
        ConditionalTriggerExecute(gg_trg_SilitidsOn)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h0FA'), p, l, bj_UNIT_FACING)
        CreateNUnitsAtLoc(1, FourCC('h0FX'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BX'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
        ConditionalTriggerExecute(gg_trg_GnomesOn)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h0FA'), p, l, bj_UNIT_FACING)
        CreateNUnitsAtLoc(1, FourCC('h0FX'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0BX'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
        ConditionalTriggerExecute(gg_trg_GnomesOn)
    end
    
    if racechance == incN() then
        SetPlayerTechResearchedSwap(FourCC('R0FX'), 1, p)
        CreateNUnitsAtLoc(5, FourCC('h0IT'), p, l, bj_UNIT_FACING)
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('nmpe'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0FS'), 1, p)
        --call SetPlayerTechResearchedSwap( 'R0KZ', 1, p )
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(6, FourCC('ewsp'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0G4'), 1, p)
    end
    
    --Forsaken ??????????
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('h0J5'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0G3'), 1, p)
        ForsakenOn()
    end
    
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('o03W'), p, l, bj_UNIT_FACING)
    end
    --Alliance
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('hpea'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0GZ'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HX'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HW'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0HY'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KK'), 1, p)
    end
    
    
    
    -- Horde W2
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('w200'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0KB'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KD'), 1, p)
        HordeW2On()
    end
    --Pandarens
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('pa01'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0L3'), 1, p)
    end
    -- Cult of Damned
    if racechance == incN() then
        CreateNUnitsAtLoc(3, FourCC('cD02'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0J4'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0J5'), 1, p)
        CultOn()
    end
    --Forest Trolls
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('o04V'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0J1'), 1, p)
        StartForestTrolls()
    end
    --FellOrc
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('n06B'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0KA'), 1, p)
        SetPlayerTechResearchedSwap(FourCC('R0KC'), 1, p)
    end
    --Jungle Trolls
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('o04Q'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0IH'), 1, p)
        StartJungleTrolls()
    end
    --Ice Trolls
    if racechance == incN() then
        CreateNUnitsAtLoc(5, FourCC('o045'), p, l, bj_UNIT_FACING)
        SetPlayerTechResearchedSwap(FourCC('R0L1'), 1, p)
        --call StartJungleTrolls()
    end
    RemoveLocation(l)
end
--===========================================================================
function InitTrig_Race_Random()
    gg_trg_Race_Random=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Race_Random, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Race_Random, function()
        if GetSpellAbilityId() ~= FourCC('A12Q') then return end
        Trig_Race_Random_Actions()
    end)
end
--===========================================================================
-- Trigger: Page1
--===========================================================================
function Trig_Page1_Actions()
    UnitAddAbilityBJ(FourCC('A0HZ'), GetTriggerUnit()) -- 2 c
    UnitRemoveAbilityBJ(FourCC('A0I1'), GetTriggerUnit()) -- 1 c
    
    
    
    
    
    UnitAddAbilityBJ(FourCC('A02A'), GetTriggerUnit()) -- ??????
    UnitAddAbilityBJ(FourCC('A0YV'), GetTriggerUnit()) -- Horde
    UnitAddAbilityBJ(FourCC('A0HV'), GetTriggerUnit()) -- Plet
    UnitAddAbilityBJ(FourCC('A0HL'), GetTriggerUnit()) -- Night Elves
    
    UnitAddAbilityBJ(FourCC('A0HQ'), GetTriggerUnit()) -- Blood Elves
    UnitAddAbilityBJ(FourCC('A14O'), GetTriggerUnit()) -- Nags
    UnitAddAbilityBJ(FourCC('A0OK'), GetTriggerUnit()) -- Illidary
    UnitAddAbilityBJ(FourCC('A0MY'), GetTriggerUnit()) -- Legion
    UnitAddAbilityBJ(FourCC('A0HS'), GetTriggerUnit()) -- Draeneys
    
    
    
    
    
    UnitRemoveAbilityBJ(FourCC('A0QN'), GetTriggerUnit()) -- Elems
    UnitRemoveAbilityBJ(FourCC('A0HT'), GetTriggerUnit()) -- Nerubs
    UnitRemoveAbilityBJ(FourCC('A0QQ'), GetTriggerUnit()) -- Argwinol (Ent)
    
    UnitRemoveAbilityBJ(FourCC('A0RQ'), GetTriggerUnit()) -- Dragons
    UnitRemoveAbilityBJ(FourCC('A0J7'), GetTriggerUnit()) -- Ogres
    UnitRemoveAbilityBJ(FourCC('A1HA'), GetTriggerUnit()) -- Cult of Damned
    
    
    UnitRemoveAbilityBJ(FourCC('A1JN'), GetTriggerUnit()) -- HordeW2
    UnitRemoveAbilityBJ(FourCC('A0HW'), GetTriggerUnit()) -- Faceless
end
--===========================================================================
function InitTrig_Page1()
    gg_trg_Page1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Page1, EVENT_PLAYER_UNIT_SPELL_ENDCAST)
    TriggerAddAction(gg_trg_Page1, function()
        if GetSpellAbilityId() ~= FourCC('A0I1') then return end
        Trig_Page1_Actions()
    end)
end
--===========================================================================
-- Trigger: Page2
--===========================================================================
function Trig_Page2_Actions()
    
    UnitRemoveAbilityBJ(GetSpellAbilityId(), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A1GW'), GetTriggerUnit())
    
    
    
    
    UnitAddAbilityBJ(FourCC('A0HM'), GetTriggerUnit()) -- ???? ?????
    UnitAddAbilityBJ(FourCC('A0Y0'), GetTriggerUnit()) -- ?????
    UnitAddAbilityBJ(FourCC('A1EG'), GetTriggerUnit()) -- ??????? ??????
    
    UnitAddAbilityBJ(FourCC('A121'), GetTriggerUnit()) -- Worgens
    UnitAddAbilityBJ(FourCC('A0HN'), GetTriggerUnit()) -- Dalaran
    UnitAddAbilityBJ(FourCC('A1FN'), GetTriggerUnit()) -- ?????? ??????
    
    
    UnitAddAbilityBJ(FourCC('A0HR'), GetTriggerUnit()) -- Thieves
    UnitAddAbilityBJ(FourCC('A0HO'), GetTriggerUnit()) -- Kultiras
    UnitAddAbilityBJ(FourCC('A1DZ'), GetTriggerUnit()) -- Trolls Jungle
    
    
    
    
    
    UnitRemoveAbilityBJ(FourCC('A02A'), GetTriggerUnit()) -- ??????
    UnitRemoveAbilityBJ(FourCC('A0YV'), GetTriggerUnit()) -- Horde
    UnitRemoveAbilityBJ(FourCC('A0HV'), GetTriggerUnit()) -- Plet
    UnitRemoveAbilityBJ(FourCC('A0HL'), GetTriggerUnit()) -- Night Elves
    
    UnitRemoveAbilityBJ(FourCC('A0HQ'), GetTriggerUnit()) -- Blood Elves
    UnitRemoveAbilityBJ(FourCC('A14O'), GetTriggerUnit()) -- Nags
    UnitRemoveAbilityBJ(FourCC('A0OK'), GetTriggerUnit()) -- Illidary
    UnitRemoveAbilityBJ(FourCC('A0MY'), GetTriggerUnit()) -- Legion
    UnitRemoveAbilityBJ(FourCC('A0HS'), GetTriggerUnit()) -- Draeneys
    
end
--===========================================================================
function InitTrig_Page2()
    gg_trg_Page2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Page2, EVENT_PLAYER_UNIT_SPELL_ENDCAST)
    TriggerAddAction(gg_trg_Page2, function()
        if GetSpellAbilityId() ~= FourCC('A0HZ') then return end
        Trig_Page2_Actions()
    end)
end
--===========================================================================
-- Trigger: Page3
--===========================================================================
function Trig_Page3_Actions()
    
    
    
    
    
    
    
    
    
        
    
    UnitAddAbilityBJ(FourCC('A0SD'), GetTriggerUnit()) -- Gnomes
    UnitAddAbilityBJ(FourCC('A0AC'), GetTriggerUnit()) -- Goblins
    UnitAddAbilityBJ(FourCC('A0HU'), GetTriggerUnit()) -- Nighborn
    
    UnitAddAbilityBJ(FourCC('A0HP'), GetTriggerUnit()) -- Vryculs
    UnitAddAbilityBJ(FourCC('A17N'), GetTriggerUnit()) -- Ogres
    UnitAddAbilityBJ(FourCC('A155'), GetTriggerUnit()) -- Forsacen
    
    
    UnitAddAbilityBJ(FourCC('A1I6'), GetTriggerUnit()) -- Pandarens
    UnitAddAbilityBJ(FourCC('A0HX'), GetTriggerUnit()) -- Twilig cult
    UnitAddAbilityBJ(FourCC('A1JL'), GetTriggerUnit()) -- Horde of Fel
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    UnitRemoveAbilityBJ(FourCC('A0HM'), GetTriggerUnit()) -- ???? ?????
    UnitRemoveAbilityBJ(FourCC('A0Y0'), GetTriggerUnit()) -- ?????
    UnitRemoveAbilityBJ(FourCC('A1EG'), GetTriggerUnit()) -- ??????? ??????
    
    UnitRemoveAbilityBJ(FourCC('A121'), GetTriggerUnit()) -- Worgens
    UnitRemoveAbilityBJ(FourCC('A0HN'), GetTriggerUnit()) -- Dalaran
    UnitRemoveAbilityBJ(FourCC('A1FN'), GetTriggerUnit()) -- ?????? ??????
    
    
    UnitRemoveAbilityBJ(FourCC('A0HR'), GetTriggerUnit()) -- Thieves
    UnitRemoveAbilityBJ(FourCC('A0HO'), GetTriggerUnit()) -- Kultiras
    UnitRemoveAbilityBJ(FourCC('A1DZ'), GetTriggerUnit()) -- Trolls Jungle
    
    
    
    UnitAddAbilityBJ(FourCC('A0QR'), GetTriggerUnit())
    UnitRemoveAbilityBJ(GetSpellAbilityId(), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Page3()
    gg_trg_Page3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Page3, EVENT_PLAYER_UNIT_SPELL_ENDCAST)
    TriggerAddAction(gg_trg_Page3, function()
        if GetSpellAbilityId() ~= FourCC('A1GW') then return end
        Trig_Page3_Actions()
    end)
end
--===========================================================================
-- Trigger: Page4
--===========================================================================
function Trig_Page4_Actions()
    
    
        
    
    UnitAddAbilityBJ(FourCC('A0QN'), GetTriggerUnit()) -- Elems
    UnitAddAbilityBJ(FourCC('A0HT'), GetTriggerUnit()) -- Nerubs
    UnitAddAbilityBJ(FourCC('A0QQ'), GetTriggerUnit()) -- Argwinol (Ent)
    
    UnitAddAbilityBJ(FourCC('A0RQ'), GetTriggerUnit()) -- Dragons
    UnitAddAbilityBJ(FourCC('A0J7'), GetTriggerUnit()) -- Ogres
    UnitAddAbilityBJ(FourCC('A1HA'), GetTriggerUnit()) -- Cult of Damned
    
    
    UnitAddAbilityBJ(FourCC('A1JN'), GetTriggerUnit()) -- HordeW2
    UnitAddAbilityBJ(FourCC('A0HW'), GetTriggerUnit()) -- Faceless
    
    
        
    
    
    UnitRemoveAbilityBJ(FourCC('A0SD'), GetTriggerUnit()) -- Gnomes
    UnitRemoveAbilityBJ(FourCC('A0AC'), GetTriggerUnit()) -- Goblins
    UnitRemoveAbilityBJ(FourCC('A0HU'), GetTriggerUnit()) -- Nighborn
    
    UnitRemoveAbilityBJ(FourCC('A0HP'), GetTriggerUnit()) -- Vryculs
    UnitRemoveAbilityBJ(FourCC('A17N'), GetTriggerUnit()) -- Ogres
    UnitRemoveAbilityBJ(FourCC('A155'), GetTriggerUnit()) -- Forsacen
    
    
    UnitRemoveAbilityBJ(FourCC('A1I6'), GetTriggerUnit()) -- Pandarens
    UnitRemoveAbilityBJ(FourCC('A0HX'), GetTriggerUnit()) -- Twilig cult
    UnitRemoveAbilityBJ(FourCC('A1JL'), GetTriggerUnit()) -- Horde of Fel
    
    
        
    
    
    UnitAddAbility(GetTriggerUnit(), FourCC('A0I1'))
    UnitRemoveAbility(GetTriggerUnit(), GetSpellAbilityId())
end
--===========================================================================
function InitTrig_Page4()
