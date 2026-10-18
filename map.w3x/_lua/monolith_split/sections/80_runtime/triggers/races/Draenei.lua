
--===========================================================================
-- Trigger: Draenei Build Abill
--===========================================================================
function Trig_Draenei_Build_Abill_Conditions()
    return GetUnitAbilityLevel(GetConstructingStructure(), FourCC('A0Z3')) > 0
end
function Trig_Draenei_Build_Abill_Actions()
    local u = GetConstructingStructure()
    if Random(1 , 2) and GetPlayerTechCount(GetOwningPlayer(u), FourCC('R0EB'), true) > 0 then
        local t = CreateTimer()
        TimerStart(t, 0, false, function()
            DestroyTimer(t)
            if GetUnitTypeId(u) == 0 or GetUnitState(u, UNIT_STATE_LIFE) <= 0.405 then
                return
            end
            UnitSetConstructionProgress(u, 20)
            DestroyEffect(AddSpecialEffectTarget("Abilities\\Spells\\Undead\\OrbOfDeath\\OrbOfDeathMissile.mdl", u, "origin"))
        end)
    end
    UnitRemoveAbility(u, FourCC('A0Z3'))
end
--===========================================================================
function InitTrig_Draenei_Build_Abill()
    gg_trg_Draenei_Build_Abill=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Draenei_Build_Abill, EVENT_PLAYER_UNIT_CONSTRUCT_START)
    TriggerAddCondition(gg_trg_Draenei_Build_Abill, Condition(Trig_Draenei_Build_Abill_Conditions))
    TriggerAddAction(gg_trg_Draenei_Build_Abill, Trig_Draenei_Build_Abill_Actions)
    DraeneiCombat.Init()
end
--===========================================================================
-- Trigger: flot1
--===========================================================================
function Trig_flot1_Conditions()
    return GetResearched() == FourCC('R027')
end

--===========================================================================
-- Draenei combat: charged attacks, protective vows and the memory idol.
-- Each timer services only units/effects that have used these mechanics.
--===========================================================================
DraeneiCombat = {
    units = {}, protection = {}, wards = {}, clock = 0, timer = nil,
    ids = {
        arrows = FourCC('ADr1'), blade = FourCC('ADr2'), vow = FourCC('ADr3'),
        wave = FourCC('ADr4'), idol = FourCC('ADr5'), ward = FourCC('nDr1'),
        arrowTech = FourCC('RDr1'), bladeTech = FourCC('RDr2'),
        vowTech = FourCC('RDr3'), waveTech = FourCC('RDr4'), idolTech = FourCC('RDr5'),
    },
    fx = {
        arrow = "Draenei\\Effects\\NetherArrow.mdx",
        blade = "Draenei\\Effects\\BlazingSpecialArt.mdx",
        shield = "Draenei\\Effects\\GlowShield.mdx",
        heal = "Draenei\\Effects\\Reconstitute.mdx",
        blessing = "Draenei\\Effects\\HolyAura.mdx",
    },
}

function DraeneiCombat.Alive(u)
    return u ~= nil and GetUnitTypeId(u) ~= 0 and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
end

function DraeneiCombat.HasTech(p, id)
    return GetPlayerTechCount(p, id, true) > 0
end

function DraeneiCombat.Flash(path, u)
    DestroyEffect(AddSpecialEffectTarget(path, u, "origin"))
end

function DraeneiCombat.EnsureTimer()
    if DraeneiCombat.timer == nil then
        DraeneiCombat.timer = CreateTimer()
        TimerStart(DraeneiCombat.timer, 0.25, true, DraeneiCombat.Tick)
    end
end

function DraeneiCombat.State(u)
    local data = DraeneiCombat.units[u]
    local owner = GetOwningPlayer(u)
    if data == nil or data.owner ~= owner then
        data = {unit = u, owner = owner, charges = 2, recharge = 0, bladeRemaining = 0}
        DraeneiCombat.units[u] = data
    end
    DraeneiCombat.EnsureTimer()
    return data
end

function DraeneiCombat.InMemoryField(u)
    local owner = GetOwningPlayer(u)
    for _, data in ipairs(DraeneiCombat.wards) do
        if data.owner == owner and DraeneiCombat.Alive(data.unit)
            and GetOwningPlayer(data.unit) == owner then
            local dx, dy = GetUnitX(u) - GetUnitX(data.unit), GetUnitY(u) - GetUnitY(data.unit)
            if dx * dx + dy * dy <= 400 * 400 then return true end
        end
    end
    return false
end

-- Explicit stable tie-breaks keep target selection deterministic in multiplayer.
function DraeneiCombat.Targets(x, y, radius, owner, predicate, byHealth)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, x, y, radius, nil)
    local result = {}
    for i = 0, BlzGroupGetSize(group) - 1 do
        local u = BlzGroupUnitAt(group, i)
        if DraeneiCombat.Alive(u) and predicate(u, owner) then
            local dx, dy = GetUnitX(u) - x, GetUnitY(u) - y
            result[#result + 1] = {
                unit = u, distance = dx * dx + dy * dy, handle = GetHandleId(u),
                health = GetUnitState(u, UNIT_STATE_LIFE) / GetUnitState(u, UNIT_STATE_MAX_LIFE),
            }
        end
    end
    DestroyGroup(group)
    table.sort(result, function(a, b)
        if byHealth and a.health ~= b.health then return a.health < b.health end
        if a.distance ~= b.distance then return a.distance < b.distance end
        return a.handle < b.handle
    end)
    return result
end

function DraeneiCombat.Healable(u, owner)
    return IsUnitAlly(u, owner) and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
        and not IsUnitType(u, UNIT_TYPE_MECHANICAL) and not IsUnitType(u, UNIT_TYPE_WARD)
        and not IsUnitIllusion(u)
        and GetUnitState(u, UNIT_STATE_LIFE) < GetUnitState(u, UNIT_STATE_MAX_LIFE)
end

function DraeneiCombat.Enemy(u, owner)
    return IsUnitEnemy(u, owner) and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
        and not IsUnitType(u, UNIT_TYPE_MAGIC_IMMUNE) and not BlzIsUnitInvulnerable(u)
end

function DraeneiCombat.Heal(u, amount)
    if not DraeneiCombat.Alive(u) then return 0 end
    local life = GetUnitState(u, UNIT_STATE_LIFE)
    local restored = math.min(amount, GetUnitState(u, UNIT_STATE_MAX_LIFE) - life)
    if restored <= 0 then return 0 end
    SetUnitState(u, UNIT_STATE_LIFE, life + restored)
    DraeneiCombat.Flash(DraeneiCombat.fx.heal, u)
    -- Only actual, substantial healing from these spells hastens the blade.
    if restored >= 20 and GetUnitAbilityLevel(u, DraeneiCombat.ids.blade) > 0 then
        local data = DraeneiCombat.State(u)
        data.bladeRemaining = math.max(0, data.bladeRemaining - 2)
    end
    return restored
end

function DraeneiCombat.ClearProtection(u)
    local data = DraeneiCombat.protection[u]
    if data ~= nil then
        if data.vowEffect ~= nil then DestroyEffect(data.vowEffect) end
        if data.blessingEffect ~= nil then DestroyEffect(data.blessingEffect) end
        DraeneiCombat.protection[u] = nil
    end
end

function DraeneiCombat.Protection(u)
    local data = DraeneiCombat.protection[u]
    if data ~= nil and data.owner ~= GetOwningPlayer(u) then
        DraeneiCombat.ClearProtection(u)
        data = nil
    end
    if data == nil then
        data = {unit = u, owner = GetOwningPlayer(u)}
        DraeneiCombat.protection[u] = data
    end
    DraeneiCombat.EnsureTimer()
    return data
end

function DraeneiCombat.ApplyVow(caster, target)
    if not DraeneiCombat.Alive(target) or not IsUnitAlly(target, GetOwningPlayer(caster))
        or IsUnitType(target, UNIT_TYPE_STRUCTURE) or IsUnitIllusion(target) then return false end
    local data = DraeneiCombat.Protection(target)
    local hero = IsUnitType(target, UNIT_TYPE_HERO)
    data.vowCharges = hero and 2 or 3
    data.vowReduction = hero and 0.15 or 0.30
    data.vowExpires = DraeneiCombat.clock + (hero and 8 or 12)
    data.vowOwner = GetOwningPlayer(caster)
    if data.vowEffect ~= nil then DestroyEffect(data.vowEffect) end
    data.vowEffect = AddSpecialEffectTarget(DraeneiCombat.fx.shield, target, "origin")
    BlzSetSpecialEffectScale(data.vowEffect, hero and 0.6 or 0.8)
    return true
end

function DraeneiCombat.ApplyBlessing(caster, target)
    local data = DraeneiCombat.Protection(target)
    local hero = IsUnitType(target, UNIT_TYPE_HERO)
    data.blessingReduction = hero and 0.05 or 0.10
    data.blessingExpires = DraeneiCombat.clock + (hero and 3 or 4)
    data.blessingOwner = GetOwningPlayer(caster)
    if data.blessingEffect ~= nil then DestroyEffect(data.blessingEffect) end
    data.blessingEffect = AddSpecialEffectTarget(DraeneiCombat.fx.blessing, target, "origin")
    BlzSetSpecialEffectScale(data.blessingEffect, 0.35)
end

function DraeneiCombat.Wave(caster, target)
    local owner = GetOwningPlayer(caster)
    if not DraeneiCombat.Alive(target) or not DraeneiCombat.Healable(target, owner) then return false end
    local restored = DraeneiCombat.Heal(target, 130)
    if restored >= 20 and DraeneiCombat.HasTech(owner, DraeneiCombat.ids.waveTech) then
        DraeneiCombat.ApplyBlessing(caster, target)
    end
    local hit = {[target] = true}
    local current, amount = target, 130
    for bounce = 1, 2 do
        local choices = DraeneiCombat.Targets(GetUnitX(current), GetUnitY(current), 500, owner,
            function(u, p) return not hit[u] and DraeneiCombat.Healable(u, p) end, false)
        if #choices == 0 then break end
        current = choices[1].unit
        hit[current] = true
        amount = amount * 0.75
        DraeneiCombat.Heal(current, amount)
    end
    return true
end

function DraeneiCombat.SummonIdol(caster, x, y)
    -- A caster owns one idol; remove its previous copy before placing the new one.
    for i = #DraeneiCombat.wards, 1, -1 do
        local data = DraeneiCombat.wards[i]
        if data.caster == caster then
            if GetUnitTypeId(data.unit) ~= 0 then RemoveUnit(data.unit) end
            table.remove(DraeneiCombat.wards, i)
        end
    end
    local owner = GetOwningPlayer(caster)
    local ward = CreateUnit(owner, DraeneiCombat.ids.ward, x, y, 0)
    if ward == nil then return nil end
    UnitApplyTimedLife(ward, FourCC('BTlf'), 25)
    DraeneiCombat.wards[#DraeneiCombat.wards + 1] = {
        unit = ward, caster = caster, owner = owner,
        expires = DraeneiCombat.clock + 25, pulse = DraeneiCombat.clock + 1,
    }
    DraeneiCombat.EnsureTimer()
    return ward
end

function DraeneiCombat.ArrowShards(source, primary, x, y)
    local owner = GetOwningPlayer(source)
    local t = CreateTimer()
    TimerStart(t, 0, false, function()
        DestroyTimer(t)
        if not DraeneiCombat.Alive(source) or GetOwningPlayer(source) ~= owner then return end
        local targets = DraeneiCombat.Targets(x, y, 220, owner,
            function(u, p) return u ~= primary and DraeneiCombat.Enemy(u, p) end, false)
        for i = 1, math.min(2, #targets) do
            local target = targets[i].unit
            if DraeneiCombat.Alive(target) then
                DraeneiCombat.Flash(DraeneiCombat.fx.arrow, target)
                -- Spell damage cannot retrigger charged basic attacks.
                UnitDamageTarget(source, target, 15, false, false, ATTACK_TYPE_NORMAL,
                    DAMAGE_TYPE_MAGIC, WEAPON_TYPE_WHOKNOWS)
            end
        end
    end)
end

function DraeneiCombat.Damage()
    local amount = GetEventDamage()
    if amount <= 0 then return end
    local source, target = GetEventDamageSource(), BlzGetEventDamageTarget()
    if not DraeneiCombat.Alive(source) or not DraeneiCombat.Alive(target)
        or not IsUnitEnemy(target, GetOwningPlayer(source)) then return end
    local attack = BlzGetEventIsAttack()
    if attack and not IsUnitIllusion(source) and not IsUnitType(target, UNIT_TYPE_STRUCTURE)
        and not BlzIsUnitInvulnerable(target) then
        local owner = GetOwningPlayer(source)
        if GetUnitTypeId(source) == FourCC('e000')
            and GetUnitAbilityLevel(source, DraeneiCombat.ids.arrows) > 0
            and DraeneiCombat.HasTech(owner, DraeneiCombat.ids.arrowTech) then
            local data = DraeneiCombat.State(source)
            if data.charges > 0 then
                data.charges = data.charges - 1
                SetUnitAbilityLevel(source, DraeneiCombat.ids.arrows, 3 - data.charges)
                amount = amount + 8
                DraeneiCombat.Flash(DraeneiCombat.fx.arrow, target)
                DraeneiCombat.ArrowShards(source, target, GetUnitX(target), GetUnitY(target))
            end
        elseif GetUnitTypeId(source) == FourCC('h059')
            and GetUnitAbilityLevel(source, DraeneiCombat.ids.blade) > 0
            and DraeneiCombat.HasTech(owner, DraeneiCombat.ids.bladeTech) then
            local data = DraeneiCombat.State(source)
            if data.bladeRemaining <= 0
                and GetUnitState(source, UNIT_STATE_LIFE) >= GetUnitState(source, UNIT_STATE_MAX_LIFE) * 0.85 then
                amount = amount + 30
                data.bladeRemaining = 8
                DraeneiCombat.Flash(DraeneiCombat.fx.blade, target)
            end
        end
    end
    local protection = DraeneiCombat.protection[target]
    if protection ~= nil then
        if protection.owner ~= GetOwningPlayer(target) then
            DraeneiCombat.ClearProtection(target)
        else
            local reduction = 0
            if attack and (protection.vowCharges or 0) > 0
                and protection.vowExpires > DraeneiCombat.clock
                and IsUnitAlly(target, protection.vowOwner) then
                reduction = protection.vowReduction
                protection.vowCharges = protection.vowCharges - 1
                if protection.vowCharges == 0 and protection.vowEffect ~= nil then
                    DestroyEffect(protection.vowEffect)
                    protection.vowEffect = nil
                end
            end
            if protection.blessingExpires ~= nil and protection.blessingExpires > DraeneiCombat.clock
                and IsUnitAlly(target, protection.blessingOwner) then
                -- Vow and blessing use the stronger reduction rather than stacking.
                reduction = math.max(reduction, protection.blessingReduction)
            end
            amount = amount * (1 - reduction)
        end
    end
    BlzSetEventDamage(amount)
end

function DraeneiCombat.Tick()
    DraeneiCombat.clock = DraeneiCombat.clock + 0.25
    local now = DraeneiCombat.clock
    local healed = {}
    for i = #DraeneiCombat.wards, 1, -1 do
        local data = DraeneiCombat.wards[i]
        if not DraeneiCombat.Alive(data.unit) or GetOwningPlayer(data.unit) ~= data.owner or now >= data.expires then
            if GetUnitTypeId(data.unit) ~= 0 then RemoveUnit(data.unit) end
            table.remove(DraeneiCombat.wards, i)
        elseif now >= data.pulse then
            data.pulse = now + 1
            local targets = DraeneiCombat.Targets(GetUnitX(data.unit), GetUnitY(data.unit), 400, data.owner,
                function(u, owner) return GetOwningPlayer(u) == owner and DraeneiCombat.Healable(u, owner) end, true)
            for j = 1, math.min(6, #targets) do
                local u = targets[j].unit
                if not healed[u] then
                    healed[u] = true
                    local fraction = IsUnitType(u, UNIT_TYPE_HERO) and 0.01 or 0.02
                    DraeneiCombat.Heal(u, math.min(40, GetUnitState(u, UNIT_STATE_MAX_LIFE) * fraction))
                end
            end
        end
    end
    for u, data in pairs(DraeneiCombat.units) do
        if not DraeneiCombat.Alive(u) or GetOwningPlayer(u) ~= data.owner
            or (GetUnitAbilityLevel(u, DraeneiCombat.ids.arrows) == 0
                and GetUnitAbilityLevel(u, DraeneiCombat.ids.blade) == 0) then
            DraeneiCombat.units[u] = nil
        else
            local speed = DraeneiCombat.InMemoryField(u) and 1.5 or 1
            if GetUnitAbilityLevel(u, DraeneiCombat.ids.arrows) > 0 and data.charges < 2 then
                data.recharge = data.recharge + 0.25 * speed
                if data.recharge >= 18 then
                    data.recharge = data.recharge - 18
                    data.charges = data.charges + 1
                    if data.charges == 2 then data.recharge = 0 end
                    SetUnitAbilityLevel(u, DraeneiCombat.ids.arrows, 3 - data.charges)
                end
            end
            if GetUnitAbilityLevel(u, DraeneiCombat.ids.blade) > 0 then
                data.bladeRemaining = math.max(0, data.bladeRemaining - 0.25 * speed)
            end
        end
    end
    for u, data in pairs(DraeneiCombat.protection) do
        if not DraeneiCombat.Alive(u) or GetOwningPlayer(u) ~= data.owner then
            DraeneiCombat.ClearProtection(u)
        else
            if data.vowEffect ~= nil and (now >= data.vowExpires or not IsUnitAlly(u, data.vowOwner)) then
                DestroyEffect(data.vowEffect)
                data.vowEffect = nil
                data.vowCharges = 0
            end
            if data.blessingEffect ~= nil and (now >= data.blessingExpires or not IsUnitAlly(u, data.blessingOwner)) then
                DestroyEffect(data.blessingEffect)
                data.blessingEffect = nil
            end
            if data.vowEffect == nil and data.blessingEffect == nil then DraeneiCombat.ClearProtection(u) end
        end
    end
    if next(DraeneiCombat.units) == nil and next(DraeneiCombat.protection) == nil and #DraeneiCombat.wards == 0 then
        local t = DraeneiCombat.timer
        DraeneiCombat.timer = nil
        if t ~= nil then DestroyTimer(t) end
    end
end

function DraeneiCombat.Spell()
    local id, caster = GetSpellAbilityId(), GetTriggerUnit()
    if not DraeneiCombat.Alive(caster) then return end
    local owner = GetOwningPlayer(caster)
    if id == DraeneiCombat.ids.vow and GetUnitTypeId(caster) == FourCC('h01O')
        and DraeneiCombat.HasTech(owner, DraeneiCombat.ids.vowTech) then
        DraeneiCombat.ApplyVow(caster, GetSpellTargetUnit())
    elseif id == DraeneiCombat.ids.wave and GetUnitTypeId(caster) == FourCC('h01R') then
        DraeneiCombat.Wave(caster, GetSpellTargetUnit())
    elseif id == DraeneiCombat.ids.idol and GetUnitTypeId(caster) == FourCC('n005')
        and DraeneiCombat.HasTech(owner, DraeneiCombat.ids.idolTech) then
        DraeneiCombat.SummonIdol(caster, GetSpellTargetX(), GetSpellTargetY())
    end
end

function DraeneiCombat.Init()
    if DraeneiCombat.damageTrigger ~= nil then return end
    DraeneiCombat.damageTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(DraeneiCombat.damageTrigger, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddAction(DraeneiCombat.damageTrigger, DraeneiCombat.Damage)
    DraeneiCombat.spellTrigger = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(DraeneiCombat.spellTrigger, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(DraeneiCombat.spellTrigger, DraeneiCombat.Spell)
end

function DraeneiCombat.AiVow(caster)
    if GetUnitState(caster, UNIT_STATE_MANA) < 70
        or BlzGetUnitAbilityCooldownRemaining(caster, DraeneiCombat.ids.vow) > 0
        or not DraeneiCombat.HasTech(GetOwningPlayer(caster), DraeneiCombat.ids.vowTech) then return false end
    local targets = DraeneiCombat.Targets(GetUnitX(caster), GetUnitY(caster), 600, GetOwningPlayer(caster),
        function(u, owner)
            local data = DraeneiCombat.protection[u]
            return GetOwningPlayer(u) == owner and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
                and not IsUnitType(u, UNIT_TYPE_MECHANICAL) and not IsUnitIllusion(u)
                and not IsUnitType(u, UNIT_TYPE_RANGED_ATTACKER)
                and (data == nil or (data.vowCharges or 0) == 0 or data.vowExpires <= DraeneiCombat.clock)
        end, true)
    if #targets > 0 then return IssueTargetOrder(caster, "spiritlink", targets[1].unit) end
    return false
end

function DraeneiCombat.AiIdol(caster)
    if GetUnitState(caster, UNIT_STATE_MANA) < 150
        or BlzGetUnitAbilityCooldownRemaining(caster, DraeneiCombat.ids.idol) > 0
        or not DraeneiCombat.HasTech(GetOwningPlayer(caster), DraeneiCombat.ids.idolTech)
        or DraeneiCombat.InMemoryField(caster) then return false end
    local targets = DraeneiCombat.Targets(GetUnitX(caster), GetUnitY(caster), 400, GetOwningPlayer(caster),
        function(u, owner) return GetOwningPlayer(u) == owner and not IsUnitType(u, UNIT_TYPE_STRUCTURE)
            and not IsUnitType(u, UNIT_TYPE_MECHANICAL) and not IsUnitIllusion(u) end, true)
    local lost, spent = 0, false
    for _, target in ipairs(targets) do
        local u = target.unit
        lost = lost + GetUnitState(u, UNIT_STATE_MAX_LIFE) - GetUnitState(u, UNIT_STATE_LIFE)
        local data = DraeneiCombat.units[u]
        if data ~= nil and (data.charges < 2 or data.bladeRemaining > 0) then spent = true end
    end
    if #targets >= 3 and (lost >= 60 or spent) then
        return IssuePointOrder(caster, "healingward", GetUnitX(caster), GetUnitY(caster))
    end
    return false
end
function Trig_flot1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02S'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot1()
    gg_trg_flot1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_flot1, Condition(Trig_flot1_Conditions))
    TriggerAddAction(gg_trg_flot1, Trig_flot1_Actions)
end
--===========================================================================
-- Trigger: flot2
--===========================================================================
function Trig_flot2_Conditions()
    return GetResearched() == FourCC('R027')
end
function Trig_flot2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R02S'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_flot2()
    gg_trg_flot2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_flot2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_flot2, Condition(Trig_flot2_Conditions))
    TriggerAddAction(gg_trg_flot2, Trig_flot2_Actions)
end
--===========================================================================
-- Trigger: arm1
--===========================================================================
function Trig_arm1_Conditions()
    return GetResearched() == FourCC('R02S')
end
function Trig_arm1_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R027'), 0, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm1()
    gg_trg_arm1=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1, EVENT_PLAYER_UNIT_RESEARCH_FINISH)
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm1, EVENT_PLAYER_UNIT_RESEARCH_START)
    TriggerAddCondition(gg_trg_arm1, Condition(Trig_arm1_Conditions))
    TriggerAddAction(gg_trg_arm1, Trig_arm1_Actions)
end
--===========================================================================
-- Trigger: arm2
--===========================================================================
function Trig_arm2_Conditions()
    return GetResearched() == FourCC('R02S')
end
function Trig_arm2_Actions()
    SetPlayerTechMaxAllowedSwap(FourCC('R027'), 1, GetOwningPlayer(GetTriggerUnit()))
end
--===========================================================================
function InitTrig_arm2()
    gg_trg_arm2=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_arm2, EVENT_PLAYER_UNIT_RESEARCH_CANCEL)
    TriggerAddCondition(gg_trg_arm2, Condition(Trig_arm2_Conditions))
    TriggerAddAction(gg_trg_arm2, Trig_arm2_Actions)
end
--===========================================================================
-- Trigger: Auto pohichenie Copy
--===========================================================================
function Trig_Auto_pohichenie_Copy_Actions()
    IssueTargetOrderBJ(GetTriggerUnit(), "banish", GetSpellTargetUnit())
end
--===========================================================================
function InitTrig_Auto_pohichenie_Copy()
    gg_trg_Auto_pohichenie_Copy=CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(gg_trg_Auto_pohichenie_Copy, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(gg_trg_Auto_pohichenie_Copy, function()
        if GetSpellAbilityId() ~= FourCC('A031') then return end
        Trig_Auto_pohichenie_Copy_Actions()
    end)
end
