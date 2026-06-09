
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
    return GetUnitTypeId(GetConstructedStructure()) == FourCC('cD12')
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
PlagueOwner = PlagueOwner or {}

function Trig_PlagueOnBuilding_Actions()
    local caster = GetTriggerUnit()
    local u = GetSpellTargetUnit()
    if u ~= nil then
        if GetUnitAbilityLevel(u, FourCC('A1HS')) < 1 and IsPlayerEnemy(GetOwningPlayer(u), GetOwningPlayer(caster)) then
            if GetUnitFoodMade(u) > 0 then
                income[GetPlayerId(GetOwningPlayer(caster))] = income[GetPlayerId(GetOwningPlayer(caster))] + 5
                income[GetPlayerId(GetOwningPlayer(u))] = income[GetPlayerId(GetOwningPlayer(u))] - 5
            end
            PlagueOwner[GetHandleId(u)] = GetPlayerId(GetOwningPlayer(caster))
            local time = 0
            local e
            local t = CreateTimer()
            TimerStart(t, 1.00, true, function()
                if time == 0 and UnitAlive(u) then
                    UnitAddAbility(u, FourCC('A1HS'))
                    e = AddSpecialEffectTargetUnitBJ("overhead", u, "CultOfDamnedPlagueCloudTargetLight.mdx")
                    time = time + 1
                elseif time < 30 and UnitAlive(u) then
                    time = time + 1
                else
                    if UnitAlive(u) then
                        local casterPi = PlagueOwner[GetHandleId(u)] or 0
                        income[casterPi] = income[casterPi] - 5
                        income[GetPlayerId(GetOwningPlayer(u))] = income[GetPlayerId(GetOwningPlayer(u))] + 5
                    end
                    UnitRemoveAbility(u, FourCC('A1HS'))
                    if e then DestroyEffect(e) end
                    DestroyTimer(t)
                end
            end)
        else
            local t = CreateTimer()
            TimerStart(t, 1.00, true, function() DestroyTimer(t) end)
        end
    end
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
    local id = PlagueOwner[GetHandleId(GetTriggerUnit())] or 0
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