
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
        BlzSetUnitMaxHP(u, BlzGetUnitMaxHP(u) + 1)
        BlzSetUnitMaxMana(u, BlzGetUnitMaxMana(u) + 6)
        SetUnitLifeBJ(u, GetUnitStateSwap(UNIT_STATE_LIFE, u) + 1)
        SetUnitManaBJ(u, GetUnitStateSwap(UNIT_STATE_MANA, u) + 6)
        BlzSetUnitRealFieldBJ(u, UNIT_RF_MANA_REGENERATION, BlzGetUnitRealField(u, UNIT_RF_MANA_REGENERATION) + 0.05)
        
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
    BlzSetUnitMaxHP(u, BlzGetUnitMaxHP(u) + 5)
    BlzSetUnitMaxMana(u, BlzGetUnitMaxMana(u) + 5)
    SetUnitLifeBJ(u, GetUnitStateSwap(UNIT_STATE_LIFE, u) + 5.00)
    
    SetUnitManaBJ(u, GetUnitStateSwap(UNIT_STATE_MANA, u) + 5.00)
   
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
            
            SetUnitLifeBJ(u, GetUnitStateSwap(UNIT_STATE_LIFE, u) + GetUnitStateSwap(UNIT_STATE_LIFE, u2) * 0.4)
            SetUnitManaBJ(u, GetUnitStateSwap(UNIT_STATE_MANA, u) + GetUnitStateSwap(UNIT_STATE_MANA, u2) * 0.4)
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
    
    
    
    SetUnitLifeBJ(u, GetUnitStateSwap(UNIT_STATE_LIFE, u) - 75 * GetUnitAbilityLevel(u, GetSpellAbilityId()))
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
                SetUnitLifeBJ(u, GetUnitStateSwap(UNIT_STATE_LIFE, u) + GetUnitStateSwap(UNIT_STATE_LIFE, u2) * 0.4)
                SetUnitManaBJ(u, GetUnitStateSwap(UNIT_STATE_MANA, u) + GetUnitStateSwap(UNIT_STATE_MANA, u2) * 0.4)
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
        TriggerRegisterUnitLifeEvent(gg_trg_Help, GetTrainedUnit(), LESS_THAN, 14 * I2R(GetForLoopIndexA()))
    end
    TriggerRegisterUnitLifeEvent(gg_trg_Help, GetTrainedUnit(), LESS_THAN, 2.00)
end
--===========================================================================
function InitTrig_TrainHakkar()
    gg_trg_TrainHakkar=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainHakkar, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainHakkar, Condition(Trig_TrainHakkar_Conditions))
    TriggerAddAction(gg_trg_TrainHakkar, Trig_TrainHakkar_Actions)
end