
--===========================================================================
-- Trigger: StartUlt
--===========================================================================
function Trig_StartUlt_Func002C()
    return (( GetUnitTypeId(GetTriggerUnit()) == FourCC('MIMH') )) and (( GetSpellAbilityId() == FourCC('MIM6') ))
end
function Trig_StartUlt_Conditions()
    return Trig_StartUlt_Func002C()
end
function Trig_StartUlt_Func001Func001C()
    return (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) >= 8000 )) and (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) >= 8000 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) < 2 )) and (( GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()) == 2 ))
end
function Trig_StartUlt_Func001C()
    return (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) >= 8000 )) and (( GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) >= 8000 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) < 1 )) and (( GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()) == 1 ))
end
function Trig_StartUlt_Actions()
    if Trig_StartUlt_Func001C() then
        SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) - 8000)
        SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) - 8000)
        UnitAddAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()))
        BlzUnitHideAbility(GetTriggerUnit(), FourCC('MIM4'), false)
        SetUnitAnimationWithRarity(GetTriggerUnit(), "Attackspell", RARITY_FREQUENT)
        PauseUnitBJ(true, GetTriggerUnit())
        TriggerSleepAction(50.00)
        PauseUnitBJ(false, GetTriggerUnit())
        IssueImmediateOrderBJ(GetTriggerUnit(), "stomp")
    else
        if Trig_StartUlt_Func001Func001C() then
            SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_GOLD) - 8000)
            SetPlayerStateBJ(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(GetTriggerPlayer(), PLAYER_STATE_RESOURCE_LUMBER) - 8000)
            UnitAddAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('MIM6'), GetTriggerUnit()))
            BlzUnitHideAbility(GetTriggerUnit(), FourCC('MIM4'), false)
            PauseUnitBJ(true, GetTriggerUnit())
            TriggerSleepAction(50.00)
            PauseUnitBJ(false, GetTriggerUnit())
            IssueImmediateOrderBJ(GetTriggerUnit(), "stomp")
        else
            DoNothing()
        end
    end
end
--===========================================================================
function InitTrig_StartUlt()
    gg_trg_StartUlt=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_StartUlt, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_StartUlt, Condition(Trig_StartUlt_Conditions))
    TriggerAddAction(gg_trg_StartUlt, Trig_StartUlt_Actions)
end
--===========================================================================
-- Trigger: UltSummon
--===========================================================================
function Trig_UltSummon_Func003C()
    return (( GetUnitTypeId(GetTriggerUnit()) == FourCC('MIMH') )) and (( GetSpellAbilityId() == FourCC('MIM4') ))
end
function Trig_UltSummon_Conditions()
    return Trig_UltSummon_Func003C()
end
function Trig_UltSummon_Func002Func001C()
    return (( GetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit()) == 2 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) < 2 ))
end
function Trig_UltSummon_Func002C()
    return (( GetUnitAbilityLevelSwapped(FourCC('MIM4'), GetTriggerUnit()) == 1 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('mim1'), GetTriggerPlayer()) == 0 ))
end
function Trig_UltSummon_Actions()
    if Trig_UltSummon_Func002C() then
        CreateNUnitsAtLoc(1, FourCC('mim1'), GetOwningPlayer(GetTriggerUnit()), GetUnitLoc(GetTriggerUnit()), bj_UNIT_FACING)
        SetUnitAnimation(GetLastCreatedUnit(), "birth")
        UnitRemoveAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
    else
        if Trig_UltSummon_Func002Func001C() then
            CreateNUnitsAtLoc(1, FourCC('mim1'), GetOwningPlayer(GetTriggerUnit()), GetUnitLoc(GetTriggerUnit()), bj_UNIT_FACING)
            SetUnitAnimation(GetLastCreatedUnit(), "birth")
            UnitRemoveAbilityBJ(FourCC('MIM4'), GetTriggerUnit())
        else
            DoNothing()
        end
    end
end
--===========================================================================
function InitTrig_UltSummon()
    gg_trg_UltSummon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UltSummon, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_UltSummon, Condition(Trig_UltSummon_Conditions))
    TriggerAddAction(gg_trg_UltSummon, Trig_UltSummon_Actions)
end
--===========================================================================
-- Trigger: MassHEX
--===========================================================================
function Trig_MassHEX_Func001A()
    CreateNUnitsAtLoc(1, FourCC('repD'), GetTriggerPlayer(), GetUnitLoc(GetEnumUnit()), bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('VLJ5'), GetLastCreatedUnit())
    SetUnitAbilityLevelSwapped(FourCC('VLJ5'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('VLJ1'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "hex", GetEnumUnit())
end
function Trig_MassHEX_Actions()
    ForGroupBJ(GetUnitsInRangeOfLocAll(300.00, GetSpellTargetLoc()), Trig_MassHEX_Func001A)
end
--===========================================================================
function InitTrig_MassHEX()
    gg_trg_MassHEX=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassHEX, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassHEX, function()
        if GetSpellAbilityId() ~= FourCC('VLJ1') then return end
        Trig_MassHEX_Actions()
    end)
end
--===========================================================================
-- Trigger: SomeVoljinSpell
--===========================================================================
function Trig_SomeVoljinSpell_Actions()
    UnitAddAbilityBJ(FourCC('A0OR'), GetTriggerUnit())
    BlzUnitHideAbility(GetTriggerUnit(), FourCC('A0OR'), true)
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A0OR') , 15)
end
--===========================================================================
function InitTrig_SomeVoljinSpell()
    gg_trg_SomeVoljinSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SomeVoljinSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SomeVoljinSpell, function()
        if GetSpellAbilityId() ~= FourCC('VLJ4') then return end
        Trig_SomeVoljinSpell_Actions()
    end)
end
--===========================================================================
-- Trigger: Kill
--===========================================================================
function Trig_Kill_Func002A()
    local id= GetUnitTypeId(GetEnumUnit())
    if not IsUnitInGroup(GetEnumUnit(), udg_ZahvatBuildings) and GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() and not IsUnitInGroup(GetEnumUnit(), udg_StolicaGroups) and id ~= FourCC('e00C') and id ~= FourCC('e00D') then
        KillUnit(GetEnumUnit())
    else
        if IsUnitInGroup(GetEnumUnit(), udg_StolicaGroups) and GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() then
            
            if udg_GameMode == 2 then
                HandleVassalization(GetEnumUnit(), GetTriggerPlayer())
            else
                KillUnit(GetEnumUnit())
                udg_LocalPlayer=GetTriggerPlayer()
                ConditionalTriggerExecute(gg_trg_StolicaKill)
            end
        end
    end
end
function Trig_Kill_Actions()
    local p= GetTriggerPlayer()
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, nil)
    ForGroup(g, Trig_Kill_Func002A)
    DestroyGroup(g)
    g=nil
    p=nil
end
--===========================================================================
function InitTrig_Kill()
    gg_trg_Kill=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(0), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(1), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(2), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(3), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(4), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(5), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(6), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(7), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(8), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(9), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(10), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(11), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(12), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(13), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(14), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(15), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(16), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(17), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(18), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(19), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(20), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(21), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(22), " - kill", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Kill, Player(23), " - kill", true)
    TriggerAddAction(gg_trg_Kill, Trig_Kill_Actions)
end
--===========================================================================
-- Trigger: Rep
--===========================================================================
function RepConditions()
    if GetOwningPlayer(GetEnumUnit()) == GetTriggerPlayer() and not IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE) then
        
        ReplaceUnit2(GetEnumUnit() , GetUnitTypeId(GetEnumUnit()) , bj_UNIT_STATE_METHOD_RELATIVE)
    end
end
function Trig_Rep_Actions()
    local p= GetTriggerPlayer()
    local g= CreateGroup()
    GroupEnumUnitsSelected(g, p, nil)
    ForGroup(g, RepConditions)
    DestroyGroup(g)
    g=nil
    p=nil
end
--===========================================================================
function InitTrig_Rep()
    gg_trg_Rep=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(0), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(1), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(2), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(3), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(4), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(5), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(6), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(7), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(8), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(9), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(10), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(11), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(12), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(13), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(14), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(15), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(16), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(17), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(18), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(19), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(20), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(21), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(22), " - rep", true)
    TriggerRegisterPlayerChatEvent(gg_trg_Rep, Player(23), " - rep", true)
    TriggerAddAction(gg_trg_Rep, Trig_Rep_Actions)
end
--===========================================================================
-- Trigger: StolicaKill
--===========================================================================
function Trig_StolicaKill_Actions()
    -- ??????? ???????? ??????????. ?? ????????!
end
--===========================================================================
function InitTrig_StolicaKill()
    gg_trg_StolicaKill=CreateTrigger()
    TriggerAddAction(gg_trg_StolicaKill, Trig_StolicaKill_Actions)
end
--===========================================================================
-- Trigger: Camera command O
--===========================================================================
function Trig_Camera_command_O_Actions()
    udg_wawt=S2R(SubStringBJ(GetEventPlayerChatString(), 6, 9))
    SetCameraFieldForPlayer(GetTriggerPlayer(), CAMERA_FIELD_TARGET_DISTANCE, udg_wawt, 1.00)
end
--===========================================================================
function InitTrig_Camera_command_O()
    gg_trg_Camera_command_O=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(0), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(1), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(2), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(3), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(4), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(5), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(6), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(7), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(8), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(9), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(10), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(11), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(12), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(13), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(14), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(15), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(16), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(17), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(18), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(19), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(20), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(21), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(22), " - cam", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Camera_command_O, Player(23), " - cam", false)
    TriggerAddAction(gg_trg_Camera_command_O, Trig_Camera_command_O_Actions)
end
--===========================================================================
-- Trigger: Name command O
--===========================================================================
function Trig_Name_command_O_Conditions()
    return SubStringBJ(GetEventPlayerChatString(), 1, 6) == " - name"
end
function Trig_Name_command_O_Actions()
    local i= GetPlayerId(GetTriggerPlayer())
    local ownerIndex
    udg_LocalText2=GetEventPlayerChatString()
    udg_LocalText2=SubStringBJ(udg_LocalText2, 7, 50)
    SetPlayerName(GetTriggerPlayer(), udg_LocalText2)
    ownerIndex=EnsureMultiboardPlayerRow(i)
    udg_LocalText2=I2S(GetConvertedPlayerId(GetTriggerPlayer())) .. "." .. udg_LocalText2
    if ownerIndex ~= nil then
        MultiboardSetItemValue(MultiboardItem[ownerIndex * 2 + 0], udg_LocalText2)
    end
    i=0
end
--===========================================================================
function InitTrig_Name_command_O()
    gg_trg_Name_command_O=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(0), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(1), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(2), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(3), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(4), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(5), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(6), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(7), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(8), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(9), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(10), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(11), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(12), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(13), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(14), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(15), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(16), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(17), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(18), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(20), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(19), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(21), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(22), " - name", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Name_command_O, Player(23), " - name", false)
    TriggerAddCondition(gg_trg_Name_command_O, Condition(Trig_Name_command_O_Conditions))
    TriggerAddAction(gg_trg_Name_command_O, Trig_Name_command_O_Actions)
end
--===========================================================================
-- Trigger: UName command
--===========================================================================
function Trig_UName_command_Conditions()
    return SubStringBJ(GetEventPlayerChatString(), 1, 7) == " - uname"
end
function Trig_UName_command_Actions()
    local i= GetPlayerId(GetTriggerPlayer())
    local u
    local g= CreateGroup()
    udg_LocalText2=GetEventPlayerChatString()
    udg_LocalText2=SubStringBJ(udg_LocalText2, 7, 50)
    
    SyncSelections()
    GroupEnumUnitsSelected(g, GetTriggerPlayer(), nil)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        BlzSetUnitName(u, udg_LocalText2)
        
        GroupRemoveUnit(g, u)
    
    end
    
    
    
    DestroyGroup(g)
    g=nil
    u=nil
end
--===========================================================================
function InitTrig_UName_command()
    local i= 0
    gg_trg_UName_command=CreateTrigger()
    
    while true do
        if i > 23 then break end
        TriggerRegisterPlayerChatEvent(gg_trg_UName_command, Player(i), " - uname", false)
    
        
        
        
        i=i + 1
    end
    TriggerAddCondition(gg_trg_UName_command, Condition(Trig_UName_command_Conditions))
    TriggerAddAction(gg_trg_UName_command, Trig_UName_command_Actions)
end
--===========================================================================
-- Trigger: SecondChance
--===========================================================================
function Trig_SecondChance_Func003Func007001002()
    return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end
function Trig_SecondChance_Func003Func007A()
    local u= GetEnumUnit()
    local p= GetOwningPlayer(u)
    local id= GetUnitTypeId(u)
    RemoveUnit(u)
    SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
    p=nil
    u=nil
end
function Trig_SecondChance_Func003Func008C()
    if not ( udg_LocalInteger >= 1 ) then
        return false
    end
    if not ( udg_LocalInteger <= 24 ) then
        return false
    end
   
    if IsPlayerInForce(ConvertedPlayer(udg_LocalInteger), Observers) then
        DisplayTimedTextToForce(GetPlayersAll(), 5.00, ( "" .. GetPlayerName(GetTriggerPlayer()) ) .. ( "" .. ( GetPlayerName(ConvertedPlayer(udg_LocalInteger)) .. " not " ) ))
        return false
    end
    return true
end
function Trig_SecondChance_Func003C()
    return Trig_SecondChance_Func003Func008C()
end
function Trig_SecondChance_Actions()
    local t= SecondChance[GetPlayerId(ConvertedPlayer(udg_LocalInteger))]
    udg_LocalText2=SubStringBJ(GetEventPlayerChatString(), 12, 13)
    udg_LocalInteger=S2I(udg_LocalText2)
    ProbeLogWrite("[CHAT] -raceselect target=" .. tostring(udg_LocalInteger))
    if Trig_SecondChance_Func003C() then
        udg_LocalPosition2=StartLoc[GetRandomInt(0, StartLocCount - 1)] -- INLINED!!
        DisplayTimedTextToForce(GetPlayersAll(), 5.00, "???? " .. GetPlayerName(GetTriggerPlayer()) .. " ??? ?????? " .. GetPlayerName(ConvertedPlayer(udg_LocalInteger)) .. " ?????? ????!")
        DisplayTimedTextToPlayer(ConvertedPlayer(udg_LocalInteger), 0, 0, 15.00, "? ??? ???? 15 ????? ?? ??, ????? ????????? ???????!")
        CreateNUnitsAtLoc(1, FourCC('h0HJ'), ConvertedPlayer(udg_LocalInteger), udg_LocalPosition2, bj_UNIT_FACING)
        SetPlayerStateBJ(ConvertedPlayer(udg_LocalInteger), PLAYER_STATE_RESOURCE_GOLD, 5000)
        SetPlayerStateBJ(ConvertedPlayer(udg_LocalInteger), PLAYER_STATE_RESOURCE_LUMBER, 5000)
        
        ForGroupBJ(GetUnitsOfPlayerMatching(ConvertedPlayer(udg_LocalInteger), Condition(Trig_SecondChance_Func003Func007001002)), Trig_SecondChance_Func003Func007A)
    
        if udg_GameMode == 1 or udg_GameMode == 2 then
            local p = ConvertedPlayer(udg_LocalInteger)
            t=CreateTimer()
            SecondChance[GetPlayerId(p)]=t
            TimerStart(t, 60 * 15, false, function()
                CheckAndCreateCapital(p)
                DestroyTimer(t)
            end)
        end
    end
    t=nil
end
--===========================================================================
function InitTrig_SecondChance()
    gg_trg_SecondChance=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_SecondChance, Player(0), "-raceselect", false)
    TriggerAddAction(gg_trg_SecondChance, Trig_SecondChance_Actions)
end
function BridgeRaceSelect(target_index)
    local target_player = ConvertedPlayer(target_index)
    local t = SecondChance[GetPlayerId(target_player)]
    udg_LocalPosition2=StartLoc[GetRandomInt(0, StartLocCount - 1)]
    DisplayTimedTextToForce(GetPlayersAll(), 5.00, "Bridge gave player " .. GetPlayerName(target_player) .. " race selection")
    DisplayTimedTextToPlayer(target_player, 0, 0, 15.00, "You have 15 minutes to place your capital")
    CreateNUnitsAtLoc(1, FourCC('h0HJ'), target_player, udg_LocalPosition2, bj_UNIT_FACING)
    SetPlayerStateBJ(target_player, PLAYER_STATE_RESOURCE_GOLD, 5000)
    SetPlayerStateBJ(target_player, PLAYER_STATE_RESOURCE_LUMBER, 5000)
    udg_LocalInteger = target_index
    ForGroupBJ(GetUnitsOfPlayerMatching(target_player, Condition(Trig_SecondChance_Func003Func007001002)), Trig_SecondChance_Func003Func007A)
    if udg_GameMode == 1 or udg_GameMode == 2 then
        t=CreateTimer()
        SecondChance[GetPlayerId(target_player)]=t
        TimerStart(t, 60 * 15, false, function()
            CheckAndCreateCapital(target_player)
            DestroyTimer(t)
        end)
    end
    ProbeLogWrite("[BRIDGE] race_select target=" .. tostring(target_index))
    target_player = nil
    t = nil
end
--===========================================================================
-- Trigger: GG
--===========================================================================
function Trig_GG_Func004A()
    local u= GetEnumUnit()
    local id= GetUnitTypeId(u)
    local p= GetOwningPlayer(u)
    if IsUnitInGroup(u, udg_ZahvatBuildings) then
        SetUnitOwner(u, Player(25), true)
    else
        KillUnit(u)
        RemoveUnit(u)
        if IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO) then
            SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
        end
    end
    u=nil
    p=nil
end
function Trig_GG_Actions()
    --local integer pi = GetPlayerId(GetTriggerPlayer())
    DisplayTextToForce(udg_AllPlayers, GetPlayerName(GetTriggerPlayer()) .. "cffff0000 - r")
    --call GroupEnumUnitsOfPlayer( udg_LocalOtrad2, GetTriggerPlayer(), null )
    --call ForGroupBJ( udg_LocalOtrad2, function Trig_GG_Func004A )
    --call ForForce(Vassals[pi], function Freedom)
    ClearPlayer(GetTriggerPlayer())
    
end
--===========================================================================
function InitTrig_GG()
    gg_trg_GG=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(0), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(1), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(2), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(3), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(4), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(5), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(6), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(7), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(8), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(9), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(10), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(11), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(12), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(13), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(15), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(14), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(16), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(17), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(18), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(19), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(20), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(21), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(22), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(23), " - gg", true)
    TriggerRegisterPlayerChatEvent(gg_trg_GG, Player(24), " - gg", true)
    
    
    TriggerAddAction(gg_trg_GG, Trig_GG_Actions)
end
--===========================================================================
-- Trigger: Observer
--===========================================================================
function Trig_Untitled_Trigger_006_Func003A()
    SetPlayerAllianceStateBJ(GetEnumPlayer(), udg_LocalPlayer, bj_ALLIANCE_UNALLIED)
    SetPlayerAllianceStateBJ(udg_LocalPlayer, GetEnumPlayer(), bj_ALLIANCE_UNALLIED)
end
function Trig_Observer_Actions()
    local pi= GetPlayerId(GetTriggerPlayer())
    DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "")
    ClearPlayer(GetTriggerPlayer())
    ForceAddPlayer(Observers, GetTriggerPlayer())
    udg_Visibl[pi]=CreateFogModifierRectBJ(true, GetTriggerPlayer(), FOG_OF_WAR_VISIBLE, bj_mapInitialPlayableArea)
    
    udg_LocalPlayer=GetTriggerPlayer()
    ForForce(udg_AllPlayers, Trig_Untitled_Trigger_006_Func003A)
   
end
--===========================================================================
function InitTrig_Observer()
    local i= 0
    gg_trg_Observer=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_Observer, Player(i), " - observer", true)
        
        i=i + 1
    end
    TriggerAddAction(gg_trg_Observer, Trig_Observer_Actions)
end
--===========================================================================
-- Trigger: NoChangeAlly
--===========================================================================
function Trig_NoChangeAlly_Conditions()
    return IsPlayerInForce(GetTriggerPlayer(), Observers)
end
function Trig_NoChangeAlly_Actions()
    udg_LocalPlayer=GetTriggerPlayer()
    ForForce(udg_AllPlayers, Trig_Untitled_Trigger_006_Func003A)
end
--===========================================================================
function InitTrig_NoChangeAlly()
    gg_trg_NoChangeAlly=CreateTrigger()
    TriggerRegisterPlayerEventAllianceChanged(gg_trg_NoChangeAlly, Player(0))
    TriggerAddCondition(gg_trg_NoChangeAlly, Condition(Trig_NoChangeAlly_Conditions))
    TriggerAddAction(gg_trg_NoChangeAlly, Trig_NoChangeAlly_Actions)
end
--===========================================================================
-- Trigger: ObserverOff
--===========================================================================
function Trig_ObserverOff_Actions()
    local pi= GetPlayerId(GetTriggerPlayer())
    DisplayTextToPlayer(GetTriggerPlayer(), 0, 0, "")
    
    ForceRemovePlayer(Observers, GetTriggerPlayer())
    FogModifierStop(udg_Visibl[pi])
    DestroyFogModifier(udg_Visibl[pi])
    
   
   
end
--===========================================================================
function InitTrig_ObserverOff()
    local i= 0
    gg_trg_ObserverOff=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_ObserverOff, Player(i), " - observeroff", true)
        
        i=i + 1
    end
    TriggerAddAction(gg_trg_ObserverOff, Trig_ObserverOff_Actions)
end
--===========================================================================
-- Trigger: Hunter
--===========================================================================
function Trig_Hunter_Conditions()
    return CountUnitsInGroup(GetUnitsInRectOfPlayer(gg_rct_Region_112, GetTriggerPlayer())) ~= 0
end
function Trig_Hunter_Actions()
    CreateNUnitsAtLoc(1, FourCC('h0NY'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Region_112), bj_UNIT_FACING)
    DisplayTextToForce(GetForceOfPlayer(GetTriggerPlayer()), "TRIGSTR_5829")
    DisableTrigger(gg_trg_Hunter)
end
--===========================================================================
function InitTrig_Hunter()
    local i= 0
    gg_trg_Hunter=CreateTrigger()
    while true do
        if i >= 24 then break end
        TriggerRegisterPlayerChatEvent(gg_trg_Hunter, Player(i), " - s", true)
        i=i + 1
    
    end
    
    TriggerAddCondition(gg_trg_Hunter, Condition(Trig_Hunter_Conditions))
    TriggerAddAction(gg_trg_Hunter, Trig_Hunter_Actions)
end
--===========================================================================
-- Trigger: ArchontMode
--===========================================================================
function CorrectNumber()
    return pi2 >= 0 and pi2 <= 24
end
function Trig_ArchontMode_Actions()
    local s= SubStringBJ(GetEventPlayerChatString(), 8, 10)
    local pi2= S2I(s) - 1
    local pi1= GetPlayerId(GetTriggerPlayer())
    if CorrectNumber(pi2) then
        DisplayTextToPlayer(Player(pi1), 0, 0, "" .. GetPlayerName(Player(pi2)) .. "" .. I2S(pi2))
        DisplayTextToPlayer(Player(pi2), 0, 0, "" .. GetPlayerName(Player(pi1)))
        SetPlayerAllianceStateBJ(Player(pi1), Player(pi2), bj_ALLIANCE_ALLIED_ADVUNITS)
    end
    MultiboardAllowDisplayBJ(true)
end
--===========================================================================
function InitTrig_ArchontMode()
    local i= 0
    gg_trg_ArchontMode=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_ArchontMode, Player(i), " - arhont", false)
        
        i=i + 1
    end
    
    TriggerAddAction(gg_trg_ArchontMode, Trig_ArchontMode_Actions)
end
--===========================================================================
-- Trigger: Untitled Trigger 001
--===========================================================================
function Trig_Untitled_Trigger_001_Actions()
    MultiboardDisplayBJ(false, GetLastCreatedMultiboard())
    MultiboardDisplayBJ(true, Multiboard)
    TriggerSleepAction(7)
    MultiboardDisplayBJ(true, GetLastCreatedMultiboard())
end
--===========================================================================
function InitTrig_Untitled_Trigger_001()
    gg_trg_Untitled_Trigger_001=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Untitled_Trigger_001, Player(0), "A3", true)
    TriggerAddAction(gg_trg_Untitled_Trigger_001, Trig_Untitled_Trigger_001_Actions)
end
--===========================================================================
-- Trigger: ArchontModeOff
--===========================================================================
function Trig_ArchontModeOff_Actions()
    local s= SubStringBJ(GetEventPlayerChatString(), 8, 10)
    local pi2= S2I(s) - 1
    local pi1= GetPlayerId(GetTriggerPlayer())
    if CorrectNumber(pi2) and DipMode ~= 1 then
        DisplayTextToPlayer(Player(pi1), 0, 0, "" .. GetPlayerName(Player(pi2)) .. "" .. I2S(pi2))
        DisplayTextToPlayer(Player(pi1), 0, 0, "" .. GetPlayerName(Player(pi1)))
        SetPlayerAllianceBJ(Player(pi1), ALLIANCE_SHARED_ADVANCED_CONTROL, false, Player(pi2))
    end
   
end
--===========================================================================
function InitTrig_ArchontModeOff()
    local i= 0
    gg_trg_ArchontModeOff=CreateTrigger()
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerChatEvent(gg_trg_ArchontModeOff, Player(i), " - arhoff", false)
        
        i=i + 1
    end
    
    TriggerAddAction(gg_trg_ArchontModeOff, Trig_ArchontModeOff_Actions)
end
--===========================================================================
-- Trigger: ForSoldUnitsSelect
--===========================================================================
function Trig_ForSoldUnitsSelect_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('Asud')) > 0 and GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetTriggerPlayer(), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_ForSoldUnitsSelect_Actions()
    local mainplayer= GetOwningPlayer(GetTriggerUnit())
    local general= GetTriggerPlayer()
    local pi= GetPlayerId(general)
    NotOwnRes[pi]=true
    OwnGold[pi]=GetPlayerState(general, PLAYER_STATE_RESOURCE_GOLD)
    OwnLumber[pi]=GetPlayerState(general, PLAYER_STATE_RESOURCE_LUMBER)
    SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_GOLD))
    SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_LUMBER))
    
    
    mainplayer=nil
    general=nil
end
--===========================================================================
function InitTrig_ForSoldUnitsSelect()
    local i= 0
    gg_trg_ForSoldUnitsSelect=CreateTrigger()
    
    
    
    
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerSelectionEventBJ(gg_trg_ForSoldUnitsSelect, Player(i), true)
        
        i=i + 1
    end
    
    
    
    TriggerAddCondition(gg_trg_ForSoldUnitsSelect, Condition(Trig_ForSoldUnitsSelect_Conditions))
      
    TriggerAddAction(gg_trg_ForSoldUnitsSelect, Trig_ForSoldUnitsSelect_Actions)
end
--===========================================================================
-- Trigger: ForSoldUnitsDesel
--===========================================================================
function Trig_ForSoldUnitsDesel_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('Asud')) > 0 and GetPlayerAlliance(GetOwningPlayer(GetTriggerUnit()), GetTriggerPlayer(), ALLIANCE_SHARED_ADVANCED_CONTROL)
end
function Trig_ForSoldUnitsDesel_Actions()
    local mainplayer= GetOwningPlayer(GetTriggerUnit())
    local general= GetTriggerPlayer()
    local pi= GetPlayerId(general)
   
    if NotOwnRes[pi] then
        SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_GOLD, OwnGold[pi])
        SetPlayerStateBJ(general, PLAYER_STATE_RESOURCE_LUMBER, OwnLumber[pi])
        
        
        --??? ???
        
        SetPlayerStateBJ(mainplayer, PLAYER_STATE_RESOURCE_GOLD, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_GOLD) + GoldDifference[pi])
        SetPlayerStateBJ(mainplayer, PLAYER_STATE_RESOURCE_LUMBER, GetPlayerState(mainplayer, PLAYER_STATE_RESOURCE_LUMBER) + LumberDifference[pi])
        GoldDifference[pi]=0
        LumberDifference[pi]=0
    end
    
    mainplayer=nil
    general=nil
end
--===========================================================================
function InitTrig_ForSoldUnitsDesel()
    local i= 0
    gg_trg_ForSoldUnitsDesel=CreateTrigger()
    
    
    while true do
        if i > 23 then break end
        
        TriggerRegisterPlayerSelectionEventBJ(gg_trg_ForSoldUnitsDesel, Player(i), true)
        
        i=i + 1
    end
    TriggerAddCondition(gg_trg_ForSoldUnitsDesel, Condition(Trig_ForSoldUnitsDesel_Conditions))
    TriggerAddAction(gg_trg_ForSoldUnitsDesel, Trig_ForSoldUnitsDesel_Actions)
end
--set GoldDifference[pi]= GoldDifference[pi] - GetUnitGoldCost(GetUnitTypeId(u))
--set LumberDifference[pi]= LumberDifference[pi] - GetUnitWoodCost(GetUnitTypeId(u))
--===========================================================================
-- Trigger: InitGlobals
--===========================================================================
function Trig_InitGlobals_Actions()
    local i= 0
    while true do
        if i > 23 then break end
        OwnGold[i]=0
        OwnLumber[i]=0
        GoldDifference[i]=0
        LumberDifference[i]=0
        NotOwnRes[i]=false
        
        
        i=i + 1
    end
end
--===========================================================================
function InitTrig_InitGlobals()
    gg_trg_InitGlobals=CreateTrigger()
    TriggerAddAction(gg_trg_InitGlobals, Trig_InitGlobals_Actions)
end
--
-- 
-- From this abyssal portal, deep monsters and nags emerge.
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
-- Trigger: Dark green color
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
--===========================================================================
-- Trigger: KillTestUnits   OFF ME
--===========================================================================
function Trig_KillTestUnits_O_Copy_Func001002()
    return RectContainsUnit(gg_rct_TestRegion, GetFilterUnit())
end
function Trig_KillTestUnits_O_Copy_Func003A()
    local u= GetEnumUnit()
    local p= GetOwningPlayer(u)
    local id= GetUnitTypeId(u)
    if IsUnitType(u, UNIT_TYPE_HERO) then
        SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
    end
    RemoveUnit(u)
    u=nil
    p=nil
end
function Trig_KillTestUnits___OFF_ME_Actions()
    GroupEnumUnitsInRect(udg_LocalOtrad2, bj_mapInitialPlayableArea, Condition(Trig_KillTestUnits_O_Copy_Func001002))
    ForGroupBJ(GetUnitsInRectAll(gg_rct_TestRegion), Trig_KillTestUnits_O_Copy_Func003A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_KillTestUnits___OFF_ME()
    gg_trg_KillTestUnits___OFF_ME=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_KillTestUnits___OFF_ME, 0.01)
    TriggerAddAction(gg_trg_KillTestUnits___OFF_ME, Trig_KillTestUnits___OFF_ME_Actions)
end
--===========================================================================
-- Trigger: Setlvl
--===========================================================================
function Trig_Setlvl_Func001001002()
    return IsUnitType(GetFilterUnit(), UNIT_TYPE_HERO)
end
function Trig_Setlvl_Func001A()
    SetHeroLevelBJ(GetEnumUnit(), S2I(SubStringBJ(GetEventPlayerChatString(), 8, 10)), false)
end
function Trig_Setlvl_Actions()
    ForGroupBJ(GetUnitsOfPlayerMatching(GetTriggerPlayer(), Condition(Trig_Setlvl_Func001001002)), Trig_Setlvl_Func001A)
end
--===========================================================================
function InitTrig_Setlvl()
    gg_trg_Setlvl=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Setlvl, Player(0), " - setlvl", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Setlvl, Player(1), "setlvl", false)
    TriggerRegisterPlayerChatEvent(gg_trg_Setlvl, Player(2), "setlvl", false)
    TriggerAddAction(gg_trg_Setlvl, Trig_Setlvl_Actions)
end
--===========================================================================
-- Trigger: A1
--===========================================================================
function Trig_A1_Func001A()
    UnitAddAbilityBJ(FourCC('A0IQ'), GetEnumUnit())
end
function Trig_A1_Actions()
    ForGroupBJ(GetUnitsSelectedAll(Player(0)), Trig_A1_Func001A)
end
--===========================================================================
function InitTrig_A1()
    gg_trg_A1=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_A1, Player(0), "a1", true)
    TriggerAddAction(gg_trg_A1, Trig_A1_Actions)
end
--===========================================================================
-- Trigger: Second O
--===========================================================================
function Trig_Second_O_Func001A()
    CreateNUnitsAtLoc(1, FourCC('h0HJ'), GetEnumPlayer(), GetRectCenter(GetPlayableMapRect()), bj_UNIT_FACING)
end
function Trig_Second_O_Actions()
    ForForce(udg_AllPlayers, Trig_Second_O_Func001A)
end
--===========================================================================
function InitTrig_Second_O()
    gg_trg_Second_O=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Second_O, Player(0), "s2", true)
    TriggerAddAction(gg_trg_Second_O, Trig_Second_O_Actions)
end
--===========================================================================
-- Trigger: KillTestUnits Command
--===========================================================================
function Trig_KillTestUnits_Command_Func001002()
    return RectContainsUnit(gg_rct_TestRegion, GetFilterUnit())
end
function Trig_KillTestUnits_Command_Func003A()
    local u= GetEnumUnit()
    local p= GetOwningPlayer(u)
    local id= GetUnitTypeId(u)
    if IsUnitType(u, UNIT_TYPE_HERO) then
        SetPlayerTechMaxAllowed(p, id, GetPlayerTechMaxAllowed(p, id) + 1)
    end
    RemoveUnit(u)
    u=nil
    p=nil
    
end
function Trig_KillTestUnits_Command_Actions()
    GroupEnumUnitsInRect(udg_LocalOtrad2, bj_mapInitialPlayableArea, Condition(Trig_KillTestUnits_Command_Func001002))
    ForGroupBJ(GetUnitsInRectAll(gg_rct_TestRegion), Trig_KillTestUnits_Command_Func003A)
    GroupClear(udg_LocalOtrad2)
end
--===========================================================================
function InitTrig_KillTestUnits_Command()
    gg_trg_KillTestUnits_Command=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_KillTestUnits_Command, Player(0), "kill", true)
    TriggerAddAction(gg_trg_KillTestUnits_Command, Trig_KillTestUnits_Command_Actions)
end
--===========================================================================
-- Trigger: Visible Copy
--===========================================================================
function Trig_Visible_Copy_Actions()
    CreateFogModifierRectBJ(true, Player(0), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
end
--===========================================================================
function InitTrig_Visible_Copy()
    gg_trg_Visible_Copy=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_Visible_Copy, Player(0), " - v", true)
    TriggerAddAction(gg_trg_Visible_Copy, Trig_Visible_Copy_Actions)
end
-- Helper: parse "2,3,5-7" into array of player numbers (1..24)
function ParseAllyList(s)
    local items = {}
    while #s > 0 do
        local lo, hi = string.match(s, "^(%d+)%-(%d+)")
        if lo then
            local l = tonumber(lo); local h = tonumber(hi)
            if l < 1 then l = 1 end
            if h > 24 then h = 24 end
            if l > h then l, h = h, l end
            for n = l, h do items[#items + 1] = n end
            s = string.gsub(s, "^%d+%-%d+", "", 1)
        else
            local num = string.match(s, "^(%d+)")
            if num then
                local n = tonumber(num)
                if n >= 1 and n <= 24 then items[#items + 1] = n end
                s = string.gsub(s, "^%d+", "", 1)
            else break end
        end
        s = string.gsub(s, "^[,%s]+", "")
    end
    return items
end

-- Set ally shared control (ALLIED_ADVUNITS) for a list of player numbers (1-based)
function SetAllyControl(players, enable)
    for _, pi in ipairs(players) do
        if enable then
            SetPlayerAllianceStateBJ(Player(pi - 1), Player(0), bj_ALLIANCE_ALLIED_ADVUNITS)
        else
            SetPlayerAllianceStateBJ(Player(pi - 1), Player(0), bj_ALLIANCE_UNALLIED)
        end
    end
end

--===========================================================================
-- Trigger: AllyControl (-ally)
--  Usage: -ally 2,3,5-7       — share control of players 2,3,5,6,7
--         -ally off 2,3,5-7   — revoke shared control
--  Also available via bridge: op="ally", arg="2,3,5-7" / arg="off:2,3,5-7"
--  Also via live eval: SetAllyControl(ParseAllyList("2,3,5-7"), true)
--===========================================================================
function Trig_AllyControl_Conditions()
    local s = GetEventPlayerChatString()
    return string.find(s, "^%-ally%s") ~= nil
end
function Trig_AllyControl_Actions()
    local s = GetEventPlayerChatString()
    local offMode, numsPart = string.match(s, "^%-ally%s+([oO][fF][fF])%s+([%d,%-]+)")
    local enable = true
    if numsPart then
        enable = false
    else
        numsPart = string.match(s, "^%-ally%s+([%d,%-]+)")
    end
    if not numsPart then
        ProbeLogWrite("[CHAT] -ally parse failed: " .. s)
        return
    end
    local players = ParseAllyList(numsPart)
    ProbeLogWrite("[CHAT] -ally " .. (enable and "on" or "off") .. " players=" .. tostring(numsPart))
    SetAllyControl(players, enable)
    ReshowArmyBoard()
end
-- Becoming allied with shared units makes WC3 show its native ally-resource panel,
-- which contends for the same screen slot and displaces/minimizes our army multiboard.
-- The board isn't destroyed, just hidden — re-assert it shortly after the change so it
-- pops back. Also exposed as the "-board" chat command.
function ReshowArmyBoard()
    if Multiboard == nil then return end
    local t = CreateTimer()
    TimerStart(t, 0.8, false, function()
        MultiboardDisplay(Multiboard, true)
        MultiboardMinimize(Multiboard, false)
        DestroyTimer(GetExpiredTimer())
    end)
end
function InitTrig_AllyControl()
    gg_trg_AllyControl = CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_AllyControl, Player(0), "-ally", false)
    TriggerAddCondition(gg_trg_AllyControl, Condition(Trig_AllyControl_Conditions))
    TriggerAddAction(gg_trg_AllyControl, Trig_AllyControl_Actions)

    -- Manual re-show fallback if the native ally panel keeps the board hidden.
    local b = CreateTrigger()
    for i = 0, 23 do
        TriggerRegisterPlayerChatEvent(b, Player(i), "-board", true)
    end
    TriggerAddAction(b, ReshowArmyBoard)
end
--===========================================================================
-- Trigger: ResO
--===========================================================================
function Trig_ResO_Actions()
    SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
    SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
    SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
end
--===========================================================================
function InitTrig_ResO()
    gg_trg_ResO=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_ResO, Player(0), "reso", true)
    TriggerAddAction(gg_trg_ResO, Trig_ResO_Actions)
end
--===========================================================================
-- Trigger: ResO Copy
--===========================================================================
function Trig_ResO_Copy_Actions()
    SetMapFlag(MAP_LOCK_RESOURCE_TRADING, false)
    SetMapFlag(MAP_LOCK_ALLIANCE_CHANGES, false)
    SetMapFlag(MAP_ALLIANCE_CHANGES_HIDDEN, false)
end
--===========================================================================
function InitTrig_ResO_Copy()
    gg_trg_ResO_Copy=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_ResO_Copy, Player(0), "reson", true)
    TriggerAddAction(gg_trg_ResO_Copy, Trig_ResO_Copy_Actions)
end
--===========================================================================
-- Trigger: OpemVis
--===========================================================================
function Trig_OpemVis_Func003A()
    FogModifierStop(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    DestroyFogModifier(udg_Visibl[GetConvertedPlayerId(GetEnumPlayer())])
    CreateFogModifierRectBJ(true, GetEnumPlayer(), FOG_OF_WAR_VISIBLE, GetPlayableMapRect())
end
function Trig_OpemVis_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_4166")
    ForForce(udg_AllPlayers, Trig_OpemVis_Func003A)
end
--===========================================================================
function InitTrig_OpemVis()
    gg_trg_OpemVis=CreateTrigger()
    TriggerRegisterPlayerChatEvent(gg_trg_OpemVis, Player(0), "OpenVis", true)
    TriggerAddAction(gg_trg_OpemVis, Trig_OpemVis_Actions)
end
--===========================================================================
-- Trigger: StartLimit
--===========================================================================
function Trig_StartWorgens_Copy_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('h0P7'), 1, GetEnumPlayer())
end
function Trig_StartLimit_Actions()
    ForForce(udg_AllPlayers, Trig_StartWorgens_Copy_Func001A)
end
--===========================================================================
function InitTrig_StartLimit()
    gg_trg_StartLimit=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartLimit, 0.01)
    TriggerAddAction(gg_trg_StartLimit, Trig_StartLimit_Actions)
end
--===========================================================================
-- Trigger: DestroyTrain
--===========================================================================
function Trig_DestroyTrain_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0P7')
end
function Trig_DestroyTrain_Func002A()
    KillUnit(GetEnumUnit())
end
function LimitTrainDestroy()
    SetPlayerTechMaxAllowedSwap(FourCC('h0P7'), 0, GetEnumPlayer())
end
function Trig_DestroyTrain_Actions()
    RemoveUnit(GetTrainedUnit())
    ForGroupBJ(GetUnitsInRectAll(gg_rct_TrainArea), Trig_DestroyTrain_Func002A)
    CreateDestructableLoc(FourCC('B01R'), GetRectCenter(gg_rct_Region_143), 0.0, 3, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 0, 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 0, - 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 650.00, 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 650.00, - 200.00)), GetRandomDirectionDeg(), 1, 0)
    
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 1300.00, 200.00)), GetRandomDirectionDeg(), 1, 0)
    CreateDestructableLoc(FourCC('B01S'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 1300.00, - 200.00)), GetRandomDirectionDeg(), 1, 0)
    
    CreateDestructableLoc(FourCC('B01R'), GetRectCenter(OffsetRectBJ(gg_rct_Region_143, 1300.00, 0.00)), GetRandomDirectionDeg(), 3, 0)
    RemoveUnit(gg_unit_n003_0149)
    RemoveUnit(gg_unit_n003_0028)
    ForForce(udg_AllPlayers, LimitTrainDestroy)
end
--===========================================================================
function InitTrig_DestroyTrain()
    gg_trg_DestroyTrain=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DestroyTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_DestroyTrain, Condition(Trig_DestroyTrain_Conditions))
    TriggerAddAction(gg_trg_DestroyTrain, Trig_DestroyTrain_Actions)
end
--===========================================================================
-- Trigger: BeginDestroingTrain
--===========================================================================
function Trig_BeginDestroingTrain_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('h0P7')
end
function Trig_BeginDestroingTrain_Actions()
      DisplayTextToForce(udg_AllPlayers, " - ...")
end
--===========================================================================
function InitTrig_BeginDestroingTrain()
    gg_trg_BeginDestroingTrain=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BeginDestroingTrain, EVENT_PLAYER_UNIT_TRAIN_START)
    TriggerAddCondition(gg_trg_BeginDestroingTrain, Condition(Trig_BeginDestroingTrain_Conditions))
    TriggerAddAction(gg_trg_BeginDestroingTrain, Trig_BeginDestroingTrain_Actions)
end