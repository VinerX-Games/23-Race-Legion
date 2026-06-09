
--===========================================================================
-- Trigger: Deathwing
--===========================================================================
function Trig_Deathwing_Conditions()
    return GetUnitAbilityLevel(GetTrainedUnit(), FourCC('A0YW')) > 0
end
function Trig_Deathwing_Actions()
    BlzStartUnitAbilityCooldown(GetTrainedUnit(), FourCC('A0YW'), 150)
end
--===========================================================================
function InitTrig_Deathwing()
    gg_trg_Deathwing=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Deathwing, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_Deathwing, Condition(Trig_Deathwing_Conditions))
    TriggerAddAction(gg_trg_Deathwing, Trig_Deathwing_Actions)
end
--===========================================================================
-- Trigger: TrainHeroGiveItem
--===========================================================================
function Trig_TrainHeroGiveItem_Conditions()
    return IsUnitType(GetTrainedUnit(), UNIT_TYPE_HERO) and not udg_HeroFirstYes[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]
end
function Trig_TrainHeroGiveItem_Actions()
    UnitAddItemByIdSwapped(FourCC('stwp'), GetTrainedUnit())
    UnitAddItemByIdSwapped(FourCC('I015'), GetTrainedUnit())
    udg_HeroFirstYes[GetConvertedPlayerId(GetOwningPlayer(GetTriggerUnit()))]=true
end
--===========================================================================
function InitTrig_TrainHeroGiveItem()
    gg_trg_TrainHeroGiveItem=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_TrainHeroGiveItem, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_TrainHeroGiveItem, Condition(Trig_TrainHeroGiveItem_Conditions))
    TriggerAddAction(gg_trg_TrainHeroGiveItem, Trig_TrainHeroGiveItem_Actions)
end
--===========================================================================
-- Trigger: LimitHero Exep
--===========================================================================
function Trig_LimitHero_Exep_Conditions()
    return IsUnitType(GetTrainedUnit(), UNIT_TYPE_HERO)
end
function Trig_LimitHero_Exep_Actions()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), GetTrainedUnitType(), 1)
end
--===========================================================================
function InitTrig_LimitHero_Exep()
    gg_trg_LimitHero_Exep=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LimitHero_Exep, EVENT_PLAYER_UNIT_TRAIN_START)
    TriggerAddCondition(gg_trg_LimitHero_Exep, Condition(Trig_LimitHero_Exep_Conditions))
    TriggerAddAction(gg_trg_LimitHero_Exep, Trig_LimitHero_Exep_Actions)
end
--===========================================================================
-- Trigger: fire
--===========================================================================
function Trig_fire_Conditions()
    return GetResearched() == FourCC('pa16')
end
function Trig_fire_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa47'), 0, Player(0))
end
--===========================================================================
function InitTrig_fire()
    gg_trg_fire=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_fire, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_fire, Condition(Trig_fire_Conditions))
    TriggerAddAction(gg_trg_fire, Trig_fire_Actions)
end
--===========================================================================
-- Trigger: fire1
--===========================================================================
function Trig_fire1_Conditions()
    return GetResearched() == FourCC('pa16')
end
function Trig_fire1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa47'), 1, Player(0))
end
--===========================================================================
function InitTrig_fire1()
    gg_trg_fire1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_fire1, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_fire1, Condition(Trig_fire1_Conditions))
    TriggerAddAction(gg_trg_fire1, Trig_fire1_Actions)
end
--===========================================================================
-- Trigger: earth
--===========================================================================
function Trig_earth_Conditions()
    return GetResearched() == FourCC('pa47')
end
function Trig_earth_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa16'), 0, Player(0))
end
--===========================================================================
function InitTrig_earth()
    gg_trg_earth=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_earth, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_earth, Condition(Trig_earth_Conditions))
    TriggerAddAction(gg_trg_earth, Trig_earth_Actions)
end
--===========================================================================
-- Trigger: earth1
--===========================================================================
function Trig_earth1_Conditions()
    return GetResearched() == FourCC('pa47')
end
function Trig_earth1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa16'), 1, Player(0))
end
--===========================================================================
function InitTrig_earth1()
    gg_trg_earth1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_earth1, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_earth1, Condition(Trig_earth1_Conditions))
    TriggerAddAction(gg_trg_earth1, Trig_earth1_Actions)
end
--===========================================================================
-- Trigger: Beer
--===========================================================================
function Trig_Beer_Conditions()
    return GetResearched() == FourCC('PA82')
end
function Trig_Beer_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA83'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Beer()
    gg_trg_Beer=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Beer, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Beer, Condition(Trig_Beer_Conditions))
    TriggerAddAction(gg_trg_Beer, Trig_Beer_Actions)
end
--===========================================================================
-- Trigger: BeerFin
--===========================================================================
function Trig_BeerFin_Conditions()
    return GetResearched() == FourCC('PA82')
end
function Trig_BeerFin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa22'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BeerFin()
    gg_trg_BeerFin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BeerFin, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_BeerFin, Condition(Trig_BeerFin_Conditions))
    TriggerAddAction(gg_trg_BeerFin, Trig_BeerFin_Actions)
end
--===========================================================================
-- Trigger: flot2 Copy O Copy
--===========================================================================
function Trig_flot2_Copy_O_Copy_Conditions()
    return GetResearched() == FourCC('PA82')
end
function Trig_flot2_Copy_O_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA83'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2_Copy_O_Copy()
    gg_trg_flot2_Copy_O_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2_Copy_O_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2_Copy_O_Copy, Condition(Trig_flot2_Copy_O_Copy_Conditions))
    TriggerAddAction(gg_trg_flot2_Copy_O_Copy, Trig_flot2_Copy_O_Copy_Actions)
end
--===========================================================================
-- Trigger: Geo
--===========================================================================
function Trig_Geo_Conditions()
    return GetResearched() == FourCC('PA83')
end
function Trig_Geo_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA82'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Geo()
    gg_trg_Geo=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Geo, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Geo, Condition(Trig_Geo_Conditions))
    TriggerAddAction(gg_trg_Geo, Trig_Geo_Actions)
end
--===========================================================================
-- Trigger: GeoFin
--===========================================================================
function Trig_GeoFin_Conditions()
    return GetResearched() == FourCC('PA83')
end
function Trig_GeoFin_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('pa06'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_GeoFin()
    gg_trg_GeoFin=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GeoFin, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_GeoFin, Condition(Trig_GeoFin_Conditions))
    TriggerAddAction(gg_trg_GeoFin, Trig_GeoFin_Actions)
end
--===========================================================================
-- Trigger: arm2 Copy O Copy
--===========================================================================
function Trig_arm2_Copy_O_Copy_Conditions()
    return GetResearched() == FourCC('PA83')
end
function Trig_arm2_Copy_O_Copy_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('PA82'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2_Copy_O_Copy()
    gg_trg_arm2_Copy_O_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2_Copy_O_Copy, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2_Copy_O_Copy, Condition(Trig_arm2_Copy_O_Copy_Conditions))
    TriggerAddAction(gg_trg_arm2_Copy_O_Copy, Trig_arm2_Copy_O_Copy_Actions)
end
--===========================================================================
-- Trigger: FarmBuild
--===========================================================================
PData = PData or {}

function Trig_FarmBuild_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('pa26') or GetUnitTypeId(GetTriggerUnit()) == FourCC('h0NZ')
end
function Trig_FarmBuild_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local phash= StringHash("Pfarm")
    PData[pi] = PData[pi] or {}
    PData[pi][phash] = (PData[pi][phash] or 0) + 1
    Ptiers(pi)
end
--===========================================================================
function InitTrig_FarmBuild()
    gg_trg_FarmBuild=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmBuild, EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    TriggerAddCondition(gg_trg_FarmBuild, Condition(Trig_FarmBuild_Conditions))
    TriggerAddAction(gg_trg_FarmBuild, Trig_FarmBuild_Actions)
end
--===========================================================================
-- Trigger: FarmLose
--===========================================================================
function Trig_FarmLose_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('pa26') or GetUnitTypeId(GetTriggerUnit()) == FourCC('h0NZ')
end
function Trig_FarmLose_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local phash= StringHash("Pfarm")
    PData[pi] = PData[pi] or {}
    PData[pi][phash] = (PData[pi][phash] or 0) - 1
    Ptiers(pi)
end
--===========================================================================
function InitTrig_FarmLose()
    gg_trg_FarmLose=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FarmLose, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_FarmLose, Condition(Trig_FarmLose_Conditions))
    TriggerAddAction(gg_trg_FarmLose, Trig_FarmLose_Actions)
end
--===========================================================================
-- Trigger: Provocation
--===========================================================================
function Trig_Provocation_Actions()
    UnitAddAbility(GetTriggerUnit(), FourCC('A1OH'))
    RemoveAbilityTimed(GetTriggerUnit() , FourCC('A1OH') , 7)
end
--===========================================================================
function InitTrig_Provocation()
    gg_trg_Provocation=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Provocation, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Provocation, function()
        if GetSpellAbilityId() ~= FourCC('PA78') then return end
        Trig_Provocation_Actions()
    end)
end
--===========================================================================
-- Trigger: PUnitTrained
--===========================================================================
function Trig_PUnitTrained_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1I7')) > 0
end
function Trig_PUnitTrained_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    local phash= StringHash("Pfarm")
    PData[pi] = PData[pi] or {}
    local count= PData[pi][phash] or 0
    local u= GetTrainedUnit()
    if Random(count , 200) then
        BlzSetUnitMaxHP(u, R2I(BlzGetUnitMaxHP(u) * 1.2))
        SetUnitLifePercentBJ(u, 100)
        UnitAddAbility(u, FourCC('A1I8'))
    end
    u=nil
end
--===========================================================================
function InitTrig_PUnitTrained()
    gg_trg_PUnitTrained=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PUnitTrained, EVENT_PLAYER_UNIT_TRAIN_FINISH)
    TriggerAddCondition(gg_trg_PUnitTrained, Condition(Trig_PUnitTrained_Conditions))
    TriggerAddAction(gg_trg_PUnitTrained, Trig_PUnitTrained_Actions)
end
--===========================================================================
-- Trigger: Anub Vozvratka
--===========================================================================
function Trig_Anub_Vozvratka_Conditions()
    return (( GetUnitAbilityLevelSwapped(FourCC('A1LJ'), BlzGetEventDamageTarget()) > 0 )) and (( GetEventDamage() >= 2.00 )) and (( GetUnitAbilityLevelSwapped(FourCC('A1LJ'), GetEventDamageSource()) == 0 ))
end
function Trig_Anub_Vozvratka_Actions()
    UnitDamageTargetBJ(BlzGetEventDamageTarget(), GetEventDamageSource(), 0.50 * I2R(GetHeroStatBJ(bj_HEROSTAT_STR, BlzGetEventDamageTarget(), false)), ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL)
end
--===========================================================================
function InitTrig_Anub_Vozvratka()
    gg_trg_Anub_Vozvratka=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Anub_Vozvratka, EVENT_PLAYER_UNIT_DAMAGED)
    TriggerAddCondition(gg_trg_Anub_Vozvratka, Condition(Trig_Anub_Vozvratka_Conditions))
    TriggerAddAction(gg_trg_Anub_Vozvratka, Trig_Anub_Vozvratka_Actions)
end
--===========================================================================
-- Trigger: Undermining
--
-- Abilities\Spells\Undead\Impale\ImpaleMissTarget.mdl
--===========================================================================
-- ?????????? ?????????? ?????? ?????? ???
--===================================================================================================================================
-- ???????? ???????, ??? ?????? ?????? ?? ?????
--===================================================================================================================================
--================================================================================================================================================================================
-- ???? 0 - ??? ???????
--================
function UnUgolMT()
    return bj_RADTODEG * Atan2(y2 - y1, x2 - x1)
end
function UnRastMT()
    local dx= x2 - x1
    local dy= y2 - y1
    return SquareRoot(dx * dx + dy * dy)
end
--function UnParabolaZ takes real h, real d, real x returns real
 -- return (4 * h / d) * (d - x) * (x / d)
--endfunction
--h - ???????????? ?????? ? ?????? ?? ???????? ?????????? (x = d / 2),
--d - ????? ?????????? ?? ????
--x - ?????????? ?? ???????? ???? ?? ?????, ??? ??????? ????? ?????? ?? ????????.
--================================================================================================================================================================================
-- ???? 1 - ???????? ?????
--================
function Trig_Undermining_Conditions()
    return GetSpellAbilityId() == UnSkill
end
--================================================================================================================================================================================
-- ???? 2 - ???????? ???????
--================
function Trig_Undermining_Actions()
    local GT= GetTriggerUnit()
    local x= GetUnitX(GT)
    local y= GetUnitY(GT)
    local x1= GetSpellTargetX()
    local y1= GetSpellTargetY()
    local l= UnRastMT(x , x1 , y , y1)
    ---------
    SetSoundPosition(gg_snd_ImpaleHit, x, y, 0)
    SetSoundVolume(gg_snd_ImpaleHit, PercentToInt(100, 127))
    PlaySoundBJ(gg_snd_ImpaleHit)
    ------
    local g= CreateGroup()       -- hit tracking
    local gg= CreateGroup()      -- enum reuse
    PauseUnit(GT, true)
    ShowUnit(GT, false)
    DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", x, y))
    local t= CreateTimer()
    TimerStart(t, 0.055, true, function()
        local dx= GetUnitX(GT)
        local dy= GetUnitY(GT)
        local ugol= UnUgolMT(dx , x1 , dy , y1)
        ---------
        local nx=dx + 70 * Cos(ugol * bj_DEGTORAD)
        local ny=dy + 70 * Sin(ugol * bj_DEGTORAD)
        if UnRastMT(x1 , dx , y1 , dy) > 70 and not IsTerrainPathable(nx, ny, PATHING_TYPE_FLYABILITY) then
            SetUnitX(GT, nx)
            SetUnitY(GT, ny)
            SetUnitFacing(GT, ugol)
            --------------------------------------
            GroupClear(gg)
            GroupEnumUnitsInRange(gg, nx, ny, 150, nil)
            while true do
                local un=FirstOfGroup(gg)
                if un == nil then break end
                if not IsUnitType(un, UNIT_TYPE_STRUCTURE) and IsUnitEnemy(un, GetOwningPlayer(GT)) and not IsUnitType(un, UNIT_TYPE_DEAD) and not IsUnitType(un, UNIT_TYPE_FLYING) and not IsUnitInGroup(un, g) then
                    UnitAddAbility(un, FourCC('Amrf'))
                    UnitRemoveAbility(un, FourCC('Amrf'))
                    GroupAddUnit(g, un)
                    local subUn = un
                    local subKol = 1
                    local subUpward = true
                    local subTimer = CreateTimer()
                    TimerStart(subTimer, 0.02, true, function()
                        SetUnitFlyHeight(subUn, subKol * 20, 0)
                        if subUpward then
                            subKol = subKol + 1
                            if subKol >= 13 then
                                subUpward = false
                            end
                        else
                            subKol = subKol - 1
                            if subKol <= 1 then
                                SetUnitFlyHeight(subUn, 0, 0)
                                DestroyTimer(subTimer)
                                local lvl=GetUnitAbilityLevel(GT, UnSkill)
                                local uron=UnKofDmg1 * lvl * GetHeroStr(GT, true) + lvl * UnKofDmg2
                                UnitDamageTarget(GT, subUn, uron, true, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
                                DestroyEffect(AddSpecialEffectTarget("AbilitiesSpellsDemonDemonBoltImpactDemonBoltImpact.mdl", subUn, "orign"))
                            end
                        end
                    end)
                end
                GroupRemoveUnit(gg, un)
            end
            -----------------------------------------
        else
            DestroyGroup(g)
            DestroyGroup(gg)
            DestroyTimer(t)
            SetUnitFlyHeight(GT, 0, 0)
            DestroyEffect(AddSpecialEffect("AbilitiesSpellsOtherVolcanoVolcanoDeath.mdl", dx, dy))
            PauseUnit(GT, false)
            ShowUnit(GT, true)
            SelectUnitAddForPlayer(GT, GetOwningPlayer(GT))
        end
    end)
    ---------
    GT=nil
    t=nil
end
--===========================================================================
function InitTrig_Undermining()
    gg_trg_Undermining=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Undermining, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_Undermining, Condition(Trig_Undermining_Conditions))
    TriggerAddAction(gg_trg_Undermining, Trig_Undermining_Actions)
end
--===========================================================================
-- Trigger: PassiveAdal
--===========================================================================
function Trig_PassiveAdal_Conditions()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC('B084')) > 0 and not IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO) and GetEventDamage() >= GetUnitState(GetTriggerUnit(), UNIT_STATE_LIFE) --?? ????
end
function Adal()
    return GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1L6')) > 0 --??????
end
function Trig_PassiveAdal_Actions()
    local g= CreateGroup()
    local u= GetTriggerUnit()
    local u2
    GroupEnumUnitsInRangeCounted(g, GetUnitX(u), GetUnitY(u), 500, Adal, 1)
    u2=FirstOfGroup(g)
    if GetRandomInt(1, 4) + 0.25 * GetUnitAbilityLevel(u2, FourCC('A1L6')) > 3 and GetUnitState(u2, UNIT_STATE_MANA) > 50 then --??????
        SetUnitManaBJ(u2, GetUnitState(u2, UNIT_STATE_MANA) - 50)
        SetUnitLifePercentBJ(u, 50)
        RemoveEffectTimed(AddSpecialEffect("AbilitiesSpellsHumanResurrectResurrectTarget.mdl", GetUnitX(u), GetUnitY(u)) , 3)
    end
    
    DestroyGroup(g)
    g=nil
    u=nil
    u2=nil
end
--===========================================================================
function InitTrig_PassiveAdal()
    gg_trg_PassiveAdal=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PassiveAdal, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddCondition(gg_trg_PassiveAdal, Condition(Trig_PassiveAdal_Conditions))
    TriggerAddAction(gg_trg_PassiveAdal, Trig_PassiveAdal_Actions)
end
--===========================================================================
-- Trigger: ADall
--
-- Default melee game initialization for all players
--===========================================================================
function Trig_ADall_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "healingwave", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_ADall()
    gg_trg_ADall=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_ADall, EVENT_PLAYER_UNIT_SPELL_CAST)
    TriggerAddAction(gg_trg_ADall, function()
        if GetSpellAbilityId() ~= FourCC('A1L1') then return end
        Trig_ADall_Actions()
    end)
end
--===========================================================================
-- Trigger: Rexan
--===========================================================================
function Trig_Rexan_Conditions()
    return GetLearnedSkillBJ() == FourCC('A1NW')
end
function Trig_Rexan_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A1NW'), GetTriggerUnit()) == 1
end
function Trig_Rexan_Actions()
    if Trig_Rexan_Func001C() then
        UnitAddAbilityBJ(FourCC('A1NY'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A1NY'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1NW'), GetTriggerUnit()))
    else
        SetUnitAbilityLevelSwapped(FourCC('A1NY'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A1NW'), GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_Rexan()
    gg_trg_Rexan=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Rexan, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Rexan, Condition(Trig_Rexan_Conditions))
    TriggerAddAction(gg_trg_Rexan, Trig_Rexan_Actions)
end
--===========================================================================
-- Trigger: OgresHpSpell2
--===========================================================================
function Trig_OgresHpSpell2_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A173'), GetTriggerUnit()) == 2
end
function Trig_OgresHpSpell2_Func001Func001Func007C()
    return GetUnitLifePercent(GetTriggerUnit()) < 95.00
end
function Trig_OgresHpSpell2_Func001Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 70.00
end
function Trig_OgresHpSpell2_Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 45.00
end
function Trig_OgresHpSpell2_Actions()
    if Trig_OgresHpSpell2_Func001C() then
        UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 3)
    else
        if Trig_OgresHpSpell2_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 2)
        else
            if Trig_OgresHpSpell2_Func001Func001Func007C() then
                UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 1)
            else
                UnitRemoveAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            end
        end
    end
end
--===========================================================================
function InitTrig_OgresHpSpell2()
    gg_trg_OgresHpSpell2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OgresHpSpell2, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_OgresHpSpell2, Condition(Trig_OgresHpSpell2_Conditions))
    TriggerAddAction(gg_trg_OgresHpSpell2, Trig_OgresHpSpell2_Actions)
end
--===========================================================================
-- Trigger: OrgesHpSpell
--===========================================================================
function Trig_OrgesHpSpell_Conditions()
    return GetUnitAbilityLevelSwapped(FourCC('A173'), GetTriggerUnit()) == 1
end
function Trig_OrgesHpSpell_Func001Func001Func007C()
    return GetUnitLifePercent(GetTriggerUnit()) < 75.00
end
function Trig_OrgesHpSpell_Func001Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 50.00
end
function Trig_OrgesHpSpell_Func001C()
    return GetUnitLifePercent(GetTriggerUnit()) < 25.00
end
function Trig_OrgesHpSpell_Actions()
    if Trig_OrgesHpSpell_Func001C() then
        UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
        UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 3)
        SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 3)
    else
        if Trig_OrgesHpSpell_Func001Func001C() then
            UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
            UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
            SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 2)
            SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 2)
        else
            if Trig_OrgesHpSpell_Func001Func001Func007C() then
                UnitAddAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitAddAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                SetUnitAbilityLevelSwapped(FourCC('A0WY'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WX'), GetTriggerUnit(), 1)
                SetUnitAbilityLevelSwapped(FourCC('A0WW'), GetTriggerUnit(), 1)
            else
                UnitRemoveAbilityBJ(FourCC('A0WW'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WX'), GetTriggerUnit())
                UnitRemoveAbilityBJ(FourCC('A0WY'), GetTriggerUnit())
            end
        end
    end
end
--===========================================================================
function InitTrig_OrgesHpSpell()
    gg_trg_OrgesHpSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_OrgesHpSpell, EVENT_PLAYER_UNIT_ATTACKED)
    TriggerAddCondition(gg_trg_OrgesHpSpell, Condition(Trig_OrgesHpSpell_Conditions))
    TriggerAddAction(gg_trg_OrgesHpSpell, Trig_OrgesHpSpell_Actions)
end
--===========================================================================
-- Trigger: Gruul
--===========================================================================
function Trig_Gruul_Conditions()
    return (( GetLearnedSkillBJ() == FourCC('A18S') )) and (( GetUnitAbilityLevelSwapped(FourCC('A18S'), GetTriggerUnit()) >= 1 ))
end
function Trig_Gruul_Actions()
    UnitAddAbilityBJ(FourCC('A18T'), GetTriggerUnit())
    SetUnitAbilityLevelSwapped(FourCC('A18T'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A18S'), GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Gruul()
    gg_trg_Gruul=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Gruul, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_Gruul, Condition(Trig_Gruul_Conditions))
    TriggerAddAction(gg_trg_Gruul, Trig_Gruul_Actions)
end
--===========================================================================
-- Trigger: GruulSpell
--===========================================================================
function Trig_GruulSpell_Actions()
    local pi= GetPlayerId(GetOwningPlayer(GetTriggerUnit()))
    Gruul[pi]=GetSpellAbilityUnit()
    EnableTrigger(gg_trg_RRR)
    
    -- ????? ????? ?????? ?????? 1.10+ 0.15 ?????? ???
    TriggerSleepAction(1.10 + ( 0.15 * I2R(GetUnitAbilityLevel(Gruul[pi], FourCC('A18Q'))) ))
    
    
    DisableTrigger(gg_trg_RRR)
    -- ??????? ??????????
    Gruul[pi]=nil
end
--===========================================================================
function InitTrig_GruulSpell()
    gg_trg_GruulSpell=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GruulSpell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_GruulSpell, function()
        if GetSpellAbilityId() ~= FourCC('A18Q') then return end
        Trig_GruulSpell_Actions()
    end)
end
--===========================================================================
-- Trigger: BegYel
--===========================================================================
function Trig_BegYel_Conditions()
    return GetResearched() == FourCC('R0GH')
end
function Trig_BegYel_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegYel_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegYel_Actions()
    if Trig_BegYel_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_BegYel_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_BegYel()
    gg_trg_BegYel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegYel, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegYel, Condition(Trig_BegYel_Conditions))
    TriggerAddAction(gg_trg_BegYel, Trig_BegYel_Actions)
end
--===========================================================================
-- Trigger: CanYel
--===========================================================================
function Trig_CanYel_Conditions()
    return GetResearched() == FourCC('R0GH')
end
function Trig_CanYel_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanYel_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanYel_Actions()
    if Trig_CanYel_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_CanYel_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanYel()
    gg_trg_CanYel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanYel, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanYel, Condition(Trig_CanYel_Conditions))
    TriggerAddAction(gg_trg_CanYel, Trig_CanYel_Actions)
end
--===========================================================================
-- Trigger: FinYel
--===========================================================================
function Trig_FinYel_Conditions()
    return GetResearched() == FourCC('R0GH')
end
function Trig_FinYel_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03Q'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinYel()
    gg_trg_FinYel=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinYel, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinYel, Condition(Trig_FinYel_Conditions))
    TriggerAddAction(gg_trg_FinYel, Trig_FinYel_Actions)
end
--===========================================================================
-- Trigger: BegRed
--===========================================================================
function Trig_BegRed_Conditions()
    return GetResearched() == FourCC('R0GG')
end
function Trig_BegRed_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegRed_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegRed_Actions()
    if Trig_BegRed_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_BegRed_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_BegRed()
    gg_trg_BegRed=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegRed, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegRed, Condition(Trig_BegRed_Conditions))
    TriggerAddAction(gg_trg_BegRed, Trig_BegRed_Actions)
end
--===========================================================================
-- Trigger: CanRed
--===========================================================================
function Trig_CanRed_Conditions()
    return GetResearched() == FourCC('R0GG')
end
function Trig_CanRed_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GF'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanRed_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanRed_Actions()
    if Trig_CanRed_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_CanRed_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GF'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanRed()
    gg_trg_CanRed=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanRed, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanRed, Condition(Trig_CanRed_Conditions))
    TriggerAddAction(gg_trg_CanRed, Trig_CanRed_Actions)
end
--===========================================================================
-- Trigger: FinRed
--===========================================================================
function Trig_FinRed_Conditions()
    return GetResearched() == FourCC('R0GG')
end
function Trig_FinRed_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03S'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinRed()
    gg_trg_FinRed=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinRed, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinRed, Condition(Trig_FinRed_Conditions))
    TriggerAddAction(gg_trg_FinRed, Trig_FinRed_Actions)
end
--===========================================================================
-- Trigger: BegBlue
--===========================================================================
function Trig_BegBlue_Conditions()
    return GetResearched() == FourCC('R0GF')
end
function Trig_BegBlue_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegBlue_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_BegBlue_Actions()
    if Trig_BegBlue_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_BegBlue_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 0, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_BegBlue()
    gg_trg_BegBlue=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegBlue, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegBlue, Condition(Trig_BegBlue_Conditions))
    TriggerAddAction(gg_trg_BegBlue, Trig_BegBlue_Actions)
end
--===========================================================================
-- Trigger: CanBlue
--===========================================================================
function Trig_CanBlue_Conditions()
    return GetResearched() == FourCC('R0GF')
end
function Trig_CanBlue_Func001C()
    return GetPlayerTechCountSimple(FourCC('R0GG'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanBlue_Func002C()
    return GetPlayerTechCountSimple(FourCC('R0GH'), GetOwningPlayer(GetTriggerUnit())) ~= 0
end
function Trig_CanBlue_Actions()
    if Trig_CanBlue_Func001C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GH'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
    if Trig_CanBlue_Func002C() then
        SetPlayerTechMaxAllowedSwap(FourCC('R0GG'), 1, GetOwningPlayer(GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_CanBlue()
    gg_trg_CanBlue=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanBlue, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanBlue, Condition(Trig_CanBlue_Conditions))
    TriggerAddAction(gg_trg_CanBlue, Trig_CanBlue_Actions)
end
--===========================================================================
-- Trigger: FinBlue
--===========================================================================
function Trig_FinBlue_Conditions()
    return GetResearched() == FourCC('R0GF')
end
function Trig_FinBlue_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03R'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinBlue()
    gg_trg_FinBlue=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinBlue, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinBlue, Condition(Trig_FinBlue_Conditions))
    TriggerAddAction(gg_trg_FinBlue, Trig_FinBlue_Actions)
end
--===========================================================================
-- Trigger: Begred
--===========================================================================
function Trig_Begred_Conditions()
    return GetResearched() == FourCC('R0GI')
end
function Trig_Begred_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Begred()
    gg_trg_Begred=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Begred, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_Begred, Condition(Trig_Begred_Conditions))
    TriggerAddAction(gg_trg_Begred, Trig_Begred_Actions)
end
--===========================================================================
-- Trigger: Canred
--===========================================================================
function Trig_Canred_Conditions()
    return GetResearched() == FourCC('R0GI')
end
function Trig_Canred_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Canred()
    gg_trg_Canred=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Canred, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_Canred, Condition(Trig_Canred_Conditions))
    TriggerAddAction(gg_trg_Canred, Trig_Canred_Actions)
end
--===========================================================================
-- Trigger: Finred
--===========================================================================
function Trig_Finred_Conditions()
    return GetResearched() == FourCC('R0GI')
end
function Trig_Finred_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03V'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_Finred()
    gg_trg_Finred=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Finred, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_Finred, Condition(Trig_Finred_Conditions))
    TriggerAddAction(gg_trg_Finred, Trig_Finred_Actions)
end
--===========================================================================
-- Trigger: BegWhite
--===========================================================================
function Trig_BegWhite_Conditions()
    return GetResearched() == FourCC('R0GK')
end
function Trig_BegWhite_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegWhite()
    gg_trg_BegWhite=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegWhite, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegWhite, Condition(Trig_BegWhite_Conditions))
    TriggerAddAction(gg_trg_BegWhite, Trig_BegWhite_Actions)
end
--===========================================================================
-- Trigger: CanWhite
--===========================================================================
function Trig_CanWhite_Conditions()
    return GetResearched() == FourCC('R0GK')
end
function Trig_CanWhite_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GJ'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CanWhite()
    gg_trg_CanWhite=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanWhite, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanWhite, Condition(Trig_CanWhite_Conditions))
    TriggerAddAction(gg_trg_CanWhite, Trig_CanWhite_Actions)
end
--===========================================================================
-- Trigger: FinWhite
--===========================================================================
function Trig_FinWhite_Conditions()
    return GetResearched() == FourCC('R0GK')
end
function Trig_FinWhite_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03U'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinWhite()
    gg_trg_FinWhite=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinWhite, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinWhite, Condition(Trig_FinWhite_Conditions))
    TriggerAddAction(gg_trg_FinWhite, Trig_FinWhite_Actions)
end
--===========================================================================
-- Trigger: BegBlack
--===========================================================================
function Trig_BegBlack_Conditions()
    return GetResearched() == FourCC('R0GJ')
end
function Trig_BegBlack_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 0, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_BegBlack()
    gg_trg_BegBlack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_BegBlack, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_BegBlack, Condition(Trig_BegBlack_Conditions))
    TriggerAddAction(gg_trg_BegBlack, Trig_BegBlack_Actions)
end
--===========================================================================
-- Trigger: CanBlack
--===========================================================================
function Trig_CanBlack_Conditions()
    return GetResearched() == FourCC('R0GJ')
end
function Trig_CanBlack_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R0GI'), 1, GetOwningPlayer(GetTriggerUnit()))
    SetPlayerTechMaxAllowedSwap(FourCC('R0GK'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_CanBlack()
    gg_trg_CanBlack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_CanBlack, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_CanBlack, Condition(Trig_CanBlack_Conditions))
    TriggerAddAction(gg_trg_CanBlack, Trig_CanBlack_Actions)
end
--===========================================================================
-- Trigger: FinBlack
--===========================================================================
function Trig_FinBlack_Conditions()
    return GetResearched() == FourCC('R0GJ')
end
function Trig_FinBlack_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('o03T'), - 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_FinBlack()
    gg_trg_FinBlack=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_FinBlack, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerAddCondition(gg_trg_FinBlack, Condition(Trig_FinBlack_Conditions))
    TriggerAddAction(gg_trg_FinBlack, Trig_FinBlack_Actions)
end
--===========================================================================
-- Trigger: UltDanath
--
-- ??? ??????? ???????. ??????? ?????????? ??????????.
-- ? ????????: (Ability beng cast) ????? ""
-- ???????? ????????:
-- 1. ??????? ????????? ?????????? ?????
-- 2. ???? ????? ?? ???????? ??????????? ??????????? "", ??????????? ""
-- 3. ? ????????? ?????????? ????? ????????? ????? ?? ???????? ????????? ???????????
-- 4. ??????? ??????? ? ????? ????? ?????????????? ???????????
-- 5. ?? ????????? ??????? ???????? ? ????? ?????????????? ???????????
-- ? 5 ?????? 'AEev' - ??? ??? ??????????? '??????? ????????'
-- ???? ???-?? ?? ??????? - ?????????.
-- by Dragonear for xgm.guru
--===========================================================================
function Trig_UltDanath_Actions()
    local u= GetTriggerUnit()
    UnitAddAbility(u, FourCC('A17T'))
    RemoveAbilityTimed(u , FourCC('A17T') , 60)
    u=nil
end
--===========================================================================
function InitTrig_UltDanath()
    gg_trg_UltDanath=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_UltDanath, EVENT_PLAYER_UNIT_SPELL_CHANNEL)
    TriggerAddAction(gg_trg_UltDanath, function()
        if GetSpellAbilityId() ~= FourCC('A17S') then return end
        Trig_UltDanath_Actions()
    end)
end
--===========================================================================
-- Trigger: GeneralRegen
--===========================================================================
function Trig_GeneralRegen_Conditions()
    return GetLearnedSkillBJ() == FourCC('A0Y8')
end
function Trig_GeneralRegen_Func001C()
    return GetUnitAbilityLevelSwapped(FourCC('A0Y8'), GetTriggerUnit()) == 1
end
function Trig_GeneralRegen_Actions()
    if Trig_GeneralRegen_Func001C() then
        UnitAddAbilityBJ(FourCC('A104'), GetTriggerUnit())
        SetUnitAbilityLevelSwapped(FourCC('A104'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A0Y8'), GetTriggerUnit()))
    else
        SetUnitAbilityLevelSwapped(FourCC('A104'), GetTriggerUnit(), GetUnitAbilityLevelSwapped(FourCC('A0Y8'), GetTriggerUnit()))
    end
end
--===========================================================================
function InitTrig_GeneralRegen()
    gg_trg_GeneralRegen=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_GeneralRegen, EVENT_PLAYER_HERO_SKILL)
    TriggerAddCondition(gg_trg_GeneralRegen, Condition(Trig_GeneralRegen_Conditions))
    TriggerAddAction(gg_trg_GeneralRegen, Trig_GeneralRegen_Actions)
end
--===========================================================================
-- Trigger: Pribavka k zoloty
--===========================================================================
function Trig_Pribavka_k_zoloty_Actions()
    AdjustPlayerStateBJ(2000 * GetUnitAbilityLevelSwapped(FourCC('A0ZN'), GetTriggerUnit()), GetOwningPlayer(GetTriggerUnit()), PLAYER_STATE_RESOURCE_GOLD)
end
--===========================================================================
function InitTrig_Pribavka_k_zoloty()
    gg_trg_Pribavka_k_zoloty=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Pribavka_k_zoloty, EVENT_PLAYER_UNIT_SPELL_FINISH)
    TriggerAddAction(gg_trg_Pribavka_k_zoloty, function()
        if GetSpellAbilityId() ~= FourCC('A0ZN') then return end
        Trig_Pribavka_k_zoloty_Actions()
    end)
end