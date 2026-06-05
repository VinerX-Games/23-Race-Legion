-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/spells_common.lua — SpellSleepAOE, SanctifiedEnchantment, Portal system
-- ============================================================

-- ============================================================
-- LIBRARY_SpellSleepAOE
-- ============================================================

G.SpellSleepAOE___SpellHero = FourCC('A06P')
G.SpellSleepAOE___SpellCast = FourCC('A06O')
G.SpellSleepAOE___SpellOrder = "sleep"
G.SpellSleepAOE___DummyID = FourCC('u000')
G.SpellSleepAOE___DummyOwner = Player(PLAYER_NEUTRAL_PASSIVE)
G.SpellSleepAOE___DummyUnit = nil

function SpellSleepAOE___getRange(level)
    local range = {}
    range[1] = 185
    range[2] = 275
    range[3] = 365
    range[4] = 430
    return range[level]
end

function SpellSleepAOE___DummyCastBuff(caster, target)
    if GetUnitState(target, UNIT_STATE_LIFE) > 0.405 then
        SetUnitX(G.SpellSleepAOE___DummyUnit, GetUnitX(target))
        SetUnitY(G.SpellSleepAOE___DummyUnit, GetUnitY(target))
        SetUnitAbilityLevel(G.SpellSleepAOE___DummyUnit, G.SpellSleepAOE___SpellCast, GetUnitAbilityLevel(caster, G.SpellSleepAOE___SpellHero))
        IssueTargetOrder(G.SpellSleepAOE___DummyUnit, G.SpellSleepAOE___SpellOrder, target)
    end
end

local function SpellSleepAOE___anon__2()
    return GetUnitState(GetFilterUnit(), UNIT_STATE_LIFE) > 0.405
        and not IsPlayerAlly(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetFilterUnit()))
        and not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE)
end

local function SpellSleepAOE___anon__1()
    local loc = GetSpellTargetLoc()
    local x = GetLocationX(loc)
    local y = GetLocationY(loc)
    local g = CreateGroup()
    local u
    GroupEnumUnitsInRange(g, x, y, SpellSleepAOE___getRange(GetUnitAbilityLevel(GetTriggerUnit(), G.SpellSleepAOE___SpellHero)), Condition(SpellSleepAOE___anon__2))
    repeat
        u = FirstOfGroup(g)
        if u ~= nil then
            SpellSleepAOE___DummyCastBuff(GetTriggerUnit(), u)
            GroupRemoveUnit(g, u)
        end
    until u == nil
    RemoveLocation(loc)
    DestroyGroup(g)
end

function SpellSleepAOE___onInit()
    local t = CreateTrigger()
    G.SpellSleepAOE___DummyUnit = CreateUnit(G.SpellSleepAOE___DummyOwner, G.SpellSleepAOE___DummyID, 0, 0, 0)
    UnitAddAbility(G.SpellSleepAOE___DummyUnit, G.SpellSleepAOE___SpellCast)
    for i = 0, bj_MAX_PLAYER_SLOTS - 1 do
        TriggerRegisterPlayerUnitEvent(t, Player(i), EVENT_PLAYER_UNIT_SPELL_EFFECT, nil)
    end
    TriggerAddCondition(t, Condition(function()
        return G.SpellSleepAOE___SpellHero == GetSpellAbilityId()
    end))
    TriggerAddAction(t, SpellSleepAOE___anon__1)
end

-- ============================================================
-- LIBRARY_SanctifiedEnchantment
-- ============================================================

G.SanctifiedEnchantment_SkillId = FourCC('A1K0')
G.SanctifiedEnchantment_SkillBookId = FourCC('A1JU')
G.SanctifiedEnchantment_SkillAbilityStatusId = FourCC('A1JW')
G.SanctifiedEnchantment_SkillBuffStatusId = FourCC('B07Z')
G.SanctifiedEnchantment_AbilitySplashId = FourCC('A1JX')
G.SanctifiedEnchantment_MAXLVL = 4
G.SanctifiedEnchantment_Key = 8
G.SanctifiedEnchantment_Date = 0.05
G.SanctifiedEnchantment_BuffDuration = {}

-- Struct replacement: SanctifiedEnchantment instance arrays
G.SE_Level = {}
G.SE_Target = {}
G.SE_Time = {}
G.SE_Trigger = {}

-- Free list for allocator
G.SE_I = 0
G.SE_F = 0
G.SE_V = {}

-- Hash key helper
local SE_BASE = 10000 + 32768 * 8 -- JASS_MAX_ARRAY_SIZE = 32768, Key = 8

local function SE_SaveUnique(handle, value)
    local id = tostring(GetHandleId(handle))
    local keyStr = tostring(SE_BASE - 1)
    if not G.Global_Hash[id] then G.Global_Hash[id] = {} end
    G.Global_Hash[id][keyStr] = value
end

local function SE_LoadUnique(handle)
    local id = tostring(GetHandleId(handle))
    local keyStr = tostring(SE_BASE - 1)
    if G.Global_Hash[id] then return G.Global_Hash[id][keyStr] or 0 end
    return 0
end

local function SE_FlushUnique(handle)
    local id = tostring(GetHandleId(handle))
    local keyStr = tostring(SE_BASE - 1)
    if G.Global_Hash[id] then G.Global_Hash[id][keyStr] = 0 end
end

function SE_allocate()
    local this = G.SE_F
    if this ~= 0 then
        G.SE_F = G.SE_V[this]
    else
        G.SE_I = G.SE_I + 1
        this = G.SE_I
    end
    if this > 8190 then
        return 0
    end
    G.SE_Time[this] = 0
    G.SE_V[this] = -1
    return this
end

function SE_deallocate(this)
    if this == nil or this == 0 then
        return
    elseif G.SE_V[this] ~= -1 then
        return
    end
    G.SE_V[this] = G.SE_F
    G.SE_F = this
end

local function SE_update(this, c)
    G.SE_Time[this] = 0
    G.SE_Level[this] = GetUnitAbilityLevel(c, G.SanctifiedEnchantment_SkillId)
    SetUnitAbilityLevel(G.SE_Target[this], G.SanctifiedEnchantment_SkillAbilityStatusId, G.SE_Level[this])
    SetUnitAbilityLevel(G.SE_Target[this], G.SanctifiedEnchantment_AbilitySplashId, G.SE_Level[this])
end

local function SE_destroy(this)
    DisableTrigger(G.SE_Trigger[this])
    SE_FlushUnique(G.SE_Trigger[this])
    DestroyTrigger(G.SE_Trigger[this])
    G.SE_Trigger[this] = nil
    SE_FlushUnique(G.SE_Target[this])
    UnitRemoveAbility(G.SE_Target[this], G.SanctifiedEnchantment_SkillBookId)
    UnitRemoveAbility(G.SE_Target[this], G.SanctifiedEnchantment_SkillBuffStatusId)
    G.SE_Target[this] = nil
    SE_deallocate(this)
end

local function SE_Function()
    local this = SE_LoadUnique(GetTriggeringTrigger())
    if GetTriggerEventId() == EVENT_GAME_TIMER_EXPIRED then
        G.SE_Time[this] = G.SE_Time[this] + G.SanctifiedEnchantment_Date
        if G.SE_Time[this] >= G.SanctifiedEnchantment_BuffDuration[G.SE_Level[this]] or GetUnitAbilityLevel(G.SE_Target[this], G.SanctifiedEnchantment_SkillBuffStatusId) == 0 then
            SE_destroy(this)
        end
    else
        SE_destroy(this)
    end
    return false
end

local function SE_create(c, t)
    local this = SE_allocate()
    G.SE_Level[this] = GetUnitAbilityLevel(c, G.SanctifiedEnchantment_SkillId)
    G.SE_Target[this] = t
    UnitAddAbility(G.SE_Target[this], G.SanctifiedEnchantment_SkillBookId)
    UnitMakeAbilityPermanent(G.SE_Target[this], true, G.SanctifiedEnchantment_SkillBookId)
    UnitMakeAbilityPermanent(G.SE_Target[this], true, G.SanctifiedEnchantment_SkillAbilityStatusId)
    UnitMakeAbilityPermanent(G.SE_Target[this], true, G.SanctifiedEnchantment_AbilitySplashId)
    SetUnitAbilityLevel(G.SE_Target[this], G.SanctifiedEnchantment_SkillAbilityStatusId, G.SE_Level[this])
    SetUnitAbilityLevel(G.SE_Target[this], G.SanctifiedEnchantment_AbilitySplashId, G.SE_Level[this])
    SE_SaveUnique(G.SE_Target[this], this)
    G.SE_Trigger[this] = CreateTrigger()
    SE_SaveUnique(G.SE_Trigger[this], this)
    TriggerAddCondition(G.SE_Trigger[this], Condition(SE_Function))
    TriggerRegisterDeathEvent(G.SE_Trigger[this], G.SE_Target[this])
    TriggerRegisterTimerEvent(G.SE_Trigger[this], G.SanctifiedEnchantment_Date, true)
    return this
end

local function SanctifiedEnchantment___SkillCondition_EFFECT()
    return GetSpellAbilityId() == G.SanctifiedEnchantment_SkillId
end

local function SanctifiedEnchantment___SkillAction_EFFECT()
    local se = SE_LoadUnique(GetSpellTargetUnit())
    if se > 0 then
        SE_update(se, GetTriggerUnit())
    else
        SE_create(GetTriggerUnit(), GetSpellTargetUnit())
    end
end

local function SanctifiedEnchantment___InitPreload()
    for index = 0, bj_MAX_PLAYER_SLOTS - 1 do
        SetPlayerAbilityAvailable(Player(index), G.SanctifiedEnchantment_SkillBookId, false)
    end
end

function SanctifiedEnchantment___Init()
    local trg = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(trg, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(trg, Condition(SanctifiedEnchantment___SkillCondition_EFFECT))
    TriggerAddAction(trg, SanctifiedEnchantment___SkillAction_EFFECT)
    SanctifiedEnchantment___InitPreload()
    G.SanctifiedEnchantment_BuffDuration[1] = 40
    G.SanctifiedEnchantment_BuffDuration[2] = 40
    G.SanctifiedEnchantment_BuffDuration[3] = 40
    G.SanctifiedEnchantment_BuffDuration[4] = 40
end

-- ============================================================
-- Portal System
-- ============================================================

-- Globals are already in globals.lua as G.udg_Portal_*

-- ============================================================
-- Portal_Connect
-- ============================================================

local function Portal_Connect_Func008C()
    return G.udg_Portal_active[G.udg_Portal_INDEX_CASTER] == true
        and GetSpellTargetUnit() ~= G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER]
        and G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] == false
end

local function Portal_Connect_Func008Func004C()
    return G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] == true
        and GetSpellTargetUnit() ~= G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER]
end

local function Portal_Connect_Func008Func004Func001C()
    return GetTriggerUnit() == G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET]
end

local function Portal_Connect_Func008Func004Func001Func002C()
    return G.udg_Portal_active[G.udg_Portal_INDEX_CASTER] == false
        and G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] == false
end

function Trig_Portal_Connect_Actions()
    if G.udg_Portal_SeverAbility == 0 then
        G.udg_Portal_SeverAbility = FourCC('A0TR')
    end
    if Portal_Connect_Func008C() then
        G.udg_Portal_INDEX_TRAVELLER = GetUnitUserData(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER])
        DestroyEffect(G.udg_Portal_FX[G.udg_Portal_INDEX_CASTER])
        DestroyEffect(G.udg_Portal_FX[G.udg_Portal_INDEX_TRAVELLER])
        UnitRemoveAbility(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER], G.udg_Portal_SeverAbility)
        UnitRemoveAbility(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER], G.udg_Portal_SeverAbility)
        G.udg_Portal_active[G.udg_Portal_INDEX_TRAVELLER] = false
        G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER] = nil
        G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER] = GetSpellTargetUnit()
        G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET] = GetTriggerUnit()
        G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] = true
        G.udg_Portal_FX[G.udg_Portal_INDEX_CASTER] = AddSpecialEffectTarget(G.udg_Portal_activeFX[G.udg_Portal_INDEX_CASTER], G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET], "origin")
        G.udg_Portal_FX[G.udg_Portal_INDEX_TARGET] = AddSpecialEffectTarget(G.udg_Portal_activeFX[G.udg_Portal_INDEX_TARGET], G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER], "origin")
        UnitAddAbility(G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET], G.udg_Portal_SeverAbility)
        UnitAddAbility(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER], G.udg_Portal_SeverAbility)
    elseif Portal_Connect_Func008Func004C() then
    elseif Portal_Connect_Func008Func004Func001C() then
    elseif Portal_Connect_Func008Func004Func001Func002C() then
        G.udg_Portal_active[G.udg_Portal_INDEX_CASTER] = true
        G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] = true
        G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER] = GetSpellTargetUnit()
        G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET] = GetTriggerUnit()
        G.udg_Portal_FX[G.udg_Portal_INDEX_CASTER] = AddSpecialEffectTarget(G.udg_Portal_activeFX[G.udg_Portal_INDEX_CASTER], GetTriggerUnit(), "origin")
        G.udg_Portal_FX[G.udg_Portal_INDEX_TARGET] = AddSpecialEffectTarget(G.udg_Portal_activeFX[G.udg_Portal_INDEX_TARGET], GetSpellTargetUnit(), "origin")
        UnitAddAbility(G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET], G.udg_Portal_SeverAbility)
        UnitAddAbility(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER], G.udg_Portal_SeverAbility)
    end
end

function InitTrig_Portal_Connect()
    gg_trg_Portal_Connect = CreateTrigger()
    TriggerAddAction(gg_trg_Portal_Connect, Trig_Portal_Connect_Actions)
end

-- ============================================================
-- Portal_Periodic
-- ============================================================

local function Portal_Periodic_Func001Func006C()
    return DistanceBetweenPoints(G.udg_Portal_loc1, G.udg_Portal_loc3) <= G.udg_Portal_range[G.udg_Portal_INDEX_TARGET]
end

local function Portal_Periodic_Func001Func006Func002C()
    return G.udg_Portal_delay[G.udg_Portal_INDEX_CASTER] > 0
end

local function Portal_Periodic_Func001Func006Func002Func002C()
    return G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_CASTER] == false
end

local function Portal_Periodic_Func001Func006Func002Func011C()
    return G.udg_Portal_missileUseOwnMovement[G.udg_Portal_INDEX_TARGET] == true
end

local function Portal_Periodic_Func001Func006Func002Func011Func003C()
    return IsUnitSelected(G.udg_Portal_traveller, GetOwningPlayer(G.udg_Portal_traveller)) == true
end

local function Portal_Periodic_Func001Func006Func002Func011Func004C()
    return G.udg_Portal_missileTargetable[G.udg_Portal_INDEX_TARGET] == true
end

local function Portal_Periodic_Func001Func006Func002Func011Func012C()
    return G.udg_Portal_missileSpeed[G.udg_Portal_INDEX_TARGET] > 0
end

local function Portal_Periodic_Func001Func006Func002Func011Func012Func004C()
    return IsUnitSelected(G.udg_Portal_traveller, GetOwningPlayer(G.udg_Portal_traveller)) == true
end

local function Portal_Periodic_Func001Func006Func002Func011Func012Func005C()
    return G.udg_Portal_missileTargetable[G.udg_Portal_INDEX_TARGET] == true
end

local function Portal_Periodic_Func001Func006Func001C()
    return G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_CASTER] == true
end

function Trig_Portal_Periodic_Func001A()
    G.udg_Portal_traveller = GetEnumUnit()
    G.udg_Portal_INDEX_CASTER = GetUnitUserData(G.udg_Portal_traveller)
    G.udg_Portal_INDEX_TARGET = GetUnitUserData(G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER])
    G.udg_Portal_loc1 = GetUnitLoc(G.udg_Portal_traveller)
    G.udg_Portal_loc3 = GetUnitLoc(G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER])
    if Portal_Periodic_Func001Func006C() then
        if Portal_Periodic_Func001Func006Func002C() then
            if Portal_Periodic_Func001Func006Func002Func002C() then
                G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_CASTER] = true
                G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_CASTER] = G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_TARGET]
                UnitAddAbility(G.udg_Portal_traveller, G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_CASTER])
            end
            G.udg_Portal_delay[G.udg_Portal_INDEX_CASTER] = G.udg_Portal_delay[G.udg_Portal_INDEX_CASTER] - (1.0 / 32.0)
        else
            G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_CASTER] = false
            G.udg_Portal_loc2 = GetUnitLoc(G.udg_Portal_traveller)
            DestroyEffect(AddSpecialEffectLoc(G.udg_Portal_departureFX[G.udg_Portal_INDEX_TARGET], G.udg_Portal_loc2))
            UnitRemoveAbility(G.udg_Portal_traveller, G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_CASTER])
            RemoveLocation(G.udg_Portal_loc2)
            G.udg_Portal_loc2 = GetUnitLoc(G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET])
            if Portal_Periodic_Func001Func006Func002Func011C() then
                G.udg_Portal_dummy = CreateUnit(GetOwningPlayer(G.udg_Portal_traveller), G.udg_Portal_missileDummy[G.udg_Portal_INDEX_TARGET], GetLocationX(G.udg_Portal_loc1), GetLocationY(G.udg_Portal_loc1), AngleBetweenPoints(G.udg_Portal_loc1, G.udg_Portal_loc2))
                if Portal_Periodic_Func001Func006Func002Func011Func003C() then
                    SelectUnitAddForPlayer(G.udg_Portal_dummy, GetOwningPlayer(G.udg_Portal_traveller))
                end
                if Portal_Periodic_Func001Func006Func002Func011Func004C() then
                    SetUnitInvulnerable(G.udg_Portal_dummy, false)
                end
                IssuePointOrderLoc(G.udg_Portal_dummy, "move", G.udg_Portal_loc2)
                G.udg_Portal_INDEX_TRAVELLER = GetUnitUserData(G.udg_Portal_dummy)
                G.udg_Portal_missileSpeed[G.udg_Portal_INDEX_TRAVELLER] = 0
                G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER] = G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET]
                G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER] = G.udg_Portal_traveller
                GroupAddUnit(G.udg_Portal_teleMissiles, G.udg_Portal_dummy)
                ShowUnit(G.udg_Portal_traveller, false)
            else
                if Portal_Periodic_Func001Func006Func002Func011Func012C() then
                    G.udg_Portal_dummy = CreateUnit(GetOwningPlayer(G.udg_Portal_traveller), G.udg_Portal_missileDummy[G.udg_Portal_INDEX_TARGET], GetLocationX(G.udg_Portal_loc1), GetLocationY(G.udg_Portal_loc1), AngleBetweenPoints(G.udg_Portal_loc1, G.udg_Portal_loc2))
                    if Portal_Periodic_Func001Func006Func002Func011Func012Func004C() then
                        SelectUnitAddForPlayer(G.udg_Portal_dummy, GetOwningPlayer(G.udg_Portal_traveller))
                    end
                    if Portal_Periodic_Func001Func006Func002Func011Func012Func005C() then
                        SetUnitInvulnerable(G.udg_Portal_dummy, false)
                    end
                    UnitAddAbility(G.udg_Portal_dummy, G.udg_Portal_missileFXAbil[G.udg_Portal_INDEX_TARGET])
                    SetUnitFlyHeight(G.udg_Portal_dummy, G.udg_Portal_missileHeight[G.udg_Portal_INDEX_TARGET], 0)
                    G.udg_Portal_INDEX_TRAVELLER = GetUnitUserData(G.udg_Portal_dummy)
                    G.udg_Portal_missileSpeed[G.udg_Portal_INDEX_TRAVELLER] = G.udg_Portal_missileSpeed[G.udg_Portal_INDEX_TARGET]
                    G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER] = G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET]
                    G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER] = G.udg_Portal_traveller
                    SetUnitPathing(G.udg_Portal_dummy, false)
                    GroupAddUnit(G.udg_Portal_teleMissiles, G.udg_Portal_dummy)
                    ShowUnit(G.udg_Portal_traveller, false)
                else
                    RemoveLocation(G.udg_Portal_loc3)
                    G.udg_Portal_INDEX_TRAVELLER = GetUnitUserData(G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET])
                    G.udg_Portal_loc3 = PolarProjectionBJ(G.udg_Portal_loc2, GetRandomReal(0, G.udg_Portal_range[G.udg_Portal_INDEX_TRAVELLER]), GetRandomDirectionDeg())
                    SetUnitPositionLoc(G.udg_Portal_traveller, G.udg_Portal_loc3)
                    G.udg_Portal_loc4 = GetUnitRallyPoint(G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER])
                    IssuePointOrderLoc(G.udg_Portal_traveller, "attack", G.udg_Portal_loc4)
                    RemoveLocation(G.udg_Portal_loc4)
                    DestroyEffect(AddSpecialEffectLoc(G.udg_Portal_arrivalFX[G.udg_Portal_INDEX_TRAVELLER], G.udg_Portal_loc3))
                end
            end
            RemoveLocation(G.udg_Portal_loc2)
            G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER] = nil
            GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_traveller)
        end
    else
        if Portal_Periodic_Func001Func006Func001C() then
            G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_CASTER] = false
            IssueTargetOrder(G.udg_Portal_traveller, "smart", G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER])
        end
    end
    RemoveLocation(G.udg_Portal_loc3)
    RemoveLocation(G.udg_Portal_loc1)
end

-- Missile movement (Func002A)
local function Portal_Periodic_Func002Func007C()
    return IsUnitAliveBJ(G.udg_Portal_traveller) == true
end

local function Portal_Periodic_Func002Func007Func003C()
    return G.udg_Portal_missileSpeed[G.udg_Portal_INDEX_TRAVELLER] > 0
end

local function Portal_Periodic_Func002Func007Func003Func002C()
    return DistanceBetweenPoints(G.udg_Portal_loc1, G.udg_Portal_loc2) <= (G.udg_Portal_missileSpeed[G.udg_Portal_INDEX_TRAVELLER] / 33.0)
end

local function Portal_Periodic_Func002Func007Func003Func002Func013C()
    return IsUnitSelected(G.udg_Portal_traveller, GetOwningPlayer(G.udg_Portal_traveller)) == true
end

local function Portal_Periodic_Func002Func007Func003Func002Func014C()
    return IsUnitAliveBJ(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER]) == true
end

local function Portal_Periodic_Func002Func007Func003Func001C()
    return DistanceBetweenPoints(G.udg_Portal_loc1, G.udg_Portal_loc2) <= G.udg_Portal_range[G.udg_Portal_INDEX_TARGET]
end

local function Portal_Periodic_Func002Func007Func003Func001Func001C()
    return IsUnitAliveBJ(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER]) == true
end

local function Portal_Periodic_Func002Func007Func003Func001Func012C()
    return IsUnitSelected(G.udg_Portal_traveller, GetOwningPlayer(G.udg_Portal_traveller)) == true
end

local function Portal_Periodic_Func002Func007Func015C()
    return IsUnitSelected(G.udg_Portal_traveller, GetOwningPlayer(G.udg_Portal_traveller)) == true
end

function Trig_Portal_Periodic_Func002A()
    G.udg_Portal_traveller = GetEnumUnit()
    G.udg_Portal_INDEX_TRAVELLER = GetUnitUserData(G.udg_Portal_traveller)
    G.udg_Portal_INDEX_CASTER = GetUnitUserData(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER])
    G.udg_Portal_INDEX_TARGET = GetUnitUserData(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER])
    if Portal_Periodic_Func002Func007C() then
        G.udg_Portal_loc1 = GetUnitLoc(G.udg_Portal_traveller)
        G.udg_Portal_loc2 = GetUnitLoc(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER])
        if Portal_Periodic_Func002Func007Func003C() then
            if Portal_Periodic_Func002Func007Func003Func002C() then
                ShowUnit(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], true)
                G.udg_Portal_loc3 = PolarProjectionBJ(G.udg_Portal_loc1, GetRandomReal(0, G.udg_Portal_range[GetUnitUserData(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER])]), GetRandomDirectionDeg())
                SetUnitPositionLoc(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], G.udg_Portal_loc3)
                UnitApplyTimedLife(G.udg_Portal_traveller, FourCC('BTLF'), 0.01)
                GroupRemoveUnit(G.udg_Portal_teleMissiles, G.udg_Portal_traveller)
                GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER])
                DestroyEffect(AddSpecialEffectLoc(G.udg_Portal_arrivalFX[GetUnitUserData(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER])], G.udg_Portal_loc3))
                G.udg_Portal_loc4 = GetUnitRallyPoint(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER])
                IssuePointOrderLoc(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], "attack", G.udg_Portal_loc4)
                RemoveLocation(G.udg_Portal_loc4)
                RemoveLocation(G.udg_Portal_loc3)
                if Portal_Periodic_Func002Func007Func003Func002Func013C() then
                    SelectUnitAddForPlayer(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], GetOwningPlayer(G.udg_Portal_traveller))
                end
            else
                if Portal_Periodic_Func002Func007Func003Func002Func014C() then
                    G.udg_Portal_loc3 = PolarProjectionBJ(G.udg_Portal_loc1, (G.udg_Portal_missileSpeed[G.udg_Portal_INDEX_TRAVELLER] / 33.0), AngleBetweenPoints(G.udg_Portal_loc1, G.udg_Portal_loc2))
                    SetUnitPositionLocFacingLocBJ(G.udg_Portal_traveller, G.udg_Portal_loc3, G.udg_Portal_loc2)
                    RemoveLocation(G.udg_Portal_loc3)
                else
                    UnitApplyTimedLife(G.udg_Portal_traveller, FourCC('BTLF'), 0.01)
                end
            end
        else
            if Portal_Periodic_Func002Func007Func003Func001C() then
                ShowUnit(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], true)
                SetUnitPositionLoc(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], G.udg_Portal_loc1)
                UnitApplyTimedLife(G.udg_Portal_traveller, FourCC('BTLF'), 0.01)
                GroupRemoveUnit(G.udg_Portal_teleMissiles, G.udg_Portal_traveller)
                GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER])
                DestroyEffect(AddSpecialEffectLoc(G.udg_Portal_arrivalFX[G.udg_Portal_INDEX_TARGET], G.udg_Portal_loc1))
                G.udg_Portal_loc4 = GetUnitRallyPoint(G.udg_Portal_portal[G.udg_Portal_INDEX_TRAVELLER])
                IssuePointOrderLoc(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], "attack", G.udg_Portal_loc4)
                RemoveLocation(G.udg_Portal_loc4)
                if Portal_Periodic_Func002Func007Func003Func001Func012C() then
                    SelectUnitAddForPlayer(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], GetOwningPlayer(G.udg_Portal_traveller))
                end
            else
                if Portal_Periodic_Func002Func007Func003Func001Func001C() then
                else
                    UnitApplyTimedLife(G.udg_Portal_traveller, FourCC('BTLF'), 0.01)
                end
            end
        end
        RemoveLocation(G.udg_Portal_loc2)
        RemoveLocation(G.udg_Portal_loc1)
    else
        ShowUnit(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], true)
        G.udg_Portal_loc1 = GetUnitLoc(G.udg_Portal_traveller)
        SetUnitPositionLoc(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], G.udg_Portal_loc1)
        RemoveLocation(G.udg_Portal_loc1)
        SetUnitFlyHeight(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], GetUnitFlyHeight(G.udg_Portal_traveller), 0)
        ExplodeUnitBJ(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER])
        GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER])
        GroupRemoveUnit(G.udg_Portal_teleMissiles, G.udg_Portal_traveller)
        UnitRemoveAbility(G.udg_Portal_traveller, G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_TRAVELLER])
        if Portal_Periodic_Func002Func007Func015C() then
            SelectUnitAddForPlayer(G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER], GetOwningPlayer(G.udg_Portal_traveller))
        end
    end
end

local function Portal_Periodic_Func003C()
    return IsUnitGroupEmptyBJ(G.udg_Portal_group) == true and IsUnitGroupEmptyBJ(G.udg_Portal_teleMissiles) == true
end

function Trig_Portal_Periodic_Actions()
    ForGroup(G.udg_Portal_group, Trig_Portal_Periodic_Func001A)
    ForGroup(G.udg_Portal_teleMissiles, Trig_Portal_Periodic_Func002A)
    if Portal_Periodic_Func003C() then
        DisableTrigger(GetTriggeringTrigger())
    end
end

function InitTrig_Portal_Periodic()
    gg_trg_Portal_Periodic = CreateTrigger()
    DisableTrigger(gg_trg_Portal_Periodic)
    TriggerRegisterTimerEvent(gg_trg_Portal_Periodic, 1.0 / 32.0, true)
    TriggerAddAction(gg_trg_Portal_Periodic, Trig_Portal_Periodic_Actions)
end

-- ============================================================
-- Portal_Target
-- ============================================================

local function Portal_Target_Func006C()
    return GetIssuedOrderId() == OrderId("smart") or GetIssuedOrderId() == OrderId("move")
end

function Trig_Portal_Target_Conditions()
    return G.udg_Portal_active[GetUnitUserData(GetOrderTargetUnit())] == true
        and IsUnitInGroup(GetTriggerUnit(), G.udg_Portal_teleMissiles) == false
        and Portal_Target_Func006C()
        and IsUnitAlly(GetTriggerUnit(), GetOwningPlayer(GetOrderTargetUnit())) == true
        and IsUnitType(GetTriggerUnit(), UNIT_TYPE_STRUCTURE) == false
end

local function Portal_Target_Func003C()
    return G.udg_Portal_active[G.udg_Portal_INDEX_CASTER] == true
end

local function Portal_Target_Func003Func001C()
    return G.udg_Portal_preventAllies[G.udg_Portal_INDEX_TARGET] == true
        and GetOwningPlayer(GetTriggerUnit()) ~= GetOwningPlayer(GetOrderTargetUnit())
end

local function Portal_Target_Func003Func001Func005C()
    return IsTriggerEnabled(gg_trg_Portal_Periodic) == false
end

function Trig_Portal_Target_Actions()
    G.udg_Portal_INDEX_CASTER = GetUnitUserData(GetTriggerUnit())
    G.udg_Portal_INDEX_TARGET = GetUnitUserData(GetOrderTargetUnit())
    if Portal_Target_Func003C() then
        DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.0, "TRIGSTR_19362")
    else
        if Portal_Target_Func003Func001C() then
        else
            G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER] = GetOrderTargetUnit()
            GroupAddUnit(G.udg_Portal_group, GetTriggerUnit())
            G.udg_Portal_delay[G.udg_Portal_INDEX_CASTER] = G.udg_Portal_delay[G.udg_Portal_INDEX_TARGET]
            if Portal_Target_Func003Func001Func005C() then
                EnableTrigger(gg_trg_Portal_Periodic)
            end
        end
    end
end

function InitTrig_Portal_Target()
    gg_trg_Portal_Target = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Target, EVENT_PLAYER_UNIT_ISSUED_TARGET_ORDER)
    TriggerAddCondition(gg_trg_Portal_Target, Condition(Trig_Portal_Target_Conditions))
    TriggerAddAction(gg_trg_Portal_Target, Trig_Portal_Target_Actions)
end

-- ============================================================
-- Portal_Disengage
-- ============================================================

function Trig_Portal_Disengage_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), G.udg_Portal_group) == true
        and GetOrderTargetUnit() ~= G.udg_Portal_targeted[GetUnitUserData(GetTriggerUnit())]
end

function Trig_Portal_Disengage_Actions()
    G.udg_Portal_INDEX_CASTER = GetUnitUserData(GetTriggerUnit())
    G.udg_Portal_INDEX_TARGET = GetUnitUserData(G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER])
    G.udg_Portal_delay[G.udg_Portal_INDEX_CASTER] = 0
    G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_CASTER] = false
    G.udg_Portal_targeted[G.udg_Portal_INDEX_CASTER] = nil
    GroupRemoveUnit(G.udg_Portal_group, GetTriggerUnit())
    UnitRemoveAbility(GetTriggerUnit(), G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_TARGET])
end

function InitTrig_Portal_Disengage()
    gg_trg_Portal_Disengage = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_ISSUED_TARGET_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_ISSUED_POINT_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_ISSUED_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disengage, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Portal_Disengage, Condition(Trig_Portal_Disengage_Conditions))
    TriggerAddAction(gg_trg_Portal_Disengage, Trig_Portal_Disengage_Actions)
end

-- ============================================================
-- Portal_Death
-- ============================================================

function Trig_Portal_Death_Conditions()
    return G.udg_Portal_active[GetUnitUserData(GetTriggerUnit())] == true
end

local function Portal_Death_Func004Func004C()
    return GetTriggerUnit() == G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER]
end

local function Portal_Death_Func004Func005C()
    return G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER] == G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER]
end

function Trig_Portal_Death_Func004A()
    G.udg_Portal_traveller = GetEnumUnit()
    G.udg_Portal_INDEX_TRAVELLER = GetUnitUserData(G.udg_Portal_traveller)
    UnitRemoveAbility(G.udg_Portal_traveller, G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_CASTER])
    if Portal_Death_Func004Func004C() then
        G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER] = nil
        G.udg_Portal_delay[G.udg_Portal_INDEX_TRAVELLER] = 0
        G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_TRAVELLER] = false
        GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_traveller)
    end
    if Portal_Death_Func004Func005C() then
        G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER] = nil
        G.udg_Portal_delay[G.udg_Portal_INDEX_TRAVELLER] = 0
        G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_TRAVELLER] = false
        GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_traveller)
    end
end

function Trig_Portal_Death_Actions()
    G.udg_Portal_INDEX_CASTER = GetUnitUserData(GetTriggerUnit())
    G.udg_Portal_INDEX_TARGET = GetUnitUserData(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER])
    ForGroup(G.udg_Portal_group, Trig_Portal_Death_Func004A)
    G.udg_Portal_active[G.udg_Portal_INDEX_CASTER] = false
    G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] = false
    DestroyEffect(G.udg_Portal_FX[G.udg_Portal_INDEX_CASTER])
    DestroyEffect(G.udg_Portal_FX[G.udg_Portal_INDEX_TARGET])
    G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER] = nil
    G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET] = nil
end

function InitTrig_Portal_Death()
    gg_trg_Portal_Death = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Death, EVENT_PLAYER_UNIT_DEATH)
    TriggerAddCondition(gg_trg_Portal_Death, Condition(Trig_Portal_Death_Conditions))
    TriggerAddAction(gg_trg_Portal_Death, Trig_Portal_Death_Actions)
end

-- ============================================================
-- Portal_Missile_Order
-- ============================================================

function Trig_Portal_Missile_Order_Conditions()
    return IsUnitInGroup(GetTriggerUnit(), G.udg_Portal_teleMissiles) == true
end

function Trig_Portal_Missile_Order_Actions()
    DisableTrigger(GetTriggeringTrigger())
    G.udg_Portal_INDEX_CASTER = GetUnitUserData(GetTriggerUnit())
    G.udg_Portal_loc1 = GetUnitLoc(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER])
    IssuePointOrderLoc(GetTriggerUnit(), "move", G.udg_Portal_loc1)
    RemoveLocation(G.udg_Portal_loc1)
    EnableTrigger(GetTriggeringTrigger())
end

function InitTrig_Portal_Missile_Order()
    gg_trg_Portal_Missile_Order = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Missile_Order, EVENT_PLAYER_UNIT_ISSUED_TARGET_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Missile_Order, EVENT_PLAYER_UNIT_ISSUED_POINT_ORDER)
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Missile_Order, EVENT_PLAYER_UNIT_ISSUED_ORDER)
    TriggerAddCondition(gg_trg_Portal_Missile_Order, Condition(Trig_Portal_Missile_Order_Conditions))
    TriggerAddAction(gg_trg_Portal_Missile_Order, Trig_Portal_Missile_Order_Actions)
end

-- ============================================================
-- Portal_Disconnect
-- ============================================================

function Trig_Portal_Disconnect_Conditions()
    return G.udg_Portal_active[GetUnitUserData(GetTriggerUnit())] == true
end

local function Portal_Disconnect_Func001C()
    return GetSpellAbilityId() == G.udg_Portal_SeverAbility
end

local function Portal_Disconnect_Func001Func005Func004C()
    return GetTriggerUnit() == G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER]
end

local function Portal_Disconnect_Func001Func005Func005C()
    return G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER] == G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER]
end

function Trig_Portal_Disconnect_Func001Func005A()
    G.udg_Portal_traveller = GetEnumUnit()
    G.udg_Portal_INDEX_TRAVELLER = GetUnitUserData(G.udg_Portal_traveller)
    UnitRemoveAbility(G.udg_Portal_traveller, G.udg_Portal_delayFXAbil[G.udg_Portal_INDEX_CASTER])
    if Portal_Disconnect_Func001Func005Func004C() then
        G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER] = nil
        G.udg_Portal_delay[G.udg_Portal_INDEX_TRAVELLER] = 0
        G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_TRAVELLER] = false
        GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_traveller)
    end
    if Portal_Disconnect_Func001Func005Func005C() then
        G.udg_Portal_targeted[G.udg_Portal_INDEX_TRAVELLER] = nil
        G.udg_Portal_delay[G.udg_Portal_INDEX_TRAVELLER] = 0
        G.udg_Portal_isTeleporting[G.udg_Portal_INDEX_TRAVELLER] = false
        GroupRemoveUnit(G.udg_Portal_group, G.udg_Portal_traveller)
    end
end

function Trig_Portal_Disconnect_Actions()
    if Portal_Disconnect_Func001C() then
        G.udg_Portal_INDEX_CASTER = GetUnitUserData(GetTriggerUnit())
        G.udg_Portal_INDEX_TARGET = GetUnitUserData(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER])
        UnitRemoveAbility(GetTriggerUnit(), G.udg_Portal_SeverAbility)
        UnitRemoveAbility(G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER], G.udg_Portal_SeverAbility)
        ForGroup(G.udg_Portal_group, Trig_Portal_Disconnect_Func001Func005A)
        G.udg_Portal_active[G.udg_Portal_INDEX_CASTER] = false
        G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] = false
        DestroyEffect(G.udg_Portal_FX[G.udg_Portal_INDEX_CASTER])
        DestroyEffect(G.udg_Portal_FX[G.udg_Portal_INDEX_TARGET])
        G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER] = nil
        G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET] = nil
    end
end

function InitTrig_Portal_Disconnect()
    gg_trg_Portal_Disconnect = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Portal_Disconnect, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_Portal_Disconnect, Condition(Trig_Portal_Disconnect_Conditions))
    TriggerAddAction(gg_trg_Portal_Disconnect, Trig_Portal_Disconnect_Actions)
end

-- ============================================================
-- Connect_Portal_2
-- ============================================================

function Trig_Connect_Portal_2_Conditions()
    return GetSpellAbilityId() == FourCC('A0TQ')
end

local function Connect_Portal_2_Func001C()
    return GetUnitTypeId(GetSpellTargetUnit()) == GetUnitTypeId(GetTriggerUnit())
end

local function Connect_Portal_2_Func001Func003C()
    return G.udg_Portal_active[G.udg_Portal_INDEX_TARGET] == true
        and GetSpellTargetUnit() ~= G.udg_Portal_portal[G.udg_Portal_INDEX_CASTER]
end

local function Connect_Portal_2_Func001Func003Func002C()
    return GetTriggerUnit() == G.udg_Portal_portal[G.udg_Portal_INDEX_TARGET]
end

function Trig_Connect_Portal_2_Actions()
    if Connect_Portal_2_Func001C() then
        G.udg_Portal_INDEX_CASTER = GetUnitUserData(GetTriggerUnit())
        G.udg_Portal_INDEX_TARGET = GetUnitUserData(GetSpellTargetUnit())
        if Connect_Portal_2_Func001Func003C() then
            DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.0, "TRIGSTR_19222")
        else
            if Connect_Portal_2_Func001Func003Func002C() then
                DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.0, "TRIGSTR_19228")
            else
                G.udg_Portal_ConfigIndex[1] = G.udg_Portal_INDEX_CASTER
                G.udg_Portal_ConfigIndex[2] = G.udg_Portal_INDEX_TARGET
                for loopA = 1, 2 do
                    G.udg_Portal_departureFX[G.udg_Portal_ConfigIndex[loopA]] = "Abilities\\Spells\\Human\\MassTeleport\\MassTeleportCaster.mdl"
                    G.udg_Portal_arrivalFX[G.udg_Portal_ConfigIndex[loopA]] = "Abilities\\Spells\\Human\\MassTeleport\\MassTeleportTarget.mdl"
                    G.udg_Portal_activeFX[G.udg_Portal_ConfigIndex[loopA]] = "Abilities\\Spells\\Orc\\Voodoo\\VoodooAura.mdl"
                    G.udg_Portal_range[G.udg_Portal_ConfigIndex[loopA]] = 180.0
                    G.udg_Portal_delay[G.udg_Portal_ConfigIndex[loopA]] = 0.0
                    G.udg_Portal_missileSpeed[G.udg_Portal_ConfigIndex[loopA]] = 0.0
                    G.udg_Portal_preventAllies[G.udg_Portal_ConfigIndex[loopA]] = false
                    G.udg_Portal_missileHeight[G.udg_Portal_ConfigIndex[loopA]] = 0.0
                    G.udg_Portal_missileTargetable[G.udg_Portal_ConfigIndex[loopA]] = false
                    G.udg_Portal_missileUseOwnMovement[G.udg_Portal_ConfigIndex[loopA]] = false
                end
                G.udg_Portal_INDEX_CASTER = G.udg_Portal_ConfigIndex[1]
                G.udg_Portal_INDEX_TARGET = G.udg_Portal_ConfigIndex[2]
                TriggerExecute(gg_trg_Portal_Connect)
            end
        end
    else
        DisplayTimedTextToForce(GetForceOfPlayer(GetOwningPlayer(GetTriggerUnit())), 10.0, "TRIGSTR_19244")
    end
end

function InitTrig_Connect_Portal_2()
    gg_trg_Connect_Portal_2 = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Connect_Portal_2, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddCondition(gg_trg_Connect_Portal_2, Condition(Trig_Connect_Portal_2_Conditions))
    TriggerAddAction(gg_trg_Connect_Portal_2, Trig_Connect_Portal_2_Actions)
end

-- ============================================================
-- PortalSell
-- ============================================================

function Trig_PortalSell_Conditions()
    return GetUnitTypeId(GetSoldUnit()) == FourCC('h0P0')
end

function Trig_PortalSell_Actions()
    IssueImmediateOrder(GetTriggerUnit(), "web")
    RemoveUnit(GetSoldUnit())
end

function InitTrig_PortalSell()
    gg_trg_PortalSell = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_PortalSell, EVENT_PLAYER_UNIT_SELL)
    TriggerAddCondition(gg_trg_PortalSell, Condition(Trig_PortalSell_Conditions))
    TriggerAddAction(gg_trg_PortalSell, Trig_PortalSell_Actions)
end

-- ============================================================
-- PortalFix
-- ============================================================

function Trig_PortalFix_Actions()
    WaygateSetDestinationLoc(gg_unit_n003_0020, GetRectCenter(gg_rct_UldamanOut))
    WaygateSetDestinationLoc(gg_unit_n003_0588, GetRectCenter(gg_rct_DalaranOut))
    WaygateSetDestinationLoc(gg_unit_n003_0126, GetRectCenter(gg_rct_NaxOut))
end

function InitTrig_PortalFix()
    gg_trg_PortalFix = CreateTrigger()
    TriggerAddAction(gg_trg_PortalFix, Trig_PortalFix_Actions)
end

-- ============================================================
-- RemPortalsFromAnotherSide
-- ============================================================

function Trig_RemPortalsFromAnotherSide_Actions()
    GroupRemoveUnit(G.udg_TempGroup, gg_unit_n003_0124)
    GroupRemoveUnit(G.udg_TempGroup, gg_unit_n003_0123)
    GroupRemoveUnit(G.udg_TempGroup, gg_unit_n003_0118)
    GroupRemoveUnit(G.udg_TempGroup, gg_unit_n003_0117)
end

function InitTrig_RemPortalsFromAnotherSide()
    gg_trg_RemPortalsFromAnotherSide = CreateTrigger()
    TriggerAddAction(gg_trg_RemPortalsFromAnotherSide, Trig_RemPortalsFromAnotherSide_Actions)
end

-- ============================================================
-- PortalCommonFunction
-- ============================================================

-- Shared globals used by TeleportUnits and TeleportUnitsED
G.gLoc = nil
G.gRect = nil

-- EnterGreen is defined in the original JASS (line 10020). It calls WakeGreenUp().
-- These must be available in the global scope when this file is loaded.
-- If not already converted, add them here or in a separate file.

function PortalConditions()
    return not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE)
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Sch5')) == 0
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A001')) == 0
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1M3')) == 0
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Awrp')) == 0
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A00A')) == 0
end

function TeleportUnitsEach()
    SetUnitPosition(GetEnumUnit(), GetRandomReal(GetRectMinX(G.gRect), GetRectMaxX(G.gRect)), GetRandomReal(GetRectMinY(G.gRect), GetRectMaxY(G.gRect)))
    RemoveLocation(G.gLoc)
    EnterGreen(GetEnumUnit())
end

function TeleportUnits(Portal, Rect2, radious)
    G.gLoc = GetUnitLoc(Portal)
    G.gRect = Rect2
    GroupEnumUnitsInRangeOfLocCounted(G.gGroup, G.gLoc, radious, Condition(PortalConditions), 150)
    ForGroup(G.gGroup, TeleportUnitsEach)
    GroupClear(G.gGroup)
    RemoveLocation(G.gLoc)
end

-- Extra Dimension variant
function PortalConditionsED()
    return not IsUnitType(GetFilterUnit(), UNIT_TYPE_STRUCTURE)
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Sch5')) == 0
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A001')) == 0
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1M3')) == 0
        and GetUnitTypeId(GetFilterUnit()) ~= FourCC('n01W')
        and GetUnitTypeId(GetFilterUnit()) ~= FourCC('n01X')
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('Awrp')) == 0
        and GetUnitAbilityLevel(GetFilterUnit(), FourCC('A1LR')) >= 1
end

function TeleportUnitsED(Portal, Rect2, radious)
    G.gLoc = GetUnitLoc(Portal)
    G.gRect = Rect2
    GroupEnumUnitsInRangeOfLocCounted(G.gGroup, G.gLoc, radious, Condition(PortalConditionsED), 150)
    ForGroup(G.gGroup, TeleportUnitsEach)
    GroupClear(G.gGroup)
    RemoveLocation(G.gLoc)
end

-- ============================================================
-- Init function for spells that need runtime setup
-- ============================================================

function SpellsCommon_Init()
    SpellSleepAOE___onInit()
    SanctifiedEnchantment___Init()
end
