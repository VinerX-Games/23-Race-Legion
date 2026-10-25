-- Spell-scent charge lives in the passive ability level: no per-unit tables or timers.
WorgenKnight = {unitId = FourCC('h0IW'), abilityId = FourCC('AWkn'), researchId = FourCC('RWkn')}

function WorgenKnight.Eligible(unit)
    return unit ~= nil and GetUnitTypeId(unit) == WorgenKnight.unitId
        and GetUnitState(unit, UNIT_STATE_LIFE) > 0.405 and not IsUnitIllusion(unit)
        and not IsUnitHidden(unit) and not IsUnitLoaded(unit)
        and GetUnitAbilityLevel(unit, WorgenKnight.abilityId) > 0
        and GetPlayerTechCount(GetOwningPlayer(unit), WorgenKnight.researchId, true) > 0
end

function WorgenKnight.Spell()
    local caster = GetTriggerUnit()
    if caster == nil or GetUnitTypeId(caster) == 0 then return end
    local x, y, owner = GetUnitX(caster), GetUnitY(caster), GetOwningPlayer(caster)
    local group = CreateGroup()
    GroupEnumUnitsInRange(group, x, y, 600, nil)
    for i = 0, BlzGroupGetSize(group) - 1 do
        local knight = BlzGroupUnitAt(group, i)
        if WorgenKnight.Eligible(knight) and IsUnitEnemy(knight, owner) then
            local dx, dy = GetUnitX(knight) - x, GetUnitY(knight) - y
            if dx * dx + dy * dy <= 600 * 600 then
                SetUnitAbilityLevel(knight, WorgenKnight.abilityId, 2)
            end
        end
    end
    DestroyGroup(group)
end

function WorgenKnight.Damage()
    if not BlzGetEventIsAttack() or GetEventDamage() <= 0 then return end
    local knight = GetEventDamageSource()
    if not WorgenKnight.Eligible(knight)
        or GetUnitAbilityLevel(knight, WorgenKnight.abilityId) ~= 2 then return end
    local target = BlzGetEventDamageTarget()
    if target == nil or GetUnitTypeId(target) == 0
        or not IsUnitEnemy(target, GetOwningPlayer(knight)) then return end
    -- Modify the existing ordinary attack before armor; do not cause a nested damage event.
    SetUnitAbilityLevel(knight, WorgenKnight.abilityId, 1)
    BlzSetEventDamage(GetEventDamage() + 20)
end

function WorgenKnight.Reset()
    local unit = GetTriggerUnit()
    if unit ~= nil and GetUnitTypeId(unit) == WorgenKnight.unitId
        and GetUnitAbilityLevel(unit, WorgenKnight.abilityId) > 0 then
        SetUnitAbilityLevel(unit, WorgenKnight.abilityId, 1)
    end
end

function InitTrig_WorgenKnight()
    if WorgenKnight.initialized then return end
    WorgenKnight.initialized = true
    local spell = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
    TriggerAddAction(spell, WorgenKnight.Spell)
    local damage = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(damage, EVENT_PLAYER_UNIT_DAMAGING)
    TriggerAddAction(damage, WorgenKnight.Damage)
    local reset = CreateTrigger()
    TriggerRegisterAnyUnitEventBJ(reset, EVENT_PLAYER_UNIT_DEATH)
    TriggerRegisterAnyUnitEventBJ(reset, EVENT_PLAYER_UNIT_CHANGE_OWNER)
    TriggerAddAction(reset, WorgenKnight.Reset)
end
