
--===========================================================================
-- Trigger: IceTrollsStart
--===========================================================================
function IceTrollsStartEach()
    local p= GetEnumPlayer()
    
    SetPlayerTechMaxAllowedSwap(FourCC('n07B'), 0, p) -- ????????? ???
    SetPlayerTechMaxAllowedSwap(FourCC('R09L'), 0, p) -- ??? ?????
    SetPlayerTechMaxAllowedSwap(FourCC('o04T'), 0, p) -- ?????
    SetPlayerTechMaxAllowedSwap(FourCC('R09P'), 0, p) -- Golem grade
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('n05W'), 0, p) -- Mamont
    SetPlayerTechMaxAllowedSwap(FourCC('n05X'), 0, p) -- Magnatavr
    SetPlayerTechMaxAllowedSwap(FourCC('R0I5'), 0, p) -- Grade
    
    --Loa
    SetPlayerTechMaxAllowedSwap(FourCC('n061'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('n062'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o05B'), 0, p)
    
    --Loa poglosenie
    SetPlayerTechMaxAllowedSwap(FourCC('R0AI'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AJ'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AD'), 0, p)
    
     
    --Loa altars
    SetPlayerTechMaxAllowedSwap(FourCC('o06J'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06K'), 0, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06I'), 0, p)
    
    SetPlayerTechMaxAllowedSwap(FourCC('O06L'), 1, p) -- Malakk
end
function Trig_IceTrollsStart_Actions()
    ForForce(udg_AllPlayers, IceTrollsStartEach)
end
--===========================================================================
function InitTrig_IceTrollsStart()
    gg_trg_IceTrollsStart=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_IceTrollsStart, 0.01)
    TriggerAddAction(gg_trg_IceTrollsStart, Trig_IceTrollsStart_Actions)
end
--===========================================================================
-- Trigger: KillLoa
--===========================================================================
function Trig_KillLoa_Actions()
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechResearchedSwap(FourCC('R0IX'), 1, p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FR'), p)
    
    
    SetPlayerTechMaxAllowedSwap(FourCC('n07B'), - 1, p) -- ????????? ???
    SetPlayerTechMaxAllowedSwap(FourCC('R09L'), 2, p) -- ??? ?????
    SetPlayerTechMaxAllowedSwap(FourCC('o04T'), - 1, p) -- Golem
    SetPlayerTechMaxAllowedSwap(FourCC('R09P'), 2, p) -- Golem grade
    
    --Loa grades poglosenie
    SetPlayerTechMaxAllowedSwap(FourCC('R0AI'), 3, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AJ'), 3, p)
    SetPlayerTechMaxAllowedSwap(FourCC('R0AD'), 3, p)
    
    
end
--===========================================================================
function InitTrig_KillLoa()
    gg_trg_KillLoa=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_KillLoa, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_KillLoa, function()
        if GetSpellAbilityId() ~= FourCC('A1FS') then return end
        Trig_KillLoa_Actions()
    end)
end
--===========================================================================
-- Trigger: ServeLoa
--===========================================================================
function Trig_ServeLoa_Actions()
    local p= GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechResearchedSwap(FourCC('R0IY'), 1, p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FS'), p)
    SetPlayerAbilityAvailableBJ(false, FourCC('A1FR'), p)
    
    SetPlayerTechMaxAllowedSwap(FourCC('n05W'), - 1, p) -- Mamont
    SetPlayerTechMaxAllowedSwap(FourCC('n05X'), - 1, p) -- Magnatavr
    SetPlayerTechMaxAllowedSwap(FourCC('R0I5'), 2, p) -- Grade
    
    --Loa
    SetPlayerTechMaxAllowedSwap(FourCC('n061'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('n062'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o05B'), 1, p)
    
  
       
    --Loa altars
    SetPlayerTechMaxAllowedSwap(FourCC('o06J'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06K'), 1, p)
    SetPlayerTechMaxAllowedSwap(FourCC('o06I'), 1, p)
    
end
--===========================================================================
function InitTrig_ServeLoa()
    gg_trg_ServeLoa=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ServeLoa, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_ServeLoa, function()
        if GetSpellAbilityId() ~= FourCC('A1FR') then return end
        Trig_ServeLoa_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell E Copy
--===========================================================================
function Trig_Spell_E_Copy_Actions()
    udg_MUI_E_Glaz=udg_MUI_E_Glaz + 1
    udg_Antibag_E_Glaz[udg_MUI_E_Glaz]=udg_Antibag_E_Glaz[udg_MUI_E_Glaz] + 1
    udg_Cikl_E_Glaz=0
    udg_Dalnost_E_Glaz[udg_MUI_E_Glaz]=0.00
    udg_Caster_E_Glaz[udg_MUI_E_Glaz]=GetTriggerUnit()
    SetUnitPathing(udg_Caster_E_Glaz[udg_MUI_E_Glaz], false)
    PauseUnitBJ(true, udg_Caster_E_Glaz[udg_MUI_E_Glaz])
    SetUnitAnimation(udg_Caster_E_Glaz[udg_MUI_E_Glaz], "attackwalkstandspin")
    udg_Logika_E_Glaz[udg_MUI_E_Glaz]=true
    StartTimerBJ(udg_Timer_E_Glaz, true, 0.03)
end
--===========================================================================
function InitTrig_Spell_E_Copy()
    gg_trg_Spell_E_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_E_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Spell_E_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1DA') then return end
        Trig_Spell_E_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell E Dvij
--===========================================================================
function Trig_Spell_E_Dvij_Func001Func001Func007Func001C()
    return IsUnitEnemy(GetEnumUnit(), GetOwningPlayer(udg_Caster_E_Glaz[udg_Cikl_E_Glaz])) and not (IsUnitAlly(GetEnumUnit(), GetOwningPlayer(udg_Caster_E_Glaz[udg_Cikl_E_Glaz]))) and not (IsUnitInGroup(GetEnumUnit(), udg_Group_E_Glaz[udg_Cikl_E_Glaz])) and not (IsUnitDeadBJ(GetEnumUnit())) and not (IsUnitType(GetEnumUnit(), UNIT_TYPE_STRUCTURE))
end
function Trig_Spell_E_Dvij_Func001Func001Func007A()
    if Trig_Spell_E_Dvij_Func001Func001Func007Func001C() then
        UnitDamageTargetBJ(udg_Caster_E_Glaz[udg_Cikl_E_Glaz], GetEnumUnit(), 50.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A1DA'), udg_Caster_E_Glaz[udg_Cikl_E_Glaz])), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
        GroupAddUnitSimple(GetEnumUnit(), udg_Group_E_Glaz[udg_Cikl_E_Glaz])
    end
end
function Trig_Spell_E_Dvij_Func001Func001Func008Func001C()
    return IsUnitDeadBJ(udg_Caster_E_Glaz[udg_Cikl_E_Glaz]) or (( ( udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz] == 0.20 ) ))
end
function Trig_Spell_E_Dvij_Func001Func001Func008Func008C()
    return udg_Antibag_E_Glaz[udg_MUI_E_Glaz] == 0
end
function Trig_Spell_E_Dvij_Func001Func001Func008C()
    return Trig_Spell_E_Dvij_Func001Func001Func008Func001C()
end
function Trig_Spell_E_Dvij_Func001Func001C()
    return udg_Logika_E_Glaz[udg_Cikl_E_Glaz]
end
function Trig_Spell_E_Dvij_Actions()
    udg_Cikl_E_Glaz=1
    while true do
        if udg_Cikl_E_Glaz > udg_MUI_E_Glaz then break end
        if Trig_Spell_E_Dvij_Func001Func001C() then
            udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz]=udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz] + 0.02
            udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz]=GetUnitLoc(udg_Caster_E_Glaz[udg_Cikl_E_Glaz])
            SetUnitPositionLoc(udg_Caster_E_Glaz[udg_Cikl_E_Glaz], PolarProjectionBJ(udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz], 60.00, GetUnitFacing(udg_Caster_E_Glaz[udg_Cikl_E_Glaz])))
            AddSpecialEffectLocBJ(udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz], "CosmicBall.mdx")
            DestroyEffectBJ(GetLastCreatedEffectBJ())
            bj_wantDestroyGroup=true
            ForGroupBJ(GetUnitsInRangeOfLocAll(150.00, udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz]), Trig_Spell_E_Dvij_Func001Func001Func007A)
            if Trig_Spell_E_Dvij_Func001Func001Func008C() then
                GroupClear(udg_Group_E_Glaz[udg_Cikl_E_Glaz])
                SetUnitPathing(udg_Caster_E_Glaz[udg_Cikl_E_Glaz], true)
                PauseUnitBJ(false, udg_Caster_E_Glaz[udg_Cikl_E_Glaz])
                udg_Dalnost_E_Glaz[udg_Cikl_E_Glaz]=0.00
                udg_Logika_E_Glaz[udg_Cikl_E_Glaz]=false
                udg_Antibag_E_Glaz[udg_Cikl_E_Glaz]=udg_Antibag_E_Glaz[udg_Cikl_E_Glaz] - 1
                if Trig_Spell_E_Dvij_Func001Func001Func008Func008C() then
                    PauseTimerBJ(true, udg_Timer_E_Glaz)
                    udg_MUI_E_Glaz=0
                end
            end
            RemoveLocation(udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz])
        end
        udg_Cikl_E_Glaz=udg_Cikl_E_Glaz + 1
    end
end
--===========================================================================
function InitTrig_Spell_E_Dvij()
    gg_trg_Spell_E_Dvij=CreateTrigger()
    TriggerRegisterTimerExpireEventBJ(gg_trg_Spell_E_Dvij, udg_Timer_E_Glaz)
    TriggerAddAction(gg_trg_Spell_E_Dvij, Trig_Spell_E_Dvij_Actions)
end
--===========================================================================
-- Trigger: Ini2
--
-- ????????????? ???????????? ?????? ???????? ??? ???? ???????
--===========================================================================
function Trig_Ini2_Actions()
    --call DisplayTextToPlayer(Player(0),0,0,"")
    UnitAddAbility(GetSpellTargetUnit(), FourCC('A0H1'))
end
--===========================================================================
function InitTrig_Ini2()
    gg_trg_Ini2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Ini2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Ini2, function()
        if GetSpellAbilityId() ~= FourCC('A1DQ') then return end
        Trig_Ini2_Actions()
    end)
end
--===========================================================================
-- Trigger: Spell E2
--===========================================================================
function Trig_Spell_E2_Conditions()
 
    return GetUnitTypeId(GetEventDamageSource()) == FourCC('O04H') and GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A0H1')) > 0
    -- ??? ???????????? ? ???? ????????????
end
function Trig_Spell_E2_Actions()
    local u= GetTriggerUnit()
    DisableTrigger(GetTriggeringTrigger())
    UnitRemoveAbility(u, FourCC('A0H1'))
    --call DisplayTextToPlayer(Player(0),0,0,"")
    udg_To4kaTarget=GetUnitLoc(u)
    UnitDamageTargetBJ(GetEventDamageSource(), u, I2R(GetHeroStatBJ(bj_HEROSTAT_AGI, GetEventDamageSource(), true)), ATTACK_TYPE_HERO, DAMAGE_TYPE_UNIVERSAL)
    AddSpecialEffectLocBJ(udg_To4kaTarget, "AbilitiesSpellsOtherCrushingWaveCrushingWaveDamage.mdl")
    DestroyEffectBJ(GetLastCreatedEffectBJ())
    CreateTextTagLocBJ("cff00ff00 .. " .. I2S(GetHeroStatBJ(bj_HEROSTAT_AGI, GetEventDamageSource(), true)), udg_To4kaTarget, 140.00, 9.00, 100, 100, 100, 0)
    SetTextTagVelocityBJ(GetLastCreatedTextTag(), 150.00, 90)
    SetTextTagSuspendedBJ(GetLastCreatedTextTag(), false)
    SetTextTagPermanentBJ(GetLastCreatedTextTag(), false)
    SetTextTagLifespanBJ(GetLastCreatedTextTag(), 0.80)
    SetTextTagFadepointBJ(GetLastCreatedTextTag(), 0.80)
    RemoveLocation(udg_To4kaTarget)
    EnableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Spell_E2()
    gg_trg_Spell_E2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_E2, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_Spell_E2, Condition(Trig_Spell_E2_Conditions))
    TriggerAddAction(gg_trg_Spell_E2, Trig_Spell_E2_Actions)
end
--===========================================================================
-- Trigger: HpRegen2
--===========================================================================
function Trig_HpRegen2_Conditions()
    
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1CA')) > 0 -- ??? ?????? ??????
    
    
end
function Trig_HpRegen2_Actions()
    local u= GetTriggerUnit()
    local spellid= FourCC('A1CY')
    local timerspellid= FourCC('A1CX')
    local lifep= GetUnitLifePercent(u)
    local time= 10
    
    if lifep < 25 then
        UnitAddAbility(u, spellid)
        SetUnitAbilityLevel(u, spellid, 2)
        BlzStartUnitAbilityCooldown(u, timerspellid, 20)
       -- call DisplayTextToPlayer(Player(0),0,0,"25"+R2S(lifep))
    elseif lifep < 50 then
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
function InitTrig_HpRegen2()
    gg_trg_HpRegen2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_HpRegen2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_HpRegen2, Condition(Trig_HpRegen2_Conditions))
    TriggerAddAction(gg_trg_HpRegen2, Trig_HpRegen2_Actions)
end
--===========================================================================
-- Trigger: Spell Copy 2 Copy
--===========================================================================
function Trig_Spell_Copy_2_Copy_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1CB')
end
function Trig_Spell_Copy_2_Copy_Actions()
    udg_u=GetLearningUnit()
    TriggerRegisterUnitEvent(gg_trg_Lech, udg_u, EVENT_UNIT_DAMAGED)
    TriggerRegisterUnitEvent(gg_trg_AvtoCast, udg_u, EVENT_UNIT_DAMAGED)
    DisableTrigger(GetTriggeringTrigger())
end
--===========================================================================
function InitTrig_Spell_Copy_2_Copy()
    gg_trg_Spell_Copy_2_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Spell_Copy_2_Copy, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Spell_Copy_2_Copy, Condition(Trig_Spell_Copy_2_Copy_Conditions))
    TriggerAddAction(gg_trg_Spell_Copy_2_Copy, Trig_Spell_Copy_2_Copy_Actions)
end
--===========================================================================
-- Trigger: Lech Copy
--===========================================================================
function Trig_Lech_Copy_Actions()
    SetUnitLifeBJ(udg_u, GetUnitStateSwap(UNIT_STATE_LIFE, udg_u) + GetEventDamage())
end
--===========================================================================
function InitTrig_Lech_Copy()
    gg_trg_Lech_Copy=CreateTrigger()
    DisableTrigger(gg_trg_Lech_Copy)
    TriggerAddAction(gg_trg_Lech_Copy, Trig_Lech_Copy_Actions)
end
--===========================================================================
-- Trigger: Cast Copy
--===========================================================================
function Trig_Cast_Copy_Actions()
    EnableTrigger(gg_trg_Lech)
    CreateNUnitsAtLoc(1, FourCC('h0ML'), GetOwningPlayer(udg_u), GetUnitLoc(GetSpellAbilityUnit()), bj_UNIT_FACING)
    UnitAddAbilityBJ(FourCC('A1BS'), GetLastCreatedUnit())
    IssueTargetOrderBJ(GetLastCreatedUnit(), "purge", GetSpellAbilityUnit())
    UnitApplyTimedLifeBJ(1.00, FourCC('BTLF'), GetLastCreatedUnit())
    TriggerSleepAction(5.00 + ( 1.00 * I2R(GetUnitAbilityLevelSwapped(FourCC('A1CB'), GetSpellAbilityUnit())) ))
    DisableTrigger(gg_trg_Lech)
end
--===========================================================================
function InitTrig_Cast_Copy()
    gg_trg_Cast_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Cast_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Cast_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A1CB') then return end
        Trig_Cast_Copy_Actions()
    end)
end
--===========================================================================
-- Trigger: AvtoCast Copy
--===========================================================================
function Trig_AvtoCast_Copy_Conditions()
    return GetUnitStateSwap(UNIT_STATE_LIFE, udg_u) <= 400.00
end
function Trig_AvtoCast_Copy_Actions()
    IssueImmediateOrderBJ(udg_u, "stomp")
end
--===========================================================================
function InitTrig_AvtoCast_Copy()
    gg_trg_AvtoCast_Copy=CreateTrigger()
    TriggerAddCondition(gg_trg_AvtoCast_Copy, Condition(Trig_AvtoCast_Copy_Conditions))
    TriggerAddAction(gg_trg_AvtoCast_Copy, Trig_AvtoCast_Copy_Actions)
end
--===========================================================================
-- Trigger: DammyDeath Copy
--===========================================================================
function Trig_DammyDeath_Copy_Func001C()
    return GetUnitTypeId(GetDyingUnit()) == FourCC('h0ML')
end
function Trig_DammyDeath_Copy_Actions()
    if Trig_DammyDeath_Copy_Func001C() then
        RemoveUnit(GetDyingUnit())
    end
end
--===========================================================================
function InitTrig_DammyDeath_Copy()
    gg_trg_DammyDeath_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DammyDeath_Copy, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddAction(gg_trg_DammyDeath_Copy, Trig_DammyDeath_Copy_Actions)
end
--===========================================================================
-- Trigger: TakenDamage
--===========================================================================
function Trig_TakenDamage_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A1CA'), GetTriggerUnit()) == 1
end
function Trig_TakenDamage_Func001Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 50.00
end
function Trig_TakenDamage_Func001C()
    return GetUnitLifePercent(GetAttackedUnitBJ()) < 25.00
end
function Trig_TakenDamage_Actions()
    if Trig_TakenDamage_Func001C() then
        UnitAddAbilityBJ(FourCC('A1C9'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A1C9'), GetTriggerUnit(), 2)
    else
        if Trig_TakenDamage_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A1C9'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A1C9'), GetTriggerUnit(), 1)
        else
            UnitRemoveAbilityBJ(FourCC('A1C9'), GetTriggerUnit())
        end
    end
end
--===========================================================================
function InitTrig_TakenDamage()
    gg_trg_TakenDamage=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TakenDamage, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_TakenDamage, Condition(Trig_TakenDamage_Conditions))
    TriggerAddAction(gg_trg_TakenDamage, Trig_TakenDamage_Actions)
end