
--===========================================================================
-- Trigger: PoleAstralaDragons
--===========================================================================
function Trig_PoleAstralaDragons_Func003002()
    return 0 == 0
end
function Trig_PoleAstralaDragons_Func005A()
    local u
    CreateNUnitsAtLoc(1, FourCC('H0BN'), GetOwningPlayer(GetTriggerUnit()), udg_LocalPosition[14], bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('AHbn'), GetLastCreatedUnit())
    SetUnitManaBJ(GetLastCreatedUnit(), 1111111.00)
    SetUnitAbilityLevelSwapped(FourCC('AHbn'), GetLastCreatedUnit(), GetUnitAbilityLevelSwapped(FourCC('A08R'), GetTriggerUnit()))
    IssueTargetOrderBJ(GetLastCreatedUnit(), "banish", GetEnumUnit())
    u=udg_LocalUnit[1]
    UnitApplyTimedLife(u, FourCC('BTLF'), 2)
    u=nil
end
function Trig_PoleAstralaDragons_Actions()
    udg_LocalPosition[14]=GetUnitLoc(GetTriggerUnit())
    udg_LocalPosition2=GetSpellTargetLoc()
    udg_Boolexpr = Trig_PoleAstralaDragons_Func003002
    GroupEnumUnitsInRangeOfLoc(udg_LocalOtrad2, udg_LocalPosition2, 200, udg_Boolexpr)
    ForGroupBJ(udg_LocalOtrad2, Trig_PoleAstralaDragons_Func005A)
    RemoveLocation(udg_LocalPosition[14])
end
--===========================================================================
function InitTrig_PoleAstralaDragons()
    gg_trg_PoleAstralaDragons=CreateTrigger()
    DisableTrigger(gg_trg_PoleAstralaDragons)
    TriggerRegisterAnyUnitEventBJ(gg_trg_PoleAstralaDragons, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_PoleAstralaDragons, function()
        if GetSpellAbilityId() ~= FourCC('A0QV') then return end
        Trig_PoleAstralaDragons_Actions()
    end)
end
--===========================================================================
-- Trigger: Dark Dragon
--===========================================================================
function Trig_Dark_Dragon_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n03O'), 0, GetEnumPlayer())
end
function Trig_Dark_Dragon_Actions()
    ForForce(udg_AllPlayers, Trig_Dark_Dragon_Func001A)
end
--===========================================================================
function InitTrig_Dark_Dragon()
    gg_trg_Dark_Dragon=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Dark_Dragon, 5)
    TriggerAddAction(gg_trg_Dark_Dragon, Trig_Dark_Dragon_Actions)
end
--===========================================================================
-- Trigger: Old Dark Dragon
--===========================================================================
function Trig_Old_Dark_Dragon_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('n03P'), 0, GetEnumPlayer())
end
function Trig_Old_Dark_Dragon_Actions()
    ForForce(udg_AllPlayers, Trig_Old_Dark_Dragon_Func001A)
end
--===========================================================================
function InitTrig_Old_Dark_Dragon()
    gg_trg_Old_Dark_Dragon=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_Old_Dark_Dragon, 5)
    TriggerAddAction(gg_trg_Old_Dark_Dragon, Trig_Old_Dark_Dragon_Actions)
end
--===========================================================================
-- Trigger: FlyDragon
--===========================================================================
--================
function Trig_Charge_move_heroD()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local GT= LoadUnitHandle(Hash, h, 1)
    local l= LoadReal(Hash, h, 2)
    local g
    local x1= LoadReal(Hash, h, 4)
    local y1= LoadReal(Hash, h, 5)
    local fl= LoadReal(Hash, h, 6)
    local dx= GetUnitX(GT)
    local dy= GetUnitY(GT)
    local un
    local x
    local y
    local uron
    local lvl
    local w
    local ugol= JSTRUgolMT(dx , x1 , dy , y1)
    local t1
    local h1
    local MaxW
    if l <= 500 then
        MaxW=l
    else
        MaxW=500
    end
    ---------
    x=dx + 6 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=dy + 6 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    w=JSTRParabolaZ(MaxW , l , JSTRRastMT(x , x1 , y , y1)) --????????? ??????
    
    -- ???? ????? ????
    if JSTRRastMT(x1 , dx , y1 , dy) > 25 then --and not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then
        -- ??????? ?????
        SetUnitX(GT, x)
        SetUnitY(GT, y)
        SetUnitFacing(GT, ugol)
        SetUnitFlyHeight(GT, fl + w, 0)
        
    else
        UnitRemoveAbility(GT, FourCC('A16S')) -- ?????? ?????
        DestroyEffect(LoadEffectHandle(Hash, h, 6))
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitAnimation(GT, "Stand")
        SetUnitFlyHeight(GT, fl, 0)
        --call DestroyEffect(AddSpecialEffect("AbilitiesSpellsOrcWarStompWarStompCaster.mdl", dx, dy))
        g=CreateGroup()
        GroupEnumUnitsInRange(g, dx, dy, 260, nil)
        while true do
            un=FirstOfGroup(g)
            if un == nil then break end
            lvl=GetUnitAbilityLevel(GT, JSTRSkill)
                    
            GroupRemoveUnit(g, un)
        end
        DestroyGroup(g)
    end
    ---------
    GT=nil
    un=nil
    g=nil
    t=nil
    t1=nil
end
--================================================================================================================================================================================
-- ???? 2 - ???????? ???????
--================
function Trig_FlyDragon_Actions()
    local GT= GetTriggerUnit()
    --local group g = CreateGroup()
    local t= CreateTimer()
    local h= GetHandleId(t)
    local x= GetUnitX(GT)
    local y= GetUnitY(GT)
    local x1= GetSpellTargetX()
    local y1= GetSpellTargetY()
    local l= JSTRRastMT(x , x1 , y , y1)
    
    JSTRSkill=GetSpellAbilityId()
    UnitAddAbility(GT, FourCC('Amrf'))
    UnitAddAbility(GT, FourCC('A16S')) -- ?????? ?????
    
    UnitRemoveAbility(GT, FourCC('Amrf'))
    ---------
    SaveUnitHandle(Hash, h, 1, GT)
    if l ~= 0 then
        SaveReal(Hash, h, 2, l)
    else
        SaveReal(Hash, h, 2, 1)
    end
    SaveReal(Hash, h, 4, x1)
    SaveReal(Hash, h, 5, y1)
    SaveReal(Hash, h, 6, GetUnitFlyHeight(GT))
    --call DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.05, true, Trig_Charge_move_heroD) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_FlyDragon()
    gg_trg_FlyDragon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FlyDragon, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_FlyDragon, function()
        if GetSpellAbilityId() ~= FourCC('drA2') then return end
        Trig_FlyDragon_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonUnionStart
--===========================================================================
function Trig_DragonUnionStart_Actions()
    gPlayer=GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(gPlayer, FourCC('n044'), 0)
    SetPlayerTechMaxAllowed(gPlayer, FourCC('R0A7'), 0)
    SetPlayerTechMaxAllowed(gPlayer, FourCC('R0AZ'), 0)
end
--===========================================================================
function InitTrig_DragonUnionStart()
    gg_trg_DragonUnionStart=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonUnionStart, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_DragonUnionStart, function()
        if GetSpellAbilityId() ~= FourCC('A1MZ') then return end
        Trig_DragonUnionStart_Actions()
    end)
end
--===========================================================================
-- Trigger: GreenAutoAstral
--===========================================================================
function Trig_GreenAutoAstral_Actions()
    IssueTargetOrder(GetTriggerUnit(), "banish", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_GreenAutoAstral()
    gg_trg_GreenAutoAstral=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GreenAutoAstral, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GreenAutoAstral, function()
        if GetSpellAbilityId() ~= FourCC('drAe') then return end
        Trig_GreenAutoAstral_Actions()
    end)
end
--===========================================================================
-- Trigger: TrainGreenPhase
--===========================================================================
function Trig_TrainGreenPhase_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('drAw')) > 0
end
function Trig_TrainGreenPhase_Actions()
    IssueImmediateOrder(GetTrainedUnit(), "phaseshifton")
end
--===========================================================================
function InitTrig_TrainGreenPhase()
    gg_trg_TrainGreenPhase=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainGreenPhase, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_TrainGreenPhase, Condition(Trig_TrainGreenPhase_Conditions))
    TriggerAddAction(gg_trg_TrainGreenPhase, Trig_TrainGreenPhase_Actions)
end
--===========================================================================
-- Trigger: TrainGreenSpellSteal
--===========================================================================
function Trig_TrainGreenSpellSteal_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('A0RM')) > 0
end
function Trig_TrainGreenSpellSteal_Actions()
    IssueImmediateOrder(GetTrainedUnit(), "spellstealon")
end
--===========================================================================
function InitTrig_TrainGreenSpellSteal()
    gg_trg_TrainGreenSpellSteal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainGreenSpellSteal, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_TrainGreenSpellSteal, Condition(Trig_TrainGreenSpellSteal_Conditions))
    TriggerAddAction(gg_trg_TrainGreenSpellSteal, Trig_TrainGreenSpellSteal_Actions)
end