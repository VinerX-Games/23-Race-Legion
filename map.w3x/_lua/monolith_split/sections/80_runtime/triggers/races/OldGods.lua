
--===========================================================================
-- Trigger: KakecCommon
--===========================================================================
function DisableKalec()
    SetPlayerAbilityAvailableBJ(false, FourCC('A12R'), GetEnumPlayer())
end
function EnableKalec()
    SetPlayerAbilityAvailableBJ(true, FourCC('A12R'), GetEnumPlayer())
end
--===========================================================================
-- Trigger: KalecStart
--===========================================================================
function Trig_KalecStart_Actions()
    local u
    local l= GetUnitLoc(GetTriggerUnit())
    u=CreateUnitAtLoc(Player(24), FourCC('n04W'), l, bj_UNIT_FACING)
    TriggerRegisterUnitEvent(gg_trg_KalecDead, u, EVENT_UNIT_DEATH)
    UnitRemoveAbility(GetTriggerUnit(), FourCC('A12R'))
    ForForce(udg_AllPlayers, DisableKalec)
    TriggerSleepAction(245)
    if UnitAlive(u) then
        ShowUnit(u, false)
        RemoveUnit(u)
        DisplayTextToPlayer(GetOwningPlayer(GetTriggerUnit()), 0, 0, "4")
        ForForce(udg_AllPlayers, EnableKalec)
        UnitAddAbility(GetTriggerUnit(), FourCC('A12R'))
    end
    
    RemoveLocation(l)
    l=nil
    u=nil
end
--===========================================================================
function InitTrig_KalecStart()
    gg_trg_KalecStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KalecStart, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_KalecStart, function()
        if GetSpellAbilityId() ~= FourCC('A12R') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_KalecStart_Actions()
    end)
end
--===========================================================================
-- Trigger: KalecDead
--===========================================================================
function Trig_KalecDead_Func004A()
    SetPlayerAbilityAvailableBJ(false, FourCC('A12R'), GetEnumPlayer())
end
function Trig_KalecDead_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    SpawnGroundItem(FourCC('I01U'), GetLocationX(udg_LocalPosition2), GetLocationY(udg_LocalPosition2))
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_25200")
    ForForce(udg_AllPlayers, Trig_KalecDead_Func004A)
    DisableTrigger(gg_trg_KalecStart)
end
--===========================================================================
function InitTrig_KalecDead()
    gg_trg_KalecDead=CreateTrigger()
    TriggerAddAction(gg_trg_KalecDead, Trig_KalecDead_Actions)
end
--===========================================================================
-- Trigger: ShaStart
--===========================================================================
function DisableSha()
    SetPlayerAbilityAvailableBJ(false, FourCC('A1ML'), GetEnumPlayer())
end
function Trig_ShaStart_Actions()
    local u
    u=CreateUnit(Player(24), FourCC('n076'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), bj_UNIT_FACING)
    TriggerRegisterUnitEvent(gg_trg_ShaDead, u, EVENT_UNIT_DEATH)
    UnitRemoveAbility(GetTriggerUnit(), FourCC('A1ML'))
    ForForce(udg_AllPlayers, DisableSha)
    u=nil
end
--===========================================================================
function InitTrig_ShaStart()
    gg_trg_ShaStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ShaStart, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ShaStart, function()
        if GetSpellAbilityId() ~= FourCC('A1ML') then return end
        if not (IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))) then return end
        Trig_ShaStart_Actions()
    end)
end
--===========================================================================
-- Trigger: ShaDead
--===========================================================================
function Trig_ShaDead_Actions()
    SpawnGroundItem(FourCC('I021'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()))
    DisplayTextToForce(udg_AllPlayers2, ".")
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnit()), PLAYER_STATE_RESOURCE_GOLD)
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnit()), PLAYER_STATE_RESOURCE_LUMBER)
    DisableTrigger(gg_trg_ShaStart)
    DisableTrigger(gg_trg_ShaDead)
end
--===========================================================================
function InitTrig_ShaDead()
    gg_trg_ShaDead=CreateTrigger()
    TriggerAddAction(gg_trg_ShaDead, Trig_ShaDead_Actions)
end
--===========================================================================
-- Trigger: AncientGods add MindControl Copy
--===========================================================================
function Trig_AncientGods_add_MindControl_Copy_Actions()
    UnitAddAbilityBJ(FourCC('A0W4'), gg_unit_n03D_0666)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_AncientGods_add_MindControl_Copy()
    gg_trg_AncientGods_add_MindControl_Copy=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncientGods_add_MindControl_Copy, gg_unit_n03D_0666, LESS_THAN, 15000.00)
    TriggerAddAction(gg_trg_AncientGods_add_MindControl_Copy, Trig_AncientGods_add_MindControl_Copy_Actions)
end
--===========================================================================
-- Trigger: AncienGods Add MassAttak Copy
--===========================================================================
function Trig_AncienGods_Add_MassAttak_Copy_Actions()
    UnitAddAbilityBJ(FourCC('A0T3'), gg_unit_n03D_0666)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_AncienGods_Add_MassAttak_Copy()
    gg_trg_AncienGods_Add_MassAttak_Copy=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncienGods_Add_MassAttak_Copy, gg_unit_n03D_0666, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_AncienGods_Add_MassAttak_Copy, Trig_AncienGods_Add_MassAttak_Copy_Actions)
end
--===========================================================================
-- Trigger: Qtun 17k o
--===========================================================================
function Trig_Qtun_17k_o_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt1)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt2)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt3)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt4)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qtun_17k_o()
    gg_trg_Qtun_17k_o=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qtun_17k_o, gg_unit_n03D_0666, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_Qtun_17k_o, Trig_Qtun_17k_o_Actions)
end
--===========================================================================
-- Trigger: Qtun HP 24k O
--===========================================================================
function Trig_Qtun_HP_24k_O_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt1)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt2)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt3)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Qt4)
    CreateNUnitsAtLoc(1, FourCC('n03J'), Player(PLAYER_NEUTRAL_AGGRESSIVE), udg_LocalPosition2, bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qtun_HP_24k_O()
    gg_trg_Qtun_HP_24k_O=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qtun_HP_24k_O, gg_unit_n03D_0666, LESS_THAN, 24000.00)
    TriggerAddAction(gg_trg_Qtun_HP_24k_O, Trig_Qtun_HP_24k_O_Actions)
end
--===========================================================================
-- Trigger: Qtun Die
--===========================================================================
function Trig_Qtun_Die_Conditions()
    return (( GetTriggerUnit() == gg_unit_n03D_0666 )) and (( GetOwningPlayer(GetTriggerUnit()) ~= GetOwningPlayer(GetKillingUnitBJ()) ))
end
function Trig_Qtun_Die_Actions()
    udg_LocalPosition2=GetUnitLoc(GetTriggerUnit())
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_2385")
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_GOLD)
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_LUMBER)
    SpawnGroundItem(FourCC('I01R'), GetLocationX(udg_LocalPosition2), GetLocationY(udg_LocalPosition2))
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qtun_Die()
    gg_trg_Qtun_Die=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Qtun_Die, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Qtun_Die, Condition(Trig_Qtun_Die_Conditions))
    TriggerAddAction(gg_trg_Qtun_Die, Trig_Qtun_Die_Actions)
end
--===========================================================================
-- Trigger: SpawnQtun
--===========================================================================
function Trig_SpawnQtun_Func006C()
    return (( GetTriggerUnit() == gg_unit_n03D_0666 )) and (( GetSpellAbilityId() == FourCC('A0W0') )) and (( GetPlayerController(GetOwningPlayer(GetTriggerUnit())) ~= MAP_CONTROL_USER ))
end
function Trig_SpawnQtun_Conditions()
    return Trig_SpawnQtun_Func006C()
end
function Trig_SpawnQtun_Func002Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func002Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func002C()
    return GetUnitLifePercent(GetTriggerUnit()) >= 75.00
end
function Trig_SpawnQtun_Func003Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func003Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func003C()
    return (( GetUnitLifePercent(GetTriggerUnit()) <= 75.00 )) and (( GetUnitLifePercent(GetTriggerUnit()) >= 50.00 ))
end
function Trig_SpawnQtun_Func004Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func004Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func004C()
    return (( GetUnitLifePercent(GetTriggerUnit()) <= 50.00 )) and (( GetUnitLifePercent(GetTriggerUnit()) >= 25.00 ))
end
function Trig_SpawnQtun_Func005Func002C()
    return udg_LocalInteger2 == 1
end
function Trig_SpawnQtun_Func005Func008A()
    UnitApplyTimedLifeBJ(30.00, FourCC('BTLF'), GetEnumUnit())
    IssuePointOrderLocBJ(GetEnumUnit(), "attack", udg_LocalPosition3)
end
function Trig_SpawnQtun_Func005C()
    return GetUnitLifePercent(GetTriggerUnit()) <= 50.00
end
function Trig_SpawnQtun_Actions()
    udg_LocalInteger2=GetRandomInt(1, 2)
    if Trig_SpawnQtun_Func002C() then
        if Trig_SpawnQtun_Func002Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00)
        udg_LocalInteger2=udg_LocalInteger * 2
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func002Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
    if Trig_SpawnQtun_Func003C() then
        udg_LocalInteger2=GetRandomInt(1, 2)
        if Trig_SpawnQtun_Func003Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00)
        udg_LocalInteger2=udg_LocalInteger * 4
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func003Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
    if Trig_SpawnQtun_Func004C() then
        udg_LocalInteger2=GetRandomInt(1, 2)
        if Trig_SpawnQtun_Func004Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00)
        udg_LocalInteger2=udg_LocalInteger * 1
        CreateNUnitsAtLoc(udg_LocalInteger2, FourCC('e01Q'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func004Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
    if Trig_SpawnQtun_Func005C() then
        udg_LocalInteger2=GetRandomInt(1, 2)
        if Trig_SpawnQtun_Func005Func002C() then
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp2)
        else
            udg_LocalPosition2=GetRectCenter(gg_rct_QtunSp1)
        end
        udg_LocalInteger=R2I(( I2R(BlzGetUnitMaxHP(GetTriggerUnit())) - GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) ) / 1000.00)
        udg_LocalInteger2=udg_LocalInteger * 1
        CreateNUnitsAtLoc(udg_LocalInteger2, FourCC('e01P'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition2, bj_UNIT_FACING)
        udg_LocalOtrad=GetLastCreatedGroup()
        udg_LocalPosition3=GetUnitLoc(gg_unit_n03D_0666)
        ForGroupBJ(udg_LocalOtrad, Trig_SpawnQtun_Func005Func008A)
        GroupClear(udg_LocalOtrad)
        RemoveLocation(udg_LocalPosition2)
        RemoveLocation(udg_LocalPosition3)
    end
end
--===========================================================================
function InitTrig_SpawnQtun()
    gg_trg_SpawnQtun=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpawnQtun, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_SpawnQtun, Condition(Trig_SpawnQtun_Conditions))
    TriggerAddAction(gg_trg_SpawnQtun, Trig_SpawnQtun_Actions)
end
--===========================================================================
-- Trigger: Qogg HP 24k O
--===========================================================================
function Trig_Qogg_HP_24k_O_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_1)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_2)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_3)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_4)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qogg_HP_24k_O()
    gg_trg_Qogg_HP_24k_O=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qogg_HP_24k_O, gg_unit_n03A_0657, LESS_THAN, 24000.00)
    TriggerAddAction(gg_trg_Qogg_HP_24k_O, Trig_Qogg_HP_24k_O_Actions)
end
--===========================================================================
-- Trigger: Qogg HP 17k O
--===========================================================================
function Trig_Qogg_HP_17k_O_Actions()
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_5)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_5), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_6)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_6), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_7)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_7), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    udg_LocalPosition2=GetRectCenter(gg_rct_Yog1_8)
    CreateNUnitsAtLoc(1, FourCC('n04C'), Player(PLAYER_NEUTRAL_AGGRESSIVE), GetRectCenter(gg_rct_Yog1_8), bj_UNIT_FACING)
    RemoveLocation(udg_LocalPosition2)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qogg_HP_17k_O()
    gg_trg_Qogg_HP_17k_O=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_Qogg_HP_17k_O, gg_unit_n03A_0657, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_Qogg_HP_17k_O, Trig_Qogg_HP_17k_O_Actions)
end
--===========================================================================
-- Trigger: AncienGods Add MassAttak
--===========================================================================
function Trig_AncienGods_Add_MassAttak_Actions()
    UnitAddAbilityBJ(FourCC('A0T3'), gg_unit_n03A_0657)
end
--===========================================================================
function InitTrig_AncienGods_Add_MassAttak()
    gg_trg_AncienGods_Add_MassAttak=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncienGods_Add_MassAttak, gg_unit_n03A_0657, LESS_THAN, 17000.00)
    TriggerAddAction(gg_trg_AncienGods_Add_MassAttak, Trig_AncienGods_Add_MassAttak_Actions)
end
--===========================================================================
-- Trigger: AncientGods add MindControl
--===========================================================================
function Trig_AncientGods_add_MindControl_Actions()
    UnitAddAbilityBJ(FourCC('A0W4'), gg_unit_n03A_0657)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_AncientGods_add_MindControl()
    gg_trg_AncientGods_add_MindControl=CreateTrigger()
    TriggerRegisterUnitLifeEvent(gg_trg_AncientGods_add_MindControl, gg_unit_n03A_0657, LESS_THAN, 15000.00)
    TriggerAddAction(gg_trg_AncientGods_add_MindControl, Trig_AncientGods_add_MindControl_Actions)
end
--===========================================================================
-- Trigger: Qogg Die
--===========================================================================
function Trig_Qogg_Die_Conditions()
    return GetTriggerUnit() == gg_unit_n03A_0657
end
function Trig_Qogg_Die_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_20558")
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_GOLD)
    AdjustPlayerStateBJ(20000, GetOwningPlayer(GetKillingUnitBJ()), PLAYER_STATE_RESOURCE_LUMBER)
    SpawnGroundItem(FourCC('I01Q'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()))
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Qogg_Die()
    gg_trg_Qogg_Die=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Qogg_Die, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Qogg_Die, Condition(Trig_Qogg_Die_Conditions))
    TriggerAddAction(gg_trg_Qogg_Die, Trig_Qogg_Die_Actions)
end
--===========================================================================
-- Trigger: QoggSpawn
--===========================================================================
function Trig_Spell1_Copy_2_Func008C()
    return (( GetTriggerUnit() == gg_unit_n03A_0657 )) and (( GetSpellAbilityId() == FourCC('A0T7') )) and (( GetPlayerController(GetOwningPlayer(GetTriggerUnit())) ~= MAP_CONTROL_USER ))
end
function Trig_QoggSpawn_Conditions()
    return Trig_Spell1_Copy_2_Func008C()
end
function Trig_Spell1_Copy_2_Func003C()
    return udg_LocalInteger == 1
end
function Trig_Spell1_Copy_2_Func004C()
    return udg_LocalInteger == 2
end
function Trig_Spell1_Copy_2_Func005C()
    return udg_LocalInteger == 3
end
function Trig_Spell1_Copy_2_Func006C()
    return udg_LocalInteger == 4
end
function Trig_Spell1_Copy_2_Func007C()
    return udg_LocalInteger == 5
end
function Trig_QoggSpawn_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    udg_LocalPosition2=GetRandomLocInRect(gg_rct_Region_083)
    udg_LocalInteger=GetRandomInt(1, 5)
    if Trig_Spell1_Copy_2_Func003C() then
        CreateNUnitsAtLoc(1, FourCC('n04C'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func004C() then
        CreateNUnitsAtLoc(1, FourCC('n03C'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func005C() then
        CreateNUnitsAtLoc(1, FourCC('n04K'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func006C() then
        CreateNUnitsAtLoc(1, FourCC('n04L'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    if Trig_Spell1_Copy_2_Func007C() then
        CreateNUnitsAtLoc(1, FourCC('n04J'), p, udg_LocalPosition2, bj_UNIT_FACING)
        UnitApplyTimedLifeBJ(60, FourCC('BTLF'), GetLastCreatedUnit())
        return
    end
    
    p=nil
    u=nil
end
--===========================================================================
function InitTrig_QoggSpawn()
    gg_trg_QoggSpawn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_QoggSpawn, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddCondition(gg_trg_QoggSpawn, Condition(Trig_QoggSpawn_Conditions))
    TriggerAddAction(gg_trg_QoggSpawn, Trig_QoggSpawn_Actions)
end