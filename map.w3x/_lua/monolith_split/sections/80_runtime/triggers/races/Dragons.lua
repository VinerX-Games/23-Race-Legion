
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
function Trig_FlyDragon_Actions()
    local GT= GetTriggerUnit()
    local t= CreateTimer()
    local x= GetUnitX(GT)
    local y= GetUnitY(GT)
    local x1= GetSpellTargetX()
    local y1= GetSpellTargetY()
    local l= JSTRRastMT(x , x1 , y , y1)
    local fl= GetUnitFlyHeight(GT)
    
    JSTRSkill=GetSpellAbilityId()
    UnitAddAbility(GT, FourCC('Amrf'))
    UnitAddAbility(GT, FourCC('A16S'))
    UnitRemoveAbility(GT, FourCC('Amrf'))
    ---------
    TimerStart(t, 0.05, true, function()
        local dx= GetUnitX(GT)
        local dy= GetUnitY(GT)
        local ugol= JSTRUgolMT(dx, x1, dy, y1)
        local MaxW
        if l <= 500 then MaxW=l else MaxW=500 end
        local nx=dx + 6 * Cos(ugol * bj_DEGTORAD)
        local ny=dy + 6 * Sin(ugol * bj_DEGTORAD)
        local w=JSTRParabolaZ(MaxW, l, JSTRRastMT(nx, x1, ny, y1))
        if JSTRRastMT(x1, dx, y1, dy) > 25 then
            SetUnitX(GT, nx)
            SetUnitY(GT, ny)
            SetUnitFacing(GT, ugol)
            SetUnitFlyHeight(GT, fl + w, 0)
        else
            UnitRemoveAbility(GT, FourCC('A16S'))
            DestroyTimer(t)
            SetUnitAnimation(GT, "Stand")
            SetUnitFlyHeight(GT, fl, 0)
            local g=CreateGroup()
            GroupEnumUnitsInRange(g, dx, dy, 260, nil)
            while true do
                local un=FirstOfGroup(g)
                if un == nil then break end
                local lvl=GetUnitAbilityLevel(GT, JSTRSkill)
                GroupRemoveUnit(g, un)
            end
            DestroyGroup(g)
        end
    end)
    ---------
    GT=nil
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