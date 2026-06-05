-- ===========================================================================
-- spells_races_1.lua — Race-specific spell triggers (vJASS → Lua)
-- ===========================================================================

-- ============================== ORDA (HORDE) ==============================

-- IronStar — кастует A103 → юнит получает таймер жизни 10 сек
G.Trig_IronStar = G.Trig_IronStar or CreateTrigger()
G.Trig_IronStar:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_IronStar:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A103")
end))
G.Trig_IronStar:AddAction(function()
    UnitApplyTimedLife(GetTriggerUnit(), FourCC("BTLF"), 10.0)
end)
G.Trig_IronStar:SetEnabled(false)

-- AutoShield2 — A124 → antimagicshell на цель
G.Trig_AutoShield2 = G.Trig_AutoShield2 or CreateTrigger()
G.Trig_AutoShield2:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_AutoShield2:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A124")
end))
G.Trig_AutoShield2:AddAction(function()
    IssueTargetOrder(GetTriggerUnit(), "antimagicshell", GetSpellTargetUnit())
end)
G.Trig_AutoShield2:SetEnabled(false)

-- PandaSecondAttack — при атаке если есть A129 и нет A12A → добавить, иначе убрать
G.Trig_PandaSecondAttack = G.Trig_PandaSecondAttack or CreateTrigger()
G.Trig_PandaSecondAttack:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_PandaSecondAttack:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetAttacker(), FourCC("A129")) > 0
end))
G.Trig_PandaSecondAttack:AddAction(function()
    local attacker = GetAttacker()
    if GetUnitAbilityLevel(attacker, FourCC("A12A")) == 0 then
        UnitAddAbility(attacker, FourCC("A12A"))
    else
        UnitRemoveAbility(attacker, FourCC("A12A"))
    end
end)
G.Trig_PandaSecondAttack:SetEnabled(false)

-- DragonFire — при атаке, если есть A0ZX, 8% шанс breathoffire
G.Trig_DragonFire = G.Trig_DragonFire or CreateTrigger()
G.Trig_DragonFire:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_DragonFire:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetAttacker(), FourCC("A0ZX")) > 0
        and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker()))
        and math.random(1, 100) <= 8
end))
G.Trig_DragonFire:AddAction(function()
    IssueTargetOrder(GetAttacker(), "breathoffire", GetTriggerUnit())
end)

-- AutoShield — A016 → antimagicshell на цель
G.Trig_AutoShield = G.Trig_AutoShield or CreateTrigger()
G.Trig_AutoShield:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_AutoShield:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A016")
end))
G.Trig_AutoShield:AddAction(function()
    IssueTargetOrder(GetTriggerUnit(), "antimagicshell", GetSpellTargetUnit())
end)
G.Trig_AutoShield:SetEnabled(false)

-- GarraoshMassBloodlast ("MassBloodlust") — A12M → bloodlust на всех своих в радиусе 500
G.Trig_GarraoshMassBloodlast = G.Trig_GarraoshMassBloodlast or CreateTrigger()
G.Trig_GarraoshMassBloodlast:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_GarraoshMassBloodlast:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A12M")
end))
G.Trig_GarraoshMassBloodlast:AddAction(function()
    local caster = GetTriggerUnit()
    local owner = GetOwningPlayer(caster)
    local cloc = GetUnitLoc(caster)
    G.udg_LocalOtrad2 = G.udg_LocalOtrad2 or CreateGroup()
    GroupEnumUnitsInRangeOfLoc(G.udg_LocalOtrad2, cloc, 500,
        Condition(function() return GetOwningPlayer(GetFilterUnit()) == owner end))
    RemoveLocation(cloc)
    cloc = GetUnitLoc(caster)
    ForGroup(G.udg_LocalOtrad2, function()
        local dumb = CreateUnit(owner, FourCC("H0BN"), GetLocationX(cloc), GetLocationY(cloc), bj_UNIT_FACING)
        G.udg_LocalUnit2 = dumb
        TriggerExecute(G.gg_trg_ToKill2)
        UnitAddAbility(dumb, FourCC("A12L"))
        SetUnitManaBJ(dumb, 1111111.0)
        SetUnitAbilityLevel(dumb, FourCC("A12L"), GetUnitAbilityLevel(caster, FourCC("A12M")))
        IssueTargetOrder(dumb, "bloodlust", GetEnumUnit())
    end)
    RemoveLocation(cloc)
    GroupClear(G.udg_LocalOtrad2)
end)

-- ============================== BANDITS ==============================

-- MoveTimed / MoveWithOrderTimed helpers (converted to Lua)
function MoveTimedEnd()
    local t = GetExpiredTimer()
    local id = GetHandleId(t)
    SetUnitPositionLoc(LoadUnitHandle(G.Hash, id, 1), LoadLocationHandle(G.Hash, id, 2))
    RemoveLocation(LoadLocationHandle(G.Hash, id, 2))
    DestroyTimer(t)
end

function MoveTimed(u, loc, time)
    local t = CreateTimer()
    local id = GetHandleId(t)
    SaveUnitHandle(G.Hash, id, 1, u)
    SaveLocationHandle(G.Hash, id, 2, loc)
    TimerStart(t, time, false, MoveTimedEnd)
end

function MoveWithOrderTimedEnd()
    local t = GetExpiredTimer()
    local id = GetHandleId(t)
    SetUnitPositionLoc(LoadUnitHandle(G.Hash, id, 1), LoadLocationHandle(G.Hash, id, 2))
    IssueTargetOrder(LoadUnitHandle(G.Hash, id, 1), LoadStr(G.Hash, id, 4), LoadUnitHandle(G.Hash, id, 3))
    RemoveLocation(LoadLocationHandle(G.Hash, id, 2))
    DestroyTimer(t)
end

function MoveWithOrderTimed(u, target, loc, order, time)
    local t = CreateTimer()
    local id = GetHandleId(t)
    SaveUnitHandle(G.Hash, id, 1, u)
    SaveLocationHandle(G.Hash, id, 2, loc)
    SaveUnitHandle(G.Hash, id, 3, target)
    SaveStr(G.Hash, id, 4, order)
    TimerStart(t, time, false, MoveWithOrderTimedEnd)
end

-- BlinkToUnit attack — A0MZ на атаке: телепорт к цели + shadowstrike, 3 сек КД
G.Trig_BlinkToUnit_attack = G.Trig_BlinkToUnit_attack or CreateTrigger()
G.Trig_BlinkToUnit_attack:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_BlinkToUnit_attack:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetAttacker(), FourCC("A0MZ")) >= 1
        and BlzGetUnitAbilityCooldownRemaining(GetAttacker(), FourCC("A0MZ")) == 0
end))
G.Trig_BlinkToUnit_attack:AddAction(function()
    G.gUnit = GetAttacker()
    MoveWithOrderTimed(G.gUnit, GetTriggerUnit(), GetUnitLoc(GetTriggerUnit()), "attack", 0.1)
    -- DummyCastTargetLevel (inline)
    local dumb = CreateUnit(GetOwningPlayer(G.gUnit), FourCC("H0BN"),
        GetUnitX(G.gUnit), GetUnitY(G.gUnit), bj_UNIT_FACING)
    UnitAddAbility(dumb, FourCC("A1MY"))
    SetUnitAbilityLevel(dumb, FourCC("A1MY"), GetUnitAbilityLevel(G.gUnit, FourCC("A0MZ")))
    IssueTargetOrder(dumb, "shadowstrike", GetTriggerUnit())
    UnitApplyTimedLife(dumb, FourCC("BTLF"), 2.0)
    BlzStartUnitAbilityCooldown(G.gUnit, FourCC("A0MZ"), 3)
end)
G.Trig_BlinkToUnit_attack:SetEnabled(false)

-- BlinkToUnit Spell — A0N3 → телепорт к цели с задержкой по дистанции
G.Trig_BlinkToUnit_Spell = G.Trig_BlinkToUnit_Spell or CreateTrigger()
G.Trig_BlinkToUnit_Spell:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_CAST)
G.Trig_BlinkToUnit_Spell:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A0N3")
end))
G.Trig_BlinkToUnit_Spell:AddAction(function()
    local l1 = GetUnitLoc(GetSpellTargetUnit())
    local l2 = GetUnitLoc(GetTriggerUnit())
    MoveWithOrderTimed(GetTriggerUnit(), GetSpellTargetUnit(), l1, "attack",
        DistanceBetweenPoints(l1, l2) / 1200 + 0.4)
    RemoveLocation(l2)
end)
G.Trig_BlinkToUnit_Spell:SetEnabled(false)

-- Edvin Ult ("Резня в тени") — A0N4 → урон врагам в радиусе, windwalk
G.Trig_Edvin_Ult = G.Trig_Edvin_Ult or CreateTrigger()
G.Trig_Edvin_Ult:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_CAST)
G.Trig_Edvin_Ult:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A0N4")
end))
G.Trig_Edvin_Ult:AddAction(function()
    local u = GetTriggerUnit()
    local g = CreateGroup()
    GroupEnumUnitsInRange(g, GetSpellTargetX(), GetSpellTargetY(), 235.0, nil)
    loop
        local u2 = FirstOfGroup(g)
        if u2 == nil then break end
        if GetOwningPlayer(u2) ~= GetOwningPlayer(u) then
            SetUnitX(u, GetUnitX(u2))
            SetUnitY(u, GetUnitY(u2))
            -- RemoveEffectTimed
            DestroyEffect(AddSpecialEffect("Objects\\Spawnmodels\\Human\\HumanBlood\\HumanBloodLarge1.mdl",
                GetUnitX(u2), GetUnitY(u2)))
            UnitDamageTarget(u, u2, 300 * GetUnitAbilityLevel(u, FourCC("A0N4")) + 2 * GetHeroAgi(u, true),
                true, false, ATTACK_TYPE_HERO, DAMAGE_TYPE_FORCE, WEAPON_TYPE_WHOKNOWS)
        end
        GroupRemoveUnit(g, u2)
    end
    UnitAddAbility(u, FourCC("A0N5"))
    BlzUnitDisableAbility(u, FourCC("A0N1"), true, true)
    IssueImmediateOrder(u, "windwalk")
    BlzUnitDisableAbility(u, FourCC("A0N1"), false, false)
    BlzStartUnitAbilityCooldown(u, FourCC("A0N4"), 35)
    DestroyGroup(g)
end)
G.Trig_Edvin_Ult:SetEnabled(false)

-- Dovorougenie helpers
function DovorougenieIsSelected()
    return IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end

-- Dovorougenie Code O (lvl 1) — A000 → улучшение юнитов
G.Trig_Dovorougenie_Code_O = G.Trig_Dovorougenie_Code_O or CreateTrigger()
G.Trig_Dovorougenie_Code_O:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_Dovorougenie_Code_O:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A000") and IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end))
G.Trig_Dovorougenie_Code_O:AddAction(function()
    local uid = GetUnitTypeId(GetTriggerUnit())
    local replace = nil
    if uid == FourCC("h003") then replace = FourCC("h005")
    elseif uid == FourCC("h00P") then replace = FourCC("h00S")
    elseif uid == FourCC("h029") then replace = FourCC("h02A")
    elseif uid == FourCC("n000") then replace = FourCC("n002")
    end
    if replace then
        ReplaceUnitBJ(GetTriggerUnit(), replace, bj_UNIT_STATE_METHOD_RELATIVE)
        if DovorougenieIsSelected() then
            SelectUnitAddForPlayer(bj_lastReplacedUnit, GetOwningPlayer(GetTriggerUnit()))
        end
    end
end)
-- Del1FromTable action appended (JASS init also appends it)
G.Trig_Dovorougenie_Code_O:AddAction(function()
    local i = GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1
    G.udg_UnitsCount[i] = G.udg_UnitsCount[i] - 1
    MultiboardSetItemValue(G.MultiboardItem[G.MultiboardItemOwnerIndex[i - 1] * 2 + 1], tostring(G.udg_UnitsCount[i]))
end)

-- Dovorougenie 2t Code O (lvl 2) — A01A
G.Trig_Dovorougenie_2t_Code_O = G.Trig_Dovorougenie_2t_Code_O or CreateTrigger()
G.Trig_Dovorougenie_2t_Code_O:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_Dovorougenie_2t_Code_O:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A01A") and IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end))
G.Trig_Dovorougenie_2t_Code_O:AddAction(function()
    local uid = GetUnitTypeId(GetTriggerUnit())
    local replace = nil
    if uid == FourCC("h005") then replace = FourCC("h006")
    elseif uid == FourCC("h00S") then replace = FourCC("h00U")
    elseif uid == FourCC("h02A") then replace = FourCC("h02B")
    elseif uid == FourCC("n002") then replace = FourCC("n004")
    end
    if replace then
        ReplaceUnitBJ(GetTriggerUnit(), replace, bj_UNIT_STATE_METHOD_RELATIVE)
        if DovorougenieIsSelected() then
            SelectUnitAddForPlayer(bj_lastReplacedUnit, GetOwningPlayer(GetTriggerUnit()))
        end
    end
end)
G.Trig_Dovorougenie_2t_Code_O:AddAction(function()
    local i = GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1
    G.udg_UnitsCount[i] = G.udg_UnitsCount[i] - 1
    MultiboardSetItemValue(G.MultiboardItem[G.MultiboardItemOwnerIndex[i - 1] * 2 + 1], tostring(G.udg_UnitsCount[i]))
end)

-- Dovorougenie 3t O (lvl 3) — A01B → только h006 → h00Q
G.Trig_Dovorougenie_3t_O = G.Trig_Dovorougenie_3t_O or CreateTrigger()
G.Trig_Dovorougenie_3t_O:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_Dovorougenie_3t_O:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A01B") and IsUnitSelected(GetTriggerUnit(), GetOwningPlayer(GetTriggerUnit()))
end))
G.Trig_Dovorougenie_3t_O:AddAction(function()
    local i = GetPlayerId(GetOwningPlayer(GetTriggerUnit())) + 1
    if GetUnitTypeId(GetTriggerUnit()) == FourCC("h006") then
        ReplaceUnitBJ(GetTriggerUnit(), FourCC("h00Q"), bj_UNIT_STATE_METHOD_RELATIVE)
        if DovorougenieIsSelected() then
            SelectUnitAddForPlayer(bj_lastReplacedUnit, GetOwningPlayer(GetTriggerUnit()))
        end
    end
    G.udg_UnitsCount[i] = G.udg_UnitsCount[i] - 1
    MultiboardSetItemValue(G.MultiboardItem[G.MultiboardItemOwnerIndex[i - 1] * 2 + 1], tostring(G.udg_UnitsCount[i]))
end)
G.Trig_Dovorougenie_3t_O:SetEnabled(false)

-- ============================== NIGHT ELF ==============================

-- KrugBeg — исследование R0G1 на старте → заблокировать другие ветки
G.Trig_KrugBeg = G.Trig_KrugBeg or CreateTrigger()
G.Trig_KrugBeg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_KrugBeg:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0G1")
end))
G.Trig_KrugBeg:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R0G2"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("Remk"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("Remg"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("Reib"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("R0G6"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("R0G7"), 0)
    SetPlayerTechResearched(p, FourCC("R0GB"), 1)
end)

-- KrugCan — отмена R0G1 → вернуть доступ к веткам
G.Trig_KrugCan = G.Trig_KrugCan or CreateTrigger()
G.Trig_KrugCan:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_KrugCan:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0G1")
end))
G.Trig_KrugCan:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R0G2"), 1)
    SetPlayerTechMaxAllowed(p, FourCC("Remk"), 1)
    SetPlayerTechMaxAllowed(p, FourCC("Remg"), 1)
    SetPlayerTechMaxAllowed(p, FourCC("Reib"), 1)
end)

-- KrugFin — завершение R0G1 → разблокировать юнитов круга
G.Trig_KrugFin = G.Trig_KrugFin or CreateTrigger()
G.Trig_KrugFin:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_KrugFin:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0G1")
end))
G.Trig_KrugFin:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("e00J"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("n064"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("edot"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("edoc"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("n05D"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("n05H"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("earc"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("esen"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("e00I"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("e00H"), 0)
end)

-- ElfBegFin — исследование R0G2 (начало или завершение) → переключение веток
G.Trig_ElfBegFin = G.Trig_ElfBegFin or CreateTrigger()
G.Trig_ElfBegFin:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_ElfBegFin:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_ElfBegFin:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0G2")
end))
G.Trig_ElfBegFin:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R0GB"), 1)
    SetPlayerTechMaxAllowed(p, FourCC("R0G1"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("Redc"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("Reeb"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("Reec"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("Redt"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("R0G9"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("R0GA"), 0)
    SetPlayerTechMaxAllowed(p, FourCC("R0G8"), 0)
    SetPlayerTechResearched(p, FourCC("R0GB"), 1)
end)

-- ElfCan — отмена R0G2 → вернуть R0G1
G.Trig_ElfCan = G.Trig_ElfCan or CreateTrigger()
G.Trig_ElfCan:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_ElfCan:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0G2")
end))
G.Trig_ElfCan:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0G1"), 1)
end)

-- malfurionPas — изучение A160 → добавить A161 с тем же уровнем
G.Trig_malfurionPas = G.Trig_malfurionPas or CreateTrigger()
G.Trig_malfurionPas:RegisterAnyUnitEvent(EVENT_PLAYER_HERO_SKILL)
G.Trig_malfurionPas:AddCondition(Condition(function()
    return GetLearnedSkill() == FourCC("A160")
end))
G.Trig_malfurionPas:AddAction(function()
    local u = GetTriggerUnit()
    local lvl = GetUnitAbilityLevel(u, FourCC("A160"))
    UnitAddAbility(u, FourCC("A161"))
    SetUnitAbilityLevel(u, FourCC("A161"), lvl)
end)

-- ============================== NAGA ==============================

-- MurlokCan — отмена R0FF → разблокировать R0FE
G.Trig_MurlokCan = G.Trig_MurlokCan or CreateTrigger()
G.Trig_MurlokCan:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_MurlokCan:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0FF")
end))
G.Trig_MurlokCan:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0FE"), 1)
end)

-- MurlokBeg — старт R0FF → заблокировать R0FE
G.Trig_MurlokBeg = G.Trig_MurlokBeg or CreateTrigger()
G.Trig_MurlokBeg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_MurlokBeg:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0FF")
end))
G.Trig_MurlokBeg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0FE"), 0)
end)

-- MurlocFin — завершение R0FF → разблокировать юнитов мурлоков
G.Trig_MurlocFin = G.Trig_MurlocFin or CreateTrigger()
G.Trig_MurlocFin:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_MurlocFin:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0FF")
end))
G.Trig_MurlocFin:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("n053"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("n052"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("n050"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("n054"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("H0OZ"), 1) -- HERO TANK
    SetPlayerTechMaxAllowed(p, FourCC("R0FQ"), 3)
end)

-- VaishBuria — A16E → создаёт торнадо (ntor) на 30 сек
G.Trig_VaishBuria = G.Trig_VaishBuria or CreateTrigger()
G.Trig_VaishBuria:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_VaishBuria:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A16E")
end))
G.Trig_VaishBuria:AddAction(function()
    local loc = GetSpellTargetLoc()
    local u2 = CreateUnitAtLoc(GetOwningPlayer(GetTriggerUnit()), FourCC("ntor"), loc, bj_UNIT_FACING)
    UnitApplyTimedLife(u2, FourCC("BTLF"), 30.0)
    RemoveLocation(loc)
end)

-- VaishArrow — A16C пассивка: 10% шанс frostnova при атаке
G.Trig_VaishArrow = G.Trig_VaishArrow or CreateTrigger()
G.Trig_VaishArrow:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_DAMAGED)
G.Trig_VaishArrow:AddCondition(Condition(function()
    G.gCaster = GetEventDamageSource()
    return GetUnitAbilityLevel(G.gCaster, FourCC("A16C")) > 0
        and BlzGetEventAttackType() == ATTACK_TYPE_NORMAL
        and math.random(1, 10) == 1
end))
G.Trig_VaishArrow:AddAction(function()
    local lvl = GetUnitAbilityLevel(G.gCaster, FourCC("A16C"))
    local dumb = CreateUnit(GetOwningPlayer(G.gCaster), FourCC("H0BN"),
        GetUnitX(G.gCaster), GetUnitY(G.gCaster), bj_UNIT_FACING)
    UnitAddAbility(dumb, FourCC("A16D"))
    SetUnitAbilityLevel(dumb, FourCC("A16D"), lvl)
    IssueTargetOrder(dumb, "frostnova", BlzGetEventDamageTarget())
    UnitApplyTimedLife(dumb, FourCC("BTLF"), 2.0)
end)

-- NagaPas — изучение A13A → замена пассивки по уровню
G.Trig_NagaPas = G.Trig_NagaPas or CreateTrigger()
G.Trig_NagaPas:RegisterAnyUnitEvent(EVENT_PLAYER_HERO_SKILL)
G.Trig_NagaPas:AddCondition(Condition(function()
    return GetLearnedSkill() == FourCC("A13A")
end))
G.Trig_NagaPas:AddAction(function()
    local u = GetTriggerUnit()
    local lvl = GetUnitAbilityLevel(u, FourCC("A13A"))
    if lvl == 1 then
        UnitAddAbility(u, FourCC("A136"))
    elseif lvl == 2 then
        UnitAddAbility(u, FourCC("A137"))
        UnitRemoveAbility(u, FourCC("A136"))
    elseif lvl == 3 then
        UnitAddAbility(u, FourCC("A138"))
        UnitRemoveAbility(u, FourCC("A137"))
    elseif lvl == 4 then
        UnitAddAbility(u, FourCC("A139"))
        UnitRemoveAbility(u, FourCC("A138"))
    end
end)

-- NagaCommonSpell — A1LT если юнит на воде → добавить S00E на 180 сек
G.Trig_NagaCommonSpell = G.Trig_NagaCommonSpell or CreateTrigger()
G.Trig_NagaCommonSpell:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_NagaCommonSpell:AddCondition(Condition(function()
    local u = GetTriggerUnit()
    return GetSpellAbilityId() == FourCC("A1LT")
        and not IsTerrainPathable(GetUnitX(u), GetUnitY(u), PATHING_TYPE_FLOATABILITY)
end))
G.Trig_NagaCommonSpell:AddAction(function()
    local u = GetTriggerUnit()
    UnitAddAbility(u, FourCC("S00E"))
    -- RemoveAbilityTimed
    local t = CreateTimer()
    local id = GetHandleId(t)
    SaveUnitHandle(G.Hash, id, 1, u)
    TimerStart(t, 180, false, function()
        local tid = GetHandleId(GetExpiredTimer())
        local uu = LoadUnitHandle(G.Hash, tid, 1)
        UnitRemoveAbility(uu, FourCC("S00E"))
        DestroyTimer(GetExpiredTimer())
    end)
end)

-- ============================== GOBLINS ==============================

-- CorrupTrain — тренировка юнита: установить уровни A0AV/A0AW по уровню R04O
G.Trig_CorrupTrain = G.Trig_CorrupTrain or CreateTrigger()
G.Trig_CorrupTrain:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_TRAIN_FINISH)
G.Trig_CorrupTrain:AddCondition(Condition(function()
    return GetPlayerTechCountSimple(GetOwningPlayer(GetTriggerUnit()), FourCC("R04O")) >= 1
end))
G.Trig_CorrupTrain:AddAction(function()
    local u = GetTrainedUnit()
    local lvl = GetPlayerTechCountSimple(GetOwningPlayer(GetTriggerUnit()), FourCC("R04O"))
    SetUnitAbilityLevel(u, FourCC("A0AV"), lvl)
    SetUnitAbilityLevel(u, FourCC("A0AW"), lvl)
end)
G.Trig_CorrupTrain:SetEnabled(false)

-- CorrupPlus — A0AS → +1 к R04O, обновить способности юнитам, КД 60 сек
G.Trig_CorrupPlus = G.Trig_CorrupPlus or CreateTrigger()
G.Trig_CorrupPlus:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_CorrupPlus:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A0AS")
end))
G.Trig_CorrupPlus:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailable(p, FourCC("A0AS"), false)
    SetPlayerAbilityAvailable(p, FourCC("A0AT"), false)
    SetPlayerTechResearched(p, FourCC("R04O"), GetPlayerTechCountSimple(p, FourCC("R04O")) + 1)

    local g = CreateGroup()
    GroupEnumUnitsOfPlayer(g, p, nil)
    local lvl = GetPlayerTechCountSimple(p, FourCC("R04O"))
    ForGroup(g, function()
        SetUnitAbilityLevel(GetEnumUnit(), FourCC("A0AW"), lvl)
        SetUnitAbilityLevel(GetEnumUnit(), FourCC("A0AV"), lvl)
    end)
    DestroyGroup(g)

    local t = CreateTimer()
    local tid = GetHandleId(t)
    SaveInteger(G.Hash, tid, 0, GetPlayerId(p))
    TimerStart(t, 60, false, function()
        local ti = GetExpiredTimer()
        local thi = GetHandleId(ti)
        local pp = Player(LoadInteger(G.Hash, thi, 0))
        if GetPlayerTechCountSimple(pp, FourCC("R04O")) == 6 then
            SetPlayerAbilityAvailable(pp, FourCC("A0AT"), true)
        else
            SetPlayerAbilityAvailable(pp, FourCC("A0AS"), true)
            SetPlayerAbilityAvailable(pp, FourCC("A0AT"), true)
        end
        FlushChildHashtable(G.Hash, thi)
        DestroyTimer(ti)
    end)
end)
G.Trig_CorrupPlus:SetEnabled(false)

-- CorrupMinus — A0AT → -1 от R04O, КД 60 сек
G.Trig_CorrupMinus = G.Trig_CorrupMinus or CreateTrigger()
G.Trig_CorrupMinus:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_CorrupMinus:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A0AT")
end))
G.Trig_CorrupMinus:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailable(p, FourCC("A0AS"), false)
    SetPlayerAbilityAvailable(p, FourCC("A0AT"), false)
    SetPlayerTechResearched(p, FourCC("R04O"), GetPlayerTechCountSimple(p, FourCC("R04O")) - 1)

    local g = CreateGroup()
    GroupEnumUnitsOfPlayer(g, p, nil)
    local lvl = GetPlayerTechCountSimple(p, FourCC("R04O"))
    ForGroup(g, function()
        SetUnitAbilityLevel(GetEnumUnit(), FourCC("A0AW"), lvl)
        SetUnitAbilityLevel(GetEnumUnit(), FourCC("A0AV"), lvl)
    end)
    DestroyGroup(g)

    local t = CreateTimer()
    local tid = GetHandleId(t)
    SaveInteger(G.Hash, tid, 0, GetPlayerId(p))
    TimerStart(t, 60, false, function()
        local ti = GetExpiredTimer()
        local thi = GetHandleId(ti)
        local pp = Player(LoadInteger(G.Hash, thi, 0))
        if GetPlayerTechCountSimple(pp, FourCC("R04O")) == 1 then
            SetPlayerAbilityAvailable(pp, FourCC("A0AS"), true)
        else
            SetPlayerAbilityAvailable(pp, FourCC("A0AS"), true)
            SetPlayerAbilityAvailable(pp, FourCC("A0AT"), true)
        end
        FlushChildHashtable(G.Hash, thi)
        DestroyTimer(ti)
    end)
end)
G.Trig_CorrupMinus:SetEnabled(false)

-- Potreblenie — исследование R04N → улучшить A0A5 всем юнитам (+1; макс 6)
G.Trig_Potreblenie = G.Trig_Potreblenie or CreateTrigger()
G.Trig_Potreblenie:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_Potreblenie:AddCondition(Condition(function()
    return GetResearched() == FourCC("R04N")
end))
G.Trig_Potreblenie:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    if GetPlayerTechCountSimple(p, FourCC("R04N")) == 6 then
        SetPlayerAbilityAvailable(p, FourCC("A0A5"), false)
        return
    end
    local g = CreateGroup()
    GroupEnumUnitsOfPlayer(g, p, Condition(function() return GetUnitAbilityLevel(GetFilterUnit(), FourCC("A0A5")) ~= 0 end))
    ForGroup(g, function()
        SetUnitAbilityLevel(GetEnumUnit(), FourCC("A0A5"), GetPlayerTechCountSimple(p, FourCC("R04N")) + 1)
    end)
    DestroyGroup(g)
end)
G.Trig_Potreblenie:SetEnabled(false)

-- PotreblenieTrain — тренировка юнита с A0A5 → установить уровень
G.Trig_PotreblenieTrain = G.Trig_PotreblenieTrain or CreateTrigger()
G.Trig_PotreblenieTrain:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_TRAIN_FINISH)
G.Trig_PotreblenieTrain:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC("A0A5")) >= 1
end))
G.Trig_PotreblenieTrain:AddAction(function()
    local u = GetTriggerUnit()
    SetUnitAbilityLevel(u, FourCC("A0A5"), GetPlayerTechCountSimple(GetOwningPlayer(u), FourCC("R04N")) + 1)
end)
G.Trig_PotreblenieTrain:SetEnabled(false)

-- Adrenalin — A0D2 → -15% HP кастера
G.Trig_Adrenalin = G.Trig_Adrenalin or CreateTrigger()
G.Trig_Adrenalin:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_Adrenalin:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A0D2")
end))
G.Trig_Adrenalin:AddAction(function()
    local u = GetTriggerUnit()
    SetUnitLifePercentBJ(u, GetUnitLifePercent(u) - 15.0)
end)
G.Trig_Adrenalin:SetEnabled(false)

-- GazloySpellheals — A1KK: вампиризм при атаке (level * 1% от урона)
G.Trig_GazloySpellheals = G.Trig_GazloySpellheals or CreateTrigger()
G.Trig_GazloySpellheals:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_DAMAGED)
G.Trig_GazloySpellheals:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetEventDamageSource(), FourCC("A1KK")) > 0
        and IsPlayerEnemy(GetOwningPlayer(GetEventDamageSource()), GetOwningPlayer(GetTriggerUnit()))
end))
G.Trig_GazloySpellheals:AddAction(function()
    local u = GetEventDamageSource()
    local level = GetUnitAbilityLevel(u, FourCC("A1KK"))
    local damage = GetEventDamage()
    local e = AddSpecialEffectTarget("Abilities\\Spells\\Items\\VampiricPotion\\VampPotionCaster.mdl", u, "Chest")
    SetUnitState(u, UNIT_STATE_LIFE, GetUnitState(u, UNIT_STATE_LIFE) + damage * (0.01 * level))
    DestroyEffect(e)
end)

-- Helper for research-based unit unlocks (GOBLINS)
local function MakeGoblinResearchTrig(name, researchIds, requiredCounts, unitRawcode)
    local trig = G["Trig_" .. name] or CreateTrigger()
    G["Trig_" .. name] = trig
    trig:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    trig:AddCondition(Condition(function()
        local r = GetResearched()
        for _, rid in ipairs(researchIds) do
            if r == rid then return true end
        end
        return false
    end))
    trig:AddCondition(Condition(function()
        local p = GetOwningPlayer(GetTriggerUnit())
        for i, rid in ipairs(researchIds) do
            if GetPlayerTechCountSimple(p, rid) < requiredCounts[i] then return false end
        end
        return true
    end))
    trig:AddAction(function()
        SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), unitRawcode, -1)
    end)
    trig:SetEnabled(false)
end

-- Pulimetchik — R04E >=2 + R04K >=2 → h06L
MakeGoblinResearchTrig("Pulimetchik", {FourCC("R04E"), FourCC("R04K")}, {2, 2}, FourCC("h06L"))

-- Ognemetchik — R04G >=2 + R04K >=2 → h06Q
MakeGoblinResearchTrig("Ognemetchik", {FourCC("R04G"), FourCC("R04K")}, {2, 2}, FourCC("h06Q"))

-- Raketchik — R04F >=2 + R04K >=2 → h06N
MakeGoblinResearchTrig("Raketchik", {FourCC("R04F"), FourCC("R04K")}, {2, 2}, FourCC("h06N"))

-- Medic — R04P >=2 + R04K >=2 → h06O
MakeGoblinResearchTrig("Medic", {FourCC("R04P"), FourCC("R04K")}, {2, 2}, FourCC("h06O"))

-- Sniper — R04E >=3 + R04M >=2 + R04K >=2 → h06M
MakeGoblinResearchTrig("Sniper", {FourCC("R04E"), FourCC("R04M"), FourCC("R04K")}, {3, 2, 2}, FourCC("h06M"))

-- Saper — R04F >=3 + R04K >=2 → h078
MakeGoblinResearchTrig("Saper", {FourCC("R04F"), FourCC("R04K")}, {3, 2}, FourCC("h078"))

-- Car (goblins) — R04F >=2 + R04L >=1 + R04I >=1 → h06R
MakeGoblinResearchTrig("Car", {FourCC("R04F"), FourCC("R04L"), FourCC("R04I")}, {2, 1, 1}, FourCC("h06R"))

-- Vezdehod — R04E >=2 + R04L >=1 + R04I >=1 → h06U
MakeGoblinResearchTrig("Vezdehod", {FourCC("R04E"), FourCC("R04L"), FourCC("R04I")}, {2, 1, 1}, FourCC("h06U"))

-- Tank (goblins) — R04F >=2 + R04L >=2 + R04I >=2 → h06T
MakeGoblinResearchTrig("Tank", {FourCC("R04F"), FourCC("R04L"), FourCC("R04I")}, {2, 2, 2}, FourCC("h06T"))

-- FireTank — R04G >=2 + R04L >=2 + R04I >=2 → h06S
MakeGoblinResearchTrig("FireTank", {FourCC("R04G"), FourCC("R04L"), FourCC("R04I")}, {2, 2, 2}, FourCC("h06S"))

-- Arta — R04F >=2 + R04L >=1 + R04M >=2 + R04I >=1 → h06Y
MakeGoblinResearchTrig("Arta", {FourCC("R04F"), FourCC("R04L"), FourCC("R04M"), FourCC("R04I")}, {2, 1, 2, 1}, FourCC("h06Y"))

-- Submarina — R04F >=1 + R04L >=1 + R04I >=1 → h06V
MakeGoblinResearchTrig("Submarina", {FourCC("R04F"), FourCC("R04L"), FourCC("R04I")}, {1, 1, 1}, FourCC("h06V"))

-- Podlodka1 — R04L >=2 + R04I >=2 + R04F >=2 → h06W
MakeGoblinResearchTrig("Podlodka1", {FourCC("R04F"), FourCC("R04L"), FourCC("R04I")}, {2, 2, 2}, FourCC("h06W"))

-- TankFire — A19N при атаке: 7% шанс breathoffire
G.Trig_TankFire = G.Trig_TankFire or CreateTrigger()
G.Trig_TankFire:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_TankFire:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetAttacker(), FourCC("A19N")) > 0
        and IsPlayerEnemy(GetOwningPlayer(GetTriggerUnit()), GetOwningPlayer(GetAttacker()))
        and math.random(1, 100) <= 7
end))
G.Trig_TankFire:AddAction(function()
    IssueTargetOrder(GetAttacker(), "breathoffire", GetTriggerUnit())
end)

-- TankChangeAttack — A0S6 → переключение оружия (0 ↔ 1)
G.Trig_TankChangeAttack = G.Trig_TankChangeAttack or CreateTrigger()
G.Trig_TankChangeAttack:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_TankChangeAttack:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A0S6")
end))
G.Trig_TankChangeAttack:AddAction(function()
    local u = GetTriggerUnit()
    if BlzGetUnitWeaponBooleanField(u, UNIT_WEAPON_BF_ATTACKS_ENABLED, 0) then
        BlzSetUnitWeaponBooleanField(u, UNIT_WEAPON_BF_ATTACKS_ENABLED, 0, false)
        BlzSetUnitWeaponBooleanField(u, UNIT_WEAPON_BF_ATTACKS_ENABLED, 1, true)
    else
        BlzSetUnitWeaponBooleanField(u, UNIT_WEAPON_BF_ATTACKS_ENABLED, 0, true)
        BlzSetUnitWeaponBooleanField(u, UNIT_WEAPON_BF_ATTACKS_ENABLED, 1, false)
    end
end)
G.Trig_TankChangeAttack:SetEnabled(false)

-- TankVenecAttack — A0S2 пассивка: добавить/убрать A0S3 при атаке
G.Trig_TankVenecAttack = G.Trig_TankVenecAttack or CreateTrigger()
G.Trig_TankVenecAttack:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_TankVenecAttack:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetAttacker(), FourCC("A0S2")) > 0
end))
G.Trig_TankVenecAttack:AddAction(function()
    local attacker = GetAttacker()
    if GetUnitAbilityLevel(attacker, FourCC("A0S3")) == 0 then
        UnitAddAbility(attacker, FourCC("A0S3"))
    else
        UnitRemoveAbility(attacker, FourCC("A0S3"))
    end
end)
G.Trig_TankVenecAttack:SetEnabled(false)

-- ============================== BLOOD ELVES ==============================

-- ManaAura — постройка h04F → добавить A1GT
G.Trig_ManaAura = G.Trig_ManaAura or CreateTrigger()
G.Trig_ManaAura:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
G.Trig_ManaAura:AddCondition(Condition(function()
    return GetUnitTypeId(GetConstructedStructure()) == FourCC("h04F")
end))
G.Trig_ManaAura:AddAction(function()
    UnitAddAbility(GetConstructedStructure(), FourCC("A1GT"))
end)
G.Trig_ManaAura:SetEnabled(false)

-- Helper for Blood Elf path selection (Arcana/Fel/Void/Light)
local function MakeBloodElfPathTrig(name, research, count, colorName)
    -- Main finish trigger
    local trig = G["Trig_" .. name] or CreateTrigger()
    G["Trig_" .. name] = trig
    trig:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    trig:AddCondition(Condition(function()
        return GetResearched() == research and GetPlayerTechCountSimple(GetOwningPlayer(GetTriggerUnit()), research) == count
    end))
    trig:AddAction(function()
        local p = GetOwningPlayer(GetTriggerUnit())
        local g1 = CreateGroup()
        GroupEnumUnitsOfPlayer(g1, p, Condition(function() return GetUnitTypeId(GetFilterUnit()) == FourCC("h04F") end))
        ForGroup(g1, function()
            BlzSetUnitName(GetEnumUnit(), colorName)
        end)
        DestroyGroup(g1)
    end)
    trig:SetEnabled(false)

    -- Begin trigger
    local trigB = G["Trig_" .. name .. "Begin"] or CreateTrigger()
    G["Trig_" .. name .. "Begin"] = trigB
    trigB:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
    trigB:AddCondition(Condition(function()
        return GetResearched() == research and GetPlayerTechCountSimple(GetOwningPlayer(GetTriggerUnit()), research) == count - 1
    end))
    trigB:AddAction(function() end) -- Will be filled per-path
    trigB:SetEnabled(false)

    -- Cancel trigger
    local trigC = G["Trig_" .. name .. "Cansel"] or CreateTrigger()
    G["Trig_" .. name .. "Cansel"] = trigC
    trigC:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    trigC:AddCondition(Condition(function()
        return GetResearched() == research and GetPlayerTechCountSimple(GetOwningPlayer(GetTriggerUnit()), research) == count - 1
    end))
    trigC:AddAction(function() end) -- Will be filled per-path
    trigC:SetEnabled(false)

    return trig, trigB, trigC
end

-- Arcana (R01D count==3)
MakeBloodElfPathTrig("Arcana", FourCC("R01D"), 3, "|cff8080ffКолодец арканы|r")
G.Trig_Arcana:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechResearched(p, FourCC("R01E"), 1)
    SetPlayerTechResearched(p, FourCC("R01F"), 1)
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 2)
end)
G.Trig_ArcanaBegin:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 2)
end)
G.Trig_ArcanaCansel:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 3)
end)

-- Fel (R01G count==3)
MakeBloodElfPathTrig("Fel", FourCC("R01G"), 3, "|cff80ff80Колодец скверны|r")
G.Trig_Fel:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("h0O6"), -1)
    SetPlayerTechMaxAllowed(p, FourCC("h03Z"), 0)
end)
G.Trig_FelBegin:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 2)
end)
G.Trig_FelCansel:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 3)
end)

-- Void (R01H count==3)
MakeBloodElfPathTrig("Void", FourCC("R01H"), 3, "|cffff00ffКолодец бездны|r")
G.Trig_Void:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 2)
    SetPlayerTechResearched(p, FourCC("R020"), 1)
end)
G.Trig_VoidBegin:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 2)
end)
G.Trig_VoidCansel:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01I"), 3)
end)

-- Light (R01I count==3)
MakeBloodElfPathTrig("Light", FourCC("R01I"), 3, "|cffffff00Колодец света|r")
G.Trig_Light:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 2)
end)
G.Trig_LightBegin:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 2)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 2)
end)
G.Trig_LightCansel:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R01D"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01G"), 3)
    SetPlayerTechMaxAllowed(p, FourCC("R01H"), 3)
end)

-- Build triggers: rename h04F on construction based on active path
local function MakeBuildTrig(name, research, colorName)
    local trig = G["Trig_" .. name] or CreateTrigger()
    G["Trig_" .. name] = trig
    trig:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_CONSTRUCT_FINISH)
    trig:AddCondition(Condition(function()
        return GetUnitTypeId(GetConstructedStructure()) == FourCC("h04F")
            and GetPlayerTechCountSimple(GetOwningPlayer(GetTriggerUnit()), research) == 3
    end))
    trig:AddAction(function()
        BlzSetUnitName(GetTriggerUnit(), colorName)
    end)
    trig:SetEnabled(false)
end

MakeBuildTrig("ArcanaBuild", FourCC("R01D"), "|cff8080ffКолодец арканы|r")
MakeBuildTrig("FelBuild", FourCC("R01G"), "|cff80ff80Колодец скверны|r")
MakeBuildTrig("VoidBuild", FourCC("R01H"), "|cffff00ffКолодец бездны|r")
MakeBuildTrig("LigthBuild", FourCC("R01I"), "|cffffff00Колодец света|r")

-- FelGolemStrike — A1LW: 5% шанс forkedlightning при атаке
G.Trig_FelGolemStrike = G.Trig_FelGolemStrike or CreateTrigger()
G.Trig_FelGolemStrike:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_FelGolemStrike:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetAttacker(), FourCC("A1LW")) == 1 and math.random(1, 20) == 1
end))
G.Trig_FelGolemStrike:AddAction(function()
    IssueTargetOrder(GetAttacker(), "forkedlightning", GetTriggerUnit())
end)

-- VoidElfes — R0HL → пересчёт лимита, -3 main price
G.Trig_VoidElfes = G.Trig_VoidElfes or CreateTrigger()
G.Trig_VoidElfes:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_VoidElfes:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0HL")
end))
G.Trig_VoidElfes:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    local pi = GetPlayerId(p)
    AcountAll(p)
    G.udg_MainPrice[pi] = G.udg_MainPrice[pi] - 3
end)

-- LightArmy — R0HK → пересчёт лимита, -3 main price
G.Trig_LightArmy = G.Trig_LightArmy or CreateTrigger()
G.Trig_LightArmy:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_LightArmy:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0HK")
end))
G.Trig_LightArmy:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    local pi = GetPlayerId(p)
    AcountAll(p)
    G.udg_MainPrice[pi] = G.udg_MainPrice[pi] - 3
end)

-- Porcha — A02X: 10% шанс A08I на 9 сек при атаке
G.Trig_Porcha = G.Trig_Porcha or CreateTrigger()
G.Trig_Porcha:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_Porcha:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetAttacker(), FourCC("A02X")) > 0
end))
G.Trig_Porcha:AddAction(function()
    if math.random(1, 10) == 1 then
        local atk = GetAttacker()
        UnitAddAbility(atk, FourCC("A08I"))
        -- RemoveAbilityTimed
        local t = CreateTimer()
        local id = GetHandleId(t)
        SaveUnitHandle(G.Hash, id, 1, atk)
        TimerStart(t, 9, false, function()
            local ti = GetExpiredTimer()
            local thi = GetHandleId(ti)
            UnitRemoveAbility(LoadUnitHandle(G.Hash, thi, 1), FourCC("A08I"))
            DestroyTimer(ti)
        end)
    end
end)
G.Trig_Porcha:SetEnabled(false)

-- Souz — A02Y → добавить A16H цели на 60 сек (если ещё нет)
G.Trig_Souz = G.Trig_Souz or CreateTrigger()
G.Trig_Souz:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_Souz:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A02Y") and GetUnitAbilityLevel(GetSpellTargetUnit(), FourCC("A16H")) ~= 1
end))
G.Trig_Souz:AddAction(function()
    local u = GetSpellTargetUnit()
    UnitAddAbility(u, FourCC("A16H"))
    local t = CreateTimer()
    local id = GetHandleId(t)
    SaveUnitHandle(G.Hash, id, 1, u)
    TimerStart(t, 60, false, function()
        local ti = GetExpiredTimer()
        local thi = GetHandleId(ti)
        UnitRemoveAbility(LoadUnitHandle(G.Hash, thi, 1), FourCC("A16H"))
        DestroyTimer(ti)
    end)
end)
G.Trig_Souz:SetEnabled(false)

-- AutoStrela helpers
local function MakeAutoStrelaTrig(name, spellIds, order)
    local trig = G["Trig_AutoStrela" .. name] or CreateTrigger()
    G["Trig_AutoStrela" .. name] = trig
    trig:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
    trig:AddCondition(Condition(function()
        local sid = GetSpellAbilityId()
        for _, id in ipairs(spellIds) do
            if sid == id then return true end
        end
        return false
    end))
    trig:AddAction(function()
        IssueTargetOrder(GetTriggerUnit(), order, GetSpellTargetUnit())
    end)
    trig:SetEnabled(false)
end

-- AutoStrelaFire — A00W/A07Q → firebolt
MakeAutoStrelaTrig("Fire", {FourCC("A00W"), FourCC("A07Q")}, "firebolt")

-- AutoStrelaArcana — A07D/A02U → firebolt
MakeAutoStrelaTrig("Arcana", {FourCC("A07D"), FourCC("A02U")}, "firebolt")

-- AutoStrelaFel — A02Z/A07O → firebolt
MakeAutoStrelaTrig("Fel", {FourCC("A02Z"), FourCC("A07O")}, "firebolt")

-- AutoStrelaFireIlly — A1KL → firebolt
G.Trig_AutoStrelaFireIlly = G.Trig_AutoStrelaFireIlly or CreateTrigger()
G.Trig_AutoStrelaFireIlly:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_AutoStrelaFireIlly:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A1KL")
end))
G.Trig_AutoStrelaFireIlly:AddAction(function()
    IssueTargetOrder(GetTriggerUnit(), "firebolt", GetSpellTargetUnit())
end)

-- AutoStrelaFelllly — A1KO → acidbomb
G.Trig_AutoStrelaFelllly = G.Trig_AutoStrelaFelllly or CreateTrigger()
G.Trig_AutoStrelaFelllly:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_AutoStrelaFelllly:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A1KO")
end))
G.Trig_AutoStrelaFelllly:AddAction(function()
    IssueTargetOrder(GetTriggerUnit(), "acidbomb", GetSpellTargetUnit())
end)

-- ============================== GNOMES ==============================

-- Helper: tech tree node with start/1_beg/1_can/1/2_beg/2_can/2 pattern
local function MakeGnomeTechTree(name, startResearch, sub1, sub2, startUnit, sub2Abil)
    -- start trigger
    local trigS = G["Trig_" .. name .. "_start"] or CreateTrigger()
    G["Trig_" .. name .. "_start"] = trigS
    trigS:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    trigS:AddCondition(Condition(function() return GetResearched() == startResearch end))
    trigS:AddAction(function()
        G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
        TriggerExecute(G.gg_trg_All_Gnomes_Off)
        SetPlayerTechMaxAllowed(G.udg_LocalPlayer, sub1, 1)
        SetPlayerTechMaxAllowed(G.udg_LocalPlayer, sub2, 1)
        SetPlayerTechMaxAllowed(G.udg_LocalPlayer, startUnit, -1)
    end)

    -- 1 finish
    local trig1 = G["Trig_" .. name .. "_1"] or CreateTrigger()
    G["Trig_" .. name .. "_1"] = trig1
    trig1:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    trig1:AddCondition(Condition(function() return GetResearched() == sub1 end))
    trig1:AddAction(function()
        SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), sub2, 0)
        G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
        TriggerExecute(G.gg_trg_All_Gnomes)
    end)

    -- 1 beg (disable other)
    local trig1B = G["Trig_" .. name .. "_1_Beg"] or CreateTrigger()
    G["Trig_" .. name .. "_1_Beg"] = trig1B
    trig1B:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
    trig1B:AddCondition(Condition(function() return GetResearched() == sub1 end))
    trig1B:AddAction(function()
        SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), sub2, 0)
    end)

    -- 1 can (re-enable other)
    local trig1C = G["Trig_" .. name .. "_1_Can"] or CreateTrigger()
    G["Trig_" .. name .. "_1_Can"] = trig1C
    trig1C:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    trig1C:AddCondition(Condition(function() return GetResearched() == sub1 end))
    trig1C:AddAction(function()
        SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), sub2, 1)
    end)

    -- 2 finish
    local trig2 = G["Trig_" .. name .. "_2"] or CreateTrigger()
    G["Trig_" .. name .. "_2"] = trig2
    trig2:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    trig2:AddCondition(Condition(function() return GetResearched() == sub2 end))
    trig2:AddAction(function()
        SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), sub1, 0)
        G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
        if sub2Abil then
            SetPlayerAbilityAvailable(G.udg_LocalPlayer, sub2Abil, true)
        end
        TriggerExecute(G.gg_trg_All_Gnomes)
    end)

    -- 2 beg
    local trig2B = G["Trig_" .. name .. "_2_Beg"] or CreateTrigger()
    G["Trig_" .. name .. "_2_Beg"] = trig2B
    trig2B:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
    trig2B:AddCondition(Condition(function() return GetResearched() == sub2 end))
    trig2B:AddAction(function()
        SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), sub1, 0)
    end)

    -- 2 can
    local trig2C = G["Trig_" .. name .. "_2_Can"] or CreateTrigger()
    G["Trig_" .. name .. "_2_Can"] = trig2C
    trig2C:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    trig2C:AddCondition(Condition(function() return GetResearched() == sub2 end))
    trig2C:AddAction(function()
        SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), sub1, 1)
    end)
end

-- Also handle the simpler 2-research pattern (no sub-abil on 2)
local function MakeGnomeTechTreeSimple(name, startResearch, sub1, sub2, startUnit)
    MakeGnomeTechTree(name, startResearch, sub1, sub2, startUnit, nil)
end

-- ===== GELBIN SPELLS =====

-- GelbinSpellAttacked — A0XC: при атаке юнита, в зависимости от HP% выставить уровень A0XD
G.Trig_GelbinSpellAttacked = G.Trig_GelbinSpellAttacked or CreateTrigger()
G.Trig_GelbinSpellAttacked:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_ATTACKED)
G.Trig_GelbinSpellAttacked:AddCondition(Condition(function()
    return GetUnitAbilityLevel(GetTriggerUnit(), FourCC("A0XC")) == 1
end))
G.Trig_GelbinSpellAttacked:AddAction(function()
    local u = GetTriggerUnit()
    local hp = GetUnitLifePercent(u)
    local lvl = 1
    if hp < 20 then lvl = 5
    elseif hp < 40 then lvl = 4
    elseif hp < 60 then lvl = 3
    elseif hp < 80 then lvl = 2
    end
    SetUnitAbilityLevel(u, FourCC("A0XD"), lvl)
end)
G.Trig_GelbinSpellAttacked:SetEnabled(false)

-- GelbinSpellClick — A0XC активное: +10% HP + обновить A0XD
G.Trig_GelbinSpellClick = G.Trig_GelbinSpellClick or CreateTrigger()
G.Trig_GelbinSpellClick:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_SPELL_EFFECT)
G.Trig_GelbinSpellClick:AddCondition(Condition(function()
    return GetSpellAbilityId() == FourCC("A0XC")
end))
G.Trig_GelbinSpellClick:AddAction(function()
    local u = GetTriggerUnit()
    SetUnitLifePercentBJ(u, GetUnitLifePercent(u) + 10.0)
    local hp = GetUnitLifePercent(u)
    local lvl = 1
    if hp < 20 then lvl = 5
    elseif hp < 40 then lvl = 4
    elseif hp < 60 then lvl = 3
    elseif hp < 80 then lvl = 2
    end
    SetUnitAbilityLevel(u, FourCC("A0XD"), lvl)
end)
G.Trig_GelbinSpellClick:SetEnabled(false)

-- ===== MEHAWAR =====
MakeGnomeTechTree("MehaWar", FourCC("R0BA"), FourCC("R0BQ"), FourCC("R0BR"), FourCC("h0G1"))

-- MehaWar Def (R0BQ finish) — disable opponent, execute All_Gnomes
-- Already handled by MakeGnomeTechTree

-- MehaWar Stan (R0BR finish) — disable opponent, execute All_Gnomes
-- Already handled by MakeGnomeTechTree

-- ===== NANOGNOME =====
MakeGnomeTechTree("NanoGnome", FourCC("R0BC"), FourCC("R0C2"), FourCC("R0C8"), FourCC("h0G2"))

-- Additional NanoGnome1 ability unlock
G.Trig_NanoGnome1:AddAction(function()
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC("A16A"), true)
end)

-- ===== MEHA GIGANT =====
MakeGnomeTechTree("MehaGigant", FourCC("R0BH"), FourCC("R0CP"), FourCC("R0CQ"), FourCC("h0FW"), FourCC("A0U8"))

-- ===== SPIDER =====
MakeGnomeTechTree("Spider", FourCC("R0B5"), FourCC("R0CR"), FourCC("R0CS"), FourCC("h0FV"))

-- ===== CHAHOHOD =====
MakeGnomeTechTree("Chahohod", FourCC("R0B3"), FourCC("R0CT"), FourCC("R0CU"), FourCC("h0G0"))

-- Chahohod also has a 3rd tier (R0CV)
-- Chahohod 3 and its _beg_Copy (same as _beg for 3, just copy-pasted)
G.Trig_Chahohod_3 = G.Trig_Chahohod_3 or CreateTrigger()
G.Trig_Chahohod_3:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_Chahohod_3:AddCondition(Condition(function() return GetResearched() == FourCC("R0CV") end))
G.Trig_Chahohod_3:AddAction(function()
    G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailable(G.udg_LocalPlayer, FourCC("A0U5"), true)
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_Chahohod_3_beg = G.Trig_Chahohod_3_beg or CreateTrigger()
G.Trig_Chahohod_3_beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_Chahohod_3_beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0CV") end))
G.Trig_Chahohod_3_beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0CW"), 0)
end)

-- Chahohod_3_beg_Copy (identical, registers start for R0CW)
G.Trig_Chahohod_3_beg_Copy = G.Trig_Chahohod_3_beg_Copy or CreateTrigger()
G.Trig_Chahohod_3_beg_Copy:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_Chahohod_3_beg_Copy:AddCondition(Condition(function() return GetResearched() == FourCC("R0CW") end))
G.Trig_Chahohod_3_beg_Copy:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0CV"), 0)
end)

-- Chahohod_3_can (cancel for R0CV)
G.Trig_Chahohod_3_can = G.Trig_Chahohod_3_can or CreateTrigger()
G.Trig_Chahohod_3_can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_Chahohod_3_can:AddCondition(Condition(function() return GetResearched() == FourCC("R0CV") end))
G.Trig_Chahohod_3_can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0CU"), 1)
end)

-- ===== MINITANK =====
MakeGnomeTechTree("Minitank", FourCC("R0B4"), FourCC("R0CX"), FourCC("R0CY"), FourCC("h0FX"))

-- Minitank 3 tier
G.Trig_Minitank_3 = G.Trig_Minitank_3 or CreateTrigger()
G.Trig_Minitank_3:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_Minitank_3:AddCondition(Condition(function() return GetResearched() == FourCC("R0CZ") end))
G.Trig_Minitank_3:AddAction(function()
    G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailable(G.udg_LocalPlayer, FourCC("A0UC"), true)
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_Minitank_3_beg = G.Trig_Minitank_3_beg or CreateTrigger()
G.Trig_Minitank_3_beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_Minitank_3_beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0CZ") end))
G.Trig_Minitank_3_beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0D0"), 0)
end)

G.Trig_Minitank_3_can = G.Trig_Minitank_3_can or CreateTrigger()
G.Trig_Minitank_3_can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_Minitank_3_can:AddCondition(Condition(function() return GetResearched() == FourCC("R0CZ") end))
G.Trig_Minitank_3_can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0CY"), 1)
end)

-- ===== UNITANK =====
MakeGnomeTechTree("UniTank", FourCC("R0B1"), FourCC("R0D1"), FourCC("R0D2"), FourCC("h0FT"))

-- UniTank 3 tier
G.Trig_UniTank_3 = G.Trig_UniTank_3 or CreateTrigger()
G.Trig_UniTank_3:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_UniTank_3:AddCondition(Condition(function() return GetResearched() == FourCC("R0D3") end))
G.Trig_UniTank_3:AddAction(function()
    G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailable(G.udg_LocalPlayer, FourCC("A0UB"), true)
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_UniTank_3_beg = G.Trig_UniTank_3_beg or CreateTrigger()
G.Trig_UniTank_3_beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_UniTank_3_beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0D3") end))
G.Trig_UniTank_3_beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0D4"), 0)
end)

G.Trig_UniTank_3_can = G.Trig_UniTank_3_can or CreateTrigger()
G.Trig_UniTank_3_can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_UniTank_3_can:AddCondition(Condition(function() return GetResearched() == FourCC("R0D3") end))
G.Trig_UniTank_3_can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0D2"), 1)
end)

-- ===== VENEC TANK =====
MakeGnomeTechTree("Venec_Tank", FourCC("R0B2"), FourCC("R0D5"), FourCC("R0D6"), FourCC("h0FU"))

-- Venec_Tank 3 tier
G.Trig_Venec_Tank_3 = G.Trig_Venec_Tank_3 or CreateTrigger()
G.Trig_Venec_Tank_3:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_Venec_Tank_3:AddCondition(Condition(function() return GetResearched() == FourCC("R0D7") end))
G.Trig_Venec_Tank_3:AddAction(function()
    G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_Venec_Tank_3_beg = G.Trig_Venec_Tank_3_beg or CreateTrigger()
G.Trig_Venec_Tank_3_beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_Venec_Tank_3_beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0D7") end))
G.Trig_Venec_Tank_3_beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0D8"), 0)
end)

G.Trig_Venec_Tank_3_can = G.Trig_Venec_Tank_3_can or CreateTrigger()
G.Trig_Venec_Tank_3_can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_Venec_Tank_3_can:AddCondition(Condition(function() return GetResearched() == FourCC("R0D7") end))
G.Trig_Venec_Tank_3_can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0D6"), 1)
end)

-- ===== CAR (Gnomes) =====
MakeGnomeTechTree("Car", FourCC("R0B9"), FourCC("R0D9"), FourCC("R0DA"), FourCC("h0FZ"))

-- Car 3 tier
G.Trig_Car_3 = G.Trig_Car_3 or CreateTrigger()
G.Trig_Car_3:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_Car_3:AddCondition(Condition(function() return GetResearched() == FourCC("R0DB") end))
G.Trig_Car_3:AddAction(function()
    G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
    SetPlayerAbilityAvailable(G.udg_LocalPlayer, FourCC("A19F"), true)
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_Car_3_beg = G.Trig_Car_3_beg or CreateTrigger()
G.Trig_Car_3_beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_Car_3_beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0DB") end))
G.Trig_Car_3_beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DC"), 0)
end)

G.Trig_Car_3_can = G.Trig_Car_3_can or CreateTrigger()
G.Trig_Car_3_can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_Car_3_can:AddCondition(Condition(function() return GetResearched() == FourCC("R0DB") end))
G.Trig_Car_3_can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DA"), 1)
end)

-- ===== SGT =====
MakeGnomeTechTree("SGT", FourCC("R0B8"), FourCC("R0DL"), FourCC("R0DM"), FourCC("h0GJ"))

-- SGT 2 ability unlock
G.Trig_SGT_2:AddAction(function()
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC("A0UG"), true)
end)

-- SGT 3 tier
G.Trig_SGT_3 = G.Trig_SGT_3 or CreateTrigger()
G.Trig_SGT_3:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_SGT_3:AddCondition(Condition(function() return GetResearched() == FourCC("R0DN") end))
G.Trig_SGT_3:AddAction(function()
    G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_SGT_3_beg = G.Trig_SGT_3_beg or CreateTrigger()
G.Trig_SGT_3_beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_SGT_3_beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0DN") end))
G.Trig_SGT_3_beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DO"), 0)
end)

G.Trig_SGT_3_can = G.Trig_SGT_3_can or CreateTrigger()
G.Trig_SGT_3_can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_SGT_3_can:AddCondition(Condition(function() return GetResearched() == FourCC("R0DN") end))
G.Trig_SGT_3_can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DM"), 1)
end)

-- ===== SAU =====
MakeGnomeTechTree("SAU", FourCC("R0B7"), FourCC("R0DP"), FourCC("R0DQ"), FourCC("h0GI"))

-- SAU 2 ability unlock
G.Trig_SAU_2:AddAction(function()
    SetPlayerAbilityAvailable(GetOwningPlayer(GetTriggerUnit()), FourCC("A0UL"), true)
end)

-- SAU 3 tier
G.Trig_SAU_3 = G.Trig_SAU_3 or CreateTrigger()
G.Trig_SAU_3:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_SAU_3:AddCondition(Condition(function() return GetResearched() == FourCC("R0DR") end))
G.Trig_SAU_3:AddAction(function()
    G.udg_LocalPlayer = GetOwningPlayer(GetTriggerUnit())
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_SAU_3_beg = G.Trig_SAU_3_beg or CreateTrigger()
G.Trig_SAU_3_beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_SAU_3_beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0DR") end))
G.Trig_SAU_3_beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DS"), 0)
end)

G.Trig_SAU_3_can = G.Trig_SAU_3_can or CreateTrigger()
G.Trig_SAU_3_can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_SAU_3_can:AddCondition(Condition(function() return GetResearched() == FourCC("R0DR") end))
G.Trig_SAU_3_can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DQ"), 1)
end)

-- ===== MEGA_SAU =====
G.Trig_MEGA_SAU = G.Trig_MEGA_SAU or CreateTrigger()
G.Trig_MEGA_SAU:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_MEGA_SAU:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0DT")
end))
G.Trig_MEGA_SAU:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R0DU"), 0)
    G.udg_LocalPlayer = p
    SetPlayerAbilityAvailable(p, FourCC("A0VN"), true)
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_MEGA_SAU_Beg = G.Trig_MEGA_SAU_Beg or CreateTrigger()
G.Trig_MEGA_SAU_Beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_MEGA_SAU_Beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0DT") end))
G.Trig_MEGA_SAU_Beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DU"), 0)
end)

G.Trig_MEGA_SAU_Can = G.Trig_MEGA_SAU_Can or CreateTrigger()
G.Trig_MEGA_SAU_Can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_MEGA_SAU_Can:AddCondition(Condition(function() return GetResearched() == FourCC("R0DT") end))
G.Trig_MEGA_SAU_Can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DU"), 1)
end)

-- ===== URAN =====
G.Trig_URAN = G.Trig_URAN or CreateTrigger()
G.Trig_URAN:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_FINISH)
G.Trig_URAN:AddCondition(Condition(function()
    return GetResearched() == FourCC("R0DU")
end))
G.Trig_URAN:AddAction(function()
    local p = GetOwningPlayer(GetTriggerUnit())
    SetPlayerTechMaxAllowed(p, FourCC("R0DT"), 0)
    G.udg_LocalPlayer = p
    SetPlayerAbilityAvailable(p, FourCC("A0VM"), true)
    TriggerExecute(G.gg_trg_All_Gnomes)
end)

G.Trig_URAN_Beg = G.Trig_URAN_Beg or CreateTrigger()
G.Trig_URAN_Beg:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_START)
G.Trig_URAN_Beg:AddCondition(Condition(function() return GetResearched() == FourCC("R0DU") end))
G.Trig_URAN_Beg:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DT"), 0)
end)

G.Trig_URAN_Can = G.Trig_URAN_Can or CreateTrigger()
G.Trig_URAN_Can:RegisterAnyUnitEvent(EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
G.Trig_URAN_Can:AddCondition(Condition(function() return GetResearched() == FourCC("R0DU") end))
G.Trig_URAN_Can:AddAction(function()
    SetPlayerTechMaxAllowed(GetOwningPlayer(GetTriggerUnit()), FourCC("R0DT"), 1)
end)
