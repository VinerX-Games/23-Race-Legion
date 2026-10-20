
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
    BearGrip.Init()
    gg_trg_IceTrollsStart=CreateTrigger()
    TriggerRegisterTimerEventSingle(gg_trg_IceTrollsStart, 0.01)
    TriggerAddAction(gg_trg_IceTrollsStart, Trig_IceTrollsStart_Actions)
end

-- A separate ensnare buff roots the victim without pausing attacks or spells.
BearGrip = {bears = {}, targets = {}}
do
    local G = BearGrip
    local ability, buff = FourCC('ABgr'), FourCC('BBgr')
    local function alive(u)
        return u ~= nil and GetUnitTypeId(u) ~= 0
            and GetUnitState(u, UNIT_STATE_LIFE) > 0.405
    end
    local function distanceSquared(x1, y1, x2, y2)
        return (x1 - x2) ^ 2 + (y1 - y2) ^ 2
    end

    function G.ValidTarget(bear, target)
        return alive(bear) and GetUnitTypeId(bear) == FourCC('n05V') and alive(target)
            and IsUnitEnemy(target, GetOwningPlayer(bear))
            and not IsUnitType(target, UNIT_TYPE_STRUCTURE)
            and not IsUnitType(target, UNIT_TYPE_MECHANICAL)
            and not IsUnitType(target, UNIT_TYPE_FLYING)
            and not IsUnitType(target, UNIT_TYPE_WARD)
            and not IsUnitHidden(bear) and not IsUnitPaused(bear) and not IsUnitLoaded(bear)
            and not IsUnitHidden(target) and not IsUnitPaused(target) and not IsUnitLoaded(target)
            and not BlzIsUnitInvulnerable(target)
            and G.bears[bear] == nil and G.targets[bear] == nil
            and G.targets[target] == nil and G.bears[target] == nil
            and GetUnitAbilityLevel(target, buff) == 0
            and distanceSquared(GetUnitX(bear), GetUnitY(bear), GetUnitX(target), GetUnitY(target)) <= 180 ^ 2
    end

    function G.Release(state)
        if state == nil or state.finished then return end
        state.finished = true
        G.bears[state.bear], G.targets[state.target] = nil, nil
        PauseTimer(state.timer)
        DestroyTimer(state.timer)
        if GetUnitTypeId(state.bear) ~= 0 then
            BlzSetUnitWeaponBooleanField(state.bear, UNIT_WEAPON_BF_ATTACKS_ENABLED, 0, state.attack0)
            BlzSetUnitWeaponBooleanField(state.bear, UNIT_WEAPON_BF_ATTACKS_ENABLED, 1, state.attack1)
        end
        if GetUnitTypeId(state.target) ~= 0 then UnitRemoveAbility(state.target, buff) end
        if GetUnitTypeId(state.dummy) ~= 0 then RemoveUnit(state.dummy) end
        if GetItemTypeId(state.probe) ~= 0 then RemoveItem(state.probe) end
    end

    function G.Tick(state)
        if state.finished then return end
        local bear, target = state.bear, state.target
        if not alive(bear) or not alive(target) or GetUnitTypeId(bear) ~= FourCC('n05V')
            or GetOwningPlayer(bear) ~= state.owner or GetOwningPlayer(target) ~= state.targetOwner
            or not IsUnitEnemy(target, GetOwningPlayer(bear))
            or IsUnitHidden(bear) or IsUnitHidden(target) or IsUnitPaused(bear) or IsUnitPaused(target)
            or IsUnitLoaded(bear) or IsUnitLoaded(target)
            or IsUnitType(target, UNIT_TYPE_FLYING) or BlzIsUnitInvulnerable(target)
            or GetUnitAbilityLevel(bear, ability) == 0 then
            G.Release(state)
            return
        end
        state.elapsed = state.elapsed + 0.03125
        local hasBuff = GetUnitAbilityLevel(target, buff) > 0
        if hasBuff then state.applied = true end
        if state.elapsed >= state.duration or (not hasBuff and (state.applied or state.elapsed >= 0.25)) then
            G.Release(state)
            return
        end
        if not hasBuff then return end
        local bx, by, tx, ty = GetUnitX(bear), GetUnitY(bear), GetUnitX(target), GetUnitY(target)
        -- Teleports and abrupt forced movement break the grip, never drag across portals.
        if distanceSquared(bx, by, state.bx, state.by) > 96 ^ 2
            or distanceSquared(tx, ty, state.tx, state.ty) > 96 ^ 2
            or distanceSquared(bx, by, tx, ty) > 256 ^ 2 then
            G.Release(state)
            return
        end
        local dx, dy = bx + state.offsetX - tx, by + state.offsetY - ty
        local distance = math.sqrt(dx * dx + dy * dy)
        if distance > 0.5 then
            local step = math.min(distance, 24)
            local nx, ny = tx + dx / distance * step, ty + dy / distance * step
            -- Sample terrain and probe dynamic pathing without stopping the victim's orders.
            for i = 1, 3 do
                if IsTerrainPathable(tx + (nx - tx) * i / 3, ty + (ny - ty) * i / 3,
                    PATHING_TYPE_WALKABILITY) then
                    G.Release(state)
                    return
                end
            end
            SetItemPosition(state.probe, nx, ny)
            if distanceSquared(GetItemX(state.probe), GetItemY(state.probe), nx, ny) > 1 then
                G.Release(state)
                return
            end
            -- SetUnitPosition cancels orders, which would prevent the victim fighting back.
            SetUnitX(target, nx)
            SetUnitY(target, ny)
        end
        state.bx, state.by, state.tx, state.ty = bx, by, GetUnitX(target), GetUnitY(target)
        if state.ai and state.elapsed >= state.nextMove then
            state.nextMove = state.elapsed + 0.5
            IssuePointOrder(bear, 'move', state.retreatX, state.retreatY)
        end
    end

    function G.Cast(bear, target)
        if not G.ValidTarget(bear, target) then return false end
        local bx, by, tx, ty = GetUnitX(bear), GetUnitY(bear), GetUnitX(target), GetUnitY(target)
        local dummy = CreateUnit(GetOwningPlayer(bear), FourCC('nBgr'), bx, by, 0)
        if dummy == nil then return false end
        local probe = CreateItem(FourCC('ratf'), tx, ty)
        if probe == nil then RemoveUnit(dummy); return false end
        SetItemVisible(probe, false)
        if not IssueTargetOrder(dummy, 'ensnare', target) then
            RemoveUnit(dummy)
            RemoveItem(probe)
            return false
        end
        local state = {bear = bear, target = target, dummy = dummy, probe = probe, owner = GetOwningPlayer(bear),
            targetOwner = GetOwningPlayer(target), bx = bx, by = by, tx = tx, ty = ty,
            offsetX = tx - bx, offsetY = ty - by, elapsed = 0, timer = CreateTimer(),
            duration = IsUnitType(target, UNIT_TYPE_HERO) and 1 or 5,
            attack0 = BlzGetUnitWeaponBooleanField(bear, UNIT_WEAPON_BF_ATTACKS_ENABLED, 0),
            attack1 = BlzGetUnitWeaponBooleanField(bear, UNIT_WEAPON_BF_ATTACKS_ENABLED, 1)}
        G.bears[bear], G.targets[target] = state, state
        BlzSetUnitWeaponBooleanField(bear, UNIT_WEAPON_BF_ATTACKS_ENABLED, 0, false)
        BlzSetUnitWeaponBooleanField(bear, UNIT_WEAPON_BF_ATTACKS_ENABLED, 1, false)
        TimerStart(state.timer, 0.03125, true, function() G.Tick(state) end)
        UnitDamageTarget(bear, target, 30, false, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_NORMAL,
            WEAPON_TYPE_WHOKNOWS)
        if state.finished then return true end
        if not alive(target) then G.Release(state); return true end
        if udg_AiControl and udg_AiControl[GetPlayerId(state.owner)] then
            local length = math.sqrt((tx - bx) ^ 2 + (ty - by) ^ 2)
            if length > 1 then
                state.ai, state.nextMove = true, 0.5
                state.retreatX, state.retreatY = bx - (tx - bx) / length * 350, by - (ty - by) / length * 350
                IssuePointOrder(bear, 'move', state.retreatX, state.retreatY)
            end
        end
        return true
    end

    function G.AiCast(bear, target)
        return G.ValidTarget(bear, target) and IssueTargetOrder(bear, 'ensnare', target)
    end

    function G.Init()
        if G.initialized then return end
        G.initialized = true
        local spell = CreateTrigger()
        TriggerRegisterAnyUnitEventBJ(spell, EVENT_PLAYER_UNIT_SPELL_EFFECT)
        TriggerAddAction(spell, function()
            if GetSpellAbilityId() ~= ability then return end
            local bear = GetTriggerUnit()
            if not G.Cast(bear, GetSpellTargetUnit()) then
                BlzEndUnitAbilityCooldown(bear, ability)
                DisplayTextToPlayer(GetOwningPlayer(bear), 0, 0,
                    '|cffef8173Хватка требует наземного вражеского бойца рядом. Здания и механизмы не подходят.|r')
            end
        end)
        local death = CreateTrigger()
        TriggerRegisterAnyUnitEventBJ(death, EVENT_PLAYER_UNIT_DEATH)
        TriggerAddAction(death, function()
            local unit = GetTriggerUnit()
            G.Release(G.bears[unit] or G.targets[unit])
        end)
    end
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
    TimerStart(udg_Timer_E_Glaz, 0.03, true, nil)
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
            SetUnitPolarLoc(udg_Caster_E_Glaz[udg_Cikl_E_Glaz], udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz], 60.00, GetUnitFacing(udg_Caster_E_Glaz[udg_Cikl_E_Glaz]))
            AddSpecialEffectLocBJ(udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz], "CosmicBall.mdx")
            DestroyEffectBJ(GetLastCreatedEffectBJ())
            ForGroupDestroy(GetUnitsInRangeOfLocAll(150.00, udg_To4kaCaster_E_Glaz[udg_Cikl_E_Glaz]), Trig_Spell_E_Dvij_Func001Func001Func007A)
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
    AddSpecialEffectLocBJ(udg_To4kaTarget, "Abilities\\Spells\\Other\\CrushingWave\\CrushingWaveDamage.mdl")
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
