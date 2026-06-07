	gg_trg_FastResearch = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_FastResearch, EVENT_PLAYER_UNIT_RESEARCH_START)
	TriggerAddCondition(gg_trg_FastResearch, Condition(Trig_FastResearch_Conditions))
	TriggerAddAction(gg_trg_FastResearch, Trig_FastResearch_Actions)
end
-- ===========================================================================
--  Trigger: Only Eastern
-- ===========================================================================
---@return boolean
function Trig_Only_Eastern_Func004001002()
	return (GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1)
end
---@return nothing
function Trig_Only_Eastern_Func004A()
	WaygateActivateBJ(false, GetEnumUnit())
end
---@return nothing
function Trig_Only_Eastern_Actions()
	DisplayTextToForce(udg_AllPlayers, "TRIGSTR_19899")
	EnableTrigger(gg_trg_Leave_Easten)
	EnableTrigger(gg_trg_Back_Easten)
	ForGroupBJ(GetUnitsInRectMatching(GetPlayableMapRect(), Condition(Trig_Only_Eastern_Func004001002)), Trig_Only_Eastern_Func004A)
end
-- ===========================================================================
---@return nothing
function InitTrig_Only_Eastern()
	gg_trg_Only_Eastern = CreateTrigger()
	TriggerRegisterPlayerChatEvent(gg_trg_Only_Eastern, Player(0), "-only ek", true)
	TriggerAddAction(gg_trg_Only_Eastern, Trig_Only_Eastern_Actions)
end
-- ===========================================================================
--  Trigger: Leave Easten
-- ===========================================================================
---@return nothing
function Trig_Leave_Easten_Actions()
	udg_LocalUnit2 = GetTriggerUnit()
	UnitAddAbilityBJ(FourCC('A0U6'), GetTriggerUnit())
end
-- ===========================================================================
---@return nothing
function InitTrig_Leave_Easten()
	gg_trg_Leave_Easten = CreateTrigger()
	DisableTrigger(gg_trg_Leave_Easten)
	TriggerRegisterLeaveRectSimple(gg_trg_Leave_Easten, gg_rct_EastenKingdoms)
	TriggerAddAction(gg_trg_Leave_Easten, Trig_Leave_Easten_Actions)
end
-- ===========================================================================
--  Trigger: Back Easten
-- ===========================================================================
---@return nothing
function Trig_Back_Easten_Actions()
	UnitRemoveAbilityBJ(FourCC('A0U6'), GetTriggerUnit())
end
-- ===========================================================================
---@return nothing
function InitTrig_Back_Easten()
	gg_trg_Back_Easten = CreateTrigger()
	DisableTrigger(gg_trg_Back_Easten)
	TriggerRegisterEnterRectSimple(gg_trg_Back_Easten, gg_rct_EastenKingdoms)
	TriggerAddAction(gg_trg_Back_Easten, Trig_Back_Easten_Actions)
end
-- ===========================================================================
--  Trigger: Continents Spell
-- ===========================================================================
---@return boolean
---@return nothing
function Trig_Continents_Spell_Actions()
	DisplayTextToForce(GetPlayersAll(), "TRIGSTR_12041")
	udg_Continents[0] = 0
	for bj_forLoopAIndex = 1, 15 do
		udg_Continents[GetForLoopIndexA()] = 0
	end
	UnitAddAbilityBJ(FourCC('A0UB'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0UM'), GetTriggerUnit())
	UnitAddAbilityBJ(FourCC('A0UC'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0UN'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0UO'), GetTriggerUnit())
	UnitAddAbilityBJ(FourCC('A0UD'), GetTriggerUnit())
	UnitAddAbilityBJ(FourCC('A0UE'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0UP'), GetTriggerUnit())
	UnitAddAbilityBJ(FourCC('A0UF'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0UQ'), GetTriggerUnit())
	UnitAddAbilityBJ(FourCC('A0UH'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0UR'), GetTriggerUnit())
	UnitAddAbilityBJ(FourCC('A0UG'), GetTriggerUnit())
	UnitRemoveAbilityBJ(FourCC('A0US'), GetTriggerUnit())
end
-- ===========================================================================
---@return nothing
function InitTrig_Continents_Spell()
	gg_trg_Continents_Spell = CreateTrigger()
	TriggerRegisterAnyUnitEventBJ(gg_trg_Continents_Spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Continents_Spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UI') then return end
        Trig_Continents_Spell_Actions()
    end)
end
-- ===========================================================================
--  Trigger: Continents set On
-- ===========================================================================
---@return boolean
function Trig_Continents_set_On_Conditions()
	if ( not (udg_Continents[0] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func004C()
	if ( not (udg_Continents[1] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func005C()
	if ( not (udg_Continents[2] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func006C()
	if ( not (udg_Continents[3] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func007C()
	if ( not (udg_Continents[4] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func008C()
	if ( not (udg_Continents[5] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func009C()
	if ( not (udg_Continents[6] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func010C()
	if ( not (udg_Continents[7] == 1)) then
		return false
	end
	return true
end
---@return boolean
function Trig_Continents_set_On_Func013001002()
	return (GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1)
end
---@return nothing
function Trig_Continents_set_On_Func013A()
	WaygateActivateBJ(false, GetEnumUnit())
end
---@return nothing
function Trig_Continents_set_On_Actions()
	udg_LocalText2 = ("????? ???????????:|cffffff00 ???????|r")
	DisplayTextToForce(GetPlayersAll(), udg_LocalText2)
	udg_LocalText2 = "|cff00ff00????? ???????? ??? ????: |r"
	if (Trig_Continents_set_On_Func004C()) then
		udg_LocalText2 = (udg_LocalText2 .. "????????? ???????????\\" )
    else
    end
    if ( Trig_Continents_set_On_Func005C() ) then
        udg_LocalText2=( udg_LocalText2 + "" )
    else
    end
    if ( Trig_Continents_set_On_Func006C() ) then
        udg_LocalText2=( udg_LocalText2 + "" )
    else
    end
    if ( Trig_Continents_set_On_Func007C() ) then
        udg_LocalText2=( udg_LocalText2 + "" )
    else
    end
    if ( Trig_Continents_set_On_Func008C() ) then
        udg_LocalText2=( udg_LocalText2 + "" )
    else
    end
    if ( Trig_Continents_set_On_Func009C() ) then
        udg_LocalText2=( udg_LocalText2 + "" )
    else
    end
    if ( Trig_Continents_set_On_Func010C() ) then
        udg_LocalText2=( udg_LocalText2 + "" )
    else
    end
    DisplayTextToForce(GetPlayersAll(), udg_LocalText2)
    EnableTrigger(gg_trg_LeaveNeadedRegions)
    ForGroupBJ(GetUnitsInRectMatching(GetPlayableMapRect(), Condition(Trig_Continents_set_On_Func013001002)), Trig_Continents_set_On_Func013A)
    StartTimerBJ(udg_TimerToCont, false, 0.50)
end
--===========================================================================
function InitTrig_Continents_set_On()
    gg_trg_Continents_set_On=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Continents_set_On, udg_LobbyTime)
    TriggerAddCondition(gg_trg_Continents_set_On, Condition(Trig_Continents_set_On_Conditions))
    TriggerAddAction(gg_trg_Continents_set_On, Trig_Continents_set_On_Actions)
end
--===========================================================================
-- Trigger: Continents Off
--===========================================================================
function Trig_Continents_Off_Conditions()
    if ( not ( udg_Continents[0] == 0 ) ) then
        return false
    end
    return true
end
function Trig_Continents_Off_Func005001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
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
    udg_LocalText2=( "cffffff00r" )
    DisplayTextToForce(GetPlayersAll(), udg_LocalText2)
    ForGroupBJ(GetUnitsInRectMatching(GetPlayableMapRect(), Condition(Trig_Continents_Off_Func005001002)), Trig_Continents_Off_Func005A)
    ForForce(udg_AllPlayers, Trig_Continents_Off_Func006A)
end
--===========================================================================
function InitTrig_Continents_Off()
    gg_trg_Continents_Off=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Continents_Off, udg_LobbyTime)
    TriggerAddCondition(gg_trg_Continents_Off, Condition(Trig_Continents_Off_Conditions))
    TriggerAddAction(gg_trg_Continents_Off, Trig_Continents_Off_Actions)
end
--===========================================================================
-- Trigger: ItsFineOrNot
--===========================================================================
function AllowedPosition()
    local x= GetUnitX(u)
    local y= GetUnitY(u)
    
    if udg_Continents[1] == 1 and ( RectContainsCoords(gg_rct_EastenKingdoms, x, y) or RectContainsCoords(gg_rct_BlackMountain, x, y) or RectContainsCoords(gg_rct_EasternDungeons, x, y) ) then
        return true
    end
    if udg_Continents[2] == 1 and ( RectContainsCoords(gg_rct_Kalim, x, y) or RectContainsCoords(gg_rct_Ankirag, x, y) and RectContainsCoords(gg_rct_Maradon, x, y) and RectContainsCoords(gg_rct_Orgrimmar, x, y) ) then
        return true
    end
    if udg_Continents[3] == 1 and ( RectContainsCoords(gg_rct_Outland, x, y) ) then
        return true
    end
    if udg_Continents[4] == 1 and ( RectContainsCoords(gg_rct_Nord, x, y) or RectContainsCoords(gg_rct_Azgel, x, y) ) then
        return true
    end
    if udg_Continents[5] == 1 and ( RectContainsCoords(gg_rct_Pandaria, x, y) ) then
        return true
    end
    if udg_Continents[6] == 1 and ( RectContainsCoords(gg_rct_Argus, x, y) ) then
        return true
    end
    if udg_Continents[7] == 1 and RectContainsCoords(gg_rct_BrokenIsles, x, y) then
        return true
    end
    if RectContainsCoords(gg_rct_EmeraldDream, x, y) then
        return true
    end
    return false
end
function KillIf()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    --local integer uid = StringHash( I2S(GetHandleId(u))+"k")
    local time= LoadInteger(Hash, id, 1)
    local e= LoadEffectHandle(Hash, id, 2)
    
    
    if time > 0 then
        if GetUnitAbilityLevel(u, FourCC('A0U6')) == 0 or AllowedPosition(u) then
            UnitRemoveAbility(u, FourCC('A0U6'))
            UnitRemoveAbility(u, FourCC('B05M'))
            DestroyEffect(e)
            DestroyTimer(t)
            FlushChildHashtable(Hash, id)
        
        else
            time=time - 2
            SaveInteger(Hash, id, 1, time)
        
        end
        
        
        
    
    
    else
        KillUnit(u)
        DestroyEffect(e)
        DestroyTimer(t)
        FlushChildHashtable(Hash, id)
        
    end
    
    t=nil
    u=nil
    e=nil
end
function Continents()
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    --local integer uid = StringHash( I2S(GetHandleId(u))+"k")
    local e
    if AllowedPosition(u) then
        if GetUnitAbilityLevel(u, FourCC('A0U6')) > 0 then
            UnitRemoveAbility(u, FourCC('A0U6'))
            UnitRemoveAbility(u, FourCC('B05M'))
        end
        
        
    else
        if IsUnitType(u, UNIT_TYPE_STRUCTURE) then
            ExplodeUnitBJ(u)
            
        elseif GetUnitTypeId(u) == FourCC('H049') then
            
            
        else
            if GetUnitAbilityLevel(u, FourCC('A0U6')) > 0 then
                SetUnitPosition(u, 0, 0)
                DisplayTextToPlayer(GetOwningPlayer(u), 0, 0, "")
                
                
                --call SaveInteger(Hash,id,1,30)
                
            else
                UnitAddAbility(u, FourCC('A0U6'))
                e=AddSpecialEffectTarget("AbilitiesSpellsOtherTalkToMeTalkToMe", u, "overhead")
                --call TriggerExecute( gg_trg_GoHome_No_fine )
                
                
                TimerStart(t, 2, true, KillIf)
                --call SaveTimerHandle(Hash,uid,0,t)
                SaveUnitHandle(Hash, id, 0, u)
                SaveInteger(Hash, id, 1, 30)
                SaveEffectHandle(Hash, id, 2, e)
            end
            
        end
    end
    
    t=nil
    u=nil
    e=nil
end
--===========================================================================
-- Trigger: LeaveNeadedRegions
--===========================================================================
function Trig_LeaveNeadedRegions_Conditions()
    return udg_Continents[0] == 1
end
function Trig_LeaveNeadedRegions_Actions()
    Continents(GetTriggerUnit())
end
--===========================================================================
function InitTrig_LeaveNeadedRegions()
    gg_trg_LeaveNeadedRegions=CreateTrigger()
    DisableTrigger(gg_trg_LeaveNeadedRegions)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_Pandaria)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_Outland)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_Nord)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_EastenKingdoms)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_Kalim)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_BrokenIsles)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_Argus)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_BlackMountain)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_Azgel)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_Ankirag)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_HostRegion)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_BlackMountain)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_EasternDungeons)
    TriggerRegisterLeaveRectSimple(gg_trg_LeaveNeadedRegions, gg_rct_EmeraldDream)
    TriggerAddCondition(gg_trg_LeaveNeadedRegions, Condition(Trig_LeaveNeadedRegions_Conditions))
    TriggerAddAction(gg_trg_LeaveNeadedRegions, Trig_LeaveNeadedRegions_Actions)
end
--===========================================================================
-- Trigger: UseMassProssvet
--===========================================================================
function Trig_UseMassProssvet_Func008C()
    if ( not ( GetItemTypeId(GetManipulatedItem()) == FourCC('I00C') ) ) then
        return false
    end
    if ( not ( udg_Continents[0] == 1 ) ) then
        return false
    end
    return true
end
function Trig_UseMassProssvet_Conditions()
    if ( not Trig_UseMassProssvet_Func008C() ) then
        return false
    end
    return true
end
function Trig_UseMassProssvet_Actions()
    TriggerSleepAction(7.00)
    FogModifierStop(GetLastCreatedFogModifier())
    DestroyFogModifier(GetLastCreatedFogModifier())
    TriggerExecute(gg_trg_SeeOnlyNeedeed)
end
--===========================================================================
function InitTrig_UseMassProssvet()
    gg_trg_UseMassProssvet=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UseMassProssvet, EVENT_PLAYER_UNIT_PICKUP_ITEM)
    TriggerAddCondition(gg_trg_UseMassProssvet, Condition(Trig_UseMassProssvet_Conditions))
    TriggerAddAction(gg_trg_UseMassProssvet, Trig_UseMassProssvet_Actions)
end
--===========================================================================
-- Trigger: SeeOnlyNeedeed
--===========================================================================
function Trig_SeeOnlyNeedeed_Func001C()
    if ( not ( udg_Continents[1] == 1 ) ) then
        return false
    end
    return true
end
function Trig_SeeOnlyNeedeed_Func002C()
    if ( not ( udg_Continents[2] == 1 ) ) then
        return false
    end
    return true
end
function Trig_SeeOnlyNeedeed_Func003C()
    if ( not ( udg_Continents[3] == 1 ) ) then
        return false
    end
    return true
end
function Trig_SeeOnlyNeedeed_Func004C()
    if ( not ( udg_Continents[4] == 1 ) ) then
        return false
    end
    return true
end
function Trig_SeeOnlyNeedeed_Func005C()
    if ( not ( udg_Continents[5] == 1 ) ) then
        return false
    end
    return true
end
function Trig_SeeOnlyNeedeed_Func006C()
    if ( not ( udg_Continents[6] == 1 ) ) then
        return false
    end
    return true
end
function Trig_SeeOnlyNeedeed_Func007C()
    if ( not ( udg_Continents[7] == 1 ) ) then
        return false
    end
    return true
end
function Trig_SeeOnlyNeedeed_Actions()
    if ( Trig_SeeOnlyNeedeed_Func001C() ) then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
    end
    if ( Trig_SeeOnlyNeedeed_Func002C() ) then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
    end
    if ( Trig_SeeOnlyNeedeed_Func003C() ) then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
    end
    if ( Trig_SeeOnlyNeedeed_Func004C() ) then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
    end
    if ( Trig_SeeOnlyNeedeed_Func005C() ) then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
    end
    if ( Trig_SeeOnlyNeedeed_Func006C() ) then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
    end
    if ( Trig_SeeOnlyNeedeed_Func007C() ) then
        FogModifierStop(GetLastCreatedFogModifier())
        DestroyFogModifier(GetLastCreatedFogModifier())
    else
    end
end
--===========================================================================
function InitTrig_SeeOnlyNeedeed()
    gg_trg_SeeOnlyNeedeed=CreateTrigger()
    TriggerAddAction(gg_trg_SeeOnlyNeedeed, Trig_SeeOnlyNeedeed_Actions)
end
--===========================================================================
-- Trigger: NoBuild
--===========================================================================
function Trig_NoBuild_Conditions()
    return udg_Continents[0] == 1
end
function Trig_NoBuild_Actions()
    Continents(GetTriggerUnit())
end
--===========================================================================
function InitTrig_NoBuild()
    gg_trg_NoBuild=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NoBuild, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_NoBuild, Condition(Trig_NoBuild_Conditions))
    TriggerAddAction(gg_trg_NoBuild, Trig_NoBuild_Actions)
end
--===========================================================================
-- Trigger: EasternOn 1
--===========================================================================
function Trig_EasternOn_1_Conditions()
    if ( not ( udg_Continents[1] == 1 ) ) then
        return false
    end
    return true
end
function Trig_EasternOn_1_Func003001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_EasternOn_1_Func003A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_EasternOn_1_Func004001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_EasternOn_1_Func004A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_EasternOn_1_Func005001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_EasternOn_1_Func005A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_EasternOn_1_Actions()
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_EastenKingdoms, Condition(Trig_EasternOn_1_Func003001002)), Trig_EasternOn_1_Func003A)
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_EasternDungeons, Condition(Trig_EasternOn_1_Func004001002)), Trig_EasternOn_1_Func004A)
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_BlackMountain, Condition(Trig_EasternOn_1_Func005001002)), Trig_EasternOn_1_Func005A)
end
--===========================================================================
function InitTrig_EasternOn_1()
    gg_trg_EasternOn_1=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_EasternOn_1, udg_TimerToCont)
    TriggerAddCondition(gg_trg_EasternOn_1, Condition(Trig_EasternOn_1_Conditions))
    TriggerAddAction(gg_trg_EasternOn_1, Trig_EasternOn_1_Actions)
end
--===========================================================================
-- Trigger: EasternOn Spell
--===========================================================================
function Trig_EasternOn_Spell_Actions()
    udg_Continents[1]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UM'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UB'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_EasternOn_Spell()
    gg_trg_EasternOn_Spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EasternOn_Spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_EasternOn_Spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UB') then return end
        Trig_EasternOn_Spell_Actions()
    end)
end
--===========================================================================
-- Trigger: EasternOn Spell Off
--===========================================================================
function Trig_EasternOn_Spell_Off_Actions()
    udg_Continents[1]=0
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UB'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UM'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_EasternOn_Spell_Off()
    gg_trg_EasternOn_Spell_Off=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EasternOn_Spell_Off, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_EasternOn_Spell_Off, function()
        if GetSpellAbilityId() ~= FourCC('A0UM') then return end
        Trig_EasternOn_Spell_Off_Actions()
    end)
end
--===========================================================================
-- Trigger: EasternOn Set
--===========================================================================
function Trig_EasternOn_Set_Actions()
    udg_Continents[1]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
end
--===========================================================================
function InitTrig_EasternOn_Set()
    gg_trg_EasternOn_Set=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_EasternOn_Set, Player(0), " .. ek", true)
    TriggerAddAction(gg_trg_EasternOn_Set, Trig_EasternOn_Set_Actions)
end
--===========================================================================
-- Trigger: KalimOn 2
--===========================================================================
function Trig_KalimOn_2_Conditions()
    if ( not ( udg_Continents[2] == 1 ) ) then
        return false
    end
    return true
end
function Trig_KalimOn_2_Func002001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_KalimOn_2_Func002A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_KalimOn_2_Func003001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_KalimOn_2_Func003A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_KalimOn_2_Actions()
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Kalim, Condition(Trig_KalimOn_2_Func002001002)), Trig_KalimOn_2_Func002A)
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Ankirag, Condition(Trig_KalimOn_2_Func003001002)), Trig_KalimOn_2_Func003A)
end
--===========================================================================
function InitTrig_KalimOn_2()
    gg_trg_KalimOn_2=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_KalimOn_2, udg_TimerToCont)
    TriggerAddCondition(gg_trg_KalimOn_2, Condition(Trig_KalimOn_2_Conditions))
    TriggerAddAction(gg_trg_KalimOn_2, Trig_KalimOn_2_Actions)
end
--===========================================================================
-- Trigger: KalimOn 2 Spell
--===========================================================================
function Trig_KalimOn_2_Spell_Actions()
    udg_Continents[2]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UN'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UC'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_KalimOn_2_Spell()
    gg_trg_KalimOn_2_Spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KalimOn_2_Spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_KalimOn_2_Spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UC') then return end
        Trig_KalimOn_2_Spell_Actions()
    end)
end
--===========================================================================
-- Trigger: KalimOn 2 Spell off
--===========================================================================
function Trig_KalimOn_2_Spell_off_Actions()
    udg_Continents[2]=0
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UC'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UN'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_KalimOn_2_Spell_off()
    gg_trg_KalimOn_2_Spell_off=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KalimOn_2_Spell_off, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_KalimOn_2_Spell_off, function()
        if GetSpellAbilityId() ~= FourCC('A0UN') then return end
        Trig_KalimOn_2_Spell_off_Actions()
    end)
end
--===========================================================================
-- Trigger: KalimOn 2 set
--===========================================================================
function Trig_KalimOn_2_set_Actions()
    udg_Continents[2]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
end
--===========================================================================
function InitTrig_KalimOn_2_set()
    gg_trg_KalimOn_2_set=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_KalimOn_2_set, Player(0), " .. ka", true)
    TriggerAddAction(gg_trg_KalimOn_2_set, Trig_KalimOn_2_set_Actions)
end
--===========================================================================
-- Trigger: Outland 3
--===========================================================================
function Trig_Outland_3_Conditions()
    if ( not ( udg_Continents[3] == 1 ) ) then
        return false
    end
    return true
end
function Trig_Outland_3_Func002001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_Outland_3_Func002A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_Outland_3_Actions()
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Outland, Condition(Trig_Outland_3_Func002001002)), Trig_Outland_3_Func002A)
end
--===========================================================================
function InitTrig_Outland_3()
    gg_trg_Outland_3=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Outland_3, udg_TimerToCont)
    TriggerAddCondition(gg_trg_Outland_3, Condition(Trig_Outland_3_Conditions))
    TriggerAddAction(gg_trg_Outland_3, Trig_Outland_3_Actions)
end
--===========================================================================
-- Trigger: Outland 3 spell
--===========================================================================
function Trig_Outland_3_spell_Actions()
    udg_Continents[3]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UO'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UD'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Outland_3_spell()
    gg_trg_Outland_3_spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Outland_3_spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Outland_3_spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UD') then return end
        Trig_Outland_3_spell_Actions()
    end)
end
--===========================================================================
-- Trigger: Outland 3 spell off
--===========================================================================
function Trig_Outland_3_spell_off_Actions()
    udg_Continents[3]=0
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitRemoveAbilityBJ(FourCC('A0UO'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A0UD'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Outland_3_spell_off()
    gg_trg_Outland_3_spell_off=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Outland_3_spell_off, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Outland_3_spell_off, function()
        if GetSpellAbilityId() ~= FourCC('A0UO') then return end
        Trig_Outland_3_spell_off_Actions()
    end)
end
--===========================================================================
-- Trigger: Outland 3 set
--===========================================================================
function Trig_Outland_3_set_Actions()
    udg_Continents[3]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
end
--===========================================================================
function InitTrig_Outland_3_set()
    gg_trg_Outland_3_set=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Outland_3_set, Player(0), " .. ot", true)
    TriggerAddAction(gg_trg_Outland_3_set, Trig_Outland_3_set_Actions)
end
--===========================================================================
-- Trigger: NordOn 4
--===========================================================================
function Trig_NordOn_4_Conditions()
    if ( not ( udg_Continents[4] == 1 ) ) then
        return false
    end
    return true
end
function Trig_NordOn_4_Func002001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_NordOn_4_Func002A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_NordOn_4_Func003001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_NordOn_4_Func003A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_NordOn_4_Actions()
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Nord, Condition(Trig_NordOn_4_Func002001002)), Trig_NordOn_4_Func002A)
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Azgel, Condition(Trig_NordOn_4_Func003001002)), Trig_NordOn_4_Func003A)
end
--===========================================================================
function InitTrig_NordOn_4()
    gg_trg_NordOn_4=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_NordOn_4, udg_TimerToCont)
    TriggerAddCondition(gg_trg_NordOn_4, Condition(Trig_NordOn_4_Conditions))
    TriggerAddAction(gg_trg_NordOn_4, Trig_NordOn_4_Actions)
end
--===========================================================================
-- Trigger: NordOn 4 spell
--===========================================================================
function Trig_NordOn_4_spell_Actions()
    udg_Continents[4]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitRemoveAbilityBJ(FourCC('A0UE'), GetTriggerUnit())
    UnitAddAbilityBJ(FourCC('A0UP'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_NordOn_4_spell()
    gg_trg_NordOn_4_spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NordOn_4_spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_NordOn_4_spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UE') then return end
        Trig_NordOn_4_spell_Actions()
    end)
end
--===========================================================================
-- Trigger: NordOn 4 spell off
--===========================================================================
function Trig_NordOn_4_spell_off_Actions()
    udg_Continents[4]=0
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UE'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UP'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_NordOn_4_spell_off()
    gg_trg_NordOn_4_spell_off=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NordOn_4_spell_off, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_NordOn_4_spell_off, function()
        if GetSpellAbilityId() ~= FourCC('A0UP') then return end
        Trig_NordOn_4_spell_off_Actions()
    end)
end
--===========================================================================
-- Trigger: NordOn 4 set
--===========================================================================
function Trig_NordOn_4_set_Actions()
    udg_Continents[4]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
end
--===========================================================================
function InitTrig_NordOn_4_set()
    gg_trg_NordOn_4_set=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_NordOn_4_set, Player(0), " .. nd", true)
    TriggerAddAction(gg_trg_NordOn_4_set, Trig_NordOn_4_set_Actions)
end
--===========================================================================
-- Trigger: Pandaria 5
--===========================================================================
function Trig_Pandaria_5_Conditions()
    if ( not ( udg_Continents[5] == 1 ) ) then
        return false
    end
    return true
end
function Trig_Pandaria_5_Func002001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_Pandaria_5_Func002A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_Pandaria_5_Actions()
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Pandaria, Condition(Trig_Pandaria_5_Func002001002)), Trig_Pandaria_5_Func002A)
end
--===========================================================================
function InitTrig_Pandaria_5()
    gg_trg_Pandaria_5=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Pandaria_5, udg_TimerToCont)
    TriggerAddCondition(gg_trg_Pandaria_5, Condition(Trig_Pandaria_5_Conditions))
    TriggerAddAction(gg_trg_Pandaria_5, Trig_Pandaria_5_Actions)
end
--===========================================================================
-- Trigger: Pandaria 5 spell
--===========================================================================
function Trig_Pandaria_5_spell_Actions()
    udg_Continents[5]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UQ'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UF'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Pandaria_5_spell()
    gg_trg_Pandaria_5_spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pandaria_5_spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Pandaria_5_spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UF') then return end
        Trig_Pandaria_5_spell_Actions()
    end)
end
--===========================================================================
-- Trigger: Pandaria 5 spell off
--===========================================================================
function Trig_Pandaria_5_spell_off_Actions()
    udg_Continents[5]=0
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UF'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UQ'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Pandaria_5_spell_off()
    gg_trg_Pandaria_5_spell_off=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pandaria_5_spell_off, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Pandaria_5_spell_off, function()
        if GetSpellAbilityId() ~= FourCC('A0UQ') then return end
        Trig_Pandaria_5_spell_off_Actions()
    end)
end
--===========================================================================
-- Trigger: Pandaria 5 set
--===========================================================================
function Trig_Pandaria_5_set_Actions()
    udg_Continents[5]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
end
--===========================================================================
function InitTrig_Pandaria_5_set()
    gg_trg_Pandaria_5_set=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Pandaria_5_set, Player(0), " .. pd", true)
    TriggerAddAction(gg_trg_Pandaria_5_set, Trig_Pandaria_5_set_Actions)
end
--===========================================================================
-- Trigger: Argus 6
--===========================================================================
function Trig_Argus_6_Conditions()
    if ( not ( udg_Continents[6] == 1 ) ) then
        return false
    end
    return true
end
function Trig_Argus_6_Func002001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_Argus_6_Func002A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_Argus_6_Actions()
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Argus, Condition(Trig_Argus_6_Func002001002)), Trig_Argus_6_Func002A)
end
--===========================================================================
function InitTrig_Argus_6()
    gg_trg_Argus_6=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Argus_6, udg_TimerToCont)
    TriggerAddCondition(gg_trg_Argus_6, Condition(Trig_Argus_6_Conditions))
    TriggerAddAction(gg_trg_Argus_6, Trig_Argus_6_Actions)
end
--===========================================================================
-- Trigger: Argus 6 spell
--===========================================================================
function Trig_Argus_6_spell_Actions()
    udg_Continents[6]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UR'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UH'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Argus_6_spell()
    gg_trg_Argus_6_spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Argus_6_spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Argus_6_spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UH') then return end
        Trig_Argus_6_spell_Actions()
    end)
end
--===========================================================================
-- Trigger: Argus 6 spell off
--===========================================================================
function Trig_Argus_6_spell_off_Actions()
    udg_Continents[6]=0
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UH'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UR'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_Argus_6_spell_off()
    gg_trg_Argus_6_spell_off=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Argus_6_spell_off, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Argus_6_spell_off, function()
        if GetSpellAbilityId() ~= FourCC('A0UR') then return end
        Trig_Argus_6_spell_off_Actions()
    end)
end
--===========================================================================
-- Trigger: Argus 6 set
--===========================================================================
function Trig_Argus_6_set_Actions()
    udg_Continents[6]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
end
--===========================================================================
function InitTrig_Argus_6_set()
    gg_trg_Argus_6_set=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Argus_6_set, Player(0), " .. ar", true)
    TriggerAddAction(gg_trg_Argus_6_set, Trig_Argus_6_set_Actions)
end
--===========================================================================
-- Trigger: BrokenIsled 7
--===========================================================================
function Trig_BrokenIsled_7_Conditions()
    if ( not ( udg_Continents[7] == 1 ) ) then
        return false
    end
    return true
end
function Trig_BrokenIsled_7_Func002001002()
    return ( GetUnitAbilityLevelSwapped(FourCC('Awrp'), GetFilterUnit()) >= 1 )
end
function Trig_BrokenIsled_7_Func002A()
    WaygateActivateBJ(true, GetEnumUnit())
end
function Trig_BrokenIsled_7_Actions()
    ForGroupBJ(GetUnitsInRectMatching(gg_rct_Broken_Island, Condition(Trig_BrokenIsled_7_Func002001002)), Trig_BrokenIsled_7_Func002A)
end
--===========================================================================
function InitTrig_BrokenIsled_7()
    gg_trg_BrokenIsled_7=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_BrokenIsled_7, udg_TimerToCont)
    TriggerAddCondition(gg_trg_BrokenIsled_7, Condition(Trig_BrokenIsled_7_Conditions))
    TriggerAddAction(gg_trg_BrokenIsled_7, Trig_BrokenIsled_7_Actions)
end
--===========================================================================
-- Trigger: BrokenIsled 7 spell
--===========================================================================
function Trig_BrokenIsled_7_spell_Actions()
    udg_Continents[7]=1
    udg_Continents[0]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0US'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0UG'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_BrokenIsled_7_spell()
    gg_trg_BrokenIsled_7_spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BrokenIsled_7_spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_BrokenIsled_7_spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UG') then return end
        Trig_BrokenIsled_7_spell_Actions()
    end)
end
--===========================================================================
-- Trigger: BrokenIsled 7 spell off
--===========================================================================
function Trig_BrokenIsled_7_spell_off_Actions()
    udg_Continents[7]=0
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
    UnitAddAbilityBJ(FourCC('A0UG'), GetTriggerUnit())
    UnitRemoveAbilityBJ(FourCC('A0US'), GetTriggerUnit())
end
--===========================================================================
function InitTrig_BrokenIsled_7_spell_off()
    gg_trg_BrokenIsled_7_spell_off=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BrokenIsled_7_spell_off, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_BrokenIsled_7_spell_off, function()
        if GetSpellAbilityId() ~= FourCC('A0US') then return end
        Trig_BrokenIsled_7_spell_off_Actions()
    end)
end
--===========================================================================
-- Trigger: BrokenIsled 7 set
--===========================================================================
function Trig_BrokenIsled_7_set_Actions()
    udg_Continents[7]=1
    DisplayTextToForce(GetPlayersAll(), ( "cffffff00r" ))
end
--===========================================================================
function InitTrig_BrokenIsled_7_set()
    gg_trg_BrokenIsled_7_set=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_BrokenIsled_7_set, Player(0), " .. bi", true)
    TriggerAddAction(gg_trg_BrokenIsled_7_set, Trig_BrokenIsled_7_set_Actions)
end
--===========================================================================
-- Trigger: Standart
--===========================================================================
function Trig_Standart_Actions()
    udg_SET_VISIBLE_MODE=0
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19654")
end
--===========================================================================
function InitTrig_Standart()
    gg_trg_Standart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Standart, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Standart, function()
        if GetSpellAbilityId() ~= FourCC('A0UT') then return end
        Trig_Standart_Actions()
    end)
end
--===========================================================================
-- Trigger: DarkMode Spell
--===========================================================================
function Trig_DarkMode_Spell_Actions()
    udg_SET_VISIBLE_MODE=1
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19693")
end
--===========================================================================
function InitTrig_DarkMode_Spell()
    gg_trg_DarkMode_Spell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DarkMode_Spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_DarkMode_Spell, function()
        if GetSpellAbilityId() ~= FourCC('A0UL') then return end
        Trig_DarkMode_Spell_Actions()
    end)
end
--===========================================================================
-- Trigger: OpenModeSpell
--===========================================================================
function Trig_OpenModeSpell_Actions()
    udg_SET_VISIBLE_MODE=2
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_25625")
end
--===========================================================================
function InitTrig_OpenModeSpell()
    gg_trg_OpenModeSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OpenModeSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_OpenModeSpell, function()
        if GetSpellAbilityId() ~= FourCC('A131') then return end
        Trig_OpenModeSpell_Actions()
    end)
end
--===========================================================================
-- Trigger: StartDarkMode
--===========================================================================
function Trig_StartDarkMode_Conditions()
    if ( not ( udg_SET_VISIBLE_MODE == 1 ) ) then
        return false
    end
    return true
end
function Trig_StartDarkMode_Func006A()
    FogModifierStop(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_MASKED, GetPlayableMapRect())
end
function Trig_StartDarkMode_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20065")
    TriggerSleepAction(30.00)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20066")
    TriggerSleepAction(30.00)
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20067")
    ForForce(udg_AllPlayers, Trig_StartDarkMode_Func006A)
end
--===========================================================================
function InitTrig_StartDarkMode()
    gg_trg_StartDarkMode=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_StartDarkMode, udg_LobbyTime)
    TriggerAddCondition(gg_trg_StartDarkMode, Condition(Trig_StartDarkMode_Conditions))
    TriggerAddAction(gg_trg_StartDarkMode, Trig_StartDarkMode_Actions)
end
--===========================================================================
-- Trigger: StartOpenMode
--===========================================================================
function Trig_StartOpenMode_Conditions()
    if ( not ( udg_SET_VISIBLE_MODE == 2 ) ) then
        return false
    end
    return true
end
function Trig_StartOpenMode_Func002A()
    FogModifierStop(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
end
function Trig_StartOpenMode_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_7375")
    ForForce(udg_AllPlayers, Trig_StartOpenMode_Func002A)
end
--===========================================================================
function InitTrig_StartOpenMode()
    gg_trg_StartOpenMode=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_StartOpenMode, udg_LobbyTime)
    TriggerAddCondition(gg_trg_StartOpenMode, Condition(Trig_StartOpenMode_Conditions))
    TriggerAddAction(gg_trg_StartOpenMode, Trig_StartOpenMode_Actions)
end
--===========================================================================
-- Trigger: StartDarkMode Command
--===========================================================================
function Trig_StartDarkMode_Command_Func003A()
    FogModifierStop(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_MASKED, GetPlayableMapRect())
end
function Trig_StartDarkMode_Command_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20055")
    ForForce(udg_AllPlayers, Trig_StartDarkMode_Command_Func003A)
end
--===========================================================================
function InitTrig_StartDarkMode_Command()
    gg_trg_StartDarkMode_Command=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_StartDarkMode_Command, Player(0), " - dmon", true)
    TriggerAddAction(gg_trg_StartDarkMode_Command, Trig_StartDarkMode_Command_Actions)
end
--===========================================================================
-- Trigger: OfDarkModeCommand
--===========================================================================
function Trig_OfDarkModeCommand_Func002A()
    FogModifierStop(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
end
function Trig_OfDarkModeCommand_Actions()
    ForForce(udg_AllPlayers, Trig_OfDarkModeCommand_Func002A)
end
--===========================================================================
function InitTrig_OfDarkModeCommand()
    gg_trg_OfDarkModeCommand=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_OfDarkModeCommand, Player(0), " - dmoff", true)
    TriggerAddAction(gg_trg_OfDarkModeCommand, Trig_OfDarkModeCommand_Actions)
end
--===========================================================================
-- Trigger: StartAlly
--===========================================================================
function WritePlayerName()
    DisplayTextToForce(udg_AllPlayers, "" + GetPlayerName(GetEnumPlayer()))
end
function Trig_StartAlly_Actions()
    local p= GetTriggerPlayer()
    local AllyCount= 0
    ForceEnumAllies(gForce, p, nil)
    AllyCount=CountPlayersInForceBJ(gForce)
    if DipMode == 0 then
        --?????????? ? ??????????
        if AllyCount > 1 then
            DisplayTextToForce(udg_AllPlayers, "" + GetPlayerName(p) + " not ")
            ForForce(gForce, WritePlayerName)
            
        end
    else
        if AllyCount > DipMode then
            ClearAllies(p)
            DisplayTextToForce(udg_AllPlayers, "" + GetPlayerName(p) + "")
            
        end
    
    end
    AllyTax[GetPlayerId(p)]=0.1 * AllyCount
    ForceClear(gForce)
end
--===========================================================================
function InitTrig_StartAlly()
    local i= 0
    gg_trg_StartAlly=CreateTrigger()
    while true do
        if i > 23 then break end
        TriggerRegisterPlayerEventAllianceChanged(gg_trg_StartAlly, Player(i))
        i=i + 1
    end
    
    --call TriggerAddCondition( gg_trg_StartAlly, Condition( function Trig_StartAlly_Conditions ) )
    TriggerAddAction(gg_trg_StartAlly, Trig_StartAlly_Actions)
end
--===========================================================================
-- Trigger: NoDipFFA
--===========================================================================
function Trig_NoDipFFA_Actions()
    DipMode=1
    DisplayTextToForce(GetPlayersAll(), "..")
   
end
--===========================================================================
function InitTrig_NoDipFFA()
    gg_trg_NoDipFFA=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NoDipFFA, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_NoDipFFA, function()
        if GetSpellAbilityId() ~= FourCC('A1KR') then return end
        Trig_NoDipFFA_Actions()
    end)
end
--===========================================================================
-- Trigger: Dip2
--===========================================================================
function Trig_Dip2_Actions()
    DipMode=2
    DisplayTextToForce(GetPlayersAll(), "2")
end
--===========================================================================
function InitTrig_Dip2()
    gg_trg_Dip2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dip2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dip2, function()
        if GetSpellAbilityId() ~= FourCC('A1KS') then return end
        Trig_Dip2_Actions()
    end)
end
--===========================================================================
-- Trigger: Dip3
--===========================================================================
function Trig_Dip3_Actions()
    DipMode=3
    DisplayTextToForce(GetPlayersAll(), "3")
end
--===========================================================================
function InitTrig_Dip3()
    gg_trg_Dip3=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Dip3, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Dip3, function()
        if GetSpellAbilityId() ~= FourCC('A1KT') then return end
        Trig_Dip3_Actions()
    end)
end
--===========================================================================
-- Trigger: FreeDip
--===========================================================================
function Trig_FreeDip_Actions()
    DipMode=0
    DisplayTextToForce(GetPlayersAll(), "")
end
--===========================================================================
function InitTrig_FreeDip()
    gg_trg_FreeDip=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FreeDip, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FreeDip, function()
        if GetSpellAbilityId() ~= FourCC('A1KQ') then return end
        Trig_FreeDip_Actions()
    end)
end
--===========================================================================
-- Trigger: DipStart
--===========================================================================
function ClearPlayerEach()
    ClearOldAllies(GetEnumPlayer())
end
function Trig_DipStart_Actions()
    
   
    
    --FFA
    if DipMode == 1 then
        SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, true)
        SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, true)
        SetMapFlag(MAP_LOCK_RESOURCE_TRADING, true)
        ForForce(udg_AllPlayers2, ClearPlayerEach)
    -- FREE
    else
        SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
        SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
        SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
        --if DipMode==0 then
           
           
        --endif
    
    end
end
--===========================================================================
function InitTrig_DipStart()
    gg_trg_DipStart=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_DipStart, udg_LobbyTime)
    TriggerAddAction(gg_trg_DipStart, Trig_DipStart_Actions)
end
--===========================================================================
-- Trigger: Income075
--===========================================================================
function Trig_Income075_Actions()
    IncomeMod=0.75
    DisplayTextToForce(GetPlayersAll(), "75")
end
--===========================================================================
function InitTrig_Income075()
    gg_trg_Income075=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Income075, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Income075, function()
        if GetSpellAbilityId() ~= FourCC('A1N6') then return end
        Trig_Income075_Actions()
    end)
end
--===========================================================================
-- Trigger: Income100
--===========================================================================
function Trig_Income100_Actions()
    IncomeMod=1
    DisplayTextToForce(GetPlayersAll(), "")
end
--===========================================================================
function InitTrig_Income100()
    gg_trg_Income100=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Income100, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Income100, function()
        if GetSpellAbilityId() ~= FourCC('A1N7') then return end
        Trig_Income100_Actions()
    end)
end
--===========================================================================
-- Trigger: StartTotalProductionCommon
--
-- ??? ?? ???????????????? ???????? ??????
--===========================================================================
function Trig_StartTotalProductionCommon_Actions()
    local i= 0
    TotalProduction=true
    
    while true do
        if i >= 23 then break end
        SetPlayerAbilityAvailable(Player(i), FourCC('A1KH'), true)
        i=i + 1
    end
end
--===========================================================================
function InitTrig_StartTotalProductionCommon()
    gg_trg_StartTotalProductionCommon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartTotalProductionCommon, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_StartTotalProductionCommon, function()
        if GetSpellAbilityId() ~= FourCC('A1KC') then return end
        Trig_StartTotalProductionCommon_Actions()
    end)
    
    
end
--===========================================================================
-- Trigger: StartTotalProductionPlayer
--
-- ??? ?? ???????????????? ???????? ??????
--===========================================================================
function Trig_StartTotalProductionPlayer_Actions()
    TotalProductionP[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]=true
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC('A1KI'), true)
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC('A1KH'), false)
end
--===========================================================================
function InitTrig_StartTotalProductionPlayer()
    local i= 0
    gg_trg_StartTotalProductionPlayer=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartTotalProductionPlayer, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_StartTotalProductionPlayer, function()
        if GetSpellAbilityId() ~= FourCC('A1KH') then return end
        Trig_StartTotalProductionPlayer_Actions()
    end)
    
    while true do
        if i == 23 then break end
        TotalProductionP[i]=false
        SetPlayerAbilityAvailable(Player(i), FourCC('A1KI'), false)
        SetPlayerAbilityAvailable(Player(i), FourCC('A1KH'), false)
        i=i + 1
    end
    
    
end
--===========================================================================
-- Trigger: EndTotalProductionPlayer
--
-- ??? ?? ???????????????? ???????? ??????
--===========================================================================
function Trig_EndTotalProductionPlayer_Actions()
    TotalProductionP[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]=false
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC('A1KH'), true)
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC('A1KI'), false)
end
--===========================================================================
function InitTrig_EndTotalProductionPlayer()
    
    gg_trg_EndTotalProductionPlayer=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_EndTotalProductionPlayer, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_EndTotalProductionPlayer, function()
        if GetSpellAbilityId() ~= FourCC('A1KI') then return end
        Trig_EndTotalProductionPlayer_Actions()
    end)
    
end
--===========================================================================
-- Trigger: TotalProductionTrain
--===========================================================================
function Trig_TotalProductionTrain_Conditions()
    return TotalProduction
end
function Trig_TotalProductionTrain_Actions()
    local u= GetTrainedUnit()
    local uh= GetHandleId(u)
    SaveInteger(Hash, S2I(I2S(uh) + "a"), 0, GetUnitTypeId(GetTriggerUnit())) --StringHash("lvl"),0)
    
    u=nil
    --call IssueTrainOrderByIdBJ( GetTriggerUnit(), GetUnitTypeId(GetTrainedUnit()) )
end
--===========================================================================
function InitTrig_TotalProductionTrain()
    gg_trg_TotalProductionTrain=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TotalProductionTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TotalProductionTrain, Condition(Trig_TotalProductionTrain_Conditions))
    TriggerAddAction(gg_trg_TotalProductionTrain, Trig_TotalProductionTrain_Actions)
end
--===========================================================================
-- Trigger: TotalProductionDeath
--===========================================================================
function Trig_TotalProductionDeath_Conditions()
    return TotalProductionP[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
function ThisId()
    return GetUnitTypeId(GetFilterUnit()) == udg_LocalInteger5
end
function Trig_TotalProductionDeath_Actions()
    local u= GetTriggerUnit()
    local uh= GetHandleId(u)
    local id= LoadInteger(Hash, S2I(I2S(uh) + "a"), 0)
    local p= GetOwningPlayer(u)
    local u2
    local g= CreateGroup()
    udg_LocalInteger5=id
    
    FlushChildHashtable(Hash, S2I(I2S(uh) + "a"))
    GroupEnumUnitsOfPlayer(g, p, b)
    u2=GroupPickRandomUnit(g)
    if u2 ~= nil then
        IssueImmediateOrderById(u2, GetUnitTypeId(u))
    end
    
    u=nil
    u2=nil
    DestroyGroup(g)
    DestroyBoolExpr(b)
    b=nil
    g=nil
end
--===========================================================================
function InitTrig_TotalProductionDeath()
    gg_trg_TotalProductionDeath=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TotalProductionDeath, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_TotalProductionDeath, Condition(Trig_TotalProductionDeath_Conditions))
    TriggerAddAction(gg_trg_TotalProductionDeath, Trig_TotalProductionDeath_Actions)
end
--===========================================================================
-- Trigger: Timer
--
-- ?????? ??????? ?????? ? ??????? ??????? ?? ???????????
--===========================================================================
function Trig_Timer_Func009Func001A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A0IQ'), GetEnumPlayer())
end
function Trig_Timer_Func009C()
    if ( not ( udg_GameMode == 0 ) ) then
        return false
    end
    return true
end
function Trig_Timer_Actions()
    udg_AllPlayers=GetPlayersAll()
    StartTimerBJ(udg_IncomeTimerSecond, true, I2R(udg_SET_TimerTime))
    CreateTimerDialogBJ(GetLastCreatedTimerBJ(), "TRIGSTR_4633")
    udg_TimerSecond=GetLastCreatedTimerDialogBJ()
    StartTimerBJ(udg_IncomeTimerFirst, false, 600.00)
    CreateTimerDialogBJ(GetLastCreatedTimerBJ(), "TRIGSTR_7397")
    udg_TimerToDis=GetLastCreatedTimerDialogBJ()
    if ( Trig_Timer_Func009C() ) then
        ForForce(udg_AllPlayers, Trig_Timer_Func009Func001A)
    else
    end
end
--===========================================================================
function InitTrig_Timer()
    gg_trg_Timer=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Timer, udg_LobbyTime)
    TriggerAddAction(gg_trg_Timer, Trig_Timer_Actions)
end
--===========================================================================
-- Trigger: ChangeTimerHost
--===========================================================================
function Trig_ChangeTimerHost_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_19902")
    udg_SET_TimerTime=S2I(SubStringBJ(GetEventPlayerChatString(), 7, 8))
    StartTimerBJ(udg_IncomeTimerSecond, true, I2R(udg_SET_TimerTime))
end
--===========================================================================
function InitTrig_ChangeTimerHost()
    gg_trg_ChangeTimerHost=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_ChangeTimerHost, Player(0), " - ", false)
    TriggerAddAction(gg_trg_ChangeTimerHost, Trig_ChangeTimerHost_Actions)
end
--===========================================================================
-- Trigger: DisIncomeStart
--
-- ??????? ?????????? ?????? ?? ???????? ???????? ??????? ???????????, ????????? ????? ??????? ?? ????.
--===========================================================================
function Trig_DisIncomeStart_Func002A()
    TimerDialogDisplayForPlayerBJ(false, udg_TimerToDis, GetEnumPlayer())
end
function Trig_DisIncomeStart_Actions()
    ForForce(udg_AllPlayers, Trig_DisIncomeStart_Func002A)
    TimerDialogDisplayBJ(false, udg_TimerToDis)
    DisOn=true
end
--===========================================================================
function InitTrig_DisIncomeStart()
