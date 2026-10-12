
--===========================================================================
-- Trigger: LordWave
--===========================================================================
function Trig_LordWave_Func010C()
    return GetSpellAbilityId() == FourCC('NQ02')
end
function Trig_LordWave_Conditions()
    return Trig_LordWave_Func010C()
end
function Trig_LordWave_Func001002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('lord')
end
function Trig_LordWave_Func002002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('nq01')
end
function Trig_LordWave_Actions()
    local caster = GetTriggerUnit()
    local spellLvl = GetUnitAbilityLevel(caster, FourCC('NQ14'))
    local tx, ty = GetSpellTargetX(), GetSpellTargetY()
    local g = CreateGroup()
    local gMell = CreateGroup()
    GroupEnumUnitsInRange(g, tx, ty, 700.0, CachedFilter(Trig_LordWave_Func001002003))
    GroupEnumUnitsInRange(gMell, tx, ty, 700.0, CachedFilter(Trig_LordWave_Func002002003))
    GroupAddGroup(gMell, g)
    DestroyGroup(gMell)

    local affected = CreateGroup()
    local sz = BlzGroupGetSize(g)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil then
            UnitAddAbility(u, FourCC('NQ14'))
            SetUnitAbilityLevel(u, FourCC('NQ14'), spellLvl)
            IssuePointOrder(u, "carrionswarm", tx, ty)
            BlzUnitHideAbility(u, FourCC('NQ14'), true)
            GroupAddUnit(affected, u)
        end
    end
    DestroyGroup(g)

    local t = CreateTimer()
    TimerStart(t, 6.0, false, function()
        DestroyTimer(t)
        local afSz = BlzGroupGetSize(affected)
        for i = 0, afSz - 1 do
            local u = BlzGroupUnitAt(affected, i)
            if u ~= nil then
                UnitRemoveAbility(u, FourCC('NQ14'))
            end
        end
        DestroyGroup(affected)
    end)
end
--===========================================================================
function InitTrig_LordWave()
    gg_trg_LordWave=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LordWave, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_LordWave, Condition(Trig_LordWave_Conditions))
    TriggerAddAction(gg_trg_LordWave, Trig_LordWave_Actions)
end
--===========================================================================
-- Trigger: MassBaff
--===========================================================================
function Trig_MassBaff_Func010C()
    return GetSpellAbilityId() == FourCC('NQ07')
end
function Trig_MassBaff_Conditions()
    return Trig_MassBaff_Func010C()
end
function Trig_MassBaff_Actions()
    local caster = GetTriggerUnit()
    local p = GetTriggerPlayer()
    local spellLvl = GetUnitAbilityLevel(caster, FourCC('NQ07'))
    local g = GetUnitsOfPlayerAndTypeId(p, FourCC('lord'))
    local gMell = GetUnitsOfPlayerAndTypeId(p, FourCC('nq01'))
    GroupAddGroup(gMell, g)
    DestroyGroup(gMell)

    local affected = CreateGroup()
    local sz = BlzGroupGetSize(g)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil then
            UnitAddAbility(u, FourCC('NQ08'))
            SetUnitAbilityLevel(u, FourCC('NQ08'), spellLvl)
            IssueImmediateOrder(u, "roar")
            BlzUnitHideAbility(u, FourCC('NQ08'), true)
            GroupAddUnit(affected, u)
        end
    end
    DestroyGroup(g)

    local t = CreateTimer()
    TimerStart(t, 3.0, false, function()
        DestroyTimer(t)
        local afSz = BlzGroupGetSize(affected)
        for i = 0, afSz - 1 do
            local u = BlzGroupUnitAt(affected, i)
            if u ~= nil then
                UnitRemoveAbility(u, FourCC('NQ08'))
            end
        end
        DestroyGroup(affected)
    end)
end
--===========================================================================
function InitTrig_MassBaff()
    gg_trg_MassBaff=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_MassBaff, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_MassBaff, Condition(Trig_MassBaff_Conditions))
    TriggerAddAction(gg_trg_MassBaff, Trig_MassBaff_Actions)
end
--===========================================================================
-- Trigger: LordsAssist
--===========================================================================
function Trig_LordsAssist_Func010C()
    return GetSpellAbilityId() == FourCC('NQ03')
end
function Trig_LordsAssist_Conditions()
    return Trig_LordsAssist_Func010C()
end
function Trig_LordsAssist_Func001002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('lord')
end
function Trig_LordsAssist_Func002002003()
    return GetUnitTypeId(GetFilterUnit()) == FourCC('nq01')
end
function Trig_LordsAssist_Actions()
    local caster = GetTriggerUnit()
    local spellTarget = GetSpellTargetUnit()
    local spellLvl = GetUnitAbilityLevel(caster, FourCC('NQ03'))
    local tx, ty = GetSpellTargetX(), GetSpellTargetY()
    local g = CreateGroup()
    local gMell = CreateGroup()
    GroupEnumUnitsInRange(g, tx, ty, 512.0, CachedFilter(Trig_LordsAssist_Func001002003))
    GroupEnumUnitsInRange(gMell, tx, ty, 512.0, CachedFilter(Trig_LordsAssist_Func002002003))
    GroupAddGroup(gMell, g)
    DestroyGroup(gMell)

    local affected = CreateGroup()
    local sz = BlzGroupGetSize(g)
    for i = 0, sz - 1 do
        local u = BlzGroupUnitAt(g, i)
        if u ~= nil then
            UnitAddAbility(u, FourCC('NQ09'))
            SetUnitAbilityLevel(u, FourCC('NQ09'), spellLvl)
            IssueTargetOrder(u, "manaburn", spellTarget)
            BlzUnitHideAbility(u, FourCC('NQ09'), true)
            GroupAddUnit(affected, u)
        end
    end
    DestroyGroup(g)

    local t = CreateTimer()
    TimerStart(t, 3.0, false, function()
        DestroyTimer(t)
        local afSz = BlzGroupGetSize(affected)
        for i = 0, afSz - 1 do
            local u = BlzGroupUnitAt(affected, i)
            if u ~= nil then
                UnitRemoveAbility(u, FourCC('NQ09'))
            end
        end
        DestroyGroup(affected)
    end)
end
--===========================================================================
function InitTrig_LordsAssist()
    gg_trg_LordsAssist=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LordsAssist, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_LordsAssist, Condition(Trig_LordsAssist_Conditions))
    TriggerAddAction(gg_trg_LordsAssist, Trig_LordsAssist_Actions)
end
--===========================================================================
-- Trigger: Lord
--===========================================================================
function Trig_Lord_Func001Func001Func001C()
    return (( GetUnitAbilityLevelSwapped(FourCC('NQ06'), GetTriggerUnit()) == 2 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('lord'), GetTriggerPlayer()) < 3 )) and (( GetUnitTypeId(GetSpellTargetUnit()) == FourCC('u019') ))
end
function Trig_Lord_Func001Func001C()
    return Trig_Lord_Func001Func001Func001C()
end
function Trig_Lord_Func001Func002C()
    return (( GetUnitAbilityLevelSwapped(FourCC('NQ06'), GetTriggerUnit()) == 1 )) and (( CountLivingPlayerUnitsOfTypeId(FourCC('lord'), GetTriggerPlayer()) == 0 )) and (( GetUnitTypeId(GetSpellTargetUnit()) == FourCC('u019') ))
end
function Trig_Lord_Func001C()
    return Trig_Lord_Func001Func002C()
end
function Trig_Lord_Actions()
    if Trig_Lord_Func001C() then
        ReplaceUnitBJ(GetSpellTargetUnit(), FourCC('lorE'), bj_UNIT_STATE_METHOD_DEFAULTS)
        UnitApplyTimedLifeBJ(60.00, FourCC('BTLF'), GetLastReplacedUnitBJ())
    else
        if Trig_Lord_Func001Func001C() then
            ReplaceUnitBJ(GetSpellTargetUnit(), FourCC('lorE'), bj_UNIT_STATE_METHOD_DEFAULTS)
            UnitApplyTimedLifeBJ(60.00, FourCC('BTLF'), GetLastReplacedUnitBJ())
        else
            DoNothing()
        end
    end
end
--===========================================================================
function InitTrig_Lord()
    gg_trg_Lord=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Lord, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Lord, function()
        if GetSpellAbilityId() ~= FourCC('NQ06') then return end
        Trig_Lord_Actions()
    end)
end
--===========================================================================
-- Trigger: LordBirth
--===========================================================================
function Trig_LordBirth_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('lorE')
end
function Trig_LordBirth_Actions()
    local u = GetTriggerUnit()
    CreateUnit(GetTriggerPlayer(), FourCC('lord'), GetUnitX(u), GetUnitY(u), bj_UNIT_FACING)
end
--===========================================================================
function InitTrig_LordBirth()
    gg_trg_LordBirth=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_LordBirth, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_LordBirth, Condition(Trig_LordBirth_Conditions))
    TriggerAddAction(gg_trg_LordBirth, Trig_LordBirth_Actions)
end
--===========================================================================
-- Trigger: NaxramasKills
--===========================================================================
function Trig_NaxramasKills_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e00D')
end
function Trig_NaxramasKills_Func003A()
    KillUnit(GetEnumUnit())
end
function Trig_NaxramasKills_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_3138")
    ForGroupDestroy(GetUnitsInRectAll(gg_rct_DeathNaxramas), Trig_NaxramasKills_Func003A)
end
--===========================================================================
function InitTrig_NaxramasKills()
    gg_trg_NaxramasKills=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_NaxramasKills, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_NaxramasKills, Condition(Trig_NaxramasKills_Conditions))
    TriggerAddAction(gg_trg_NaxramasKills, Trig_NaxramasKills_Actions)
end
--===========================================================================
-- Trigger: DalaranKills
--===========================================================================
function Trig_DalaranKills_Conditions()
    return GetUnitTypeId(GetTriggerUnit()) == FourCC('e00C')
end
function Trig_DalaranKills_Func003A()
    KillUnit(GetEnumUnit())
end
function Trig_DalaranKills_Actions()
    DisplayTextToForce(GetPlayersAll(), "TRIGSTR_3139")
    ForGroupDestroy(GetUnitsInRectAll(gg_rct_DeathDalaran), Trig_DalaranKills_Func003A)
end
--===========================================================================
function InitTrig_DalaranKills()
    gg_trg_DalaranKills=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_DalaranKills, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_DalaranKills, Condition(Trig_DalaranKills_Conditions))
    TriggerAddAction(gg_trg_DalaranKills, Trig_DalaranKills_Actions)
end