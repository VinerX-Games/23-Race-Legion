
--===========================================================================
-- Trigger: TrainW2
--===========================================================================
function Trig_TrainW2_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('w2a0')) > 0
end
function Trig_TrainW2_Actions()
    local u= GetTrainedUnit()
    local uh= GetHandleId(u)
    local p= GetOwningPlayer(u)
    local r
    SaveInteger(Hash, uh, 0, 0) --StringHash("lvl"),0)
    SaveReal(Hash, uh, 1, 0) --StringHash("xp"),0)
    
    r=GetPlayerTechCount(p, FourCC('w2r3'), true)
    if r > 0 then
        AddXp(u , 100 * r + 25 * r)
    end
    
    u=nil
end
--===========================================================================
function InitTrig_TrainW2()
    gg_trg_TrainW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainW2, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainW2, Condition(Trig_TrainW2_Conditions))
    TriggerAddAction(gg_trg_TrainW2, Trig_TrainW2_Actions)
end
--===========================================================================
-- Trigger: DamagerW2
--===========================================================================
function Trig_DamagerW2_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('w2a0')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_DamagerW2_Actions()
    local u= GetEventDamageSource()
    local damage= GetEventDamage()
    AddXp(u , damage * 0.25)
    
    u=nil
end
--===========================================================================
function InitTrig_DamagerW2()
    gg_trg_DamagerW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamagerW2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_DamagerW2, Condition(Trig_DamagerW2_Conditions))
    TriggerAddAction(gg_trg_DamagerW2, Trig_DamagerW2_Actions)
end
--===========================================================================
-- Trigger: DamageBeforeW2
--===========================================================================
function Trig_DamageBeforeW2_Conditions()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC('w2a0')) > 0 and BlzGetEventAttackType() == ATTACK_TYPE_NORMAL
end
function Trig_DamageBeforeW2_Actions()
    local u= GetEventDamageSource()
    local uh= GetHandleId(u)
    local lvl= LoadInteger(Hash, uh, 0)
    local damage= GetEventDamage()
    
    DisableTrigger(gg_trg_DamageBeforeW2)
    DisableTrigger(gg_trg_DamagerW2)
    if u ~= nil then
        UnitDamageTargetBJ(u, GetTriggerUnit(), damage * 0.02 * lvl, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL)
    else
        UnitDamageTargetBJ(GetTriggerUnit(), GetTriggerUnit(), damage * 0.02 * lvl, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL)
    end
    EnableTrigger(gg_trg_DamageBeforeW2)
    EnableTrigger(gg_trg_DamagerW2)
        
    
    u=nil
end
--===========================================================================
function InitTrig_DamageBeforeW2()
    gg_trg_DamageBeforeW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamageBeforeW2, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_DamageBeforeW2, Condition(Trig_DamageBeforeW2_Conditions))
    TriggerAddAction(gg_trg_DamageBeforeW2, Trig_DamageBeforeW2_Actions)
end
--===========================================================================
-- Trigger: DamagedW2
--===========================================================================
function Trig_DamagedW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
end
function Trig_DamagedW2_Actions()
    local u= GetTriggerUnit()
    local Damage= GetEventDamage()
    
    
    
    AddXp(u , Damage * 0.25)
    
    
    
    u=nil
end
--===========================================================================
function InitTrig_DamagedW2()
    gg_trg_DamagedW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DamagedW2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_DamagedW2, Condition(Trig_DamagedW2_Conditions))
    TriggerAddAction(gg_trg_DamagedW2, Trig_DamagedW2_Actions)
end
--===========================================================================
-- Trigger: AlmostDiyW2
--===========================================================================
function Trig_AlmostDiyW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0
end
function FZepp()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('w2a1')) > 0 and GetOwningPlayer(GetFilterUnit()) == udg_LocalPlayer and UnitAlive(GetFilterUnit()) --and GetUnitUserData(GetFilterUnit())<6
end
function Trig_AlmostDiyW2_Actions()
    local u= GetTriggerUnit()
    local Damage= GetEventDamage()
    local hp= GetUnitState(u, UNIT_STATE_LIFE)
    local Zepp
    local u2
    local g
    
    
    
    
    if hp - Damage < 1 and Random(5 + GetPlayerTechCount(GetOwningPlayer(u), FourCC('w2rq'), true) , 10) then
        
        udg_LocalPlayer=GetOwningPlayer(u)
        Zepp=Condition(FZepp)
        g=CreateGroup()
        GroupEnumUnitsInRangeCounted(g, GetUnitX(u), GetUnitY(u), 1000, Zepp, 5)
        
        
        u2=BlzGroupUnitAt(g, GetRandomInt(1, BlzGroupGetSize(g)))
        if u2 ~= nil and UnitAlive(u2) then
            
            RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanFlakCannonsFlakTarget.mdl", GetUnitX(u), GetUnitY(u)) , 1)
            SetUnitState(u, UNIT_STATE_LIFE, hp + Damage)
            SetUnitPosition(u, GetUnitX(u2), GetUnitY(u2))
            IssueTargetOrder(u, "smart", u2)
        end
        
        DestroyGroup(g)
        g=nil
        u2=nil
    end
    
    
    
    
    u=nil
    
end
--===========================================================================
function InitTrig_AlmostDiyW2()
    gg_trg_AlmostDiyW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_AlmostDiyW2, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_AlmostDiyW2, Condition(Trig_AlmostDiyW2_Conditions))
    TriggerAddAction(gg_trg_AlmostDiyW2, Trig_AlmostDiyW2_Actions)
end
--===========================================================================
-- Trigger: SpellW2
--===========================================================================
function Trig_SpellW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0
end
function Trig_SpellW2_Actions()
    AddXp(GetTriggerUnit() , 4)
end
--===========================================================================
function InitTrig_SpellW2()
    gg_trg_SpellW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellW2, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddCondition(gg_trg_SpellW2, Condition(Trig_SpellW2_Conditions))
    TriggerAddAction(gg_trg_SpellW2, Trig_SpellW2_Actions)
end
--===========================================================================
-- Trigger: DiyGoblinW2
--===========================================================================
function Trig_DiyGoblinW2_Conditions()
    --return GetUnitAbilityLevel(GetTriggerUnit(),'w2a0' ) > 0 
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('w206')
end
function Trig_DiyGoblinW2_Actions()
    local u= GetTriggerUnit()
    local p= GetOwningPlayer(u)
    local hp= GetUnitState(u, UNIT_STATE_LIFE)
    local uh= GetHandleId(u)
    local lvl= LoadInteger(Hash, uh, 0)
    local Zepp
    local u2
    local g
    
    
    
    
    if Random(3 , 4) then
        
        udg_LocalPlayer=GetOwningPlayer(u)
        Zepp=Condition(FZepp)
        g=CreateGroup()
        GroupEnumUnitsInRangeCounted(g, GetUnitX(u), GetUnitY(u), 1000, Zepp, 5)
        
        
        u2=BlzGroupUnitAt(g, GetRandomInt(1, BlzGroupGetSize(g)))
        if u2 ~= nil and UnitAlive(u2) then
                   
            RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanFlakCannonsFlakTarget.mdl", GetUnitX(u2), GetUnitY(u2)) , 1)
            CreateUnit(p, FourCC('w206'), GetUnitX(u2), GetUnitY(u2), 0.0)
            AddXp(u2 , 100 * lvl + 25 * lvl)
        end
    end
    
    
    DestroyGroup(g)
    g=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_DiyGoblinW2()
    gg_trg_DiyGoblinW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DiyGoblinW2, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DiyGoblinW2, Condition(Trig_DiyGoblinW2_Conditions))
    TriggerAddAction(gg_trg_DiyGoblinW2, Trig_DiyGoblinW2_Actions)
end
--===========================================================================
-- Trigger: DiyW2
--
-- ??? ??????? ??????????
--===========================================================================
function Trig_DiyW2_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('w2a0')) > 0
    
end
function deadEdly()
    
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    local uh= LoadInteger(Hash, id, 1)
    
    if u == nil then
        FlushChildHashtable(Hash, uh)
    end
    FlushChildHashtable(Hash, id)
    DestroyTimer(t)
    t=nil
    u=nil
end
function Trig_DiyW2_Actions()
    local u= GetTriggerUnit()
    local uh= GetHandleId(u)
    
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    TimerStart(t, 45, false, deadEdly)
    SaveUnitHandle(Hash, id, 0, u)
    SaveInteger(Hash, id, 1, uh)
    t=nil
    u=nil
end
--===========================================================================
function InitTrig_DiyW2()
    gg_trg_DiyW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DiyW2, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DiyW2, Condition(Trig_DiyW2_Conditions))
    TriggerAddAction(gg_trg_DiyW2, Trig_DiyW2_Actions)
end
--===========================================================================
-- Trigger: KillW2
--===========================================================================
function Trig_KillW2_Conditions()
    return GetUnitAbilityLevel(GetKillingUnit(), FourCC('w2a0')) > 0 and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetEventDamageSource()))
end
function Trig_KillW2_Actions()
    local u= GetKillingUnit()
    
    
    
    AddXp(u , 55)
    u=nil
end
--===========================================================================
function InitTrig_KillW2()
    gg_trg_KillW2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KillW2, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_KillW2, Condition(Trig_KillW2_Conditions))
    TriggerAddAction(gg_trg_KillW2, Trig_KillW2_Actions)
end
--===========================================================================
-- Trigger: SummonRune
--===========================================================================
function Trig_SummonRune_Conditions()
    return GetUnitTypeId(GetSummonedUnit()) == FourCC('w216')
end
function Trig_SummonRune_Actions()
    UnitApplyTimedLifeBJ(2.00, FourCC('BTLF'), GetSummonedUnit())
end
--===========================================================================
function InitTrig_SummonRune()
    gg_trg_SummonRune=CreateTrigger()
    DisableTrigger(gg_trg_SummonRune)
    TriggerRegisterAnyUnitEventBJ(gg_trg_SummonRune, EVENT_PLAYER_UNIT_SUMMON)
    TriggerAddCondition(gg_trg_SummonRune, Condition(Trig_SummonRune_Conditions))
    TriggerAddAction(gg_trg_SummonRune, Trig_SummonRune_Actions)
end
--===========================================================================
-- Trigger: RuneExplode
--===========================================================================
function Trig_RuneExplode_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('w216')
end
function Trig_RuneExplode_Actions()
    local u= GetTriggerUnit()
    RemoveEffectTimed(AddSpecialEffect("AbilitiesWeaponsBoltBoltImpact.mdl", GetUnitX(u), GetUnitY(u)) , 2)
    u=nil
end
--===========================================================================
function InitTrig_RuneExplode()
    gg_trg_RuneExplode=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_RuneExplode, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_RuneExplode, Condition(Trig_RuneExplode_Conditions))
    TriggerAddAction(gg_trg_RuneExplode, Trig_RuneExplode_Actions)
end
--===========================================================================
-- Trigger: SpellArmorDamage
--===========================================================================
function Trig_SpellArmorDamage_Actions()
    UnitDamageTargetBJ(GetTriggerUnit(), GetSpellTargetUnit(), RMinBJ(GetUnitState(GetSpellTargetUnit(), UNIT_STATE_LIFE) * 0.33, 500), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_DEATH)
end
--===========================================================================
function InitTrig_SpellArmorDamage()
    gg_trg_SpellArmorDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellArmorDamage, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellArmorDamage, function()
        if GetSpellAbilityId() ~= FourCC('w2a8') then return end
        Trig_SpellArmorDamage_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellMassAxes
--===========================================================================
function Trig_SpellMassAxes_Actions()
    local l= GetSpellTargetLoc()
    local caster= GetTriggerUnit()
    local p= GetOwningPlayer(caster)
    local bex
    local dammyAbility= FourCC('w2aa')
    local level= GetUnitAbilityLevel(caster, GetSpellAbilityId())
    local g= CreateGroup()
    local u
    local u2
    local i= 0
    udg_LocalPlayer=p
    bex = EnemEl
    GroupEnumUnitsInRangeOfLoc(g, l, 150, bex)
    
    if FirstOfGroup(g) == nil then
        --???? ??????
        BlzStartUnitAbilityCooldown(caster, dammyAbility, 15)
        SetUnitState(caster, UNIT_STATE_MANA, GetUnitState(caster, UNIT_STATE_MANA) + 100 + 35 * level)
        
    
    else
        RemoveLocation(l)
        l=GetUnitLoc(caster)
        while true do
            u=FirstOfGroup(g)
            if u == nil then break end
            
            u2=CreateUnitAtLoc(p, Dummy, l, bj_UNIT_FACING)
            
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
function InitTrig_SpellMassAxes()
    gg_trg_SpellMassAxes=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellMassAxes, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellMassAxes, function()
        if GetSpellAbilityId() ~= FourCC('w2af') then return end
        Trig_SpellMassAxes_Actions()
    end)
end
--===========================================================================
-- Trigger: SpellArrow
--===========================================================================
function FireDark()
    
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    --local integer aid = LoadInteger(Hash,id,1)
    local times= LoadInteger(Hash, id, 2)
    local level= LoadInteger(Hash, id, 3)
    local loc= LoadLocationHandle(Hash, id, 4)
    local u2= CreateUnit(GetOwningPlayer(u), Dummy, GetUnitX(u), GetUnitY(u), bj_UNIT_FACING)
    SetUnitFlyHeight(u2, 100.00, 10)
    UnitAddAbility(u2, FourCC('w2aE'))
    SetUnitAbilityLevel(u2, FourCC('w2aE'), level)
    IssuePointOrderLoc(u2, "carrionswarm", loc)
    RemoveUnitTimed(u2 , 2)
    
    
    times=times + 1
    SaveInteger(Hash, id, 2, times)
    if times > 8 then
        RemoveLocation(loc)
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
    end
    
    
    u=nil
    u2=nil
    t=nil
    
    loc=nil
end
function Trig_SpellArrow_Actions()
    local u= GetTriggerUnit()
    
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    TimerStart(t, 0.35, true, FireDark)
    SaveUnitHandle(Hash, id, 0, u)
    --call SaveInteger(Hash,id,1, 'w2aW')
    SaveInteger(Hash, id, 2, 0)
    SaveInteger(Hash, id, 3, GetUnitAbilityLevel(u, FourCC('w2aW')))
    SaveLocationHandle(Hash, id, 4, GetSpellTargetLoc())
    t=nil
    u=nil
    
end
--===========================================================================
function InitTrig_SpellArrow()
    gg_trg_SpellArrow=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_SpellArrow, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_SpellArrow, function()
        if GetSpellAbilityId() ~= FourCC('w2aW') then return end
        if not (IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO)) then return end
        Trig_SpellArrow_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonHP
--===========================================================================
function Trig_DragonHP_Actions()
    SetPlayerTechResearchedSwap(FourCC('w292'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('w290'), GetOwningPlayer(GetTriggerUnit()))
    
    SetPlayerAbilityAvailableBJ(false, FourCC('w294'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w297'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w295'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DragonHP()
    gg_trg_DragonHP=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonHP, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DragonHP, function()
        if GetSpellAbilityId() ~= FourCC('w294') then return end
        Trig_DragonHP_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonDamage
--===========================================================================
function Trig_DragonDamage_Actions()
    SetPlayerTechResearchedSwap(FourCC('w293'), 1, GetOwningPlayer(GetTriggerUnit()))
    --call SetPlayerAbilityAvailableBJ( true, 'w290', GetOwningPlayer(GetTriggerUnit()) )
        SetPlayerAbilityAvailableBJ(false, FourCC('w294'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w297'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w295'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DragonDamage()
    gg_trg_DragonDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonDamage, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DragonDamage, function()
        if GetSpellAbilityId() ~= FourCC('w297') then return end
        Trig_DragonDamage_Actions()
    end)
end
--===========================================================================
-- Trigger: DragonMage
--===========================================================================
function Trig_DragonMage_Actions()
    SetPlayerTechResearchedSwap(FourCC('w291'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('w289'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(true, FourCC('w288'), GetOwningPlayer(GetTriggerUnit()))
    --call SetPlayerAbilityAvailableBJ( true, 'w290', GetOwningPlayer(GetTriggerUnit()) )
    
    SetPlayerAbilityAvailableBJ(false, FourCC('w294'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w297'), GetOwningPlayer(GetTriggerUnit()))
    SetPlayerAbilityAvailableBJ(false, FourCC('w295'), GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_DragonMage()
    gg_trg_DragonMage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DragonMage, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_DragonMage, function()
        if GetSpellAbilityId() ~= FourCC('w295') then return end
        Trig_DragonMage_Actions()
    end)
end
--===========================================================================
-- Trigger: OgrimmCharge
--===========================================================================
-- ???? 1 - ???????? ????? - ????? ??? ??? ??????)))
--================
--================================================================================================================================================================================
-- ???? 2 - ???????? ???????
--================
function Trig_OgrimmCharge_Actions()
    local GT= GetTriggerUnit()
    local x= GetUnitX(GT)
    local y= GetUnitY(GT)
    local x1= GetSpellTargetX()
    local y1= GetSpellTargetY()
    local l= JSTRRastMT(x , x1 , y , y1)
    if l == 0 then l = 1 end

    JSTRSkill=GetSpellAbilityId()
    local skillId = JSTRSkill
    UnitAddAbility(GT, FourCC('Amrf'))
    UnitRemoveAbility(GT, FourCC('Amrf'))
    ---------
    DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    local t= CreateTimer()
    TimerStart(t, 0.025, true, function()
        local dx= GetUnitX(GT)
        local dy= GetUnitY(GT)
        local ugol= JSTRUgolMT(dx , x1 , dy , y1)
        local MaxW
        if l <= 500 then MaxW=l else MaxW=500 end
        ---------
        local nx=dx + 25 * Cos(ugol * bj_DEGTORAD)
        local ny=dy + 25 * Sin(ugol * bj_DEGTORAD)
        local w=JSTRParabolaZ(MaxW , l , JSTRRastMT(nx , x1 , ny , y1))

        if JSTRRastMT(x1 , dx , y1 , dy) > 25 then
            SetUnitX(GT, nx)
            SetUnitY(GT, ny)
            SetUnitFacing(GT, ugol)
            SetUnitFlyHeight(GT, w, 0)
        else
            DestroyTimer(t)
            SetUnitAnimation(GT, "attack")
            SetUnitFlyHeight(GT, 0, 0)
            DestroyEffect(AddSpecialEffect("AbilitiesSpellsOrcWarStompWarStompCaster.mdl", dx, dy))
            local g=CreateGroup()
            GroupEnumUnitsInRange(g, dx, dy, 260, nil)
            while true do
                local un=FirstOfGroup(g)
                if un == nil then break end
                local lvl=GetUnitAbilityLevel(GT, skillId)
                local uron=1.3 * lvl * GetHeroStr(GT, true) + lvl * 50
                if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) then
                    UnitDamageTarget(GT, un, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
                    DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsOrcMirrorImageMirrorImageDeathCaster.mdl", un, "orign"))
                    local knockUn = un
                    local knockAngle=JSTRUgolMT(dx , GetUnitX(un) , dy , GetUnitY(un))
                    local knockCos = Cos(knockAngle * bj_DEGTORAD)
                    local knockSin = Sin(knockAngle * bj_DEGTORAD)
                    local knockKol = 9
                    local knockTimer = CreateTimer()
                    TimerStart(knockTimer, 0.03, true, function()
                        local kx = GetUnitX(knockUn) + 20 * knockCos
                        local ky = GetUnitY(knockUn) + 20 * knockSin
                        if knockKol >= 0 then
                            SetUnitX(knockUn, kx)
                            SetUnitY(knockUn, ky)
                            knockKol = knockKol - 1
                        else
                            DestroyTimer(knockTimer)
                        end
                    end)
                end
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
function InitTrig_OgrimmCharge()
    gg_trg_OgrimmCharge=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OgrimmCharge, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_OgrimmCharge, function()
        if GetSpellAbilityId() ~= FourCC('w2o6') then return end
        Trig_OgrimmCharge_Actions()
    end)
end
--===========================================================================
-- Trigger: Duel
--===========================================================================
function Duel()
    local t= GetExpiredTimer()
    local id= GetHandleId(t)
    local u= LoadUnitHandle(Hash, id, 0)
    local u2= LoadUnitHandle(Hash, id, 1)
    local l1=GetUnitLoc(u)
    local l2=GetUnitLoc(u2)
    UnitRemoveAbility(u, FourCC('Avul'))
    UnitRemoveAbility(u2, FourCC('Avul'))
    PauseUnit(u, true)
    PauseUnit(u2, true)
    SetUnitAnimation(u, "attack")
    SetUnitAnimation(u2, "attack")
    SetUnitLookAt(u, "bone_chest", u2, 0, 0, 0)
    SetUnitLookAt(u2, "bone_chest", u, 0, 0, 0)
    
    
    UnitDamageTargetBJ(u, u2, BlzGetUnitBaseDamage(u, 1), ATTACK_TYPE_HERO, DAMAGE_TYPE_UNIVERSAL)
    if UnitAlive(u2) then
         UnitDamageTargetBJ(u2, u, BlzGetUnitBaseDamage(u, 1), ATTACK_TYPE_HERO, DAMAGE_TYPE_UNIVERSAL)
    end
   
    UnitAddAbility(u, FourCC('Avul'))
    UnitAddAbility(u2, FourCC('Avul'))
    if not UnitAlive(u) then
        PauseUnit(u, false)
        PauseUnit(u2, false)
        SetUnitAnimation(u, "death")
        SetUnitAnimation(u2, "stand")
        UnitAddAbility(u2, FourCC('w2oz'))
        IssueImmediateOrder(u2, "howlofterror")
            UnitRemoveAbility(u, FourCC('Avul'))
        UnitRemoveAbility(u2, FourCC('Avul'))
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
        
        ResetUnitLookAt(u)
        ResetUnitLookAt(u2)
        
    elseif not UnitAlive(u2) then
        PauseUnit(u, false)
        PauseUnit(u2, false)
        SetUnitAnimation(u, "stand")
        SetUnitAnimation(u2, "death")
        UnitAddAbility(u, FourCC('w2oz'))
        IssueImmediateOrder(u, "howlofterror")
        UnitRemoveAbility(u, FourCC('Avul'))
        UnitRemoveAbility(u2, FourCC('Avul'))
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
        
        ResetUnitLookAt(u)
        ResetUnitLookAt(u2)
        
    elseif u == nil or u2 == nil or DistanceBetweenPoints(l1, l2) > 500 then
        PauseUnit(u, false)
        PauseUnit(u2, false)
        SetUnitAnimation(u, "stand")
        SetUnitAnimation(u2, "stand")
        ResetUnitLookAt(u)
        ResetUnitLookAt(u2)
        UnitRemoveAbility(u, FourCC('Avul'))
        UnitRemoveAbility(u2, FourCC('Avul'))
        FlushChildHashtable(Hash, id)
        PauseTimer(t)
        DestroyTimer(t)
        
    
    end
    t=nil
    u=nil
    u2=nil
    
    RemoveLocation(l1)
    RemoveLocation(l2)
    l1=nil
    l2=nil
end
function Trig_Duel_Actions()
    local u= GetTriggerUnit()
    local u2= GetSpellTargetUnit()
    local t= CreateTimer()
    local id= GetHandleId(t)
    
    TimerStart(t, 1, true, Duel)
    SaveUnitHandle(Hash, id, 0, u)
    SaveUnitHandle(Hash, id, 1, u2)
    
    UnitAddAbility(u, FourCC('Avul'))
    UnitAddAbility(u2, FourCC('Avul'))
    
    
    --call SaveInteger(Hash,id,1, 'w2aW')
    --call SaveInteger(Hash,id,2, 0)
    --call SaveInteger(Hash,id,3, GetUnitAbilityLevel(u,'w2aW'))
    --call SaveLocationHandle(Hash,id,4, GetSpellTargetLoc())
    t=nil
    u=nil
    u2=nil
    
end
--===========================================================================
function InitTrig_Duel()
    gg_trg_Duel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Duel, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Duel, function()
        if GetSpellAbilityId() ~= FourCC('w2ou') then return end
        if not (IsUnitType(GetSpellTargetUnit(), UNIT_TYPE_HERO)) then return end
        Trig_Duel_Actions()
    end)
end