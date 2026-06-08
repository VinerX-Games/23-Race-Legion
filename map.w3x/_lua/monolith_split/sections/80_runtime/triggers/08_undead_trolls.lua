    gg_trg_Duel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Duel, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Duel, function()
        if GetSpellAbilityId() ~= FourCC('w2ou') then return end
        if not (IsUnitType(GetSpellTargetUnit(), UNIT_TYPE_HERO)) then return end
        Trig_Duel_Actions()
    end)
end
--===========================================================================
-- Trigger: RiseDeadWorkers
--===========================================================================
function Trig_RiseDeadWorkers_Conditions()
    return GetUnitTypeId(GetSummonedUnit()) == FourCC('cD32')
end
function Trig_RiseDeadWorkers_Actions()
    IssueImmediateOrderBJ(GetSummonedUnit(), "autoharvestlumber")
end
--===========================================================================
function InitTrig_RiseDeadWorkers()
    gg_trg_RiseDeadWorkers=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RiseDeadWorkers, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_RiseDeadWorkers, Condition(Trig_RiseDeadWorkers_Conditions))
    TriggerAddAction(gg_trg_RiseDeadWorkers, Trig_RiseDeadWorkers_Actions)
end
--===========================================================================
-- Trigger: SummonCase
--===========================================================================
function Trig_SummonCase_Conditions()
    return GetUnitAbilityLevel(GetSummonedUnit(), FourCC('cDa6')) ~= 0 or GetUnitAbilityLevel(GetSummonedUnit(), FourCC('cDat')) ~= 0 and GetUnitTypeId(GetSummonedUnit()) ~= FourCC('cD32')
end
function Trig_SummonCase_Actions()
    local u= GetSummonedUnit()
    --call UnitRemoveTypeBJ( UNIT_TYPE_SUMMONED, GetSummonedUnit() )
    UnitAddAbility(u, FourCC('A1HL')) --?????? ?? ???????????
    --call AddCountDis(u, GetPlayerId(GetOwningPlayer(u)))
    
    
    -- ?????? ???? ? ???????
    if GetSummoningUnit() ~= nil then
        IssuePointOrder(u, "smart", GetUnitX(GetSummoningUnit()), GetUnitY(GetSummoningUnit()))
    end
    
    u=nil
    
    
end
--===========================================================================
function InitTrig_SummonCase()
    gg_trg_SummonCase=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SummonCase, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_SummonCase, Condition(Trig_SummonCase_Conditions))
    TriggerAddAction(gg_trg_SummonCase, Trig_SummonCase_Actions)
end
--===========================================================================
-- Trigger: UpgradeSkelets
--===========================================================================
function Trig_UpgradeSkelets_Conditions()
    return GetResearched() == FourCC('R0K4')
end
function Trig_UpgradeSkelets_Actions()
    local p= GetOwningPlayer(GetTriggerUnit())
    local lvl= GetPlayerTechCount(p, FourCC('R0K4'), true)
    
    if lvl == 1 then
        SetPlayerTechMaxAllowed(p, FourCC('cD19'), 0)
        SetPlayerTechMaxAllowed(p, FourCC('cD34'), - 1)
    elseif lvl == 2 then
        SetPlayerTechMaxAllowed(p, FourCC('cD34'), 0)
        SetPlayerTechMaxAllowed(p, FourCC('cD35'), - 1)
    end
    
end
--===========================================================================
function InitTrig_UpgradeSkelets()
    gg_trg_UpgradeSkelets=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UpgradeSkelets, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_UpgradeSkelets, Condition(Trig_UpgradeSkelets_Conditions))
    TriggerAddAction(gg_trg_UpgradeSkelets, Trig_UpgradeSkelets_Actions)
end
--===========================================================================
-- Trigger: MeatDeal
--===========================================================================
function Trig_Untitled_Trigger_003_Func001001003()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('cDa6')) > 0 and GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer and UnitAlive(GetFilterUnit())
end
function Trig_MeatDeal_Actions()
    local Boolexpr
    local caster= GetTriggerUnit()
    local target
    local eachUnit
    local g= CreateGroup()
    local healthMax
    local healthCurrent
    local id
    local p= GetOwningPlayer(caster)
    local Efficiency= 0.5 + GetPlayerTechCount(p, FourCC('cDR5'), true) * 0.05
    local count= 0
    udg_LocalPlayer=p
    GroupEnumUnitsInRangeCounted(g, GetSpellTargetX(), GetSpellTargetY(), 275, Boolexpr, 12)
    
    --if target == null then
        target=FirstOfGroup(g)
        id=GetUnitTypeId(target)
    --endif 
    
    if target == nil then
        
        DestroyGroup(g)
        DestroyBoolExpr(Boolexpr)
        Boolexpr=nil
        g=nil
        caster=nil
        target=nil
        eachUnit=nil
        return
    else
        healthMax=GetUnitState(target, UNIT_STATE_MAX_LIFE) * Efficiency
        healthCurrent=GetUnitState(target, UNIT_STATE_LIFE) * Efficiency
        GroupRemoveUnit(g, target)
        
        while true do
            eachUnit=FirstOfGroup(g)
            if eachUnit == nil or healthMax >= 5000 then break end
            GroupRemoveUnit(g, eachUnit)
            healthMax=healthMax + GetUnitState(eachUnit, UNIT_STATE_MAX_LIFE) * Efficiency
            healthCurrent=healthCurrent + GetUnitState(eachUnit, UNIT_STATE_LIFE) * Efficiency
            count=count + 1
            if eachUnit ~= target then
                DelCountDis(eachUnit , GetPlayerId(GetOwningPlayer(eachUnit)))
                
                RemoveUnit(eachUnit)
                RemoveEffectTimed(AddSpecialEffect("ObjectsSpawnmodelsNightElfEntBirthTargetEntBirthTarget.mdl", GetUnitX(eachUnit), GetUnitY(eachUnit)) , 2)
            end
            
        end
        
        
        
        if healthMax > 5000 then --????? ?? ?????
            if id ~= FourCC('cD00') then
                target=ReplaceUnit2(target , FourCC('cD00') , bj_UNIT_STATE_METHOD_RELATIVE)
            end
            
        
        elseif healthMax > 2500 and id ~= FourCC('cD09') then --?????? ?????
            
            if id ~= FourCC('cD09') or id ~= FourCC('cD14') then
                if Random(1 , 2) then
                    target=ReplaceUnit2(target , FourCC('cD14') , bj_UNIT_STATE_METHOD_RELATIVE)
                else
                    target=ReplaceUnit2(target , FourCC('cD09') , bj_UNIT_STATE_METHOD_RELATIVE)
                end
                
            end
            
        elseif healthMax > 1000 and id ~= FourCC('cD09') then --????????
            
            if id ~= FourCC('cD10') then
                target=ReplaceUnit2(target , FourCC('cD10') , bj_UNIT_STATE_METHOD_RELATIVE)
            end
        else
            
            BlzUnitCancelTimedLife(target)
            
            --call UnitApplyTimedLife( target, 'BTLF', 60)
        
        end
        
        
        --call UnitRemoveType(target, UNIT_TYPE_SUMMONED)
        RemoveEffectTimed(AddSpecialEffectTarget("NewEffects / SoulDischarge.mdx", target, "origin") , 2)
        BlzSetUnitMaxHP(target, IMinBJ(R2I(healthMax), 8000))
        SetUnitState(target, UNIT_STATE_LIFE, healthCurrent)
        --call AddCountDis(target,GetPlayerId(GetOwningPlayer(target)))
    end
    
    DestroyBoolExpr(Boolexpr)
    Boolexpr=nil
    DestroyGroup(g)
    g=nil
    caster=nil
    target=nil
    eachUnit=nil
end
--===========================================================================
function InitTrig_MeatDeal()
    gg_trg_MeatDeal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MeatDeal, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MeatDeal, function()
        if GetSpellAbilityId() ~= FourCC('cDa5') then return end
        Trig_MeatDeal_Actions()
    end)
end
--===========================================================================
-- Trigger: BoneDeal
--===========================================================================
function BoneCheck()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('cDat')) > 0 and GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer and UnitAlive(GetFilterUnit())
end
function Trig_BoneDeal_Actions()
    local Boolexpr
    local caster= GetTriggerUnit()
    local target
    local eachUnit
    local g= CreateGroup()
    local healthMax
    local healthCurrent
    local id
    local p= GetOwningPlayer(caster)
    local Efficiency= 0.5 + GetPlayerTechCount(p, FourCC('R0JH'), true) * 0.05
    local count= 0
    
    udg_LocalPlayer=p
    GroupEnumUnitsInRangeCounted(g, GetSpellTargetX(), GetSpellTargetY(), 275, Boolexpr, 12)
    
    --if target == null then
        target=FirstOfGroup(g)
        id=GetUnitTypeId(target)
    --endif 
    
    if target == nil then
        
        DestroyGroup(g)
        DestroyBoolExpr(Boolexpr)
        Boolexpr=nil
        g=nil
        caster=nil
        target=nil
        eachUnit=nil
        return
    else
        healthMax=GetUnitState(target, UNIT_STATE_MAX_LIFE) * Efficiency
        healthCurrent=GetUnitState(target, UNIT_STATE_LIFE) * Efficiency
        GroupRemoveUnit(g, target)
        
        while true do
            eachUnit=FirstOfGroup(g)
            if eachUnit == nil or healthMax >= 3500 then break end
            GroupRemoveUnit(g, eachUnit)
            healthMax=healthMax + GetUnitState(eachUnit, UNIT_STATE_MAX_LIFE) * Efficiency
            healthCurrent=healthCurrent + GetUnitState(eachUnit, UNIT_STATE_LIFE) * Efficiency
            count=count + 1
            if eachUnit ~= target then
                --call KillUnit(eachUnit)
                DelCountDis(eachUnit , GetPlayerId(GetOwningPlayer(eachUnit)))
                RemoveUnit(eachUnit)
                RemoveEffectTimed(AddSpecialEffect("NewEffects / FlareStampedeMissileDeath.mdx", GetUnitX(eachUnit), GetUnitY(eachUnit)) , 2)
            end
            
        end
        
        
        
        if healthMax > 2500 then --????? ?? ??????
            if id ~= FourCC('cD23') then
                target=ReplaceUnit2(target , FourCC('cD23') , bj_UNIT_STATE_METHOD_RELATIVE)
                IssueImmediateOrder(target, "Locustswarm")
            end
            
            
        elseif healthMax > 1250 and id ~= FourCC('cD09') then --????? ??? ??????????
            
            if id ~= FourCC('cD33') or id ~= FourCC('cD18') then
                if Random(1 , 2) then
                    target=ReplaceUnit2(target , FourCC('cD18') , bj_UNIT_STATE_METHOD_RELATIVE)
                else
                    target=ReplaceUnit2(target , FourCC('cD33') , bj_UNIT_STATE_METHOD_RELATIVE)
                end
                
            end
            
        else
            BlzUnitCancelTimedLife(target)
            --call UnitApplyTimedLife( target, 'BTLF', 60)
        end
        
        --call UnitRemoveType(target, UNIT_TYPE_SUMMONED)
        RemoveEffectTimed(AddSpecialEffectTarget("NewEffects / SoulDischargePurple.mdx", target, "origin") , 2)
        BlzSetUnitMaxHP(target, IMinBJ(R2I(healthMax), 3500))
        SetUnitState(target, UNIT_STATE_LIFE, healthCurrent)
        --call UnitAddType(target, UNIT_TYPE_SUMMONED)
        --call AddCountDis(target,GetPlayerId(GetOwningPlayer(target)))
    end
    
    DestroyBoolExpr(Boolexpr)
    Boolexpr=nil
    DestroyGroup(g)
    g=nil
    caster=nil
    target=nil
    eachUnit=nil
end
--===========================================================================
function InitTrig_BoneDeal()
    gg_trg_BoneDeal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BoneDeal, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_BoneDeal, function()
        if GetSpellAbilityId() ~= FourCC('cDar') then return end
        Trig_BoneDeal_Actions()
    end)
end
--===========================================================================
-- Trigger: HealWhenRise
--===========================================================================
function Trig_HealWhenRise_Conditions()
end
function Trig_HealWhenRise_Actions()
    SetUnitLifeBJ(GetTriggerUnit(), GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) + 15)
    SetUnitManaBJ(GetTriggerUnit(), GetUnitStateSwap(UNIT_STATE_MANA, GetTriggerUnit()) + 5)
end
--===========================================================================
function InitTrig_HealWhenRise()
    gg_trg_HealWhenRise=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_HealWhenRise, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_HealWhenRise, function()
        if GetSpellAbilityId() ~= FourCC('cDa2') then return end
        if not Trig_HealWhenRise_Conditions() then return end
        Trig_HealWhenRise_Actions()
    end)
end
--===========================================================================
-- Trigger: ZombyTrain
--===========================================================================
function Trig_ZombyTrain_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('cD11') or GetUnitTypeId(GetTrainedUnit()) == FourCC('cD11')
end
function Trig_ZombyTrain_Actions()
    local u= GetTrainedUnit()
    IssueTargetOrder(CreateUnit(GetOwningPlayer(u), FourCC('cD11'), GetUnitX(u), GetUnitY(u), 0.00), "smart", u)
    u=nil
end
--===========================================================================
function InitTrig_ZombyTrain()
    gg_trg_ZombyTrain=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZombyTrain, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_ZombyTrain, Condition(Trig_ZombyTrain_Conditions))
    TriggerAddAction(gg_trg_ZombyTrain, Trig_ZombyTrain_Actions)
end
--===========================================================================
-- Trigger: BuildFleCitadel
--===========================================================================
function Trig_BuildFleCitadel_Conditions()
    return ( GetUnitTypeId(GetConstructedStructure()) == FourCC('cD12') )
end
function Trig_BuildFleCitadel_Actions()
    IssueImmediateOrderBJ(GetConstructedStructure(), "windwalk")
    IssueImmediateOrderBJ(GetConstructedStructure(), "replenishlifeon")
    BlzStartUnitAbilityCooldown(GetConstructedStructure(), FourCC('A1HC'), 45.00)
end
--===========================================================================
function InitTrig_BuildFleCitadel()
    gg_trg_BuildFleCitadel=CreateTrigger()
    DisableTrigger(gg_trg_BuildFleCitadel)
    TriggerRegisterAnyUnitEventBJ(gg_trg_BuildFleCitadel, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_BuildFleCitadel, Condition(Trig_BuildFleCitadel_Conditions))
    TriggerAddAction(gg_trg_BuildFleCitadel, Trig_BuildFleCitadel_Actions)
end
--===========================================================================
-- Trigger: PoisonGolemDesease
--===========================================================================
function Trig_PoisonGolemDesease_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('cDay')) > 0 and BlzGetEventAttackType() == ATTACK_TYPE_CHAOS --and GetUnitAbilityLevel(GetEventDamageSource(), FourCC('cDay') )
end
function Trig_PoisonGolemDesease_Actions()
        local u2= CreateUnit(GetOwningPlayer(GetEventDamageSource()), FourCC('h05P'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), bj_UNIT_FACING)
        
        UnitAddAbility(u2, FourCC('cDau'))
        IssueTargetOrder(u2, "parasite", GetTriggerUnit())
        RemoveUnitTimed(u2 , 2)
        u2=nil
end
--===========================================================================
function InitTrig_PoisonGolemDesease()
    gg_trg_PoisonGolemDesease=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PoisonGolemDesease, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_PoisonGolemDesease, Condition(Trig_PoisonGolemDesease_Conditions))
    TriggerAddAction(gg_trg_PoisonGolemDesease, Trig_PoisonGolemDesease_Actions)
end
--===========================================================================
-- Trigger: ZombyDesease
--===========================================================================
function Trig_ZombyDesease_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A1HO')) > 0 and BlzGetEventAttackType() == ATTACK_TYPE_MELEE --and GetUnitAbilityLevel(GetEventDamageSource(), FourCC('cDay') )
end
function Trig_ZombyDesease_Actions()
        local u2
        
        if Random(1 , 3) then
            u2=CreateUnit(GetOwningPlayer(GetEventDamageSource()), FourCC('h05P'), GetUnitX(GetTriggerUnit()), GetUnitY(GetTriggerUnit()), bj_UNIT_FACING)
            UnitAddAbility(u2, FourCC('cDau'))
            IssueTargetOrder(u2, "parasite", GetTriggerUnit())
            RemoveUnitTimed(u2 , 2)
        
        end
        
        u2=nil
end
--===========================================================================
function InitTrig_ZombyDesease()
    gg_trg_ZombyDesease=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZombyDesease, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_ZombyDesease, Condition(Trig_ZombyDesease_Conditions))
    TriggerAddAction(gg_trg_ZombyDesease, Trig_ZombyDesease_Actions)
end
--===========================================================================
-- Trigger: Overcharge
--===========================================================================
function Trig_Overcharge_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('A1HB'))
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A1HB') , 22)
end
--===========================================================================
function InitTrig_Overcharge()
    gg_trg_Overcharge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Overcharge, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Overcharge, function()
        if GetSpellAbilityId() ~= FourCC('A1HC') then return end
        Trig_Overcharge_Actions()
    end)
end
--===========================================================================
-- Trigger: NoAutoSkeletsButton
--===========================================================================
function Trig_NoAutoSkeletsButton_Actions()
    local lvl= GetUnitAbilityLevel(GetTriggerUnit(), FourCC('cDAZ'))
    if lvl == 1 then
        SetUnitAbilityLevel(GetTriggerUnit(), FourCC('cDAZ'), 2)
    else
        SetUnitAbilityLevel(GetTriggerUnit(), FourCC('cDAZ'), 1)
    end
end
--===========================================================================
function InitTrig_NoAutoSkeletsButton()
    gg_trg_NoAutoSkeletsButton=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NoAutoSkeletsButton, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_NoAutoSkeletsButton, function()
        if GetSpellAbilityId() ~= FourCC('cDAZ') then return end
        Trig_NoAutoSkeletsButton_Actions()
    end)
end
--===========================================================================
-- Trigger: ChangeAutoWorkers
--===========================================================================
function Trig_ChangeAutoWorkers_Actions()
    local u= GetTriggerUnit()
    local lvl= GetUnitAbilityLevel(u, FourCC('A1L9'))
    if lvl == 1 then
        SetUnitAbilityLevel(u, FourCC('A1L9'), 2)
        UnitAddAbility(u, FourCC('cDA9'))
        UnitRemoveAbility(u, FourCC('cDa4'))
        BlzStartUnitAbilityCooldown(u, FourCC('cDA9'), 30)
    else
        SetUnitAbilityLevel(u, FourCC('A1L9'), 1)
        UnitAddAbility(u, FourCC('cDa4'))
        UnitRemoveAbility(u, FourCC('cDA9'))
        BlzStartUnitAbilityCooldown(u, FourCC('cDa4'), 30)
    end
    IssueImmediateOrder(u, "raisedeadon")
    u=nil
end
--===========================================================================
function InitTrig_ChangeAutoWorkers()
    gg_trg_ChangeAutoWorkers=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ChangeAutoWorkers, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ChangeAutoWorkers, function()
        if GetSpellAbilityId() ~= FourCC('A1L9') then return end
        Trig_ChangeAutoWorkers_Actions()
    end)
end
--===========================================================================
-- Trigger: UnitTrainedNoSkelets
--===========================================================================
function Trig_UnitTrainedNoSkelets_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('cDAZ')) == 2
end
function Trig_UnitTrainedNoSkelets_Actions()
    IssueImmediateOrder(GetTrainedUnit(), "raisedeadoff")
end
--===========================================================================
function InitTrig_UnitTrainedNoSkelets()
    gg_trg_UnitTrainedNoSkelets=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UnitTrainedNoSkelets, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_UnitTrainedNoSkelets, Condition(Trig_UnitTrainedNoSkelets_Conditions))
    TriggerAddAction(gg_trg_UnitTrainedNoSkelets, Trig_UnitTrainedNoSkelets_Actions)
end
--===========================================================================
-- Trigger: MassIceArrow
--===========================================================================
function Trig_MassIceArrow_Actions()
    local l= GetSpellTargetLoc()
    local p= GetOwningPlayer(GetTriggerUnit())
    local bex
    local dammyAbility= FourCC('A1HF')
    local level= GetUnitAbilityLevel(GetTriggerUnit(), GetSpellAbilityId())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = EnemEl
    GroupEnumUnitsInRangeOfLoc(g, l, 150, bex)
    
    if FirstOfGroup(g) == nil then
        --???? ??????
        BlzStartUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1HE'), 14)
        SetUnitState(GetTriggerUnit(), UNIT_STATE_MANA, GetUnitState(GetTriggerUnit(), UNIT_STATE_MANA) + 100 + 35 * level)
        
    
    else
        RemoveLocation(l)
        l=GetUnitLoc(GetTriggerUnit())
        while true do
            u=FirstOfGroup(g)
            if u == nil then break end
            
            u2=CreateUnitAtLoc(p, FourCC('h05P'), l, bj_UNIT_FACING)
            
            UnitAddAbility(u2, dammyAbility)
            SetUnitAbilityLevel(u2, dammyAbility, level)
            IssueTargetOrder(u2, "thunderbolt", u)
            RemoveUnitTimed(u2 , 2)
            i=i + 1
            GroupRemoveUnit(g, u)
        end
    end
    
    u=nil
    DestroyGroup(g)
    g=nil
    RemoveLocation(l)
    p=nil
    u2=nil
    bex=nil
end
--===========================================================================
function InitTrig_MassIceArrow()
    gg_trg_MassIceArrow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassIceArrow, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassIceArrow, function()
        if GetSpellAbilityId() ~= FourCC('A1HE') then return end
        Trig_MassIceArrow_Actions()
    end)
end
--===========================================================================
-- Trigger: UsePorcha
--===========================================================================
function Trig_UsePorcha_Conditions()
    return GetUnitAbilityLevel(GetAttacker(), FourCC('cDa0')) > 0 and BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC('cDa0')) <= 0
end
function Trig_UsePorcha_Actions()
    DummyCastTarget(FourCC('cDa0') , "shadowstrike" , GetAttacker() , GetTriggerUnit())
    BlzStartUnitAbilityCooldown(GetAttacker(), FourCC('cDa0'), 15)
    --call IssueTargetOrderBJ( GetAttacker(), "shadowstrike", GetAttackedUnitBJ() )
end
--===========================================================================
function InitTrig_UsePorcha()
    gg_trg_UsePorcha=CreateTrigger()
    DisableTrigger(gg_trg_UsePorcha)
    TriggerRegisterAnyUnitEventBJ(gg_trg_UsePorcha, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_UsePorcha, Condition(Trig_UsePorcha_Conditions))
    TriggerAddAction(gg_trg_UsePorcha, Trig_UsePorcha_Actions)
end
--===========================================================================
-- Trigger: PlagueOnBuilding
--===========================================================================
function Plague()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local time= LoadInteger(Hash, id, 1)
    local e
    local u= LoadUnitHandle(Hash, id, 0)
    --??????
    if time == 0 and UnitAlive(u) and u ~= nil then
        UnitAddAbility(u, FourCC('A1HS'))
        e=AddSpecialEffectTargetUnitBJ("overhead", u, "CultOfDamnedPlagueCloudTargetLight.mdx")
        SaveEffectHandle(Hash, id, 2, e)
        
    --??????
    elseif time < 30 and UnitAlive(u) and u ~= nil then
        SaveInteger(Hash, id, 1, time + 1)
        
    --?????
    else
        if UnitAlive(u) then
            income[LoadInteger(Hash, GetHandleId(u), 0)]=income[LoadInteger(Hash, GetHandleId(u), 0)] - 5
            income[GetPlayerId(GetOwningPlayer(u))]=income[GetPlayerId(GetOwningPlayer(u))] + 5
        end
        UnitRemoveAbility(u, FourCC('A1HS'))
        DestroyEffect(LoadEffectHandle(Hash, id, 2))
        PauseTimer(t)
        DestroyTimer(t)
        FlushChildHashtable(Hash, id)
    
    end
    e=nil
    t=nil
    u=nil
end
function Trig_PlagueOnBuilding_Actions()
    local t= CreateTimer()
    local id= GetHandleId(t)
    local u= GetSpellTargetUnit()
    if u ~= nil then
        if GetUnitAbilityLevel(u, FourCC('A1HS')) < 1 and IsPlayerEnemy(GetOwningPlayer(u), GetOwningPlayer(GetTriggerUnit())) then
            --??????
            
            if GetUnitFoodMade(u) > 0 then
                income[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))]=income[GetPlayerId(GetOwningPlayer(GetTriggerUnit()))] + 5
                income[GetPlayerId(GetOwningPlayer(u))]=income[GetPlayerId(GetOwningPlayer(u))] - 5
            end
            
            SaveInteger(Hash, GetHandleId(u), 0, GetPlayerId(GetOwningPlayer(GetTriggerUnit())))
            SaveUnitHandle(Hash, id, 0, u)
            SaveInteger(Hash, id, 1, 0)
            TimerStart(t, 1.00, true, Plague)
        else
            --????????
            SaveInteger(Hash, id, 1, 1)
        
        end
    end
    t=nil
    
end
--===========================================================================
function InitTrig_PlagueOnBuilding()
    gg_trg_PlagueOnBuilding=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PlagueOnBuilding, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_PlagueOnBuilding, function()
        if GetSpellAbilityId() ~= FourCC('A1HR') then return end
        Trig_PlagueOnBuilding_Actions()
    end)
end
--===========================================================================
-- Trigger: UnitTrained
--===========================================================================
function Trig_UnitTrained_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1HS')) > 0
end
function Trig_UnitTrained_Actions()
    local u2
    local id=  LoadInteger(Hash, GetHandleId(GetTriggerUnit()), 0)
    
    u2=CreateUnit(Player(id), FourCC('h05P'), GetUnitX(GetTrainedUnit()), GetUnitY(GetTrainedUnit()), bj_UNIT_FACING)
    UnitAddAbility(u2, FourCC('cDau'))
    IssueTargetOrder(u2, "parasite", GetTrainedUnit())
    RemoveUnitTimed(u2 , 2)
    
        
    
    u2=nil
end
--===========================================================================
function InitTrig_UnitTrained()
    gg_trg_UnitTrained=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UnitTrained, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_UnitTrained, Condition(Trig_UnitTrained_Conditions))
    TriggerAddAction(gg_trg_UnitTrained, Trig_UnitTrained_Actions)
end
--===========================================================================
-- Trigger: InfestBuilding
--===========================================================================
function Trig_InfestBuilding_Actions()
    local u= GetSpellTargetUnit()
    if GetUnitLifePercent(u) <= 10 and u ~= nil and IsPlayerEnemy(GetOwningPlayer(u), GetOwningPlayer(GetTriggerUnit())) then
        KillUnit(u)
        CreateUnit(GetOwningPlayer(GetTriggerUnit()), FourCC('u02Z'), GetUnitX(u), GetUnitY(u), 0.0)
        
    
    end
  
    
    
    u=nil
    
    
    
    
end
--===========================================================================
function InitTrig_InfestBuilding()
    gg_trg_InfestBuilding=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_InfestBuilding, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_InfestBuilding, function()
        if GetSpellAbilityId() ~= FourCC('A1JC') then return end
        if not (not IsUnitInGroup(GetSpellTargetUnit(), udg_StolicaGroups)) then return end
        Trig_InfestBuilding_Actions()
    end)
end
--===========================================================================
-- Trigger: StartForestTrolls
--===========================================================================
function ForestStart()
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('o05N'), 3, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o05M'), 3, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('o05O'), 3, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('O056'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O057'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O058'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O059'), 1, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('o04Y'), 0, GetEnumPlayer())
    
end
function Trig_StartForestTrolls_Actions()
    ForForce(udg_AllPlayers, ForestStart)
end
--===========================================================================
function InitTrig_StartForestTrolls()
    gg_trg_StartForestTrolls=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartForestTrolls, 0.01)
    TriggerAddAction(gg_trg_StartForestTrolls, Trig_StartForestTrolls_Actions)
end
--===========================================================================
-- Trigger: Charge
--===========================================================================
--//================================================================================================================================================================================
--// ???? 3 - ??????? ??????
--//================
--function Trig_JumpSTR_move_units takes nothing returns nothing
--    local timer t = GetExpiredTimer()
--    local integer h = GetHandleId(t)
--    local unit un = LoadUnitHandle(Hash,h,1)
--    local real ugol = LoadReal(Hash,h,2)
--    local integer kol = LoadInteger(Hash,h,3)
--    local real x = GetUnitX(un)
--    local real y = GetUnitY(un)
--    // ---------
--    set x = x + 10 * Cos(ugol * bj_DEGTORAD) //????????? ????????? ?
--    set y = y + 10 * Sin(ugol * bj_DEGTORAD) //????????? ????????? ?
--    if kol >= 0 and not IsTerrainPathable(x, y, PATHING_TYPE_FLYABILITY) then
--        call SetUnitX(un,x)
--        call SetUnitY(un,y)
--        call SaveInteger(Hash, h, 3, kol-1)
--    else
--        call DestroyTimer(t)
--        call FlushChildHashtable(Hash,h)
--    endif
--    // ----------
--    set un = null
--    set t = null
--endfunction
--================================================================================================================================================================================
-- ???? 2 - ??????? ?????
--================
function Trig_Charge_move_hero()
    local t= GetExpiredTimer()
    local h= GetHandleId(t)
    local GT= LoadUnitHandle(Hash, h, 1)
    local l= LoadReal(Hash, h, 2)
    local g
    local x1= LoadReal(Hash, h, 4)
    local y1= LoadReal(Hash, h, 5)
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
    x=dx + 25 * Cos(ugol * bj_DEGTORAD) --????????? ????????? ?
    y=dy + 25 * Sin(ugol * bj_DEGTORAD) --????????? ????????? ?
    w=JSTRParabolaZ(MaxW , l , JSTRRastMT(x , x1 , y , y1)) --????????? ??????
    
    -- ???? ????? ????
    if JSTRRastMT(x1 , dx , y1 , dy) > 25 then --and not IsTerrainPathable(x, y, PATHING_TYPE_WALKABILITY) then
        -- ??????? ?????
        SetUnitX(GT, x)
        SetUnitY(GT, y)
        SetUnitFacing(GT, ugol)
        --call SetUnitFlyHeight(GT, w, 0)
    else
        DestroyEffect(LoadEffectHandle(Hash, h, 6))
        DestroyTimer(t)
        FlushChildHashtable(Hash, h)
        SetUnitAnimation(GT, "attack")
        --call SetUnitFlyHeight(GT, 0, 0)
        DestroyEffect(AddSpecialEffect("AbilitiesSpellsOrcWarStompWarStompCaster.mdl", dx, dy))
        g=CreateGroup()
        GroupEnumUnitsInRange(g, dx, dy, 260, nil)
        while true do
            un=FirstOfGroup(g)
            if un == nil then break end
            lvl=GetUnitAbilityLevel(GT, JSTRSkill)
            
            -- ????? - ???????? ?? ?????
            if IsUnitType(GT, UNIT_TYPE_HERO) then
                uron=JSTRKofDmg1 * lvl * GetHeroStr(GT, true) + lvl * JSTRKofDmg2
            else
                uron=lvl * JSTRKofDmg2 * 4
            end
            
            if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) then
                UnitDamageTarget(GT, un, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
                DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsOrcMirrorImageMirrorImageDeathCaster.mdl", un, "orign"))
                ----------
                -- ??????? ????? ? ?????? ??????? ?? ???????
                if JSTRBoolMove then
                    ugol=JSTRUgolMT(dx , GetUnitX(un) , dy , GetUnitY(un))
                    t1=CreateTimer()
                    h1=GetHandleId(t1)
                    SaveUnitHandle(Hash, h1, 1, un)
                    SaveReal(Hash, h1, 2, ugol)
                    SaveInteger(Hash, h1, 3, 17)
                    TimerStart(t1, 0.015, true, Trig_JumpSTR_move_units)
                end
                ---------- 
            end
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
function Trig_Charge_Actions()
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
    --call DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    TimerStart(t, 0.025, true, Trig_Charge_move_hero) --???????? ???????? ?????
    ---------
    GT=nil
    --set g = null
    t=nil
end
--===========================================================================
function InitTrig_Charge()
    gg_trg_Charge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Charge, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Charge, function()
        if GetSpellAbilityId() ~= FourCC('A1H3') then return end
        Trig_Charge_Actions()
    end)
end
--===========================================================================
-- Trigger: SetLifeNormal
--===========================================================================
function Trig_SetLifeNormal_Conditions()
    return GetUnitStateSwap(UNIT_STATE_LIFE, GetTriggerUnit()) - GetEventDamage() < 5 and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1G6')) ~= 0
end
function Trig_SetLifeNormal_Actions()
   
    SetUnitLifeBJ(GetTriggerUnit(), ( 3.00 + GetEventDamage() ))
end
--===========================================================================
function InitTrig_SetLifeNormal()
    gg_trg_SetLifeNormal=CreateTrigger()
    
    --call TriggerRegisterAnyUnitEventBJ( gg_trg_SetLifeNormal, EVENT_PLAYER_UNIT_DAMAGING )
    TriggerAddCondition(gg_trg_SetLifeNormal, Condition(Trig_SetLifeNormal_Conditions))
    TriggerAddAction(gg_trg_SetLifeNormal, Trig_SetLifeNormal_Actions)
end
function Trig_ZacliatieOfLive_Actions()
    local u= GetTriggerUnit()
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    UnitAddAbility(u, FourCC('A1G6'))
    TriggerRegisterUnitEvent(gg_trg_SetLifeNormal, u, EVENT_UNIT_DAMAGING)
	local t = CreateTimer()
	TimerStart(t, 15 * GetUnitAbilityLevel(u, FourCC('A1G6')), false, function()
		UnitRemoveAbility(u, FourCC('A1G6'))
		DestroyTimer(t)
	end)
    
    u=nil
    t=nil
end
--===========================================================================
function InitTrig_ZacliatieOfLive()
    gg_trg_ZacliatieOfLive=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZacliatieOfLive, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_ZacliatieOfLive, function()
        if GetSpellAbilityId() ~= FourCC('A1G5') then return end
        Trig_ZacliatieOfLive_Actions()
    end)
end
--===========================================================================
-- Trigger: ReturnDamage
--===========================================================================
function Trig_ReturnDamage_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1GQ')) > 0
end
function Trig_ReturnDamage_Actions()
    local u= GetTriggerUnit()
    local u2= nil
    local g= CreateGroup()
    local b
    local l
    local damage= GetEventDamage() * 1.30
    DisableTrigger(GetTriggeringTrigger())
    udg_LocalPlayer=GetOwningPlayer(u)
    udg_LocalInteger2=0
    GroupEnumUnitsInRange(g, GetUnitX(u), GetUnitY(u), 550, b)
   -- set u2 = FirstOfGroup(g) 
    if udg_LocalInteger2 > 0 then
        u2=BlzGroupUnitAt(g, GetRandomInt(0, udg_LocalInteger2 - 1))
        if u2 ~= nil and UnitAlive(u2) and u ~= u2 then
            SetUnitLifeBJ(u, GetUnitState(u, UNIT_STATE_LIFE) + damage)
            UnitDamageTargetBJ(u, u2, damage, ATTACK_TYPE_HERO, DAMAGE_TYPE_DEATH)
            l=AddLightning("MFPB", true, GetUnitX(u), GetUnitY(u), GetUnitX(u2), GetUnitY(u2))
            RemoveLigtingTimed(l , 0.9)
            
        end
    end
    DestroyGroup(g)
    DestroyBoolExpr(b)
    g=nil
    b=nil
    l=nil
    u=nil
    u2=nil
    
    EnableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_ReturnDamage()
    gg_trg_ReturnDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ReturnDamage, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_ReturnDamage, Condition(Trig_ReturnDamage_Conditions))
    TriggerAddAction(gg_trg_ReturnDamage, Trig_ReturnDamage_Actions)
end
--===========================================================================
-- Trigger: ZacliatieOfDamage
--===========================================================================
function Trig_ZacliatieOfDamage_Actions()
    local u= GetTriggerUnit()
    
    UnitAddAbility(u, FourCC('A1GQ'))
    RemoveAbilityTimed(u , FourCC('A1GQ') , GetUnitAbilityLevel(u, FourCC('A1GP')) * 20)
    u=nil
end
--===========================================================================
function InitTrig_ZacliatieOfDamage()
    gg_trg_ZacliatieOfDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ZacliatieOfDamage, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_ZacliatieOfDamage, function()
        if GetSpellAbilityId() ~= FourCC('A1GP') then return end
        Trig_ZacliatieOfDamage_Actions()
    end)
end
--===========================================================================
-- Trigger: YarostBeg
--===========================================================================
function Trig_YarostBeg_Actions()
    local u= GetTriggerUnit()
    
    SetUnitLifePercentBJ(u, GetUnitLifePercent(u) * 0.75)
    
    UnitAddAbility(u, FourCC('A1GS')) -- ?????? ?? ????
    RemoveAbilityTimed(u , FourCC('A1GS') , 24.5)
    --call UnitAddAbility(u,'A1G2')
    --call BlzStartUnitAbilityCooldown(u,'A1G2',1)
    --call BlzUnitHideAbility(u,'A1F9',true)
    RemoveAbilityTimed(u , FourCC('A1GS') , 25)
    
    u=nil
end
--===========================================================================
function InitTrig_YarostBeg()
    gg_trg_YarostBeg=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_YarostBeg, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_YarostBeg, function()
        if GetSpellAbilityId() ~= FourCC('A1F9') then return end
        Trig_YarostBeg_Actions()
    end)
end
--===========================================================================
-- Trigger: RitualPoglocenia
--===========================================================================
function Trig_RitualPoglocenia_Actions()
   --local unit u = GetTriggerUnit()
    local u2= GetSpellTargetUnit()
    local id= GetUnitTypeId(u2)
    
    
    --????
    if id == FourCC('o052') or id == FourCC('o051') then
        u2=ReplaceUnit2(u2 , FourCC('o05O') , bj_UNIT_STATE_METHOD_RELATIVE)
        
    --?????
    elseif id == FourCC('o04Z') or id == FourCC('o04X') or id == FourCC('o04V') or id == FourCC('o050') then
        u2=ReplaceUnit2(u2 , FourCC('o05M') , bj_UNIT_STATE_METHOD_RELATIVE)
    --??
    elseif id == FourCC('o04W') or id == FourCC('o04Y') or id == FourCC('o053') then
        u2=ReplaceUnit2(u2 , FourCC('o05N') , bj_UNIT_STATE_METHOD_RELATIVE)
    else
        KillUnit(u2)
    end
    
    UnitAddAbility(u2, FourCC('A0Z5'))
    
    u2=nil
end
--===========================================================================
function InitTrig_RitualPoglocenia()
    gg_trg_RitualPoglocenia=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RitualPoglocenia, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_RitualPoglocenia, function()
        if GetSpellAbilityId() ~= FourCC('A1GA') then return end
        if not (GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC('A1F9')) > 0 and not IsUnitType(GetSpellTargetUnit(), UNIT_TYPE_HERO)) then return end
        Trig_RitualPoglocenia_Actions()
    end)
end
--===========================================================================
-- Trigger: WantAxe
--===========================================================================
function Trig_WantAxe_Conditions()
    --call DisplayTextToPlayer(Player(0),0,0,"2")
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A1G3')) > 0 and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1G4')) == 0 and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_WantAxe_Actions()
    local u= GetEventDamageSource()
    local u2= GetTriggerUnit()
    local t= CreateTimer()
    local id= GetHandleId(t)
    --call DisplayTextToPlayer(Player(0),0,0,"2"+GetUnitName(u2))
     
    UnitAddAbility(u2, FourCC('A1G4'))
    
	local t = CreateTimer()
	TimerStart(t, 7, false, function()
		UnitRemoveAbility(u2, FourCC('A1G4'))
		DestroyTimer(t)
	end)
    
    u=nil
    u2=nil
    t=nil
end
--===========================================================================
function InitTrig_WantAxe()
    gg_trg_WantAxe=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_WantAxe, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_WantAxe, Condition(Trig_WantAxe_Conditions))
    TriggerAddAction(gg_trg_WantAxe, Trig_WantAxe_Actions)
end
--===========================================================================
-- Trigger: BeFaster
--===========================================================================
function Trig_BeFaster_Conditions()
    
    return GetUnitAbilityLevel(BlzGetEventDamageTarget(), FourCC('A1F9')) > 0 or GetUnitAbilityLevel(BlzGetEventDamageTarget(), FourCC('A1G2')) > 0 -- ??? ?????? ??????
    
    
end
function Trig_BeFaster_Actions()
    local u= BlzGetEventDamageTarget()
    local spellid= FourCC('A1F8')
    local timerspellid= FourCC('A1CX')
    local lifep= GetUnitLifePercent(u)
    local time= 10
    
    
    --call DisplayTextToPlayer(Player(0),0,0,"")
    if lifep <= 30 then
        UnitAddAbility(u, spellid)
        SetUnitAbilityLevel(u, spellid, 4)
        BlzStartUnitAbilityCooldown(u, timerspellid, 20)
       -- call DisplayTextToPlayer(Player(0),0,0,"25"+R2S(lifep))
    elseif lifep <= 50 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 3)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))   
    elseif lifep <= 70 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 2)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))
    elseif lifep <= 90 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 1)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))
                
    else
            UnitRemoveAbility(u, spellid)
       --     call DisplayTextToPlayer(Player(0),0,0,""+R2S(lifep))
    end
    UnitAddAbility(u, timerspellid)
    BlzStartUnitAbilityCooldown(u, timerspellid, time)
    TriggerSleepAction(time)
    
    if BlzGetUnitAbilityCooldownRemaining(u, timerspellid) == 0 then
        UnitRemoveAbility(u, spellid)
    end
    
    
    
    u=nil
end
--===========================================================================
function InitTrig_BeFaster()
    gg_trg_BeFaster=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BeFaster, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_BeFaster, Condition(Trig_BeFaster_Conditions))
    TriggerAddAction(gg_trg_BeFaster, Trig_BeFaster_Actions)
end
--===========================================================================
-- Trigger: MassSetca
--===========================================================================
function Trig_MassSetca_Actions()
    local l= GetSpellTargetLoc()
    local p= GetOwningPlayer(GetTriggerUnit())
    local bex
    local dammyAbility= FourCC('A1FD')
    local level= GetUnitAbilityLevel(GetTriggerUnit(), GetSpellAbilityId())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = EnemEl
    GroupEnumUnitsInRangeOfLoc(g, l, 100 + 45 * level, bex)
    
    RemoveLocation(l)
    l=GetUnitLoc(GetTriggerUnit())
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        u2=CreateUnitAtLoc(p, FourCC('H0BN'), l, bj_UNIT_FACING)
        udg_LocalUnit2=u2
        TriggerExecute(gg_trg_ToKill2)
        UnitAddAbility(u2, dammyAbility)
        SetUnitManaBJ(u2, 1111111.00)
        SetUnitAbilityLevel(u2, dammyAbility, level)
        IssueTargetOrder(u2, "ensnare", u)
        
        i=i + 1
        GroupRemoveUnit(g, u)
    end
    
    
    u=nil
    DestroyGroup(g)
    g=nil
    RemoveLocation(l)
    p=nil
    u2=nil
    bex=nil
end
--===========================================================================
function InitTrig_MassSetca()
    gg_trg_MassSetca=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassSetca, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassSetca, function()
        if GetSpellAbilityId() ~= FourCC('A1FC') then return end
        Trig_MassSetca_Actions()
    end)
end
--===========================================================================
-- Trigger: MassFrenzy
--===========================================================================
function FFrenzy()
    return GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer and GetUnitAbilityLevel(GetFilterUnit(), FourCC('BUhf')) == 0 and not IsUnitType(GetFilterUnit(), UNIT_TYPE_MECHANICAL) and not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE)
    
end
function Trig_MassFrenzy_Actions()
    local l= GetUnitLoc(GetTriggerUnit())
    local p= GetOwningPlayer(GetTriggerUnit())
    
    local bex
    
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = FFrenzy
    GroupEnumUnitsInRangeOfLocCounted(g, l, 400, bex, 4)
    
    RemoveLocation(l)
    l=GetUnitLoc(GetTriggerUnit())
    while true do
        u=FirstOfGroup(g)
        if i > 4 or u == nil then break end
        
        u2=CreateUnitAtLoc(p, FourCC('h05P'), l, bj_UNIT_FACING)
        
        
        UnitAddAbility(u2, FourCC('A1FA'))
        SetUnitManaBJ(u2, 1111111.00)
        
        IssueTargetOrder(u2, "unholyfrenzy", u)
        
        i=i + 1
        RemoveUnitTimed(u2 , 2)
        GroupRemoveUnit(g, u)
    end
    
    
    u=nil
    DestroyGroup(g)
    g=nil
    RemoveLocation(l)
    p=nil
    u2=nil
    bex=nil
end
--===========================================================================
function InitTrig_MassFrenzy()
    gg_trg_MassFrenzy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassFrenzy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassFrenzy, function()
        if GetSpellAbilityId() ~= FourCC('A1ID') then return end
        Trig_MassFrenzy_Actions()
    end)
end
--===========================================================================
-- Trigger: StartJungleTrools
--===========================================================================
function Trig_StartJungleTrools_Func001A()
    SetPlayerTechMaxAllowedSwap(FourCC('O05B'), 1, GetEnumPlayer())
    
    SetPlayerTechMaxAllowedSwap(FourCC('O05A'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O05D'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O055'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O054'), 1, GetEnumPlayer())
    
    --Black spear
    SetPlayerTechMaxAllowedSwap(FourCC('o04P'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O05L'), 0, GetEnumPlayer())
    
    --Gurubashy
    SetPlayerTechMaxAllowedSwap(FourCC('o04N'), 0, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('O055'), 0, GetEnumPlayer())
    
    --call SetPlayerTechMaxAllowedSwap( 'A1DN', 0, GetEnumPlayer() )
    
    SetPlayerTechMaxAllowedSwap(FourCC('A1EP'), 1, GetEnumPlayer())
    SetPlayerTechMaxAllowedSwap(FourCC('A1EQ'), 1, GetEnumPlayer())
    
end
function Trig_StartJungleTrools_Actions()
    ForForce(udg_AllPlayers, Trig_StartJungleTrools_Func001A)
end
--===========================================================================
function InitTrig_StartJungleTrools()
    gg_trg_StartJungleTrools=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_StartJungleTrools, 0.01)
    TriggerAddAction(gg_trg_StartJungleTrools, Trig_StartJungleTrools_Actions)
end
--===========================================================================
-- Trigger: BlackSpear
--===========================================================================
function BlackSpear_Conditions()
    return GetSpellAbilityId() == FourCC('A1EP')
end
function BlackSpear_Actions()
    
    --Black spear
    SetPlayerTechMaxAllowedSwap(FourCC('o04P'), - 1, GetOwningPlayer(GetTriggerUnit())) -- ????
    SetPlayerTechMaxAllowedSwap(FourCC('O05L'), 1, GetOwningPlayer(GetTriggerUnit())) --????
    
    SetPlayerAbilityAvailableBJ(false, FourCC('A1EP'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1EQ'), GetOwningPlayer(GetTriggerUnit()))
    --call SetPlayerTechMaxAllowedSwap( 'A1DN', 0, GetEnumPlayer() )
    
    SetPlayerTechResearchedSwap(FourCC('R0IR'), 1, GetOwningPlayer(GetTriggerUnit()))
    
end
--===========================================================================
function InitTrig_BlackSpear()
    gg_trg_BlackSpear=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BlackSpear, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_BlackSpear, Condition(BlackSpear_Conditions))
    TriggerAddAction(gg_trg_BlackSpear, BlackSpear_Actions)
end
--===========================================================================
-- Trigger: Gurubashy
--===========================================================================
function Gurubashy_Conditions()
    return GetSpellAbilityId() == FourCC('A1EQ')
end
function Gurubashy_Actions()
    
    --Gurubashy
    SetPlayerTechMaxAllowedSwap(FourCC('o04N'), - 1, GetOwningPlayer(GetTriggerUnit())) --??????
    SetPlayerTechMaxAllowedSwap(FourCC('O055'), 1, GetOwningPlayer(GetTriggerUnit())) --??????
    
    SetPlayerAbilityAvailableBJ(false, FourCC('A1EP'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('A1EQ'), GetOwningPlayer(GetTriggerUnit()))
    
end
--===========================================================================
function InitTrig_Gurubashy()
    gg_trg_Gurubashy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Gurubashy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_Gurubashy, Condition(Gurubashy_Conditions))
    TriggerAddAction(gg_trg_Gurubashy, Gurubashy_Actions)
end
--===========================================================================
-- Trigger: SpelltakesHealthCommon
--===========================================================================
function Trig_SpelltakesHealthCommon_Actions()
    local u= GetTriggerUnit()
    UnitDamageTargetBJ(u, u, 100, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_DEATH)
    SetUnitState(u, UNIT_STATE_MANA, GetUnitState(u, UNIT_STATE_MANA) + 100)
    u=nil
end
--===========================================================================
function InitTrig_SpelltakesHealthCommon()
    gg_trg_SpelltakesHealthCommon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpelltakesHealthCommon, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpelltakesHealthCommon, function()
        if GetSpellAbilityId() ~= FourCC('A1DX') then return end
        Trig_SpelltakesHealthCommon_Actions()
    end)
end
--===========================================================================
-- Trigger: SpelltakesHealthCommon2
--===========================================================================
function Trig_SpelltakesHealthCommon2_Actions()
    local u= GetTriggerUnit()
    
    SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) - 75)
    UnitDamageTargetBJ(u, u, 1, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_DEATH)
    u=nil
end
--===========================================================================
function InitTrig_SpelltakesHealthCommon2()
    gg_trg_SpelltakesHealthCommon2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpelltakesHealthCommon2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpelltakesHealthCommon2, function()
        if GetSpellAbilityId() ~= FourCC('A1EJ') then return end
        Trig_SpelltakesHealthCommon2_Actions()
    end)
end
--===========================================================================
-- Trigger: MassSglaz
--===========================================================================
function Trig_MassSglaz_Actions()
    local l= GetSpellTargetLoc()
    local p= GetOwningPlayer(GetTriggerUnit())
    local bex
    local level= GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1E0'))
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = EnemEl
    GroupEnumUnitsInRangeOfLoc(g, l, 110 + 50 * level, bex)
    
    RemoveLocation(l)
    l=GetUnitLoc(GetTriggerUnit())
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        
        u2=CreateUnitAtLoc(p, FourCC('H0BN'), l, bj_UNIT_FACING)
        RemoveUnitTimed(u2 , 2)
        UnitAddAbility(u2, FourCC('A1E1'))
        SetUnitManaBJ(u2, 1111111.00)
        --call SetUnitAbilityLevel( u2,'A17Z', level )
        IssueTargetOrder(u2, "hex", u)
        
        i=i + 1
        GroupRemoveUnit(g, u)
    end
    
    
    u=nil
    DestroyGroup(g)
    g=nil
    RemoveLocation(l)
    p=nil
    u2=nil
    bex=nil
end
--===========================================================================
function InitTrig_MassSglaz()
    gg_trg_MassSglaz=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassSglaz, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_MassSglaz, function()
        if GetSpellAbilityId() ~= FourCC('A1E0') then return end
        Trig_MassSglaz_Actions()
    end)
end
--===========================================================================
-- Trigger: BladeStorm
--===========================================================================
function Trig_BladeStorm_Actions()
    local u= GetTriggerUnit()
    SetUnitFlyHeightBJ(u, 45.00, 3)
    SetUnitPathing(u, false)
    UnitAddTypeBJ(UNIT_TYPE_FLYING, u)
    
    u=nil
end
--===========================================================================
function InitTrig_BladeStorm()
    gg_trg_BladeStorm=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BladeStorm, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_BladeStorm, function()
        if GetSpellAbilityId() ~= FourCC('A1E4') then return end
        Trig_BladeStorm_Actions()
    end)
end
--===========================================================================
-- Trigger: BladeStormEnd
--===========================================================================
function Trig_BladeStormEnd_Actions()
    local u= GetTriggerUnit()
    SetUnitFlyHeightBJ(u, 0, 3)
    SetUnitPathing(u, true)
    UnitRemoveTypeBJ(UNIT_TYPE_FLYING, u)
    
    u=nil
end
--===========================================================================
function InitTrig_BladeStormEnd()
    gg_trg_BladeStormEnd=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BladeStormEnd, EVENT_PLAYER_UNIT_SPELL_ENDCAST)
    TriggerAddAction(gg_trg_BladeStormEnd, function()
        if GetSpellAbilityId() ~= FourCC('A1E4') then return end
        Trig_BladeStormEnd_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellDamageReturn
--===========================================================================
function Trig_SpellDamageReturn_Actions()
    local u= GetTriggerUnit()
    local hp= GetUnitState(u, UNIT_STATE_LIFE) * 0.6
    local seconds= 7
    local i= 0
    local e= AddSpecialEffectTargetUnitBJ("Chest", u, "AbilitiesSpellsItemsVampiricPotionVampPotionCaster.mdl")
    UnitDamageTargetBJ(u, u, hp, ATTACK_TYPE_HERO, DAMAGE_TYPE_UNIVERSAL)
    
    while true do
        if not UnitAlive(u) or u == nil or i * 0.5 > seconds then break end
        SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + hp * 0.07)
        UnitDamageTargetBJ(u, u, 0, ATTACK_TYPE_HERO, DAMAGE_TYPE_DEATH)
        TriggerSleepAction(0.25)
       
        i=i + 1
    end
    DestroyEffect(e)
    e=nil
    u=nil
end
--===========================================================================
function InitTrig_SpellDamageReturn()
    gg_trg_SpellDamageReturn=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellDamageReturn, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellDamageReturn, function()
        if GetSpellAbilityId() ~= FourCC('A1E3') then return end
        Trig_SpellDamageReturn_Actions()
    end)
end
--===========================================================================
-- Trigger: DamageConvert
--===========================================================================
function Trig_DamageConvert_Conditions()
    
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A1E5')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
    
    
    
end
function Trig_DamageConvert_Actions()
    local u= GetEventDamageSource()
    local level= GetUnitAbilityLevel(u, FourCC('A1E5'))
    local damage= GetEventDamage()
    local e= AddSpecialEffectTargetUnitBJ("Chest", u, "AbilitiesSpellsItemsVampiricPotionVampPotionCaster.mdl")
    SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + damage * ( 0.04 * level ))
  
    
    u=nil
    DestroyEffect(e)
    e=nil
end
--===========================================================================
function InitTrig_DamageConvert()
    gg_trg_DamageConvert=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamageConvert, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_DamageConvert, Condition(Trig_DamageConvert_Conditions))
    TriggerAddAction(gg_trg_DamageConvert, Trig_DamageConvert_Actions)
end
--===========================================================================
-- Trigger: AreaOfDeath
--===========================================================================
function Trig_AreaOfDeath_Actions()
    local l= GetSpellTargetLoc()
    local p= GetOwningPlayer(GetTriggerUnit())
    local level= GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1E0'))
    
    local u
    local u2
    local i= 0
   
    
    u2=CreateUnitAtLoc(p, Dummy, l, bj_UNIT_FACING)
    UnitAddAbility(u2, FourCC('A1E7'))
    SetUnitManaBJ(u2, 1111111.00)
    --call SetUnitAbilityLevel( u2,'A17Z', level )
    IssuePointOrderLoc(u2, "deathanddecay", l)
    RemoveLocation(l)
    
    RemoveUnitTimed(u2 , 20)
    
    
    u=nil
    p=nil
    u2=nil
end
--===========================================================================
function InitTrig_AreaOfDeath()
    gg_trg_AreaOfDeath=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AreaOfDeath, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_AreaOfDeath, function()
        if GetSpellAbilityId() ~= FourCC('A1E8') then return end
        Trig_AreaOfDeath_Actions()
    end)
end
--===========================================================================
-- Trigger: Plenenie
--===========================================================================
function Trig_Plenenie_Conditions()
end
function Trig_Plenenie_Actions()
    BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1E9'))
end
--===========================================================================
function InitTrig_Plenenie()
    gg_trg_Plenenie=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Plenenie, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Plenenie, function()
        if GetSpellAbilityId() ~= FourCC('A1E9') then return end
        if not Trig_Plenenie_Conditions() then return end
        Trig_Plenenie_Actions()
    end)
end
--===========================================================================
-- Trigger: DamageMore
--===========================================================================
function Trig_DamageMore_Conditions()
    
    return GetUnitAbilityLevel(BlzGetEventDamageTarget(), FourCC('A1D0')) > 0 -- ??? ?????? ??????
    
    
end
function Trig_DamageMore_Actions()
    local u= BlzGetEventDamageTarget()
    local spellid= FourCC('A1D1')
    local timerspellid= FourCC('A1CX')
    local lifep= GetUnitLifePercent(u)
    local time= 10
    
    
    --call DisplayTextToPlayer(Player(0),0,0,"")
    if lifep < 25 then
        UnitAddAbility(u, spellid)
        SetUnitAbilityLevel(u, spellid, 3)
        BlzStartUnitAbilityCooldown(u, timerspellid, 20)
       -- call DisplayTextToPlayer(Player(0),0,0,"25"+R2S(lifep))
    elseif lifep < 50 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 2)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))   
    elseif lifep < 75 then
            UnitAddAbility(u, spellid)
            SetUnitAbilityLevel(u, spellid, 1)
            BlzStartUnitAbilityCooldown(u, timerspellid, 20)
     --       call DisplayTextToPlayer(Player(0),0,0,"50"+R2S(lifep))
            
    else
            UnitRemoveAbility(u, spellid)
       --     call DisplayTextToPlayer(Player(0),0,0,""+R2S(lifep))
    end
    UnitAddAbility(u, timerspellid)
    BlzStartUnitAbilityCooldown(u, timerspellid, time)
    TriggerSleepAction(time)
    
    if BlzGetUnitAbilityCooldownRemaining(u, timerspellid) == 0 then
        UnitRemoveAbility(u, spellid)
    end
    
    
    
    u=nil
end
--===========================================================================
function InitTrig_DamageMore()
    gg_trg_DamageMore=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamageMore, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_DamageMore, Condition(Trig_DamageMore_Conditions))
    TriggerAddAction(gg_trg_DamageMore, Trig_DamageMore_Actions)
end
--===========================================================================
-- Trigger: TrainBwonsamdy
--===========================================================================
function Trig_TrainBwonsamdy_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('O05L')
end
function Trig_TrainBwonsamdy_Actions()
    Bwonsamdy[GetPlayerId(GetOwningPlayer(GetTrainedUnit()))]=GetTrainedUnit()
    TriggerRegisterUnitLifeEvent(gg_trg_ReturnToAstral, GetTrainedUnit(), LESS_THAN, 150)
end
--===========================================================================
function InitTrig_TrainBwonsamdy()
    gg_trg_TrainBwonsamdy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainBwonsamdy, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainBwonsamdy, Condition(Trig_TrainBwonsamdy_Conditions))
    TriggerAddAction(gg_trg_TrainBwonsamdy, Trig_TrainBwonsamdy_Actions)
end
--===========================================================================
-- Trigger: SpellGiveQSpell
--===========================================================================
function Trig_SpellGiveQSpell_Actions()
    local u= GetTriggerUnit()
    --call DisplayTextToPlayer(Player(0),0,0,"2")
    TriggerSleepAction(0.5)
    if GetUnitAbilityLevel(u, FourCC('A1EZ')) > 0 then
        --???
        UnitRemoveAbility(u, FourCC('A1EW'))
        BlzUnitHideAbility(u, FourCC('A1EV'), false)
    else
        --????????????? ???
        UnitAddAbility(u, FourCC('A1EW'))
        SetUnitAbilityLevel(u, FourCC('A1EW'), GetUnitAbilityLevel(u, FourCC('A1EV')))
        BlzUnitHideAbility(u, FourCC('A1EV'), true)
    end
    u=nil
end
--===========================================================================
function InitTrig_SpellGiveQSpell()
    gg_trg_SpellGiveQSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellGiveQSpell, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_SpellGiveQSpell, function()
        if GetSpellAbilityId() ~= FourCC('A1ES') then return end
        Trig_SpellGiveQSpell_Actions()
    end)
end
--===========================================================================
-- Trigger: GetMoreStatsBwon
--
-- Default melee game initialization for all players
--===========================================================================
function Trig_GetMoreStatsBwon_Conditions()
    return Bwonsamdy[GetPlayerId(GetOwningPlayer(GetKillingUnit()))] ~= nil
end
function Trig_GetMoreStatsBwon_Actions()
    local u= Bwonsamdy[GetPlayerId(GetOwningPlayer(GetKillingUnit()))]
    if u ~= nil then
        BlzSetUnitMaxHP(u, ( BlzGetUnitMaxHP(u) + 1 ))
        BlzSetUnitMaxMana(u, ( BlzGetUnitMaxMana(u) + 6 ))
        SetUnitLifeBJ(u, ( GetUnitStateSwap(UNIT_STATE_LIFE, u) + 1 ))
        SetUnitManaBJ(u, ( GetUnitStateSwap(UNIT_STATE_MANA, u) + 6 ))
        BlzSetUnitRealFieldBJ(u, UNIT_RF_MANA_REGENERATION, ( BlzGetUnitRealField(u, UNIT_RF_MANA_REGENERATION) + 0.05 ))
        
    end
    u=nil
end
--===========================================================================
function InitTrig_GetMoreStatsBwon()
    gg_trg_GetMoreStatsBwon=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GetMoreStatsBwon, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_GetMoreStatsBwon, Condition(Trig_GetMoreStatsBwon_Conditions))
    TriggerAddAction(gg_trg_GetMoreStatsBwon, Trig_GetMoreStatsBwon_Actions)
end
--===========================================================================
-- Trigger: DamagePercent
--===========================================================================
function Trig_DamagePercent_Conditions()
    --call DisplayTextToPlayer(Player(0),0,0,"2")
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('A1ET')) > 0 and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1EU')) == 0
end
function Trig_DamagePercent_Actions()
    local seconds= 7
    local u= GetEventDamageSource()
    local u2= GetTriggerUnit()
    local e= AddSpecialEffectTargetUnitBJ("overhead", u2, "AbilitiesSpellsUndeadCurseCurseTarget.mdl")
    local i= 0
    --call DisplayTextToPlayer(Player(0),0,0,"2"+GetUnitName(u2))
     
    UnitAddAbility(u2, FourCC('A1EU'))
    --call BlzSetAbilityTooltip( 'ANav', I2S(GetPlayerId(GetOwningPlayer(u))), 0 )
    while true do
        if not UnitAlive(u2) or i * 0.25 > seconds then break end
        UnitDamageTargetBJ(u, u2, RMaxBJ(75, BlzGetUnitMaxHP(u2) * 0.005), ATTACK_TYPE_HERO, DAMAGE_TYPE_DEATH)
        TriggerSleepAction(0.25)
        i=i + 1
    end
    UnitRemoveAbility(u2, FourCC('A1EU'))
    DestroyEffect(e)
    u=nil
    u2=nil
    e=nil
end
--===========================================================================
function InitTrig_DamagePercent()
    gg_trg_DamagePercent=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamagePercent, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_DamagePercent, Condition(Trig_DamagePercent_Conditions))
    TriggerAddAction(gg_trg_DamagePercent, Trig_DamagePercent_Actions)
end
--===========================================================================
-- Trigger: ReturnToAstral
--===========================================================================
function Trig_ReturnToAstral_Actions()
    SetUnitManaBJ(GetTriggerUnit(), 0)
    IssueImmediateOrderBJ(GetTriggerUnit(), "metamorphosis")
end
--===========================================================================
function InitTrig_ReturnToAstral()
    gg_trg_ReturnToAstral=CreateTrigger()
    DisableTrigger(gg_trg_ReturnToAstral)
    TriggerAddAction(gg_trg_ReturnToAstral, Trig_ReturnToAstral_Actions)
end
--===========================================================================
-- Trigger: SpellChangeWorld
--===========================================================================
function Trig_SpellChangeWorld_Actions()
    local g= CreateGroup()
    local u
    local i= 0
    local l= GetSpellTargetLoc()
    SetUnitPositionLoc(GetTriggerUnit(), l)
    IssueImmediateOrder(GetTriggerUnit(), "metamorphosis")
    GroupEnumUnitsInRangeOfLoc(g, l, 250, nil)
    while true do
        u=FirstOfGroup(g)
        if u == nil then break end
        if GetOwningPlayer(u) ~= GetOwningPlayer(GetTriggerUnit()) then
            UnitDamageTargetBJ(GetTriggerUnit(), u, 225, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_DEATH)
        end
        GroupRemoveUnit(g, u)
        u=nil
    end
    DestroyGroup(g)
    RemoveLocation(l)
    l=nil
    g=nil
    u=nil
end
--===========================================================================
function InitTrig_SpellChangeWorld()
    gg_trg_SpellChangeWorld=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellChangeWorld, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellChangeWorld, function()
        if GetSpellAbilityId() ~= FourCC('A1ER') then return end
        Trig_SpellChangeWorld_Actions()
    end)
end
--===========================================================================
-- Trigger: GetMoreStats
--
-- Default melee game initialization for all players
--===========================================================================
function Trig_GetMoreStats_Conditions()
    return GetUnitAbilityLevel(GetKillingUnit(), FourCC('A1DD')) > 0
end
function Trig_GetMoreStats_Actions()
    local u= GetKillingUnit()
    BlzSetUnitMaxHP(u, ( BlzGetUnitMaxHP(u) + 5 ))
    BlzSetUnitMaxMana(u, ( BlzGetUnitMaxMana(u) + 5 ))
    SetUnitLifeBJ(u, ( GetUnitStateSwap(UNIT_STATE_LIFE, u) + 5.00 ))
    
    SetUnitManaBJ(u, ( GetUnitStateSwap(UNIT_STATE_MANA, u) + 5.00 ))
   
    u=nil
end
--===========================================================================
function InitTrig_GetMoreStats()
    gg_trg_GetMoreStats=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GetMoreStats, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_GetMoreStats, Condition(Trig_GetMoreStats_Conditions))
    TriggerAddAction(gg_trg_GetMoreStats, Trig_GetMoreStats_Actions)
end
--===========================================================================
-- Trigger: Help
--===========================================================================
function Trig_Help_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1DD')) > 0 and GetUnitLifePercent(GetTriggerUnit()) <= 75
end
function AllyToKill()
    local u= GetFilterUnit()
    if UnitAlive(u) and GetOwningPlayer(u) == udg_LocalPlayer and not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_HERO) and not IsUnitType(u, UNIT_TYPE_SUMMONED) and not IsUnitType(u, UNIT_TYPE_MECHANICAL) and GetUnitTypeId(u) ~= FourCC('h07A') then
        u=nil
        udg_LocalInteger2=udg_LocalInteger2 + 1
        return true
    end
    u=nil
    return false
end
function Trig_Help_Actions()
    local u= GetTriggerUnit()
    local u2= nil
    local g= CreateGroup()
    local b
    local l
    
    DisableTrigger(GetTriggeringTrigger())
    udg_LocalPlayer=GetOwningPlayer(u)
    udg_LocalInteger2=0
    GroupEnumUnitsInRange(g, GetUnitX(u), GetUnitY(u), 750, b)
   -- set u2 = FirstOfGroup(g) 
    if udg_LocalInteger2 > 0 then
        u2=BlzGroupUnitAt(g, GetRandomInt(0, udg_LocalInteger2 - 1))
        if u2 ~= nil and UnitAlive(u2) and u ~= u2 then
            
            SetUnitLifeBJ(u, ( GetUnitStateSwap(UNIT_STATE_LIFE, u) + GetUnitStateSwap(UNIT_STATE_LIFE, u2) * 0.4 ))
            SetUnitManaBJ(u, ( GetUnitStateSwap(UNIT_STATE_MANA, u) + GetUnitStateSwap(UNIT_STATE_MANA, u2) * 0.4 ))
            UnitDamageTargetBJ(u, u2, 9999, ATTACK_TYPE_HERO, DAMAGE_TYPE_DEATH)
            l=AddLightning("AFOD", true, GetUnitX(u), GetUnitY(u), GetUnitX(u2), GetUnitY(u2))
            TriggerSleepAction(0.15)
            DestroyLightning(l)
        end
    end
    DestroyGroup(g)
    DestroyBoolExpr(b)
    g=nil
    b=nil
    l=nil
    u=nil
    u2=nil
    
    EnableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Help()
    gg_trg_Help=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Help, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_Help, Condition(Trig_Help_Conditions))
    TriggerAddAction(gg_trg_Help, Trig_Help_Actions)
end
--===========================================================================
-- Trigger: SpelltakesHealth
--===========================================================================
function Trig_SpelltakesHealth_Conditions()
end
function Trig_SpelltakesHealth_Actions()
    local u= GetTriggerUnit()
    --call UnitDamageTargetBJ( GetTriggerUnit(), GetTriggerUnit(), 150.00, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_DEATH )
    
    
    
    SetUnitLifeBJ(u, ( GetUnitStateSwap(UNIT_STATE_LIFE, u) - 75 * GetUnitAbilityLevel(u, GetSpellAbilityId()) ))
    if GetSpellAbilityId() == FourCC('A1EL') and GetOwningPlayer(GetTriggerUnit()) == GetOwningPlayer(GetSpellTargetUnit()) then
        
        BlzEndUnitAbilityCooldown(GetTriggerUnit(), FourCC('A1EL'))
    end
    
    u=nil
end
--===========================================================================
function InitTrig_SpelltakesHealth()
    gg_trg_SpelltakesHealth=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpelltakesHealth, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpelltakesHealth, function()
        if GetSpellAbilityId() ~= FourCC('A1DC') then return end
        if not Trig_SpelltakesHealth_Conditions() then return end
        Trig_SpelltakesHealth_Actions()
    end)
end
--===========================================================================
-- Trigger: HakkarAuraDeb
--===========================================================================
function Trig_HakkarAuraDeb_Conditions()
    return GetLearnedSkill() == FourCC('A2DM')
end
function Trig_HakkarAuraDeb_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A1EK'))
    SetUnitAbilityLevel(u, FourCC('A1EK'), GetUnitAbilityLevel(u, FourCC('A2DM')))
    u=nil
end
--===========================================================================
function InitTrig_HakkarAuraDeb()
    gg_trg_HakkarAuraDeb=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_HakkarAuraDeb, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_HakkarAuraDeb, Condition(Trig_HakkarAuraDeb_Conditions))
    TriggerAddAction(gg_trg_HakkarAuraDeb, Trig_HakkarAuraDeb_Actions)
end
--===========================================================================
-- Trigger: HelpButton
--===========================================================================
function Trig_HelpButton_Actions()
    local u= GetTriggerUnit()
    local u2= nil
    local g= CreateGroup()
    local b
    local l
    
    DisableTrigger(GetTriggeringTrigger())
    udg_LocalPlayer=GetOwningPlayer(u)
    udg_LocalInteger2=0
    GroupEnumUnitsInRange(g, GetUnitX(u), GetUnitY(u), 750, b)
    
    
    
    while true do
        if udg_LocalInteger2 < 1 or ( GetUnitLifePercent(u) >= 98.0 and GetUnitManaPercent(u) > 98.0 ) then break end
            u2=BlzGroupUnitAt(g, GetRandomInt(0, udg_LocalInteger2 - 1))
            if u2 ~= nil and UnitAlive(u2) and u ~= u2 then
                GroupRemoveUnit(g, u2)
                udg_LocalInteger2=udg_LocalInteger2 - 1
                SetUnitLifeBJ(u, ( GetUnitStateSwap(UNIT_STATE_LIFE, u) + GetUnitStateSwap(UNIT_STATE_LIFE, u2) * 0.4 ))
                SetUnitManaBJ(u, ( GetUnitStateSwap(UNIT_STATE_MANA, u) + GetUnitStateSwap(UNIT_STATE_MANA, u2) * 0.4 ))
                UnitDamageTargetBJ(u, u2, 9999, ATTACK_TYPE_HERO, DAMAGE_TYPE_DEATH)
                l=AddLightning("AFOD", true, GetUnitX(u), GetUnitY(u), GetUnitX(u2), GetUnitY(u2))
                RemoveLigtingTimed(l , 2)
            end
            
        
    end
    DestroyGroup(g)
    DestroyBoolExpr(b)
    g=nil
    b=nil
    l=nil
    u=nil
    u2=nil
    
    EnableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_HelpButton()
    gg_trg_HelpButton=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_HelpButton, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_HelpButton, function()
        if GetSpellAbilityId() ~= FourCC('A1EM') then return end
        Trig_HelpButton_Actions()
    end)
end
--===========================================================================
-- Trigger: BrokenBlood
--===========================================================================
function Trig_BrokenBlood_Conditions()
    --call DisplayTextToPlayer(Player(0),0,0," - ")
end
function EnemyToBlood()
    local u= GetFilterUnit()
    if UnitAlive(u) and IsPlayerEnemy(GetOwningPlayer(u), udg_LocalPlayer) and not IsUnitType(u, UNIT_TYPE_STRUCTURE) and not IsUnitType(u, UNIT_TYPE_MECHANICAL) and GetUnitAbilityLevel(u, FourCC('A1DE')) == 0 then
        u=nil
        return true
    
    end
    u=nil
    return false
end
function BrokenBlood()
    local seconds= 10
    local damage= udg_LocalReal2
    local u= udg_LocalUnit3
    local u2= udg_LocalUnit2
    local g= CreateGroup()
    local b
    local e= AddSpecialEffectTargetUnitBJ("overhead", u2, "Trolls / RedsplashMissilebyRas.mdx")
    local i= 0
    --call DisplayTextToPlayer(Player(0),0,0,"2"+GetUnitName(u2))
     
    UnitAddAbility(u2, FourCC('A1DE'))
    --call BlzSetAbilityTooltip( 'ANav', I2S(GetPlayerId(GetOwningPlayer(u))), 0 )
    while true do
        if not UnitAlive(u2) or i * 0.25 > seconds then break end
        UnitDamageTargetBJ(u, u2, damage, ATTACK_TYPE_HERO, DAMAGE_TYPE_DEATH)
        TriggerSleepAction(0.25)
        i=i + 1
    end
    
--    
    DestroyEffect(e)
    udg_LocalPlayer=GetOwningPlayer(u)
    GroupEnumUnitsInRange(g, GetUnitX(u2), GetUnitY(u2), 425, b)
   
    u2=FirstOfGroup(g)
    if u2 ~= nil and UnitAlive(u2) then
        GroupRemoveUnit(g, u2)
        udg_LocalUnit3=u
        udg_LocalUnit2=u2
        udg_LocalReal2=RMaxBJ(2.5, damage + 0.25)
        ExecuteFunc("BrokenBlood")
    end
    --? ?????? 50% ??????????????? ???
    if Random(1 , 2) then
        u2=FirstOfGroup(g)
        if u2 ~= nil and UnitAlive(u2) then
            GroupRemoveUnit(g, u2)
            udg_LocalUnit3=u
            udg_LocalUnit2=u2
            udg_LocalReal2=RMaxBJ(2.5, damage + 0.25)
            ExecuteFunc("BrokenBlood")
        end
    
    end
    
    UnitRemoveAbility(u2, FourCC('A1DE'))
    DestroyGroup(g)
    DestroyBoolExpr(b)
    g=nil
    b=nil
    e=nil
    
end
function Trig_BrokenBlood_Actions()
    udg_LocalUnit3=GetTriggerUnit()
    udg_LocalUnit2=GetSpellTargetUnit()
    udg_LocalReal2=1
    ExecuteFunc("BrokenBlood")
    
    
    
    
end
--===========================================================================
function InitTrig_BrokenBlood()
    gg_trg_BrokenBlood=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BrokenBlood, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_BrokenBlood, function()
        if GetSpellAbilityId() ~= FourCC('A1DB') then return end
        if not Trig_BrokenBlood_Conditions() then return end
        Trig_BrokenBlood_Actions()
    end)
end
--===========================================================================
-- Trigger: TrainHakkar
--===========================================================================
function Trig_TrainHakkar_Conditions()
    return GetUnitTypeId(GetTrainedUnit()) == FourCC('O055')
end
function Trig_TrainHakkar_Actions()
    for bj_forLoopAIndex = 1, 50 do
        TriggerRegisterUnitLifeEvent(gg_trg_Help, GetTrainedUnit(), LESS_THAN, ( 14 * I2R(GetForLoopIndexA()) ))
    end
    TriggerRegisterUnitLifeEvent(gg_trg_Help, GetTrainedUnit(), LESS_THAN, 2.00)
end
--===========================================================================
function InitTrig_TrainHakkar()
